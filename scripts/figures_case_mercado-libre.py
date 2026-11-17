"""Figures for the Mercado Libre success case (casos/exito/mercado-libre.md).

Numbers come from the company's annual reports (10-K for 2007 and 2022), its Q4 2024
results release and the Go project's case study, all cited in the case page. Diagrams
mark what is documented and what is inferred.
"""
from __future__ import annotations

import re

from figure_kit import Fig, _wrap, dumbbell, stacked_bars, timeline

from case_diagrams import B, G, finish, lane_steps, legend, sequence
from figure_kit import grouped_bars, line_chart
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


SEC = "Fuente: Mercado Libre, Form 10-K de 2019, 2021, 2024 y 2025 (SEC). Consulta: 16 de noviembre de 2026."


def actores() -> Fig:
    f = _canvas("Quién da qué a quién: los actores del ecosistema de Mercado Libre",
                "Diagrama de incentivos: el comprador paga y recibe con protección; el vendedor paga comisiones y obtiene alcance, cobro y envío; el anunciante paga por visibilidad; quien usa servicios financieros obtiene cuenta, tarjeta o crédito; los transportistas y las tiendas de barrio prestan logística; los reguladores fijan reglas; Mercado Libre integra todo.",
                940, 0)
    B(f, 340, 160, 260, 100, "Mercado Libre: marketplace, pagos, envíos, publicidad y crédito en una plataforma", "navy", 13, bold=True)
    B(f, 10, 56, 250, 70, "Comprador: paga y recibe con protección ante incumplimientos", "teal")
    B(f, 345, 56, 250, 70, "Vendedor: paga comisiones; obtiene alcance, cobro y envío", "plain")
    B(f, 680, 56, 250, 70, "Anunciante y marcas: pagan por visibilidad en Mercado Ads", "gold")
    B(f, 10, 300, 250, 70, "Usuario fintech: billetera, tarjeta, ahorro o crédito", "teal")
    B(f, 345, 300, 250, 70, "Transportistas y tiendas de barrio (MELI Places): prestan logística", "plain")
    B(f, 680, 300, 250, 80, "Reguladores y bancos centrales: pagos, lavado de activos, competencia", "grey")
    f.arrow([(200, 126), (340, 190)], "compra", label_at=(250, 150))
    f.arrow([(470, 126), (470, 160)], "comisión", label_at=(520, 148))
    f.arrow([(690, 126), (600, 190)], "anuncios", label_at=(670, 160))
    f.arrow([(340, 240), (230, 300)], "crédito", label_at=(265, 270))
    f.arrow([(470, 260), (470, 300)])
    f.arrow([(690, 300), (600, 245)], dashed=True)
    return finish(f, 400, "Documentado en el 10-K: el modelo cobra comisiones por valor final y tarifas fijas, envíos, publicidad y servicios fintech; la logística combina centros propios con transportistas externos y comercios vecinales; hay un programa de protección al comprador; los reguladores son los bancos centrales y autoridades de competencia. No se sabe cómo se negocian las tarifas con transportistas ni con comercios.", DOC)


def viajes() -> Fig:
    f = _canvas("Cinco recorridos completos: de la primera interacción al caso límite",
                "Cinco filas de pasos encadenados: comprador, vendedor que usa los centros de cumplimiento, usuario de crédito, desarrollador externo y anunciante; cada fila termina en su caso límite.",
                940, 0)
    y = 54.0
    y = lane_steps(f, y, "Comprador", [("Busca y compara", "plain"), ("Paga con Mercado Pago", "teal"), ("Recibe por Mercado Envíos", "gold"), ("Límite: no llega o llega mal; protección", "coral")], h=64)
    y = lane_steps(f, y, "Vendedor", [("Publica y fija precio", "plain"), ("Envía su stock a un centro", "gold"), ("Se despacha y se cobra", "teal"), ("Límite: devolución o reclamo", "coral")], h=64)
    y = lane_steps(f, y, "Usuario de crédito", [("Usa la billetera", "plain"), ("Recibe una oferta de crédito", "plain!"), ("Paga en cuotas", "teal"), ("Límite: mora, con provisión de pérdidas", "coral")], h=64)
    y = lane_steps(f, y, "Desarrollador", [("Crea una aplicación", "plain"), ("Autoriza con OAuth", "plain"), ("Recibe notificaciones del pago", "teal"), ("Límite: notificación repetida o perdida", "coral!")], h=64)
    y = lane_steps(f, y, "Anunciante", [("Elige productos a promover", "plain"), ("Aparece en búsquedas y banners", "gold"), ("Paga por resultado", "plain!"), ("Límite: saturar la página de anuncios", "coral!")], h=64)
    legend(f, y + 14, "Trazo punteado: paso inferido. Cajas coral: el caso límite de cada recorrido.")
    return finish(f, y + 28, "Los pasos continuos salen del 10-K de 2025, del caso de Go y de la documentación pública de Mercado Pago (aplicaciones, preferencias, URL de retorno, notificaciones, 3DS 2.0). Los punteados son comportamiento plausible no detallado; los casos límite de mora, devolución y notificaciones repetidas son riesgos que el curso conecta con el 10-K.", DOC)


