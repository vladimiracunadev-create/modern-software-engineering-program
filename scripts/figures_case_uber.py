"""Figures for the Uber success case (casos/exito/uber.md).

Numbers come from Uber's Q4 2024 results release and from its public engineering blog and
founding post, all cited in the case page. Diagrams mark what is documented and what is inferred.
"""
from __future__ import annotations

import re

from figure_kit import Fig, _wrap, grouped_bars, line_chart, timeline

from case_diagrams import B, G, finish, lane_steps, legend, sequence
from figure_kit import stacked_bars
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


SEC = "Fuente: Uber, Form 10-K de 2020, 2023 y 2025 (SEC). Consulta: 16 de noviembre de 2026."


def actores() -> Fig:
    f = _canvas("Quién da qué a quién: los actores del mercado de Uber",
                "Diagrama de incentivos: quien pide un viaje o un pedido paga un precio fijo por adelantado; el conductor o repartidor cobra según tiempo y distancia reales; el comercio vende por la plataforma; Uber cobra la diferencia como ingreso y soporta el riesgo de precio; las ciudades y reguladores fijan reglas; los competidores presionan precios e incentivos.",
                940, 0)
    B(f, 340, 160, 260, 96, "Uber: empareja, fija el precio, cobra, cubre el riesgo de precio y opera la plataforma", "navy", 13, bold=True)
    B(f, 10, 56, 250, 70, "Quien pide: ve un precio fijo por adelantado y paga por el servicio", "teal")
    B(f, 345, 56, 250, 70, "Conductor o repartidor: cobra por tiempo y distancia reales", "plain")
    B(f, 680, 56, 250, 70, "Comercio o restaurante: vende por la plataforma (Delivery)", "plain")
    B(f, 10, 300, 250, 70, "Empresas clientes y cargadores: movilidad y envíos (Freight)", "plain", dashed=True)
    B(f, 345, 300, 250, 80, "Ciudades y reguladores: licencias, seguros, clasificación laboral, tarifas máximas", "grey")
    B(f, 680, 300, 250, 70, "Competidores: obligan a ofrecer incentivos y bajar precios", "coral")
    f.arrow([(200, 126), (340, 190)], "precio fijo", label_at=(235, 150))
    f.arrow([(470, 126), (470, 160)], "viaje", label_at=(505, 148))
    f.arrow([(670, 126), (600, 190)], "pedido", label_at=(660, 160))
    f.arrow([(340, 236), (230, 300)], dashed=True)
    f.arrow([(470, 256), (470, 300)])
    f.arrow([(690, 300), (600, 236)], dashed=True)
    return finish(f, 390, "Documentado en el 10-K de 2025: el usuario recibe un precio fijo por adelantado mientras a quien conduce se le paga por el tiempo y la distancia reales, que Uber reconoce la diferencia, que hay regulación fragmentada de licencias, seguros y clasificación de conductores, y que los competidores recurren a incentivos. No se sabe cómo se negocia con comercios ni con empresas clientes.", DOC)


def viajes() -> Fig:
    f = _canvas("Cinco recorridos completos: de la primera interacción al caso límite",
                "Cinco filas de pasos encadenados: quien pide un viaje, quien pide comida, el conductor, el comercio y el cargador de Freight; cada fila termina en su caso límite.",
                940, 0)
    y = 54.0
    y = lane_steps(f, y, "Pasajero", [("Pide origen y destino", "plain"), ("Ve un precio fijo por adelantado", "gold"), ("Se empareja con un conductor", "teal"), ("Límite: nadie cerca o precio capado por ley", "coral")], h=64)
    y = lane_steps(f, y, "Quien pide comida", [("Elige comercio y pedido", "plain"), ("Se busca repartidor", "teal"), ("Tres partes coordinadas", "plain"), ("Límite: el comercio rechaza o el reparto se retrasa", "coral!")], h=64)
    y = lane_steps(f, y, "Conductor", [("Se conecta y recibe ofertas", "plain"), ("Acepta y recoge", "teal"), ("Cobra por tiempo y distancia", "gold"), ("Límite: clasificación laboral y salario mínimo", "coral")], h=64)
    y = lane_steps(f, y, "Comercio", [("Se registra en Delivery", "plain!"), ("Recibe pedidos", "plain"), ("Prepara y entrega al repartidor", "plain!"), ("Límite: pico de pedidos sin cocina", "coral!")], h=64)
    y = lane_steps(f, y, "Cargador (Freight)", [("Publica una carga", "plain!"), ("Se asigna un transportista", "plain!"), ("Seguimiento del envío", "plain!"), ("Límite: la línea sigue sin ganancias", "coral")], h=64)
    legend(f, y + 14, "Trazo punteado: paso inferido. Cajas coral: el caso límite de cada recorrido.")
    return finish(f, y + 28, "Los pasos continuos salen del 10-K de 2025 (precio fijo por adelantado, pago por tiempo y distancia, Prop. 22, tarifas máximas) y de los artículos de ingeniería (emparejamiento, mercado de tres lados). Los punteados son comportamiento visible o plausible, no mecanismo publicado; el resultado negativo de Freight es el dato del 10-K.", DOC)


