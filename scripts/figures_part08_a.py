"""Figures for SE-097 to SE-108 (values measured with CPython 3.12.9 on Windows 11; Linux 3.12.3 where noted)."""
from __future__ import annotations

from figure_kit import Fig, _kit_finish, _kit_start, grouped_bars, heatmap, timeline
from figure_diagrams import card, chain, fan, merge, nested
from figures_part07_a import bars


M = "Medido con CPython 3.12.9 en Windows 11 (ruff 0.15.20, mypy 2.1.0); los tiempos dependen del equipo y se leen como razones."
S = "Medido con CPython 3.12.9 en Windows 11; Linux (WSL2, CPython 3.12.3) donde se indica."


# ---------------------------------------------------------------- SE-097
def se097_intercambio() -> Fig:
    return grouped_bars(
        'Un intercambio LSP real con ruff server',
        "Barras horizontales con el tiempo de cada mensaje de un intercambio real con ruff server: initialize tarda 240 milisegundos, el primer análisis tras didOpen 351 y la actualización tras didChange 5; el arranque y el primer análisis pesan decenas de veces más que una edición.",
        ["initialize → respuesta", "didOpen → publishDiagnostics", "didChange → publishDiagnostics"],
        [("Tiempo", [240, 351, 5], "teal")],
        unit="Tiempo hasta la respuesta (ms)", horizontal=True, label_w=270,
        note='El primer análisis es mucho más lento que las ediciones siguientes (351 ms frente a 5 ms): el editor no recibe diagnósticos con la misma latencia en el arranque que durante la edición.', note_kind='gold', foot=M)


def se097_capacidades() -> Fig:
    f, y = _kit_start('Protocolo no es capacidad',
                      "Diagrama del intercambio initialize entre el editor y ruff server: el servidor declara en su respuesta cinco grupos de capacidades, entre ellas sincronización de texto, diagnósticos, acciones de código, formato y hover, y no declara completado ni definición.",
                      940, None)
    card(f, 14, y + 70, 150, 120, "Editor", "pide initialize", "navy")
    f.group(250, y + 4, 676, 270, "Respuesta de initialize: 10 capacidades declaradas", "teal")
    f.arrow([(164, y + 130), (248, y + 130)], "initialize", label_at=(206, y + 118))
    f.arrow([(248, y + 160), (164, y + 160)])
    card(f, 268, y + 38, 300, 56, "textDocumentSync", "didOpen y didChange", "teal")
    card(f, 580, y + 38, 330, 56, "diagnosticProvider", "diagnósticos publicados", "teal")
    card(f, 268, y + 104, 300, 70, "codeActionProvider · documentFormattingProvider", "correcciones y formato", "teal")
    card(f, 580, y + 104, 330, 70, "hoverProvider", "información al pasar el cursor", "teal")
    card(f, 268, y + 190, 642, 66, "completionProvider · definitionProvider: no declaradas", "este servidor no completa ni navega; el completado lo ofrece otro servidor o falta", "coral", True)
    out = _kit_finish(f, y + 286, 'Hablar LSP no equivale a ofrecer todas las funciones. Si el editor muestra completado, lo ofrece otro servidor; si no lo muestra, no es un fallo del protocolo sino una capacidad ausente.', 'gold', M)
    out.kind = "diagram"
    return out


def se097_tolerancia() -> Fig:
    return fan(
        'Editar código roto y mantener la latencia',
        "Diagrama de lo que ocurre al editar código roto con un paréntesis sin cerrar: ast.parse lanza SyntaxError en la línea 1 y tokenize TokenError, los dos se detienen en el primer error; reanalizar 59999 líneas válidas con ast.parse tarda 432 ms, mientras ruff server mantiene el documento en memoria y actualiza en 5 ms.",
        ("Código roto en el editor", "un «(» sin cerrar", "navy"),
        [("ast.parse: SyntaxError en la línea 1", "se detiene en el primer error; reanalizar 59 999 líneas válidas cuesta 432 ms", "coral"),
         ("tokenize: TokenError", "el analizador léxico también se detiene antes del final", "coral"),
         ("Servidor de ruff: didChange en 5 ms", "mantiene el documento en memoria y actualiza sin reanalizar todo", "teal")],
        note='Un editor trabaja casi siempre con código incompleto. Por eso los servidores usan analizadores tolerantes a errores y actualizaciones incrementales; la biblioteca estándar es un compilador, no un servicio interactivo.', note_kind='gold', foot=M)


