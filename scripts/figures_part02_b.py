"""Figures for SE-031 to SE-036 (values measured on Windows 11 and Ubuntu 24.04 under WSL2)."""
from __future__ import annotations

from figure_kit import Fig


# ---------------------------------------------------------------- SE-031
def se031_precedencia() -> Fig:
    f = Fig(960, 440, "Precedencia de configuración: tres resoluciones reales",
            "Tabla con la función de precedencia argumento, entorno, archivo y valor por omisión aplicada a tres casos: sin argumento gana el entorno, con argumento gana el argumento y sin nada gana el valor por omisión.")
    heads = ["Argumento", "Entorno", "Archivo", "Por omisión", "Resultado (fuente, valor)"]
    rows = [
        ["—", "8081", "8082", "8080", "entorno, 8081"],
        ["9000", "8081", "8082", "8080", "argumento, 9000"],
        ["—", "—", "—", "8080", "default, 8080"],
    ]
    f.table(heads, rows, 10, 12, [150, 150, 150, 150, 340], row_h=60, size=14, kinds=["plain", "plain", "plain", "plain", "teal"])
    f.box(10, 262, 940, 76, "El orden es determinista y se registra: la ficha de configuración efectiva dice de dónde viene cada valor. Cambiar el orden entre ejecuciones (o entre adaptadores) cambia el comportamiento sin cambiar el código.", "gold", 13)
    f.box(10, 350, 940, 76, "En el laboratorio, `profile` se resuelve con argumento, DIAG_PROFILE, settings.json y valor predeterminado, y el reporte conserva la fuente elegida.", "grey", 13)
    return f


def se031_entorno() -> Fig:
    f = Fig(960, 450, "Variables de entorno en Windows y en Linux",
            "Tabla con resultados reales: buscar una variable con distinto uso de mayúsculas la encuentra en Windows y no en Linux; un proceso hijo hereda la variable en ambos; los valores son siempre texto "
            "y asignar un entero lanza TypeError.")
    heads = ["Prueba", "Windows", "Linux (WSL2)"]
    rows = [
        ["Buscar «mi_var» tras fijar «MI_VAR»", "'valor' (no distingue mayúsculas)", "None (distingue mayúsculas)"],
        ["Un proceso hijo lee la variable", "'valor' (la hereda)", "'valor' (la hereda)"],
        ["Tipo de «PUERTO» = 8080", "str", "str"],
        ["os.environ['N'] = 5", "TypeError", "TypeError"],
    ]
    f.table(heads, rows, 10, 12, [380, 280, 280], row_h=60, size=13)
    f.box(10, 332, 940, 100, "El entorno es una lista de pares texto-texto que se hereda; no tiene tipos ni esquema. Un programa que lo usa convierte y valida explícitamente (por ejemplo, un puerto debe ser un entero entre 1 y 65535) "
          "y no depende de mayúsculas para distinguir variables si debe funcionar en ambos sistemas.", "grey", 13)
    return f


def se031_secreto() -> Fig:
    f = Fig(960, 470, "Dónde puede verse un secreto ficticio en Linux y cómo lo trata el laboratorio",
            "Tabla: un secreto pasado como argumento es visible en /proc/PID/cmdline y en ps; el mismo secreto en una variable de entorno es legible en /proc/PID/environ por el propietario, cuyo modo es 0o400; "
            "el laboratorio informa solo presencia, longitud 23 y el texto redactado.")
    heads = ["Dónde viaja el secreto", "Resultado observado", "Lectura"]
    rows = [
        ["Argumento de línea de comandos (--token=...)", "Visible en /proc/PID/cmdline y en la salida de ps: «ps muestra el secreto: True»", "Cualquier usuario que pueda listar procesos lo ve; evitar secretos en argumentos"],
        ["Variable de entorno (API_KEY=...)", "Legible en /proc/PID/environ; archivo con modo 0o400", "Protegido de otros usuarios, no del propietario ni de procesos hijos que lo heredan"],
        ["Reporte del laboratorio (DIAG_DEMO_TOKEN)", "present: true; length: 23; value: [REDACTED]; el texto no aparece", "Se conserva presencia y longitud, no el valor"],
    ]
    f.table(heads, rows, 10, 12, [300, 360, 280], row_h=100, size=12)
    f.box(10, 390, 940, 64, "El valor era una cadena ficticia. Un secreto real se lee de un almacén dedicado, se pasa por un canal restringido y se redacta en cualquier registro o informe.", "coral", 13)
    return f


