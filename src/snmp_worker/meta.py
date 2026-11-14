"""Discovery metadata for the snmp catalog.

DuckDB, coding agents and the ``vgi-lint`` metadata checker all read these tags.
Every function carries ``object_tags(...)``: a title, a category from
``SCHEMA_CATEGORIES``, search keywords, and LLM- and human-facing docs.
"""

from __future__ import annotations

import json
from typing import Any

import pyarrow as pa

CATALOG_NAME = "snmp"

SOURCE_URL = "https://github.com/Query-farm/vgi-snmp"

SCHEMA_CATEGORIES = [
    {
        "name": "snmp",
        "title": "SNMP Queries",
        "description": "Table functions that query SNMP agents on the network (GET, WALK, tables).",
    },
    {
        "name": "mib",
        "title": "MIB Lookups",
        "description": "Offline functions over the loaded MIB modules: OID/name resolution and object listings.",
    },
]


def keywords_array(keywords: str) -> str:
    """Turn ``"a, b, c"`` into the JSON array string ``vgi.keywords`` requires."""
    return json.dumps([k.strip() for k in keywords.split(",") if k.strip()])


def object_tags(*, title: str, category: str, keywords: str, doc_llm: str, doc_md: str) -> dict[str, str]:
    """Build the standard per-object discovery tags."""
    if category not in {c["name"] for c in SCHEMA_CATEGORIES}:
        raise ValueError(f"unknown category {category!r}; add it to SCHEMA_CATEGORIES")
    return {
        "vgi.title": title,
        "vgi.category": category,
        "vgi.keywords": keywords_array(keywords),
        "vgi.doc_llm": doc_llm,
        "vgi.doc_md": doc_md,
    }


def column(name: str, type_: pa.DataType, comment: str, *, nullable: bool = True) -> pa.Field[Any]:
    """Build an Arrow field whose ``comment`` shows up in DuckDB's ``DESCRIBE`` and agent tools."""
    return pa.field(name, type_, nullable=nullable, metadata={b"comment": comment.encode()})


# Shared by the docs of every function that talks to an agent.
CONNECTION_DOC_LLM = (
    "Connection named arguments: `version` ('1', '2c' or '3'; default '3' when a v3 user is "
    "configured, else '2c'), `community`, `port` (default 161; 'host:port' also works), `timeout` "
    "(seconds per attempt, default 2), `retries` (default 1) and `context` (SNMPv3 context name). "
    "Credentials come from the `community` argument, else from a DuckDB secret of type `snmp` whose "
    "SCOPE is a prefix of 'snmp://<host>:<port>', else from the SNMP_COMMUNITY, SNMP_USER, "
    "SNMP_AUTH_PROTOCOL, SNMP_AUTH_KEY, SNMP_PRIV_PROTOCOL and SNMP_PRIV_KEY environment variables, "
    "else the community 'public'. A v3 secret looks like:\n\n"
    "```sql\nCREATE SECRET (TYPE snmp, SCOPE 'snmp://10.0.0.', USER 'monitor', AUTH_PROTOCOL 'sha256',\n"
    "  AUTH_KEY 'auth-passphrase', PRIV_PROTOCOL 'aes', PRIV_KEY 'priv-passphrase');\n```\n\n"
    "A timeout or wrong credentials raise an error that names the agent."
)

CONNECTION_DOC_MD = (
    "**Connection:** `version := '1' | '2c' | '3'`, `community := '...'`, `port := 161`, "
    "`timeout := 2.0`, `retries := 1`, `context := ''`. Credentials can also come from a "
    "`snmp` secret scoped to `snmp://<host>` or from `SNMP_*` environment variables; see the README."
)

CATALOG_DOC_LLM = (
    "Query SNMP agents (routers, switches, servers, printers, UPS units) from SQL. Device queries "
    "are table functions that take the agent address first and return either raw variable bindings "
    "(one row per OID instance, with the MIB name, SNMP type, display value, exact integer and raw "
    "octets) or a MIB conceptual table as typed rows, one column per MIB column, where only the "
    "columns the query uses are fetched. Offline helpers translate between MIB names and numeric "
    "OIDs and list the objects of the loaded MIBs (IF-MIB, IP-MIB, HOST-RESOURCES-MIB, ENTITY-MIB, "
    "ENTITY-SENSOR-MIB, UCD-SNMP-MIB, NET-SNMP-MIB and the SNMPv2 core). SNMP v1, v2c and v3 (USM "
    "authentication and privacy) are supported. Credentials come from arguments, a host-scoped DuckDB "
    "secret of type `snmp`, or SNMP_* environment variables, so they stay out of queries. To poll "
    "several devices, UNION ALL one call per host."
)

