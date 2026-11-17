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



# ==== EXPANDED FIGURES (begin) ====

# ------------------------------------------------------------------ 7. canales de información
def canales_de_informacion() -> Fig:
    f, y = sketch("Quién podía saber qué: el fabricante recibía cada historia y ningún centro conocía las otras",
                  "Diagrama de actores y canales. Cuatro hospitales envían llamadas y cartas al fabricante. El fabricante informa a la FDA tras Tyler y la FDA declara el defecto. La asociación de físicos y las reuniones de usuarios conectan a los centros con el fabricante. Los hospitales no tenían obligación de notificar al regulador ni canal para compartir incidentes entre sí.")
    hosp = ["Marietta, 1985", "Hamilton, 1985", "Yakima, 1985 y 1987", "Tyler, 1986"]
    for i, h in enumerate(hosp):
        x = 10 + i * 232
        bx(f, x, y + 6, 214, 50, h, "plain")
        f.line(x + 107, y + 56, x + 107, y + 86, "#32505f")
    f.line(117, y + 86, 817, y + 86, "#32505f")
    f.arrow([(437, y + 86), (437, y + 130)], "llamadas y cartas", label_at=(450, y + 112), label_anchor="start")
    bx(f, 310, y + 130, 250, 64, "AECL, el fabricante: ve cada incidente por separado", "gold", 13, bold=True)
    bx(f, 10, y + 130, 200, 64, "Asociación de físicos y reuniones de usuarios", "teal", 13)
    f.arrow([(210, y + 162), (310, y + 162)], "desde 1986", label_at=(260, y + 154))
    bx(f, 700, y + 130, 230, 64, "FDA de EE. UU.", "navy", 13, bold=True)
    f.arrow([(560, y + 150), (700, y + 150)], "15 abr 1986", label_at=(630, y + 142))
    f.arrow([(700, y + 178), (560, y + 178)], "2 may 1986", label_at=(630, y + 196))
    bx(f, 700, y + 240, 230, 56, "Autoridad sanitaria de Canadá", "navy", 13)
    f.arrow([(437, y + 194), (437, y + 268), (700, y + 268)], dashed=True)
    bx(f, 10, y + 240, 330, 56, "Entre hospitales no había canal: se enteraban por conversaciones informales", "coral", 13)
    bx(f, 10, y + 320, 920, 56, "No existía obligación de notificar incidentes del hospital al fabricante ni a la FDA hasta la enmienda legal de 1990", "coral", 13)
    return done(f, y + 392, "Las flechas sólidas son flujos documentados; las punteadas, flujos que faltaban o llegaron tarde. El fabricante era el único que veía varias historias a la vez y respondió a los centros que no conocía otros incidentes.")


# ------------------------------------------------------------------ 8. hardware
def arquitectura_de_hardware() -> Fig:
    f, y = sketch("Hardware en dos salas: lo que el operador veía y lo que ocurría detrás del blindaje",
                  "Dos zonas separadas por un blindaje. En la sala de control, el operador, un terminal VT100 y el computador PDP-11/23 de 32 KB. En la sala de tratamiento, el acelerador, los imanes de barrido, la plataforma giratoria con tres microinterruptores, las cámaras de ionización, el paciente y el sistema de interlocks de hardware. Entre ambas, solo un monitor de vídeo y un intercomunicador.")
    f.group(10, y, 300, 290, "Sala de control", "grey")
    bx(f, 26, y + 40, 268, 56, "Operador", "plain")
    bx(f, 26, y + 116, 268, 56, "Terminal VT100", "plain")
    bx(f, 26, y + 196, 268, 70, "Computador PDP-11/23 con 32 KB: lee sensores y comanda actuadores", "gold")
    f.arrow([(160, y + 96), (160, y + 116)])
    f.arrow([(160, y + 172), (160, y + 196)])
    f.box(326, y + 10, 40, 270, "", "grey")
    f.text(346, y + 306, "blindaje", 13, "middle", 700)
    f.group(382, y, 548, 290, "Sala de tratamiento", "grey")
    cells = [("Acelerador: electrones de 5 a 25 MeV", "plain"), ("Imanes de barrido y de flexión", "plain"),
             ("Plataforma giratoria con tres microinterruptores", "teal"), ("Cámaras de ionización que miden el haz", "teal"),
             ("Paciente sobre la mesa", "plain"), ("Interlocks de hardware: retiran la alimentación ante una falla", "coral")]
    for i, (t, k) in enumerate(cells):
        r, c = divmod(i, 2)
        bx(f, 398 + c * 267, y + 40 + r * 80, 252, 66, t, k, 13)
    f.arrow([(310, y + 224), (382, y + 224)], "órdenes", label_at=(346, y + 216))
    f.arrow([(382, y + 256), (310, y + 256)], "lecturas", label_at=(346, y + 276))
    bx(f, 10, y + 326, 920, 56, "Entre las salas: un monitor de vídeo y un intercomunicador. Ninguna vista del estado interno de la máquina.", "gold", 13)
    return done(f, y + 400, "Los bloques teal son los que decidían qué haz recibía el paciente y cuánto se medía. El computador era el único enlace entre lo que el operador pedía y lo que ocurría en la sala.")


