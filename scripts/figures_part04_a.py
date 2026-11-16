"""Figures for SE-049 to SE-060 (values computed or measured with CPython 3.12.9 on Windows 11)."""
from __future__ import annotations

from figure_flow_rows import chain_rows, steps_row
from figure_kit import Fig, grouped_bars, line_chart, stacked_bars


CALC = "Resultados calculados con Python 3.12.9; las mediciones de tiempo dependen del equipo."


# ---------------------------------------------------------------- SE-049
def se049_arbol() -> Fig:
    f = Fig(960, 450, "Descomposición del incidente en decisión, hipótesis, pruebas y restricciones",
            "Árbol del modelo del laboratorio: la decisión es elegir la próxima prueba segura; las hipótesis son dns, tls y http; las pruebas son resolve, handshake, request y production-capture "
            "(esta última no autorizada); las restricciones son solo pruebas autorizadas y un presupuesto de cinco unidades.")
    f.box(300, 14, 360, 56, "Decisión: elegir la próxima prueba segura para explicar una petición fallida", "navy", 13, bold=True)
    cols = [
        ("Hipótesis", ["dns", "tls", "http"], "teal", 30),
        ("Pruebas (costo)", ["resolve (1)", "handshake (2)", "request (3)", "production-capture (1): NO autorizada"], "gold", 350),
        ("Restricciones", ["authorized_only: solo pruebas autorizadas", "bounded_cost: presupuesto de 5 unidades"], "coral", 670),
    ]
    for name, items, kind, x in cols:
        f.arrow([(480, 70), (x + 130, 110)])
        f.box(x, 110, 260, 40, name, "navy", 13, bold=True)
        for i, it in enumerate(items):
            f.box(x, 158 + i * 54, 260, 48, it, kind, 12)
    f.box(30, 380, 900, 56, "Descomponer es separar lo que se decide de lo que se supone y de lo que se limita; cada nodo puede revisarse por separado.", "grey", 13)
    return f


def se049_matriz() -> Fig:
    return grouped_bars(
        "Cuánto discrimina cada prueba entre las tres hipótesis y cuánto cuesta",
        "Barras horizontales con el costo de cada prueba y cuántos resultados distintos produce bajo las hipótesis dns, tls y http: resolve cuesta 1 y da 2 resultados distintos, handshake cuesta 2 y da 3, request cuesta 3 y da 2, production-capture cuesta 1 y da 1 porque devuelve unknown bajo todas y no está autorizada.",
        ["resolve", "handshake", "request", "production-capture (no autorizada)"],
        [("Costo de la prueba", [1, 2, 3, 1], "navy"), ("Resultados distintos entre las 3 hipótesis", [2, 3, 2, 1], "teal")],
        unit="Unidades de costo o resultados distintos", horizontal=True, label_w=240, ticks=[0, 1, 2, 3],
        note="Cada celda del modelo es una predicción que puede refutarse. Una prueba que da el mismo resultado bajo todas las hipótesis, como production-capture con «unknown», no discrimina ni está permitida.",
        note_kind="gold", foot=CALC)


def se049_abstraccion() -> Fig:
    rows = [
        [("Un conjunto cerrado de hipótesis (dns, tls, http)", "teal"), ("Causas simultáneas o fuera de la lista", "coral"), ("Solo es correcto respecto de las hipótesis declaradas", "gold")],
        [("Costos y presupuesto de cada prueba", "teal"), ("Costo variable según el momento o la carga", "coral"), ("La puntuación codiciosa no garantiza una secuencia global óptima", "gold")],
        [("Resultados deterministas por prueba", "teal"), ("Ruido, variación y fallos intermitentes", "coral"), ("Una medición de tiempo no sustituye el análisis de crecimiento", "gold")],
    ]
    return chain_rows(
        "Qué conserva y qué descarta el modelo, y qué límite declara cada descarte",
        "Diagrama de tres filas del laboratorio: el modelo conserva un conjunto cerrado de hipótesis, los costos y los resultados deterministas; descarta las causas simultáneas, el costo variable y el ruido; y de cada descarte nace un límite declarado, por ejemplo que la selección codiciosa no garantiza una secuencia global óptima.",
        ["Lo que conserva", "Lo que descarta", "Límite declarado"], rows, [280, 280, 280], gap=26,
        note="Toda abstracción es una decisión de qué ignorar. La pregunta útil es qué descarte puede invalidar la conclusión y cómo se detectaría.",
        note_kind="gold", foot=CALC)


# ---------------------------------------------------------------- SE-050
def se050_implicacion() -> Fig:
    rows = [
        [("p falso", "plain"), ("q falso", "plain"), ("p → q verdadero", "teal")],
        [("p falso", "plain"), ("q verdadero", "plain"), ("p → q verdadero", "teal")],
        [("p verdadero", "plain"), ("q falso", "plain"), ("p → q FALSO", "coral")],
        [("p verdadero", "plain"), ("q verdadero", "plain"), ("p → q verdadero", "teal")],
    ]
    return chain_rows(
        "La implicación solo es falsa cuando p es verdadera y q falsa, y su recíproca no es equivalente",
        "Diagrama de las cuatro combinaciones de p y q que llevan al valor de p implica q: verdadero en tres y falso solo cuando p es verdadera y q falsa; la contrapositiva es equivalente en las cuatro filas y la recíproca difiere en las filas con p y q distintos.",
        ["Premisa", "Conclusión", "Valor de p → q"], rows, [250, 250, 300], gap=34,
        note="Contrapositiva (¬q → ¬p): equivalente en las 4 filas, verificado. Recíproca (q → p): no equivalente, difiere en «falso, verdadero» y «verdadero, falso». Por eso «si hay un fallo de DNS, no resuelve» no permite concluir lo contrario.",
        note_kind="gold", foot=CALC)


