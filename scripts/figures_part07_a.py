"""Figures for SE-085 to SE-090 (values measured or computed with CPython 3.12.9 on Windows 11; Linux 3.12.3 where noted)."""
from __future__ import annotations

import math

from figure_kit import Fig, _wrap

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
    rows = [["1", "88 B", "4 ranuras"], ["5", "120 B", "8 ranuras"], ["9", "184 B", "16 ranuras"], ["17", "248 B", "24 ranuras"],
            ["33", "376 B", "40 ranuras"], ["65", "664 B", "76 ranuras"], ["109", "1 080 B", "128 ranuras"]]
    return tab("Una lista reserva más capacidad de la que usa", "Tabla de los puntos de redimensionado de list.append: con 1, 5, 9, 17, 33, 65 y 109 elementos el tamaño en bytes salta a 88, 120, 184, 248, 376, 664 y 1080, con capacidades de 4 a 128 ranuras; 128 appends producen doce redimensionados.",
               ["Longitud al crecer", "sys.getsizeof", "Capacidad implícita"], rows, [260, 270, 380], row_h=40,
               note="128 llamadas a append provocaron solo 12 redimensionados. Un millón de enteros ocupa 8,0 MB en la lista, 36,0 MB contando los objetos int y 8,18 MB en array('q'): la lista guarda referencias, el arreglo guarda los valores.", note_kind="gold")


def se085_vistas() -> Fig:
    rows = [["bytearray de 50 MB: rebanada que copia", "15,8 ms", "36,1 ms", "Copia 50 MB cada vez"],
            ["memoryview del mismo bytearray", "0,0006 ms", "0,0007 ms", "Vista: no copia, pero bloquea el redimensionado"],
            ["sum() de una lista de 1 M de enteros", "9,8 ms", "9,5 ms", "Bucle en C sobre referencias contiguas"],
            ["Recorrer 1 M de nodos enlazados en Python", "91,0 ms", "58,1 ms", "Un salto de puntero por nodo"]]
    return tab("Copias, vistas y recorridos: lo que cuesta cada decisión", "Cuatro filas con tiempos en Windows y Linux: copiar una rebanada de 50 MB tarda 15,8 y 36,1 milisegundos, una vista de memoria menos de un microsegundo, sumar un millón de enteros en una lista 9,8 y 9,5 milisegundos y recorrer una lista enlazada de un millón de nodos 91,0 y 58,1.",
               ["Operación", "Windows", "Linux (WSL2)", "Lectura"], rows, [330, 130, 140, 330], row_h=62,
               note="Tras escribir en el bytearray original, la vista muestra el cambio (aliasing: «Z» frente a «b») y la copia no. Con una vista viva, bytearray.extend falla con BufferError: «Existing exports of data».", note_kind="coral")


# ---------------------------------------------------------------- SE-086
def se086_prioridad() -> Fig:
    rows = [["2 000", "0,6 ms", "2,9 ms", "43,6 ms"], ["4 000", "1,4 ms", "4,3 ms", "194,4 ms"], ["8 000", "3,2 ms", "16,9 ms", "833,3 ms"], ["16 000", "11,2 ms", "59,4 ms", "3 746,4 ms"]]
    return tab("Tres maneras de implementar una cola de prioridad", "Tabla de tiempos para insertar y extraer n elementos: el montículo binario tarda 0,6 a 11,2 milisegundos, la lista ordenada con bisect.insort 2,9 a 59,4 y buscar el mínimo con min y remove 43,6 a 3746 milisegundos entre 2000 y 16000 elementos.",
               ["n elementos", "heapq (montículo)", "bisect.insort + pop", "min() + remove()"], rows, [190, 230, 250, 240], row_h=46,
               note="Al duplicar n, min()+remove() multiplica su tiempo por 4,5, 4,3 y 4,5 (cuadrático). El montículo no mantiene orden total: solo garantiza el mínimo en la raíz, y por eso es más barato que ordenar en cada inserción.", note_kind="gold")


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
    rows = [["1 000", "2 212", "8 703", "0,87"], ["2 000", "4 485", "19 342", "0,88"], ["4 000", "9 018", "42 666", "0,89"], ["8 000", "18 300", "93 390", "0,90"]]
    return tab("Comparaciones del montículo: n inserciones y n extracciones", "Tabla con el número de comparaciones contadas: n inserciones cuestan unas 2,2 n comparaciones (2212 a 18 300) y n extracciones cuestan 8703 a 93 390, entre 0,87 y 0,90 veces n por el logaritmo de n.",
               ["n", "Comparaciones al insertar n", "Comparaciones al extraer n", "Extraer / (n·log₂ n)"], rows, [140, 270, 270, 240], row_h=44,
               note="Insertar es casi lineal (cada elemento sube pocos niveles en promedio); extraer es n·log n porque cada elemento nuevo en la raíz baja por la altura del árbol. La recursión de 5 000 niveles falla con RecursionError (límite 1 000), mientras que una pila explícita procesó 1 000 000 de pasos sin problema.", note_kind="teal", foot="Comparaciones contadas con __lt__ sobre datos aleatorios con semilla fija; no dependen del equipo.")


