"""Figures for SE-313 to SE-318 (synthetic data, fixed seeds, SQLite 3.45; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos con semilla fija; SQLite 3.45 en Windows y Ubuntu (WSL2); cifras idénticas salvo donde se indica."


# ---------------------------------------------------------------- SE-313
def se313_anomalias() -> Fig:
    rows = [
        ["Filas que se actualizan al renombrar un curso", "112", "1"],
        ["Nombres distintos del curso si el lote se corta tras 100 filas", "2", "1"],
        ["Cursos visibles tras borrar las entregas del curso 40", "39", "40"],
        ["Tamaño del archivo con 5 000 entregas, tras VACUUM (bytes)", "483 328", "147 456"],
    ]
    return tab("Una tabla plana frente a un modelo normalizado (5 000 entregas, 800 estudiantes, 40 cursos)",
               "Tabla: al renombrar un curso, la tabla plana actualiza 112 filas y, si el lote se corta tras 100, deja dos nombres distintos; el modelo normalizado cambia una fila. Al borrar las entregas de un curso, la tabla plana lo pierde. La plana ocupa 483 328 bytes y la normalizada 147 456.",
               ["Medida", "Tabla plana", "Normalizado"], rows, [520, 170, 170], row_h=48, size=13,
               note="La redundancia no es un problema de espacio sino de verdad: el mismo hecho vive en 112 lugares y cada escritura parcial deja dos versiones. Un curso que solo existe como columna de las entregas desaparece con la última entrega. Los nombres, las cifras y la interrupción tras 100 filas son construcciones del autor.",
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
    rows = [
        ["Lista en una columna, LIKE '%12%'", "33 099", "25 691", "No"],
        ["Lista en una columna, con comas alrededor", "7 408", "0", "No"],
        ["Tabla intermedia estudiante-grupo", "7 408", "0", "Sí"],
    ]
    return tab("Estudiantes de un grupo guardados como lista de identificadores (3 000 grupos, 800 estudiantes)",
               "Tabla: buscar los grupos de cada estudiante con LIKE sobre una lista separada por comas devuelve 33 099 resultados cuando los correctos son 7 408, con 25 691 falsos positivos y 99 estudiantes con resultado erróneo; con delimitadores o con una tabla intermedia el resultado es exacto, y solo la tabla intermedia permite una clave foránea.",
               ["Modelo", "Resultados", "Falsos positivos", "Permite clave foránea"], rows, [430, 150, 170, 170], row_h=48, size=13,
               note="El estudiante 12 aparece al buscar 1, 2, 12, 112 o 120: 99 de los 800 identificadores (los de uno y dos dígitos) dan un resultado equivocado. Arreglar la búsqueda con delimitadores corrige la consulta pero no impide guardar un identificador inexistente ni permite un índice.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-314
def se314_lecturas() -> Fig:
    rows = [
        ["Leer una entrega con estudiante y curso", "3 filas, 291 B", "1 documento, 305 B"],
        ["Promedio de notas por curso (4 000 entregas)", "4 000 filas, ≈104 KB", "4 000 documentos, 1 229 KB"],
        ["Renombrar a un estudiante con 16 entregas", "1 fila", "16 documentos"],
        ["Mismo cambio, cortado a mitad", "Nada o todo", "8 de 16 con el nombre viejo"],
        ["Tamaño total de los datos", "257 103 B", "1 229 093 B (4,78 ×)"],
    ]
    return tab("Mismos datos en filas relacionadas y en documentos con el estudiante y el curso embebidos",
               "Tabla: leer una entrega cuesta tres filas o un documento de tamaño parecido; el promedio por curso lee unos 104 kilobytes en el modelo relacional y 1 229 kilobytes en el documental; renombrar a un estudiante cambia una fila o dieciséis documentos y, si se corta a mitad, deja ocho con el nombre viejo; el documental ocupa 4,78 veces más.",
               ["Operación", "Filas relacionadas", "Documentos embebidos"], rows, [430, 220, 270], row_h=48, size=13,
               note="El documento gana cuando la lectura es siempre la misma entidad completa; pierde cuando el mismo dato se repite y cambia. Los bytes son del JSON de los objetos, no de un motor documental real, y la lectura relacional se midió solo como las dos columnas necesarias.",
               note_kind="gold", foot=SINT)


def se314_busqueda() -> Fig:
    rows = [
        ["Por clave directa (mapa de claves)", "1", "Sin riesgo: es la clave"],
        ["Por posición en una lista de claves", "23 881", "Sin riesgo"],
        ["Por atributo (estudiante), sin índice", "50 000", "Sin riesgo"],
        ["Por atributo, con índice secundario mantenido a mano", "1", "206 de 20 000 escrituras sin entrada (1,03 %)"],
    ]
    return tab("Buscar entre 50 000 valores guardados por clave: comparaciones por consulta",
               "Tabla: buscar por la clave cuesta un sondeo; recorrer por posición cuesta unos 23 881 comparaciones y por un atributo sin índice cuesta 50 000; un índice secundario mantenido a mano vuelve a un sondeo pero, con un fallo del 1 por ciento entre las dos escrituras, deja 206 de 20 000 entradas sin registrar.",
               ["Búsqueda", "Comparaciones", "Consistencia del índice"], rows, [430, 150, 340], row_h=48, size=13,
               note="El almacén de clave-valor es la estructura más barata para una sola pregunta y la más cara para cualquier otra. El índice secundario devuelve el costo a uno, pero ahora son dos escrituras sin transacción entre ellas: la probabilidad de 1 % de cortarse en medio es un supuesto del autor.",
               note_kind="teal", foot=SINT)


def se314_grafo() -> Fig:
    rows = [
        ["UNION ALL, grafo sin ciclos, profundidad máxima 12", "478", "88 cursos distintos"],
        ["UNION, grafo sin ciclos", "88", "Termina sin límite"],
        ["UNION ALL con un ciclo, límite 6 / 8 / 10", "62 / 159 / 386", "Crece con el límite (sin ciclo: 40 / 96 / 226)"],
        ["UNION con el mismo ciclo", "89", "Termina sin límite"],
    ]
    return tab("Prerrequisitos de un curso con una consulta recursiva (grafo de 200 cursos y 291 aristas)",
               "Tabla: con UNION ALL la consulta recursiva devuelve rutas y no cursos: 478 filas para 88 cursos distintos; con UNION devuelve los 88 y termina. Con un ciclo, UNION ALL solo se detiene por el límite de profundidad y crece de 62 a 159 y 386 filas, mientras que UNION termina con 89.",
               ["Consulta", "Filas", "Observación"], rows, [440, 190, 290], row_h=48, size=13,
               note="El grafo se recorre con una recursión de la base de datos, no con un modelo especial. UNION ALL cuenta caminos y UNION cuenta alcanzables; en un grafo con ciclos la primera necesita un tope y la segunda se detiene sola. El grafo es sintético y las cifras dependen de la semilla.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-315
def se315_perdida() -> Fig:
    rows = [
        ["Leer, sumar uno y escribir", "90", "6", "48", "36"],
        ["Escribir solo si la versión no cambió", "90", "6 (3 aceptadas)", "36 (1 aceptada)", "48 (2 aceptadas)"],
        ["UPDATE n = n + 1 atómico", "6", "6", "0", "0"],
    ]
    return tab("Tres clientes suben un contador en todas las intercalaciones posibles (valor correcto: 3)",
               "Tabla: con leer-sumar-escribir, de 90 intercalaciones solo 6 terminan en 3; 48 terminan en 1 y 36 en 2 sin ningún aviso. Escribir solo si la versión no cambió acepta exactamente tantas escrituras como el valor final. Un UPDATE atómico termina siempre en 3.",
               ["Variante", "Intercalaciones", "Final = 3", "Final = 1", "Final = 2"], rows, [350, 150, 160, 160, 160], row_h=48, size=13,
               note="La actualización perdida no falla: devuelve éxito a los tres clientes y deja un valor equivocado. La comprobación de versión no evita el conflicto, lo vuelve visible para que el cliente reintente. Se ejecutó sobre SQLite con tres conexiones en un hilo y orden forzado.",
               note_kind="coral", foot=SINT)


def se315_cortes() -> Fig:
    rows = [
        ["Antes del paso 1 (registro del movimiento)", "Consistente", "Consistente"],
        ["Antes del paso 2 (descontar 5 cupos)", "Registro «iniciado» sin movimiento", "Consistente"],
        ["Antes del paso 3 (sumar 5 cupos)", "Suma de cupos 55: se pierden 5", "Consistente"],
        ["Antes del paso 4 (cerrar el registro)", "Cupos bien; registro «iniciado» para siempre", "Consistente"],
        ["Sin corte", "Completado", "Completado"],
    ]
    return tab("Una transferencia de cupos en cuatro pasos, cortada antes de cada paso",
               "Tabla: sin transacción, un corte antes de los pasos 2, 3 o 4 deja un registro huérfano, una suma de cupos de 55 en vez de 60 o un registro que nunca se cierra; con una transacción, todos los cortes dejan el estado anterior intacto.",
               ["Momento del corte", "Cada paso confirmado solo", "Una transacción"], rows, [420, 330, 170], row_h=48, size=13,
               note="Tres de cuatro cortes dejan el sistema inconsistente sin transacción y ninguno con ella. La atomicidad es la propiedad de que el corte no es observable, no de que los pasos sean rápidos. El corte es una excepción lanzada en el cliente, no un apagón del servidor.",
               note_kind="teal", foot=SINT)


def se315_sesgo() -> Fig:
    rows = [
        ["Lee lo confirmado (READ COMMITTED)", "60", "0"],
        ["Lee una instantánea (SNAPSHOT)", "68", "0"],
        ["Instantánea + detección de lecturas obsoletas", "0", "68"],
        ["SQLite con dos conexiones DEFERRED", "0", "La segunda escritura y el commit del primero fallan con «database is locked»"],
    ]
    return tab("Dos docentes de guardia se retiran a la vez: intercalaciones que dejan cero (70 posibles)",
               "Tabla: en 70 intercalaciones de dos transacciones que comprueban que quedan dos docentes y se retiran, 60 terminan sin nadie de guardia bajo lectura confirmada y 68 bajo instantánea; con detección de conflictos de lectura-escritura ninguna, a costa de abortar una transacción en 68. SQLite lo evita bloqueando.",
               ["Nivel o motor", "Quedan 0 de guardia", "Abortos o comportamiento"], rows, [400, 190, 360], row_h=56, size=13,
               note="Las dos transacciones escriben filas distintas, así que ningún conflicto de escritura las detiene: el invariante «al menos uno» solo se protege si la lectura también cuenta. El modelo de niveles es una simplificación del autor; SQLite se ejecutó de verdad.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-316
def se316_capas() -> Fig:
    rows = [
        ["Nota fuera de rango", "200", "0", "0", "0"],
        ["Estudiante inexistente", "200", "200", "0", "0"],
        ["Correo duplicado", "200", "0", "0", "0"],
        ["Estado desconocido", "200", "0", "0", "0"],
        ["Calificada sin nota", "200", "200", "200", "0"],
        ["Entrega anterior a la publicación", "200", "200", "200", "0"],
        ["Curso inexistente", "200", "200", "0", "0"],
        ["Calificada sin docente", "200", "200", "200", "0"],
        ["Total persistido de 1 600 intentos", "1 600", "1 000", "600", "0"],
    ]
    return tab("Filas inválidas que llegan a la base según la capa que las rechaza (200 intentos por defecto)",
               "Tabla: de 1 600 filas inválidas, 1 600 se guardan sin restricciones, 1 000 con NOT NULL, CHECK y UNIQUE, 600 al añadir claves foráneas y ninguna al añadir disparadores para las reglas entre filas.",
               ["Defecto del cliente", "Sin restricciones", "NOT NULL, CHECK, UNIQUE", "+ claves foráneas", "+ disparadores"], rows, [330, 140, 190, 150, 130], row_h=34, size=12,
               note="Cada capa elimina una familia de defectos y deja pasar la siguiente: las reglas que cruzan columnas o tablas piden claves foráneas o disparadores. Los defectos se generaron para cada capa conociendo sus límites, de modo que 0 en la última columna no mide cobertura real.",
               note_kind="gold", foot=SINT)


def se316_carrera() -> Fig:
    rows = [
        ["Comprobar y luego insertar, sin UNIQUE", "90", "18", "36", "36", "0"],
        ["Comprobar y luego insertar, con UNIQUE", "90", "90", "0", "0", "108"],
    ]
    return tab("Tres clientes registran la misma entrega (estudiante, tarea) en las 90 intercalaciones posibles",
               "Tabla: sin restricción de unicidad, solo 18 de 90 intercalaciones dejan una fila; 36 dejan dos y 36 dejan tres. Con UNIQUE todas dejan una y el motor rechaza 108 inserciones duplicadas.",
               ["Variante", "Intercalaciones", "1 fila", "2 filas", "3 filas", "Rechazos del motor"], rows, [380, 150, 90, 90, 90, 130], row_h=48, size=13,
               note="La comprobación en la aplicación es correcta en un solo hilo y falla bajo concurrencia; la restricción convierte el defecto en un error que el cliente puede manejar. Los 108 rechazos son trabajo útil, no un problema del motor.",
               note_kind="teal", foot=SINT)


def se316_borrado() -> Fig:
    rows = [
        ["Cualquier acción, foreign_keys = OFF (valor por defecto de SQLite)", "Borra sin error", "100", "50"],
        ["NO ACTION o RESTRICT, foreign_keys = ON", "Rechaza el borrado", "100", "0"],
        ["ON DELETE CASCADE, foreign_keys = ON", "Borra el curso y 50 entregas", "50", "0"],
        ["ON DELETE SET NULL, foreign_keys = ON", "Borra el curso; 50 entregas con curso nulo", "100", "0"],
    ]
    return tab("Borrar un curso con 50 de las 100 entregas de una tabla: efecto según la clave foránea",
               "Tabla: con las claves foráneas desactivadas, que es el valor por defecto de SQLite, borrar el curso no da error y deja 50 entregas huérfanas; con ellas activadas, NO ACTION y RESTRICT rechazan, CASCADE borra las 50 entregas y SET NULL las deja con curso nulo.",
               ["Configuración", "Resultado", "Entregas que quedan", "Huérfanas"], rows, [380, 300, 110, 100], row_h=56, size=12,
               note="La clave foránea declarada no protege nada si el motor no la aplica. CASCADE, RESTRICT y SET NULL son tres decisiones de negocio distintas sobre qué pasa con las 50 entregas, no tres sintaxis de lo mismo. Comportamiento de SQLite; otros motores aplican las claves por defecto.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-317
def se317_pasos() -> Fig:
    rows = [
        ["Estudiante = 17 (36 filas, 0,07 %)", "150 296", "407", "SEARCH con índice"],
        ["Estado = «anulada» (1 258 filas, 2,5 %)", "160 072", "13 847", "SEARCH con índice"],
        ["Estado = «enviada» (45 030 filas, 90 %)", "510 248", "495 339", "SEARCH, 3 % menos pasos"],
    ]
    return tab("Pasos de la máquina virtual de SQLite para leer filas con y sin índice (50 000 entregas)",
               "Tabla: buscar al estudiante 17 baja de 150 296 a 407 pasos con un índice; buscar el estado anulada, con el 2,5 por ciento de las filas, baja de 160 072 a 13 847; buscar el estado enviada, con el 90 por ciento, apenas baja de 510 248 a 495 339.",
               ["Consulta", "Sin índice", "Con índice", "Plan"], rows, [400, 150, 150, 220], row_h=48, size=13,
               note="El índice sirve cuanto menos selectiva es la fila buscada, no cuanto más grande es la tabla. Para el 90 % de las filas, recorrer el índice cuesta casi lo mismo que recorrer la tabla. Los pasos son una métrica determinista de trabajo, no tiempo.",
               note_kind="gold", foot=SINT)


def se317_orden() -> Fig:
    rows = [
        ["curso y estudiante", "91 266", "27", "26", "3 142"],
        ["solo estudiante", "90 192", "663", "264", "90 192"],
        ["solo curso", "94 904", "6 743", "94 904", "6 743"],
        ["curso y rango de fechas", "91 948", "3 788", "91 948", "404"],
        ["solo rango de fechas", "124 772", "124 772", "124 772", "18 142"],
    ]
    return tab("Pasos por consulta según el índice compuesto (30 000 entregas)",
               "Tabla: un índice sobre curso y estudiante resuelve curso y estudiante en 27 pasos y solo curso en 6 743, pero no una consulta solo por fechas; el índice en el orden inverso resuelve estudiante en 264 pasos y deja solo curso en 94 904; un índice sobre curso y fecha resuelve el rango de un curso en 404 pasos y el rango solo en 18 142 mediante un recorrido por saltos.",
               ["Consulta", "Sin índice", "(curso, estudiante)", "(estudiante, curso)", "(curso, fecha)"], rows, [250, 130, 190, 190, 160], row_h=44, size=13,
               note="El orden de las columnas decide qué consultas ayuda. SQLite, tras ANALYZE, usó un recorrido por saltos (ANY(curso)) para algunas consultas sin el primer prefijo, algo que otros motores no hacen. Pasos medidos, no tiempo.",
               note_kind="teal", foot=SINT)


def se317_escritura() -> Fig:
    rows = [
        ["0 índices", "340 006", "507 904", "—"],
        ["1 índice", "460 006", "729 088", "+35 % pasos, +44 % espacio"],
        ["2 índices", "580 006", "987 136", "+71 % pasos, +94 % espacio"],
        ["4 índices", "780 006", "1 544 192", "+129 % pasos, +204 % espacio"],
    ]
    return tab("Insertar 20 000 filas según el número de índices; y una consulta por curso lanzada 200 veces",
               "Tabla: insertar 20 000 filas cuesta 340 006 pasos y 507 904 bytes sin índices, 460 006 pasos y 729 088 bytes con uno, 580 006 y 987 136 con dos y 780 006 y 1 544 192 con cuatro. Lanzar una consulta por curso 200 veces cuesta 12 062 807 pasos, una sola agregada 322 819 y con índice 123 406.",
               ["Índices", "Pasos", "Bytes", "Frente a sin índices"], rows, [150, 170, 170, 400], row_h=44, size=13,
               note="Cada índice es una promesa de lectura pagada en cada escritura. En el mismo experimento, 201 sentencias para promediar 200 cursos cuestan 12 062 807 pasos, una agregación 322 819 y las 200 con índice 123 406: el índice rescata al bucle en pasos, pero no mide el viaje de cada sentencia.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-318
def se318_compat() -> Fig:
    rows = [
        ["Original: columna nombre", "Sí", "Sí", "No", "No"],
        ["Renombrar a nombre_completo en un solo paso", "No", "No", "Sí", "Sí"],
        ["Expandir: añadir la columna, rellenar y copiar con disparadores", "Sí", "Sí", "Sí", "Sí"],
        ["Contraer: quitar nombre y los disparadores", "No", "No", "Sí", "Sí"],
    ]
    return tab("Qué versión de la aplicación funciona con cada estado del esquema",
               "Tabla: el renombrado de una columna en un solo paso rompe las dos operaciones de la versión antigua; el estado intermedio con la columna nueva, el relleno y los disparadores de copia permite las cuatro operaciones de ambas versiones; contraer rompe otra vez a la versión antigua, pero ya no debe quedar ninguna.",
               ["Estado del esquema", "v1 lee", "v1 escribe", "v2 lee", "v2 escribe"], rows, [450, 110, 130, 110, 120], row_h=56, size=13,
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
    rows = [
        ["Renombrar una columna y volver", "0", "Sin pérdida"],
        ["Añadir una columna, escribir en ella y quitarla", "1 000", "Se pierden los datos nuevos"],
        ["Quitar la columna comentario y volver a añadirla", "666", "Se pierden los valores"],
        ["Nota de decimal a entero y volver", "937", "Se pierden los decimales"],
        ["Dividir el nombre en dos columnas y recomponer", "66", "Los nombres sin coma cambian"],
        ["Pasar el nombre a mayúsculas y volver", "1 000", "Se pierde la capitalización"],
    ]
    return tab("Valores alterados o perdidos tras aplicar una migración y su inversa (1 000 filas)",
               "Tabla: renombrar una columna y volver no pierde nada; añadir una columna, escribir en ella y quitarla pierde las 1 000 escrituras; quitar y volver a añadir una columna pierde 666 valores; pasar una nota a entero y volver altera 937 filas; dividir y recomponer el nombre altera 66; pasar a mayúsculas y volver altera 1 000.",
               ["Operación y su inversa", "Filas alteradas", "Qué se pierde"], rows, [450, 130, 330], row_h=44, size=13,
               note="«Tiene un down» no significa «es reversible»: solo el renombrado devuelve los mismos datos. Las demás restauran la estructura y pierden información; para volver de verdad hace falta una copia anterior al paso. Datos sintéticos con 5 % de nombres sin coma.",
               note_kind="coral", foot=SINT)


FIGURES = {
    "se-313-anomalias-de-una-tabla-plana.svg": se313_anomalias,
    "se-313-tipo-de-clave-y-tamano.svg": se313_clave,
    "se-313-lista-separada-por-comas.svg": se313_comas,
    "se-314-documento-o-relacional.svg": se314_lecturas,
    "se-314-busqueda-por-clave-o-atributo.svg": se314_busqueda,
    "se-314-prerrequisitos-con-recursion.svg": se314_grafo,
    "se-315-actualizacion-perdida.svg": se315_perdida,
    "se-315-corte-en-cada-paso.svg": se315_cortes,
    "se-315-sesgo-de-escritura.svg": se315_sesgo,
    "se-316-defectos-que-persisten-por-capa.svg": se316_capas,
    "se-316-comprobar-y-luego-insertar.svg": se316_carrera,
    "se-316-claves-foraneas-y-borrado.svg": se316_borrado,
    "se-317-pasos-con-indice-y-sin-indice.svg": se317_pasos,
    "se-317-orden-de-columnas-del-indice.svg": se317_orden,
    "se-317-coste-de-escribir-con-indices.svg": se317_escritura,
    "se-318-compatibilidad-entre-versiones.svg": se318_compat,
    "se-318-lotes-y-bloqueo.svg": se318_lotes,
    "se-318-deshacer-una-migracion.svg": se318_reversion,
}
