"""Figures for SE-505 to SE-510 (agentic patterns and LLM systems: synthetic model with fixed seed, real tools, router, retrieval over the corpus of Parts 39 and 40; no language model was invoked)."""
from __future__ import annotations

from figure_cases import case_cards
from figure_kit import Fig, fmt_es, grouped_bars, heatmap, line_chart, scatter
from figures_part40_a import bars, flow

SIM = "Experimento propio con la biblioteca estándar; el modelo es sintético con semilla fija y no se invocó ningún modelo de lenguaje."
REAL = "Código y corpus reales del repositorio; las consultas son sintéticas y no se invocó ningún modelo de lenguaje."


# ---------------------------------------------------------------- SE-505
def se505_workflow_frente_a_agente() -> Fig:
    return grouped_bars('Workflow fijo frente a agente en tres tipos de solicitud de Avisos: llamadas, solicitudes resueltas y tokens',
                        'Barras agrupadas con el porcentaje de solicitudes resueltas por tipo de solicitud de Avisos: en la consulta de plazo el workflow resuelve el 100,0 por ciento y el agente el 99,0 con 1,2 veces los tokens; en silenciar un curso 100,0 y 96,7 con 2,8 veces; en la incidencia abierta el workflow no resuelve ninguna y se escala a una persona, mientras el agente resuelve el 93,1 con 7,0 veces los tokens.',
                        ['Consulta de plazo (60 %) · 2,0 llamadas frente a 2,1 · agente ×1,2 tokens', 'Silenciar un curso (25 %) · 2,0 frente a 4,2 llamadas · ×2,8 tokens', 'Incidencia abierta, de 3 a 8 pasos (15 %) · 2,0 frente a 6,8 llamadas · ×7,0 tokens'],
                        [('Workflow fijo', [100.0, 100.0, 0.0], 'teal'), ('Agente', [99.0, 96.7, 93.1], 'coral')],
                        unit='% de solicitudes resueltas', horizontal=True, label_w=360, decimals=1, ticks=[0, 25, 50, 75, 100],
                        note='Cada grupo es un tipo de solicitud con las llamadas y los tokens en la etiqueta; el agente (p95 de 3, 5 y 10 llamadas) cuesta más cuanto más fijo era el camino, y el workflow no resuelve las incidencias y las escala a una persona. Cómo leer la figura: cada fila es un tipo de solicitud y el agente cuesta más cuanto más fijo era el camino. Dónde deja de valer: el modelo es sintético, con 8 % de pasos equivocados y 1 % de pasos irreversibles por llamada, y 2 000 solicitudes con semilla 42; la tasa de errores de un modelo real es otra.',
                        note_kind='gold', foot=SIM)

def se505_costo_por_solicitud() -> Fig:
    items = [('Workflow para todo', 774, 'teal', '774 tokens; 85,0 % resueltas'), ('Agente para todo', 1862, 'coral', '1 862 tokens; 97,5 % resueltas'), ('Híbrido: agente solo en incidencias', 1421, 'gold', '1 421 tokens; 99,0 % resueltas')]
    return bars('Tokens medios por solicitud y solicitudes resueltas según la arquitectura de Avisos',
                'Barras con los tokens medios por solicitud de Avisos: el workflow para todo usa 774 tokens y resuelve el 85,0 por ciento, el agente para todo usa 1 862 tokens y resuelve el 97,5 por ciento, y el híbrido que usa el agente solo en las incidencias usa 1 421 tokens y resuelve el 99,0 por ciento.',
                items, 0.17, label_w=330, width=1000,
                note='Cómo leer la figura: la barra mide el costo y la etiqueta, el resultado. Dónde deja de valer: los tokens son una aproximación de un token por cuatro caracteres y cada llamada del agente vuelve a leer todo el historial; con otra política de caché el cociente cambia.', foot=SIM)


