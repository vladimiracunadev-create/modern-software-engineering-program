"""Figures for SE-025 to SE-030 (values measured on Windows 11 and Ubuntu 24.04 under WSL2)."""
from __future__ import annotations

from pathlib import PurePosixPath, PureWindowsPath

from figure_kit import Fig, text_width
from figure_flows import columnas, mapa


# ---------------------------------------------------------------- SE-025
def se025_capas() -> Fig:
    return mapa("Una pregunta diagnóstica por frontera",
                "Cinco capas apiladas de la aplicación al hardware. De cada capa sale una pregunta que permite ubicar un fallo y una evidencia que la discrimina.",
                [("Aplicación", "¿Construyó bien la petición?", "gold", "Argumentos, excepción y traza del propio programa"),
                 ("Biblioteca o runtime", "¿Existe la función en esta versión?", "gold", "Versión del runtime; ImportError o AttributeError"),
                 ("API del sistema", "¿Existe en esta plataforma?", "gold", "Código de error del sistema (por ejemplo, WinError 1314)"),
                 ("Kernel", "¿Lo autorizó y pudo cumplirlo?", "gold", "Permission denied, política, registro del sistema"),
                 ("Controlador y recurso", "¿El dispositivo pudo atenderlo?", "gold", "Errores de E/S, estado del dispositivo, registros")],
                note="Versión, arquitectura y política pueden alterar varias fronteras: se registra el contexto antes de culpar una capa.",
                width=960, left_w=210, mid_w=290, row_h=56, stack=True, heads=("Capa (de arriba abajo)", "Pregunta que ubica el fallo", "Evidencia que la discrimina"))


def se025_misma_etiqueta() -> Fig:
    return columnas("Dos sistemas, mismo programa: lo que informa cada uno",
                    "Cada dato que consulta el mismo script de Python sale por dos caminos, uno hacia Windows 11 y otro hacia Ubuntu 24.04 bajo WSL2; en los siete datos observados el valor difiere: sistema, versión, arquitectura, separadores, fin de línea, nombre del sistema de módulos y proceso de inicio.",
                    [("platform.system()", "Windows", "Linux"),
                     ("Versión informada", "release 11; 10.0.26300", "kernel 6.18.58.1-microsoft-standard-WSL2"),
                     ("platform.machine()", "AMD64", "x86_64"),
                     ("Separador de rutas / de PATH", "«\\» y «;»", "«/» y «:»"),
                     ("Fin de línea (os.linesep)", "\\r\\n", "\\n"),
                     ("os.name", "nt", "posix"),
                     ("Proceso 1 / virtualización", "No aplicable", "systemd; systemd-detect-virt = wsl")],
                    ["Windows 11 (CPython 3.12.9)", "Linux en WSL2 (CPython 3.12.3)"], ["gold", "teal"],
                    note="Mismo hardware, distinta plataforma efectiva: «AMD64» y «x86_64» nombran la misma ISA, y «Linux» aquí corre dentro de una máquina virtual ligera.",
                    label_w=250, row_h=52)


def se025_sintomas() -> Fig:
    return mapa("Tres mensajes de error reales y la capa que señalan",
                "Tres errores observados, cada uno con su capa y la prueba que lo discrimina: un script con finales de línea de Windows en Linux, un script sin bit de ejecución y la creación de un enlace simbólico sin privilegio en Windows.",
                [("/usr/bin/env: ‘bash\\r’: No such file or directory", "Formato del script e intérprete (shebang)", "gold",
                  "`file script.sh` informa «with CRLF line terminators»; al convertir los finales, funciona"),
                 ("Permission denied al ejecutar ./script.sh", "Política del sistema de archivos (bit de ejecución)", "gold",
                  "`bash script.sh` funciona: el contenido es válido y falta el permiso"),
                 ("OSError: [WinError 1314] Un privilegio requerido no es retenido por el cliente", "API y política de Windows (privilegio de enlaces simbólicos)", "gold",
                  "El mismo código funciona en ext4 de WSL; el fallo depende del privilegio, no del código")],
                note="Cada mensaje nombra un síntoma, no un sistema operativo entero. «Es un problema de Windows» o «en Linux sí funciona» no explica nada: la prueba de la tercera columna sí separa las hipótesis.",
                note_kind="grey", left_w=300, mid_w=250, row_h=96, heads=("Mensaje observado", "Capa que señala", "Prueba que lo discrimina"))


