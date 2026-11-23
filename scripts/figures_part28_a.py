"""Figures for SE-337 to SE-342 (architectural styles: runs of real CPython code and seeded models over the Avisos case; Windows CPython 3.12.9; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars

from figures_part45_a import bars, flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9; los recuentos se repiten y los tiempos varían de un equipo a otro."
MODELO = "Modelo con parámetros del autor y semilla fija 44; muestra un mecanismo, no mide un sistema real."


# ---------------------------------------------------------------- SE-337
def se529_cuatro_contextos() -> Fig:
    return grouped_bars(
        "Cuatro contextos, cuatro estilos distintos: la misma matriz de valoraciones con pesos de cada contexto",
        "Barras agrupadas con el puntaje del estilo ganador y del segundo en cuatro contextos con la misma matriz de seis estilos y siete atributos: un equipo de seis gana el monolito modular con 4,00 frente a 3,65, doce equipos los microservicios con 3,45 frente a 3,15, una plataforma con extensiones de terceros el microkernel con 3,75 frente a 3,10 y un sistema crítico y multi-inquilino la arquitectura celular con 3,50 frente a 3,30.",
        ["Equipo de 6: gana monolito modular (2.º: monolito en capas)", "12 equipos: gana microservicios (2.º: celular)", "Plataforma con terceros: gana microkernel (2.º: microservicios)", "Crítico y multi-inquilino: gana celular (2.º: microservicios)"],
        [("Ganador", [4.00, 3.45, 3.75, 3.50], "teal"), ("Segundo", [3.65, 3.15, 3.10, 3.30], "grey")],
        unit="Puntaje ponderado", decimals=2, horizontal=True, label_w=330,
        note="El puntaje del segundo es el del ganador menos la diferencia: 0,35, 0,30, 0,65 y 0,20. La matriz de valoraciones es la misma en los cuatro casos; solo cambian los pesos. Cuatro estilos distintos ganan, y en el contexto crítico la ventaja sobre el segundo es de 0,20 puntos, menos que el margen de error de un juicio de 1 a 5. Las valoraciones y los pesos los fijó el autor.",
        note_kind="gold", foot=MODELO)


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


# ---------------------------------------------------------------- SE-338
def se530_alta_de_canales() -> Fig:
    return grouped_bars(
        "Añadir tres canales de aviso: líneas tocadas del núcleo en un monolito con if y elif y en un núcleo con complementos",
        "Barras con las líneas del núcleo que se tocan al añadir tres canales: un monolito con if y elif toca 6 líneas, pasando de 8 a 14, y un núcleo con complementos descubiertos en un directorio toca 0 porque los tres canales son archivos nuevos y la huella del código no cambia.",
        ["Monolito con if y elif", "Núcleo con complementos descubiertos"], [("Líneas tocadas del núcleo", [6, 0], "navy")],
        unit="Líneas del núcleo tocadas al añadir 3 canales", decimals=0, plot_h=240,
        note="El monolito pasa de 8 líneas con 3 canales a 14 con 6; el núcleo con complementos conserva la misma huella SHA-256 del código fuente de su clase antes y después. La huella se calcula con SHA-256 del código fuente de la clase del núcleo. Esto mide la extensión sin tocar el núcleo, no que el contrato del complemento sea bueno: ese contrato es el costo del estilo.",
        note_kind="teal", foot=EJEC)


def se530_aislamiento() -> Fig:
    return grouped_bars(
        "Tres formas de ejecutar un complemento: qué pasa con uno que falla y con uno lento, y cuánto cuesta cada una",
        "Barras agrupadas en escala logarítmica con el bloqueo por un complemento lento y el costo por llamada de tres formas de ejecutar complementos: en el mismo hilo, con o sin try y except, el lento bloquea 1000 milisegundos y la llamada cuesta 0,0003; en un proceso con límite de 0,3 segundos el lento se corta a los 314 milisegundos y la llamada cuesta una mediana de 122.",
        ["Mismo hilo, sin protección", "Mismo hilo, con try y except", "Proceso con límite de 0,3 s"],
        [("Bloqueo por el complemento lento", [1000, 1000, 314], "coral"), ("Costo por llamada", [0.0003, 0.0003, 122], "navy")],
        unit="Milisegundos", log=True, plot_h=280,
        note="Sin protección, la excepción detiene la entrega a los demás; con try y except queda aislada y se entregan 7 de 8 resultados; con un proceso, el error se aísla con un código de error. El aislamiento por proceso protege del complemento lento y del que cuelga, pero cuesta más de cinco órdenes de magnitud por llamada (0,30 µs frente a 122 ms). Una excepción se contiene con una línea; un bloqueo exige otro proceso o un hilo con límite.",
        note_kind="gold", foot=EJEC)


def se530_version_del_contrato() -> Fig:
    return stacked_bars(
        "Un núcleo que sube su contrato a la versión 2: seis complementos, cinco escritos para la versión 1",
        "Barras apiladas horizontales con los seis complementos según la política del núcleo: sin comprobar la versión, 0 correctos y 6 rotos en plena ejecución; si exige la API 2, 1 cargado y 5 rechazados al arrancar con su motivo; con un adaptador para la API 1, 6 cargados y 0 rechazados, sin cambios para sus autores.",
        ["Sin comprobar la versión", "Exigir la API 2", "Adaptador para la API 1"],
        [("Correctos o cargados", [0, 1, 6], "teal"), ("Rotos o rechazados", [6, 5, 0], "coral")],
        unit="Complementos de 6", horizontal=True, decimals=0, label_w=190,
        note="Cuándo se descubre: sin comprobar, en plena ejecución; exigiendo la API 2, al arrancar y con motivo; con adaptador, no hay nada que descubrir. El contrato entre núcleo y complemento es la parte más cara de un microkernel: cambiarlo rompe a quien no controlas. La versión declarada convierte un fallo en ejecución en un rechazo al arrancar; el adaptador lo convierte en una deuda del núcleo.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-339
def se531_memoria() -> Fig:
    return bars('Pico de memoria al procesar 100 000 registros: por lotes, en flujo y en flujo con un filtro que necesita todo',
                'Gráfico de barras con el pico de memoria medido con tracemalloc sobre 100 000 registros: por lotes 48,4 megabytes, en flujo con generadores 0,006 megabytes y en flujo con un filtro de ordenación al final 1,2 megabytes; las tres versiones producen la misma salida de 16 259 elementos.',
                [('Por lotes (listas)', 48.4, 'coral', '48,4 MB'), ('En flujo (generadores)', 0.006, 'teal', '0,006 MB'), ('En flujo con ordenación', 1.2, 'gold', '1,2 MB')],
                scale=9, label_w=300,
                note='El flujo procesa un registro a la vez y su memoria no depende de la entrada; la ordenación necesita retener todo lo que llega a ese filtro, de modo que el pico crece con el tamaño de la salida. La razón por lotes frente a flujo es de unas 7 700 veces solo con estos datos y esta forma de medir.',
                note_kind='gold', foot=EJEC)


def se531_orden_de_filtros() -> Fig:
    return grouped_bars(
        "Orden de dos filtros en una cadena de 100 000 registros: llamadas al filtro caro de enriquecer",
        "Barras horizontales con las llamadas al filtro caro de enriquecer: si va antes del selectivo se llama 90079 veces y si va después 16259, un 82,0 por ciento menos, con la misma salida.",
        ["Filtro caro antes del selectivo", "Filtro selectivo antes del caro"], [("Llamadas al filtro caro", [90079, 16259], "navy")],
        unit="Llamadas al filtro caro", horizontal=True, decimals=0, label_w=250,
        note="En la primera cadena se enriquece todo lo válido; en la segunda, un 82,0 % menos de llamadas. En una cadena de filtros el orden cambia el costo sin cambiar el resultado, siempre que los filtros conmuten. Poner primero el que descarta más y cuesta menos es una decisión de diseño que se comprueba contando llamadas.",
        note_kind="teal", foot=EJEC)


def se531_contrapresion() -> Fig:
    return grouped_bars(
        "Productor rápido y consumidor lento con 5 000 mensajes: profundidad máxima de la cola y qué ocurre con un registro malformado",
        "Barras con la profundidad máxima de la cola en dos situaciones: con una cola ilimitada llega a unos 5000 mensajes y el productor nunca espera; con una cola acotada a 100 es 100 y el productor espera cuando se llena.",
        ["Cola ilimitada", "Cola acotada a 100"], [("Profundidad máxima de la cola", [5000, 100], "navy")],
        unit="Mensajes en la cola", decimals=0, plot_h=240,
        note="Un filtro que falla sin manejo detiene el flujo en el registro 5; con una cola de rechazos se procesan 19 registros y se rechaza 1. La cola acotada convierte la sobrecarga en espera del productor en lugar de memoria sin límite; es contrapresión. La profundidad de la cola ilimitada depende del reparto de hilos del sistema (entre 4 999 y 5 000 en las ejecuciones hechas).",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-340
def se532_costo_de_llamada() -> Fig:
    return grouped_bars(
        "Costo medido de una consulta de aviso según cómo se llame: en proceso, serializada y por HTTP en la misma máquina",
        "Barras agrupadas en escala logarítmica con la mediana y el percentil 99 en milisegundos de cuatro formas de hacer la misma consulta: en el mismo proceso 0,0002 y 0,0002, serializar y deserializar JSON 0,0051 y 0,0162, HTTP local con conexión reutilizada 0,3237 y 0,6739, y HTTP local con conexión nueva 1,0791 y 1,8198.",
        ["En el mismo proceso", "JSON ida y vuelta", "HTTP, conexión reutilizada", "HTTP, conexión nueva"],
        [("Mediana", [0.0002, 0.0051, 0.3237, 1.0791], "teal"), ("p99", [0.0002, 0.0162, 0.6739, 1.8198], "coral")],
        unit="Milisegundos", log=True, decimals=4, plot_h=280, width=1000,
        note="Cruzar un límite de proceso cuesta más de mil veces lo que una llamada en proceso aun en la misma máquina y sin red real; con red, balanceador y TLS el costo sube. Una ejecución en Windows 11: las proporciones son estables y los valores absolutos no.",
        note_kind="coral", foot=EJEC)


def se532_cadena_de_servicios() -> Fig:
    ks = [1, 2, 4, 8]
    return line_chart(
        "Una petición que atraviesa k servicios en serie, cada uno al 99,9 % y con latencia mediana de 20 ms: disponibilidad y latencia",
        "Líneas con la latencia mediana y el percentil 99 de una petición que atraviesa k servicios en serie: la mediana sube de 20,1 a 186,1 milisegundos y el percentil 99 de 79,2 a 316,7 con 1, 2, 4 y 8 servicios; la disponibilidad analítica baja de 99,900 a 99,203 por ciento.",
        [("p50", list(zip(ks, [20.1, 43.3, 90.7, 186.1])), "teal"), ("p99", list(zip(ks, [79.2, 120.6, 193.9, 316.7])), "coral")],
        x_label="Servicios en la cadena", y_label="Milisegundos", x_ticks=[(k, str(k)) for k in ks], y_ticks=[0, 100, 200, 300, 400], point_labels="all", decimals=1, plot_h=300,
        note="Disponibilidad analítica y simulada con 1, 2, 4 y 8 servicios: 99,900 % y 99,915 %; 99,800 % y 99,750 %; 99,601 % y 99,655 %; 99,203 % y 99,150 %. La disponibilidad de una cadena es el producto de las de sus eslabones: ocho servicios al 99,9 % dan 99,2 %, unas cinco horas más de caída al mes que un solo servicio. Los 20 000 casos simulados con semilla 44 coinciden con la fórmula dentro de su ruido. La latencia de cada salto es una distribución lognormal del autor.",
        note_kind="coral", foot=MODELO)


def se532_acoplamiento() -> Fig:
    return grouped_bars(
        "Cambio incompatible del contrato de s7 en ocho servicios: cuántos deben cambiar o desplegarse a la vez",
        "Barras agrupadas con los servicios afectados por un cambio incompatible en s7 en dos topologías de ocho servicios: en una cadena, 7 transitivos y 1 directo; en una estrella con siete servicios que llaman a s7, 7 transitivos y 7 directos; con un cambio compatible y consumidores tolerantes, 0 despliegues coordinados en ambas.",
        ["Cadena de ocho servicios", "Siete servicios que llaman a uno"],
        [("Afectados (transitivos)", [7, 7], "gold"), ("Afectados (directos)", [1, 7], "coral"), ("Con cambio compatible", [0, 0], "teal")],
        unit="Servicios que coordinar", decimals=0, plot_h=260,
        note="Un servicio con consumidores que dependen de su forma exacta se despliega con ellos: es un monolito distribuido con más latencia. Lo que desacopla es la compatibilidad de los contratos, no la separación de procesos.",
        note_kind="teal", foot=MODELO)


# ---------------------------------------------------------------- SE-341
def se533_rondas_y_bytes() -> Fig:
    return grouped_bars(
        "Una pantalla de avisos con cuatro servicios detrás: rondas, bytes y tiempo modelado según quién agrega",
        "Barras horizontales en escala logarítmica con los bytes y el tiempo modelado de cuatro caminos para armar la pantalla: el cliente llama a cuatro servicios en dos rondas con 6692 bytes y 173 milisegundos, un gateway de agregación usa una ronda con 6692 bytes y 93, un BFF móvil una ronda con 163 bytes y 80 y un BFF web una ronda con 1169 bytes y 82.",
        ["El cliente llama a cuatro servicios (2 rondas)", "Gateway de agregación, carga completa (1 ronda)", "BFF móvil, carga proyectada (1 ronda)", "BFF web, carga proyectada (1 ronda)"],
        [("Bytes", [6692, 6692, 163, 1169], "navy"), ("Tiempo modelado (ms)", [173, 93, 80, 82], "coral")],
        unit="Bytes o milisegundos", horizontal=True, log=True, decimals=0, label_w=300,
        note="La agregación ahorra una ronda; la proyección por cliente ahorra bytes: el móvil necesita el 2,4 % de la carga completa. Los tiempos usan 80 ms de ida y vuelta y 0,5 MB/s, supuestos del autor, no una medición de red; los tamaños sí son medidos sobre datos sintéticos.",
        note_kind="teal", foot=MODELO)


def se533_confianza_en_el_borde() -> Fig:
    return grouped_bars(
        "Una petición interna falsificada que no pasa por el gateway: cuántos de cuatro servicios la aceptan",
        "Barras con los servicios de cuatro que aceptan una petición interna falsificada que salta el gateway: si cada servicio confía en el gateway la aceptan 4 de 4; si cada uno valida la firma HMAC del token la aceptan 0 de 4, y aceptan la petición válida 4 de 4.",
        ["Cada servicio confía en el gateway", "Cada servicio valida la firma del token"], [("Servicios que aceptan la petición falsa", [4, 0], "coral")],
        unit="Servicios de 4 que la aceptan", decimals=0, plot_h=240,
        note="Con la validación de firma, la petición válida pasa en 4 de 4; con la confianza en el gateway no hay otra barrera. El gateway centraliza la autenticación en el borde, pero no sustituye la validación en cada servicio: cualquier camino interno que lo evite hereda la confianza. Defensa en profundidad cuesta una verificación de firma por llamada.",
        note_kind="coral", foot=EJEC)


def se533_saltos_de_proxy() -> Fig:
    return bars('Latencia mediana de una llamada HTTP local según el número de proxies de un salto en el camino',
                'Gráfico de barras con la mediana de medianas de ocho rondas intercaladas de 500 llamadas: directo 0,365 milisegundos, con un proxy 0,483 y con dos proxies 0,586; cada proxy añade entre 0,11 y 0,12 milisegundos.',
                [('Directo', 0.365, 'teal', '0,365 ms'), ('Un salto (un proxy)', 0.483, 'gold', '0,483 ms'), ('Dos saltos (dos proxies)', 0.586, 'coral', '0,586 ms')],
                scale=600, label_w=300,
                note='Un proxy de bytes escrito en Python añade unos 0,12 ms por salto sobre esta base; un sidecar de producción tiene otro costo y además hace TLS, métricas y reintentos. La cifra enseña que el salto no es gratis, no el costo de un mesh real.',
                note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-342
def se534_fugas() -> Fig:
    return grouped_bars(
        "Doce consultas sobre una tabla compartida por cinco inquilinos: cuántas filtran datos ajenos según la protección",
        "Barras horizontales con las consultas de doce que filtran o se señalan según la estrategia: sin protección cuatro consultas devuelven datos ajenos, un linter que busca el filtro por tenant_id en el texto señala tres y no ve la Q12, cuyo filtro se anula con OR, y una vista temporal del inquilino creada en cada solicitud deja cero fugas sin cambiar las consultas.",
        ["Sin protección: consultas que filtran (Q09, Q10, Q11, Q12)", "Linter de «tenant_id = ?»: fugas señaladas (no ve Q12)", "Vista temporal del inquilino: consultas que filtran"],
        [("Consultas", [4, 3, 0], "coral")],
        unit="Consultas de 12", horizontal=True, decimals=0, label_w=330,
        note="La regla «filtrar por inquilino» escrita en cada consulta falla donde un humano la olvida o la anula; una barrera que no depende de la consulta (la vista que tapa el nombre de la tabla) falla solo si alguien usa otra conexión. Doce consultas escritas por el autor, no una muestra de código real.",
        note_kind="gold", foot=EJEC)


def se534_costo_de_aislar() -> Fig:
    return grouped_bars(
        "Una base de datos por inquilino frente a una tabla compartida: crear 200 inquilinos y migrar el esquema",
        "Barras horizontales en escala logarítmica con el tiempo de aislar por base de datos con 200 inquilinos de SQLite: crear las 200 bases tarda 3619 milisegundos y migrar el esquema en las 200 tarda 1401, mientras que alterar la tabla compartida tarda 0,18 milisegundos.",
        ["Crear 200 bases, una por inquilino", "Migrar el esquema en las 200 bases", "Migrar el esquema en la tabla compartida"],
        [("Tiempo", [3619, 1401, 0.18], "navy")],
        unit="Milisegundos", horizontal=True, log=True, decimals=2, label_w=290,
        note="Cada base ocupa 12 288 bytes, mientras que la tabla compartida se crea una vez y guarda filas con inquilino_id. El aislamiento fuerte se paga en operaciones que se multiplican por el número de inquilinos; con 200 es tolerable y con 20 000 la migración deja de ser un comando para ser un proyecto. Tiempos de escritura con sincronización de disco en Windows: varían mucho entre equipos.",
        note_kind="coral", foot=EJEC)


def se534_vecino_ruidoso() -> Fig:
    return grouped_bars(
        "Un inquilino ruidoso a 40 solicitudes por segundo durante 20 s con cuatro trabajadores: espera p95 por política",
        "Barras agrupadas con la espera p95 de los inquilinos normales y del ruidoso por política: sin política 7,96 segundos y 7,84; con un tope de un trabajador de cuatro para el ruidoso, 0,16 y 54,24.",
        ["Ninguna (cola común)", "Tope de 1 trabajador de 4 para el ruidoso"],
        [("Espera p95 de los normales", [7.96, 0.16], "teal"), ("Espera p95 del ruidoso", [7.84, 54.24], "coral")],
        unit="Segundos de espera (p95)", decimals=2, plot_h=260,
        note="Las solicitudes son 1 056 normales y 818 ruidosas en ambos casos. El tope no hace desaparecer la sobrecarga: la traslada a quien la causa. Los inquilinos normales vuelven a 0,16 s y el ruidoso espera 54 s. Simulación de eventos con semilla 44; los tiempos de servicio son exponenciales de media 0,1 s, un supuesto del autor.",
        note_kind="teal", foot=MODELO)


FIGURES = {
    "se-337-cuatro-contextos.svg": se529_cuatro_contextos,
    "se-337-de-fuerza-a-estilo.svg": se529_de_fuerza_a_estilo,
    "se-337-victorias-por-estilo.svg": se529_victorias_por_estilo,
    "se-338-alta-de-canales.svg": se530_alta_de_canales,
    "se-338-aislamiento.svg": se530_aislamiento,
    "se-338-version-del-contrato.svg": se530_version_del_contrato,
    "se-339-memoria.svg": se531_memoria,
    "se-339-orden-de-filtros.svg": se531_orden_de_filtros,
    "se-339-contrapresion.svg": se531_contrapresion,
    "se-340-costo-de-llamada.svg": se532_costo_de_llamada,
    "se-340-cadena-de-servicios.svg": se532_cadena_de_servicios,
    "se-340-acoplamiento.svg": se532_acoplamiento,
    "se-341-rondas-y-bytes.svg": se533_rondas_y_bytes,
    "se-341-confianza-en-el-borde.svg": se533_confianza_en_el_borde,
    "se-341-saltos-de-proxy.svg": se533_saltos_de_proxy,
    "se-342-fugas.svg": se534_fugas,
    "se-342-costo-de-aislar.svg": se534_costo_de_aislar,
    "se-342-vecino-ruidoso.svg": se534_vecino_ruidoso,
}
