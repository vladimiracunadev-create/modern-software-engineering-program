"""Figures for SE-463 to SE-468 (AI-assisted development: synthetic processes with fixed seeds and real runs of standard-library code).

Los números se calculan con scripts/experiments_part38_b.py para que figuras y texto no se transcriban a mano.
"""
from __future__ import annotations

from functools import lru_cache

import experiments_part38_b as ex
from figure_kit import Fig
from figures_part07_a import bars, tab
from figures_part38_a import EJEC, SINT, n, p

@lru_cache(maxsize=None)
def R(name: str):
    return getattr(ex, name)()


# ---------------------------------------------------------------- SE-463
def se463_umbral_del_revisor() -> Fig:
    f = R("e463_umbral")["filas"]
    rows = [[n(r["umbral"], 2), str(r["marcados"]), p(r["precision"]), p(r["cobertura"]), str(r["falsas_alarmas"])] for r in f]
    return tab('400 cambios sintéticos (80 con defecto real): lo que marca un revisor automático según su umbral',
              f'Tabla con cinco umbrales de un revisor automático sobre 400 cambios con 80 defectos: con umbral {n(f[0]["umbral"], 2)} marca {f[0]["marcados"]} cambios con precisión {p(f[0]["precision"])} y cobertura {p(f[0]["cobertura"])}; con {n(f[4]["umbral"], 2)} marca {f[4]["marcados"]} con precisión {p(f[4]["precision"])} y cobertura {p(f[4]["cobertura"])}.',
              ['Umbral', 'Cambios marcados', 'Precisión', 'Defectos cubiertos', 'Falsas alarmas'], rows, [150, 210, 170, 220, 180], row_h=44, size=13,
              note='Subir el umbral baja el ruido y deja pasar defectos; bajarlo cubre casi todo y obliga a revisar cientos de alarmas falsas. Las puntuaciones son gaussianas con medias del autor, no las de un revisor real.',
              note_kind='gold', foot=SINT)


def se463_equivalencia_por_entradas() -> Fig:
    f = R("e463_equivalencia")["filas"]
    rows = [[r["candidato"], p(r["p_por_entrada"], 2), p(r["detecta_5"]), p(r["detecta_20"]), p(r["detecta_100"]), p(r["detecta_1000"])] for r in f]
    return tab('Cuatro versiones refactorizadas frente a la original: probabilidad de que n entradas aleatorias las distingan',
              f'Tabla con la probabilidad de detectar la diferencia con 5, 20, 100 y 1.000 entradas aleatorias: la refactorización equivalente nunca difiere, las que pierden el orden o descartan la nota cero se detectan con 5 entradas y la que descarta cursos con cinco notas difiere en {p(f[3]["p_por_entrada"], 2)} de las entradas y se detecta con {p(f[3]["detecta_5"])} con 5 entradas y {p(f[3]["detecta_100"])} con 100.',
              ['Refactorización', 'Entradas que difieren', '5 entradas', '20', '100', '1 000'], rows, [330, 150, 130, 100, 100, 110], row_h=48, size=13,
              note='Las diferencias frecuentes se ven con unas pocas entradas; la que ocurre en una de cien exige cientos, y una prueba con tres ejemplos escritos a mano casi nunca la encuentra. Que no aparezca una diferencia no demuestra equivalencia. Las funciones y la distribución de entradas son del autor.',
              note_kind='coral', foot=EJEC)


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
    rows = [[r["paso"], str(r["interpretaciones"]), p(r["p_acertar_al_azar"], 2)] for r in f]
    return tab('«Calcula la nota final»: interpretaciones coherentes con el texto según las restricciones dadas',
              f'Tabla con siete pasos de precisión de la instrucción «calcula la nota final»: sin restricciones hay {f[0]["interpretaciones"]} interpretaciones y se acierta al azar con {p(f[0]["p_acertar_al_azar"], 2)}; con seis restricciones queda {f[6]["interpretaciones"]}.',
              ['Restricciones añadidas', 'Interpretaciones posibles', 'Acierto al elegir una al azar'], rows, [380, 280, 270], row_h=40, size=13,
              note='Seis dimensiones con tres opciones dan 729 combinaciones; cada restricción divide por tres. Las dimensiones y sus opciones son un ejemplo del autor, y las combinaciones reales dependen de requisitos que no se enumeran tan limpiamente.',
              note_kind='teal', foot='Enumeración exacta del producto cartesiano; no interviene ningún modelo.')


