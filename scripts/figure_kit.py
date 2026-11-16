"""Minimal, dependency-free SVG kit for lesson figures.

Every figure carries <title> and <desc>, uses text of at least 13 px, and never
relies on colour alone: each coloured shape also has a label or a line style.
The output is deterministic so that ``--check`` builds can compare it byte by byte.
"""
from __future__ import annotations

from html import escape

PALETTE = {
    "plain": ("#ffffff", "#5b7280", "#142231"),
    "teal": ("#dff1ee", "#087f8c", "#0b3f45"),
    "coral": ("#fbe4de", "#c0432f", "#5c1f14"),
    "gold": ("#f7ebc8", "#a8761a", "#4a3209"),
    "navy": ("#102a43", "#102a43", "#ffffff"),
    "grey": ("#eef1f2", "#8a9aa3", "#2b3a44"),
}
FONT = "Inter, 'Segoe UI', system-ui, -apple-system, sans-serif"


def _wrap(text: str, size: int, width: float) -> list[str]:
    capacity = max(4, int(width / (size * 0.56)))
    lines: list[str] = []
    for paragraph in text.split("\n"):
        current = ""
        for word in paragraph.split():
            candidate = f"{current} {word}".strip()
            if len(candidate) <= capacity or not current:
                current = candidate
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


class Fig:
    def __init__(self, width: int, height: int, title: str, desc: str) -> None:
        self.width, self.height, self.title, self.desc = width, height, title, desc
        self.parts: list[str] = []
        # "diagram" | "table" (set by figures_part07_a.tab) | "chart" (set by the chart primitives); tests/test_figure_redesign.py counts tables.
        self.kind = "diagram"
        self.table_calls = 0  # Fig.table() calls; a diagram that is mostly a table is also counted by the ratchet

    # -- primitives ---------------------------------------------------------
    def text(self, x: float, y: float, value: str, size: int = 14, anchor: str = "middle",
             weight: int = 400, fill: str = "#142231", italic: bool = False, halo: bool = False) -> None:
        style = ' font-style="italic"' if italic else ""
        if halo:  # white outline so a label stays legible over lines and bars
            style += ' stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round" paint-order="stroke"'
        lines = value.split("\n")
        spans = "".join(
            f'<tspan x="{x:g}" dy="{0 if i == 0 else size * 1.28:g}">{escape(line)}</tspan>'
            for i, line in enumerate(lines)
        )
        self.parts.append(
            f'<text x="{x:g}" y="{y:g}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}" fill="{fill}"{style}>{spans}</text>'
        )

    def box(self, x: float, y: float, w: float, h: float, value: str = "", kind: str = "plain",
            size: int = 14, bold: bool = False, dashed: bool = False, radius: int = 10,
            align: str = "middle", inset_top: float = 0) -> None:
        fill, stroke, ink = PALETTE[kind]
        dash = ' stroke-dasharray="6 4"' if dashed else ""
        self.parts.append(
            f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="{radius}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="1.6"{dash}/>'
        )
        if value:
            pad = 10
            lines = _wrap(value, size, w - 2 * pad)
            line_height = size * 1.28
            top = y + inset_top + (h - inset_top - line_height * len(lines)) / 2 + size * 0.92
            tx = x + w / 2 if align == "middle" else x + pad
            anchor = "middle" if align == "middle" else "start"
            for i, line in enumerate(lines):
                self.text(tx, top + i * line_height, line, size, anchor,
                          700 if bold else 400, ink)

    def group(self, x: float, y: float, w: float, h: float, label: str, kind: str = "grey") -> None:
        fill, stroke, ink = PALETTE[kind]
        self.parts.append(
            f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" rx="16" fill="{fill}" '
            f'fill-opacity="0.45" stroke="{stroke}" stroke-width="1.6" stroke-dasharray="8 5"/>'
        )
        self.text(x + 14, y + 22, label, 14, "start", 700, ink)

    def arrow(self, points: list[tuple[float, float]], label: str = "", dashed: bool = False,
              color: str = "#32505f", label_at: tuple[float, float] | None = None,
              label_anchor: str = "middle") -> None:
        path = " ".join(f"{px:g},{py:g}" for px, py in points)
        dash = ' stroke-dasharray="6 4"' if dashed else ""
        marker = "arrow-coral" if color == "#c0432f" else "arrow"
        self.parts.append(
            f'<polyline points="{path}" fill="none" stroke="{color}" stroke-width="1.8"{dash} '
            f'marker-end="url(#{marker})"/>'
        )
        if label:
            if label_at is None:
                (x1, y1), (x2, y2) = points[0], points[-1]
                label_at = ((x1 + x2) / 2, (y1 + y2) / 2 - 6)
            self.text(label_at[0], label_at[1], label, 13, label_anchor, 400, "#142231")

    def line(self, x1: float, y1: float, x2: float, y2: float, color: str = "#8a9aa3",
             dashed: bool = False, width: float = 1.4) -> None:
        dash = ' stroke-dasharray="5 4"' if dashed else ""
        self.parts.append(
            f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{color}" '
            f'stroke-width="{width:g}"{dash}/>'
        )

    def dot(self, x: float, y: float, value: str, kind: str = "navy") -> None:
        fill, stroke, ink = PALETTE[kind]
        self.parts.append(f'<circle cx="{x:g}" cy="{y:g}" r="12" fill="{fill}" stroke="{stroke}" stroke-width="1.6"/>')
        self.text(x, y + 5, value, 13, "middle", 700, ink)


    # -- compound helpers -----------------------------------------------------
    def table(self, heads: list[str], rows: list[list[str]], x: float, y: float, widths: list[float],
              row_h: float = 52, head_h: float = 38, size: int = 12, kinds: list[str] | None = None,
              first_bold: bool = True, gap: float = 6) -> float:
        """Draw a table of boxes and return the y coordinate below the last row."""
        self.table_calls += 1
        cx = x
        for width, head in zip(widths, heads):
            self.box(cx, y, width - gap, head_h, head, "navy", size + 1, bold=True)
            cx += width
        cy = y + head_h + gap
        for i, row in enumerate(rows):
            cx = x
            for j, (width, cell) in enumerate(zip(widths, row)):
                kind = (kinds[j] if kinds else "plain")
                if isinstance(kind, tuple):
                    kind = kind[i % len(kind)]
                self.box(cx, cy, width - gap, row_h, cell, kind, size, bold=(first_bold and j == 0))
                cx += width
            cy += row_h + gap
        return cy

    def hbars(self, items: list[tuple[str, float, str, str]], x: float, y: float, scale: float,
              label_w: float = 220, bar_h: float = 30, step: float = 46, size: int = 13) -> float:
        """Horizontal bars: items are (label, value, kind, value_label)."""
        cy = y
        for label, value, kind, value_label in items:
            self.text(x + label_w - 10, cy + bar_h * 0.7, label, size, "end", 700)
            width = max(value * scale, 4)
            self.box(x + label_w, cy, width, bar_h, "", kind, radius=3)
            self.text(x + label_w + width + 8, cy + bar_h * 0.7, value_label, size, "start", 700)
            cy += step
        return cy

    # -- output -------------------------------------------------------------
    def svg(self) -> str:
        defs = (
            "<defs>"
            '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="#32505f"/></marker>'
            '<marker id="arrow-coral" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
            '<path d="M0,0 L10,5 L0,10 z" fill="#c0432f"/></marker>'
            "</defs>"
        )
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.width} {self.height}" '
            f'width="{self.width}" height="{self.height}" role="img" aria-labelledby="t d" '
            f'font-family="{FONT}">'
            f'<title id="t">{escape(self.title)}</title><desc id="d">{escape(self.desc)}</desc>'
            f'{defs}<rect width="{self.width}" height="{self.height}" fill="#ffffff"/>'
            + "".join(self.parts)
            + "</svg>\n"
        )


