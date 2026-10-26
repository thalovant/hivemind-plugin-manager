Last Edit: Codex - 2026-10-25 - Motive: Record verified dependency security and compatibility constraints.

# Quick Facts

The build checks out its event revision with read-only contents permission.
Seven dependency/workflow regression tests pass on Python3.10. Both release
workflows are read-only notices, with no package/tag/release publication.
Exact-head hosted checks remain required before source merge and rearchival.

| Field | Value |
| --- | --- |
| Package | hivemind-plugin-manager |
| Version | 0.4.1a2 |
| Entry points | hpm = hivemind_plugin_manager.tui:cli |
| filelock | Exact 3.20.3 in real installation requirements |
| Python | >=3.10 in actual installer metadata |

Source: [Client and AbstractDB](hivemind_plugin_manager/database.py); [dependency evidence](docs/dependency-security.md).