# ---------------------------------------------------------------- SE-098
def se098_sesion() -> Fig:
    return chain(
        'Una sesión de pdb guionada',
        "Cadena de cinco comandos de una sesión real de pdb: b 3 fija el punto en la línea 3, c continúa y se detiene allí, p b y p a muestran 10 y 5, bt muestra la pila y n más p c imprime 11, el resultado esperado de 5 por 2 más 1.",
        [("b 3", "Breakpoint 1 en la línea 3", "navy"), ("c", "se detiene en la línea 3: c = b + 1", "navy"), ("p b · p a", "10 · 5", "teal"),
         ("bt", "run() → <module> → f()", "teal"), ("n · p c", "11 (esperado: 5·2+1)", "teal")],
        note='Un depurador no «arregla»: muestra el estado en un instante. La hipótesis (¿b vale 10?) se formula antes del comando y el resultado la confirma o la refuta.', note_kind='gold', foot=S)


def se098_costo() -> Fig:
    items = [("Sin trazado", 43.7, "teal", "43,7 ms"), ("sys.monitoring (PY_START)", 84.9, "gold", "84,9 ms · 1,9×"),
             ("settrace, eventos de llamada", 174.7, "coral", "174,7 ms · 4,0×"), ("settrace, eventos de línea", 422.6, "coral", "422,6 ms · 9,7×")]
    return bars("Costo de observar la ejecución", "Barras con el tiempo de 300 000 llamadas a una función: sin trazado 43,7 ms, con sys.monitoring 84,9 ms (1,9 veces), con settrace de llamadas 174,7 ms (4,0 veces, 300 001 eventos) y con settrace de líneas 422,6 ms (9,7 veces, 1 500 005 eventos).",
                items, 0.7, "Observar cambia lo observado: un fallo que depende de tiempos puede desaparecer bajo el depurador. Los eventos medidos fueron 300 001 de llamada y 1 500 005 de línea para 300 000 llamadas.", label_w=280, foot=S)


def se098_breakpoint() -> Fig:
    return fan(
        'Controlar los puntos de interrupción',
        "Diagrama de tres formas de entrar en el depurador: breakpoint con PYTHONBREAKPOINT igual a cero no hace nada y la ejecución imprime siguio 1; sin la variable detiene el proceso y espera entrada, y en un servicio sin terminal queda colgado; python -m pdb script.py arranca en la primera línea sin tocar el código.",
        ("Un breakpoint() en el código", "tres formas de entrar", "navy"),
        [("PYTHONBREAKPOINT=0", "la llamada no hace nada: imprime «siguio 1» y se puede dejar sin querer", "gold"),
         ("Sin la variable", "detiene el proceso y espera entrada; sin terminal queda colgado", "coral"),
         ("python -m pdb script.py", "arranca en la primera línea; no requiere modificar el código", "teal")],
        note='Un breakpoint() olvidado en el código es un defecto: puede colgar un proceso sin terminal. La política es una regla de revisión y una variable de entorno de entornos no interactivos.', note_kind='gold', foot=S)


# ---------------------------------------------------------------- SE-099
def se099_cprofile() -> Fig:
    items = [("Carga sin perfilar", 27.4, "teal", "27,4 ms"), ("Con cProfile", 132.5, "coral", "132,5 ms · 4,8×")]
    return bars("El perfilador determinista altera la carga", "Barras con el tiempo de una carga con 1 200 018 llamadas: 27,4 milisegundos sin perfilar y 132,5 milisegundos con cProfile, 4,8 veces más.",
                items, 2.2, "cProfile registró 1 200 018 llamadas. Su costo se paga por llamada: reparte el tiempo entre funciones pequeñas con un sesgo hacia las que se llaman más veces. El perfil indica dónde mirar, no cuánto vale cada función sin la herramienta.", label_w=250, foot=M)


def se099_memoria() -> Fig:
    items = [("Asignar 200 000 cadenas, sin tracemalloc", 44, "teal", "44 ms"), ("Con tracemalloc activo", 2719, "coral", "2 719 ms · ≈62×")]
    return bars("Medir memoria también cuesta", "Barras con el tiempo de crear 200 000 cadenas: 44 milisegundos sin tracemalloc y 2 719 milisegundos con tracemalloc, unas 62 veces más; el pico medido fue de 14 910 KiB.",
                items, 0.17, "tracemalloc midió un pico de 14 910 KiB para 200 000 cadenas, pero multiplicó el tiempo por unas 62. La memoria se perfila en una ejecución dedicada, no en la medición de tiempos.", label_w=330, foot=M)


def se099_muestreo() -> Fig:
    return grouped_bars(
        'Un perfil por muestreo con poca perturbación',
        "Barras horizontales con las muestras de la pila del hilo principal tomadas cada milisegundo: 21 en el generador, 7 en helper y una en cold y otra en wait; el muestreo añade solo un 7 por ciento al tiempo (205 ms frente a 192 ms).",
        ["<genexpr>", "helper", "cold", "wait"],
        [("Muestras", [21, 7, 1, 1], "teal")],
        unit="Muestras de la pila (30 en total)", horizontal=True, label_w=130, ticks=[0, 5, 10, 15, 20, 25],
        note='Con 30 muestras en total la precisión es baja: el muestreo señala dónde se gasta el tiempo con un margen amplio. Perturba mucho menos (+7 % frente a 4,8×), a cambio de menos detalle y de funciones rápidas que pueden no aparecer.', note_kind='gold', foot=S)