# =============================================================================
# Chart primitives (figure redesign kit)
#
# Every function below returns a complete ``Fig`` (visible heading, legend, axes
# with units, value labels, optional note box and footer). They are deterministic,
# use no third-party code, keep text >= 13 px (footer 12 px) and raise
# ``ValueError`` when a label cannot fit, so a broken layout fails the build
# instead of shipping clipped text. See docs/FIGURE-REDESIGN-GUIDE.md.
# =============================================================================
import math  # noqa: E402
from typing import Callable, Sequence  # noqa: E402

# Fills are darker than the table palette so white and dark text keep >= 4.5:1.
FILL = {"teal": "#087f8c", "coral": "#c0432f", "gold": "#946512", "navy": "#102a43", "grey": "#6b7c86"}
LIGHT = {"teal": "#dff1ee", "coral": "#fbe4de", "gold": "#f7ebc8", "navy": "#d9e2ec", "grey": "#eef1f2"}
INK = "#142231"
GRID = "#d5dde1"
AXIS = "#5b7280"
WARN = "#5c1f14"
MARKERS = ("circle", "square", "triangle", "diamond", "cross")
MARK_KINDS = ("teal", "gold", "coral", "navy", "grey")
CHAR_W = 0.58  # average glyph width / font size used by every fit check


def fmt_es(value: float, decimals: int | None = None) -> str:
    """Spanish number format: decimal comma, plain space between thousands groups."""
    if decimals is None:
        decimals = 0 if float(value).is_integer() else (1 if abs(value) >= 10 else 2 if abs(value) >= 1 else 3)
    body = f"{abs(value):,.{decimals}f}".replace(",", " ").replace(".", ",")
    negative = value < 0 and any(ch in "123456789" for ch in body)
    return ("−" if negative else "") + body


def fmt_exact(value: float) -> str:
    """Spanish format keeping exactly the decimals the number was written with (0,025 stays 0,025)."""
    text = repr(round(float(value), 10))
    decimals = 0 if text.endswith(".0") else len(text.split(".")[1]) if "." in text else 0
    return fmt_es(value, decimals)


def text_width(value: str, size: int = 13, weight: int = 400) -> float:
    return len(value) * size * (CHAR_W + (0.04 if weight >= 700 else 0))


def nice_ticks(lo: float, hi: float, count: int = 5) -> list[float]:
    """Round, evenly spaced tick values; the last one is the first tick at or above ``hi``."""
    if hi <= lo:
        hi = lo + 1
    raw = (hi - lo) / max(count, 1)
    magnitude = 10 ** math.floor(math.log10(raw))
    step = next(m * magnitude for m in (1, 2, 2.5, 5, 10) if m * magnitude >= raw)
    value = math.floor(lo / step) * step
    ticks = []
    while True:
        ticks.append(round(value, 10))
        if value >= hi - step * 1e-9 or len(ticks) > 60:
            return ticks
        value += step


def log_ticks(lo: float, hi: float) -> list[float]:
    """Decade ticks (1, 10, 100...) covering [lo, hi]; 1-2-5 steps when the span is short."""
    if lo <= 0:
        raise ValueError("a logarithmic axis needs strictly positive values")
    first, last = math.floor(math.log10(lo)), math.ceil(math.log10(hi))
    decades = [10.0 ** e for e in range(first, last + 1)]
    if last - first <= 1:
        return [m * d for d in decades for m in (1, 2, 5) if lo * 0.999 <= m * d <= hi * 1.001] or decades
    return decades


class Scale:
    """Maps data values to pixels along one axis; ``log`` uses base 10."""

    def __init__(self, lo: float, hi: float, p0: float, p1: float, log: bool = False) -> None:
        if log and lo <= 0:
            raise ValueError("a logarithmic axis needs strictly positive values")
        self.lo, self.hi, self.p0, self.p1, self.log = lo, hi, p0, p1, log

    def __call__(self, v: float) -> float:
        if self.log:
            t = (math.log10(max(v, self.lo)) - math.log10(self.lo)) / (math.log10(self.hi) - math.log10(self.lo))
        else:
            t = (v - self.lo) / (self.hi - self.lo)
        return self.p0 + t * (self.p1 - self.p0)


def _scale_for(values: Sequence[float], log: bool, p0: float, p1: float, zero: bool = True,
               ticks: Sequence[float] | None = None) -> tuple[Scale, list[float]]:
    vmax = max(values)
    if log:
        tks = list(ticks) if ticks else log_ticks(min(v for v in values if v > 0) * 0.999, vmax)
        return Scale(tks[0], tks[-1], p0, p1, True), tks
    vmin = min(0.0, min(values)) if zero else min(values)
    tks = list(ticks) if ticks else nice_ticks(vmin, vmax)
    return Scale(tks[0], tks[-1], p0, p1), tks


