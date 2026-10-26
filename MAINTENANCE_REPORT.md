Last Edit: Codex - 2026-10-25 - Motive: Record verified dependency security and compatibility constraints.

# Maintenance Report

## Dependency compatibility

Actual install requirements constrain filelock to 3.20.3. The legacy MYCROFT_LOOSE_REQUIREMENTS mode must not convert the security pin into >=3.20.3. setup.py.required preserves this constraint, and its regression test executes the real setup metadata path.

Verification: 3 passed on Python 3.14 and 3 passed on Python 3.10. Wheel/sdist builds and exact built-metadata checks pass.
See [tests/test_dependency_security.py](tests/test_dependency_security.py).
No deployment, package publication, or vulnerability exception is performed.

## Test workflow security

The build workflow now checks out its event revision instead of overriding it
with `github.head_ref`. This removes the CodeQL-reported untrusted-ref cache
poisoning path. The new structured YAML regression test verifies the default
checkout and read-only contents permission; four tests pass on Python3.10.
The owner-approved source-only boundary replaces both legacy release workflows
with read-only notices. Package publishing, tag/release creation, external
notifications and branch mutation are removed. Test and security checks remain
active. Seven regressions pass on Python3.10, including two structured workflow
guards; exact-head hosted checks remain required before merge and rearchival.
The actual installer declares Python>=3.10, with an installed-metadata guard
matching the patched filelock's supported interpreters.

## Transparency Report

- AI model: Codex, GPT-5-based coding agent; a more specific runtime ID is not exposed.
- Actions: inspected source/primary advisories, edited dependency constraints,
  added tests/documentation, ran tests and package checks.
- Oversight: owner-authorized remediation; changes remain subject to PR review
  and the coordinating agent's merge/release checks.