# ---------------------------------------------------------------- SE-100
def se100_matriz() -> Fig:
    return heatmap(
        'Qué detecta cada herramienta',
        "Mapa de calor con lo que detecta cada herramienta en seis fragmentos: ruff detecta la importación sin usar y el nombre no definido; mypy solo el argumento mal tipado; la ejecución solo el TypeError con Any y el KeyError; el argumento mutable por defecto no lo detecta ninguna.",
        ["Importación sin usar", "Nombre no definido (función no llamada)", "f('a') con x: int", "x: Any y x + 1 con una cadena", "d['k'] sobre un dict vacío", "Argumento mutable por defecto"],
        ["ruff", "mypy", "Ejecución"],
        [[1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 0, 0]],
        unit="detección", row_title="Fragmento", col_title="¿La herramienta lo detecta?",
        scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "detecta" if v else "no lo ve", cell_h=42, label_w=300,
        note='Ninguna herramienta cubre todo: el linter, el verificador de tipos y la ejecución detectan clases distintas de defectos. Un conjunto de reglas por defecto no incluye todas las reglas relevantes.', note_kind='gold', foot=M)


def se100_velocidad() -> Fig:
    items = [("ruff check (3000 funciones)", 199, "teal", "199 ms"), ("py_compile", 217, "teal", "217 ms"), ("mypy (sin caché)", 2031, "gold", "2 031 ms · ≈10×")]
    return bars("Cuánto tardan en un archivo de 6000 líneas", "Barras con el tiempo de analizar un archivo con 3000 funciones: ruff 199 milisegundos, py_compile 217 y mypy sin caché 2031, unas diez veces más.",
                items, 0.1, "La velocidad cambia dónde se puede ejecutar: un linter de 0,2 s corre en cada guardado; un verificador de tipos de 2 s sin caché se ejecuta al guardar con caché incremental o en integración continua. La medición incluye el arranque del intérprete.", label_w=270, foot=M)


def se100_formato() -> Fig:
    f, y = _kit_start('Formato, reglas y configuración',
                      "Diagrama de la configuración de ruff: de 59 familias de reglas solo E y F están activas por defecto; la regla B006 del argumento mutable existe pero no está activa y no da aviso; aplicar black dos veces da la misma salida.",
                      940, None)
    f.group(14, y + 4, 640, 214, "ruff: 59 familias de reglas, cada una se activa por separado", "grey")
    card(f, 34, y + 40, 290, 70, "E y F: activas por defecto", "estilo básico y errores de nombres", "teal")
    card(f, 344, y + 40, 290, 70, "Resto de familias", "se eligen en la configuración", "plain", True)
    card(f, 34, y + 126, 600, 74, "B006 (argumento mutable por defecto): existe pero no está activa", "con el conjunto por defecto el código con ese defecto no recibe aviso", "coral", True)
    card(f, 680, y + 40, 246, 100, "black aplicado dos veces", "misma salida: el formateo es idempotente", "teal")
    f.arrow([(680 + 123, y + 140), (680 + 123, y + 160)])
    card(f, 680, y + 160, 246, 58, "La configuración se versiona con el código", "", "gold")
    out = _kit_finish(f, y + 234, 'La configuración es parte del resultado: el mismo código pasa o falla según las reglas activas. Por eso el conjunto de reglas se versiona junto con el código.', 'gold', M)
    out.kind = "diagram"
    return out


# ---------------------------------------------------------------- SE-101
def se101_orden() -> Fig:
    return timeline(
        'El estado oculto de un cuaderno',
        "Líneas de ejecución de las mismas celdas de un cuaderno: en orden 1, 2, 3 la celda 2 da 11 y la 3 da 22; si se ejecuta la celda 2 dos veces antes de la 3, la celda 2 da 11 y luego 21 y la 3 da 42, con el mismo texto en el cuaderno.",
        [("Orden 1, 2, 3 (de arriba abajo)", [(0, 1, "celda 1", "grey"), (1, 2, "celda 2 → 11", "teal"), (2, 3, "celda 3 → 22", "teal")]),
         ("Celda 2 dos veces, luego la 3", [(0, 1, "celda 1", "grey"), (1, 2, "celda 2 → 11", "teal"), (2, 3, "celda 2 → 21", "gold"), (3, 4, "celda 3 → 42", "coral")])],
        unit="Orden de ejecución (número de celda ejecutada)", ticks=[0, 1, 2, 3, 4], t_max=4, lane_h=58, label_w=250,
        note='El kernel conserva variables entre celdas. Ejecutar la celda 2 dos veces cambió el valor de x y el resultado final pasó de 22 a 42 sin que el texto del cuaderno cambiara. Un cuaderno reproducible se ejecuta completo desde un kernel nuevo.', note_kind='gold', foot=S)


