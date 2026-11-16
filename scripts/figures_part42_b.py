"""Figures for SE-511 to SE-516 (agentic patterns and LLM systems: real JSON-RPC process, SQLite journal with injected crashes, statistical gates over synthetic results, capability policy; no language model was invoked)."""
from __future__ import annotations

from figure_cases import case_cards
from figure_kit import Fig, fmt_es, grouped_bars, heatmap, line_chart, percentile_intervals
from figures_part40_a import bars, flow

SIM = "Experimento propio con la biblioteca estándar; el modelo es sintético con semilla fija y no se invocó ningún modelo de lenguaje."
REAL = "Procesos, diario SQLite y mensajes reales en un directorio temporal; no se invocó ningún modelo de lenguaje."


# ---------------------------------------------------------------- SE-511
def se511_protocolo_por_stdio() -> Fig:
    return case_cards('Un servidor JSON-RPC por entrada y salida estándar en un proceso real: qué responde a cada mensaje',
                      'Seis mensajes a un servidor real de dos herramientas como tarjetas: initialize devuelve nombre y versión del servidor; tools/list devuelve dos herramientas con su esquema; tools/call con el curso c1 devuelve la fecha 2026-11-20 con una mediana de 0,10 milisegundos; un JSON roto devuelve el error -32700; un método inexistente y unos parámetros inválidos devuelven -32601 y -32602; y unos argumentos faltantes devuelven un resultado con isError verdadero.',
                      [('initialize', 'Responde nombre y versión del servidor', 'Primera llamada de cualquier sesión.', 'teal'),
                       ('tools/list', 'Devuelve 2 herramientas con su esquema de entrada', 'El agente descubre qué puede hacer.', 'teal'),
                       ('tools/call con curso c1', 'Devuelve la fecha 2026-11-20', 'Mediana de 0,10 ms por ida y vuelta (reloj real).', 'teal'),
                       ('JSON roto', 'Error -32700', 'El servidor sigue vivo y responde al siguiente.', 'coral'),
                       ('Método inexistente o parámetros inválidos', 'Errores -32601 y -32602', 'Fallo del protocolo, no de la herramienta.', 'coral'),
                       ('Faltan argumentos de la herramienta', 'Resultado con isError verdadero', 'Fallo de la herramienta, que el modelo puede leer y corregir.', 'gold')],
                      note='Cómo leer la figura: los tres primeros mensajes son la vida normal de una sesión y los tres últimos son los fallos que distinguen protocolo de herramienta. Dónde deja de valer: es un servidor de demostración con los nombres de métodos del Model Context Protocol, no una implementación conforme de ninguna versión de su especificación.',
                      note_kind='teal', foot=REAL)

def se511_integraciones() -> Fig:
    items = [('Integración a medida, 4 agentes por 6 herramientas', 24, 'coral', '24 conectores'), ('Protocolo común, 4 clientes más 6 servidores', 10, 'teal', '10 adaptadores')]
    return bars('Conectores necesarios con y sin un protocolo común entre agentes y herramientas',
                'Barras con los conectores necesarios para cuatro agentes y seis herramientas: a medida hacen falta 24 y con un protocolo común 10.',
                items, 14.0, label_w=420, width=1040,
                note='Cómo leer la figura: es aritmética, no una medición: el producto crece con ambos lados y la suma con cada uno. Dónde deja de valer: el protocolo común añade un costo de seguridad y de versión que la aritmética no cuenta.', foot='')


