"""Referencias cruzadas: toda mención SE-nnn / Parte NN publicada es un enlace válido.

El mecanismo vive en ``scripts/cross_references.py`` y se aplica en la publicación
(clases, partes, portal, roles, casos). Estas pruebas fallan si en una página publicada
queda una mención desnuda (fuera de código, encabezados y enlaces), una mención a una
clase o parte inexistente, un enlace relativo roto o un nombre de parte distinto del
oficial. Los documentos históricos de migración (ID-MIGRATION, ADR, CHANGELOG, tracker)
están exentos.
"""
from __future__ import annotations

import json
import posixpath
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import cross_references as cr  # noqa: E402

MARKDOWN_SURFACES = ("classes/**/*.md", "roles/*.md", "casos/**/*.md", "README.md", "STATUS.md", "FILE_INDEX.md")
HTML_EXEMPT = ("site/legacy/", "site/404.html")  # narran la migración y conservan IDs antiguos
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def surface_files(patterns: tuple[str, ...]) -> list[Path]:
    seen: dict[str, Path] = {}
    for pattern in patterns:
        for path in ROOT.glob(pattern):
            relative = path.relative_to(ROOT).as_posix()
            if not cr.is_historical(relative):
                seen[relative] = path
    return [seen[key] for key in sorted(seen)]


class ResolverBehavior(unittest.TestCase):
    def test_links_lessons_and_parts_in_prose_and_tables(self) -> None:
        text = "Ver SE-241 y la Parte 20.\n\n| A | B |\n|---|---|\n| SE-241, SE-242 | Partes 03–05 |\n"
        result = cr.resolve(text, "casos/fallo")
        self.assertIn("[SE-241](../../classes/part-20-", result)
        self.assertIn("[Parte 20](../../classes/part-20-", result)
        self.assertIn("[SE-242](", result)
        self.assertIn("Partes [03](", result)
        self.assertEqual(cr.audit_markdown(result), [])

    def test_is_idempotent(self) -> None:
        text = "La Parte 3 — Redes e internet precede a SE-241 (Parte 20)."
        once = cr.resolve(text, "roles")
        self.assertEqual(cr.resolve(once, "roles"), once)

    def test_leaves_code_headings_links_and_figures_untouched(self) -> None:
        text = (
            "## SE-241 en un encabezado\n\n"
            "`SE-241` y `Parte 20` en código.\n\n"
            "```text\nSE-241 Parte 20\n```\n\n"
            "[SE-241](https://example.org/x) ya enlazado.\n\n"
            "![Parte 20 en una figura](figures/x.svg)\n\n"
            "Ruta content/part-20/SE-241.md y SE-241.md.\n"
        )
        self.assertEqual(cr.resolve(text, "roles"), text)

    def test_multiline_link_text_is_not_split(self) -> None:
        text = "Mira [la Parte 20\ny SE-241](https://example.org) entera."
        self.assertEqual(cr.resolve(text, "roles"), text)

    def test_unknown_references_are_reported_not_linked(self) -> None:
        findings = {finding.kind for finding in cr.audit_markdown("SE-999 y Parte 77 no existen.")}
        self.assertEqual(findings, {"bare-se", "unknown-se", "unknown-parte"} & findings)
        self.assertIn("unknown-se", findings)
        self.assertIn("unknown-parte", findings)

    def test_normalizes_retired_part_names_to_the_official_title(self) -> None:
        official = cr.official_title("20") if hasattr(cr, "official_title") else cr.load_index().parts["20"].title
        for text in (
            "Parte 20 — Backend y APIs",
            "Parte 20 (Backend y APIs)",
            "[Parte 20 — Backend y APIs](../classes/part-20-backend-apis-y-procesamiento-asincrono/README.md)",
        ):
            result = cr.resolve(text, "roles")
            self.assertIn(official, result, text)
            self.assertNotIn("Backend y APIs", result.replace(official, ""), text)
        self.assertEqual(cr.audit_part_names(cr.resolve("Parte 3 — Redes e internet", "roles")), [])

    def test_lesson_label_titles_follow_the_real_title(self) -> None:
        reference = cr.load_index().lessons["SE-041"]
        link = f"[SE-041 · otro título]({cr.relative_link('casos/exito', reference.path)})"
        self.assertIn(reference.title, cr.resolve(link, "casos/exito"))

    def test_html_resolver_links_text_nodes_only(self) -> None:
        html = '<p>Ver SE-241.</p><a href="x">SE-241</a><h2>SE-241</h2><code>Parte 20</code><p class="eyebrow">Parte 20</p>'
        result = cr.resolve_html(html, "site/classes")
        self.assertIn('<a href="./SE-241.html">SE-241</a>.</p>', result)
        self.assertEqual(result.count("<a "), 2)
        self.assertEqual(cr.audit_html(result), [])


