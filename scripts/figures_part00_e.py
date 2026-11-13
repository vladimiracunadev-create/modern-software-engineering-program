"""Figures for SE-009 and SE-010."""
from __future__ import annotations

from figure_kit import Fig


def se009_escalas() -> Fig:
    f = Fig(940, 450, "Tres escalas de impacto de una decisión de software",
            "Tres filas: impacto directo, habilitado y sistémico. Para cada una se indican ejemplos, cómo se observa y "
            "qué decisión de diseño cambia.")
    rows = [
        ("Directo", "Construir y operar: cómputo, red, almacenamiento, dispositivos y trabajo humano",
         "Se mide con consumo y horas dentro de una frontera declarada", "Imágenes livianas, retención acotada, guardias rotativas", "teal"),
        ("Habilitado", "Cambios de conducta que el software facilita: menos viajes, o más consumo inducido",
         "Se hipotetiza y se monitorea; no se asume", "Medir volumen total, no solo costo por transacción", "gold"),
        ("Sistémico", "Efectos acumulados: el canal digital se vuelve la única vía y cierra alternativas",
         "Se observan señales por grupo y se consulta a quienes cargan el cambio", "Mantener una ruta alternativa con el mismo plazo", "coral"),
    ]
    f.text(20, 34, "Escala", 13, "start", 700)
    f.text(160, 34, "Ejemplo", 13, "start", 700)
    f.text(500, 34, "Cómo se observa", 13, "start", 700)
    f.text(730, 34, "Qué cambia en el diseño", 13, "start", 700)
    for i, (name, ex, obs, design, kind) in enumerate(rows):
        y = 46 + i * 120
        f.box(20, y, 130, 108, name, "navy", 14, bold=True)
        f.box(160, y, 330, 108, ex, kind, 13)
        f.box(500, y, 220, 108, obs, "plain", 13)
        f.box(730, y, 200, 108, design, "plain", 13)
    f.text(470, 430, "Un análisis responsable formula hipótesis sobre lo habilitado y lo sistémico; no inventa certeza.", 13, "middle")
    return f


def se009_rebote() -> Fig:
    f = Fig(900, 420, "Efecto rebote: más eficiente por transacción, más consumo total",
            "Gráfico de barras con datos sintéticos en índice 100. El costo por transacción baja a 60, el número de "
            "transacciones sube a 220 y el consumo total sube a 132.")
    base, unit, x0 = 330, 1.2, 80
    f.line(x0, base, 600, base, "#32505f", width=1.8)
    f.line(x0, 40, x0, base, "#32505f", width=1.8)
    f.text(x0 - 8, 44, "índice", 13, "end")
    groups = [("Costo por transacción", 100, 60), ("Número de transacciones", 100, 220), ("Consumo total", 100, 132)]
    for k, (name, before, after) in enumerate(groups):
        gx = x0 + 30 + k * 170
        f.box(gx, base - before * unit, 52, before * unit, "", "grey", radius=3)
        kind = "teal" if after < before else "coral"
        f.box(gx + 58, base - after * unit, 52, after * unit, "", kind, radius=3)
        f.text(gx + 26, base - before * unit - 8, str(before), 13, weight=700)
        f.text(gx + 84, base - after * unit - 8, str(after), 13, weight=700)
        f.text(gx + 55, base + 22, name, 13)
    f.box(640, 60, 240, 100, "Cada transacción es 40 % más barata, pero se hacen 2,2 veces más: 0,6 × 2,2 = 1,32.", "coral", 13)
    f.box(640, 178, 240, 100, "Barra gris = antes (índice 100). Barra de color = después; el número confirma el sentido.", "grey", 13)
    f.box(640, 296, 240, 90, "La optimización local no garantiza reducir el total: mide volumen y conducta dentro de la frontera.", "gold", 13)
    f.text(340, 398, "Datos sintéticos de ilustración; no son mediciones.", 13, "middle", 400, "#5c1f14")
    return f


