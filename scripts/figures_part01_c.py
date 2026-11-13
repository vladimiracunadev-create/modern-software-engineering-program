"""Figures for SE-019 and SE-020."""
from __future__ import annotations

from figure_kit import Fig


# ---------------------------------------------------------------- SE-019
def se019_estados() -> Fig:
    f = Fig(940, 430, "Estados de un hilo y las transiciones que los provocan",
            "Diagrama de estados: nuevo pasa a listo; listo y ejecutando se alternan por asignación de CPU y expropiación; "
            "ejecutando pasa a bloqueado al esperar un evento y vuelve a listo cuando ocurre; ejecutando termina.")
    f.box(20, 150, 120, 56, "Nuevo", "grey", 14, bold=True)
    f.box(230, 150, 130, 56, "Listo", "gold", 14, bold=True)
    f.box(470, 150, 150, 56, "Ejecutando", "teal", 14, bold=True)
    f.box(470, 320, 150, 56, "Bloqueado", "coral", 14, bold=True)
    f.box(760, 150, 140, 56, "Terminado", "grey", 14, bold=True)
    f.arrow([(140, 178), (230, 178)], "se crea", label_at=(185, 168))
    f.arrow([(360, 166), (470, 166)], "el planificador asigna CPU", label_at=(415, 138))
    f.arrow([(470, 196), (360, 196)], "cuota agotada: expropiación", label_at=(415, 226))
    f.arrow([(620, 178), (760, 178)], "termina o falla", label_at=(690, 168))
    f.arrow([(545, 206), (545, 320)], "espera I/O, bloqueo o sleep", label_at=(560, 266), label_anchor="start")
    f.arrow([(470, 348), (295, 348), (295, 206)], "ocurre el evento", label_at=(380, 340))
    f.box(20, 262, 250, 150, "Un hilo bloqueado no consume CPU: el reloj de pared corre, el de CPU no. Un hilo listo sí quiere CPU y espera turno; "
          "esa espera también cuenta como tiempo de pared.", "grey", 13)
    f.box(680, 262, 240, 136, "Un cambio de contexto guarda el estado de un hilo y carga el de otro. Tiene costo y desordena las cachés.", "gold", 13)
    return f


def se019_lectura() -> Fig:
    f = Fig(960, 540, "Ruta de una lectura bloqueante entre aplicación, núcleo y dispositivo",
            "Tres carriles y siete pasos: la aplicación llama a read; el núcleo valida y programa la operación y bloquea el hilo; "
            "el dispositivo transfiere los datos a memoria y avisa con una interrupción; el núcleo marca el hilo como listo "
            "y el planificador le devuelve la CPU.")
    lanes = [("Hilo de la aplicación", 160), ("Núcleo del sistema operativo", 480), ("Dispositivo", 800)]
    for name, x in lanes:
        f.box(x - 130, 12, 260, 40, name, "navy", 13, bold=True)
        f.line(x, 52, x, 520, dashed=True)
    f.box(30, 76, 260, 52, "1 read(): pide datos del archivo", "plain", 13)
    f.arrow([(290, 102), (350, 102)], "syscall", label_at=(320, 94))
    f.box(350, 76, 260, 52, "2 Entra en modo núcleo: valida y programa la E/S", "teal", 13)
    f.arrow([(610, 102), (670, 102)], "orden", label_at=(640, 94))
    f.box(30, 152, 260, 52, "3 El hilo queda bloqueado; la CPU atiende a otro", "gold", 13)
    f.arrow([(350, 178), (290, 178)])
    f.box(670, 152, 260, 52, "4 Transfiere los datos a memoria (DMA)", "plain", 13)
    f.box(670, 228, 260, 52, "5 Señala el fin con una interrupción", "coral", 13, bold=True)
    f.arrow([(670, 254), (610, 254)], "interrupción", label_at=(640, 246))
    f.box(350, 228, 260, 64, "6 El manejador marca el hilo como listo; el planificador decide cuándo", "teal", 13)
    f.box(30, 320, 260, 60, "7 El hilo vuelve al modo usuario: read() devuelve los bytes", "plain", 13)
    f.arrow([(350, 350), (290, 350)])
    f.box(30, 420, 900, 90, "La CPU no esperó ocupada: mientras el dispositivo trabajaba, atendía a otros hilos. Por eso una lectura puede tardar mucho en tiempo de pared "
          "y casi nada en tiempo de CPU. El sistema real puede usar sondeo, búferes o E/S asíncrona; la secuencia muestra responsabilidades, no cada señal.", "grey", 13)
    return f


