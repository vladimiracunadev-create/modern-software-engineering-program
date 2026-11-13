"""Figures for SE-079 to SE-084 (CPython 3.12.9 on Windows 11 and 3.12.3 on Ubuntu 24.04 under WSL2)."""
from __future__ import annotations

from figure_kit import Fig

OBS = "Medido con CPython 3.12 en un equipo concreto; las magnitudes cambian con la máquina, el orden relativo es lo que importa."


def _note(f: Fig, y: float, text: str = OBS) -> None:
    f.text(f.width / 2, y, text, 12, "middle", 400, "#5c1f14")


# ---------------------------------------------------------------- SE-079
def se079_orden() -> Fig:
    f = Fig(960, 340, "Orden en que el bucle de eventos de asyncio atiende lo que se programó",
            "Secuencia observada: primero el código síncrono que sigue a la programación, luego las dos devoluciones de llamada call_soon en el orden en que se registraron, "
            "después la tarea creada con create_task y por último la devolución de call_later con retardo cero.")
    f.text(20, 28, "Registro en el código: call_soon(1), call_later(0), call_soon(2), create_task, y una línea síncrona", 13, "start", 700)
    steps = [("1", "línea síncrona\nposterior a programar", "gold"), ("2", "call_soon(1)", "teal"), ("3", "call_soon(2)", "teal"), ("4", "tarea\n(create_task)", "teal"), ("5", "call_later(0)", "coral")]
    x = 20
    for n, label, kind in steps:
        f.box(x, 90, 170, 78, label, kind, 13, bold=True)
        f.dot(x + 85, 78, n)
        if n != "5":
            f.arrow([(x + 170, 129), (x + 186, 129)])
        x += 186
    f.box(20, 190, 920, 62, "call_later(0) se registró en segundo lugar pero corre al final: los temporizadores pasan por un montículo y se mueven a la cola de listos solo en la iteración siguiente.", "gold", 13)
    f.box(20, 266, 920, 48, "El orden es el observado en CPython 3.12; la documentación solo promete que call_soon respeta el orden de registro entre sí.", "coral", 13)
    return f


def se079_bloqueo() -> Fig:
    f = Fig(940, 340, "Un manejador bloqueante detiene todos los eventos del mismo bucle",
            "Barras: un temporizador configurado para 10 ms tiene un intervalo mediano de 11,9 ms en Windows y 10,2 ms en Linux, pero cuando otro manejador bloquea 300 ms el intervalo máximo observado es de 300,6 ms en Windows y 310,5 ms en Linux.")
    f.text(20, 28, "Milisegundos entre ticks consecutivos (objetivo: 10 ms)", 14, "start", 700)
    f.hbars([("Win · mediana", 11.9, "teal", "11,9 ms"), ("Win · máximo", 300.6, "coral", "300,6 ms"),
             ("Linux · mediana", 10.2, "teal", "10,2 ms"), ("Linux · máximo", 310.5, "coral", "310,5 ms")], 20, 44, 2.2, label_w=170, step=46)
    f.box(20, 238, 900, 74, "El bucle de eventos es un solo hilo que alterna entre manejadores. Un time.sleep(0.3) dentro de un manejador no cede el control: durante 300 ms no hubo ningún otro evento atendido.", "gold", 13)
    return f


def se079_fallos() -> Fig:
    f = Fig(960, 400, "Cuatro fallos típicos de un bus de eventos ejecutados",
            "Tabla: si el segundo de tres manejadores lanza una excepción el tercero nunca corre; un manejador que emite el mismo evento llega a profundidad 5; "
            "sin identificador de evento una entrega duplicada suma 13 en vez de 8; y una excepción dentro de una tarea no esperada queda guardada en la tarea sin interrumpir al resto.")
    heads = ["Experimento", "Resultado ejecutado", "Lectura"]
    rows = [
        ["Tres manejadores; el segundo lanza RuntimeError", "El registro quedó [h1]; h3 nunca corrió", "Un despachador síncrono ligado a sus manejadores propaga el fallo al emisor"],
        ["Un manejador de «y» vuelve a emitir «y»", "Profundidad máxima de 5", "Sin límite ni cola, la reentrada es recursión disfrazada"],
        ["Eventos e1 (5), e1 (5), e2 (3) entregados dos veces el primero", "Suma 13 sin id; 8 con id de evento", "Con entrega «al menos una vez» el consumidor debe ser idempotente"],
        ["Tarea creada con create_task que lanza ValueError y nadie la espera", "La tarea terminó con la excepción guardada", "Si nadie la consulta, el error aparece tarde o nunca como un aviso"],
    ]
    f.table(heads, rows, 10, 12, [320, 280, 340], row_h=78, size=12)
    return f


