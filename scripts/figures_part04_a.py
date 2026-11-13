"""Figures for SE-049 to SE-060 (values computed or measured with CPython 3.12.9 on Windows 11)."""
from __future__ import annotations

import math

from figure_kit import Fig

CALC = "Resultados calculados con Python 3.12.9; las mediciones de tiempo dependen del equipo."


def _note(f: Fig, y: float, text: str = CALC) -> None:
    f.text(f.width / 2, y, text, 12, "middle", 400, "#5c1f14")


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
    f = Fig(940, 430, "Resultados declarados de cada prueba bajo cada hipótesis",
            "Tabla del modelo: resolve da fail bajo dns y ok bajo tls y http; handshake da blocked bajo dns, fail bajo tls y ok bajo http; request da blocked bajo dns y tls y fail bajo http; "
            "production-capture da unknown bajo todas y no está autorizada.")
    heads = ["Prueba (costo)", "Si es dns", "Si es tls", "Si es http", "Autorizada"]
    rows = [["resolve (1)", "fail", "ok", "ok", "sí"], ["handshake (2)", "blocked", "fail", "ok", "sí"], ["request (3)", "blocked", "blocked", "fail", "sí"], ["production-capture (1)", "unknown", "unknown", "unknown", "no"]]
    f.table(heads, rows, 10, 12, [250, 170, 170, 170, 160], row_h=58, size=14)
    f.box(10, 316, 920, 80, "Cada celda es una predicción que puede refutarse. Una prueba que da el mismo resultado bajo todas las hipótesis (como production-capture, «unknown») no discrimina ni está permitida.", "gold", 13)
    return f


