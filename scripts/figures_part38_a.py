"""Figures for SE-457 to SE-462 (AI-assisted development: synthetic processes with fixed seeds and real runs of standard-library code).

Los números se calculan con scripts/experiments_part38_a.py para que figuras y texto no se transcriban a mano.
"""
from __future__ import annotations

from functools import lru_cache

import experiments_part38_a as ex
from figure_kit import Fig
from figures_part07_a import bars, tab

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


# ---------------------------------------------------------------- SE-457
def se457_muestreo_y_mayoria() -> Fig:
    f = R("e457_temperatura")["filas"]
    rows = [[n(r["T"]), p(r["p_correcta"] * 100), p(r["una_muestra"]), p(r["mayoria_de_5"]), p(r["alguna_de_5"])] for r in f]
    return tab('Cinco respuestas candidatas: la correcta es la segunda más probable (20 000 muestras por temperatura)',
              f'Tabla con la probabilidad de la respuesta correcta, el acierto con una muestra, con el voto de mayoría de cinco y con al menos una de cinco según la temperatura: a temperatura {n(f[0]["T"])} una muestra acierta {p(f[0]["una_muestra"])} y la mayoría {p(f[0]["mayoria_de_5"])}; a {n(f[2]["T"])} acierta {p(f[2]["una_muestra"])} y la mayoría {p(f[2]["mayoria_de_5"])}, y alguna de cinco incluye la correcta en {p(f[2]["alguna_de_5"])}.',
              ['Temperatura', 'Prob. de la correcta', 'Una muestra', 'Mayoría de 5', 'Alguna de 5 correcta'], rows, [150, 220, 170, 170, 200], row_h=48, size=13,
              note='Con temperatura baja el modelo repite con firmeza la respuesta más probable, que aquí es la incorrecta, y el voto de mayoría la confirma. Generar varias muestras ayuda a encontrar una correcta solo si algo externo (una prueba) puede reconocerla. Los logits son un supuesto del autor, no un modelo real.',
              note_kind='coral', foot=SINT)


def se457_confianza_no_es_exactitud() -> Fig:
    d = R("e457_calibracion")
    rows = [[t["tramo"], str(t["n"]), p(t["confianza"]), p(t["exactitud"])] for t in d["tramos"]]
    rows += [['Fáciles', str(d["faciles"]["n"]), p(d["faciles"]["confianza"]), p(d["faciles"]["exactitud"])],
             ['Difíciles', str(d["dificiles"]["n"]), p(d["dificiles"]["confianza"]), p(d["dificiles"]["exactitud"])]]
    return tab('1 000 preguntas sintéticas: la confianza declarada frente al acierto observado',
              f'Tabla con la confianza media declarada y la exactitud observada por tramo de confianza y por dificultad: globalmente {p(d["global"]["confianza"])} de confianza frente a {p(d["global"]["exactitud"])} de acierto, y en las preguntas difíciles {p(d["dificiles"]["confianza"])} de confianza frente a {p(d["dificiles"]["exactitud"])} de acierto.',
              ['Grupo', 'Preguntas', 'Confianza media', 'Exactitud observada'], rows, [260, 190, 230, 250], row_h=44, size=13,
              note=f'El error de calibración esperado es {n(d["ece"])} puntos y la confianza casi no distingue las preguntas fáciles de las difíciles: el tono seguro no informa de la dificultad. Que exista este patrón en un modelo real es una pregunta empírica; aquí es un supuesto del autor.',
              note_kind='gold', foot=SINT)


def se457_ventana_y_conjuntos() -> Fig:
    d = R("e457_ventana")
    rows = [[f'{r["ventana"]:,}'.replace(",", "."), p(r["fraccion_del_repositorio"]), p(r["conjuntos_que_caben"])] for r in d["filas"]]
    return tab('Un repositorio sintético de 120 archivos: qué cabe en la ventana de contexto',
              f'Tabla con el tamaño de la ventana en tokens, la fracción del repositorio que cabe y el porcentaje de conjuntos de trabajo de 8 archivos que caben: con 8.000 tokens caben {p(d["filas"][0]["conjuntos_que_caben"])} de los conjuntos, con 128.000 caben {p(d["filas"][2]["conjuntos_que_caben"])} y con 200.000 caben {p(d["filas"][3]["conjuntos_que_caben"])}, aunque el repositorio completo no cabe en ninguna.',
              ['Ventana (tokens)', 'Fracción del repositorio que cabe', 'Conjuntos de 8 archivos que caben'], rows, [250, 350, 330], row_h=44, size=13,
              note=f'El repositorio suma {n(d["tokens_totales"]/1e6, 2)} millones de tokens (tamaños lognormales con mediana {d["mediana"]}): ninguna ventana lo contiene, así que alguien decide qué entra. La distribución de tamaños y el recuento de 1 token ≈ 4 caracteres son supuestos del autor.',
              note_kind='teal', foot=SINT)


