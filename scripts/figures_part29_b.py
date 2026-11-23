"""Figures for SE-355 to SE-360 (synthetic data, fixed seeds, SQLite 3.45; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3).

Every figure is a chart or a diagram of the mechanism; the Markdown tables of the classes keep the exact values.
"""
from __future__ import annotations

from figure_kit import Fig, fmt_exact, grouped_bars, line_chart, scatter, stacked_bars, timeline
from figures_part07_a import bars

SINT = "Datos sintéticos con semilla fija; SQLite 3.45 en Windows y Ubuntu (WSL2); cifras idénticas salvo donde se indica."


# ---------------------------------------------------------------- SE-355
def se319_replicas() -> Fig:
    return grouped_bars(
        "Lecturas obsoletas tras una escritura propia: réplicas asíncronas y cuórum (100 000 y 60 000 pruebas)",
        "Barras horizontales con el porcentaje de lecturas obsoletas inmediatas a la propia escritura: leer del líder o de una réplica con la versión, 0; de una réplica al azar o siempre de la misma, cerca del 24 por ciento; con tres réplicas, escribir en 1 y leer 1 falla el 66,7 por ciento, escribir 1 y leer 2 o escribir 2 y leer 1 cerca del 33, y con R más W mayor que N ninguna.",
        ["Leer del líder", "Réplica al azar (retardo medio 50 ms, lectura a 0–200 ms)", "Siempre la misma réplica",
         "Réplica con la versión de la escritura (8,3 % van al líder)", "Cuórum de 3: escribir en 1 y leer 1", "Cuórum de 3: escribir en 1 y leer 2",
         "Cuórum de 3: escribir en 2 y leer 1", "Cuórum de 3: escribir en 2 y leer 2 (R + W > N)", "Escribir en las 3 y leer 1, o escribir en 1 y leer 3"],
        [("Lecturas obsoletas (%)", [0, 24.37, 24.46, 0, 66.7, 33.4, 33.1, 0, 0], "coral")],
        unit="Lecturas obsoletas tras la propia escritura (%)", horizontal=True, label_w=390, ticks=[0, 20, 40, 60, 80],
        value_fmt=lambda v: fmt_exact(v) + " %",
        note="Que el 24 % sea alto depende de un retardo medio de 50 ms y una lectura uniforme entre 0 y 200 ms: son supuestos del autor, no medidas de una base real. Lo que se mantiene es la forma: la lectura propia necesita la versión o el líder, y el cuórum solo acierta si las dos mitades se solapan.",
        note_kind="coral", foot=SINT)


def se319_movimiento() -> Fig:
    return line_chart(
        "Claves que cambian de nodo al pasar de 4 a 5 nodos con un anillo de hash (100 000 claves)",
        "Líneas con el porcentaje de claves que cambian de nodo al añadir uno según los puntos del anillo por nodo: con 1 punto se mueve el 41,5 por ciento y el nodo más cargado recibe 2,07 veces la media; con 16 puntos 17,0 por ciento; con 128, 21,1 y 1,06 veces; con 512, 20,8 y 1,04 veces. El reparto por módulo mueve el 79,9 por ciento de 4 a 5 nodos y el 94,2 de 16 a 17.",
        [("Anillo de hash", [(1, 41.5, "41,5 % · máx./media 2,07", "r"), (16, 17.0, "17,0 % · 1,20", "b"),
                            (128, 21.1, "21,1 % · 1,06", "t"), (512, 20.8, "20,8 % · 1,04", "b")], "teal")],
        x_label="Puntos del anillo por nodo", y_label="Claves que cambian de nodo (%)", log_x=True,
        x_ticks=[(1, "1"), (16, "16"), (128, "128"), (512, "512")], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        hlines=[(20, "Ideal al pasar de 4 a 5 nodos: 20 %"), (79.9, "Módulo, 4 → 5 nodos: 79,9 %"), (94.2, "Módulo, 16 → 17 nodos: 94,2 %")],
        note="El módulo es sencillo y obliga a mover casi todo; el anillo mueve solo lo que llega al nodo nuevo, pero con pocos puntos reparte desigual (el rótulo de cada punto da el cociente entre la carga del nodo más cargado y la media con 5 nodos). El ideal al pasar de 4 a 5 nodos es mover 1/5 = 20 %. Hash MD5 de claves sintéticas; ningún motor de bases de datos real.",
        note_kind="teal", foot=SINT)