def se101_json() -> Fig:
    items = [("Cuaderno sin ejecutar", 587, "teal", "587 bytes"), ("Tras ejecutar tres celdas", 1838, "coral", "1 838 bytes · 3,1×")]
    return bars("Qué guarda un archivo .ipynb", "Barras con el tamaño de un cuaderno de tres celdas: 587 bytes sin ejecutar y 1838 bytes tras ejecutarlo; la diferencia genera 61 líneas de cambio.",
                items, 0.18, "Ejecutar el cuaderno añadió salidas y números de ejecución: el diff creció en 61 líneas por código idéntico. Para revisar cambios se limpian las salidas antes de confirmar o se usan herramientas de comparación de cuadernos.", label_w=280, foot=S)


def se101_exploracion() -> Fig:
    return chain(
        'De la exploración al código reproducible',
        "Cadena de tres etapas de la exploración al código reproducible: el REPL no deja archivo, el cuaderno guarda identificadores de celda y salidas que pueden contener datos o secretos, y la ejecución completa desde un kernel nuevo da 11 y 22 y es la comprobación de reproducibilidad.",
        [("REPL de Python (python -i)", "sin archivo: el estado vive en la sesión y no queda registrado", "coral"),
         ("Cuaderno .ipynb", "id de cada celda presente; salidas guardadas que pueden contener datos o secretos", "gold"),
         ("Ejecución completa desde un kernel nuevo", "11 → 22: es la comprobación de reproducibilidad", "teal")],
        labels=["", ""], note='La exploración es valiosa si termina en un artefacto que otra persona pueda ejecutar de arriba abajo. Lo explorado en una sesión sin registro es una conjetura, no evidencia.', note_kind='gold', foot=S)


# ---------------------------------------------------------------- SE-102
def se102_arranque() -> Fig:
    items = [("Windows, arranque normal", 127, "gold", "127 ms"), ("Windows, -I -S", 63, "teal", "63 ms"),
             ("Linux (WSL2), arranque normal", 31, "gold", "31 ms"), ("Linux (WSL2), -I -S", 19, "teal", "19 ms")]
    return bars("Cuánto tarda en arrancar un intérprete vacío", "Barras con la mediana de siete arranques de un intérprete que no hace nada: 127 ms en Windows con arranque normal y 63 ms con las opciones -I y -S; 31 ms y 19 ms en Linux.",
                items, 2.4, "Cada módulo que carga el arranque suma tiempo (66 líneas de importación en Windows). El mismo intérprete y la misma versión no tienen el mismo costo en dos sistemas; el runtime también es parte del entorno.", label_w=300, foot=S)


def se102_resolucion() -> Fig:
    return grouped_bars(
        'Qué Python se ejecuta',
        "Barras horizontales con cuántos intérpretes lista cada consulta en la misma máquina: where python encuentra 3 candidatos, py -0 lista 3 versiones, uv python list lista 4 y sys.executable identifica uno solo, el que ejecutó el script.",
        ["where python", "py -0", "uv python list --only-installed", "sys.executable"],
        [("Intérpretes listados", [3, 3, 4, 1], "gold")],
        unit="Intérpretes que lista la consulta", horizontal=True, label_w=250, ticks=[0, 1, 2, 3, 4, 5],
        note='«python» no identifica un intérprete: depende de PATH, del lanzador y de la herramienta. La evidencia es `sys.executable` y `sys.version` dentro del propio proceso.', note_kind='gold', foot=S)


def se102_versiones() -> Fig:
    f, y = _kit_start('Una misma serie, dos compilaciones',
                      "Diagrama de las versiones medidas dentro de la serie 3.12: Windows ejecutó CPython 3.12.9 y Linux 3.12.3; el repositorio no tiene un archivo de versión, así que ninguna de las dos queda fijada.",
                      940, None)
    f.group(14, y + 4, 912, 120, "Serie 3.12 de CPython", "teal")
    card(f, 34, y + 40, 430, 72, "Windows: 3.12.9", "64 bits en PATH; también hay 3.14 de 32 bits y otros", "teal")
    card(f, 484, y + 40, 422, 72, "Linux (WSL2): 3.12.3", "versión menor distinta de la de Windows", "teal")
    f.arrow([(470, y + 124), (470, y + 148)], color="#c0432f")
    card(f, 14, y + 148, 912, 62, "Archivo de versión del proyecto: falta", "ni una ni otra quedan fijadas por el repositorio", "coral", True)
    out = _kit_finish(f, y + 224, 'Un resultado medido en 3.12.9 puede no repetirse en 3.12.3 o en 3.14. Fijar la versión exacta (en un archivo de versión del gestor o en la configuración del contenedor) convierte la suposición en un requisito comprobable.', 'gold', S)
    out.kind = "diagram"
    return out


