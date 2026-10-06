from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path


LAB = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("part02_diagnostic_kit", LAB / "diagnostic_kit.py")
assert SPEC and SPEC.loader
kit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(kit)


class DiagnosticKitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=LAB)
        self.workspace = Path(self.temporary.name).resolve()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def invoke(self, *arguments: str, environ: dict[str, str] | None = None) -> tuple[int, dict]:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = kit.main(arguments, environ={} if environ is None else environ)
        return code, json.loads(output.getvalue())

    def prepare(self) -> dict:
        code, payload = self.invoke("prepare", "--workspace", str(self.workspace))
        self.assertEqual(0, code, payload)
        return payload

    def test_prepare_is_idempotent(self) -> None:
        first = self.prepare()
        second = self.prepare()
        self.assertEqual("changed", first["status"])
        self.assertEqual("unchanged", second["status"])

    def test_inspect_uses_stable_schema_without_personal_identifiers(self) -> None:
        self.prepare()
        code, report = self.invoke("inspect", "--workspace", str(self.workspace))
        self.assertEqual(0, code)
        self.assertEqual(1, report["schema_version"])
        self.assertNotIn("hostname", report["platform"])
        self.assertNotIn("username", report["platform"])
        self.assertEqual({"managed_path": ".diagnostic-kit", "owned": True}, report["workspace"])

    def test_configuration_precedence_is_argument_environment_file_default(self) -> None:
        self.prepare()
        code, report = self.invoke(
            "inspect", "--workspace", str(self.workspace), environ={"DIAG_PROFILE": "environment"}
        )
        self.assertEqual(0, code)
        self.assertEqual({"source": "environment", "value": "environment"}, report["configuration"]["profile"])
        code, report = self.invoke(
            "inspect", "--workspace", str(self.workspace), "--profile", "argument",
            environ={"DIAG_PROFILE": "environment"},
        )
        self.assertEqual(0, code)
        self.assertEqual({"source": "argument", "value": "argument"}, report["configuration"]["profile"])

    def test_secret_sentinel_is_redacted(self) -> None:
        self.prepare()
        sentinel = "NEVER-PRINT-THIS-SECRET"
        code, report = self.invoke(
            "inspect", "--workspace", str(self.workspace), environ={"DIAG_DEMO_TOKEN": sentinel}
        )
        self.assertEqual(0, code)
        serialized = json.dumps(report)
        self.assertNotIn(sentinel, serialized)
        self.assertIn("[REDACTED]", serialized)

    def test_corrupt_settings_produce_structured_degradation(self) -> None:
        self.prepare()
        settings = self.workspace / kit.MANAGED_NAME / kit.SETTINGS_NAME
        settings.write_text("{broken", encoding="utf-8")
        code, report = self.invoke("inspect", "--workspace", str(self.workspace))
        self.assertEqual(2, code)
        self.assertEqual("degraded", report["status"])
        self.assertEqual("integrity", report["findings"][0]["category"])

    def test_repair_restores_corrupt_settings(self) -> None:
        self.prepare()
        settings = self.workspace / kit.MANAGED_NAME / kit.SETTINGS_NAME
        settings.write_text("{broken", encoding="utf-8")
        code, repaired = self.invoke("repair", "--workspace", str(self.workspace))
        self.assertEqual(0, code, repaired)
        code, report = self.invoke("inspect", "--workspace", str(self.workspace))
        self.assertEqual(0, code)
        self.assertEqual("healthy", report["status"])

    def test_clean_removes_only_owned_directory(self) -> None:
        self.prepare()
        survivor = self.workspace / "keep.txt"
        survivor.write_text("keep\n", encoding="utf-8")
        code, report = self.invoke("clean", "--workspace", str(self.workspace))
        self.assertEqual(0, code, report)
        self.assertTrue(survivor.is_file())
        self.assertFalse((self.workspace / kit.MANAGED_NAME).exists())

    def test_clean_refuses_unknown_entries(self) -> None:
        self.prepare()
        unknown = self.workspace / kit.MANAGED_NAME / "student-notes.txt"
        unknown.write_text("preserve\n", encoding="utf-8")
        code, report = self.invoke("clean", "--workspace", str(self.workspace))
        self.assertEqual(3, code)
        self.assertEqual("refused", report["status"])
        self.assertTrue(unknown.is_file())

    def test_missing_workspace_never_gets_created(self) -> None:
        missing = self.workspace / "missing"
        code, report = self.invoke("prepare", "--workspace", str(missing))
        self.assertEqual(2, code)
        self.assertEqual("degraded", report["status"])
        self.assertFalse(missing.exists())

    def test_foreign_marker_blocks_repair_and_cleanup(self) -> None:
        managed = self.workspace / kit.MANAGED_NAME
        managed.mkdir()
        (managed / kit.MARKER_NAME).write_text('{"owner":"someone-else","schema_version":1}\n', encoding="utf-8")
        for command in ("repair", "clean"):
            code, report = self.invoke(command, "--workspace", str(self.workspace))
            self.assertEqual(3, code)
            self.assertEqual("refused", report["status"])
        self.assertTrue(managed.exists())


if __name__ == "__main__":
    unittest.main()
