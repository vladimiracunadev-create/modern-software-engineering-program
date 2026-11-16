"""Figures for the failure case study casos/fallo/therac-25.md.

Facts come from Leveson and Turner, "An Investigation of the Therac-25 Accidents", IEEE Computer 26(7), 1993,
pp. 18-41. Where a figure is a schematic and not a measurement, the foot says so.
"""
from __future__ import annotations

from figure_kit import Fig, _kit_finish, _kit_start, _wrap, percentile_intervals, timeline

FUENTE = "Fuente: Leveson y Turner, IEEE Computer 26(7), 1993; esquema propio."


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


# ------------------------------------------------------------------ 1. tres máquinas
def tres_maquinas() -> Fig:
    f, y = sketch("Tres aceleradores, un cambio de reparto: quién protegía al paciente",
                  "Tres columnas: Therac-6, Therac-20 y Therac-25. En las dos primeras, el computador PDP-11 se añadió a máquinas que ya funcionaban solas y conservaron los interlocks y circuitos protectores de hardware. En el Therac-25, diseñado desde el inicio para control por computador, el software asumió más responsabilidad de seguridad y no se duplicaron todos los interlocks de hardware.")
    cols = (("Therac-6", "Máquina independiente con historial clínico; el computador añadió comodidad", "Interlocks y seguridad de hardware conservados", "teal"),
            ("Therac-20", "Misma base de software; circuitos protectores independientes y topes mecánicos", "El mismo error de edición existía, pero el hardware impedía la dosis", "teal"),
            ("Therac-25", "Doble paso compacto; prototipo de 1976 y versión computarizada a fines de 1982", "El software vigilaba y controlaba; no se duplicaron todos los interlocks", "coral"))
    w, gap = 290, 25
    for i, (nombre, a, b, k) in enumerate(cols):
        x = 10 + i * (w + gap)
        bx(f, x, y + 6, w, 40, nombre, "navy", 14, True)
        bx(f, x, y + 62, w, 84, a, "plain")
        bx(f, x, y + 164, w, 84, b, k)
        f.arrow([(x + w / 2, y + 46), (x + w / 2, y + 62)])
        f.arrow([(x + w / 2, y + 146), (x + w / 2, y + 164)])
        if i:
            f.arrow([(x - gap, y + 26), (x, y + 26)])
    bx(f, 10, y + 270, 920, 62, "Marzo de 1983: análisis de seguridad por árbol de fallos. Supuso que los errores de programación estaban reducidos por pruebas y modeló los fallos del computador como fallos de hardware o ruido.", "gold")
    return done(f, y + 346, "Documentado: que parte del software se reutilizó entre las tres máquinas y que el análisis de 1983 no consideró errores de software. La lectura de que ese reparto de responsabilidad fue la decisión de arquitectura de mayor consecuencia es el análisis de Leveson y Turner, no un dato medido.", "gold")


# ------------------------------------------------------------------ 2. plataforma giratoria
def plataforma_giratoria() -> Fig:
    f, y = sketch("Una plataforma giratoria decide qué haz recibe el paciente",
                  "Tres posiciones de la plataforma giratoria. En modo electrones, imanes de barrido esparcen el haz y una cámara de ionización lo mide. En modo rayos X, un blanco, un aplanador del haz y una cámara miden y moldean un haz con una corriente unas cien veces mayor. En la posición de luz de campo hay un espejo y ningún haz. Si la plataforma está en la posición equivocada, el haz llega concentrado.")
    w, gap = 290, 25
    cols = (("Electrones (5 a 25 MeV)", "Imanes de barrido esparcen el haz hasta una concentración terapéutica", "teal"),
            ("Rayos X (25 MeV)", "Blanco y aplanador del haz; corriente cerca de 100 veces mayor para compensar el atenuador", "gold"),
            ("Luz de campo", "Espejo de acero y luz que simula el haz; no se espera haz", "grey"))
    for i, (t, d, k) in enumerate(cols):
        x = 10 + i * (w + gap)
        bx(f, x, y + 6, w, 40, t, "navy", 14, True)
        bx(f, x, y + 62, w, 90, d, k)
    f.text(10, y + 178, "Las tres posiciones las informan tres microinterruptores como un número de 3 bits que lee el computador.", 13, "start", 400)
    bx(f, 10, y + 198, 440, 78, "Falla 1 (columna de rayos X): haz de rayos X sin aplanador en su sitio, con corriente alta. Es el riesgo básico de una máquina de dos modos.", "coral")
    bx(f, 480, y + 198, 450, 78, "Falla 2 (columnas de electrones y luz de campo): haz de electrones de energía plena sin barrido, o con la plataforma en luz de campo: un haz estrecho y muy intenso.", "coral")
    return done(f, y + 296, "En máquinas anteriores, interlocks electromecánicos aseguraban la posición. En la Therac-25, comprobaciones de software sustituyeron a muchos de esos interlocks. La figura describe la geometría de la máquina según Leveson y Turner; no es un plano ni un valor de ingeniería.", "gold")


