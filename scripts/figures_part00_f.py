"""Figures for SE-011 and SE-012."""
from __future__ import annotations

from figure_kit import Fig


def se011_flujo() -> Fig:
    f = Fig(960, 560, "Flujo vertical de una confirmación repetida, con evidencia por salto",
            "Cadena de nueve saltos desde la persona hasta la señal operativa, con la fuente que muestra cada uno y su "
            "clasificación como observado, inferido o desconocido. Una rama degradada muestra que el comportamiento "
            "tras expirar la reserva es desconocido.")
    hops = [
        ("Persona repite la confirmación", "Escenario del taller", "observado"),
        ("Interfaz o punto de entrada", "Contrato OpenAPI", "observado"),
        ("Contrato: clave idempotente", "Especificación del endpoint", "observado"),
        ("Validación y autorización", "Código del handler", "observado"),
        ("Lógica y cambio de estado", "Código y prueba de repetición", "observado"),
        ("Persistencia: una escritura", "Prueba: dos solicitudes, una escritura", "observado"),
        ("Respuesta y estado consultable", "Contrato; falta ver mensaje real", "inferido"),
        ("Señal de duplicado", "Configuración de métricas", "inferido"),
        ("Recuperación tras expirar la reserva", "No se encontró runbook ni prueba", "desconocido"),
    ]
    sym = {"observado": "✔ observado", "inferido": "~ inferido", "desconocido": "? desconocido"}
    kinds = {"observado": "teal", "inferido": "gold", "desconocido": "coral"}
    for i, (step, source, status) in enumerate(hops):
        y = 14 + i * 58
        f.box(20, y, 330, 46, step, "navy", 13, bold=True)
        f.box(364, y, 340, 46, source, "plain", 13)
        f.box(718, y, 220, 46, sym[status], kinds[status], 13, bold=(status == "desconocido"))
        if i < len(hops) - 1:
            f.arrow([(185, y + 46), (185, y + 58)])
    f.text(534, 546, "Un salto sin evidencia se registra como incógnita; no se rellena por intuición.", 13, "middle")
    return f


def se011_triaje() -> Fig:
    f = Fig(940, 430, "Observado, inferido y desconocido en el hallazgo de la demostración",
            "Tres columnas con el hallazgo de Campus Abierto: lo observado es la prueba de dos solicitudes y una "
            "escritura; lo inferido es la protección dentro de la ventana; lo desconocido es el comportamiento "
            "tras la expiración, que se convierte en un gap.")
    cols = [
        ("Observado", "La prueba ejecuta dos solicitudes iguales y registra una sola escritura. La configuración define la expiración.",
         "Cita ruta y versión; cualquiera puede repetirlo.", "teal"),
        ("Inferido", "La ruta probada evita duplicados dentro de la ventana configurada.",
         "Declara el supuesto: la configuración probada coincide con la desplegada.", "gold"),
        ("Desconocido", "No hay evidencia del comportamiento después de expirar: ¿se concilia el cobro?",
         "Se registra como gap con la evidencia que lo resolvería: runbook o prueba de conciliación.", "coral"),
    ]
    for i, (name, text, action, kind) in enumerate(cols):
        x = 20 + i * 308
        f.box(x, 20, 296, 44, name, "navy", 14, bold=True)
        f.box(x, 72, 296, 116, text, kind, 13)
        f.text(x + 148, 214, "Qué se hace", 13, "middle", 700)
        f.box(x, 224, 296, 90, action, "plain", 13)
    f.box(20, 336, 900, 76, "Hallazgo responsable: «La ruta probada evita duplicado dentro de la ventana configurada. No se encontró evidencia "
          "suficiente sobre el comportamiento tras expirar». No es una vulnerabilidad ni una garantía total.", "grey", 13)
    return f