# ---------------------------------------------------------------- SE-087
def se087_colisiones() -> Fig:
    items = []
    for n, bad, good in ((500, 16.01, 0.39), (1000, 60.44, 0.27), (2000, 227.72, 0.53), (4000, 960.27, 3.48)):
        items.append((f"__hash__ = 1, n={n}", bad, "coral", f"{bad:g} ms"))
        items.append((f"hash(valor), n={n}", good, "teal", f"{good:g} ms"))
    return bars("Buscar n claves con un hash constante y con un hash razonable", "Barras con el tiempo de buscar n claves en un diccionario: con un __hash__ constante tarda 16, 60, 228 y 960 milisegundos para 500, 1000, 2000 y 4000 claves, y con hash(valor) 0,39, 0,27, 0,53 y 3,48 milisegundos.",
                items, 0.55, "Con hash constante, duplicar n multiplica el tiempo por 3,8, 3,8 y 4,2: cada búsqueda compara con todas las claves anteriores. Probar 500 pertenencias en una lista de 20 000 elementos tardó 93,7 ms y en un set 0,027 ms (3 500 veces menos) a costa de 4,2 MB frente a 0,8 MB por cada 100 000 enteros.", label_w=240)


def se087_sorpresas() -> Fig:
    rows = [["Orden de un set de 5 cadenas, 6 valores de PYTHONHASHSEED", "5 órdenes distintos", "El hash de str se aleatoriza por proceso"],
            ["Orden de un set de enteros, 3 valores de PYTHONHASHSEED", "1 solo orden", "El hash de int no se aleatoriza"],
            ["hash(-1) y hash(-2)", "ambos −2", "−1 está reservado como error en C: hay colisión"],
            ["{1: 'a', 1.0: 'b', True: 'c'}", "1 clave", "1 == 1.0 == True y tienen el mismo hash"],
            ["float('nan') in {nan: 1}", "True con el mismo objeto; False con otro nan", "NaN no es igual a sí mismo: la identidad rescata la búsqueda"]]
    return tab("Hash e igualdad: cinco sorpresas medidas", "Tabla de cinco comprobaciones: un set de cadenas cambia de orden con cinco de seis semillas, uno de enteros no cambia, hash de menos uno y menos dos coinciden, uno, uno punto cero y True son la misma clave, y NaN solo se encuentra con el mismo objeto.",
               ["Comprobación", "Resultado", "Causa"], rows, [380, 250, 300], row_h=62,
               note="Ordenar por iteración de un set de cadenas no es reproducible entre procesos. Los diccionarios, en cambio, conservan el orden de inserción desde Python 3.7: tras borrar «b» y reinsertarla queda al final («acdeb»).", note_kind="coral")


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
    rows = [["255", "255 / 32 385", "17 / 2 104", "8", "8,0"], ["1 000", "1 000 / 499 500", "26 / 11 562", "10", "10,0"], ["4 000", "4 000 / 7 998 000", "30 / 56 801", "12", "12,0"]]
    return tab("Altura de un árbol según el orden de inserción", "Tabla de alturas y comparaciones acumuladas de un árbol binario de búsqueda sin balanceo: con claves ordenadas la altura es n (255, 1000, 4000) y las comparaciones suman 32 385, 499 500 y 7 998 000; con claves aleatorias la altura es 17, 26 y 30; un árbol AVL da 8, 10 y 12.",
               ["n", "BST ordenado: altura / comparaciones", "BST aleatorio: altura / comparaciones", "AVL ordenado: altura", "log₂ n"], rows, [100, 280, 270, 170, 100], row_h=54,
               note="Un BST es una lista enlazada cuando se alimenta en orden. Un AVL con 100 000 claves ordenadas llegó a altura 17 (cota teórica 23,9) a cambio de 99 983 rotaciones.", note_kind="gold", foot="Alturas y comparaciones calculadas con semilla fija; no dependen del equipo.")


