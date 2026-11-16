"""Figures for SE-187 to SE-192 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, scatter, stacked_bars
from figures_part07_a import bars

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-187
def se187_exposicion() -> Fig:
    return percentile_intervals(
        "Diez riesgos: retraso en días con riesgos independientes y con una causa común",
        "Intervalos con la mediana, el percentil 85 y el percentil 95 del retraso de diez riesgos: con riesgos independientes valen 21, 35 y 44 días; con una causa común que arrastra a la mayoría valen 10, 66 y 81, y la media casi no cambia (21,7 y 22,2) respecto de la exposición esperada de 21,6.",
        [("Riesgos independientes", [21, 35, 44]), ("Con una causa común", [10, 66, 81])],
        unit="Retraso (días)", marks=("mediana", "p85", "p95"), label_w=190,
        note="La exposición esperada es la misma y el riesgo no: la causa común reparte el retraso entre muchos proyectos buenos y unos pocos desastrosos. El 25 % de probabilidad del evento común y el 70 % de arrastre son supuestos.", note_kind="coral", foot=SINT)


def se187_supuestos() -> Fig:
    items = [
        ("Validar en orden arbitrario", 78.7, "coral", "78,7"),
        ("Primero el más barato de validar", 65.4, "gold", "65,4"),
        ("Primero el más caro de fallar", 64.2, "gold", "64,2"),
        ("Primero el mayor coste de fallar por coste de validar", 57.9, "teal", "57,9"),
    ]
    return bars("Coste esperado de descubrir tarde que un supuesto era falso (12 supuestos)",
                "Barras: con 12 supuestos cada uno cierto con probabilidad 0,85, el coste medio de descubrir tarde un supuesto falso es 78,7 con orden arbitrario, 65,4 validando primero el más barato, 64,2 el más caro de fallar y 57,9 ordenando por coste de fallar sobre coste de validar.",
                items, 6.0, "Todos los supuestos ciertos a la vez ocurre solo en 14,2 % de los planes: casi siempre alguno falla. Importa cuándo se descubre. El coste crece 15 % por semana de trabajo construido encima, un supuesto del autor.",
                label_w=450, width=1000, note_kind="gold", foot=SINT)


def se187_registro() -> Fig:
    return stacked_bars(
        "Linter de registros de decisión sobre 200 mutaciones de un registro correcto",
        "Barras apiladas con las mutaciones detectadas y no detectadas por un linter de forma: detecta 28 de 28 campos ausentes, 22 de 22 fechas sin formato, 15 de 15 responsables colectivos, 22 de 22 con una sola opción, 21 de 21 disparadores vagos y 34 de 34 decisiones sin opción, y 0 de 38 cambios de sentido del contexto y 0 de 20 actas que contradicen la decisión; en total 142 de 200.",
        ["Campo ausente", "Fecha sin formato", "Responsable colectivo", "Una sola opción", "Disparador de revisión vago", "Decisión que no corresponde a ninguna opción",
         "Cambio del sentido del contexto", "Decisión y acta que se contradicen"],
        [("Detectadas", [28, 22, 15, 22, 21, 34, 0, 0], "teal"), ("No detectadas", [0, 0, 0, 0, 0, 0, 38, 20], "coral")],
        unit="Mutaciones", horizontal=True, label_w=300, plot_h=320,
        note="El linter acierta 142 de 200 y falla exactamente donde importa el criterio humano: el sentido de lo escrito. Las reglas se escribieron conociendo las mutaciones, así que el 100 % por tipo es optimista.", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-188
def se188_escapes() -> Fig:
    return line_chart(
        "Defectos que se escapan de 10 000 según cuántas comprobaciones forman la definición de terminado",
        "Líneas con los defectos que se escapan de 10 000 según el número de comprobaciones y su correlación: con comprobaciones independientes bajan de 4 436 con una a 1 122 con cuatro; con correlación 0,5 llegan a 2 961, con 0,8 se quedan en 4 258 y con 1,0 en 4 500 sin importar cuántas se añadan.",
        [("Correlación 0,0 (independientes)", [(1, 4436), (2, 2372), (3, 1772), (4, 1122)], "teal"),
         ("Correlación 0,5", [(1, 4030), (2, 3174), (3, 3137), (4, 2961)], "gold"),
         ("Correlación 0,8", [(1, 4319), (2, 4258), (3, 4258), (4, 4258, "", "b")], "navy"),
         ("Correlación 1,0 (ven lo mismo)", [(1, 4500), (2, 4500), (3, 4500), (4, 4500, "", "t")], "coral")],
        x_label="Comprobaciones en la definición de terminado", y_label="Defectos que se escapan (de 10 000)",
        x_ticks=[(1, "1"), (2, "2"), (3, "3"), (4, "4")], point_labels="last",
        note="Añadir comprobaciones solo ayuda si ven defectos distintos. Con alta correlación la segunda ya no aporta casi nada. El modelo reduce la dificultad a un número; en la realidad la correlación depende de qué mira cada comprobación.", note_kind="coral", foot=SINT)


def se188_listo() -> Fig:
    items = [
        ("Sin refinar (60,0 % con ambigüedad)", 5.37, "coral", "5,37 d"),
        ("1 día de refinamiento (38,3 %)", 5.54, "gold", "5,54 d"),
        ("2 días (24,4 %)", 5.97, "teal", "5,97 d"),
        ("4 días (9,9 %)", 7.40, "gold", "7,40 d"),
        ("8 días (1,6 %)", 11.07, "coral", "11,07 d"),
    ]
    return bars("Plazo medio hasta terminar según los días de refinamiento previo",
                "Barras: con 60 por ciento de ambigüedad inicial que baja con cada día de refinamiento, el plazo medio hasta terminar es 5,37 días sin refinar, 5,54 con un día, 5,97 con dos, 7,40 con cuatro y 11,07 con ocho.",
                items, 40.0, "Exigir más preparación reduce la ambigüedad pero retrasa el inicio: con estos parámetros no refinar tiene el menor plazo medio, aunque con el peor riesgo de rehacer. El plazo medio no incluye el coste de oportunidad de lo que se aprende al empezar; la elección depende de cuánto cuesta rehacer.",
                label_w=360, width=980, note_kind="gold", foot=SINT)


def se188_criterios() -> Fig:
    return stacked_bars(
        "Linter de criterios de aceptación: criterios con los que se ajustó frente a casos nuevos",
        "Barras apiladas con los criterios en que el linter coincide con el juicio del autor: acierta 8 de 8 con los criterios con los que se ajustó y 6 de 8 con ocho casos nuevos, en los que dio dos falsos avisos sobre criterios verificables.",
        ["Criterios del ajuste (8)", "Ocho casos nuevos (8)"],
        [("Coincide con el juicio del autor", [8, 6], "teal"), ("Falso aviso", [0, 2], "coral")],
        unit="Criterios", horizontal=True, label_w=220,
        note="Ajuste 8 de 8; casos nuevos 6 de 8, con 4 aciertos y 2 falsos avisos. Con ocho casos la exactitud real es desconocida. El linter ve palabras, no si un criterio se puede comprobar.", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-189
def se189_resumen() -> Fig:
    items = [
        ("Mediana", 4.01, "teal", "4,01 d"),
        ("Media", 5.52, "gold", "5,52 d"),
        ("Percentil 85", 9.18, "gold", "9,18 d"),
        ("Percentil 95", 14.95, "coral", "14,95 d"),
    ]
    return bars("Tiempo de ciclo de 100 000 elementos con cola larga: qué número resumir",
                "Barras: con tiempo de ciclo lognormal de mediana 4 días, la media es 5,52, el percentil 85 es 9,18 y el 95 es 14,95; 34,5 por ciento de los elementos supera la media, y un solo elemento de 60 días mueve la media de una muestra de 20 de 6,05 a 8,75 sin cambiar casi la mediana.",
                items, 40.0, "Prometer la media falla en 34,5 % de los elementos. En una muestra de 20, un elemento de 60 días sube la media de 6,05 a 8,75 y deja la mediana en 4,32 → 4,48. Los datos son lognormales sintéticos: uno real puede ser distinto.",
                label_w=190, width=900, note_kind="gold", foot=SINT)


def se189_velocidad() -> Fig:
    data = [(1, 11, 33.0), (2, 10, 31.2), (4, 8, 27.0), (6, 12, 43.8), (8, 10, 39.5), (10, 8, 34.2), (11, 10, 44.4), (12, 13, 60.0)]
    items = []
    for s, n, v in data:
        kind = "coral" if s >= 11 else "gold"
        items.append((f"Sprint {s}: {n} elementos", v, kind, f"{v:g}".replace(".", ",") + " pt"))
    return bars("Velocidad en puntos frente a elementos terminados cuando la velocidad se premia",
                "Barras: con un rendimiento real constante de unos 10 elementos por sprint y una inflación de estimaciones de 4 por ciento por sprint, la velocidad en puntos va de 33,0 en el sprint 1 a 60,0 en el 12, 1,82 veces, mientras los elementos terminados pasan de 11 a 13, 1,18 veces.",
                items, 7.5, "La velocidad de sprint 12 es 1,82 veces la del sprint 1; los elementos terminados, 1,18 veces. Partir cada historia en dos duplicaría el conteo sin cambiar el alcance. Toda métrica premiada se puede inflar; por eso se miran juntas.",
                label_w=290, width=900, note_kind="coral", foot=SINT)


def se189_muestra() -> Fig:
    return percentile_intervals(
        "Percentil estimado dividido por el verdadero: intervalo que contiene el 90 % de 1000 muestras",
        "Intervalos del percentil 85 y del percentil 95 estimados divididos por el verdadero según el tamaño de la muestra: con 10 elementos el 85 va de 0,54 a 1,81 y el 95 de 0,46 a 2,09; con 20, de 0,69 a 1,74 y de 0,64 a 2,62; con 100, de 0,83 a 1,25 y de 0,79 a 1,40; con 400, de 0,91 a 1,11 y de 0,89 a 1,18.",
        [("10 elementos · P85", [0.54, 1.81]), ("10 elementos · P95", [0.46, 2.09]), ("20 elementos · P85", [0.69, 1.74]), ("20 elementos · P95", [0.64, 2.62]),
         ("50 elementos · P85", [0.76, 1.34]), ("50 elementos · P95", [0.69, 1.46]), ("100 elementos · P85", [0.83, 1.25]), ("100 elementos · P95", [0.79, 1.40]),
         ("400 elementos · P85", [0.91, 1.11]), ("400 elementos · P95", [0.89, 1.18])],
        unit="Percentil estimado / percentil verdadero", marks=("p5", "p95"), ref_lines=[(1.0, "verdadero = 1")], decimals=2, label_w=190,
        note="Con pocos elementos los percentiles altos son imprecisos: el percentil 95 de 20 elementos puede estar 2,6 veces por encima del real. Informar el tamaño de la muestra junto al percentil es parte de la métrica.", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-190
def se190_acciones() -> Fig:
    return line_chart(
        "Acciones acordadas por retrospectiva con 2 días de capacidad de mejora por sprint (12 sprints)",
        "Líneas con las acciones creadas y terminadas en 12 sprints según las acordadas por retrospectiva: las creadas suben de 12 a 96, pero las terminadas se quedan en 9,2 con una y en 9,4 con dos o más; con 8 acciones por retrospectiva quedan 86,6 abiertas y el beneficio acumulado es 12,7 puntos porcentuales frente a 12,1 con una.",
        [("Acciones creadas", [(1, 12), (2, 24), (3, 36), (5, 60), (8, 96)], "coral"),
         ("Acciones terminadas", [(1, 9.2, "", "b"), (2, 9.4, "", "b"), (3, 9.4, "", "b"), (5, 9.4, "", "b"), (8, 9.4, "", "b")], "teal")],
        x_label="Acciones acordadas por retrospectiva", y_label="Acciones en 12 sprints", x_ticks=[(1, "1"), (2, "2"), (3, "3"), (5, "5"), (8, "8")], decimals=1,
        note="La capacidad limita lo que se termina, no lo que se acuerda: ocho acciones por retrospectiva no mejoran más que dos y dejan 87 abiertas. Los costes de 1 a 4 días y el 3 % de mejora por acción son supuestos.", note_kind="coral", foot=SINT)


def se190_deteccion() -> Fig:
    return line_chart(
        "Cuántas veces una prueba declara una mejora, con efecto real de 15 % y sin efecto",
        "Líneas con el porcentaje de casos en que una prueba de rangos declara una mejora según las semanas de datos tras el cambio: con efecto real de 15 por ciento sube de 20,5 con 2 semanas a 51,0 con 8 y 70,9 con 24; sin efecto real queda entre 1,9 y 2,9, pero llega a 19,7 si se mira cada semana durante 12.",
        [("Con efecto real de 15 %", [(2, 20.5), (4, 36.0), (8, 51.0), (12, 59.8), (24, 70.9)], "teal"),
         ("Sin efecto, una sola mirada", [(2, 2.7), (4, 2.9), (8, 1.9, "", "t"), (12, 2.7), (24, 2.4)], "gold"),
         ("Sin efecto, mirando cada semana", [(12, 19.7)], "coral")],
        x_label="Semanas de datos tras el cambio", y_label="Casos en que declara mejora (%)", x_ticks=[(2, "2"), (4, "4"), (8, "8"), (12, "12"), (24, "24")], decimals=1,
        note="Dos semanas de datos casi nunca bastan para ver una mejora real del 15 %. Mirar cada semana multiplica por siete la falsa mejora. La dispersión de 0,5 y los 8 elementos por semana son supuestos.", note_kind="gold", foot=SINT)


def se190_intervenciones() -> Fig:
    items = [
        ("Situación actual: lotes de 5 y variabilidad alta", 41.2, "coral", "41,2"),
        ("Trabajar más horas sin cambiar nada", 41.6, "coral", "41,6"),
        ("Reducir la variabilidad del servicio", 28.9, "gold", "28,9"),
        ("Llegadas de una en una", 23.1, "gold", "23,1"),
        ("Añadir 10 % de capacidad", 22.6, "gold", "22,6"),
        ("Llegadas de una en una y menos variabilidad", 9.4, "teal", "9,4"),
    ]
    return bars("Espera media en una cola al 90 % de utilización según la intervención",
                "Barras: en una cola con 90 por ciento de utilización, lotes de cinco y alta variabilidad la espera es 41,2 servicios; trabajar más horas la deja en 41,6, añadir 10 por ciento de capacidad en 22,6, enviar de una en una en 23,1, reducir la variabilidad en 28,9 y combinar lotes pequeños y baja variabilidad en 9,4.",
                items, 10.0, "Una retrospectiva que concluye trabajar más no mueve la espera. Las intervenciones sobre el sistema (lotes, variabilidad, capacidad) sí, y se combinan. El modelo es una sola cola: un sistema real tiene muchas.",
                label_w=470, width=1010, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-191
def se191_calibracion() -> Fig:
    return heatmap(
        "Calibración de pronósticos de «cuándo termina» con alcance que crece de 0 a 20 %",
        "Mapa de calor con el porcentaje de casos en que se cumple cada pronóstico según la historia disponible: el P85 que ignora el crecimiento del alcance se cumple en 65,2, 64,7 y 69,2 por ciento con 4, 8 y 16 semanas, y el que lo incluye en 77,7, 80,1 y 85,2; una estimación puntual con el rendimiento medio se cumple en 45,8, 40,2 y 42,2.",
        ["4 semanas de historia", "8 semanas", "16 semanas"],
        ["P50", "P85", "P95", "Estimación puntual", "P85 con alcance"],
        [[46.3, 65.2, 74.4, 45.8, 77.7], [40.8, 64.7, 76.5, 40.2, 80.1], [42.7, 69.2, 82.1, 42.2, 85.2]],
        unit="Casos en que se cumple el pronóstico (%)", scale="teal", decimals=1, suffix=" %", highlight=[(1, 1), (1, 4)], label_w=170,
        note="El percentil 85 que ignora el crecimiento del alcance se cumple en 65 % a 69 %, no en 85 %. Un pronóstico está calibrado solo si incluye las fuentes de incertidumbre que existirán. La estimación puntual se cumple menos que la mediana.", note_kind="coral", foot=SINT)


def se191_colchon() -> Fig:
    return grouped_bars(
        "Diez tareas en cadena: margen por tarea frente a colchón compartido",
        "Barras con el porcentaje de proyectos que cumplen el plazo según el plan: la suma de medianas (50 días) se cumple en 25,2 por ciento; el margen P85 en cada tarea (84 días) en 99,2 si no hay expansión y en 22,6 si el trabajo se expande hasta agotar el margen; un colchón compartido (60,7 días) en 68,8 por ciento en ambos casos.",
        ["Suma de medianas (50 días)", "Margen P85 en cada tarea (84 días)", "Medianas más colchón de proyecto (60,7 días)"],
        [("Se cumple sin expansión", [25.2, 99.2, 68.8], "teal"), ("Se cumple con expansión", [25.2, 22.6, 68.8], "coral")],
        unit="Proyectos que cumplen el plazo (%)", decimals=1,
        note="El margen en cada tarea parece seguro hasta que las tareas lo consumen; un colchón al final del proyecto no puede gastarse hasta que hace falta. La regla de expansión (entregar al agotar el margen si se iba antes) es un supuesto del autor.", note_kind="gold", foot=SINT)


def se191_tornado() -> Fig:
    items = [
        ("Rendimiento semanal (de 26 a 13 semanas)", 13, "coral", "13 semanas"),
        ("Tamaño del backlog (de 13 a 22)", 9, "gold", "9 semanas"),
        ("Crecimiento semanal del alcance (de 16 a 19)", 3, "teal", "3 semanas"),
        ("Factor de partición de elementos (de 17 a 18)", 1, "teal", "1 semana"),
    ]
    return bars("Cuánto mueve el plazo P85 cada supuesto al variarlo ±30 % (base: 17 semanas)",
                "Barras: variar cada supuesto un 30 por ciento mueve el plazo P85 de 17 semanas en 13 semanas para el rendimiento semanal, 9 para el tamaño del backlog, 3 para el crecimiento del alcance y 1 para el factor de partición de elementos.",
                items, 30.0, "El rendimiento domina el plan: es el supuesto que conviene medir y vigilar. El orden depende de los valores base (60 elementos, 6 por semana, 1 de crecimiento, factor 1,2) que son supuestos del autor.",
                label_w=470, width=1010, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-192
def se192_disparadores() -> Fig:
    return scatter(
        "Disparador de replanificación por pronóstico P85: falsas alarmas frente a retraso de detección",
        "Puntos de seis reglas con la falsa alarma en proyectos sin deriva y el retraso mediano en detectar una caída real: con 4 semanas de historia y 1, 2 y 3 avisos seguidos la falsa alarma es 68,0, 46,5 y 34,8 por ciento con 3, 4 y 5 semanas de retraso; con 8 semanas es 47,2, 34,2 y 26,2 por ciento con 4, 5 y 6 semanas.",
        [("4 semanas de historia", [(3, 68.0, "1 aviso", "r"), (4, 46.5, "2 avisos", "r"), (5, 34.8, "3 avisos", "r")], "coral"),
         ("8 semanas de historia", [(4, 47.2, "1 aviso", "l"), (5, 34.2, "2 avisos", "l"), (6, 26.2, "3 avisos", "l")], "teal")],
        x_label="Retraso mediano en detectar una caída real (semanas)", y_label="Falsa alarma en proyectos sin deriva (%)", decimals=1,
        x_ticks=[(3, "3"), (4, "4"), (5, "5"), (6, "6")], y_zero=True,
        note="Endurecer la regla reduce las falsas alarmas y retrasa la detección: no existe una regla sin costo. Con un plazo de 22 semanas y 100 elementos, el 83 % de los proyectos con caída no terminaría a tiempo. Todos los parámetros son supuestos.", note_kind="coral", foot=SINT)


def se192_validador() -> Fig:
    return stacked_bars(
        "Validador de planes sobre 200 mutaciones de un plan correcto",
        "Barras apiladas con las mutaciones detectadas y no detectadas por un validador de forma: detecta todas las de campo ausente (28), rango ausente (15), confianza ausente (18), disparador sin umbral (17), supuesto sin responsable ni fecha (21), fecha sin formato (17), responsable colectivo (22) y métrica sin definición (19), y ninguna de las 20 de rango invertido ni de las 23 de salvaguarda que contradice el objetivo; en total 157 de 200.",
        ["Campo ausente", "Rango ausente", "Confianza ausente", "Disparador sin umbral", "Supuesto sin responsable ni fecha", "Fecha de revisión sin formato",
         "Responsable colectivo", "Métrica sin definición", "Rango invertido (14 a 9 semanas)", "Salvaguarda que contradice el objetivo"],
        [("Detectadas", [28, 15, 18, 17, 21, 17, 22, 19, 0, 0], "teal"), ("No detectadas", [0, 0, 0, 0, 0, 0, 0, 0, 20, 23], "coral")],
        unit="Mutaciones", horizontal=True, label_w=300, plot_h=340,
        note="Detecta 157 de 200 y no ve ninguna de las 43 mutaciones de sentido. Un plan que pasa el validador está completo en forma; no se sabe si es razonable.", note_kind="gold", foot=SINT)


def se192_replay() -> Fig:
    return grouped_bars(
        "Mil proyectos sintéticos: 60 elementos, 11 semanas, caída de 30 % en 40 % de ellos",
        "Barras con el cumplimiento de lo prometido y el valor entregado de tres estrategias: el plan fijo de 60 elementos cumple en 52,1 por ciento de los proyectos y entrega 92,9 por ciento del valor; ordenado por valor entrega 98,8 con el mismo cumplimiento; el plan adaptativo promete 42,8 elementos de media, cumple en 99,4 por ciento y entrega 98,8.",
        ["Plan fijo de 60 elementos", "Plan fijo ordenado por valor", "Plan adaptativo (promete 42,8 de media)"],
        [("Cumple lo prometido", [52.1, 52.1, 99.4], "teal"), ("Valor entregado", [92.9, 98.8, 98.8], "gold")],
        unit="Proyectos o valor (%)", decimals=1,
        note="La mejora de valor viene de ordenar por valor; la de cumplimiento, de prometer menos con un pronóstico prudente. Son dos efectos separables. Los valores lognormales y la caída de rendimiento son supuestos.", note_kind="teal", foot=SINT)


FIGURES = {
    "se-187-riesgos-independientes-y-causa-comun.svg": se187_exposicion,
    "se-187-orden-de-validacion-de-supuestos.svg": se187_supuestos,
    "se-187-linter-de-decisiones.svg": se187_registro,
    "se-188-comprobaciones-correlacionadas.svg": se188_escapes,
    "se-188-refinar-antes-de-empezar.svg": se188_listo,
    "se-188-linter-de-criterios.svg": se188_criterios,
    "se-189-que-numero-resumir.svg": se189_resumen,
    "se-189-velocidad-premiada.svg": se189_velocidad,
    "se-189-tamano-de-muestra.svg": se189_muestra,
    "se-190-acciones-por-retrospectiva.svg": se190_acciones,
    "se-190-detectar-una-mejora.svg": se190_deteccion,
    "se-190-intervenciones-sobre-el-sistema.svg": se190_intervenciones,
    "se-191-calibracion-de-pronosticos.svg": se191_calibracion,
    "se-191-margen-o-colchon.svg": se191_colchon,
    "se-191-sensibilidad-del-plan.svg": se191_tornado,
    "se-192-disparadores-de-replanificacion.svg": se192_disparadores,
    "se-192-validador-de-planes.svg": se192_validador,
    "se-192-reproduccion-de-proyectos.svg": se192_replay,
}
