"""Figures for SE-553 to SE-558 (AI-assisted development: synthetic processes with fixed seeds and real runs of standard-library code).

Los números se calculan con scripts/experiments_part46_a.py para que figuras y texto no se transcriban a mano.
"""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, scatter, stacked_bars
from figure_diagrams import fan
from figures_part07_a import bars

from functools import lru_cache

import experiments_part46_a as ex

SINT = "Proceso sintético con semilla fija; no se llamó a ningún modelo real. Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código estándar ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos."


def n(x, d: int = 1) -> str:
    """Formatea un número con coma decimal."""
    return f"{x:.{d}f}".replace(".", ",")


def p(x, d: int = 1) -> str:
    return n(x, d) + " %"


@lru_cache(maxsize=None)
def R(name: str):
    return getattr(ex, name)()


# ---------------------------------------------------------------- SE-553
def se457_muestreo_y_mayoria() -> Fig:
    f = R("e457_temperatura")["filas"]
    ts = [(r["T"], n(r["T"])) for r in f]
    return line_chart(
        'Cinco respuestas candidatas: la correcta es la segunda más probable (20 000 muestras por temperatura)',
        f'Líneas con el acierto según la temperatura: con una muestra pasa de {p(f[0]["una_muestra"])} a temperatura {n(f[0]["T"])} a {p(f[1]["una_muestra"])} con {n(f[1]["T"])}; el voto de mayoría de cinco pasa de {p(f[0]["mayoria_de_5"])} a {p(f[1]["mayoria_de_5"])}; que alguna de cinco sea correcta pasa de {p(f[0]["alguna_de_5"])} a {p(f[1]["alguna_de_5"])}; con temperatura baja la mayoría confirma la respuesta equivocada.',
        [("Alguna de 5 correcta", [(r["T"], r["alguna_de_5"], n(r["alguna_de_5"]), "t") for r in f], "teal"),
         ("Una muestra", [(r["T"], r["una_muestra"], n(r["una_muestra"]), "t") for r in f], "gold"),
         ("Mayoría de 5", [(r["T"], r["mayoria_de_5"], n(r["mayoria_de_5"]), "r" if i == 0 else "b") for i, r in enumerate(f)], "coral")],
        x_label="Temperatura de muestreo", y_label="Acierto (%)", x_ticks=ts, y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        note='Con temperatura baja el modelo repite con firmeza la respuesta más probable, que aquí es la incorrecta, y el voto de mayoría la confirma. Generar varias muestras ayuda a encontrar una correcta solo si algo externo (una prueba) puede reconocerla. Los logits son un supuesto del autor, no un modelo real.', note_kind='coral', foot=SINT)


def se457_confianza_no_es_exactitud() -> Fig:
    d = R("e457_calibracion")
    grupos = [(t["tramo"], t["confianza"], t["exactitud"]) for t in d["tramos"]] + [("Fáciles", d["faciles"]["confianza"], d["faciles"]["exactitud"]), ("Difíciles", d["dificiles"]["confianza"], d["dificiles"]["exactitud"])]
    return grouped_bars(
        '1 000 preguntas sintéticas: la confianza declarada frente al acierto observado',
        f'Barras agrupadas con la confianza media declarada y la exactitud observada por tramo de confianza y por dificultad: globalmente {p(d["global"]["confianza"])} de confianza frente a {p(d["global"]["exactitud"])} de exactitud; en las preguntas difíciles la confianza es {p(d["dificiles"]["confianza"])} y el acierto {p(d["dificiles"]["exactitud"])}.',
        [g[0] for g in grupos],
        [("Confianza media declarada", [g[1] for g in grupos], "gold"), ("Exactitud observada", [g[2] for g in grupos], "teal")],
        unit="Porcentaje (%)", decimals=1, ticks=[0, 20, 40, 60, 80, 100],
        note=f'El error de calibración esperado es {n(d["ece"])} puntos y la confianza casi no distingue las preguntas fáciles de las difíciles: el tono seguro no informa de la dificultad. Que exista este patrón en un modelo real es una pregunta empírica; aquí es un supuesto del autor.', note_kind='gold', foot=SINT)


