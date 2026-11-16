"""Figures for SE-085 to SE-090 (values measured or computed with CPython 3.12.9 on Windows 11; Linux 3.12.3 where noted)."""
from __future__ import annotations

import math

from figure_kit import Fig, _wrap, fmt_es, grouped_bars, heatmap, line_chart
from figure_cases import case_cards

MEDIDO = "Medido con CPython 3.12.9 en Windows 11; los tiempos dependen del equipo y se leen como razones."


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
    f.kind = "table"  # counted by tests/test_figure_redesign.py (ratchet towards zero)
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


# ---------------------------------------------------------------- SE-085
def se085_pop0() -> Fig:
    items = []
    for n, a, b in ((10000, 12.01, 0.68), (20000, 45.12, 1.55), (40000, 233.54, 3.08), (80000, 998.65, 5.92)):
        items.append((f"list.pop(0), n={n:,}".replace(",", " "), a, "coral", f"{a:g} ms"))
        items.append((f"deque.popleft(), n={n:,}".replace(",", " "), b, "teal", f"{b:g} ms"))
    return bars("Vaciar una cola de n elementos: list.pop(0) frente a deque.popleft()",
                "Barras con el tiempo de vaciar una cola de 10 000 a 80 000 elementos: la lista tarda 12, 45, 234 y 999 milisegundos y el deque 0,68, 1,55, 3,08 y 5,92 milisegundos.",
                items, 0.5, "Al duplicar n la lista multiplica su tiempo por 3,8, 5,2 y 4,3 (crecimiento cuadrático); el deque lo multiplica por 2,3, 2,0 y 1,9 (casi lineal). Con n = 80 000 la diferencia es de 169 veces.", label_w=270)


def se085_capacidad() -> Fig:
    datos = [(1, 88, 4), (5, 120, 8), (9, 184, 16), (17, 248, 24), (33, 376, 40), (65, 664, 76), (109, 1080, 128)]
    puntos = [(n, b, f"{fmt_es(b)} B · {c} ranuras", "l" if n == 109 else "r" if n == 1 else "b") for n, b, c in datos]
    return line_chart("Una lista reserva más capacidad de la que usa",
                      "Línea con el tamaño en bytes de una lista de CPython en cada redimensionado de list.append: sube por escalones de 88 bytes con 4 ranuras a 1080 bytes con 128 ranuras al pasar de 1 a 109 elementos, siempre con ranuras reservadas por encima de la longitud.",
                      [("sys.getsizeof al redimensionar", puntos, "teal")], x_label="Longitud de la lista al redimensionar", y_label="Tamaño (bytes)",
                      log_x=True, x_ticks=[(1, "1"), (5, "5"), (9, "9"), (17, "17"), (33, "33"), (65, "65"), (109, "109")],
                      note="128 llamadas a append provocaron solo 12 redimensionados. Un millón de enteros ocupa 8,0 MB en la lista, 36,0 MB contando los objetos int y 8,18 MB en array('q'): la lista guarda referencias, el arreglo guarda los valores.",
                      note_kind="gold", foot=MEDIDO)


def se085_vistas() -> Fig:
    return grouped_bars("Copias, vistas y recorridos: lo que cuesta cada decisión",
                        "Barras agrupadas en escala logarítmica con el tiempo de cuatro operaciones en Windows y Linux: copiar una rebanada de 50 MB tarda 15,8 y 36,1 milisegundos, una vista de memoria menos de un microsegundo, sumar un millón de enteros 9,8 y 9,5 milisegundos y recorrer un millón de nodos enlazados 91,0 y 58,1; la vista es la única que no copia.",
                        ["Rebanada de 50 MB (copia)", "memoryview del mismo bytearray (vista)", "sum() de 1 M de enteros", "Recorrer 1 M de nodos enlazados"],
                        [("Windows", [15.8, 0.0006, 9.8, 91.0], "teal"), ("Linux (WSL2)", [36.1, 0.0007, 9.5, 58.1], "coral")],
                        unit="ms", log=True, value_fmt=lambda v: fmt_es(v, 1) if v >= 1 else fmt_es(v, 4),
                        note="Tras escribir en el bytearray original, la vista muestra el cambio (aliasing: «Z» frente a «b») y la copia no. Con una vista viva, bytearray.extend falla con BufferError: «Existing exports of data».",
                        note_kind="coral", foot=MEDIDO)