def se050_filas() -> Fig:
    return line_chart(
        "Filas de una tabla de verdad según el número de variables",
        "Línea con las filas de una tabla de verdad, 2 elevado a n, en escala logarítmica: 1 024 con 10 variables, 1 048 576 con 20 y unos 1 073 millones con 30; enumerar las 1 048 576 filas tomó 0,102 segundos en Python.",
        [("Filas (2^n)", [(10, 1024), (20, 1048576), (30, 1073741824)], "coral")],
        x_label="Variables n", y_label="Filas de la tabla", log_y=True, x_ticks=[(10, "10"), (20, "20"), (30, "30")], point_labels="all",
        note="Con 20 variables la enumeración tomó 0,102 s; con 30 sería inviable. Un ciclo de implicaciones entre n variables tiene solo 2 modelos para n = 3, 5 y 10. Para muchas variables se usan solucionadores SAT.",
        note_kind="gold", foot=CALC)


def se050_cuantificadores() -> Fig:
    rows = [
        [("all([])", "plain"), ("True", "gold"), ("Verdad vacía: «todo elemento cumple» es verdadero si no hay elementos", "plain")],
        [("any([])", "plain"), ("False", "gold"), ("No existe ningún elemento que cumpla", "plain")],
        [("¬(a ∧ b) ≡ ¬a ∨ ¬b", "plain"), ("True en las 4 filas", "teal"), ("Ley de De Morgan verificada", "plain")],
    ]
    return chain_rows(
        "Cuantificadores sobre dominios finitos y la verdad vacía",
        "Diagrama de tres expresiones y su resultado: all sobre una lista vacía es True, any sobre una lista vacía es False y las leyes de De Morgan se verificaron en las cuatro filas.",
        ["Expresión", "Resultado", "Lectura"], rows, [220, 190, 380], gap=34,
        note="Una regla «todas las pruebas autorizadas pasan» se cumple si no hay ninguna prueba: la verdad vacía puede ocultar un conjunto vacío. Se comprueba además que el conjunto no sea vacío.",
        note_kind="coral", foot=CALC)


# ---------------------------------------------------------------- SE-051
def se051_dependencias() -> Fig:
    f = Fig(940, 400, "Dependencias como grafo: orden topológico y ciclo",
            "Un grafo de dependencias app depende de lib y util, lib depende de util tiene el orden topológico util, lib, app; con un ciclo a, b, c, a, graphlib lanza CycleError y señala el ciclo.")
    f.box(20, 40, 400, 100, "Grafo acíclico: app → {lib, util}; lib → util\nOrden de construcción: util, lib, app", "teal", 14, bold=True)
    f.box(520, 40, 400, 100, "Grafo con ciclo: a → b → c → a\ngraphlib.CycleError: ciclo ['a', 'c', 'b', 'a']", "coral", 14, bold=True)
    f.box(20, 170, 900, 70, "Un orden de construcción existe si y solo si el grafo no tiene ciclos. La herramienta no «resuelve» el ciclo: lo informa con el camino.", "grey", 13)
    f.box(20, 252, 900, 70, "Un ciclo de dependencias es un defecto de diseño que se rompe extrayendo un componente común o invirtiendo una dependencia.", "gold", 13)
    return f


def se051_recorrido() -> Fig:
    f = Fig(940, 410, "Recorrer un grafo con ciclo sin repetir ni colgarse",
            "Un grafo A conecta con B y C, B y C con D, y D vuelve a A. Un recorrido en anchura con un conjunto de visitados produce A, B, C, D y termina; sin el conjunto de visitados recorrería el ciclo indefinidamente.")
    f.box(20, 40, 200, 56, "A → B, C", "plain", 14, bold=True)
    f.box(240, 40, 200, 56, "B → D · C → D", "plain", 14, bold=True)
    f.box(460, 40, 200, 56, "D → A (ciclo)", "coral", 14, bold=True)
    f.box(680, 40, 240, 56, "Orden en anchura: A, B, C, D", "teal", 14, bold=True)
    f.box(20, 130, 900, 80, "El conjunto de visitados es el invariante de terminación: cada nodo entra una vez, así que el número de pasos está acotado por el de nodos más aristas.", "grey", 13)
    f.box(20, 222, 900, 80, "Sin visitados, el recorrido de un grafo con ciclo no termina: la terminación se demuestra con una medida que decrece (nodos aún no visitados).", "gold", 13)
    return f


def se051_cierre() -> Fig:
    pts = [(10, 45), (20, 190), (100, 4950), (1000, 499500)]
    return line_chart(
        "Pares alcanzables del cierre transitivo de una cadena de n nodos",
        "Línea en escala logarítmica con los pares alcanzables n por n menos 1 entre 2: 45 con 10 nodos, 190 con 20, 4 950 con 100 y 499 500 con 1 000; cada vez que n se multiplica por 10 los pares se multiplican por unos 100.",
        [("n(n−1)/2 pares", pts, "gold")],
        x_label="Nodos n en cadena", y_label="Pares alcanzables", log_x=True, log_y=True, x_ticks=[(10, "10"), (20, "20"), (100, "100"), (1000, "1 000")], point_labels="all",
        note="La información derivable (quién depende de quién, directa o indirectamente) puede ser mucho mayor que la declarada: para consultas frecuentes se calcula una vez y se guarda. El crecimiento es cuadrático.",
        note_kind="gold", foot=CALC)


