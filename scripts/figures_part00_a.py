"""Figures for SE-001 and SE-002."""
from __future__ import annotations

from figure_kit import Fig


def se001_fronteras() -> Fig:
    f = Fig(900, 440, "Tres fronteras anidadas para Campus Abierto",
            "Una frontera de sistema contiene al producto de matrícula, y este contiene a la aplicación web. "
            "Cada nivel responde una pregunta distinta, indicada con los números 1, 2 y 3.")
    f.group(20, 20, 580, 405, "③ Sistema universitario de matrícula")
    f.group(40, 56, 540, 218, "② Producto de matrícula", "teal")
    f.group(58, 90, 312, 168, "① Aplicación web", "gold")
    f.box(72, 124, 138, 56, "Interfaz y validación local", "plain", 13)
    f.box(220, 124, 138, 56, "Llamadas a API", "plain", 13)
    f.box(72, 192, 286, 52, "Estado consultable de cada solicitud", "plain", 13)
    f.box(386, 100, 178, 70, "Soporte y operación", "plain", 13)
    f.box(386, 184, 178, 70, "Datos propios y registro de decisiones", "plain", 13)
    f.box(40, 300, 128, 100, "Secretaría y reglas académicas", "gold", 13)
    f.box(180, 300, 118, 100, "Identidad", "grey", 13)
    f.box(310, 300, 134, 100, "Pagos (proveedor externo)", "coral", 13, dashed=True)
    f.box(456, 300, 124, 100, "Cupos (sistema heredado)", "grey", 13)
    f.text(310, 416, "Línea discontinua = depende de un tercero: el deber de informar no se externaliza",
           13, "middle", 400, "#5c1f14")
    questions = [
        (80, "①", "Aplicación", "¿La solicitud se captura y se transmite bien?", "gold"),
        (178, "②", "Producto", "¿La persona completa y entiende el trámite?", "teal"),
        (276, "③", "Sistema", "¿La capacidad funciona de extremo a extremo?", "grey"),
    ]
    for y, mark, name, question, kind in questions:
        f.box(630, y, 250, 88, question, kind, 13, inset_top=30)
        f.dot(656, y + 24, {"①": "1", "②": "2", "③": "3"}[mark])
        f.text(676, y + 29, name, 14, "start", 700)
    return f


def se001_solicitud() -> Fig:
    f = Fig(900, 560, "Una solicitud de matrícula recorre cinco actores",
            "Diagrama de secuencia: el portal responde 200 OK antes de que el cupo esté reservado y el pago "
            "confirmado. El pago devuelve una respuesta incierta y el portal debe publicar un estado consultable.")
    lanes = [("Estudiante", 90), ("Portal", 270), ("Reglas y secretaría", 460), ("Cupos (heredado)", 660), ("Pagos", 820)]
    for name, x in lanes:
        f.box(x - 70, 14, 140, 44, name, "navy", 13, bold=True)
        f.line(x, 58, x, 540, dashed=True)
    x = dict(lanes)
    step = [96, 150, 204, 258, 312, 366, 440]
    f.arrow([(x["Estudiante"], step[0]), (x["Portal"], step[0])], "1 solicitar matrícula")
    f.arrow([(x["Portal"], step[1]), (x["Estudiante"], step[1])], "2 «200 OK: recibido»", dashed=True)
    f.arrow([(x["Portal"], step[2]), (x["Reglas y secretaría"], step[2])], "3 validar elegibilidad")
    f.arrow([(x["Reglas y secretaría"], step[3]), (x["Cupos (heredado)"], step[3])], "4 reservar cupo (hasta 15 min)")
    f.arrow([(x["Portal"], step[4]), (x["Pagos"], step[4])], "5 cobrar", label_at=(560, step[4] - 6))
    f.arrow([(x["Pagos"], step[5]), (x["Portal"], step[5])], "6 sin respuesta (tiempo agotado)",
            color="#c0432f", label_at=(560, step[5] - 6))
    f.arrow([(x["Portal"], step[6]), (x["Estudiante"], step[6])], "7 «pendiente de conciliación» + código de consulta")
    f.box(30, 482, 840, 62,
          "Lectura: el 200 OK del paso 2 es evidencia de una pieza. La matrícula solo existe cuando 3, 4 y 5 concluyen. "
          "Si el paso 6 falla, el sistema debe decir la verdad (7), no fingir éxito ni cobrar dos veces.",
          "coral", 13)
    return f