# ---------------------------------------------------------------- SE-026
def se026_comparacion() -> Fig:
    return columnas("Tres sistemas de archivos, tres comportamientos medidos",
                    "Seis propiedades de una misma prueba ejecutada en NTFS bajo Windows, ext4 bajo WSL2 y el montaje 9p de la unidad de Windows. Cuando los tres dan el mismo resultado las cajas se unen en una; en las demás propiedades se separan: sensibilidad a mayúsculas, enlaces simbólicos, efecto de chmod 600 y nombres con dos puntos.",
                    [("Distingue Aa.txt de aA.txt", "No (conserva el caso)", "Sí", "No"),
                     ("Enlace simbólico sin privilegios", "No: WinError 1314", "Sí", "Sí (con el privilegio de la interoperabilidad)"),
                     ("Enlace físico (nlink)", "Sí; nlink = 2", "Sí; nlink = 2", "Sí; nlink = 2"),
                     ("Modo tras chmod 600", "0o666 (solo solo-lectura)", "0o600", "0o777 (emulado)"),
                     ("Nombre «a:b.txt»", "Error (el «:» tiene significado)", "Permitido", "Permitido (pero no sobrevive en NTFS)"),
                     ("é compuesta y descompuesta", "Dos entradas distintas", "Dos entradas distintas", "Dos entradas distintas")],
                    ["NTFS (Windows)", "ext4 (WSL2)", "9p sobre C: (WSL2)"], ["gold", "teal", "plain"],
                    note="Una operación correcta en un sistema de archivos puede fallar o cambiar de significado en otro. El mismo código y el mismo nombre de archivo no son suficientes: se declara qué sistema de archivos se usa.",
                    label_w=250, row_h=58)


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
    cases = [
        (r"C:\Users\ana\datos\informe.txt", "PureWindowsPath", w.parts, f"drive={w.drive!r} root={w.root!r}; {len(w.parts)} partes; nombre {w.name!r}"),
        (r"\\servidor\compartido\datos\informe.txt", "PureWindowsPath", u.parts, f"drive={u.drive!r}; {len(u.parts)} partes; ancla UNC"),
        ("/mnt/c/Users/ana/datos/informe.txt", "PurePosixPath", p.parts, f"root={p.root!r}; sin unidad; {len(p.parts)} partes; nombre {p.name!r}"),
        (r"C:\Users\ana\datos\informe.txt", "PurePosixPath", q.parts, f"root={q.root!r}; sin ancla; {len(q.parts)} parte: todo es un nombre"),
    ]
    f = Fig(960, 500, "La misma ruta como texto: cómo la leen pathlib de Windows y de POSIX",
            "Cuatro rutas que pathlib descompone en partes, mostradas como fichas: una ruta de unidad de Windows, una ruta UNC, una ruta POSIX y una ruta de Windows leída como POSIX, que se interpreta como una sola ficha, un nombre de archivo único.")
    f.text(160, 24, "Ruta como texto", 13, "middle", 700, "#32505f")
    f.text(406, 24, "Leída con", 13, "middle", 700, "#32505f")
    f.text(510, 24, "Partes que obtiene pathlib", 13, "start", 700, "#32505f")
    y = 38
    for text, reader, parts, caption in cases:
        f.box(10, y, 300, 56, text, "plain", 12)
        f.box(336, y, 140, 56, reader, "navy", 12, True)
        f.arrow([(310, y + 28), (336, y + 28)])
        f.arrow([(476, y + 28), (502, y + 28)])
        x = 502.0
        for i, part in enumerate(parts):
            wd = text_width(part, 12, 700) + 20
            kind = "coral" if len(parts) == 1 else ("gold" if i == 0 and part.endswith(("\\", "/")) else "teal")
            f.box(x, y + 4, wd, 32, part, kind, 12, True)
            x += wd + 6
        f.text(502, y + 52, caption, 11, "start", 400, "#32505f")
        y += 84
    f.box(10, y + 4, 940, 60, "El separador, la raíz y la unidad pertenecen a la interpretación, no al texto. Construir rutas con pathlib o os.path y no con concatenación evita "
          "que una ruta de un sistema se lea con las reglas de otro.", "teal", 13)
    f.text(480, y + 86, "Valores obtenidos con pathlib de Python 3.12 (rutas puras: no tocan el disco).", 12, "middle", 400, "#5c1f14")
    return f