CATALOG_DOC_MD = (
    "# SNMP for DuckDB\n\n"
    "**Read SNMP devices with SQL.** GET instances, walk subtrees and read MIB tables such as "
    "`ifXTable` or `hrStorageTable` as typed rows, over SNMP v1, v2c or v3.\n\n"
    "MIB names resolve offline against the bundled IETF and Net-SNMP MIB modules, and table "
    "schemas come from the MIB, so `DESCRIBE` works without contacting a device.\n\n"
    "Credentials come from a `snmp` DuckDB secret scoped by host, so they stay out of queries."
)

SCHEMA_DOC_LLM = (
    "The `main` schema holds the SNMP functions. Device queries take the agent address as their first "
    "argument and share the named arguments `version`, `community`, `port`, `timeout`, `retries` and "
    "`context`; raw results have the columns host, oid, name, object, instance, type, value, "
    "value_int and value_bytes, and table results have typed columns named after the MIB objects plus "
    "`_index`, the row's instance suffix. OIDs are written numerically or as MIB names, optionally "
    "module-qualified, with an instance suffix for scalars ('sysUpTime.0'). The offline MIB lookups "
    "return NULL for NULL or unresolvable input and are how to discover table and column names. "
    "OIDs are `VARCHAR`, so sort them numerically by casting string_split(oid, '.') to `INTEGER[]`."
)

SCHEMA_DOC_MD = (
    "## main\n\n"
    "Device queries send SNMP GET, GETNEXT and GETBULK requests to the agent named by their first "
    "argument, using SNMP v1, v2c or v3.\n\n"
    "MIB lookups work offline against the bundled MIB modules: translate names and OIDs, and find "
    "the tables and columns a device query can name."
)

AGENT_TEST_TASKS = [
    {
        "name": "ifinoctets_oid",
        "prompt": "Using the snmp worker, what is the numeric OID of IF-MIB's ifHCInOctets column?",
    },
    {"name": "oid_to_name", "prompt": "Which MIB object and instance does the OID 1.3.6.1.2.1.1.3.0 refer to?"},
    {
        "name": "iftable_columns",
        "prompt": "How many columns does the IF-MIB ifTable define, according to the snmp worker's MIBs?",
    },
    {
        "name": "counter64_columns",
        "prompt": "List the names of the IF-MIB columns whose syntax is Counter64, in OID order.",
    },
    {
        "name": "ifxtable_counter_type",
        "prompt": (
            "When the snmp worker reads IF-MIB's ifXTable from a device, what DuckDB type does the "
            "ifHCInOctets column have? Answer without contacting a device."
        ),
    },
    {
        "name": "get_exact_value_column",
        "prompt": (
            "Which column of the snmp worker's single-instance GET results holds a counter's exact "
            "integer value, and what is its DuckDB type? Answer without contacting a device."
        ),
    },
    {
        "name": "hc_counter_oids_for_interface",
        "prompt": (
            "I need to poll interface ifIndex 7 with a tool that only takes numeric OIDs. Using the snmp "
            "worker's MIBs, list every IF-MIB column whose syntax is Counter64 together with the numeric OID "
            "of its instance for ifIndex 7. Return two columns: name and oid, in OID order."
        ),
    },
    {
        "name": "walk_result_columns",
        "prompt": "How many columns does the snmp worker's subtree walk return? Answer without contacting a device.",
    },
]

CATALOG_TAGS = {
    "vgi.title": "SNMP Devices",
    "vgi.subtitle": "Query SNMP v1/v2c/v3 devices from SQL: GET, WALK and MIB tables as typed rows.",
    "vgi.doc_llm": CATALOG_DOC_LLM,
    "vgi.doc_md": CATALOG_DOC_MD,
    "vgi.source_url": SOURCE_URL,
    "vgi.icon_url": "https://query.farm/media-kit/products/vgi/vgi-logo.png",
    "vgi.license": "0BSD",
    "vgi.author": "Query.Farm",
    "vgi.copyright": "Copyright 2026 Query Farm LLC - https://query.farm",
    "vgi.keywords": keywords_array(
        "snmp, snmpwalk, snmpget, mib, network monitoring, routers, switches, interfaces, ifTable, duckdb"
    ),
    "vgi.support_contact": f"{SOURCE_URL}/issues",
    "vgi.support_policy_url": f"{SOURCE_URL}#support",
    "vgi.agent_test_tasks": json.dumps(AGENT_TEST_TASKS),
}