# ---------------------------------------------------------------- SE-086
def se086_prioridad() -> Fig:
    ns = [2000, 4000, 8000, 16000]
    return line_chart("Tres maneras de implementar una cola de prioridad",
                      "Líneas en doble escala logarítmica con el tiempo de insertar y extraer n elementos entre 2000 y 16000: el montículo binario pasa de 0,6 a 11,2 milisegundos, la lista ordenada con bisect.insort de 2,9 a 59,4 y buscar el mínimo con min y remove de 43,6 a 3746; esta última es la más empinada.",
                      [("heapq (montículo)", list(zip(ns, [0.6, 1.4, 3.2, 11.2])), "teal"),
                       ("bisect.insort + pop", list(zip(ns, [2.9, 4.3, 16.9, 59.4])), "gold"),
                       ("min() + remove()", list(zip(ns, [43.6, 194.4, 833.3, 3746.4])), "coral")],
                      x_label="n elementos", y_label="Tiempo (ms)", log_x=True, log_y=True,
                      x_ticks=[(2000, "2 000"), (4000, "4 000"), (8000, "8 000"), (16000, "16 000")], y_ticks=[0.1, 1, 10, 100, 1000, 10000],
                      note="Al duplicar n, min()+remove() multiplica su tiempo por 4,5, 4,3 y 4,5 (cuadrático). El montículo no mantiene orden total: solo garantiza el mínimo en la raíz, y por eso es más barato que ordenar en cada inserción.",
                      note_kind="gold", foot=MEDIDO)


def se086_empates() -> Fig:
    f = Fig(940, 400, "Empates en una cola de prioridad: el orden de salida depende de la clave de desempate",
            "Se insertaron cinco tareas E, D, C, B, A con la misma prioridad. Con tuplas (prioridad, nombre) salen A B C D E, orden alfabético y no de llegada; con un contador intermedio (prioridad, contador, nombre) salen E D C B A, orden de llegada. Dos diccionarios como carga útil lanzan TypeError.")
    f.box(10, 14, 910, 44, "Entrada con prioridad igual, en este orden de llegada: E, D, C, B, A", "navy", 14, bold=True)
    f.box(10, 80, 440, 100, "heappush((1, nombre))\nSale: A B C D E\nDesempata por el texto, no por la llegada", "coral", 14)
    f.box(480, 80, 440, 100, "heappush((1, contador, nombre))\nSale: E D C B A\nDesempata por llegada: FIFO estable", "teal", 14)
    f.box(10, 200, 910, 74, "heappush((1, {'a': 1})) y luego heappush((1, {'b': 2})) lanza TypeError: '<' not supported between instances of 'dict' and 'dict'. La prioridad empata y Python intenta comparar la carga útil.", "gold", 13)
    f.box(10, 292, 910, 70, "Un contador monótono como segundo elemento hace el orden total, estable y determinista, y evita comparar cargas útiles que no se pueden ordenar.", "grey", 13)
    f.text(470, 386, MEDIDO, 12, "middle", 400, "#5c1f14")
    return f


def se086_comparaciones() -> Fig:
    return grouped_bars("Comparaciones del montículo: n inserciones y n extracciones",
                        "Barras agrupadas con el número de comparaciones contadas para n entre 1000 y 8000: n inserciones cuestan unas 2,2 n comparaciones (2212 a 18 300) y n extracciones 8703 a 93 390, entre 0,87 y 0,90 veces n por el logaritmo de n; extraer pesa cuatro o cinco veces más que insertar.",
                        ["n = 1 000", "n = 2 000", "n = 4 000", "n = 8 000"],
                        [("Insertar n", [2212, 4485, 9018, 18300], "teal"), ("Extraer n", [8703, 19342, 42666, 93390], "coral")],
                        unit="comparaciones",
                        note="Extraer / (n·log₂ n) vale 0,87, 0,88, 0,89 y 0,90. Insertar es casi lineal (cada elemento sube pocos niveles en promedio); extraer es n·log n porque cada elemento nuevo en la raíz baja por la altura del árbol. La recursión de 5 000 niveles falla con RecursionError (límite 1 000), mientras que una pila explícita procesó 1 000 000 de pasos sin problema.",
                        note_kind="teal", foot="Comparaciones contadas con __lt__ sobre datos aleatorios con semilla fija; no dependen del equipo.")


