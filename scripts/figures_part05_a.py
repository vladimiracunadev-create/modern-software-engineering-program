"""Figures for SE-061 to SE-066 (Python 3.12 measured on Windows 11 and Ubuntu 24.04 under WSL2)."""
from __future__ import annotations

from figure_kit import Fig
from figure_tables import finish, note, table

W = 960


def _fig(h: int, title: str, desc: str) -> Fig:
    return Fig(W, h, title, desc)


# ---------------------------------------------------------------- SE-061
def se061_expresiones() -> Fig:
    f = _fig(520, "Expresiones cuyo resultado el tipo decide",
             "Tabla con siete expresiones de Python ejecutadas: 0.1+0.2 da 0.30000000000000004, bool('false') es True, 3/2 es 1.5 y 3//2 es 1, "
             "-7//2 es -4 y -7%2 es 1, '3'*2 es '33' y 2**53+1 convertido a float no se distingue de 2**53.")
    rows = [
        ["0.1 + 0.2 == 0.3", "False (0.30000000000000004)", "float binario aproxima decimales; comparar con tolerancia o usar enteros/Decimal"],
        ["bool('false')", "True", "cualquier cadena no vacía es verdadera; la conversión necesita un parser explícito"],
        ["3 / 2  y  3 // 2", "1.5  y  1", "/ siempre devuelve float; // trunca hacia menos infinito"],
        ["-7 // 2  y  -7 % 2", "-4  y  1", "el módulo toma el signo del divisor; otros lenguajes devuelven -3 y -1"],
        ["'3' * 2", "'33'", "el mismo operador repite una secuencia: la semántica depende del tipo del operando"],
        ["float(2**53 + 1) == float(2**53)", "True", "a partir de 2**53 un float no distingue enteros consecutivos; int sí (9007199254740993)"],
        ["round(2.5), round(3.5), round(2.675, 2)", "2, 4, 2.67", "redondeo al par y representación binaria: no es «medio hacia arriba»"],
    ]
    y = table(f, ["Expresión", "Resultado observado", "Qué enseña"], rows, 10, 14, [290, 250, 400], size=13)
    y = note(f, y + 4, "Mismo resultado en Python 3.12.9 (Windows) y 3.12.3 (Linux): la semántica la define el lenguaje, no el sistema operativo.", "gold")
    return finish(f, y)


def se061_identidad() -> Fig:
    f = _fig(500, "Nombres, objetos e identidad: lo que se midió",
             "Dos nombres a y b apuntan a la misma lista, por lo que añadir por b cambia a. Un entero pequeño ocupa 28 bytes, 2**100 ocupa 40 y 2**1000 ocupa 160. "
             "Un dataclass congelado impide asignar atributos y bool es subtipo de int.")
    f.text(20, 28, "Aliasing: dos nombres, un objeto", 14, "start", 700)
    f.box(20, 44, 90, 40, "a", "navy", 14, bold=True)
    f.box(20, 100, 90, 40, "b", "navy", 14, bold=True)
    f.box(300, 60, 300, 64, "objeto list  [1, 2]  →  [1, 2, 3]", "teal", 14, bold=True)
    f.arrow([(110, 64), (300, 84)])
    f.arrow([(110, 120), (300, 104)])
    f.box(640, 44, 300, 96, "b.append(3) cambió lo que ve a. Medido: a is b → True; a == [1, 2, 3].", "gold", 13)
    rows = [
        ["tamaño de 1  /  2**30", "28 B  /  32 B", "un int de Python es un objeto, no una palabra de máquina"],
        ["tamaño de 2**100  /  2**1000", "40 B  /  160 B", "el entero crece con su valor: precisión arbitraria"],
        ["isinstance(True, int)  y  True + True", "True  y  2", "bool es subtipo de int: el JSON true pasaría como 1 si no se comprueba type()"],
        ["probe.cost = 3  (dataclass congelado)", "FrozenInstanceError", "el laboratorio impide mutar un Probe ya validado"],
    ]
    y = table(f, ["Observación", "Valor medido", "Consecuencia"], rows, 10, 170, [300, 190, 450], size=13)
    y = note(f, y + 2, "Identidad de enteros pequeños (256 sí, 257 no) es un detalle de CPython: no se usa nunca para comparar valores.", "coral")
    return finish(f, y)


