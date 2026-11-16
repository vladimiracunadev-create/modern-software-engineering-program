"""Figures for SE-307 to SE-312 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, line_chart, scatter, stacked_bars
from figures_part07_a import bars

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-307
def se307_frio() -> Fig:
    return grouped_bars(
        "Arranques en frío con picos de entrega según las instancias mantenidas (una hora de tráfico, escala logarítmica)",
        "Barras agrupadas en escala logarítmica con el porcentaje de peticiones que arranca en frío con picos de entrega: en toda la hora 0,40, 0,17 y 0,06 por ciento con 0, 5 y 10 instancias mantenidas, pero en los primeros 10 segundos del pico 11,1, 5,1 y 0,7 por ciento; con tráfico estable, sin instancias mantenidas, es solo 0,10 por ciento.",
        ["Sin instancias mantenidas", "5 instancias mantenidas", "10 instancias mantenidas"],
        [("En toda la hora", [0.40, 0.17, 0.06], "gold"), ("En los primeros 10 s del pico", [11.1, 5.1, 0.7], "coral")],
        unit="Peticiones con arranque en frío (%)", log=True, ticks=[0.01, 0.1, 1, 10, 100],
        note="El promedio engaña: 0,40 % parece despreciable, pero se concentra en los primeros segundos de la ráfaga, justo cuando hay gente entregando contra un plazo. El arranque en frío (0,8 s) y el tibio (30 ms) son supuestos del autor; el mecanismo es la espera mientras se crea una instancia por cada petición simultánea sin instancia libre.",
        note_kind="coral", foot=SINT)


def se307_costo() -> Fig:
    return grouped_bars(
        "Tráfico a partir del cual un servidor fijo cuesta menos que pagar por uso (unidades ficticias)",
        "Barras agrupadas con el tráfico de equilibrio en peticiones por segundo según la memoria de la función y la duración por petición: con 128 megabytes y 0,15 segundos es 22,2, más de la mitad de las 40 peticiones por segundo del servidor; con 1024 megabytes y un segundo baja a 0,7, el 2 por ciento.",
        ["128 MB", "512 MB", "1 024 MB"],
        [("0,15 s por petición", [22.2, 7.8, 4.2], "gold"), ("1,0 s por petición", [5.0, 1.3, 0.7], "teal")],
        unit="Tráfico de equilibrio (peticiones por segundo)", ticks=[0, 10, 20, 30, 40], ref_lines=[(40, "servidor fijo: 40 rps")],
        note="El equilibrio no es una propiedad del modelo serverless sino del producto memoria × duración y de la utilización: una función ligera y esporádica favorece el pago por uso; una pesada y sostenida favorece el servidor. Los precios (0,20 por millón, 0,0000167 por GB-s, 30 por servidor) son unidades ficticias de orden de magnitud, no una tarifa de proveedor; con dos servidores el equilibrio sube a 44,5 rps.",
        note_kind="gold", foot=SINT)


def se307_rumor() -> Fig:
    return line_chart(
        "Rondas para que un rumor llegue al 99 % de los pares conectados (1000 pares, 20 % desconectados, 200 repeticiones)",
        "Líneas con las rondas necesarias frente a los mensajes enviados al variar el fanout de 1 a 5: con fanout 1 el rumor tarda 17,8 rondas de media y 21 como máximo con 5003 mensajes; con fanout 2, 10,5 y 12 con 5402; con 3, 8,1 y 9 con 5769; con 5, 6,0 y 7 con 6563, de modo que cinco veces el fanout envía solo un 31 por ciento más de mensajes.",
        [("Rondas, máximo", [(5003, 21, "fanout 1: 21", "t"), (5402, 12, "fanout 2: 12", "t"), (5769, 9, "fanout 3: 9", "t"), (6563, 7, "fanout 5: 7", "t")], "coral"),
         ("Rondas, media", [(5003, 17.8, "17,8", "b"), (5402, 10.5, "10,5", "b"), (5769, 8.1, "8,1", "b"), (6563, 6.0, "6,0", "b")], "teal")],
        x_label="Mensajes enviados (media)", y_label="Rondas hasta el 99 % de los conectados",
        x_ticks=[(4800, "4 800"), (5200, "5 200"), (5600, "5 600"), (6000, "6 000"), (6400, "6 400"), (6800, "6 800")],
        y_ticks=[0, 5, 10, 15, 20, 25],
        note="Las rondas crecen con el logaritmo del tamaño (8,2 con 100 pares, 10,5 con 1000, 13,1 con 10 000) y se disparan cuando casi todos los pares están desconectados. Más fanout acorta la difusión y encarece el tráfico: cinco veces el fanout envía solo un 31 % más de mensajes. Modelo sin latencias, sin fallos de enlace y con elección uniforme de pares.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-308
def se308_deteccion() -> Fig:
    items = [("Se revisa en cada commit", 1.00, "teal", "1,00 (p95: 1)"), ("Cada 20 commits", 1.30, "teal", "1,30 (p95: 2)"),
             ("Cada 100 commits", 2.50, "gold", "2,50 (p95: 5)"), ("Solo al final (400 commits)", 7.05, "coral", "7,05 (p95: 14)")]
    return bars("Puntos de uso de una dependencia indebida que hay que corregir según cuándo se detecta",
                "Barras: una dependencia indebida que entra en el commit t y atrae un uso nuevo con probabilidad 3 por ciento por commit deja 1,00 punto de uso por corregir si se detecta en el mismo commit, 1,30 si se revisa cada 20, 2,50 cada 100 y 7,05 si solo se revisa al final.",
                items, 60, "Cada commit sin detección es una oportunidad de que alguien se apoye en la violación: el coste de corregir crece con el tiempo hasta detectar. La tasa del 3 % es un supuesto; con otra tasa cambian las cifras, no la forma. Una función de aptitud que falla en el commit que introduce el problema hace la corrección tan barata como puede ser.",
                label_w=290, width=980, note_kind="teal", foot=SINT)


def se308_ruido() -> Fig:
    return scatter(
        "Prueba de rendimiento con umbral sobre el percentil 95: falsas alarmas y regresiones de +20 % no detectadas",
        "Dispersión con las falsas alarmas en el eje horizontal y las regresiones de 20 por ciento no detectadas en el vertical, un punto por muestras y margen del umbral: con 30 muestras y margen 1,10 hay 24,7 y 21,6 por ciento; con 500 muestras y 1,10 casi nada, 0,3 y 0,5; los márgenes 1,25 y 1,50 reducen las falsas alarmas pero dejan pasar del 61 al 94 por ciento de las regresiones con 30 muestras y 87,5 con 500.",
        [("30 muestras", [(24.7, 21.6, "×1,10", "r"), (6.5, 61.0, "×1,25", "r"), (0.4, 94.5, "×1,50", "r")], "coral"),
         ("100 muestras", [(11.1, 10.1, "×1,10", "r"), (0.2, 69.3, "×1,25", "r")], "gold"),
         ("500 muestras", [(0.3, 0.5, "×1,10", "r"), (0.0, 87.5, "×1,25", "r")], "teal")],
        x_label="Falsas alarmas (% de ejecuciones sin regresión)", y_label="Regresión de +20 % no detectada (%)", y_zero=True,
        y_ticks=[0, 20, 40, 60, 80, 100],
        note="El umbral y el número de muestras son una decisión estadística: con pocas muestras no existe un umbral que dé a la vez pocas falsas alarmas y pocas regresiones perdidas; con muchas sí, a costa de tiempo de ejecución. Una prueba que falla al azar se ignora, y una función de aptitud ignorada ha dejado de existir. 2000 ejecuciones por celda, latencias lognormales sintéticas.",
        note_kind="gold", foot=SINT)


def se308_tendencia() -> Fig:
    return grouped_bars(
        "Tres alarmas sobre una deriva de acoplamiento (926 series de 80 semanas con daño real sobre 26)",
        "Barras horizontales agrupadas con tres resultados de cada alarma en porcentaje de series: el umbral absoluto de 30 avisa antes del daño en 0 por ciento, no avisa nunca en 18 y no da falsas alarmas; el trinquete avisa antes en 99 por ciento con 24,4 de falsas alarmas; la pendiente avisa antes en 95 por ciento con 95,4 de falsas alarmas.",
        ["Umbral absoluto de 30", "Trinquete: +2 sobre el mejor valor", "Pendiente > 0,1 por semana en 8 semanas"],
        [("Avisa antes del daño", [0, 99, 95], "teal"), ("Nunca avisa", [18, 0, 0], "gold"), ("Falsa alarma en series planas", [0, 24.4, 95.4], "coral")],
        unit="Series (%)", horizontal=True, ticks=[0, 25, 50, 75, 100], label_w=260,
        note="Una alarma que llega pronto es una alarma que se equivoca más: el umbral absoluto no da falsas alarmas porque llega tarde; la pendiente de ocho semanas ve tendencias en el ruido. La combinación habitual, un trinquete con tolerancia más una revisión humana de las alarmas, es una decisión sobre qué error cuesta más. Series sintéticas con deriva de 0,05 por semana y ruido de 0,4.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-309
def se309_pesos() -> Fig:
    return grouped_bars(
        "Quién gana la matriz de decisión cuando cambian los pesos o los puntajes",
        "Barras agrupadas con el porcentaje de veces que gana cada alternativa: con 20000 conjuntos de pesos al azar el monolito modular gana 64,5 por ciento, servicios 35,0 y serverless 0,5; con los pesos base y puntajes que varían en uno gana el monolito 80,4 por ciento, servicios 3,7 y serverless 15,9. Con los pesos base exactos el monolito suma 3,95 puntos, servicios 3,30 y serverless 3,45.",
        ["Monolito modular", "Servicios", "Serverless"],
        [("20 000 conjuntos de pesos al azar", [64.5, 35.0, 0.5], "teal"), ("Pesos base, puntajes con ±1 en la mitad de los casos", [80.4, 3.7, 15.9], "gold")],
        unit="Veces que gana la alternativa (%)", ticks=[0, 20, 40, 60, 80, 100],
        note="El ganador de los pesos base lleva 0,5 puntos de ventaja sobre 3,95, pero con pesos al azar pierde una de cada tres veces frente a servicios. Una matriz no decide: muestra qué supuestos hay que defender. Los puntajes son juicios del autor, no mediciones; sirven para ver sensibilidad, no para elegir una arquitectura real.",
        note_kind="gold", foot=SINT)


def se309_adr() -> Fig:
    return stacked_bars(
        "Un comprobador de ADR frente a 12 ADR válidos con un defecto cada uno",
        "Barras horizontales apiladas con los defectos detectados y no detectados según su tipo: las cuatro variantes de forma, falta de sección, estado inventado, fecha mal escrita o una sola alternativa, se detectan en 48 de 48 casos; las cuatro de sentido, alternativas vacías, consecuencias solo positivas, decisión que no responde al contexto o reversibilidad sin condición, en 0 de 48; los doce ADR válidos pasan sin falsos positivos.",
        ["Defectos de forma (4 variantes × 12 ADR)", "Defectos de sentido (4 variantes × 12 ADR)"],
        [("Detectados", [48, 0], "teal"), ("No detectados", [0, 48], "coral")],
        unit="Casos (defecto × ADR)", horizontal=True, label_w=250,
        note="El comprobador exige secciones, estado válido, fecha ISO y al menos dos alternativas: eso evita ADR incompletos, no malos. Las cuatro variantes que pasan cumplen la forma y vacían el contenido; eso lo ve una persona leyendo. Un ADR aceptado por el comprobador sigue necesitando revisión humana del sentido.",
        note_kind="coral", foot=SINT)


def se309_espera() -> Fig:
    return line_chart(
        "Coste esperado (semanas-equipo) de decidir tras esperar, según lo caro que sea revertir",
        "Líneas con el coste esperado total según las semanas de espera antes de decidir: si revertir cuesta 5 o 30 semanas-equipo el coste mínimo está en decidir ya, 2,0 y 12,0; si cuesta 100 el coste baja de 40,2 al decidir ya a 25,0 tras esperar 20 semanas y vuelve a subir a 35,0 con 30.",
        [("Revertir cuesta 5", [(0, 2.0, "2,0", "t"), (4, 5.7), (8, 9.4), (12, 13.0), (20, 20.3), (30, 30.3)], "teal"),
         ("Revertir cuesta 30", [(0, 12.0, "12,0", "t"), (4, 14.3), (8, 16.2), (12, 17.9), (20, 21.5), (30, 31.5)], "gold"),
         ("Revertir cuesta 100", [(0, 40.2, "40,2", "t"), (4, 38.2), (8, 35.2), (12, 31.8), (20, 25.0, "25,0 (mínimo)", "t"), (30, 35.0, "35,0", "t")], "coral")],
        x_label="Semanas de espera antes de decidir", y_label="Coste esperado (semanas-equipo)", point_labels="none",
        x_ticks=[(0, "0"), (4, "4"), (8, "8"), (12, "12"), (20, "20"), (30, "30")], y_ticks=[0, 10, 20, 30, 40, 50],
        note="La espera tiene un coste lineal de 1 por semana y la evidencia pasa de acertar el 60 % a acertar el 95 % tras un tiempo desconocido (2 a 20 semanas). Esperar solo compensa cuando equivocarse es caro y la evidencia mejora de verdad. Es un modelo de juguete con supuestos del autor: sirve para pensar la reversibilidad, no para fijar cifras.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-310
def se310_reparto() -> Fig:
    return grouped_bars(
        "Reparto de 24 módulos entre 4 equipos: dependencias y cambios que cruzan equipos (32 dependencias)",
        "Barras horizontales agrupadas con el porcentaje de dependencias y de cambios que cruzan equipos según el reparto: por comunidades de afinidad cruzan el 12 por ciento de las dependencias y el 16,3 de los cambios; con un equipo grande, 38 y 40,0; al azar, 81 y 66,8; por capa técnica, 91 y 72,5.",
        ["Por comunidad (afinidad real)", "Un equipo grande y tres pequeños", "Al azar", "Por capa técnica"],
        [("Dependencias que cruzan equipos (de 32)", [12, 38, 81, 91], "gold"), ("Cambios que cruzan equipos", [16.3, 40.0, 66.8, 72.5], "coral")],
        unit="Proporción (%)", horizontal=True, ticks=[0, 20, 40, 60, 80, 100], label_w=240,
        note="Los equipos por capa técnica son cómodos para especialistas y obligan a que casi todo cambio de negocio cruce equipos. El reparto por comunidad ahorra coordinación solo si las comunidades existen en el grafo de dependencias; el grafo y las probabilidades de arista son sintéticos. Los canales de comunicación crecen como n(n−1)/2: 28 con 8 personas, 190 con 20.",
        note_kind="teal", foot=SINT)


def se310_huerfanos() -> Fig:
    return line_chart(
        "Módulos sin nadie que los conozca según cuántas personas los conocen y cuántas se van (escala logarítmica)",
        "Líneas en escala logarítmica con el porcentaje de módulos que quedan sin conocimiento según la fracción del equipo que se va: con una persona por módulo 5,04, 14,94 y 29,99 por ciento al irse el 5, el 15 y el 30; con dos personas 0,24, 2,13 y 8,83; con tres 0,01, 0,32 y 2,69; cada persona más baja el riesgo en un factor entre seis y siete.",
        [("Una persona por módulo", [(5, 5.04), (15, 14.94), (30, 29.99)], "coral"),
         ("Dos personas por módulo", [(5, 0.24), (15, 2.13), (30, 8.83)], "gold"),
         ("Tres personas por módulo", [(5, 0.01), (15, 0.32), (30, 2.69)], "teal")],
        x_label="Personas que se van del equipo (%)", y_label="Módulos sin conocimiento (%)", log_y=True,
        x_ticks=[(5, "5 %"), (15, "15 %"), (30, "30 %")], y_ticks=[0.01, 0.1, 1, 10, 100],
        note="Pasar de una a dos personas por módulo reduce el riesgo unas siete veces (14,94 % → 2,13 %); pasar de dos a tres, algo más de seis. El resultado es q^k con salidas independientes; las salidas reales se correlacionan (reorganizaciones, un mismo proyecto). Además, con un propietario principal por módulo, 5 de 15 personas concentran la mitad de los 60 módulos.",
        note_kind="gold", foot=SINT)


def se310_colas() -> Fig:
    return line_chart(
        "Días de entrega de un cambio según los equipos por los que pasa y su ocupación",
        "Líneas con los días de entrega según el número de equipos por los que pasa un cambio: con ocupación del 50 por ciento la mediana sube de 1,4 días con un equipo a 9,3 con cinco; con 70, de 2,3 a 15,4; con 90, de 6,5 a 42,8, y su percentil 90 llega a 71,4; la espera crece más rápido cuanto mayor es la ocupación.",
        [("Ocupación 50 %, mediana", [(1, 1.4), (2, 3.4), (3, 5.3), (5, 9.3, "9,3", "b")], "teal"),
         ("Ocupación 70 %, mediana", [(1, 2.3), (2, 5.6), (3, 8.9), (5, 15.4, "15,4", "t")], "gold"),
         ("Ocupación 90 %, mediana", [(1, 6.5), (2, 15.8), (3, 24.9), (5, 42.8, "42,8", "t")], "coral"),
         ("Ocupación 90 %, percentil 90", [(1, 18.9), (2, 34.1), (3, 47.3), (5, 71.4, "71,4", "t")], "navy")],
        x_label="Equipos por los que pasa el cambio", y_label="Días de entrega", point_labels="none",
        x_ticks=[(1, "1"), (2, "2"), (3, "3"), (5, "5")], y_ticks=[0, 20, 40, 60, 80],
        note="Cada traspaso añade una cola y la espera crece más que linealmente con la ocupación. El trabajo (servicio medio de un día) es el mismo en todas las celdas: lo que cambia es cuánto espera. Colas M/M/1 en serie con llegadas de Poisson, un modelo ideal; los equipos reales tienen trabajo en paralelo, prioridades y vacaciones.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-311
def se311_revision() -> Fig:
    return stacked_bars(
        "Revisión ejecutable de la arquitectura en servicios contra 12 escenarios (supuestos del autor)",
        "Barras horizontales apiladas con los escenarios que cumple y los que falla el modelo de la arquitectura en servicios según su categoría: latencia 2 y 1, disponibilidad 1 y 1, aislamiento 3 y 0, capacidad 0 y 2, cambio 0 y 2; en total seis de doce fallan, y los cuatro de capacidad y cambio fallan todos.",
        ["Latencia (E01 – E03)", "Disponibilidad (E04 – E05)", "Aislamiento (E06 – E08)", "Capacidad (E09 – E10)", "Cambio (E11 – E12)"],
        [("Cumple", [2, 1, 3, 0, 0], "teal"), ("Falla", [1, 1, 0, 2, 2], "coral")],
        unit="Escenarios", horizontal=True, label_w=220,
        note="Seis de doce escenarios fallan y cuatro de ellos por la misma pieza: el almacenamiento de archivos y su revisión limitan el pico. Los números salen de un modelo con latencias p95 sumadas, disponibilidades por componente y capacidades supuestas; sirve para encontrar dónde mirar, no para predecir el comportamiento de un sistema real.",
        note_kind="coral", foot=SINT)


def se311_revisores() -> Fig:
    return line_chart(
        "Probabilidad de que la revisión cubra las tres categorías débiles según quién revisa (5 escenarios por persona, 30 candidatos)",
        "Líneas con la probabilidad de cubrir las tres categorías débiles, capacidad, disponibilidad y cambio, según cuántas personas revisan: con la misma especialidad sube de 2,0 por ciento con una persona a 61,5 con cinco; con especialidades distintas, de 9,4 a 89,4; dos personas con especialidades distintas, 40,3, superan a tres con la misma especialidad, 30,5.",
        [("Todas con la misma especialidad", [(1, 2.0, "2,0", "l"), (2, 13.9, "13,9", "b"), (3, 30.5, "30,5", "b"), (5, 61.5, "61,5", "b")], "coral"),
         ("Con especialidades distintas", [(1, 9.4, "9,4", "l"), (2, 40.3, "40,3", "t"), (3, 65.3, "65,3", "t"), (5, 89.4, "89,4", "t")], "teal")],
        x_label="Personas que revisan", y_label="Cobertura de las tres categorías (%)",
        x_ticks=[(0.4, ""), (1, "1"), (2, "2"), (3, "3"), (5, "5")], y_ticks=[0, 20, 40, 60, 80, 100],
        note="Elegir escenarios sin sesgo (5 de 30 al azar) cubre las tres categorías el 12,2 % de las veces, más que una persona sesgada. El valor de varias miradas está en que sus sesgos no coinciden. Pesos de preferencia (×4 por la especialidad), categorías y debilidades son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se311_sensibilidad() -> Fig:
    return stacked_bars(
        "Perturbaciones de un parámetro que invierten algún veredicto (8 de 144 combinaciones)",
        "Barras horizontales apiladas con las perturbaciones, de 36 por parámetro, que invierten algún veredicto: seis de capacidad y dos de instancias del antivirus lo cambian; ninguna de latencia ni de tasa de fallo, de 0,5 a 2 veces, cambia un veredicto.",
        ["Capacidad", "Instancias", "Latencia", "Tasa de fallo"],
        [("Invierten un veredicto", [6, 2, 0, 0], "coral"), ("No cambian ninguno", [30, 34, 36, 36], "teal")],
        unit="Perturbaciones (9 componentes × 4 variaciones por parámetro)", horizontal=True, label_w=130,
        note="Los veredictos son robustos a la latencia y a la tasa de fallo y frágiles a la capacidad. El escenario E04 falla por solo 0,015 puntos de disponibilidad, pero ninguna mejora individual de un componente lo arregla: su causa es la suma de componentes y la causa común. Un margen pequeño no implica sensibilidad a un parámetro concreto.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-312
def se312_validador() -> Fig:
    return stacked_bars(
        "Validador del dossier de arquitectura frente a 200 mutaciones (150 detectadas)",
        "Barras horizontales apiladas con las mutaciones detectadas y no detectadas según su tipo: las seis de estructura, referencias rotas, umbral borrado, vista incompleta o una sola alternativa, se detectan en 150 de 150 casos; las dos de sentido, un umbral de 999999 milisegundos y una función de aptitud que siempre pasa, en 0 de 50.",
        ["Estructura (6 tipos × 25)", "Sentido (2 tipos × 25)"],
        [("Detectadas", [150, 0], "teal"), ("No detectadas", [0, 50], "coral")],
        unit="Mutaciones del dossier", horizontal=True, label_w=190,
        note="El dossier base (4 drivers, 12 escenarios, 4 ADR, 6 funciones de aptitud, 4 vistas) pasa el validador y, aun así, el modelo ejecutable da cuatro fallas (E04, E08, E10, E12): validar la forma no es evaluar la arquitectura. Las mutaciones son del autor; la tasa de 150/200 depende de cuántas sean de sentido.",
        note_kind="coral", foot=SINT)


def se312_mes() -> Fig:
    return scatter(
        "Mil meses simulados de cuatro arquitecturas (4 picos de 60 a 90 rps de 10 minutos por mes)",
        "Dispersión con la capacidad de la ruta de entrega y el porcentaje de meses que alcanzan 99,9 por ciento de disponibilidad: servicios con 50 peticiones por segundo logra 60 por ciento y pasa 40 minutos saturado; el monolito modular con 50 logra 74 y también 40 minutos; con 120 y con 135 desaparece la saturación pero el porcentaje sigue en 74, de modo que añadir capacidad no mejora la disponibilidad.",
        [("Saturan 40 minutos en los picos", [(50, 60, "Servicios · 40 min saturados", "r"), (50, 74, "Monolito modular · 40 min saturados", "r")], "coral"),
         ("No saturan", [(120, 74, "Monolito + archivos asíncronos · 0 min", "b"), (135, 74, "Propuesta final · 0 min", "t")], "teal")],
        x_label="Capacidad de la ruta de entrega (peticiones por segundo)", y_label="Meses con al menos 99,9 % de disponibilidad (%)",
        x_ticks=[(40, "40"), (60, "60"), (80, "80"), (100, "100"), (120, "120"), (140, "140"), (160, "160")], y_ticks=[55, 60, 65, 70, 75, 80],
        note="Añadir instancias elimina la saturación pero no mejora la disponibilidad: lo domina la causa común. Eso obliga a una decisión de negocio escrita en un ADR: aceptar 99,9 % o invertir en aislar la causa común. Caídas con duración exponencial de 20 minutos y 30 % de causa común: supuestos del autor, no datos de un sistema.",
        note_kind="gold", foot=SINT)


def se312_impacto() -> Fig:
    return grouped_bars(
        "Escenarios que dependen de los componentes de cada decisión y los que su ADR no declara",
        "Barras agrupadas con, para cuatro decisiones, los escenarios de doce que dependen de sus componentes, los que su ADR declara y los no declarados: revertir el monolito modular afecta a 10 escenarios y el ADR declara 2, con 9 sin declarar; subir archivos por URL firmada afecta a 8 con 3 declarados; la revisión asíncrona a 7 con 3; las tres instancias a 10 con 4.",
        ["ADR-1 · URL firmada de subida", "ADR-2 · monolito modular", "ADR-3 · revisión asíncrona", "ADR-4 · tres instancias"],
        [("Afectados", [8, 10, 7, 10], "coral"), ("Declarados en el ADR", [3, 2, 3, 4], "teal"), ("Sin declarar", [5, 9, 4, 6], "gold")],
        unit="Escenarios (de 12)", ticks=[0, 2, 4, 6, 8, 10, 12],
        note="El grafo decisión → componente → escenario muestra que los ADR declaran menos dependencias de las reales: una decisión estructural como el monolito modular toca casi todo. Por eso un ADR lista los escenarios que podría romper, y esa lista se regenera desde el modelo en lugar de escribirse de memoria.",
        note_kind="teal", foot=SINT)


FIGURES = {
    "se-307-arranques-en-frio.svg": se307_frio,
    "se-307-equilibrio-de-costo.svg": se307_costo,
    "se-307-difusion-por-rumor.svg": se307_rumor,
    "se-308-cuando-se-detecta-una-violacion.svg": se308_deteccion,
    "se-308-falsas-alarmas-y-regresiones.svg": se308_ruido,
    "se-308-umbral-trinquete-y-tendencia.svg": se308_tendencia,
    "se-309-ganador-segun-pesos.svg": se309_pesos,
    "se-309-comprobador-de-adr.svg": se309_adr,
    "se-309-cuanto-esperar.svg": se309_espera,
    "se-310-reparto-de-modulos.svg": se310_reparto,
    "se-310-modulos-huerfanos.svg": se310_huerfanos,
    "se-310-entrega-con-colas.svg": se310_colas,
    "se-311-revision-ejecutable.svg": se311_revision,
    "se-311-cobertura-de-revisores.svg": se311_revisores,
    "se-311-sensibilidad-de-parametros.svg": se311_sensibilidad,
    "se-312-validador-del-dossier.svg": se312_validador,
    "se-312-un-mes-de-cuatro-arquitecturas.svg": se312_mes,
    "se-312-impacto-de-revertir-una-decision.svg": se312_impacto,
}