# ---------------------------------------------------------------- SE-032
def se032_paquete() -> Fig:
    f = Fig(960, 480, "Un paquete visto desde el gestor del sistema: coreutils en Ubuntu 24.04",
            "Tabla con campos reales de dpkg y apt para el paquete coreutils: versión instalada 9.4-3ubuntu6, arquitectura amd64, mantenedor Ubuntu Developers, versión candidata 9.4-3ubuntu6.3 del repositorio noble-updates, "
            "dependencias previas como libacl1, libattr1, libc6, libgmp10 y libselinux1, y verificación de archivos sin diferencias.")
    heads = ["Campo", "Valor observado", "Qué informa"]
    rows = [
        ["Package / Maintainer", "coreutils / Ubuntu Developers", "Quién empaqueta y se responsabiliza del paquete en esta distribución"],
        ["Version / Architecture", "9.4-3ubuntu6 / amd64", "La versión del paquete (no solo del programa) y el contrato binario"],
        ["Candidate (apt policy)", "9.4-3ubuntu6.3 desde noble-updates", "Hay una actualización disponible; instalada no es lo mismo que candidata"],
        ["PreDepends", "libacl1, libattr1, libc6, libgmp10, libselinux1", "Lo que debe estar presente antes de instalar: el árbol de dependencias"],
        ["dpkg --verify coreutils", "Sin salida; código 0", "Los archivos coinciden con las sumas de verificación registradas"],
    ]
    f.table(heads, rows, 10, 12, [230, 330, 380], row_h=64, size=12)
    f.box(10, 414, 940, 52, "Un gestor de paquetes es una base de datos de versiones, relaciones y sumas de verificación; instalar es modificarla de forma controlada.", "gold", 13)
    return f


def se032_usrmerge() -> Fig:
    f = Fig(940, 420, "Qué paquete es dueño de /bin/ls: una respuesta que depende de la ruta",
            "Preguntar a dpkg por /bin/ls no encuentra ninguna ruta, mientras /usr/bin/ls pertenece al paquete coreutils, porque /bin es un enlace simbólico a usr/bin en Ubuntu 24.04.")
    f.box(20, 30, 360, 70, "dpkg -S /bin/ls\n→ no path found matching pattern /bin/ls", "coral", 13, bold=True)
    f.box(20, 130, 360, 70, "dpkg -S /usr/bin/ls\n→ coreutils: /usr/bin/ls", "teal", 13, bold=True)
    f.box(430, 30, 490, 70, "ls -ld /bin → lrwxrwxrwx ... /bin -> usr/bin", "grey", 13, bold=True)
    f.arrow([(380, 65), (430, 65)], dashed=True)
    f.box(430, 130, 490, 70, "El gestor registra rutas reales (/usr/bin/ls); un enlace simbólico no es dueño de nada", "plain", 13)
    f.box(20, 230, 900, 70, "Una consulta correcta del gestor exige la ruta canónica (por ejemplo, con `readlink -f`). La misma pregunta con una ruta equivalente da respuestas distintas: la evidencia depende de cómo se formula.", "gold", 13)
    f.box(20, 316, 900, 70, "Qué paquete es dueño de un archivo es una afirmación del gestor del sistema, no una propiedad del archivo. Los programas instalados por otras vías (pip, descargas) no aparecen en dpkg.", "grey", 13)
    return f


