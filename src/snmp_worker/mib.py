"""MIB knowledge: name <-> OID resolution, object metadata and value rendering.

The worker ships pre-compiled IETF/IANA/Net-SNMP MIB modules (``mibs/``, generated
with pysmi) on top of the modules bundled with pysnmp, so names such as
``ifInOctets`` or ``HOST-RESOURCES-MIB::hrStorageTable`` resolve offline. Extra
compiled modules can be added with the ``SNMP_MIB_DIRS`` environment variable
(an ``os.pathsep``-separated list of directories holding pysmi ``--destination-format
pysnmp`` output).

Everything here is loaded once per process, lazily, on first use.
"""

from __future__ import annotations

import ipaddress
import os
import re
import threading
from dataclasses import dataclass
from decimal import Decimal
from functools import cached_property
from pathlib import Path
from typing import Any

import pyarrow as pa
from pyasn1.type import univ
from pysnmp.proto import rfc1902, rfc1905
from pysnmp.smi import builder, view

MIB_DIR = Path(__file__).resolve().parent / "mibs"
MIB_DIRS_ENV_VAR = "SNMP_MIB_DIRS"

# When a bare symbol is defined by several modules, prefer the modern definition.
_DEPRIORITIZED_MODULES = {"RFC1213-MIB", "RFC1158-MIB", "RFC1155-SMI", "SNMPv2-SMI"}

OidTuple = tuple[int, ...]

_NODE_CLASSES = {
    "MibIdentifier",
    "ObjectIdentity",
    "ModuleIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
}

_NAME_RE = re.compile(r"^(?:(?P<module>[A-Za-z][\w-]*)::)?(?P<symbol>[A-Za-z][\w-]*)(?P<suffix>(?:\.\d+)*)$")
_NUMERIC_RE = re.compile(r"^\.?\d+(?:\.\d+)*$")


class MibError(ValueError):
    """A name or OID could not be resolved against the loaded MIBs."""


def oid_str(oid: OidTuple) -> str:
    """Render an OID tuple as dotted numbers."""
    return ".".join(str(x) for x in oid)


def parse_numeric_oid(text: str) -> OidTuple | None:
    """Parse ``1.3.6.1`` (optionally with a leading dot); None if it isn't numeric."""
    text = text.strip()
    if not _NUMERIC_RE.match(text):
        return None
    return tuple(int(x) for x in text.lstrip(".").split("."))


# ---------------------------------------------------------------- SNMP value types

# Wire types, keyed by ASN.1 tag set. Order matters: subtypes share tags with
# their base type (DisplayString is an OCTET STRING), and the first match wins.
_TYPE_NAMES: list[tuple[Any, str]] = [
    (rfc1905.NoSuchObject.tagSet, "noSuchObject"),
    (rfc1905.NoSuchInstance.tagSet, "noSuchInstance"),
    (rfc1905.EndOfMibView.tagSet, "endOfMibView"),
    (rfc1902.IpAddress.tagSet, "IpAddress"),
    (rfc1902.Counter32.tagSet, "Counter32"),
    (rfc1902.Gauge32.tagSet, "Gauge32"),
    (rfc1902.TimeTicks.tagSet, "TimeTicks"),
    (rfc1902.Opaque.tagSet, "Opaque"),
    (rfc1902.Counter64.tagSet, "Counter64"),
    (univ.Integer.tagSet, "INTEGER"),
    (univ.OctetString.tagSet, "OCTET STRING"),
    (univ.ObjectIdentifier.tagSet, "OBJECT IDENTIFIER"),
    (univ.Null.tagSet, "NULL"),
]

EXCEPTION_TYPES = {"noSuchObject", "noSuchInstance", "endOfMibView"}
_INTEGER_TYPES = {"INTEGER", "Counter32", "Gauge32", "TimeTicks", "Counter64"}


def wire_type(value: Any) -> str:
    """Name the SNMP wire type of a received value, e.g. ``Counter64`` or ``noSuchInstance``."""
    tag_set = value.tagSet
    for tags, name in _TYPE_NAMES:
        if tag_set == tags:
            return name
    return type(value).__name__


@dataclass(frozen=True, slots=True)
class RenderedValue:
    """A received value in the four shapes the generic functions return."""

    type: str
    text: str | None
    number: Decimal | None
    raw: bytes | None