def contenedores() -> Fig:
    f = _canvas("Nivel 2, contenedores: seis servicios integrados sobre una plataforma común",
                "Diagrama de contenedores: aplicaciones y sitios por país; servicios de comercio, pagos, envíos, publicidad y crédito; celdas autónomas; la plataforma interna Fury; las nubes de AWS y Google Cloud como proveedores principales; y los sistemas externos de bancos, transportistas y reguladores.",
                940, 0)
    B(f, 10, 80, 170, 64, "Apps y sitios por país", "teal")
    B(f, 10, 164, 170, 64, "API pública y desarrolladores", "teal")
    G(f, 210, 52, 540, 296, "Plataforma Mercado Libre (documentado en 2019-2025)", "navy")
    B(f, 228, 90, 160, 60, "Marketplace", "plain", 13, bold=True)
    B(f, 402, 90, 160, 60, "Mercado Pago", "gold", 13, bold=True)
    B(f, 576, 90, 160, 60, "Mercado Envíos", "plain", 13, bold=True)
    B(f, 228, 164, 160, 60, "Mercado Ads", "plain", 13, bold=True)
    B(f, 402, 164, 160, 60, "Crédito y ahorro", "gold", 13, bold=True)
    B(f, 576, 164, 160, 60, "Celdas con equipo y datos propios", "plain")
    B(f, 228, 240, 508, 92, "Fury: plataforma interna para construir, desplegar y operar servicios, independiente de la nube; sobre ella AWS y Google Cloud, los proveedores más grandes", "grey")
    G(f, 780, 52, 150, 296, "Externos", "gold")
    B(f, 792, 90, 126, 70, "Bancos y emisores", "plain", 13)
    B(f, 792, 174, 126, 70, "Transportistas y MELI Places", "plain", 13)
    B(f, 792, 258, 126, 70, "Reguladores", "plain", 13)
    f.arrow([(180, 112), (228, 120)])
    f.arrow([(180, 196), (228, 130)])
    f.arrow([(388, 120), (402, 120)])
    f.arrow([(562, 120), (576, 120)])
    f.arrow([(736, 120), (792, 124)], dashed=True)
    f.arrow([(736, 204), (792, 208)], dashed=True)
    return finish(f, 368, "Documentado: seis servicios integrados, celdas con equipo, hardware, datos y código propios que se comunican por API, la plataforma Fury, AWS y Google Cloud como mayores proveedores de nube, la red logística con transportistas externos y la API pública con OAuth y notificaciones. Inferido: la ubicación exacta de cada servicio. No se sabe cuántas celdas ni cuántos servicios existen.", DOC)


def sec_compra() -> Fig:
    return sequence(
        "Nivel 4, secuencia: una compra de principio a fin",
        "Diagrama de secuencia entre comprador, marketplace, Mercado Pago, centro de cumplimiento y vendedor: el comprador elige, se procesa el pago, se avisa al vendedor, se prepara y despacha, se entrega y se liquida al vendedor.",
        ["Comprador", "Marketplace", "Mercado Pago", "Cumplimiento y envío", "Vendedor"],
        [(0, 1, "Elige un artículo y confirma", ""), (1, 2, "Solicita el cobro", ""),
         (2, 1, "Aprueba el pago (cuotas posibles)", ""), (1, 4, "Avisa de la venta", "dashed"),
         (1, 3, "Pide preparar y despachar", ""), (3, 0, "Entrega el paquete", ""),
         (0, 1, "Confirma o reclama (protección)", "dashed"), (2, 4, "Liquida al vendedor (inferido)", "dashed")],
        "Documentado: Mercado Pago procesa y liquida las transacciones del marketplace en varios países, admite cuotas, la logística combina centros de cumplimiento y recogida cruzada y existe un programa de protección al comprador. Inferido: el orden exacto de los avisos y el momento de la liquidación; el 10-K no lo detalla.",
        DOC, kinds=["teal", "navy", "gold", "plain", "plain"], row_h=44, first_gap=46)


