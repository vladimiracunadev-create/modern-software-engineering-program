"""Figures for SE-349 to SE-354 (synthetic data, fixed seeds, SQLite 3.45; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3).

Every figure is a chart or a diagram of the mechanism; the Markdown tables of the classes keep the exact values.
"""
from __future__ import annotations

import math

from figure_kit import Fig, dumbbell, fmt_es, grouped_bars, heatmap, line_chart, stacked_bars, timeline
from figures_part07_a import bars

SINT = "Datos sintéticos con semilla fija; SQLite 3.45 en Windows y Ubuntu (WSL2); cifras idénticas salvo donde se indica."


# ---------------------------------------------------------------- SE-349
def se313_anomalias() -> Fig:
    return stacked_bars(
        "Renombrar el curso 7 con un lote que se corta tras 100 filas: cuántas filas guardan cada nombre",
        "Barras apiladas horizontales con las filas que guardan el nombre del curso 7 después de un renombrado cortado tras 100 filas: la tabla plana tiene 112 filas, 100 con el nombre nuevo y 12 con el viejo, es decir dos versiones de la verdad; el modelo normalizado tiene una sola fila con el nombre nuevo.",
        ["Tabla plana (el nombre se repite en cada entrega)", "Modelo normalizado (el nombre vive en el curso)"],
        [("Con el nombre nuevo", [100, 1], "teal"), ("Con el nombre viejo", [12, 0], "coral")],
        unit="Filas que guardan el nombre del curso 7", horizontal=True, label_w=250,
        note="La redundancia no es un problema de espacio sino de verdad: el mismo hecho vive en 112 lugares y cada escritura parcial deja dos versiones. Un curso que solo existe como columna de las entregas desaparece con la última entrega (39 cursos visibles en vez de 40). Los nombres, las cifras y la interrupción tras 100 filas son construcciones del autor; la tabla de la clase da también el tamaño del archivo (483 328 frente a 147 456 bytes).",
        note_kind="coral", foot=SINT)


def se313_clave() -> Fig:
    items = [
        ("Clave entera (INTEGER PRIMARY KEY)", 284.0, "teal", "284 KiB"),
        ("Clave UUID como texto, tabla con rowid", 1708.0, "coral", "1 708 KiB"),
        ("Clave UUID como texto, WITHOUT ROWID", 872.0, "gold", "872 KiB"),
    ]
    return bars("Tamaño del archivo con 20 000 filas según la clave primaria",
                "Barras: la misma tabla de 20 000 filas ocupa 284 KiB con una clave entera, 1 708 KiB con un UUID de texto en una tabla con rowid y 872 KiB con el UUID en una tabla WITHOUT ROWID.",
                items, 0.36, "La clave de 32 caracteres se escribe en la tabla y otra vez en el índice que SQLite crea para ella; sin rowid solo se escribe una vez, pero las filas se insertan en orden aleatorio y dividen páginas. Seis veces más espacio no es un defecto de UUID sino de la decisión física.",
                label_w=400, width=940, note_kind="gold", foot=SINT)


