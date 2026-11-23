"""Figures for SE-283 to SE-288 (secure hardware logic, quantum simulation, post-quantum cryptography, zero trust, a hostile-behaviour workshop and an isolated-execution platform: code run on Windows 11 with CPython 3.12.9, NumPy 2.5.5, wasmtime 50.0.1, kyber-py 1.2.0 and dilithium-py 1.5.1; no language model was invoked)."""
from __future__ import annotations

import math

from figure_kit import Fig, dumbbell, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars

from figures_part45_a import flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9; los recuentos se repiten y los tiempos varían de una ejecución y de un equipo a otro."
MODELO = "Modelo con parámetros del autor y semilla fija 48; muestra un mecanismo, no mide un sistema real."
SIMULADO = "Simulación clásica con NumPy: no hubo acceso a ningún ordenador cuántico ni se ejecutó ningún SDK de proveedor."
SIN_TEE = "Lógica de medición y cita con SHA-256 y HMAC de la biblioteca estándar: no se ejecutó ningún entorno de ejecución confiable ni TPM."


# ---------------------------------------------------------------- SE-283
def se583_cita_y_desafio() -> Fig:
    return heatmap(
        "Qué acepta el verificador: tres escenarios de cita con y sin desafío fresco",
        "Mapa de calor con tres escenarios y dos condiciones: una cita legítima se acepta con y sin desafío, la de la cadena alterada se rechaza con desafío fresco y una cita vieja reproducida se acepta sin desafío y se rechaza con desafío fresco.",
        ["Cita legítima del estado correcto", "Cita de la cadena alterada", "Cita vieja de un estado bueno, reproducida"], ["Sin desafío fresco", "Con desafío fresco"],
        [[1, 1], [None, 0], [1, 0]], unit="se acepta", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "se acepta" if v else "se rechaza", cell_h=58, label_w=290,
        note="Solo la fila de la cita reproducida cambia con la columna: sin desafío, una cita vieja de un estado bueno se acepta aunque el nodo ya esté alterado. La cita de la cadena alterada solo se probó con desafío fresco (la celda vacía no se midió). Es una simulación con HMAC y una clave generada al azar, no hardware.",
        note_kind="gold", foot=SIN_TEE)


def se583_que_detecta() -> Fig:
    return stacked_bars(
        "Nodos mal en una flota de 1 000: cuántos detecta la atestación de arranque",
        "Barras apiladas horizontales con los 39 nodos mal de una flota de 1000: 7 con el arranque alterado, que la atestación detecta, y 32 explotados en ejecución con el software legítimo, que la atestación de arranque no detecta.",
        ["Flota de 1 000 nodos: 39 mal"],
        [("Arranque alterado: detectados", [7], "teal"), ("Explotados en ejecución: no detectados", [32], "coral")],
        unit="Nodos mal", horizontal=True, decimals=0, label_w=210,
        note="La atestación de arranque detecta 7 de 39 (18 %): los explotados en ejecución con el software legítimo no cambian la medición. Los porcentajes (1 % alterado en el arranque y 3 % explotado en ejecución, semilla 48) son supuestos del autor; el patrón, no. Una atestación demuestra qué código se cargó, no que ese código sea seguro.",
        note_kind="coral", foot=MODELO)


def se583_decisiones_del_verificador() -> Fig:
    return flow(
        "Las cuatro decisiones del verificador antes de liberar la clave de datos",
        "Diagrama de cuatro cajas encadenadas: verificar la firma de la cita con la clave del hardware, comprobar que el desafío es el propio, comparar la medición con un valor de referencia aceptado y liberar la clave de datos solo si las tres comprobaciones pasan; una nota advierte que el valor de referencia debe venir de un canal independiente.",
        [[("1. Firma\nLa cita está firmada por una clave del hardware que el fabricante certificó", "teal"),
          ("2. Frescura\nEl desafío que contiene es el que el verificador acaba de enviar", "gold"),
          ("3. Medición\nCoincide con un valor de referencia aceptado y vigente", "gold"),
          ("4. Liberar\nSolo si pasan las tres, se entrega la clave de datos", "coral")]],
        note="El valor de referencia debe venir de un canal independiente del atestador (el proceso de construcción, firmado) y la lista de versiones aceptadas necesita un dueño y un plan para retirar las vulnerables. Se omiten la validación de la cadena de certificados y la revocación, que son parte de cualquier despliegue real.",
        note_kind="teal", box_h=118, foot="Diagrama conceptual basado en RFC 9334; no es una medición.")


