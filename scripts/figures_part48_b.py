"""Figures for SE-583 to SE-588 (harness and agentic engineering: gates, real Git merges, seeded simulations, injected faults and a governed mini-harness; Windows 11, CPython 3.12.9, Git 2.55; no language model was invoked)."""
from __future__ import annotations

from figure_flow_rows import chain_rows
from figure_kit import AXIS, Fig, _kit_finish, _kit_start, grouped_bars, line_chart, stacked_bars

from figures_part45_a import bars, flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9; ninguna cifra viene de un modelo de lenguaje."
SIM = "Simulación con semilla fija (parámetros del autor) ejecutada en Windows 11 con CPython 3.12.9; no mide ningún modelo real."


# ---------------------------------------------------------------- SE-583
def se499_cambios() -> Fig:
    return stacked_bars(
        "Qué atrapan las compuertas de un menú completo frente a las pruebas solas sobre 11 cambios defectuosos",
        "Barras apiladas horizontales con los 11 cambios defectuosos: el menú completo de compuertas atrapa 9 y deja pasar 2, un error que ninguna prueba ejerce y una prueba que replica el error; las pruebas solas atrapan 2, el error de sintaxis y el error de lógica que una prueba ve, y dejan pasar 9.",
        ["Menú completo de compuertas", "Solo las pruebas"],
        [("Atrapados", [9, 2], "teal"), ("Se escapan", [2, 9], "coral")],
        unit="Cambios defectuosos de 11", horizontal=True, label_w=200,
        note="Las compuertas especializadas atrapan la importación sin usar, el secreto literal, la prueba debilitada y la prueba omitida; el error de sintaxis lo atrapan tres compuertas. Los 2 restantes (un error que ninguna prueba ejerce y una prueba que replica el error) no los atrapa ninguna compuerta: son el límite del gate.",
        note_kind="coral", foot=EJEC)


def se499_por_compuerta() -> Fig:
    return bars('Defectos atrapados por cada compuerta del menú único (de 11)',
                'Gráfico de barras con los defectos atrapados de once por compuerta: sintaxis 1, estilo 5, secretos 1, pruebas 2, no debilitar pruebas 2; el menú completo atrapa 9.',
                [('Sintaxis', 1, 'plain', '1'), ('Estilo', 5, 'teal', '5'), ('Secretos', 1, 'plain', '1'), ('Pruebas', 2, 'gold', '2'), ('No debilitar pruebas', 2, 'gold', '2'), ('Menú completo', 9, 'navy', '9')],
                scale=40, note='Las compuertas baratas atrapan más defectos que la costosa: las pruebas tardan cientos de milisegundos; la sintaxis, el estilo y los secretos, unos pocos. Orden: lo barato primero.',
                note_kind='gold', foot=EJEC, label_w=330)


def se499_menu() -> Fig:
    return flow('Un solo punto de entrada que ejecuta las compuertas de la más barata a la más cara',
                'Diagrama con dos filas: el agente y la persona invocan el mismo comando; el menú ejecuta sintaxis, estilo, secretos, pruebas y la comprobación de que no se debilitaron pruebas; al primer fallo se detiene e imprime el nombre de la compuerta y el motivo; el código de salida decide.',
                [[('Mismo comando para agente y persona', 'gold'), ('Sintaxis, estilo y secretos', 'teal'), ('Pruebas y no debilitar pruebas', 'teal')],
                 [('Primer fallo detiene y nombra la compuerta', 'coral'), ('Código de salida decide', 'navy'), ('Misma compuerta en integración continua', 'plain')]],
                note='Un menú único elimina que cada quien corra una parte. La compuerta que corre en la integración continua debe ser exactamente la que corre el agente antes de entregar.',
                note_kind='gold', foot=EJEC, box_h=76)


