"""Pruebas de la superficie «Glosario»: inventario, normalización, entradas y coherencia con los conteos."""
from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_glossary as bg  # noqa: E402
import glossary_compose as gc  # noqa: E402
import glossary_data as data  # noqa: E402
import validate_glossary  # noqa: E402


class Normalization(unittest.TestCase):
    def test_singular_plural_and_accents_share_a_key(self) -> None:
        self.assertEqual(data.key_of("Restricciones"), data.key_of("restricción"))
        self.assertEqual(data.key_of("Cohesión"), data.key_of("cohesion"))
        self.assertEqual(data.key_of("Pruebas de contrato"), data.key_of("prueba de contrato"))

    def test_parenthesis_becomes_alias(self) -> None:
        self.assertEqual(data.variants_of("reversión (rollback)"), ("reversión", ["rollback"]))
        self.assertEqual(data.variants_of("calidad de servicio (QoS)"), ("calidad de servicio", ["QoS"]))
        base, aliases = data.variants_of("decisión reversible (de dos sentidos)")
        self.assertEqual(base, "decisión reversible (de dos sentidos)")
        self.assertEqual(aliases, [])

    def test_topics_that_are_questions_or_sentences_are_not_terms(self) -> None:
        self.assertFalse(data.term_like("¿Qué es una clase?"))
        self.assertFalse(data.term_like("Cómo leer un diagrama"))
        self.assertFalse(data.term_like("Diseño, pruebas y operación"))
        self.assertTrue(data.term_like("Acoplamiento"))
        self.assertTrue(data.term_like("Condición de carrera"))

    def test_slugs_are_ascii_and_unique(self) -> None:
        slugs = [concept.slug for concept in data.inventory().values()]
        self.assertEqual(len(slugs), len(set(slugs)))
        self.assertTrue(all(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) for slug in slugs))


class Inventory(unittest.TestCase):
    def test_every_defined_term_has_a_concept(self) -> None:
        keys = {key for concept in data.inventory().values() for key in concept.keys}
        for cls in data.classes().values():
            for term, _ in cls.definitions:
                base, _ = data.variants_of(term)
                self.assertIn(data.key_of(base), keys, f"{cls.id}: {term}")

    def test_every_role_has_a_concept(self) -> None:
        roles = [path for path in (ROOT / "roles").glob("*.md") if path.name != "README.md"]
        concepts = [concept for concept in data.inventory().values() if concept.role]
        self.assertEqual(len(roles), len(concepts))

    def test_tiers_partition_the_inventory(self) -> None:
        summary = bg.summary()
        self.assertEqual(summary["total"], summary["troncal"] + summary["apoyo"])
        self.assertGreaterEqual(summary["troncal"], 100)

    def test_every_concept_lives_in_a_real_class(self) -> None:
        known = set(data.classes())
        for concept in data.inventory().values():
            self.assertTrue(concept.classes, concept.name)
            self.assertTrue(set(concept.classes) <= known, concept.name)


class Publication(unittest.TestCase):
    def test_entries_match_the_inventory(self) -> None:
        on_disk = {path.stem for path in (ROOT / "glosario/entradas").rglob("*.md")}
        self.assertEqual({concept.slug for concept in data.inventory().values()}, on_disk)

    def test_validator_passes(self) -> None:
        self.assertEqual(validate_glossary.main(), 0)

    def test_readme_counts_are_the_real_ones(self) -> None:
        total = len(data.inventory())
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        match = re.search(r"glosario profundo\*\* con\s+([\d.]+) conceptos", readme)
        self.assertIsNotNone(match)
        self.assertEqual(int(match.group(1).replace(".", "")), total)
        self.assertIn("<!-- state:glossary -->", readme)
        block = readme.split("<!-- state:glossary -->")[1].split("<!-- /state:glossary -->")[0]
        self.assertNotIn("|", block, "el bloque del glosario no debe ir dentro de una tabla")

    def test_glossary_does_not_change_program_counters(self) -> None:
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        self.assertEqual((catalog["classes"], catalog["parts"]), (612, 51))

    def test_cases_mapping_points_to_real_cases(self) -> None:
        from cases_data import CASES

        slugs = {case["slug"] for case in CASES}
        mapping = json.loads((ROOT / "glosario/casos.json").read_text(encoding="utf-8"))
        for hits in mapping.values():
            for _, slug, _ in hits:
                self.assertIn(slug, slugs)


class Composition(unittest.TestCase):
    def test_curated_sections_override_composed_ones(self) -> None:
        concept = next(iter(data.inventory().values()))
        entry = gc.compose(concept, {concept.slug: {"Definición": "Texto propio."}}, [])
        self.assertEqual(entry.sections["Definición"], "Texto propio.")
        self.assertIn("Definición", entry.curated)
        self.assertFalse(entry.developed)

    def test_clip_cuts_on_sentence_boundaries(self) -> None:
        text = "Primera frase con varias palabras. Segunda frase con otras palabras. Tercera frase final."
        self.assertEqual(gc.clip(text, 8), "Primera frase con varias palabras.")


if __name__ == "__main__":
    unittest.main()


class CuratedQuality(unittest.TestCase):
    """Calidad mínima de las entradas escritas a mano (glosario/curado/)."""

    def test_curated_entries_are_complete_and_long_enough(self) -> None:
        by_slug = {concept.slug: concept for concept in data.inventory().values()}
        for slug, sections in gc.load_curated().items():
            self.assertIn(slug, by_slug, slug)
            self.assertEqual([], [n for n in gc.DEVELOPED_SECTIONS if n not in sections], slug)
            total = sum(validate_glossary.words(sections[n]) for n in gc.DEVELOPED_SECTIONS)
            low, high = validate_glossary.WORDS_TRONCAL if data.tier_of(by_slug[slug]) == "troncal" else validate_glossary.WORDS_APOYO
            self.assertTrue(low <= total <= high, f"{slug}: {total} words")

    def test_published_curated_entries_link_classes_without_bare_references(self) -> None:
        import cross_references

        for slug in gc.load_curated():
            path = next((ROOT / "glosario/entradas").rglob(f"{slug}.md"))
            text = path.read_text(encoding="utf-8")
            self.assertEqual([], cross_references.audit_markdown(text), slug)
            self.assertRegex(text, r"\]\((?:\.\./)+classes/part-\d\d-[^)]*\)", slug)
