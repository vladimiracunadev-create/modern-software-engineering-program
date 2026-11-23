"""La navegación anterior/siguiente salta los huecos de las partes planificadas (ADR-007).

Las Partes 34 y 42 están reservadas: sus números no tienen clases. La navegación de las
588 clases desarrolladas debe enlazar con la vecina desarrollada en ambos sentidos, hacia
arriba y hacia abajo del hueco, y no debe enlazar nunca con una clase reservada.
"""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import program_state as ps  # noqa: E402

PROGRAM = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
FLAT = [lesson for part in PROGRAM["parts"] for lesson in part["lessons"]]
ID_RE = re.compile(r"(?i:SE)-(\d{3})")


def reserved_ids() -> set[str]:
    return {class_id for part in ps.planned_parts() for class_id in ps.class_ids(part)}


class NavigationGapTests(unittest.TestCase):
    def test_flat_order_skips_exactly_the_reserved_ids(self) -> None:
        ids = [lesson["id"] for lesson in FLAT]
        self.assertEqual(sorted(ids), ids)
        self.assertEqual(len(ids), ps.developed_class_count())
        self.assertFalse(set(ids) & reserved_ids())

    def test_neighbours_across_every_gap_in_both_directions(self) -> None:
        by_id = {lesson["id"]: index for index, lesson in enumerate(FLAT)}
        gaps = 0
        for part in ps.planned_parts():
            before, after = f"SE-{ps.part_first_class(part) - 1:03d}", f"SE-{ps.part_last_class(part) + 1:03d}"
            if before not in by_id or after not in by_id:
                continue
            gaps += 1
            self.assertEqual(by_id[before] + 1, by_id[after], f"hueco de la Parte {part:02d}")
            self._assert_nav(before, following=after)
            self._assert_nav(after, previous=before)
        self.assertGreaterEqual(gaps, 2)

    def test_every_class_links_its_developed_neighbours_only(self) -> None:
        reserved = reserved_ids()
        for index, lesson in enumerate(FLAT):
            previous = FLAT[index - 1]["id"] if index else None
            following = FLAT[index + 1]["id"] if index + 1 < len(FLAT) else None
            self._assert_nav(lesson["id"], previous=previous, following=following)
            readme = (ROOT / lesson["path"] / "README.md").read_text(encoding="utf-8")
            page = (ROOT / "site" / "classes" / f"{lesson['id']}.html").read_text(encoding="utf-8")
            nav = readme.split("\n", 3)[2]
            nav_ids = set(f"SE-{n}" for n in ID_RE.findall(nav))
            self.assertFalse(nav_ids & reserved, lesson["id"])
            page_nav = re.search(r'<nav class="class-nav".*?</nav>', page, re.S)
            self.assertIsNotNone(page_nav, lesson["id"])
            self.assertFalse(set(f"SE-{n}" for n in ID_RE.findall(page_nav.group(0))) & reserved, lesson["id"])

    def test_first_and_last_have_boundary_markers(self) -> None:
        first, last = FLAT[0], FLAT[-1]
        self.assertIn("← Inicio del programa", (ROOT / first["path"] / "README.md").read_text(encoding="utf-8"))
        self.assertIn("Fin del programa →", (ROOT / last["path"] / "README.md").read_text(encoding="utf-8"))

    def test_reserved_urls_are_empty_and_404_explains_the_renumbering(self) -> None:
        for part in ps.planned_parts():
            self.assertFalse((ROOT / "site" / "parts" / f"{part:02d}.html").exists())
            for class_id in ps.class_ids(part):
                self.assertFalse((ROOT / "site" / "classes" / f"{class_id}.html").exists(), class_id)
        page = (ROOT / "site" / "404.html").read_text(encoding="utf-8")
        self.assertIn("legacy/index.html", page)
        self.assertIn("numeración anterior", page)

    def _assert_nav(self, class_id: str, previous: str | None = None, following: str | None = None) -> None:
        lesson = next(item for item in FLAT if item["id"] == class_id)
        readme = (ROOT / lesson["path"] / "README.md").read_text(encoding="utf-8")
        page = (ROOT / "site" / "classes" / f"{class_id}.html").read_text(encoding="utf-8")
        nav = readme.split("\n", 3)[2]
        if previous:
            self.assertIn(f"/{previous.lower()}-", nav, class_id)
            self.assertIn(f'href="{previous}.html">← {previous}</a>', page, class_id)
        if following:
            self.assertIn(f"/{following.lower()}-", nav, class_id)
            self.assertIn(f'href="{following}.html">{following} →</a>', page, class_id)


if __name__ == "__main__":
    unittest.main()
