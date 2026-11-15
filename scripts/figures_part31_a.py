"""Figures for SE-373 to SE-377 (synthetic data, fixed seeds, virtual time; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."


# ---------------------------------------------------------------- SE-373
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
    rows = [
        ["Media de las medias diarias", "161 ms", "Cumple"],
        ["p95 de todas las peticiones del mes", "227 ms", "Cumple"],
        ["p95 de cada día (se exige en los 30)", "29 de 30 días", "No cumple: falla el día 17"],
        ["p95 del día 17 (tres horas con 60 % de peticiones lentas)", "2 294 ms", "No cumple"],
        ["Fracción del mes por encima de 300 ms", "2,00 %", "Cumple si el margen es 5 %"],
        ["p99 del mes", "2 057 ms", "Sin objetivo: la cola existe y nadie la pide"],
    ]
    return tab("Un mismo mes de 60 000 peticiones medido con seis definiciones del objetivo «p95 ≤ 300 ms»",
               "Tabla: con la misma ventana de 30 días, la media de las medias diarias cumple con 161 milisegundos, el percentil 95 del mes cumple con 227, pero exigir el percentil 95 en cada día falla el día 17 con 2 294 milisegundos, y el percentil 99 del mes es de 2 057 milisegundos.",
               ["Definición de «cumple»", "Valor", "Veredicto"], rows, [430, 160, 330], row_h=52, size=13,
               note="El objetivo es el mismo número y las definiciones llegan a conclusiones opuestas. Agregar el mes entero diluye un incidente de tres horas porque 59 de cada 60 peticiones fueron normales. La definición forma parte del requisito: ventana, estadístico y alcance.",
               note_kind="gold", foot=SINT)


def se373_linter() -> Fig:
    rows = [
        ["Quitar el número de la medida", "20 de 20", "La forma lo delata"],
        ["Sustituirlo por «rápido» o «razonable»", "20 de 20", "La forma lo delata"],
        ["Quitar el estadístico (p95, máximo…)", "20 de 20", "La forma lo delata"],
        ["Dejar el entorno vacío", "20 de 20", "La forma lo delata"],
        ["Entorno vago («carga normal»)", "20 de 20", "Sin cifra no pasa"],
        ["Cambiar la unidad (ms por s, s por min)", "6 de 20", "Solo si deja la medida mal formada"],
        ["Umbral igual a 0", "0 de 20", "Forma correcta, valor absurdo"],
        ["Rebajar el percentil a p50", "0 de 20", "Forma correcta, exigencia menor"],
        ["Estímulo copiado de otro escenario", "0 de 20", "Forma correcta, contenido ajeno"],
    ]
    return tab("Un verificador de forma de escenarios de calidad frente a 180 mutaciones (nueve operadores)",
               "Tabla: un verificador que exige un estadístico, un número con unidad y un entorno con cifras detecta las cuatro mutaciones que quitan o vacían un campo y el entorno vago, 20 de 20 cada una; detecta 6 de 20 cambios de unidad y ninguna de las mutaciones que mantienen la forma, como umbral cero, percentil más débil o estímulo ajeno.",
               ["Mutación del escenario", "Detectadas", "Por qué"], rows, [400, 130, 390], row_h=40, size=13,
               note="Detecta 106 de 180 mutaciones (59 %). Todo lo que ve es forma; ninguna de las 74 que se escapan viola el formato. Un escenario bien formado y falso es peor que uno ausente porque parece medido. Las diez bases y los operadores son construcciones del autor.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-374
def se374_reglas() -> Fig:
    rows = [
        ["Argumento por defecto mutable", "44", "44", "18 (caché intencional)", "0"],
        ["Excepción sin tipo (bare except)", "60", "60", "40 → 0 con la excepción de «relanzar»", "0"],
        ["Variable local sin uso", "37", "37", "53 → 26 al ignorar el prefijo «_»", "0"],
        ["Recorrido que omite el primer elemento", "70", "0", "0", "70"],
    ]
    return tab("Tres reglas de análisis estático con ast sobre 300 funciones generadas con defectos conocidos",
               "Tabla: sobre 300 funciones con 161 con algún defecto, las tres reglas encuentran todos los defectos de su clase, pero producen 18 falsas alarmas de argumentos mutables, 40 de excepciones sin tipo que se reducen a cero con una excepción y 53 de variables sin uso que bajan a 26; ninguna regla ve los 70 recorridos que omiten el primer elemento.",
               ["Regla", "Defectos reales", "Hallados", "Falsas alarmas", "No vistos"], rows, [310, 130, 110, 270, 110], row_h=52, size=12,
               note="Encontrar el 100 % de lo que busca no es calidad: la regla afinada deja 18 + 26 falsas alarmas y su precisión es del 71 % para argumentos mutables y del 59 % para variables sin uso. Afinar la excepción con los mismos casos que evalúan la regla es un sesgo declarado. El defecto lógico (70) queda fuera de cualquier regla sintáctica.",
               note_kind="gold", foot=SINT)


def se374_compuerta() -> Fig:
    rows = [
        ["Cobertura total ≥ 70 %", "117 de 117", "0 de 193"],
        ["La cobertura total no baja", "0 de 117", "0 de 193"],
        ["Cobertura de las líneas del cambio ≥ 80 %", "0 de 117", "1 de 193"],
    ]
    return tab("Tres compuertas de cobertura sobre 500 cambios que se fusionan en un repositorio de 20 000 líneas al 72 %",
               "Tabla: la compuerta de cobertura total mínima del 70 por ciento deja pasar los 117 cambios con pruebas pobres; las compuertas de que la cobertura total no baje y de cobertura del cambio al 80 por ciento no dejan pasar ninguno; la del cambio bloquea a 1 de 193 cambios bien probados.",
               ["Compuerta", "Cambios con pruebas pobres que pasan", "Cambios bien probados que se bloquean"], rows, [390, 280, 270], row_h=52, size=13,
               note="El repositorio crece de 20 000 a 118 813 líneas y la cobertura total termina en 73,1 %: cada cambio mueve el total menos de 0,1 punto, así que un umbral absoluto no ve a ninguno. «Pobre» significa que la calidad real de las pruebas es menor del 60 %; la cobertura mide líneas ejecutadas, no aserciones.",
               note_kind="teal", foot=SINT)


def se374_espurios() -> Fig:
    rows = [
        ["1", "2,1 %", "0,01 %"],
        ["5", "9,4 %", "0,11 %"],
        ["10", "18,4 %", "0,61 %"],
        ["20", "33,5 %", "3,52 %"],
        ["40", "55,9 %", "17,14 %"],
        ["Defecto detectado el 90 % de las veces", "Se cuela el 10,0 %", "Se cuela el 27,3 %"],
    ]
    return tab("Bloqueos espurios al encadenar comprobaciones que fallan solas el 2 % de las veces",
               "Tabla: con comprobaciones que fallan solas el 2 por ciento de las veces, encadenar 10 bloquea el 18,4 por ciento de los cambios al primer intento y 40 el 55,9; permitir hasta tres intentos baja el bloqueo pero deja que un defecto detectado el 90 por ciento de las veces se cuele en el 27,3 por ciento de los casos en lugar del 10.",
               ["Comprobaciones encadenadas", "Bloqueo al primer intento", "Bloqueo tras hasta 3 intentos"], rows, [400, 270, 270], row_h=46, size=13,
               note="Reintentar hasta ponerse en verde elimina el ruido y también la señal: si la detección es intermitente, el defecto pasa en cuanto una ejecución sale verde. La corrección es hacer determinista la comprobación o separar «inestable» de «falla», no ampliar los intentos.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-375
def se375_pruebas() -> Fig:
    rows = [
        ["Carga: 60 req/s durante 5 min (75 % de utilización)", "n = 17 829; p50 57, p95 202, p99 285 ms; sin fallos", "No dice dónde está el límite"],
        ["Estrés: rampa de 20 a 160 req/s en 8 min", "p95 288 ms a 68/s; 357 ms a 77/s; 1 718 ms y 32,7 % de fallos a 86/s; después, 100 %", "Sin descartar trabajo vencido, 0 respuestas útiles por segundo (con descarte, 80,8)"],
        ["Pico: 240 req/s durante 20 s sobre 60 base", "Latencia máxima 41,4 s; 165 s para volver a p95 < 200 ms", "Un pico de 20 s deja 165 s de daño"],
        ["Resistencia: 60 req/s, fuga de 1 conexión cada 5 000", "En 5 min se pierden 3 de 50 conexiones; el pool se agota a los 67 min", "La prueba de 5 min no lo ve"],
    ]
    return tab("Cuatro pruebas sobre el mismo sistema sintético (4 servidores, 50 ms de servicio medio, capacidad nominal de 80 req/s)",
               "Tabla: la prueba de carga a 60 solicitudes por segundo no muestra límite; la rampa de estrés encuentra el codo entre 68 y 86 solicitudes por segundo y un colapso completo si el servidor sigue trabajando para clientes que ya se fueron; un pico de 20 segundos deja 165 segundos de recuperación; y una fuga de una conexión cada 5 000 solicitudes solo aparece a los 67 minutos.",
               ["Prueba", "Qué se observa", "Qué enseña o qué no ve"], rows, [300, 360, 280], row_h=84, size=12,
               note="Cada forma de carga responde a una pregunta distinta y ninguna sustituye a otra. El colapso de la rampa no es un defecto del algoritmo de cola: el servidor sigue atendiendo solicitudes cuyo cliente ya se rindió a los 2 s, así que cada respuesta llega tarde.",
               note_kind="gold", foot=SINT)


def se375_omision() -> Fig:
    rows = [
        ["Abierto: llegadas programadas, latencia desde la hora prevista", "7 117", "45 ms", "9 071 ms", "9 848 ms", "10,51 %"],
        ["Cerrado: 8 usuarios virtuales que esperan la respuesta", "5 438", "35 ms", "232 ms", "9 916 ms", "0,15 %"],
        ["Cerrado con corrección de la omisión", "5 827", "38 ms", "8 600 ms", "9 916 ms", "6,23 %"],
    ]
    return tab("Una pausa de 10 s del servidor a 40 req/s medida con tres generadores de carga",
               "Tabla: con una pausa de 10 segundos, el generador de lazo abierto registra 7 117 muestras y un percentil 99 de 9 071 milisegundos; el de lazo cerrado con 8 usuarios registra 5 438 muestras y un percentil 99 de solo 232 milisegundos; la corrección de omisión coordinada lo acerca a 8 600.",
               ["Generador", "Muestras", "p50", "p99", "p99,9", "> 1 s"], rows, [340, 100, 90, 120, 120, 100], row_h=64, size=12,
               note="El generador cerrado dejó de enviar mientras el servidor estaba parado, de modo que casi nadie llegó a esperar: el p99 pasa de 9 071 a 232 ms sin que el sistema haya cambiado. Solo 8 muestras de 5 438 cayeron en la pausa. La corrección recupera una parte porque asume un intervalo esperado.",
               note_kind="coral", foot=SINT)


def se375_duracion() -> Fig:
    rows = [
        ["30 s, sin calentamiento", "290 ms", "244 – 378 ms"],
        ["120 s, sin calentamiento", "301 ms", "268 – 359 ms"],
        ["600 s, sin calentamiento", "301 ms", "279 – 343 ms"],
        ["300 s, caché fría los primeros 60 s (todo)", "1 045 ms", "609 – 2 724 ms"],
        ["300 s, descartando los primeros 120 s", "300 ms", "266 – 340 ms"],
        ["900 s, caché fría (todo)", "904 ms", "376 – 1 671 ms"],
        ["900 s, descartando los primeros 120 s", "298 ms", "279 – 321 ms"],
    ]
    return tab("p99 estimado en 30 repeticiones según la duración de la prueba y el calentamiento (60 req/s, 4 servidores)",
               "Tabla: sin calentamiento, el percentil 99 estimado oscila entre 244 y 378 milisegundos con 30 segundos de prueba y entre 279 y 343 con 600; con 60 segundos de caché fría que enlentece un 30 por ciento, incluir el arranque lleva el percentil 99 medio a 1 045 milisegundos y descartar los 120 primeros segundos lo devuelve a 300.",
               ["Prueba", "p99 medio", "Mínimo – máximo en 30 repeticiones"], rows, [440, 170, 310], row_h=44, size=13,
               note="Una prueba más larga estrecha el intervalo (de 134 a 64 ms de rango), pero el sesgo mayor viene de mezclar el arranque con el régimen estable: 1 045 frente a 300 ms. Descartar un tramo exige decidirlo antes de ver el resultado y publicar cuánto se descartó.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-376
def se376_utilizacion() -> Fig:
    rows = [
        ["50 %", "99 / 100 ms", "297 ms", "454 / 461 ms"],
        ["70 %", "165 / 167 ms", "496 ms", "754 / 768 ms"],
        ["80 %", "246 / 250 ms", "733 ms", "1 132 / 1 151 ms"],
        ["90 %", "481 / 500 ms", "1 436 ms", "2 098 / 2 303 ms"],
        ["95 %", "973 / 1 000 ms", "2 901 ms", "4 165 / 4 605 ms"],
        ["99 %", "6 115 / 5 000 ms", "17 175 ms", "24 286 / 23 026 ms"],
    ]
    return tab("Una cola M/M/1 de 50 ms de servicio medio: latencia simulada frente a teoría según la utilización",
               "Tabla: con un servicio medio de 50 milisegundos, la latencia media pasa de 99 milisegundos al 50 por ciento de utilización a 481 al 90 y a más de 6 000 al 99; el percentil 99 simulado coincide con la fórmula entre el 50 y el 80 por ciento y se separa por debajo de la teoría al 90 y 95 por ciento y por encima al 99.",
               ["Utilización", "Media simulada / teoría", "p95 simulado", "p99 simulado / teoría"], rows, [180, 280, 200, 280], row_h=44, size=13,
               note="El crecimiento no es lineal: del 90 al 99 % la media se multiplica por 12. La simulación de 400 000 llegadas se aparta de la teoría cerca del 100 % porque el régimen estable tarda mucho en alcanzarse; 400 000 llegadas no bastan al 99 %. Con llegadas de Poisson y servicio exponencial; un sistema real no cumple ninguna de las dos.",
               note_kind="gold", foot=SINT)


def se376_variabilidad() -> Fig:
    rows = [
        ["Determinista (cv² = 0)", "0,00", "101 / 100 ms", "573 ms", "2,42 / 2,42"],
        ["Exponencial (cv² = 1)", "1,00", "203 / 200 ms", "1 160 ms", "4,06 / 4,06"],
        ["Lognormal (cv² = 4)", "3,94", "502 / 495 ms", "3 617 ms", "8,85 / 8,85"],
        ["Bimodal: 95 % 10 ms y 5 % 810 ms", "12,13", "1 364 / 1 317 ms", "7 053 ms", "22,67 / 22,67"],
    ]
    return tab("Mismo promedio de servicio (50 ms) y misma utilización (80 %) con cuatro formas de variabilidad",
               "Tabla: con la misma utilización del 80 por ciento y el mismo servicio medio, la espera media pasa de 101 milisegundos con servicio constante a 203 con exponencial, 502 con lognormal y 1 364 con una mezcla de 95 por ciento rápida y 5 por ciento lenta; la ley de Little se cumple en los cuatro casos.",
               ["Distribución del servicio", "cv² observado", "Espera media simulada / teoría", "p99 de la latencia", "L / λ·W"], rows, [300, 120, 230, 130, 140], row_h=52, size=12,
               note="La fórmula de Pollaczek–Khinchine acierta y dice lo importante: la espera crece con (1 + cv²). Con un 5 % de solicitudes lentas el sistema espera 13 veces más que con servicio constante, aunque el promedio no cambie. La ley de Little es una identidad: sirve para detectar una instrumentación inconsistente, no para predecir.",
               note_kind="teal", foot=SINT)


def se376_agregar() -> Fig:
    rows = [
        ["Promedio simple de los 8 p99", "345 ms", "Mezcla servidores con 12 000 y con 1 000 peticiones"],
        ["Promedio ponderado por peticiones", "262 ms", "Mejor, pero no es un percentil"],
        ["Máximo de los 8 p99", "983 ms", "Cota, no valor"],
        ["p99 de las muestras unidas", "323 ms", "El único resultado correcto"],
        ["Objetivo p99 ≤ 300 ms, cola M/M/1", "23 % de utilización; 216 servidores para 1 000 req/s", "Planificar con la media (80 %) da 63 servidores"],
        ["Objetivo p99 ≤ 500 ms", "54 %; 93 servidores", ""],
        ["Objetivo p99 ≤ 1 s", "77 %; 65 servidores", ""],
        ["Objetivo p99 ≤ 2 s", "88 %; 57 servidores", ""],
    ]
    return tab("Agregar percentiles de 8 servidores y planificar la capacidad con un objetivo de cola",
               "Tabla: promediar los percentiles 99 de ocho servidores da 345 milisegundos, el promedio ponderado 262, el máximo 983 y el percentil 99 de las muestras unidas 323; planificar 1 000 solicitudes por segundo con un objetivo de percentil 99 de 300 milisegundos exige 216 servidores al 23 por ciento de utilización, frente a 63 al planificar con la media al 80 por ciento.",
               ["Cálculo", "Resultado", "Lectura"], rows, [340, 330, 270], row_h=48, size=12,
               note="Un servidor lento con poco tráfico (983 ms con 1 000 peticiones) mueve el promedio simple 22 ms por encima del p99 real. Y exigir un percentil, no una media, multiplica por 3,4 la flota: la elección del estadístico es una decisión de costo.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-377
def se377_variacion() -> Fig:
    rows = [
        ["Proceso 1", "7,24 ms", "5,97 ms", "7,10 ms", "18,06 ms", "3,03"],
        ["Proceso 2", "7,12 ms", "6,00 ms", "7,11 ms", "11,48 ms", "1,91"],
        ["Proceso 3", "6,27 ms", "5,75 ms", "11,04 ms", "15,37 ms", "2,67"],
        ["Proceso 4", "5,57 ms", "4,06 ms", "5,73 ms", "7,52 ms", "1,85"],
        ["Proceso 5", "5,77 ms", "3,85 ms", "5,49 ms", "6,42 ms", "1,66"],
        ["Ubuntu (WSL2), 5 procesos", "—", "3,67 – 3,83", "3,97 – 5,18", "5,16 – 7,01", "1,35 – 1,85"],
    ]
    return tab("La misma función (ordenar 20 000 enteros) medida 30 veces en cinco procesos nuevos de Windows 11",
               "Tabla: cinco procesos de Python que miden 30 veces la misma ordenación de 20 000 enteros obtienen medianas entre 5,49 y 11,04 milisegundos en Windows, una razón de 2,01, y razones entre el máximo y el mínimo de 1,66 a 3,03 dentro de un mismo proceso; en Ubuntu las medianas van de 3,97 a 5,18.",
               ["Medición", "Primera", "Mínimo", "Mediana", "Máximo", "Máx / mín"], rows, [290, 120, 130, 130, 130, 120], row_h=46, size=12,
               note="La variación entre procesos (medianas con razón 2,01) supera a la variación que una mejora típica querría detectar. Ninguna de estas cifras es reproducible al milisegundo; sí lo es la conclusión de que una sola medición no basta. Equipo, versión y carga de fondo del sistema no se controlaron.",
               note_kind="coral", foot=REAL)


def se377_perfilador() -> Fig:
    rows = [
        ["300 000 llamadas a una función mínima, sin perfilador", "43,7 ms", "26,9 ms"],
        ["Las mismas con cProfile", "199,9 ms (× 4,6)", "98,7 ms (× 3,7)"],
        ["Parte del tiempo atribuida a la función mínima", "34 % (cProfile) frente a 46 % (con y sin la llamada)", "31 % frente a 39 %"],
        ["300 llamadas a una función cara, sin caché", "69,49 ms", "68,64 ms"],
        ["Con caché y la misma clave", "0,050 ms (1 395 × menos)", "0,026 ms (2 599 × menos)"],
        ["Con caché y claves distintas", "68,80 ms", "50,93 ms"],
    ]
    return tab("El perfilador cambia lo que mide y una caché puede estar midiéndose a sí misma",
               "Tabla: perfilar con cProfile multiplica por 4,6 el tiempo de 300 000 llamadas mínimas en Windows y por 3,7 en Ubuntu, y atribuye a la función mínima el 34 por ciento del tiempo cuando midiendo con y sin la llamada es el 46; repetir la misma clave con caché reduce el tiempo de 69 milisegundos a 0,05, mil trescientas noventa y cinco veces menos.",
               ["Medida", "Windows 11", "Ubuntu (WSL2)"], rows, [430, 270, 220], row_h=56, size=12,
               note="Un perfil determinista cuenta llamadas con precisión y altera el reparto del tiempo; sirve para ver qué se llama, no para decir cuánto cuesta. El benchmark con caché de una sola clave mide una búsqueda en diccionario, no el trabajo: 1 395 veces menos con la misma clave y casi igual con claves distintas.",
               note_kind="gold", foot=REAL)


def se377_aa() -> Fig:
    rows = [
        ["3", "58,8 % / 64 %", "48,6 % / 67 %", "48,9 % / 66 %"],
        ["5", "60,4 % / 64 %", "37,7 % / 72 %", "43,7 % / 69 %"],
        ["10", "58,0 % / 64 %", "18,6 % / 79 %", "36,0 % / 71 %"],
        ["30", "39,5 % / 72 %", "2,8 % / 92 %", "27,5 % / 77 %"],
    ]
    return tab("Comparar dos copias idénticas: falsas diferencias de más del 3 % / detección de una regresión real del 5 %",
               "Tabla: al comparar dos copias idénticas con ruido y un 8 por ciento de interferencias, la media declara una diferencia de más del 3 por ciento en el 58 al 60 por ciento de los casos con 3 a 10 repeticiones; la mediana baja del 48,6 al 2,8 por ciento al pasar de 3 a 30 repeticiones y detecta el 92 por ciento de una regresión real del 5 por ciento.",
               ["Repeticiones por versión", "Media", "Mediana", "Mínimo"], rows, [260, 220, 220, 220], row_h=48, size=13,
               note="Con 5 repeticiones y la media, dos programas idénticos «difieren» el 60 % de las veces. La mediana es robusta a las interferencias, el mínimo reduce el ruido pero también la señal. El ruido (lognormal de 4 %, 8 % de interferencias de +15 a +80 %) es un supuesto del autor.",
               note_kind="coral", foot=SINT)


FIGURES = {
    "se-373-la-media-oculta-la-cola.svg": se373_cola,
    "se-373-un-mes-seis-definiciones.svg": se373_mes,
    "se-373-verificador-de-escenarios.svg": se373_linter,
    "se-374-reglas-de-analisis-estatico.svg": se374_reglas,
    "se-374-compuertas-de-cobertura.svg": se374_compuerta,
    "se-374-bloqueos-espurios.svg": se374_espurios,
    "se-375-cuatro-pruebas-un-sistema.svg": se375_pruebas,
    "se-375-omision-coordinada.svg": se375_omision,
    "se-375-duracion-y-calentamiento.svg": se375_duracion,
    "se-376-latencia-segun-la-utilizacion.svg": se376_utilizacion,
    "se-376-variabilidad-del-servicio.svg": se376_variabilidad,
    "se-376-agregar-percentiles-y-capacidad.svg": se376_agregar,
    "se-377-variacion-entre-procesos.svg": se377_variacion,
    "se-377-perfilador-y-cache.svg": se377_perfilador,
    "se-377-copias-identicas-que-difieren.svg": se377_aa,
}
