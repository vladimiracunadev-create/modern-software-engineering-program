"""Figures for SE-109 to SE-114 (values measured with CPython 3.12.9 on Windows 11; Linux 3.12.3 under WSL2 where noted)."""
from __future__ import annotations

from figure_kit import Fig, _kit_finish, _kit_start, _wrap, grouped_bars, heatmap, scatter, stacked_bars, timeline

MEDIDO = "Medido con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu bajo WSL2; los tiempos dependen del equipo y se leen como razones."




def sketch(title: str, desc: str, width: int = 940):
    """Start a mechanism diagram with a visible title; returns the figure and the first free y."""
    return _kit_start(title, desc, width, None)


def bx(f: Fig, x: float, y: float, w: float, h: float, text: str, kind: str = "plain", size: int = 13, bold: bool = False) -> None:
    """Box that refuses to overflow: the text must fit its rectangle."""
    lines = _wrap(text, size, w - 20)
    assert len(lines) * size * 1.28 <= h - 6, f"box overflows: {text!r} ({len(lines)} lines in {h}px)"
    f.box(x, y, w, h, text, kind, size, bold=bold)


def done(f: Fig, y: float, note: str, kind: str = "gold", foot: str = "") -> Fig:
    _kit_finish(f, y, note, kind, foot)
    f.kind = "diagram"
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






# ---------------------------------------------------------------- SE-110




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






# ---------------------------------------------------------------- SE-112






# ---------------------------------------------------------------- SE-113






# ---------------------------------------------------------------- SE-114




def se114_perdida() -> Fig:
    items = [("Windows, sin bloqueo", 148, "coral", "148 de 600"), ("Windows, sin bloqueo (otra pasada)", 20, "coral", "20 de 600"),
             ("Linux, sin bloqueo", 12, "coral", "12 de 600"), ("Linux, sin bloqueo (otra pasada)", 46, "coral", "46 de 600"),
             ("Windows, bloqueo O_EXCL (un proceso murió)", 310, "gold", "310 de 600"),
             ("Windows, bloqueo O_EXCL corregido", 600, "teal", "600 de 600"), ("Linux, bloqueo O_EXCL", 600, "teal", "600 de 600")]
    return bars("Dos procesos incrementan 300 veces un contador compartido", "Barras con el valor final de un contador al que dos procesos suman 300 veces cada uno, esperado 600: sin bloqueo quedó en 148 y 20 en Windows y en 12 y 46 en Linux; con un bloqueo O_EXCL el primer intento en Windows dio 310 porque un proceso murió con PermissionError; corregido dio 600 en Windows y 600 en Linux.",
                items, 0.9, "Leer, sumar y escribir no es atómico: los dos procesos leen el mismo valor y uno pisa al otro (actualización perdida). El bloqueo con O_EXCL lo evita, pero en Windows crear el archivo de bloqueo mientras otro lo borra lanzó PermissionError y mató a un proceso: hay que tratarlo como «ocupado». Con bloqueo, 600 incrementos tardaron 1,4–1,7 s en Windows y 0,4 s en Linux.", label_w=330, width=1000, note_kind="coral")


# ---------------------------------------------------------------- SE-109
def se109_importar() -> Fig:
    win = [("json", 24, 33.6, "l"), ("argparse", 29, 36.6, "t"), ("logging", 42, 53.5, "t"), ("unittest", 67, 265.6, "l"), ("http.server", 91, 263.7, "r"), ("asyncio", 126, 303.3, "t")]
    lin = [("json", 24, 18.8, "l"), ("argparse", 28, 22.6, "b"), ("logging", 41, 31.1, "b"), ("unittest", 65, 54.4, "b"), ("http.server", 90, 68.9, "r"), ("asyncio", 111, 92.8, "b")]
    return scatter("Costo de importar: más módulos cargados, más milisegundos", "Dispersión de seis módulos de la biblioteca estándar: en el eje horizontal los módulos nuevos que carga cada import en un intérprete limpio y en el vertical el mejor de tres tiempos en milisegundos. En Windows el tiempo sube de 33,6 ms con json y 24 módulos a 303,3 ms con asyncio y 126 módulos; en Linux sube de 18,8 a 92,8 ms. A igual número de módulos Windows tarda entre 1,8 y 3,8 veces más.",
                   [("Windows (3.12.9)", [(m, t, n, s) for n, m, t, s in win], "coral"), ("Linux (3.12.3)", [(m, t, n, s) for n, m, t, s in lin], "teal")],
                   x_label="módulos nuevos cargados por el import (intérprete limpio con -S)", y_label="ms, mejor de 3 arranques", point_labels="all", log_y=True,
                   note="El número de módulos es estable entre plataformas (24 frente a 24 en json, 126 frente a 111 en asyncio); el tiempo no: asyncio costó 9,0 veces lo de json en Windows y 4,9 en Linux. Un import con open() en el cuerpo produjo un evento de auditoría de apertura más (3 frente a 2 en Windows, 5 frente a 4 en Linux). Un intérprete limpio parte con 25 módulos en Windows y 23 en Linux.", foot=MEDIDO)