def se505_arbol_de_decision() -> Fig:
    rows = [[('¿Puedes escribir los pasos antes de ver la entrada?', 'navy'), ('Sí: workflow, el código decide el orden', 'teal'), ('No: ¿las acciones son reversibles y acotadas?', 'gold')],
            [('No: persona o diseño del flujo primero', 'coral'), ('Sí: agente con presupuesto de pasos y de costo', 'gold'), ('Mezcla: workflow para lo conocido y agente para el resto', 'teal')]]
    return flow('Árbol de decisión para elegir entre workflow, agente o persona',
                'Diagrama en dos filas. Primero se pregunta si los pasos se pueden escribir antes de ver la entrada: si sí, workflow donde el código decide el orden; si no, se pregunta si las acciones son reversibles y acotadas. Si no lo son, interviene una persona o se rediseña el flujo; si sí, un agente con presupuesto de pasos y de costo; y cuando hay mezcla, workflow para lo conocido y agente para el resto.',
                [[t for t in r] for r in rows], note='Cómo leer la figura: se recorre de izquierda a derecha y la segunda fila resuelve la segunda pregunta. Dónde deja de valer: es un criterio de partida y no sustituye la medición de calidad y costo con casos reales.', foot='')


# ---------------------------------------------------------------- SE-506
def se506_cadena_con_puerta() -> Fig:
    items = [('Cadena de 3 pasos sin puerta', 85.8, 'coral', '85,8 %'), ('Con puerta programática y un reintento', 97.8, 'teal', '97,8 %; 0,148 reintentos por ejecución')]
    return bars('Éxito de una cadena de tres pasos con y sin puerta programática entre pasos',
                'Barras con el éxito de una cadena de tres pasos donde cada paso acierta el 95 por ciento: sin puerta llega al 85,8 por ciento y con una puerta programática que detecta el error en el 90 por ciento de los casos y un reintento llega al 97,8 por ciento, con 0,148 reintentos por ejecución.',
                items, 4.5, label_w=330, width=1000,
                note='Cómo leer la figura: el error se multiplica a lo largo de la cadena y la puerta lo corta en el paso donde ocurre. Dónde deja de valer: supone errores independientes entre pasos y una puerta que detecta el 90 % de los errores; una puerta que mira lo que el propio modelo dijo no detecta nada.', foot=SIM)


def se506_enrutamiento() -> Fig:
    ns = [0, 30, 60]
    return line_chart('Dos enrutadores sobre 2 000 solicitudes de cuatro intenciones según el ruido del texto',
                      'Líneas con el acierto de dos enrutadores sobre 2 000 solicitudes de cuatro intenciones según el ruido del texto: las palabras clave bajan de 100,0 por ciento con texto limpio a 73,7 con 30 por ciento de ruido y 47,9 con 60; el clasificador por trigramas de 94,8 a 92,8 y 90,5; con umbral de confianza acierta el 100,0 por ciento de lo que acepta, que es el 53,9, el 47,8 y el 36,0 por ciento de las solicitudes.',
                      [('Palabras clave', [(n, v, fmt_es(v, 1), 't') for n, v in zip(ns, [100.0, 73.7, 47.9])], 'coral'), ('Centroide de trigramas', [(n, v, fmt_es(v, 1), 'b' if n == 0 else 't') for n, v in zip(ns, [94.8, 92.8, 90.5])], 'teal'),
                       ('Centroide con umbral 0,35: cobertura (acierto 100 %)', [(n, v, fmt_es(v, 1), 'b') for n, v in zip(ns, [53.9, 47.8, 36.0])], 'gold')],
                      x_label='Ruido en el texto (%)', y_label='Acierto o cobertura (%)', x_ticks=[(n, f'{n} %') for n in ns], y_ticks=[0, 20, 40, 60, 80, 100],
                      note='Sin ruta quedan el 0,0, el 26,3 y el 52,1 % de las solicitudes con palabras clave. Cómo leer la figura: el router de reglas no se equivoca, se queda sin ruta; el estadístico acierta más pero se equivoca sin avisar salvo que se le ponga umbral. Dónde deja de valer: cuatro intenciones y ocho ejemplos de entrenamiento escritos por el autor; con intenciones solapadas el acierto cae.',
                      note_kind='teal', foot=SIM)

