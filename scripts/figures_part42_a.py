"""Figures for SE-507 to SE-511 (chaos engineering; simulated time with fixed seeds, plus one local measurement)."""
from __future__ import annotations

from experiments_part42_a import (
    e505_estado_estable, e506_radio, e507_declarada, e507_serie, e508_disco, e508_firmas, e508_reloj, e510_ml, e510_replicacion,
)
from figure_kit import Fig, grouped_bars, heatmap, line_chart

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Medición real del 23 de noviembre de 2026 en Windows 11 con CPython 3.12.9 (sockets y relojes reales): los conteos se repiten y los milisegundos varían unos puntos."

# Valores medidos con scripts/experiments_part42_a.py e509 (30 peticiones por escenario, espera de 300 ms). La figura usa estas constantes para que el SVG sea determinista.
MEDIDO_509 = {
    "n": 30,
    "directo": {"mediana ms": 10.4, "p95 ms": 12.1},
    "filas": {
        "sin tóxico": {"exitos": 30, "mediana ms": 11.1, "p95 ms": 12.0},
        "latencia 50 ms": {"exitos": 30, "mediana ms": 61.4, "p95 ms": 62.4},
        "latencia 200 ms": {"exitos": 30, "mediana ms": 211.5, "p95 ms": 251.4},
        "latencia 400 ms": {"exitos": 0, "mediana ms": 310.8, "p95 ms": 312.3},
        "reinicio de conexión": {"exitos": 0, "mediana ms": 10.4, "p95 ms": 11.3},
        "silencio": {"exitos": 0, "mediana ms": 311.0, "p95 ms": 311.8},
    },
}


def n(x: float, d: int = 0) -> str:
    """Formato español: espacio como separador de miles y coma decimal."""
    return f"{x:,.{d}f}".replace(",", "§").replace(".", ",").replace("§", " ")


def p(x: float, d: int = 1) -> str:
    return n(100 * x, d) + " %"


CFG_LABEL = {
    "A": "A · solo espera de 5 s",
    "B": "B · 3 reintentos sin pausa",
    "C": "C · espera corta y reintentos con azar",
    "D": "D · C con cortacircuitos sensible",
    "E": "E · C con cortacircuitos calibrado",
}