def se011_gaps() -> Fig:
    f = Fig(900, 460, "Priorizar gaps por consecuencia y costo de obtener evidencia",
            "Cuadrícula de dos por dos: consecuencia alta o baja frente a costo bajo o alto de conseguir la evidencia. "
            "Si repetir una solicitud duplica el cobro, la consecuencia es alta y se investiga primero; el color del "
            "tablero interno es un desconocido irrelevante.")
    f.text(450, 22, "Consecuencia si el desconocido resulta adverso", 14, "middle", 700)
    f.text(285, 52, "Alta", 13, "middle", 700)
    f.text(615, 52, "Baja", 13, "middle", 700)
    f.text(46, 170, "Costo bajo", 13, "middle", 700)
    f.text(46, 330, "Costo alto", 13, "middle", 700)
    f.box(110, 66, 350, 150, "Investiga primero: «¿repetir la solicitud duplica el cobro?». Alta consecuencia y una prueba basta.", "coral", 13, bold=True)
    f.box(470, 66, 350, 150, "Resuelve si es barato: confirma la versión de una dependencia no crítica.", "teal", 13)
    f.box(110, 226, 350, 150, "Planifica: evaluar el comportamiento ante una caída regional exige un ensayo costoso, pero la consecuencia lo justifica.", "gold", 13)
    f.box(470, 226, 820 - 470 + 0, 150, "No persigas: «no sé el color del tablero interno». Es desconocido, no relevante para ninguna decisión.", "grey", 13)
    f.box(110, 392, 710, 52, "Un gap es una pregunta necesaria que la evidencia disponible no responde; no cualquier ausencia de documentación.", "plain", 13)
    return f


def se012_competencias() -> Fig:
    f = Fig(960, 500, "Mapa de competencias con cuatro estados de evidencia",
            "Tabla de siete capacidades de la Parte 00 por cuatro estados: aún no tengo evidencia, puedo reconocer y "
            "explicar, puedo ejecutar con guía y puedo transferir y defender. Un perfil de ejemplo marca con un punto "
            "el estado de cada capacidad; los estados no son rangos personales.")
    states = ["Aún no tengo evidencia", "Puedo reconocer y explicar", "Puedo ejecutar con guía", "Puedo transferir y defender"]
    caps = [
        ("Delimitar un sistema y su responsabilidad", 3),
        ("Sostener decisiones en el ciclo de vida", 2),
        ("Deliberar y coordinar con otras personas", 2),
        ("Razonar bajo incertidumbre", 3),
        ("Comparar consecuencias y riesgos", 2),
        ("Fundamentar afirmaciones con fuentes", 1),
        ("Integrar las lentes en un producto real", 0),
    ]
    f.box(10, 12, 300, 54, "Capacidad (evidencia previa)", "navy", 13, bold=True)
    for j, s in enumerate(states):
        f.box(316 + j * 158, 12, 152, 54, s, "navy", 12, bold=True)
    for i, (cap, state) in enumerate(caps):
        y = 74 + i * 52
        f.box(10, y, 300, 46, cap, "grey", 13)
        for j in range(4):
            f.box(316 + j * 158, y, 152, 46, "", "teal" if j == state else "plain")
            if j == state:
                f.dot(316 + j * 158 + 76, y + 23, "●", "navy")
    f.text(480, 462, "Perfil ficticio de ejemplo orientado a backend: no es una evaluación ni un ranking.", 13, "middle")
    f.text(480, 482, "Se avanza con evidencia revisable, no con autoestima ni años de experiencia. Cada capacidad puede estar en un estado distinto.", 13, "middle")
    return f