# ---------------------------------------------------------------- SE-103
def se103_tamano() -> Fig:
    return grouped_bars(
        'Crear un entorno virtual cuesta lo que se instala',
        "Barras horizontales en escala logarítmica con el tiempo de crear un entorno virtual: con pip tarda 11 344 ms en Windows y 6 376 ms en Linux; sin pip 180 ms en Windows y 118 en Linux; uv venv en Windows 278 ms; casi todo el costo es pip.",
        ["Windows · venv con pip", "Windows · venv --without-pip", "Windows · uv venv", "Linux · venv con pip", "Linux · venv --without-pip"],
        [("Tiempo de creación", [11344, 180, 278, 6376, 118], "gold")],
        unit="Tiempo de creación (ms)", horizontal=True, log=True, label_w=250, ticks=[10, 100, 1000, 10000, 100000],
        note='Casi todo el costo del entorno es pip: 860 archivos frente a 7. En Linux el intérprete del entorno es un enlace simbólico; en Windows se copia un ejecutable lanzador.', note_kind='gold', foot=S)


def se103_cfg() -> Fig:
    f, y = _kit_start('Cómo se aísla un entorno',
                      "Diagrama de cómo se aísla un entorno virtual: pyvenv.cfg con cinco claves lo enlaza con el intérprete base; dentro del entorno sys.prefix difiere de sys.base_prefix y sys.path tiene 7 rutas frente a 16 del intérprete global.",
                      940, None)
    f.group(14, y + 4, 560, 246, "Entorno virtual", "teal")
    card(f, 34, y + 40, 520, 64, "pyvenv.cfg: cinco claves", "home · include-system-site-packages · version · executable · command", "teal")
    card(f, 34, y + 116, 520, 56, "sys.prefix == sys.base_prefix → False", "así se detecta que se ejecuta dentro de un venv", "teal")
    card(f, 34, y + 182, 520, 56, "sys.path: 7 rutas", "", "teal")
    card(f, 700, y + 40, 226, 76, "Intérprete base compartido", "el entorno solo cambia dónde se instala", "grey")
    card(f, 700, y + 182, 226, 56, "sys.path: 16 rutas", "intérprete global", "grey")
    f.arrow([(554, y + 72), (700, y + 72)], "home", label_at=(627, y + 62))
    out = _kit_finish(f, y + 266, 'El aislamiento no es un contenedor: es una configuración de rutas. El entorno comparte el intérprete base y el sistema operativo; solo cambia dónde se buscan e instalan los paquetes.', 'gold', S)
    out.kind = "diagram"
    return out


def se103_paquete() -> Fig:
    return fan(
        'Instalar sin contaminar el sistema',
        "Diagrama de la instalación local de una rueda: demo_pkg no se importa en el intérprete global; dentro del entorno se importa con versión 1.0.0 y pip list muestra dos paquetes; dos entornos nuevos con la misma rueda dan el mismo pip freeze.",
        ("Rueda demo_pkg 1.0.0", "instalada con --no-index --no-deps desde un archivo local", "navy"),
        [("Intérprete global: import falla", "el paquete no está instalado allí", "coral"),
         ("Entorno: import → 1.0.0", "pip list: 2 paquetes, pip y demo-pkg; nada más", "teal"),
         ("Dos entornos nuevos: pip freeze idéntico", "la misma rueda produce el mismo estado", "teal")],
        note='Se instaló una rueda construida localmente, sin red. La reproducibilidad del entorno depende de poder instalar los mismos archivos exactos, no de la versión escrita en un archivo de requisitos.', note_kind='gold', foot=S)


# ---------------------------------------------------------------- SE-104
def se104_estado() -> Fig:
    return grouped_bars(
        'Qué se midió con el motor en marcha',
        "Barras horizontales con los tiempos medidos con el motor de Docker 29.9.2 en marcha: docker info 1 327 ms, primera construcción de la imagen desde scratch 4 325 ms, segunda 1 221 ms, docker create 314 ms y docker cp 373 ms; la ejecución de un proceso no se midió.",
        ["docker info", "Construcción de la imagen, 1.ª vez", "Construcción de la imagen, 2.ª vez", "docker create", "docker cp"],
        [("Tiempo", [1327, 4325, 1221, 314, 373], "teal")],
        unit="Tiempo medido (ms)", horizontal=True, label_w=270,
        note='Todo se hizo sin red: la imagen parte de `scratch` y no hay proceso que ejecutar. El arranque de un contenedor con un sistema base real queda sin medir, y se declara como límite.', note_kind='gold', foot="Medido con Docker 29.9.2 sobre Windows 11 (motor Linux, 8 CPU).")


