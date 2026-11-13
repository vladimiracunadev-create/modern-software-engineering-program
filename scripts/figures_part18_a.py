"""Figures for SE-217 to SE-222 (synthetic data, fixed seeds; CPython 3.12.9 on Windows 11 and 3.12.3 on Ubuntu 24.04 under WSL2; times are one machine's)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos y procesos locales; Windows (CPython 3.12.9) y Ubuntu/WSL2 (3.12.3); los tiempos son de un equipo."


# ---------------------------------------------------------------- SE-217
def se217_abreviaturas() -> Fig:
    items = [
        ("Prefijos probados de 5 flags", 15, "grey", "15"),
        ("Aceptados con 5 flags (v1)", 14, "teal", "14"),
        ("Aceptados tras añadir 3 flags (v2)", 5, "gold", "5"),
        ("Rotos por añadir flags sin tocar el código", 9, "coral", "9"),
        ("Aceptados con allow_abbrev=False", 0, "teal", "0"),
    ]
    return bars("Abreviaturas de flags que dejan de valer al añadir flags",
                "Barras: de 15 prefijos de flags de una herramienta con cinco opciones, 14 se aceptan; al añadir tres opciones nuevas solo 5 siguen aceptándose y 9 se rompen; con las abreviaturas desactivadas se aceptan 0.",
                items, 36, "Un script que escribió --sal y funcionaba deja de funcionar cuando aparece --salida-json: la abreviatura es un contrato implícito que cada flag nuevo puede romper. Desactivar las abreviaturas convierte el contrato en explícito.",
                label_w=400, width=1020, note_kind="coral", foot=SINT)


def se217_contrato() -> Fig:
    rows = [["-h", "0", "125 B", "0 B", "Ayuda: va a stdout"],
            ["Sin subcomando", "2", "0 B", "89 B", "Uso incorrecto: stderr"],
            ["Flag desconocido", "2", "0 B", "77 B", "Uso incorrecto: stderr"],
            ["Valor fuera de las opciones", "2", "0 B", "139 B (Ubuntu: 143 B)", "El texto del mensaje cambia entre versiones"],
            ["Invocación válida", "0", "12 B", "0 B", "Resultado: stdout; nada en stderr"]]
    return tab("Lo que observa quien invoca una CLI de argparse",
               "Tabla con cinco invocaciones de una herramienta de ejemplo: la ayuda sale con código 0 por la salida estándar; los cuatro tipos de uso incorrecto salen con código 2 y escriben solo en el error estándar; una invocación válida escribe 12 bytes y sale con 0.",
               ["Invocación", "Código", "stdout", "stderr", "Lectura"], rows, [250, 90, 110, 250, 330], row_h=52,
               note="El código 2 y la separación de flujos salen gratis de argparse, pero el texto exacto del mensaje no es contrato: entre Python 3.12.9 y 3.12.3 el mismo error midió 139 y 143 bytes. Quien automatice debe leer el código, no analizar el mensaje.", note_kind="gold", foot=SINT)


def se217_sugerencias() -> Fig:
    items = [
        ("Corte 0,6: acierta (de 294 erratas dobles)", 294, "teal", "294"),
        ("Corte 0,8: acierta", 193, "gold", "193"),
        ("Corte 0,8: sin sugerencia", 101, "coral", "101"),
        ("Corte 0,9: acierta", 23, "gold", "23"),
        ("Corte 0,9: sin sugerencia", 271, "coral", "271"),
        ("Corte 0,6: palabras ajenas con sugerencia (de 16)", 6, "coral", "6"),
        ("Corte 0,8: palabras ajenas con sugerencia (de 16)", 3, "gold", "3"),
    ]
    return bars("Sugerir el comando correcto ante un error de tecleo",
                "Barras: con 12 subcomandos y 294 erratas de dos ediciones, un corte de similitud de 0,6 acierta 294, de 0,8 acierta 193 y no sugiere en 101, de 0,9 acierta solo 23; ninguna sugerencia fue equivocada, pero con 0,6 seis de 16 palabras ajenas recibieron una sugerencia.",
                items, 1.35, "Ningún corte produjo una sugerencia equivocada ante erratas, pero un corte laxo sugiere «revisar» a quien escribió «crear». Una sugerencia es una ayuda y nunca una acción: la herramienta no debe ejecutar el comando adivinado.",
                label_w=480, width=1080, note_kind="gold", foot="Datos sintéticos con semilla 217: 12 subcomandos del dominio de la herramienta; resultados idénticos en ambos sistemas.")


# ---------------------------------------------------------------- SE-218
def se218_buffer() -> Fig:
    items = [
        ("Salida a tubería, por defecto", 1.2, "coral", "1,2 s"),
        ("print(flush=True)", 0.1, "teal", "0,1 s"),
        ("python -u", 0.1, "teal", "0,1 s"),
        ("PYTHONUNBUFFERED=1", 0.2, "teal", "0,2 s"),
    ]
    return bars("Tiempo hasta recibir la primera línea de un productor que emite una línea cada 0,1 s",
                "Barras: con la salida conectada a una tubería, el productor por defecto entrega la primera línea a los 1,2 segundos en Windows, cuando termina; con flush, con la opción -u o con la variable de entorno la entrega a los 0,1 a 0,2 segundos.",
                items, 330, "Con una tubería la salida se acumula en un búfer de bloque y llega al final: el consumidor ve las diez líneas juntas. En Ubuntu la serie fue 1,0 / 0,0 / 0,0 / 0,0 s: mismo mecanismo. Una herramienta que informa progreso debe vaciar el búfer o decirlo en su contrato.",
                label_w=300, width=1000, note_kind="coral", foot=SINT)


def se218_tuberia_rota() -> Fig:
    rows = [["Productor que captura la excepción", "Código 7 · OSError, errno 22", "Código 7 · BrokenPipeError, errno 32"],
            ["Productor sin manejo", "Código 1 · OSError: [Errno 22] Invalid argument", "Código 1 · BrokenPipeError: [Errno 32] Broken pipe"],
            ["Qué debe hacer una herramienta", "Tratar errno 22 y 32 como «el consumidor ya no quiere más»", "Salir en silencio con el código acordado, sin traza"]]
    return tab("Qué ocurre cuando el consumidor cierra la tubería tras una línea",
               "Tabla: ante el cierre anticipado de la tubería, un productor Python en Windows recibe OSError con errno 22 y uno en Ubuntu recibe BrokenPipeError con errno 32; sin manejo ambos terminan con código 1 y una traza.",
               ["Situación", "Windows", "Ubuntu (WSL2)"], rows, [250, 380, 400], row_h=66,
               note="El mismo hecho —leer una línea y cerrar— produce excepciones distintas. Una herramienta portable debe tratar ambas como una terminación normal del consumidor; imprimir una traza por haber usado «| head» es un defecto de la herramienta.", note_kind="gold", foot=SINT)


def se218_memoria() -> Fig:
    items = [
        ("Archivo CRLF de 400 000 líneas", 9.6, "grey", "9,6 MB"),
        ("read().splitlines(): pico de memoria", 37.7, "coral", "37,7 MB"),
        ("Iterar línea a línea: pico de memoria", 0.03, "teal", "0,03 MB"),
    ]
    return bars("Memoria máxima al procesar un archivo: cargarlo entero o iterar",
                "Barras: un archivo de 9,6 megabytes con 400 000 líneas necesita un pico de 37,7 megabytes si se lee entero y partir con splitlines, y 0,03 megabytes si se itera línea a línea.",
                items, 11, "Cargar el archivo cuesta unas cuatro veces su tamaño por los objetos de texto; iterar mantiene la memoria constante. En modo texto las 400 000 líneas CRLF llegan como «\\n»; en modo binario las 400 000 conservan el «\\r» final: la decisión sobre los saltos de línea cambia el contenido.",
                label_w=370, width=1020, note_kind="teal", foot="Datos sintéticos con semilla 218; tracemalloc; mismas cifras en Windows y Ubuntu.")


# ---------------------------------------------------------------- SE-219
def se219_precedencia() -> Fig:
    rows = [["El entorno gana al flag", "16", "No", "Sí"],
            ["El archivo gana al entorno", "4", "No", "Sí"],
            ["Un entorno vacío cuenta como definido", "3", "No", "No"],
            ["if flag: descarta el flag vacío", "14", "No", "No"],
            ["if archivo: descarta el valor vacío", "2", "No", "No"],
            ["Ignora el entorno", "6", "Sí", "Sí"]]
    return tab("Seis resolvedores defectuosos de precedencia frente a 64 combinaciones",
               "Tabla: de 64 combinaciones de cuatro valores por capa, seis resolvedores defectuosos difieren del correcto en 16, 4, 3, 14, 2 y 6 combinaciones; cuatro ejemplos de una sola capa solo detectan uno; tres ejemplos que combinan capas detectan dos más.",
               ["Defecto del resolvedor", "Combinaciones que difieren (de 64)", "Lo detectan 4 ejemplos de una capa", "Lo detectan + 3 ejemplos de varias capas"], rows, [330, 200, 230, 240], row_h=52,
               note="Los ejemplos de una sola capa no pueden distinguir el orden de dos capas. Tres de los seis defectos sobreviven incluso a siete ejemplos razonables: los que dependen del valor vacío exigen escribir ese caso a propósito.", note_kind="coral", foot="Enumeración exhaustiva de 4 × 4 × 4 combinaciones; sin aleatoriedad; idéntica en ambos sistemas.")


def se219_booleanos() -> Fig:
    rows = [["«0»", "True", "falso", "False"],
            ["«false» y «FALSE»", "True", "falso", "False"],
            ["«no» y «off»", "True", "falso", "False"],
            ["«1» y «true»", "True", "verdadero", "True"],
            ["«» (vacío)", "False", "sin definir", "Se trata como no definido"],
            ["«2»", "True", "desconocido", "Rechaza con un error de uso"],
            ["«٣» (dígito arábigo)", "int() lo lee como 3", "no es ASCII", "Rechaza: solo dígitos ASCII"]]
    return tab("Interpretar booleanos del entorno: bool(cadena) frente a un analizador estricto",
               "Tabla: bool aplicado a una cadena del entorno devuelve True para 0, false, FALSE, no y off, es decir, interpreta mal cinco de las doce cadenas reconocidas; un analizador estricto acepta ocho formas, trata el vacío como no definido y rechaza 2 y los dígitos no ASCII.",
               ["Valor del entorno", "bool(cadena)", "Significado", "Analizador estricto"], rows, [260, 220, 200, 340], row_h=52,
               note="bool(«false») es True porque la cadena no está vacía: cinco de las doce cadenas reconocidas se interpretan al revés. int() acepta dígitos de otros alfabetos (int(«٣») = 3), así que «isdigit» tampoco basta para validar un número.", note_kind="gold", foot="Doce cadenas reconocidas y dos no reconocidas; idéntico en ambos sistemas (CPython 3.12.9 y 3.12.3).")


def se219_secreto() -> Fig:
    rows = [["Secreto pasado como --token=VALOR", "Visible para otro proceso del mismo usuario (Get-CimInstance)", "Visible en /proc/pid/cmdline"],
            ["Secreto pasado por variable de entorno", "No comprobado por esa vía (WMI no lista el entorno)", "Visible en /proc/pid/environ"],
            ["Secreto leído de un archivo o de stdin", "No aparece en la línea de comandos", "No aparece en cmdline ni en el historial del shell"]]
    return tab("Dónde puede verse un secreto sintético según cómo se entrega a la herramienta",
               "Tabla: un valor falso pasado como argumento de línea de comandos fue visible para otro proceso del mismo usuario tanto en Windows como en Ubuntu; la variable de entorno fue visible en Ubuntu mediante /proc y no se comprobó en Windows; leerlo de un archivo o de la entrada estándar no lo expone en la línea de comandos.",
               ["Cómo se entrega el secreto", "Windows", "Ubuntu (WSL2)"], rows, [300, 380, 350], row_h=66,
               note="El valor usado fue FAKE-TOKEN-0001, sintético. Cualquier proceso del mismo usuario lo leyó mientras la herramienta corría; el historial del shell y los registros de procesos lo conservan además. Pasar secretos por flag es una decisión de diseño, no un detalle de comodidad.", note_kind="coral", foot="Medición en un equipo, mismo usuario; no incluye usuarios distintos, contenedores ni auditoría del sistema.")


# ---------------------------------------------------------------- SE-220
def se220_codigos() -> Fig:
    rows = [["sys.exit(256)", "256", "0"], ["sys.exit(257)", "257", "1"], ["sys.exit(1000)", "1000", "232"], ["sys.exit(-1)", "4294967295", "255"],
            ["os.abort()", "3221226505", "-6 (señal SIGABRT)"], ["kill() desde el padre", "1", "-9 (señal SIGKILL)"],
            ["Excepción sin capturar", "1", "1"], ["sys.exit(«mensaje»)", "1", "1"]]
    return tab("El mismo código de salida observado desde el padre en Windows y en Ubuntu",
               "Tabla: sys.exit(256) devuelve 256 en Windows y 0 en Ubuntu; sys.exit(1000) devuelve 1000 y 232; sys.exit(-1) devuelve 4294967295 y 255; un proceso abortado devuelve 3221226505 en Windows y menos 6 en Ubuntu; una excepción sin capturar devuelve 1 en ambos.",
               ["Cómo termina el hijo", "Windows (CPython 3.12.9)", "Ubuntu (3.12.3)"], rows, [320, 330, 340], row_h=44,
               note="Linux conserva solo ocho bits del código: 256 se lee como 0, es decir, éxito. Windows conserva treinta y dos. Un código fuera de 0–255 no es portable; en POSIX una señal se informa como un número negativo y en Windows como un código de excepción.", note_kind="coral", foot=SINT)


def se220_tuberias() -> Fig:
    rows = [["false | cat; echo $?", "0", "El estado de la tubería es el del último comando; el fallo se pierde"],
            ["set -o pipefail; false | cat; echo $?", "1", "pipefail propaga el primer fallo"],
            ["false | true | cat; echo ${PIPESTATUS[@]}", "1 0 0", "PIPESTATUS conserva el estado de cada etapa"],
            ["false && echo ok; echo $?", "1", "El && no ejecuta la segunda orden; $? queda en 1"],
            ["false; echo continua; true; echo $?", "continua · 0", "Sin set -e el script sigue y el último estado oculta el fallo"],
            ["set -e; false; echo continua", "(nada) · 1", "Con set -e el script se detiene en el primer fallo"]]
    return tab("Estado de salida de tuberías y guiones de shell (bash, mismos resultados en Windows y Ubuntu)",
               "Tabla de seis guiones de bash: false seguido de cat devuelve 0 aunque la primera etapa falló; con pipefail devuelve 1; PIPESTATUS muestra 1 0 0; sin set -e el guion continúa y termina con 0; con set -e se detiene con 1.",
               ["Guion", "Resultado", "Lectura"], rows, [400, 130, 500], row_h=52,
               note="Una tubería sin pipefail devuelve éxito aunque falle la primera etapa. Un trabajo programado que termina con 0 después de un fallo intermedio es la forma más común de fallo silencioso en la automatización.", note_kind="gold", foot="Git Bash en Windows y bash 5.2.21 en Ubuntu/WSL2; los resultados fueron iguales.")


def se220_reintentos() -> Fig:
    items = [
        ("Nunca reintentar: intentos", 10000, "grey", "10 000"),
        ("Reintentar solo el código 75: intentos", 11675, "teal", "11 675"),
        ("Reintentar todo: intentos", 29744, "coral", "29 744"),
        ("Reintentar todo: reintentos inútiles", 24092, "coral", "24 092"),
    ]
    return bars("10 000 trabajos con cinco tipos de fallo: coste de tres políticas de reintento",
                "Barras: con 10 000 trabajos y fallos transitorios recuperables 70 por ciento de las veces, reintentar solo lo transitorio recupera 3 950 trabajos con 11 675 intentos; reintentar todo recupera los mismos 3 950 con 29 744 intentos, de ellos 24 092 inútiles.",
                items, 0.0155, "Reintentar solo el código transitorio recuperó 3 950 trabajos, 1 165 más que no reintentar (2 785), con 1 675 intentos extra; reintentar todo recuperó los mismos 3 950 y gastó 18 069 intentos más. Un código de salida que distingue «temporal» de «permanente» es lo que hace posible la política barata.",
                label_w=420, width=1020, note_kind="gold", foot="Simulación con semilla 220; porcentajes y la probabilidad de recuperación de 70 % son supuestos del autor, no mediciones.")


# ---------------------------------------------------------------- SE-221
def se221_color() -> Fig:
    rows = [["Color solo en terminal (salida a tubería)", "8 000 / 7 800", "0", "200"],
            ["Color siempre (ingenuo)", "9 800 / 9 600", "200", "0 (200 tras quitar los escapes)"],
            ["Sobrecoste del color", "+22,5 % / +23,1 %", "—", "—"]]
    return tab("Un informe de 200 líneas con una palabra en rojo, escrito a una tubería",
               "Tabla: con detección de terminal el informe ocupa 8 000 bytes en Windows y 7 800 en Ubuntu y no tiene escapes; con color siempre ocupa 9 800 y 9 600, tiene 200 líneas con escapes y la búsqueda de la frase ERROR nota encuentra 0 coincidencias, que pasan a 200 al quitar los escapes.",
               ["Política", "Bytes (Windows / Ubuntu)", "Líneas con escapes", "Coincidencias de «ERROR nota»"], rows, [370, 230, 190, 240], row_h=52,
               note="El color añadió una quinta parte de bytes y, sobre todo, partió la frase buscada con secuencias invisibles: la búsqueda del equipo dejó de funcionar. La diferencia de 200 bytes entre sistemas son los 200 saltos de línea CRLF de Windows.", note_kind="coral", foot="La salida se capturó con una tubería, de modo que isatty() fue falso; no se probó un terminal interactivo.")


def se221_truncado() -> Fig:
    items = [
        ("Truncado al final, ancho 12", 3, "coral", "3 de 500"),
        ("Truncado al final, ancho 16", 458, "gold", "458"),
        ("Truncado al final, ancho 20", 500, "teal", "500"),
        ("Truncado al final, ancho 24", 500, "teal", "500"),
        ("Truncado por el medio, ancho 12", 500, "teal", "500"),
        ("Truncado por el medio, ancho 16", 500, "teal", "500"),
    ]
    return bars("Identificadores distintos de 500 tras truncarlos a un ancho dado",
                "Barras: de 500 identificadores sintéticos que comparten un prefijo, truncar por el final a 12 caracteres deja solo 3 distintos, a 16 deja 458 y a 20 o 24 los 500; truncar por el medio conserva los 500 con cualquiera de los cuatro anchos.",
                items, 0.85, "Cortar por el final conserva el prefijo común y destruye lo distintivo: con 12 columnas 497 filas se volvieron indistinguibles. Mostrar principio y final (o lo distintivo primero) conserva la diferencia con el mismo ancho. El truncado es una vista; la herramienta debe poder dar el valor completo.",
                label_w=370, width=1000, note_kind="coral", foot="Identificadores de 23 caracteres con semilla 221; si lo distintivo estuviera al principio, cortar por el final bastaría.")


def se221_ancho() -> Fig:
    rows = [["Ana", "3", "3", "3"], ["José", "4", "5", "4"], ["Björn", "5", "6", "5"], ["李雨", "2", "2", "4"], ["田中太郎", "4", "4", "8"],
            ["👩‍💻 Eva", "7", "7", "8 (estimado)"]]
    return tab("Longitud y ancho en pantalla de seis nombres",
               "Tabla: José mide 4 caracteres en NFC y 5 en NFD pero ocupa 4 celdas; 李雨 mide 2 caracteres y ocupa 4 celdas; 田中太郎 mide 4 y ocupa 8; en 1 000 filas con diez nombres, rellenar con len desalineó 607 y rellenar por ancho estimado desalineó 0.",
               ["Nombre", "len en NFC", "len en NFD", "Ancho en celdas"], rows, [300, 220, 220, 300], row_h=44,
               note="En 607 de 1 000 filas len() no es el ancho en pantalla; rellenar con ljust desalineó esas 607 filas y rellenar por ancho estimado ninguna. Seis de los diez nombres tienen una forma NFD distinta de la NFC: se ven igual y son cadenas distintas hasta que se normalizan.", note_kind="gold", foot="Semilla 1; el ancho se estimó con East Asian Width y es una aproximación: el emoji compuesto se dibuja distinto según el terminal.")


# ---------------------------------------------------------------- SE-222
def se222_senales() -> Fig:
    rows = [["terminate() con un manejador que limpia en 0,2 s", "Código 1 · sin limpieza (terminación inmediata)", "Código 0 · marca de limpieza escrita"],
            ["terminate() con un manejador que ignora la señal", "Código 1 · el proceso desaparece", "Código −9 tras 1,5 s: hubo que forzar"],
            ["CTRL_BREAK_EVENT (grupo de procesos nuevo)", "Código 0 · marca de limpieza escrita", "No existe"]]
    return tab("Pedir a un servicio que termine: lo que ocurre en Windows y en Ubuntu",
               "Tabla: en Windows, terminate equivale a una terminación forzada que no ejecuta el manejador y devuelve código 1, y solo CTRL_BREAK_EVENT dispara una limpieza ordenada; en Ubuntu terminate envía SIGTERM, que ejecuta el manejador y deja la marca de limpieza, y un manejador que ignora la señal obliga a forzar con SIGKILL.",
               ["Qué se hace", "Windows", "Ubuntu (WSL2)"], rows, [350, 340, 340], row_h=66,
               note="El mismo método de Python significa dos cosas: pedir y obligar. Un servicio que debe cerrar conexiones y vaciar datos necesita, en Windows, un canal de aviso distinto (CTRL_BREAK, una orden de control o una petición por un canal propio), y en cualquier sistema un plazo tras el cual se fuerza.", note_kind="coral", foot="Un hijo de Python con un manejador de señales; no se probó un servicio de Windows real ni systemd.")


def se222_preparado() -> Fig:
    items = [
        ("Preparado = proceso lanzado", 0.8, "coral", "0,8 s (≈20 fallos a 25 peticiones/s)"),
        ("Preparado = puerto abierto", 0.3, "gold", "0,3 s (≈6 fallos)"),
        ("Preparado = responde 200", 0.0, "teal", "0,0 s (0 fallos)"),
    ]
    return bars("Ventana en la que llegan peticiones que fallan según qué significa preparado",
                "Barras: con un servicio que abre su puerto a los 0,5 segundos y termina de calentar a los 0,8, declararlo preparado al lanzar el proceso deja 0,8 segundos de peticiones fallidas, hacerlo al abrirse el puerto deja 0,3 y esperar a que responda con éxito deja 0.",
                items, 280, "«Vivo» (el proceso existe) no es «preparado» (puede atender). Entre el arranque y la primera respuesta correcta hay una ventana en la que el tráfico recibe rechazos o 503; a 25 peticiones por segundo son unas 20, 6 o 0 según la definición. Una sonda de preparación debe probar lo mismo que hará el cliente.",
                label_w=330, width=1050, note_kind="gold", foot="Servidor HTTP local en 127.0.0.1 con retardos configurados; Ubuntu midió ≈7 fallos para «puerto abierto».")


def se222_reinicios() -> Fig:
    items = [
        ("Sin espera (0,2 s por arranque)", 3000, "coral", "3 000"),
        ("Espera fija de 1 s", 501, "gold", "501"),
        ("Espera exponencial hasta 60 s", 15, "teal", "15"),
        ("Exponencial con jitter", 24, "teal", "24"),
    ]
    return bars("Arranques de un servicio que siempre falla al iniciar, durante 600 s",
                "Barras: un servicio que falla de inmediato se arranca 3 000 veces en 600 segundos si se reinicia sin espera, 501 con una espera fija de un segundo, 15 con espera exponencial hasta 60 segundos y 24 con espera exponencial con jitter.",
                items, 0.15, "Un reinicio inmediato convierte un fallo de arranque en una carga de miles de intentos y de líneas de registro por diez minutos. La espera creciente reduce los arranques a decenas; el jitter reparte los reintentos de varias instancias para que no coincidan.",
                label_w=370, width=950, note_kind="coral", foot="Simulación determinista con semilla 3 para el jitter; los tiempos de arranque (0,2 s) y de espera son supuestos del autor.")


FIGURES = {
    "se-217-abreviaturas-que-dejan-de-valer.svg": se217_abreviaturas,
    "se-217-contrato-observable-de-una-cli.svg": se217_contrato,
    "se-217-sugerir-sin-adivinar.svg": se217_sugerencias,
    "se-218-buffer-de-una-tuberia.svg": se218_buffer,
    "se-218-cierre-de-tuberia-por-sistema.svg": se218_tuberia_rota,
    "se-218-cargar-o-iterar.svg": se218_memoria,
    "se-219-precedencia-y-combinaciones.svg": se219_precedencia,
    "se-219-booleanos-del-entorno.svg": se219_booleanos,
    "se-219-donde-se-ve-un-secreto.svg": se219_secreto,
    "se-220-codigos-por-sistema.svg": se220_codigos,
    "se-220-tuberias-y-estado.svg": se220_tuberias,
    "se-220-coste-de-los-reintentos.svg": se220_reintentos,
    "se-221-color-en-una-tuberia.svg": se221_color,
    "se-221-truncar-sin-perder-la-diferencia.svg": se221_truncado,
    "se-221-ancho-de-los-nombres.svg": se221_ancho,
    "se-222-senales-por-sistema.svg": se222_senales,
    "se-222-preparado-no-es-vivo.svg": se222_preparado,
    "se-222-reinicios-en-bucle.svg": se222_reinicios,
}
