"""Figures for SE-463 to SE-468 (AI-assisted development: synthetic processes with fixed seeds and real runs of standard-library code).

Los números se calculan con scripts/experiments_part38_b.py para que figuras y texto no se transcriban a mano.
"""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, scatter, stacked_bars
from figure_diagrams import fan
from figures_part07_a import bars

from functools import lru_cache

import experiments_part38_b as ex
from figures_part38_a import EJEC, SINT, n, p

@lru_cache(maxsize=None)
def R(name: str):
    return getattr(ex, name)()


# ---------------------------------------------------------------- SE-463
def se463_umbral_del_revisor() -> Fig:
    f = R("e463_umbral")["filas"]
    ts = [(r["umbral"], n(r["umbral"], 2)) for r in f]
    return line_chart(
        '400 cambios sintéticos (80 con defecto real): lo que marca un revisor automático según su umbral',
        f'Líneas con la precisión y la cobertura de un revisor automático según su umbral: con umbral {n(f[0]["umbral"], 2)} marca {f[0]["marcados"]} cambios con precisión {p(f[0]["precision"])} y cobertura {p(f[0]["cobertura"])}; con {n(f[4]["umbral"], 2)} marca {f[4]["marcados"]} con precisión {p(f[4]["precision"])} y cobertura {p(f[4]["cobertura"])}; subir el umbral sube la precisión y baja la cobertura.',
        [("Precisión", [(r["umbral"], r["precision"], n(r["precision"]), "t") for r in f], "teal"), ("Cobertura de defectos", [(r["umbral"], r["cobertura"], n(r["cobertura"]), "t") for r in f], "coral")],
        x_label="Umbral del revisor", y_label="Porcentaje (%)", x_ticks=ts, y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        note='Subir el umbral baja el ruido y deja pasar defectos; bajarlo cubre casi todo y obliga a revisar cientos de alarmas falsas. Las puntuaciones son gaussianas con medias del autor, no las de un revisor real.', note_kind='gold', foot=SINT)


def se463_equivalencia_por_entradas() -> Fig:
    f = R("e463_equivalencia")["filas"]
    return heatmap(
        'Cuatro versiones refactorizadas frente a la original: probabilidad de que n entradas aleatorias las distingan',
        f'Mapa de calor con la probabilidad de que n entradas aleatorias distingan cada refactorización de la original: la equivalente nunca difiere; las que pierden el orden o descartan la nota cero se distinguen con 5 entradas; la que descarta cursos con 5 notas o más necesita 1 000 entradas para el {p(f[3]["detecta_1000"])}.',
        [r["candidato"].capitalize() for r in f], ["5 entradas", "20", "100", "1 000"],
        [[r["detecta_5"], r["detecta_20"], r["detecta_100"], r["detecta_1000"]] for r in f],
        unit="% que la detecta", row_title="Refactorización", col_title="Entradas aleatorias",
        scale="teal", vmin=0, vmax=100, decimals=1, suffix=" %", cell_h=44, label_w=300,
        note='Las diferencias frecuentes se ven con unas pocas entradas; la que ocurre en una de cien exige cientos, y una prueba con tres ejemplos escritos a mano casi nunca la encuentra. Que no aparezca una diferencia no demuestra equivalencia. Las funciones y la distribución de entradas son del autor.', note_kind='coral', foot=EJEC)