def contenedores() -> Fig:
    f = _canvas("Nivel 2, contenedores: de las aplicaciones a la plataforma de cumplimiento y los datos",
                "Diagrama de contenedores: las aplicaciones de quien pide y de quien conduce llegan a puertas de entrada por dominio; la plataforma de cumplimiento gestiona viajes y ofertas con almacenamiento transaccional; servicios de ubicación usan una rejilla hexagonal y un anillo de nodos; Cadence orquesta procesos largos; una plataforma de datos en tiempo real alimenta decisiones.",
                940, 0)
    B(f, 10, 70, 170, 60, "App de quien pide", "teal")
    B(f, 10, 150, 170, 60, "App de quien conduce o reparte", "teal")
    G(f, 210, 52, 720, 300, "Plataforma de Uber (documentado en artículos 2016-2021; inferido donde se indica)", "navy")
    B(f, 228, 90, 200, 66, "Puertas de entrada por dominio (DOMA)", "plain")
    B(f, 446, 90, 220, 66, "Plataforma de cumplimiento: Viaje y Oferta, estados", "gold")
    B(f, 684, 90, 228, 66, "Almacén transaccional (Spanner desde 2021)", "plain")
    B(f, 228, 174, 200, 66, "Ubicación y rejilla H3; anillo de nodos con Ringpop", "plain")
    B(f, 446, 174, 220, 66, "Cadence: orquestación de procesos largos", "plain")
    B(f, 684, 174, 228, 66, "Datos en tiempo real, precios y mapas (inferido)", "plain", dashed=True)
    B(f, 228, 258, 684, 76, "Pagos, verificación de identidad, seguros y detección de fraude: existen y se rigen por reglas locales, pero las fuentes consultadas no los describen", "grey", dashed=True)
    f.arrow([(180, 100), (228, 123)])
    f.arrow([(180, 180), (228, 140)])
    f.arrow([(428, 123), (446, 123)])
    f.arrow([(666, 123), (684, 123)])
    f.arrow([(328, 156), (328, 174)])
    f.arrow([(556, 156), (556, 174)], dashed=True)
    return finish(f, 372, "Documentado: dominios con puertas de entrada (DOMA, 2020), la plataforma de cumplimiento con Viaje y Oferta sobre Spanner (2021), H3 (2018), Ringpop (2016) y Cadence (2019). Inferido: la ubicación de los datos en tiempo real, el cálculo de precios y los pagos. No se sabe el número de servicios actuales ni cómo se reparten por región.", DOC)


def sec_viaje() -> Fig:
    return sequence(
        "Nivel 4, secuencia: pedir un viaje y completarlo",
        "Diagrama de secuencia entre quien pide, la plataforma de cumplimiento, el servicio de ubicación, quien conduce y el almacén: se crea el Viaje, se buscan Ofertas cercanas con la rejilla, se ofrece el trabajo, se acepta, se cambian los estados y se cierra el viaje.",
        ["Quien pide", "Cumplimiento (demanda)", "Ubicación y oferta", "Quien conduce", "Almacén"],
        [(0, 1, "Solicita viaje con origen y destino", ""), (1, 4, "Crea la entidad Viaje", ""),
         (1, 2, "Busca ofertas cercanas (inferido)", "dashed"), (2, 3, "Ofrece el trabajo", "dashed"),
         (3, 1, "Acepta: Viaje y Oferta quedan unidos", ""), (1, 4, "Cambia estados en una transacción", ""),
         (3, 0, "Recoge y lleva a destino", "dashed"), (1, 4, "Cierra el viaje y registra el cobro", "")],
        "Documentado en el artículo de 2021: las entidades Viaje y Oferta, los estados jerárquicos y que el almacén transaccional sustituyó al modelo de mejor esfuerzo. Inferido: el orden exacto de la búsqueda y de la oferta, y el momento del cobro. Uber no publica el algoritmo de emparejamiento ni el cálculo del precio.",
        DOC, kinds=["teal", "gold", "navy", "teal", "grey"], row_h=44, first_gap=46)