def _marker(f: Fig, x: float, y: float, shape: str, color: str, r: float = 6, hollow: bool = False) -> None:
    if shape == "circle-hollow":
        shape, hollow = "circle", True
    attrs = f'fill="{"#ffffff" if hollow else color}" stroke="{color}" stroke-width="2"'
    if shape == "circle":
        f.parts.append(f'<circle cx="{x:g}" cy="{y:g}" r="{r:g}" {attrs}/>')
    elif shape == "square":
        f.parts.append(f'<rect x="{x - r:g}" y="{y - r:g}" width="{2 * r:g}" height="{2 * r:g}" {attrs}/>')
    elif shape == "triangle":
        f.parts.append(f'<polygon points="{x:g},{y - r * 1.15:g} {x + r * 1.1:g},{y + r * .9:g} {x - r * 1.1:g},{y + r * .9:g}" {attrs}/>')
    elif shape == "diamond":
        f.parts.append(f'<polygon points="{x:g},{y - r * 1.25:g} {x + r * 1.25:g},{y:g} {x:g},{y + r * 1.25:g} {x - r * 1.25:g},{y:g}" {attrs}/>')
    elif shape == "bar":
        f.parts.append(f'<rect x="{x - r:g}" y="{y - r:g}" width="{2 * r:g}" height="{2 * r:g}" rx="2" fill="{color}"/>')
    else:  # cross
        f.parts.append(f'<path d="M{x - r:g},{y - r:g} L{x + r:g},{y + r:g} M{x + r:g},{y - r:g} L{x - r:g},{y + r:g}" '
                       f'stroke="{color}" stroke-width="2.4" fill="none"/>')


def _kit_start(title: str, desc: str, width: int, legend: Sequence[tuple[str, str, str]] | None) -> tuple[Fig, float]:
    """Fig plus the y below the heading and legend. Legend items: (label, kind, marker shape)."""
    f = Fig(width, 0, title, desc)
    lines = _wrap(title, 15, width - 28)
    for i, line in enumerate(lines):
        f.text(14, 27 + i * 19, line, 15, "start", 700, INK)
    y = 20.0 + len(lines) * 19
    if legend:
        x, row = 14.0, 0
        for label, kind, marker in legend:
            need = 30 + text_width(label) + 18
            if x + need > width - 10 and x > 14:
                x, row = 14.0, row + 1
            _marker(f, x + 8, y + 12 + row * 24, marker, FILL[kind], 6)
            f.text(x + 22, y + 17 + row * 24, label, 13, "start", 400, INK)
            x += need
        y += (row + 1) * 24 + 4
    return f, y + 6


def _kit_finish(f: Fig, y: float, note: str, note_kind: str, foot: str) -> Fig:
    f.kind = "chart"
    if note:
        note_h = max(54, len(_wrap(note, 13, f.width - 40)) * 13 * 1.28 + 26)
        f.box(10, y + 6, f.width - 20, note_h, note, note_kind, 13)
        y += note_h + 14
    if foot:
        f.text(f.width / 2, y + 22, foot, 12, "middle", 400, WARN)
        y += 30
    f.height = int(y + 10)
    return f


def _rotated_text(f: Fig, x: float, y: float, value: str, size: int = 13, fill: str = AXIS) -> None:
    f.parts.append(
        f'<text x="{x:g}" y="{y:g}" font-size="{size}" text-anchor="middle" font-weight="400" fill="{fill}" '
        f'transform="rotate(-90 {x:g} {y:g})">{escape(value)}</text>'
    )


def _check_fit(label: str, available: float, size: int = 13, weight: int = 400, what: str = "") -> None:
    if text_width(label, size, weight) > available + 0.5:
        raise ValueError(f"label does not fit ({what or 'chart'}): {label!r} needs "
                         f"{text_width(label, size, weight):.0f}px of {available:.0f}px")


def _wrapped(labels: Sequence[str], width: float, max_lines: int = 3) -> tuple[list[list[str]], int]:
    wrapped = [_wrap(label, 13, width) for label in labels]
    most = max(len(w) for w in wrapped)
    if most > max_lines:
        raise ValueError(f"category label needs {most} lines (max {max_lines}): shorten it or use a horizontal chart")
    for lab, lines in zip(labels, wrapped):
        for ln in lines:
            _check_fit(ln, width + 4, what=f"category {lab!r}")
    return wrapped, most


def _draw_value_axis(f: Fig, scale: Scale, ticks: Sequence[float], *, vertical: bool, x0: float, y0: float,
                     x1: float, y1: float) -> None:
    """Axis line, ticks, light grid and tick labels. (x0,y0)-(x1,y1) is the plot rectangle."""
    for t in ticks:
        p = scale(t)
        if vertical:
            f.line(x0, p, x1, p, GRID, width=1)
            f.line(x0 - 5, p, x0, p, AXIS, width=1.4)
            f.text(x0 - 9, p + 4.5, fmt_exact(t), 13, "end", 400, INK)
        else:
            f.line(p, y0, p, y1, GRID, width=1)
            f.line(p, y1, p, y1 + 5, AXIS, width=1.4)
            f.text(p, y1 + 21, fmt_exact(t), 13, "middle", 400, INK)
    if vertical:
        f.line(x0, y0, x0, y1, AXIS, width=1.6)
    else:
        f.line(x0, y1, x1, y1, AXIS, width=1.6)


def _axis_margin(ticks: Sequence[float]) -> float:
    return max(text_width(fmt_exact(t)) for t in ticks) + 42


def _ref_lines(f: Fig, scale: Scale, lines: Sequence[tuple[float, str]], *, vertical: bool, x0: float, y0: float,
               x1: float, y1: float, left: bool = False) -> None:
    """Dashed reference lines (limit, deadline, budget) labelled at the plot edge."""
    for value, label in lines:
        p = scale(value)
        if vertical:
            f.line(x0, p, x1, p, "#c0432f", dashed=True, width=1.8)
            if left:
                f.text(x0 + 6, p - 6, label, 13, "start", 700, WARN, halo=True)
            else:
                f.text(x1 - 4, p - 6, label, 13, "end", 700, WARN, halo=True)
        else:
            f.line(p, y0, p, y1, "#c0432f", dashed=True, width=1.8)
            f.text(p + 5, y0 + 13, label, 13, "start", 700, WARN, halo=True)


def _axis_title(unit: str, log: bool) -> str:
    return f"{unit} (escala logarítmica)" if log else unit


def _row_labels(f: Fig, labels: Sequence[str], right: float, top: float, row_h: float, width: float,
                weight: int = 400) -> None:
    for i, label in enumerate(labels):
        lines = _wrap(label, 13, width)
        mid = top + row_h * i + row_h / 2
        for li, line in enumerate(lines):
            f.text(right, mid - (len(lines) - 1) * 8.5 + li * 17 + 4.5, line, 13, "end", weight, INK)


