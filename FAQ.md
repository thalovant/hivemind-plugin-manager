Last Edit: Codex - 2026-10-25 - Motive: Record verified dependency security and compatibility constraints.

# FAQ

## Can this maintenance merge publish the legacy package?

No. Both release workflows contain only a read-only notice. They have no
publisher action, reusable release workflow, secret access, tag creation or
branch mutation. Tests verify that exact boundary; build and security checks
remain enabled.

## Why does the test checkout omit an explicit ref?

The event revision is the intended test input. Overriding it with an untrusted
PR head name in manual or default-branch context can poison trusted caches.
The workflow keeps read-only permissions and tests this boundary explicitly.

## Why is filelock pinned exactly?

Python>=3.10 is explicitly declared because the patched dependency does not
support earlier interpreters. The installed distribution metadata is tested.

3.20.3 contains the earlier fixes and predates the newer affected features.
A broad 3.x range can select an affected version. See the primary ranges and
verified limits in [dependency security](docs/dependency-security.md).

## Does this alter runtime behavior?

[Client and AbstractDB](hivemind_plugin_manager/database.py) is unchanged. The regression tests exercise classic
lock contention and real dependency metadata. The legacy MYCROFT_LOOSE_REQUIREMENTS mode must not convert the security pin into >=3.20.3. setup.py.required preserves this constraint, and its regression test executes the real setup metadata path.

