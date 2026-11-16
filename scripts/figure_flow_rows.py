"""Flow rows: each case is a chain of boxes joined by arrows (cause, mechanism, outcome), for figures whose data are text.

Unlike ``Fig.table`` this draws a sequence, not a grid: the arrows say what leads to what and the colour of the last
box says how it ended. It is meant for mechanisms; use the chart primitives of ``figure_kit`` for numbers.
"""
from __future__ import annotations

from collections.abc import Sequence

from figure_kit import Fig, _kit_finish, _kit_start, _wrap, AXIS


def chain_rows(title: str, desc: str, heads: Sequence[str], rows: Sequence[Sequence[tuple[str, str]]],
               widths: Sequence[float], *, note: str = "", note_kind: str = "gold", foot: str = "", width: int = 940,
               gap: float = 34, size: int = 13) -> Fig:
    """``rows`` hold ``(text, kind)`` per step; ``heads`` name each step above the first row."""
    f, y = _kit_start(title, desc, width, None)
    x0 = 14.0
    if x0 + sum(widths) + gap * (len(widths) - 1) > width - 14:
        raise ValueError("chain_rows: the columns do not fit the width")
    x = x0
    for w, h in zip(widths, heads):
        f.text(x + w / 2, y + 12, h, 13, "middle", 700, AXIS)
        x += w + gap
    y += 26
    for row in rows:
        lines = max(len(_wrap(t, size, w - 20)) for (t, _), w in zip(row, widths))
        h = max(46.0, lines * size * 1.28 + 22)
        x = x0
        for i, ((text, kind), w) in enumerate(zip(row, widths)):
            f.box(x, y, w, h, text, kind, size, bold=(i == 0))
            if i < len(row) - 1:
                f.arrow([(x + w + 4, y + h / 2), (x + w + gap - 4, y + h / 2)])
            x += w + gap
        y += h + 12
    return _kit_finish(f, y, note, note_kind, foot)
