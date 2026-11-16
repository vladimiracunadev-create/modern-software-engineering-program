"""Diagram helpers that replace figures which used to redraw a Markdown table with ``Fig.table()``.

``mapa``     one row per case: left box -> coloured verdict box -> right box, joined by arrows.
``columnas`` one row per case: a label box that forks into one outcome box per environment; adjacent
             identical outcomes merge into a single wide box, so a difference is a split and a
             coincidence is a join.
"""
from __future__ import annotations

from figure_kit import Fig, _wrap

EJEC = ""


def _fits(title: str, text: str, width: float, size: int, row_h: float) -> None:
    lines = len(_wrap(text, size, width - 20))
    assert lines * size * 1.28 <= row_h - 12, f"box overflows in {title!r}: {text!r} ({lines} lines in {width} px)"


def _tail(f: Fig, y: float, width: int, note: str, note_kind: str, foot: str) -> int:
    note_lines = len(_wrap(note, 13, width - 40)) if note else 0
    note_h = max(54, note_lines * 13 * 1.28 + 26) if note else 0
    if note:
        f.box(10, y + 14, width - 20, note_h, note, note_kind, 13)
        y += note_h + 22
    if foot:
        f.text(width / 2, y + 16, foot, 12, "middle", 400, "#5c1f14")
    return 0


def _height(last_bottom: float, note: str, width: int, foot: str) -> int:
    note_lines = len(_wrap(note, 13, width - 40)) if note else 0
    note_h = max(54, note_lines * 13 * 1.28 + 26) if note else 0
    return int(last_bottom + (note_h + 22 if note else 8) + (26 if foot else 6))


def mapa(title: str, desc: str, rows: list[tuple[str, str, str, str]], note: str = "", note_kind: str = "gold", foot: str = EJEC,
         width: int = 960, left_w: float = 300, mid_w: float = 250, row_h: float = 76, gap: float = 36, size: int = 13,
         heads: tuple[str, str, str] | None = None, stack: bool = False) -> Fig:
    """``rows`` are ``(left text, verdict text, verdict kind, right text)``; ``heads`` names the three columns."""
    right_w = width - 20 - left_w - mid_w - 2 * gap
    for left, mid, _, right in rows:
        for text, w in ((left, left_w), (mid, mid_w), (right, right_w)):
            _fits(title, text, w, size, row_h)
    top = 14.0 + (24 if heads else 0)
    last_bottom = top + len(rows) * row_h + (len(rows) - 1) * 18
    f = Fig(width, _height(last_bottom, note, width, foot), title, desc)
    x1, x2, x3 = 10.0, 10.0 + left_w + gap, 10.0 + left_w + gap + mid_w + gap
    if heads:
        for x, w, h in ((x1, left_w, heads[0]), (x2, mid_w, heads[1]), (x3, right_w, heads[2])):
            f.text(x + w / 2, 24, h, 13, "middle", 700, "#32505f")
    y = top
    for left, mid, kind, right in rows:
        f.box(x1, y, left_w, row_h, left, "plain", size)
        f.box(x2, y, mid_w, row_h, mid, kind, size, True)
        f.box(x3, y, right_w, row_h, right, "grey", size)
        f.arrow([(x1 + left_w, y + row_h / 2), (x2, y + row_h / 2)])
        f.arrow([(x2 + mid_w, y + row_h / 2), (x3, y + row_h / 2)])
        if stack and y + row_h + 18 < last_bottom:
            f.arrow([(x1 + left_w / 2, y + row_h), (x1 + left_w / 2, y + row_h + 18)])
        y += row_h + 18
    _tail(f, last_bottom, width, note, note_kind, foot)
    return f


def columnas(title: str, desc: str, rows: list[tuple], heads: list[str], kinds: list[str], note: str = "",
             note_kind: str = "gold", foot: str = EJEC, width: int = 960, label_w: float = 270, row_h: float = 56,
             gap: float = 40, size: int = 13, same_kind: str = "grey") -> Fig:
    """``rows`` are ``(label, outcome per column ...)``; identical neighbouring outcomes merge into one box."""
    n = len(heads)
    region = width - 20 - label_w - gap
    col_w = (region - (n - 1) * 8) / n
    for row in rows:
        _fits(title, row[0], label_w, size, row_h)
        j = 1
        while j <= n:
            k = j
            while k < n and row[k + 1] == row[j]:
                k += 1
            _fits(title, row[j], col_w * (k - j + 1) + 8 * (k - j), size, row_h)
            j = k + 1
    top = 14.0 + 34
    last_bottom = top + len(rows) * row_h + (len(rows) - 1) * 18
    f = Fig(width, _height(last_bottom, note, width, foot), title, desc)
    cx0 = 10.0 + label_w + gap
    for j, (h, kind) in enumerate(zip(heads, kinds)):
        f.box(cx0 + j * (col_w + 8), 12, col_w, 28, h, kind, size, True)
    y = top
    for row in rows:
        f.box(10, y, label_w, row_h, row[0], "plain", size, True)
        f.box(cx0 - 5, y - 5, region + 10, row_h + 10, "", "plain", size, dashed=True, radius=12)
        f.arrow([(10 + label_w, y + row_h / 2), (cx0 - 5, y + row_h / 2)])
        j = 1
        while j <= n:
            k = j
            while k < n and row[k + 1] == row[j]:
                k += 1
            x = cx0 + (j - 1) * (col_w + 8)
            w = col_w * (k - j + 1) + 8 * (k - j)
            kind = same_kind if k > j else kinds[j - 1]
            f.box(x, y, w, row_h, row[j], kind, size)
            j = k + 1
        y += row_h + 18
    _tail(f, last_bottom, width, note, note_kind, foot)
    return f