def se463_explicar_el_comentario() -> Fig:
    d = R("e463_explicacion")
    items = [('Funciones', d["funciones"], 'gold', str(d["funciones"])), ('Comentario correcto', d["coinciden_con_el_codigo"], 'teal', str(d["coinciden_con_el_codigo"])),
             ('Comentario desfasado', d["explicaciones_que_repiten_el_comentario_erroneas"], 'coral', str(d["explicaciones_que_repiten_el_comentario_erroneas"]))]
    return bars('Treinta funciones con un comentario: qué entrega un explicador que lo repite',
               f'Barras con treinta funciones de las que {d["coinciden_con_el_codigo"]} tienen un comentario que coincide con el código y {d["explicaciones_que_repiten_el_comentario_erroneas"]} un comentario desfasado; un explicador que repite el comentario entrega {d["explicaciones_que_repiten_el_comentario_erroneas"]} explicaciones erróneas.',
               items, 20.0, 'Una explicación fluida que repite el comentario hereda su error y lo presenta con aplomo; leer la sentencia del código lo habría evitado. El número de funciones desfasadas y el parecido con un explicador real son supuestos del autor.',
               label_w=250, width=940, note_kind='coral', foot=EJEC)


# ---------------------------------------------------------------- SE-464
def se464_espacio_de_interpretaciones() -> Fig:
    d = R("e464_ambiguedad")
    f = d["filas"]
    return line_chart(
        '«Calcula la nota final»: interpretaciones coherentes con el texto según las restricciones dadas',
        f'Línea en escala logarítmica con las interpretaciones coherentes de «calcula la nota final» al añadir restricciones: sin restricciones hay {f[0]["interpretaciones"]} y se acierta al azar con {p(f[0]["p_acertar_al_azar"], 2)}; cada restricción divide por tres y con todas queda {f[6]["interpretaciones"]} interpretación.',
        [("Interpretaciones posibles", [(i, r["interpretaciones"], f'{r["interpretaciones"]} · {p(r["p_acertar_al_azar"], 2)}', "t" if i else "r") for i, r in enumerate(f)], "teal")],
        x_label="Restricciones añadidas a la instrucción", y_label="Interpretaciones posibles", log_y=True,
        x_ticks=[(i, r["paso"]) for i, r in enumerate(f)], y_ticks=[1, 10, 100, 1000], point_labels="none", plot_h=280,
        note='Seis dimensiones con tres opciones dan 729 combinaciones; cada restricción divide por tres. Las dimensiones y sus opciones son un ejemplo del autor, y las combinaciones reales dependen de requisitos que no se enumeran tan limpiamente.', note_kind='teal', foot='Enumeración exacta del producto cartesiano; no interviene ningún modelo.')


def se464_versiones_en_contexto() -> Fig:
    d = R("e464_distractores")
    items = [('Sin filtrar versiones', d["sin_filtro"], 'coral', p(d["sin_filtro"])), ('Filtrando la versión vigente', d["con_filtro"], 'teal', p(d["con_filtro"]))]
    return bars(f'{d["consultas"]} consultas con documentos de versiones anteriores mezclados en el contexto',
               f'Barras con el porcentaje de consultas en que el primer documento recuperado es el vigente: {p(d["sin_filtro"])} sin filtrar por versión y {p(d["con_filtro"])} filtrando.',
               items, 5.0, 'Los documentos antiguos comparten el vocabulario del vigente y compiten con él por la puntuación; los metadatos de versión resuelven lo que el texto no puede. El 100 % es por construcción, pues se supone la etiqueta de versión correcta, y en la práctica a menudo falta o está mal.',
               label_w=270, width=940, note_kind='gold', foot=SINT)


