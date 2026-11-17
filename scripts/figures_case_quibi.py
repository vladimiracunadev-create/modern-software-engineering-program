"""Figures for the failure case study casos/fallo/quibi.md.

Only public facts are used: Deadline (21 Oct 2020), Variety (2018 and 2020), TechCrunch (2019 and 2020), The Verge (2020),
NBC News (2020). Quibi's internal data are not public and are not inferred.
"""
from __future__ import annotations

from case_fig_helpers import hub, kanban, layer_stack
from figure_kit import Fig, _kit_finish, _kit_start, _wrap, grouped_bars, line_chart, stacked_bars, timeline

FUENTE = "Fuente: prensa especializada citada en el caso; esquema propio."


def sketch(title: str, desc: str, width: int = 940):
    """Start a mechanism diagram with a visible title; returns the figure and the first free y."""
    return _kit_start(title, desc, width, None)


def bx(f: Fig, x: float, y: float, w: float, h: float, text: str, kind: str = "plain", size: int = 13,
       bold: bool = False, dashed: bool = False) -> None:
    """Box that refuses to overflow: the text must fit its rectangle."""
    lines = _wrap(text, size, w - 20)
    assert len(lines) * size * 1.28 <= h - 6, f"box overflows: {text!r} ({len(lines)} lines in {h}px)"
    f.box(x, y, w, h, text, kind, size, bold=bold, dashed=dashed)


def done(f: Fig, y: float, note: str, kind: str = "gold", foot: str = FUENTE) -> Fig:
    _kit_finish(f, y, note, kind, foot)
    f.kind = "diagram"
    return f


# ------------------------------------------------------------------ 1. premisa frente a abril de 2020
def premisa_y_realidad() -> Fig:
    f, y = sketch("La apuesta de Quibi y el mundo en que llegó",
                  "Dos columnas. A la izquierda, la premisa: la gente en movimiento, entre las siete de la mañana y las siete de la noche, quiere episodios de diez minutos o menos de calidad de cine en el teléfono, por suscripción. A la derecha, abril de 2020: confinamiento, personas en casa con televisor y varios servicios nuevos de streaming compitiendo, además de aplicaciones de video corto gratuitas.")
    bx(f, 10, y + 6, 440, 40, "Premisa (2018-2019)", "navy", 14, True)
    bx(f, 490, y + 6, 440, 40, "Abril de 2020", "navy", 14, True)
    izq = ("Uso previsto: en movimiento, de 7 de la mañana a 7 de la noche", "Episodios de 10 minutos o menos, con talento reconocido", "Solo teléfono: sin aplicaciones para televisor en el lanzamiento", "Suscripción: 4,99 USD con anuncios o 7,99 USD sin anuncios")
    der = ("Confinamiento: la audiencia en movimiento estaba en casa", "El televisor, a un paso y con otros servicios nuevos que competían", "Disney+, HBO Max y Peacock con catálogos que ya tenían público", "TikTok, Instagram y YouTube ofrecen video corto sin pagar")
    for i, (a, b) in enumerate(zip(izq, der)):
        yy = y + 62 + i * 76
        bx(f, 10, yy, 440, 60, a, "teal")
        bx(f, 490, yy, 440, 60, b, "coral")
        f.arrow([(450, yy + 30), (490, yy + 30)], dashed=True, color="#c0432f")
    return done(f, y + 62 + 4 * 76 + 2, "Documentado: la premisa según Whitman y Katzenberg y el contexto de abril de 2020 según la prensa citada. Lo que la prensa y los propios directivos no pueden afirmar es cuánto de la distancia entre premisa y realidad se debió a la pandemia: Katzenberg reconoció que atribuirlo todo a la pandemia no era justo.", "gold")


# ------------------------------------------------------------------ 2. el producto
def producto() -> Fig:
    f, y = sketch("Qué ofrecía Quibi y por dónde llegaba al espectador",
                  "Diagrama del producto. Estudios y creadores producen series, películas y programas de menos de diez minutos que se entregan por la aplicación móvil. Dentro de la aplicación, Turnstyle cambia entre vertical y horizontal al girar el teléfono y una función propia permite capturas de pantalla. Dos planes, con anuncios y sin ellos. Al inicio solo teléfonos; AirPlay y Chromecast llegaron en junio y las aplicaciones de Apple TV, Fire TV y Android TV el 20 de octubre de 2020.")
    bx(f, 10, y + 6, 300, 80, "Estudios y creadores: series, documentales y programas de bocados rápidos", "plain")
    bx(f, 360, y + 6, 330, 80, "App móvil de Quibi: episodios de 10 minutos o menos", "navy", 13, True)
    bx(f, 740, y + 6, 190, 80, "Teléfono del espectador", "plain")
    f.arrow([(310, y + 46), (360, y + 46)])
    f.arrow([(690, y + 46), (740, y + 46)])
    bx(f, 10, y + 118, 290, 76, "Turnstyle: cambia entre vertical y horizontal al girar el teléfono", "teal")
    bx(f, 325, y + 118, 290, 76, "Capturas de pantalla con un método propio por las restricciones de DRM", "teal")
    bx(f, 640, y + 118, 290, 76, "Plan con anuncios o sin anuncios; 90 días gratis al inicio", "teal")
    f.arrow([(525, y + 86), (525, y + 118)], dashed=True)
    f.group(10, y + 222, 920, 118, "Llegada a la pantalla grande", "grey")
    bx(f, 24, y + 256, 284, 70, "Abril de 2020: solo teléfono", "coral")
    bx(f, 328, y + 256, 284, 70, "Junio: AirPlay y Chromecast", "gold")
    bx(f, 632, y + 256, 284, 70, "20 oct: apps de Apple TV, Fire TV y Android TV", "teal")
    f.arrow([(308, y + 291), (328, y + 291)])
    f.arrow([(612, y + 291), (632, y + 291)])
    return done(f, y + 358, "Turnstyle fue objeto de una disputa de patentes y secretos industriales con Eko; Quibi calificó las demandas de infundadas. El caso no toma partido: lo que importa para el curso es que una función diferencial no sustituyó a la distribución en televisores.", "gold")


