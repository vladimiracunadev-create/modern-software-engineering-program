"""Figures for SE-378 to SE-384 (synthetic data, fixed seeds, virtual time; real probes on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3).

Every figure is a chart or a diagram of the same measured numbers; the Markdown tables of the classes keep the exact values.
"""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, heatmap, line_chart, stacked_bars, timeline

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Sondas reales en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); cada fila es una observación, no una norma."


# ---------------------------------------------------------------- SE-378

def se378_tormenta() -> Fig:
    return heatmap(
        "Trabajo del servidor hecho para clientes que ya se fueron, tras un brownout de 10 s y tras una oleada de 400 clientes",
        "Mapa de calor con el porcentaje de trabajo inútil por política: en el brownout sube de 15 por ciento sin reintentos a 94 con reintento inmediato, exponencial o jitter completo, y un presupuesto del 10 por ciento lo deja en 19; en la oleada sincronizada va de 0 a 2, 1 y 67 por ciento con jitter; las celdas con borde son las que colapsan en las diez semillas.",
        ["Brownout de 10 s", "Oleada de 400 clientes"],
        ["Sin reintentos", "Reintento inmediato", "Retardo exponencial", "Exponencial con jitter completo", "Jitter y presupuesto del 10 %"],
        [[15, 94, 94, 94, 19], [0, 2, 1, 67, None]],
        unit="% del trabajo del servidor que es inútil", scale="coral", vmin=0, vmax=100, suffix=" %", label_w=170,
        highlight=[(0, 1), (0, 2), (0, 3), (1, 3)],
        note="Tres políticas de espera distintas dan el mismo colapso en el brownout (10 de 10 semillas, pico de 70 a unos 234 req/s, 3,38 intentos por solicitud) porque el problema es la cantidad de trabajo, no su sincronización; lo evita el presupuesto. En la oleada el jitter aplana el pico de 332 a 143 reintentos por 100 ms pero reparte los reintentos de modo que muchos terminan justo después del timeout. Es un resultado de este modelo (el servidor solo descarta tras 1 s de espera), no una regla general.",
        note_kind="coral", foot=SINT)


def se378_capas() -> Fig:
    pct = [0, 10, 50, 100]
    return line_chart(
        "Tres capas encadenadas con hasta tres intentos cada una: intentos que llegan a la base de datos por solicitud",
        "Líneas con los intentos que llegan a la base de datos por solicitud del usuario según el porcentaje de fallo de la base: con la base caída, reintentar en las tres capas envía 27 intentos, solo el borde 3, el presupuesto del 10 por ciento 1,37 y sin reintentos 1; con fallos independientes del 10 por ciento todas las políticas con reintentos envían 1,11.",
        [("Sin reintentos", list(zip(pct[:3], [1.0, 1.0, 1.0])) + [(100, 1.0, "1", "r")], "grey"),
         ("Solo el borde", list(zip(pct[:3], [1.0, 1.11, 1.75])) + [(100, 3.0, "3", "r")], "gold"),
         ("Las tres capas", list(zip(pct[:3], [1.0, 1.11, 2.01])) + [(100, 27.0, "27", "r")], "coral"),
         ("Presupuesto del 10 %", list(zip(pct[:3], [1.0, 1.11, 1.37])) + [(100, 1.37, "1,37", "r")], "teal")],
        x_label="Fallo de la base de datos (%)", y_label="Intentos a la base por solicitud", log_y=True,
        x_ticks=[(0, "0"), (10, "10"), (50, "50"), (100, "100 (caída)"), (112, "")], y_ticks=[1, 3, 10, 30],
        point_labels="none", plot_h=300,
        note="Los reintentos son un buen remedio para fallos independientes y transitorios (10 %: de 90 % a 100 % de éxito con 1,11 intentos) y una trampa cuando la base está caída: la amplificación es 3 × 3 × 3. Con un 50 % de fallos las tres capas llegan al 100 % de éxito con 2,01 intentos y el presupuesto del 10 % queda en 69 %: limita el daño y lo paga con éxito.",
        note_kind="gold", foot=SINT)


