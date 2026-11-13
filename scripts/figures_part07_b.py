"""Figures for SE-091 to SE-096 (values measured or computed with CPython 3.12.9 on Windows 11; Linux 3.12.3 where noted)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import MEDIDO, bars, tab

DET = "Cuentas deterministas con semilla fija; no dependen del equipo."


# ---------------------------------------------------------------- SE-091
def se091_monedas() -> Fig:
    rows = [["{1, 5, 10, 25}, objetivo 63", "6 monedas", "6 monedas", "Coinciden: sistema «canónico»"],
            ["{1, 3, 4}, objetivo 6", "3 monedas (4+1+1)", "2 monedas (3+3)", "El voraz falla"],
            ["{1, 5, 12, 25}", "falla para algún objetivo < 200", "—", "No canónico"],
            ["{1, 7, 10}", "falla para algún objetivo < 200", "—", "No canónico"],
            ["2 000 sistemas aleatorios con objetivos 1–60", "442 resultados distintos del óptimo", "—", "22 % de los casos"]]
    return tab("Cambio mínimo: voraz frente a programación dinámica", "Tabla: para el sistema 1, 5, 10, 25 y objetivo 63 voraz y dinámica dan 6 monedas; para 1, 3, 4 y objetivo 6 el voraz da 3 y la dinámica 2; 442 de 2000 sistemas aleatorios de monedas hicieron que el voraz no fuera óptimo.",
               ["Sistema de monedas", "Voraz", "Programación dinámica", "Lectura"], rows, [310, 250, 190, 180], row_h=60,
               note="El voraz es correcto solo si la estructura del problema lo garantiza (propiedad de elección voraz). No basta con que funcione en el ejemplo de monedas conocido: hay que demostrarlo o refutarlo con casos.", note_kind="coral", foot=DET)


def se091_seleccion() -> Fig:
    rows = [["Intervalos: ordenar por fin (400 casos aleatorios)", "400 de 400 óptimos", "Elección voraz demostrable"],
            ["Intervalos: ordenar por inicio (los mismos 400)", "338 de 400 óptimos", "62 casos con resultado peor"],
            ["Mochila 0/1: mayor valor/peso, 1 000 casos", "228 subóptimos; peor razón 0,556", "No es voraz-correcto"],
            ["Mochila: pesos 10, 20, 30; valores 60, 100, 120; capacidad 50", "voraz 160; óptimo 220", "El contraejemplo clásico"]]
    return tab("Voraz que sí y voraz que no: intervalos y mochila", "Tabla: ordenar intervalos por hora de fin fue óptimo en 400 de 400 casos y por hora de inicio solo en 338; para la mochila 0/1 el criterio valor por peso fue subóptimo en 228 de 1000 casos, con un peor caso de 0,556 del óptimo, y en el ejemplo clásico dio 160 frente a 220.",
               ["Problema y criterio", "Resultado", "Lectura"], rows, [420, 290, 220], row_h=60,
               note="El mismo problema (intervalos) tiene un criterio voraz correcto y otro incorrecto: la elección del criterio es la parte difícil. Se detecta contrastando con fuerza bruta en instancias pequeñas, sin sustituir la demostración.", note_kind="gold", foot=DET)


def se091_memoria() -> Fig:
    rows = [["250 × 250", "63 001", "22,0 ms"], ["500 × 500", "251 001", "92,1 ms"], ["1 000 × 1 000", "1 002 001", "506 ms"]]
    return tab("Subsecuencia común más larga: celdas, tiempo y memoria", "Tabla: la tabla de programación dinámica tiene 63 001, 251 001 y 1 002 001 celdas para cadenas de 250, 500 y 1000 caracteres y tarda 22, 92 y 506 milisegundos; con 1000 caracteres el pico de memoria fue 11,97 MB con la tabla completa y 44 KB con dos filas.",
               ["Cadenas", "Celdas de la tabla", "Tiempo en Windows"], rows, [260, 330, 340], row_h=46,
               note="Duplicar la longitud cuadruplica las celdas (y el tiempo ×4,2 y ×5,5). Guardar solo dos filas dio el mismo resultado con 44 192 bytes en vez de 11 972 832: 271 veces menos memoria, pero sin poder reconstruir la subsecuencia.", note_kind="teal", foot=MEDIDO)


# ---------------------------------------------------------------- SE-092
def se092_reinas() -> Fig:
    rows = [["4", "2", "17", "24"], ["5", "10", "54", "120"], ["6", "4", "153", "720"], ["7", "40", "552", "5 040"], ["8", "92", "2 057", "40 320"], ["9", "352", "8 394", "362 880"]]
    return tab("N reinas: nodos visitados con poda frente a permutaciones", "Tabla: el número de soluciones es 2, 10, 4, 40, 92 y 352 para 4 a 9 reinas; el retroceso con poda visita 17, 54, 153, 552, 2057 y 8394 nodos, muy por debajo de las n factorial permutaciones (24 a 362 880).",
               ["n", "Soluciones", "Nodos con poda", "Permutaciones (n!)"], rows, [140, 230, 270, 290], row_h=40,
               note="Con n = 8 el retroceso tardó 3,9 ms y generar y filtrar las 40 320 permutaciones 38,2 ms (Linux: 4,0 y 42,7). Ambos hallaron las 92 soluciones: la poda cambia el costo, no el resultado.", note_kind="teal", foot=MEDIDO)


def se092_poda() -> Fig:
    rows = [["Suma de subconjunto, 18 números, objetivo 100", "4 441 nodos", "277 soluciones"],
            ["La misma búsqueda sin poda", "450 869 nodos", "277 soluciones"],
            ["Máximo del árbol completo (2¹⁹ − 1)", "524 287 nodos", "—"],
            ["8 reinas: primera solución con columnas 0..7, 7..0 o desde el centro", "114 / 114 / 15 nodos", "El orden importa"],
            ["16 reinas: las mismas tres órdenes", "10 053 / 10 053 / 26 nodos", "387 veces menos"]]
    return tab("Podar y ordenar las decisiones", "Tabla: con poda la suma de subconjunto visita 4441 nodos frente a 450 869 sin poda y 524 287 en el árbol completo, con las mismas 277 soluciones; en 16 reinas la primera solución exige 10 053 nodos con orden ascendente y 26 empezando por el centro.",
               ["Búsqueda", "Nodos visitados", "Lectura"], rows, [430, 270, 230], row_h=60,
               note="La poda válida elimina solo ramas que no pueden contener soluciones; el orden de las decisiones no cambia qué existe, cambia qué se encuentra primero. Si una poda elimina una solución real, el conteo de soluciones difiere del de la fuerza bruta: esa comparación es la prueba.", note_kind="gold", foot=DET)


def se092_dyc() -> Fig:
    rows = [["1 000", "8 678", "9 966", "10"], ["10 000", "120 398", "132 877", "14"], ["100 000", "1 536 147", "1 660 964", "17"]]
    return tab("Divide y vencerás: mezcla, subarreglo máximo y particiones desiguales", "Tabla: la ordenación por mezcla usó 8678, 120 398 y 1 536 147 comparaciones con profundidad 10, 14 y 17 para 1000, 10 000 y 100 000 elementos, cerca de n log2 n; el subarreglo de suma máxima por divide y vencerás tardó 6,22 ms frente a 0,62 ms de Kadane, y una partición de uno en uno agotó la pila.",
               ["n", "Comparaciones de mezcla", "n·log₂ n", "Profundidad de recursión"], rows, [150, 270, 240, 270], row_h=46,
               note="Dividir en mitades da profundidad log n; dividir quitando un elemento da profundidad n (RecursionError con 2 000). Para el subarreglo máximo, 500 de 500 casos coincidieron entre divide y vencerás, Kadane y fuerza bruta, y Kadane fue 10 veces más rápido: el esquema no siempre es el mejor algoritmo.", note_kind="gold", foot=MEDIDO)


# ---------------------------------------------------------------- SE-093
def se093_filtros() -> Fig:
    rows = [["Bloom, 8 bits por elemento (k = 6)", "falsos positivos 2,12 %", "teoría 2,16 %; 0 falsos negativos"],
            ["Bloom, 16 bits por elemento (k = 11)", "falsos positivos 0,04 %", "teoría 0,05 %; 20 000 B frente a 1 003 394 B de un set"],
            ["Count-Min 1 000 × 4 sobre 100 000 eventos", "sobreestima 0,02 en promedio, máx. 2", "Nunca subestima"],
            ["Count-Min de una sola fila de 1 000", "sobreestima 187,8 en promedio, máx. 53 591", "Las filas extra reducen el error"],
            ["HyperLogLog, 1 024 registros, 100 000 distintos", "estima 103 020 (error 3,02 %)", "Error teórico ≈ 3,25 %"]]
    return tab("Estructuras probabilísticas: el error es un parámetro que se elige", "Tabla: un filtro de Bloom con 8 bits por elemento dio 2,12 por ciento de falsos positivos frente a 2,16 teórico y ningún falso negativo; Count-Min nunca subestimó y su error medio pasó de 187,8 con una fila a 0,02 con cuatro; HyperLogLog con 1024 registros estimó 103 020 para 100 000 con 3,02 por ciento de error.",
               ["Estructura y configuración", "Error medido", "Referencia"], rows, [330, 300, 300], row_h=60,
               note="Cada una renuncia a algo declarado: Bloom a decir «sí» con certeza, Count-Min a la exactitud (sobreestima) y HyperLogLog a la identidad de los elementos. Con 10 000 distintos HyperLogLog acertó casi exacto (error 0,01 %): el error es una distribución, no un valor fijo.", note_kind="gold", foot=DET)


def se093_indice() -> Fig:
    rows = [["email = ? en 300 000 filas, sin índice", "SCAN t", "21,6 ms"], ["email = ? con índice", "SEARCH t USING COVERING INDEX ix_email (email=?)", "0,0059 ms (≈ 3 700 veces menos)"],
            ["score < 5 (1 511 filas) con y sin índice", "índice: 1,02 ms; sin índice: 21,04 ms", "20 veces menos"],
            ["score < 900 (269 990 filas, 90 %) con y sin índice", "índice: 196,9 ms; sin índice: 207,1 ms", "Casi igual: poca selectividad"],
            ["Conjunción de dos palabras: recorrer 20 000 documentos o intersectar listas invertidas", "9,55 ms frente a 0,008 ms", "8 coincidencias; índice invertido de 595 725 entradas"]]
    return tab("Un índice ayuda según cuántas filas selecciona la consulta", "Tabla: en SQLite con 300 000 filas buscar un correo exacto tardó 21,6 milisegundos con recorrido completo y 0,0059 con índice; una condición que selecciona 1511 filas pasó de 21 a 1 milisegundo y una que selecciona el 90 por ciento apenas cambió de 207 a 197.",
               ["Consulta", "Plan o tiempos", "Lectura"], rows, [330, 330, 270], row_h=68,
               note="EXPLAIN QUERY PLAN muestra la decisión del planificador: SCAN o SEARCH. El índice cuesta espacio y trabajo en cada escritura; sin selectividad no compensa la lectura.", note_kind="coral", foot=MEDIDO)


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
    rows = [["x in lista (n de 1 000 a 16 000)", "≈ 1", "1,02 (Windows) · 1,01 (Linux)", "La primera pasada en Windows dio 1,21"],
            ["sorted(lista aleatoria) (20 000 a 160 000)", "≈ 1 (n log n)", "1,10 · 1,24", "log n añade pendiente aparente"],
            ["Bucle de list.insert(0, x) (5 000 a 40 000)", "2", "2,10 · 2,11", "Cuadrático confirmado"],
            ["x in set (1 000 a 1 000 000)", "0", "0,01 · −0,00", "Constante"]]
    return tab("Pendiente de la recta log-log: estimar el exponente en vez de adivinarlo", "Tabla de pendientes log-log del tiempo frente a n: x en lista da 1,02 en Windows y 1,01 en Linux, sorted 1,10 y 1,24, un bucle de insert en cero 2,10 y 2,11 y la pertenencia en un set 0,01 y menos de 0,01.",
               ["Operación (rango de n)", "Teoría", "Medido: Windows · Linux", "Observación"], rows, [310, 130, 250, 240], row_h=60,
               note="Una pendiente de 1,10 no distingue n de n·log n, y una sola pasada puede dar 1,21 o 1,02 para el mismo código. Se reporta el rango de n, la cantidad de repeticiones y varias pasadas; el exponente es una estimación con incertidumbre.", note_kind="gold", foot="Medido con CPython 3.12.9 (Windows 11) y 3.12.3 (Ubuntu 24.04, WSL2).")


def se094_ruido() -> Fig:
    rows = [["15 repeticiones de sorted(random.sample(50 000))", "mínimo 35,0 · mediana 39,0 · máximo 62,1 ms", "Coef. de variación 20,5 %"],
            ["Mismo trabajo con cProfile", "9,9 ms → 26,9 ms", "Sobrecosto ×2,7 y distorsión por función"],
            ["Mismo trabajo con tracemalloc", "9,9 ms → 105,5 ms", "Sobrecosto ×10,7"],
            ["2**20 con literales frente a variables", "14,2 ns frente a 149,1 ns", "El plegado de constantes midió otra cosa"],
            ["0 in lista de 100 000: primero, medio, ausente", "0,2 µs · 453,7 µs · 957,6 µs", "El caso medido cambia el resultado ×4 800"]]
    return tab("Lo que contamina una medición", "Tabla: quince repeticiones del mismo ordenamiento variaron entre 35,0 y 62,1 milisegundos; cProfile multiplicó el tiempo por 2,7 y tracemalloc por 10,7; calcular 2 a la 20 con literales fue 10 veces más barato por plegado de constantes; y buscar el primer, el del medio o un ausente en una lista cambia el tiempo de 0,2 a 957,6 microsegundos.",
               ["Qué se midió", "Resultado", "Lectura"], rows, [330, 330, 270], row_h=60,
               note="Para comparar alternativas se usa el mínimo o la mediana de muchas repeticiones sobre entradas representativas, y se declara cuál. Un perfilador responde «dónde», no «cuánto» absoluto.", note_kind="coral", foot=MEDIDO)


def se094_pequenos() -> Fig:
    rows = [["4", "0,5 µs", "0,9 µs", "1,8×"], ["16", "1,1 µs", "5,8 µs", "5,3×"], ["64", "3,2 µs", "73,0 µs", "23×"], ["256", "12,8 µs", "1 113,5 µs", "87×"]]
    return tab("Complejidad asintótica y constantes: dónde se cruzan", "Tabla con búsqueda de todas las claves: con 4 claves el diccionario tarda 0,5 microsegundos y la búsqueda lineal en pares 0,9; con 16, 1,1 y 5,8; con 64, 3,2 y 73,0; con 256, 12,8 y 1113,5 microsegundos.",
               ["n claves", "Diccionario", "Recorrido lineal de pares", "Razón"], rows, [150, 250, 330, 200], row_h=44,
               note="Con n pequeño las constantes importan y las diferencias son de microsegundos; con n = 256 la razón ya es de 87. Un generador que suma 100 000 enteros tuvo un pico de 520 B frente a 3,99 MB de la lista equivalente: la memoria también se mide.", note_kind="teal", foot=MEDIDO)


# ---------------------------------------------------------------- SE-095
def se095_colas() -> Fig:
    items = [("Equilibrada, list.pop(0)", 4.4, "coral", "4,4 ms"), ("Equilibrada, deque.popleft()", 3.8, "teal", "3,8 ms"),
             ("Con más entradas, list.pop(0)", 21.6, "coral", "21,6 ms"), ("Con más entradas, deque.popleft()", 3.7, "teal", "3,7 ms")]
    return bars("Misma estructura, dos cargas: la lista como cola", "Barras de 40 000 operaciones: con carga equilibrada la lista tarda 4,4 milisegundos y el deque 3,8, y la cola queda con 78 elementos; con 70 por ciento de entradas la lista tarda 21,6 y el deque 3,7, y la cola queda con 16 024 elementos.",
                items, 22, "La lista funcionó aceptablemente mientras la cola se mantuvo corta (78 elementos al final). Con una cola que crece (16 024 elementos), pop(0) costó 5,8 veces más. La recomendación depende de la longitud típica de la cola, que se mide en producción.", label_w=330, foot=MEDIDO)


def se095_matriz() -> Fig:
    rows = [["Cola de prioridad, 20 000 elementos", "montículo 11,2 ms", "lista ordenada 50,0 ms", "min+remove (5 000): 310,9 ms"],
            ["2 000 pertenencias sobre 20 000 claves", "set 1,64 ms", "lista 315,2 ms", "—"],
            ["Conteo en un rango de 20 000 claves ordenadas", "bisect 1,6 µs", "recorrido 1 036 µs", "—"],
            ["Memoria por 100 000 enteros", "lista 0,80 MB", "set 4,19 MB", "dict 5,24 MB"]]
    return tab("Matriz de compromisos medida: operación dominante frente a estructura", "Tabla: cola de prioridad con montículo 11,2 milisegundos, lista ordenada 50,0 y buscar el mínimo 310,9 para cinco mil elementos; 2000 pertenencias con set 1,64 milisegundos y con lista 315,2; conteo por rango 1,6 microsegundos con bisect y 1036 con recorrido; memoria de 100 000 enteros 0,80 MB en lista, 4,19 en set y 5,24 en dict.",
               ["Carga", "Mejor candidato", "Alternativa", "Peor"], rows, [300, 200, 220, 210], row_h=60,
               note="Cada fila tiene un ganador distinto, y el que gana en tiempo suele perder en memoria. Una recomendación única sin la operación dominante no es defendible; con ella se escribe en una línea.", note_kind="gold", foot=MEDIDO)


def se095_umbral() -> Fig:
    rows = [["1", "92,8 µs", "173,9 µs", "La lista gana"], ["3", "282,9 µs", "174,7 µs", "El set ya gana"], ["10", "905,3 µs", "272,8 µs", "Set 3,3× más rápido"], ["100", "8 497 µs", "188,4 µs", "Set 45× más rápido"]]
    return tab("¿Cuántas consultas justifican construir un set?", "Tabla con n igual a 10 000: con 1 consulta la lista tarda 92,8 microsegundos y construir un set y consultar 173,9; con 3 consultas, 282,9 contra 174,7; con 10, 905,3 contra 272,8; con 100, 8497 contra 188,4.",
               ["Consultas sobre 10 000 elementos", "Recorrer la lista", "Construir set y consultar", "Lectura"], rows, [240, 200, 260, 230], row_h=44,
               note="El punto de cruce está en 2 o 3 consultas por construcción. Construir el set solo compensa si se reutiliza: esa frase («cuántas veces se consulta») es parte de la recomendación.", note_kind="teal", foot=MEDIDO)


# ---------------------------------------------------------------- SE-096
def se096_mutantes() -> Fig:
    rows = [["add_end: agrega al final sin ordenar", "No (falla)", "100 %", "6"], ["closed_hi: el rango incluye el extremo superior", "No (falla)", "98,5 %", "20"],
            ["remove_all: borra todos los duplicados", "Sí (pasa)", "99,0 %", "29"], ["raise_missing: lanza KeyError al borrar un ausente", "Sí (pasa)", "98,5 %", "4"],
            ["neg_range: devuelve negativo si lo > hi", "Sí (pasa)", "97,5 %", "15"], ["left_dups: inserta duplicados a la izquierda", "Sí (pasa)", "0 %", "—"]]
    return tab("Seis mutantes de una secuencia ordenada: ejemplos frente a oráculo diferencial", "Tabla de seis defectos inyectados: las pruebas de ejemplo solo detectan dos (agregar al final y rango cerrado); el oráculo diferencial con 200 semillas de 60 pasos detecta cinco entre 97,5 y 100 por ciento y no detecta el sexto, que es equivalente para enteros.",
               ["Mutante", "¿Pasan los ejemplos?", "Detectado por el oráculo", "Pasos medianos hasta fallar"], rows, [350, 190, 210, 180], row_h=48,
               note="Los ejemplos escritos a mano dejaron pasar cuatro de seis defectos. left_dups no se detecta porque, para enteros iguales, insertar a izquierda o derecha es indistinguible: es un mutante equivalente, y solo una prueba con identidad (registros) lo revelaría.", note_kind="coral", foot=DET)


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
    rows = [["list.pop() en una lista vacía", "IndexError", "heappop([]) y deque().popleft(): IndexError"],
            ["min([])", "ValueError", "Distinto tipo de error para «vacío»"],
            ["{}[1] y set().remove(1)", "KeyError", "dict.get y set.discard no lanzan"],
            ["bisect_left([3, 1, 2], 2)", "2 (sin error)", "Precondición de orden violada: respuesta silenciosa"],
            ["k menores: sorted(set(xs))[:k] frente a sorted(xs)[:k]", "coincide en 1 419 de 2 000", "Descarta duplicados: 581 discrepancias"],
            ["k = 10 sobre 100 000: sorted frente a heapq.nsmallest", "22,8 ms frente a 2,35 ms", "k = 30 000: 24,1 ms frente a 74,2 ms"]]
    return tab("Casos límite entre bibliotecas y una comparación con cruce", "Tabla: sacar de una estructura vacía lanza IndexError en list, heappop y deque, ValueError en min y KeyError en dict y set; bisect sobre una lista desordenada devuelve 2 sin error; una variante que elimina duplicados coincide con la de referencia en 1419 de 2000 casos; y heapq.nsmallest gana para k pequeño y pierde para k grande.",
               ["Caso", "Resultado", "Lectura"], rows, [370, 220, 340], row_h=60,
               note="Una biblioteca comparada declara, para cada estructura, qué ocurre en vacío, con duplicados y con precondiciones violadas. La elección de la mejor implementación puede invertirse al cambiar el parámetro k, así que la recomendación lo menciona.", note_kind="gold", foot=MEDIDO)


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
