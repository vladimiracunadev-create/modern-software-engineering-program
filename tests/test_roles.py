from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_GUIDES = {
    "accessibility-engineer.md",
    "ai-augmented-software-engineer.md",
    "ai-systems-engineer.md",
    "api-engineer.md",
    "backend-engineer.md",
    "build-release-engineer.md",
    "cloud-engineer.md",
    "compliance-engineer.md",
    "cto.md",
    "data-engineer.md",
    "database-reliability-engineer.md",
    "desktop-engineer.md",
    "developer-experience-engineer.md",
    "devops-engineer.md",
    "distributed-systems-engineer.md",
    "embedded-iot-engineer.md",
    "engineering-manager.md",
    "finops-engineer.md",
    "frontend-engineer.md",
    "full-stack-engineer.md",
    "green-software-engineer.md",
    "internationalization-engineer.md",
    "legacy-modernization-engineer.md",
    "mobile-engineer.md",
    "observability-engineer.md",
    "open-source-innersource-engineer.md",
    "performance-engineer.md",
    "platform-engineer.md",
    "qa-test-engineer.md",
    "requirements-engineer.md",
    "safety-critical-software-engineer.md",
    "security-engineer.md",
    "site-reliability-engineer.md",
    "software-architect.md",
    "software-engineer.md",
    "solutions-architect.md",
    "systems-programmer.md",
    "technical-leadership.md",
    "technical-product-engineer.md",
    "technical-writer.md",
}


class RoleGuideTests(unittest.TestCase):
    def test_inventory_is_explicit_and_complete(self) -> None:
        actual = {
            path.name
            for path in (ROOT / "roles").glob("*.md")
            if path.name != "README.md"
        }
        self.assertEqual(EXPECTED_GUIDES, actual)

    def test_every_guide_is_linked_from_both_entry_points(self) -> None:
        main = (ROOT / "README.md").read_text(encoding="utf-8")
        index = (ROOT / "roles" / "README.md").read_text(encoding="utf-8")
        for name in EXPECTED_GUIDES:
            with self.subTest(role=name):
                self.assertIn(f"roles/{name}", main)
                self.assertIn(f"]({name})", index)

    def test_every_guide_has_the_professional_contract(self) -> None:
        sections = (
            "## 🧭 Qué es y por qué importa",
            "## 🗓️ Un día en el puesto",
            "## ✅ Responsabilidades y límites",
            "## 🧠 Qué necesitas saber",
            "## 📚 Tu ruta en el programa",
            "## 🧪 Evidencia de portafolio",
            "## 📈 Progresión",
            "## ⚠️ Mitos frecuentes",
            "## 🚀 Siguientes pasos",
        )
        for name in EXPECTED_GUIDES:
            text = (ROOT / "roles" / name).read_text(encoding="utf-8")
            with self.subTest(role=name):
                self.assertGreaterEqual(len(text.split()), 300)
                self.assertIn("../classes/", text)
                for section in sections:
                    self.assertIn(section, text)


if __name__ == "__main__":
    unittest.main()
