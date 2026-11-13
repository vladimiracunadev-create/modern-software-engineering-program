"""Figures for SE-025 to SE-030 (values measured on Windows 11 and Ubuntu 24.04 under WSL2)."""
from __future__ import annotations

from pathlib import PurePosixPath, PureWindowsPath

from figure_kit import Fig


# ---------------------------------------------------------------- SE-025
def se025_capas() -> Fig:
    f = Fig(960, 470, "Una pregunta diagnóstica por frontera",
            "Cinco capas de la aplicación al hardware. Para cada frontera se indica la pregunta que permite ubicar un fallo y la evidencia que la discrimina.")
    heads = ["Capa", "Pregunta", "Evidencia que la discrimina"]
    rows = [
        ["Aplicación", "¿Construyó bien la petición?", "Argumentos, excepción y traza del propio programa"],
        ["Biblioteca o runtime", "¿Existe la función en esta versión?", "Versión del runtime; ImportError o AttributeError"],
        ["API del sistema", "¿Existe en esta plataforma?", "Código de error del sistema (por ejemplo, WinError 1314)"],
        ["Kernel", "¿Lo autorizó y pudo cumplirlo?", "Permission denied, política, registro del sistema"],
        ["Controlador y recurso", "¿El dispositivo pudo atenderlo?", "Errores de E/S, estado del dispositivo, registros"],
    ]
    f.table(heads, rows, 10, 12, [190, 300, 450], row_h=60, size=13)
    f.text(480, 452, "Versión, arquitectura y política pueden alterar varias fronteras: se registra el contexto antes de culpar una capa.", 13, "middle")
    return f


def se025_misma_etiqueta() -> Fig:
    f = Fig(960, 520, "Dos sistemas, mismo programa: lo que informa cada uno",
            "Tabla con valores reales observados con el mismo script de Python en Windows 11 y en Ubuntu 24.04 bajo WSL2: sistema, versión, arquitectura, separadores, "
            "fin de línea, nombre del sistema de módulos y proceso de inicio.")
    heads = ["Dato", "Windows 11 (CPython 3.12.9)", "Linux en WSL2 (CPython 3.12.3)"]
    rows = [
        ["platform.system()", "Windows", "Linux"],
        ["Versión informada", "release 11; 10.0.26300", "kernel 6.18.58.1-microsoft-standard-WSL2"],
        ["platform.machine()", "AMD64", "x86_64"],
        ["Separador de rutas / de PATH", "«\\» y «;»", "«/» y «:»"],
        ["Fin de línea (os.linesep)", "\\r\\n", "\\n"],
        ["os.name", "nt", "posix"],
        ["Proceso 1 / virtualización", "No aplicable", "systemd; systemd-detect-virt = wsl"],
    ]
    f.table(heads, rows, 10, 12, [260, 340, 340], row_h=50, size=13)
    f.box(10, 458, 940, 48, "Mismo hardware, distinta plataforma efectiva: «AMD64» y «x86_64» nombran la misma ISA, y «Linux» aquí corre dentro de una máquina virtual ligera.", "gold", 13)
    return f


def se025_sintomas() -> Fig:
    f = Fig(960, 490, "Tres mensajes de error reales y la capa que señalan",
            "Tabla de tres errores observados: un script con finales de línea de Windows en Linux, un script sin bit de ejecución y la creación de un enlace simbólico "
            "sin privilegio en Windows. Cada uno se asigna a una capa y a una prueba que lo discrimina.")
    heads = ["Mensaje observado", "Capa", "Prueba que lo discrimina"]
    rows = [
        ["/usr/bin/env: ‘bash\\r’: No such file or directory", "Formato del script e intérprete (shebang)", "`file script.sh` informa «with CRLF line terminators»; al convertir los finales, funciona"],
        ["Permission denied al ejecutar ./script.sh", "Política del sistema de archivos (bit de ejecución)", "`bash script.sh` funciona: el contenido es válido y falta el permiso"],
        ["OSError: [WinError 1314] Un privilegio requerido no es retenido por el cliente", "API y política de Windows (privilegio de enlaces simbólicos)", "El mismo código funciona en ext4 de WSL; el fallo depende del privilegio, no del código"],
    ]
    f.table(heads, rows, 10, 12, [330, 260, 350], row_h=96, size=13)
    f.box(10, 372, 940, 100, "Cada mensaje nombra un síntoma, no un sistema operativo entero. «Es un problema de Windows» o «en Linux sí funciona» no explica nada: "
          "la prueba de la tercera columna sí separa las hipótesis.", "grey", 13)
    return f


