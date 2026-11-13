"""Figures for SE-021 and SE-022."""
from __future__ import annotations

from figure_kit import Fig


# ---------------------------------------------------------------- SE-021
def se021_ciclos() -> Fig:
    f = Fig(960, 470, "Conteo de referencias y un ciclo que solo recupera el recolector de ciclos",
            "Tres paneles. A: dos objetos que se referencian mutuamente tienen conteo 2 cada uno (un nombre y el otro objeto). "
            "B: al borrar los nombres cada conteo baja a 1 pero ya nadie alcanza el ciclo. "
            "C: gc.collect() detecta los dos objetos inalcanzables y los libera.")
    panels = [("A · Con nombres", "2", "2", True, "teal"), ("B · Tras del a, b", "1", "1", False, "gold"), ("C · Tras gc.collect()", "—", "—", False, "grey")]
    for i, (title, ca, cb, names, kind) in enumerate(panels):
        x = 20 + i * 310
        f.text(x + 140, 28, title, 14, "middle", 700)
        if i < 2:
            f.box(x + 20, 120, 100, 56, f"objeto A\nconteo = {ca}", kind, 13, bold=True)
            f.box(x + 170, 120, 100, 56, f"objeto B\nconteo = {cb}", kind, 13, bold=True)
            f.arrow([(x + 120, 138), (x + 170, 138)])
            f.arrow([(x + 170, 160), (x + 120, 160)])
            if names:
                f.box(x + 20, 50, 100, 34, "nombre a", "plain", 13)
                f.box(x + 170, 50, 100, 34, "nombre b", "plain", 13)
                f.arrow([(x + 70, 84), (x + 70, 120)])
                f.arrow([(x + 220, 84), (x + 220, 120)])
            else:
                f.text(x + 145, 76, "sin nombres que apunten al ciclo", 13, "middle", 400, "#5c1f14")
        else:
            f.box(x + 20, 120, 250, 56, "memoria liberada", "grey", 14, bold=True, dashed=True)
        f.box(x, 200, 290, 96, ["Cada objeto es alcanzable desde un nombre y desde el otro objeto.",
                                "Los conteos no llegan a cero, pero el ciclo ya no es alcanzable desde ninguna raíz: es memoria perdida para el programa.",
                                "En una ejecución de ejemplo gc.collect() devolvió 2: los dos objetos del ciclo."][i], "plain", 13)
    f.box(20, 320, 920, 56, "El conteo de referencias libera al instante cuando llega a cero; no basta para ciclos. CPython añade un recolector generacional "
          "que se activa por umbrales (en 3.12, (700, 10, 10)).", "teal", 13)
    f.box(20, 386, 920, 56, "El recolector prueba inalcanzabilidad, no «utilidad»: una referencia olvidada conserva un objeto legítimamente, y eso no es un fallo del recolector.", "coral", 13)
    return f