def _label_width(labels: Sequence[str], explicit: float | None, cap: float = 300, weight: int = 400) -> float:
    return explicit or min(cap, max(text_width(c, 13, weight) for c in labels) + 8)


# ---------------------------------------------------------------- grouped bars
def grouped_bars(title: str, desc: str, categories: Sequence[str], series: Sequence[tuple[str, Sequence[float], str]],
                 *, unit: str, horizontal: bool = False, log: bool = False, decimals: int | None = None,
                 value_fmt: Callable[[float], str] | None = None, ticks: Sequence[float] | None = None,
                 ref_lines: Sequence[tuple[float, str]] = (), width: int = 940, plot_h: float = 280,
                 label_w: float | None = None, note: str = "", note_kind: str = "gold", foot: str = "") -> Fig:
    """Bars of several series side by side, with value labels, axis, unit and legend.

    ``series`` is a list of ``(name, values, kind)`` (kind: teal, coral, gold, navy, grey), one
    value per category. Use ``log=True`` when values span more than ~2 decades (mean 0,03 ms next
    to a maximum of 166 ms): the axis title then says so. ``ref_lines`` are ``(value, label)``
    dashed limits. ``horizontal=True`` suits long category names.
    """
    if not 1 <= len(series) <= 5:
        raise ValueError("grouped_bars takes between 1 and 5 series")
    for name, values, _ in series:
        if len(values) != len(categories):
            raise ValueError(f"series {name!r} needs {len(categories)} values")
    vf = value_fmt or (lambda v: fmt_es(v, decimals) if decimals is not None else fmt_exact(v))
    every = [v for _, vals, _ in series for v in vals] + [v for v, _ in ref_lines]
    k = len(series)
    f, y = _kit_start(title, desc, width, [(n, kd, "bar") for n, _, kd in series] if k > 1 else None)
    probe, tks = _scale_for(every, log, 0, 1, True, ticks)
    if not horizontal:
        x0, x1 = 14 + _axis_margin(tks), width - 20
        slot = (x1 - x0) / len(categories)
        wrapped, most = _wrapped(categories, slot - 8)
        top, bottom = y + 22, y + 22 + plot_h
        scale = Scale(probe.lo, probe.hi, bottom, top, log)
        _draw_value_axis(f, scale, tks, vertical=True, x0=x0, y0=top, x1=x1, y1=bottom)
        _rotated_text(f, 20, (top + bottom) / 2, _axis_title(unit, log))
        group_w = slot * 0.8
        bar_w = (group_w - (k - 1) * 4) / k
        for i, lines in enumerate(wrapped):
            gx = x0 + slot * i + (slot - group_w) / 2
            for j, (_, values, kind) in enumerate(series):
                bx, v = gx + j * (bar_w + 4), values[i]
                h = max(bottom - scale(v), 2) if (v > 0 or log) else 2
                f.parts.append(f'<rect x="{bx:g}" y="{bottom - h:g}" width="{bar_w:g}" height="{h:g}" rx="3" fill="{FILL[kind]}"/>')
                label = vf(v)
                _check_fit(label, bar_w + 4 + (slot - group_w) / k, 13, 700, f"value over {categories[i]!r}")
                f.text(bx + bar_w / 2, bottom - h - 6, label, 13, "middle", 700, INK)
            for li, line in enumerate(lines):
                f.text(x0 + slot * i + slot / 2, bottom + 21 + li * 17, line, 13, "middle", 400, INK)
        _ref_lines(f, scale, ref_lines, vertical=True, x0=x0, y0=top, x1=x1, y1=bottom)
        return _kit_finish(f, bottom + 21 + most * 17 + 8, note, note_kind, foot)
    lw = _label_width(categories, label_w)
    x0 = 14 + lw + 10
    x1 = width - 24 - max(text_width(vf(v), 13, 700) for v in every)
    wrapped = [_wrap(c, 13, lw) for c in categories]
    row_h = max(34.0, max(len(w) for w in wrapped) * 17 + 10, k * 26 + 12)
    top, bottom = y + 4, y + 4 + row_h * len(categories)
    scale = Scale(probe.lo, probe.hi, x0, x1, log)
    _draw_value_axis(f, scale, tks, vertical=False, x0=x0, y0=top, x1=x1, y1=bottom)
    _row_labels(f, categories, 14 + lw, top, row_h, lw)
    bar_h = (row_h - 12 - (k - 1) * 3) / k
    for i in range(len(categories)):
        for j, (_, values, kind) in enumerate(series):
            by, v = top + row_h * i + 6 + j * (bar_h + 3), values[i]
            w = max(scale(v) - x0, 2) if (v > 0 or log) else 2
            f.parts.append(f'<rect x="{x0:g}" y="{by:g}" width="{w:g}" height="{bar_h:g}" rx="3" fill="{FILL[kind]}"/>')
            f.text(x0 + w + 7, by + bar_h / 2 + 4.5, vf(v), 13, "start", 700, INK)
    _ref_lines(f, scale, ref_lines, vertical=False, x0=x0, y0=top, x1=x1, y1=bottom)
    f.text((x0 + x1) / 2, bottom + 44, _axis_title(unit, log), 13, "middle", 400, AXIS)
    return _kit_finish(f, bottom + 52, note, note_kind, foot)