def se009_barreras() -> Fig:
    f = Fig(960, 480, "De la barrera detectada a la alternativa y su señal",
            "Tabla de cinco barreras detectadas en la matrícula solo digital, el diseño que las atiende y la señal "
            "con su guardrail. Todas conservan resultado, plazo comparable, privacidad y derecho a recuperación.")
    heads = ["Barrera detectada", "Diseño alternativo", "Señal y guardrail"]
    rows = [
        ("Dispositivo compartido o antiguo", "HTML liviano, reanudación sin pérdida de datos", "Finalización por tipo de dispositivo; carga de soporte"),
        ("Conectividad baja o intermitente", "Documentos mínimos, imágenes comprimidas, estado consultable", "Abandono por franja de conectividad; reintentos"),
        ("Tecnología asistiva", "Teclado completo, texto alternativo, pruebas de tarea con la tecnología", "Tareas completadas con tecnología asistiva"),
        ("Necesidad de privacidad", "Confirmación por canal elegible, sin exponer historial ni notificaciones", "Solicitudes de cambio de canal; incidentes de exposición"),
        ("Guardia nocturna concentrada", "Automatización, rotación y límites de carga para el equipo", "Interrupciones por persona; rotación del equipo"),
    ]
    xs, ws = [10, 290, 690], [245, 370, 260]
    for j, h in enumerate(heads):
        f.box(xs[j], 12, ws[j], 40, h, "navy", 14, bold=True)
    for i, (a, b, c) in enumerate(rows):
        y = 60 + i * 66
        f.box(xs[0], y, ws[0], 58, a, "coral", 13)
        f.box(xs[1], y, ws[1], 58, b, "teal", 13)
        f.box(xs[2], y, ws[2], 58, c, "gold", 13)
        f.arrow([(xs[0] + ws[0], y + 29), (xs[1], y + 29)])
        f.arrow([(xs[1] + ws[1], y + 29), (xs[2], y + 29)])
    f.box(10, 396, 940, 72, "Invariantes de toda alternativa: el mismo resultado esencial, un plazo comparable, privacidad y derecho a recuperación. "
          "Una ruta lenta o estigmatizante no cuenta como alternativa.", "grey", 13)
    return f


def se010_cadena() -> Fig:
    f = Fig(960, 520, "La cadena afirmación a límite aplicada a «Campus Abierto cumple ISO 25010»",
            "Seis pasos, cada uno con el ejemplo del caso conductor: la afirmación original se divide en preguntas, "
            "se localiza la fuente y su edición, se lee el pasaje visible y se declara qué no demuestra.")
    steps = [
        ("1 Afirmación", "«Cumplimos ISO 25010» (sin edición, alcance ni evidencia)", "coral"),
        ("2 Pregunta", "¿Qué modelo, qué características, qué escenarios y medidas, y quién afirma conformidad?", "gold"),
        ("3 Fuente candidata", "Ficha oficial de ISO/IEC 25010:2023; ISO/IEC 25019:2023 para calidad en uso", "teal"),
        ("4 Versión y autoridad", "Edición 2023; ISO tiene autoridad sobre el modelo, no sobre nuestra evaluación", "teal"),
        ("5 Pasaje e interpretación", "La ficha confirma nombre, edición y alcance general; el equipo eligió escenarios y umbrales", "teal"),
        ("6 Límite", "Revisión interna de fiabilidad, desempeño y compatibilidad; no es certificación ni calidad en uso", "grey"),
    ]
    for i, (name, text, kind) in enumerate(steps):
        y = 20 + i * 82
        f.box(20, y, 210, 66, name, "navy", 14, bold=True)
        f.box(244, y, 690, 66, text, kind, 13)
        if i < 5:
            f.arrow([(125, y + 66), (125, y + 82)])
    f.text(480, 514, "Cada paso omitido convierte la cita en eslogan: otra persona debe poder hallar el soporte sin adivinar.", 13, "middle")
    return f


