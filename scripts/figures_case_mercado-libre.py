"""Figures for the Mercado Libre success case (casos/exito/mercado-libre.md).

Numbers come from the company's annual reports (10-K for 2007 and 2022), its Q4 2024
results release and the Go project's case study, all cited in the case page. Diagrams
mark what is documented and what is inferred.
"""
from __future__ import annotations

import re

from figure_kit import Fig, _wrap, dumbbell, stacked_bars, timeline

DOC = "Fuente: informes anuales y comunicados de Mercado Libre y el caso publicado por Go, citados en la página del caso. Consulta: 16 de noviembre de 2026."
INF = "Esquema pedagógico: las cajas punteadas son inferencia del curso, no arquitectura confirmada por Mercado Libre."


def _years(fig: Fig) -> Fig:
    """The kit groups thousands with a space; a year is not a quantity, so join them again."""
    fig.parts = [re.sub(r">([12]) (\d{3})<", r">\g<1>\g<2><", p) for p in fig.parts]
    return fig


def _canvas(title: str, desc: str, width: int, height: int) -> Fig:
    f = Fig(width, height, title, desc)
    for i, line in enumerate(_wrap(title, 15, width - 28)):
        f.text(14, 27 + i * 19, line, 15, "start", 700, "#142231")
    return f


def _foot(f: Fig, y: float, note: str, foot: str, kind: str = "gold") -> Fig:
    lines = len(_wrap(note, 13, f.width - 40))
    h = max(54, lines * 13 * 1.28 + 26)
    f.box(10, y, f.width - 20, h, note, kind, 13)
    f.text(f.width / 2, y + h + 20, foot, 12, "middle", 400, "#5c1f14")
    f.height = int(y + h + 34)
    return f


def contexto() -> Fig:
    f = _canvas("Un ecosistema de seis servicios alrededor del mercado: cada uno alimenta a los demás",
                "Diagrama de contexto: compradores y vendedores se encuentran en el marketplace; Mercado Pago cobra, Mercado Envíos entrega, Mercado Ads financia la visibilidad de los vendedores, Mercado Shops da tiendas propias y los clasificados atraen tráfico; todo se integra con el crédito y la cuenta digital.",
                940, 0)
    f.group(10, 52, 250, 230, "Personas y negocios", "grey")
    f.box(30, 90, 210, 56, "Comprador en Latinoamérica", "teal", 13)
    f.box(30, 158, 210, 56, "Vendedor del marketplace (individuos, pymes y marcas)", "gold", 13)
    f.box(30, 226, 210, 44, "Desarrollador que usa las API", "plain", 13)
    f.group(300, 52, 630, 230, "Ecosistema Mercado Libre", "navy")
    f.box(320, 90, 180, 56, "Marketplace: publicar y comprar", "plain", 13, bold=True)
    f.box(520, 90, 180, 56, "Mercado Pago: cobros, billetera y crédito", "plain", 13)
    f.box(720, 90, 190, 56, "Mercado Envíos: logística y entrega", "plain", 13)
    f.box(320, 166, 180, 56, "Mercado Ads: publicidad de vendedores", "plain", 13)
    f.box(520, 166, 180, 56, "Mercado Shops: tiendas propias", "plain", 13)
    f.box(720, 166, 190, 56, "Clasificados: autos, inmuebles, servicios", "plain", 13)
    f.box(320, 234, 590, 36, "Programa de lealtad por puntos y niveles que une el marketplace y Mercado Pago", "gold", 13)
    f.arrow([(240, 118), (320, 118)])
    f.arrow([(240, 186), (320, 186)])
    f.arrow([(240, 248), (300, 248)], dashed=True)
    return _foot(f, 300, "Lo documentado: el informe anual de 2022 describe seis servicios integrados, el marketplace, Mercado Pago, Mercado Envíos, Mercado Ads, los clasificados y Mercado Shops, y un programa de lealtad de seis niveles. Las flechas resumen el uso; cómo se reparte el tráfico entre servicios no se publica.",
                 DOC)


