"""Figures for SE-109 to SE-114 (values measured with CPython 3.12.9 on Windows 11; Linux 3.12.3 under WSL2 where noted)."""
from __future__ import annotations

from figure_kit import Fig, _wrap

MEDIDO = "Medido con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2; los tiempos dependen del equipo y se leen como razones."


def tab(title: str, desc: str, heads: list[str], rows: list[list[str]], widths: list[float], note: str = "",
        note_kind: str = "gold", row_h: float = 52, size: int = 12, kinds=None, foot: str = MEDIDO) -> Fig:
    """Table figure with an optional note box; checks that every cell fits its box."""
    for row in rows:
        for width, cell in zip(widths, row):
            lines = _wrap(cell, size, width - 6 - 20)
            assert len(lines) * size * 1.28 <= row_h - 6, f"cell overflows in {title!r}: {cell!r}"
    for width, head in zip(widths, heads):
        assert len(_wrap(head, size + 1, width - 6 - 20)) * (size + 1) * 1.28 <= 38, f"header overflows in {title!r}: {head!r}"
    width_total = int(sum(widths)) + 20
    y_end = 12 + 38 + 6 + len(rows) * (row_h + 6)
    note_lines = len(_wrap(note, 13, width_total - 40)) if note else 0
    note_h = max(54, note_lines * 13 * 1.28 + 26) if note else 0
    height = int(y_end + (note_h + 12 if note else 0) + (28 if foot else 8))
    f = Fig(width_total, height, title, desc)
    f.table(heads, rows, 10, 12, widths, row_h=row_h, size=size, kinds=kinds)
    y = y_end
    if note:
        f.box(10, y + 4, width_total - 20, note_h, note, note_kind, 13)
        y += note_h + 12
    if foot:
        f.text(width_total / 2, y + 14, foot, 12, "middle", 400, "#5c1f14")
    return f


def bars(title: str, desc: str, items, scale: float, note: str = "", label_w: float = 250, width: int = 940,
         note_kind: str = "gold", foot: str = MEDIDO) -> Fig:
    note_lines = len(_wrap(note, 13, width - 40)) if note else 0
    note_h = max(54, note_lines * 13 * 1.28 + 26) if note else 0
    y_end = 16 + len(items) * 44
    height = int(y_end + (note_h + 12 if note else 0) + (28 if foot else 8))
    f = Fig(width, height, title, desc)
    f.hbars(items, 10, 16, scale, label_w=label_w, bar_h=28, step=44)
    y = y_end
    if note:
        f.box(10, y + 4, width - 20, note_h, note, note_kind, 13)
        y += note_h + 12
    if foot:
        f.text(width / 2, y + 14, foot, 12, "middle", 400, "#5c1f14")
    return f


# ---------------------------------------------------------------- SE-109
def se109_pila() -> Fig:
    f = Fig(940, 420, "Quién llama a quién: biblioteca frente a framework",
            "Dos pilas de llamadas medidas con traceback.extract_stack. En la biblioteca la pila es módulo, main_library, lib_func, user_cb: el consumidor llama a la biblioteca y esta le devuelve el control. En el framework la pila es módulo, main_fw, run, handler: el consumidor entrega el control a run, que decide cuántas veces y en qué orden llama a sus handlers.")
    f.box(10, 14, 440, 40, "Biblioteca: el consumidor conserva el flujo", "teal", 14, bold=True)
    f.box(480, 14, 440, 40, "Framework: el framework posee el flujo", "coral", 14, bold=True)
    for i, (a, b) in enumerate((("<module>", "<module>"), ("main_library()  (código del consumidor)", "main_fw()  (código del consumidor)"),
                                ("lib_func(cb)  (biblioteca)", "Framework.run()  (framework)"), ("user_cb(3)  (callback del consumidor)", "handler()  (registrado con @fw.route)"))):
        y = 70 + i * 54
        f.box(10, y, 440, 44, a, "plain", 13)
        f.box(480, y, 440, 44, b, "plain", 13)
        if i:
            f.arrow([(230, y - 10), (230, y)])
            f.arrow([(700, y - 10), (700, y)])
    f.box(10, 296, 440, 70, "Al terminar lib_func, el control vuelve a main_library. El consumidor decide si llama de nuevo, cuándo y con qué.", "teal", 13)
    f.box(480, 296, 440, 70, "run() recorre los handlers registrados. El consumidor registró; ya no decide el orden ni la cantidad de llamadas.", "coral", 13)
    f.text(470, 392, "Pila idéntica en Windows (3.12.9) y Linux (3.12.3); lo que cambia es quién ocupa el fondo de la pila.", 12, "middle", 400, "#5c1f14")
    return f