def se109_timeout() -> Fig:
    return grouped_bars("Un SDK que oculta el timeout oculta también el peor caso", "Barras horizontales con el tiempo hasta que la llamada termina contra un servidor local que tarda 2 segundos: sin timeout la llamada espera los 2,00 s completos; con timeout=0,3 lanza TimeoutError a los 0,47 s en Windows y a los 0,37 s en Linux, cerca del plazo pedido. El timeout por defecto del socket es None, sin límite.",
                        ["Sin timeout (urlopen por defecto)", "Con timeout=0,3 s"], [("Windows", [2.00, 0.47], "coral"), ("Linux (WSL2)", [2.00, 0.37], "teal")],
                        unit="s hasta que la llamada termina", horizontal=True, decimals=2, label_w=230,
                        note="El valor por defecto de la biblioteca estándar es «esperar sin límite» (socket.getdefaulttimeout() es None). Un SDK que envuelve la llamada sin exponer timeout hereda ese peor caso: con un servidor que nunca contestara, la espera no terminaría (no se midió; se deduce del valor None). El SDK debe fijar un timeout razonable y dejar que el consumidor lo cambie.", note_kind="coral", foot=MEDIDO)


# ---------------------------------------------------------------- SE-110
def se110_versiones() -> Fig:
    f, y = sketch("Cómo ordena packaging las versiones: PEP 440 de menor a mayor",
                  "Diagrama del orden de PEP 440 medido con packaging 26.2: 1.0.0a2 es menor que 1.0.0a10, que es menor que 1.0.0rc1, que es menor que 1.0.0, igual a 1.0; por encima de 1.0.0 quedan 1.0.0+build5 y 1.0.post1. Aparte, 1.0.0-alpha.beta es inválida y 1.0.0-01 se lee como post-release.")
    f.text(14, y + 14, "orden ascendente (de menor a mayor)", 13, "start", 700, "#32505f")
    ys = y + 28
    xs = [10, 160, 310, 470]
    labels = [("1.0.0a2", "teal"), ("1.0.0a10", "teal"), ("1.0.0rc1", "teal"), ("1.0.0  =  1.0", "navy")]
    for x, (t, k) in zip(xs, labels):
        bx(f, x, ys, 120 if x != 470 else 140, 44, t, k, 14, True)
    for i in range(3):
        wend = 120 if i < 3 else 140
        f.arrow([(xs[i] + 120, ys + 22), (xs[i + 1], ys + 22)], "<", label_at=((xs[i] + 120 + xs[i + 1]) / 2, ys + 12))
    f.text(250, ys + 62, "prerrelease", 13, "middle", 400, "#32505f")
    bx(f, 10, ys + 72, 270, 62, "a10 > a2: los números se comparan como números, no como texto", "grey")
    bx(f, 290, ys + 72, 160, 62, "1.0.0-rc.1 se normaliza a 1.0.0rc1", "grey")
    bx(f, 470, ys + 72, 140, 62, "los ceros finales no cuentan", "grey")
    bx(f, 690, ys - 4, 240, 44, "1.0.0+build5  (metadatos locales)", "gold")
    bx(f, 690, ys + 52, 240, 44, "1.0.post1  (post-release)", "gold")
    f.arrow([(610, ys + 22), (690, ys + 18)], ">", label_at=(650, ys + 8))
    f.arrow([(610, ys + 22), (690, ys + 74)], ">", label_at=(634, ys + 56))
    f.text(810, ys + 118, "mayores que 1.0.0", 13, "middle", 400, "#32505f")
    y2 = ys + 156
    f.text(14, y2 + 6, "no entran en el orden", 13, "start", 700, "#32505f")
    bx(f, 10, y2 + 16, 300, 62, "1.0.0-alpha.beta y 1.0.0.x → InvalidVersion", "coral")
    bx(f, 330, y2 + 16, 300, 62, "1.0.0-01 → se lee como 1.0.0.post1: un guion puede ser post-release", "gold")
    bx(f, 650, y2 + 16, 280, 62, "Como texto: 1.10.0, 1.2.0, 1.9.0. Como versiones: 1.2.0, 1.9.0, 1.10.0", "grey")
    return done(f, y2 + 90, "SemVer escribe el guion de 1.0.0-rc.1 y PEP 440 lo reescribe; SemVer ignora «+metadata» al ordenar y PEP 440 no; SemVer no define post-releases. No todo SemVer válido es PEP 440 válido. Si un SDK expone versiones, debe declarar qué esquema usa.",
                "gold", "Medido con CPython 3.12.9 y packaging 26.2 en Windows 11; las comparaciones no dependen del sistema operativo.")


