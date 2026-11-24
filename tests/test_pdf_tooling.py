"""Pruebas de la cadena de PDF que no necesitan navegador ni los binarios (docs/PDF.md)."""
from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_pdf as bp  # noqa: E402
import publish_pdf as pp  # noqa: E402
import verify_pdf as vp  # noqa: E402


class LinkResolutionTests(unittest.TestCase):
    def test_site_and_repository_paths_map_to_the_same_anchor(self) -> None:
        self.assertEqual("c-SE-002", bp.canonical_key("classes/SE-002.html"))
        self.assertEqual(
            "c-SE-002",
            bp.canonical_key("classes/part-00-ingenieria-de-software-como-profesion/se-002-historia-de-la-crisis-del-software-a-la-ingenieria-continua/README.md"),
        )
        self.assertEqual("p-03", bp.canonical_key("parts/03.html"))
        self.assertEqual("p-03", bp.canonical_key("classes/part-03-redes-internet-y-protocolos/README.md"))
        self.assertEqual("case-exito-amazon", bp.canonical_key("casos/exito/amazon.html"))
        self.assertEqual("case-fallo-tsb", bp.canonical_key("casos/fallo/tsb.md"))
        self.assertEqual("role-api-engineer", bp.canonical_key("roles/api-engineer.md"))
        self.assertIsNone(bp.canonical_key("docs/PEDAGOGICAL-STANDARD.md"))

    def test_links_outside_the_volume_go_to_the_portal_and_inside_stay_internal(self) -> None:
        unit = bp.Unit("class", "c-SE-001", "t", base="classes/SE-001.html")
        stats = {"repo": 0, "bare_linked": 0, "bare_portal": 0, "internal": 0, "portal": 0, "external": 0, "unwrapped": 0}
        body = '<a href="SE-002.html">a</a> <a href="SE-300.html">b</a> <a href="https://example.org/x">c</a> <a href="../index.html">d</a>'
        out = bp.rewrite_links(body, unit, {"c-SE-001", "c-SE-002"}, set(), stats)
        self.assertIn('href="#c-SE-002"', out)
        self.assertIn(f'href="{bp.PAGES}classes/SE-300.html"', out)
        self.assertIn('href="https://example.org/x"', out)
        self.assertNotIn("index.html", out)
        self.assertEqual({"internal": 1, "portal": 1, "external": 1, "unwrapped": 1}, {k: v for k, v in stats.items() if v})

    def test_glossary_links_outside_the_volume_go_to_the_portal(self) -> None:
        paths = bp.glossary_paths()
        self.assertTrue(paths, "el glosario publicado debe existir")
        slug, rel = next(iter(paths.items()))
        self.assertEqual(f"{bp.PAGES}glosario/{rel}", bp.portal_url(f"gl-{slug}"))
        self.assertEqual(f"gl-{slug}", bp.canonical_key(f"glosario/{rel}"))

    def test_bare_references_are_linked_outside_code_and_links(self) -> None:
        stats = {"bare_linked": 0, "bare_portal": 0}
        out = bp.link_bare_references("<p>Ver SE-002 y <code>SE-003</code>, <a href='x'>SE-004</a>, work/SE-005</p>", {"c-SE-002"}, stats)
        self.assertIn('<a href="#c-SE-002">SE-002</a>', out)
        self.assertEqual(2, out.count("<a "), out)  # el nuevo y el que ya existía
        self.assertIn("<code>SE-003</code>", out)

    def test_markdown_layout_tables_and_missing_blank_lines(self) -> None:
        title, body = bp.markdown_to_html("# T\n\nTexto\n### Sub\n- uno\n- dos\n")
        self.assertEqual("T", title)
        self.assertIn("<h3>Sub</h3>", body)
        self.assertIn("<li>uno</li>", body)


class VolumeStructureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.curriculum = bp.load_curriculum()
        cls.volumes = bp.build_volumes(cls.curriculum, None)

    def test_book_carries_every_part_class_role_and_case(self) -> None:
        book = self.volumes["libro-completo"]
        counts = bp.counts_of(book)
        self.assertEqual(self.curriculum["part_count"], counts["parts"])
        self.assertEqual(self.curriculum["class_count"], counts["classes"])
        self.assertEqual(len(list((ROOT / "roles").glob("*.md"))) - 1, counts["roles"])
        expected_cases = sum(len(bp.case_listing(kind)) for kind in ("exito", "fallo"))
        self.assertEqual(expected_cases, counts["cases"])

    def test_stage_volumes_partition_the_classes(self) -> None:
        stage_classes: list[str] = []
        for slug, vol in self.volumes.items():
            if slug.startswith("etapa-"):
                stage_classes += [u.sid for u in vol.units if u.kind == "class"]
        self.assertEqual(self.curriculum["class_count"], len(stage_classes))
        self.assertEqual(len(stage_classes), len(set(stage_classes)))

    def test_verifier_expectations_match_the_builder(self) -> None:
        for slug, vol in self.volumes.items():
            expected = vp.expected_volume(slug, self.curriculum)
            counts = bp.counts_of(vol)
            self.assertEqual(len(expected["classes"]), counts["classes"], slug)
            self.assertEqual(len(expected["cases"]), counts["cases"], slug)
            self.assertEqual(expected["roles"], counts["roles"], slug)


class PublishedRecordTests(unittest.TestCase):
    """Si hay PDF publicados, sus sumas y su tabla deben coincidir con lo registrado."""

    def test_checksums_manifest_and_docs_agree(self) -> None:
        manifest_path = ROOT / "pdf" / "manifest.json"
        if not manifest_path.exists():
            self.skipTest("todavía no se ha publicado ningún PDF")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        sums = {}
        for line in (ROOT / "pdf" / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
            digest, name = line.split("  ", 1)
            sums[name] = digest
        self.assertEqual({v["file"] for v in manifest["volumes"]}, set(sums))
        docs = (ROOT / "docs" / "PDF.md").read_text(encoding="utf-8")
        curriculum = bp.load_curriculum()
        for vol in manifest["volumes"]:
            self.assertEqual(vol["sha256"], sums[vol["file"]])
            self.assertRegex(vol["sha256"], r"^[0-9a-f]{64}$")
            self.assertIn(vol["sha256"][:16], docs, vol["file"])
            if vol["file"].endswith("libro-completo.pdf"):
                self.assertEqual(curriculum["class_count"], vol["counts"]["classes"])
                self.assertEqual(curriculum["part_count"], vol["counts"]["parts"])

    def test_readme_status_and_about_quote_the_real_state(self) -> None:
        manifest_path = ROOT / "pdf" / "manifest.json"
        if not manifest_path.exists():
            self.skipTest("todavía no se ha publicado ningún PDF")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
        curriculum = bp.load_curriculum()
        self.assertIn(manifest["tag"], readme)
        self.assertIn(manifest["tag"], status)
        for vol in manifest["volumes"]:
            self.assertIn(vol["file"], readme, vol["file"])
        book = next(v for v in manifest["volumes"] if v["file"].endswith("libro-completo.pdf"))
        self.assertEqual(curriculum["class_count"], book["counts"]["classes"])
        self.assertEqual(curriculum["part_count"], book["counts"]["parts"])
        self.assertEqual(len(list((ROOT / "roles").glob("*.md"))) - 1, book["counts"]["roles"])
        self.assertEqual(sum(len(bp.case_listing(k)) for k in ("exito", "fallo")), book["counts"]["cases"])
        self.assertEqual(len(vp.glossary_slugs()), book["counts"]["glossary_entries"])
        self.assertEqual(vp.inventory_count(), book["counts"]["glossary_entries"])

    def test_no_pdf_is_tracked_in_git(self) -> None:
        tracked = bp.git("ls-files", "*.pdf")
        self.assertEqual("", tracked, "los PDF van como activos de un Release, no en git")

    def test_release_tag_is_derived_from_the_manifest(self) -> None:
        tag = pp.release_tag({"date": "2026-11-23T10:00:00+00:00", "commit": "0123456789abcdef"})
        self.assertEqual("pdf-2026-11-23-01234567", tag)
        self.assertRegex(pp.download_url(tag, "a.pdf"), r"^https://github\.com/.+/releases/download/pdf-")


if __name__ == "__main__":
    unittest.main()