# ---------------------------------------------------------------- SE-284
def se584_costo_de_simular() -> Fig:
    nq = [10, 14, 18, 20, 22, 24]
    return line_chart(
        "Tiempo de aplicar la puerta H a todos los qubits en un simulador de vector de estado, según el número de qubits",
        "Líneas en escala logarítmica con el tiempo de aplicar la puerta H a todos los qubits de un simulador de vector de estado: 1,1 milisegundos con 10 qubits, 11 con 14, 294 con 18, 862 con 20, 4712 con 22 y 14309 con 24; la memoria del vector pasa de 0,02 a 256 MiB.",
        [("Tiempo", list(zip(nq, [1.1, 11.0, 293.8, 861.8, 4711.7, 14309.3])), "navy")],
        x_label="Qubits", y_label="Milisegundos (escala logarítmica)", log_y=True, x_ticks=[(k, str(k)) for k in nq], y_ticks=[1, 10, 100, 1000, 10000], point_labels="all", decimals=1, plot_h=290,
        note="Cada dos qubits más, la memoria se multiplica por 4 (de 0,02 MiB con 10 qubits a 256 MiB con 24) y el tiempo por entre 4 y 16. Extrapolado aritméticamente, no medido: 50 qubits necesitarían 16 PiB solo para el vector. NumPy con tensordot y sin optimizar: un simulador especializado llega más lejos con la misma pendiente exponencial.",
        note_kind="gold", foot=SIMULADO)


def _grover(n: int, k: int) -> float:
    theta = math.asin(1 / math.sqrt(2 ** n))
    return math.sin((2 * k + 1) * theta) ** 2


def se584_grover() -> Fig:
    k4 = list(range(0, 9))
    k8 = list(range(0, 25, 3))
    return line_chart(
        "Probabilidad de medir el elemento buscado según las iteraciones de Grover, para 4 y para 8 qubits",
        "Líneas con la probabilidad de medir el elemento buscado según las iteraciones de Grover para 4 y 8 qubits: con 4 qubits sube a 0,96 con 3 iteraciones y cae por debajo de 0,1 con 6; con 8 qubits alcanza 0,9999 con 12 iteraciones y cae a 0,006 con 24.",
        [("4 qubits (16 elementos)", [(k, round(_grover(4, k), 4)) for k in k4], "coral"),
         ("8 qubits (256 elementos)", [(k, round(_grover(8, k), 4)) for k in k8], "teal")],
        x_label="Iteraciones de Grover", y_label="Probabilidad de acertar", x_ticks=[(k, str(k)) for k in (0, 3, 6, 9, 12, 15, 18, 21, 24)], y_ticks=[0, 0.25, 0.5, 0.75, 1.0], point_labels="none", decimals=2, plot_h=290,
        note="El óptimo está cerca de (π/4)·√N: 3 iteraciones con 16 elementos y 12 con 256. Con el doble de iteraciones la probabilidad cae (0,02 con 6 y 4 qubits; 0,006 con 24 y 8): la amplificación es una rotación y se puede pasar de largo. Fórmula exacta para un elemento marcado y sin ruido; la simulación del laboratorio da los mismos valores salvo redondeo.",
        note_kind="teal", foot=SIMULADO)


def se584_ruido_ghz() -> Fig:
    return heatmap(
        "Porcentaje de mediciones correctas de un estado GHZ según el número de qubits y la probabilidad de error por puerta",
        "Mapa de calor con el porcentaje de mediciones correctas de un estado GHZ según el número de qubits y la probabilidad de error por puerta: con 0,001 está entre 99,6 y 100 por ciento, con 0,01 baja de 99,8 a 95,7 y con 0,05 baja de 97,2 a 79,5 al pasar de 2 a 10 qubits.",
        ["2 qubits", "4 qubits", "6 qubits", "8 qubits", "10 qubits"], ["Error 0,001", "Error 0,01", "Error 0,05"],
        [[100.0, 99.8, 97.2], [99.7, 98.7, 92.1], [99.7, 97.5, 88.8], [99.8, 96.5, 83.8], [99.6, 95.7, 79.5]],
        unit="% correctas", scale="teal", vmin=75, vmax=100, decimals=1, suffix=" %", cell_h=44, label_w=130,
        note="El efecto se acumula con el número de puertas y con la probabilidad de error: con 10 qubits y error de 0,05, una de cada cinco mediciones es incorrecta. El modelo cuenta solo la medición inmediata (4 000 repeticiones por celda, semilla 48) y subestima el daño en algoritmos que interfieren, donde los errores de fase destruyen justo la cancelación que se necesita.",
        note_kind="gold", foot=SIMULADO)