def se110_firmas() -> Fig:
    rows = ["Añadir parámetro opcional con nombre", "Añadir parámetro obligatorio", "Renombrar b a second", "Reordenar a, b a b, a", "Quitar el parámetro timeout", "Cambiar el valor por defecto de timeout", "Hacer b solo por nombre", "Hacer a solo posicional"]
    cols = ["f(1, 2)", "f(1, b=2)", "f(a=1, b=2, timeout=5)", "f(1, 2, timeout=3)"]
    v = [[0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0]]
    return heatmap("Qué llamadas rompe cada cambio de firma", "Mapa de calor de ocho cambios sobre f(a, b, *, timeout=10) frente a cuatro formas de llamar: oscuro es TypeError y claro es que la llamada funciona. Añadir un parámetro obligatorio rompe las cuatro llamadas; renombrar b rompe las dos que lo nombran; reordenar y cambiar el valor por defecto no rompen ninguna pero cambian el resultado de f(1, 2), señalado con contorno.",
                   rows, cols, v, unit="TypeError", scale="coral", vmin=0, vmax=1, cell_fmt=lambda x: "TypeError" if x else "ok", highlight=[(3, 0), (5, 0)], cell_h=40, label_w=300,
                   note="Dos de los ocho cambios (reordenar y cambiar el valor por defecto) no producen ningún error y cambian el resultado de f(1, 2) (celdas con contorno): son los que una revisión de firmas no detecta y una prueba de contrato sí. También hacer b solo por nombre rompe f(1, 2) y f(1, 2, timeout=3), y hacer a solo posicional rompe la llamada con a=1.", note_kind="coral", foot="Medido con CPython 3.12.9; «ok» = la llamada funciona; contorno = funciona pero devuelve otro valor.")


# ---------------------------------------------------------------- SE-111
def se111_resolutor() -> Fig:
    f, y = sketch("Resolver dependencias es buscar, y a veces no hay solución",
                  "Diagrama del conflicto de un índice de cuatro paquetes: app depende de libA y libB; libA 2.0 exige core de versión 2 o mayor y libB exige core menor que 2, de modo que la versión más nueva de cada uno no es una solución. Con retroceso el resolutor evalúa 15 candidatos y llega a app 1.0, libA 1.0, libB 2.0 y core 1.0; un índice sin combinación válida termina sin solución y graphlib ordena core, libA, libB, app o detecta el ciclo app, core, libA, app.")
    bx(f, 380, y + 6, 180, 44, "app", "navy", 15, True)
    bx(f, 150, y + 86, 230, 44, "libA 2.0", "plain", 14, True)
    bx(f, 560, y + 86, 230, 44, "libB", "plain", 14, True)
    bx(f, 150, y + 150, 230, 44, "pide core ≥ 2", "gold")
    bx(f, 560, y + 150, 230, 44, "pide core < 2", "gold")
    f.arrow([(440, y + 50), (265, y + 86)])
    f.arrow([(500, y + 50), (675, y + 86)])
    f.arrow([(265, y + 130), (265, y + 150)])
    f.arrow([(675, y + 130), (675, y + 150)])
    bx(f, 330, y + 220, 280, 52, "core: ninguna versión cumple las dos a la vez", "coral", 13, True)
    f.arrow([(265, y + 194), (390, y + 220)], color="#c0432f")
    f.arrow([(675, y + 194), (550, y + 220)], color="#c0432f")
    y2 = y + 300
    bx(f, 10, y2, 300, 96, "Siempre la más nueva: sin solución (6 candidatos evaluados, 3 retrocesos)", "coral")
    bx(f, 320, y2, 300, 96, "Con retroceso: app 1.0, libA 1.0, libB 2.0, core 1.0 (15 candidatos, 3 retrocesos)", "teal")
    bx(f, 630, y2, 300, 96, "Índice sin ninguna combinación válida: termina y lo declara (6 candidatos, 3 retrocesos)", "coral")
    bx(f, 10, y2 + 112, 450, 60, "graphlib ordena la instalación: core, libA, libB, app (dependencias primero)", "grey")
    bx(f, 480, y2 + 112, 450, 60, "Dependencia circular app → core → libA → app: CycleError", "gold")
    return done(f, y2 + 184, "El conflicto es real: la versión más nueva de cada paquete no es una solución; la solución es un conjunto compatible, y a veces no existe. Los conteos son del resolutor de juguete, no de pip.", "gold", "Cuentas deterministas, idénticas en Windows (3.12.9) y Linux (3.12.3).")