class PublishedSurfaces(unittest.TestCase):
    def test_markdown_pages_have_no_bare_or_unknown_references(self) -> None:
        failures: list[str] = []
        for path in surface_files(MARKDOWN_SURFACES):
            text = path.read_text(encoding="utf-8")
            for finding in cr.audit_markdown(text) + cr.audit_part_names(text):
                failures.append(f"{path.relative_to(ROOT).as_posix()}:{finding.line} {finding.kind} {finding.detail}")
        self.assertEqual(failures[:20], [], f"{len(failures)} referencias sin resolver")

    def test_site_pages_have_no_bare_references(self) -> None:
        failures: list[str] = []
        for path in sorted((ROOT / "site").rglob("*.html")):
            relative = path.relative_to(ROOT).as_posix()
            if relative.startswith(HTML_EXEMPT):
                continue
            for finding in cr.audit_html(path.read_text(encoding="utf-8")):
                failures.append(f"{relative} {finding.kind} {finding.detail}")
        self.assertEqual(failures[:20], [], f"{len(failures)} referencias sin resolver")

    def test_relative_links_to_classes_and_parts_exist(self) -> None:
        index = cr.load_index()
        known = {reference.path for reference in [*index.lessons.values(), *index.parts.values()]}
        broken: list[str] = []
        for path in surface_files(MARKDOWN_SURFACES):
            relative = path.relative_to(ROOT).as_posix()
            base = posixpath.dirname(relative)
            for match in LINK.finditer(path.read_text(encoding="utf-8")):
                target = match.group(1).partition("#")[0]
                if not target.startswith((".", "classes/")) or target.startswith(("http", "mailto")):
                    continue
                resolved = posixpath.normpath(posixpath.join(base, target))
                if "classes/part-" in resolved and resolved.endswith("README.md") and resolved not in known:
                    broken.append(f"{relative} -> {target}")
        self.assertEqual(broken[:20], [], f"{len(broken)} enlaces a clases o partes inexistentes")

    def test_part_h1_matches_the_official_curriculum_title(self) -> None:
        index = cr.load_index()
        mismatches = []
        for part_id, reference in index.parts.items():
            readme = ROOT / "content" / f"part-{part_id}" / "README.md"
            heading = re.match(r"# Parte 0*\d+ — (.+)", readme.read_text(encoding="utf-8").splitlines()[0])
            if not heading or heading.group(1) != reference.title:
                mismatches.append(f"{part_id}: {heading and heading.group(1)!r} != {reference.title!r}")
        self.assertEqual(mismatches, [])

    def test_class_titles_agree_across_sources_and_portal(self) -> None:
        program = json.loads((ROOT / "curriculum.yaml").read_text(encoding="utf-8"))
        problems: list[str] = []
        for part in program["parts"]:
            for lesson in part["lessons"]:
                expected = f"# {lesson['id']} — {lesson['title']}"
                readme = ROOT / lesson["path"] / "README.md"
                if readme.read_text(encoding="utf-8").splitlines()[0] != expected:
                    problems.append(f"README {lesson['id']}")
                page = (ROOT / "site/classes" / f"{lesson['id']}.html").read_text(encoding="utf-8")
                title = re.search(r"<title>(.*?)</title>", page)
                shown = f"{lesson['id']} · {lesson['title']}".replace("&", "&amp;")
                if not title or title.group(1) != shown:
                    problems.append(f"portal {lesson['id']}")
        self.assertEqual(problems[:10], [])

    def test_no_naive_link_lookalikes_in_code(self) -> None:
        """Código como ``f[x](y)`` parece un enlace Markdown a un validador ingenuo."""
        pattern = re.compile(r"\[[^\]\n]*\]\(([^)\s]*)\)")
        allowed = re.compile(r"(https?://|mailto:|#|\.{1,2}/|[\w.-]+/|[\w.-]+\.(?:md|svg|html|png|json|ya?ml|py|txt|rs|sh|ps1|toml|csv|tsv|css|js)(?:#[\w-]*)?$|LICENSE$|NOTICE$)")
        suspicious: list[str] = []
        for path in [*sorted((ROOT / "content").glob("part-*/*.md")), *sorted((ROOT / "docs").glob("*.md"))]:
            for match in pattern.finditer(path.read_text(encoding="utf-8")):
                if not allowed.match(match.group(1)):
                    suspicious.append(f"{path.relative_to(ROOT).as_posix()}: {match.group(0)[:60]}")
        self.assertEqual(suspicious[:10], [])


if __name__ == "__main__":
    unittest.main()