def se061_frontera() -> Fig:
    f = _fig(520, "El presupuesto del laboratorio ante seis valores externos",
             "Tabla del parser del laboratorio: el presupuesto 5 se acepta; True, 5.0, '5', -1 y null se rechazan con invalid_budget. "
             "Además int(' 42 ') vale 42, int('4_2') vale 42, int('٣') vale 3 y int('²') falla.")
    rows = [
        ["5", "int válido", "aceptado"],
        ["true", "bool, subtipo de int en Python", "invalid_budget (type(value) is int)"],
        ["5.0", "float con valor entero", "invalid_budget: no se redondea en silencio"],
        ["\"5\"", "texto numérico", "invalid_budget: no se convierte en la frontera JSON"],
        ["-1", "int fuera de dominio", "invalid_budget (budget < 0)"],
        ["null", "ausencia", "invalid_budget: ausencia no es cero"],
    ]
    y = table(f, ["budget en el JSON", "Tipo / situación", "Resultado del parser"], rows, 10, 14, [200, 330, 410], size=13,
              kinds=["teal", "plain", "plain"])
    y = note(f, y + 4, "int() es más permisivo que el contrato: int(' 42 ') = 42, int('4_2') = 42, int('٣') = 3 (dígito arábigo-índico); int('²') falla aunque '²'.isdigit() sea True. "
             "Por eso el contrato fija qué formatos acepta en lugar de heredar los de int().", "gold")
    y = note(f, y, "Medido con el parser real de labs/part-05-diagnostic-cli en ambas plataformas. Otros lenguajes tendrán otra jerarquía bool/int.", "grey", 12)
    return finish(f, y)


# ---------------------------------------------------------------- SE-062
def se062_verdad() -> Fig:
    f = _fig(500, "Qué valores son falsos en Python (trece medidos)",
             "Tabla de truthiness: 0, 0.0, cadena vacía, lista vacía, diccionario vacío, None, tupla vacía y set vacío son falsos; "
             "espacio, [0], 'false', '0' y nan son verdaderos.")
    rows = [
        ["0   0.0   ''   []   {}   ()   set()   None", "False", "vacío o cero: la ausencia de contenido"],
        ["' '   [0]   'false'   '0'   float('nan')", "True", "no vacío: el contenido no se interpreta, solo se cuenta"],
    ]
    y = table(f, ["Valores", "bool(valor)", "Lectura"], rows, 10, 14, [420, 130, 390], size=14, kinds=["plain", "plain", "plain"])
    y = note(f, y + 6, "if budget: trata 0, None y [] igual. Si 0 es un presupuesto válido y None significa «no informado», la condición necesita comparar explícitamente: "
             "if budget is None / if budget == 0.", "coral")
    y = note(f, y, "Operadores lógicos devuelven operandos, no booleanos: None or 5 → 5; 0 or '' → ''; [] and 3 → []; 1 and 2 → 2. Útil para valores por defecto, peligroso si el operando puede ser 0.", "gold")
    y = note(f, y, "Resultados idénticos en Windows y Linux (Python 3.12). Otros lenguajes tienen otra tabla: en JavaScript [] es verdadero.", "grey", 12)
    return finish(f, y)