def se088_prefijos() -> Fig:
    rows = [["Recorrer los 28 785 textos (startswith)", "6 374 µs", "3 370 µs", "Lineal en el número de textos"],
            ["Trie de diccionarios anidados", "30,9 µs", "28,9 µs", "Proporcional al prefijo y a las coincidencias"],
            ["Lista ordenada + bisect", "1,1 µs", "0,9 µs", "Dos búsquedas binarias, sin recorrer"]]
    return tab("Contar palabras con un prefijo: tres estructuras", "Tabla de tiempos para contar 39 palabras con el prefijo abc entre 28 785: el recorrido tarda 6374 microsegundos en Windows y 3370 en Linux, el trie 30,9 y 28,9, y la lista ordenada con bisect 1,1 y 0,9. El trie ocupa 15,3 MB frente a 1,6 MB de la lista.",
               ["Estructura", "Windows", "Linux (WSL2)", "Lectura"], rows, [360, 130, 140, 300], row_h=52,
               note="El trie tuvo 82 553 nodos para 190 043 caracteres (43 %) y ocupó 9,6 veces más memoria que la lista de textos. En CPython, bisect sobre una lista ordenada ganó al trie para contar prefijos; el trie conserva su valor cuando hace falta recorrer o completar por carácter.", note_kind="coral")


def se088_profundidad() -> Fig:
    rows = [["Inserción recursiva en BST, 1 500 claves ordenadas, límite 1 000", "RecursionError", "La altura del árbol consume la pila de llamadas"],
            ["Misma inserción con bucle iterativo, 4 000 claves ordenadas", "Funciona (altura 4 000)", "Correcta pero cuadrática: 7 998 000 comparaciones"],
            ["AVL, 100 000 claves ordenadas", "Altura 17", "Cota 1,44·log₂(n+2) = 23,9; 99 983 rotaciones"],
            ["Montículo de 31 elementos tras heapify", "Invariante cumplido", "padre ≤ hijo en los 30 pares; índices (i−1)//2"]]
    return tab("La altura manda: recursión, balanceo e invariante", "Tabla con cuatro resultados: la inserción recursiva en un árbol de claves ordenadas falla con RecursionError, la iterativa funciona pero es cuadrática, un árbol AVL de 100 000 claves ordenadas tiene altura 17 y un montículo satisface el invariante padre menor o igual que hijo.",
               ["Caso", "Resultado", "Lectura"], rows, [360, 220, 340], row_h=62,
               note="La altura no es un detalle de implementación: determina el costo de cada operación y el riesgo de agotar la pila. Un árbol correcto en pruebas con datos aleatorios puede romperse con datos ordenados.", note_kind="gold")