def se021_retencion() -> Fig:
    f = Fig(940, 440, "Conservar todos los eventos frente a procesarlos en flujo",
            "Dos paneles con una medición real: la memoria máxima de Python crece con el tamaño si se conservan los eventos "
            "(2,7, 27,3 y 274,3 megabytes con diez mil, cien mil y un millón) y es despreciable al procesarlos en flujo; el tiempo también es menor en flujo.")
    f.text(20, 28, "Memoria máxima de Python (tracemalloc)", 14, "start", 700)
    rows = [("10 000", 2.7, 0.0), ("100 000", 27.3, 0.0), ("1 000 000", 274.3, 0.0)]
    for i, (n, mat, st) in enumerate(rows):
        y = 48 + i * 62
        f.text(110, y + 22, n, 13, "end", 700)
        f.box(120, y, max(mat * 1.7, 4), 22, "", "coral", radius=3)
        f.text(120 + max(mat * 1.7, 4) + 8, y + 17, f"{mat:g} MB (lista de eventos)", 12, "start", 700)
        f.box(120, y + 26, 4, 22, "", "teal", radius=3)
        f.text(132, y + 43, "< 0,1 MB (en flujo)", 12, "start", 700)
    f.text(20, 270, "Tiempo de pared, mediana (s)", 14, "start", 700)
    times = [("10 000", 0.015, 0.014), ("100 000", 0.168, 0.115), ("1 000 000", 1.776, 1.337)]
    for i, (n, mat, st) in enumerate(times):
        y = 286 + i * 44
        f.text(110, y + 20, n, 13, "end", 700)
        f.box(120, y, mat * 150 + 4, 18, "", "coral", radius=3)
        f.text(120 + mat * 150 + 12, y + 14, f"{mat:g} s", 12, "start", 700)
        f.box(120, y + 20, st * 150 + 4, 18, "", "teal", radius=3)
        f.text(120 + st * 150 + 12, y + 34, f"{st:g} s", 12, "start", 700)
    f.box(640, 48, 290, 140, "Rojo = conservar todos los eventos en una lista. Verde azulado = procesar uno por vez. Mismo resultado: la misma suma y el mismo conteo en ambos.", "grey", 13)
    f.box(640, 204, 290, 150, "Con un millón de eventos la versión que conserva tuvo una ejecución de 3,1 s frente a una mediana de 1,8 s: la presión de memoria añade variación.", "gold", 13)
    f.text(470, 430, "CPython 3.12.9 en Windows; 3 a 7 repeticiones. tracemalloc mide solo la memoria que gestiona Python.", 12, "middle", 400, "#5c1f14")
    return f


def se021_pila_heap() -> Fig:
    f = Fig(940, 470, "Marcos de la pila y objetos del heap: vidas distintas",
            "Pila con tres marcos (principal, resumir, analizar) cuyas variables apuntan a objetos del heap. "
            "Al retornar analizar su marco desaparece, pero el diccionario que creó sigue vivo porque una lista global lo referencia.")
    f.text(20, 26, "Pila de llamadas (vida = la de la llamada)", 14, "start", 700)
    frames = [("marco: analizar(linea)", "linea · evento", 60), ("marco: resumir(valores)", "valores · total", 142), ("marco: principal()", "eventos_global", 224)]
    for name, localv, y in frames:
        f.box(20, y, 300, 72, "", "navy" if y == 60 else "grey")
        f.text(34, y + 26, name, 13, "start", 700, "#ffffff" if y == 60 else "#142231")
        f.text(34, y + 50, localv, 13, "start", 400, "#ffffff" if y == 60 else "#142231")
    f.text(520, 26, "Heap (vida = mientras sea alcanzable)", 14, "start", 700)
    f.box(520, 60, 180, 56, "dict evento #1", "teal", 13, bold=True)
    f.box(520, 142, 180, 56, "dict evento #2", "teal", 13, bold=True)
    f.box(760, 224, 160, 56, "list eventos_global", "gold", 13, bold=True)
    f.arrow([(320, 96), (520, 90)], "evento", label_at=(420, 84))
    f.arrow([(760, 252), (700, 180)], dashed=True)
    f.arrow([(760, 244), (700, 100)], dashed=True)
    f.arrow([(320, 262), (760, 262)], "referencia global", label_at=(540, 254))
    f.box(20, 320, 440, 110, "Cuando analizar() retorna, su marco desaparece y el nombre «evento» deja de existir. El objeto, en cambio, vive en el heap: "
          "sigue alcanzable desde la lista global.", "grey", 13)
    f.box(480, 320, 440, 110, "La memoria crece por referencias que se conservan, no por un fallo del recolector. Para liberar, se elimina la referencia "
          "(o se procesa en flujo); forzar gc.collect() no cambia la alcanzabilidad.", "coral", 13)
    return f


