"""Mechanism diagrams for figures whose table has no numeric story: fan-out, fan-in, chains and nested levels.

They complement the chart primitives of ``figure_kit`` (see docs/FIGURE-REDESIGN-GUIDE.md). Every card is
checked to fit its box (``ValueError`` otherwise), text is at least 13 px and the result is a ``Fig`` with a
visible title, an optional note and a footer, like the chart primitives.
"""
from __future__ import annotations

from figure_kit import PALETTE, Fig, _kit_finish, _kit_start, _wrap

LINE = 13 * 1.28


def _card_height(head: str, detail: str, w: float) -> float:
    lines = len(_wrap(head, 13, w - 20)) + len(_wrap(detail, 13, w - 20)) if detail else len(_wrap(head, 13, w - 20))
    return lines * LINE + 20


def card(f: Fig, x: float, y: float, w: float, h: float, head: str, detail: str = "", kind: str = "plain",
         dashed: bool = False) -> None:
    """Rounded box with a bold head and a regular detail, vertically centred; raises if the text does not fit."""
    need = _card_height(head, detail, w)
    if need > h + 0.5:
        raise ValueError(f"card text does not fit ({need:.0f}px needed, {h:.0f}px available): {head!r}")
    f.box(x, y, w, h, "", kind, dashed=dashed)
    _, _, ink = PALETTE[kind]
    head_lines = _wrap(head, 13, w - 20)
    detail_lines = _wrap(detail, 13, w - 20) if detail else []
    top = y + (h - (len(head_lines) + len(detail_lines)) * LINE) / 2 + 13 * 0.92
    for i, line in enumerate(head_lines):
        f.text(x + w / 2, top + i * LINE, line, 13, "middle", 700, ink)
    for j, line in enumerate(detail_lines):
        f.text(x + w / 2, top + (len(head_lines) + j) * LINE, line, 13, "middle", 400, ink)


def _finish(f: Fig, y: float, note: str, note_kind: str, foot: str) -> Fig:
    out = _kit_finish(f, y, note, note_kind, foot)
    out.kind = "diagram"
    return out


def fan(title: str, desc: str, root: tuple[str, str, str], outcomes: list[tuple], *, arrow_label: str = "",
        note: str = "", note_kind: str = "gold", foot: str = "", width: int = 940, root_w: float = 250) -> Fig:
    """One cause on the left, several outcomes on the right. ``outcomes`` are ``(head, detail, kind[, dashed])``."""
    f, y = _kit_start(title, desc, width, None)
    x_out = 14 + root_w + 70
    w_out = width - 14 - x_out
    heights = [max(54.0, _card_height(o[0], o[1], w_out)) for o in outcomes]
    gap = 12.0
    total = sum(heights) + gap * (len(outcomes) - 1)
    root_h = max(70.0, _card_height(root[0], root[1], root_w))
    top = y + max(0.0, (root_h - total) / 2) + 4
    cy_root = top + total / 2
    card(f, 14, cy_root - root_h / 2, root_w, root_h, root[0], root[1], root[2])
    mid_x = 14 + root_w + 35
    cy = top
    for o, h in zip(outcomes, heights):
        kind, dashed = o[2], (o[3] if len(o) > 3 else False)
        card(f, x_out, cy, w_out, h, o[0], o[1], kind, dashed)
        f.arrow([(14 + root_w, cy_root), (mid_x, cy_root), (mid_x, cy + h / 2), (x_out, cy + h / 2)],
                color="#c0432f" if kind == "coral" else "#32505f", dashed=dashed)
        cy += h + gap
    if arrow_label:
        f.text(14 + root_w + 35, top - 10, arrow_label, 13, "middle", 400, "#5b7280")
    return _finish(f, max(top + total, cy_root + root_h / 2) + 8, note, note_kind, foot)


