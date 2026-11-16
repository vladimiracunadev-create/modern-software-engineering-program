"""Figures for SE-529 to SE-534 (architectural styles: runs of real CPython code and seeded models over the Avisos case; Windows CPython 3.12.9; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab
from figures_part40_a import bars, flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9; los recuentos se repiten y los tiempos varían de un equipo a otro."
MODELO = "Modelo con parámetros del autor y semilla fija 44; muestra un mecanismo, no mide un sistema real."


# ---------------------------------------------------------------- SE-529
def se529_cuatro_contextos() -> Fig:
    rows = [['Equipo de 6, producto nuevo', 'Monolito modular', '4,00', 'Monolito en capas', '0,35'],
            ['12 equipos, 120 personas', 'Microservicios', '3,45', 'Arquitectura celular', '0,30'],
            ['Plataforma con extensiones de terceros', 'Microkernel', '3,75', 'Microservicios', '0,65'],
            ['Crítico y multi-inquilino', 'Arquitectura celular', '3,50', 'Microservicios', '0,20']]
    return tab('Cuatro contextos, cuatro estilos distintos: la misma matriz de valoraciones con pesos de cada contexto',
               'Tabla con cuatro contextos de decisión y el estilo que gana en cada uno con la misma matriz de seis estilos y siete atributos: un equipo de seis gana el monolito modular con 4,00 puntos, doce equipos ganan los microservicios con 3,45, una plataforma con extensiones de terceros gana el microkernel con 3,75 y un sistema crítico y multi-inquilino gana la arquitectura celular con 3,50; las diferencias con el segundo van de 0,20 a 0,65.',
               ['Contexto', 'Ganador', 'Puntaje', 'Segundo', 'Diferencia'], rows, [330, 210, 90, 210, 110], row_h=60, size=13,
               note='La matriz de valoraciones es la misma en los cuatro casos; solo cambian los pesos. Cuatro estilos distintos ganan, y en el contexto crítico la ventaja sobre el segundo es de 0,20 puntos, menos que el margen de error de un juicio de 1 a 5. Las valoraciones y los pesos los fijó el autor.',
               note_kind='gold', foot=MODELO)


def se529_de_fuerza_a_estilo() -> Fig:
    return flow('De una fuerza de calidad a un estilo: el camino que recorre una decisión arquitectónica',
                'Diagrama de cuatro cajas encadenadas: una fuerza de calidad expresada como escenario con medida, una táctica que la atiende, el estilo que agrupa tácticas compatibles y el costo que el equipo acepta al elegirlo; una nota advierte que sin el escenario la elección es una preferencia.',
                [[('Fuerza\nEscenario con medida: p99 de 200 ms, 99,9 % de disponibilidad', 'teal'), ('Táctica\nCaché, réplica, aislamiento, desacople por cola', 'gold'),
                  ('Estilo\nConjunto de tácticas y restricciones que se refuerzan', 'teal'), ('Costo aceptado\nLo que se pierde: latencia, simplicidad, coordinación', 'coral')]],
                note='Un estilo es una respuesta empaquetada a un conjunto de fuerzas. Si la fuerza no tiene medida, la elección del estilo no se puede refutar: es una preferencia.',
                note_kind='teal', box_h=118, foot=MODELO)


def se529_victorias_por_estilo() -> Fig:
    return bars('Victorias de cada estilo con 10 000 juegos de pesos al azar sobre la misma matriz de valoraciones',
                'Gráfico de barras con las victorias de seis estilos en 10 000 sorteos de pesos: monolito en capas 663, monolito modular 2 999, microkernel 3 923, pipes and filters 20, microservicios 1 571 y arquitectura celular 824.',
                [('Monolito en capas', 663, 'gold', '663'), ('Monolito modular', 2999, 'teal', '2 999'), ('Microkernel', 3923, 'teal', '3 923'),
                 ('Pipes and filters', 20, 'coral', '20'), ('Microservicios', 1571, 'gold', '1 571'), ('Arquitectura celular', 824, 'gold', '824')],
                scale=0.1, note='Con pesos al azar gana el microkernel casi cuatro de cada diez veces: no porque sea mejor, sino porque la matriz le da valoraciones altas en cinco de siete atributos. El resultado depende de las valoraciones del autor tanto como de los pesos; pipes and filters casi nunca gana porque sus fuerzas (flujo) no están entre los siete atributos.',
                note_kind='gold', foot=MODELO)


# ---------------------------------------------------------------- SE-530
def se530_alta_de_canales() -> Fig:
    rows = [['Monolito con if y elif', '8 líneas', '14 líneas', '6 líneas del núcleo'],
            ['Núcleo con complementos descubiertos', 'misma huella SHA-256', 'misma huella SHA-256', '0 líneas del núcleo']]
    return tab('Añadir tres canales de aviso: líneas tocadas del núcleo en un monolito con if y elif y en un núcleo con complementos',
               'Tabla con dos estructuras: un monolito con if y elif pasa de 8 a 14 líneas y toca 6 líneas del núcleo al añadir tres canales, y un núcleo con complementos descubiertos en un directorio conserva la misma huella del código y toca 0 líneas porque los tres canales son archivos nuevos.',
               ['Estructura', 'Con 3 canales', 'Con 6 canales', 'Líneas tocadas al añadir 3'], rows, [330, 200, 200, 230], row_h=66, size=13,
               note='La huella del núcleo se calcula con SHA-256 del código fuente de la clase del núcleo antes y después de añadir los complementos, y es idéntica. Esto mide la extensión sin tocar el núcleo, no que el contrato del complemento sea bueno: ese contrato es el costo del estilo.',
               note_kind='teal', foot=EJEC)


def se530_aislamiento() -> Fig:
    rows = [['En el mismo hilo, sin protección', 'Detiene la entrega a los demás', 'Bloquea 1,00 s', '0,30 µs'],
            ['En el mismo hilo, con try y except', 'Aislada: 7 de 8 resultados', 'Bloquea 1,00 s', '0,30 µs'],
            ['En un proceso con límite de 0,3 s', 'Aislada: código de error', 'Cortada a los 314 ms', '122 ms']]
    return tab('Tres formas de ejecutar un complemento: qué pasa con uno que falla y con uno lento, y cuánto cuesta cada una',
               'Tabla con tres formas de ejecutar complementos: en el mismo hilo sin protección la excepción detiene la entrega a los demás y un complemento lento bloquea un segundo, con try y except se aísla la excepción y se entregan 7 de 8 resultados pero el lento sigue bloqueando 1,00 segundos, y en un proceso con límite de 0,3 segundos se aísla el error y el lento se corta a los 314 milisegundos, con una mediana de 122 milisegundos por llamada frente a 0,30 microsegundos.',
               ['Forma de ejecutar', 'Complemento que falla', 'Complemento lento', 'Costo por llamada'], rows, [310, 270, 220, 160], row_h=66, size=13,
               note='El aislamiento por proceso protege del complemento lento y del que cuelga, pero cuesta más de cinco órdenes de magnitud por llamada. Una excepción se contiene con una línea; un bloqueo exige otro proceso o un hilo con límite.',
               note_kind='gold', foot=EJEC)


def se530_version_del_contrato() -> Fig:
    rows = [['Sin comprobar la versión', '0 correctos y 6 rotos', 'En plena ejecución'],
            ['Exigir la API 2', '1 cargado y 5 rechazados', 'Al arrancar, con motivo'],
            ['Adaptador para la API 1', '6 cargados, 0 rechazados', 'Sin cambios para los autores']]
    return tab('Un núcleo que sube su contrato a la versión 2: seis complementos, cinco escritos para la versión 1',
               'Tabla con tres políticas de un núcleo que cambia su contrato: sin comprobar la versión, los seis complementos fallan en plena ejecución con 0 correctos; si exige la API 2 carga uno y rechaza cinco al arrancar con su motivo; con un adaptador para la API 1 carga los seis sin cambios para sus autores.',
               ['Política del núcleo', 'Resultado', 'Cuándo se descubre'], rows, [330, 330, 300], row_h=62, size=13,
               note='El contrato entre núcleo y complemento es la parte más cara de un microkernel: cambiarlo rompe a quien no controlas. La versión declarada convierte un fallo en ejecución en un rechazo al arrancar; el adaptador lo convierte en una deuda del núcleo.',
               note_kind='coral', foot=EJEC)


# ---------------------------------------------------------------- SE-531
def se531_memoria() -> Fig:
    return bars('Pico de memoria al procesar 100 000 registros: por lotes, en flujo y en flujo con un filtro que necesita todo',
                'Gráfico de barras con el pico de memoria medido con tracemalloc sobre 100 000 registros: por lotes 48,4 megabytes, en flujo con generadores 0,006 megabytes y en flujo con un filtro de ordenación al final 1,2 megabytes; las tres versiones producen la misma salida de 16 259 elementos.',
                [('Por lotes (listas)', 48.4, 'coral', '48,4 MB'), ('En flujo (generadores)', 0.006, 'teal', '0,006 MB'), ('En flujo con ordenación', 1.2, 'gold', '1,2 MB')],
                scale=9, label_w=300,
                note='El flujo procesa un registro a la vez y su memoria no depende de la entrada; la ordenación necesita retener todo lo que llega a ese filtro, de modo que el pico crece con el tamaño de la salida. La razón por lotes frente a flujo es de unas 7 700 veces solo con estos datos y esta forma de medir.',
                note_kind='gold', foot=EJEC)


def se531_orden_de_filtros() -> Fig:
    rows = [['Filtro caro antes del selectivo', '90 079', 'Enriquece todo lo válido'],
            ['Filtro selectivo antes del caro', '16 259', '82,0 % menos llamadas']]
    return tab('Orden de dos filtros en una cadena de 100 000 registros: llamadas al filtro caro de enriquecer',
               'Tabla con dos órdenes de la misma cadena: si el filtro caro de enriquecer va antes del selectivo se llama 90 079 veces y si va después se llama 16 259 veces, un 82,0 por ciento menos, con la misma salida.',
               ['Orden de la cadena', 'Llamadas al filtro caro', 'Efecto'], rows, [400, 270, 290], row_h=62, size=13,
               note='En una cadena de filtros el orden cambia el costo sin cambiar el resultado, siempre que los filtros conmuten. Poner primero el que descarta más y cuesta menos es una decisión de diseño que se comprueba contando llamadas.',
               note_kind='teal', foot=EJEC)


def se531_contrapresion() -> Fig:
    rows = [['Cola ilimitada', 'Hasta 5 000 (todo)', 'El productor nunca espera'],
            ['Cola acotada a 100', '100', 'El productor espera cuando se llena'],
            ['Filtro que falla sin manejo', 'Se detiene en el registro 5', '19 procesados y 1 rechazado si hay cola de rechazos']]
    return tab('Productor rápido y consumidor lento con 5 000 mensajes: profundidad máxima de la cola y qué ocurre con un registro malformado',
               'Tabla con tres situaciones de un flujo: con una cola ilimitada la profundidad máxima llega a unos 5 000 mensajes y el productor nunca espera, con una cola acotada a 100 la profundidad máxima es 100 y el productor espera cuando se llena, y un filtro que falla sin manejo detiene el flujo en el registro 5, mientras que con una cola de rechazos se procesan 19 registros y se rechaza 1.',
               ['Situación', 'Profundidad máxima o efecto', 'Consecuencia'], rows, [310, 290, 360], row_h=70, size=13,
               note='La cola acotada convierte la sobrecarga en espera del productor en lugar de memoria sin límite; es contrapresión. La profundidad de la cola ilimitada depende del reparto de hilos del sistema (entre 4 999 y 5 000 en las ejecuciones hechas).',
               note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-532
def se532_costo_de_llamada() -> Fig:
    rows = [['Llamada en el mismo proceso', '0,0002', '0,0002'], ['Serializar y deserializar JSON', '0,0051', '0,0162'],
            ['HTTP local con conexión reutilizada', '0,3237', '0,6739'], ['HTTP local con conexión nueva', '1,0791', '1,8198']]
    return tab('Costo medido de una consulta de aviso según cómo se llame: en proceso, serializada y por HTTP en la misma máquina',
               'Tabla con cuatro formas de hacer la misma consulta, con mediana y percentil 99 en milisegundos: en el mismo proceso 0,0002 y 0,0002, serializar y deserializar JSON 0,0051 y 0,0162, HTTP local con conexión reutilizada 0,3237 y 0,6739, y HTTP local con conexión nueva 1,0791 y 1,8198.',
               ['Camino', 'Mediana (ms)', 'p99 (ms)'], rows, [450, 250, 250], row_h=58, size=13,
               note='Cruzar un límite de proceso cuesta más de mil veces lo que una llamada en proceso aun en la misma máquina y sin red real; con red, balanceador y TLS el costo sube. Una ejecución en Windows 11: las proporciones son estables y los valores absolutos no.',
               note_kind='coral', foot=EJEC)


def se532_cadena_de_servicios() -> Fig:
    rows = [['1', '99,900 %', '99,915 %', '20,1', '79,2'], ['2', '99,800 %', '99,750 %', '43,3', '120,6'],
            ['4', '99,601 %', '99,655 %', '90,7', '193,9'], ['8', '99,203 %', '99,150 %', '186,1', '316,7']]
    return tab('Una petición que atraviesa k servicios en serie, cada uno al 99,9 % y con latencia mediana de 20 ms: disponibilidad y latencia',
               'Tabla con una cadena de k servicios síncronos: con 1 servicio la disponibilidad analítica es 99,900 por ciento y la simulada 99,915, con 2 es 99,800 y 99,750, con 4 es 99,601 y 99,655, y con 8 es 99,203 y 99,150; la latencia mediana sube de 20,1 a 186,1 milisegundos y el percentil 99 de 79,2 a 316,7 milisegundos.',
               ['Servicios en la cadena', 'Disponibilidad analítica', 'Disponibilidad simulada', 'p50 (ms)', 'p99 (ms)'], rows, [180, 240, 240, 140, 140], row_h=56, size=13,
               note='La disponibilidad de una cadena es el producto de las de sus eslabones: ocho servicios al 99,9 % dan 99,2 %, unas cinco horas más de caída al mes que un solo servicio. Los 20 000 casos simulados con semilla 44 coinciden con la fórmula dentro de su ruido. La latencia de cada salto es una distribución lognormal del autor.',
               note_kind='coral', foot=MODELO)


def se532_acoplamiento() -> Fig:
    rows = [['Cadena de ocho servicios', '7', '1', '0'], ['Siete servicios que llaman a uno', '7', '7', '0']]
    return tab('Cambio incompatible del contrato de s7 en ocho servicios: cuántos deben cambiar o desplegarse a la vez',
               'Tabla con dos topologías de ocho servicios y un cambio incompatible en el servicio s7: en una cadena deben coordinarse 7 servicios transitivos y 1 directo, en una estrella con siete servicios que llaman a s7 deben coordinarse 7 transitivos y 7 directos, y con un cambio compatible y consumidores tolerantes el número de despliegues coordinados es 0 en ambos casos.',
               ['Topología', 'Servicios afectados (transitivos)', 'Servicios afectados (directos)', 'Con cambio compatible'], rows, [330, 220, 220, 190], row_h=64, size=13,
               note='Un servicio con consumidores que dependen de su forma exacta se despliega con ellos: es un monolito distribuido con más latencia. Lo que desacopla es la compatibilidad de los contratos, no la separación de procesos.',
               note_kind='teal', foot=MODELO)


# ---------------------------------------------------------------- SE-533
def se533_rondas_y_bytes() -> Fig:
    rows = [['El cliente llama a cuatro servicios', '2', '6 692', '173'], ['Gateway de agregación (carga completa)', '1', '6 692', '93'],
            ['BFF móvil (carga proyectada)', '1', '163', '80'], ['BFF web (carga proyectada)', '1', '1 169', '82']]
    return tab('Una pantalla de avisos con cuatro servicios detrás: rondas, bytes y tiempo modelado según quién agrega',
               'Tabla con cuatro caminos para armar la pantalla de avisos: el cliente llama a cuatro servicios en dos rondas con 6 692 bytes y 173 milisegundos modelados, un gateway de agregación usa una ronda con los mismos 6 692 bytes y 93 milisegundos, un BFF móvil usa una ronda con 163 bytes y 80 milisegundos y un BFF web usa una ronda con 1 169 bytes y 82 milisegundos.',
               ['Camino', 'Rondas', 'Bytes', 'Tiempo modelado (ms)'], rows, [450, 110, 160, 240], row_h=58, size=13,
               note='La agregación ahorra una ronda; la proyección por cliente ahorra bytes: el móvil necesita el 2,4 % de la carga completa. Los tiempos usan 80 ms de ida y vuelta y 0,5 MB/s, supuestos del autor, no una medición de red; los tamaños sí son medidos sobre datos sintéticos.',
               note_kind='teal', foot=MODELO)


def se533_confianza_en_el_borde() -> Fig:
    rows = [['Cada servicio confía en el gateway', '4 de 4', 'No hay otra barrera'], ['Cada servicio valida la firma del token', '0 de 4', 'La petición válida pasa en 4 de 4']]
    return tab('Una petición interna falsificada que no pasa por el gateway: cuántos de cuatro servicios la aceptan',
               'Tabla con dos políticas de autenticación frente a una petición interna falsificada que salta el gateway: si los cuatro servicios confían en el gateway la aceptan 4 de 4, y si cada servicio valida la firma HMAC del token la aceptan 0 de 4 y aceptan la petición válida 4 de 4.',
               ['Política', 'Servicios que aceptan la falsa', 'Observación'], rows, [380, 270, 310], row_h=64, size=13,
               note='El gateway centraliza la autenticación en el borde, pero no sustituye la validación en cada servicio: cualquier camino interno que lo evite hereda la confianza. Defensa en profundidad cuesta una verificación de firma por llamada.',
               note_kind='coral', foot=EJEC)


def se533_saltos_de_proxy() -> Fig:
    return bars('Latencia mediana de una llamada HTTP local según el número de proxies de un salto en el camino',
                'Gráfico de barras con la mediana de medianas de ocho rondas intercaladas de 500 llamadas: directo 0,365 milisegundos, con un proxy 0,483 y con dos proxies 0,586; cada proxy añade entre 0,11 y 0,12 milisegundos.',
                [('Directo', 0.365, 'teal', '0,365 ms'), ('Un salto (un proxy)', 0.483, 'gold', '0,483 ms'), ('Dos saltos (dos proxies)', 0.586, 'coral', '0,586 ms')],
                scale=600, label_w=300,
                note='Un proxy de bytes escrito en Python añade unos 0,12 ms por salto sobre esta base; un sidecar de producción tiene otro costo y además hace TLS, métricas y reintentos. La cifra enseña que el salto no es gratis, no el costo de un mesh real.',
                note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-534
def se534_fugas() -> Fig:
    rows = [['Consultas sobre la tabla compartida sin protección', '4 de 12', 'Q09, Q10, Q11 y Q12'],
            ['Linter: busca «tenant_id = ?» en el texto', 'Señala 3 de 4', 'No ve Q12 (filtro anulado por OR)'],
            ['Vista temporal del inquilino en cada solicitud', '0 de 12', 'Las mismas consultas, sin cambios']]
    return tab('Doce consultas sobre una tabla compartida por cinco inquilinos: cuántas filtran datos ajenos según la protección',
               'Tabla con tres estrategias sobre doce consultas: sin protección cuatro consultas devuelven datos ajenos, un linter que busca el filtro por tenant_id en el texto señala tres y no ve la consulta Q12 cuyo filtro se anula con OR, y una vista temporal del inquilino creada en cada solicitud deja cero fugas en las doce consultas sin cambiarlas.',
               ['Estrategia', 'Fugas', 'Detalle'], rows, [400, 190, 370], row_h=64, size=13,
               note='La regla «filtrar por inquilino» escrita en cada consulta falla donde un humano la olvida o la anula; una barrera que no depende de la consulta (la vista que tapa el nombre de la tabla) falla solo si alguien usa otra conexión. Doce consultas escritas por el autor, no una muestra de código real.',
               note_kind='gold', foot=EJEC)


def se534_costo_de_aislar() -> Fig:
    rows = [['Crear la estructura', '3 619 ms para 200', 'Una tabla creada una vez'], ['Disco por inquilino', '12 288 bytes', 'Filas con inquilino_id'],
            ['Migrar el esquema', '1 401 ms en 200 bases', '0,18 ms en una tabla']]
    return tab('Una base de datos por inquilino frente a una tabla compartida: crear 200 inquilinos y migrar el esquema',
               'Tabla con el costo de aislar por base de datos con 200 inquilinos de SQLite frente a una tabla compartida: crear las 200 bases tarda 3 619 milisegundos, cada una ocupa 12 288 bytes y migrar el esquema en las 200 tarda 1 401 milisegundos, mientras que alterar la tabla compartida tarda 0,18 milisegundos.',
               ['Operación', 'Una base por inquilino', 'Tabla compartida'], rows, [300, 330, 330], row_h=62, size=13,
               note='El aislamiento fuerte se paga en operaciones que se multiplican por el número de inquilinos; con 200 es tolerable y con 20 000 la migración deja de ser un comando para ser un proyecto. Tiempos de escritura con sincronización de disco en Windows: varían mucho entre equipos.',
               note_kind='coral', foot=EJEC)


def se534_vecino_ruidoso() -> Fig:
    rows = [['Ninguna (cola común)', '7,96', '7,84'], ['Tope de 1 trabajador de 4 para el ruidoso', '0,16', '54,24']]
    return tab('Un inquilino ruidoso a 40 solicitudes por segundo durante 20 s con cuatro trabajadores: espera p95 por política',
               'Tabla con dos políticas de planificación: sin ninguna política la espera p95 de los nueve inquilinos normales es 7,96 segundos y la del ruidoso 7,84; con un tope de un trabajador de cuatro para el inquilino ruidoso la espera p95 de los normales baja a 0,16 segundos y la del ruidoso sube a 54,24 segundos; las solicitudes son 1 056 normales y 818 ruidosas en ambos casos.',
               ['Política', 'Espera p95 normales (s)', 'Espera p95 ruidoso (s)'], rows, [420, 270, 270], row_h=62, size=13,
               note='El tope no hace desaparecer la sobrecarga: la traslada a quien la causa. Los inquilinos normales vuelven a 0,16 s y el ruidoso espera 54 s. Simulación de eventos con semilla 44; los tiempos de servicio son exponenciales de media 0,1 s, un supuesto del autor.',
               note_kind='teal', foot=MODELO)


FIGURES = {
    "se-529-cuatro-contextos.svg": se529_cuatro_contextos,
    "se-529-de-fuerza-a-estilo.svg": se529_de_fuerza_a_estilo,
    "se-529-victorias-por-estilo.svg": se529_victorias_por_estilo,
    "se-530-alta-de-canales.svg": se530_alta_de_canales,
    "se-530-aislamiento.svg": se530_aislamiento,
    "se-530-version-del-contrato.svg": se530_version_del_contrato,
    "se-531-memoria.svg": se531_memoria,
    "se-531-orden-de-filtros.svg": se531_orden_de_filtros,
    "se-531-contrapresion.svg": se531_contrapresion,
    "se-532-costo-de-llamada.svg": se532_costo_de_llamada,
    "se-532-cadena-de-servicios.svg": se532_cadena_de_servicios,
    "se-532-acoplamiento.svg": se532_acoplamiento,
    "se-533-rondas-y-bytes.svg": se533_rondas_y_bytes,
    "se-533-confianza-en-el-borde.svg": se533_confianza_en_el_borde,
    "se-533-saltos-de-proxy.svg": se533_saltos_de_proxy,
    "se-534-fugas.svg": se534_fugas,
    "se-534-costo-de-aislar.svg": se534_costo_de_aislar,
    "se-534-vecino-ruidoso.svg": se534_vecino_ruidoso,
}
