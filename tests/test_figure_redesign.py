"""Ratchet against figures that redraw a Markdown table, and fit checks for the chart kit.

Rule (docs/PEDAGOGICAL-STANDARD.md, "Figuras"): a figure must add something the table does not
(pattern, comparison, distribution, relation, sequence, mechanism), never repeat rows and columns.
``scripts/figure_tab_baseline.json`` holds the ceiling per part; sessions that redesign a part lower it.
"""
from __future__ import annotations

import re
import sys
import unittest
from xml.etree import ElementTree

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import figure_tab_baseline as fb  # noqa: E402
from figure_kit import Fig, fmt_es, fmt_exact, grouped_bars, log_ticks, nice_ticks  # noqa: E402
from figure_kit_gallery import GALLERY  # noqa: E402

MEASURED = fb.measure()
BASE = fb.load()


class TableRatchetTests(unittest.TestCase):
    def _ratchet(self, metric: str) -> None:
        current, ceiling = MEASURED["counts"][metric], BASE[metric]
        for part, count in sorted(current.items()):
            self.assertLessEqual(
                count, ceiling.get(part, 0),
                f"{metric}: la parte {part} sube a {count} (tope {ceiling.get(part, 0)}). Una figura debe aportar algo "
                "que la tabla no da; usa una primitiva de scripts/figure_kit.py (docs/FIGURE-REDESIGN-GUIDE.md).")
        for part, cap in sorted(ceiling.items()):
            self.assertLessEqual(
                current.get(part, 0), cap,
                f"{metric}: la parte {part} bajó a {current.get(part, 0)}; baja el tope con "
                "`python scripts/figure_tab_baseline.py --write` y confírmalo en el mismo commit.")

    def test_tab_figures_do_not_increase(self) -> None:
        self._ratchet("tables")

    def test_table_alt_texts_do_not_increase(self) -> None:
        self._ratchet("table_alts")

    def test_diagrams_built_from_tables_do_not_increase(self) -> None:
        self._ratchet("embedded_tables")

    def test_chart_figures_never_describe_themselves_as_tables(self) -> None:
        kinds = MEASURED["kinds"]
        for part, name, alt in MEASURED["alts"]:
            if kinds.get(name) == "chart":
                self.assertFalse(alt.strip().lower().startswith("tabla"), f"{name}: el alt de un gráfico no puede empezar por «Tabla»")
        from build_figures import collect

        for path, builder in collect().items():
            fig = builder()
            if fig.kind == "chart":
                self.assertNotRegex(fig.desc, r"^\s*Tabla\b", f"{path.name}: la descripción de un gráfico no empieza por «Tabla»")

    def test_allowed_tables_are_explicit_and_justified(self) -> None:
        allowed = BASE.get("allowed_tables", {})
        for name, why in allowed.items():
            self.assertEqual(MEASURED["kinds"].get(name), "table", f"{name} no es una figura tab() existente")
            self.assertGreaterEqual(len(why.strip()), 60, f"{name}: la excepción necesita una justificación de verdad")


class ChartKitTests(unittest.TestCase):
    def test_every_gallery_chart_is_valid_accessible_svg(self) -> None:
        for name, builder in GALLERY.items():
            fig = builder()
            svg = fig.svg()
            ElementTree.fromstring(svg)  # well-formed XML
            self.assertEqual(fig.kind, "chart", name)
            self.assertEqual(svg, builder().svg(), f"{name} is not deterministic")
            self.assertIn('role="img"', svg)
            self.assertRegex(svg, r"<desc id=\"d\">[^<]{40,}</desc>")
            sizes = [int(v) for v in re.findall(r'font-size="(\d+)"', svg)]
            self.assertGreaterEqual(min(sizes), 12, name)
            for x, y in re.findall(r'<text x="(-?[\d.]+)" y="(-?[\d.]+)"', svg):
                if "rotate" in svg.split(f'x="{x}" y="{y}"')[1][:200]:
                    continue
                self.assertGreaterEqual(float(x), 0, name)
                self.assertTrue(0 <= float(y) <= fig.height, f"{name}: text outside the canvas")

    def test_value_formatting_follows_spanish_conventions(self) -> None:
        self.assertEqual(fmt_es(1515.0, 1), "1 515,0")
        self.assertEqual(fmt_es(0.025), "0,025")
        self.assertEqual(fmt_exact(14.19), "14,19")
        self.assertEqual(fmt_exact(1000), "1 000")
        self.assertEqual(fmt_es(-3.5, 1), "−3,5")

    def test_ticks_cover_the_range(self) -> None:
        ticks = nice_ticks(0, 166)
        self.assertEqual((ticks[0], ticks[-1]), (0, 200))
        self.assertEqual(log_ticks(0.02, 166), [0.01, 0.1, 1.0, 10.0, 100.0, 1000.0])

    def test_overflowing_labels_fail_instead_of_being_clipped(self) -> None:
        with self.assertRaises(ValueError):
            grouped_bars("t" * 12, "d" * 50, ["una categoría con un nombre larguísimo que no cabe en su columna estrecha"] * 8,
                         [("a", [1] * 8, "teal")], unit="u", width=500)

    def test_log_axis_rejects_non_positive_values(self) -> None:
        with self.assertRaises(ValueError):
            grouped_bars("título del gráfico", "d" * 50, ["a"], [("s", [0.0], "teal")], unit="u", log=True)

    def test_plain_figures_keep_their_kind(self) -> None:
        self.assertEqual(Fig(10, 10, "t", "d").kind, "diagram")


if __name__ == "__main__":
    unittest.main()
