"""Figures for SE-475 to SE-480 (SPEC, agents and agentic life cycle: synthetic data with fixed seeds, plus runs of real CPython/SQLite code on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars


SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."

# ---------------------------------------------------------------- SE-475
def se475_validar_cada_mensaje() -> Fig:
    return heatmap(
        "Cien mensajes y tres niveles de comprobación: cuántos de cada clase se ejecutan",
        "Mapa de calor con los mensajes malformados que se ejecutan, de 5 por clase, según el nivel de comprobación: con solo la forma JSON-RPC se ejecutan 25 de los 40 malformados, con versión y método de la cabecera 15 y con nombre, argumentos y alcance ninguno; los 5 mensajes con cabecera de una herramienta permitida y cuerpo de borrar historial se ejecutan en los dos primeros niveles y en el tercero no.",
        ["JSON roto", "Sin identificador", "Versión antigua", "Método distinto en cabecera y cuerpo", "Nombre distinto en cabecera y cuerpo", "Herramienta inexistente", "Argumento de tipo equivocado", "Recurso fuera de alcance", "Cabecera permitida, cuerpo de borrar historial"],
        ["Solo forma", "+ versión y método", "+ nombre, argumentos y alcance"],
        [[5, 0, 0], [5, 0, 0], [5, 5, 0], [5, 5, 0], [5, 5, 5], [5, 0, 0], [5, 5, 5], [5, 5, 5], [5, 5, 0]],
        unit="Ejecutados de 5", scale="coral", vmin=0, vmax=5, decimals=0, label_w=300, cell_h=38,
        note="Los 60 mensajes válidos pasan siempre, en los tres niveles. La última fila es el desajuste entre quien autoriza por cabecera y quien ejecuta el cuerpo. El manejador es una imitación escrita por el autor, no una implementación conforme.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-475
def se475_descripciones_y_huellas() -> Fig:
    return grouped_bars(
        "Catálogo de 20 herramientas con 4 descripciones con instrucciones: buscador de patrones y huellas fijadas",
        "Barras horizontales con los resultados de un catálogo de 20 herramientas, 4 con instrucciones escondidas: el buscador de patrones halla 3 de las 4 y marca 3 legítimas; la huella fijada alerta en 6 de 6 actualizaciones, 4 benignas y 2 maliciosas; el buscador marca solo 1 de las 2 actualizaciones maliciosas.",
        ["Buscador: descripciones con instrucciones halladas (de 4)", "Buscador: herramientas legítimas marcadas", "Buscador: actualizaciones maliciosas marcadas (de 2)", "Huella fijada: actualizaciones que alertan (de 6)"],
        [("Cantidad", [3, 3, 1, 6], "navy")],
        unit="Herramientas o actualizaciones", horizontal=True, decimals=0, label_w=330,
        note="El buscador marca 6 herramientas; la descripción que no usa palabras de mando pasa. La huella no deja pasar ningún cambio y a cambio obliga a revisar también los benignos (4 de las 6 alertas); el buscador prioriza qué leer primero y falla de las dos maneras. Las descripciones y los patrones los escribió el autor.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-475
def se475_cache_y_obsolescencia() -> Fig:
    return grouped_bars(
        "Caché de listados durante siete días con 120 consultas por hora y un cambio de catálogo cada seis horas de media",
        "Barras horizontales en escala logarítmica con las lecturas por día según el tiempo de vida de la caché: sin caché 2853 y ninguna respuesta vieja; con 30 segundos 1436 y 0,04 por ciento viejas; con 5 minutos 262 y 0,71; con una hora 24 y 8,66; con un día 1 y 79,01 por ciento de respuestas viejas.",
        ["Sin caché (0,00 % con catálogo viejo)", "30 segundos (0,04 %)", "5 minutos (0,71 %)", "1 hora (8,66 %)", "1 día (79,01 %)"],
        [("Lecturas por día", [2853, 1436, 262, 24, 1], "navy")],
        unit="Lecturas por día", horizontal=True, log=True, decimals=0, label_w=250,
        note="Entre paréntesis, las respuestas con catálogo viejo; la antigüedad máxima de un cambio no visto crece de menos de 1 minuto con 30 s a 5 min, 58 min y 1 405 min (23 h). La elección del tiempo de vida es de riesgo, no de comodidad: una retirada urgente de una herramienta tarda en surtir efecto lo que dure la caché. Los cambios de catálogo son un proceso de Poisson supuesto.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-476
def se476_contexto_con_subagentes() -> Fig:
    return grouped_bars(
        "Contexto de entrada procesado por un agente único y por ocho subagentes según la lectura redundante",
        "Barras horizontales con los millones de tokens de entrada procesados: el agente único procesa 4,16 y termina con 165000; con subagentes el consumo es 0,90 con lectura mínima, 1,46 con el doble, 2,02 con el triple, 2,58 con el cuádruple y 3,70 con seis veces, y el contexto final del orquestador es siempre 17000 tokens.",
        ["Agente único (100 %)", "Subagentes, lectura mínima 1× (22 %)", "Subagentes, 2× (35 %)", "Subagentes, 3× (49 %)", "Subagentes, 4× (62 %)", "Subagentes, 6× (89 %)"],
        [("Tokens procesados", [4.16, 0.90, 1.46, 2.02, 2.58, 3.70], "navy")],
        unit="Millones de tokens procesados", horizontal=True, decimals=2, label_w=260,
        note="Entre paréntesis, el consumo frente al agente único. Contexto final: 165 000 tokens del agente único y 17 000 del orquestador. El modelo cuenta solo tokens de entrada por turno: no incluye salida, caché ni coordinación, y por eso no contradice que en la práctica los sistemas multiagente consuman más. Muestra la forma cuadrática del agente único.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-476
def se476_hechos_que_sobreviven() -> Fig:
    return grouped_bars(
        "Probabilidad de que cinco hechos necesarios lleguen al orquestador según la retención de cada resumen",
        "Barras agrupadas con la probabilidad de que lleguen los cinco hechos según la retención de cada resumen: con 99 por ciento llegan el 95,1 por ciento de las veces, con 95 el 77,4, con 90 el 59,0 y con 80 el 32,8; la simulación de 20000 corridas da 95,1, 77,3, 59,0 y 33,0.",
        ["Retención del 99 %", "Retención del 95 %", "Retención del 90 %", "Retención del 80 %"],
        [("Cálculo", [95.1, 77.4, 59.0, 32.8], "navy"), ("Simulación (20 000 corridas)", [95.1, 77.3, 59.0, 33.0], "teal")],
        unit="Llegan los 5 hechos (%)", decimals=1, plot_h=260,
        note="La probabilidad cae como la retención elevada al número de hechos. Se supone independencia entre hechos; en la práctica se pierden primero los números y los matices.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-476
def se476_colisiones_de_edicion() -> Fig:
    xs = [2, 3, 4, 6, 8]
    return line_chart(
        "Probabilidad de conflicto de edición con 60 archivos y 5 por agente según el reparto",
        "Líneas con la probabilidad de conflicto de edición según los agentes y el reparto: con reparto al azar 36,5 por ciento con dos agentes, 75,3 con tres, 94,4 con cuatro y 100 con seis y ocho; con propiedad por carpeta 0,0 en todos los casos; con propiedad y 20 por ciento de tareas con un archivo común 0,7, 2,0, 3,6, 8,9 y 16,0.",
        [("Reparto al azar", list(zip(xs, [36.5, 75.3, 94.4, 100.0, 100.0])), "coral"), ("Propiedad por carpeta", list(zip(xs, [0.0, 0.0, 0.0, 0.0, 0.0])), "teal"),
         ("Propiedad y 20 % con archivo común", list(zip(xs, [0.7, 2.0, 3.6, 8.9, 16.0])), "gold")],
        x_label="Agentes", y_label="Probabilidad de conflicto (%)", x_ticks=[(x, str(x)) for x in xs], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none", decimals=1, plot_h=300,
        note="Los archivos comunes reintroducen el conflicto aunque cada agente respete su zona. El trabajo real no elige archivos al azar y la propiedad rara vez se respeta al 100 %.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-476
def se476_protocolos_de_escritura() -> Fig:
    return grouped_bars(
        "Tres protocolos de escritura de cuatro agentes sobre una fila compartida de SQLite en 200 rondas",
        "Barras agrupadas con las contribuciones perdidas de 800, los reintentos y los ticks de espera de tres protocolos: la escritura ciega pierde 600 sin reintentos ni espera; la versión optimista no pierde ninguna y hace 1200 reintentos; el arrendamiento con caducidad no pierde ninguna, no reintenta y espera 980 ticks.",
        ["Escritura ciega", "Versión optimista", "Arrendamiento con caducidad"],
        [("Contribuciones perdidas de 800", [600, 0, 0], "coral"), ("Reintentos", [0, 1200, 0], "gold"), ("Ticks de espera", [0, 0, 980], "navy")],
        unit="Cantidad", decimals=0, plot_h=260,
        note="La pérdida de la escritura ciega es estructural: sobrevive una de cuatro contribuciones. Los cuatro agentes leen a la vez en cada ronda, el caso peor para la versión optimista; SQLite en memoria no reproduce la concurrencia real.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-477
def se477_politicas_de_aprobacion() -> Fig:
    return grouped_bars(
        "Cuatro políticas de aprobación en 5 000 sesiones de 200 acciones con un 4 % irreversibles",
        "Barras horizontales en escala logarítmica con los avisos por sesión y las irreversibles ejecutadas por sesión: preguntar en cada acción genera 200 avisos y deja ejecutar 3,02, con 93,5 por ciento de sesiones afectadas; preguntar por riesgo 22,5 y 1,30; aprobar un plan 11,1 y 1,18; preguntar solo lo irreversible con pausa 8,0 y 0,54, con 41,5 por ciento.",
        ["Preguntar en cada acción (93,5 % de sesiones con alguna)", "Preguntar solo las de riesgo (73,2 %)", "Aprobar el plan y preguntar las desviaciones (69,5 %)", "Solo lo irreversible, con pausa obligatoria (41,5 %)"],
        [("Avisos por sesión", [200.0, 22.5, 11.1, 8.0], "grey"), ("Irreversibles ejecutadas por sesión", [3.02, 1.30, 1.18, 0.54], "coral")],
        unit="Avisos o irreversibles por sesión", horizontal=True, log=True, decimals=2, label_w=300,
        note="Entre paréntesis, el porcentaje de sesiones con alguna acción irreversible ejecutada. El clasificador de riesgo supone un 90 % de aciertos y un 8 % de falsas alarmas. Preguntar por todo agota la atención en lo rutinario. La última política supone saber qué es irreversible. La función de atención, el 4 % y el clasificador son supuestos del autor: no se observó a ninguna persona.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-477
def se477_deshacer_con_diario() -> Fig:
    return stacked_bars(
        "Sesenta acciones de un generador con semilla sobre 40 archivos y su deshacer con un diario por acción",
        "Barra apilada con las 60 acciones de un generador sobre 40 archivos: 55 sobre archivos, que el diario deshace hasta dejar el estado igual al inicial, y 5 correos simulados que el diario no puede deshacer.",
        ["60 acciones"], [("Acciones que el diario deshace (archivos)", [55], "teal"), ("Acciones que no se pueden deshacer (correos)", [5], "coral")],
        unit="Acciones", horizontal=True, decimals=0, label_w=130,
        note="El directorio cambió tras las 60 acciones y, al deshacer en orden inverso, el estado coincide con el inicial. El diario ocupa 2 216 bytes (85 % del espacio). El diario restaura el estado de los archivos y no lo que sale del sistema. Son archivos pequeños, sin enlaces simbólicos, permisos especiales ni caídas a mitad de acción.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-477
def se477_compensar_un_flujo() -> Fig:
    return stacked_bars(
        "Flujo de cinco pasos con 8 % de fallo por intento: consistencia según la estrategia de compensación (20 000 ejecuciones)",
        "Barras apiladas horizontales con el resultado de 20000 ejecuciones según la compensación: sin compensación el 34,3 por ciento queda a medias; compensar sin reintentar deja 95,5 por ciento consistente y 4,5 a medias; con dos reintentos 100,0 y 0,1; con el paso 3 irreversible 87,8 consistente y 12,1 con efecto residual.",
        ["Sin compensación", "Compensar sin reintentar", "Compensar con 2 reintentos", "Con 2 reintentos y el paso 3 irreversible"],
        [("Consistentes", [65.7, 95.5, 100.0, 87.8], "teal"), ("A medias", [34.3, 4.5, 0.1, 0.0], "gold"), ("Con efecto residual", [0.0, 0.0, 0.0, 12.1], "coral")],
        unit="Ejecuciones (%)", horizontal=True, decimals=1, label_w=250,
        note="Ejecuciones completas: 65,7 %, 65,4 %, 65,4 % y 65,6 %. Un paso irreversible deja un efecto que ninguna compensación elimina; conviene ponerlo al final. El 8 % de fallo y la independencia entre intentos son supuestos del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-478
def se478_filtros_de_instrucciones() -> Fig:
    return heatmap(
        "Cuatro filtros de instrucciones inyectadas sobre 200 documentos: 40 con una orden de prueba en cinco formas y 160 inocuos",
        "Mapa de calor con las órdenes detectadas, de 8 por forma, por cuatro filtros: la frase fija detecta 8 de 8 directas y ninguna de las otras formas; normalizar y decodificar suma las de ancho cero y las codificadas; unir los campos suma las repartidas; el patrón amplio detecta las 40 y marca 19 de los 160 documentos inocuos.",
        ["Frase fija sobre el texto sin tratar", "+ normalizar el texto y decodificar", "+ unir los campos antes de buscar", "+ patrón amplio (paráfrasis)"],
        ["Directa", "Parafraseada", "Ancho cero", "Codificada", "Repartida"],
        [[8, 0, 0, 0, 0], [8, 0, 8, 8, 0], [8, 0, 8, 8, 8], [8, 8, 8, 8, 8]],
        unit="Detectadas de 8", scale="teal", vmin=0, vmax=8, decimals=0, label_w=280,
        note="Inocuos marcados de 160: 0, 0, 0 y 19. Cada forma que se cierra añade ingeniería o falsas alarmas: el patrón amplio marca 19 de 160 inocuos. El 100 % es consecuencia de un conjunto de pruebas escrito conociendo las cinco formas; no se midió ningún modelo.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-478
def se478_tres_capacidades() -> Fig:
    return stacked_bars(
        "Doce tareas típicas de un agente y cinco políticas sobre datos privados, contenido no confiable y comunicación hacia fuera",
        "Barras apiladas horizontales con las 12 tareas según la política: sin restricción pasan 12 sin ayuda; quitar la comunicación hacia fuera deja 6 y bloquea 6; quitar el contenido no confiable deja 4 y bloquea 8; quitar los datos privados deja 2 y bloquea 10; marcar lo leído y exigir aprobación para salir deja 9 sin ayuda y 3 con aprobación, sin ninguna bloqueada.",
        ["Sin restricción", "Quitar la comunicación hacia fuera", "Quitar el contenido no confiable", "Quitar los datos privados", "Marcar lo leído como no confiable y exigir aprobación para salir"],
        [("Sin ayuda", [12, 6, 4, 2, 9], "teal"), ("Bloqueadas", [0, 6, 8, 10, 0], "coral"), ("Con aprobación", [0, 0, 0, 0, 3], "gold")],
        unit="Tareas de 12", horizontal=True, decimals=0, label_w=310,
        note="Sin restricción, 3 de las 12 tareas reúnen las tres capacidades sin aprobación. En 5 000 configuraciones de 6 herramientas de un catálogo de 15, el 73,5 % reúne las tres capacidades. Las tareas y sus capacidades son una clasificación del autor tratada como todo o nada.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-478
def se478_registro_que_se_nota() -> Fig:
    return heatmap(
        "Cinco manipulaciones de un registro de auditoría de 500 eventos: fracción detectada por esquema (200 ensayos cada una)",
        "Mapa de calor con la fracción detectada de cinco manipulaciones de un registro de 500 eventos: un registro simple detecta 0 por ciento en todas; una cadena de huellas detecta 100 por ciento de editar, borrar e intercambiar eventos y 0 de cortar los últimos 20 o reescribir y recalcular; con la huella final guardada aparte se detectan las cinco al 100 por ciento.",
        ["Editar un evento", "Borrar un evento", "Intercambiar dos eventos", "Cortar los últimos 20 eventos", "Reescribir desde un punto y recalcular la cadena"],
        ["Registro simple", "Cadena de huellas", "Cadena y huella final aparte"],
        [[0, 100, 100], [0, 100, 100], [0, 100, 100], [0, 0, 100], [0, 0, 100]],
        unit="Detectado (%)", scale="navy", vmin=0, vmax=100, decimals=0, label_w=300,
        note="La integridad de un registro es una propiedad de quién controla la referencia: quien puede reescribir la cadena entera produce una cadena válida. Un atacante que controle también la referencia no sería detectado.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-479
def se479_reglas_de_parada() -> Fig:
    return heatmap(
        "Pasos ejecutados antes de la parada según la regla, para cinco comportamientos de agente (tope de 200)",
        "Mapa de calor con los pasos antes de la parada de cinco comportamientos según cinco reglas: repetir el mismo paso se detiene en 50 con el máximo, 25 con el presupuesto, 3 con el estado repetido y 9 sin avance; oscilar en 50, 25, 5 y 9; cambiar de estado sin avanzar en 50, 25, nunca y 9; avanzar 12 pasos y estancarse en 50, 25, nunca y 21; la tarea legítima de 60 pasos se corta por error en 50 y 25; combinadas, 3, 5, 9, 21 y 25.",
        ["Repite el mismo paso", "Oscila entre dos estados", "Cambia de estado sin avanzar", "Avanza 12 pasos y se estanca", "Tarea larga legítima (60 pasos)"],
        ["50 pasos", "30 000 tokens", "Estado 3 veces", "Sin avance en 8", "Combinadas"],
        [[50, 25, 3, 9, 3], [50, 25, 5, 9, 5], [50, 25, None, 9, 9], [50, 25, None, 21, 21], [50, 25, None, None, 25]],
        unit="Pasos hasta parar (celda vacía: no para)", scale="coral", vmin=0, vmax=50, decimals=0, label_w=260,
        note="Las celdas vacías son los casos en que la regla no para al agente. La última fila no debe detenerse: el máximo y el presupuesto la cortan sin motivo y las combinadas heredan el falso paro. Los comportamientos son máquinas de estados del autor y los parámetros son arbitrarios.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-479
def se479_reanudar_sin_duplicar() -> Fig:
    return grouped_bars(
        "Reanudar tras una caída en una tarea de 30 pasos que envía un aviso por paso (500 caídas por variante)",
        "Barras horizontales con los avisos duplicados de media y los pasos recalculados en 500 caídas por variante: reiniciar desde cero duplica 20,90 y deja algún duplicado en el 99 por ciento de las caídas; un punto de control tras el efecto en otra transacción duplica 0,31 en el 31 por ciento; la clave de idempotencia por paso y la transacción única no duplican ninguno.",
        ["Sin punto de control, reiniciar (99 % de caídas con duplicado)", "Punto de control tras el efecto, otra transacción (31 %)", "Clave de idempotencia por paso (0 %)", "Efecto y punto de control en una transacción (0 %)"],
        [("Duplicados (media)", [20.90, 0.31, 0.0, 0.0], "coral"), ("Pasos recalculados", [20.9, 0.3, 0.3, 0.3], "navy")],
        unit="Avisos duplicados o pasos recalculados", horizontal=True, decimals=2, label_w=310,
        note="Entre paréntesis, las caídas con algún duplicado. Lo que duplica es el instante entre el efecto y el punto de control. Los efectos son filas de una base en memoria; un efecto externo necesita la clave de idempotencia en el receptor.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-479
def se479_evaluar_con_ruido() -> Fig:
    xs = [20, 50, 100, 300, 1000]
    return line_chart(
        "Dos agentes con aciertos de 70 y 76 %: detección de la diferencia según el número de tareas (2 000 repeticiones)",
        "Líneas en escala logarítmica con el porcentaje de repeticiones que detectan la diferencia entre dos agentes con aciertos de 70 y 76 por ciento según las tareas: la prueba z declara a B mejor en 4,3 por ciento con 20 tareas, 8,3 con 50, 15,2 con 100, 38,1 con 300 y 89,5 con 1000; los intervalos separados en 0,4, 1,1, 2,2, 10,2 y 60,7.",
        [("Prueba z: B mejor", list(zip(xs, [4.3, 8.3, 15.2, 38.1, 89.5])), "teal"), ("Intervalos separados", list(zip(xs, [0.4, 1.1, 2.2, 10.2, 60.7])), "coral")],
        x_label="Tareas de la evaluación", y_label="Repeticiones que detectan la diferencia (%)", log_x=True,
        x_ticks=[(x, f"{x:,}".replace(",", " ")) for x in xs], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="all", decimals=1, plot_h=300,
        note="Semiancho del intervalo de A: 36,5, 24,4, 17,6, 10,3 y 5,7 puntos; la prueba z declara a B peor en 0,45 %, 0,10 % y 0,00 %. Con la misma dificultad, el acierto en un intento es del 70,1 %, en tres de tres del 44,7 %, y dos intentos de una tarea discrepan en el 31,4 %. Con efectos grandes bastan veinte tareas; con seis puntos hacen falta del orden de mil.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-480
def se480_autodeclaracion_y_verificacion() -> Fig:
    return heatmap(
        "Seis defectos inyectados en un servicio de diez requisitos: qué vía de verificación los detecta",
        "Mapa de calor con seis defectos inyectados en un servicio de avisos de diez requisitos y cuatro vías de verificación: la autodeclaración con tres pruebas del camino feliz detecta 0 de 6, las pruebas por requisito de RF-01 a RF-08 detectan 6 de 6, las pruebas de reinicio y copia detectan 1 de 6 y la vista combinada 6 de 6.",
        ["D1 envía todos los umbrales (RF-06)", "D2 no reabre al cambiar el vencimiento (RF-07)", "D3 estado de envíos en memoria (RF-09)", "D4 distingue mayúsculas en el silencio (RF-04)", "D5 historial incompleto (RF-08)", "D6 avisa tras el vencimiento (RF-05)"],
        ["Autodeclaración", "Pruebas RF-01 a RF-08", "Reinicio y copia", "Combinada"],
        [[0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]],
        unit="Detectado", scale="navy", vmin=0, vmax=1, cell_fmt=lambda v: "sí" if v else "no", label_w=310,
        note="Con los seis defectos a la vez, siete de diez requisitos tienen una prueba en rojo y los tres de la autodeclaración siguen en verde. Los defectos los eligió el autor: el 6 de 6 es una cota superior, no una tasa de detección.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-480
def se480_restaurar_una_copia() -> Fig:
    return grouped_bars(
        "Restaurar una copia de un servicio con 30 entregas y 60 pasadas al día durante tres días (400 caídas por fila)",
        "Barras agrupadas con las pasadas perdidas y los avisos reenviados de media según la frecuencia de copia: una copia cada 24 horas pierde 28,9 pasadas y reenvía 6,8 avisos, con algún reenvío en el 87 por ciento de las caídas; cada 6 horas 6,9 y 1,4, el 60 por ciento; cada hora 0,8 y 0,0, el 0 por ciento.",
        ["Cada 24 h (87 % de caídas con reenvío)", "Cada 6 h (60 %)", "Cada 1 h (0 %)"],
        [("Pasadas perdidas", [28.9, 6.9, 0.8], "coral"), ("Avisos reenviados", [6.8, 1.4, 0.0], "gold")],
        unit="Pasadas o avisos (media)", decimals=1, plot_h=260,
        note="Entre paréntesis, las caídas con algún reenvío. Todas las copias pasan la comprobación de integridad. La copia en línea de SQLite sale siempre íntegra; la frecuencia decide cuántos estudiantes reciben un aviso repetido. La caída uniforme en el tiempo y la ausencia de escrituras concurrentes son supuestos del autor.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-480
def se480_paquete_de_evidencia() -> Fig:
    return heatmap(
        "Paquete de evidencia de diez requisitos y doce pruebas: qué requisitos tienen una variante que su prueba detecta",
        "Mapa de calor con diez requisitos de un servicio de avisos, todos en verde con el servicio de referencia: seis de ellos, del cuatro al nueve, tienen una variante defectuosa que su prueba detecta; los cuatro restantes, uno, dos, tres y diez, no tienen variante que demuestre que su prueba puede fallar.",
        ["RF-01 umbrales de 72, 24 y 1 hora", "RF-02 no repetir un aviso", "RF-03 no avisar si está entregada", "RF-04 no avisar si está silenciada", "RF-05 no avisar tras el vencimiento",
         "RF-06 solo el umbral más cercano tras una caída", "RF-07 cambiar el vencimiento reabre umbrales", "RF-08 registrar cada aviso en el historial", "RF-09 reiniciar no repite avisos", "RF-10 una copia restaurada es consistente"],
        ["Variante que su prueba detecta"],
        [[0], [0], [0], [1], [1], [1], [1], [1], [1], [0]],
        unit="Con variante", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "sí" if v else "sin variante", label_w=330, cell_h=34,
        note="Defectos que rompen cada requisito: RF-04 D4, RF-05 D6, RF-06 D1, RF-07 D2, RF-08 D5 y RF-09 D3. Las pruebas por requisito son 2, 1, 1, 1, 2, 1, 1, 1, 1 y 1. Cuatro requisitos están en verde sin una variante que demuestre que su prueba puede fallar: verde significa pasa, no verificado. Hay una sola variante por requisito, de modo que la figura muestra que la capacidad de detección no es nula, no cuánta tiene.",
        note_kind="coral", foot=EJEC)


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