# ---------------------------------------------------------------- SE-584
def se500_fusiones() -> Fig:
    rows = [
        [("Archivos distintos", "plain"), ("Fusión limpia", "teal"), ("Las pruebas pasan", "teal")],
        [("Mismo archivo, zonas lejanas", "plain"), ("Fusión limpia", "teal"), ("Las pruebas pasan", "teal")],
        [("Mismas líneas", "plain"), ("Conflicto de texto", "gold"), ("No aplica", "grey")],
        [("Renombrar una función en una rama y usarla desde otra", "plain"), ("Fusión limpia", "teal"), ("Las pruebas FALLAN", "coral")],
    ]
    return chain_rows(
        "Dos agentes en ramas de Git reales: lo que dice la fusión y lo que dicen las pruebas",
        "Diagrama de flujo de cuatro escenarios de dos ramas de Git creadas en directorios temporales: archivos distintos y zonas lejanas del mismo archivo se fusionan limpios y las pruebas pasan; editar las mismas líneas produce un conflicto; renombrar una función en una rama y usarla desde otra se fusiona limpio y las pruebas fallan.",
        ["Escenario", "Fusión de Git", "Pruebas tras fusionar"], rows, [340, 220, 250],
        note="Que Git fusione sin conflicto no significa que el resultado funcione. El conflicto semántico solo lo ve una verificación posterior a la fusión, y el conflicto textual es el caso fácil.",
        note_kind="coral", foot=EJEC)


def se500_solapamiento() -> Fig:
    return bars('Probabilidad de que dos agentes toquen algún archivo común, con 40 archivos y 3 por tarea',
                'Gráfico de barras con la probabilidad de algún archivo compartido: 2 agentes 21,3 por ciento, 3 agentes 53,0, 4 agentes 79,9, 6 agentes 98,4 y 8 agentes 100.',
                [('2 agentes', 21.3, 'teal', '21,3 %'), ('3 agentes', 53.0, 'gold', '53,0 %'), ('4 agentes', 79.9, 'coral', '79,9 %'), ('6 agentes', 98.4, 'coral', '98,4 %'), ('8 agentes', 100.0, 'coral', '100 %')],
                scale=7.5, note='Los canales entre pares crecen como n(n-1)/2: 1, 3, 6, 15 y 28. Con un coordinador crecen como n. Más agentes en el mismo árbol compran paralelismo y pagan colisión.',
                note_kind='gold', foot=SIM, label_w=250)


def se500_roles() -> Fig:
    return flow('Coordinación mínima: propiedad de archivos, aislamiento por rama y un único integrador',
                'Diagrama con dos filas: un coordinador divide la tarea por propiedad de archivos; cada agente trabaja en su propia rama con su árbol de trabajo; un integrador fusiona de una en una y ejecuta la verificación completa después de cada fusión.',
                [[('Coordinador divide por propiedad de archivos', 'gold'), ('Cada agente en su rama y su árbol', 'teal'), ('Entrega con rastro y pruebas', 'plain')],
                 [('Un integrador fusiona de una en una', 'navy'), ('Verificación completa tras cada fusión', 'teal'), ('Conflicto: vuelve al coordinador', 'coral')]],
                note='La separación por rama evita pisarse; la verificación posterior a la fusión detecta lo que Git no ve. Falta decidir quién resuelve un conflicto, y esa decisión es de una persona o de un solo agente designado.',
                note_kind='gold', foot=EJEC, box_h=76)


# ---------------------------------------------------------------- SE-585
def se501_trazas() -> Fig:
    return grouped_bars(
        "Métricas calculadas desde las trazas de cuatro configuraciones del harness mínimo",
        "Barras agrupadas con los pasos totales y las denegaciones de las trazas de cuatro configuraciones sobre seis tareas: el harness completo usa 30 pasos y ninguna denegación y resuelve 6 de 6; sin contexto usa 72 pasos y resuelve 0; con la escritura denegada usa 36 pasos con 12 denegaciones y resuelve 0; sin criterio de parada usa 72 pasos y resuelve 6 de 6 con 12,0 pasos por tarea.",
        ["Completo (6 de 6 resueltas, 5,0 pasos por tarea)", "Sin contexto (0 de 6)", "Escritura denegada (0 de 6)", "Sin criterio de parada (6 de 6, 12,0 pasos por tarea)"],
        [("Pasos totales", [30, 72, 36, 72], "navy"), ("Denegaciones", [0, 0, 12, 0], "coral")],
        unit="Pasos o denegaciones", horizontal=True, label_w=290, ticks=[0, 20, 40, 60, 80],
        note="Las dos configuraciones que gastan 72 pasos fallan por razones opuestas: una no resuelve nada y la otra lo resuelve todo sin parar. Solo la combinación de pasos, denegaciones y resultado las distingue.",
        note_kind="gold", foot=EJEC)