# ---------------------------------------------------------------- SE-052
def se052_assert() -> Fig:
    f = Fig(940, 400, "Una aserción no es un control de entrada",
            "Ejecutando python con la opción -O, la sentencia assert False se ignora y el programa continúa e imprime «las aserciones se ignoraron». Un contrato que debe cumplirse siempre se valida con excepciones, no con assert.")
    f.box(20, 40, 420, 100, "python -c \"assert False; print('sigue')\"\n→ AssertionError", "teal", 13, bold=True)
    f.box(500, 40, 420, 100, "python -O -c \"assert False; print('sigue')\"\n→ imprime: las aserciones se ignoraron", "coral", 13, bold=True)
    f.box(20, 170, 900, 80, "Las aserciones documentan invariantes internos y ayudan a depurar; se eliminan con -O. Validar entradas de usuarios, permisos o presupuestos con assert crea una brecha que solo aparece en producción.", "gold", 13)
    f.box(20, 262, 900, 60, "Precondiciones de una API pública: excepciones (ValueError). Invariantes internos: assert. Seguridad: nunca assert.", "grey", 13)
    return f


def se052_busqueda() -> Fig:
    return stacked_bars(
        "Búsqueda binaria sobre 3 234 casos exhaustivos: la versión correcta y la que usa hi = mid",
        "Barras apiladas horizontales con los 3 234 casos de arreglos ordenados de longitud hasta 6: la versión con hi = mid − 1 comete 0 fallos y la versión con hi = mid comete 1 181, incluidos casos en que no termina.",
        ["hi = mid − 1 (correcta)", "hi = mid (error)"],
        [("Sin fallo", [3234, 2053], "teal"), ("Fallos", [0, 1181], "coral")],
        unit="Casos de 3 234", horizontal=True, label_w=190,
        note="En un dominio pequeño se prueba todo: pocos valores bastan para exponer el error de borde. Un invariante (0 ≤ lo ≤ hi + 1 ≤ n) más una medida que decrece (hi − lo) explican por qué la versión correcta termina.",
        note_kind="gold", foot=CALC)


def se052_contrato() -> Fig:
    rows = [
        [("Precondición", "gold"), ("El presupuesto cubre el costo de la prueba elegida", "plain"), ("La selección falla con un error explícito", "coral")],
        [("Invariante", "gold"), ("Los candidatos restantes son un subconjunto de las hipótesis", "plain"), ("No puede crecer: una observación solo descarta", "coral")],
        [("Poscondición", "gold"), ("Observaciones contradictorias se informan en lugar de ocultarse", "plain"), ("La ejecución falla en voz alta con el conflicto", "coral")],
    ]
    return chain_rows(
        "Contratos del laboratorio: qué se exige y qué ocurre cuando se viola",
        "Diagrama de tres contratos del laboratorio: la precondición exige que el presupuesto cubra el costo y su violación hace fallar la selección con un error; el invariante exige que los candidatos sean un subconjunto de las hipótesis; la poscondición exige informar las observaciones contradictorias.",
        ["Tipo", "Contrato del laboratorio", "Si se viola"], rows, [190, 380, 290], gap=26,
        note="Un contrato convierte «debería funcionar» en una frase comprobable: quién debe qué, antes, durante y después. Violarlo es un defecto del llamador (precondición) o de la implementación (poscondición).",
        note_kind="gold", foot=CALC)


# ---------------------------------------------------------------- SE-053
def se053_limite() -> Fig:
    return grouped_bars(
        "La recursión tiene profundidad finita: límite del intérprete y profundidad alcanzada",
        "Barras horizontales con el límite de recursión por defecto, 1 000, y la profundidad que alcanzó una recursión simple antes de lanzar RecursionError, 999; json.loads sobre una estructura anidada 100 000 veces también lanzó RecursionError.",
        ["sys.getrecursionlimit()", "Profundidad alcanzada por una recursión simple"],
        [("Niveles", [1000, 999], "navy")],
        unit="Niveles de recursión", horizontal=True, label_w=250, ticks=[0, 250, 500, 750, 1000],
        note="Quedan marcos para el propio manejo del error. Con 100 000 niveles de anidación, json.loads lanzó RecursionError: una entrada hostil puede agotar la pila. Entradas de tamaño no acotado exigen límites de profundidad o una versión iterativa con pila explícita.",
        note_kind="coral", foot=CALC)


def se053_fibonacci() -> Fig:
    return grouped_bars(
        "Recursión ingenua frente a memoización: llamadas o cálculos para fib(27) = 196 418",
        "Barras en escala logarítmica con las llamadas necesarias para fib(27): 635 621 con la definición recursiva directa, que tarda 0,097 segundos, y 28 cálculos únicos con memoización, que tarda 0,000021 segundos.",
        ["Recursiva directa (0,097 s)", "Con memoización, lru_cache (0,000021 s)"],
        [("Llamadas o cálculos", [635621, 28], "coral")],
        unit="Llamadas o cálculos", horizontal=True, log=True, label_w=270,
        note="Las llamadas se solapan: los mismos subproblemas se recalculan exponencialmente. La memoización los resuelve una vez cada uno: la estructura de la recursión es la misma, la complejidad cambia de exponencial a lineal.",
        note_kind="gold", foot=CALC)


