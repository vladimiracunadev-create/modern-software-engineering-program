from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


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
        self.assertEqual(40, len(parts))
        self.assertEqual(480, len(metadata))

    def test_source_registry_covers_every_class(self) -> None:
        registry = json.loads((ROOT / "sources/class-sources.json").read_text(encoding="utf-8"))
        self.assertEqual(480, registry["class_count"])
        self.assertEqual({f"SE-{number:03d}" for number in range(1, 481)}, set(registry["classes"]))
        self.assertTrue(all(item["source_ids"] for item in registry["classes"].values()))

    def test_site_contains_landing_parts_and_classes(self) -> None:
        pages = list((ROOT / "site").rglob("*.html"))
        self.assertEqual(521, len(pages))
        self.assertTrue((ROOT / "site/index.html").is_file())
        self.assertTrue((ROOT / "site/classes/SE-480.html").is_file())

    def test_web_catalog_matches_manifest(self) -> None:
        catalog = json.loads((ROOT / "site/assets/catalog.json").read_text(encoding="utf-8"))
        self.assertEqual(480, len(catalog["classes"]))
        self.assertEqual("SE-001", catalog["classes"][0]["id"])
        self.assertEqual("SE-480", catalog["classes"][-1]["id"])

    def test_class_index_links_every_class_and_portal_page(self) -> None:
        index = (ROOT / "classes/README.md").read_text(encoding="utf-8")
        for part in self.program["parts"]:
            part_folder = Path(part["path"]).name
            for lesson in part["lessons"]:
                lesson_folder = Path(lesson["path"]).name
                self.assertIn(f"({part_folder}/{lesson_folder}/README.md)", index, lesson["id"])
                self.assertIn(f"/classes/{lesson['id']}.html)", index, lesson["id"])


if __name__ == "__main__":
    unittest.main()
