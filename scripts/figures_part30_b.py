"""Figures for SE-367 to SE-372 (data engineering: runs of real CPython and SQLite code and seeded models over the Avisos case; Windows CPython 3.12.9, SQLite 3.45.3; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, timeline
from figures_part45_a import flow, mapa

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9 y SQLite 3.45.3; los recuentos se repiten y los tiempos varían de un equipo a otro."
MODELO = "Modelo con parámetros del autor y semilla fija 45; muestra un mecanismo, no mide un sistema real."


# ---------------------------------------------------------------- SE-367
def se547_impacto() -> Fig:
    cats = ["orders.order_id", "orders.customer_id", "orders.amount", "orders.status", "orders.day", "orders.note", "customers.customer_id", "customers.city", "customers.segment"]
    return grouped_bars(
        "Columnas de salida que cambian al perturbar cada columna de origen, medidas y predichas por tres linajes",
        "Barras horizontales agrupadas, por columna de origen, con las salidas que cambian de 17: medidas al perturbar, predichas por el linaje de datos solo, por el linaje con condiciones y por el linaje de tablas; por ejemplo orders.status cambia 12 salidas, el linaje de datos solo predice 0 y con condiciones 15; orders.note y customers.segment no cambian ninguna.",
        cats,
        [("Medido al perturbar", [2, 9, 5, 12, 3, 0, 9, 6, 0], "teal"), ("Linaje de datos solo", [2, 1, 5, 0, 3, 0, 1, 4, 0], "gold"), ("Datos y condiciones", [2, 12, 6, 15, 4, 0, 12, 7, 0], "navy"), ("Linaje de tablas", [15, 15, 15, 15, 15, 15, 13, 13, 13], "grey")],
        unit="Columnas de salida afectadas", horizontal=True, decimals=0, label_w=190, plot_h=420,
        note="El linaje de datos solo omite 31 cambios medidos, casi todos por columnas de filtro y de unión como status y customer_id; el linaje con condiciones no omite ninguno y sobrepredice un poco. El linaje de tablas predice todo o nada: avisa de 13 a 15 columnas aunque note y segment no cambien ninguna. Las 17 salidas son las de seis tablas de un pipeline de juguete.",
        note_kind="gold", foot=EJEC)


def se547_cadena() -> Fig:
    return flow(
        "Linaje de columnas de un importe: de la tabla cruda al informe y qué lo toca por el camino",
        "Diagrama en dos filas que sigue la columna amount: raw_orders.amount se convierte en stg_orders.amount_clp dividiendo por cien, pasa a fact_sales.amount_clp tras unirse con los clientes, se suma en mart_city.total_clp y se ordena en report_top.total_clp; las condiciones status, customer_id y city influyen en qué filas llegan sin ser parte del valor.",
        [[("raw_orders.amount\nCentavos, entero", "teal"), ("stg_orders.amount_clp\nEntre 100 y sin pedidos cancelados", "gold"), ("fact_sales.amount_clp\nUnión por customer_id", "gold")],
         [("mart_city.total_clp\nSuma por ciudad", "gold"), ("report_top.total_clp\nTres ciudades con más ventas", "coral"), ("Condiciones que filtran\nstatus, customer_id, city: cambian qué filas", "plain")]],
        note="Una columna de salida depende de los valores que entran en su expresión y de las condiciones que deciden qué filas la forman. Un catálogo que solo guarda la primera relación declara seguro cambiar status, y el cambio se ve al día siguiente en un informe.",
        note_kind="teal", box_h=96, foot=EJEC)


def se547_limites() -> Fig:
    return mapa(
        "Cuatro formas de SQL que un analizador de texto no resuelve y de dónde sale el linaje en cada una",
        "Cuatro casos: un SELECT con comodín no nombra columnas y produce cero aristas, de modo que hay que expandirlo con el catálogo; el SQL armado por concatenación en código no aparece en el texto y se recupera con los metadatos de la ejecución; una condición de filtro no forma parte del valor y se declara como arista de condición; una función definida por el usuario oculta qué columnas lee y pide declararlo.",
        [("SELECT * FROM fact_sales", "0 aristas de columna", "coral", "Expandir el comodín con las columnas del catálogo"),
         ("f'SELECT {col} FROM {tabla}' en código", "Invisible al texto", "coral", "Capturar el SQL ejecutado o usar metadatos de la consulta"),
         ("WHERE status <> 'cancelled'", "No entra en el valor, sí en las filas", "gold", "Registrar condiciones como un tipo de arista propio"),
         ("Función definida por el usuario", "Entradas ocultas", "gold", "Declarar las columnas que lee en el contrato de la función")],
        note="Ningún método de linaje es completo: el análisis estático ve el texto, la captura en ejecución ve lo que se corrió y la declaración manual ve lo que alguien recordó. Un catálogo honesto marca de qué método viene cada arista y qué no cubre.",
        note_kind="gold", foot=EJEC, left_w=280, mid_w=240)


# ---------------------------------------------------------------- SE-368
def se548_tamanos() -> Fig:
    return grouped_bars(
        "Tamaño de los mismos 200 000 pedidos en cuatro formatos de archivo",
        "Barras con el tamaño en megabytes de 200000 pedidos de ocho columnas: CSV 7,33, JSON por líneas 25,93, binario por filas 11,60 y columnar con compresión 2,00, un 27 por ciento del CSV.",
        ["CSV", "JSON por líneas", "Binario por filas de ancho fijo", "Columnar con diccionario y compresión"],
        [("Megabytes", [7.33, 25.93, 11.60, 2.00], "navy")],
        unit="Megabytes en disco", decimals=2, plot_h=250,
        note="El binario de ancho fijo es mayor que el CSV porque reserva ocho bytes por entero y por texto; el JSON repite el nombre de cada columna en cada fila. El columnar gana porque cada columna guarda valores parecidos juntos y comprime mejor, y la columna de estado, con tres valores, se reduce a un byte por fila antes de comprimir.",
        note_kind="gold", foot=EJEC)


def se548_bytes_leidos() -> Fig:
    return grouped_bars(
        "Megabytes que lee cada formato para sumar el importe de 10 días de 365",
        "Barras horizontales con los megabytes leídos: el JSON por líneas lee 25,93, el binario por filas 11,60, el CSV 7,33, el columnar sin ordenar por día 0,945, el columnar leyendo solo dos columnas de todo el rango 0,59 y el columnar ordenado por día que salta 18 de 20 grupos 0,059.",
        ["JSON por líneas", "Binario por filas", "CSV", "Columnar sin ordenar por día (20 de 20 grupos)", "Columnar, dos columnas, todo el rango", "Columnar ordenado por día (2 de 20 grupos)"],
        [("Megabytes leídos", [25.93, 11.60, 7.33, 0.945, 0.59, 0.059], "teal")],
        unit="Megabytes leídos", horizontal=True, decimals=3, label_w=330, log=True,
        note="Los formatos por filas leen el archivo entero aunque la consulta use dos de ocho columnas y 10 de 365 días. El columnar ahorra por dos vías distintas: leer solo las columnas (de 2,00 a 0,59) y saltar grupos con las estadísticas de mínimo y máximo, que solo funcionan si los datos están agrupados por esa columna: sin ordenar por día se leen los 20 grupos.",
        note_kind="gold", foot=EJEC)


def se548_manifiesto() -> Fig:
    return flow(
        "Un manifiesto con versiones: cómo una compactación no rompe a quien está leyendo",
        "Diagrama en dos filas: el lector A abre la versión 1 del manifiesto, que lista 10 archivos; la compactación escribe un archivo nuevo y publica la versión 2 con un único renombrado atómico; el lector A sigue viendo los 10 archivos de la versión 1 y un lector B nuevo ve la versión 2 con 1 archivo; los archivos viejos se borran más tarde, cuando nadie los usa.",
        [[("Versión 1\nManifiesto con 10 archivos", "teal"), ("Lector A\nAbre la versión 1 y la conserva", "plain"), ("Compactación\nEscribe 1 archivo nuevo", "gold")],
         [("Publicar versión 2\nUn solo renombrado atómico", "gold"), ("Lector B\nVe la versión 2: 1 archivo", "teal"), ("Limpieza\nBorra archivos viejos cuando nadie los lee", "coral")]],
        note="La tabla no es la carpeta: es la lista de archivos de una versión. Eso da lecturas consistentes, viaje en el tiempo y compactación sin parar a los lectores, y exige que todos pasen por el manifiesto; quien lee la carpeta directo vuelve a ver archivos a medias.",
        note_kind="teal", box_h=96, foot=EJEC)


# ---------------------------------------------------------------- SE-369
def se549_clasificacion() -> Fig:
    return grouped_bars(
        "Filas con un correo o un teléfono dentro de cada columna, sobre una muestra de 500 filas",
        "Barras horizontales con las filas de la muestra que contienen un dato personal: email 500 y phone 500, columnas cuyo nombre lo delata, y contact_ref 150 y note 55, columnas con nombre inocuo que también guardan correos.",
        ["email (el nombre lo delata)", "phone (el nombre lo delata)", "contact_ref (el nombre no lo delata)", "note (el nombre no lo delata)"],
        [("Filas con dato personal", [500, 500, 150, 55], "navy")],
        unit="Filas de 500 con correo o teléfono", horizontal=True, decimals=0, label_w=300,
        note="Un clasificador por nombre de columna encuentra dos de las cuatro columnas con datos personales; el texto libre y los identificadores externos esconden el resto. Clasificar por contenido sobre una muestra encuentra las cuatro, a costa de leer datos y de errar en ambos sentidos con valores que se parecen a un correo sin serlo.",
        note_kind="coral", foot=EJEC)


def se549_k_anonimato() -> Fig:
    return grouped_bars(
        "Grupos pequeños de un agregado liberado según los cuasi-identificadores, con k igual a 5",
        "Barras agrupadas con los grupos de menos de 5 personas y las personas en ellos: ciudad 0 y 0, ciudad y plan 0 y 0, ciudad plan y año de nacimiento 441 grupos y 1310 personas, y ciudad plan y década de nacimiento 0 y 0.",
        ["Ciudad", "Ciudad y plan", "Ciudad, plan y año de nacimiento", "Ciudad, plan y década de nacimiento"],
        [("Grupos con menos de 5 personas", [0, 0, 441, 0], "coral"), ("Personas en esos grupos", [0, 0, 1310, 0], "navy")],
        unit="Grupos o personas", decimals=0, plot_h=260,
        note="Añadir el año de nacimiento convierte 18 grupos cómodos en 1 004 grupos, 441 de ellos con menos de cinco personas: 1 310 de 5 000 personas quedan señaladas por su combinación. Generalizar a la década vuelve a 108 grupos sin ninguno pequeño. K-anonimato es una condición necesaria sobre la tabla liberada y no garantiza privacidad frente a quien sabe más.",
        note_kind="gold", foot=EJEC)


def se549_borrado() -> Fig:
    return grouped_bars(
        "Dónde queda el usuario 42 tras una solicitud de borrado, según se borre solo el origen o se propague por el linaje",
        "Barras agrupadas con las filas o copias del usuario 42 que quedan: borrando solo en la tabla de origen quedan 0 en raw, 1 en la tabla intermedia, 3 en la tabla de eventos, 1 en el almacén de variables y 1 en el archivo exportado; propagando por el linaje de tablas queda solo la copia del archivo exportado.",
        ["raw_users", "stg_users", "fact_events", "feature_store", "export.csv (copia fuera de las tablas)"],
        [("Borrar solo en el origen", [0, 1, 3, 1, 1], "coral"), ("Propagar por el linaje de tablas", [0, 0, 0, 0, 1], "teal")],
        unit="Filas o copias que quedan", decimals=0, plot_h=260,
        note="El linaje de tablas encuentra todas las copias que son tablas; la copia exportada a un archivo no está en el grafo y sobrevive. Por eso el catálogo debe registrar las exportaciones como activos con dueño, y por eso el plazo de un borrado incluye las copias de seguridad, que esta prueba no modeló.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-370
def se550_consulta() -> Fig:
    return grouped_bars(
        "Costo mensual de una consulta de 10 días ejecutada 100 veces al día, sobre una tabla escalada a 1 TB",
        "Barras con el costo mensual en unidades inventadas, a 5 unidades por terabyte escaneado: leer el CSV completo 15000, columnar leyendo dos columnas de todo el rango 1213 y columnar leyendo dos columnas con estadísticas que descartan 18 de 20 grupos 121; escala logarítmica.",
        ["CSV, lectura completa", "Columnar, dos columnas, todo el rango", "Columnar, dos columnas, 10 días con estadísticas"],
        [("Costo mensual (unidades)", [15000, 1213, 121], "navy")],
        unit="Costo mensual (unidades inventadas)", decimals=0, plot_h=250, log=True,
        note="Los bytes escaneados se midieron sobre 200 000 filas y se escalaron a 1 TB; el precio de 5 unidades por TB es un parámetro del autor, no una tarifa. La proporción entre barras (124 veces entre la primera y la última) es lo que se traslada, y solo para consultas que lean un rango estrecho de un archivo agrupado por esa columna.",
        note_kind="gold", foot=MODELO)


def se550_refresco() -> Fig:
    return grouped_bars(
        "Costo mensual de refrescar un mart según la frecuencia, con recálculo completo o incremental de 2 días",
        "Barras agrupadas en unidades inventadas: cada 5 minutos el recálculo completo cuesta 24335 y el incremental 3042; cada hora 2028 y 253; una vez al día 84 y 11; escala logarítmica.",
        ["Cada 5 minutos", "Cada hora", "Una vez al día"],
        [("Recálculo completo", [24335, 2028, 84], "coral"), ("Incremental, últimos 2 días", [3042, 253, 11], "teal")],
        unit="Costo mensual (unidades inventadas)", decimals=0, plot_h=270, log=True,
        note="Con los tiempos de esta ejecución (700 ms completo y 78 ms incremental sobre 500 000 filas, escalados 2 000 veces) el incremental cuesta unas 8 veces menos en cada frecuencia, y pasar de diario a cada 5 minutos multiplica el costo por 288 en ambos. La frecuencia es la decisión más cara de la plataforma y la menos discutida.",
        note_kind="gold", foot=MODELO)


def se550_ruta_critica() -> Fig:
    lanes = [("ingest_orders", [(0, 12, "12", "coral")]), ("stg_orders", [(12, 18, "6", "coral")]), ("fact_sales", [(18, 33, "15", "coral")]),
             ("mart_city", [(33, 38, "5", "coral")]), ("report", [(38, 40, "2", "coral")]),
             ("ingest_customers", [(0, 4, "4", "teal")]), ("dim_customer", [(4, 7, "3", "teal")]), ("mart_daily", [(33, 37, "4", "teal")])]
    return timeline(
        "Ocho tareas de un pipeline: la ruta crítica de 40 minutos y las tareas que tienen holgura",
        "Diagrama de Gantt con ocho tareas: la ruta crítica, en rojo, es ingest_orders 12 minutos, stg_orders 6, fact_sales 15, mart_city 5 y report 2, en total 40 minutos; ingest_customers 4, dim_customer 3 y mart_daily 4 tienen holgura; la suma de todas las duraciones es 51 minutos.",
        lanes, unit="Minutos desde el inicio", t_max=42, ticks=[0, 10, 20, 30, 40], lane_h=40, label_w=170,
        note="Reducir a la mitad fact_sales baja el total de 40 a 32,5 minutos; reducir mart_city, de 40 a 39; reducir ingest_customers no cambia nada. Optimizar fuera de la ruta crítica no mueve la hora de entrega.",
        note_kind="teal", foot=MODELO)


# ---------------------------------------------------------------- SE-371
def se551_matriz() -> Fig:
    cols = ["Filas contra origen", "Importe contra origen", "Unicidad", "Frescura", "Repetir ejecución", "Frontera de día", "Esquema de entrada", "Importe medio en banda"]
    rows = ["D1 carga por append", "D2 día en UTC", "D3 unión sin fecha", "D4 tardíos descartados", "D5 unión interna y nulos", "D6 coma flotante", "D7 columna renombrada", "D8 archivo truncado"]
    vals = [[0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1], [1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 0, 0]]
    return heatmap(
        "Ocho defectos sembrados en un pipeline y las ocho comprobaciones que los ven",
        "Mapa de calor de ocho defectos por ocho comprobaciones: D1 solo lo ve repetir la ejecución; D2 lo ven la frontera de día y el importe medio; D3 lo ven las conciliaciones; D4 y D5 las conciliaciones y el importe medio; D6 solo la conciliación de importe; D7 la conciliación de importe, el esquema de entrada y el importe medio; D8 las conciliaciones; la conciliación del importe ve siete de los ocho; unicidad y frescura no ven ninguno.",
        rows, cols, vals, unit="falla", scale="navy", vmin=0, vmax=1, cell_fmt=lambda v: "x" if v else "—", cell_h=34, label_w=210,
        note="Cada defecto lo ve alguna comprobación, pero ninguna sola ve los ocho: la conciliación del importe ve siete y solo se le escapa D1, que únicamente aparece al repetir la ejecución; unicidad y frescura no vieron ninguno de estos ocho y sirven contra otros fallos. D6 pierde 2 centavos en 912 729 905 y solo lo ve una conciliación exacta del importe.",
        note_kind="teal", foot=EJEC)


def se551_arreglar_uno_a_uno() -> Fig:
    labels = ["Los 8", "−D1", "−D8", "−D5", "−D4", "−D3", "−D2", "−D7", "−D6"]
    rows = [42384, 11192, 13558, 13731, 19787, 0, 0, 0, 0]
    days = [15, 15, 15, 15, 15, 15, 15, 2, 0]
    pts = list(zip(range(9), rows))
    return line_chart(
        "Filas de más al corregir los defectos uno a uno, con cada ejecución repetida una vez",
        "Línea con las filas de más respecto de la verdad al ir corrigiendo defectos: con los ocho defectos 42384, tras corregir D1 11192, D8 13558, D5 13731, D4 19787, D3 0, D2 0, D7 0 y D6 0; los días con un resultado distinto bajan solo al corregir D7, de 15 a 2, y D6, a 0.",
        [("Filas de más o de menos", pts, "navy")],
        x_label="Defectos corregidos, de izquierda a derecha", y_label="Filas de más", x_ticks=[(i, l) for i, l in enumerate(labels)], y_ticks=[0, 10000, 20000, 30000, 40000, 50000], point_labels="all", decimals=0, plot_h=280,
        note="El error no baja de forma monótona: al corregir D4 (que dejaba de descartar los tardíos) las filas de más suben de 13 731 a 19 787 porque ahora el defecto D3 las duplica. Y los días con resultado distinto siguen siendo 15 hasta corregir D7 y bajan a 2 y a 0 solo con D6. Los defectos se enmascaran: corregir en cualquier orden y medir tras cada paso.",
        note_kind="coral", foot=EJEC)


def se551_metodo() -> Fig:
    return flow(
        "Método para diagnosticar un resultado erróneo en un pipeline: acotar antes de arreglar",
        "Diagrama en dos filas con seis pasos: reproducir con la misma entrada y una réplica pequeña, acotar la capa donde el resultado deja de coincidir con la verdad, conciliar filas e importes entre capas, formular una causa y una prueba que la distinga, corregir una sola causa y medir tras cada corrección, y escribir una comprobación que habría detenido el defecto.",
        [[("1. Reproducir\nMisma entrada, réplica pequeña", "teal"), ("2. Acotar la capa\nPrimera tabla que difiere de la verdad", "teal"), ("3. Conciliar\nFilas e importes entre capas", "gold")],
         [("4. Una causa y una prueba\nQué la distingue de las otras", "gold"), ("5. Corregir una y medir\nLas causas se enmascaran", "coral"), ("6. Escribir la comprobación\nQue habría parado el defecto", "teal")]],
        note="El orden importa: arreglar sin acotar corrige un síntoma, y corregir varias causas a la vez impide saber cuál movió el resultado. El paso 6 es el que convierte una guardia en una mejora permanente.",
        note_kind="teal", box_h=96, foot=MODELO)


# ---------------------------------------------------------------- SE-372
def se552_arquitectura() -> Fig:
    return flow(
        "Plataforma mínima gobernada de Avisos: tres capas, un registro de metadatos y un control que decide si se publica",
        "Diagrama en dos filas: la zona cruda raw_orders con datos personales declarados, la capa intermedia stg_orders con un seudónimo en lugar del correo y el mart diario mart_daily; un registro de metadatos con dueño, contrato, comprobaciones, retención y entradas de cada conjunto; y un control de siete reglas sobre dueño, contrato, comprobaciones, datos personales, retención, linaje y frescura que se ejecuta antes de publicar.",
        [[("raw_orders\nCorreo declarado como dato personal", "teal"), ("stg_orders\nSeudónimo en lugar del correo", "gold"), ("mart_daily\nDía, pedidos e ingreso, sin datos personales", "teal")],
         [("Registro de metadatos\nDueño, contrato, comprobaciones, retención, entradas", "plain"), ("Control de siete reglas\nSe ejecuta antes de publicar", "coral"), ("Informe de evidencia\nQué se comprobó y qué no se ve", "gold")]],
        note="Todo lo que el control comprueba está declarado en el registro y verificado contra lo construido: el registro dice lo que debería ser y el control lo compara con lo que es. Sin las dos mitades, o la gobernanza es un documento o es una conjetura.",
        note_kind="teal", box_h=96, foot=EJEC)


def se552_mutaciones() -> Fig:
    rows = ["Quitar el dueño de un conjunto", "Columna nueva en el mart sin contrato", "Columna de correo en el mart", "Retención de 10 días sin purga", "Quitar todas las comprobaciones", "El mart lee de raw sin declararlo", "Cambiar el tipo declarado", "Datos con 3 días de atraso", "Retención sin declarar", "Ingreso de SUM a MAX (semántico)"]
    cols = ["R1 dueño", "R2 contrato", "R3 comprobaciones", "R4 datos personales", "R5 retención", "R6 linaje", "R7 frescura"]
    vals = [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    return heatmap(
        "Diez cambios en la plataforma y la regla del control que cada uno dispara",
        "Mapa de calor de diez mutaciones por siete reglas: cada una de las nueve primeras mutaciones dispara exactamente una regla y la décima, cambiar el ingreso de suma a máximo, no dispara ninguna.",
        rows, cols, vals, unit="falla", scale="navy", vmin=0, vmax=1, cell_fmt=lambda v: "falla" if v else "—", highlight=[(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6)], cell_h=34, label_w=270,
        note="Nueve de diez cambios los detiene una regla; el décimo, que mantiene nombres, tipos, dueño, retención, linaje y frescura pero cambia el significado del ingreso, pasa las siete. El control reduce el error posible y no lo elimina: la definición con ejemplos y la conciliación con una fuente independiente son la capa que falta.",
        note_kind="coral", foot=EJEC)


def se552_cobertura() -> Fig:
    return grouped_bars(
        "Mutaciones detectadas de 10 según el control que se aplique a la plataforma",
        "Barras con las mutaciones detectadas de diez: el control de siete reglas detecta 9, un control que solo compara el esquema con el contrato detecta 2 y sin control se detectan 0 antes de que un consumidor las vea.",
        ["Control de siete reglas", "Solo comparar el esquema con el contrato", "Sin control"],
        [("Mutaciones detectadas (de 10)", [9, 2, 0], "teal")],
        unit="Mutaciones detectadas de 10", decimals=0, plot_h=240, ref_lines=[(10, "10")],
        note="Las diez mutaciones son de autor y cubren las siete reglas con una por regla, más una semántica: miden qué familia de defectos ve cada regla, no la tasa de defectos de una plataforma real. Comparar el esquema detecta solo lo que cambia el contrato; el resto exige reglas sobre dueños, datos personales, retención, linaje y frescura.",
        note_kind="gold", foot=MODELO)


FIGURES = {
    "se-367-impacto.svg": se547_impacto,
    "se-367-cadena.svg": se547_cadena,
    "se-367-limites.svg": se547_limites,
    "se-368-tamanos.svg": se548_tamanos,
    "se-368-bytes-leidos.svg": se548_bytes_leidos,
    "se-368-manifiesto.svg": se548_manifiesto,
    "se-369-clasificacion.svg": se549_clasificacion,
    "se-369-k-anonimato.svg": se549_k_anonimato,
    "se-369-borrado.svg": se549_borrado,
    "se-370-consulta.svg": se550_consulta,
    "se-370-refresco.svg": se550_refresco,
    "se-370-ruta-critica.svg": se550_ruta_critica,
    "se-371-matriz.svg": se551_matriz,
    "se-371-arreglar-uno-a-uno.svg": se551_arreglar_uno_a_uno,
    "se-371-metodo.svg": se551_metodo,
    "se-372-arquitectura.svg": se552_arquitectura,
    "se-372-mutaciones.svg": se552_mutaciones,
    "se-372-cobertura.svg": se552_cobertura,
}