def sec_pago() -> Fig:
    return sequence(
        "Nivel 4, secuencia: un cobro con Checkout Pro y notificación",
        "Diagrama de secuencia entre el sitio del comercio, el comprador, Mercado Pago y el servidor del comercio: se crea la preferencia de pago, el comprador es redirigido al formulario, paga, vuelve al sitio y Mercado Pago envía una notificación que el comercio debe consultar y procesar sin duplicar.",
        ["Sitio del comercio", "Comprador", "Mercado Pago", "Servidor del comercio"],
        [(0, 2, "Crea la preferencia de pago", ""), (2, 0, "Devuelve el enlace de pago", ""),
         (0, 1, "Redirige al formulario", ""), (1, 2, "Elige método y paga", ""),
         (2, 1, "Vuelve al sitio (URL de retorno)", ""), (2, 3, "Notificación del pago", ""),
         (3, 2, "Consulta el estado del pago (inferido)", "dashed"), (3, 3, "Procesa una sola vez (inferido)", "dashed")],
        "Documentado en la guía pública: creación de la aplicación, preferencia de pago, redirección, URL de retorno y configuración de notificaciones, con 3DS 2.0 y prevención de fraude. Inferido: la consulta del estado y la idempotencia del proceso, que son la práctica habitual y que la página consultada no detalla.",
        DOC, kinds=["plain", "teal", "gold", "plain"], row_h=44, first_gap=46)


def logistica() -> Fig:
    f = _canvas("Nivel 3, componente: la red logística, de las bodegas a la última milla",
                "Diagrama de flujo logístico: el vendedor deja inventario en centros de cumplimiento propios, que atienden más de la mitad de los envíos, o entrega los artículos vendidos en tiendas aliadas o los recoge Mercado Libre; luego una red de aviones dedicados, camiones y furgonetas operados en su mayoría por transportistas externos lleva el paquete al comprador.",
                940, 0)
    B(f, 10, 60, 210, 80, "Vendedor con inventario en un centro de cumplimiento", "gold")
    B(f, 10, 160, 210, 80, "Vendedor que entrega el artículo vendido en una tienda aliada (MELI Places) o a recogida", "plain")
    B(f, 270, 110, 200, 90, "Cross-docking: se recoge y se mete a la red logística", "plain")
    B(f, 270, 220, 200, 70, "Más de la mitad de los envíos salen de centros de cumplimiento", "gold")
    B(f, 520, 60, 190, 90, "Transporte: aviones dedicados, camiones y furgonetas (en su mayoría de terceros)", "navy", 13, bold=True)
    B(f, 520, 180, 190, 90, "Última milla a domicilio, o recogida en un MELI Place", "plain")
    B(f, 760, 110, 170, 100, "Comprador: recibe, devuelve o reclama", "teal")
    f.arrow([(220, 100), (270, 135)])
    f.arrow([(220, 200), (270, 170)])
    f.arrow([(220, 110), (270, 250)], dashed=True)
    f.arrow([(470, 155), (520, 110)])
    f.arrow([(470, 255), (520, 225)])
    f.arrow([(710, 110), (760, 140)])
    f.arrow([(710, 225), (760, 185)])
    return finish(f, 310, "Documentado en el 10-K de 2025: los centros de cumplimiento (más de la mitad de los envíos), el cross-docking con una red de miles de tiendas aliadas, que también sirven para recogida y devoluciones, y la red de transporte con aviones dedicados, camiones y miles de furgonetas, en su gran mayoría de transportistas externos. No se sabe el número de centros ni cómo se asigna cada envío.", DOC)