def se378_timeout() -> Fig:
    pts = [(200, 3.96, "100 ms", "t"), (310, 1.88, "200 ms", "t"), (594, 1.77, "500 ms", "t"), (1088, 1.67, "1 s", "t"),
           (3060, 1.17, "3 s", "t"), (3976, 0.46, "10 s", "t")]
    return line_chart(
        "Timeout por intento y un reintento: la carga inútil frente a la cola de latencia (97 % de peticiones de ~80 ms)",
        "Línea con el trabajo inútil por trabajo útil según el percentil 99 de la latencia, con cada punto rotulado por su timeout: con 100 milisegundos el p99 es 200 y el servidor hace 3,96 veces más trabajo inútil que útil; con 1 segundo, 1 088 y 1,67; con 10 segundos el p99 llega a 3 976 y el cociente baja a 0,46.",
        [("Un reintento por timeout", pts, "navy")],
        x_label="Latencia p99 (ms)", y_label="Trabajo tras el abandono por trabajo útil", log_x=True,
        x_ticks=[(200, "200"), (500, "500"), (1000, "1 000"), (2000, "2 000"), (4000, "4 000")], y_ticks=[0, 1, 2, 3, 4],
        point_labels="none", decimals=2, plot_h=290,
        note="No existe un timeout correcto en abstracto: uno demasiado corto crea carga (3,96) y uno demasiado largo retiene recursos y alarga la cola (p99 de 3 976 ms). El éxito con un reintento sube de 90,36 % con 100 ms a 99,83 % con 200 ms y 100 % con 10 s. El cociente baja con timeouts largos porque lo inútil se limita a 30 s en el modelo. Un plazo para varias llamadas en serie debe repartirse: tres de 1 s con un reintento suman hasta 6 s.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-379
def se379_interruptor() -> Fig:
    return grouped_bars(
        "Una dependencia que se cuelga 60 s a 100 req/s: llamadas que llegan a ella y solicitudes rechazadas según el interruptor",
        "Barras agrupadas en escala logarítmica con las llamadas a la dependencia caída y las solicitudes rechazadas por pool agotado: sin interruptor 4 430 y 1 637; con un interruptor de cinco fallos seguidos o del 50 por ciento de 20 llamadas, entre 152 y 165 llamadas y 59 rechazos con cualquier tiempo de apertura.",
        ["Sin interruptor", "5 fallos seguidos, abierto 2 s", "5 fallos seguidos, abierto 10 s", "5 fallos seguidos, abierto 30 s", "50 % de 20 llamadas, abierto 10 s"],
        [("Llamadas a la dependencia", [4430, 165, 155, 152, 160], "coral"), ("Rechazadas por pool agotado", [1637, 59, 59, 59, 59], "gold")],
        unit="Solicitudes", log=True, ticks=[10, 100, 1000, 10000], plot_h=280,
        note="Abrir cuesta 59 rechazos igualmente: detectar cinco fallos de 2 s lleva 2 s y en ese tiempo entran 200 solicitudes a un pool de 150. El p99 del usuario baja de 2 000 a 50 ms. Abierto más tiempo protege más y tarda más en volver: la recuperación media va de 2,2 s con 2 s de apertura a 11,6 s con 30 s (máximo 31,8 s).",
        note_kind="gold", foot=SINT)


def se379_mamparos() -> Fig:
    return grouped_bars(
        "Dos dependencias (A: 80 req/s de 50 ms; B: 20 req/s) y 20 trabajadores: solicitudes atendidas según el reparto",
        "Barras agrupadas con el porcentaje de solicitudes atendidas de A y de B con B sana y con B lenta: con un pool compartido de 20, B lenta arrastra a A a 74,3 por ciento; con pools separados A queda en 100 por ciento y B atiende 23,1 por ciento con 15 y 5, 45,0 con 10 y 10 y 9,3 con 18 y 2.",
        ["Un pool compartido de 20", "A 15 y B 5", "A 10 y B 10", "A 18 y B 2"],
        [("A con B sana", [100.0, 100.0, 99.5, 100.0], "teal"), ("B con B sana", [100.0, 99.6, 100.0, 79.6], "grey"),
         ("A con B lenta", [74.3, 100.0, 99.6, 100.0], "navy"), ("B con B lenta", [73.6, 23.1, 45.0, 9.3], "coral")],
        unit="Solicitudes atendidas (%)", decimals=1, ticks=[0, 25, 50, 75, 100], plot_h=270,
        note="El mamparo no arregla B: lo confina. Cuesta capacidad ociosa (con B sana, 18 + 2 rechaza el 20 % de B) y exige dimensionar cada compartimento. A 10 y B 10 protege a A y deja a B en 45 %, y no existe un reparto que dé lo mejor a ambos.",
        note_kind="teal", foot=SINT)


def se379_degradar() -> Fig:
    return grouped_bars(
        "Sobrecarga de 2 × (160 req/s sobre 80 de capacidad, 20 % críticas) durante 60 s: respuestas útiles dentro de 2 s",
        "Barras agrupadas con el porcentaje de solicitudes críticas y no críticas atendidas a tiempo por política: sin control 3,0 y 3,7 por ciento; con cola acotada a 50, 53,9 y 52,3; con prioridad a las críticas, 100 y 40,3; con prioridad y respuesta degradada, 100 y 100 por ciento.",
        ["Sin control", "Cola acotada a 50", "Prioridad a las críticas", "Prioridad y respuesta degradada"],
        [("Críticas a tiempo", [3.0, 53.9, 100.0, 100.0], "teal"), ("No críticas a tiempo", [3.7, 52.3, 40.3, 100.0], "gold")],
        unit="Solicitudes a tiempo (%)", decimals=1, ticks=[0, 25, 50, 75, 100], plot_h=260,
        note="La degradación bajo control es una decisión de producto: qué es crítico y qué respuesta barata sigue siendo útil. Las respuestas útiles por segundo pasan de 5,6 sin control a 82,0, 81,6 y 155,9. El 155,9 supone que la respuesta degradada cuesta 5 ms en lugar de 50 ms (supuesto del autor): si degradar costara lo mismo, no habría ganancia.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-380
def se380_disponibilidad() -> Fig:
    return grouped_bars(
        "Disponibilidad simulada durante 400 años: minutos de caída al año según la arquitectura y la causa común de fallo",
        "Barras horizontales con los minutos de caída al año: un componente 529, tres componentes en serie 1 574, dos réplicas de la aplicación 1 044 y dos réplicas con cuatro despliegues malos al año 1 282; la réplica mejora de 99,70 a 99,80 por ciento de disponibilidad y la causa común la baja a 99,756.",
        ["Un componente (MTBF 500 h, MTTR 0,5 h)", "Serie: web, aplicación y base de datos", "Dos réplicas independientes de la aplicación", "Dos réplicas y 4 despliegues malos al año de 1 h"],
        [("Minutos de caída al año", [529, 1574, 1044, 1282], "navy")],
        unit="Minutos de caída al año", horizontal=True, label_w=300, ticks=[0, 500, 1000, 1500, 2000],
        note="La réplica de una capa mejora el 99,70 % a un 99,80 % y nada más: los otros dos tramos en serie mandan. La causa común es la que quita el beneficio: la aplicación con dos réplicas pasa de 0,9999996 a 0,99955. Los MTBF y MTTR son supuestos del autor y las caídas independientes son un modelo, no una medición.",
        note_kind="gold", foot=SINT)


def se380_durabilidad() -> Fig:
    k = 1e10  # eje en pérdidas por cada 10 000 millones de objetos al año; los rótulos vuelven a la probabilidad

    def sci(v: float) -> str:
        return f"{v / k:.2e}".replace(".", ",")
    return grouped_bars(
        "Probabilidad anual de perder un objeto con réplicas independientes según el tiempo de reparación",
        "Barras horizontales en escala logarítmica con la aproximación analítica de la pérdida anual con tasa de fallo de disco del 20 y del 2 por ciento: con dos réplicas va de 9,13e-06 con 1 hora de reparación a 1,53e-03 con 168, y con tres réplicas y 168 horas baja a 8,83e-06; con tasa del 2 por ciento, tres réplicas y 24 horas dan 1,80e-10.",
        ["2 réplicas, reparación de 1 h", "2 réplicas, reparación de 24 h", "2 réplicas, reparación de 168 h", "3 réplicas, reparación de 168 h", "3 réplicas, reparación de 336 h", "3 réplicas, reparación de 24 h"],
        [("Aproximación con tasa anual del 20 %", [v * k for v in (9.13e-06, 2.19e-04, 1.53e-03, 8.83e-06, 3.53e-05, 1.80e-07)], "coral"),
         ("Aproximación con tasa anual del 2 %", [v * k for v in (9.13e-08, 2.19e-06, 1.53e-05, 8.83e-09, 3.53e-08, 1.80e-10)], "teal")],
        unit="Pérdidas por cada 10 000 millones de objetos al año (rótulos: probabilidad anual)", horizontal=True, log=True, label_w=250, value_fmt=sci,
        ticks=[1, 100, 10000, 1000000, 100000000],
        note="La aproximación 8 760 · N · λᴺ · Rᴺ⁻¹ coincide con la simulación (por ejemplo 2,35e-04 simulada frente a 2,19e-04 con 2 réplicas y 24 h) y enseña que la reparación pesa más que el número: 7 veces más tiempo, 7ᴺ⁻¹ más pérdida. Pero si el 0,1 % de los fallos afecta a las tres réplicas a la vez (mismo lote, misma sala, mismo error), la pérdida anual es 2,0e-05, cinco órdenes mayor que la independiente (1,8e-10).",
        note_kind="coral", foot=SINT)


def se380_deteccion() -> Fig:
    umbral = [1.5, 2, 3, 5, 10]
    return line_chart(
        "Detector de fallos por latidos de 1 s con pérdida del 0,5 % y pausas del emisor: el umbral y sus dos costos anuales",
        "Líneas en escala logarítmica con los minutos al año por detectar tarde cuatro caídas reales y por conmutar sin motivo según el umbral: detectar tarde sube de 0,07 minutos con 1,5 segundos a 1,97 con 30, mientras que conmutar sin motivo baja de 79 491 minutos con 1,5 segundos a 43 con 10 y 0 con 30.",
        [("Por detectar tarde (4 caídas al año)", list(zip(umbral + [30], [0.07, 0.10, 0.17, 0.30, 0.63, 1.97])), "gold"),
         ("Por conmutar sin motivo (30 s cada una)", list(zip(umbral, [79491, 39968, 694, 195, 43])), "coral")],
        x_label="Umbral del detector (s)", y_label="Minutos por año", log_x=True, log_y=True,
        x_ticks=[(1.5, "1,5"), (2, "2"), (3, "3"), (5, "5"), (10, "10"), (30, "30")], y_ticks=[0.01, 0.1, 1, 10, 100, 1000, 10000, 100000],
        point_labels="all", plot_h=300,
        note="El umbral intercambia un tipo de pérdida por otro: 30 s cuestan 2 minutos al año en detección tardía y 0 en conmutaciones falsas (no se dibuja: no cabe en escala logarítmica); 2 s cuestan 0,1 minutos y casi 40 000 en falsas (unas 219 conmutaciones falsas por día frente a 0). Las pausas del emisor (una cada 5 horas, mediana de 2 s) y la pérdida del 0,5 % son supuestos del autor.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-381
def se381_sondas() -> Fig:
    return grouped_bars(
        "Doce sondas de portabilidad ejecutadas con el mismo script de Python en Windows 11 y en Ubuntu bajo WSL2",
        "Barras horizontales con el número de sondas por área en las que Windows y Ubuntu dan un resultado distinto: texto y bytes 3, nombres y rutas 3, operaciones sobre archivos 2, funciones de la plataforma 3 y procesos 1; en las doce sondas los resultados difieren.",
        ["Texto y bytes (separador y fin de línea, codificación por defecto, bytes de un texto con eñe)", "Nombres y rutas (mayúsculas, carácter «:», rutas anidadas largas)",
         "Operaciones sobre archivos (renombrar sobre uno existente, borrar uno abierto)", "Funciones de la plataforma (fecha anterior a 1970, «%-d», os.getuid)", "Procesos (método de arranque de multiprocessing)"],
        [("Sondas con resultado distinto", [3, 3, 2, 3, 1], "coral")],
        unit="Sondas con resultado distinto (de 12 en total)", horizontal=True, label_w=440, ticks=[0, 1, 2, 3, 4],
        note="Las doce sondas difieren y ninguna es exótica. El texto «año» escrito sin encoding ocupa 5 bytes con salto de línea en ambos sistemas y los bytes son distintos: el tamaño no delata la diferencia. La ruta de Windows falla por el límite de 260 caracteres con la configuración de este equipo (en el cuarto nivel, 252 caracteres, frente a 8 niveles y 428 caracteres en Ubuntu); con rutas largas habilitadas no fallaría.",
        note_kind="coral", foot=REAL)


def se381_interop() -> Fig:
    return grouped_bars(
        "Datos que cambian de significado al cruzar una frontera: porcentaje de casos que cambian en cada medida",
        "Barras horizontales con el porcentaje de casos que cambian al cruzar cada frontera: los identificadores de 53 bits o menos 0 por ciento, los de 54 bits 49,9, los de 63 bits 99,9, dos fuentes con el mismo nombre en NFC y NFD 51,3, los precios al multiplicar por cien 4,6 y las fechas de 2026 que se leen distinto como día-mes o mes-día 36,2.",
        ["Identificadores de 40 y 53 bits a decimal de 64 bits", "Identificadores de 54 bits", "Identificadores de 63 bits",
         "«José» en NFC y NFD de dos fuentes (1 026 de 2 000 pares)", "Precios de 1 a 99 999 centavos con int(precio · 100)", "Fechas de 2026 que dd/mm y mm/dd leen distinto (132 de 365)"],
        [("Casos que cambian", [0, 49.9, 99.9, 51.3, 4.6, 36.2], "coral")],
        unit="Casos que cambian (%)", horizontal=True, label_w=330, ticks=[0, 25, 50, 75, 100],
        note="Ninguno de estos fallos lanza una excepción: el dato llega y es otro. Un contrato de interoperabilidad debe fijar la representación (cadena para identificadores de más de 53 bits, normalización Unicode, enteros en centavos o decimales, fechas ISO 8601 con zona) y probar con valores en los bordes. Con NFC las 1 026 diferencias pasan a 0.",
        note_kind="gold", foot=SINT)


def se381_matriz() -> Fig:
    return grouped_bars(
        "Mensajes de la versión 1 a la 5 leídos por lectores de la versión 1 a la 5: lectores compatibles con cada productor",
        "Barras agrupadas con los lectores de las cinco versiones que aceptan el mensaje de cada productor, con lector estricto y con lector tolerante: la versión 1 la leen 2 con ambos, la 2 solo 1 con el estricto y 2 con el tolerante, la 3 solo 1 con ambos, la 4 la leen 2 con ambos y la 5, 1 con el estricto y 2 con el tolerante; son 7 de 25 pares con el estricto y 9 con el tolerante.",
        ["v1: id, estudiante, nota", "v2: añade comentario opcional", "v3: renombra estudiante a alumno", "v4: la nota pasa de número a texto", "v5: añade el campo estado"],
        [("Lector estricto (7 de 25 pares)", [2, 1, 1, 2, 1], "coral"), ("Lector tolerante (9 de 25 pares)", [2, 2, 1, 2, 2], "teal")],
        unit="Versiones de lector que aceptan el mensaje (de 5)", ticks=[0, 1, 2, 3, 4, 5], plot_h=250,
        note="El lector tolerante gana 2 de 25 pares: los cambios aditivos (v2 y v5). Renombrar (v3) y cambiar el tipo (v4) rompen en ambos sentidos y exigen expandir y contraer. La matriz se construye ejecutando los lectores, no leyendo la especificación. Es un modelo de cinco versiones, no un esquema real.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-382
def se382_campo() -> Fig:
    return grouped_bars(
        "La misma página (440 KB) vista desde el laboratorio y desde tres segmentos de dispositivos: percentil 75 de la carga",
        "Barras horizontales con el percentil 75 del tiempo de carga frente al límite de 2,5 segundos: el laboratorio con un escritorio rápido da 0,49, el escritorio rápido 0,49, el teléfono medio 1,69 y el teléfono lento 4,93; la población completa da 1,50 y supera el límite en el 10,2 por ciento de las cargas, mientras que el teléfono lento lo supera en el 98 por ciento.",
        ["Laboratorio: solo escritorio rápido", "Escritorio rápido (55 % de la población)", "Teléfono medio (35 %)", "Teléfono lento (10 %)", "Campo: la población completa"],
        [("p75", [0.49, 0.49, 1.69, 4.93, 1.50], "navy")],
        unit="Tiempo de carga p75 (s)", horizontal=True, label_w=300, decimals=2, ref_lines=[(2.5, "Límite 2,5 s")], ticks=[0, 1, 2, 3, 4, 5],
        note="El p75 de la población (1,50 s) cumple y deja fuera a quienes más lo necesitan: el 10 % con teléfono lento queda en 4,93 s. Para esa persona la página necesitaría 110 KB, o menos CPU, para llegar a 2,5 s. Los segmentos, los porcentajes y el modelo de tiempo son supuestos del autor; no se midió ningún navegador ni dispositivo.",
        note_kind="coral", foot=SINT)


def se382_deriva() -> Fig:
    return timeline(
        "Una deriva de peso del 0,6 % por compilación (de 800 KB a 1 324 KB en 80) frente a tres compuertas",
        "Línea de tiempo por compilación con el momento en que cada compuerta avisa: el presupuesto absoluto de 1 000 kilobytes avisa en la compilación 38 con un 25 por ciento de aumento; la tendencia, en la 26 con 926 kilobytes y un 16 por ciento; la compuerta contra la compilación anterior falla 21 veces en 79 por ruido y ninguna por la deriva real.",
        [("Presupuesto absoluto de 1 000 KB", [(0, 38, "Sin aviso", "grey"), (38, 80, "Avisa desde la 38 (+25 %)", "coral")]),
         ("Tendencia: mediana de 3 contra las 10 primeras, +10 %", [(0, 26, "Sin aviso", "grey"), (26, 80, "Avisa desde la 26 (926 KB, +16 %)", "teal")]),
         ("Contra la compilación anterior, +2 %", [(0, 80, "21 de 79 compilaciones fallan por ruido; ninguna por la deriva real", "gold")])],
        unit="Número de compilación", events=[(26, "26"), (38, "38")], t_max=80, ticks=[0, 10, 20, 30, 40, 50, 60, 70, 80], lane_h=58, label_w=260,
        note="Cada compilación solo engorda 0,6 %, por debajo del ruido de 1,2 %, y por eso la compuerta paso a paso no la ve (y se dispara por ruido). La tendencia ve el conjunto sin disparar: 12 compilaciones antes que el presupuesto absoluto, con la ventaja de llegar cuando aún hay margen. Sin deriva, las falsas alarmas son 0 de 80, 15 de 79 y 0 de 70.",
        note_kind="teal", foot=SINT)


def se382_contraste() -> Fig:
    return grouped_bars(
        "Contraste WCAG medido con la fórmula de luminancia sobre los colores del propio repositorio",
        "Barras horizontales con la razón de contraste de siete combinaciones frente a los umbrales de 3 a 1 para componentes gráficos y de 4,5 a 1 para texto: el texto de las figuras (9,91 como mínimo), el pie, el texto atenuado y los enlaces cumplen; el borde dorado, 3,98, cumple 3; la etiqueta superior del portal, 3,51, y el borde gris, 2,90, no cumplen su umbral.",
        ["Borde gris de las figuras (gráfico) sobre blanco", "Etiqueta superior del portal (texto): coral sobre el papel", "Borde dorado de las figuras (gráfico) sobre blanco",
         "Texto atenuado del portal sobre el papel", "Enlaces del portal sobre el papel", "Texto de figura sobre su relleno (el peor de seis tipos)", "Pie de las figuras sobre blanco"],
        [("Razón de contraste", [2.90, 3.51, 3.98, 5.24, 5.60, 9.91, 12.64], "navy")],
        unit="Razón de contraste (a 1)", horizontal=True, label_w=330, decimals=2, ref_lines=[(3, "3:1"), (4.5, "4,5:1")], ticks=[0, 3, 4.5, 6, 9, 12, 15],
        note="Texto pequeño pide 4,5:1 y un componente gráfico 3:1. Los seis tipos de recuadro llegan hasta 16,12:1. La medida es exacta y encuentra algo concreto: una etiqueta del portal por debajo del umbral. No prueba que la experiencia sea accesible: ninguna fórmula de contraste ve el orden de lectura, el foco ni el texto alternativo. En las figuras el borde nunca es la única señal, porque cada recuadro lleva texto.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-383
def se383_umbral() -> Fig:
    return grouped_bars(
        "Umbral de la hipótesis de estado estable (p95 por ventana de 10 s): falsas alarmas y detección de un aumento de 10 ms",
        "Barras agrupadas con las ejecuciones sanas que alarman y las que detectan un aumento de 10 milisegundos por umbral: el máximo de una ejecución base de 73 milisegundos alarma en 46 de 100 y detecta 100 de 100; multiplicarlo por 1,5 da 0 falsas alarmas y detecta 41; el p99,9 de 30 ejecuciones por 1,2 da 0 y detecta 92.",
        ["Máximo de la base (5 min) = 73 ms", "Ese máximo × 1,5 = 110 ms", "p99,9 de 30 ejecuciones base × 1,2 = 94 ms"],
        [("Ejecuciones sanas con alarma", [46, 0, 0], "coral"), ("Detecta +10 ms", [100, 41, 92], "teal")],
        unit="Ejecuciones de 100", ticks=[0, 25, 50, 75, 100], plot_h=250,
        note="Un solo experimento de base fija un umbral demasiado ajustado o demasiado holgado sin que se note. Con 30 ejecuciones base se conoce la forma del ruido y el umbral deja de ser una conjetura. El aumento de 10 ms sobre 50 ms de servicio (al 75 % de utilización) es un fallo sutil escogido por el autor. Ventanas falsas: 2,00 % con el primer umbral y 0,00 % con los otros dos.",
        note_kind="gold", foot=SINT)


def se383_matriz() -> Fig:
    return dumbbell(
        "Cuatro fallos inyectados 30 s en una API con 6 trabajadores y una base de datos: errores de la configuración ingenua y de la endurecida",
        "Puntos unidos con el porcentaje de errores de cada configuración: con 200 milisegundos extra en la base baja de 90,6 a 35,9 por ciento, con 20 por ciento de errores de la base de 19,7 a 0, con la base caída de 100 a 0 y con el tráfico multiplicado por cinco de 82,9 a 27,5; en la caída total responde degradada al 100 por ciento.",
        [("+200 ms en la base de datos", 90.6, 35.9), ("20 % de errores de la base", 19.7, 0.0), ("Caída total de la base", 100.0, 0.0), ("Tráfico × 5", 82.9, 27.5)],
        unit="Solicitudes con error (%)", names=("Configuración ingenua", "Configuración endurecida"), decimals=1,
        delta=lambda a, b: "100 % degradadas" if (a, b) == (100.0, 0.0) else "19,7 % degradadas" if (a, b) == (19.7, 0.0) else "",
        label_w=230,
        note="Endurecer cambia el tipo de fallo: de errores a respuestas degradadas, que son una decisión de producto. No sustituye a la capacidad: con +200 ms o con ×5 siguen los errores (35,9 % y 27,5 %) porque el sistema necesita más trabajadores. Sin fallo ambas dan 0,0 % de errores y p99 de 70 ms. El modelo (6 trabajadores, 40 req/s, base de 30 ms) es una construcción del autor.",
        note_kind="teal", foot=SINT)


def se383_radio() -> Fig:
    return heatmap(
        "Error inyectado frente a fracción del tráfico afectado: probabilidad de detección (60 s a 40 req/s)",
        "Mapa de calor con la probabilidad de detectar el fallo según el error inyectado y la fracción del tráfico afectada: un error del 20 por ciento se detecta el 97 por ciento de las veces con el 1 por ciento del tráfico; uno del 5 por ciento, el 33; uno del 2 por ciento solo el 9, y solo llega a 100 por ciento exponiendo todo el tráfico.",
        ["Error inyectado del 2 %", "Error inyectado del 5 %", "Error inyectado del 20 %"], ["1 % del tráfico", "5 %", "10 %", "100 %"],
        [[9, 43, 70, 100], [33, 94, 100, 100], [97, 100, 100, 100]],
        unit="% de ejecuciones en que se detecta", scale="teal", vmin=0, vmax=100, suffix=" %", label_w=190,
        note="Un fallo fuerte se descubre con un radio de impacto mínimo (5 solicitudes erróneas esperadas con el error del 20 % al 1 %); un fallo sutil exige exponer más usuarios o ejecutar más tiempo (48 solicitudes erróneas con el error del 2 % al 100 %), y eso hay que decidirlo antes. Detección: cola binomial exacta con error base de 0,3 % y nivel 1 %, estimada con 2 000 repeticiones por celda.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-384
def se384_validador() -> Fig:
    detected = ["Quitar un campo obligatorio", "Alterar una fila de los datos", "Alterar un resultado un 10 %", "Invertir el veredicto",
                "Vaciar los límites («n/a»)", "Dejar el entorno incompleto", "Cambiar el umbral sin el plan"]
    missed = ["Cambiar umbral y plan a la vez", "Reemplazar datos, hash y resultados", "Conservar solo la mitad más rápida",
              "Un límite genérico pero extenso", "Borrar lo no medido («nada»)"]
    return stacked_bars(
        "Un validador de paquetes de informe frente a 240 mutaciones (12 operadores × 20): 140 detectadas",
        "Barras apiladas horizontales con las mutaciones detectadas de 20 por cada uno de los doce operadores: los siete que quitan, alteran o contradicen un dato, como quitar un campo, alterar una fila o invertir el veredicto, se detectan 20 de 20; los cinco coherentes, como reemplazar los datos con su hash y sus resultados o cambiar a la vez el umbral y el plan, 0 de 20.",
        detected + missed, [("Detectadas", [20] * 7 + [0] * 5, "teal"), ("No detectadas", [0] * 7 + [20] * 5, "coral")],
        unit="Mutaciones de 20 por operador", horizontal=True, label_w=270,
        note="Detecta 140 de 240 (58 %) y las 100 que se escapan son coherentes: el informe se contradice solo cuando algo se olvidó, no cuando se eligió. El hash prueba que los datos no cambiaron, no que sean los correctos; el plan con hash prueba el orden solo si se registró antes (por ejemplo, en un commit anterior).",
        note_kind="coral", foot=SINT)


def se384_reproducibilidad() -> Fig:
    return stacked_bars(
        "Ocho artefactos del mismo canal: cuántos son idénticos (SHA-256) entre dos ejecuciones y entre Windows y Ubuntu",
        "Barras apiladas horizontales con los ocho artefactos clasificados: entre dos ejecuciones en el mismo sistema 6 son idénticos y 2 cambian por naturaleza, el reloj y el orden de un conjunto; entre Windows y Ubuntu solo 3 son idénticos, 2 difieren por un defecto de escritura corregible, 2 por naturaleza y 1 por diseño.",
        ["Entre dos ejecuciones en el mismo sistema", "Entre Windows y Ubuntu"],
        [("Idénticos", [6, 3], "teal"), ("Difieren por defecto de escritura (modo texto sin newline ni encoding)", [0, 2], "coral"),
         ("Difieren por naturaleza (reloj, orden de un set)", [2, 2], "gold"), ("Difieren por diseño (nombre del sistema)", [0, 1], "grey")],
        unit="Artefactos de 8", horizontal=True, label_w=250,
        note="Reproducible no significa idéntico a nivel de bytes en todo: el reloj y el orden de un set nunca lo serán y hay que excluirlos del hash o declararlos. Los dos que difieren entre sistemas por escritura (ingenuo.csv e informe_ingenuo.md) son defectos de escritura, no del experimento, y se corrigen sin tocar los datos.",
        note_kind="gold", foot=REAL)


def se384_seleccion() -> Fig:
    return grouped_bars(
        "Dos versiones idénticas comparadas 4 000 veces: porcentaje de informes que declaran una mejora de al menos el 5 %",
        "Barras horizontales con el porcentaje de informes que declaran una mejora de al menos 5 por ciento entre dos versiones idénticas: 0,1 con el procedimiento fijado de antemano, 23,1 al elegir la mejor de cinco repeticiones, 59,1 al elegir la mejor de seis métricas y 96,4 al combinar ambas.",
        ["Mediana de 30 contra mediana de 30, una métrica, una vez", "La mejor de 5 repeticiones de B contra una corrida de A", "La mejor de 6 métricas, 30 contra 30", "La mejor de 6 métricas y la mejor de 5 repeticiones de B"],
        [("Informes con «mejora» ≥ 5 %", [0.1, 23.1, 59.1, 96.4], "coral")],
        unit="Informes que declaran una mejora (%)", horizontal=True, label_w=330, ticks=[0, 25, 50, 75, 100],
        note="Nada del procedimiento es fraudulento paso a paso y casi todos los informes concluyen una mejora que no existe. La defensa es registrar antes la métrica, el número de repeticiones y el criterio, y publicar todas las corridas; el validador de la figura anterior no puede verificar el orden.",
        note_kind="coral", foot=SINT)


FIGURES = {
    "se-378-tormenta-de-reintentos.svg": se378_tormenta,
    "se-378-amplificacion-por-capas.svg": se378_capas,
    "se-378-eleccion-del-timeout.svg": se378_timeout,
    "se-379-interruptor-de-circuito.svg": se379_interruptor,
    "se-379-mamparos.svg": se379_mamparos,
    "se-379-degradar-bajo-sobrecarga.svg": se379_degradar,
    "se-380-disponibilidad-y-causa-comun.svg": se380_disponibilidad,
    "se-380-durabilidad-y-reparacion.svg": se380_durabilidad,
    "se-380-umbral-de-deteccion-de-fallos.svg": se380_deteccion,
    "se-381-doce-sondas-de-portabilidad.svg": se381_sondas,
    "se-381-datos-que-cambian-de-significado.svg": se381_interop,
    "se-381-matriz-de-compatibilidad.svg": se381_matriz,
    "se-382-campo-frente-a-laboratorio.svg": se382_campo,
    "se-382-deriva-de-peso.svg": se382_deriva,
    "se-382-contraste-medido.svg": se382_contraste,
    "se-383-umbral-de-estado-estable.svg": se383_umbral,
    "se-383-matriz-de-fallos.svg": se383_matriz,
    "se-383-deteccion-y-radio-de-impacto.svg": se383_radio,
    "se-384-validador-de-paquetes.svg": se384_validador,
    "se-384-reproducibilidad-entre-sistemas.svg": se384_reproducibilidad,
    "se-384-seleccion-de-resultados.svg": se384_seleccion,
}
