"""Figures for SE-385 to SE-390 (synthetic models with fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3).

Every figure is a chart or a diagram of the mechanism; the Markdown tables of the classes keep the exact values.
"""
from __future__ import annotations

from figure_kit import (AXIS, FILL, INK, Fig, _kit_finish, _kit_start, dumbbell, grouped_bars, line_chart, scatter,
                        stacked_bars)
from figures_part07_a import bars

SINT = "Modelos sintéticos con semilla fija; resultados idénticos en Windows y Ubuntu (WSL2) salvo donde se indica."


# ---------------------------------------------------------------- SE-385
def se337_modelos() -> Fig:
    return grouped_bars(
        "Tiempo total de 200 solicitudes según el modelo de ejecución y la proporción de espera",
        "Barras agrupadas en escala logarítmica con el tiempo total de 200 solicitudes: con 10 ms de CPU y 90 de espera, el modelo concurrente de un núcleo baja de 20 000 a 2 090 ms y combinado con 4 núcleos a 590; con 100 ms de CPU y nada de espera solo ayuda el paralelismo, que da 5 000 ms, y la concurrencia no mejora nada.",
        ["10 ms CPU + 90 ms espera", "90 ms CPU + 10 ms espera", "100 ms CPU + 0 espera"],
        [("Secuencial", [20000, 20000, 20000], "grey"), ("Concurrente, 1 núcleo", [2090, 18010, 20000], "gold"),
         ("Paralelo, 4 núcleos", [5000, 5000, 5000], "navy"), ("Concurrente y 4 núcleos", [590, 4510, 5000], "teal")],
        unit="Milisegundos virtuales", log=True, plot_h=300,
        note="Concurrencia y paralelismo resuelven problemas distintos: solapar esperas ayuda cuando hay espera (barra dorada baja a la izquierda y se pega a la gris a la derecha); repartir CPU ayuda cuando hay CPU (barra azul igual en los tres grupos). Un hilo que bloquea mientras espera gasta un núcleo entero. Es un planificador en tiempo virtual escrito por el autor, no una medición de Python ni de un sistema operativo.",
        note_kind="gold", foot=SINT)


def se337_bucle() -> Fig:
    items = [("Sin ceder nunca", 1, "coral", "1 de 20 latidos"), ("Cede cada 50 000 vueltas", 5, "gold", "5 de 20"),
             ("Cede cada 10 000 vueltas", 20, "teal", "20 de 20"), ("Cede cada 1 000 vueltas", 20, "teal", "20 de 20")]
    return bars("Latidos de una tarea vecina emitidos antes de que termine un cálculo de 200 000 vueltas (asyncio)",
                "Barras con los latidos que una tarea vecina logra emitir mientras otra calcula en el mismo bucle de eventos: un latido de 20 si el cálculo nunca cede, 5 si cede cada 50 000 vueltas y 20 de 20 si cede cada 10 000 o cada 1 000.",
                items, 22, "Un bucle de eventos es un solo hilo: una tarea que no espera no deja pasar a ninguna otra. Se cuentan latidos en vez de milisegundos para que el resultado no dependa del equipo. Ceder más a menudo reparte mejor, a costa de más cambios de contexto que esta medida no cuenta.",
                label_w=300, width=980, note_kind="coral", foot=SINT)


