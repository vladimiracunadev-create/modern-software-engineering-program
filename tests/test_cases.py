"""Structure tests for the "Casos de estudio" surface (casos/GUIDE.md)."""
from __future__ import annotations

import io
import json
import re
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_cases  # noqa: E402
import program_state as ps  # noqa: E402
import figure_tab_baseline as fb  # noqa: E402
import validate_cases  # noqa: E402
from build_figures import collect  # noqa: E402
from cases_data import CASES, KINDS, SKELETON_MARKER, case_path, cases_of  # noqa: E402

SLUGS = {
    "exito": ["netflix", "whatsapp", "uber", "mercado-libre", "amazon", "spotify", "airbnb", "stripe"],
    "fallo": ["knight-capital", "healthcare-gov", "tsb", "meta-2021", "crowdstrike", "therac-25", "gitlab-2017", "quibi"],
}


class CasesSurfaceTests(unittest.TestCase):
    def test_fixed_list_of_sixteen_cases(self) -> None:
        for kind, slugs in SLUGS.items():
            self.assertEqual(slugs, [case["slug"] for case in cases_of(kind)])
        for case in CASES:
            self.assertTrue((ROOT / case_path(case)).is_file(), case_path(case))
            self.assertTrue(case["hook"].endswith("."), case["slug"])
            self.assertRegex(case["year"], r"^\d{4}$")

    def test_validator_passes(self) -> None:
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = validate_cases.main()
        self.assertEqual(0, code, err.getvalue())

    def test_generated_files_are_current(self) -> None:
        for path, content in build_cases.expected_files().items():
            self.assertTrue(path.is_file(), path)
            self.assertEqual(content, path.read_text(encoding="utf-8"), path.relative_to(ROOT))

    def test_group_pages_index_every_case_with_year(self) -> None:
        for kind in KINDS:
            text = (ROOT / "casos" / kind / "README.md").read_text(encoding="utf-8")
            for case in cases_of(kind):
                self.assertRegex(text, rf"\]\({re.escape(case['slug'])}\.md\) — \*\*{case['year']}\*\*")
            self.assertIn(f"../figures/{kind}-mapa.svg", text)

    def test_skeletons_carry_marker_and_navigation(self) -> None:
        for case in CASES:
            text = (ROOT / case_path(case)).read_text(encoding="utf-8")
            if SKELETON_MARKER in text:
                self.assertIn("en elaboración", text)
            self.assertEqual(2, text.count(build_cases.case_nav(case)), case["slug"])

    def test_surface_does_not_change_the_counters(self) -> None:
        program = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
        self.assertEqual(ps.developed_class_count(), program["class_count"])
        self.assertEqual(len(ps.developed_parts()), program["part_count"])
        self.assertFalse(list((ROOT / "classes").glob("*caso*")))

    def test_readme_section_sits_between_parts_and_roles(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        parts = readme.index("<!-- /state:parts-table -->")
        section = readme.index("## 🏛️ Casos de estudio: la realidad frente a la teoría")
        roles = readme.index("## 🧭 Rutas sugeridas por rol")
        self.assertLess(parts, section)
        self.assertLess(section, roles)
        block = readme[readme.index("<!-- state:cases -->"):readme.index("<!-- /state:cases -->")]
        self.assertNotIn("|", block, "el bloque no debe contener tablas")
        self.assertIn("casos/exito/README.md", block)
        self.assertIn("casos/fallo/README.md", block)

    def test_portal_pages_exist_with_navigation_and_figures(self) -> None:
        for kind in KINDS:
            index = ROOT / "site/casos" / kind / "index.html"
            self.assertTrue(index.is_file())
            self.assertIn(f"figures/{kind}-mapa.svg", index.read_text(encoding="utf-8"))
            self.assertTrue((ROOT / "site/casos/figures" / f"{kind}-mapa.svg").is_file())
            for case in cases_of(kind):
                page = (ROOT / "site/casos" / kind / f"{case['slug']}.html").read_text(encoding="utf-8")
                self.assertIn('class="class-nav"', page)
                self.assertIn("Programa de Ingeniería de Software Moderna", page)


class CaseFigureTests(unittest.TestCase):
    def test_case_figures_follow_the_contract(self) -> None:
        figures = {path: builder for path, builder in collect().items() if path.parent == ROOT / "casos" / "figures"}
        self.assertGreaterEqual(len(figures), 2)
        slugs = {case["slug"] for case in CASES} | set(KINDS)
        for path, builder in figures.items():
            self.assertTrue(any(path.name.startswith(f"{slug}-") for slug in slugs), path.name)
            fig = builder()
            self.assertNotEqual("table", fig.kind, f"{path.name} repite una tabla")
            self.assertEqual(0, fig.table_calls, f"{path.name} dibuja una tabla")
            self.assertNotRegex(fig.desc, r"^\s*Tabla\b", path.name)
            self.assertTrue(path.is_file(), f"{path.name}: ejecuta python scripts/build_figures.py")
            self.assertEqual(builder().svg(), path.read_text(encoding="utf-8"), path.name)

    def test_ratchet_counts_zero_tables_in_cases(self) -> None:
        counts = fb.measure()["counts"]
        for metric in fb.METRICS:
            self.assertEqual(0, counts[metric].get("casos", 0), metric)

    def test_case_alt_texts_have_no_brackets_and_no_table_prefix(self) -> None:
        image = re.compile(r"!\[([^\n]*?)\]\(([^)\s]+)")
        for md in (ROOT / "casos").glob("*/*.md"):
            for alt, _src in image.findall(md.read_text(encoding="utf-8")):
                self.assertFalse(re.search(r"[\[\]]", alt), f"{md.name}: {alt[:40]}")
                self.assertFalse(alt.strip().lower().startswith("tabla"), f"{md.name}: {alt[:40]}")


if __name__ == "__main__":
    unittest.main()