def se001_decidir() -> Fig:
    f = Fig(900, 470, "Cómo decidir dónde trazar la frontera",
            "Árbol de decisión: según si el equipo controla, puede influir o solo puede observar una "
            "dependencia, la frontera incorpora su modelo, su contrato o su monitoreo.")
    f.box(300, 14, 300, 50, "Quiero explicar un resultado o un fallo concreto", "navy", 14, bold=True)
    f.arrow([(450, 64), (450, 96)])
    f.box(270, 96, 360, 58, "¿La causa está en algo que el equipo controla directamente?", "plain", 14, bold=True)
    f.arrow([(270, 125), (150, 125), (150, 190)], "sí", label_at=(205, 117))
    f.arrow([(630, 125), (750, 125), (750, 190)], "no", label_at=(695, 117))
    f.box(30, 190, 240, 92, "Modela el componente en detalle: responsabilidades, interfaces y señales de falla propias",
          "teal", 13)
    f.box(630, 190, 240, 58, "¿Se puede influir por contrato, regulación o colaboración?", "plain", 13, bold=True)
    f.arrow([(690, 248), (690, 292), (560, 292)], "sí", label_at=(675, 276))
    f.arrow([(810, 248), (810, 292)], "no", label_at=(826, 276), label_anchor="start")
    f.box(330, 262, 230, 100, "Incluye el contrato: qué se espera, cómo se detecta la degradación y a quién se escala",
          "gold", 13)
    f.box(690, 292, 190, 84, "Monitorea y comunica: declara la dependencia y planifica la respuesta local",
          "coral", 13)
    f.box(40, 392, 820, 60,
          "Prueba de suficiencia: cada flecha cruzada debe poder responder qué viaja, cuándo, en qué estado, "
          "quién confirma y qué ocurre si no responde. Si no puede, la frontera aún es una caja negra.",
          "grey", 13)
    return f


def se002_canales() -> Fig:
    f = Fig(900, 420, "Canales de coordinación frente a capacidad lineal",
            "Gráfico de barras: con n personas hay n(n-1)/2 pares posibles de comunicación (1 con 2 personas, "
            "6 con 4, 66 con 12), mientras la capacidad de trabajo separable crece de forma lineal.")
    x0, y0, base, unit = 70, 40, 340, 4.1
    f.line(x0, base, 560, base, "#32505f", width=1.8)
    f.line(x0, y0, x0, base, "#32505f", width=1.8)
    f.text(x0 - 10, y0 + 6, "pares", 13, "end")
    for k, n in enumerate(range(2, 13)):
        pairs = n * (n - 1) // 2
        x = x0 + 14 + k * 43
        h = pairs * unit
        kind = "coral" if n in (4, 12) else "teal"
        f.box(x, base - h, 30, h, "", kind, radius=3)
        f.text(x + 15, base + 20, str(n), 13)
        if n in (2, 4, 8, 12):
            f.text(x + 15, base - h - 8, str(pairs), 13, weight=700)
    f.text(315, base + 44, "personas en el equipo (n)", 13)
    pts = [(x0 + 29 + k * 43, base - n * unit) for k, n in enumerate(range(2, 13))]
    f.arrow(pts, "", dashed=True, color="#a8761a")
    f.arrow([(96, 76), (136, 76)], dashed=True, color="#a8761a")
    f.text(146, 74, "capacidad si el trabajo fuera totalmente separable", 13, "start", 400, "#4a3209")
    f.box(96, 100, 18, 14, "", "coral", radius=3)
    f.text(122, 112, "pares posibles de comunicación", 13, "start")
    f.box(600, 60, 280, 130, "Lectura: añadir personas aumenta la capacidad solo si el trabajo se puede dividir. "
          "Los pares posibles crecen como n(n−1)/2, de modo que cada incorporación suma más canales que la anterior.",
          "teal", 13, align="start")
    f.box(600, 210, 280, 130, "Límite: no todos los pares necesitan hablar. Módulos con contratos claros reducen los "
          "canales efectivos; por eso la conclusión es diseñar límites, no limitar el tamaño del equipo.",
          "gold", 13, align="start")
    return f


