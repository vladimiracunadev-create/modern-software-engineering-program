from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_builder():
    path = ROOT / "scripts" / "build_program_blueprint.py"
    spec = importlib.util.spec_from_file_location("build_program_blueprint", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Cannot load blueprint builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProgramBlueprintTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.builder = load_builder()
        cls.payload = cls.builder.build_payload()

    def test_program_has_expected_shape(self) -> None:
        self.assertEqual(8, len(self.payload["stages"]))
        self.assertEqual(40, len(self.payload["parts"]))
        self.assertEqual(480, self.payload["class_count"])
        self.assertEqual(2160, self.payload["estimated_hours"])

    def test_identifiers_are_unique_and_sequential(self) -> None:
        lessons = [lesson for part in self.payload["parts"] for lesson in part["lessons"]]
        self.assertEqual(
            [f"SE-{number:03d}" for number in range(1, 481)],
            [lesson["id"] for lesson in lessons],
        )

    def test_each_part_has_ten_classes_studio_and_project(self) -> None:
        for part in self.payload["parts"]:
            self.assertEqual(12, len(part["lessons"]))
            self.assertEqual(
                ["class"] * 10 + ["studio", "project"],
                [lesson["kind"] for lesson in part["lessons"]],
            )

    def test_generated_manifest_matches_builder(self) -> None:
        generated = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
        self.assertEqual(self.payload, generated)

    def test_phase_three_rebuild_is_honest(self) -> None:
        statuses = [
            lesson["status"]
            for part in self.payload["parts"]
            for lesson in part["lessons"]
        ]
        self.assertEqual(["GUIDED"] * 60 + ["PLANNED"] * 420, statuses)
        self.assertEqual("PHASE_3_AND_4_REBUILDING", self.payload["status"])
        self.assertEqual(180, self.payload["phase_3_target"]["classes"])
        self.assertEqual(60, self.payload["phase_3_target"]["approved"])
        self.assertEqual(180, self.payload["phase_4_target"]["classes"])
        self.assertEqual("SE-181", self.payload["phase_4_target"]["first_class"])
        self.assertEqual("SE-360", self.payload["phase_4_target"]["last_class"])
        self.assertEqual(0, self.payload["phase_4_target"]["approved"])


if __name__ == "__main__":
    unittest.main()
