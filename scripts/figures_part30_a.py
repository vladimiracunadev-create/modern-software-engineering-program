"""Figures for SE-361 to SE-366 (data engineering: runs of real CPython and SQLite code and seeded models over the Avisos case; Windows CPython 3.12.9, SQLite 3.45.3; no language model was invoked)."""
from __future__ import annotations

from experiments_part30_b import series as daily_series
from figure_kit import Fig, grouped_bars, heatmap, line_chart, scatter
from figures_part45_a import flow, mapa

import random

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9 y SQLite 3.45.3; los recuentos se repiten y los tiempos varían de un equipo a otro."
MODELO = "Modelo con parámetros del autor y semilla fija 45; muestra un mecanismo, no mide un sistema real."


# ---------------------------------------------------------------- SE-361
def se541_bytes_por_consulta() -> Fig:
    return grouped_bars(
        "Datos que debe tocar cada consulta sobre 200 000 pedidos guardados por filas en SQLite",
        "Barras horizontales con los megabytes que toca cada consulta sobre una tabla de 200000 pedidos de 14,1 megabytes: una búsqueda por clave toca una página de 4 kilobytes, una agregación por día sin índice recorre los 14,1 megabytes y las dos columnas que la agregación necesita suman 3,2 megabytes, un 22,8 por ciento de la tabla.",
        ["Búsqueda por clave (una página)", "Agregación por día recorriendo las filas", "Solo las dos columnas que la agregación usa"],
        [("Megabytes", [0.004, 14.1, 3.2], "navy")],
        unit="Megabytes que toca la consulta", horizontal=True, decimals=3, label_w=330, log=True,
        note="Un almacén por filas guarda cada pedido junto, de modo que la agregación lee las columnas que no necesita (nota, estado, cliente). La búsqueda por clave tardó unos 13 a 18 microsegundos y la agregación entre 280 y 540 milisegundos en tres ejecuciones: miles de veces más, no por ser lenta sino por tocar 200 000 filas. Un índice que cubre día e importe bajó la agregación a unos 60 milisegundos.",
        note_kind="gold", foot=EJEC)


def se541_camino_del_dato() -> Fig:
    return flow(
        "El camino de un pedido desde la base operacional hasta una cifra de un informe",
        "Diagrama en dos filas con el camino del dato: la aplicación escribe en la base operacional, un registro de cambios o una copia periódica lo extrae, aterriza sin modificar en una zona cruda, se limpia en una zona intermedia, se modela en tablas analíticas y se consume en informes, con el contrato y la calidad vigilando cada traspaso.",
        [[("Aplicación y base operacional\nEstado actual, transacciones cortas", "teal"), ("Extracción\nRegistro de cambios o copia periódica", "gold"), ("Zona cruda\nEl dato tal como llegó, con su fecha de carga", "plain")],
         [("Zona intermedia\nTipos, duplicados y zonas horarias resueltos", "gold"), ("Modelo analítico\nHechos y dimensiones con historia", "teal"), ("Consumo\nInformes, paneles y modelos", "coral")]],
        note="Cada flecha es un traspaso donde el dato puede cambiar de significado sin cambiar de forma. La zona cruda se conserva para poder reconstruir lo posterior; sin ella un error de transformación no se corrige, solo se arrastra.",
        note_kind="teal", box_h=96, foot=MODELO)


def se541_lectores_y_escritores() -> Fig:
    return mapa(
        "Lecturas largas, escrituras y la pregunta sobre el pasado: qué pasó en cada caso medido",
        "Cuatro casos medidos en SQLite: con el diario de reversión una lectura larga abierta impide que una escritura se confirme y falla con database is locked; con el registro anticipado, WAL, la escritura se confirma mientras la lectura sigue abierta; la tabla de estado actual solo responde 1486 pagados hoy y el registro de eventos responde 989 pagados y sin enviar el día 100.",
        [("Lectura larga abierta, modo delete", "La escritura falla: database is locked", "coral", "El informe pesado bloquea a la aplicación"),
         ("Lectura larga abierta, modo WAL", "La escritura se confirma", "teal", "Lector y escritor no se esperan, con el costo del archivo WAL"),
         ("«¿Cuántos estaban pagados el día 100?» con el estado actual", "1 486 pagados hoy: otra pregunta", "coral", "La tabla sobrescribe el estado y borra el pasado"),
         ("La misma pregunta con el registro de cambios de estado", "989 pagados y sin enviar", "teal", "La historia se reconstruye porque se conservó")],
        note="Dos problemas distintos justifican separar lo operacional de lo analítico: la interferencia (una lectura larga contra escrituras cortas) y la historia (lo operacional guarda el presente). Ni el modo WAL ni un índice resuelven el segundo.",
        note_kind="gold", foot=EJEC, left_w=290, mid_w=270)