_INET_ADDRESS_SYNTAXES = {"InetAddress", "InetAddressIPv4", "InetAddressIPv6", "IpAddress"}


def _pretty(syntax: Any, value: Any) -> str:
    """``prettyPrint`` through the MIB syntax when it accepts the value, else raw.

    INET-ADDRESS-MIB addresses are rendered as IPv4/IPv6 text when they are 4 or 16
    octets long; their MIB display hint depends on a sibling type column.
    """
    if syntax is not None and type(syntax).__name__ in _INET_ADDRESS_SYNTAXES:
        octets = bytes(value.asOctets())
        if len(octets) in (4, 16):
            return str(ipaddress.ip_address(octets))
    if syntax is not None:
        try:
            return str(syntax.clone(value).prettyPrint())
        except Exception:
            pass
    return str(value.prettyPrint())


def render_value(value: Any, syntax: Any | None) -> RenderedValue:
    """Render a received value: MIB-aware text, exact integer and raw octets."""
    kind = wire_type(value)
    if kind in EXCEPTION_TYPES or kind == "NULL":
        return RenderedValue(kind, None, None, None)
    if kind in _INTEGER_TYPES:
        number = int(value)
        return RenderedValue(kind, _pretty(syntax, value), Decimal(number), None)
    if kind == "OBJECT IDENTIFIER":
        return RenderedValue(kind, oid_str(tuple(value)), None, None)
    if kind == "IpAddress":
        octets = bytes(value.asOctets())
        return RenderedValue(kind, ".".join(str(b) for b in octets), None, octets)
    octets = bytes(value.asOctets())
    return RenderedValue(kind, _pretty(syntax, value), None, octets)


# ---------------------------------------------------------------- typed table columns


@dataclass(frozen=True, slots=True)
class ColumnKind:
    """How one MIB syntax maps to an Arrow column."""

    arrow_type: pa.DataType
    sql_type: str


_STRING = ColumnKind(pa.string(), "VARCHAR")
_INT64 = ColumnKind(pa.int64(), "BIGINT")
_UINT64 = ColumnKind(pa.uint64(), "UBIGINT")


def _is_enum(syntax: Any) -> bool:
    return isinstance(syntax, univ.Integer) and bool(getattr(syntax, "namedValues", None))


def column_kind(syntax: Any) -> ColumnKind:
    """Arrow type for a MIB object's syntax.

    Counter64 maps to UBIGINT, other integers to BIGINT, enumerations (INTEGER with
    named values, e.g. ``ifOperStatus``) to their label as VARCHAR, and everything
    else (strings, addresses, OIDs, BITS) to its display text.
    """
    if isinstance(syntax, rfc1902.Counter64):
        return _UINT64
    if _is_enum(syntax):
        return _STRING
    if isinstance(syntax, univ.Integer):  # Integer32, Unsigned32, Gauge32, Counter32, TimeTicks
        return _INT64
    return _STRING


def column_value(syntax: Any, value: Any) -> Any:
    """Convert a received value for a typed column (see `column_kind`); None for exceptions."""
    kind = wire_type(value)
    if kind in EXCEPTION_TYPES or kind == "NULL":
        return None
    target = column_kind(syntax)
    if target is _STRING:
        if _is_enum(syntax) and kind == "INTEGER":
            number = int(value)
            name = syntax.namedValues.getName(number)
            return str(name) if name is not None else str(number)
        if kind == "OBJECT IDENTIFIER":
            return oid_str(tuple(value))
        if kind == "IpAddress":
            return ".".join(str(b) for b in bytes(value.asOctets()))
        return _pretty(syntax, value)
    if kind in _INTEGER_TYPES:
        number = int(value)
        if target is _UINT64 and number < 0:
            return None
        return number
    # The agent sent a non-integer for an integer column: not representable.
    return None


# ---------------------------------------------------------------- the MIB view