def se019_medicion() -> Fig:
    f = Fig(960, 470, "Hilos y procesos medidos en CPython 3.12: la carga decide",
            "Tres grupos de barras con una medición real: en tareas de espera cuatro hilos reducen 1,0 s a 0,25 s; en cálculo largo, "
            "dos hilos casi no ayudan (4,57 a 4,10 s) y dos procesos lo reducen a 2,88 s; en cálculo corto los procesos pierden por su costo de arranque.")
    groups = [
        ("4 tareas de espera (0,25 s cada una)", [("secuencial", 1.001, "gold"), ("4 hilos", 0.252, "teal")]),
        ("2 tareas de cálculo corto (≈ 0,2 s)", [("secuencial", 0.42, "gold"), ("2 hilos", 0.43, "gold"), ("2 procesos", 0.534, "coral")]),
        ("2 tareas de cálculo largo (≈ 2,3 s)", [("secuencial", 4.566, "gold"), ("2 hilos", 4.101, "gold"), ("2 procesos", 2.88, "teal")]),
    ]
    y = 26
    for title, bars in groups:
        f.text(20, y + 10, title, 14, "start", 700)
        for i, (label, v, kind) in enumerate(bars):
            by = y + 22 + i * 32
            f.text(190, by + 18, label, 13, "end")
            w = v * 90
            f.box(200, by, w, 26, "", kind, radius=3)
            f.text(200 + w + 8, by + 19, f"{v:g} s", 13, "start", 700)
        y += 22 + len(bars) * 32 + 28
    f.box(700, 40, 240, 190, "Los hilos de CPython 3.12 comparten un bloqueo global del intérprete: el cálculo en bytecode no se ejecuta en paralelo, pero la espera sí se solapa.", "gold", 13)
    f.box(700, 246, 240, 150, "Un proceso nuevo cuesta unos 240 ms al arrancar en Windows (medido); un hilo, unos 175 µs. El trabajo debe compensarlo.", "coral", 13)
    f.text(480, 452, "Mediana de 2 a 3 repeticiones, 8 CPU lógicas, CPython 3.12.9 en Windows. Los valores cambian con el equipo y la versión.", 12, "middle", 400, "#5c1f14")
    return f


# ---------------------------------------------------------------- SE-020
def se020_etapas() -> Fig:
    f = Fig(960, 470, "Las etapas reales para la línea total = price * 3 + tax en CPython 3.12",
            "Cuatro representaciones de la misma línea: tokens, árbol sintáctico, bytecode y ejecución. Cada una responde una pregunta distinta.")
    cols = [
        ("1 Tokens", "NAME total · OP = · NAME price · OP * · NUMBER 3 · OP + · NAME tax", "¿Qué unidades hay?", "teal"),
        ("2 AST", "Assign(total, BinOp(BinOp(price * 3) + tax))", "¿Cómo se agrupan? El producto se evalúa antes que la suma", "teal"),
        ("3 Bytecode", "LOAD_NAME price · LOAD_CONST 3 · BINARY_OP * · LOAD_NAME tax · BINARY_OP + · STORE_NAME total", "¿Qué hace la máquina virtual de CPython?", "gold"),
        ("4 Ejecución", "price y tax se buscan por nombre al ejecutar; si no existen, NameError", "¿Qué valores hay ahora?", "coral"),
    ]
    for i, (name, content, question, kind) in enumerate(cols):
        x = 14 + i * 236
        f.box(x, 20, 220, 46, name, "navy", 14, bold=True)
        f.box(x, 74, 220, 160, content, kind, 13)
        f.box(x, 242, 220, 70, question, "plain", 13, bold=True)
        if i < 3:
            f.arrow([(x + 220, 154), (x + 236, 154)])
    f.box(14, 332, 930, 56, "Con 2 * 3 + 4 el compilador pliega la constante: el bytecode contiene LOAD_CONST 10 y no hay multiplicación en tiempo de ejecución. "
          "Es una optimización que conserva la semántica.", "grey", 13)
    f.box(14, 398, 930, 56, "Nada de esto es código nativo: el bytecode lo ejecuta el intérprete de CPython, y su forma cambia entre versiones menores.", "coral", 13)
    return f


def se020_errores() -> Fig:
    f = Fig(960, 440, "En qué etapa aparece cada tipo de error",
            "Tres etapas: analizar y compilar, cargar y enlazar, ejecutar. Un error de sintaxis aparece antes de ejecutar nada aunque esté en una rama "
            "inalcanzable; un módulo inexistente falla al importarlo; un nombre indefinido falla al ejecutar la línea, no al definir la función.")
    stages = [
        ("Analizar y compilar", "SyntaxError", "compile() de un archivo con «x = = 1» dentro de if False falla antes de ejecutar nada.", "teal"),
        ("Cargar y enlazar", "ModuleNotFoundError", "El nombre se resuelve al importar. Un .pyc de otra versión se descarta y se regenera.", "gold"),
        ("Ejecutar", "NameError", "def f(): return nombre_inexistente compila sin error; falla solo cuando se llama a f().", "coral"),
    ]
    for i, (name, err, text, kind) in enumerate(stages):
        x = 20 + i * 308
        f.box(x, 30, 296, 46, name, "navy", 14, bold=True)
        f.box(x, 86, 296, 50, err, kind, 15, bold=True)
        f.box(x, 144, 296, 130, text, "plain", 13)
        if i < 2:
            f.arrow([(x + 296, 53), (x + 308, 53)])
    f.box(20, 296, 920, 56, "La etapa del error indica dónde buscar: sintaxis y estructura, resolución de dependencias y versiones, o datos y estado en ejecución.", "grey", 13)
    f.box(20, 362, 920, 56, "Un error que «no aparece» en las pruebas puede estar en una rama no ejecutada: compilar el archivo no valida lo que no se corre.", "coral", 13)
    return f


