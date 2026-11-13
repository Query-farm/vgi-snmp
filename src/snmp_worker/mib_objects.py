"""``snmp_mib_objects(module := NULL, kind := NULL)``: browse the loaded MIBs offline."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Annotated, ClassVar

import pyarrow as pa
from vgi.arguments import Arg
from vgi.metadata import FunctionExample
from vgi.table_function import (
    OutputCollector,
    ProcessParams,
    TableFunctionGenerator,
    bind_fixed_schema,
    init_single_worker,
)
from vgi_rpc import ArrowSerializableDataclass

from .meta import column, object_tags
from .mib import mibs, oid_str

KINDS = ["scalar", "table", "row", "column", "notification", "node"]

SCHEMA = pa.schema(
    [
        column("module", pa.string(), "MIB module defining the object, e.g. 'IF-MIB'.", nullable=False),
        column("name", pa.string(), "Object name, e.g. 'ifHCInOctets'.", nullable=False),
        column("oid", pa.string(), "Numeric OID of the object (without instance suffix).", nullable=False),
        column("kind", pa.string(), "scalar, table, row, column, notification or node.", nullable=False),
        column("syntax", pa.string(), "Syntax or textual convention, e.g. 'Counter64', 'DisplayString'."),
        column("access", pa.string(), "MAX-ACCESS: read-only, read-write, read-create, not-accessible, ..."),
        column("status", pa.string(), "STATUS: current, deprecated or obsolete."),
        column("units", pa.string(), "UNITS clause, when declared."),
        column("description", pa.string(), "DESCRIPTION clause, whitespace-normalized."),
    ]
)


@dataclass(slots=True, frozen=True, kw_only=True)
class MibObjectsArgs:
    """Arguments for ``snmp_mib_objects(module := NULL, kind := NULL)``."""

    module: Annotated[
        str | None, Arg("module", default=None, doc="Only objects of this MIB module, e.g. 'IF-MIB'. NULL: all.")
    ]
    kind: Annotated[
        str | None,
        Arg(
            "kind", default=None, doc="Only this kind: scalar, table, row, column, notification or node.", choices=KINDS
        ),
    ]


@dataclass(kw_only=True)
class MibObjectsState(ArrowSerializableDataclass):
    """Cursor: whether the listing was emitted."""

    done: bool = False


@init_single_worker
@bind_fixed_schema
class SnmpMibObjects(TableFunctionGenerator[MibObjectsArgs, MibObjectsState]):
    """List the objects defined by the loaded MIB modules."""

    FIXED_SCHEMA: ClassVar[pa.Schema] = SCHEMA

    class Meta:
        """Function metadata surfaced to DuckDB, agents and vgi-lint."""

        name = "snmp_mib_objects"
        description = "List the objects (tables, columns, scalars) defined by the loaded MIB modules"
        tags = {
            **object_tags(
                title="MIB Objects",
                category="mib",
                keywords="mib browser, mib objects, tables, columns, oid list, syntax, description",
                doc_llm=(
                    "List every named object in the MIB modules this worker has loaded, offline: module, "
                    "name, oid, kind (scalar/table/row/column/notification/node), syntax, access, status, "
                    "units and description. Filter with the named arguments `module := 'IF-MIB'` and "
                    "`kind := 'table'`. Use it to discover which tables snmp_table can read and which "
                    "columns they have (a column's oid starts with its row's oid), and which scalars "
                    "snmp_get can read (append '.0')."
                ),
                doc_md=(
                    "## snmp_mib_objects(module := NULL, kind := NULL)\n\n"
                    "Browse the loaded MIBs: tables `snmp_table` can read, and the scalars and columns "
                    "`snmp_get` and `snmp_walk` can name."
                ),
            ),
            "vgi.result_columns_schema": json.dumps(
                [
                    {"name": "module", "type": "VARCHAR", "description": "MIB module defining the object."},
                    {"name": "name", "type": "VARCHAR", "description": "Object name."},
                    {"name": "oid", "type": "VARCHAR", "description": "Numeric OID of the object."},
                    {
                        "name": "kind",
                        "type": "VARCHAR",
                        "description": "scalar, table, row, column, notification or node.",
                    },
                    {"name": "syntax", "type": "VARCHAR", "description": "Syntax or textual convention."},
                    {"name": "access", "type": "VARCHAR", "description": "MAX-ACCESS."},
                    {"name": "status", "type": "VARCHAR", "description": "STATUS."},
                    {"name": "units", "type": "VARCHAR", "description": "UNITS clause."},
                    {"name": "description", "type": "VARCHAR", "description": "DESCRIPTION clause."},
                ]
            ),
            "vgi.executable_examples": json.dumps(
                [
                    {
                        "description": "The 64-bit counters in IF-MIB",
                        "sql": (
                            "SELECT name FROM snmp.main.snmp_mib_objects(module := 'IF-MIB', kind := 'column') "
                            "WHERE syntax = 'Counter64' ORDER BY name LIMIT 3"
                        ),
                        "expected_result": [["ifHCInBroadcastPkts"], ["ifHCInMulticastPkts"], ["ifHCInOctets"]],
                    },
                    {
                        "description": "Columns of hrStorageTable",
                        "sql": (
                            "SELECT count(*) AS columns FROM snmp.main.snmp_mib_objects("
                            "module := 'HOST-RESOURCES-MIB', kind := 'column') WHERE oid LIKE '1.3.6.1.2.1.25.2.3.1.%'"
                        ),
                        "expected_result": [[7]],
                    },
                ]
            ),
        }
        examples = [
            FunctionExample(
                sql=(
                    "SELECT module, count(*) AS tables FROM snmp.main.snmp_mib_objects(kind := 'table') "
                    "GROUP BY module ORDER BY tables DESC"
                ),
                description="Which loaded MIB modules define the most tables?",
            ),
            FunctionExample(
                sql=(
                    "SELECT name, syntax, units FROM snmp.main.snmp_mib_objects(module := 'UCD-SNMP-MIB', "
                    "kind := 'scalar') WHERE name LIKE 'mem%' ORDER BY oid"
                ),
                description="Net-SNMP memory statistics available with snmp_get",
            ),
        ]

    @classmethod
    def initial_state(cls, params: ProcessParams[MibObjectsArgs]) -> MibObjectsState:
        """Nothing emitted yet."""
        return MibObjectsState()

    @classmethod
    def process(cls, params: ProcessParams[MibObjectsArgs], state: MibObjectsState, out: OutputCollector) -> None:
        """Emit the filtered listing as one batch."""
        if state.done:
            out.finish()
            return
        state.done = True
        module, kind = params.args.module, params.args.kind
        cols: dict[str, list[str | None]] = {f.name: [] for f in SCHEMA}
        for obj in mibs().objects:
            if module is not None and obj.module != module:
                continue
            obj_kind = obj.kind
            if kind is not None and obj_kind != kind:
                continue
            cols["module"].append(obj.module)
            cols["name"].append(obj.name)
            cols["oid"].append(oid_str(obj.oid))
            cols["kind"].append(obj_kind)
            cols["syntax"].append(obj.syntax_name)
            cols["access"].append(obj.access)
            cols["status"].append(obj.status)
            cols["units"].append(obj.units)
            cols["description"].append(obj.description)
        out.emit(
            pa.RecordBatch.from_pydict(
                {f.name: cols[f.name] for f in params.output_schema}, schema=params.output_schema
            )
        )
