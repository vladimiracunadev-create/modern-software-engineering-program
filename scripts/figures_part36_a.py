"""Figures for SE-433 to SE-437 (synthetic data, fixed seeds, virtual time; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3).

Every figure but the first is a chart of the same measured numbers; the Markdown tables of the classes keep the exact values.
"""
from __future__ import annotations

from figure_kit import Fig, dumbbell, fmt_es, grouped_bars, line_chart, percentile_intervals, stacked_bars
from figures_part07_a import bars

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."


# ---------------------------------------------------------------- SE-433
def se373_cola() -> Fig:
    items = [
        ("Mediana", 121.0, "teal", "121 ms"),
        ("Media", 157.0, "teal", "157 ms"),
        ("p95", 225.0, "gold", "225 ms"),
        ("p99", 1929.0, "coral", "1 929 ms"),
        ("p99,9", 2908.0, "coral", "2 908 ms"),
        ("Máximo", 2996.0, "coral", "2 996 ms"),
    ]
    return bars("Latencia de 20 000 peticiones sintéticas: lo que dicen la media y los percentiles",
                "Barras: con una cola lenta del 1,5 por ciento de las peticiones, la mediana es 121 milisegundos, la media 157, el percentil 95 es 225, el percentil 99 sube a 1 929, el 99,9 a 2 908 y el máximo a 2 996.",
                items, 0.18, "El 98,5 % de las peticiones sigue una distribución de mediana 120 ms y el 1,5 % restante tarda entre 1,5 y 3 s. La media se mueve 36 ms y no delata nada; el p95 tampoco; el p99 sí. Un requisito que nombre solo la media o el p95 deja sin proteger a 1 de cada 73 peticiones.",
                label_w=150, width=940, note_kind="coral", foot=SINT)


def se373_mes() -> Fig:
    return grouped_bars(
        "Un mismo mes de 60 000 peticiones medido con cuatro definiciones frente al objetivo de 300 ms",
        "Barras horizontales con el valor que cada definición compara con el objetivo de 300 milisegundos: la media de las medias diarias da 161, el percentil 95 del mes 227, el percentil 99 del mes 2 057 y el percentil 95 del día 17 con tres horas lentas 2 294; solo las dos primeras quedan bajo la línea del objetivo.",
        ["Media de las medias diarias", "p95 de todas las peticiones del mes", "p99 del mes", "p95 del día 17 (tres horas con 60 % de peticiones lentas)"],
        [("Valor medido", [161, 227, 2057, 2294], "navy")],
        unit="Milisegundos (ms)", horizontal=True, label_w=300, ref_lines=[(300, "Objetivo: 300 ms")], ticks=[0, 500, 1000, 1500, 2000, 2500],
        note="El objetivo es el mismo número y las definiciones llegan a conclusiones opuestas. Agregar el mes entero diluye un incidente de tres horas porque 59 de cada 60 peticiones fueron normales; exigir el p95 en cada día falla el día 17 (29 de 30 días cumplen). La definición forma parte del requisito: ventana, estadístico y alcance.",
        note_kind="gold", foot=SINT)