def se012_experimento() -> Fig:
    f = Fig(960, 440, "Ciclo adaptativo del contrato de aprendizaje",
            "Cinco pasos: evidencia actual, dirección, brecha, experimento acotado y revisión. La revisión produce una de "
            "cuatro decisiones (avanzar, repetir, dividir o cambiar de estrategia) y reabre la brecha.")
    f.box(20, 40, 190, 70, "Evidencia actual: qué puedes demostrar hoy", "teal", 13)
    f.box(20, 140, 190, 70, "Dirección: problemas y responsabilidades que buscas", "teal", 13)
    f.box(270, 90, 190, 70, "Brecha: capacidad que falta, no solo un tema", "gold", 13, bold=True)
    f.arrow([(210, 75), (270, 115)])
    f.arrow([(210, 175), (270, 135)])
    f.box(520, 90, 200, 70, "Experimento: máximo dos semanas, con criterio y resultado que pueda refutarlo", "navy", 13, bold=True)
    f.arrow([(460, 125), (520, 125)])
    f.box(780, 90, 160, 70, "Artefacto + revisión por otra persona", "teal", 13)
    f.arrow([(720, 125), (780, 125)])
    f.box(250, 250, 460, 56, "Decisión de revisión (con fecha y disparadores)", "grey", 14, bold=True)
    f.arrow([(860, 160), (860, 220), (710, 270)])
    outcomes = ["Avanzar", "Repetir", "Dividir", "Cambiar estrategia"]
    for i, o in enumerate(outcomes):
        x = 100 + i * 200
        f.box(x, 340, 180, 46, o, "plain", 13, bold=True)
        f.arrow([(480, 306), (x + 90, 340)], dashed=True)
    f.arrow([(100, 363), (50, 363), (50, 210)], "reabre la brecha", dashed=True, color="#a8761a", label_at=(60, 285), label_anchor="start")
    f.text(480, 420, "Si todo experimento termina «completo» por consumir contenido, no es un experimento: debe existir un resultado que lo refute.", 13, "middle")
    return f


def se012_capacidad() -> Fig:
    f = Fig(940, 460, "Trabajo en curso limitado frente a diez objetivos simultáneos",
            "Dos carriles de seis semanas con datos ilustrativos. En el carril A, diez objetivos empiezan a la vez, "
            "superan la capacidad declarada de 8 horas semanales y no producen feedback. En el carril B, tres "
            "experimentos encadenados producen una revisión cada dos semanas.")
    f.text(20, 34, "A · Diez objetivos a la vez", 14, "start", 700)
    f.line(40, 130, 900, 130, "#32505f", width=1.8)
    for k in range(10):
        f.box(60 + k * 84, 56, 76, 44, f"obj. {k + 1}", "grey", 12)
    for w in range(7):
        f.text(60 + w * 130, 150, f"sem. {w}", 13, "start")
    f.box(40, 164, 860, 78, "Demanda ilustrativa: 10 objetivos × 2 h = 20 h/semana. Capacidad declarada: 8 h/semana. "
          "Resultado: ningún artefacto revisable, sin feedback y con riesgo de sobreesfuerzo.", "coral", 13)
    f.text(20, 280, "B · Tres experimentos encadenados", 14, "start", 700)
    f.line(40, 350, 900, 350, "#32505f", width=1.8)
    for k, label in enumerate(["Exp. 1 (sem. 1-2)", "Exp. 2 (sem. 3-4)", "Exp. 3 (sem. 5-6)"]):
        x = 60 + k * 280
        f.box(x, 296, 250, 44, label, "teal", 13)
        f.dot(x + 250, 350, str(k + 1))
        f.text(x + 250, 384, "revisión", 13, "middle", 700)
    f.box(40, 402, 860, 44, "Cabe en 8 h/semana, cada paso produce un artefacto y una decisión, y el siguiente experimento usa lo aprendido.", "teal", 13)
    return f


FIGURES = {
    "se-011-flujo-vertical.svg": se011_flujo,
    "se-011-observado-inferido-desconocido.svg": se011_triaje,
    "se-011-priorizar-gaps.svg": se011_gaps,
    "se-012-mapa-de-competencias.svg": se012_competencias,
    "se-012-ciclo-del-contrato.svg": se012_experimento,
    "se-012-capacidad-y-wip.svg": se012_capacidad,
}