# ---------------------------------------------------------------- SE-087
def se087_colisiones() -> Fig:
    items = []
    for n, bad, good in ((500, 16.01, 0.39), (1000, 60.44, 0.27), (2000, 227.72, 0.53), (4000, 960.27, 3.48)):
        items.append((f"__hash__ = 1, n={n}", bad, "coral", f"{bad:g} ms"))
        items.append((f"hash(valor), n={n}", good, "teal", f"{good:g} ms"))
    return bars("Buscar n claves con un hash constante y con un hash razonable", "Barras con el tiempo de buscar n claves en un diccionario: con un __hash__ constante tarda 16, 60, 228 y 960 milisegundos para 500, 1000, 2000 y 4000 claves, y con hash(valor) 0,39, 0,27, 0,53 y 3,48 milisegundos.",
                items, 0.55, "Con hash constante, duplicar n multiplica el tiempo por 3,8, 3,8 y 4,2: cada búsqueda compara con todas las claves anteriores. Probar 500 pertenencias en una lista de 20 000 elementos tardó 93,7 ms y en un set 0,027 ms (3 500 veces menos) a costa de 4,2 MB frente a 0,8 MB por cada 100 000 enteros.", label_w=240)


def se087_sorpresas() -> Fig:
    return case_cards("Hash e igualdad: cinco sorpresas medidas",
                      "Cinco comprobaciones de hash e igualdad como tarjetas con su resultado: un set de cadenas cambia de orden con cinco de seis semillas, uno de enteros no cambia, hash de menos uno y menos dos coinciden, uno, uno punto cero y True son la misma clave, y NaN solo se encuentra con el mismo objeto.",
                      [("Orden de un set de 5 cadenas con 6 valores de PYTHONHASHSEED", "5 órdenes distintos", "El hash de str se aleatoriza por proceso.", "coral"),
                       ("Orden de un set de enteros con 3 valores de PYTHONHASHSEED", "1 solo orden", "El hash de int no se aleatoriza.", "teal"),
                       ("hash(-1) y hash(-2)", "ambos −2", "−1 está reservado como error en C: hay colisión.", "coral"),
                       ("{1: 'a', 1.0: 'b', True: 'c'}", "1 clave", "1 == 1.0 == True y tienen el mismo hash.", "coral"),
                       ("float('nan') in {nan: 1}", "True con el mismo objeto; False con otro nan", "NaN no es igual a sí mismo: la identidad rescata la búsqueda.", "gold")],
                      note="Ordenar por iteración de un set de cadenas no es reproducible entre procesos. Los diccionarios, en cambio, conservan el orden de inserción desde Python 3.7: tras borrar «b» y reinsertarla queda al final («acdeb»).",
                      note_kind="coral", foot=MEDIDO)


def se087_clave_mutada() -> Fig:
    f = Fig(940, 410, "Mutar una clave después de insertarla deja la entrada inalcanzable",
            "Se inserta la clave K(1) en un diccionario y luego se cambia su valor a 2. Buscar K(2) da False, buscar K(1) da False, el diccionario sigue teniendo un elemento y la iteración todavía devuelve la clave: la entrada existe pero no se puede encontrar.")
    f.box(10, 14, 280, 70, "1. d = {K(1): 'x'}\nel hash 1 elige la ranura", "teal", 14)
    f.arrow([(290, 49), (330, 49)])
    f.box(330, 14, 280, 70, "2. k.v = 2\nla clave cambia, la ranura no", "coral", 14)
    f.arrow([(610, 49), (650, 49)])
    f.box(650, 14, 270, 70, "3. buscar", "navy", 14, bold=True)
    f.box(10, 120, 290, 76, "K(2) in d → False\nhash 2 apunta a otra ranura", "gold", 14)
    f.box(325, 120, 290, 76, "K(1) in d → False\nla ranura tiene una clave que ya no es igual", "gold", 14)
    f.box(640, 120, 280, 76, "len(d) = 1 y for k in d la devuelve", "coral", 14)
    f.box(10, 220, 910, 70, "Las colecciones por hash exigen que el hash y la igualdad de una clave no cambien mientras la clave esté dentro. Por eso list, dict y set no son hashables (TypeError: unhashable type: 'list').", "grey", 13)
    f.box(10, 306, 910, 56, "Tras borrar 99 990 de 100 000 entradas, el tamaño del diccionario siguió en 5,24 MB: un dict no devuelve memoria al borrar.", "gold", 13)
    f.text(470, 392, MEDIDO, 12, "middle", 400, "#5c1f14")
    return f