# ---------------------------------------------------------------- SE-089
def se089_bfs_dfs() -> Fig:
    rows = [["20 × 20", "400 / 760", "38 (óptimo 38)", "190", "229"], ["40 × 40", "1 600 / 3 120", "78 (óptimo 78)", "780", "859"], ["80 × 80", "6 400 / 12 640", "158 (óptimo 158)", "3 160", "3 319"]]
    return tab("Rejilla: BFS encuentra el camino más corto, DFS encuentra uno cualquiera", "Tabla sobre rejillas de 20, 40 y 80 de lado: la búsqueda en anchura devuelve distancias 38, 78 y 158, que son las óptimas, y visita todos los nodos; la búsqueda en profundidad devuelve caminos de 190, 780 y 3160 pasos.",
               ["Rejilla", "Nodos / aristas", "BFS: distancia", "DFS: largo del camino", "DFS: nodos visitados"], rows, [120, 190, 220, 210, 190], row_h=48,
               note="El camino que halla DFS es 5, 10 y 20 veces más largo que el óptimo. BFS cuesta V visitas en el peor caso; elegir entre ambos es elegir qué propiedad se necesita: mínima cantidad de aristas o simple alcanzabilidad.", note_kind="teal", foot="Cuentas deterministas sobre rejillas sin obstáculos; no dependen del equipo.")


def se089_representacion() -> Fig:
    rows = [["Lista de adyacencia (2 000 nodos, 7 993 aristas)", "≈ 360 KB", "Vecinos de un nodo: 0,3 µs"],
            ["Matriz de adyacencia (bytearray por fila)", "≈ 4,1 MB (4 000 000 celdas)", "Vecinos de un nodo: 135,9 µs"],
            ["BFS completo, rejilla de 50 × 50 (4 900 aristas)", "—", "3,6 ms"],
            ["BFS completo, rejilla de 100 × 100 (19 800 aristas)", "—", "12,4 ms"],
            ["BFS completo, rejilla de 200 × 200 (79 600 aristas)", "—", "39,2 ms"]]
    return tab("Representación del grafo y costo del recorrido", "Tabla: para 2000 nodos y 7993 aristas la lista de adyacencia ocupa unos 360 kilobytes y obtener los vecinos tarda 0,3 microsegundos, mientras que la matriz ocupa 4,1 megabytes y tarda 135,9 microsegundos; un BFS completo tarda 3,6, 12,4 y 39,2 milisegundos al cuadruplicar las aristas aproximadamente.",
               ["Representación o recorrido", "Memoria", "Tiempo"], rows, [430, 250, 250], row_h=50,
               note="La matriz paga V² celdas aunque el grafo sea disperso (0,4 % de ocupación). Al multiplicar V+E por 4, el BFS tardó 3,5 y 3,2 veces más: consistente con O(V+E).", note_kind="gold")


def se089_pesos() -> Fig:
    rows = [["Aristas con costos 10 (A→B) o 1+1+1 (A→C→D→B)", "BFS: 1 salto, costo real 10", "Dijkstra: costo 3"],
            ["Arista negativa (C→B = −2) y B→D = 3", "Dijkstra con nodos cerrados: D = 5", "Bellman-Ford: D = 4"],
            ["Recorrido sin conjunto de visitados en una rejilla de 25 nodos", "100 000 expansiones (corté por tope)", "Con visitados: 25 expansiones"],
            ["Rejilla de 6×6 con una pared completa", "2 componentes conexas", "Sin pared: 1 componente"],
            ["DFS recursivo sobre una cadena de 5 001 nodos", "RecursionError", "Pila explícita: funciona"]]
    return tab("Cuando el recorrido correcto deja de serlo", "Tabla de cinco casos: BFS minimiza saltos pero no costo, Dijkstra falla con aristas negativas y Bellman-Ford no, un recorrido sin conjunto de visitados no termina, una pared parte la rejilla en dos componentes y el DFS recursivo agota la pila.",
               ["Caso", "Resultado", "Alternativa"], rows, [380, 300, 250], row_h=62,
               note="Cada algoritmo trae una precondición sobre el grafo: pesos no negativos para Dijkstra, ausencia de ciclos negativos para Bellman-Ford. Un resultado «razonable» con la precondición violada es el peor fallo porque no avisa.", note_kind="coral", foot="Cuentas deterministas; no dependen del equipo.")


