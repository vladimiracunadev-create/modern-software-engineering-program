"""Figures for SE-547 to SE-552 (development methodologies: contracts, specification drift, evaluation gates, a real Git history, five methodologies on one change, and a team policy; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, scatter, stacked_bars
from figures_part45_a import EJEC, LAB, bars, flow, mapa

SINT = "Simulación con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
GIT = "Historiales de Git creados de verdad en un directorio temporal y ejecutados en Windows 11 y Ubuntu (WSL2) con los mismos resultados."


# ---------------------------------------------------------------- SE-547
def se487_cambios_del_proveedor() -> Fig:
    cambios = [("C01 añadir priority", 0, 1, 1, 0), ("C02 renombrar due por due_at", 1, 1, 1, 1), ("C03 due pasa a texto ISO", 1, 1, 1, 1), ("C04 eliminar student", 1, 1, 1, 1),
               ("C05 submitted pasa a «yes» o «no»", 1, 1, 1, 1), ("C06 añadir course", 0, 1, 1, 0), ("C07 reordenar los campos", 0, 0, 0, 0), ("C08 due pasa de entero a decimal", 0, 0, 1, 0),
               ("C09 id pasa de texto a entero", 1, 1, 1, 1), ("C10 añadir status con valor nuevo", 0, 1, 1, 0), ("C11 eliminar submitted", 1, 1, 1, 1), ("C12 envolver la lista en data", 1, 1, 1, 1)]
    return heatmap(
        "Doce cambios de un proveedor de entregas y tres formas de detectar los que rompen a un consumidor",
        "Mapa de calor de doce cambios del proveedor, siete de los cuales rompen al cliente de avisos: la instantánea de la respuesta alerta en 10 cambios y se equivoca en 3 de los 5 inocuos, la diferencia de esquema alerta en 11 y se equivoca en 4 de los 5, y el contrato del consumidor alerta solo en los 7 que rompen y no se equivoca en ninguno de los 5.",
        [f"{c[0]} ({'rompe' if c[1] else 'inocuo'})" for c in cambios],
        ["Instantánea", "Diferencia de esquema", "Contrato del consumidor"],
        [[c[2], c[3], c[4]] for c in cambios],
        unit="Alerta", scale="coral", vmin=0, vmax=1, cell_fmt=lambda v: "alerta" if v else "—", cell_h=34, label_w=380,
        note='Las tres detectan los 7 cambios que rompen; la diferencia está en las falsas alarmas: 3, 4 y 0 de 5. El contrato del consumidor declara solo los campos y tipos que el cliente lee. Doce cambios escritos por el autor sobre un cliente de cuatro campos.', note_kind='teal', foot=EJEC)


def se487_asercion_y_optimizacion() -> Fig:
    return mapa(
        "La misma precondición ejecutada con y sin la opción de optimización de Python",
        "Diagrama de dos ejecuciones reales de la misma función con una entrega ya vencida: en modo normal la aserción de la precondición se evalúa y el programa informa de que el contrato se violó; con la opción -O la aserción desaparece y la función devuelve menos diez, un valor sin sentido.",
        [("python (normal)", "contrato violado: precondición: la entrega no ha vencido", "teal", "la aserción se evalúa y detiene el cálculo"),
         ("python -O", "resultado -10", "coral", "la aserción desaparece y el cálculo devuelve un valor sin sentido")],
        note='Una precondición escrita con assert no es un contrato si el despliegue puede ejecutarse con -O o PYTHONOPTIMIZE. Un contrato que debe valer en producción se escribe como una comprobación explícita que lanza una excepción.', note_kind='coral', foot='Dos procesos de Python lanzados con subprocess; mismo resultado en Windows 11 (CPython 3.12.9) y Ubuntu (3.12.3).', left_w=200, mid_w=330)


def se487_falsas_alarmas() -> Fig:
    return bars('Falsas alarmas de cada detector sobre los 5 cambios del proveedor que no rompen al cliente',
                'Gráfico de barras con las falsas alarmas sobre cinco cambios inocuos: la instantánea de la respuesta emite 3, la diferencia de esquema 4 y el contrato del consumidor 0; los tres detectan los siete cambios que sí rompen.',
                [('Instantánea de la respuesta', 3, 'coral', '3 de 5'), ('Diferencia de esquema', 4, 'coral', '4 de 5'), ('Contrato del consumidor', 0, 'teal', '0 de 5')],
                scale=120, note='Una alerta falsa recurrente enseña a ignorar las alertas: el costo de una instantánea no está en el cambio que no detecta sino en el que empieza a descartarse sin leer. El contrato del consumidor exige además mantener qué campos lee cada cliente.',
                note_kind='gold', foot=EJEC, label_w=300)


# ---------------------------------------------------------------- SE-548
def se488_derivas_inyectadas() -> Fig:
    return stacked_bars(
        "Diez derivas entre especificación, código y pruebas inyectadas y lo que ve un comprobador mecánico",
        "Barra apilada de diez derivas inyectadas: el comprobador mecánico detecta ocho por completo (reglas sin código, sin prueba o inexistentes, umbrales distintos, código editado sin tocar la especificación y archivo generado editado a mano), detecta una solo de lado (el cambio de significado de una regla aparece como archivo generado desactualizado) y no detecta una (el cambio de menor o igual a menor estricto dentro del código).",
        ["Derivas inyectadas (10)"],
        [("Detectadas", [8], "teal"), ("Detectada solo de lado", [1], "gold"), ("No detectada", [1], "coral")],
        unit="Derivas", horizontal=True, label_w=220, plot_h=120,
        note='Detecta 9 de 10, y la décima solo de lado: avisa de que el archivo generado quedó viejo, no de que el significado cambió. Lo que no ve es la semántica de una expresión sin anclaje en la especificación. Las diez derivas y el comprobador son del autor.', note_kind='gold', foot=EJEC)


def se488_tres_niveles() -> Fig:
    return flow('Tres niveles de SDD según el papel que conserva la especificación',
                'Diagrama con tres filas de dos cajas: en spec-first la especificación guía la primera construcción y después puede quedar atrás; en spec-anchored la especificación se mantiene viva y comprobaciones mecánicas la ligan al código y a las pruebas; en spec-as-source la especificación es la fuente y el código se genera de ella sin edición manual.',
                [[('SPEC-FIRST\nLa especificación guía la primera construcción', 'plain'), ('Después puede quedar atrás: deriva sin aviso', 'coral')],
                 [('SPEC-ANCHORED\nLa especificación se mantiene viva', 'teal'), ('Comprobaciones ligan reglas, código y pruebas', 'teal')],
                 [('SPEC-AS-SOURCE\nLa especificación es la fuente', 'gold'), ('El código se genera; editarlo a mano se detecta', 'gold')]],
                note='Los tres niveles son una gradación del compromiso con mantener la especificación, no tres productos. Cuanto más alto el nivel, menos deriva y más rigidez: lo que la especificación no puede expresar no puede construirse.',
                note_kind='teal', box_h=70)


def se488_que_ve_y_que_no() -> Fig:
    return mapa(
        "Qué puede comprobar una máquina entre una especificación y su código, y qué no",
        "Diagrama de cuatro familias de comprobación entre una especificación y su código: la estructura de identificadores se comprueba de forma exacta, los valores declarados en forma legible por máquina se comparan con una lectura del árbol sintáctico, el código cambiado sin que cambie la especificación se detecta con la lista de archivos, y el significado de una condición distinta no se comprueba y exige una prueba o una persona.",
        [("Estructura: identificadores de reglas, citas en código y en pruebas", "Sí, de forma exacta", "teal", "Que una cita exista no prueba que el código cumpla la regla"),
         ("Valores declarados: umbrales y constantes comparables", "Sí, con una lectura del árbol sintáctico", "teal", "Solo valores que la especificación declara en forma legible por máquina"),
         ("Quién cambió qué: código sin especificación", "Sí, con la lista de archivos del cambio", "teal", "Un cambio trivial y uno de comportamiento valen lo mismo"),
         ("Significado: una comparación o una condición distinta", "No", "coral", "Exige una prueba que el cambio rompa o la lectura de una persona")],
        note='La especificación pagada con comprobaciones mecánicas gana lo que se puede enunciar como estructura; el significado sigue exigiendo pruebas ejecutables que lo enuncien.', note_kind='gold', foot='')


# ---------------------------------------------------------------- SE-549
def se489_tamano_del_conjunto() -> Fig:
    xs = [20, 50, 100, 400, 1600]
    return line_chart(
        "Una versión con 5 puntos menos de precisión pasa la puerta: según casos y repeticiones por evaluación",
        "Líneas en escala logarítmica con el porcentaje de 4 000 simulaciones en que la puerta de release deja pasar la regresión de 5 puntos y en que rechaza la versión sana, según los casos: con una corrida pasa la regresión 41,9, 31,1, 28,0, 12,0 y 0,6 por ciento con 20, 50, 100, 400 y 1 600 casos y rechaza la sana 36,0, 33,7, 22,4, 7,3 y 0,3; con tres corridas por caso las cifras bajan, con 400 casos a 1,5 y 0,7.",
        [("Pasa la regresión (1 corrida)", list(zip(xs, [41.9, 31.1, 28.0, 12.0, 0.6])), "coral"),
         ("Rechaza la sana (1 corrida)", list(zip(xs, [36.0, 33.7, 22.4, 7.3, 0.3])), "gold"),
         ("Pasa la regresión (3 corridas)", list(zip(xs, [31.6, 23.7, 13.5, 1.5, 0.0])), "navy"),
         ("Rechaza la sana (3 corridas)", list(zip(xs, [29.6, 16.8, 11.3, 0.7, 0.0])), "teal")],
        x_label="Casos del conjunto de evaluación", y_label="Simulaciones (%)", log_x=True, x_ticks=[(x, f"{x:,}".replace(",", " ")) for x in xs], decimals=1, point_labels="last",
        note='Con 100 casos y una corrida, más de una de cada cuatro regresiones de 5 puntos se cuela y más de una de cada cinco versiones sanas se rechaza. Repetir tres veces cada caso ayuda, pero la reducción grande viene de más casos. Precisiones, umbral y modelo de azar son supuestos del autor.', note_kind='coral', foot=SINT)


def se489_bucle_de_evaluacion() -> Fig:
    return flow('El bucle de desarrollo guiado por evaluaciones',
                'Diagrama de seis cajas en dos filas: definir los casos y el criterio de aceptación, fijar una línea base, hacer un cambio, ejecutar la evaluación varias veces, comparar con el umbral y la variación y decidir entre publicar, retener o añadir casos.',
                [[('Casos y criterio de aceptación', 'gold'), ('Línea base medida con su variación', 'teal'), ('Cambio de prompt, modelo o código', 'plain')],
                 [('Evaluación repetida varias veces', 'teal'), ('Comparar con umbral y con la variación', 'coral'), ('Publicar, retener o añadir casos', 'navy')]],
                note='Una evaluación es un instrumento de medida con ruido. Sin línea base y sin variación, una diferencia de dos puntos es una opinión, no un resultado.',
                note_kind='gold', foot=SINT, box_h=84)


def se489_regresion_concentrada() -> Fig:
    return grouped_bars(
        "Regresión concentrada en los casos difíciles: qué conjunto de 100 casos la ve",
        "Barras agrupadas con el porcentaje de veces que una puerta deja pasar la regresión y rechaza la versión sana: una muestra al azar de 100 casos, con 10 por ciento difíciles, deja pasar la regresión 72,8 por ciento de las veces y rechaza la sana 4,4; un conjunto de 100 casos solo difíciles no deja pasar ninguna regresión; la misma versión sobre los mismos 100 casos varía con desviación 0,037 y rango de 0,72 a 0,95.",
        ["Muestra al azar, 100 casos (10 % difíciles)", "Solo casos difíciles, 100 casos"],
        [("Pasa la regresión", [72.8, 0.0], "coral"), ("Rechaza la sana", [4.4, 0.0], "gold")],
        unit="Veces que ocurre (%)", decimals=1,
        note='Un conjunto pequeño y curado en lo difícil detecta una regresión que una muestra grande al azar no ve. Al revés, la misma versión puede variar 23 puntos entre corridas con 100 casos: una sola corrida no mide.', note_kind='gold', foot=SINT)


# ---------------------------------------------------------------- SE-550
def se490_dos_historiales() -> Fig:
    return grouped_bars(
        "Dos historiales de Git reales evaluados contra tres reglas del flujo ODD: el commit más grande",
        "Barras con las líneas del commit más grande de dos historiales de Git reales: el ordenado, con documento de tarea primero y un tramo rojo seguido de uno verde, tiene 13 líneas y el comprobador no halla nada; el desordenado, con todo el código en un commit y el documento después, tiene 463 líneas y incumple las tres reglas, con el límite de 400.",
        ["Historial A (ordenado)", "Historial B (desordenado)"],
        [("Líneas del commit mayor", [13, 463], "teal")],
        unit="Líneas del commit más grande", ref_lines=[(400, "límite de 400 líneas")],
        note='El comprobador ejecuta las pruebas de cada commit para saber si estaba en rojo o en verde. Mira orden, tamaño y estado de las pruebas; no puede saber si el documento de tarea describe la realidad ni si 400 líneas es el límite adecuado.', note_kind='teal', foot=GIT)


def se490_flujo_odd() -> Fig:
    return flow('El flujo ODD de un cambio sustancial, de la autorización al commit',
                'Diagrama de seis cajas en dos filas: primero la autorización, porque explicar e investigar son solo lectura; un documento de tarea con alcance, tareas, evidencia y siguiente paso; una prueba roja; el código mínimo en verde; el refactor; y commits pequeños, con push, pull request y merge como decisiones aparte.',
                [[('Autorización primero: explorar es solo lectura', 'gold'), ('Documento de tarea: alcance, tareas, evidencia, siguiente paso', 'teal'), ('ROJO: una prueba determinista', 'coral')],
                 [('VERDE: el código mínimo', 'teal'), ('REFACTOR con todo en verde', 'plain'), ('Commits pequeños; push, PR y merge son decisiones aparte', 'navy')]],
                note='Los pasos descritos proceden de la documentación del proyecto que define el flujo y no de un estudio independiente: la clase los enseña como una descripción de un flujo concreto, con su evidencia declarada y sus límites.',
                note_kind='gold', foot='', box_h=96)


def se490_que_ve_el_comprobador() -> Fig:
    return mapa(
        "Qué comprueba la máquina del flujo ODD y qué solo puede juzgar una persona",
        "Diagrama de cuatro aspectos del flujo ODD: el orden entre el documento y el primer código se comprueba con el historial, el tamaño de cada commit con la estadística numérica de Git, el estado de las pruebas ejecutándolas en cada commit, y que el documento sea cierto y sirva para retomar el trabajo no lo puede comprobar una máquina.",
        [("Orden: el documento existe antes del primer código", "Sí, con el historial", "teal", "Un documento vacío cumple la regla"),
         ("Tamaño: líneas por commit", "Sí, con numstat", "teal", "Las líneas generadas o movidas cuentan igual que las escritas"),
         ("Estado de las pruebas en cada commit", "Sí, ejecutándolas", "teal", "Una prueba que no afirma nada pone el commit en verde"),
         ("Que el documento sea cierto y útil para retomar", "No", "coral", "Solo una persona al retomar lo sabe")],
        note='Comprobar la forma del flujo es barato y ayuda; comprobar su fondo exige que alguien retome el trabajo con solo el documento y diga si pudo.', note_kind='gold', foot='')


# ---------------------------------------------------------------- SE-551
def se491_cinco_metodologias() -> Fig:
    return grouped_bars(
        "El mismo cambio, silenciar un curso, con cinco metodologías: siete silencios mal hechos que mata cada una",
        "Barras horizontales con los mutantes del silencio que mata cada metodología de siete: dos pruebas de TDD con 9 líneas matan 6, tres escenarios de BDD con 15 líneas matan 6, una tabla de ejemplos de ATDD con 17 líneas mata 5, un contrato con 400 estados con 15 líneas mata 3 y un modelo ejecutable de SDD con 17 líneas mata los 7.",
        ["TDD: dos pruebas (9 líneas)", "BDD: tres escenarios (15)", "ATDD: tabla de ejemplos (17)", "Contrato con 400 estados (15)", "SDD: modelo ejecutable (17)"],
        [("Mutantes que mata", [6, 6, 5, 3, 7], "teal")],
        unit="Mutantes del silencio que mata (de 7)", horizontal=True, label_w=290, ref_lines=[(7, "7")],
        note='La unión de las cinco mata los 7 mutantes del silencio, pero el único método que mata los siete solo es el modelo ejecutable, que es también el que exige escribir de nuevo la regla. Líneas y tiempos son del experimento; la comparación de esfuerzo humano no se midió.', note_kind='gold', foot=LAB)


def se491_silencios_que_matan() -> Fig:
    return bars('Silencios mal hechos que mata cada metodología, de 7',
                'Gráfico de barras con los siete mutantes del silencio de un curso que mata cada metodología: dos pruebas de TDD matan 6, tres escenarios de BDD matan 6, la tabla de ejemplos de ATDD mata 5, el contrato con 400 estados mata 3 y el modelo ejecutable de SDD mata 7.',
                [('TDD (dos pruebas)', 6, 'gold', '6'), ('BDD (tres escenarios)', 6, 'gold', '6'), ('ATDD (tabla de ejemplos)', 5, 'gold', '5'), ('Contrato (400 estados)', 3, 'coral', '3'), ('SDD (modelo ejecutable)', 7, 'teal', '7')],
                scale=70, note='La barra más corta no indica la peor metodología: el contrato comprueba propiedades, no valores concretos, y ese es su papel. Indica qué clase de error deja ver y cuál deja pasar.',
                note_kind='gold', foot=LAB, label_w=300)


def se491_lo_que_deja_vivo() -> Fig:
    return heatmap(
        "Qué silencios mal hechos deja vivos cada metodología",
        "Mapa de calor con los mutantes del silencio que deja vivos cada metodología: TDD y BDD dejan vivo S4, que silencia el curso para todas las personas; ATDD deja vivos S3 y S4; el contrato deja vivos S2, S3, S4 y S7; el modelo ejecutable no deja ninguno.",
        ["TDD y BDD", "ATDD", "Contrato", "SDD (modelo)"],
        ["S2", "S3", "S4", "S7"],
        [[0, 0, 1, 0], [0, 1, 1, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
        unit="Mutante vivo", scale="coral", vmin=0, vmax=1, cell_fmt=lambda v: "vive" if v else "muerto", cell_h=50, label_w=170,
        note='En todos los casos la causa es una dimensión que el artefacto no varía o una regla que no repite. Añadir un ejemplo con dos personas y un curso común mata S4 en TDD, BDD y ATDD.', note_kind='coral', foot=LAB)


# ---------------------------------------------------------------- SE-552
def se492_politicas() -> Fig:
    return scatter(
        "Cinco políticas aplicadas a 300 cambios sintéticos: costo frente a impacto escapado",
        "Puntos con el costo en horas y el impacto escapado de cinco políticas sobre 300 cambios sintéticos: no hacer nada cuesta 0 y deja escapar 1 157; TDD en todo cuesta 232 y deja 745; todo en todo cuesta 1 240 y deja 489; por riesgo cuesta 482 y deja 532; por riesgo y ambigüedad cuesta 485 y deja 499.",
        [("Políticas", [(0, 1157, "Nada", "r"), (232, 745, "TDD en todo", "r"), (1240, 489, "Todo en todo", "t"), (482, 532, "Por riesgo", "l"), (485, 499, "Por riesgo y ambigüedad", "r")], "teal")],
        x_label="Costo (horas)", y_label="Impacto escapado", decimals=0, y_zero=True,
        note='Aplicarlo todo a todo es la política más cara y deja menos impacto, pero evita 0,54 por hora frente a 1,77 de TDD en todo. Costos, riesgos y fracción con reglas son supuestos del autor; solo las tasas de detección vienen del experimento de SE-541.', note_kind='gold', foot=SINT)


def se492_arbol_de_politica() -> Fig:
    return flow('Una política de equipo como reglas que dependen del cambio',
                'Diagrama con tres reglas de política: un cambio de bajo riesgo exige TDD; uno de riesgo medio añade contratos; uno de riesgo alto añade modelo ejecutable y, si es ambiguo, conversación con ejemplos; un cambio sin reglas deterministas no usa estas prácticas y se evalúa de otra forma.',
                [[('Riesgo bajo: TDD', 'teal'), ('Riesgo medio: TDD y contratos', 'gold'), ('Riesgo alto: TDD, contratos y modelo ejecutable', 'coral')],
                 [('Ambiguo y no bajo: añadir ejemplos con negocio (BDD o ATDD)', 'gold'), ('Sin reglas deterministas: evaluación (EDD) y revisión humana', 'plain')]],
                note='La política es una tabla de entradas y evidencias, revisable cada trimestre con los defectos que escaparon. Lo que no se registra no puede corregirla.',
                note_kind='teal', foot='', box_h=96)


def se492_tasas_de_deteccion() -> Fig:
    return bars('Tasa de detección de cada práctica medida en el laboratorio, sobre 18 mutantes',
                'Gráfico de barras con la fracción de mutantes no equivalentes que mata cada oráculo del laboratorio y que se usa como tasa de detección en la política: caso feliz 0,39, ocho pruebas de TDD 0,83, escenarios de aceptación 0,94, contrato con 400 estados 0,72 y modelo de referencia 1,00.',
                [('Caso feliz único', 0.39, 'coral', '0,39'), ('Ocho pruebas (TDD)', 0.83, 'gold', '0,83'), ('Escenarios de aceptación', 0.94, 'gold', '0,94'), ('Contrato (400 estados)', 0.72, 'gold', '0,72'), ('Modelo de referencia', 1.0, 'teal', '1,00')],
                scale=500, note='Son tasas sobre 18 mutantes de una función de 20 líneas: sirven para anclar la simulación, no para predecir la detección en un sistema real. La política cambia mucho si se supone otra.',
                note_kind='coral', foot=LAB, label_w=300)


FIGURES = {
    "se-547-cambios-del-proveedor.svg": se487_cambios_del_proveedor,
    "se-547-asercion-y-optimizacion.svg": se487_asercion_y_optimizacion,
    "se-547-falsas-alarmas.svg": se487_falsas_alarmas,
    "se-548-derivas-inyectadas.svg": se488_derivas_inyectadas,
    "se-548-tres-niveles.svg": se488_tres_niveles,
    "se-548-que-ve-y-que-no.svg": se488_que_ve_y_que_no,
    "se-549-tamano-del-conjunto.svg": se489_tamano_del_conjunto,
    "se-549-bucle-de-evaluacion.svg": se489_bucle_de_evaluacion,
    "se-549-regresion-concentrada.svg": se489_regresion_concentrada,
    "se-550-dos-historiales.svg": se490_dos_historiales,
    "se-550-flujo-odd.svg": se490_flujo_odd,
    "se-550-que-ve-el-comprobador.svg": se490_que_ve_el_comprobador,
    "se-551-cinco-metodologias.svg": se491_cinco_metodologias,
    "se-551-silencios-que-matan.svg": se491_silencios_que_matan,
    "se-551-lo-que-deja-vivo.svg": se491_lo_que_deja_vivo,
    "se-552-politicas.svg": se492_politicas,
    "se-552-arbol-de-politica.svg": se492_arbol_de_politica,
    "se-552-tasas-de-deteccion.svg": se492_tasas_de_deteccion,
}