# ---------------------------------------------------------------- SE-026
def se026_comparacion() -> Fig:
    f = Fig(960, 500, "Tres sistemas de archivos, tres comportamientos medidos",
            "Tabla con los resultados de una misma prueba en NTFS bajo Windows, ext4 bajo WSL2 y el montaje 9p de la unidad de Windows visto desde WSL: sensibilidad a mayúsculas, "
            "enlaces simbólicos y físicos, efecto de chmod 600 y coexistencia de nombres equivalentes en Unicode.")
    heads = ["Propiedad", "NTFS (Windows)", "ext4 (WSL2)", "9p sobre C: (WSL2)"]
    rows = [
        ["Distingue Aa.txt de aA.txt", "No (conserva el caso)", "Sí", "No"],
        ["Enlace simbólico sin privilegios", "No: WinError 1314", "Sí", "Sí (con el privilegio de la interoperabilidad)"],
        ["Enlace físico (nlink)", "Sí; nlink = 2", "Sí; nlink = 2", "Sí; nlink = 2"],
        ["Modo tras chmod 600", "0o666 (solo solo-lectura)", "0o600", "0o777 (emulado)"],
        ["Nombre «a:b.txt»", "Error (el «:» tiene significado)", "Permitido", "Permitido (pero no sobrevive en NTFS)"],
        ["é compuesta y descompuesta", "Dos entradas distintas", "Dos entradas distintas", "Dos entradas distintas"],
    ]
    f.table(heads, rows, 10, 12, [250, 230, 210, 250], row_h=52, size=12)
    f.box(10, 420, 940, 62, "Una operación correcta en un sistema de archivos puede fallar o cambiar de significado en otro. El mismo código y el mismo nombre de archivo no son suficientes: "
          "se declara qué sistema de archivos se usa.", "gold", 13)
    return f


def se026_costo() -> Fig:
    f = Fig(960, 440, "El costo de cruzar la frontera de sistema de archivos",
            "Barras con una medición real: crear 2000 archivos pequeños tarda 0,33 s en ext4, 1,32 s en NTFS desde Windows y 12,79 s en el montaje 9p de WSL; "
            "hacer stat de 2000 archivos tarda 0,007 s, 0,116 s y 4,886 s respectivamente.")
    f.text(20, 28, "Crear 2000 archivos de un byte (segundos)", 14, "start", 700)
    f.hbars([("ext4 (WSL2)", 0.332, "teal", "0,33 s"), ("NTFS (Windows)", 1.316, "gold", "1,32 s"), ("9p sobre C: (WSL2)", 12.792, "coral", "12,79 s")], 20, 44, 40, label_w=210, step=42)
    f.text(20, 214, "Hacer stat de 2000 archivos (segundos)", 14, "start", 700)
    f.hbars([("ext4 (WSL2)", 0.007, "teal", "0,007 s"), ("NTFS (Windows)", 0.116, "gold", "0,12 s"), ("9p sobre C: (WSL2)", 4.886, "coral", "4,89 s")], 20, 230, 80, label_w=210, step=42)
    f.box(20, 372, 920, 56, "Mantener un proyecto con muchos archivos pequeños en /mnt/c es unas 38 veces más lento al crear y unas 700 veces más lento al consultar metadatos que en ext4 de WSL.", "grey", 13)
    f.text(480, 436, "Una ejecución por celda, Python 3.12 en cada entorno. Los valores dependen del equipo y de las políticas de seguridad; el patrón es el resultado.", 12, "middle", 400, "#5c1f14")
    return f