def se111_pip() -> Fig:
    lanes = [("pip install libaX", [(1.0, 3.0, "permitido: cualquier coreX", "teal"), (2.95, 3.0, "", "navy")]),
             ("pip install libbX", [(1.0, 2.0, "permitido: coreX < 2", "gold"), (1.0, 1.05, "", "navy")]),
             ("pip install libaX libbX", [(1.0, 2.0, "permitido: coreX < 2", "gold"), (1.0, 1.05, "", "navy")]),
             ("libbX con «coreX>=3»", [(1.0, 2.0, "libbX: < 2", "gold"), (3.0, 3.1, "≥3", "coral")]),
             ("libaX tras publicarse coreX 3.1", [(1.0, 3.1, "permitido: cualquier coreX", "teal"), (3.05, 3.1, "", "navy")])]
    return timeline("pip resuelve coreX: versiones permitidas y versión elegida", "Líneas de tiempo de versiones de coreX para cinco órdenes de pip install con la opción dry-run: la barra es el rango permitido y la marca oscura la versión elegida. libaX solo instala coreX 3.0; libbX o libaX con libbX bajan a coreX 1.0 porque libbX pide menos de 2; libbX con coreX mayor o igual que 3 deja dos rangos que no se tocan y falla con ResolutionImpossible; tras publicarse coreX 3.1 la misma orden de libaX elige 3.1.",
                    lanes, unit="versión de coreX (barra: rango permitido; marca oscura: versión elegida)", ticks=[1.0, 1.5, 2.0, 2.5, 3.0, 3.1], t_max=3.1, lane_h=46, label_w=240,
                    note="Elecciones: libaX 2.0 con coreX 3.0; libbX 1.0 con coreX 1.0; libaX 1.0 con libbX 1.0 y coreX 1.0 (libaX retrocede para convivir); en la cuarta orden los rangos < 2 y ≥ 3 no se tocan: ResolutionImpossible, salida 1, y pip no instala nada; en la quinta, sin fijar, la misma orden instala coreX 3.1 y libaX 2.0. Mismo resultado en Windows (pip 24.3.1) y Linux (pip 24.0); en Linux se aceptó el modo «gestionado externamente» de PEP 668 porque se usó el intérprete del sistema con dry-run, sin instalar nada.", note_kind="teal", foot=MEDIDO)


def se111_hashes() -> Fig:
    f, y = sketch("Un lockfile con hashes: pip acepta el artefacto, no el nombre",
                  "Árbol de decisión de pip con la opción require-hashes: un requisito sin versión fijada con == se rechaza con salida 1; uno fijado cuyo hash no coincide se rechaza con salida 1 y muestra Expected y Got; uno fijado con el hash correcto se acepta con salida 0. Sin la opción y sin fijar, una versión nueva del índice se instala sin aviso.")
    bx(f, 10, y + 20, 200, 60, "pip install --require-hashes", "navy", 13, True)
    bx(f, 280, y + 20, 190, 60, "¿el requisito está fijado con ==?", "grey", 13, True)
    bx(f, 540, y + 20, 190, 60, "¿el SHA-256 de la rueda coincide?", "grey", 13, True)
    f.arrow([(210, y + 50), (280, y + 50)])
    f.arrow([(470, y + 50), (540, y + 50)], "sí", label_at=(505, y + 40))
    bx(f, 780, y + 20, 150, 60, "Salida 0: «Would install coreX-3.0»", "teal")
    f.arrow([(730, y + 50), (780, y + 50)], "sí", label_at=(755, y + 40))
    bx(f, 280, y + 140, 240, 76, "Salida 1: «all requirements must have their versions pinned with ==»", "coral")
    f.arrow([(375, y + 80), (375, y + 140)], "no", label_at=(390, y + 112), label_anchor="start")
    bx(f, 560, y + 140, 370, 76, "Salida 1: «THESE PACKAGES DO NOT MATCH THE HASHES»; Expected y Got muestran dos SHA-256 distintos (un byte alterado)", "coral")
    f.arrow([(635, y + 80), (700, y + 140)], "no", label_at=(690, y + 104), label_anchor="start")
    bx(f, 10, y + 140, 230, 76, "Sin --require-hashes y sin fijar, con coreX 3.1 en el índice: instala coreX 3.1", "gold")
    return done(f, y + 232, "El hash vincula la instalación a unos bytes concretos, no a un nombre y una versión. No prueba que esos bytes sean seguros: solo que son los mismos que alguien revisó. La reproducibilidad no está en la orden sino en el archivo de fijación. Resultados idénticos en Windows y Linux.", "gold", MEDIDO)