def se032_instalar() -> Fig:
    f = Fig(940, 440, "Instalar puede ejecutar código: lo que se observa y lo que se documenta",
            "Tabla con una observación real (hay 624 archivos de scripts de mantenedor preinst, postinst, prerm o postrm en /var/lib/dpkg/info de este Ubuntu) y dos afirmaciones documentadas: "
            "las fuentes de Python pueden ejecutar código al construirse, y las ruedas no ejecutan código de instalación.")
    heads = ["Mecanismo", "Evidencia", "Consecuencia"]
    rows = [
        ["Scripts de mantenedor de paquetes .deb", "Observado: 624 archivos preinst/postinst/prerm/postrm en el sistema de prueba", "Instalar un paquete del sistema ejecuta código con privilegios de administrador"],
        ["Distribución fuente de Python (sdist)", "Documentado: la construcción puede ejecutar código del paquete", "Instalar desde una fuente es ejecutar código de un tercero en tu equipo"],
        ["Rueda de Python (wheel)", "Documentado: formato de archivos ya construidos, sin paso de ejecución de instalación", "Reduce la superficie, pero el código del paquete sigue ejecutándose al importarlo"],
    ]
    f.table(heads, rows, 10, 12, [260, 360, 320], row_h=88, size=12)
    f.box(10, 350, 920, 72, "La confianza se decide antes de instalar: procedencia del repositorio, firma, alcance (sistema o usuario) y un plan de reversión.", "coral", 13)
    return f


# ---------------------------------------------------------------- SE-033
def se033_evento() -> Fig:
    f = Fig(940, 420, "Anatomía de un evento del Registro de eventos de Windows",
            "Tabla con los campos de tres eventos reales del registro Application: hora de creación, identificador, nivel y proveedor. El registro es circular.")
    heads = ["Hora (local)", "Id", "Nivel", "Proveedor"]
    rows = [
        ["13/11/2026 11:38:00", "8224", "Información", "VSS"],
        ["13/11/2026 11:25:53", "8224", "Información", "VSS"],
        ["13/11/2026 11:25:41", "8302", "Información", "Microsoft-Windows-System-Restore"],
    ]
    f.table(heads, rows, 10, 12, [240, 100, 200, 390], row_h=54, size=13)
    f.box(10, 250, 920, 76, "Un evento útil tiene estructura: cuándo (con zona horaria), quién lo emitió (proveedor), qué es (identificador) y cuánta importancia tiene (nivel). El texto libre es el último recurso.", "gold", 13)
    f.box(10, 338, 920, 60, "El modo del registro es circular: los eventos antiguos se sobrescriben. La evidencia de un incidente se exporta antes de que se pierda.", "coral", 13)
    return f


def se033_tiempo() -> Fig:
    f = Fig(940, 400, "La misma hora, dos escrituras: local con desfase y UTC",
            "Una entrada del journal con la marca 2026-11-13T11:38:54-03:00 y la hora en UTC 14:38:54 son el mismo instante. Sin el desfase, dos registros de equipos distintos no se pueden ordenar.")
    f.box(20, 40, 400, 70, "Journal (hora local con desfase)\n2026-11-13T11:38:54-03:00", "gold", 14, bold=True)
    f.box(520, 40, 400, 70, "date -u (UTC)\n2026-11-13T14:38:54Z", "teal", 14, bold=True)
    f.arrow([(420, 75), (520, 75)], "mismo instante")
    f.box(20, 150, 900, 70, "11:38:54 en -03:00 equivale a 14:38:54 en UTC (11 + 3 = 14). Los formatos ISO 8601 con desfase o con Z permiten ordenar eventos de distintos orígenes.", "plain", 13)
    f.box(20, 236, 900, 70, "Un reloj de pared puede ajustarse hacia atrás; para medir duraciones se usa un reloj monotónico (en la prueba, 0,203 s en ambos relojes: no hubo ajuste).", "grey", 13)
    f.box(20, 320, 900, 56, "El orden de llegada de líneas de registro no es el orden de ocurrencia: se ordena por marca de tiempo y se declara la sincronización.", "coral", 13)
    return f