def se511_descripciones_con_instrucciones() -> Fig:
    return case_cards('Qué detecta un filtro de descripciones de herramientas y qué impone una máquina de estados de tareas',
                      'Tres pruebas como tarjetas: un filtro por expresión regular sobre seis descripciones con instrucciones ocultas detecta tres y deja pasar tres; sobre seis descripciones benignas da una falsa alarma; una máquina de estados de tarea rechaza 9 246 de 12 000 transiciones al azar y deja pasar 2 754 legales.',
                      [('Descripciones de herramienta con instrucciones ocultas (6 escritas)', 'El filtro por expresión regular detecta 3 y deja pasar 3', 'Las paráfrasis y otros idiomas pasan.', 'coral'),
                       ('Descripciones benignas (6 escritas)', '1 falsa alarma por mencionar una frase de ataque', 'El filtro castiga el texto, no la intención.', 'gold'),
                       ('Transiciones al azar de una tarea entre estados (12 000)', '2 754 legales y 9 246 rechazadas', 'La máquina de estados impide saltos que el protocolo no permite.', 'teal')],
                      note='Cómo leer la figura: un filtro de texto es una capa y no una defensa; las transiciones sí se imponen por construcción. Dónde deja de valer: doce descripciones escritas por el autor; ningún servidor real ni agente de terceros se probó.',
                      note_kind='coral', foot='Experimento propio con la biblioteca estándar; no se invocó ningún modelo de lenguaje.')

# ---------------------------------------------------------------- SE-512
def se512_puntos_de_caida() -> Fig:
    return heatmap('Envíos reales de un aviso que debe salir una sola vez, según la estrategia y el punto de la caída',
                   'Mapa de calor con los envíos reales de un aviso que debe salir una sola vez: reiniciar desde el principio sin diario envía 1, 1, 2 y 2 según no haya caída, caída antes del efecto, tras el efecto antes del diario o tras el diario; el diario de pasos sin clave envía 1, 1, 2 y 1; con clave de idempotencia envía una sola vez en los cuatro casos.',
                   ['Reiniciar desde el principio, sin diario', 'Diario de pasos, sin clave de idempotencia', 'Diario de pasos con clave de idempotencia'], ['Sin caída', 'Antes del efecto', 'Tras el efecto, antes del diario', 'Tras el diario'],
                   [[1, 1, 2, 2], [1, 1, 2, 1], [1, 1, 1, 1]], unit='envíos reales (1 = correcto)', scale='coral', vmin=1, vmax=2, highlight=[(0, 2), (0, 3), (1, 2)], label_w=310,
                   note='El contorno marca los envíos duplicados: el aviso salió dos veces. Cómo leer la figura: el envío duplicado aparece cuando el efecto ocurrió y el diario no lo supo; la clave lo neutraliza en el servicio. Dónde deja de valer: un solo paso con efecto externo, SQLite en memoria y un servicio simulado que respeta la clave; un servicio real puede no hacerlo.',
                   note_kind='coral', foot=REAL)

def se512_tormenta_de_reintentos() -> Fig:
    return grouped_bars('Mil clientes sincronizados reintentan contra un servidor caído durante 5 segundos',
                        'Barras agrupadas con los picos de solicitudes de tres políticas de reintento de mil clientes sincronizados contra un servidor caído cinco segundos: con intervalo fijo el pico por medio segundo es 1 000, también tras la recuperación; con retroceso exponencial sin aleatoriedad 1 000 y 1 000; con jitter completo 1 552 en el primer instante y 145 tras la recuperación.',
                        ['Intervalo fijo de 1 s (6 000 solicitudes)', 'Retroceso exponencial sin aleatoriedad (4 000)', 'Retroceso exponencial con jitter completo (5 061)'],
                        [('Pico por 0,5 s', [1000, 1000, 1552], 'coral'), ('Pico tras la recuperación', [1000, 1000, 145], 'teal')],
                        unit='solicitudes por medio segundo',
                        note='Entre paréntesis, las solicitudes totales. Cómo leer la figura: el retroceso exponencial reduce el volumen pero conserva la sincronía; solo la aleatoriedad reparte la carga de recuperación. Dónde deja de valer: clientes sincronizados desde el instante cero, sin límite de reintentos ni cola en el servidor.',
                        note_kind='gold', foot='Simulación propia con semilla fija; no se invocó ningún modelo de lenguaje.')