def se501_potencia() -> Fig:
    return bars('Probabilidad de detectar una mejora real de 6 puntos según el número de tareas',
                'Gráfico de barras con la probabilidad de detectar con una prueba pareada una mejora real de 6 puntos del harness: con 50 tareas 9,7 por ciento, con 200 tareas 24,5 y con 800 tareas 75,9.',
                [('50 tareas', 9.7, 'coral', '9,7 %'), ('200 tareas', 24.5, 'gold', '24,5 %'), ('800 tareas', 75.9, 'teal', '75,9 %')],
                scale=11, note='Con 50 tareas una mejora real de 6 puntos se detecta una vez de diez. Una conclusión «sin diferencia» con pocas tareas no dice que no la haya.',
                note_kind='gold', foot=SIM, label_w=250)


def se501_falsos_positivos() -> Fig:
    tasks = [50, 200, 800]
    return line_chart(
        "Declarar mejor a un harness idéntico: la regla «tiene más aciertos» frente a una prueba pareada",
        "Líneas con la proporción de veces que se declara mejor a un harness idéntico a la línea base: con 50 tareas la regla de más aciertos lo declara mejor el 45,7 por ciento y la prueba pareada el 2,1; con 200 tareas 48,7 y 3,0; con 800 tareas 47,1 y 3,0.",
        [("Regla «tiene más aciertos»", list(zip(tasks, [45.7, 48.7, 47.1])), "coral"), ("Prueba pareada", list(zip(tasks, [2.1, 3.0, 3.0])), "teal")],
        x_label="Tareas de la comparación", y_label="Se declara mejor (%)", log_x=True, x_ticks=[(50, "50"), (200, "200"), (800, "800")], y_ticks=[0, 10, 20, 30, 40, 50, 60],
        point_labels="all", decimals=1,
        note="Comparar contra un harness idéntico muestra el ruido: la regla ingenua da por mejor la mitad de las veces algo que no cambió. La prueba pareada mantiene el error cerca del 3 %, a costa de la potencia.",
        note_kind="coral", foot=SIM)


# ---------------------------------------------------------------- SE-586
def se502_clasificacion() -> Fig:
    f, y = _kit_start("Clasificación de riesgo por reglas sobre rutas, tamaño y dependencias: ocho de doce cambios",
                      "Diagrama con ocho de doce cambios agrupados por el nivel de riesgo que les asignan reglas deterministas: en el riesgo bajo la documentación y un cambio de código con su prueba y 40 líneas; en el medio el código sin prueba, el cambio de 400 líneas y el archivo de dependencias; en el alto el workflow de integración continua, la autenticación y la migración.",
                      940, None)
    cols = [("Riesgo bajo", "teal", ["docs/guia.md", "src/a.py con su prueba (40 líneas)"]),
            ("Riesgo medio", "gold", ["src/a.py sin prueba", "src/a.py con prueba, 400 líneas", "requirements.txt (dependencias)"]),
            ("Riesgo alto", "coral", [".github/workflows/ci.yml", "auth/login.py con su prueba", "migrations/0004.sql"])]
    w, gap, top = 290, 20, y + 4
    for i, (head, kind, items) in enumerate(cols):
        x = 14 + i * (w + gap)
        f.group(x, top, w, 220, head, kind)
        for j, text in enumerate(items):
            f.box(x + 12, top + 38 + j * 58, w - 24, 48, text, kind, 13)
    f.text(14, top + 246, "Las reglas se leen de arriba abajo por ruta, tamaño y dependencias; el primer nivel que coincide fija el riesgo.", 13, "start", 400, AXIS)
    return _kit_finish(f, top + 258,
                       "Una regla de rutas es barata, auditable y fácil de eludir: un cambio peligroso en una carpeta que no aparece en la lista es de riesgo bajo. Se complementa con revisión humana de las reglas.",
                       "gold", EJEC)


def se502_escapes() -> Fig:
    return bars('Defectos que escapan por cada 1000 cambios según el modo de trabajo (modelo del autor)',
                'Gráfico de barras con los defectos que escapan por cada mil cambios: sin controles 89, revisión humana de todo 38 con 271 horas, y compuertas más revisión por riesgo 22 con 201 horas.',
                [('Sin controles', 89, 'coral', '89 (0 h)'), ('Revisión humana de todo', 38, 'gold', '38 (271 h)'), ('Compuertas + revisión por riesgo', 22, 'teal', '22 (201 h)')],
                scale=4.2, note='Modelo paramétrico: tres niveles de riesgo con probabilidades de defecto del autor y compuertas que atrapan 60 % de los defectos. Sirve para razonar la forma del compromiso; ninguna cifra es una tasa real.',
                note_kind='coral', foot=SIM, label_w=330)


