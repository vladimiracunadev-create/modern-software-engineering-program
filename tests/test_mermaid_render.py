"""Mermaid diagrams are published as static SVG drawn by scripts/mermaid_render.py.

The Mermaid blocks of content/ stay as the editable source; classes/, roles/ and the
portal must contain the rendered figure and never the code. See docs/ADDING-A-PART.md.
"""
from __future__ import annotations

import re
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import mermaid_render as mr  # noqa: E402

FIGURES = ROOT / "site" / "assets" / "figures"
SOURCES = sorted((ROOT / "content").rglob("*.md"))


def source_blocks() -> list[tuple[Path, str]]:
    return [(path, block) for path in SOURCES for block in mr.mermaid_blocks(path.read_text(encoding="utf-8"))]


def published_files() -> list[Path]:
    files = [p for p in (ROOT / "classes").rglob("*.md")] + list((ROOT / "roles").glob("*.md"))
    return files + list((ROOT / "site").rglob("*.html"))


class RenderEverySource(unittest.TestCase):
    def test_every_source_block_parses_renders_and_fits(self) -> None:
        blocks = source_blocks()
        self.assertGreaterEqual(len(blocks), 670)
        for path, block in blocks:
            with self.subTest(source=path.relative_to(ROOT).as_posix(), first=block.strip().splitlines()[0]):
                rendered = mr.render(block)  # raises MermaidError on unsupported syntax or overflowing text
                self.assertEqual(mr.fit_problems(rendered), [])
                self.assertLessEqual(rendered.width, mr.MAX_W + 2)
                self.assertTrue(rendered.svg.startswith("<svg "))

    def test_rendering_is_deterministic(self) -> None:
        sample = source_blocks()[::7]
        first = [mr.render(block).svg for _, block in sample]
        mr._render_cached.cache_clear()
        second = [mr.render(block).svg for _, block in sample]
        self.assertEqual(first, second)

    def test_names_are_stable_and_derived_from_the_source(self) -> None:
        block = source_blocks()[0][1]
        self.assertEqual(mr.figure_name(block), mr.figure_name(block + "\n"))
        self.assertNotEqual(mr.figure_name(block), mr.figure_name(block + "\n    X --> Y"))
        self.assertRegex(mr.figure_name(block), r"^mermaid-[0-9a-f]{10}\.svg$")

    def test_unsupported_syntax_fails_loudly(self) -> None:
        for source in ("gantt\n title x", "flowchart LR\n A --> B\n subgraph S\n B --> C",
                       "flowchart LR\n A ~~> B", "sequenceDiagram\n loop x\n A->>B: hi\n end",
                       "stateDiagram-v2\n state X {\n }"):
            with self.subTest(source=source), self.assertRaises(mr.MermaidError):
                mr.render(source)


class LayoutReadability(unittest.TestCase):
    CHAIN = "flowchart LR\n" + "\n".join(f"    N{i}[Paso número {i} del recorrido] --> N{i + 1}[Paso número {i + 1}]" for i in range(0, 12, 2))

    def test_a_long_chain_folds_into_rows_within_the_reading_width(self) -> None:
        rendered = mr.render(self.CHAIN)
        self.assertLessEqual(rendered.width, mr.MAX_W)
        self.assertGreater(rendered.height, 150, "a 12-node chain must wrap into several rows")

    def test_text_is_never_smaller_than_13px(self) -> None:
        for _, block in source_blocks()[::25]:
            sizes = {float(m) for m in re.findall(r'font-size="([\d.]+)"', mr.render(block).svg)}
            self.assertTrue(sizes and min(sizes) >= 13, sizes)

    def test_return_edge_is_dashed_coral_and_keeps_its_label(self) -> None:
        svg = mr.render("flowchart LR\n A[Uno] --> B[Dos]\n B --> C[Tres]\n C -->|hallazgo| A").svg
        self.assertIn('stroke="#c0432f"', svg)
        self.assertIn("stroke-dasharray", svg)
        self.assertIn("hallazgo", svg)

    def test_alt_text_has_no_brackets_and_describes_the_path(self) -> None:
        rendered = mr.render("flowchart LR\n A[Uno] --> B{¿Dos?}\n B -->|sí| C[Tres]")
        self.assertNotRegex(rendered.alt, r"[\[\]]")
        self.assertIn("«Uno»", rendered.alt)
        self.assertIn("«Tres»", rendered.alt)

    def test_state_and_sequence_diagrams_keep_all_their_information(self) -> None:
        state = mr.render("stateDiagram-v2\n [*] --> A\n A --> B: evento\n B --> [*]")
        for token in ("A", "B", "evento"):
            self.assertIn(token, state.svg)
        seq = mr.render("sequenceDiagram\n participant X as Cliente\n X->>Y: pide\n Y-->>X: responde\n Note over X,Y: nota")
        for token in ("Cliente", "pide", "responde", "nota"):
            self.assertIn(token, seq.svg)