def se506_paralelo_y_votacion() -> Fig:
    return case_cards('Paralelización con hilos reales y votación con y sin errores correlacionados',
                      'Cinco medidas como tarjetas: ocho subtareas de 50 milisegundos tardan 402 milisegundos en secuencia, 54 con ocho hilos y 203 con dos hilos; una votación de cinco muestras con acierto de 0,80 llega al 94,0 por ciento si los errores son independientes y al 87,4 por ciento si en la mitad de las ejecuciones las cinco comparten el mismo sesgo.',
                      [('Ocho subtareas de 50 ms, secuencial', '402 ms', 'La suma de las esperas.', 'coral'),
                       ('Las mismas, con 8 hilos', '54 ms', 'La espera más larga; solo vale si son independientes.', 'teal'),
                       ('Las mismas, con 2 hilos', '203 ms', 'Un límite de concurrencia reparte en cuatro tandas.', 'gold'),
                       ('Votación de 5 muestras, acierto 0,80, independientes', '94,0 % de acierto', 'El voto compra calidad si los errores no se repiten.', 'teal'),
                       ('Votación de 5, con la mitad de las ejecuciones sesgadas', '87,4 % de acierto', 'Los errores correlacionados reducen el beneficio del voto.', 'coral')],
                      note='Cómo leer la figura: los tiempos son del reloj real y varían entre equipos; los porcentajes son simulaciones con semilla. Dónde deja de valer: las esperas son de sueño, no de red, y la correlación del 50 % es un supuesto, no una medida de ningún modelo.',
                      note_kind='gold', foot='Hilos de CPython y simulación con semilla; no se invocó ningún modelo de lenguaje.')

# ---------------------------------------------------------------- SE-507
def se507_reparto_de_carga() -> Fig:
    return grouped_bars('Tiempo de reloj de un repaso de entregas con un agente, con reparto fijo y con orquestador',
                        'Barras agrupadas con el tiempo de reloj en unidades de trabajo de un repaso de entregas: con cursos de tamaño parecido un solo agente tarda 57,2, un reparto fijo entre tres trabajadores 23,1 y un orquestador 20,8; con cursos de tamaño de cola larga 155,4, 87,1 y 68,5.',
                        ['Cursos de tamaño parecido', 'Cursos con tamaño de cola larga'],
                        [('Un solo agente', [57.2, 155.4], 'coral'), ('Reparto fijo entre 3', [23.1, 87.1], 'gold'), ('Orquestador', [20.8, 68.5], 'teal')],
                        unit='unidades de trabajo (tiempo de reloj)', decimals=1,
                        note='Cómo leer la figura: la ventaja del orquestador crece con el desequilibrio, de 10 % a 21 % menos que el reparto fijo; la coordinación añade dos llamadas que no están en el gráfico. Dónde deja de valer: 500 repasos sintéticos con semilla 3 y trabajo medido en unidades, no en segundos.',
                        note_kind='teal', foot=SIM)

def se507_evaluador_optimizador() -> Fig:
    its = [0, 1, 2, 3]
    return line_chart('Evaluador-optimizador sobre un aviso con cuatro restricciones: verificador programático frente a juez ruidoso',
                      'Líneas con el porcentaje de avisos que pasa el verificador según las iteraciones de revisión: sin revisión pasa el 35,5 por ciento con evaluador programático y el 36,3 con juez ruidoso; con tres iteraciones el programático llega al 97,9 por ciento con 1,92 generaciones y el juez ruidoso se estanca en el 75,1 por ciento con 2,50 generaciones.',
                      [('Evaluador programático', [(i, v, fmt_es(v, 1), 't') for i, v in zip(its, [35.5, 77.3, 92.8, 97.9])], 'teal'), ('Juez ruidoso', [(i, v, fmt_es(v, 1), 'b') for i, v in zip(its, [36.3, 55.9, 71.1, 75.1])], 'coral')],
                      x_label='Iteraciones de revisión', y_label='Avisos que pasan el verificador (%)', x_ticks=[(i, str(i)) for i in its], y_ticks=[0, 20, 40, 60, 80, 100],
                      note='Generaciones medias por aviso con 0, 1, 2 y 3 iteraciones: 1,00, 1,64, 1,86 y 1,92 con el programático; 1,00, 1,74, 2,18 y 2,50 con el juez ruidoso. Cómo leer la figura: un evaluador que ve exactamente las fallas converge en tres vueltas; uno que se equivoca en el 30 % de las fallas y acusa falsas en el 15 % se estanca. Dónde deja de valer: cuatro restricciones, generador sintético que corrige lo señalado con probabilidad 0,80; un juez real puede ser mejor o peor.',
                      note_kind='gold', foot=SIM)

