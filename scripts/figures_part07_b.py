"""Figures for SE-091 to SE-096 (values measured or computed with CPython 3.12.9 on Windows 11; Linux 3.12.3 where noted)."""
from __future__ import annotations

from figure_cases import case_cards
from figure_kit import Fig, dumbbell, fmt_es, grouped_bars, line_chart, stacked_bars
from figures_part07_a import MEDIDO, bars

DET = "Cuentas deterministas con semilla fija; no dependen del equipo."


# ---------------------------------------------------------------- SE-091
def se091_monedas() -> Fig:
    return case_cards("Cambio mínimo: voraz frente a programación dinámica",
                      "Cinco sistemas de monedas como tarjetas: con 1, 5, 10, 25 y objetivo 63 voraz y dinámica dan 6 monedas; con 1, 3, 4 y objetivo 6 el voraz da 3 y la dinámica 2; 442 de 2000 sistemas aleatorios hicieron que el voraz no fuera óptimo.",
                      [("{1, 5, 10, 25}, objetivo 63", "Voraz 6 monedas = dinámica 6 monedas", "Coinciden: sistema «canónico».", "teal"),
                       ("{1, 3, 4}, objetivo 6", "Voraz 3 monedas (4+1+1); dinámica 2 (3+3)", "El voraz falla.", "coral"),
                       ("{1, 5, 12, 25}", "El voraz falla para algún objetivo < 200", "Sistema no canónico.", "coral"),
                       ("{1, 7, 10}", "El voraz falla para algún objetivo < 200", "Sistema no canónico.", "coral"),
                       ("2 000 sistemas aleatorios con objetivos 1–60", "442 resultados distintos del óptimo", "22 % de los casos.", "gold")],
                      note="El voraz es correcto solo si la estructura del problema lo garantiza (propiedad de elección voraz). No basta con que funcione en el ejemplo de monedas conocido: hay que demostrarlo o refutarlo con casos.",
                      note_kind="coral", foot=DET)


def se091_seleccion() -> Fig:
    return stacked_bars("Voraz que sí y voraz que no: intervalos y mochila",
                        "Barras apiladas al 100 % con los casos en que el criterio voraz fue óptimo y subóptimo: ordenar intervalos por hora de fin fue óptimo en 400 de 400 casos y por hora de inicio en 338 de 400; en la mochila 0/1 el criterio valor por peso fue subóptimo en 228 de 1000 casos.",
                        ["Intervalos: ordenar por fin (400 casos)", "Intervalos: ordenar por inicio (400 casos)", "Mochila 0/1: mayor valor/peso (1 000 casos)"],
                        [("Óptimos", [400, 338, 772], "teal"), ("Subóptimos", [0, 62, 228], "coral")],
                        unit="casos", horizontal=True, percent=True, decimals=1,
                        note="En la mochila el peor caso llegó a 0,556 del óptimo; con pesos 10, 20 y 30, valores 60, 100 y 120 y capacidad 50, el voraz da 160 y el óptimo 220 (el contraejemplo clásico). El mismo problema (intervalos) tiene un criterio voraz correcto y otro incorrecto: la elección del criterio es la parte difícil. Se detecta contrastando con fuerza bruta en instancias pequeñas, sin sustituir la demostración.",
                        note_kind="gold", foot=DET)


def se091_memoria() -> Fig:
    return line_chart("Subsecuencia común más larga: celdas, tiempo y memoria",
                      "Línea en doble escala logarítmica con el tiempo de la tabla de programación dinámica para cadenas de 250, 500 y 1000 caracteres: 22, 92 y 506 milisegundos con 63 001, 251 001 y 1 002 001 celdas; duplicar la longitud cuadruplica las celdas y multiplica el tiempo por 4,2 y 5,5.",
                      [("Tabla completa, Python puro (Windows)", [(250, 22.0, "22,0 ms", "t"), (500, 92.1, "92,1 ms", "t"), (1000, 506, "506 ms", "t")], "teal")],
                      x_label="Longitud de cada cadena (caracteres)", y_label="Tiempo (ms)", log_x=True, log_y=True,
                      x_ticks=[(250, "250 (63 001 celdas)"), (500, "500 (251 001 celdas)"), (1000, "1 000 (1 002 001 celdas)")], y_ticks=[10, 100, 1000],
                      note="Con cadenas de 1 000 caracteres el pico de memoria fue 11,97 MB con la tabla completa y 44 KB con dos filas: 271 veces menos memoria, pero sin poder reconstruir la subsecuencia. Guardar solo dos filas dio el mismo resultado con 44 192 bytes en vez de 11 972 832.",
                      note_kind="teal", foot=MEDIDO)


