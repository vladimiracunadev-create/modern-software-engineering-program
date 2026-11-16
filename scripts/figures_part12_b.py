"""Figures for SE-151 to SE-156 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3 unless a timing is shown)."""
from __future__ import annotations

from figure_cases import case_cards
from figure_kit import Fig, fmt_es, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars
from figures_part07_a import bars
from figures_part10_a import SINT, intervals


# ---------------------------------------------------------------- SE-151
def se151_densidad() -> Fig:
    return grouped_bars("Matriz de trazabilidad sintética (40 requisitos, 60 pruebas, 30 módulos): densidad de enlaces e impacto",
                        "Barras agrupadas con tres densidades de enlaces entre requisitos, pruebas y módulos: al pasar de 123 a 382 enlaces los requisitos sin prueba bajan de 11 a 0 y las pruebas sin requisito de 27 a 0, pero el impacto medio de un cambio sube de 2,8 a 17,1 elementos y el máximo de 9 a 31.",
                        ["123 enlaces (2 % / 4 %)", "193 enlaces (4 % / 6 %)", "382 enlaces (8 % / 10 %)"],
                        [("Requisitos sin prueba", [11, 4, 0], "coral"), ("Pruebas sin requisito", [27, 14, 0], "gold"), ("Impacto medio de un cambio", [2.8, 5.5, 17.1], "teal"), ("Impacto máximo", [9, 15, 31], "navy")],
                        unit="requisitos, pruebas o elementos afectados",
                        note="La probabilidad de enlace es requisito–prueba / prueba–módulo. Más enlaces eliminan huérfanos pero también hacen que casi cualquier cambio toque casi todo: un enlace por si acaso vuelve inútil el análisis de impacto. La trazabilidad útil es la mínima que responde preguntas concretas.",
                        note_kind="gold", foot=SINT)


def se151_deterioro() -> Fig:
    ss = [5, 10, 20, 40]
    return line_chart("Fracción de enlaces manuales todavía correctos tras 5, 10, 20 y 40 sprints",
                      "Líneas con el porcentaje de enlaces de trazabilidad mantenidos a mano que siguen siendo correctos si cada sprint se degrada una fracción: con 1 por ciento por sprint quedan 66,9 por ciento tras 40 sprints, con 3 por ciento 29,6 y con 5 por ciento 12,9.",
                      [("1 % por sprint", [(s, v, fmt_es(v, 1), "t") for s, v in zip(ss, [95.1, 90.4, 81.8, 66.9])], "teal"),
                       ("3 % por sprint", [(s, v, fmt_es(v, 1), "t") for s, v in zip(ss, [85.9, 73.7, 54.4, 29.6])], "gold"),
                       ("5 % por sprint", [(s, v, fmt_es(v, 1), "b") for s, v in zip(ss, [77.4, 59.9, 35.8, 12.9])], "coral")],
                      x_label="Sprints transcurridos", y_label="Enlaces correctos (%)", x_ticks=[(s, str(s)) for s in ss], y_ticks=[0, 20, 40, 60, 80, 100],
                      note="El cálculo es (1−p)^sprints. En un verificador sintético con 10 requisitos, una etiqueta REQ-nnn en las pruebas detectó 1 enlace colgante y 6 requisitos sin prueba, pero también dejó fuera dos pruebas bien intencionadas por escribir «req-005» y «REQ-0006».",
                      note_kind="coral", foot="Los porcentajes de degradación son hipótesis del autor; el verificador se ejecutó sobre un proyecto temporal con defectos inyectados.")


def se151_derivada() -> Fig:
    funcs = ["comprobante", "exento", "formato", "tarifa", "total"]
    pruebas = [("T1 tarifa(0) · declara R1", [0, 0, 0, 1, 0]), ("T2 tarifa(5) · declara R2", [0, 0, 0, 1, 0]), ("T3 total(5, docente) · declara R3", [0, 1, 0, 0, 1]),
               ("T4 comprobante(10, estudiante) · declara R4", [1, 1, 1, 1, 1]), ("T5 exento(estudiante) · declara R3", [0, 1, 0, 0, 0])]
    return heatmap("Trazabilidad derivada: qué funciones toca realmente cada prueba (sys.settrace)",
                   "Mapa de calor de cinco pruebas y las cinco funciones que ejecutan según un trazador: T1 y T2 solo tarifa, T3 exento y total, T4 las cinco funciones y T5 exento; la prueba declarada de R4 toca también cuatro funciones de otros requisitos.",
                   [p for p, _ in pruebas], funcs, [v for _, v in pruebas], unit="funciones ejecutadas", scale="teal", vmin=0, vmax=1,
                   cell_fmt=lambda v: "ejecuta" if v else "—", highlight=[(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)], label_w=340,
                   note="El enlace declarado y el observado coinciden en R1–R3. T4 verifica el comprobante, pero un fallo en tarifa también la rompe: la prueba está acoplada a cuatro requisitos más (el contorno marca su fila). Ejecutar una función no prueba que se haya verificado su comportamiento.",
                   note_kind="gold", foot="Medido con sys.settrace en CPython 3.12.9 (Windows) y 3.12.3 (Ubuntu); solo cuenta llamadas a funciones del módulo bajo prueba.")


