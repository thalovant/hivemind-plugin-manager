Last Edit: Codex - 2026-10-25 - Motive: Record verified dependency security and compatibility constraints.

# Suggestions

Keep the archived fork source-only: preserve test/security checks, prevent
obsolete package publication before merging the repair, and restore the
repository's archived state afterward.

| Problem | Proposal | Impact |
| --- | --- | --- |
| An exact compatibility pin can become stale | Recheck all filelock advisory ranges during consumer release scans | Prevent stale security assumptions |
| Dependency APIs can change independently of this package | Retain [installed metadata and behavior tests](tests/test_dependency_security.py); review bounds before widening | Catch fresh-install incompatibilities |

Source boundary: [Client and AbstractDB](hivemind_plugin_manager/database.py).

