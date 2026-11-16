"""Figures for SE-073 to SE-078 (CPython 3.12.9 on Windows 11 and 3.12.3 on Ubuntu 24.04 under WSL2)."""
from __future__ import annotations

from figure_flow_rows import chain_rows
from figure_kit import Fig, grouped_bars


OBS = "Medido con CPython 3.12 en un equipo concreto; las magnitudes cambian con la máquina, el orden relativo es lo que importa."


def _note(f: Fig, y: float, text: str = OBS) -> None:
    f.text(f.width / 2, y, text, 12, "middle", 400, "#5c1f14")


# ---------------------------------------------------------------- SE-073
def se073_alias() -> Fig:
    return grouped_bars(
        "Costo de aislar estado: copia superficial frente a copia profunda de un diccionario de mil claves con listas",
        "Barras agrupadas en escala logarítmica con el costo de copiar un diccionario de mil claves con listas: la copia superficial tarda unos 9,7 microsegundos en Windows y 9,6 en Linux; deepcopy tarda unos 4 900 en Windows y 4 100 en Linux; la asignación b igual a a no cuesta nada porque solo crea un nombre nuevo.",
        ["dict(a) o copy.copy(a): otro contenedor, mismas listas internas", "copy.deepcopy(a): copia recursiva, todo aislado"],
        [("Windows", [9.7, 4900], "gold"), ("Linux", [9.6, 4100], "teal")],
        unit="Microsegundos por copia", horizontal=True, log=True, label_w=330,
        note="b = a no copia nada: comparte todo. La copia superficial comparte las listas internas; deepcopy las aísla y cuesta unas 500 veces más. Una función que devuelve estado nuevo cuesta según lo que copie. Aislar estado es una decisión de costo, no un hábito gratuito.",
        note_kind="gold", foot=OBS)


def se073_retorno() -> Fig:
    f = Fig(960, 400, "Un retorno temprano deja el estado a medias; copiar y confirmar lo evita",
            "Dos columnas: en la versión mutante, score pasa de 2 a 5 y la función devuelve rechazo, de modo que el estado queda modificado aunque se rechazó; "
            "en la versión que copia y confirma, el rechazo devuelve el estado original sin cambios.")
    f.text(240, 30, "Versión que muta en sitio", 15, "middle", 700)
    f.text(720, 30, "Versión que copia y confirma", 15, "middle", 700)
    f.box(40, 44, 400, 50, "Antes: {score: 2}", "plain", 13)
    f.box(40, 120, 400, 50, "state[score] += 3  →  score = 5", "coral", 13)
    f.box(40, 196, 400, 50, "if rechazo: return «rechazo»  (sin registrar next)", "coral", 13)
    f.box(40, 272, 400, 56, "Después: {score: 5}  ← rechazado, pero modificado", "coral", 13, bold=True)
    f.box(520, 44, 400, 50, "Antes: {score: 2}", "plain", 13)
    f.box(520, 120, 400, 50, "nuevo = dict(state); nuevo[score] += 3", "teal", 13)
    f.box(520, 196, 400, 50, "if rechazo: return «rechazo», state  (original)", "teal", 13)
    f.box(520, 272, 400, 56, "Después: {score: 2}  ← rechazo sin efecto", "teal", 13, bold=True)
    for x in (240, 720):
        for y in (94, 170, 246):
            f.arrow([(x, y), (x, y + 26)])
    f.box(40, 340, 880, 40, "Ejecutado: el primer caso devuelve «rechazo» con {score: 5}; el segundo devuelve «rechazo» y conserva {score: 2}.", "gold", 12)
    return f