def se109_importar() -> Fig:
    rows = [["json", "24 / 33,6 ms", "24 / 18,8 ms", "Casi nada que cargar"],
            ["argparse", "29 / 36,6 ms", "28 / 22,6 ms", "Construye la CLI sin red ni disco"],
            ["logging", "42 / 53,5 ms", "41 / 31,1 ms", "Arrastra threading, traceback, string"],
            ["http.server", "91 / 263,7 ms", "90 / 68,9 ms", "Carga http, socketserver, email..."],
            ["unittest", "67 / 265,6 ms", "65 / 54,4 ms", "Descubrimiento, aserciones, señales"],
            ["asyncio", "126 / 303,3 ms", "111 / 92,8 ms", "Un runtime dentro de la biblioteca estándar"]]
    return tab("Costo de importar: módulos nuevos y tiempo, en un intérprete limpio",
               "Tabla con módulos nuevos cargados y milisegundos de import en un intérprete limpio con la opción -S: json carga 24 módulos en 33,6 ms en Windows y 18,8 en Linux; asyncio carga 126 y 111 módulos en 303,3 y 92,8 ms. Un intérprete limpio parte con 25 módulos en Windows y 23 en Linux.",
               ["Import", "Windows: módulos / mejor de 3", "Linux: módulos / mejor de 3", "Qué se arrastra"], rows, [150, 250, 250, 280], row_h=46,
               note="Importar asyncio costó 9,0 veces lo de json en Windows y 4,9 en Linux. Una biblioteca que importa un runtime completo en su __init__ lo cobra a cada consumidor, lo use o no. Además, un módulo con open() en el momento de importar produjo un evento de auditoría de apertura más que uno sin efectos (3 frente a 2 en Windows, 5 frente a 4 en Linux).", note_kind="gold")


def se109_timeout() -> Fig:
    rows = [["urlopen(url) sin timeout, servidor local que responde en 2 s", "Espera 2,00 s y devuelve", "Espera 2,00 s y devuelve"],
            ["urlopen(url, timeout=0.3) contra el mismo servidor", "TimeoutError tras 0,47 s", "TimeoutError tras 0,37 s"],
            ["socket.getdefaulttimeout()", "None (sin límite)", "None (sin límite)"]]
    return tab("Un SDK que oculta el timeout oculta también el peor caso", "Tabla con un servidor local en el bucle de retorno que tarda 2 segundos: sin timeout la llamada espera 2,00 segundos; con timeout de 0,3 segundos lanza TimeoutError tras 0,47 segundos en Windows y 0,37 en Linux; el timeout por defecto de los sockets es None.",
               ["Llamada", "Windows", "Linux (WSL2)"], rows, [430, 260, 260], row_h=56,
               note="El valor por defecto de la biblioteca estándar es «esperar sin límite». Un SDK que envuelve la llamada sin exponer timeout hereda ese peor caso: con un servidor que nunca contestara, la espera no terminaría (no se midió; se deduce del valor None). El SDK debe fijar un timeout razonable y dejar que el consumidor lo cambie.", note_kind="coral")


