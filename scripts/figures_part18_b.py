"""Figures for SE-223 to SE-228 (synthetic data, fixed seeds; CPython 3.12.9 on Windows 11 and 3.12.3 on Ubuntu 24.04 under WSL2; times are one machine's)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos y procesos locales; Windows (CPython 3.12.9) y Ubuntu/WSL2 (3.12.3); los tiempos son de un equipo."


# ---------------------------------------------------------------- SE-223
def se223_solapes() -> Fig:
    rows = [["Sin bloqueo", "271 arranques solapados", "1 353 arranques solapados"],
            ["Omitir si sigue activo", "174 ejecuciones omitidas (1 266 hechas)", "439 omitidas (1 001 hechas)"],
            ["Encolar y ejecutar en orden", "Retraso máximo de inicio: 79 s", "Retraso máximo de inicio: 576 s"]]
    return tab("Un trabajo cada 60 s cuya duración varía: tres políticas durante 1 440 ejecuciones",
               "Tabla: con una duración mediana de 40 segundos y 14 por ciento de ejecuciones por encima del periodo, sin bloqueo hay 271 arranques solapados, omitir deja 174 sin ejecutar y encolar retrasa hasta 79 segundos; con mediana de 55 segundos y 41,7 por ciento por encima del periodo hay 1 353 solapes, 439 omitidas o un retraso de 576 segundos.",
               ["Política", "Mediana 40 s (14,0 % superan el periodo)", "Mediana 55 s (41,7 % superan el periodo)"], rows, [270, 380, 380], row_h=52,
               note="Ninguna política arregla un trabajo que tarda más que su periodo: elige entre solapar (riesgo de corromper datos), omitir (datos que no se procesan) o encolar (retraso que crece). La señal para actuar es la proporción de ejecuciones que superan el periodo, no el promedio.", note_kind="coral", foot="Simulación con semilla 223: duraciones lognormales con sigma 0,35; supuestos del autor, no mediciones de un sistema.")


def se223_pools() -> Fig:
    rows = [["40 esperas de 0,05 s: secuencial", "2,01 s", "2,01 s"],
            ["40 esperas: 8 hilos", "0,25 s", "0,26 s"],
            ["40 esperas: 4 procesos", "1,14 s", "0,52 s"],
            ["8 cálculos de CPU: secuencial", "2,27 s", "1,16 s"],
            ["8 cálculos: 8 hilos", "4,95 s", "1,34 s"],
            ["8 cálculos: 4 procesos", "1,31 s", "0,54 s"],
            ["Arrancar 2 procesos con 2 tareas triviales", "0,41 s", "0,06 s"]]
    return tab("Hilos y procesos para trabajo de espera y de cálculo",
               "Tabla: para 40 esperas de 0,05 segundos, ocho hilos tardan 0,25 segundos frente a 2,01 secuencial; para ocho cálculos de CPU los hilos no aceleran (4,95 s en Windows frente a 2,27 secuencial) y cuatro procesos sí lo hacen; arrancar un pool de procesos cuesta 0,41 segundos en Windows y 0,06 en Ubuntu.",
               ["Carga y estrategia", "Windows", "Ubuntu (WSL2)"], rows, [450, 270, 280], row_h=40,
               note="Los hilos sirven para esperar, no para calcular; los procesos sirven para calcular pero cuestan arranque (mucho más en Windows, que no puede hacer fork). Las cifras son medianas de tres ejecuciones en un equipo y variaron entre ejecuciones hasta 2 veces: se leen como orden de magnitud.", note_kind="gold", foot="Tiempos de un equipo con 8 procesadores lógicos; el patrón (no las cifras) es el hallazgo.")


def se223_veneno() -> Fig:
    rows = [["Reintentar sin límite, al frente de la cola", "6", "0", "3 000", "994"],
            ["Reintentar sin límite, al final de la cola", "965", "0", "3 000", "35"],
            ["Máximo 3 intentos y cola de muertos", "965", "35", "1 214", "0"]]
    return tab("1 000 trabajos, 35 venenosos y 110 con un fallo transitorio, con presupuesto de 3 000 intentos",
               "Tabla: reintentar sin límite un trabajo venenoso colocado al frente consume el presupuesto de 3 000 intentos y completa solo 6 trabajos; ponerlo al final completa 965 pero deja 35 venenosos circulando; limitar a tres intentos con cola de muertos completa 965 con 1 214 intentos y aparta los 35.",
               ["Política", "Completados", "En cola de muertos", "Intentos", "Sin procesar"], rows, [370, 130, 180, 130, 150], row_h=52,
               note="Un solo trabajo que siempre falla, reintentado al frente de la cola, bloquea al resto: 994 trabajos sanos quedaron sin procesar. Un límite de intentos y un lugar donde esperan los fallidos convierten un bloqueo en una lista de revisión.", note_kind="coral", foot="Simulación con semilla 23; tasas del 3 % y del 10 % son supuestos del autor.")


# ---------------------------------------------------------------- SE-224
def se224_idempotencia() -> Fig:
    rows = [["Anexar una línea", "1 línea", "3 líneas iguales", "No"],
            ["Fijar un valor", "nota = ent-1", "nota = ent-1", "Sí"],
            ["Incrementar un contador", "1", "3", "No"],
            ["Upsert por clave", "1 entrada", "1 entrada", "Sí"],
            ["Crear si falta", "1 borrador", "1 borrador", "Sí"],
            ["Enviar un aviso (efecto externo)", "1 aviso", "3 avisos", "No"],
            ["Enviar un aviso con clave de idempotencia", "1 aviso", "1 aviso", "Sí"]]
    return tab("Una ejecución frente a tres: qué operaciones se pueden repetir",
               "Tabla de siete operaciones ejecutadas una y tres veces: anexar, incrementar y enviar un aviso no son idempotentes; fijar un valor, el upsert por clave, crear si falta y enviar un aviso con clave de idempotencia sí lo son.",
               ["Operación", "Tras 1 ejecución", "Tras 3 ejecuciones", "Idempotente"], rows, [380, 220, 240, 190], row_h=40,
               note="La misma intención —«registrar la nota»— es idempotente como «fijar» y no lo es como «anexar». El efecto externo (un aviso) solo se vuelve repetible cuando se acompaña de una clave que el receptor recuerda.", note_kind="teal", foot="Simulación local en memoria; sin servicios reales; idéntica en ambos sistemas.")


def se224_caidas() -> Fig:
    rows = [["A. Reescribir en el sitio", "0", "40", "El resultado final es correcto, pero durante la caída hay un archivo vacío o incompleto"],
            ["B. Anexar sin punto de control", "38", "40", "38 reanudaciones duplican filas"],
            ["C. Anexar y marcar después", "19", "40", "La caída entre escribir y marcar duplica una fila"],
            ["D. Marcar antes de anexar", "40", "40", "Todas las reanudaciones pierden una fila"],
            ["E. Anexar con clave de fila", "0", "40", "Correcto: repetir no cambia el resultado"],
            ["F. Temporal y os.replace", "0", "0", "Correcto y nunca visible a medias"]]
    return tab("Caídas en cada paso de un lote de 20 filas (40 escenarios por estrategia)",
               "Tabla: seis estrategias de escritura con 40 escenarios de caída; reescribir en el sitio termina bien pero deja un archivo incompleto visible; anexar sin control duplica en 38; marcar después duplica en 19; marcar antes pierde en 40; anexar con clave y escribir a un temporal con reemplazo atómico terminan correctas, y solo la última no deja nunca un archivo incompleto.",
               ["Estrategia", "Resultados finales incorrectos", "Veces que un lector vio un archivo incompleto", "Qué pasó"], rows, [300, 190, 210, 330], row_h=66,
               note="Reanudar sin más información o duplica o pierde, según el orden de escribir y marcar. La salida correcta combina dos ideas distintas: una clave que hace repetible cada fila (E) y un reemplazo atómico que oculta el trabajo a medias (F).", note_kind="gold", foot="Exhaustivo: 20 puntos de caída × 2 variantes; idéntico en Windows y Ubuntu.")


def se224_reemplazo() -> Fig:
    rows = [["os.replace con el destino abierto por un lector", "PermissionError (errno 13, WinError 5)", "Reemplazo permitido; el lector sigue viendo el contenido viejo"],
            ["os.remove con el archivo abierto", "PermissionError (errno 13)", "Borrado permitido"],
            ["Tras cerrar el lector", "El reemplazo funciona", "No aplica"]]
    return tab("Reemplazar un archivo que otro proceso mantiene abierto",
               "Tabla: en Windows, os.replace sobre un archivo abierto por un lector falla con PermissionError y el borrado también; en Ubuntu ambos se permiten y el lector conserva el contenido anterior; tras cerrar el lector el reemplazo funciona en Windows.",
               ["Operación", "Windows", "Ubuntu (WSL2)"], rows, [380, 330, 330], row_h=66,
               note="El reemplazo atómico no es igual de atómico en los dos sistemas: en Windows exige que nadie tenga el destino abierto y la automatización debe reintentar o fallar con un código temporal. La solución no es ignorar el error sino tratarlo como una condición esperada.", note_kind="coral", foot="Un proceso lector y un reemplazo en el mismo equipo; no se midieron antivirus, indexadores ni sistemas de red.")


# ---------------------------------------------------------------- SE-225
def se225_integridad() -> Fig:
    rows = [["Un bit alterado", "Igual", "Distinto", "Distinto"],
            ["Truncado en 1 000 bytes", "Distinta", "Distinto", "Distinto"],
            ["16 bytes añadidos al final", "Distinta", "Distinto", "Distinto"],
            ["Idéntico", "Igual", "Igual", "Igual"]]
    return tab("Archivo sintético de 20 MB: qué comprobación detecta cada alteración",
               "Tabla: sobre un archivo sintético de 20 megabytes, un bit alterado conserva la longitud pero cambia CRC32 y SHA-256; el truncado y el relleno cambian la longitud y los resúmenes; el archivo idéntico coincide en todo; un CRC32 de 32 bits colisionó entre dos mensajes de 8 bytes tras 87 650 intentos.",
               ["Alteración", "Longitud", "CRC32", "SHA-256"], rows, [330, 220, 230, 230], row_h=44,
               note="La longitud detecta un truncado pero no un bit alterado. El CRC32 detecta errores accidentales, pero se encontró una colisión entre dos mensajes de 8 bytes tras 87 650 intentos: no protege frente a quien alterara el archivo a propósito. SHA-256 corrió a unos 256 MB/s en Windows y 178 MB/s en Ubuntu en este equipo; un resumen publicado por el mismo canal que el binario no prueba su origen.", note_kind="gold", foot="Semilla 225; los resúmenes dan integridad frente a errores, no autenticidad: eso exige una firma o un canal independiente.")


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
    rows = [["python -c pass", "281 ms", "44 ms"],
            ["python -I -S -c pass (sin sitio ni usuario)", "100 ms", "17 ms"],
            ["python notas.pyz (zipapp de 167 B)", "267 ms", "36 ms"],
            ["python app/ (directorio con __main__)", "235 ms", "29 ms"],
            ["Orden de 10 versiones como cadenas", "6 posiciones mal", "6 posiciones mal"]]
    return tab("Coste de arrancar y de ordenar versiones",
               "Tabla: el arranque mínimo de Python tardó 281 milisegundos en Windows y 44 en Ubuntu; un zipapp de 167 bytes añadió poco al arranque; ordenar diez versiones como cadenas coloca seis en posición equivocada, por ejemplo 1.10.0 antes que 1.2.0.",
               ["Qué se mide", "Windows (mediana de 15)", "Ubuntu (mediana de 15)"], rows, [450, 290, 290], row_h=44,
               note="Empaquetar en un zipapp no cambia el arranque de forma apreciable: el intérprete domina. Lo que sí cambia es la corrección: 1.10.0 < 1.2.0 al ordenar como texto, y una actualización que «ve» una versión anterior como más nueva no se instala. Comparar versiones con tuplas numéricas.", note_kind="teal", foot="Un equipo; el antivirus y la caché de archivos afectan al arranque en Windows y no se controlaron.")


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
    rows = [["Código correcto", "0 de 5", "—"],
            ["M1 activado por defecto", "1 de 5", "Primera ejecución sin configuración"],
            ["M2 ignora DO_NOT_TRACK", "1 de 5", "Opt-in con DO_NOT_TRACK=1"],
            ["M3 ignora el entorno de CI", "1 de 5", "Opt-in en un entorno de CI"],
            ["M4 envía antes de decidir", "5 de 5", "Todos: llega una petición siempre"],
            ["M6 incluye una ruta local", "1 de 5", "Opt-in explícito (inspecciona la carga)"],
            ["M7 ignora el opt-out explícito", "1 de 5", "Opt-out explícito"]]
    return tab("Una compuerta de consentimiento frente a cinco escenarios (servidor local en 127.0.0.1)",
               "Tabla: una suite de cinco escenarios contra el código correcto y seis defectos: cada defecto lo detecta un único escenario, salvo el que envía antes de decidir, que los cinco detectan; el opt-in explícito solo detecta la ruta local incluida en la carga.",
               ["Defecto inyectado", "Escenarios que lo detectan", "Cuál lo detecta"], rows, [380, 250, 400], row_h=40,
               note="Cada defecto exige su escenario: una suite con solo «opt-in» y «opt-out», los dos casos que cualquiera escribe, deja pasar tres de los seis. Las pruebas de una compuerta de privacidad se escriben por los casos en que NO debe salir nada.", note_kind="gold", foot="Servidor HTTP local que cuenta peticiones y examina la carga; no hay red ni servicio real.")


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
    rows = [["Normal", "Correcto", "Correcto"],
            ["Directorio de origen con espacio", "Daño silencioso", "Correcto"],
            ["Nombre con tilde y eñe", "Correcto", "Correcto"],
            ["Origen inexistente", "Daño silencioso", "Rechaza (código 2)"],
            ["Origen vacío", "Daño silencioso", "Rechaza (código 2)"],
            ["El destino es un archivo", "Daño silencioso", "Rechaza (código 2)"],
            ["La copia sale con código 3", "Daño silencioso", "Falla (código 1)"],
            ["La copia se cuelga 4 s", "Se cuelga", "Código 75 tras 1,5 s"],
            ["Copia a la mitad con código 0", "Daño silencioso", "Detecta (código 65)"],
            ["Otra instancia ya corre", "Daño silencioso", "Rechaza (código 75)"]]
    return tab("Diez fallos inyectados en una copia de seguridad: versión frágil frente a endurecida",
               "Tabla: ante diez escenarios, la versión frágil acierta en 2, se cuelga en 1 y daña en silencio en 7; la versión endurecida acierta en los 10, rechazando o fallando con códigos 2, 1, 65 o 75 sin tocar las copias existentes.",
               ["Escenario", "Versión frágil", "Versión endurecida"], rows, [400, 250, 380], row_h=34,
               note="«Daño silencioso» significa código 0 con las copias viejas borradas o sin copia nueva. La versión frágil borra antes de copiar, no cita las rutas y no mira el código de salida; en siete de los diez escenarios el trabajo terminó con éxito aparente.", note_kind="coral", foot="Resultados idénticos en Windows y Ubuntu; la sintaxis de rutas con espacio y las tildes son los casos que más cambian entre sistemas.")


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
    rows = [["a b.txt", "Mal", "Mal", "Bien"],
            ["x;echo INYECTADO", "Mal", "Inyección", "Bien"],
            ["x&echo INYECTADO", "Inyección", "Inyección", "Bien"],
            ["$HOME.txt", "Bien", "Mal (se expande)", "Bien"],
            ["'q'.txt", "Bien", "Mal", "Bien"],
            ["(x).txt", "Bien", "Mal", "Bien"],
            ["a|b.txt", "Mal", "Mal", "Bien"],
            ["ñandú.txt", "Mal (codificación)", "Bien", "Windows: mal por la codificación"]]
    return tab("Un nombre de archivo pasado como cadena con shell=True frente a una lista de argumentos",
               "Tabla: de doce nombres de archivo, seis se interpretan mal con shell=True en Windows y ocho en Ubuntu, con una inyección de comando en Windows y dos en Ubuntu; pasar los argumentos como lista los interpreta bien en Ubuntu y falla uno en Windows por la codificación de la salida del hijo.",
               ["Nombre", "Cadena, Windows (cmd)", "Cadena, Ubuntu (sh)", "Lista de argumentos"], rows, [250, 250, 250, 280], row_h=40,
               note="La misma cadena se interpreta distinto según el shell. Con una lista de argumentos el sistema no reinterpreta nada. El único fallo restante (ñandú en Windows) es de otra naturaleza: la salida del hijo se escribió en la codificación local y el padre la leyó como UTF-8.", note_kind="coral", foot="Doce nombres de prueba; el comando ejecutado es un script que imprime sus argumentos, sin tocar archivos reales.")


# ---------------------------------------------------------------- SE-228
def se228_mutantes() -> Fig:
    rows = [["Herramienta limpia, primera ejecución", "12 de 13", "T13: allow_abbrev no se hereda en subcomandos"],
            ["Herramienta corregida", "13 de 13", "—"],
            ["entorno_gana", "T09", "Precedencia: el entorno vence al flag"],
            ["error_en_stdout", "T04, T07", "Errores por la salida estándar"],
            ["salida_1_generica", "T04, T07, T08", "Un solo código 1 para datos inválidos"],
            ["escritura_directa", "T11", "Escribe sin archivo temporal"],
            ["traceback_utf8", "T08", "Traza en lugar de código 65"],
            ["abreviaturas", "T13", "Acepta --form por --formato"]]
    return tab("Trece pruebas de contrato sobre la herramienta de referencia y seis defectos inyectados",
               "Tabla: la suite de trece pruebas de contrato pasó 12 en la primera ejecución sobre la herramienta de referencia y reveló que las abreviaturas no se heredan en los subcomandos; tras corregirlo pasa 13; cada uno de los seis defectos inyectados lo detectan entre una y tres pruebas.",
               ["Variante", "Pruebas que fallan o pasan", "Qué se descubrió"], rows, [350, 240, 440], row_h=40,
               note="La suite se probó a sí misma: cada defecto inyectado fue detectado por al menos una prueba, y antes de eso encontró un defecto real de la herramienta que no se había inyectado. Ninguno de los seis defectos fue visible en las pruebas del camino feliz (T01, T02, T05): cayeron en errores, precedencia y escritura.", note_kind="teal", foot="Resultados idénticos en Windows y Ubuntu; la herramienta es sintética (notas.py) y no es un producto.")


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