def se053_induccion() -> Fig:
    return steps_row(
        "Inducción: caso base, hipótesis, paso y comprobación para la suma de 0 a n",
        "Diagrama de cuatro pasos para demostrar que la suma de 0 a n es n por n más 1 entre 2: el caso base n igual a 0, la hipótesis inductiva para n, el paso de n a n más 1 y la comprobación computacional para n de 0 a 1999 sin contraejemplos.",
        [("1 · Caso base", "n = 0: la suma es 0 y 0·1/2 = 0", "teal"),
         ("2 · Hipótesis", "Se cumple para n: Σ = n(n+1)/2", "plain"),
         ("3 · Paso", "Σ hasta n+1 = n(n+1)/2 + (n+1) = (n+1)(n+2)/2", "plain"),
         ("4 · Comprobación", "Verificada para n = 0 … 1999: sin contraejemplos", "gold")],
        note="Probar muchos casos no demuestra la propiedad: solo la inducción cubre todos los n. A la inversa, una demostración puede contener un error: por eso se contrasta con casos.",
        note_kind="gold", foot=CALC)


# ---------------------------------------------------------------- SE-054
def se054_euclides() -> Fig:
    return grouped_bars(
        "Pasos del algoritmo de Euclides en un caso común y en el peor caso",
        "Barras horizontales con los pasos de dos ejecuciones: gcd de 1071 y 462 da 21 en 3 pasos; gcd de 987 y 610, Fibonacci consecutivos, da 1 en 14 pasos, el peor caso. La medida b decrece estrictamente en cada paso.",
        ["gcd(1071, 462) = 21", "gcd(987, 610) = 1 (Fibonacci consecutivos)"],
        [("Pasos", [3, 14], "teal")],
        unit="Pasos", horizontal=True, label_w=270, ticks=[0, 4, 8, 12, 16],
        note="Correctitud: gcd(a, b) = gcd(b, a mod b). Terminación: b disminuye en cada paso y no puede bajar de 0. Costo: proporcional al logaritmo de la entrada; el peor caso son números de Fibonacci consecutivos.",
        note_kind="gold", foot=CALC)


def se054_collatz() -> Fig:
    return steps_row(
        "Cuando la terminación no se sabe demostrar: la conjetura de Collatz",
        "Diagrama de cuatro pasos: en el rango de 1 a 99 999 el número que más pasos necesita es 77 031 con 350 pasos hasta llegar a 1; que todos terminen no está demostrado en general, así que la terminación es una conjetura.",
        [("Rango probado", "1 … 99 999", "plain"), ("Número más largo", "77 031", "gold"), ("Pasos hasta llegar a 1", "350", "gold"),
         ("¿Termina siempre?", "Sin demostración general: es una conjetura", "coral")],
        note="El procedimiento (si es par, dividir entre 2; si no, multiplicar por 3 y sumar 1) termina para todo n probado. Un programa cuya terminación depende de un problema abierto necesita un límite de pasos o un plazo.",
        note_kind="coral", foot=CALC)


def se054_oraculo() -> Fig:
    rows = [
        [("2000 casos aleatorios: burbuja = sorted", "gold"), ("Confianza en esos casos y en su distribución", "teal"), ("Garantía para todos los arreglos ni para tamaños grandes", "coral")],
        [("Argumento de invariante (cola ordenada)", "gold"), ("Prueba para toda entrada si es correcto", "teal"), ("Que el código implemente el argumento", "coral")],
    ]
    return chain_rows(
        "Probar contra un oráculo y lo que no demuestra",
        "Diagrama de dos tipos de evidencia: 2000 casos aleatorios en que la burbuja coincidió con sorted aportan confianza en esos casos pero no garantía para todos los arreglos; un argumento de invariante prueba para toda entrada si es correcto, pero no que el código lo implemente.",
        ["Evidencia", "Qué aporta", "Qué no aporta"], rows, [290, 280, 290], gap=26,
        note="Pruebas y demostraciones se complementan: una exhibe fallos concretos y la otra cubre todos los casos. Un contraejemplo invalida el algoritmo; la ausencia de contraejemplos no lo valida.",
        note_kind="gold", foot=CALC)


# ---------------------------------------------------------------- SE-055
def se055_doblar() -> Fig:
    ns = [2000, 4000, 8000]
    return line_chart(
        "Tiempo mediano de cuatro operaciones al duplicar n y la razón entre n = 8000 y n = 4000",
        "Líneas en escala logarítmica con las medianas por operación para n igual a 2000, 4000 y 8000: la búsqueda lineal pasa de 2,96 a 11,74 ms (razón 1,99), la búsqueda por hash se mantiene en 0,020 ms (0,99), la ordenación pasa de 0,22 a 1,01 ms (2,10) y el doble bucle sobre n/4 de 9,64 a 171,63 ms (4,30).",
        [("Doble bucle sobre n/4 (razón 4,30)", list(zip(ns, [9.64, 39.89, 171.63])), "coral"),
         ("Búsqueda lineal (1,99)", list(zip(ns, [2.96, 5.89, 11.74])), "gold"),
         ("Ordenación (2,10)", list(zip(ns, [0.22, 0.48, 1.01])), "navy"),
         ("Búsqueda por hash (0,99)", list(zip(ns, [0.020, 0.020, 0.020])), "teal")],
        x_label="n", y_label="Tiempo mediano (ms)", log_x=True, log_y=True, x_ticks=[(2000, "2 000"), (4000, "4 000"), (8000, "8 000")], point_labels="last", decimals=2,
        note="Si duplicar n multiplica el tiempo por ≈2, el crecimiento es lineal; por ≈4, cuadrático; por ≈1, constante. La razón se mide, no se supone.",
        note_kind="gold", foot=CALC)


