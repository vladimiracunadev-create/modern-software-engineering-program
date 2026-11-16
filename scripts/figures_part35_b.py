"""Figures for SE-427 to SE-432 (synthetic data, fixed seeds, virtual time; real probes of SQLite copies and platform on Windows CPython 3.12.9 and Ubuntu/WSL2 3.12.3)."""
from __future__ import annotations

from experiments_part35_b import (
    e427_escalamiento, e427_guardia, e427_linter, e428_actualizaciones, e428_cronologia, e428_severidad, e429_cadena, e429_linter, e429_recurrencia,
    e430_dependencias, e430_rpo, e431_ambiguedad, e431_estrategias, e431_perdida, e432_cadena, e432_validador,
)
from figure_kit import Fig, grouped_bars, line_chart, percentile_intervals, stacked_bars
from figures_part35_a import _cap, n, p

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."


# ---------------------------------------------------------------- SE-427
def se427_guardia() -> Fig:
    r = e427_guardia()
    f = r["filas"]
    return grouped_bars(
        "Carga de una guardia semanal según el tamaño del equipo (1,5 páginas al día, 35 % de noche)",
        "Barras con la carga anual de la persona más cargada según el tamaño del equipo: con dos personas hace 27 semanas de guardia y tiene 77 noches interrumpidas; con cuatro, 14,4 semanas y 42 noches; con ocho, 8 semanas y 23 noches.",
        [f"{x['personas']} personas" for x in f],
        [("Semanas de guardia de la persona más cargada", [x["semanas de guardia de la persona más cargada"] for x in f], "gold"), ("Noches interrumpidas", [x["noches interrumpidas"] for x in f], "coral")],
        unit="Semanas o noches al año", decimals=1,
        note="Las cifras son de la persona más cargada tras las ausencias, que es la que se agota primero. Con dos personas una ausencia deja a la otra en guardia permanente. 1,5 páginas al día y 35 % de noche son supuestos del autor; cada página nocturna cuesta más que su duración porque rompe el sueño.", note_kind="coral", foot=SINT)


def se427_escalamiento() -> Fig:
    r = e427_escalamiento()
    f = r["filas"]
    return grouped_bars(
        "Una página con y sin escalamiento: fracción atendida",
        "Barras horizontales con el porcentaje de páginas atendidas: con respuesta de 85 por ciento por persona y fallos independientes, una página sin escalar se atiende 84,8 por ciento de las veces y con tres niveles de cinco minutos 99,8 por ciento en 15 minutos; si 30 por ciento comparten causa, sin escalar se atiende 59,9 por ciento y con tres niveles 96,9.",
        [x["escenario"] for x in f],
        [("Sin escalar", [x["sin escalar, atendida %"] for x in f], "coral"), ("Con tres niveles (15 min)", [x["con tres niveles, atendida en 15 min %"] for x in f], "teal")],
        unit="Páginas atendidas (%)", horizontal=True, decimals=1, label_w=300,
        note="El escalamiento protege contra el olvido y el sueño; no protege contra una causa compartida entre niveles (la misma zona sin red, el mismo canal de aviso). Las probabilidades de 85 %, 85 % y 90 % por nivel y el 30 % de causa compartida son supuestos del autor, no mediciones de ninguna herramienta de guardia.", note_kind="gold", foot=SINT)