# ---------------------------------------------------------------- SE-285
def se585_tamanos() -> Fig:
    return grouped_bars(
        "Tamaño en bytes de claves públicas y de firmas o textos cifrados en algoritmos clásicos y poscuánticos",
        "Barras agrupadas en escala logarítmica con el tamaño en bytes de la clave pública y de la firma o texto cifrado: X25519 32 y 32, Ed25519 32 y 64, ML-KEM-768 1184 y 1088, ML-DSA-65 1952 y 3309 y la firma de Lamport con SHA-256 16384 y 8192.",
        ["X25519", "Ed25519", "ML-KEM-768", "ML-DSA-65", "Lamport (SHA-256)"],
        [("Clave pública", [32, 32, 1184, 1952, 16384], "navy"), ("Firma, texto cifrado o valor intercambiado", [32, 64, 1088, 3309, 8192], "coral")],
        unit="Bytes (escala logarítmica)", log=True, decimals=0, plot_h=290, width=1000,
        note="Una firma de ML-DSA-65 es unas 52 veces mayor que una de Ed25519 y una clave pública de ML-KEM-768 unas 37 veces mayor que la de X25519. En un saludo, el intercambio pasa de 64 bytes (un segmento) a 2 272 con ML-KEM-768 y a 2 336 con el híbrido (dos segmentos de 1 460). Para X25519 se muestra el valor de 32 bytes que cada lado envía. La firma de Lamport es una ilustración, no un estándar.",
        note_kind="gold", foot=EJEC)


def se585_reutilizar_la_clave() -> Fig:
    ks = [1, 2, 4, 8, 12, 16]
    return line_chart(
        "Probabilidad de falsificar un mensaje nuevo tras k firmas con el mismo par de claves de Lamport",
        "Líneas con la probabilidad de poder falsificar un mensaje nuevo tras k firmas con el mismo par de claves de Lamport: prácticamente cero con 1, 2 y 4 firmas, 0,367 con 8, 0,939 con 12 y 0,996 con 16.",
        [("(1 − 2^−k)^256", [(k, round((1 - 2.0 ** -k) ** 256, 4)) for k in ks], "coral")],
        x_label="Firmas ya emitidas con el mismo par de claves", y_label="Probabilidad de falsificar", x_ticks=[(k, str(k)) for k in ks], y_ticks=[0, 0.25, 0.5, 0.75, 1.0], point_labels="all", decimals=3, plot_h=280,
        note="La curva despega entre 4 y 8 firmas y casi se satura en 16: cada firma revela la mitad de los secretos. La fórmula es el promedio sobre mensajes y firmas al azar; con 8 firmas reales y 300 mensajes nuevos se falsificaron 49 (16,3 %), porque ese conjunto concreto dejó 3 de 512 secretos sin revelar (probabilidad 2⁻³). SLH-DSA evita el problema con un árbol de claves.",
        note_kind="coral", foot=EJEC)


