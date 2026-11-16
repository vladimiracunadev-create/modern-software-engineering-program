"""Figures for the failure case study casos/fallo/quibi.md.

Only public facts are used: Deadline (21 Oct 2020), Variety (2018 and 2020), TechCrunch (2019 and 2020), The Verge (2020),
NBC News (2020). Quibi's internal data are not public and are not inferred.
"""
from __future__ import annotations

from figure_kit import Fig, _kit_finish, _kit_start, _wrap, grouped_bars, timeline

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


FIGURES = {
    "quibi-premisa-y-realidad.svg": premisa_y_realidad,
    "quibi-producto-y-distribucion.svg": producto,
    "quibi-linea-de-tiempo.svg": linea_de_tiempo,
    "quibi-dinero.svg": dinero,
    "quibi-audiencia.svg": audiencia,
    "quibi-aprender-antes-de-escalar.svg": aprender_antes_de_escalar,
}