def se427_linter() -> Fig:
    r = e427_linter()
    f = r["filas"]
    return stacked_bars(
        "Un verificador de runbooks frente a 240 mutaciones de ocho runbooks base (diez operadores)",
        f"Barras apiladas con las mutaciones detectadas y no detectadas por tipo: el verificador de campos, fechas, referencias a alertas y reversiones detecta {r['detectadas']} de 240; detecta las seis que rompen la forma y ninguna de las cuatro que cambian el sentido sin romperla: intercambiar el contenido de dos pasos, apuntar al entorno equivocado, cambiar el comando por otro plausible y un propietario inexistente.",
        [_cap(x["mutación"]) for x in f],
        [("Detectadas", [x["detectadas"] for x in f], "teal"), ("No detectadas", [x["de"] - x["detectadas"] for x in f], "coral")],
        unit="Mutaciones", horizontal=True, label_w=330, plot_h=300,
        note=f"Detecta {r['detectadas']} de {r['total']} ({p(r['detectadas'] / r['total'], 0)}): todo lo que ve es forma y ninguna de las 96 que se escapan la viola. Un runbook bien formado y erróneo es peor que uno ausente porque se ejecuta con confianza; solo un ejercicio real lo descubre. Las ocho bases y los operadores son construcciones del autor.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-428
def se428_cronologia() -> Fig:
    r = e428_cronologia()
    t = r["medias por tramo"]
    e = r["media si se reduce a la mitad la mediana de"]
    lo, hi = r["media de 30 incidentes: p5–p95"]
    return stacked_bars(
        "Dos mil incidentes sintéticos: de qué se compone la media del tiempo hasta resolver",
        f"Barra apilada con la media del tiempo hasta resolver, {n(r['media min'], 1)} minutos, por tramo: detección {n(t['detección'], 1)}, reconocimiento {n(t['reconocimiento'], 1)}, diagnóstico {n(t['diagnóstico'], 1)}, mitigación {n(t['mitigación'], 1)} y verificación {n(t['verificación'], 1)}; la media de un trimestre de 30 incidentes va de {n(lo, 1)} a {n(hi, 1)} minutos con la misma práctica.",
        ["Media del tiempo hasta resolver"],
        [("Detección", [t["detección"]], "navy"), ("Reconocimiento", [t["reconocimiento"]], "grey"), ("Diagnóstico", [t["diagnóstico"]], "coral"),
         ("Mitigación", [t["mitigación"]], "gold"), ("Verificación", [t["verificación"]], "teal")],
        unit="Minutos", horizontal=True, decimals=1, label_w=230, plot_h=120,
        note="Comparar la media de dos trimestres con 30 incidentes cada uno confunde azar y mejora: la diferencia entre p5 y p95 (31 minutos) es mayor que la mejora que produce adelantar la detección. Las medianas y dispersiones de cada tramo son supuestos del autor, no mediciones.", note_kind="gold", foot=SINT)


def se428_actualizaciones() -> Fig:
    r = e428_actualizaciones()
    f = r["filas"]
    return grouped_bars(
        "Cadencia de actualizaciones de estado: minutos de la persona al mando según la política",
        "Barras horizontales con los minutos que gasta la persona al mando por incidente según la política de actualización: sin cadencia recibe 32,9 preguntas y gasta 98,7 minutos; actualizar cada 30 minutos baja las preguntas a 10,1 y el gasto a 42,4 minutos, el mínimo.",
        [f"{_cap(x['política'])} ({n(x['preguntas por incidente'], 1)} preguntas)" for x in f],
        [("Minutos de la persona al mando", [x["minutos de la persona al mando"] for x in f], "teal")],
        unit="Minutos de la persona al mando por incidente", horizontal=True, decimals=1, label_w=300,
        note="Hay una cadencia que minimiza el coste y no es la más frecuente: cada actualización cuesta 4 minutos y cada pregunta 3. La tasa de preguntas que crece con la antigüedad de la última noticia y la duración mediana de 90 minutos son supuestos del autor; el óptimo real depende de a quién se informa y de cómo.", note_kind="teal", foot=SINT)


def se428_severidad() -> Fig:
    r = e428_severidad()
    f = r["filas"]
    return grouped_bars(
        "Tres personas clasifican 400 incidentes en cuatro niveles de severidad con tres tipos de criterio",
        "Barras horizontales con el acuerdo con la severidad verdadera y el error de dos o más niveles según el criterio: con criterios vagos el kappa de Cohen es 0,29 y se coincide con la verdad 57,8 por ciento de las veces; con umbrales numéricos de impacto el kappa sube a 0,61 y el acuerdo a 80,1; con umbrales y un ejemplo por nivel, a 0,83 y 91,8, y el error de dos o más niveles baja de 2,2 a 0 por ciento.",
        [f"{x['criterio']} (kappa {n(x['kappa medio'], 2)})" for x in f],
        [("Acuerdo con la verdad", [x["acuerdo con la verdad %"] for x in f], "teal"), ("Error de 2 o más niveles", [x["error de 2 o más niveles %"] for x in f], "coral")],
        unit="Incidentes (%)", horizontal=True, decimals=1, label_w=330,
        note="La severidad que se declara en minutos de tensión depende de cómo se perciba el impacto: el ruido de percepción (0,9, 0,35 y 0,15 en escala logarítmica) es un supuesto del autor. Lo que importa es la dirección: un criterio medible convierte una opinión en una decisión que otra persona reproduce.", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-429
def se429_recurrencia() -> Fig:
    r = e429_recurrencia()
    f = r["filas"]
    kinds = ["coral", "gold", "teal", "navy", "grey"]
    return line_chart(
        "Incidentes por año tras tres años según el porcentaje de acciones correctivas que se completan",
        "Líneas con los incidentes por año a lo largo de tres años según el porcentaje de acciones correctivas completadas: con 12 causas y unos 40 incidentes el primer año, completar 30 por ciento deja 16,7 incidentes el segundo año y 11,2 el tercero; completar 60 por ciento deja 9,7 y 5,9; cuanto más se completa, más rápido bajan.",
        [(f"{x['acciones completadas %']} % de las acciones completadas", [(1, x["año 1"]), (2, x["año 2"]), (3, x["año 3"])], kinds[i]) for i, x in enumerate(f)],
        x_label="Año", y_label="Incidentes por año", x_ticks=[(1, "1"), (2, "2"), (3, "3")], decimals=1, point_labels="last",
        note="Cada acción completada reduce al 40 % la tasa de su causa (supuesto del autor) y la reduce una vez por incidente. La brecha entre 30 % y 90 % de cumplimiento es 3,3 veces en el tercer año: un postmortem cuyas acciones no se cierran enseña, pero no cambia el sistema.", note_kind="coral", foot=SINT)


def se429_cadena() -> Fig:
    r = e429_cadena()
    top = sorted(r["reparto de raíces"].items(), key=lambda x: -x[1])
    return grouped_bars(
        "Cinco porqués sobre un grafo de 12 factores: causas raíz distintas que declaran 400 analistas",
        f"Barras horizontales con los analistas, de 400, que declaran cada causa raíz tras seguir una cadena de porqués sobre el mismo grafo de 12 factores contribuyentes: aparecen {len(top)} causas raíz distintas; una cadena recorre en promedio {p(r['cobertura media de una cadena %'] / 100)} de los factores y cuatro analistas independientes cubren {p(r['cobertura media de cuatro analistas %'] / 100)}.",
        [f"Raíz declarada: {k}" for k, _ in top],
        [("Analistas", [v for _, v in top], "teal")],
        unit="Analistas (de 400)", horizontal=True, label_w=330,
        note="Una cadena lineal sobre un sistema con causas que convergen produce una causa raíz que depende de qué rama se eligió primero, no de qué pasó. El grafo (un síntoma, 12 factores y 12 aristas) es un caso construido por el autor para la clase; su forma, no sus nombres, es el punto.", note_kind="gold", foot=SINT)


def se429_linter() -> Fig:
    r = e429_linter()
    f = r["filas"]
    return stacked_bars(
        "Un verificador de postmortems frente a 180 mutaciones (nueve operadores sobre veinte documentos cada uno)",
        f"Barras apiladas con las mutaciones detectadas y no detectadas por tipo: el verificador de lenguaje de culpa explícito, cifras de impacto, horas en la línea de tiempo, dos factores como mínimo y propietario y verificación de cada acción detecta {r['detectadas']} de 180; las que cambian el sentido sin tocar la forma pasan.",
        [_cap(x["mutación"]) for x in f],
        [("Detectadas", [x["detectadas"] for x in f], "teal"), ("No detectadas", [x["de"] - x["detectadas"] for x in f], "coral")],
        unit="Mutaciones", horizontal=True, label_w=330, plot_h=300,
        note=f"Detecta {r['detectadas']} de {r['total']} ({p(r['detectadas'] / r['total'], 0)}). Un documento que pasa el verificador puede culpar sin nombrar a nadie («como siempre, el turno de noche…») y proponer acciones que nadie podrá comprobar. Medir la forma de un postmortem es medir su limpieza, no su calidad.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-430
def se430_rpo() -> Fig:
    r = e430_rpo()
    f = r["filas"]
    return percentile_intervals(
        "Datos perdidos al fallar en un instante aleatorio según la estrategia de copia y réplica frente a un RPO de 5 minutos",
        "Intervalos en escala logarítmica con la pérdida de datos mediana, el percentil 99 y la máxima según la estrategia: con copia diaria la mediana es 719,7 minutos y la máxima 1 440; con copia cada hora la mediana es 30 y la máxima 60; la réplica asíncrona pierde segundos y es la única que cumple el RPO de 5 minutos.",
        [(_cap(x["estrategia"]), [x["pérdida mediana min"], x["p99 min"], x["máxima min"]]) for x in f],
        unit="Pérdida de datos (minutos)", marks=("mediana", "p99", "máx"), log=True, ref_lines=[(5, "RPO = 5 min")], label_w=300,
        note="El RPO real de una copia periódica es su intervalo, no la mediana; el de una réplica es el peor retraso, no el habitual, y una réplica también copia los errores (un borrado). 20 000 fallas por estrategia; el retraso con 1 % de picos es un supuesto del autor.", note_kind="gold", foot=SINT)


def se430_copias() -> Fig:
    return grouped_bars(
        "Cuarenta copias dañadas de una base de 20 000 filas: daños que detecta cada comprobación",
        "Barras horizontales con los daños detectados de 40 copias de una base SQLite alterada en ocho posiciones: el éxito del trabajo de copia, el tamaño y el conteo de filas detectan 0; la verificación de integridad de SQLite detecta 20; la huella sha256 y leer y comprobar todas las filas detectan 40.",
        ["El trabajo de copia terminó sin error", "El tamaño del archivo coincide", "Huella sha256 distinta de la registrada", "PRAGMA integrity_check", "COUNT(*) de la tabla", "Leer y comprobar todas las filas"],
        [("Daños detectados", [0, 0, 40, 20, 0, 40], "teal")],
        unit="Daños detectados (de 40)", horizontal=True, label_w=300, ref_lines=[(40, "40")],
        note="La copia buena se creó con la API de copia en línea de SQLite y restauró las 20 000 filas con integrity_check «ok». Una copia que nadie restaura no es una copia: la huella detecta el cambio, y solo restaurar y consultar prueba que la base funciona. Medición real en Windows y Ubuntu con resultado igual; la lectura completa depende de que el daño invalide el texto.", note_kind="teal", foot=REAL)


def se430_dependencias() -> Fig:
    r = e430_dependencias()
    f = [x for x in r["filas"] if not x["ciclo"]]
    return grouped_bars(
        "Restaurar 12 componentes desde cero: tiempo en serie y ruta crítica",
        "Barras horizontales con los minutos para restaurar 12 componentes: uno a uno tarda 225 y en paralelo respetando las dependencias la ruta crítica es de 125; cuando la identidad necesita los secretos y los secretos necesitan la identidad hay un ciclo y no se arranca desde cero, lo que solo revela un ejercicio.",
        [_cap(x["conjunto"]) for x in f],
        [("Restauración en serie", [x["serie min"] for x in f], "coral"), ("Ruta crítica", [x["ruta crítica min"] for x in f], "teal")],
        unit="Minutos para restaurar", horizontal=True, label_w=330,
        note="El RTO de 125 minutos de una tabla de dependencias incompleta es una promesa vacía: el ejercicio encontró un ciclo y añadió 5 minutos a la ruta crítica. Los 12 componentes, sus duraciones y sus dependencias son un ejemplo del autor, no una medición de ningún sistema.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-431
def se431_ambiguedad() -> Fig:
    r = e431_ambiguedad()
    f = r["filas"]
    return line_chart(
        "Diez fallas posibles y doce señales: cuántas fallas se distinguen cuando faltan señales",
        "Líneas con las clases de falla distinguibles y las fallas identificables sin ambigüedad según las señales ausentes: con las 12 señales las 10 fallas se distinguen; si falta una cualquiera, 9,83 se identifican sin ambigüedad en promedio; si faltan tres, 8,95, y hasta tres fallas pueden quedar indistinguibles.",
        [("Clases distinguibles (media de 10)", [(x["señales ausentes"], x["clases distinguibles (media de 10)"]) for x in f], "teal"),
         ("Fallas sin ambigüedad (media)", [(x["señales ausentes"], x["fallas identificables sin ambigüedad (media)"]) for x in f], "coral")],
        x_label="Señales ausentes (de 12)", y_label="Fallas (de 10)", point_labels="last", x_ticks=[(x["señales ausentes"], str(x["señales ausentes"])) for x in f], decimals=2, y_zero=False,
        note="La matriz de firmas (qué señal se desvía con cada falla) es del autor y trata cada señal como binaria; sirve para contar ambigüedades, no para estimar probabilidades. Lo que falta importa más que cuántas faltan: la combinación de señales ausentes decide qué fallas se confunden.", note_kind="gold", foot=SINT)


def se431_estrategias() -> Fig:
    r = e431_estrategias()
    f = r["filas"]
    return grouped_bars(
        "Cómo elegir la siguiente observación para aislar una falla entre diez: tres estrategias sobre 4 000 diagnósticos",
        "Barras horizontales con las observaciones hasta aislar la falla y el coste medio: elegir en cada paso la observación que mejor reparte las hipótesis restantes aísla la falla en 3,59 observaciones y coste 4,98; mirar primero lo más barato necesita 6,09 observaciones y coste 8,49.",
        [_cap(x["estrategia"]) for x in f],
        [("Observaciones hasta aislar", [x["observaciones hasta aislar (media)"] for x in f], "teal"), ("Coste medio", [x["coste medio"] for x in f], "gold")],
        unit="Observaciones o coste (unidades)", horizontal=True, decimals=2, label_w=330,
        note="Lo más barato primero no es lo más informativo: mira señales que no separan hipótesis. Los costes de 1 a 4 por observación y la ausencia de ruido de medida son supuestos del autor; con medidas ruidosas hay que repetir observaciones y la ventaja de elegir bien se reduce.", note_kind="teal", foot=SINT)


def se431_perdida() -> Fig:
    r = e431_perdida()
    f = r["filas"]
    return grouped_bars(
        "Tasa de error durante un incidente leída en registros cuando el agente pierde más líneas de error que de éxito",
        "Barras con la tasa de error real y la observada en los registros según el modelo de pérdida de líneas: con una pérdida igual para todas las líneas la observada es 12,51 por ciento frente a 12,53 reales; si se pierde 25 o 50 por ciento de las líneas de error, la tasa observada baja a 10,20 y a 6,99 por ciento.",
        [_cap(x["modelo"]) for x in f],
        [("Tasa de error real", [x["tasa de error real %"] for x in f], "navy"), ("Tasa observada en los registros", [x["tasa observada en los registros %"] for x in f], "coral")],
        unit="Líneas que son error (%)", decimals=2,
        note="Se conserva más de 92 % de las líneas y la tasa de error se ve a la mitad: la pérdida depende de aquello que se mide. La telemetría falla justo cuando el sistema falla, y la ausencia de errores en los registros no prueba que no los haya habido. Los porcentajes de pérdida son supuestos del autor.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-432
def se432_validador() -> Fig:
    r = e432_validador()
    f = r["filas"]
    return stacked_bars(
        "Un validador de paquetes operativos frente a 360 mutaciones (doce operadores, treinta paquetes cada uno)",
        f"Barras apiladas con las mutaciones detectadas y no detectadas por tipo: el validador de referencias cruzadas entre servicios, objetivos, alertas, runbooks, copias y ejercicios detecta {r['detectadas']} de 360; detecta todas las de siete operadores y ninguna de las que cambian el sentido sin romper una referencia.",
        [_cap(x["mutación"]) for x in f],
        [("Detectadas", [x["detectadas"] for x in f], "teal"), ("No detectadas", [x["de"] - x["detectadas"] for x in f], "coral")],
        unit="Mutaciones", horizontal=True, label_w=330, plot_h=340,
        note=f"Detecta {r['detectadas']} de {r['total']} ({p(r['detectadas'] / r['total'], 0)}), todas por referencias rotas o fechas vencidas. Ninguna de las cinco clases que se escapan viola el formato: son errores de significado. Un paquete coherente consigo mismo no es un sistema operable; los doce operadores y el paquete base son construcciones del autor.", note_kind="coral", foot=SINT)


def se432_reproducibilidad() -> Fig:
    return stacked_bars(
        "Mismo código, dos sistemas: sondas que se reproducen y sondas que cambian en Windows 11 y Ubuntu bajo WSL2",
        "Barra apilada con las siete sondas comparadas entre Windows 11 con CPython 3.12.9 y Ubuntu con 3.12.3: dos son idénticas (la huella de los resultados de tiempo virtual y la conservación de un nombre con eñe) y cinco difieren (separador de línea, bytes escritos como texto, caracteres leídos con la codificación local, separador de rutas y distinción de mayúsculas en una ruta).",
        ["Sondas comparadas (7)"],
        [("Idénticas", [2], "teal"), ("Distintas", [5], "coral")],
        unit="Sondas", horizontal=True, label_w=230, plot_h=120,
        note="Un resultado calculado con semilla fija se reproduce en cualquier sistema; todo lo que toca el sistema de archivos o la codificación cambia. Declarar la codificación (utf-8) en cada lectura y escritura evita el caso del texto leído con otra. Medición real de los dos sistemas; la huella cubre tres experimentos del paquete.", note_kind="gold", foot=REAL)


def se432_cadena() -> Fig:
    r = e432_cadena()
    names = list(r["fallos por etapa %"])
    return grouped_bars(
        "Una respuesta a incidentes de cinco etapas: dónde se pierde y cuánto sube la recuperación al mejorar cada etapa 5 puntos",
        f"Barras horizontales con los incidentes que fallan en cada etapa y con la recuperación completa que resultaría de mejorar esa etapa 5 puntos: con cinco etapas de 95, 92, 80, 88 y 90 por ciento de éxito, el producto es {p(r['producto de las etapas %'] / 100)} y la simulación de 20 000 incidentes da {p(r['recuperación completa simulada %'] / 100)}; la etapa más débil es la que más rinde al mejorarla.",
        [_cap(k) for k in names],
        [("Incidentes que fallan en la etapa", [r["fallos por etapa %"][k] for k in names], "coral"), ("Recuperación completa si se mejora 5 puntos", [r["mejorar 5 puntos la etapa (producto %)"][k] for k in names], "teal")],
        unit="Porcentaje (%)", horizontal=True, decimals=1, label_w=230, ref_lines=[(r["producto de las etapas %"], "actual")],
        note="Una cadena de etapas buenas por separado se recupera menos de una de cada dos veces a lo largo del año, y la mejora más rentable está en la etapa más débil, no en la más visible. Las probabilidades por etapa y la dependencia por la telemetría son supuestos del autor.", note_kind="teal", foot=SINT)


FIGURES = {
    "se-427-carga-de-la-guardia.svg": se427_guardia,
    "se-427-escalamiento-y-causa-compartida.svg": se427_escalamiento,
    "se-427-verificador-de-runbooks.svg": se427_linter,
    "se-428-de-que-se-compone-el-tiempo.svg": se428_cronologia,
    "se-428-cadencia-de-actualizaciones.svg": se428_actualizaciones,
    "se-428-acuerdo-sobre-la-severidad.svg": se428_severidad,
    "se-429-cumplimiento-y-recurrencia.svg": se429_recurrencia,
    "se-429-cinco-porques-sobre-un-grafo.svg": se429_cadena,
    "se-429-verificador-de-postmortems.svg": se429_linter,
    "se-430-datos-perdidos-y-rpo.svg": se430_rpo,
    "se-430-copias-danadas.svg": se430_copias,
    "se-430-orden-de-restauracion.svg": se430_dependencias,
    "se-431-fallas-indistinguibles.svg": se431_ambiguedad,
    "se-431-elegir-la-siguiente-observacion.svg": se431_estrategias,
    "se-431-telemetria-que-se-pierde.svg": se431_perdida,
    "se-432-verificador-de-paquetes.svg": se432_validador,
    "se-432-reproducibilidad-entre-sistemas.svg": se432_reproducibilidad,
    "se-432-cadena-de-respuesta.svg": se432_cadena,
}
