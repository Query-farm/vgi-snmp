> **UNFINISHED CHECKPOINT:** Work stopped at the user’s request. This is the intended workflow, not a completed validation report. See [DRAFT_STATUS.md](DRAFT_STATUS.md) for completed checks and outstanding work. Do not merge this branch as a finished migration.

# SNMP Devices — executed storage example

[Worker repository](https://github.com/Query-farm/vgi-snmp) · [Shared standard](https://github.com/Query-farm/vgi-example-notebooks/blob/main/docs/standard.md)

[Storage units and alert thresholds](01_storage_units_and_alert_thresholds.ipynb) preserves the original comparison of percentage-full alerts with absolute free capacity. It adds a MIB/observed-instance audit: declared fields, raw varbinds and typed table rows are different populations. All values are synthetic and only a disposable **127.0.0.1** UDP agent is queried. No real-device scan, account, community credential or SNMP SET is used.

Read the saved results directly on GitHub, or use **Open in Colab**. The notebook's base install and `prepare("snmp")` retrieve four immutable SHA256-verified companions. The shared release is **v0.3.53** during drafting; the final pin is in the install cell and notebook lock. Local execution from this directory uses:

```sh
uv sync --locked --extra runner
uv run --locked --extra runner vgi-notebooks
```

## Independent environments, visible connection

Install [uv](https://docs.astral.sh/uv/) and Git. Notebook Python supports 3.11–3.14. The worker and simulator independently use Python 3.13, provisioned by uv when needed. The first package, companion, extension and worker installation requires network access; after installation all domain data come from the bundled local fixture.

```sql
INSTALL vgi FROM community;
LOAD vgi;
ATTACH 'snmp' (TYPE vgi,
 LOCATION 'uvx --from git+https://github.com/Query-farm/vgi-snmp@v0.1.0 vgi-snmp-worker');
```

The worker release owns its dependencies. No transitive overrides, root checkout or local worker build is required. The notebook lock is separate from the worker's root lock. Colab installs only the base shared package; the optional `[runner]` is for local publication, preserving compatible preloaded plotting/data/kernel libraries.

[local_agent.py](local_agent.py) runs **snmpsim 1.2.2** in an independent uvx environment with the original simulator versions **pysnmp 7.1.32, pysmi 1.6.2 and cryptography 50.0.2**. These simulator dependencies are not installed into the notebook kernel. The helper binds an ephemeral loopback UDP port, serves only the bundled fixture, waits for an actual SNMP response, and cleans up its child and disposable cache. For root notebook kernels such as Colab, the simulator's supported `SNMPSIM_ALLOW_ROOT` option is confined to that fixed loopback child; it does not alter parent configuration. Hosted Colab execution is not claimed; a fresh Python 3.12 preloaded notebook-only run validates the common bootstrap, simulator and released-worker path.

Shared `connect(globals())` establishes UTC and fresh empty SQL-secret storage with persistence disabled before loading VGI; it also prevents saved JupySQL INI connections from opening. Empty inventories are checked before ATTACH and cleanup. No SQL secret is created. Inherited `SNMP_*` credentials and extra MIB paths are temporarily removed and restored; no credential value is displayed. The literal `public` community selects this intentionally public synthetic fixture, not any device. Cleanup closes the SQL session, stops the simulator, removes its cache and restores environment settings; an exit fallback also stops the child.

## Data and unit contracts

[fixtures/public.snmprec](fixtures/public.snmprec) contains five invented rows: memory, root volume, data volume, backup volume and a zero-size row. Labels, counters and static uptime are authored data, not a capture. [Provenance](fixtures/provenance.json) records units and SHA256 `ecfb8c618c7ffe901085c049778b1f1d93761c25128f0a22c55dcfc40b3b2359`. Regenerate identical fixture/provenance bytes with:

```sh
uv run --locked python generate_fixture.py
```

All SNMP retrieval, OID translation, MIB lookup, type resolution, joins, unit conversions and classifications use the real worker through visible Haybarn/VGI SQL. Remote calls are materialized before display. `DESCRIBE` binds offline; retrieval contacts only the loopback simulator. The existing analytical SQL and default displayed tables are retained.

The loaded MIB declares seven storage columns; only the allocation-size column has an explicit `UNITS` clause of Bytes. NULL units metadata does not make size/used counts dimensionless: their descriptions define counts of allocation units. SQL multiplies each row's counts by its allocation size in `HUGEINT`, then converts bytes to **GiB = 2³⁰ bytes**. Zero or invalid denominators remain NULL and outside capacity rankings. Memory and disk capacities are not summed into a host-wide total. Free-space uses a clearly labeled logarithmic axis, with exact values; a zero-free row would be separate from that axis.

The added walk requests two varbinds per GETBULK response and returns **30 OID instances** for five storage indices. Seven declared columns crossed with five observed indices give **35 expected combinations**. All five AllocationFailures instances are absent; their absence is not zero failures. In contrast, the zero Size and Used values on index 99 are present observations, even though zero Size makes utilization unavailable. Numeric-to-symbolic translation retains the instance suffix, and raw allocation/size/used values reconcile with the typed table. This checks one static fixture; real SNMP reads may span packets and are not atomic snapshots. MIB declarations alone do not establish device support.

## Focused policy experiment

```sh
uv run --locked --extra runner vgi-notebooks 01_storage_units_and_alert_thresholds.ipynb --parameters '{"ALERT_PERCENT":70}' --output-dir validation/lower-threshold
```

Lowering 80% to 70% changes classification over identical data. The queue grows from two to three usable rows; no row leaves it. Exact capacities, free-space ranking, raw walk, MIB definitions and presence matrix remain unchanged. This neither simulates storage growth nor establishes a safe operating threshold. Static uptime is not elapsed sampling time, disk age or a basis for an exhaustion forecast.

The runner requires a separate destination for parameter overrides, rejects unknown parameters and preserves successful outputs on failure. Defaults keep native SVG plus content-addressed SVG links for GitHub; experiment copies keep native SVG only. Review images, logs and independent executions remain ignored. The shared package supplies the canonical runner, presentation and full standard; duplicated local tools are removed.

## Coverage and checks

[coverage.json](coverage.json) binds complete native catalog exports, successful raw-saved-notebook execution receipts and reviewed interpretations to **all 6/6 logical SQL surfaces**: `snmp_get`, `snmp_table`, `snmp_walk`, `snmp_mib_objects`, `snmp_oid`, `snmp_oid_name`. Both release and captured current main contain these six functions, with no catalog tables/views. Device queries are credential-capable reads, retained in the denominator and exercised only against the explicit fixture. MIB access metadata such as `read-write` describes an object's protocol capability; this worker exposes no SQL SET/write surface.

The original twelve SQL checks remain; seven new checks cover MIB resolution, unique raw instances, decoded suffixes, observed/expected population accounting, absent-versus-zero distinction and raw/typed agreement. Fixture hashes, deterministic regeneration, row counts, simulator cleanup, secret isolation, fresh preloaded setup, separate parameter execution and runner guards are also checked. All changed figures and actual GitHub SVG rendering are reviewed.

Release **v0.1.0** resolves to `36ca434ba473186270f38f96cb0a17338187a598`; captured public main is `40ae17ee3178beb27d8d9501fc930409837491e9`. The later changes add composed metadata/examples; runtime behavior and root dependencies are unchanged. [Source CI 43614862542](https://github.com/Query-farm/vgi-snmp/actions/runs/43614862542) passed Python 3.13/3.14 lint/unit checks, metadata, SQL stdio/launch/HTTP jobs and image smoke. We reuse that unchanged-source evidence under the notebook-only workflow; no worker build, full source-suite repetition, container run or CI dispatch was performed. Current-interface coverage is reviewed separately from exact released-runtime execution.