# ---------------------------------------------------------------- SE-022
def se022_amdahl() -> Fig:
    f = Fig(940, 470, "Límite de acelerar una fracción del trabajo (ley de Amdahl)",
            "Gráfico de líneas: si una fracción p del tiempo se acelera por un factor s, el beneficio total es 1 sobre (1 menos p más p dividido s). "
            "Con s infinito el máximo para p = 0,2 es 1,25; para p = 0,9 es 10. Con s = 10 los valores son 1,22 y 5,26.")
    ps = [0.2, 0.4, 0.6, 0.8, 0.9, 0.95]
    inf = [1 / (1 - p) for p in ps]
    ten = [1 / ((1 - p) + p / 10) for p in ps]
    x0, base, h, wid = 90, 330, 240, 480
    f.line(x0, base, x0 + wid, base, "#32505f", width=1.8)
    f.line(x0, 70, x0, base, "#32505f", width=1.8)
    f.text(x0 + 8, 62, "aceleración total", 13, "start")
    def X(i):
        return x0 + 40 + i * 85
    def Y(v):
        return base - min(v, 10) / 10 * h
    f.arrow([(X(i), Y(v)) for i, v in enumerate(inf)], color="#c0432f")
    f.arrow([(X(i), Y(v)) for i, v in enumerate(ten)], dashed=True, color="#087f8c")
    for i, p in enumerate(ps):
        f.text(X(i), base + 20, f"{p:g}", 13)
        f.text(X(i), Y(ten[i]) + 20, f"{ten[i]:.2f}".replace(".", ","), 12, "middle", 700, "#0b3f45")
        label = f"{inf[i]:.2f}".replace(".", ",") if inf[i] < 10 else f"{inf[i]:.0f}"
        f.text(X(i), Y(inf[i]) - 10, label, 12, "middle", 700, "#5c1f14")
    f.text(x0 + wid / 2, base + 46, "fracción p del tiempo que se acelera", 13, "middle")
    f.text(X(5) + 4, 66, "20 (recortado)", 11, "middle", 400, "#5c1f14")
    f.box(600, 70, 320, 70, "Línea continua roja: s infinito (se elimina esa parte).", "coral", 13)
    f.box(600, 152, 320, 70, "Línea discontinua azul: s = 10 (esa parte diez veces más rápida).", "teal", 13)
    f.box(600, 234, 320, 130, "Acelerar una fracción del 20 % nunca da más de 1,25 veces, aunque se elimine. Primero se perfila para saber dónde está el tiempo.", "gold", 13)
    f.text(470, 440, "Cálculo directo de la fórmula; no es una medición. El gráfico recorta el eje en 10.", 12, "middle", 400, "#5c1f14")
    return f


def se022_comparacion() -> Fig:
    f = Fig(940, 430, "Materializar frente a flujo: tiempo, variación y memoria",
            "Tabla con la medición real de dos implementaciones del mismo cálculo para tres tamaños: tiempo mediano, rango entre mínimo y máximo y memoria máxima de Python. "
            "Ambas producen el mismo resultado.")
    heads = ["Eventos", "Versión", "Mediana", "Mínimo–máximo", "CPU", "Memoria máx."]
    xs, ws = [10, 130, 290, 410, 590, 700], [115, 155, 115, 175, 105, 125]
    rows = [
        ("10 000", "materializa", "0,015 s", "0,014–0,017 s", "0,016 s", "2,7 MB"),
        ("10 000", "flujo", "0,014 s", "0,013–0,018 s", "0,016 s", "< 0,1 MB"),
        ("100 000", "materializa", "0,168 s", "0,152–0,195 s", "0,172 s", "27,3 MB"),
        ("100 000", "flujo", "0,115 s", "0,111–0,120 s", "0,109 s", "< 0,1 MB"),
        ("1 000 000", "materializa", "1,776 s", "1,424–3,144 s", "1,734 s", "274,3 MB"),
        ("1 000 000", "flujo", "1,337 s", "1,282–1,726 s", "1,297 s", "< 0,1 MB"),
    ]
    for j, h in enumerate(heads):
        f.box(xs[j], 10, ws[j], 36, h, "navy", 12, bold=True)
    for i, row in enumerate(rows):
        y = 52 + i * 44
        for j, cell in enumerate(row):
            kind = "coral" if row[1] == "materializa" and j == 5 else ("teal" if row[1] == "flujo" and j == 5 else "plain")
            f.box(xs[j], y, ws[j], 40, cell, kind, 12, bold=(j in (1, 2)))
    f.box(10, 324, 820, 56, "Mismo resultado en ambas (hash y conteo iguales). Con un millón, el rango de la versión que materializa llega a 3,1 s: la mediana sola esconde esa variación.", "gold", 13)
    f.text(420, 408, "CPython 3.12.9, Windows; 3 a 7 repeticiones por celda. La energía no se midió.", 12, "middle", 400, "#5c1f14")
    return f