def despliegue() -> Fig:
    f = _canvas("Nivel 5, despliegue: tres capas, de las celdas a la nube",
                "Diagrama de despliegue por capas: las celdas autónomas de comercio, pagos y envíos corren sobre la plataforma Fury, que es independiente de la nube; esa plataforma usa proveedores de nube, de los que AWS y Google Cloud son los mayores; los países se sirven con un marketplace separado por país y una plataforma tecnológica común.",
                940, 0)
    B(f, 10, 56, 920, 60, "Capa de producto: marketplaces por país (Argentina, Brasil, México y otros), pagos en 8 países y logística; una plataforma tecnológica común", "plain")
    B(f, 10, 130, 920, 60, "Capa de equipos: celdas con su equipo, hardware, datos y código, que se hablan por API", "teal")
    B(f, 10, 204, 920, 60, "Capa de plataforma: Fury, para construir, desplegar, monitorear y gestionar servicios sin depender de una nube concreta", "gold")
    B(f, 10, 278, 450, 60, "Nube pública: AWS y Google Cloud, los proveedores mayores", "navy", 13, bold=True)
    B(f, 480, 278, 450, 60, "Otros centros de datos: el reparto actual no se publica", "grey", dashed=True)
    f.arrow([(470, 116), (470, 130)])
    f.arrow([(470, 190), (470, 204)])
    f.arrow([(235, 264), (235, 278)])
    f.arrow([(705, 264), (705, 278)], dashed=True)
    return finish(f, 358, "Documentado: marketplace en 18 países y Mercado Pago en 8 (10-K de 2025), celdas con recursos propios y plataforma independiente de la nube (informe de 2022 y caso de Go), y AWS y Google Cloud como mayores proveedores (10-K de 2025). No se sabe cuántas regiones ni centros de datos se usan, ni cómo se reparte el tráfico.", DOC)


def evolucion() -> Fig:
    f = _canvas("Cómo evolucionó el negocio y la arquitectura: tres etapas",
                "Tres columnas: de 1999 a 2007 un marketplace por país con plataforma común y pagos con custodia en 2003; de 2008 a 2019 una plataforma abierta, Go desde 2015 y envíos propios; de 2020 en adelante un ecosistema con aviones, crédito, banca y más de veinte mil empleados de tecnología.",
                940, 0)
    cols = [
        ("1999-2007: marketplace por país", "grey", ["Una plataforma tecnológica y un marketplace separado por país", "Mercado Pago nace como custodia en 2003", "Alianza con eBay en 2001 y bolsa en 2007"]),
        ("2008-2019: plataforma abierta", "navy", ["Groovy y Grails alcanzan su límite; migración a Go desde 2015", "Celdas, API abiertas y Fury", "Mercado Envíos y crédito crecen sobre el marketplace"]),
        ("2020 en adelante: ecosistema", "teal", ["Meli Air en 2020; red de tiendas aliadas", "Crédito como línea mayor; solicitud de licencia bancaria en Argentina (2025)", "20 347 empleados de tecnología en 2025"]),
    ]
    x = 10.0
    for head, kind, items in cols:
        B(f, x, 56, 292, 44, head, kind, 14, bold=True)
        y = 112
        for it in items:
            B(f, x, y, 292, 70, it, "plain")
            y += 82
        x += 314
    f.arrow([(302, 78), (324, 78)])
    f.arrow([(616, 78), (638, 78)])
    return finish(f, 368, "Periodización del curso sobre hechos de los 10-K de 2007, 2019, 2022 y 2025 y del caso de Go. Las fronteras son aproximadas: la migración a Go empezó en 2015 y convivió con la pila anterior. No se sabe qué parte de cada etapa se rehízo por completo ni cuándo se introdujeron las celdas.", DOC)


def alternativas() -> Fig:
    f = _canvas("Alternativas descartadas: cuatro bifurcaciones y su coste probable (análisis propio)",
                "Cuatro filas de decisión con la opción elegida y la alternativa: celdas frente a un sistema monolítico; logística propia frente a transportistas puros; Go frente a seguir con Groovy y Grails; y crédito propio frente a socios financieros.",
                940, 0)
    rows = [
        ("Estructura", "Elegida: celdas con equipo, datos y código propios", "teal", "Alternativa: un monolito compartido por todos los equipos", "Despliegues lentos y acoplados entre países y productos; menos autonomía por equipo"),
        ("Logística", "Elegida: red propia con centros, aviones y terceros", "gold", "Alternativa: depender solo de transportistas externos", "Menos capital, pero menos control de plazos y de la experiencia de entrega"),
        ("Lenguaje", "Elegida: Go para servicios con mucho tráfico (2015)", "navy", "Alternativa: afinar Groovy y Grails", "Construcciones, pruebas y despliegues lentos; más servidores para el mismo tráfico"),
        ("Crédito", "Elegida: crédito propio con fondeo mixto", "teal", "Alternativa: derivar el crédito a bancos aliados", "Menos riesgo propio y menos ingreso; sin datos de pago aprovechados"),
    ]
    y = 56.0
    for name, a, ka, b, cost in rows:
        B(f, 10, y, 110, 96, name, "navy", 13, bold=True)
        B(f, 134, y, 262, 96, a, ka)
        B(f, 412, y, 250, 96, b, "grey", dashed=True)
        B(f, 678, y, 252, 96, cost, "coral", dashed=True)
        f.arrow([(396, y + 48), (412, y + 48)])
        f.arrow([(662, y + 48), (678, y + 48)], dashed=True)
        y += 108
    return finish(f, y + 4, "Es un análisis propio, no un hecho: la empresa no publica las alternativas que evaluó. Lo documentado son las opciones elegidas (celdas, red logística propia, Go, crédito propio) y los motivos que da el informe; los costes de las alternativas son hipótesis razonadas con la teoría del curso.", INF, "coral")


