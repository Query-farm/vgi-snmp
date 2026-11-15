# Unfinished SNMP notebook checkpoint

Work stopped at the user's explicit request. This branch is a reviewable draft, not a completed fleet migration; it must not be merged to main as finished work.

## Completed

- Captured the clean original checkout baseline and authored in an isolated worktree.
- Read root AGENTS.md and reused existing green source CI 43614862542; no worker builds, full suites, containers or CI dispatches.
- Actual released v0.1.0 and current-main catalog probes through Haybarn 2.0.0rc11: six functions, no tables or views; same named interface.
- Preserved the storage-unit/threshold story and added MIB-definition versus raw-instance audit SQL.
- Moved the local synthetic simulator to its own pinned uvx environment. Actual loopback response, raw GETBULK read, idempotent cleanup, scoped environment restoration and exact fixture regeneration passed.
- Four companions frozen and publicly pushed at 239c020ec62ddea3fd1e30c647c7ca822a8b2f14.
- Draft default executed successfully: 24 code cells, three SVG charts, 27.2 seconds. The kernel emitted a transport notice in the process log, outside saved outputs.
- Draft notebook Ruff format/check completed during that execution preparation.

## Pending when stopped

- Shared companion registry release/pin confirmation and replacement of draft `Path.cwd()` setup with the registered bootstrap; current draft uses shared v0.3.53 and local companions.
- Visual review of all three figures, including parent review.
- Detached 80 → 70 threshold experiment and unchanged-data/plot comparison.
- Fresh preloaded Python 3.12 notebook-only bootstrap covering simulator and worker.
- Final coverage.json, catalog normalization, execution receipts and editorial review. Raw complete catalogs are already included; six-of-six is the intended mapping, not yet verified coverage.
- Original analytical SQL/table preservation audit, final runner guards and output/presentation checks.
- README finalization: the README describes the intended finished workflow, and its claims of completed final checks must not be treated as achieved at this checkpoint.
- Final main publication, actual anonymous GitHub SVG verification, durable completed report and synchronization back to the original checkout.

No real device was contacted. All SNMP execution used the disposable synthetic loopback agent; no community credentials from the environment or SQL secret store were used. Worker source, root dependency files and original checkout remain untouched. Only this draft branch is being pushed.