# ---------------------------------------------------------------- SE-088
def se088_altura() -> Fig:
    return grouped_bars("Altura de un árbol según el orden de inserción",
                        "Barras agrupadas en escala logarítmica con la altura de un árbol binario de búsqueda para 255, 1000 y 4000 claves: con claves ordenadas la altura es n, con claves aleatorias 17, 26 y 30 y con un árbol AVL 8, 10 y 12, igual a log2 n.",
                        ["n = 255", "n = 1 000", "n = 4 000"],
                        [("BST, claves ordenadas", [255, 1000, 4000], "coral"), ("BST, claves aleatorias", [17, 26, 30], "gold"), ("AVL, claves ordenadas", [8, 10, 12], "teal")],
                        unit="altura (niveles)", log=True,
                        note="Comparaciones acumuladas: ordenado 32 385, 499 500 y 7 998 000; aleatorio 2 104, 11 562 y 56 801. Un BST es una lista enlazada cuando se alimenta en orden. Un AVL con 100 000 claves ordenadas llegó a altura 17 (cota teórica 23,9) a cambio de 99 983 rotaciones.",
                        note_kind="gold", foot="Alturas y comparaciones calculadas con semilla fija; no dependen del equipo.")


def se088_prefijos() -> Fig:
    return grouped_bars("Contar palabras con un prefijo: tres estructuras",
                        "Barras agrupadas en escala logarítmica con el tiempo de contar 39 palabras con el prefijo abc entre 28 785: recorrer todo tarda 6374 microsegundos en Windows y 3370 en Linux, el trie 30,9 y 28,9, y la lista ordenada con bisect 1,1 y 0,9; el trie ocupa 15,3 MB frente a 1,6 MB de la lista.",
                        ["Recorrer los 28 785 textos (startswith)", "Trie de diccionarios anidados", "Lista ordenada + bisect"],
                        [("Windows", [6374, 30.9, 1.1], "teal"), ("Linux (WSL2)", [3370, 28.9, 0.9], "coral")],
                        unit="µs", log=True,
                        note="El trie tuvo 82 553 nodos para 190 043 caracteres (43 %) y ocupó 15,3 MB frente a 1,6 MB de la lista, 9,6 veces más memoria. En CPython, bisect sobre una lista ordenada ganó al trie para contar prefijos; el trie conserva su valor cuando hace falta recorrer o completar por carácter.",
                        note_kind="coral", foot=MEDIDO)


def se088_profundidad() -> Fig:
    return case_cards("La altura manda: recursión, balanceo e invariante",
                      "Cuatro casos como tarjetas con su resultado: la inserción recursiva en un árbol de claves ordenadas falla con RecursionError, la iterativa funciona pero es cuadrática, un árbol AVL de 100 000 claves ordenadas tiene altura 17 y un montículo satisface el invariante padre menor o igual que hijo.",
                      [("Inserción recursiva en BST, 1 500 claves ordenadas, límite 1 000", "RecursionError", "La altura del árbol consume la pila de llamadas.", "coral"),
                       ("Misma inserción con bucle iterativo, 4 000 claves ordenadas", "Funciona (altura 4 000)", "Correcta pero cuadrática: 7 998 000 comparaciones.", "gold"),
                       ("AVL, 100 000 claves ordenadas", "Altura 17", "Cota 1,44·log₂(n+2) = 23,9; 99 983 rotaciones.", "teal"),
                       ("Montículo de 31 elementos tras heapify", "Invariante cumplido", "padre ≤ hijo en los 30 pares; índices (i−1)//2.", "teal")],
                      note="La altura no es un detalle de implementación: determina el costo de cada operación y el riesgo de agotar la pila. Un árbol correcto en pruebas con datos aleatorios puede romperse con datos ordenados.",
                      note_kind="gold", foot=MEDIDO)


# ---------------------------------------------------------------- SE-089
def se089_bfs_dfs() -> Fig:
    return grouped_bars("Rejilla: BFS encuentra el camino más corto, DFS encuentra uno cualquiera",
                        "Barras agrupadas en escala logarítmica con el largo del camino hallado en rejillas de 20, 40 y 80 de lado: la búsqueda en anchura devuelve 38, 78 y 158 pasos, que son los óptimos, y la búsqueda en profundidad 190, 780 y 3160, cinco, diez y veinte veces más largos.",
                        ["20 × 20", "40 × 40", "80 × 80"],
                        [("BFS = óptimo", [38, 78, 158], "teal"), ("DFS", [190, 780, 3160], "coral")],
                        unit="pasos del camino", log=True,
                        note="Nodos y aristas: 400 y 760, 1 600 y 3 120, 6 400 y 12 640; BFS visita todos los nodos y DFS 229, 859 y 3 319. El camino de DFS es 5, 10 y 20 veces más largo que el óptimo. Elegir entre ambos es elegir qué propiedad se necesita: mínima cantidad de aristas o simple alcanzabilidad.",
                        note_kind="teal", foot="Cuentas deterministas sobre rejillas sin obstáculos; no dependen del equipo.")


