"""Figures for the failure case study casos/fallo/crowdstrike.md.

Every number comes from a cited public source: the CrowdStrike Root Cause Analysis of Channel File 291
(6 Aug 2024), its preliminary Post Incident Review and the BBC report on the Parametrix estimate.
"""
from __future__ import annotations

from figure_kit import Fig, _kit_finish, _kit_start, _wrap, stacked_bars, timeline

FUENTE = "Fuente: análisis de causa raíz de CrowdStrike (6 ago 2024) y revisión preliminar del incidente; lectura propia."


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


# ------------------------------------------------------------------ 1. camino del contenido
def camino_del_contenido() -> Fig:
    f, y = sketch("El camino de un archivo de canal: de la nube de CrowdStrike al kernel de Windows",
                  "Diagrama de dos zonas. En la nube, el sistema de configuración de contenido crea instancias de plantilla, el validador las comprueba y se publica el archivo de canal 291. En el equipo Windows del cliente, el controlador csagent.sys, que corre en modo kernel, contiene el intérprete de contenido que lee ese archivo cuando Windows notifica la creación de una tubería con nombre.")
    f.group(10, y, 300, 250, "Nube de CrowdStrike", "grey")
    bx(f, 28, y + 40, 264, 56, "Content Configuration System: los ingenieros de detección crean Template Instances", "plain")
    bx(f, 28, y + 112, 264, 56, "Content Validator: comprueba cada instancia contra la definición del Template Type", "gold")
    bx(f, 28, y + 184, 264, 50, "Se publica el archivo de canal 291 (C-00000291*.sys)", "plain")
    f.arrow([(160, y + 96), (160, y + 112)])
    f.arrow([(160, y + 168), (160, y + 184)])
    f.group(360, y, 570, 250, "Equipo Windows del cliente (sensor 7.11 o superior)", "grey")
    bx(f, 380, y + 40, 530, 40, "Windows notifica la creación de una tubería con nombre (IPC)", "plain")
    f.group(380, y + 96, 530, 138, "Controlador csagent.sys (modo kernel)", "navy")
    bx(f, 396, y + 126, 240, 92, "Content Interpreter: lee el archivo de canal y compara con expresiones regulares", "coral")
    bx(f, 660, y + 126, 234, 92, "Template Type IPC: arma 20 entradas para el intérprete", "teal")
    f.arrow([(645, y + 172), (636, y + 172)])
    f.arrow([(645, y + 80), (645, y + 96)])
    f.arrow([(292, y + 209), (360, y + 209)])
    bx(f, 10, y + 266, 440, 74, "Sensor Content: viaja con el sensor. El cliente decide qué versión instala (N, N-1 o N-2).", "teal")
    bx(f, 470, y + 266, 460, 74, "Rapid Response Content: es configuración, no código, y llegó a todos los equipos conectados sin que el cliente eligiera dónde ni cuándo.", "coral")
    return done(f, y + 354, "El riesgo no estaba en el archivo en sí, sino en que un archivo de datos se interpretaba dentro del kernel y salía a toda la flota sin una puerta intermedia. Es lectura propia sobre lo que describe el informe: el informe documenta las dos rutas de entrega y que el control del cliente sobre el contenido rápido se añadió después.")