def se507_quien_decide() -> Fig:
    rows = [[('Entrada de tamaño variable', 'navy'), ('Orquestador: divide en subtareas (1 llamada)', 'teal'), ('Trabajadores con contexto propio y herramientas mínimas', 'teal')],
            [('Síntesis: reúne y verifica la salida', 'gold'), ('Evaluador: devuelve fallas concretas y verificables', 'gold'), ('Salida, o escalado a una persona al agotar el presupuesto', 'coral')]]
    return flow('Orquestador-trabajadores con un evaluador al final: quién decide qué',
                'Diagrama en dos filas: una entrada de tamaño variable llega a un orquestador que la divide en subtareas con una llamada, los trabajadores resuelven cada una con contexto propio y herramientas mínimas; después una síntesis reúne y verifica la salida, un evaluador devuelve fallas concretas y verificables, y el resultado sale o se escala a una persona al agotar el presupuesto.',
                rows, note='Cómo leer la figura: la decisión de cuántas subtareas hay es del orquestador y no se fija antes de ver la entrada. Dónde deja de valer: si el número de subtareas se conoce de antemano, es una paralelización de la clase anterior y no hace falta un orquestador.', foot='')


# ---------------------------------------------------------------- SE-508
def se508_estrategias() -> Fig:
    ss = [0, 15, 35]
    return line_chart('Cuatro estrategias en un entorno de avisos con contactos que faltan o estudiantes que se cambiaron de curso',
                      'Líneas con el éxito de cuatro estrategias según la tasa de sorpresas del entorno: sin sorpresas ReAct resuelve el 90,6 por ciento y las otras tres el 100; con 15 por ciento ReAct 88,2, el plan solo 54,2, la replanificación 94,9 y la reflexión 93,7; con 35 por ciento ReAct 89,0, el plan solo 21,1, la replanificación 88,2 y la reflexión 87,6.',
                      [('Plan', [(s, v, fmt_es(v, 1), 'b') for s, v in zip(ss, [100.0, 54.2, 21.1])], 'coral'), ('Plan con replanificación', [(s, v, '', 't') for s, v in zip(ss, [100.0, 94.9, 88.2])], 'teal'),
                       ('Plan con reflexión', [(s, v, '', 'b') for s, v in zip(ss, [100.0, 93.7, 87.6])], 'gold'), ('ReAct', [(s, v, fmt_es(v, 1) if s == 0 else '', 'b') for s, v in zip(ss, [90.6, 88.2, 89.0])], 'navy')],
                      point_labels='none', x_label='Tasa de sorpresas del entorno (%)', y_label='Solicitudes resueltas (%)', x_ticks=[(s, f'{s} %') for s in ss], y_ticks=[0, 20, 40, 60, 80, 100],
                      note='Éxito con 15 y 35 % de sorpresas: ReAct 88,2 y 89,0; replanificación 94,9 y 88,2; reflexión 93,7 y 87,6. Llamadas medias con 0, 15 y 35 % de sorpresas: ReAct 10,4, 11,1 y 11,7; plan 1,0 en los tres; replanificación 1,0, 1,6 y 2,3; reflexión 1,0, 2,5 y 3,9. Cómo leer la figura: ReAct paga más llamadas pero casi no depende de las sorpresas; el plan solo se hunde. Dónde deja de valer: 3 000 episodios con semilla 8, 5 % de decisiones equivocadas y 1 % de fatales por llamada para ReAct; las probabilidades de replanificar y reflexionar con éxito (0,90 y 0,85) son supuestos del autor.',
                      note_kind='gold', foot=SIM)