def se457_ventana_y_conjuntos() -> Fig:
    d = R("e457_ventana")
    f = d["filas"]
    ts = [(r["ventana"], f'{r["ventana"] // 1000}k') for r in f]
    return line_chart(
        'Un repositorio sintético de 120 archivos: qué cabe en la ventana de contexto',
        f'Líneas con lo que cabe en la ventana de contexto de un repositorio de {d["archivos"]} archivos: con 8 000 tokens cabe el {p(f[0]["fraccion_del_repositorio"])} del repositorio y el {p(f[0]["conjuntos_que_caben"])} de los conjuntos de 8 archivos; con 128 000 cabe el {p(f[2]["fraccion_del_repositorio"])} del repositorio pero caben el {p(f[2]["conjuntos_que_caben"])} de los conjuntos.',
        [("Conjuntos de 8 archivos que caben", [(r["ventana"], r["conjuntos_que_caben"], n(r["conjuntos_que_caben"]), "t") for r in f], "teal"),
         ("Fracción del repositorio que cabe", [(r["ventana"], r["fraccion_del_repositorio"], n(r["fraccion_del_repositorio"]) if i > 1 else "", "b") for i, r in enumerate(f)], "coral")],
        x_label="Ventana de contexto (tokens)", y_label="Cabe en la ventana (%)", log_x=True, x_ticks=ts, y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        note=f'El repositorio suma {n(d["tokens_totales"]/1e6, 2)} millones de tokens (tamaños lognormales con mediana {d["mediana"]}): ninguna ventana lo contiene, así que alguien decide qué entra. La distribución de tamaños y el recuento de 1 token ≈ 4 caracteres son supuestos del autor.', note_kind='teal', foot=SINT)


# ---------------------------------------------------------------- SE-554
def se458_requisitos_sin_decir() -> Fig:
    f = R("e458_requisitos")["filas"]
    items = [(f'{r["especificados"]} de 6 especificados', r["todos"], 'coral' if r["todos"] < 25 else ('gold' if r["todos"] < 60 else 'teal'), p(r["todos"])) for r in f]
    return bars('Probabilidad de cumplir los seis requisitos de una tarea según cuántos se escribieron en el prompt',
               f'Barras con la probabilidad de que se cumplan los seis requisitos de una tarea según cuántos estén escritos: {p(f[0]["todos"])} con ninguno, {p(f[3]["todos"])} con tres, {p(f[5]["todos"])} con cinco y {p(f[6]["todos"])} con los seis.',
               items, 6.0, 'Cada requisito no escrito se cumple por azar la mitad de las veces y cada escrito el 95 %; el producto cae rápido porque los fallos se multiplican. Los dos porcentajes son supuestos del autor: muestran la forma, no la tasa de ningún modelo.',
               label_w=250, width=940, note_kind='gold', foot=SINT)


def se458_capas_de_validacion() -> Fig:
    d = R("e458_validadores")
    nombres = {"texto_extra": "Texto antes del JSON", "falta_clave": "Falta una clave", "fuera_de_rango": "Nota fuera de 1–7",
               "estado_invalido": "Estado no permitido", "incoherente": "Estado contradice la nota", "redondeo": "Dos decimales indebidos"}
    t = d["total"]
    claves = list(d["por_defecto"])
    return heatmap(
        '200 salidas sintéticas con un defecto cada una: cuántas atrapa cada capa de validación',
        f'Mapa de calor con cuántas de las 200 salidas defectuosas detecta cada capa acumulada de validación: solo el formato detecta {t["formato"]}, con el rango {t["formato_rango"]} y con la coherencia {t["formato_rango_coherencia"]}; los dos decimales indebidos no los detecta ninguna capa.',
        [f'{nombres[k]} ({d["por_defecto"][k]["n"]})' for k in claves], ["Solo formato", "+ rango", "+ coherencia"],
        [[d["por_defecto"][k]["formato"], d["por_defecto"][k]["formato_rango"], d["por_defecto"][k]["formato_rango_coherencia"]] for k in claves],
        unit="detectadas", row_title="Defecto (casos)", col_title="Casos detectados por cada capa acumulada",
        scale="teal", vmin=0, vmax=34, decimals=0, cell_h=42, label_w=290,
        note=f'Tres capas baratas detectan {t["formato_rango_coherencia"]} de {d["n"]}; los {d["n"] - t["formato_rango_coherencia"]} restantes cumplen todas las reglas escritas y siguen mal. Lo que ninguna regla enuncia no se comprueba. Los seis defectos y su reparto son del autor.', note_kind='coral', foot=EJEC)