def se337_amdahl() -> Fig:
    def serie(vals):
        return [(1, 1.0)] + list(zip((2, 4, 8, 16, 64), vals))
    return line_chart(
        "Aceleración según el número de trabajadores y la parte secuencial (ley de Amdahl)",
        "Líneas en escala logarítmica del número de trabajadores con la aceleración teórica: con un 5 por ciento secuencial, 64 trabajadores dan 15,4 veces y el tope es 20; con un 10 por ciento dan 8,8 y el tope es 10; con un 25 por ciento dan 3,8 y el tope es 4; con un 50 por ciento el tope es 2 y 8 trabajadores ya dan 1,8. Cada curva se aplana contra su tope.",
        [("5 % secuencial", serie([1.90, 3.48, 5.93, 9.14, 15.42]), "teal"), ("10 %", serie([1.82, 3.08, 4.71, 6.40, 8.77]), "navy"),
         ("25 %", serie([1.60, 2.29, 2.91, 3.37, 3.82]), "gold"), ("50 %", serie([1.33, 1.60, 1.78, 1.88, 1.97]), "coral")],
        x_label="Trabajadores", y_label="Aceleración (veces frente a un trabajador)", log_x=True,
        x_ticks=[(1, "1"), (2, "2"), (4, "4"), (8, "8"), (16, "16"), (64, "64")], y_ticks=[0, 5, 10, 15, 20],
        hlines=[(20, "tope 5 %: 20"), (10, "tope 10 %: 10"), (4, "tope 25 %: 4"), (2, "tope 50 %: 2")],
        point_labels="last", plot_h=330, decimals=1,
        note="Acercarse al tope exige muchos más trabajadores de los que parece: con un 5 % secuencial hacen falta 171 para llegar al 90 % de 20, y con un 50 %, 10 para el 90 % de 2. La fórmula es 1 / (s + (1 − s) / n) y supone una carga fija sin costo de coordinación, que en la práctica añade un tramo secuencial más.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-386
def se338_contador() -> Fig:
    return stacked_bars(
        "Dos hilos suben un contador dos veces cada uno: valor final en todas las intercalaciones (correcto: 4)",
        "Barras apiladas horizontales con el valor final del contador en todas las intercalaciones: sin cerrojo, de 70 intercalaciones solo 6 terminan en 4, 32 terminan en 3 y 32 en 2 sin aviso; con un cerrojo alrededor de cada incremento solo son posibles 6 intercalaciones y todas terminan en 4.",
        ["Sin cerrojo: leer, sumar, escribir", "Con cerrojo alrededor de cada incremento"],
        [("Final = 4 (correcto)", [6, 6], "teal"), ("Final = 3", [32, 0], "gold"), ("Final = 2", [32, 0], "coral")],
        unit="Intercalaciones posibles", horizontal=True, label_w=260,
        note="Cuatro hilos reales de CPython 3.12 con 100 000 incrementos sin cerrojo dieron 400 000 en tres ejecuciones: el defecto existe y no se vio. Que una prueba pase no demuestra que no haya carrera; enumerar o forzar el orden sí la expone.",
        note_kind="coral", foot=SINT)


def se338_interbloqueo() -> Fig:
    return stacked_bars(
        "Dos hilos y dos cerrojos: ejecuciones del modelo de estados que completan o terminan en interbloqueo",
        "Barras apiladas horizontales con las ejecuciones del modelo de estados: con orden opuesto de adquisición, de 6 ejecuciones 4 completan y 2 terminan en interbloqueo, el 33,3 por ciento; con el mismo orden las 2 ejecuciones completan y ninguna se bloquea.",
        ["Un hilo toma A y luego B; el otro, B y luego A", "Ambos toman A y luego B"],
        [("Completan", [4, 2], "teal"), ("Interbloqueo", [2, 0], "coral")],
        unit="Ejecuciones del modelo", horizontal=True, label_w=260,
        note="Un orden global de adquisición elimina el ciclo de espera. El tiempo límite no lo evita: lo convierte en un error, y quién falla primero depende de una carrera de temporización (en la versión real con barrera y 0,3 s ambos hilos agotan el tiempo en Windows y uno completa en Ubuntu). Recuperarse exige liberar lo ya tomado y poder repetir.",
        note_kind="teal", foot="Modelo exhaustivo determinista; la versión real con tiempo límite no es reproducible entre sistemas.")


def se338_granularidad() -> Fig:
    return grouped_bars(
        "Fracción del trabajo que avanza sin esperar con 8 trabajadores (20 000 rondas, 40 cursos)",
        "Barras agrupadas con la fracción del trabajo que avanza sin esperar: con un cerrojo global 12,5 por ciento; con 8 fragmentos 59,1 si los cursos se piden con popularidad Zipf y 65,6 si son uniformes; con un cerrojo por curso 73,8 y 91,7. La popularidad desigual limita lo que gana dividir.",
        ["Un cerrojo global", "8 fragmentos (clave módulo 8)", "Un cerrojo por curso (40)"],
        [("Cursos con popularidad Zipf 1,1", [12.5, 59.1, 73.8], "coral"), ("Cursos uniformes", [12.5, 65.6, 91.7], "teal")],
        unit="% del trabajo que avanza sin esperar", decimals=1,
        note="Dividir el cerrojo ayuda hasta donde la distribución de las claves lo permite: con unos pocos cursos populares, los trabajadores siguen chocando en el mismo cerrojo. Cada ronda es una comparación de claves, no tiempo de ejecución; un cerrojo por curso tiene además un costo de memoria y de orden de adquisición.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-387
def se339_orden() -> Fig:
    title = "Un buzón conserva el orden de cada emisor, no el orden entre emisores: dos de los 90 órdenes posibles"
    desc = ("Diagrama con dos de los 90 órdenes globales que pueden salir del buzón cuando tres emisores envían dos mensajes cada uno: en ambos, el primer mensaje de cada emisor sale antes que su segundo, pero los emisores se intercalan de forma distinta. "
            "En 2 000 ejecuciones asyncio produjo 89 órdenes globales distintos y ninguna alteró el orden de los mensajes de un mismo emisor.")
    width = 940
    f, y = _kit_start(title, desc, width, [("Emisor A", "teal", "bar"), ("Emisor B", "gold", "bar"), ("Emisor C", "coral", "bar")])
    orders = [("Una ejecución", ["A1", "B1", "A2", "C1", "C2", "B2"]), ("Otra ejecución", ["C1", "B1", "B2", "A1", "C2", "A2"])]
    kinds = {"A": "teal", "B": "gold", "C": "coral"}
    lw, x0 = 150, 14 + 150 + 10
    cw = (width - 20 - x0) / 6
    f.text(x0 + cw * 3, y + 14, "Orden en que el buzón entrega los mensajes", 13, "middle", 400, AXIS)
    f.arrow([(x0, y + 24), (width - 24, y + 24)])
    y += 34
    for r, (name, seq) in enumerate(orders):
        ry = y + r * 62
        f.text(14 + lw, ry + 36, name, 13, "end", 700, INK)
        for i, m in enumerate(seq):
            f.parts.append(f'<rect x="{x0 + cw * i + 3:g}" y="{ry + 8:g}" width="{cw - 6:g}" height="44" rx="6" fill="{FILL[kinds[m[0]]]}"/>')
            f.text(x0 + cw * i + cw / 2, ry + 36, m, 15, "middle", 700, "#ffffff")
    y += 2 * 62
    f.text(14, y + 22, "Dentro de cada color el número 1 siempre sale antes que el 2: eso es lo único que el buzón garantiza.", 13, "start", 700, INK)
    return _kit_finish(f, y + 30,
                       "El orden entre emisores no existe como propiedad del buzón: depende de quién llegó antes. De los 90 órdenes posibles se observaron 89 en 2 000 ejecuciones, y en 0 un emisor vio alterado su propio orden. Cualquier lógica que suponga el orden entre emisores funcionará hasta que cambie el reparto de los turnos. El retardo aleatorio de los emisores es una construcción del autor.",
                       "teal", SINT)


def se339_contrapresion() -> Fig:
    return stacked_bars(
        "Un productor de 3 mensajes por turno y un consumidor de 1 por turno, 1 000 turnos: adónde va el exceso",
        "Barras apiladas horizontales de los 3 000 mensajes producidos: el consumidor procesa siempre 1 000; sin límite quedan 2 000 en cola y el último espera 2 000 turnos; con una cola de 100 se rechazan 1 901 y quedan 99 con espera de 99 turnos; con una cola de 10 se rechazan 1 991 y quedan 9.",
        ["Cola sin límite", "Cola de 100", "Cola de 10"],
        [("Procesados", [1000, 1000, 1000], "teal"), ("En cola al final", [2000, 99, 9], "gold"), ("Rechazados", [0, 1901, 1991], "coral")],
        unit="Mensajes producidos en 1 000 turnos", horizontal=True, label_w=150,
        note="La cola no crea capacidad: solo decide dónde espera el exceso. Sin límite, el exceso se convierte en latencia creciente y memoria (el último espera 2 000 turnos); con límite se convierte en un rechazo que el emisor puede ver y manejar (espera de 99 y de 9 turnos). Las tasas de 3 y 1 son supuestos del autor.",
        note_kind="coral", foot=SINT)


def se339_estructura() -> Fig:
    return dumbbell(
        "Qué queda a medias cuando una tarea falla o se cancela, sin y con la protección de la clase (asyncio, CPython 3.12)",
        "Mancuernas con dos comparaciones: tras una falla, gather deja 2 tareas hermanas vivas sin dueño y TaskGroup deja 0; al cancelar una transferencia de cuatro pasos, 3 de 6 instantes dejan estado a medias sin escudo y 0 con escudo.",
        [("Tareas hermanas vivas tras una falla (gather frente a TaskGroup)", 2, 0),
         ("Instantes de cancelación de 6 que dejan la transferencia a medias (sin escudo frente a con escudo)", 3, 0)],
        unit="Tareas vivas o instantes incoherentes", names=("gather / sin escudo", "TaskGroup / con escudo"),
        delta=lambda a, b: f"−{a - b:g}", label_w=330,
        note="La concurrencia estructurada ata la vida de una tarea al bloque que la creó: con TaskGroup una hermana que falla cancela a las demás y el error llega a quien creó el grupo; con gather las hermanas terminan «ok» sin dueño. No resuelve la atomicidad: una cancelación llega en un punto de espera y deja lo ya hecho (por ejemplo 25 + 30); hay que decidir qué es indivisible. Pasos simulados con await de turno, no entrada y salida real.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-388
def se340_lamport() -> Fig:
    return stacked_bars(
        "Los 44 850 pares de eventos de 3 nodos: qué relación ve cada reloj",
        "Barras apiladas horizontales sobre los 44 850 pares de eventos: el reloj vectorial separa 40 317 pares con causalidad y 4 533 concurrentes; el reloj de Lamport da marcas distintas a 44 617 pares y ordena 4 300 pares que en realidad son concurrentes, aparentando un orden que no existe.",
        ["Reloj vectorial", "Reloj de Lamport"],
        [("Con causalidad (orden real)", [40317, 40317], "teal"), ("Concurrentes, reconocidos como tales", [4533, 233], "gold"),
         ("Concurrentes con un orden inventado", [0, 4300], "coral")],
        unit="Pares de eventos", horizontal=True, label_w=150,
        note="Si a causó b, la marca de Lamport de a es menor; la inversa no vale: una marca menor no implica causa. Los 4 300 pares en coral son el 9,6 % de los pares con marcas distintas; los vectoriales distinguen causa de concurrencia a cambio de un vector por evento. Mensajes y turnos son una simulación del autor con semilla 340.",
        note_kind="gold", foot=SINT)


def se340_desfase() -> Fig:
    items = [("Desfase ±50 ms", 0.0, "teal", "0 %"), ("Desfase ±75 ms", 5.08, "gold", "5,08 %"), ("Desfase ±100 ms", 11.94, "gold", "11,94 %"),
             ("Desfase ±250 ms", 31.47, "coral", "31,47 %"), ("Desfase ±1 000 ms", 44.41, "coral", "44,41 %")]
    return bars("Escrituras posteriores que pierden frente a una anterior cuando gana la marca de tiempo más alta",
                "Barras con el porcentaje de veces que una escritura causalmente posterior, hecha 100 ms después, pierde contra la anterior: 0 con desfase de 50 ms, 5,1 con 75, 11,9 con 100, 31,5 con 250 y 44,4 con 1 000 ms; con reloj híbrido, 0 en todos.",
                items, 11, "La pérdida empieza cuando el desfase entre relojes supera la mitad de la separación causal (50 ms de cada lado con 100 ms de separación). Un reloj híbrido que toma el máximo entre la hora local y la última marca vista dio 0 de 20 000 en todos los casos. Los desfases son supuestos del autor.",
                label_w=240, width=980, note_kind="coral", foot=SINT)


def se340_reloj() -> Fig:
    return grouped_bars(
        "Resolución de los relojes de Python en dos sistemas operativos (escala logarítmica)",
        "Barras agrupadas horizontales en escala logarítmica con la resolución de time.time() y de time.monotonic(): 15,6 ms en Windows 11 frente a 1 ns en Ubuntu (WSL2), una diferencia de unos 15 millones de veces en los dos relojes.",
        ["time.time()", "time.monotonic()"],
        [("Windows 11", [15_600_000, 15_600_000], "coral"), ("Ubuntu (WSL2)", [1, 1], "teal")],
        unit="Resolución en nanosegundos", horizontal=True, log=True, ticks=[1, 1000, 1_000_000, 1_000_000_000],
        value_fmt=lambda v: "15,6 ms" if v > 1000 else "1 ns", label_w=150, plot_h=180,
        note="Para medir cuánto duró algo se usa un reloj monotónico; para decir cuándo ocurrió, el de pared, sabiendo que se ajusta y que los nodos no coinciden. Medir 5 ms con un reloj de 15,6 ms es inexacto: la resolución es una propiedad del sistema, no de Python. El monotónico no retrocedió en 2 000 000 de lecturas y, con un ajuste simulado de −80 ms (1 de cada 500), el reloj de pared dio 205 duraciones negativas en 100 000 mediciones y el monotónico 0 (iguales en los dos sistemas).",
        note_kind="teal", foot="Resolución medida con time.get_clock_info; el ajuste de reloj es una simulación con semilla 3403.")


# ---------------------------------------------------------------- SE-389
def se341_agotado() -> Fig:
    return stacked_bars(
        "Cuando el cliente se rinde, ¿se ejecutó la operación? (100 000 solicitudes, tres perfiles de red)",
        "Barras apiladas horizontales al 100 por ciento con los tiempos agotados de 100 000 solicitudes: con peticiones perdidas 2 por ciento, respuestas perdidas 2 y lentas 1, la operación sí se ejecutó en el 59,1 por ciento de los 4 986 tiempos agotados; con respuestas lentas del 10 por ciento sube al 85,1 y con pérdida de peticiones de 0,5 y de respuestas de 5, al 93,4.",
        ["2 % · 2 % · 1 % (4 986 tiempos agotados)", "2 % · 2 % · 10 % (13 649)", "0,5 % · 5 % · 2 % (7 389)"],
        [("La operación se ejecutó", [2946, 11609, 6904], "coral"), ("No se ejecutó", [2040, 2040, 485], "teal")],
        unit="Tiempos agotados", horizontal=True, percent=True, decimals=1, label_w=270,
        note="Desde fuera, un tiempo agotado cubre tres historias que el cliente no puede distinguir (petición perdida, respuesta perdida, respuesta lenta). Reintentar sin una clave de idempotencia duplica el efecto en la mayoría de los casos. El perfil se lee petición perdida · respuesta perdida · respuesta lenta. Las tres probabilidades son supuestos del autor; la proporción cambia con ellas, el mecanismo no.",
        note_kind="coral", foot=SINT)


def se341_reintentos() -> Fig:
    items = [("1 capa", 3, "teal", "3 intentos"), ("2 capas", 9, "gold", "9 intentos"), ("3 capas", 27, "coral", "27 intentos"), ("4 capas", 81, "coral", "81 intentos")]
    return bars("Intentos que recibe el servicio final por cada solicitud, si cada capa reintenta 2 veces y el servicio falla siempre",
                "Barras: con 2 reintentos por capa, el servicio del fondo recibe 3 intentos con una capa, 9 con dos, 27 con tres y 81 con cuatro por cada solicitud del usuario.",
                items, 6, "El factor es (1 + reintentos) elevado al número de capas. Con un presupuesto de reintentos del 10 % por capa, los intentos por solicitud con el servicio caído quedaron en 1,10 en vez de 3,00, y con un reintento con espera aleatoria el pico bajó de 1 000 a 159 reintentos por ventana de 10 ms.",
                label_w=190, width=980, note_kind="gold", foot=SINT)


def se341_detector() -> Fig:
    pts = [(32.34, 1150, "150 ms", "r"), (10.97, 1300, "300 ms", "t"), (2.25, 1600, "600 ms", "t"), (0.28, 2200, "1 200 ms", "t"), (0.02, 3400, "2 400 ms", "t")]
    return line_chart(
        "Detector de fallos por latidos cada 1 000 ms: falsas sospechas frente a retraso en detectar, según el tiempo límite",
        "Línea que une cinco tiempos límite: con 150 ms el 32,34 por ciento de los latidos de un nodo sano parece una falla y un nodo caído se detecta 1 150 ms después del último latido; con 600 ms, 2,25 por ciento y 1 600 ms; con 2 400 ms, 0,02 por ciento y 3 400 ms. Bajar las falsas alarmas retrasa la detección.",
        [("Tiempo límite (rótulo de cada punto)", pts, "teal")],
        x_label="Latidos de un nodo sano que se sospechan (%)", y_label="Retraso en detectar un nodo caído (ms)",
        log_x=True, x_ticks=[(0.01, "0,01"), (0.1, "0,1"), (1, "1"), (10, "10"), (100, "100")], y_ticks=[0, 1000, 2000, 3000, 4000],
        point_labels="all", y_zero=True, plot_h=300,
        note="No existe un tiempo límite que dé detección rápida y cero falsas sospechas: subirlo baja las falsas alarmas y retrasa la detección, y por eso la curva baja hacia la derecha. La distribución del retardo (lognormal, mediana 100 ms, p99 de 795 ms) es un supuesto del autor, no una red medida.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-390
def se342_cp_ap() -> Fig:
    return grouped_bars(
        "Una réplica de tres aislada durante 300 de 1 000 operaciones: qué cuesta rechazar y qué cuesta aceptar",
        "Barras agrupadas con el costo de cada política: si la réplica aislada rechaza (CP) se rechazan 97 operaciones y no hay lecturas obsoletas ni escrituras perdidas; si acepta (AP) se atienden las 1 000, pero hay 89 lecturas obsoletas y 27 escrituras del lado aislado que se descartan al reparar.",
        ["Operaciones rechazadas", "Lecturas obsoletas", "Escrituras aceptadas por el lado aislado", "Escrituras descartadas al reparar"],
        [("Rechazar (CP)", [97, 0, 0, 0], "navy"), ("Aceptar (AP)", [0, 89, 27, 27], "coral")],
        unit="Operaciones de 1 000", horizontal=True, label_w=250,
        note="Durante la partición no se puede conservar a la vez la respuesta a todas las peticiones y la coherencia con lo último escrito: rechazar atiende 903 operaciones de 1 000 y aceptar las atiende todas. Rechazar cuesta disponibilidad visible; aceptar cuesta un trabajo de reparación que hay que definir antes. La carga y la duración de la partición son supuestos del autor.",
        note_kind="teal", foot=SINT)


def se342_cuorum() -> Fig:
    return scatter(
        "Tres réplicas: caídas que tolera cada cuórum al escribir y al leer, y si garantiza ver lo último",
        "Dispersión con cinco cuórums de tres réplicas según las caídas que toleran al escribir y al leer: W=2 y R=2 (1 y 1), W=3 y R=1 (0 y 2) y W=1 y R=3 (2 y 0) garantizan leer lo último porque W + R supera 3; W=1 y R=1 (2 y 2) y W=2 y R=1 (1 y 2) no lo garantizan. Los que garantizan caen sobre una diagonal: lo que se gana en una operación se pierde en la otra.",
        [("Garantiza leer lo último (W + R > 3)", [(1, 1, "W=2, R=2", "t"), (0, 2, "W=3, R=1", "r"), (2, 0, "W=1, R=3", "t")], "teal"),
         ("No lo garantiza", [(2, 2, "W=1, R=1", "l"), (1, 2, "W=2, R=1", "t")], "coral")],
        x_label="Caídas toleradas al escribir (N − W)", y_label="Caídas toleradas al leer (N − R)",
        x_ticks=[(0, "0"), (1, "1"), (2, "2")], y_ticks=[0, 1, 2], point_labels="all", y_zero=True, plot_h=300,
        note="La garantía sale de la intersección: toda lectura toca al menos una réplica que vio la última escritura cuando W + R > N. A cambio se pierde tolerancia a caídas en una de las dos operaciones; con 1 % de caída por réplica la disponibilidad va del 97,03 % (W=3) al 99,9999 % (W=1). Sin reloj ni fallos parciales de red: es el modelo de conjuntos alcanzables, no un sistema real.",
        note_kind="gold", foot="Enumeración exacta de subconjuntos y cálculo binomial; sin simulación aleatoria.")


def se342_reparacion() -> Fig:
    return dumbbell(
        "Reparar dos lados que divergieron: entregas que conserva el último escritor gana frente a un tipo que se fusiona",
        "Mancuernas con las entregas conservadas tras una partición: el último escritor gana conserva 1 048 de 2 059 entregas contadas y 500 de 750 entregas distintas; un contador por réplica y una unión de conjuntos conservan las 2 059 y las 750.",
        [("Contador de entregas (2 059 reales)", 1048, 2059), ("Conjunto de entregas (750 reales)", 500, 750)],
        unit="Entregas conservadas", names=("Último escritor gana", "Tipo que se fusiona"), lower_is_better=False,
        delta=lambda a, b: f"+{b - a:,.0f}".replace(",", " "), label_w=260,
        note="Fusionar sin perder nada es posible cuando la operación conmuta y se tolera su semántica: sumar sí, borrar no sin más información (la unión simple resucita 50 entregas que se habían borrado en un lado). Cada tipo fusionable fija qué conflictos resuelve. Las cantidades salen de semilla 3423; la latencia de 1 ms frente a 81 ms de replicar de forma síncrona entre regiones es un supuesto.",
        note_kind="coral", foot=SINT)


FIGURES = {
    "se-385-concurrente-o-paralelo.svg": se337_modelos,
    "se-385-bucle-que-no-cede.svg": se337_bucle,
    "se-385-ley-de-amdahl.svg": se337_amdahl,
    "se-386-intercalaciones-del-contador.svg": se338_contador,
    "se-386-interbloqueo-por-orden.svg": se338_interbloqueo,
    "se-386-granularidad-del-cerrojo.svg": se338_granularidad,
    "se-387-orden-por-emisor.svg": se339_orden,
    "se-387-contrapresion-del-buzon.svg": se339_contrapresion,
    "se-387-dueno-de-una-tarea.svg": se339_estructura,
    "se-388-lamport-y-vectores.svg": se340_lamport,
    "se-388-desfase-y-ultimo-escritor.svg": se340_desfase,
    "se-388-reloj-de-pared-y-monotonico.svg": se340_reloj,
    "se-389-que-significa-un-tiempo-agotado.svg": se341_agotado,
    "se-389-amplificacion-de-reintentos.svg": se341_reintentos,
    "se-389-detector-de-fallos.svg": se341_detector,
    "se-390-rechazar-o-aceptar.svg": se342_cp_ap,
    "se-390-cuorum-de-lectura-y-escritura.svg": se342_cuorum,
    "se-390-reparar-lo-divergente.svg": se342_reparacion,
}