def sec_consistencia() -> Fig:
    return sequence(
        "Nivel 4, secuencia: por qué el modelo de mejor esfuerzo se sobrescribía (modelo didáctico)",
        "Diagrama de secuencia didáctico de dos escrituras concurrentes sobre un mismo viaje durante una conmutación de región: dos trabajadores creen ser el dueño, ambos escriben, gana la última escritura y se pierde un cambio; el nuevo diseño transaccional rechaza la segunda.",
        ["Trabajador A (dueño antiguo)", "Almacén antiguo (último gana)", "Trabajador B (dueño nuevo)", "Almacén nuevo (transaccional)"],
        [(0, 1, "Escribe estado «aceptado»", ""), (2, 1, "Escribe estado «cancelado»", ""),
         (1, 1, "Gana la última escritura; se pierde la otra", "dashed"), (0, 3, "Escribe estado «aceptado»", ""),
         (2, 3, "Escribe estado «cancelado»", ""), (3, 3, "Una sola transacción gana; la otra se rechaza", "")],
        "Documentado: durante despliegues o conmutaciones de región podían producirse escrituras concurrentes con la regla del último que escribe, lo que obligaba a reconciliar, y el rediseño usa un almacén con transacciones. Los dos escenarios dibujados son un modelo didáctico del mecanismo, no un incidente real descrito por Uber.",
        INF, "coral", kinds=["plain", "grey", "plain", "navy"], row_h=44, first_gap=46)


