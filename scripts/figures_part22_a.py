"""Figures for SE-265 to SE-270 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-265
def se265_latencia() -> Fig:
    rows = [
        ["Sondeo del botón en el bucle principal", "14,19", "78,2", "166,0"],
        ["Interrupción con manejo inmediato", "0,025", "0,03", "0,03"],
    ]
    return tab("Latencia de un botón según la arquitectura del firmware (milisegundos)",
               "Tabla: en un bucle principal con sensor, pantalla y un envío de radio cada diez vueltas, un botón consultado por sondeo tarda 14,19 milisegundos de media, 78,2 en el percentil 99 y 166,0 en el peor caso; con una interrupción de manejo inmediato tarda unos 0,03.",
               ["Arquitectura", "Media", "Percentil 99", "Máximo"], rows, [430, 150, 170, 150], row_h=44, size=13,
               note="La latencia del sondeo no depende del botón sino de lo más lento que haga el bucle: una vuelta con radio dura unos 50 ms. La interrupción cambia el problema de sitio: ahora hay que acotar lo que hace dentro de la rutina. Las duraciones del bucle son supuestos del autor.",
               note_kind="gold", foot=SINT)


def se265_acumulador() -> Fig:
    rows = [
        ["4, 8, 16 o 17 lecturas", "0 %", "0 %", "—"],
        ["32 lecturas", "0 %", "100 %", "2 048"],
        ["64 lecturas", "10,0 %", "100 %", "1 024 y 2 048"],
    ]
    return tab("Promedio de lecturas de 12 bits con un acumulador de 16 bits",
               "Tabla: al promediar lecturas de 12 bits con un acumulador de 16 bits, con una señal media de 1000 no falla nada hasta 32 lecturas y con 64 falla el 10 por ciento; con una señal media de 3000 falla el 100 por ciento desde 32 lecturas, con un error de 2048 cuentas.",
               ["Número de lecturas", "Señal media 1000", "Señal media 3000", "Error medio (cuentas)"], rows, [300, 200, 200, 240], row_h=44, size=13,
               note="El desbordamiento no avisa: el promedio sale plausible y erróneo en 2048 cuentas, la mitad del rango del convertidor. Depende del producto del número de lecturas por el máximo posible, no de la señal típica. Sobre 20 000 ventanas por celda, señal con ruido gaussiano de 150 cuentas.",
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
    rows = [
        ["1", "39", "20,5 %", "97,5", "50,0 %"],
        ["2", "48", "33,3 %", "120,0", "66,7 %"],
        ["6", "84", "57,1 %", "210,0", "85,7 %"],
        ["16", "174", "73,6 %", "435,0", "94,1 %"],
        ["64", "606", "84,5 %", "1 515,0", "98,5 %"],
    ]
    return tab("Leer N bytes de un registro: ciclos de reloj, eficiencia y tiempo en I²C",
               "Tabla: leer un byte de un registro por I2C cuesta 39 ciclos de reloj y la eficiencia de datos es de 20,5 por ciento; con 64 bytes sube a 84,5 por ciento; a 400 kilohercios el primer caso tarda 97,5 microsegundos; por SPI las eficiencias son 50 y 98,5 por ciento.",
               ["Bytes", "Ciclos I²C", "Eficiencia I²C", "Tiempo a 400 kHz (µs)", "Eficiencia SPI"], rows, [110, 170, 200, 270, 190], row_h=40, size=13,
               note="La eficiencia mide bits útiles sobre ciclos de reloj, no la velocidad del bus: con direcciones, confirmaciones y reinicio, leer un solo byte desperdicia cuatro de cada cinco ciclos. El cálculo es aritmético, sin dispositivo real ni capacitancia de la línea.",
               note_kind="gold", foot=SINT)


def se266_codigos() -> Fig:
    rows = [
        ["Un bit invertido", "0", "0", "0"],
        ["Dos bits invertidos", "200 000", "12 445", "0"],
        ["Tres bits invertidos", "0", "2 143", "0"],
        ["Ráfaga de hasta 8 bits", "99 238", "0", "0"],
    ]
    return tab("Errores no detectados de 200 000 tramas de 8 bytes según el código de control",
               "Tabla: de 200 000 tramas con errores de bits, la paridad no detecta ninguno con dos bits invertidos ni la mitad de las ráfagas; la suma de 8 bits deja pasar 12 445 con dos bits y 2 143 con tres; el CRC-8 de polinomio 0x07 no deja pasar ninguno en estos casos.",
               ["Error inyectado", "Paridad", "Suma de 8 bits", "CRC-8"], rows, [300, 190, 220, 170], row_h=44, size=13,
               note="El CRC-8 detecta toda ráfaga de hasta ocho bits y toda combinación de uno a tres bits en tramas tan cortas, pero deja pasar errores más largos o más numerosos en la proporción de 1 entre 256. Las tramas, los errores y la semilla son sintéticos: no se midió ningún bus real.",
               note_kind="teal", foot=SINT)


def se266_adc() -> Fig:
    rows = [
        ["0,0 (sin ruido)", "0,431", "0,431", "0,431", "0,431", "0,431"],
        ["0,5", "0,583", "0,289", "0,145", "0,071", "0,036"],
        ["1,0", "1,031", "0,520", "0,259", "0,128", "0,065"],
    ]
    return tab("Error eficaz (en LSB) de un ADC de 10 bits al promediar N lecturas",
               "Tabla: al promediar cuatro, dieciséis, sesenta y cuatro o doscientas cincuenta y seis lecturas, el error eficaz baja a la mitad por cada factor cuatro de sobremuestreo cuando hay ruido de 0,5 o 1,0 LSB, y no baja nada, 0,431, cuando no hay ruido.",
               ["Ruido (σ en LSB)", "N = 1", "4", "16", "64", "256"], rows, [250, 130, 130, 130, 130, 130], row_h=44, size=13,
               note="Sobremuestrear mejora la resolución solo si hay un poco de ruido que la reparta: sin ruido todas las lecturas redondean igual y el promedio no mejora. Cada factor cuatro cuesta cuatro veces más tiempo y energía. Señal constante de 1,2345 V con referencia de 3,3 V.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-267
def se267_bateria() -> Fig:
    rows = [
        ["10 s", "198", "197", "191", "166"],
        ["60 s", "1 135", "1 098", "943", "538"],
        ["600 s", "7 650", "6 222", "3 219", "901"],
    ]
    return tab("Vida de una pila de 2400 mAh (días) según el periodo y la corriente de reposo",
               "Tabla: con una pila de 2400 miliamperios hora y un nodo que despierta cada diez segundos la vida es de 198 días con una corriente de reposo de 2 microamperios y 166 con 100; despertando cada 600 segundos va de 7650 a 901 días, de modo que el reposo domina cuando el nodo despierta poco.",
               ["Periodo", "Reposo 2 µA", "5 µA", "20 µA", "100 µA"], rows, [190, 220, 180, 180, 180], row_h=44, size=13,
               note="Con un despertar cada 10 s la corriente de reposo apenas cuenta: manda lo que se gasta despierto. Con 600 s, pasar de 2 a 100 µA divide la vida por 8,5. Supuestos: 15 mA durante 120 ms y 80 mA durante 40 ms de radio, autodescarga del 1 % anual, sin envejecimiento ni temperatura.",
               note_kind="gold", foot=SINT)


def se267_flash() -> Fig:
    rows = [
        ["Sobrescribir siempre el mismo sector", "200 000", "0,062", "6,9 días"],
        ["Rotar entre los sectores libres", "25 000", "0,500", "—"],
        ["Rotar entre todos, moviendo los datos fríos", "12 500", "1,000", "—"],
    ]
    return tab("Desgaste de una flash de 16 sectores tras 200 000 escrituras (mitad de los datos fríos)",
               "Tabla: tras 200 000 escrituras, sobrescribir el mismo sector lo borra 200 000 veces y deja una vida relativa de 0,062; rotar solo entre los sectores libres lo deja en 0,5 con 25 000 borrados por sector; moverse entre todos los sectores, incluidos los de datos fríos, llega a 1,0.",
               ["Política", "Borrados del sector más usado", "Vida relativa al ideal", "Vida a 1 registro por minuto"], rows, [420, 240, 200, 200], row_h=52, size=13,
               note="Con 64 sectores de 4 KiB, registros de 16 B y 10 000 borrados por sector, un registro por minuto da 6,9 días si se sobrescribe un solo sector y unos 312 años con un registro circular. La segunda cifra ignora otros límites (retención de datos, tensión): es un techo teórico.",
               note_kind="coral", foot=SINT)


def se267_filtro() -> Fig:
    rows = [
        ["2", "3", "1", "0", "2"],
        ["4", "15", "7", "0", "8"],
        ["6", "63", "31", "0", "23 a 32"],
    ]
    return tab("Filtro y += (x − y) >> k con enteros: error final en cuentas de 10 bits",
               "Tabla: un filtro de paso bajo con enteros se queda a 3, 15 y 63 cuentas de la entrada subiendo con k igual a 2, 4 y 6 si se trunca, y a 1, 7 y 31 si se redondea; bajando, el truncado converge exactamente y el redondeado se queda a entre 2 y 32 cuentas; con coma flotante el error es cero.",
               ["k", "Truncado subiendo", "Redondeado subiendo", "Truncado bajando", "Redondeado bajando"], rows, [90, 230, 240, 220, 240], row_h=44, size=13,
               note="El truncado tiene una zona muerta de 2^k − 1 cuentas hacia arriba: el filtro «converge» sin llegar a la entrada y el sesgo es asimétrico. Redondear reduce la zona a la mitad y la mueve. Con k = 6 y entradas de 10 bits, 63 cuentas son un 6 % del rango.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-268
def se268_rm() -> Fig:
    rows = [
        ["3", "0,780", "100 %", "100 %", "92,5 %", "73,0 %"],
        ["5", "0,743", "100 %", "100 %", "89,3 %", "62,5 %"],
        ["8", "0,724", "100 %", "100 %", "88,8 %", "49,7 %"],
    ]
    return tab("Conjuntos de tareas rate-monotonic planificables según la utilización (análisis exacto)",
               "Tabla: con tres, cinco u ocho tareas, todos los conjuntos de utilización 0,6 a 0,8 son planificables por prioridades por periodo, aunque la cota de Liu y Layland sea 0,78, 0,743 y 0,724; con utilización 0,9 lo son entre 88,8 y 92,5 por ciento y con 0,95 entre 49,7 y 73,0 por ciento.",
               ["Tareas", "Cota Liu y Layland", "U = 0,7", "U = 0,8", "U = 0,9", "U = 0,95"], rows, [120, 240, 130, 130, 130, 150], row_h=44, size=13,
               note="La cota es suficiente pero no necesaria: por debajo de ella siempre se cumple y por encima a veces. Con U = 0,8 todos los conjuntos sintéticos pasan aunque 0,8 supere la cota. El análisis exacto de tiempo de respuesta decide cada caso; 2000 conjuntos por celda, periodos entre 10 y 1000.",
               note_kind="teal", foot=SINT)


def se268_plazos() -> Fig:
    rows = [
        ["0,5", "0,0 %", "0,7 %", "9,7 %"],
        ["0,7", "0,01 %", "11,2 %", "32,3 %"],
        ["0,9", "17,0 %", "55,6 %", "72,4 %"],
    ]
    return tab("Plazos incumplidos de una tarea periódica según la variabilidad del tiempo de ejecución",
               "Tabla: una tarea con periodo y plazo de 10 milisegundos y tiempo medio de ejecución del 50 por ciento del periodo incumple el 0,0 por ciento de los plazos con poca variabilidad y el 9,7 con mucha; con utilización media 0,9 incumple entre 17,0 y 72,4 por ciento.",
               ["Utilización media", "σ = 0,1", "σ = 0,3", "σ = 0,6"], rows, [260, 190, 190, 190], row_h=44, size=13,
               note="Con utilización media de 0,7 y σ = 0,3 se incumple un plazo de cada nueve, aunque la media quepa con holgura. El tiempo medio no sirve para decidir si se cumple un plazo: hace falta el peor caso o un percentil alto. 200 000 trabajos por celda, tiempos lognormales y trabajos encadenados.",
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
    rows = [
        ["Sin protección", "2 de 10", "9,9 %", "0"],
        ["Sección crítica con interrupciones enmascaradas", "0 de 10", "0,0 %", "2"],
    ]
    return tab("Incrementos de una ISR perdidos al compartir un contador con el bucle principal",
               "Tabla: al enumerar las diez posiciones en que una interrupción puede caer dentro de una vuelta de un bucle que lee, suma y escribe un contador, dos posiciones pierden el incremento de la rutina, y en 300 corridas se pierde el 9,9 por ciento; con una sección crítica no se pierde ninguno y la rutina se retrasa como máximo dos instrucciones.",
               ["Estrategia", "Posiciones con pérdida", "Incrementos perdidos", "Retraso máximo de la ISR (instrucciones)"], rows, [430, 190, 200, 240], row_h=52, size=13,
               note="El defecto solo existe en dos de diez posiciones, de modo que una prueba corta casi nunca lo ve. Enumerar las posiciones lo encuentra siempre. La sección crítica cuesta latencia de la rutina: acota esa espera o cambia a una estructura sin bloqueo. Modelo de instrucciones, no de un procesador concreto.",
               note_kind="gold", foot=SINT)


def se269_lectura() -> Fig:
    rows = [
        ["Lecturas simuladas", "400 000"],
        ["Lecturas rotas", "66 (0,017 %)"],
        ["Lecturas rotas con error mayor que 100", "66 (todas)"],
        ["Error máximo", "256 cuentas"],
        ["Frecuencia esperada: 1/20 × 1/256", "0,0195 %"],
    ]
    return tab("Lectura de un valor de 16 bits en un micro de 8 bits con una ISR que lo incrementa",
               "Tabla: de 400 000 lecturas de un valor de 16 bits que una interrupción incrementa escribiendo primero el byte alto y luego el bajo, 66 resultan rotas, el 0,017 por ciento; todas con un error de más de 100 cuentas y un máximo de 256, porque solo se rompe cuando el incremento cruza un límite de byte.",
               ["Medida", "Resultado"], rows, [520, 280], row_h=40, size=13,
               note="Una lectura rota ocurre una vez cada 5000 y casi nunca se ve en pruebas, pero cuando ocurre el error es de 256 cuentas, no de 1. Se evita con una sección crítica, leyendo dos veces hasta que coincidan, o con un número de secuencia. La mitigación no se midió: es una idealización.",
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
    rows = [
        ["10 %", "0", "9,96 %", "0 %", "1,00"],
        ["10 %", "1", "0,0 %", "10,01 %", "2,35"],
        ["10 %", "2", "0,0 %", "0 %", "4,69"],
        ["30 %", "0", "29,27 %", "0 %", "1,00"],
        ["30 %", "1", "0,16 %", "29,58 %", "3,37"],
        ["30 %", "2", "0,24 %", "0 %", "6,59"],
    ]
    return tab("Garantías de entrega sobre un enlace con pérdida (20 000 mensajes, hasta 5 envíos)",
               "Tabla: con pérdida del 10 por ciento por sentido, un nivel 0 no entrega el 9,96 por ciento, el nivel 1 entrega siempre pero duplica el 10,01 por ciento y usa 2,35 paquetes por mensaje, y el nivel 2 no duplica y usa 4,69; con pérdida del 30 por ciento el nivel 1 duplica el 29,58 y el 2 deja el 6,67 por ciento sin que el emisor lo sepa.",
               ["Pérdida", "Nivel", "No llegó", "Duplicados", "Paquetes por mensaje"], rows, [150, 120, 190, 200, 270], row_h=40, size=13,
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
    rows = [
        ["Fijo cada 5 s", "5 000", "245 s", "5 000"],
        ["Exponencial sin jitter", "5 000", "no termina", "691"],
        ["Exponencial con jitter completo", "5 000", "169 s", "5 000"],
    ]
    return tab("Reconexión de 5000 dispositivos tras una caída (servidor admite 200 intentos por segundo)",
               "Tabla: tras una caída que termina a la vez, con reintento fijo cada 5 segundos todos se conectan en 245 segundos, con espera exponencial sin jitter solo 691 de 5000 están conectados a los 900 segundos porque los reintentos siguen sincronizados, y con jitter completo se conectan todos en 169 segundos.",
               ["Política de reintento", "Pico en el primer segundo", "Todos conectados en", "Conectados a los 900 s"], rows, [380, 220, 210, 200], row_h=44, size=13,
               note="Sin jitter, la espera exponencial mantiene a todos los dispositivos en las mismas olas: el servidor se satura en cada una. El jitter reparte los intentos en el tiempo. El colapso de la capacidad por encima de 1,5 veces la carga admisible es un supuesto del modelo.",
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
