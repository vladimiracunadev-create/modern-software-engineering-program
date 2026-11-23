"""Enlaces de ida y vuelta entre las clases publicadas y el glosario.

``link_class`` es un paso de la publicación de una clase (``build_phase3.published_markdown``): no toca
``content/``. Enlaza a su entrada cada término en negrita de «Definiciones de trabajo» y «Glosario» y añade al
final del apartado «Glosario» los conceptos que la clase enseña, de modo que cada entrada del glosario
(que lista sus clases) tiene su correspondencia en la clase.
"""
from __future__ import annotations

import posixpath
import re
from functools import lru_cache

import cross_references
import glossary_data as data

SECTION_NAMES = ("Definiciones de trabajo", "Glosario")
BOLD_TERM = re.compile(r"\*\*(?!\[)([^*\n]+?)\*\*")


@lru_cache(maxsize=1)
def _by_key() -> dict[str, data.Concept]:
    table: dict[str, data.Concept] = {}
    for concept in data.inventory().values():
        for key in concept.keys:
            table.setdefault(key, concept)
    return table


@lru_cache(maxsize=1)
def _by_class() -> dict[str, list[data.Concept]]:
    result: dict[str, list[data.Concept]] = {}
    for concept in data.inventory().values():
        if concept.role:
            continue
        for class_id in concept.classes:
            result.setdefault(class_id, []).append(concept)
    return result


def entry_href(class_dir: str, concept: data.Concept) -> str:
    target = f"glosario/entradas/{data.letter_of(concept.slug)}/{concept.slug}.md"
    return cross_references.relative_link(class_dir, target)


def _section_bounds(markdown: str, name: str) -> tuple[int, int] | None:
    match = re.search(rf"^## {re.escape(name)}\n", markdown, re.M)
    if not match:
        return None
    start = match.end()
    stops = [m.start() for m in (re.search(r"^## ", markdown[start:], re.M), re.search(r"^---$", markdown[start:], re.M)) if m]
    return start, start + min(stops) if stops else len(markdown)


def link_class(markdown: str, class_id: str, class_dir: str) -> str:
    """Devuelve ``markdown`` con los términos de la clase enlazados al glosario."""
    table = _by_key()

    def linkify(match: re.Match[str]) -> str:
        term = match.group(1).strip(" :")
        base, _ = data.variants_of(term)
        concept = table.get(data.key_of(base))
        if concept is None:
            return match.group(0)
        inner = match.group(1)
        trailing = ":" if inner.rstrip().endswith(":") else ""
        label = inner.rstrip(" :")
        return f"**[{label}]({entry_href(class_dir, concept)}){trailing}**"

    for name in SECTION_NAMES:
        bounds = _section_bounds(markdown, name)
        if bounds:
            start, end = bounds
            markdown = markdown[:start] + BOLD_TERM.sub(linkify, markdown[start:end]) + markdown[end:]
    bounds = _section_bounds(markdown, "Glosario")
    concepts = sorted(_by_class().get(class_id, []), key=lambda c: data.fold(c.name))
    if bounds and concepts:
        start, end = bounds
        glossary_readme = cross_references.relative_link(class_dir, "glosario/README.md")
        links = " · ".join(f"[{c.name}]({entry_href(class_dir, c)})" for c in concepts)
        block = f"\n\nConceptos de esta clase en el [glosario del programa]({glossary_readme}): {links}.\n"
        markdown = markdown[:end].rstrip("\n") + block + "\n" + markdown[end:].lstrip("\n")
    return markdown


def class_dir_of(lesson_path: str) -> str:
    return posixpath.normpath(lesson_path)
