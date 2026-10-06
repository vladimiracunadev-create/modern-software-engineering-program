"""Safe, dependency-free diagnostic kit for Part 02.

The kit only mutates a `.diagnostic-kit` directory below an explicit workspace.
It never enumerates the full environment, elevates privileges, installs software,
or removes an unowned directory.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Mapping, Sequence


SCHEMA_VERSION = 1
OWNER = "modern-software-engineering-program/part-02"
MANAGED_NAME = ".diagnostic-kit"
MARKER_NAME = "owner.json"
SETTINGS_NAME = "settings.json"
CAPABILITIES_NAME = "capabilities.json"
ALLOWED_FILES = {MARKER_NAME, SETTINGS_NAME, CAPABILITIES_NAME}
DEFAULT_SETTINGS = {
    "profile": "training",
    "required_runtime": "python>=3.11",
}
SENSITIVE_FRAGMENTS = ("SECRET", "TOKEN", "PASSWORD", "CREDENTIAL", "PRIVATE", "KEY")
VISIBLE_ENVIRONMENT = ("DIAG_PROFILE", "DIAG_ENDPOINT", "DIAG_DEMO_TOKEN")


class KitError(Exception):
    """Expected failure with a stable category and exit code."""

    def __init__(self, category: str, message: str, exit_code: int = 2) -> None:
        super().__init__(message)
        self.category = category
        self.exit_code = exit_code


def _json_bytes(payload: object) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def _atomic_json(path: Path, payload: object) -> bool:
    """Write JSON atomically and return whether bytes changed."""
    expected = _json_bytes(payload)
    if path.is_file() and path.read_bytes() == expected:
        return False
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_bytes(expected)
    os.replace(temporary, path)
    return True


def _workspace(value: str) -> Path:
    path = Path(value).expanduser().resolve(strict=False)
    if not path.exists():
        raise KitError("precondition", "workspace does not exist")
    if not path.is_dir():
        raise KitError("precondition", "workspace is not a directory")
    return path


def _managed(workspace: Path) -> Path:
    managed = (workspace / MANAGED_NAME).resolve(strict=False)
    if managed.parent != workspace:
        raise KitError("safety", "managed path escaped the workspace", 3)
    return managed


def _read_json(path: Path) -> dict:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise KitError("precondition", f"missing {path.name}") from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise KitError("integrity", f"invalid {path.name}") from error
    if not isinstance(payload, dict):
        raise KitError("integrity", f"{path.name} must contain a JSON object")
    return payload


def _require_owned(managed: Path) -> dict:
    marker = _read_json(managed / MARKER_NAME)
    if marker != {"owner": OWNER, "schema_version": SCHEMA_VERSION}:
        raise KitError("safety", "ownership marker does not match this kit", 3)
    return marker


def _probe_capabilities(managed: Path) -> dict:
    """Probe only inside a temporary child and always clean it."""
    probe = Path(tempfile.mkdtemp(prefix="probe-", dir=managed))
    try:
        mixed = probe / "CaseProbe"
        mixed.write_text("synthetic\n", encoding="utf-8")
        case_sensitive = not (probe / "caseprobe").exists()
        target = probe / "target.txt"
        target.write_text("synthetic\n", encoding="utf-8")
        link = probe / "target.link"
        try:
            link.symlink_to(target.name)
            symlink = link.is_symlink() and link.read_text(encoding="utf-8") == "synthetic\n"
            symlink_note = "created inside disposable workspace"
        except (NotImplementedError, OSError) as error:
            symlink = False
            symlink_note = f"unavailable: {type(error).__name__}"
        return {
            "case_sensitive_lookup": case_sensitive,
            "path_separator": os.sep,
            "symlink_supported": symlink,
            "symlink_note": symlink_note,
        }
    finally:
        shutil.rmtree(probe)


def prepare(workspace: Path) -> dict:
    managed = _managed(workspace)
    if managed.exists() and not managed.is_dir():
        raise KitError("safety", "managed path exists but is not a directory", 3)
    managed.mkdir(exist_ok=True)
    marker_path = managed / MARKER_NAME
    if marker_path.exists():
        _require_owned(managed)
    changed = []
    marker = {"owner": OWNER, "schema_version": SCHEMA_VERSION}
    if _atomic_json(marker_path, marker):
        changed.append(MARKER_NAME)
    if _atomic_json(managed / SETTINGS_NAME, DEFAULT_SETTINGS):
        changed.append(SETTINGS_NAME)
    capabilities = _probe_capabilities(managed)
    if _atomic_json(managed / CAPABILITIES_NAME, capabilities):
        changed.append(CAPABILITIES_NAME)
    return {
        "command": "prepare",
        "status": "changed" if changed else "unchanged",
        "changed": changed,
        "managed_path": MANAGED_NAME,
    }


def _redacted_environment(environ: Mapping[str, str]) -> dict:
    result = {}
    for name in VISIBLE_ENVIRONMENT:
        if name not in environ:
            result[name] = {"present": False}
            continue
        value = environ[name]
        sensitive = any(fragment in name.upper() for fragment in SENSITIVE_FRAGMENTS)
        result[name] = {
            "present": True,
            "value": "[REDACTED]" if sensitive else value,
            "length": len(value) if sensitive else None,
        }
    return result


def _effective_profile(settings: Mapping[str, object], environ: Mapping[str, str], cli: str | None) -> dict:
    value = settings.get("profile", DEFAULT_SETTINGS["profile"])
    source = "settings"
    if "DIAG_PROFILE" in environ:
        value = environ["DIAG_PROFILE"]
        source = "environment"
    if cli is not None:
        value = cli
        source = "argument"
    if not isinstance(value, str) or not value.strip():
        raise KitError("configuration", "profile must be a non-empty string")
    return {"value": value, "source": source}


def inspect(workspace: Path, profile: str | None, environ: Mapping[str, str]) -> tuple[dict, int]:
    managed = _managed(workspace)
    findings = []
    try:
        _require_owned(managed)
        settings = _read_json(managed / SETTINGS_NAME)
        capabilities = _read_json(managed / CAPABILITIES_NAME)
        effective = _effective_profile(settings, environ, profile)
        status = "healthy"
        exit_code = 0
    except KitError as error:
        settings = {}
        capabilities = {}
        effective = None
        status = "degraded"
        exit_code = error.exit_code
        findings.append({"category": error.category, "message": str(error)})
    report = {
        "schema_version": SCHEMA_VERSION,
        "command": "inspect",
        "status": status,
        "platform": {
            "system": platform.system(),
            "machine": platform.machine(),
            "python_implementation": platform.python_implementation(),
            "python_version": platform.python_version(),
        },
        "workspace": {"managed_path": MANAGED_NAME, "owned": status == "healthy"},
        "capabilities": capabilities,
        "configuration": {"profile": effective} if effective else {},
        "environment": _redacted_environment(environ),
        "findings": findings,
        "limits": [
            "does not enumerate users, hostname, serial numbers, processes or the full environment",
            "does not prove compatibility beyond the executed platform and tests",
            "does not elevate privileges, install packages or change system configuration",
        ],
    }
    return report, exit_code


def repair(workspace: Path) -> dict:
    managed = _managed(workspace)
    _require_owned(managed)
    changed = []
    if _atomic_json(managed / SETTINGS_NAME, DEFAULT_SETTINGS):
        changed.append(SETTINGS_NAME)
    capabilities = _probe_capabilities(managed)
    if _atomic_json(managed / CAPABILITIES_NAME, capabilities):
        changed.append(CAPABILITIES_NAME)
    return {
        "command": "repair",
        "status": "changed" if changed else "unchanged",
        "changed": changed,
        "rollback": "clean removes only the three owned files when no unknown file exists",
    }


def clean(workspace: Path) -> dict:
    managed = _managed(workspace)
    _require_owned(managed)
    entries = {entry.name for entry in managed.iterdir()}
    unknown = sorted(entries - ALLOWED_FILES)
    if unknown:
        raise KitError("safety", f"refusing cleanup; unknown entries: {', '.join(unknown)}", 3)
    for name in sorted(ALLOWED_FILES):
        path = managed / name
        if path.is_file() or path.is_symlink():
            path.unlink()
    managed.rmdir()
    return {"command": "clean", "status": "removed", "managed_path": MANAGED_NAME}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Safe Part 02 cross-platform diagnostic kit")
    parser.add_argument("command", choices=("prepare", "inspect", "repair", "clean"))
    parser.add_argument("--workspace", required=True, help="existing disposable workspace")
    parser.add_argument("--profile", help="override DIAG_PROFILE and settings.json")
    return parser


def main(argv: Sequence[str] | None = None, environ: Mapping[str, str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    environment = os.environ if environ is None else environ
    try:
        workspace = _workspace(args.workspace)
        if args.command == "prepare":
            payload, exit_code = prepare(workspace), 0
        elif args.command == "inspect":
            payload, exit_code = inspect(workspace, args.profile, environment)
        elif args.command == "repair":
            payload, exit_code = repair(workspace), 0
        else:
            payload, exit_code = clean(workspace), 0
    except KitError as error:
        payload = {
            "schema_version": SCHEMA_VERSION,
            "command": args.command,
            "status": "refused" if error.exit_code == 3 else "degraded",
            "findings": [{"category": error.category, "message": str(error)}],
        }
        exit_code = error.exit_code
    print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