def se055_conteo() -> Fig:
    return grouped_bars(
        "Razón teórica y razón medida al duplicar n en cuatro operaciones",
        "Barras agrupadas con la razón de tiempos al duplicar n: lineal, teórica 2 y medida 1,99; hash, teórica 1 y medida 0,99; n log n, teórica un poco más de 2 (≈2,1) y medida 2,10; cuadrática, teórica 4 y medida 4,30.",
        ["Lineal", "Hash", "n log n", "Cuadrática"],
        [("Razón teórica", [2, 1, 2.1, 4], "navy"), ("Razón medida", [1.99, 0.99, 2.10, 4.30], "teal")],
        unit="Razón al duplicar n", decimals=2, ticks=[0, 1, 2, 3, 4, 5], plot_h=250,
        note="Cuando la medición discrepa mucho de la teoría hay un error de análisis, de medición o un efecto de caché o del intérprete; ninguna de las dos fuentes sustituye a la otra.",
        note_kind="gold", foot=CALC)


def se055_capacidad() -> Fig:
    pts = [(1, 88), (5, 120), (9, 184), (17, 248), (25, 312), (33, 376)]
    return line_chart(
        "Tamaño en bytes de una lista de Python en los puntos en que reserva memoria",
        "Línea con el tamaño en bytes de una lista al añadir elementos uno por uno: 88 con 1 elemento, 120 con 5, 184 con 9, 248 con 17, 312 con 25 y 376 con 33; el tamaño cambia solo en algunos puntos y la mayoría de las inserciones no reservan memoria.",
        [("Bytes de la lista en cada reserva", pts, "gold")],
        x_label="Elementos al reservar", y_label="Bytes de la lista", x_ticks=[(1, "1"), (5, "5"), (9, "9"), (17, "17"), (25, "25"), (33, "33")], y_ticks=[0, 100, 200, 300, 400], point_labels="all",
        note="Cada reserva es costosa y rara: el costo promedio por inserción es constante (amortizado), aunque una inserción concreta pueda ser lenta. Las cifras dependen de la versión de CPython y de la arquitectura.",
        note_kind="gold", foot=CALC)


# ---------------------------------------------------------------- SE-056
def se056_monedas() -> Fig:
    return grouped_bars(
        "Monedas para devolver 6 con monedas de 1, 3 y 4: algoritmo codicioso y óptimo",
        "Barras horizontales con las monedas necesarias para devolver 6: el algoritmo codicioso usa 4, 1 y 1, tres monedas; la programación dinámica usa 3 y 3, dos monedas. En el rango hasta 60 el mayor exceso del codicioso ocurre en el monto 6.",
        ["Codiciosa: la mayor posible primero (4 + 1 + 1)", "Programación dinámica, óptima (3 + 3)"],
        [("Monedas", [3, 2], "coral")],
        unit="Monedas para devolver 6", horizontal=True, label_w=300, ticks=[0, 1, 2, 3],
        note="La heurística es correcta con monedas de un sistema canónico (1, 5, 10, 25) y falla con otros conjuntos: un solo contraejemplo basta para refutar que sea óptima en general. Una heurística se acompaña de su contraejemplo y de la condición en que funciona.",
        note_kind="gold", foot=CALC)


def se056_tsp() -> Fig:
    return grouped_bars(
        "Vecino más cercano frente al óptimo en 100 instancias de 8 ciudades: razón del recorrido",
        "Barras horizontales con la razón entre el recorrido de la heurística del vecino más cercano y el óptimo, en 100 instancias aleatorias de 8 ciudades: 1,000 en el mejor caso, 1,086 de media y 1,318 en el peor caso.",
        ["Mejor caso", "Razón media", "Peor caso observado"],
        [("Recorrido heurístico / óptimo", [1.0, 1.086, 1.318], "gold")],
        unit="Razón al óptimo", horizontal=True, decimals=3, label_w=190, ticks=[0, 0.5, 1.0, 1.5], ref_lines=[(1.0, "Óptimo")],
        note="La heurística es rápida y, en promedio, razonable; en el peor caso observado es un 32 % peor. No hay garantía general: se conoce la razón en la muestra, no el máximo en todos los casos. Semilla 5; el óptimo se calculó por fuerza bruta (7! permutaciones por instancia).",
        note_kind="gold", foot=CALC)


def se056_fuerza() -> Fig:
    ns = [7, 8, 9]
    return line_chart(
        "Fuerza bruta del viajante: permutaciones y tiempo medido, relativos a n = 7",
        "Líneas en escala logarítmica con el crecimiento respecto de 7 ciudades: las permutaciones (n−1)! pasan de 720 a 5 040 y 40 320, es decir 1, 7 y 56 veces; el tiempo medido pasa de 0,002 s a 0,012 s y 0,110 s, es decir 1, 6 y 55 veces. Con 12 ciudades habría 39 916 800 permutaciones.",
        [("Permutaciones (n−1)!", list(zip(ns, [1, 7, 56])), "navy"), ("Tiempo medido", list(zip(ns, [1, 6, 55])), "coral")],
        x_label="Ciudades n", y_label="Veces respecto de n = 7", log_y=True, x_ticks=[(7, "7"), (8, "8"), (9, "9")], point_labels="all",
        note="Cada ciudad adicional multiplica el tiempo por 6 a 9, coherente con las permutaciones. Un algoritmo exacto de crecimiento factorial se vuelve inviable muy pronto: con 12 ciudades serían horas; por eso existen heurísticas y aproximaciones.",
        note_kind="gold", foot=CALC)