def se002_cadena() -> Fig:
    f = Fig(960, 470, "Cadena causal de la ingeniería continua",
            "Cinco etapas: escala, coordinación difícil, prácticas de control, integración frecuente y operación "
            "continua. Para cada una se muestra la señal de control y lo que no garantiza. Un riesgo nuevo "
            "reabre el ciclo.")
    heads = ["Escala y dependencias", "Coordinación y feedback tardío", "Modularidad, revisión y versiones",
             "Integración y entrega frecuentes", "Operación observable"]
    signals = ["Número de interfaces y de personas que deben alinearse", "Defectos hallados lejos del cambio que los causó",
               "Cambios revisables y reversibles por separado", "Fallo cercano al cambio, lote pequeño",
               "Ruta reconstruible de una decisión o un rechazo"]
    limits = ["Más líneas no son más valor", "Reunirse más no es entender más", "No prueba que la decisión fuera correcta",
              "No garantiza adopción ni recuperación", "No explica causalidad por sí sola"]
    f.text(60, 70, "Causa o práctica", 13, "middle", 700)
    f.text(60, 190, "Señal de control", 13, "middle", 700)
    f.text(60, 310, "No garantiza", 13, "middle", 700)
    for i in range(5):
        x = 125 + i * 166
        f.box(x, 40, 152, 60, heads[i], "navy", 13, bold=True)
        f.box(x, 150, 152, 80, signals[i], "teal", 13)
        f.box(x, 270, 152, 80, limits[i], "coral", 13)
        if i < 4:
            f.arrow([(x + 152, 70), (x + 166, 70)])
        f.arrow([(x + 76, 100), (x + 76, 150)], dashed=True)
        f.arrow([(x + 76, 230), (x + 76, 270)], dashed=True)
    f.box(125, 385, 812, 58, "Riesgo nuevo: cambiar más rápido permite dañar más rápido. Reabre el ciclo y exige "
          "gradualidad, telemetría y recuperación; cada respuesta desplaza el cuello de botella, no lo elimina.",
          "gold", 13)
    f.arrow([(937, 414), (950, 414), (950, 70), (937, 70)], dashed=True, color="#a8761a")
    return f


def se002_lotes() -> Fig:
    f = Fig(900, 440, "Un lote grande frente a cambios integrados a diario",
            "Dos carriles de tiempo. En el carril superior diez cambios se integran al final y un fallo tiene "
            "diez sospechosos. En el inferior cada cambio se integra el mismo día y el fallo señala un único cambio.")
    f.text(20, 40, "A · Entrega semestral: un lote", 14, "start", 700)
    f.line(40, 130, 860, 130, "#32505f", width=1.8)
    for k in range(10):
        x = 60 + k * 52
        f.box(x, 74, 44, 40, f"c{k + 1}", "grey", 13)
    f.text(60, 150, "mes 1", 13, "start")
    f.text(780, 150, "mes 6", 13, "end")
    f.box(640, 70, 220, 44, "Integración al final", "navy", 13, bold=True)
    f.box(40, 168, 820, 50, "Falla: 10 cambios sospechosos, contexto original perdido, defectos que se combinan entre sí.",
          "coral", 13)
    f.text(20, 262, "B · Integración diaria: cambios pequeños", 14, "start", 700)
    f.line(40, 352, 860, 352, "#32505f", width=1.8)
    marks = ["ok", "ok", "fail", "ok", "ok", "ok", "ok", "ok", "ok", "ok"]
    for k, mark in enumerate(marks):
        x = 60 + k * 78
        kind = "coral" if mark == "fail" else "teal"
        f.box(x, 296, 44, 40, f"c{k + 1}", kind, 13, bold=mark == "fail")
        f.text(x + 22, 372, "✗ falla" if mark == "fail" else "✓", 13, "middle", 700 if mark == "fail" else 400)
    f.box(40, 392, 820, 36, "Falla en c3: un solo sospechoso, aislado el mismo día y revertible sin tocar el resto.", "teal", 13)
    return f


FIGURES = {
    "se-001-fronteras.svg": se001_fronteras,
    "se-001-solicitud-extremo-a-extremo.svg": se001_solicitud,
    "se-001-decidir-frontera.svg": se001_decidir,
    "se-002-canales-de-coordinacion.svg": se002_canales,
    "se-002-cadena-causal.svg": se002_cadena,
    "se-002-lote-vs-integracion.svg": se002_lotes,
}