def componentes() -> Fig:
    f = _canvas("Celdas autónomas, API abiertas y una plataforma interna que oculta la infraestructura",
                "Diagrama por capas: equipos organizados en celdas con su propio código, datos y hardware, que se comunican por API; una plataforma interna (Fury) entre los desarrolladores y los proveedores de nube; servicios en Go dentro de contenedores; y terceros que integran la plataforma mediante las mismas API.",
                940, 0)
    rows = [
        ("Terceros", "Desarrolladores externos integran el marketplace y Mercado Pago con las API públicas y construyen empresas sobre ellas", "gold"),
        ("Celdas", "Unidad funcional con su equipo, hardware, datos y código fuente; se hablan solo por API", "teal"),
        ("Servicios", "API centrales en Go sobre contenedores: de 8 a 10 millones de peticiones por minuto en una API de usuarios", "plain"),
        ("Plataforma", "Fury: plataforma como servicio propia para construir, desplegar, monitorear y gestionar servicios sin atarse a una nube", "navy"),
    ]
    y = 52.0
    for name, text, kind in rows:
        f.box(10, y, 170, 64, name, "navy" if kind != "navy" else "coral", 14, bold=True)
        f.box(192, y, 738, 64, text, kind if kind != "navy" else "grey", 13)
        y += 80
    return _foot(f, y + 6, "Lo documentado procede del informe anual de 2022 (celdas, API abiertas, plataforma como servicio propia) y del caso publicado por Go (Fury, contenedores, cifras de tráfico). El número de celdas, los nombres de los servicios y la nube concreta no se publican en esas fuentes.",
                 DOC)


def flujo() -> Fig:
    f = _canvas("Una compra de principio a fin: encontrar, pagar, enviar y cerrar",
                "Diagrama de flujo en seis pasos: el comprador encuentra y compra un producto; Mercado Pago procesa el pago; el vendedor prepara el envío; Mercado Envíos recoge y entrega, a veces desde un centro de cumplimiento; el comprador confirma la recepción; y se cierra la operación con la liquidación al vendedor.",
                940, 0)
    steps = [
        ("1. Encontrar", "El comprador busca y elige un producto del marketplace", "plain", False),
        ("2. Pagar", "Mercado Pago procesa el pago en el marketplace", "navy", False),
        ("3. Preparar", "El vendedor empaca o usa el cumplimiento de Mercado Libre", "gold", False),
        ("4. Entregar", "Mercado Envíos transporta con red propia o terceros", "gold", False),
        ("5. Recibir", "El comprador recibe y puede calificar o reclamar", "plain", True),
        ("6. Liquidar", "El dinero queda disponible para el vendedor", "teal", True),
    ]
    w, gap = 134, 22
    x = 10.0
    for i, (head, body, kind, inferred) in enumerate(steps):
        f.box(x, 66, w, 38, head, kind, 13, bold=True)
        f.box(x, 112, w, 118, body, "plain", 13, dashed=inferred)
        if i:
            f.arrow([(x - gap, 85), (x, 85)])
        x += w + gap
    f.text(14, 262, "Trazo continuo: respaldado por el informe anual. Trazo punteado: inferido.", 13, "start", 400, "#32505f")
    return _foot(f, 280, "El informe anual documenta que Mercado Pago procesa y liquida las transacciones del marketplace en la mayoría de los países y que Mercado Envíos ofrece transporte y cumplimiento. Las reglas de calificación, reclamo y el momento de liberar el dinero al vendedor se infieren: no están descritas en las fuentes consultadas.",
                 INF, "coral")