# ------------------------------------------------------------------ 3. línea de tiempo en meses
def linea_de_tiempo() -> Fig:
    return timeline(
        "Veintinueve meses entre el anuncio y la venta del catálogo",
        "Línea de tiempo en meses desde agosto de 2018. El anuncio de 1.000 millones de dólares es el mes 0. El lanzamiento del 6 de abril de 2020 es el mes 20. El 21 de octubre de 2020 se anuncia el cierre, el 1 de diciembre la aplicación deja de funcionar y el 8 de enero de 2021 Roku adquiere los derechos de más de 75 programas.",
        [
            ("Preparación", [(0, 20.17, "desde el anuncio hasta el lanzamiento (20 meses)", "navy")]),
            ("Servicio en operación", [(20.17, 28.0, "abr a dic de 2020", "teal")]),
            ("Tras el cierre", [(26.67, 29.23, "venta", "grey")]),
        ],
        unit="meses desde agosto de 2018 (12 = agosto de 2019, 24 = agosto de 2020)",
        events=[(0, "ago 2018: 1.000 M$"), (20.17, "6 abr 2020: lanzamiento"), (26.67, "21 oct: cierre")],
        t_max=32, ticks=[0, 4, 8, 12, 16, 20, 24, 28, 32], lane_h=50, label_w=170,
        note="El servicio funcionó unos ocho meses, del 6 de abril al 1 de diciembre de 2020. En octubre de 2019, antes de lanzar, ya tenía vendido el inventario publicitario de su primer año, unos 150 millones de dólares según TechCrunch. Los meses son cálculo propio a partir de las fechas de prensa.",
        foot="Fuentes: Variety (2018), TechCrunch (2019), Deadline y Variety (2020), The Verge (2021).")


# ------------------------------------------------------------------ 4. dinero
def dinero() -> Fig:
    return grouped_bars(
        "El dinero de Quibi en cuatro cifras publicadas",
        "Barras horizontales en millones de dólares. Capital recaudado, unos 1.750; gasto que la empresa esperaba haber acumulado hacia el tercer trimestre de 2020, unos 1.000; efectivo restante en el anuncio del cierre, unos 350; precio de los derechos que compró Roku, menos de 100.",
        ["Capital recaudado", "Gasto esperado al tercer trimestre de 2020", "Efectivo restante al anunciar el cierre", "Roku por los derechos (tope)"],
        [("Millones de dólares", [1750, 1000, 350, 100], "navy")],
        unit="millones de dólares (aproximados)", horizontal=True, label_w=300,
        note="La última barra es un tope, no un precio: las fuentes dicen que Roku pagó menos de 100 millones. La cifra de gasto es una expectativa informada por prensa en junio de 2020, no un resultado contable. El efectivo remanente se devolvió a inversionistas.",
        foot="Fuentes: NBC News y Variety (2020), Deadline (21 oct 2020), The Verge (2021). Cifras aproximadas y redondeadas.")


# ------------------------------------------------------------------ 5. audiencia
def audiencia() -> Fig:
    return grouped_bars(
        "Audiencia de Quibi: las cifras de terceros y su escala frente a Disney+",
        "Barras horizontales. Instalaciones del primer día, unas 4.000.000 de Disney+ y unas 300.000 de Quibi según Sensor Tower. Hogares suscriptores de Quibi según Kantar, 1.100.000 en el segundo trimestre de 2020 y 710.000 en el tercero.",
        ["Disney+, instalaciones del primer día", "Quibi, instalaciones del primer día", "Quibi, hogares suscriptores, 2.º trim. 2020", "Quibi, hogares suscriptores, 3.er trim. 2020"],
        [("Personas u hogares", [4000000, 300000, 1100000, 710000], "navy")],
        unit="instalaciones u hogares (aproximados)", horizontal=True, label_w=330,
        note="Las dos primeras barras son instalaciones y las dos últimas, hogares suscriptores estimados por Kantar: son medidas distintas y no se comparan entre sí. A julio de 2020 Quibi no había publicado su número de suscriptores de pago; discutió la estimación de Sensor Tower y dio una cifra de 5,6 millones de descargas.",
        foot="Fuentes: TechCrunch y The Verge (2020), Variety (2020, estimación de Kantar). Cifras aproximadas de terceros.")


# ------------------------------------------------------------------ 6. aprender antes de escalar
def aprender_antes_de_escalar() -> Fig:
    f, y = sketch("Una forma de aprender antes de gastar todo (análisis propio)",
                  "Dos recorridos. Arriba, el recorrido seguido: financiar, producir una gran cartera de contenido, lanzar a gran escala y medir después. Abajo, un recorrido alternativo con pasos de aprendizaje: probar el supuesto de uso en movimiento con una cohorte, medir conversión tras la prueba gratuita, medir uso en televisor y ampliar solo si el dato lo respalda.")
    f.text(14, y + 18, "Recorrido seguido (según la prensa)", 14, "start", 700, "#5c1f14")
    for i, t in enumerate(("Financiar 1.750 M$ y producir un catálogo grande", "Lanzar a gran escala con mucha atención", "Medir la audiencia y la conversión", "Ajustar durante el verano: pruebas, precios, marketing")):
        x = 10 + i * 232
        bx(f, x, y + 30, 212, 72, t, "coral" if i < 2 else "gold")
        if i:
            f.arrow([(x - 20, y + 66), (x, y + 66)])
    f.text(14, y + 140, "Recorrido alternativo (propuesta de análisis, no un hecho)", 14, "start", 700, "#0b3f45")
    for i, t in enumerate(("Declarar el supuesto: uso en movimiento", "Probar con una cohorte y medir conversión", "Medir el uso en televisor y el abandono", "Ampliar solo si cada medición se cumple")):
        x = 10 + i * 232
        bx(f, x, y + 152, 212, 72, t, "teal")
        if i:
            f.arrow([(x - 20, y + 188), (x, y + 188)])
    return done(f, y + 240, "El recorrido seguido es el que describen Whitman y Katzenberg y la prensa: decidieron lanzar con atención masiva por considerar que creaban una categoría. El alternativo es una propuesta de este programa para estudiar la decisión; no sabemos si habría funcionado ni si los inversionistas lo habrían aceptado.", "gold")