def se502_ciclo() -> Fig:
    return flow('Un ciclo de desarrollo asistido con compuertas humanas donde el riesgo lo pide',
                'Diagrama con dos filas: la intención y el alcance se acuerdan antes; el agente construye con compuertas automáticas; el cambio se clasifica por riesgo; el riesgo bajo pasa con las compuertas, el medio y el alto exigen revisión humana; todo queda con rastro y se mide el resultado en operación.',
                [[('Intención y alcance acordados', 'gold'), ('Construcción con compuertas automáticas', 'teal'), ('Clasificar por riesgo', 'navy')],
                 [('Bajo: pasa con las compuertas', 'plain'), ('Medio y alto: revisión humana', 'coral'), ('Rastro y medición en operación', 'teal')]],
                note='AI-DLC organiza el trabajo en Inception, Construction y Operations con puntos de aprobación humana. Aquí se muestra solo la idea común: la profundidad del control depende del riesgo.',
                note_kind='gold', foot=EJEC, box_h=76)


# ---------------------------------------------------------------- SE-587
def se503_fallos() -> Fig:
    return grouped_bars(
        "Seis fallos inyectados en el harness y cuántas veces los acierta el diagnóstico desde la traza",
        "Barras horizontales con los casos que el diagnóstico acierta, de 30, por fallo inyectado: con la traza mínima acierta los fallos de contexto, parada, verificación, permiso y tope y confunde siempre la herramienta ausente con la falta de contexto, 24 de 30; con la traza enriquecida, que incluye las herramientas ofrecidas, el contexto visible y la observación, acierta los 30.",
        ["F1 sin contexto entre pasos (6 casos)", "F2 herramienta de escritura ausente (6)", "F3 la parada no se respeta (6)", "F4 sin instrucción de verificar (3)", "F5 escritura denegada por permiso (6)", "F6 tope de pasos demasiado bajo (3)"],
        [("Traza mínima", [6, 0, 6, 3, 6, 3], "coral"), ("Traza enriquecida", [6, 6, 6, 3, 6, 3], "teal")],
        unit="Casos acertados", horizontal=True, label_w=290, ticks=[0, 2, 4, 6],
        note="Con la traza mínima el diagnóstico acierta 24 de 30; con la enriquecida, 30 de 30. La diferencia es un campo, las herramientas ofrecidas, que decide entre dos fallos con síntomas idénticos.",
        note_kind="gold", foot=EJEC)


def se503_aciertos() -> Fig:
    return bars('Diagnósticos correctos de 30 con cada versión de la traza',
                'Gráfico de barras con los diagnósticos correctos de treinta casos: la traza mínima acierta 24 y la traza enriquecida con herramientas ofrecidas, contexto visible y observación acierta 30.',
                [('Traza mínima', 24, 'gold', '24 de 30'), ('Traza enriquecida', 30, 'teal', '30 de 30')],
                scale=28, note='Los 6 casos que falla la traza mínima son un mismo fallo, no seis: se corrige con un solo campo. Un diagnóstico que acierta siempre en un conjunto inyectado no garantiza lo mismo ante fallos que no se inyectaron.',
                note_kind='coral', foot=EJEC, label_w=330)


def se503_procedimiento() -> Fig:
    return flow('Procedimiento de diagnóstico: de la traza al componente y de ahí a una prueba de regresión',
                'Diagrama con dos filas: reproducir la falla con la misma tarea y la misma configuración; leer la traza buscando repeticiones, denegaciones y herramientas ofrecidas; formular una hipótesis sobre un componente del harness; cambiar solo ese componente; volver a ejecutar y añadir el caso al conjunto de regresión.',
                [[('Reproducir con la misma configuración', 'plain'), ('Leer la traza: repeticiones y denegaciones', 'teal'), ('Hipótesis sobre un solo componente', 'gold')],
                 [('Cambiar solo ese componente', 'navy'), ('Ejecutar de nuevo y comparar', 'teal'), ('Añadir el caso a la regresión', 'plain')]],
                note='Cambiar dos componentes a la vez impide saber cuál arregló la falla. El diagnóstico es una hipótesis refutable, no una intuición.',
                note_kind='gold', foot=EJEC, box_h=76)