def se458_instrucciones_que_chocan() -> Fig:
    f = R("e458_conflicto")["filas"]
    ts = [(r["n"], str(r["n"])) for r in f]
    return line_chart(
        'Probabilidad de que un conjunto de instrucciones no tenga ningún par en conflicto',
        f'Líneas con la probabilidad de que un conjunto de instrucciones no tenga ningún par en conflicto según su tamaño: con 12 instrucciones es {p(f[3]["q0.005"])} si cada par choca con probabilidad 0,5 por ciento y {p(f[3]["q0.02"])} si choca con 2 por ciento; con 20 instrucciones baja a {p(f[4]["q0.005"])} y {p(f[4]["q0.02"])}.',
        [("0,5 % por par", [(r["n"], r["q0.005"], n(r["q0.005"]), "t") for r in f], "teal"), ("2 % por par", [(r["n"], r["q0.02"], n(r["q0.02"]), "l" if i == 4 else "b") for i, r in enumerate(f)], "coral")],
        x_label="Instrucciones en el conjunto", y_label="Sin ningún par en conflicto (%)", x_ticks=ts, y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        note='Los pares crecen con el cuadrado de las instrucciones, así que añadir reglas «por si acaso» vuelve casi seguro algún choque. La probabilidad por par es un supuesto del autor y supone pares independientes.', note_kind='gold', foot='Cálculo exacto (1 − q)^pares; no hay simulación ni modelo real.')


# ---------------------------------------------------------------- SE-555
def se459_tamano_de_fragmento() -> Fig:
    f = R("e459_fragmentos")["filas"]
    return line_chart(
        '240 documentos de 900 palabras y un hecho escondido en cada uno: tamaño del fragmento (BM25 real)',
        f'Línea con la precisión frente al costo según el tamaño del fragmento: con fragmentos de {f[0]["tam"]} palabras el fragmento correcto es el primero en {p(f[0]["exacto_top1"])} de las consultas y se envían {f[0]["tokens_por_consulta"]} palabras; con {f[2]["tam"]} es el primero en {p(f[2]["exacto_top1"])} y se envían {f[2]["tokens_por_consulta"]}; con {f[3]["tam"]} se envían {f[3]["tokens_por_consulta"]} palabras sin ganar precisión.',
        [("Hecho completo en el primer fragmento", [(r["tokens_por_consulta"], r["exacto_top1"], f'{r["tam"]} pal. · {n(r["exacto_top1"])} %', "b" if i % 2 else "t") for i, r in enumerate(f)], "teal")],
        x_label="Palabras enviadas por consulta (3 fragmentos)", y_label="Hecho completo en el 1.º (%)", log_x=True, y_zero=False,
        x_ticks=[(100, "100"), (300, "300"), (1000, "1 000"), (3000, "3 000")], y_ticks=[95, 96, 97, 98, 99, 100], point_labels="none",
        note='Con una clave única la recuperación léxica acierta casi siempre en cualquier tamaño; los fragmentos pequeños parten algunos hechos por la frontera y los grandes cuestan 18 veces más contexto. La consulta con clave única es el caso más fácil: con paráfrasis o sin clave el resultado sería peor.', note_kind='teal', foot=EJEC)


