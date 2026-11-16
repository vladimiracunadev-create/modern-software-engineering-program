"""Figures for SE-265 to SE-270 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import (AXIS, FILL, INK, Fig, _kit_finish, _kit_start, _row_labels, fmt_es, grouped_bars, heatmap,
                        line_chart, timeline)
from figures_part07_a import bars

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-265
def se265_latencia() -> Fig:
    return grouped_bars(
        "Latencia de un botón según la arquitectura del firmware (escala logarítmica)",
        "Barras horizontales en escala logarítmica con la latencia de un botón: el sondeo en el bucle principal tarda 14,19 milisegundos de media, 78,2 en el percentil 99 y 166,0 como máximo; la interrupción con manejo inmediato tarda unos 0,03 en los tres casos, cerca de cinco mil veces menos en el peor caso.",
        ["Sondeo del botón en el bucle principal", "Interrupción con manejo inmediato"],
        [("Media", [14.19, 0.025], "teal"), ("Percentil 99", [78.2, 0.03], "gold"), ("Máximo", [166.0, 0.03], "coral")],
        unit="Latencia (ms)", horizontal=True, log=True, label_w=250, ticks=[0.01, 0.1, 1, 10, 100, 1000],
        note="La cola larga manda: el máximo del sondeo es 12 veces su media, porque lo fija la vuelta más lenta del bucle (una con radio dura unos 50 ms), no el botón. La interrupción cambia el problema de sitio: ahora hay que acotar lo que hace dentro de la rutina. Las duraciones del bucle son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se265_acumulador() -> Fig:
    return heatmap(
        "Promedios erróneos al acumular lecturas de 12 bits en 16 bits (% de ventanas)",
        "Mapa de calor con el porcentaje de promedios erróneos según el número de lecturas y la señal media: con señal media de 1000 no falla ninguno hasta 32 lecturas y con 64 falla el 10 por ciento; con señal media de 3000 falla el 100 por ciento desde 32 lecturas, con un error de 2048 cuentas.",
        ["4 lecturas", "8 lecturas", "16 lecturas", "17 lecturas", "32 lecturas", "64 lecturas"],
        ["Señal media 1000", "Señal media 3000"],
        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 100], [10, 100]],
        unit="% de ventanas erróneas", row_title="Lecturas promediadas", col_title="Ventanas con el promedio erróneo (%)",
        scale="coral", vmin=0, vmax=100, decimals=0, suffix=" %", highlight=[(4, 1), (5, 1), (5, 0)], cell_h=40,
        note="El frente de fallo avanza con el producto número de lecturas × valor máximo: 32 × 3000 supera 65 535 y desborda siempre. Cuando falla, el error es de 2048 cuentas (65 536 / 32) y el promedio sigue pareciendo plausible. Sobre 20 000 ventanas por celda, señal con ruido gaussiano de 150 cuentas.",
        note_kind="coral", foot=SINT)


def se265_antirrebote() -> Fig:
    items = [
        ("Tres ejemplos de camino feliz", 4, "gold", "4 de 5"),
        ("200 secuencias con rebotes aleatorios", 5, "teal", "5 de 5"),
    ]
    return bars("Mutantes distinguibles de un antirrebote de tres muestras que mata cada suite",
                "Barras: de ocho variantes de un antirrebote, tres son equivalentes y cinco son distinguibles; tres ejemplos de camino feliz matan cuatro de las cinco y doscientas secuencias con rebotes aleatorios, contra un modelo de referencia, matan las cinco.",
                items, 80, "El mutante que sobrevive a los ejemplos no reinicia el contador al cambiar la entrada: solo se nota con rebotes. Tres variantes no cambian ninguna salida y no se pueden matar. El modelo de referencia es una función pura que se ejecuta en el equipo de desarrollo, sin hardware.",
                label_w=420, width=900, note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-266
def se266_bus() -> Fig:
    ticks = [(1, "1"), (2, "2"), (6, "6"), (16, "16"), (64, "64")]
    return line_chart(
        "Eficiencia de datos al leer N bytes de un registro: I²C frente a SPI",
        "Líneas de eficiencia de datos según los bytes leídos, en escala logarítmica: por I2C sube de 20,5 por ciento con 1 byte a 84,5 con 64 bytes; por SPI sube de 50 a 98,5 por ciento; leer un byte por I2C cuesta 39 ciclos de reloj, 97,5 microsegundos a 400 kilohercios.",
        [("I²C", [(1, 20.5), (2, 33.3), (6, 57.1), (16, 73.6), (64, 84.5)], "coral"),
         ("SPI", [(1, 50.0), (2, 66.7), (6, 85.7), (16, 94.1), (64, 98.5)], "teal")],
        x_label="Bytes leídos por transacción", y_label="Eficiencia (bits útiles / ciclos de reloj, %)", log_x=True,
        x_ticks=ticks, y_ticks=[0, 20, 40, 60, 80, 100], decimals=1,
        annotations=[(1, 20.5, "1 byte por I²C: 39 ciclos, 97,5 µs a 400 kHz", 95, 18)],
        note="La eficiencia mide bits útiles sobre ciclos de reloj, no la velocidad del bus: con direcciones, confirmaciones y reinicio, leer un solo byte por I²C desperdicia cuatro de cada cinco ciclos, y la brecha con SPI se cierra al agrupar lecturas. El cálculo es aritmético, sin dispositivo real ni capacitancia de la línea.",
        note_kind="gold", foot=SINT)


def se266_codigos() -> Fig:
    return grouped_bars(
        "Errores no detectados de 200 000 tramas de 8 bytes según el código de control",
        "Barras horizontales con las tramas con error que no detecta cada código, de 200 000 inyectadas por tipo de error: la paridad deja pasar todas las de dos bits invertidos (200 000) y 99 238 ráfagas de hasta 8 bits; la suma de 8 bits deja pasar 12 445 con dos bits y 2 143 con tres; el CRC-8 de polinomio 0x07 no deja pasar ninguna en estos casos.",
        ["Un bit invertido", "Dos bits invertidos", "Tres bits invertidos", "Ráfaga de hasta 8 bits"],
        [("Paridad", [0, 200000, 0, 99238], "coral"), ("Suma de 8 bits", [0, 12445, 2143, 0], "gold"),
         ("CRC-8", [0, 0, 0, 0], "teal")],
        unit="Tramas con error no detectado (de 200 000)", horizontal=True, label_w=200,
        ticks=[0, 50000, 100000, 150000, 200000],
        note="El CRC-8 detecta toda ráfaga de hasta ocho bits y toda combinación de uno a tres bits en tramas tan cortas, pero deja pasar errores más largos o más numerosos en la proporción de 1 entre 256. Las tramas, los errores y la semilla son sintéticos: no se midió ningún bus real.",
        note_kind="teal", foot=SINT)


def se266_adc() -> Fig:
    xs = [1, 4, 16, 64, 256]
    flat = [(x, 0.431, "0,431 en todos" if i == 3 else " ", "t") for i, x in enumerate(xs)]
    return line_chart(
        "Error eficaz de un ADC de 10 bits al promediar N lecturas",
        "Líneas en doble escala logarítmica con el error eficaz en LSB según el número de lecturas promediadas: con ruido de 0,5 LSB baja de 0,583 con una lectura a 0,036 con 256, y con ruido de 1,0 LSB de 1,031 a 0,065, a la mitad por cada factor cuatro; sin ruido se queda plana en 0,431.",
        [("Sin ruido", flat, "grey"),
         ("Ruido de 0,5 LSB", list(zip(xs, [0.583, 0.289, 0.145, 0.071, 0.036])), "teal"),
         ("Ruido de 1,0 LSB", list(zip(xs, [1.031, 0.520, 0.259, 0.128, 0.065])), "coral")],
        x_label="Lecturas promediadas, N", y_label="Error eficaz (LSB)", log_x=True, log_y=True,
        x_ticks=[(1, "1"), (4, "4"), (16, "16"), (64, "64"), (256, "256")], y_ticks=[0.03, 0.1, 0.3, 1, 3],
        note="Sobremuestrear mejora la resolución solo si hay un poco de ruido que la reparta: sin ruido todas las lecturas redondean igual y el promedio no mejora. Cada factor cuatro cuesta cuatro veces más tiempo y energía. Señal constante de 1,2345 V con referencia de 3,3 V.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-267
def se267_bateria() -> Fig:
    xs = [2, 5, 20, 100]
    return line_chart(
        "Vida de una pila de 2400 mAh según la corriente de reposo y el periodo de despertar",
        "Líneas en doble escala logarítmica con la vida de una pila de 2400 miliamperios hora según la corriente de reposo: con despertar cada 10 segundos baja de 198 a 166 días entre 2 y 100 microamperios; con 60 segundos de 1 135 a 538; con 600 segundos de 7 650 a 901, de modo que el reposo domina cuando el nodo despierta poco.",
        [("Despierta cada 10 s", list(zip(xs, [198, 197, 191, 166])), "coral"),
         ("Cada 60 s", list(zip(xs, [1135, 1098, 943, 538])), "gold"),
         ("Cada 600 s", [(2, 7650, "7 650", "r"), (5, 6222), (20, 3219), (100, 901)], "teal")],
        x_label="Corriente de reposo (µA)", y_label="Vida de la pila (días)", log_x=True, log_y=True,
        x_ticks=[(2, "2"), (5, "5"), (20, "20"), (100, "100")], y_ticks=[100, 1000, 10000],
        note="Con un despertar cada 10 s la corriente de reposo apenas cuenta (la línea es casi plana): manda lo que se gasta despierto. Con 600 s, pasar de 2 a 100 µA divide la vida por 8,5. Supuestos: 15 mA durante 120 ms y 80 mA durante 40 ms de radio, autodescarga del 1 % anual, sin envejecimiento ni temperatura.",
        note_kind="gold", foot=SINT)


def se267_flash() -> Fig:
    return grouped_bars(
        "Borrados del sector más usado tras 200 000 escrituras en una flash de 16 sectores",
        "Barras horizontales con los borrados del sector más usado tras 200 000 escrituras (la mitad de los datos, fríos): sobrescribir siempre el mismo sector lo borra 200 000 veces y deja una vida relativa de 0,062; rotar entre los sectores libres lo deja en 25 000 y 0,5; rotar entre todos, moviendo los datos fríos, en 12 500 y 1,0.",
        ["Sobrescribir siempre el mismo sector (vida relativa 0,062)", "Rotar entre los sectores libres (vida relativa 0,5)",
         "Rotar entre todos, moviendo los datos fríos (vida relativa 1,0)"],
        [("Borrados del sector más usado", [200000, 25000, 12500], "coral")],
        unit="Borrados del sector más usado", horizontal=True, label_w=330, ticks=[0, 50000, 100000, 150000, 200000],
        note="Con 64 sectores de 4 KiB, registros de 16 B y 10 000 borrados por sector, un registro por minuto da 6,9 días si se sobrescribe un solo sector y unos 312 años con un registro circular. La segunda cifra ignora otros límites (retención de datos, tensión): es un techo teórico.",
        note_kind="coral", foot=SINT)


def se267_filtro() -> Fig:
    return grouped_bars(
        "Filtro y += (x − y) >> k con enteros: error final subiendo, en cuentas de 10 bits",
        "Barras agrupadas con el error final de un filtro de paso bajo con enteros cuando la entrada sube: con k igual a 2, 4 y 6 se queda a 3, 15 y 63 cuentas si se trunca y a 1, 7 y 31 si se redondea, de modo que redondear reduce la zona muerta a la mitad; con coma flotante el error es cero.",
        ["k = 2", "k = 4", "k = 6"],
        [("Truncado subiendo", [3, 15, 63], "coral"), ("Redondeado subiendo", [1, 7, 31], "teal")],
        unit="Error final (cuentas de 10 bits)",
        note="El truncado tiene una zona muerta de 2^k − 1 cuentas hacia arriba: el filtro «converge» sin llegar a la entrada y el sesgo es asimétrico. Bajando, el truncado converge exactamente (0) y el redondeado se queda a 2, 8 y entre 23 y 32 cuentas. Con k = 6 y entradas de 10 bits, 63 cuentas son un 6 % del rango.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-268
def se268_rm() -> Fig:
    xs = [0.7, 0.8, 0.9, 0.95]

    def pts(values, sides, hide_full):
        out = []
        for x, v, side in zip(xs, values, sides):
            label = " " if (hide_full and v == 100) else fmt_es(v, 0 if v == 100 else 1) + " %"
            out.append((x, v, label, side))
        return out
    return line_chart(
        "Conjuntos de tareas rate-monotonic planificables según la utilización (análisis exacto)",
        "Líneas con el porcentaje de conjuntos de tareas planificables por prioridades por periodo según la utilización total: con tres, cinco u ocho tareas lo son el 100 por ciento con utilización 0,7 y 0,8, aunque la cota de Liu y Layland sea 0,78, 0,743 y 0,724; con 0,9 lo son entre 88,8 y 92,5 por ciento y con 0,95 entre 49,7 y 73,0, y la caída es más fuerte cuantas más tareas hay.",
        [("3 tareas", pts([100, 100, 92.5, 73.0], "tttt", False), "teal"),
         ("5 tareas", pts([100, 100, 89.3, 62.5], "ttrl", True), "gold"),
         ("8 tareas", pts([100, 100, 88.8, 49.7], "bbbb", True), "coral")],
        x_label="Utilización total del procesador, U", y_label="Conjuntos planificables (%)",
        x_ticks=[(0.7, "0,7"), (0.8, "0,8"), (0.9, "0,9"), (0.95, "0,95")], y_ticks=[0, 20, 40, 60, 80, 100],
        note="La cota es suficiente pero no necesaria: por debajo de ella siempre se cumple y por encima a veces. Con U = 0,8 todos los conjuntos sintéticos pasan aunque 0,8 supere la cota de las tres series (0,78, 0,743 y 0,724). El análisis exacto de tiempo de respuesta decide cada caso; 2000 conjuntos por punto, periodos entre 10 y 1000.",
        note_kind="teal", foot=SINT)


def se268_plazos() -> Fig:
    return line_chart(
        "Plazos incumplidos de una tarea periódica según la variabilidad del tiempo de ejecución",
        "Líneas con el porcentaje de plazos incumplidos de una tarea con periodo y plazo de 10 milisegundos según la variabilidad σ del tiempo de ejecución: con utilización media 0,5 sube de 0,0 a 9,7 por ciento, con 0,7 de 0,01 a 32,3 y con 0,9 de 17,0 a 72,4; la media sola no decide un plazo.",
        [("Utilización media 0,5", [(0.1, 0.0, " ", "t"), (0.3, 0.7, "0,7 %", "t"), (0.6, 9.7, "9,7 %", "b")], "teal"),
         ("Utilización media 0,7", [(0.1, 0.01, "0,0 y 0,01 %", "t"), (0.3, 11.2, "11,2 %", "t"), (0.6, 32.3, "32,3 %", "t")], "gold"),
         ("Utilización media 0,9", [(0.1, 17.0, "17,0 %", "t"), (0.3, 55.6, "55,6 %", "t"), (0.6, 72.4, "72,4 %", "t")], "coral")],
        x_label="Variabilidad del tiempo de ejecución, σ", y_label="Plazos incumplidos (%)",
        x_ticks=[(0.1, "0,1"), (0.3, "0,3"), (0.6, "0,6")], y_ticks=[0, 20, 40, 60, 80],
        annotations=[(0.3, 11.2, "Con U = 0,7 y σ = 0,3 se incumple un plazo de cada nueve", 30, -100)],
        note="Con utilización media de 0,7 y σ = 0,3 se incumple un plazo de cada nueve, aunque la media quepa con holgura. El tiempo medio no sirve para decidir si se cumple un plazo: hace falta el peor caso o un percentil alto. 200 000 trabajos por punto, tiempos lognormales y trabajos encadenados.",
        note_kind="coral", foot=SINT)


def se268_inversion() -> Fig:
    items = [
        ("Sin herencia, M liberada entre 2 y 5 ms", 15.1, "coral", "15,1 ms"),
        ("Sin herencia, M liberada entre 6 y 10 ms", 7.0, "gold", "7,0 ms"),
        ("Con herencia de prioridad, cualquier caso", 7.0, "teal", "7,0 ms"),
    ]
    return bars("Respuesta de la tarea de prioridad alta con un mutex tomado por la de baja",
                "Barras: la tarea de prioridad alta, con 2 milisegundos de trabajo y un mutex que retiene la de baja, responde en 15,1 milisegundos si una de prioridad media se libera mientras la baja tiene el mutex y en 7,0 si no; con herencia de prioridad responde siempre en 7,0.",
                items, 25, "La tarea media, que no necesita el mutex, retrasa a la alta durante todo su cómputo. La herencia de prioridad acota la espera a lo que dura la sección crítica de la baja. Simulación en pasos de 0,1 ms con tres tareas; no se midió ningún sistema operativo.",
                label_w=430, width=960, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-269
def se269_perdida() -> Fig:
    title = "Posiciones de la interrupción que pierden un incremento en una vuelta de diez instrucciones"
    desc = ("Diagrama de las diez posiciones en que una interrupción puede caer en una vuelta del bucle (load, add, store y siete instrucciones más): sin protección, las posiciones 1 y 2, antes de add y antes de store, pierden el incremento de la rutina, el 9,9 por ciento en 300 corridas; "
            "con una sección crítica que enmascara las interrupciones entre load y store ninguna posición pierde y la rutina se retrasa como máximo dos instrucciones.")
    width = 940
    f, y = _kit_start(title, desc, width, [("La interrupción cae aquí y se pierde su incremento", "coral", "bar"),
                                           ("Sin pérdida", "teal", "bar"), ("Interrupción diferida hasta salir de la sección crítica", "gold", "bar")])
    lw = 270
    x0 = 14 + lw + 10
    cw = (width - 20 - x0) / 10
    f.text(x0 + cw * 5, y + 14, "Posición de la interrupción: justo antes de la instrucción", 13, "middle", 400, AXIS)
    y += 26
    names = ["load", "add", "store"] + ["otra"] * 7
    for i, name in enumerate(names):
        f.text(x0 + cw * i + cw / 2, y + 13, f"{i} · {name}", 13, "middle", 700, INK)
    y += 24
    lanes = [("Sin protección: 2 de 10 posiciones pierden el incremento (9,9 % de los incrementos perdidos)",
              [("pierde" if i in (1, 2) else "ok", "coral" if i in (1, 2) else "teal") for i in range(10)]),
             ("Sección crítica entre load y store: 0 de 10 pierden; la rutina espera como máximo 2 instrucciones",
              [("difiere" if i in (1, 2) else "ok", "gold" if i in (1, 2) else "teal") for i in range(10)])]
    row_h = 64
    _row_labels(f, [lab for lab, _ in lanes], 14 + lw, y, row_h, lw, 700)
    for r, (_, cells) in enumerate(lanes):
        ry = y + r * row_h
        for i, (label, kind) in enumerate(cells):
            f.parts.append(f'<rect x="{x0 + cw * i + 2:g}" y="{ry + 8:g}" width="{cw - 4:g}" height="{row_h - 16:g}" rx="5" fill="{FILL[kind]}"/>')
            f.text(x0 + cw * i + cw / 2, ry + row_h / 2 + 4.5, label, 13, "middle", 700, "#ffffff")
    return _kit_finish(f, y + row_h * 2 + 6,
                       "El defecto solo existe en dos de diez posiciones, de modo que una prueba corta casi nunca lo ve. Enumerar las posiciones lo encuentra siempre. La sección crítica cuesta latencia de la rutina: acota esa espera o cambia a una estructura sin bloqueo. Modelo de instrucciones, no de un procesador concreto.",
                       "gold", SINT)


def se269_lectura() -> Fig:
    return timeline(
        "Lectura partida de un valor de 16 bits: la interrupción cae entre las dos lecturas",
        "Línea de tiempo de una lectura rota: el programa principal lee el byte alto, la interrupción escribe el byte alto y luego el bajo del valor incrementado, y el programa lee el byte bajo; une así un byte alto de antes con un byte bajo de después. En 400 000 lecturas simuladas se rompen 66, el 0,017 por ciento, todas con más de 100 cuentas de error y un máximo de 256.",
        [("Programa principal", [(0, 1, "lee el byte alto", "teal"), (3, 4, "lee el byte bajo", "teal")]),
         ("Interrupción", [(1, 2, "escribe el alto", "coral"), (2, 3, "escribe el bajo", "coral")])],
        unit="Orden de las operaciones (sin escala de tiempo)", ticks=[0, 1, 2, 3, 4, 5], t_max=5,
        events=[(1, "la interrupción cae entre las dos lecturas"), (4, "resultado: alto viejo y bajo nuevo")],
        lane_h=56, label_w=170,
        note="Una lectura rota ocurre una vez cada 5000 (0,017 % observado frente a 0,0195 % esperado, 1/20 × 1/256) y casi nunca se ve en pruebas, pero cuando ocurre el error es de 256 cuentas, no de 1. Se evita con una sección crítica, leyendo dos veces hasta que coincidan, o con un número de secuencia. La mitigación no se midió: es una idealización.",
        note_kind="coral", foot=SINT)


def se269_buffer() -> Fig:
    items = [
        ("Capacidad de 8 muestras", 27.31, "coral", "27,31 %"),
        ("16 muestras", 11.09, "gold", "11,09 %"),
        ("32 muestras", 6.45, "gold", "6,45 %"),
        ("64 muestras", 0.2, "teal", "0,2 %"),
        ("128 muestras", 0.0, "teal", "0,0 %"),
    ]
    return bars("Muestras perdidas por un búfer circular entre una ISR y un bucle con paradas",
                "Barras: con una interrupción que produce 0,5 muestras por milisegundo y un bucle principal que vacía el búfer cada 15 milisegundos con paradas ocasionales de 100, un búfer de 8 muestras pierde el 27,31 por ciento, uno de 16 el 11,09, uno de 32 el 6,45, uno de 64 el 0,2 y uno de 128 ninguna.",
                items, 10, "El tamaño necesario lo fija la parada más larga del bucle, no su período habitual: cada 100 ms de parada acumulan 50 muestras. Un búfer que alcanza para el caso típico pierde datos justo cuando el sistema está ocupado. Modelo de 60 000 muestras por capacidad.",
                label_w=300, width=900, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-270
def se270_qos() -> Fig:
    return grouped_bars(
        "Garantías de entrega sobre un enlace con pérdida (20 000 mensajes, hasta 5 envíos)",
        "Barras agrupadas con el porcentaje de mensajes que no llegan y de duplicados según el nivel de garantía y la pérdida del enlace: con pérdida del 10 por ciento el nivel 0 no entrega el 9,96 por ciento, el nivel 1 duplica el 10,01 y el nivel 2 ni pierde ni duplica; con 30 por ciento el nivel 1 duplica el 29,58, y la garantía más fuerte cuesta de 1,00 a 6,59 paquetes por mensaje.",
        ["10 % · nivel 0\n1,00 paq./msj.", "10 % · nivel 1\n2,35 paq./msj.", "10 % · nivel 2\n4,69 paq./msj.",
         "30 % · nivel 0\n1,00 paq./msj.", "30 % · nivel 1\n3,37 paq./msj.", "30 % · nivel 2\n6,59 paq./msj."],
        [("No llegó", [9.96, 0.0, 0.0, 29.27, 0.16, 0.24], "coral"), ("Duplicados", [0.0, 10.01, 0.0, 0.0, 29.58, 0.0], "gold")],
        unit="% de los 20 000 mensajes", decimals=2, plot_h=260,
        note="Cada nivel compra una garantía con paquetes: el 2 no duplica y cuesta cuatro o seis veces el nivel 0. Con 30 % de pérdida el 6,67 % de los mensajes del nivel 2 llega y el emisor no lo sabe (agotó los reintentos). Simulación del protocolo, no de un agente MQTT real.",
        note_kind="gold", foot=SINT)


def se270_cola() -> Fig:
    items = [
        ("Cola de 5 muestras (latencia máxima 4 min)", 17.53, "coral", "17,53 %"),
        ("15 muestras (14 min)", 12.5, "coral", "12,5 %"),
        ("30 muestras (29 min)", 7.45, "gold", "7,45 %"),
        ("60 muestras (56 min)", 2.68, "gold", "2,68 %"),
        ("120 muestras (82 min)", 0.25, "teal", "0,25 %"),
        ("240 muestras (85 min)", 0.01, "teal", "0,01 %"),
    ]
    return bars("Muestras perdidas por día según la capacidad de la cola de almacenar y reenviar",
                "Barras: con una muestra por minuto y desconexiones de media 30 minutos, una cola de 5 muestras pierde el 17,53 por ciento del día, una de 30 el 7,45, una de 120 el 0,25 y una de 240 el 0,01; la latencia máxima de los datos reenviados crece de 4 a 85 minutos.",
                items, 25, "Más cola pierde menos datos pero los entrega más tarde: la capacidad se elige por la desconexión más larga que se quiere cubrir y por cuánto vale un dato viejo. Las desconexiones geométricas de media 30 min, 400 días simulados por capacidad, son un supuesto.",
                label_w=470, width=1010, note_kind="gold", foot=SINT)


def se270_tormenta() -> Fig:
    return grouped_bars(
        "Dispositivos conectados a los 900 s tras una caída de 5000 (servidor: 200 intentos por segundo)",
        "Barras horizontales con los dispositivos conectados a los 900 segundos tras una caída que termina a la vez: con reintento fijo cada 5 segundos y con espera exponencial con jitter completo están los 5000 (todos conectados en 245 y en 169 segundos); con espera exponencial sin jitter solo 691, porque los reintentos siguen sincronizados.",
        ["Fijo cada 5 s (todos conectados en 245 s)", "Exponencial sin jitter (no termina)", "Exponencial con jitter completo (todos en 169 s)"],
        [("Conectados a los 900 s", [5000, 691, 5000], "teal")],
        unit="Dispositivos conectados a los 900 s (de 5 000)", horizontal=True, label_w=300, ticks=[0, 1000, 2000, 3000, 4000, 5000],
        note="El pico del primer segundo es el mismo en las tres políticas (5 000 intentos) porque todas empiezan a la vez. Sin jitter, la espera exponencial mantiene a todos los dispositivos en las mismas olas: el servidor se satura en cada una. El jitter reparte los intentos en el tiempo. El colapso de la capacidad por encima de 1,5 veces la carga admisible es un supuesto del modelo.",
        note_kind="coral", foot=SINT)


FIGURES = {
    "se-265-latencia-segun-la-arquitectura.svg": se265_latencia,
    "se-265-acumulador-de-16-bits.svg": se265_acumulador,
    "se-265-mutantes-de-un-antirrebote.svg": se265_antirrebote,
    "se-266-eficiencia-de-un-bus.svg": se266_bus,
    "se-266-errores-no-detectados.svg": se266_codigos,
    "se-266-sobremuestreo-de-un-adc.svg": se266_adc,
    "se-267-vida-de-una-pila.svg": se267_bateria,
    "se-267-desgaste-de-la-flash.svg": se267_flash,
    "se-267-filtro-con-enteros.svg": se267_filtro,
    "se-268-planificabilidad-rate-monotonic.svg": se268_rm,
    "se-268-plazos-incumplidos.svg": se268_plazos,
    "se-268-inversion-de-prioridad.svg": se268_inversion,
    "se-269-incrementos-perdidos.svg": se269_perdida,
    "se-269-lectura-rota-de-16-bits.svg": se269_lectura,
    "se-269-buffer-circular.svg": se269_buffer,
    "se-270-garantias-de-entrega.svg": se270_qos,
    "se-270-cola-de-almacenar-y-reenviar.svg": se270_cola,
    "se-270-tormenta-de-reconexion.svg": se270_tormenta,
}