def linea() -> Fig:
    return _years(timeline(
        "De un mercado en línea en Argentina a un ecosistema de comercio y finanzas (1999-2025)",
        "Línea de tiempo con dos carriles: en negocio, la empresa nace en 1999 con lanzamientos en Argentina, Brasil, México y Uruguay, es privada hasta su salida a Nasdaq en agosto de 2007 y cotiza después; en tecnología, la pila histórica de Grails y Groovy llega hasta 2015, cuando se adopta Go, y después evolucionan las celdas y la plataforma Fury.",
        [("Negocio", [(1999, 2007, "Privada: 4 países y eBay", "grey"), (2007, 2026, "Cotizada en Nasdaq", "teal")]),
         ("Tecnología", [(1999, 2015, "Pila Grails y Groovy sobre bases relacionales", "gold"), (2015, 2026, "Go, celdas, Fury", "coral")])],
        unit="Año", events=[(1999, "Argentina"), (2003, "Mercado Pago"), (2007, "IPO"), (2015, "Giro a Go")],
        ticks=[1999, 2003, 2007, 2011, 2015, 2019, 2023, 2026], t_max=2026, lane_h=58, label_w=100,
        note="Los años salen del informe anual de 2007 (lanzamientos, eBay, Nasdaq), del de 2022 (Mercado Pago) y del caso de Go (2015). Las dos barras de tecnología son una simplificación: el informe dice «históricamente» sin fechar el inicio de la pila y el caso de Go no fecha el final. El año 2026 es el límite de la figura, no un hito.",
        note_kind="gold", foot=DOC))


def paises() -> Fig:
    return stacked_bars(
        "De dónde vienen los ingresos de Mercado Libre: 2021 y 2022 (millones de USD)",
        "Barras apiladas al cien por ciento: Brasil aporta 55 por ciento de los ingresos en 2021 y 54 por ciento en 2022, Argentina 22 y 24 por ciento, México 17 y 18 por ciento, y el resto de los países 6 y 5 por ciento; tres países suman cerca del 95 por ciento.",
        ["2021 (ingresos 7 069)", "2022 (ingresos 10 537)"],
        [("Brasil", [3910, 5666], "teal"), ("Argentina", [1531, 2500], "gold"), ("México", [1172, 1864], "navy"), ("Otros países", [456, 507], "grey")],
        unit="% de los ingresos netos", percent=True, horizontal=True, decimals=0, label_w=190,
        note="Los ingresos netos totales crecieron 49 por ciento entre 2021 y 2022 y la contribución directa pasó de 18,7 a 21,6 por ciento de los ingresos. Por país, la contribución directa de 2022 fue de 40,5 por ciento en Argentina frente a 15,3 en México. Son dólares de cada año: la inflación y el tipo de cambio afectan lo que se informa; el informe señala ambos como riesgos.",
        note_kind="gold", foot="Fuente: Mercado Libre, Form 10-K del año 2022 (resultados por segmento). Consulta: 16 de noviembre de 2026.")


def go() -> Fig:
    return dumbbell(
        "Efecto de pasar un servicio de Grails a Go (según el caso de Go)",
        "Puntos antes y después en escala logarítmica para un servicio grande: servidores de 32 a 4, núcleos por servidor de 4 a 2 y núcleos totales de 128 a 8, una reducción de 94 por ciento en capacidad de cómputo para el mismo servicio.",
        [("Servidores", 32, 4), ("Núcleos por servidor", 4, 2), ("Núcleos totales (cálculo)", 128, 8)],
        unit="Cantidad", names=("Antes (Grails)", "Después (Go)"), log=True, decimals=0, label_w=220,
        note="Los 128 y 8 núcleos son el producto de las dos cifras publicadas (32 × 4 y 4 × 2), no una medida directa; Go señala que desapareció el 88 por ciento de los servidores y que cada uno usa la mitad de CPU. Es un servicio elegido por la propia compañía de un caso publicado por el proyecto Go: puede no ser representativo y no incluye el coste de reescribir.",
        note_kind="coral", foot="Fuente: The Go Programming Language, «MercadoLibre Grows with Go», 10 de noviembre de 2019.")


FIGURES = {
    "mercado-libre-contexto.svg": contexto,
    "mercado-libre-celdas-y-plataforma.svg": componentes,
    "mercado-libre-flujo-de-una-compra.svg": flujo,
    "mercado-libre-linea-de-tiempo.svg": linea,
    "mercado-libre-ingresos-por-pais.svg": paises,
    "mercado-libre-efecto-de-go.svg": go,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