# ---------------------------------------------------------------- SE-110
def se110_versiones() -> Fig:
    rows = [["1.0.0-rc.1 frente a 1.0.0", "Se normaliza a 1.0.0rc1; 1.0.0rc1 < 1.0.0", "SemVer escribe el guion; PEP 440 lo reescribe"],
            ["1.0 frente a 1.0.0", "Iguales", "Los ceros finales no cuentan"],
            ["1.0.post1 frente a 1.0.0", "1.0.post1 > 1.0.0", "SemVer no define post-releases"],
            ["1.0.0a10 frente a 1.0.0a2", "a10 > a2", "Compara como números, no como texto"],
            ["1.0.0+build5 frente a 1.0.0", "1.0.0+build5 > 1.0.0", "SemVer ignora «+metadata» al ordenar; PEP 440 no"],
            ["1.0.0-alpha.beta y 1.0.0.x", "InvalidVersion", "No todo SemVer válido es PEP 440 válido"],
            ["1.0.0-01", "Se interpreta como 1.0.0.post1", "Un guion puede significar post-release"]]
    return tab("Cómo ordena Python las versiones: PEP 440 frente a SemVer", "Tabla con siete comparaciones hechas con la biblioteca packaging: 1.0.0-rc.1 se normaliza a 1.0.0rc1 y es menor que 1.0.0; 1.0 es igual a 1.0.0; 1.0.post1 es mayor que 1.0.0; a10 es mayor que a2; 1.0.0+build5 es mayor que 1.0.0; 1.0.0-alpha.beta es inválida; 1.0.0-01 se lee como post-release.",
               ["Comparación", "Resultado con packaging 26.2", "Diferencia con SemVer 2.0.0"], rows, [290, 330, 330], row_h=46,
               note="Además, ordenar los textos 1.10.0, 1.2.0 y 1.9.0 como cadenas da 1.10.0, 1.2.0, 1.9.0; ordenarlos como versiones da 1.2.0, 1.9.0, 1.10.0. Si un SDK expone versiones, debe declarar qué esquema usa.", note_kind="gold", foot="Medido con CPython 3.12.9 y packaging 26.2 en Windows 11; las comparaciones no dependen del sistema operativo.")


def se110_firmas() -> Fig:
    rows = [["Añadir parámetro opcional con nombre", "ok", "ok", "ok", "ok", "igual"],
            ["Añadir parámetro obligatorio", "TypeError", "TypeError", "TypeError", "TypeError", "TypeError"],
            ["Renombrar b a second", "ok", "TypeError", "TypeError", "ok", "igual"],
            ["Reordenar a, b a b, a", "ok", "TypeError", "ok", "ok", "distinto"],
            ["Quitar el parámetro timeout", "ok", "ok", "TypeError", "TypeError", "igual"],
            ["Cambiar el valor por defecto de timeout", "ok", "ok", "ok", "ok", "distinto"],
            ["Hacer b solo por nombre", "TypeError", "ok", "ok", "TypeError", "TypeError"],
            ["Hacer a solo posicional", "ok", "ok", "TypeError", "ok", "igual"]]
    return tab("Ocho cambios de firma frente a cinco formas de llamar", "Matriz de ocho cambios sobre la función f(a, b, *, timeout=10) frente a cinco llamadas: añadir un parámetro opcional no rompe ninguna; añadir uno obligatorio rompe todas; renombrar b rompe la llamada por nombre; reordenar cambia el resultado sin error; cambiar el valor por defecto cambia el resultado sin error.",
               ["Cambio sobre f(a, b, *, timeout=10)", "f(1, 2)", "f(1, b=2)", "f(a=1, b=2, timeout=5)", "f(1, 2, timeout=3)", "Resultado de f(1, 2)"], rows, [290, 110, 110, 170, 140, 130], row_h=38, size=12,
               note="Dos de los ocho cambios (reordenar y cambiar el valor por defecto) no producen ningún error y cambian el resultado: son los que una revisión de firmas no detecta y una prueba de contrato sí.", note_kind="coral", foot="Medido con CPython 3.12.9; ok = la llamada funciona y devuelve lo esperado; resultado distinto = devuelve otro valor sin error.")


