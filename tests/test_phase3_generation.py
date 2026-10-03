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
        self.assertEqual(Counter({"GUIDED": 120, "PLANNED": 360}), Counter(item["status"] for item in self.lessons))

    def test_phase_three_scope_is_first_180_classes(self) -> None:
        target = self.program["phase_3_target"]
        self.assertEqual({"first_class": "SE-001", "last_class": "SE-180", "classes": 180, "approved": 120}, target)

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

    def test_guided_classes_form_a_connected_visual_path(self) -> None:
        part_page = (ROOT / "site/parts/00.html").read_text(encoding="utf-8")
        self.assertIn("Caso conductor · Campus Abierto", part_page)
        self.assertIn("Guía razonada clase por clase", part_page)
        self.assertLess(
            part_page.index("SE-001 — Software, sistemas y productos"),
            part_page.index("Resumen visual del recorrido"),
        )
        self.assertEqual(12, part_page.count('class="route-number"'))
        part_one_page = (ROOT / "site/parts/01.html").read_text(encoding="utf-8")
        self.assertIn("Pulso", part_one_page)
        self.assertIn("Guía razonada clase por clase", part_one_page)
        part_two_page = (ROOT / "site/parts/02.html").read_text(encoding="utf-8")
        self.assertIn("Faro", part_two_page)
        self.assertIn("Recorrido clase por clase", part_two_page)
        part_three_page = (ROOT / "site/parts/03.html").read_text(encoding="utf-8")
        self.assertIn("Nexo", part_three_page)
        self.assertIn("Recorrido clase por clase", part_three_page)
        part_four_page = (ROOT / "site/parts/04.html").read_text(encoding="utf-8")
        self.assertIn("Atlas", part_four_page)
        self.assertIn("Recorrido clase por clase", part_four_page)
        part_five_page = (ROOT / "site/parts/05.html").read_text(encoding="utf-8")
        self.assertIn("Brújula", part_five_page)
        self.assertIn("Recorrido clase por clase", part_five_page)
        for index, lesson in enumerate(self.lessons[:120]):
            readme = (ROOT / lesson["path"] / "README.md").read_text(encoding="utf-8")
            page = (ROOT / "site/classes" / f"{lesson['id']}.html").read_text(encoding="utf-8")
            self.assertIn("## Antes de empezar", readme, lesson["id"])
            expected_case = "Campus Abierto" if index < 12 else "Pulso" if index < 24 else "Faro" if index < 36 else "Nexo" if index < 48 else "Atlas" if index < 60 else "Brújula" if index < 72 else "Prisma" if index < 84 else "Orbe" if index < 96 else "Lupa" if index < 108 else "Constelación"
            self.assertIn(expected_case, readme, lesson["id"])
            self.assertIn("## Errores comunes y cómo corregirlos", readme, lesson["id"])
            self.assertIn('class="lesson-progress"', page, lesson["id"])
            self.assertIn('class="lesson-context"', page, lesson["id"])
            self.assertIn('class="concept-map"', page, lesson["id"])

    def test_portal_reports_current_maturity(self) -> None:
        home = (ROOT / "site/index.html").read_text(encoding="utf-8")
        self.assertIn("120</strong><span>clases revisadas", home)
        self.assertIn("360</strong><span>clases por desarrollar", home)
        self.assertNotIn("0</strong><span>aprobadas", home)

    def test_prerequisite_renders_identifier_not_internal_record(self) -> None:
        text = (ROOT / self.lessons[41]["path"] / "README.md").read_text(encoding="utf-8")
        self.assertIn("`SE-041`", text)
        self.assertNotIn("{'id':", text)


if __name__ == "__main__":
    unittest.main()
