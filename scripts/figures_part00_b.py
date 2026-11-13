"""Figures for SE-003 and SE-004."""
from __future__ import annotations

from figure_kit import Fig


def se003_ciclo() -> Fig:
    f = Fig(960, 500, "Ciclo de vida con bucles de retroalimentación",
            "Seis momentos en fila, de concepción a retiro, con tres flechas de retorno: operación informa nuevos "
            "requisitos, mantenimiento reabre decisiones de diseño y el retiro devuelve lecciones al inicio.")
    names = ["Concepción", "Realización", "Transición", "Operación", "Mantenimiento", "Retiro"]
    questions = ["¿Debemos construir esto?", "¿Es reproducible y recuperable?", "¿Se puede revertir?",
                 "¿Qué señal detecta el fallo?", "¿Qué compatibilidad conservo?", "¿Qué datos y consumidores quedan?"]
    for i, name in enumerate(names):
        x = 30 + i * 150
        f.box(x, 150, 135, 70, name, "navy", 14, bold=True)
        f.box(x, 380, 135, 66, questions[i], "teal", 13)
        f.arrow([(x + 67, 220), (x + 67, 380)], dashed=True)
        if i < 5:
            f.arrow([(x + 135, 185), (x + 150, 185)])
    cx = [30 + i * 150 + 67 for i in range(6)]
    f.arrow([(cx[3], 150), (cx[3], 108), (cx[0], 108), (cx[0], 150)], "señales de operación → nuevos requisitos",
            color="#c0432f", label_at=((cx[0] + cx[3]) / 2, 100))
    f.arrow([(cx[4], 150), (cx[4], 62), (cx[1], 62), (cx[1], 150)], "cambios y deuda → decisiones de diseño y pruebas",
            color="#c0432f", label_at=((cx[1] + cx[4]) / 2, 54))
    f.arrow([(cx[5], 150), (cx[5], 24), (cx[0], 24), (cx[0], 150)], "retiro → criterio de no construir y exportabilidad",
            color="#c0432f", label_at=((cx[0] + cx[5]) / 2, 16))
    f.text(480, 470, "Las flechas rojas continuas son bucles: el ciclo no es una cascada de departamentos.", 13)
    f.text(480, 490, "Las flechas punteadas hacia abajo indican la pregunta de control de cada momento.", 13)
    return f


def se003_terminado() -> Fig:
    f = Fig(940, 480, "Cinco significados de terminado",
            "Escalera de cinco peldaños: fusionado, desplegado, liberado, adoptado y resultado logrado. Para cada "
            "uno se indica la evidencia que lo demuestra y lo que queda oculto si se declara terminado ahí.")
    steps = [
        ("Fusionado", "PR aprobado y pruebas verdes", "Nadie comprueba que funciona fuera de la máquina del equipo"),
        ("Desplegado", "Versión corriendo en el entorno destino", "Corre, pero tras una bandera apagada o sin tráfico"),
        ("Liberado", "Disponible para la audiencia prevista", "Disponible sin soporte, documentación ni señales"),
        ("Adoptado", "Uso real medido en las personas objetivo", "Se usa, pero no se logra la tarea o se abandona"),
        ("Resultado logrado", "El efecto declarado se mide y se sostiene", "Efecto no medido o con daño en otro grupo"),
    ]
    f.text(40, 262, "Evidencia", 13, "start", 700)
    f.text(40, 372, "Queda oculto si", 13, "start", 700)
    for i, (name, evidence, hidden) in enumerate(steps):
        x = 40 + i * 176
        top = 190 - i * 38
        f.box(x, top, 160, 50 + i * 38, name, "navy", 14, bold=True)
        f.box(x, 270, 160, 80, evidence, "teal", 13)
        f.box(x, 380, 160, 84, hidden, "coral", 13)
    f.text(480, 30, "Cada peldaño exige una evidencia distinta; decir «done» sin elegir uno oculta el trabajo restante.",
           14, "middle", 700)
    return f


