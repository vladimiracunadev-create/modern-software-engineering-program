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

    # -- primitives ---------------------------------------------------------
    def text(self, x: float, y: float, value: str, size: int = 14, anchor: str = "middle",
             weight: int = 400, fill: str = "#142231", italic: bool = False) -> None:
        style = ' font-style="italic"' if italic else ""
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
