"""Offline scalars: ``snmp_oid(name)`` and ``snmp_oid_name(oid)``."""

from __future__ import annotations

import json
from typing import Annotated

import pyarrow as pa
from vgi.arguments import Param, Returns
from vgi.metadata import FunctionExample
from vgi.scalar_function import ScalarFunction

from .meta import object_tags
from .mib import MibError, mibs, oid_str


def to_oid(values: list[str | None]) -> list[str | None]:
    """Numeric OID for each name; None for NULL or unresolvable input."""
    table = mibs()
    out: list[str | None] = []
    for text in values:
        if text is None:
            out.append(None)
            continue
        try:
            out.append(oid_str(table.resolve(text)))
        except MibError:
            out.append(None)
    return out


def to_name(values: list[str | None]) -> list[str | None]:
    """``MODULE::object.instance`` for each numeric OID; None for NULL, malformed or unnamed OIDs."""
    from .mib import parse_numeric_oid

    table = mibs()
    out: list[str | None] = []
    for text in values:
        oid = parse_numeric_oid(text) if text is not None else None
        out.append(None if oid is None else table.name_of(oid))
    return out


class SnmpOid(ScalarFunction):
    """``snmp_oid(name)``: resolve a MIB name to its numeric OID."""

    class Meta:
        """Function metadata surfaced to DuckDB, agents and vgi-lint."""

        name = "snmp_oid"
        description = "Resolve a MIB name such as 'IF-MIB::ifInOctets.3' to its numeric OID"
        tags = {
            **object_tags(
                title="MIB Name to OID",
                category="mib",
                keywords="oid, translate, snmptranslate, mib name, numeric oid, resolve",
                doc_llm=(
                    "Translate a MIB name to a dotted numeric OID, offline, like `snmptranslate -On`. "
                    "Accepts 'sysDescr', 'sysDescr.0', 'IF-MIB::ifInOctets.3' or an already numeric OID "
                    "(returned normalized without a leading dot). Returns NULL for NULL input and for "
                    "names not in the loaded MIBs. Vectorized: works over a column of names."
                ),
                doc_md=(
                    "## snmp_oid(name)\n\n"
                    "`snmp_oid('IF-MIB::ifInOctets.3')` returns `'1.3.6.1.2.1.2.2.1.10.3'`. NULL for "
                    "unknown names."
                ),
            ),
            "vgi.executable_examples": json.dumps(
                [
                    {
                        "description": "Resolve a column instance",
                        "sql": "SELECT snmp.main.snmp_oid('IF-MIB::ifInOctets.3') AS oid",
                        "expected_result": [["1.3.6.1.2.1.2.2.1.10.3"]],
                    },
                    {
                        "description": "Resolve system group scalars",
                        "sql": (
                            "SELECT n, snmp.main.snmp_oid(n) AS oid FROM (VALUES ('sysDescr.0'), ('sysUpTime.0')) "
                            "t(n) ORDER BY n"
                        ),
                        "expected_result": [["sysDescr.0", "1.3.6.1.2.1.1.1.0"], ["sysUpTime.0", "1.3.6.1.2.1.1.3.0"]],
                    },
                ]
            ),
        }
        examples = [
            FunctionExample(
                sql="SELECT snmp.main.snmp_oid('IF-MIB::ifHCInOctets') AS oid",
                description="The numeric OID of the 64-bit input octet counter column",
            ),
            FunctionExample(
                sql=(
                    "SELECT n, snmp.main.snmp_oid(n) AS oid "
                    "FROM (VALUES ('sysName.0'), ('hrStorageUsed'), ('notAnObject')) t(n) ORDER BY n"
                ),
                description="Resolve a column of names; unknown names give NULL",
            ),
        ]

    @classmethod
    def compute(
        cls,
        name: Annotated[
            pa.StringArray, Param(doc="MIB name, optionally 'MODULE::' qualified with an instance suffix.")
        ],
    ) -> Annotated[pa.StringArray, Returns()]:
        """Resolve every name in the column."""
        return pa.array(to_oid(name.to_pylist()), type=pa.string())


class SnmpOidName(ScalarFunction):
    """``snmp_oid_name(oid)``: the MIB name of a numeric OID."""

    class Meta:
        """Function metadata surfaced to DuckDB, agents and vgi-lint."""

        name = "snmp_oid_name"
        description = "Name a numeric OID, e.g. '1.3.6.1.2.1.1.3.0' becomes 'SNMPv2-MIB::sysUpTime.0'"
        tags = {
            **object_tags(
                title="OID to MIB Name",
                category="mib",
                keywords="oid, translate, snmptranslate, mib name, symbolic name, decode oid",
                doc_llm=(
                    "Translate a dotted numeric OID to 'MODULE::object.instance' using the loaded MIBs, "
                    "offline. The deepest named ancestor is used, so an unknown vendor OID still gets a "
                    "prefix such as 'SNMPv2-SMI::enterprises.9.1.1'. Returns NULL for NULL, non-numeric "
                    "input, or OIDs outside every loaded MIB."
                ),
                doc_md=(
                    "## snmp_oid_name(oid)\n\n"
                    "`snmp_oid_name('1.3.6.1.2.1.2.2.1.10.3')` returns `'IF-MIB::ifInOctets.3'`."
                ),
            ),
            "vgi.executable_examples": json.dumps(
                [
                    {
                        "description": "Name an interface counter instance",
                        "sql": "SELECT snmp.main.snmp_oid_name('1.3.6.1.2.1.2.2.1.10.3') AS name",
                        "expected_result": [["IF-MIB::ifInOctets.3"]],
                    },
                ]
            ),
        }
        examples = [
            FunctionExample(
                sql="SELECT snmp.main.snmp_oid_name('1.3.6.1.2.1.1.3.0') AS name",
                description="Name the sysUpTime instance",
            ),
            FunctionExample(
                sql=(
                    "SELECT oid, snmp.main.snmp_oid_name(oid) AS name "
                    "FROM (VALUES ('1.3.6.1.2.1.25.2.3.1.6.1'), ('1.3.6.1.4.1.9.1.1')) t(oid) ORDER BY oid"
                ),
                description="Name a column of OIDs, including an unknown vendor OID",
            ),
        ]

    @classmethod
    def compute(
        cls,
        oid: Annotated[pa.StringArray, Param(doc="Numeric OID in dotted form, for example 1.3.6.1.2.1.1.3.0.")],
    ) -> Annotated[pa.StringArray, Returns()]:
        """Name every OID in the column."""
        return pa.array(to_name(oid.to_pylist()), type=pa.string())
