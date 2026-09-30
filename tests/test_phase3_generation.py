from __future__ import annotations

import json
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PhaseThreeGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.program = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
        cls.lessons = [lesson for part in cls.program["parts"] for lesson in part["lessons"]]

    def test_maturity_counts(self) -> None:
        self.assertEqual(Counter({"PLANNED": 324, "GUIDED": 156}), Counter(item["status"] for item in self.lessons))

    def test_guided_scope_is_stages_a_and_c(self) -> None:
        guided_stages = {
            part["stage"] for part in self.program["parts"]
            if any(lesson["status"] == "GUIDED" for lesson in part["lessons"])
        }
        self.assertEqual({"A", "C"}, guided_stages)

    def test_guided_classes_have_activity_and_rubric(self) -> None:
        for lesson in self.lessons:
            if lesson["status"] != "GUIDED":
                continue
            directory = ROOT / lesson["path"]
            self.assertTrue((directory / "activity.yaml").is_file(), lesson["id"])
            self.assertTrue((directory / "rubric.json").is_file(), lesson["id"])

    def test_planned_classes_do_not_claim_guided(self) -> None:
        for lesson in self.lessons:
            if lesson["status"] != "PLANNED":
                continue
            text = (ROOT / lesson["path"] / "README.md").read_text(encoding="utf-8")
            self.assertIn("Estado: **PLANNED**", text, lesson["id"])

    def test_phase_three_source_registry_is_primary_or_official(self) -> None:
        sources = json.loads((ROOT / "sources/phase3.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(sources["sources"]), 20)
        self.assertTrue(all(item["url"].startswith("https://") for item in sources["sources"]))
        self.assertEqual(13, len(sources["parts"]))


if __name__ == "__main__":
    unittest.main()