# ==== EXPANDED FIGURES (begin) ====

# ------------------------------------------------------------------ 6. cuadrante de mercado
def cuadrante_de_mercado() -> Fig:
    f, y = sketch("Cuadrante de mercado: Quibi apostó por el único hueco donde el espectador tenía que pagar por lo corto",
                  "Cuadrante con dos ejes. Horizontal: contenido largo a la izquierda y corto a la derecha. Vertical: gratuito arriba y de pago abajo. Arriba a la derecha, vídeo corto gratuito como TikTok, YouTube e Instagram. Abajo a la izquierda, servicios de pago de formato largo como Netflix, Disney+, HBO Max y Peacock. Abajo a la derecha, Quibi con producciones premium. A la derecha, Go90 de Verizon, cerrado en 2018, de vídeo corto con anuncios.")
    f.box(60, y + 10, 420, 150, "", "plain")
    f.box(480, y + 10, 420, 150, "", "plain")
    f.box(60, y + 160, 420, 150, "", "plain")
    f.box(480, y + 160, 420, 150, "", "coral")
    f.text(270, y + 34, "Gratuito y largo", 13, "middle", 700, "#5b7280")
    f.text(690, y + 34, "Gratuito y corto", 13, "middle", 700, "#5b7280")
    f.text(270, y + 184, "De pago y largo", 13, "middle", 700, "#5b7280")
    f.text(690, y + 184, "De pago y corto", 13, "middle", 700, "#5c1f14")
    bx(f, 80, y + 52, 380, 88, "Televisión abierta y vídeo bajo demanda con anuncios (fuera del caso)", "grey", 13, dashed=True)
    bx(f, 500, y + 52, 190, 88, "TikTok, YouTube, Instagram y Snapchat", "teal", 13)
    bx(f, 710, y + 52, 170, 88, "Go90 de Verizon: cerrado en 2018", "gold", 13)
    bx(f, 80, y + 202, 380, 88, "Netflix, Disney+, HBO Max y Peacock: catálogos largos y marcas conocidas", "plain", 13)
    bx(f, 500, y + 202, 380, 88, "Quibi: episodios de diez minutos o menos, producciones con talento, solo teléfono al inicio", "coral", 13, bold=True)
    f.text(60, y + 328, "contenido largo", 13, "start", 400, "#5b7280")
    f.text(900, y + 328, "contenido corto", 13, "end", 400, "#5b7280")
    return done(f, y + 340, "El cuadrante inferior derecho obliga a pagar por lo que el superior derecho ofrece sin costo. Go90 es el antecedente que Variety recordó en 2018. Mapa cualitativo, no una medición de cuota de mercado.",
                foot="Fuente: Variety (2018 y 2020), The Verge (2020) y NBC News (2020); esquema propio.")


# ------------------------------------------------------------------ 7. lienzo del producto
def lienzo_del_producto() -> Fig:
    f, y = sketch("Lienzo del producto con datos públicos: tres supuestos sostenían los nueve bloques",
                  "Lienzo de modelo de negocio de nueve bloques resumido con datos públicos: segmentos, propuesta de valor, canales, relación, ingresos, recursos, actividades, costos y socios. Tres supuestos, uso en movimiento, solo teléfono y pago por contenido premium breve, aparecen marcados como los que el caso examina.")
    w, g = 296, 16
    blocks = [
        (0, 0, "Segmentos: espectador en movimiento, anunciantes, creadores", "plain"),
        (1, 0, "Propuesta: episodios de diez minutos o menos con talento reconocido", "teal"),
        (2, 0, "Canales: tiendas de aplicaciones; luego AirPlay, Chromecast y televisor", "gold"),
        (0, 1, "Relación: suscripción de dos planes y publicidad", "plain"),
        (1, 1, "Ingresos: 4,99 con anuncios; 7,99 sin ellos; publicidad", "plain"),
        (2, 1, "Socios: estudios inversores, operador móvil y anunciantes", "plain"),
        (0, 2, "Recursos: producciones, talento y la función Turnstyle", "plain"),
        (1, 2, "Actividades: producción, marketing y desarrollo de la aplicación", "plain"),
        (2, 2, "Costos: contenido (hasta 6 millones por hora) y marketing", "plain"),
    ]
    for c, r, t, k in blocks:
        bx(f, 10 + c * (w + g), y + 8 + r * 96, w, 80, t, k, 13)
    f.group(10, y + 310, 920, 120, "Los tres supuestos que sostenían el modelo (el caso los examina)", "grey")
    for i, t in enumerate(["1 El uso en movimiento es frecuente y valioso", "2 Basta el teléfono, sin televisor", "3 Se paga por contenido premium breve frente a lo gratuito"]):
        bx(f, 26 + i * 300, y + 344, 280, 66, t, "coral", 13)
    return done(f, y + 450, "Reconstrucción de este programa a partir de la prensa: Quibi no publicó su lienzo y no se infieren cifras internas. Las tres cajas coral eran verificables con experimentos baratos antes de comprometer el gasto.",
                foot="Fuente: Variety, TechCrunch, Deadline y The Verge (2018 a 2021); esquema propio.")


