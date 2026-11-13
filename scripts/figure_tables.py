"""Auto-sized tables and captions on top of ``figure_kit`` (rows grow to fit their text)."""
from __future__ import annotations

from figure_kit import Fig, _wrap


def lines_needed(text: str, size: int, width: float, gap: float = 6) -> int:
    return len(_wrap(text, size, width - gap - 20))


def table(f: Fig, heads: list[str], rows: list[list[str]], x: float, y: float, widths: list[float],
          size: int = 13, kinds: list[str] | None = None, first_bold: bool = True, gap: float = 6) -> float:
    """Draw a table whose row heights follow the longest cell; return the y below it."""
    cx = x
    for width, head in zip(widths, heads):
        f.box(cx, y, width - gap, 36, head, "navy", size, bold=True)
        cx += width
    cy = y + 36 + gap
    for i, row in enumerate(rows):
        need = max(lines_needed(cell, size, w, gap) for w, cell in zip(widths, row))
        height = max(40, need * size * 1.28 + 20)
        cx = x
        for j, (width, cell) in enumerate(zip(widths, row)):
            kind = kinds[j] if kinds else "plain"
            if isinstance(kind, tuple):
                kind = kind[i]
            f.box(cx, cy, width - gap, height, cell, kind, size, bold=(first_bold and j == 0))
            cx += width
        cy += height + gap
    return cy


def note(f: Fig, y: float, text: str, kind: str = "gold", size: int = 13, x: float = 10, w: float | None = None) -> float:
    """A full-width box sized to its text; return the y below it."""
    w = w if w is not None else f.width - 2 * x
    height = lines_needed(text, size, w, 0) * size * 1.28 + 20
    f.box(x, y, w, height, text, kind, size)
    return y + height + 8


def finish(f: Fig, bottom: float) -> Fig:
    f.height = int(bottom + 6)
    return f
