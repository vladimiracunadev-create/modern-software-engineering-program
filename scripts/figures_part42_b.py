"""Figures for SE-511 to SE-516 (agentic patterns and LLM systems: real JSON-RPC process, SQLite journal with injected crashes, statistical gates over synthetic results, capability policy; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab
from figures_part40_a import bars, flow

SIM = "Experimento propio con la biblioteca estándar; el modelo es sintético con semilla fija y no se invocó ningún modelo de lenguaje."
REAL = "Procesos, diario SQLite y mensajes reales en un directorio temporal; no se invocó ningún modelo de lenguaje."


# ---------------------------------------------------------------- SE-511
def se511_protocolo_por_stdio() -> Fig:
    rows = [['initialize', 'Responde nombre y versión del servidor', 'Primera llamada de cualquier sesión'],
            ['tools/list', 'Devuelve 2 herramientas con su esquema de entrada', 'El agente descubre qué puede hacer'],
            ['tools/call con curso c1', 'Devuelve la fecha 2026-11-20', 'Mediana de 0,10 ms por ida y vuelta (reloj real)'],
            ['JSON roto', 'Error -32700', 'El servidor sigue vivo y responde al siguiente'],
            ['Método inexistente o parámetros inválidos', 'Errores -32601 y -32602', 'Fallo del protocolo, no de la herramienta'],
            ['Faltan argumentos de la herramienta', 'Resultado con isError verdadero', 'Fallo de la herramienta, que el modelo puede leer y corregir']]
    return tab('Un servidor JSON-RPC por entrada y salida estándar en un proceso real: qué responde a cada mensaje',
               'Tabla con seis mensajes a un servidor real de dos herramientas. initialize devuelve nombre y versión del servidor; tools/list devuelve dos herramientas con su esquema; tools/call con el curso c1 devuelve la fecha 2026-11-20 con una mediana de 0,10 milisegundos; un JSON roto devuelve el error -32700; un método inexistente y unos parámetros inválidos devuelven -32601 y -32602; y unos argumentos faltantes devuelven un resultado con isError verdadero.',
               ['Mensaje', 'Respuesta observada', 'Qué enseña'], rows, [270, 330, 370], row_h=60, size=13,
               note='Cómo leer la figura: los tres primeros mensajes son la vida normal de una sesión y los tres últimos son los fallos que distinguen protocolo de herramienta. Dónde deja de valer: es un servidor de demostración con los nombres de métodos del Model Context Protocol, no una implementación conforme de ninguna versión de su especificación.',
               note_kind='teal', foot=REAL)


def se511_integraciones() -> Fig:
    items = [('Integración a medida, 4 agentes por 6 herramientas', 24, 'coral', '24 conectores'), ('Protocolo común, 4 clientes más 6 servidores', 10, 'teal', '10 adaptadores')]
    return bars('Conectores necesarios con y sin un protocolo común entre agentes y herramientas',
                'Barras con los conectores necesarios para cuatro agentes y seis herramientas: a medida hacen falta 24 y con un protocolo común 10.',
                items, 14.0, label_w=420, width=1040,
                note='Cómo leer la figura: es aritmética, no una medición: el producto crece con ambos lados y la suma con cada uno. Dónde deja de valer: el protocolo común añade un costo de seguridad y de versión que la aritmética no cuenta.', foot='')


def se511_descripciones_con_instrucciones() -> Fig:
    rows = [['Descripciones de herramienta con instrucciones ocultas (6 escritas)', 'El filtro por expresión regular detecta 3 y deja pasar 3', 'Las paráfrasis y otros idiomas pasan'],
            ['Descripciones benignas (6 escritas)', '1 falsa alarma por mencionar una frase de ataque', 'El filtro castiga el texto, no la intención'],
            ['Transiciones al azar de una tarea entre estados (12 000)', '2 754 legales y 9 246 rechazadas', 'La máquina de estados impide saltos que el protocolo no permite']]
    return tab('Qué detecta un filtro de descripciones de herramientas y qué impone una máquina de estados de tareas',
               'Tabla con tres pruebas. Un filtro por expresión regular sobre seis descripciones con instrucciones ocultas detecta tres y deja pasar tres; sobre seis descripciones benignas da una falsa alarma. Una máquina de estados de tarea rechaza 9 246 de 12 000 transiciones al azar y deja pasar 2 754 legales.',
               ['Prueba', 'Resultado', 'Lectura'], rows, [380, 330, 260], row_h=76, size=13,
               note='Cómo leer la figura: un filtro de texto es una capa y no una defensa; las transiciones sí se imponen por construcción. Dónde deja de valer: doce descripciones escritas por el autor; ningún servidor real ni agente de terceros se probó.',
               note_kind='coral', foot='Experimento propio con la biblioteca estándar; no se invocó ningún modelo de lenguaje.')


# ---------------------------------------------------------------- SE-512
def se512_puntos_de_caida() -> Fig:
    rows = [['Reiniciar desde el principio, sin diario', '1', '1', '2', '2'], ['Diario de pasos, sin clave de idempotencia', '1', '1', '2', '1'], ['Diario de pasos con clave de idempotencia', '1', '1', '1', '1']]
    return tab('Envíos reales de un aviso que debe salir una sola vez, según la estrategia y el punto de la caída',
               'Tabla con los envíos reales de un aviso que debe salir una sola vez. Reiniciar desde el principio sin diario envía 1, 1, 2 y 2 según no haya caída, caída antes del efecto, tras el efecto antes del diario o tras el diario. El diario de pasos sin clave envía 1, 1, 2 y 1. El diario con clave de idempotencia envía una sola vez en los cuatro casos.',
               ['Estrategia', 'Sin caída', 'Antes del efecto', 'Tras el efecto, antes del diario', 'Tras el diario'], rows, [330, 110, 150, 230, 140], row_h=64, size=13,
               note='Cómo leer la figura: el envío duplicado aparece cuando el efecto ocurrió y el diario no lo supo; la clave lo neutraliza en el servicio. Dónde deja de valer: un solo paso con efecto externo, SQLite en memoria y un servicio simulado que respeta la clave; un servicio real puede no hacerlo.',
               note_kind='coral', foot=REAL)


def se512_tormenta_de_reintentos() -> Fig:
    rows = [['Intervalo fijo de 1 s', '6 000', '1 000', '1 000'], ['Retroceso exponencial sin aleatoriedad', '4 000', '1 000', '1 000'], ['Retroceso exponencial con jitter completo', '5 061', '1 552', '145']]
    return tab('Mil clientes sincronizados reintentan contra un servidor caído durante 5 segundos',
               'Tabla con tres políticas de reintento de mil clientes sincronizados contra un servidor caído cinco segundos. Con intervalo fijo de un segundo hay 6 000 solicitudes y un pico de 1 000 por medio segundo, también tras la recuperación. Con retroceso exponencial sin aleatoriedad hay 4 000 solicitudes y los mismos picos de 1 000. Con jitter completo hay 5 061 solicitudes, un pico máximo de 1 552 en el primer instante y 145 tras la recuperación.',
               ['Política de reintento', 'Solicitudes totales', 'Pico por 0,5 s', 'Pico tras la recuperación'], rows, [380, 190, 190, 210], row_h=56, size=13,
               note='Cómo leer la figura: el retroceso exponencial reduce el volumen pero conserva la sincronía; solo la aleatoriedad reparte la carga de recuperación. Dónde deja de valer: clientes sincronizados desde el instante cero, sin límite de reintentos ni cola en el servidor.',
               note_kind='gold', foot='Simulación propia con semilla fija; no se invocó ningún modelo de lenguaje.')


def se512_diario_y_clave() -> Fig:
    rows = [[('Leer el diario: ¿el paso ya se hizo?', 'navy'), ('Si sí, saltarlo; si no, ejecutarlo', 'teal'), ('Efecto externo con clave de idempotencia por paso', 'teal')],
            [('Anotar el paso en el diario tras el efecto', 'gold'), ('Caída: reanudar leyendo el diario', 'coral'), ('El servicio ignora la repetición de la misma clave', 'teal')]]
    return flow('Ejecución durable: diario de pasos, reanudación y clave de idempotencia',
                'Diagrama en dos filas. Se lee el diario para saber si el paso ya se hizo, se salta si es así o se ejecuta si no, y el efecto externo lleva una clave de idempotencia por paso. Después se anota el paso en el diario tras el efecto; si hay una caída se reanuda leyendo el diario; y el servicio ignora la repetición de la misma clave.',
                rows, note='Cómo leer la figura: el diario resuelve qué pasos faltan y la clave resuelve el único caso que el diario no puede, la caída entre el efecto y la anotación. Dónde deja de valer: si el servicio externo no acepta claves, hay que consultar su estado antes de repetir.', foot='')


# ---------------------------------------------------------------- SE-513
def se513_puerta_de_mejora() -> Fig:
    rows = [['50', '5,6 %', '10,1 %'], ['100', '5,1 %', '15,2 %'], ['400', '4,8 %', '37,2 %'], ['1 600', '6,8 %', '81,8 %']]
    return tab('Casos de la evaluación frente a falsos positivos y capacidad de detectar una mejora real de unos 4 puntos',
               'Tabla con el número de casos de una evaluación pareada, los falsos positivos sin mejora real y la proporción de veces que detecta una mejora real de unos 4 puntos. Con 50 casos 5,6 por ciento y 10,1; con 100, 5,1 y 15,2; con 400, 4,8 y 37,2; con 1 600, 6,8 y 81,8.',
               ['Casos', 'Falsos positivos sin mejora real', 'Detecta una mejora real de 4 puntos'], rows, [160, 380, 430], row_h=50, size=13,
               note='Cómo leer la figura: los falsos positivos se quedan cerca del 5 % que fija el umbral, pero con 100 casos la mejora real pasa desapercibida en 85 de cada 100 evaluaciones. Dónde deja de valer: 800 evaluaciones sintéticas por celda con semilla 13 y una prueba z de McNemar de una cola; otros diseños cambian la potencia.',
               note_kind='gold', foot=SIM)


def se513_juez_y_ruido() -> Fig:
    rows = [['Juez con sesgo de posición 0,65 ante respuestas iguales', 'Elige la primera el 65,5 %; el veredicto se contradice al cruzar el orden el 54,8 %', 'Evaluar en los dos órdenes y exigir coincidencia'],
            ['30 ejecuciones del mismo sistema sobre 100 casos', 'De 55,0 % a 74,0 %; desviación de 4,3 puntos', 'Una sola ejecución no mide el sistema'],
            ['Traza JSONL de una ejecución de tres tramos', '730 tokens de entrada, 95 de salida y 1 402 ms', 'Sin traza no se atribuye costo ni falla']]
    return tab('Ruido de una evaluación: sesgo del juez, variación entre ejecuciones y traza reconstruida',
               'Tabla con tres medidas del ruido de una evaluación. Un juez con sesgo de posición de 0,65 elige la primera respuesta el 65,5 por ciento de las veces y se contradice al cruzar el orden el 54,8. Treinta ejecuciones del mismo sistema sobre cien casos van del 55,0 al 74,0 por ciento con una desviación de 4,3 puntos. Una traza de tres tramos permite reconstruir 730 tokens de entrada, 95 de salida y 1 402 milisegundos.',
               ['Medida', 'Resultado', 'Consecuencia'], rows, [330, 380, 260], row_h=84, size=13,
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
    rows = [['1', '3 750', '4 500', 'cuesta 20 % más'], ['3', '12 450', '7 440', '40 % menos'], ['5', '22 750', '10 540', '54 % menos'], ['10', '55 500', '18 990', '66 % menos']]
    return tab('Costo relativo de un bucle de N pasos con y sin caché del prefijo estable',
               'Tabla con el costo relativo de un bucle según los pasos. Con un paso cuesta 3 750 sin caché y 4 500 con caché, 20 por ciento más. Con tres pasos 12 450 y 7 440, 40 por ciento menos. Con cinco 22 750 y 10 540, 54 por ciento menos. Con diez 55 500 y 18 990, 66 por ciento menos.',
               ['Pasos del bucle', 'Sin caché', 'Con caché', 'Diferencia'], rows, [210, 230, 230, 300], row_h=50, size=13,
               note='Cómo leer la figura: sin caché cada paso paga de nuevo todo el historial y el costo crece de forma cuadrática; con caché, el primer paso cuesta más y los siguientes mucho menos. Dónde deja de valer: las unidades son de la clase (salida cinco veces la entrada, lectura de caché 0,1 y escritura 1,25), no precios de ningún proveedor.',
               note_kind='gold', foot='Modelo de costo propio con supuestos declarados; no son precios ni se invocó ningún modelo de lenguaje.')


def se514_latencia() -> Fig:
    rows = [['1 llamada', '1,40', '3,50', '5,11'], ['3 llamadas en cadena', '4,63', '7,98', '10,16'], ['5 llamadas en cadena', '7,90', '12,05', '14,48'], ['8 llamadas en cadena', '12,74', '17,97', '21,00'],
            ['5 llamadas en paralelo (el máximo)', '2,36', '4,76', 'sin medir'], ['1 llamada con copia de cobertura', 'sin medir', 'sin medir', '2,61 frente a 4,89']]
    return tab('Latencia en segundos de cadenas y paralelos de llamadas con cola larga sintética',
               'Tabla con la latencia en segundos. Una llamada: mediana 1,40, p95 3,50 y p99 5,11. Tres en cadena: 4,63, 7,98 y 10,16. Cinco en cadena: 7,90, 12,05 y 14,48. Ocho en cadena: 12,74, 17,97 y 21,00. Cinco en paralelo, el máximo: mediana 2,36 y p95 4,76. Una llamada con copia de cobertura reduce el p99 de 4,89 a 2,61.',
               ['Estructura', 'Mediana', 'p95', 'p99'], rows, [400, 150, 150, 270], row_h=46, size=13,
               note='Cómo leer la figura: el p95 de una cadena crece más despacio que la mediana por promediarse, pero el de ocho pasos ya supera 18 segundos; el paralelo espera a la más lenta. Dónde deja de valer: distribución log-normal sintética con mediana de 1,2 s y 0,2 s por herramienta; la cola de un proveedor real hay que medirla.',
               note_kind='teal', foot='Simulación propia con semilla fija; no se invocó ningún modelo de lenguaje.')


def se514_defensas() -> Fig:
    rows = [['Ninguna', '19,23 %', '0 %'], ['Lista de destinatarios permitidos', '3,02 %', '0 %'], ['Confirmación humana antes de enviar', '7,42 %', '25 % se retrasa'], ['Sin canal de salida si hay contenido no confiable', '0,00 %', '49 % bloqueado']]
    return tab('Ataques exitosos por inyección y envíos legítimos afectados según la defensa, en 4 000 solicitudes sintéticas',
               'Tabla con cuatro defensas. Sin defensa el 19,23 por ciento de las solicitudes sufre un ataque exitoso y ningún envío legítimo se afecta. Con lista de destinatarios permitidos 3,02 por ciento y 0. Con confirmación humana 7,42 por ciento y el 25 por ciento de los envíos se retrasa. Sin canal de salida si hay contenido no confiable 0,00 por ciento y se bloquea el 49 por ciento de los envíos legítimos.',
               ['Defensa', 'Ataques exitosos', 'Envíos legítimos afectados'], rows, [430, 230, 310], row_h=56, size=13,
               note='Cómo leer la figura: ninguna defensa es gratuita; la que elimina el ataque elimina también la capacidad que lo hace posible. Dónde deja de valer: el modelo obedece la instrucción inyectada con probabilidad 0,40 y la fatiga humana aprueba el 35 %; ambos son supuestos del autor.',
               note_kind='coral', foot=SIM)


# ---------------------------------------------------------------- SE-515
def se515_selector() -> Fig:
    rows = [['Pasos conocidos, sin herramientas', 'Una llamada'], ['Pasos conocidos con herramientas', 'Workflow encadenado'], ['Pasos conocidos y partes independientes', 'Workflow paralelo'],
            ['Camino impredecible, herramientas, presupuesto y tiempo amplios', 'Agente'], ['Camino impredecible, pero poco presupuesto', 'Enrutamiento a workflow'], ['Acción irreversible sin aprobación', 'Persona decide']]
    return tab('Selector de patrón agéntico: seis de las ocho tareas con la decisión que toma el código',
               'Tabla con seis situaciones y el patrón que elige el selector: pasos conocidos sin herramientas una llamada; con herramientas un workflow encadenado; con partes independientes un workflow paralelo; camino impredecible con presupuesto y tiempo amplios un agente; camino impredecible con poco presupuesto enrutamiento a un workflow; y acción irreversible sin aprobación una persona decide.',
               ['Situación de la tarea', 'Patrón elegido'], rows, [560, 410], row_h=48, size=13,
               note='Cómo leer la figura: el selector coincide con la decisión escrita a mano en 8 de 8 tareas, dos de ellas no mostradas; la coincidencia prueba que la regla es consistente, no que sea correcta. Dónde deja de valer: las ocho tareas las escribió el autor al mismo tiempo que la regla.',
               note_kind='gold', foot='Selector propio en Python; no se invocó ningún modelo de lenguaje.')


def se515_incidente() -> Fig:
    rows = [['Agente fijo', '60,4 %', '5,42', '24,9 s', '0'], ['Con degradación a workflow', '70,7 %', '3,67', '13,7 s', '420']]
    return tab('Mil solicitudes con un incidente del proveedor: política fija frente a degradación a un workflow',
               'Tabla con mil solicitudes de las que las 300 a 600 sufren un 40 por ciento de errores del proveedor. Con agente fijo resuelve el 60,4 por ciento, hace 5,42 llamadas por solicitud, tiene un p95 de 24,9 segundos y degrada 0. Con degradación a un workflow resuelve el 70,7 por ciento, hace 3,67 llamadas, tiene un p95 de 13,7 segundos y degrada 420 solicitudes.',
               ['Política', 'Resueltas', 'Llamadas por solicitud', 'p95 de latencia', 'Solicitudes degradadas'], rows, [300, 140, 190, 170, 170], row_h=56, size=13,
               note='Cómo leer la figura: degradar cuesta calidad en lo que el workflow no sabe hacer, pero corta la espera y el gasto en reintentos. Dónde deja de valer: el interruptor abre con 6 fallos de las últimas 20 y se sondea cada 20 solicitudes; esos umbrales son del autor y el costo de la calidad perdida no está en la tabla.',
               note_kind='teal', foot=SIM)


def se515_escalera() -> Fig:
    rows = [[('Agente con presupuesto de pasos', 'teal'), ('Workflow fijo con los mismos permisos', 'teal'), ('Plantilla o respuesta guardada', 'gold')],
            [('Cola para una persona con el contexto', 'coral'), ('Disparadores: errores, costo, latencia, confianza', 'navy'), ('Vuelta al nivel superior tras sondas correctas', 'teal')]]
    return flow('Escalera de degradación de un sistema con LLM y los disparadores que bajan o suben de nivel',
                'Diagrama en dos filas. La escalera baja del agente con presupuesto de pasos al workflow fijo con los mismos permisos, a una plantilla o respuesta guardada y a una cola para una persona con el contexto. Los disparadores son errores, costo, latencia y confianza, y la vuelta al nivel superior ocurre tras sondas correctas.',
                rows, note='Cómo leer la figura: cada escalón pierde capacidad y gana previsibilidad. Dónde deja de valer: la escalera exige que cada nivel inferior exista y se pruebe antes del incidente.', foot='')


# ---------------------------------------------------------------- SE-516
def se516_puerta_de_entrada() -> Fig:
    rows = [['Agente solo', '97,5 %', '1 862', '18,0 s', '19,23 %', '2', 'NO PASA'], ['Workflow solo', '85,0 %', '774', '5,8 s', '19,23 %', '2', 'NO PASA'],
            ['Híbrido sin gobierno', '99,0 %', '1 421', '18,0 s', '19,23 %', '2', 'NO PASA'], ['Híbrido gobernado', '99,0 %', '1 421', '18,0 s', '0,00 %', '1', 'PASA']]
    return tab('Puerta de entrada a producción aplicada a cuatro candidatos del sistema de Avisos',
               'Tabla con cuatro candidatos y una puerta de calidad de al menos 97 por ciento, tokens hasta 1 500, p95 hasta 20 segundos, ataques hasta 0,5 por ciento y envíos tras una caída hasta uno. El agente solo cumple la calidad pero no los tokens ni los ataques; el workflow solo no cumple la calidad ni los ataques; el híbrido sin gobierno no cumple los ataques ni los envíos duplicados; el híbrido gobernado cumple todo y pasa.',
               ['Candidato', 'Calidad', 'Tokens', 'p95', 'Ataques', 'Envíos tras caída', 'Puerta'], rows, [200, 110, 100, 100, 120, 170, 130], row_h=52, size=13,
               note='Cómo leer la figura: la puerta se decidió antes de medir y cada columna viene de un experimento de una clase anterior. Dónde deja de valer: los candidatos son configuraciones sintéticas; el p95 combina la cadena de 8 llamadas medida y no una ejecución del sistema completo.',
               note_kind='gold', foot=SIM)


def se516_arquitectura() -> Fig:
    rows = [[('Solicitud con presupuesto y permisos', 'navy'), ('Enrutador: workflow, agente o persona', 'teal'), ('Agente acotado o workflow, con herramientas por protocolo', 'teal')],
            [('Diario durable e idempotencia por paso', 'gold'), ('Trazas y evaluaciones con puerta de release', 'gold'), ('Degradación, interruptor y escalado a persona', 'coral')]]
    return flow('Arquitectura del sistema con LLM evaluado y operable del proyecto',
                'Diagrama en dos filas. Una solicitud con presupuesto y permisos llega a un enrutador que elige workflow, agente o persona y a un agente acotado o workflow cuyas herramientas se conectan por protocolo. Después un diario durable con idempotencia por paso, trazas y evaluaciones con puerta de release, y degradación con interruptor y escalado a una persona.',
                rows, note='Cómo leer la figura: la primera fila ejecuta y la segunda hace al sistema repetible, medible y reversible. Dónde deja de valer: es un esquema mínimo; un sistema real añade autenticación, cuotas por usuario y retención de datos.', foot='')


def se516_evidencia() -> Fig:
    rows = [['Elegir el patrón', 'Workflow fijo frente a agente por tipo de solicitud', 'SE-505'], ['Limitar el contexto', 'Memoria versionada: 95,2 % frente a 40,8 %', 'SE-509'], ['Recuperar con respaldo', 'BM25 y abstención con umbral', 'SE-510'],
            ['No repetir efectos', 'Envíos tras caída: 1 con diario y clave', 'SE-512'], ['Decidir con evidencia', 'Puerta con 400 casos o más para mejoras de 4 puntos', 'SE-513'], ['Contener el daño', '0,00 % de ataques sin canal de salida', 'SE-514']]
    return tab('Evidencia que el proyecto reutiliza de cada clase de la parte',
               'Tabla con seis criterios del proyecto y la evidencia medida que cada uno reutiliza: elegir el patrón usa la comparación de workflow y agente de la clase 505; limitar el contexto usa la memoria versionada de la 509; recuperar con respaldo usa BM25 y abstención de la 510; no repetir efectos usa el diario con clave de la 512; decidir con evidencia usa la puerta con 400 casos de la 513; y contener el daño usa el resultado sin canal de salida de la 514.',
               ['Criterio del proyecto', 'Evidencia que se reutiliza', 'Clase'], rows, [250, 600, 120], row_h=50, size=13,
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