# ---------------------------------------------------------------- SE-458
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
    rows = []
    for k, v in d["por_defecto"].items():
        rows.append([nombres[k], str(v["n"]), f'{v["formato"]}', f'{v["formato_rango"]}', f'{v["formato_rango_coherencia"]}'])
    t = d["total"]
    rows.append(['Total', str(d["n"]), f'{t["formato"]}', f'{t["formato_rango"]}', f'{t["formato_rango_coherencia"]}'])
    return tab('200 salidas sintéticas con un defecto cada una: cuántas atrapa cada capa de validación',
              f'Tabla con seis tipos de defecto en 200 salidas y cuántas detecta cada capa acumulada: el formato detecta {t["formato"]}, formato y rango {t["formato_rango"]} y formato, rango y coherencia {t["formato_rango_coherencia"]}; ninguna capa detecta los dos decimales indebidos.',
              ['Defecto', 'Casos', 'Solo formato', '+ rango', '+ coherencia'], rows, [330, 100, 170, 140, 190], row_h=40, size=13,
              note=f'Tres capas baratas detectan {t["formato_rango_coherencia"]} de {d["n"]}; los {d["n"] - t["formato_rango_coherencia"]} restantes cumplen todas las reglas escritas y siguen mal. Lo que ninguna regla enuncia no se comprueba. Los seis defectos y su reparto son del autor.',
              note_kind='coral', foot=EJEC)


def se458_instrucciones_que_chocan() -> Fig:
    f = R("e458_conflicto")["filas"]
    rows = [[str(r["n"]), str(r["pares"]), p(r["q0.005"]), p(r["q0.02"])] for r in f]
    return tab('Probabilidad de que un conjunto de instrucciones no tenga ningún par en conflicto',
              f'Tabla con el número de instrucciones, el de pares y la probabilidad de que ninguno choque si cada par choca con probabilidad 0,5 por ciento o 2 por ciento: con 12 instrucciones {p(f[3]["q0.005"])} y {p(f[3]["q0.02"])}, y con 20 instrucciones {p(f[4]["q0.005"])} y {p(f[4]["q0.02"])}.',
              ['Instrucciones', 'Pares posibles', 'Sin conflicto (0,5 % por par)', 'Sin conflicto (2 % por par)'], rows, [190, 200, 280, 260], row_h=44, size=13,
              note='Los pares crecen con el cuadrado de las instrucciones, así que añadir reglas «por si acaso» vuelve casi seguro algún choque. La probabilidad por par es un supuesto del autor y supone pares independientes.',
              note_kind='gold', foot='Cálculo exacto (1 − q)^pares; no hay simulación ni modelo real.')


# ---------------------------------------------------------------- SE-459
def se459_tamano_de_fragmento() -> Fig:
    f = R("e459_fragmentos")["filas"]
    rows = [[str(r["tam"]), str(r["fragmentos"]), p(r["exacto_top1"]), p(r["doc_en_top3"]), str(r["tokens_por_consulta"])] for r in f]
    return tab('240 documentos de 900 palabras y un hecho escondido en cada uno: tamaño del fragmento (BM25 real)',
              f'Tabla con cinco medidas por tamaño de fragmento en palabras: con fragmentos de {f[0]["tam"]} palabras el fragmento correcto es el primero en {p(f[0]["exacto_top1"])} de las consultas y se envían {f[0]["tokens_por_consulta"]} palabras; con {f[3]["tam"]} es el primero en {p(f[3]["exacto_top1"])} y se envían {f[3]["tokens_por_consulta"]}.',
              ['Palabras por fragmento', 'Fragmentos', 'Hecho completo en el 1.º', 'Documento correcto en los 3 primeros', 'Palabras enviadas (3 fragmentos)'], rows, [160, 150, 220, 230, 190], row_h=64, size=13,
              note='Con una clave única la recuperación léxica acierta casi siempre en cualquier tamaño; los fragmentos pequeños parten algunos hechos por la frontera y los grandes cuestan 18 veces más contexto. La consulta con clave única es el caso más fácil: con paráfrasis o sin clave el resultado sería peor.',
              note_kind='teal', foot=EJEC)