# ---------------------------------------------------------------- SE-152
def se152_retencion() -> Fig:
    items = [("«>=» en vez de «>»", 10, "gold", "10 borrados de más"), ("Ignora la retención de 730 días", 1473, "coral", "1 473 de más"), ("Ignora la retención legal", 39, "coral", "39 de más"),
             ("«12 meses» como 360 días", 83, "gold", "83 de más"), ("Desfase de un día por zona horaria", 14, "gold", "14 retenidos de más")]
    return bars("Purga por retención en 10 000 registros sintéticos: cuántos se tratan mal según la variante",
                "Barras de errores sobre 3907 registros que debían purgarse y 104 con retención legal: usar mayor o igual borra 10 de más; ignorar la retención de 730 días borra 1473; ignorar la retención legal borra 39; contar 12 meses como 360 días borra 83; un desfase de un día retiene 14 de más.",
                items, 0.3, "Cada variante parece correcta en una lectura rápida. Ignorar el caso de 730 días borra 1 473 registros que aún debían conservarse; ignorar la retención legal borra 39 que estaban bajo retención. Con un desfase de un día el error es de signo contrario: retiene datos que debían borrarse.",
                label_w=340, width=1000, note_kind="coral", foot=SINT)


def se152_stride() -> Fig:
    return stacked_bars("STRIDE por elemento en un diagrama de flujo de datos sintético con 18 elementos",
                        "Barras horizontales apiladas con las celdas de amenaza STRIDE por tipo de elemento: entidades externas 6 a revisar y 12 que no aplican, procesos 24 y 0, almacenes de datos 12 y 6, flujos de datos 24 y 24; en total 66 de 108 celdas.",
                        ["Entidad externa (3 · S, R)", "Proceso (4 · S, T, R, I, D, E)", "Almacén de datos (3 · T, R, I, D)", "Flujo de datos (8 · T, I, D)"],
                        [("Celdas a revisar", [6, 24, 12, 24], "teal"), ("No aplican", [12, 0, 6, 24], "grey")],
                        unit="celdas de amenaza (6 categorías por elemento)", horizontal=True, label_w=290,
                        note="Total: 18 elementos y 66 de 108 celdas. El mapa por elemento reduce 108 preguntas a 66, pero 66 sigue siendo una lista larga: cada celda debe terminar en un requisito, una aceptación explícita del riesgo o una nota de «no aplica». Una celda sin decisión es un requisito de seguridad que nadie escribió.",
                        note_kind="gold", foot="Conteo aritmético con la tabla STRIDE por elemento de Microsoft; los números de elementos son un ejemplo del autor.")