def se073_sorpresas() -> Fig:
    rows = [
        [("Dos reglas sobre la misma prioridad (+2 y ×3), partiendo de 1", "plain"), ("r1 luego r2 = 9; r2 luego r1 = 5", "gold"), ("La secuencia es parte de la semántica: las operaciones no conmutan", "plain")],
        [("def f(x, acc=[]) llamada tres veces", "plain"), ("[1], luego [1, 2], luego [1, 2, 3]: el mismo objeto", "gold"), ("El valor por defecto se crea una vez, al definir la función", "plain")],
        [("Atributo _bal de una cuenta con property sin setter", "plain"), ("a.bal = 99 falla; a._bal = -100 funciona", "gold"), ("El guion bajo es convención, no barrera: la invariante debe vivir en un método", "plain")],
    ]
    return chain_rows(
        "Tres sorpresas de estado mutable observadas en Python, de la observación a su causa",
        "Diagrama de tres observaciones y su causa: el orden de dos reglas que modifican la misma prioridad produce 9 o 5; un argumento por defecto mutable acumula las listas 1; 1 y 2; 1, 2 y 3; y un atributo con guion bajo se puede dejar en -100 porque la privacidad es solo una convención.",
        ["Observación", "Resultado ejecutado", "Causa"], rows, [290, 270, 290], gap=26,
        note="Cada sorpresa desaparece al hacer explícito quién posee el estado y cuándo cambia.",
        note_kind="gold", foot=OBS)


# ---------------------------------------------------------------- SE-074
def se074_llamar() -> Fig:
    f = Fig(940, 350, "Costo de extraer una función: el mismo bucle en línea y llamando a una función",
            "Barras por iteración: en Windows el bucle en línea tarda unos 105 ns y con una llamada a función unos 161 ns; en Linux unos 96 ns y 134 ns. "
            "La llamada añade entre 40 % y 54 %, que es costo fijo por llamada, no por línea.")
    f.text(20, 28, "Nanosegundos por iteración (mediana de siete repeticiones)", 14, "start", 700)
    f.hbars([("Windows, en línea", 104.6, "teal", "105 ns"), ("Windows, con función", 160.8, "coral", "161 ns"),
             ("Linux, en línea", 95.8, "teal", "96 ns"), ("Linux, con función", 133.9, "coral", "134 ns")],
            20, 44, 3.4, label_w=210, step=46)
    f.box(20, 238, 900, 64, "La extracción cuesta decenas de nanosegundos por llamada. Solo domina si la función hace muy poco trabajo y se invoca millones de veces; "
          "en el resto de los casos la claridad de un contrato estrecho pesa más.", "gold", 13)
    _note(f, 336)
    return f


def se074_recursion() -> Fig:
    rows = [
        [("Límite por defecto", "plain"), ("sys.getrecursionlimit() = 1000; se alcanzó profundidad 998", "coral"), ("La pila de llamadas es un recurso finito con tope configurable", "plain")],
        [("Límite elevado a 100000, recursión de 50000", "plain"), ("Devolvió 50000 en Windows y en Linux", "teal"), ("Funciona, pero el tope existe para proteger el proceso de agotar la pila de C", "plain")],
        [("Cuenta atrás con bucle y acumulador", "plain"), ("Sin límite de profundidad", "teal"), ("Cuando la descomposición es lineal, un bucle es más seguro", "plain")],
    ]
    return chain_rows(
        "El límite de recursión de CPython frente a una descomposición recursiva",
        "Diagrama de tres situaciones: con el límite por defecto de 1000 la recursión se detiene en profundidad 998 con RecursionError; elevando el límite a 100000 una recursión de 50000 niveles funciona en ambos sistemas; una iteración con pila explícita no depende del límite.",
        ["Situación", "Resultado observado", "Lectura"], rows, [260, 300, 290], gap=26,
        note="El límite se eleva con sys.setrecursionlimit, pero un valor excesivo puede cerrar el intérprete en vez de lanzar RecursionError.",
        note_kind="coral", foot=OBS)