def se459_memoria_que_caduca() -> Fig:
    f = R("e459_memoria")["filas"]
    rows = [[r["ttl"], p(r["erroneas"]), n(r["refrescos_por_hecho"])] for r in f]
    return tab('Hechos que cambian el 1 % de los días: respuestas obsoletas según la caducidad de la memoria (180 días)',
              f'Tabla con la caducidad de la memoria, el porcentaje de respuestas obsoletas y los refrescos por hecho: sin caducidad {p(f[0]["erroneas"])} de respuestas obsoletas, con 30 días {p(f[2]["erroneas"])} y con 7 días {p(f[3]["erroneas"])} a cambio de {n(f[3]["refrescos_por_hecho"])} refrescos por hecho.',
              ['Caducidad', 'Respuestas obsoletas', 'Refrescos por hecho'], rows, [330, 300, 290], row_h=44, size=13,
              note='Una memoria sin caducidad envejece hasta responder mal más de la mitad de las veces; acortar la caducidad compra frescura con cargas de lectura. La tasa de cambio del 1 % diario es un supuesto del autor y cada hecho cambia por separado.',
              note_kind='gold', foot=SINT)


def se459_presupuesto_de_contexto() -> Fig:
    d = R("e459_presupuesto")
    m = d["medias"]
    items = [('Al azar', m["aleatorio"], 'coral', n(m["aleatorio"], 2)), ('Por relevancia', m["relevancia"], 'gold', n(m["relevancia"], 2)), ('Por relevancia por token', m["densidad"], 'teal', n(m["densidad"], 2))]
    return bars('Relevancia total empaquetada en 3 000 tokens con 30 fragmentos candidatos (300 repeticiones)',
               f'Barras con la relevancia media empaquetada en un presupuesto de 3.000 tokens: {n(m["aleatorio"], 2)} al azar, {n(m["relevancia"], 2)} ordenando por relevancia y {n(m["densidad"], 2)} ordenando por relevancia por token, {p(d["mejora_densidad_vs_relevancia"])} más que la segunda.',
               items, 90.0, f'Elegir lo más relevante a secas gasta el presupuesto en fragmentos grandes; dividir por el tamaño mete {p(d["mejora_densidad_vs_relevancia"])} más relevancia. Las relevancias y tamaños son del autor y la relevancia se supone conocida, algo que en la práctica se estima con error.',
               label_w=250, width=940, note_kind='teal', foot=SINT)


# ---------------------------------------------------------------- SE-460
def se460_politica_de_aceptacion() -> Fig:
    f = R("e460_aceptacion")["filas"]
    rows = [[r["politica"], str(r["aceptadas"]), str(r["defectos_aceptados"]), p(100 * r["defectos_aceptados"] / r["aceptadas"])] for r in f]
    return tab('1 000 sugerencias sintéticas (78 % correctas): defectos que entran según cómo se acepta',
              f'Tabla con tres políticas de aceptación de 1.000 sugerencias: aceptar sin leer deja entrar {f[0]["defectos_aceptados"]} defectos, leer solo las largas {f[1]["defectos_aceptados"]} y leer siempre y ejecutar {f[2]["defectos_aceptados"]} a cambio de aceptar menos sugerencias.',
              ['Política', 'Sugerencias aceptadas', 'Defectos aceptados', 'Defectos por cada 100 aceptadas'], rows, [330, 200, 200, 190], row_h=48, size=13,
              note='Leer y ejecutar cuesta tiempo y reduce lo aceptado, pero deja entrar una quinta parte de los defectos. La tasa de acierto del 78 % y las tasas de detección del revisor son supuestos del autor; no miden ninguna herramienta ni persona.',
              note_kind='coral', foot=SINT)


def se460_alcance_de_la_edicion() -> Fig:
    d = R("e460_alcance")
    rows = [['Edición dirigida (una condición)', str(d["diff_dirigido"]), p(d["p_detectar_dirigido"])],
            ['Archivo regenerado con deriva cosmética', str(d["diff_regenerado"]), p(d["p_detectar_regenerado"])]]
    return tab(f'Corregir una condición en un archivo de {d["lineas_archivo"]} líneas: líneas de diferencia que debe revisar la persona',
              f'Tabla con dos formas de aplicar el mismo arreglo en un archivo de {d["lineas_archivo"]} líneas: la edición dirigida cambia {d["diff_dirigido"]} líneas y se detecta con probabilidad {p(d["p_detectar_dirigido"])}; regenerar el archivo cambia {d["diff_regenerado"]} por deriva cosmética y la probabilidad cae a {p(d["p_detectar_regenerado"])}.',
              ['Forma de aplicar el cambio', 'Líneas distintas (difflib)', 'Prob. de encontrar el cambio real'], rows, [380, 270, 280], row_h=48, size=13,
              note='Las líneas se miden con difflib sobre un archivo real generado; la probabilidad de detección usa una curva del autor que decae con el tamaño del diff, así que esa columna es un modelo y no una medición de personas.',
              note_kind='gold', foot=EJEC)