def se062_cortocircuito() -> Fig:
    f = _fig(470, "Cortocircuito y comparaciones encadenadas: qué se evalúa",
             "Se registraron las llamadas a una función con efecto: f(0) and f(1) evalúa solo f(0); f(1) or f(2) evalúa solo f(1); "
             "5 < 3 < f(9) no llama a f. Además 3 > 2 > 2 es False y 0 == False es True.")
    rows = [
        ["f(0) and f(1)", "solo f(0)", "0 es falso: el resultado ya está decidido"],
        ["f(1) or f(2)", "solo f(1)", "1 es verdadero: la segunda operando no se evalúa"],
        ["5 < 3 < f(9)", "f no se llama", "equivale a (5 < 3) and (3 < f(9)): la primera falla"],
        ["3 > 2 > 2", "False", "se evalúa como (3 > 2) and (2 > 2), no como (3 > 2) > 2"],
        ["0 == False   y   '' == None", "True   y   False", "== iguala 0 y False; None solo es igual a None"],
    ]
    y = table(f, ["Expresión", "Efecto observado", "Por qué"], rows, 10, 14, [290, 210, 440], size=13)
    y = note(f, y + 4, "Una guarda como if x is not None and x.ok depende del cortocircuito para no fallar. Invertir el orden convierte una condición segura en AttributeError.", "gold")
    return finish(f, y)


def se062_cadena_tabla() -> Fig:
    f = _fig(520, "Cadena de if y tabla de umbrales: mismo resultado, distinto costo",
             "Una clasificación de latencia en cuatro tramos se implementó con if/elif y con bisect sobre una tabla; coincidieron en 1000 muestras con frontera. "
             "Costo por llamada en Windows: cadena con 1500 ms 104.7 ns, con 50 ms 74.0 ns, tabla 126.4 ns; en Linux 65.3, 49.4 y 98.2 ns.")
    f.text(20, 28, "Windows (ns por llamada, mejor de 5 repeticiones)", 14, "start", 700)
    f.hbars([("if/elif, valor 50", 74.0, "teal", "74.0"), ("if/elif, valor 1500", 104.7, "teal", "104.7"), ("tabla + bisect, 1500", 126.4, "gold", "126.4")],
            20, 40, 4.2, label_w=250, step=42)
    f.text(20, 178, "Linux / WSL2 (ns por llamada)", 14, "start", 700)
    f.hbars([("if/elif, valor 50", 49.4, "teal", "49.4"), ("if/elif, valor 1500", 65.3, "teal", "65.3"), ("tabla + bisect, 1500", 98.2, "gold", "98.2")],
            20, 190, 4.2, label_w=250, step=42)
    y = note(f, 318, "Con 4 tramos la cadena es más rápida y más legible. La diferencia es de decenas de nanosegundos: irrelevante frente a una llamada de red. "
             "La tabla vale cuando los tramos son muchos o vienen de configuración, y cada frontera se prueba (100 → fast, 101 → ok).", "gold")
    y = note(f, y, "Los números dependen del equipo y de la carga; úsalos para comparar órdenes de magnitud, no como constantes. Cambiar <= por < en la frontera 100 cambia la clase de 100 de fast a ok: solo una prueba de frontera lo detecta.", "coral", 12)
    return finish(f, y)


# ---------------------------------------------------------------- SE-063
def se063_recursion() -> Fig:
    f = _fig(520, "Suma de 1 a 900 con recursión y con bucle, y el límite de pila",
             "Sumar 1..900 recursivamente tarda 148.8 microsegundos en Windows y 164.0 en Linux; con un bucle 39.4 y 36.3. "
             "El límite de recursión es 1000 y la profundidad alcanzada fue 998; sum_rec(5000) lanza RecursionError.")
    f.text(20, 28, "Microsegundos por llamada (n = 900)", 14, "start", 700)
    f.hbars([("recursión · Windows", 148.8, "coral", "148.8"), ("bucle · Windows", 39.4, "teal", "39.4"),
             ("recursión · Linux", 164.0, "coral", "164.0"), ("bucle · Linux", 36.3, "teal", "36.3")], 20, 42, 3.4, label_w=210, step=44)
    rows = [["sys.getrecursionlimit()", "1000", "profundidad máxima alcanzada: 998 (quedan marcos de intérprete)"],
            ["sum_rec(5000)", "RecursionError", "maximum recursion depth exceeded: el fallo es controlable, no un cierre del proceso"]]
    y = table(f, ["Medida", "Valor", "Lectura"], rows, 10, 232, [260, 170, 510], size=13)
    y = note(f, y + 2, "Recorrer una estructura profunda de datos externos con recursión convierte el tamaño de la entrada en un riesgo. El laboratorio itera y acota el número de pasos.", "gold")
    return finish(f, y)


