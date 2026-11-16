from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import program_state as ps  # noqa: E402


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
        developed = ps.developed_parts()
        self.assertEqual(8, len(self.payload["stages"]))
        self.assertEqual(len(developed), len(self.payload["parts"]))
        self.assertEqual(len(developed), self.payload["part_count"])
        self.assertEqual(12 * len(developed), self.payload["class_count"])
        self.assertEqual(ps.developed_hours(), self.payload["estimated_hours"])

    def test_planned_scope_is_declared_and_honest(self) -> None:
        scope = self.payload["planned_scope"]
        self.assertEqual((45, 540, ps.planned_hours()), (scope["part_count"], scope["class_count"], scope["estimated_hours"]))
        self.assertEqual("SE-540", scope["last_class"])
        pending = [item["id"] for item in scope["unpublished_parts"]]
        self.assertEqual([f"{n:02d}" for n in ps.planned_parts()], pending)
        published = {part["id"] for part in self.payload["parts"]}
        self.assertFalse(published & set(pending))
        self.assertTrue(all(item["status"] == "planned" for item in scope["unpublished_parts"]))

    def test_full_plan_defines_540_classes_in_45_parts(self) -> None:
        plan = self.builder.build_full_plan()
        self.assertEqual(45, len(plan))
        numbers = [lesson["number"] for part in plan for lesson in part["lessons"]]
        self.assertEqual(list(range(1, 541)), numbers)
        titles = [lesson["title"].casefold() for part in plan for lesson in part["lessons"]]
        self.assertEqual(len(titles), len(set(titles)))

    def test_identifiers_are_unique_and_sequential(self) -> None:
        lessons = [lesson for part in self.payload["parts"] for lesson in part["lessons"]]
        self.assertEqual(
            [class_id for number in ps.developed_parts() for class_id in ps.class_ids(number)],
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

    def test_phase_scopes_do_not_create_class_states(self) -> None:
        lessons = [lesson for part in self.payload["parts"] for lesson in part["lessons"]]
        self.assertTrue(all("status" not in lesson for lesson in lessons))
        self.assertNotIn("status", self.payload)
        self.assertEqual(180, self.payload["phase_3_target"]["classes"])
        self.assertEqual(180, self.payload["phase_4_target"]["classes"])
        self.assertEqual("SE-181", self.payload["phase_4_target"]["first_class"])
        self.assertEqual("SE-360", self.payload["phase_4_target"]["last_class"])


if __name__ == "__main__":
    unittest.main()
