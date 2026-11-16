"""Figures for SE-271 to SE-276 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, fmt_es, grouped_bars, heatmap, line_chart, scatter, stacked_bars
from figures_part07_a import bars

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-271
def se271_cortes() -> Fig:
    return stacked_bars(
        "Corte de energía en cada paso posible de una actualización (enumeración exhaustiva)",
        "Barras horizontales apiladas con el estado en que queda el dispositivo según el punto de corte: una sola ranura que sobrescribe deja 17 de 19 puntos de corte con el dispositivo inservible; dos ranuras con indicador atómico, ninguno de 19; con un indicador de dos bytes sin validar queda 1 de 20 inválido y al validarlo ninguno.",
        ["Una sola ranura (sobrescribe)", "Dos ranuras, indicador atómico", "Dos ranuras, indicador de 2 bytes sin validar",
         "Dos ranuras, indicador de 2 bytes validado"],
        [("Queda la antigua", [1, 18, 18, 19], "teal"), ("Queda la nueva", [1, 1, 1, 1], "navy"),
         ("Queda inservible", [17, 0, 1, 0], "coral")],
        unit="Puntos de corte posibles", horizontal=True, label_w=300,
        note="La enumeración prueba todos los cortes posibles, no una muestra: el defecto del indicador de dos bytes existe en un solo punto de veinte y una prueba con cortes al azar lo vería pocas veces. Es un modelo de pasos, no de una memoria flash concreta con su orden de programación.",
        note_kind="coral", foot=SINT)


def se271_delta() -> Fig:
    return grouped_bars(
        "Bytes de una actualización diferencial de una imagen de 256 KiB",
        "Barras horizontales en escala logarítmica con los bytes que se transmiten según el cambio y el método: comparar bloques de 256 bytes por posición envía 13 200 bytes si cambian 50 bytes al azar y 135 168 si se inserta un solo byte a mitad de la imagen; buscar los bloques en cualquier posición envía 288 en ese caso, frente a 262 144 de la imagen completa.",
        ["50 bytes cambiados al azar", "500 bytes cambiados al azar", "Inserción de 100 bytes a mitad", "Inserción de 1 byte a mitad"],
        [("Bloques por posición", [13200, 106128, 135168, 135168], "coral"),
         ("Bloques en cualquier posición", [13512, 106936, 288, 288], "teal")],
        unit="Bytes enviados", horizontal=True, log=True, label_w=220, ticks=[100, 1000, 10000, 100000, 1000000],
        ref_lines=[(262144, "Imagen completa")],
        note="Una inserción desplaza todo lo que sigue y la comparación por posición lo trata como un cambio total; la búsqueda de bloques lo reduce a 288 bytes. Con cambios dispersos ambos métodos se parecen. Firmware sintético de 50 % de estructura y 50 % de bytes aleatorios: uno real se comprime de otro modo. La imagen nueva comprimida ocupa unos 184 000 bytes.",
        note_kind="gold", foot=SINT)


def se271_etapas() -> Fig:
    xs = [0.1, 0.5, 2, 10]
    return line_chart(
        "Dispositivos dañados de 10 000 según la fracción de fallo y la política de despliegue",
        "Líneas en doble escala logarítmica con los dispositivos dañados de 10 000 según el porcentaje de fallo de la versión: publicar a todos a la vez daña 10, 50, 200 y 1 002; las etapas de 1, 10 y 100 por ciento y las de 0,1, 1, 10 y 100 por ciento dañan entre 10 y 16 en cualquier caso, y detienen el despliegue casi siempre con fallos de 2 y 10 por ciento y casi nunca con 0,1.",
        [("Todos a la vez", [(0.1, 10, "10", "t"), (0.5, 50, "50", "t"), (2, 200, "200", "t"), (10, 1002, "1 002", "t")], "coral"),
         ("Etapas 1 %, 10 %, 100 %", [(0.1, 10, " ", "b"), (0.5, 15, "15", "b"), (2, 15, "15", "b"), (10, 11, "11", "b")], "gold"),
         ("Etapas 0,1 %, 1 %, 10 %, 100 %", [(0.1, 10, "10", "b"), (0.5, 15, "15", "t"), (2, 16, "16", "t"), (10, 10, "10", "t")], "teal")],
        x_label="Fallo de la versión (% de dispositivos)", y_label="Dispositivos dañados (de 10 000)", log_x=True, log_y=True,
        x_ticks=[(0.1, "0,1"), (0.5, "0,5"), (2, "2"), (10, "10")], y_ticks=[3, 10, 100, 1000],
        annotations=[(0.1, 10, "Con 0,1 % las etapas solo detienen el 5 % de los despliegues", 40, -70)],
        note="Las etapas protegen cuando el fallo es lo bastante frecuente como para dar tres informes en la etapa pequeña: con 2 % y 10 % detienen el 100 % de los despliegues. Con un fallo del 0,1 % la etapa de 100 dispositivos espera 0,1 fallos y el defecto llega a toda la flota: el tamaño de la primera etapa fija qué fallos se ven. Probabilidad de informe 0,9; 600 despliegues por punto.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-272
def se272_radio() -> Fig:
    return grouped_bars(
        "Dispositivos suplantables tras extraer k claves de una flota de 10 000",
        "Barras agrupadas en escala logarítmica con los dispositivos suplantables según las claves extraídas: con una clave de flota, una sola extracción permite suplantar a los 10 000; con claves por dispositivo, 1, 10 o 100 claves permiten suplantar exactamente 1, 10 o 100; con claves derivadas, si la clave maestra sale del dispositivo, vuelven a ser 10 000.",
        ["1 clave extraída", "10 claves extraídas", "100 claves extraídas"],
        [("Una clave de flota", [10000, 10000, 10000], "coral"), ("Claves por dispositivo", [1, 10, 100], "teal"),
         ("Derivadas, con la maestra extraída", [10000, 10000, 10000], "navy")],
        unit="Dispositivos suplantables (de 10 000)", log=True, ticks=[1, 10, 100, 1000, 10000],
        note="La clave por dispositivo limita el daño de una extracción a un dispositivo, siempre que la clave maestra nunca esté en ninguno. Las firmas son HMAC-SHA256 reales; la flota, la extracción y los números son sintéticos y no se atacó ningún chip.",
        note_kind="teal", foot=SINT)


def se272_reloj() -> Fig:
    def pct(v):
        return "0 %" if v == 0 else fmt_es(v, 2) + " %"
    return heatmap(
        "Mensajes legítimos rechazados por una ventana de tiempo según el desfase del reloj",
        "Mapa de calor con el porcentaje de mensajes legítimos rechazados según el desfase típico del reloj y el ancho de la ventana: con desfase de 5 segundos una ventana de más o menos 5 rechaza el 31,56 por ciento; con 30 segundos de desfase una de más o menos 5 rechaza el 86,71 y una de 30 el 31,56; una de 120 segundos casi no rechaza, 0,01 por ciento.",
        ["σ = 1 s", "σ = 5 s", "σ = 30 s"], ["Ventana ±5 s", "Ventana ±30 s", "Ventana ±120 s"],
        [[0.0, 0.0, 0.0], [31.56, 0.0, 0.0], [86.71, 31.56, 0.01]],
        unit="% de mensajes rechazados", row_title="Desfase típico del reloj", col_title="Ancho de la ventana de aceptación",
        scale="coral", vmin=0, vmax=100, cell_fmt=pct, highlight=[(1, 0), (2, 1)], cell_h=48, label_w=90,
        note="Ensanchar la ventana evita rechazos y deja más tiempo para reproducir un mensaje capturado. Un contador estricto no depende del reloj, pero si se reinicia sin memoria persistente acepta el 50,8 % de las reproducciones del modelo. Desfase gaussiano supuesto; no se midió ningún reloj.",
        note_kind="coral", foot=SINT)


def se272_semilla() -> Fig:
    return grouped_bars(
        "Claves de 64 bits generadas con una semilla débil (5000 dispositivos)",
        "Barras agrupadas con las claves repetidas y las recuperadas por enumeración de 3 600 semillas, de 5000 dispositivos: con el segundo de arranque dentro de una hora hay 2279 repetidas y se recuperan las 5000; con un día, 149 repetidas y 197 recuperadas (3,94 por ciento); con una semilla de 32 bits, ninguna.",
        ["Segundo de arranque dentro de 1 hora", "Segundo de arranque dentro de 1 día", "Semilla de 32 bits"],
        [("Claves repetidas", [2279, 149, 0], "gold"), ("Recuperadas enumerando 3 600 semillas", [5000, 197, 0], "coral")],
        unit="Dispositivos (de 5 000)",
        note="Una clave de 64 bits con una semilla de 3600 posibilidades tiene la seguridad de 12 bits: la longitud de la clave no importa si la semilla es predecible. Se usó el generador estándar de Python solo para ilustrar el mecanismo; no es un generador criptográfico y ningún dispositivo real lo hace así.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-273
def se273_reporte() -> Fig:
    return scatter(
        "Costo en bytes frente al error de reconstrucción de cinco estrategias de reporte",
        "Dispersión con los bytes enviados al día, en escala logarítmica, frente al error medio de reconstrucción de una señal de 1 Hz: enviar cada segundo cuesta 691 200 bytes y no tiene error; la banda muerta de 0,5 cuesta 1 250 con error 0,140; la media por minuto, 11 520 con error 0,089, y el máximo por minuto, 11 520 con 0,250. Ninguna estrategia gana en las dos medidas.",
        [("Cada segundo", [(691200, 0.0, "Cada segundo · aviso 0 s", "l")], "teal"),
         ("Media por minuto", [(11520, 0.089, "Media por minuto · 22 s", "l")], "gold"),
         ("Máximo por minuto", [(11520, 0.25, "Máximo por minuto · 22 s", "r")], "coral"),
         ("Banda muerta de 0,5", [(1250, 0.14, "Banda muerta de 0,5 · 0 s", "r")], "navy"),
         ("Media por minuto y evento", [(11608, 0.10, "Media y evento · 22 s", "r")], "grey")],
        x_label="Bytes enviados al día", y_label="Error medio de reconstrucción (°C)", log_x=True,
        x_ticks=[(1000, "1 000"), (10000, "10 000"), (100000, "100 000"), (1000000, "1 000 000")],
        y_ticks=[0, 0.1, 0.2, 0.3], y_zero=True, decimals=3,
        note="El rótulo de cada punto añade el retraso mediano de aviso. La banda muerta reduce los bytes 550 veces y avisa de inmediato, pero reconstruye peor la señal lenta. La media por minuto la reconstruye mejor y retrasa el aviso. No hay estrategia que gane en todo: se elige según lo que se decide con los datos. Señal sintética con ocho picos de 3 °C; las cinco detectan los ocho eventos.",
        note_kind="gold", foot=SINT)


def se273_plazo() -> Fig:
    items = [
        ("Decisión local", 100.0, "teal", "100,0 %"),
        ("Decisión solo en la nube", 61.41, "coral", "61,41 %"),
        ("Nube con respaldo local", 100.0, "teal", "100,0 %"),
    ]
    return bars("Decisiones de control que cumplen un plazo de 100 ms (100 000 decisiones)",
                "Barras: con un plazo de 100 milisegundos, una decisión local lo cumple el 100 por ciento de las veces, una que depende de la nube el 61,41 por ciento, con un percentil 99 de ida y vuelta de 256,7 milisegundos y la nube caída el 5 por ciento del tiempo, y una nube con respaldo local el 100 por ciento.",
                items, 5, "La nube incumple por la latencia (mediana de 80 ms con cola larga) y por las caídas; el respaldo local cumple siempre, pero decide con menos información. Latencias lognormales y caídas del 5 % supuestas, no medidas en ninguna red.",
                label_w=300, width=950, note_kind="gold", foot=SINT)


def se273_carga() -> Fig:
    return grouped_bars(
        "Bytes por muestra según la codificación y el tamaño del lote",
        "Barras agrupadas con los bytes por muestra de una lectura de cinco magnitudes: JSON ocupa unos 85 con cualquier lote y binario 13; comprimir un lote de 60 muestras baja el JSON a 14,9 y el binario a 10,5, pero con una sola muestra el JSON comprimido ocupa 83,0 y el binario comprimido 21,0, más que el binario sin comprimir.",
        ["Lote de 1 muestra", "Lote de 10 muestras", "Lote de 60 muestras"],
        [("JSON", [85.0, 84.9, 84.7], "coral"), ("Binario", [13.0, 13.0, 13.0], "teal"),
         ("JSON comprimido", [83.0, 23.0, 14.9], "gold"), ("Binario comprimido", [21.0, 13.0, 10.5], "navy")],
        unit="Bytes por muestra", decimals=1,
        note="El formato compacto ahorra más que comprimir cuando el lote es pequeño; comprimir ayuda cuando hay muchas muestras parecidas y a cambio exige memoria y energía en el dispositivo. Lecturas sintéticas con ruido gaussiano; la compresión es zlib en el nivel 9.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-274
def se274_voto() -> Fig:
    return grouped_bars(
        "Fallo peligroso no detectado en una misión: un sensor frente a votación 2 de 3",
        "Barras agrupadas con la probabilidad de fallo peligroso no detectado según la fracción de fallos de causa común, con probabilidad de fallo de 0,1 por sensor: un sensor se queda en unos 0,099; la votación de dos de tres baja a 0,0278 con fallos independientes, 3,6 veces menos, y sube a 0,0380 con 20 por ciento de causa común, con una mejora de 2,6 veces.",
        ["Sin causa común (0 %)", "5 % de causa común", "20 % de causa común"],
        [("Un sensor", [0.0998, 0.0997, 0.0988], "coral"), ("2 de 3 simulado", [0.0278, 0.0303, 0.0380], "teal"),
         ("2 de 3 analítico", [0.0300, 0.0321, 0.0392], "navy")],
        unit="Probabilidad de fallo peligroso no detectado", decimals=4,
        note="La redundancia no triplica la seguridad: con p = 0,1 solo la divide por 3,6 (3,3 con 5 % y 2,6 con 20 % de causa común), y la causa común (misma fuente de alimentación, mismo error de calibración, mismo software) se come la mejora. Un millón de misiones por grupo; p = 0,1 es alto a propósito para poder medirlo.",
        note_kind="coral", foot=SINT)


def se274_vigilancia() -> Fig:
    return line_chart(
        "Horas perdidas por año según el plazo del temporizador de vigilancia",
        "Línea en doble escala logarítmica con las horas perdidas por año según el plazo del temporizador de vigilancia: un plazo de 0,1 segundos pierde 8,78 horas por reinicios falsos (17,3 al día), uno de 1 segundo 1,17, uno de 5 segundos 0,06 y uno de 10 segundos 0,05, pero con 10 segundos un cuelgue tarda 15 en resolverse.",
        [("Horas perdidas por año", [(0.1, 8.78, "8,78", "t"), (0.5, 3.10, "3,10", "t"), (1, 1.17, "1,17", "t"),
                                    (2, 0.32, "0,32", "t"), (5, 0.06, "0,06", "t"), (10, 0.05, "0,05", "b")], "coral")],
        x_label="Plazo del temporizador de vigilancia (s)", y_label="Horas perdidas por año", log_x=True, log_y=True,
        x_ticks=[(0.1, "0,1"), (0.5, "0,5"), (1, "1"), (2, "2"), (5, "5"), (10, "10")], y_ticks=[0.01, 0.1, 1, 10],
        annotations=[(0.1, 8.78, "0,1 s: 17,3 reinicios falsos por día; un cuelgue se resuelve en 5,1 s", 60, 60),
                     (10, 0.05, "10 s: casi sin reinicios falsos, pero un cuelgue tarda 15 s", -30, -100)],
        note="Un plazo corto reacciona rápido y reinicia sin motivo las operaciones largas legítimas; uno largo casi no se equivoca y tarda en actuar. El percentil 99,9 de las operaciones es 6,6 s: un plazo de 5 s aún reinicia una de cada mil. Un cuelgue al mes y 20 operaciones largas al día son supuestos.",
        note_kind="gold", foot=SINT)


def se274_vuelta() -> Fig:
    return grouped_bars(
        "Temporizadores armados en los dos minutos previos a la vuelta de un contador de 32 bits",
        "Barras horizontales con el porcentaje de decisiones erróneas de 200 000 temporizadores armados justo antes de la vuelta de un contador de milisegundos de 32 bits: la comparación directa decide mal el 33,35 por ciento, 66 703, y la resta sin signo ninguno.",
        ["Comparación directa de tiempos (66 703 de 200 000)", "Resta sin signo en 32 bits (0 de 200 000)"],
        [("Decisiones erróneas", [33.35, 0.0], "coral")],
        unit="% de los 200 000 temporizadores", horizontal=True, label_w=300, ticks=[0, 10, 20, 30, 40],
        note="El defecto no aparece nunca en las pruebas de un día y llega a los 49,71 días en todos los dispositivos a la vez si arrancaron juntos; los segundos con signo de 32 bits se desbordan el 19 de enero de 2038, 03:14:07 UTC. Se cura con una comparación escrita para la vuelta, no con un contador más grande. Un dispositivo de 15 años instalado en 2026 pasa por 2038.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-275
def se275_inyeccion() -> Fig:
    return heatmap(
        "Fallos detectados de 100 inyectados por tipo según las comprobaciones activas",
        "Mapa de calor con los fallos detectados de 100 inyectados por tipo según las comprobaciones activas, acumulativas: solo rango no detecta ninguno; la variación máxima detecta picos, ruido y bit alto; el valor congelado y la ausencia de lectura completan esos tipos; la dispersión cierra el ruido; y solo la referencia independiente detecta la deriva, hasta los 600 de 600.",
        ["Solo rango · 0 de 600", "Rango y variación · 298", "Más congelado y ausencia · 498", "Más dispersión · 500",
         "Más referencia independiente · 600"],
        ["Congelado", "Deriva", "Pico", "Ruido ×10", "Bit alto", "Ausencia"],
        [[0, 0, 0, 0, 0, 0], [0, 0, 100, 98, 100, 0], [100, 0, 100, 98, 100, 100], [100, 0, 100, 100, 100, 100],
         [100, 100, 100, 100, 100, 100]],
        unit="fallos detectados de 100", row_title="Comprobaciones activas (acumulativas)", col_title="Tipo de fallo inyectado",
        scale="teal", vmin=0, vmax=100, decimals=0, highlight=[(4, 1)], cell_h=44, label_w=280,
        note="La deriva lenta pasa todas las comprobaciones que miran solo el propio sensor: cada lectura parece plausible con respecto a la anterior. Solo una referencia independiente la ve. Cada celda son 100 fallos con instante de aparición aleatorio; los fallos y las comprobaciones son modelos del autor. El número tras cada fila es el total detectado de 600.",
        note_kind="gold", foot=SINT)


def se275_escritura() -> Fig:
    return stacked_bars(
        "Corte de energía en cada punto de la escritura de una configuración de 8 bytes",
        "Barras horizontales apiladas con el estado en que queda la configuración según el punto de corte: sobrescribir en el mismo sitio deja una configuración inválida en 8 de 10 puntos; una sola copia con CRC, en 10 de 12; dos copias alternadas con CRC, en ninguno de 12, y queda siempre la antigua o la nueva.",
        ["Sobrescribir en el mismo sitio", "Una copia con CRC", "Dos copias alternadas con CRC"],
        [("Antigua válida", [1, 1, 11], "teal"), ("Nueva válida", [1, 1, 1], "navy"), ("Inválida", [8, 10, 0], "coral")],
        unit="Puntos de corte posibles", horizontal=True, label_w=260,
        note="Una sola copia con CRC detecta la corrupción, pero no la repara: sin la copia anterior no hay a qué volver. La alternancia de dos copias convierte cualquier corte en «antigua o nueva». Modelo de escritura byte a byte; una flash real programa páginas y puede dejar bits a medias.",
        note_kind="teal", foot=SINT)


def se275_amfe() -> Fig:
    items = [
        ("Se conserva el mismo primer modo de fallo", 86.3, "gold", "86,3 %"),
        ("Se conservan los mismos tres peores modos", 27.2, "coral", "27,2 %"),
        ("Correlación de rangos media (×100)", 83.4, "gold", "0,834"),
    ]
    return bars("Estabilidad de un AMFE de 12 modos de fallo si dos evaluadoras difieren en ±1 punto",
                "Barras: al perturbar cada puntuación de gravedad, ocurrencia y detección en más o menos un punto en 2000 repeticiones, el primer modo de fallo se conserva el 86,3 por ciento de las veces, el conjunto de los tres peores solo el 27,2 y la correlación de rangos media es 0,834, con un mínimo de 0,427.",
                items, 5, "El número de prioridad de riesgo mezcla tres escalas ordinales: un punto de desacuerdo mueve el ranking. Sirve para empezar una conversación, no para ordenar con precisión. Las puntuaciones de los doce modos son sintéticas, con semilla fija.",
                label_w=470, width=1010, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-276
def se276_mes() -> Fig:
    return grouped_bars(
        "Un mes de 1000 dispositivos simulados con cortes de red, cuelgues y una actualización",
        "Barras agrupadas con las horas fuera de servicio por dispositivo y los dispositivos inutilizados de 1000 en un mes simulado, al sumar defensas: el dispositivo básico, que recibe el 86,3 por ciento de los datos, acumula 51,5 horas y 22 inutilizados; con vigilancia, 9,5 horas y 20; con la cola de almacenar y reenviar, 98,6 por ciento de los datos; con dos ranuras y reversión, 0,1 horas y ninguno inutilizado, con 99,9 por ciento.",
        ["Básico\n86,3 % de los datos", "Con vigilancia\n91,8 % de los datos", "Y cola de reenvío\n98,6 % de los datos", "Y dos ranuras\n99,9 % de los datos"],
        [("Horas fuera de servicio por dispositivo", [51.5, 9.5, 9.5, 0.1], "gold"),
         ("Dispositivos inutilizados de 1000", [22, 20, 20, 0], "coral")],
        unit="Horas · dispositivos de 1000 (menos es mejor)",
        note="Cada mecanismo cura un problema distinto: la vigilancia el tiempo caído, la cola los datos perdidos, las dos ranuras los dispositivos inutilizados. Probabilidades de cuelgue, cortes y fallo de actualización supuestas por el autor; no se simuló ningún componente real.",
        note_kind="teal", foot=SINT)


def se276_validador() -> Fig:
    kinds = [("Campo ausente", 17, 0), ("Sin identidad individual", 12, 0), ("Sin plan de reversión", 12, 0),
             ("Sin rotación con plazo", 15, 0), ("Reintentos sin jitter", 25, 0), ("Despliegue sin etapas", 20, 0),
             ("Fecha de revisión sin formato", 17, 0), ("Responsable colectivo", 24, 0),
             ("Plazo del temporizador menor que la operación más larga", 0, 15),
             ("Etapas de despliegue en orden inverso", 0, 16), ("Umbral invertido (40 a 5 °C)", 0, 17),
             ("Clave maestra almacenada en el dispositivo", 0, 10)]
    return stacked_bars(
        "Validador de paquetes de dispositivo sobre 200 mutaciones: 142 detectadas",
        "Barras horizontales apiladas con las mutaciones detectadas y no detectadas por un verificador de forma, por tipo de mutación: detecta todas las de los ocho tipos que rompen la forma, 142 de 200, y ninguna de las 58 que cambian el sentido: un plazo de vigilancia menor que la operación más larga, etapas de despliegue en orden inverso, un umbral invertido o una clave maestra almacenada en el dispositivo.",
        [k for k, _, _ in kinds],
        [("Detectadas", [d for _, d, _ in kinds], "teal"), ("No detectadas", [m for _, _, m in kinds], "coral")],
        unit="Mutaciones de cada tipo", horizontal=True, label_w=330,
        note="Las cuatro mutaciones que no ve son justo las que rompen el dispositivo: tienen forma correcta y sentido contrario. Las reglas se escribieron conociendo las mutaciones, así que el 100 % por tipo es optimista.",
        note_kind="gold", foot=SINT)


def se276_flota() -> Fig:
    def factor(a, b):
        return "sin cambio" if a == b else f"÷ {fmt_es(a / b, 0)}"
    return dumbbell(
        "Mil dispositivos y una versión defectuosa (3 % fallan; informe con probabilidad 0,9)",
        "Dumbbell con los dispositivos dañados cuando acaba la publicación y los que siguen dañados al final, de 1000 con una versión que daña al 3 por ciento: publicar a todos daña 30 y siguen 30; las etapas dañan 18, detienen el despliegue a tiempo en el 44,2 por ciento y también dejan 18 sin reversión; con reversión automática y umbral de tres informes solo 1,8 siguen dañados.",
        [("Publicar a todos el día 1 · 1 día · 0 % detenidos", 30.0, 30.0),
         ("Etapas sin reversión automática · 7,7 días · 44,2 % detenidos", 18.0, 18.0),
         ("Etapas con reversión y umbral de 3 informes · 7,7 días · 44,2 % detenidos", 18.0, 1.8)],
        unit="Dispositivos dañados (de 1000)", names=("Dañados al terminar la publicación", "Siguen dañados al final"),
        delta=factor, label_w=330,
        note="Las etapas reducen el daño inicial; la reversión lo repara. Con el 3 % de fallo, 55,8 % de los despliegues llegan a toda la flota antes de detectar el problema, porque la primera etapa de 10 dispositivos espera 0,3 fallos. 2000 despliegues; la reparación al 90 % es un supuesto.",
        note_kind="teal", foot=SINT)


FIGURES = {
    "se-271-cortes-de-energia-en-una-actualizacion.svg": se271_cortes,
    "se-271-actualizacion-diferencial.svg": se271_delta,
    "se-271-despliegue-por-etapas.svg": se271_etapas,
    "se-272-claves-extraidas-de-una-flota.svg": se272_radio,
    "se-272-ventana-de-tiempo-y-desfase.svg": se272_reloj,
    "se-272-semillas-debiles.svg": se272_semilla,
    "se-273-estrategias-de-reporte.svg": se273_reporte,
    "se-273-decision-local-o-en-la-nube.svg": se273_plazo,
    "se-273-codificacion-de-la-carga.svg": se273_carga,
    "se-274-votacion-y-causa-comun.svg": se274_voto,
    "se-274-plazo-de-vigilancia.svg": se274_vigilancia,
    "se-274-vuelta-del-contador.svg": se274_vuelta,
    "se-275-inyeccion-de-fallos.svg": se275_inyeccion,
    "se-275-corte-durante-la-escritura.svg": se275_escritura,
    "se-275-estabilidad-de-un-amfe.svg": se275_amfe,
    "se-276-un-mes-de-flota-simulada.svg": se276_mes,
    "se-276-validador-de-paquetes.svg": se276_validador,
    "se-276-flota-y-version-defectuosa.svg": se276_flota,
}
