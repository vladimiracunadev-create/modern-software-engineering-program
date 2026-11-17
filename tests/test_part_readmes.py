"""Esquema único del README de parte y navegación de clase en las clases desarrolladas.

Cada parte desarrollada explica sus 12 clases en «Guía razonada clase por clase»
(sin enlaces sueltos) y, después, reúne todos los enlaces en la tabla de
«Resumen operativo del recorrido».
"""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import program_state as ps  # noqa: E402

DEVELOPED_CLASSES = ps.developed_class_count()
GUIDE = "## Guía razonada clase por clase"
SUMMARY = "## Resumen operativo del recorrido"
CLASS_LINK = re.compile(r"\]\((\.\./\.\./classes/part-\d{2}-[^/)]+/se-(\d{3})-[^/)]+/(?:README\.md)?)\)")
NAV_MARKER = "[↑ Parte"


def part_readmes() -> list[Path]:
    return sorted((ROOT / "content").glob("part-*/README.md"))


class PartReadmeScheme(unittest.TestCase):
    def test_there_is_a_readme_per_developed_part_with_12_classes(self) -> None:
        readmes = part_readmes()
        self.assertEqual(len(readmes), len(ps.developed_parts()))
        for readme in readmes:
            self.assertEqual(len(list(readme.parent.glob("SE-*.md"))), 12, readme)

    def test_summary_table_follows_the_guide_and_links_the_12_classes(self) -> None:
        for readme in part_readmes():
            part = readme.parent.name
            lines = readme.read_text(encoding="utf-8").split("\n")
            self.assertEqual(lines.count(GUIDE), 1, f"{part}: falta la guía razonada")
            self.assertEqual(lines.count(SUMMARY), 1, f"{part}: falta el resumen operativo")
            guide_at, summary_at = lines.index(GUIDE), lines.index(SUMMARY)
            self.assertLess(guide_at, summary_at, f"{part}: el resumen debe ir después de la guía")
            end = next((i for i in range(summary_at + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
            rows = [line for line in lines[summary_at:end] if line.startswith("| [SE-")]
            self.assertEqual(len(rows), 12, f"{part}: la tabla debe tener 12 filas")
            expected = sorted(p.stem for p in readme.parent.glob("SE-*.md"))
            seen = []
            for row in rows:
                cells = [cell.strip() for cell in row.strip("|").split("|")]
                self.assertGreaterEqual(len(cells), 2, f"{part}: fila incompleta {row[:60]}")
                self.assertTrue(all(cells), f"{part}: celda vacía en {row[:60]}")
                link = CLASS_LINK.search(cells[0])
                self.assertIsNotNone(link, f"{part}: la primera celda debe enlazar la clase: {row[:60]}")
                target = (readme.parent / link.group(1)).resolve()
                self.assertTrue(target.exists(), f"{part}: enlace roto {target}")
                seen.append(f"SE-{link.group(2)}")
            self.assertEqual(seen, expected, f"{part}: filas distintas de las clases de la parte")

    def test_no_loose_class_links_inside_the_guide(self) -> None:
        for readme in part_readmes():
            lines = readme.read_text(encoding="utf-8").split("\n")
            guide_at = lines.index(GUIDE)
            end = next(i for i in range(guide_at + 1, len(lines)) if lines[i].startswith("## "))
            guide = "\n".join(lines[guide_at:end])
            self.assertNotIn("Abrir la clase", guide, f"{readme.parent.name}: enlace suelto en la guía")
            self.assertIsNone(CLASS_LINK.search(guide), f"{readme.parent.name}: enlace a clase dentro de la guía")


class ClassNavigation(unittest.TestCase):
    def test_all_developed_classes_have_navigation_above_and_below(self) -> None:
        pages = sorted((ROOT / "classes").glob("part-*/se-*/README.md"))
        self.assertEqual(len(pages), DEVELOPED_CLASSES)
        numbers = [int(re.search(r"se-(\d{3})", page.parent.name).group(1)) for page in pages]
        for index, page in enumerate(pages):
            # anterior y siguiente son los de las clases desarrolladas, que no son contiguas cuando
            # una parte se publica antes que las anteriores (por ejemplo, la 48 antes que la 45 a la 47)
            lines = page.read_text(encoding="utf-8").rstrip("\n").split("\n")
            nav_top = [line for line in lines[:8] if NAV_MARKER in line]
            nav_bottom = [line for line in lines[-8:] if NAV_MARKER in line]
            self.assertEqual(len(nav_top), 1, f"{page}: falta la navegación superior")
            self.assertEqual(len(nav_bottom), 1, f"{page}: falta la navegación inferior")
            for nav in (nav_top[0], nav_bottom[0]):
                if index == 0:
                    self.assertTrue(nav.startswith("← Inicio del programa"), f"{page}: SE-001 no tiene anterior")
                else:
                    self.assertTrue(re.match(rf"\[← SE-{numbers[index - 1]:03d}[ \]]", nav), f"{page}: anterior incorrecto")
                if index == DEVELOPED_CLASSES - 1:
                    self.assertTrue(nav.endswith("Fin del programa →"), f"{page}: la última clase desarrollada no tiene siguiente")
                else:
                    self.assertRegex(nav, rf"\[SE-{numbers[index + 1]:03d}[ \]]", f"{page}: siguiente incorrecto")

    def test_portal_pages_have_navigation_above_and_below(self) -> None:
        pages = sorted((ROOT / "site" / "classes").glob("SE-*.html"))
        self.assertEqual(len(pages), DEVELOPED_CLASSES)
        numbers = [int(re.search(r"SE-(\d{3})", page.name).group(1)) for page in pages]
        for index, page in enumerate(pages):
            html = page.read_text(encoding="utf-8")
            navs = re.findall(r'<nav class="class-nav".*?</nav>', html, re.S)
            self.assertEqual(len(navs), 2, f"{page}: debe tener navegación arriba y abajo")
            self.assertTrue(html.index(navs[0]) < html.index("lesson-shell") < html.rindex(navs[1]), page)
            for nav in navs:
                if index == 0:
                    self.assertIn("<span>Inicio</span>", nav)
                else:
                    self.assertIn(f'href="SE-{numbers[index - 1]:03d}.html"', nav)
                if index == DEVELOPED_CLASSES - 1:
                    self.assertIn("<span>Fin</span>", nav)
                else:
                    self.assertIn(f'href="SE-{numbers[index + 1]:03d}.html"', nav)


if __name__ == "__main__":
    unittest.main()
