"""Genera el «Resumen operativo del recorrido» de cada README de parte.

Esquema canónico de un README de parte desarrollada:

1. ``## Guía razonada clase por clase``: explica las 12 clases, sin enlaces sueltos;
2. ``## Resumen operativo del recorrido``: una tabla con una fila por clase, enlace
   a la clase, su título como núcleo profesional y su aporte acumulativo.

Este script convierte el esquema antiguo (una línea «Abrir la clase» dentro de cada
sección de la guía) en el canónico y sirve también para las partes nuevas: lee la
guía, extrae de cada clase lo que entrega y compone la tabla.

Uso: python scripts/part_summary_tables.py [NN ...]   (sin argumentos: todas las partes)
Idempotente: no toca las partes que ya tienen la tabla.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = "## Resumen operativo del recorrido"
GUIDE = "## Guía razonada clase por clase"
HEAD = re.compile(r"^#### (SE-(\d{3})) — (.+)$")
INLINE_STANDALONE = re.compile(r"^\[Abrir la clase[^\]]*\]\([^)]*\)\s*$")
INLINE_TRAILING = re.compile(r"\s*\[Abrir la clase[^\]]*\]\([^)]*\)\.?")
# Una frase: admite puntos internos (nombres de archivo) que no van seguidos de espacio.
SENTENCE = r"((?:[^.\n]|\.(?=\S))+)\.(?:\s|$)"
DELIVERY = (
    re.compile(r"El estudiante " + SENTENCE),
    re.compile(r"\bEntrega:? " + SENTENCE),
    re.compile(r"\bProduce " + SENTENCE),
)
MAX_CONTRIBUTION = 170


def class_dirs(part: str) -> tuple[Path, dict[int, str]]:
    pdir = next((ROOT / "classes").glob(f"part-{part}-*"))
    return pdir, {int(d.name[3:6]): d.name for d in pdir.glob("se-*") if d.is_dir()}


def strip_inline_links(lines: list[str]) -> list[str]:
    """Quita los enlaces «Abrir la clase» (línea propia o final de párrafo)."""
    out: list[str] = []
    for line in lines:
        if INLINE_STANDALONE.match(line):
            if out and out[-1] == "":
                out.pop()  # el hueco que separaba el enlace del texto
            continue
        out.append(INLINE_TRAILING.sub("", line))
    return out


def contribution(body: str) -> str:
    """Aporte acumulativo: lo que la clase entrega, en una frase corta."""
    for pattern in DELIVERY:
        found = pattern.search(body)
        if not found:
            continue
        text = found.group(1).strip()
        if pattern is DELIVERY[0]:
            text = text[0].upper() + text[1:]
        else:
            verb = "Entrega" if pattern is DELIVERY[1] else "Produce"
            text = f"{verb} {text}"
        if len(text) > MAX_CONTRIBUTION:
            cut = text.rfind(", ", 60, MAX_CONTRIBUTION)
            cut = cut if cut > 0 else text.rfind(" y ", 60, MAX_CONTRIBUTION)
            if cut > 0:
                text = text[:cut]
        return text.replace("|", "/")
    # Sin frase de entrega explícita (talleres y proyectos): la última frase de
    # contenido, sin el puntero a la clase siguiente.
    sentences = [
        x.strip()
        for x in re.findall(SENTENCE, body)
        if "`SE-" not in x and not x.startswith("La Parte")
    ]
    if not sentences:
        raise ValueError("no hay frase de entrega en: " + body[-300:])
    last = sentences[-1].replace("|", "/")
    if last.startswith("Se entrega "):
        last = "Entrega " + last[len("Se entrega "):]
    return last


def guide_bounds(lines: list[str]) -> tuple[int, int]:
    start = next(i for i, line in enumerate(lines) if line == GUIDE)
    end = next(
        (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines)
    )
    return start, end


def build_table(part: str, guide: list[str]) -> list[str]:
    pdir, dirs = class_dirs(part)
    sections: dict[int, tuple[str, list[str]]] = {}
    current = None
    for line in guide:
        match = HEAD.match(line)
        if match:
            current = int(match.group(2))
            sections[current] = (match.group(3).strip(), [])
        elif current is not None:
            sections[current][1].append(line)
    rows = ["| Clase | Núcleo profesional | Aporte acumulativo |", "|---|---|---|"]
    for number in sorted(sections):
        title, body = sections[number]
        text = " ".join(line.strip() for line in body if line.strip())
        rel = f"../../classes/{pdir.name}/{dirs[number]}/"
        rows.append(
            f"| [SE-{number:03d}]({rel}) | {title.replace('|', '/')} | {contribution(text)} |"
        )
    return rows


def convert_part(part: str) -> bool:
    readme = ROOT / "content" / f"part-{part}" / "README.md"
    text = readme.read_text(encoding="utf-8")
    if SUMMARY in text.split("\n"):
        return False
    lines = text.split("\n")
    start, end = guide_bounds(lines)
    guide = strip_inline_links(lines[start:end])
    while guide and guide[-1] == "":
        guide.pop()
    table = build_table(part, guide)
    result = lines[:start] + guide + ["", SUMMARY, ""] + table + [""] + lines[end:]
    readme.write_text("\n".join(result), encoding="utf-8", newline="\n")
    return True


def main() -> None:
    parts = sys.argv[1:] or sorted(p.name[5:] for p in (ROOT / "content").glob("part-*"))
    for part in parts:
        if convert_part(part):
            print(f"part-{part}: resumen operativo generado")


if __name__ == "__main__":
    main()
