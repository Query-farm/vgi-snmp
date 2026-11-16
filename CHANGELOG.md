# Changelog

## 0.1.3 (2026-11-16)

- Bump vgi-python to 0.52.2.
- Requires Python 3.14 (CI, Docker image and tooling moved to 3.14).

## 0.1.2 (2026-11-14)

- Docs link to upstream sources: the catalog docs now link RFC 3416, RFC 3414, RFC 2863,
  Net-SNMP and PySNMP (vgi-lint VGI183).
- The `main` schema comment is now a one-line summary; its Markdown docs no longer repeat it
  (vgi-lint VGI102).

## 0.1.1 (2026-11-14)

- The catalog comment (the worker's one-line description in directories) is now a short
  plain-text sentence instead of the Markdown overview, which stays in the catalog's
  `vgi.doc_md` tag.
- Composed example queries combining device queries with MIB lookups. The SQL surface is unchanged.

## 0.1.0 (2026-11-12)

First release.

- `snmp_get`, `snmp_walk` and `snmp_table` query SNMP v1, v2c and v3 agents (USM auth and
  privacy via pysnmp). `snmp_table` builds a typed schema from the MIB, fetches only the
  projected columns and streams rows across batches.
- `snmp_oid`, `snmp_oid_name` and `snmp_mib_objects` resolve and browse the bundled MIBs offline.
- Credentials from a host-scoped `snmp` DuckDB secret, `SNMP_*` environment variables or arguments.

Targets: vgi-python 0.51 · VGI protocol 3.3 · Haybarn 2.0.0rc11 · vgi-lint-check 2.x (unpinned)