def se464_reglas_que_chocan() -> Fig:
    d = R("e464_reglas")
    f = d["filas"]
    return line_chart(
        f'Archivos de instrucciones sintéticos con reglas «siempre/nunca» sobre {d["claves"]} temas: los que se contradicen',
        f'Línea con el porcentaje de archivos de instrucciones con al menos una contradicción según el número de reglas sobre {d["claves"]} temas: {p(f[0]["con_conflicto"])} con 5 reglas, {p(f[1]["con_conflicto"])} con 10, {p(f[2]["con_conflicto"])} con 20 y {p(f[3]["con_conflicto"])} con 40.',
        [("Archivos con alguna contradicción", [(r["reglas"], r["con_conflicto"], n(r["con_conflicto"]), "t") for r in f], "coral")],
        x_label="Reglas en el archivo", y_label="Archivos con alguna contradicción (%)", x_ticks=[(r["reglas"], str(r["reglas"])) for r in f], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        note='Un detector que compara reglas del mismo tema las encuentra todas, pero solo si las reglas se escriben de forma estructurada; en prosa libre la contradicción pasa desapercibida. Las 500 muestras por tamaño y la elección al azar de tema y polaridad son del autor.', note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-465
def se465_tamano_del_conjunto() -> Fig:
    f = R("e465_tamano")["filas"]
    return percentile_intervals(
        'Un sistema con 70 % de éxito y otro con 75 %: intervalo de Wilson y probabilidad de ordenarlos bien',
        f'Intervalos horizontales con el intervalo de Wilson al 95 por ciento para un 70 por ciento de éxito según el tamaño del conjunto: con {f[0]["tareas"]} tareas va de {p(f[0]["ic"][0])} a {p(f[0]["ic"][1])}, con {f[3]["tareas"]} de {p(f[3]["ic"][0])} a {p(f[3]["ic"][1])} y con {f[4]["tareas"]} de {p(f[4]["ic"][0])} a {p(f[4]["ic"][1])}; la probabilidad de ordenar bien 70 y 75 por ciento sube de {p(f[0]["ordena_bien"])} a {p(f[4]["ordena_bien"])}.',
        [(f'{r["tareas"]} tareas', [r["ic"][0], 70, r["ic"][1]]) for r in f],
        unit="Tasa de éxito (%)", marks=("límite inferior", "70 % observado", "límite superior"), decimals=1, label_w=120,
        note='Con 100 tareas la diferencia de cinco puntos se ordena bien tres de cada cuatro veces; para distinguir cinco puntos con holgura hacen falta cientos. Las tasas de éxito son hipotéticas y las tareas se suponen independientes e igual de difíciles.', note_kind='coral', foot=SINT)


def se465_frontera_costo_calidad() -> Fig:
    d = R("e465_frontera")
    f = d["filas"]
    return scatter(
        'Seis configuraciones sintéticas: éxito, costo por intento, latencia y costo por solución aceptada',
        f'Dispersión de la latencia y la tasa de éxito de seis configuraciones de un asistente: el pequeño con reintento queda dominado, con menos éxito que el mediano y más latencia; el éxito sube de {n(f[0]["exito"], 0)} por ciento con {n(f[0]["latencia_s"])} segundos a {n(f[5]["exito"], 0)} con {n(f[5]["latencia_s"], 0)} segundos; el costo por solución aceptada incluye una revisión humana de {n(d["revision"], 2)}.',
        [("Configuración no dominada", [(r["latencia_s"], r["exito"], r["config"], "l" if r["config"] == "mediano" else "r") for r in f if not r["dominada"]], "teal"),
         ("Configuración dominada", [(r["latencia_s"], r["exito"], r["config"], "r") for r in f if r["dominada"]], "coral")],
        x_label="Latencia (s)", y_label="Éxito (%)", x_ticks=[(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10"), (12, "12"), (18, "")], y_ticks=[40, 50, 60, 70, 80, 90, 100], y_zero=False,
        note=f'La revisión humana (0,40 por intento) pesa mucho más que el costo del modelo: lo barato por intento sale caro por solución aceptada. Todos los valores, incluida la revisión de {n(d["revision"], 2)}, son supuestos del autor en una unidad arbitraria.', note_kind='gold', foot=SINT)


def se465_sesgos_del_juez() -> Fig:
    d = R("e465_juez")
    items = [('Acuerdo con la etiqueta humana', d["acuerdo_con_humano"], 'gold', p(d["acuerdo_con_humano"])),
             ('Mismo veredicto al intercambiar el orden', d["estable_al_intercambiar_orden"], 'coral', p(d["estable_al_intercambiar_orden"])),
             ('Gana la respuesta más larga', d["gana_la_mas_larga"], 'coral', p(d["gana_la_mas_larga"]))]
    return bars(f'Un juez automático sintético con sesgos de posición y de longitud ({d["n"]} comparaciones)',
               f'Barras con tres medidas de un juez automático: acuerda con la etiqueta humana {p(d["acuerdo_con_humano"])}, mantiene el veredicto al intercambiar el orden {p(d["estable_al_intercambiar_orden"])} y gana la respuesta más larga en {p(d["gana_la_mas_larga"])} de las comparaciones, cuando por azar serían 50 por ciento.',
               items, 5.0, 'Un 83 % de acuerdo suena bien y convive con que una cuarta parte de los veredictos cambie solo por el orden de presentación. Los sesgos son parámetros del autor; medir los de un juez real exige comparaciones con orden permutado.',
               label_w=300, width=980, note_kind='coral', foot=SINT)


# ---------------------------------------------------------------- SE-466
def se466_escaner_de_datos() -> Fig:
    d = R("e466_escaner")
    nombres = {"correo": "Correo electrónico", "secreto": "Cadena aleatoria alfanumérica", "secreto_hex": "Cadena aleatoria hexadecimal", "identificador": "Identificador con guion", "limpio": "Texto sin datos sensibles"}
    ks = list(d)
    return heatmap(
        '240 mensajes sintéticos: qué detecta cada regla de un escáner previo al envío',
        'Mapa de calor con cuántos mensajes de cada clase detecta cada regla de un escáner previo al envío: el patrón detecta los 40 correos y los 40 identificadores, la entropía solo las cadenas alfanuméricas, la palabra clave seguida de un valor las dos cadenas aleatorias, y las tres reglas juntas cubren los cuatro tipos de dato sin marcar ningún texto limpio.',
        [f'{nombres[k]} ({d[k]["n"]})' for k in ks], ["Patrón", "Entropía", "Contexto", "Las tres"],
        [[d[k]["patron"], d[k]["entropia"], d[k]["contexto"], d[k]["las_tres"]] for k in ks],
        unit="detectados", row_title="Clase de mensaje (casos)", col_title="Mensajes detectados por cada regla",
        scale="teal", vmin=0, vmax=40, decimals=0, cell_h=42, label_w=300,
        note='Cada regla ve una cara; la entropía no puede marcar una cadena hexadecimal porque su entropía máxima es 4 bits, y la regla de contexto depende de la palabra «clave». Las cadenas se generan en tiempo de ejecución; ninguna es un dato real. Los mensajes son plantillas del autor.', note_kind='gold', foot=EJEC)


def se466_patrones_inseguros() -> Fig:
    d = R("e466_patrones")
    return grouped_bars(
        f'{len(ex.SNIPPETS)} fragmentos de Python ({d["inseguros"]} inseguros): búsqueda de texto frente a recorrido del árbol sintáctico',
        f'Barras agrupadas con el resultado de dos técnicas para encontrar nueve patrones inseguros: la búsqueda de texto halla {d["filas"][0]["verdaderos"]}, marca {d["filas"][0]["falsos_positivos"]} fragmentos seguros y omite {d["filas"][0]["omitidos"]}; el recorrido del árbol sintáctico halla {d["filas"][1]["verdaderos"]}, marca {d["filas"][1]["falsos_positivos"]} y omite {d["filas"][1]["omitidos"]}.',
        [r["tecnica"].capitalize() for r in d["filas"]],
        [("Inseguros hallados", [r["verdaderos"] for r in d["filas"]], "teal"), ("Falsas alarmas", [r["falsos_positivos"] for r in d["filas"]], "coral"), ("Inseguros omitidos", [r["omitidos"] for r in d["filas"]], "gold")],
        unit="Fragmentos", ticks=[0, 2, 4, 6, 8],
        note='El árbol evita marcar comentarios y mensajes pero no ve alias como «f = eval»; ninguna de las dos técnicas sustituye a un análisis de flujo de datos. Los fragmentos están escritos por el autor, algunos pensados para engañar a cada técnica.', note_kind='coral', foot=EJEC)


def se466_parecido_con_licencia() -> Fig:
    f = R("e466_similitud")["filas"]
    return grouped_bars(
        'Huellas de cinco símbolos: fragmento generado frente a un corpus con licencia',
        f'Barras horizontales con el porcentaje de huellas de cinco símbolos de cada fragmento que aparece en el corpus: la copia literal da {p(100 * f[0]["literal"], 0)} en las dos comparaciones; la copia con nombres cambiados baja a {p(100 * f[1]["literal"], 0)} comparando símbolos literales y vuelve a {p(100 * f[1]["normalizada"], 0)} con identificadores normalizados; una solución independiente da {p(100 * f[3]["literal"], 0)} y {p(100 * f[3]["normalizada"], 0)}.',
        [r["caso"] for r in f],
        [("Huellas literales", [100 * r["literal"] for r in f], "coral"), ("Con identificadores normalizados", [100 * r["normalizada"] for r in f], "teal")],
        unit="Huellas presentes en el corpus (%)", horizontal=True, label_w=270, decimals=0, ticks=[0, 20, 40, 60, 80, 100],
        note='Cambiar los nombres engaña a la comparación literal pero no a la normalizada; un idioma muy común coincide al 100 % sin ser copia de nadie. Un parecido alto es una señal para investigar y no un veredicto de infracción. El corpus de una función es mínimo y del autor.', note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-467
def se467_tres_flujos() -> Fig:
    d = R("e467_flujos")
    return percentile_intervals(
        f'{d["n"]} tareas sintéticas en tres flujos: horas por tarea y defectos que escapan a la revisión',
        f'Intervalos horizontales con la mediana de horas por tarea y su intervalo bootstrap al 95 por ciento en tres flujos: manual {n(d["filas"][0]["mediana_h"], 2)} horas, asistido {n(d["filas"][1]["mediana_h"], 2)} y automatizado {n(d["filas"][2]["mediana_h"], 2)}; los defectos que escapan a la revisión suben de {d["filas"][0]["defectos_escapan"]} a {d["filas"][1]["defectos_escapan"]} y {d["filas"][2]["defectos_escapan"]}.',
        [(r["flujo"].capitalize(), [r["ic95"][0], r["mediana_h"], r["ic95"][1]]) for r in d["filas"]],
        unit="Horas por tarea", marks=("IC 95 % inferior", "mediana", "IC 95 % superior"), decimals=2, label_w=130,
        note='Cada paso ahorra tiempo y deja escapar más defectos: no hay un flujo «mejor» sin decidir cuánto vale cada defecto. Todos los tiempos relativos y tasas de defecto son supuestos del autor; no se midió a ninguna persona ni herramienta.', note_kind='gold', foot=SINT)


def se467_punto_de_equilibrio() -> Fig:
    d = R("e467_sensibilidad")
    f = d["filas"]
    ts = [(r["aciertos"], f'{n(r["aciertos"], 0)} %') for r in f]
    return line_chart(
        'Flujo asistido frente a manual: ahorro de tiempo según la tasa de aciertos del asistente',
        f'Línea con el ahorro de tiempo del flujo asistido frente al manual según la tasa de aciertos del asistente: con {p(f[0]["aciertos"], 0)} ahorra {p(f[0]["ahorro"], 0)}, con 50 por ciento no ahorra nada y con {p(f[4]["aciertos"], 0)} cuesta {p(abs(f[4]["ahorro"]), 0)} más; la línea roja marca el punto de equilibrio.',
        [("Ahorro de tiempo", [(r["aciertos"], r["ahorro"], p(r["ahorro"], 0), "t") for r in f], "teal")],
        x_label="Aciertos del asistente", y_label="Ahorro frente al flujo manual (%)", x_ticks=ts, y_ticks=[-30, -20, -10, 0, 10, 20, 30, 40], point_labels="none", hlines=[(0, "equilibrio")],
        note=f'Con generar 35 %, revisar 25 % y rehacer 80 % del tiempo manual, el asistente solo ahorra por encima del {p(d["p_equilibrio"], 0)} de aciertos. Los tres porcentajes son supuestos del autor y se pueden cambiar; la tasa real de aciertos se mide por tipo de tarea.', note_kind='coral', foot='Cálculo exacto con la fórmula del texto; sin simulación ni modelo real.')


def se467_diseno_pareado() -> Fig:
    f = R("e467_diseno")["filas"]
    return line_chart(
        'Detectar una diferencia real del 15 % en tiempo: diseño pareado frente a grupos distintos',
        f'Líneas con la probabilidad de detectar una diferencia real del 15 por ciento según el número de tareas: con {f[1]["tareas"]} tareas el diseño pareado la detecta {p(f[1]["pareado"], 0)} y el de grupos distintos {p(f[1]["independiente"], 0)}; con {f[3]["tareas"]} tareas {p(f[3]["pareado"], 0)} y {p(f[3]["independiente"], 0)}.',
        [("Mismas tareas en ambos flujos", [(r["tareas"], r["pareado"], p(r["pareado"], 0), "t") for r in f], "teal"), ("Tareas distintas en cada flujo", [(r["tareas"], r["independiente"], p(r["independiente"], 0), "t") for r in f], "coral")],
        x_label="Tareas por flujo", y_label="Probabilidad de detectar la diferencia (%)", log_x=True, x_ticks=[(r["tareas"], str(r["tareas"])) for r in f], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        note='La dificultad varía mucho más entre tareas que entre flujos; si cada flujo hace tareas distintas, esa variación tapa el efecto. Hacer las mismas tareas en los dos flujos (con orden alternado) lo revela con una fracción de las tareas. La variación de tareas es lognormal del autor.', note_kind='teal', foot=SINT)


# ---------------------------------------------------------------- SE-468
def se468_bitacora_encadenada() -> Fig:
    d = R("e468_bitacora")
    return fan(
        'Bitácora de seis pasos encadenada por hash: qué manipulaciones detecta la verificación',
        f'Diagrama de las manipulaciones de una bitácora de seis entradas encadenadas por hash: editar o borrar la entrada 3 se detecta en la entrada {d["editar_entrada_3_detectada_en"]}, intercambiar las entradas 2 y 3 en la {d["intercambiar_2_y_3_detectada_en"]}; editar la 3 y recalcular todos los hashes siguientes no se detecta; con el último hash guardado fuera de la bitácora sí se detecta.',
        ("Bitácora de seis entradas encadenada por hash", "la verificación recorre la cadena", "navy"),
        [("Editar el texto de la entrada 3", f'se detecta en la entrada {d["editar_entrada_3_detectada_en"]}', "teal"),
         ("Borrar la entrada 3", f'se detecta en la entrada {d["borrar_entrada_3_detectada_en"]}', "teal"),
         ("Intercambiar las entradas 2 y 3", f'se detecta en la entrada {d["intercambiar_2_y_3_detectada_en"]}', "teal"),
         ("Editar la 3 y recalcular todos los hashes siguientes", "no se detecta: la verificación pasa sin error", "coral"),
         ("Lo mismo, con el último hash guardado fuera de la bitácora", "el último hash no coincide: se detecta", "teal")],
        note='El encadenado detecta alteraciones torpes y no a quien tiene acceso para reescribir la cola: hace falta un ancla externa (el último hash en otro sistema, una firma). Es evidencia de integridad, no de que el contenido sea cierto.', note_kind='gold', foot=EJEC)


def se468_compuertas() -> Fig:
    d = R("e468_compuertas")
    f = d["filas"]
    return grouped_bars(
        'Cambios asistidos sintéticos (20 % con defecto): defectos que llegan a producción según las compuertas',
        f'Barras horizontales con los defectos que llegan a producción de 10 000 cambios asistidos según las compuertas: sin compuertas {f[0]["defectos_en_produccion"]}, solo pruebas {f[1]["defectos_en_produccion"]}, pruebas y análisis {f[2]["defectos_en_produccion"]}, con revisión {f[3]["defectos_en_produccion"]} y las cuatro compuertas {f[4]["defectos_en_produccion"]}.',
        [r["compuertas"].capitalize() for r in f],
        [("Defectos en producción", [r["defectos_en_produccion"] for r in f], "coral")],
        unit="Defectos que llegan a producción, de 10 000 cambios", horizontal=True, label_w=250, ticks=[0, 500, 1000, 1500, 2000, 2500],
        note=f'Cada compuerta quita una fracción y ninguna llega a cero; además la revisión humana pierde eficacia con el tamaño: detecta {p(d["fatiga"][0]["p_detectar"])} con 20 líneas y {p(d["fatiga"][3]["p_detectar"])} con 1.000. Las probabilidades de detección y su independencia son supuestos del autor.', note_kind='coral', foot=SINT)


def se468_reversion_limpia() -> Fig:
    f = R("e468_reversion")["filas"]
    return line_chart(
        'Revertir un cambio de 40 líneas (4 bloques de 10) en un archivo de 400 tras k ediciones posteriores',
        f'Línea con la probabilidad de revertir un cambio de 40 líneas sin conflicto según las ediciones posteriores: {p(f[0]["reversion_limpia"])} sin ediciones, {p(f[1]["reversion_limpia"])} con 5, {p(f[2]["reversion_limpia"])} con 20 y {p(f[3]["reversion_limpia"])} con 60.',
        [("Reversión limpia", [(r["ediciones_posteriores"], r["reversion_limpia"], p(r["reversion_limpia"]), "r") for r in f], "coral")],
        x_label="Ediciones posteriores en el archivo", y_label="Reversión sin conflicto (%)", x_ticks=[(r["ediciones_posteriores"], str(r["ediciones_posteriores"])) for r in f] + [(170, "")], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        note='La ventana para deshacer un cambio sin conflictos se cierra rápido: cuanto más tarda la revisión, más probable es que revertir sea ya otro cambio. Las ediciones al azar sobre líneas uniformes son una simplificación del autor; los cambios reales se concentran.', note_kind='gold', foot=SINT)


FIGURES = {
    "se-463-umbral-del-revisor.svg": se463_umbral_del_revisor,
    "se-463-equivalencia-por-entradas.svg": se463_equivalencia_por_entradas,
    "se-463-explicar-el-comentario.svg": se463_explicar_el_comentario,
    "se-464-espacio-de-interpretaciones.svg": se464_espacio_de_interpretaciones,
    "se-464-versiones-en-contexto.svg": se464_versiones_en_contexto,
    "se-464-reglas-que-chocan.svg": se464_reglas_que_chocan,
    "se-465-tamano-del-conjunto.svg": se465_tamano_del_conjunto,
    "se-465-frontera-costo-calidad.svg": se465_frontera_costo_calidad,
    "se-465-sesgos-del-juez.svg": se465_sesgos_del_juez,
    "se-466-escaner-de-datos.svg": se466_escaner_de_datos,
    "se-466-patrones-inseguros.svg": se466_patrones_inseguros,
    "se-466-parecido-con-licencia.svg": se466_parecido_con_licencia,
    "se-467-tres-flujos.svg": se467_tres_flujos,
    "se-467-punto-de-equilibrio.svg": se467_punto_de_equilibrio,
    "se-467-diseno-pareado.svg": se467_diseno_pareado,
    "se-468-bitacora-encadenada.svg": se468_bitacora_encadenada,
    "se-468-compuertas.svg": se468_compuertas,
    "se-468-reversion-limpia.svg": se468_reversion_limpia,
}
