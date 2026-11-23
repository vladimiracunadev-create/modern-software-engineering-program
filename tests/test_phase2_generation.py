from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import program_state as ps  # noqa: E402


class PhaseTwoGenerationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.program = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))

    def test_every_class_has_scaffold_and_metadata(self) -> None:
        for part in self.program["parts"]:
            for lesson in part["lessons"]:
                directory = ROOT / lesson["path"]
                self.assertTrue((directory / "README.md").is_file(), lesson["id"])
                self.assertTrue((directory / "lesson.json").is_file(), lesson["id"])

    def test_part_and_class_counts_on_disk(self) -> None:
        parts = list((ROOT / "classes").glob("part-*"))
        metadata = list((ROOT / "classes").glob("part-*/se-*/lesson.json"))
        self.assertEqual(len(ps.developed_parts()), len(parts))
        self.assertEqual(ps.developed_class_count(), len(metadata))

    def test_source_registry_covers_every_class(self) -> None:
        registry = json.loads((ROOT / "sources/class-sources.json").read_text(encoding="utf-8"))
        expected = {class_id for number in ps.developed_parts() for class_id in ps.class_ids(number)}
        self.assertEqual(len(expected), registry["class_count"])
        self.assertEqual(expected, set(registry["classes"]))
        self.assertTrue(all(item["source_ids"] for item in registry["classes"].values()))

    def test_site_contains_landing_parts_and_classes(self) -> None:
        pages = [
            page
            for page in (ROOT / "site").rglob("*.html")
            if page.relative_to(ROOT / "site").parts[0] not in ("casos", "glosario", "legacy")
            and page.relative_to(ROOT / "site").as_posix() != "404.html"
        ]
        self.assertEqual(1 + len(ps.developed_parts()) + ps.developed_class_count(), len(pages))
        self.assertTrue((ROOT / "site/index.html").is_file())
        for number in ps.developed_parts():
            self.assertTrue((ROOT / "site/classes" / f"{ps.class_ids(number)[-1]}.html").is_file())
        for number in ps.planned_parts():
            self.assertFalse((ROOT / "site/classes" / f"{ps.class_ids(number)[0]}.html").exists())

    def test_site_uses_current_program_name(self) -> None:
        current_name = "Programa de Ingeniería de Software Moderna"
        retired_name = "Software Engineering Learning Suite"
        for page in (ROOT / "site").rglob("*.html"):
            text = page.read_text(encoding="utf-8")
            self.assertIn(current_name, text, page.relative_to(ROOT))
            self.assertNotIn(retired_name, text, page.relative_to(ROOT))

    def test_web_catalog_matches_manifest(self) -> None:
        catalog = json.loads((ROOT / "site/assets/catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(ps.developed_class_count(), len(catalog["classes"]))
        self.assertEqual("SE-001", catalog["classes"][0]["id"])
        self.assertEqual(ps.class_ids(ps.developed_parts()[-1])[-1], catalog["classes"][-1]["id"])

    def test_class_index_links_every_class_and_portal_page(self) -> None:
        index = (ROOT / "classes/README.md").read_text(encoding="utf-8")
        for part in self.program["parts"]:
            part_folder = Path(part["path"]).name
            for lesson in part["lessons"]:
                lesson_folder = Path(lesson["path"]).name
                self.assertIn(f"({part_folder}/{lesson_folder}/README.md)", index, lesson["id"])
                self.assertIn(f"/classes/{lesson['id']}.html)", index, lesson["id"])

    def test_classes_have_navigation_and_no_record_table(self) -> None:
        lessons = [lesson for part in self.program["parts"] for lesson in part["lessons"]]
        for lesson in lessons:
            text = (ROOT / lesson["path"] / "README.md").read_text(encoding="utf-8")
            self.assertNotIn("## Ficha", text, lesson["id"])
            self.assertNotIn("| Campo | Valor |", text, lesson["id"])
            self.assertIn("Índice completo", text, lesson["id"])
            part_id = Path(lesson["path"]).parts[-2].split("-")[1]
            self.assertIn(f"↑ Parte {part_id}", text, lesson["id"])

    def test_middle_class_links_to_both_neighbors(self) -> None:
        text = (ROOT / self.program["parts"][3]["lessons"][5]["path"] / "README.md").read_text(encoding="utf-8")
        self.assertIn("SE-041", text)
        self.assertIn("SE-043", text)


if __name__ == "__main__":
    unittest.main()