def se152_cadena() -> Fig:
    return case_cards("Registro encadenado con SHA-256: qué manipulaciones detecta la verificación",
                      "Cinco manipulaciones de un registro de auditoría de 100 entradas encadenadas por hash como tarjetas: modificar y borrar una entrada se detectan; truncar el final y reconstruir toda la cadena no; con un hash final guardado fuera de la cadena la reconstrucción se detecta.",
                      [("Modificar la entrada 40", "Detectada, en la 40", "El hash de la entrada ya no encadena.", "teal"),
                       ("Borrar la entrada 40", "Detectada, en la 40", "La entrada siguiente apunta a un hash que no existe.", "teal"),
                       ("Truncar el final (quedan 70 de 100)", "No se detecta", "Lo que queda sigue siendo una cadena válida.", "coral"),
                       ("Reconstruir toda la cadena sin la entrada 40", "No se detecta", "La cadena nueva es coherente consigo misma.", "coral"),
                       ("Reconstruir y comparar con el último hash guardado fuera", "Detectada: el hash final no coincide", "El ancla externa fija el final.", "teal")],
                      note="La cadena prueba continuidad, no autoría ni totalidad. «Registro inalterable» como requisito debe decir qué ancla externa (almacén de solo anexar, sello de tiempo, copia en otro dominio) hace detectables el truncado y la reconstrucción.",
                      note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-153
def se153_alcance() -> Fig:
    xs = [18, 38, 76]
    return line_chart("Alcance transitivo de un cambio en 30 requisitos sintéticos según la densidad de dependencias",
                      "Líneas con el alcance de un cambio según las aristas de dependencia entre 30 requisitos: de 18 a 76 aristas los dependientes medios suben de 0,7 a 4,9, el máximo de 4 a 17 y los cambios sin dependientes bajan de 17 a 6 de 30.",
                      [("Dependientes medios", [(x, v, fmt_es(v, 1), "r" if x == 18 else "b") for x, v in zip(xs, [0.7, 3.2, 4.9])], "teal"),
                       ("Máximo de dependientes", [(x, v, fmt_es(v), "t") for x, v in zip(xs, [4, 13, 17])], "coral"),
                       ("Cambios sin dependientes (de 30)", [(x, v, fmt_es(v), "t") for x, v in zip(xs, [17, 8, 6])], "gold")],
                      x_label="Aristas de dependencia (probabilidad 4 %, 8 % y 15 %)", y_label="Requisitos", x_ticks=[(18, "18"), (38, "38"), (76, "76")], y_ticks=[0, 5, 10, 15, 20],
                      note="El coste de un cambio depende más de su posición en el grafo que de su tamaño textual: un requisito raíz con 17 dependientes transitivos es una decisión de línea base; uno sin dependientes es un ajuste local.",
                      note_kind="gold", foot=SINT)


def se153_hash() -> Fig:
    return heatmap("Hash de una línea base: texto crudo frente a texto normalizado (6 ediciones)",
                   "Mapa de calor con seis ediciones de una tabla de requisitos y si cambian el hash: cuatro ediciones de formato (espacios, CRLF, columnas, tabulador) cambian el hash del texto crudo pero no el normalizado, y cambiar 30 s por 60 s o el estado cambian ambos.",
                   ["Espacio al final de cada fila", "Saltos de línea CRLF", "Columnas realineadas", "Tabulador en lugar de espacio", "30 s → 60 s", "Estado aprobado → borrador"], ["Hash del texto crudo", "Hash normalizado"],
                   [[1, 0], [1, 0], [1, 0], [1, 0], [1, 1], [1, 1]], unit="cambia el hash", scale="coral", vmin=0, vmax=1, cell_fmt=lambda v: "cambia" if v else "no cambia", highlight=[(0, 0), (1, 0), (2, 0), (3, 0)], label_w=280,
                   note="El contorno marca las falsas alarmas del hash crudo: cuatro cambios de formato. Un hash crudo da falsas alarmas de cambio; uno normalizado detecta cambios de contenido, pero también puede ocultar uno que importe (un espacio dentro de un identificador). La normalización es parte del contrato de la línea base y debe escribirse.",
                   note_kind="gold", foot=SINT)


def se153_comite() -> Fig:
    return grouped_bars("Comité de cambios: espera de una solicitud según la cadencia (6 solicitudes por semana)",
                        "Barras agrupadas con la espera de solicitudes de cambio con llegadas de 6 por semana: reunirse cada 0,2 semanas da espera media 0,10 y p95 0,19; cada semana 0,50 y 0,95; cada 2 semanas 0,99 y 1,90; cada 4 semanas 1,97 y 3,79, con 1,2, 6,0, 12,0 y 23,9 solicitudes por reunión.",
                        ["Cada 0,2 semanas (1,2 por reunión)", "Cada semana (6,0 por reunión)", "Cada 2 semanas (12,0 por reunión)", "Cada 4 semanas (23,9 por reunión)"],
                        [("Espera media", [0.10, 0.50, 0.99, 1.97], "teal"), ("Espera p95", [0.19, 0.95, 1.90, 3.79], "coral")],
                        unit="semanas de espera", decimals=2,
                        note="La espera media es la mitad del periodo, y la carga por reunión crece con él: a las cuatro semanas el comité revisa 24 solicitudes de una vez. La cadencia es una decisión de costo y estabilidad, no una convención de calendario.",
                        note_kind="gold", foot="Llegadas de Poisson sintéticas con semilla 1530; la tasa de 6 por semana es un supuesto del autor.")


# ---------------------------------------------------------------- SE-154
def se154_lecturas() -> Fig:
    items = [("3 operandos (A y B o C)", 2, "teal", "2 lecturas"), ("4 operandos", 5, "teal", "5"), ("5 operandos", 14, "gold", "14"), ("6 operandos", 42, "coral", "42"), ("7 operandos", 132, "coral", "132")]
    return bars("Lecturas posibles de una frase con y/o sin paréntesis (números de Catalan)",
                "Barras con el número de formas de agrupar una frase con conectores y y o: 2 con tres operandos, 5 con cuatro, 14 con cinco, 42 con seis y 132 con siete; la frase A y B o C se lee de dos maneras que difieren en 2 de 8 estados.",
                items, 4, "«A y B o C» tiene dos lecturas que dan resultados distintos en 2 de los 8 estados. Con cinco operandos mezclados (A y B o C y D o E) hay 14 lecturas y 10 funciones lógicas distintas: la ambigüedad estructural no se resuelve «leyendo con cuidado».",
                label_w=300, width=940, note_kind="coral", foot="Cálculo exacto; idéntico en Windows y Ubuntu.")


def se154_conflictos() -> Fig:
    qs = [f"Q{i}" for i in range(1, 13)]
    conf = [("Q4, Q8, Q9", [4, 8, 9]), ("Q5, Q6, Q7", [5, 6, 7]), ("Q1, Q6, Q7, Q12", [1, 6, 7, 12]), ("Q2, Q4, Q9, Q10", [2, 4, 9, 10]),
            ("Q3, Q6, Q7, Q9, Q12", [3, 6, 7, 9, 12]), ("Q4, Q5, Q9, Q10, Q11", [4, 5, 9, 10, 11])]
    vals = [[1 if i in m else 0 for i in range(1, 13)] for _, m in conf]
    return heatmap("Doce requisitos y seis conflictos mínimos: ninguno es un par de contradicciones evidentes",
                   "Mapa de calor con los doce requisitos que forman cada uno de los seis subconjuntos mínimos insatisfacibles: dos de tres requisitos, dos de cuatro y dos de cinco; Q7 y Q9 aparecen en todos los conflictos entre los dos, de modo que quitarlos resuelve los seis y deja diez de doce compatibles.",
                   [f"Conflicto {i + 1} · {len(m)} requisitos" for i, (_, m) in enumerate(conf)], qs, vals, unit="participa en el conflicto", scale="coral", vmin=0, vmax=1,
                   cell_fmt=lambda v: "●" if v else "", highlight=[(r, c) for r in range(6) for c in (6, 8) if vals[r][c]], label_w=210,
                   note="Contorno: Q7 y Q9. Quitar los requisitos Q9 y Q7 resuelve los seis conflictos, y el máximo compatible es 10 de 12. Pero ningún par de ellos se contradice por sí solo: una revisión que compare requisitos de dos en dos no los verá. Es lógica proposicional exhaustiva, no una herramienta de producción.",
                   note_kind="gold", foot=SINT)


def se154_celdas() -> Fig:
    items = [("Definidas en la especificación", 10, "teal", "10"), ("Imposibles por una regla escrita", 11, "gold", "11"), ("Preguntas abiertas", 21, "coral", "21")]
    return bars("Tabla estado–evento de una entrega: 6 estados × 7 eventos = 42 celdas",
                "Barras del estado de 42 celdas de una máquina de estados de una entrega: 10 definidas, 11 imposibles por una regla explícita y 21 preguntas abiertas, como qué ocurre al enviar una entrega ya enviada.",
                items, 20, "El borrador de especificación define 10 de 42 celdas. Las 21 preguntas abiertas incluyen casos reales: calificar una entrega solo «Enviada», retirar una entrega «En revisión», expirar sesión en cualquier estado posterior. Cada una es un requisito que alguien tendrá que inventar en código.",
                label_w=330, width=960, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-155
def se155_puntaje() -> Fig:
    return stacked_bars("Regla léxica de verificabilidad (4 señales, umbral 3) frente a 26 enunciados",
                        "Barras horizontales apiladas con los enunciados bien y mal clasificados por una regla que puntúa cantidad con unidad, condición, estadístico o cota y respuesta observable: 10 de 10 enunciados vagos, 8 de 10 reparados y 6 de 6 nuevos.",
                        ["10 requisitos no verificables", "10 reparados por el autor", "6 enunciados nuevos"],
                        [("Clasificados como se esperaba", [10, 8, 6], "teal"), ("Clasificados mal", [0, 2, 0], "coral")],
                        unit="enunciados", horizontal=True, label_w=250,
                        note="La regla no entiende nada: cuenta señales. Los 10 vagos tienen un puntaje medio de 0,1 de 4 señales. Marcó como no verificable una reparación correcta («redondeará a un decimal con mitad hacia arriba… 25 casos») porque su vocabulario no incluye «redondeará»; las dos reparaciones que fallan puntúan 2 y 0. Sirve para mirar primero lo más vago, no para aprobar.",
                        note_kind="gold", foot="Reglas y etiquetas escritas por el autor; seis casos nuevos no bastan para estimar una exactitud real.")


def se155_latencia() -> Fig:
    return percentile_intervals("Percentil 95 de 400 peticiones a un servidor local: tres corridas por escenario",
                                "Rangos del percentil 95 de tres corridas de 400 peticiones a un servidor HTTP local: con un cliente de 1,88 a 2,02 ms en Windows y de 1,47 a 1,71 en Ubuntu; con ocho clientes de 5,56 a 6,04 y de 9,69 a 10,89.",
                                [("1 cliente · Windows 11", [1.88, 2.02]), ("1 cliente · Ubuntu (WSL2)", [1.47, 1.71]), ("8 clientes · Windows 11", [5.56, 6.04]), ("8 clientes · Ubuntu (WSL2)", [9.69, 10.89])],
                                unit="ms (p95)", marks=("mínimo", "máximo"), decimals=2,
                                note="Un requisito reparado («p95 ≤ 800 ms con 8 clientes») se verifica con un procedimiento, no con un adjetivo. Estas cifras son del bucle local de un solo equipo con un servidor trivial: ilustran el procedimiento, no el rendimiento de ningún sistema, y la variación entre corridas es parte del resultado.",
                                note_kind="teal", foot="Medido con http.server y http.client en CPython 3.12.9 (Windows 11) y 3.12.3 (Ubuntu/WSL2); un solo equipo, red de bucle local.")


def se155_ceros() -> Fig:
    return grouped_bars("Pruebas sin fallo necesarias para afirmar con 95 % de confianza que la tasa de fallo es menor que p",
                        "Barras agrupadas en escala logarítmica con las pruebas sin ningún fallo necesarias para acotar la tasa de fallo con 95 por ciento de confianza: 299 para 1 por ciento, 2995 para 1 por mil, 29 956 para 1 por diez mil y 2 995 731 para 1 por millón, casi iguales a la regla de tres.",
                        ["1 por 100 (1e-2)", "1 por 1 000 (1e-3)", "1 por 10 000 (1e-4)", "1 por millón (1e-6)"],
                        [("Pruebas sin fallo (exacto)", [299, 2995, 29956, 2995731], "teal"), ("Regla de tres (3/p)", [300, 3000, 30000, 3000000], "grey")],
                        unit="pruebas sin ningún fallo", log=True,
                        note="Cada orden de magnitud de confianza en la tasa cuesta diez veces más pruebas. «El sistema nunca perderá datos» no se puede verificar con pruebas finitas. Con 100 pruebas sin fallos solo se puede afirmar que la tasa es menor que 3 %, y un sistema que falla 2 % de las veces pasa esas 100 pruebas en 12,8 % de las ocasiones.",
                        note_kind="coral", foot="Cálculo exacto y simulación con semilla 155; idéntico en Windows y Ubuntu.")


# ---------------------------------------------------------------- SE-156
def se156_mutaciones() -> Fig:
    return stacked_bars("Validador de una especificación sintética con 16 defectos inyectados: 11 de 16 detectados",
                        "Barras horizontales apiladas con los defectos detectados y no detectados por un validador de especificaciones: las estructurales se detectan 8 de 8, las de completitud 3 de 3, el vocabulario flexionado 0 de 1 y las semánticas (umbral absurdo, contradicción, criterio ajeno y ambigüedad) 0 de 4.",
                        ["Estructurales (id duplicado, criterio inexistente, ciclo…)", "De completitud (sin supuestos, «por definir»…)", "Vocabulario («adecuada» frente a «adecuado»)", "Semánticas (30 → 3 000 días, plazos contradictorios…)"],
                        [("Detectados", [8, 3, 0, 0], "teal"), ("No detectados", [0, 0, 1, 4], "coral")],
                        unit="defectos inyectados", horizontal=True, label_w=330,
                        note="La especificación base no produce errores. El validador comprueba forma y referencias; no compara 30 con 3 000 días, no sabe que dos plazos se excluyen y no distingue un criterio ajeno. Esa parte la cubre la revisión humana. Detectar 11 de 16 no es una probabilidad de que una especificación real esté bien.",
                        note_kind="coral", foot=SINT)


def se156_camino() -> Fig:
    items = [("REQ-001 (5 días)", 5, "teal", "5"), ("REQ-003 (2 días, sin dependencias)", 2, "teal", "2"), ("REQ-002 (necesita REQ-001)", 8, "gold", "8"),
             ("REQ-005 (necesita REQ-001)", 8, "gold", "8"), ("REQ-004 (necesita REQ-001)", 9, "coral", "9, camino crítico")]
    return bars("Duración acumulada mínima de cinco requisitos con dependencias (costos supuestos en días)",
                "Barras del tiempo acumulado de cada requisito: REQ-001 5 días, REQ-003 2, REQ-002 8, REQ-005 8 y REQ-004 9; la suma secuencial es 17 días y el camino crítico 9, por REQ-001 seguido de REQ-004.",
                items, 40, "Con costos de 5, 3, 2, 4 y 3 días la suma secuencial es 17 y el camino crítico solo 9, porque tres requisitos pueden avanzar a la vez una vez terminado REQ-001. Una especificación que declara dependencias permite ese cálculo; una que no las declara no.",
                label_w=360, width=980, note_kind="teal", foot="Costos y dependencias de un ejemplo del autor; cálculo exacto.")


def se156_captura() -> Fig:
    items = [("Revisores independientes y defectos iguales", 30.0, 41.9, 60.0, "teal", "media 41,9"),
             ("Defectos de dificultad desigual", 23.1, 30.5, 39.6, "coral", "media 30,5")]
    return intervals("Estimar cuántos defectos quedan por captura-recaptura: dos revisores, 40 defectos reales",
                     "Gráfico de intervalos del estimador de Lincoln-Petersen sobre 40 defectos sembrados: con revisores independientes e igual dificultad la media es 41,9 con rango p5 a p95 de 30 a 60; con dificultad desigual, 30,5 con rango de 23,1 a 39,6, siempre por debajo de 40.",
                     items, 65, "defectos estimados",
                     note="Juntos, los dos revisores hallaron en media 28,0 y 25,4 defectos distintos de 40. Con dificultad igual el estimador es correcto en media pero impreciso (30 a 60). Con defectos difíciles para ambos, subestima: 30,5 frente a 40. Un número bajo de defectos restantes no es una garantía.", label_w=330, note_kind="gold", foot="3 000 simulaciones por escenario, semilla 156; probabilidades de detección 0,5 y 0,4 (supuestos del autor).")


FIGURES = {
    "se-151-densidad-de-enlaces-e-impacto.svg": se151_densidad,
    "se-151-deterioro-de-enlaces-manuales.svg": se151_deterioro,
    "se-151-trazabilidad-derivada-por-ejecucion.svg": se151_derivada,
    "se-152-errores-de-purga-por-retencion.svg": se152_retencion,
    "se-152-stride-por-elemento.svg": se152_stride,
    "se-152-cadena-de-hash-y-ancla-externa.svg": se152_cadena,
    "se-153-alcance-de-un-cambio.svg": se153_alcance,
    "se-153-hash-crudo-o-normalizado.svg": se153_hash,
    "se-153-cadencia-del-comite-de-cambios.svg": se153_comite,
    "se-154-lecturas-de-una-frase.svg": se154_lecturas,
    "se-154-conflictos-minimos.svg": se154_conflictos,
    "se-154-celdas-sin-definir.svg": se154_celdas,
    "se-155-regla-de-verificabilidad.svg": se155_puntaje,
    "se-155-latencia-en-bucle-local.svg": se155_latencia,
    "se-155-pruebas-sin-fallos.svg": se155_ceros,
    "se-156-validador-de-especificacion.svg": se156_mutaciones,
    "se-156-camino-critico.svg": se156_camino,
    "se-156-captura-recaptura.svg": se156_captura,
}
