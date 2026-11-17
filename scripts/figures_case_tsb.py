"""Figures for the failure case study TSB (IT migration of 20-22 April 2018).

Numbers come from the FCA Final Notice of 20 December 2022 and the joint FCA/PRA press release of the same date.
Output goes to ``casos/figures/``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_helpers_fallo import equi_axis, sequence, slices  # noqa: E402
from figure_kit import dumbbell as _dumbbell_unused  # noqa: E402
from figure_cases import case_cards  # noqa: E402
from figure_kit import Fig, _kit_finish, _kit_start, _wrap, grouped_bars, timeline  # noqa: E402

FCA = "Fuente: FCA, Final Notice a TSB Bank plc (20 de diciembre de 2022)."
ANALISIS = "Análisis propio apoyado en el Final Notice de la FCA; no es una conclusión del regulador."


def sketch(title: str, desc: str, width: int = 940):
    return _kit_start(title, desc, width, None)


def bx(f: Fig, x: float, y: float, w: float, h: float, text: str, kind: str = "plain", size: int = 13, bold: bool = False, dashed: bool = False) -> None:
    lines = _wrap(text, size, w - 20)
    assert len(lines) * size * 1.28 <= h - 6, f"box overflows: {text!r} ({len(lines)} lines in {h}px)"
    f.box(x, y, w, h, text, kind, size, bold=bold, dashed=dashed)


def done(f: Fig, y: float, note: str, kind: str = "gold", foot: str = "") -> Fig:
    _kit_finish(f, y, note, kind, foot)
    f.kind = "diagram"
    return f


# ------------------------------------------------------------------ 1. contexto y arquitectura
def contexto() -> Fig:
    f, y = sketch("De la plataforma de Lloyds a Proteo4UK: una migración sin vuelta atrás",
                  "Diagrama de antes y después: hasta abril de 2018 TSB recibía sus servicios informáticos de la plataforma de Lloyds Banking Group; el fin de semana del 20 al 22 de abril de 2018 migró a Proteo4UK, una versión nueva de la plataforma de Sabadell construida y operada por SABIS, que a su vez dependía de 85 terceros; tras la migración no se podía volver a la plataforma de Lloyds.")
    y0 = y + 6
    f.group(10, y0, 420, 232, "Antes (hasta el 20 de abril de 2018)", "grey")
    bx(f, 30, y0 + 40, 380, 56, "Plataforma de Lloyds Banking Group, bajo contrato de externalización hasta julio de 2024", "plain")
    bx(f, 30, y0 + 112, 380, 56, "Servicios de TSB: sucursales, teléfono, banca por internet y móvil", "teal")
    f.arrow([(220, y0 + 96), (220, y0 + 112)])
    bx(f, 30, y0 + 178, 380, 44, "Operación a cargo de Lloyds, ya en producción", "plain")
    f.group(510, y0, 420, 232, "Después (desde el 22 de abril de 2018)", "coral")
    bx(f, 530, y0 + 40, 380, 56, "Proteo4UK: versión nueva de la plataforma de Sabadell, construida y operada por SABIS", "coral", 13, True)
    bx(f, 530, y0 + 112, 380, 56, "SABIS depende de 85 terceros (cuartas partes desde TSB)", "gold")
    f.arrow([(720, y0 + 96), (720, y0 + 112)])
    bx(f, 530, y0 + 178, 380, 44, "Sin vuelta atrás a la plataforma de Lloyds", "navy", 13, True)
    f.arrow([(430, y0 + 116), (510, y0 + 116)], "migración", label_at=(470, y0 + 100))
    return done(f, y0 + 246,
                "Lo que enseña: la migración cambió de una vez el sistema, el operador y la cadena de proveedores, y eliminó la posibilidad de volver. Eso convierte cualquier defecto en un incidente sin salida, porque solo se puede arreglar hacia delante.",
                "gold", FCA + " Secciones 2.1 a 2.4, 2.22 y 2.27.")


# ------------------------------------------------------------------ 2. cascada
def cascada() -> Fig:
    f, y = sketch("La cascada: cada canal que falló empujó a los clientes al siguiente",
                  "Cadena de cinco pasos: fallos en la banca por internet y móvil llevan a los clientes al teléfono; el teléfono se satura y también falla por otros problemas de tecnología; los clientes acuden a las sucursales, donde los servicios eran lentos por fallos de tecnología; y las quejas desbordan la capacidad de gestión durante casi doce meses.")
    y0 = y + 6
    pasos = [("Fallos en internet y móvil", "coral"), ("Los clientes llaman por teléfono", "gold"), ("Teléfono saturado y con fallos propios", "coral"), ("Colas en sucursales con servicios lentos", "gold"), ("225 492 quejas; casi 12 meses para resolverlas", "coral")]
    w, gap = 160, 30
    for i, (t, k) in enumerate(pasos):
        x = 10 + i * (w + gap)
        bx(f, x, y0 + 20, w, 104, t, k, 13, True)
        if i < 4:
            f.arrow([(x + w, y0 + 72), (x + w + gap, y0 + 72)])
    bx(f, 10, y0 + 160, 420, 64, "Cada paso aumentaba la carga del siguiente: la demanda se trasladaba, no se resolvía", "navy", 13)
    bx(f, 470, y0 + 160, 460, 64, "El plan de crisis cubría las primeras 48 horas y ejercicios de unos pocos días; muchos incidentes duraron semanas", "teal")
    return done(f, y0 + 240,
                "Lo que enseña: un fallo en un canal aparece como carga en los demás. La capacidad de teléfono y sucursales estaba dimensionada, según el regulador, por debajo del volumen que provocó el incidente.",
                "gold", FCA + " Párrafos 2.6, 2.29 a 2.31.")


# ------------------------------------------------------------------ 3. línea de tiempo
def tiempos() -> Fig:
    return timeline(
        "De la compra por Sabadell al regreso a la normalidad: 54 meses",
        "Línea de tiempo en meses desde junio de 2014: TSB se escinde de Lloyds en junio de 2014, Sabadell la adquiere en julio de 2015, el plan maestro de marzo de 2016 apuntaba a migrar a finales de 2017, en septiembre de 2017 se decide replantear el plan, el fin de semana del 20 al 22 de abril de 2018 se migra y TSB no vuelve a la normalidad operativa hasta el 10 de diciembre de 2018.",
        [("Programa de migración", [(13, 46, "Diseño, construcción y pruebas", "gold")]),
         ("Después de la migración", [(46, 54, "Incidente", "coral")])],
        unit="Meses desde junio de 2014 (0 = junio de 2014)",
        events=[(13, "Jul 2015"), (21, "Mar 2016"), (39, "Sep 2017"), (46, "Abr 2018")],
        ticks=[0, 12, 24, 36, 48, 54], t_max=56, label_w=190,
        note="Julio de 2015: Sabadell adquiere TSB. Marzo de 2016: plan maestro con migración a finales de 2017 pese a ir meses atrasado. Septiembre de 2017: se decide replantear el plan y nueve días después se anuncia migración en el primer trimestre de 2018. Abril de 2018: migración. Diciembre de 2018: fin del incidente, según el regulador. Las posiciones son aproximadas al mes.",
        note_kind="gold", foot=FCA + " Párrafos 2.1 a 2.12 y 2.7.")


# ------------------------------------------------------------------ 4. gráfico con datos citados
def dinero() -> Fig:
    return grouped_bars(
        "Lo que el regulador cuantifica: compensación y multas",
        "Barras horizontales en millones de libras: compensación pagada a clientes 32,7; multa de la FCA 29,75 tras el descuento del 30 %; multa de la FCA antes del descuento 42,5; y multa de la PRA 18,9.",
        ["Compensación a clientes (22 abr 2018 a 7 abr 2019)", "Multa FCA tras el 30 % de descuento", "Multa FCA sin descuento", "Multa PRA"],
        [("Millones de libras", [32.7, 29.75, 42.5, 18.9], "coral")],
        unit="Millones de libras esterlinas (£)", horizontal=True, label_w=330, decimals=2,
        ticks=[0, 10, 20, 30, 40, 50],
        note="La multa total fue de 48,65 millones (FCA 29,75 más PRA 18,9). La compensación pagada fue de 32 705 762 libras por distintos conceptos (reparación, gastos, molestias). No incluye el costo interno del programa de remediación ni la pérdida de clientes, que las fuentes consultadas no cuantifican.",
        note_kind="gold", foot=FCA + " y comunicado conjunto FCA/PRA del 20 de diciembre de 2022.")


# ------------------------------------------------------------------ 5. mejoras
def mejoras() -> Fig:
    return case_cards(
        "Siete decisiones del caso y la mejora que las habría cambiado",
        "Siete tarjetas con una situación documentada y la mejora propuesta: plan realista con incertidumbre, criterios de salida de pruebas, prueba de configuración de centros de datos, diligencia sobre el proveedor, migración por etapas con vuelta atrás, plan de crisis de semanas y comunicación a clientes.",
        [("Plan maestro de izquierda a derecha con fecha pública, ya atrasado", "Plan con la incertidumbre explícita y fecha no comprometida", "La fecha pública redujo el margen para decidir con evidencia.", "teal"),
         ("Pruebas en paralelo y terminadas el día antes de decidir", "Criterios de salida de pruebas y tiempo para corregir", "Las pruebas se comprimieron para cumplir los plazos.", "teal"),
         ("Pruebas de configuración de los centros de datos reducidas en febrero de 2018", "Mantener la prueba, o registrar el riesgo ante el comité adecuado", "Según la FCA, probablemente habría detectado el problema de configuración.", "teal"),
         ("Capacidad de SABIS y de sus 85 terceros sin evaluación formal", "Diligencia formal y ejercicios conjuntos de incidente con el proveedor", "No se identificó de forma explícita el riesgo de incumplimiento del proveedor.", "teal"),
         ("Migración casi total en un fin de semana y sin vuelta atrás", "Migración por oleadas con vuelta atrás probada", "Sin retorno posible, cualquier defecto se arregla en caliente.", "teal"),
         ("Guías para las primeras 48 horas y ejercicios de unos días", "Plan para semanas, con ampliación de capacidad y comunicación", "Muchos incidentes duraron semanas.", "teal"),
         ("Mensajes genéricos y clientes vulnerables sin identificar", "Guion de comunicación y registro de clientes vulnerables antes de migrar", "Los mensajes no reflejaban la experiencia real del cliente.", "teal")],
        note=ANALISIS, note_kind="teal", foot="", left=0.46)


# ================================================================== ampliación: niveles de arquitectura y análisis


def capas() -> Fig:
    f, y = sketch("Contenedores: de los canales del cliente a la plataforma y sus proveedores",
                  "Diagrama de contenedores: los clientes usan cuatro canales (internet y móvil, teléfono, sucursales y tarjetas) que dependen de la plataforma Proteo4UK construida y operada por SABIS, que a su vez se apoya en 85 terceros; hasta abril de 2018 los canales dependían de la plataforma de Lloyds, a la que ya no se podía volver tras migrar.")
    y0 = y + 6
    bx(f, 10, y0 + 30, 140, 70, "5,2 millones de clientes", "plain", 13, True)
    f.group(180, y0, 420, 130, "Canales de TSB", "grey")
    bx(f, 196, y0 + 36, 90, 76, "Internet y móvil", "coral", 13, True)
    bx(f, 294, y0 + 36, 90, 76, "Teléfono", "coral", 13, True)
    bx(f, 392, y0 + 36, 90, 76, "Sucursales", "coral", 13, True)
    bx(f, 490, y0 + 36, 100, 76, "Pagos y tarjetas", "coral", 13, True)
    bx(f, 640, y0 + 6, 290, 118, "Plataforma Proteo4UK: diseñada, construida, probada y operada por SABIS (filial de Sabadell)", "navy", 13, True)
    bx(f, 640, y0 + 160, 290, 70, "85 terceros de SABIS: para TSB, cuartas partes", "gold")
    bx(f, 180, y0 + 160, 420, 70, "Plataforma de Lloyds: hasta el 22 de abril de 2018; después, sin vuelta atrás", "grey", 13, False, True)
    f.arrow([(150, y0 + 65), (180, y0 + 65)])
    f.arrow([(600, y0 + 65), (640, y0 + 65)])
    f.arrow([(785, y0 + 124), (785, y0 + 160)], dashed=True)
    f.arrow([(390, y0 + 160), (390, y0 + 130)], dashed=True, color="#c0432f")
    bx(f, 10, y0 + 256, 300, 62, "Contrato con Lloyds: uso posible hasta julio de 2024", "plain")
    bx(f, 330, y0 + 256, 300, 62, "SABIS aportaba el diseño, la migración de datos y la operación", "plain")
    bx(f, 650, y0 + 256, 280, 62, "Gobierno: consejo de TSB y comité ejecutivo", "plain")
    return done(f, y0 + 334,
                "Lo que enseña: los cuatro canales colgaban de una sola plataforma nueva y de un solo proveedor con cadena de 85 subcontratistas. Tras la migración, la plataforma anterior dejó de ser una opción, y el único recurso era que SABIS arreglara los incidentes.",
                "gold", FCA + " Párrafos 2.1 a 2.5, 2.22 y 2.27. Esquema propio.")


def secuencia() -> Fig:
    f, y = sketch("Secuencia del fin de semana de migración y de la primera semana",
                  "Diagrama de secuencia con consejo de TSB, SABIS, plataforma Proteo4UK, clientes y plataforma de Lloyds: terminan las pruebas el día antes de decidir, se migra el 20 al 22 de abril, fallan los canales, los clientes pasan del móvil al teléfono y a las sucursales, y no se puede volver a la plataforma de Lloyds.")
    y0 = y + 6
    lanes = [("Consejo y dirección de TSB", "gold"), ("SABIS", "navy"), ("Proteo4UK", "teal"), ("Clientes", "plain"), ("Plataforma de Lloyds", "grey")]
    steps = [(1, 0, "carta", "dashed"), (0, 1, "decide migrar"), (1, 2, "migra datos"),
             (2, 3, "abre el 22 abr"), (3, 2, "canales fallan", "red"),
             (3, 3, "pasan al teléfono", "note"), (3, 0, "colas y quejas", "red"),
             (0, 4, "sin vuelta", "red"), (0, 1, "pide arreglar"), (1, 2, "correcciones")]
    yy = sequence(f, y0, lanes, steps, row_h=35)
    return done(f, yy,
                "Lo que enseña: el consejo decidió con una carta del proveedor que era en parte una declaración de intención, y desde el primer día no tenía retorno. La figura es un modelo del orden de hechos que describe la FCA; el Final Notice no da horas por paso.",
                "coral", FCA + " Párrafos 2.5 a 2.7, 2.13, 2.24, 2.25 y 2.27. Orden de pasos: reconstrucción propia.")


def activo_activo() -> Fig:
    f, y = sketch("La prueba que se recortó: la configuración «activo-activo» de los centros de datos",
                  "Esquema de despliegue con dos centros de datos que atienden banca digital en configuración activo-activo, un balanceo entre ambos, y la prueba no funcional de esa configuración que se redujo de alcance en febrero de 2018; un problema de configuración en ciertos componentes dejó sin disponibilidad a internet y móvil tras la migración.")
    y0 = y + 6
    bx(f, 340, y0, 260, 60, "Clientes de banca digital", "plain", 13, True)
    bx(f, 340, y0 + 90, 260, 60, "Reparto de tráfico entre los dos centros", "gold", 13, True)
    f.group(60, y0 + 190, 330, 170, "Centro de datos A", "grey")
    f.group(550, y0 + 190, 330, 170, "Centro de datos B", "grey")
    bx(f, 80, y0 + 230, 290, 110, "Componentes de banca digital en configuración activo-activo", "coral")
    bx(f, 570, y0 + 230, 290, 110, "Componentes de banca digital en configuración activo-activo", "teal")
    f.arrow([(470, y0 + 60), (470, y0 + 90)])
    f.arrow([(400, y0 + 150), (225, y0 + 230)])
    f.arrow([(540, y0 + 150), (715, y0 + 230)])
    f.arrow([(390, y0 + 285), (570, y0 + 285)], "sincronía", dashed=True, label_at=(480, y0 + 272))
    bx(f, 660, y0 + 10, 270, 100, "Febrero de 2018: se reduce el alcance de esta prueba, fuera del foro de gobierno adecuado", "gold")
    bx(f, 160, y0 + 372, 620, 54, "Problema de configuración de ciertos componentes; según TSB (2019), los dos centros no quedaron idénticos", "coral", 13, True)
    return done(f, y0 + 440,
                "Lo que enseña: la FCA dice que, de haberse hecho esa prueba, probablemente se habría encontrado el problema de configuración que dejó sin disponibilidad a internet y móvil. TSB solo consideró el riesgo de la prueba sobre servicios ya activos y la trató como una decisión técnica; el riesgo de no hacerla no se identificó.",
                "coral", FCA + " Párrafo 2.14. La topología es un modelo didáctico: el Final Notice no describe los componentes concretos.")


def dependencias() -> Fig:
    f, y = sketch("Dependencias y puntos únicos de fallo después de migrar",
                  "Mapa de dependencias: la operación de TSB depende de un solo proveedor principal, que depende de 85 terceros, sin plataforma de vuelta; arriba el cliente, y debajo la dependencia de documentación de configuración en vez de diseño, la confirmación de cuatro terceros críticos, la carta del proveedor y la fecha pública.")
    y0 = y + 6
    bx(f, 360, y0, 220, 56, "Cliente de TSB", "plain", 13, True)
    bx(f, 60, y0 + 100, 240, 66, "Proveedor principal: SABIS (único)", "coral", 13, True)
    bx(f, 360, y0 + 100, 220, 66, "Sin retorno a la plataforma de Lloyds", "coral", 13, True)
    bx(f, 650, y0 + 100, 240, 66, "85 terceros de SABIS, visibilidad limitada", "gold")
    bx(f, 60, y0 + 210, 240, 66, "Configuración en lugar de diseño", "gold")
    bx(f, 360, y0 + 210, 220, 66, "Carta del proveedor y cuatro terceros críticos", "gold")
    bx(f, 650, y0 + 210, 240, 66, "Fecha pública de migración", "gold")
    f.arrow([(180, y0 + 100), (400, y0 + 56)])
    f.arrow([(470, y0 + 100), (470, y0 + 56)])
    f.arrow([(770, y0 + 100), (540, y0 + 56)])
    f.arrow([(180, y0 + 210), (180, y0 + 166)], dashed=True)
    f.arrow([(470, y0 + 210), (470, y0 + 166)], dashed=True)
    f.arrow([(770, y0 + 210), (770, y0 + 166)], dashed=True)
    return done(f, y0 + 292,
                "Lo que enseña: las cajas rojas son puntos únicos con efecto directo sobre el cliente; las doradas, las garantías que debían sostenerlos. La carta de preparación y las confirmaciones de terceros eran en parte declaraciones de intención o tenían tareas pendientes, no hechos.",
                "gold", ANALISIS + " Hechos: párrafos 2.19 a 2.25.")


def defensa() -> Fig:
    f, y = sketch("Defensa en profundidad: ocho barreras antes del 22 de abril de 2018",
                  "Esquema de láminas con huecos: planificación, pruebas, documentación de diseño, evaluación del proveedor, confirmaciones de terceros críticos, revisión del consejo, continuidad e incidentes, y capacidad de atención de quejas; ninguna impidió migrar con riesgos no resueltos; una flecha las atraviesa.")
    y0 = y + 6
    items = [("Planificación (plan maestro y replan, sin «izquierda a derecha» suficiente)", "gold", 0.5),
             ("Pruebas (comprimidas, en paralelo; fin el día antes)", "gold", 0.5),
             ("Prueba activo-activo (reducida en febrero de 2018)", "coral", 0.5),
             ("Documentación de diseño (sustituida por configuración)", "gold", 0.5),
             ("Evaluación del proveedor (sin diligencia formal inicial)", "coral", 0.5),
             ("Confirmaciones de terceros (con tareas pendientes)", "gold", 0.5),
             ("Revisión del consejo (limitaciones no discutidas)", "gold", 0.5),
             ("Continuidad (planes de 48 horas, ejercicios de días)", "coral", 0.5)]
    yy = slices(f, y0, items, x0=30, w=62, gap=51, h=170, label_h=170, label_w=104)
    ymid = y0 + 18 + 0.5 * (170 - 80) + 22
    f.arrow([(10, ymid), (930, ymid)], color="#c0432f")
    return done(f, yy,
                "Lo que enseña: las barreras existían, pero cada una estaba debilitada por la presión de la fecha: pruebas que se solapan, documentación sustituida, confirmaciones con salvedades. Rojo: no se hizo o se redujo; dorado: se hizo con eficacia parcial. La flecha es la decisión de migrar.",
                "coral", ANALISIS + " Hechos: párrafos 2.10 a 2.31.")


def arbol() -> Fig:
    f, y = sketch("Árbol de fallas: qué tuvo que coincidir para ocho meses de crisis",
                  "Árbol de fallas con el evento principal arriba, clientes sin servicio normal hasta diciembre de 2018, y tres ramas: la plataforma falla, se migra pese a riesgos no resueltos y no hay recuperación posible; cada rama con sus condiciones documentadas.")
    y0 = y + 6
    bx(f, 300, y0, 340, 52, "Servicio degradado del 22 de abril al 10 de diciembre de 2018", "navy", 13, True)
    f.dot(470, y0 + 76, "Y", "navy")
    f.arrow([(470, y0 + 52), (470, y0 + 64)])
    f.line(470, y0 + 88, 160, y0 + 110)
    f.line(470, y0 + 88, 470, y0 + 110)
    f.line(470, y0 + 88, 780, y0 + 110)
    bx(f, 30, y0 + 110, 260, 56, "A. La plataforma falla", "coral", 13, True)
    bx(f, 340, y0 + 110, 260, 56, "B. Se migra con riesgo sin resolver", "coral", 13, True)
    bx(f, 650, y0 + 110, 260, 56, "C. No hay vuelta ni recuperación", "coral", 13, True)
    hojas = [["Configuración", "Capacidad", "Código"],
             ["Fecha pública", "Pruebas hasta el día antes", "Proveedor sin diligencia formal"],
             ["Sin retorno a Lloyds", "Planes de 48 horas", "Quejas sin capacidad"]]
    for c, col in enumerate(hojas):
        cx = 160 + c * 310
        f.dot(cx, y0 + 190, "O" if c != 1 else "Y", "navy")
        f.line(cx, y0 + 166, cx, y0 + 178)
        for i, t in enumerate(col):
            x = cx - 140 + i * 96
            bx(f, x, y0 + 226, 88, 130, t, "gold", 13)
            f.line(cx, y0 + 202, x + 44, y0 + 226)
    return done(f, y0 + 372,
                "Lo que enseña: «Y» en la cima: hacían falta las tres ramas, y la ausencia de vuelta atrás (C) es lo que convierte un fallo técnico en una crisis de meses. Cortar B (decidir con evidencia) o C (poder volver) habría evitado o acotado el incidente.",
                "gold", ANALISIS + " Hechos de los párrafos 2.9 a 2.31; la estructura lógica es propia.")


def antecedentes() -> Fig:
    f, y = sketch("Cuatro años de decisiones hasta el fin de semana de la migración",
                  "Eje no proporcional con nueve hitos: la escisión de junio de 2014, la compra de Sabadell en julio de 2015, el plan maestro de marzo de 2016, la decisión de replanificar el 20 de septiembre de 2017, el anuncio público nueve días después, la reducción de pruebas en febrero de 2018, el fin de las pruebas el día antes de la decisión, la migración del 20 al 22 de abril y la vuelta a la normalidad el 10 de diciembre.")
    ev = [("Jun 2014: TSB se escinde de Lloyds; sigue en su plataforma hasta 2024", "navy"),
          ("Jul 2015: Sabadell compra TSB; meta: migrar a fines de 2017", "navy"),
          ("Mar 2016: plan maestro con meses de retraso", "gold"),
          ("20 sep 2017: se decide replanificar", "gold"),
          ("29 sep 2017: anuncio público de migrar en el 1.er trim. de 2018", "gold"),
          ("Feb 2018: se reducen pruebas y documentos; cambia la atestación", "coral"),
          ("Víspera de decidir: terminan las pruebas", "coral"),
          ("20-22 abr 2018: migración principal", "coral"),
          ("10 dic 2018: vuelta a la normalidad", "teal")]
    yy = equi_axis(f, y + 4, ev, box_w=168, box_h=108, x0=84, x1=856)
    return done(f, yy + 6,
                "Lo que enseña: el anuncio público llegó nueve días después de decidir que había que replanificar y antes de acabar de replanificar: la fecha pasó a ser un compromiso externo antes de ser un plan. El riesgo se acumula entre 2017 y febrero de 2018.",
                "gold", FCA + " Párrafos 2.1, 2.2, 2.10 a 2.15, 2.7 y 2.13. Espaciado uniforme, no a escala de meses.")


def doce_meses() -> Fig:
    return timeline(
        "Del 22 de abril de 2018 al 7 de abril de 2019: servicio, quejas y reparación",
        "Línea de tiempo en meses desde abril de 2018: servicios afectados hasta el 10 de diciembre de 2018, quejas recibidas durante casi doce meses, programa de reparación desde mayo de 2018 y compensación pagada durante el periodo.",
        [("Servicio degradado", [(0, 7.6, "hasta el 10 de diciembre de 2018", "coral")]),
         ("Quejas recibidas", [(0, 11.5, "225 492 quejas en 12 meses", "gold")]),
         ("Programa «Putting Things Right»", [(1, 11.5, "desde mayo de 2018", "teal")])],
        unit="Meses desde el 22 de abril de 2018", events=[(0, "22 abr"), (7.6, "10 dic"), (11.5, "7 abr 2019")],
        ticks=[0, 2, 4, 6, 8, 10, 12], t_max=12, label_w=250,
        note="La FCA da el inicio, el fin del servicio degradado y el cierre del periodo de quejas; no da el reparto de las quejas por mes ni la carga diaria. Los 32 705 762 de compensación son del conjunto del periodo. «Casi doce meses» es el plazo que, según la FCA, tardó en gestionar las quejas.",
        note_kind="gold", foot=FCA + " Párrafos 2.7, 2.8, 2.31 y 2.32.")


def oleadas() -> Fig:
    return grouped_bars(
        "Cuántos clientes ven un error nuevo el primer día: de una vez y por oleadas",
        "Modelo didáctico: con la migración de una vez, el cien por cien de los 5,2 millones de clientes queda expuesto al primer error de la plataforma; con diez oleadas iguales y vuelta atrás probada, solo el diez por ciento, unos 520 000.",
        ["Migración de una vez (como en abril de 2018)", "Cinco oleadas iguales", "Diez oleadas iguales"],
        [("Clientes expuestos al primer error (millones)", [5.2, 1.04, 0.52], "coral")],
        unit="Millones de clientes expuestos (5,2 millones en total)", horizontal=True, label_w=320, decimals=2,
        ticks=[0, 1, 2, 3, 4, 5, 6],
        note="El modelo supone oleadas del mismo tamaño y un error visible en la primera; solo muestra el orden de magnitud de la exposición. La FCA documenta que el evento único afectó a todas las sucursales y a una proporción significativa de los 5,2 millones de clientes. Las oleadas tienen un coste propio de coexistencia y de datos duplicados que no se mide aquí.",
        note_kind="gold", foot="Modelo didáctico con valores ilustrativos. Fuente del total: FCA/PRA, comunicado del 20 de diciembre de 2022.")


def despues() -> Fig:
    f, y = sketch("Arquitectura de migración «después»: oleadas, coexistencia y retorno ensayado",
                  "Arquitectura objetivo propuesta: una capa de enrutamiento que lleva a cada cliente a la plataforma antigua o a la nueva, oleadas sucesivas de clientes con comprobaciones de datos, un camino de vuelta atrás ensayado, observabilidad compartida con el proveedor y criterios de entrada de cada oleada.")
    y0 = y + 6
    bx(f, 10, y0 + 20, 150, 80, "Clientes por oleadas", "plain", 13, True)
    bx(f, 200, y0 + 20, 190, 80, "Capa de enrutamiento: cada cliente en una sola plataforma", "navy", 13, True)
    bx(f, 440, y0, 220, 60, "Plataforma de Lloyds (origen)", "grey")
    bx(f, 440, y0 + 70, 220, 60, "Proteo4UK (destino)", "teal", 13, True)
    bx(f, 710, y0 + 20, 220, 80, "Comprobación de datos y reconciliación por oleada", "gold")
    f.arrow([(160, y0 + 60), (200, y0 + 60)])
    f.arrow([(390, y0 + 40), (440, y0 + 30)])
    f.arrow([(390, y0 + 80), (440, y0 + 100)])
    f.arrow([(660, y0 + 100), (710, y0 + 70)], dashed=True)
    f.arrow([(440, y0 + 100), (390, y0 + 100)], "vuelta atrás ensayada", dashed=True, color="#c0432f", label_at=(300, y0 + 122))
    bx(f, 10, y0 + 180, 290, 76, "Criterio de entrada de cada oleada: carga al doble, activo-activo probado, retorno ensayado", "teal")
    bx(f, 320, y0 + 180, 290, 76, "Observabilidad y guion de incidente compartidos con el proveedor", "teal")
    bx(f, 630, y0 + 180, 300, 76, "Capacidad de contacto y de quejas escalable desde la primera oleada", "teal")
    return done(f, y0 + 270,
                "Lo que enseña: cada oleada es un experimento acotado con retorno. La capa de enrutamiento hace posible la coexistencia, y la comprobación de datos detecta errores antes de la siguiente oleada. Es análisis propio apoyado en las deficiencias del Final Notice; no describe lo que TSB adoptó después.",
                "teal", ANALISIS)


def escalera() -> Fig:
    f, y = sketch("La evidencia que exige un cambio crece con su irreversibilidad",
                  "Escalera de tres peldaños: un cambio reversible exige una prueba y un retorno simple; un cambio parcialmente reversible exige pruebas de carga, ensayos con datos reales y criterios de salida; un cambio irreversible como migrar sin vuelta atrás exige además diligencia del proveedor, ensayos completos de incidente y decisión informada del consejo.")
    y0 = y + 6
    bx(f, 10, y0 + 180, 290, 90, "Reversible (un servicio, con retorno inmediato): prueba y plan de vuelta", "teal", 13, True)
    bx(f, 320, y0 + 100, 290, 170, "Parcialmente reversible (una oleada): carga, datos reales, activo-activo y criterios de salida", "gold", 13, True)
    bx(f, 630, y0 + 20, 300, 250, "Irreversible (migración total sin retorno): todo lo anterior, diligencia formal del proveedor y sus subcontratistas, incidentes de semanas y decisión del consejo con riesgos escritos", "coral", 13, True)
    f.arrow([(300, y0 + 225), (320, y0 + 225)])
    f.arrow([(610, y0 + 185), (630, y0 + 185)])
    f.text(14, y0 + 10, "Más irreversible → más evidencia exigida", 13, "start", 700, "#142231")
    return done(f, y0 + 286,
                "Lo que enseña: La migración estaba en el peldaño más alto; la evidencia que describe el Final Notice (pruebas hasta el día antes, una prueba clave reducida, un proveedor sin diligencia formal) se parece más a la de un peldaño inferior. Es una regla de diseño propia, no un criterio del regulador.",
                "teal", ANALISIS)


def organizacion() -> Fig:
    f, y = sketch("Quién contrataba con quién: propietario, banco, proveedor y regulador",
                  "Esquema de organizaciones y contratos: Banco Sabadell como propietario de TSB, el grupo holding y el banco TSB con su consejo y su comité ejecutivo, el proveedor SABIS con 85 terceros bajo contratos de servicios, Lloyds como proveedor anterior, y la FCA y la PRA como reguladores.")
    y0 = y + 6
    bx(f, 310, y0, 320, 56, "Banco Sabadell: propietario desde julio de 2015", "navy", 13, True)
    bx(f, 310, y0 + 84, 320, 56, "TSB Banking Group plc: holding; su consejo y el del banco", "teal", 13, True)
    bx(f, 310, y0 + 168, 320, 56, "TSB Bank plc: banco minorista; comité ejecutivo (BEC)", "teal", 13, True)
    f.arrow([(470, y0 + 56), (470, y0 + 84)])
    f.arrow([(470, y0 + 140), (470, y0 + 168)])
    bx(f, 10, y0 + 84, 250, 80, "Lloyds Banking Group: plataforma anterior; contrato hasta julio de 2024", "grey")
    bx(f, 680, y0 + 84, 250, 80, "SABIS (Sabadell Information Systems): diseña, construye, prueba, migra y opera", "coral", 13, True)
    f.arrow([(310, y0 + 196), (135, y0 + 164)], dashed=True)
    f.arrow([(630, y0 + 196), (805, y0 + 164)], "contrato de servicios", label_at=(560, y0 + 192))
    bx(f, 680, y0 + 220, 250, 60, "85 terceros de SABIS (cuartas partes para TSB)", "gold")
    f.arrow([(805, y0 + 164), (805, y0 + 220)], dashed=True)
    bx(f, 10, y0 + 250, 450, 56, "FCA y PRA: reguladores que sancionaron en diciembre de 2022", "plain", 13, True)
    bx(f, 480, y0 + 320, 450, 56, "5,2 millones de clientes (junio de 2014: banco escindido de Lloyds)", "plain")
    return done(f, y0 + 392,
                "Lo que enseña: el banco era una pieza de un grupo en el que el diseño, la construcción y la operación de la plataforma estaban en un proveedor del mismo propietario, con una cadena de subcontratistas debajo. El Final Notice destaca que el consejo debía supervisar ese proveedor como un tercero.",
                "gold", "Fuente: FCA, Final Notice, párrafos 2.1 a 2.4, 2.18 y 2.22 y definiciones. Plantilla, oficinas y organigrama interno: no se sabe.")


def hw_sw() -> Fig:
    f, y = sketch("Hardware y software de TSB: lo que se sabe y lo que no es público",
                  "Pila de seis capas: aplicaciones bancarias de la plataforma Proteo4UK, derivada de la plataforma española Proteo; migración de datos; documentación de diseño sustituida por documentos de configuración; dos centros de datos en configuración activo-activo con una configuración incoherente; lenguajes, sistemas operativos y hardware no constan.")
    y0 = y + 6
    capas = [("Aplicación: plataforma bancaria Proteo4UK, versión británica de Proteo, aún no probada en el Reino Unido (documentado)", "teal", "FCA, 2.3"),
             ("Migración: evento principal del 20 al 22 de abril de 2018; datos de clientes (documentado)", "teal", "FCA, 2.5"),
             ("Diseño y configuración: documentos de configuración en lugar de diseño (documentado)", "teal", "FCA, 2.21"),
             ("Dos centros de datos en activo-activo, configurados de forma incoherente según TSB (parcial)", "gold", "FCA, 2.14; TSB, 2019"),
             ("Lenguajes, frameworks, bases de datos, sistemas operativos (no se sabe)", "grey", "no consta"),
             ("Hardware, red, ubicación de los centros de datos y proveedores de nube (no se sabe)", "grey", "no consta")]
    for i, (t, k, s) in enumerate(capas):
        yy = y0 + i * 66
        bx(f, 10, yy, 640, 58, t, k, 13, k == "teal")
        bx(f, 670, yy, 250, 58, s, "plain", 13)
    return done(f, y0 + 6 * 66 + 4,
                "Lo que enseña: lo documentado de la tecnología es su procedencia, su configuración y su proceso de migración, no su implementación. El único detalle de infraestructura es la configuración activo-activo, con el relato de TSB sobre centros no idénticos. No se inventa ningún dato de hardware ni de lenguajes.",
                "gold", "Fuentes: FCA, Final Notice y TSB, comunicado del 19 de noviembre de 2019. Verde: documentado; dorado: en parte; gris: no se sabe.")


def prueba_de_fallos() -> Fig:
    f, y = sketch("A prueba de fallos: lo que existía, lo que falló y lo que debió existir",
                  "Tres columnas: mecanismos que existían (estructura de incidentes Bronze, Silver y Gold, playbooks de 48 horas, migración por etapas de algunos servicios, programa de reparación), los que fallaron o faltaban (retorno a Lloyds, prueba activo-activo, diligencia del proveedor, capacidad de quejas) y los que debieron existir.")
    y0 = y + 6
    cols = [("Existían (documentado)", "teal", ["Estructura de incidentes Bronze, Silver y Gold", "Playbooks para las primeras 48 horas", "Servicios migrados antes por etapas (según TSB)", "Plan maestro y replan", "Programa «Putting Things Right» desde mayo de 2018"]),
            ("Fallaron o faltaban (documentado)", "coral", ["Vuelta atrás a la plataforma de Lloyds", "Prueba de configuración activo-activo completa", "Diligencia formal del proveedor y de sus terceros", "Capacidad de contacto y de quejas", "Ejercicios de incidente de semanas"]),
            ("Debieron existir (análisis propio)", "gold", ["Migración por oleadas con retorno ensayado", "Criterio de salida con evidencia por irreversibilidad", "Reconciliación de datos por oleada", "Ejercicios conjuntos con el proveedor", "Plan de escalado de quejas desde el inicio"])]
    for c, (h, k, items) in enumerate(cols):
        x = 10 + c * 306
        bx(f, x, y0, 296, 40, h, k, 13, True)
        for i, t in enumerate(items):
            bx(f, x, y0 + 52 + i * 68, 296, 60, t, k, 13)
    return done(f, y0 + 52 + 5 * 68 + 4,
                "Lo que enseña: había estructuras de incidente y de plan, pero dimensionadas para horas o días y sin la posibilidad de volver atrás. La columna de la derecha es análisis propio.",
                "gold", "Fuente: FCA, Final Notice, párrafos 2.10 a 2.32 y TSB (2019); tercera columna: análisis propio.")


FIGURES = {
    "tsb-contexto.svg": contexto,
    "tsb-cascada-de-canales.svg": cascada,
    "tsb-linea-de-tiempo.svg": tiempos,
    "tsb-costos.svg": dinero,
    "tsb-mejoras.svg": mejoras,
    "tsb-contenedores.svg": capas,
    "tsb-secuencia-de-la-migracion.svg": secuencia,
    "tsb-despliegue-activo-activo.svg": activo_activo,
    "tsb-dependencias.svg": dependencias,
    "tsb-defensa-en-profundidad.svg": defensa,
    "tsb-arbol-de-fallas.svg": arbol,
    "tsb-antecedentes.svg": antecedentes,
    "tsb-doce-meses.svg": doce_meses,
    "tsb-explosion-de-una-vez-u-oleadas.svg": oleadas,
    "tsb-arquitectura-despues.svg": despues,
    "tsb-evidencia-segun-irreversibilidad.svg": escalera,
    "tsb-organizacion-y-contratos.svg": organizacion,
    "tsb-hardware-y-software.svg": hw_sw,
    "tsb-a-prueba-de-fallos.svg": prueba_de_fallos,
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