def se063_mutar() -> Fig:
    f = _fig(470, "Modificar una colección mientras se recorre",
             "Quitar los pares de [1..6] mientras se itera parece funcionar, pero con [2, 4, 6, 8] deja [4, 8]. "
             "Añadir una clave a un diccionario durante el recorrido lanza RuntimeError. Filtrar con una comprensión da el resultado correcto.")
    rows = [
        ["quitar pares de [1, 2, 3, 4, 5, 6] iterando", "[1, 3, 5]", "correcto por casualidad: los elementos saltados eran impares"],
        ["quitar pares de [2, 4, 6, 8] iterando", "[4, 8]", "al borrar el índice 0 el iterador salta el siguiente: 4 y 8 sobreviven"],
        ["d['c'] = 3 dentro de for k in d", "RuntimeError", "dictionary changed size during iteration: el lenguaje avisa"],
        ["[v for v in xs if v % 2]", "nueva lista correcta", "construir un resultado nuevo evita el estado compartido"],
    ]
    y = table(f, ["Operación", "Resultado medido", "Por qué"], rows, 10, 14, [330, 180, 430], size=13, kinds=["plain", "coral", "plain"])
    y = note(f, y + 4, "Una prueba con una sola entrada que «pasa» no demuestra que el bucle sea correcto: [1..6] lo ocultaba. El invariante del bucle («los elementos vistos ya están decididos») es lo que se comprueba.", "gold")
    return finish(f, y)


def se063_memoria() -> Fig:
    f = _fig(520, "Iterar sin materializar: memoria medida y trampas de los iteradores",
             "range(10**9) ocupa 48 bytes, una lista de 10**5 enteros 800056 bytes y una expresión generadora 192 bytes. "
             "Los cierres de un bucle devuelven [2, 2, 2] por enlace tardío y un iterador agotado devuelve una lista vacía.")
    f.text(20, 28, "sys.getsizeof (bytes, escala logarítmica por tramos)", 14, "start", 700)
    f.hbars([("range(10**9)", 48, "teal", "48 B"), ("generador sobre range(10**9)", 192, "teal", "192 B")], 20, 42, 1.2, label_w=270, step=44)
    f.hbars([("list(range(10**5)) · 800 056 B", 600, "coral", "≈ 800 KB")], 20, 130, 0.8, label_w=270, step=44)
    rows = [
        ["[lambda: i for i in range(3)]", "[2, 2, 2]", "el cierre captura el nombre i, no su valor en cada vuelta"],
        ["it = iter([1,2,3]); list(it); list(it)", "[]", "un iterador se consume una vez; repetirlo exige recrearlo"],
        ["while v != 1.0: v += 0.1", "no termina por igualdad", "v llega a 2.0000000000000004; el contador de seguridad cortó a 20 vueltas"],
    ]
    y = table(f, ["Fragmento", "Resultado medido", "Lectura"], rows, 10, 190, [330, 170, 440], size=13)
    y = note(f, y + 2, "La barra de 800 KB está truncada en la escala: la lista es unas 4 000 veces mayor que el generador (y 16 000 que el range). Pero el generador no permite volver atrás ni conocer su longitud.", "grey", 12)
    return finish(f, y)


