"""``snmp_table(host, table)``: a MIB conceptual table as typed rows.

The output schema comes from the MIB at bind time, with no network traffic: one column
per accessible columnar object (``ifDescr``, ``ifHCInOctets``, ...), plus the decoded
INDEX objects and the raw instance suffix ``_index``. Only the projected columns are
walked, so ``SELECT ifDescr FROM snmp_table(..., 'ifXTable')`` reads one column.

Columns are walked side by side with multi-varbind GETBULK. A row is emitted once every
walked column has moved past its index, so the scan streams and the cursor that crosses
HTTP requests stays small: the per-column positions plus rows still being assembled.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Annotated, Any, cast

import pyarrow as pa
from pyasn1.type import univ
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

from .client import SnmpError, is_end
from .common import MAX_REPETITIONS, ConnectionArgs, open_session, request_secret
from .meta import CONNECTION_DOC_LLM, CONNECTION_DOC_MD, column, object_tags
from .mib import MibError, MibObject, MibTable, OidTuple, column_kind, column_value, mibs, oid_str, parse_numeric_oid

BATCH_ROWS = 2_000
INDEX_COLUMN = "_index"
_READABLE = {"read-only", "read-write", "read-create"}
_DONE = "~"


@dataclass(slots=True, frozen=True, kw_only=True)
class TableArgs(ConnectionArgs):
    """Arguments for ``snmp_table(host, table, max_repetitions := 25)``."""

    mib_table: Annotated[
        str,
        Arg(
            1,
            doc=("MIB table to read, for example IF-MIB::ifXTable."),
        ),
    ]
    max_repetitions: Annotated[
        int,
        Arg(
            "max_repetitions",
            default=MAX_REPETITIONS,
            doc="Rows requested per GETBULK (v2c/v3), 1 to 200; ignored for v1.",
            ge=1,
            le=200,
        ),
    ]


@dataclass(kw_only=True)
class TableState(ArrowSerializableDataclass):
    """Cursor: per walked column, the last instance seen (``~`` once finished), and unfinished rows."""

    cursors: list[str]
    pending: str = "{}"
    started: bool = False


def _comment(obj: MibObject) -> str:
    text = obj.description or obj.name
    first = text.split(". ")[0].rstrip(".")
    if len(first) > 240:
        first = first[:237] + "..."
    units = f" Units: {obj.units}." if obj.units else ""
    labels = ""
    named = getattr(obj.syntax, "namedValues", None)
    if isinstance(obj.syntax, univ.Integer) and named:
        labels = " Values: " + ", ".join(str(name) for name in named) + "."
    return f"{obj.module}::{obj.name} ({obj.syntax_name}). {first}.{units}{labels}"


def readable_columns(mt: MibTable) -> list[MibObject]:
    """Columns an agent can be asked for, excluding INDEX objects (decoded from the instance)."""
    index_names = {o.name for o in mt.index}
    return [c for c in mt.columns if c.access in _READABLE and c.name not in index_names]


def table_schema(mt: MibTable) -> pa.Schema:
    """``_index``, then the INDEX objects, then the readable columns in OID order."""
    fields = [
        column(
            INDEX_COLUMN,
            pa.string(),
            "Instance suffix that identifies the row, e.g. '3' or '1.4.192.0.2.1'.",
            nullable=False,
        )
    ]
    for obj in [*mt.index, *readable_columns(mt)]:
        fields.append(column(obj.name, column_kind(obj.syntax).arrow_type, _comment(obj)))
    return pa.schema(fields)


def _table(args: TableArgs) -> MibTable:
    try:
        return mibs().table(args.mib_table)
    except MibError as err:
        raise SnmpError(str(err)) from err


def _suffix_key(suffix: str) -> OidTuple:
    parsed = parse_numeric_oid(suffix) if suffix else ()
    return parsed or ()


# Tables whose columns are spelled out in the function's result-column docs.
DOCUMENTED_TABLES = ["IF-MIB::ifXTable", "HOST-RESOURCES-MIB::hrStorageTable"]


def dynamic_columns_md(tables: list[str]) -> str:
    """Result-column tables, one variant per documented MIB table, generated from the MIB."""
    parts = [
        "The columns depend on the `table` argument and come from its MIB definition: `_index`, then "
        "the INDEX objects decoded from it, then one column per readable column object. Counter64 is "
        "`UBIGINT`, other integers `BIGINT`, enumerations and everything else `VARCHAR`. Common tables:"
    ]
    for name in tables:
        schema = table_schema(mibs().table(name))
        mt = mibs().table(name)
        syntaxes = {o.name: o.syntax_name for o in [*mt.index, *mt.columns]}
        rows = "".join(
            f"| {f.name} | {_sql_type(f.type)} | {syntaxes.get(f.name) or 'Instance suffix'} |\n" for f in schema
        )
        parts.append(f"**`table` = '{name}'**:\n\n| Name | Type | Description |\n|---|---|---|\n{rows}")
    return "\n\n".join(parts)


def _sql_type(arrow_type: pa.DataType) -> str:
    return {pa.string(): "VARCHAR", pa.int64(): "BIGINT", pa.uint64(): "UBIGINT"}[arrow_type]


@init_single_worker
class SnmpTable(TableFunctionGenerator[TableArgs, TableState]):
    """Read a conceptual table with typed columns taken from its MIB definition."""

    class Meta:
        """Function metadata surfaced to DuckDB, agents and vgi-lint."""

        name = "snmp_table"
        description = "Read an SNMP MIB table (ifTable, hrStorageTable, ...) as typed rows, one per table row"
        projection_pushdown = True
        tags = {
            **object_tags(
                title="SNMP Table",
                category="snmp",
                keywords="snmp table, snmptable, ifTable, ifXTable, hrStorageTable, interfaces, counters, mib table",
                doc_llm=(
                    "Read a MIB conceptual table from the agent at `host`, one row per table row, with one "
                    "typed column per readable MIB column. The table can be named by the table, its entry, one "
                    "of its columns or its numeric OID. Column names are the MIB object names (ifDescr, "
                    "ifOperStatus, ifHCInOctets). Enumerations become their labels ('up', 'down'), Counter64 "
                    "becomes `UBIGINT`, other integers `BIGINT`, and everything else `VARCHAR` display text. "
                    "`_index` is the row's instance suffix, and the INDEX objects (such as ifIndex) are "
                    "decoded from it. Only the columns the query uses are fetched. "
                    "The schema comes from the MIB, so describing the query lists the columns without "
                    "contacting the agent, and the MIB object listing shows which tables exist. Tables that "
                    "augment another (ifXTable augments ifTable) share its index and combine by `_index`. "
                    "For tables of MIBs this worker does not load, walk the subtree instead. " + CONNECTION_DOC_LLM
                ),
                doc_md=(
                    "## snmp_table(host, table, max_repetitions := 25)\n\n"
                    "A MIB table as rows with typed columns, like `snmptable`. Only projected columns are "
                    "walked.\n\n" + CONNECTION_DOC_MD
                ),
            ),
            "vgi.result_dynamic_columns_md": dynamic_columns_md(DOCUMENTED_TABLES),
        }
        examples = [
            FunctionExample(
                sql=(
                    "SELECT ifName, ifHCInOctets, ifHCOutOctets FROM snmp.main.snmp_table('192.0.2.10', 'ifXTable') "
                    "ORDER BY ifHCInOctets DESC LIMIT 5"
                ),
                description="The five busiest interfaces by received octets",
            ),
            FunctionExample(
                sql=(
                    "SELECT hrStorageDescr, round(100.0 * hrStorageUsed / nullif(hrStorageSize, 0), 1) AS pct_used "
                    "FROM snmp.main.snmp_table('192.0.2.10', 'hrStorageTable') ORDER BY pct_used DESC NULLS LAST"
                ),
                description="Disk and memory utilisation from HOST-RESOURCES-MIB",
            ),
        ]

    @classmethod
    def on_bind(cls, params: BindParams[TableArgs]) -> BindResponse:
        """Build the schema from the MIB and request the target's ``snmp`` secret."""
        schema = table_schema(_table(params.args))
        request_secret(params)
        return BindResponse(output_schema=schema)

    @classmethod
    def _walked(cls, mt: MibTable, output: pa.Schema) -> list[MibObject]:
        wanted = set(output.names)
        readable = readable_columns(mt)
        walked = [c for c in readable if c.name in wanted]
        if not walked:
            # Only _index / INDEX objects (or nothing, for count(*)) were asked for: walk one column to find the rows.
            candidates = readable or [c for c in mt.columns if c.access in _READABLE]
            if not candidates:
                raise SnmpError(f"{mt.table.name} has no readable columns")
            walked = candidates[:1]
        return walked

    @classmethod
    def initial_state(cls, params: ProcessParams[TableArgs]) -> TableState:
        """One cursor per walked column, all at the start."""
        mt = _table(params.args)
        return TableState(cursors=["" for _ in cls._walked(mt, params.output_schema)])

    @classmethod
    def process(cls, params: ProcessParams[TableArgs], state: TableState, out: OutputCollector) -> None:
        """Advance the column cursors and emit every row they have all passed."""
        mt = _table(params.args)
        walked = cls._walked(mt, params.output_schema)
        if all(c == _DONE for c in state.cursors) and state.started:
            out.finish()
            return
        state.started = True
        session = open_session(params.args, params.secrets)
        pending: dict[str, dict[str, Any]] = json.loads(state.pending)
        ready: dict[str, dict[str, Any]] = {}
        while len(ready) < BATCH_ROWS:
            active = [i for i, c in enumerate(state.cursors) if c != _DONE]
            if not active:
                break
            requests = [walked[i].oid + _suffix_key(state.cursors[i]) for i in active]
            responses = session.next_rows(requests, params.args.max_repetitions)
            for i, binds in zip(active, responses, strict=True):
                cls._advance(session, walked[i], binds, i, state, pending)
            positions = [_suffix_key(c) for c in state.cursors if c != _DONE]
            threshold = min(positions) if positions else None
            for key in [k for k in pending if threshold is None or _suffix_key(k) <= threshold]:
                ready[key] = pending.pop(key)
        state.pending = json.dumps(pending)
        if ready:
            out.emit(cls._batch(mt, ready, params.output_schema))
        elif all(c == _DONE for c in state.cursors):
            out.finish()

    @staticmethod
    def _advance(
        session: Any,
        col: MibObject,
        binds: list[tuple[OidTuple, Any]],
        i: int,
        state: TableState,
        pending: dict[str, dict[str, Any]],
    ) -> None:
        """Record one column's successors; mark the cursor done when it leaves the column."""
        prefix = len(col.oid)
        before = _suffix_key(state.cursors[i])
        if not binds:
            state.cursors[i] = _DONE
            return
        for oid, value in binds:
            if is_end(value) or oid[:prefix] != col.oid or len(oid) == prefix:
                state.cursors[i] = _DONE
                return
            suffix = oid[prefix:]
            if suffix <= before:
                raise SnmpError(
                    f"{session.target}: agent returned OIDs out of order in {col.name} "
                    f"({oid_str(oid)}); stopping to avoid an endless walk"
                )
            key = oid_str(suffix)
            pending.setdefault(key, {})[col.name] = column_value(col.syntax, value)
            state.cursors[i] = key
            before = suffix

    @staticmethod
    def _batch(mt: MibTable, rows: dict[str, dict[str, Any]], schema: pa.Schema) -> pa.RecordBatch:
        """Rows in index order, with INDEX objects decoded from the instance suffix."""
        keys = sorted(rows, key=_suffix_key)
        cols: dict[str, list[Any]] = {name: [] for name in schema.names}
        index_names = [o.name for o in mt.index]
        wants_index = any(name in cols for name in index_names)
        for key in keys:
            decoded: dict[str, Any] = {}
            if wants_index:
                values = mt.decode_index(_suffix_key(key))
                if values is not None:
                    for obj, value in zip(mt.index, values, strict=True):
                        decoded[obj.name] = column_value(obj.syntax, value)
            row = rows[key]
            for name, values_list in cols.items():
                if name == INDEX_COLUMN:
                    values_list.append(key)
                elif name in decoded or name in index_names:
                    values_list.append(decoded.get(name))
                else:
                    values_list.append(row.get(name))
        if not schema.names:
            return pa.RecordBatch.from_arrays([], schema=schema) if not keys else _empty_columns(len(keys))
        return pa.RecordBatch.from_pydict(cols, schema=schema)


def _empty_columns(n: int) -> pa.RecordBatch:
    """Build a batch with rows but no columns (``count(*)`` with nothing projected)."""
    return pa.RecordBatch.from_struct_array(cast("pa.StructArray", pa.array([{}] * n, type=pa.struct([]))))
