# SNMP SQL notebooks

[Storage units and alert thresholds](01_storage_units_and_alert_thresholds.ipynb) queries a synthetic loopback SNMP agent, converts MIB allocation counts into GiB, and compares percentage-full alerts with absolute free capacity. A zero-size row stays unavailable.

## Run from this directory

Install [uv](https://docs.astral.sh/uv/) and Git. The locked notebook environment uses Python 3.13 or 3.14. First use needs network access for dependencies, the published Haybarn/VGI extension and the pinned public Git worker. The example then reads only a disposable local UDP agent. A copy of this directory runs without the worker checkout or a local worker build.

```bash
uv sync --frozen
uv run --frozen python execute.py
```

The visible SQL starts revision `36ca434ba473186270f38f96cb0a17338187a598` with `uvx`, Python 3.13, VGI SDK 0.51.1 / RPC 0.53.1, pysnmp 7.1.32 and cryptography 50.0.2. The independent notebook environment pins Haybarn 2.0.0rc11. Rerun default and experiment after changing any pin.

For interactive use, register this environment and select its kernel in Jupyter:

```bash
uv run --frozen python -m ipykernel install --user --name vgi-snmp-notebooks --display-name 'Python (vgi-snmp notebooks)'
```

Restart and run all after editing `ALERT_PERCENT`. Parameters, connection SQL and analytical SQL remain visible; Python setup, plots, result prose and cleanup are folded. The runner uses a temporary kernel and this directory as cwd. It saves only successful runs and requires a separate destination for overrides; unknown parameters and source-directory destinations are rejected.

## Focused experiment

```bash
uv run --frozen python execute.py --parameters '{"ALERT_PERCENT":70}' --output-dir validation/lower-threshold
```

Lowering the policy threshold from 80% to 70% changes classification over identical returned data. Compare the alert queue and percentage chart; the free-space chart and capacities must stay unchanged. This is neither a growth simulation nor advice on a safe device threshold.

## Fixture and local agent

All rows, labels and uptime values are invented. [Provenance](fixtures/provenance.json) records the hash and units of [public.snmprec](fixtures/public.snmprec). Regenerate its exact bytes with:

```bash
uv run --frozen python generate_fixture.py
```

[local_agent.py](local_agent.py) starts pinned snmpsim 1.2.2 with an ephemeral UDP port bound to `127.0.0.1`. It uses a disposable cache, waits for an actual SNMP response and terminates the child during cleanup. Inherited SNMP credentials and extra MIB paths are temporarily removed and restored afterward. The community `public` is explicitly part of this synthetic fixture. No real device credentials or addresses are required, and the worker performs only GET/table reads.

The helper serves fixtures; all SNMP retrieval, type resolution, joins, unit conversions and classifications pass through real Haybarn/VGI SQL. Network worker calls are materialized before separate display queries. The MIB table is typed at bind time; allocation sizes and counts are multiplied in HUGEINT before conversion to GiB. Zero/invalid denominators remain NULL and outside rankings. The free-space chart uses a labeled logarithmic scale; zero free space would be reported separately.

Twelve SQL checks cover identity, exact byte arithmetic, unit conversion, bounds, policy classification and GET result types, with additional fixture hash/row-count checks. Memory and disk rows are compared individually and never summed into a host-wide capacity. Real SNMP reads are not atomic snapshots. Static uptime is not elapsed sampling time and cannot support a growth rate or exhaustion forecast.

Saved default outputs are embedded. Generated charts, logs and experiment copies are ignored under `validation/`; experiment copies carry their relative helpers, fixtures and branding. [STANDARD.md](STANDARD.md) records presentation conventions.

Source `make check` with the published Haybarn unittest runner passed: 18 pytest tests, 189 stdio assertions, 189 Unix-launch assertions and 152 HTTP assertions; Ruff/format, mypy, pydoclint and metadata 100/100 L2 with zero findings.