def se003_autoridad() -> Fig:
    f = Fig(940, 480, "Matriz de decisión, ejecución, custodia y parada en el cambio de proveedor de identidad",
            "Tabla de seis roles por cuatro dimensiones (decide, ejecuta, custodia, puede detener). Cada dimensión "
            "tiene un propietario explícito y la dimensión parar la migración está asignada a producto y operación.")
    cols = ["Decide", "Ejecuta", "Custodia", "Puede detener"]
    rows = [
        ("Producto", ["● qué experiencia no puede perderse", "—", "—", "● si cae la tasa de acceso"]),
        ("Identidad", ["—", "● adapta contrato y pruebas", "● credenciales y secretos", "—"]),
        ("Datos", ["—", "● reconcilia identificadores", "● relaciones y registros", "—"]),
        ("Soporte", ["—", "● comunica y recupera cuentas", "—", "—"]),
        ("Seguridad", ["● acepta o veta el riesgo de secretos", "● revisa y revoca", "—", "● si hay secretos expuestos"]),
        ("Operación", ["—", "● observa y ejecuta reversión", "—", "● supera el umbral de errores"]),
    ]
    f.box(20, 14, 140, 40, "Rol", "navy", 14, bold=True)
    for j, c in enumerate(cols):
        f.box(170 + j * 188, 14, 180, 40, c, "navy", 14, bold=True)
    for i, (role, cells) in enumerate(rows):
        y = 62 + i * 62
        f.box(20, y, 140, 54, role, "grey", 14, bold=True)
        for j, cell in enumerate(cells):
            kind = "plain" if cell == "—" else ("coral" if j == 3 else "teal")
            f.box(170 + j * 188, y, 180, 54, cell, kind, 13)
    f.text(470, 446, "● = propietario de esa dimensión · — = sin papel.", 13, "middle", 400)
    f.text(470, 466, "Una columna sin ● o un rol con ● pero sin acceso real es una ficción.", 13, "middle", 400)
    return f


def se004_promedio() -> Fig:
    f = Fig(900, 440, "El promedio global oculta a un grupo que empeora",
            "Gráfico de barras con datos sintéticos: el tiempo medio de espera baja de 5 a 3,3 días, pero el grupo "
            "que estudia y trabaja pasa de 5 a 9 días mientras los otros dos grupos mejoran.")
    base, unit, x0 = 340, 26, 80
    f.line(x0, base, 600, base, "#32505f", width=1.8)
    f.line(x0, 50, x0, base, "#32505f", width=1.8)
    f.text(x0 - 8, 54, "días", 13, "end")
    groups = [("Tiempo completo\n(60 %)", 5, 2), ("Medio tiempo\n(25 %)", 5, 3), ("Estudian y trabajan\n(15 %)", 5, 9)]
    for k, (name, before, after) in enumerate(groups):
        gx = x0 + 30 + k * 170
        f.box(gx, base - before * unit, 52, before * unit, "", "grey", radius=3)
        kind = "coral" if after > before else "teal"
        f.box(gx + 58, base - after * unit, 52, after * unit, "", kind, radius=3)
        f.text(gx + 26, base - before * unit - 8, str(before), 13, weight=700)
        f.text(gx + 84, base - after * unit - 8, str(after), 13, weight=700)
        f.text(gx + 55, base + 22, name, 13)
    f.box(630, 60, 250, 70, "Promedio global: de 5 a 3,3 días (0,6·2 + 0,25·3 + 0,15·9)", "teal", 13)
    f.box(630, 146, 250, 96, "Segmento afectado: de 5 a 9 días. Sin apelación ni señal por grupo, nadie lo ve: el promedio sí «mejoró».",
          "coral", 13)
    f.box(630, 258, 250, 78, "Barra gris = antes; barra de color = después (azul verdoso mejora, rojo empeora; el número lo confirma).",
          "grey", 13)
    f.text(450, 410, "Datos sintéticos de ilustración, no medidos. La regla: decide con la distribución, no solo con el promedio.",
           13, "middle", 400, "#5c1f14")
    return f