# ---------------------------------------------------------------- SE-027
def se027_modos() -> Fig:
    return columnas("Qué hace chmod en Linux y en Windows: resultados reales",
                    "Cuatro modos aplicados a un archivo propio. Cada modo pedido produce un resultado en Linux (ext4, usuario sin privilegios) y otro en Windows, expresado como el modo que se ve, si se puede leer y si se puede escribir; solo el modo 0o444 da lo mismo en ambos.",
                    [("Se pide 0o644", "0o644 · lee · escribe", "0o666 · lee · escribe"),
                     ("Se pide 0o600", "0o600 · lee · escribe", "0o666 · lee · escribe"),
                     ("Se pide 0o000", "0o000 · PermissionError · PermissionError", "0o444 · lee · PermissionError"),
                     ("Se pide 0o444", "0o444 · lee · PermissionError", "0o444 · lee · PermissionError")],
                    ["Linux: ve · lee · escribe", "Windows: ve · lee · escribe"], ["teal", "gold"],
                    note="En Windows, chmod solo activa o quita el atributo de solo lectura: 0o000 no impide leer. Los permisos reales de Windows viven en listas de control de acceso (ACL) "
                         "y tokens, no en bits de modo. Linux se comprobó como usuario sin privilegios (uid 1000); como administrador el resultado de 0o000 sería otro.",
                    note_kind="coral", label_w=220, row_h=56)


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
    return mapa("Una denegación es información: dos intentos observados",
                "Tres comandos como usuario sin privilegios, cada uno con su resultado y su lectura: leer /etc/shadow (modo 640, propietario root) produce Permission denied; sudo sin contraseña interactiva informa que se requiere una contraseña; id muestra que la identidad no equivale a autoridad.",
                [("cat /etc/shadow", "cat: /etc/shadow: Permission denied (modo 640, propietario root)", "coral",
                  "El kernel aplicó el control de acceso: el archivo existe y la identidad no tiene el permiso"),
                 ("sudo -n true", "sudo: a password is required", "gold",
                  "La elevación requiere una autenticación que este contexto no ofrece; no es una falla del comando"),
                 ("id (uid 1000)", "El usuario pertenece a varios grupos y no a root", "teal",
                  "Identidad no equivale a autoridad: los grupos y la política deciden qué puede hacerse")],
                note="Elevar privilegios para «ver si funciona» es una intervención con riesgo y no una prueba. La respuesta correcta empieza por identificar sujeto, acción, objeto y política.",
                left_w=200, mid_w=330, row_h=76, heads=("Intento", "Resultado observado", "Lectura correcta"))


