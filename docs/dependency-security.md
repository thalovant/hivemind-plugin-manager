Last Edit: Codex - 2026-10-25 - Motive: Record verified dependency security and compatibility constraints.

# Dependency Security

The real installation source, `requirements.txt and setup.py`, pins `filelock==3.20.3`.
This maintains the classic FileLock interface accepted by upstream combo-lock's
`filelock~=3.0` requirement and Python 3.10. No direct URL or scanner exception
is used, and no claim is made that future advisories cannot affect this version.

## Evidence

The GitHub Advisory Database lists older affected ranges `<3.20.1`
([GHSA-w853-jp5j-5j7f](https://github.com/advisories/GHSA-w853-jp5j-5j7f)) and
`<3.20.3` ([GHSA-qmgc-5h2g-mvrw](https://github.com/advisories/GHSA-qmgc-5h2g-mvrw)).
The newer HIGH [GHSA-v4x8-3wr5-3wq8](https://github.com/advisories/GHSA-v4x8-3wr5-3wq8)
affects `>=3.20.4,<=4.2.0`; the other five published ranges begin at 3.20.4,
3.22.0, or 4.1.0. Exact 3.20.3 lies outside all eight ranges.

The legacy MYCROFT_LOOSE_REQUIREMENTS mode must not convert the security pin into >=3.20.3. setup.py.required preserves this constraint, and its regression test executes the real setup metadata path.

## Verification

- 3 passed on Python 3.14 and 3 passed on Python 3.10.
- [Regression tests](../tests/test_dependency_security.py) check the installed
  dependency and real classic-lock contention/release.
- Wheel and sdist builds pass; built wheel metadata contains exact filelock==3.20.3 and no direct-URL dependency.
- [Client and AbstractDB](../hivemind_plugin_manager/database.py) remains unchanged.
- Four tests pass on Python3.10 after adding the workflow regression. It verifies
  structured checkout settings and read-only permissions; CodeQL's untrusted-ref
  finding is repaired by using the event revision, not dismissed.

A passing library test does not approve a production rollout. The consuming
application's normal build and vulnerability gates remain required.

## Source-only maintenance

Both legacy release workflows now contain only a notice with read-only contents
permission. They cannot publish packages, tags or releases, or mutate branches.
The owner approved this boundary specifically for the archived fork repair.
Six regressions pass on Python3.10, including structured checks of both release
workflows; normal build and CodeQL checks are retained. No package is published.