def se585_mosca() -> Fig:
    filas = [("x = 1, y = 3, z = 15", 15, 4), ("x = 15, y = 5, z = 15", 15, 20), ("x = 25, y = 5, z = 15", 15, 30), ("x = 10, y = 8, z = 15", 15, 18), ("x = 30, y = 6, z = 25", 25, 36)]
    return dumbbell(
        "Desigualdad de Mosca en cinco escenarios: años hasta un ordenador cuántico capaz frente a vida del dato más migración",
        "Mancuernas con cinco escenarios: el tiempo hasta el ordenador cuántico supuesto frente a la vida del dato más la migración: 15 frente a 4, 15 frente a 20, 15 frente a 30, 15 frente a 18 y 25 frente a 36 años.",
        filas, unit="Años", names=("z: años hasta un ordenador capaz (supuesto)", "x + y: vida del dato más migración"), decimals=0, label_w=190, lower_is_better=True,
        note="Hay riesgo cuando x + y supera a z: cuatro de los cinco escenarios lo tienen. El cuarto (x = 10, y = 8) muestra que datos de vida media con una migración lenta ya son urgentes. Todos los valores son ejemplos del autor, no pronósticos; la fecha z es la incógnita y se hace un análisis de sensibilidad en lugar de buscar una predicción.",
        note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-286
def se586_casos_del_token() -> Fig:
    return heatmap(
        "Cuatro casos de un token presentado al servicio de calificaciones y las tres comprobaciones que se aplican en orden",
        "Mapa de calor con cuatro casos de un token y tres comprobaciones: el token legítimo pasa firma, vigencia y audiencia; el de otra audiencia falla la audiencia; el vencido falla la vigencia; el de firma alterada falla la firma; cada rechazo lo es por una sola comprobación.",
        ["Token legítimo", "Token para otra audiencia", "Token vencido (seis minutos después)", "Token con la firma alterada"], ["Firma", "Vigencia", "Audiencia"],
        [[0, 0, 0], [0, 0, 1], [0, 1, None], [1, None, None]], unit="resultado", scale="coral", vmin=0, vmax=1,
        cell_fmt=lambda v: "falla" if v else "pasa", cell_h=48, label_w=290,
        note="Las comprobaciones se aplican en orden (firma, vigencia, audiencia) y una vez que una falla las siguientes no se evalúan (guion). Cada propiedad del token tiene un caso que la ejercita. Tokens firmados con HMAC-SHA-256 y una clave compartida: no es OAuth ni SPIFFE, y faltan la revocación, la rotación de claves y la firma asimétrica.",
        note_kind="gold", foot=EJEC)


def se586_radio_de_dano() -> Fig:
    return grouped_bars(
        "Servicios alcanzables con una credencial robada de un servicio al azar entre 200, según la arquitectura",
        "Barras horizontales con los servicios alcanzables con una credencial robada de un servicio al azar entre 200: red plana tras el perímetro 200, segmentada en 5 partes 45 y con credencial limitada por destinatario a 3 dependencias 3.",
        ["Red plana tras el perímetro", "Segmentada en 5 partes", "Credencial limitada a 3 dependencias"],
        [("Servicios alcanzables", [200, 40, 3], "coral")],
        unit="Servicios alcanzables de 200", horizontal=True, decimals=0, label_w=270,
        note="Segmentar divide el radio de daño por el número de segmentos y limitar la credencial por destinatario lo reduce al grado de dependencia del servicio comprometido. Valores del modelo con supuestos del autor (200 servicios, 5 segmentos, 3 dependencias por servicio); en un sistema real el grafo es heterogéneo y los servicios muy conectados alcanzan más.",
        note_kind="teal", foot=MODELO)


def se586_ventana_de_uso_indebido() -> Fig:
    vidas = [5, 60, 480, 43200]
    return line_chart(
        "Ventana media de uso indebido de una credencial robada según su vida, con detección de media 20 minutos",
        "Líneas con la ventana media de uso indebido de una credencial robada según su vida, con detección exponencial de media 20 minutos: 2,3 minutos con vida de 5 minutos, 13,5 con 60, 19,2 con 480 y 20,1 con 30 días.",
        [("Ventana media (minutos)", list(zip(vidas, [2.3, 13.5, 19.2, 20.1])), "teal")],
        x_label="Vida del token en minutos (escala logarítmica)", y_label="Ventana media de uso indebido (minutos)", log_x=True, x_ticks=[(5, "5"), (60, "60"), (480, "480 (8 h)"), (43200, "43 200 (30 días)")],
        y_ticks=[0, 5, 10, 15, 20, 25], point_labels="all", decimals=1, plot_h=280,
        note="Pasar de 8 horas a 5 minutos reduce la ventana de 19,2 a 2,3 minutos; pasar de 30 días a 8 horas casi no cambia nada, porque ya manda la detección (20 minutos de media). Acortar la vida ayuda mientras sea menor que el retraso de detección. La detección exponencial de media 20 minutos y la vida restante uniforme son supuestos del autor.",
        note_kind="coral", foot=MODELO)


# ---------------------------------------------------------------- SE-287
def se587_matriz_de_contencion() -> Fig:
    return heatmap(
        "Seis comportamientos hostiles contra tres formas de ejecutar código ajeno: qué contuvo cada una",
        "Mapa de calor con seis comportamientos hostiles y tres candidatos: el bucle infinito lo contienen el proceso hijo y el módulo de WebAssembly; la bomba de memoria, leer un archivo ajeno y abrir una conexión de red solo el módulo; leer el entorno el proceso hijo y el módulo; la introspección la hace inocua el módulo; el exec sin funciones integradas no contiene ninguno de los probados.",
        ["Bucle infinito", "Bomba de memoria", "Leer un archivo ajeno", "Leer el entorno del servicio", "Abrir una conexión de red", "Escapar por introspección"],
        ["exec sin funciones integradas", "Proceso hijo con entorno vacío", "Módulo de WebAssembly"],
        [[None, 1, 1], [None, 0, 1], [None, 0, 1], [0, 1, 1], [None, 0, 1], [0, None, 1]], unit="contuvo", scale="teal", vmin=0, vmax=1,
        cell_fmt=lambda v: "contuvo" if v else "no contuvo", cell_h=44, label_w=250,
        note="Ninguna columna contiene todo salvo el módulo, que lo logra porque no puede expresar esas operaciones y solo ejecuta código compilado a Wasm. El proceso hijo contiene el bucle y el entorno, no la memoria, los archivos ni la red. El guion es «no se ejecutó» (el bucle y la memoria en el mismo proceso no se pueden probar sin colgarlo) o «no aplica» (un intérprete completo).",
        note_kind="gold", foot=EJEC)


def se587_cortar_un_bucle() -> Fig:
    return grouped_bars(
        "Tiempo que tardó el anfitrión en cortar un bucle infinito: módulo de WebAssembly con combustible y proceso hijo con límite de tiempo",
        "Barras horizontales con el tiempo en milisegundos para cortar un bucle infinito: el módulo de WebAssembly con 2 000 000 de unidades de combustible 27 y el proceso hijo con límite de 0,5 segundos 629.",
        ["Módulo de WebAssembly (2 000 000 de combustible)", "Proceso hijo (límite de 0,5 s)"],
        [("Milisegundos hasta el corte", [27, 629], "navy")],
        unit="Milisegundos hasta el corte", horizontal=True, decimals=0, label_w=300,
        note="Los dos tiempos dependen de los parámetros elegidos (2 000 000 de unidades de combustible y 0,5 s) y no son comparables como velocidad de aislamiento: con otro combustible el módulo tardaría otro tiempo, y el proceso incluye su límite y su arranque. Lo que muestran es que el mecanismo de corte existe en ambos y que su costo es parte de la decisión.",
        note_kind="teal", foot=EJEC)


def se587_decision() -> Fig:
    return flow(
        "Árbol de decisión del taller: de la capacidad de la carga a la frontera, con la batería hostil al final",
        "Diagrama con tres filas de cajas: una pregunta de capacidad sobre si la carga se puede compilar a WebAssembly, una pregunta de amenaza sobre si el código es de un inquilino o de varios y la elección entre módulo, proceso con límites y frontera reforzada; una nota indica que la batería hostil se repite tras cada cambio.",
        [[("Pregunta 1: capacidad\n¿Se puede compilar a Wasm y no necesita bibliotecas del sistema?", "gold")],
         [("Pregunta 2: amenaza\n¿Código de un inquilino o de varios, conocido o arbitrario?", "gold")],
         [("Módulo de Wasm\nCombustible, memoria acotada y cero importaciones", "teal"),
          ("Proceso con límites\nEntorno vacío, directorio propio y tiempo máximo", "teal"),
          ("Frontera reforzada\nContenedor, núcleo de aplicación o microVM alrededor", "coral")]],
        note="Cada hoja pasa por la misma batería de seis comportamientos y la decisión se confirma con cada cambio de configuración, no una sola vez. El árbol tiene tres hojas porque el taller probó tres candidatos; con contenedores y microVM tendría más y sus costos habría que medirlos.",
        note_kind="gold", box_h=104, foot="Diagrama de decisión del taller; no es una medición.")


# ---------------------------------------------------------------- SE-288
def se588_registro() -> Fig:
    return grouped_bars(
        "Entradas del registro de evidencia de la ejecución de referencia, por tipo de evento",
        "Barras con las entradas del registro de evidencia de la ejecución de referencia por evento: 5 aceptaciones, 1 rechazo, 5 llamadas y 5 muestras de la carga de 2000 peticiones, para un total de 16 entradas.",
        ["Aceptaciones", "Rechazos", "Llamadas de prueba", "Muestras de la carga"],
        [("Entradas del registro", [5, 1, 5, 5], "navy")],
        unit="Entradas (16 en total)", decimals=0, plot_h=250,
        note="La cadena de 16 entradas verificó como íntegra; alterar el resultado de la entrada 3 hizo que la verificación señalara la entrada 3, y borrar la entrada 2 hizo que señalara la entrada 2. El rechazo también es evidencia. Un registro real anotaría cada llamada (aquí solo cinco muestras de las 2 000) y su volumen cambiaría el diseño del almacenamiento.",
        note_kind="teal", foot=EJEC)


def se588_latencia() -> Fig:
    return percentile_intervals(
        "Latencia por petición con instancia nueva y módulo ya compilado: mediana, percentil 99 y máximo de dos reglas",
        "Intervalos de percentiles en milisegundos con la mediana, el percentil 99 y el máximo de 1012 peticiones de la regla estándar, 0,338, 1,106 y 5,321, y de 988 peticiones de la regla con cálculo, 0,344, 1,416 y 17,254.",
        [("Regla estándar (1 012 peticiones)", [0.338, 1.106, 5.321]), ("Regla con cálculo (988 peticiones)", [0.344, 1.416, 17.254])],
        unit="Milisegundos", log=True, decimals=3, label_w=250,
        note="El máximo está lejos del p99: son llamadas aisladas, con calentamiento. Se emitieron 651 avisos de 2 000 peticiones (semilla 48). La instancia nueva por petición cuesta del orden de 0,3 ms con módulos triviales, el precio de no filtrar estado entre peticiones. Con módulos reales la latencia depende de su tamaño y de su memoria.",
        note_kind="gold", foot=EJEC)


def se588_amenazas() -> Fig:
    filas = ["Una regla pide acceso a archivos o red", "Una regla no termina", "Una regla reserva memoria sin límite", "Una regla lee fuera de su memoria",
             "Una regla filtra estado a la siguiente petición", "Alguien altera o borra el registro", "Alguien altera el informe"]
    cols = ["Validador de subida", "Límites de ejecución", "Instancia por petición", "Cadena de resúmenes", "Firma del informe"]
    mapa = [0, 1, 1, 1, 2, 3, 4]
    vals = [[1 if j == mapa[i] else 0 for j in range(5)] for i in range(7)]
    return heatmap(
        "Siete amenazas de la plataforma de referencia y el mecanismo que contiene cada una",
        "Mapa de calor con siete amenazas y cinco mecanismos de contención: el acceso a archivos o red lo contiene el validador de subida; que no termine, que reserve memoria o que lea fuera de su memoria, los límites de ejecución; que filtre estado, la instancia por petición; alterar o borrar el registro, la cadena de resúmenes; y alterar el informe, la firma.",
        filas, cols, vals, unit="contiene", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "contiene" if v else "—", cell_h=40, label_w=300,
        note="Ninguna fila queda sin marca y ninguna columna queda vacía: cada mecanismo existe porque una amenaza lo exige y cada uno necesita una prueba que falle si se quita. Los límites de ejecución agrupan combustible, memoria acotada y memoria lineal. Las amenazas que la referencia no cubre (autenticación, entorno del anfitrión, hardware) no son filas porque no hay mecanismo que marcar.",
        note_kind="gold", foot=EJEC)


FIGURES = {
    "se-283-cita-y-desafio.svg": se583_cita_y_desafio,
    "se-283-que-detecta.svg": se583_que_detecta,
    "se-283-decisiones-del-verificador.svg": se583_decisiones_del_verificador,
    "se-284-costo-de-simular.svg": se584_costo_de_simular,
    "se-284-grover.svg": se584_grover,
    "se-284-ruido-ghz.svg": se584_ruido_ghz,
    "se-285-tamanos.svg": se585_tamanos,
    "se-285-reutilizar-la-clave.svg": se585_reutilizar_la_clave,
    "se-285-mosca.svg": se585_mosca,
    "se-286-casos-del-token.svg": se586_casos_del_token,
    "se-286-radio-de-dano.svg": se586_radio_de_dano,
    "se-286-ventana-de-uso-indebido.svg": se586_ventana_de_uso_indebido,
    "se-287-matriz-de-contencion.svg": se587_matriz_de_contencion,
    "se-287-cortar-un-bucle.svg": se587_cortar_un_bucle,
    "se-287-decision.svg": se587_decision,
    "se-288-registro.svg": se588_registro,
    "se-288-latencia.svg": se588_latencia,
    "se-288-amenazas.svg": se588_amenazas,
}