# ---------------------------------------------------------------- SE-362
def se542_politicas() -> Fig:
    return grouped_bars(
        "Eventos que cada política de ingesta deja fuera de su ventana, sobre 10 000 eventos con 3 % de llegadas tardías",
        "Barras horizontales con los eventos fuera de su ventana: el flujo sin tolerancia deja 315, con marca de agua de 1 minuto 262, de 10 minutos 257, de 1 hora 229 y de 6 horas 0; el lote nocturno a las 02:00 del día siguiente deja 15 y el lote con reproceso 3 días después deja 0.",
        ["Flujo sin tolerancia", "Flujo, marca de agua de 1 min", "Flujo, marca de agua de 10 min", "Flujo, marca de agua de 1 h", "Flujo, marca de agua de 6 h", "Lote a las 02:00 del día siguiente", "Lote con reproceso a los 3 días"],
        [("Eventos fuera de su ventana", [315, 262, 257, 229, 0, 15, 0], "navy")],
        unit="Eventos fuera de su ventana (de 10 000)", horizontal=True, decimals=0, label_w=290,
        note="Los eventos que llegan entre 1 y 6 horas tarde no caben en una marca de agua corta; solo una espera de 6 horas los recoge, y esa espera es el retraso con que se publica cada ventana. El lote los recoge porque espera: cambia latencia por completitud. Los retrasos de llegada son una mezcla inventada por el autor.",
        note_kind="gold", foot=MODELO)


def se542_reloj_y_ventana() -> Fig:
    return flow(
        "Tiempo del evento y tiempo de llegada: por qué una ventana necesita una marca de agua",
        "Diagrama en dos filas: el evento ocurre en un instante, viaja con un retraso variable y llega al sistema; la ventana de una hora que lo contiene se emite cuando la marca de agua, el instante hasta el que se espera a los rezagados, la cierra; un evento que llega después de la marca es tardío y se descarta, se corrige o se procesa aparte.",
        [[("Evento ocurre\nTiempo del evento: 10:59", "teal"), ("Viaja con retraso\nRed, colas, teléfono sin cobertura", "gold"), ("Llega al sistema\nTiempo de llegada: 12:30", "plain")],
         [("Ventana 10:00 a 11:00\nAcumula lo que llega a tiempo", "teal"), ("Marca de agua\nSe espera hasta 11:10 por rezagados", "gold"), ("Evento tardío\nLlegó pasada la marca: se corrige o se aparta", "coral")]],
        note="La ventana se define por el tiempo del evento; la marca de agua se define por el tiempo de llegada. Subir la tolerancia recoge más rezagados y retrasa cada resultado la misma cantidad; ninguna marca de agua puede garantizar que no llegue algo más tarde.",
        note_kind="teal", box_h=96, foot=MODELO)


