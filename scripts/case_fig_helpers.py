"""Shared drawing helpers for the failure-case figure scripts (not a figure module: it has no FIGURES).

Every helper returns a finished ``Fig`` of kind "diagram" and refuses to overflow text.
"""
from __future__ import annotations

from figure_kit import Fig, _kit_finish, _kit_start, _wrap


def _bx(f: Fig, x: float, y: float, w: float, h: float, text: str, kind: str = "plain", size: int = 13,
        bold: bool = False, dashed: bool = False) -> None:
    lines = _wrap(text, size, w - 20)
    assert len(lines) * size * 1.28 <= h - 6, f"box overflows: {text!r} ({len(lines)} lines in {h}px)"
    f.box(x, y, w, h, text, kind, size, bold=bold, dashed=dashed)


def _done(f: Fig, y: float, note: str, foot: str) -> Fig:
    _kit_finish(f, y, note, "gold", foot)
    f.kind = "diagram"
    return f


def layer_stack(title: str, desc: str, layers: list[tuple[str, str, str]], side: list[tuple[str, str]], note: str,
                foot: str, width: int = 940) -> Fig:
    """Vertical stack of layers (top to bottom): (name, detail, kind); ``side`` are (text, kind) notes on the right."""
    f, y = _kit_start(title, desc, width, None)
    h, gap = 66, 14
    for i, (name, detail, kind) in enumerate(layers):
        yy = y + 8 + i * (h + gap)
        _bx(f, 10, yy, 190, h, name, "navy", 13, bold=True)
        _bx(f, 214, yy, 430, h, detail, kind, 13)
    for i, (text, kind) in enumerate(side):
        hh = (len(layers) * (h + gap) - gap) / max(len(side), 1) - gap
        _bx(f, 668, y + 8 + i * (hh + gap), 262, hh, text, kind, 13)
    return _done(f, y + 8 + len(layers) * (h + gap), note, foot)


def kanban(title: str, desc: str, cols: list[tuple[str, str, list[str]]], note: str, foot: str, width: int = 940,
           box_h: int = 70) -> Fig:
    """Columns of boxes: (header, kind, [texts]). Four columns by default (documented status of each mechanism)."""
    f, y = _kit_start(title, desc, width, None)
    n = len(cols)
    gap = 12
    w = (width - 20 - gap * (n - 1)) / n
    most = max(len(c[2]) for c in cols)
    for i, (head, kind, items) in enumerate(cols):
        x = 10 + i * (w + gap)
        _bx(f, x, y + 6, w, 52, head, "navy", 13, bold=True)
        for j, t in enumerate(items):
            _bx(f, x, y + 66 + j * (box_h + 10), w, box_h, t, kind, 13)
    return _done(f, y + 66 + most * (box_h + 10), note, foot)


def hub(title: str, desc: str, center: tuple[str, str], nodes: list[tuple[str, str, str]], note: str, foot: str,
        width: int = 940) -> Fig:
    """Central box with up to 8 satellites in two rows: (text, kind, arrow label)."""
    f, y = _kit_start(title, desc, width, None)
    top = nodes[: (len(nodes) + 1) // 2]
    bot = nodes[(len(nodes) + 1) // 2:]
    w, gap = 214, 12
    def row(items, yy):
        cnt = len(items)
        total = cnt * w + (cnt - 1) * gap
        x0 = (width - total) / 2
        out = []
        for i, (t, k, _lab) in enumerate(items):
            x = x0 + i * (w + gap)
            _bx(f, x, yy, w, 74, t, k, 13)
            out.append(x + w / 2)
        return out
    xt = row(top, y + 6)
    cy = y + 150
    _bx(f, width / 2 - 170, cy, 340, 64, center[0], center[1], 14, bold=True)
    for x, (_, _, lab) in zip(xt, top):
        f.arrow([(x, y + 80), (width / 2 + (x - width / 2) * 0.4, cy)], lab, label_at=(x, y + 112)) if lab else f.arrow([(x, y + 80), (width / 2 + (x - width / 2) * 0.4, cy)])
    if bot:
        xb = row(bot, y + 300)
        for x, (_, _, lab) in zip(xb, bot):
            f.arrow([(width / 2 + (x - width / 2) * 0.4, cy + 64), (x, y + 300)], lab, label_at=(x, y + 270)) if lab else f.arrow([(width / 2 + (x - width / 2) * 0.4, cy + 64), (x, y + 300)])
        end = y + 300 + 74
    else:
        end = cy + 64
    return _done(f, end + 14, note, foot)
