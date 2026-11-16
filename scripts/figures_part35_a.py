"""Figures for SE-421 to SE-426 (synthetic data, fixed seeds, virtual time; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from experiments_part35_a import (
    e421_atribucion, e421_preguntas, e421_segmento, e422_correlacion, e422_formato, e422_politicas, e423_contadores, e423_histogramas,
    e424_contexto, e424_muestreo, e424_ruta_critica, e425_composicion, e425_donde_se_mide, e425_trafico, e426_reglas, e426_ruido, e426_ventanas,
)
from figure_kit import Fig, grouped_bars, heatmap, line_chart

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."
MEDIDO_35 = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); el valor de memoria depende de la versión del intérprete."



def _cap(text: str) -> str:
    return text[:1].upper() + text[1:]

def n(x: float, d: int = 0) -> str:
    """Formato español: espacio como separador de miles y coma decimal."""
    return f"{x:,.{d}f}".replace(",", "§").replace(".", ",").replace("§", " ")


def p(x: float, d: int = 1) -> str:
    return n(100 * x, d) + " %"


# ---------------------------------------------------------------- SE-421
def se421_localizar() -> Fig:
    r = e421_atribucion()
    h, total = r["aciertos"], r["incidentes"]
    return grouped_bars(
        "Localizar el componente lento en una cadena de cuatro servicios con cuatro conjuntos de señales",
        f"Barras horizontales con las localizaciones correctas de {total} incidentes sintéticos con un servicio lento: mirar solo el borde acierta {h['solo borde']}, el percentil 99 absoluto {h['p99 absoluto']}, el aumento relativo del percentil 99 frente a la línea base {h['aumento relativo']} y el mismo método sin ver uno de los cuatro servicios {h['aumento relativo sin un servicio']}.",
        ["Solo la latencia del borde", "p99 absoluto de cada servicio", "Aumento relativo del p99 frente a su línea base", "Aumento relativo con un servicio sin instrumentar"],
        [("Localizaciones correctas", [h["solo borde"], h["p99 absoluto"], h["aumento relativo"], h["aumento relativo sin un servicio"]], "teal")],
        unit=f"Localizaciones correctas (de {total})", horizontal=True, label_w=300, ref_lines=[(total, f"{total}")],
        note="Cada servicio informa su duración inclusiva (la suya más la de lo que llama). La línea base de 400 peticiones sanas y los factores de lentitud de 3 a 8 son supuestos del autor. Un punto ciego no apaga la alarma: la desplaza al servicio vecino, y por eso un hueco de instrumentación se parece a una conclusión.", note_kind="coral", foot=SINT)


def se421_cliente() -> Fig:
    r = e421_segmento()
    names = list(r)
    labels = [f"{name} ({p(v['cuota de tráfico %'] / 100, 2)} del tráfico)" for name, v in r.items()]
    cols = [("tasa global > 1 % en 5 min", "Tasa global > 1 %"), ("sonda fija en el cliente 1", "Sonda fija"), ("sonda rotativa", "Sonda rotativa")]
    return heatmap(
        "Una falla total que afecta a un solo cliente: qué señal la detecta en una hora",
        "Mapa de calor con el porcentaje de intentos en que cada señal detecta en una hora una falla total de un solo cliente: el umbral global de 1 por ciento en 5 minutos lo detecta siempre si el cliente aporta 23,4 o 2,3 por ciento del tráfico y en 8,7 por ciento de los intentos si aporta 0,58; una sonda fija en el cliente grande solo ve al cliente grande; una sonda rotativa por los 40 clientes detecta a todos.",
        labels, [c[1] for c in cols],
        [[r[nm][c[0]] * 100 for c in cols] for nm in names],
        unit="Detección (%)", scale="teal", vmin=0, vmax=100, decimals=0, suffix=" %", label_w=330,
        note="El cliente de la cola larga está 100 % caído y la tasa global apenas se mueve: aporta 0,58 % de las peticiones y el umbral exige 1 %. La sonda rotativa lo encuentra, pero tarda hasta 40 minutos. Cuarenta clientes con reparto 1/k son un supuesto del autor; la forma del reparto real cambia el resultado.", note_kind="gold", foot=SINT)


def se421_preguntas() -> Fig:
    r = e421_preguntas()
    day_mb = r["bytes por evento"] * r["peticiones por día"] / 1e6
    return grouped_bars(
        "Sesenta preguntas hechas después de un incidente: qué diseño de señales puede responderlas",
        f"Barras horizontales con las preguntas respondidas de {r['preguntas']}: las métricas con tres dimensiones previstas responden {r['responde métricas']} con {n(r['series por métrica previstas'])} series; los eventos anchos con todos los campos responden {r['responde eventos anchos']} con unos {n(day_mb)} megabytes al día; las métricas con todas las combinaciones responden las {r['preguntas']} pero exigirían {n(r['series para todas las combinaciones'])} series.",
        [f"Métricas con 3 dimensiones previstas ({n(r['series por métrica previstas'])} series)", f"Eventos anchos con todos los campos ({n(day_mb)} MB al día)",
         f"Métricas con todas las combinaciones ({n(r['series para todas las combinaciones'])} series)"],
        [("Preguntas respondidas", [r["responde métricas"], r["responde eventos anchos"], r["preguntas"]], "teal")],
        unit=f"Preguntas respondidas (de {r['preguntas']})", horizontal=True, label_w=330,
        note="Las 60 preguntas son combinaciones de 1 a 3 de las 8 dimensiones del servicio (endpoint, estado, región, curso, cliente, versión, dispositivo, plan); las dimensiones previstas son endpoint, estado y región. Los eventos conservan el detalle a cambio de volumen y de privacidad: cada campo extra es un dato que alguien puede leer.", note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-422
def se422_formato() -> Fig:
    r = e422_formato()
    words = ["v1: «Entrega 123 aceptada para curso 45 en 83 ms»", "v2: «Entrega aceptada: id=123 curso=45 duración=83ms»", "v3: «[api] entrega id=123 (curso 45) OK tiempo=83 milisegundos»", "v4: «Submission 123 accepted for course 45 in 83 ms»"]
    return grouped_bars(
        "La misma línea de registro en cuatro versiones del código: extracción con una expresión regular y con campos por nombre",
        "Barras horizontales con el porcentaje de líneas extraídas: una expresión regular escrita para la versión 1 extrae el 100 por ciento de las líneas de esa versión y 0 de las tres siguientes; leer campos por nombre de un registro JSON se mantiene en 100 por ciento en las versiones 1 a 3 y solo falla en la 4, donde se renombró un campo.",
        words,
        [("Regex escrita para la v1", [row["regex v1"] * 100 for row in r["filas"]], "coral"), ("Campos del JSON por nombre", [row["json por nombre"] * 100 for row in r["filas"]], "teal")],
        unit="Líneas extraídas (%)", horizontal=True, decimals=0, label_w=330,
        note="Cada versión se evaluó con 1 500 líneas. El registro estructurado mueve la ruptura del texto al contrato: sobrevive a un cambio de redacción y no a un campo renombrado. Por eso el nombre de un campo es una interfaz que se versiona y se prueba, no un detalle de implementación.", note_kind="gold", foot=SINT)


def se422_correlacion() -> Fig:
    r = e422_correlacion()
    prop = r["propagación"]
    return line_chart(
        "Correlación: cadenas completas según la probabilidad de conservar el identificador en cada salto",
        "Líneas con el porcentaje de peticiones de una cadena de cinco servicios y cuatro saltos que llegan completas según la probabilidad de conservar el identificador en cada salto: la simulación coincide con la fórmula p elevada a cuatro y baja de 95,9 por ciento con 0,99 a 81,4 con 0,95, 66,3 con 0,90 y menos con 0,80.",
        [("Simulada", [(e["p por salto"], e["completas simuladas"] * 100, "", "t") for e in prop], "teal"),
         ("Fórmula p⁴", [(e["p por salto"], e["p^4"] * 100, "", "b") for e in prop], "gold")],
        x_label="Probabilidad de conservar el identificador en cada salto", y_label="Peticiones con la cadena completa (%)", decimals=1,
        x_ticks=[(e["p por salto"], n(e["p por salto"], 2)) for e in prop], y_zero=False,
        note="La propagación falla de forma multiplicativa: cuatro saltos al 95 % dejan 81 % y la cola de peticiones incompletas es justo la de las colas y los hilos. Sin identificador, el tiempo solo desambigua con tráfico muy bajo; con una petición durando hasta 250 ms (supuesto del autor), a 20 por segundo siempre hay varias candidatas.", note_kind="coral", foot=SINT)


def se422_politicas() -> Fig:
    r = e422_politicas()
    return grouped_bars(
        "Muestreo de registros: errores que conserva cada política",
        f"Barras horizontales con los errores conservados de {n(r['errores'])}: el muestreo uniforme del 10 por ciento deja {n(r['errores con 10 %'])}, es decir pierde 9 de cada 10, y conservar todos los errores más el 10 por ciento del resto deja los {n(r['errores'])}.",
        ["Muestreo uniforme del 10 %", "Todos los errores y 10 % del resto"],
        [("Errores conservados", [r["errores con 10 %"], r["errores"]], "teal")],
        unit=f"Errores conservados (de {n(r['errores'])})", horizontal=True, label_w=270, ref_lines=[(r["errores"], "todos los errores")],
        note="La redacción por patrones solo protege los formatos que alguien previó: cada variante escrita por una persona (mayúsculas, espacios, un «arroba» escrito) es un dato personal que llega al almacén. Los 200 000 registros y las variantes son sintéticos; el 2 % de errores es un supuesto del autor.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-423
def se423_cardinalidad() -> Fig:
    steps = [("endpoint × estado × región (5 × 3 × 3)", 45), ("+ curso (30)", 1350), ("+ cliente (40)", 54000), ("+ identificador de persona (20 000)", 1080000000)]
    per = 429
    labels = []
    for name, series in steps:
        mem = series * per
        shown = f"{n(mem / 1e3, 0)} KB" if mem < 1e6 else (f"{n(mem / 1e6, 1)} MB" if mem < 1e9 else f"{n(mem / 1e9)} GB")
        labels.append(f"{name} · {shown}")
    return grouped_bars(
        "El número de series de una sola métrica según las dimensiones que se le añaden",
        "Barras horizontales en escala logarítmica con las series de una métrica: con endpoint, estado y región hay 45; añadir curso lleva a 1 350, añadir cliente a 54 000 y añadir el identificador de una persona a 1 080 millones de series.",
        labels, [("Series", [s for _, s in steps], "coral")],
        unit="Series de la métrica", horizontal=True, log=True, ticks=[10, 1000, 100000, 10000000, 1000000000], label_w=330,
        note="El número de series es el producto de las cardinalidades, no la suma, y cada serie nueva cuesta memoria e índice aunque nadie la consulte. Los 429 bytes por serie son una medición de CPython en este equipo con un diccionario de claves de texto; un almacén real tiene otra constante, y la forma del crecimiento es la misma.", note_kind="coral", foot=MEDIDO_35)


def se423_contadores() -> Fig:
    r = e423_contadores()
    c15, c60 = r["intervalos"]
    return grouped_bars(
        "Contador con reinicios: incrementos que reconstruye cada forma de leer y cada intervalo de muestreo",
        f"Barras horizontales con los incrementos de un contador de {n(r['verdad'])} con tres reinicios: restar el último valor del primero da {n(c15['diferencia ingenua'])}; con detección de reinicios da {n(c15['con reinicios'])} con scrape de 15 segundos y {n(c60['con reinicios'])} con scrape de 60.",
        ["Incremento real (verdad de la simulación)", "Último valor menos primero, scrape cada 15 s", "Con detección de reinicios, scrape cada 15 s", "Con detección de reinicios, scrape cada 60 s"],
        [("Incremento reconstruido", [r["verdad"], c15["diferencia ingenua"], c15["con reinicios"], c60["con reinicios"]], "teal")],
        unit="Incremento del contador en 600 s", horizontal=True, label_w=310, ref_lines=[(r["verdad"], "real")],
        note="Un contador sobrevive a un muestreo grueso porque acumula; un gauge no, porque el valor entre dos lecturas desaparece. La detección de reinicios pierde el tramo anterior a cada reinicio dentro del intervalo. Tasa de 100 por segundo, reinicios en 137, 301 y 452 s y picos uniformes son supuestos del autor.", note_kind="gold", foot=SINT)


def se423_histogramas() -> Fig:
    r = e423_histogramas()
    truth = r["verdad"]
    designs = list(r["diseños"].items())
    kinds = ["gold", "teal", "coral"]
    return grouped_bars(
        "Percentiles estimados con histogramas de tres diseños de cubetas frente al valor exacto",
        "Barras agrupadas con la mediana, el percentil 95 y el percentil 99 de 100 000 latencias lognormales: el valor exacto es 120,5, 381 y 608,2 milisegundos y cada diseño de cubetas lo estima con un error distinto, que se ve en la diferencia de altura frente a la barra gris.",
        ["p50", "p95", "p99"],
        [("Valor exacto", [truth[50], truth[95], truth[99]], "grey")] + [(f"Cubetas: {name}", [v[50], v[95], v[99]], kinds[i]) for i, (name, v) in enumerate(designs)],
        unit="Latencia (ms)", decimals=1,
        note="La interpolación lineal dentro de una cubeta supone datos repartidos de forma uniforme y el error nunca es menor que el ancho de la cubeta donde cae el percentil. Cubetas pensadas para otro rango (hasta 10 s) estiman el p99 con un 28 % de error. Elegir cubetas es elegir el error permitido antes de ver el incidente.", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-424
def se424_contexto() -> Fig:
    r = e424_contexto()
    return grouped_bars(
        "Propagación del contexto en una petición de seis saltos: dónde se pierde",
        f"Barras horizontales con el porcentaje de veces que cada frontera pierde el contexto: el salto HTTP síncrono 1 por ciento, la cola de mensajes 15, el grupo de hilos o tarea asíncrona 20 y el reintento automático 10; con esas pérdidas solo {p(r['completas'])} de las peticiones conservan una traza completa.",
        ["Salto HTTP síncrono", "Cola de mensajes", "Grupo de hilos o tarea asíncrona", "Reintento automático"],
        [("Contexto perdido", [1, 15, 20, 10], "coral")],
        unit="Veces que se pierde el contexto (%)", horizontal=True, decimals=0, label_w=260,
        note="Las probabilidades por frontera son supuestos del autor, pero el patrón es de diseño: el contexto se pierde donde cambia el medio de transporte o la unidad de ejecución. El formato W3C traceparent (versión, identificador de traza de 32 hex, identificador de span de 16 hex, banderas) se valida con una expresión regular estricta en minúsculas.", note_kind="gold", foot=SINT)


def se424_critica() -> Fig:
    r = e424_ruta_critica()
    a, b, c = list(r["ahorro medio ms"])
    return grouped_bars(
        "Reducir a la mitad un span: ahorro medio de latencia según cómo se elige el span a optimizar",
        f"Barras horizontales con el ahorro medio de latencia en {r['árboles']} árboles de spans sintéticos con latencia media de {n(r['latencia media ms'], 0)} milisegundos al reducir a la mitad un span: {n(r['ahorro medio ms'][a], 1)} milisegundos si se elige al azar, {n(r['ahorro medio ms'][b], 1)} si se elige el span más largo y {n(r['ahorro medio ms'][c], 1)} si se elige el de la ruta crítica.",
        [_cap(a), _cap(b), _cap(c)],
        [("Ahorro medio", [r["ahorro medio ms"][a], r["ahorro medio ms"][b], r["ahorro medio ms"][c]], "teal")],
        unit="Ahorro medio de latencia (ms)", horizontal=True, decimals=1, label_w=300,
        note="Un span fuera de la ruta crítica (hijos paralelos que no son el más lento) no cambia la latencia de la petición aunque se acelere. Los árboles (3 a 5 hijos en la raíz, hasta 3 niveles, la mitad de los nodos con hijos en paralelo) son un generador del autor, no trazas observadas.", note_kind="teal", foot=SINT)


def se424_muestreo() -> Fig:
    r = e424_muestreo()
    rc = r["recuento"]
    return grouped_bars(
        "Muestreo de trazas: lo interesante que conserva cada política",
        f"Barras con el porcentaje de trazas interesantes conservadas de 100 000 trazas con {n(rc['error'])} errores y {n(rc['lenta'])} lentas: el muestreo de cabeza del 1 por ciento conserva {r['cabeza 1 %']['error']} errores y {r['cabeza 1 %']['lenta']} lentas, y el muestreo por cola las conserva todas.",
        ["Errores", "Trazas lentas"],
        [("Muestreo de cabeza del 1 %", [r["cabeza 1 %"]["error"] / rc["error"] * 100, r["cabeza 1 %"]["lenta"] / rc["lenta"] * 100], "coral"),
         ("Muestreo por cola", [100.0, 100.0], "teal")],
        unit="Trazas conservadas (%)", decimals=1,
        note="El muestreo por cola decide con la traza entera, así que exige que todos los spans de una traza lleguen al mismo recolector (enrutado por hash del identificador) y memoria para retenerlos mientras se decide. Las proporciones de 1 % de errores y 2 % de lentas son supuestos del autor.", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-425
def se425_trafico() -> Fig:
    r = e425_trafico()
    esc = r["escenarios"]
    return grouped_bars(
        "Un presupuesto de error del 99,9 % mensual medido por peticiones y por minutos en tres incidentes",
        "Barras horizontales con el presupuesto mensual consumido por tres incidentes según se cuente por peticiones o por minutos: un corte total de 30 minutos a las 03:00 consume 8,6 por ciento por peticiones y 69,4 por minutos; el mismo corte a las 14:00 consume 166 por ciento por peticiones y 69,4 por minutos; 5 por ciento de errores durante 8 horas consume 121 por peticiones y 1 111 por minutos.",
        [e["nombre"] for e in esc],
        [("Presupuesto por peticiones", [e["presupuesto gastado por peticiones %"] for e in esc], "coral"), ("Presupuesto por minutos", [e["presupuesto gastado por minutos %"] for e in esc], "teal")],
        unit="Presupuesto de error consumido (%)", horizontal=True, log=True, decimals=1, label_w=300, ref_lines=[(100, "presupuesto agotado")],
        note="Contar por peticiones pondera el daño por las personas afectadas; contar minutos malos no distingue el tráfico y, con un umbral de 1 %, trata como minuto perdido uno con 5 % de errores. El tráfico (5 por segundo de noche, hasta 100 de día) y los 43,2 minutos mensuales del 99,9 % son el marco del autor.", note_kind="gold", foot=SINT)


def se425_donde() -> Fig:
    r = e425_donde_se_mide()
    return grouped_bars(
        "La misma disponibilidad medida en el servidor, en el cliente y tras reintentos: fallos que se ven",
        "Barras horizontales en escala logarítmica con el porcentaje de fallos de 200 000 solicitudes sintéticas: 0,073 si se mide en el servidor, 2,039 en el cliente con un intento, 0,0005 con tres intentos si todos los fallos fueran independientes y unas cien veces más con tres intentos cuando el fallo va pegado a la petición.",
        ["Servidor", "Cliente, un intento", "Tres intentos si los fallos fueran independientes", "Tres intentos con fallos pegados a la petición"],
        [("Fallos", [100 - r["servidor %"], 100 - r["cliente por intento %"], 100 - r["3 intentos si todo fuera independiente %"], 100 - r["3 intentos con fallos pegados %"]], "coral")],
        unit="Fallos (% = 100 − éxito)", horizontal=True, log=True, label_w=310,
        note="El servidor no cuenta lo que no llegó (2 % de fallos de red del cliente, supuesto del autor) y el reintento solo ayuda con fallos independientes: 0,03 % de peticiones que fallan siempre aparece como 0,03 % de fallos aunque se intente tres veces. Un objetivo debe nombrar el punto de medición.", note_kind="coral", foot=SINT)


def se425_composicion() -> Fig:
    r = e425_composicion()
    a, b = r["duración mediana 20 min"], r["duración mediana 10 min"]
    return grouped_bars(
        "Meses que incumplen un SLO de 99,9 % y un SLA de 99,5 % según la duración de los incidentes",
        f"Barras con el porcentaje de meses que incumplen el objetivo: con incidentes de duración mediana de 20 minutos, {n(a['incumple SLO 99,9 %'], 1)} por ciento incumple el SLO de 99,9 y {n(a['incumple SLA 99,5 %'], 2)} el SLA de 99,5; con duración mediana de 10 minutos, {n(b['incumple SLO 99,9 %'], 1)} y {n(b['incumple SLA 99,5 %'], 2)}.",
        ["Incidentes de duración mediana de 20 min", "Incidentes de duración mediana de 10 min"],
        [("Incumple el SLO de 99,9 %", [a["incumple SLO 99,9 %"], b["incumple SLO 99,9 %"]], "coral"), ("Incumple el SLA de 99,5 %", [a["incumple SLA 99,5 %"], b["incumple SLA 99,5 %"]], "gold")],
        unit="Meses que incumplen (%)", decimals=1,
        note="Un SLO de 99,9 % con tres o más dependencias del mismo nivel ya es optimista, y un SLA más holgado que el SLO deja margen para el contrato y no para la ingeniería. Dos incidentes de 20 minutos agotan el mes entero. 20 000 meses simulados; 1,2 incidentes por mes y la forma lognormal son supuestos del autor.", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-426
def se426_reglas() -> Fig:
    r = e426_reglas()
    reglas = r["reglas"]
    return grouped_bars(
        "Seis reglas de alerta sobre 180 días de tráfico diurno y nocturno con 14 caídas y 12 degradaciones lentas",
        "Barras horizontales con las páginas que genera cada regla y las que no corresponden a ningún incidente: el umbral de 0,5 por ciento en un minuto genera 12 622 páginas, 11 748 sin incidente, y el de 1 por ciento en 5 minutos genera 609, 396 sin incidente; las reglas por tasa de consumo del presupuesto generan entre 13 y 31 páginas y ninguna sin incidente.",
        [_cap(x["regla"]) for x in reglas],
        [("Páginas", [x["páginas"] for x in reglas], "gold"), ("Páginas sin incidente", [x["páginas sin incidente"] for x in reglas], "coral")],
        unit="Páginas en 180 días", horizontal=True, label_w=300,
        note="Ninguna regla detecta las 12 degradaciones sin pagar páginas falsas: la regla de 1 % en 5 minutos las ve todas porque de noche, con 30 peticiones por minuto, dos errores bastan. Una página que no pide acción es coste puro. Tasa de error base de 0,1 %, tráfico entre 30 y 300 por minuto e incidentes inyectados son supuestos del autor.", note_kind="coral", foot=SINT)


def se426_ruido() -> Fig:
    r = e426_ruido()
    return grouped_bars(
        "Fatiga de alertas: páginas por 200 incidentes en cascada y 3 000 destellos según la política de filtrado",
        f"Barras horizontales con las páginas que genera cada política: {n(r['páginas sin filtros'])} sin filtros, {n(r['con duración mínima'])} con una duración mínima antes de paginar y {n(r['con duración y agrupación'])} con duración mínima y agrupación por incidente.",
        ["Sin filtros: cada alerta de cada servicio pagina", "Con duración mínima antes de paginar", "Con duración mínima y agrupación por incidente"],
        [("Páginas", [r["páginas sin filtros"], r["con duración mínima"], r["con duración y agrupación"]], "coral")],
        unit="Páginas", horizontal=True, label_w=310,
        note="Filtrar no es silenciar: el filtro de duración retrasa la página por construcción y la agrupación exige conocer el mapa de dependencias para saber qué alertas pertenecen al mismo incidente. El 4 % de destellos que sobrevive al filtro es un supuesto del autor.", note_kind="gold", foot=SINT)


def se426_ventanas() -> Fig:
    r = e426_ventanas()
    f = r["filas"]
    xs = [x["ventana min"] for x in f]
    def serie(k):
        return [(x["ventana min"], x[k]) for x in f if isinstance(x[k], (int, float))]
    return line_chart(
        "Umbral de 1 % de errores con ventanas de 1 a 60 minutos: minutos hasta alertar",
        "Líneas con los minutos hasta alertar según la ventana: crecen con la ventana cuando el error es pequeño (con 2 por ciento pasan de 1 a 28 minutos) y quedan en 1 minuto con la caída total; los falsos positivos al día, que van entre paréntesis en cada ventana, bajan de 6,85 con un minuto a 0,02 con 5 y a 0 con 15 y 60.",
        [("2 % de errores", serie("2 % de errores"), "gold"), ("10 % de errores", serie("10 % de errores"), "teal"), ("Caída total", serie("100 % de errores"), "coral")],
        x_label="Ventana (minutos); entre paréntesis, falsos positivos por día", y_label="Minutos hasta alertar", log_x=True, log_y=True,
        x_ticks=[(x["ventana min"], f"{x['ventana min']} ({n(x['falsos positivos por día'], 2)})") for x in f], decimals=0,
        note="Una ventana larga suprime el ruido y retrasa lo moderado, y a una caída total no la retrasa casi nada: por eso se combinan ventanas largas para lo lento y cortas para lo grave. La ventana incluye la historia sana previa al incidente; 120 días de ruido con 100 peticiones por minuto es un supuesto del autor.", note_kind="teal", foot=SINT)


FIGURES = {
    "se-421-localizar-la-lentitud.svg": se421_localizar,
    "se-421-falla-de-un-solo-cliente.svg": se421_cliente,
    "se-421-preguntas-sin-respuesta.svg": se421_preguntas,
    "se-422-cuatro-versiones-del-registro.svg": se422_formato,
    "se-422-propagacion-y-lineas-huerfanas.svg": se422_correlacion,
    "se-422-volumen-muestreo-y-redaccion.svg": se422_politicas,
    "se-423-explosion-de-series.svg": se423_cardinalidad,
    "se-423-contadores-y-picos.svg": se423_contadores,
    "se-423-percentiles-con-histogramas.svg": se423_histogramas,
    "se-424-donde-se-rompe-el-contexto.svg": se424_contexto,
    "se-424-ruta-critica.svg": se424_critica,
    "se-424-muestreo-de-trazas.svg": se424_muestreo,
    "se-425-peticiones-o-minutos.svg": se425_trafico,
    "se-425-donde-se-mide.svg": se425_donde,
    "se-425-composicion-y-meses.svg": se425_composicion,
    "se-426-seis-reglas-de-alerta.svg": se426_reglas,
    "se-426-fatiga-y-agrupacion.svg": se426_ruido,
    "se-426-ventanas-de-alerta.svg": se426_ventanas,
}