def se464_versiones_en_contexto() -> Fig:
    d = R("e464_distractores")
    items = [('Sin filtrar versiones', d["sin_filtro"], 'coral', p(d["sin_filtro"])), ('Filtrando la versión vigente', d["con_filtro"], 'teal', p(d["con_filtro"]))]
    return bars(f'{d["consultas"]} consultas con documentos de versiones anteriores mezclados en el contexto',
               f'Barras con el porcentaje de consultas en que el primer documento recuperado es el vigente: {p(d["sin_filtro"])} sin filtrar por versión y {p(d["con_filtro"])} filtrando.',
               items, 8.0, 'Los documentos antiguos comparten el vocabulario del vigente y compiten con él por la puntuación; los metadatos de versión resuelven lo que el texto no puede. El 100 % es por construcción, pues se supone la etiqueta de versión correcta, y en la práctica a menudo falta o está mal.',
               label_w=270, width=940, note_kind='gold', foot=SINT)


def se464_reglas_que_chocan() -> Fig:
    d = R("e464_reglas")
    rows = [[str(r["reglas"]), p(r["con_conflicto"])] for r in d["filas"]]
    return tab(f'Archivos de instrucciones sintéticos con reglas «siempre/nunca» sobre {d["claves"]} temas: los que se contradicen',
              f'Tabla con el porcentaje de archivos con al menos una contradicción según el número de reglas: {p(d["filas"][0]["con_conflicto"])} con 5 reglas, {p(d["filas"][1]["con_conflicto"])} con 10, {p(d["filas"][2]["con_conflicto"])} con 20 y {p(d["filas"][3]["con_conflicto"])} con 40.',
              ['Reglas en el archivo', 'Archivos con alguna contradicción'], rows, [380, 450], row_h=44, size=13,
              note='Un detector que compara reglas del mismo tema las encuentra todas, pero solo si las reglas se escriben de forma estructurada; en prosa libre la contradicción pasa desapercibida. Las 500 muestras por tamaño y la elección al azar de tema y polaridad son del autor.',
              note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-465
def se465_tamano_del_conjunto() -> Fig:
    f = R("e465_tamano")["filas"]
    rows = [[str(r["tareas"]), f'{p(r["ic"][0])} – {p(r["ic"][1])}', n(r["ancho_ic_pts"]), p(r["ordena_bien"])] for r in f]
    return tab('Un sistema con 70 % de éxito y otro con 75 %: intervalo de Wilson y probabilidad de ordenarlos bien',
              f'Tabla con el tamaño del conjunto de tareas, el intervalo de Wilson al 95 por ciento para el 70 por ciento de éxito, su ancho y la probabilidad de ordenar bien dos sistemas: con {f[0]["tareas"]} tareas el ancho es {n(f[0]["ancho_ic_pts"])} puntos y se ordenan bien {p(f[0]["ordena_bien"])}; con {f[4]["tareas"]} el ancho es {n(f[4]["ancho_ic_pts"])} y {p(f[4]["ordena_bien"])}.',
              ['Tareas', 'Intervalo al 95 % (70 % observado)', 'Ancho (puntos)', 'Ordena bien 70 % vs 75 %'], rows, [150, 340, 190, 250], row_h=44, size=13,
              note='Con 100 tareas la diferencia de cinco puntos se ordena bien tres de cada cuatro veces; para distinguir cinco puntos con holgura hacen falta cientos. Las tasas de éxito son hipotéticas y las tareas se suponen independientes e igual de difíciles.',
              note_kind='coral', foot=SINT)


def se465_frontera_costo_calidad() -> Fig:
    d = R("e465_frontera")
    rows = [[r["config"], p(r["exito"], 0), n(r["costo_intento"], 3), n(r["latencia_s"]), n(r["costo_por_aceptada"], 2), 'sí' if r["dominada"] else 'no'] for r in d["filas"]]
    return tab('Seis configuraciones sintéticas: éxito, costo por intento, latencia y costo por solución aceptada',
              'Tabla con seis configuraciones de un asistente con su tasa de éxito, costo por intento, latencia, costo por solución aceptada incluyendo una revisión humana de 0,40 y si están dominadas: solo «pequeño + reintento» está dominada; el costo por solución aceptada es mínimo con «mediano + contexto» y casi igual con «grande».',
              ['Configuración', 'Éxito', 'Costo por intento', 'Latencia (s)', 'Costo por aceptada', '¿Dominada?'], rows, [260, 100, 160, 140, 170, 120], row_h=44, size=13,
              note=f'La revisión humana (0,40 por intento) pesa mucho más que el costo del modelo: lo barato por intento sale caro por solución aceptada. Todos los valores, incluida la revisión de {n(d["revision"], 2)}, son supuestos del autor en una unidad arbitraria.',
              note_kind='gold', foot=SINT)


def se465_sesgos_del_juez() -> Fig:
    d = R("e465_juez")
    items = [('Acuerdo con la etiqueta humana', d["acuerdo_con_humano"], 'gold', p(d["acuerdo_con_humano"])),
             ('Mismo veredicto al intercambiar el orden', d["estable_al_intercambiar_orden"], 'coral', p(d["estable_al_intercambiar_orden"])),
             ('Gana la respuesta más larga', d["gana_la_mas_larga"], 'coral', p(d["gana_la_mas_larga"]))]
    return bars(f'Un juez automático sintético con sesgos de posición y de longitud ({d["n"]} comparaciones)',
               f'Barras con tres medidas de un juez automático: acuerda con la etiqueta humana {p(d["acuerdo_con_humano"])}, mantiene el veredicto al intercambiar el orden {p(d["estable_al_intercambiar_orden"])} y gana la respuesta más larga en {p(d["gana_la_mas_larga"])} de las comparaciones, cuando por azar serían 50 por ciento.',
               items, 8.0, 'Un 83 % de acuerdo suena bien y convive con que una cuarta parte de los veredictos cambie solo por el orden de presentación. Los sesgos son parámetros del autor; medir los de un juez real exige comparaciones con orden permutado.',
               label_w=300, width=980, note_kind='coral', foot=SINT)


# ---------------------------------------------------------------- SE-466
def se466_escaner_de_datos() -> Fig:
    d = R("e466_escaner")
    nombres = {"correo": "Correo electrónico", "secreto": "Cadena aleatoria alfanumérica", "secreto_hex": "Cadena aleatoria hexadecimal", "identificador": "Identificador con guion", "limpio": "Texto sin datos sensibles"}
    rows = [[nombres[k], str(v["n"]), str(v["patron"]), str(v["entropia"]), str(v["contexto"]), str(v["las_tres"])] for k, v in d.items()]
    return tab('240 mensajes sintéticos: qué detecta cada regla de un escáner previo al envío',
              'Tabla con cinco clases de mensaje y cuántos detecta cada regla: el patrón de correos e identificadores detecta 40 y 40, la entropía solo las cadenas alfanuméricas, la palabra clave seguida de una cadena larga detecta las dos clases de cadenas, las tres reglas juntas detectan todo lo sensible y no marcan ningún texto limpio, incluidos los hashes de versión.',
              ['Clase', 'Casos', 'Patrón', 'Entropía', 'Contexto', 'Las tres'], rows, [320, 90, 120, 130, 130, 130], row_h=44, size=13,
              note='Cada regla ve una cara; la entropía no puede marcar una cadena hexadecimal porque su entropía máxima es 4 bits, y la regla de contexto depende de la palabra «clave». Las cadenas se generan en tiempo de ejecución; ninguna es un dato real. Los mensajes son plantillas del autor.',
              note_kind='gold', foot=EJEC)


def se466_patrones_inseguros() -> Fig:
    d = R("e466_patrones")
    rows = [[r["tecnica"].capitalize(), str(r["verdaderos"]), str(r["falsos_positivos"]), str(r["omitidos"])] for r in d["filas"]]
    return tab(f'{len(ex.SNIPPETS)} fragmentos de Python ({d["inseguros"]} inseguros): búsqueda de texto frente a recorrido del árbol sintáctico',
              f'Tabla con dos técnicas para encontrar nueve patrones inseguros: la búsqueda de texto acierta {d["filas"][0]["verdaderos"]}, marca {d["filas"][0]["falsos_positivos"]} fragmentos seguros y omite {d["filas"][0]["omitidos"]}; el recorrido del árbol acierta {d["filas"][1]["verdaderos"]}, no marca ninguno seguro y omite {d["filas"][1]["omitidos"]}.',
              ['Técnica', 'Inseguros hallados', 'Falsas alarmas', 'Inseguros omitidos'], rows, [260, 250, 200, 220], row_h=44, size=13,
              note='El árbol evita marcar comentarios y mensajes pero no ve alias como «f = eval»; ninguna de las dos técnicas sustituye a un análisis de flujo de datos. Los fragmentos están escritos por el autor, algunos pensados para engañar a cada técnica.',
              note_kind='coral', foot=EJEC)


def se466_parecido_con_licencia() -> Fig:
    f = R("e466_similitud")["filas"]
    rows = [[r["caso"], p(100 * r["literal"], 0), p(100 * r["normalizada"], 0)] for r in f]
    return tab('Huellas de cinco símbolos: fragmento generado frente a un corpus con licencia',
              f'Tabla con el porcentaje de huellas de cinco símbolos de cada fragmento que aparece en el corpus, comparando símbolos literales y con identificadores normalizados: la copia literal da {p(100 * f[0]["literal"], 0)} y {p(100 * f[0]["normalizada"], 0)}, la copia con nombres cambiados baja a {p(100 * f[1]["literal"], 0)} pero vuelve a {p(100 * f[1]["normalizada"], 0)}, el idioma común da {p(100 * f[2]["literal"], 0)} y la solución independiente {p(100 * f[3]["literal"], 0)} y {p(100 * f[3]["normalizada"], 0)}.',
              ['Fragmento', 'Huellas literales en el corpus', 'Con identificadores normalizados'], rows, [420, 280, 250], row_h=48, size=13,
              note='Cambiar los nombres engaña a la comparación literal pero no a la normalizada; un idioma muy común coincide al 100 % sin ser copia de nadie. Un parecido alto es una señal para investigar y no un veredicto de infracción. El corpus de una función es mínimo y del autor.',
              note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-467
def se467_tres_flujos() -> Fig:
    d = R("e467_flujos")
    rows = [[r["flujo"].capitalize(), n(r["mediana_h"], 2), f'{n(r["ic95"][0], 2)} – {n(r["ic95"][1], 2)}', n(r["total_h"]), str(r["defectos_escapan"])] for r in d["filas"]]
    return tab(f'{d["n"]} tareas sintéticas en tres flujos: horas por tarea y defectos que escapan a la revisión',
              f'Tabla con la mediana de horas por tarea, su intervalo bootstrap al 95 por ciento, las horas totales y los defectos que escapan en tres flujos: manual {n(d["filas"][0]["mediana_h"], 2)} horas y {d["filas"][0]["defectos_escapan"]} defectos, asistido {n(d["filas"][1]["mediana_h"], 2)} y {d["filas"][1]["defectos_escapan"]}, automatizado {n(d["filas"][2]["mediana_h"], 2)} y {d["filas"][2]["defectos_escapan"]}.',
              ['Flujo', 'Mediana (h)', 'IC 95 % (bootstrap)', 'Horas totales', 'Defectos que escapan'], rows, [210, 160, 240, 160, 190], row_h=44, size=13,
              note='Cada paso ahorra tiempo y deja escapar más defectos: no hay un flujo «mejor» sin decidir cuánto vale cada defecto. Todos los tiempos relativos y tasas de defecto son supuestos del autor; no se midió a ninguna persona ni herramienta.',
              note_kind='gold', foot=SINT)


def se467_punto_de_equilibrio() -> Fig:
    d = R("e467_sensibilidad")
    rows = [[p(r["aciertos"], 0), n(r["horas_relativas"], 2), p(r["ahorro"], 0)] for r in d["filas"]]
    return tab('Flujo asistido frente a manual: ahorro de tiempo según la tasa de aciertos del asistente',
              f'Tabla con la tasa de aciertos del asistente, las horas relativas al flujo manual y el ahorro: con 90 por ciento ahorra {p(d["filas"][0]["ahorro"], 0)}, con 50 por ciento no ahorra nada y con 20 por ciento cuesta {p(-d["filas"][4]["ahorro"], 0)} más.',
              ['Aciertos del asistente', 'Horas respecto al manual', 'Ahorro'], rows, [330, 330, 270], row_h=44, size=13,
              note=f'Con generar 35 %, revisar 25 % y rehacer 80 % del tiempo manual, el asistente solo ahorra por encima del {p(d["p_equilibrio"], 0)} de aciertos. Los tres porcentajes son supuestos del autor y se pueden cambiar; la tasa real de aciertos se mide por tipo de tarea.',
              note_kind='coral', foot='Cálculo exacto con la fórmula del texto; sin simulación ni modelo real.')


def se467_diseno_pareado() -> Fig:
    f = R("e467_diseno")["filas"]
    rows = [[str(r["tareas"]), p(r["pareado"], 0), p(r["independiente"], 0)] for r in f]
    return tab('Detectar una diferencia real del 15 % en tiempo: diseño pareado frente a grupos distintos',
              f'Tabla con la probabilidad de detectar una diferencia real del 15 por ciento según el número de tareas: con {f[1]["tareas"]} tareas el diseño pareado la detecta {p(f[1]["pareado"], 0)} y el de grupos distintos {p(f[1]["independiente"], 0)}; con {f[3]["tareas"]} tareas {p(f[3]["pareado"], 0)} y {p(f[3]["independiente"], 0)}.',
              ['Tareas por flujo', 'Mismas tareas en ambos flujos', 'Tareas distintas en cada flujo'], rows, [250, 340, 340], row_h=44, size=13,
              note='La dificultad varía mucho más entre tareas que entre flujos; si cada flujo hace tareas distintas, esa variación tapa el efecto. Hacer las mismas tareas en los dos flujos (con orden alternado) lo revela con una fracción de las tareas. La variación de tareas es lognormal del autor.',
              note_kind='teal', foot=SINT)


# ---------------------------------------------------------------- SE-468
def se468_bitacora_encadenada() -> Fig:
    d = R("e468_bitacora")
    rows = [['Editar el texto de la entrada 3', f'entrada {d["editar_entrada_3_detectada_en"]}'], ['Borrar la entrada 3', f'entrada {d["borrar_entrada_3_detectada_en"]}'],
            ['Intercambiar las entradas 2 y 3', f'entrada {d["intercambiar_2_y_3_detectada_en"]}'],
            ['Editar la 3 y recalcular todos los hashes siguientes', 'no se detecta (verifica sin error)'],
            ['Lo mismo, con el último hash guardado fuera de la bitácora', 'el último hash no coincide: se detecta']]
    return tab('Bitácora de seis pasos encadenada por hash: qué manipulaciones detecta la verificación',
              f'Tabla con cinco manipulaciones de una bitácora de seis entradas encadenadas por hash: editar, borrar o intercambiar entradas se detecta en las entradas {d["editar_entrada_3_detectada_en"]}, {d["borrar_entrada_3_detectada_en"]} y {d["intercambiar_2_y_3_detectada_en"]}; recalcular los hashes siguientes no se detecta salvo que el último hash se haya guardado fuera.',
              ['Manipulación', 'Resultado de la verificación'], rows, [520, 420], row_h=48, size=13,
              note='El encadenado detecta alteraciones torpes y no a quien tiene acceso para reescribir la cola: hace falta un ancla externa (el último hash en otro sistema, una firma). Es evidencia de integridad, no de que el contenido sea cierto.',
              note_kind='gold', foot=EJEC)


def se468_compuertas() -> Fig:
    d = R("e468_compuertas")
    f = d["filas"]
    rows = [[r["compuertas"], f'{r["defectos_en_produccion"]} de {r["de"]:,}'.replace(",", "."), p(100 * r["defectos_en_produccion"] / r["de"])] for r in f]
    return tab('Cambios asistidos sintéticos (20 % con defecto): defectos que llegan a producción según las compuertas',
              f'Tabla con cinco conjuntos de compuertas y los defectos que llegan a producción de 10.000 cambios: sin compuertas {f[0]["defectos_en_produccion"]}, solo pruebas {f[1]["defectos_en_produccion"]}, pruebas y análisis {f[2]["defectos_en_produccion"]}, con revisión humana {f[3]["defectos_en_produccion"]} y con las cuatro {f[4]["defectos_en_produccion"]}.',
              ['Compuertas', 'Defectos en producción', 'Fracción de los cambios'], rows, [420, 300, 210], row_h=44, size=13,
              note=f'Cada compuerta quita una fracción y ninguna llega a cero; además la revisión humana pierde eficacia con el tamaño: detecta {p(d["fatiga"][0]["p_detectar"])} con 20 líneas y {p(d["fatiga"][3]["p_detectar"])} con 1.000. Las probabilidades de detección y su independencia son supuestos del autor.',
              note_kind='coral', foot=SINT)


def se468_reversion_limpia() -> Fig:
    f = R("e468_reversion")["filas"]
    rows = [[str(r["ediciones_posteriores"]), p(r["reversion_limpia"])] for r in f]
    return tab('Revertir un cambio de 40 líneas (4 bloques de 10) en un archivo de 400 tras k ediciones posteriores',
              f'Tabla con la probabilidad de poder revertir el cambio sin conflicto según las ediciones posteriores: {p(f[0]["reversion_limpia"])} sin ediciones, {p(f[1]["reversion_limpia"])} con 5, {p(f[2]["reversion_limpia"])} con 20 y {p(f[3]["reversion_limpia"])} con 60.',
              ['Ediciones posteriores', 'Reversión limpia'], rows, [400, 400], row_h=44, size=13,
              note='La ventana para deshacer un cambio sin conflictos se cierra rápido: cuanto más tarda la revisión, más probable es que revertir sea ya otro cambio. Las ediciones al azar sobre líneas uniformes son una simplificación del autor; los cambios reales se concentran.',
              note_kind='gold', foot=SINT)


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
