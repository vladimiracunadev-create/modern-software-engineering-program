"""Figures for SE-343 to SE-348 (synthetic models with fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3).

Every figure is a chart or a diagram of the mechanism; the Markdown tables of the classes keep the exact values.
"""
from __future__ import annotations

from figure_kit import (Fig, grouped_bars, line_chart, percentile_intervals, stacked_bars, timeline)
from figures_part07_a import bars

SINT = "Modelos sintéticos con semilla fija; resultados idénticos en Windows y Ubuntu (WSL2) salvo donde se indica."


# ---------------------------------------------------------------- SE-343
def se343_lideres() -> Fig:
    return grouped_bars(
        "Cinco nodos y una partición: líderes que se creen legítimos según la regla de elección",
        "Barras agrupadas horizontales con los líderes simultáneos: con la regla «el identificador mayor que veo vivo», una partición de cinco nodos produce dos o tres líderes a la vez; con la regla de mayoría nunca hay más de uno y en un reparto 2, 2, 1 no hay ninguno. Las 15 biparticiones posibles producen dos líderes con la primera regla y nunca más de uno con la segunda.",
        ["Sin partición", "Partición en 2 y 3", "Partición en 1 y 4", "Partición en 1, 1 y 3", "Partición en 2, 2 y 1"],
        [("Regla «el mayor que veo»", [1, 2, 2, 3, 3], "coral"), ("Regla de mayoría", [1, 1, 1, 1, 0], "teal")],
        unit="Líderes que se creen legítimos", horizontal=True, label_w=190,
        note="La mayoría resuelve el cerebro dividido a cambio de disponibilidad: el grupo sin mayoría no elige a nadie (reparto 2, 2, 1). Dos mayorías siempre se cruzan en algún nodo, y de ahí sale la seguridad. En las 15 biparticiones posibles de 5 nodos la primera regla da 2 líderes en las 15 y la mayoría nunca más de 1. Es un modelo de conjuntos de nodos, sin mensajes ni tiempo.",
        note_kind="teal", foot="Enumeración exacta de particiones; sin simulación aleatoria.")


def se343_cerco() -> Fig:
    return grouped_bars(
        "Titular del arrendamiento que se pausa más de 10 s y escribe después de que otro tomó su lugar",
        "Barras con las tareas de 10 000 cuyo arrendamiento de 10 segundos caduca antes de que el titular escriba, según la pausa media: 1 con pausas de 1 s, 73 con 2 s, 854 con 4 s y 2 918 con 8 s. Sin testigo de cerco el almacén acepta esas escrituras tardías y con testigo las rechaza todas (849 en la corrida de media 4 s).",
        ["Pausa media 1 s", "Pausa media 2 s", "Pausa media 4 s", "Pausa media 8 s"],
        [("Arrendamiento caducado antes de escribir", [1, 73, 854, 2918], "coral")],
        unit="Tareas de 10 000", plot_h=260,
        note="En la corrida de media 4 s hay 849 escrituras de un titular caducado (otra semilla da 854 caducados): sin testigo el almacén las acepta todas, con un número de cerco creciente las rechaza todas. El arrendamiento solo no basta porque el titular no sabe que caducó. Las pausas exponenciales son un supuesto del autor.",
        note_kind="coral", foot=SINT)