# ------------------------------------------------------------------ 8. embudo con datos
def embudo_con_datos() -> Fig:
    f, y = sketch("El embudo con las cifras públicas: una estimación de terceros y una objeción sin cifra",
                  "A la izquierda, embudo de la cohorte inicial según Sensor Tower: unos 910.000 registros en los primeros días de abril de 2020 y unos 72.000 usuarios de pago tras los tres meses de prueba, cerca del 8 por ciento. A la derecha, la posición de Quibi: el número de suscriptores de pago de esa estimación es incorrecto en un orden de magnitud, sin publicar su propia cifra.")
    f.group(10, y, 560, 280, "Estimación de Sensor Tower (julio de 2020)", "grey")
    f.parts.append(f'<polygon points="40,{y + 50} 540,{y + 50} 440,{y + 130} 140,{y + 130}" fill="#dff1ee" stroke="#087f8c" stroke-width="1.6"/>')
    f.text(290, y + 96, "unos 910.000 registros en los primeros días", 13, "middle", 700, "#0b3f45")
    f.parts.append(f'<polygon points="140,{y + 150} 440,{y + 150} 380,{y + 230} 200,{y + 230}" fill="#fbe4de" stroke="#c0432f" stroke-width="1.6"/>')
    f.text(290, y + 196, "unos 72.000 de pago tras 90 días", 13, "middle", 700, "#5c1f14")
    f.text(290, y + 258, "conversión estimada: cerca del 8 %", 13, "middle", 700, "#0b3f45")
    f.group(590, y, 340, 280, "Posición de Quibi", "grey")
    bx(f, 606, y + 44, 308, 88, "El número de suscriptores de pago es incorrecto en un orden de magnitud", "gold", 13)
    bx(f, 606, y + 150, 308, 88, "Cifra propia de suscriptores de pago: no publicada", "plain", 13, dashed=True, bold=True)
    f.arrow([(570, y + 190), (606, y + 190)], dashed=True)
    return done(f, y + 300, "Las dos columnas no se pueden comparar: una tiene números y la otra, una objeción. Disney+ convirtió, según la misma fuente, un 11 % de unos 9,5 millones de registros iniciales. La estimación cubre solo los primeros días de abril.",
                foot="Fuente: The Verge (8 jul 2020), con datos de Sensor Tower; esquema propio.")


# ------------------------------------------------------------------ 9. descargas según cada fuente
def descargas_segun_cada_fuente() -> Fig:
    return line_chart(
        "Descargas acumuladas según cada fuente: la discrepancia crece con el tiempo",
        "Dos líneas por días desde el lanzamiento. Sensor Tower: 0,3 millones el primer día, 2,6 el primer mes y 4,5 en julio. Quibi: 0,6 millones de usuarios nuevos la primera semana, 3,5 de descargas el primer mes y más de 5,6 en julio.",
        [("Sensor Tower", [(1, 0.3, "0,3", "b"), (30, 2.6, "2,6", "b"), (93, 4.5, "4,5", "b")], "navy"),
         ("Quibi", [(7, 0.6, "0,6", "t"), (30, 3.5, "3,5", "t"), (93, 5.6, "5,6", "t")], "coral")],
        x_label="días desde el 6 de abril de 2020", y_label="millones", x_ticks=[(0, "0"), (30, "30"), (60, "60"), (93, "93")], y_ticks=[0, 2, 4, 6],
        decimals=1, point_labels="all",
        note="Los puntos son hitos informados por cada fuente, no una serie continua. El de la primera semana de Quibi son usuarios nuevos y el de Sensor Tower, descargas del primer día; no son la misma medida. A los 93 días Quibi dice más de 5,6 millones y Sensor Tower estima 4,5.",
        foot="Fuentes: TechCrunch (7 abr 2020), Deadline (21 oct 2020), NBC News (22 oct 2020) y The Verge (8 jul 2020).")


# ------------------------------------------------------------------ 10. recorrido y cobro
def recorrido_y_cobro() -> Fig:
    return timeline(
        "El dato que decidía el negocio llegó cuando ya había pasado más de un tercio de la vida del servicio",
        "Línea de tiempo en días desde el 6 de abril de 2020. La cohorte de lanzamiento tiene una prueba gratuita de 90 días hasta el 5 de julio, día 90. Las altas de mayo y junio tienen pruebas de 14 días. El primer cobro posible es el día 90 y el cierre del servicio el día 239.",
        [
            ("Cohorte de lanzamiento", [(0, 90, "prueba gratuita de 90 días", "teal")]),
            ("Altas de mayo y junio", [(25, 85, "pruebas de 14 días", "gold")]),
            ("Servicio abierto", [(0, 239, "de abril a diciembre", "grey")]),
        ],
        unit="días desde el 6 de abril de 2020",
        events=[(90, "5 jul: cobro"), (239, "1 dic")],
        t_max=250, ticks=[0, 50, 100, 150, 200, 250], lane_h=50, label_w=230,
        note="El primer cobro de la cohorte de lanzamiento es cálculo propio (90 días después del 6 de abril). Las pruebas de 14 días se introdujeron en mayo y junio según la propia empresa; no se sabe cuántos usuarios convirtieron o cancelaron antes.",
        foot="Fuentes: TechCrunch (7 abr 2020), Deadline (21 oct 2020) y The Verge (8 jul y 22 oct 2020).")


# ------------------------------------------------------------------ 11. decisiones técnicas
def decisiones_tecnicas() -> Fig:
    f, y = sketch("Cuatro decisiones técnicas documentadas: la restricción, la decisión y lo que la fuente dice que ocurrió",
                  "Cuatro filas de tres cajas unidas por flechas. Solo teléfono: se priorizaron otras tareas de ingeniería y las aplicaciones de televisor llegaron el 20 de octubre. Turnstyle: dos versiones de vídeo según la patente y una disputa con Eko. Capturas de pantalla: la gestión de derechos digitales bloqueaba las capturas y se desarrolló un método propio. Televisor: AirPlay y Chromecast en junio y aplicaciones nativas el 20 de octubre.")
    heads = ["Restricción que la motivó", "Decisión", "Lo que dice la fuente"]
    for i, h in enumerate(heads):
        bx(f, 10 + i * 316, y + 4, 296, 34, h, "navy", 13, bold=True)
    rows = [
        ("Caso de uso en movimiento y prioridades de ingeniería", "Solo teléfono al inicio", "Aplicación nativa de televisor el 20 de octubre, un día antes del anuncio del cierre", "coral"),
        ("Una experiencia propia al girar el teléfono", "Turnstyle: dos versiones de vídeo según la patente", "Disputa con Eko: patente y secretos industriales; Quibi lo niega", "coral"),
        ("Gestión de derechos digitales que bloquea capturas", "Método propio: pulsar, mantener y deslizar", "Anunciado en julio de 2020 por el director de producto", "gold"),
        ("El uso real era en casa", "AirPlay y Chromecast, y después aplicaciones nativas", "Acceso por etapas; las fuentes difieren en la fecha de la primera", "gold"),
    ]
    for r, (a, b, c, k) in enumerate(rows):
        yy = y + 52 + r * 100
        bx(f, 10, yy, 296, 80, a, "plain", 13)
        bx(f, 326, yy, 296, 80, b, "teal", 13)
        bx(f, 642, yy, 288, 80, c, k, 13)
        f.arrow([(306, yy + 40), (326, yy + 40)])
        f.arrow([(622, yy + 40), (642, yy + 40)])
    return done(f, y + 52 + 4 * 100, "Dorado: consecuencia o dato de la fuente sin juicio; coral: costo o disputa señalados por la fuente. Whitman habló de AirPlay y Chromecast «a las pocas semanas»; Variety las sitúa en junio. No hay documentación técnica pública.",
                foot="Fuente: Deadline (21 oct 2020), The Verge (11 mar 2020), Engadget (24 jul 2020), Variety (1 dic 2020); esquema propio.")