# ---------------------------------------------------------------- SE-112
def se112_instalado() -> Fig:
    f, y = sketch("Funciona en el repositorio, falla instalado: el archivo de datos que no viajó",
                  "Diagrama de dos ruedas del mismo código: sin package-data la rueda pesa 1353 bytes en Windows y 1351 en Linux y no contiene data/rules.json, de modo que load_rules funciona desde el árbol de fuentes pero lanza FileNotFoundError una vez instalada; con package-data la rueda pesa 1536 y 1533 bytes, incluye el archivo y funciona en los dos lugares.")
    bx(f, 10, y + 54, 170, 150, "Mismo código fuente y mismo load_rules()", "navy", 14, True)
    f.text(465, y + 20, "pyproject.toml decide qué archivos empaqueta el constructor", 13, "middle", 700, "#32505f")
    bx(f, 250, y + 6 + 40, 220, 64, "Sin package-data", "coral", 14, True)
    bx(f, 250, y + 6 + 130, 220, 64, "package-data = data/*.json", "teal", 14, True)
    f.arrow([(180, y + 100), (250, y + 78)])
    f.arrow([(180, y + 160), (250, y + 168)])
    bx(f, 530, y + 46, 230, 64, "Rueda: 1353 B (Windows) · 1351 B (Linux). Sin data/rules.json", "coral")
    bx(f, 530, y + 136, 230, 64, "Rueda: 1536 B (Windows) · 1533 B (Linux). Con data/rules.json", "teal")
    f.arrow([(470, y + 78), (530, y + 78)])
    f.arrow([(470, y + 168), (530, y + 168)])
    bx(f, 800, y + 46, 130, 64, "Instalada: FileNotFoundError", "coral")
    bx(f, 800, y + 136, 130, 64, "Instalada: {'v': 1}", "teal")
    f.arrow([(760, y + 78), (800, y + 78)])
    f.arrow([(760, y + 168), (800, y + 168)])
    bx(f, 10, y + 222, 920, 40, "Desde el árbol de fuentes, las dos ruedas devuelven {'v': 1}: el repositorio tiene el archivo, así que ninguna prueba que corra ahí puede ver la diferencia.", "grey")
    return done(f, y + 274, "El código no cambió entre las dos ramas: cambió qué archivos empaquetó el constructor. Solo una instalación limpia lo muestra. El paquete sub/ no tiene __init__.py y aun así se empaquetó, porque la configuración de pyproject.toml permite paquetes de espacio de nombres por defecto.", "coral", MEDIDO)


def se112_sombras() -> Fig:
    f, y = sketch("Quién gana en sys.path: la carpeta propia va primero",
                  "Diagrama de dos listas sys.path: con python main.py la carpeta del script va primero, de modo que un json.py local tapa a la biblioteca estándar y json.dumps({}) devuelve FAKE; con la opción -I esa carpeta se quita y gana la biblioteca estándar, que devuelve {}. Con -c el directorio actual va primero y se ejecuta el random.py local; python -m json.tool falla porque el json.py local no es un paquete; y un directorio sin __init__.py se importa como paquete de espacio de nombres.")
    f.text(235, y + 16, "python main.py", 14, "middle", 700, "#142231")
    f.text(705, y + 16, "python -I main.py", 14, "middle", 700, "#142231")
    for x, first, kind1, res, kind2 in ((10, "1.º carpeta del script: json.py local", "coral", "json.dumps({}) devuelve «FAKE»", "coral"), (480, "carpeta del script y del usuario: quitadas", "grey", "json.dumps({}) devuelve «{}»", "teal")):
        bx(f, x, y + 28, 450, 44, first, kind1, 13, True)
        bx(f, x, y + 80, 450, 40, "2.º biblioteca estándar (json/__init__.py)", "teal" if kind1 == "grey" else "plain", 13)
        bx(f, x, y + 128, 450, 36, "3.º site-packages", "plain", 13)
        bx(f, x, y + 180, 450, 40, res, kind2, 13, True)
        f.arrow([(x + 225, y + 164), (x + 225, y + 180)])
    f.text(470, y + 244, "Otros casos medidos con la misma regla", 13, "middle", 700, "#32505f")
    bx(f, 10, y + 256, 300, 84, "python -c «import random» con random.py en la carpeta: con -c, el directorio actual va primero y se ejecuta el local", "gold")
    bx(f, 320, y + 256, 300, 84, "python -m json.tool con un json.py local: error, no se puede encontrar json.tool (el local no es un paquete)", "coral")
    bx(f, 630, y + 256, 300, 84, "import capkit.sub.mod sin sub/__init__.py: funciona; sub.__file__ es None y __path__ es un _NamespacePath", "grey")
    return done(f, y + 354, "Mismo resultado en Windows y Linux. Nombrar un módulo como uno de la biblioteca estándar (json, random, email, test) rompe programas ajenos al proyecto sin dar un error de nombre; el fallo aparece lejos del archivo mal nombrado.", "coral", MEDIDO)