# ------------------------------------------------------------------ 9. posiciones de la plataforma
def posiciones_de_la_plataforma() -> Fig:
    f, y = sketch("Tres bits, tres posiciones legales: lo que el software debía comprobar y un interlock podía imponer",
                  "Las ocho combinaciones de tres microinterruptores de la plataforma giratoria. Solo tres son posiciones legales: electrones, rayos X y luz de campo. Las otras cinco, incluida la de ningún interruptor pulsado, son posiciones intermedias o inválidas en las que el plan final impide el haz.")
    heads = ["Electrones", "Rayos X", "Luz de campo"]
    for i, h in enumerate(heads):
        f.text(60 + i * 100, y + 18, h, 13, "middle", 700)
    combos = [((0, 0, 0), "Ningún interruptor: posición intermedia", "coral"), ((1, 0, 0), "Electrones: posición legal", "teal"),
              ((0, 1, 0), "Rayos X: posición legal", "teal"), ((0, 0, 1), "Luz de campo: sin haz esperado", "teal"),
              ((1, 1, 0), "Dos pulsados: inválida", "coral"), ((1, 0, 1), "Dos pulsados: inválida", "coral"),
              ((0, 1, 1), "Dos pulsados: inválida", "coral"), ((1, 1, 1), "Tres pulsados: inválida", "coral")]
    for r, (bits, label, k) in enumerate(combos):
        cy = y + 40 + r * 46
        for i, b in enumerate(bits):
            fill = "#102a43" if b else "#ffffff"
            f.parts.append(f'<circle cx="{60 + i * 100}" cy="{cy + 18}" r="13" fill="{fill}" stroke="#102a43" stroke-width="2"/>')
        bx(f, 350, cy, 400, 38, label, k, 13)
    bx(f, 770, y + 40, 160, 120, "Plan final: interlock de hardware y potenciómetro que muestra la posición exacta", "teal", 13)
    bx(f, 770, y + 180, 160, 100, "Sin haz si la plataforma está en luz de campo o entre posiciones", "gold", 13)
    return done(f, y + 420, "Círculo lleno: microinterruptor pulsado. Cinco de ocho combinaciones deben rechazarse. Es un esquema del principio y no un mapa mecánico: las combinaciones físicamente posibles dependen del diseño real.")