# ------------------------------------------------------------------ 12. cascada del capital
def cascada_del_capital() -> Fig:
    return stacked_bars(
        "De 1.750 millones recaudados a unos 350 en caja: el uso del capital y lo que se devolvió",
        "Cuatro barras horizontales en millones de dólares. Capital recaudado: unos 1.750. Uso del capital por diferencia: unos 1.400 consumidos y unos 350 en caja al anunciar el cierre. Efectivo a devolver a los inversores: unos 350. Derechos vendidos a Roku: menos de 100.",
        ["Capital recaudado", "Uso del capital (cálculo propio)", "Efectivo a devolver", "Derechos a Roku (tope)"],
        [("Recaudado", [1750, 0, 0, 0], "navy"), ("Consumido por diferencia", [0, 1400, 0, 0], "coral"), ("En caja al cierre", [0, 350, 0, 0], "teal"),
         ("Efectivo a devolver", [0, 0, 350, 0], "teal"), ("Derechos a Roku (tope)", [0, 0, 0, 100], "gold")],
        unit="millones de dólares", horizontal=True, label_w=270,
        note="Lo consumido es la diferencia entre dos cifras de prensa y no una cifra contable: no distingue contenido, marketing y operación. Las dos últimas barras vienen de fuentes distintas y no se suman; la de Roku es un tope («significativamente menos» de 100 millones) y su destino no es público.",
        foot="Fuentes: Deadline (21 oct 2020), Variety (1 dic 2020) y The Verge (8 ene 2021, citando al WSJ).")


# ------------------------------------------------------------------ 13. mapa de supuestos
def mapa_de_supuestos() -> Fig:
    f, y = sketch("Mapa de supuestos: los más importantes eran los que menos evidencia tenían antes de lanzar",
                  "Cuadrante con dos ejes: importancia para el negocio, de abajo hacia arriba, y evidencia disponible antes del lanzamiento, de izquierda a derecha. Uso en movimiento y disposición a pagar por contenido corto premium están arriba a la izquierda. Que bastara el teléfono está en el centro con evidencia contraria posterior. El inventario publicitario vendido está a la derecha como evidencia a favor.")
    f.box(70, y + 10, 420, 150, "", "coral")
    f.box(490, y + 10, 420, 150, "", "plain")
    f.box(70, y + 160, 420, 150, "", "plain")
    f.box(490, y + 160, 420, 150, "", "plain")
    f.text(280, y + 34, "Probar primero: muy importante y poca evidencia", 13, "middle", 700, "#5c1f14")
    f.text(700, y + 34, "Seguir con vigilancia", 13, "middle", 700, "#5b7280")
    f.text(280, y + 184, "Probar si es barato", 13, "middle", 700, "#5b7280")
    f.text(700, y + 184, "Dar por buenos", 13, "middle", 700, "#5b7280")
    bx(f, 100, y + 56, 180, 80, "Uso en movimiento frecuente y valioso", "coral", 13)
    bx(f, 296, y + 56, 180, 80, "Se paga por lo corto premium frente a lo gratuito", "coral", 13)
    bx(f, 506, y + 56, 190, 80, "Basta el teléfono, sin televisor: evidencia contraria posterior", "gold", 13)
    bx(f, 726, y + 56, 170, 80, "Calidad de los títulos: valoración disputada", "gold", 13)
    bx(f, 726, y + 206, 170, 80, "Interés de anunciantes: 150 millones vendidos", "teal", 13)
    bx(f, 100, y + 206, 380, 80, "Que una función propia (Turnstyle) diferencie al producto", "plain", 13)
    f.text(70, y + 330, "poca evidencia", 13, "start", 400, "#5b7280")
    f.text(910, y + 330, "mucha evidencia", 13, "end", 400, "#5b7280")
    return done(f, y + 340, "Ubicación según valoración de este programa a partir de lo público; Quibi pudo tener estudios internos que moverían puntos. El eje vertical es la importancia para que el negocio funcione, de menos abajo a más arriba.",
                foot="Fuente: Variety, TechCrunch, Deadline y NBC News (2018 a 2020); esquema propio.")