# ---------------------------------------------------------------- SE-092
def se092_reinas() -> Fig:
    ns = [4, 5, 6, 7, 8, 9]
    return line_chart("N reinas: nodos visitados con poda frente a permutaciones",
                      "Líneas en escala logarítmica vertical con los nodos que visita el retroceso con poda (17, 54, 153, 552, 2057 y 8394) frente a las n factorial permutaciones (24 a 362 880) para 4 a 9 reinas: la brecha crece con n, de 1,4 veces a 43 veces.",
                      [("Permutaciones (n!)", [(n, v, fmt_es(v), "t") for n, v in zip(ns, [24, 120, 720, 5040, 40320, 362880])], "coral"),
                       ("Nodos con poda", [(n, v, fmt_es(v), "r" if n == 4 else "b") for n, v in zip(ns, [17, 54, 153, 552, 2057, 8394])], "teal")],
                      x_label="Número de reinas n", y_label="Nodos o permutaciones", log_y=True, x_ticks=[(n, str(n)) for n in ns], y_ticks=[10, 100, 1000, 10000, 100000, 1000000],
                      note="Soluciones halladas: 2, 10, 4, 40, 92 y 352 para n = 4 a 9. Con n = 8 el retroceso tardó 3,9 ms y generar y filtrar las 40 320 permutaciones 38,2 ms (Linux: 4,0 y 42,7). Ambos hallaron las 92 soluciones: la poda cambia el costo, no el resultado.",
                      note_kind="teal", foot=MEDIDO)


def se092_poda() -> Fig:
    return grouped_bars("Podar y ordenar las decisiones",
                        "Barras agrupadas en escala logarítmica con los nodos visitados antes y después de mejorar la búsqueda: la suma de subconjunto pasa de 450 869 sin poda a 4441 con poda, con las mismas 277 soluciones; para la primera solución, 8 reinas pasa de 114 a 15 nodos y 16 reinas de 10 053 a 26 al empezar por el centro.",
                        ["Suma de subconjunto, 18 números, objetivo 100", "8 reinas, primera solución", "16 reinas, primera solución"],
                        [("Sin poda / columnas en orden 0, 1, 2…", [450869, 114, 10053], "coral"), ("Con poda / empezando por el centro", [4441, 15, 26], "teal")],
                        unit="nodos visitados", log=True, ref_lines=[(524287, "Árbol completo 2¹⁹ − 1")],
                        note="En reinas, las columnas 0..7 y 7..0 visitan los mismos nodos (114 y 114; 10 053 y 10 053). La poda válida elimina solo ramas que no pueden contener soluciones; el orden de las decisiones no cambia qué existe, cambia qué se encuentra primero. Si una poda elimina una solución real, el conteo de soluciones difiere del de la fuerza bruta: esa comparación es la prueba.",
                        note_kind="gold", foot=DET)


def se092_dyc() -> Fig:
    return grouped_bars("Divide y vencerás: mezcla, subarreglo máximo y particiones desiguales",
                        "Barras agrupadas con las comparaciones de la ordenación por mezcla para 1000, 10 000 y 100 000 elementos frente a n log2 n: 8678, 120 398 y 1 536 147 contra 9966, 132 877 y 1 660 964, con profundidad de recursión 10, 14 y 17; la mezcla se queda justo bajo la predicción teórica.",
                        ["n = 1 000 · profundidad 10", "n = 10 000 · profundidad 14", "n = 100 000 · profundidad 17"],
                        [("Comparaciones de mezcla", [8678, 120398, 1536147], "teal"), ("n·log₂ n", [9966, 132877, 1660964], "grey")],
                        unit="comparaciones", log=True,
                        note="Dividir en mitades da profundidad log n; dividir quitando un elemento da profundidad n (RecursionError con 2 000). Para el subarreglo máximo, 500 de 500 casos coincidieron entre divide y vencerás, Kadane y fuerza bruta (6,22 ms frente a 0,62 ms de Kadane): el esquema no siempre es el mejor algoritmo.",
                        note_kind="gold", foot=MEDIDO)