# ------------------------------------------------------------------ 2. lectura fuera de límites
def lectura_fuera_de_limites() -> Fig:
    f, y = sketch("Veintiuna entradas pedidas, veinte entregadas: la lectura que no existía",
                  "Fila de 21 casillas numeradas del 1 al 21. Las casillas 1 a 20 son punteros válidos que entrega el sensor; la casilla 21 queda fuera del arreglo y no apunta a memoria válida. El intérprete de contenido pide el índice 0x14, es decir la entrada 21, lee una dirección inválida y Windows detiene el sistema con el código PAGE_FAULT_IN_NONPAGED_AREA.")
    left, cw = 40, 40
    f.text(left, y + 14, "Arreglo de entradas que el sensor arma para el Template Type IPC", 13, "start", 700)
    for i in range(21):
        kind = "teal" if i < 20 else "coral"
        f.box(left + i * cw, y + 26, cw - 4, 40, str(i + 1), kind, 13, bold=True, radius=4)
    f.line(left - 4, y + 78, left + 20 * cw - 8, y + 78, "#087f8c", width=2)
    f.text(left + 10 * cw - 4, y + 98, "20 entradas válidas: lo que entrega el código del sensor", 13, "middle", 400, "#0b3f45")
    f.arrow([(left + 20 * cw + 14, y + 112), (left + 20 * cw + 14, y + 72)], color="#c0432f")
    f.text(left + 20 * cw - 10, y + 128, "entrada 21: no hay puntero válido", 13, "end", 700, "#5c1f14")
    bx(f, 40, y + 158, 410, 74, "La definición del Template Type declaraba 21 campos. El validador y las instancias del archivo 291 asumían 21.", "gold")
    bx(f, 490, y + 158, 410, 74, "El código del sensor pasaba 20 al intérprete. Con un comodín en el campo 21 nunca se leía; con un criterio real, sí.", "gold")
    f.arrow([(245, y + 232), (245, y + 258)])
    f.arrow([(695, y + 232), (695, y + 258)])
    bx(f, 40, y + 258, 860, 52, "Content Interpreter lee el índice 0x14 (la entrada 21) → lee una dirección inválida en csagent.sys", "coral")
    f.arrow([(470, y + 310), (470, y + 334)])
    bx(f, 40, y + 334, 860, 52, "Windows detiene el sistema (pantalla azul): PAGE_FAULT_IN_NONPAGED_AREA (0x50), módulo csagent.sys.", "navy")
    return done(f, y + 400, "La lectura fuera de límites no escribe memoria: el informe indica que no es una escritura arbitraria y que fue revisada de forma independiente. Documentado: el desajuste 21 frente a 20, el índice 0x14 y la excepción no recuperable. El bucle de reinicios aparece en la guía de remediación de CrowdStrike, no en el análisis de causa raíz.", "gold")


# ------------------------------------------------------------------ 3. línea de tiempo en días
def tiempo_en_dias() -> Fig:
    return timeline(
        "142 días entre la disponibilidad del sensor 7.11 y la caída",
        "Línea de tiempo en días desde el 28 de febrero de 2024. El sensor 7.11 está disponible desde el día 0. La primera instancia IPC se despliega el día 6, tres más entre los días 40 y 56, todas sin incidentes. El día 142 se despliegan dos instancias, una con el criterio no comodín en el campo 21, y se produce la caída.",
        [
            ("Sensor 7.11", [(0, 142, "Disponible con el Template Type IPC compilado", "teal")]),
            ("Instancias IPC", [(6, 8, "", "navy"), (40, 56, "3", "navy"), (142, 144, "", "coral")]),
            ("Resultado", [(6, 56, "sin incidentes en producción", "grey"), (142, 150, "", "coral")]),
        ],
        unit="días desde el 28 de febrero de 2024 (sensor 7.11)",
        events=[(0, "28 feb"), (6, "5 mar"), (40, "8 abr"), (56, "24 abr"), (142, "19 jul")],
        t_max=150, ticks=[0, 30, 60, 90, 120, 150], lane_h=50,
        note="Que cuatro despliegues funcionaran no probó que el quinto lo hiciera: los anteriores usaban un comodín en el campo 21 y la entrada que faltaba nunca se leyó. Los días son cálculo propio a partir de las fechas del informe.",
        foot="Fuente: revisión preliminar del incidente de CrowdStrike (julio de 2024) y análisis de causa raíz (6 ago 2024).")


# ------------------------------------------------------------------ 4. ventana de exposición
def ventana_de_exposicion() -> Fig:
    return timeline(
        "Una ventana de 78 minutos bastó para alcanzar a 8,5 millones de equipos",
        "Línea de tiempo en minutos desde las 04:00 UTC del 19 de julio de 2024. El archivo defectuoso se publica a las 04:09, minuto 9, y se revierte a las 05:27, minuto 87. Los equipos Windows con sensor 7.11 o superior conectados en esos 78 minutos lo recibieron; los que se conectaron después no.",
        [
            ("Archivo 291 defectuoso", [(9, 87, "78 min publicado", "coral")]),
            ("Equipos en línea con sensor 7.11+", [(9, 87, "reciben el archivo y caen", "coral")]),
            ("Equipos que se conectan después", [(87, 120, "no afectados", "teal")]),
        ],
        unit="minutos desde las 04:00 UTC del 19 de julio de 2024",
        events=[(9, "04:09 publicación"), (87, "05:27 reversión")],
        t_max=120, ticks=[0, 20, 40, 60, 80, 100, 120], lane_h=54, label_w=250,
        note="La reversión protegió a los equipos que se conectaron después. Los que ya habían caído solo se recuperaban si lograban descargar el archivo corregido al reiniciar; si seguían cayendo, hacía falta intervención manual (guía de remediación de CrowdStrike). Cifra de Microsoft: unos 8,5 millones de equipos Windows, menos del 1 % del total.",
        foot="Fuentes: CrowdStrike (revisión preliminar) y Microsoft (20 jul 2024). Esquema temporal propio.")