# ------------------------------------------------------------------ 14. puertas de aprendizaje
def puertas_de_aprendizaje() -> Fig:
    f, y = sketch("Siete puertas de decisión: qué se sabe públicamente de cada una",
                  "Siete puertas en dos filas. Investigación de la hipótesis y prototipo o prueba pequeña: se desconoce. Lanzamiento escalonado: considerado y descartado por los responsables. Medición de conversión antes de comprometer capital: la prueba de 90 días retrasó el dato hasta julio. Criterios de abandono escritos: se desconocen. Capital por tramos: no, capital grande desde 2018. Preventa de publicidad: 150 millones vendidos antes del lanzamiento.")
    cells = [
        ("1 Investigación de la hipótesis", "No se sabe: no hay documentos públicos", "grey"),
        ("2 Prototipo o prueba pequeña", "No se sabe: no hay documentos públicos", "grey"),
        ("3 Lanzamiento escalonado", "Considerado y descartado, según Whitman, para crear una categoría", "coral"),
        ("4 Medir conversión antes de comprometer capital", "La prueba de 90 días llevó el dato a julio", "coral"),
        ("5 Criterios de abandono escritos", "No se sabe; la salida se decidió con los datos del verano", "grey"),
        ("6 Capital por tramos", "Capital grande desde 2018: 1.000 millones anunciados", "coral"),
        ("7 Preventa de publicidad", "Unos 150 millones vendidos antes del lanzamiento", "teal"),
    ]
    w, g = 224, 12
    for i, (t, r, k) in enumerate(cells):
        row, col = divmod(i, 4)
        x = 10 + col * (w + g)
        yy = y + 8 + row * 190
        bx(f, x, yy, w, 76, t, "plain", 13, bold=True)
        bx(f, x, yy + 80, w, 90, r, k, 13)
    return done(f, y + 8 + 2 * 190, "Teal: hay evidencia pública de que existió. Coral: hay evidencia pública de que no existió o se decidió no hacerlo. Gris: no se sabe. Que una puerta no sea pública no significa que faltara.",
                foot="Fuente: Deadline (21 oct 2020), TechCrunch (2019), The Verge (8 jul 2020); esquema propio.")


# ------------------------------------------------------------------ 15. cronología del cierre
def cronologia_del_cierre() -> Fig:
    return timeline(
        "Del 30 de septiembre al 8 de enero: tres semanas de búsqueda, un anuncio, el cierre y la venta de los derechos",
        "Línea de tiempo en días desde el 30 de septiembre de 2020. Tres semanas de búsqueda de socios y compradores hasta el anuncio del 21 de octubre, día 21. La decisión de devolver el efectivo hacia el 7 de octubre, día 7. El servicio se cierra el 1 de diciembre, día 62, y los derechos se venden a Roku el 8 de enero, día 100.",
        [
            ("Búsqueda de socios y compradores", [(0, 21, "tres semanas", "gold")]),
            ("Decisión de devolver el efectivo", [(6, 21, "decisión", "navy")]),
            ("Servicio y plantilla", [(21, 62, "desmontaje", "coral")]),
            ("Activos y litigios", [(62, 100, "venta a Roku", "teal")]),
        ],
        unit="días desde el 30 de septiembre de 2020",
        events=[(21, "21 oct: anuncio"), (62, "1 dic: cierre"), (100, "8 ene: Roku")],
        t_max=120, ticks=[0, 20, 40, 60, 80, 100, 120], lane_h=50, label_w=280,
        note="El día 0 es tres semanas antes del anuncio, según Katzenberg. La fecha de la decisión es una aproximación a partir de «un par de semanas» que dijo Whitman. Roku compró más de 75 programas por menos de 100 millones; la disputa con Eko seguía abierta.",
        foot="Fuentes: Deadline (21 oct 2020), The Verge (22 oct 2020 y 8 ene 2021) y Variety (1 dic 2020).")


# ------------------------------------------------------------------ 16. capital por tramos
def capital_por_tramos() -> Fig:
    f, y = sketch("Propuesta: capital por tramos, cada uno liberado por un hito de evidencia y con una salida si no se cumple",
                  "Cuatro etapas en fila: hipótesis y prueba barata, piloto con una cohorte, lanzamiento por segmento y escala. Cada una tiene un hito de evidencia que libera el siguiente tramo y una flecha de salida hacia abandono o cambio si no se cumple. Es una propuesta de este programa.")
    steps = [("1 Hipótesis y prueba barata", "Hito: uso y disposición a pagar medidos con una cohorte pequeña", "Tramo pequeño"),
             ("2 Piloto con una cohorte", "Hito: conversión y retención por encima del umbral pactado", "Tramo moderado"),
             ("3 Lanzamiento por segmento", "Hito: costo por suscriptor por debajo del límite", "Tramo mayor"),
             ("4 Escala", "Hito: retención sostenida a los 90 días", "Resto del capital")]
    w, g = 214, 21
    for i, (t, h, c) in enumerate(steps):
        x = 10 + i * (w + g)
        bx(f, x, y + 8, w, 56, t, "teal", 13, bold=True)
        bx(f, x, y + 68, w, 90, h, "plain", 13)
        bx(f, x, y + 162, w, 40, c, "gold", 13)
        if i:
            f.arrow([(x - g, y + 36), (x, y + 36)])
        f.arrow([(x + w / 2, y + 202), (x + w / 2, y + 232)], color="#c0432f", dashed=True)
    bx(f, 10, y + 232, 920, 58, "Si el hito no se cumple: cambiar de modelo, devolver el capital restante o parar, según criterios firmados antes de gastar", "coral", 13, bold=True)
    return done(f, y + 310, "La proporción de capital por tramo es ilustrativa. Propuesta de este programa: no afirma que los inversores la habrían aceptado ni que el resultado habría cambiado.",
                foot="Fuente: análisis propio apoyado en las clases SE-130 y SE-141 del curso.")