def se110_contrato() -> Fig:
    f = Fig(940, 410, "Misma firma, otro contrato: lo que SemVer no puede ver",
            "Dos pares de funciones con la firma idéntica según inspect.signature. get_ids v1 devuelve las claves en orden de inserción, b y a; v2 las devuelve ordenadas, a y b. parse v1 lanza ValueError con el texto empty input y v2 con el texto input is empty; un consumidor que comparaba el texto exacto deja de reconocer el error.")
    f.box(10, 14, 440, 40, "Orden del resultado", "navy", 14, bold=True)
    f.box(480, 14, 440, 40, "Texto del error", "navy", 14, bold=True)
    f.box(10, 70, 210, 80, "v1: get_ids({'b':1,'a':2})\n→ ['b', 'a']", "teal", 13)
    f.box(240, 70, 210, 80, "v2: sorted(d)\n→ ['a', 'b']", "coral", 13)
    f.box(480, 70, 210, 80, "v1: ValueError\n«empty input»", "teal", 13)
    f.box(710, 70, 210, 80, "v2: ValueError\n«input is empty»", "coral", 13)
    f.box(10, 170, 440, 60, "inspect.signature(v1) == inspect.signature(v2) → True", "gold", 13)
    f.box(480, 170, 440, 60, "El consumidor que hacía  str(e) == 'empty input'  pasa de True a False", "gold", 13)
    f.box(10, 250, 910, 70, "Las dos versiones podrían publicarse como parche y ninguna herramienta que compare firmas lo notaría. La compatibilidad es una propiedad del comportamiento que los consumidores usan, y la única forma de vigilarlo es con pruebas de contrato escritas desde su punto de vista (ley de Hyrum).", "grey", 13)
    f.text(470, 346, "Medido con CPython 3.12.9 en Windows 11; sin dependencia del sistema operativo.", 12, "middle", 400, "#5c1f14")
    f.text(470, 372, "Hyrum's Law: con suficientes usuarios, cualquier comportamiento observable será usado por alguien.", 12, "middle", 400, "#2b3a44", italic=True)
    return f


# ---------------------------------------------------------------- SE-111
def se111_resolutor() -> Fig:
    rows = [["Elegir siempre la versión más nueva y no retroceder", "Sin solución", "6 candidatos evaluados, 3 retrocesos: libA 2.0 exige core ≥ 2 y libB exige core < 2"],
            ["Elegir la más nueva y retroceder ante el conflicto", "app 1.0, libA 1.0, libB 2.0, core 1.0", "15 candidatos evaluados, 3 retrocesos: baja libA hasta que core < 2 sirve a ambos"],
            ["Índice sin ninguna combinación válida", "Sin solución", "6 candidatos evaluados, 3 retrocesos: el resolutor termina y lo declara"],
            ["Orden de instalación del resultado (graphlib)", "core, libA, libB, app", "Las dependencias antes que quien las usa"],
            ["Dependencia circular app → core → libA → app", "CycleError", "Camino: app, core, libA, app"]]
    return tab("Resolver dependencias es buscar, y a veces no hay solución", "Tabla de cinco casos de un resolutor de juguete sobre un índice de cuatro paquetes: sin retroceso no hay solución; con retroceso se encuentra libA 1.0, libB 2.0, core 1.0 tras evaluar 15 candidatos; un índice sin combinación válida termina sin solución; graphlib ordena core, libA, libB, app y detecta el ciclo app, core, libA, app.",
               ["Estrategia o caso", "Resultado", "Lectura"], rows, [330, 270, 350], row_h=62,
               note="El conflicto es real: libA 2.0 pide core ≥ 2 y libB pide core < 2. La versión más nueva de cada paquete no es una solución; la solución es un conjunto compatible. Los conteos son del resolutor de juguete, no de pip.", note_kind="gold", foot="Cuentas deterministas, idénticas en Windows (3.12.9) y Linux (3.12.3).")


def se111_pip() -> Fig:
    rows = [["pip install libaX", "coreX 3.0 y libaX 2.0", "Elige lo más nuevo que cumple"],
            ["pip install libbX (pide coreX < 2)", "coreX 1.0 y libbX 1.0", "La restricción excluye 2.0 y 3.0"],
            ["pip install libaX libbX", "libaX 1.0, coreX 1.0 y libbX 1.0", "Retrocede a libaX 1.0 para que ambos convivan"],
            ["pip install libbX «coreX>=3»", "ResolutionImpossible, salida 1", "Las dos peticiones se contradicen: pip lo dice y no instala nada"],
            ["libaX tras publicarse coreX 3.1", "coreX 3.1 y libaX 2.0", "Sin fijar, la misma orden instala otra cosa"]]
    return tab("pip resuelve sobre un directorio de ruedas locales", "Tabla de cinco órdenes de pip install con la opción dry-run sobre ruedas locales sin índice: libaX instala coreX 3.0 y libaX 2.0; libbX instala coreX 1.0; ambos juntos retroceden a libaX 1.0 y coreX 1.0; libbX con coreX mayor o igual que 3 falla con ResolutionImpossible; tras publicar coreX 3.1 la misma orden elige 3.1.",
               ["Orden", "Qué habría instalado", "Lectura"], rows, [330, 300, 320], row_h=56,
               note="Mismo resultado en Windows (pip 24.3.1) y Linux (pip 24.0). En Linux fue necesario aceptar el modo «gestionado externamente» de PEP 668 porque se usó el intérprete del sistema con la opción dry-run, sin instalar nada.", note_kind="teal")


