"""Figures for SE-097 to SE-108 (values measured with CPython 3.12.9 on Windows 11; Linux 3.12.3 where noted)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab, bars

M = "Medido con CPython 3.12.9 en Windows 11 (ruff 0.15.20, mypy 2.1.0); los tiempos dependen del equipo y se leen como razones."
S = "Medido con CPython 3.12.9 en Windows 11; Linux (WSL2, CPython 3.12.3) donde se indica."


# ---------------------------------------------------------------- SE-097
def se097_intercambio() -> Fig:
    rows = [["initialize → respuesta", "240 ms", "El servidor arranca y declara sus capacidades"],
            ["didOpen → publishDiagnostics", "351 ms", "Tres diagnósticos: F401 (línea 1), F401 (línea 2) y F841 (línea 5)"],
            ["didChange → publishDiagnostics", "5 ms", "Dos diagnósticos: F401 (línea 1) y F841 (línea 4); `os` ya no se importa"],
            ["Mensaje `initialized`", "79 bytes", "Cabecera Content-Length más cuerpo JSON-RPC"]]
    return tab("Un intercambio LSP real con ruff server", "Tabla de mediciones de un intercambio con un servidor de lenguaje real: initialize tardó 240 ms, el primer análisis tras didOpen 351 ms y la actualización tras didChange 5 ms; el mensaje initialized ocupa 79 bytes.",
               ["Mensaje", "Tiempo o tamaño", "Qué ocurrió"], rows, [270, 160, 480], row_h=56,
               note="El primer análisis es mucho más lento que las ediciones siguientes (351 ms frente a 5 ms): el editor no recibe diagnósticos con la misma latencia en el arranque que durante la edición.", foot=M)


def se097_capacidades() -> Fig:
    rows = [["textDocumentSync", "Sí", "El editor envía el texto con didOpen y didChange"],
            ["diagnosticProvider", "Sí", "Calcula diagnósticos y los publica"],
            ["codeActionProvider · documentFormattingProvider", "Sí", "Ofrece correcciones y formato"],
            ["hoverProvider", "Sí", "Información al pasar el cursor"],
            ["completionProvider · definitionProvider", "No", "No aparecen entre las 10 capacidades declaradas: este servidor no completa ni navega"]]
    return tab("Protocolo no es capacidad", "Tabla de las diez capacidades que declaró ruff server en la respuesta initialize: sincronización de texto, diagnósticos, acciones de código, formato y hover están declaradas; completado y definición no aparecen.",
               ["Capacidad", "¿Declarada?", "Consecuencia"], rows, [330, 120, 460], row_h=56,
               note="Hablar LSP no equivale a ofrecer todas las funciones. Si el editor muestra completado, lo ofrece otro servidor; si no lo muestra, no es un fallo del protocolo sino una capacidad ausente.", foot=M)


def se097_tolerancia() -> Fig:
    rows = [["ast.parse del código roto", "SyntaxError en la línea 1", "'(' was never closed: se detiene en el primer error"],
            ["tokenize del mismo código", "TokenError", "El analizador léxico también se detiene antes del final"],
            ["ast.parse de 59 999 líneas válidas", "432 ms", "Reanalizar el archivo completo en cada pulsación no es viable"],
            ["didChange de ruff en un archivo pequeño", "5 ms", "El servidor mantiene el documento en memoria"]]
    return tab("Editar código roto y mantener la latencia", "Tabla que muestra que ast.parse y tokenize se detienen en el primer error del código roto, que analizar 59999 líneas con ast.parse tarda 432 ms y que una actualización incremental en el servidor tarda 5 ms.",
               ["Prueba", "Resultado", "Lectura"], rows, [320, 220, 370], row_h=56,
               note="Un editor trabaja casi siempre con código incompleto. Por eso los servidores usan analizadores tolerantes a errores y actualizaciones incrementales; la biblioteca estándar es un compilador, no un servicio interactivo.", foot=M)


# ---------------------------------------------------------------- SE-098
def se098_sesion() -> Fig:
    rows = [["b 3", "Breakpoint 1 at …t.py:3", "Se fija el punto en la línea de `c = b + 1`"],
            ["c", "> …(3)f() → c = b + 1", "La ejecución continúa y se detiene en la línea 3"],
            ["p b · p a", "10 · 5", "Estado observado: a = 5 y b = 10"],
            ["bt", "run() → <module> → f()", "La pila muestra el llamador y la función"],
            ["n · p c", "11 (esperado: 5·2+1)", "Un paso y se imprime el resultado"]]
    return tab("Una sesión de pdb guionada", "Tabla de una sesión real de pdb ejecutada con comandos por entrada estándar: un breakpoint en la línea 3, continuar, imprimir b igual a 10 y a igual a 5, mostrar la pila y avanzar un paso.",
               ["Comando", "Salida", "Qué se aprende"], rows, [140, 330, 440], row_h=52,
               note="Un depurador no «arregla»: muestra el estado en un instante. La hipótesis (¿b vale 10?) se formula antes del comando y el resultado la confirma o la refuta.", foot=S)


def se098_costo() -> Fig:
    items = [("Sin trazado", 43.7, "teal", "43,7 ms"), ("sys.monitoring (PY_START)", 84.9, "gold", "84,9 ms · 1,9×"),
             ("settrace, eventos de llamada", 174.7, "coral", "174,7 ms · 4,0×"), ("settrace, eventos de línea", 422.6, "coral", "422,6 ms · 9,7×")]
    return bars("Costo de observar la ejecución", "Barras con el tiempo de 300 000 llamadas a una función: sin trazado 43,7 ms, con sys.monitoring 84,9 ms (1,9 veces), con settrace de llamadas 174,7 ms (4,0 veces, 300 001 eventos) y con settrace de líneas 422,6 ms (9,7 veces, 1 500 005 eventos).",
                items, 0.7, "Observar cambia lo observado: un fallo que depende de tiempos puede desaparecer bajo el depurador. Los eventos medidos fueron 300 001 de llamada y 1 500 005 de línea para 300 000 llamadas.", label_w=280, foot=S)


def se098_breakpoint() -> Fig:
    rows = [["`breakpoint()` con PYTHONBREAKPOINT=0", "Imprime «siguio 1»", "La llamada no hace nada: se puede dejar sin querer"],
            ["`breakpoint()` sin la variable", "Detiene el proceso y espera entrada", "En un servicio sin terminal queda colgado"],
            ["`python -m pdb script.py`", "Arranca en la primera línea", "No requiere modificar el código"]]
    return tab("Controlar los puntos de interrupción", "Tabla que compara tres formas de entrar en el depurador: breakpoint con PYTHONBREAKPOINT igual a cero continúa y la ejecución imprime siguio 1, sin la variable detiene el proceso y python -m pdb arranca en la primera línea.",
               ["Forma de entrar", "Resultado medido", "Riesgo o ventaja"], rows, [310, 280, 320], row_h=56,
               note="Un breakpoint() olvidado en el código es un defecto: puede colgar un proceso sin terminal. La política es una regla de revisión y una variable de entorno de entornos no interactivos.", foot=S)


# ---------------------------------------------------------------- SE-099
def se099_cprofile() -> Fig:
    items = [("Carga sin perfilar", 27.4, "teal", "27,4 ms"), ("Con cProfile", 132.5, "coral", "132,5 ms · 4,8×")]
    return bars("El perfilador determinista altera la carga", "Barras con el tiempo de una carga con 1 200 018 llamadas: 27,4 milisegundos sin perfilar y 132,5 milisegundos con cProfile, 4,8 veces más.",
                items, 2.2, "cProfile registró 1 200 018 llamadas. Su costo se paga por llamada: reparte el tiempo entre funciones pequeñas con un sesgo hacia las que se llaman más veces. El perfil indica dónde mirar, no cuánto vale cada función sin la herramienta.", label_w=250, foot=M)


def se099_memoria() -> Fig:
    items = [("Asignar 200 000 cadenas, sin tracemalloc", 44, "teal", "44 ms"), ("Con tracemalloc activo", 2719, "coral", "2 719 ms · ≈62×")]
    return bars("Medir memoria también cuesta", "Barras con el tiempo de crear 200 000 cadenas: 44 milisegundos sin tracemalloc y 2 719 milisegundos con tracemalloc, unas 62 veces más; el pico medido fue de 14 910 KiB.",
                items, 0.3, "tracemalloc midió un pico de 14 910 KiB para 200 000 cadenas, pero multiplicó el tiempo por unas 62. La memoria se perfila en una ejecución dedicada, no en la medición de tiempos.", label_w=330, foot=M)


def se099_muestreo() -> Fig:
    rows = [["<genexpr>", "21", "Es donde estaba la ejecución la mayor parte del tiempo"],
            ["helper", "7", "La función llamada desde el generador"],
            ["cold · wait", "1 y 1", "Casi sin muestras: no es el cuello de botella"],
            ["Tiempo con muestreo", "205 ms", "Frente a 192 ms sin muestrear: +7 %"]]
    return tab("Un perfil por muestreo con poca perturbación", "Tabla del resultado de muestrear la pila del hilo principal cada milisegundo: 21 muestras en el generador, 7 en helper y una en cold y wait; el tiempo con muestreo fue 205 ms frente a 192 ms sin muestrear.",
               ["Función observada", "Muestras", "Lectura"], rows, [240, 150, 520], row_h=52,
               note="Con 30 muestras en total la precisión es baja: el muestreo señala dónde se gasta el tiempo con un margen amplio. Perturba mucho menos (+7 % frente a 4,8×), a cambio de menos detalle y de funciones rápidas que pueden no aparecer.", foot=S)


# ---------------------------------------------------------------- SE-100
def se100_matriz() -> Fig:
    rows = [["Importación sin usar", "F401", "0", "ok", "Lo ve el linter"],
            ["Nombre no definido (en función no llamada)", "F821", "0", "ok", "Falla solo si la función se ejecuta"],
            ["`f('a')` con `x: int`", "—", "1", "ok", "Lo ve el verificador; las anotaciones no se aplican en ejecución"],
            ["`x: Any` y `x + 1` con una cadena", "—", "0", "TypeError", "`Any` apaga la verificación"],
            ["`d['k']` sobre un dict vacío", "—", "0", "KeyError", "Solo la ejecución lo revela"],
            ["Argumento mutable por defecto", "—", "0", "ok", "No lo marca el conjunto de reglas por defecto"]]
    return tab("Qué detecta cada herramienta", "Matriz de seis fragmentos con lo que detectan ruff y mypy y lo que ocurre al ejecutar: ruff detecta F401 y F821, mypy detecta el argumento mal tipado y los demás defectos solo aparecen al ejecutar o con reglas no activas.",
               ["Fragmento", "ruff", "Errores de mypy", "Ejecución", "Lectura"], rows, [290, 70, 110, 100, 340], row_h=60,
               note="Ninguna herramienta cubre todo: el linter, el verificador de tipos y la ejecución detectan clases distintas de defectos. Un conjunto de reglas por defecto no incluye todas las reglas relevantes.", foot=M)


def se100_velocidad() -> Fig:
    items = [("ruff check (3000 funciones)", 199, "teal", "199 ms"), ("py_compile", 217, "teal", "217 ms"), ("mypy (sin caché)", 2031, "gold", "2 031 ms · ≈10×")]
    return bars("Cuánto tardan en un archivo de 6000 líneas", "Barras con el tiempo de analizar un archivo con 3000 funciones: ruff 199 milisegundos, py_compile 217 y mypy sin caché 2031, unas diez veces más.",
                items, 0.1, "La velocidad cambia dónde se puede ejecutar: un linter de 0,2 s corre en cada guardado; un verificador de tipos de 2 s sin caché se ejecuta al guardar con caché incremental o en integración continua. La medición incluye el arranque del intérprete.", label_w=270, foot=M)


def se100_formato() -> Fig:
    rows = [["Aplicar black dos veces", "Misma salida", "El formateo es idempotente: aplicarlo de nuevo no cambia nada"],
            ["Linters integrados en ruff", "59", "Familias de reglas; cada una se activa o desactiva por separado"],
            ["Reglas activas por defecto", "E y F", "Estilo básico y errores de nombres; el resto se elige"],
            ["Argumento mutable por defecto", "Sin aviso", "La regla B006 existe pero no está activa por defecto"]]
    return tab("Formato, reglas y configuración", "Tabla con tres comprobaciones: black es idempotente, ruff integra 59 familias de reglas y el argumento mutable por defecto no genera aviso con el conjunto por defecto.",
               ["Comprobación", "Resultado", "Lectura"], rows, [280, 160, 470], row_h=56,
               note="La configuración es parte del resultado: el mismo código pasa o falla según las reglas activas. Por eso el conjunto de reglas se versiona junto con el código.", foot=M)


# ---------------------------------------------------------------- SE-101
def se101_orden() -> Fig:
    rows = [["Orden 1, 2, 3 (de arriba abajo)", "11", "22", "El resultado coincide con el texto del cuaderno"],
            ["Se ejecuta la celda 2 dos veces y luego la 3", "11 → 21", "42", "El mismo cuaderno produce otra salida"]]
    return tab("El estado oculto de un cuaderno", "Tabla con la misma secuencia de celdas ejecutada en orden y fuera de orden: en orden las salidas son 11 y 22 y con la segunda celda ejecutada dos veces son 11, 21 y 42.",
               ["Secuencia de ejecución", "Celda 2", "Celda 3", "Lectura"], rows, [310, 130, 110, 360], row_h=56,
               note="El kernel conserva variables entre celdas. Ejecutar la celda 2 dos veces cambió el valor de x y el resultado final pasó de 22 a 42 sin que el texto del cuaderno cambiara. Un cuaderno reproducible se ejecuta completo desde un kernel nuevo.", foot=S)


def se101_json() -> Fig:
    items = [("Cuaderno sin ejecutar", 587, "teal", "587 bytes"), ("Tras ejecutar tres celdas", 1838, "coral", "1 838 bytes · 3,1×")]
    return bars("Qué guarda un archivo .ipynb", "Barras con el tamaño de un cuaderno de tres celdas: 587 bytes sin ejecutar y 1838 bytes tras ejecutarlo; la diferencia genera 61 líneas de cambio.",
                items, 0.18, "Ejecutar el cuaderno añadió salidas y números de ejecución: el diff creció en 61 líneas por código idéntico. Para revisar cambios se limpian las salidas antes de confirmar o se usan herramientas de comparación de cuadernos.", label_w=280, foot=S)


def se101_exploracion() -> Fig:
    rows = [["Identificador de celda en el JSON", "Presente", "Permite referirse a una celda concreta entre versiones"],
            ["Salidas guardadas en el archivo", "Sí", "Pueden contener datos o secretos que se confirman sin querer"],
            ["Ejecución completa desde un kernel nuevo", "11 → 22", "Es la comprobación de reproducibilidad"],
            ["REPL de Python (`python -i`)", "Sin archivo", "El estado vive en la sesión y no queda registrado"]]
    return tab("De la exploración al código reproducible", "Tabla con cuatro propiedades de los cuadernos y del REPL: identificadores de celda presentes, salidas guardadas, ejecución completa desde un kernel nuevo con resultado 11 y 22 y el REPL sin archivo asociado.",
               ["Propiedad", "Valor medido", "Consecuencia"], rows, [340, 150, 420], row_h=56,
               note="La exploración es valiosa si termina en un artefacto que otra persona pueda ejecutar de arriba abajo. Lo explorado en una sesión sin registro es una conjetura, no evidencia.", foot=S)


# ---------------------------------------------------------------- SE-102
def se102_arranque() -> Fig:
    items = [("Windows, arranque normal", 127, "gold", "127 ms"), ("Windows, -I -S", 63, "teal", "63 ms"),
             ("Linux (WSL2), arranque normal", 31, "gold", "31 ms"), ("Linux (WSL2), -I -S", 19, "teal", "19 ms")]
    return bars("Cuánto tarda en arrancar un intérprete vacío", "Barras con la mediana de siete arranques de un intérprete que no hace nada: 127 ms en Windows con arranque normal y 63 ms con las opciones -I y -S; 31 ms y 19 ms en Linux.",
                items, 2.4, "Cada módulo que carga el arranque suma tiempo (66 líneas de importación en Windows). El mismo intérprete y la misma versión no tienen el mismo costo en dos sistemas; el runtime también es parte del entorno.", label_w=300, foot=S)


def se102_resolucion() -> Fig:
    rows = [["`where python`", "3 candidatos", "Varios ejecutables cumplen el nombre; gana el primero en PATH"],
            ["`py -0`", "3 entradas", "El lanzador lista versiones registradas, incluida una de 32 bits"],
            ["`uv python list --only-installed`", "4 entradas", "Otra herramienta ve un conjunto distinto"],
            ["`sys.executable`", "Uno", "El intérprete que ejecutó el script"]]
    return tab("Qué Python se ejecuta", "Tabla de tres formas de listar intérpretes en la misma máquina: where encontró tres candidatos, el lanzador py listó tres versiones y uv listó cuatro; sys.executable identifica el que realmente se ejecuta.",
               ["Consulta", "Resultado", "Lectura"], rows, [310, 160, 440], row_h=56,
               note="«python» no identifica un intérprete: depende de PATH, del lanzador y de la herramienta. La evidencia es `sys.executable` y `sys.version` dentro del propio proceso.", foot=S)


def se102_versiones() -> Fig:
    rows = [["Windows", "3.12.9", "3.12.9 (64 bits) en PATH; también 3.14 de 32 bits y otros"],
            ["Linux (WSL2)", "3.12.3", "Versión menor distinta de la de Windows con la misma serie 3.12"],
            ["Archivo de versión del proyecto", "Falta", "Ni una ni otra quedan fijadas por el repositorio"]]
    return tab("Una misma serie, dos compilaciones", "Tabla que compara las versiones medidas: Windows ejecutó CPython 3.12.9 y Linux 3.12.3, ambas de la serie 3.12, y el repositorio no fija una versión exacta.",
               ["Entorno", "Versión", "Lectura"], rows, [220, 160, 530], row_h=56,
               note="Un resultado medido en 3.12.9 puede no repetirse en 3.12.3 o en 3.14. Fijar la versión exacta (en un archivo de versión del gestor o en la configuración del contenedor) convierte la suposición en un requisito comprobable.", foot=S)


# ---------------------------------------------------------------- SE-103
def se103_tamano() -> Fig:
    rows = [["venv con pip (Windows)", "11 344 ms", "860", "11 550 KiB"],
            ["venv --without-pip (Windows)", "180 ms", "7", "557 KiB"],
            ["uv venv (Windows)", "278 ms", "16", "555 KiB"],
            ["venv --without-pip (Linux)", "118 ms", "8", "enlace simbólico a python"],
            ["venv con pip (Linux)", "6 376 ms", "—", "pip y setuptools incluidos"]]
    return tab("Crear un entorno virtual cuesta lo que se instala", "Tabla de la creación de entornos virtuales: con pip en Windows 11 344 ms, 860 archivos y 11 550 KiB; sin pip 180 ms, 7 archivos y 557 KiB; con uv 278 ms; en Linux sin pip 118 ms y con pip 6376 ms.",
               ["Creación", "Tiempo", "Archivos", "Tamaño o nota"], rows, [310, 150, 130, 320], row_h=52,
               note="Casi todo el costo del entorno es pip: 860 archivos frente a 7. En Linux el intérprete del entorno es un enlace simbólico; en Windows se copia un ejecutable lanzador.", foot=S)


def se103_cfg() -> Fig:
    rows = [["`pyvenv.cfg`", "home · include-system-site-packages · version · executable · command", "Cinco claves que enlazan el entorno con su intérprete"],
            ["`sys.prefix == sys.base_prefix`", "False dentro del entorno", "Así se detecta que se ejecuta dentro de un venv"],
            ["Longitud de `sys.path`", "7 (entorno) · 16 (sistema)", "El entorno ve menos rutas que el intérprete global"]]
    return tab("Cómo se aísla un entorno", "Tabla de lo medido en un entorno virtual: pyvenv.cfg tiene cinco claves, sys.prefix difiere de sys.base_prefix y sys.path tiene 7 entradas dentro del entorno frente a 16 en el intérprete del sistema.",
               ["Elemento", "Valor medido", "Lectura"], rows, [250, 340, 320], row_h=60,
               note="El aislamiento no es un contenedor: es una configuración de rutas. El entorno comparte el intérprete base y el sistema operativo; solo cambia dónde se buscan e instalan los paquetes.", foot=S)


def se103_paquete() -> Fig:
    rows = [["`import demo_pkg` en el intérprete global", "Falla", "El paquete no está instalado allí"],
            ["`import demo_pkg` dentro del entorno", "1.0.0", "Instalado con `--no-index --no-deps` desde un archivo local"],
            ["`pip list` dentro del entorno", "2 paquetes", "pip y demo-pkg; nada más"],
            ["`pip freeze` de dos entornos nuevos", "Idéntico", "Misma rueda instalada produce el mismo estado"]]
    return tab("Instalar sin contaminar el sistema", "Tabla de una instalación local: demo_pkg no se puede importar en el intérprete global, se importa dentro del entorno con versión 1.0.0, pip list muestra dos paquetes y pip freeze de dos entornos nuevos es idéntico.",
               ["Comprobación", "Resultado", "Lectura"], rows, [330, 160, 420], row_h=56,
               note="Se instaló una rueda construida localmente, sin red. La reproducibilidad del entorno depende de poder instalar los mismos archivos exactos, no de la versión escrita en un archivo de requisitos.", foot=S)


# ---------------------------------------------------------------- SE-104
def se104_estado() -> Fig:
    rows = [["Cliente y motor de Docker", "29.9.2 · linux · overlayfs", "`docker info` respondió en 1 327 ms: el motor estaba en marcha"],
            ["Imagen construida desde `scratch`", "9 383 bytes · 1 capa", "Un solo archivo copiado; primera construcción 4 325 ms, segunda 1 221 ms"],
            ["Dos construcciones con `--no-cache`", "IDs distintos", "ddb3953a1aea frente a 244e4937f237 con el mismo contexto"],
            ["`docker create` + `docker cp`", "314 ms · 373 ms", "Se creó el contenedor y se leyó el archivo sin ejecutar nada"],
            ["Ejecutar un proceso en el contenedor", "No medido", "No se descargó ninguna imagen base de un registro externo"]]
    return tab("Qué se midió con el motor en marcha", "Tabla de lo medido con Docker 29.9.2: docker info en 1327 ms, una imagen de 9383 bytes y una capa construida desde scratch en 4325 y 1221 ms, dos construcciones con identificadores distintos, creación del contenedor en 314 ms y copia del archivo en 373 ms; la ejecución de un proceso no se midió.",
               ["Elemento", "Valor medido", "Lectura"], rows, [270, 210, 430], row_h=60,
               note="Todo se hizo sin red: la imagen parte de `scratch` y no hay proceso que ejecutar. El arranque de un contenedor con un sistema base real queda sin medir, y se declara como límite.", foot="Medido con Docker 29.9.2 sobre Windows 11 (motor Linux, 8 CPU).")


def se104_config() -> Fig:
    rows = [["image", "Imagen base", "Una etiqueta cambia; un digest fija el contenido"],
            ["features", "Piezas instalables", "Añaden herramientas sin editar la imagen"],
            ["postCreateCommand", "pip install -r requirements.txt", "Se ejecuta después de crear el contenedor, con red"],
            ["customizations", "Extensiones del editor", "La extensión de ruff queda en la configuración, no en la memoria de alguien"]]
    return tab("Anatomía de un dev container", "Tabla de las cinco claves de un devcontainer.json de ejemplo y su efecto: image, features, postCreateCommand y customizations con una extensión de ruff.",
               ["Clave", "Contenido de ejemplo", "Efecto"], rows, [180, 280, 450], row_h=56,
               note="Un dev container declara el entorno como código. La garantía depende de lo que se fije: una etiqueta de imagen puede apuntar a otro contenido mañana; un digest no.", foot="Estructura de una configuración de ejemplo; no se ejecutó.")


def se104_desechable() -> Fig:
    rows = [["Entorno virtual", "180–278 ms", "Aísla paquetes; comparte intérprete y sistema"],
            ["Contenedor (`docker create`)", "314 ms", "Aísla también el sistema de archivos y las herramientas"],
            ["Máquina virtual", "No medido", "Aísla el kernel; más pesada"]]
    return tab("Niveles de aislamiento", "Tabla de niveles de aislamiento: un entorno virtual se crea en 180 a 278 ms y comparte el intérprete y el sistema; crear un contenedor tomó 314 ms y la máquina virtual no se midió.",
               ["Nivel", "Costo medido", "Qué aísla"], rows, [260, 210, 440], row_h=56,
               note="Más aislamiento no es mejor por defecto: cuesta tiempo y recursos. Se elige el nivel que cubre el riesgo (dependencias, herramientas o sistema operativo) y se declara el resto.", foot="El costo de la máquina virtual no se midió; 314 ms es crear, no arrancar, un contenedor.")


# ---------------------------------------------------------------- SE-105
def se105_ddmin() -> Fig:
    rows = [["Entrada que falla", "403 caracteres", "Contiene un `[` sin cerrar tras «ab»"],
            ["Caso mínimo", "`ab[` (3 caracteres)", "Reducción del 99,3 %"],
            ["Pruebas ejecutadas", "24", "Frente a 403 pruebas de un carácter cada una"]]
    return tab("Reducir un caso hasta lo esencial", "Tabla de una reducción automática: una entrada de 403 caracteres que falla se redujo a los tres caracteres ab[ con 24 pruebas.",
               ["Magnitud", "Valor", "Lectura"], rows, [250, 230, 430], row_h=52,
               note="La reducción no entiende el defecto: solo elimina trozos mientras el fallo persista. Funciona si la prueba es determinista; con una prueba intermitente puede quedarse con un caso que no es mínimo.", foot=S)


def se105_bisect() -> Fig:
    rows = [["Historia", "64 commits", "El defecto se introduce en el commit 41"],
            ["`git bisect run`", "6 pasos", "log₂ 64 = 6: cada paso descarta la mitad"],
            ["Commit señalado", "c41", "Coincide con el cambio introducido a propósito"]]
    return tab("Buscar el cambio culpable", "Tabla de una bisección automática en una historia de 64 commits: el defecto se introdujo en el commit 41 y git bisect run lo encontró en 6 pasos.",
               ["Elemento", "Resultado", "Lectura"], rows, [250, 190, 470], row_h=52,
               note="La bisección da el primer commit en que falla la prueba, no la causa. Asume que antes funcionaba y después falla siempre; un defecto intermitente o dos defectos distintos la engañan.", foot=S)


def se105_pasos() -> Fig:
    items = [("Eliminar un carácter cada vez", 403, "coral", "403 pruebas"), ("ddmin (reducción por trozos)", 24, "teal", "24 pruebas"), ("Bisección de 64 commits", 6, "teal", "6 pruebas")]
    return bars("Cuántas pruebas necesita cada estrategia", "Barras con las pruebas necesarias: 403 eliminando un carácter cada vez, 24 con ddmin y 6 para bisecar 64 commits.",
                items, 2.0, "Elegir la estrategia cambia el costo en órdenes de magnitud. El conteo de pruebas es reproducible; el tiempo de cada prueba depende de lo que se ejecute.", label_w=290, foot=S)


# ---------------------------------------------------------------- SE-106
def se106_contraste() -> Fig:
    rows = [["Negro sobre blanco", "21,00", "Cumple"], ["Gris #767676 sobre blanco", "4,54", "Cumple AA (≥ 4,5)"],
            ["Gris #777777 sobre blanco", "4,48", "No cumple AA"], ["Verde #00aa00 sobre blanco", "3,11", "No cumple para texto normal"],
            ["Azul #0000ff sobre fondo #1e1e1e", "1,94", "Prácticamente ilegible"]]
    return tab("Contraste calculado con la fórmula de WCAG", "Tabla de razones de contraste calculadas: negro sobre blanco 21,00, gris 767676 sobre blanco 4,54 que cumple AA, gris 777777 sobre blanco 4,48 que no cumple, verde 00aa00 sobre blanco 3,11 y azul 0000ff sobre fondo 1e1e1e 1,94.",
               ["Combinación", "Razón", "Veredicto"], rows, [400, 150, 360], row_h=44,
               note="Una diferencia imperceptible en el color (#767676 frente a #777777) cruza el umbral de 4,5. El contraste se calcula, no se juzga a ojo, y vale para el texto normal; el grande admite 3.", foot="Calculado con la fórmula de luminancia relativa de WCAG 2.2.")


def se106_tema() -> Fig:
    rows = [["Comentario #6a9955 sobre #1e1e1e (tema oscuro)", "5,00", "Cumple AA"], ["Comentario #008000 sobre blanco (tema claro)", "5,14", "Cumple AA"],
            ["Rojo #ff0000 sobre negro", "5,25", "Cumple, pero el color no es el único canal"]]
    return tab("Temas del editor y accesibilidad", "Tabla de contraste de colores de comentarios en temas del editor: 5,00 en el tema oscuro, 5,14 en el claro y 5,25 el rojo sobre negro.",
               ["Combinación", "Razón", "Veredicto"], rows, [440, 130, 340], row_h=52,
               note="Cumplir el contraste no basta: el color no debe ser el único modo de distinguir un error. El editor debe ofrecer también un símbolo o un texto.", foot="Calculado con la fórmula de luminancia relativa de WCAG 2.2.")


def se106_latencia() -> Fig:
    items = [("Actualización de diagnósticos (didChange)", 5, "teal", "5 ms"), ("Primer análisis (didOpen)", 351, "gold", "351 ms"), ("Reanalizar 60 000 líneas con ast.parse", 432, "coral", "432 ms")]
    return bars("Presupuesto de latencia de una herramienta interactiva", "Barras con tres latencias medidas: 5 ms para actualizar diagnósticos, 351 ms para el primer análisis y 432 ms para reanalizar 60 000 líneas.",
                items, 0.9, "La herramienta debe responder dentro del ritmo de la persona. Con 5 ms la ayuda es continua; con 351 ms es perceptible; con 432 ms por pulsación, inutilizable. Una herramienta lenta se vuelve una herramienta que se desactiva.", label_w=330, foot=M)


# ---------------------------------------------------------------- SE-107
def se107_flujo() -> Fig:
    rows = [["1. Reproducir", "Prueba determinista que falla", "Sin ella, ninguna técnica posterior es fiable"],
            ["2. Reducir", "403 → 3 caracteres en 24 pruebas", "El caso mínimo apunta al mecanismo"],
            ["3. Localizar", "6 pasos para 64 commits", "Encuentra el cambio, no la causa"],
            ["4. Observar", "pdb: b = 10 y a = 5 en la línea 3", "Confirma o refuta la hipótesis"],
            ["5. Verificar", "Nueva prueba, falla antes y pasa después", "Evita declarar resuelto lo que solo dejó de verse"]]
    return tab("Diagnosticar un fallo desconocido: la secuencia", "Tabla de cinco pasos con datos medidos: reproducir con una prueba determinista, reducir 403 caracteres a 3 en 24 pruebas, bisecar 64 commits en 6 pasos, observar el estado con pdb y verificar con una prueba nueva.",
               ["Paso", "Dato medido", "Por qué importa"], rows, [190, 330, 390], row_h=52,
               note="Cada paso reduce el espacio de búsqueda y deja un registro. El orden no es rígido, pero saltarse la reproducción deja el resto sin base.", foot=S)


def se107_hipotesis() -> Fig:
    rows = [["H1: el defecto está en el analizador", "Se reduce a `ab[`", "Se confirma: el caso mínimo lo fuerza"],
            ["H2: el defecto lo introdujo el commit 41", "Bisect señala c41", "Se confirma con la prueba automática"],
            ["H3: depende del estado de `b`", "pdb muestra b = 10", "Se descarta: el valor es el esperado"]]
    return tab("Registro de hipótesis", "Tabla de un registro de tres hipótesis: el analizador, el commit 41 y el valor de b; las dos primeras se confirman con la reducción y la bisección, y la tercera se descarta con la observación en pdb.",
               ["Hipótesis", "Prueba", "Resultado"], rows, [340, 240, 330], row_h=56,
               note="Descartar es información. Una hipótesis descartada con su prueba evita volver a investigarla y muestra qué se comprobó.", foot=S)


def se107_limites() -> Fig:
    rows = [["Reducción", "Funciona con pruebas deterministas", "Falla con fallos intermitentes"],
            ["Bisección", "Funciona con un solo cambio culpable", "Dos defectos o interacciones la confunden"],
            ["Depurador", "Muestra el estado en un instante", "Perturba tiempos (hasta 9,7× de costo)"]]
    return tab("Cada técnica tiene su condición", "Tabla de las condiciones de cada técnica de diagnóstico: la reducción requiere pruebas deterministas, la bisección un único cambio culpable y el depurador perturba los tiempos hasta 9,7 veces.",
               ["Técnica", "Cuándo funciona", "Cuándo falla"], rows, [190, 360, 360], row_h=56,
               note="Elegir mal la técnica produce conclusiones falsas con aspecto de evidencia. Antes de aplicarla se comprueba su condición.", foot=S)


# ---------------------------------------------------------------- SE-108
def se108_inventario() -> Fig:
    rows = [["Intérprete", "CPython 3.12.9 (Windows) · 3.12.3 (Linux)", "Se fija con la versión exacta"],
            ["Entorno virtual", "7 archivos sin pip · 860 con pip", "Se crea desde cero con un comando"],
            ["Dependencias", "Una rueda local", "Se instala con `--no-index --no-deps`"],
            ["Verificación", "`pip freeze` idéntico en dos entornos", "Se compara el estado, no se asume"]]
    return tab("Inventario de un entorno autocontenido", "Tabla del inventario de un entorno autocontenido: intérprete con versión exacta, entorno virtual de 7 archivos sin pip y 860 con pip, dependencias desde una rueda local y verificación con pip freeze idéntico en dos entornos.",
               ["Elemento", "Valor medido", "Cómo se fija"], rows, [190, 380, 340], row_h=56,
               note="Un entorno autocontenido es el que se puede reconstruir desde el repositorio y comprobar. Cada fila debe tener su comprobación; lo que solo se asume queda como riesgo.", foot=S)


def se108_hash() -> Fig:
    rows = [["Primera construcción de la rueda", "b384a5f15d7d", "SHA-256 abreviado"],
            ["Segunda construcción, mismo código", "762d3c781a63", "Distinto aunque el código no cambió"],
            ["`pip freeze` en dos entornos", "Idéntico", "Instalar la misma rueda reproduce el estado"]]
    return tab("Reproducir el entorno no es reproducir los bytes", "Tabla de dos construcciones de la misma rueda con hashes distintos, b384a5f15d7d y 762d3c781a63, aunque el código no cambió, mientras que dos entornos con la misma rueda producen el mismo pip freeze.",
               ["Comprobación", "Resultado", "Lectura"], rows, [350, 190, 370], row_h=56,
               note="Dos construcciones del mismo código dieron archivos distintos (las marcas de tiempo entran en la rueda). Por eso se fija el archivo que se instala por su hash, y no se reconstruye en cada entorno.", foot=S)


def se108_aceptacion() -> Fig:
    rows = [["Reconstruir el entorno desde cero", "Un comando", "Sin pasos manuales ni conocimiento oral"],
            ["Aislamiento comprobado", "Importa solo dentro del entorno", "`import demo_pkg` falla fuera y devuelve 1.0.0 dentro"],
            ["Versiones fijadas", "Intérprete y rueda por hash", "No se aceptan etiquetas flotantes"],
            ["Límites declarados", "Arranque en contenedor no medido", "No se descargó ninguna imagen base"]]
    return tab("Criterios de aceptación del proyecto", "Tabla de cuatro criterios de aceptación: reconstrucción desde cero con un comando, aislamiento comprobado, versiones fijadas por hash y límites declarados como el arranque en contenedor no medido.",
               ["Criterio", "Evidencia", "Lectura"], rows, [310, 250, 350], row_h=56,
               note="El proyecto se acepta por lo que se puede comprobar, incluidos los límites declarados. Un entorno que «funciona en mi máquina» no cumple ninguno de los cuatro.", foot=S)


FIGURES = {
    "se-097-intercambio-lsp.svg": se097_intercambio,
    "se-097-capacidades-declaradas.svg": se097_capacidades,
    "se-097-codigo-roto-y-latencia.svg": se097_tolerancia,
    "se-098-sesion-pdb.svg": se098_sesion,
    "se-098-costo-de-observar.svg": se098_costo,
    "se-098-breakpoint-olvidado.svg": se098_breakpoint,
    "se-099-costo-de-cprofile.svg": se099_cprofile,
    "se-099-costo-de-tracemalloc.svg": se099_memoria,
    "se-099-perfil-por-muestreo.svg": se099_muestreo,
    "se-100-que-detecta-cada-herramienta.svg": se100_matriz,
    "se-100-velocidad-de-analisis.svg": se100_velocidad,
    "se-100-formato-y-reglas.svg": se100_formato,
    "se-101-estado-oculto.svg": se101_orden,
    "se-101-tamano-del-ipynb.svg": se101_json,
    "se-101-de-la-exploracion-al-codigo.svg": se101_exploracion,
    "se-102-arranque-del-interprete.svg": se102_arranque,
    "se-102-que-python-se-ejecuta.svg": se102_resolucion,
    "se-102-versiones-medidas.svg": se102_versiones,
    "se-103-costo-del-entorno.svg": se103_tamano,
    "se-103-como-se-aisla.svg": se103_cfg,
    "se-103-instalacion-local.svg": se103_paquete,
    "se-104-lo-verificado.svg": se104_estado,
    "se-104-anatomia-devcontainer.svg": se104_config,
    "se-104-niveles-de-aislamiento.svg": se104_desechable,
    "se-105-reduccion-de-casos.svg": se105_ddmin,
    "se-105-biseccion-de-64-commits.svg": se105_bisect,
    "se-105-pruebas-por-estrategia.svg": se105_pasos,
    "se-106-contraste-wcag.svg": se106_contraste,
    "se-106-temas-del-editor.svg": se106_tema,
    "se-106-presupuesto-de-latencia.svg": se106_latencia,
    "se-107-secuencia-de-diagnostico.svg": se107_flujo,
    "se-107-registro-de-hipotesis.svg": se107_hipotesis,
    "se-107-condiciones-de-cada-tecnica.svg": se107_limites,
    "se-108-inventario-del-entorno.svg": se108_inventario,
    "se-108-hash-de-la-rueda.svg": se108_hash,
    "se-108-criterios-de-aceptacion.svg": se108_aceptacion,
}
