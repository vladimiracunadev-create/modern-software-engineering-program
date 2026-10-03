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
        self.assertEqual(Counter({"GUIDED": 12, "PLANNED": 468}), Counter(item["status"] for item in self.lessons))

    def test_phase_three_scope_is_first_180_classes(self) -> None:
        target = self.program["phase_3_target"]
        self.assertEqual({"first_class": "SE-001", "last_class": "SE-180", "classes": 180, "approved": 12}, target)

    def test_phase_three_drafts_have_activity_and_rubric(self) -> None:
        for lesson in self.lessons:
            if lesson["number"] > 180:
                continue
            directory = ROOT / lesson["path"]
            self.assertTrue((directory / "activity.yaml").is_file(), lesson["id"])
            self.assertTrue((directory / "rubric.json").is_file(), lesson["id"])

    def test_only_approved_classes_claim_guided(self) -> None:
        for lesson in self.lessons:
            text = (ROOT / lesson["path"] / "README.md").read_text(encoding="utf-8")
            if lesson["status"] == "GUIDED":
                self.assertIn("Estado: **GUIDED**", text, lesson["id"])
            else:
                self.assertNotIn("Estado: **GUIDED**", text, lesson["id"])

    def test_phase_three_source_registry_is_primary_or_official(self) -> None:
        sources = json.loads((ROOT / "sources/phase3.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(sources["sources"]), 20)
        self.assertTrue(all(item["url"].startswith("https://") for item in sources["sources"]))
        self.assertEqual(15, len(sources["parts"]))

    def test_phase_three_drafts_have_deeper_learning_sections(self) -> None:
        required = (
            "## Temas y por qué importan",
            "## Definiciones de trabajo",
            "## Reto verificable",
            "## Preguntas frecuentes",
        )
        for lesson in self.lessons[:180]:
            text = (ROOT / lesson["path"] / "README.md").read_text(encoding="utf-8")
            for heading in required:
                self.assertIn(heading, text, lesson["id"])

    def test_phase_three_pages_have_bidirectional_navigation(self) -> None:
        page = (ROOT / "site/classes/SE-090.html").read_text(encoding="utf-8")
        self.assertGreaterEqual(page.count('class="class-nav"'), 2)
        self.assertIn("SE-089", page)
        self.assertIn("SE-091", page)
        self.assertNotIn("](", page)

    def test_prerequisite_renders_identifier_not_internal_record(self) -> None:
        text = (ROOT / self.lessons[41]["path"] / "README.md").read_text(encoding="utf-8")
        self.assertIn("diagnosticado `SE-041`", text)
        self.assertNotIn("{'id':", text)


if __name__ == "__main__":
    unittest.main()
