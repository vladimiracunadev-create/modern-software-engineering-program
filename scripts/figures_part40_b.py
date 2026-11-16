"""Figures for SE-487 to SE-492 (development methodologies: contracts, specification drift, evaluation gates, a real Git history, five methodologies on one change, and a team policy; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab
from figures_part40_a import EJEC, LAB, bars, flow

SINT = "Simulación con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
GIT = "Historiales de Git creados de verdad en un directorio temporal y ejecutados en Windows 11 y Ubuntu (WSL2) con los mismos resultados."


# ---------------------------------------------------------------- SE-487
def se487_cambios_del_proveedor() -> Fig:
    rows = [['C01 añadir priority', 'no', 'alerta', 'alerta', '—'], ['C02 renombrar due por due_at', 'sí', 'alerta', 'alerta', 'alerta'], ['C03 due pasa a texto ISO', 'sí', 'alerta', 'alerta', 'alerta'],
            ['C04 eliminar student', 'sí', 'alerta', 'alerta', 'alerta'], ['C05 submitted pasa a «yes» o «no»', 'sí', 'alerta', 'alerta', 'alerta'], ['C06 añadir course', 'no', 'alerta', 'alerta', '—'],
            ['C07 reordenar los campos', 'no', '—', '—', '—'], ['C08 due pasa de entero a decimal', 'no', '—', 'alerta', '—'], ['C09 id pasa de texto a entero', 'sí', 'alerta', 'alerta', 'alerta'],
            ['C10 añadir status con valor nuevo', 'no', 'alerta', 'alerta', '—'], ['C11 eliminar submitted', 'sí', 'alerta', 'alerta', 'alerta'], ['C12 envolver la lista en data', 'sí', 'alerta', 'alerta', 'alerta']]
    return tab('Doce cambios de un proveedor de entregas y tres formas de detectar los que rompen a un consumidor',
               'Tabla con doce cambios del proveedor de entregas, siete de los cuales rompen al cliente de avisos: la instantánea de la respuesta alerta en 10 cambios y se equivoca en 3 de los 5 inocuos, la diferencia de esquema alerta en 11 y se equivoca en 4 de los 5, y el contrato del consumidor alerta solo en los 7 que rompen y no se equivoca en ninguno de los 5.',
               ['Cambio del proveedor', 'Rompe al cliente', 'Instantánea', 'Diferencia de esquema', 'Contrato del consumidor'], rows, [330, 140, 150, 180, 190], row_h=40, size=13,
               note='Las tres detectan los 7 cambios que rompen; la diferencia está en las falsas alarmas: 3, 4 y 0 de 5. El contrato del consumidor declara solo los campos y tipos que el cliente lee. Doce cambios escritos por el autor sobre un cliente de cuatro campos.',
               note_kind='teal', foot=EJEC)


def se487_asercion_y_optimizacion() -> Fig:
    rows = [['python (normal)', 'contrato violado: precondición: la entrega no ha vencido', 'la aserción se evalúa y detiene el cálculo'], ['python -O', 'resultado -10', 'la aserción desaparece y el cálculo devuelve un valor sin sentido']]
    return tab('La misma precondición ejecutada con y sin la opción de optimización de Python',
               'Tabla con la misma función y la misma llamada con una entrega ya vencida ejecutadas en dos procesos reales de Python: en modo normal la aserción de la precondición se evalúa y el programa informa de que el contrato se violó, y con la opción de optimización la aserción desaparece y la función devuelve menos diez.',
               ['Ejecución', 'Salida observada', 'Qué ocurrió'], rows, [200, 430, 340], row_h=70, size=13,
               note='Una precondición escrita con assert no es un contrato si el despliegue puede ejecutarse con -O o PYTHONOPTIMIZE. Un contrato que debe valer en producción se escribe como una comprobación explícita que lanza una excepción.',
               note_kind='coral', foot='Dos procesos de Python lanzados con subprocess; mismo resultado en Windows 11 (CPython 3.12.9) y Ubuntu (3.12.3).')


def se487_falsas_alarmas() -> Fig:
    return bars('Falsas alarmas de cada detector sobre los 5 cambios del proveedor que no rompen al cliente',
                'Gráfico de barras con las falsas alarmas sobre cinco cambios inocuos: la instantánea de la respuesta emite 3, la diferencia de esquema 4 y el contrato del consumidor 0; los tres detectan los siete cambios que sí rompen.',
                [('Instantánea de la respuesta', 3, 'coral', '3 de 5'), ('Diferencia de esquema', 4, 'coral', '4 de 5'), ('Contrato del consumidor', 0, 'teal', '0 de 5')],
                scale=120, note='Una alerta falsa recurrente enseña a ignorar las alertas: el costo de una instantánea no está en el cambio que no detecta sino en el que empieza a descartarse sin leer. El contrato del consumidor exige además mantener qué campos lee cada cliente.',
                note_kind='gold', foot=EJEC, label_w=300)


# ---------------------------------------------------------------- SE-488
def se488_derivas_inyectadas() -> Fig:
    rows = [['D1 una regla se quita de la especificación y sigue en el código', 'sí'], ['D2 una regla nueva sin código', 'sí'], ['D3 una regla nueva sin prueba', 'sí'], ['D4 una prueba cita una regla inexistente', 'sí'],
            ['D5 el umbral del código se cambia a mano', 'sí'], ['D6 el umbral cambia en la especificación y no en el código', 'sí'], ['D7 se edita el código sin tocar la especificación', 'sí'],
            ['D8 se edita a mano el archivo generado', 'sí'], ['D9 la condición cambia de <= a < dentro del código', 'NO'], ['D10 una regla cambia de significado en el texto', 'sí, solo como «generado desactualizado»']]
    return tab('Diez derivas entre especificación, código y pruebas inyectadas y lo que ve un comprobador mecánico',
               'Tabla con diez derivas inyectadas entre una especificación, el código y las pruebas: el comprobador mecánico detecta nueve, entre ellas reglas sin código, sin prueba o inexistentes, umbrales distintos, código editado sin tocar la especificación y archivo generado editado a mano, y no detecta el cambio de una comparación menor o igual por menor estricto; el cambio de significado de una regla solo aparece como archivo generado desactualizado.',
               ['Deriva inyectada', '¿La ve el comprobador?'], rows, [660, 310], row_h=48, size=13,
               note='Detecta 9 de 10, y la décima solo de lado: avisa de que el archivo generado quedó viejo, no de que el significado cambió. Lo que no ve es la semántica de una expresión sin anclaje en la especificación. Las diez derivas y el comprobador son del autor.',
               note_kind='gold', foot=EJEC)


def se488_tres_niveles() -> Fig:
    return flow('Tres niveles de SDD según el papel que conserva la especificación',
                'Diagrama con tres filas de dos cajas: en spec-first la especificación guía la primera construcción y después puede quedar atrás; en spec-anchored la especificación se mantiene viva y comprobaciones mecánicas la ligan al código y a las pruebas; en spec-as-source la especificación es la fuente y el código se genera de ella sin edición manual.',
                [[('SPEC-FIRST\nLa especificación guía la primera construcción', 'plain'), ('Después puede quedar atrás: deriva sin aviso', 'coral')],
                 [('SPEC-ANCHORED\nLa especificación se mantiene viva', 'teal'), ('Comprobaciones ligan reglas, código y pruebas', 'teal')],
                 [('SPEC-AS-SOURCE\nLa especificación es la fuente', 'gold'), ('El código se genera; editarlo a mano se detecta', 'gold')]],
                note='Los tres niveles son una gradación del compromiso con mantener la especificación, no tres productos. Cuanto más alto el nivel, menos deriva y más rigidez: lo que la especificación no puede expresar no puede construirse.',
                note_kind='teal', box_h=70)


def se488_que_ve_y_que_no() -> Fig:
    rows = [['Estructura: identificadores de reglas, citas en código y en pruebas', 'Sí, de forma exacta', 'Que una cita exista no prueba que el código cumpla la regla'],
            ['Valores declarados: umbrales y constantes comparables', 'Sí, con una lectura del árbol sintáctico', 'Solo valores que la especificación declara en forma legible por máquina'],
            ['Quién cambió qué: código sin especificación', 'Sí, con la lista de archivos del cambio', 'Un cambio trivial y uno de comportamiento valen lo mismo'],
            ['Significado: una comparación o una condición distinta', 'No', 'Exige una prueba que el cambio rompa o la lectura de una persona']]
    return tab('Qué puede comprobar una máquina entre una especificación y su código, y qué no',
               'Tabla de cuatro familias de comprobación entre una especificación y su código: la estructura de identificadores se comprueba de forma exacta, los valores declarados en forma legible por máquina se comparan con una lectura del árbol sintáctico, la ausencia de cambios de especificación junto a cambios de código se detecta con la lista de archivos, y el significado de una condición distinta no se comprueba y exige una prueba o una persona.',
               ['Qué se comprueba', '¿Lo ve la máquina?', 'Límite'], rows, [370, 250, 350], row_h=76, size=13,
               note='La especificación pagada con comprobaciones mecánicas gana lo que se puede enunciar como estructura; el significado sigue exigiendo pruebas ejecutables que lo enuncien.',
               note_kind='gold', foot='')


# ---------------------------------------------------------------- SE-489
def se489_tamano_del_conjunto() -> Fig:
    rows = [['20', '41,9 %', '36,0 %', '31,6 %', '29,6 %'], ['50', '31,1 %', '33,7 %', '23,7 %', '16,8 %'], ['100', '28,0 %', '22,4 %', '13,5 %', '11,3 %'],
            ['400', '12,0 %', '7,3 %', '1,5 %', '0,7 %'], ['1 600', '0,6 %', '0,3 %', '0,0 %', '0,0 %']]
    return tab('Una versión con 5 puntos menos de precisión pasa la puerta: según casos y repeticiones por evaluación',
               'Tabla con una puerta de release de umbral 0,825 sobre una versión sana de precisión 0,85 y una versión con regresión de 0,80, con 4000 simulaciones por celda: con 20 casos y una corrida la puerta deja pasar la regresión el 41,9 por ciento de las veces y rechaza la versión sana el 36,0; con 100 casos, 28,0 y 22,4; con 400, 12,0 y 7,3; con 1600, 0,6 y 0,3; con tres corridas por caso las cifras bajan, con 400 casos a 1,5 y 0,7.',
               ['Casos', 'Pasa la regresión (1 corrida)', 'Rechaza la sana (1 corrida)', 'Pasa la regresión (3 corridas)', 'Rechaza la sana (3 corridas)'], rows, [110, 220, 220, 220, 200], row_h=44, size=13,
               note='Con 100 casos y una corrida, más de una de cada cuatro regresiones de 5 puntos se cuela y más de una de cada cinco versiones sanas se rechaza. Repetir tres veces cada caso ayuda, pero la reducción grande viene de más casos. Precisiones, umbral y modelo de azar son supuestos del autor.',
               note_kind='coral', foot=SINT)


def se489_bucle_de_evaluacion() -> Fig:
    return flow('El bucle de desarrollo guiado por evaluaciones',
                'Diagrama de seis cajas en dos filas: definir los casos y el criterio de aceptación, fijar una línea base, hacer un cambio, ejecutar la evaluación varias veces, comparar con el umbral y la variación y decidir entre publicar, retener o añadir casos.',
                [[('Casos y criterio de aceptación', 'gold'), ('Línea base medida con su variación', 'teal'), ('Cambio de prompt, modelo o código', 'plain')],
                 [('Evaluación repetida varias veces', 'teal'), ('Comparar con umbral y con la variación', 'coral'), ('Publicar, retener o añadir casos', 'navy')]],
                note='Una evaluación es un instrumento de medida con ruido. Sin línea base y sin variación, una diferencia de dos puntos es una opinión, no un resultado.',
                note_kind='gold', foot=SINT, box_h=84)


def se489_regresion_concentrada() -> Fig:
    rows = [['Muestra al azar, 100 casos (10 % difíciles)', '72,8 %', '4,4 %'], ['Solo casos difíciles, 100 casos', '0,0 %', '0,0 %'], ['Misma versión, mismos 100 casos, 1000 corridas', 'desviación 0,037', 'rango 0,72 a 0,95']]
    return tab('Regresión concentrada en los casos difíciles y ruido de la misma versión',
               'Tabla con una regresión concentrada en el 10 por ciento de casos difíciles que bajan de 0,60 a 0,20 de acierto: una muestra al azar de 100 casos deja pasar la regresión el 72,8 por ciento de las veces y rechaza la versión sana el 4,4, y un conjunto de 100 casos solo difíciles no deja pasar ninguna; la misma versión evaluada 1000 veces sobre los mismos 100 casos da una desviación de 0,037 y un rango de 0,72 a 0,95.',
               ['Conjunto o medida', 'Pasa la regresión', 'Rechaza la sana'], rows, [510, 230, 230], row_h=64, size=13,
               note='Un conjunto pequeño y curado en lo difícil detecta una regresión que una muestra grande al azar no ve. Al revés, la misma versión puede variar 23 puntos entre corridas con 100 casos: una sola corrida no mide.',
               note_kind='gold', foot=SINT)


# ---------------------------------------------------------------- SE-490
def se490_dos_historiales() -> Fig:
    rows = [['Documento de tarea antes del primer código', 'cumple', 'no cumple'], ['Ningún commit supera 400 líneas', 'cumple (el mayor, 13)', 'no cumple (463)'], ['Un tramo rojo seguido de uno verde', 'cumple', 'no cumple (todo verde de golpe)'], ['Hallazgos del comprobador', 'ninguno', 'tres']]
    return tab('Dos historiales de Git reales evaluados contra tres reglas del flujo ODD',
               'Tabla con dos historiales de Git reales creados en un directorio temporal y evaluados contra tres reglas: en el historial ordenado, con documento de tarea primero, un tramo rojo seguido de uno verde y un commit mayor de 13 líneas, el comprobador no halla nada; en el historial desordenado, con todo el código en un commit de 463 líneas y el documento después, incumple las tres reglas.',
               ['Regla', 'Historial A', 'Historial B'], rows, [430, 270, 270], row_h=56, size=13,
               note='El comprobador ejecuta las pruebas de cada commit para saber si estaba en rojo o en verde. Mira orden, tamaño y estado de las pruebas; no puede saber si el documento de tarea describe la realidad ni si 400 líneas es el límite adecuado.',
               note_kind='teal', foot=GIT)


def se490_flujo_odd() -> Fig:
    return flow('El flujo ODD de un cambio sustancial, de la autorización al commit',
                'Diagrama de seis cajas en dos filas: primero la autorización, porque explicar e investigar son solo lectura; un documento de tarea con alcance, tareas, evidencia y siguiente paso; una prueba roja; el código mínimo en verde; el refactor; y commits pequeños, con push, pull request y merge como decisiones aparte.',
                [[('Autorización primero: explorar es solo lectura', 'gold'), ('Documento de tarea: alcance, tareas, evidencia, siguiente paso', 'teal'), ('ROJO: una prueba determinista', 'coral')],
                 [('VERDE: el código mínimo', 'teal'), ('REFACTOR con todo en verde', 'plain'), ('Commits pequeños; push, PR y merge son decisiones aparte', 'navy')]],
                note='Los pasos descritos proceden de la documentación del proyecto que define el flujo y no de un estudio independiente: la clase los enseña como una descripción de un flujo concreto, con su evidencia declarada y sus límites.',
                note_kind='gold', foot='', box_h=96)


def se490_que_ve_el_comprobador() -> Fig:
    rows = [['Orden: el documento existe antes del primer código', 'Sí, con el historial', 'Un documento vacío cumple la regla'], ['Tamaño: líneas por commit', 'Sí, con numstat', 'Las líneas generadas o movidas cuentan igual que las escritas'],
            ['Estado de las pruebas en cada commit', 'Sí, ejecutándolas', 'Una prueba que no afirma nada pone el commit en verde'], ['Que el documento sea cierto y útil para retomar', 'No', 'Solo una persona al retomar lo sabe']]
    return tab('Qué comprueba la máquina del flujo ODD y qué solo puede juzgar una persona',
               'Tabla con cuatro aspectos del flujo ODD: el orden entre el documento y el primer código se comprueba con el historial, el tamaño de cada commit con la estadística numérica de Git, el estado de las pruebas ejecutándolas en cada commit, y que el documento sea cierto y sirva para retomar el trabajo no lo puede comprobar una máquina.',
               ['Aspecto', '¿Lo comprueba la máquina?', 'Límite'], rows, [370, 220, 380], row_h=70, size=13,
               note='Comprobar la forma del flujo es barato y ayuda; comprobar su fondo exige que alguien retome el trabajo con solo el documento y diga si pudo.',
               note_kind='gold', foot='')


# ---------------------------------------------------------------- SE-491
def se491_cinco_metodologias() -> Fig:
    rows = [['TDD: dos pruebas', '9', '6 de 7', '< 0,1'], ['BDD: tres escenarios', '15', '6 de 7', '< 0,1'], ['ATDD: tabla de ejemplos', '17', '5 de 7', '< 0,1'],
            ['Contrato con 400 estados', '15', '3 de 7', '≈ 4,5'], ['SDD: modelo ejecutable', '17', '7 de 7', '≈ 4,5']]
    return tab('El mismo cambio, silenciar un curso, con cinco metodologías: tamaño del artefacto y siete silencios mal hechos que mata',
               'Tabla con cinco metodologías aplicadas al mismo cambio de silenciar un curso y evaluadas contra siete mutantes del silencio: dos pruebas de TDD con 9 líneas matan 6, tres escenarios de BDD con 15 líneas matan 6, una tabla de ejemplos de ATDD con 17 líneas mata 5, un contrato con 400 estados con 15 líneas mata 3 y un modelo ejecutable de SDD con 17 líneas mata los 7.',
               ['Metodología', 'Líneas del artefacto', 'Mata', 'Tiempo (ms)'], rows, [380, 200, 170, 180], row_h=48, size=13,
               note='La unión de las cinco mata los 7 mutantes del silencio, pero el único método que mata los siete solo es el modelo ejecutable, que es también el que exige escribir de nuevo la regla. Líneas y tiempos son del experimento; la comparación de esfuerzo humano no se midió.',
               note_kind='gold', foot=LAB)


def se491_silencios_que_matan() -> Fig:
    return bars('Silencios mal hechos que mata cada metodología, de 7',
                'Gráfico de barras con los siete mutantes del silencio de un curso que mata cada metodología: dos pruebas de TDD matan 6, tres escenarios de BDD matan 6, la tabla de ejemplos de ATDD mata 5, el contrato con 400 estados mata 3 y el modelo ejecutable de SDD mata 7.',
                [('TDD (dos pruebas)', 6, 'gold', '6'), ('BDD (tres escenarios)', 6, 'gold', '6'), ('ATDD (tabla de ejemplos)', 5, 'gold', '5'), ('Contrato (400 estados)', 3, 'coral', '3'), ('SDD (modelo ejecutable)', 7, 'teal', '7')],
                scale=70, note='La barra más corta no indica la peor metodología: el contrato comprueba propiedades, no valores concretos, y ese es su papel. Indica qué clase de error deja ver y cuál deja pasar.',
                note_kind='gold', foot=LAB, label_w=300)


def se491_lo_que_deja_vivo() -> Fig:
    rows = [['TDD y BDD', 'S4: silencia el curso para todas las personas', 'Ningún ejemplo tiene dos personas en el mismo curso'], ['ATDD', 'S3 y S4: persona y curso', 'La tabla no varía persona ni curso'],
            ['Contrato', 'S2, S3, S4 y S7', 'Solo comprueba que un curso silenciado no recibe nada salvo la última hora'], ['SDD (modelo)', 'ninguno', 'Reescribe la regla por segunda vez; si ambas fallan igual, no se ve']]
    return tab('Qué silencios mal hechos deja vivos cada metodología y por qué',
               'Tabla con los mutantes que deja vivos cada metodología sobre el silencio de un curso: TDD y BDD dejan vivo S4, que silencia el curso para todas las personas, porque ningún ejemplo tiene dos personas en el mismo curso; ATDD deja vivos S3 y S4 porque su tabla no varía persona ni curso; el contrato deja vivos S2, S3, S4 y S7 porque solo comprueba una propiedad general; el modelo ejecutable no deja ninguno.',
               ['Metodología', 'Mutantes vivos', 'Por qué sobreviven'], rows, [200, 330, 440], row_h=64, size=13,
               note='En todos los casos la causa es una dimensión que el artefacto no varía o una regla que no repite. Añadir un ejemplo con dos personas y un curso común mata S4 en TDD, BDD y ATDD.',
               note_kind='coral', foot=LAB)


# ---------------------------------------------------------------- SE-492
def se492_politicas() -> Fig:
    rows = [['Nada', '0', '1 157', '—'], ['TDD en todo', '232', '745', '1,77'], ['Todo en todo', '1 240', '489', '0,54'], ['Por riesgo', '482', '532', '1,29'], ['Por riesgo y ambigüedad', '485', '499', '1,36']]
    return tab('Cinco políticas aplicadas a 300 cambios sintéticos: costo, impacto escapado e impacto evitado por hora',
               'Tabla con cinco políticas metodológicas aplicadas a 300 cambios sintéticos con tasas de detección medidas: no hacer nada deja un impacto escapado de 1157; TDD en todo cuesta 232 horas y deja 745; todo en todo cuesta 1240 y deja 489; por riesgo cuesta 482 y deja 532; por riesgo y ambigüedad cuesta 485 y deja 499.',
               ['Política', 'Costo (horas)', 'Impacto escapado', 'Impacto evitado por hora'], rows, [330, 190, 220, 230], row_h=44, size=13,
               note='Aplicarlo todo a todo es la política más cara y deja menos impacto, pero evita 0,54 por hora frente a 1,77 de TDD en todo. Costos, riesgos y fracción con reglas son supuestos del autor; solo las tasas de detección vienen del experimento de SE-481.',
               note_kind='gold', foot=SINT)


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
    "se-487-cambios-del-proveedor.svg": se487_cambios_del_proveedor,
    "se-487-asercion-y-optimizacion.svg": se487_asercion_y_optimizacion,
    "se-487-falsas-alarmas.svg": se487_falsas_alarmas,
    "se-488-derivas-inyectadas.svg": se488_derivas_inyectadas,
    "se-488-tres-niveles.svg": se488_tres_niveles,
    "se-488-que-ve-y-que-no.svg": se488_que_ve_y_que_no,
    "se-489-tamano-del-conjunto.svg": se489_tamano_del_conjunto,
    "se-489-bucle-de-evaluacion.svg": se489_bucle_de_evaluacion,
    "se-489-regresion-concentrada.svg": se489_regresion_concentrada,
    "se-490-dos-historiales.svg": se490_dos_historiales,
    "se-490-flujo-odd.svg": se490_flujo_odd,
    "se-490-que-ve-el-comprobador.svg": se490_que_ve_el_comprobador,
    "se-491-cinco-metodologias.svg": se491_cinco_metodologias,
    "se-491-silencios-que-matan.svg": se491_silencios_que_matan,
    "se-491-lo-que-deja-vivo.svg": se491_lo_que_deja_vivo,
    "se-492-politicas.svg": se492_politicas,
    "se-492-arbol-de-politica.svg": se492_arbol_de_politica,
    "se-492-tasas-de-deteccion.svg": se492_tasas_de_deteccion,
}