def se033_linea() -> Fig:
    f = Fig(960, 460, "Diagnosticar es iterar hipótesis: un servicio que falla con 200/CHDIR",
            "Cuatro pasos: observar el registro del servicio, formular hipótesis, probar la más barata y verificar la corrección. Ejemplo genérico: el código de salida 200/CHDIR indica que el servicio no pudo cambiar al directorio de trabajo configurado.")
    steps = [
        ("1 Observar", "journalctl: «Main process exited, code=exited, status=200/CHDIR»", "teal"),
        ("2 Hipótesis", "El directorio de trabajo no existe, no es accesible o la ruta está mal escrita", "gold"),
        ("3 Prueba barata", "Comprobar la ruta de WorkingDirectory con ls -ld y los permisos con namei -l", "gold"),
        ("4 Corregir y verificar", "Crear el directorio o corregir la ruta; reiniciar y comprobar que el servicio queda activo", "teal"),
    ]
    for i, (name, text, kind) in enumerate(steps):
        x = 14 + i * 236
        f.box(x, 20, 222, 46, name, "navy", 13, bold=True)
        f.box(x, 74, 222, 130, text, kind, 12)
        if i < 3:
            f.arrow([(x + 222, 43), (x + 236, 43)])
    f.box(14, 232, 930, 70, "El código nombra la causa de preparación (no pudo entrar al directorio) y excluye hipótesis sobre el programa: el servicio ni siquiera llegó a ejecutarse. Un buen diagnóstico usa lo que el registro dice, no lo que sugiere.", "grey", 13)
    f.box(14, 316, 930, 60, "La línea roja anterior no siempre es la causa: se busca el primer evento anómalo y se comprueba que la corrección cambia el resultado.", "coral", 13)
    f.text(480, 410, "El ejemplo es genérico: el nombre de la unidad y la ruta se omiten a propósito.", 12, "middle", 400, "#5c1f14")
    return f


# ---------------------------------------------------------------- SE-034
def se034_capas() -> Fig:
    f = Fig(960, 470, "Capas de WSL2 con la evidencia que cada una deja",
            "Pila de capas: Windows como anfitrión, una máquina virtual ligera, un kernel de Linux con cadena microsoft-standard-WSL2, systemd como proceso 1 y el usuario; y el montaje 9p que conecta la unidad de Windows. "
            "Cada capa tiene un dato observable.")
    layers = [
        ("Usuario de Linux (uid 1000)", "id; cat /etc/os-release → Ubuntu 24.04", "teal"),
        ("systemd como PID 1", "ps -p 1 → systemd; systemd-detect-virt → wsl", "teal"),
        ("Kernel de Linux 6.18.58.1-microsoft-standard-WSL2", "uname -r; /proc/version", "gold"),
        ("Máquina virtual ligera gestionada por Windows", "No se ve desde dentro: se infiere por detect-virt y la cadena del kernel", "gold"),
        ("Windows 11 (anfitrión)", "platform.system() = Windows; los mismos archivos aparecen en /mnt/c vía 9p", "coral"),
    ]
    for i, (name, ev, kind) in enumerate(layers):
        y = 20 + i * 72
        f.box(14, y, 420, 60, name, kind, 13, bold=True)
        f.box(444, y, 500, 60, ev, "plain", 12)
        if i < 4:
            f.arrow([(224, y + 60), (224, y + 72)])
    f.box(14, 392, 930, 62, "Montajes observados: la raíz de Linux es ext4 y /mnt/c es 9p. Cruzar de una a otra cuesta rendimiento y cambia la semántica de permisos y de nombres (SE-026 y SE-027).", "grey", 13)
    return f