def se512_diario_y_clave() -> Fig:
    rows = [[('Leer el diario: ¿el paso ya se hizo?', 'navy'), ('Si sí, saltarlo; si no, ejecutarlo', 'teal'), ('Efecto externo con clave de idempotencia por paso', 'teal')],
            [('Anotar el paso en el diario tras el efecto', 'gold'), ('Caída: reanudar leyendo el diario', 'coral'), ('El servicio ignora la repetición de la misma clave', 'teal')]]
    return flow('Ejecución durable: diario de pasos, reanudación y clave de idempotencia',
                'Diagrama en dos filas. Se lee el diario para saber si el paso ya se hizo, se salta si es así o se ejecuta si no, y el efecto externo lleva una clave de idempotencia por paso. Después se anota el paso en el diario tras el efecto; si hay una caída se reanuda leyendo el diario; y el servicio ignora la repetición de la misma clave.',
                rows, note='Cómo leer la figura: el diario resuelve qué pasos faltan y la clave resuelve el único caso que el diario no puede, la caída entre el efecto y la anotación. Dónde deja de valer: si el servicio externo no acepta claves, hay que consultar su estado antes de repetir.', foot='')


# ---------------------------------------------------------------- SE-513
def se513_puerta_de_mejora() -> Fig:
    ns = [50, 100, 400, 1600]
    return line_chart('Casos de la evaluación frente a falsos positivos y capacidad de detectar una mejora real de unos 4 puntos',
                      'Líneas con el número de casos de una evaluación pareada frente a los falsos positivos sin mejora real y la proporción de veces que detecta una mejora real de unos 4 puntos: los falsos positivos se quedan cerca del 5 por ciento con 5,6, 5,1, 4,8 y 6,8 mientras la detección sube de 10,1 con 50 casos a 15,2, 37,2 y 81,8 con 1 600.',
                      [('Detecta una mejora real de 4 puntos', [(n, v, fmt_es(v, 1), 't') for n, v in zip(ns, [10.1, 15.2, 37.2, 81.8])], 'teal'), ('Falsos positivos sin mejora real', [(n, v, fmt_es(v, 1), 'b') for n, v in zip(ns, [5.6, 5.1, 4.8, 6.8])], 'coral')],
                      x_label='Casos de la evaluación', y_label='Proporción de evaluaciones (%)', log_x=True, x_ticks=[(n, fmt_es(n)) for n in ns], y_ticks=[0, 20, 40, 60, 80, 100],
                      note='Cómo leer la figura: los falsos positivos se quedan cerca del 5 % que fija el umbral, pero con 100 casos la mejora real pasa desapercibida en 85 de cada 100 evaluaciones. Dónde deja de valer: 800 evaluaciones sintéticas por celda con semilla 13 y una prueba z de McNemar de una cola; otros diseños cambian la potencia.',
                      note_kind='gold', foot=SIM)

def se513_juez_y_ruido() -> Fig:
    return case_cards('Ruido de una evaluación: sesgo del juez, variación entre ejecuciones y traza reconstruida',
                      'Tres medidas del ruido de una evaluación como tarjetas: un juez con sesgo de posición de 0,65 elige la primera respuesta el 65,5 por ciento de las veces y se contradice al cruzar el orden el 54,8; treinta ejecuciones del mismo sistema sobre cien casos van del 55,0 al 74,0 por ciento con una desviación de 4,3 puntos; una traza de tres tramos permite reconstruir 730 tokens de entrada, 95 de salida y 1 402 milisegundos.',
                      [('Juez con sesgo de posición 0,65 ante respuestas iguales', 'Elige la primera el 65,5 %; el veredicto se contradice al cruzar el orden el 54,8 %', 'Evaluar en los dos órdenes y exigir coincidencia.', 'coral'),
                       ('30 ejecuciones del mismo sistema sobre 100 casos', 'De 55,0 % a 74,0 %; desviación de 4,3 puntos', 'Una sola ejecución no mide el sistema.', 'coral'),
                       ('Traza JSONL de una ejecución de tres tramos', '730 tokens de entrada, 95 de salida y 1 402 ms', 'Sin traza no se atribuye costo ni falla.', 'teal')],
                      note='Cómo leer la figura: cada fila es una fuente de ruido distinta y cada consecuencia es una práctica de evaluación. Dónde deja de valer: el sesgo y la variación son parámetros simulados; el de un juez real hay que medirlo con casos etiquetados.',
                      note_kind='coral', foot=SIM)