def se026_rutas() -> Fig:
    w = PureWindowsPath(r"C:\Users\ana\datos\informe.txt")
    u = PureWindowsPath(r"\\servidor\compartido\datos\informe.txt")
    p = PurePosixPath("/mnt/c/Users/ana/datos/informe.txt")
    q = PurePosixPath(r"C:\Users\ana\datos\informe.txt")
    f = Fig(960, 500, "La misma ruta como texto: cómo la leen pathlib de Windows y de POSIX",
            "Cuatro rutas y su descomposición real con pathlib: una ruta de unidad de Windows, una ruta UNC, una ruta POSIX y una ruta de Windows leída como POSIX, "
            "que se interpreta como un solo nombre de archivo.")
    heads = ["Ruta", "Leída con", "Unidad / ancla", "Partes"]
    rows = [
        [r"C:\Users\ana\datos\informe.txt", "PureWindowsPath", f"drive={w.drive!r} root={w.root!r}", f"{len(w.parts)} partes; nombre {w.name!r}"],
        [r"\\servidor\compartido\datos\informe.txt", "PureWindowsPath", f"drive={u.drive!r}", f"{len(u.parts)} partes; ancla UNC"],
        ["/mnt/c/Users/ana/datos/informe.txt", "PurePosixPath", f"root={p.root!r}; sin unidad", f"{len(p.parts)} partes; nombre {p.name!r}"],
        [r"C:\Users\ana\datos\informe.txt", "PurePosixPath", f"root={q.root!r}; sin ancla", f"{len(q.parts)} parte: todo es un nombre"],
    ]
    f.table(heads, rows, 10, 12, [330, 150, 270, 190], row_h=70, size=12)
    f.box(10, 366, 940, 60, "El separador, la raíz y la unidad pertenecen a la interpretación, no al texto. Construir rutas con pathlib o os.path y no con concatenación evita "
          "que una ruta de un sistema se lea con las reglas de otro.", "teal", 13)
    f.text(480, 460, "Valores obtenidos con pathlib de Python 3.12 (rutas puras: no tocan el disco).", 12, "middle", 400, "#5c1f14")
    return f


# ---------------------------------------------------------------- SE-027
def se027_modos() -> Fig:
    f = Fig(960, 470, "Qué hace chmod en Linux y en Windows: resultados reales",
            "Tabla de cuatro modos aplicados a un archivo propio, con lo observado en Linux (ext4, usuario sin privilegios) y en Windows: el modo que se ve, si se puede leer y si se puede escribir.")
    heads = ["Modo pedido", "Linux: ve / lee / escribe", "Windows: ve / lee / escribe"]
    rows = [
        ["0o644", "0o644 · lee · escribe", "0o666 · lee · escribe"],
        ["0o600", "0o600 · lee · escribe", "0o666 · lee · escribe"],
        ["0o000", "0o000 · PermissionError · PermissionError", "0o444 · lee · PermissionError"],
        ["0o444", "0o444 · lee · PermissionError", "0o444 · lee · PermissionError"],
    ]
    f.table(heads, rows, 10, 12, [200, 380, 360], row_h=54, size=13)
    f.box(10, 310, 940, 74, "En Windows, chmod solo activa o quita el atributo de solo lectura: 0o000 no impide leer. Los permisos reales de Windows viven en listas de control de acceso (ACL) "
          "y tokens, no en bits de modo.", "coral", 13)
    f.box(10, 394, 940, 56, "Linux comprobó como usuario sin privilegios (uid 1000); como administrador el resultado de 0o000 sería otro.", "grey", 13)
    return f