def se074_efectos() -> Fig:
    rows = [
        [("impure(x) agrega a una lista y devuelve x + 1; con lru_cache; tres llamadas con 1", "plain"), ("1 efecto registrado en 3 llamadas", "coral"), ("Memoizar una función con efecto cambia el comportamiento; solo es válido si es pura", "plain")],
        [("mut(l): l.append(1) y rebind(l): l = [9]", "plain"), ("Tras ambas, la lista del llamador es [1]", "gold"), ("Los argumentos pasan por referencia al objeto: mutar se ve, reasignar el nombre local no", "plain")],
        [("pure(x) = x + 1 con la misma envoltura", "plain"), ("Mismo resultado con y sin caché", "teal"), ("La pureza es lo que permite sustituir una llamada por su resultado", "plain")],
    ]
    return chain_rows(
        "Efectos ocultos en funciones: caché de una función con efecto y paso de objetos",
        "Diagrama de tres experimentos: al envolver con lru_cache una función que registra un efecto, tres llamadas producen un solo efecto; una función que añade a la lista recibida modifica la lista del llamador mientras reasignar el parámetro no; y una función pura se puede memoizar sin cambiar su significado.",
        ["Experimento", "Resultado ejecutado", "Consecuencia para el diseño"], rows, [290, 250, 290], gap=26,
        note="Un contrato de procedimiento debe declarar si lee, escribe o solo calcula.",
        note_kind="gold", foot=OBS)


# ---------------------------------------------------------------- SE-075
def se075_slots() -> Fig:
    f = Fig(940, 340, "Memoria por objeto: instancia con diccionario frente a __slots__",
            "Barras con 100000 objetos de tres atributos: unos 96 bytes por objeto con diccionario de atributos y unos 64 bytes con __slots__, es decir 9378 KiB frente a 6250 KiB, igual en Windows y en Linux.")
    f.text(20, 28, "Bytes por objeto (tracemalloc, 100000 objetos con tres atributos)", 14, "start", 700)
    f.hbars([("Clase normal (dict)", 96, "coral", "96 B (9378 KiB)"), ("Clase con __slots__", 64, "teal", "64 B (6250 KiB)")],
            20, 50, 4.4, label_w=220, step=52)
    f.box(20, 178, 900, 78, "__slots__ ahorra un tercio de la memoria, pero impide crear atributos nuevos en la instancia y complica la herencia múltiple. "
          "Es una optimización medida, no una regla de diseño.", "gold", 13)
    _note(f, 306)
    return f


def se075_mro() -> Fig:
    f = Fig(960, 440, "Herencia en diamante y encapsulación: lo que garantiza el lenguaje y lo que es convención",
            "Diagrama: la clase D hereda de B y C que heredan de A; el orden de resolución observado es D, B, C, A, object y D().m() devuelve «DBCA». "
            "Debajo, tres mecanismos de encapsulación y su resultado: property sin setter falla, el guion bajo es convención y el prefijo doble guion bajo cambia el nombre a _M__x.")
    f.box(400, 14, 160, 40, "A: m() → «A»", "plain", 13)
    f.box(260, 84, 160, 40, "B(A): «B» + super()", "teal", 12)
    f.box(540, 84, 160, 40, "C(A): «C» + super()", "teal", 12)
    f.box(400, 154, 160, 40, "D(B, C): «D» + super()", "gold", 12)
    f.arrow([(340, 84), (440, 54)]); f.arrow([(620, 84), (520, 54)])
    f.arrow([(440, 154), (340, 124)]); f.arrow([(520, 154), (620, 124)])
    f.text(780, 112, "MRO observado:", 13, "start", 700)
    f.text(780, 132, "D, B, C, A, object", 13, "start")
    f.text(780, 152, "D().m() = «DBCA»", 13, "start")
    widths, gap, x0 = [250, 340, 280], 25, 15
    heads = ["Mecanismo", "Resultado ejecutado", "Garantía real"]
    rows = [[("property sin setter", "plain"), ("a.bal = 99 → AttributeError", "teal"), ("Impide la asignación por ese nombre", "teal")],
            [("_bal con guion bajo", "plain"), ("a._bal = -100 acepta el valor", "coral"), ("Ninguna: es una convención", "coral")],
            [("__x con doble guion bajo", "plain"), ("El atributo se guarda como _M__x", "gold"), ("Evita colisiones, no es seguridad", "gold")]]
    x = x0
    for w, h in zip(widths, heads):
        f.text(x + w / 2, 232, h, 13, "middle", 700, "#5c6b73")
        x += w + gap
    y = 244
    for row in rows:
        x = x0
        for i, ((text, kind), w) in enumerate(zip(row, widths)):
            f.box(x, y, w, 46, text, kind, 12, bold=(i == 0))
            if i < len(row) - 1:
                f.arrow([(x + w + 3, y + 23), (x + w + gap - 3, y + 23)])
            x += w + gap
        y += 58
    return f