def se542_duplicados() -> Fig:
    return grouped_bars(
        "Efecto de las reentregas de un sistema de entrega al menos una vez sobre el conteo por hora",
        "Barras con el error en el conteo de eventos por hora como porcentaje del total, sobre 10221 entregas de 10000 eventos únicos: contar entregas infla un 2,21 por ciento, contar eventos únicos por clave deja 0, y el 2,21 por ciento es el mismo número de reentregas, 221, sobre 10000.",
        ["Contar entregas (10 221)", "Contar eventos únicos por clave (10 000)"],
        [("Error del conteo (% del total)", [2.21, 0.0], "coral")],
        unit="Error del conteo (% del total)", decimals=2, plot_h=230,
        note="La entrega al menos una vez reenvía lo que no se confirmó; el 2,2 % de reentregas inventado por el autor se vuelve un 2,21 % de error cuando se cuentan entregas. Escribir por clave (la misma clave, el mismo resultado) vuelve inofensiva la reentrega: las 221 reentregas no cambian nada.",
        note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-363
def se543_ciudad() -> Fig:
    cities = ["Santiago", "Valparaíso", "Concepción", "Temuco"]
    return grouped_bars(
        "Ventas por ciudad con la ciudad actual del cliente y con la ciudad que tenía el día del pedido",
        "Barras agrupadas con las ventas por ciudad en millones: con la ciudad actual Santiago 141,4, Valparaíso 163,9, Concepción 145,8 y Temuco 144,8; con la ciudad de la fecha del pedido Santiago 138,4, Valparaíso 162,6, Concepción 147,3 y Temuco 147,5; ambas suman 595,8 millones porque 132 de 1000 clientes se mudaron.",
        cities,
        [("Ciudad actual (dimensión sobrescrita)", [141.4, 163.9, 145.8, 144.8], "gold"), ("Ciudad de la fecha (dimensión con historia)", [138.4, 162.6, 147.3, 147.5], "teal")],
        unit="Ventas (millones)", decimals=1, plot_h=270,
        note="El total no cambia (595,8 millones en las dos); cambia el reparto, hasta 2,9 millones por ciudad, porque 132 de 1 000 clientes se mudaron. Sobrescribir la dimensión responde «¿cuánto vende hoy cada ciudad con los clientes que tiene hoy?», no «¿cuánto vendió cada ciudad?».",
        note_kind="gold", foot=EJEC)


def se543_abanico() -> Fig:
    return grouped_bars(
        "Envío total de 20 000 pedidos según el grano de la consulta",
        "Barras con el envío total en millones: el real, con un grano por pedido, es 10,0; sumado después de unir los pedidos con sus 59809 líneas es 29,9, un 199 por ciento de más; sumado sobre una subconsulta de un registro por pedido vuelve a ser 10,0.",
        ["Un grano por pedido", "Después de unir con las líneas", "Subconsulta con un registro por pedido"],
        [("Envío total (millones)", [10.0, 29.9, 10.0], "coral")],
        unit="Envío total (millones)", decimals=1, plot_h=250,
        note="Cada pedido tiene entre 1 y 5 líneas y su costo de envío se repite en cada una; sumarlo tras la unión lo cuenta una vez por línea. El error no falla ni avisa: la consulta devuelve un número verosímil. El grano de cada tabla (una fila por qué) es la defensa.",
        note_kind="coral", foot=EJEC)


def se543_vault() -> Fig:
    return flow(
        "Data Vault sobre Avisos: qué guarda cada tabla y cuántas filas dejó la carga repetida",
        "Diagrama en dos filas: el hub de clientes con 1000 claves de negocio, el hub de pedidos con 13672 claves, el enlace pedido cliente con 13672 relaciones y el satélite de clientes con 1132 versiones, mil iniciales y 132 cambios de ciudad; cargar de nuevo el día 250 no añadió ninguna fila.",
        [[("hub_customer\n1 000 claves de negocio y su clave hash", "teal"), ("link_order_customer\n13 672 relaciones pedido a cliente", "gold"), ("hub_order\n13 672 claves de negocio y su clave hash", "teal")],
         [("sat_customer\n1 132 versiones: 1 000 iniciales y 132 cambios", "plain"), ("Carga repetida del día 250\n0 filas nuevas: la clave y la huella lo impiden", "gold"), ("Vista de negocio\nSe construye encima; no se consulta el vault directo", "coral")]],
        note="El vault separa la identidad (hub), las relaciones (enlace) y los atributos con su historia (satélite), y solo inserta. Gana trazabilidad y cargas repetibles; paga en uniones, porque la misma pregunta necesita hub, enlace y satélite.",
        note_kind="teal", box_h=96, foot=EJEC)


# ---------------------------------------------------------------- SE-364
def se544_estrategias() -> Fig:
    return grouped_bars(
        "Filas de más respecto de la verdad según la estrategia de carga y el escenario, sobre 30 días y 1790 filas",
        "Barras horizontales con las filas de más: append con ejecución limpia 0, append con fallo y reintento dentro de una transacción 0, append con fallo y reintento sin transacción 37, borrar e insertar sin transacción 0, fusionar por clave sin transacción 0 y append ejecutado dos veces 1790.",
        ["Append, ejecución limpia", "Append, fallo y reintento con transacción", "Append, fallo y reintento sin transacción", "Borrar e insertar, fallo y reintento sin transacción", "Fusionar por clave, fallo y reintento sin transacción", "Append, los 30 días ejecutados dos veces"],
        [("Filas de más", [0, 0, 37, 0, 0, 1790], "navy")],
        unit="Filas de más sobre las 1 790 correctas", horizontal=True, decimals=0, label_w=350,
        note="El append es correcto mientras nada se repite y falla en cuanto un reintento cae sobre una carga a medias o se ejecuta dos veces. Borrar e insertar la partición y fusionar por clave dan el mismo resultado con cualquier número de ejecuciones; la transacción evita además las cargas a medias.",
        note_kind="gold", foot=EJEC)


def se544_ventana_de_reproceso() -> Fig:
    xs = [0, 1, 2, 3, 6]
    return line_chart(
        "Datos tardíos perdidos y trabajo repetido según los días que reprocesa cada ejecución",
        "Líneas con la ventana de reproceso en días: con 0 días se pierden 619 filas tardías de 6000, con 1 día 349, con 2 días 226, con 3 días 118 y con 6 días 0; las filas reprocesadas por ejecución suben de 100 a 700.",
        [("Filas tardías perdidas", list(zip(xs, [619, 349, 226, 118, 0])), "coral"), ("Filas reprocesadas por ejecución", list(zip(xs, [100, 200, 300, 400, 700])), "navy")],
        x_label="Ventana de reproceso (días)", y_label="Filas", x_ticks=[(x, str(x)) for x in xs], y_ticks=[0, 200, 400, 600, 800], point_labels="all", decimals=0, plot_h=280,
        note="Con 10 % de filas que llegan hasta 5 días tarde (distribución del autor), cada día de ventana recupera menos filas y cuesta lo mismo: el beneficio decrece y el costo no. La ventana correcta es la que cubre el retraso máximo tolerado, y es una decisión sobre el negocio, no sobre la herramienta.",
        note_kind="gold", foot=MODELO)


def se544_dependencias() -> Fig:
    return flow(
        "Nueve tareas con dependencias: qué hay que recalcular si cambia un dato crudo",
        "Diagrama en tres filas con nueve tareas: las crudas de pedidos y de clientes, las intermedias, la dimensión de clientes y los hechos de ventas, los dos marts por ciudad y por día y el informe ejecutivo; si cambia raw_orders hay que recalcular 5 tareas, si cambia raw_customers 6 y si cambia fact_sales 3.",
        [[("raw_orders\nCambia: 5 tareas detrás", "coral"), ("stg_orders\nRecalcular", "gold"), ("fact_sales\nSi cambia: 3 detrás", "gold")],
         [("raw_customers\nCambia: 6 tareas detrás", "coral"), ("stg_customers y dim_customer\nRecalcular", "gold"), ("mart_city y mart_daily\nRecalcular las dos", "gold")],
         [("Orden válido\nraw, stg, dim, fact, marts, informe", "teal"), ("report_exec\nSiempre al final de lo anterior", "plain"), ("Sin ciclos\nUn ciclo no tiene orden y se rechaza", "plain")]],
        note="El grafo de dependencias dice qué recalcular y en qué orden; sin él, una corrección en un dato crudo se reparte a mano. La misma lista es la base del linaje de la clase siguiente de la parte.",
        note_kind="teal", box_h=84, foot=EJEC)


# ---------------------------------------------------------------- SE-365
def se545_detectores() -> Fig:
    return grouped_bars(
        "Tres detectores de volumen sobre 120 días con 4 incidentes: incidentes vistos, falsas alarmas e incidentes perdidos",
        "Barras agrupadas: el umbral fijo ve 4 incidentes, da 32 falsas alarmas y pierde 0; el z-score sobre 14 días ve 2, da 0 falsas alarmas y pierde 2; la mediana del mismo día de la semana con MAD ve 4, da 0 falsas alarmas y pierde 0.",
        ["Umbral fijo", "z-score sobre 14 días", "Mediana del mismo día y MAD"],
        [("Incidentes vistos (de 4)", [4, 2, 4], "teal"), ("Falsas alarmas", [32, 0, 0], "coral"), ("Incidentes perdidos", [0, 2, 0], "gold")],
        unit="Cantidad en 120 días", decimals=0, plot_h=270,
        note="El umbral fijo grita cada fin de semana (el volumen cae a 60 %): 32 falsas alarmas. El z-score calma ese ruido pero la caída del fin de semana ya le enseña una varianza grande y no ve la carga parcial de un día hábil ni la de un sábado. Comparar con el mismo día de semanas anteriores recoge los cuatro incidentes sin ruido, con datos sintéticos de patrón semanal único.",
        note_kind="gold", foot=MODELO)


def se545_serie_de_volumen() -> Fig:
    rng = random.Random(45)
    rows, _ = daily_series(rng)
    for d, k in ((42, 0.5), (54, 0.7), (71, 2.0), (89, 0.0)):
        rows[d] = int(rows[d] * k)
    days = list(range(0, 120, 1))
    pts = [(d, rows[d]) for d in days]
    bad = [(d, rows[d]) for d in (42, 54, 71, 89)]
    return scatter(
        "Filas cargadas por día durante 120 días, con cuatro incidentes sembrados",
        "Puntos de 120 días con las filas cargadas por día, alrededor de 10000 en días hábiles y 6000 en fines de semana; los incidentes marcados son una carga parcial al 50 por ciento el día 42, una carga parcial al 70 por ciento el sábado 54, duplicados el día 71 con unas 20000 filas y una carga que no corrió el día 89 con 0 filas.",
        [("Filas por día", pts, "navy"), ("Incidente sembrado", bad, "coral")],
        x_label="Día", y_label="Filas cargadas", x_ticks=[(d, str(d)) for d in range(0, 121, 20)], y_ticks=[0, 5000, 10000, 15000, 20000], point_labels="none", decimals=0, plot_h=300, y_zero=True,
        annotations=[(42, 5000, "Día 42: 50 %", -16, 50), (54, 4200, "Sábado 54: 70 %", 16, 62), (71, 20000, "Día 71: duplicados", 16, 24), (89, 0, "Día 89: 0 filas", -16, -44)],
        note="La serie tiene una forma semanal: sin ella, el sábado 54 parece un día normal. Un incidente es una desviación respecto de lo esperado ese día, no respecto de un número fijo.",
        note_kind="teal", foot=MODELO)


def se545_matriz() -> Fig:
    return heatmap(
        "Seis variantes defectuosas de una tabla de pedidos y qué comprobación falla en cada una",
        "Mapa de calor con siete variantes y seis comprobaciones: la variante limpia no falla ninguna; la carga parcial falla el volumen; los duplicados fallan volumen y unicidad; los nulos en el cliente fallan nulos; los clientes huérfanos fallan integridad referencial; los datos atrasados fallan frescura; los importes en centavos solo fallan la distribución.",
        ["Limpia", "Carga parcial", "Duplicados", "Nulos en el cliente", "Clientes huérfanos", "Datos atrasados", "Importes en centavos"],
        ["Volumen", "Unicidad", "Nulos", "Integridad referencial", "Frescura", "Distribución"],
        [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]],
        unit="falla", scale="navy", vmin=0, vmax=1, cell_fmt=lambda v: "falla" if v else "—", cell_h=36, label_w=200,
        note="Cada comprobación ve una familia de defectos y es ciega a las demás: los importes en centavos pasan volumen, unicidad, nulos, integridad y frescura. Una batería sin la comprobación de distribución habría dado verde.",
        note_kind="teal", foot=EJEC)


