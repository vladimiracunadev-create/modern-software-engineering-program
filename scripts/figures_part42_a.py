"""Figures for SE-505 to SE-510 (agentic patterns and LLM systems: synthetic model with fixed seed, real tools, router, retrieval over the corpus of Parts 39 and 40; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab
from figures_part40_a import bars, flow

SIM = "Experimento propio con la biblioteca estándar; el modelo es sintético con semilla fija y no se invocó ningún modelo de lenguaje."
REAL = "Código y corpus reales del repositorio; las consultas son sintéticas y no se invocó ningún modelo de lenguaje."


# ---------------------------------------------------------------- SE-505
def se505_workflow_frente_a_agente() -> Fig:
    rows = [['Consulta de plazo (60 % de las solicitudes)', '2,0 llamadas; 100,0 % resueltas', '2,1 llamadas (p95 de 3); 99,0 % resueltas', '1,2 veces'],
            ['Silenciar un curso (25 %)', '2,0 llamadas; 100,0 % resueltas', '4,2 llamadas (p95 de 5); 96,7 % resueltas', '2,8 veces'],
            ['Incidencia abierta, de 3 a 8 pasos (15 %)', '2,0 llamadas; 0,0 % resueltas, se escala a una persona', '6,8 llamadas (p95 de 10); 93,1 % resueltas', '7,0 veces']]
    return tab('Workflow fijo frente a agente en tres tipos de solicitud de Avisos: llamadas, solicitudes resueltas y tokens',
               'Tabla con tres tipos de solicitud de Avisos. En la consulta de plazo el workflow usa 2,0 llamadas y resuelve el 100,0 por ciento, el agente usa 2,1 llamadas y resuelve el 99,0 por ciento y gasta 1,2 veces los tokens. En silenciar un curso el agente usa 4,2 llamadas y gasta 2,8 veces los tokens. En la incidencia abierta el workflow no resuelve ninguna y se escala a una persona, mientras el agente usa 6,8 llamadas, resuelve el 93,1 por ciento y gasta 7,0 veces los tokens.',
               ['Tipo de solicitud', 'Workflow fijo', 'Agente', 'Tokens: agente / wf'], rows, [300, 260, 270, 140], row_h=70, size=13,
               note='Cómo leer la figura: cada fila es un tipo de solicitud y el agente cuesta más cuanto más fijo era el camino. Dónde deja de valer: el modelo es sintético, con 8 % de pasos equivocados y 1 % de pasos irreversibles por llamada, y 2 000 solicitudes con semilla 42; la tasa de errores de un modelo real es otra.',
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
    rows = [['0 % (solicitudes limpias)', '100,0 %; 0,0 % sin ruta', '94,8 %', '53,9 % de cobertura; 100,0 % de acierto'],
            ['30 % (erratas y palabras de relleno)', '73,7 %; 26,3 % sin ruta', '92,8 %', '47,8 % de cobertura; 100,0 % de acierto'],
            ['60 % (mucho ruido)', '47,9 %; 52,1 % sin ruta', '90,5 %', '36,0 % de cobertura; 100,0 % de acierto']]
    return tab('Dos enrutadores sobre 2 000 solicitudes de cuatro intenciones según el ruido del texto',
               'Tabla con dos enrutadores sobre 2 000 solicitudes de cuatro intenciones. Con texto limpio las palabras clave aciertan el 100,0 por ciento y el clasificador por trigramas el 94,8; con 30 por ciento de ruido las palabras clave bajan al 73,7 y dejan el 26,3 sin ruta y el clasificador baja al 92,8; con 60 por ciento las palabras clave aciertan el 47,9 y el clasificador el 90,5. Con un umbral de confianza el clasificador acierta el 100,0 por ciento de lo que acepta, que es el 53,9, el 47,8 y el 36,0 por ciento de las solicitudes.',
               ['Ruido en el texto', 'Palabras clave', 'Centroide de trigramas', 'Centroide con umbral 0,35'], rows, [260, 230, 190, 290], row_h=70, size=13,
               note='Cómo leer la figura: el router de reglas no se equivoca, se queda sin ruta; el estadístico acierta más pero se equivoca sin avisar salvo que se le ponga umbral. Dónde deja de valer: cuatro intenciones y ocho ejemplos de entrenamiento escritos por el autor; con intenciones solapadas el acierto cae.',
               note_kind='teal', foot=SIM)


def se506_paralelo_y_votacion() -> Fig:
    rows = [['Ocho subtareas de 50 ms, secuencial', '402 ms', 'La suma de las esperas'],
            ['Las mismas, con 8 hilos', '54 ms', 'La espera más larga; solo vale si son independientes'],
            ['Las mismas, con 2 hilos', '203 ms', 'Un límite de concurrencia reparte en cuatro tandas'],
            ['Votación de 5 muestras, acierto 0,80, independientes', '94,0 %', 'El voto compra calidad si los errores no se repiten'],
            ['Votación de 5, con la mitad de las ejecuciones sesgadas', '87,4 %', 'Los errores correlacionados reducen el beneficio del voto']]
    return tab('Paralelización con hilos reales y votación con y sin errores correlacionados',
               'Tabla con cinco medidas. Ocho subtareas de 50 milisegundos tardan 402 milisegundos en secuencia, 54 con ocho hilos y 203 con dos hilos. Una votación de cinco muestras con acierto de 0,80 llega al 94,0 por ciento si los errores son independientes y al 87,4 por ciento si en la mitad de las ejecuciones las cinco comparten el mismo sesgo.',
               ['Medida', 'Resultado', 'Lectura'], rows, [380, 140, 450], row_h=60, size=13,
               note='Cómo leer la figura: los tiempos son del reloj real y varían entre equipos; los porcentajes son simulaciones con semilla. Dónde deja de valer: las esperas son de sueño, no de red, y la correlación del 50 % es un supuesto, no una medida de ningún modelo.',
               note_kind='gold', foot='Hilos de CPython y simulación con semilla; no se invocó ningún modelo de lenguaje.')


# ---------------------------------------------------------------- SE-507
def se507_reparto_de_carga() -> Fig:
    rows = [['Cursos de tamaño parecido', '57,2', '23,1', '20,8'], ['Cursos con tamaño de cola larga', '155,4', '87,1', '68,5']]
    return tab('Tiempo de reloj de un repaso de entregas con un agente, con reparto fijo y con orquestador',
               'Tabla con el tiempo de reloj en unidades de trabajo de un repaso de entregas. Con cursos de tamaño parecido un solo agente tarda 57,2, un reparto fijo entre tres trabajadores 23,1 y un orquestador que reparte primero lo más grande 20,8. Con cursos de tamaño de cola larga tarda 155,4, 87,1 y 68,5.',
               ['Carga', 'Un solo agente', 'Reparto fijo entre 3', 'Orquestador'], rows, [330, 200, 220, 200], row_h=56, size=13,
               note='Cómo leer la figura: la ventaja del orquestador crece con el desequilibrio, de 10 % a 21 % menos que el reparto fijo; la coordinación añade dos llamadas que no están en la tabla. Dónde deja de valer: 500 repasos sintéticos con semilla 3 y trabajo medido en unidades, no en segundos.',
               note_kind='teal', foot=SIM)


def se507_evaluador_optimizador() -> Fig:
    rows = [['0 (sin revisión)', '35,5 %; 1,00', '36,3 %; 1,00'], ['1', '77,3 %; 1,64', '55,9 %; 1,74'], ['2', '92,8 %; 1,86', '71,1 %; 2,18'], ['3', '97,9 %; 1,92', '75,1 %; 2,50']]
    return tab('Evaluador-optimizador sobre un aviso con cuatro restricciones: verificador programático frente a juez ruidoso',
               'Tabla con el porcentaje de avisos que pasa el verificador y las generaciones medias por aviso según las iteraciones de revisión. Sin revisión pasa el 35,5 por ciento con evaluador programático y el 36,3 con juez ruidoso. Con tres iteraciones el programático llega al 97,9 por ciento con 1,92 generaciones y el juez ruidoso al 75,1 por ciento con 2,50 generaciones.',
               ['Iteraciones de revisión', 'Evaluador programático: pasa; generaciones', 'Juez ruidoso: pasa; generaciones'], rows, [240, 370, 360], row_h=52, size=13,
               note='Cómo leer la figura: un evaluador que ve exactamente las fallas converge en tres vueltas; uno que se equivoca en el 30 % de las fallas y acusa falsas en el 15 % se estanca. Dónde deja de valer: cuatro restricciones, generador sintético que corrige lo señalado con probabilidad 0,80; un juez real puede ser mejor o peor.',
               note_kind='gold', foot=SIM)


def se507_quien_decide() -> Fig:
    rows = [[('Entrada de tamaño variable', 'navy'), ('Orquestador: divide en subtareas (1 llamada)', 'teal'), ('Trabajadores con contexto propio y herramientas mínimas', 'teal')],
            [('Síntesis: reúne y verifica la salida', 'gold'), ('Evaluador: devuelve fallas concretas y verificables', 'gold'), ('Salida, o escalado a una persona al agotar el presupuesto', 'coral')]]
    return flow('Orquestador-trabajadores con un evaluador al final: quién decide qué',
                'Diagrama en dos filas: una entrada de tamaño variable llega a un orquestador que la divide en subtareas con una llamada, los trabajadores resuelven cada una con contexto propio y herramientas mínimas; después una síntesis reúne y verifica la salida, un evaluador devuelve fallas concretas y verificables, y el resultado sale o se escala a una persona al agotar el presupuesto.',
                rows, note='Cómo leer la figura: la decisión de cuántas subtareas hay es del orquestador y no se fija antes de ver la entrada. Dónde deja de valer: si el número de subtareas se conoce de antemano, es una paralelización de la clase anterior y no hace falta un orquestador.', foot='')


# ---------------------------------------------------------------- SE-508
def se508_estrategias() -> Fig:
    rows = [['0 % (el mundo es como se planeó)', '90,6 %; 10,4 llamadas', '100,0 %; 1,0', '100,0 %; 1,0', '100,0 %; 1,0'],
            ['15 %', '88,2 %; 11,1', '54,2 %; 1,0', '94,9 %; 1,6', '93,7 %; 2,5'],
            ['35 %', '89,0 %; 11,7', '21,1 %; 1,0', '88,2 %; 2,3', '87,6 %; 3,9']]
    return tab('Cuatro estrategias en un entorno de avisos con contactos que faltan o estudiantes que se cambiaron de curso',
               'Tabla con el éxito y las llamadas medias de cuatro estrategias según la tasa de sorpresas del entorno. Sin sorpresas ReAct resuelve el 90,6 por ciento con 10,4 llamadas y las otras tres el 100 por ciento con una llamada. Con 15 por ciento de sorpresas ReAct resuelve el 88,2, el plan solo el 54,2, el plan con replanificación el 94,9 con 1,6 llamadas y el plan con reflexión el 93,7 con 2,5 llamadas. Con 35 por ciento ReAct resuelve el 89,0, el plan solo el 21,1, la replanificación el 88,2 y la reflexión el 87,6.',
               ['Tasa de sorpresas', 'ReAct', 'Plan', 'Plan con replanificación', 'Plan con reflexión'], rows, [250, 200, 140, 200, 180], row_h=64, size=13,
               note='Cómo leer la figura: cada celda dice solicitudes resueltas y llamadas medias. Dónde deja de valer: 3 000 episodios con semilla 8, 5 % de decisiones equivocadas y 1 % de fatales por llamada para ReAct; las probabilidades de replanificar y reflexionar con éxito (0,90 y 0,85) son supuestos del autor.',
               note_kind='gold', foot=SIM)


def se508_bucle_react_y_plan() -> Fig:
    rows = [[('ReAct: razonar sobre lo que falta', 'teal'), ('Actuar: una herramienta por vuelta', 'teal'), ('Observar: el resultado real entra al contexto', 'teal')],
            [('Plan: escribir todos los pasos una vez', 'gold'), ('Ejecutar con código, sin modelo en cada paso', 'gold'), ('Ante una sorpresa: replanificar, reflexionar o fallar', 'coral')]]
    return flow('El bucle de ReAct frente al plan único con reintento o reflexión',
                'Diagrama en dos filas. La primera es el bucle de ReAct: razonar sobre lo que falta, actuar con una herramienta por vuelta y observar el resultado real que entra al contexto. La segunda es plan-and-execute: escribir todos los pasos una vez, ejecutarlos con código sin modelo en cada paso y, ante una sorpresa, replanificar, reflexionar o fallar.',
                rows, note='Cómo leer la figura: ReAct paga una llamada por paso y se adapta; el plan paga una llamada y necesita que el mundo coopere. Dónde deja de valer: los dos se pueden combinar y muchos sistemas reales planifican por tramos.', foot='')


def se508_cuando_cada_una() -> Fig:
    rows = [['Los pasos y sus dependencias se conocen y el entorno es estable', 'Plan-and-execute', 'Una llamada de plan y ejecución barata, con registro de cada paso'],
            ['Cada observación puede cambiar el siguiente paso', 'ReAct', 'La decisión depende de lo que devolvió la herramienta'],
            ['El plan falla de forma recuperable y se puede repetir', 'Plan con replanificación', 'Replanificar solo cuando una observación contradice el plan'],
            ['Un fallo deja una lección que sirve en el segundo intento', 'Reflexión con verificador', 'Solo si hay una señal de fallo que no sea el propio modelo']]
    return tab('Qué estrategia agéntica conviene según la estabilidad del entorno y el tipo de fallo',
               'Tabla de decisión con cuatro situaciones: pasos y dependencias conocidos con entorno estable favorecen plan-and-execute; observaciones que cambian el siguiente paso favorecen ReAct; fallos recuperables y repetibles favorecen el plan con replanificación; y una lección útil para un segundo intento favorece la reflexión, siempre que exista una señal de fallo distinta del propio modelo.',
               ['Situación', 'Estrategia que conviene', 'Por qué'], rows, [370, 220, 380], row_h=70, size=13,
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
    rows = [['Contexto completo con presupuesto', '1 973', '67,1 %', 'Lo más antiguo se pierde sin aviso'],
            ['Ventana de 20 turnos', '1 041', '41,5 %', 'Olvida todo lo anterior a la ventana'],
            ['Resumen con pérdidas', '150', '74,8 %', 'Un cambio no resumido deja el valor viejo'],
            ['Almacén sin versión', '80', '40,8 %', 'Devuelve el primer valor, ya obsoleto'],
            ['Almacén con versión', '80', '95,2 %', 'Falla si el extractor no detecta el hecho']]
    return tab('Tokens de memoria que se envían al preguntar, aciertos y fallo típico de cada estrategia',
               'Tabla con los tokens de memoria enviados al preguntar, el acierto y el fallo típico: contexto completo con presupuesto 1 973 tokens y 67,1 por ciento, ventana de 20 turnos 1 041 y 41,5, resumen con pérdidas 150 y 74,8, almacén sin versión 80 y 40,8, almacén con versión 80 y 95,2.',
               ['Estrategia', 'Tokens', 'Aciertos', 'Fallo típico'], rows, [290, 100, 120, 460], row_h=52, size=13,
               note='Cómo leer la figura: menos tokens no significa menos aciertos; una memoria externa bien versionada gasta una fracción y acierta más. Dónde deja de valer: el costo de extraer, escribir y consultar el almacén no está en los tokens de la tabla.',
               note_kind='gold', foot=SIM)


def se509_capas_de_memoria() -> Fig:
    rows = [[('Contexto de trabajo: lo que el modelo ve ahora', 'navy'), ('Resumen: lo que se comprime con pérdidas', 'gold'), ('Almacén externo: hechos con clave, fecha y origen', 'teal')],
            [('Escritura: quién decide qué se guarda', 'coral'), ('Lectura: por clave o por similitud, con versión vigente', 'teal'), ('Borrado y caducidad: qué se olvida a propósito', 'coral')]]
    return flow('Capas de memoria de un agente y sus decisiones de escritura, lectura y olvido',
                'Diagrama en dos filas. La primera tiene el contexto de trabajo que el modelo ve ahora, el resumen que comprime con pérdidas y el almacén externo de hechos con clave, fecha y origen. La segunda tiene la escritura, que decide qué se guarda, la lectura por clave o por similitud con la versión vigente, y el borrado y la caducidad, que deciden qué se olvida a propósito.',
                rows, note='Cómo leer la figura: la memoria no es una sola cosa; cada capa tiene un costo y una forma de fallar distintos. Dónde deja de valer: una memoria con datos personales exige además base legal, plazo y derecho de borrado, que el esquema no muestra.', foot='')


# ---------------------------------------------------------------- SE-510
def se510_recuperadores() -> Fig:
    rows = [['Exactas', 'BM25', '98,3 %', '100,0 %', '0,992'], ['Exactas', 'Vector por trigramas con hashing', '65,0 %', '80,0 %', '0,732'], ['Exactas', 'Híbrido por rango recíproco', '85,0 %', '93,3 %', '0,893'],
            ['Con erratas y raíces', 'BM25', '75,0 %', '90,8 %', '0,817'], ['Con erratas y raíces', 'Vector por trigramas con hashing', '59,2 %', '77,5 %', '0,685'], ['Con erratas y raíces', 'Híbrido por rango recíproco', '77,5 %', '90,0 %', '0,829']]
    return tab('Tres recuperadores sobre 835 fragmentos de las Partes 39 y 40 y 120 consultas sintéticas',
               'Tabla con tres recuperadores sobre 835 fragmentos. Con consultas exactas BM25 acierta en primer lugar el 98,3 por ciento, el vector por trigramas el 65,0 y el híbrido el 85,0. Con erratas y raíces BM25 acierta el 75,0, el vector el 59,2 y el híbrido el 77,5; en los cinco primeros BM25 llega al 90,8, el vector al 77,5 y el híbrido al 90,0.',
               ['Consultas', 'Recuperador', 'Acierto en 1.º', 'Acierto en 5', 'MRR'], rows, [200, 330, 140, 140, 130], row_h=48, size=13,
               note='Cómo leer la figura: el vector por trigramas no es un modelo semántico; es un sustituto que muestra el mecanismo denso sin descargar ningún modelo. Dónde deja de valer: las consultas salen del propio texto y favorecen la coincidencia léxica; con paráfrasis reales un modelo de embeddings cambiaría el orden.',
               note_kind='gold', foot=REAL)


def se510_reformulacion_y_abstencion() -> Fig:
    rows = [['Reformular con términos de los tres mejores fragmentos', 'Acierto en 1.º de 68,3 % a 66,7 %; 39 de 120 consultas reformuladas', 'Costó llamadas y no mejoró: había que medirlo'],
            ['Rechazar consultas por umbral de puntuación', '67 % de las 6 consultas ajenas al corpus rechazadas; 10 % de las válidas rechazadas por construcción', 'Abstenerse tiene un precio en consultas válidas'],
            ['Citar el fragmento que respalda la respuesta', 'Cada respuesta enlaza su origen', 'Permite que otra persona verifique']]
    return tab('Reformulación de consultas y abstención en una recuperación agéntica sobre el corpus propio',
               'Tabla con tres decisiones de un sistema de recuperación. Reformular con términos de los tres mejores fragmentos movió el acierto en primer lugar de 68,3 por ciento a 66,7 con 39 de 120 consultas reformuladas, sin mejorar. Rechazar por umbral de puntuación descartó el 67 por ciento de seis consultas ajenas al corpus y el 10 por ciento de las válidas por construcción. Citar el fragmento que respalda la respuesta permite verificarla.',
               ['Decisión', 'Resultado medido', 'Lectura'], rows, [330, 400, 240], row_h=84, size=13,
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