# ---------------------------------------------------------------- SE-057
def se057_pedido() -> Fig:
    f = Fig(960, 430, "Máquina de estados de un pedido",
            "Seis estados (nuevo, pagado, enviado, entregado, cancelado, devuelto) y cinco eventos definen 30 pares estado-evento, de los cuales 6 son transiciones legales y 24 son ilegales y deben rechazarse.")
    f.text(14, 27, "Seis estados y las seis transiciones legales", 15, "start", 700, "#142231")
    f.box(20, 60, 150, 52, "nuevo", "navy", 14, bold=True)
    f.box(290, 60, 150, 52, "pagado", "navy", 14, bold=True)
    f.box(560, 60, 150, 52, "enviado", "navy", 14, bold=True)
    f.box(800, 60, 150, 52, "entregado", "teal", 14, bold=True)
    f.box(150, 190, 150, 52, "cancelado", "coral", 14, bold=True)
    f.box(560, 190, 150, 52, "devuelto", "gold", 14, bold=True)
    f.arrow([(174, 86), (286, 86)], "pagar")
    f.arrow([(444, 86), (556, 86)], "enviar")
    f.arrow([(714, 86), (796, 86)], "entregar")
    f.arrow([(95, 116), (95, 216), (146, 216)], "cancelar", label_at=(60, 170))
    f.arrow([(365, 116), (365, 150), (225, 150), (225, 186)], "cancelar", label_at=(300, 144))
    f.arrow([(635, 116), (635, 186)], "devolver", label_at=(668, 156))
    f.box(740, 160, 210, 98, "6 estados × 5 eventos = 30 pares: 6 legales y 24 ilegales.", "gold", 13, bold=True)
    f.box(10, 290, 940, 56, "Un evento ilegal (por ejemplo, enviar un pedido nuevo) se rechaza de forma explícita: no se ignora ni cambia el estado.", "coral", 13)
    f.box(10, 358, 940, 56, "El modelo hace visible lo que antes era implícito: qué está permitido en cada estado y qué no.", "grey", 13)
    f.kind = "diagram"
    return f


def se057_producto() -> Fig:
    return grouped_bars(
        "Explosión de estados al combinar máquinas independientes",
        "Barras horizontales con los estados del producto de máquinas independientes: 6 por 5 son 30, 6 por 5 por 4 son 120 y 6 por 5 por 4 por 4 por 3 son 1 440; un sistema de cinco componentes pequeños ya tiene más de mil estados.",
        ["6 × 5", "6 × 5 × 4", "6 × 5 × 4 × 4 × 3"],
        [("Estados del producto", [30, 120, 1440], "coral")],
        unit="Estados del producto", horizontal=True, label_w=190, ticks=[0, 400, 800, 1200, 1600],
        note="Razonar sobre el producto a mano es inviable: se modelan los componentes por separado, se declaran las interacciones y se explora el espacio de estados con una herramienta (verificación de modelos).",
        note_kind="gold", foot=CALC)


def se057_alcanzables() -> Fig:
    rows = [
        [("¿Cuántos estados son alcanzables desde «nuevo»?", "plain"), ("6 de 6", "teal")],
        [("¿Se puede llegar a «entregado» sin pasar por «pagado»?", "plain"), ("No: hay que pasar por pagado y enviado", "teal")],
        [("¿Se puede devolver un pedido cancelado?", "plain"), ("No: no hay transición desde cancelado", "teal")],
    ]
    return chain_rows(
        "Estados alcanzables e invariantes del pedido: preguntas y respuestas de la exploración",
        "Diagrama de tres preguntas sobre el pedido y su respuesta: desde nuevo se alcanzan los 6 estados, no se llega a entregado sin pasar por pagado y enviado, y no se puede devolver un pedido cancelado porque no hay transición desde cancelado.",
        ["Pregunta sobre el modelo", "Respuesta de la exploración"], rows, [520, 340], gap=40,
        note="Un invariante como «entregado implica pagado» se verifica recorriendo los estados alcanzables; si algún estado lo viola, el modelo (o la regla) está mal.",
        note_kind="gold", foot=CALC)


# ---------------------------------------------------------------- SE-058
def se058_biseccion() -> Fig:
    return grouped_bars(
        "Pruebas necesarias para localizar un cambio defectuoso por bisección",
        "Barras horizontales con las pruebas de la bisección: 10 pruebas entre 1 024 cambios para hallar un defecto en el cambio 700, y 20 pruebas entre un millón para hallar uno en el cambio 123 456; cada prueba descarta la mitad de los candidatos.",
        ["1 024 cambios (defecto en el 700)", "1 000 000 de cambios (defecto en el 123 456)"],
        [("Pruebas (≈ log2 n)", [10, 20], "teal")],
        unit="Pruebas", horizontal=True, label_w=300, ticks=[0, 5, 10, 15, 20],
        note="La bisección (git bisect) exige una prueba determinista y la suposición de monotonía: todo cambio anterior al defecto es sano y todo cambio posterior lo contiene. Si la prueba es intermitente, el resultado no es fiable.",
        note_kind="gold", foot=CALC)