@dataclass(frozen=True, slots=True)
class MibObject:
    """One named node from a loaded MIB module."""

    module: str
    name: str
    oid: OidTuple
    node: Any

    @property
    def kind(self) -> str:
        """``scalar``, ``table``, ``row``, ``column``, ``notification`` or ``node``."""
        cls = type(self.node).__name__
        return {
            "MibScalar": "scalar",
            "MibTable": "table",
            "MibTableRow": "row",
            "MibTableColumn": "column",
            "NotificationType": "notification",
        }.get(cls, "node")

    @property
    def syntax(self) -> Any | None:
        """The object's syntax instance, for scalars and columns."""
        get = getattr(self.node, "getSyntax", None)
        return get() if self.kind in ("scalar", "column") and get is not None else None

    @property
    def syntax_name(self) -> str | None:
        """Textual-convention or base type name, e.g. ``DisplayString`` or ``Counter64``."""
        syntax = self.syntax
        return None if syntax is None else type(syntax).__name__

    def _text(self, getter: str) -> str | None:
        get = getattr(self.node, getter, None)
        if get is None:
            return None
        text = get()
        return str(text) if text else None

    @property
    def access(self) -> str | None:
        """MAX-ACCESS, e.g. ``read-only``."""
        return self._text("getMaxAccess")

    @property
    def status(self) -> str | None:
        """STATUS, e.g. ``current`` or ``deprecated``."""
        return self._text("getStatus")

    @property
    def units(self) -> str | None:
        """UNITS clause, when the MIB declares one."""
        return self._text("getUnits")

    @property
    def description(self) -> str | None:
        """DESCRIPTION clause, whitespace-normalized."""
        text = self._text("getDescription")
        return " ".join(text.split()) if text else None


