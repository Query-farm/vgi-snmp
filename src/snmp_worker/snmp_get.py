"""``snmp_get(host, oid, ...)``: SNMP GET of one or more instances."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Annotated, ClassVar

import pyarrow as pa
from vgi.arguments import Arg
from vgi.invocation import BindResponse
from vgi.metadata import FunctionExample
from vgi.table_function import (
    BindParams,
    OutputCollector,
    ProcessParams,
    TableCardinality,
    TableFunctionGenerator,
    init_single_worker,
)
from vgi_rpc import ArrowSerializableDataclass

from .client import SnmpError
from .common import (
    VARBIND_COLUMNS_JSON,
    VARBIND_SCHEMA,
    ConnectionArgs,
    open_session,
    project,
    request_secret,
    resolve_oid,
    varbind_rows,
)
from .meta import CONNECTION_DOC_LLM, CONNECTION_DOC_MD, object_tags
from .mib import mibs


@dataclass(slots=True, frozen=True, kw_only=True)
class GetArgs(ConnectionArgs):
    """Arguments for ``snmp_get(host, oid, ...)``."""

    oids: Annotated[
        list[str],
        Arg(
            1,
            varargs=True,
            arrow_type=pa.string(),
            doc=(
                "Instance OIDs to read, each a dotted numeric OID or a MIB name with its instance "
                "suffix, for example sysUpTime.0 or IF-MIB::ifInOctets.2."
            ),
        ),
    ]


def oid_texts(args: GetArgs) -> list[str]:
    """Return the OID arguments as strings (varargs arrive as Arrow scalars)."""
    out: list[str] = []
    for value in args.oids:
        py = value.as_py() if hasattr(value, "as_py") else value
        if py is None:
            raise SnmpError("OID arguments must not be NULL")
        out.append(str(py))
    return out


@dataclass(kw_only=True)
class GetState(ArrowSerializableDataclass):
    """Cursor: whether the single response has been emitted."""

    done: bool = False


@init_single_worker
class SnmpGet(TableFunctionGenerator[GetArgs, GetState]):
    """GET the listed instances from one agent: one row per requested OID, in argument order."""

    FIXED_SCHEMA: ClassVar[pa.Schema] = VARBIND_SCHEMA

    class Meta:
        """Function metadata surfaced to DuckDB, agents and vgi-lint."""

        name = "snmp_get"
        description = "Read specific SNMP instances (GET) from an agent, one row per OID"
        tags = {
            **object_tags(
                title="SNMP GET",
                category="snmp",
                keywords="snmp get, snmpget, oid, sysDescr, sysUpTime, read value, network device, monitoring",
                doc_llm=(
                    "Send one SNMP GET to the agent at `host` for every OID listed after it and return one "
                    "row per OID, in argument order: `host, oid, name, object, instance, type, value, "
                    "value_int, value_bytes`. OIDs are numeric ('1.3.6.1.2.1.1.5.0') or MIB names with an "
                    "instance suffix ('sysName.0', 'IF-MIB::ifHCInOctets.2'); scalars need the '.0' suffix. "
                    "A missing object is a row with type 'noSuchObject' or 'noSuchInstance' and NULL "
                    "values, not an error. Use `value` for display text (enum labels, MAC addresses), "
                    "`value_int` for arithmetic on counters/gauges/TimeTicks (TimeTicks are hundredths of "
                    "a second). " + CONNECTION_DOC_LLM
                ),
                doc_md=(
                    "## snmp_get(host, oid, ...)\n\n"
                    "One row per requested instance. Missing instances come back as `noSuchObject` / "
                    "`noSuchInstance` rows.\n\n"
                    "Scalars need the `.0` instance suffix: `sysName.0`, not `sysName`.\n\n" + CONNECTION_DOC_MD
                ),
            ),
            "vgi.result_columns_schema": json.dumps(VARBIND_COLUMNS_JSON),
        }
        examples = [
            FunctionExample(
                sql=(
                    "SELECT object, value FROM snmp.main.snmp_get('192.0.2.10', 'sysName.0', 'sysDescr.0', "
                    "'sysLocation.0') ORDER BY object"
                ),
                description="Identify a device by its system group",
            ),
            FunctionExample(
                sql=(
                    "SELECT round(value_int / 8640000.0, 1) AS uptime_days "
                    "FROM snmp.main.snmp_get('192.0.2.10', 'sysUpTime.0', community := 'monitor')"
                ),
                description="Uptime in days from sysUpTime (hundredths of a second)",
            ),
        ]

    @classmethod
    def on_bind(cls, params: BindParams[GetArgs]) -> BindResponse:
        """Validate the OIDs offline and request the target's ``snmp`` secret."""
        table = mibs()
        for text in oid_texts(params.args):
            resolve_oid(table, text)
        request_secret(params)
        return BindResponse(output_schema=VARBIND_SCHEMA)

    @classmethod
    def cardinality(cls, params: BindParams[GetArgs]) -> TableCardinality:
        """Exactly one row per requested OID."""
        return TableCardinality(estimate=len(params.args.oids), max=len(params.args.oids))

    @classmethod
    def initial_state(cls, params: ProcessParams[GetArgs]) -> GetState:
        """Nothing sent yet."""
        return GetState()

    @classmethod
    def process(cls, params: ProcessParams[GetArgs], state: GetState, out: OutputCollector) -> None:
        """Send the GET (split as needed) and emit every result as one batch."""
        if state.done:
            out.finish()
            return
        table = mibs()
        oids = [resolve_oid(table, text) for text in oid_texts(params.args)]
        session = open_session(params.args, params.secrets)
        binds = session.get(oids)
        out.emit(project(varbind_rows(table, params.args.host, binds), params.output_schema))
        state.done = True
