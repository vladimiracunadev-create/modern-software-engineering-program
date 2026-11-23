"""Valida la superficie «Glosario» (ver glosario/GUIDE.md).

Comprueba, sobre los archivos publicados: una entrada por concepto del inventario (sin duplicados ni huérfanas),
el esquema completo y ordenado, que cada entrada enlace al menos una clase real y que todos los enlaces existan,
que no queden menciones ``SE-nnn`` o ``Parte NN`` sin enlazar, texto alternativo de figuras sin corchetes, que los
índices enlacen todas las entradas, que el texto curado cite un concepto real y tenga la extensión de su nivel, y que
``glosario/casos.json`` apunte a casos y conceptos que existen.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import cross_references  # noqa: E402
import glossary_compose as gc  # noqa: E402
import glossary_data as data  # noqa: E402
from cases_data import CASES  # noqa: E402

LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMAGE = re.compile(r"!\[([^\n]*?)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CLASS_LINK = re.compile(r"\]\((?:\.\./)+classes/part-\d\d-[^/]+/se-(\d{3})-[^/]+/README\.md\)")
HEADING = re.compile(r"^## (.+)$", re.M)
WORDS_TRONCAL = (330, 1100)
WORDS_APOYO = (110, 500)
MIN_SECTION_WORDS = 3


def words(text: str) -> int:
    return len(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text).split())


def check_links(path: Path, text: str, failures: list[str]) -> None:
    rel = path.relative_to(ROOT).as_posix()
    for target in LINK.findall(text) + [m[1] for m in IMAGE.findall(text)]:
        if re.match(r"^(?:[a-z][a-z0-9+.-]*:|#)", target):
            continue
        clean = unquote(target.split("#", 1)[0])
        if clean and not (path.parent / clean).resolve().exists():
            failures.append(f"{rel}: broken link -> {target}")


def main() -> int:
    failures: list[str] = []
    inventory = data.inventory()
    expected = {concept.slug: concept for concept in inventory.values()}
    if len(expected) != len(inventory):
        failures.append("inventory has duplicate slugs")
    names = [data.key_of(concept.name) for concept in inventory.values()]
    if len(set(names)) != len(names):
        failures.append("inventory has duplicate concept names")
    entries_dir = ROOT / "glosario" / "entradas"
    found = {path.stem: path for path in entries_dir.rglob("*.md")} if entries_dir.is_dir() else {}
    for slug in sorted(set(expected) - set(found)):
        failures.append(f"missing entry for concept: {slug}")
    for slug in sorted(set(found) - set(expected)):
        failures.append(f"entry without concept in the inventory: {slug}")
    curated = gc.load_curated()
    for slug, sections in curated.items():
        if slug not in expected:
            failures.append(f"glosario/curado/{slug}.md does not match any concept")
            continue
        unknown = [name for name in sections if name not in gc.SECTIONS]
        if unknown:
            failures.append(f"glosario/curado/{slug}.md has unknown sections: {unknown}")
        if all(name in sections for name in gc.DEVELOPED_SECTIONS):
            low, high = WORDS_TRONCAL if data.tier_of(expected[slug]) == "troncal" else WORDS_APOYO
            total = sum(words(sections[name]) for name in gc.DEVELOPED_SECTIONS)
            if not low <= total <= high:
                failures.append(f"glosario/curado/{slug}.md: {total} words, expected {low}-{high} for its level")
    for slug, path in sorted(found.items()):
        concept = expected.get(slug)
        if concept is None:
            continue
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        if rel != gc.entry_path(concept):
            failures.append(f"{rel}: expected path {gc.entry_path(concept)}")
        headings = HEADING.findall(text)
        if headings != gc.SECTIONS:
            failures.append(f"{rel}: sections {headings} differ from the schema")
        if not text.startswith(f"# {concept.name}\n"):
            failures.append(f"{rel}: first heading must be '# {concept.name}'")
        for name in gc.SECTIONS:
            body = re.search(rf"^## {re.escape(name)}\n\n(.*?)(?=^## |^---\n)", text, re.M | re.S)
            if not body or words(body.group(1)) < MIN_SECTION_WORDS:
                failures.append(f"{rel}: section '{name}' is empty")
        class_ids = {f"SE-{n}" for n in CLASS_LINK.findall(text)}
        known = cross_references.load_index().lessons
        if not class_ids:
            failures.append(f"{rel}: links no class")
        elif not class_ids <= set(known) and not concept.role:
            failures.append(f"{rel}: links unknown classes {sorted(class_ids - set(known))}")
        check_links(path, text, failures)
        for finding in cross_references.audit_markdown(text):
            failures.append(f"{rel}: bare reference {finding.kind} at line {finding.line}")
        for alt, _ in IMAGE.findall(text):
            if "[" in alt or "]" in alt:
                failures.append(f"{rel}: figure alt text contains brackets")
    # índices: todas las entradas enlazadas desde el índice alfabético y desde el de familias
    letters_text = "".join(path.read_text(encoding="utf-8") for path in (ROOT / "glosario/indice").glob("*.md")) if (ROOT / "glosario/indice").is_dir() else ""
    families_text = "".join(path.read_text(encoding="utf-8") for path in (ROOT / "glosario/familias").glob("*.md")) if (ROOT / "glosario/familias").is_dir() else ""
    for slug, concept in expected.items():
        target = f"entradas/{data.letter_of(slug)}/{slug}.md)"
        if target not in letters_text:
            failures.append(f"alphabetical index does not link {slug}")
        if target not in families_text:
            failures.append(f"family index does not link {slug}")
    readme = ROOT / "glosario/README.md"
    inventory_md = ROOT / "glosario/INVENTARIO.md"
    for required in (readme, inventory_md, ROOT / "glosario/GUIDE.md"):
        if not required.is_file():
            failures.append(f"missing {required.relative_to(ROOT).as_posix()}")
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        check_links(readme, text, failures)
        if f"{len(expected)} conceptos" not in text:
            failures.append("glosario/README.md does not state the real concept count")
        for letter in {data.letter_of(slug) for slug in expected}:
            if f"indice/{letter}.md" not in text:
                failures.append(f"glosario/README.md lacks the link to the index {letter}")
    if inventory_md.is_file() and f"**{len(expected)} conceptos**" not in inventory_md.read_text(encoding="utf-8"):
        failures.append("glosario/INVENTARIO.md does not state the real concept count")
    # casos
    cases_file = ROOT / "glosario/casos.json"
    if cases_file.is_file():
        mapping = json.loads(cases_file.read_text(encoding="utf-8"))
        slugs = {case["slug"] for case in CASES}
        for slug, hits in mapping.items():
            if slug not in expected:
                failures.append(f"casos.json: unknown concept {slug}")
            for _, case_slug, _ in hits:
                if case_slug not in slugs:
                    failures.append(f"casos.json: unknown case {case_slug}")
    # portal
    for slug, concept in expected.items():
        if not (ROOT / "site/glosario" / data.letter_of(slug) / f"{slug}.html").is_file():
            failures.append(f"missing portal page for {slug}")
    if not (ROOT / "site/glosario/index.html").is_file():
        failures.append("missing site/glosario/index.html")
    if failures:
        for failure in failures[:80]:
            print("GLOSSARY_FAIL: " + failure, file=sys.stderr)
        print(f"GLOSSARY_FAIL: {len(failures)} problems", file=sys.stderr)
        return 1
    print(f"GLOSSARY_OK: {len(expected)} concepts, {len(found)} entries, {len(curated)} curated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
