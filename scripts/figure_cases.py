"""Case cards: a figure for qualitative results that no axis can carry (an error, a verdict, a rule).

Each case is a card: the situation on the left, an arrow, the observed outcome on the right (colour =
verdict: coral falls over or surprises, teal holds, gold depends) and one line with the cause. It is a
mechanism diagram read top to bottom, not a table: there are no columns, headings or cell borders.
"""
from __future__ import annotations

from figure_kit import FILL, INK, Fig, _wrap

MUTED = "#4a5d68"
VERDICTS = (("coral", "falla o sorprende"), ("teal", "se sostiene"), ("gold", "depende"))


def case_cards(title: str, desc: str, cases, *, note: str = "", note_kind: str = "gold", foot: str = "",
               width: int = 940, left: float = 0.42, size: int = 13) -> Fig:
    """``cases`` is a list of ``(situation, outcome, cause, kind)`` with kind in coral / teal / gold / grey."""
    inner = width - 40
    left_w = inner * left
    gap = 44
    right_w = inner - left_w - gap
    pad = 12
    # heading + verdict key
    head_lines = _wrap(title, 15, width - 28)
    y = 20.0 + len(head_lines) * 19
    key_y = y + 4
    heights = []
    for situation, outcome, cause, _kind in cases:
        a = len(_wrap(situation, size, left_w - 2 * pad))
        b = len(_wrap(outcome, size, right_w - 2 * pad))
        c = len(_wrap(cause, size, inner - 8))
        box_h = max(a, b) * size * 1.28 + 2 * pad
        heights.append((box_h, c * size * 1.28))
    total = sum(bh + ch + 22 for bh, ch in heights) + 14
    note_lines = len(_wrap(note, 13, width - 40)) if note else 0
    note_h = max(54, note_lines * 13 * 1.28 + 26) if note else 0
    height = int(key_y + 34 + total + (note_h + 12 if note else 0) + (30 if foot else 10))
    f = Fig(width, height, title, desc)
    for i, line in enumerate(head_lines):
        f.text(14, 27 + i * 19, line, 15, "start", 700, INK)
    x = 14.0
    for kind, label in VERDICTS:
        f.parts.append(f'<rect x="{x:g}" y="{key_y + 4:g}" width="14" height="14" rx="3" fill="{FILL[kind]}"/>')
        f.text(x + 22, key_y + 16, label, 13, "start", 400, INK)
        x += 40 + len(label) * 7.6
    y = key_y + 34
    for (situation, outcome, cause, kind), (box_h, cause_h) in zip(cases, heights):
        f.box(20, y, left_w, box_h, situation, "navy", size, align="start")
        f.arrow([(20 + left_w + 4, y + box_h / 2), (20 + left_w + gap - 4, y + box_h / 2)])
        f.box(20 + left_w + gap, y, right_w, box_h, outcome, kind, size, bold=True, align="start")
        for i, line in enumerate(_wrap(cause, size, inner - 8)):
            f.text(24, y + box_h + 17 + i * size * 1.28, line, size, "start", 400, MUTED)
        y += box_h + cause_h + 22
    if note:
        f.box(10, y + 2, width - 20, note_h, note, note_kind, 13)
        y += note_h + 12
    if foot:
        f.text(width / 2, y + 16, foot, 12, "middle", 400, "#5c1f14")
    return f
