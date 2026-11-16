"""Figures for SE-223 to SE-228 (synthetic data, fixed seeds; CPython 3.12.9 on Windows 11 and 3.12.3 on Ubuntu 24.04 under WSL2; times are one machine's)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, heatmap, stacked_bars
from figure_diagrams import fan
from figures_part07_a import bars


SINT = "Datos sintéticos y procesos locales; Windows (CPython 3.12.9) y Ubuntu/WSL2 (3.12.3); los tiempos son de un equipo."


# ---------------------------------------------------------------- SE-223
def se223_solapes() -> Fig:
    return grouped_bars(
        'Un trabajo cada 60 s cuya duración varía: tres políticas durante 1 440 ejecuciones',
        "Barras agrupadas con el efecto de tres políticas en un trabajo cada 60 segundos durante 1 440 ejecuciones: sin bloqueo hay 271 arranques solapados con duración mediana de 40 s y 1 353 con 55 s; omitir deja 174 y 439 ejecuciones sin hacer; encolar retrasa el inicio hasta 79 y 576 segundos.",
        ["Sin bloqueo: arranques solapados", "Omitir si sigue activo: ejecuciones omitidas", "Encolar en orden: retraso máximo de inicio (s)"],
        [("Mediana 40 s (14,0 % superan el periodo)", [271, 174, 79], "teal"), ("Mediana 55 s (41,7 % superan el periodo)", [1353, 439, 576], "coral")],
        unit="Arranques, ejecuciones o segundos según la política",
        note='Ninguna política arregla un trabajo que tarda más que su periodo: elige entre solapar (riesgo de corromper datos), omitir (datos que no se procesan) o encolar (retraso que crece). La señal para actuar es la proporción de ejecuciones que superan el periodo, no el promedio.', note_kind='coral', foot="Simulación con semilla 223: duraciones lognormales con sigma 0,35; supuestos del autor, no mediciones de un sistema.")


def se223_pools() -> Fig:
    return grouped_bars(
        'Hilos y procesos para trabajo de espera y de cálculo',
        "Barras horizontales en escala logarítmica con el tiempo de cada estrategia en Windows y en Ubuntu: 40 esperas de 0,05 s tardan 2,01 s en secuencial y 0,25 s con ocho hilos; ocho cálculos de CPU no se aceleran con hilos (4,95 s frente a 2,27 s en Windows) y sí con cuatro procesos (1,31 s); arrancar procesos cuesta 0,41 s en Windows.",
        ["40 esperas: secuencial", "40 esperas: 8 hilos", "40 esperas: 4 procesos", "8 cálculos de CPU: secuencial", "8 cálculos: 8 hilos", "8 cálculos: 4 procesos", "Arrancar 2 procesos con 2 tareas triviales"],
        [("Windows", [2.01, 0.25, 1.14, 2.27, 4.95, 1.31, 0.41], "coral"), ("Ubuntu (WSL2)", [2.01, 0.26, 0.52, 1.16, 1.34, 0.54, 0.06], "teal")],
        unit="Tiempo (s)", horizontal=True, log=True, label_w=270, ticks=[0.01, 0.1, 1, 10],
        note='Los hilos sirven para esperar, no para calcular; los procesos sirven para calcular pero cuestan arranque (mucho más en Windows, que no puede hacer fork). Las cifras son medianas de tres ejecuciones en un equipo y variaron entre ejecuciones hasta 2 veces: se leen como orden de magnitud.', note_kind='gold', foot="Tiempos de un equipo con 8 procesadores lógicos; el patrón (no las cifras) es el hallazgo.")


def se223_veneno() -> Fig:
    return stacked_bars(
        '1 000 trabajos, 35 venenosos y 110 con un fallo transitorio, con presupuesto de 3 000 intentos',
        "Barras apiladas con el destino de 1 000 trabajos según la política de reintento: reintentar sin límite al frente de la cola completa 6 y deja 994 sin procesar; al final de la cola completa 965 y deja 35 sin procesar; limitar a tres intentos con cola de muertos completa 965 y aparta los 35 venenosos.",
        ["Reintentar sin límite, al frente de la cola", "Reintentar sin límite, al final de la cola", "Máximo 3 intentos y cola de muertos"],
        [("Completados", [6, 965, 965], "teal"), ("En cola de muertos", [0, 0, 35], "gold"), ("Sin procesar", [994, 35, 0], "coral")],
        unit="Trabajos", horizontal=True, label_w=300,
        note='Un solo trabajo que siempre falla, reintentado al frente de la cola, bloquea al resto: 994 trabajos sanos quedaron sin procesar. Un límite de intentos y un lugar donde esperan los fallidos convierten un bloqueo en una lista de revisión.', note_kind='coral', foot="Simulación con semilla 23; tasas del 3 % y del 10 % son supuestos del autor.")


# ---------------------------------------------------------------- SE-224
def se224_idempotencia() -> Fig:
    return dumbbell(
        'Una ejecución frente a tres: qué operaciones se pueden repetir',
        "Puntos unidos por una línea con el efecto observable tras una y tras tres ejecuciones de siete operaciones: anexar una línea, incrementar un contador y enviar un aviso pasan de 1 a 3; fijar un valor, el upsert por clave, crear si falta y enviar un aviso con clave de idempotencia se quedan en 1.",
        [("Anexar una línea", 1, 3), ("Fijar un valor", 1, 1), ("Incrementar un contador", 1, 3), ("Upsert por clave", 1, 1), ("Crear si falta", 1, 1),
         ("Enviar un aviso (efecto externo)", 1, 3), ("Enviar un aviso con clave de idempotencia", 1, 1)],
        unit="Efecto observado (líneas, entradas, valor o avisos)", names=("Tras 1 ejecución", "Tras 3 ejecuciones"), decimals=0, label_w=290,
        delta=lambda a, b: "×3: no idempotente" if b > a else "igual: idempotente",
        note='La misma intención —«registrar la nota»— es idempotente como «fijar» y no lo es como «anexar». El efecto externo (un aviso) solo se vuelve repetible cuando se acompaña de una clave que el receptor recuerda.', note_kind='teal', foot="Simulación local en memoria; sin servicios reales; idéntica en ambos sistemas.")


def se224_caidas() -> Fig:
    return grouped_bars(
        'Caídas en cada paso de un lote de 20 filas (40 escenarios por estrategia)',
        "Barras horizontales con las caídas de 40 escenarios por estrategia de escritura: anexar sin punto de control deja 38 resultados incorrectos, marcar después 19 y marcar antes 40; reescribir en el sitio, anexar con clave y marcar antes deja 40 escenarios con un lector que vio un archivo incompleto; solo el temporal con os.replace no lo muestra nunca.",
        ["A. Reescribir en el sitio", "B. Anexar sin punto de control", "C. Anexar y marcar después", "D. Marcar antes de anexar", "E. Anexar con clave de fila", "F. Temporal y os.replace"],
        [("Resultados finales incorrectos", [0, 38, 19, 40, 0, 0], "coral"), ("Veces que un lector vio un archivo incompleto", [40, 40, 40, 40, 40, 0], "gold")],
        unit="Escenarios de caída, de 40", horizontal=True, label_w=250, ticks=[0, 10, 20, 30, 40],
        note='Reanudar sin más información o duplica o pierde, según el orden de escribir y marcar. La salida correcta combina dos ideas distintas: una clave que hace repetible cada fila (E) y un reemplazo atómico que oculta el trabajo a medias (F).', note_kind='gold', foot="Exhaustivo: 20 puntos de caída × 2 variantes; idéntico en Windows y Ubuntu.")


def se224_reemplazo() -> Fig:
    return fan(
        'Reemplazar un archivo que otro proceso mantiene abierto',
        "Diagrama de reemplazar o borrar un archivo que otro proceso mantiene abierto: en Windows os.replace y os.remove fallan con PermissionError; en Ubuntu ambos se permiten y el lector conserva el contenido anterior; tras cerrar el lector el reemplazo funciona.",
        ("Un lector mantiene el archivo abierto", "otro proceso intenta reemplazarlo o borrarlo", "navy"),
        [("os.replace sobre el destino abierto", "Windows: PermissionError (errno 13, WinError 5) · Ubuntu: reemplazo permitido; el lector sigue viendo el contenido viejo", "coral"),
         ("os.remove con el archivo abierto", "Windows: PermissionError (errno 13) · Ubuntu: borrado permitido", "coral"),
         ("Tras cerrar el lector", "el reemplazo funciona", "teal")],
        note='El reemplazo atómico no es igual de atómico en los dos sistemas: en Windows exige que nadie tenga el destino abierto y la automatización debe reintentar o fallar con un código temporal. La solución no es ignorar el error sino tratarlo como una condición esperada.', note_kind='coral', foot="Un proceso lector y un reemplazo en el mismo equipo; no se midieron antivirus, indexadores ni sistemas de red.")


# ---------------------------------------------------------------- SE-225
def se225_integridad() -> Fig:
    return heatmap(
        'Archivo sintético de 20 MB: qué comprobación detecta cada alteración',
        "Mapa de calor con qué comprobación cambia ante cada alteración de un archivo sintético de 20 MB: un bit alterado conserva la longitud pero cambia CRC32 y SHA-256; el truncado y el relleno cambian la longitud y los dos resúmenes; el archivo idéntico no cambia ninguna.",
        ["Un bit alterado", "Truncado en 1 000 bytes", "16 bytes añadidos al final", "Idéntico"],
        ["Longitud", "CRC32", "SHA-256"],
        [[0, 1, 1], [1, 1, 1], [1, 1, 1], [0, 0, 0]],
        unit="distinto frente al original", row_title="Alteración", col_title="¿La comprobación lo detecta?",
        scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "distinto" if v else "igual", highlight=[(0, 0)], cell_h=46, label_w=240,
        note='La longitud detecta un truncado pero no un bit alterado. El CRC32 detecta errores accidentales, pero se encontró una colisión entre dos mensajes de 8 bytes tras 87 650 intentos: no protege frente a quien alterara el archivo a propósito. SHA-256 corrió a unos 256 MB/s en Windows y 178 MB/s en Ubuntu en este equipo; un resumen publicado por el mismo canal que el binario no prueba su origen.', note_kind='gold', foot="Semilla 225; los resúmenes dan integridad frente a errores, no autenticidad: eso exige una firma o un canal independiente.")


def se225_escalonado() -> Fig:
    items = [
        ("Defecto 0,2 %: todos a la vez", 20, "coral", "20 rotos"),
        ("Defecto 0,2 %: escalonado (no se detiene)", 20, "gold", "20 rotos"),
        ("Defecto 2 %: todos a la vez", 194, "coral", "194 rotos"),
        ("Defecto 2 %: escalonado (se detiene al 1 %)", 3, "teal", "3 rotos"),
        ("Defecto 10 %: todos a la vez", 1002, "coral", "1 002 rotos"),
        ("Defecto 10 %: escalonado (se detiene al 1 %)", 11, "teal", "11 rotos"),
    ]
    return bars("Clientes rotos de 10 000 por un lanzamiento defectuoso",
                "Barras: con un defecto del 10 por ciento un lanzamiento a todos rompe 1 002 clientes y uno escalonado se detiene tras 11; con 2 por ciento rompe 194 frente a 3; con un defecto de 0,2 por ciento ambos rompen 20 porque el umbral de 1 por ciento nunca se supera.",
                items, 0.4, "El escalonamiento acota el daño de un defecto visible, pero con un defecto por debajo del umbral de detección completó el lanzamiento y rompió a 20 clientes de todos modos. El umbral y la señal de fallo son parte del diseño; sin ellos el escalonamiento es solo lentitud.",
                label_w=470, width=1050, note_kind="gold", foot="Simulación con semilla 5; el umbral del 1 % y las tasas de defecto son supuestos del autor.")


def se225_arranque() -> Fig:
    return grouped_bars(
        'Coste de arrancar y de ordenar versiones',
        "Barras horizontales con la mediana de 15 arranques de Python en Windows y en Ubuntu: el arranque mínimo tarda 281 ms y 44 ms; sin sitio ni usuario 100 ms y 17 ms; un zipapp de 167 bytes 267 ms y 36 ms; un directorio con archivo principal 235 ms y 29 ms; el sistema operativo pesa más que el empaquetado.",
        ["python -c pass", "python -I -S -c pass (sin sitio ni usuario)", "python notas.pyz (zipapp de 167 B)", "python app/ (directorio con __main__)"],
        [("Windows", [281, 100, 267, 235], "coral"), ("Ubuntu (WSL2)", [44, 17, 36, 29], "teal")],
        unit="Mediana de 15 arranques (ms)", horizontal=True, label_w=270,
        note='Empaquetar en un zipapp no cambia el arranque de forma apreciable: el intérprete domina. Lo que sí cambia es la corrección: 1.10.0 < 1.2.0 al ordenar como texto, y una actualización que «ve» una versión anterior como más nueva no se instala. Comparar versiones con tuplas numéricas.', note_kind='teal', foot="Un equipo; el antivirus y la caché de archivos afectan al arranque en Windows y no se controlaron.")


# ---------------------------------------------------------------- SE-226
def se226_unicidad() -> Fig:
    items = [
        ("1 atributo", 0.0, "teal", "0,0 %"),
        ("2 atributos", 0.0, "teal", "0,0 %"),
        ("3 atributos", 0.5, "teal", "0,5 %"),
        ("4 atributos", 7.1, "gold", "7,1 %"),
        ("5 atributos", 31.2, "coral", "31,2 %"),
        ("6 atributos", 67.5, "coral", "67,5 %"),
    ]
    return bars("Instalaciones únicas (de 5 000) según cuántos atributos «inocuos» se combinan",
                "Barras: con 5 000 instalaciones sintéticas, combinar 1 o 2 atributos como sistema, versión o idioma no deja a nadie único; con 3 es único el 0,5 por ciento, con 4 el 7,1, con 5 el 31,2 y con los 6 atributos es único el 67,5 por ciento.",
                items, 9, "Ningún atributo identifica a nadie por sí solo, pero la combinación sí: con los seis atributos dos de cada tres instalaciones quedan únicas. El riesgo no está en cada campo sino en juntar campos en un mismo registro.",
                label_w=190, width=900, note_kind="coral", foot="Distribuciones y atributos inventados con semilla 226: la proporción real de un producto dependería de sus datos.")


def se226_compuerta() -> Fig:
    return grouped_bars(
        'Una compuerta de consentimiento frente a cinco escenarios (servidor local en 127.0.0.1)',
        "Barras horizontales con cuántos de cinco escenarios detectan cada defecto de una compuerta de consentimiento: el código correcto no dispara ninguno, cuatro defectos y el opt-out explícito los detecta un único escenario cada uno y el que envía antes de decidir lo detectan los cinco.",
        ["Código correcto", "M1 activado por defecto", "M2 ignora DO_NOT_TRACK", "M3 ignora el entorno de CI", "M4 envía antes de decidir", "M6 incluye una ruta local", "M7 ignora el opt-out explícito"],
        [("Escenarios que lo detectan", [0, 1, 1, 1, 5, 1, 1], "teal")],
        unit="Escenarios que lo detectan, de 5", horizontal=True, label_w=250, ticks=[0, 1, 2, 3, 4, 5],
        note='Cada defecto exige su escenario: una suite con solo «opt-in» y «opt-out», los dos casos que cualquiera escribe, deja pasar tres de los seis. Las pruebas de una compuerta de privacidad se escriben por los casos en que NO debe salir nada.', note_kind='gold', foot="Servidor HTTP local que cuenta peticiones y examina la carga; no hay red ni servicio real.")


def se226_sesgo() -> Fig:
    items = [
        ("Adopción real de la función", 22.0, "grey", "22,0 %"),
        ("Estimada con opt-in sesgado (40 % / 4 %)", 52.8, "coral", "52,8 %"),
        ("Estimada con opt-in no sesgado (10 % / 10 %)", 22.0, "teal", "22,0 %"),
    ]
    return bars("Adopción de una función estimada solo con quienes aceptan telemetría",
                "Barras: en una población sintética de 100 000 donde 22 por ciento adopta la función, quienes aceptan telemetría son sobre todo usuarios intensivos y la estimación es 52,8 por ciento, 30,8 puntos de sesgo; si aceptaran igual todos los grupos la estimación sería 22,0.",
                items, 6, "Con más de 11 000 participantes el intervalo era de 52,0 a 53,6: más datos no corrigen el sesgo, solo lo hacen más seguro. El ruido de Laplace (epsilon 1) sobre un conteo agregado costó 1 % de error con n = 100 y 0,01 % con n = 10 000: la privacidad diferencial es barata a escala y no arregla quién participa.",
                label_w=420, width=1000, note_kind="coral", foot="Población sintética de 100 000 con semilla 226; las tasas de aceptación y de adopción son supuestos del autor.")


# ---------------------------------------------------------------- SE-227
def se227_matriz() -> Fig:
    return stacked_bars(
        'Diez fallos inyectados en una copia de seguridad: versión frágil frente a endurecida',
        "Barras apiladas con el resultado de diez fallos inyectados en una copia de seguridad: la versión frágil acierta en 2, se cuelga en 1 y daña en silencio en 7; la versión endurecida acierta en los 10 rechazando o fallando con códigos 2, 1, 65 o 75.",
        ["Versión frágil", "Versión endurecida"],
        [("Correcto", [2, 10], "teal"), ("Se cuelga", [1, 0], "gold"), ("Daño silencioso", [7, 0], "coral")],
        unit="Escenarios, de 10", horizontal=True, label_w=170,
        note='«Daño silencioso» significa código 0 con las copias viejas borradas o sin copia nueva. La versión frágil borra antes de copiar, no cita las rutas y no mira el código de salida; en siete de los diez escenarios el trabajo terminó con éxito aparente.', note_kind='coral', foot="Resultados idénticos en Windows y Ubuntu; la sintaxis de rutas con espacio y las tildes son los casos que más cambian entre sistemas.")


def se227_perdidas() -> Fig:
    items = [
        ("Sin bloqueo, Windows (mediana de 5)", 427, "coral", "427 perdidas"),
        ("Sin bloqueo, Ubuntu (mediana de 5)", 443, "coral", "443 perdidas"),
        ("Con bloqueo O_EXCL, Windows", 0, "teal", "0"),
        ("Con bloqueo O_EXCL, Ubuntu", 0, "teal", "0"),
    ]
    return bars("Actualizaciones perdidas de 450: tres procesos incrementan un contador guardado en un archivo",
                "Barras: tres procesos que incrementan 150 veces cada uno un contador en un archivo pierden en mediana 427 de las 450 actualizaciones en Windows y 443 en Ubuntu cuando no hay bloqueo, y 0 en ambos con un archivo de bloqueo creado en exclusiva.",
                items, 0.9, "Las pérdidas no son 1 o 2: casi todas, porque leer, sumar y escribir sin exclusión hace que cada proceso sobrescriba al otro (y abrir con «w» vacía el archivo antes de que otro lo lea). El bloqueo exclusivo corrigió todas las repeticiones, pero un bloqueo que sobrevive a un proceso muerto exige detectar bloqueos viejos.",
                label_w=400, width=1000, note_kind="gold", foot="Cinco repeticiones por sistema; las cifras varían entre ejecuciones (Windows 404–438, Ubuntu 442–448).")


def se227_citado() -> Fig:
    return heatmap(
        'Un nombre de archivo pasado como cadena con shell=True frente a una lista de argumentos',
        "Mapa de calor con el resultado de pasar ocho nombres de archivo como cadena con shell=True en Windows y en Ubuntu, o como lista de argumentos: la lista acierta en todos; la cadena falla o permite una inyección de comando en la mayoría, con una inyección en Windows y dos en Ubuntu.",
        ["a b.txt", "x;echo INYECTADO", "x&echo INYECTADO", "$HOME.txt", "'q'.txt", "(x).txt", "a|b.txt", "ñandú.txt"],
        ["Cadena, Windows (cmd)", "Cadena, Ubuntu (sh)", "Lista de argumentos"],
        [[1, 1, 0], [1, 2, 0], [2, 2, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 0], [1, 0, 1]],
        unit="0 bien, 1 mal, 2 inyección", row_title="Nombre de archivo", col_title="Resultado",
        scale="coral", vmin=0, vmax=2, cell_fmt=lambda v: "bien" if v == 0 else ("mal" if v == 1 else "inyección"), cell_h=36, label_w=200,
        note='La misma cadena se interpreta distinto según el shell. Con una lista de argumentos el sistema no reinterpreta nada. El único fallo restante (ñandú en Windows) es de otra naturaleza: la salida del hijo se escribió en la codificación local y el padre la leyó como UTF-8.', note_kind='coral', foot="Doce nombres de prueba; el comando ejecutado es un script que imprime sus argumentos, sin tocar archivos reales.")


# ---------------------------------------------------------------- SE-228
def se228_mutantes() -> Fig:
    return grouped_bars(
        'Trece pruebas de contrato sobre la herramienta de referencia y seis defectos inyectados',
        "Barras horizontales con las pruebas de contrato, de trece, que fallan en cada variante: la herramienta de referencia falla 1 en la primera ejecución (las abreviaturas no se heredan en los subcomandos) y 0 tras corregirla; cada uno de los seis defectos inyectados lo detectan de 1 a 3 pruebas.",
        ["Herramienta limpia, primera ejecución", "Herramienta corregida", "entorno_gana", "error_en_stdout", "salida_1_generica", "escritura_directa", "traceback_utf8", "abreviaturas"],
        [("Pruebas que fallan", [1, 0, 1, 2, 3, 1, 1, 1], "coral")],
        unit="Pruebas de contrato que fallan, de 13", horizontal=True, label_w=260, ticks=[0, 1, 2, 3, 4],
        note='La suite se probó a sí misma: cada defecto inyectado fue detectado por al menos una prueba, y antes de eso encontró un defecto real de la herramienta que no se había inyectado. Ninguno de los seis defectos fue visible en las pruebas del camino feliz (T01, T02, T05): cayeron en errores, precedencia y escritura.', note_kind='teal', foot="Resultados idénticos en Windows y Ubuntu; la herramienta es sintética (notas.py) y no es un producto.")


def se228_manifiesto() -> Fig:
    items = [
        ("Mutantes del manifiesto (borrar, tipo, valor)", 102, "grey", "102"),
        ("Detectados por el validador estructural", 102, "teal", "102"),
        ("Afirmaciones falsas con forma válida (de 5)", 5, "coral", "5 aceptadas"),
    ]
    return bars("Un validador de manifiesto de operabilidad: lo que ve y lo que no",
                "Barras: de 102 mutantes de un manifiesto de 17 campos el validador estructural detecta los 102; pero acepta las 5 afirmaciones falsas con forma válida, como declarar SIGTERM sin manejarlo o publicar un hash sha256 que en realidad es md5.",
                items, 4.2, "Un manifiesto completo no prueba una herramienta operable: el validador comprueba presencia, tipos y valores, no que la herramienta haga lo que declara. Por eso el manifiesto remite a pruebas de contrato por cada afirmación y a evidencia por plataforma.",
                label_w=420, width=1000, note_kind="coral", foot="Mutantes con semilla 228 (60 pares de campos borrados); las cinco afirmaciones falsas son ejemplos escritos por el autor.")


def se228_flaky() -> Fig:
    items = [
        ("Espera fija de 0,35 s, Windows sin carga", 1, "gold", "1 de 20"),
        ("Espera fija de 0,35 s, Windows con 16 procesos ocupados", 20, "coral", "20 de 20"),
        ("Espera por evento, Windows con carga", 0, "teal", "0 de 20"),
        ("Espera fija de 0,35 s, Ubuntu con carga (dos ejecuciones)", 4, "gold", "0 y 4 de 20"),
        ("Espera por evento, Ubuntu con carga", 0, "teal", "0 de 20"),
    ]
    return bars("Falsos fallos de una prueba que arranca un proceso: esperar un tiempo o esperar un evento",
                "Barras: una prueba que espera 0,35 segundos a que un proceso diga que está listo falló 1 de 20 veces en Windows sin carga y 20 de 20 con 16 procesos ocupando la CPU; esperar el evento no falló nunca; en Ubuntu con carga falló 0 y 4 veces en dos ejecuciones.",
                items, 18, "El proceso era correcto siempre: lo que fallaba era la suposición de cuánto tarda en arrancar. Una prueba que depende de un tiempo mide la carga de la máquina; una que espera la señal de que el servicio está listo (con un límite generoso) mide el servicio.",
                label_w=520, width=1100, note_kind="gold", foot="Mediciones en un equipo con 8 procesadores lógicos; los falsos fallos varían entre ejecuciones y se leen como orden de magnitud.")


FIGURES = {
    "se-223-politicas-ante-solapes.svg": se223_solapes,
    "se-223-hilos-y-procesos.svg": se223_pools,
    "se-223-trabajo-venenoso.svg": se223_veneno,
    "se-224-operaciones-repetibles.svg": se224_idempotencia,
    "se-224-caidas-en-cada-paso.svg": se224_caidas,
    "se-224-reemplazo-con-destino-abierto.svg": se224_reemplazo,
    "se-225-integridad-de-un-binario.svg": se225_integridad,
    "se-225-lanzamiento-escalonado.svg": se225_escalonado,
    "se-225-arranque-y-versiones.svg": se225_arranque,
    "se-226-combinar-atributos-identifica.svg": se226_unicidad,
    "se-226-compuerta-de-consentimiento.svg": se226_compuerta,
    "se-226-sesgo-del-opt-in.svg": se226_sesgo,
    "se-227-diez-fallos-inyectados.svg": se227_matriz,
    "se-227-actualizaciones-perdidas.svg": se227_perdidas,
    "se-227-citado-de-argumentos.svg": se227_citado,
    "se-228-pruebas-de-contrato-y-defectos.svg": se228_mutantes,
    "se-228-lo-que-no-ve-el-manifiesto.svg": se228_manifiesto,
    "se-228-esperar-un-tiempo-o-un-evento.svg": se228_flaky,
}