# ---------------------------------------------------------------- stacked bars
def stacked_bars(title: str, desc: str, categories: Sequence[str], series: Sequence[tuple[str, Sequence[float], str]],
                 *, unit: str, horizontal: bool = False, percent: bool = False, decimals: int | None = None,
                 totals: bool = True, width: int = 940, plot_h: float = 280, label_w: float | None = None,
                 note: str = "", note_kind: str = "gold", foot: str = "") -> Fig:
    """Stacked bars: each category is split into series that add up to a whole.

    ``percent=True`` normalises every bar to 100 %. Segment labels are written inside the
    segment when they fit; the total (or 100 %) is written at the end of each bar.
    """
    if not 1 <= len(series) <= 5:
        raise ValueError("stacked_bars takes between 1 and 5 series")
    n = len(categories)
    sums = [sum(vals[i] for _, vals, _ in series) for i in range(n)]
    shown = [[(v / sums[i] * 100 if percent else v) for i, v in enumerate(vals)] for _, vals, _ in series]
    ticks = [0, 25, 50, 75, 100] if percent else nice_ticks(0, max(sums))
    f, y = _kit_start(title, desc, width, [(nm, kd, "bar") for nm, _, kd in series])
    axis_unit = "% del total" if percent else unit
    seg = (lambda v: fmt_es(v, 0 if percent else decimals) + (" %" if percent else ""))
    tot = (lambda i: "100 %" if percent else fmt_es(sums[i], decimals))
    if not horizontal:
        x0, x1 = 14 + _axis_margin(ticks), width - 20
        slot = (x1 - x0) / n
        wrapped, most = _wrapped(categories, slot - 8)
        top, bottom = y + 24, y + 24 + plot_h
        scale = Scale(ticks[0], ticks[-1], bottom, top)
        _draw_value_axis(f, scale, ticks, vertical=True, x0=x0, y0=top, x1=x1, y1=bottom)
        _rotated_text(f, 20, (top + bottom) / 2, axis_unit)
        bw = slot * 0.56
        for i, lines in enumerate(wrapped):
            bx, acc = x0 + slot * i + (slot - bw) / 2, 0.0
            for j, (_, _, kind) in enumerate(series):
                v = shown[j][i]
                y_hi, y_lo = scale(acc + v), scale(acc)
                f.parts.append(f'<rect x="{bx:g}" y="{y_hi:g}" width="{bw:g}" height="{max(y_lo - y_hi, 0):g}" '
                               f'fill="{FILL[kind]}" stroke="#ffffff" stroke-width="1.5"/>')
                if y_lo - y_hi >= 16 and text_width(seg(v), 13, 700) <= bw - 6:
                    f.text(bx + bw / 2, (y_hi + y_lo) / 2 + 4.5, seg(v), 13, "middle", 700, "#ffffff")
                acc += v
            if totals:
                f.text(bx + bw / 2, scale(acc) - 7, tot(i), 13, "middle", 700, INK)
            for li, line in enumerate(lines):
                f.text(x0 + slot * i + slot / 2, bottom + 21 + li * 17, line, 13, "middle", 400, INK)
        return _kit_finish(f, bottom + 21 + most * 17 + 8, note, note_kind, foot)
    lw = _label_width(categories, label_w)
    x0 = 14 + lw + 10
    x1 = width - 24 - (text_width("100 %", 13, 700) if totals else 0)
    row_h = max(40.0, max(len(_wrap(c, 13, lw)) for c in categories) * 17 + 10)
    top, bottom = y + 4, y + 4 + row_h * n
    scale = Scale(ticks[0], ticks[-1], x0, x1)
    _draw_value_axis(f, scale, ticks, vertical=False, x0=x0, y0=top, x1=x1, y1=bottom)
    _row_labels(f, categories, 14 + lw, top, row_h, lw)
    for i in range(n):
        cy, acc = top + row_h * i, 0.0
        for j, (_, _, kind) in enumerate(series):
            v = shown[j][i]
            p0, p1 = scale(acc), scale(acc + v)
            f.parts.append(f'<rect x="{p0:g}" y="{cy + 7:g}" width="{max(p1 - p0, 0):g}" height="{row_h - 14:g}" '
                           f'fill="{FILL[kind]}" stroke="#ffffff" stroke-width="1.5"/>')
            if p1 - p0 >= text_width(seg(v), 13, 700) + 8:
                f.text((p0 + p1) / 2, cy + row_h / 2 + 4.5, seg(v), 13, "middle", 700, "#ffffff")
            acc += v
        if totals:
            f.text(scale(acc) + 7, cy + row_h / 2 + 4.5, tot(i), 13, "start", 700, INK)
    f.text((x0 + x1) / 2, bottom + 44, axis_unit, 13, "middle", 400, AXIS)
    return _kit_finish(f, bottom + 52, note, note_kind, foot)


# ---------------------------------------------------------------- lines and scatter
def _xy_chart(title, desc, series, *, connect, x_label, y_label, log_x, log_y, x_ticks, y_ticks, annotations,
              hlines, vlines, point_labels, decimals, width, plot_h, y_zero, note, note_kind, foot) -> Fig:
    if not 1 <= len(series) <= 5:
        raise ValueError("a chart takes between 1 and 5 series")
    pts = [p for _, data, _ in series for p in data]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts] + [v for v, _ in hlines]
    f, y = _kit_start(title, desc, width,
                      [(nm, kd, MARKERS[i % len(MARKERS)]) for i, (nm, _, kd) in enumerate(series)] if len(series) > 1 else None)
    yprobe, ytks = _scale_for(ys, log_y, 0, 1, y_zero and not log_y, y_ticks)
    x0, x1 = 14 + _axis_margin(ytks), width - 30
    top, bottom = y + 14, y + 14 + plot_h
    ysc = Scale(yprobe.lo, yprobe.hi, bottom, top, log_y)
    if x_ticks:
        xtks = [t for t, _ in x_ticks]
        xsc = Scale(min(xtks), max(xtks), x0 + 18, x1 - 18, log_x)
    else:
        xprobe, xtks = _scale_for(xs + [v for v, _ in vlines], log_x, 0, 1, False, None)
        xsc = Scale(xprobe.lo, xprobe.hi, x0 + 18, x1 - 18, log_x)
        x_ticks = [(t, fmt_exact(t)) for t in xtks]
    _draw_value_axis(f, ysc, ytks, vertical=True, x0=x0, y0=top, x1=x1, y1=bottom)
    for t, label in x_ticks:
        px = xsc(t)
        f.line(px, top, px, bottom, GRID, width=1)
        f.line(px, bottom, px, bottom + 5, AXIS, width=1.4)
        f.text(px, bottom + 21, label, 13, "middle", 400, INK)
    f.line(x0, bottom, x1, bottom, AXIS, width=1.6)
    _rotated_text(f, 20, (top + bottom) / 2, _axis_title(y_label, log_y))
    f.text((x0 + x1) / 2, bottom + 46, _axis_title(x_label, log_x), 13, "middle", 400, AXIS)
    _ref_lines(f, ysc, hlines, vertical=True, x0=x0, y0=top, x1=x1, y1=bottom, left=True)
    for value, label in vlines:
        p = xsc(value)
        f.line(p, top, p, bottom, "#c0432f", dashed=True, width=1.8)
        f.text(p + 5, top + 13, label, 13, "start", 700, WARN)
    for i, (_, data, kind) in enumerate(series):
        color, shape = FILL[kind], MARKERS[i % len(MARKERS)]
        if connect:
            path = " ".join(f"{xsc(p[0]):g},{ysc(p[1]):g}" for p in data)
            dash = ' stroke-dasharray="7 4"' if i % 2 else ""
            f.parts.append(f'<polyline points="{path}" fill="none" stroke="{color}" stroke-width="2.4"{dash}/>')
        for n, p in enumerate(data):
            px, py = xsc(p[0]), ysc(p[1])
            _marker(f, px, py, shape, color, 5.5)
            label = p[2] if len(p) > 2 and p[2] else None
            side = p[3] if len(p) > 3 else "t"
            if label is None and (point_labels == "all" or (point_labels == "last" and n == len(data) - 1)):
                label = fmt_es(p[1], decimals) if decimals is not None else fmt_exact(p[1])
            if label:
                dx, dy, anchor = {"t": (0, -11, "middle"), "b": (0, 24, "middle"), "r": (10, 4.5, "start"),
                                  "l": (-10, 4.5, "end")}[side]
                f.text(px + dx, py + dy, label, 13, anchor, 700, INK, halo=True)
    for ann in annotations:
        ax, ay, text = ann[:3]
        dx, dy = (ann[3], ann[4]) if len(ann) > 4 else (28, -38)
        px, py = xsc(ax), ysc(ay)
        anchor = "start" if dx >= 0 else "end"
        lines = _wrap(text, 13, 190)
        for li, line in enumerate(lines):
            f.text(px + dx, py + dy + li * 17, line, 13, anchor, 400, WARN, italic=True, halo=True)
        ex, ey = px + dx + (8 if dx < 0 else -8), py + dy - 5
        f.line(px + (ex - px) * 0.08, py + (ey - py) * 0.08, ex, ey, WARN, width=1.2)
    return _kit_finish(f, bottom + 54, note, note_kind, foot)