def se058_intermitentes() -> Fig:
    return line_chart(
        "Corridas necesarias para ver con 95 % de confianza un fallo intermitente",
        "Línea en escala logarítmica con las corridas necesarias según la probabilidad de fallo por corrida: 5 si vale 0,5; 29 si vale 0,1 y 299 si vale 0,01, con la fórmula techo de ln 0,05 entre ln de 1 menos p; una simulación con p igual a 0,1 y 29 corridas lo observó en 95,2 % de 10 000 intentos.",
        [("⌈ln(0,05) / ln(1 − p)⌉", [(0.5, 5), (0.1, 29), (0.01, 299)], "coral")],
        x_label="Probabilidad de fallo por corrida", y_label="Corridas para verlo con 95 %", log_x=True, log_y=True,
        x_ticks=[(0.01, "0,01"), (0.1, "0,1"), (0.5, "0,5")], point_labels="all",
        note="Simulación (10 000 intentos, p = 0,1, 29 corridas): el fallo apareció en el 95,2 %, coherente con la fórmula. Un fallo raro exige muchas corridas: «no lo reproduje» con pocas corridas no es evidencia de que no exista.",
        note_kind="coral", foot=CALC)


def se058_confianza() -> Fig:
    return stacked_bars(
        "Con el defecto presente (p = 0,1), qué ocurre en cinco corridas seguidas",
        "Barra apilada horizontal con la probabilidad de lo que ocurre en cinco corridas si el defecto está presente con p igual a 0,1: pasan las cinco con probabilidad 0,9 elevado a 5, es decir 0,59, y se observa al menos una falla con probabilidad 1 menos 0,59, es decir 0,41.",
        ["Defecto presente, cinco corridas"],
        [("Pasan las cinco: 0,9^5 = 0,59", [59], "gold"), ("Al menos una falla: 1 − 0,59 = 0,41", [41], "coral")],
        unit="Probabilidad (%)", horizontal=True, label_w=190,
        note="Con un 59 % de probabilidad, «lo corregí porque ahora pasa cinco veces» es una conclusión que falla más de la mitad de las veces. Se registra la hipótesis, la predicción y el número de corridas planificado antes de concluir.",
        note_kind="coral", foot=CALC)


# ---------------------------------------------------------------- SE-059
def se059_contradiccion() -> Fig:
    return grouped_bars(
        "Requisitos que cumple cada configuración: ninguna cumple los tres",
        "Barras horizontales con cuántos de los tres requisitos (cifrado extremo a extremo, búsqueda en el servidor y sin índice en claro en el servidor) cumple cada una de las cuatro configuraciones: e2e con índice en servidor cumple 2, e2e con índice en cliente cumple 2, transporte con índice en servidor cumple 2 y transporte con índice en cliente cumple 1; ninguna llega a 3.",
        ["e2e + índice en servidor", "e2e + índice en cliente", "transporte + índice en servidor", "transporte + índice en cliente"],
        [("Requisitos cumplidos de 3", [2, 2, 2, 1], "navy")],
        unit="Requisitos cumplidos de 3", horizontal=True, label_w=240, ticks=[0, 1, 2, 3], ref_lines=[(3, "Los tres requisitos")],
        note="Ninguna de las 4 configuraciones satisface los tres requisitos: la contradicción es del conjunto, no de la implementación. Se detecta enumerando el espacio pequeño antes de construir nada.",
        note_kind="gold", foot=CALC)


def se059_relajar() -> Fig:
    rows = [
        [("Búsqueda en el servidor", "gold"), ("1: e2e + índice en el cliente", "teal"), ("La búsqueda ocurre en el dispositivo: más datos locales, más tiempo", "coral")],
        [("Cifrado extremo a extremo", "gold"), ("Más de una", "teal"), ("El servidor puede leer los datos", "coral")],
    ]
    return chain_rows(
        "Relajar un requisito: qué configuraciones quedan y qué cuesta a la persona usuaria",
        "Diagrama de dos relajaciones posibles: al relajar la búsqueda en el servidor queda una única configuración válida, cifrado extremo a extremo con el índice en el cliente, a costa de más datos locales y más tiempo; al relajar el cifrado quedan más de una, pero el servidor puede leer los datos.",
        ["Requisito relajado", "Configuraciones válidas", "Costo para la persona usuaria"], rows, [250, 270, 310], gap=26,
        note="El análisis no decide por la persona: muestra qué se gana y qué se pierde con cada relajación, y deja la decisión a quien tenga autoridad y a quienes resultan afectados.",
        note_kind="gold", foot=CALC)


def se059_preguntas() -> Fig:
    return steps_row(
        "Preguntas abiertas y registro de la decisión ante una contradicción",
        "Diagrama de cuatro elementos del registro de una contradicción: la contradicción de los tres requisitos sin solución conjunta, las opciones, quién decide y las preguntas abiertas; no se escoge en silencio.",
        [("1 · Contradicción", "Los tres requisitos no tienen solución conjunta (0 de 4 configuraciones)", "coral"),
         ("2 · Opciones", "Relajar la búsqueda en servidor, relajar e2e o cambiar el alcance", "plain"),
         ("3 · Quién decide", "Propietario del producto con asesoría de seguridad; las personas afectadas se consultan", "gold"),
         ("4 · Preguntas abiertas", "¿Qué dato necesita realmente buscarse? ¿Con qué latencia? ¿Qué riesgo se acepta?", "plain")],
        note="Una contradicción no resuelta que se oculta reaparece como un defecto en producción; una que se registra es una decisión revisable.",
        note_kind="gold", foot=CALC)