def se373_linter() -> Fig:
    names = ["Quitar el número de la medida", "Sustituirlo por «rápido» o «razonable»", "Quitar el estadístico (p95, máximo…)",
             "Dejar el entorno vacío", "Entorno vago («carga normal»)", "Cambiar la unidad (ms por s, s por min)",
             "Umbral igual a 0", "Rebajar el percentil a p50", "Estímulo copiado de otro escenario"]
    hit = [20, 20, 20, 20, 20, 6, 0, 0, 0]
    return stacked_bars(
        "Un verificador de forma de escenarios de calidad frente a 180 mutaciones (nueve operadores de 20)",
        "Barras apiladas horizontales con las mutaciones detectadas de 20 por cada operador: las cinco que quitan, vacían o vuelven vago un campo se detectan 20 de 20, el cambio de unidad 6 de 20 y las tres que conservan la forma, umbral cero, percentil más débil y estímulo ajeno, 0 de 20; el verificador solo ve la forma.",
        names, [("Detectadas", hit, "teal"), ("No detectadas", [20 - h for h in hit], "coral")],
        unit="Mutaciones de 20 por operador", horizontal=True, label_w=300,
        note="Detecta 106 de 180 mutaciones (59 %). Todo lo que ve es forma; ninguna de las 74 que se escapan viola el formato. Un escenario bien formado y falso es peor que uno ausente porque parece medido. Las diez bases y los operadores son construcciones del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-434
def se374_reglas() -> Fig:
    return grouped_bars(
        "Tres reglas de análisis estático con ast sobre 300 funciones generadas con defectos conocidos",
        "Barras agrupadas con los defectos reales, los hallados y las falsas alarmas antes y después de afinar para cuatro clases de defecto: las tres reglas halladoras encuentran todos los suyos (44, 60 y 37), dejan 18, 40 y 53 falsas alarmas que la afinación baja a 18, 0 y 26, y el recorrido que omite el primer elemento tiene 70 defectos y ninguno hallado.",
        ["Argumento por defecto mutable", "Excepción sin tipo (bare except)", "Variable local sin uso", "Recorrido que omite el primer elemento"],
        [("Defectos reales", [44, 60, 37, 70], "navy"), ("Hallados", [44, 60, 37, 0], "teal"),
         ("Falsas alarmas sin afinar", [18, 40, 53, 0], "coral"), ("Falsas alarmas afinadas", [18, 0, 26, 0], "gold")],
        unit="Defectos o alertas", plot_h=260,
        note="Encontrar el 100 % de lo que busca no es calidad: la regla afinada deja 18 + 26 falsas alarmas y su precisión es del 71 % para argumentos mutables y del 59 % para variables sin uso. Afinar la excepción con los mismos casos que evalúan la regla es un sesgo declarado. El defecto lógico (70) queda fuera de cualquier regla sintáctica.",
        note_kind="gold", foot=SINT)


def se374_compuerta() -> Fig:
    return grouped_bars(
        "Tres compuertas de cobertura sobre 500 cambios que se fusionan en un repositorio de 20 000 líneas al 72 %",
        "Barras agrupadas con los dos errores de cada compuerta: la cobertura total mínima del 70 por ciento deja pasar los 117 cambios con pruebas pobres y no bloquea ninguno bueno; la cobertura total que no baje y la cobertura del cambio al 80 por ciento no dejan pasar ninguno pobre, y la segunda bloquea 1 de 193 cambios bien probados.",
        ["Cobertura total ≥ 70 %", "La cobertura total no baja", "Cobertura de las líneas del cambio ≥ 80 %"],
        [("Cambios pobres que pasan (de 117)", [117, 0, 0], "coral"), ("Cambios bien probados que se bloquean (de 193)", [0, 0, 1], "gold")],
        unit="Cambios", plot_h=240,
        note="El repositorio crece de 20 000 a 118 813 líneas y la cobertura total termina en 73,1 %: cada cambio mueve el total menos de 0,1 punto, así que un umbral absoluto no ve a ninguno. «Pobre» significa que la calidad real de las pruebas es menor del 60 %; la cobertura mide líneas ejecutadas, no aserciones.",
        note_kind="teal", foot=SINT)


def se374_espurios() -> Fig:
    xs = [1, 5, 10, 20, 40]
    first = [2.1, 9.4, 18.4, 33.5, 55.9]
    third = [0.01, 0.11, 0.61, 3.52, 17.14]
    return line_chart(
        "Bloqueos espurios al encadenar comprobaciones que fallan solas el 2 % de las veces",
        "Líneas con la fracción de cambios bloqueados por ruido según el número de comprobaciones encadenadas: al primer intento sube de 2,1 por ciento con una a 55,9 con cuarenta; con hasta tres intentos baja a 0,01, 0,11, 0,61, 3,52 y 17,14, pero un defecto detectado el 90 por ciento de las veces se cuela en el 27,3 por ciento de los casos en lugar del 10.",
        [("Bloqueo al primer intento", [(x, v) for x, v in zip(xs, first)], "coral"),
         ("Bloqueo tras hasta 3 intentos", [(x, v) for x, v in zip(xs, third)], "teal")],
        x_label="Comprobaciones encadenadas", y_label="Cambios bloqueados por ruido (%)", log_y=True,
        x_ticks=[(1, "1"), (5, "5"), (10, "10"), (20, "20"), (40, "40")], y_ticks=[0.01, 0.1, 1, 10, 100],
        point_labels="all", plot_h=290,
        note="Reintentar hasta ponerse en verde elimina el ruido y también la señal: un defecto que la comprobación detecta el 90 % de las veces pasa en el 27,3 % de los casos tras tres intentos, frente al 10,0 % con un intento. La corrección es hacer determinista la comprobación o separar «inestable» de «falla», no ampliar los intentos.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-435
def se375_pruebas() -> Fig:
    return line_chart(
        "Rampa de estrés sobre el sistema sintético: percentil 95 según la carga (4 servidores, capacidad nominal de 80 req/s)",
        "Líneas con el percentil 95 según la carga ofrecida: la prueba de carga estable a 60 solicitudes por segundo da 202 milisegundos, y la rampa de estrés da 288 a 68, 357 a 77 y 1 718 a 86 solicitudes por segundo con 32,7 por ciento de fallos, por encima de la capacidad nominal de 80; el codo está entre 68 y 86 y la carga estable no lo muestra.",
        [("Rampa de estrés", [(68, 288, "288 ms", "t"), (77, 357, "357 ms", "t"), (86, 1718, "1 718 ms · 32,7 % fallos", "l")], "coral"),
         ("Carga estable a 60 req/s", [(60, 202, "202 ms", "b")], "teal")],
        x_label="Solicitudes por segundo ofrecidas", y_label="p95 (ms)", log_y=True,
        x_ticks=[(60, "60"), (68, "68"), (77, "77"), (86, "86")], y_ticks=[100, 1000, 10000],
        vlines=[(80, "Capacidad nominal 80 req/s")], point_labels="none", plot_h=280,
        note="Cada forma de carga responde a una pregunta distinta y ninguna sustituye a otra: la carga estable no dice dónde está el límite; el pico de 20 s a 240 req/s deja 165 s de recuperación y la fuga de una conexión cada 5 000 solicitudes solo agota el pool a los 67 min. El colapso de la rampa (100 % de fallos después) no es un defecto del algoritmo de cola: el servidor sigue atendiendo solicitudes cuyo cliente ya se rindió a los 2 s.",
        note_kind="gold", foot=SINT)


def se375_omision() -> Fig:
    return percentile_intervals(
        "Una pausa de 10 s del servidor a 40 req/s medida con tres generadores de carga",
        "Intervalos en escala logarítmica con la mediana, el percentil 99 y el percentil 99,9 de cada generador: el abierto tiene mediana de 45 milisegundos y percentil 99 de 9 071; el cerrado de 8 usuarios, 35 y solo 232; el cerrado con corrección de omisión coordinada, 38 y 8 600; el percentil 99,9 queda cerca de 10 000 en los tres.",
        [("Abierto: llegadas programadas, latencia desde la hora prevista", [45, 9071, 9848]),
         ("Cerrado: 8 usuarios virtuales que esperan la respuesta", [35, 232, 9916]),
         ("Cerrado con corrección de la omisión", [38, 8600, 9916])],
        unit="Milisegundos (ms)", marks=("p50", "p99", "p99,9"), log=True, label_w=250,
        note="El generador cerrado dejó de enviar mientras el servidor estaba parado, de modo que casi nadie llegó a esperar: el p99 pasa de 9 071 a 232 ms sin que el sistema haya cambiado. Solo 8 muestras de 5 438 cayeron en la pausa (7 117 muestras en el abierto; 10,51 % por encima de 1 s frente a 0,15 %). La corrección recupera una parte porque asume un intervalo esperado.",
        note_kind="coral", foot=SINT)


def se375_duracion() -> Fig:
    means = {(244, 378): "media 290", (268, 359): "media 301", (279, 343): "media 301", (609, 2724): "media 1 045",
             (266, 340): "media 300", (376, 1671): "media 904", (279, 321): "media 298"}
    return dumbbell(
        "p99 estimado en 30 repeticiones según la duración de la prueba y el calentamiento (60 req/s, 4 servidores)",
        "Intervalos en escala logarítmica con el mínimo y el máximo del percentil 99 en 30 repeticiones y su media al final de cada fila: sin calentamiento el rango se estrecha de 244 a 378 milisegundos con 30 segundos a 279 a 343 con 600; con caché fría los primeros 60 segundos, incluir el arranque da una media de 1 045 y un máximo de 2 724, y descartar los 120 primeros segundos lo devuelve a 300.",
        [("30 s, sin calentamiento", 244, 378), ("120 s, sin calentamiento", 268, 359), ("600 s, sin calentamiento", 279, 343),
         ("300 s, caché fría (todo)", 609, 2724), ("300 s, descartando los primeros 120 s", 266, 340),
         ("900 s, caché fría (todo)", 376, 1671), ("900 s, descartando los primeros 120 s", 279, 321)],
        unit="p99 en milisegundos (ms)", names=("Mínimo de 30 repeticiones", "Máximo de 30 repeticiones"), log=True, label_w=280,
        delta=lambda lo, hi: means[(lo, hi)],
        note="Una prueba más larga estrecha el intervalo (de 134 a 64 ms de rango), pero el sesgo mayor viene de mezclar el arranque con el régimen estable: 1 045 frente a 300 ms de media. Descartar un tramo exige decidirlo antes de ver el resultado y publicar cuánto se descartó.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-436
def se376_utilizacion() -> Fig:
    xs = [50, 70, 80, 90, 95, 99]
    mean_sim = [99, 165, 246, 481, 973, 6115]
    mean_th = [100, 167, 250, 500, 1000, 5000]
    p99_sim = [454, 754, 1132, 2098, 4165, 24286]
    p99_th = [461, 768, 1151, 2303, 4605, 23026]
    return line_chart(
        "Una cola M/M/1 de 50 ms de servicio medio: latencia simulada frente a teoría según la utilización",
        "Líneas en escala logarítmica con la latencia media y el percentil 99 simulados y teóricos según la utilización: la media simulada pasa de 99 milisegundos al 50 por ciento a 481 al 90 y 6 115 al 99, y el percentil 99 de 454 a 2 098 y 24 286; simulación y teoría coinciden entre el 50 y el 80 por ciento y se separan al 90, 95 y 99.",
        [("Media simulada", list(zip(xs, mean_sim)), "teal"), ("Media teórica", list(zip(xs, mean_th)), "grey"),
         ("p99 simulado", list(zip(xs, p99_sim)), "coral"), ("p99 teórico", list(zip(xs, p99_th)), "gold")],
        x_label="Utilización del servidor (%)", y_label="Latencia (ms)", log_y=True,
        x_ticks=[(50, "50"), (70, "70"), (80, "80"), (90, "90"), (95, "95"), (99, "99")], y_ticks=[100, 1000, 10000, 100000],
        point_labels="none", plot_h=300,
        note="El crecimiento no es lineal: del 90 al 99 % la media se multiplica por 12. La simulación de 400 000 llegadas se aparta de la teoría cerca del 100 % porque el régimen estable tarda mucho en alcanzarse; 400 000 llegadas no bastan al 99 %. Con llegadas de Poisson y servicio exponencial; un sistema real no cumple ninguna de las dos.",
        note_kind="gold", foot=SINT)


def se376_variabilidad() -> Fig:
    cv = [0.0, 1.0, 3.94, 12.13]
    return line_chart(
        "Mismo promedio de servicio (50 ms) y misma utilización (80 %) con cuatro formas de variabilidad",
        "Líneas con la espera media y el percentil 99 según el cuadrado del coeficiente de variación del servicio: la espera simulada sube de 101 milisegundos con servicio constante a 203 con exponencial, 502 con lognormal y 1 364 con una mezcla de 95 por ciento rápida y 5 por ciento lenta, casi sobre la fórmula teórica, y el percentil 99 de 573 a 7 053.",
        [("Espera media simulada", [(x, y, f"{y:,}".replace(",", " "), "b") for x, y in zip(cv, [101, 203, 502, 1364])], "teal"),
         ("Espera media teórica", list(zip(cv, [100, 200, 495, 1317])), "grey"),
         ("p99 de la latencia", [(x, y, f"{y:,}".replace(",", " "), "t") for x, y in zip(cv, [573, 1160, 3617, 7053])], "coral")],
        x_label="cv² observado: 0 constante · 1 exponencial · 3,94 lognormal · 12,13 mezcla 95 % rápida y 5 % lenta", y_label="Milisegundos (ms)",
        x_ticks=[(0, "0"), (1, "1"), (3.94, "3,94"), (12.13, "12,13")],
        y_ticks=[0, 2000, 4000, 6000, 8000], point_labels="none", plot_h=300,
        note="La fórmula de Pollaczek–Khinchine acierta y dice lo importante: la espera crece con (1 + cv²). Con un 5 % de solicitudes lentas el sistema espera 13 veces más que con servicio constante, aunque el promedio no cambie. La ley de Little se cumple en los cuatro casos: es una identidad que detecta una instrumentación inconsistente, no una predicción.",
        note_kind="teal", foot=SINT)


def se376_agregar() -> Fig:
    return grouped_bars(
        "Servidores necesarios para 1 000 req/s según el objetivo de cola (M/M/1, 50 ms de servicio)",
        "Barras horizontales con los servidores que exige cada objetivo de percentil 99: 216 con 300 milisegundos (utilización del 23 por ciento), 93 con 500, 65 con 1 segundo y 57 con 2 segundos, frente a 63 al planificar con la media al 80 por ciento; exigir un percentil en lugar de la media multiplica la flota por 3,4.",
        ["p99 ≤ 300 ms (utilización 23 %)", "p99 ≤ 500 ms (54 %)", "p99 ≤ 1 s (77 %)", "p99 ≤ 2 s (88 %)", "Planificar con la media (80 %)"],
        [("Servidores", [216, 93, 65, 57, 63], "navy")],
        unit="Servidores para 1 000 solicitudes por segundo", horizontal=True, label_w=250, ticks=[0, 50, 100, 150, 200, 250],
        note="Exigir un percentil, no una media, multiplica por 3,4 la flota: la elección del estadístico es una decisión de costo. Aparte, agregar percentiles es un error: el promedio simple de los p99 de 8 servidores da 345 ms, el ponderado 262, el máximo 983 y solo el p99 de las muestras unidas (323 ms) es correcto; un servidor lento con poco tráfico mueve el promedio simple 22 ms por encima.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-437
def se377_variacion() -> Fig:
    return percentile_intervals(
        "La misma función (ordenar 20 000 enteros) medida 30 veces en cinco procesos nuevos de Windows 11",
        "Intervalos con el mínimo, la mediana y el máximo de 30 mediciones por proceso: las medianas van de 5,49 a 11,04 milisegundos, una razón de 2,01 entre procesos, y el máximo supera de 1,66 a 3,03 veces el mínimo dentro de cada uno; el proceso 3 tiene la mediana más alta y el 1 el máximo de 18,06.",
        [("Proceso 1", [5.97, 7.10, 18.06]), ("Proceso 2", [6.00, 7.11, 11.48]), ("Proceso 3", [5.75, 11.04, 15.37]),
         ("Proceso 4", [4.06, 5.73, 7.52]), ("Proceso 5", [3.85, 5.49, 6.42])],
        unit="Milisegundos (ms)", marks=("mínimo", "mediana", "máximo"), decimals=2, label_w=120,
        note="La variación entre procesos (medianas con razón 2,01) supera a la variación que una mejora típica querría detectar. En Ubuntu las medianas de cinco procesos van de 3,97 a 5,18 ms. Ninguna de estas cifras es reproducible al milisegundo; sí lo es la conclusión de que una sola medición no basta. Equipo, versión y carga de fondo del sistema no se controlaron.",
        note_kind="coral", foot=REAL)


def se377_perfilador() -> Fig:
    ratios = {(43.7, 199.9): "× 4,6", (26.9, 98.7): "× 3,7", (69.49, 0.050): "1 395 × menos", (68.64, 0.026): "2 599 × menos",
              (69.49, 68.80): "casi igual", (68.64, 50.93): "−26 %"}
    return dumbbell(
        "El perfilador cambia lo que mide y una caché puede estar midiéndose a sí misma",
        "Puntos unidos en escala logarítmica con el tiempo sin y con cambio: cProfile multiplica por 4,6 el tiempo de 300 000 llamadas mínimas en Windows y por 3,7 en Ubuntu; repetir la misma clave con caché baja 300 llamadas caras de 69 a 0,05 milisegundos, 1 395 veces menos, mientras que con claves distintas apenas cambian.",
        [("300 000 llamadas mínimas · cProfile, Windows", 43.7, 199.9), ("300 000 llamadas mínimas · cProfile, Ubuntu", 26.9, 98.7),
         ("300 llamadas caras · caché, misma clave, Windows", 69.49, 0.050), ("300 llamadas caras · caché, misma clave, Ubuntu", 68.64, 0.026),
         ("300 llamadas caras · caché, claves distintas, Windows", 69.49, 68.80), ("300 llamadas caras · caché, claves distintas, Ubuntu", 68.64, 50.93)],
        unit="Milisegundos (ms)", names=("Sin perfilador / sin caché", "Con cProfile / con caché"), log=True, label_w=330,
        delta=lambda a, b: ratios[(a, b)],
        note="Un perfil determinista cuenta llamadas con precisión y altera el reparto del tiempo (atribuye el 34 % a la función mínima cuando midiendo con y sin la llamada es el 46 %). El benchmark con caché de una sola clave mide una búsqueda en diccionario, no el trabajo: 1 395 veces menos con la misma clave y casi igual con claves distintas en Windows.",
        note_kind="gold", foot=REAL)


def se377_aa() -> Fig:
    media = [(58.8, 64, "3", "t"), (60.4, 64, "5", "b"), (58.0, 64, "10", "b"), (39.5, 72, "30", "t")]
    mediana = [(48.6, 67, "3", "t"), (37.7, 72, "5", "t"), (18.6, 79, "10", "t"), (2.8, 92, "30", "r")]
    minimo = [(48.9, 66, "3", "r"), (43.7, 69, "5", "r"), (36.0, 71, "10", "b"), (27.5, 77, "30", "t")]
    return line_chart(
        "Comparar dos copias idénticas: falsas diferencias frente a detección de una regresión real del 5 %",
        "Líneas con una serie por estadístico con 3, 5, 10 y 30 repeticiones por versión: la media se queda en 58 a 60 por ciento de falsas diferencias entre copias idénticas con 3 a 10 repeticiones y detecta 64 por ciento; la mediana baja de 48,6 a 2,8 por ciento de falsas diferencias y sube de 67 a 92 por ciento de detección; el mínimo queda en medio.",
        [("Media", media, "coral"), ("Mediana", mediana, "teal"), ("Mínimo", minimo, "gold")],
        x_label="Falsas diferencias de más del 3 % entre copias idénticas (%)", y_label="Detección de una regresión real del 5 % (%)",
        point_labels="all", plot_h=300, y_zero=False,
        note="Cada punto está rotulado con las repeticiones por versión (3, 5, 10 o 30); lo mejor es arriba a la izquierda, con pocas falsas diferencias y mucha detección. Con 5 repeticiones y la media, dos programas idénticos «difieren» el 60 % de las veces. La mediana es robusta a las interferencias y mejora con las repeticiones; el mínimo reduce el ruido pero también la señal. El ruido (lognormal de 4 %, 8 % de interferencias de +15 a +80 %) es un supuesto del autor.",
        note_kind="coral", foot=SINT)


FIGURES = {
    "se-433-la-media-oculta-la-cola.svg": se373_cola,
    "se-433-un-mes-seis-definiciones.svg": se373_mes,
    "se-433-verificador-de-escenarios.svg": se373_linter,
    "se-434-reglas-de-analisis-estatico.svg": se374_reglas,
    "se-434-compuertas-de-cobertura.svg": se374_compuerta,
    "se-434-bloqueos-espurios.svg": se374_espurios,
    "se-435-cuatro-pruebas-un-sistema.svg": se375_pruebas,
    "se-435-omision-coordinada.svg": se375_omision,
    "se-435-duracion-y-calentamiento.svg": se375_duracion,
    "se-436-latencia-segun-la-utilizacion.svg": se376_utilizacion,
    "se-436-variabilidad-del-servicio.svg": se376_variabilidad,
    "se-436-agregar-percentiles-y-capacidad.svg": se376_agregar,
    "se-437-variacion-entre-procesos.svg": se377_variacion,
    "se-437-perfilador-y-cache.svg": se377_perfilador,
    "se-437-copias-identicas-que-difieren.svg": se377_aa,
}
