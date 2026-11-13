"""Figures for SE-007 and SE-008."""
from __future__ import annotations

from figure_kit import Fig


def se007_cadena() -> Fig:
    f = Fig(940, 470, "Métricas verdes en dos capas, abandono en la tercera",
            "Tres columnas: calidad interna, producto en ejecución y calidad en uso. Para cada una se muestra lo que el "
            "tablero mide y lo que no observa. Las dos primeras capas muestran valores aceptables mientras la tercera "
            "muestra abandono; la idempotencia de la confirmación no se observa en ninguna.")
    cols = [
        ("Calidad interna", "Cobertura 90 %, linter limpio, baja complejidad", "No observa si las aserciones prueban la regla ni si hay idempotencia", "teal"),
        ("Producto en ejecución", "p95 de la API por debajo del objetivo", "No observa reintentos con la misma clave ni estados contradictorios", "teal"),
        ("Calidad en uso", "Abandono del flujo y llamadas a soporte", "Es la señal que sí muestra el daño; llega tarde y sin causa", "coral"),
    ]
    for i, (name, measures, blind, kind) in enumerate(cols):
        x = 30 + i * 300
        f.box(x, 24, 270, 46, name, "navy", 14, bold=True)
        f.text(x + 135, 96, "El tablero muestra", 13, "middle", 700)
        f.box(x, 106, 270, 84, measures, kind, 13)
        f.text(x + 135, 218, "No observa", 13, "middle", 700)
        f.box(x, 228, 270, 84, blind, "grey", 13)
        if i < 2:
            f.arrow([(x + 270, 148), (x + 300, 148)], "¿evidencia?", label_at=(x + 285, 92))
    f.box(30, 340, 870, 70, "Cada flecha es una hipótesis: código legible facilita cambiar, pero no asegura que la persona complete su tarea. "
          "Hace falta un escenario que una las tres capas.", "gold", 13)
    f.text(465, 442, "Los valores son ilustrativos del caso Campus Abierto; no son mediciones.", 13, "middle")
    return f


def se007_escenario() -> Fig:
    f = Fig(960, 430, "Anatomía de un escenario de calidad con un ejemplo completo",
            "Seis elementos del escenario: fuente, estímulo, entorno, artefacto, respuesta y medida, rellenados con el "
            "ejemplo de la confirmación repetida durante la apertura de matrícula.")
    f.group(10, 70, 940, 230, "Entorno: apertura de matrícula, 2.000 sesiones, conectividad móvil inestable", "grey")
    items = [
        ("1 Fuente", "Estudiante con conexión intermitente", "plain"),
        ("2 Estímulo", "Repite la confirmación con la misma clave", "plain"),
        ("4 Artefacto", "Servicio de confirmación de matrícula", "plain"),
        ("5 Respuesta", "Conserva un único cupo; muestra estado comprensible; permite consultarlo después", "teal"),
    ]
    xs = [30, 270, 510, 735]
    ws = [210, 210, 200, 205]
    for (name, text, kind), x, w in zip(items, xs, ws):
        f.box(x, 130, w, 50, name, "navy", 14, bold=True)
        f.box(x, 186, w, 100, text, kind, 13)
    for a, b in [(0, 1), (1, 2), (2, 3)]:
        f.arrow([(xs[a] + ws[a], 155), (xs[b], 155)])
    f.text(480, 56, "3 Entorno (recuadro)", 13, "middle", 700)
    f.box(30, 320, 900, 90, "6 Medida: cero cupos duplicados en reintentos; estado visible en ≤ 10 s para el percentil que se declare; "
          "la persona recupera su confirmación sin reiniciar. Los umbrales se justifican por necesidad, historial o prueba con personas, "
          "no por copiar un número común.", "gold", 13)
    return f