class PublishRules(unittest.TestCase):
    def test_publish_replaces_blocks_by_images_and_adds_reading_text_only_when_missing(self) -> None:
        figure = "```mermaid\nflowchart LR\n A[Uno] --> B[Dos]\n```\n"
        with_prose = mr.publish_markdown(f"# T\n\n{figure}\nEl diagrama se lee de izquierda a derecha.\n", ROOT / "roles")
        self.assertNotIn("```mermaid", with_prose)
        self.assertRegex(with_prose, r"!\[[^\]]+\]\(\.\./site/assets/figures/mermaid-[0-9a-f]{10}\.svg\)")
        self.assertNotIn("Cómo leer el diagrama", with_prose)
        without = mr.publish_markdown(f"# T\n\n{figure}\n## Siguiente\n", ROOT / "roles")
        self.assertIn("**Cómo leer el diagrama:**", without)


class PublishedOutput(unittest.TestCase):
    def test_no_mermaid_code_is_published(self) -> None:
        offenders = []
        for path in published_files():
            text = path.read_text(encoding="utf-8")
            if "```mermaid" in text or "mermaid-source" in text or 'class="mermaid"' in text:
                offenders.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(offenders[:10], [])

    def test_every_published_diagram_exists_and_none_is_orphaned(self) -> None:
        referenced: set[str] = set()
        for path in published_files():
            for name in re.findall(r"figures/(mermaid-[0-9a-f]{10}\.svg)", path.read_text(encoding="utf-8")):
                referenced.add(name)
                self.assertTrue((FIGURES / name).is_file(), f"{path.name}: missing {name}")
        on_disk = {p.name for p in FIGURES.glob("mermaid-*.svg")}
        self.assertEqual(sorted(on_disk - referenced)[:5], [], "orphan diagrams: rebuild and delete stale files")
        self.assertGreaterEqual(len(on_disk), 600)

    def test_images_in_markdown_carry_alt_text_without_brackets(self) -> None:
        pattern = re.compile(r"!\[([^\]]*)\]\([^)]*figures/mermaid-[0-9a-f]{10}\.svg\)")
        count = 0
        for path in [p for p in published_files() if p.suffix == ".md"]:
            for alt in pattern.findall(path.read_text(encoding="utf-8")):
                count += 1
                self.assertGreater(len(alt), 20, path.name)
        self.assertGreaterEqual(count, 700)

    def test_published_svgs_stay_inside_their_viewbox(self) -> None:
        ns = "{http://www.w3.org/2000/svg}"
        for path in sorted(FIGURES.glob("mermaid-*.svg")):
            root = ET.fromstring(path.read_text(encoding="utf-8"))
            _, _, w, h = (float(v) for v in root.attrib["viewBox"].split())
            self.assertLessEqual(w, mr.MAX_W + 2, path.name)
            self.assertIsNotNone(root.find(f"{ns}title"), path.name)
            self.assertIsNotNone(root.find(f"{ns}desc"), path.name)
            for el in root.iter():
                tag = el.tag.removeprefix(ns)
                xs: list[float] = []
                ys: list[float] = []
                a = el.attrib
                if tag == "rect" and "x" in a:
                    xs += [float(a["x"]), float(a["x"]) + float(a["width"])]
                    ys += [float(a["y"]), float(a["y"]) + float(a["height"])]
                elif tag == "text":
                    xs.append(float(a["x"]))
                    ys.append(float(a["y"]))
                elif tag in {"circle", "ellipse"}:
                    xs.append(float(a["cx"]))
                    ys.append(float(a["cy"]))
                elif tag == "polygon":
                    pts = [tuple(float(v) for v in p.split(",")) for p in a["points"].split()]
                    xs += [p[0] for p in pts]
                    ys += [p[1] for p in pts]
                for x in xs:
                    self.assertTrue(-0.5 <= x <= w + 0.5, f"{path.name}: x={x} outside 0..{w}")
                for y in ys:
                    self.assertTrue(-0.5 <= y <= h + 0.5, f"{path.name}: y={y} outside 0..{h}")


if __name__ == "__main__":
    unittest.main()