# ------------------------------------------------------------------ 10. software
def arquitectura_de_software() -> Fig:
    f, y = sketch("Arquitectura de software: tareas que solo hablan por variables compartidas",
                  "Planificador que lanza tareas cada 0,1 segundos. Tareas críticas: monitor de tratamiento, servos y ama de llaves. Tareas no críticas: procesador de teclado, pantalla, suma de verificación y otras. Servicios de interrupción. En la franja inferior, las variables compartidas sin sincronización real: fase del monitor, desplazamiento de modo y energía, marca de entrada completa y contador de verificación del colimador.")
    bx(f, 10, y + 6, 920, 50, "Planificador expropiativo en ensamblador de PDP-11: lanza las tareas cada 0,1 segundos; primero las críticas", "navy", 13, bold=True)
    f.group(10, y + 76, 300, 200, "Tareas críticas", "grey")
    bx(f, 24, y + 108, 272, 48, "Monitor de tratamiento: ocho fases", "coral", 13)
    bx(f, 24, y + 164, 272, 48, "Servos: haz, dosis, imanes", "coral", 13)
    bx(f, 24, y + 220, 272, 44, "Ama de llaves: interlocks y límites", "coral", 13)
    f.group(330, y + 76, 300, 200, "Tareas no críticas", "grey")
    bx(f, 344, y + 108, 272, 48, "Procesador de teclado de la consola", "gold", 13)
    bx(f, 344, y + 164, 272, 48, "Pantalla, suma de verificación, snapshot", "plain", 13)
    bx(f, 344, y + 220, 272, 44, "Control manual y calibración", "plain", 13)
    f.group(650, y + 76, 280, 200, "Servicios de interrupción", "grey")
    bx(f, 664, y + 108, 252, 156, "Reloj, barrido, teclados, pantalla, impresora, arranque y trampas de desbordamiento", "plain", 13)
    f.group(10, y + 296, 920, 118, "Variables compartidas: sin sincronización real entre quien escribe y quien lee", "navy")
    names = ["Tphase: fase del monitor", "MEOS: modo y energía, 2 bytes", "Marca de entrada completa", "Class3: 1 byte, verificación del colimador"]
    for i, n in enumerate(names):
        bx(f, 24 + i * 226, y + 336, 214, 64, n, "coral" if i in (1, 3) else "gold", 13)
    for x in (160, 480, 790):
        f.arrow([(x, y + 276), (x, y + 296)], dashed=True)
    return done(f, y + 430, "Los nombres son los que usa el artículo; el código de AECL no es público y la figura simplifica. Las dos cajas coral de la franja inferior son las variables implicadas en los accidentes de Tyler y de Yakima de 1987.")


# ------------------------------------------------------------------ 11. secuencia de Tyler
def secuencia_de_tyler() -> Fig:
    f, y = sketch("Secuencia de la edición rápida: la marca de entrada completa llega antes que la corrección",
                  "Diagrama de secuencia con cuatro líneas de vida: operador, procesador de teclado, rutina de entrada de datos con el ajuste de imanes y la máquina. El operador teclea X y va a la línea de comandos; el teclado marca la entrada como completa; el ajuste de imanes comienza con X y dura unos 8 segundos; dentro de esa ventana el operador corrige a E; el modo y la energía cambian pero el ajuste no vuelve a comprobar ediciones; el haz se enciende con la plataforma en electrones y los parámetros de rayos X.")
    xs = [110, 330, 580, 830]
    names = ["Operador", "Procesador de teclado", "Entrada de datos y ajuste de imanes", "Máquina"]
    for x, n in zip(xs, names):
        bx(f, x - 100, y, 200, 50, n, "navy", 13, bold=True)
        f.line(x, y + 50, x, y + 640, "#8a9aa3", dashed=True)
    def msg(yy, a, b, text, color="#32505f"):
        f.arrow([(xs[a], y + yy), (xs[b], y + yy)], color=color)
        f.text((xs[a] + xs[b]) / 2, y + yy - 22, text, 13, "middle", 400)
    msg(104, 0, 1, "1  teclea X y baja\na la línea de comandos")
    msg(172, 1, 2, "2  marca la entrada\ncomo completa")
    msg(240, 2, 3, "3  ajusta imanes con X\n(unos 8 segundos)")
    msg(308, 0, 1, "4  sube el cursor y corrige\na E dentro de esos 8 s", "#c0432f")
    bx(f, xs[1] - 100, y + 324, 200, 66, "5  el byte bajo de MEOS pasa a E; el alto sigue en X", "coral", 13)
    bx(f, xs[2] - 100, y + 410, 200, 66, "6  la espera ya no mira ediciones: nadie detecta el cambio", "coral", 13)
    msg(520, 0, 3, "7  pulsa B: haz encendido", "#c0432f")
    bx(f, xs[3] - 100, y + 540, 200, 80, "8  plataforma en electrones con parámetros de rayos X", "coral", 13)
    return done(f, y + 660, "La comprobación de ediciones se hacía en un punto del tiempo y no de forma continua. Los tiempos entre teclas no constan en el artículo; solo la ventana de unos 8 segundos.")


