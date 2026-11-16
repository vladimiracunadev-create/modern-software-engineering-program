"""Cada parte desarrollada debe enlazar sus 12 clases desde su README."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\]\(\.\./\.\./classes/part-\d{2}-[^/)]+/se-(\d{3})-[^/)]+/(?:README\.md)?\)")


class PartReadmeLinks(unittest.TestCase):
    def test_every_class_is_linked_and_exists(self) -> None:
        for readme in sorted((ROOT / "content").glob("part-*/README.md")):
            part = readme.parent.name
            classes = sorted(p.stem for p in readme.parent.glob("SE-*.md"))
            if not classes:
                continue
            text = readme.read_text(encoding="utf-8")
            linked = {int(m.group(1)) for m in LINK.finditer(text)}
            missing = [c for c in classes if int(c[3:]) not in linked]
            self.assertFalse(missing, f"{part}: clases sin enlace en el README: {missing}")
            for m in LINK.finditer(text):
                target = (readme.parent / m.group(0)[2:-1]).resolve()
                self.assertTrue(target.exists(), f"{part}: enlace roto {target}")


if __name__ == "__main__":
    unittest.main()
