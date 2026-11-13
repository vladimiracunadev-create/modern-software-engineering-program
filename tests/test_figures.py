"""Structural checks for the static SVG figures of Parts 00 and 01."""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_figures import FIGURES, collect  # noqa: E402

PARTS = {"00": range(1, 13), "01": range(13, 25), "02": range(25, 37), "03": range(37, 49), "04": range(49, 61), "05": range(61, 73), "06": range(73, 85), "07": range(85, 97)}


class FigureTests(unittest.TestCase):
    def test_every_figure_is_accessible_and_sized(self) -> None:
        for name, builder in FIGURES.items():
            svg = builder().svg()
            self.assertIn('role="img"', svg, name)
            self.assertRegex(svg, r"<title id=\"t\">[^<]{10,}</title>", name)
            self.assertRegex(svg, r"<desc id=\"d\">[^<]{40,}</desc>", name)
            sizes = [int(v) for v in re.findall(r'font-size="(\d+)"', svg)]
            self.assertTrue(sizes and min(sizes) >= 11, f"{name}: text too small")

    def test_every_lesson_references_at_least_three_figures(self) -> None:
        for part, numbers in PARTS.items():
            for number in numbers:
                lesson = f"SE-{number:03d}"
                text = (ROOT / "content" / f"part-{part}" / f"{lesson}.md").read_text(encoding="utf-8")
                refs = re.findall(r"\]\(figures/([^)\s]+)\)", text)
                self.assertGreaterEqual(len(refs), 3, lesson)
                self.assertEqual(len(refs), len(set(refs)), f"{lesson} repeats a figure")
                for ref in refs:
                    self.assertIn(ref, FIGURES, f"{lesson} references an unknown figure {ref}")
                flat = re.sub(r"\s+", " ", text)
                self.assertEqual(flat.count("**Cómo leer la figura.**"), len(refs), lesson)
                self.assertEqual(flat.count("**Dónde deja de valer"), len(refs), lesson)
                self.assertIn("## Puente hacia el trabajo con agentes", text, lesson)

    def test_every_figure_is_used_by_a_lesson(self) -> None:
        used = set()
        for part, numbers in PARTS.items():
            for number in numbers:
                text = (ROOT / "content" / f"part-{part}" / f"SE-{number:03d}.md").read_text(encoding="utf-8")
                used.update(re.findall(r"\]\(figures/([^)\s]+)\)", text))
        self.assertEqual(set(FIGURES) - used, set())

    def test_committed_svgs_match_definitions(self) -> None:
        for path, builder in collect().items():
            self.assertEqual(path.read_text(encoding="utf-8"), builder().svg(), path.name)


if __name__ == "__main__":
    unittest.main()