# ------------------------------------------------------------------ 5. quién asume la pérdida
def quien_asume_la_perdida() -> Fig:
    return stacked_bars(
        "Cuánto de una pérdida estimada de 5.400 millones estaba asegurada",
        "Dos barras horizontales de 5.400 millones de dólares cada una, la pérdida directa estimada por Parametrix para las 500 mayores empresas de Estados Unidos sin contar a Microsoft. En el escenario bajo, 540 millones están asegurados y 4.860 no; en el escenario alto, 1.080 millones asegurados y 4.320 no.",
        ["Escenario bajo de cobertura", "Escenario alto de cobertura"],
        [("Asegurada", [540, 1080], "teal"), ("No asegurada", [4860, 4320], "coral")],
        unit="millones de dólares", horizontal=True, label_w=230,
        note="Delta Air Lines declaró por separado un costo de más de 500 millones de dólares y demandó a CrowdStrike: es una cifra de una empresa, no se suma a la estimación de Parametrix y la demanda sigue siendo una alegación, no un hecho probado.",
        foot="Fuentes: BBC News (24 jul 2024) sobre estimación de Parametrix; CNBC (17 dic 2024) sobre la demanda de Delta.")


# ------------------------------------------------------------------ 6. antes y después
def antes_y_despues() -> Fig:
    f, y = sketch("Del reparto a toda la flota a un despliegue por anillos con control del cliente",
                  "Dos filas de cajas. La fila superior muestra el recorrido del 19 de julio: validador, publicación a todos los sensores conectados y caída de los equipos. La fila inferior muestra el recorrido prometido en el análisis de causa raíz: validador con comprobaciones nuevas, pruebas por instancia, canary, anillos con tiempo de observación y control del cliente.")
    f.text(14, y + 18, "Antes (19 de julio de 2024)", 14, "start", 700, "#5c1f14")
    bw, gap = 262, 40
    for i, (t, k) in enumerate((("Validador: acepta la instancia con un campo 21 sin respaldo", "gold"),
                                ("Publicación a todos los sensores conectados", "coral"),
                                ("Caída de los equipos Windows 7.11+ que recibieron el archivo", "coral"))):
        bx(f, 10 + i * (bw + gap), y + 30, bw, 66, t, k)
        if i:
            f.arrow([(10 + i * (bw + gap) - gap, y + 63), (10 + i * (bw + gap), y + 63)])
    f.text(14, y + 134, "Después (compromisos del análisis de causa raíz)", 14, "start", 700, "#0b3f45")
    w5, g5 = 168, 20
    pasos = (("Validador con comprobación de campos pedidos y entregados", "teal"),
             ("Prueba de cada instancia con criterios no comodín", "teal"),
             ("Canary: un grupo pequeño primero", "teal"),
             ("Anillos más amplios con tiempo de observación", "teal"),
             ("El cliente elige dónde y cuándo", "teal"))
    for i, (t, k) in enumerate(pasos):
        bx(f, 10 + i * (w5 + g5), y + 148, w5, 88, t, k)
        if i:
            f.arrow([(10 + i * (w5 + g5) - g5, y + 192), (10 + i * (w5 + g5), y + 192)])
    f.group(10, y + 256, 920, 108, "Defensas en el propio sensor", "grey")
    bx(f, 24, y + 288, 280, 62, "Comprobación de límites del arreglo (25 jul)", "plain")
    bx(f, 330, y + 288, 280, 62, "El compilador valida el número de entradas (27 jul)", "plain")
    bx(f, 636, y + 288, 280, 62, "Fuzzing de los manejadores de contenido", "plain")
    return done(f, y + 380, "Las fechas son las que informa CrowdStrike como implantadas o comprometidas al 6 de agosto de 2024. Que cada compromiso se cumpliera y fuera suficiente no lo documenta el informe: es lo que el programa llama una afirmación por verificar.", "gold")


FIGURES = {
    "crowdstrike-camino-del-contenido.svg": camino_del_contenido,
    "crowdstrike-lectura-fuera-de-limites.svg": lectura_fuera_de_limites,
    "crowdstrike-142-dias-hasta-la-caida.svg": tiempo_en_dias,
    "crowdstrike-ventana-de-78-minutos.svg": ventana_de_exposicion,
    "crowdstrike-quien-asume-la-perdida.svg": quien_asume_la_perdida,
    "crowdstrike-antes-y-despues.svg": antes_y_despues,
}
