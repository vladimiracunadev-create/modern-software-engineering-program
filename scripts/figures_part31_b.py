"""Figures for SE-378 to SE-384 (synthetic data, fixed seeds, virtual time; real probes on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Sondas reales en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); cada fila es una observación, no una norma."


# ---------------------------------------------------------------- SE-378
def se378_tormenta() -> Fig:
    rows = [
        ["Brownout de 10 s: sin reintentos", "70 req/s", "1,00", "0 de 10", "15 %"],
        ["Brownout: reintento inmediato", "235 req/s", "3,38", "10 de 10", "94 %"],
        ["Brownout: retardo exponencial", "232 req/s", "3,38", "10 de 10", "94 %"],
        ["Brownout: exponencial con jitter completo", "234 req/s", "3,38", "10 de 10", "94 %"],
        ["Brownout: jitter y presupuesto del 10 %", "88 req/s", "1,01", "0 de 10", "19 %"],
        ["Oleada de 400 clientes: sin reintentos", "14 por 100 ms", "1,00", "0 de 10", "0 %"],
        ["Oleada: reintento inmediato", "333 por 100 ms", "1,12", "0 de 10", "2 %"],
        ["Oleada: retardo exponencial", "332 por 100 ms", "1,11", "0 de 10", "1 %"],
        ["Oleada: exponencial con jitter completo", "143 por 100 ms", "2,53", "10 de 10", "67 %"],
    ]
    return tab("Reintentos tras un brownout de 10 s y tras una oleada sincronizada de 400 clientes (10 semillas cada caso)",
               "Tabla: en un brownout de 10 segundos con timeout de 1 segundo, el reintento inmediato, el exponencial y el jitter completo llevan el pico de 70 a unas 234 solicitudes por segundo y las diez semillas colapsan, con 94 por ciento del trabajo del servidor hecho para clientes que ya se fueron; un presupuesto de reintentos del 10 por ciento evita el colapso. En una oleada sincronizada el jitter reduce el pico de reintentos de 332 a 143 por cada 100 milisegundos pero las diez semillas entran en sobrecarga sostenida.",
               ["Escenario y política", "Pico de carga", "Intentos por solicitud", "Semillas que colapsan", "Trabajo inútil"], rows, [370, 170, 130, 140, 130], row_h=44, size=12,
               note="Tres políticas de espera distintas dan el mismo colapso porque el problema es la cantidad de trabajo, no su sincronización; lo evita el presupuesto. En la oleada el jitter aplana el pico pero reparte los reintentos de modo que muchos terminan justo después del timeout: 67 % del trabajo es inútil. Es un resultado de este modelo (el servidor solo descarta tras 1 s de espera), no una regla general.",
               note_kind="coral", foot=SINT)


def se378_capas() -> Fig:
    rows = [
        ["100 % (caído)", "1,00 / 0 %", "3,00 / 0 %", "27,00 / 0 %", "1,37 / 0 %"],
        ["50 %", "1,00 / 49 %", "1,75 / 88 %", "2,01 / 100 %", "1,37 / 69 %"],
        ["10 %", "1,00 / 90 %", "1,11 / 100 %", "1,11 / 100 %", "1,11 / 100 %"],
        ["0 %", "1,00 / 100 %", "1,00 / 100 %", "1,00 / 100 %", "1,00 / 100 %"],
    ]
    return tab("Tres capas encadenadas con hasta tres intentos cada una: intentos que llegan a la base de datos / solicitudes que terminan bien",
               "Tabla: con la base de datos caída, tres capas con tres intentos cada una envían 27 intentos a la base por cada solicitud del usuario, frente a 3 si solo reintenta el borde y 1,37 con un presupuesto del 10 por ciento; con un 50 por ciento de fallos independientes, reintentar en las tres capas lleva el éxito al 100 por ciento con 2,01 intentos por solicitud y el presupuesto lo deja en 69 por ciento.",
               ["Fallo de la base de datos", "Sin reintentos", "Solo el borde", "Las tres capas", "Presupuesto del 10 %"], rows, [210, 170, 170, 190, 200], row_h=52, size=12,
               note="Los reintentos son un buen remedio para fallos independientes y transitorios (10 %: de 90 % a 100 % con 1,11 intentos) y una trampa cuando la base está caída: la amplificación es 3 × 3 × 3. El presupuesto limita el daño y paga con éxito (69 % en lugar de 100 % al 50 % de fallo).",
               note_kind="gold", foot=SINT)


def se378_timeout() -> Fig:
    rows = [
        ["100 ms", "68,9 %", "90,36 %", "103 ms / 200 ms", "3,96"],
        ["200 ms", "95,9 %", "99,83 %", "94 ms / 310 ms", "1,88"],
        ["500 ms", "97,2 %", "99,93 %", "102 ms / 594 ms", "1,77"],
        ["1 s", "97,6 %", "99,95 %", "114 ms / 1 088 ms", "1,67"],
        ["3 s", "98,7 %", "99,98 %", "149 ms / 3 060 ms", "1,17"],
        ["10 s", "99,7 %", "100,00 %", "192 ms / 3 976 ms", "0,46"],
    ]
    return tab("Timeout por intento y un reintento: 97 % de peticiones de ~80 ms, 3 % lentas y 0,2 % que no responden",
               "Tabla: con un timeout de 100 milisegundos solo el 68,9 por ciento de los primeros intentos tiene éxito y el servidor hace 3,96 veces más trabajo inútil que útil; con 200 milisegundos el éxito con un reintento es 99,83 por ciento y la latencia media 94 milisegundos; con 10 segundos el éxito es total pero el percentil 99 llega a 3 976 milisegundos.",
               ["Timeout", "Éxito con 1 intento", "Éxito con reintento", "Latencia media / p99", "Trabajo tras el abandono / útil"], rows, [150, 190, 190, 210, 200], row_h=46, size=12,
               note="No existe un timeout correcto en abstracto: uno demasiado corto crea carga (3,96) y uno demasiado largo retiene recursos y alarga la cola (p99 de 3 976 ms). El cociente baja con timeouts largos porque lo inútil se limita a 30 s en el modelo. Un plazo para varias llamadas en serie debe repartirse: tres de 1 s con un reintento suman hasta 6 s.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-379
def se379_interruptor() -> Fig:
    rows = [
        ["Sin interruptor", "4 430", "0", "1 637", "2 000 ms", "—"],
        ["5 fallos seguidos, abierto 2 s", "165", "5 860", "59", "50 ms", "2,2 s / 4,0 s"],
        ["5 fallos seguidos, abierto 10 s", "155", "5 859", "59", "50 ms", "6,5 s / 11,4 s"],
        ["5 fallos seguidos, abierto 30 s", "152", "6 270", "59", "50 ms", "11,6 s / 31,8 s"],
        ["50 % de 20 llamadas, abierto 10 s", "160", "5 861", "59", "50 ms", "6,6 s / 11,5 s"],
    ]
    return tab("Una dependencia que se cuelga 60 s a 100 req/s: efecto de un interruptor de circuito según sus parámetros",
               "Tabla: sin interruptor, 4 430 llamadas llegan a la dependencia caída, 1 637 solicitudes se rechazan por pool agotado y el percentil 99 del usuario es de 2 000 milisegundos; con un interruptor las llamadas bajan a unas 150, el percentil 99 a 50 milisegundos y la recuperación tras sanar tarda en promedio entre 2,2 y 11,6 segundos según cuánto tiempo permanezca abierto.",
               ["Configuración", "Llamadas a la dependencia", "Respuestas de respaldo", "Rechazadas por pool agotado", "p99 del usuario", "Recuperación media / máx"], rows, [250, 130, 120, 140, 120, 160], row_h=58, size=12,
               note="Abrir cuesta 59 rechazos igualmente: detectar cinco fallos de 2 s lleva 2 s y en ese tiempo entran 200 solicitudes a un pool de 150. Abierto más tiempo protege más y tarda más en volver. Con una dependencia con 40 % de fallos aleatorios (el 60 % de las llamadas tendría éxito), el de 2 s se abre 133 veces y responde con respaldo el 65 % de las solicitudes; el de 10 s, 31 veces y el 92 %.",
               note_kind="gold", foot=SINT)


def se379_mamparos() -> Fig:
    rows = [
        ["Un pool compartido de 20", "100,0 % / 100,0 %", "74,3 % / 73,6 %"],
        ["A 15 y B 5", "100,0 % / 99,6 %", "100,0 % / 23,1 %"],
        ["A 10 y B 10", "99,5 % / 100,0 %", "99,6 % / 45,0 %"],
        ["A 18 y B 2", "100,0 % / 79,6 %", "100,0 % / 9,3 %"],
    ]
    return tab("Dos dependencias (A: 80 req/s de 50 ms; B: 20 req/s) y 20 trabajadores: solicitudes atendidas A / B",
               "Tabla: con un pool compartido de 20 trabajadores y la dependencia B lenta, la A deja de atender el 25,7 por ciento de sus solicitudes; con pools separados A queda en 100 por ciento y B atiende entre 9,3 y 45 por ciento según su tamaño.",
               ["Reparto de trabajadores", "B sana (50 ms): A / B", "B lenta (1 s): A / B"], rows, [330, 300, 290], row_h=50, size=13,
               note="El mamparo no arregla B: lo confina. Cuesta capacidad ociosa (con B sana, 18 + 2 rechaza el 20 % de B) y exige dimensionar cada compartimento. A 10 y B 10 protege a A y deja a B en 45 %, y no existe un reparto que dé lo mejor a ambos.",
               note_kind="teal", foot=SINT)


def se379_degradar() -> Fig:
    rows = [
        ["Sin control", "3,0 % (p99 1 989 ms)", "3,7 %", "5,6"],
        ["Cola acotada a 50", "53,9 % (p99 930 ms)", "52,3 %", "82,0"],
        ["Prioridad a las críticas", "100,0 % (p99 271 ms)", "40,3 %", "81,6"],
        ["Prioridad y respuesta degradada", "100,0 % (p99 243 ms)", "100,0 % (4 919 degradadas)", "155,9"],
    ]
    return tab("Sobrecarga de 2 × (160 req/s sobre 80 de capacidad, 20 % críticas) durante 60 s: respuestas útiles dentro de 2 s",
               "Tabla: sin control casi nada llega a tiempo, 3 por ciento de las críticas; una cola acotada a 50 reparte el daño y atiende el 53,9 por ciento de las críticas; priorizar las críticas las atiende todas, 100 por ciento, y las no críticas el 40,3; añadir una respuesta degradada de bajo costo atiende todas las solicitudes con 155,9 respuestas útiles por segundo.",
               ["Política", "Críticas a tiempo", "No críticas a tiempo", "Respuestas útiles por segundo"], rows, [300, 230, 240, 170], row_h=52, size=12,
               note="La degradación bajo control es una decisión de producto: qué es crítico y qué respuesta barata sigue siendo útil. El 155,9 supone que la respuesta degradada cuesta 5 ms en lugar de 50 ms (supuesto del autor): si degradar costara lo mismo, no habría ganancia.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-380
def se380_disponibilidad() -> Fig:
    rows = [
        ["Un componente (MTBF 500 h, MTTR 0,5 h)", "0,99899", "529", "0,99900 → 526"],
        ["Serie: web, aplicación y base de datos", "0,99701", "1 574", "0,99700 → 1 575"],
        ["Dos réplicas independientes de la aplicación", "0,99801", "1 044", "0,99800"],
        ["Dos réplicas y 4 despliegues malos al año de 1 h", "0,99756", "1 282", "0,99800 si fueran independientes"],
    ]
    return tab("Disponibilidad simulada durante 400 años según la arquitectura y la causa común de fallo",
               "Tabla: tres componentes en serie con 99,9 por ciento cada uno dan 99,70 por ciento, unos 1 574 minutos de caída al año; duplicar solo la aplicación sube a 99,80 por ciento porque web y base de datos siguen siendo un punto único; cuatro despliegues malos al año que tumban ambas réplicas la bajan a 99,756 por ciento.",
               ["Configuración", "Disponibilidad", "Minutos de caída al año", "Teoría"], rows, [420, 150, 170, 190], row_h=52, size=12,
               note="La réplica de una capa mejora el 99,70 % a un 99,80 % y nada más: los otros dos tramos en serie mandan. La causa común es la que quita el beneficio: la aplicación con dos réplicas pasa de 0,9999996 a 0,99955. Los MTBF y MTTR son supuestos del autor y las caídas independientes son un modelo, no una medición.",
               note_kind="gold", foot=SINT)


def se380_durabilidad() -> Fig:
    rows = [
        ["2 réplicas, reparación de 1 h", "1,75e-05 (7 eventos)", "9,13e-06", "9,13e-08"],
        ["2 réplicas, reparación de 24 h", "2,35e-04", "2,19e-04", "2,19e-06"],
        ["2 réplicas, reparación de 168 h", "1,50e-03", "1,53e-03", "1,53e-05"],
        ["3 réplicas, reparación de 168 h", "1,00e-05 (10 eventos)", "8,83e-06", "8,83e-09"],
        ["3 réplicas, reparación de 336 h", "3,50e-05", "3,53e-05", "3,53e-08"],
        ["3 réplicas, reparación de 24 h", "no observable", "1,80e-07", "1,80e-10"],
    ]
    return tab("Probabilidad anual de perder un objeto con réplicas independientes según el tiempo de reparación",
               "Tabla: con una tasa anual de fallo de disco del 20 por ciento, dos réplicas con 24 horas de reparación pierden el objeto con probabilidad simulada 2,35 por diez mil al año, y la aproximación analítica da 2,19; pasar a tres réplicas con 168 horas baja la pérdida a 1 por cien mil. Con una tasa del 2 por ciento, tres réplicas con 24 horas dan 1,8 por diez mil millones al año.",
               ["Configuración", "Simulada (tasa anual 20 %)", "Aproximación 20 %", "Aproximación 2 %"], rows, [340, 220, 170, 170], row_h=50, size=12,
               note="La aproximación 8 760 · N · λᴺ · Rᴺ⁻¹ coincide con la simulación y enseña que la reparación pesa más que el número: 7 veces más tiempo, 7ᴺ⁻¹ más pérdida. Pero si el 0,1 % de los fallos afecta a las tres réplicas a la vez (mismo lote, misma sala, mismo error), la pérdida anual es 2,0e-05, cinco órdenes mayor que la independiente (1,8e-10).",
               note_kind="coral", foot=SINT)


def se380_deteccion() -> Fig:
    rows = [
        ["1,5 s", "1,0 s", "435,6", "0,07", "79 491"],
        ["2 s", "1,5 s", "219,0", "0,10", "39 968"],
        ["3 s", "2,5 s", "3,8", "0,17", "694"],
        ["5 s", "4,5 s", "1,07", "0,30", "195"],
        ["10 s", "9,5 s", "0,23", "0,63", "43"],
        ["30 s", "29,5 s", "0,00", "1,97", "0"],
    ]
    return tab("Detector de fallos por latidos de 1 s con pérdida del 0,5 % y pausas del emisor: umbral frente a conmutaciones falsas",
               "Tabla: con un umbral de 1,5 segundos hay unas 436 conmutaciones falsas por día y con 30 segundos prácticamente ninguna, pero la detección de una caída real tarda 1 segundo en promedio en el primer caso y 29,5 en el segundo; con 3 segundos se obtienen 3,8 conmutaciones falsas al día y 2,5 segundos de detección.",
               ["Umbral", "Detección media", "Conmutaciones falsas por día", "Min/año por detectar tarde (4 caídas)", "Min/año por conmutar sin motivo (30 s cada una)"], rows, [120, 170, 190, 210, 230], row_h=52, size=11,
               note="El umbral intercambia un tipo de pérdida por otro: 30 s cuestan 2 minutos al año en detección tardía y ninguno en conmutaciones falsas; 2 s cuestan 0,1 minutos y casi 40 000 en falsas. Las pausas del emisor (una cada 5 horas, mediana de 2 s) y la pérdida del 0,5 % son supuestos del autor.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-381
def se381_sondas() -> Fig:
    rows = [
        ["Separador de ruta y fin de línea", "«\\» y «\\r\\n»", "«/» y «\\n»"],
        ["Codificación por defecto de open() sin encoding", "cp1252", "UTF-8"],
        ["Bytes de «a», «ñ», «o» y salto de línea en modo texto", "61 f1 6f 0d 0a", "61 c3 b1 6f 0a"],
        ["«archivo.txt» existe tras crear «Archivo.TXT»", "Sí", "No"],
        ["Crear un archivo llamado «a:b»", "Error", "Sí"],
        ["8 directorios anidados de 50 caracteres", "Falla en el 4.º (252 caracteres)", "8 niveles (428 caracteres)"],
        ["os.rename sobre un archivo existente", "FileExistsError", "Sobrescribe sin error"],
        ["Borrar un archivo que sigue abierto", "PermissionError", "Borra"],
        ["datetime.fromtimestamp(-1)", "OSError", "1969"],
        ["time.strftime con «%-d»", "ValueError", "5"],
        ["os.getuid()", "AttributeError", "Un entero"],
        ["Método de arranque de multiprocessing", "spawn", "fork"],
    ]
    return tab("Doce sondas de portabilidad ejecutadas con el mismo script de Python en Windows 11 y en Ubuntu bajo WSL2",
               "Tabla: el mismo script de Python obtiene resultados distintos en Windows y Ubuntu en las doce sondas, entre ellas la codificación por defecto cp1252 frente a UTF-8, los bytes de un texto con eñe, la sensibilidad a mayúsculas, el límite de 260 caracteres de ruta, renombrar sobre un archivo existente, borrar un archivo abierto y el método de arranque de procesos.",
               ["Sonda", "Windows 11", "Ubuntu (WSL2)"], rows, [430, 270, 220], row_h=44, size=12,
               note="El texto «año» escrito sin encoding ocupa 5 bytes con salto de línea en ambos sistemas y los bytes son distintos: el tamaño no delata la diferencia. La ruta de Windows falla por el límite de 260 caracteres con la configuración de este equipo; con rutas largas habilitadas no fallaría.",
               note_kind="coral", foot=REAL)


def se381_interop() -> Fig:
    rows = [
        ["Identificadores de 40 y 53 bits convertidos a decimal de 64 bits", "0 de 100 000 cambian", "0 de 100 000"],
        ["Identificadores de 54 bits", "49 896 de 100 000 cambian (49,9 %)", "Pasan de 2⁵³"],
        ["Identificadores de 63 bits", "99 886 de 100 000 cambian (99,9 %)", "Casi todos"],
        ["«José» en NFC y en NFD de dos fuentes (2 000 pares)", "1 026 distintos con ==; 0 tras NFC", "Longitud 4 frente a 5"],
        ["Precios de 1 a 99 999 centavos con int(precio · 100)", "4 586 de 99 999 cambian (4,6 %)", "0 con round()"],
        ["Fechas de 2026 que dd/mm y mm/dd leen distinto", "132 de 365 (36,2 %)", "ISO 8601 sin ambigüedad"],
    ]
    return tab("Datos que cambian de significado al cruzar una frontera: medidas sobre cinco formatos",
               "Tabla: un identificador de 54 bits cambia en el 49,9 por ciento de los casos al pasar por un decimal de 64 bits y uno de 63 bits en el 99,9 por ciento, mientras que los de 53 bits o menos no cambian; dos fuentes con el mismo nombre en NFC y NFD difieren en 1 026 de 2 000 pares; 4,6 por ciento de los precios cambia al multiplicar por cien con decimales binarios; y el 36,2 por ciento de las fechas de 2026 se lee distinto como día-mes o mes-día.",
               ["Frontera y dato", "Medida", "Lectura"], rows, [400, 300, 220], row_h=56, size=12,
               note="Ninguno de estos fallos lanza una excepción: el dato llega y es otro. Un contrato de interoperabilidad debe fijar la representación (cadena para identificadores de más de 53 bits, normalización Unicode, enteros en centavos o decimales, fechas ISO 8601 con zona) y probar con valores en los bordes.",
               note_kind="gold", foot=SINT)


def se381_matriz() -> Fig:
    rows = [
        ["v1: id, estudiante, nota", "sí · sí · — · — · —", "sí · sí · — · — · —"],
        ["v2: añade comentario opcional", "— · sí · — · — · —", "sí · sí · — · — · —"],
        ["v3: renombra estudiante a alumno", "— · — · sí · — · —", "— · — · sí · — · —"],
        ["v4: la nota pasa de número a texto", "— · — · — · sí · sí", "— · — · — · sí · sí"],
        ["v5: añade el campo estado", "— · — · — · — · sí", "— · — · — · sí · sí"],
    ]
    return tab("Mensajes de la versión 1 a la 5 leídos por lectores de la versión 1 a la 5: 25 pares con lector estricto y con lector tolerante",
               "Tabla: con lectores estrictos que rechazan campos desconocidos son compatibles 7 de los 25 pares de versiones; con lectores tolerantes que ignoran campos desconocidos, 9 de 25; añadir un campo opcional solo es compatible hacia atrás con el lector tolerante, y renombrar un campo o cambiar el tipo de otro rompe con ambos.",
               ["Versión del productor", "Lector estricto: v1 · v2 · v3 · v4 · v5", "Lector tolerante: v1 · v2 · v3 · v4 · v5"], rows, [320, 300, 300], row_h=50, size=12,
               note="El lector tolerante gana 2 de 25 pares: los cambios aditivos. Renombrar (v3) y cambiar el tipo (v4) rompen en ambos sentidos y exigen expandir y contraer. La matriz se construye ejecutando los lectores, no leyendo la especificación. Es un modelo de cinco versiones, no un esquema real.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-382
def se382_campo() -> Fig:
    rows = [
        ["Laboratorio: solo equipo de escritorio rápido", "100 %", "—", "0,49 s", "—"],
        ["Equipo de escritorio rápido", "55 %", "0,41 s", "0,49 s", "0 %"],
        ["Teléfono medio", "35 %", "1,43 s", "1,69 s", "1 %"],
        ["Teléfono lento", "10 %", "4,16 s", "4,93 s", "98 %"],
        ["Campo: la población completa", "100 %", "—", "1,50 s", "10,2 %"],
    ]
    return tab("La misma página (440 KB) vista desde el laboratorio y desde tres segmentos de dispositivos",
               "Tabla: el laboratorio con un equipo de escritorio rápido da un percentil 75 de 0,49 segundos; el campo completo da 1,50 segundos y supera el límite de 2,5 segundos en el 10,2 por ciento de las cargas; el teléfono lento, que es el 10 por ciento de la población, tiene un percentil 75 de 4,93 segundos y el 98 por ciento de sus cargas supera 2,5.",
               ["Medición", "Población", "Mediana", "p75", "Cargas > 2,5 s"], rows, [380, 130, 120, 120, 170], row_h=50, size=12,
               note="El p75 de la población (1,50 s) cumple y deja fuera a quienes más lo necesitan: el 10 % con teléfono lento queda en 4,93 s. Para esa persona la página necesitaría 110 KB, o menos CPU, para llegar a 2,5 s. Los segmentos, los porcentajes y el modelo de tiempo son supuestos del autor; no se midió ningún navegador ni dispositivo.",
               note_kind="coral", foot=SINT)


def se382_deriva() -> Fig:
    rows = [
        ["Presupuesto absoluto de 1 000 KB", "Primera falla en la compilación 38 (+25 %)", "0 de 80"],
        ["Contra la compilación anterior, +2 %", "Falla en 21 de 79; ninguna por la deriva real", "15 de 79"],
        ["Tendencia: mediana de 3 contra las 10 primeras, +10 %", "Primera falla en la 26 (926 KB, +16 %)", "0 de 70"],
    ]
    return tab("Una deriva de peso del 0,6 % por compilación (de 800 KB a 1 324 KB en 80) frente a tres compuertas",
               "Tabla: el presupuesto absoluto de 1 000 kilobytes avisa recién en la compilación 38, cuando el peso ya subió un 25 por ciento; la compuerta contra la compilación anterior falla en 21 de 79 compilaciones por puro ruido y 15 de 79 sin deriva alguna; la compuerta de tendencia avisa en la compilación 26 con un 16 por ciento de aumento y no da falsas alarmas.",
               ["Compuerta", "Con deriva", "Falsas alarmas sin deriva"], rows, [380, 360, 180], row_h=56, size=12,
               note="Cada compilación solo engorda 0,6 %, por debajo del ruido de 1,2 %, y por eso la compuerta paso a paso no la ve (y se dispara por ruido). La tendencia ve el conjunto sin disparar: 12 compilaciones antes que el presupuesto absoluto, con la ventaja de llegar cuando aún hay margen.",
               note_kind="teal", foot=SINT)


def se382_contraste() -> Fig:
    rows = [
        ["Texto de figura sobre su relleno (seis tipos)", "9,91:1 a 16,12:1", "≥ 4,5:1: cumplen los seis"],
        ["Pie de las figuras (#5c1f14 sobre blanco)", "12,64:1", "Cumple"],
        ["Texto atenuado del portal sobre el papel", "5,24:1", "Cumple"],
        ["Enlaces del portal sobre el papel", "5,60:1", "Cumple"],
        ["Eyebrow del portal: coral #d85845 sobre el papel #f6f3ec", "3,51:1", "No cumple el 4,5:1 del texto pequeño"],
        ["Borde dorado de las figuras sobre blanco", "3,98:1", "Cumple el 3:1 de componentes gráficos"],
        ["Borde gris de las figuras sobre blanco", "2,90:1", "No cumple el 3:1 si el borde fuera la única señal"],
    ]
    return tab("Contraste WCAG medido con la fórmula de luminancia sobre los colores del propio repositorio",
               "Tabla: los seis tipos de recuadro de las figuras tienen entre 9,91 y 16,12 a 1 de contraste de texto; el pie, el texto atenuado y los enlaces del portal cumplen 4,5 a 1; el texto de la etiqueta superior del portal, coral sobre papel, llega a 3,51 a 1 y no cumple para texto pequeño; el borde gris de las figuras llega a 2,90 a 1.",
               ["Combinación", "Razón de contraste", "Criterio"], rows, [440, 190, 290], row_h=50, size=12,
               note="La medida es exacta y encuentra algo concreto: una etiqueta del portal por debajo del umbral. No prueba que la experiencia sea accesible: ninguna fórmula de contraste ve el orden de lectura, el foco ni el texto alternativo. En las figuras el borde nunca es la única señal, porque cada recuadro lleva texto.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-383
def se383_umbral() -> Fig:
    rows = [
        ["Máximo de una ejecución base de 5 min = 73 ms", "2,00 %", "46 de 100", "100 de 100"],
        ["Ese máximo × 1,5 = 110 ms", "0,00 %", "0 de 100", "41 de 100"],
        ["p99,9 de 30 ejecuciones base × 1,2 = 94 ms", "0,00 %", "0 de 100", "92 de 100"],
    ]
    return tab("Umbral de la hipótesis de estado estable (p95 por ventana de 10 s): falsas alarmas y detección de un +10 ms",
               "Tabla: un umbral tomado del máximo de una sola ejecución base produce falsas alarmas en 46 de 100 ejecuciones sanas pero detecta el aumento de 10 milisegundos en 100 de 100; multiplicarlo por 1,5 elimina las falsas alarmas y detecta solo 41 de 100; el percentil 99,9 de 30 ejecuciones base por 1,2 no da falsas alarmas y detecta 92 de 100.",
               ["Umbral", "Ventanas falsas", "Ejecuciones sanas con alarma", "Detecta +10 ms"], rows, [400, 130, 200, 190], row_h=56, size=12,
               note="Un solo experimento de base fija un umbral demasiado ajustado o demasiado holgado sin que se note. Con 30 ejecuciones base se conoce la forma del ruido y el umbral deja de ser una conjetura. El aumento de 10 ms sobre 50 ms de servicio (al 75 % de utilización) es un fallo sutil escogido por el autor.",
               note_kind="gold", foot=SINT)


def se383_matriz() -> Fig:
    rows = [
        ["Sin fallo", "0,0 % · p99 70 ms", "0,0 % · p99 70 ms"],
        ["+200 ms en la base de datos", "90,6 % errores · p99 1 968 ms · recupera en 5 s", "35,9 % errores · p99 1 481 ms"],
        ["20 % de errores de la base", "19,7 % errores", "0,0 % errores · 19,7 % degradadas"],
        ["Caída total de la base", "100 % errores · recupera en 10 s", "0,0 % errores · 100 % degradadas · p99 510 ms"],
        ["Tráfico × 5", "82,9 % errores · recupera en 15 s", "27,5 % errores · p99 276 ms"],
    ]
    return tab("Cuatro fallos inyectados 30 s en una API con 6 trabajadores y una base de datos (mediana de 10 semillas)",
               "Tabla: la configuración ingenua termina con 90,6 por ciento de errores con 200 milisegundos extra de la base, 100 por ciento con la base caída y 82,9 por ciento con tráfico cinco veces mayor; la endurecida con timeout de 0,5 segundos, interruptor, cola acotada y respaldo en caché baja esos errores a 35,9, 0 y 27,5 por ciento, y responde degradada al 100 por ciento cuando la base cae.",
               ["Fallo inyectado (60 s a 90 s)", "Configuración ingenua", "Configuración endurecida"], rows, [280, 330, 330], row_h=60, size=12,
               note="Endurecer cambia el tipo de fallo: de errores a respuestas degradadas, que son una decisión de producto. No sustituye a la capacidad: con +200 ms o con ×5 siguen los errores (35,9 % y 27,5 %) porque el sistema necesita más trabajadores. El modelo (6 trabajadores, 40 req/s, base de 30 ms) es una construcción del autor.",
               note_kind="teal", foot=SINT)


def se383_radio() -> Fig:
    rows = [
        ["2 %", "9 % · 0", "43 % · 2", "70 % · 5", "100 % · 48"],
        ["5 %", "33 % · 1", "94 % · 6", "100 % · 12", "100 % · 120"],
        ["20 %", "97 % · 5", "100 % · 24", "100 % · 48", "100 % · 480"],
    ]
    return tab("Error inyectado frente a fracción del tráfico afectado: detección / solicitudes erróneas esperadas (60 s a 40 req/s)",
               "Tabla: inyectar un error del 20 por ciento al 1 por ciento del tráfico se detecta el 97 por ciento de las veces con cinco solicitudes erróneas; inyectar un error del 2 por ciento solo se detecta con certeza al 100 por ciento del tráfico, con 48 solicitudes erróneas, y al 1 por ciento no se detecta en el 91 por ciento de las ejecuciones.",
               ["Error inyectado", "1 % del tráfico", "5 %", "10 %", "100 %"], rows, [210, 180, 180, 180, 190], row_h=54, size=12,
               note="Un fallo fuerte se descubre con un radio de impacto mínimo; un fallo sutil exige exponer más usuarios o ejecutar más tiempo, y eso hay que decidirlo antes. Detección: cola binomial exacta con error base de 0,3 % y nivel 1 %, estimada con 2 000 repeticiones por celda.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-384
def se384_validador() -> Fig:
    rows = [
        ["Quitar un campo obligatorio", "20 de 20", "Cambiar umbral y plan a la vez", "0 de 20"],
        ["Alterar una fila de los datos", "20 de 20", "Reemplazar datos, hash y resultados", "0 de 20"],
        ["Alterar un resultado un 10 %", "20 de 20", "Conservar solo la mitad más rápida", "0 de 20"],
        ["Invertir el veredicto", "20 de 20", "Un límite genérico pero extenso", "0 de 20"],
        ["Vaciar los límites («n/a»)", "20 de 20", "Borrar lo no medido («nada»)", "0 de 20"],
        ["Dejar el entorno incompleto", "20 de 20", "", ""],
        ["Cambiar el umbral sin el plan", "20 de 20", "", ""],
    ]
    return tab("Un validador de paquetes de informe frente a 240 mutaciones (12 operadores × 20): 140 detectadas",
               "Tabla: un validador que recalcula el hash de los datos, los percentiles, el veredicto y exige campos y un plan con hash detecta 20 de 20 en cada uno de siete operadores, como quitar un campo, alterar una fila o invertir el veredicto, y 0 de 20 en cinco operadores coherentes, como reemplazar los datos con su hash y sus resultados, cambiar a la vez el umbral y el plan o conservar solo la mitad más rápida.",
               ["Mutación detectada", "Detectadas", "Mutación no detectada", "Detectadas"], rows, [300, 120, 380, 120], row_h=44, size=12,
               note="Detecta 140 de 240 (58 %) y las 100 que se escapan son coherentes: el informe se contradice solo cuando algo se olvidó, no cuando se eligió. El hash prueba que los datos no cambiaron, no que sean los correctos; el plan con hash prueba el orden solo si se registró antes (por ejemplo, en un commit anterior).",
               note_kind="coral", foot=SINT)


def se384_reproducibilidad() -> Fig:
    rows = [
        ["resultados.json (estadísticos con semilla fija)", "Sí", "Sí"],
        ["correcto.csv (newline vacío, terminador explícito)", "Sí", "Sí"],
        ["informe_correcto.md (UTF-8 y \\n explícitos)", "Sí", "Sí"],
        ["ingenuo.csv (modo texto sin newline vacío)", "Sí", "No: \\r\\r\\n frente a \\r\\n"],
        ["informe_ingenuo.md (modo texto sin encoding)", "Sí", "No: cp1252 y \\r\\n frente a UTF-8 y \\n"],
        ["tiempos.json (reloj de pared)", "No", "No"],
        ["orden de un conjunto de cadenas (set)", "No", "No"],
        ["entorno.json (nombre del sistema)", "Sí", "No, por diseño"],
    ]
    return tab("Ocho artefactos del mismo canal: ¿idénticos entre dos ejecuciones? ¿idénticos entre Windows y Ubuntu? (SHA-256)",
               "Tabla: de ocho artefactos generados por el mismo programa, seis son idénticos entre dos ejecuciones en el mismo sistema y solo tres lo son entre Windows y Ubuntu; los resultados con semilla fija y los archivos escritos con codificación y fin de línea explícitos coinciden; el CSV y el informe escritos en modo texto por defecto difieren; el reloj y el orden de un conjunto cambian en cada ejecución.",
               ["Artefacto", "Igual entre dos ejecuciones", "Igual entre Windows y Ubuntu"], rows, [450, 210, 260], row_h=50, size=12,
               note="Reproducible no significa idéntico a nivel de bytes en todo: el reloj y el orden de un set nunca lo serán y hay que excluirlos del hash o declararlos. Los dos que difieren entre sistemas son defectos de escritura (modo texto sin newline ni encoding), no del experimento, y se corrigen sin tocar los datos.",
               note_kind="gold", foot=REAL)


def se384_seleccion() -> Fig:
    rows = [
        ["Mediana de 30 contra mediana de 30, una métrica, una vez", "0,1 %"],
        ["La mejor de 5 repeticiones de B contra una corrida de A", "23,1 %"],
        ["La mejor de 6 métricas, 30 contra 30", "59,1 %"],
        ["La mejor de 6 métricas y la mejor de 5 repeticiones de B", "96,4 %"],
    ]
    return tab("Dos versiones idénticas comparadas 4 000 veces: porcentaje de informes que declaran una mejora de al menos el 5 %",
               "Tabla: al comparar dos versiones idénticas, el procedimiento fijado de antemano con medianas de 30 corridas declara una mejora de al menos 5 por ciento en el 0,1 por ciento de los casos; elegir la mejor de cinco repeticiones lo sube a 23,1; elegir la mejor de seis métricas, a 59,1; y combinar ambas, a 96,4 por ciento.",
               ["Cómo se elige el resultado que se informa", "Informes con «mejora» ≥ 5 %"], rows, [680, 240], row_h=52, size=13,
               note="Nada del procedimiento es fraudulento paso a paso y casi todos los informes concluyen una mejora que no existe. La defensa es registrar antes la métrica, el número de repeticiones y el criterio, y publicar todas las corridas; el validador de la figura anterior no puede verificar el orden.",
               note_kind="coral", foot=SINT)


FIGURES = {
    "se-378-tormenta-de-reintentos.svg": se378_tormenta,
    "se-378-amplificacion-por-capas.svg": se378_capas,
    "se-378-eleccion-del-timeout.svg": se378_timeout,
    "se-379-interruptor-de-circuito.svg": se379_interruptor,
    "se-379-mamparos.svg": se379_mamparos,
    "se-379-degradar-bajo-sobrecarga.svg": se379_degradar,
    "se-380-disponibilidad-y-causa-comun.svg": se380_disponibilidad,
    "se-380-durabilidad-y-reparacion.svg": se380_durabilidad,
    "se-380-umbral-de-deteccion-de-fallos.svg": se380_deteccion,
    "se-381-doce-sondas-de-portabilidad.svg": se381_sondas,
    "se-381-datos-que-cambian-de-significado.svg": se381_interop,
    "se-381-matriz-de-compatibilidad.svg": se381_matriz,
    "se-382-campo-frente-a-laboratorio.svg": se382_campo,
    "se-382-deriva-de-peso.svg": se382_deriva,
    "se-382-contraste-medido.svg": se382_contraste,
    "se-383-umbral-de-estado-estable.svg": se383_umbral,
    "se-383-matriz-de-fallos.svg": se383_matriz,
    "se-383-deteccion-y-radio-de-impacto.svg": se383_radio,
    "se-384-validador-de-paquetes.svg": se384_validador,
    "se-384-reproducibilidad-entre-sistemas.svg": se384_reproducibilidad,
    "se-384-seleccion-de-resultados.svg": se384_seleccion,
}
