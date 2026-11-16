"""Añade a cada clase de la guía razonada de una parte su enlace «Abrir la clase».

Uso: python scripts/link_part_classes.py [NN ...]   (sin argumentos: todas las partes sin enlaces)
Idempotente: no toca las clases que ya tienen el enlace.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEAD = re.compile(r"^#### (SE-(\d{3})) — .+$")
LINK = re.compile(r"\]\([^)]*se-\d{3}-")


def class_dirs(part: str) -> tuple[Path, dict[int, str]]:
    pdir = next((ROOT / "classes").glob(f"part-{part}-*"))
    return pdir, {int(d.name[3:6]): d.name for d in pdir.glob("se-*") if d.is_dir()}


def link_part(part: str) -> int:
    readme = ROOT / "content" / f"part-{part}" / "README.md"
    text = readme.read_text(encoding="utf-8")
    pdir, dirs = class_dirs(part)
    lines = text.split("\n")
    out: list[str] = []
    changed = 0
    i = 0
    while i < len(lines):
        out.append(lines[i])
        m = HEAD.match(lines[i])
        if m:
            n = int(m.group(2))
            # ¿ya hay enlace dentro de la sección?
            j = i + 1
            section: list[str] = []
            while j < len(lines) and not lines[j].startswith("#"):
                section.append(lines[j])
                j += 1
            if n in dirs and not any(LINK.search(s) for s in section):
                rel = f"../../classes/{pdir.name}/{dirs[n]}/"
                out.append("")
                out.append(f"[Abrir la clase {m.group(1)}]({rel})")
                changed += 1
        i += 1
    if changed:
        readme.write_text("\n".join(out), encoding="utf-8")
    return changed


def main() -> None:
    parts = sys.argv[1:] or sorted(p.name[5:] for p in (ROOT / "content").glob("part-*"))
    for p in parts:
        n = link_part(p)
        if n:
            print(f"part-{p}: {n} enlaces añadidos")


if __name__ == "__main__":
    main()