def se089_representacion() -> Fig:
    return line_chart("Representación del grafo y costo del recorrido",
                      "Línea en doble escala logarítmica con el tiempo de un recorrido BFS completo en rejillas de 4900, 19 800 y 79 600 aristas: 3,6, 12,4 y 39,2 milisegundos, de modo que al cuadruplicar las aristas el tiempo se multiplica por 3,5 y 3,2, como predice O(V+E).",
                      [("BFS completo sobre una rejilla", [(4900, 3.6, "3,6 ms", "t"), (19800, 12.4, "12,4 ms", "t"), (79600, 39.2, "39,2 ms", "t")], "teal")],
                      x_label="Aristas del grafo", y_label="Tiempo del BFS completo (ms)", log_x=True, log_y=True,
                      x_ticks=[(4900, "4 900 (50 × 50)"), (19800, "19 800 (100 × 100)"), (79600, "79 600 (200 × 200)")], y_ticks=[1, 10, 100],
                      note="Para 2 000 nodos y 7 993 aristas, la lista de adyacencia ocupa ≈ 360 KB y dar los vecinos de un nodo tarda 0,3 µs; la matriz (bytearray por fila, 4 000 000 de celdas) ocupa ≈ 4,1 MB y tarda 135,9 µs. La matriz paga V² celdas aunque el grafo sea disperso (0,4 % de ocupación).",
                      note_kind="gold", foot=MEDIDO)


def se089_pesos() -> Fig:
    return case_cards("Cuando el recorrido correcto deja de serlo",
                      "Cinco casos en que una precondición del grafo se rompe, como tarjetas con el resultado: BFS minimiza saltos pero no costo, Dijkstra falla con aristas negativas y Bellman-Ford no, un recorrido sin conjunto de visitados no termina, una pared parte la rejilla en dos componentes y el DFS recursivo agota la pila.",
                      [("Aristas con costos 10 (A→B) o 1+1+1 (A→C→D→B)", "BFS: 1 salto, costo real 10", "Dijkstra encuentra el costo 3.", "coral"),
                       ("Arista negativa (C→B = −2) y B→D = 3", "Dijkstra con nodos cerrados: D = 5", "Bellman-Ford da D = 4.", "coral"),
                       ("Recorrido sin conjunto de visitados en una rejilla de 25 nodos", "100 000 expansiones (corté por tope)", "Con visitados bastan 25 expansiones.", "coral"),
                       ("Rejilla de 6×6 con una pared completa", "2 componentes conexas", "Sin pared hay 1 componente.", "gold"),
                       ("DFS recursivo sobre una cadena de 5 001 nodos", "RecursionError", "Con pila explícita funciona.", "coral")],
                      note="Cada algoritmo trae una precondición sobre el grafo: pesos no negativos para Dijkstra, ausencia de ciclos negativos para Bellman-Ford. Un resultado «razonable» con la precondición violada es el peor fallo porque no avisa.",
                      note_kind="coral", foot="Cuentas deterministas; no dependen del equipo.")


# ---------------------------------------------------------------- SE-090
def se090_comparaciones() -> Fig:
    return heatmap("Comparaciones contadas con 800 elementos",
                   "Mapa de calor con las comparaciones de cuatro algoritmos de ordenación con 800 elementos según la entrada: sorted usa 6655 con datos aleatorios y 799 con ordenados o invertidos; inserción 157 960, 799 y 319 600; mezcla 6695, 3728 y 4048; quicksort con el primer elemento como pivote 16 284, 639 200 y 639 200; las celdas oscuras son las cuadráticas.",
                   ["sorted (Timsort)", "Inserción", "Mezcla (merge)", "Quicksort, pivote = primero"], ["Aleatoria", "Ya ordenada", "Invertida"],
                   [[6655, 799, 799], [157960, 799, 319600], [6695, 3728, 4048], [16284, 639200, 639200]],
                   unit="comparaciones", scale="coral", highlight=[(1, 0), (1, 2), (3, 1), (3, 2)],
                   note="Referencia: n·log₂ n = 7 715 y n(n−1)/2 = 319 600. El quicksort con pivote ingenuo se vuelve cuadrático justo con la entrada «ya ordenada», la más común en la práctica; Timsort aprovecha el orden existente y usa n−1 comparaciones. Contorno: casos cuadráticos.",
                   note_kind="coral", foot="Comparaciones contadas con __lt__ y semilla fija; no dependen del equipo.")