# ---------------------------------------------------------------- SE-080
def se080_memoria() -> Fig:
    f = Fig(940, 360, "Un flujo perezoso evita materializar los elementos",
            "Barras: producir un millón de elementos en una lista alcanza un pico de 39 496 KiB, mientras que consumirlos con un generador tiene un pico cercano a cero. "
            "Pedir cinco números pares de un generador de un millón solo produjo nueve elementos.")
    f.text(20, 28, "Pico de memoria al sumar 1 000 000 de elementos (tracemalloc)", 14, "start", 700)
    f.hbars([("Lista completa", 39496, "coral", "39 496 KiB"), ("Generador", 1, "teal", "≈ 0 KiB")], 20, 46, 0.0135, label_w=170, step=52)
    f.box(20, 170, 900, 70, "Pidiendo los primeros 5 pares de un origen de 1 000 000: elementos producidos = 9. El flujo hace trabajo solo bajo demanda; el productor no se adelanta.", "gold", 13)
    f.box(20, 254, 900, 62, "Un generador se agota: la segunda lectura de [0, 1, 2] devolvió [] vacía. Un flujo «frío» se vuelve a ejecutar al suscribirse otra vez y repite su efecto.", "coral", 13)
    _note(f, 346)
    return f


def se080_contrapresion() -> Fig:
    f = Fig(940, 350, "Contrapresión: una cola acotada limita lo que espera, una ilimitada no",
            "Barras del tamaño máximo observado de la cola cuando un productor envía 500 elementos a un consumidor lento: con cola ilimitada llegó a 500 y con cola de capacidad 10 nunca pasó de 10; "
            "el tiempo total fue casi igual, 0,77 y 0,79 s en Windows.")
    f.text(20, 28, "Elementos en espera como máximo (productor rápido, consumidor de 1 ms por elemento)", 14, "start", 700)
    f.hbars([("Cola ilimitada", 500, "coral", "500"), ("Cola con maxsize = 10", 10, "teal", "10")], 20, 46, 1.2, label_w=220, step=52)
    f.box(20, 170, 900, 74, "Tiempo total: 0,77 s con cola ilimitada y 0,79 s con capacidad 10 (Windows); 0,57 s y 0,58 s en Linux. El límite no hizo más lento el sistema: solo hizo esperar al productor.", "gold", 13)
    f.box(20, 258, 900, 60, "Con tasas reales distintas la cola ilimitada crece sin tope hasta agotar la memoria. Aquí el consumidor terminó, pero la cola ilimitada no avisó de nada.", "coral", 13)
    return f