# ---------------------------------------------------------------- SE-060
def se060_pruebas() -> Fig:
    return grouped_bars(
        "Las trece pruebas del laboratorio repartidas por el contrato que protegen",
        "Barras horizontales con las pruebas por grupo: especificación 3, razonamiento 3, selección y observación 4 y evidencia 3, en total 13; pasaron en Windows 11 en 0,167 s y en Linux en 0,245 s.",
        ["Especificación (datos válidos y conflictos explícitos)", "Razonamiento (lógica, terminación y estados)", "Selección y observación (invariantes y precondiciones)", "Evidencia (trazabilidad y límites)"],
        [("Pruebas", [3, 3, 4, 3], "teal")],
        unit="Pruebas de 13", horizontal=True, label_w=330, ticks=[0, 1, 2, 3, 4],
        note="13 pruebas: Windows 11 (Python 3.12.9) 0,167 s; Linux (WSL2, Python 3.12.3) 0,245 s. Cada grupo protege un contrato distinto y la clase lista las trece en su tabla.",
        note_kind="gold", foot=CALC)


def se060_resolucion() -> Fig:
    return steps_row(
        "Resolución del caso de referencia, paso a paso",
        "Diagrama de tres pasos del caso de referencia: resolve da ok y deja tls y http como candidatos con costo 1; handshake da fail y deja solo tls con costo acumulado 3; el estado final es resolved, con 3 de 5 unidades gastadas y presupuesto restante 2.",
        [("Paso 1 · resolve", "Resultado ok. Candidatos: tls, http. Costo acumulado 1", "plain"),
         ("Paso 2 · handshake", "Resultado fail. Candidatos: tls. Costo acumulado 3", "plain"),
         ("Estado final", "resolved · candidatos [tls] · gastado 3 de 5 · restante 2 · próxima prueba: ninguna", "teal")],
        note="«Resuelto» significa que, dentro del modelo, solo queda una hipótesis compatible con las observaciones. No significa que el mundo real esté completo ni que las premisas sean verdaderas.",
        note_kind="gold", foot=CALC)


def se060_limites() -> Fig:
    rows = [
        [("La selección converge a una hipótesis", "gold"), ("Trece pruebas y el caso de referencia", "teal"), ("Que las hipótesis cubran todas las causas reales", "coral")],
        [("La próxima prueba es una buena elección", "gold"), ("Una puntuación por costo y poder de descarte", "teal"), ("Que la secuencia sea globalmente óptima", "coral")],
        [("El procedimiento es eficiente", "gold"), ("Conteos de operaciones y medición", "teal"), ("Que otro entorno o tamaño mantenga la proporción", "coral")],
    ]
    return chain_rows(
        "Lo que la evidencia sostiene y lo que no demuestra",
        "Diagrama de tres afirmaciones del laboratorio con la evidencia que las sostiene y lo que esa evidencia no demuestra: la convergencia a una hipótesis no prueba que las hipótesis cubran todas las causas, la buena elección de la próxima prueba no prueba una secuencia óptima y la eficiencia medida no prueba que otro entorno mantenga la proporción.",
        ["Afirmación", "Evidencia que la sostiene", "Lo que no demuestra"], rows, [280, 280, 280], gap=26,
        note="Cambiar un resultado esperado para que una implementación pase invalida la evidencia: un contraejemplo obliga a revisar la regla, el modelo o el alcance.",
        note_kind="coral", foot=CALC)


FIGURES = {
    "se-049-arbol-de-decision.svg": se049_arbol,
    "se-049-matriz-de-resultados.svg": se049_matriz,
    "se-049-abstraccion-y-limites.svg": se049_abstraccion,
    "se-050-implicacion-y-recipro.svg": se050_implicacion,
    "se-050-filas-y-modelos.svg": se050_filas,
    "se-050-cuantificadores-finitos.svg": se050_cuantificadores,
    "se-051-dependencias-y-ciclo.svg": se051_dependencias,
    "se-051-recorrido-con-ciclo.svg": se051_recorrido,
    "se-051-cierre-transitivo.svg": se051_cierre,
    "se-052-assert-y-optimizacion.svg": se052_assert,
    "se-052-busqueda-binaria-exhaustiva.svg": se052_busqueda,
    "se-052-contratos-del-laboratorio.svg": se052_contrato,
    "se-053-limite-de-recursion.svg": se053_limite,
    "se-053-fibonacci-llamadas.svg": se053_fibonacci,
    "se-053-induccion-comprobada.svg": se053_induccion,
    "se-054-euclides-y-medida.svg": se054_euclides,
    "se-054-collatz.svg": se054_collatz,
    "se-054-oraculo-y-demostracion.svg": se054_oraculo,
    "se-055-duplicar-n.svg": se055_doblar,
    "se-055-teoria-y-medicion.svg": se055_conteo,
    "se-055-capacidad-de-lista.svg": se055_capacidad,
    "se-056-monedas-codicioso.svg": se056_monedas,
    "se-056-vecino-mas-cercano.svg": se056_tsp,
    "se-056-fuerza-bruta.svg": se056_fuerza,
    "se-057-maquina-de-pedido.svg": se057_pedido,
    "se-057-producto-de-maquinas.svg": se057_producto,
    "se-057-alcanzables-e-invariantes.svg": se057_alcanzables,
    "se-058-biseccion.svg": se058_biseccion,
    "se-058-pruebas-intermitentes.svg": se058_intermitentes,
    "se-058-falsa-confianza.svg": se058_confianza,
    "se-059-requisitos-contradictorios.svg": se059_contradiccion,
    "se-059-relajar-un-requisito.svg": se059_relajar,
    "se-059-registro-de-la-decision.svg": se059_preguntas,
    "se-060-trece-pruebas.svg": se060_pruebas,
    "se-060-resolucion-paso-a-paso.svg": se060_resolucion,
    "se-060-limites-de-la-evidencia.svg": se060_limites,
}