def se075_despacho() -> Fig:
    f = Fig(940, 380, "Despacho polimórfico frente a una cadena de condiciones",
            "Barras en nanosegundos por objeto: en Windows el despacho por método tarda unos 135 ns y la condición por tipo unos 110 ns; en Linux unos 108 ns frente a 78 ns. "
            "El polimorfismo cuesta entre 22 % y 38 % más por llamada en este microbenchmark.")
    f.text(20, 28, "Nanosegundos por objeto (mil objetos de dos clases, mediana)", 14, "start", 700)
    f.hbars([("Windows, método", 135.1, "coral", "135 ns"), ("Windows, if por tipo", 110.4, "teal", "110 ns"),
             ("Linux, método", 108.0, "coral", "108 ns"), ("Linux, if por tipo", 78.2, "teal", "78 ns")],
            20, 44, 3.0, label_w=200, step=46)
    f.box(20, 240, 900, 80, "El costo por llamada es pequeño y aparece a escala de millones. A cambio, añadir una tercera clase no modifica el bucle, mientras que la cadena de condiciones "
          "debe editarse en cada lugar donde se pregunta por el tipo.", "gold", 13)
    _note(f, 360)
    return f


# ---------------------------------------------------------------- SE-076
def se076_comprension() -> Fig:
    f = Fig(940, 400, "Filtrar cien mil números de tres maneras",
            "Barras en nanosegundos por elemento: la comprensión de listas tarda 93 ns en Windows y 56 ns en Linux, el bucle con append 98 y 72, y map con filter y lambdas 219 y 227, "
            "unas 2,4 y 4 veces más que la comprensión.")
    f.text(20, 28, "Nanosegundos por elemento (cien mil elementos, mediana)", 14, "start", 700)
    f.hbars([("Win · comprensión", 93.0, "teal", "93 ns"), ("Win · bucle y append", 97.6, "plain", "98 ns"), ("Win · map + filter + lambda", 219.4, "coral", "219 ns"),
             ("Linux · comprensión", 55.9, "teal", "56 ns"), ("Linux · bucle y append", 71.8, "plain", "72 ns"), ("Linux · map + filter + lambda", 227.2, "coral", "227 ns")],
            20, 44, 1.5, label_w=250, step=46)
    f.box(20, 328, 900, 52, "Ser funcional no significa usar map y lambda: en CPython la comprensión es la forma declarativa más rápida; las lambdas añaden una llamada por elemento.", "gold", 12)
    return f