# ------------------------------------------------------------------ 12. dos órdenes de eventos
def dos_ordenes_de_eventos() -> Fig:
    return timeline(
        "La misma secuencia de teclas, dos resultados: solo importa el momento de la edición",
        "Dos pares de carriles en una escala de 0 a 12 segundos. En el orden seguro el operador edita antes de que comience el ajuste de imanes y la máquina se reconfigura. En el orden peligroso, el ajuste de imanes dura unos 8 segundos y el operador edita dentro de esa ventana, después de la primera comprobación, y la máquina queda inconsistente.",
        [
            ("Seguro: operador", [(0, 1.8, "edita", "teal")]),
            ("Seguro: ajuste de imanes", [(2.2, 10.2, "ajuste de unos 8 s", "grey")]),
            ("Peligroso: operador", [(4, 5.8, "edita", "coral")]),
            ("Peligroso: ajuste de imanes", [(0.5, 8.5, "ajuste de unos 8 s", "grey")]),
        ],
        unit="segundos (esquema ilustrativo)",
        events=[(8.5, "fin del ajuste (peligroso)")],
        t_max=12, ticks=[0, 2, 4, 6, 8, 10, 12], lane_h=52, label_w=250,
        note="El resultado depende solo del instante de la edición respecto de la ventana de unos 8 segundos. Solo ese tope es un dato del artículo; los instantes son ilustrativos y no se estima la probabilidad de cada orden.",
        foot="Fuente: Leveson y Turner, IEEE Computer 26(7), 1993; esquema propio.")


# ------------------------------------------------------------------ 13. contador de un byte
def contador_de_un_byte() -> Fig:
    f, y = sketch("Un contador de un byte: una de cada 256 pasadas la comprobación del colimador no se ejecutaba",
                  "Fila de casillas que representan pasadas por la rutina de preparación. Las pasadas 1 a 255 dejan la variable Class3 distinta de cero y activan la comprobación del colimador. En la pasada 256 el contador vuelve a cero y la comprobación se omite. Si el operador confirma en ese instante, el haz de 25 MeV se enciende con el colimador en posición de luz de campo.")
    labels = ["1", "2", "3", "4", "…", "254", "255", "256"]
    w, g = 100, 15
    for i, t in enumerate(labels):
        x = 10 + i * (w + g)
        bx(f, x, y + 8, w, 50, t if i < 7 else "256 = 0", "teal" if i < 7 else "coral", 13, bold=True)
    f.text(480, y + 82, "Pasadas por la rutina de preparación; Class3 se incrementa en cada una", 13, "middle", 400)
    bx(f, 10, y + 110, 440, 70, "Class3 distinta de cero: Lmtchk llama a Chkcol y se comprueba la posición del colimador", "teal", 13)
    bx(f, 490, y + 110, 440, 70, "Class3 igual a cero: se omite Chkcol; la falta de luz de campo no se detecta", "coral", 13)
    f.arrow([(230, y + 58), (230, y + 110)])
    f.arrow([(710, y + 58), (710, y + 110)], color="#c0432f")
    bx(f, 490, y + 210, 440, 76, "Si el operador pulsa la tecla de ajuste en esa pasada: haz de 25 MeV sin blanco ni barrido", "coral", 13, bold=True)
    f.arrow([(710, y + 180), (710, y + 210)], color="#c0432f")
    bx(f, 10, y + 210, 440, 76, "Corrección de AECL: asignar a Class3 un valor fijo distinto de cero en cada pasada, en vez de incrementarla", "gold", 13)
    return done(f, y + 306, "La comprobación no falló: no se ejecutó. La preparación se ejecuta varios cientos de veces por puesta a punto; la probabilidad de coincidir con la pasada 256 no se puede estimar con los datos del artículo.")