# ------------------------------------------------------------------ 3. ventana de ocho segundos
def ventana_de_ocho_segundos() -> Fig:
    return timeline(
        "La edición dentro de la ventana de 8 segundos que el software no vigilaba",
        "Línea de tiempo esquemática de 0 a 10 segundos. El software ajusta los imanes durante unos 8 segundos. La rutina Ptime comprueba si hay ediciones solo en su primera ejecución y luego borra la bandera. Si el operador teclea el modo, sube el cursor, cambia el modo y vuelve a la línea de comandos dentro de esos 8 segundos, la entrada de datos termina sin detectar el cambio y el haz queda ajustado con parámetros inconsistentes.",
        [
            ("Software: ajuste de imanes", [(0, 8, "Magnet y Ptime ajustan los imanes (unos 8 s)", "gold")]),
            ("Ptime: ¿hay ediciones?", [(0, 1, "", "navy"), (1, 8, "no vuelve a mirar", "grey")]),
            ("Operador", [(0, 2, "teclea x", "grey"), (2, 6, "sube y cambia a e", "coral"), (6, 7, "vuelve", "grey")]),
            ("Resultado", [(8, 10, "inconsistente", "coral")]),
        ],
        unit="segundos desde que se completa la entrada de datos (esquemático)",
        events=[(8, "fin del ajuste")],
        t_max=10, ticks=[0, 2, 4, 6, 8, 10], lane_h=50, label_w=250,
        note="Documentado: unos 8 segundos de ajuste, una comprobación de ediciones solo en la primera pasada y que un operador experimentado, al editar rápido, producía Malfunction 54 con sobredosis. Esquemático: el reparto del tiempo del operador no es una medición.",
        foot="Fuente: Leveson y Turner (1993), descripción del código de entrada de datos de AECL. Los tramos del operador son ilustrativos.")


# ------------------------------------------------------------------ 4. cronología
def cronologia() -> Fig:
    return timeline(
        "Veinticinco meses entre el primer accidente y el plan correctivo final",
        "Línea de tiempo en meses desde enero de 1985. Seis accidentes: Marietta en junio de 1985, Hamilton en julio de 1985, Yakima en diciembre de 1985, Tyler en marzo y abril de 1986 y Yakima en enero de 1987. AECL presenta el primer plan de acción correctiva el 13 de junio de 1986 y el quinto y último el 21 de julio de 1987. El uso rutinario se suspende de febrero a agosto de 1987.",
        [
            ("1 Marietta, 3 jun 1985", [(5.07, 5.6, "", "coral")]),
            ("2 Hamilton, 26 jul 1985", [(6.83, 7.4, "", "coral")]),
            ("3 Yakima, dic 1985", [(11.3, 11.9, "", "coral")]),
            ("4 Tyler, 21 mar 1986", [(14.67, 15.2, "", "coral")]),
            ("5 Tyler, 11 abr 1986", [(15.33, 15.9, "", "coral")]),
            ("6 Yakima, 17 ene 1987", [(24.53, 25.1, "", "coral")]),
            ("Plan correctivo de AECL", [(17.4, 30.67, "cinco revisiones del plan", "gold")]),
            ("Uso rutinario suspendido", [(25.63, 32.5, "hasta ago 1987", "navy")]),
        ],
        unit="meses desde enero de 1985 (12 = enero de 1986, 24 = enero de 1987)",
        events=[(16.03, "2 may 1986: FDA declara el defecto"), (30.67, "21 jul 1987: plan final")],
        t_max=36, ticks=[0, 6, 12, 18, 24, 30, 36], lane_h=38, label_w=210,
        note="Cada marca coral es un accidente con una sobredosis masiva documentada. Que pasaran meses y varios accidentes antes de que se reconociera un defecto de la máquina es lo que Leveson y Turner vinculan a la falta de seguimiento de incidentes (interpretación de los autores). Los meses son cálculo propio a partir de las fechas del artículo.",
        foot="Fuente: Leveson y Turner (1993). La fecha de Yakima 1985 es aproximada: el artículo la sitúa en diciembre.")


