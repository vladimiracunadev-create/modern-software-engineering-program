from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PhaseFourGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.program = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
        cls.lessons = [lesson for part in cls.program["parts"] for lesson in part["lessons"]]
        cls.target = [lesson for lesson in cls.lessons if 181 <= lesson["number"] <= 360]

    def test_phase_four_scope(self) -> None:
        self.assertEqual(180, len(self.target))
        self.assertEqual("SE-181", self.target[0]["id"])
        self.assertEqual("SE-360", self.target[-1]["id"])
        self.assertEqual(
            {"first_class": "SE-181", "last_class": "SE-360", "classes": 180},
            self.program["phase_4_target"],
        )

    def test_every_phase_four_class_has_learning_contracts(self) -> None:
        for lesson in self.target:
            directory = ROOT / lesson["path"]
            text = (directory / "README.md").read_text(encoding="utf-8")
            self.assertTrue((directory / "activity.yaml").is_file(), lesson["id"])
            self.assertTrue((directory / "rubric.json").is_file(), lesson["id"])
            self.assertIn("## Reto verificable", text, lesson["id"])
            self.assertIn("## Preguntas frecuentes", text, lesson["id"])
            self.assertNotIn("## Ficha", text, lesson["id"])

    def test_phase_four_pages_are_full_and_navigable(self) -> None:
        page = (ROOT / "site/classes/SE-270.html").read_text(encoding="utf-8")
        self.assertGreaterEqual(page.count('class="class-nav"'), 2)
        self.assertIn("SE-269", page)
        self.assertIn("SE-271", page)
        self.assertIn("Práctica guiada", page)
        self.assertNotIn("scaffold navegable", page)

    def test_phase_four_sources_cover_all_parts(self) -> None:
        sources = json.loads((ROOT / "sources/phase4.json").read_text(encoding="utf-8"))
        self.assertEqual(15, len(sources["parts"]))
        self.assertTrue(all(item["url"].startswith("https://") for item in sources["sources"]))


if __name__ == "__main__":
    unittest.main()