def ingresos() -> Fig:
    pts_r = [(2017, 1.217, "1,2", "t"), (2018, 1.440, "1,4", "t"), (2019, 2.296, "2,3", "t"), (2020, 3.974, "4,0", "t"), (2021, 7.069, "7,1", "t"),
             (2022, 10.780, "10,8", "t"), (2023, 15.107, "15,1", "t"), (2024, 20.777, "20,8", "t"), (2025, 28.893, "28,9", "t")]
    pts_o = [(2019, -0.153, "-0,2", "b"), (2020, 0.128, "0,1", "b"), (2021, 0.441, "0,4", "b"), (2022, 1.069, "1,1", "b"), (2023, 2.207, "2,2", "b"), (2024, 2.631, "2,6", "b"), (2025, 3.201, "3,2", "b")]
    return line_chart(
        "Ingresos y resultado operativo de Mercado Libre, 2017-2025 (miles de millones de USD)",
        "Dos líneas: los ingresos suben de 1,2 miles de millones en 2017 a 28,9 en 2025, con aceleración desde 2020; el resultado operativo pasa de menos 0,15 en 2019 a 3,2 en 2025.",
        [("Ingresos netos y financieros", pts_r, "navy"), ("Resultado operativo", pts_o, "gold")],
        x_label="Año fiscal", y_label="Miles de millones de USD", x_ticks=[(y, str(y)) for y in range(2017, 2026)], y_zero=False, plot_h=300,
        note="El resultado operativo creció de 0,4 a 3,2 miles de millones entre 2021 y 2025. El margen operativo subió de 6,2 por ciento en 2021 a 14,6 en 2023 y bajó a 12,7 en 2024 y 11,1 en 2025 (cálculo propio): desde 2023 el resultado crece menos que los ingresos, a la vez que pesan más la provisión de crédito y el marketing. Las cifras de 2022 y 2023 están recompuestas en el 10-K de 2024 por un cambio de presentación.",
        note_kind="gold", foot=SEC)


def lineas() -> Fig:
    return stacked_bars(
        "De qué viven los ingresos: comercio y fintech por línea (2024 y 2025, miles de millones de USD)",
        "Barras apiladas de ingresos por línea: en 2024, servicios de comercio 10,1, venta de producto 2,1, servicios financieros 5,0 y crédito 3,6; en 2025, servicios de comercio 12,8, venta de producto 3,5, servicios financieros 6,7 y crédito 5,9.",
        ["2024 (20,8 en total)", "2025 (28,9 en total)"],
        [("Servicios de comercio", [10.076, 12.750], "navy"), ("Venta de producto", [2.083, 3.544], "grey"), ("Servicios financieros", [4.962, 6.678], "teal"), ("Crédito", [3.600, 5.858], "gold")],
        unit="miles de millones de USD", horizontal=True, decimals=1, label_w=130,
        note="Fintech (servicios financieros más crédito, más 0,06 de productos) pasó de 8,6 a 12,6 miles de millones y es 44 por ciento de los ingresos de 2025 (cálculo propio); el crédito creció 63 por ciento en el año. Los ingresos de comercio incluyen comisiones, envíos netos de costes de transportistas, publicidad y venta propia; el 10-K no separa la publicidad en este cuadro.",
        note_kind="gold", foot=SEC)


