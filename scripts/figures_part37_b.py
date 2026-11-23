"""Figures for SE-451 to SE-456 (real-time, verification and assurance: runs of real CPython code and seeded models over the Horno de curado case and the Therac-25 case; Windows CPython 3.12.9; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, line_chart, percentile_intervals, stacked_bars

from figures_part45_a import flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9; los recuentos se repiten con la misma semilla."
MODELO = "Modelo con parámetros del autor y semilla fija 47; muestra un mecanismo, no mide un producto real."


# ---------------------------------------------------------------- SE-451
def se571_inversion() -> Fig:
    return grouped_bars(
        "Tres tareas con un mutex compartido durante 400 ms simulados: plazos perdidos y ticks bloqueados de la tarea de más prioridad",
        "Barras con los resultados de tres protocolos: sin protocolo, la tarea H pierde 2 plazos y queda bloqueada 84 ticks; con herencia de prioridad pierde 0 y queda bloqueada 25 ticks; con techo de prioridad pierde 0 y queda bloqueada 0.",
        ["Sin protocolo", "Herencia de prioridad", "Techo de prioridad"],
        [("Plazos perdidos de H", [2, 0, 0], "coral"), ("Ticks de H bloqueada", [84, 25, 0], "navy")],
        unit="Plazos o ticks de 1 ms", decimals=0, plot_h=260,
        note="La tarea de prioridad media se interpone mientras la de baja prioridad tiene el mutex que H necesita: es la inversión de prioridad. La herencia acota el bloqueo a la sección crítica restante (25 ticks acumulados en la ventana); con techo no se bloquea nunca porque nadie más entra a la sección crítica a destiempo. Es un simulador de ticks, no un RTOS.",
        note_kind="coral", foot=EJEC)


def se571_analisis() -> Fig:
    return grouped_bars(
        "Respuesta máxima de cada tarea con herencia de prioridad: simulada y calculada por análisis de tiempo de respuesta",
        "Barras con la respuesta máxima en milisegundos de las tareas H, M y L: simulada 23, 63 y 120, y calculada con bloqueo de 13 milisegundos 23, 63 y 120; sin tener en cuenta el bloqueo, el análisis daría 10, 40 y 120.",
        ["H (prioridad alta)", "M (prioridad media)", "L (prioridad baja)"],
        [("Simulada", [23, 63, 120], "teal"), ("Análisis con bloqueo", [23, 63, 120], "navy"), ("Análisis sin bloqueo", [10, 40, 120], "grey")],
        unit="Milisegundos", decimals=0, plot_h=270,
        note="El análisis coincide con el simulador cuando incluye el bloqueo: 13 ms para H por la sección crítica y 13 ms para M porque L hereda la prioridad de H y corre por encima de M. Omitir el bloqueo subestima H en más del doble. La cota de Liu y Layland para tres tareas es 0,780 y la utilización de este conjunto 0,829: la cota es suficiente, no necesaria.",
        note_kind="gold", foot=EJEC)


def se571_wcet() -> Fig:
    return percentile_intervals(
        "Pasos de una ordenación de 8 elementos: mediana, máximo observado en 1000 entradas al azar y peor caso real",
        "Intervalo con la mediana de 56 pasos, el máximo observado de 80 y el peor caso real de 84 pasos de una ordenación con intercambio y salida anticipada.",
        [("Ordenación de 8 elementos", [56, 80, 84])], unit="Pasos de ejecución", marks=("mediana", "máx. observado", "peor caso"), decimals=0,
        note="La marca de agua medida queda 4,8 % por debajo del peor caso, que se alcanza con la entrada en orden inverso; 1000 entradas al azar no lo generan. La medición da un límite inferior del WCET, no una cota; el análisis de caminos o la entrada construida a propósito la encuentran. Se cuentan pasos y no segundos para que el resultado no dependa del equipo.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-452
def se572_reglas() -> Fig:
    return grouped_bars(
        "Seis reglas comprobables por máquina sobre dos versiones de las mismas tres funciones: avisos por regla",
        "Barras con los avisos de cada regla: la muestra con recursión, bucle sin cota, función con lógica sin aserciones, valor de retorno ignorado y excepción vacía acumula 1 aviso en cada una de cinco reglas y 0 en la de longitud; la versión corregida acumula 0 en las seis.",
        ["Sin recursión", "Bucles con cota", "Funciones cortas", "Aserciones", "Retorno comprobado", "Sin excepción vacía"],
        [("Muestra con defectos", [1, 1, 0, 1, 1, 1], "coral"), ("Versión corregida", [0, 0, 0, 0, 0, 0], "teal")],
        unit="Avisos", decimals=0, plot_h=250,
        note="Las reglas se inspiran en las diez reglas de Holzmann para código de misión crítica (NASA/JPL) y se implementan sobre el árbol sintáctico de Python. Una regla mecánica también da falsos positivos: la recursión acotada por la profundidad de un árbol dispara el aviso de recursión aunque sea segura.",
        note_kind="gold", foot=EJEC)


def se572_desbordamiento() -> Fig:
    return grouped_bars(
        "Promedio de dos enteros sin signo de 16 bits con aritmética modular: pares con resultado incorrecto según el conjunto de prueba",
        "Barras con el porcentaje de pares con resultado incorrecto: 50,0 por ciento con 200 000 pares al azar de 16 bits, 0 con los 65 536 pares de valores pequeños de 0 a 255 y 0 con la fórmula que resta antes de dividir.",
        ["Pares al azar de 16 bits", "Pares pequeños (0 a 255)", "Con la resta previa"],
        [("Resultado incorrecto (%)", [50.0, 0.0, 0.0], "coral")], unit="Por ciento de pares", decimals=1, plot_h=250,
        note="La suma se desborda cuando supera 65 535 y el resultado envuelve sin avisar. Las pruebas con valores pequeños no lo ven jamás: el defecto exige entradas que las pruebas habituales no generan. Es la clase de defecto de las reglas sobre enteros de los estándares de codificación segura; aquí se emula la aritmética en Python y no se ejecuta C.",
        note_kind="teal", foot=EJEC)


def se572_cadena() -> Fig:
    return flow("Qué comprueba cada capa de una política de codificación segura y qué deja a la capa siguiente",
                "Diagrama de cuatro cajas: reglas del estándar de codificación comprobadas por herramienta, revisión por una persona de las desviaciones justificadas, pruebas dinámicas con entradas extremas, y análisis estático o formal para lo que las pruebas no alcanzan.",
                [[("Regla\nComprobada por herramienta en cada cambio", "teal"), ("Desviación\nJustificada por escrito y revisada", "gold"),
                  ("Prueba\nEntradas extremas y de frontera", "teal"), ("Análisis\nEstático o formal donde las pruebas no llegan", "coral")]],
                note="Un estándar de codificación reduce clases de defectos, no demuestra corrección: una regla cumplida no dice que el programa haga lo correcto. Las desviaciones con justificación son parte del proceso, no un fallo del proceso.",
                note_kind="teal", box_h=118, foot=EJEC)


# ---------------------------------------------------------------- SE-453
def se573_estados() -> Fig:
    return grouped_bars(
        "Cuatro protocolos de exclusión mutua para dos procesos: estados alcanzables explorados por el verificador",
        "Barras con los estados alcanzables: comprobar y luego marcar 14 con la exclusión mutua violada, solo bandera 15 con exclusión mutua correcta pero un bloqueo alcanzable, Peterson con los pasos invertidos 39 con la exclusión mutua violada y Peterson 34 con la propiedad cumplida y sin bloqueos.",
        ["Comprobar y luego marcar", "Solo bandera", "Peterson con pasos invertidos", "Peterson"], [("Estados alcanzables", [14, 15, 39, 34], "navy")],
        unit="Estados alcanzables", decimals=0, horizontal=True, label_w=250,
        note="Dos protocolos violan la exclusión mutua (contraejemplos de 4 y 6 pasos), uno la cumple pero puede bloquearse y solo Peterson cumple la exclusión y no se bloquea en este modelo. Un verificador de estados explícitos propio, en Python, recorre todos los estados; no se ejecutó TLA+, SPARK ni Alloy en esta clase.",
        note_kind="gold", foot=EJEC)


def se573_azar() -> Fig:
    return grouped_bars(
        "Encontrar la violación con planificaciones al azar de 40 pasos frente a explorar todos los estados",
        "Barras con el porcentaje de corridas que encuentran la violación: 86,62 por ciento en el protocolo comprobar y luego marcar, 9,47 en Peterson con los pasos invertidos y 100 con el verificador en ambos.",
        ["Comprobar y luego marcar", "Peterson con pasos invertidos"],
        [("Planificaciones al azar (20 000 corridas)", [86.62, 9.47], "gold"), ("Verificador de estados", [100.0, 100.0], "teal")],
        unit="Por ciento de detección", decimals=2, plot_h=260,
        note="Cuanto más fino es el orden de eventos que revela el defecto, menos probable es que el azar lo produzca: pasar de 4 a 6 pasos de contraejemplo bajó la detección de 87 a 9 por ciento. El verificador la encuentra siempre, y devuelve el camino. Con las pruebas por azar, la ausencia de fallos no demuestra ausencia de defectos.",
        note_kind="coral", foot=EJEC)


def se573_explosion() -> Fig:
    ns = [2, 3, 4, 5, 6, 7]
    return line_chart(
        "Espacio de estados de n procesos independientes de cuatro pasos cada uno: crecimiento exponencial",
        "Línea en escala logarítmica con los estados alcanzables: 16 con 2 procesos, 64 con 3, 256 con 4, 1024 con 5, 4096 con 6 y 16384 con 7.",
        [("Estados alcanzables", list(zip(ns, [16, 64, 256, 1024, 4096, 16384])), "navy")],
        x_label="Procesos", y_label="Estados alcanzables", log_y=True, x_ticks=[(n, str(n)) for n in ns], y_ticks=[10, 100, 1000, 10000], point_labels="all", decimals=0, plot_h=280,
        note="Cada proceso multiplica por cuatro el espacio: es la explosión de estados. Las técnicas que la contienen (abstracción, reducción por orden parcial, verificación simbólica, límites en el tamaño del modelo) tienen costo propio y exigen que el modelo conserve lo que importa. Procesos que no interactúan son el mejor caso; el real es peor.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-454
def se574_mutantes() -> Fig:
    return percentile_intervals(
        "Mutantes de una decisión de cuatro condiciones que matan los conjuntos mínimos de cada criterio (17 mutantes en total)",
        "Intervalos con el mínimo, la media y el máximo de mutantes muertos sobre 17: cobertura de decisión de 4 a 13 con media 8,3; cobertura de condiciones de 3 a 8 con media 5,6; MC/DC de 17 a 17 con media 17.",
        [("Decisión (2 pruebas, 39 conjuntos)", [4, 8.3, 13]), ("Condiciones (2 pruebas, 8 conjuntos)", [3, 5.6, 8]), ("MC/DC (5 pruebas, 4 conjuntos)", [17, 17, 17])],
        unit="Mutantes muertos de 17", marks=("mín", "media", "máx"), decimals=1, label_w=290, ref_lines=[(17, "17")],
        note="De los 8 conjuntos mínimos de cobertura de condiciones, 5 nunca cambian el resultado de la decisión. Los 4 conjuntos mínimos de MC/DC (5 pruebas, n + 1) matan los 17 mutantes de esta decisión, igual que los 16 vectores. Los mutantes los escribió el autor: la ventaja se mide aquí, no se generaliza a otros programas.",
        note_kind="teal", foot=EJEC)


def se574_retardo() -> Fig:
    ds = [0, 2, 5, 10, 15]
    return line_chart(
        "Simulación en software de 300 escenarios de calentamiento: escenarios que superan 250 grados según el retardo del sensor",
        "Línea con los escenarios con violación: 0 con retardo de 0, 2 y 5 muestras, 30 con 10 muestras y 52 con 15 muestras de retardo, con el limitador en 245 grados.",
        [("Escenarios con violación", list(zip(ds, [0, 0, 0, 30, 52])), "coral")],
        x_label="Retardo del sensor (muestras)", y_label="Escenarios de 300 con T mayor que 250", x_ticks=[(d, str(d)) for d in ds], y_ticks=[0, 20, 40, 60], point_labels="all", decimals=0, plot_h=270,
        note="Con retardo cero la lógica es correcta en los 300 escenarios; el defecto aparece solo cuando el sensor llega tarde, una propiedad del hardware y del tiempo que un banco de prueba con el sensor real (HIL) reproduce y una simulación ideal no. Por eso se combinan: simulación para volumen y banco para lo que el modelo no incluye.",
        note_kind="gold", foot=MODELO)


def se574_costo() -> Fig:
    ns = list(range(1, 9))
    return line_chart(
        "Pruebas necesarias para cubrir una decisión con n condiciones: mínimo de MC/DC (n + 1) y combinaciones exhaustivas",
        "Líneas en escala logarítmica con el número de pruebas para n de 1 a 8 condiciones: MC/DC necesita n + 1, de 2 a 9, y el recorrido exhaustivo 2 elevado a n, de 2 a 256.",
        [("MC/DC (n + 1)", [(n, n + 1) for n in ns], "teal"), ("Exhaustivo (2 a la n)", [(n, 2 ** n) for n in ns], "coral")],
        x_label="Condiciones de la decisión", y_label="Pruebas", log_y=True, x_ticks=[(n, str(n)) for n in ns], y_ticks=[1, 10, 100], point_labels="none", plot_h=270,
        note="Con 4 condiciones son 5 pruebas frente a 16; con 8, 9 frente a 256. El mínimo n + 1 vale cuando existen vectores que aíslan cada condición; con condiciones acopladas (la misma variable en dos condiciones) el mínimo es mayor o imposible. La cantidad se cuenta con la definición de independencia de causa única.",
        note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-455
def se575_variantes() -> Fig:
    return grouped_bars(
        "Modelo de la carrera de edición del Therac-25: 100 000 tratamientos con 15 % de ediciones y un ajuste de 8 segundos",
        "Barras con las configuraciones inconsistentes y las exposiciones peligrosas de tres variantes: la original 5705 y 5705, con enclavamiento de hardware 5627 y 58, y con parámetros versionados 0 y 0.",
        ["Original", "Con enclavamiento de hardware", "Parámetros versionados"],
        [("Configuraciones inconsistentes", [5705, 5627, 0], "gold"), ("Exposiciones peligrosas", [5705, 58, 0], "coral")],
        unit="Tratamientos de 100 000", decimals=0, plot_h=260,
        note="El enclavamiento de hardware no evita la inconsistencia: reduce la exposición porque falla con una probabilidad del autor del 1 %. Versionar los parámetros elimina la clase de defecto en este modelo. Es un modelo inspirado en los hechos publicados por Leveson y Turner, no la reconstrucción del código de la máquina; la probabilidad de edición y el reparto de tiempos son supuestos.",
        note_kind="coral", foot=MODELO)


def se575_ventana() -> Fig:
    ws = [2, 4, 8, 12]
    return line_chart(
        "Variante original del modelo: configuraciones inconsistentes por 100 000 tratamientos según la duración de la ventana de ajuste",
        "Línea con las configuraciones inconsistentes: 1129 con una ventana de 2 segundos, 2574 con 4, 5669 con 8 y 8611 con 12 segundos.",
        [("Configuraciones inconsistentes", list(zip(ws, [1129, 2574, 5669, 8611])), "coral")],
        x_label="Ventana de ajuste (segundos)", y_label="Inconsistencias por 100 000", x_ticks=[(w, str(w)) for w in ws], y_ticks=[0, 3000, 6000, 9000], point_labels="all", decimals=0, plot_h=270,
        note="El riesgo crece casi en proporción a la ventana durante la que una edición no se vuelve a comprobar. En el modelo, acortar el ajuste reduce la exposición pero no la elimina; lo que la elimina es invalidar el ajuste ante cada edición. Solo el tope de 8 segundos es un dato del caso; el resto de los valores es del autor.",
        note_kind="gold", foot=MODELO)


def se575_contador() -> Fig:
    return grouped_bars(
        "Modelo del contador de un byte: pasadas de 100 000 en las que se omite la comprobación del colimador",
        "Barras con las pasadas sin comprobación: 390 de 100 000 si la variable se incrementa y vuelve a cero cada 256 pasadas, y 0 si se asigna un valor fijo distinto de cero.",
        ["Incrementar la variable", "Asignar un valor fijo"], [("Pasadas sin comprobación", [390, 0], "coral")],
        unit="Pasadas de 100 000", decimals=0, plot_h=240,
        note="Una pasada de cada 256 es el 0,39 %: pequeño, pero la rutina se ejecuta cientos de veces por puesta a punto. Un invariante enunciado («vale cero solo si todo está bien») y una prueba que ejecute más de 256 pasadas lo habrían hecho visible. La probabilidad real por tratamiento no puede estimarse con los datos publicados.",
        note_kind="teal", foot=MODELO)


# ---------------------------------------------------------------- SE-456
def se576_peligros() -> Fig:
    return stacked_bars(
        "Cinco peligros del Horno de curado: estado de su evidencia en el paquete de aseguramiento inicial",
        "Barra apilada con los cinco peligros: 3 con un control verificado por una prueba que pasa, 1 con un control sin prueba que pase y 1 sin ningún control.",
        ["Peligros del Horno de curado"],
        [("Control verificado", [3], "teal"), ("Control sin prueba que pase", [1], "gold"), ("Sin control", [1], "coral")],
        unit="Peligros", horizontal=True, decimals=0, label_w=210,
        note="La comprobación automática encuentra tres huecos: el control REQ-05 sin prueba, el peligro H5 (deriva de calibración) sin control y el requisito REQ-05 sin prueba. El peligro sin control no se oculta: se registra como riesgo residual que una persona con autoridad acepta o se cierra con un control. Los datos son los del paquete de ejemplo.",
        note_kind="gold", foot=MODELO)


def se576_evidencia() -> Fig:
    return grouped_bars(
        "Tras editar el texto de un requisito sin rehacer la evidencia: huecos de contenido y archivos que ya no coinciden con el manifiesto",
        "Barras con huecos de contenido, 3 antes y 3 después de editar REQ-02, y archivos de evidencia que no coinciden con el manifiesto de resúmenes SHA-256: 0 antes y 1 después.",
        ["Antes de editar REQ-02", "Después de editar REQ-02"],
        [("Huecos de contenido", [3, 3], "gold"), ("Archivos que no coinciden con el manifiesto", [0, 1], "coral")],
        unit="Elementos", decimals=0, plot_h=240,
        note="Las comprobaciones de contenido no ven el cambio porque todas las referencias siguen existiendo; el manifiesto sí. Dice que la evidencia ya no es la que se revisó y no si la prueba sigue valiendo: esa decisión es de una persona. Sin manifiesto, un paquete puede quedar verde con evidencia de una versión anterior.",
        note_kind="coral", foot=EJEC)


def se576_paquete() -> Fig:
    return flow("Cadena de un paquete de aseguramiento: cada eslabón apunta al anterior y se resume con un hash",
                "Diagrama de cinco cajas en dos filas: peligros con sus controles, requisitos derivados, pruebas con resultados, comprobación automática de huecos, y manifiesto de resúmenes firmado por una persona responsable.",
                [[("Peligros\nCada uno con sus controles", "coral"), ("Requisitos\nLos controles hechos verificables", "gold"), ("Pruebas y resultados\nVinculados a requisitos", "teal")],
                 [("Comprobación\nHuecos y referencias rotas", "gold"), ("Manifiesto\nResumen de cada archivo y decisión de una persona", "teal")]],
                note="El paquete no demuestra seguridad: ordena la evidencia para que otra persona pueda desafiarla. La herramienta señala lo que falta o cambió; la aceptación del riesgo residual es de una persona con nombre y autoridad.",
                note_kind="teal", box_h=96, foot=EJEC)


FIGURES = {
    "se-451-inversion.svg": se571_inversion,
    "se-451-analisis.svg": se571_analisis,
    "se-451-wcet.svg": se571_wcet,
    "se-452-reglas.svg": se572_reglas,
    "se-452-desbordamiento.svg": se572_desbordamiento,
    "se-452-cadena.svg": se572_cadena,
    "se-453-estados.svg": se573_estados,
    "se-453-azar.svg": se573_azar,
    "se-453-explosion.svg": se573_explosion,
    "se-454-mutantes.svg": se574_mutantes,
    "se-454-retardo.svg": se574_retardo,
    "se-454-costo.svg": se574_costo,
    "se-455-variantes.svg": se575_variantes,
    "se-455-ventana.svg": se575_ventana,
    "se-455-contador.svg": se575_contador,
    "se-456-peligros.svg": se576_peligros,
    "se-456-evidencia.svg": se576_evidencia,
    "se-456-paquete.svg": se576_paquete,
}
