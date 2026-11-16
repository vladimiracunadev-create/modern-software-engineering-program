"""Figures for SE-475 to SE-480 (SPEC, agents and agentic life cycle: synthetic data with fixed seeds, plus runs of real CPython/SQLite code on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."

# ---------------------------------------------------------------- SE-475
def se475_validar_cada_mensaje() -> Fig:
    rows = [['Válido', '60', '60', '60', '60'], ['JSON roto', '5', '0', '0', '0'], ['Sin identificador', '5', '0', '0', '0'], ['Versión antigua', '5', '5', '0', '0'], ['Método distinto en cabecera y cuerpo', '5', '5', '0', '0'], ['Nombre distinto en cabecera y cuerpo', '5', '5', '5', '0'], ['Herramienta inexistente', '5', '0', '0', '0'], ['Argumento de tipo equivocado', '5', '5', '5', '0'], ['Recurso fuera de alcance', '5', '5', '5', '0'], ['Pasarela que autoriza por cabecera: herramienta no permitida ejecutada', '5', '5', '5', '0']]
    return tab('Cien mensajes y tres niveles de comprobación: cuántos de cada clase se ejecutan',
               'Tabla con 100 mensajes y tres niveles de comprobación: con solo la forma JSON-RPC se ejecutan 25 de los 40 malformados, con versión y método de la cabecera 15 y con nombre, argumentos y alcance ninguno, mientras los 60 válidos pasan siempre; los 5 mensajes con cabecera de una herramienta permitida y cuerpo de borrar historial se ejecutan en los dos primeros niveles y ninguno en el tercero.',
               ['Clase de mensaje', 'Cuántos', 'Solo forma', '+ versión y método', '+ nombre, argumentos y alcance'], rows, [330, 80, 110, 160, 250], row_h=48, size=12,
               note='Los 60 válidos pasan siempre. La última fila es el desajuste entre quien autoriza por cabecera y quien ejecuta el cuerpo. El manejador es una imitación escrita por el autor, no una implementación conforme.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-475
def se475_descripciones_y_huellas() -> Fig:
    rows = [['Buscador de patrones sobre el catálogo', 'marca 6: halla 3 de 4 con instrucciones y marca 3 legítimas; la que no usa palabras de mando pasa'], ['Huella fijada tras 6 actualizaciones', 'alerta en 6 de 6 (4 benignas y 2 maliciosas)'], ['Buscador sobre las 2 actualizaciones maliciosas', 'marca 1 de 2']]
    return tab('Catálogo de 20 herramientas con 4 descripciones con instrucciones: buscador de patrones y huellas fijadas',
               'Tabla con un catálogo de 20 herramientas, 4 con instrucciones escondidas: un buscador de patrones marca 6, halla 3 de las 4 y marca 3 legítimas, y la que no usa palabras de mando pasa; una huella fijada alerta en 6 de 6 actualizaciones, 4 benignas y 2 maliciosas; el buscador marca solo 1 de las 2 actualizaciones maliciosas.',
               ['Comprobación', 'Resultado'], rows, [380, 540], row_h=58, size=13,
               note='La huella no deja pasar ningún cambio y a cambio obliga a revisar también los benignos; el buscador prioriza qué leer primero y falla de las dos maneras. Las descripciones y los patrones los escribió el autor.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-475
def se475_cache_y_obsolescencia() -> Fig:
    rows = [['0', '2 853', '0 de 19 973 (0,00 %)', '—'], ['30 000', '1 436', '8 de 19 973 (0,04 %)', 'menos de 1 min'], ['300 000', '262', '142 de 19 973 (0,71 %)', '5 min'], ['3 600 000', '24', '1 729 de 19 973 (8,66 %)', '58 min'], ['86 400 000', '1', '15 780 de 19 973 (79,01 %)', '1 405 min (23 h)']]
    return tab('Caché de listados durante siete días con 120 consultas por hora y un cambio de catálogo cada seis horas de media',
               'Tabla con una caché de listados de herramientas durante siete días con 120 consultas por hora y un cambio de catálogo cada seis horas de media: sin caché 2853 lecturas al día y ninguna respuesta vieja; con 30 segundos 1436 lecturas y 0,04 por ciento viejas; con 5 minutos 262 y 0,71; con una hora 24 y 8,66; con un día 1 lectura y 79,01 por ciento de respuestas viejas, hasta 1405 minutos de antigüedad.',
               ['ttlMs', 'Lecturas por día', 'Respuestas con catálogo viejo', 'Antigüedad máxima de un cambio no visto'], rows, [150, 150, 330, 290], row_h=44, size=13,
               note='La elección del tiempo de vida es de riesgo, no de comodidad: una retirada urgente de una herramienta tarda en surtir efecto lo que dure la caché. Los cambios de catálogo son un proceso de Poisson supuesto.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-476
def se476_contexto_con_subagentes() -> Fig:
    rows = [['Agente único', '4,16 M', '100 %', '165 000'], ['Subagentes, lectura mínima (1×)', '0,90 M', '22 %', '17 000 (orquestador)'], ['Subagentes, 2×', '1,46 M', '35 %', '17 000'], ['Subagentes, 3×', '2,02 M', '49 %', '17 000'], ['Subagentes, 4×', '2,58 M', '62 %', '17 000'], ['Subagentes, 6×', '3,70 M', '89 %', '17 000']]
    return tab('Contexto de entrada procesado por un agente único y por ocho subagentes según la lectura redundante',
               'Tabla con el contexto de entrada procesado por un agente único y por ocho subagentes según la lectura redundante: el agente único procesa 4,16 millones de tokens y termina con 165000; con subagentes el consumo es 22 por ciento con lectura mínima, 35 con el doble, 49 con el triple, 62 con el cuádruple y 89 con seis veces, y el contexto final del orquestador es siempre 17000 tokens.',
               ['Caso', 'Tokens procesados', 'Frente al agente único', 'Contexto final'], rows, [380, 190, 190, 190], row_h=40, size=13,
               note='El modelo cuenta solo tokens de entrada por turno: no incluye salida, caché ni coordinación, y por eso no contradice que en la práctica los sistemas multiagente consuman más. Muestra la forma cuadrática del agente único.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-476
def se476_hechos_que_sobreviven() -> Fig:
    rows = [['99 %', '95,1 %', '95,1 %'], ['95 %', '77,4 %', '77,3 %'], ['90 %', '59,0 %', '59,0 %'], ['80 %', '32,8 %', '33,0 %']]
    return tab('Probabilidad de que cinco hechos necesarios lleguen al orquestador según la retención de cada resumen',
               'Tabla con la probabilidad de que cinco hechos necesarios lleguen al orquestador según la fracción que conserva cada resumen: con 99 por ciento llegan el 95,1 por ciento de las veces, con 95 el 77,4, con 90 el 59,0 y con 80 el 32,8, y la simulación de 20000 corridas coincide con 95,1, 77,3, 59,0 y 33,0.',
               ['Retención por hecho', 'Llegan los 5 (cálculo)', 'Simulación (20 000 corridas)'], rows, [300, 300, 320], row_h=44, size=13,
               note='La probabilidad cae como la retención elevada al número de hechos. Se supone independencia entre hechos; en la práctica se pierden primero los números y los matices.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-476
def se476_colisiones_de_edicion() -> Fig:
    rows = [['2', '36,5 %', '0,0 %', '0,7 %'], ['3', '75,3 %', '0,0 %', '2,0 %'], ['4', '94,4 %', '0,0 %', '3,6 %'], ['6', '100,0 %', '0,0 %', '8,9 %'], ['8', '100,0 %', '0,0 %', '16,0 %']]
    return tab('Probabilidad de conflicto de edición con 60 archivos y 5 por agente según el reparto',
               'Tabla con la probabilidad de conflicto de edición con 60 archivos y 5 por agente: con reparto al azar 36,5 por ciento con dos agentes, 75,3 con tres, 94,4 con cuatro y 100 con seis y ocho; con propiedad por carpeta 0,0 en todos los casos; con propiedad y 20 por ciento de tareas que tocan un archivo común 0,7, 2,0, 3,6, 8,9 y 16,0 por ciento.',
               ['Agentes', 'Reparto al azar', 'Propiedad por carpeta', 'Propiedad y 20 % con archivo común'], rows, [170, 230, 250, 270], row_h=44, size=13,
               note='Los archivos comunes reintroducen el conflicto aunque cada agente respete su zona. El trabajo real no elige archivos al azar y la propiedad rara vez se respeta al 100 %.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-476
def se476_protocolos_de_escritura() -> Fig:
    rows = [['Escritura ciega', '600', '0', '0'], ['Versión optimista', '0', '1 200', '0'], ['Arrendamiento con caducidad', '0', '0', '980']]
    return tab('Tres protocolos de escritura de cuatro agentes sobre una fila compartida de SQLite en 200 rondas',
               'Tabla con tres protocolos de escritura de cuatro agentes sobre una fila compartida de SQLite en 200 rondas: la escritura ciega pierde 600 de 800 contribuciones sin reintentos ni espera; la versión optimista no pierde ninguna y hace 1200 reintentos; el arrendamiento con caducidad no pierde ninguna, no reintenta y espera 980 ticks.',
               ['Protocolo', 'Contribuciones perdidas de 800', 'Reintentos', 'Ticks de espera'], rows, [330, 260, 150, 180], row_h=44, size=13,
               note='La pérdida de la escritura ciega es estructural: sobrevive una de cuatro contribuciones. Los cuatro agentes leen a la vez en cada ronda, el caso peor para la versión optimista; SQLite en memoria no reproduce la concurrencia real.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-477
def se477_politicas_de_aprobacion() -> Fig:
    rows = [['Preguntar en cada acción', '200,0', '3,02', '93,5 %'], ['Preguntar solo las de riesgo (clasificador del 90 % y 8 %)', '22,5', '1,30', '73,2 %'], ['Aprobar el plan y preguntar las desviaciones', '11,1', '1,18', '69,5 %'], ['Solo lo irreversible, con pausa obligatoria', '8,0', '0,54', '41,5 %']]
    return tab('Cuatro políticas de aprobación en 5 000 sesiones de 200 acciones con un 4 % irreversibles',
               'Tabla con cuatro políticas de aprobación en 5000 sesiones de 200 acciones con 4 por ciento irreversibles: preguntar en cada acción genera 200 avisos y deja ejecutar 3,02 irreversibles por sesión, con 93,5 por ciento de sesiones afectadas; preguntar por riesgo 22,5 avisos y 1,30; aprobar un plan 11,1 y 1,18; preguntar solo lo irreversible con pausa 8,0 y 0,54, con 41,5 por ciento de sesiones.',
               ['Política', 'Avisos por sesión', 'Irreversibles ejecutadas por sesión', 'Sesiones con alguna'], rows, [400, 140, 230, 150], row_h=48, size=13,
               note='Preguntar por todo agota la atención en lo rutinario. La última política supone saber qué es irreversible. La función de atención, el 4 % y el clasificador son supuestos del autor: no se observó a ninguna persona.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-477
def se477_deshacer_con_diario() -> Fig:
    rows = [['Acciones ejecutadas', '60 (55 sobre archivos y 5 correos simulados)'], ['El directorio cambió tras las 60 acciones', 'sí'], ['Estado tras deshacer idéntico al inicial', 'sí'], ['Tamaño del diario', '2 216 bytes (85 % del espacio)'], ['Acciones que el diario no puede deshacer', '5 de 60 (los correos)']]
    return tab('Sesenta acciones de un generador con semilla sobre 40 archivos y su deshacer con un diario por acción',
               'Tabla con 60 acciones de un generador con semilla sobre 40 archivos en un directorio temporal: tras ejecutarlas el directorio cambió; al deshacer en orden inverso con un diario por acción el estado coincide con el inicial; el diario ocupa 2216 bytes, el 85 por ciento del espacio de trabajo; las 5 acciones de enviar correo no se pueden deshacer con el diario.',
               ['Medida', 'Resultado'], rows, [470, 400], row_h=44, size=13,
               note='El diario restaura el estado de los archivos y no lo que sale del sistema. Son archivos pequeños, sin enlaces simbólicos, permisos especiales ni caídas a mitad de acción.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-477
def se477_compensar_un_flujo() -> Fig:
    rows = [['Sin compensación', '65,7 %', '65,7 %', '34,3 %', '0,0 %'], ['Compensar sin reintentar', '65,4 %', '95,5 %', '4,5 %', '0,0 %'], ['Compensar con 2 reintentos', '65,4 %', '100,0 %', '0,1 %', '0,0 %'], ['Con 2 reintentos y el paso 3 irreversible', '65,6 %', '87,8 %', '0,0 %', '12,1 %']]
    return tab('Flujo de cinco pasos con 8 % de fallo por intento: consistencia según la estrategia de compensación (20 000 ejecuciones)',
               'Tabla con un flujo de cinco pasos con 8 por ciento de fallo por intento en 20000 ejecuciones: sin compensación el 34,3 por ciento queda a medias; compensar sin reintentar deja 95,5 por ciento consistente y 4,5 a medias; con dos reintentos 100,0 y 0,1; con el paso 3 irreversible 87,8 por ciento consistente y 12,1 por ciento con efecto residual.',
               ['Estrategia', 'Completas', 'Consistentes', 'A medias', 'Con efecto residual'], rows, [400, 120, 140, 120, 140], row_h=44, size=13,
               note='Un paso irreversible deja un efecto que ninguna compensación elimina; conviene ponerlo al final. El 8 % de fallo y la independencia entre intentos son supuestos del autor.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-478
def se478_filtros_de_instrucciones() -> Fig:
    rows = [['Frase fija sobre el texto sin tratar', '8 de 8', '0 de 8', '0 de 8', '0 de 8', '0 de 8', '0 de 160'], ['+ normalizar el texto y decodificar', '8 de 8', '0 de 8', '8 de 8', '8 de 8', '0 de 8', '0 de 160'], ['+ unir los campos antes de buscar', '8 de 8', '0 de 8', '8 de 8', '8 de 8', '8 de 8', '0 de 160'], ['+ patrón amplio (paráfrasis)', '8 de 8', '8 de 8', '8 de 8', '8 de 8', '8 de 8', '19 de 160']]
    return tab('Cuatro filtros de instrucciones inyectadas sobre 200 documentos: 40 con una orden de prueba en cinco formas y 160 inocuos',
               'Tabla con cuatro filtros de instrucciones inyectadas sobre 200 documentos, 40 con una orden de prueba en cinco formas y 160 inocuos: la frase fija detecta 8 de 8 directas y ninguna de las otras formas; normalizar y decodificar suma 8 de ancho cero y 8 codificadas; unir los campos suma 8 repartidas; el patrón amplio detecta las 40 y marca 19 de los 160 inocuos.',
               ['Filtro', 'Directa', 'Parafraseada', 'Ancho cero', 'Codificada', 'Repartida', 'Inocuos marcados'], rows, [330, 90, 130, 110, 110, 100, 130], row_h=48, size=12,
               note='Cada forma que se cierra añade ingeniería o falsas alarmas: el patrón amplio marca 19 de 160 inocuos. El 100 % es consecuencia de un conjunto de pruebas escrito conociendo las cinco formas; no se midió ningún modelo.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-478
def se478_tres_capacidades() -> Fig:
    rows = [['Sin restricción', '12', '0', '0', '3'], ['Quitar la comunicación hacia fuera', '6', '6', '0', '0'], ['Quitar el contenido no confiable', '4', '8', '0', '0'], ['Quitar los datos privados', '2', '10', '0', '0'], ['Marcar lo leído como no confiable y exigir aprobación para salir', '9', '0', '3', '0']]
    return tab('Doce tareas típicas de un agente y cinco políticas sobre datos privados, contenido no confiable y comunicación hacia fuera',
               'Tabla con 12 tareas típicas de un agente y 5 políticas sobre las tres capacidades de datos privados, contenido no confiable y comunicación hacia fuera: sin restricción 12 tareas pasan sin ayuda y 3 reúnen las tres sin aprobación; quitar la comunicación hacia fuera deja 6 y bloquea 6; quitar contenido no confiable deja 4 y bloquea 8; quitar datos privados deja 2 y bloquea 10; marcar lo leído como no confiable y exigir aprobación para salir deja 9 sin ayuda y 3 con aprobación, sin ninguna bloqueada.',
               ['Política', 'Sin ayuda', 'Bloqueadas', 'Con aprobación', 'Con las tres sin aprobación'], rows, [420, 110, 120, 140, 130], row_h=48, size=12,
               note='En 5 000 configuraciones de 6 herramientas de un catálogo de 15, el 73,5 % reúne las tres capacidades. Las tareas y sus capacidades son una clasificación del autor tratada como todo o nada.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-478
def se478_registro_que_se_nota() -> Fig:
    rows = [['Editar un evento', '0 %', '100 %', '100 %'], ['Borrar un evento', '0 %', '100 %', '100 %'], ['Intercambiar dos eventos', '0 %', '100 %', '100 %'], ['Cortar los últimos 20 eventos', '0 %', '0 %', '100 %'], ['Reescribir desde un punto y recalcular la cadena', '0 %', '0 %', '100 %']]
    return tab('Cinco manipulaciones de un registro de auditoría de 500 eventos: fracción detectada por esquema (200 ensayos cada una)',
               'Tabla con cinco manipulaciones de un registro de auditoría de 500 eventos en 200 ensayos cada una: un registro simple detecta 0 por ciento en todas; una cadena de huellas detecta 100 por ciento de editar, borrar e intercambiar eventos y 0 por ciento de cortar los últimos 20 o reescribir y recalcular; con la huella final guardada aparte se detectan las cinco al 100 por ciento.',
               ['Manipulación', 'Registro simple', 'Cadena de huellas', 'Cadena y huella final aparte'], rows, [440, 150, 170, 170], row_h=44, size=13,
               note='La integridad de un registro es una propiedad de quién controla la referencia: quien puede reescribir la cadena entera produce una cadena válida. Un atacante que controle también la referencia no sería detectado.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-479
def se479_reglas_de_parada() -> Fig:
    rows = [['Repite el mismo paso', '50', '25', '3', '9', '3'], ['Oscila entre dos estados', '50', '25', '5', '9', '5'], ['Cambia de estado sin avanzar', '50', '25', 'no para', '9', '9'], ['Avanza 12 pasos y se estanca', '50', '25', 'no para', '21', '21'], ['Tarea larga legítima (60 pasos)', '50', '25', 'no para', 'no para', '25']]
    return tab('Pasos ejecutados antes de la parada según la regla, para cinco comportamientos de agente (tope de 200)',
               'Tabla con cuatro reglas de parada aplicadas a cinco comportamientos de agente: repetir el mismo paso se detiene en 50 pasos con el máximo, 25 con el presupuesto, 3 con el estado repetido y 9 sin avance; oscilar en 50, 25, 5 y 9; cambiar de estado sin avanzar en 50, 25, nunca y 9; avanzar 12 pasos y estancarse en 50, 25, nunca y 21; la tarea larga legítima de 60 pasos se detiene por error en 50 y 25 y no con las dos reglas de estado y avance; combinadas se detiene en 3, 5, 9, 21 y 25.',
               ['Comportamiento', '50 pasos', '30 000 tokens', 'Estado 3 veces', 'Sin avance en 8', 'Combinadas'], rows, [330, 100, 130, 130, 130, 120], row_h=44, size=13,
               note='La última fila no debe detenerse: el máximo y el presupuesto la cortan sin motivo y las combinadas heredan el falso paro. Los comportamientos son máquinas de estados del autor y los parámetros son arbitrarios.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-479
def se479_reanudar_sin_duplicar() -> Fig:
    rows = [['Sin punto de control (reiniciar)', '20,90', '99 %', '20,9'], ['Punto de control tras el efecto, en otra transacción', '0,31', '31 %', '0,3'], ['Clave de idempotencia por paso', '0,00', '0 %', '0,3'], ['Efecto y punto de control en una transacción', '0,00', '0 %', '0,3']]
    return tab('Reanudar tras una caída en una tarea de 30 pasos que envía un aviso por paso (500 caídas por variante)',
               'Tabla con la reanudación tras una caída en una tarea de 30 pasos que envía un aviso por paso en 500 caídas por variante: reiniciar desde cero duplica 20,90 avisos de media y deja algún duplicado en el 99 por ciento de las caídas; un punto de control tras el efecto en otra transacción duplica 0,31 y el 31 por ciento; la clave de idempotencia por paso y la transacción única con el punto de control no duplican ninguno, y las tres con punto de control recalculan 0,3 pasos de media.',
               ['Variante', 'Duplicados (media)', 'Caídas con duplicado', 'Pasos recalculados'], rows, [430, 170, 170, 150], row_h=44, size=13,
               note='Lo que duplica es el instante entre el efecto y el punto de control. Los efectos son filas de una base en memoria; un efecto externo necesita la clave de idempotencia en el receptor.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-479
def se479_evaluar_con_ruido() -> Fig:
    rows = [['20', '36,5 puntos', '0,4 %', '4,3 %', '0,45 %'], ['50', '24,4 puntos', '1,1 %', '8,3 %', '0,10 %'], ['100', '17,6 puntos', '2,2 %', '15,2 %', '0,00 %'], ['300', '10,3 puntos', '10,2 %', '38,1 %', '0,00 %'], ['1 000', '5,7 puntos', '60,7 %', '89,5 %', '0,00 %']]
    return tab('Dos agentes con aciertos de 70 y 76 %: detección de la diferencia según el número de tareas (2 000 repeticiones)',
               'Tabla con la comparación de dos agentes con aciertos de 70 y 76 por ciento según el número de tareas en 2000 repeticiones: con 20 tareas el intervalo de A mide 36,5 puntos y la prueba z declara a B mejor en el 4,3 por ciento; con 50, 24,4 y 8,3; con 100, 17,6 y 15,2; con 300, 10,3 y 38,1; con 1000, 5,7 y 89,5; en una distribución de dificultad con acierto de 70,1 por ciento en un intento, el acierto en tres de tres es 44,7 por ciento y dos intentos discrepan en el 31,4 por ciento de las tareas.',
               ['Tareas', 'Intervalo de A', 'Intervalos separados', 'Prueba z: B mejor', 'Prueba z: B peor'], rows, [130, 200, 220, 190, 180], row_h=44, size=13,
               note='Con la misma dificultad, el acierto en un intento es del 70,1 %, en tres de tres del 44,7 %, y dos intentos de una tarea discrepan en el 31,4 %. Con efectos grandes bastan veinte tareas; con seis puntos hacen falta del orden de mil.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-480
def se480_autodeclaracion_y_verificacion() -> Fig:
    rows = [['D1 envía todos los umbrales (RF-06)', 'no', 'sí', 'no', 'sí'], ['D2 no reabre al cambiar el vencimiento (RF-07)', 'no', 'sí', 'no', 'sí'], ['D3 estado de envíos en memoria (RF-09)', 'no', 'sí', 'sí', 'sí'], ['D4 distingue mayúsculas en el silencio (RF-04)', 'no', 'sí', 'no', 'sí'], ['D5 historial incompleto (RF-08)', 'no', 'sí', 'no', 'sí'], ['D6 avisa tras el vencimiento (RF-05)', 'no', 'sí', 'no', 'sí'], ['Total de 6', '0 de 6', '6 de 6', '1 de 6', '6 de 6']]
    return tab('Seis defectos inyectados en un servicio de diez requisitos: qué vía de verificación los detecta',
               'Tabla con seis defectos inyectados en un servicio de avisos de diez requisitos y tres vías de verificación: la autodeclaración con las tres pruebas del camino feliz detecta 0 de 6, las pruebas por requisito de RF-01 a RF-08 detectan 6 de 6, las pruebas de reinicio y copia detectan 1 de 6 y la vista combinada detecta 6 de 6; con los seis defectos a la vez siete de los diez requisitos tienen una prueba en rojo y los tres de la autodeclaración siguen en verde.',
               ['Defecto (requisito)', 'Autodeclaración', 'Pruebas RF-01 a RF-08', 'Reinicio y copia', 'Combinada'], rows, [400, 140, 150, 130, 100], row_h=40, size=12,
               note='Con los seis defectos a la vez, siete de diez requisitos tienen una prueba en rojo y los tres de la autodeclaración siguen en verde. Los defectos los eligió el autor: el 6 de 6 es una cota superior, no una tasa de detección.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-480
def se480_restaurar_una_copia() -> Fig:
    rows = [['Cada 24 h', '28,9', '6,8', '87 %', '100 %'], ['Cada 6 h', '6,9', '1,4', '60 %', '100 %'], ['Cada 1 h', '0,8', '0,0', '0 %', '100 %']]
    return tab('Restaurar una copia de un servicio con 30 entregas y 60 pasadas al día durante tres días (400 caídas por fila)',
               'Tabla con la restauración de una copia de un servicio de avisos con 30 entregas y 60 pasadas al día durante tres días en 400 caídas por fila: con una copia cada 24 horas se pierden 28,9 pasadas de media y se reenviarían 6,8 avisos, con algún reenvío en el 87 por ciento de las caídas; con una cada 6 horas 6,9 y 1,4, el 60 por ciento; con una cada hora 0,8 y 0,0, el 0 por ciento; todas las copias pasan la comprobación de integridad.',
               ['Frecuencia de copia', 'Pasadas perdidas', 'Avisos reenviados', 'Caídas con reenvío', 'Copias íntegras'], rows, [240, 170, 190, 170, 150], row_h=44, size=13,
               note='La copia en línea de SQLite sale siempre íntegra; la frecuencia decide cuántos estudiantes reciben un aviso repetido. La caída uniforme en el tiempo y la ausencia de escrituras concurrentes son supuestos del autor.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-480
def se480_paquete_de_evidencia() -> Fig:
    rows = [['RF-01 umbrales de 72, 24 y 1 hora', '2', 'verde', 'ninguno', '—'], ['RF-02 no repetir un aviso', '1', 'verde', 'ninguno', '—'], ['RF-03 no avisar si está entregada', '1', 'verde', 'ninguno', '—'], ['RF-04 no avisar si está silenciada', '1', 'verde', 'D4', 'sí'], ['RF-05 no avisar tras el vencimiento', '2', 'verde', 'D6', 'sí'], ['RF-06 solo el umbral más cercano tras una caída', '1', 'verde', 'D1', 'sí'], ['RF-07 cambiar el vencimiento reabre umbrales', '1', 'verde', 'D2', 'sí'], ['RF-08 registrar cada aviso en el historial', '1', 'verde', 'D5', 'sí'], ['RF-09 reiniciar no repite avisos', '1', 'verde', 'D3', 'sí'], ['RF-10 una copia restaurada es consistente', '1', 'verde', 'ninguno', '—']]
    return tab('Paquete de evidencia de diez requisitos y doce pruebas: qué requisitos tienen una variante que su prueba detecta',
               'Tabla con el paquete de evidencia de diez requisitos de un servicio de avisos y doce pruebas: todos están en verde con el servicio de referencia; seis requisitos, el cuatro, cinco, seis, siete, ocho y nueve, tienen una variante defectuosa que su prueba detecta; los cuatro requisitos uno, dos, tres y diez no tienen variante que demuestre que su prueba puede fallar.',
               ['Requisito', 'Pruebas', 'Resultado', 'Defecto que lo rompe', '¿La prueba lo detecta?'], rows, [430, 90, 110, 170, 150], row_h=40, size=12,
               note='Cuatro requisitos están en verde sin una variante que demuestre que su prueba puede fallar: verde significa pasa, no verificado. Hay una sola variante por requisito, de modo que la figura muestra que la capacidad de detección no es nula, no cuánta tiene.',
               note_kind='coral', foot=EJEC)


FIGURES = {
    "se-475-validar-cada-mensaje.svg": se475_validar_cada_mensaje,
    "se-475-descripciones-y-huellas.svg": se475_descripciones_y_huellas,
    "se-475-cache-y-obsolescencia.svg": se475_cache_y_obsolescencia,
    "se-476-contexto-con-subagentes.svg": se476_contexto_con_subagentes,
    "se-476-hechos-que-sobreviven.svg": se476_hechos_que_sobreviven,
    "se-476-colisiones-de-edicion.svg": se476_colisiones_de_edicion,
    "se-476-protocolos-de-escritura.svg": se476_protocolos_de_escritura,
    "se-477-politicas-de-aprobacion.svg": se477_politicas_de_aprobacion,
    "se-477-deshacer-con-diario.svg": se477_deshacer_con_diario,
    "se-477-compensar-un-flujo.svg": se477_compensar_un_flujo,
    "se-478-filtros-de-instrucciones.svg": se478_filtros_de_instrucciones,
    "se-478-tres-capacidades.svg": se478_tres_capacidades,
    "se-478-registro-que-se-nota.svg": se478_registro_que_se_nota,
    "se-479-reglas-de-parada.svg": se479_reglas_de_parada,
    "se-479-reanudar-sin-duplicar.svg": se479_reanudar_sin_duplicar,
    "se-479-evaluar-con-ruido.svg": se479_evaluar_con_ruido,
    "se-480-autodeclaracion-y-verificacion.svg": se480_autodeclaracion_y_verificacion,
    "se-480-restaurar-una-copia.svg": se480_restaurar_una_copia,
    "se-480-paquete-de-evidencia.svg": se480_paquete_de_evidencia,
}
