"""Data-driven figure builders shared by the failure cases added in the second batch.

Each builder lays out boxes with automatic heights (text is wrapped, so a label never overflows) and
returns a finished ``Fig``. Only layout lives here: every number, claim and source footer stays in the
``figures_case_<slug>.py`` file that calls the builder. Figures never draw tables.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_helpers_fallo import done as _done, sketch, slices  # noqa: E402
from figure_kit import Fig, _wrap  # noqa: E402

RED = "#c0432f"


def done(f: Fig, y: float, note: str, kind: str = "gold", foot: str = "") -> Fig:
    """Like the shared ``done`` but a long source footer wraps onto a second line instead of being clipped."""
    lines = _wrap(foot, 12, 880) if foot else []
    if len(lines) <= 1:
        return _done(f, y, note, kind, foot)
    assert len(lines) <= 3, f"footer too long: {foot!r}"
    _done(f, y, note, kind, lines[0])
    base = f.height - 18
    for i, extra in enumerate(lines[1:], 1):
        f.text(f.width / 2, base + 16 * i, extra, 12, "middle", 400, "#7a2e1d")
    f.height = int(f.height + 16 * (len(lines) - 1))
    return f


def _h(text: str, w: float, size: int = 13, minh: float = 40) -> float:
    return max(minh, len(_wrap(text, size, w - 20)) * size * 1.28 + 14)


def _box(f: Fig, x: float, y: float, w: float, text: str, kind: str = "plain", h: float | None = None,
         bold: bool = False, dashed: bool = False) -> float:
    h = h or _h(text, w)
    f.box(x, y, w, h, text, kind, 13, bold=bold, dashed=dashed)
    return h


def chain(title: str, desc: str, steps: list[tuple], note: str, foot: str, per_row: int = 4,
          note_kind: str = "gold", arrows: list[str] | None = None) -> Fig:
    """Rows of boxes joined by arrows, read left to right; each row connects to the next with an elbow. ``steps`` = (text, kind[, bold]); ``arrows`` = optional labels between steps."""
    f, y = sketch(title, desc)
    gap = 40
    w = (920 - gap * (per_row - 1)) / per_row
    y0 = y + 6
    rows = [steps[i:i + per_row] for i in range(0, len(steps), per_row)]
    prev_exit: float | None = None
    prev_bottom = 0.0
    for r, row in enumerate(rows):
        rh = max(_h(s[0], w) for s in row)
        xs = [10 + i * (w + gap) for i in range(len(row))]
        if prev_exit is not None:
            mid = prev_bottom + 15
            f.arrow([(prev_exit + w / 2, prev_bottom), (prev_exit + w / 2, mid), (xs[0] + w / 2, mid), (xs[0] + w / 2, y0)])
        for i, s in enumerate(row):
            _box(f, xs[i], y0, w, s[0], s[1], rh, bold=len(s) > 2 and bool(s[2]))
        for i in range(len(row) - 1):
            gi = r * per_row + i
            lab = arrows[gi] if arrows and gi < len(arrows) else ""
            a, b = xs[i], xs[i + 1]
            yc = y0 + rh / 2
            if a < b:
                f.arrow([(a + w, yc), (b, yc)], lab, label_at=((a + w + b) / 2, yc - 8) if lab else None)
            else:
                f.arrow([(a, yc), (b + w, yc)], lab, label_at=((a + b + w) / 2, yc - 8) if lab else None)
        prev_exit, prev_bottom = xs[-1], y0 + rh
        y0 += rh + 34
    return done(f, y0 - 24, note, note_kind, foot)


def columns(title: str, desc: str, cols: list[tuple[str, str, list[str]]], note: str, foot: str,
            note_kind: str = "gold") -> Fig:
    """Columns with a header and stacked boxes. ``cols`` = (header, kind, items)."""
    f, y = sketch(title, desc)
    n = len(cols)
    gap = 18
    w = (920 - gap * (n - 1)) / n
    y0 = y + 6
    bottom = y0
    for c, (head, kind, items) in enumerate(cols):
        x = 10 + c * (w + gap)
        hh = _box(f, x, y0, w, head, kind, bold=True)
        yy = y0 + hh + 10
        for it in items:
            yy += _box(f, x, yy, w, it, "plain") + 8
        bottom = max(bottom, yy)
    return done(f, bottom + 4, note, note_kind, foot)


def layers(title: str, desc: str, rows: list[tuple[str, str, str]], note: str, foot: str,
           note_kind: str = "gold") -> Fig:
    """Stack of layers: (label, status, detail); status doc (teal), part (gold) or unk (grey)."""
    f, y = sketch(title, desc)
    kinds = {"doc": "teal", "part": "gold", "unk": "grey"}
    y0 = y + 6
    for label, status, detail in rows:
        h = max(_h(label, 250), _h(detail, 660))
        _box(f, 10, y0, 250, label, kinds[status], h, bold=True)
        _box(f, 270, y0, 660, detail, "plain", h)
        y0 += h + 8
    return done(f, y0 + 2, note, note_kind, foot)


def context(title: str, desc: str, left: list[tuple[str, str]], center: tuple[str, list[tuple[str, str]]],
            right: list[tuple[str, str]], note: str, foot: str, left_labels: list[str] | None = None,
            right_labels: list[str] | None = None, note_kind: str = "gold") -> Fig:
    """Context diagram: actors left, system group in the centre (name, inner boxes), actors right."""
    f, y = sketch(title, desc)
    y0 = y + 6
    lw, cw = 200, 330
    inner = [(t, k, _h(t, cw - 10)) for t, k in center[1]]
    ch = 50 + sum(h + 10 for _, _, h in inner)

    def col(items, x):
        ys, yy = [], y0
        for t, k in items:
            h = _h(t, lw)
            _box(f, x, yy, lw, t, k, h)
            ys.append(yy + h / 2)
            yy += h + 14
        return ys, yy

    ly, lb = col(left, 10)
    ry, rb = col(right, 730)
    total = max(ch, lb - y0, rb - y0)
    f.group(280, y0, cw + 40, total, center[0], "grey")
    yy = y0 + 40
    for t, k, h in inner:
        _box(f, 300, yy, cw, t, k, h)
        yy += h + 10
    for i, yc in enumerate(ly):
        lab = left_labels[i] if left_labels and i < len(left_labels) else ""
        f.arrow([(210, yc), (280, yc)], lab, label_at=(245, yc - 8) if lab else None)
    for i, yc in enumerate(ry):
        lab = right_labels[i] if right_labels and i < len(right_labels) else ""
        f.arrow([(650, yc), (730, yc)], lab, label_at=(690, yc - 8) if lab else None)
    return done(f, y0 + total + 8, note, note_kind, foot)


def fault_tree(title: str, desc: str, top: str, gate_a: tuple[str, str, list[str]], gate_b: tuple[str, str, list[str]],
               note: str, foot: str, note_kind: str = "gold") -> Fig:
    """Two-branch fault tree under an AND gate. ``gate_x`` = (branch label, "Y" or "O", leaves)."""
    f, y = sketch(title, desc)
    y0 = y + 6
    th = _box(f, 270, y0, 400, top, "navy", bold=True)
    f.dot(470, y0 + th + 24, "Y", "navy")
    f.arrow([(470, y0 + th), (470, y0 + th + 12)])
    my = y0 + th + 64
    bottoms = []
    for gx, (label, gate, leaves) in zip((10, 485), (gate_a, gate_b)):
        w = 445
        cx = gx + w / 2
        mh = _box(f, gx, my, w, label, "coral", bold=True)
        f.line(470, y0 + th + 36, cx, my)
        f.dot(cx, my + mh + 22, gate, "navy")
        f.line(cx, my + mh, cx, my + mh + 12)
        yy = my + mh + 44
        for lf in leaves:
            h = _box(f, gx + 30, yy, w - 60, lf, "gold")
            f.line(cx, yy - 8, cx, yy)
            yy += h + 8
        bottoms.append(yy)
    return done(f, max(bottoms) + 2, note, note_kind, foot)


def pairs(title: str, desc: str, items: list[tuple[str, str]], note: str, foot: str, per_row: int = 4,
          top_kind: str = "coral", bottom_kind: str = "teal", note_kind: str = "teal") -> Fig:
    """Each item = (cause or gap, control or improvement): top box above bottom box, joined by an arrow."""
    f, y = sketch(title, desc)
    gap = 20
    w = (920 - gap * (per_row - 1)) / per_row
    y0 = y + 6
    for r in range(0, len(items), per_row):
        row = items[r:r + per_row]
        ha = max(_h(a, w) for a, _ in row)
        hb = max(_h(b, w) for _, b in row)
        for i, (a, b) in enumerate(row):
            x = 10 + i * (w + gap)
            _box(f, x, y0, w, a, top_kind, ha)
            _box(f, x, y0 + ha + 28, w, b, bottom_kind, hb)
            f.arrow([(x + w / 2, y0 + ha), (x + w / 2, y0 + ha + 28)], dashed=True)
        y0 += ha + hb + 28 + 16
    return done(f, y0, note, note_kind, foot)


def barrier_slices(title: str, desc: str, items: list[tuple[str, str]], note: str, foot: str,
                   note_kind: str = "coral") -> Fig:
    """Swiss-cheese view, up to eight barriers: ``items`` = (label, kind coral|gold|teal); a red arrow crosses the holes."""
    f, y = sketch(title, desc)
    y0 = y + 6
    n = len(items)
    w = 62 if n >= 7 else 70
    gap = min((880 - n * w) / max(n - 1, 1), 60)
    lw = w + gap - 6
    yy = slices(f, y0, [(lab, kind, 0.5) for lab, kind in items], x0=30, w=w, gap=gap, h=170, label_h=150, label_w=lw)
    ymid = y0 + 18 + 0.5 * (170 - 80) + 22
    f.arrow([(10, ymid), (930, ymid)], color=RED)
    return done(f, yy, note, note_kind, foot)