def se513_bucle_de_evals() -> Fig:
    rows = [[('Casos: reales, difíciles y con etiqueta', 'navy'), ('Ejecutar con traza de cada tramo', 'teal'), ('Calificar: código, persona o juez calibrado', 'teal')],
            [('Comparar versiones con intervalo y pareando casos', 'gold'), ('Puerta: umbral y margen decididos antes', 'gold'), ('Tráfico real: fallos nuevos pasan a ser casos', 'coral')]]
    return flow('Bucle de evaluación y operación de un sistema con LLM',
                'Diagrama en dos filas. Primero se reúnen casos reales, difíciles y con etiqueta, se ejecutan con traza de cada tramo y se califican con código, una persona o un juez calibrado. Después se comparan versiones con intervalo y pareando casos, una puerta con umbral y margen decididos antes decide la publicación y los fallos del tráfico real pasan a ser casos nuevos.',
                rows, note='Cómo leer la figura: la última caja devuelve al principio y por eso el conjunto de casos crece con la operación. Dónde deja de valer: con datos personales en los casos, guardar trazas exige minimizar y anonimizar.', foot='')


# ---------------------------------------------------------------- SE-514
def se514_cache_y_costo() -> Fig:
    ps = [1, 3, 5, 10]
    return line_chart('Costo relativo de un bucle de N pasos con y sin caché del prefijo estable',
                      'Líneas con el costo relativo de un bucle según los pasos: sin caché sube de 3 750 con un paso a 12 450, 22 750 y 55 500 con 3, 5 y 10 pasos; con caché de 4 500 a 7 440, 10 540 y 18 990, de modo que cuesta 20 por ciento más con un paso y 40, 54 y 66 por ciento menos con 3, 5 y 10.',
                      [('Sin caché', [(p, v, fmt_es(v), 't') for p, v in zip(ps, [3750, 12450, 22750, 55500])], 'coral'), ('Con caché', [(p, v, fmt_es(v), 'r' if p == 1 else 'b') for p, v in zip(ps, [4500, 7440, 10540, 18990])], 'teal')],
                      x_label='Pasos del bucle', y_label='Costo relativo (unidades de la clase)', x_ticks=[(p, str(p)) for p in ps], y_ticks=[0, 20000, 40000, 60000],
                      note='Diferencia con caché: +20 % con 1 paso, −40 % con 3, −54 % con 5 y −66 % con 10. Cómo leer la figura: sin caché cada paso paga de nuevo todo el historial y el costo crece de forma cuadrática; con caché, el primer paso cuesta más y los siguientes mucho menos. Dónde deja de valer: las unidades son de la clase (salida cinco veces la entrada, lectura de caché 0,1 y escritura 1,25), no precios de ningún proveedor.',
                      note_kind='gold', foot='Modelo de costo propio con supuestos declarados; no son precios ni se invocó ningún modelo de lenguaje.')

def se514_latencia() -> Fig:
    return percentile_intervals('Latencia en segundos de cadenas y paralelos de llamadas con cola larga sintética',
                                'Rangos de latencia en segundos de la mediana al percentil 99: una llamada 1,40, 3,50 y 5,11; tres en cadena 4,63, 7,98 y 10,16; cinco en cadena 7,90, 12,05 y 14,48; ocho en cadena 12,74, 17,97 y 21,00; cinco en paralelo, el máximo, mediana 2,36 y p95 4,76.',
                                [('1 llamada', [1.40, 3.50, 5.11]), ('3 llamadas en cadena', [4.63, 7.98, 10.16]), ('5 llamadas en cadena', [7.90, 12.05, 14.48]), ('8 llamadas en cadena', [12.74, 17.97, 21.00]), ('5 llamadas en paralelo (el máximo)', [2.36, 4.76])],
                                unit='segundos', marks=('Mediana', 'p95', 'p99'), decimals=2, label_w=290,
                                note='El paralelo no tiene p99 medido y una llamada con copia de cobertura reduce el p99 de 4,89 a 2,61 s. Cómo leer la figura: el p95 de una cadena crece más despacio que la mediana por promediarse, pero el de ocho pasos ya supera 18 segundos; el paralelo espera a la más lenta. Dónde deja de valer: distribución log-normal sintética con mediana de 1,2 s y 0,2 s por herramienta; la cola de un proveedor real hay que medirla.',
                                note_kind='teal', foot='Simulación propia con semilla fija; no se invocó ningún modelo de lenguaje.')