def line_chart(title: str, desc: str, series: Sequence[tuple[str, Sequence[tuple], str]], *, x_label: str,
               y_label: str, log_x: bool = False, log_y: bool = False,
               x_ticks: Sequence[tuple[float, str]] | None = None, y_ticks: Sequence[float] | None = None,
               annotations: Sequence[tuple] = (), hlines: Sequence[tuple[float, str]] = (),
               vlines: Sequence[tuple[float, str]] = (), point_labels: str = "all", decimals: int | None = None,
               width: int = 940, plot_h: float = 300, y_zero: bool = True, note: str = "", note_kind: str = "gold",
               foot: str = "") -> Fig:
    """Lines with markers (a different marker shape and dash per series, so colour is never the only cue).

    Points are ``(x, y)`` or ``(x, y, label, side)`` with side in t/b/l/r. ``point_labels`` is
    ``"all"``, ``"last"`` or ``"none"``. ``annotations`` are ``(x, y, text[, dx, dy])`` callouts with
    a leader line; ``hlines`` / ``vlines`` are dashed reference lines such as a deadline.
    ``log_x`` / ``log_y`` switch an axis to base 10 and say so in the axis title. ``x_ticks`` is an
    optional list of ``(value, label)`` that forces readable ticks (1, 4, 16, 64).
    """
    return _xy_chart(title, desc, series, connect=True, x_label=x_label, y_label=y_label, log_x=log_x, log_y=log_y,
                     x_ticks=x_ticks, y_ticks=y_ticks, annotations=annotations, hlines=hlines, vlines=vlines,
                     point_labels=point_labels, decimals=decimals, width=width, plot_h=plot_h, y_zero=y_zero,
                     note=note, note_kind=note_kind, foot=foot)


def scatter(title: str, desc: str, series: Sequence[tuple[str, Sequence[tuple], str]], *, x_label: str, y_label: str,
            log_x: bool = False, log_y: bool = False, x_ticks: Sequence[tuple[float, str]] | None = None,
            y_ticks: Sequence[float] | None = None, annotations: Sequence[tuple] = (),
            hlines: Sequence[tuple[float, str]] = (), vlines: Sequence[tuple[float, str]] = (),
            point_labels: str = "none", decimals: int | None = None, width: int = 940, plot_h: float = 320,
            y_zero: bool = False, note: str = "", note_kind: str = "gold", foot: str = "") -> Fig:
    """Scatter plot: one marker per observation; same arguments as ``line_chart`` but no connecting line."""
    return _xy_chart(title, desc, series, connect=False, x_label=x_label, y_label=y_label, log_x=log_x, log_y=log_y,
                     x_ticks=x_ticks, y_ticks=y_ticks, annotations=annotations, hlines=hlines, vlines=vlines,
                     point_labels=point_labels, decimals=decimals, width=width, plot_h=plot_h, y_zero=y_zero,
                     note=note, note_kind=note_kind, foot=foot)


# ---------------------------------------------------------------- heat map
def _mix(a: str, b: str, t: float) -> str:
    t = min(max(t, 0.0), 1.0)
    ca = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    cb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(p + (q - p) * t):02x}" for p, q in zip(ca, cb))


