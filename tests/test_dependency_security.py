"""Keep the real install metadata and classic lock behavior security-pinned."""

from importlib.metadata import metadata, version
from pathlib import Path

import pytest
import yaml
from combo_lock import ComboLock
from packaging.requirements import Requirement


def test_wheel_metadata_keeps_exact_filelock_pin() -> None:
    """Installed distribution metadata must constrain the actual runtime graph."""
    requirements = [
        Requirement(value)
        for value in metadata("hivemind-plugin-manager").get_all("Requires-Dist", [])
    ]
    selected = [item for item in requirements if item.name == "filelock"]
    assert len(selected) == 1
    assert str(selected[0].specifier) == "==3.20.3"
    assert selected[0].marker is None
    assert all(item.url is None for item in requirements)
    assert version("filelock") == "3.20.3"


def test_ci_checks_out_the_event_revision_with_read_only_permissions() -> None:
    """Manual or push builds must not replace the event ref with an input ref."""
    path = Path(__file__).resolve().parents[1] / ".github/workflows/build_tests.yml"
    workflow = yaml.safe_load(path.read_text())
    assert workflow["permissions"] == {"contents": "read"}
    checkouts = [
        step
        for step in workflow["jobs"]["build_tests"]["steps"]
        if step.get("uses", "").startswith("actions/checkout@")
    ]
    assert len(checkouts) == 1
    assert "ref" not in checkouts[0].get("with", {})
    assert checkouts[0].get("with", {}).get("persist-credentials") is False


def test_python_floor_matches_the_patched_filelock() -> None:
    """Reject interpreters unsupported by the real filelock dependency."""
    assert metadata("hivemind-plugin-manager")["Requires-Python"] == ">=3.10"


def test_combo_lock_excludes_other_instances_and_releases(tmp_path: Path) -> None:
    """The selected filelock must preserve the API used by transitive consumers."""
    held = ComboLock(tmp_path / "dependency.lock")
    contender = ComboLock(tmp_path / "dependency.lock")
    with held:
        assert contender.acquire(blocking=False) is False
    assert contender.acquire(blocking=False) is True
    contender.release()


@pytest.mark.parametrize("filename", ["release_workflow.yml", "publish_stable.yml"])
def test_legacy_release_workflows_are_source_only(filename: str) -> None:
    """Merging this repair must not publish an obsolete distribution or tag."""
    path = Path(__file__).resolve().parents[1] / ".github/workflows" / filename
    workflow = yaml.safe_load(path.read_text())
    assert workflow["permissions"] == {"contents": "read"}
    assert set(workflow["jobs"]) == {"source_only"}
    job = workflow["jobs"]["source_only"]
    assert "uses" not in job
    assert "secrets" not in job
    assert "permissions" not in job
    assert job["steps"] == [{
        "name": "Record source-only maintenance",
        "run": 'echo "This legacy fork does not publish packages, tags, or releases."',
    }]


def test_legacy_loose_requirements_cannot_weaken_security_pin(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Legacy loose mode must leave the security constraint in wheel metadata."""
    import runpy
    from typing import Any

    import setuptools

    captured: dict[str, Any] = {}

    def capture_setup(**kwargs: Any) -> None:
        """Capture setup metadata without invoking a packaging command."""
        captured.update(kwargs)

    monkeypatch.setenv("MYCROFT_LOOSE_REQUIREMENTS", "1")
    monkeypatch.setattr(setuptools, "setup", capture_setup)
    runpy.run_path(str(Path(__file__).resolve().parents[1] / "setup.py"))
    requirements = [Requirement(value) for value in captured["install_requires"]]
    selected = [item for item in requirements if item.name == "filelock"]
    assert len(selected) == 1
    assert str(selected[0].specifier) == "==3.20.3"