# ---------------------------------------------------------------- SE-064
def se064_defecto() -> Fig:
    f = _fig(480, "El argumento por defecto mutable se crea una sola vez",
             "Con def bad(item, acc=[]) tres llamadas devuelven [1, 2, 3] porque comparten la misma lista; con acc=None y una lista nueva dentro, cada llamada devuelve su propia lista. "
             "La lista vive en bad.__defaults__.")
    f.box(20, 20, 420, 80, "def bad(item, acc=[]):\n    acc.append(item); return acc", "coral", 13)
    f.box(520, 20, 420, 80, "def good(item, acc=None):\n    acc = [] if acc is None else acc\n    acc.append(item); return acc", "teal", 13)
    rows = [["bad(1), bad(2)", "[1, 2, 3] (la misma lista; tras la tercera llamada)", "bad.__defaults__[0] is lista devuelta → True"],
            ["good(1), good(2)", "[1] y [2]", "cada llamada crea su lista"]]
    y = table(f, ["Llamadas", "Resultado medido", "Evidencia"], rows, 10, 118, [180, 430, 330], size=13)
    y = note(f, y + 4, "Python evalúa los valores por defecto al definir la función, no en cada llamada. Un valor mutable por defecto es estado global oculto.", "gold")
    y = note(f, y, "Firma observada con inspect: (a, b=2, /, c=3, *, d). Pasar cuatro posicionales produce TypeError: «takes from 1 to 3 positional arguments but 4 were given».", "grey", 12)
    return finish(f, y)


def se064_alcance() -> Fig:
    f = _fig(500, "Alcance, cierres y paso de argumentos: cuatro comportamientos medidos",
             "Un contador global vale 2 tras dos llamadas; un cierre con nonlocal devuelve 1 y luego 2; leer zz antes de asignarlo en la función lanza UnboundLocalError; "
             "pasar una lista y reasignar el parámetro no cambia la lista, mientras que mutarla sí: queda [1, 9].")
    rows = [
        ["global cnt; cnt += 1  (dos veces)", "2", "global declara que el nombre vive en el módulo"],
        ["nonlocal n; n += 1 en un cierre", "1, luego 2", "el estado vive en la celda del cierre: closure[0].cell_contents = 2"],
        ["print(zz); zz = 1 dentro de f", "UnboundLocalError", "asignar en la función hace local el nombre en todo el cuerpo"],
        ["mut(L) → L.append(9);  rebind(L) → L = [0]", "L queda [1, 9]", "se pasa una referencia al objeto: mutar afecta, reasignar no"],
    ]
    y = table(f, ["Fragmento", "Resultado medido", "Regla"], rows, 10, 14, [330, 170, 440], size=13)
    y = note(f, y + 4, "Resolución de nombres: local → envolvente → global → incorporado (LEGB). Una función que depende de un global es difícil de probar: sus pruebas tienen que preparar y limpiar ese estado.", "gold")
    return finish(f, y)


def se064_costo() -> Fig:
    f = _fig(540, "Costo de llamar funciones y de memoizar",
             "Llamar una función vacía cuesta 41.7 ns en Windows y 29.7 en Linux; con tres argumentos posicionales 54.2 y 35.5; con tres por nombre 73.1 y 61.8. "
             "fib(25) sin caché tarda 22.6 ms en Windows y 14.1 en Linux; con lru_cache, 0.123 y 0.084 microsegundos.")
    f.text(20, 28, "Nanosegundos por llamada", 14, "start", 700)
    f.hbars([("vacía · Windows", 41.7, "teal", "41.7"), ("3 posicionales · Windows", 54.2, "teal", "54.2"), ("3 por nombre · Windows", 73.1, "gold", "73.1"),
             ("vacía · Linux", 29.7, "teal", "29.7"), ("3 posicionales · Linux", 35.5, "teal", "35.5"), ("3 por nombre · Linux", 61.8, "gold", "61.8")],
            20, 42, 6, label_w=250, step=38)
    rows = [["fib(25) sin caché", "22.6 ms", "14.1 ms", "≈ 242 785 llamadas recursivas"],
            ["fib(25) con lru_cache (ya calentada)", "0.123 µs", "0.084 µs", "una búsqueda en diccionario"]]
    y = table(f, ["Caso", "Windows", "Linux", "Nota"], rows, 10, 280, [330, 130, 130, 350], size=13)
    y = note(f, y + 2, "Memoizar solo es correcto si la función es pura: mismos argumentos, mismo resultado, sin efectos. Con una función que lee el reloj o un archivo, la caché devuelve datos viejos.", "coral")
    y = note(f, y, "Las diferencias entre posicional y por nombre son decenas de nanosegundos: elige por claridad (los parámetros por nombre documentan unidades) y mide solo si un perfilador lo señala.", "grey", 12)
    return finish(f, y)