# ---------------------------------------------------------------- SE-093
def se093_filtros() -> Fig:
    return grouped_bars("Estructuras probabilísticas: el error es un parámetro que se elige",
                        "Barras agrupadas con el error medido frente al teórico: un filtro de Bloom con 8 bits por elemento dio 2,12 por ciento de falsos positivos frente a 2,16 teórico, con 16 bits 0,04 frente a 0,05, y HyperLogLog con 1024 registros estimó con 3,02 por ciento de error frente a 3,25 teórico, sin falsos negativos.",
                        ["Bloom, 8 bits por elemento (k = 6)", "Bloom, 16 bits por elemento (k = 11)", "HyperLogLog, 1 024 registros"],
                        [("Error medido", [2.12, 0.04, 3.02], "teal"), ("Error teórico", [2.16, 0.05, 3.25], "grey")],
                        unit="% de error", decimals=2,
                        note="Count-Min 1 000 × 4 sobre 100 000 eventos sobreestima 0,02 en promedio (máx. 2) y nunca subestima; con una sola fila de 1 000 sobreestima 187,8 en promedio (máx. 53 591). Con 16 bits por elemento el filtro ocupa 20 000 B frente a 1 003 394 B de un set. Cada una renuncia a algo declarado; con 10 000 distintos HyperLogLog acertó casi exacto (error 0,01 %).",
                        note_kind="gold", foot=DET)


def se093_indice() -> Fig:
    return grouped_bars("Un índice ayuda según cuántas filas selecciona la consulta",
                        "Barras agrupadas en escala logarítmica con el tiempo de cuatro consultas con y sin índice: buscar un correo exacto pasa de 21,6 a 0,0059 milisegundos, una condición que selecciona 1511 filas de 21,04 a 1,02, una que selecciona el 90 por ciento apenas cambia de 207,1 a 196,9 y la conjunción de dos palabras de 9,55 a 0,008.",
                        ["email = ? (300 000 filas)", "score < 5 (1 511 filas)", "score < 900 (90 % de las filas)", "Dos palabras en 20 000 documentos"],
                        [("Recorrido completo", [21.6, 21.04, 207.1, 9.55], "coral"), ("Con índice", [0.0059, 1.02, 196.9, 0.008], "teal")],
                        unit="ms", log=True,
                        note="Planes: SCAN t sin índice y SEARCH t USING COVERING INDEX ix_email (email=?) con índice (≈ 3 700 veces menos). La conjunción se resolvió con listas invertidas (595 725 entradas) y 8 coincidencias. EXPLAIN QUERY PLAN muestra la decisión del planificador. El índice cuesta espacio y trabajo en cada escritura; sin selectividad no compensa la lectura.",
                        note_kind="coral", foot=MEDIDO)


def se093_persistente() -> Fig:
    f = Fig(940, 420, "Estructura persistente: la versión nueva comparte casi todos los nodos",
            "Un árbol binario balanceado de 4095 nodos se actualiza insertando una clave copiando el camino: se crean 13 nodos y 4083 nodos quedan compartidos entre las versiones; en total existen 4108 nodos distintos en lugar de 8190. Copiar la lista completa de 4095 elementos tardó entre 14 y 19 microsegundos y copiar el camino entre 7 y 16: el tiempo es comparable, la ganancia es de memoria.")
    f.box(10, 14, 440, 54, "Versión 1: 4 095 nodos", "teal", 14, bold=True)
    f.box(490, 14, 440, 54, "Versión 2: copia 13 nodos del camino", "gold", 14, bold=True)
    f.box(10, 92, 270, 90, "Nodos compartidos por ambas versiones: 4 083", "teal", 14)
    f.box(300, 92, 270, 90, "Nodos que existen solo en la versión 2: 13", "gold", 14)
    f.box(590, 92, 340, 90, "Nodos distintos en memoria: 4 108 (no 8 190)", "grey", 14)
    f.box(10, 206, 440, 74, "Copiar la lista de 4 095 referencias (memcpy): 13,6–19,0 µs. Crea 4 095 ranuras nuevas", "coral", 13)
    f.box(490, 206, 440, 74, "Copiar el camino de 13 nodos: 6,6–16,0 µs. Crea 13 nodos nuevos; el tiempo es parecido, la memoria no", "teal", 13)
    f.box(10, 300, 920, 70, "Una referencia mutable compartida rompe la promesa: con b = a; b.append(4), la lista a pasó a [1, 2, 3, 4]. La persistencia exige no modificar nodos ya publicados.", "gold", 13)
    f.text(470, 402, MEDIDO, 12, "middle", 400, "#5c1f14")
    return f


