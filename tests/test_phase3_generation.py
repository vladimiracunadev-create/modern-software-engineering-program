from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PhaseThreeGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.program = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
        cls.lessons = [lesson for part in cls.program["parts"] for lesson in part["lessons"]]

    def test_curriculum_has_no_class_workflow_states(self) -> None:
        self.assertTrue(all("status" not in item for item in self.lessons))

    def test_phase_three_scope_is_first_180_classes(self) -> None:
        target = self.program["phase_3_target"]
        self.assertEqual({"first_class": "SE-001", "last_class": "SE-180", "classes": 180}, target)

    def test_phase_three_drafts_have_activity_and_rubric(self) -> None:
        for lesson in self.lessons:
            if lesson["number"] > 180:
                continue
            directory = ROOT / lesson["path"]
            self.assertTrue((directory / "activity.yaml").is_file(), lesson["id"])
            self.assertTrue((directory / "rubric.json").is_file(), lesson["id"])

    def test_classes_do_not_publish_workflow_state_labels(self) -> None:
        for lesson in self.lessons:
            text = (ROOT / lesson["path"] / "README.md").read_text(encoding="utf-8")
            self.assertNotIn("> Estado:", text, lesson["id"])

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

    def test_developed_classes_form_a_connected_visual_path(self) -> None:
        part_page = (ROOT / "site/parts/00.html").read_text(encoding="utf-8")
        self.assertIn("Caso conductor · Campus Abierto", part_page)
        self.assertIn("Guía razonada clase por clase", part_page)
        self.assertLess(
            part_page.index("SE-001 — Software, sistemas y productos"),
            part_page.index("Resumen visual del recorrido"),
        )
        self.assertEqual(12, part_page.count('class="route-number"'))
        part_labels = {
            "01": "analizador local de eventos",
            "02": "kit de diagnóstico multiplataforma",
            "03": "petición observable de extremo a extremo",
            "04": "modelo de decisión diagnóstica",
            "05": "CLI diagnóstica",
            "06": "motor de reglas comparado",
            "07": "biblioteca de estructuras y algoritmos",
            "08": "entorno reproducible de diagnóstico",
            "09": "producto reutilizable con SDK y CLI",
        }
        for part_id, label in part_labels.items():
            part_page = (ROOT / "site/parts" / f"{part_id}.html").read_text(encoding="utf-8")
            self.assertIn(label, part_page)
            self.assertIn("Guía razonada clase por clase", part_page)
        for part in self.program["parts"][:10]:
            part_page = (ROOT / "site/parts" / f"{part['id']}.html").read_text(encoding="utf-8")
            self.assertIn("Guía razonada clase por clase", part_page, part["id"])
            self.assertIn("Resumen operativo del recorrido", part_page, part["id"])
            source = (ROOT / "content" / f"part-{part['id']}" / "README.md").read_text(encoding="utf-8")
            guide = source.split("## Guía razonada clase por clase", 1)[1].split("## Resumen operativo del recorrido", 1)[0]
            for lesson in part["lessons"]:
                self.assertIn(f"{lesson['id']} —", guide, lesson["id"])
                self.assertIn(f'<h4 id="{lesson["id"].lower()}-', part_page, lesson["id"])
        for index, lesson in enumerate(self.lessons[:120]):
            readme = (ROOT / lesson["path"] / "README.md").read_text(encoding="utf-8")
            page = (ROOT / "site/classes" / f"{lesson['id']}.html").read_text(encoding="utf-8")
            self.assertIn("## Antes de empezar", readme, lesson["id"])
            part_number = index // 12
            expected_case = "Campus Abierto" if part_number == 0 else part_labels[f"{part_number:02d}"]
            self.assertIn(expected_case, readme, lesson["id"])
            self.assertIn("## Errores comunes y cómo corregirlos", readme, lesson["id"])
            self.assertIn('class="lesson-progress"', page, lesson["id"])
            self.assertIn('class="lesson-context"', page, lesson["id"])
            self.assertIn('class="concept-map"', page, lesson["id"])

    def test_portal_reports_program_shape_without_class_states(self) -> None:
        home = (ROOT / "site/index.html").read_text(encoding="utf-8")
        self.assertIn("480</strong><span>clases en el recorrido", home)
        self.assertNotIn("data-status", home)
        self.assertNotIn("class-status", home)

    def test_prerequisite_renders_identifier_not_internal_record(self) -> None:
        text = (ROOT / self.lessons[41]["path"] / "README.md").read_text(encoding="utf-8")
        self.assertIn("`SE-041`", text)
        self.assertNotIn("{'id':", text)


if __name__ == "__main__":
    unittest.main()