def _luminance(color: str) -> float:
    def lin(c: int) -> float:
        s = c / 255
        return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(int(color[i:i + 2], 16)) for i in (1, 3, 5))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def heatmap(title: str, desc: str, row_labels: Sequence[str], col_labels: Sequence[str],
            values: Sequence[Sequence[float | None]], *, unit: str, row_title: str = "", col_title: str = "",
            scale: str = "teal", vmin: float | None = None, vmax: float | None = None, decimals: int | None = None,
            suffix: str = "", cell_fmt: Callable[[float], str] | None = None,
            highlight: Sequence[tuple[int, int]] = (), width: int = 940, cell_h: float = 44,
            label_w: float | None = None, note: str = "", note_kind: str = "gold", foot: str = "") -> Fig:
    """Heat map with the value written in every cell (``None`` shows an em dash).

    ``scale`` is the hue (teal, coral, gold, navy); darker means larger. ``unit`` names what the
    cells hold and appears in the colour key. ``highlight`` outlines ``(row, col)`` cells.
    """
    flat = [v for row in values for v in row if v is not None]
    lo = min(flat) if vmin is None else vmin
    hi = max(flat) if vmax is None else vmax
    if hi == lo:
        hi = lo + 1
    cf = cell_fmt or (lambda v: fmt_es(v, decimals) + suffix)
    f, y = _kit_start(title, desc, width, None)
    lw = _label_width(row_labels, label_w, weight=700)
    side = 22 if row_title else 0
    x0 = 14 + side + lw + 10
    cw = (width - 20 - x0) / len(col_labels)
    heads = [_wrap(c, 13, cw - 8) for c in col_labels]
    for c, h in zip(col_labels, heads):
        if len(h) > 3:
            raise ValueError(f"column header too long for a heat map: {c!r}")
    if col_title:
        f.text(x0 + cw * len(col_labels) / 2, y + 14, col_title, 13, "middle", 400, AXIS)
        y += 22
    for j, h in enumerate(heads):
        for li, line in enumerate(h):
            f.text(x0 + cw * j + cw / 2, y + 15 + li * 17, line, 13, "middle", 700, INK)
    y += max(len(h) for h in heads) * 17 + 10
    base = LIGHT[scale]
    strong = FILL[scale]
    _row_labels(f, row_labels, 14 + side + lw, y, cell_h, lw, 700)
    for i, row_label in enumerate(row_labels):
        ry = y + i * cell_h
        for j, v in enumerate(values[i]):
            fill = "#ffffff" if v is None else _mix(base, strong, (v - lo) / (hi - lo))
            on = (i, j) in highlight
            f.parts.append(f'<rect x="{x0 + cw * j + 1.5:g}" y="{ry + 1.5:g}" width="{cw - 3:g}" height="{cell_h - 3:g}" rx="4" '
                           f'fill="{fill}" stroke="{"#102a43" if on else "#ffffff"}" stroke-width="{3 if on else 1}"/>')
            label = "—" if v is None else cf(v)
            _check_fit(label, cw - 8, 13, 700, f"heat map cell ({row_label!r}, {col_labels[j]!r})")
            ink = "#ffffff" if v is not None and _luminance(fill) < 0.22 else INK
            f.text(x0 + cw * j + cw / 2, ry + cell_h / 2 + 4.5, label, 13, "middle", 700, ink)
    if row_title:
        _rotated_text(f, 20, y + cell_h * len(row_labels) / 2, row_title)
    y += cell_h * len(row_labels) + 14
    key_w, steps = min(240.0, cw * len(col_labels) * 0.5), 8
    key_x = x0 + text_width(cf(lo)) + 8
    f.text(x0, y + 12, cf(lo), 13, "start", 400, INK)
    for s in range(steps):
        f.parts.append(f'<rect x="{key_x + key_w / steps * s:g}" y="{y:g}" width="{key_w / steps + 0.5:g}" height="14" '
                       f'fill="{_mix(base, strong, s / (steps - 1))}"/>')
    f.text(key_x + key_w + 8, y + 12, cf(hi), 13, "start", 400, INK)
    f.text(key_x + key_w + 16 + text_width(cf(hi)), y + 12, f"más oscuro = mayor ({unit})", 13, "start", 400, AXIS)
    return _kit_finish(f, y + 22, note, note_kind, foot)


# ---------------------------------------------------------------- dumbbell
def dumbbell(title: str, desc: str, rows: Sequence[tuple[str, float, float]], *, unit: str,
             names: tuple[str, str] = ("Antes", "Después"), log: bool = False, decimals: int | None = None,
             value_fmt: Callable[[float], str] | None = None, delta: Callable[[float, float], str] | None = None,
             lower_is_better: bool = True, width: int = 940, label_w: float | None = None, note: str = "",
             note_kind: str = "gold", foot: str = "") -> Fig:
    """Before/after per row: a hollow dot (before), a filled dot (after) and the line between them.

    The segment is teal when the change is an improvement and coral when it is a regression
    (``lower_is_better`` decides which direction is good); ``delta(before, after)`` may return a
    short text such as ``"×5,4"`` written at the end of the row.
    """
    vf = value_fmt or (lambda v: fmt_es(v, decimals) if decimals is not None else fmt_exact(v))
    vals = [v for _, a, b in rows for v in (a, b)]
    f, y = _kit_start(title, desc, width, [(names[0], "grey", "circle-hollow"), (names[1], "navy", "circle")])
    lw = _label_width([r for r, _, _ in rows], label_w, weight=700)
    d_w = max(text_width(delta(a, b), 13, 700) for _, a, b in rows) + 14 if delta else 0
    pad = max(text_width(vf(v), 13, 700) for v in vals) + 18
    x0, x1 = 14 + lw + 10 + pad, width - 24 - d_w - pad
    probe, tks = _scale_for(vals, log, 0, 1, not log)
    scale = Scale(probe.lo, probe.hi, x0, x1, log)
    row_h = max(40.0, 17 * max(len(_wrap(r, 13, lw)) for r, _, _ in rows) + 10)
    top, bottom = y + 4, y + 4 + row_h * len(rows)
    _draw_value_axis(f, scale, tks, vertical=False, x0=x0, y0=top, x1=x1, y1=bottom)
    _row_labels(f, [r for r, _, _ in rows], 14 + lw, top, row_h, lw, 700)
    for i, (_, a, b) in enumerate(rows):
        cy = top + row_h * i + row_h / 2
        better = (b < a) if lower_is_better else (b > a)
        pa, pb = scale(a), scale(b)
        f.line(pa, cy, pb, cy, FILL["teal"] if better else FILL["coral"], width=4)
        _marker(f, pa, cy, "circle", FILL["grey"], 7, hollow=True)
        _marker(f, pb, cy, "circle", FILL["navy"], 7)
        left_first = pa <= pb
        f.text(pa + (-12 if left_first else 12), cy + 4.5, vf(a), 13, "end" if left_first else "start", 400, INK)
        f.text(pb + (12 if left_first else -12), cy + 4.5, vf(b), 13, "start" if left_first else "end", 700, INK)
        if delta:
            f.text(width - 14, cy + 4.5, delta(a, b), 13, "end", 700, WARN)
    f.text((x0 + x1) / 2, bottom + 44, _axis_title(unit, log), 13, "middle", 400, AXIS)
    return _kit_finish(f, bottom + 52, note, note_kind, foot)