def se027_directorio() -> Fig:
    f = Fig(940, 400, "En un directorio, r lista y x atraviesa",
            "Un directorio con modo 600 (solo lectura y escritura del propietario, sin permiso de ejecución): listar sus nombres funciona, pero consultar un archivo hijo falla con PermissionError.")
    f.box(20, 40, 280, 100, "directorio con modo 600\n(rw-, sin x)", "gold", 14, bold=True)
    f.box(380, 40, 260, 56, "os.listdir(dir) → funciona", "teal", 13, bold=True)
    f.box(380, 104, 260, 56, "os.stat(dir/a) → PermissionError", "coral", 13, bold=True)
    f.arrow([(300, 80), (380, 68)])
    f.arrow([(300, 100), (380, 132)])
    f.box(680, 40, 240, 120, "r permite leer los nombres. x permite atravesar el directorio para llegar a lo que contiene.", "grey", 13)
    f.box(20, 190, 900, 90, "Para atravesar /a/b/c se necesita x en cada directorio del camino y los permisos del archivo final. Un archivo con permisos correctos puede ser inalcanzable "
          "si un directorio superior no concede x.", "plain", 13)
    f.box(20, 292, 900, 70, "En Windows el modelo es distinto: la lista de control de acceso del objeto y el token del proceso se evalúan juntos, y existe un privilegio de «omitir comprobación de recorrido».", "grey", 13)
    return f