def se111_hashes() -> Fig:
    rows = [["Requisito fijado con == y el hash correcto", "Salida 0: «Would install coreX-3.0»", "Se acepta el artefacto exacto"],
            ["La misma rueda con un byte alterado", "Salida 1: «THESE PACKAGES DO NOT MATCH THE HASHES»", "Muestra Expected y Got con dos SHA-256 distintos"],
            ["Requisito sin versión fijada (coreX)", "Salida 1: «all requirements must have their versions pinned with ==»", "El modo con hashes exige fijar todo"],
            ["Sin fijar y con una versión nueva en el índice", "Instala coreX 3.1", "La reproducibilidad no está en la orden sino en el archivo de fijación"]]
    return tab("Un lockfile con hashes: aceptar el artefacto, no el nombre", "Tabla de cuatro casos de pip con la opción require-hashes: la versión fijada con el hash correcto se acepta; la misma rueda con un byte alterado se rechaza con salida 1 y los dos SHA-256; un requisito sin versión fijada se rechaza; sin fijar y con una versión nueva en el índice se instala la nueva.",
               ["Caso", "Resultado", "Lectura"], rows, [310, 340, 300], row_h=62,
               note="El hash vincula la instalación a unos bytes concretos, no a un nombre y una versión. No prueba que esos bytes sean seguros: solo que son los mismos que alguien revisó. Resultados idénticos en Windows y Linux.", note_kind="gold")


# ---------------------------------------------------------------- SE-112
def se112_instalado() -> Fig:
    rows = [["Sin package-data", "__init__.py, sub/mod.py, METADATA", "1 353 B / 1 351 B", "{'v': 1}", "FileNotFoundError"],
            ["Con package-data = data/*.json", "__init__.py, data/rules.json, sub/mod.py, METADATA", "1 536 B / 1 533 B", "{'v': 1}", "{'v': 1}"]]
    return tab("Funciona en el repositorio, falla instalado: el archivo de datos que no viajó", "Tabla con dos ruedas del mismo proyecto: sin package-data la rueda mide 1353 bytes en Windows y 1351 en Linux, no contiene data/rules.json, y load_rules funciona desde el árbol de fuentes pero lanza FileNotFoundError una vez instalada; con package-data la rueda incluye el archivo y funciona en ambos lugares.",
               ["Configuración", "Contenido de la rueda", "Tamaño Windows / Linux", "Desde el árbol de fuentes", "Tras instalar la rueda"], rows, [190, 260, 170, 160, 170], row_h=70,
               note="El código no cambió entre las dos filas: cambió qué archivos empaquetó el constructor. Las pruebas que se ejecutan desde el repositorio no pueden verlo; solo una instalación limpia lo muestra. El paquete sub/ no tiene __init__.py y aun así se empaquetó, porque la configuración de pyproject.toml permite paquetes de espacio de nombres por defecto.", note_kind="coral")


def se112_sombras() -> Fig:
    rows = [["python main.py con un json.py local junto a main.py", "json.py local; json.dumps({}) devuelve «FAKE»", "Un archivo propio tapa a la biblioteca estándar"],
            ["El mismo programa con python -I", "__init__.py de la biblioteca estándar; json.dumps({}) devuelve «{}»", "El modo aislado quita el directorio del script y del usuario de sys.path"],
            ["python -c «import random» en un directorio con random.py", "Ejecuta el random.py local", "Con -c, el directorio actual va primero en sys.path"],
            ["python -m json.tool con un json.py local", "Error: no se puede encontrar json.tool", "El json.py local se encontró antes y no es un paquete"],
            ["import capkit.sub.mod sin sub/__init__.py", "Funciona; sub.__file__ es None y __path__ es un _NamespacePath", "Paquete de espacio de nombres: sin __init__.py"]]
    return tab("Quién gana en sys.path: sombras y paquetes de espacio de nombres", "Tabla de cinco comprobaciones: un json.py local tapa a la biblioteca estándar y json.dumps devuelve FAKE; con la opción -I se importa la estándar; random.py local se ejecuta con python -c; python -m json.tool falla; un directorio sin __init__.py se importa como paquete de espacio de nombres con __file__ None.",
               ["Comprobación", "Resultado", "Causa"], rows, [310, 340, 300], row_h=70,
               note="Mismo resultado en Windows y Linux. Nombrar un módulo como uno de la biblioteca estándar (json, random, email, test) rompe programas ajenos al proyecto sin dar un error de nombre; el fallo aparece lejos del archivo mal nombrado.", note_kind="coral")