def se459_memoria_que_caduca() -> Fig:
    f = R("e459_memoria")["filas"]
    return line_chart(
        'Hechos que cambian el 1 % de los días: respuestas obsoletas según la caducidad de la memoria (180 días)',
        f'Línea con el costo y el riesgo de la caducidad de la memoria: sin caducidad el {p(f[0]["erroneas"])} de las respuestas está obsoleto con 0 refrescos por hecho; con 30 días baja a {p(f[2]["erroneas"])} con {n(f[2]["refrescos_por_hecho"], 0)} refrescos y con 7 días a {p(f[3]["erroneas"])} con {n(f[3]["refrescos_por_hecho"], 0)}.',
        [("Respuestas obsoletas", [(r["refrescos_por_hecho"], r["erroneas"], f'{r["ttl"]} · {n(r["erroneas"])} %', "r") for r in f], "coral")],
        x_label="Refrescos por hecho en 180 días", y_label="Respuestas obsoletas (%)", x_ticks=[(0, "0"), (5, "5"), (10, "10"), (15, "15"), (20, "20"), (25, "25"), (40, "")], y_ticks=[0, 20, 40, 60], point_labels="none",
        note='Una memoria sin caducidad envejece hasta responder mal más de la mitad de las veces; acortar la caducidad compra frescura con cargas de lectura. La tasa de cambio del 1 % diario es un supuesto del autor y cada hecho cambia por separado.', note_kind='gold', foot=SINT)


def se459_presupuesto_de_contexto() -> Fig:
    d = R("e459_presupuesto")
    m = d["medias"]
    items = [('Al azar', m["aleatorio"], 'coral', n(m["aleatorio"], 2)), ('Por relevancia', m["relevancia"], 'gold', n(m["relevancia"], 2)), ('Por relevancia por token', m["densidad"], 'teal', n(m["densidad"], 2))]
    return bars('Relevancia total empaquetada en 3 000 tokens con 30 fragmentos candidatos (300 repeticiones)',
               f'Barras con la relevancia media empaquetada en un presupuesto de 3.000 tokens: {n(m["aleatorio"], 2)} al azar, {n(m["relevancia"], 2)} ordenando por relevancia y {n(m["densidad"], 2)} ordenando por relevancia por token, {p(d["mejora_densidad_vs_relevancia"])} más que la segunda.',
               items, 90.0, f'Elegir lo más relevante a secas gasta el presupuesto en fragmentos grandes; dividir por el tamaño mete {p(d["mejora_densidad_vs_relevancia"])} más relevancia. Las relevancias y tamaños son del autor y la relevancia se supone conocida, algo que en la práctica se estima con error.',
               label_w=250, width=940, note_kind='teal', foot=SINT)


# ---------------------------------------------------------------- SE-556
def se460_politica_de_aceptacion() -> Fig:
    f = R("e460_aceptacion")["filas"]
    return grouped_bars(
        '1 000 sugerencias sintéticas (78 % correctas): defectos que entran según cómo se acepta',
        f'Barras agrupadas con las sugerencias aceptadas y los defectos que entran según la política: aceptar sin leer acepta {f[0]["aceptadas"]} y deja entrar {f[0]["defectos_aceptados"]} defectos, leer solo las largas acepta {f[1]["aceptadas"]} y deja entrar {f[1]["defectos_aceptados"]}, y leer siempre y ejecutar acepta {f[2]["aceptadas"]} y deja entrar {f[2]["defectos_aceptados"]}.',
        [r["politica"] for r in f],
        [("Sugerencias aceptadas", [r["aceptadas"] for r in f], "grey"), ("Defectos aceptados", [r["defectos_aceptados"] for r in f], "coral")],
        unit="Sugerencias, de 1 000", ticks=[0, 250, 500, 750, 1000],
        note='Leer y ejecutar cuesta tiempo y reduce lo aceptado, pero deja entrar una quinta parte de los defectos. La tasa de acierto del 78 % y las tasas de detección del revisor son supuestos del autor; no miden ninguna herramienta ni persona.', note_kind='coral', foot=SINT)


