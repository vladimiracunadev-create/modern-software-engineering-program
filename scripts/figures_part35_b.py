"""Figures for SE-427 to SE-432 (synthetic data, fixed seeds, virtual time; real probes of SQLite copies and platform on Windows CPython 3.12.9 and Ubuntu/WSL2 3.12.3)."""
from __future__ import annotations

from experiments_part35_b import (
    e427_escalamiento, e427_guardia, e427_linter, e428_actualizaciones, e428_cronologia, e428_severidad, e429_cadena, e429_linter, e429_recurrencia,
    e430_dependencias, e430_rpo, e431_ambiguedad, e431_estrategias, e431_perdida, e432_cadena, e432_validador,
)
from figure_kit import Fig
from figures_part07_a import tab
from figures_part35_a import n, p

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."


# ---------------------------------------------------------------- SE-427
def se427_guardia() -> Fig:
    r = e427_guardia()
    rows = [[str(x["personas"]), n(x["semanas de guardia de la persona más cargada"], 1), n(x["noches interrumpidas"]), n(x["páginas nocturnas"])] for x in r["filas"]]
    return tab("Carga de una guardia semanal con 1,5 páginas al día, 35 % de noche y 4 semanas de ausencia por persona, según el tamaño del equipo",
               "Tabla: con dos personas la más cargada hace 27 semanas de guardia al año y tiene 77 noches interrumpidas; con cuatro hace 14,4 semanas y 42 noches; con ocho hace 8 semanas y 23 noches. La probabilidad de que una noche tenga al menos una página es 40,8 por ciento.",
               ["Personas en la rotación", "Semanas de guardia al año", "Noches interrumpidas al año", "Páginas nocturnas al año"], rows, [210, 230, 230, 230], row_h=44, size=13,
               note="Las cifras son de la persona más cargada tras las ausencias, que es la que se agota primero. Con dos personas una ausencia deja a la otra en guardia permanente. 1,5 páginas al día y 35 % de noche son supuestos del autor; cada página nocturna cuesta más que su duración porque rompe el sueño.",
               note_kind="coral", foot=SINT)


def se427_escalamiento() -> Fig:
    r = e427_escalamiento()
    rows = [[x["escenario"], p(x["sin escalar, atendida %"] / 100), p(x["con tres niveles, atendida en 15 min %"] / 100), f"{n(x['mediana de minutos hasta atender'], 1)} / {n(x['p99'], 1)} min"] for x in r["filas"]]
    return tab("Una página con y sin escalamiento: fracción atendida y minutos hasta que alguien responde",
               "Tabla: con respuesta de 85 por ciento por persona y fallos independientes, una página sin escalar se atiende 84,8 por ciento de las veces y con tres niveles de cinco minutos 99,8 por ciento en 15 minutos; si 30 por ciento de los fallos comparte causa, esas cifras son 59,9 y 96,9 por ciento.",
               ["Escenario", "Sin escalar", "Tres niveles (15 min)", "Mediana / p99 hasta atender"], rows, [380, 140, 190, 210], row_h=64, size=12,
               note="El escalamiento protege contra el olvido y el sueño; no protege contra una causa compartida entre niveles (la misma zona sin red, el mismo canal de aviso). Las probabilidades de 85 %, 85 % y 90 % por nivel y el 30 % de causa compartida son supuestos del autor, no mediciones de ninguna herramienta de guardia.",
               note_kind="gold", foot=SINT)


