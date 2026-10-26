Last Edit: Codex - 2026-10-25 - Motive: Record verified dependency security and compatibility constraints.

# Quick Facts

The build checks out its event revision with read-only contents permission.
Four dependency/workflow regression tests pass on Python3.10. Source merge is
held pending a no-publication boundary and exact-head hosted checks.

| Field | Value |
| --- | --- |
| Package | hivemind-plugin-manager |
| Version | 0.4.1a2 |
| Entry points | hpm = hivemind_plugin_manager.tui:cli |
| filelock | Exact 3.20.3 in real installation requirements |

Source: [Client and AbstractDB](hivemind_plugin_manager/database.py); [dependency evidence](docs/dependency-security.md).

