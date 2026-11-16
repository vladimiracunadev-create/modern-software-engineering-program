"""Figuras de SE-445 a SE-450: datos sintéticos con semilla fija y ejecuciones de código propio sobre datos sintéticos (CPython 3.12.9 en Windows 11, repetido con 3.12.3 en Ubuntu bajo WSL2)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."


# ---------------------------------------------------------------- SE-445
def se445_redes_y_siembra() -> Fig:
    return tab('Qué siembra produce adopción',
               'Tabla con 2 000 redes sintéticas de 30 personas y cuatro siembras de una práctica: con solo un anuncio general la adopción es nula en el 100 por ciento de las redes, con dos personas al azar la mediana es 93,3 por ciento y 63,2 por ciento de las redes pasan del 80 por ciento, con dos muy conectadas 96,7 y 95,7 por ciento, y con dos poco conectadas 6,7 y 11,4 por ciento.',
               ['Siembra', 'Adopción final (mediana)', 'Redes con 80 % o más', 'Redes que no pasan del 10 %'], [['Solo un anuncio general', '0,0 %', '0,0 %', '100,0 %'], ['2 personas al azar', '93,3 %', '63,2 %', '14,4 %'], ['2 personas muy conectadas', '96,7 %', '95,7 %', '0,2 %'], ['2 personas poco conectadas', '6,7 %', '11,4 %', '72,7 %']], [222, 216, 185, 240], row_h=44, size=13,
               note='Cada fila es una forma de empezar; la columna central dice cuánto del equipo termina usando la práctica y las demás cuántas redes llegan lejos o se quedan inmóviles. La diferencia entre las dos últimas filas es la lección: son dos personas en ambos casos, y el resultado va de casi todo a casi nada según dónde están.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-445
def se445_cuello_de_aprobacion() -> Fig:
    return tab('Cuánto espera una decisión',
               'Tabla con la espera de una decisión según cuántas aprueba una sola persona: con 5 por día la utilización es 87,5 por ciento y la espera media 9,4 horas con percentil 90 de 22,8, con 2 por día 35 por ciento, 0,8 horas y 2,7, y con 1 por día 17,5 por ciento, 0,3 horas y 0,9.',
               ['Quién decide', 'Utilización', 'Espera media', 'Espera p90'], [['Una persona aprueba todo (5 por día)', '87,5 %', '9,4 h', '22,8 h'], ['Aprueba el 40 % (2 por día)', '35,0 %', '0,8 h', '2,7 h'], ['Criterios delegados (1 por día)', '17,5 %', '0,3 h', '0,9 h']], [369, 144, 153, 134], row_h=44, size=13,
               note='La utilización pasa de 17,5 % a 87,5 % y la espera media se multiplica por más de treinta, no por cinco: la espera no es proporcional a la carga. El percentil 90 muestra que una decisión de cada diez espera casi tres jornadas.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-445
def se445_consulta_previa() -> Fig:
    return tab('Cuántas decisiones se revierten',
               'Tabla con 6 000 decisiones sintéticas: sin consulta previa por escrito se revierte el 29,9 por ciento y cuesta 4,49 días de trabajo por decisión, con 2 personas 21,7 por ciento y 4,75 días, con 4 personas 13,9 por ciento y 4,09 días, y con 8 personas 5,9 por ciento y 3,89 días.',
               ['Personas que leen antes', 'Decisiones revertidas', 'Días de trabajo por decisión (consulta más reversión)'], [['0', '29,9 %', '4,49'], ['2', '21,7 %', '4,75'], ['4', '13,9 %', '4,09'], ['8', '5,9 %', '3,89']], [228, 211, 361], row_h=44, size=13,
               note='Las reversiones bajan con cada persona que lee, pero el costo total no baja de inmediato: consultar a dos personas cuesta más días que no consultar a nadie, porque el beneficio no compensa aún el costo fijo de preparar y esperar. El balance mejora con cuatro y con ocho.',
               note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-446
def se446_factor_de_camion() -> Fig:
    return tab('Cuántas personas deben irse',
               'Tabla con 200 repositorios sintéticos de 300 archivos y 8 personas: con un autor por archivo y reparto concentrado el factor de camión mediano es 2 y la salida de la persona más cargada deja sin conocedor al 37 por ciento de los archivos, con reparto uniforme 4 y 15,4 por ciento, con dos conocedores por archivo 5,5 y 0 por ciento y con dos conocedores y rotación 6 y 0 por ciento.',
               ['Reparto del conocimiento', 'Factor de camión (mediana)', 'Archivos sin conocedor al irse la persona más cargada'], [['Un autor por archivo, reparto concentrado', '2', '37,0 %'], ['Un autor por archivo, reparto uniforme', '4', '15,4 %'], ['Dos conocedores por archivo', '5,5', '0,0 %'], ['Dos conocedores y rotación', '6', '0,0 %']], [330, 232, 330], row_h=44, size=13,
               note='Cada fila es una política de reparto; el factor dice cuántas personas habría que perder para dejar sin conocedor a la mitad del código, y la última columna cuánto se pierde si se va solo la persona que más sabe. La diferencia entre un autor concentrado y dos conocedores por archivo es lo que compra la revisión por un segundo conocedor.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-446
def se446_fronteras_y_relevos() -> Fig:
    return tab('Cuántos equipos cruza un cambio',
               'Tabla con 5 000 cambios sintéticos sobre cuatro dominios y tres capas: con equipos por capa un cambio cruza 2,31 equipos de media, el 81 por ciento requiere relevo y el plazo es de 5,9 días, y con equipos por dominio cruza 1,21, el 21,1 por ciento requiere relevo y el plazo es de 2,6 días.',
               ['Organización', 'Equipos por cambio', 'Cambios que requieren relevo', 'Plazo estimado'], [['Equipos por capa', '2,31', '81,0 %', '5,9 días'], ['Equipos por dominio', '1,21', '21,1 %', '2,6 días']], [188, 187, 272, 153], row_h=44, size=13,
               note='Cada fila es una forma de cortar el mismo trabajo; el plazo baja a menos de la mitad porque los relevos desaparecen, no porque se trabaje más rápido.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-446
def se446_carga_de_guardia() -> Fig:
    return tab('Cuánta guardia recibe cada persona',
               'Tabla con 3 000 años simulados de una guardia semanal con 1,5 avisos por semana fuera de horario: con 3 personas cada una está 18 semanas al año de guardia y recibe 27 avisos con 3,45 semanas de tres o más, con 4 personas 13 semanas, 19,5 avisos y 2,48 semanas, con 6 personas 9, 13,5 y 1,73, y con 8 personas 7, 10,5 y 1,33.',
               ['Tamaño de la rotación', 'Semanas de guardia al año', 'Avisos fuera de horario por persona y año', 'Semanas con 3 o más avisos por persona y año'], [['3 personas', '18', '27,0', '3,45'], ['4 personas', '13', '19,5', '2,48'], ['6 personas', '9', '13,5', '1,73'], ['8 personas', '7', '10,5', '1,33']], [174, 202, 298, 298], row_h=44, size=13,
               note='El número de avisos por persona baja en proporción al tamaño de la rotación, pero las semanas malas (tres o más avisos) bajan más despacio: aunque la media baje, siempre habrá semanas duras.',
               note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-447
def se447_estimar_en_grupo() -> Fig:
    return tab('Cuánto distorsiona hablar en orden',
               'Tabla con 5 000 ensayos sintéticos de una estimación de grupo de siete personas sobre una cantidad real de 100 días: si escriben solas y luego se muestran el error mediano es 8,4 por ciento y el 22,9 por ciento supera el 15, si hablan en orden sin sesgo 9,8 y 30,7, y si abre una persona sénior con un valor 30 por ciento mayor 16 y 52,8.',
               ['Cómo se recogen las estimaciones', 'Error mediano del promedio', 'Ensayos con error mayor al 15 %'], [['Escriben solas y luego se muestran', '8,4 %', '22,9 %'], ['Se habla en orden, sin sesgo del primero', '9,8 %', '30,7 %'], ['Se habla en orden y la persona sénior (+30 %) abre', '16,0 %', '52,8 %']], [330, 232, 271], row_h=44, size=13,
               note='La primera fila es la referencia: el promedio de estimaciones independientes. Hablar en orden ya la empeora, y un sesgo del primero la duplica; más de la mitad de las sesiones de la última fila yerra por más del 15 %.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-447
def se447_campos_que_se_pierden() -> Fig:
    return tab('Cuántos campos sobreviven a los relevos',
               'Tabla con 6 000 mensajes sintéticos de decisión de cinco campos tras varios relevos: oral llega completo en 26,2 por ciento tras un relevo, 6,7 tras dos y 0,5 tras cuatro y conserva el motivo en 17,6, el correo libre 49,6, 24,7 y 5,5 con motivo en 40,8, y la plantilla con acuse 88, 76,7 y 58,3 con motivo en 84,6.',
               ['Formato', 'Mensaje completo tras 1 relevo', 'Tras 2', 'Tras 4', 'Conserva el motivo tras 4'], [['Oral', '26,2 %', '6,7 %', '0,5 %', '17,6 %'], ['Correo libre', '49,6 %', '24,7 %', '5,5 %', '40,8 %'], ['Plantilla con acuse', '88,0 %', '76,7 %', '58,3 %', '84,6 %']], [171, 263, 90, 90, 224], row_h=44, size=13,
               note='Incluso con la plantilla, tras cuatro relevos solo el 58,3 % del mensaje llega completo; el oral prácticamente no sobrevive. El motivo, que explica cómo adaptar la decisión, cae más rápido que el resto en los formatos libres.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-447
def se447_conflicto_con_ruido() -> Fig:
    return tab('Qué estrategia aguanta un malentendido',
               'Tabla con partidas sintéticas de 200 rondas con 5 por ciento de malentendidos: contra sí misma el ojo por ojo obtiene 2,29 puntos por ronda, el generoso 2,85, el que siempre coopera 2,95 y el que siempre ataca 1,15, y en promedio contra las cuatro estrategias obtienen 2,31, 2,34, 2,21 y 2,39.',
               ['Estrategia', 'Pago por ronda contra sí misma', 'Pago promedio contra las cuatro estrategias'], [['Ojo por ojo', '2,29', '2,31'], ['Ojo por ojo generoso', '2,85', '2,34'], ['Siempre coopera', '2,95', '2,21'], ['Siempre ataca', '1,15', '2,39']], [185, 273, 342], row_h=44, size=13,
               note='Contra una igual, un malentendido hace caer el ojo por ojo estricto de 3 a 2,29 porque las represalias se alternan; la versión generosa lo recupera hasta 2,85. La segunda columna muestra el límite: contra una mezcla que incluye a quien siempre ataca, esa estrategia obtiene el promedio más alto y quien siempre coopera, el más bajo.',
               note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-448
def se448_tareas_que_estiran() -> Fig:
    return tab('Qué tareas hacen crecer',
               'Tabla con 1 000 personas simuladas durante 52 semanas con nivel inicial 3: con tareas fáciles el nivel final mediano es 3,07 y hay 0,3 semanas de fracaso, con tareas calibradas 8,87 y 6,2, con tareas muy difíciles 3,04 y 37,9, y con dificultad al azar 4,8 y 14.',
               ['Tareas asignadas', 'Nivel final (mediana)', 'Semanas con fracaso al año'], [['Fáciles (nivel − 2)', '3,07', '0,3'], ['Calibradas (nivel + 1)', '8,87', '6,2'], ['Muy difíciles (nivel + 4)', '3,04', '37,9'], ['Dificultad al azar', '4,80', '14,0']], [269, 241, 290], row_h=44, size=13,
               note='Las tareas fáciles y las muy difíciles dejan casi igual el nivel final, por razones opuestas: una no enseña y la otra fracasa casi todas las semanas. Las calibradas aceptan semanas de fracaso (6 de 52) como costo del aprendizaje.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-448
def se448_cuando_llega_el_aviso() -> Fig:
    return tab('Cuánto cuesta esperar la retroalimentación',
               'Tabla con 4 000 personas simuladas durante 12 semanas con un hábito erróneo en el 30 por ciento de cinco cambios semanales: con retroalimentación en el mismo cambio se repite el error 3,4 veces, a los 2 días 4,3, en la revisión semanal 4,7 y en la evaluación trimestral a los 60 días 14,3.',
               ['Cuándo llega la retroalimentación', 'Errores repetidos en 12 semanas'], [['En el mismo cambio', '3,4'], ['A los 2 días', '4,3'], ['En la revisión semanal', '4,7'], ['En la evaluación trimestral (60 días)', '14,3']], [423, 377], row_h=44, size=13,
               note='Pasar de la retroalimentación inmediata a la semanal añade poco (de 3,4 a 4,7); pasar a la trimestral la cuadruplica. El costo no es lineal en el retraso: se pierde el aprendizaje de varias semanas de trabajo.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-448
def se448_ruido_de_evaluacion() -> Fig:
    return tab('Cuánto ruido hay en una evaluación',
               'Tabla con 300 grupos simulados de 200 personas evaluadas por una o tres evaluadoras: una evaluadora sin rúbrica alcanza una correlación de 0,73 con el desempeño verdadero y promueve al 58,7 por ciento del 20 por ciento mejor, tres evaluadoras sin rúbrica 0,89 y 74,1, y tres con rúbrica calibrada 0,97 y 85,9.',
               ['Esquema de evaluación', 'Correlación con el desempeño', 'Del 20 % mejor, promovidas'], [['Una evaluadora, sin rúbrica', '0,73', '58,7 %'], ['Tres evaluadoras, sin rúbrica', '0,89', '74,1 %'], ['Tres evaluadoras con rúbrica calibrada', '0,97', '85,9 %']], [315, 250, 235], row_h=44, size=13,
               note='Con una sola evaluadora y sin rúbrica, cuatro de cada diez personas que merecían promoción no la reciben aunque el desempeño exista y se mide con ruido. Añadir evaluadoras ayuda y la rúbrica calibrada ayuda más.',
               note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-449
def se449_suma_de_medianas() -> Fig:
    return tab('Por qué la suma de medianas no se cumple',
               'Tabla con 20 000 proyectos simulados de doce tareas con mediana de cinco días y suma de medianas de 60 días: con tareas independientes la probabilidad de terminar en 60 días es 19,3 por ciento y los percentiles 50, 85 y 95 son 70,5, 85,7 y 96,4 días, y con un factor común de dificultad 31,9 por ciento y 68,9, 93,4 y 111,7.',
               ['Supuesto', 'Probabilidad de terminar en 60 días', 'p50', 'p85', 'p95'], [['Tareas independientes', '19,3 %', '70,5', '85,7', '96,4'], ['Con un factor común de dificultad', '31,9 %', '68,9', '93,4', '111,7']], [274, 302, 90, 90, 90], row_h=44, size=13,
               note='La suma de medianas se cumple una de cada cinco veces con tareas independientes y una de cada tres con un factor común. El factor común no desplaza la mediana, ensancha la cola: el percentil 95 pasa de 96 a 112 días.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-449
def se449_pronostico_por_flujo() -> Fig:
    return tab('Cuántas semanas necesita un backlog de 60 elementos',
               'Tabla con el pronóstico de 60 elementos pendientes con un historial de 20 semanas y entrega media de 4,95: la media da 13 semanas con 70,6 por ciento de probabilidad, la simulación da percentiles 50, 85 y 95 de 13, 14 y 16 semanas, y el percentil 85 calculado con 200 historiales de 6, 12, 24 y 48 semanas tiene mediana 15 y rangos de 12 a 21, 13 a 20, 13 a 18 y 14 a 17.',
               ['Cálculo', 'Resultado'], [['Fecha con la media del historial (60 / 4,95)', '13 semanas, con 70,6 % de probabilidad de cumplirla'], ['Pronóstico por simulación, historial de 20 semanas', 'p50 13, p85 14 y p95 16 semanas'], ['p85 con 6 semanas de historial (200 repeticiones)', 'mediana 15; entre 12 y 21 semanas (p10–p90)'], ['p85 con 12 semanas de historial', 'mediana 15; entre 13 y 20'], ['p85 con 24 semanas de historial', 'mediana 15; entre 13 y 18'], ['p85 con 48 semanas de historial', 'mediana 15; entre 14 y 17']], [400, 400], row_h=44, size=13,
               note='La fecha de la media parece segura y se cumple el 70,6 % de las veces; el percentil 85 añade una semana. La parte inferior muestra el límite del método: con seis semanas de historial, el mismo pronóstico oscila entre doce y veintiuna semanas según qué seis semanas se tuvieron.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-449
def se449_ciclo_y_carga() -> Fig:
    return tab('Qué ocurre cuando el equipo está lleno',
               'Tabla con 60 000 elementos simulados por escenario en una cola de un servidor: con carga del 50 por ciento el ciclo medio es 2 unidades de trabajo y el percentil 90 es 4,6, con 70 por ciento 3,3 y 7,7, con 85 por ciento 6,7 y 15,1, y con 95 por ciento 18,2 y 42, frente a un valor teórico de 20 con 95 por ciento.',
               ['Carga del equipo', 'Ciclo medio (unidades de trabajo)', 'Valor teórico 1/(1 − carga)', 'Ciclo p90'], [['50 %', '2,0', '2,0', '4,6'], ['70 %', '3,3', '3,3', '7,7'], ['85 %', '6,7', '6,7', '15,1'], ['95 %', '18,2', '20,0', '42,0']], [158, 294, 246, 102], row_h=44, size=13,
               note='Pasar de 70 % a 95 % de carga multiplica el ciclo por más de cinco; el percentil 90 de un equipo al 95 % es de 42 veces el trabajo del elemento. La simulación coincide con la fórmula teórica salvo al 95 %, donde 60 000 elementos no bastan para promediar la cola.',
               note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-450
def se450_matriz_y_valor_esperado() -> Fig:
    return tab('Qué fracción del riesgo cubren los cinco primeros',
               'Tabla con 400 carteras sintéticas de 30 riesgos de los que se eligen cinco para mitigar: ordenar por valor esperado cubre el 72,2 por ciento de la pérdida esperada, una matriz de cinco por cinco cubre el 65,8 por ciento y deja fuera el mayor riesgo en el 8,5 por ciento de las carteras, y elegir al azar cubre el 16,6 por ciento.',
               ['Criterio para elegir los cinco', 'Pérdida esperada cubierta', 'Deja fuera el mayor riesgo'], [['Valor esperado', '72,2 %', '0 % por definición'], ['Matriz 5×5', '65,8 %', '8,5 % de las carteras'], ['Azar', '16,6 %', '—']], [293, 249, 258], row_h=44, size=13,
               note='La matriz es mucho mejor que el azar y algo peor que el valor esperado: pierde 6,4 puntos de cobertura. En una de cada doce carteras deja fuera el riesgo más caro.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-450
def se450_valor_de_la_informacion() -> Fig:
    return tab('Cuánto vale saber antes de decidir',
               'Tabla con una inversión de valor neto incierto con desviación 100 y un experimento con ruido de 40: con valor esperado a priori de menos 20 la información perfecta vale 30,6 y el experimento 27,8, con valor esperado cero 39,8 y 36,9, y con más 20 vale 30,6 y 27,7 sobre una base de 20.',
               ['Valor esperado a priori', 'Sin información', 'VEIP simulado (analítico)', 'VEII de un experimento ruidoso'], [['−20', '0,0', '30,6 (30,7)', '27,8'], ['0', '0,0', '39,8 (39,9)', '36,9'], ['+20', '20,0', '30,6 (30,7)', '27,7']], [209, 147, 224, 263], row_h=44, size=13,
               note='La información vale más cuando la decisión está en el límite (valor esperado cero: 39,8) y menos cuando se inclina hacia un lado. El experimento ruidoso captura entre el 90 y el 93 % de ese valor, así que cualquier experimento que cueste menos de 27 es rentable en el caso central, y uno que cueste 40 nunca lo es.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-450
def se450_escalar_lo_que_corresponde() -> Fig:
    return tab('Cuánto cuesta decidir a qué nivel',
               'Tabla con 200 decisiones por trimestre durante 3 000 trimestres con 30 por ciento irreversibles: escalar todo cuesta 407 de mediana y 487 en el percentil 90, escalar solo lo irreversible 301,5 y 382, y no escalar nada 369,5 y 463,5.',
               ['Política de escalamiento', 'Costo trimestral (mediana)', 'Costo p90'], [['Todo se escala', '407,0', '487,0'], ['Solo se escala lo irreversible', '301,5', '382,0'], ['Nada se escala', '369,5', '463,5']], [345, 318, 137], row_h=44, size=13,
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
