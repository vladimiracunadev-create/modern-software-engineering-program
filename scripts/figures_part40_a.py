"""Figures for SE-481 to SE-486 (development methodologies: runs of real CPython code over the Avisos core with 20 hand-written mutants; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, _wrap, grouped_bars, heatmap, line_chart, stacked_bars

EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2); los recuentos son idénticos en ambos y los tiempos varían de equipo en equipo."
LAB = "Núcleo de Avisos con 20 mutantes escritos a mano (18 no equivalentes y 2 equivalentes); ejecutado en Windows 11 y Ubuntu (WSL2) con los mismos recuentos."


def flow(title: str, desc: str, rows: list[list[tuple[str, str]]], note: str = "", note_kind: str = "gold",
         foot: str = EJEC, width: int = 960, box_h: int = 84, gap: int = 44, size: int = 13) -> Fig:
    """Rows of boxes joined by arrows; each box is (text, kind). Rows are joined by an elbow arrow."""
    n_max = max(len(r) for r in rows)
    box_w = (width - 20 - gap * (n_max - 1)) / n_max
    for r in rows:
        for text, _ in r:
            lines = len(_wrap(text, size, box_w - 20))
            assert lines * size * 1.28 <= box_h - 12, f"box overflows in {title!r}: {text!r}"
    y = 14.0
    boxes = []
    for r in rows:
        row = []
        x = 10.0
        for text, kind in r:
            row.append((x, y, text, kind))
            x += box_w + gap
        boxes.append(row)
        y += box_h + 40
    y_end = y - 40 + box_h - box_h  # y of last row bottom computed below
    last_bottom = 14 + (len(rows) - 1) * (box_h + 40) + box_h
    note_lines = len(_wrap(note, 13, width - 40)) if note else 0
    note_h = max(54, note_lines * 13 * 1.28 + 26) if note else 0
    height = int(last_bottom + (note_h + 22 if note else 8) + (26 if foot else 6))
    f = Fig(width, height, title, desc)
    for ri, row in enumerate(boxes):
        for ci, (x, yy, text, kind) in enumerate(row):
            f.box(x, yy, box_w, box_h, text, kind, size)
            if ci:
                px = row[ci - 1][0] + box_w
                f.arrow([(px, yy + box_h / 2), (x, yy + box_h / 2)])
        if ri:
            prev = boxes[ri - 1]
            f.arrow([(prev[-1][0] + box_w / 2, prev[-1][1] + box_h), (prev[-1][0] + box_w / 2, prev[-1][1] + box_h + 20),
                     (row[0][0] + box_w / 2, prev[-1][1] + box_h + 20), (row[0][0] + box_w / 2, row[0][1])])
    y = last_bottom
    if note:
        f.box(10, y + 14, width - 20, note_h, note, note_kind, 13)
        y += note_h + 22
    if foot:
        f.text(width / 2, y + 16, foot, 12, "middle", 400, "#5c1f14")
    return f


def mapa(title: str, desc: str, rows: list[tuple[str, str, str, str]], note: str = "", note_kind: str = "gold", foot: str = EJEC,
         width: int = 960, left_w: float = 300, mid_w: float = 250, row_h: float = 76, gap: float = 36, size: int = 13) -> Fig:
    """Mapping diagram: one row per case, ``(left text, verdict text, verdict kind, reason text)``, joined by arrows."""
    right_w = width - 20 - left_w - mid_w - 2 * gap
    for left, mid, _, right in rows:
        for text, w in ((left, left_w), (mid, mid_w), (right, right_w)):
            lines = len(_wrap(text, size, w - 20))
            assert lines * size * 1.28 <= row_h - 12, f"box overflows in {title!r}: {text!r}"
    note_lines = len(_wrap(note, 13, width - 40)) if note else 0
    note_h = max(54, note_lines * 13 * 1.28 + 26) if note else 0
    last_bottom = 14 + len(rows) * row_h + (len(rows) - 1) * 18
    height = int(last_bottom + (note_h + 22 if note else 8) + (26 if foot else 6))
    f = Fig(width, height, title, desc)
    y = 14.0
    for left, mid, kind, right in rows:
        x1, x2, x3 = 10.0, 10.0 + left_w + gap, 10.0 + left_w + gap + mid_w + gap
        f.box(x1, y, left_w, row_h, left, "plain", size)
        f.box(x2, y, mid_w, row_h, mid, kind, size, True)
        f.box(x3, y, right_w, row_h, right, "grey", size)
        f.arrow([(x1 + left_w, y + row_h / 2), (x2, y + row_h / 2)])
        f.arrow([(x2 + mid_w, y + row_h / 2), (x3, y + row_h / 2)])
        y += row_h + 18
    y = last_bottom
    if note:
        f.box(10, y + 14, width - 20, note_h, note, note_kind, 13)
        y += note_h + 22
    if foot:
        f.text(width / 2, y + 16, foot, 12, "middle", 400, "#5c1f14")
    return f


def bars(title: str, desc: str, items: list[tuple[str, float, str, str]], scale: float, note: str = "",
         note_kind: str = "gold", foot: str = EJEC, width: int = 960, label_w: float = 330) -> Fig:
    step = 46
    note_lines = len(_wrap(note, 13, width - 40)) if note else 0
    note_h = max(54, note_lines * 13 * 1.28 + 26) if note else 0
    height = int(16 + len(items) * step + (note_h + 18 if note else 6) + (28 if foot else 8))
    f = Fig(width, height, title, desc)
    y = f.hbars(items, 14, 16, scale, label_w=label_w)
    if note:
        f.box(10, y + 2, width - 20, note_h, note, note_kind, 13)
        y += note_h + 18
    if foot:
        f.text(width / 2, y + 14, foot, 12, "middle", 400, "#5c1f14")
    return f


# ---------------------------------------------------------------- SE-481
def se481_oraculos_y_mutantes() -> Fig:
    return grouped_bars(
        "Cinco oráculos sobre 18 mutantes no equivalentes del núcleo de Avisos: cuántos mata cada uno",
        "Barras horizontales con los mutantes que mata cada oráculo de 18 no equivalentes: un caso feliz único mata 7, ocho pruebas de ejemplo (TDD) matan 15, los escenarios de aceptación con reloj matan 17, el contrato con 400 estados al azar mata 13 y un modelo de referencia ejecutable mata los 18.",
        ["Caso feliz único", "Ocho pruebas de ejemplo (TDD)", "Escenarios de aceptación con reloj", "Contrato con 400 estados al azar", "Modelo de referencia ejecutable"],
        [("Mutantes que mata", [7, 15, 17, 13, 18], "teal")],
        unit="Mutantes que mata (de 18)", horizontal=True, label_w=290, ref_lines=[(18, "18")],
        note='Ningún oráculo cubre lo mismo: el contrato deja vivos cinco mutantes que las ocho pruebas matan, y las ocho pruebas dejan vivos tres que el contrato mata. Los dos mutantes equivalentes sobreviven a todos, como debe ser. Las 20 variantes las escribió el autor; no son una muestra de defectos reales.', note_kind='gold', foot=LAB)


def se481_preguntas_y_metodologias() -> Fig:
    return flow('Cinco preguntas de desarrollo y la metodología que responde a cada una',
                'Diagrama con cinco preguntas encadenadas en dos filas: qué debe hacer el sistema, con qué vocabulario se dice, con qué interfaces se conecta, cómo se construye paso a paso y cómo se sabe que sigue sirviendo; a cada pregunta le corresponden BDD, ATDD y SDD, DDD, el diseño y las pruebas de contrato, TDD, y EDD y ODD.',
                [[('¿Qué debe hacer?\nBDD · ATDD · Specification by Example · SDD', 'teal'), ('¿Con qué palabras se dice?\nDDD: lenguaje ubicuo y contextos', 'gold'), ('¿Con qué interfaces se conecta?\nDiseño por contrato y pruebas de contrato', 'teal')],
                 [('¿Cómo se construye paso a paso?\nTDD: rojo, verde, refactor', 'coral'), ('¿Cómo sé que sigue sirviendo?\nEDD (evaluaciones) y ODD (flujo y evidencia)', 'gold')]],
                note='Cada metodología ordena una pregunta distinta; ninguna sustituye a las demás. La clase las trata como instrumentos con un oráculo, un costo y un punto ciego, no como identidades de equipo.',
                note_kind='teal', box_h=96)


def se481_union_de_oraculos() -> Fig:
    return bars('Mutantes muertos por cada oráculo y por tres parejas de oráculos',
                'Gráfico de barras con los mutantes no equivalentes muertos de 18 posibles: caso feliz 7, ocho pruebas de ejemplo 15, escenarios de aceptación 17, contrato con 400 estados 13 y modelo de referencia 18; entre las parejas, ocho pruebas más escenarios matan 17 y tanto ocho pruebas más contrato como escenarios más contrato matan los 18.',
                [('Caso feliz único', 7, 'coral', '7'), ('Ocho pruebas de ejemplo', 15, 'gold', '15'), ('Escenarios de aceptación', 17, 'gold', '17'),
                 ('Contrato (400 estados)', 13, 'gold', '13'), ('Modelo de referencia', 18, 'teal', '18'), ('Ocho pruebas + escenarios', 17, 'gold', '17'),
                 ('Ocho pruebas + contrato', 18, 'teal', '18'), ('Escenarios + contrato', 18, 'teal', '18')],
                scale=26, note='Dos oráculos de naturaleza distinta cubren lo que uno solo no ve: las ocho pruebas y el contrato, que por separado dejan vivos 3 y 5 mutantes, juntos no dejan ninguno. Dos oráculos parecidos (ocho pruebas y escenarios) comparten el punto ciego M01. Con 18 mutantes y un programa pequeño no se puede ordenar nada en general.',
                note_kind='gold', foot=LAB)


# ---------------------------------------------------------------- SE-482
def se482_cuaderno_del_ciclo() -> Fig:
    return line_chart(
        "Ocho pasos rojo-verde sobre el núcleo de Avisos: mutantes muertos tras cada prueba",
        "Línea con los mutantes muertos acumulados tras cada una de las ocho pruebas de un ciclo rojo-verde sobre el núcleo de Avisos: 1, 6, 8, 9, 9, 11, 14 y 15 de 18 posibles; cada prueba nueva falló con la versión anterior y pasó con la nueva, y la quinta no añade ninguno.",
        [("Mutantes muertos (acumulados)", [(1, 1), (2, 6), (3, 8), (4, 9), (5, 9), (6, 11), (7, 14), (8, 15)], "teal")],
        x_label="Prueba añadida (paso del ciclo)", y_label="Mutantes muertos de 18", x_ticks=[(i, str(i)) for i in range(1, 9)], y_ticks=[0, 5, 10, 15, 18],
        hlines=[(18, "18 no equivalentes")], decimals=0,
        note='Las ocho pruebas fallaron primero por la razón esperada y pasaron con la versión mínima; la prueba 5 no añadió ninguno porque protege una regla (no avisar tras el vencimiento) que ninguno de los 18 mutantes elimina. La curva depende de qué 18 mutantes escribió el autor.', note_kind='gold', foot=LAB)


def se482_ciclo_rojo_verde() -> Fig:
    return flow('El ciclo rojo-verde-refactor con sus tres comprobaciones',
                'Diagrama del ciclo de TDD en cuatro cajas: escribir una prueba mínima y verla fallar por la razón correcta, escribir el código más simple que la pasa, refactorizar con todas las pruebas en verde y elegir la siguiente prueba; una flecha de retorno lleva de la última caja a la primera.',
                [[('ROJO\nUna prueba mínima falla, y por la razón esperada', 'coral'), ('VERDE\nEl código más simple que la pasa, aunque sea una trampa', 'teal'), ('REFACTOR\nMejora el diseño sin cambiar el comportamiento', 'gold')],
                 [('SIGUIENTE\nElige la prueba que más enseña, no la más fácil', 'navy')]],
                note='Dos controles hacen del ciclo un método y no un ritual: ver la prueba fallar (si pasa de inmediato no prueba nada) y no tocar el comportamiento durante el refactor (si una prueba se rompe, el cambio no era un refactor).',
                note_kind='teal', box_h=96)


def se482_sobrevivientes() -> Fig:
    return stacked_bars(
        "Tres mutantes sobreviven a las ocho pruebas; tres pruebas guiadas por ellos matan los 18",
        "Barras apiladas con los mutantes muertos y vivos de 18: tras las ocho pruebas de TDD mueren 15 y sobreviven M01, M12 y M16; al añadir tres pruebas guiadas por esos sobrevivientes mueren los 18.",
        ["Ocho pruebas de TDD", "Ocho pruebas más tres guiadas por los sobrevivientes"],
        [("Muertos", [15, 18], "teal"), ("Vivos", [3, 0], "coral")],
        unit="Mutantes no equivalentes", horizontal=True, label_w=300,
        note='Los sobrevivientes señalan qué ejemplo falta; no sustituyen el criterio de quien diseña las pruebas. Matar los 18 no demuestra que el código sea correcto: demuestra que estas 18 variantes se distinguen del original con estas pruebas.', note_kind='coral', foot=LAB)


# ---------------------------------------------------------------- SE-483
def se483_refactores_y_defectos() -> Fig:
    return heatmap(
        "Dos estilos de prueba ante cuatro refactores y un cambio de contrato del mismo servicio",
        "Mapa de calor con las pruebas que fallan en dos estilos tras cada cambio: el estilo clásico, con dobles con estado, pasa los cuatro refactores y falla solo con el cambio de contrato del puerto; el estilo de Londres, con dobles simulados, falla además el refactor que pide todas las entregas y filtra en el servicio; los dos detectan los seis defectos de comportamiento.",
        ["R1 leer el reloj una vez (refactor)", "R2 pedir todas las entregas y filtrar en el servicio (refactor)", "R3 extraer el cálculo del umbral (refactor)",
         "R4 leer lo registrado antes del reloj (refactor)", "R5 renombrar el puerto de registro (cambio de contrato)"],
        ["Estilo clásico", "Estilo de Londres"],
        [[0, 0], [0, 1], [0, 0], [0, 0], [1, 1]],
        unit="Falla", scale="coral", vmin=0, vmax=1, cell_fmt=lambda v: "FALLA" if v else "pasa", cell_h=44, label_w=430,
        note='La diferencia aparece donde el refactor cambia cómo el servicio consulta a un colaborador: la prueba de Londres fijó esa consulta, la clásica solo fijó el resultado. Ambas detectan los mismos seis defectos. Son dos suites escritas por el autor sobre un servicio pequeño.', note_kind='gold', foot=EJEC)


def se483_dos_estilos() -> Fig:
    f = Fig(960, 330, 'Dónde corta cada estilo la misma colaboración entre el servicio, el repositorio, el canal y el reloj',
            'Diagrama del servicio de recordatorios con tres colaboradores, el repositorio, el canal y el reloj: el estilo clásico los sustituye por dobles con estado y comprueba el resultado observable, mensajes entregados y envíos registrados; el estilo de Londres los sustituye por dobles simulados y comprueba las llamadas que el servicio les hace.')
    f.box(380, 20, 200, 64, 'Servicio de recordatorios', 'navy', 14, bold=True)
    for x, label in ((40, 'Repositorio'), (380, 'Canal'), (720, 'Reloj')):
        f.box(x, 150, 200, 54, label, 'plain', 14)
        f.arrow([(480, 84), (x + 100, 150)])
    f.box(20, 238, 440, 78, 'ESTILO CLÁSICO\nDobles con estado: se mira qué mensajes se entregaron y qué envíos quedaron registrados', 'teal', 13)
    f.box(500, 238, 440, 78, 'ESTILO DE LONDRES\nDobles simulados: se mira qué llamadas hizo el servicio y con qué argumentos', 'gold', 13)
    return f


def se483_cuando_usar_cada_uno() -> Fig:
    return mapa(
        "Qué estilo conviene según la situación del colaborador y del cambio",
        "Diagrama de decisión con cuatro situaciones y el estilo que conviene en cada una: un colaborador lento, externo o no determinista pide un doble con estado si es posible y simulados si no; querer refactorizar el interior sin tocar pruebas favorece el estilo clásico; diseñar de fuera hacia dentro favorece el estilo de Londres; y un cambio de interfaz de un colaborador hace fallar a ambos porque es un cambio de contrato.",
        [("El colaborador es lento, externo o no determinista", "Doble con estado si se puede; si no, simulado", "gold", "El estilo de Londres sirve para fijar el contrato en la frontera"),
         ("Se quiere refactorizar el interior sin tocar pruebas", "Clásico", "teal", "Aserciones sobre resultados toleran cambios de colaboración"),
         ("Se diseña de fuera hacia dentro sin saber aún qué colabora", "Londres", "gold", "Simular descubre las interfaces que hacen falta"),
         ("Un colaborador cambia de interfaz", "Ambos fallan", "coral", "Es un cambio de contrato, no un refactor")],
        note='La tabla es una guía de criterio, no un resultado medido: lo medido está en la primera figura. Muchos equipos usan los dos estilos según el colaborador.', note_kind='teal', foot='')


# ---------------------------------------------------------------- SE-484
def se484_escenarios_y_contribucion() -> Fig:
    return grouped_bars(
        "Nueve escenarios en lenguaje de negocio ejecutados contra 18 mutantes: cuántos mata cada uno y cuántos solo él",
        "Barras horizontales con los mutantes que mata cada uno de nueve escenarios Gherkin y los que mata solo él: avisar a las 72 horas mata 5 y ninguno solo él, no repetir un aviso mata 3 y los 3 solo él, quien ya entregó mata 2 y 1 solo él, la caída mata 6, el silencio con la última hora mata 9 y 1 solo él, el silencio sin el de 24 horas mata 2 y 1, el silencio por curso mata 8 y 1, la entrega vencida mata 1 y el escenario de la interfaz agradable no mata ninguno.",
        ["Avisa a las 72 horas", "No repite un aviso enviado", "Quien ya entregó no recibe avisos", "Tras una caída solo llega el aviso más urgente",
         "Un curso silenciado conserva el aviso de la última hora", "Un curso silenciado no recibe el de 24 horas", "El silencio de un curso no afecta a otro",
         "Una entrega vencida no avisa", "La interfaz es agradable"],
        [("Mutantes que mata", [5, 3, 2, 6, 9, 2, 8, 1, 0], "teal"), ("Mutantes que mata solo él", [0, 3, 1, 0, 1, 1, 1, 0, 0], "gold")],
        unit="Mutantes (de 18)", horizontal=True, label_w=330, plot_h=380,
        note='Los nueve escenarios usan 32 pasos y 10 definiciones de paso (3,2 pasos por definición) y matan 15 de 18; sobreviven M01, M12 y M16. El último escenario pasa siempre: su «Entonces» no afirma nada comprobable. Escenarios y mutantes los escribió el autor.', note_kind='coral', foot=EJEC)


def se484_de_la_conversacion_al_paso() -> Fig:
    return flow('De la conversación a un paso ejecutable',
                'Diagrama de seis cajas en dos filas: la conversación de las tres perspectivas, un ejemplo concreto, un escenario con dado, cuando y entonces, la definición de paso enlazada a código, la ejecución contra el sistema y la documentación viva que se actualiza al ejecutar.',
                [[('Conversación entre negocio, desarrollo y prueba', 'gold'), ('Ejemplo concreto con datos reales', 'teal'), ('Escenario: Dado, Cuando, Entonces', 'teal')],
                 [('Definición de paso enlazada a código', 'plain'), ('Ejecución contra el sistema', 'coral'), ('Documentación viva que falla si miente', 'navy')]],
                note='El valor está en las dos primeras cajas: las ambigüedades salen en la conversación, no en la herramienta. Si nadie de negocio lee ni discute los escenarios, queda una suite de pruebas escrita en un formato más costoso.',
                note_kind='gold', box_h=84)


def se484_entonces_vaciado() -> Fig:
    return grouped_bars(
        "Reemplazar el «Entonces» de un escenario por un paso que no afirma nada: mutantes que dejan de morir",
        "Barras horizontales con los mutantes que dejan de morir de los 15 que matan los escenarios completos al vaciar el paso Entonces de cada escenario: el de no repetir pierde 2, los de quien ya entregó, última hora, 24 horas y otro curso pierden 1 cada uno, y los de 72 horas, caída y entrega vencida no pierden ninguno.",
        ["Avisa a las 72 horas", "No repite un aviso enviado", "Quien ya entregó no recibe avisos", "Tras una caída solo llega el aviso más urgente",
         "Conserva el aviso de la última hora", "No recibe el de 24 horas", "No afecta a otro curso", "Una entrega vencida no avisa"],
        [("Mutantes que dejan de morir", [0, 2, 1, 0, 1, 1, 1, 0], "coral")],
        unit="Mutantes que dejan de morir (de 15)", horizontal=True, decimals=0, ticks=[0, 1, 2], label_w=330,
        note='Tres escenarios pueden perder su «Entonces» sin que ninguna comprobación se resienta: quedan cubiertos por otros o no afirman lo que dicen. Es una señal para revisar el texto, no una prueba de que sobren.', note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-485
def se485_conjuntos_de_ejemplos() -> Fig:
    return grouped_bars(
        "Cuatro conjuntos de ejemplos de aceptación y los mutantes que matan de 18",
        "Barras horizontales con los mutantes que mata cada conjunto de ejemplos de 18 no equivalentes: cinco típicos matan 10, doce de frontera del tiempo matan 11, veinte al azar matan 8, 144 combinatorios matan 17 y dejan vivo solo M08, y frontera con típicos juntos, 17 ejemplos, matan 14.",
        ["5 ejemplos típicos", "12 ejemplos de frontera del tiempo", "20 ejemplos al azar", "144 ejemplos combinatorios", "Frontera y típicos juntos (17 ejemplos)"],
        [("Mutantes que mata", [10, 11, 8, 17, 14], "teal")],
        unit="Mutantes que mata (de 18)", horizontal=True, label_w=310, ref_lines=[(18, "18")],
        note='Más ejemplos no es mejor: 20 al azar matan menos que 12 bien elegidos. El conjunto combinatorio llega a 17 pero no mata M08 porque solo combina un estudiante y un curso; las dimensiones que el conjunto no varía quedan sin comprobar. Los resultados esperados salen de un modelo escrito aparte.', note_kind='coral', foot=EJEC)


def se485_ciclo_de_aceptacion() -> Fig:
    return flow('ATDD: la tabla de ejemplos antes que el código',
                'Diagrama de cinco cajas en dos filas: se redacta la tabla de ejemplos con negocio, se convierte en una prueba de aceptación que falla, se desarrolla con ciclos de TDD internos hasta que pasa, se muestran los resultados a quien aceptó los ejemplos y los ejemplos pasan a la suite de regresión.',
                [[('Tabla de ejemplos redactada con negocio', 'gold'), ('Prueba de aceptación: roja', 'coral'), ('Ciclos de TDD internos hasta el verde', 'teal')],
                 [('Se muestra a quien aceptó los ejemplos', 'plain'), ('Los ejemplos pasan a la suite de regresión', 'navy')]],
                note='La prueba de aceptación es el ciclo externo y cada ciclo de TDD el interno. Si los ejemplos los escribe solo quien implementa, se pierde la mitad del valor: el acuerdo.',
                note_kind='teal', box_h=84)


def se485_dimensiones_cubiertas() -> Fig:
    return heatmap(
        "Qué dimensiones del problema varía cada conjunto de ejemplos",
        "Mapa de calor con las dimensiones que varía cada conjunto de ejemplos: los cinco típicos eligen tres puntos sueltos del tiempo e incluyen una vez una entrega entregada y un curso silenciado; los doce de frontera cubren los límites del tiempo pero no varían entregada ni silenciado; los veinte al azar varían tiempo, entregada y silenciado a veces; los 144 combinatorios cubren tiempo, entregada y silenciado; ninguno varía el curso ni la persona, por lo que los 144 dejan vivo M08.",
        ["5 típicos", "12 de frontera", "20 al azar", "144 combinatorios"],
        ["Límites del tiempo", "Entregada", "Silenciado", "Varios cursos o personas"],
        [[0.5, 1, 0.5, 0], [1, 0, 0, 0], [0.5, 0.5, 0.5, 0], [1, 1, 1, 0]],
        unit="Dimensión variada", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "sí" if v == 1 else ("no" if v == 0 else "parcial"), cell_h=50, label_w=190,
        note='La columna de la derecha explica el único mutante que sobrevive al conjunto más grande: ningún ejemplo distingue silenciar a una persona de silenciar un curso. Elegir ejemplos es decidir qué dimensiones se comprueban.', note_kind='gold', foot='')


# ---------------------------------------------------------------- SE-486
def se486_polisemia_de_entrega() -> Fig:
    return grouped_bars(
        "Cuatro mil doscientas cuarenta y nueve frases con «entrega» en las Partes 00 a 39 clasificadas por sentido",
        "Barras horizontales en escala logarítmica con las frases que contienen entrega clasificadas por reglas léxicas: 487 hablan del trabajo de una persona estudiante en 29 partes, 89 de liberar o desplegar software en 16 partes, 122 de hacer llegar un mensaje o resultado en 19 partes, 15 mezclan más de un sentido y 3 536 no tienen un sentido que las reglas reconozcan.",
        ["Trabajo de una persona estudiante (29 partes)", "Liberar o desplegar software (16 partes)", "Hacer llegar un mensaje o resultado (19 partes)", "Frases con más de un sentido a la vez", "Frases sin sentido reconocible por las reglas"],
        [("Frases", [487, 89, 122, 15, 3536], "gold")],
        unit="Frases (escala logarítmica)", horizontal=True, log=True, label_w=330,
        note='La palabra que da nombre al dominio de Avisos tiene al menos tres sentidos en el propio programa. Las reglas léxicas son burdas: las 3 536 frases sin clasificar no significan que carezcan de sentido, sino que las reglas no lo ven.', note_kind='gold', foot='Recuento léxico sobre content/part-00..39 con expresiones regulares; idéntico en Windows 11 y Ubuntu (WSL2).')


def se486_contextos_y_traduccion() -> Fig:
    f = Fig(960, 330, 'Dos contextos acotados con una capa de traducción entre ellos',
            'Diagrama con dos contextos delimitados: en el contexto académico una entrega es un trabajo con estado pendiente o recibida, en el contexto de avisos una entrega es un elemento con vencimiento y un indicador de entregada; una capa de traducción en medio convierte el estado textual en un indicador booleano y es el único lugar donde se conocen ambos vocabularios.')
    f.group(10, 14, 400, 220, 'Contexto académico', 'teal')
    f.box(30, 60, 360, 70, 'Entrega = trabajo de una persona estudiante\nestado: pendiente o recibida', 'plain', 13)
    f.box(30, 150, 360, 66, 'Lenguaje: entrega, estudiante, curso, vence_en', 'teal', 13)
    f.group(550, 14, 400, 220, 'Contexto de avisos', 'gold')
    f.box(570, 60, 360, 70, 'Entrega = elemento con vencimiento\nsubmitted: verdadero o falso', 'plain', 13)
    f.box(570, 150, 360, 66, 'Lenguaje: delivery, student, due, submitted', 'gold', 13)
    f.box(425, 80, 110, 80, 'Capa de traducción', 'navy', 13, bold=True)
    f.arrow([(410, 120), (425, 120)])
    f.arrow([(535, 120), (550, 120)])
    f.box(10, 250, 940, 66, 'La traducción es el único lugar que conoce los dos vocabularios: «recibida» pasa a verdadero y «pendiente» a falso. Sin ella, el texto «pendiente» cuenta como verdadero.', 'coral', 13)
    return f


def se486_con_y_sin_traduccion() -> Fig:
    return grouped_bars(
        "Ocho entregas del contexto académico leídas por el contexto de avisos, con y sin traducción",
        "Barras agrupadas de ocho entregas del contexto académico: con la capa de traducción, 2 quedan como entregadas y se envían 6 avisos; sin traducir, el estado pasa como texto, cuenta las 8 como entregadas porque cualquier texto no vacío es verdadero y no se envía ningún aviso.",
        ["Con la capa de traducción", "Sin traducir (el estado pasa como texto)"],
        [("Contadas como entregadas", [2, 8], "gold"), ("Avisos enviados", [6, 0], "teal")],
        unit="Entregas (de 8)",
        note='El fallo no lanza ninguna excepción: el servicio funciona y no avisa a nadie. Un nombre compartido entre contextos sin traducción explícita produce errores silenciosos. Ocho entregas sintéticas; el mecanismo es general, la magnitud no.', note_kind='coral', foot=EJEC)


FIGURES = {
    "se-481-oraculos-y-mutantes.svg": se481_oraculos_y_mutantes,
    "se-481-preguntas-y-metodologias.svg": se481_preguntas_y_metodologias,
    "se-481-union-de-oraculos.svg": se481_union_de_oraculos,
    "se-482-cuaderno-del-ciclo.svg": se482_cuaderno_del_ciclo,
    "se-482-ciclo-rojo-verde.svg": se482_ciclo_rojo_verde,
    "se-482-sobrevivientes.svg": se482_sobrevivientes,
    "se-483-refactores-y-defectos.svg": se483_refactores_y_defectos,
    "se-483-dos-estilos.svg": se483_dos_estilos,
    "se-483-cuando-usar-cada-uno.svg": se483_cuando_usar_cada_uno,
    "se-484-escenarios-y-contribucion.svg": se484_escenarios_y_contribucion,
    "se-484-de-la-conversacion-al-paso.svg": se484_de_la_conversacion_al_paso,
    "se-484-entonces-vaciado.svg": se484_entonces_vaciado,
    "se-485-conjuntos-de-ejemplos.svg": se485_conjuntos_de_ejemplos,
    "se-485-ciclo-de-aceptacion.svg": se485_ciclo_de_aceptacion,
    "se-485-dimensiones-cubiertas.svg": se485_dimensiones_cubiertas,
    "se-486-polisemia-de-entrega.svg": se486_polisemia_de_entrega,
    "se-486-contextos-y-traduccion.svg": se486_contextos_y_traduccion,
    "se-486-con-y-sin-traduccion.svg": se486_con_y_sin_traduccion,
}