def se460_alcance_de_la_edicion() -> Fig:
    d = R("e460_alcance")
    return grouped_bars(
        f'Corregir una condición en un archivo de {d["lineas_archivo"]} líneas: líneas de diferencia que debe revisar la persona',
        f'Barras horizontales con la probabilidad de encontrar el cambio real al revisar dos formas de aplicar el mismo arreglo en un archivo de {d["lineas_archivo"]} líneas: la edición dirigida cambia {d["diff_dirigido"]} líneas y se detecta con probabilidad {p(d["p_detectar_dirigido"])}; el archivo regenerado con deriva cosmética cambia {d["diff_regenerado"]} y se detecta con {p(d["p_detectar_regenerado"])}.',
        [f'Edición dirigida: {d["diff_dirigido"]} líneas distintas', f'Archivo regenerado con deriva: {d["diff_regenerado"]} líneas distintas'],
        [("Prob. de encontrar el cambio real", [d["p_detectar_dirigido"], d["p_detectar_regenerado"]], "teal")],
        unit="Probabilidad de encontrar el cambio real (%)", horizontal=True, label_w=270, decimals=1, ticks=[0, 20, 40, 60, 80, 100],
        note='Las líneas se miden con difflib sobre un archivo real generado; la probabilidad de detección usa una curva del autor que decae con el tamaño del diff, así que esa probabilidad es un modelo y no una medición de personas.', note_kind='gold', foot=EJEC)


def se460_retardo_de_sugerencias() -> Fig:
    f = R("e460_debounce")["filas"]
    return grouped_bars(
        '467 pulsaciones sintéticas: peticiones de sugerencia según el retardo antes de pedir',
        f'Barras agrupadas con las peticiones al modelo y las útiles según el retardo antes de pedir: sin retardo hay {f[0]["peticiones"]} peticiones para {f[0]["utiles"]} útiles y con 600 milisegundos hay {f[3]["peticiones"]} peticiones para {f[3]["utiles"]} útiles, a costa de esperar antes de ver la sugerencia.',
        [f'{r["retardo_ms"]} ms' for r in f],
        [("Peticiones al modelo", [r["peticiones"] for r in f], "coral"), ("Peticiones útiles", [r["utiles"] for r in f], "teal")],
        unit="Peticiones (467 pulsaciones)", ticks=[0, 100, 200, 300, 400, 500],
        note='Esperar a que la escritura se detenga elimina casi todo el gasto sin perder las pausas donde la sugerencia se habría mostrado. El ritmo de escritura y la regla «útil si hay una pausa de 0,5 s» son supuestos del autor; con otra persona cambiarían.', note_kind='teal', foot=EJEC)


# ---------------------------------------------------------------- SE-557
def se461_mejor_de_n() -> Fig:
    f = R("e461_mejor_de_n")["filas"]
    ts = [(r["n"], str(r["n"])) for r in f]
    return line_chart(
        'Elegir la mejor de N alternativas: calidad medida de la ganadora → calidad real (en desviaciones)',
        f'Líneas con la calidad de la mejor de N alternativas: con un evaluador exacto la calidad real crece de {n(f[0]["real_s0.0"], 2)} a {n(f[4]["real_s0.0"], 2)}; con ruido 1 la ganadora de 20 se mide en {n(f[4]["medida_s1.0"], 2)} y vale {n(f[4]["real_s1.0"], 2)}; con ruido 2 se mide en {n(f[4]["medida_s2.0"], 2)} y vale {n(f[4]["real_s2.0"], 2)}: elegir entre más alternativas sobrestima la calidad.',
        [("Ruido 2: medida", [(r["n"], r["medida_s2.0"]) for r in f], "coral"), ("Ruido 1: medida", [(r["n"], r["medida_s1.0"]) for r in f], "gold"),
         ("Evaluador exacto", [(r["n"], r["real_s0.0"]) for r in f], "navy"), ("Ruido 1: real", [(r["n"], r["real_s1.0"]) for r in f], "teal"), ("Ruido 2: real", [(r["n"], r["real_s2.0"]) for r in f], "grey")],
        x_label="Alternativas entre las que se elige (N)", y_label="Calidad de la ganadora (desviaciones)", x_ticks=ts, y_ticks=[0, 1, 2, 3, 4, 5], decimals=2, point_labels="last",
        note='Cuantas más alternativas y más ruido, mayor es la distancia entre lo que parece ganar y lo que vale: la ganadora suele ser la que el ruido favoreció. Calidad normal estándar y ruido gaussiano son supuestos del autor.', note_kind='coral', foot=SINT)