def se004_deliberacion() -> Fig:
    f = Fig(940, 440, "Secuencia de deliberación y prueba de que cambia el diseño",
            "Cinco pasos en secuencia, desde describir la decisión hasta fijar autoridad de parada, seguidos de "
            "una compuerta: si ninguna alternativa cambió población, datos, automatización, umbral, supervisión, "
            "comunicación o apelación, el análisis fue decoración.")
    steps = [
        ("1 Describir", "Separa observación, inferencia e incertidumbre"),
        ("2 Afectados", "Quién gana, quién carga, quién queda fuera"),
        ("3 Alternativas", "Incluye la opción de no proceder"),
        ("4 Comparar", "Prevención, detección, apelación, reparación y costo desplazado"),
        ("5 Autoridad", "Quién para, con qué señal y cuándo se revisa"),
    ]
    for i, (name, note) in enumerate(steps):
        x = 24 + i * 182
        f.box(x, 40, 170, 44, name, "navy", 14, bold=True)
        f.box(x, 96, 170, 90, note, "teal", 13)
        if i < 4:
            f.arrow([(x + 170, 62), (x + 182, 62)])
    f.box(150, 230, 640, 72, "Compuerta: ¿cambió población, datos, automatización, umbral, supervisión, comunicación o derecho de apelación?",
          "gold", 14, bold=True)
    f.arrow([(470, 186), (470, 230)])
    f.arrow([(150, 266), (60, 266), (60, 340)], "no", label_at=(100, 258))
    f.arrow([(790, 266), (880, 266), (880, 340)], "sí", label_at=(840, 258))
    f.box(10, 340, 200, 80, "Era decoración: lista de principios sin efecto. Vuelve al paso 3.", "coral", 13)
    f.box(680, 340, 250, 80, "Decisión gobernada: con límites, voz, reparación y condición de parada.", "teal", 13)
    f.box(260, 340, 380, 80, "Después: monitorear por grupo, revisar casos y mantener apelación accesible. "
          "El caso nunca queda «resuelto éticamente».", "grey", 13)
    return f


def se004_reparacion() -> Fig:
    f = Fig(940, 400, "Retirar una función no repara el daño ocurrido",
            "Línea de tiempo: el daño ocurre en t0. Retirar la función evita daños futuros. La reparación actúa "
            "sobre el caso pasado y el aprendizaje rediseña el sistema; son tres acciones distintas.")
    f.line(40, 150, 900, 150, "#32505f", width=2)
    f.dot(120, 150, "t0", "coral")
    f.text(120, 186, "Ocurre el daño", 13, "middle", 700)
    f.text(120, 204, "a una persona real", 13)
    f.box(210, 40, 220, 66, "Detectar: señal por grupo, revisión de casos, canal de queja accesible", "teal", 13)
    f.arrow([(320, 106), (320, 140)], dashed=True)
    f.box(450, 40, 230, 66, "Retirar o suspender la función: evita casos futuros", "gold", 13)
    f.box(700, 40, 210, 66, "No repara el caso pasado", "coral", 13, bold=True)
    f.arrow([(680, 73), (700, 73)])
    f.box(210, 228, 330, 100, "Reparar: restaurar la oportunidad, corregir datos, explicar la decisión, compensar o permitir revisión humana. "
          "Accesible para quien sufrió el efecto.", "teal", 13)
    f.box(570, 228, 340, 100, "Aprender: rediseñar población, datos, umbral o supervisión y registrar el cambio para que no se repita.",
          "grey", 13)
    f.arrow([(540, 278), (570, 278)])
    f.arrow([(375, 196), (375, 228)], dashed=True)
    f.text(470, 372, "Tres acciones, tres responsables posibles: suspender protege el futuro; reparar atiende el pasado; aprender cambia el sistema.",
           13, "middle", 400)
    return f


FIGURES = {
    "se-003-ciclo-de-vida-con-bucles.svg": se003_ciclo,
    "se-003-significados-de-terminado.svg": se003_terminado,
    "se-003-matriz-de-autoridad.svg": se003_autoridad,
    "se-004-promedio-vs-distribucion.svg": se004_promedio,
    "se-004-deliberacion.svg": se004_deliberacion,
    "se-004-reparacion.svg": se004_reparacion,
}