def se112_etiquetas() -> Fig:
    f, y = sketch("Etiquetas de compatibilidad: una escalera de la más específica a py30-none-any",
                  "Diagrama de dos escaleras de etiquetas de rueda ordenadas de la más específica a la menos específica: el intérprete de Windows acepta 42 etiquetas, de cp312-cp312-win_amd64 a py30-none-any, y el de Linux bajo WSL2 acepta 1067, de cp312-cp312-manylinux_2_39_x86_64 a py30-none-any. La rueda de Python puro py3-none-any aparece en las dos.")
    f.text(10, y + 14, "más específica", 13, "start", 700, "#32505f")
    f.text(930, y + 14, "menos específica", 13, "end", 700, "#32505f")
    for i, (name, count, first, wide, kind) in enumerate((("Windows (3.12.9)", "42 etiquetas", "cp312-cp312-win_amd64", 270, "coral"), ("Linux bajo WSL2 (3.12.3)", "1 067 etiquetas", "cp312-cp312-manylinux_2_39_x86_64", 430, "teal"))):
        top = y + 28 + i * 118
        f.text(10, top + 12, f"{name}: {count}", 14, "start", 700, "#142231")
        bx(f, 10, top + 24, 340 if i == 0 else 380, 46, first, kind, 13, True)
        bx(f, 790, top + 24, 140, 46, "py30-none-any", "grey", 13, True)
        f.arrow([(350 if i == 0 else 390, top + 47), (790, top + 47)], "…" + (" 40 etiquetas intermedias" if i == 0 else " 1 065 etiquetas intermedias"), label_at=(570, top + 38))
    bx(f, 290, y + 262, 360, 44, "capkit-1.0.0-py3-none-any.whl", "gold", 13, True)
    f.text(470, y + 330, "La rueda de Python puro cuadra con py3-none-any: sirve en las dos plataformas", 13, "middle", 400, "#142231")
    return done(f, y + 344, "Una rueda py3-none-any sirve en las dos plataformas; una rueda con extensión compilada necesita una etiqueta de la lista. Linux acepta tantas etiquetas porque cuenta cada versión de la biblioteca C compatible (manylinux_2_39 hacia abajo). Una rueda con etiqueta win_amd64 no se instala en Linux ni a la inversa.", "teal", MEDIDO)


# ---------------------------------------------------------------- SE-113
def se113_salida() -> Fig:
    f, y = sketch("Códigos de salida: seis coinciden y tres dependen del sistema",
                  "Diagrama de nueve escenarios de salida de un programa en Python observados con subprocess: terminar sin error, sys.exit(3), sys.exit con texto, una excepción, opción desconocida y --help dan el mismo código en Windows y Linux; Ctrl+C da 3221225786 en Windows y menos 2 en Linux, sys.exit(256) da 256 y 0, y sys.exit(-1) da 4294967295 y 255, porque Windows conserva 32 bits sin signo y Linux solo el byte bajo.")
    bx(f, 10, y + 8, 920, 30, "Coinciden en ambos sistemas", "teal", 14, True)
    chips = [("terminar sin error", "0"), ("sys.exit(3)", "3"), ("sys.exit('mensaje')", "1, mensaje a stderr"), ("excepción sin capturar", "1"), ("argparse: opción desconocida", "2"), ("argparse: --help", "0")]
    cw = (920 - 5 * 8) / 6
    for i, (a, b) in enumerate(chips):
        bx(f, 10 + i * (cw + 8), y + 46, cw, 70, f"{a}\n→ {b}", "plain", 13)
    bx(f, 10, y + 140, 920, 30, "Difieren: Windows conserva 32 bits sin signo; Linux entrega el byte bajo", "coral", 14, True)
    heads = [("sys.exit(256)", "Windows: 256", "Linux: 0 (256 mod 256)"), ("sys.exit(-1)", "Windows: 4294967295", "Linux: 255 (−1 mod 256)"), ("Ctrl+C sin capturar", "Windows: 3221225786 (0xC000013A)", "Linux: −2 (terminado por SIGINT)")]
    cw2 = (920 - 2 * 20) / 3
    for i, (h, w, l) in enumerate(heads):
        x = 10 + i * (cw2 + 20)
        bx(f, x, y + 180, cw2, 34, h, "navy", 13, True)
        bx(f, x, y + 220, cw2, 52, w, "coral", 13)
        bx(f, x, y + 280, cw2, 52, l, "teal", 13)
    return done(f, y + 346, "Los códigos 0 a 3 coinciden; los valores fuera de 0–255 y la interrupción no. Un contrato de CLI que quiera ser portable debe usar solo 0–125 y documentar cada valor.", "gold", "Medido con CPython 3.12.9 y 3.12.3; la interrupción se envió con CTRL_BREAK_EVENT en Windows y SIGINT en Linux.")