# ---------------------------------------------------------------- SE-094
def se094_pendientes() -> Fig:
    return grouped_bars("Pendiente de la recta log-log: estimar el exponente en vez de adivinarlo",
                        "Barras agrupadas con la pendiente log-log del tiempo frente a n: x en lista da 1,02 en Windows y 1,01 en Linux frente a la teoría de 1, sorted 1,10 y 1,24 frente a 1 de n log n, un bucle de insert en cero 2,10 y 2,11 frente a 2, y la pertenencia en un set 0,01 y 0 frente a 0.",
                        ["x in lista (n de 1 000 a 16 000)", "sorted(lista aleatoria) (20 000 a 160 000)", "Bucle de list.insert(0, x) (5 000 a 40 000)", "x in set (1 000 a 1 000 000)"],
                        [("Teoría", [1, 1, 2, 0], "grey"), ("Windows", [1.02, 1.10, 2.10, 0.01], "teal"), ("Linux (WSL2)", [1.01, 1.24, 2.11, 0.0], "coral")],
                        unit="pendiente log-log", decimals=2,
                        note="La primera pasada en Windows de x in lista dio 1,21; la teoría de sorted es n log n y su «≈ 1» lleva una pendiente aparente por el log n. Una pendiente de 1,10 no distingue n de n·log n, y una sola pasada puede dar 1,21 o 1,02 para el mismo código. Se reporta el rango de n, la cantidad de repeticiones y varias pasadas; el exponente es una estimación con incertidumbre.",
                        note_kind="gold", foot="Medido con CPython 3.12.9 (Windows 11) y 3.12.3 (Ubuntu 24.04, WSL2).")


def se094_ruido() -> Fig:
    return dumbbell("Lo que contamina una medición",
                    "Puntos unidos en escala logarítmica con el valor de referencia y el medido con distorsión: quince repeticiones del mismo ordenamiento variaron de 35 000 a 62 100 microsegundos, cProfile pasó de 9900 a 26 900 y tracemalloc a 105 500, calcular 2 a la 20 con variables costó 149,1 nanosegundos frente a 14,2 con literales, y buscar un ausente en una lista tardó 957,6 microsegundos frente a 0,2 para el primero.",
                    [("15 repeticiones: mínimo → máximo", 35000, 62100), ("Con cProfile", 9900, 26900), ("Con tracemalloc", 9900, 105500),
                     ("2**20: literales → variables", 0.0142, 0.1491), ("0 in lista: primero → ausente", 0.2, 957.6)],
                    unit="µs", names=("Referencia o mínimo", "Con la distorsión"), log=True, label_w=230,
                    delta=lambda a, b: {35000: "CV 20,5 %", 9900: "×2,7" if b < 30000 else "×10,7", 0.0142: "×10", 0.2: "×4 800"}[a],
                    note="El mismo trabajo con cProfile pasó de 9,9 a 26,9 ms (sobrecosto ×2,7 y distorsión por función) y con tracemalloc a 105,5 ms (×10,7); en la lista, el del medio tardó 453,7 µs. Los literales se pliegan en compilación (14,2 ns frente a 149,1 ns): se midió otra cosa. Para comparar alternativas se usa el mínimo o la mediana de muchas repeticiones sobre entradas representativas, y se declara cuál. Un perfilador responde «dónde», no «cuánto» absoluto.",
                    note_kind="coral", foot=MEDIDO)