# ------------------------------------------------------------------ 17. árbol de fallas
def arbol_de_fallas() -> Fig:
    f, y = sketch("Árbol de fallas: el cierre a los siete meses exigió tres condiciones a la vez",
                  "Árbol de fallas con compuerta Y. Evento superior: cierre del servicio a los siete meses del lanzamiento. Ramas: la demanda de pago fue insuficiente, el capital necesario para llegar a escala no estaba disponible y no hubo un cambio de rumbo a tiempo. Cada rama tiene causas documentadas e interpretaciones.")
    bx(f, 290, y + 4, 360, 56, "Cierre del servicio a los siete meses", "navy", 14, bold=True)
    f.line(470, y + 60, 470, y + 84)
    f.dot(470, y + 96, "Y")
    f.line(155, y + 112, 785, y + 112)
    for x in (155, 470, 785):
        f.line(x, y + 112, x, y + 130)
    bx(f, 10, y + 130, 290, 60, "La demanda de pago fue insuficiente", "plain", bold=True)
    bx(f, 325, y + 130, 290, 60, "No había capital para llegar a escala", "plain", bold=True)
    bx(f, 640, y + 130, 290, 60, "No hubo cambio de rumbo a tiempo", "plain", bold=True)
    for x in (155, 470, 785):
        f.line(x, y + 190, x, y + 206)
    f.dot(155, y + 218, "O")
    f.dot(470, y + 218, "Y")
    f.dot(785, y + 218, "O")
    leaves = [
        (10, [("Conversión baja o en disputa (estimaciones de terceros)", "coral"), ("Oferta gratuita de vídeo corto (documentado)", "coral"), ("Uso en movimiento reducido por el confinamiento (documentado)", "coral")]),
        (325, [("Necesidad de más capital pronto, según Whitman (documentado)", "coral"), ("Datos que no respaldaban una nueva ronda (documentado)", "coral")]),
        (640, [("Experimentos del verano sin cambiar la respuesta (documentado)", "coral"), ("Televisor solo el 20 de octubre (documentado)", "coral"), ("Compromiso de capital previo muy grande (interpretación)", "gold")]),
    ]
    for x, items in leaves:
        cy = y + 244
        f.line(x + 145, y + 230, x + 145, y + 244)
        for t, k in items:
            bx(f, x, cy, 290, 58, t, k)
            cy += 70
    return done(f, y + 244 + 70 * 3 + 6, "O: basta una causa; Y: hacen falta todas. Es un modelo lógico simplificado, sin probabilidades ni datos internos. Evitar una de las tres ramas principales habría evitado el cierre en ese plazo, según el modelo.",
                foot="Fuente: Deadline, Variety, NBC News y The Verge (2020); esquema propio.")


# ------------------------------------------------------------------ 18. operación en días
def operacion_en_dias() -> Fig:
    return timeline(
        "Siete meses de operación: cuándo llegaron el producto, los datos y las decisiones de capital",
        "Línea de tiempo en días desde el 6 de abril de 2020 con tres carriles: producto, datos y capital. Producto: AirPlay y Chromecast en junio y aplicaciones de televisor el día 197. Datos: primer cobro posible el día 90, informe de Sensor Tower el día 93 y estimaciones de Kantar al final de cada trimestre. Capital: gasto esperado de 1.000 millones hacia el tercer trimestre, decisión de cerrar hacia el día 184 y anuncio el día 198.",
        [
            ("Producto: acceso al televisor", [(0, 70, "solo teléfono", "coral"), (70, 197, "AirPlay y Chromecast", "gold"), (197, 239, "apps", "teal")]),
            ("Datos que decidían el negocio", [(90, 93, "", "navy"), (85, 87, "", "grey"), (177, 179, "", "grey")]),
            ("Capital", [(0, 177, "gasto esperado: 1.000 millones", "gold"), (184, 198, "", "navy")]),
        ],
        unit="días desde el 6 de abril de 2020",
        events=[(90, "5 jul"), (198, "21 oct")],
        t_max=250, ticks=[0, 50, 100, 150, 200, 250], lane_h=52, label_w=260,
        note="Los días son cálculo propio a partir de fechas de prensa. En el carril de datos: primer cobro (día 90), informe de Sensor Tower (93) y cierres de trimestre con las estimaciones de Kantar (85 y 177). El paso de «solo teléfono» a AirPlay y Chromecast se sitúa en junio (Variety); Whitman habló de pocas semanas.",
        foot="Fuentes: Variety (1 dic 2020), NBC News (22 oct 2020), Deadline (21 oct 2020) y The Verge (8 jul 2020).")

# ==== EXPANDED FIGURES (end) ====

# ==== EXPANDED FIGURES2 (begin) ====

SRCQB = "Fuente: prensa especializada citada en el caso (2018 a 2021); esquema propio."


def sedes_y_equipo() -> Fig:
    return hub(
        "Sede y entorno: una empresa de unas 200 personas que orquestaba a estudios, tiendas y socios",
        "Esquema de relaciones con Quibi en Los Ángeles en el centro. Arriba: estudios y bancos inversores, creadores y estudios que producían series, un operador móvil socio y anunciantes. Abajo: tiendas de aplicaciones, fabricantes de dispositivos de televisor y Roku como comprador de los derechos.",
        ("Quibi: Los Ángeles, unas 200 personas al cierre", "navy"),
        [("Estudios y bancos inversores", "plain", ""), ("Creadores y estudios: producen las series", "plain", ""), ("Operador móvil socio", "plain", ""), ("Anunciantes: inventario del primer año vendido", "plain", ""),
         ("Tiendas de aplicaciones", "teal", ""), ("Dispositivos de televisor: AirPlay, Chromecast y apps", "teal", ""), ("Roku: compra los derechos en 2021", "gold", "")],
        "No es un organigrama ni un mapa. Estructura interna, oficinas fuera de Los Ángeles y plantilla de 2018 y 2019: no se sabe.", SRCQB)


def competidores() -> Fig:
    return grouped_bars(
        "Frente a Disney+: uno o dos órdenes de magnitud menos en registros y en suscriptores",
        "Dos grupos de barras en millones con eje logarítmico. Registros en los primeros tres días: unos 9,5 de Disney+ y unos 0,91 de Quibi. Suscriptores de pago o hogares suscriptores en 2020: más de 50 de Disney y 1,1 de Quibi en el segundo trimestre.",
        ["Registros en los tres primeros días", "Suscriptores de pago u hogares, 2020"],
        [("Disney+", [9.5, 50], "navy"), ("Quibi", [0.91, 1.1], "coral")],
        unit="millones", log=True, decimals=2, ticks=[0.5, 1, 5, 10, 50],
        note="Las dos medidas no son iguales (registros frente a suscriptores o hogares), las fuentes son estimaciones de terceros (Sensor Tower y Kantar) y la cifra de Disney es de abril de 2020. La figura compara órdenes de magnitud, no calidad ni gustos.",
        foot="Fuentes: The Verge (8 jul 2020, Sensor Tower) y Variety (1 dic 2020, Kantar).")