# ------------------------------------------------------------------ 14. defensa en profundidad
def defensa_en_profundidad() -> Fig:
    f, y = sketch("Once barreras entre un error de diseño y un paciente: casi ninguna cumplió su papel",
                  "Once barreras en tres filas: análisis de peligros, interlocks de hardware, diseño de software, pruebas, mensajes de error, dosimetría, observación del operador, procedimiento ante pausas, investigación de incidentes, vigilancia del regulador y el plan final de 1987. Cada barrera indica si existió y si funcionó según Leveson y Turner.")
    cells = [
        ("1 Análisis de peligros, 1983", "Excluyó el software; probabilidades sin justificación", "coral"),
        ("2 Interlocks de hardware", "Sustituidos en parte por comprobaciones de software", "coral"),
        ("3 Diseño del software", "Variables compartidas sin sincronización", "coral"),
        ("4 Pruebas", "Casi solo de sistema; sin plan de pruebas documentado", "coral"),
        ("5 Mensajes de error", "Malfunction y un número que el manual no explicaba", "coral"),
        ("6 Dosimetría", "Cámaras saturadas mostraron una dosis baja", "coral"),
        ("7 Observación del operador", "Solo vídeo e intercomunicador; el paciente era la señal", "grey"),
        ("8 Procedimiento ante pausas", "Pulsar P y continuar era lo habitual", "coral"),
        ("9 Investigación de incidentes", "Sin seguimiento; respuesta de que era imposible", "coral"),
        ("10 Vigilancia del regulador", "Sin aviso obligatorio de los hospitales hasta 1990", "grey"),
        ("11 Plan final de 1987", "Hardware independiente, suspensión y mensajes claros", "teal"),
    ]
    w, g = 224, 12
    for i, (t, r, k) in enumerate(cells):
        row, col = divmod(i, 4)
        x = 10 + col * (w + g)
        yy = y + 8 + row * 190
        bx(f, x, yy, w, 58, t, "plain", 13, bold=True)
        bx(f, x, yy + 62, w, 100, r, k, 13)
    return done(f, y + 8 + 3 * 190, "Coral: no existió o no funcionó. Gris: existía pero no cubría este riesgo (valoración de Leveson y Turner). Teal: añadida por el plan final de julio de 1987. Que fallaran por razones distintas es lo que impide atribuir el caso a una sola causa.")


# ------------------------------------------------------------------ 15. plan correctivo por causa
def plan_correctivo_por_causa() -> Fig:
    f, y = sketch("Del plan final de 1987 a las causas: qué medida corta qué eslabón",
                  "Dos columnas unidas por flechas. A la izquierda, siete causas documentadas: software como única barrera, edición rápida, contador de un byte, dosimetría saturada, pausas normalizadas, mensajes crípticos, ausencia de registro y notificación. A la derecha, seis medidas del plan final: circuito de hardware de un pulso, interlock y potenciómetro de la plataforma, límite de teclas de edición, suspensión con reingreso de parámetros, mensajes claros y otros cambios de software. Las flechas asocian cada causa con las medidas que la cortan; la última causa no recibe flecha.")
    causes = ["Software como única barrera", "Edición rápida deja parámetros inconsistentes", "Contador de un byte omite la comprobación",
              "Dosimetría saturada: dosis aparente baja", "Pausas normalizadas", "Mensajes crípticos", "Sin registro de auditoría ni notificación"]
    meas = ["Circuito de hardware: corta tras un pulso alto", "Interlock y potenciómetro de la plataforma", "Teclas de edición limitadas",
            "Fallos de dosimetría suspenden; reingreso de parámetros", "Mensajes claros y manuales", "Otros 23 cambios de software"]
    step = 62
    for i, c in enumerate(causes):
        bx(f, 10, y + 6 + i * step, 330, 52, c, "coral" if i < 6 else "gold", 13)
    for i, m in enumerate(meas):
        bx(f, 600, y + 6 + i * step, 330, 52, m, "teal", 13)
    links = [(0, 0), (0, 1), (1, 2), (2, 5), (3, 0), (3, 3), (4, 3), (5, 4)]
    for c, m in links:
        f.arrow([(340, y + 32 + c * step), (600, y + 32 + m * step)])
    return done(f, y + 6 + 7 * step + 6, "La causa sin flecha, el registro de auditoría y la notificación, se atendió por otras vías: la reunión de usuarios pidió el registro y el fabricante alegó límites de memoria; la notificación obligatoria llegó con la ley de 1990.")