def se104_config() -> Fig:
    return merge(
        'Anatomía de un dev container',
        "Diagrama de las cuatro claves de un devcontainer.json de ejemplo que definen el contenedor de desarrollo: image fija la imagen base, features añade piezas instalables, postCreateCommand instala dependencias después de crear y customizations deja la extensión de ruff en la configuración.",
        [("image", "imagen base: una etiqueta cambia, un digest fija el contenido", "gold"),
         ("features", "piezas instalables: añaden herramientas sin editar la imagen", "plain"),
         ("postCreateCommand: pip install -r requirements.txt", "se ejecuta después de crear el contenedor, con red", "plain"),
         ("customizations", "extensiones del editor: la de ruff queda en la configuración", "plain")],
        ("Contenedor de desarrollo", "el entorno declarado como código", "teal"),
        note='Un dev container declara el entorno como código. La garantía depende de lo que se fije: una etiqueta de imagen puede apuntar a otro contenido mañana; un digest no.', note_kind='gold', foot="Estructura de una configuración de ejemplo; no se ejecutó.")


def se104_desechable() -> Fig:
    return nested(
        'Niveles de aislamiento',
        "Niveles de aislamiento anidados: el entorno virtual aísla paquetes y se crea en 180 a 278 ms; el contenedor aísla además el sistema de archivos y las herramientas y crearlo tomó 314 ms; la máquina virtual aísla el kernel y su costo no se midió.",
        [("Máquina virtual", "aísla el kernel; más pesada · costo no medido", "grey", True),
         ("Contenedor", "aísla también el sistema de archivos y las herramientas · crear: 314 ms", "gold", False),
         ("Entorno virtual", "aísla paquetes; comparte intérprete y sistema · 180 a 278 ms", "teal", False)],
        note='Más aislamiento no es mejor por defecto: cuesta tiempo y recursos. Se elige el nivel que cubre el riesgo (dependencias, herramientas o sistema operativo) y se declara el resto.', note_kind='gold', foot="El costo de la máquina virtual no se midió; 314 ms es crear, no arrancar, un contenedor.")


# ---------------------------------------------------------------- SE-105
def se105_ddmin() -> Fig:
    return chain(
        'Reducir un caso hasta lo esencial',
        "Cadena de una reducción automática: una entrada de 403 caracteres que falla se reduce con 24 pruebas al caso mínimo de 3 caracteres (ab y un corchete abierto), una reducción del 99,3 por ciento; probar un carácter cada vez habría exigido 403 pruebas.",
        [("Entrada que falla", "403 caracteres: contiene un «[» sin cerrar tras «ab»", "coral"),
         ("Caso mínimo", "ab[ (3 caracteres): reducción del 99,3 %", "teal")],
        labels=["24 pruebas"], note='La reducción no entiende el defecto: solo elimina trozos mientras el fallo persista. Funciona si la prueba es determinista; con una prueba intermitente puede quedarse con un caso que no es mínimo.', note_kind='gold', foot=S)


def se105_bisect() -> Fig:
    return timeline(
        'Buscar el cambio culpable',
        "Línea de tiempo de una historia de 64 commits: la prueba pasa hasta el commit 40 y falla desde el 41, donde se introdujo el defecto a propósito; git bisect run señala el commit 41 en 6 pasos porque cada paso descarta la mitad.",
        [("Historia de 64 commits", [(0, 40, "la prueba pasa", "teal"), (40, 64, "la prueba falla", "coral")])],
        unit="Commit (1 a 64)", events=[(40, "c41: primer commit que falla · 6 pasos"),], ticks=[0, 16, 32, 40, 48, 64], t_max=64, lane_h=62, label_w=200,
        note='La bisección da el primer commit en que falla la prueba, no la causa. Asume que antes funcionaba y después falla siempre; un defecto intermitente o dos defectos distintos la engañan.', note_kind='gold', foot=S)


def se105_pasos() -> Fig:
    items = [("Eliminar un carácter cada vez", 403, "coral", "403 pruebas"), ("ddmin (reducción por trozos)", 24, "teal", "24 pruebas"), ("Bisección de 64 commits", 6, "teal", "6 pruebas")]
    return bars("Cuántas pruebas necesita cada estrategia", "Barras con las pruebas necesarias: 403 eliminando un carácter cada vez, 24 con ddmin y 6 para bisecar 64 commits.",
                items, 1.3, "Elegir la estrategia cambia el costo en órdenes de magnitud. El conteo de pruebas es reproducible; el tiempo de cada prueba depende de lo que se ejecute.", label_w=290, foot=S)


# ---------------------------------------------------------------- SE-106
def se106_contraste() -> Fig:
    return grouped_bars(
        'Contraste calculado con la fórmula de WCAG',
        "Barras horizontales con la razón de contraste WCAG de cinco combinaciones: negro sobre blanco 21,00, gris 767676 4,54 que cumple AA, gris 777777 4,48 que queda bajo el umbral de 4,5, verde 00aa00 3,11 y azul sobre fondo oscuro 1,94.",
        ["Azul #0000ff sobre #1e1e1e", "Verde #00aa00 sobre blanco", "Gris #777777 sobre blanco", "Gris #767676 sobre blanco", "Negro sobre blanco"],
        [("Razón de contraste", [1.94, 3.11, 4.48, 4.54, 21.00], "navy")],
        unit="Razón de contraste (WCAG)", horizontal=True, label_w=250, decimals=2, ref_lines=[(4.5, "AA: 4,5")],
        note='Una diferencia imperceptible en el color (#767676 frente a #777777) cruza el umbral de 4,5. El contraste se calcula, no se juzga a ojo, y vale para el texto normal; el grande admite 3.', note_kind='gold', foot="Calculado con la fórmula de luminancia relativa de WCAG 2.2.")