class Mibs:
    """All loaded MIB modules, with indexes for resolution."""

    def __init__(self) -> None:
        """Load the bundled, vendored and ``SNMP_MIB_DIRS`` modules."""
        self.builder = builder.MibBuilder()
        self.builder.loadTexts = True
        sources = [builder.DirMibSource(str(MIB_DIR))]
        for extra in os.environ.get(MIB_DIRS_ENV_VAR, "").split(os.pathsep):
            if extra.strip():
                sources.append(builder.DirMibSource(extra.strip()))
        # Later sources are searched first, so user directories override ours.
        self.builder.add_mib_sources(*sources)
        self.builder.load_modules()
        self.view = view.MibViewController(self.builder)

    @cached_property
    def objects(self) -> list[MibObject]:
        """Every named node in every loaded module, ordered by module then OID."""
        found: list[MibObject] = []
        for module, symbols in self.builder.mibSymbols.items():
            # "__X" modules are pysnmp's agent-side instances; PYSNMP-* are its own internals.
            if module.startswith(("__", "PYSNMP-")):
                continue
            for name, node in symbols.items():
                oid = getattr(node, "name", None)
                if type(node).__name__ not in _NODE_CLASSES or not isinstance(oid, tuple) or not oid:
                    continue
                found.append(MibObject(module, name, tuple(int(x) for x in oid), node))
        found.sort(key=lambda o: (o.module, o.oid))
        return found

    @cached_property
    def _by_name(self) -> dict[str, list[MibObject]]:
        index: dict[str, list[MibObject]] = {}
        for obj in self.objects:
            index.setdefault(obj.name, []).append(obj)
        for candidates in index.values():
            candidates.sort(key=lambda o: o.module in _DEPRIORITIZED_MODULES)
        return index

    @cached_property
    def _by_oid(self) -> dict[OidTuple, MibObject]:
        index: dict[OidTuple, MibObject] = {}
        for obj in self.objects:
            current = index.get(obj.oid)
            if current is None or (
                current.module in _DEPRIORITIZED_MODULES and obj.module not in _DEPRIORITIZED_MODULES
            ):
                index[obj.oid] = obj
        # An OBJECT-IDENTITY naming an instance (DISMAN-EVENT-MIB::sysUpTimeInstance is
        # sysUpTime.0) would hide the scalar it belongs to; name such OIDs by the scalar.
        for oid in [o for o, obj in index.items() if obj.kind == "node"]:
            parent = index.get(oid[:-1])
            if parent is not None and parent.kind in ("scalar", "column"):
                del index[oid]
        return index

    def lookup(self, name: str, module: str | None = None) -> MibObject | None:
        """Find the object a symbol names, optionally qualified by its module."""
        for obj in self._by_name.get(name, []):
            if module is None or obj.module == module:
                return obj
        return None

    def resolve(self, text: str) -> OidTuple:
        """Resolve ``1.3.6.1...``, ``sysDescr.0`` or ``IF-MIB::ifInOctets.3`` to an OID.

        Args:
            text: Numeric OID or MIB name with an optional instance suffix.

        Returns:
            The numeric OID.

        Raises:
            MibError: The text is neither a numeric OID nor a known symbol.

        """
        numeric = parse_numeric_oid(text)
        if numeric is not None:
            return numeric
        match = _NAME_RE.match(text.strip())
        if match is None:
            raise MibError(f"not an OID or MIB name: {text!r} (expected e.g. '1.3.6.1.2.1.1.1.0' or 'sysDescr.0')")
        module, symbol, suffix = match.group("module"), match.group("symbol"), match.group("suffix")
        obj = self.lookup(symbol, module)
        if obj is None:
            where = f" in module {module}" if module else ""
            raise MibError(
                f"unknown MIB object {symbol!r}{where}; use a numeric OID, or add the compiled MIB "
                f"directory to {MIB_DIRS_ENV_VAR}"
            )
        return obj.oid + tuple(int(x) for x in suffix.lstrip(".").split(".") if x)

    def locate(self, oid: OidTuple) -> tuple[MibObject | None, OidTuple]:
        """Find the deepest named object at or above ``oid``, and the remaining instance suffix."""
        for depth in range(len(oid), 0, -1):
            obj = self._by_oid.get(oid[:depth])
            if obj is not None:
                return obj, oid[depth:]
        return None, oid

    def name_of(self, oid: OidTuple) -> str | None:
        """``MODULE::symbol.suffix`` for an OID, or None when nothing above it is named."""
        obj, suffix = self.locate(oid)
        if obj is None:
            return None
        rest = "".join(f".{x}" for x in suffix)
        return f"{obj.module}::{obj.name}{rest}"

    def syntax_for(self, oid: OidTuple) -> Any | None:
        """Return the syntax of the scalar or column an instance OID belongs to."""
        obj, suffix = self.locate(oid)
        if obj is None or not suffix:
            return None
        return obj.syntax

    def table(self, text: str) -> MibTable:
        """Find the conceptual table a name refers to: the table, its entry, or a column of it.

        Args:
            text: Table, entry or column name, or a numeric OID.

        Returns:
            The table with its entry, columns and INDEX objects.

        Raises:
            MibError: The name is unknown or isn't part of a table.

        """
        oid = self.resolve(text)
        obj = self._by_oid.get(oid)
        if obj is None:
            raise MibError(f"{text!r} is not a MIB object known to this worker; use snmp_walk instead")
        if obj.kind == "table":
            row = next((o for o in self.objects if o.kind == "row" and o.oid[:-1] == obj.oid), None)
        elif obj.kind == "row":
            row = obj
        elif obj.kind == "column":
            row = self._by_oid.get(obj.oid[:-1])
        else:
            row = None
        if row is None:
            raise MibError(f"{text!r} is a {obj.kind}, not a table; use snmp_get or snmp_walk instead")
        table = self._by_oid.get(row.oid[:-1])
        columns = sorted(
            (o for o in self._by_oid.values() if o.kind == "column" and o.oid[:-1] == row.oid),
            key=lambda o: o.oid,
        )
        index_objects: list[MibObject] = []
        for _implied, module, name in row.node.getIndexNames():
            index_obj = self.lookup(name, module)
            if index_obj is not None:
                index_objects.append(index_obj)
        return MibTable(
            table=table if table is not None else row,
            row=row,
            columns=columns,
            index=index_objects,
        )


@dataclass(frozen=True, slots=True)
class MibTable:
    """A conceptual table: its entry row, columns in OID order, and INDEX objects."""

    table: MibObject
    row: MibObject
    columns: list[MibObject]
    index: list[MibObject]

    def decode_index(self, suffix: OidTuple) -> list[Any] | None:
        """Decode an instance suffix into the INDEX objects' values; None if it doesn't parse."""
        if not self.index:
            return None
        try:
            values = self.row.node.getIndicesFromInstId(suffix)
        except Exception:
            return None
        if len(values) != len(self.index):
            return None
        return list(values)


_MIBS: Mibs | None = None
_LOCK = threading.Lock()


def mibs() -> Mibs:
    """Return the process-wide MIB view, loading it on first use."""
    global _MIBS
    if _MIBS is None:
        with _LOCK:
            if _MIBS is None:
                _MIBS = Mibs()
    return _MIBS
