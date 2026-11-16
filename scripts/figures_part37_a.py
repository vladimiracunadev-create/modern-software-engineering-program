"""Figuras de SE-445 a SE-450: datos sintéticos con semilla fija y ejecuciones de código propio sobre datos sintéticos (CPython 3.12.9 en Windows 11, repetido con 3.12.3 en Ubuntu bajo WSL2)."""
from __future__ import annotations

from figure_kit import Fig, fmt_es, grouped_bars, line_chart, percentile_intervals, scatter

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."


# ---------------------------------------------------------------- SE-445
def se445_redes_y_siembra() -> Fig:
    return grouped_bars('Qué siembra produce adopción',
                        'Barras agrupadas con 2 000 redes sintéticas de 30 personas y cuatro siembras de una práctica: con solo un anuncio general la adopción es nula en el 100 por ciento de las redes, con dos personas al azar la mediana es 93,3 por ciento y 63,2 por ciento de las redes pasan del 80 por ciento, con dos muy conectadas 96,7 y 95,7 por ciento, y con dos poco conectadas 6,7 y 11,4 por ciento.',
                        ['Solo un anuncio general', '2 personas al azar', '2 personas muy conectadas', '2 personas poco conectadas'],
                        [('Adopción final (mediana)', [0.0, 93.3, 96.7, 6.7], 'teal'), ('Redes con 80 % o más', [0.0, 63.2, 95.7, 11.4], 'gold'), ('Redes que no pasan del 10 %', [100.0, 14.4, 0.2, 72.7], 'coral')],
                        unit='% de personas o de redes', decimals=1,
                        note='Cada grupo es una forma de empezar; la barra verde azulada dice cuánto del equipo termina usando la práctica y las otras dos cuántas redes llegan lejos o se quedan inmóviles. La diferencia entre las dos últimas es la lección: son dos personas en ambos casos, y el resultado va de casi todo a casi nada según dónde están.',
                        note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-445
def se445_cuello_de_aprobacion() -> Fig:
    return grouped_bars('Cuánto espera una decisión',
                        'Barras agrupadas con la espera de una decisión según cuántas aprueba una sola persona: con 5 por día y utilización de 87,5 por ciento la espera media es 9,4 horas y el percentil 90 22,8; con 2 por día y 35 por ciento 0,8 y 2,7; con 1 por día y 17,5 por ciento 0,3 y 0,9.',
                        ['Una persona aprueba todo (5 por día · utilización 87,5 %)', 'Aprueba el 40 % (2 por día · 35,0 %)', 'Criterios delegados (1 por día · 17,5 %)'],
                        [('Espera media', [9.4, 0.8, 0.3], 'teal'), ('Espera p90', [22.8, 2.7, 0.9], 'coral')],
                        unit='horas de espera', decimals=1,
                        note='La utilización pasa de 17,5 % a 87,5 % y la espera media se multiplica por más de treinta, no por cinco: la espera no es proporcional a la carga. El percentil 90 muestra que una decisión de cada diez espera casi tres jornadas.',
                        note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-445
def se445_consulta_previa() -> Fig:
    return grouped_bars('Cuántas decisiones se revierten',
                        'Barras con 6 000 decisiones sintéticas: sin consulta previa por escrito se revierte el 29,9 por ciento y cuesta 4,49 días de trabajo por decisión; con 2 personas que leen 21,7 por ciento y 4,75 días, con 4 personas 13,9 por ciento y 4,09 días y con 8 personas 5,9 por ciento y 3,89 días.',
                        ['0 personas leen antes (4,49 días por decisión)', '2 personas (4,75 días)', '4 personas (4,09 días)', '8 personas (3,89 días)'],
                        [('Decisiones revertidas', [29.9, 21.7, 13.9, 5.9], 'coral')],
                        unit='% de decisiones revertidas', decimals=1,
                        note='Entre paréntesis, los días de trabajo por decisión (consulta más reversión). Las reversiones bajan con cada persona que lee, pero el costo total no baja de inmediato: consultar a dos personas cuesta más días que no consultar a nadie, porque el beneficio no compensa aún el costo fijo de preparar y esperar. El balance mejora con cuatro y con ocho.',
                        note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-446
def se446_factor_de_camion() -> Fig:
    return grouped_bars('Cuántas personas deben irse',
                        'Barras con 200 repositorios sintéticos de 300 archivos y 8 personas: con un autor por archivo y reparto concentrado la salida de la persona más cargada deja sin conocedor al 37 por ciento de los archivos, con reparto uniforme 15,4 por ciento, con dos conocedores por archivo y con dos conocedores y rotación 0 por ciento; el factor de camión mediano sube de 2 a 4, 5,5 y 6.',
                        ['Un autor por archivo, reparto concentrado (factor 2)', 'Un autor por archivo, reparto uniforme (factor 4)', 'Dos conocedores por archivo (factor 5,5)', 'Dos conocedores y rotación (factor 6)'],
                        [('Archivos sin conocedor al irse la persona más cargada', [37.0, 15.4, 0.0, 0.0], 'coral')],
                        unit='% de archivos sin conocedor', horizontal=True, label_w=320, decimals=1,
                        note='Cada fila es una política de reparto; el factor de camión, entre paréntesis, dice cuántas personas habría que perder para dejar sin conocedor a la mitad del código, y la barra cuánto se pierde si se va solo la persona que más sabe. La diferencia entre un autor concentrado y dos conocedores por archivo es lo que compra la revisión por un segundo conocedor.',
                        note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-446
def se446_fronteras_y_relevos() -> Fig:
    return grouped_bars('Cuántos equipos cruza un cambio',
                        'Barras con 5 000 cambios sintéticos sobre cuatro dominios y tres capas: con equipos por capa el plazo estimado es de 5,9 días, un cambio cruza 2,31 equipos y el 81 por ciento requiere relevo; con equipos por dominio el plazo es de 2,6 días, cruza 1,21 y el 21,1 por ciento requiere relevo.',
                        ['Equipos por capa (2,31 equipos por cambio · 81,0 % requiere relevo)', 'Equipos por dominio (1,21 equipos · 21,1 % requiere relevo)'],
                        [('Plazo estimado', [5.9, 2.6], 'coral')],
                        unit='días de plazo estimado', horizontal=True, label_w=330, decimals=1,
                        note='Cada barra es una forma de cortar el mismo trabajo; el plazo baja a menos de la mitad porque los relevos desaparecen, no porque se trabaje más rápido.',
                        note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-446
def se446_carga_de_guardia() -> Fig:
    ps = [3, 4, 6, 8]
    avisos = ['27,0', '19,5', '13,5', '10,5']
    return line_chart('Cuánta guardia recibe cada persona',
                      'Líneas con las semanas por persona y año de una guardia semanal con 1,5 avisos por semana fuera de horario: de 3 a 8 personas las semanas de guardia bajan de 18 a 7 y las semanas con tres o más avisos de 3,45 a 1,33, mientras los avisos por persona bajan de 27 a 10,5 al año.',
                      [('Semanas de guardia al año', [(p, v, fmt_es(v), 't') for p, v in zip(ps, [18, 13, 9, 7])], 'teal'),
                       ('Semanas con 3 o más avisos por persona y año', [(p, v, fmt_es(v, 2), 'b') for p, v in zip(ps, [3.45, 2.48, 1.73, 1.33])], 'coral')],
                      x_label='Personas en la rotación (entre paréntesis, avisos fuera de horario por persona y año)', y_label='Semanas por persona y año',
                      x_ticks=[(p, f'{p} ({a})') for p, a in zip(ps, avisos)], y_ticks=[0, 5, 10, 15, 20],
                      note='El número de avisos por persona baja en proporción al tamaño de la rotación, pero las semanas malas (tres o más avisos) bajan más despacio: aunque la media baje, siempre habrá semanas duras.',
                      note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-447
def se447_estimar_en_grupo() -> Fig:
    return grouped_bars('Cuánto distorsiona hablar en orden',
                        'Barras con 5 000 ensayos sintéticos de una estimación de grupo de siete personas sobre una cantidad real de 100 días: si escriben solas y luego se muestran el error mediano es 8,4 por ciento y el 22,9 por ciento de los ensayos supera el 15; si hablan en orden sin sesgo 9,8 y 30,7; y si abre una persona sénior con un valor 30 por ciento mayor 16 y 52,8.',
                        ['Escriben solas y luego se muestran', 'Se habla en orden, sin sesgo del primero', 'Se habla en orden y la persona sénior (+30 %) abre'],
                        [('Error mediano del promedio', [8.4, 9.8, 16.0], 'gold'), ('Ensayos con error mayor al 15 %', [22.9, 30.7, 52.8], 'coral')],
                        unit='% del valor real o de los ensayos', decimals=1,
                        note='La primera categoría es la referencia: el promedio de estimaciones independientes. Hablar en orden ya la empeora, y un sesgo del primero la duplica; más de la mitad de las sesiones de la última yerra por más del 15 %.',
                        note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-447
def se447_campos_que_se_pierden() -> Fig:
    rs = [1, 2, 4]
    return line_chart('Cuántos campos sobreviven a los relevos',
                      'Líneas con el porcentaje de mensajes de decisión completos tras varios relevos: el oral llega completo en 26,2 por ciento tras un relevo, 6,7 tras dos y 0,5 tras cuatro; el correo libre 49,6, 24,7 y 5,5; la plantilla con acuse 88,0, 76,7 y 58,3.',
                      [('Plantilla con acuse', [(r, v, fmt_es(v, 1), 't') for r, v in zip(rs, [88.0, 76.7, 58.3])], 'teal'), ('Correo libre', [(r, v, fmt_es(v, 1), 't') for r, v in zip(rs, [49.6, 24.7, 5.5])], 'gold'),
                       ('Oral', [(r, v, fmt_es(v, 1), 'l' if r == 4 else 'b') for r, v in zip(rs, [26.2, 6.7, 0.5])], 'coral')],
                      x_label='Relevos que atraviesa el mensaje', y_label='Mensajes completos (%)', x_ticks=[(r, str(r)) for r in rs], y_ticks=[0, 20, 40, 60, 80, 100],
                      note='Tras cuatro relevos el motivo se conserva en el 17,6 % de los mensajes orales, el 40,8 % de los correos libres y el 84,6 % de las plantillas con acuse. Incluso con la plantilla, solo el 58,3 % del mensaje llega completo; el oral prácticamente no sobrevive. El motivo, que explica cómo adaptar la decisión, cae más rápido que el resto en los formatos libres.',
                      note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-447
def se447_conflicto_con_ruido() -> Fig:
    return grouped_bars('Qué estrategia aguanta un malentendido',
                        'Barras agrupadas con partidas sintéticas de 200 rondas con 5 por ciento de malentendidos: contra sí misma el ojo por ojo obtiene 2,29 puntos por ronda, el generoso 2,85, el que siempre coopera 2,95 y el que siempre ataca 1,15, y en promedio contra las cuatro estrategias 2,31, 2,34, 2,21 y 2,39.',
                        ['Ojo por ojo', 'Ojo por ojo generoso', 'Siempre coopera', 'Siempre ataca'],
                        [('Pago por ronda contra sí misma', [2.29, 2.85, 2.95, 1.15], 'teal'), ('Pago promedio contra las cuatro estrategias', [2.31, 2.34, 2.21, 2.39], 'gold')],
                        unit='puntos por ronda', decimals=2,
                        note='Contra una igual, un malentendido hace caer el ojo por ojo estricto de 3 a 2,29 porque las represalias se alternan; la versión generosa lo recupera hasta 2,85. La barra dorada muestra el límite: contra una mezcla que incluye a quien siempre ataca, esa estrategia obtiene el promedio más alto y quien siempre coopera, el más bajo.',
                        note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-448
def se448_tareas_que_estiran() -> Fig:
    return scatter('Qué tareas hacen crecer',
                   'Puntos con el nivel final mediano y las semanas de fracaso al año de 1 000 personas simuladas durante 52 semanas con nivel inicial 3: tareas fáciles 3,07 y 0,3, calibradas 8,87 y 6,2, muy difíciles 3,04 y 37,9 y de dificultad al azar 4,8 y 14; solo las calibradas hacen crecer.',
                   [('Fáciles (nivel − 2)', [(0.3, 3.07, '3,07', 'r')], 'teal'), ('Calibradas (nivel + 1)', [(6.2, 8.87, '8,87', 'r')], 'gold'), ('Muy difíciles (nivel + 4)', [(37.9, 3.04, '3,04', 'l')], 'coral'),
                    ('Dificultad al azar', [(14.0, 4.8, '4,80', 'r')], 'navy')],
                   x_label='Semanas con fracaso al año', y_label='Nivel final (mediana)', x_ticks=[(x, str(x)) for x in (0, 10, 20, 30, 40)], y_ticks=[0, 3, 6, 9],
                   note='Las tareas fáciles y las muy difíciles dejan casi igual el nivel final (de 3 a 3,07 y 3,04), por razones opuestas: una no enseña y la otra fracasa casi todas las semanas. Las calibradas aceptan semanas de fracaso (6 de 52) como costo del aprendizaje.',
                   note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-448
def se448_cuando_llega_el_aviso() -> Fig:
    return grouped_bars('Cuánto cuesta esperar la retroalimentación',
                        'Barras con los errores repetidos en 12 semanas de 4 000 personas simuladas con un hábito erróneo en el 30 por ciento de cinco cambios semanales: 3,4 con retroalimentación en el mismo cambio, 4,3 a los 2 días, 4,7 en la revisión semanal y 14,3 en la evaluación trimestral a los 60 días.',
                        ['En el mismo cambio', 'A los 2 días', 'En la revisión semanal', 'En la evaluación trimestral (60 días)'],
                        [('Errores repetidos en 12 semanas', [3.4, 4.3, 4.7, 14.3], 'coral')],
                        unit='errores repetidos en 12 semanas', decimals=1,
                        note='Pasar de la retroalimentación inmediata a la semanal añade poco (de 3,4 a 4,7); pasar a la trimestral la cuadruplica. El costo no es lineal en el retraso: se pierde el aprendizaje de varias semanas de trabajo.',
                        note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-448
def se448_ruido_de_evaluacion() -> Fig:
    return grouped_bars('Cuánto ruido hay en una evaluación',
                        'Barras con 300 grupos simulados de 200 personas evaluadas por una o tres evaluadoras: una evaluadora sin rúbrica promueve al 58,7 por ciento del 20 por ciento mejor, con una correlación de 0,73 con el desempeño verdadero; tres sin rúbrica 74,1 y 0,89; tres con rúbrica calibrada 85,9 y 0,97.',
                        ['Una evaluadora, sin rúbrica (correlación 0,73)', 'Tres evaluadoras, sin rúbrica (0,89)', 'Tres evaluadoras con rúbrica calibrada (0,97)'],
                        [('Del 20 % mejor, promovidas', [58.7, 74.1, 85.9], 'teal')],
                        unit='% del 20 % mejor que es promovido', horizontal=True, label_w=320, decimals=1, ticks=[0, 25, 50, 75, 100],
                        note='Entre paréntesis, la correlación con el desempeño verdadero. Con una sola evaluadora y sin rúbrica, cuatro de cada diez personas que merecían promoción no la reciben aunque el desempeño exista y se mide con ruido. Añadir evaluadoras ayuda y la rúbrica calibrada ayuda más.',
                        note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-449
def se449_suma_de_medianas() -> Fig:
    return grouped_bars('Por qué la suma de medianas no se cumple',
                        'Barras agrupadas con 20 000 proyectos simulados de doce tareas con mediana de cinco días y suma de medianas de 60 días: con tareas independientes los percentiles 50, 85 y 95 son 70,5, 85,7 y 96,4 días y la probabilidad de terminar en 60 es 19,3 por ciento; con un factor común de dificultad 68,9, 93,4 y 111,7 días y 31,9 por ciento.',
                        ['Tareas independientes (19,3 % termina en 60 días)', 'Con un factor común de dificultad (31,9 %)'],
                        [('p50', [70.5, 68.9], 'teal'), ('p85', [85.7, 93.4], 'gold'), ('p95', [96.4, 111.7], 'coral')],
                        unit='días del proyecto', decimals=1, ref_lines=[(60, '60 d')],
                        note='La línea discontinua es la suma de medianas, 60 días. La suma de medianas se cumple una de cada cinco veces con tareas independientes y una de cada tres con un factor común. El factor común no desplaza la mediana, ensancha la cola: el percentil 95 pasa de 96 a 112 días.',
                        note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-449
def se449_pronostico_por_flujo() -> Fig:
    return percentile_intervals('Cuántas semanas necesita un backlog de 60 elementos',
                                'Rangos del percentil 85 del pronóstico de 60 elementos según las semanas de historial: con 6 semanas la mediana es 15 y el rango de 12 a 21, con 12 de 13 a 20, con 24 de 13 a 18 y con 48 de 14 a 17; la media del historial de 20 semanas da 13 semanas con 70,6 por ciento de probabilidad.',
                                [('Historial de 6 semanas', [12, 15, 21]), ('Historial de 12 semanas', [13, 15, 20]), ('Historial de 24 semanas', [13, 15, 18]), ('Historial de 48 semanas', [14, 15, 17])],
                                unit='semanas para entregar 60 elementos (p85)', marks=('p10', 'mediana', 'p90'), decimals=0, ref_lines=[(13, 'media: 13')],
                                note='Con un historial de 20 semanas y entrega media de 4,95 la fecha de la media es 60 / 4,95 = 13 semanas, con 70,6 % de probabilidad de cumplirla; la simulación da p50 13, p85 14 y p95 16 semanas. El percentil 85 añade una semana. Cada fila usa 200 repeticiones: con seis semanas de historial, el mismo pronóstico oscila entre doce y veintiuna semanas según qué seis semanas se tuvieron.',
                                note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-449
def se449_ciclo_y_carga() -> Fig:
    cs = [50, 70, 85, 95]
    return line_chart('Qué ocurre cuando el equipo está lleno',
                      'Líneas con el ciclo de elementos simulados en una cola de un servidor según la carga: el ciclo medio es 2 unidades de trabajo con 50 por ciento, 3,3 con 70, 6,7 con 85 y 18,2 con 95 frente a 20 teórico, y el percentil 90 es 4,6, 7,7, 15,1 y 42; la curva se dispara al acercarse al 100 por ciento.',
                      [('Ciclo p90', [(c, v, fmt_es(v, 1), 't') for c, v in zip(cs, [4.6, 7.7, 15.1, 42.0])], 'coral'), ('Valor teórico 1/(1 − carga)', [(c, v, fmt_es(v, 1) if c == 95 else '', 't') for c, v in zip(cs, [2.0, 3.3, 6.7, 20.0])], 'grey'),
                       ('Ciclo medio', [(c, v, fmt_es(v, 1) if c == 95 else '', 'b') for c, v in zip(cs, [2.0, 3.3, 6.7, 18.2])], 'teal')],
      point_labels='none', x_label='Carga del equipo (%)', y_label='Ciclo (unidades de trabajo)', x_ticks=[(c, f'{c} %') for c in cs], y_ticks=[0, 10, 20, 30, 40, 50],
                      note='Pasar de 70 % a 95 % de carga multiplica el ciclo por más de cinco; el percentil 90 de un equipo al 95 % es de 42 veces el trabajo del elemento. La simulación coincide con la fórmula teórica salvo al 95 %, donde 60 000 elementos no bastan para promediar la cola.',
                      note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-450
def se450_matriz_y_valor_esperado() -> Fig:
    return grouped_bars('Qué fracción del riesgo cubren los cinco primeros',
                        'Barras con 400 carteras sintéticas de 30 riesgos de los que se eligen cinco para mitigar: ordenar por valor esperado cubre el 72,2 por ciento de la pérdida esperada, una matriz de cinco por cinco cubre el 65,8 por ciento y deja fuera el mayor riesgo en el 8,5 por ciento de las carteras, y elegir al azar cubre el 16,6 por ciento.',
                        ['Valor esperado (deja fuera el mayor riesgo: 0 % por definición)', 'Matriz 5×5 (lo deja fuera en el 8,5 % de las carteras)', 'Azar'],
                        [('Pérdida esperada cubierta', [72.2, 65.8, 16.6], 'teal')],
                        unit='% de la pérdida esperada cubierta', horizontal=True, label_w=330, decimals=1, ticks=[0, 25, 50, 75, 100],
                        note='La matriz es mucho mejor que el azar y algo peor que el valor esperado: pierde 6,4 puntos de cobertura. En una de cada doce carteras deja fuera el riesgo más caro.',
                        note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-450
def se450_valor_de_la_informacion() -> Fig:
    return grouped_bars('Cuánto vale saber antes de decidir',
                        'Barras agrupadas con el valor de la información en una inversión de valor neto incierto con desviación 100 y un experimento con ruido de 40: con valor esperado a priori de menos 20 la información perfecta vale 30,6 y el experimento 27,8, con valor esperado cero 39,8 y 36,9, y con más 20 vale 30,6 y 27,7.',
                        ['Valor esperado a priori −20', 'Valor esperado a priori 0', 'Valor esperado a priori +20 (20,0 sin información)'],
                        [('Información perfecta (simulado)', [30.6, 39.8, 30.6], 'teal'), ('Experimento ruidoso', [27.8, 36.9, 27.7], 'gold')],
                        unit='valor de la información', decimals=1,
                        note='El valor analítico de la información perfecta es 30,7, 39,9 y 30,7. La información vale más cuando la decisión está en el límite (valor esperado cero: 39,8) y menos cuando se inclina hacia un lado. El experimento ruidoso captura entre el 90 y el 93 % de ese valor, así que cualquier experimento que cueste menos de 27 es rentable en el caso central, y uno que cueste 40 nunca lo es.',
                        note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-450
def se450_escalar_lo_que_corresponde() -> Fig:
    return grouped_bars('Cuánto cuesta decidir a qué nivel',
                        'Barras agrupadas con el costo trimestral de 200 decisiones durante 3 000 trimestres con 30 por ciento irreversibles: escalar todo cuesta 407 de mediana y 487 en el percentil 90, escalar solo lo irreversible 301,5 y 382, y no escalar nada 369,5 y 463,5.',
                        ['Todo se escala', 'Solo se escala lo irreversible', 'Nada se escala'],
                        [('Costo trimestral (mediana)', [407.0, 301.5, 369.5], 'teal'), ('Costo p90', [487.0, 382.0, 463.5], 'coral')],
                        unit='costo trimestral', decimals=1,
                        note='Escalar todo es la política más cara porque paga la espera de las decisiones reversibles; no escalar nada paga los errores de las irreversibles. La política intermedia ahorra una cuarta parte del costo de la peor.',
                        note_kind='teal', foot=SINT)

FIGURES = {
    "se-445-redes-y-siembra.svg": se445_redes_y_siembra,
    "se-445-cuello-de-aprobacion.svg": se445_cuello_de_aprobacion,
    "se-445-consulta-previa.svg": se445_consulta_previa,
    "se-446-factor-de-camion.svg": se446_factor_de_camion,
    "se-446-fronteras-y-relevos.svg": se446_fronteras_y_relevos,
    "se-446-carga-de-guardia.svg": se446_carga_de_guardia,
    "se-447-estimar-en-grupo.svg": se447_estimar_en_grupo,
    "se-447-campos-que-se-pierden.svg": se447_campos_que_se_pierden,
    "se-447-conflicto-con-ruido.svg": se447_conflicto_con_ruido,
    "se-448-tareas-que-estiran.svg": se448_tareas_que_estiran,
    "se-448-cuando-llega-el-aviso.svg": se448_cuando_llega_el_aviso,
    "se-448-ruido-de-evaluacion.svg": se448_ruido_de_evaluacion,
    "se-449-suma-de-medianas.svg": se449_suma_de_medianas,
    "se-449-pronostico-por-flujo.svg": se449_pronostico_por_flujo,
    "se-449-ciclo-y-carga.svg": se449_ciclo_y_carga,
    "se-450-matriz-y-valor-esperado.svg": se450_matriz_y_valor_esperado,
    "se-450-valor-de-la-informacion.svg": se450_valor_de_la_informacion,
    "se-450-escalar-lo-que-corresponde.svg": se450_escalar_lo_que_corresponde,
}
