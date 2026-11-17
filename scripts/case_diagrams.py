"""Shared diagram helpers for the success-case figures (casos/exito/*.md).

Thin layer over scripts/figure_kit.py: a canvas with a wrapped title, boxes that raise ValueError when
their text does not fit, a sequence diagram, rows of journey steps and a closing note + footer. Nothing
here draws a table: the case guide forbids figures that repeat a Markdown table.
"""
from __future__ import annotations

import re

from figure_kit import Fig, _wrap

ARROW = "#32505f"
INK = "#142231"


def years(fig: Fig) -> Fig:
    """The kit groups thousands with a space; a year is not a quantity, so join them again."""
    fig.parts = [re.sub(r">([12]) (\d{3})<", r">\g<1>\g<2><", p) for p in fig.parts]
    return fig


def canvas(title: str, desc: str, width: int = 940) -> Fig:
    f = Fig(width, 0, title, desc)
    for i, line in enumerate(_wrap(title, 15, width - 28)):
        f.text(14, 27 + i * 19, line, 15, "start", 700, INK)
    return f


def need(text: str, w: float, h: float, size: int = 13, inset: float = 0) -> None:
    lines = _wrap(text, size, w - 20)
    if len(lines) * size * 1.28 + 8 + inset > h:
        raise ValueError(f"text does not fit in {w:g}x{h:g}: {text!r} ({len(lines)} lines)")


def B(f: Fig, x: float, y: float, w: float, h: float, text: str, kind: str = "plain", size: int = 13,
      bold: bool = False, dashed: bool = False) -> None:
    need(text, w, h, size)
    f.box(x, y, w, h, text, kind, size, bold=bold, dashed=dashed)


def G(f: Fig, x: float, y: float, w: float, h: float, label: str, kind: str = "grey") -> None:
    f.group(x, y, w, h, label, kind)


def finish(f: Fig, y: float, note: str, foot: str, kind: str = "gold") -> Fig:
    lines = len(_wrap(note, 13, f.width - 40))
    h = max(54, lines * 13 * 1.28 + 26)
    f.box(10, y, f.width - 20, h, note, kind, 13)
    f.text(f.width / 2, y + h + 20, foot, 12, "middle", 400, "#5c1f14")
    f.height = int(y + h + 34)
    return f


def legend(f: Fig, y: float, text: str = "Trazo continuo: documentado en una fuente citada. Trazo punteado: inferido por el curso.") -> None:
    f.text(14, y, text, 13, "start", 400, "#32505f")


def sequence(title: str, desc: str, actors: list[str], messages: list[tuple], note: str, foot: str,
             note_kind: str = "gold", width: int = 940, row_h: float = 46, kinds: list[str] | None = None, first_gap: float = 34) -> Fig:
    """Sequence diagram. messages: (src, dst, text, style) with style in '', 'dashed' (inferred) or 'ret'."""
    f = canvas(title, desc, width)
    n = len(actors)
    margin = 20
    span = (width - 2 * margin) / n
    xs = [margin + span * (i + 0.5) for i in range(n)]
    top = 58 + 19 * (len(_wrap(title, 15, width - 28)) - 1)
    bw = min(span - 12, 170)
    for i, a in enumerate(actors):
        kind = kinds[i] if kinds else "navy"
        B(f, xs[i] - bw / 2, top, bw, 46, a, kind, 13, bold=True)
    y0 = top + 46
    total = y0 + first_gap - 12 + row_h * len(messages) + 10
    for x in xs:
        f.line(x, y0, x, total - 6, "#8a9aa3", dashed=True, width=1.2)
    y = y0 + first_gap
    for i, msg in enumerate(messages, 1):
        s, d, text, style = (list(msg) + [""])[:4]
        x1, x2 = xs[s], xs[d]
        dashed = style in ("dashed", "ret")
        if s == d:
            f.arrow([(x1, y - 6), (x1 + 46, y - 6), (x1 + 46, y + 8), (x1 + 4, y + 8)], dashed=dashed)
            f.text(x1 + 54, y + 4, f"{i}. {text}", 13, "start", 400, INK, halo=True)
        else:
            sx, ex = (x1 + 3, x2 - 3) if x2 > x1 else (x1 - 3, x2 + 3)
            f.arrow([(sx, y), (ex, y)], dashed=dashed)
            mid = (x1 + x2) / 2
            label = f"{i}. {text}"
            lines = _wrap(label, 13, max(abs(x2 - x1) + 60, 200))
            if len(lines) > 2:
                raise ValueError(f"message too long: {label!r}")
            half = max(len(l) for l in lines) * 13 * 0.56 / 2
            mid = min(max(mid, half + 8), width - half - 8)
            f.text(mid, y - 8 - 16 * (len(lines) - 1), "\n".join(lines), 13, "middle", 400, INK, halo=True)
        y += row_h
    return finish(f, total + 8, note, foot, note_kind)


def lane_steps(f: Fig, y: float, name: str, steps: list[tuple[str, str]], *, name_w: float = 150, h: float = 76,
               kind: str = "navy", gap: float = 14) -> float:
    """A row: lane name box and n step boxes joined by arrows. steps: (text, kind or kind+'!' for dashed)."""
    B(f, 10, y, name_w, h, name, kind, 13, bold=True)
    n = len(steps)
    avail = f.width - 20 - name_w - gap
    w = (avail - gap * (n - 1) - 0) / n
    x = 10 + name_w + gap
    for i, (text, k) in enumerate(steps):
        dashed = k.endswith("!")
        B(f, x, y, w, h, text, k.rstrip("!"), 13, dashed=dashed)
        if i:
            f.arrow([(x - gap, y + h / 2), (x, y + h / 2)])
        x += w + gap
    return y + h + 12
