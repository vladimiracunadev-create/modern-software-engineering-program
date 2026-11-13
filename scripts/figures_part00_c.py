"""Figures for SE-005 and SE-006."""
from __future__ import annotations

import math

from figure_kit import Fig


def se005_incidente() -> Fig:
    f = Fig(960, 520, "Red de colaboración durante el incidente de matrículas duplicadas",
            "Un nodo central, el incidente, rodeado de siete roles. Cada rol indica qué aporta o decide; "
            "operación puede detener nuevas confirmaciones si se cruza un umbral acordado y el líder conserva la línea temporal.")
    cx, cy = 480, 262
    f.box(cx - 105, cy - 38, 210, 76, "Incidente: matrículas duplicadas", "navy", 14, bold=True)
    nodes = [
        ("Líder del incidente", "mantiene la línea temporal y la imagen compartida", "gold"),
        ("Soporte", "clasifica reclamos y comunica el impacto", "teal"),
        ("Desarrollo", "compara el cambio reciente (timeout)", "teal"),
        ("Datos", "diseña la reconciliación de escrituras", "teal"),
        ("Seguridad", "separa abuso de reintento legítimo", "teal"),
        ("Producto", "decide la experiencia de reparación", "teal"),
        ("Operación", "puede detener nuevas confirmaciones al umbral", "coral"),
    ]
    rx, ry = 340, 195
    for k, (name, role, kind) in enumerate(nodes):
        angle = -math.pi / 2 + k * 2 * math.pi / len(nodes)
        x = cx + rx * math.cos(angle)
        y = cy + ry * math.sin(angle)
        f.arrow([(cx + 90 * math.cos(angle) * 0.0 + (x - cx) * 0.34, cy + (y - cy) * 0.52),
                 (cx + (x - cx) * 0.7, cy + (y - cy) * 0.78)], dashed=True)
        f.box(x - 100, y - 36, 200, 72, f"{name}\n{role}", kind, 13)
    f.text(480, 508, "Decisión final: registra evidencia y voces disidentes. Un líder coordina; no necesita diagnosticar todo.",
           13, "middle", 400)
    return f


def se005_derechos() -> Fig:
    f = Fig(960, 420, "Derechos de decisión proporcionales al riesgo",
            "Tabla de cuatro decisiones por seis dimensiones: quién propone, decide, revisa de forma independiente, "
            "acepta el riesgo, puede detener y cómo se registra el desacuerdo. A mayor impacto e irreversibilidad, "
            "más se separan los incentivos.")
    cols = ["Propone", "Decide", "Revisión independiente", "Acepta el riesgo", "Puede detener", "Registro de desacuerdo"]
    rows = [
        ("Cambiar un texto reversible", ["Quien lo escribe", "El mismo equipo", "Revisión automática", "El equipo", "Cualquiera con acceso", "En el commit"]),
        ("Cambiar la semántica de cupos", ["Producto", "Producto + secretaría", "Ingeniería + datos", "Producto", "Operación", "En la decisión (ADR)"]),
        ("Liberar la migración de identidad", ["Identidad", "Comité con autoridad nombrada", "Seguridad externa al equipo", "Quien posee el servicio", "Operación y seguridad", "Acta con voces disidentes"]),
        ("Detener confirmaciones en un incidente", ["Operación", "Líder del incidente", "Después, en la retrospectiva", "Líder del incidente", "Líder o umbral automático", "Línea temporal"]),
    ]
    f.box(10, 12, 190, 44, "Decisión", "navy", 13, bold=True)
    for j, c in enumerate(cols):
        f.box(206 + j * 124, 12, 118, 44, c, "navy", 12, bold=True)
    for i, (name, cells) in enumerate(rows):
        y = 64 + i * 78
        f.box(10, y, 190, 70, name, "grey", 13, bold=True)
        for j, cell in enumerate(cells):
            kind = "plain" if i < 1 else "teal" if i < 3 else "coral"
            f.box(206 + j * 124, y, 118, 70, cell, kind, 12)
    f.text(480, 392, "Claro = bajo riesgo reversible · verde azulado = alto impacto · rojo = urgencia con autoridad pre-acordada.", 13, "middle")
    f.text(480, 412, "La gobernanza crece con el impacto y la irreversibilidad; un texto reversible no necesita la de una migración.", 13, "middle")
    return f