def se514_defensas() -> Fig:
    return grouped_bars('Ataques exitosos por inyección y envíos legítimos afectados según la defensa, en 4 000 solicitudes sintéticas',
                        'Barras agrupadas con cuatro defensas: sin defensa el 19,23 por ciento de las solicitudes sufre un ataque exitoso y ningún envío legítimo se afecta; con lista de destinatarios permitidos 3,02 y 0; con confirmación humana 7,42 por ciento de ataques y se retrasa el 25 por ciento de los envíos; sin canal de salida si hay contenido no confiable 0,00 y se bloquea el 49 por ciento.',
                        ['Ninguna', 'Lista de destinatarios', 'Confirmación humana', 'Sin canal de salida'],
                        [('Ataques exitosos', [19.23, 3.02, 7.42, 0.0], 'coral'), ('Envíos legítimos afectados', [0.0, 0.0, 25.0, 49.0], 'gold')],
                        unit='% de las solicitudes', decimals=2,
                        note='Con la confirmación humana el 25 % de los envíos se retrasa y sin canal de salida se bloquea el 49 %. Cómo leer la figura: ninguna defensa es gratuita; la que elimina el ataque elimina también la capacidad que lo hace posible. Dónde deja de valer: el modelo obedece la instrucción inyectada con probabilidad 0,40 y la fatiga humana aprueba el 35 %; ambos son supuestos del autor.',
                        note_kind='coral', foot=SIM)

# ---------------------------------------------------------------- SE-515
def se515_selector() -> Fig:
    return case_cards('Selector de patrón agéntico: seis de las ocho tareas con la decisión que toma el código',
                      'Seis situaciones y el patrón que elige el selector como tarjetas: pasos conocidos sin herramientas una llamada; con herramientas un workflow encadenado; con partes independientes un workflow paralelo; camino impredecible con presupuesto y tiempo amplios un agente; camino impredecible con poco presupuesto enrutamiento a un workflow; y acción irreversible sin aprobación una persona decide.',
                      [('Pasos conocidos, sin herramientas', 'Una llamada', 'El patrón más simple que alcanza.', 'teal'), ('Pasos conocidos con herramientas', 'Workflow encadenado', 'El código decide el orden.', 'teal'),
                       ('Pasos conocidos y partes independientes', 'Workflow paralelo', 'Las partes no se esperan.', 'teal'), ('Camino impredecible, herramientas, presupuesto y tiempo amplios', 'Agente', 'El modelo decide el siguiente paso.', 'gold'),
                       ('Camino impredecible, pero poco presupuesto', 'Enrutamiento a workflow', 'Se limita la autonomía al presupuesto.', 'gold'), ('Acción irreversible sin aprobación', 'Persona decide', 'Ningún patrón automático sustituye la aprobación.', 'coral')],
                      note='Cómo leer la figura: el selector coincide con la decisión escrita a mano en 8 de 8 tareas, dos de ellas no mostradas; la coincidencia prueba que la regla es consistente, no que sea correcta. Dónde deja de valer: las ocho tareas las escribió el autor al mismo tiempo que la regla.',
                      note_kind='gold', foot='Selector propio en Python; no se invocó ningún modelo de lenguaje.')