def se460_retardo_de_sugerencias() -> Fig:
    f = R("e460_debounce")["filas"]
    rows = [[str(r["retardo_ms"]), str(r["peticiones"]), str(r["utiles"]), p(100 * r["utiles"] / r["peticiones"])] for r in f]
    return tab('467 pulsaciones sintéticas: peticiones de sugerencia según el retardo antes de pedir',
              f'Tabla con el retardo en milisegundos, las peticiones, las útiles y la fracción útil: sin retardo {f[0]["peticiones"]} peticiones para {f[0]["utiles"]} útiles, y con 600 milisegundos {f[3]["peticiones"]} peticiones para las mismas {f[3]["utiles"]}.',
              ['Retardo (ms)', 'Peticiones al modelo', 'Peticiones útiles', 'Fracción útil'], rows, [210, 260, 240, 220], row_h=44, size=13,
              note='Esperar a que la escritura se detenga elimina casi todo el gasto sin perder las pausas donde la sugerencia se habría mostrado. El ritmo de escritura y la regla «útil si hay una pausa de 0,5 s» son supuestos del autor; con otra persona cambiarían.',
              note_kind='teal', foot=EJEC)


# ---------------------------------------------------------------- SE-461
def se461_mejor_de_n() -> Fig:
    f = R("e461_mejor_de_n")["filas"]
    rows = [[str(r["n"]), n(r["real_s0.0"], 2), f'{n(r["medida_s1.0"], 2)} → {n(r["real_s1.0"], 2)}', f'{n(r["medida_s2.0"], 2)} → {n(r["real_s2.0"], 2)}'] for r in f]
    return tab('Elegir la mejor de N alternativas: calidad medida de la ganadora → calidad real (en desviaciones)',
              f'Tabla con la calidad de la mejor de N alternativas: con un evaluador perfecto crece de {n(f[0]["real_s0.0"], 2)} a {n(f[4]["real_s0.0"], 2)}; con ruido 1 la ganadora de 20 se mide en {n(f[4]["medida_s1.0"], 2)} pero vale {n(f[4]["real_s1.0"], 2)}, y con ruido 2 se mide en {n(f[4]["medida_s2.0"], 2)} pero vale {n(f[4]["real_s2.0"], 2)}.',
              ['Alternativas (N)', 'Evaluador exacto', 'Ruido 1: medida → real', 'Ruido 2: medida → real'], rows, [200, 220, 260, 250], row_h=44, size=13,
              note='Cuantas más alternativas y más ruido, mayor es la distancia entre lo que parece ganar y lo que vale: la ganadora suele ser la que el ruido favoreció. Calidad normal estándar y ruido gaussiano son supuestos del autor.',
              note_kind='coral', foot=SINT)


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
               items, 11.0, f'En la mediana queda pendiente el {p(d["fraccion_pendiente_mediana"])} del trabajo: el prototipo demostró la idea, no la ingeniería. Las probabilidades de que cada atributo ya exista y los puntos de esfuerzo son supuestos del autor.',
               label_w=270, width=940, note_kind='coral', foot=SINT)


# ---------------------------------------------------------------- SE-462
def se462_pruebas_copiadas() -> Fig:
    d = R("e462_pruebas")
    rows = [['Copiar la salida actual en entradas típicas', f'{d["detectados_snapshot"]} de {d["mutantes"]}'], ['Derivar casos de la especificación (fronteras)', f'{d["detectados_espec"]} de {d["mutantes"]}']]
    return tab('Ocho mutantes de la función de nota final: lo que detecta cada estilo de prueba',
              f'Tabla con dos estilos de prueba frente a ocho mutantes de la nota final: copiar la salida actual en entradas típicas detecta {d["detectados_snapshot"]} y derivar casos de la especificación con fronteras detecta {d["detectados_espec"]}.',
              ['Estilo de prueba', 'Mutantes detectados'], rows, [600, 330], row_h=48, size=13,
              note='Una prueba que copia la salida acepta por construcción el comportamiento actual, defectuoso o no; los casos que apuntan a fronteras y a diferencias entre operaciones sí lo cuestionan. Los mutantes y los casos están escritos sabiendo qué se busca, así que 8 de 8 es una cota optimista.',
              note_kind='gold', foot=EJEC)


