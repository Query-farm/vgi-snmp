# Changelog

## 0.1.0 (2026-11-12)

First release.

- `snmp_get`, `snmp_walk` and `snmp_table` query SNMP v1, v2c and v3 agents (USM auth and
  privacy via pysnmp). `snmp_table` builds a typed schema from the MIB, fetches only the
  projected columns and streams rows across batches.
- `snmp_oid`, `snmp_oid_name` and `snmp_mib_objects` resolve and browse the bundled MIBs offline.
- Credentials from a host-scoped `snmp` DuckDB secret, `SNMP_*` environment variables or arguments.

Targets: vgi-python 0.51 · VGI protocol 3.3 · Haybarn 2.0.0rc11 · vgi-lint-check 2.x (unpinned)