def se313_comas() -> Fig:
    return stacked_bars(
        "Grupos devueltos al buscar los grupos de cada estudiante (800 búsquedas, 3 000 grupos)",
        "Barras apiladas horizontales con los grupos devueltos por las 800 búsquedas: la lista con LIKE devuelve 33 099 resultados de los que 7 408 son correctos y 25 691 son falsos positivos; con comas alrededor del patrón o con una tabla intermedia se devuelven solo los 7 408 correctos.",
        ["Lista separada por comas con LIKE", "Lista con comas alrededor del patrón", "Tabla intermedia estudiante-grupo"],
        [("Resultados correctos", [7408, 7408, 7408], "teal"), ("Falsos positivos", [25691, 0, 0], "coral")],
        unit="Grupos devueltos por las 800 búsquedas", horizontal=True, label_w=250,
        note="El estudiante 12 aparece al buscar 1, 2, 12, 112 o 120: 99 de los 800 identificadores (los de uno y dos dígitos) dan un resultado equivocado. Arreglar la búsqueda con delimitadores corrige la consulta pero no impide guardar un identificador inexistente ni permite un índice: solo la tabla intermedia admite una clave foránea.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-350
def se314_lecturas() -> Fig:
    return grouped_bars(
        "Registros que toca cada operación con filas relacionadas y con documentos embebidos",
        "Barras agrupadas con los registros tocados por tres operaciones: leer una entrega toca 3 filas relacionadas o 1 documento; renombrar a un estudiante con 16 entregas toca 1 fila o 16 documentos; si el renombrado se corta a mitad, ninguna fila queda con el nombre viejo y 8 de los 16 documentos sí.",
        ["Leer una entrega con su estudiante y su curso", "Renombrar a un estudiante con 16 entregas", "Mismo renombrado cortado a mitad: registros con el nombre viejo"],
        [("Filas relacionadas", [3, 1, 0], "teal"), ("Documentos embebidos", [1, 16, 8], "gold")],
        unit="Registros tocados o desactualizados", plot_h=250,
        note="El documento gana cuando la lectura es siempre la misma entidad completa (1 documento frente a 3 filas); pierde cuando el mismo dato se repite y cambia (16 documentos frente a 1 fila). Los bytes del JSON del documento ocupan 4,78 veces más (1 229 093 frente a 257 103); no son de un motor documental real y la lectura relacional se midió solo como las dos columnas necesarias.",
        note_kind="gold", foot=SINT)


def se314_busqueda() -> Fig:
    return grouped_bars(
        "Buscar entre 50 000 valores guardados por clave: comparaciones por consulta",
        "Barras horizontales en escala logarítmica con las comparaciones por consulta: buscar por la clave o con un índice secundario cuesta 1; recorrer por posición cuesta 23 881 y buscar por un atributo sin índice cuesta 50 000; el índice mantenido a mano deja 206 de 20 000 escrituras sin entrada.",
        ["Por clave directa (mapa de claves)", "Por posición en una lista de claves", "Por atributo (estudiante), sin índice", "Por atributo, con índice a mano (206 de 20 000 escrituras sin entrada)"],
        [("Comparaciones", [1, 23881, 50000, 1], "coral")],
        unit="Comparaciones por consulta", horizontal=True, log=True, label_w=330, ticks=[1, 10, 100, 1000, 10000, 100000],
        note="El almacén de clave-valor es la estructura más barata para una sola pregunta y la más cara para cualquier otra. El índice secundario devuelve el costo a uno, pero ahora son dos escrituras sin transacción entre ellas: la probabilidad de 1 % de cortarse en medio es un supuesto del autor.",
        note_kind="teal", foot=SINT)


def se314_grafo() -> Fig:
    return line_chart(
        "Filas de la recursión de prerrequisitos según el límite de profundidad (200 cursos, 291 aristas)",
        "Líneas con las filas devueltas por una consulta recursiva según el límite de profundidad 6, 8 y 10: con UNION ALL y un ciclo crece de 62 a 159 y 386 filas, y sin ciclo de 40 a 96 y 226; con UNION y el mismo ciclo devuelve 89 filas y termina sin necesitar límite.",
        [("UNION ALL con un ciclo", [(6, 62, "62", "r"), (8, 159, "159", "t"), (10, 386, "386", "t")], "coral"),
         ("UNION ALL sin ciclo", [(6, 40, "40", "b"), (8, 96, "96", "b"), (10, 226, "226", "b")], "gold")],
        x_label="Límite de profundidad de la recursión", y_label="Filas devueltas",
        x_ticks=[(6, "6"), (8, "8"), (10, "10")], y_ticks=[0, 100, 200, 300, 400],
        hlines=[(89, "UNION con el ciclo: 89 filas, termina sin límite")], point_labels="none", plot_h=280,
        note="El grafo se recorre con una recursión de la base de datos, no con un modelo especial. UNION ALL cuenta caminos y UNION cuenta alcanzables (sin ciclos, 478 filas frente a 88 cursos distintos); en un grafo con ciclos la primera necesita un tope y la segunda se detiene sola. El grafo es sintético y las cifras dependen de la semilla.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-351
def se315_perdida() -> Fig:
    return stacked_bars(
        "Valor final de un contador que suben tres clientes (valor correcto: 3)",
        "Barras apiladas horizontales con la proporción de intercalaciones según el valor final: con leer-sumar-escribir 7 por ciento termina en 3, 53 por ciento en 1 y 40 por ciento en 2, sin aviso; con comprobación de versión 7 por ciento acepta tres escrituras y el resto pierde dos o una; con un UPDATE atómico el 100 por ciento termina en 3.",
        ["Leer, sumar uno y escribir (90 intercalaciones)", "Escribir solo si la versión no cambió (90 intercalaciones)", "UPDATE n = n + 1 atómico (6 intercalaciones)"],
        [("Final = 3 (correcto)", [6, 6, 6], "teal"), ("Final = 2", [36, 48, 0], "gold"), ("Final = 1", [48, 36, 0], "coral")],
        unit="Intercalaciones", horizontal=True, percent=True, label_w=270,
        note="La actualización perdida no falla: devuelve éxito a los tres clientes y deja un valor equivocado. La comprobación de versión no evita el conflicto, lo vuelve visible para que el cliente reintente (acepta tantas escrituras como el valor final). Se ejecutó sobre SQLite con tres conexiones en un hilo y orden forzado.",
        note_kind="coral", foot=SINT)


def se315_cortes() -> Fig:
    return timeline(
        "Una transferencia de cupos en cuatro pasos, cortada antes de cada paso",
        "Diagrama de secuencia de los cuatro pasos de una transferencia de cupos y del estado que deja un corte antes de cada uno: sin transacción, cortar antes del paso 2, 3 o 4 deja un registro huérfano, una suma de cupos de 55 en vez de 60 o un registro que nunca se cierra; con una transacción, todos los cortes dejan el estado anterior intacto.",
        [("Pasos de la transferencia", [(0, 1, "1 registrar", "navy"), (1, 2, "2 descontar 5", "navy"), (2, 3, "3 sumar 5", "navy"),
                                        (3, 4, "4 cerrar", "navy"), (4, 5, "fin", "grey")]),
         ("Sin transacción: estado si se corta antes del paso", [(0, 1, "consistente", "teal"), (1, 2, "huérfano", "coral"), (2, 3, "suma de 55", "coral"),
                                                                   (3, 4, "abierto", "gold"), (4, 5, "completado", "teal")]),
         ("Con una transacción: estado si se corta", [(0, 4, "el estado anterior queda intacto", "teal"), (4, 5, "completado", "teal")])],
        unit="Punto de corte: antes del paso indicado (el último no corta)", ticks=[0, 1, 2, 3, 4, 5], t_max=5, lane_h=54,
        note="Tres de cuatro cortes dejan el sistema inconsistente sin transacción y ninguno con ella: «huérfano» es un registro «iniciado» sin movimiento, «suma de 55» pierde 5 cupos y «abierto» deja el registro «iniciado» para siempre. La atomicidad es la propiedad de que el corte no es observable, no de que los pasos sean rápidos. El corte es una excepción lanzada en el cliente, no un apagón del servidor.",
        note_kind="teal", foot=SINT)


def se315_sesgo() -> Fig:
    return stacked_bars(
        "Dos docentes de guardia se retiran a la vez: destino de las 70 intercalaciones posibles",
        "Barras apiladas horizontales con el destino de las 70 intercalaciones de dos transacciones que comprueban que quedan dos docentes y se retiran: bajo lectura confirmada 60 dejan cero docentes de guardia, bajo instantánea 68; con detección de conflictos de lectura-escritura ninguna, a costa de abortar una transacción en 68.",
        ["Lee lo confirmado (READ COMMITTED)", "Lee una instantánea (SNAPSHOT)", "Instantánea con detección de lecturas obsoletas"],
        [("Quedan 0 de guardia", [60, 68, 0], "coral"), ("Una transacción aborta", [0, 0, 68], "gold"), ("Termina bien sin abortar", [10, 2, 2], "teal")],
        unit="Intercalaciones de 70", horizontal=True, label_w=250,
        note="Las dos transacciones escriben filas distintas, así que ningún conflicto de escritura las detiene: el invariante «al menos uno» solo se protege si la lectura también cuenta. Los tramos «sin abortar» son lo que resta de 70. SQLite, con dos conexiones DEFERRED, lo evita bloqueando: la segunda escritura y el commit del primero fallan con «database is locked». El modelo de niveles es una simplificación del autor; SQLite se ejecutó de verdad.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-352
def se316_capas() -> Fig:
    return heatmap(
        "Filas inválidas que llegan a la base según la capa que las rechaza (200 intentos por defecto)",
        "Mapa de calor con las filas inválidas que se guardan, de 200 intentos por defecto del cliente, en cuatro capas acumulativas: sin restricciones se guardan las 1 600; con NOT NULL, CHECK y UNIQUE persisten 1 000, solo los defectos entre filas o tablas; con claves foráneas, 600; con disparadores, ninguna.",
        ["Nota fuera de rango", "Estudiante inexistente", "Correo duplicado", "Estado desconocido", "Calificada sin nota",
         "Entrega anterior a la publicación", "Curso inexistente", "Calificada sin docente"],
        ["Sin restricciones (1 600)", "NOT NULL, CHECK, UNIQUE (1 000)", "+ claves foráneas (600)", "+ disparadores (0)"],
        [[200, 0, 0, 0], [200, 200, 0, 0], [200, 0, 0, 0], [200, 0, 0, 0], [200, 200, 200, 0],
         [200, 200, 200, 0], [200, 200, 0, 0], [200, 200, 200, 0]],
        unit="filas inválidas guardadas de 200", row_title="Defecto del cliente", col_title="Capas acumulativas de restricciones",
        scale="coral", vmin=0, vmax=200, decimals=0, cell_h=36, label_w=250,
        note="Cada capa elimina una familia de defectos y deja pasar la siguiente: las reglas que cruzan columnas o tablas piden claves foráneas o disparadores. Los defectos se generaron para cada capa conociendo sus límites, de modo que 0 en la última columna no mide cobertura real.",
        note_kind="gold", foot=SINT)


def se316_carrera() -> Fig:
    return stacked_bars(
        "Tres clientes registran la misma entrega (estudiante, tarea) en las 90 intercalaciones posibles",
        "Barras apiladas horizontales con las filas que quedan tras 90 intercalaciones de comprobar y luego insertar: sin restricción de unicidad solo 18 dejan una fila, 36 dejan dos y 36 dejan tres; con UNIQUE todas dejan una y el motor rechaza 108 inserciones duplicadas.",
        ["Comprobar y luego insertar, sin UNIQUE", "Comprobar y luego insertar, con UNIQUE (el motor rechaza 108 inserciones)"],
        [("1 fila (correcto)", [18, 90], "teal"), ("2 filas", [36, 0], "gold"), ("3 filas", [36, 0], "coral")],
        unit="Intercalaciones de 90 según las filas finales", horizontal=True, label_w=250,
        note="La comprobación en la aplicación es correcta en un solo hilo y falla bajo concurrencia; la restricción convierte el defecto en un error que el cliente puede manejar. Los 108 rechazos son trabajo útil, no un problema del motor.",
        note_kind="teal", foot=SINT)


def se316_borrado() -> Fig:
    return stacked_bars(
        "Entregas que quedan tras borrar un curso que tenía 50 de las 100 entregas, según la clave foránea",
        "Barras apiladas horizontales con las entregas que quedan de 100 tras borrar un curso con 50 de ellas: con las claves foráneas desactivadas, valor por defecto de SQLite, quedan las 100 y 50 son huérfanas sin que haya error; con NO ACTION o RESTRICT el borrado se rechaza y quedan 100 intactas; con CASCADE quedan 50 porque las otras 50 se borran con el curso; con SET NULL quedan 100, 50 con curso nulo.",
        ["Cualquier acción, foreign_keys = OFF (valor por defecto de SQLite)", "NO ACTION o RESTRICT, foreign_keys = ON", "ON DELETE CASCADE, foreign_keys = ON", "ON DELETE SET NULL, foreign_keys = ON"],
        [("Con un curso válido", [50, 100, 50, 50], "teal"), ("Huérfanas (curso inexistente)", [50, 0, 0, 0], "coral"), ("Con curso nulo", [0, 0, 0, 50], "gold")],
        unit="Entregas que quedan en la tabla (de 100)", horizontal=True, label_w=300,
        note="La clave foránea declarada no protege nada si el motor no la aplica. CASCADE, RESTRICT y SET NULL son tres decisiones de negocio distintas sobre qué pasa con las 50 entregas del curso (se borran, se rechaza el borrado, quedan sin curso), no tres sintaxis de lo mismo. Comportamiento de SQLite; otros motores aplican las claves por defecto.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-353
def se317_pasos() -> Fig:
    def factor(a: float, b: float) -> str:
        q = a / b
        return "÷" + fmt_es(q, 0 if q >= 100 else 1 if q >= 10 else 2)
    return dumbbell(
        "Pasos de la máquina virtual de SQLite para leer filas con y sin índice (50 000 entregas)",
        "Gráfico de puntos unidos en escala logarítmica con los pasos sin índice y con índice: buscar al estudiante 17, el 0,07 por ciento de las filas, baja de 150 296 a 407 pasos; el estado anulada, el 2,5 por ciento, de 160 072 a 13 847; el estado enviada, el 90 por ciento, apenas baja de 510 248 a 495 339.",
        [("Estudiante = 17 (36 filas, 0,07 %)", 150296, 407), ("Estado = «anulada» (1 258 filas, 2,5 %)", 160072, 13847),
         ("Estado = «enviada» (45 030 filas, 90 %)", 510248, 495339)],
        unit="Pasos de la máquina virtual", names=("Sin índice", "Con índice"), log=True, delta=factor, label_w=250,
        note="El índice sirve cuanto más selectiva es la fila buscada, no cuanto más grande es la tabla. Para el 90 % de las filas, recorrer el índice cuesta casi lo mismo que recorrer la tabla (el plan es SEARCH, solo un 3 % menos de pasos). Los pasos son una métrica determinista de trabajo, no tiempo.",
        note_kind="gold", foot=SINT)


def se317_orden() -> Fig:
    data = [[91266, 27, 26, 3142], [90192, 663, 264, 90192], [94904, 6743, 94904, 6743], [91948, 3788, 91948, 404],
            [124772, 124772, 124772, 18142]]
    best = [(i, j) for i, row in enumerate(data) for j, v in enumerate(row) if v == min(row)]
    return heatmap(
        "Pasos por consulta según el índice compuesto (30 000 entregas)",
        "Mapa de calor con los pasos de cinco consultas con cuatro conjuntos de índices, con el color en escala logarítmica: el índice sobre curso y estudiante resuelve curso y estudiante en 27 pasos y solo curso en 6 743; el orden inverso resuelve estudiante en 264 y deja solo curso en 94 904; curso y fecha resuelve el rango de un curso en 404 pasos; el rango solo cuesta 124 772 sin índice y 18 142 con el último.",
        ["Curso y estudiante", "Solo estudiante", "Solo curso", "Curso y rango de fechas", "Solo rango de fechas"],
        ["Sin índice", "(curso, estudiante)", "(estudiante, curso)", "(curso, fecha)"],
        [[math.log10(v) for v in row] for row in data],
        unit="pasos, color en escala logarítmica", row_title="Consulta", col_title="Índice disponible",
        scale="coral", cell_fmt=lambda x: fmt_es(round(10 ** x), 0), highlight=best, cell_h=44, label_w=230,
        note="El orden de las columnas decide qué consultas ayuda; el contorno marca el mejor índice de cada consulta (o los empatados). SQLite, tras ANALYZE, usó un recorrido por saltos (ANY(curso)) para algunas consultas sin el primer prefijo, algo que otros motores no hacen. Pasos medidos, no tiempo.",
        note_kind="teal", foot=SINT)


def se317_escritura() -> Fig:
    return line_chart(
        "Coste de insertar 20 000 filas según el número de índices (sin índices = 100)",
        "Líneas del coste relativo de insertar 20 000 filas con 0, 1, 2 y 4 índices: los pasos suben a 135, 171 y 229 por ciento (340 006 a 780 006 pasos) y el espacio a 144, 194 y 304 por ciento (507 904 a 1 544 192 bytes); cada índice se paga en cada escritura.",
        [("Pasos", [(0, 100, "", "t"), (1, 135, "+35 %", "b"), (2, 171, "+71 %", "b"), (4, 229, "+129 %", "b")], "coral"),
         ("Bytes del archivo", [(0, 100, "", "t"), (1, 144, "+44 %", "t"), (2, 194, "+94 %", "t"), (4, 304, "+204 %", "t")], "teal")],
        x_label="Índices sobre la tabla", y_label="Coste relativo (0 índices = 100)",
        x_ticks=[(0, "0"), (1, "1"), (2, "2"), (4, "4")], y_ticks=[0, 100, 200, 300, 400], point_labels="none",
        note="Cada índice es una promesa de lectura pagada en cada escritura. En el mismo experimento, 201 sentencias para promediar 200 cursos cuestan 12 062 807 pasos, una agregación 322 819 y las 200 con índice 123 406: el índice rescata al bucle en pasos, pero no mide el viaje de cada sentencia.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-354
def se318_compat() -> Fig:
    return timeline(
        "Qué versión de la aplicación funciona con cada estado del esquema",
        "Diagrama de fases con el estado de cada versión de la aplicación al renombrar una columna: renombrar en un solo paso rompe la versión 1 desde el cambio y deja la versión 2 sin funcionar antes de él; expandir, rellenar y copiar con disparadores permite que las dos versiones lean y escriban a la vez, y solo al contraer la versión 1 deja de funcionar, cuando ya no debe quedar ninguna.",
        [("Un solo paso: v1", [(0, 1, "lee y escribe", "teal"), (1, 3, "no lee ni escribe", "coral")]),
         ("Un solo paso: v2", [(0, 1, "no funciona", "coral"), (1, 3, "lee y escribe", "teal")]),
         ("Expandir y contraer: v1", [(0, 2, "lee y escribe", "teal"), (2, 3, "se rompe", "coral")]),
         ("Expandir y contraer: v2", [(0, 1, "no funciona", "coral"), (1, 3, "lee y escribe", "teal")])],
        unit="Fases del despliegue (no es una escala de tiempo)", ticks=[0, 1, 2, 3], t_max=3,
        events=[(1, "1: esquema nuevo"), (2, "2: se quita la columna vieja")], lane_h=54,
        note="El estado intermedio es el único compatible con las dos versiones y con una vuelta atrás; solo se contrae cuando ya ninguna instancia de v1 corre. En el experimento, 0 filas quedaron con nombres distintos o vacíos tras escrituras de ambas versiones.",
        note_kind="teal", foot=SINT)


def se318_lotes() -> Fig:
    items = [
        ("1 transacción de 100 000 filas", 1400.0, "coral", "1 400 021 pasos"),
        ("5 transacciones de 20 000", 280.0, "gold", "280 023 pasos"),
        ("20 transacciones de 5 000", 70.0, "gold", "70 023 pasos"),
        ("100 transacciones de 1 000", 14.0, "teal", "14 023 pasos"),
        ("1 000 transacciones de 100", 1.4, "teal", "1 423 pasos"),
    ]
    return bars("Pasos de la transacción más larga al rellenar una columna en 100 000 filas",
                "Barras: rellenar una columna en 100 000 filas en una sola transacción ocupa 1 400 021 pasos seguidos; en lotes de 20 000, 5 000, 1 000 y 100 filas la transacción más larga baja a 280 023, 70 023, 14 023 y 1 423 pasos. El total apenas cambia.",
                items, 0.36, "El trabajo total es casi el mismo (1,40 a 1,42 millones de pasos) pero el tiempo que se retiene el bloqueo de escritura baja con el tamaño del lote; con lotes más pequeños hay más transacciones. Windows (SQLite 3.45.3); en Ubuntu (3.45.1) las cifras son 7 % mayores con la misma proporción.",
                label_w=330, width=940, note_kind="gold", foot=SINT)


def se318_reversion() -> Fig:
    return grouped_bars(
        "Filas alteradas tras aplicar una migración y su inversa (1 000 filas)",
        "Barras horizontales con las filas alteradas de 1 000 tras aplicar una migración y su inversa: renombrar una columna y volver no altera ninguna; dividir y recomponer el nombre altera 66; quitar y volver a añadir una columna, 666; pasar la nota a entero y volver, 937; añadir una columna, escribir en ella y quitarla, y pasar a mayúsculas y volver, las 1 000.",
        ["Renombrar una columna y volver", "Dividir el nombre en dos columnas y recomponer", "Quitar la columna comentario y volver a añadirla",
         "Nota de decimal a entero y volver", "Añadir una columna, escribir en ella y quitarla", "Pasar el nombre a mayúsculas y volver"],
        [("Filas alteradas", [0, 66, 666, 937, 1000, 1000], "coral")],
        unit="Filas alteradas de 1 000", horizontal=True, label_w=300, ticks=[0, 250, 500, 750, 1000],
        note="«Tiene un down» no significa «es reversible»: solo el renombrado devuelve los mismos datos. Las demás restauran la estructura y pierden información (los valores, los decimales, la capitalización o las escrituras nuevas); para volver de verdad hace falta una copia anterior al paso. Datos sintéticos con 5 % de nombres sin coma.",
        note_kind="coral", foot=SINT)


FIGURES = {
    "se-349-anomalias-de-una-tabla-plana.svg": se313_anomalias,
    "se-349-tipo-de-clave-y-tamano.svg": se313_clave,
    "se-349-lista-separada-por-comas.svg": se313_comas,
    "se-350-documento-o-relacional.svg": se314_lecturas,
    "se-350-busqueda-por-clave-o-atributo.svg": se314_busqueda,
    "se-350-prerrequisitos-con-recursion.svg": se314_grafo,
    "se-351-actualizacion-perdida.svg": se315_perdida,
    "se-351-corte-en-cada-paso.svg": se315_cortes,
    "se-351-sesgo-de-escritura.svg": se315_sesgo,
    "se-352-defectos-que-persisten-por-capa.svg": se316_capas,
    "se-352-comprobar-y-luego-insertar.svg": se316_carrera,
    "se-352-claves-foraneas-y-borrado.svg": se316_borrado,
    "se-353-pasos-con-indice-y-sin-indice.svg": se317_pasos,
    "se-353-orden-de-columnas-del-indice.svg": se317_orden,
    "se-353-coste-de-escribir-con-indices.svg": se317_escritura,
    "se-354-compatibilidad-entre-versiones.svg": se318_compat,
    "se-354-lotes-y-bloqueo.svg": se318_lotes,
    "se-354-deshacer-una-migracion.svg": se318_reversion,
}