def se113_precedencia() -> Fig:
    rows = ["Nada", "Solo archivo (3)", "Solo entorno (5)", "Entorno (5) y archivo (3)", "Solo flag (9)", "Flag (9) y archivo (3)", "Flag (9) y entorno (5)", "Flag, entorno y archivo"]
    good = [1, 3, 5, 5, 9, 9, 9, 9]
    bad = [1, 1, 1, 1, 9, 9, 9, 9]
    return heatmap("Precedencia de configuración: el valor por defecto aplicado antes borra el entorno y el archivo", "Mapa de calor del valor efectivo de level en las ocho combinaciones de flag, entorno y archivo: con el orden correcto gana el flag, luego el entorno, luego el archivo y por último el valor por defecto; si el valor por defecto se aplica antes, tres combinaciones (solo archivo, solo entorno y entorno con archivo) dan 1 en vez de 3, 5 y 5, señaladas con contorno.",
                   rows, ["Orden correcto: flag, entorno, archivo, por defecto", "Por defecto aplicado antes (default=1 en argparse)"], list(map(list, zip(good, bad))), unit="valor efectivo de level", scale="navy", vmin=1, vmax=9,
                   highlight=[(1, 1), (2, 1), (3, 1)], cell_h=40, label_w=240, width=860,
                   note="El error clásico es declarar default=1 en argparse: el parser siempre devuelve un valor y ya no se puede saber si el usuario lo escribió. Con default=None se distingue «ausente» y se aplican entorno y archivo. Fallaron 3 de 8 combinaciones (con contorno).", note_kind="coral", foot="Cuentas deterministas sobre una función de ejemplo; idénticas en Windows y Linux.")


def se113_tuberias() -> Fig:
    f, y = sketch("Tuberías y codificación: la misma CLI, dos comportamientos",
                  "Diagrama de tres etapas de una CLI con la salida redirigida, en Windows y en Linux. Codificación: Windows falla con UnicodeEncodeError (códec charmap) al imprimir un carácter fuera de la página de códigos y Linux escribe UTF-8; con PYTHONUTF8=1 ambos funcionan. Saltos de línea: CRLF en Windows y LF en Linux. Cierre de la tubería: salida 120 con OSError en Windows y salida 1 con BrokenPipeError en Linux.")
    heads = ["1. Codificar print('señal ✓')", "2. Escribir los saltos de línea", "3. El lector cierra la tubería"]
    cw = (920 - 2 * 44) / 3
    for i, h in enumerate(heads):
        bx(f, 10 + i * (cw + 44), y + 8, cw, 36, h, "navy", 13, True)
    rows = [("Windows", "coral", ["Salida 1: UnicodeEncodeError, el códec «charmap» no codifica ✓", "61 0D 0A 62 0D 0A (CRLF)", "Salida 120: OSError, Invalid argument"]),
            ("Linux (WSL2)", "teal", ["Salida 0: bytes UTF-8", "61 0A 62 0A (LF)", "Salida 1: BrokenPipeError"])]
    for r, (name, kind, cells) in enumerate(rows):
        top = y + 60 + r * 112
        for i, c in enumerate(cells):
            bx(f, 10 + i * (cw + 44), top, cw, 84, f"{name}: {c}", kind, 13)
            if i:
                f.arrow([(10 + i * (cw + 44) - 44, top + 42), (10 + i * (cw + 44), top + 42)])
    bx(f, 10, y + 288, 920, 44, "Con PYTHONUTF8=1 la primera etapa da salida 0 y «señal ✓» en ambos sistemas. stdout (datos) y stderr (diagnóstico) quedaron separados en ambos.", "gold")
    return done(f, y + 344, "Una CLI que escribe a una tubería debe fijar la codificación (reconfigure(encoding='utf-8')), los saltos de línea si compara archivos, y tratar el cierre de la tubería como terminación normal.", "coral", MEDIDO)