def se080_semantica() -> Fig:
    f = Fig(960, 430, "Semántica de flujos observada: agotamiento, error final y debounce",
            "Tabla: un generador agotado devuelve vacío, un error termina el flujo después de entregar 1 y 2 sin llegar a 3, "
            "y un debounce de 100 ms sobre eventos en 0, 10, 20, 400, 410 y 900 ms emite solo los de 20, 410 y 900.")
    heads = ["Experimento", "Resultado ejecutado", "Contrato que implica"]
    rows = [
        ["list(g) dos veces sobre el mismo generador", "[0, 1, 2] y luego []", "Un flujo caliente o un generador no se rebobinan"],
        ["Flujo que entrega 1 y 2 y lanza ValueError antes de 3", "Se recibieron [1, 2]; error «fin con error»", "Error y finalización son terminales: no hay elementos después"],
        ["Debounce de 100 ms sobre 0, 10, 20, 400, 410, 900", "Emite 20, 410 y 900", "Un operador de tiempo cambia la cardinalidad de salida"],
        ["Suscribirse dos veces a un flujo frío con efecto", "El efecto se ejecutó dos veces", "Frío: cada suscripción empieza de nuevo; caliente: comparten"],
    ]
    f.table(heads, rows, 10, 12, [330, 300, 310], row_h=70, size=12)
    f.box(10, 372, 940, 40, "El contrato de ReactiveX fija que tras un error o una finalización no hay más notificaciones.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-081
def se081_carrera() -> Fig:
    f = Fig(960, 420, "Una condición de carrera que a veces no aparece",
            "Cuatro hilos incrementan un contador 200000 veces cada uno. Sin ceder el hilo el resultado fue 800000 en ambos sistemas; cediendo el hilo cada 50 iteraciones fue cerca de 200800, y cediendo en cada iteración 200064; con un cerrojo 800000.")
    f.text(20, 28, "Valor final del contador (esperado: 800 000)", 14, "start", 700)
    f.hbars([("Sin ceder el hilo", 800000, "plain", "800 000"), ("Ceder cada 50 iteraciones", 200800, "coral", "200 800"),
             ("Ceder en cada iteración", 200064, "coral", "200 064"), ("Con cerrojo (Lock)", 800000, "teal", "800 000")], 20, 44, 0.00055, label_w=240, step=46)
    f.box(20, 248, 900, 84, "La versión sin ceder el hilo «funcionó» en 3.12 porque el intérprete cambia de hilo cada 5 ms y el bucle es corto: la ausencia de fallo no era corrección. "
          "Cuando el cambio de hilo cayó entre la lectura y la escritura, se perdieron tres cuartas partes de las actualizaciones.", "gold", 13)
    f.box(20, 346, 900, 54, "Resultados iguales en Windows (3.12.9) y Linux (3.12.3). El costo del cerrojo no se midió de forma comparable y no se afirma.", "grey", 13)
    return f


def se081_cpu() -> Fig:
    f = Fig(940, 400, "Trabajo de CPU: un hilo, cuatro hilos y cuatro procesos",
            "Barras en segundos para cuatro tareas de CPU iguales: en Windows una tarea tarda 0,55 s, cuatro hilos 2,09 s y cuatro procesos 1,34 s; en Linux 0,35 s, 1,38 s y 0,50 s. "
            "Los hilos no aceleran el cálculo en CPython por el bloqueo global del intérprete.")
    f.text(20, 28, "Segundos totales (tarea de 2 millones de multiplicaciones; 8 CPU lógicas)", 14, "start", 700)
    f.hbars([("Win · una tarea", 0.55, "plain", "0,55 s"), ("Win · 4 hilos", 2.09, "coral", "2,09 s"), ("Win · 4 procesos", 1.34, "teal", "1,34 s"),
             ("Linux · una tarea", 0.35, "plain", "0,35 s"), ("Linux · 4 hilos", 1.38, "coral", "1,38 s"), ("Linux · 4 procesos", 0.50, "teal", "0,50 s")], 20, 44, 190, label_w=200, step=44)
    f.box(20, 318, 900, 66, "Cuatro hilos tardaron casi cuatro veces lo que una tarea (2,09 s frente a 0,55 s): ninguna ganancia sobre hacerlas en serie. Los hilos de CPython sirven para esperar E/S, no para repartir cálculo. "
          "Los procesos en Windows pagan el arranque con «spawn».", "gold", 13)
    return f


def se081_buzon() -> Fig:
    f = Fig(960, 400, "Actores como buzones: orden, bloqueo mutuo y buzón sin límite",
            "Tabla: un actor con buzón recibió 4 emisores por 50000 mensajes y su estado fue 200000 sin cerrojos; dos hilos que toman dos cerrojos en orden opuesto con espera acotada terminaron con A fallando y B teniendo éxito; "
            "y un buzón sin límite aceptó un millón de mensajes sin rechazar ninguno.")
    heads = ["Experimento", "Resultado ejecutado", "Lectura"]
    rows = [
        ["Actor: un hilo dueño del estado y un buzón; 4 emisores × 50 000 mensajes", "Estado final = 200 000", "El estado tiene un solo escritor; la sincronización está en la cola"],
        ["Dos cerrojos tomados en orden opuesto por A y B, con timeout de 0,3 s", "A no obtuvo el segundo; B sí", "Sin timeout habría bloqueo mutuo; el timeout lo convierte en fallo observable"],
        ["Buzón sin límite: poner un millón de mensajes", "Aceptó todos; qsize = 1 000 000", "Sin límite de buzón no hay contrapresión: el productor no se entera"],
    ]
    f.table(heads, rows, 10, 12, [340, 270, 330], row_h=88, size=12)
    f.box(10, 332, 940, 56, "Los actores evitan los datos compartidos, no los fallos: el orden entre emisores distintos no está garantizado y el buzón es un recurso finito.", "coral", 13)
    return f


# ---------------------------------------------------------------- SE-082
def se082_tamano() -> Fig:
    f = Fig(960, 430, "Cinco implementaciones de la misma regla: tamaño y costo de añadir una regla",
            "Tabla con el tamaño en líneas no vacías y las líneas modificadas al añadir la regla R4: imperativo 12 y 2, funcional 12 y 1, objetos 24 y 5, declarativo 17 y 1, lógico 26 y 3.")
    heads = ["Paradigma", "Líneas de código", "Líneas cambiadas al añadir R4", "Dónde está la regla nueva"]
    rows = [
        ["Imperativo (if/elif)", "12", "2", "Una rama en la cadena, en el sitio correcto"],
        ["Funcional (predicados y next)", "12", "1", "Una fila en la tupla de reglas"],
        ["Objetos (una clase por regla)", "24", "5", "Una clase nueva y su registro en la lista"],
        ["Declarativo (condiciones como datos)", "17", "1", "Una fila en la tabla de datos"],
        ["Lógico (hechos y cláusulas)", "26", "3", "Una cláusula y un ajuste de otra"],
    ]
    f.table(heads, rows, 10, 12, [270, 140, 230, 300], row_h=50, size=12, head_h=46)
    f.box(10, 370, 940, 44, "Menos líneas no significa mejor: la regla es corta en todos; cambian el lugar donde viven y cuánto del resto hay que tocar.", "gold", 13)
    return f


def se082_costo() -> Fig:
    f = Fig(940, 380, "Costo de ejecutar la misma decisión según el paradigma",
            "Barras en nanosegundos por decisión en Windows: imperativo unos 700, funcional 2035, objetos 2255, declarativo 4820 y lógico 17818; en Linux 1333, 1617, 1856, 2898 y 8375. "
            "El orden relativo se mantiene en lo grueso pero las magnitudes varían entre ejecuciones.")
    f.text(20, 28, "Nanosegundos por decisión en Windows (caso 900 ms, autorizado, mediana)", 14, "start", 700)
    f.hbars([("Imperativo", 700, "teal", "700"), ("Funcional", 2035, "plain", "2035"), ("Objetos", 2255, "plain", "2255"),
             ("Declarativo", 4820, "gold", "4820"), ("Lógico (cláusulas)", 17818, "coral", "17 818")], 20, 44, 0.03, label_w=190, step=46)
    f.box(20, 288, 900, 64, "En Linux el orden fue el mismo, con 1333, 1617, 1856, 2898 y 8375 ns. La interpretación de reglas o cláusulas paga una capa de indirección por decisión.", "gold", 13)
    _note(f, 370, "Medición ruidosa: el imperativo varió de 700 a 1333 ns entre sistemas. Solo se interpreta el orden de magnitud.")
    return f


def se082_matriz() -> Fig:
    f = Fig(960, 450, "Qué evidencia respalda cada criterio de selección de paradigma",
            "Tabla de criterios con su evidencia: tamaño y cambio medidos por diferencia de líneas, costo de ejecución medido, legibilidad y modelo del dominio como juicio sin medir, y acoplamiento declarado como inferencia.")
    heads = ["Criterio", "Cómo se obtuvo aquí", "Estado"]
    rows = [
        ["Costo de ejecutar", "timeit, mediana de cinco repeticiones, dos sistemas", "Medido"],
        ["Superficie de cambio", "difflib entre la versión 1 y la 2 de cada implementación", "Medido"],
        ["Equivalencia de comportamiento", "14 casos fijos más 20 000 entradas aleatorias, 0 desacuerdos", "Medido"],
        ["Legibilidad para un equipo", "Juicio sobre el equipo y su formación", "No medido"],
        ["Ajuste al modelo del dominio", "Depende de si el problema se expresa mejor como reglas, flujo o estado", "Inferencia"],
    ]
    f.table(heads, rows, 10, 12, [260, 500, 180], row_h=56, size=13, kinds=["plain", "plain", ("teal", "teal", "teal", "gold", "gold")])
    f.box(10, 392, 940, 44, "Una selección responsable separa lo medido de lo supuesto y deja los supuestos visibles para revisarlos.", "grey", 13)
    return f


# ---------------------------------------------------------------- SE-083
def se083_contrato() -> Fig:
    f = Fig(960, 400, "Una regla, cinco implementaciones y un contrato común",
            "Diagrama: una observación con latencia y autorización entra a cinco implementaciones (imperativa, funcional, objetos, declarativa y lógica) que devuelven la misma estructura de acción y regla. "
            "Resultado: 14 de 14 casos fijos en cada una y 0 desacuerdos en 20000 entradas aleatorias.")
    f.box(20, 150, 150, 80, "Observación\n{latencia, autorizada}", "gold", 13, bold=True)
    names = ["Imperativa", "Funcional", "Objetos", "Declarativa", "Lógica"]
    for i, n in enumerate(names):
        y = 24 + i * 66
        f.box(300, y, 190, 50, n, "teal", 13, bold=True)
        f.arrow([(170, 190), (300, y + 25)])
        f.arrow([(490, y + 25), (620, 190)])
    f.box(620, 150, 190, 80, "Respuesta\n{acción, regla}", "gold", 13, bold=True)
    f.box(830, 140, 120, 100, "14 / 14\ncasos\n0 desacuerdos\nen 20 000", "plain", 12)
    f.box(20, 350, 920, 38, "La comparación solo es válida porque entrada y salida son las mismas; cambiar el contrato invalida la comparación.", "coral", 13)
    return f


def se083_superficie() -> Fig:
    f = Fig(940, 340, "Superficie de cambio: líneas modificadas al añadir la regla R4",
            "Barras de líneas cambiadas: funcional 1, declarativo 1, imperativo 2, lógico 3 y objetos 5. Los cinco pasaron 16 de 16 casos tras el cambio.")
    f.text(20, 28, "Líneas modificadas al pasar de la versión 1 a la 2 (difflib)", 14, "start", 700)
    f.hbars([("Funcional", 1, "teal", "1"), ("Declarativo", 1, "teal", "1"), ("Imperativo", 2, "plain", "2"), ("Lógico", 3, "gold", "3"), ("Objetos", 5, "coral", "5")],
            20, 44, 90, label_w=170, step=44)
    f.box(20, 270, 900, 52, "Las cinco versiones aprobaron 16 de 16 casos tras el cambio. Pocas líneas no implican menos riesgo: el orden de las reglas sigue siendo significado.", "gold", 13)
    return f


def se083_mutantes() -> Fig:
    f = Fig(960, 430, "Mutantes de la versión imperativa y qué caso los detecta",
            "Tabla de seis mutantes: cambiar mayor por mayor o igual lo detecta solo el caso de latencia 800; quitar la autorización los casos no autorizados; "
            "invalidar menos de -5 el caso -1; permitir booleanos el caso True; invertir autorización y latencia los casos 3 y 12; y mover el umbral a 900 los casos feliz y 801.")
    heads = ["Mutante", "Casos que lo detectan", "Lección"]
    rows = [
        ["> 800 por >= 800", "Solo el caso de latencia 800", "El valor límite exacto es el único que lo delata"],
        ["Sin chequeo de autorización", "Tres casos con authorized = false", "Un camino feliz nunca lo detecta"],
        ["Invalidez: latencia < 0 pasa a < -5", "Solo el caso -1", "Sin un caso inválido cercano, el error pasa"],
        ["Aceptar booleanos como latencia", "Solo el caso True", "Python trata True como entero; solo un caso lo delata"],
        ["Orden: latencia antes de autorización", "Casos 900 no autorizado y 5000 no autorizado", "El orden de las reglas es semántica"],
        ["Umbral 800 pasa a 900", "Caso 900 y caso 801", "Un caso feliz bien elegido ya lo detecta"],
    ]
    f.table(heads, rows, 10, 12, [300, 320, 320], row_h=52, size=12)
    return f


# ---------------------------------------------------------------- SE-084
def se084_matriz() -> Fig:
    f = Fig(960, 420, "Matriz de evidencia común: qué se ejecutó y en qué sistema",
            "Tabla de cuatro comprobaciones: contrato común de 14 casos en cinco implementaciones, 20000 entradas aleatorias con 0 desacuerdos, versión 2 con 16 de 16 casos y costo medido; "
            "las cuatro se ejecutaron en Windows y Linux.")
    heads = ["Comprobación", "Resultado", "Windows 3.12.9", "Linux 3.12.3"]
    rows = [
        ["Contrato: 14 casos fijos × 5 implementaciones", "70 de 70", "Ejecutado", "Ejecutado"],
        ["Prueba diferencial: 20 000 entradas aleatorias", "0 desacuerdos", "Ejecutado", "Ejecutado"],
        ["Versión 2 con R4: 16 casos × 5", "80 de 80", "Ejecutado", "Ejecutado"],
        ["Costo por decisión (timeit)", "700 a 17 818 ns", "Ejecutado", "Ejecutado"],
        ["Prolog real, Erlang, Rust, Rx", "—", "No ejecutado", "No ejecutado"],
    ]
    f.table(heads, rows, 10, 12, [380, 190, 190, 180], row_h=52, size=13, kinds=["plain", "plain", ("teal", "teal", "teal", "teal", "coral"), ("teal", "teal", "teal", "teal", "coral")])
    f.box(10, 366, 940, 40, "Los lenguajes que no estaban instalados se declaran como no ejecutados, no se dan por equivalentes.", "gold", 13)
    return f


def se084_suites() -> Fig:
    f = Fig(940, 380, "Mutantes detectados según el tamaño de la suite de pruebas",
            "Barras del número de mutantes detectados de seis: solo el camino feliz detecta 1, camino feliz más no autorizado detecta 3, camino feliz más el límite 800 y 801 detecta 2, y los catorce casos detectan los 6.")
    f.text(20, 28, "Mutantes detectados de 6 por cada suite", 14, "start", 700)
    f.hbars([("Solo camino feliz (1 caso)", 1, "coral", "1 de 6"), ("Feliz + no autorizado (2)", 3, "gold", "3 de 6"),
             ("Feliz + límites 800 y 801 (3)", 2, "gold", "2 de 6"), ("Los 14 casos", 6, "teal", "6 de 6")], 20, 44, 100, label_w=270, step=46)
    f.box(20, 252, 900, 74, "Dos suites de tamaño parecido detectan mutantes distintos. El valor de una prueba depende de qué regla ejercita, no de cuántas hay.", "gold", 13)
    _note(f, 360, "Seis mutantes escritos a mano sobre la versión imperativa; no es una medición de mutación sistemática.")
    return f


def se084_informe() -> Fig:
    f = Fig(960, 430, "Estructura del informe de comparación: afirmación, evidencia y límite",
            "Tabla de tres afirmaciones con su evidencia y lo que no prueban: equivalencia en los casos probados, costo de cambio medido por diferencia de líneas y costo de ejecución medido en un microbenchmark.")
    heads = ["Afirmación del informe", "Evidencia que la sostiene", "Lo que no prueba"]
    rows = [
        ["Las cinco versiones son equivalentes sobre el dominio probado", "14 casos fijos y 20 000 entradas aleatorias, 0 desacuerdos", "Equivalencia sobre entradas fuera del generador, incluidos tipos exóticos"],
        ["La regla nueva cuesta menos líneas en el funcional y el declarativo", "Diferencia de líneas entre versión 1 y 2", "Que el equipo entienda mejor esas formas"],
        ["El imperativo es el más rápido y el lógico el más lento", "timeit en dos sistemas, mismo orden", "Que la diferencia importe para la carga real"],
    ]
    f.table(heads, rows, 10, 12, [330, 320, 290], row_h=96, size=13)
    f.box(10, 366, 940, 44, "Cada afirmación del informe enlaza un artefacto reproducible; las que no lo tienen se marcan como juicio.", "coral", 13)
    return f


FIGURES = {
    "se-079-orden-de-despacho.svg": se079_orden,
    "se-079-manejador-bloqueante.svg": se079_bloqueo,
    "se-079-fallos-de-un-bus.svg": se079_fallos,
    "se-080-memoria-perezosa.svg": se080_memoria,
    "se-080-contrapresion.svg": se080_contrapresion,
    "se-080-semantica-de-flujos.svg": se080_semantica,
    "se-081-condicion-de-carrera.svg": se081_carrera,
    "se-081-hilos-y-procesos.svg": se081_cpu,
    "se-081-buzones-y-cerrojos.svg": se081_buzon,
    "se-082-tamano-y-cambio.svg": se082_tamano,
    "se-082-costo-de-ejecucion.svg": se082_costo,
    "se-082-criterios-y-evidencia.svg": se082_matriz,
    "se-083-contrato-comun.svg": se083_contrato,
    "se-083-superficie-de-cambio.svg": se083_superficie,
    "se-083-mutantes.svg": se083_mutantes,
    "se-084-matriz-de-evidencia.svg": se084_matriz,
    "se-084-suites-y-mutantes.svg": se084_suites,
    "se-084-estructura-del-informe.svg": se084_informe,
}