# ---------------------------------------------------------------- SE-507
def se507_matriz() -> Fig:
    r = e507_declarada()
    faults = r["fallas"]
    rows = list(r["configs"])
    vals = [[r["celdas"][f"{c}|{fn}"]["ok"] * 100 for fn in faults] for c in rows]
    short = ["Red +100 ms", "Lenta +100 ms", "30 % errores", "Mitad hilos", "Sin respuesta", "Caída 12 s"]
    return heatmap(
        "Cinco clientes que declaran resiliencia frente a seis fallas: peticiones respondidas con calidad completa mientras dura la falla",
        "Mapa de calor con el porcentaje de peticiones correctas y completas durante la falla para cinco configuraciones del cliente y seis fallas inyectadas: solo la latencia de red de 100 milisegundos no daña a ninguna; la configuración con reintentos sin pausa llega a 0 por ciento con la dependencia lenta y la configuración con espera corta y reintentos con azar cae a 0 con la dependencia lenta y con la caída del proceso; ninguna configuración sostiene la calidad completa con la dependencia lenta, la falta de respuesta y la caída del proceso.",
        [CFG_LABEL[c] for c in rows], short, vals,
        unit="Peticiones correctas (%)", scale="teal", vmin=0, vmax=100, decimals=0, suffix=" %", label_w=300,
        note=f"Cada configuración «declara» tiempo de espera y reintentos, y desde fuera todas se ven iguales. Con {r['semillas']} semillas y {int(r['tasa'])} peticiones por segundo, la superficie solo se distingue al inyectar. Las alternativas de D y E responden algo en lugar de fallar, pero eso no es calidad completa. El servicio, los parámetros y las fallas son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se507_recuperacion() -> Fig:
    r = e507_serie()["serie"]
    return line_chart(
        "La falla termina a los 60 s: tres clientes tras perder la mitad de los hilos de la dependencia entre los 30 y los 60 s",
        "Líneas con el porcentaje de peticiones correctas por ventana de 10 segundos: el cliente con una espera de 5 segundos y sin reintentos se mantiene en 100 por ciento; el cliente con espera corta y reintentos con azar cae a 10 por ciento a los 45 segundos y a 0 desde los 55 y no se recupera cuando la falla termina a los 60; el cliente con cortacircuitos calibrado cae a 44 por ciento y vuelve a 100 a los 75 segundos.",
        [("A · solo espera de 5 s", [(x, y * 100) for x, y in r["A"]], "gold"), ("C · espera corta y reintentos con azar", [(x, y * 100) for x, y in r["C"]], "coral"), ("E · con cortacircuitos calibrado", [(x, y * 100) for x, y in r["E"]], "teal")],
        x_label="Segundos desde el inicio (centro de cada ventana de 10 s)", y_label="Peticiones correctas (%)", decimals=0, point_labels="none",
        x_ticks=[(x, str(x)) for x in range(5, 110, 10)], vlines=[(30, "inicio"), (60, "fin")], y_ticks=[0, 25, 50, 75, 100],
        note="El cliente C sigue fallando 50 segundos después de que la dependencia se recuperó: cada petición lenta se reintenta tres veces, el triple de carga mantiene la cola llena y la cola llena produce más esperas agotadas. Es un fallo metaestable. El cliente A no lo sufre porque no multiplica la carga, pero tampoco ayuda: pierde 63 % con una dependencia lenta.",
        note_kind="coral", foot=SINT)


def se507_amplificacion() -> Fig:
    r = e507_declarada()
    rows = list(r["configs"])
    return grouped_bars(
        "Intentos que cada petición de una persona manda a la dependencia mientras esta falla",
        "Barras horizontales con los intentos por petición durante la dependencia lenta y durante la caída del proceso: la espera de 5 segundos sin reintentos manda 1 intento en ambos casos; los reintentos sin pausa mandan 2,3 y 3,6; la espera corta con reintentos con azar manda 3,0 y 3,0; el cortacircuitos los reduce a cerca de 1.",
        [CFG_LABEL[c] for c in rows],
        [("Dependencia lenta +100 ms", [r["celdas"][f"{c}|dependencia lenta +100 ms"]["intentos"] for c in rows], "gold"), ("Proceso caído 12 s", [r["celdas"][f"{c}|proceso caído 12 s"]["intentos"] for c in rows], "coral")],
        unit="Intentos por petición", horizontal=True, decimals=1, label_w=290, ref_lines=[(1, "1 intento")],
        note="Un intento extra por cada petición que falla es la forma más barata de convertir una lentitud en una sobrecarga: la dependencia recibe tres veces el trabajo justo cuando tiene menos capacidad. El cortacircuitos corta el flujo y por eso recupera. Los 90 intentos por segundo y los 8 hilos de 40 ms son supuestos del autor.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-505
def se505_ruido() -> Fig:
    r = e505_estado_estable()
    ws = list(r["estado estable"])
    return line_chart(
        "Cuánto varía por azar la proporción de peticiones rápidas de un servicio sano según la ventana de medición",
        f"Línea con la desviación típica de la proporción de peticiones correctas y rápidas, en puntos porcentuales, según la ventana: {n(r['estado estable'][ws[0]]['desv'] * 100, 2)} con 5 segundos, {n(r['estado estable'][ws[2]]['desv'] * 100, 2)} con 30 y {n(r['estado estable'][ws[4]]['desv'] * 100, 2)} con 120; la media es {n(r['sli base'] * 100, 1)} por ciento en todas.",
        [("Desviación típica del indicador", [(int(w), r["estado estable"][w]["desv"] * 100, n(r["estado estable"][w]["desv"] * 100, 2), "t") for w in ws], "teal"),
         ("Percentil 1 del indicador, respecto de la media", [(int(w), (r["estado estable"][w]["media"] - r["estado estable"][w]["p1"]) * 100, n((r["estado estable"][w]["media"] - r["estado estable"][w]["p1"]) * 100, 2), "b") for w in ws], "gold")],
        x_label="Ventana de medición (s)", y_label="Puntos porcentuales", x_ticks=[(int(w), str(w)) for w in ws], decimals=2,
        note=f"El estado estable no es un número, es una banda cuyo ancho depende de la ventana: con 5 s el indicador oscila ±{n(3 * r['estado estable'][ws[0]]['desv'] * 100, 1)} puntos con 3 desviaciones y con 120 s solo ±{n(3 * r['estado estable'][ws[4]]['desv'] * 100, 1)}. Una ventana larga mide mejor y tarda más en abortar. La media de {n(r['sli base'] * 100, 1)} % y la dispersión salen de {n(r['ventanas'][ws[0]])} ventanas de 5 s.",
        note_kind="gold", foot=SINT)


def se505_falsas() -> Fig:
    r = e505_estado_estable()["reglas"]
    ws = list(r)
    keys = [("falsa «menor que la media»", "Menor que la media", "coral"), ("falsa «menor que media menos 3 desv»", "Menor que media − 3 desviaciones", "teal"), ("falsa «menor que el SLO de 0,96»", "Menor que el SLO de 96 %", "gold")]
    return line_chart(
        "Refutaciones falsas: con el sistema sano, cuántas ventanas hacen «fallar» la hipótesis según la regla",
        "Líneas con el porcentaje de ventanas de un sistema sano que una regla declara refutadas según la longitud de la ventana: «menor que la media» refuta alrededor de la mitad de las ventanas con cualquier longitud; «menor que la media menos tres desviaciones» refuta menos de 1 por ciento; «menor que el SLO de 96 por ciento» refuta 29 por ciento con 5 segundos y 0 con 120.",
        [(lab, [(int(w), r[w][k] * 100, n(r[w][k] * 100, 1), "t") for w in ws], kind) for k, lab, kind in keys],
        x_label="Ventana de medición (s)", y_label="Ventanas sanas refutadas (%)", x_ticks=[(int(w), str(w)) for w in ws], decimals=1,
        note="Una regla sin banda refuta la mitad de las veces por pura mala suerte y destruye la confianza en el experimento. Una regla con la banda medida casi nunca. Un umbral de SLO sirve con ventanas largas y es ruidoso con cortas, porque su distancia a la media es menor que el ruido. Las 24 ejecuciones de 240 s con 0,4 % de errores de fondo y cola larga son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se505_potencia() -> Fig:
    r = e505_estado_estable()["reglas"]
    ws = list(r)
    return line_chart(
        "Detectar un efecto pequeño (4 ms más en una dependencia de 40 ms): ventanas con la regla de banda frente al umbral de SLO",
        "Líneas con el porcentaje de ventanas con el efecto que la regla declara refutadas: con la regla de banda de tres desviaciones sube de 2 por ciento con 5 segundos a 75 con 120; con el umbral de SLO de 96 por ciento sube de 53 a 79, pero también refuta ventanas sanas.",
        [("Regla de banda (media − 3 desviaciones)", [(int(w), r[w]["detecta «menor que media menos 3 desv»"] * 100, n(r[w]["detecta «menor que media menos 3 desv»"] * 100, 0), "t") for w in ws], "teal"),
         ("Umbral de SLO de 96 %", [(int(w), r[w]["detecta «menor que el SLO de 0,96»"] * 100, n(r[w]["detecta «menor que el SLO de 0,96»"] * 100, 0), "b") for w in ws], "gold")],
        x_label="Ventana de medición (s)", y_label="Ventanas con efecto refutadas (%)", x_ticks=[(int(w), str(w)) for w in ws], decimals=0, y_ticks=[0, 25, 50, 75, 100],
        note="Un efecto real de 4 ms mueve el indicador solo 0,6 puntos: para verlo sin falsas alarmas hacen falta ventanas de dos minutos o varias repeticiones. Un experimento que no puede detectar el efecto que busca no confirma la hipótesis, solo no la contradice. El umbral de SLO parece detectar más, pero lo logra porque el indicador sano ya está pegado a él.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-506
def se506_detectar() -> Fig:
    r = e506_radio()
    rows = r["filas"]
    return line_chart(
        "Radio de explosión y capacidad de ver el efecto: un 5 % de errores inyectado durante un minuto",
        "Línea con el porcentaje de repeticiones en que una prueba entre el grupo experimental y el de control detecta el efecto según la fracción de tráfico afectada: 72 por ciento con 0,5 por ciento del tráfico, 95 con 1, 100 con 2 por ciento o más.",
        [("Repeticiones en que se detecta el efecto", [(x["fracción"] * 100, x["detecta"] * 100, n(x["detecta"] * 100, 0), "t") for x in rows], "teal")],
        x_label="Fracción del tráfico afectada (%)", y_label="Detección (%)", log_x=True, y_zero=True, decimals=0,
        x_ticks=[(x["fracción"] * 100, n(x["fracción"] * 100, 1)) for x in rows], y_ticks=[0, 25, 50, 75, 100],
        note="Un radio mínimo basta para ver un efecto grande, pero no uno pequeño: con 0,5 % del tráfico (unas 270 peticiones por minuto en el grupo) se pierde 1 de cada 4 repeticiones. La prueba compara el grupo con el control de la misma ejecución, que absorbe las variaciones comunes del tráfico. 60 repeticiones por fracción con 90 peticiones por segundo son supuestos del autor.",
        note_kind="teal", foot=SINT)


def se506_dano() -> Fig:
    r = e506_radio()
    rows = r["filas"]
    return grouped_bars(
        "Peticiones de personas que fallan por culpa del experimento en un minuto, según el radio",
        "Barras con las peticiones falladas por el experimento durante un minuto: 1,3 con 0,5 por ciento del tráfico, 5,4 con 2, 13,6 con 5, 27,8 con 10, 68,5 con 25 y 138,5 con 50; el daño crece en proporción al radio.",
        [n(x["fracción"] * 100, 1) + " %" for x in rows],
        [("Peticiones falladas por el experimento", [x["peticiones falladas"] for x in rows], "coral")],
        unit="Peticiones falladas (media de 60 repeticiones)", decimals=1,
        note="El daño es lineal en el radio y la detección no: pasar de 2 % a 50 % multiplica el daño por 25 y no mejora la detección, que ya era total. El radio razonable es el menor que detecta el efecto buscado con la potencia exigida. El 5 % de errores sobre un tráfico de 90 peticiones por segundo es un supuesto del autor.",
        note_kind="gold", foot=SINT)


def se506_aborto() -> Fig:
    r = e506_radio()["aborto"]
    fr = list(r)
    names = ["sin aborto", "SLO global", "grupo experimental", "presupuesto de 300 peticiones"]
    label = {"sin aborto": "Sin aborto", "SLO global": "Aborto por el SLO global", "grupo experimental": "Aborto por el grupo experimental", "presupuesto de 300 peticiones": "Aborto por presupuesto de 300 peticiones"}
    cols = {"sin aborto": "coral", "SLO global": "gold", "grupo experimental": "teal", "presupuesto de 300 peticiones": "grey"}
    return grouped_bars(
        "Una falla que empeora a los 60 s (de 20 % a 100 % de errores): peticiones dañadas según la condición de aborto y el radio",
        "Barras con las peticiones dañadas en un experimento de cinco minutos que empeora a los 60 segundos, según el radio y la condición de aborto: con 0,5 por ciento ninguna condición se activa y se dañan 104; con 2 por ciento, el SLO global y el grupo abortan a los 65 segundos y dañan 34 frente a 420; con 10 por ciento el SLO global aborta a los 10 segundos por culpa de la propia falla del 20 por ciento.",
        [n(float(f) * 100, 1) + " % del tráfico" for f in fr],
        [(label[k], [r[f][k]["peticiones dañadas"] for f in fr], cols[k]) for k in names],
        unit="Peticiones dañadas", log=True, decimals=0,
        note="Con radio pequeño ninguna condición global ve nada: el SLO global tolera hasta 1 % de error y 0,5 % del tráfico no llega a rozarlo. Con radio mayor el SLO global aborta antes de tiempo, porque el experimento ya lo consume desde el primer segundo. La condición que aísla al grupo experimental es la única que decide bien en los dos casos; con 0,5 % tampoco se activa, porque no hay peticiones suficientes en 10 s.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-508
def se508_firmas() -> Fig:
    r = e508_firmas()
    base = r["base"]
    rows = r["filas"]
    names = list(rows)

    def level(v, b, lo, hi):
        if v is None:
            return 3
        d = v / b if b else v
        return 2 if d >= hi else (1 if d >= lo else 0)

    cells = []
    for nm in names:
        s = rows[nm]
        cells.append([
            (2 if s["tasa de error"] >= 0.2 else (1 if s["tasa de error"] >= 0.01 else 0)),
            level(s["p99 ms"], base["p99 ms"], 1.3, 2.5),
            level(s["intentos por petición"], base["intentos por petición"], 1.2, 2.0),
            level(s["utilización"], base["utilización"], 1.2, 1.6),
        ])
    return heatmap(
        "Qué señal mueve cada tipo de falla: la huella que deja en cuatro señales del cliente y del servicio",
        "Mapa de calor con el tamaño del cambio de cuatro señales frente a la línea base para seis fallas: la latencia de red solo mueve el p99; la falta de respuesta mueve los errores, los intentos y el p99 pero no la utilización; los errores de la dependencia mueven los intentos; la pérdida de hilos y la lentitud suben utilización, intentos y errores; la caída de un proceso se parece a la lentitud en la huella.",
        [nm for nm in names], ["Tasa de error", "p99 de las correctas", "Intentos por petición", "Utilización del servidor"],
        [[float(v) for v in row] for row in cells], unit="Cambio frente a la línea base (0 ninguno, 1 moderado, 2 grande, 3 sin datos)", scale="coral", vmin=0, vmax=3, decimals=0,
        cell_fmt=lambda v: ["no se mueve", "moderado", "grande", "sin datos"][int(round(v))], label_w=270,
        note="Dos fallas distintas pueden dejar la misma huella: la lentitud de la dependencia y la caída de un proceso suben las mismas señales, y solo el reinicio o el tiempo las separa. La huella decide qué observar antes de inyectar y evita atribuir a la red lo que es saturación. Umbrales de 1,3 y 2,5 veces (p99), 1,2 y 2 (intentos) y 1,2 y 1,6 (utilización) son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se508_reloj() -> Fig:
    r = e508_reloj()["celdas"]
    skews = [0, 5, 30, 60, 120, 300]
    return line_chart(
        "Desfase de reloj en un validador de tokens de 300 s: peticiones rechazadas según el desfase y la tolerancia",
        "Líneas con el porcentaje de tokens válidos que un validador adelantado rechaza según el desfase: sin tolerancia, 1,6 por ciento con 5 segundos, 10 con 30, 20 con 60 y 40 con 120; con tolerancia de 30 segundos no rechaza nada hasta 30 de desfase y 10 con 60; con 60 segundos de tolerancia no rechaza hasta 60.",
        [("Sin tolerancia", [(s, r[f"0|{s}"]["adelantado"] * 100, n(r[f"0|{s}"]["adelantado"] * 100, 1), "t") for s in skews], "coral"),
         ("Tolerancia de 30 s", [(s, r[f"30|{s}"]["adelantado"] * 100, n(r[f"30|{s}"]["adelantado"] * 100, 1), "t") for s in skews], "gold"),
         ("Tolerancia de 60 s", [(s, r[f"60|{s}"]["adelantado"] * 100, n(r[f"60|{s}"]["adelantado"] * 100, 1), "b") for s in skews], "teal")],
        x_label="Desfase del reloj del validador (s)", y_label="Tokens válidos rechazados (%)", x_ticks=[(s, str(s)) for s in skews], decimals=1, point_labels="none",
        note="La fracción rechazada es (desfase − tolerancia) / duración del token: lineal y sin umbral de aviso, de modo que un desfase pequeño falla un poco y nadie lo investiga. El reloj atrasado produce el mismo número por la causa opuesta (tokens «emitidos en el futuro»). 100 000 tokens con edades uniformes son un supuesto del autor.",
        note_kind="gold", foot=SINT)


def se508_disco() -> Fig:
    r = e508_disco()
    cats = ["Registro síncrono", "Búfer de 50 líneas", "Búfer de 200 líneas", "Búfer de 1 000 líneas"]
    asy = r["asincrono"]
    lines = asy[50]["líneas"]
    return grouped_bars(
        "Un disco que se detiene 2 s: el registro síncrono bloquea peticiones durante 10 s y el asíncrono pierde líneas",
        f"Barras con el porcentaje de peticiones que fallan en los 10 segundos siguientes al inicio de una parada de disco de 2 segundos y de líneas de registro que se pierden: el registro síncrono hace fallar {p(r['sincrono']['fallan'], 0)} de las peticiones y no pierde líneas; un búfer de 50 líneas no bloquea ninguna petición y pierde {p(asy[50]['líneas perdidas'] / lines, 0)}; con 200 o 1 000 no hay pérdida.",
        cats,
        [("Peticiones que fallan", [r["sincrono"]["fallan"] * 100, 0, 0, 0], "coral"), ("Líneas de registro perdidas", [0, asy[50]["líneas perdidas"] / lines * 100, asy[200]["líneas perdidas"] / lines * 100, asy[1000]["líneas perdidas"] / lines * 100], "gold")],
        unit="Porcentaje (%)", decimals=0,
        note="El disco no falla igual según quién espere por él: si la ruta de la petición escribe y sincroniza, la parada del disco es una parada del servicio; si escribe en un búfer, es una pérdida acotada de evidencia justo cuando más se necesita. La elección es de diseño y se prueba inyectándola. 90 peticiones por segundo y 2 s de parada son supuestos del autor.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-509
def se509_latencia() -> Fig:
    r = MEDIDO_509
    names = list(r["filas"])
    return grouped_bars(
        "Un cliente con espera de 300 ms contra un servicio local a través de un proxy que inyecta fallas: tiempo hasta el desenlace",
        "Barras horizontales con la mediana del tiempo hasta el desenlace en milisegundos de 30 peticiones reales por escenario: unos 11 sin tóxico, 61 con 50 de latencia, 211 con 200, 311 con 400 porque la espera se agota a los 300, 10 con el reinicio de conexión y 311 con el silencio; los éxitos son 30 de 30 hasta 200 milisegundos de latencia y 0 de 30 en los otros tres.",
        [f"{nm} ({r['filas'][nm]['exitos']} de {r['n']})" for nm in names],
        [("Mediana (ms)", [r["filas"][nm]["mediana ms"] for nm in names], "teal"), ("Percentil 95 (ms)", [r["filas"][nm]["p95 ms"] for nm in names], "gold")],
        unit="Milisegundos", horizontal=True, decimals=0, label_w=300, ref_lines=[(300, "espera de 300 ms")],
        note="El reinicio falla rápido y el silencio falla lento: el silencio cuesta una espera completa por petición, y por eso es la falla que más recursos retiene. Un tóxico de latencia de 400 ms equivale desde el cliente a un silencio. El proxy sin tóxico añade menos de 1 ms a la mediana directa (10,4 ms). Una máquina, 30 peticiones secuenciales.",
        note_kind="gold", foot=REAL)


def se509_donde() -> Fig:
    f = Fig(940, 400, "Dónde se inyecta la falla: un proxy entre el cliente y el servicio deja intactos el código de ambos",
            "Diagrama con el cliente que mide a la izquierda, un proxy en el centro con tres tóxicos aplicados a la dirección de respuesta (latencia, reinicio de conexión y silencio) y el servicio local a la derecha; abajo, un panel de control que activa y retira los tóxicos y un registro con lo que mide el cliente.")
    f.box(10, 40, 200, 90, "Cliente de la API\nespera 300 ms, sin reintentos", "plain", 14, bold=True)
    f.group(250, 14, 440, 160, "Proxy (el mecanismo de Toxiproxy)", "teal")
    f.box(268, 50, 120, 60, "Latencia\nretrasa los datos", "gold", 13)
    f.box(398, 50, 120, 60, "Reinicio\ncierra al instante", "coral", 13)
    f.box(528, 50, 144, 60, "Silencio\nretiene y descarta", "coral", 13)
    f.box(268, 120, 404, 44, "Sin tóxico: reenvía bytes y añade menos de 1 ms", "grey", 13)
    f.box(730, 40, 200, 90, "Servicio local\nresponde «ok» en 10 ms", "plain", 14, bold=True)
    f.arrow([(210, 70), (250, 70)])
    f.arrow([(690, 70), (730, 70)])
    f.arrow([(250, 105), (210, 105)], dashed=True)
    f.box(250, 210, 440, 60, "Panel de control: activa un tóxico, lo retira y cuenta cada experimento", "navy", 14, bold=True)
    f.arrow([(470, 210), (470, 176)], "activar y retirar", label_at=(560, 198))
    f.box(10, 300, 440, 70, "Lo que se mide: éxitos y tiempo hasta el desenlace en el cliente, nunca el código del servicio", "plain", 13)
    f.box(480, 300, 450, 70, "Lo que NO ve: fallas dentro del servicio (hilos, disco, memoria). Esas se inyectan en el nodo, no en el cable", "coral", 13)
    f.text(470, 392, REAL, 12, "middle", 400, "#5c1f14")
    return f


def se509_capas() -> Fig:
    f = Fig(940, 430, "Qué capa toca cada herramienta: del cable al proceso y a la nube",
            "Diagrama de cuatro capas de abajo arriba: proceso o instancia (Chaos Monkey termina instancias), red (Toxiproxy y NetworkChaos actúan sobre conexiones), nodo y contenedor (Chaos Mesh y LitmusChaos inyectan estrés, ficheros, tiempo y pods) y servicio de nube (AWS Fault Injection Service y Azure Chaos Studio actúan sobre recursos de la nube con condiciones de parada).")
    layers = [
        (14, "Servicio de nube", "Actúa sobre recursos del proveedor: AWS Fault Injection Service (acciones, objetivos, condiciones de parada) y Azure Chaos Studio", "navy"),
        (110, "Orquestador (Kubernetes)", "Chaos Mesh y LitmusChaos declaran el experimento como recurso: PodChaos, NetworkChaos, StressChaos, IOChaos, TimeChaos, DNSChaos", "teal"),
        (206, "Red y conexión", "Toxiproxy: proxy TCP con tóxicos (latencia, ancho de banda, timeout, reset_peer, packet_loss) controlado por una API HTTP", "gold"),
        (302, "Instancia o proceso", "Chaos Monkey: termina instancias y contenedores al azar en producción; requiere Spinnaker", "coral"),
    ]
    for y, head, body, kind in layers:
        f.box(10, y, 190, 80, head, kind, 14, bold=True)
        f.box(210, y, 720, 80, body, "plain", 13, align="start")
    f.arrow([(105, 396), (105, 382)])
    f.text(470, 416, "De arriba abajo crece el control fino sobre un componente y cae el alcance sobre la plataforma.", 13, "middle", 400, "#142231")
    return f



# ---------------------------------------------------------------- SE-510
def se510_replicacion() -> Fig:
    r = e510_replicacion()
    names = list(r["pérdida"])
    return grouped_bars(
        "Escrituras confirmadas que se pierden al caer el primario con replicación asíncrona (200 escrituras por segundo)",
        "Barras con las escrituras confirmadas que no estaban en la réplica al conmutar: media 4,3 con retraso típico de 20 milisegundos, 7,8 con 1 por ciento de picos de 2 segundos y 65,4 con 5 por ciento de picos de hasta 10 segundos; el percentil 99 es 15, 25 y 2 000.",
        ["Retraso típico (mediana de 20 ms)", "1 % de picos de 2 s", "5 % de picos de 2 s o 10 s"],
        [("Media", [r["pérdida"][k]["media"] for k in names], "teal"), ("Percentil 99", [r["pérdida"][k]["p99"] for k in names], "gold"), ("Máximo", [r["pérdida"][k]["máx"] for k in names], "coral")],
        unit="Escrituras confirmadas perdidas por conmutación", log=True, decimals=0,
        note=f"Con replicación síncrona la pérdida es 0, a cambio de {r['latencia añadida ms']['síncrona entre regiones']} ms por escritura entre regiones. La media engaña: el percentil 99 con picos de 10 s es 2 000 escrituras. El caso que importa es el pico, y solo se ve provocándolo. {n(r['n'])} conmutaciones por escenario y la distribución del retraso son supuestos del autor.",
        note_kind="coral", foot=SINT)


def se510_lecturas() -> Fig:
    r = e510_replicacion()["lecturas obsoletas"]
    ks = list(r)
    return line_chart(
        "Leer de una réplica justo después de escribir: fracción de lecturas obsoletas según el retraso de replicación",
        "Línea con el porcentaje de lecturas que ven datos anteriores a la escritura de la misma persona según el retraso de la réplica: 10 por ciento con 5 milisegundos, 35 con 20, 85 con 100 y 99,9 con 500.",
        [("Lecturas obsoletas", [(k, r[k] * 100, n(r[k] * 100, 0), "t") for k in ks], "teal")],
        x_label="Retraso de replicación (ms, escala logarítmica)", y_label="Lecturas obsoletas (%)", log_x=True, x_ticks=[(k, str(k)) for k in ks], decimals=0, y_ticks=[0, 25, 50, 75, 100],
        note="Una réplica sana con 20 ms de retraso devuelve datos viejos a más de uno de cada tres lectores que leen dentro de 50 ms de su propia escritura. Es consistencia eventual en vigor, no una falla, y solo una prueba con retraso inyectado la distingue de un defecto. El tiempo entre escritura y lectura (media de 50 ms) es un supuesto del autor.",
        note_kind="gold", foot=SINT)


def se510_modelo() -> Fig:
    r = e510_ml()
    fr = list(r["filas"])
    return line_chart(
        "Un modelo con el almacén de características degradado: exactitud según la fracción de peticiones afectadas y la política",
        f"Líneas con la exactitud del modelo según la fracción de peticiones con las dos características más informativas ausentes: con valor por omisión baja de {p(r['exactitud sana'], 1)} a {p(r['filas'][0.5]['valor por omisión'], 1)} con la mitad afectada, con valores obsoletos a {p(r['filas'][0.5]['valor obsoleto'], 1)} y con una regla de reserva a {p(r['filas'][0.5]['reserva con regla'], 1)}.",
        [("Valor por omisión", [(f * 100, r["filas"][f]["valor por omisión"] * 100, n(r["filas"][f]["valor por omisión"] * 100, 1), "b") for f in fr], "coral"),
         ("Valor obsoleto", [(f * 100, r["filas"][f]["valor obsoleto"] * 100, n(r["filas"][f]["valor obsoleto"] * 100, 1), "b") for f in fr], "gold"),
         ("Regla de reserva", [(f * 100, r["filas"][f]["reserva con regla"] * 100, n(r["filas"][f]["reserva con regla"] * 100, 1), "t") for f in fr], "teal")],
        x_label="Peticiones con características ausentes (%)", y_label="Exactitud (%)", x_ticks=[(f * 100, n(f * 100, 0)) for f in fr], decimals=1, y_zero=False, hlines=[(r["exactitud de la regla"] * 100, "exactitud de la regla sola")],
        note="La falla es silenciosa: no hay error ni latencia, solo respuestas peores. Un valor obsoleto es el peor de los tres porque parece válido. La regla de reserva, más simple que el modelo, pierde menos que ambas con la mitad afectada. La muestra de 4 000 peticiones y el modelo logístico de 6 características son sintéticos.",
        note_kind="coral", foot=SINT)


FIGURES = {
    "se-505-ruido-segun-la-ventana.svg": se505_ruido,
    "se-505-refutaciones-falsas.svg": se505_falsas,
    "se-505-detectar-un-efecto-pequeno.svg": se505_potencia,
    "se-506-detectar-con-un-radio-pequeno.svg": se506_detectar,
    "se-506-dano-segun-el-radio.svg": se506_dano,
    "se-506-condiciones-de-aborto.svg": se506_aborto,
    "se-507-cinco-clientes-seis-fallas.svg": se507_matriz,
    "se-507-fallo-que-no-se-recupera.svg": se507_recuperacion,
    "se-507-intentos-por-peticion.svg": se507_amplificacion,
    "se-508-huella-de-cada-falla.svg": se508_firmas,
    "se-508-desfase-de-reloj.svg": se508_reloj,
    "se-508-disco-detenido.svg": se508_disco,
    "se-509-latencia-medida-con-el-proxy.svg": se509_latencia,
    "se-509-donde-se-inyecta-la-falla.svg": se509_donde,
    "se-509-capas-de-las-herramientas.svg": se509_capas,
    "se-510-escrituras-perdidas-al-conmutar.svg": se510_replicacion,
    "se-510-lecturas-obsoletas.svg": se510_lecturas,
    "se-510-modelo-con-caracteristicas-degradadas.svg": se510_modelo,
}