def pagos_vs_ventas() -> Fig:
    yrs = [2015, 2016, 2017, 2018, 2019, 2023, 2024, 2025]
    gmv = [7.151, 8.048, 11.749, 12.505, 13.997, 44.749, 51.467, 65.037]
    tpv = [5.184, 7.754, 13.732, 18.456, 28.390, 146.738, 196.660, 277.823]
    return line_chart(
        "Los pagos crecen más que las ventas: GMV y volumen de pagos (miles de millones de USD)",
        "Dos líneas en escala logarítmica: el valor vendido en el marketplace sube de 7,2 en 2015 a 65,0 en 2025 y el volumen de pagos de 5,2 a 277,8; desde 2017 el volumen de pagos supera al valor vendido.",
        [("Valor vendido en el marketplace (GMV)", [(y, v, f"{v:.1f}".replace(".", ","), "t" if y <= 2016 else "b") for y, v in zip(yrs, gmv)], "navy"),
         ("Volumen total de pagos (TPV)", [(y, v, f"{v:.0f}".replace(".", ","), "b" if y <= 2016 else "t") for y, v in zip(yrs, tpv)], "gold")],
        x_label="Año fiscal (no se grafican 2020 a 2022)", y_label="Miles de millones de USD", log_y=True, x_ticks=[(y, str(y)) for y in yrs],
        plot_h=300, y_zero=False,
        note="El volumen de pagos incluye cobros fuera del marketplace (puntos de venta, QR, billetera), por eso supera al valor vendido; en 2025 es 4,3 veces el GMV (277,8 frente a 65,0, cálculo propio) y en 2015 era 0,7 veces. Los años 2020 a 2022 no se grafican porque no están en los 10-K citados; unir puntos no es una tasa de crecimiento.",
        note_kind="gold", foot=SEC)


def credito() -> Fig:
    return grouped_bars(
        "El crédito crece y su riesgo también: ingresos por crédito y provisión por incobrables (miles de millones de USD)",
        "Barras agrupadas de 2023, 2024 y 2025: ingresos por crédito de 2,5, 3,6 y 5,9 miles de millones y provisión para cuentas dudosas de 1,1, 1,9 y 3,1; el margen de interés neto tras pérdidas bajó de 36,2 a 28,2 y a 22,4 por ciento.",
        ["2023", "2024", "2025"],
        [("Ingresos por crédito", [2.546, 3.600, 5.858], "teal"), ("Provisión para cuentas dudosas", [1.050, 1.858, 3.091], "coral")],
        unit="miles de millones de USD", decimals=1, plot_h=260,
        note="La provisión pasó de 41 a 53 por ciento de los ingresos por crédito entre 2023 y 2025 (cálculo propio) y el indicador NIMAL de la empresa cayó de 36,2 a 28,2 y a 22,4 por ciento. Crecer en crédito exige reservar más contra pérdidas. Los ingresos de crédito de 2023 son los recompuestos en el 10-K de 2025.",
        note_kind="gold", foot=SEC)


def moneda() -> Fig:
    return grouped_bars(
        "Moneda e inflación: tres países concentran 96 por ciento de los ingresos (2025)",
        "Barras agrupadas por país: porcentaje de los ingresos denominado en moneda local de 52,6 en Brasil, 22,4 en México y 20,6 en Argentina; e inflación de 2025 de 4,3, 3,7 y 31,5 por ciento.",
        ["Brasil", "México", "Argentina"],
        [("Ingresos en moneda local (%)", [52.6, 22.4, 20.6], "navy"), ("Inflación de 2025 (%)", [4.3, 3.7, 31.5], "coral")],
        unit="por ciento", decimals=1, plot_h=250,
        note="Brasil, Argentina y México sumaron 95,6 por ciento de los ingresos de 2025. Argentina es el país con 31,5 por ciento de inflación y desde 2018 se clasifica como altamente inflacionario, por lo que su subsidiaria reporta en dólares. La barra de Argentina muestra por qué comparar ingresos en dólares entre años engaña.",
        note_kind="gold", foot=SEC)


def negocio() -> Fig:
    f = _canvas("Esquema del negocio: cuatro corrientes de ingreso y de qué viven",
                "Diagrama de flujos: compradores y vendedores generan comisiones y envíos; los anunciantes pagan por visibilidad; los usuarios financieros generan comisiones por pagos, intereses de crédito y venta de terminales; Mercado Libre paga logística, fondeo, pérdidas de crédito, marketing y tecnología y retiene el resultado operativo, de 3 201 millones en 2025.",
                940, 0)
    B(f, 10, 56, 220, 64, "Compradores y vendedores: comisiones y envíos", "teal")
    B(f, 10, 130, 220, 64, "Anunciantes: publicidad en el marketplace", "gold")
    B(f, 10, 204, 220, 64, "Usuarios fintech: pagos, tarjetas y cuotas", "teal")
    B(f, 10, 278, 220, 64, "Quien toma crédito: intereses", "gold")
    B(f, 330, 120, 270, 110, "Mercado Libre: 28 893 millones de ingresos netos y financieros en 2025", "navy", 13, bold=True)
    B(f, 700, 56, 230, 56, "Costo de ingresos: 55,5 % (envíos, fondeo, bienes)", "plain")
    B(f, 700, 122, 230, 56, "Provisión por incobrables: 10,7 %", "coral")
    B(f, 700, 188, 230, 56, "Marketing, tecnología y administración: 22,7 %", "plain")
    B(f, 700, 254, 230, 56, "Resultado operativo: 11,1 %", "gold")
    for y in (88, 162, 236, 310):
        f.arrow([(230, y), (330, 175)])
    for y in (84, 150, 216, 282):
        f.arrow([(600, 175), (700, y)])
    return finish(f, 364, "Porcentajes de 2025 calculados con el 10-K: costo de ingresos y gastos financieros 16 035 millones (55,5 %), provisión para cuentas dudosas 3 091 (10,7 %), marketing 3 219, desarrollo 2 269 y administración 1 078 (22,7 % en conjunto) y resultado operativo 3 201 (11,1 %). Las dos cajas de ingresos de abajo son la línea fintech; el 10-K no asigna costes por corriente.", SEC)