# ---------------------------------------------------------------- SE-065
def se065_jerarquia() -> Fig:
    f = _fig(500, "Jerarquía de excepciones: qué captura cada except",
             "KeyError desciende de LookupError, Exception y BaseException; FileNotFoundError de OSError; KeyboardInterrupt desciende directamente de BaseException. "
             "except Exception no captura KeyboardInterrupt ni SystemExit.")
    f.box(20, 20, 200, 44, "BaseException", "navy", 14, bold=True)
    f.box(40, 100, 180, 44, "Exception", "teal", 14, bold=True)
    f.box(300, 20, 200, 44, "KeyboardInterrupt", "coral", 13, bold=True)
    f.box(520, 20, 140, 44, "SystemExit", "coral", 13, bold=True)
    f.box(40, 180, 170, 44, "LookupError", "plain", 13, bold=True)
    f.box(40, 250, 170, 44, "KeyError", "plain", 13, bold=True)
    f.box(260, 180, 150, 44, "OSError", "plain", 13, bold=True)
    f.box(260, 250, 200, 44, "FileNotFoundError", "plain", 13, bold=True)
    f.arrow([(120, 100), (120, 64)])
    f.arrow([(220, 42), (300, 42)])
    f.arrow([(125, 180), (125, 144)]); f.arrow([(125, 250), (125, 224)])
    f.arrow([(335, 180), (215, 128)]); f.arrow([(360, 250), (350, 224)])
    f.box(560, 110, 380, 150, "Medido: issubclass(KeyboardInterrupt, Exception) → False; issubclass(SystemExit, Exception) → False. "
          "Un except Exception: deja pasar Ctrl+C y sys.exit(); un except: sin tipo o except BaseException: los traga.", "gold", 13)
    y = note(f, 320, "Capturar la clase concreta (KeyError, FileNotFoundError) documenta qué fallo se espera y deja pasar los demás. El laboratorio captura solo (FileNotFoundError, OSError, UnicodeDecodeError) alrededor de la lectura.", "grey")
    return finish(f, y)


def se065_costo() -> Fig:
    f = _fig(520, "Costo de lanzar una excepción frente a preguntar antes",
             "Lanzar y capturar una excepción cuesta 192.1 ns en Windows y 183.7 en Linux; leer una clave ausente con try/except KeyError 196.1 y 174.6 ns; "
             "d.get 32.8 y 35.0 ns; la pregunta 'k' in d 23.3 y 20.8 ns. Un try sin lanzar no se distingue del ruido.")
    f.text(20, 28, "Nanosegundos por operación (clave ausente en un diccionario vacío)", 14, "start", 700)
    f.hbars([("try/except KeyError · Win", 196.1, "coral", "196.1"), ("try/except KeyError · Linux", 174.6, "coral", "174.6"),
             ("d.get(k) · Windows", 32.8, "teal", "32.8"), ("d.get(k) · Linux", 35.0, "teal", "35.0"),
             ("k in d · Windows", 23.3, "teal", "23.3"), ("k in d · Linux", 20.8, "teal", "20.8")], 20, 42, 2.3, label_w=280, step=38)
    y = note(f, 280, "Un try que no lanza costó 15.5 ns frente a 36.8 ns de la línea de control en Windows y 9.1 frente a 8.5 en Linux: la diferencia cambia de signo, es ruido. "
             "No se puede afirmar que try «sea gratis» ni «cueste»: a esta escala el reloj y la carga dominan.", "gold")
    y = note(f, y, "Conclusión útil: una excepción cuesta de seis a ocho veces más que preguntar, pero en nanosegundos. Elige por claridad y por si el fallo es excepcional o esperado. "
             "Si el caso «ausente» es normal, un resultado explícito expresa mejor la intención.", "grey", 12)
    return finish(f, y)