def se343_plazos() -> Fig:
    pts = [(0, 7650, "7 650", "t"), (25, 7863, "7 863", "t"), (50, 4057, "4 057", "r"), (100, 725, "725", "t"), (150, 461, "461", "t"), (300, 333, "333", "t")]
    return line_chart(
        "Elección de líder entre cinco nodos: tiempo medio hasta tener líder según la anchura del plazo aleatorio",
        "Línea en escala logarítmica con el tiempo medio hasta tener líder según cuánto se ensancha el plazo de elección sobre 150 ms: con 0 y 25 ms de dispersión no se llega a un líder en 50 rondas (7 650 y 7 863 ms); con 50 ms, 25,5 rondas y 4 057 ms; con 150 ms, 2,49 rondas y 461 ms; con 300 ms, 1,54 rondas y 333 ms.",
        [("Tiempo medio hasta líder (ms)", pts, "teal")],
        x_label="Dispersión del plazo de elección sobre 150 ms (ms)", y_label="Tiempo medio hasta tener líder (ms)",
        log_y=True, x_ticks=[(0, "0"), (25, "25"), (50, "50"), (100, "100"), (150, "150"), (300, "300")],
        vlines=[(25, "retardo máximo de mensajes: 25 ms")], y_ticks=[100, 1000, 10000, 100000],
        point_labels="all", y_zero=False, plot_h=300,
        note="La dispersión de los plazos debe ser mayor que el retardo de los mensajes para que un candidato gane antes de que otro se presente: a la izquierda de la línea punteada no hay líder en 50 rondas. Con 300 ms de dispersión un líder sale en la primera ronda el 64,7 % de las veces; con 150 ms, el 40,3 %. Mayor dispersión tarda más en empezar una elección y menos en terminarla. Es un modelo simplificado inspirado en Raft, no Raft.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-344
def se344_entrega() -> Fig:
    return stacked_bars(
        "Contar 1 000 entregas cuando el consumidor se cae el 5 % de las veces en el peor punto",
        "Barras apiladas horizontales con el total contado de 1 000 entregas: aplicar y luego confirmar cuenta 1 053 por 53 duplicados de mensajes reentregados; confirmar y luego aplicar cuenta 950 y pierde 50; aplicar y registrar la clave de mensaje visto en la misma transacción cuenta exactamente 1 000.",
        ["Aplicar y luego confirmar (al menos una vez)", "Confirmar y luego aplicar (como mucho una vez)", "Aplicar y registrar la clave en una transacción"],
        [("Entregas contadas una vez", [1000, 950, 1000], "teal"), ("Duplicados contados de más", [53, 0, 0], "coral"),
         ("Entregas perdidas (no contadas)", [0, 50, 0], "gold")],
        unit="Entregas (el total correcto es 1 000)", horizontal=True, totals=False, label_w=300,
        note="El proceso exactamente una vez no existe entre dos sistemas: lo que se logra es efecto único sobre el estado porque aplicar y recordar viven en una sola transacción. El segmento dorado son entregas que faltan: el total contado es 950. El 5 % de caídas es un supuesto del autor; el estado es una base SQLite real en memoria.",
        note_kind="teal", foot=SINT)


def se344_retencion() -> Fig:
    pts = [(1, 48.20, "48,20 %", "r"), (60, 2.75, "2,75 %", "t"), (1440, 0.03, "0,03 %", "t")]
    return line_chart(
        "Duplicados que se reejecutan porque la clave de idempotencia ya se olvidó, según cuánto se retiene la clave",
        "Línea en escala logarítmica con los duplicados reejecutados de 20 000, según la retención de la clave: 48,20 por ciento con 1 minuto, 2,75 con 1 hora y 0,03 con 24 horas; con 7 días no escapa ninguno (0 de 20 000, no representable en escala logarítmica). La cola larga del retraso obliga a retener mucho más que la mediana de 55 s.",
        [("Duplicados reejecutados", pts, "coral")],
        x_label="Retención de la clave (minutos; 1 h = 60, 24 h = 1 440)", y_label="Duplicados reejecutados (% de 20 000)",
        log_x=True, log_y=True, x_ticks=[(1, "1 min"), (10, "10"), (60, "1 h"), (1440, "24 h")], y_ticks=[0.01, 0.1, 1, 10, 100],
        point_labels="all", plot_h=280,
        note="La retención de claves es una decisión de negocio sobre cuánto tarda en llegar el último duplicado posible, no un detalle de almacenamiento: con 7 días, 0 de 20 000. Además, 615 de 640 reutilizaciones de una clave con otro cuerpo habrían devuelto la respuesta ajena sin la huella del cuerpo. La distribución lognormal (mediana 55 s, p99 9 209 s) es un supuesto del autor.",
        note_kind="gold", foot=SINT)


def se344_salida() -> Fig:
    return grouped_bars(
        "200 tareas, el 5 % se reintenta tras escribir y antes de confirmar: qué queda mal en la salida",
        "Barras agrupadas con los defectos que deja la salida: anexar al archivo deja 9 filas duplicadas si la tarea es determinista y 14 si devuelve un valor aleatorio, con 13 claves con valores distintos; escribir por clave de tarea deja siempre 200 filas, sin duplicados ni claves con valores distintos.",
        ["Anexar · tarea determinista", "Anexar · valor aleatorio", "Por clave · tarea determinista", "Por clave · valor aleatorio"],
        [("Filas duplicadas", [9, 14, 0, 0], "coral"), ("Claves con valores distintos", [0, 13, 0, 0], "gold")],
        unit="Filas o claves de 200 tareas", plot_h=260,
        note="Escribir por clave convierte el reintento en una sobrescritura del mismo resultado (200 filas siempre); anexar convierte cada reintento en una fila más (209 y 214 filas) y, si la tarea no es determinista, en dos verdades. La tasa del 5 % y los valores son sintéticos; no se usó ningún sistema de procesamiento distribuido.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-345
def se345_balanceo() -> Fig:
    return percentile_intervals(
        "10 servidores, 200 000 solicitudes de tamaño Pareto y 85 % de carga: tiempo hasta terminar",
        "Intervalos con la mediana, el percentil 99 y el percentil 99,9 del tiempo hasta terminar una solicitud (tamaño medio 3,0) en escala logarítmica: con turnos rotativos 13,3, 316,8 y 535,1 unidades; con reparto aleatorio 19,9, 361,6 y 632,4; con dos opciones al azar 4,5, 95,4 y 203,6; con la de menos conexiones 2,7, 52,6 y 188,5.",
        [("Turnos rotativos", [13.3, 316.8, 535.1]), ("Aleatorio", [19.9, 361.6, 632.4]),
         ("Dos opciones al azar, la menos cargada", [4.5, 95.4, 203.6]), ("Menos conexiones (estado global)", [2.7, 52.6, 188.5])],
        unit="Unidades de tiempo (tamaño medio de solicitud 3,0)", marks=("mediana", "p99", "p99,9"), log=True, decimals=1, label_w=300,
        note="Repartir por turnos equilibra el número de solicitudes, no el trabajo: un tamaño de cola pesada deja un servidor atascado mientras otros esperan, y la mediana es parecida pero el p99 es seis veces mayor que con dos opciones. Mirar solo dos servidores logra casi todo el beneficio sin estado global. Los tamaños Pareto (forma 1,5) y el 85 % son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se345_conmutacion() -> Fig:
    return percentile_intervals(
        "Conmutar tras la caída del primario con 200 escrituras por segundo: costo de confirmar y escrituras perdidas",
        "Intervalos con la latencia de confirmación en escala logarítmica: la replicación asíncrona confirma en 1,0 ms y pierde en promedio 6,11 escrituras ya confirmadas al conmutar; la semisíncrona confirma en 21,1 ms de mediana y 63,6 ms en el percentil 99 y no pierde ninguna; la síncrona, 27,5 y 75,3 ms, tampoco pierde.",
        [("Asíncrona · pierde 6,11 escrituras", [1.0, 1.0]), ("Semisíncrona (1 réplica) · pierde 0", [21.1, 63.6]),
         ("Síncrona (2 réplicas) · pierde 0", [27.5, 75.3])],
        unit="Milisegundos hasta confirmar la escritura", marks=("mediana", "p99"), log=True, decimals=1, label_w=300,
        note="La pérdida es el trabajo que el cliente ya consideró guardado y que la réplica nunca vio (6,11 escrituras en promedio con replicación asíncrona). Pagarlo en latencia lo evita: de 1 ms a 21–28 ms de mediana. El retraso de 30 ms y el tiempo de ida y vuelta lognormal son supuestos del autor, no una red medida.",
        note_kind="coral", foot=SINT)


def se345_reparto() -> Fig:
    return grouped_bars(
        "Repartir por hash o por rango de fecha: fragmentos que toca cada operación (de 8)",
        "Barras agrupadas horizontales con los fragmentos de 8 que toca cada operación: con reparto por hash, las 5 000 escrituras más recientes se reparten entre los 8 fragmentos y toda consulta de un tramo de claves toca los 8; con rangos fijos, las 5 000 escrituras caen en un solo fragmento y las consultas de 100 y 10 000 claves tocan uno y la de 50 000, cinco.",
        ["5 000 escrituras recientes", "Consulta de 100 claves consecutivas", "Consulta de 10 000 claves consecutivas", "Consulta de 50 000 claves consecutivas"],
        [("Reparto por hash", [8, 8, 8, 8], "teal"), ("Reparto por rango fijo", [1, 1, 1, 5], "coral")],
        unit="Fragmentos que toca la operación (de 8)", horizontal=True, label_w=250,
        note="Cada reparto abarata una pregunta y encarece la otra: el hash esparce la escritura (578 a 674 por fragmento) y dispersa la lectura por rango; el rango agrupa la lectura y acumula las 5 000 escrituras nuevas en un fragmento. Ocho fragmentos y 100 000 claves son sintéticos; el hash es MD5 solo por su reparto, no por seguridad.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-346
def se346_reintentos() -> Fig:
    def s(vals):
        return list(zip((0, 20, 50, 80), vals))
    return line_chart(
        "Éxito de las solicitudes según el fallo inyectado y la estrategia del cliente (80 solicitudes por turno)",
        "Líneas con el éxito según el fallo inyectado: con 20 por ciento de fallo, los reintentos suben el éxito de 80,5 a 99,9 por ciento con 1,24 llamadas por solicitud; con 80 por ciento de fallo los reintentos llegan a 54,1 con 3,05 llamadas y el interruptor baja el éxito a 9,9 con 0,53 llamadas. Las curvas de reintentos e interruptor coinciden hasta el 50 por ciento.",
        [("Sin reintentos", s([100.0, 80.5, 50.1, 20.1]), "grey"), ("Con reintentos (máx. 4)", s([100.0, 99.9, 93.1, 54.1]), "gold"),
         ("Con interruptor", s([100.0, 99.9, 93.1, 9.9]), "coral")],
        x_label="Fallo inyectado en la dependencia (%)", y_label="Solicitudes con éxito (%)",
        x_ticks=[(0, "0"), (20, "20"), (50, "50"), (80, "80")], y_ticks=[0, 20, 40, 60, 80, 100],
        point_labels="last", plot_h=300, decimals=1,
        annotations=[(80, 54.1, "3,05 llamadas", -60, -30), (80, 9.9, "0,53 llamadas", -90, -20)],
        note="Un experimento de caos busca el punto donde la estrategia deja de proteger: aquí, entre 50 % y 80 %, los reintentos triplican la carga sobre una dependencia ya enferma (1,90 llamadas por solicitud con 50 % de fallo y 3,05 con 80 %, frente a 1,00) y el interruptor sacrifica éxito para dejarla respirar (0,53 llamadas). El servicio, su capacidad de 100 y el exceso son un modelo del autor.",
        note_kind="gold", foot=SINT)


def se346_planificador() -> Fig:
    return percentile_intervals(
        "El mismo defecto en 1 620 de 1 680 intercalaciones: ejecuciones al azar hasta verlo según el planificador",
        "Intervalos en escala logarítmica con las ejecuciones hasta el primer fallo (mediana y percentil 95) según la probabilidad de cambiar de hilo: con 1,0 el defecto aparece en 1 y 2 ejecuciones y falla el 84,35 por ciento; con 0,1, en 5 y 17; con 0,03 solo falla el 4,84 por ciento de las ejecuciones y hacen falta 14 de mediana y 57 en el percentil 95.",
        [("Cambio de hilo 1,0 · falla el 84,35 %", [1, 2]), ("Cambio 0,3 · falla el 40,34 %", [2, 6]),
         ("Cambio 0,1 · falla el 15,41 %", [5, 17]), ("Cambio 0,03 · falla el 4,84 %", [14, 57])],
        unit="Ejecuciones hasta el primer fallo", marks=("mediana", "p95"), log=True, decimals=0, label_w=300,
        note="No todas las intercalaciones son igual de probables: los planificadores reales mantienen un hilo en marcha un buen rato, y con hilos casi siempre seguidos (0,03) una pasada limpia dice poco. Una semilla guardada permite repetir exactamente el mismo orden (misma semilla, misma traza, comprobado).",
        note_kind="coral", foot=SINT)


def se346_plan() -> Fig:
    return stacked_bars(
        "Linter de planes de caos sobre 200 mutaciones: 147 detectadas y 53 que pasan",
        "Barras apiladas horizontales por tipo de mutación de un plan de experimento de caos: el linter de forma detecta las 50 de campo ausente o vacío, las 33 de alcance del 100 por ciento, las 29 de aborto inalcanzable y las 35 de hipótesis sin umbral, y ninguna de las 29 de resultado copiado de otro entorno ni de las 24 de reversión nunca ensayada.",
        ["Campo ausente o vacío", "Alcance del 100 % del tráfico", "Condición de aborto inalcanzable", "Hipótesis sin umbral medible",
         "Resultado copiado de otro entorno", "Reversión nunca ensayada"],
        [("Detectadas", [50, 33, 29, 35, 0, 0], "teal"), ("No detectadas", [0, 0, 0, 0, 29, 24], "coral")],
        unit="Mutaciones del plan", horizontal=True, label_w=250,
        note="Las dos que el linter no ve son las que convierten un experimento en teatro: un resultado que no se obtuvo y una reversión que nunca se probó. Las reglas se escribieron conociendo las mutaciones, así que cada tipo sale al 0 % o al 100 %; la exactitud sobre planes reales es desconocida.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-347
def se347_carrera() -> Fig:
    return timeline(
        "El calendario mínimo que reproduce la carrera del cupo: seis pasos de dos solicitudes",
        "Línea de tiempo de seis pasos en el orden en que dos solicitudes leen, comprueban y escriben un cupo de 1: la solicitud A lee y comprueba, la B lee antes de que A escriba, A escribe y B, con el valor viejo, comprueba y escribe, y se aceptan dos entregas con cupo 1. De las 20 intercalaciones de este tipo, 18 (90 por ciento) fallan; un calendario fallido de 40 pasos con ruido se redujo a estos 6.",
        [("Solicitud A", [(0, 1, "lee", "teal"), (1, 2, "comprueba", "teal"), (3, 4, "escribe", "teal")]),
         ("Solicitud B", [(2, 3, "lee", "gold"), (4, 5, "comprueba", "gold"), (5, 6, "escribe", "gold")])],
        unit="Orden de los pasos del calendario (sin escala de tiempo)", ticks=[0, 1, 2, 3, 4, 5, 6], t_max=6,
        events=[(3, "A escribe; B ya leyó el cupo viejo")], label_w=140,
        note="Un fallo reproducible se reduce eliminando pasos mientras siga fallando: lo que queda es la explicación (leer, comprobar, leer, escribir, comprobar, escribir). De las 20 intercalaciones de dos solicitudes con 3 pasos cada una, 18 aceptan dos entregas; el calendario al azar con 4 solicitudes y ruido tenía 40 pasos. El ruido son pasos ajenos al cupo y el calendario sale de la semilla 347; con hilos del sistema operativo no se controla el orden.",
        note_kind="teal", foot=SINT)


def se347_parcial() -> Fig:
    return stacked_bars(
        "Flujo de 5 pasos con efectos: puntos de fallo que dejan el estado coherente o incoherente",
        "Barras apiladas horizontales sobre los 5 puntos de fallo de un flujo de cinco pasos: un corte antes de cada paso, sin reintento, deja un estado incoherente en 4 de 5 puntos; perder la respuesta tras cada paso y reintentar el flujo entero lo deja incoherente en 5 de 5; con pasos idempotentes, en 0 de 5.",
        ["Corte antes de cada paso, sin reintento", "Respuesta perdida, reintento del flujo completo", "Respuesta perdida, pasos idempotentes"],
        [("Estado coherente", [1, 0, 5], "teal"), ("Estado incoherente", [4, 5, 0], "coral")],
        unit="Puntos de fallo del flujo (de 5)", horizontal=True, label_w=300,
        note="Los dos fallos parciales distintos, el corte y la respuesta perdida, necesitan defensas distintas: el corte pide atomicidad o compensación (solo el corte antes del primer paso deja todo intacto); la respuesta perdida pide idempotencia, porque el reintento repite cupo, entrega, penalización y aviso. Se enumeran todos los puntos del flujo; los efectos son contadores en memoria, sin red.",
        note_kind="coral", foot="Enumeración exacta de los puntos de fallo; sin aleatoriedad.")


def se347_repeticiones() -> Fig:
    items = [("5 ejecuciones", 6.9, "coral", "6,9 %"), ("10 ejecuciones", 13.4, "coral", "13,4 %"), ("50 ejecuciones", 51.3, "gold", "51,3 %"),
             ("100 ejecuciones", 76.3, "gold", "76,3 %"), ("200 ejecuciones", 94.4, "teal", "94,4 %"), ("300 ejecuciones", 98.7, "teal", "98,7 %")]
    return bars("Probabilidad de ver al menos una vez un fallo que aparece en 1 de cada 70 ejecuciones",
                "Barras con la probabilidad de ver un fallo que ocurre en 1 de cada 70 ejecuciones al repetir la prueba: 6,9 por ciento con 5 repeticiones, 13,4 con 10, 51,3 con 50, 76,3 con 100, 94,4 con 200 y 98,7 con 300.",
                items, 5.4, "Para el 95 % hacen falta 209 repeticiones y para el 99,9 % 481; una simulación de 10 000 campañas de 10 repeticiones dio 14,0 % frente al 13,4 % teórico. Enumerar las 70 intercalaciones las cubre todas. Repetir una prueba inestable en CI sin controlar el orden no la arregla.",
                label_w=190, width=980, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-348
def se348_escalera() -> Fig:
    return stacked_bars(
        "La base de entregas cae 60 s de 300 (50 lecturas y 10 escrituras por segundo): qué ve cada solicitud afectada",
        "Barras apiladas horizontales con las 3 600 solicitudes que llegan durante la caída de 60 segundos: con fallo duro fallan 3 000 lecturas y se rechazan 600 escrituras; con caché obsoleta las 3 000 lecturas se sirven obsoletas y las 600 escrituras se rechazan; con caché y cola, las 3 000 lecturas son obsoletas, ninguna falla y las 600 escrituras se encolan y se reenvían al volver.",
        ["Fallo duro", "Caché obsoleta para lecturas", "Caché + cola de escrituras"],
        [("Lecturas falladas", [3000, 0, 0], "coral"), ("Lecturas obsoletas servidas", [0, 3000, 3000], "gold"),
         ("Escrituras rechazadas", [600, 600, 0], "navy"), ("Escrituras encoladas y reenviadas", [0, 0, 600], "teal")],
        unit="Solicitudes durante la caída de 60 s", horizontal=True, label_w=220,
        note="Cada peldaño cambia un fallo visible por un estado que hay que declarar: una lectura vieja hasta N minutos, una escritura confirmada que aún no está en la base. No se pierden datos con la cola si cabe. Pasar de uno a otro es una decisión de producto con su límite, no un interruptor técnico. Tasas y duración son supuestos del autor.",
        note_kind="teal", foot=SINT)


def se348_sobrecarga() -> Fig:
    return stacked_bars(
        "Llegan 150 solicitudes por turno a un sistema que atiende 100, durante 120 turnos: adónde va el exceso",
        "Barras apiladas horizontales de las 18 000 solicitudes que llegan: se atienden 12 000 en las tres políticas; sin límite quedan 6 000 en cola; con cola acotada a 200 quedan 100 y se descartan 1 761 entregas y 4 139 listados; con prioridad quedan 100 y se descartan 0 entregas y 5 900 listados.",
        ["Sin límite", "Cola acotada a 200", "Cola acotada con prioridad"],
        [("Atendidas", [12000, 12000, 12000], "teal"), ("En cola al final", [6000, 100, 100], "gold"),
         ("Descartadas: entregas", [0, 1761, 0], "coral"), ("Descartadas: listados", [0, 4139, 5900], "navy")],
        unit="Solicitudes llegadas en 120 turnos", horizontal=True, label_w=200,
        note="Si llegan más solicitudes de las que se atienden, algo espera o se descarta; elegir qué se descarta es la política. La prioridad protege lo que no se puede reintentar sin costo: la espera media de una entrega pasa de 21,2 turnos sin límite a 2,0 con cola acotada y a 1,0 con prioridad, y la de un listado de 20,9 a 2,0 y 2,8. Que la cola crezca 50 por turno hasta 6 000 explica una espera que sube hasta unos 41 turnos (ley de Little). Las proporciones 30/70 y la capacidad son supuestos del autor.",
        note_kind="coral", foot=SINT)


def se348_paquete() -> Fig:
    return stacked_bars(
        "Validador del paquete del servicio distribuido sobre 200 mutaciones: 101 detectadas y 99 que pasan",
        "Barras apiladas horizontales por tipo de mutación de un paquete de servicio distribuido: el verificador de forma detecta las 59 de campo ausente, las 21 de degradación sin límite y las 21 de reintento «hasta que funcione», y ninguna de las 23 de presupuesto de tiempos incoherente, 23 de evidencia copiada, 25 de prueba nunca ejecutada ni 28 de garantía imposible.",
        ["Campo ausente o vacío", "Degradación sin límite declarado", "Reintento «hasta que funcione»", "Presupuesto de tiempos incoherente",
         "Evidencia copiada del servicio vecino", "Prueba de fallos que nunca se ejecutó", "Garantía imposible"],
        [("Detectadas", [59, 21, 21, 0, 0, 0, 0], "teal"), ("No detectadas", [0, 0, 0, 23, 23, 25, 28], "coral")],
        unit="Mutaciones del paquete", horizontal=True, label_w=260,
        note="Un paquete completo no es un paquete correcto. Lo que ningún validador de forma ve es lo que ocurre en las revisiones reales: un presupuesto de 800 ms con 3 llamadas de 500 ms, una garantía de exactamente una vez y disponible en cualquier partición, una prueba que no se corrió. Reglas escritas conociendo las mutaciones: la exactitud sobre paquetes reales es desconocida.",
        note_kind="gold", foot=SINT)


FIGURES = {
    "se-343-lideres-que-se-creen-legitimos.svg": se343_lideres,
    "se-343-testigo-de-cerco.svg": se343_cerco,
    "se-343-plazos-de-eleccion.svg": se343_plazos,
    "se-344-orden-de-aplicar-y-confirmar.svg": se344_entrega,
    "se-344-retencion-de-claves.svg": se344_retencion,
    "se-344-salida-por-anexo-o-por-clave.svg": se344_salida,
    "se-345-balanceo-y-cola-pesada.svg": se345_balanceo,
    "se-345-conmutacion-y-perdida.svg": se345_conmutacion,
    "se-345-hash-o-rango.svg": se345_reparto,
    "se-346-reintentos-e-interruptor.svg": se346_reintentos,
    "se-346-planificador-y-fallo-raro.svg": se346_planificador,
    "se-346-linter-de-planes-de-caos.svg": se346_plan,
    "se-347-carrera-y-calendario-minimo.svg": se347_carrera,
    "se-347-fallo-parcial-del-flujo.svg": se347_parcial,
    "se-347-repeticiones-para-ver-un-fallo.svg": se347_repeticiones,
    "se-348-escalera-de-degradacion.svg": se348_escalera,
    "se-348-sobrecarga-y-prioridad.svg": se348_sobrecarga,
    "se-348-validador-del-paquete.svg": se348_paquete,
}