def costos() -> Fig:
    names = ["2023", "2024", "2025"]
    rev = [15107, 20777, 28893]
    cost = [15107 - 5383 - 2207, 11200, 16035]
    parts = [("Costo de ingresos y gastos financieros", cost, "navy"), ("Provisión para cuentas dudosas", [1050, 1858, 3091], "coral"),
             ("Marketing", [1736, 2191, 3219], "grey"), ("Desarrollo, tecnología y administración", [1831 + 766, 1934 + 963, 2269 + 1078], "teal"), ("Resultado operativo", [2207, 2631, 3201], "gold")]
    series = [(n, [round(100 * v / r, 1) for v, r in zip(vals, rev)], k) for n, vals, k in parts]
    return stacked_bars(
        "Costos operativos de Mercado Libre por rubro, 2023-2025 (porcentaje de los ingresos)",
        "Barras apiladas al cien por ciento: el costo de ingresos sube de 49,8 a 53,9 y a 55,5 por ciento de los ingresos; la provisión por incobrables de 7,0 a 8,9 y a 10,7; el marketing de 11,5 a 10,5 y a 11,1; y el resultado operativo baja de 14,6 a 12,7 y a 11,1 por ciento.",
        names, series, unit="% de los ingresos", percent=True, horizontal=True, decimals=1, label_w=70,
        note="El costo de 2023 se obtiene por diferencia (ingresos menos gastos operativos menos resultado operativo, cálculo propio); los de 2024 y 2025 son del 10-K. El costo de ingresos incluye envíos y bodegas, transportistas, costo de bienes vendidos, comisiones de cobro, impuestos, fondeo del negocio fintech, prevención de fraude y alojamiento. La provisión crece más rápido que los ingresos por el peso del crédito.",
        note_kind="gold", foot=SEC)


def plantilla() -> Fig:
    return grouped_bars(
        "Plantilla de tecnología y producto de Mercado Libre al cierre de cada año (personas)",
        "Barras de empleados de tecnología y desarrollo de producto: 9 471 al cierre de 2021, 13 856 al de 2022, 18 282 al de 2024 y 20 347 al de 2025.",
        ["2021", "2022", "2024", "2025"],
        [("Empleados de tecnología y producto", [9471, 13856, 18282, 20347], "navy")],
        unit="personas", decimals=0, plot_h=240,
        note="Crece 2,1 veces entre 2021 y 2025 (cálculo propio) mientras los ingresos crecen 4,1 veces (7 069 a 28 893 millones). El 10-K de 2025 no publica la plantilla total ni por país; solo la de tecnología y producto. No se grafica 2023 porque el cierre de ese año no está en los documentos usados.",
        note_kind="gold", foot=SEC)