def se065_orden() -> Fig:
    f = _fig(520, "Orden de ejecución, encadenamiento y lo que anula un finally",
             "En try/except con raise y finally el orden observado fue try, except, finally y luego el llamador. return dentro de finally reemplaza el valor devuelto. "
             "raise ... from conserva la causa; una excepción lanzada dentro de un except conserva el contexto implícito. assert desaparece con python -O.")
    rows = [
        ["try → except → raise → finally → llamador", "orden medido: try, except, finally, caller", "finally corre aunque la excepción siga viajando"],
        ["try: return 'try'  finally: return 'finally'", "'finally'", "return en finally anula el valor y silencia excepciones: no lo uses"],
        ["raise RuntimeError(...) from e", "__cause__ = ValueError, contexto suprimido", "se conserva la causa original para el diagnóstico"],
        ["1/0 dentro de un except ValueError", "__context__ = ValueError, __cause__ = None", "Python encadena automáticamente lo que ocurrió mientras se manejaba otro error"],
        ["python -O con assert False", "el assert no se ejecuta", "assert verifica supuestos de programador; nunca valida datos externos"],
        ["except* ValueError / except* KeyError", "cada grupo recibe su subconjunto", "ExceptionGroup agrupa varios fallos simultáneos (Python 3.11 o posterior)"],
    ]
    y = table(f, ["Fragmento", "Resultado observado", "Lectura"], rows, 10, 14, [320, 290, 330], size=13)
    return finish(f, y)


# ---------------------------------------------------------------- SE-066
def se066_pertenencia() -> Fig:
    f = _fig(500, "Buscar un elemento: lista frente a conjunto y diccionario",
             "Preguntar si el último elemento está en una lista cuesta 8.41 microsegundos con 1000 elementos, 94.28 con 10000 y 997.55 con 100000 en Windows; "
             "en un conjunto o diccionario de 100000 elementos cuesta 77.1 y 78.5 nanosegundos. En Linux la lista de 100000 cuesta 1221.18 µs y el conjunto 69.0 ns.")
    f.text(20, 28, "Microsegundos por consulta en lista (Windows)", 14, "start", 700)
    f.hbars([("lista, n = 1 000", 8.41, "teal", "8.41 µs"), ("lista, n = 10 000", 94.28, "gold", "94.28 µs"), ("lista, n = 100 000", 997.55, "coral", "997.55 µs")],
            20, 42, 0.5, label_w=210, step=42)
    rows = [["conjunto, n = 100 000", "77.1 ns", "69.0 ns"], ["diccionario, n = 100 000", "78.5 ns", "67.7 ns"],
            ["lista, n = 100 000", "997 550 ns", "1 221 180 ns"]]
    y = table(f, ["Estructura (último elemento)", "Windows", "Linux"], rows, 10, 180, [380, 200, 200], size=13)
    y = note(f, y + 2, "La lista crece linealmente (10× elementos ≈ 10× tiempo); el conjunto es casi constante porque busca por hash. Usarlo exige que los elementos sean hashables y paga memoria (siguiente figura).", "gold")
    y = note(f, y, "Es el peor caso de la lista (elemento al final). Para n pequeño la lista gana en simplicidad; mide con tus datos antes de optimizar.", "grey", 12)
    return finish(f, y)


