"""Shared drawing helpers for the expanded failure-case figures (Knight, HealthCare.gov, TSB, Meta 2021).

Only layout helpers live here; every number and claim stays in each ``figures_case_<slug>.py`` with its
own source footer. Helpers raise ``AssertionError`` when a label does not fit, so a broken layout fails the build.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from figure_kit import Fig, _kit_finish, _kit_start, _wrap, text_width  # noqa: E402


def sketch(title: str, desc: str, width: int = 940):
    return _kit_start(title, desc, width, None)


def bx(f: Fig, x: float, y: float, w: float, h: float, text: str, kind: str = "plain", size: int = 13,
       bold: bool = False, dashed: bool = False) -> None:
    lines = _wrap(text, size, w - 20)
    assert len(lines) * size * 1.28 <= h - 6, f"box overflows: {text!r} ({len(lines)} lines in {h}px)"
    f.box(x, y, w, h, text, kind, size, bold=bold, dashed=dashed)


def done(f: Fig, y: float, note: str, kind: str = "gold", foot: str = "") -> Fig:
    _kit_finish(f, y, note, kind, foot)
    f.kind = "diagram"
    return f


def fit(label: str, width: float, size: int = 13, weight: int = 400) -> None:
    assert text_width(label, size, weight) <= width, f"label too wide ({text_width(label, size, weight):.0f}>{width:.0f}): {label!r}"


def sequence(f: Fig, y0: float, lanes: list[tuple[str, str]], steps: list[tuple], x0: float = 20, x1: float = 920,
             row_h: float = 36, head_h: float = 46) -> float:
    """UML-like sequence diagram. ``lanes`` = (name, kind). ``steps``:

    ``(a, b, text)`` or ``(a, b, text, "dashed"|"red"|"dashed-red")`` arrow from lane a to lane b;
    ``(a, a, text, "note")`` a note box centred on lane a (width 190). Returns the y below the diagram.
    """
    n = len(lanes)
    gap = (x1 - x0) / n
    cx = [x0 + gap * (i + 0.5) for i in range(n)]
    bw = min(gap - 10, 150)
    for (name, kind), c in zip(lanes, cx):
        bx(f, c - bw / 2, y0, bw, head_h, name, kind, 13, True)
    total = row_h * len(steps) + 14
    for c in cx:
        f.line(c, y0 + head_h, c, y0 + head_h + total, "#8a9aa3", dashed=True, width=1.2)
    y = y0 + head_h + 12
    for i, st in enumerate(steps, 1):
        a, b, text = st[0], st[1], st[2]
        style = st[3] if len(st) > 3 else ""
        yy = y + row_h * (i - 1) + row_h / 2
        label = f"{i}. {text}"
        if style == "note":
            w = 250
            fit(label, w - 14)
            bx(f, min(max(cx[a] - w / 2, 6), f.width - 6 - w), yy - 15, w, 30, label, "gold", 13)
            continue
        red = "red" in style
        dashed = "dashed" in style
        span = abs(cx[b] - cx[a])
        fit(label, max(span, 40) + gap * 0.0 + 6 if a != b else 180)
        color = "#c0432f" if red else "#32505f"
        if a == b:
            f.arrow([(cx[a], yy - 8), (cx[a] + 46, yy - 8), (cx[a] + 46, yy + 8), (cx[a], yy + 8)], "", dashed, color)
            f.text(cx[a] + 54, yy + 4, label, 13, "start", 400, "#142231")
        else:
            f.arrow([(cx[a], yy + 4), (cx[b], yy + 4)], "", dashed, color)
            f.text((cx[a] + cx[b]) / 2, yy - 4, label, 13, "middle", 400, "#142231")
    return y0 + head_h + total + 6


def year_axis(f: Fig, y: float, lo: float, hi: float, events: list[tuple], x0: float = 40, x1: float = 900,
              up: float = 140, down: float = 140, box_w: float = 150, box_h: float = 74, step: float = 1.0,
              tick_fmt=None) -> float:
    """Horizontal time axis with event boxes above or below. ``events`` = (t, text, kind, side, level).

    side is "u" or "d"; level 0, 1 or 2 stacks boxes at different heights so they do not collide.
    Returns the y below the diagram.
    """
    axis_y = y + up
    f.line(x0, axis_y, x1, axis_y, "#32505f", width=2)
    t = lo
    while t <= hi + 1e-9:
        px = x0 + (t - lo) / (hi - lo) * (x1 - x0)
        f.line(px, axis_y - 5, px, axis_y + 5, "#32505f")
        f.text(px, axis_y + 21 if tick_fmt else axis_y + 21, tick_fmt(t) if tick_fmt else f"{t:g}", 13, "middle", 400, "#5b7280")
        t += step
    placed: dict[tuple[str, int], list[tuple[float, float]]] = {}
    for t, text, kind, side, level in events:
        px = x0 + (t - lo) / (hi - lo) * (x1 - x0)
        bxl = min(max(px - box_w / 2, 6), f.width - box_w - 6)
        for a, b in placed.get((side, level), []):
            assert bxl + box_w + 4 <= a or bxl >= b + 4, f"year_axis boxes collide at level {level}: {text!r}"
        placed.setdefault((side, level), []).append((bxl, bxl + box_w))
        if side == "u":
            by = axis_y - 36 - box_h - level * (box_h + 12)
            f.line(px, axis_y, px, by + box_h, "#8a9aa3", dashed=True)
        else:
            by = axis_y + 40 + level * (box_h + 12)
            f.line(px, axis_y, px, by, "#8a9aa3", dashed=True)
        f.dot(px, axis_y, "", kind if kind in ("teal", "coral", "gold", "navy") else "navy")
        bx(f, bxl, by, box_w, box_h, text, kind, 13)
    top_lv = max([e[4] for e in events if e[3] == "u"], default=-1)
    bot_lv = max([e[4] for e in events if e[3] == "d"], default=-1)
    return axis_y + 40 + (bot_lv + 1) * (box_h + 12) + 6 if bot_lv >= 0 else axis_y + 40


def slices(f: Fig, y0: float, items: list[tuple[str, str, float]], x0: float = 30, w: float = 74, gap: float = 28,
           h: float = 190, label_h: float = 118, label_w: float | None = None) -> float:
    """Swiss-cheese defences. ``items`` = (label, kind, hole_y 0..1). Kind coral: absent/failed; teal: worked; gold: partial.

    A hazard arrow crosses the holes that line up. Returns the y below the labels.
    """
    n = len(items)
    lw = label_w or (gap + w - 6)
    for i, (label, kind, hole) in enumerate(items):
        x = x0 + i * (w + gap)
        f.box(x, y0, w, h, "", kind, 13, radius=14)
        hy = y0 + 18 + hole * (h - 80)
        f.parts.append(f'<rect x="{x + 12:g}" y="{hy:g}" width="{w - 24:g}" height="44" rx="10" fill="#ffffff" stroke="#8a9aa3" stroke-width="1" stroke-dasharray="4 3"/>')
        bx(f, x - (lw - w) / 2, y0 + h + 10, lw, label_h, label, kind, 13)
    return y0 + h + label_h + 22