# ---------------------------------------------------------------- SE-366
def se546_compatibilidad() -> Fig:
    names = ["Añadir campo opcional con valor por defecto", "Añadir campo requerido sin valor por defecto", "Quitar un campo con valor por defecto", "Quitar un campo requerido", "Renombrar un campo", "Ampliar el tipo de int a long", "Estrechar el tipo de long a int", "Cambiar el tipo a texto", "Cambiar la unidad de horas a minutos", "Reordenar los campos"]
    vals = [[1, 1], [0, 1], [1, 1], [1, 0], [0, 0], [1, 0], [0, 1], [0, 0], [1, 1], [1, 1]]
    return heatmap(
        "Diez cambios de esquema: si un lector nuevo lee datos viejos y si un lector viejo lee datos nuevos",
        "Mapa de calor con diez cambios y dos columnas, compatible hacia atrás y compatible hacia adelante: añadir un campo con valor por defecto, quitar un campo con valor por defecto, reordenar y cambiar la unidad son compatibles en las dos direcciones; añadir un campo requerido rompe hacia atrás; quitar un campo requerido y ampliar el tipo rompen hacia adelante; renombrar y cambiar a texto rompen en las dos.",
        names, ["Lector nuevo lee datos viejos", "Lector viejo lee datos nuevos"], vals,
        unit="compatible", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "sí" if v else "NO", highlight=[(8, 0), (8, 1)], cell_h=36, label_w=330,
        note="La celda resaltada es la trampa: cambiar la unidad conserva nombre y tipo y el verificador la aprueba en las dos direcciones, pero los datos dejan de significar lo mismo. La compatibilidad de esquema es necesaria y no suficiente; la semántica pide una versión nueva, un campo nuevo o un acuerdo escrito.",
        note_kind="coral", foot=EJEC)