def se076_copiar() -> Fig:
    return grouped_bars(
        "El precio de no mutar: actualizar un elemento de una lista de 10 000 copiando frente a hacerlo en sitio",
        "Barras agrupadas en escala logarítmica con el costo de cambiar un elemento de una lista de 10000: copiando tarda unos 98 291 nanosegundos en Windows y 94 720 en Linux; en sitio, 81 y 56, unas 1 200 veces menos. Calcular fib(25) con memoización hace 26 cálculos y 23 aciertos en vez de recomputar.",
        ["Copiando: lst[:k] + [x] + lst[k+1:]", "En sitio"],
        [("Windows", [98291, 81], "gold"), ("Linux", [94720, 56], "teal")],
        unit="Nanosegundos por actualización", horizontal=True, log=True, label_w=260,
        note="Copiar cuesta O(n) por actualización y en sitio O(1), pero destruye el valor anterior. fib(25) sin memoización tardó 27,2 ms en Windows; con lru_cache hizo 26 fallos y 23 aciertos, válido solo porque fib es pura. Las estructuras persistentes comparten partes; Python no las trae en la biblioteca estándar, así que copiar tiene un costo real que debe medirse.",
        note_kind="coral", foot=OBS)


def se076_cierres() -> Fig:
    rows = [
        [("[lambda: i for i in range(3)]", "plain"), ("[2, 2, 2]; con lambda i=i: i → [0, 1, 2]", "coral"), ("Un cierre captura la variable, no su valor en ese instante", "plain")],
        [("t = (1, [2]); t[1].append(3)", "plain"), ("(1, [2, 3]); t[0] = 9 falla", "gold"), ("Inmutabilidad superficial: la tupla protege sus referencias, no los objetos", "plain")],
        [("compose(inc, dbl)(3) y compose(dbl, inc)(3)", "plain"), ("8 y 7", "gold"), ("Composición asociativa, no conmutativa: el orden es significado", "plain")],
        [("reduce(suma, []) sin valor inicial", "plain"), ("TypeError", "coral"), ("Una operación sin elemento neutro necesita un caso vacío explícito", "plain")],
    ]
    return chain_rows(
        "Cuatro comportamientos funcionales que sorprenden en Python",
        "Diagrama de cuatro experimentos: las lambdas creadas en un bucle ven la variable final y devuelven 2, 2 y 2, mientras que fijar el valor con un argumento por defecto da 0, 1 y 2; una tupla puede contener una lista mutable; la composición no es conmutativa: componer inc y dbl da 8 y dbl e inc da 7; y reduce sobre una lista vacía sin valor inicial falla.",
        ["Experimento", "Resultado ejecutado", "Qué enseña"], rows, [290, 270, 290], gap=26,
        note="Cada sorpresa nace de una regla del lenguaje que se aplica sin avisar: la captura por variable, la inmutabilidad superficial, el orden de la composición y el caso vacío.",
        note_kind="gold", foot=OBS)


# ---------------------------------------------------------------- SE-077
def se077_indice() -> Fig:
    f = Fig(940, 400, "Una consulta declarativa y el plan que elige el motor",
            "Barras en milisegundos para contar observaciones con latencia mayor que 800 y autorizadas en 200000 filas: sin índice el plan es SCAN y tarda unos 31 ms en Windows; "
            "con un índice sobre la latencia el plan es SEARCH USING INDEX y tarda unos 103 ms, es decir más lento, con el mismo resultado de 60000 filas.")
    f.text(20, 28, "Milisegundos por consulta (SQLite 3.45, 200000 filas, mediana)", 14, "start", 700)
    f.hbars([("Win · SCAN obs", 31.2, "teal", "31 ms"), ("Win · SEARCH con índice", 103.4, "coral", "103 ms"),
             ("Linux · SCAN obs", 18.8, "teal", "19 ms"), ("Linux · SEARCH con índice", 79.2, "coral", "79 ms")],
            20, 44, 2.6, label_w=230, step=46)
    f.box(20, 240, 900, 82, "El predicado latency > 800 selecciona el 60 % de las filas; recorrer un índice y saltar a cada fila cuesta más que leer la tabla de corrido. "
          "Declarar qué se quiere no garantiza el mejor camino: el plan se verifica con EXPLAIN QUERY PLAN.", "gold", 13)
    f.box(20, 336, 900, 36, "La consulta no cambió entre las dos mediciones: solo cambió el plan.", "grey", 13)
    return f