def se508_bucle_react_y_plan() -> Fig:
    rows = [[('ReAct: razonar sobre lo que falta', 'teal'), ('Actuar: una herramienta por vuelta', 'teal'), ('Observar: el resultado real entra al contexto', 'teal')],
            [('Plan: escribir todos los pasos una vez', 'gold'), ('Ejecutar con código, sin modelo en cada paso', 'gold'), ('Ante una sorpresa: replanificar, reflexionar o fallar', 'coral')]]
    return flow('El bucle de ReAct frente al plan único con reintento o reflexión',
                'Diagrama en dos filas. La primera es el bucle de ReAct: razonar sobre lo que falta, actuar con una herramienta por vuelta y observar el resultado real que entra al contexto. La segunda es plan-and-execute: escribir todos los pasos una vez, ejecutarlos con código sin modelo en cada paso y, ante una sorpresa, replanificar, reflexionar o fallar.',
                rows, note='Cómo leer la figura: ReAct paga una llamada por paso y se adapta; el plan paga una llamada y necesita que el mundo coopere. Dónde deja de valer: los dos se pueden combinar y muchos sistemas reales planifican por tramos.', foot='')


def se508_cuando_cada_una() -> Fig:
    return case_cards('Qué estrategia agéntica conviene según la estabilidad del entorno y el tipo de fallo',
                      'Cuatro situaciones como tarjetas: pasos y dependencias conocidos con entorno estable favorecen plan-and-execute; observaciones que cambian el siguiente paso favorecen ReAct; fallos recuperables y repetibles favorecen el plan con replanificación; y una lección útil para un segundo intento favorece la reflexión, siempre que exista una señal de fallo distinta del propio modelo.',
                      [('Los pasos y sus dependencias se conocen y el entorno es estable', 'Plan-and-execute', 'Una llamada de plan y ejecución barata, con registro de cada paso.', 'teal'),
                       ('Cada observación puede cambiar el siguiente paso', 'ReAct', 'La decisión depende de lo que devolvió la herramienta.', 'teal'),
                       ('El plan falla de forma recuperable y se puede repetir', 'Plan con replanificación', 'Replanificar solo cuando una observación contradice el plan.', 'gold'),
                       ('Un fallo deja una lección que sirve en el segundo intento', 'Reflexión con verificador', 'Solo si hay una señal de fallo que no sea el propio modelo.', 'gold')],
                      note='Cómo leer la figura: es una guía de criterio y no una medida; lo medido está en la primera figura de la clase. Dónde deja de valer: en tareas de pocas herramientas la diferencia de costo es pequeña y pesa más la facilidad de depurar.',
                      note_kind='teal', foot='')

# ---------------------------------------------------------------- SE-509
def se509_recuperacion_de_hechos() -> Fig:
    items = [('Contexto completo con presupuesto', 67.1, 'gold', '67,1 %'), ('Ventana de 20 turnos', 41.5, 'coral', '41,5 %'), ('Resumen con pérdidas', 74.8, 'gold', '74,8 %'),
             ('Almacén sin versión', 40.8, 'coral', '40,8 %'), ('Almacén con versión', 95.2, 'teal', '95,2 %')]
    return bars('Hechos vigentes recuperados al final de 80 turnos según la estrategia de memoria',
                'Barras con el porcentaje de hechos vigentes que cada estrategia recupera al final de 80 turnos: contexto completo con presupuesto 67,1, ventana de 20 turnos 41,5, resumen con pérdidas 74,8, almacén externo sin versión 40,8 y almacén externo con versión 95,2.',
                items, 5.0, label_w=300, width=1000,
                note='Cómo leer la figura: se pregunta por el valor vigente de cada hecho, y 25 % de los turnos contienen un hecho que a veces reemplaza a uno anterior. Dónde deja de valer: 300 conversaciones sintéticas, extracción con 95 % de acierto y resumen que conserva cada cambio con 75 %; son supuestos y no mediciones de un modelo.', foot=SIM)


