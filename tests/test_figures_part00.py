"""Structural checks for the static SVG figures of Part 00."""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_figures_part00 import FIGURES  # noqa: E402


class FigureTests(unittest.TestCase):
    def test_every_figure_is_accessible_and_sized(self) -> None:
        for name, builder in FIGURES.items():
            svg = builder().svg()
            self.assertIn('role="img"', svg, name)
            self.assertRegex(svg, r"<title id=\"t\">[^<]{10,}</title>", name)
            self.assertRegex(svg, r"<desc id=\"d\">[^<]{40,}</desc>", name)
            sizes = [int(v) for v in re.findall(r'font-size="(\d+)"', svg)]
            self.assertTrue(sizes and min(sizes) >= 12, f"{name}: text too small")

    def test_every_lesson_has_three_referenced_figures(self) -> None:
        for number in range(1, 13):
            lesson = f"SE-{number:03d}"
            text = (ROOT / "content" / "part-00" / f"{lesson}.md").read_text(encoding="utf-8")
            refs = re.findall(r"\]\(figures/([^)\s]+)\)", text)
            self.assertEqual(len(refs), 3, lesson)
            for ref in refs:
                self.assertIn(ref, FIGURES, f"{lesson} references an unknown figure {ref}")
            flat = re.sub(r"\s+", " ", text)
            self.assertEqual(flat.count("**Cómo leer la figura.**"), 3, lesson)
            self.assertEqual(flat.count("**Dónde deja de valer"), 3, lesson)
            self.assertIn("## Puente hacia el trabajo con agentes", text, lesson)

    def test_committed_svgs_match_definitions(self) -> None:
        for name, builder in FIGURES.items():
            committed = (ROOT / "content" / "part-00" / "figures" / name).read_text(encoding="utf-8")
            self.assertEqual(committed, builder().svg(), name)


if __name__ == "__main__":
    unittest.main()