# ---------------------------------------------------------------- SE-028
def se028_codigos() -> Fig:
    return columnas("Cómo termina un proceso: códigos de salida observados en Windows y Linux",
                    "Seis formas de terminar un proceso observadas desde Python. Tres dan el mismo resultado en ambos sistemas (sys.exit(3), una excepción sin tratar y el tiempo agotado de subprocess.run) y tres divergen: terminate() da 1 en Windows y -15 en Linux, SIGKILL solo existe como señal en Linux (-9) y un manejador de SIGTERM limpia y sale con 0.",
                    [("sys.exit(3)", "3", "3"),
                     ("Excepción sin tratar", "1", "1"),
                     ("terminate() sin manejador", "1 (TerminateProcess)", "-15 (señal SIGTERM)"),
                     ("kill / SIGKILL", "No aplicable como señal", "-9 (no se puede interceptar)"),
                     ("SIGTERM con manejador que limpia", "No aplicable", "0 y escribe «limpiando»"),
                     ("subprocess.run(timeout=1) sobre un proceso de 10 s", "TimeoutExpired", "TimeoutExpired")],
                    ["Windows", "Linux (WSL2)"], ["gold", "teal"],
                    note="En POSIX un código negativo en Python significa «terminado por la señal N»; en Windows no existe ese canal y todo es un entero.",
                    label_w=330, row_h=52)


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
    cases = [
        ("prog /tmp/p02*.txt", "Bash", ["/tmp/p02a.txt", "/tmp/p02b.txt"], "gold", "el comodín se expande antes de llegar al programa"),
        ('prog "/tmp/p02*.txt"', "Bash", ["/tmp/p02*.txt"], "teal", "las comillas impiden la expansión: llega literal"),
        ('x="un archivo.txt"; prog $x', "Bash", ["un", "archivo.txt"], "gold", "la variable sin comillas se divide por los espacios"),
        ('x="un archivo.txt"; prog "$x"', "Bash", ["un archivo.txt"], "teal", "con comillas el valor es un solo argumento"),
        ("prog *.nada", "PowerShell 5.1", ["*.nada"], "teal", "no expande el comodín para programas nativos"),
        ("prog $x (con espacio)", "PowerShell 5.1", ["un archivo.txt"], "teal", "no divide el valor: un solo argumento"),
    ]
    f = Fig(960, 550, "Quién interpreta los argumentos antes de que el programa los reciba",
            "Seis órdenes con su shell y la lista de argumentos que recibe el programa, dibujada como fichas: en Bash, un comodín sin comillas se expande a dos archivos y entre comillas llega literal; una variable con espacio sin comillas se divide en dos argumentos y entre comillas es uno; en PowerShell un comodín sin coincidencias llega literal.")
    f.text(155, 24, "Orden escrita", 13, "middle", 700, "#32505f")
    f.text(391, 24, "Shell", 13, "middle", 700, "#32505f")
    f.text(490, 24, "Argumentos que recibe el programa", 13, "start", 700, "#32505f")
    y = 38
    for command, shell, args, kind, why in cases:
        f.box(10, y, 290, 56, command, "plain", 12)
        f.box(326, y, 130, 56, shell, "navy", 12, True)
        f.arrow([(300, y + 28), (326, y + 28)])
        f.arrow([(456, y + 28), (482, y + 28)])
        x = 482.0
        for a in args:
            wd = text_width(a, 12, 700) + 20
            f.box(x, y + 4, wd, 32, a, kind, 12, True)
            x += wd + 6
        f.text(482, y + 52, f"{len(args)} argumento{'s' if len(args) > 1 else ''}: {why}", 11, "start", 400, "#32505f")
        y += 74
    f.box(10, y + 6, 940, 50, "El programa nunca ve las comillas ni el comodín: ve la lista final. Un shell distinto produce otra lista con el mismo texto.", "gold", 13)
    return f