# ---------------------------------------------------------------- percentile intervals
def percentile_intervals(title: str, desc: str, rows: Sequence[tuple[str, Sequence[float]]], *, unit: str,
                         marks: Sequence[str] = ("p50", "p99", "máx"), log: bool = False,
                         decimals: int | None = None, ref_lines: Sequence[tuple[float, str]] = (),
                         width: int = 940, label_w: float | None = None, note: str = "", note_kind: str = "gold",
                         foot: str = "") -> Fig:
    """One row per configuration: a track from the smallest to the largest mark, a distinct marker per mark.

    Use it for latency (p50 / p99 / máx), ranges or any minimum-typical-maximum triple. Marks that
    land on the same pixel are merged into one label ("0,03 · p50, p99, máx"); neighbouring labels
    alternate above and below the track so they do not collide.
    """
    if len(marks) > 4:
        raise ValueError("percentile_intervals takes up to 4 marks")
    f, y = _kit_start(title, desc, width, [(m, MARK_KINDS[i], MARKERS[i + 1]) for i, m in enumerate(marks)])
    lw = _label_width([r for r, _ in rows], label_w, weight=700)
    every = [v for _, vals in rows for v in vals] + [v for v, _ in ref_lines]
    x0, x1 = 14 + lw + 30, width - 50
    probe, tks = _scale_for(every, log, 0, 1, not log)
    scale = Scale(probe.lo, probe.hi, x0, x1, log)
    row_h = max(74.0, 17 * max(len(_wrap(r, 13, lw)) for r, _ in rows) + 30)
    top, bottom = y + 4, y + 4 + row_h * len(rows)
    _draw_value_axis(f, scale, tks, vertical=False, x0=x0, y0=top, x1=x1, y1=bottom)
    _row_labels(f, [r for r, _ in rows], 14 + lw, top, row_h, lw, 700)
    for i, (_, vals) in enumerate(rows):
        cy = top + row_h * i + row_h / 2
        px = [scale(v) for v in vals]
        f.line(min(px), cy, max(px), cy, "#8a9aa3", width=5)
        groups: list[list[int]] = []
        for idx in sorted(range(len(vals)), key=lambda m: px[m]):
            if groups and abs(px[idx] - px[groups[-1][0]]) < 5:
                groups[-1].append(idx)
            else:
                groups.append([idx])
        for gi, grp in enumerate(groups):
            gx = px[grp[0]]
            for idx in grp[::-1]:
                _marker(f, gx, cy, MARKERS[idx + 1], FILL[MARK_KINDS[idx]], 7)
            text = fmt_es(vals[grp[0]], decimals) if decimals is not None else fmt_exact(vals[grp[0]])
            if len(grp) > 1:
                text += " · " + ", ".join(marks[m] for m in grp)
            half = text_width(text, 13, 700) / 2
            anchor, tx = "middle", gx
            if gx + half > width - 8:
                anchor, tx = "end", width - 8
            elif gx - half < 8:
                anchor, tx = "start", 8
            f.text(tx, cy - 16 if gi % 2 == 0 else cy + 29, text, 13, anchor, 700, INK)
    _ref_lines(f, scale, ref_lines, vertical=False, x0=x0, y0=top, x1=x1, y1=bottom)
    f.text((x0 + x1) / 2, bottom + 44, _axis_title(unit, log), 13, "middle", 400, AXIS)
    return _kit_finish(f, bottom + 52, note, note_kind, foot)


# ---------------------------------------------------------------- timeline
def timeline(title: str, desc: str, lanes: Sequence[tuple[str, Sequence[tuple]]], *, unit: str,
             events: Sequence[tuple[float, str]] = (), ref_lines: Sequence[tuple[float, str]] = (),
             t_max: float | None = None, ticks: Sequence[float] | None = None, width: int = 940,
             lane_h: float = 50, label_w: float | None = None, note: str = "", note_kind: str = "gold",
             foot: str = "") -> Fig:
    """Sequence / Gantt view: one lane per actor, segments ``(start, end, label, kind)`` along a time axis.

    ``events`` are instants drawn as a dashed vertical line across the lanes with a label on top;
    ``ref_lines`` are dashed limits (deadline, timeout). Segment labels are written inside the
    segment and must fit (ValueError otherwise): shorten them or widen the figure.
    """
    lw = _label_width([n for n, _ in lanes], label_w, 260, 700)
    f, y = _kit_start(title, desc, width, None)
    end = t_max if t_max is not None else max([s[1] for _, segs in lanes for s in segs] + [e[0] for e in events] + [r[0] for r in ref_lines])
    tks = list(ticks) if ticks else nice_ticks(0, end)
    x0, x1 = 14 + lw + 10, width - 28
    scale = Scale(tks[0], tks[-1], x0, x1)
    ev_h = 38 if events else 6
    top = y + ev_h
    bottom = top + lane_h * len(lanes)
    _draw_value_axis(f, scale, tks, vertical=False, x0=x0, y0=top, x1=x1, y1=bottom)
    _row_labels(f, [n for n, _ in lanes], 14 + lw, top, lane_h, lw, 700)
    prev_end = -1e9
    for t, label in sorted(events):
        p = scale(t)
        f.line(p, y + ev_h - 8, p, bottom, "#102a43", width=1.4, dashed=True)
        half = text_width(label, 13, 700) / 2
        start = max(p - half, prev_end + 6, 8)
        if start + 2 * half > width - 6:
            raise ValueError(f"event label overflows: {label!r}")
        f.text(start + half, y + ev_h - 14, label, 13, "middle", 700, INK)
        prev_end = start + 2 * half
    for i, (_, segs) in enumerate(lanes):
        ly = top + lane_h * i
        if i:
            f.line(14, ly, x1, ly, GRID, width=1)
        for s0, s1, label, kind in (seg[:4] for seg in segs):
            xa, xb = scale(s0), scale(s1)
            f.parts.append(f'<rect x="{xa:g}" y="{ly + 9:g}" width="{max(xb - xa, 2):g}" height="{lane_h - 18:g}" rx="4" '
                           f'fill="{FILL[kind]}" stroke="#ffffff" stroke-width="1"/>')
            if label:
                _check_fit(label, xb - xa - 8, 13, 700, f"segment {label!r}")
                f.text((xa + xb) / 2, ly + lane_h / 2 + 4.5, label, 13, "middle", 700, "#ffffff")
    _ref_lines(f, scale, ref_lines, vertical=False, x0=x0, y0=top, x1=x1, y1=bottom)
    f.text((x0 + x1) / 2, bottom + 44, unit, 13, "middle", 400, AXIS)
    return _kit_finish(f, bottom + 52, note, note_kind, foot)


# Diagrams of states and flows already exist: ``Fig.box``, ``Fig.arrow``, ``Fig.group``, ``Fig.dot`` and the
# ``flow()`` helper of scripts/figures_part40_a.py (rows of boxes joined by arrows).