def se077_conflictos() -> Fig:
    return grouped_bars(
        "Reglas como datos: cuántas reglas se activan a la vez en 10 000 observaciones sintéticas",
        "Barras con las observaciones según las reglas que activan: ninguna observación queda sin regla, 7511 activan una regla y 2489 activan dos. Para una observación con latencia 900 y no autorizada, usar la primera coincidencia da R1, usar la prioridad da R2 y la lista invertida da R2.",
        ["0 reglas", "1 regla", "2 reglas (conflicto)"],
        [("Observaciones", [0, 7511, 2489], "gold")],
        unit="Observaciones de 10 000", horizontal=True, label_w=170, ticks=[0, 2000, 4000, 6000, 8000],
        note="Para 900 ms y no autorizado: la primera coincidencia con el orden R1, R2, R3 da R1 (inspect-transport); la mayor prioridad (R2 = 2) da R2 (deny); la primera coincidencia con el orden invertido da R2 (deny). El resultado depende de la política de conflictos, que es parte de la regla aunque no figure en ella.",
        note_kind="coral", foot=OBS)


def se077_tabla() -> Fig:
    f = Fig(940, 320, "Tres formas de codificar la misma decisión y su costo por evaluación",
            "Barras en nanosegundos: en Windows una cadena de condiciones tarda unos 363 ns, una tabla de decisión 585 ns y un motor con reglas como datos unos 2817 ns; "
            "en Linux 259, 450 y 1490 ns. El motor cuesta 5 a 8 veces más y a cambio las reglas se pueden listar, probar y cambiar sin editar código.")
    f.text(20, 28, "Nanosegundos por decisión (mediana)", 14, "start", 700)
    f.hbars([("Win · cadena if", 363, "teal", "363 ns"), ("Win · tabla", 585, "plain", "585 ns"), ("Win · motor de reglas", 2817, "coral", "2817 ns"),
             ("Linux · cadena if", 259, "teal", "259 ns"), ("Linux · tabla", 450, "plain", "450 ns"), ("Linux · motor de reglas", 1490, "coral", "1490 ns")],
            20, 44, 0.12, label_w=220, step=44)
    return f


# ---------------------------------------------------------------- SE-078
def se078_orden() -> Fig:
    f = Fig(940, 380, "El orden de las metas no cambia la respuesta pero sí el trabajo",
            "Con 300 hechos padre(pN, pN+1) y tres metas encadenadas, el orden que empieza por la meta con la constante final llega a la misma respuesta p297 con 903 inferencias, "
            "mientras el orden que empieza sin restricciones necesita 180600, unas 200 veces más.")
    f.text(20, 28, "Comparaciones de unificación hasta obtener todas las soluciones", 14, "start", 700)
    f.hbars([("Metas con la constante primero", 903, "teal", "903"), ("Metas sin restricción primero", 180600, "coral", "180 600")], 20, 50, 0.0030, label_w=250, step=56)
    f.box(20, 180, 900, 70, "Respuesta idéntica en ambos órdenes: [p297]. La lógica fija el significado; el orden de búsqueda decide el costo.", "grey", 13)
    f.box(20, 266, 900, 70, "En Prolog el motor intenta las metas de izquierda a derecha y las cláusulas de arriba abajo, así que escribir mal el orden no cambia lo verdadero, pero puede hacer inviable consultarlo.", "gold", 13)
    return f