# ------------------------------------------------------------------ 16. bucle de pausas
def bucle_de_pausas() -> Fig:
    f, y = sketch("El bucle de pausas: cada pausa inocua refuerza el hábito que vuelve peligrosa la pausa grave",
                  "Diagrama de lazo con seis estados. Una pausa inocua frecuente lleva al operador a pulsar P de inmediato; no pasa nada y el hábito se confirma; la atención a cada mensaje baja; un mensaje de fallo grave se trata igual; resulta una sobredosis con una dosis aparente baja. Una flecha de refuerzo vuelve del hábito al inicio.")
    top = [("A  Pausa inocua frecuente, por ejemplo por baja tasa de dosis", "plain"), ("B  El operador pulsa P para continuar", "gold"), ("C  No pasa nada: P parece seguro", "gold")]
    for i, (t, k) in enumerate(top):
        x = 10 + i * 316
        bx(f, x, y + 10, 296, 70, t, k, 13)
        if i:
            f.arrow([(x - 20, y + 45), (x, y + 45)])
    f.arrow([(778, y + 80), (778, y + 140)])
    bot = [("D  Menos atención a cada mensaje", "gold"), ("E  Un mensaje de fallo grave se trata igual", "coral"), ("F  Sobredosis con dosis aparente baja", "coral")]
    for i, (t, k) in enumerate(bot):
        x = 10 + (2 - i) * 316
        bx(f, x, y + 140, 296, 70, t, k, 13)
        if i:
            f.arrow([(x + 316, y + 175), (x + 296, y + 175)])
    f.arrow([(326 + 148, y + 140), (326 + 148, y + 80)], "refuerza el hábito", dashed=True, label_at=(490, y + 118), label_anchor="start")
    return done(f, y + 230, "Cada paso es razonable con la información del operador. Hasta cinco pausas seguidas eran posibles antes de una suspensión. Es un modelo didáctico de lo que el artículo describe; no mide la frecuencia de cada paso.")


# ------------------------------------------------------------------ 17. revisiones del plan
def revisiones_del_plan() -> Fig:
    return timeline(
        "Catorce meses y cinco revisiones: de la declaración de defecto al plan final",
        "Línea de tiempo en meses desde el 1 de mayo de 1986 hasta agosto de 1987 con carriles para el fabricante, el regulador, el uso restringido y el segundo accidente de Yakima. El fabricante presenta el plan en junio de 1986 y revisiones en noviembre, diciembre, marzo, mayo y julio de 1987. El regulador responde en julio, octubre, diciembre, abril y mayo. El uso queda restringido de febrero a agosto de 1987.",
        [
            ("Fabricante: planes", [(1.4, 1.7, "", "navy"), (6.4, 6.7, "", "navy"), (7.7, 8.0, "", "navy"), (10.1, 10.4, "", "navy"), (12.0, 12.3, "", "navy"), (14.7, 15.0, "", "navy")]),
            ("Regulador: respuestas", [(2.7, 3.0, "", "gold"), (5.9, 6.2, "", "gold"), (7.3, 7.6, "", "gold"), (11.3, 11.6, "", "gold"), (12.8, 13.1, "", "gold")]),
            ("Uso restringido", [(9.7, 16, "restricción del uso rutinario", "coral")]),
            ("Accidente", [(8.6, 8.9, "", "coral")]),
        ],
        unit="meses desde el 1 de mayo de 1986",
        events=[(0, "2 may 1986: defecto"), (14.7, "21 jul 1987")],
        t_max=16, ticks=[0, 2, 4, 6, 8, 10, 12, 14, 16], lane_h=48, label_w=200,
        note="Cada marca del fabricante es un envío del plan (junio de 1986 y revisiones 1 a 5 en las fechas del artículo); cada marca del regulador, una respuesta pidiendo más información. La barra coral va de febrero a agosto de 1987. Meses: cálculo propio.",
        foot="Fuente: Leveson y Turner, IEEE Computer 26(7), 1993; fechas del artículo.")