def se461_andamiaje_sin_uso() -> Fig:
    d = R("e461_andamiaje")
    items = [('Funciones generadas', d["funciones"], 'gold', str(d["funciones"])), ('Funciones sin uso', d["funciones_sin_uso"], 'coral', f'{d["funciones_sin_uso"]} ({p(d["pct_sin_uso"], 0)})'),
             ('Funciones que usa tu código', d["funciones"] - d["funciones_sin_uso"], 'teal', str(d["funciones"] - d["funciones_sin_uso"]))]
    return bars(f'Andamiaje de {d["entidades"]} entidades ({d["lineas_generadas"]} líneas): lo que tu código llega a usar',
               f'Barras con las funciones del andamiaje de {d["entidades"]} entidades: {d["funciones"]} generadas, {d["funciones_sin_uso"]} sin uso ({p(d["pct_sin_uso"], 0)}) y {d["funciones"] - d["funciones_sin_uso"]} usadas por el código propio.',
               items, 12.0, f'Generar es instantáneo; el costo aparece después, porque todo lo generado hay que entender, probar y mantener aunque no se use. Las {d["lineas_generadas"]} líneas contienen cero líneas de dominio. Las cuatro funciones usadas son un supuesto del autor.',
               label_w=250, width=940, note_kind='gold', foot=EJEC)


def se461_brecha_a_produccion() -> Fig:
    d = R("e461_brecha")
    items = [('Trabajo para producción', d["trabajo_total"], 'gold', f'{d["trabajo_total"]} puntos'), ('Pendiente en la mediana', d["mediana_restante"], 'coral', f'{int(d["mediana_restante"])} puntos'),
             ('Pendiente en el percentil 90', d["p90_restante"], 'coral', f'{d["p90_restante"]} puntos')]
    return bars(f'Un prototipo sintético frente a {d["atributos"]} atributos que producción exige (5 000 prototipos)',
               f'Barras con el trabajo necesario para llevar un prototipo a producción: {d["trabajo_total"]} puntos en total, {int(d["mediana_restante"])} pendientes en la mediana ({p(d["fraccion_pendiente_mediana"])}) y {d["p90_restante"]} en el percentil 90.',
               items, 440 / d["trabajo_total"], f'En la mediana queda pendiente el {p(d["fraccion_pendiente_mediana"])} del trabajo: el prototipo demostró la idea, no la ingeniería. Las probabilidades de que cada atributo ya exista y los puntos de esfuerzo son supuestos del autor.',
               label_w=270, width=940, note_kind='coral', foot=SINT)


# ---------------------------------------------------------------- SE-558
def se462_pruebas_copiadas() -> Fig:
    d = R("e462_pruebas")
    nom = {"peso_40_cambiado": "Peso del 40 % cambiado", "umbral_mayor": "Umbral mayor", "sin_redondeo": "Sin redondeo", "redondeo_cero": "Redondeo a cero",
           "examen_ignorado": "Examen ignorado", "promedio_max": "Promedio con el máximo", "estado_invertido": "Estado invertido", "peso_60_cambiado": "Peso del 60 % cambiado"}
    ks = list(d["detalle"])
    return heatmap(
        'Ocho mutantes de la función de nota final: lo que detecta cada estilo de prueba',
        f'Mapa de calor con qué estilo de prueba detecta cada uno de ocho mutantes de la nota final: copiar la salida actual en entradas típicas detecta {d["detectados_snapshot"]} de {d["mutantes"]} y derivar casos de la especificación con fronteras detecta {d["detectados_espec"]} de {d["mutantes"]}.',
        [nom[k] for k in ks], ["Copiar la salida actual", "Derivar de la especificación"],
        [[1 if d["detalle"][k]["snapshot"] else 0, 1 if d["detalle"][k]["espec"] else 0] for k in ks],
        unit="detección", row_title="Mutante", col_title="¿Lo detecta el estilo de prueba?",
        scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "lo detecta" if v else "no lo ve", cell_h=36, label_w=240,
        note='Una prueba que copia la salida acepta por construcción el comportamiento actual, defectuoso o no; los casos que apuntan a fronteras y a diferencias entre operaciones sí lo cuestionan. Los mutantes y los casos están escritos sabiendo qué se busca, así que 8 de 8 es una cota optimista.', note_kind='gold', foot=EJEC)