def se034_namespaces() -> Fig:
    f = Fig(960, 450, "Aislar sin una máquina virtual: espacios de nombres observados",
            "Un proceso de Linux pertenece a diez espacios de nombres. Con unshare se crean uno de usuario y uno de PIDs sin privilegios: dentro, el shell tiene PID 1 y uid 0; fuera, el mismo usuario es uid 1000.")
    f.box(14, 20, 440, 60, "Espacios de nombres del proceso (ls /proc/self/ns)", "navy", 13, bold=True)
    f.box(14, 88, 440, 130, "cgroup · ipc · mnt · net · pid · pid_for_children · time · time_for_children · user · uts", "grey", 13)
    f.box(484, 20, 460, 60, "unshare --user --map-root-user --pid --fork --mount-proc", "navy", 12, bold=True)
    f.box(484, 88, 220, 130, "Dentro:\nshell con PID 1\nuid = 0\nps solo ve 3 procesos", "teal", 13, bold=True)
    f.box(724, 88, 220, 130, "Fuera:\nel mismo usuario\nuid = 1000\nve todo su sistema", "gold", 13, bold=True)
    f.box(14, 244, 930, 70, "Un contenedor es un proceso con un conjunto de espacios de nombres (qué ve) y de cgroups (cuánto consume) sobre el kernel del anfitrión. El «root» de adentro es un mapeo, no autoridad sobre el equipo.", "plain", 13)
    f.box(14, 328, 930, 62, "cgroups v2 observado: el sistema de archivos de /sys/fs/cgroup es cgroup2fs.", "grey", 13)
    f.text(480, 424, "Docker Desktop estaba instalado pero su motor no estaba en ejecución; no se ejecutó ningún contenedor. Lo observado usa unshare, el mecanismo del kernel.", 12, "middle", 400, "#5c1f14")
    return f


def se034_comparacion() -> Fig:
    f = Fig(960, 440, "Máquina virtual, contenedor y proceso aislado: qué comparten",
            "Tabla comparativa de tres mecanismos: máquina virtual completa, contenedor y proceso con espacios de nombres. Se indica qué kernel usan, qué aísla y qué costo tiene.")
    heads = ["Mecanismo", "Kernel", "Qué aísla", "Costo y riesgo"]
    rows = [
        ["Máquina virtual (WSL2, Hyper-V)", "Uno propio por máquina", "Hardware virtual completo", "Arranque y memoria mayores; frontera fuerte mediada por el hipervisor"],
        ["Contenedor (Docker, Podman)", "El del anfitrión", "Procesos, red, sistema de archivos y recursos", "Arranque rápido; una falla del kernel afecta a todos"],
        ["Proceso con unshare", "El del anfitrión", "Los espacios de nombres elegidos", "Sin imagen ni red de forma automática: un bloque de construcción"],
    ]
    f.table(heads, rows, 10, 12, [250, 190, 250, 250], row_h=84, size=12)
    f.box(10, 350, 940, 70, "«Un contenedor es una VM pequeña» es falso: no tiene kernel propio. Aislar no elimina la confianza: el anfitrión y el kernel siguen siendo parte del límite.", "coral", 13)
    return f