def se029_pipefail() -> Fig:
    return mapa("El código de salida de un pipeline",
                "Cinco situaciones de Bash con su resultado: false | true da código 0 por defecto y 1 con pipefail; un cd fallido sin set -e deja al script operando en el directorio anterior y con set -e detiene el subshell con código 1; ls de un directorio inexistente da 2.",
                [("false | true", "código 0", "gold", "Solo cuenta el último comando: el fallo inicial se oculta"),
                 ("set -o pipefail; false | true", "código 1", "teal", "Cualquier comando que falle hace fallar el pipeline"),
                 ("cd /noexiste (sin set -e)", "el script sigue en el directorio anterior", "coral", "Un fallo ignorado deja el script operando en otro lugar"),
                 ("set -e; cd /noexiste", "el subshell termina con código 1", "teal", "El fallo detiene la ejecución"),
                 ("ls /noexiste", "código 2", "gold", "Los códigos son una interfaz: cada herramienta documenta los suyos")],
                note="Un script robusto declara cómo trata los fallos y comprueba los códigos que le importan.",
                left_w=270, mid_w=250, row_h=58, heads=("Situación", "Resultado observado", "Lectura"))


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
    return columnas("PowerShell pasa objetos; Bash pasa texto",
                    "Cuatro aspectos con la respuesta de cada shell: en PowerShell 5.1 el pipeline lleva objetos System.Diagnostics.Process con propiedades como BasePriority y una lista de cadenas es un arreglo de objetos String; en Bash los comandos intercambian bytes de texto que cada programa debe analizar.",
                    [("Lo que viaja por el pipeline", "Objetos .NET: System.Diagnostics.Process", "Bytes de texto por stdout"),
                     ("Acceso a un dato", "Propiedad: (Get-Process -Id $PID).BasePriority", "Analizar columnas con otro programa (awk, cut)"),
                     ("Tipo de una lista", "Object[] de String", "Texto separado por saltos de línea"),
                     ("Conversión de tipos", "1 + '2' = 3; '1' + 2 = 12 (manda el tipo del lado izquierdo)", "Todo es texto hasta que un programa lo interpreta")],
                    ["PowerShell 5.1", "Bash"], ["gold", "teal"],
                    note="Ninguno es «mejor»: los objetos evitan analizar texto, y el texto es la interfaz común de las herramientas POSIX. Un adaptador debe traducir entre ambos modelos, no suponer que son iguales.",
                    label_w=220, row_h=62)


def se030_errores() -> Fig:
    return columnas("Errores en dos shells: lo que se observó",
                    "Cuatro situaciones con la respuesta de PowerShell 5.1 y de Bash: un error no terminante deja $? en falso y sigue; con -ErrorAction Stop se lanza ItemNotFoundException que se captura; un programa nativo deja su código en $LASTEXITCODE; con Set-StrictMode una variable no definida es un error. En Bash, $? guarda el código del último comando y set -e detiene el script.",
                    [("Falla un comando", "Error no terminante: $? = False y el script continúa", "$? = código distinto de 0 y el script continúa"),
                     ("Hacer que el fallo detenga", "-ErrorAction Stop → excepción ItemNotFoundException que try/catch captura", "set -e (con sus excepciones documentadas)"),
                     ("Programa nativo con código 5", "$LASTEXITCODE = 5 y $? = False", "$? = 5"),
                     ("Variable no definida", "Set-StrictMode: error «no se puede recuperar porque no se ha establecido»", "Expande a vacío salvo set -u")],
                    ["PowerShell 5.1", "Bash"], ["gold", "teal"],
                    note="Cada shell tiene varios canales de error. Un contrato común define qué es un fallo (código de salida y mensaje estructurado) y cada adaptador lo traduce.",
                    label_w=220, row_h=66)


def se030_niveles() -> Fig:
    return mapa("Niveles de portabilidad de un script",
                "Cuatro niveles de portabilidad, de lo más estrecho a lo más amplio: un script de Bash, un script POSIX sh, un script de PowerShell y un núcleo en un lenguaje con adaptadores finos; de cada nivel salen lo que exige de la plataforma y lo que no garantiza.",
                [("Bash", "Que Bash esté instalado y sea compatible", "teal", "Que exista en Windows sin una capa adicional"),
                 ("POSIX sh", "Un intérprete que cumpla la especificación POSIX", "teal", "Que las herramientas externas (sed, date) se comporten igual"),
                 ("PowerShell", "PowerShell 5.1 en Windows o PowerShell 7 multiplataforma", "teal", "Que 5.1 y 7 tengan los mismos módulos y comportamientos"),
                 ("Núcleo común + adaptadores finos", "Un runtime (por ejemplo, Python 3.11+) y un adaptador por shell", "teal", "Que el adaptador exprese cada diferencia: se prueba en cada plataforma")],
                note="Copiar el mismo script a tres sistemas solo desplaza el fallo; definir la intención común y probar cada adaptador lo hace visible.",
                left_w=210, mid_w=330, row_h=64, stack=True, heads=("Nivel (de lo estrecho a lo amplio)", "Qué exige de la plataforma", "Qué no garantiza"))


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
