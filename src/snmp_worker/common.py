"""Arguments and helpers shared by the SNMP table functions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Annotated, Any, Protocol

import pyarrow as pa
from vgi.arguments import Arg

from .client import SECRET_TYPE as SECRET_TYPE
from .client import VERSIONS, Session, SnmpError, parse_target, resolve_credentials
from .meta import column
from .mib import Mibs, OidTuple, oid_str, render_value

MAX_REPETITIONS = 25


@dataclass(slots=True, frozen=True, kw_only=True)
class ConnectionArgs:
    """Named arguments every SNMP table function accepts."""

    host: Annotated[
        str,
        Arg(0, doc="Agent address: 'host', 'host:port', an IPv4/IPv6 address or '[v6addr]:port'.", pattern=r"\S"),
    ]
    version: Annotated[
        str | None,
        Arg(
            "version",
            default=None,
            doc="SNMP version: '1', '2c' or '3'. Default: '3' when a v3 user is configured, else '2c'.",
            choices=VERSIONS,
        ),
    ]
    community: Annotated[
        str | None,
        Arg(
            "community",
            default=None,
            doc="v1/v2c community. Default: the snmp secret, then SNMP_COMMUNITY, then 'public'.",
        ),
    ]
    port: Annotated[int | None, Arg("port", default=None, doc="UDP port; default 161.", ge=1, le=65535)]
    timeout: Annotated[
        float, Arg("timeout", default=2.0, doc="Seconds to wait for each response, 0.1 to 60.", ge=0.1, le=60.0)
    ]
    retries: Annotated[int, Arg("retries", default=1, doc="Retransmissions after a timeout, 0 to 10.", ge=0, le=10)]
    context: Annotated[str, Arg("context", default="", doc="SNMPv3 context name; empty for the default context.")]


class _Secrets(Protocol):
    def lookup(self, secret_type: str, *, name: str | None = ..., scope: str | None = ...) -> dict[str, Any] | None: ...


def request_secret(params: Any) -> None:
    """At bind: ask DuckDB for the ``snmp`` secret scoped to this target."""
    target = parse_target(params.args.host, params.args.port)
    params.secrets.get(SECRET_TYPE, scope=target.scope)


def open_session(args: ConnectionArgs, secrets: _Secrets) -> Session:
    """Build a session from the arguments and the secret resolved for the target."""
    target = parse_target(args.host, args.port)
    secret = secrets.lookup(SECRET_TYPE, scope=target.scope)
    credentials = resolve_credentials(version=args.version, community=args.community, secret=secret)
    return Session(
        target=target, credentials=credentials, timeout=args.timeout, retries=args.retries, context=args.context
    )


def resolve_oid(mibs: Mibs, text: str) -> OidTuple:
    """Resolve a name or OID argument, as an SnmpError."""
    try:
        return mibs.resolve(text)
    except ValueError as err:
        raise SnmpError(str(err)) from err


# ---------------------------------------------------------------- varbind rows

VARBIND_SCHEMA = pa.schema(
    [
        column("host", pa.string(), "The agent queried, as given in the host argument.", nullable=False),
        column("oid", pa.string(), "Numeric OID of the returned instance, e.g. '1.3.6.1.2.1.1.1.0'.", nullable=False),
        column("name", pa.string(), "Symbolic name from the loaded MIBs, e.g. 'SNMPv2-MIB::sysDescr.0'."),
        column("object", pa.string(), "The MIB object the instance belongs to, e.g. 'ifInOctets'."),
        column("instance", pa.string(), "Instance suffix after the object's OID, e.g. '3' or '0'."),
        column(
            "type", pa.string(), "SNMP type: INTEGER, OCTET STRING, Counter64, ..., or noSuchObject.", nullable=False
        ),
        column("value", pa.string(), "Display value, formatted by the MIB (enum labels, MAC addresses, text)."),
        column(
            "value_int",
            pa.decimal128(20, 0),
            "Exact value of integer types (INTEGER, Counter32/64, Gauge32, TimeTicks).",
        ),
        column("value_bytes", pa.binary(), "Raw octets of OCTET STRING, Opaque and IpAddress values."),
    ]
)

VARBIND_COLUMNS_JSON = [
    {"name": "host", "type": "VARCHAR", "description": "The agent queried, as given in the host argument."},
    {"name": "oid", "type": "VARCHAR", "description": "Numeric OID of the returned instance."},
    {
        "name": "name",
        "type": "VARCHAR",
        "description": "Symbolic name from the loaded MIBs, e.g. 'SNMPv2-MIB::sysDescr.0'.",
    },
    {"name": "object", "type": "VARCHAR", "description": "The MIB object the instance belongs to, e.g. 'ifInOctets'."},
    {"name": "instance", "type": "VARCHAR", "description": "Instance suffix after the object's OID, e.g. '3'."},
    {"name": "type", "type": "VARCHAR", "description": "SNMP type, or noSuchObject / noSuchInstance."},
    {"name": "value", "type": "VARCHAR", "description": "Display value formatted by the MIB."},
    {"name": "value_int", "type": "DECIMAL(20,0)", "description": "Exact value of integer types."},
    {"name": "value_bytes", "type": "BLOB", "description": "Raw octets of string-like values."},
]


def varbind_rows(mibs: Mibs, host: str, binds: list[tuple[OidTuple, Any]]) -> dict[str, list[Any]]:
    """Columns of VARBIND_SCHEMA for a list of (oid, value) pairs."""
    cols: dict[str, list[Any]] = {f.name: [] for f in VARBIND_SCHEMA}
    for oid, value in binds:
        obj, suffix = mibs.locate(oid)
        syntax = obj.syntax if obj is not None and suffix else None
        rendered = render_value(value, syntax)
        cols["host"].append(host)
        cols["oid"].append(oid_str(oid))
        cols["name"].append(None if obj is None else f"{obj.module}::{obj.name}" + "".join(f".{x}" for x in suffix))
        cols["object"].append(None if obj is None else obj.name)
        cols["instance"].append(oid_str(suffix) if obj is not None and suffix else None)
        cols["type"].append(rendered.type)
        cols["value"].append(rendered.text)
        cols["value_int"].append(rendered.number)
        cols["value_bytes"].append(rendered.raw)
    return cols


def project(cols: dict[str, list[Any]], schema: pa.Schema) -> pa.RecordBatch:
    """Build a batch with only the columns in ``schema`` (the projected output)."""
    return pa.RecordBatch.from_pydict({f.name: cols[f.name] for f in schema}, schema=schema)