def merge(title: str, desc: str, inputs: list[tuple], final: tuple[str, str, str], *, note: str = "",
          note_kind: str = "gold", foot: str = "", width: int = 940, final_w: float = 250) -> Fig:
    """Several conditions on the left that must hold for one result on the right. ``inputs``: ``(head, detail, kind)``."""
    f, y = _kit_start(title, desc, width, None)
    w_in = width - 14 - (14 + final_w + 70)
    heights = [max(54.0, _card_height(i[0], i[1], w_in)) for i in inputs]
    gap = 12.0
    total = sum(heights) + gap * (len(inputs) - 1)
    final_h = max(70.0, _card_height(final[0], final[1], final_w))
    top = y + 4
    cy_final = top + total / 2
    x_final = width - 14 - final_w
    cy = top
    mid_x = 14 + w_in + 35
    for i, h in zip(inputs, heights):
        card(f, 14, cy, w_in, h, i[0], i[1], i[2])
        f.arrow([(14 + w_in, cy + h / 2), (mid_x, cy + h / 2), (mid_x, cy_final), (x_final, cy_final)])
        cy += h + gap
    card(f, x_final, cy_final - final_h / 2, final_w, final_h, final[0], final[1], final[2])
    return _finish(f, max(top + total, cy_final + final_h / 2) + 8, note, note_kind, foot)


def chain(title: str, desc: str, steps: list[tuple], *, labels: list[str] | None = None, note: str = "",
          note_kind: str = "gold", foot: str = "", width: int = 940) -> Fig:
    """A row of cards joined by arrows. ``steps`` are ``(head, detail, kind)``; ``labels`` go on the arrows."""
    f, y = _kit_start(title, desc, width, None)
    n = len(steps)
    gap = 36.0 if not labels else 60.0
    w = (width - 28 - gap * (n - 1)) / n
    h = max(_card_height(s[0], s[1], w) for s in steps)
    top = y + 4
    for i, s in enumerate(steps):
        x = 14 + i * (w + gap)
        card(f, x, top, w, h, s[0], s[1], s[2])
        if i < n - 1:
            f.arrow([(x + w, top + h / 2), (x + w + gap, top + h / 2)])
            if labels and labels[i]:
                for k, line in enumerate(_wrap(labels[i], 13, gap + 6)):
                    f.text(x + w + gap / 2, top + h / 2 - 10 - (len(_wrap(labels[i], 13, gap + 6)) - 1 - k) * 15, line, 13, "middle", 400, "#142231")
    return _finish(f, top + h + 8, note, note_kind, foot)


def nested(title: str, desc: str, levels: list[tuple], *, note: str = "", note_kind: str = "gold", foot: str = "",
           width: int = 940) -> Fig:
    """Concentric levels, outermost first. ``levels`` are ``(head, detail, kind, dashed)``; text sits in the top band."""
    f, y = _kit_start(title, desc, width, None)
    band = 40.0
    top = y + 4
    n = len(levels)
    base = n * (band + 6) + 24
    for i, lv in enumerate(levels):
        x0 = 14 + i * 22.0
        y0 = top + i * (band + 6)
        h = base - i * (band + 6) + (n - 1 - i) * 10
        fill, stroke, ink = PALETTE[lv[2]]
        dashed = lv[3] if len(lv) > 3 else False
        dash = ' stroke-dasharray="8 5"' if dashed else ""
        f.parts.append(f'<rect x="{x0:g}" y="{y0:g}" width="{width - 2 * x0:g}" height="{h:g}" rx="14" fill="{fill}" '
                       f'fill-opacity="0.55" stroke="{stroke}" stroke-width="1.8"{dash}/>')
        room = width - 2 * x0 - 28
        if (len(lv[0]) * 0.62 + len(lv[1]) * 0.56) * 13 + 8 > room:
            raise ValueError(f"nested level text does not fit: {lv[0]!r}")
        f.text(x0 + 14, y0 + 24, lv[0], 13, "start", 700, ink)
        f.text(x0 + 14 + len(lv[0]) * 13 * 0.62 + 8, y0 + 24, lv[1], 13, "start", 400, ink)
    total = base + (n - 1) * 10
    return _finish(f, top + total + 6, note, note_kind, foot)