def se020_compilar_vs_cargar() -> Fig:
    f = Fig(900, 360, "Compilar el fuente frente a cargar el bytecode ya compilado",
            "Dos barras con una medición real: compilar 8 999 líneas de Python tardó 55,9 milisegundos y cargar el mismo código ya compilado "
            "con marshal tardó 1,8 milisegundos, unas 31 veces menos.")
    f.text(20, 28, "Mismo programa (9 000 líneas, 3 000 funciones), CPython 3.12.9, una medición", 14, "start", 700)
    items = [("compile(fuente)", 55.9, "gold"), ("marshal.loads(bytecode)", 1.8, "teal")]
    for i, (name, ms, kind) in enumerate(items):
        y = 56 + i * 80
        f.text(250, y + 28, name, 13, "end", 700)
        f.box(260, y + 6, ms * 9, 34, "", kind, radius=3)
        f.text(260 + ms * 9 + 8, y + 29, f"{ms:g} ms", 13, "start", 700)
    f.box(20, 232, 860, 100, "Por eso existen los archivos .pyc: guardan el bytecode para no recompilar en cada arranque. "
          "Incluyen un número mágico y la fecha o el hash del fuente; si no coinciden con la versión del intérprete, se regeneran. "
          "No son un artefacto portable entre versiones.", "grey", 13)
    return f


def se020_estrategias() -> Fig:
    f = Fig(960, 440, "Estrategias de traducción: no es «compilado» frente a «interpretado»",
            "Tabla de cuatro estrategias (compilación anticipada, intérprete simple, intérprete con especialización y compilación en ejecución) "
            "frente a arranque, rendimiento sostenido, portabilidad y qué observar al medir.")
    cols = ["Estrategia", "Arranque", "Rendimiento sostenido", "Qué decide la elección"]
    xs, ws = [10, 210, 400, 640], [195, 185, 235, 305]
    rows = [
        ("AOT (anticipada): C, Rust, Go", "Rápido: el código ya está generado", "Fijado al compilar; sin información de la ejecución", "Distribución por plataforma, tiempo de compilación, enlace"),
        ("Intérprete simple de bytecode", "Rápido: poco que preparar", "Bajo: cada operación pasa por el intérprete", "Portabilidad y facilidad de depuración"),
        ("Intérprete con especialización (CPython 3.11+)", "Rápido", "Mejora con el calentamiento: BINARY_OP_ADD_INT tras repetir sumas de enteros", "Mide fases por separado: arranque y estado estable"),
        ("JIT: JVM, motores de JavaScript", "Más lento: interpreta y compila rutas calientes", "Alto si hay perfil representativo y tiempo de vida", "Memoria, calentamiento y benchmarks que descarten el arranque"),
    ]
    for j, h in enumerate(cols):
        f.box(xs[j], 12, ws[j], 40, h, "navy", 13, bold=True)
    for i, row in enumerate(rows):
        y = 60 + i * 84
        for j, cell in enumerate(row):
            f.box(xs[j], y, ws[j], 76, cell, ["grey", "teal", "gold", "plain"][j], 12 if j else 13, bold=(j == 0))
    f.text(480, 410, "Un mismo lenguaje puede admitir varias estrategias; la clasificación es de la implementación y del momento, no del lenguaje.", 13, "middle")
    f.text(480, 430, "CPython 3.13 incluye un JIT experimental desactivado por defecto (PEP 744); verifica el estado en la versión que uses.", 12, "middle", 400, "#5c1f14")
    return f


FIGURES = {
    "se-019-estados-de-un-hilo.svg": se019_estados,
    "se-019-ruta-de-una-lectura.svg": se019_lectura,
    "se-019-hilos-y-procesos-medidos.svg": se019_medicion,
    "se-020-etapas-con-ejemplo.svg": se020_etapas,
    "se-020-errores-por-etapa.svg": se020_errores,
    "se-020-compilar-frente-a-cargar.svg": se020_compilar_vs_cargar,
    "se-020-estrategias-de-traduccion.svg": se020_estrategias,
}