def se462_documentacion_que_deriva() -> Fig:
    d = R("e462_documentacion")
    rows = [['Funciones con ejemplo ejecutable', str(d["funciones"]), str(d["con_deriva"]), str(d["detectadas_doctest"])],
            ['Funciones con descripción en prosa', str(d["prosa_funciones"]), str(d["prosa_con_deriva"]), str(d["prosa_detectadas_doctest"])]]
    return tab('Documentación que dejó de ser cierta: lo que detecta doctest',
              f'Tabla con dos grupos de funciones: de {d["funciones"]} con ejemplo ejecutable {d["con_deriva"]} derivaron y doctest detecta {d["detectadas_doctest"]}; de {d["prosa_funciones"]} con descripción en prosa {d["prosa_con_deriva"]} derivaron y doctest detecta {d["prosa_detectadas_doctest"]}.',
              ['Tipo de documentación', 'Funciones', 'Con deriva', 'Detectadas por doctest'], rows, [380, 150, 170, 230], row_h=48, size=13,
              note='La documentación que se ejecuta se vigila sola; la prosa envejece sin que nada falle. Pedir a un modelo que genere docstrings produce sobre todo prosa. Los grupos y las derivas son sintéticos y escritos por el autor.',
              note_kind='coral', foot=EJEC)


def se462_migracion_silenciosa() -> Fig:
    d = R("e462_migracion")
    rows = [['Conversión directa con CAST', str(d["filas"]), f'{d["ceros_silenciosos_ingenua"]} a 0,0 y {d["parciales_silenciosos_ingenua"]} parciales', '0'],
            ['Validación y cuarentena', str(d["filas"]), f'{d["migradas_validada"]} migradas', str(d["cuarentena"])]]
    return tab('2 000 notas guardadas como texto en SQLite: migración ingenua frente a migración con validación',
              f'Tabla con dos migraciones de 2.000 notas de texto a número: la conversión directa convierte sin error {d["invalidas"]} valores inválidos ({d["ceros_silenciosos_ingenua"]} a cero y {d["parciales_silenciosos_ingenua"]} a un número parcial) y la validación migra {d["migradas_validada"]} y aparta {d["cuarentena"]} en cuarentena.',
              ['Estrategia', 'Filas', 'Resultado', 'En cuarentena'], rows, [330, 120, 340, 140], row_h=64, size=13,
              note='La conversión directa no falla: transforma «NP», vacíos y «5,5,0» en ceros o números parciales y deja el recuento intacto. Una migración generada sin esta verificación pasa cualquier revisión que cuente filas. La mezcla de valores es sintética.',
              note_kind='coral', foot=EJEC)


FIGURES = {
    "se-457-muestreo-y-mayoria.svg": se457_muestreo_y_mayoria,
    "se-457-confianza-no-es-exactitud.svg": se457_confianza_no_es_exactitud,
    "se-457-ventana-y-conjuntos.svg": se457_ventana_y_conjuntos,
    "se-458-requisitos-sin-decir.svg": se458_requisitos_sin_decir,
    "se-458-capas-de-validacion.svg": se458_capas_de_validacion,
    "se-458-instrucciones-que-chocan.svg": se458_instrucciones_que_chocan,
    "se-459-tamano-de-fragmento.svg": se459_tamano_de_fragmento,
    "se-459-memoria-que-caduca.svg": se459_memoria_que_caduca,
    "se-459-presupuesto-de-contexto.svg": se459_presupuesto_de_contexto,
    "se-460-politica-de-aceptacion.svg": se460_politica_de_aceptacion,
    "se-460-alcance-de-la-edicion.svg": se460_alcance_de_la_edicion,
    "se-460-retardo-de-sugerencias.svg": se460_retardo_de_sugerencias,
    "se-461-mejor-de-n.svg": se461_mejor_de_n,
    "se-461-andamiaje-sin-uso.svg": se461_andamiaje_sin_uso,
    "se-461-brecha-a-produccion.svg": se461_brecha_a_produccion,
    "se-462-pruebas-copiadas.svg": se462_pruebas_copiadas,
    "se-462-documentacion-que-deriva.svg": se462_documentacion_que_deriva,
    "se-462-migracion-silenciosa.svg": se462_migracion_silenciosa,
}