def se049_abstraccion() -> Fig:
    f = Fig(940, 430, "Qué conserva y qué descarta el modelo",
            "Tabla de lo que el modelo conserva (hipótesis, pruebas, costos, autorización, presupuesto) y lo que descarta (distribución de latencias, fallos parciales, causas simultáneas), con los límites declarados por el laboratorio.")
    heads = ["Conserva", "Descarta", "Límite declarado"]
    rows = [["Un conjunto cerrado de hipótesis (dns, tls, http)", "Causas simultáneas o que no están en la lista", "El resultado solo es correcto respecto de las hipótesis declaradas"],
            ["Costos y presupuesto de cada prueba", "Costo variable según el momento o la carga", "La puntuación codiciosa no garantiza una secuencia global óptima"],
            ["Resultados deterministas por prueba", "Ruido, variación y fallos intermitentes", "Una medición de tiempo no sustituye el análisis de crecimiento"]]
    f.table(heads, rows, 10, 12, [320, 290, 310], row_h=84, size=12)
    f.box(10, 330, 920, 70, "Toda abstracción es una decisión de qué ignorar. La pregunta útil es qué descarte puede invalidar la conclusión y cómo se detectaría.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-050
def se050_implicacion() -> Fig:
    f = Fig(940, 430, "Tabla de la implicación y dos razonamientos comparados",
            "La implicación p entonces q es falsa solo cuando p es verdadera y q falsa; su contrapositiva es equivalente y su recíproca no lo es, comprobado sobre las cuatro filas.")
    f.table(["p", "q", "p → q"], [["falso", "falso", "verdadero"], ["falso", "verdadero", "verdadero"], ["verdadero", "falso", "FALSO"], ["verdadero", "verdadero", "verdadero"]],
            10, 12, [160, 160, 200], row_h=46, size=14, kinds=["plain", "plain", ("teal", "teal", "coral", "teal")])
    f.box(560, 12, 370, 120, "Contrapositiva (¬q → ¬p): equivalente a p → q en las 4 filas (verificado).", "teal", 13)
    f.box(560, 140, 370, 120, "Recíproca (q → p): NO equivalente: difiere en las filas «falso, verdadero» y «verdadero, falso».", "coral", 13)
    f.box(10, 300, 920, 90, "Falacia frecuente: «si hay un fallo de DNS, no resuelve» no permite concluir que «si no resuelve, hay un fallo de DNS»: el recíproco necesita otras evidencias.", "gold", 13)
    return f


def se050_filas() -> Fig:
    f = Fig(940, 430, "Cuántas filas tiene una tabla de verdad y cuántos modelos tiene una fórmula",
            "Una fórmula con n variables tiene 2 elevado a n filas; enumerar 1 048 576 filas con 20 variables tomó 0,102 segundos en Python. Un ciclo de implicaciones entre n variables tiene solo 2 modelos para n igual a 3, 5 y 10.")
    f.table(["Variables n", "Filas (2^n)", "Observación"], [["10", "1 024", "Se enumera al instante"], ["20", "1 048 576", "0,102 s enumerando en Python"], ["30", "≈ 1 073 millones", "Inviable por enumeración simple"]], 10, 12, [190, 260, 470], row_h=54, size=13)
    f.box(10, 250, 920, 76, "(p1 → p2) ∧ (p2 → p3) ∧ … ∧ (pn → p1) tiene exactamente 2 modelos para n = 3, 5 y 10: todas verdaderas o todas falsas. Las variables de un ciclo de implicaciones son equivalentes.", "teal", 13)
    f.box(10, 338, 920, 60, "La enumeración sirve para comprobar fórmulas pequeñas; para muchas variables se usan solucionadores SAT y razonamiento simbólico.", "grey", 13)
    return f


def se050_cuantificadores() -> Fig:
    f = Fig(940, 400, "Cuantificadores sobre dominios finitos y la verdad vacía",
            "En un dominio finito, todos se comprueba con all y existe con any: all sobre una lista vacía es verdadero y any sobre una lista vacía es falso; las leyes de De Morgan se verificaron en las cuatro filas.")
    f.table(["Expresión", "Resultado", "Lectura"], [["all([])", "True", "Verdad vacía: «todo elemento cumple» es verdadero si no hay elementos"], ["any([])", "False", "No existe ningún elemento que cumpla"], ["¬(a ∧ b) ≡ ¬a ∨ ¬b", "True en las 4 filas", "Ley de De Morgan verificada"]],
            10, 12, [200, 190, 530], row_h=64, size=13)
    f.box(10, 296, 920, 80, "Una regla «todas las pruebas autorizadas pasan» se cumple si no hay ninguna prueba: la verdad vacía puede ocultar un conjunto vacío. Se comprueba además que el conjunto no sea vacío.", "coral", 13)
    return f


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
    f = Fig(940, 400, "Cierre transitivo: una cadena de 20 nodos tiene 190 pares alcanzables",
            "El cierre transitivo de una cadena de 20 nodos contiene 190 pares, que es 20 por 19 dividido entre 2; crece de forma cuadrática con la longitud de la cadena.")
    f.table(["Nodos n en cadena", "Pares alcanzables n(n−1)/2"], [["10", "45"], ["20", "190 (calculado)"], ["100", "4 950"], ["1 000", "499 500"]], 10, 12, [300, 380], row_h=52, size=14)
    f.box(10, 270, 920, 80, "La información derivable (quién depende de quién, directa o indirectamente) puede ser mucho mayor que la declarada: para consultas frecuentes se calcula una vez y se guarda.", "gold", 13)
    return f


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
    f = Fig(940, 430, "Búsqueda binaria: comprobación exhaustiva con y sin error",
            "Se probaron 3234 casos con todos los arreglos ordenados de longitud hasta 6 con valores de 0 a 4 y valores de búsqueda de -1 a 5: la versión correcta cometió 0 fallos y la versión con hi = mid cometió 1181, incluidos casos donde no termina.")
    f.table(["Versión", "Casos", "Fallos", "Qué ocurre"], [["hi = mid − 1 (correcta)", "3234", "0", "Termina y devuelve la posición o −1"], ["hi = mid (error)", "3234", "1181", "Puede no terminar: lo detecta un límite de vueltas"]],
            10, 12, [290, 120, 120, 390], row_h=66, size=13, kinds=["plain", "plain", ("teal", "coral"), "plain"])
    f.box(10, 250, 920, 76, "En un dominio pequeño se prueba todo: pocos valores bastan para exponer el error de borde. Un invariante (0 ≤ lo ≤ hi + 1 ≤ n) más una medida que decrece (hi − lo) explican por qué la versión correcta termina.", "gold", 13)
    _note(f, 360)
    return f


def se052_contrato() -> Fig:
    f = Fig(940, 430, "Contratos del laboratorio: precondición, invariante y poscondición",
            "Tabla de tres contratos del laboratorio de la Parte 04: el presupuesto es una precondición, las pruebas elegidas son un subconjunto de las autorizadas (invariante) y una observación contradictoria falla de forma visible.")
    heads = ["Tipo", "Contrato del laboratorio", "Qué pasa si se viola"]
    rows = [["Precondición", "El presupuesto cubre el costo de la prueba elegida", "La selección falla con un error explícito"],
            ["Invariante", "Los candidatos restantes son un subconjunto de las hipótesis", "No puede crecer: una observación solo descarta"],
            ["Poscondición", "Observaciones contradictorias se informan en lugar de ocultarse", "La ejecución falla en voz alta con el conflicto"]]
    f.table(heads, rows, 10, 12, [190, 410, 320], row_h=84, size=12)
    f.box(10, 330, 920, 70, "Un contrato convierte «debería funcionar» en una frase comprobable: quién debe qué, antes, durante y después. Violarlo es un defecto del llamador (precondición) o de la implementación (poscondición).", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-053
def se053_limite() -> Fig:
    f = Fig(940, 400, "La recursión tiene profundidad finita",
            "Con el límite por defecto de 1000, una función recursiva simple alcanzó una profundidad máxima de 999 antes de lanzar RecursionError; json.loads sobre una estructura anidada 100000 veces también lanzó RecursionError.")
    f.table(["Prueba", "Resultado", "Lectura"], [["sys.getrecursionlimit()", "1000", "Límite por defecto del intérprete"], ["Profundidad alcanzada por una recursión simple", "999", "Quedan marcos para el propio manejo del error"], ["json.loads con 100 000 niveles de anidación", "RecursionError", "Una entrada hostil puede agotar la pila"]], 10, 12, [360, 190, 370], row_h=62, size=13)
    f.box(10, 290, 920, 80, "Una definición recursiva correcta puede fallar por profundidad. Entradas de tamaño no acotado (JSON, árboles, expresiones) exigen límites de profundidad o una versión iterativa con pila explícita.", "coral", 13)
    return f


def se053_fibonacci() -> Fig:
    f = Fig(940, 400, "Recursión ingenua frente a memoización: fib(27)",
            "Calcular fib(27) con la definición recursiva directa hace 635 621 llamadas y tarda 0,097 segundos; con memoización hace 28 cálculos únicos y tarda 21 microsegundos.")
    f.text(20, 28, "Cálculo de fib(27) = 196 418", 14, "start", 700)
    f.table(["Versión", "Llamadas / cálculos", "Tiempo"], [["Recursiva directa", "635 621", "0,097 s"], ["Con memoización (lru_cache)", "28 cálculos únicos", "0,000021 s"]], 10, 44, [380, 280, 260], row_h=60, size=14, kinds=["plain", ("coral", "teal"), "plain"])
    f.box(10, 220, 920, 90, "Las llamadas se solapan: los mismos subproblemas se recalculan exponencialmente. La memoización los resuelve una vez cada uno: la estructura de la recursión es la misma, la complejidad cambia de exponencial a lineal.", "gold", 13)
    _note(f, 350)
    return f


def se053_induccion() -> Fig:
    f = Fig(940, 420, "Inducción: caso base, paso y comprobación",
            "Para demostrar que la suma de 0 a n es n por n más 1 entre 2: caso base n igual a 0, paso inductivo de n a n más 1, y comprobación computacional para n de 0 a 1999 sin excepciones. La comprobación no sustituye la demostración.")
    f.table(["Paso", "Contenido"], [["Caso base", "n = 0: la suma es 0 y 0·1/2 = 0"], ["Hipótesis inductiva", "Se cumple para n: Σ = n(n+1)/2"], ["Paso", "Σ hasta n+1 = n(n+1)/2 + (n+1) = (n+1)(n+2)/2"], ["Comprobación", "Verificada para n = 0 … 1999: sin contraejemplos"]], 10, 12, [230, 690], row_h=54, size=13)
    f.box(10, 296, 920, 90, "Probar muchos casos no demuestra la propiedad: solo la inducción cubre todos los n. A la inversa, una demostración puede contener un error: por eso se contrasta con casos.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-054
def se054_euclides() -> Fig:
    f = Fig(940, 400, "Algoritmo de Euclides: terminación por una medida que decrece",
            "El máximo común divisor de 1071 y 462 es 21 y se obtiene en 3 pasos; para dos números de Fibonacci consecutivos, 987 y 610, se obtiene 1 en 14 pasos, el peor caso. La medida b decrece estrictamente en cada paso.")
    f.table(["Entrada", "Resultado", "Pasos"], [["gcd(1071, 462)", "21", "3"], ["gcd(987, 610): Fibonacci consecutivos", "1", "14 (peor caso)"]], 10, 12, [420, 230, 270], row_h=60, size=14)
    f.box(10, 220, 920, 90, "Correctitud: gcd(a, b) = gcd(b, a mod b). Terminación: b disminuye en cada paso y no puede bajar de 0. Costo: proporcional al logaritmo de la entrada; el peor caso son números de Fibonacci consecutivos.", "gold", 13)
    return f


def se054_collatz() -> Fig:
    f = Fig(940, 400, "Cuando la terminación no se sabe demostrar: la conjetura de Collatz",
            "Para los números hasta 100 000, el que más pasos necesita es 77 031 con 350 pasos hasta llegar a 1. Que todos terminen no está demostrado en general.")
    f.table(["Rango probado", "Número más largo", "Pasos"], [["1 … 99 999", "77 031", "350"]], 10, 12, [330, 330, 260], row_h=60, size=14)
    f.box(10, 130, 920, 90, "El procedimiento (si es par, dividir entre 2; si no, multiplicar por 3 y sumar 1) termina para todo n probado, pero no hay demostración general. Sin una medida que decrezca, la terminación es una conjetura.", "coral", 13)
    f.box(10, 232, 920, 76, "Un programa cuya terminación depende de un problema abierto necesita un límite de pasos o un plazo, como el que protege cualquier ciclo en producción.", "gold", 13)
    return f


def se054_oraculo() -> Fig:
    f = Fig(940, 400, "Probar contra un oráculo y lo que no demuestra",
            "Un ordenamiento de burbuja coincidió con sorted en 2000 casos aleatorios de longitud hasta 30; eso aporta evidencia, no una demostración de corrección.")
    f.table(["Evidencia", "Qué aporta", "Qué no aporta"], [["2000 casos aleatorios: burbuja = sorted", "Confianza en esos casos y en su distribución", "Garantía para todos los arreglos ni para tamaños grandes"], ["Argumento de invariante (cola ordenada)", "Prueba para toda entrada si es correcto", "Que el código implemente el argumento"]], 10, 12, [330, 290, 300], row_h=84, size=12)
    f.box(10, 270, 920, 90, "Pruebas y demostraciones se complementan: una exhibe fallos concretos y la otra cubre todos los casos. Un contraejemplo invalida el algoritmo; la ausencia de contraejemplos no lo valida.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-055
def se055_doblar() -> Fig:
    f = Fig(960, 440, "Duplicar n: la razón de tiempos revela el crecimiento",
            "Tabla con medianas medidas para n igual a 4000 y 8000: la búsqueda lineal pasa de 5,9 a 11,7 ms (razón 1,99), la búsqueda por hash se mantiene en 0,02 ms (razón 0,99), la ordenación pasa de 0,48 a 1,01 ms (razón 2,10) y el doble bucle de 5,9 a 171,6 ms (razón 4,30 sobre n/4).")
    heads = ["Operación", "n = 2000", "n = 4000", "n = 8000", "Razón 8000/4000", "Crecimiento"]
    rows = [["Búsqueda lineal (in en lista)", "2,96 ms", "5,89 ms", "11,74 ms", "1,99", "≈ n"],
            ["Búsqueda por hash (in en set)", "0,020 ms", "0,020 ms", "0,020 ms", "0,99", "≈ 1"],
            ["Ordenación (sorted)", "0,22 ms", "0,48 ms", "1,01 ms", "2,10", "≈ n log n"],
            ["Doble bucle sobre n/4", "9,64 ms", "39,89 ms", "171,63 ms", "4,30", "≈ n²"]]
    f.table(heads, rows, 10, 12, [300, 120, 120, 130, 140, 130], row_h=62, size=12)
    f.box(10, 330, 940, 70, "Si duplicar n multiplica el tiempo por ≈2, el crecimiento es lineal; por ≈4, cuadrático; por ≈1, constante. La razón se mide, no se supone.", "gold", 13)
    _note(f, 424)
    return f


def se055_conteo() -> Fig:
    f = Fig(940, 400, "Teoría y medición: dos fuentes que deben coincidir",
            "Tabla que contrasta la razón teórica esperada al duplicar n con la razón medida: lineal 2 frente a 1,99, hash 1 frente a 0,99, n log n un poco más de 2 frente a 2,10 y cuadrático 4 frente a 4,30.")
    f.table(["Operación", "Razón teórica al duplicar n", "Razón medida"], [["Lineal", "2", "1,99"], ["Hash", "1", "0,99"], ["n log n", "2 + pequeño (≈2,1)", "2,10"], ["Cuadrática", "4", "4,30"]], 10, 12, [300, 340, 280], row_h=54, size=14)
    f.box(10, 290, 920, 76, "Cuando la medición discrepa mucho de la teoría hay un error de análisis, de medición o un efecto de caché o del intérprete; ninguna de las dos fuentes sustituye a la otra.", "gold", 13)
    return f


def se055_capacidad() -> Fig:
    f = Fig(940, 400, "Costo amortizado: cómo crece la capacidad de una lista",
            "Al añadir elementos uno por uno, el tamaño en bytes de una lista de Python cambia solo en algunos puntos: 88 bytes con 1 elemento, 120 con 5, 184 con 9, 248 con 17, 312 con 25 y 376 con 33; la mayoría de las inserciones no reservan memoria.")
    f.table(["Elementos al reservar", "Bytes de la lista", "Lectura"], [["1", "88", "Primera reserva"], ["5", "120", "Crece"], ["9", "184", "Crece"], ["17", "248", "Crece"], ["25", "312", "Crece"], ["33", "376", "Crece"]], 10, 12, [260, 240, 420], row_h=40, size=13)
    f.box(10, 340, 920, 50, "Cada reserva es costosa y rara: el costo promedio por inserción es constante (amortizado), aunque una inserción concreta pueda ser lenta.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-056
def se056_monedas() -> Fig:
    f = Fig(940, 400, "El algoritmo codicioso falla con monedas 1, 3 y 4",
            "Para devolver 6 con monedas de 1, 3 y 4, el algoritmo codicioso usa 4, 1 y 1 (3 monedas) y la solución óptima usa 3 y 3 (2 monedas). En el rango hasta 60, el mayor exceso del codicioso ocurre en el monto 6.")
    f.table(["Estrategia", "Monedas para 6", "Cantidad"], [["Codiciosa: la mayor posible primero", "4 + 1 + 1", "3"], ["Programación dinámica (óptima)", "3 + 3", "2"]], 10, 12, [420, 260, 240], row_h=60, size=14, kinds=["plain", "plain", ("coral", "teal")])
    f.box(10, 220, 920, 90, "La heurística es correcta con monedas de un sistema canónico (1, 5, 10, 25) y falla con otros conjuntos: un solo contraejemplo basta para refutar que sea óptima en general.", "gold", 13)
    f.box(10, 322, 920, 50, "Una heurística se acompaña de su contraejemplo y de la condición en que funciona.", "grey", 13)
    return f


def se056_tsp() -> Fig:
    f = Fig(940, 400, "Vecino más cercano frente al óptimo: 100 instancias de 8 ciudades",
            "En 100 instancias aleatorias de 8 ciudades, la heurística del vecino más cercano produjo un recorrido de media 1,086 veces el óptimo, en el peor caso 1,318 veces y en el mejor 1,0.")
    f.table(["Medida (recorrido heurístico / óptimo)", "Valor"], [["Razón media", "1,086"], ["Peor caso observado", "1,318"], ["Mejor caso", "1,000"]], 10, 12, [560, 300], row_h=58, size=14)
    f.box(10, 220, 920, 80, "La heurística es rápida y, en promedio, razonable; en el peor caso observado un 32 % peor. No hay garantía general: se conoce la razón en la muestra, no el máximo en todos los casos.", "gold", 13)
    _note(f, 340, "100 instancias con semilla 5; el óptimo se calculó por fuerza bruta (7! permutaciones por instancia).")
    return f


def se056_fuerza() -> Fig:
    f = Fig(940, 400, "La fuerza bruta crece factorialmente",
            "El tiempo de resolver el viajante por fuerza bruta pasó de 0,002 s con 7 ciudades a 0,012 s con 8 y 0,110 s con 9: cada ciudad adicional multiplica el tiempo por 6 a 9, coherente con las permutaciones (n−1)!.")
    f.table(["Ciudades n", "Permutaciones (n−1)!", "Tiempo"], [["7", "720", "0,002 s"], ["8", "5 040", "0,012 s"], ["9", "40 320", "0,110 s"], ["12 (extrapolado)", "39 916 800", "≈ horas con este método"]], 10, 12, [260, 340, 320], row_h=54, size=13)
    f.box(10, 300, 920, 76, "Un algoritmo exacto de crecimiento factorial se vuelve inviable muy pronto; por eso existen heurísticas y aproximaciones, con sus garantías y límites declarados.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-057
def se057_pedido() -> Fig:
    f = Fig(960, 430, "Máquina de estados de un pedido",
            "Seis estados (nuevo, pagado, enviado, entregado, cancelado, devuelto) y cinco eventos definen 30 pares estado-evento, de los cuales 6 son transiciones legales y 24 son ilegales y deben rechazarse.")
    f.table(["Estado", "Evento", "Siguiente estado"], [["nuevo", "pagar", "pagado"], ["nuevo", "cancelar", "cancelado"], ["pagado", "enviar", "enviado"], ["pagado", "cancelar", "cancelado"], ["enviado", "entregar", "entregado"], ["enviado", "devolver", "devuelto"]], 10, 12, [200, 200, 240], row_h=40, size=13)
    f.box(680, 12, 270, 130, "6 estados × 5 eventos = 30 pares; 6 legales; 24 ilegales.", "gold", 13, bold=True)
    f.box(680, 150, 270, 160, "Un evento ilegal (por ejemplo, enviar un pedido nuevo) se rechaza de forma explícita: no se ignora ni cambia el estado.", "coral", 13)
    f.box(10, 340, 940, 56, "El modelo hace visible lo que antes era implícito: qué está permitido en cada estado y qué no.", "grey", 13)
    return f


def se057_producto() -> Fig:
    f = Fig(940, 400, "Explosión de estados al combinar máquinas",
            "Combinar máquinas independientes multiplica sus estados: 6 por 5 son 30, 6 por 5 por 4 son 120 y 6 por 5 por 4 por 4 por 3 son 1440; un sistema de cinco componentes pequeños ya tiene más de mil estados.")
    f.table(["Máquinas combinadas", "Estados del producto"], [["6 × 5", "30"], ["6 × 5 × 4", "120"], ["6 × 5 × 4 × 4 × 3", "1 440"]], 10, 12, [460, 400], row_h=58, size=14)
    f.box(10, 220, 920, 90, "Razonar sobre el producto a mano es inviable: se modelan los componentes por separado, se declaran las interacciones y se explora el espacio de estados con una herramienta (verificación de modelos).", "gold", 13)
    return f


def se057_alcanzables() -> Fig:
    f = Fig(940, 400, "Estados alcanzables e invariantes del pedido",
            "Una exploración desde el estado nuevo alcanza los 6 estados del pedido; los invariantes se comprueban sobre los estados alcanzables, no sobre todas las combinaciones posibles.")
    f.table(["Pregunta", "Resultado"], [["¿Cuántos estados son alcanzables desde «nuevo»?", "6 de 6"], ["¿Se puede llegar a «entregado» sin pasar por «pagado»?", "No: hay que pasar por pagado y enviado"], ["¿Se puede devolver un pedido cancelado?", "No: no hay transición desde cancelado"]], 10, 12, [560, 340], row_h=62, size=13)
    f.box(10, 290, 920, 76, "Un invariante como «entregado implica pagado» se verifica recorriendo los estados alcanzables; si algún estado lo viola, el modelo (o la regla) está mal.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-058
def se058_biseccion() -> Fig:
    f = Fig(940, 400, "Búsqueda binaria de una causa: pasos necesarios",
            "Localizar una modificación defectuosa entre 1024 cambios ordenados requiere 10 pruebas y entre un millón requiere 20; cada prueba descarta la mitad de los candidatos.")
    f.table(["Cambios candidatos", "Pruebas (≈ log2 n)", "Ejemplo observado"], [["1 024", "10", "defecto en el cambio 700 hallado en 10 pasos"], ["1 000 000", "20", "defecto en el cambio 123 456 hallado en 20 pasos"]], 10, 12, [260, 240, 420], row_h=64, size=13)
    f.box(10, 220, 920, 90, "La biseccion (git bisect) exige una prueba determinista y la suposición de monotonía: todo cambio anterior al defecto es sano y todo cambio posterior lo contiene. Si la prueba es intermitente, el resultado no es fiable.", "gold", 13)
    return f


def se058_intermitentes() -> Fig:
    f = Fig(940, 410, "Pruebas intermitentes: cuántas repeticiones para reproducir un fallo",
            "Para reproducir con 95 % de confianza un fallo que ocurre en una fracción p de las ejecuciones se necesitan 5 corridas si p vale 0,5; 29 si vale 0,1 y 299 si vale 0,01; una simulación con p igual a 0,1 y 29 corridas lo observó en 95,2 % de los intentos.")
    f.table(["Probabilidad de fallo por corrida", "Corridas para verlo con 95 %", "Fórmula"], [["0,5", "5", "⌈ln(0,05) / ln(1 − p)⌉"], ["0,1", "29", "⌈ln(0,05) / ln(1 − p)⌉"], ["0,01", "299", "⌈ln(0,05) / ln(1 − p)⌉"]], 10, 12, [330, 290, 300], row_h=56, size=13)
    f.box(10, 250, 920, 76, "Simulación (10 000 intentos, p = 0,1, 29 corridas): el fallo apareció en el 95,2 %, coherente con la fórmula.", "teal", 13)
    f.box(10, 338, 920, 56, "Un fallo raro exige muchas corridas: «no lo reproduje» con pocas corridas no es evidencia de que no exista.", "coral", 13)
    return f


def se058_confianza() -> Fig:
    f = Fig(940, 400, "Falsa confianza: pasar cinco veces no descarta un fallo intermitente",
            "Si un fallo ocurre en el 10 % de las corridas, la probabilidad de que cinco corridas seguidas pasen aunque el defecto exista es 0,9 elevado a 5, es decir 0,59.")
    f.table(["Situación", "Probabilidad"], [["Defecto presente (p = 0,1) y cinco corridas pasan", "0,9^5 = 0,59"], ["Defecto presente y se observa al menos una falla en cinco corridas", "1 − 0,59 = 0,41"]], 10, 12, [600, 300], row_h=62, size=14)
    f.box(10, 220, 920, 90, "Con un 59 % de probabilidad, «lo corregí porque ahora pasa cinco veces» es una conclusión que falla más de la mitad de las veces. Se registra la hipótesis, la predicción y el número de corridas planificado antes de concluir.", "coral", 13)
    return f


# ---------------------------------------------------------------- SE-059
def se059_contradiccion() -> Fig:
    f = Fig(960, 430, "Tres requisitos que juntos no tienen solución",
            "Tabla con tres requisitos: cifrado extremo a extremo, búsqueda en el servidor e «índice en servidor requiere texto en claro». De las 4 configuraciones posibles (cifrado e2e o de transporte, índice en servidor o en cliente), ninguna satisface los tres.")
    f.table(["Configuración", "Cifrado e2e", "Búsqueda en servidor", "Sin índice en claro en servidor", "¿Cumple los 3?"],
            [["e2e + índice en servidor", "sí", "sí", "no", "no"], ["e2e + índice en cliente", "sí", "no", "sí", "no"], ["transporte + índice en servidor", "no", "sí", "sí", "no"], ["transporte + índice en cliente", "no", "no", "sí", "no"]],
            10, 12, [290, 130, 190, 210, 120], row_h=52, size=12)
    f.box(10, 310, 940, 80, "Ninguna de las 4 configuraciones satisface los tres requisitos: la contradicción es del conjunto, no de la implementación. Se detecta enumerando el espacio pequeño antes de construir nada.", "gold", 13)
    return f


def se059_relajar() -> Fig:
    f = Fig(940, 400, "Relajar un requisito: lo que cambia y lo que cuesta",
            "Al relajar el requisito de búsqueda en el servidor queda una única configuración válida: cifrado extremo a extremo con el índice en el cliente. La decisión de qué requisito relajar es de negocio, con consecuencias para quienes lo usan.")
    f.table(["Requisito relajado", "Configuraciones válidas", "Costo para la persona usuaria"], [["Búsqueda en el servidor", "1: e2e + índice en el cliente", "La búsqueda ocurre en el dispositivo: más datos locales, más tiempo"], ["Cifrado extremo a extremo", "Más de una", "El servidor puede leer los datos"]], 10, 12, [260, 300, 360], row_h=84, size=12)
    f.box(10, 280, 920, 80, "El análisis no decide por la persona: muestra qué se gana y qué se pierde con cada relajación, y deja la decisión a quien tenga autoridad y a quienes resultan afectados.", "gold", 13)
    return f


def se059_preguntas() -> Fig:
    f = Fig(940, 400, "Preguntas abiertas y registro de la decisión",
            "Al encontrar una contradicción se registran preguntas abiertas, las opciones, quién decide y el plazo; no se escoge en silencio.")
    f.table(["Elemento del registro", "Contenido"], [["Contradicción", "Los tres requisitos no tienen solución conjunta (0 de 4 configuraciones)"], ["Opciones", "Relajar la búsqueda en servidor, relajar e2e o cambiar el alcance"], ["Quién decide", "Propietario del producto con asesoría de seguridad; las personas afectadas se consultan"], ["Preguntas abiertas", "¿Qué dato necesita realmente buscarse? ¿Con qué latencia? ¿Qué riesgo se acepta?"]], 10, 12, [260, 660], row_h=56, size=12)
    f.box(10, 300, 920, 76, "Una contradicción no resuelta que se oculta reaparece como un defecto en producción; una que se registra es una decisión revisable.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-060
def se060_pruebas() -> Fig:
    f = Fig(960, 470, "Las trece pruebas del laboratorio y el contrato que cada una protege",
            "Tabla con las trece pruebas del laboratorio de la Parte 04: especificación completa, resultado ausente rechazado, conflicto visible, implicación con una fila falsa, grafo con ciclo, máquina de estados, selector, invariante de subconjunto, observación contradictoria, presupuesto, caso de referencia, conteos y salida legible. Pasaron en Windows (0,167 s) y en Linux (0,245 s).")
    heads = ["Grupo", "Pruebas", "Contrato"]
    rows = [["Especificación", "completa · resultado ausente rechazado · conflicto sin resolver visible", "Datos de entrada válidos y conflictos explícitos"],
            ["Razonamiento", "implicación con una fila falsa · grafo con ciclo termina · máquina de estados rechaza lo imposible", "Lógica, terminación y estados"],
            ["Selección y observación", "excluye pruebas no autorizadas · el subconjunto se preserva · observación contradictoria falla · presupuesto como precondición", "Invariantes y precondiciones"],
            ["Evidencia", "caso de referencia se resuelve con traza · conteos separan teoría de tiempo · salida legible por máquina", "Trazabilidad y límites"]]
    f.table(heads, rows, 10, 12, [190, 480, 270], row_h=84, size=12)
    f.box(10, 420, 940, 40, "13 pruebas: Windows 11 (Python 3.12.9) 0,167 s; Linux (WSL2, Python 3.12.3) 0,245 s.", "gold", 12)
    return f


def se060_resolucion() -> Fig:
    f = Fig(940, 430, "Resolución del caso de referencia, paso a paso",
            "Con la especificación y las observaciones de referencia: resolve da ok y deja tls y http como candidatos con costo 1; handshake da fail y deja solo tls con costo acumulado 3; el estado es resolved, con presupuesto restante 2.")
    f.table(["Paso", "Prueba", "Resultado", "Candidatos restantes", "Costo acumulado"], [["1", "resolve", "ok", "tls, http", "1"], ["2", "handshake", "fail", "tls", "3"]], 10, 12, [100, 220, 160, 260, 180], row_h=60, size=14)
    f.box(10, 190, 920, 60, "Estado final: resolved · candidatos: [tls] · gastado 3 de 5 · presupuesto restante 2 · próxima prueba: ninguna.", "teal", 13, bold=True)
    f.box(10, 262, 920, 90, "«Resuelto» significa que, dentro del modelo, solo queda una hipótesis compatible con las observaciones. No significa que el mundo real esté completo ni que las premisas sean verdaderas.", "gold", 13)
    return f


def se060_limites() -> Fig:
    f = Fig(940, 430, "Lo que la evidencia sostiene y lo que no",
            "Tres límites declarados por el laboratorio: el resultado es correcto solo respecto de las hipótesis y resultados declarados, la heurística codiciosa no es óptima global y una medición de tiempo no sustituye el análisis de crecimiento.")
    f.table(["Afirmación", "Evidencia que la sostiene", "Lo que no demuestra"], [["La selección converge a una hipótesis", "Trece pruebas y el caso de referencia", "Que las hipótesis cubran todas las causas reales"], ["La próxima prueba es una buena elección", "Una puntuación por costo y poder de descarte", "Que la secuencia sea globalmente óptima"], ["El procedimiento es eficiente", "Conteos de operaciones y medición", "Que otro entorno o tamaño mantenga la proporción"]], 10, 12, [290, 320, 310], row_h=84, size=12)
    f.box(10, 340, 920, 70, "Cambiar un resultado esperado para que una implementación pase invalida la evidencia: un contraejemplo obliga a revisar la regla, el modelo o el alcance.", "coral", 13)
    return f


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