def se106_tema() -> Fig:
    return grouped_bars(
        'Temas del editor y accesibilidad',
        "Barras horizontales con la razón de contraste de colores de comentarios en temas del editor: 5,00 en el tema oscuro, 5,14 en el claro y 5,25 el rojo sobre negro, los tres sobre el umbral AA de 4,5.",
        ["Comentario #6a9955 sobre #1e1e1e (oscuro)", "Comentario #008000 sobre blanco (claro)", "Rojo #ff0000 sobre negro"],
        [("Razón de contraste", [5.00, 5.14, 5.25], "teal")],
        unit="Razón de contraste (WCAG)", horizontal=True, label_w=270, decimals=2, ref_lines=[(4.5, "AA: 4,5")],
        note='Cumplir el contraste no basta: el color no debe ser el único modo de distinguir un error. El editor debe ofrecer también un símbolo o un texto.', note_kind='gold', foot="Calculado con la fórmula de luminancia relativa de WCAG 2.2.")


def se106_latencia() -> Fig:
    items = [("Actualización de diagnósticos (didChange)", 5, "teal", "5 ms"), ("Primer análisis (didOpen)", 351, "gold", "351 ms"), ("Reanalizar 60 000 líneas con ast.parse", 432, "coral", "432 ms")]
    return bars("Presupuesto de latencia de una herramienta interactiva", "Barras con tres latencias medidas: 5 ms para actualizar diagnósticos, 351 ms para el primer análisis y 432 ms para reanalizar 60 000 líneas.",
                items, 0.9, "La herramienta debe responder dentro del ritmo de la persona. Con 5 ms la ayuda es continua; con 351 ms es perceptible; con 432 ms por pulsación, inutilizable. Una herramienta lenta se vuelve una herramienta que se desactiva.", label_w=330, foot=M)


# ---------------------------------------------------------------- SE-107
def se107_flujo() -> Fig:
    return chain(
        'Diagnosticar un fallo desconocido: la secuencia',
        "Cadena de cinco pasos de diagnóstico con su dato medido: reproducir con una prueba determinista, reducir de 403 a 3 caracteres en 24 pruebas, localizar el commit en 6 pasos para 64, observar con pdb que b vale 10 y a vale 5, y verificar con una prueba nueva.",
        [("1. Reproducir", "prueba determinista que falla", "navy"), ("2. Reducir", "403 → 3 caracteres en 24 pruebas", "navy"),
         ("3. Localizar", "6 pasos para 64 commits", "navy"), ("4. Observar", "pdb: b = 10 y a = 5 en la línea 3", "navy"),
         ("5. Verificar", "nueva prueba: falla antes y pasa después", "teal")],
        note='Cada paso reduce el espacio de búsqueda y deja un registro. El orden no es rígido, pero saltarse la reproducción deja el resto sin base.', note_kind='gold', foot=S)


def se107_hipotesis() -> Fig:
    return fan(
        'Registro de hipótesis',
        "Diagrama de tres hipótesis ante un fallo: el analizador y el commit 41 se confirman con la reducción a un caso mínimo y con la bisección que señala c41; que dependa del estado de b se descarta porque pdb muestra b igual a 10, el valor esperado.",
        ("Fallo observado", "tres hipótesis con su prueba", "navy"),
        [("H1: el defecto está en el analizador", "se reduce a ab[: el caso mínimo lo fuerza → confirmada", "teal"),
         ("H2: lo introdujo el commit 41", "bisect señala c41 y la prueba automática lo confirma → confirmada", "teal"),
         ("H3: depende del estado de b", "pdb muestra b = 10, el valor esperado → descartada", "coral", True)],
        note='Descartar es información. Una hipótesis descartada con su prueba evita volver a investigarla y muestra qué se comprobó.', note_kind='gold', foot=S)