def se066_memoria() -> Fig:
    f = _fig(500, "Memoria de las colecciones: vacías y con 100 enteros",
             "Con 100 enteros una lista ocupa 856 bytes, una tupla 840, un conjunto 8408 y un diccionario 4688; vacíos ocupan 56, 40, 216 y 64. "
             "sys.getsizeof no incluye los objetos contenidos.")
    f.text(20, 28, "Bytes con 100 elementos (sys.getsizeof)", 14, "start", 700)
    f.hbars([("lista", 856, "teal", "856 B"), ("tupla", 840, "teal", "840 B"), ("diccionario", 4688, "gold", "4 688 B"), ("conjunto", 8408, "coral", "8 408 B")],
            20, 42, 0.08, label_w=140, step=40)
    rows = [["lista · tupla · conjunto · diccionario", "56 · 40 · 216 · 64 B", "estructura vacía"]]
    y = table(f, ["Vacías", "Bytes", "Nota"], rows, 10, 214, [330, 230, 380], size=13)
    y = note(f, y + 2, "El conjunto compra consulta casi constante con unas diez veces la memoria de una lista. Para un registro de tres campos, una tupla o un dataclass son más compactos que un diccionario.", "gold")
    y = note(f, y, "getsizeof mide el contenedor, no los 100 enteros que referencia. Los tamaños son de CPython 3.12 de 64 bits; otra versión o implementación da otros números.", "grey", 12)
    return finish(f, y)


def se066_trampas() -> Fig:
    f = _fig(540, "Seis trampas de las colecciones, todas medidas",
             "[[0]*2]*2 comparte la fila y tras escribir da [[9, 0], [9, 0]]; la copia superficial de un diccionario comparte las listas internas; "
             "1, 1.0 y True son la misma clave; nan crea dos claves; una lista no es hashable ni dentro de una tupla; sorted es estable.")
    rows = [
        ["a = [[0]*2]*2; a[0][0] = 9", "[[9, 0], [9, 0]]", "dos filas son el mismo objeto; con comprensión: [[9, 0], [0, 0]]"],
        ["dict(orig) y luego orig['k'].append(2)", "la copia también cambia", "copia superficial; copy.deepcopy conserva el original"],
        ["{1: 'a', 1.0: 'b', True: 'c'}", "{1: 'c'}", "1 == 1.0 == True y hash igual: una sola clave"],
        ["{float('nan'): 1, float('nan'): 2}", "2 claves", "nan != nan: dos claves no iguales"],
        ["{[1]: 1}  y  hash((1, [2]))", "TypeError: unhashable type: 'list'", "solo lo inmutable (en profundidad) es hashable"],
        ["sorted(recs, key=segundo)", "[('c',1),('b',2),('a',2)]", "ordenamiento estable: b y a conservan su orden relativo"],
    ]
    y = table(f, ["Fragmento", "Resultado medido", "Causa"], rows, 10, 14, [310, 240, 390], size=13)
    y = note(f, y + 4, "Además sorted(['b', 'B', 'a']) = ['B', 'a', 'b']: el orden es por punto de código, no alfabético. Una comparación «natural» exige una clave explícita.", "gold")
    return finish(f, y)


FIGURES = {
    "se-061-expresiones-y-tipos.svg": se061_expresiones,
    "se-061-nombres-e-identidad.svg": se061_identidad,
    "se-061-frontera-del-presupuesto.svg": se061_frontera,
    "se-062-valores-verdaderos-y-falsos.svg": se062_verdad,
    "se-062-cortocircuito-y-cadenas.svg": se062_cortocircuito,
    "se-062-cadena-o-tabla.svg": se062_cadena_tabla,
    "se-063-recursion-contra-bucle.svg": se063_recursion,
    "se-063-mutar-mientras-se-recorre.svg": se063_mutar,
    "se-063-memoria-de-iteradores.svg": se063_memoria,
    "se-064-argumento-por-defecto.svg": se064_defecto,
    "se-064-alcance-y-cierres.svg": se064_alcance,
    "se-064-costo-de-llamar.svg": se064_costo,
    "se-065-jerarquia-de-excepciones.svg": se065_jerarquia,
    "se-065-costo-de-excepciones.svg": se065_costo,
    "se-065-orden-y-encadenamiento.svg": se065_orden,
    "se-066-costo-de-pertenencia.svg": se066_pertenencia,
    "se-066-memoria-de-colecciones.svg": se066_memoria,
    "se-066-trampas-de-colecciones.svg": se066_trampas,
}