# ---------------------------------------------------------------- SE-114
def se114_idempotencia() -> Fig:
    return grouped_bars("Repetir una tarea tres veces: el estado crece o se queda quieto", "Barras agrupadas con el estado tras cada una de tres ejecuciones, dividido por el estado de la primera: añadir una línea al archivo (9, 18 y 27 bytes) e incrementar un contador (1, 2 y 3) crecen 1, 2 y 3 veces; asegurar la línea (9 bytes) y fijar un valor (1) se quedan en 1 en las tres. Son las tareas idempotentes frente a las que cambian el estado en cada ejecución.",
                        ["Añadir una línea (9, 18, 27 B)", "Asegurar la línea (9, 9, 9 B)", "Incrementar un contador (1, 2, 3)", "Fijar un valor = 1 (1, 1, 1)"],
                        [("1.ª ejecución", [1, 1, 1, 1], "grey"), ("2.ª ejecución", [2, 1, 2, 1], "gold"), ("3.ª ejecución", [3, 1, 3, 1], "coral")],
                        unit="estado ÷ estado de la 1.ª ejecución", ticks=[0, 1, 2, 3], decimals=0, horizontal=True, label_w=260,
                        note="Idempotente no significa «no hace nada la segunda vez» sino «el estado final es el mismo». mkdir sin exist_ok crea la primera vez y falla con FileExistsError en la segunda y la tercera; con exist_ok=True crea y luego no cambia nada. Una tarea que declara el estado deseado (asegurar, fijar) se puede repetir tras un fallo; una que describe un cambio (añadir, incrementar) no.", note_kind="teal", foot="Cuentas deterministas, idénticas en Windows (3.12.9) y Linux (3.12.3).")


def se114_atomica() -> Fig:
    f, y = sketch("Escritura atómica: el reemplazo nunca deja un archivo a medias",
                  "Diagrama de dos estrategias de escritura con una muerte a mitad: reescribir con open en modo w trunca el archivo de 60 bytes, escribe 2000 bytes de «NUEVO» y al morir deja un archivo de 2000 bytes con contenido a medias y sin el original; escribir en un temporal y morir antes de os.replace deja el original de 60 bytes intacto y un temporal huérfano. En Windows, os.replace y borrar con el destino abierto fallan con PermissionError.")
    f.text(10, y + 14, "Reescritura directa", 14, "start", 700, "#142231")
    steps = [("open(destino, 'w') trunca el archivo de 60 B «VIEJO»", "gold"), ("escribe 2 000 B de «NUEVO»…", "gold"), ("✖ el proceso muere", "coral"), ("Destino: 2 000 B con «NUEVO» a medias; el original se perdió", "coral")]
    cw = (920 - 3 * 32) / 4
    for i, (t, k) in enumerate(steps):
        bx(f, 10 + i * (cw + 32), y + 24, cw, 76, t, k)
        if i:
            f.arrow([(10 + i * (cw + 32) - 32, y + 62), (10 + i * (cw + 32), y + 62)])
    f.text(10, y + 134, "Temporal en el mismo directorio y os.replace", 14, "start", 700, "#142231")
    steps2 = [("escribe un temporal con el contenido nuevo", "teal"), ("vacía a disco", "teal"), ("✖ el proceso muere antes de os.replace", "coral"), ("Destino: 60 B «VIEJO» intacto; queda un .tmp huérfano", "teal")]
    for i, (t, k) in enumerate(steps2):
        bx(f, 10 + i * (cw + 32), y + 148, cw, 76, t, k)
        if i:
            f.arrow([(10 + i * (cw + 32) - 32, y + 186), (10 + i * (cw + 32), y + 186)])
    bx(f, 10, y + 250, 450, 64, "Solo en Windows: os.replace con el destino abierto por otro lector falla con PermissionError (WinError 5)", "coral")
    bx(f, 480, y + 250, 450, 64, "Solo en Windows: borrar un archivo que sigue abierto falla con PermissionError; en Linux reemplaza y borra sin error", "coral")
    return done(f, y + 328, "El patrón seguro es: escribir un temporal en el mismo directorio, vaciar a disco y reemplazar con os.replace. En Windows el reemplazo puede fallar si otro proceso tiene el destino abierto, así que hay que reintentar con espera acotada y limpiar los temporales huérfanos al empezar. Los dos cortes dieron el mismo resultado en Linux.", "gold", MEDIDO)


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
