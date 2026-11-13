"""``snmp_walk(host, oid)``: every instance under a subtree, streamed in batches."""

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
    TableFunctionGenerator,
    init_single_worker,
)
from vgi_rpc import ArrowSerializableDataclass

from .client import SnmpError, is_end, is_exception
from .common import (
    MAX_REPETITIONS,
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
from .mib import OidTuple, mibs, oid_str, parse_numeric_oid

BATCH_ROWS = 2_000


@dataclass(slots=True, frozen=True, kw_only=True)
class WalkArgs(ConnectionArgs):
    """Arguments for ``snmp_walk(host, oid, max_repetitions := 25)``."""

    oid: Annotated[
        str,
        Arg(
            1,
            doc=("Root of the subtree to walk: a MIB name such as IF-MIB::ifTable, or a dotted numeric OID."),
        ),
    ]
    max_repetitions: Annotated[
        int,
        Arg(
            "max_repetitions",
            default=MAX_REPETITIONS,
            doc="Instances requested per GETBULK (v2c/v3), 1 to 200; ignored for v1, which uses GETNEXT.",
            ge=1,
            le=200,
        ),
    ]


@dataclass(kw_only=True)
class WalkState(ArrowSerializableDataclass):
    """Cursor: the last OID returned (dotted), or empty before the first request."""

    last: str = ""
    done: bool = False
    emitted: bool = False


def _in_subtree(oid: OidTuple, root: OidTuple) -> bool:
    return oid[: len(root)] == root and len(oid) > len(root)


@init_single_worker
class SnmpWalk(TableFunctionGenerator[WalkArgs, WalkState]):
    """Walk a subtree with GETBULK (v2c/v3) or GETNEXT (v1), one row per instance."""

    FIXED_SCHEMA: ClassVar[pa.Schema] = VARBIND_SCHEMA

    class Meta:
        """Function metadata surfaced to DuckDB, agents and vgi-lint."""

        name = "snmp_walk"
        description = "Walk an SNMP subtree (GETBULK/GETNEXT) and return every instance under it"
        tags = {
            **object_tags(
                title="SNMP Walk",
                category="snmp",
                keywords="snmp walk, snmpwalk, snmpbulkwalk, getbulk, getnext, subtree, mib, interfaces",
                doc_llm=(
                    "Walk every instance below the subtree `oid` on the agent at `host` and return one row "
                    "per instance, in OID order: `host, oid, name, object, instance, type, value, "
                    "value_int, value_bytes`. `oid` is numeric or a MIB name without instance suffix "
                    "('system', 'ifTable', 'ifHCInOctets', 'hrStorageTable'). Rows stream in batches, so "
                    "LIMIT stops the walk early. Uses GETBULK with `max_repetitions` (named, default 25) "
                    "on v2c/v3 and GETNEXT on v1. Use snmp_table instead when you want one row per table "
                    "row with typed columns; use snmp_walk for raw subtrees, vendor MIBs this worker does "
                    "not know, or discovery. " + CONNECTION_DOC_LLM
                ),
                doc_md=(
                    "## snmp_walk(host, oid, max_repetitions := 25)\n\n"
                    "Every instance under a subtree, like `snmpbulkwalk`.\n\n"
                    "Rows stream in OID order, so `LIMIT` ends the walk early.\n\n" + CONNECTION_DOC_MD
                ),
            ),
            "vgi.result_columns_schema": json.dumps(VARBIND_COLUMNS_JSON),
        }
        examples = [
            FunctionExample(
                sql=(
                    "SELECT instance AS if_index, value AS interface "
                    "FROM snmp.main.snmp_walk('192.0.2.10', 'ifDescr') ORDER BY value_int NULLS LAST, instance"
                ),
                description="List interface names by ifIndex",
            ),
            FunctionExample(
                sql=(
                    "SELECT object, count(*) AS instances FROM snmp.main.snmp_walk('192.0.2.10', 'mib-2') "
                    "GROUP BY object ORDER BY instances DESC LIMIT 10"
                ),
                description="Which MIB-2 objects does a device populate most?",
            ),
        ]

    @classmethod
    def on_bind(cls, params: BindParams[WalkArgs]) -> BindResponse:
        """Validate the root OID offline and request the target's ``snmp`` secret."""
        resolve_oid(mibs(), params.args.oid)
        request_secret(params)
        return BindResponse(output_schema=VARBIND_SCHEMA)

    @classmethod
    def initial_state(cls, params: ProcessParams[WalkArgs]) -> WalkState:
        """Start at the subtree root."""
        return WalkState()

    @classmethod
    def process(cls, params: ProcessParams[WalkArgs], state: WalkState, out: OutputCollector) -> None:
        """Request successors until a batch is full or the walk leaves the subtree."""
        if state.done:
            out.finish()
            return
        table = mibs()
        root = resolve_oid(table, params.args.oid)
        cursor = parse_numeric_oid(state.last) if state.last else root
        assert cursor is not None
        session = open_session(params.args, params.secrets)
        rows: list[tuple[OidTuple, object]] = []
        while len(rows) < BATCH_ROWS and not state.done:
            (binds,) = session.next_rows([cursor], params.args.max_repetitions)
            if not binds:
                state.done = True
                break
            for oid, value in binds:
                if is_end(value) or not _in_subtree(oid, root):
                    state.done = True
                    break
                if oid <= cursor:
                    raise SnmpError(
                        f"{session.target}: agent returned OIDs out of order ({oid_str(oid)} after "
                        f"{oid_str(cursor)}); stopping to avoid an endless walk"
                    )
                rows.append((oid, value))
                cursor = oid
        state.last = oid_str(cursor)
        if state.done and not rows and not state.emitted:
            # Like snmpwalk: a root that is itself an instance (e.g. 'sysUpTime.0') is fetched with GET.
            ((oid, value),) = session.get([root])
            if not is_exception(value):
                rows.append((oid, value))
        if rows:
            state.emitted = True
            out.emit(project(varbind_rows(table, params.args.host, rows), params.output_schema))
        if state.done and not rows:
            out.finish()