def hexagonos() -> Fig:
    import math
    f = _canvas("Nivel 3, componente: la rejilla hexagonal H3 que mide oferta y demanda por celda",
                "Siete hexágonos: una celda central y sus seis vecinas, todas a la misma distancia del centro; en cada celda se cuentan solicitudes y conductores disponibles, y la comparación indica dónde hay más demanda que oferta; a la derecha, las resoluciones, cada una con celdas de un séptimo del área de la anterior.",
                940, 0)
    r = 46.0
    cx0, cy0 = 230.0, 190.0
    cells = [((0, 0), "centro", "teal"), ((1, 0), "", "plain"), ((0.5, 1), "", "plain"), ((-0.5, 1), "", "plain"), ((-1, 0), "", "plain"), ((-0.5, -1), "", "plain"), ((0.5, -1), "", "plain")]
    data = [("8 solic.\n3 cond.", "coral"), ("2 solic.\n4 cond.", "teal"), ("5 solic.\n2 cond.", "coral"), ("1 solic.\n3 cond.", "teal"), ("3 solic.\n3 cond.", "plain"), ("2 solic.\n2 cond.", "plain"), ("4 solic.\n1 cond.", "coral")]
    w = math.sqrt(3) * r
    from figure_kit import PALETTE
    for ((dx, dy), _, _), (txt, kind) in zip(cells, data):
        cx, cy = cx0 + dx * w * 1.0 + (0 if dy == 0 else 0), cy0 + dy * r * 1.5
        pts = " ".join(f"{cx + r * math.cos(math.radians(60 * i - 30)):.1f},{cy + r * math.sin(math.radians(60 * i - 30)):.1f}" for i in range(6))
        fill, stroke, ink = PALETTE[kind]
        f.parts.append(f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="1.8"/>')
        f.text(cx, cy - 2, txt.split("\n")[0], 13, "middle", 700, ink)
        f.text(cx, cy + 14, txt.split("\n")[1], 13, "middle", 700, ink)
    f.text(cx0, 345, "Ilustrativo: números inventados para mostrar el mecanismo", 13, "middle", 400, "#32505f")
    B(f, 440, 56, 490, 64, "Cada celda cuenta solicitudes y conductores disponibles; donde sobran solicitudes hay precio dinámico o se ofrece a conductores cercanos", "gold")
    B(f, 440, 130, 490, 56, "Una sola distancia del centro a sus seis vecinas simplifica el análisis y el suavizado", "plain")
    B(f, 440, 200, 490, 56, "16 resoluciones (0 a 15); cada una tiene celdas de un séptimo del área de la anterior", "plain")
    B(f, 440, 270, 490, 56, "Un vecindario es un conjunto de celdas; pertenecer a él es una consulta de conjunto", "plain")
    return finish(f, 366, "Documentado en el artículo de 2018 sobre H3: la rejilla hexagonal jerárquica, sus 16 resoluciones, el uso para precios dinámicos y despacho, y la ventaja de la distancia uniforme. Los números de las celdas son un ejemplo inventado; Uber no publica cómo calcula el precio.", DOC)


def anillo() -> Fig:
    import math
    f = _canvas("Nivel 3, componente: el anillo de Ringpop reparte claves y reenvía peticiones",
                "Diagrama de un anillo de hashing consistente con cuatro nodos: una clave cae en el arco del nodo propietario; una petición que llega a otro nodo se reenvía al dueño; si un nodo cae, solo sus claves pasan al vecino.",
                940, 0)
    cx, cy, R = 250.0, 205.0, 120.0
    f.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#8a9aa3" stroke-width="2" stroke-dasharray="6 4"/>')
    names = ["Nodo A", "Nodo B", "Nodo C", "Nodo D"]
    kinds = ["teal", "gold", "plain", "navy"]
    for i, (n, k) in enumerate(zip(names, kinds)):
        a = math.radians(-90 + 90 * i)
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        B(f, x - 42, y - 20, 84, 40, n, k, 13, bold=True)
    f.text(cx, cy - 6, "Clave «viaje 42»", 13, "middle", 700)
    f.text(cx, cy + 12, "cae en el arco de C", 13, "middle", 400)
    f.arrow([(cx + 105, cy + 18), (cx + 20, cy + 100)], "", dashed=True)
    B(f, 520, 60, 410, 62, "1. Una petición por el viaje 42 llega a cualquier nodo, por ejemplo B", "plain")
    B(f, 520, 136, 410, 62, "2. B calcula el dueño con la función de hash y reenvía la petición a C", "gold")
    B(f, 520, 212, 410, 62, "3. C procesa la petición en su turno, una a la vez para esa clave", "teal")
    B(f, 520, 288, 410, 62, "4. Si C cae, el protocolo de pertenencia lo detecta y solo sus claves pasan al vecino", "coral")
    return finish(f, 380, "Documentado en el artículo de 2016 sobre Ringpop: pertenencia con una variante del protocolo SWIM sobre TCP, hashing consistente con FarmHash y reenvío de peticiones al propietario. El artículo de 2021 añade que el diseño entre pares limitaba el tamaño de cada pod en ciudades con mucha concurrencia. El ejemplo de la clave es didáctico.", DOC)


def datos() -> Fig:
    f = _canvas("Nivel 6, datos: tres generaciones de almacenamiento y qué corrigió cada una",
                "Diagrama de tres generaciones: un monolito sobre Postgres con amplificación de escritura, replicación verbosa y actualizaciones difíciles; MySQL con Schemaless y Cassandra con la regla del último que escribe en 2014; y Spanner con transacciones y un mecanismo propio de ejecución posterior a la confirmación desde 2021.",
                940, 0)
    cols = [
        ("Monolito: Postgres", "grey", ["Escrituras amplificadas: un campo cambia varios índices", "Replicación física verbosa entre centros de datos", "Actualizar de versión exigía horas de parada"]),
        ("2014-2016: MySQL, Schemaless, Cassandra", "navy", ["Schemaless: particionado sobre MySQL", "Cassandra y Redis en cumplimiento, disponibilidad antes que consistencia", "Sin atomicidad: reconciliar fallos a mano"]),
        ("2021: Spanner", "teal", ["Consistencia fuerte y transacciones entre filas y regiones", "LATE: ejecución posterior a la confirmación, al menos una vez", "Primera base NewSQL de Uber"]),
    ]
    x = 10.0
    for head, kind, items in cols:
        B(f, x, 56, 292, 50, head, kind, 14, bold=True)
        y = 118
        for it in items:
            B(f, x, y, 292, 62, it, "plain")
            y += 72
        x += 314
    f.arrow([(302, 80), (324, 80)])
    f.arrow([(616, 80), (638, 80)])
    return finish(f, 342, "Documentado en los artículos de 2016 (Postgres a MySQL) y 2021 (plataforma de cumplimiento): los problemas de Postgres, el diseño de 2014 y el motivo del cambio a Spanner. El orden de las columnas es el orden conceptual de la historia, no una cronología exacta: Schemaless y la plataforma de 2014 coexistieron.", DOC)


def pods() -> Fig:
    f = _canvas("Nivel 5, despliegue: dos dominios de fallo, dos regiones cada uno y pods por ciudad",
                "Diagrama de despliegue: dos dominios de fallo con dos regiones independientes cada uno; dentro de cada región, pods con servicios fundamentales a los que se asignan ciudades según varios criterios; la plataforma de cumplimiento nueva corre en regiones operativas de América del Norte y usa una configuración multirregión de Spanner.",
                940, 0)
    for i, name in enumerate(["Dominio de fallo 1", "Dominio de fallo 2"]):
        x = 10 + i * 470
        G(f, x, 52, 450, 200, name, "navy")
        for j in range(2):
            gx = x + 14 + j * 218
            G(f, gx, 84, 208, 156, f"Región {i * 2 + j + 1}", "grey")
            B(f, gx + 12, 114, 90, 64, "Pod con servicios clave", "teal")
            B(f, gx + 108, 114, 90, 64, "Pod de otras ciudades", "teal")
            B(f, gx + 12, 186, 186, 46, "Ciudades a pods según criterios", "plain")
    B(f, 10, 272, 920, 56, "Cumplimiento nuevo (2021): corre en regiones operativas de América del Norte y llama a una configuración multirregión de Spanner para cada transacción", "gold")
    return finish(f, 348, "Documentado en el artículo de 2021: el diseño con dos dominios de fallo y dos regiones independientes por dominio, los pods con servicios fundamentales para reducir el radio del impacto y la asignación de ciudades a pods. No se sabe cuántos pods hay ni cómo se asignan hoy; es la foto de ese año.", DOC)


def evolucion() -> Fig:
    f = _canvas("Cómo evolucionó la arquitectura: del monolito a dominios",
                "Tres columnas: monolito en Python con Postgres en la etapa inicial; microservicios desde 2012-2013 con Schemaless, Ringpop y Cassandra; dominios, capas y puertas de entrada en 2020 con una plataforma de cumplimiento nueva sobre Spanner en 2021.",
                940, 0)
    cols = [
        ("2010-2012: monolito", "grey", ["Backend monolítico en Python con Postgres", "El problema parecía operativo, no técnico", "Lanzamiento en San Francisco, 31 de mayo de 2010"]),
        ("2012-2019: microservicios", "navy", ["Adopción de microservicios hacia 2012-2013", "Schemaless, Ringpop y Cassandra para escala y disponibilidad", "H3 (2018) y Cadence (2017, abierto)"]),
        ("2020-2021: dominios y consistencia", "teal", ["DOMA: dominios, capas, puertas y extensiones (2020)", "Unos 2 200 microservicios críticos y su complejidad", "Cumplimiento nuevo sobre Spanner (2021)"]),
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
    return finish(f, 368, "Etapas del curso sobre hechos citados (relato de 2010, artículos de ingeniería de 2016 a 2021). Las fronteras son aproximadas: Uber dice «alrededor de 2012-2013» para los microservicios y no fecha cada corte. No se sabe qué parte de lo descrito sigue vigente.", DOC)


def precio_fijo() -> Fig:
    f = _canvas("Quién soporta el riesgo del precio: precio fijo por adelantado y pago por tiempo y distancia",
                "Diagrama de dos flujos: quien pide ve un precio fijo por adelantado antes de aceptar; a quien conduce se le paga por el tiempo y la distancia reales; Uber reconoce la diferencia, positiva o negativa, y por eso soporta el riesgo cuando el viaje dura más de lo previsto.",
                940, 0)
    B(f, 10, 70, 200, 80, "Quien pide: ve y acepta un precio fijo", "teal")
    B(f, 370, 70, 200, 80, "Uber: recibe el pago y cubre la diferencia", "navy", 13, bold=True)
    B(f, 730, 70, 200, 80, "Quien conduce: cobra tiempo y distancia reales", "plain")
    f.arrow([(210, 110), (370, 110)], "precio fijo", label_at=(290, 98))
    f.arrow([(570, 110), (730, 110)], "pago real", label_at=(650, 98))
    B(f, 10, 180, 290, 72, "Si el viaje es más corto de lo previsto, Uber retiene más", "gold")
    B(f, 325, 180, 290, 72, "Si coincide, Uber retiene el margen planeado", "plain")
    B(f, 640, 180, 290, 72, "Si el viaje se alarga, Uber retiene menos o pierde", "coral")
    B(f, 10, 276, 920, 60, "Efecto de diseño: el pasajero conoce el coste antes de pedir, y el riesgo de tráfico, desvíos y demora pasa del usuario a la plataforma, que lo gestiona con su modelo de precios", "grey", dashed=True)
    return finish(f, 356, "Documentado en el 10-K de 2025: en los mercados donde Uber gana la diferencia entre lo que paga el usuario y lo que gana el conductor, el usuario recibe un precio fijo por adelantado y al conductor se le paga según el tiempo y la distancia reales. Los tres escenarios y su lectura económica son análisis propio.", DOC)


def resultado() -> Fig:
    yrs = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
    rev = [3.338, 7.402, 10.433, 13.0, 11.139, 17.455, 31.877, 37.281, 43.978, 52.017]
    opi = [-3.023, -4.080, -3.033, -8.596, -4.863, -3.834, -1.832, 1.110, 2.799, 5.565]
    return line_chart(
        "Ingresos y resultado operativo de Uber, 2016-2025 (miles de millones de USD)",
        "Dos líneas por año: los ingresos suben de 3,3 en 2016 a 52,0 en 2025, con una caída en 2020; el resultado operativo es negativo de 2016 a 2022, con el mínimo de menos 8,6 en 2019, y pasa a positivo en 2023 con 1,1, 2,8 en 2024 y 5,6 en 2025.",
        [("Ingresos", [(y, v, f"{v:.1f}".replace(".", ","), "t") for y, v in zip(yrs, rev)], "navy"),
         ("Resultado operativo", [(y, v, f"{v:.1f}".replace(".", ","), "b") for y, v in zip(yrs, opi)], "gold")],
        x_label="Año fiscal", y_label="Miles de millones de USD",
        x_ticks=[(y, str(y)) for y in yrs], y_zero=False, plot_h=320,
        note="Los ingresos de Uber se multiplicaron por más de 15 entre 2016 y 2025 y solo tuvo resultado operativo positivo desde 2023. 2020 es el año de la pandemia: los ingresos bajaron 14 por ciento porque las reservas de movilidad cayeron 46 por ciento mientras el reparto casi se duplicó. Las cifras de 2016 y 2017 proceden de los datos seleccionados del 10-K de 2020.",
        note_kind="gold", foot=SEC)


def segmentos() -> Fig:
    return stacked_bars(
        "Ingresos por línea de negocio de Uber, 2023-2025 (miles de millones de USD)",
        "Barras apiladas de los ingresos por segmento: movilidad de 19,8 a 25,1 y a 29,7; reparto de 12,2 a 13,8 y a 17,2; carga de 5,2 a 5,1 y a 5,1 miles de millones de dólares.",
        ["2023", "2024", "2025"],
        [("Movilidad", [19.832, 25.087, 29.670], "navy"), ("Reparto", [12.204, 13.750, 17.248], "teal"), ("Carga", [5.245, 5.141, 5.099], "gold")],
        unit="miles de millones de USD", horizontal=True, decimals=1, label_w=70,
        note="El resultado ajustado por segmento en 2025 fue 7 899 millones en movilidad (27 por ciento de sus ingresos), 3 572 en reparto (21 por ciento) y menos 33 en carga (cálculo propio con el 10-K). La carga es la línea que no crece ni gana. La suma de los segmentos no incluye los costes corporativos de 2 708 millones en 2025.",
        note_kind="gold", foot=SEC)


def estructura() -> Fig:
    seg = {"Movilidad": (29670, 8683, 13088, 7899), "Reparto": (17248, 7097, 6579, 3572)}
    cats = list(seg)
    direct = [round(100 * v[1] / v[0], 1) for v in seg.values()]
    other = [round(100 * v[2] / v[0], 1) for v in seg.values()]
    ebitda = [round(100 * v[3] / v[0], 1) for v in seg.values()]
    return stacked_bars(
        "Qué se queda Uber de cada dólar de ingreso en 2025: movilidad y reparto",
        "Barras apiladas al cien por ciento: en movilidad, 29 por ciento de los ingresos son costes directos de los participantes, 44 por ciento otros costes y 27 por ciento resultado ajustado del segmento; en reparto, 41, 38 y 21 por ciento.",
        cats, [("Costes directos de participantes e incentivos", direct, "navy"), ("Otros costes (seguro, pagos, soporte, tecnología, personal)", other, "grey"), ("Resultado ajustado del segmento", ebitda, "gold")],
        unit="% de los ingresos del segmento", percent=True, horizontal=True, decimals=1, label_w=90,
        note="Los costes directos son lo que se paga a quienes conducen o reparten y los incentivos a usuarios; «otros» incluye seguro de viaje, comisiones de tarjetas y bancos, soporte y tecnología, y el personal sin remuneración en acciones. Carga queda fuera: sus costes directos son 90 por ciento de sus ingresos y su resultado es levemente negativo. Cálculo propio con el 10-K de 2025.",
        note_kind="gold", foot=SEC)


def alternativas() -> Fig:
    f = _canvas("Alternativas descartadas: cuatro bifurcaciones y su coste probable (análisis propio)",
                "Cuatro filas de decisión con la opción elegida y la alternativa: del monolito a microservicios; de Postgres a MySQL con Schemaless; de Cassandra a una base transaccional; y la reorganización en dominios en lugar de seguir con servicios sueltos.",
                940, 0)
    rows = [
        ("Estructura", "Elegida: microservicios (2012-2013) y luego dominios (2020)", "teal", "Alternativa: monolito modular", "Menos complejidad operativa, pero equipos bloqueados y un único despliegue para una empresa que crecía por ciudades"),
        ("Base de datos", "Elegida: MySQL con Schemaless en lugar de Postgres (2016)", "gold", "Alternativa: seguir con Postgres y actualizar", "Se heredaban amplificación de escritura, replicación verbosa y paradas largas para actualizar"),
        ("Consistencia", "Elegida: Spanner transaccional (2021)", "navy", "Alternativa: afinar Cassandra y la reconciliación", "Más código de compensación en cada flujo y riesgo de sobrescrituras en cada conmutación"),
        ("Pricing", "Elegida: precio fijo por adelantado", "teal", "Alternativa: precio por taxímetro", "Menos riesgo para Uber, pero incertidumbre para el usuario y menor conversión posible"),
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
    return finish(f, y + 4, "Es un análisis propio, no un hecho: Uber no publica todas las alternativas que evaluó. Lo documentado es la opción elegida y los motivos declarados (Postgres, Cassandra) o implícitos. Las consecuencias de las alternativas son hipótesis razonadas con la teoría del curso.", INF, "coral")


FIGURES = {
    "uber-contexto.svg": contexto,
    "uber-dominios-y-capas.svg": componentes,
    "uber-ciclo-de-un-viaje.svg": flujo,
    "uber-linea-de-tiempo.svg": linea,
    "uber-reservas-e-ingresos.svg": reservas,
    "uber-actores-e-incentivos.svg": actores,
    "uber-recorridos-de-usuario.svg": viajes,
    "uber-contenedores.svg": contenedores,
    "uber-secuencia-pedir-un-viaje.svg": sec_viaje,
    "uber-secuencia-escrituras-concurrentes.svg": sec_consistencia,
    "uber-rejilla-h3.svg": hexagonos,
    "uber-anillo-de-ringpop.svg": anillo,
    "uber-datos-por-generaciones.svg": datos,
    "uber-despliegue-por-pods.svg": pods,
    "uber-evolucion-por-etapas.svg": evolucion,
    "uber-precio-fijo-y-riesgo.svg": precio_fijo,
    "uber-ingresos-y-resultado.svg": resultado,
    "uber-ingresos-por-segmento.svg": segmentos,
    "uber-alternativas-descartadas.svg": alternativas,
    "uber-estructura-de-ingresos-2025.svg": estructura,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