def se078_unificacion() -> Fig:
    rows = [
        [("f(A, 2)  =  f(1, B)", "plain"), ("Éxito: A = 1 y B = 2", "teal"), ("Las variables se ligan en ambos sentidos: no hay entrada y salida fijas", "plain")],
        [("f(1)  =  f(2)", "plain"), ("Fallo (None)", "coral"), ("Dos constantes distintas no unifican; la búsqueda retrocede", "plain")],
        [("X  =  f(X)", "plain"), ("Aceptado sin comprobación de ocurrencia", "gold"), ("Crea una estructura infinita; Prolog estándar lo permite salvo con unify_with_occurs_check", "plain")],
    ]
    return chain_rows(
        "Unificación: tres casos ejecutados con un unificador mínimo",
        "Diagrama de tres casos: f(a,2) con f(1,b) unifica con a=1 y b=2; f(1) con f(2) falla; y X con f(X) es aceptado porque el unificador mínimo no hace la comprobación de ocurrencia.",
        ["Términos", "Resultado ejecutado", "Lectura"], rows, [230, 290, 330], gap=26,
        note="El unificador de este experimento es una herramienta didáctica, no el motor de un Prolog real.",
        note_kind="coral", foot=OBS)


def se078_ciclo() -> Fig:
    f = Fig(940, 420, "Un ciclo en los hechos: recursión sin memoria y recorrido con visitados",
            "Un grafo a, b, c con aristas a hacia b, b hacia c y c hacia a. La definición recursiva ingenua del ancestro sobre una consulta sin solución recorre el ciclo hasta RecursionError; "
            "un recorrido con conjunto de visitados responde falso para el destino z y verdadero para c.")
    f.box(60, 60, 70, 46, "a", "teal", 15, bold=True); f.box(260, 60, 70, 46, "b", "teal", 15, bold=True); f.box(160, 200, 70, 46, "c", "teal", 15, bold=True)
    f.arrow([(130, 83), (260, 83)]); f.arrow([(295, 106), (210, 200)]); f.arrow([(160, 223), (95, 106)])
    f.text(560, 44, "Consulta ancestro(a, z) y ancestro(a, c)", 13, "middle", 700, "#5c6b73")
    f.box(400, 60, 220, 70, "Recursión directa sin memoria", "plain", 13, bold=True)
    f.box(680, 60, 240, 70, "ancestro(a, z): RecursionError (profundidad > 1000); ancestro(a, c): no medido", "coral", 12)
    f.arrow([(624, 95), (676, 95)])
    f.box(400, 160, 220, 70, "Recorrido con conjunto de visitados", "plain", 13, bold=True)
    f.box(680, 160, 240, 70, "ancestro(a, z): False; ancestro(a, c): True", "teal", 12)
    f.arrow([(624, 195), (676, 195)])
    f.box(20, 292, 900, 56, "El tabling de SWI-Prolog resuelve esto de forma declarativa memorizando subobjetivos; aquí se reproduce el efecto con un conjunto de visitados.", "gold", 13)
    f.box(20, 358, 900, 40, "Prolog no se ejecutó (no estaba instalado): el comportamiento del tabling se cita de la documentación.", "coral", 12)
    return f


FIGURES = {
    "se-073-alias-y-copia.svg": se073_alias,
    "se-073-retorno-temprano.svg": se073_retorno,
    "se-073-sorpresas-de-estado.svg": se073_sorpresas,
    "se-074-costo-de-llamar.svg": se074_llamar,
    "se-074-limite-de-recursion.svg": se074_recursion,
    "se-074-efectos-ocultos.svg": se074_efectos,
    "se-075-memoria-slots.svg": se075_slots,
    "se-075-herencia-y-encapsulacion.svg": se075_mro,
    "se-075-despacho-polimorfico.svg": se075_despacho,
    "se-076-formas-de-filtrar.svg": se076_comprension,
    "se-076-costo-de-copiar.svg": se076_copiar,
    "se-076-cierres-y-composicion.svg": se076_cierres,
    "se-077-plan-de-consulta.svg": se077_indice,
    "se-077-conflictos-de-reglas.svg": se077_conflictos,
    "se-077-tres-codificaciones.svg": se077_tabla,
    "se-078-orden-de-metas.svg": se078_orden,
    "se-078-unificacion.svg": se078_unificacion,
    "se-078-ciclo-y-visitados.svg": se078_ciclo,
}