def se094_pequenos() -> Fig:
    ns = [4, 16, 64, 256]
    return line_chart("Complejidad asintótica y constantes: dónde se cruzan",
                      "Líneas en doble escala logarítmica con el tiempo de buscar todas las claves: con 4 claves el diccionario tarda 0,5 microsegundos y la búsqueda lineal en pares 0,9; con 16, 1,1 y 5,8; con 64, 3,2 y 73,0; con 256, 12,8 y 1113,5, y la brecha crece de 1,8 a 87 veces.",
                      [("Diccionario", [(n, v, fmt_es(v, 1), "b") for n, v in zip(ns, [0.5, 1.1, 3.2, 12.8])], "teal"),
                       ("Recorrido lineal de pares", [(n, v, fmt_es(v, 1), "t") for n, v in zip(ns, [0.9, 5.8, 73.0, 1113.5])], "coral")],
                      x_label="n claves", y_label="Tiempo (µs)", log_x=True, log_y=True, x_ticks=[(n, str(n)) for n in ns], y_ticks=[0.1, 1, 10, 100, 1000, 10000],
                      note="Razón entre ambas: 1,8×, 5,3×, 23× y 87×. Con n pequeño las constantes importan y las diferencias son de microsegundos; con n = 256 la razón ya es de 87. Un generador que suma 100 000 enteros tuvo un pico de 520 B frente a 3,99 MB de la lista equivalente: la memoria también se mide.",
                      note_kind="teal", foot=MEDIDO)


# ---------------------------------------------------------------- SE-095
def se095_colas() -> Fig:
    items = [("Equilibrada, list.pop(0)", 4.4, "coral", "4,4 ms"), ("Equilibrada, deque.popleft()", 3.8, "teal", "3,8 ms"),
             ("Con más entradas, list.pop(0)", 21.6, "coral", "21,6 ms"), ("Con más entradas, deque.popleft()", 3.7, "teal", "3,7 ms")]
    return bars("Misma estructura, dos cargas: la lista como cola", "Barras de 40 000 operaciones: con carga equilibrada la lista tarda 4,4 milisegundos y el deque 3,8, y la cola queda con 78 elementos; con 70 por ciento de entradas la lista tarda 21,6 y el deque 3,7, y la cola queda con 16 024 elementos.",
                items, 22, "La lista funcionó aceptablemente mientras la cola se mantuvo corta (78 elementos al final). Con una cola que crece (16 024 elementos), pop(0) costó 5,8 veces más. La recomendación depende de la longitud típica de la cola, que se mide en producción.", label_w=330, foot=MEDIDO)


def se095_matriz() -> Fig:
    return grouped_bars("Matriz de compromisos medida: operación dominante frente a estructura",
                        "Barras horizontales con lo que cuesta la alternativa frente al mejor candidato de cada carga: la lista ordenada cuesta 4,5 veces el montículo en la cola de prioridad (50,0 frente a 11,2 milisegundos), la lista 192 veces el set en 2000 pertenencias (315,2 frente a 1,64), el recorrido 648 veces bisect en el conteo por rango (1036 frente a 1,6 microsegundos) y el set 5,2 veces la lista en memoria (4,19 frente a 0,80 MB).",
                        ["Cola de prioridad, 20 000 elementos: montículo 11,2 ms · lista ordenada 50,0 ms", "2 000 pertenencias sobre 20 000 claves: set 1,64 ms · lista 315,2 ms",
                         "Conteo en un rango de 20 000 claves ordenadas: bisect 1,6 µs · recorrido 1 036 µs", "Memoria por 100 000 enteros: lista 0,80 MB · set 4,19 MB · dict 5,24 MB"],
                        [("Mejor candidato (referencia = ×1)", [1, 1, 1, 1], "teal"), ("Alternativa", [4.46, 192.2, 647.5, 5.24], "gold")],
                        unit="veces el costo del mejor candidato", horizontal=True, log=True, ticks=[1, 10, 100, 1000], label_w=380,
                        value_fmt=lambda v: "×" + fmt_es(v, 0 if v >= 100 else 1),
                        note="Razones calculadas con las medidas de las etiquetas. El dict ocupa 6,5 veces la lista en la última carga. Con min()+remove() sobre 5 000 elementos la cola de prioridad tardó 310,9 ms. Cada carga tiene un ganador distinto, y el que gana en tiempo suele perder en memoria. Una recomendación única sin la operación dominante no es defendible; con ella se escribe en una línea.",
                        note_kind="gold", foot=MEDIDO)