def se427_linter() -> Fig:
    r = e427_linter()
    rows = [[x["mutación"].capitalize(), f"{x['detectadas']} de {x['de']}", "Lo ve la forma" if x["detectadas"] else "Solo lo ve quien ejecuta el runbook"] for x in r["filas"]]
    return tab("Un verificador de runbooks frente a 240 mutaciones de ocho runbooks base (diez operadores)",
               f"Tabla: un verificador de campos, fechas, referencias a alertas y reversiones detecta {r['detectadas']} de 240 mutaciones de runbooks; detecta 24 de 24 al quitar un campo, vaciar la salida esperada, quitar la reversión de un paso destructivo, envejecer la verificación, escribir mal la alerta o dejar el escalamiento en TBD, y 0 de 24 al intercambiar el contenido de dos pasos, apuntar al entorno equivocado, cambiar el comando por otro plausible o nombrar un propietario inexistente.",
               ["Mutación", "Detectadas", "Por qué"], rows, [470, 130, 320], row_h=40, size=12,
               note=f"Detecta {r['detectadas']} de {r['total']} ({p(r['detectadas'] / r['total'], 0)}): todo lo que ve es forma y ninguna de las 96 que se escapan la viola. Un runbook bien formado y erróneo es peor que uno ausente porque se ejecuta con confianza; solo un ejercicio real lo descubre. Las ocho bases y los operadores son construcciones del autor.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-428
def se428_cronologia() -> Fig:
    r = e428_cronologia()
    t = r["medias por tramo"]
    e = r["media si se reduce a la mitad la mediana de"]
    lo, hi = r["media de 30 incidentes: p5–p95"]
    rows = [
        ["Tiempo total hasta resolver: media / mediana / p90 / p99", f"{n(r['media min'], 1)} / {n(r['mediana min'], 1)} / {n(r['p90 min'], 1)} / {n(r['p99 min'], 1)} min"],
        ["Reparto de la media por tramo", f"detección {n(t['detección'], 1)}, reconocimiento {n(t['reconocimiento'], 1)}, diagnóstico {n(t['diagnóstico'], 1)}, mitigación {n(t['mitigación'], 1)}, verificación {n(t['verificación'], 1)} min"],
        ["Media de un trimestre de 30 incidentes (p5 a p95 de 4 000 trimestres)", f"de {n(lo, 1)} a {n(hi, 1)} min con la misma práctica"],
        ["Media si se reduce a la mitad la mediana de la detección / el diagnóstico / la mitigación", f"{n(e['detección'], 1)} / {n(e['diagnóstico'], 1)} / {n(e['mitigación'], 1)} min"],
    ]
    return tab("Dos mil incidentes sintéticos: de qué se compone el tiempo hasta resolver y cuánto varía su media entre trimestres",
               "Tabla: en 2 000 incidentes sintéticos la media del tiempo hasta resolver es 73,5 minutos, la mediana 58,9, el percentil 90 es 125,6 y el 99 es 259,8; el diagnóstico aporta 40,6 minutos de la media; la media de un trimestre de 30 incidentes varía de 59,9 a 91,1 minutos sin cambiar la práctica; reducir a la mitad la mediana del diagnóstico baja la media a 53,6 minutos.",
               ["Medida", "Resultado"], rows, [400, 520], row_h=64, size=12,
               note="Comparar la media de dos trimestres con 30 incidentes cada uno confunde azar y mejora: la diferencia entre p5 y p95 (31 minutos) es mayor que la mejora que produce adelantar la detección. Las medianas y dispersiones de cada tramo son supuestos del autor, no mediciones.",
               note_kind="gold", foot=SINT)


def se428_actualizaciones() -> Fig:
    r = e428_actualizaciones()
    rows = [[x["política"].capitalize(), n(x["preguntas por incidente"], 1), n(x["actualizaciones"], 1), n(x["minutos de la persona al mando"], 1) + " min"] for x in r["filas"]]
    return tab("Cadencia de actualizaciones de estado: preguntas que recibe la persona al mando según la política",
               "Tabla: sin cadencia la persona al mando recibe 32,9 preguntas por incidente y gasta 98,7 minutos entre responderlas; actualizar cada 30 minutos baja las preguntas a 10,1 y el gasto a 42,4 minutos, el mínimo; actualizar cada 5 minutos deja 6,1 preguntas y el gasto sube a 102,9 minutos por las 21,1 actualizaciones.",
               ["Política de actualización", "Preguntas por incidente", "Actualizaciones", "Minutos de la persona al mando"], rows, [260, 210, 180, 270], row_h=44, size=13,
               note="Hay una cadencia que minimiza el coste y no es la más frecuente: cada actualización cuesta 4 minutos y cada pregunta 3. La tasa de preguntas que crece con la antigüedad de la última noticia y la duración mediana de 90 minutos son supuestos del autor; el óptimo real depende de a quién se informa y de cómo.",
               note_kind="teal", foot=SINT)


def se428_severidad() -> Fig:
    r = e428_severidad()
    rows = [[x["criterio"], n(x["kappa medio"], 2), p(x["acuerdo con la verdad %"] / 100), p(x["error de 2 o más niveles %"] / 100)] for x in r["filas"]]
    return tab("Tres personas clasifican 400 incidentes en cuatro niveles de severidad con tres tipos de criterio",
               "Tabla: con criterios vagos el acuerdo entre personas medido con kappa de Cohen es 0,29 y se coincide con la severidad verdadera 57,8 por ciento de las veces; con umbrales numéricos de impacto sube a 0,61 y 80,1 por ciento; con umbrales y un ejemplo por nivel sube a 0,83 y 91,8 por ciento.",
               ["Criterio", "Kappa medio", "Acuerdo con la verdad", "Error de 2 o más niveles"], rows, [430, 130, 190, 170], row_h=52, size=13,
               note="La severidad que se declara en minutos de tensión depende de cómo se perciba el impacto: el ruido de percepción (0,9, 0,35 y 0,15 en escala logarítmica) es un supuesto del autor. Lo que importa es la dirección: un criterio medible convierte una opinión en una decisión que otra persona reproduce.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-429
def se429_recurrencia() -> Fig:
    r = e429_recurrencia()
    rows = [[f"{x['acciones completadas %']} % de las acciones completadas", n(x["año 1"], 1), n(x["año 2"], 1), n(x["año 3"], 1)] for x in r["filas"]]
    return tab("Incidentes por año tras tres años según el porcentaje de acciones correctivas que se completan",
               "Tabla: con 12 causas y unos 40 incidentes el primer año, completar 30 por ciento de las acciones deja 16,7 incidentes el segundo año y 11,2 el tercero; completar 60 por ciento deja 9,7 y 5,9; completar 90 por ciento deja 6,1 y 3,4.",
               ["Cumplimiento de las acciones", "Año 1", "Año 2", "Año 3"], rows, [400, 170, 170, 170], row_h=52, size=13,
               note="Cada acción completada reduce al 40 % la tasa de su causa (supuesto del autor) y la reduce una vez por incidente. La brecha entre 30 % y 90 % de cumplimiento es 3,3 veces en el tercer año: un postmortem cuyas acciones no se cierran enseña, pero no cambia el sistema.",
               note_kind="coral", foot=SINT)


def se429_cadena() -> Fig:
    r = e429_cadena()
    top = sorted(r["reparto de raíces"].items(), key=lambda x: -x[1])
    rows = [[f"Raíz declarada: {k}", f"{v} de 400 analistas", p(v / 400, 0)] for k, v in top]
    rows.append(["Factores contribuyentes que recorre una cadena de «cinco porqués»", p(r["cobertura media de una cadena %"] / 100), "De los 12 factores del grafo"])
    rows.append(["Factores cubiertos por cuatro analistas independientes", p(r["cobertura media de cuatro analistas %"] / 100), "Unión de cuatro cadenas"])
    return tab("Cinco porqués sobre un grafo de 12 factores: causas raíz distintas que declaran 400 analistas y fracción del grafo que ven",
               "Tabla: sobre el mismo grafo de 12 factores contribuyentes, 400 analistas que siguen cada uno una cadena de porqués declaran 6 causas raíz distintas; una cadena recorre en promedio 24 por ciento de los factores y cuatro analistas independientes cubren 61,3 por ciento.",
               ["Resultado", "Frecuencia", "Contexto"], rows, [490, 210, 220], row_h=44, size=12,
               note="Una cadena lineal sobre un sistema con causas que convergen produce una causa raíz que depende de qué rama se eligió primero, no de qué pasó. El grafo (un síntoma, 12 factores y 12 aristas) es un caso construido por el autor para la clase; su forma, no sus nombres, es el punto.",
               note_kind="gold", foot=SINT)


def se429_linter() -> Fig:
    r = e429_linter()
    rows = [[x["mutación"].capitalize(), f"{x['detectadas']} de {x['de']}", "Lo ve la forma" if x["detectadas"] else "Pasa el verificador"] for x in r["filas"]]
    return tab("Un verificador de postmortems frente a 180 mutaciones (nueve operadores sobre veinte documentos cada uno)",
               f"Tabla: un verificador de lenguaje de culpa explícito, cifras de impacto, horas en la línea de tiempo, dos factores como mínimo y propietario y verificación de cada acción detecta {r['detectadas']} de 180 mutaciones; detecta 20 de 20 de la culpa explícita, la acción sin propietario, el impacto sin cifras, la línea sin hora y la causa única, y 0 de 20 de la culpa implícita, la acción vaga con verificación débil, la hora inventada y la acción desproporcionada.",
               ["Mutación", "Detectadas", "Resultado"], rows, [500, 130, 290], row_h=40, size=12,
               note=f"Detecta {r['detectadas']} de {r['total']} ({p(r['detectadas'] / r['total'], 0)}). Un documento que pasa el verificador puede culpar sin nombrar a nadie («como siempre, el turno de noche…») y proponer acciones que nadie podrá comprobar. Medir la forma de un postmortem es medir su limpieza, no su calidad.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-430
def se430_rpo() -> Fig:
    r = e430_rpo()
    rows = [[x["estrategia"].capitalize(), f"{n(x['pérdida mediana min'], 1)} min", f"{n(x['p99 min'], 1)} min", f"{n(x['máxima min'], 1)} min", p(x["incumple RPO de 5 min %"] / 100)] for x in r["filas"]]
    return tab("Datos perdidos al fallar en un instante aleatorio según la estrategia de copia y réplica frente a un RPO de 5 minutos",
               "Tabla: con copia diaria la pérdida mediana es 719,7 minutos y el máximo 1 440; con copia cada hora la mediana es 30 y el máximo 60; una réplica asíncrona con retraso mediano de 2 segundos pierde una mediana de 0,03 minutos y en el peor caso 5, con 1 por ciento de picos de entre 10 y 300 segundos; un RPO de 5 minutos lo incumple el 99,6 por ciento de las fallas con copia diaria y ninguna con la réplica.",
               ["Estrategia", "Pérdida mediana", "p99", "Máxima", "Incumple RPO de 5 min"], rows, [330, 140, 120, 130, 200], row_h=52, size=12,
               note="El RPO real de una copia periódica es su intervalo, no la mediana; el de una réplica es el peor retraso, no el habitual, y una réplica también copia los errores (un borrado). 20 000 fallas por estrategia; el retraso con 1 % de picos es un supuesto del autor.",
               note_kind="gold", foot=SINT)


def se430_copias() -> Fig:
    rows = [
        ["El trabajo de copia terminó sin error", "0 de 40", "Dice que escribió, no que sirve"],
        ["El tamaño del archivo coincide", "0 de 40", "Los bytes alterados no cambian el tamaño"],
        ["Huella sha256 distinta de la registrada", "40 de 40", "Detecta cualquier cambio"],
        ["PRAGMA integrity_check", "20 de 40", "Solo ve daños en la estructura"],
        ["COUNT(*) de la tabla", "0 de 40", "Cuenta filas, no contenido"],
        ["Leer y comprobar todas las filas", "40 de 40", "Ve el daño en el contenido de esta prueba"],
    ]
    return tab("Cuarenta copias dañadas de una base de 20 000 filas: qué comprobación detecta cada daño",
               "Tabla: se altera en ocho posiciones cada una de 40 copias de una base SQLite de 20 000 filas y 2 797 568 bytes; el éxito del trabajo de copia y el tamaño detectan 0 de 40, la huella sha256 detecta 40, el chequeo de integridad de SQLite detecta 20, contar las filas detecta 0 y leer y comprobar todas las filas detecta 40.",
               ["Comprobación", "Daños detectados", "Lectura"], rows, [380, 190, 350], row_h=44, size=13,
               note="La copia buena se creó con la API de copia en línea de SQLite y restauró las 20 000 filas con integrity_check «ok». Una copia que nadie restaura no es una copia: la huella detecta el cambio, y solo restaurar y consultar prueba que la base funciona. Medición real en Windows y Ubuntu con resultado igual; la lectura completa depende de que el daño invalide el texto.",
               note_kind="teal", foot=REAL)


def se430_dependencias() -> Fig:
    r = e430_dependencias()
    rows = []
    for x in r["filas"]:
        rows.append([x["conjunto"].capitalize(), f"{x['serie min']} min", "Ciclo: no arranca desde cero" if x["ciclo"] else f"{x['ruta crítica min']} min"])
    return tab("Restaurar 12 componentes desde cero: tiempo en serie, ruta crítica y dependencias que solo un ejercicio revela",
               "Tabla: restaurar 12 componentes uno a uno tarda 225 minutos y en paralelo respetando las dependencias, 125 minutos de ruta crítica; si la identidad necesita los secretos y los secretos necesitan la identidad hay un ciclo y no se puede arrancar desde cero; unas credenciales de emergencia fuera de línea de 20 minutos lo rompen y dejan 245 minutos en serie y 130 de ruta crítica.",
               ["Conjunto de dependencias", "Restauración en serie", "Ruta crítica"], rows, [450, 210, 260], row_h=52, size=13,
               note="El RTO de 125 minutos de una tabla de dependencias incompleta es una promesa vacía: el ejercicio encontró un ciclo y añadió 5 minutos a la ruta crítica. Los 12 componentes, sus duraciones y sus dependencias son un ejemplo del autor, no una medición de ningún sistema.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-431
def se431_ambiguedad() -> Fig:
    r = e431_ambiguedad()
    rows = [[str(x["señales ausentes"]), n(x["clases distinguibles (media de 10)"], 2), n(x["fallas identificables sin ambigüedad (media)"], 2), str(x["mayor grupo de fallas indistinguibles"]), n(x["combinaciones"])] for x in r["filas"]]
    return tab("Diez fallas posibles y doce señales: cuántas fallas se distinguen cuando faltan señales",
               "Tabla: con las 12 señales las 10 fallas se distinguen; si falta una cualquiera, 9,83 fallas se identifican sin ambigüedad en promedio; si faltan tres, 8,95 y hasta tres fallas pueden quedar indistinguibles; si faltan seis, 5,78 se identifican y hasta cinco fallas comparten la misma firma.",
               ["Señales ausentes", "Clases distinguibles", "Fallas sin ambigüedad", "Mayor grupo indistinguible", "Combinaciones"], rows, [160, 190, 210, 210, 150], row_h=44, size=13,
               note="La matriz de firmas (qué señal se desvía con cada falla) es del autor y trata cada señal como binaria; sirve para contar ambigüedades, no para estimar probabilidades. Lo que falta importa más que cuántas faltan: la combinación de señales ausentes decide qué fallas se confunden.",
               note_kind="gold", foot=SINT)


def se431_estrategias() -> Fig:
    r = e431_estrategias()
    rows = [[x["estrategia"].capitalize(), n(x["observaciones hasta aislar (media)"], 2), n(x["coste medio"], 2)] for x in r["filas"]]
    return tab("Cómo elegir la siguiente observación para aislar una falla entre diez: tres estrategias sobre 4 000 diagnósticos",
               "Tabla: elegir en cada paso la observación que mejor reparte las hipótesis restantes aísla la falla en 3,59 observaciones y coste 4,98; mirar primero lo más barato necesita 6,09 observaciones y coste 8,49; elegir al azar necesita 5,81 observaciones y coste 12,08.",
               ["Estrategia", "Observaciones hasta aislar", "Coste medio"], rows, [430, 270, 200], row_h=52, size=13,
               note="Lo más barato primero no es lo más informativo: mira señales que no separan hipótesis. Los costes de 1 a 4 por observación y la ausencia de ruido de medida son supuestos del autor; con medidas ruidosas hay que repetir observaciones y la ventaja de elegir bien se reduce.",
               note_kind="teal", foot=SINT)


def se431_perdida() -> Fig:
    r = e431_perdida()
    rows = [[x["modelo"].capitalize(), p(x["tasa de error real %"] / 100, 2), p(x["tasa observada en los registros %"] / 100, 2), p(x["líneas conservadas %"] / 100)] for x in r["filas"]]
    return tab("Tasa de error durante un incidente leída en registros cuando el agente pierde más líneas de error que de éxito",
               "Tabla: con 9 000 líneas de un incidente con 12,53 por ciento de errores reales, una pérdida igual para todas las líneas deja una tasa observada de 12,51 por ciento; si se pierde 25 por ciento de las líneas de error, la tasa observada baja a 10,2; si se pierde 50 por ciento, baja a 6,99 aunque se conserva 92,1 por ciento de las líneas.",
               ["Modelo de pérdida", "Tasa real", "Tasa observada", "Líneas conservadas"], rows, [430, 150, 170, 170], row_h=52, size=13,
               note="Se conserva más de 92 % de las líneas y la tasa de error se ve a la mitad: la pérdida depende de aquello que se mide. La telemetría falla justo cuando el sistema falla, y la ausencia de errores en los registros no prueba que no los haya habido. Los porcentajes de pérdida son supuestos del autor.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-432
def se432_validador() -> Fig:
    r = e432_validador()
    rows = [[x["mutación"].capitalize(), f"{x['detectadas']} de {x['de']}", "Lo ve la forma" if x["detectadas"] else "Pasa el validador"] for x in r["filas"]]
    return tab("Un validador de paquetes operativos frente a 360 mutaciones (doce operadores, treinta paquetes cada uno)",
               f"Tabla: un validador de referencias cruzadas entre servicios, objetivos, alertas, runbooks, copias y ejercicios detecta {r['detectadas']} de 360 mutaciones; detecta 30 de 30 de siete operadores, entre ellos el servicio sin SLO, la alerta sin runbook, la restauración sin probar y el escalamiento de un nivel, y 0 de 30 del objetivo laxo pero en rango, el RPO incoherente, el ejercicio sin hallazgos, los runbooks intercambiados y el SLI que no mide al usuario.",
               ["Mutación", "Detectadas", "Resultado"], rows, [480, 130, 310], row_h=36, size=12,
               note=f"Detecta {r['detectadas']} de {r['total']} ({p(r['detectadas'] / r['total'], 0)}), todas por referencias rotas o fechas vencidas. Ninguna de las cinco clases que se escapan viola el formato: son errores de significado. Un paquete coherente consigo mismo no es un sistema operable; los doce operadores y el paquete base son construcciones del autor.",
               note_kind="coral", foot=SINT)


def se432_reproducibilidad() -> Fig:
    rows = [
        ["Huella de los resultados de tiempo virtual", "b3d17854ae65d56a", "b3d17854ae65d56a", "Idénticas"],
        ["Separador de línea del sistema", "\\r\\n", "\\n", "Distinto"],
        ["Bytes de «línea» más salto escritos como texto", "8", "7", "Distinto"],
        ["Caracteres al leer con la codificación local", "7", "6", "Distinto (en Windows se lee con cp1252)"],
        ["Separador de rutas", "\\", "/", "Distinto"],
        ["Mayúsculas y minúsculas distintas en una ruta", "No", "Sí", "Distinto"],
        ["Nombre de archivo con eñe conservado", "Sí", "Sí", "Idéntico"],
    ]
    return tab("Mismo código, dos sistemas: qué se reproduce y qué cambia en Windows 11 y Ubuntu bajo WSL2",
               "Tabla: los resultados de tiempo virtual del paquete operativo tienen la misma huella b3d17854ae65d56a en Windows 11 con CPython 3.12.9 y en Ubuntu con 3.12.3; el separador de línea, los bytes escritos como texto, la lectura con la codificación local, el separador de rutas y la distinción de mayúsculas en rutas cambian entre los dos sistemas.",
               ["Sonda", "Windows 11", "Ubuntu (WSL2)", "Resultado"], rows, [360, 170, 170, 220], row_h=52, size=12,
               note="Un resultado calculado con semilla fija se reproduce en cualquier sistema; todo lo que toca el sistema de archivos o la codificación cambia. Declarar la codificación (utf-8) en cada lectura y escritura evita el caso del texto leído con otra. Medición real de los dos sistemas; la huella cubre tres experimentos del paquete.",
               note_kind="gold", foot=REAL)


def se432_cadena() -> Fig:
    r = e432_cadena()
    names = list(r["fallos por etapa %"])
    rows = [[k.capitalize(), p(r["fallos por etapa %"][k] / 100), p(r["mejorar 5 puntos la etapa (producto %)"][k] / 100)] for k in names]
    rows.append(["Recuperación completa", f"Producto de etapas {p(r['producto de las etapas %'] / 100)}", f"Simulada {p(r['recuperación completa simulada %'] / 100)}"])
    return tab("Una respuesta a incidentes de cinco etapas: dónde se pierde y cuánto sube la recuperación completa al mejorar cada etapa 5 puntos",
               "Tabla: con cinco etapas de 95, 92, 80, 88 y 90 por ciento de éxito, el producto es 55,4 por ciento y la simulación de 20 000 incidentes con un 5 por ciento de caídas de telemetría que afectan a la detección y al diagnóstico da 52,8; el diagnóstico concentra 17,7 por ciento de los fallos y mejorarlo cinco puntos lleva el producto a 58,8, frente a 57,7 al mejorar la detección.",
               ["Etapa", "Incidentes que fallan aquí", "Producto si se mejora 5 puntos"], rows, [380, 260, 280], row_h=44, size=13,
               note="Una cadena de etapas buenas por separado se recupera menos de una de cada dos veces a lo largo del año, y la mejora más rentable está en la etapa más débil, no en la más visible. Las probabilidades por etapa y la dependencia por la telemetría son supuestos del autor.",
               note_kind="teal", foot=SINT)


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