def se005_silo() -> Fig:
    f = Fig(940, 430, "Cuándo entra la especialidad cambia lo que se puede corregir",
            "Línea de tiempo con cuatro hitos: idea, diseño fijado, construcción y liberación. Si seguridad entra "
            "solo como aprobación final, el diseño ya depende de supuestos costosos; si participa al modelar amenazas, "
            "ajusta el flujo antes de fijarlo. La altura cualitativa de las barras indica lo costoso de cambiar.")
    xs = [110, 330, 550, 770]
    names = ["Idea", "Diseño fijado", "Construcción", "Liberación"]
    f.line(60, 150, 880, 150, "#32505f", width=2)
    for x, n in zip(xs, names):
        f.dot(x, 150, str(xs.index(x) + 1))
        f.text(x, 184, n, 13, "middle", 700)
    heights = [20, 50, 90, 130]
    for x, h in zip(xs, heights):
        f.box(x - 24, 150 - 24 - h, 48, h, "", "grey", radius=3)
    f.text(110, 22, "Costo cualitativo de cambiar un supuesto (sube con cada hito)", 13, "start", 700)
    f.box(40, 220, 400, 96, "B · Seguridad modela amenazas con el diseño: el flujo se ajusta antes de fijarse. "
          "Su juicio cambia la decisión.", "teal", 13)
    f.arrow([(330, 192), (330, 220)], dashed=True)
    f.box(500, 220, 400, 96, "A · Seguridad entra al final: aprueba o rechaza lo ya construido. Si detecta un patrón de abuso, "
          "el rediseño toca un flujo implementado.", "coral", 13)
    f.arrow([(770, 192), (770, 220)], dashed=True)
    f.box(40, 340, 860, 60, "Soporte y operación cierran el bucle: si resuelven un error a mano sin registrarlo, "
          "ingeniería pierde la evidencia que corregiría el diseño.", "gold", 13)
    return f


def se006_observacion() -> Fig:
    f = Fig(940, 460, "De «la API estuvo lenta» a cuatro tipos de enunciado",
            "Una afirmación vaga se descompone en observación, inferencia, hipótesis y supuesto, con una "
            "pregunta de prueba para cada una: quien discrepa puede aceptar la observación y discutir la inferencia.")
    f.box(20, 20, 280, 70, "«La API estuvo lenta por la base de datos»: mezcla hecho y causa", "coral", 14, bold=True)
    f.arrow([(95, 90), (95, 116)])
    items = [
        ("Observación", "p95 subió de 220 a 480 ms durante 15 minutos en la región A, tras el despliegue X.",
         "¿Otra persona aceptaría el dato con el método declarado?", "teal"),
        ("Inferencia", "La dependencia Y contribuyó a la demora.",
         "¿Qué explicación conecta datos y conclusión? ¿Hay rivales?", "gold"),
        ("Hipótesis", "Si Y es la causa dominante, aislarla reducirá la cola.",
         "¿Qué resultado la refutaría? ¿Se escribió antes de medir?", "gold"),
        ("Supuesto", "La carga de prueba es representativa del tráfico real.",
         "¿Qué pasa con la decisión si el supuesto es falso?", "grey"),
    ]
    for i, (kind_name, text, question, kind) in enumerate(items):
        y = 120 + i * 82
        f.box(20, y, 150, 70, kind_name, "navy", 14, bold=True)
        f.box(176, y, 430, 70, text, kind, 13)
        f.box(612, y, 310, 70, question, "plain", 13)
    f.text(616, 108, "Pregunta de control", 13, "start", 700)
    f.text(180, 108, "Ejemplo", 13, "start", 700)
    f.text(470, 452, "El registro permite aceptar la observación y disputar la inferencia sin negar los datos.", 13, "middle")
    return f