def se515_incidente() -> Fig:
    return grouped_bars('Mil solicitudes con un incidente del proveedor: política fija frente a degradación a un workflow',
                        'Barras horizontales con las solicitudes resueltas de mil con un incidente del proveedor: con agente fijo resuelve el 60,4 por ciento con 5,42 llamadas por solicitud y un p95 de 24,9 segundos; con degradación a un workflow resuelve el 70,7 por ciento con 3,67 llamadas, un p95 de 13,7 segundos y 420 solicitudes degradadas.',
                        ['Agente fijo (5,42 llamadas · p95 24,9 s · 0 degradadas)', 'Con degradación a workflow (3,67 llamadas · p95 13,7 s · 420 degradadas)'],
                        [('Solicitudes resueltas', [60.4, 70.7], 'teal')],
                        unit='% de solicitudes resueltas', horizontal=True, label_w=360, decimals=1, ticks=[0, 25, 50, 75, 100],
                        note='Entre paréntesis, las llamadas por solicitud, el p95 de latencia y las solicitudes degradadas. Cómo leer la figura: degradar cuesta calidad en lo que el workflow no sabe hacer, pero corta la espera y el gasto en reintentos. Dónde deja de valer: el interruptor abre con 6 fallos de las últimas 20 y se sondea cada 20 solicitudes; esos umbrales son del autor y el costo de la calidad perdida no está en el gráfico.',
                        note_kind='teal', foot=SIM)

def se515_escalera() -> Fig:
    rows = [[('Agente con presupuesto de pasos', 'teal'), ('Workflow fijo con los mismos permisos', 'teal'), ('Plantilla o respuesta guardada', 'gold')],
            [('Cola para una persona con el contexto', 'coral'), ('Disparadores: errores, costo, latencia, confianza', 'navy'), ('Vuelta al nivel superior tras sondas correctas', 'teal')]]
    return flow('Escalera de degradación de un sistema con LLM y los disparadores que bajan o suben de nivel',
                'Diagrama en dos filas. La escalera baja del agente con presupuesto de pasos al workflow fijo con los mismos permisos, a una plantilla o respuesta guardada y a una cola para una persona con el contexto. Los disparadores son errores, costo, latencia y confianza, y la vuelta al nivel superior ocurre tras sondas correctas.',
                rows, note='Cómo leer la figura: cada escalón pierde capacidad y gana previsibilidad. Dónde deja de valer: la escalera exige que cada nivel inferior exista y se pruebe antes del incidente.', foot='')


# ---------------------------------------------------------------- SE-516
def se516_puerta_de_entrada() -> Fig:
    return case_cards('Puerta de entrada a producción aplicada a cuatro candidatos del sistema de Avisos',
                      'Cuatro candidatos frente a una puerta de calidad de al menos 97 por ciento, tokens hasta 1 500, p95 hasta 20 segundos, ataques hasta 0,5 por ciento y envíos tras una caída hasta uno: el agente solo cumple la calidad pero no los tokens ni los ataques; el workflow solo no cumple la calidad ni los ataques; el híbrido sin gobierno no cumple los ataques ni los envíos duplicados; el híbrido gobernado cumple todo y pasa.',
                      [('Agente solo', 'NO PASA: calidad 97,5 %, 1 862 tokens, p95 18,0 s, ataques 19,23 %, 2 envíos', 'Cumple la calidad; falla tokens y ataques.', 'coral'),
                       ('Workflow solo', 'NO PASA: calidad 85,0 %, 774 tokens, p95 5,8 s, ataques 19,23 %, 2 envíos', 'Falla la calidad y los ataques.', 'coral'),
                       ('Híbrido sin gobierno', 'NO PASA: calidad 99,0 %, 1 421 tokens, p95 18,0 s, ataques 19,23 %, 2 envíos', 'Falla los ataques y los envíos duplicados.', 'coral'),
                       ('Híbrido gobernado', 'PASA: calidad 99,0 %, 1 421 tokens, p95 18,0 s, ataques 0,00 %, 1 envío', 'Cumple todos los umbrales.', 'teal')],
                      note='Cómo leer la figura: la puerta se decidió antes de medir y cada columna viene de un experimento de una clase anterior. Dónde deja de valer: los candidatos son configuraciones sintéticas; el p95 combina la cadena de 8 llamadas medida y no una ejecución del sistema completo.',
                      note_kind='gold', foot=SIM)