# ------------------------------------------------------------------ 18. árbol de fallas
def arbol_de_fallas() -> Fig:
    f, y = sketch("Árbol de fallas: una sobredosis exige tres condiciones a la vez",
                  "Árbol de fallas. El evento superior es una sobredosis a un paciente y requiere, con compuerta Y, tres ramas: el haz se enciende en una configuración peligrosa, la máquina no detecta la sobredosis y el procedimiento permite continuar. La primera rama es una compuerta O con tres hojas: carrera de edición, contador de un byte y ausencia de interlocks de hardware. La segunda tiene dos hojas y la tercera tres.")
    bx(f, 320, y + 4, 300, 56, "Sobredosis a un paciente", "navy", 14, bold=True)
    f.line(470, y + 60, 470, y + 84)
    f.dot(470, y + 96, "Y")
    f.line(155, y + 112, 785, y + 112)
    for x in (155, 470, 785):
        f.line(x, y + 112, x, y + 130)
    bx(f, 10, y + 130, 290, 60, "El haz se enciende en una configuración peligrosa", "plain", bold=True)
    bx(f, 325, y + 130, 290, 60, "La máquina no detecta la sobredosis", "plain", bold=True)
    bx(f, 640, y + 130, 290, 60, "El procedimiento permite continuar", "plain", bold=True)
    for x in (155, 470, 785):
        f.line(x, y + 190, x, y + 206)
    f.dot(155, y + 218, "O")
    f.dot(470, y + 218, "Y")
    f.dot(785, y + 218, "O")
    leaves = [
        (10, [("Carrera de edición (documentado)", "coral"), ("Contador de un byte (documentado)", "coral"), ("Sin interlocks de hardware independientes (documentado)", "coral")]),
        (325, [("Cámaras saturadas muestran dosis baja (documentado)", "coral"), ("Sin registro de auditoría ni verificación independiente (documentado)", "coral")]),
        (640, [("Pausa con tecla P como rutina (documentado)", "coral"), ("Mensajes sin explicar (documentado)", "coral"), ("Causa atribuida a otro componente sin evidencia (documentado)", "coral")]),
    ]
    for x, items in leaves:
        cy = y + 244
        f.line(x + 145, y + 230, x + 145, y + 244)
        for t, k in items:
            bx(f, x, cy, 290, 58, t, k)
            cy += 70
    return done(f, y + 244 + 70 * 3 + 6, "En las ramas de los lados basta una causa (compuerta O); en la central hacen falta las dos (compuerta Y). Eliminar una de las tres ramas principales evita el evento superior. Sin probabilidades: el artículo critica justamente las cifras sin método.")

# ==== EXPANDED FIGURES (end) ====

FIGURES = {
    "therac-25-tres-maquinas.svg": tres_maquinas,
    "therac-25-plataforma-giratoria.svg": plataforma_giratoria,
    "therac-25-ventana-de-ocho-segundos.svg": ventana_de_ocho_segundos,
    "therac-25-cronologia.svg": cronologia,
    "therac-25-dosis-estimadas.svg": dosis,
    "therac-25-capas-de-proteccion.svg": capas_de_proteccion,
    # expanded entries
    "therac-25-canales-de-informacion.svg": canales_de_informacion,
    "therac-25-arquitectura-de-hardware.svg": arquitectura_de_hardware,
    "therac-25-posiciones-de-la-plataforma.svg": posiciones_de_la_plataforma,
    "therac-25-arquitectura-de-software.svg": arquitectura_de_software,
    "therac-25-secuencia-de-tyler.svg": secuencia_de_tyler,
    "therac-25-dos-ordenes-de-eventos.svg": dos_ordenes_de_eventos,
    "therac-25-contador-de-un-byte.svg": contador_de_un_byte,
    "therac-25-defensa-en-profundidad.svg": defensa_en_profundidad,
    "therac-25-plan-correctivo-por-causa.svg": plan_correctivo_por_causa,
    "therac-25-bucle-de-pausas.svg": bucle_de_pausas,
    "therac-25-revisiones-del-plan.svg": revisiones_del_plan,
    "therac-25-arbol-de-fallas.svg": arbol_de_fallas,
}