def se107_limites() -> Fig:
    f, y = _kit_start('Cada técnica tiene su condición',
                      "Diagrama de la condición de cada técnica de diagnóstico: la reducción funciona con pruebas deterministas y falla con fallos intermitentes; la bisección funciona con un solo cambio culpable y la confunden dos defectos; el depurador muestra el estado en un instante pero perturba los tiempos hasta 9,7 veces.",
                      940, None)
    rows = [("Reducción", "funciona con pruebas deterministas", "falla con fallos intermitentes"),
            ("Bisección", "funciona con un solo cambio culpable", "dos defectos o interacciones la confunden"),
            ("Depurador", "muestra el estado en un instante", "perturba tiempos (hasta 9,7× de costo)")]
    for i, (name, ok, bad) in enumerate(rows):
        ry = y + 6 + i * 84
        card(f, 14, ry, 170, 72, name, "", "navy")
        f.arrow([(184, ry + 36), (246, ry + 36)], "", color="#32505f")
        card(f, 246, ry, 330, 72, "Cuándo funciona", ok, "teal")
        f.arrow([(576, ry + 36), (626, ry + 36)], "", color="#c0432f", dashed=True)
        card(f, 626, ry, 300, 72, "Cuándo falla", bad, "coral", True)
    out = _kit_finish(f, y + 6 + 3 * 84 - 4, 'Elegir mal la técnica produce conclusiones falsas con aspecto de evidencia. Antes de aplicarla se comprueba su condición.', 'gold', S)
    out.kind = "diagram"
    return out


# ---------------------------------------------------------------- SE-108
def se108_inventario() -> Fig:
    return chain(
        'Inventario de un entorno autocontenido',
        "Cadena de cuatro elementos de un entorno autocontenido: intérprete CPython 3.12.9 en Windows y 3.12.3 en Linux, entorno virtual de 7 archivos sin pip y 860 con pip, una rueda local como dependencia y pip freeze idéntico en dos entornos como verificación.",
        [("Intérprete", "CPython 3.12.9 (Windows) · 3.12.3 (Linux): se fija con la versión exacta", "navy"),
         ("Entorno virtual", "7 archivos sin pip · 860 con pip: se crea desde cero con un comando", "navy"),
         ("Dependencias", "una rueda local: se instala con --no-index --no-deps", "navy"),
         ("Verificación", "pip freeze idéntico en dos entornos: se compara el estado", "teal")],
        note='Un entorno autocontenido es el que se puede reconstruir desde el repositorio y comprobar. Cada pieza debe tener su comprobación; lo que solo se asume queda como riesgo.', note_kind='gold', foot=S)


def se108_hash() -> Fig:
    f, y = _kit_start('Reproducir el entorno no es reproducir los bytes',
                      "Diagrama de dos construcciones de la misma rueda con el mismo código: la primera da el hash b384a5f15d7d y la segunda 762d3c781a63, distintos porque las marcas de tiempo entran en la rueda; instalar la misma rueda en dos entornos da el mismo pip freeze.",
                      940, None)
    card(f, 14, y + 20, 220, 60, "Mismo código", "sin cambios", "navy")
    card(f, 330, y + 4, 596, 44, "Primera construcción: b384a5f15d7d", "", "coral")
    card(f, 330, y + 56, 596, 44, "Segunda construcción: 762d3c781a63", "", "coral")
    f.arrow([(234, y + 50), (282, y + 50), (282, y + 26), (330, y + 26)])
    f.arrow([(234, y + 50), (282, y + 50), (282, y + 78), (330, y + 78)])
    f.text(628, y + 118, "SHA-256 abreviado: distintos aunque el código no cambió", 13, "middle", 400, "#5c1f14")
    card(f, 14, y + 150, 220, 60, "Misma rueda", "instalada en dos entornos", "navy")
    card(f, 330, y + 150, 596, 60, "pip freeze idéntico", "instalar la misma rueda reproduce el estado", "teal")
    f.arrow([(234, y + 180), (330, y + 180)])
    out = _kit_finish(f, y + 226, 'Dos construcciones del mismo código dieron archivos distintos (las marcas de tiempo entran en la rueda). Por eso se fija el archivo que se instala por su hash, y no se reconstruye en cada entorno.', 'gold', S)
    out.kind = "diagram"
    return out


def se108_aceptacion() -> Fig:
    return merge(
        'Criterios de aceptación del proyecto',
        "Diagrama de cuatro criterios que deben cumplirse para aceptar el proyecto: reconstruir el entorno desde cero con un comando, aislamiento comprobado, versiones fijadas por hash y límites declarados como el arranque en contenedor no medido.",
        [("Reconstruir el entorno desde cero", "un comando; sin pasos manuales ni conocimiento oral", "plain"),
         ("Aislamiento comprobado", "import demo_pkg falla fuera y devuelve 1.0.0 dentro", "plain"),
         ("Versiones fijadas", "intérprete y rueda por hash; no se aceptan etiquetas flotantes", "plain"),
         ("Límites declarados", "arranque en contenedor no medido: no se descargó ninguna imagen base", "plain")],
        ("Proyecto aceptado", "por lo que se puede comprobar", "teal"),
        note='El proyecto se acepta por lo que se puede comprobar, incluidos los límites declarados. Un entorno que «funciona en mi máquina» no cumple ninguno de los cuatro.', note_kind='gold', foot=S)


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