# ---------------------------------------------------------------- SE-588
def se504_escenarios() -> Fig:
    rows = [
        [("Seis tareas normales", "plain"), ("6 de 6; 5,0 pasos", "teal"), ("6 de 6; 5,0 pasos", "teal")],
        [("A1 debilitar la prueba", "plain"), ("Prueba alterada; terminada en falso", "coral"), ("Bloqueado; para por falta de progreso", "teal")],
        [("A2 leer fuera de la raíz", "plain"), ("Lectura fuera de la raíz", "coral"), ("Bloqueado; para por falta de progreso", "teal")],
        [("A3 repetir el mismo intento", "plain"), ("12 pasos hasta el tope", "coral"), ("Para en 3 pasos", "teal")],
        [("A4 terminar sin verificar", "plain"), ("Terminada en falso", "coral"), ("Rechazada; para por falta de progreso", "teal")],
    ]
    return chain_rows(
        "Harness sin controles frente a harness gobernado: tareas normales y cuatro escenarios adversos",
        "Diagrama de flujo de cinco escenarios: en las seis tareas normales ambos harness resuelven 6 de 6 con 5,0 pasos; sin controles, debilitar la prueba la altera y deja la tarea terminada en falso, leer fuera de la raíz tiene éxito, repetir el mismo intento gasta 12 pasos y terminar sin verificar queda terminada en falso; gobernado bloquea la prueba alterada y la lectura, para a los 3 pasos el intento repetido y rechaza la terminación sin verificar.",
        ["Escenario", "Sin controles", "Gobernado"], rows, [270, 290, 290], gap=26,
        note="Los controles no cuestan nada en las tareas normales y cambian el resultado en las adversas. Los cuatro escenarios son del autor: demuestran que cada control hace su trabajo, no que cubran todos los casos.",
        note_kind="gold", foot=EJEC)


def se504_arquitectura() -> Fig:
    return flow('Arquitectura del harness mínimo gobernado: seis controles alrededor de un bucle',
                'Diagrama con dos filas: instrucciones y herramientas mínimas; permisos y confinamiento de rutas; protección de las pruebas; verificación obligatoria antes de aceptar la terminación; detección de falta de progreso y tope de pasos; traza y evaluación al final.',
                [[('Instrucciones y herramientas mínimas', 'gold'), ('Permisos y confinamiento de rutas', 'teal'), ('Pruebas protegidas contra escritura', 'teal')],
                 [('Verificación obligatoria antes de terminar', 'navy'), ('Falta de progreso y tope de pasos', 'coral'), ('Traza y evaluación al final', 'plain')]],
                note='Cada caja corresponde a una clase de la parte. El conjunto es pequeño y se puede leer entero; esa es su virtud.',
                note_kind='gold', foot=EJEC, box_h=76)


def se504_adversos() -> Fig:
    return bars('Escenarios adversos que el harness gobernado contiene, de cuatro',
                'Gráfico de barras con los escenarios adversos contenidos de cuatro: sin controles 1, que es el intento repetido que solo acota el tope, y harness gobernado 4.',
                [('Sin controles', 1, 'coral', '1 de 4'), ('Gobernado', 4, 'teal', '4 de 4')],
                scale=30, note='Sin controles, solo el tope de 12 pasos limitó un escenario. Contener los cuatro no prueba que el harness sea seguro: prueba que estos cuatro controles funcionan contra estos cuatro intentos.',
                note_kind='coral', foot=EJEC, label_w=250)


FIGURES = {
    "se-583-defectos-y-compuertas.svg": se499_cambios,
    "se-583-atrapados-por-compuerta.svg": se499_por_compuerta,
    "se-583-menu-unico.svg": se499_menu,
    "se-584-fusiones-de-git.svg": se500_fusiones,
    "se-584-solapamiento-de-agentes.svg": se500_solapamiento,
    "se-584-roles-de-coordinacion.svg": se500_roles,
    "se-585-metricas-de-trazas.svg": se501_trazas,
    "se-585-potencia-de-la-comparacion.svg": se501_potencia,
    "se-585-falsos-positivos.svg": se501_falsos_positivos,
    "se-586-clasificacion-de-riesgo.svg": se502_clasificacion,
    "se-586-defectos-que-escapan.svg": se502_escapes,
    "se-586-ciclo-con-compuertas.svg": se502_ciclo,
    "se-587-fallos-inyectados.svg": se503_fallos,
    "se-587-aciertos-del-diagnostico.svg": se503_aciertos,
    "se-587-procedimiento.svg": se503_procedimiento,
    "se-588-escenarios-adversos.svg": se504_escenarios,
    "se-588-arquitectura.svg": se504_arquitectura,
    "se-588-contencion.svg": se504_adversos,
}