# ------------------------------------------------------------------ 5. dosis
def dosis() -> Fig:
    return percentile_intervals(
        "Dosis estimadas en cinco accidentes frente a una sesión típica de unos 200 rad",
        "Rangos en escala logarítmica de las dosis estimadas en cinco accidentes, en rad, con dos líneas de referencia en 200 y 1.000. Marietta, de 15.000 a 20.000; Hamilton, de 13.000 a 17.000; Tyler en marzo, de 16.500 a 25.000 según simulaciones; Tyler en abril, de más de 4.000 medidos en el hospital a unos 25.000 medidos por AECL; Yakima 1987, de 8.000 a 10.000 tras dos intentos. Una sesión típica ronda los 200 rad.",
        [
            ("Marietta, 1985", [15000, 20000]),
            ("Hamilton, 1985", [13000, 17000]),
            ("Tyler, mar 1986", [16500, 25000]),
            ("Tyler, abr 1986", [4000, 25000]),
            ("Yakima, ene 1987", [8000, 10000]),
        ],
        unit="rad (dosis localizada)", marks=("mínimo estimado", "máximo estimado"), log=True,
        ref_lines=[(200, "≈200 rad"), (1000, "1.000 rad")],
        note="Son estimaciones posteriores y localizadas; no son lecturas de la máquina, que no detectó la sobredosis. Los 1.000 rad que se citan como potencialmente letales lo son para el cuerpo entero; aquí la dosis se concentró en una zona pequeña. Se muestra el orden de magnitud, no una dosis exacta.",
        foot="Fuente: Leveson y Turner (1993). Las dosis exactas no pueden determinarse; varían entre simulaciones de distintos centros.")


# ------------------------------------------------------------------ 6. capas
def capas_de_proteccion() -> Fig:
    f, y = sketch("De una barrera de software a capas independientes entre la orden y el haz",
                  "Dos recorridos entre la orden del operador y el haz. Antes, una sola barrera: las comprobaciones de software, que podían fallar por una condición de carrera. Después del plan correctivo de 1987, capas separadas: interlock y potenciómetro de la plataforma giratoria, circuito de hardware que corta tras un pulso alto sin pasar por el software, suspensión obligatoria ante fallos de dosimetría con reingreso de parámetros, mensajes comprensibles y pedal de hombre muerto.")
    f.text(14, y + 18, "Antes (versión de los accidentes)", 14, "start", 700, "#5c1f14")
    bx(f, 10, y + 30, 200, 58, "Orden del operador", "plain")
    bx(f, 270, y + 30, 400, 58, "Software: la única barrera. Un fallo lo cruza sin que nada lo detenga.", "coral")
    bx(f, 730, y + 30, 200, 58, "Haz sobre el paciente", "coral")
    f.arrow([(210, y + 59), (270, y + 59)])
    f.arrow([(670, y + 59), (730, y + 59)], "", True, "#c0432f")
    f.text(14, y + 122, "Después (plan correctivo final, 21 de julio de 1987)", 14, "start", 700, "#0b3f45")
    bx(f, 10, y + 134, 150, 78, "Orden del operador", "plain")
    caps = ("Software con más comprobaciones", "Interlock y potenciómetro de la plataforma", "Circuito que corta tras un pulso alto, sin software")
    for i, t in enumerate(caps):
        bx(f, 196 + i * 196, y + 134, 176, 78, t, "teal")
        f.arrow([(160 + i * 196 if i == 0 else 172 + i * 196, y + 173), (196 + i * 196, y + 173)])
    bx(f, 784, y + 134, 146, 78, "Haz sobre el paciente", "navy")
    f.arrow([(772, y + 173), (784, y + 173)])
    bx(f, 10, y + 232, 300, 66, "Fallos de dosimetría: suspensión; reingreso de parámetros", "plain")
    bx(f, 328, y + 232, 300, 66, "Mensajes comprensibles en lugar de «Malfunction 54»", "plain")
    bx(f, 646, y + 232, 284, 66, "Pedal de hombre muerto para movimientos", "plain")
    return done(f, y + 314, "Las capas listadas son las del plan correctivo final según el artículo; que cada una sea suficiente es una valoración de los autores y de la FDA. La enseñanza para el curso es de arquitectura: ningún camino al daño debe depender de un único componente, y menos de uno que no se pueda verificar con pruebas.", "gold")


FIGURES = {
    "therac-25-tres-maquinas.svg": tres_maquinas,
    "therac-25-plataforma-giratoria.svg": plataforma_giratoria,
    "therac-25-ventana-de-ocho-segundos.svg": ventana_de_ocho_segundos,
    "therac-25-cronologia.svg": cronologia,
    "therac-25-dosis-estimadas.svg": dosis,
    "therac-25-capas-de-proteccion.svg": capas_de_proteccion,
}
