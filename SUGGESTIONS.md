Last Edit: Codex - 2026-10-25 - Motive: Record verified dependency security and compatibility constraints.

# Suggestions

Keep the archived fork source-only: preserve test/security checks and the
regression-tested no-publication release workflows, then restore the
repository's archived state after the approved repair.

| Problem | Proposal | Impact |
| --- | --- | --- |
| An exact compatibility pin can become stale | Recheck all filelock advisory ranges during consumer release scans | Prevent stale security assumptions |
| Dependency APIs can change independently of this package | Retain [installed metadata and behavior tests](tests/test_dependency_security.py); review bounds before widening | Catch fresh-install incompatibilities |
| Dependencies can raise their minimum interpreter | Keep Requires-Python aligned with the actual selected dependencies | Reject unsupported interpreters before installation |

Source boundary: [Client and AbstractDB](hivemind_plugin_manager/database.py).

