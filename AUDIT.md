Last Edit: Codex - 2026-10-25 - Motive: Record verified dependency security and compatibility constraints.

# Audit

The security constraint is carried by the real installer, not solely by a
scanner input. [Dependency tests](tests/test_dependency_security.py) verify
exact filelock selection and lock behavior. 3 passed on Python 3.14 and 3 passed on Python 3.10.

The legacy MYCROFT_LOOSE_REQUIREMENTS mode must not convert the security pin into >=3.20.3. setup.py.required preserves this constraint, and its regression test executes the real setup metadata path.

Client and AbstractDB in [the runtime source](hivemind_plugin_manager/database.py) is not modified.
This is not a complete audit of that implementation. Future advisory checks
and consumer artifact tests remain required; [evidence](docs/dependency-security.md).

CodeQL identified a HIGH untrusted-ref cache-poisoning path in the test workflow.
The checkout override is removed, with a structured YAML regression guard and
read-only permissions retained. Security analysis must pass on the corrected
head before merge. Existing dev-merge release jobs would publish the obsolete
package, so this draft is not mergeable until the approved source-only boundary
is in place.