def se546_registros_ilegibles() -> Fig:
    return grouped_bars(
        "Registros de 1 000 escritos con el esquema viejo que un lector con el esquema nuevo no puede leer",
        "Barras horizontales con los registros ilegibles de 1000: añadir un campo con valor por defecto 0, añadir un campo requerido sin valor por defecto 1000, quitar un campo requerido 0, renombrar un campo 1000, ampliar de int a long 0, estrechar de long a int 0, cambiar el tipo a texto 1000, cambiar la unidad 0 y reordenar 0.",
        ["Añadir campo con valor por defecto", "Añadir campo requerido sin valor", "Quitar un campo requerido", "Renombrar un campo", "Ampliar de int a long", "Estrechar de long a int", "Cambiar el tipo a texto", "Cambiar la unidad de horas a minutos", "Reordenar los campos"],
        [("Registros ilegibles", [0, 1000, 0, 1000, 0, 0, 1000, 0, 0], "navy")],
        unit="Registros ilegibles de 1 000", horizontal=True, decimals=0, label_w=300,
        note="Los cambios que rompen, rompen todo: ninguno deja la mitad de los registros legibles, porque el defecto está en la regla y no en el dato. Estrechar de long a int no rompió aquí porque ningún valor de la muestra excedía el rango; con un identificador grande sí habría roto, y esa dependencia del dato no se ve en el esquema.",
        note_kind="gold", foot=EJEC)