def se007_goodhart() -> Fig:
    f = Fig(900, 430, "Cuando una medida se convierte en objetivo",
            "Gráfico de líneas con datos sintéticos en índice 100: el tiempo de finalización baja de forma sostenida "
            "durante seis sprints mientras el abandono sube. Sin un guardrail, la mejora del indicador oculta el daño.")
    x0, y0, base, w, h = 80, 50, 320, 560, 250
    f.line(x0, base, x0 + w, base, "#32505f", width=1.8)
    f.line(x0, y0, x0, base, "#32505f", width=1.8)
    f.text(x0 - 10, y0 + 4, "índice", 13, "end")
    tiempo = [100, 92, 85, 78, 70, 64]
    abandono = [100, 104, 115, 131, 150, 172]
    top, bottom = 180, 50
    def y(v):
        return base - (v - bottom) / (top - bottom) * h
    xs = [x0 + 40 + i * 100 for i in range(6)]
    f.arrow([(a, y(v)) for a, v in zip(xs, tiempo)], color="#32505f")
    f.arrow([(a, y(v)) for a, v in zip(xs, abandono)], dashed=True, color="#c0432f")
    for a, v in zip(xs, tiempo):
        f.dot(a, y(v), "", "teal")
    for a, v in zip(xs, abandono):
        f.box(a - 8, y(v) - 8, 16, 16, "", "coral", radius=2)
    for i, a in enumerate(xs):
        f.text(a, base + 22, f"S{i}", 13)
    f.text(xs[-1] + 26, y(tiempo[-1]) + 4, "tiempo 64", 13, "start")
    f.text(xs[-1] + 26, y(abandono[-1]) + 4, "abandono 172", 13, "start", 700, "#5c1f14")
    f.box(690, 60, 190, 100, "Línea continua con círculos: tiempo de finalización (el objetivo).", "teal", 13)
    f.box(690, 176, 190, 100, "Línea discontinua con cuadrados: abandono (el guardrail).", "coral", 13)
    f.box(690, 292, 190, 90, "Sprint 0 = 100. Datos sintéticos, no medidos.", "grey", 13)
    f.text(380, 400, "Si se optimiza una sola señal, las personas y el sistema se adaptan: añade guardrails y revisa distribución.", 13, "middle")
    return f


def se008_embudo() -> Fig:
    f = Fig(940, 470, "Restricciones filtran, preferencias ordenan, supuestos se revisan",
            "Embudo de decisión: seis opciones iniciales, tres tras aplicar las restricciones duras y una decisión tras "
            "comparar con preferencias. A un lado, el fallo de declarar todas las preferencias como duras.")
    f.box(40, 30, 520, 62, "Seis opciones iniciales (incluye «no hacer nada» y alternativas poco obvias)", "grey", 13, bold=True)
    f.arrow([(300, 92), (300, 122)])
    f.box(40, 122, 520, 44, "Filtro: restricciones duras (con fuente, vigencia y autoridad)", "coral", 13, bold=True)
    f.arrow([(300, 166), (300, 196)])
    f.box(90, 196, 420, 62, "Tres opciones viables: confirmación síncrona central · reserva temporal · aceptación asincrónica", "teal", 13)
    f.arrow([(300, 258), (300, 288)])
    f.box(40, 288, 520, 44, "Comparación: preferencias graduadas, sensibilidad y evidencia", "gold", 13, bold=True)
    f.arrow([(300, 332), (300, 362)])
    f.box(110, 362, 380, 62, "Decisión: reserva temporal, con propietario, fecha y disparadores de revisión", "navy", 13, bold=True)
    f.box(600, 30, 320, 200, "Fallo: si cada deseo se declara «innegociable», el filtro deja una sola opción —la elegida de antemano— "
          "y la comparación se vuelve teatro. Revalida la fuente de cada restricción.", "coral", 13)
    f.box(600, 250, 320, 174, "Supuestos: completan información faltante. Cada uno lleva una condición de revisión, "
          "por ejemplo «si el proveedor cambia su contrato, se reabre la decisión».", "grey", 13)
    return f