def se006_latencia() -> Fig:
    f = Fig(960, 470, "Mismo p95, causas distintas: el desglose discrimina",
            "Barras horizontales apiladas con datos sintéticos. Antes: 220 ms. Después, tres escenarios que suman 480 ms: "
            "pool de conexiones agotado, consulta más costosa o proveedor de identidad lento. La métrica total no distingue "
            "entre ellos; el desglose por tramo sí.")
    parts = [("app", "Aplicación", "plain"), ("pool", "Espera de pool", "gold"), ("db", "Base de datos", "teal"),
             ("id", "Identidad externa", "coral"), ("net", "Red", "grey")]
    rows = [
        ("Antes (220 ms)", [40, 20, 90, 60, 10]),
        ("Escenario A: pool agotado (480 ms)", [40, 280, 90, 60, 10]),
        ("Escenario B: consulta costosa (480 ms)", [40, 20, 350, 60, 10]),
        ("Escenario C: identidad lenta (480 ms)", [40, 20, 90, 320, 10]),
    ]
    scale, x0 = 1.15, 40
    f.text(x0, 28, "Tiempo por tramo (ms, datos sintéticos). Cada color tiene etiqueta; el ancho también codifica el valor.", 13, "start", 700)
    for i, (label, vals) in enumerate(rows):
        y = 76 + i * 78
        f.text(x0, y - 8, label, 13, "start", 700)
        x = x0
        for (key, name, kind), v in zip(parts, vals):
            w = v * scale
            f.box(x, y, w, 36, str(v) if w > 22 else "", kind, 12, radius=2)
            x += w
    ly = 400
    for k, (key, name, kind) in enumerate(parts):
        f.box(40 + k * 186, ly, 22, 16, "", kind, radius=2)
        f.text(68 + k * 186, ly + 13, name, 13, "start")
    f.text(480, 448, "Una hipótesis útil predice qué tramo crece: así una sola medición puede debilitar a tres explicaciones.", 13, "middle")
    return f


def se006_incertidumbre() -> Fig:
    f = Fig(900, 470, "Cuánta evidencia pedir según reversibilidad e impacto",
            "Cuadrícula de dos por dos: reversible o irreversible frente a impacto bajo o alto. Cada cuadrante "
            "sugiere una forma de actuar ante la incertidumbre, desde una exposición pequeña observada hasta "
            "evidencia fuerte con revisión independiente.")
    f.text(450, 24, "Impacto de equivocarse", 14, "middle", 700)
    f.text(285, 54, "Bajo", 13, "middle", 700)
    f.text(615, 54, "Alto", 13, "middle", 700)
    f.text(40, 175, "Reversible", 13, "middle", 700)
    f.text(40, 335, "Irreversible", 13, "middle", 700)
    f.box(110, 70, 350, 150, "Reversible + bajo: exposición pequeña y observada. Aprende en producción con una señal de parada.", "teal", 13)
    f.box(470, 70, 350, 150, "Reversible + alto: piloto con cohorte limitada, comparación y parada automática antes de ampliar.", "gold", 13)
    f.box(110, 230, 350, 150, "Irreversible + bajo: ensayo previo y revisión por pares; confirma que de verdad no se puede revertir.", "gold", 13)
    f.box(470, 230, 350, 150, "Irreversible + alto: evidencia fuerte, revisión independiente, umbral alto y autoridad de parada nombrada.", "coral", 13, bold=True)
    f.box(110, 396, 710, 56, "Antes de investigar más: ¿cambiar este supuesto cambia la opción preferida? Si no, el dato adicional no vale su costo.",
          "grey", 13)
    return f


FIGURES = {
    "se-005-red-de-incidente.svg": se005_incidente,
    "se-005-derechos-de-decision.svg": se005_derechos,
    "se-005-silo-y-momento.svg": se005_silo,
    "se-006-observacion-a-supuesto.svg": se006_observacion,
    "se-006-latencia-desglose.svg": se006_latencia,
    "se-006-incertidumbre.svg": se006_incertidumbre,
}