def pila() -> Fig:
    f = _canvas("Hardware y software documentados de Mercado Libre, por capa",
                "Diagrama de capas: la aplicación con servicios en Go y la pila anterior de Groovy y Grails; la plataforma interna Fury con plantillas, imágenes de contenedor y canalizaciones; la nube con AWS y Google Cloud; el hardware de logística y de cobro, con aviones, camiones, furgonetas y terminales de pago; y los servidores, no publicados.",
                940, 0)
    rows = [
        ("Lenguajes y servicios", "Go en servicios con mucho tráfico desde 2015; Groovy y Grails antes; Go atiende aproximadamente la mitad del tráfico", "plain"),
        ("Plataforma interna", "Fury: plantillas de servicios en Go, repositorios iniciales de GitHub, imágenes de Docker y canalizaciones de despliegue", "gold"),
        ("Nube", "AWS y Google Cloud, los proveedores mayores; plataforma independiente de la nube", "plain"),
        ("Hardware de negocio", "Aviones dedicados, camiones y furgonetas (mayoría de terceros); terminales de cobro que se venden", "plain"),
        ("Servidores y red", "No se sabe: tipo de servidores, regiones, redes y bases de datos no se publican", "grey!"),
    ]
    y = 56.0
    for name, text, k in rows:
        B(f, 10, y, 190, 62, name, "navy", 13, bold=True)
        B(f, 212, y, 718, 62, text, k.rstrip("!"), 13, dashed=k.endswith("!"))
        y += 74
    return finish(f, y, "Documentado en el caso de Go (2019), el informe de 2022 y el 10-K de 2025. Los lenguajes son los de los servicios citados, no un inventario completo. No se sabe qué bases de datos, colas ni orquestadores usan los servicios; Docker y GitHub se citan por las plantillas de Fury.", DOC)


def fallos() -> Fig:
    f = _canvas("Qué pasa cuando cae cada componente de Mercado Libre: de lo pequeño a lo grande",
                "Seis filas de falla creciente: una API lenta, un servicio de una celda, un pico estacional, una moneda que se deprecia, la nube de un proveedor y un competidor o regulador; efecto y mecanismo con rótulo de documentado, inferido o no se sabe.",
                940, 0)
    rows = [
        ("Una API lenta", "Tiempos límite y reintentos con idempotencia (inferido); el 10-K no detalla", "plain!"),
        ("Un servicio de una celda", "La celda tiene su equipo, datos y código; el fallo se contiene en ella (documentado)", "teal"),
        ("Un pico estacional", "Campañas y «dobles fechas» suavizan la demanda; la capacidad se dimensiona: no se sabe", "gold"),
        ("Una moneda que se deprecia", "Ingresos en varias monedas; Argentina reporta en dólares (documentado)", "gold"),
        ("Un proveedor de nube", "Plataforma independiente de la nube; el 10-K declara dependencia de AWS y Google Cloud", "gold"),
        ("Un competidor o un regulador", "Revisión de competencia en México cerrada sin medidas; licencia bancaria en revisión", "coral"),
    ]
    y = 56.0
    for a, b, k in rows:
        B(f, 10, y, 280, 52, a, "navy", 13, bold=True)
        B(f, 330, y, 600, 52, b, k.rstrip("!"), 13, dashed=k.endswith("!"))
        f.arrow([(290, y + 26), (330, y + 26)])
        y += 62
    return finish(f, y + 4, "Documentado en el informe de 2022 (celdas), el caso de Go (Fury) y el 10-K de 2025 (temporadas, monedas, nube, competencia y licencia). Inferido: reintentos e idempotencia. No se publica un plan de continuidad ni objetivos de disponibilidad.", DOC)


FIGURES = {
    "mercado-libre-contexto.svg": contexto,
    "mercado-libre-celdas-y-plataforma.svg": componentes,
    "mercado-libre-flujo-de-una-compra.svg": flujo,
    "mercado-libre-linea-de-tiempo.svg": linea,
    "mercado-libre-ingresos-por-pais.svg": paises,
    "mercado-libre-efecto-de-go.svg": go,
    "mercado-libre-actores-e-incentivos.svg": actores,
    "mercado-libre-recorridos-de-usuario.svg": viajes,
    "mercado-libre-contenedores.svg": contenedores,
    "mercado-libre-secuencia-de-una-compra.svg": sec_compra,
    "mercado-libre-secuencia-de-un-cobro.svg": sec_pago,
    "mercado-libre-red-logistica.svg": logistica,
    "mercado-libre-despliegue-por-capas.svg": despliegue,
    "mercado-libre-evolucion-por-etapas.svg": evolucion,
    "mercado-libre-alternativas-descartadas.svg": alternativas,
    "mercado-libre-ingresos-y-resultado.svg": ingresos,
    "mercado-libre-ingresos-por-linea.svg": lineas,
    "mercado-libre-pagos-frente-a-ventas.svg": pagos_vs_ventas,
    "mercado-libre-credito-y-provisiones.svg": credito,
    "mercado-libre-moneda-e-inflacion.svg": moneda,
    "mercado-libre-esquema-del-negocio.svg": negocio,
    "mercado-libre-costos-operativos.svg": costos,
    "mercado-libre-plantilla-de-tecnologia.svg": plantilla,
    "mercado-libre-hardware-y-software.svg": pila,
    "mercado-libre-que-pasa-si-cae.svg": fallos,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