def se095_umbral() -> Fig:
    qs = [1, 3, 10, 100]
    return line_chart("¿Cuántas consultas justifican construir un set?",
                      "Líneas en doble escala logarítmica con el tiempo de n igual a 10 000 según el número de consultas: recorrer la lista tarda 92,8, 282,9, 905,3 y 8497 microsegundos con 1, 3, 10 y 100 consultas y construir un set y consultar 173,9, 174,7, 272,8 y 188,4; las líneas se cruzan entre 1 y 3 consultas.",
                      [("Recorrer la lista", [(q, v, fmt_es(v, 0 if v > 8000 else 1), "b" if q == 1 else "t") for q, v in zip(qs, [92.8, 282.9, 905.3, 8497])], "coral"),
                       ("Construir el set y consultar", [(q, v, fmt_es(v, 1), "t" if q == 1 else "b") for q, v in zip(qs, [173.9, 174.7, 272.8, 188.4])], "teal")],
                      x_label="Consultas sobre 10 000 elementos", y_label="Tiempo (µs)", log_x=True, log_y=True, x_ticks=[(q, str(q)) for q in qs], y_ticks=[10, 100, 1000, 10000],
                      note="El set ya gana con 3 consultas (3,3 veces más rápido con 10 y 45 veces con 100). El punto de cruce está en 2 o 3 consultas por construcción. Construir el set solo compensa si se reutiliza: esa frase («cuántas veces se consulta») es parte de la recomendación.",
                      note_kind="teal", foot=MEDIDO)


# ---------------------------------------------------------------- SE-096
def se096_mutantes() -> Fig:
    return grouped_bars("Seis mutantes de una secuencia ordenada: ejemplos frente a oráculo diferencial",
                        "Barras horizontales con el porcentaje de detección de seis defectos inyectados: las pruebas de ejemplo solo detectan dos (agregar al final y rango cerrado), y el oráculo diferencial con 200 semillas de 60 pasos detecta cinco entre 97,5 y 100 por ciento y no detecta left_dups, que es equivalente para enteros.",
                        ["add_end: agrega al final sin ordenar (mediana 6 pasos)", "closed_hi: el rango incluye el extremo superior (20)", "remove_all: borra todos los duplicados (29)",
                         "raise_missing: lanza KeyError al borrar un ausente (4)", "neg_range: devuelve negativo si lo > hi (15)", "left_dups: inserta duplicados a la izquierda (—)"],
                        [("Pruebas de ejemplo: detecta (100 %) o pasa (0 %)", [100, 100, 0, 0, 0, 0], "gold"), ("Oráculo diferencial (% de 200 semillas)", [100, 98.5, 99.0, 98.5, 97.5, 0], "teal")],
                        unit="% de detección", horizontal=True, label_w=330, value_fmt=lambda v: fmt_es(v, 0 if v in (0, 100) else 1),
                        note="Los ejemplos escritos a mano dejaron pasar cuatro de seis defectos. left_dups no se detecta porque, para enteros iguales, insertar a izquierda o derecha es indistinguible: es un mutante equivalente, y solo una prueba con identidad (registros) lo revelaría. Entre paréntesis, los pasos medianos hasta fallar.",
                        note_kind="coral", foot=DET)