def se010_tipos() -> Fig:
    f = Fig(960, 440, "Qué puede y qué no puede sostener cada tipo de fuente",
            "Tabla de cuatro tipos de fuente (estándar, especificación, documentación oficial y artículo o libro) "
            "con lo que sostienen bien, lo que no sostienen y su riesgo típico.")
    cols = ["Estándar", "Especificación", "Documentación oficial", "Artículo o libro"]
    rows = [
        ("Sostiene bien", ["Vocabulario, modelos y requisitos consensuados en un alcance", "Contrato preciso e interoperabilidad", "Comportamiento soportado de una versión", "Método, datos y discusión; explicación conectada"]),
        ("No sostiene", ["El umbral adecuado para tu producto", "Cómo lo implementa tu sistema", "Comparaciones imparciales con alternativas", "Que el resultado valga en tu contexto"]),
        ("Riesgo típico", ["Citar la ficha pública como si fuera la cláusula", "Copiar una frase sin su condición o excepción", "Autoridad confundida con adecuación", "Fuente secundaria usada para afirmar conformidad"]),
    ]
    f.box(10, 12, 150, 40, "", "navy")
    for j, c in enumerate(cols):
        f.box(166 + j * 196, 12, 190, 40, c, "navy", 13, bold=True)
    for i, (label, cells) in enumerate(rows):
        y = 60 + i * 110
        f.box(10, y, 150, 102, label, "grey", 13, bold=True)
        for j, cell in enumerate(cells):
            kind = ["teal", "coral", "gold"][i]
            f.box(166 + j * 196, y, 190, 102, cell, kind, 13)
    f.text(480, 410, "La selección se basa en aptitud para la afirmación, no en prestigio general: se prefiere la fuente más próxima capaz de sostenerla.", 13, "middle")
    f.text(480, 430, "Si el estándar completo es de pago y solo se vio la ficha, se cita la ficha únicamente para metadatos visibles.", 13, "middle")
    return f


def se010_vigencia() -> Fig:
    f = Fig(940, 400, "Cadena de sustitución: la edición cambia lo que significa citar",
            "Dos líneas de tiempo. ISO/IEC 25010 pasó de un solo documento de 2011 con producto y calidad en uso a "
            "dos documentos en 2023. RFC 7231, de 2014, fue reemplazado por RFC 9110, de 2022.")
    f.text(20, 34, "Estándar ISO", 14, "start", 700)
    f.line(40, 90, 900, 90, "#32505f", width=2)
    f.dot(160, 90, "A")
    f.text(160, 124, "2011", 13, "middle", 700)
    f.box(40, 140, 240, 78, "ISO/IEC 25010:2011: modelos de calidad del producto y de calidad en uso en un documento", "grey", 13)
    f.dot(660, 90, "B")
    f.text(660, 124, "2023", 13, "middle", 700)
    f.box(470, 140, 220, 78, "ISO/IEC 25010:2023: solo calidad del producto", "teal", 13)
    f.box(700, 140, 220, 78, "ISO/IEC 25019:2023: calidad en uso", "teal", 13)
    f.arrow([(280, 90), (630, 90)], "se reorganiza", label_at=(455, 80))
    f.text(20, 262, "Especificación HTTP", 14, "start", 700)
    f.line(40, 292, 900, 292, "#32505f", width=2)
    f.dot(160, 292, "C")
    f.text(160, 326, "2014", 13, "middle", 700)
    f.box(40, 340, 240, 50, "RFC 7231 (HTTP/1.1 semántica)", "grey", 13)
    f.dot(660, 292, "D")
    f.text(660, 326, "2022", 13, "middle", 700)
    f.box(470, 340, 330, 50, "RFC 9110 (HTTP semántica): obsoleta a RFC 7231", "teal", 13)
    f.arrow([(280, 292), (630, 292)], "obsoletado por", label_at=(455, 282))
    return f


FIGURES = {
    "se-009-escalas-de-impacto.svg": se009_escalas,
    "se-009-efecto-rebote.svg": se009_rebote,
    "se-009-barrera-alternativa-senal.svg": se009_barreras,
    "se-010-cadena-de-trazabilidad.svg": se010_cadena,
    "se-010-tipos-de-fuente.svg": se010_tipos,
    "se-010-cadena-de-sustitucion.svg": se010_vigencia,
}