def se509_costo_de_recordar() -> Fig:
    return scatter('Tokens de memoria que se envían al preguntar, aciertos y fallo típico de cada estrategia',
                   'Puntos con los tokens de memoria enviados al preguntar y el porcentaje de acierto: contexto completo con presupuesto 1 973 tokens y 67,1 por ciento, ventana de 20 turnos 1 041 y 41,5, resumen con pérdidas 150 y 74,8, almacén sin versión 80 y 40,8 y almacén con versión 80 y 95,2; el almacén con versión es el punto de menor costo y mayor acierto.',
                   [('Contexto completo con presupuesto', [(1973, 67.1, '67,1 %', 'l')], 'gold'), ('Ventana de 20 turnos', [(1041, 41.5, '41,5 %', 'r')], 'coral'), ('Resumen con pérdidas', [(150, 74.8, '74,8 %', 'r')], 'navy'),
                    ('Almacén sin versión', [(80, 40.8, '40,8 %', 'r')], 'grey'), ('Almacén con versión', [(80, 95.2, '95,2 %', 'r')], 'teal')],
                   x_label='Tokens de memoria enviados al preguntar', y_label='Hechos vigentes recuperados (%)', log_x=True, x_ticks=[(80, '80'), (150, '150'), (1041, '1 041'), (1973, '1 973')], y_ticks=[0, 20, 40, 60, 80, 100],
                   note='Fallo típico: el contexto completo pierde lo más antiguo sin aviso, la ventana olvida todo lo anterior, el resumen deja el valor viejo si un cambio no se resume, el almacén sin versión devuelve el primer valor, ya obsoleto, y el almacén con versión falla si el extractor no detecta el hecho. Cómo leer la figura: menos tokens no significa menos aciertos; una memoria externa bien versionada gasta una fracción y acierta más. Dónde deja de valer: el costo de extraer, escribir y consultar el almacén no está en los tokens del gráfico.',
                   note_kind='gold', foot=SIM)

def se509_capas_de_memoria() -> Fig:
    rows = [[('Contexto de trabajo: lo que el modelo ve ahora', 'navy'), ('Resumen: lo que se comprime con pérdidas', 'gold'), ('Almacén externo: hechos con clave, fecha y origen', 'teal')],
            [('Escritura: quién decide qué se guarda', 'coral'), ('Lectura: por clave o por similitud, con versión vigente', 'teal'), ('Borrado y caducidad: qué se olvida a propósito', 'coral')]]
    return flow('Capas de memoria de un agente y sus decisiones de escritura, lectura y olvido',
                'Diagrama en dos filas. La primera tiene el contexto de trabajo que el modelo ve ahora, el resumen que comprime con pérdidas y el almacén externo de hechos con clave, fecha y origen. La segunda tiene la escritura, que decide qué se guarda, la lectura por clave o por similitud con la versión vigente, y el borrado y la caducidad, que deciden qué se olvida a propósito.',
                rows, note='Cómo leer la figura: la memoria no es una sola cosa; cada capa tiene un costo y una forma de fallar distintos. Dónde deja de valer: una memoria con datos personales exige además base legal, plazo y derecho de borrado, que el esquema no muestra.', foot='')


# ---------------------------------------------------------------- SE-510
def se510_recuperadores() -> Fig:
    return heatmap('Tres recuperadores sobre 835 fragmentos de las Partes 39 y 40 y 120 consultas sintéticas',
                   'Mapa de calor con el acierto de tres recuperadores sobre 835 fragmentos: con consultas exactas BM25 acierta en primer lugar el 98,3 por ciento, el vector por trigramas el 65,0 y el híbrido el 85,0; con erratas y raíces BM25 el 75,0, el vector el 59,2 y el híbrido el 77,5; en los cinco primeros 100,0, 80,0, 93,3 y 90,8, 77,5, 90,0.',
                   ['BM25 · consultas exactas (MRR 0,992)', 'Vector por trigramas · exactas (0,732)', 'Híbrido por rango recíproco · exactas (0,893)', 'BM25 · con erratas y raíces (0,817)', 'Vector por trigramas · con erratas (0,685)', 'Híbrido por rango recíproco · con erratas (0,829)'],
                   ['Acierto en 1.º', 'Acierto en los 5 primeros'], [[98.3, 100.0], [65.0, 80.0], [85.0, 93.3], [75.0, 90.8], [59.2, 77.5], [77.5, 90.0]],
                   unit='% de acierto', scale='teal', vmin=0, vmax=100, suffix=' %', decimals=1, label_w=360,
                   note='Entre paréntesis, el MRR. Cómo leer la figura: el vector por trigramas no es un modelo semántico; es un sustituto que muestra el mecanismo denso sin descargar ningún modelo. Dónde deja de valer: las consultas salen del propio texto y favorecen la coincidencia léxica; con paráfrasis reales un modelo de embeddings cambiaría el orden.',
                   note_kind='gold', foot=REAL)

