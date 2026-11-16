"""Map figure of the success-cases page (casos/exito/README.md)."""
from __future__ import annotations

from figure_kit import Fig, _wrap, INK

NOTE = "Agrupación orientativa para elegir por dónde empezar; cada caso mezcla varias tensiones."


def _columns(title: str, desc: str, columns: list[tuple[str, str, list[str], str]], width: int = 960) -> Fig:
    n = len(columns)
    gap = 22
    col_w = (width - 20 - gap * (n - 1)) / n
    head_h, case_h, tail_h = 64, 40, 76
    max_cases = max(len(c[2]) for c in columns)
    height = int(46 + head_h + 26 + max_cases * (case_h + 8) + 34 + tail_h + 58)
    f = Fig(width, height, title, desc)
    for i, line in enumerate(_wrap(title, 15, width - 28)):
        f.text(14, 27 + i * 19, line, 15, "start", 700, INK)
    for ci, (head, kind, cases, parts) in enumerate(columns):
        x = 10 + ci * (col_w + gap)
        y = 46.0
        f.box(x, y, col_w, head_h, head, kind, 14, bold=True)
        y += head_h + 26
        f.arrow([(x + col_w / 2, y - 24), (x + col_w / 2, y - 2)])
        for name in cases:
            f.box(x + 14, y, col_w - 28, case_h, name, "plain", 14)
            y += case_h + 8
        y = 46 + head_h + 26 + max_cases * (case_h + 8) + 12
        f.arrow([(x + col_w / 2, y - 8), (x + col_w / 2, y + 18)], dashed=True)
        f.box(x, y + 22, col_w, tail_h, parts, "grey", 13)
    f.text(width / 2, height - 14, NOTE, 12, "middle", 400, "#5c1f14")
    return f


def mapa() -> Fig:
    return _columns(
        "Mapa de las plataformas exitosas: la tensión que resuelven y la teoría que la explica",
        "Diagrama de tres columnas: cada una nombra una tensión de ingeniería, enlaza con flechas a las plataformas que la ilustran y señala las partes del curso que dan las herramientas para analizarla. Escala operada como producto: Netflix, Amazon y Spotify. Mercados de dos lados: Uber, Mercado Libre y Airbnb. Interfaz y concurrencia como ventaja: Stripe y WhatsApp.",
        [
            ("Escala operada como producto", "teal", ["Netflix", "Amazon", "Spotify"],
             "Partes 28, 29, 31 y 35: sistemas distribuidos, nube, resiliencia y SRE"),
            ("Mercados de dos lados", "gold", ["Uber", "Mercado Libre", "Airbnb"],
             "Partes 10, 11, 25 y 27: producto, economía, arquitectura e integración"),
            ("Interfaz y concurrencia como ventaja", "navy", ["Stripe", "WhatsApp"],
             "Partes 13, 20, 28 y 32: contratos, backend, concurrencia y seguridad"),
        ],
    )


FIGURES = {"exito-mapa.svg": mapa}