def se112_etiquetas() -> Fig:
    rows = [["Cantidad de etiquetas aceptadas", "42", "1 067"],
            ["Primera (la más específica)", "cp312-cp312-win_amd64", "cp312-cp312-manylinux_2_39_x86_64"],
            ["Última (la menos específica)", "py30-none-any", "py30-none-any"],
            ["Rueda de Python puro construida en el experimento", "capkit-1.0.0-py3-none-any.whl", "capkit-1.0.0-py3-none-any.whl"]]
    return tab("Etiquetas de compatibilidad: qué ruedas acepta cada intérprete", "Tabla con las etiquetas de rueda que acepta el intérprete: 42 en Windows con la primera cp312-cp312-win_amd64, y 1067 en Linux con la primera cp312-cp312-manylinux_2_39_x86_64; en ambos la última es py30-none-any y la rueda de Python puro se llama py3-none-any.",
               ["Dato", "Windows (3.12.9)", "Linux bajo WSL2 (3.12.3)"], rows, [330, 300, 320], row_h=50,
               note="Una rueda py3-none-any sirve en las dos plataformas; una rueda con extensión compilada necesita una etiqueta de la lista. Linux acepta tantas etiquetas porque cuenta cada versión de la biblioteca C compatible (manylinux_2_39 hacia abajo). Una rueda con etiqueta win_amd64 no se instala en Linux ni a la inversa.", note_kind="teal")


# ---------------------------------------------------------------- SE-113
def se113_salida() -> Fig:
    rows = [["Terminar sin error", "0", "0"], ["sys.exit(3)", "3", "3"], ["sys.exit('mensaje')", "1 (y el mensaje va a stderr)", "1 (y el mensaje va a stderr)"],
            ["Excepción sin capturar", "1", "1"], ["argparse: opción desconocida", "2", "2"], ["argparse: --help", "0", "0"],
            ["Ctrl+C sin capturar (KeyboardInterrupt)", "3221225786 (0xC000013A)", "−2 (terminado por SIGINT)"],
            ["sys.exit(256)", "256", "0"], ["sys.exit(-1)", "4294967295", "255"]]
    return tab("Códigos de salida observados con subprocess", "Tabla de nueve escenarios: terminar sin error da 0; sys.exit(3) da 3; sys.exit con texto da 1; una excepción da 1; argparse con una opción desconocida da 2 y con --help da 0; Ctrl+C da 3221225786 en Windows y menos 2 en Linux; sys.exit(256) da 256 en Windows y 0 en Linux; sys.exit(-1) da 4294967295 en Windows y 255 en Linux.",
               ["Escenario", "Windows", "Linux (WSL2)"], rows, [380, 290, 280], row_h=34,
               note="Los códigos 0 a 3 y 7 coinciden; los valores fuera de 0–255 y la interrupción no. Un contrato de CLI que quiera ser portable debe usar solo 0–125 y documentar cada valor.", note_kind="gold", foot="Medido con CPython 3.12.9 y 3.12.3; la interrupción se envió con CTRL_BREAK_EVENT en Windows y SIGINT en Linux.")