def se096_hallazgo() -> Fig:
    f = Fig(940, 420, "El oráculo encontró un defecto en la propia implementación de referencia",
            "La primera versión de count_range devolvía un número negativo cuando el límite inferior era mayor que el superior, mientras que el oráculo devolvía cero. El test diferencial falló antes de inyectar mutantes; tras acotar el resultado con max(0, …) la línea base pasó 300 semillas de 200 pasos.")
    f.box(10, 14, 440, 70, "Versión 1: count_range(lo, hi) = bisect_left(hi) − bisect_left(lo)", "coral", 14)
    f.box(490, 14, 440, 70, "Oráculo: sum(1 for v in datos if lo <= v < hi)", "teal", 14)
    f.arrow([(230, 84), (230, 130)])
    f.arrow([(710, 84), (710, 130)])
    f.box(10, 130, 920, 62, "Con lo > hi y tres valores entre ambos límites, la versión 1 devuelve −3 y el oráculo 0: contradicción hallada por una ejecución aleatoria", "gold", 14)
    f.arrow([(470, 192), (470, 224)])
    f.box(10, 224, 920, 62, "Corrección: max(0, resultado). Línea base: 300 semillas × 200 pasos sin discrepancias.", "teal", 14)
    f.box(10, 306, 920, 70, "Un contrato que no dice qué pasa con lo > hi deja que cada implementación decida. El caso límite se escribió en el contrato y en una prueba de regresión nombrada.", "grey", 13)
    f.text(470, 404, DET, 12, "middle", 400, "#5c1f14")
    return f


def se096_bordes() -> Fig:
    return case_cards("Casos límite entre bibliotecas y una comparación con cruce",
                      "Seis casos límite como tarjetas: sacar de una estructura vacía lanza IndexError en list, heappop y deque, ValueError en min y KeyError en dict y set; bisect sobre una lista desordenada devuelve 2 sin error; una variante que elimina duplicados coincide en 1419 de 2000 casos; y heapq.nsmallest gana para k pequeño y pierde para k grande.",
                      [("list.pop() en una lista vacía", "IndexError", "También heappop([]) y deque().popleft().", "coral"),
                       ("min([])", "ValueError", "Distinto tipo de error para «vacío».", "coral"),
                       ("{}[1] y set().remove(1)", "KeyError", "dict.get y set.discard no lanzan.", "gold"),
                       ("bisect_left([3, 1, 2], 2)", "2 (sin error)", "Precondición de orden violada: respuesta silenciosa.", "coral"),
                       ("k menores: sorted(set(xs))[:k] frente a sorted(xs)[:k]", "Coincide en 1 419 de 2 000", "Descarta duplicados: 581 discrepancias.", "coral"),
                       ("k = 10 sobre 100 000: sorted frente a heapq.nsmallest", "22,8 ms frente a 2,35 ms", "Con k = 30 000 se invierte: 24,1 ms frente a 74,2 ms.", "gold")],
                      note="Una biblioteca comparada declara, para cada estructura, qué ocurre en vacío, con duplicados y con precondiciones violadas. La elección de la mejor implementación puede invertirse al cambiar el parámetro k, así que la recomendación lo menciona.",
                      note_kind="gold", foot=MEDIDO)


FIGURES = {
    "se-091-monedas-voraz-y-dinamica.svg": se091_monedas,
    "se-091-intervalos-y-mochila.svg": se091_seleccion,
    "se-091-tabla-y-memoria.svg": se091_memoria,
    "se-092-reinas-y-poda.svg": se092_reinas,
    "se-092-poda-y-orden.svg": se092_poda,
    "se-092-divide-y-venceras.svg": se092_dyc,
    "se-093-filtros-y-sketches.svg": se093_filtros,
    "se-093-indices-y-selectividad.svg": se093_indice,
    "se-093-estructura-persistente.svg": se093_persistente,
    "se-094-pendientes-log-log.svg": se094_pendientes,
    "se-094-ruido-y-sobrecosto.svg": se094_ruido,
    "se-094-constantes-y-cruce.svg": se094_pequenos,
    "se-095-cola-segun-la-carga.svg": se095_colas,
    "se-095-matriz-de-compromisos.svg": se095_matriz,
    "se-095-umbral-de-reutilizacion.svg": se095_umbral,
    "se-096-mutantes-y-oraculo.svg": se096_mutantes,
    "se-096-defecto-en-la-referencia.svg": se096_hallazgo,
    "se-096-bordes-y-comparacion.svg": se096_bordes,
}
