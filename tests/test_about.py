"""El About publicado debe decir lo mismo que el repositorio: cifras reales y sin repeticiones."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GITHUB_LIMIT = 350


def _description() -> str:
    metadata = json.loads((ROOT / ".github" / "repository-metadata.json").read_text(encoding="utf-8"))
    return metadata["description"]


def _real_counts() -> dict[str, int]:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    roles = [path for path in (ROOT / "roles").glob("*.md") if path.name != "README.md"]
    cases = [
        path
        for kind in ("exito", "fallo")
        for path in (ROOT / "casos" / kind).glob("*.md")
        if path.name != "README.md"
    ]
    return {
        "clases": catalog["classes"],
        "partes": catalog["parts"],
        "roles": len(roles),
        "casos": len(cases),
    }


class AboutTest(unittest.TestCase):
    def test_within_github_limit(self) -> None:
        self.assertLessEqual(len(_description()), GITHUB_LIMIT)

    def test_figures_match_repository(self) -> None:
        text = _description()
        counts = _real_counts()
        self.assertIn(f"{counts['clases']} clases desarrolladas en {counts['partes']} partes", text)
        self.assertIn(f"{counts['roles']} rutas por rol", text)
        self.assertIn(f"{counts['casos']} casos de estudio", text)

    def test_names_the_parts_still_in_preparation(self) -> None:
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        pending = len(catalog["unpublished_parts"])
        text = _description()
        if pending:
            words = {1: "una parte", 2: "dos partes", 3: "tres partes"}
            self.assertIn(f"y {words[pending]} en preparación", text)
        else:
            self.assertNotIn("en preparación", text)

    def test_no_stale_or_repeated_figures(self) -> None:
        text = _description()
        self.assertNotIn("planificad", text)
        self.assertNotIn("Programa de Ingeniería de Software Moderna", text)
        self.assertEqual(len(re.findall(r"\b\d+ clases\b", text)), 1)

    def test_publication_plan_quotes_the_same_text(self) -> None:
        plan = (ROOT / "docs" / "PUBLICATION-PLAN.md").read_text(encoding="utf-8")
        self.assertIn(_description(), plan)


if __name__ == "__main__":
    unittest.main()