def se510_reformulacion_y_abstencion() -> Fig:
    return case_cards('Reformulación de consultas y abstención en una recuperación agéntica sobre el corpus propio',
                      'Tres decisiones de un sistema de recuperación como tarjetas: reformular con términos de los tres mejores fragmentos movió el acierto en primer lugar de 68,3 por ciento a 66,7 con 39 de 120 consultas reformuladas, sin mejorar; rechazar por umbral de puntuación descartó el 67 por ciento de seis consultas ajenas al corpus y el 10 por ciento de las válidas; citar el fragmento que respalda la respuesta permite verificarla.',
                      [('Reformular con términos de los tres mejores fragmentos', 'Acierto en 1.º de 68,3 % a 66,7 %; 39 de 120 consultas reformuladas', 'Costó llamadas y no mejoró: había que medirlo.', 'coral'),
                       ('Rechazar consultas por umbral de puntuación', '67 % de las 6 consultas ajenas al corpus rechazadas; 10 % de las válidas rechazadas por construcción', 'Abstenerse tiene un precio en consultas válidas.', 'gold'),
                       ('Citar el fragmento que respalda la respuesta', 'Cada respuesta enlaza su origen', 'Permite que otra persona verifique.', 'teal')],
                      note='Cómo leer la figura: reformular o abstenerse son decisiones que se miden como cualquier otra. Dónde deja de valer: la reformulación es por retroalimentación de pseudorrelevancia y solo seis consultas ajenas al corpus; no se probó con un modelo que reescriba consultas.',
                      note_kind='coral', foot=REAL)

def se510_canalizacion() -> Fig:
    rows = [[('Fragmentar por encabezado, con título y origen', 'plain'), ('Indexar: léxico, vectorial o ambos', 'teal'), ('Recuperar k fragmentos con puntuación', 'teal')],
            [('Filtrar: umbral, permisos y vigencia', 'gold'), ('Responder citando el fragmento usado', 'gold'), ('Medir: acierto, abstención y respuestas sin respaldo', 'coral')]]
    return flow('Canalización de recuperación y respuesta con citas',
                'Diagrama en dos filas. Primero se fragmenta por encabezado conservando título y origen, se indexa de forma léxica, vectorial o ambas y se recuperan k fragmentos con puntuación. Después se filtra por umbral, permisos y vigencia, se responde citando el fragmento usado y se mide el acierto, la abstención y las respuestas sin respaldo.',
                rows, note='Cómo leer la figura: cada caja es un lugar donde se puede medir y fallar por separado. Dónde deja de valer: en corpus que cambian a diario la fragmentación y el índice se vuelven un proceso operativo con su propio ciclo.', foot='')


FIGURES = {
    "se-505-workflow-frente-a-agente.svg": se505_workflow_frente_a_agente,
    "se-505-costo-por-solicitud.svg": se505_costo_por_solicitud,
    "se-505-arbol-de-decision.svg": se505_arbol_de_decision,
    "se-506-cadena-con-puerta.svg": se506_cadena_con_puerta,
    "se-506-enrutamiento.svg": se506_enrutamiento,
    "se-506-paralelo-y-votacion.svg": se506_paralelo_y_votacion,
    "se-507-reparto-de-carga.svg": se507_reparto_de_carga,
    "se-507-evaluador-optimizador.svg": se507_evaluador_optimizador,
    "se-507-quien-decide.svg": se507_quien_decide,
    "se-508-estrategias.svg": se508_estrategias,
    "se-508-bucle-react-y-plan.svg": se508_bucle_react_y_plan,
    "se-508-cuando-cada-una.svg": se508_cuando_cada_una,
    "se-509-recuperacion-de-hechos.svg": se509_recuperacion_de_hechos,
    "se-509-costo-de-recordar.svg": se509_costo_de_recordar,
    "se-509-capas-de-memoria.svg": se509_capas_de_memoria,
    "se-510-recuperadores.svg": se510_recuperadores,
    "se-510-reformulacion-y-abstencion.svg": se510_reformulacion_y_abstencion,
    "se-510-canalizacion.svg": se510_canalizacion,
}