def se090_timsort() -> Fig:
    return grouped_bars("sorted() sobre datos aleatorios, ordenados e invertidos",
                        "Barras agrupadas con el tiempo de sorted con 100 000 y 200 000 flotantes: aleatorios 22,9 y 55,5 milisegundos, ya ordenados 1,87 y 5,19, invertidos 2,31 y 5,91; los datos con tramos ordenados son unas diez veces más rápidos.",
                        ["n = 100 000", "n = 200 000"],
                        [("Aleatoria", [22.9, 55.5], "coral"), ("Ya ordenada", [1.87, 5.19], "teal"), ("Invertida", [2.31, 5.91], "gold")],
                        unit="ms",
                        note="Timsort detecta tramos ya ordenados («runs») y los mezcla: los datos ordenados o invertidos fueron 12 y 10 veces más rápidos. La búsqueda binaria necesitó 10, 20 y 30 pasos para 10³, 10⁶ y 10⁹ elementos. Mediana de 100 000 números: sorted()[n//2] tardó 22,3 ms, un quickselect en Python puro 40,8 ms (promedio 2,3 pasadas por elemento) y heapq.nsmallest(1) 1,32 ms para el mínimo.",
                        note_kind="gold", foot=MEDIDO)


def se090_trampas() -> Fig:
    return case_cards("Cuatro comportamientos de sorted() que conviene conocer",
                      "Cuatro resultados de sorted como tarjetas: la ordenación es estable, una lista con NaN queda sin ordenar, mezclar enteros y cadenas lanza TypeError y las cadenas se ordenan por punto de código de modo que Árbol queda después de zeta.",
                      [("sorted(registros, key=prioridad)", "['c','e','b','a','d']", "Estable: los empates conservan el orden de llegada.", "teal"),
                       ("sorted([3.0, nan, 1.0, 2.0])", "[3.0, nan, 1.0, 2.0]", "NaN rompe el orden total: no ordena nada.", "coral"),
                       ("sorted([1, 'a'])", "TypeError", "No hay orden entre str e int.", "coral"),
                       ("sorted(['Zebra','apple','Árbol','zeta'])", "['Zebra','apple','zeta','Árbol']", "Orden por punto de código, no alfabético del idioma.", "gold")],
                      note="Un comparador que no define un orden total (NaN, prioridades inconsistentes) no produce un error: produce un resultado arbitrario. La estabilidad permite ordenar por varias claves aplicando sorts sucesivos de la clave menos a la más significativa.",
                      note_kind="coral", foot="Resultados deterministas de CPython 3.12; no dependen del equipo.")


FIGURES = {
    "se-085-pop0-frente-a-deque.svg": se085_pop0,
    "se-085-capacidad-y-reserva.svg": se085_capacidad,
    "se-085-vistas-copias-y-recorridos.svg": se085_vistas,
    "se-086-colas-de-prioridad.svg": se086_prioridad,
    "se-086-empates-y-estabilidad.svg": se086_empates,
    "se-086-comparaciones-del-monticulo.svg": se086_comparaciones,
    "se-087-colisiones-y-pertenencia.svg": se087_colisiones,
    "se-087-hash-e-igualdad.svg": se087_sorpresas,
    "se-087-clave-mutada.svg": se087_clave_mutada,
    "se-088-altura-segun-el-orden.svg": se088_altura,
    "se-088-prefijos-trie-y-bisect.svg": se088_prefijos,
    "se-088-profundidad-y-balanceo.svg": se088_profundidad,
    "se-089-bfs-frente-a-dfs.svg": se089_bfs_dfs,
    "se-089-representacion-del-grafo.svg": se089_representacion,
    "se-089-pesos-negativos-y-visitados.svg": se089_pesos,
    "se-090-comparaciones-por-algoritmo.svg": se090_comparaciones,
    "se-090-timsort-y-seleccion.svg": se090_timsort,
    "se-090-trampas-del-orden.svg": se090_trampas,
}