def se319_sesgo() -> Fig:
    items = [
        ("Claves uniformes, hash por estudiante", 1.05, "teal", "1,05 ×"),
        ("Estudiantes con popularidad Zipf, hash por estudiante", 1.77, "gold", "1,77 ×"),
        ("Zipf con la clave caliente repartida en 4 subclaves", 1.39, "gold", "1,39 ×"),
        ("Zipf, partición por curso (50 cursos)", 1.92, "coral", "1,92 ×"),
        ("Zipf, rangos contiguos de identificador", 6.76, "coral", "6,76 ×"),
    ]
    return bars("Carga de la partición más cargada frente a la media (8 particiones, 100 000 peticiones)",
                "Barras: con peticiones uniformes la partición más cargada recibe 1,05 veces la media; con popularidad Zipf y hash por estudiante, 1,77; repartiendo la clave caliente en cuatro subclaves, 1,39; particionando por curso, 1,92; y con rangos contiguos de identificador, 6,76.",
                items, 80, "Una sola clave recibe el 15,8 % de las peticiones: ninguna función de reparto la divide, hay que cambiar la clave. Repartirla en subclaves mejora la escritura y obliga a leer las cuatro. La popularidad Zipf con exponente 1,1 es un supuesto del autor.",
                label_w=430, width=960, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-356
def se320_politicas() -> Fig:
    return line_chart(
        "Lecturas obsoletas frente a aciertos según la política de caché (200 000 operaciones, 5 % escrituras)",
        "Líneas con las lecturas obsoletas según los aciertos de la caché: subir el TTL de 10 a 100 y 1 000 operaciones sube los aciertos de 12,7 a 37,5 y 64,6 por ciento y las lecturas obsoletas de 0,21 a 4,41 y 23,73; sin TTL ni invalidación 98,9 por ciento de aciertos y 85,49 de obsoletas; invalidar al escribir o escribir también en la caché logra 62,9 y 66,2 por ciento de aciertos con 0 obsoletas.",
        [("TTL de 10, 100, 1 000 operaciones y sin TTL", [(12.7, 0.21, "TTL 10", "t"), (37.5, 4.41, "TTL 100", "t"), (64.6, 23.73, "TTL 1 000", "l"),
                                                         (98.9, 85.49, "Sin TTL ni invalidación", "l")], "coral"),
         ("Con invalidación o escritura en la caché (TTL de 1 000)", [(62.9, 0, "", "t"), (66.2, 0, "", "t")], "teal")],
        x_label="Aciertos de la caché (% de lecturas)", y_label="Lecturas obsoletas (%)",
        x_ticks=[(0, "0"), (20, "20"), (40, "40"), (60, "60"), (80, "80"), (100, "100")], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        annotations=[(62.9, 0, "Invalidar al escribir: 62,9 %, 0 obsoletas", -34, -44), (66.2, 0, "Escribir también en la caché: 66,2 %, 0 obsoletas", 36, -62)],
        note="El TTL cambia frescura por aciertos; la invalidación elimina la obsolescencia sin perder aciertos, pero solo si la invalidación llega siempre. Las consultas a la base bajan de 165 849 con TTL de 10 a 2 000 sin TTL. Las obsolescencias no incluyen las carreras de la figura siguiente: aquí el modelo es secuencial.",
        note_kind="gold", foot=SINT)


def se320_estampida() -> Fig:
    return grouped_bars(
        "Pico de consultas a la base cuando expiran 1 000 claves (TTL de 60 s, recarga de 2 s)",
        "Barras agrupadas con el pico de consultas por segundo a la base cuando expiran mil claves: si todas expiran a la vez el pico es de 2 000 sin protección y 863 con una sola recarga por clave; con variación del TTL de 10 por ciento baja a 423 y 99; con 30 por ciento, a 167 y 39.",
        ["Todas expiran a la vez", "TTL con variación de ±10 %", "TTL con variación de ±30 %"],
        [("Sin protección", [2000, 423, 167], "coral"), ("Una sola recarga por clave", [863, 99, 39], "teal")],
        unit="Pico de consultas a la base por segundo", plot_h=270,
        note="El pico y el total miden cosas distintas: la variación del TTL reparte el pico en el tiempo, la recarga única elimina las consultas repetidas (el total en 180 s baja de 8 640 a 2 000 con las claves a la vez, de 10 091 a 2 354 con ±30 %). Combinadas, el pico baja de 2 000 a 39. Es un modelo discreto de un segundo, con 2 000 lecturas por segundo y una recarga de 2 s supuesta.",
        note_kind="teal", foot=SINT)


def se320_carrera() -> Fig:
    return timeline(
        "Dos de los seis órdenes posibles de un lector y un escritor que dejan la caché con el valor viejo",
        "Diagrama de secuencia de dos órdenes de los pasos de un lector (leer la base, llenar la caché) y de un escritor (escribir la base, borrar la clave) que dejan la caché con el valor viejo: en uno de seis órdenes la lectura vieja llega después de borrar la clave; en dos de seis, un lector rellena entre el borrado y la escritura; guardar con versión no deja la caché vieja en ninguno.",
        [("Escribir y luego borrar (1 de 6): lector", [(0, 1, "R1 lee la base", "gold"), (3, 4, "R2 llena la caché", "coral")]),
         ("Escribir y luego borrar (1 de 6): escritor", [(1, 2, "W1 escribe la base", "navy"), (2, 3, "W2 borra la clave", "navy")]),
         ("Borrar y luego escribir (2 de 6): lector", [(1, 2, "R1 lee la base", "gold"), (2, 3, "R2 llena la caché", "coral")]),
         ("Borrar y luego escribir (2 de 6): escritor", [(0, 1, "W2 borra la clave", "navy"), (3, 4, "W1 escribe la base", "navy")])],
        unit="Posición en el orden de ejecución (pasos, no segundos)", ticks=[0, 1, 2, 3, 4], t_max=4, lane_h=52, label_w=250,
        note="Mientras la clave no expire, el valor viejo se sirve para siempre: el TTL solo acota cuánto dura. El error aparece una vez en seis intercalaciones, es decir, es raro, no inexistente, y solo se ve con pruebas de intercalación; con la versión guardada y sin pisar una más nueva, 0 de 6. El modelo tiene un lector y un escritor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-357
def se321_perdida() -> Fig:
    items = [
        ("Copia diaria", 723.1, "coral", "723 min de media (máx. 1 440)"),
        ("Copia cada 6 horas", 180.4, "coral", "180 min (máx. 360)"),
        ("Copia cada hora", 30.0, "gold", "30 min (máx. 60)"),
        ("Registro archivado cada 5 min", 2.5, "teal", "2,5 min (máx. 5)"),
        ("Registro archivado cada minuto", 0.5, "teal", "0,5 min (máx. 1)"),
    ]
    return bars("Pérdida de datos al fallar a una hora uniforme, según el intervalo entre puntos recuperables",
                "Barras: con una copia diaria la pérdida media al fallar es de 723 minutos y la máxima de 1 440; con una copia cada hora, 30 y 60; archivando el registro de cambios cada 5 minutos, 2,5 y 5; cada minuto, 0,5 y 1.",
                items, 0.45, "La pérdida media es la mitad del intervalo y la máxima es el intervalo: el objetivo de punto de recuperación se cumple por diseño, no por buena suerte. 20 000 fallos uniformes en 30 días; una escritura por minuto. La copia no incluye el tiempo para detectar el fallo.",
                label_w=300, width=980, note_kind="gold", foot=SINT)


def se321_caliente() -> Fig:
    return grouped_bars(
        "Cupos que faltan en la copia frente a la suma original de 2 000 000, con la comprobación de integridad en «ok» en los tres casos",
        "Barras horizontales con los cupos que faltan frente a la suma original de 2 000 000 mientras otra transacción mueve 20 000 cupos: la base original no pierde ninguno, la copia del archivo con una transacción sin confirmar pierde 197 aunque integrity_check dice ok, y la API de copia en línea no pierde ninguno.",
        ["Base original, antes de la transferencia", "Copia del archivo con una transacción sin confirmar", "Copia con la API de copia en línea (backup)"],
        [("Cupos que faltan", [0, 197, 0], "coral")],
        unit="Cupos que faltan frente a la suma de 2 000 000", horizontal=True, label_w=290, ticks=[0, 50, 100, 150, 200],
        note="La copia a medias está estructuralmente sana (la suma queda en 1 999 803) y es lógicamente falsa: integrity_check no ve un invariante de negocio. La API la corrige tomando una instantánea consistente. Con otro tamaño de caché o de transacción, la diferencia sería otra: lo que no cambia es que puede haber alguna.",
        note_kind="coral", foot=SINT)


def se321_niveles() -> Fig:
    return grouped_bars(
        "Mutaciones de una copia que detecta cada nivel de verificación por separado (200 mutaciones)",
        "Barras con las mutaciones detectadas de 200 por cada nivel de verificación: comprobar que el archivo existe detecta 10; abrir la base, 25; quick_check, 50; integrity_check, 53; los conteos del manifiesto, 100; los conteos con suma y claves foráneas, 140. Todos los niveles juntos ven 180 y los estructurales solos 88.",
        ["Existe", "Se abre", "quick_check", "integrity_check", "Conteos", "Conteos + suma + FK"],
        [("Mutaciones detectadas", [10, 25, 50, 53, 100, 140], "teal")],
        unit="Mutaciones detectadas de 200", ticks=[0, 50, 100, 150, 200], plot_h=270,
        ref_lines=[(180, "Todos los niveles juntos: 180"), (200, "Las 200 mutaciones")],
        note="Los niveles estructurales ven 88 de 200 y ninguna de las 90 mutaciones lógicas; sumar el manifiesto de negocio eleva la cifra a 180. Los 20 bits que quedan sin ver cayeron en texto sin invariante o en espacio libre. Cada nivel es acumulativo en costo: el último exige conocer el negocio. El desglose por familia de alteración está en la tabla de la clase.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-358
def se322_restos() -> Fig:
    return grouped_bars(
        "Ocurrencias de un valor identificable en el archivo tras borrar la mitad de 2 000 filas",
        "Barras agrupadas con las ocurrencias de un valor identificable antes de borrar, tras borrar 1 000 de 2 000 filas y tras VACUUM: con el borrado estándar quedan 2 087 de las 2 090; con secure_delete, 1 001 de 2 000; el borrado estándar con VACUUM deja 1 085; secure_delete con VACUUM deja 1 000, y una copia hecha antes conserva las 2 000.",
        ["Borrado estándar", "secure_delete activado", "Borrado estándar + VACUUM", "secure_delete + VACUUM y copia previa"],
        [("Antes de borrar", [2090, 2000, 2090, 2000], "navy"), ("Tras borrar 1 000", [2087, 1001, 2087, 1001], "coral"), ("Tras VACUUM", [2087, 1001, 1085, 1000], "teal")],
        unit="Ocurrencias del valor en el archivo", plot_h=270,
        note="DELETE marca el espacio como libre pero no lo sobrescribe: el dato borrado sigue legible en el archivo. El valor de «antes» supera 2 000 porque los desbordes de páginas dejan copias viejas. Ninguna política de borrado alcanza las copias de seguridad: la copia hecha antes del borrado conserva las 2 000 ocurrencias.",
        note_kind="coral", foot=SINT)


def se322_retencion() -> Fig:
    return stacked_bars(
        "Eventos de acceso tras 36 meses según la retención (20 000 eventos al mes; plazo legítimo de 12 meses)",
        "Barras apiladas horizontales con las filas de eventos de acceso tras 36 meses: sin límite de retención hay 720 000, de las que 480 000 superan los 12 meses; con 24 meses quedan 480 000 y 240 000 vencidas; con 12 meses quedan 240 000 y con 6 meses 120 000, ninguna vencida.",
        ["Sin límite de retención", "Conservar 24 meses", "Conservar 12 meses", "Conservar 6 meses"],
        [("Dentro del plazo de 12 meses", [240000, 240000, 240000, 120000], "teal"), ("Con más de 12 meses (vencidas)", [480000, 240000, 0, 0], "coral")],
        unit="Filas de eventos tras 36 meses", horizontal=True, label_w=220,
        note="Es un cálculo aritmético, no una medición: el plazo de 12 meses es un supuesto del autor y cada institución debe fijar el suyo con su base legal (67 % de vencidas sin límite, 50 % con 24 meses). Muestra que una retención sin purga programada convierte datos legítimos en pasivo con el tiempo.",
        note_kind="gold", foot=SINT)


def se322_unicidad() -> Fig:
    return grouped_bars(
        "Personas únicas y grupos distintos según los atributos que se combinan (5 000 personas sintéticas)",
        "Barras horizontales con las personas únicas y los grupos distintos de 5 000 personas según los atributos combinados: con solo la edad hay 48 grupos y ninguna persona única; con edad y comuna, 161 únicas; con edad, comuna y año, 3 094; con el curso también, 4 876; generalizar a rangos baja a 2 y a 1 persona única.",
        ["Edad", "Edad + comuna", "Edad + comuna + año de ingreso", "Edad + comuna + año + curso", "Edad en rangos de 10 + 6 zonas + año",
         "Edad en rangos de 20 + 3 zonas + año en bloques de 4"],
        [("Personas únicas", [0, 161, 3094, 4876, 2, 1], "coral"), ("Grupos distintos", [48, 1388, 3969, 4938, 248, 32], "gold")],
        unit="Personas únicas o grupos (de 5 000 personas)", horizontal=True, label_w=300, ticks=[0, 1000, 2000, 3000, 4000, 5000],
        note="Quitar el nombre no anonimiza: combinar tres atributos que parecen inofensivos identifica a 3 094 de 5 000. El grupo más pequeño (k mínimo) es de 90 personas con solo la edad y de 1 en cuanto aparece una persona única. Aparte, con un diccionario de 200 000 correos plausibles, el hash SHA-256 sin clave recuperó 2 000 de 2 000 correos; con HMAC y clave aparte, 0.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-359
def se323_analizador() -> Fig:
    nombres = ["Añadir columna NOT NULL sin valor por defecto", "Quitar una columna", "Renombrar una columna", "UPDATE sin WHERE",
               "Crear un índice que bloquea escrituras", "Sin plan de reversión", "Sin tiempo máximo de espera de bloqueo",
               "Cambiar el tipo de una columna", "Relleno que omite filas (nota > 0)", "Relleno con la columna equivocada",
               "Relleno antes de crear la columna", "Valor por defecto equivocado"]
    total = [13, 17, 25, 18, 17, 18, 15, 18, 17, 22, 11, 9]
    visto = total[:8] + [0, 0, 0, 0]
    return stacked_bars(
        "Analizador de migraciones sobre 200 mutaciones: 141 detectadas",
        "Barras apiladas horizontales con las mutaciones detectadas y no detectadas por un analizador de texto sobre 200 mutaciones: detecta las 141 de forma, como un NOT NULL sin valor por defecto, un UPDATE sin WHERE o un índice bloqueante, y ninguna de las 59 que cambian el sentido: un relleno que omite filas, con la columna equivocada, en orden inverso o con un valor por defecto equivocado.",
        nombres,
        [("Detectadas", visto, "teal"), ("No detectadas", [t - v for t, v in zip(total, visto)], "coral")],
        unit="Mutaciones de cada tipo", horizontal=True, label_w=330,
        note="Las cuatro mutaciones que no ve son las que dañan los datos sin romper la sintaxis. Las reglas se escribieron conociendo las mutaciones, así que el 100 % por tipo es optimista. El analizador trabaja sobre texto: no ejecuta nada.",
        note_kind="gold", foot=SINT)


def se323_ensayo() -> Fig:
    return grouped_bars(
        "Defectos de migración que muestra cada entorno de ensayo (6 migraciones defectuosas, 10 000 filas de origen)",
        "Barras con los defectos detectados de seis migraciones defectuosas según el entorno de ensayo: un esquema vacío no detecta ninguno; una muestra de 100 filas detecta tres; una copia completa de 10 000 filas detecta las seis, incluidos los que dependen de pocas filas, como siete correos duplicados o treinta notas en cero.",
        ["Esquema vacío", "Muestra de 100 filas", "Copia completa de 10 000 filas"],
        [("Defectos detectados", [0, 3, 6], "teal")],
        unit="Defectos detectados de 6", ticks=[0, 2, 4, 6], plot_h=240,
        ref_lines=[(6, "6 migraciones defectuosas")],
        note="Una muestra aleatoria encuentra los defectos frecuentes y no los raros; un ensayo en una copia completa y con invariantes comprobados después encuentra ambos. Los siete duplicados y las treinta notas en cero son construcciones del autor. La tabla de la clase indica qué defecto ve cada entorno.",
        note_kind="teal", foot=SINT)


def se323_cortes() -> Fig:
    return timeline(
        "Una migración de cinco pasos cortada antes de cada paso (seis puntos de corte)",
        "Diagrama de secuencia de una migración de cinco pasos y del estado que deja un corte antes de cada paso: con cada paso confirmado por separado, cuatro de seis cortes dejan un esquema intermedio, con las dos columnas o solo con la nueva; con todos los pasos en una transacción, ninguno deja un estado intermedio, porque SQLite admite DDL transaccional.",
        [("Pasos de la migración", [(0, 1, "1 añadir", "navy"), (1, 2, "2 copiar", "navy"), (2, 3, "3 índice", "navy"), (3, 4, "4 quitar", "navy"),
                                    (4, 5, "5 renombrar", "navy"), (5, 6, "fin", "grey")]),
         ("Cada paso confirmado por separado: esquema si se corta", [(0, 1, "anterior", "teal"), (1, 2, "intermedio", "coral"), (2, 3, "intermedio", "coral"),
                                                                       (3, 4, "intermedio", "coral"), (4, 5, "intermedio", "coral"), (5, 6, "nuevo", "teal")]),
         ("Todos los pasos en una transacción: esquema si se corta", [(0, 5, "siempre el esquema anterior, completo", "teal"), (5, 6, "nuevo", "teal")])],
        unit="Punto de corte: antes del paso indicado (el sexto no corta)", ticks=[0, 1, 2, 3, 4, 5, 6], t_max=6, lane_h=56,
        note="Los intermedios son dos columnas «estado» y «estado_v2» a la vez, o solo «estado_v2» tras quitar la vieja. La seguridad de un corte depende del motor: SQLite y PostgreSQL permiten DDL transaccional, MySQL confirma implícitamente cada sentencia DDL. El experimento usa SQLite y un corte como excepción en el cliente; no prueba el comportamiento de ningún otro motor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-360
def se324_validador() -> Fig:
    nombres = ["Campo del respaldo ausente", "Migración sin down", "RPO objetivo menor que el intervalo de copia", "Copia en el mismo volumen que los datos",
               "Prueba de restauración vencida (más de 90 días)", "Retención mayor que el plazo legal", "Responsable colectivo",
               "Índice sin consulta que lo justifique", "Evidencia de restauración copiada de otro entorno", "Invariante sin prueba ejecutable",
               "Purga de retención nunca programada", "Clave de cifrado junto a la copia"]
    total = [18, 13, 23, 14, 17, 20, 11, 18, 9, 22, 17, 18]
    visto = total[:8] + [0, 0, 0, 0]
    return stacked_bars(
        "Validador del paquete de datos sobre 200 mutaciones: 134 detectadas",
        "Barras apiladas horizontales con las mutaciones detectadas y no detectadas por un verificador de forma y de coherencia sobre 200 mutaciones de un paquete de capa de datos: detecta las 134 de campos ausentes, plazos o números incoherentes, y ninguna de las 66 que dejan los campos plausibles: evidencia copiada de otro entorno, un invariante sin prueba que exista, una purga nunca programada o la clave junto a la copia.",
        nombres,
        [("Detectadas", visto, "teal"), ("No detectadas", [t - v for t, v in zip(total, visto)], "coral")],
        unit="Mutaciones de cada tipo", horizontal=True, label_w=330,
        note="Las cuatro que no ve son las que ocurren en la realidad cuando un paquete se rellena para aprobar. Las reglas se escribieron conociendo las mutaciones y cada tipo sale al 100 % o al 0 %: la exactitud real sobre paquetes reales es desconocida.",
        note_kind="gold", foot=SINT)


def se324_mes() -> Fig:
    return timeline(
        "Un mes con un borrado accidental (día 10) y una corrupción silenciosa (día 18, detectada el día 21)",
        "Línea de tiempo de un mes de 30 días con tres estrategias de respaldo: la copia diaria sin verificar solo conserva las copias de los días 28 a 30, todas posteriores a la corrupción del día 18; la copia diaria verificada conserva 14 copias sanas, de los días 4 a 17, y rechaza las del 18 en adelante; con una bitácora de cambios se recuperan además las 800 filas posteriores a la última copia sana.",
        [("A · diaria sin verificar: solo 3 copias retenidas", [(28, 30, "3", "coral")]),
         ("B · copia diaria verificada, 14 días", [(4, 17, "14 copias sanas", "teal"), (18, 30, "copias rechazadas", "coral")]),
         ("C · copias, igual que B", [(4, 17, "14 copias sanas", "teal"), (18, 30, "copias rechazadas", "coral")]),
         ("C · bitácora de cambios", [(0, 30, "bitácora: recupera las 800 filas posteriores a la última copia sana", "gold")])],
        unit="Día del mes", ticks=[0, 5, 10, 15, 20, 25, 30], t_max=30, lane_h=52, label_w=270,
        events=[(10, "10: borrado"), (18, "18: corrupción"), (21, "21: detectada")],
        note="La verificación convierte una corrupción detectada el día 21 en una detectada el día 18, y la retención larga deja una copia sana para usar; la bitácora cierra la brecha entre copias. Resultado del borrado del día 10: 200 de 2 000 filas perdidas en A y B, ninguna en C; en A quedan 68 valores alterados sin recuperar. Las cifras son de un sistema sintético de 200 filas nuevas al día y dos incidentes inyectados.",
        note_kind="teal", foot=SINT)


def se324_retencion() -> Fig:
    return scatter(
        "Retener 30 días de una base de 40 000 filas: bytes comprimidos frente a piezas al restaurar",
        "Dispersión con tres políticas de retención de 30 días: 30 copias completas comprimidas ocupan 16 237 980 bytes y se restauran con una sola pieza; cuatro completas semanales y 26 incrementales ocupan 11 614 707 y exigen hasta 7 piezas; una completa y 29 incrementales ocupan 11 081 253 y exigen hasta 30.",
        [("30 copias completas", [(1, 16.237980, "16 237 980 B", "r")], "coral"),
         ("4 completas semanales + 26 incrementales", [(7, 11.614707, "11 614 707 B", "t")], "gold"),
         ("1 completa + 29 incrementales", [(30, 11.081253, "11 081 253 B", "t")], "teal")],
        x_label="Piezas que hay que aplicar al restaurar, en el peor caso", y_label="Bytes comprimidos (millones)",
        x_ticks=[(1, "1"), (7, "7"), (30, "30")], y_ticks=[0, 5, 10, 15, 20], y_zero=True, decimals=2,
        note="La compresión reduce una copia completa al 18 % y un incremental por páginas, aunque toque el 67 % de las páginas, al 12 %. Los incrementales ahorran un 30 %, pero cada eslabón es un punto de fallo. Con la zlib de Ubuntu las cifras difieren en menos de un 1 %.",
        note_kind="gold", foot=SINT)


FIGURES = {
    "se-355-lecturas-obsoletas-y-cuorum.svg": se319_replicas,
    "se-355-claves-que-se-mueven.svg": se319_movimiento,
    "se-355-sesgo-de-carga-por-clave.svg": se319_sesgo,
    "se-356-politicas-de-cache.svg": se320_politicas,
    "se-356-estampida-tras-expirar.svg": se320_estampida,
    "se-356-carrera-de-invalidacion.svg": se320_carrera,
    "se-357-perdida-segun-el-intervalo.svg": se321_perdida,
    "se-357-copia-en-caliente.svg": se321_caliente,
    "se-357-niveles-de-verificacion.svg": se321_niveles,
    "se-358-restos-tras-borrar.svg": se322_restos,
    "se-358-retencion-y-datos-vencidos.svg": se322_retencion,
    "se-358-personas-unicas.svg": se322_unicidad,
    "se-359-analizador-de-migraciones.svg": se323_analizador,
    "se-359-ensayo-en-datos-reales.svg": se323_ensayo,
    "se-359-cortes-durante-una-migracion.svg": se323_cortes,
    "se-360-validador-del-paquete-de-datos.svg": se324_validador,
    "se-360-un-mes-con-dos-incidentes.svg": se324_mes,
    "se-360-coste-de-retener-respaldos.svg": se324_retencion,
}