# ---------------------------------------------------------------- SE-035
def se035_incidente() -> Fig:
    f = Fig(960, 480, "Incidente reproducido: un script falla al pasar de Windows a Linux",
            "Seis pasos: estabilizar el escenario, formular el síntoma, reducir hipótesis por capas, aplicar el cambio mínimo, verificar el caso original y el vecino, y documentar. Datos reales: el error de bash\\r, la prueba con file y la corrección.")
    steps = [
        ("1 Estabilizar", "Copia del script en un directorio de práctica; sin tocar el original"),
        ("2 Síntoma", "«/usr/bin/env: ‘bash\\r’: No such file or directory»"),
        ("3 Hipótesis", "¿Falta bash? ¿Shebang mal escrito? ¿Finales de línea ajenos?"),
        ("4 Prueba", "`file` informa «with CRLF line terminators»: finales de Windows"),
        ("5 Cambio mínimo", "Quitar \\r (sed -i) y fijar .gitattributes con eol=lf"),
        ("6 Verificar", "Funciona; el caso vecino (sin bit de ejecución) responde Permission denied"),
    ]
    for i, (name, text) in enumerate(steps):
        x = 14 + (i % 3) * 316
        y = 20 + (i // 3) * 190
        f.box(x, y, 300, 44, name, "navy", 13, bold=True)
        f.box(x, y + 50, 300, 110, text, ["grey", "coral", "gold", "teal", "teal", "gold"][i], 12)
    f.box(14, 408, 930, 56, "El cambio mínimo se aplica a la causa (finales de línea) y se registra su radio de efecto: el contenido no cambió, solo los finales de cada línea.", "plain", 13)
    return f


def se035_secuencia_lab() -> Fig:
    f = Fig(960, 470, "Reparar con límites: la secuencia real del laboratorio",
            "Secuencia observada en Linux con el laboratorio de la Parte 02: prepare cambia y repite sin cambios; inspect informa healthy; con settings.json corrupto inspect informa degraded con código 2; repair restaura; "
            "clean con un archivo ajeno se niega con código 3 y, tras retirarlo, termina con 0 dejando el workspace vacío.")
    heads = ["Paso", "Resultado observado", "Código", "Lectura"]
    rows = [
        ["prepare (1.ª vez / 2.ª vez)", "changed / unchanged", "0", "Idempotente: repetirlo no cambia nada"],
        ["inspect", "healthy · Linux x86_64", "0", "Diagnóstico de solo lectura"],
        ["settings.json = «{broken»; inspect", "degraded · integrity: invalid settings.json", "2", "Fallo estructurado, no una excepción"],
        ["repair; inspect", "changed; healthy", "0", "Restaura solo lo conocido"],
        ["clean con student-notes.txt dentro", "Se niega; el directorio queda con 4 archivos", "3", "No borra lo que no reconoce"],
        ["clean tras retirar el archivo", "Elimina el directorio del kit; el workspace queda vacío (0 entradas)", "0", "Limpieza acotada"],
    ]
    f.table(heads, rows, 10, 12, [290, 350, 80, 220], row_h=56, size=12)
    f.text(480, 462, "Ejecución real en Ubuntu 24.04 (WSL2) con el adaptador diagnostic-kit.sh sobre un workspace desechable.", 12, "middle", 400, "#5c1f14")
    return f


def se035_hipotesis() -> Fig:
    f = Fig(960, 450, "Reducir incertidumbre por capas: hipótesis, prueba y resultado esperado",
            "Tabla con cuatro hipótesis para el script que falla, la prueba barata para cada una y qué resultado la descarta o la confirma.")
    heads = ["Hipótesis", "Prueba barata", "La confirma si", "La descarta si"]
    rows = [
        ["El intérprete no existe", "command -v bash", "No imprime una ruta", "Imprime /usr/bin/bash"],
        ["El shebang está mal escrito", "head -1 script.sh | cat -A", "Muestra un nombre distinto de bash", "Muestra bash seguido de ^M (el nombre es correcto)"],
        ["Finales de línea de Windows", "file script.sh", "Informa CRLF line terminators", "Informa solo ASCII text"],
        ["Falta el bit de ejecución", "ls -l script.sh; bash script.sh", "bash script.sh funciona y ./script.sh falla", "Ambos fallan de la misma forma"],
    ]
    f.table(heads, rows, 10, 12, [230, 260, 230, 220], row_h=76, size=12)
    f.box(10, 396, 940, 44, "Se prueba primero lo más barato y lo que más discrimina; cada prueba debe poder refutar una hipótesis.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-036
def se036_arquitectura() -> Fig:
    f = Fig(960, 450, "Arquitectura del kit: un núcleo y dos adaptadores",
            "Un núcleo en Python (diagnostic_kit.py) con tres comandos, prepare, inspect, repair y clean, y dos adaptadores finos: diagnostic-kit.sh para Bash y diagnostic-kit.ps1 para PowerShell. "
            "El núcleo gobierna el contrato, los códigos de salida y la limpieza.")
    f.box(330, 20, 300, 60, "Persona o automatización", "grey", 14, bold=True)
    f.box(40, 130, 340, 60, "diagnostic-kit.sh (Bash)", "gold", 13, bold=True)
    f.box(580, 130, 340, 60, "diagnostic-kit.ps1 (PowerShell)", "gold", 13, bold=True)
    f.arrow([(480, 80), (210, 130)])
    f.arrow([(480, 80), (750, 130)])
    f.box(230, 240, 500, 70, "diagnostic_kit.py: contrato, esquema 1, códigos 0/2/3, limpieza acotada", "teal", 13, bold=True)
    f.arrow([(210, 190), (400, 240)])
    f.arrow([(750, 190), (560, 240)])
    f.box(40, 350, 880, 80, "Solo modifica .diagnostic-kit dentro de un workspace explícito; no enumera el entorno completo ni el usuario; no instala paquetes ni eleva privilegios. Los adaptadores traducen argumentos y códigos, no deciden.", "plain", 13)
    return f


def se036_pruebas() -> Fig:
    f = Fig(960, 520, "Matriz de verificación: diez pruebas en dos plataformas",
            "Tabla con las diez pruebas del laboratorio y su resultado: todas pasaron en Windows 11 con Python 3.12.9 en 0,257 segundos y en Ubuntu 24.04 bajo WSL2 con Python 3.12.3 en 1,710 segundos.")
    heads = ["Contrato que prueba", "Windows 11 · Python 3.12.9", "Linux (WSL2) · Python 3.12.3"]
    rows = [
        ["Idempotencia de prepare; esquema y minimización de inspect", "pasa", "pasa"],
        ["Precedencia argumento > entorno > archivo > default", "pasa", "pasa"],
        ["Secreto centinela redactado", "pasa", "pasa"],
        ["Corrupción → degraded; repair restaura", "pasa", "pasa"],
        ["clean solo elimina lo propio; se niega con entradas ajenas y con marker extraño", "pasa", "pasa"],
        ["Un workspace ausente nunca se crea", "pasa", "pasa"],
        ["Total", "10 pruebas en 0,257 s", "10 pruebas en 1,710 s"],
    ]
    f.table(heads, rows, 10, 12, [470, 235, 235], row_h=52, size=12, kinds=["plain", "teal", "teal"])
    f.box(10, 470, 940, 40, "Una ejecución local no sustituye a la matriz de CI (Linux, Windows y macOS): solo la matriz remota en verde demuestra compatibilidad.", "gold", 12)
    return f


def se036_estados() -> Fig:
    f = Fig(940, 420, "Estados y códigos de salida del kit",
            "Tres estados con su código: healthy con código 0, degraded por integridad con código 2 y refused por seguridad con código 3. Cada uno indica una acción distinta.")
    heads = ["Estado", "Código", "Cuándo ocurre", "Acción"]
    rows = [
        ["healthy / completado", "0", "El workspace es válido o la operación terminó", "Conservar la evidencia"],
        ["degraded / precondición inválida", "2", "settings.json corrupto, workspace ausente o configuración inválida", "Corregir el fixture y repetir; repair restaura lo conocido"],
        ["refused / rechazado por seguridad", "3", "Archivos ajenos o marker de otro dueño", "Revisar la propiedad; el kit no borra lo que no reconoce"],
    ]
    f.table(heads, rows, 10, 12, [230, 90, 330, 280], row_h=80, size=12)
    f.box(10, 330, 920, 70, "Los códigos son parte del contrato y están probados. Un script que consume el kit decide con ellos y no analizando el texto de los mensajes.", "gold", 13)
    return f


FIGURES = {
    "se-031-precedencia-resuelta.svg": se031_precedencia,
    "se-031-entorno-en-dos-sistemas.svg": se031_entorno,
    "se-031-donde-se-ve-un-secreto.svg": se031_secreto,
    "se-032-paquete-observado.svg": se032_paquete,
    "se-032-duenos-de-una-ruta.svg": se032_usrmerge,
    "se-032-instalar-ejecuta-codigo.svg": se032_instalar,
    "se-033-anatomia-de-un-evento.svg": se033_evento,
    "se-033-hora-local-y-utc.svg": se033_tiempo,
    "se-033-diagnostico-por-hipotesis.svg": se033_linea,
    "se-034-capas-de-wsl2.svg": se034_capas,
    "se-034-espacios-de-nombres.svg": se034_namespaces,
    "se-034-vm-contenedor-proceso.svg": se034_comparacion,
    "se-035-incidente-reproducido.svg": se035_incidente,
    "se-035-secuencia-del-laboratorio.svg": se035_secuencia_lab,
    "se-035-hipotesis-por-capa.svg": se035_hipotesis,
    "se-036-arquitectura-del-kit.svg": se036_arquitectura,
    "se-036-matriz-de-pruebas.svg": se036_pruebas,
    "se-036-estados-y-codigos.svg": se036_estados,
}