def se546_expandir_y_contraer() -> Fig:
    return mapa(
        "Renombrar la columna fee_cents a amount_cents: lo que ve cada lector en cada paso",
        "Cuatro pasos medidos en SQLite con un lector viejo que suma fee_cents y uno nuevo que suma amount_cents: al inicio el viejo lee 14950 y el nuevo falla; al añadir la columna nueva el viejo sigue leyendo 14950 y el nuevo devuelve nulo sin error; al escribir en las dos y rellenar, ambos leen 14950; al quitar la columna vieja el viejo falla.",
        [("Inicial: solo existe fee_cents", "Viejo 14 950 · Nuevo ERROR", "gold", "El lector nuevo aún no tiene dónde leer"),
         ("1. Expandir: añadir amount_cents", "Viejo 14 950 · Nuevo NULO sin error", "coral", "El peligro: el nuevo lee una columna vacía y no falla"),
         ("2. Escribir en las dos y rellenar lo antiguo", "Viejo 14 950 · Nuevo 14 950", "teal", "Ventana segura: los dos lectores coinciden"),
         ("3. Contraer: quitar fee_cents", "Viejo ERROR · Nuevo 14 950", "coral", "Solo es seguro cuando el viejo ya no existe")],
        note="Un RENAME COLUMN de golpe rompe al lector viejo al instante. Expandir y contraer reparte el cambio en pasos que cada lector sobrevive, y exige un paso que el renombre no tiene: comprobar que nadie lee la columna vieja antes de quitarla. El paso 1 muestra que «sin error» no es «correcto».",
        note_kind="gold", foot=EJEC, left_w=290, mid_w=270)


FIGURES = {
    "se-361-bytes-por-consulta.svg": se541_bytes_por_consulta,
    "se-361-camino-del-dato.svg": se541_camino_del_dato,
    "se-361-lectores-y-escritores.svg": se541_lectores_y_escritores,
    "se-362-politicas.svg": se542_politicas,
    "se-362-reloj-y-ventana.svg": se542_reloj_y_ventana,
    "se-362-duplicados.svg": se542_duplicados,
    "se-363-ciudad.svg": se543_ciudad,
    "se-363-abanico.svg": se543_abanico,
    "se-363-vault.svg": se543_vault,
    "se-364-estrategias.svg": se544_estrategias,
    "se-364-ventana-de-reproceso.svg": se544_ventana_de_reproceso,
    "se-364-dependencias.svg": se544_dependencias,
    "se-365-detectores.svg": se545_detectores,
    "se-365-serie-de-volumen.svg": se545_serie_de_volumen,
    "se-365-matriz.svg": se545_matriz,
    "se-366-compatibilidad.svg": se546_compatibilidad,
    "se-366-registros-ilegibles.svg": se546_registros_ilegibles,
    "se-366-expandir-y-contraer.svg": se546_expandir_y_contraer,
}