def se516_arquitectura() -> Fig:
    rows = [[('Solicitud con presupuesto y permisos', 'navy'), ('Enrutador: workflow, agente o persona', 'teal'), ('Agente acotado o workflow, con herramientas por protocolo', 'teal')],
            [('Diario durable e idempotencia por paso', 'gold'), ('Trazas y evaluaciones con puerta de release', 'gold'), ('Degradación, interruptor y escalado a persona', 'coral')]]
    return flow('Arquitectura del sistema con LLM evaluado y operable del proyecto',
                'Diagrama en dos filas. Una solicitud con presupuesto y permisos llega a un enrutador que elige workflow, agente o persona y a un agente acotado o workflow cuyas herramientas se conectan por protocolo. Después un diario durable con idempotencia por paso, trazas y evaluaciones con puerta de release, y degradación con interruptor y escalado a una persona.',
                rows, note='Cómo leer la figura: la primera fila ejecuta y la segunda hace al sistema repetible, medible y reversible. Dónde deja de valer: es un esquema mínimo; un sistema real añade autenticación, cuotas por usuario y retención de datos.', foot='')


def se516_evidencia() -> Fig:
    return case_cards('Evidencia que el proyecto reutiliza de cada clase de la parte',
                      'Seis criterios del proyecto y la evidencia medida que cada uno reutiliza como tarjetas: elegir el patrón usa la comparación de workflow y agente de la clase 505; limitar el contexto usa la memoria versionada de la 509; recuperar con respaldo usa BM25 y abstención de la 510; no repetir efectos usa el diario con clave de la 512; decidir con evidencia usa la puerta con 400 casos de la 513; y contener el daño usa el resultado sin canal de salida de la 514.',
                      [('Elegir el patrón', 'Workflow fijo frente a agente por tipo de solicitud', 'Clase SE-505.', 'teal'), ('Limitar el contexto', 'Memoria versionada: 95,2 % frente a 40,8 %', 'Clase SE-509.', 'teal'),
                       ('Recuperar con respaldo', 'BM25 y abstención con umbral', 'Clase SE-510.', 'teal'), ('No repetir efectos', 'Envíos tras caída: 1 con diario y clave', 'Clase SE-512.', 'teal'),
                       ('Decidir con evidencia', 'Puerta con 400 casos o más para mejoras de 4 puntos', 'Clase SE-513.', 'teal'), ('Contener el daño', '0,00 % de ataques sin canal de salida', 'Clase SE-514.', 'teal')],
                      note='Cómo leer la figura: el proyecto no inventa medidas, recompone las de la parte con su caso. Dónde deja de valer: cada medida vale para el experimento que la produjo; recomponerlas no prueba que el sistema completo las conserve.',
                      note_kind='teal', foot='')

FIGURES = {
    "se-511-protocolo-por-stdio.svg": se511_protocolo_por_stdio,
    "se-511-integraciones.svg": se511_integraciones,
    "se-511-descripciones-con-instrucciones.svg": se511_descripciones_con_instrucciones,
    "se-512-puntos-de-caida.svg": se512_puntos_de_caida,
    "se-512-tormenta-de-reintentos.svg": se512_tormenta_de_reintentos,
    "se-512-diario-y-clave.svg": se512_diario_y_clave,
    "se-513-puerta-de-mejora.svg": se513_puerta_de_mejora,
    "se-513-juez-y-ruido.svg": se513_juez_y_ruido,
    "se-513-bucle-de-evals.svg": se513_bucle_de_evals,
    "se-514-cache-y-costo.svg": se514_cache_y_costo,
    "se-514-latencia.svg": se514_latencia,
    "se-514-defensas.svg": se514_defensas,
    "se-515-selector.svg": se515_selector,
    "se-515-incidente.svg": se515_incidente,
    "se-515-escalera.svg": se515_escalera,
    "se-516-puerta-de-entrada.svg": se516_puerta_de_entrada,
    "se-516-arquitectura.svg": se516_arquitectura,
    "se-516-evidencia.svg": se516_evidencia,
}