def se113_precedencia() -> Fig:
    rows = [["—", "—", "—", "default = 1", "default = 1"], ["—", "—", "archivo = 3", "archivo = 3", "default = 1"], ["—", "APP_LEVEL = 5", "—", "entorno = 5", "default = 1"],
            ["—", "APP_LEVEL = 5", "archivo = 3", "entorno = 5", "default = 1"], ["--level 9", "—", "—", "flag = 9", "flag = 9"], ["--level 9", "—", "archivo = 3", "flag = 9", "flag = 9"],
            ["--level 9", "APP_LEVEL = 5", "—", "flag = 9", "flag = 9"], ["--level 9", "APP_LEVEL = 5", "archivo = 3", "flag = 9", "flag = 9"]]
    return tab("Precedencia de configuración: flag, entorno, archivo, valor por defecto", "Tabla con las ocho combinaciones de flag, variable de entorno y archivo de configuración: con el orden correcto gana el flag, luego el entorno, luego el archivo y por último el valor por defecto; si el valor por defecto se aplica antes, tres de las ocho combinaciones dan 1 en vez de 5 o 3.",
               ["Flag", "Entorno", "Archivo", "Orden correcto", "Valor por defecto aplicado antes"], rows, [140, 170, 170, 220, 250], row_h=34,
               note="El error clásico es declarar default=1 en argparse: el parser siempre devuelve un valor y ya no se puede saber si el usuario lo escribió. Con default=None se distingue «ausente» y se aplican entorno y archivo. Fallaron 3 de 8 combinaciones.", note_kind="coral", foot="Cuentas deterministas sobre una función de ejemplo; idénticas en Windows y Linux.")


def se113_tuberias() -> Fig:
    rows = [["print('señal ✓') con la salida redirigida", "Salida 1: UnicodeEncodeError, el códec «charmap» no codifica ✓", "Salida 0: bytes UTF-8"],
            ["Lo mismo con PYTHONUTF8=1", "Salida 0: «señal ✓»", "Salida 0: «señal ✓»"],
            ["Bytes de print('a'); print('b') redirigido", "61 0D 0A 62 0D 0A (CRLF)", "61 0A 62 0A (LF)"],
            ["Cerrar la tubería con el productor aún escribiendo", "Salida 120: OSError, Invalid argument", "Salida 1: BrokenPipeError"],
            ["print en stdout y aviso en stderr", "Separados: datos y aviso", "Separados: datos y aviso"]]
    return tab("Tuberías y codificación: la misma CLI, dos comportamientos", "Tabla de cinco comprobaciones con la salida redirigida: imprimir un carácter fuera de la página de códigos falla en Windows con UnicodeEncodeError y funciona en Linux; con PYTHONUTF8 funciona en ambos; los saltos de línea son CRLF en Windows y LF en Linux; cerrar la tubería da la salida 120 y OSError en Windows y la salida 1 con BrokenPipeError en Linux.",
               ["Comprobación", "Windows", "Linux (WSL2)"], rows, [330, 340, 280], row_h=62,
               note="Una CLI que escribe a una tubería debe fijar la codificación (reconfigure(encoding='utf-8')), los saltos de línea si compara archivos, y tratar el cierre de la tubería como terminación normal. Separar stdout (datos) de stderr (diagnóstico) funcionó igual en ambos.", note_kind="coral")


# ---------------------------------------------------------------- SE-114
def se114_idempotencia() -> Fig:
    rows = [["Añadir una línea al archivo", "9 B", "18 B", "27 B", "Crece en cada ejecución"],
            ["Asegurar que la línea exista", "9 B", "9 B", "9 B", "Idempotente"],
            ["mkdir sin exist_ok", "crea", "FileExistsError", "FileExistsError", "Falla al repetir"],
            ["mkdir con exist_ok=True", "crea", "sin cambios", "sin cambios", "Idempotente"],
            ["Incrementar un contador", "1", "2", "3", "Cambia el estado en cada ejecución"],
            ["Fijar un valor (= 1)", "1", "1", "1", "Idempotente"]]
    return tab("Tres ejecuciones seguidas de seis tareas", "Tabla de seis tareas ejecutadas tres veces: añadir una línea deja el archivo en 9, 18 y 27 bytes; asegurar la línea lo deja en 9 bytes cada vez; mkdir sin exist_ok falla con FileExistsError desde la segunda vez; fijar un valor es idempotente y incrementar un contador no lo es.",
               ["Tarea", "1.ª", "2.ª", "3.ª", "Veredicto"], rows, [250, 120, 170, 170, 240], row_h=46,
               note="Idempotente no significa «no hace nada la segunda vez» sino «el estado final es el mismo». Una tarea que declara el estado deseado (asegurar, fijar) se puede repetir tras un fallo; una que describe un cambio (añadir, incrementar) no.", note_kind="teal", foot="Cuentas deterministas, idénticas en Windows (3.12.9) y Linux (3.12.3).")