def se008_tradeoff() -> Fig:
    f = Fig(960, 440, "Trade-offs entre tres opciones de reserva de cupos",
            "Tabla cualitativa de tres opciones por seis atributos, con símbolos: alto, medio o bajo. La reserva "
            "temporal conserva experiencia rápida con estado honesto, a costa de relojes, idempotencia y recuperación.")
    cols = ["Atributo", "Confirmación síncrona central", "Reserva temporal con expiración", "Aceptación asincrónica y conciliación"]
    rows = [
        ("Verdad visible al instante", ["▲ alta", "▬ media", "▼ baja"]),
        ("Latencia percibida", ["▼ alta espera", "▬ breve", "▲ inmediata"]),
        ("Dependencia de un solo punto", ["▲ concentrada", "▬ moderada", "▼ absorbe picos"]),
        ("Complejidad operativa", ["▼ baja", "▲ relojes e idempotencia", "▲ conciliación"]),
        ("Honestidad ante la persona", ["▲ clara", "▲ estado consultable", "▼ riesgo si se comunica como confirmación"]),
        ("Reversibilidad", ["▬ media", "▲ expira sola", "▬ requiere compensación"]),
    ]
    widths = [250, 210, 230, 250]
    xs = [10, 262, 474, 706]
    for j, c in enumerate(cols):
        f.box(xs[j], 12, widths[j] - 2, 46, c, "navy", 13, bold=True)
    for i, (attr, cells) in enumerate(rows):
        y = 64 + i * 52
        f.box(xs[0], y, widths[0] - 2, 46, attr, "grey", 13, bold=True)
        for j, cell in enumerate(cells, start=1):
            kind = "teal" if j == 2 else "plain"
            f.box(xs[j], y, widths[j] - 2, 46, cell, kind, 13)
    f.text(480, 400, "▲ favorece el atributo · ▬ intermedio · ▼ lo perjudica o exige más. La columna central se eligió: condición dura, no comunicar", 13, "middle")
    f.text(480, 420, "matrícula definitiva antes de confirmarla. Reabrir si las compensaciones superan el umbral o cambia el contrato del proveedor.", 13, "middle")
    return f


def se008_riesgo() -> Fig:
    f = Fig(960, 440, "Anatomía de un riesgo y dónde actúa cada tipo de control",
            "Línea de tiempo de causa, evento y consecuencia con cuatro tipos de control: la mitigación actúa antes del evento, "
            "la detección y la contingencia después, y la transferencia financiera no repara la consecuencia no financiera.")
    f.box(20, 150, 230, 90, "Causa: reserva y pago se confirman en sistemas distintos", "grey", 13)
    f.box(365, 150, 230, 90, "Evento: una demora del proveedor libera un cupo ya cobrado", "coral", 13, bold=True)
    f.box(710, 150, 230, 90, "Consecuencia: reparación manual y una persona sin cupo pagado", "grey", 13)
    f.arrow([(250, 195), (365, 195)], "puede producir", label_at=(307, 187))
    f.arrow([(595, 195), (710, 195)], "provoca", label_at=(652, 187))
    f.box(20, 30, 330, 70, "Mitigación (antes): reduce probabilidad o impacto. Ej.: reserva con clave idempotente", "teal", 13)
    f.arrow([(185, 100), (185, 150)], dashed=True)
    f.box(380, 30, 200, 70, "Detección: señales del evento (observabilidad)", "gold", 13)
    f.arrow([(480, 100), (480, 150)], dashed=True)
    f.box(380, 290, 200, 80, "Contingencia (después): conciliar, avisar y reasignar el cupo", "teal", 13)
    f.arrow([(480, 240), (480, 290)], dashed=True)
    f.box(710, 290, 230, 80, "Transferencia: cubre el costo financiero, no repara el acceso ni la confianza", "gold", 13)
    f.arrow([(825, 240), (825, 290)], dashed=True)
    f.text(480, 412, "Nombrar el tipo de control evita prometer más de lo que hace: observar no reduce la probabilidad.", 13, "middle")
    return f


FIGURES = {
    "se-007-cadena-de-calidad.svg": se007_cadena,
    "se-007-escenario-de-calidad.svg": se007_escenario,
    "se-007-medida-como-objetivo.svg": se007_goodhart,
    "se-008-embudo-de-decision.svg": se008_embudo,
    "se-008-tabla-de-tradeoffs.svg": se008_tradeoff,
    "se-008-anatomia-de-un-riesgo.svg": se008_riesgo,
}