def se462_documentacion_que_deriva() -> Fig:
    d = R("e462_documentacion")
    return grouped_bars(
        'Documentación que dejó de ser cierta: lo que detecta doctest',
        f'Barras agrupadas con las funciones cuya documentación dejó de ser cierta: de {d["funciones"]} con ejemplo ejecutable {d["con_deriva"]} derivaron y doctest detecta {d["detectadas_doctest"]}; de {d["prosa_funciones"]} con descripción en prosa {d["prosa_con_deriva"]} derivaron y doctest detecta {d["prosa_detectadas_doctest"]}.',
        ["Con ejemplo ejecutable", "Con descripción en prosa"],
        [("Funciones", [d["funciones"], d["prosa_funciones"]], "grey"), ("Con deriva", [d["con_deriva"], d["prosa_con_deriva"]], "coral"), ("Detectadas por doctest", [d["detectadas_doctest"], d["prosa_detectadas_doctest"]], "teal")],
        unit="Funciones", ticks=[0, 5, 10, 15, 20, 25],
        note='La documentación que se ejecuta se vigila sola; la prosa envejece sin que nada falle. Pedir a un modelo que genere docstrings produce sobre todo prosa. Los grupos y las derivas son sintéticos y escritos por el autor.', note_kind='coral', foot=EJEC)


def se462_migracion_silenciosa() -> Fig:
    d = R("e462_migracion")
    return stacked_bars(
        '2 000 notas guardadas como texto en SQLite: migración ingenua frente a migración con validación',
        f'Barras apiladas con el destino de los {d["invalidas"]} valores inválidos de {d["filas"]} notas guardadas como texto: la conversión directa convierte sin error {d["ceros_silenciosos_ingenua"]} a 0,0 y {d["parciales_silenciosos_ingenua"]} parcialmente, sin cuarentena; la validación pone los {d["cuarentena"]} en cuarentena y migra {d["migradas_validada"]} notas válidas.',
        ["Conversión directa con CAST", "Validación y cuarentena"],
        [("Convertidos en silencio a 0,0", [d["ceros_silenciosos_ingenua"], 0], "coral"), ("Convertidos parcialmente en silencio", [d["parciales_silenciosos_ingenua"], 0], "gold"), ("En cuarentena", [0, d["cuarentena"]], "teal")],
        unit="Valores inválidos", horizontal=True, label_w=220,
        note='La conversión directa no falla: transforma «NP», vacíos y «5,5,0» en ceros o números parciales y deja el recuento intacto. Una migración generada sin esta verificación pasa cualquier revisión que cuente filas. La mezcla de valores es sintética.', note_kind='coral', foot=EJEC)


FIGURES = {
    "se-553-muestreo-y-mayoria.svg": se457_muestreo_y_mayoria,
    "se-553-confianza-no-es-exactitud.svg": se457_confianza_no_es_exactitud,
    "se-553-ventana-y-conjuntos.svg": se457_ventana_y_conjuntos,
    "se-554-requisitos-sin-decir.svg": se458_requisitos_sin_decir,
    "se-554-capas-de-validacion.svg": se458_capas_de_validacion,
    "se-554-instrucciones-que-chocan.svg": se458_instrucciones_que_chocan,
    "se-555-tamano-de-fragmento.svg": se459_tamano_de_fragmento,
    "se-555-memoria-que-caduca.svg": se459_memoria_que_caduca,
    "se-555-presupuesto-de-contexto.svg": se459_presupuesto_de_contexto,
    "se-556-politica-de-aceptacion.svg": se460_politica_de_aceptacion,
    "se-556-alcance-de-la-edicion.svg": se460_alcance_de_la_edicion,
    "se-556-retardo-de-sugerencias.svg": se460_retardo_de_sugerencias,
    "se-557-mejor-de-n.svg": se461_mejor_de_n,
    "se-557-andamiaje-sin-uso.svg": se461_andamiaje_sin_uso,
    "se-557-brecha-a-produccion.svg": se461_brecha_a_produccion,
    "se-558-pruebas-copiadas.svg": se462_pruebas_copiadas,
    "se-558-documentacion-que-deriva.svg": se462_documentacion_que_deriva,
    "se-558-migracion-silenciosa.svg": se462_migracion_silenciosa,
}
