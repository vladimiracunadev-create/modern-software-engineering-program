"""Figures for SE-512 to SE-516 (chaos in CI/CD, data and ML, scale, security, ethics and integration; simulated time with fixed seeds)."""
from __future__ import annotations

from experiments_part42_b import (
    e511_programa, e512_ci, e513_equidad, e513_presupuesto, e514_evidencia, e514_revocacion, e515_concentracion, e515_region, e516_integrado, e516_validador,
)
from figure_kit import Fig, grouped_bars, heatmap, line_chart, timeline

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."


def n(x: float, d: int = 0) -> str:
    """Formato español: espacio como separador de miles y coma decimal."""
    return f"{x:,.{d}f}".replace(",", "§").replace(".", ",").replace("§", " ")


def p(x: float, d: int = 1) -> str:
    return n(100 * x, d) + " %"


# ---------------------------------------------------------------- SE-512
def se512_regresiones() -> Fig:
    r = e512_ci()
    regs = list(r["regresiones"])
    scen = r["escenarios"]
    short = ["30 % de errores", "Lenta +100 ms", "Mitad de hilos", "Sin respuesta"]
    return heatmap(
        "Siete cambios de configuración frente a cuatro escenarios de falla: en cuántas de 8 ejecuciones el escenario revela el cambio",
        "Mapa de calor con el porcentaje de ejecuciones en que cada escenario hace fallar la configuración modificada: quitar el cortacircuitos o la alternativa se ve en los cuatro escenarios; los reintentos sin pausa solo con la dependencia lenta y sin respuesta; quitar la espera corta, cinco reintentos y el cortacircuitos sensible no se ven en ninguno; el cambio inocuo de un reintento menos no falla en ninguno.",
        [x for x in regs], short, [[r["regresiones"][rg][s] * 100 for s in scen] for rg in regs],
        unit="Ejecuciones en que el escenario falla (%)", scale="coral", vmin=0, vmax=100, decimals=0, suffix=" %", label_w=330,
        note=f"Tres de seis regresiones dañinas no las ve ninguno de los cuatro escenarios, y la configuración sana no falla en ninguna de las {r['semillas']} ejecuciones de cada escenario. Un escenario solo ve el cambio que sabe expresar: el cortacircuitos sensible solo falla si se mide la calidad completa, no la respuesta. Ejecuciones de 60 s con 90 peticiones por segundo son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se512_cobertura() -> Fig:
    r = e512_ci()
    harmful = [x for x in r["regresiones"] if not x.startswith("R7")]
    static = {x for x in harmful if r["estatico"][x]}
    dyn = {x for x in harmful if r["cobertura"][4][x]}
    both = static | dyn
    cats = ["Solo lectura estática de la configuración", "Solo suite de 1 escenario (30 % de errores)", "Solo suite de 2 escenarios", "Solo suite de 4 escenarios", "Lectura estática y suite de 4 escenarios"]
    vals = [len(static), sum(1 for x in harmful if r["cobertura"][1][x]), sum(1 for x in harmful if r["cobertura"][2][x]), len(dyn), len(both)]
    return grouped_bars(
        "Qué regresiones dañinas detecta cada defensa: seis cambios que empeoran la resiliencia",
        f"Barras horizontales con las regresiones dañinas detectadas de seis: la lectura estática de la configuración detecta {vals[0]}, una suite de un escenario {vals[1]}, dos escenarios {vals[2]}, cuatro escenarios {vals[3]} y la combinación de lectura estática y cuatro escenarios {vals[4]}; el cortacircuitos sensible no lo detecta ninguna.",
        cats, [("Regresiones detectadas", vals, "teal")], unit="Regresiones detectadas (de 6)", horizontal=True, decimals=0, label_w=320, ref_lines=[(6, "6")],
        note="Las dos defensas fallan en lugares distintos: la lectura estática ve lo que está escrito (esperas, reintentos sin pausa, ausencia de cortacircuitos) y no juzga umbrales; la suite ve el comportamiento y solo el que sus escenarios expresan. El cambio R5 escapa a ambas y por eso la calidad completa debe ser parte del criterio. Cada escenario cuesta 1 minuto de ejecución en el modelo.",
        note_kind="coral", foot=SINT)


def se512_pipeline() -> Fig:
    f = Fig(940, 420, "Dónde cabe el caos en el camino a producción: cada etapa responde una pregunta distinta y cuesta distinto",
            "Diagrama con seis etapas de izquierda a derecha: lectura estática de la configuración en cada commit, pruebas de integración con un proxy de fallas en el pipeline, preproducción con tráfico sintético y fallas de plataforma, canario en producción con grupo experimental y control, producción con experimentos continuos y día de práctica; debajo, el costo y el riesgo crecen y el realismo también.")
    stages = [
        ("Commit", "Lee la configuración: esperas, reintentos, cortacircuitos", "grey", "segundos"),
        ("Pipeline", "Servicio local y proxy: latencia, reinicio, silencio", "teal", "1-5 min"),
        ("Preproducción", "Tráfico sintético y fallas de plataforma", "gold", "10-60 min"),
        ("Canario", "5 % del tráfico: grupo experimental y control", "coral", "30-60 min"),
        ("Producción", "Experimentos continuos con aborto y día de práctica", "navy", "continuo"),
    ]
    x = 10
    for i, (name, body, kind, cost) in enumerate(stages):
        f.box(x, 20, 172, 40, name, kind, 14, bold=True)
        f.box(x, 66, 172, 120, body, "plain", 13)
        f.box(x, 194, 172, 34, cost, "grey", 13)
        if i:
            f.arrow([(x - 8, 40), (x + 2, 40)])
        x += 184
    f.arrow([(10, 270), (920, 270)], "más realismo, más riesgo y más coste", label_at=(470, 258))
    f.box(10, 292, 440, 60, "Pregunta de las etapas tempranas: ¿está escrita la protección?", "teal", 13)
    f.box(480, 292, 450, 60, "Pregunta de las etapas tardías: ¿funciona con el tráfico y las dependencias reales?", "coral", 13)
    f.box(10, 366, 920, 40, "Ninguna etapa sustituye a las demás: cada una atrapa regresiones que las otras no ven.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-515
def se515_region() -> Fig:
    r = e515_region()["celdas"]
    regions = [2, 3, 4, 6]
    utils = [0.4, 0.55, 0.7, 0.85]
    return heatmap(
        "Evacuar una región: peticiones correctas en las regiones que sobreviven según el número de regiones y la utilización previa",
        "Mapa de calor con el porcentaje de peticiones correctas tras evacuar una región: con dos regiones solo aguanta 40 por ciento de utilización previa; con tres, hasta 55; con cuatro, hasta 55 y falla en parte con 70; con seis aguanta hasta 70; con 85 por ciento de utilización previa ninguna configuración aguanta.",
        [f"{k} regiones" for k in regions], [f"{n(u * 100)} % de utilización" for u in utils],
        [[r[f"{k}|{u}"]["ok"] * 100 for u in utils] for k in regions], unit="Peticiones correctas (%)", scale="teal", vmin=0, vmax=100, decimals=0, suffix=" %", label_w=170,
        note="La carga que absorben las demás es u·R/(R−1): con dos regiones se duplica y con seis sube 20 %. Sobre 100 % de utilización la cola crece sin límite y las esperas agotadas lo agravan. Evacuar una región sin saber esto es una caída causada por uno mismo. La capacidad de 200 peticiones por segundo por región y las repeticiones de 60 s son supuestos del autor.",
        note_kind="coral", foot=SINT)


def se515_concentracion() -> Fig:
    r = e515_concentracion()["filas"]
    names = list(r)
    xs = [x["fracción"] * 100 for x in r[names[0]]]
    return line_chart(
        "La misma lentitud de 300 ms, repartida de forma difusa o concentrada: peticiones correctas según la fracción de peticiones lentas",
        "Líneas con el porcentaje de peticiones correctas según la fracción de peticiones con 300 milisegundos más de lentitud: sin protección baja de forma gradual hasta 26 por ciento; con reintentos sin pausa se mantiene en 100 hasta 10 por ciento de peticiones lentas y cae a 0 desde 20; con cortacircuitos calibrado la respuesta completa cae a 44 por ciento con 5 y a 12 con 10, y las respuestas completas o con alternativa se mantienen en 100.",
        [("Sin protección (A)", [(x["fracción"] * 100, x["ok"] * 100, "", "t") for x in r["sin protección"]], "gold"),
         ("Reintentos sin pausa (B)", [(x["fracción"] * 100, x["ok"] * 100, "", "t") for x in r["reintentos sin pausa"]], "coral"),
         ("Cortacircuitos calibrado (E): respuesta completa", [(x["fracción"] * 100, x["ok"] * 100, "", "t") for x in r["con cortacircuitos calibrado"]], "teal"),
         ("Cortacircuitos calibrado (E): completa o alternativa", [(x["fracción"] * 100, x["responde"] * 100, "", "t") for x in r["con cortacircuitos calibrado"]], "grey")],
        x_label="Peticiones lentas (%)", y_label="Peticiones respondidas (%)", x_ticks=[(x, n(x, 0)) for x in xs], decimals=0, point_labels="none", y_ticks=[0, 25, 50, 75, 100],
        note="Hay un umbral de concentración: con 5 % de peticiones lentas el servicio parece sano para A y B, y con 20 % B colapsa porque cada reintento retiene un hilo 340 ms. El cortacircuitos cambia calidad por supervivencia: responde siempre, pero abre antes y sirve la alternativa. Un experimento difuso confirmaría la hipótesis y no probaría nada sobre la escala. El servicio de 8 hilos y 40 ms es un supuesto del autor.",
        note_kind="gold", foot=SINT)


def se515_control() -> Fig:
    f = Fig(940, 410, "Un experimento en producción como una comparación: un 2 % de tráfico a un grupo de control y otro a un grupo experimental",
            "Diagrama con el tráfico real entrando por un enrutador que envía la mayor parte a la flota normal y dos porciones pequeñas a un grupo de control y a un grupo experimental; la falla se aplica solo al experimental; un comparador mide ambos grupos y un interruptor automático detiene el experimento si el grupo experimental se degrada más que un límite.")
    f.box(10, 150, 150, 70, "Tráfico real", "navy", 15, bold=True)
    f.box(210, 150, 150, 70, "Enrutador", "grey", 15, bold=True)
    f.box(430, 20, 220, 80, "Flota normal\n96 % del tráfico", "plain", 14)
    f.box(430, 130, 220, 90, "Grupo de control\n2 %, sin falla", "teal", 14)
    f.box(430, 250, 220, 90, "Grupo experimental\n2 %, con la falla", "coral", 14)
    f.arrow([(160, 185), (210, 185)])
    f.arrow([(360, 170), (430, 60)])
    f.arrow([(360, 185), (430, 175)])
    f.arrow([(360, 200), (430, 295)])
    f.box(720, 130, 210, 90, "Comparador\ncontrol frente a experimento", "gold", 14)
    f.arrow([(650, 175), (720, 175)])
    f.arrow([(650, 295), (685, 295), (685, 215), (720, 215)])
    f.box(720, 270, 210, 70, "Interruptor: detiene si se degrada más que el límite", "coral", 13)
    f.arrow([(825, 220), (825, 270)])
    f.arrow([(720, 305), (650, 305)], dashed=True)
    f.text(470, 372, "Modelo propio; el esquema de control, experimento e interruptor lo describe Netflix para su plataforma ChAP.", 13, "middle", 400, "#142231")
    f.text(470, 398, "Documentado por Netflix (2017); las proporciones del dibujo son ilustrativas.", 12, "middle", 400, "#5c1f14")
    return f


# ---------------------------------------------------------------- SE-514
def se514_ensayos() -> Fig:
    r = e514_evidencia()["tabla"]
    ns = [5, 20, 59, 200, 1000]
    ps = [0.9, 0.95, 0.99, 0.999]
    cols = ["coral", "gold", "teal", "grey"]
    return line_chart(
        "Un control que falla 1 vez de cada 20 (95 % de eficacia) pasa 59 ensayos seguidos solo un 5 % de las veces: probabilidad de que todos los ensayos salgan bien",
        "Líneas con la probabilidad de que todos los ensayos salgan bien según el número de ensayos y la eficacia real del control: con eficacia 90 por ciento llega a 0,2 por ciento con 59 ensayos; con 95 por ciento, a 4,8; con 99, a 55,3; con 99,9, a 94,3.",
        [(f"Eficacia real de {n(q * 100, 1)} %", [(k, r[f"{q}|{k}"] * 100, "", "t") for k in ns], cols[i]) for i, q in enumerate(ps)],
        x_label="Ensayos consecutivos (escala logarítmica)", y_label="Todos salen bien (%)", log_x=True, x_ticks=[(k, str(k)) for k in ns], y_ticks=[0, 25, 50, 75, 100], point_labels="none",
        vlines=[(59, "59")],
        note="Con 59 ensayos sin fallas se puede afirmar, con 95 % de confianza, que la tasa de fallas es inferior a 5 % (regla de tres: 3/59). Pocos ensayos no demuestran nada: con 5, un control que falla una de cada diez veces pasa en 59 % de los casos. Los ensayos son independientes e idénticos, un supuesto que los controles reales rara vez cumplen.",
        note_kind="gold", foot=SINT)


def se514_clasificacion() -> Fig:
    r = e514_evidencia()["clasificación"]
    ns = list(r)
    return grouped_bars(
        "Treinta controles de seguridad (12 con eficacia de 97 % o menos) clasificados con 5, 20, 59 y 200 ensayos cada uno",
        "Barras con el porcentaje de controles débiles que pasan todos los ensayos y de controles buenos que fallan algún ensayo: con 5 ensayos pasa 11 por ciento de los débiles y falla 0,4 de los buenos; con 20, 0,5 y 1,8; con 59, 0 y 6; con 200, 0 y 18.",
        [f"{k} ensayos por control" for k in ns],
        [("Controles débiles que pasan todos los ensayos (%)", [r[k]["controles débiles que pasan"] * 100 for k in ns], "coral"), ("Controles buenos que fallan algún ensayo (%)", [r[k]["controles buenos que fallan"] * 100 for k in ns], "gold")],
        unit="Porcentaje de controles (%)", decimals=1,
        note="Más ensayos eliminan los falsos aprobados y crean falsas alarmas: un control con 99,9 % de eficacia falla alguna vez en 200 ensayos con 18 % de probabilidad. La evidencia de cumplimiento necesita un criterio de aceptación con tolerancia y un procedimiento para repetir, no «cero fallas». Los 30 controles (18 de 99,9 %, 8 de 97 %, 4 de 80 %) son un supuesto del autor.",
        note_kind="teal", foot=SINT)


def se514_revocacion() -> Fig:
    r = e514_revocacion()["ttl"]
    ks = [t for t in r if t > 0]
    return line_chart(
        "Revocar una credencial cuando los clientes la guardan en caché: cuánto tiempo siguen autorizados según la vigencia de la caché",
        "Líneas con la exposición media y la del percentil 99 en segundos tras revocar según la vigencia de la caché: 15 y 30 segundos con 30; 30 y 59 con 60; 150 y 295 con 300; 456 y 892 con 900; sin caché la exposición es 0.",
        [("Exposición media", [(k, r[k]["exposición media s"], n(r[k]["exposición media s"], 0), "b") for k in ks], "teal"), ("Exposición del percentil 99", [(k, r[k]["exposición p99 s"], n(r[k]["exposición p99 s"], 0), "t") for k in ks], "coral")],
        x_label="Vigencia de la caché (s, escala logarítmica)", y_label="Segundos autorizados tras revocar (escala logarítmica)", log_x=True, log_y=True, x_ticks=[(k, str(k)) for k in ks], y_zero=False,
        note="La exposición máxima es la vigencia de la caché: lo que dice la política («acceso revocado de inmediato») y lo que ocurre difieren en segundos o minutos, y solo un experimento que revoque y mida lo muestra. 2 000 clientes con 0,5 peticiones por segundo y expiraciones uniformes son un supuesto del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-513
def se513_presupuesto() -> Fig:
    r = e513_presupuesto()
    names = list(r["politicas"])
    labels = ["Sin experimentos", "Calendario fijo: 4 al mes con radio de 50 %", "Con compuerta de presupuesto: radio de 5 %"]
    pol = r["politicas"]
    return grouped_bars(
        "Meses que incumplen un objetivo de 99,9 % (43,2 minutos de presupuesto) según la política de experimentos",
        f"Barras con el porcentaje de meses que incumplen el objetivo y los minutos medios gastados en experimentos: {p(pol[names[0]]['meses que incumplen'])} sin experimentos y 0 minutos, {p(pol[names[1]]['meses que incumplen'])} con cuatro experimentos fijos al mes con radio de 50 por ciento y {n(pol[names[1]]['gasto medio en experimentos'], 1)} minutos, y {p(pol[names[2]]['meses que incumplen'])} con compuerta de presupuesto y radio de 5 por ciento y {n(pol[names[2]]['gasto medio en experimentos'], 1)} minutos.",
        labels, [("Meses que incumplen el objetivo (%)", [pol[k]["meses que incumplen"] * 100 for k in names], "coral"), ("Gasto medio en experimentos (min)", [pol[k]["gasto medio en experimentos"] for k in names], "teal")],
        unit="Porcentaje de meses o minutos", horizontal=True, decimals=1, label_w=320,
        note=f"El calendario fijo gasta {n(pol[names[1]]['gasto medio en experimentos'], 0)} de 43,2 minutos y más que duplica los meses que incumplen; la compuerta gasta {n(pol[names[2]]['gasto medio en experimentos'], 1)} y omite {n(pol[names[2]]['experimentos omitidos'], 1)} experimentos al mes cuando los incidentes ya consumieron la mitad del presupuesto. Los experimentos se pagan del mismo presupuesto que las personas usuarias. {n(r['meses'])} meses simulados y 1,2 incidentes por mes son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se513_equidad() -> Fig:
    r = e513_equidad()
    return grouped_bars(
        "Quién carga con el daño: elegir peticiones al azar frente a elegir clientes enteros (24 experimentos con radio de 5 %)",
        f"Barras con la fracción máxima de las peticiones de un cliente expuestas a la falla en algún experimento y con los clientes que nunca se afectan: elegir peticiones al azar expone 5 por ciento de las de cada cliente y a todos por igual; elegir clientes enteros hace que un cliente sufra 100 por ciento de sus peticiones en un experimento, que {r['por cliente']['máximo de veces que un cliente fue el afectado']:.0f} veces el mismo cliente sea el afectado y que {r['por cliente']['clientes nunca expuestos']} de 40 nunca lo sean.",
        ["Peticiones al azar", "Clientes enteros"],
        [("Peticiones de un cliente expuestas por experimento (%)", [r["por petición"]["fracción máxima de un cliente"] * 100, 100.0], "coral"), ("Clientes nunca afectados en los 24 experimentos", [0, r["por cliente"]["clientes nunca expuestos"]], "teal")],
        unit="Porcentaje o número de clientes", decimals=0,
        note=f"Elegir clientes enteros es más fácil de operar (un solo cliente, un solo dueño de la comunicación) y concentra el daño: el cliente afectado pierde todo mientras otros nunca participan, y el cliente más pequeño aporta {n(r['cuota del cliente más pequeño'] * 100, 1)} % del tráfico y puede no estar en la muestra. Equidad y representatividad pesan contra el costo de operación. 40 clientes con reparto 1/k son un supuesto del autor.",
        note_kind="gold", foot=SINT)


def se513_compuerta() -> Fig:
    f = Fig(940, 430, "Compuerta de decisión antes de inyectar: cinco preguntas, y cualquier «no» detiene el experimento",
            "Diagrama de decisión con cinco preguntas en cascada: la hipótesis es falsable y está escrita; el radio es el mínimo que detecta el efecto; hay condiciones de aborto automáticas y reversión probada; el presupuesto de error cubre el costo máximo con margen; las personas afectadas o sus representantes están informadas y hay una persona responsable disponible. Si todas son sí, se ejecuta; si alguna es no, se corrige o se pospone.")
    qs = [
        "1. ¿La hipótesis está escrita y puede refutarse?",
        "2. ¿El radio es el mínimo que detecta el efecto?",
        "3. ¿Hay aborto automático y la reversión se probó?",
        "4. ¿El presupuesto de error cubre el costo máximo?",
        "5. ¿Hay responsable disponible y se avisó a quien corresponde?",
    ]
    y = 16
    for i, q in enumerate(qs):
        f.box(10, y, 560, 54, q, "teal" if i % 2 == 0 else "plain", 14, align="start")
        f.box(590, y, 340, 54, "No: se corrige o se pospone", "coral", 13)
        f.arrow([(570, y + 27), (590, y + 27)])
        if i < 4:
            f.arrow([(290, y + 54), (290, y + 74)], "sí", label_at=(310, y + 69), label_anchor="start")
        y += 74
    f.box(10, 386, 560, 36, "Si todas son «sí»: se ejecuta con el aborto armado", "navy", 14, bold=True)
    f.arrow([(290, 370), (290, 386)])
    f.text(760, 410, "La compuerta es un registro: se guarda con la evidencia.", 13, "middle", 400, "#142231")
    return f


# ---------------------------------------------------------------- SE-516
def se516_validador() -> Fig:
    r = e516_validador()["detectadas"]
    names = list(r)
    return grouped_bars(
        "Un validador de especificaciones de experimento frente a 360 mutaciones de diez tipos: lo que ve por forma y lo que ve por contenido",
        "Barras horizontales con las mutaciones detectadas de 36 en cada tipo: un validador de forma detecta las 36 en quitar o vaciar un campo y 0 en las demás; un validador de contenido detecta además radio de 100 por ciento, duración de tres horas, aborto más laxo que el estado estable, umbral de 0,3 y reversión que no es una orden; ninguno detecta una métrica inexistente, una hipótesis no falsable ni una ventana en hora punta.",
        [k.capitalize() for k in names],
        [("Validador de forma", [r[k]["forma"] for k in names], "gold"), ("Validador de contenido", [r[k]["semántico"] for k in names], "teal")],
        unit="Mutaciones detectadas (de 36)", horizontal=True, decimals=0, label_w=330, ref_lines=[(36, "36")],
        note="Tres de diez tipos de error escapan a los dos validadores: nada en el documento dice si la métrica existe, si la hipótesis puede refutarse de verdad o si el calendario coincide con un cierre de plazo; eso lo dice una persona o un sistema que no está en el archivo. El validador detecta forma, no sabiduría.",
        note_kind="coral", foot=SINT)


def se516_resultados() -> Fig:
    r = e516_integrado()["resultados"]
    names = [x["experimento"] for x in r]
    return grouped_bars(
        "Cuatro experimentos de la especificación válida sobre el servicio de entregas con un grupo experimental de 5 %: respuestas correctas del grupo y del control",
        "Barras con el porcentaje de peticiones respondidas en el grupo experimental y en el de control durante cada experimento: 100 y 100 por ciento con 30 por ciento de errores, con dependencia lenta y con mitad de los hilos; con la regresión R3 (sin cortacircuitos) frente a la falta de respuesta el grupo cae a 2,5 por ciento y el control sigue en 100.",
        [x.capitalize() for x in names],
        [("Grupo experimental", [x["grupo"] * 100 for x in r], "coral"), ("Grupo de control", [x["control"] * 100 for x in r], "teal")],
        unit="Peticiones respondidas (%)", horizontal=True, decimals=1, label_w=300,
        note=f"Tres hipótesis confirmadas y una refutada con 81 peticiones en el grupo: el daño de la refutación es de unas 79 peticiones y el control demuestra que el resto del servicio no se enteró. Confirmar con 81 peticiones es una prueba débil: solo refutar es concluyente a este tamaño. Huella del conjunto de resultados: {e516_integrado()['huella']}.",
        note_kind="gold", foot=SINT)


def se516_ciclo() -> Fig:
    f = Fig(940, 400, "Ciclo de un programa de experimentos: cada vuelta deja evidencia y cada hallazgo vuelve como prueba de regresión",
            "Diagrama circular de seis pasos: elegir una hipótesis a partir de un riesgo, especificar el experimento y validarlo, ejecutar con aborto y comparación, registrar la evidencia con huella, corregir lo hallado, y repetir el experimento como regresión automatizada que alimenta la siguiente hipótesis.")
    items = [
        (30, 30, "Riesgo → hipótesis falsable", "teal"),
        (330, 30, "Especificación validada y aprobada", "plain"),
        (630, 30, "Ejecución con aborto y control", "coral"),
        (630, 230, "Evidencia con huella reproducible", "gold"),
        (330, 230, "Corrección del hallazgo", "plain"),
        (30, 230, "Regresión automatizada", "teal"),
    ]
    for x, y, t, k in items:
        f.box(x, y, 280, 80, t, k, 14, bold=True)
    f.arrow([(310, 70), (330, 70)])
    f.arrow([(610, 70), (630, 70)])
    f.arrow([(770, 110), (770, 230)])
    f.arrow([(630, 270), (610, 270)])
    f.arrow([(330, 270), (310, 270)])
    f.arrow([(170, 230), (170, 110)], "nuevo riesgo", label_at=(184, 176), label_anchor="start")
    f.box(10, 340, 920, 50, "Un programa es el conjunto de estos ciclos con dueños, calendario y presupuesto; un experimento aislado solo es una demostración.", "grey", 13)
    return f


# ---------------------------------------------------------------- SE-511
def se511_programas() -> Fig:
    r = e511_programa()["programas"]
    names = list(r)
    return grouped_bars(
        "Cuatro programas de práctica durante dos años: defectos latentes que quedan y defectos que se descubren en un incidente real",
        "Barras con los defectos latentes que quedan tras 24 meses y los incidentes reales que los descubren: sin práctica quedan 12,6 y hay 11,5 incidentes; un día al año deja 3,0 y 8,7; un día trimestral, 1,1 y 3,9; experimentos automáticos mensuales con un día semestral, 1,0 y 3,8.",
        ["Sin práctica", "Un día de práctica al año", "Un día de práctica por trimestre", "Experimentos automáticos mensuales y día semestral"],
        [("Defectos latentes al final", [r[k]["defectos latentes al final"] for k in names], "coral"), ("Incidentes reales que los descubren", [r[k]["incidentes reales"] for k in names], "gold")],
        unit="Defectos o incidentes en 24 meses (media de 300 simulaciones)", decimals=1, horizontal=True, label_w=300,
        note="Un día al año ataca el inventario acumulado, pero los defectos nuevos esperan hasta 12 meses; la frecuencia importa más que la intensidad. Pasar de trimestral a automático mensual apenas cambia lo que queda, porque los defectos de personas (alertas, runbooks, escalamiento) solo salen con personas. Entre 0 y 2 defectos nuevos por mes y 70 % de hallazgo por día de práctica son supuestos del autor.",
        note_kind="teal", foot=SINT)


def se511_edad() -> Fig:
    r = e511_programa()["programas"]
    names = list(r)
    return grouped_bars(
        "Meses que un defecto latente pasa escondido antes de salir a la luz, según el programa de práctica",
        "Barras con la edad media de un defecto cuando se descubre: 5,7 meses sin práctica, 5,0 con un día al año, 1,8 con un día por trimestre y 1,6 con experimentos automáticos mensuales y un día semestral.",
        ["Sin práctica", "Un día al año", "Un día por trimestre", "Automático mensual y día semestral"],
        [("Meses medios hasta descubrirse", [r[k]["meses medios de un defecto antes de salir"] for k in names], "teal")],
        unit="Meses", decimals=1,
        note="La edad media baja casi en proporción a la frecuencia, y cada mes escondido es un mes con un defecto que un incidente real puede activar a la peor hora. Sin práctica, el 100 % de los defectos que se descubren los encuentra una persona usuaria. Las tasas de entrada y de hallazgo son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se511_estructura() -> Fig:
    return timeline(
        "Estructura de un día de práctica de 3 horas: quién hace qué y cuándo se puede abortar",
        "Línea de tiempo en minutos con cuatro carriles: quien facilita, el equipo que responde, quien observa y la plataforma. Los primeros 30 minutos son de preparación y reglas, la inyección dura 60, el cierre y la retrospectiva ocupan 90 y hay una marca de aborto a los 75 minutos.",
        [("Quien facilita", [(0, 30, "Reglas", "navy"), (30, 90, "Inyecta y lleva el reloj", "gold"), (90, 180, "Retrospectiva", "teal")]),
         ("Equipo que responde", [(0, 30, "Briefing", "grey"), (30, 90, "Detecta, decide, repara", "coral"), (90, 180, "Hallazgos y acciones", "teal")]),
         ("Quien observa", [(0, 30, "Qué ver", "grey"), (30, 90, "Anota decisiones y tiempos", "gold"), (90, 180, "Línea de tiempo", "teal")]),
         ("Plataforma y condiciones", [(0, 30, "Verifica", "grey"), (30, 90, "Falla inyectada", "coral"), (90, 180, "Restaura y comprueba", "grey")])],
        unit="Minutos desde el inicio", events=[(30, "inicio de la falla"), (90, "fin")], ref_lines=[(75, "aborto si no hay control")], t_max=180, ticks=[0, 30, 60, 90, 120, 150, 180], lane_h=56, label_w=190,
        note="El orden importa más que la duración: sin briefing el equipo no sabe qué es de verdad, sin anotador no hay evidencia y sin retrospectiva la práctica solo cansa. Un día de práctica es un experimento sobre las personas y sus procedimientos, no solo sobre el sistema. Los tiempos son una plantilla, no una medición.",
        note_kind="gold", foot="Plantilla de práctica; no es una medición.")


FIGURES = {
    "se-511-programas-de-practica.svg": se511_programas,
    "se-511-edad-de-los-defectos.svg": se511_edad,
    "se-511-estructura-de-un-dia-de-practica.svg": se511_estructura,
    "se-512-regresiones-que-ve-cada-escenario.svg": se512_regresiones,
    "se-512-defensas-frente-a-regresiones.svg": se512_cobertura,
    "se-512-caos-en-el-camino-a-produccion.svg": se512_pipeline,
    "se-513-presupuesto-y-experimentos.svg": se513_presupuesto,
    "se-513-quien-carga-con-el-dano.svg": se513_equidad,
    "se-513-compuerta-de-decision.svg": se513_compuerta,
    "se-514-probabilidad-de-pasar-los-ensayos.svg": se514_ensayos,
    "se-514-controles-clasificados.svg": se514_clasificacion,
    "se-514-revocacion-y-cache.svg": se514_revocacion,
    "se-515-evacuar-una-region.svg": se515_region,
    "se-515-difuso-frente-a-concentrado.svg": se515_concentracion,
    "se-515-control-y-experimento-en-produccion.svg": se515_control,
    "se-516-validador-de-especificaciones.svg": se516_validador,
    "se-516-resultados-del-programa.svg": se516_resultados,
    "se-516-ciclo-del-programa.svg": se516_ciclo,
}
