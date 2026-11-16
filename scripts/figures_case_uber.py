"""Figures for the Uber success case (casos/exito/uber.md).

Numbers come from Uber's Q4 2024 results release and from its public engineering blog and
founding post, all cited in the case page. Diagrams mark what is documented and what is inferred.
"""
from __future__ import annotations

import re

from figure_kit import Fig, _wrap, grouped_bars, timeline

DOC = "Fuente: documentos públicos de Uber citados en la página del caso. Consulta: 16 de noviembre de 2026."
INF = "Esquema pedagógico: las cajas punteadas son inferencia del curso, no arquitectura confirmada por Uber."


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
    f = _canvas("Un mercado de tres lados: quien pide, quien presta el servicio y la plataforma que los casa",
                "Diagrama de contexto: la persona usuaria pide un viaje, un pedido o un envío desde la aplicación; la plataforma de Uber casa esa demanda con la oferta (conductores, repartidores, comercios), calcula el precio y cobra; los conductores y repartidores reciben ingresos; en torno hay mapas, medios de pago y reguladores locales.",
                940, 0)
    f.group(10, 52, 270, 210, "Demanda", "grey")
    f.box(30, 90, 230, 60, "Persona que pide un viaje, un pedido o un envío", "teal", 13)
    f.box(30, 166, 230, 70, "Empresa que usa Uber for Business o Uber Direct (inferido)", "plain", 13, dashed=True)
    f.group(330, 52, 280, 210, "Plataforma Uber", "navy")
    f.box(350, 90, 240, 60, "Casar demanda y oferta, fijar precio y seguir el viaje", "plain", 13)
    f.box(350, 166, 240, 70, "Cobro, comisión y pago a quien presta el servicio", "plain", 13)
    f.group(660, 52, 270, 210, "Oferta", "grey")
    f.box(680, 90, 230, 60, "Conductor o repartidor que decide qué aceptar", "gold", 13)
    f.box(680, 166, 230, 70, "Restaurante o comercio del que sale el pedido", "plain", 13)
    f.arrow([(260, 120), (350, 120)])
    f.arrow([(590, 120), (680, 120)])
    f.arrow([(590, 200), (680, 200)], dashed=True)
    f.text(305, 106, "pide", 13, "middle", 700, "#142231", halo=True)
    f.text(635, 106, "oferta", 13, "middle", 700, "#142231", halo=True)
    return _foot(f, 280, "Lo documentado: Uber conecta a quien consume con quien presta el servicio en movilidad y reparto, y el informe de resultados separa Mobility y Delivery. Que la empresa y el comercio sean actores distintos del mismo mercado de tres lados se ve en la descripción pública del reparto; los flujos de pago internos no se publican.",
                 DOC)


def componentes() -> Fig:
    f = _canvas("DOMA: dominios, capas y puertas de entrada para domar la complejidad de miles de microservicios",
                "Diagrama por capas del modelo DOMA: en la capa superior las experiencias concretas afectan a pocos servicios, en la inferior el negocio general (cuentas, viajes) afecta a muchos; cada dominio es un conjunto de microservicios con una puerta de entrada; las flechas solo bajan: una capa no depende de la de arriba.",
                940, 0)
    f.group(10, 52, 920, 100, "Capa alta: experiencias concretas (afectan a pocos servicios)", "teal")
    f.box(30, 90, 270, 50, "Función de la app móvil para quien pide", "plain", 13)
    f.box(320, 90, 270, 50, "Función de la app para quien conduce", "plain", 13)
    f.box(610, 90, 300, 50, "Cada dominio expone una puerta de entrada", "gold", 13, bold=True)
    f.group(10, 172, 920, 100, "Capa media: dominios compartidos entre productos", "gold")
    f.box(30, 210, 270, 50, "Dominio con su puerta de entrada", "plain", 13)
    f.box(320, 210, 270, 50, "Dominio con su puerta de entrada", "plain", 13)
    f.box(610, 210, 300, 50, "Puntos de extensión para la lógica de otro equipo", "coral", 13)
    f.group(10, 292, 920, 100, "Capa baja: negocio general (afecta a muchos servicios)", "navy")
    f.box(30, 330, 270, 50, "Gestión de cuentas", "plain", 13)
    f.box(320, 330, 270, 50, "Viajes del mercado", "plain", 13)
    f.box(610, 330, 300, 50, "Una falla aquí tiene el mayor radio de impacto", "grey", 13)
    f.arrow([(520, 140), (520, 172)])
    f.arrow([(520, 260), (520, 292)])
    return _foot(f, 410, "El artículo de 2020 define dominios (colecciones de microservicios), capas (qué puede depender de qué), puertas de entrada (un único punto de entrada por dominio) y extensiones para lógica de otro equipo, y dice que hacia arriba los dominios afectan a menos servicios. Los nombres de los dominios intermedios y su número no se publican en esa fuente; la figura los deja genéricos.",
                 DOC)