def se027_denegacion() -> Fig:
    f = Fig(960, 460, "Una denegación es información: dos intentos observados",
            "Dos intentos reales como usuario sin privilegios: leer /etc/shadow, que tiene modo 640 y propietario root, produce Permission denied; sudo sin contraseña interactiva informa que se requiere una contraseña. "
            "La evidencia indica la capa y evita elevar sin necesidad.")
    heads = ["Intento", "Resultado observado", "Lectura correcta"]
    rows = [
        ["cat /etc/shadow", "cat: /etc/shadow: Permission denied (modo 640, propietario root)", "El kernel aplicó el control de acceso: el archivo existe y la identidad no tiene el permiso"],
        ["sudo -n true", "sudo: a password is required", "La elevación requiere una autenticación que este contexto no ofrece; no es una falla del comando"],
        ["id (uid 1000)", "El usuario pertenece a varios grupos y no a root", "Identidad no equivale a autoridad: los grupos y la política deciden qué puede hacerse"],
    ]
    f.table(heads, rows, 10, 12, [210, 340, 390], row_h=94, size=13)
    f.box(10, 368, 940, 70, "Elevar privilegios para «ver si funciona» es una intervención con riesgo y no una prueba. La respuesta correcta empieza por identificar sujeto, acción, objeto y política.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-028
def se028_codigos() -> Fig:
    f = Fig(960, 470, "Cómo termina un proceso: códigos de salida observados en Windows y Linux",
            "Tabla con el código de retorno observado desde Python: salir con 3 da 3 en ambos; una excepción sin tratar da 1 en ambos; terminar un proceso con terminate() da 1 en Windows y -15 en Linux; "
            "SIGKILL da -9 en Linux; con un manejador de SIGTERM el proceso limpia y sale con 0.")
    heads = ["Cómo termina", "Windows", "Linux (WSL2)"]
    rows = [
        ["sys.exit(3)", "3", "3"],
        ["Excepción sin tratar", "1", "1"],
        ["terminate() sin manejador", "1 (TerminateProcess)", "-15 (señal SIGTERM)"],
        ["kill / SIGKILL", "No aplicable como señal", "-9 (no se puede interceptar)"],
        ["SIGTERM con manejador que limpia", "No aplicable", "0 y escribe «limpiando»"],
        ["subprocess.run(timeout=1) sobre un proceso de 10 s", "TimeoutExpired", "TimeoutExpired"],
    ]
    f.table(heads, rows, 10, 12, [420, 270, 250], row_h=50, size=13)
    f.box(10, 408, 940, 50, "En POSIX un código negativo en Python significa «terminado por la señal N»; en Windows no existe ese canal y todo es un entero.", "gold", 13)
    return f


def se028_apagado() -> Fig:
    f = Fig(940, 460, "Apagado ordenado frente a terminación forzada",
            "Dos caminos: SIGTERM llega a un manejador que limpia y sale con código 0, mientras SIGKILL termina el proceso sin dejarle ejecutar código y deja su código en -9.")
    f.box(20, 20, 200, 50, "Proceso padre", "navy", 14, bold=True)
    f.box(20, 150, 200, 50, "SIGTERM (terminate)", "teal", 13, bold=True)
    f.box(20, 300, 200, 50, "SIGKILL", "coral", 13, bold=True)
    f.arrow([(120, 70), (120, 150)])
    f.arrow([(60, 70), (60, 300)], dashed=True)
    f.box(300, 150, 300, 50, "Manejador del proceso hijo: limpia recursos", "teal", 13)
    f.arrow([(220, 175), (300, 175)])
    f.box(660, 150, 260, 50, "Sale con código 0 y escribe «limpiando»", "teal", 13, bold=True)
    f.arrow([(600, 175), (660, 175)])
    f.box(300, 300, 300, 50, "El núcleo termina el proceso: ningún código del hijo se ejecuta", "coral", 13)
    f.arrow([(220, 325), (300, 325)])
    f.box(660, 300, 260, 50, "Código -9; recursos sin liberar", "coral", 13, bold=True)
    f.arrow([(600, 325), (660, 325)])
    f.box(20, 380, 900, 60, "Se pide cerrar con SIGTERM, se espera un plazo y solo entonces se fuerza con SIGKILL. Un proceso que ignora SIGTERM depende del plazo y de la política del supervisor.", "grey", 13)
    return f


def se028_arranque() -> Fig:
    f = Fig(900, 340, "Crear un proceso cuesta más en Windows que en Linux",
            "Barras con una medición real: arrancar un intérprete de Python vacío tarda en promedio 140,2 milisegundos en Windows y 25,8 milisegundos en Linux (WSL2).")
    f.text(20, 28, "Arrancar `python -c pass` (milisegundos, promedio de 10)", 14, "start", 700)
    f.hbars([("Linux (WSL2)", 25.8, "teal", "25,8 ms"), ("Windows", 140.2, "gold", "140,2 ms")], 20, 56, 4, label_w=170, step=50)
    f.box(20, 170, 860, 90, "Un diseño que lanza un proceso por tarea paga ese costo cada vez. Por eso se reutilizan procesos (agrupaciones), se agrupan tareas o se usan hilos para esperas. "
          "El valor incluye el arranque del intérprete, no solo la llamada al sistema.", "grey", 13)
    f.text(450, 300, "Una máquina, un día; el cociente (5,4 veces) es la lectura, no los milisegundos.", 12, "middle", 400, "#5c1f14")
    return f


# ---------------------------------------------------------------- SE-029
def se029_expansion() -> Fig:
    f = Fig(960, 470, "Quién interpreta los argumentos antes de que el programa los reciba",
            "Tabla con resultados reales: en Bash, un comodín sin comillas se expande a dos archivos y entre comillas llega literal; una variable con espacio sin comillas se divide en dos argumentos "
            "y entre comillas es uno; en PowerShell un comodín sin coincidencias llega literal al programa nativo.")
    heads = ["Orden escrita", "Shell", "Argumentos que recibe el programa", "Número"]
    rows = [
        ["prog /tmp/p02*.txt", "Bash", "['/tmp/p02a.txt', '/tmp/p02b.txt']", "2"],
        ["prog \"/tmp/p02*.txt\"", "Bash", "['/tmp/p02*.txt']", "1"],
        ["x=\"un archivo.txt\"; prog $x", "Bash", "'un' y 'archivo.txt'", "2"],
        ["x=\"un archivo.txt\"; prog \"$x\"", "Bash", "'un archivo.txt'", "1"],
        ["prog *.nada", "PowerShell 5.1", "['*.nada']: no expande para programas nativos", "1"],
        ["prog $x (con espacio)", "PowerShell 5.1", "Un solo argumento", "1"],
    ]
    f.table(heads, rows, 10, 12, [300, 140, 400, 100], row_h=50, size=12)
    f.box(10, 408, 940, 50, "El programa nunca ve las comillas ni el comodín: ve la lista final. Un shell distinto produce otra lista con el mismo texto.", "gold", 13)
    return f


def se029_pipefail() -> Fig:
    f = Fig(940, 440, "El código de salida de un pipeline",
            "Con el pipeline «false | true», Bash informa código 0 por defecto, y con pipefail activado informa 1; dentro de un subshell con set -e un cd fallido detiene el script con código 1, "
            "mientras que sin set -e el script continúa en el directorio anterior.")
    heads = ["Situación", "Resultado observado", "Lectura"]
    rows = [
        ["false | true", "código 0", "Solo cuenta el último comando: el fallo inicial se oculta"],
        ["set -o pipefail; false | true", "código 1", "Cualquier comando que falle hace fallar el pipeline"],
        ["cd /noexiste (sin set -e)", "el script sigue en el directorio anterior", "Un fallo ignorado deja el script operando en otro lugar"],
        ["set -e; cd /noexiste", "el subshell termina con código 1", "El fallo detiene la ejecución"],
        ["ls /noexiste", "código 2", "Los códigos son una interfaz: cada herramienta documenta los suyos"],
    ]
    f.table(heads, rows, 10, 12, [270, 290, 380], row_h=58, size=13)
    f.box(10, 380, 920, 46, "Un script robusto declara cómo trata los fallos y comprueba los códigos que le importan.", "gold", 13)
    return f


def se029_canales() -> Fig:
    f = Fig(940, 400, "Entrada, salida y error son canales distintos",
            "Un comando que escribe «salida» en stdout y «error» en stderr: con ambos redirigidos a archivos, el archivo de salida contiene 7 bytes y el de error 6 bytes; "
            "descartar stderr deja solo la salida en pantalla.")
    f.box(20, 150, 180, 60, "Comando", "navy", 14, bold=True)
    f.box(300, 70, 260, 60, "stdout (canal 1): resultados\n«salida» → 7 bytes", "teal", 13)
    f.box(300, 230, 260, 60, "stderr (canal 2): diagnóstico\n«error» → 6 bytes", "coral", 13)
    f.arrow([(200, 170), (300, 100)])
    f.arrow([(200, 190), (300, 260)])
    f.box(640, 70, 280, 60, "> salida.txt  (archivo de 7 bytes)", "plain", 13)
    f.box(640, 230, 280, 60, "2> error.txt  (archivo de 6 bytes)", "plain", 13)
    f.arrow([(560, 100), (640, 100)])
    f.arrow([(560, 260), (640, 260)])
    f.box(20, 320, 900, 60, "Los datos van por stdout y los mensajes por stderr: así un pipeline transmite resultados sin mezclarlos con diagnósticos. Que stderr tenga texto no implica un fallo fatal; el código de salida lo indica.", "grey", 13)
    return f


# ---------------------------------------------------------------- SE-030
def se030_objetos() -> Fig:
    f = Fig(960, 460, "PowerShell pasa objetos; Bash pasa texto",
            "Comparación con resultados reales: en PowerShell 5.1 Get-Process devuelve objetos System.Diagnostics.Process con propiedades como BasePriority y Container, y una lista de cadenas es un Object[] de String; "
            "en Bash los comandos intercambian bytes de texto que cada programa debe analizar.")
    heads = ["Aspecto", "PowerShell 5.1", "Bash"]
    rows = [
        ["Lo que viaja por el pipeline", "Objetos .NET: System.Diagnostics.Process", "Bytes de texto por stdout"],
        ["Acceso a un dato", "Propiedad: (Get-Process -Id $PID).BasePriority", "Analizar columnas con otro programa (awk, cut)"],
        ["Tipo de una lista", "Object[] de String", "Texto separado por saltos de línea"],
        ["Conversión de tipos", "1 + '2' = 3; '1' + 2 = 12 (manda el tipo del lado izquierdo)", "Todo es texto hasta que un programa lo interpreta"],
    ]
    f.table(heads, rows, 10, 12, [210, 400, 330], row_h=70, size=13)
    f.box(10, 372, 940, 80, "Ninguno es «mejor»: los objetos evitan analizar texto, y el texto es la interfaz común de las herramientas POSIX. Un adaptador debe traducir entre ambos modelos, no suponer que son iguales.", "gold", 13)
    return f


def se030_errores() -> Fig:
    f = Fig(960, 470, "Errores en dos shells: lo que se observó",
            "Tabla: en PowerShell 5.1 un error no terminante deja $? en falso y sigue; con -ErrorAction Stop se lanza ItemNotFoundException que se captura; un programa nativo deja su código en $LASTEXITCODE; "
            "con Set-StrictMode una variable no definida es un error. En Bash, $? guarda el código del último comando y set -e detiene el script.")
    heads = ["Situación", "PowerShell 5.1", "Bash"]
    rows = [
        ["Falla un comando", "Error no terminante: $? = False y el script continúa", "$? = código distinto de 0 y el script continúa"],
        ["Hacer que el fallo detenga", "-ErrorAction Stop → excepción ItemNotFoundException que try/catch captura", "set -e (con sus excepciones documentadas)"],
        ["Programa nativo con código 5", "$LASTEXITCODE = 5 y $? = False", "$? = 5"],
        ["Variable no definida", "Set-StrictMode: error «no se puede recuperar porque no se ha establecido»", "Expande a vacío salvo set -u"],
    ]
    f.table(heads, rows, 10, 12, [210, 400, 330], row_h=76, size=12)
    f.box(10, 398, 940, 56, "Cada shell tiene varios canales de error. Un contrato común define qué es un fallo (código de salida y mensaje estructurado) y cada adaptador lo traduce.", "gold", 13)
    return f


def se030_niveles() -> Fig:
    f = Fig(940, 440, "Niveles de portabilidad de un script",
            "Cuatro niveles de portabilidad, de lo más estrecho a lo más amplio: un script de Bash, un script POSIX sh, un script de PowerShell, y un núcleo en un lenguaje con adaptadores finos, "
            "con lo que cada nivel exige de la plataforma.")
    heads = ["Nivel", "Qué exige de la plataforma", "Qué no garantiza"]
    rows = [
        ["Bash", "Que Bash esté instalado y sea compatible", "Que exista en Windows sin una capa adicional"],
        ["POSIX sh", "Un intérprete que cumpla la especificación POSIX", "Que las herramientas externas (sed, date) se comporten igual"],
        ["PowerShell", "PowerShell 5.1 en Windows o PowerShell 7 multiplataforma", "Que 5.1 y 7 tengan los mismos módulos y comportamientos"],
        ["Núcleo común + adaptadores finos", "Un runtime (por ejemplo, Python 3.11+) y un adaptador por shell", "Que el adaptador exprese cada diferencia: se prueba en cada plataforma"],
    ]
    f.table(heads, rows, 10, 12, [230, 360, 350], row_h=70, size=13)
    f.box(10, 372, 920, 56, "Copiar el mismo script a tres sistemas solo desplaza el fallo; definir la intención común y probar cada adaptador lo hace visible.", "gold", 13)
    return f


FIGURES = {
    "se-025-pregunta-por-frontera.svg": se025_capas,
    "se-025-misma-etiqueta-otro-sistema.svg": se025_misma_etiqueta,
    "se-025-tres-mensajes-reales.svg": se025_sintomas,
    "se-026-tres-sistemas-de-archivos.svg": se026_comparacion,
    "se-026-costo-de-metadatos.svg": se026_costo,
    "se-026-rutas-como-texto.svg": se026_rutas,
    "se-027-chmod-en-dos-sistemas.svg": se027_modos,
    "se-027-directorio-r-y-x.svg": se027_directorio,
    "se-027-denegacion-es-informacion.svg": se027_denegacion,
    "se-028-codigos-de-salida.svg": se028_codigos,
    "se-028-apagado-ordenado.svg": se028_apagado,
    "se-028-costo-de-arrancar-procesos.svg": se028_arranque,
    "se-029-expansion-de-argumentos.svg": se029_expansion,
    "se-029-codigo-de-un-pipeline.svg": se029_pipefail,
    "se-029-tres-canales.svg": se029_canales,
    "se-030-objetos-frente-a-texto.svg": se030_objetos,
    "se-030-errores-en-dos-shells.svg": se030_errores,
    "se-030-niveles-de-portabilidad.svg": se030_niveles,
}
