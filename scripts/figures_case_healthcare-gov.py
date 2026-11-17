"""Figures for the failure case study HealthCare.gov (launch of 1 October 2013).

Numbers come from GAO-14-694 (July 2014), GAO-15-238 (March 2015), the HHS OIG case study OEI-06-14-00350 and the
CMS progress report of 1 December 2013, as each footer says. Output goes to ``casos/figures/``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_helpers_fallo import equi_axis, sequence, slices  # noqa: E402
from figure_cases import case_cards  # noqa: E402
from figure_kit import Fig, _kit_finish, _kit_start, _wrap, dumbbell, line_chart, timeline  # noqa: E402

GAO14 = "Fuente: GAO-14-694 (julio de 2014)."
ANALISIS = "Análisis propio apoyado en GAO-14-694, GAO-15-238 y OEI-06-14-00350; no es una conclusión de esas fuentes."


def sketch(title: str, desc: str, width: int = 940):
    return _kit_start(title, desc, width, None)


def bx(f: Fig, x: float, y: float, w: float, h: float, text: str, kind: str = "plain", size: int = 13, bold: bool = False) -> None:
    lines = _wrap(text, size, w - 20)
    assert len(lines) * size * 1.28 <= h - 6, f"box overflows: {text!r} ({len(lines)} lines in {h}px)"
    f.box(x, y, w, h, text, kind, size, bold=bold)


def done(f: Fig, y: float, note: str, kind: str = "gold", foot: str = "") -> Fig:
    _kit_finish(f, y, note, kind, foot)
    f.kind = "diagram"
    return f


# ------------------------------------------------------------------ 1. contexto
def contexto() -> Fig:
    f, y = sketch("Quién construyó qué: un mercado federal armado con contratistas y varias agencias",
                  "Diagrama de contexto: los ciudadanos usan el sitio Healthcare.gov; detrás está el mercado federal FFM, desarrollado por un contratista bajo CMS, que consulta el centro de servicios de datos federal, desarrollado por otro contratista, para verificar a los solicitantes con fuentes federales; las aseguradoras reciben las inscripciones.")
    y0 = y + 4
    bx(f, 10, y0 + 40, 170, 80, "Consumidores que comparan y eligen un plan", "plain", 13, True)
    bx(f, 215, y0 + 40, 170, 80, "Sitio Healthcare.gov", "teal", 13, True)
    bx(f, 420, y0 + 40, 170, 80, "FFM: mercado federal (cuentas, elegibilidad, inscripción)", "coral", 13, True)
    bx(f, 625, y0 + 40, 140, 80, "Centro de servicios de datos federal", "gold", 13, True)
    bx(f, 795, y0, 135, 56, "Fuentes federales (p. ej., IRS, SSA)", "plain")
    bx(f, 795, y0 + 76, 135, 56, "Aseguradoras (planes y primas)", "plain")
    for a, b in ((180, 215), (385, 420), (590, 625)):
        f.arrow([(a, y0 + 80), (b, y0 + 80)])
    f.arrow([(765, y0 + 66), (795, y0 + 40)])
    f.arrow([(590, y0 + 100), (600, y0 + 150), (860, y0 + 150), (860, y0 + 132)], "inscripciones", label_at=(720, y0 + 144))
    f.text(14, y0 + 190, "CMS (dentro de HHS) contrata y supervisa; en 2011 se emitieron dos órdenes de trabajo y en enero de 2014 un contrato adicional", 13, "start", 700, "#142231")
    bx(f, 14, y0 + 204, 290, 74, "FFM: orden de trabajo a CGI Federal (septiembre de 2011)", "navy", 13)
    bx(f, 325, y0 + 204, 290, 74, "Centro de datos: orden de trabajo a QSSI (septiembre de 2011)", "navy", 13)
    bx(f, 636, y0 + 204, 290, 74, "Contrato a Accenture Federal Services (enero de 2014) para completar el FFM", "navy", 13)
    return done(f, y0 + 292,
                "Lo que enseña: no era un sitio web, era una cadena de sistemas de varias organizaciones que debían funcionar juntas el mismo día. Un punto débil en cualquiera aparecía para el usuario como un único «no funciona».",
                "gold", GAO14 + " Descripción funcional; la distribución de módulos es la que GAO resume.")


# ------------------------------------------------------------------ 2. flujo y módulos
def flujo() -> Fig:
    f, y = sketch("El recorrido del usuario y el estado de cada módulo al terminar la orden de trabajo",
                  "Recorrido de cuatro pasos: crear cuenta, verificar elegibilidad, elegir plan e inscribirse, y pago de primas; GAO resume que a febrero de 2014 solo el módulo de gestión de planes estaba completo, el de elegibilidad e inscripción tenía solo parte de sus elementos y el financiero estaba sin terminar.")
    y0 = y + 6
    pasos = [("1. Crear cuenta e iniciar sesión", "coral"), ("2. Verificar identidad e ingresos con fuentes federales", "coral"), ("3. Comparar y elegir plan; inscribirse", "gold"), ("4. Pagos y conciliación con aseguradoras", "grey")]
    estado = ["Capacidad insuficiente: dificultad para crear cuentas y entrar (GAO-15-238)", "Parte de los elementos del módulo de elegibilidad e inscripción", "Módulo de gestión de planes completo (según funcionarios de CMS)", "Módulo financiero sin terminar y aplazado al final del plazo"]
    w, gap = 205, 30
    for i, ((t, k), e) in enumerate(zip(pasos, estado)):
        x = 10 + i * (w + gap)
        bx(f, x, y0, w, 90, t, k, 13, True)
        bx(f, x, y0 + 120, w, 100, e, "plain", 13)
        f.arrow([(x + w / 2, y0 + 90), (x + w / 2, y0 + 120)], dashed=True)
        if i < 3:
            f.arrow([(x + w, y0 + 45), (x + w + gap, y0 + 45)])
    f.text(14, y0 + 112, "Estado según GAO", 13, "start", 700, "#142231")
    return done(f, y0 + 234,
                "Lo que enseña: CMS priorizó para el lanzamiento lo que se necesitaba para inscribirse y aplazó lo que se necesitaba después. La decisión es defendible; el problema es que aun lo priorizado salió sin verificarse con carga ni de extremo a extremo.",
                "gold", GAO14 + " GAO-15-238 para capacidad y pruebas.")


# ------------------------------------------------------------------ 3. línea de tiempo
def tiempos() -> Fig:
    return timeline(
        "Enero de 2013 a marzo de 2014: de los plazos comprimidos al final de la primera inscripción",
        "Línea de tiempo en meses desde enero de 2013: en marzo de 2013 CMS estima que solo 65 % del FFM y 75 % del centro de datos estarán listos en septiembre; en abril amplía la fase de diseño; en septiembre hace una revisión de preparación parcial; el 1 de octubre se lanza el sitio; el 30 de noviembre es el objetivo de estabilización; la primera inscripción termina el 31 de marzo de 2014.",
        [("Desarrollo y gobierno", [(0, 9, "Requisitos aún cambiando; pruebas comprimidas", "gold")]),
         ("Operación y recuperación", [(9, 11, "Crisis", "coral"), (11, 15, "Estabilizado", "teal")])],
        unit="Meses desde enero de 2013 (0 = 1 de enero de 2013)",
        events=[(2, "Mar"), (3, "Abr"), (8, "Sep"), (9, "1 oct"), (11, "30 nov")],
        ticks=[0, 3, 6, 9, 12, 15], t_max=15.5, label_w=190,
        note="Marzo: CMS estimó que solo 65 % del FFM y 75 % del centro de datos estaría listo en septiembre. Abril: se extendió el diseño y se comprimieron las pruebas. Septiembre: revisión de preparación parcial, con el desarrollo aún sin terminar. 30 de noviembre: objetivo de estabilización declarado por la administración. Los límites de la fase «Crisis» y «Estabilizado» son aproximados.",
        note_kind="gold", foot=GAO14 + " OEI-06-14-00350 y CMS (1 de diciembre de 2013).")


# ------------------------------------------------------------------ 4. gráfico con datos citados: crecimiento de obligaciones
def obligaciones() -> Fig:
    x_ticks = [(2011.67, "sep 2011"), (2012.58, "ago 2012"), (2013.25, "abr 2013"), (2013.67, "sep 2013"), (2014.08, "feb 2014")]
    return line_chart(
        "El dinero comprometido creció con cada cambio de requisitos",
        "Líneas con la obligación acumulada en millones de dólares para el mercado federal FFM, que pasa de 55,7 en septiembre de 2011 a 209,6 en febrero de 2014, y para el centro de datos, que pasa de 29,9 a 84,5 entre septiembre de 2011 y septiembre de 2013.",
        [("FFM (CGI Federal)", [(2011.67, 55.7, "55,7", "t"), (2012.58, 91.5, "91,5", "t"), (2013.25, 119.2, "119,2", "t"), (2013.67, 196, "196", "t"), (2014.08, 209.6, "209,6", "t")], "coral"),
         ("Centro de datos (QSSI)", [(2011.67, 29.9, "29,9", "b"), (2012.75, 48.7, "48,7", "b"), (2013.42, 53.7, "53,7", "b"), (2013.67, 84.5, "84,5", "b")], "navy")],
        x_label="Fecha de la modificación del contrato", y_label="Millones de dólares de EE. UU. obligados",
        x_ticks=x_ticks, y_ticks=[0, 50, 100, 150, 200, 250], point_labels="all", plot_h=300,
        note="El FFM casi se cuadruplicó y el centro de datos casi se triplicó. GAO atribuye el aumento principalmente a requisitos nuevos o cambiantes agravados por supervisión inconsistente. Los valores son obligaciones (dinero comprometido), no gasto ejecutado ni coste final del sitio.",
        note_kind="gold", foot=GAO14 + " Figura 4 y texto; el eje horizontal sitúa cada fecha con su fracción del año.")


# ------------------------------------------------------------------ 5. inicial frente a final
def antes_despues() -> Fig:
    return dumbbell(
        "Lo comprometido al inicio frente a lo comprometido después",
        "Puntos huecos y rellenos con la obligación inicial y la final para tres contratos: FFM de 55,7 a 209,6 millones; centro de datos de 29,9 a 84,5; y el contrato de Accenture de 91 en enero de 2014 a más de 175 en junio de 2014.",
        [("FFM: de septiembre de 2011 a febrero de 2014", 55.7, 209.6), ("Centro de datos: septiembre de 2011 a septiembre de 2013", 29.9, 84.5), ("Contrato Accenture: enero a junio de 2014", 91, 175)],
        unit="Millones de dólares de EE. UU.", names=("Inicial", "Después"), lower_is_better=True,
        delta=lambda a, b: f"×{b / a:.1f}".replace(".", ","),
        label_w=330,
        note="Los tres aumentos ocurren en tramos distintos y por razones que GAO describe: requisitos cambiantes y retrabajo (FFM y centro de datos), y nuevos requisitos y mejoras (Accenture, cuyo coste pasó de 91 a más de 175 a junio de 2014, con capacidades clave aún no disponibles). El factor es aritmética propia; el 175 es un «más de» de GAO.",
        note_kind="gold", foot=GAO14)


# ------------------------------------------------------------------ 6. mejoras
def mejoras() -> Fig:
    return case_cards(
        "Cinco decisiones del caso y la mejora que las habría cambiado",
        "Cinco tarjetas con una situación documentada a la izquierda y la mejora propuesta a la derecha: congelar un alcance mínimo, dar criterios de salida de la revisión de preparación, pruebas de carga y de extremo a extremo, cadena de malas noticias y lanzamiento escalonado.",
        [("Requisitos todavía cambiando en mitad de 2013, con plazos fijos", "Alcance mínimo congelado y lo demás en olas posteriores", "Es la causa que GAO atribuye al aumento de coste y a la compresión de pruebas.", "teal"),
         ("Revisión de preparación parcial en septiembre de 2013, con el desarrollo sin terminar", "Criterio de salida explícito: sin pruebas superadas, no hay lanzamiento", "GAO: se lanzó sin verificar que cumplía los requisitos de rendimiento.", "teal"),
         ("Demanda subestimada y sin plan de capacidad", "Prueba de carga con un rango de demanda y capacidad elástica", "GAO-15-238: CMS reconoció haber subestimado la demanda.", "teal"),
         ("Sin pruebas de extremo a extremo del conjunto", "Una prueba de extremo a extremo del recorrido crítico antes de abrir", "GAO-15-238: no se hicieron aunque estaban requeridas.", "teal"),
         ("Resistencia a las malas noticias y plazo inamovible", "Lanzamiento por fases o regiones con un canal de alerta sin castigo", "OEI-06-14-00350: no se reconoció la magnitud de los problemas ni se cambió de plan.", "teal")],
        note=ANALISIS, note_kind="teal", foot="", left=0.46)


# ================================================================== ampliación: niveles de arquitectura y análisis
GAO15 = "GAO-15-238 (marzo de 2015)"
OIG = "OEI-06-14-00350"


def capas() -> Fig:
    f, y = sketch("Contenedores: qué sistema hacía qué, y quién lo construyó",
                  "Diagrama de contenedores de Healthcare.gov: el consumidor entra por el sitio y la gestión de identidad, el mercado federal FFM con sus tres módulos de elegibilidad e inscripción, gestión de planes y financiero, y el centro de servicios de datos que consulta fuentes federales; las aseguradoras envían planes y reciben inscripciones. Debajo, los contratistas de cada pieza.")
    y0 = y + 6
    bx(f, 10, y0 + 40, 130, 70, "Consumidor", "plain", 13, True)
    f.group(165, y0, 560, 252, "Sistemas federales (CMS)", "grey")
    bx(f, 185, y0 + 40, 120, 70, "Sitio Healthcare.gov", "teal", 13, True)
    bx(f, 325, y0 + 40, 150, 70, "Gestión de identidad (EIDM): cuentas y acceso", "coral", 13, True)
    f.group(495, y0 + 8, 225, 214, "FFM (CGI Federal)", "teal")
    bx(f, 510, y0 + 36, 195, 52, "Elegibilidad e inscripción", "teal")
    bx(f, 510, y0 + 96, 195, 52, "Gestión de planes", "teal")
    bx(f, 510, y0 + 156, 195, 52, "Financiero (aplazado)", "gold")
    bx(f, 310, y0 + 150, 150, 70, "Centro de servicios de datos (Hub)", "navy", 13, True)
    bx(f, 765, y0 + 10, 165, 100, "Aseguradoras: envían planes y reciben inscripciones", "plain")
    bx(f, 765, y0 + 150, 165, 80, "Fuentes federales (por ejemplo IRS y seguridad social)", "plain")
    f.arrow([(140, y0 + 75), (185, y0 + 75)])
    f.arrow([(305, y0 + 75), (325, y0 + 75)])
    f.arrow([(475, y0 + 75), (495, y0 + 75)])
    f.arrow([(495, y0 + 185), (460, y0 + 185)], dashed=True)
    f.arrow([(705, y0 + 122), (765, y0 + 80)], dashed=True)
    f.arrow([(385, y0 + 220), (385, y0 + 240), (847, y0 + 240), (847, y0 + 230)], dashed=True)
    bx(f, 10, y0 + 266, 300, 56, "FFM: CGI Federal (órdenes de septiembre de 2011)", "plain")
    bx(f, 330, y0 + 266, 300, 56, "Hub: QSSI (septiembre de 2011); integrador desde octubre de 2013", "plain")
    bx(f, 650, y0 + 266, 280, 56, "Accenture: contrato de enero de 2014 para completar el FFM", "plain")
    return done(f, y0 + 338,
                "Lo que enseña: toda persona atravesaba primero la identidad y luego la verificación sobre otros sistemas de otras agencias. El flujo crítico dependía de tres contratistas y de fuentes que CMS no controlaba, y el módulo financiero ya estaba aplazado antes de abrir.",
                "gold", "Fuente: GAO-14-694, GAO-15-238 y CMS (1 de diciembre de 2013). Modelo funcional propio.")


def secuencia() -> Fig:
    f, y = sketch("Secuencia de un solicitante el 1 de octubre de 2013 y dónde se rompía",
                  "Diagrama de secuencia con consumidor, sitio, gestión de identidad, mercado federal, centro de datos y fuentes federales: la creación de cuentas satura la gestión de identidad, las verificaciones dependen de consultas a otras agencias, y muchas inconsistencias quedaron sin resolver.")
    y0 = y + 6
    lanes = [("Consumidor", "plain"), ("Sitio", "teal"), ("Gestión de identidad", "coral"), ("FFM", "teal"), ("Centro de datos", "navy"), ("Fuentes federales", "plain")]
    steps = [(0, 1, "crea cuenta"), (1, 2, "registro"),
             (2, 2, "≈ 500 000 cuentas", "note"), (2, 1, "errores", "red"),
             (1, 3, "solicitud"), (3, 4, "verifica"), (4, 5, "consulta"),
             (5, 4, "respuesta", "dashed"), (3, 3, "inconsistencias", "note"),
             (3, 1, "planes", "dashed"), (1, 0, "elige plan", "dashed")]
    yy = sequence(f, y0, lanes, steps, row_h=36)
    return done(f, yy,
                "Lo que enseña: el cuello de botella documentado estaba al principio, en la identidad; más adelante, las verificaciones dependían de consultas a otros sistemas. Los pasos 5 a 8 son el modelo funcional del recorrido; lo medido por las auditorías son la saturación de identidad y las inconsistencias.",
                "coral", "Fuente: GAO-15-238 (identidad saturada) y OEI-06-14-00350 (inconsistencias). Orden de pasos: modelo propio.")


def datos() -> Fig:
    f, y = sketch("Flujo de datos: de lo que declara el solicitante a lo que el sistema puede confirmar",
                  "Esquema de datos: la solicitud con ingresos y ciudadanía se contrasta con fuentes federales a través del centro de datos; los desacuerdos se acumulan como inconsistencias que requieren documentos; las aseguradoras suben los planes al módulo de gestión de planes y reciben las inscripciones; los pagos y la conciliación del módulo financiero estaban aplazados.")
    y0 = y + 6
    bx(f, 10, y0, 190, 90, "Solicitud: identidad, hogar, ingresos, ciudadanía", "plain", 13, True)
    bx(f, 250, y0, 190, 90, "Verificación contra fuentes federales vía el centro de datos", "navy", 13, True)
    bx(f, 490, y0, 200, 90, "Coincide: elegibilidad y subsidio calculados", "teal")
    bx(f, 490, y0 + 120, 200, 90, "No coincide: inconsistencia; el solicitante debe aportar documentos", "coral")
    bx(f, 740, y0, 190, 90, "Plan elegido y inscripción enviada a la aseguradora", "plain", 13, True)
    bx(f, 10, y0 + 120, 190, 90, "Aseguradoras: cargan planes antes y reciben las inscripciones", "plain")
    bx(f, 740, y0 + 120, 190, 90, "Pagos y conciliación: módulo financiero aplazado", "gold")
    f.arrow([(200, y0 + 45), (250, y0 + 45)])
    f.arrow([(440, y0 + 30), (490, y0 + 30)], "sí", label_at=(465, y0 + 18))
    f.arrow([(440, y0 + 70), (520, y0 + 120)], "no", color="#c0432f", label_at=(436, y0 + 104))
    f.arrow([(690, y0 + 45), (740, y0 + 45)])
    f.arrow([(835, y0 + 90), (835, y0 + 120)], dashed=True)
    return done(f, y0 + 226,
                "Lo que enseña: cada «no coincide» crea trabajo humano y de documentos que no escala con el pico del primer día. A febrero de 2014 quedaban sin resolver unos 2,6 millones de 2,9 millones de inconsistencias. Una verificación que falla cuesta mucho más que una que pasa.",
                "gold", "Fuente: GAO-14-694 (módulo financiero aplazado) y OEI-06-14-00350 (inconsistencias, febrero de 2014). Esquema de datos funcional propio.")


def capacidad() -> Fig:
    return dumbbell(
        "La capacidad subió a 400 TB, pero las fuentes parten de bases distintas",
        "Puntos huecos y rellenos: GAO-14-694 informa un aumento de 50 a 400 terabytes con una obligación de 1,5 millones de dólares; GAO-15-238 informa que la capacidad mensual para usuarios de internet pasó de 25 a 400 terabytes.",
        [("GAO-14-694: durante el desarrollo (TB)", 50, 400), ("GAO-15-238: capacidad mensual de internet (TB)", 25, 400)],
        unit="Terabytes", names=("Antes", "Después"), lower_is_better=False,
        delta=lambda a, b: f"×{b / a:.0f}", label_w=340,
        note="Las dos fuentes coinciden en el destino (400 TB) y difieren en el punto de partida (50 y 25 TB); pueden medir cosas distintas y las mostramos ambas. Lo importante es el orden de magnitud: un factor de 8 a 16 se necesitó después de abrir, no antes. Además, CMS duplicó el número de servidores, añadió máquinas virtuales y sustituyó una base de datos virtual por una física en identidad.",
        note_kind="gold", foot="Fuente: GAO-14-694 y GAO-15-238 (cifras de capacidad y actuaciones de CMS).")


def puntos_unicos() -> Fig:
    f, y = sketch("Dependencias y puntos únicos de fallo del recorrido del solicitante",
                  "Mapa de dependencias: todo solicitante pasa por la gestión de identidad, que dependía de una capacidad subestimada; la verificación depende del centro de datos y de fuentes ajenas; el desarrollo dependía de tres contratistas sin integrador único hasta octubre; y la fecha fija de lanzamiento no tenía alternativa.")
    y0 = y + 6
    bx(f, 360, y0, 220, 60, "Solicitante inscrito", "plain", 13, True)
    bx(f, 60, y0 + 110, 230, 66, "Gestión de identidad: puerta única, saturada", "coral", 13, True)
    bx(f, 360, y0 + 110, 220, 66, "Verificación: centro de datos y fuentes federales", "coral")
    bx(f, 650, y0 + 110, 230, 66, "Aseguradoras: planes cargados y probados con retraso", "gold")
    bx(f, 60, y0 + 230, 230, 66, "Capacidad estimada por debajo de la demanda", "gold")
    bx(f, 360, y0 + 230, 220, 66, "Tres contratistas; integrador único desde octubre", "gold")
    bx(f, 650, y0 + 230, 230, 66, "Fecha fija: 1 de octubre de 2013", "gold")
    f.arrow([(175, y0 + 110), (400, y0 + 60)])
    f.arrow([(470, y0 + 110), (470, y0 + 60)])
    f.arrow([(765, y0 + 110), (540, y0 + 60)])
    f.arrow([(175, y0 + 230), (175, y0 + 176)], dashed=True)
    f.arrow([(470, y0 + 230), (470, y0 + 176)], dashed=True)
    f.arrow([(765, y0 + 230), (765, y0 + 176)], dashed=True)
    return done(f, y0 + 312,
                "Lo que enseña: las tres cajas de arriba son las rutas por las que se llega a una inscripción; cada una tenía debajo una dependencia sin holgura. La identidad era la única puerta de entrada y no tenía alternativa.",
                "gold", ANALISIS)


def defensa() -> Fig:
    f, y = sketch("Defensa en profundidad: ocho barreras antes del lanzamiento y por qué no frenaron",
                  "Esquema de láminas con huecos: estrategia de adquisición, revisiones de gobierno, gestión de requisitos, verificación independiente, pruebas de extremo a extremo, plan de capacidad, exigencia al contratista y monitoreo en tiempo real; ninguna detuvo la fecha de lanzamiento; la flecha roja atraviesa todos los huecos.")
    y0 = y + 6
    items = [("Estrategia de adquisición (no se elaboró)", "coral", 0.5),
             ("Revisiones de gobierno (movidas a septiembre, sin aprobaciones)", "gold", 0.5),
             ("Gestión de requisitos (cambiantes, sin trazar siempre)", "gold", 0.5),
             ("Verificación independiente (45 críticos y 324 graves)", "gold", 0.5),
             ("Pruebas de extremo a extremo (no se hicieron)", "coral", 0.5),
             ("Plan de capacidad (no se elaboró)", "coral", 0.5),
             ("Exigencia al contratista (cartas; sin retener honorarios)", "gold", 0.5),
             ("Monitoreo en tiempo real (insuficiente)", "coral", 0.5)]
    yy = slices(f, y0, items, x0=30, w=62, gap=51, h=170, label_h=150, label_w=104)
    ymid = y0 + 18 + 0.5 * (170 - 80) + 22
    f.arrow([(10, ymid), (930, ymid)], color="#c0432f")
    return done(f, yy,
                "Lo que enseña: varias barreras existían en papel (revisiones, verificación, cartas al contratista) y no detuvieron el lanzamiento, porque ninguna tenía poder de veto sobre la fecha. Rojo: ausente o insuficiente; dorado: existió con eficacia parcial. La flecha es la decisión de lanzar el 1 de octubre.",
                "coral", ANALISIS)


def arbol() -> Fig:
    f, y = sketch("Árbol de fallas: qué tuvo que coincidir para que el 1 de octubre no funcionara",
                  "Árbol de fallas con tres ramas bajo el evento principal: el sistema no sostenía la demanda, los defectos conocidos no estaban corregidos y se lanzó sin criterio de salida; cada rama con sus condiciones documentadas.")
    y0 = y + 6
    bx(f, 300, y0, 340, 52, "Muchos usuarios no pueden inscribirse el 1 de octubre", "navy", 13, True)
    f.dot(470, y0 + 76, "O", "navy")
    f.arrow([(470, y0 + 52), (470, y0 + 64)])
    f.line(470, y0 + 88, 160, y0 + 110)
    f.line(470, y0 + 88, 470, y0 + 110)
    f.line(470, y0 + 88, 780, y0 + 110)
    bx(f, 30, y0 + 110, 260, 56, "A. No sostiene la demanda", "coral", 13, True)
    bx(f, 340, y0 + 110, 260, 56, "B. Defectos sin corregir", "coral", 13, True)
    bx(f, 650, y0 + 110, 260, 56, "C. Se lanza sin criterio de salida", "coral", 13, True)
    hojas = [["Demanda subestimada", "Sin plan de capacidad", "Identidad saturada"],
             ["45 críticos y 324 graves", "Sin pruebas de extremo a extremo", "Pruebas con aseguradoras incompletas"],
             ["Fecha legal fija", "Revisión movida a septiembre", "Sin verificar rendimiento"]]
    for c, col in enumerate(hojas):
        cx = 160 + c * 310
        f.dot(cx, y0 + 190, "Y", "navy")
        f.line(cx, y0 + 166, cx, y0 + 178)
        for i, t in enumerate(col):
            x = cx - 140 + i * 96
            bx(f, x, y0 + 226, 88, 130, t, "gold", 13)
            f.line(cx, y0 + 202, x + 44, y0 + 226)
    return done(f, y0 + 364,
                "Lo que enseña: «O» en la cima indica que bastaba una de las tres ramas para que fallara, y se dieron las tres a la vez; en cada rama las condiciones se combinan («Y»). Cortar solo una (por ejemplo, ampliar capacidad) no habría evitado los defectos sin corregir.",
                "gold", ANALISIS)


def antecedentes() -> Fig:
    f, y = sketch("Tres años de decisiones antes del 1 de octubre de 2013",
                  "Eje no proporcional con nueve hitos: la ley de marzo de 2010, la fecha de inscripción fijada entre 2011 y 2012, las órdenes de septiembre de 2011 con requisitos desconocidos, la elección de la base de datos en enero de 2012, la advertencia de capacidad de diciembre de 2012, el reconocimiento del 65 y 75 por ciento en marzo de 2013, la ampliación de abril, la revisión de preparación de septiembre y el lanzamiento.")
    ev = [("Mar 2010: ley PPACA; mercados antes del 1 ene 2014", "navy"),
          ("Jul 2011 y mar 2012: HHS fija el 1 oct 2013 como inicio", "navy"),
          ("Sep 2011: órdenes a CGI y QSSI con requisitos clave desconocidos", "gold"),
          ("Ene 2012: CMS dirige a CGI a usar una base NoSQL pese a sus reservas", "gold"),
          ("Dic 2012: evaluación señala debilidades de capacidad", "gold"),
          ("Mar 2013: solo 65 % del FFM y 75 % del Hub estarían listos", "coral"),
          ("Abr 2013: se alarga la fase de requisitos; se comprimen las pruebas", "coral"),
          ("Sep 2013: 45 críticos y 324 graves; revisión de preparación", "coral"),
          ("1 oct 2013: lanzamiento", "coral")]
    yy = equi_axis(f, y + 4, ev, box_w=168, box_h=108, x0=84, x1=856)
    return done(f, yy + 6,
                "Lo que enseña: las decisiones que más pesaron (requisitos abiertos, contratos reembolsables, fecha fija) se tomaron en 2011 y 2012; las señales de alarma aparecen en diciembre de 2012 y marzo de 2013, con tiempo de actuar. Septiembre de 2013 fue una evaluación sin margen para corregir.",
                "gold", "Fuente: GAO-14-694, GAO-15-238 y OEI-06-14-00350. Espaciado uniforme, no a escala de meses.")


def recuperacion() -> Fig:
    return timeline(
        "Octubre a diciembre de 2013, día a día: del colapso a la estabilización",
        "Línea de tiempo en días desde el 1 de octubre de 2013: el sitio cae un sesenta por ciento del tiempo en algunas semanas de octubre; a mediados de octubre se evalúa que es arreglable y QSSI pasa a integrador; el 30 de noviembre es el objetivo de estabilización; del 15 al 24 de diciembre se amplía el plazo para elegir plan.",
        [("Sitio", [(0, 31, "octubre: caídas y errores", "coral"), (31, 61, "noviembre: mejora", "teal")]),
         ("Gestión de la respuesta", [(14, 60, "QSSI integrador y sala de crisis", "navy")]),
         ("Plazo legal para elegir plan", [(75, 84, "15-24", "gold")])],
        unit="Días desde el 1 de octubre de 2013", events=[(0, "1 oct"), (60, "30 nov"), (84, "24 dic")],
        ticks=[0, 15, 31, 46, 61, 76, 92], t_max=92, label_w=250,
        note="Los límites son aproximados: CMS dice «mediados de octubre» para la evaluación y no fija el fin de la crisis. Dentro de noviembre la disponibilidad del sistema pasó de 42,9 % a algo más del 93 % y el tiempo de respuesta del FFM, de 8 s a menos de 1 s hacia diciembre (GAO-15-238). El último día del plazo hubo 49 156 usuarios simultáneos (OIG).",
        note_kind="gold", foot="Fuente: CMS (1 de diciembre de 2013), GAO-15-238 y OEI-06-14-00350.")


def despues() -> Fig:
    f, y = sketch("Gobierno «después»: lo que se aplicó tras el fallo y lo que faltó antes",
                  "Esquema de la recuperación documentada y de las barreras propuestas: integrador general único, sala de crisis dos veces al día, monitoreo instrumentado y sistemas de respaldo, más pruebas con congelación de código en la segunda inscripción, y criterios de salida y apertura gradual propuestos para el lanzamiento.")
    y0 = y + 6
    f.text(14, y0 + 12, "Aplicado tras el lanzamiento (documentado)", 13, "start", 700, "#142231")
    bx(f, 10, y0 + 26, 210, 84, "Integrador general único (QSSI)", "teal", 13, True)
    bx(f, 240, y0 + 26, 210, 84, "Sala de crisis dos veces al día con datos", "teal")
    bx(f, 470, y0 + 26, 210, 84, "Monitoreo instrumentado en tiempo real", "teal")
    bx(f, 700, y0 + 26, 230, 84, "Respaldo, más capacidad y re-ingeniería de identidad", "teal")
    f.text(14, y0 + 142, "Segunda inscripción (documentado): calidad antes que puntualidad", 13, "start", 700, "#142231")
    bx(f, 10, y0 + 156, 300, 76, "Fecha de congelación de código el 7 de octubre de 2014", "gold")
    bx(f, 330, y0 + 156, 290, 76, "Más infraestructura de prueba y coordinación de entornos", "gold")
    bx(f, 640, y0 + 156, 290, 76, "Capacidad para 250 000 usuarios simultáneos sin caída", "gold")
    f.text(14, y0 + 264, "Habría cambiado la decisión (análisis propio)", 13, "start", 700, "#142231")
    bx(f, 10, y0 + 278, 300, 76, "Criterio de salida con veto: sin pruebas pasadas no hay lanzamiento", "coral", 13, True)
    bx(f, 330, y0 + 278, 290, 76, "Apertura gradual por regiones con vuelta atrás", "coral")
    bx(f, 640, y0 + 278, 290, 76, "Canal formal para malas noticias hacia la dirección", "coral")
    return done(f, y0 + 372,
                "Lo que enseña: lo que se hizo después (arriba) fue gobierno y observabilidad, no una tecnología nueva. Abajo, tres barreras que habrían movido la decisión antes de abrir. La recuperación en dos meses muestra que el sistema era recuperable con otra gestión.",
                "teal", "Fuente: CMS (1 de diciembre de 2013), GAO-15-238 y OEI-06-14-00350; lo rotulado «análisis propio» no es una conclusión de esas fuentes.")


def salida() -> Fig:
    f, y = sketch("Diseño de la barrera de lanzamiento: un criterio de salida con cinco preguntas y veto",
                  "Diagrama de decisión de un criterio de salida: cinco preguntas en cadena sobre extremo a extremo, defectos críticos, capacidad con margen, ensayo de reversión y canal de malas noticias; si alguna es no, el lanzamiento pasa a alcance reducido o apertura gradual, no se aplaza en bloque.")
    y0 = y + 6
    q = ["¿Pasó el recorrido extremo a extremo con terceros?", "¿Cero defectos críticos abiertos?", "¿La prueba de carga cubre 2× la demanda esperada?", "¿Hay vuelta atrás ensayada?", "¿Alguien con veto ha oído las malas noticias?"]
    w, gap = 156, 36
    for i, t in enumerate(q):
        x = 10 + i * (w + gap)
        bx(f, x, y0 + 20, w, 100, t, "navy", 13, True)
        if i < 4:
            f.arrow([(x + w, y0 + 70), (x + w + gap, y0 + 70)], "sí", label_at=(x + w + gap / 2, y0 + 58))
        f.arrow([(x + w / 2, y0 + 120), (x + w / 2, y0 + 170)], "no", color="#c0432f", label_at=(x + w / 2 + 14, y0 + 150))
    bx(f, 10, y0 + 170, 900, 66, "Salida «no»: reducir alcance o abrir por cohortes y regiones, con vuelta atrás; no empezar para todos con la fecha fija", "coral", 13, True)
    bx(f, 10, y0 + 258, 900, 60, "Salida «sí» en las cinco: lanzamiento completo con monitoreo y sala de crisis activos desde el primer día", "teal", 13, True)
    return done(f, y0 + 332,
                "Lo que enseña: la barrera no pide perfección, pide que cada «no» tenga una alternativa menor que lanzar para todos. Con fecha legal fija, lo que se mueve es el alcance, y eso se decide antes de que llegue la fecha. Las cinco preguntas son diseño propio; los umbrales se calibran por sistema.",
                "teal", ANALISIS)


FIGURES = {
    "healthcare-gov-contexto.svg": contexto,
    "healthcare-gov-recorrido-y-modulos.svg": flujo,
    "healthcare-gov-linea-de-tiempo.svg": tiempos,
    "healthcare-gov-obligaciones.svg": obligaciones,
    "healthcare-gov-inicial-y-despues.svg": antes_despues,
    "healthcare-gov-mejoras.svg": mejoras,
    "healthcare-gov-contenedores.svg": capas,
    "healthcare-gov-secuencia.svg": secuencia,
    "healthcare-gov-flujo-de-datos.svg": datos,
    "healthcare-gov-capacidad.svg": capacidad,
    "healthcare-gov-puntos-unicos.svg": puntos_unicos,
    "healthcare-gov-defensa-en-profundidad.svg": defensa,
    "healthcare-gov-arbol-de-fallas.svg": arbol,
    "healthcare-gov-antecedentes.svg": antecedentes,
    "healthcare-gov-recuperacion.svg": recuperacion,
    "healthcare-gov-arquitectura-despues.svg": despues,
    "healthcare-gov-criterio-de-salida.svg": salida,
}


def main(out: str | None = None) -> int:
    target = Path(out) if out else Path(__file__).resolve().parents[1] / "casos" / "figures"
    target.mkdir(parents=True, exist_ok=True)
    for name, builder in FIGURES.items():
        (target / name).write_text(builder().svg(), encoding="utf-8", newline="\n")
        print("wrote", target / name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else None))