def pila_de_plataforma() -> Fig:
    return layer_stack(
        "Plataforma de Quibi: del teléfono al televisor, con la infraestructura de entrega sin datos públicos",
        "Cuatro capas de abajo arriba: teléfono y tiendas de aplicaciones; aplicación con Turnstyle, protección de derechos y capturas propias; acceso al televisor por AirPlay, Chromecast y aplicaciones nativas; y entrega de vídeo cuya infraestructura no es pública.",
        [("Entrega y servidor", "Infraestructura y software de servidor: no son públicos", "plain"),
         ("Acceso al televisor", "AirPlay y Chromecast (junio); aplicaciones nativas (20 de octubre)", "gold"),
         ("Aplicación móvil", "Turnstyle, protección de derechos y capturas propias", "teal"),
         ("Teléfono y tiendas", "Descarga, preinscripción y compra dentro de la aplicación", "plain")],
        [("Turnstyle: dos versiones de vídeo según la patente (The Verge)", "teal"), ("Derechos digitales: bloquean capturas; método propio (Engadget)", "gold"), ("No se sabe: lenguajes, nube, base de datos y proveedor de vídeo", "coral")],
        "Lo que la prensa y los responsables dicen; no es una arquitectura técnica. Los datos de servidor no son públicos y no se infieren.", SRCQB)


def dependencias_externas() -> Fig:
    return hub(
        "Dependencias externas del producto: casi todo lo que llegaba al espectador pasaba por un tercero",
        "Esquema con el producto Quibi en el centro. Arriba: estudios y creadores que entregan los títulos, tiendas de aplicaciones que distribuyen y cobran, titulares de derechos que exigen protección y un operador móvil socio. Abajo: fabricantes de televisores y dispositivos, y la infraestructura propia marcada como no pública.",
        ("Producto Quibi", "teal"),
        [("Estudios y creadores: entregan los títulos", "plain", "títulos"), ("Tiendas de aplicaciones: distribuyen y cobran", "plain", "cobran"), ("Titulares de derechos: exigen protección", "plain", "exigen"), ("Operador móvil: socio con 5G y un año gratis", "plain", "socio"),
         ("Apple, Amazon y Google: pantalla grande", "gold", "acceso"), ("Infraestructura propia: no es pública", "coral", "")],
        "Solo dependencias que la prensa menciona. Cada tercero tenía sus propias reglas; la infraestructura de Quibi no se conoce y no se infiere.", SRCQB)


def a_prueba_de_fallos() -> Fig:
    return kanban(
        "Resiliencia del negocio: qué existía, qué falló, qué no existía y qué debió existir",
        "Cuatro columnas. Existían y funcionaron: preventa de publicidad, cierre ordenado con devolución del capital, venta de derechos a Roku. Existían y fallaron: pruebas de cambio de modelo en el verano, prueba gratuita larga, revisión tardía de solo móvil. No existían de forma pública: lanzamiento escalonado, criterios de abandono, tramos de capital. Debieron existir: pruebas por supuesto, tramos de capital, criterios firmados, estudio de alternativas gratuitas.",
        [("Existían y funcionaron", "teal", ["Preventa de unos 150 millones de publicidad", "Cierre ordenado: devolución de unos 350 millones", "Venta del catálogo a Roku"]),
         ("Existían y fallaron", "coral", ["Variantes del verano: ninguna cambió la respuesta", "Prueba gratuita de 90 días: datos tardíos", "Restricción solo móvil revisada tarde"]),
         ("No existían de forma pública", "gold", ["Lanzamiento escalonado (descartado)", "Criterios de abandono escritos", "Capital por tramos", "Estudio público de alternativas gratuitas"]),
         ("Debieron existir (análisis propio)", "plain", ["Una prueba barata por supuesto", "Tramos de capital ligados a hitos", "Criterios firmados antes del gasto", "Análisis del antecedente Go90"])],
        "La cuarta columna es análisis propio. De resiliencia técnica (disponibilidad y recuperación) no hay datos públicos; ninguna fuente reporta caídas.",
        SRCQB)

# ==== EXPANDED FIGURES2 (end) ====

FIGURES = {
    "quibi-premisa-y-realidad.svg": premisa_y_realidad,
    "quibi-producto-y-distribucion.svg": producto,
    "quibi-linea-de-tiempo.svg": linea_de_tiempo,
    "quibi-dinero.svg": dinero,
    "quibi-audiencia.svg": audiencia,
    "quibi-aprender-antes-de-escalar.svg": aprender_antes_de_escalar,
    # expanded entries
    "quibi-cuadrante-de-mercado.svg": cuadrante_de_mercado,
    "quibi-lienzo-del-producto.svg": lienzo_del_producto,
    "quibi-embudo-con-datos.svg": embudo_con_datos,
    "quibi-descargas-segun-cada-fuente.svg": descargas_segun_cada_fuente,
    "quibi-recorrido-y-cobro.svg": recorrido_y_cobro,
    "quibi-decisiones-tecnicas.svg": decisiones_tecnicas,
    "quibi-cascada-del-capital.svg": cascada_del_capital,
    "quibi-mapa-de-supuestos.svg": mapa_de_supuestos,
    "quibi-puertas-de-aprendizaje.svg": puertas_de_aprendizaje,
    "quibi-cronologia-del-cierre.svg": cronologia_del_cierre,
    "quibi-capital-por-tramos.svg": capital_por_tramos,
    "quibi-arbol-de-fallas.svg": arbol_de_fallas,
    "quibi-operacion-en-dias.svg": operacion_en_dias,
    # expanded entries2
    "quibi-sedes-y-equipo.svg": sedes_y_equipo,
    "quibi-competidores.svg": competidores,
    "quibi-pila-de-plataforma.svg": pila_de_plataforma,
    "quibi-dependencias-externas.svg": dependencias_externas,
    "quibi-a-prueba-de-fallos.svg": a_prueba_de_fallos,
}