def se022_cola() -> Fig:
    f = Fig(900, 440, "Promedio, mediana y cola de una distribución de latencias (datos sintéticos)",
            "Cien peticiones sintéticas: 95 tardan 10 ms y 5 tardan 500 ms. La mediana es 10 ms, el promedio 34,5 ms y el percentil 99 es 500 ms. "
            "Ningún valor único describe la experiencia de todas las personas.")
    f.text(20, 28, "Cien peticiones: cuántas tardan cada tiempo", 14, "start", 700)
    base = 330
    f.line(80, base, 700, base, "#32505f", width=1.8)
    f.line(80, 60, 80, base, "#32505f", width=1.8)
    f.box(140, base - 95 * 2.5, 90, 95 * 2.5, "", "teal", radius=3)
    f.text(185, base - 95 * 2.5 - 8, "95 peticiones", 13, "middle", 700)
    f.text(185, base + 20, "10 ms", 13, "middle", 700)
    f.box(560, base - 5 * 2.5, 90, 5 * 2.5, "", "coral", radius=3)
    f.text(605, base - 5 * 2.5 - 8, "5 peticiones", 13, "middle", 700)
    f.text(605, base + 20, "500 ms", 13, "middle", 700)
    marks = [("mediana 10 ms", 185, "#087f8c"), ("promedio 34,5 ms", 230, "#a8761a"), ("p99 500 ms", 605, "#c0432f")]
    for label, x, color in marks:
        f.line(x, 70, x, base, color, dashed=True, width=1.6)
    f.text(190, 86, "mediana 10 ms", 13, "start", 700, "#0b3f45")
    f.text(236, 108, "promedio 34,5 ms", 13, "start", 700, "#4a3209")
    f.text(596, 86, "p99 500 ms", 13, "end", 700, "#5c1f14")
    f.box(20, 372, 860, 56, "El promedio no coincide con ninguna petición real. Una de cada veinte personas espera 50 veces más: la cola, no la media, define la experiencia.", "grey", 13)
    return f


def se022_energia() -> Fig:
    f = Fig(900, 400, "Más rápido no implica menos energía: un ejemplo hipotético",
            "Dos versiones hipotéticas: A tarda 10 segundos con 25 vatios (250 julios) y B tarda 14 segundos con 15 vatios (210 julios). "
            "B es más lenta y consume menos energía en este supuesto; la energía es potencia por tiempo.")
    f.text(20, 28, "Energía = potencia media × tiempo (valores supuestos, no medidos)", 14, "start", 700)
    items = [("Versión A: 10 s × 25 W", 250, "coral"), ("Versión B: 14 s × 15 W", 210, "teal")]
    for i, (name, j, kind) in enumerate(items):
        y = 56 + i * 90
        f.text(250, y + 30, name, 13, "end", 700)
        f.box(260, y + 6, j * 2.4, 40, "", kind, radius=3)
        f.text(260 + j * 2.4 + 8, y + 32, f"{j} J", 13, "start", 700)
    f.box(20, 240, 860, 70, "Medir solo el tiempo no entrega julios. Para energía hace falta un medidor de potencia o un contador fiable; "
          "sin él se reporta tiempo y recursos observados y se declara «energía no medida».", "gold", 13)
    f.box(20, 322, 860, 60, "Intensidad de software (SCI): ((E × I) + M) por unidad funcional R, con E energía, I intensidad de carbono de la red y M carbono incorporado del hardware.", "grey", 13)
    return f


FIGURES = {
    "se-021-conteo-y-ciclos.svg": se021_ciclos,
    "se-021-retencion-frente-a-flujo.svg": se021_retencion,
    "se-021-pila-y-heap.svg": se021_pila_heap,
    "se-022-ley-de-amdahl.svg": se022_amdahl,
    "se-022-materializar-frente-a-flujo.svg": se022_comparacion,
    "se-022-promedio-y-cola.svg": se022_cola,
    "se-022-tiempo-no-es-energia.svg": se022_energia,
}
