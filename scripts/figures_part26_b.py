"""Figures for SE-319 to SE-324 (synthetic data, fixed seeds, SQLite 3.45; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos con semilla fija; SQLite 3.45 en Windows y Ubuntu (WSL2); cifras idénticas salvo donde se indica."


# ---------------------------------------------------------------- SE-319
def se319_replicas() -> Fig:
    rows = [
        ["Leer del líder", "0 %"],
        ["Leer de una réplica al azar (retardo medio 50 ms, lectura a 0–200 ms)", "24,37 %"],
        ["Leer siempre de la misma réplica", "24,46 %"],
        ["Leer de una réplica con la versión de la escritura (8,3 % van al líder)", "0 %"],
        ["Cuórum de 3 réplicas, escribir en 1 y leer 1", "66,7 %"],
        ["Escribir en 1 y leer 2, o escribir en 2 y leer 1", "33,4 % y 33,1 %"],
        ["Escribir en 2 y leer 2 (R + W > N)", "0 %"],
        ["Escribir en las 3 y leer 1, o escribir en 1 y leer 3", "0 %"],
    ]
    return tab("Lecturas obsoletas tras una escritura propia: réplicas asíncronas y cuórum (100 000 y 60 000 pruebas)",
               "Tabla: con réplicas asíncronas, leer de una réplica cualquiera devuelve el valor viejo en cerca del 24 por ciento de las lecturas inmediatas a la propia escritura; leer del líder o de una réplica con la versión, ninguna. Con tres réplicas, el cuórum de uno y uno falla en el 66,7 por ciento y cualquier combinación con R más W mayor que N, en ninguna.",
               ["Estrategia de lectura", "Lecturas obsoletas"], rows, [640, 230], row_h=44, size=13,
               note="Que el 24 % sea alto depende de un retardo medio de 50 ms y una lectura uniforme entre 0 y 200 ms: son supuestos del autor, no medidas de una base real. Lo que se mantiene es la forma: la lectura propia necesita la versión o el líder, y el cuórum solo acierta si las dos mitades se solapan.",
               note_kind="coral", foot=SINT)


def se319_movimiento() -> Fig:
    rows = [
        ["Reparto por módulo N (4 → 5 nodos)", "79,9 %", "—"],
        ["Reparto por módulo N (16 → 17 nodos)", "94,2 %", "—"],
        ["Anillo de hash con 1 punto por nodo", "41,5 %", "2,07"],
        ["Anillo con 16 puntos por nodo", "17,0 %", "1,20"],
        ["Anillo con 128 puntos por nodo", "21,1 %", "1,06"],
        ["Anillo con 512 puntos por nodo", "20,8 %", "1,04"],
    ]
    return tab("Claves que cambian de nodo al añadir uno (100 000 claves) y desequilibrio con 5 nodos",
               "Tabla: repartir por el módulo del hash mueve el 79,9 por ciento de las claves al pasar de 4 a 5 nodos y el 94,2 al pasar de 16 a 17; un anillo con 128 puntos por nodo mueve el 21,1, cerca del ideal de 20, y reduce el desequilibrio entre nodos de 2,07 veces la media a 1,06.",
               ["Reparto", "Claves movidas", "Carga máxima / media"], rows, [470, 190, 220], row_h=44, size=13,
               note="El módulo es sencillo y obliga a mover casi todo; el anillo mueve solo lo que llega al nodo nuevo, pero con pocos puntos reparte desigual. El ideal al pasar de 4 a 5 nodos es mover 1/5 = 20 %. Hash MD5 de claves sintéticas; ningún motor de bases de datos real.",
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


# ---------------------------------------------------------------- SE-320
def se320_politicas() -> Fig:
    rows = [
        ["TTL de 10 operaciones", "12,7 %", "0,21 %", "165 849"],
        ["TTL de 100 operaciones", "37,5 %", "4,41 %", "118 707"],
        ["TTL de 1 000 operaciones", "64,6 %", "23,73 %", "67 182"],
        ["Sin TTL ni invalidación", "98,9 %", "85,49 %", "2 000"],
        ["Invalidar al escribir, TTL de 1 000", "62,9 %", "0 %", "70 507"],
        ["Escribir también en la caché, TTL de 1 000", "66,2 %", "0 %", "64 271"],
    ]
    return tab("Políticas de caché sobre 200 000 operaciones (5 % escrituras, 2 000 claves con popularidad Zipf)",
               "Tabla: con TTL solo, subir el plazo de 10 a 1 000 operaciones sube los aciertos de 12,7 a 64,6 por ciento y las lecturas obsoletas de 0,21 a 23,73; sin TTL ni invalidación el 85,49 por ciento de las lecturas son obsoletas; invalidar o escribir en la caché al escribir las deja en 0 y mantiene unos 63 a 66 por ciento de aciertos.",
               ["Política", "Aciertos", "Lecturas obsoletas", "Consultas a la base"], rows, [420, 130, 190, 180], row_h=44, size=13,
               note="El TTL cambia frescura por aciertos; la invalidación elimina la obsolescencia sin perder aciertos, pero solo si la invalidación llega siempre. Las obsolescencias no incluyen las carreras de la figura siguiente: aquí el modelo es secuencial.",
               note_kind="gold", foot=SINT)


def se320_estampida() -> Fig:
    rows = [
        ["Todas expiran a la vez, sin protección", "2 000", "8 640"],
        ["Todas expiran a la vez, una sola recarga por clave", "863", "2 000"],
        ["TTL con variación de ±10 %, sin protección", "423", "9 334"],
        ["TTL con variación de ±10 %, una sola recarga", "99", "2 136"],
        ["TTL con variación de ±30 %, sin protección", "167", "10 091"],
        ["TTL con variación de ±30 %, una sola recarga", "39", "2 354"],
    ]
    return tab("Consultas a la base tras expirar: 1 000 claves, 2 000 lecturas por segundo, TTL de 60 s, recarga de 2 s",
               "Tabla: si las 1 000 claves expiran a la vez, el pico llega a 2 000 consultas por segundo sin protección y a 863 con una sola recarga por clave; variar el TTL un 10 por ciento reduce el pico a 423 y a 99; un 30 por ciento a 167 y a 39. El total de consultas baja a unas 2 000 con recarga única.",
               ["Variante", "Pico de consultas por segundo", "Consultas en 180 s"], rows, [500, 230, 180], row_h=44, size=13,
               note="El pico y el total miden cosas distintas: la variación del TTL reparte el pico en el tiempo, la recarga única elimina las consultas repetidas. Combinadas, el pico baja de 2 000 a 39. Es un modelo discreto de un segundo, con una recarga de 2 s supuesta.",
               note_kind="teal", foot=SINT)


def se320_carrera() -> Fig:
    rows = [
        ["Escribir en la base y luego borrar la clave", "6", "1", "R1 W1 W2 R2: la lectura vieja llega después"],
        ["Borrar la clave y luego escribir en la base", "6", "2", "Un lector rellena entre las dos acciones"],
        ["Guardar con versión y no pisar una más nueva", "6", "0", "Se conserva siempre la más nueva"],
    ]
    return tab("Una lectura y una escritura concurrentes sobre la misma clave: órdenes que dejan la caché vieja",
               "Tabla: de los seis órdenes posibles de dos pasos de un lector y dos de un escritor, escribir en la base y luego borrar la clave deja la caché con el valor viejo en un orden; borrar primero y escribir después en dos; guardar con versión y no sobrescribir una más nueva, en ninguno.",
               ["Orden del escritor", "Órdenes", "Caché vieja", "Cuándo ocurre"], rows, [330, 100, 130, 360], row_h=56, size=13,
               note="Mientras la clave no expire, el valor viejo se sirve para siempre: el TTL solo acota cuánto dura. El error aparece una vez en seis intercalaciones, es decir, es raro, no inexistente, y solo se ve con pruebas de intercalación. El modelo tiene un lector y un escritor.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-321
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
    rows = [
        ["Base original, antes de la transferencia", "2 000 000", "ok"],
        ["Copia del archivo con una transacción sin confirmar", "1 999 803", "ok"],
        ["Copia con la API de copia en línea (backup)", "2 000 000", "ok"],
    ]
    return tab("Copiar el archivo de una base mientras otra transacción mueve 20 000 cupos",
               "Tabla: copiar el archivo de la base mientras una transacción está a medias produce una copia con suma de cupos 1 999 803 en vez de 2 000 000 y con integrity_check en ok; la API de copia en línea conserva la suma exacta.",
               ["Método", "Suma de cupos", "integrity_check"], rows, [500, 190, 180], row_h=48, size=13,
               note="La copia a medias está estructuralmente sana y es lógicamente falsa: integrity_check no ve un invariante de negocio. La API la corrige tomando una instantánea consistente. Con otro tamaño de caché o de transacción, la diferencia sería otra: lo que no cambia es que puede haber alguna.",
               note_kind="coral", foot=SINT)


def se321_niveles() -> Fig:
    rows = [
        ["Un bit invertido (50)", "0", "0", "25", "28", "12", "22"],
        ["Archivo truncado (25)", "0", "25", "0", "0", "0", "0"],
        ["Una página a ceros (25)", "0", "0", "25", "25", "18", "18"],
        ["Archivo vacío (10)", "10", "0", "0", "0", "10", "10"],
        ["Filas borradas (30)", "0", "0", "0", "0", "30", "30"],
        ["Notas alteradas (30)", "0", "0", "0", "0", "0", "30"],
        ["Copia de un esquema antiguo (30)", "0", "0", "0", "0", "30", "30"],
        ["Total detectado de 200", "10", "25", "50", "53", "100", "140"],
    ]
    return tab("Mutaciones de una copia que detecta cada nivel de verificación (200 mutaciones)",
               "Tabla: de 200 copias alteradas, el archivo vacío solo lo ve la comprobación más simple; abrir la base detecta 25 truncados; quick_check detecta 50; integrity_check 53; los conteos del manifiesto 100 y los conteos con suma y claves foráneas 140. Juntos, los niveles estructurales ven 88 y todos los niveles 180; 20 inversiones de un bit no se ven en ninguno.",
               ["Mutación (cantidad)", "Existe", "Se abre", "quick", "integrity", "Conteos", "Conteos + suma + FK"], rows, [310, 70, 90, 70, 100, 90, 160], row_h=40, size=12,
               note="Los niveles estructurales ven 88 de 200 y ninguna de las 90 mutaciones lógicas; sumar el manifiesto de negocio eleva la cifra a 180. Los 20 bits que quedan sin ver cayeron en texto sin invariante o en espacio libre. Cada nivel es acumulativo en costo: el último exige conocer el negocio.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-322
def se322_restos() -> Fig:
    rows = [
        ["Borrado estándar", "2 090", "2 087", "2 087"],
        ["secure_delete activado", "2 000", "1 001", "1 001"],
        ["Borrado estándar + VACUUM", "2 090", "2 087", "1 085"],
        ["secure_delete + VACUUM, y copia hecha antes", "2 000", "1 001", "1 000 (la copia conserva 2 000)"],
    ]
    return tab("Ocurrencias de un valor identificable en el archivo tras borrar la mitad de 2 000 filas",
               "Tabla: borrar 1 000 de 2 000 filas deja 2 087 de las 2 090 ocurrencias en el archivo con el borrado estándar; con secure_delete queda aproximadamente la mitad; VACUUM elimina casi todas las del borrado estándar pero deja 1 085; y una copia hecha antes del borrado conserva las 2 000.",
               ["Procedimiento", "Antes", "Tras borrar 1 000", "Tras VACUUM"], rows, [380, 110, 180, 270], row_h=48, size=13,
               note="DELETE marca el espacio como libre pero no lo sobrescribe: el dato borrado sigue legible en el archivo. El valor de «antes» supera 2 000 porque los desbordes de páginas dejan copias viejas. Ninguna política de borrado alcanza las copias de seguridad.",
               note_kind="coral", foot=SINT)


def se322_retencion() -> Fig:
    rows = [
        ["Sin límite de retención", "720 000", "480 000", "67 %"],
        ["Conservar 24 meses", "480 000", "240 000", "50 %"],
        ["Conservar 12 meses", "240 000", "0", "0 %"],
        ["Conservar 6 meses", "120 000", "0", "0 %"],
    ]
    return tab("Eventos de acceso tras 36 meses según la retención (20 000 eventos al mes; plazo legítimo de 12 meses)",
               "Tabla: tras 36 meses con 20 000 eventos al mes, sin retención hay 720 000 filas y 480 000 de ellas con más de 12 meses; con 24 meses de retención quedan 480 000 y 240 000 vencidas; con 12 o 6 meses ninguna vencida.",
               ["Política", "Filas", "Con más de 12 meses", "Porcentaje"], rows, [350, 140, 220, 140], row_h=48, size=13,
               note="Es un cálculo aritmético, no una medición: el plazo de 12 meses es un supuesto del autor y cada institución debe fijar el suyo con su base legal. Muestra que una retención sin purga programada convierte datos legítimos en pasivo con el tiempo.",
               note_kind="gold", foot=SINT)


def se322_unicidad() -> Fig:
    rows = [
        ["Edad", "90", "0", "48"],
        ["Edad + comuna", "1", "161", "1 388"],
        ["Edad + comuna + año de ingreso", "1", "3 094", "3 969"],
        ["Edad + comuna + año + curso", "1", "4 876", "4 938"],
        ["Edad en rangos de 10 + 6 zonas + año", "1", "2", "248"],
        ["Edad en rangos de 20 + 3 zonas + año en bloques de 4", "1", "1", "32"],
    ]
    return tab("Personas únicas según los atributos que se combinan (5 000 personas sintéticas)",
               "Tabla: con solo la edad, el grupo más pequeño tiene 90 personas y ninguna es única; con edad y comuna hay 161 personas únicas; con edad, comuna y año, 3 094 de 5 000; con el curso también, 4 876. Generalizar a rangos baja a 2 y a 1 persona única, pero el k mínimo sigue siendo 1.",
               ["Atributos combinados", "k mínimo", "Personas únicas", "Grupos"], rows, [450, 110, 170, 140], row_h=44, size=13,
               note="Quitar el nombre no anonimiza: combinar tres atributos que parecen inofensivos identifica a 3 094 de 5 000. Aparte, con un diccionario de 200 000 correos plausibles, el hash SHA-256 sin clave recuperó 2 000 de 2 000 correos; con HMAC y clave aparte, 0.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-323
def _lint_rows() -> list[list[str]]:
    return [
        ["Añadir columna NOT NULL sin valor por defecto", "13 de 13"],
        ["Quitar una columna", "17 de 17"],
        ["Renombrar una columna", "25 de 25"],
        ["UPDATE sin WHERE", "18 de 18"],
        ["Crear un índice que bloquea escrituras", "17 de 17"],
        ["Sin plan de reversión", "18 de 18"],
        ["Sin tiempo máximo de espera de bloqueo", "15 de 15"],
        ["Cambiar el tipo de una columna", "18 de 18"],
        ["Relleno que omite filas (nota > 0)", "0 de 17"],
        ["Relleno con la columna equivocada", "0 de 22"],
        ["Relleno antes de crear la columna", "0 de 11"],
        ["Valor por defecto equivocado", "0 de 9"],
    ]


def se323_analizador() -> Fig:
    return tab("Analizador de migraciones sobre 200 mutaciones: 141 detectadas",
               "Tabla: un analizador de texto detecta 141 de 200 mutaciones de una migración segura, todas las de forma como un NOT NULL sin valor por defecto, un UPDATE sin WHERE o un índice bloqueante, y ninguna de las 59 que cambian el sentido: un relleno que omite filas, con la columna equivocada, en orden inverso o con un valor por defecto equivocado.",
               ["Mutación", "Detectadas"], _lint_rows(), [620, 200], row_h=32, size=12,
               note="Las cuatro mutaciones que no ve son las que dañan los datos sin romper la sintaxis. Las reglas se escribieron conociendo las mutaciones, así que el 100 % por tipo es optimista. El analizador trabaja sobre texto: no ejecuta nada.",
               note_kind="gold", foot=SINT)


def se323_ensayo() -> Fig:
    rows = [
        ["Índice único sobre el correo (7 duplicados en 10 000)", "No", "No", "Sí: falla el UNIQUE"],
        ["Relleno que omite las 30 notas en cero", "No", "No", "Sí: 30 filas sin valor"],
        ["Nota de decimal a entero", "No hay datos", "Sí", "Sí"],
        ["Recortar el correo a 4 caracteres", "No", "Sí: 2 colisiones", "Sí: 8 998 colisiones"],
        ["Relleno limitado a 5 000 filas", "No", "No", "Sí: 5 000 sin valor"],
        ["CHECK de rango sobre datos viejos (nota ≤ 7)", "No", "Sí: falla el CHECK", "Sí: falla el CHECK"],
    ]
    return tab("Qué defectos de migración muestra cada entorno de ensayo (10 000 filas de origen)",
               "Tabla: sobre un esquema vacío ninguna de seis migraciones defectuosas se detecta; sobre una muestra de 100 filas se detectan tres; sobre una copia completa de 10 000 filas, las seis. Los defectos que dependen de pocas filas, como siete correos duplicados o treinta notas en cero, solo aparecen con los datos completos.",
               ["Defecto de la migración", "Esquema vacío", "Muestra de 100", "Copia completa"], rows, [380, 140, 190, 220], row_h=48, size=12,
               note="Una muestra aleatoria encuentra los defectos frecuentes y no los raros; un ensayo en una copia completa y con invariantes comprobados después encuentra ambos. Los siete duplicados y las treinta notas en cero son construcciones del autor.",
               note_kind="teal", foot=SINT)


def se323_cortes() -> Fig:
    rows = [
        ["Cada paso confirmado por separado", "4 de 6", "Columnas «estado» y «estado_v2» a la vez, o solo «estado_v2»"],
        ["Todos los pasos en una transacción", "0 de 6", "Siempre el esquema anterior o el nuevo, completo"],
    ]
    return tab("Una migración de cinco pasos cortada antes de cada paso (seis puntos de corte)",
               "Tabla: si cada paso de la migración se confirma por separado, 4 de 6 cortes dejan un esquema intermedio con las dos columnas o solo con la nueva; si todos los pasos van en una transacción, ninguno deja un estado intermedio, porque SQLite admite DDL transaccional.",
               ["Variante", "Cortes con estado intermedio", "Estados observados"], rows, [330, 190, 360], row_h=56, size=13,
               note="La seguridad de un corte depende del motor: SQLite y PostgreSQL permiten DDL transaccional, MySQL confirma implícitamente cada sentencia DDL. El experimento usa SQLite y un corte como excepción en el cliente; no prueba el comportamiento de ningún otro motor.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-324
def se324_validador() -> Fig:
    rows = [
        ["Campo del respaldo ausente", "18 de 18"],
        ["Migración sin down", "13 de 13"],
        ["RPO objetivo menor que el intervalo de copia", "23 de 23"],
        ["Copia en el mismo volumen que los datos", "14 de 14"],
        ["Prueba de restauración vencida (más de 90 días)", "17 de 17"],
        ["Retención mayor que el plazo legal", "20 de 20"],
        ["Responsable colectivo", "11 de 11"],
        ["Índice sin consulta que lo justifique", "18 de 18"],
        ["Evidencia de restauración copiada de otro entorno", "0 de 9"],
        ["Invariante sin prueba ejecutable", "0 de 22"],
        ["Purga de retención nunca programada", "0 de 17"],
        ["Clave de cifrado junto a la copia", "0 de 18"],
    ]
    return tab("Validador del paquete de datos sobre 200 mutaciones: 134 detectadas",
               "Tabla: un verificador de forma y de coherencia entre campos detecta 134 de 200 mutaciones de un paquete de capa de datos, todas las de campos ausentes, plazos o números incoherentes, y ninguna de las 66 que dejan los campos plausibles: evidencia copiada de otro entorno, un invariante sin prueba que exista, una purga nunca programada o la clave junto a la copia.",
               ["Mutación", "Detectadas"], rows, [640, 200], row_h=32, size=12,
               note="Las cuatro que no ve son las que ocurren en la realidad cuando un paquete se rellena para aprobar. Las reglas se escribieron conociendo las mutaciones y cada tipo sale al 100 % o al 0 %: la exactitud real sobre paquetes reales es desconocida.",
               note_kind="gold", foot=SINT)


def se324_mes() -> Fig:
    rows = [
        ["A: copia diaria, sin verificar, 3 días", "200 de 2 000", "Copia del 18 aceptada; ninguna anterior; 68 valores alterados sin recuperar", "3 (28–30)"],
        ["B: copia diaria verificada, 14 días", "200 de 2 000", "Copia del 18 rechazada; última sana el 17; 800 filas posteriores perdidas", "14 (4–17)"],
        ["C: B + bitácora de cambios", "0 de 2 000", "Última sana el 17; 800 filas recuperables desde la bitácora", "14 (4–17)"],
    ]
    return tab("Un mes con un borrado accidental (día 10) y una corrupción silenciosa (día 18, detectada el día 21)",
               "Tabla: con una copia diaria sin verificar y tres días de retención, el borrado del día 10 pierde 200 filas y la corrupción del día 18 queda en las tres copias retenidas, sin recuperar 68 valores; con verificación y catorce días, la copia del 18 se rechaza y se pierden 800 filas posteriores; con bitácora, esas filas se recuperan.",
               ["Estrategia", "Borrado (día 10)", "Corrupción (día 18)", "Copias retenidas"], rows, [270, 130, 380, 140], row_h=92, size=12,
               note="La verificación convierte una corrupción detectada el día 21 en una detectada el día 18, y la retención larga deja una copia sana para usar; la bitácora cierra la brecha entre copias. Las cifras son de un sistema sintético de 200 filas nuevas al día y dos incidentes inyectados.",
               note_kind="teal", foot=SINT)


def se324_retencion() -> Fig:
    rows = [
        ["30 copias completas comprimidas", "16 237 980", "1 copia"],
        ["4 completas semanales + 26 incrementales", "11 614 707", "Una completa + hasta 6 incrementales"],
        ["1 completa + 29 incrementales", "11 081 253", "Una completa + hasta 29 incrementales"],
    ]
    return tab("Bytes comprimidos para retener 30 días de una base de 40 000 filas y qué hay que encadenar al restaurar",
               "Tabla: retener 30 días con copias completas comprimidas ocupa unos 16 millones de bytes y se restaura con una sola copia; con cuatro completas semanales y 26 incrementales ocupa unos 11,6 millones y exige hasta 6 incrementales; con una completa y 29 incrementales, unos 11,1 millones y hasta 29 incrementales.",
               ["Política de 30 días", "Bytes comprimidos (Windows)", "Para restaurar hay que aplicar"], rows, [400, 220, 300], row_h=52, size=12,
               note="La compresión reduce una copia completa al 18 % y un incremental por páginas, aunque toque el 67 % de las páginas, al 12 %. Los incrementales ahorran un 30 %, pero cada eslabón es un punto de fallo. Con la zlib de Ubuntu las cifras difieren en menos de un 1 %.",
               note_kind="gold", foot=SINT)


FIGURES = {
    "se-319-lecturas-obsoletas-y-cuorum.svg": se319_replicas,
    "se-319-claves-que-se-mueven.svg": se319_movimiento,
    "se-319-sesgo-de-carga-por-clave.svg": se319_sesgo,
    "se-320-politicas-de-cache.svg": se320_politicas,
    "se-320-estampida-tras-expirar.svg": se320_estampida,
    "se-320-carrera-de-invalidacion.svg": se320_carrera,
    "se-321-perdida-segun-el-intervalo.svg": se321_perdida,
    "se-321-copia-en-caliente.svg": se321_caliente,
    "se-321-niveles-de-verificacion.svg": se321_niveles,
    "se-322-restos-tras-borrar.svg": se322_restos,
    "se-322-retencion-y-datos-vencidos.svg": se322_retencion,
    "se-322-personas-unicas.svg": se322_unicidad,
    "se-323-analizador-de-migraciones.svg": se323_analizador,
    "se-323-ensayo-en-datos-reales.svg": se323_ensayo,
    "se-323-cortes-durante-una-migracion.svg": se323_cortes,
    "se-324-validador-del-paquete-de-datos.svg": se324_validador,
    "se-324-un-mes-con-dos-incidentes.svg": se324_mes,
    "se-324-coste-de-retener-respaldos.svg": se324_retencion,
}