def se114_atomica() -> Fig:
    rows = [["Reescribir con open('w') y morir tras 2 000 bytes", "Archivo de 2 000 B con «NUEVO»: el contenido antiguo (60 B) se perdió", "Igual"],
            ["Escribir en un temporal y morir antes de os.replace", "Original intacto (60 B, «VIEJO»); queda un .tmp huérfano", "Igual"],
            ["os.replace con el destino abierto por otro lector", "PermissionError (WinError 5)", "Reemplaza sin error"],
            ["Borrar un archivo que sigue abierto", "PermissionError", "Borra sin error"]]
    return tab("Escritura atómica: el reemplazo nunca deja un archivo a medias", "Tabla de cuatro casos: reescribir con open en modo w y morir deja el archivo truncado y sin el contenido antiguo; escribir en un temporal y morir antes de os.replace deja el original intacto y un temporal huérfano; os.replace y el borrado con el archivo abierto fallan con PermissionError en Windows y funcionan en Linux.",
               ["Caso", "Windows", "Linux (WSL2)"], rows, [350, 340, 260], row_h=62,
               note="El patrón seguro es: escribir un temporal en el mismo directorio, vaciar a disco y reemplazar con os.replace. En Windows el reemplazo puede fallar si otro proceso tiene el destino abierto, así que hay que reintentar con espera acotada y limpiar los temporales huérfanos al empezar.", note_kind="gold")


def se114_perdida() -> Fig:
    items = [("Windows, sin bloqueo", 148, "coral", "148 de 600"), ("Windows, sin bloqueo (otra pasada)", 20, "coral", "20 de 600"),
             ("Linux, sin bloqueo", 12, "coral", "12 de 600"), ("Linux, sin bloqueo (otra pasada)", 46, "coral", "46 de 600"),
             ("Windows, bloqueo O_EXCL (un proceso murió)", 310, "gold", "310 de 600"),
             ("Windows, bloqueo O_EXCL corregido", 600, "teal", "600 de 600"), ("Linux, bloqueo O_EXCL", 600, "teal", "600 de 600")]
    return bars("Dos procesos incrementan 300 veces un contador compartido", "Barras con el valor final de un contador al que dos procesos suman 300 veces cada uno, esperado 600: sin bloqueo quedó en 148 y 20 en Windows y en 12 y 46 en Linux; con un bloqueo O_EXCL el primer intento en Windows dio 310 porque un proceso murió con PermissionError; corregido dio 600 en Windows y 600 en Linux.",
                items, 0.9, "Leer, sumar y escribir no es atómico: los dos procesos leen el mismo valor y uno pisa al otro (actualización perdida). El bloqueo con O_EXCL lo evita, pero en Windows crear el archivo de bloqueo mientras otro lo borra lanzó PermissionError y mató a un proceso: hay que tratarlo como «ocupado». Con bloqueo, 600 incrementos tardaron 1,4–1,7 s en Windows y 0,4 s en Linux.", label_w=330, width=1000, note_kind="coral")


FIGURES = {
    "se-109-quien-llama-a-quien.svg": se109_pila,
    "se-109-costo-de-importar.svg": se109_importar,
    "se-109-sdk-y-timeout.svg": se109_timeout,
    "se-110-versiones-pep440-y-semver.svg": se110_versiones,
    "se-110-cambios-de-firma.svg": se110_firmas,
    "se-110-misma-firma-otro-contrato.svg": se110_contrato,
    "se-111-resolutor-con-retroceso.svg": se111_resolutor,
    "se-111-pip-resuelve.svg": se111_pip,
    "se-111-hashes-y-fijacion.svg": se111_hashes,
    "se-112-funciona-en-el-repo-falla-instalado.svg": se112_instalado,
    "se-112-sombras-en-sys-path.svg": se112_sombras,
    "se-112-etiquetas-de-rueda.svg": se112_etiquetas,
    "se-113-codigos-de-salida.svg": se113_salida,
    "se-113-precedencia-de-configuracion.svg": se113_precedencia,
    "se-113-tuberias-y-codificacion.svg": se113_tuberias,
    "se-114-idempotencia-de-tareas.svg": se114_idempotencia,
    "se-114-escritura-atomica.svg": se114_atomica,
    "se-114-actualizacion-perdida.svg": se114_perdida,
}