def flujo() -> Fig:
    f = _canvas("De «quiero ir al aeropuerto» a «viaje terminado»: el ciclo de un viaje",
                "Diagrama de flujo en seis pasos: la solicitud crea una entidad Viaje; la plataforma ofrece el viaje a oferta cercana, localizada con una malla de hexágonos; el conductor acepta; el viaje cambia de estado según un diagrama de estados jerárquico; se completa y se cobra, y los eventos alimentan a otros sistemas.",
                940, 0)
    steps = [
        ("1. Solicitud", "La persona indica origen y destino y ve un precio", "plain", False),
        ("2. Entidad Viaje", "La plataforma crea un Viaje con al menos dos puntos de paso", "navy", False),
        ("3. Oferta", "Se busca oferta cercana con índice espacial en hexágonos", "gold", True),
        ("4. Aceptación", "Una entidad Oferta (el conductor) acepta o rechaza", "navy", False),
        ("5. Estados", "El viaje avanza por estados del diagrama jerárquico", "navy", False),
        ("6. Cierre", "Se cobra y se emiten eventos para otros servicios", "teal", True),
    ]
    w, gap = 134, 22
    x = 10.0
    for i, (head, body, kind, inferred) in enumerate(steps):
        f.box(x, 66, w, 38, head, kind, 13, bold=True)
        f.box(x, 112, w, 118, body, "plain", 13, dashed=inferred)
        if i:
            f.arrow([(x - gap, 85), (x, 85)])
        x += w + gap
    f.text(14, 262, "Trazo continuo: respaldado por las fuentes. Trazo punteado: inferido de ellas.", 13, "start", 400, "#32505f")
    return _foot(f, 280, "Está documentado que la plataforma modela Viaje y Oferta como entidades, que el ciclo de vida se representa con diagramas de estados y que H3 se usa para precios y despacho. El algoritmo de emparejamiento, el cálculo del precio y el proceso de cobro no se publican: los pasos 3 y 6 describen la idea, no el sistema.",
                 INF, "coral")


def linea() -> Fig:
    return _years(timeline(
        "Del prototipo de 2009 a una empresa cotizada con 171 millones de consumidores al mes",
        "Línea de tiempo con dos carriles: en negocio, el prototipo va de 2009 a mayo de 2010, la empresa es privada hasta la salida a bolsa de mayo de 2019 y cotiza después; en arquitectura, el monolito inicial en Python da paso a microservicios hacia 2012-2013 y desde 2018 se organizan por dominios. Hitos: lanzamiento en San Francisco el 31 de mayo de 2010, plataforma de cumplimiento de 2014 y salida a bolsa en 2019.",
        [("Negocio", [(2009, 2010, "", "grey"), (2010, 2019, "Empresa privada en hipercrecimiento", "teal"), (2019, 2026, "Cotizada (NYSE)", "navy")]),
         ("Arquitectura", [(2010, 2013, "Monolito Python", "gold"), (2013, 2018, "Microservicios", "coral"), (2018, 2026, "Dominios (DOMA)", "grey")])],
        unit="Año", events=[(2010, "Lanzamiento SF"), (2014, "Fulfillment v1"), (2019, "IPO")],
        ticks=[2009, 2012, 2015, 2018, 2021, 2024, 2026], t_max=2026, lane_h=58, label_w=120,
        note="Las fronteras del carril de arquitectura son aproximadas: Uber dice que adoptó microservicios «alrededor de 2012-2013», que la arquitectura de fulfillment es de 2014 y que DOMA se formalizó en 2020 con trabajo previo; no publica fechas exactas de corte. La barra corta gris de 2009 es el prototipo, anterior al lanzamiento.",
        note_kind="gold", foot=DOC))


def reservas() -> Fig:
    return grouped_bars(
        "Reservas brutas e ingresos de Uber, 2023 y 2024 (miles de millones de USD)",
        "Barras agrupadas: las reservas brutas pasan de 137,9 a 162,8 miles de millones de dólares y los ingresos de 37,3 a 44,0 entre 2023 y 2024; los ingresos equivalen a algo más de una cuarta parte de las reservas, de modo que la plataforma retiene una parte pequeña del dinero que mueve.",
        ["Reservas brutas (Gross Bookings)", "Ingresos (Revenue)"],
        [("2023", [137.865, 37.281], "grey"), ("2024", [162.773, 43.978], "teal")],
        unit="Miles de millones de USD", decimals=1, ticks=[0, 50, 100, 150, 200],
        note="Los ingresos son 27,0 % de las reservas brutas en 2024 y 27,0 % en 2023 (cálculo propio sobre las dos cifras): lo que mueve la plataforma es mucho mayor que lo que reconoce como ingreso, porque una parte va a quien presta el servicio. «Reservas brutas» es una métrica propia de Uber, no un ingreso contable.",
        note_kind="gold", foot="Fuente: Uber, «Uber Announces Results for Fourth Quarter and Full Year 2024», 5 de febrero de 2025.")


FIGURES = {
    "uber-contexto.svg": contexto,
    "uber-dominios-y-capas.svg": componentes,
    "uber-ciclo-de-un-viaje.svg": flujo,
    "uber-linea-de-tiempo.svg": linea,
    "uber-reservas-e-ingresos.svg": reservas,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