# ---------------------------------------------------------------- SE-090
def se090_comparaciones() -> Fig:
    rows = [["aleatoria", "6 655", "157 960", "6 695", "16 284"], ["ya ordenada", "799", "799", "3 728", "639 200"], ["invertida", "799", "319 600", "4 048", "639 200"]]
    return tab("Comparaciones contadas con 800 elementos", "Tabla de comparaciones para 800 elementos: sorted (Timsort) usa 6655 con datos aleatorios y 799 con datos ordenados o invertidos; inserción usa 157 960, 799 y 319 600; mezcla usa 6695, 3728 y 4048; quicksort con el primer elemento como pivote usa 16 284, 639 200 y 639 200.",
               ["Entrada", "sorted (Timsort)", "Inserción", "Mezcla (merge)", "Quicksort, pivote = primero"], rows, [150, 190, 180, 190, 220], row_h=48,
               note="Referencia: n·log₂ n = 7 715 y n(n−1)/2 = 319 600. El quicksort con pivote ingenuo se vuelve cuadrático justo con la entrada «ya ordenada», la más común en la práctica; Timsort aprovecha el orden existente y usa n−1 comparaciones.", note_kind="coral", foot="Comparaciones contadas con __lt__ y semilla fija; no dependen del equipo.")


def se090_timsort() -> Fig:
    rows = [["100 000", "22,9 ms", "1,87 ms", "2,31 ms"], ["200 000", "55,5 ms", "5,19 ms", "5,91 ms"]]
    return tab("sorted() sobre datos aleatorios, ordenados e invertidos", "Tabla de tiempos de sorted con 100 000 y 200 000 flotantes: aleatorios 22,9 y 55,5 milisegundos; ya ordenados 1,87 y 5,19; invertidos 2,31 y 5,91.",
               ["n", "Aleatoria", "Ya ordenada", "Invertida"], rows, [190, 250, 250, 250], row_h=46,
               note="Timsort detecta tramos ya ordenados («runs») y los mezcla: los datos ordenados o invertidos fueron 12 y 10 veces más rápidos. La búsqueda binaria necesitó 10, 20 y 30 pasos para 10³, 10⁶ y 10⁹ elementos. Mediana de 100 000 números: sorted()[n//2] tardó 22,3 ms, un quickselect en Python puro 40,8 ms (promedio 2,3 pasadas por elemento) y heapq.nsmallest(1) 1,32 ms para el mínimo.", note_kind="gold")


def se090_trampas() -> Fig:
    rows = [["sorted(registros, key=prioridad)", "['c','e','b','a','d']", "Estable: los empates conservan el orden de llegada"],
            ["sorted([3.0, nan, 1.0, 2.0])", "[3.0, nan, 1.0, 2.0]", "NaN rompe el orden total: no ordena nada"],
            ["sorted([1, 'a'])", "TypeError", "No hay orden entre str e int"],
            ["sorted(['Zebra','apple','Árbol','zeta'])", "['Zebra','apple','zeta','Árbol']", "Orden por punto de código, no alfabético del idioma"]]
    return tab("Cuatro comportamientos de sorted() que conviene conocer", "Tabla de cuatro resultados: la ordenación es estable, una lista con NaN queda sin ordenar, mezclar enteros y cadenas lanza TypeError y las cadenas se ordenan por punto de código de modo que Árbol queda después de zeta.",
               ["Expresión", "Resultado", "Lectura"], rows, [340, 270, 320], row_h=56,
               note="Un comparador que no define un orden total (NaN, prioridades inconsistentes) no produce un error: produce un resultado arbitrario. La estabilidad permite ordenar por varias claves aplicando sorts sucesivos de la clave menos a la más significativa.", note_kind="coral", foot="Resultados deterministas de CPython 3.12; no dependen del equipo.")


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
