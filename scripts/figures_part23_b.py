"""Figures for SE-281 to SE-288 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-281
def se281_buffer() -> Fig:
    rows = [
        ["64", "1,3", "22,3 %"],
        ["128", "2,7", "7,3 %"],
        ["256", "5,3", "1,6 %"],
        ["512", "10,7", "0,23 %"],
        ["1 024", "21,3", "0,016 %"],
    ]
    return tab("Búfer de audio a 48 kHz: latencia que se añade y callbacks que no llegan a tiempo",
               "Tabla: con un búfer de 64 muestras a 48 kilohercios la latencia es 1,3 milisegundos y el 22,3 por ciento de las llamadas no termina a tiempo; con 256 muestras la latencia es 5,3 y fallan el 1,6 por ciento; con 1024 la latencia es 21,3 y falla el 0,016 por ciento.",
               ["Muestras por búfer", "Latencia del búfer (ms)", "Callbacks tardíos"], rows, [280, 330, 320], row_h=44, size=13,
               note="Un búfer mayor compra holgura con latencia: de 64 a 512 muestras los fallos bajan de 22 % a 0,23 % y la latencia sube de 1,3 a 10,7 ms. El modelo supone un coste fijo con picos lognormales (mediana 0,5 ms, σ = 1,0) más 4 µs por muestra; son supuestos del autor, no una medición de ninguna tarjeta ni sistema operativo.",
               note_kind="gold", foot=SINT)


def se281_alias() -> Fig:
    rows = [
        ["1 000", "1 000", "—"],
        ["5 000", "5 000", "—"],
        ["9 000", "7 000", "sí (8 000 es el límite)"],
        ["12 000", "4 000", "sí"],
        ["15 000", "1 000", "sí"],
    ]
    return tab("Frecuencia que mide una transformada al muestrear tonos puros a 16 kHz",
               "Tabla: al muestrear a 16 kilohercios un tono de 9000 hercios se mide como 7000, uno de 12000 como 4000 y uno de 15000 como 1000, mientras que los de 1000 y 5000 se miden correctamente; el valor medido coincide con la fórmula del pliegue.",
               ["Frecuencia real (Hz)", "Frecuencia medida (Hz)", "¿Plegada sobre otra?"], rows, [270, 330, 330], row_h=44, size=13,
               note="Sobre la mitad de la frecuencia de muestreo (8 kHz aquí) los tonos no desaparecen: se disfrazan de otro más grave, y nada en las muestras permite distinguirlos. Por eso el filtro debe ir antes de muestrear. La transformada se calculó con Goertzel sobre 1 024 muestras; medida y fórmula coincidieron en los seis casos.",
               note_kind="coral", foot=SINT)


def se281_cuadros() -> Fig:
    rows = [
        ["6", "0,5 %", "11,2", "90"],
        ["8", "7,4 %", "11,9", "84"],
        ["9", "16,5 %", "12,9", "77"],
        ["10", "29,0 %", "14,3", "70"],
        ["11", "43,3 %", "15,9", "63"],
    ]
    return tab("Pantalla de 90 Hz (presupuesto de 11,1 ms): fotogramas fuera de presupuesto según el coste medio",
               "Tabla: con un coste medio de render de 6 milisegundos solo el 0,5 por ciento de los fotogramas supera el presupuesto de 11,1; con 8 milisegundos el 7,4; con 10 milisegundos el 29 por ciento; con sincronización vertical el intervalo medio pasa de 11,2 a 15,9 milisegundos.",
               ["Coste medio (ms)", "Fotogramas fuera de presupuesto", "Intervalo medio mostrado (ms)", "Equivale a (fps)"], rows, [190, 320, 280, 170], row_h=44, size=13,
               note="El promedio engaña: con un coste medio de 8 ms, por debajo de 11,1, aún el 7 % de los fotogramas se pierde y con sincronización cada uno se muestra el doble de tiempo (22,2 ms en el percentil 99). En realidad virtual esos fotogramas son los que se sienten. Tiempos lognormales con σ = 0,25 supuestos; no se midió ningún casco.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-282
def se282_redondeo() -> Fig:
    rows = [
        ["Sumar 0,10 un millón de veces (float)", "100 000,00000133", "error de 1,3·10⁻⁶"],
        ["0,1 + 0,2 == 0,3 (float)", "Falso", "—"],
        ["round(2.675, 2) frente a Decimal con HALF_UP", "2,67 y 2,68", "dos reglas, dos totales"],
        ["Facturas cuya suma de líneas redondeadas ≠ total redondeado", "38,68 % de 100 000", "brecha media de 1 céntimo"],
        ["Repartir 100,00 en tres con float redondeado", "99,99", "falta 1 céntimo"],
        ["Repartir 10 000 céntimos en tres, resto al primero", "3334 + 3333 + 3333", "suma exacta"],
    ]
    return tab("Dinero con coma flotante, con decimales y con enteros: seis comprobaciones",
               "Tabla de seis comprobaciones: sumar 0,10 un millón de veces en coma flotante da 100000,00000133; el 38,68 por ciento de 100000 facturas simuladas tiene una suma de líneas redondeadas distinta del total redondeado; repartir 100,00 en tres con coma flotante pierde un céntimo y con enteros de céntimos la suma es exacta.",
               ["Comprobación", "Resultado", "Lectura"], rows, [470, 250, 230], row_h=52, size=13,
               note="Que la suma por líneas y la suma del total difieran en un céntimo en casi cuatro facturas de cada diez no es un error de coma flotante: es una decisión de negocio sin tomar (dónde se redondea). Hay que declararla, probarla y aplicarla en un único lugar. Facturas sintéticas con IVA del 19 %.",
               note_kind="coral", foot=SINT)


def se282_mutantes() -> Fig:
    rows = [
        ["Sin fallos (control)", "0 de 100", "0 de 100"],
        ["Transferir sin comprobar saldo", "100 de 100", "100 de 100"],
        ["Perder el abono de una transferencia", "100 de 100", "100 de 100"],
        ["Abonar dos veces", "100 de 100", "100 de 100"],
        ["Cobrar comisión sin acreditarla", "100 de 100", "100 de 100"],
        ["Redondear la comisión hacia arriba", "0 de 100", "100 de 100"],
    ]
    return tab("Libro mayor con cinco mutantes: corridas de 200 operaciones detectadas por cada tipo de comprobación",
               "Tabla: de cinco fallos inyectados en un libro mayor, cuatro los detectan las invariantes de conservación del dinero y saldo no negativo en 100 de 100 corridas; redondear la comisión hacia arriba no lo detecta ninguna de las dos invariantes y sí lo detecta la comparación con un modelo de referencia.",
               ["Fallo inyectado", "Conservación y saldo ≥ 0", "Comparación con modelo de referencia"], rows, [380, 270, 300], row_h=44, size=13,
               note="La conservación del dinero se cumple aunque el importe sea el equivocado: cobrar 8 en lugar de 7 mueve dinero entre cuentas sin crearlo ni destruirlo. Las invariantes cubren lo que el sistema nunca debe hacer; una regla de negocio exige un oráculo independiente. 100 semillas por mutante.",
               note_kind="teal", foot=SINT)


def se282_idempotencia() -> Fig:
    rows = [
        ["1 %", "1,0109", "1,08 %", "1,0000", "0 %"],
        ["5 %", "1,0526", "4,98 %", "1,0000", "0 %"],
        ["20 %", "1,2482", "19,98 %", "1,0000", "0 %"],
    ]
    return tab("Reintentar un cobro con hasta tres reintentos cuando la respuesta se pierde",
               "Tabla: si el 5 por ciento de las respuestas se pierde y el cliente reintenta hasta tres veces, sin clave de idempotencia se cobra 1,0526 veces por pago y el 4,98 por ciento de los pagos se cobra dos veces o más; con clave de idempotencia se cobra exactamente una vez.",
               ["Respuestas perdidas", "Cobros por pago sin clave", "Pagos cobrados 2+ veces", "Cobros por pago con clave", "Pagos duplicados con clave"], rows, [170, 210, 200, 200, 170], row_h=64, size=13,
               note="El reintento es correcto para el cliente y desastroso para el cargo si el servidor no reconoce la repetición. La clave de idempotencia convierte «lo intenté de nuevo» en «es el mismo cobro». Modelo de 100 000 pagos; el procesador siempre recibe la petición y solo se pierde la respuesta.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-283
def se283_kanon() -> Fig:
    rows = [
        ["Edad exacta + 4 dígitos", "4 558 (91,2 %)", "1", "4 774"],
        ["Edad en 5 años + 4 dígitos", "3 224 (64,5 %)", "1", "4 025"],
        ["Edad en 10 años + 3 dígitos", "89 (1,8 %)", "1", "736"],
        ["Edad en 10 años + 2 dígitos", "0", "2", "80"],
        ["Edad en 20 años + 1 dígito", "0", "92", "10"],
        ["Sin edad ni zona", "0", "2 479", "2"],
    ]
    return tab("Anonimizar 5 000 registros sintéticos por generalización: quién queda único",
               "Tabla: con edad exacta, sexo y cuatro dígitos de código postal el 91,2 por ciento de 5000 registros es único; con edad en tramos de 10 años y tres dígitos queda el 1,8 por ciento; con dos dígitos ninguno es único y la clase mínima es de 2 personas.",
               ["Generalización", "Registros únicos", "Clase mínima", "Clases"], rows, [380, 230, 170, 150], row_h=44, size=13,
               note="Cada nivel de generalización cuesta detalle útil: con tres dígitos todavía hay 89 personas únicas, y otras 211 están en clases de dos o más personas que comparten el mismo diagnóstico, así que pertenecer a la clase ya revela el dato. k ≥ 2 no es privacidad completa. Población y diagnósticos sintéticos.",
               note_kind="coral", foot=SINT)


def se283_fusion() -> Fig:
    rows = [
        ["1,00", "16", "0", "439"],
        ["0,95", "237", "0", "218"],
        ["0,90", "413", "0", "42"],
        ["0,85", "414", "1", "42"],
        ["0,80", "416", "3", "42"],
        ["0,70", "569", "155", "41"],
    ]
    return tab("Fusionar fichas de pacientes por similitud de nombre y fecha: 455 duplicados reales en 1 955 fichas",
               "Tabla: con un umbral de similitud de 0,90 se fusionan 413 pares, todos correctos, y quedan 42 duplicados sin fusionar de 455; con 0,80 se hacen 3 fusiones erróneas y con 0,70 se hacen 155 fusiones de pacientes distintos.",
               ["Umbral de similitud", "Fusiones", "Fusiones de personas distintas", "Duplicados sin fusionar (de 455)"], rows, [220, 170, 290, 270], row_h=44, size=13,
               note="Los dos errores no cuestan lo mismo: un duplicado sin fusionar fragmenta una historia clínica; una fusión errónea mezcla la de dos personas, y ese es el error que puede dañar. Por eso la zona intermedia se envía a revisión humana en lugar de decidirse con un umbral único. Nombres y errores de tecleo sintéticos.",
               note_kind="gold", foot=SINT)


def se283_alarmas() -> Fig:
    rows = [
        ["90", "462,4", "85 de 89", "272,0"],
        ["100", "103,0", "74 de 89", "69,6"],
        ["110", "11,3", "58 de 89", "9,8"],
        ["120", "1,0", "31 de 89", "1,6"],
    ]
    return tab("Alarma por frecuencia cardíaca: avisos por 100 pacientes-día y deterioros detectados según el umbral",
               "Tabla: con un umbral de 90 latidos por minuto hay 462 avisos por cien pacientes-día y se detectan 85 de 89 deterioros; con 110 hay 11 avisos y se detectan 58; con 120 hay 1 aviso por cien pacientes-día y se detectan 31.",
               ["Umbral (lat/min)", "Avisos por 100 pacientes-día", "Deterioros detectados", "Avisos por detección"], rows, [210, 290, 220, 210], row_h=44, size=13,
               note="No hay umbral sin coste: el que detecta casi todo emite 272 avisos por cada deterioro real, que nadie puede atender; el que casi no molesta deja pasar dos de cada tres. Pacientes, señales y deterioros sintéticos; no representan ninguna cohorte ni dispositivo, y la clase no propone umbrales clínicos.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-284
def se284_pow() -> Fig:
    rows = [
        ["8", "256", "283,5", "174,0"],
        ["10", "1 024", "946,1", "648,5"],
        ["12", "4 096", "4 027,2", "2 951,5"],
        ["14", "16 384", "15 231,2", "10 931,5"],
        ["16", "65 536", "47 442,1", "27 372,0"],
    ]
    return tab("Prueba de trabajo con SHA-256: intentos para hallar un hash con n ceros iniciales",
               "Tabla: encontrar un hash SHA-256 con 12 ceros iniciales cuesta 4027 intentos de media, cerca de los 4096 esperados, pero la mediana es 2951; con 16 ceros la media medida en 40 bloques es 47442 frente a 65536 esperados.",
               ["Ceros iniciales (bits)", "Intentos esperados 2ⁿ", "Media medida", "Mediana medida"], rows, [250, 260, 220, 200], row_h=44, size=13,
               note="El coste crece al doble por cada bit, y el tiempo de un bloque es una variable aleatoria con mucha dispersión (mínimo 26, máximo 15 969 con 12 bits). Rehacer 10 bloques encadenados de 12 bits costó unos 48 785 intentos frente a 310 de uno solo. Con 40 bloques, la media de 16 bits aún fluctúa.",
               note_kind="gold", foot=SINT)


def se284_doble_gasto() -> Fig:
    rows = [
        ["10 %", "0,200 (0,205)", "0,053 (0,051)", "0,006 (0,004)", "0,001 (0,000)", "0,000 (0,000)"],
        ["30 %", "0,603 (0,628)", "0,431 (0,446)", "0,249 (0,239)", "0,157 (0,132)", "0,064 (0,042)"],
        ["40 %", "0,800 (0,829)", "0,706 (0,736)", "0,581 (0,603)", "0,492 (0,504)", "0,372 (0,360)"],
    ]
    return tab("Probabilidad de que un atacante rehaga la cadena: simulación (fórmula de Nakamoto)",
               "Tabla: con el 10 por ciento del poder de cómputo un atacante rehace una transacción con 6 confirmaciones con probabilidad 0,001; con el 30 por ciento la probabilidad es 0,157 simulada y 0,132 por la fórmula; con el 40 por ciento es 0,492 y 0,504.",
               ["Poder del atacante", "1 confirmación", "2", "4", "6", "10"], rows, [210, 170, 170, 170, 170, 170], row_h=44, size=12,
               note="La seguridad probabilística depende de dos cosas que el código no controla: la fracción de poder del atacante y el número de confirmaciones que se esperan. Con 30 % ni 10 confirmaciones bajan la probabilidad de 0,04. Simulación (40 000 carreras) y fórmula coinciden en torno a ±0,03; no se probó ninguna red real.",
               note_kind="coral", foot=SINT)


def se284_reentrada() -> Fig:
    rows = [
        ["1", "10", "100", "10", "100"],
        ["3", "30", "80", "10", "100"],
        ["5", "50", "60", "10", "100"],
        ["11", "110", "0", "10", "100"],
    ]
    return tab("Retirada con reentrada: fondos extraídos por un atacante con 10 de saldo en un fondo de 110",
               "Tabla: en un contrato que actualiza el saldo después de enviar el pago, un atacante con 10 de saldo extrae 30 con profundidad 3, 50 con profundidad 5 y vacía los 110 con profundidad 11; si actualiza el saldo antes de enviar, extrae solo sus 10.",
               ["Profundidad de reentrada", "Extraído (actualiza después)", "Fondo restante", "Extraído (actualiza antes)", "Fondo restante"], rows, [190, 240, 180, 240, 180], row_h=64, size=13,
               note="El defecto no está en la aritmética sino en el orden: llamar a código ajeno antes de actualizar el estado permite que ese código vuelva a entrar con el estado viejo. Comprobar, actualizar y luego interactuar elimina esta clase de ataque; no elimina otras. Modelo de juguete en Python, no un contrato real ni una red.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-285
def se285_distancia() -> Fig:
    rows = [
        ["0°", "0,0 %", "0,0 %", "0,0 %"],
        ["30°", "6,8 %", "15,2 %", "16,0 %"],
        ["60°", "25,5 %", "96,5 %", "103,0 %"],
        ["80°", "41,4 %", "408,4 %", "505,2 %"],
    ]
    return tab("Error al tratar grados de longitud y latitud como un plano (pares a menos de 100 km)",
               "Tabla: medir distancias como si los grados fueran un plano tiene un error mediano de 0 por ciento en el ecuador, 6,8 a 30 grados de latitud, 25,5 a 60 y 41,4 a 80; el error máximo a 80 grados supera el 500 por ciento.",
               ["Latitud", "Error mediano", "Percentil 95", "Máximo"], rows, [210, 230, 230, 230], row_h=44, size=13,
               note="Un grado de longitud mide 111 km en el ecuador y 19 km a 80° de latitud; la fórmula plana no lo sabe. Además, dos puntos a ambos lados de ±180° quedan a 111 km pero la resta ingenua da 39 919 km. Esferas frente a elipsoides y proyecciones no se evaluaron: la haversine usa un radio medio.",
               note_kind="coral", foot=SINT)


def se285_reloj() -> Fig:
    rows = [
        ["Horas UTC de un año", "8 760"],
        ["Horas locales distintas que aparecen", "8 759"],
        ["Hora local que se repite (ambigua)", "1"],
        ["Hora local que no existe", "1"],
        ["Días locales de 23 h / 24 h / 25 h", "1 / 362 / 1"],
        ["Tarea diaria «09:00 local» guardada como 13:00 UTC fijas: días en hora equivocada", "180 de 365"],
    ]
    return tab("Una zona con cambio de hora sintético (UTC−4 y UTC−3): lo que hace un año de reloj",
               "Tabla: en una zona sintética con horario de verano, las 8760 horas de un año producen 8759 horas locales distintas, una repetida y una inexistente; hay un día de 23 horas y uno de 25; una tarea diaria guardada como hora UTC fija cae a la hora local equivocada en 180 de 365 días.",
               ["Medida", "Valor"], rows, [680, 250], row_h=52, size=13,
               note="Una hora local sin zona no identifica un instante: la mitad del año una tarea «a las 09:00» guardada como UTC se ejecuta una hora corrida. Guardar el instante en UTC y la regla de zona por separado evita ambos. Las reglas de la zona son sintéticas; no se usó la base de datos de zonas horarias.",
               note_kind="gold", foot=SINT)


def se285_indice() -> Fig:
    rows = [
        ["0,5 km", "12,7", "894,4"],
        ["1 km", "18,0", "1 260,5"],
        ["2 km", "31,6", "2 131,0"],
        ["5 km", "98,6", "5 189,9"],
        ["20 km", "934,8", "16 106,8"],
        ["Fuerza bruta", "20 000", "20 000"],
    ]
    return tab("Candidatos examinados por una consulta de radio de 1 km según el tamaño de celda de una rejilla",
               "Tabla: con puntos uniformes una rejilla de 1 kilómetro examina 18 candidatos por consulta para hallar 6,4 resultados; con puntos agrupados en una ciudad examina 1260 para hallar 455; la fuerza bruta examina 20000 en ambos casos.",
               ["Tamaño de celda", "Candidatos (uniforme; 6,4 resultados)", "Candidatos (agrupado; 455,5 resultados)"], rows, [230, 350, 350], row_h=44, size=13,
               note="El índice reduce el trabajo de 20 000 a 18 candidatos cuando los datos se reparten por igual, y a 1 260 cuando se agrupan: la distribución de los datos decide cuánto ayuda. Una celda mucho mayor que el radio pierde la ventaja. Se cuentan candidatos, no milisegundos: no se midió ninguna base de datos espacial.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-286
def se286_pares() -> Fig:
    rows = [
        ["2 pruebas aleatorias", "43,9 %", "0 %"],
        ["5 pruebas aleatorias", "76,8 %", "52 %"],
        ["8 pruebas aleatorias", "90,4 %", "93 %"],
        ["12 pruebas aleatorias", "96,9 %", "100 %"],
        ["20 pruebas aleatorias", "99,7 %", "100 %"],
        ["9 pruebas diseñadas por pares", "100 %", "100 %"],
    ]
    return tab("Un flujo con 10 bifurcaciones (1 024 caminos): defectos de dos bifurcaciones que halla cada conjunto de pruebas",
               "Tabla: en un flujo con diez bifurcaciones y 1024 caminos, 2 pruebas aleatorias hallan en promedio el 43,9 por ciento de los defectos que dependen de dos bifurcaciones, 8 pruebas el 90,4 y 20 el 99,7; un conjunto de 9 pruebas diseñado para cubrir todos los pares los halla todos.",
               ["Conjunto de pruebas", "Defectos de dos bifurcaciones hallados", "Conjuntos que ven cada rama en ambos valores"], rows, [350, 300, 280], row_h=52, size=13,
               note="Probar todos los caminos exige 1 024 ejecuciones y duplica con cada bifurcación; cubrir todos los pares exige 9. El cálculo supone que los defectos dependen como máximo de dos decisiones: uno que dependa de tres se escapa de los pares. 180 defectos posibles, 300 conjuntos aleatorios por fila.",
               note_kind="teal", foot=SINT)


def se286_duplicados() -> Fig:
    items = [
        ("Sin deduplicar (TTL 0)", 5.0, "coral", "5,0 % de los eventos"),
        ("TTL de 10 s", 3.81, "coral", "3,8 %"),
        ("TTL de 60 s", 1.61, "gold", "1,6 %"),
        ("TTL de 5 min", 0.30, "gold", "0,30 %"),
        ("TTL de 1 h", 0.004, "teal", "4 de 100 000"),
        ("TTL de 24 h", 0.0, "teal", "0"),
    ]
    return bars("Eventos ejecutados dos veces cuando el 5 % se entrega de nuevo y se guarda cada identificador un tiempo limitado",
                "Barras: si el cinco por ciento de los eventos se vuelve a entregar con un retraso lognormal de mediana 30 segundos, sin deduplicar se ejecuta dos veces el 5 por ciento; con una memoria de 60 segundos el 1,6; con una de cinco minutos el 0,3; con una de una hora 4 de cada cien mil; con una de un día ninguno.",
                items, 130, "Una memoria de identificadores con vida corta no basta: las re-entregas con retraso largo (cola de una cola, reintento tras un fallo) la superan. El TTL es una decisión de coste (memoria) frente a riesgo (duplicados). Retraso lognormal con mediana de 30 s y σ = 1,5, supuestos del autor; 100 000 eventos.",
                label_w=290, width=1000, note_kind="gold", foot=SINT)


def se286_huerfanas() -> Fig:
    rows = [
        ["Un responsable, sin revisión", "15,4 %", "37,8 %", "52,2 %"],
        ["Dos responsables, sin revisión", "2,0 %", "12,8 %", "30,8 %"],
        ["Un responsable, revisión anual", "15,4 %", "37,8 %", "52,2 %"],
        ["Dos responsables, revisión anual", "2,0 %", "5,6 %", "8,6 %"],
    ]
    return tab("Automatizaciones sin responsable activo si cada responsable se va con probabilidad del 15 % al año (500 flujos)",
               "Tabla: con un solo responsable por automatización, el 15,4 por ciento queda sin responsable al año, el 37,8 a los tres y el 52,2 a los cinco, con o sin revisión anual; con dos responsables y revisión anual con reposición queda el 2 por ciento al año, el 5,6 a los tres y el 8,6 a los cinco.",
               ["Política", "Tras 1 año", "Tras 3 años", "Tras 5 años"], rows, [400, 170, 170, 190], row_h=44, size=13,
               note="La revisión anual no sirve si no queda nadie a quien reasignar: solo cambia el resultado cuando hay al menos dos responsables y la revisión repone al que se fue. La tasa de salida del 15 % es un supuesto, no una medición de ninguna organización; el patrón (no basta revisar) es el hallazgo.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-287
def se287_ranking() -> Fig:
    rows = [
        ["Pesos casi iguales (concentración 50)", "100 %", "99,8 %", "1,00"],
        ["Pesos algo distintos (10)", "97,6 %", "88,4 %", "0,87"],
        ["Pesos muy dispares (3)", "84,9 %", "71,4 %", "0,69"],
    ]
    return tab("Diez dominios puntuados en seis criterios: cuánto cambia el ranking al variar los pesos (5 000 sorteos)",
               "Tabla: al perturbar los pesos de seis criterios sobre diez dominios, el primer lugar se mantiene en el 100 por ciento de los sorteos con pesos casi iguales, en el 97,6 con pesos algo distintos y en el 84,9 con pesos muy dispares; la correlación de Kendall en el percentil 5 baja de 1,00 a 0,69.",
               ["Dispersión de los pesos", "Primer lugar igual", "Primeros dos (conjunto) iguales", "Kendall (percentil 5)"], rows, [380, 200, 230, 130], row_h=52, size=13,
               note="El primer puesto es estable porque en este ejemplo un dominio puntúa alto en casi todo; la parte media del ranking no lo es. Los puntajes de 1 a 5 son un juicio ilustrativo del autor, no una medición de los dominios: el ejercicio muestra cómo revisar un ranking, no cuál es el orden verdadero.",
               note_kind="gold", foot=SINT)


def se287_acuerdo() -> Fig:
    rows = [
        ["0,0", "100 %", "1,00", "0 %"],
        ["0,5", "58,0 %", "0,84", "24,3 %"],
        ["1,0", "36,4 %", "0,59", "61,3 %"],
        ["1,5", "30,3 %", "0,39", "82,7 %"],
    ]
    return tab("Dos evaluadores puntúan los mismos 60 criterios con ruido: acuerdo y cambio en los tres primeros",
               "Tabla: si dos evaluadores se desvían medio punto al puntuar, coinciden exactamente en el 58 por ciento de los criterios, el kappa ponderado es 0,84 y el trío de dominios más riesgosos difiere en el 24,3 por ciento de los pares; con un punto de ruido coinciden el 36,4 por ciento y el trío difiere en el 61,3.",
               ["Ruido de cada evaluador (puntos)", "Acuerdo exacto", "Kappa ponderado", "Tres primeros distintos"], rows, [310, 200, 210, 210], row_h=44, size=13,
               note="Un kappa de 0,84 suena alto y aun así el podio cambia en uno de cada cuatro pares de evaluadores. Antes de comparar dominios hay que calibrar la escala con ejemplos y reportar el acuerdo. 300 pares simulados; el ruido gaussiano es un modelo, no una medición de personas.",
               note_kind="coral", foot=SINT)


def se287_cobertura() -> Fig:
    rows = [
        ["1", "5 de 14", "ciencia (0 %)"],
        ["2", "8 de 14", "ML (0 %)"],
        ["3", "10 de 14", "juegos (33 %)"],
        ["4", "12 de 14", "audio/XR (50 %)"],
        ["6 (cobertura voraz)", "14 de 14", "todos cubiertos"],
    ]
    return tab("Controles frente a 14 riesgos de diez dominios: lo que cubre una lista corta común",
               "Tabla: los mejores 3 controles de ocho cubren 10 de los 14 riesgos distintos de diez dominios y dejan a juegos con el 33 por ciento de sus riesgos cubiertos; cubrir los 14 riesgos exige 6 controles.",
               ["Controles elegidos", "Riesgos cubiertos", "Dominio peor cubierto"], rows, [330, 300, 300], row_h=44, size=13,
               note="Una lista universal corta cubre mucho en promedio y deja a algún dominio casi sin protección. Los riesgos más repetidos (privacidad, duplicados, pérdida de datos) aparecen en cuatro dominios cada uno; los demás son propios de uno. La matriz de controles y riesgos es una construcción del autor.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-288
def se288_validador() -> Fig:
    rows = [
        ["Borrar una sección", "25 de 25"],
        ["Vaciar una sección", "25 de 25"],
        ["Cambiar una cifra en la sección de experimentos", "25 de 25"],
        ["Quitar el enlace de las fuentes", "25 de 25"],
        ["Cambiar una cifra en la afirmación", "0 de 25"],
        ["Invertir la conclusión", "0 de 25"],
        ["Enlazar una página inexistente", "0 de 25"],
        ["Sustituir un límite concreto por uno genérico", "0 de 25"],
    ]
    return tab("Validador de forma de un dosier: mutaciones detectadas de 25 por tipo",
               "Tabla: un validador de estructura detecta 25 de 25 mutaciones que borran o vacían una sección, cambian una cifra en la sección de experimentos o quitan el enlace; no detecta ninguna de las que cambian una cifra en la afirmación, invierten la conclusión, enlazan una página inexistente o sustituyen un límite por uno genérico.",
               ["Mutación del dosier", "Detectada por el validador"], rows, [660, 270], row_h=38, size=13,
               note="El validador ve la forma y las cifras que alguien le pidió cruzar; no ve el sentido. Las cuatro mutaciones que se le escapan son las que más dañan a un lector. Por eso el dosier necesita una revisión de contenido hecha por una persona, y el validador solo evita lo mecánico.",
               note_kind="coral", foot=SINT)


def se288_sensibilidad() -> Fig:
    rows = [
        ["Licencia anual", "−17 400 a 9 600", "−0,49"],
        ["Tarifa horaria", "−7 000 a 12 000", "+0,39"],
        ["Horas de construcción", "−5 400 a 12 600", "+0,35"],
        ["Horas de mantenimiento al año", "−4 800 a 11 400", "+0,31"],
        ["Probabilidad de incidente propio", "−6 600 a 7 800", "+0,38"],
        ["Horas de integración", "−5 400 a 3 600", "−0,16"],
    ]
    return tab("Construir o comprar: cuánto mueve la diferencia de coste cada supuesto (base: construir cuesta 600 más)",
               "Tabla: la diferencia de coste entre construir y comprar vale 600 en el caso base; al variar un supuesto a la vez, la licencia anual la mueve entre menos 17400 y 9600 y la tarifa horaria entre menos 7000 y 12000; en los nueve supuestos, el signo cambia dentro de su rango, y en 20000 sorteos construir cuesta menos el 36 por ciento de las veces.",
               ["Supuesto (uno a la vez)", "Diferencia de coste", "Correlación de Spearman"], rows, [380, 290, 260], row_h=44, size=13,
               note="Los nueve supuestos cambian el signo de la diferencia dentro de su rango: la decisión no se sostiene en el punto base. En 20 000 sorteos construir sale más barato el 36 % de las veces. El modelo y los rangos son un ejemplo del autor, no cifras de un proveedor ni de un equipo real.",
               note_kind="gold", foot=SINT)


def se288_huellas() -> Fig:
    rows = [
        ["Cambiar de LF a CRLF", "3 de 3", "0 de 3"],
        ["Añadir espacios al final de una línea", "3 de 3", "0 de 3"],
        ["Quitar el salto de línea final", "3 de 3", "0 de 3"],
        ["Reordenar las claves de un JSON", "1 de 3", "0 de 3"],
        ["Cambiar una cifra del contenido", "3 de 3", "3 de 3"],
    ]
    return tab("Huella SHA-256 del paquete: cambios que la alteran con y sin canonicalizar antes",
               "Tabla: cambiar los saltos de línea de LF a CRLF altera la huella SHA-256 de 3 de 3 ficheros si se calcula sobre los bytes y de 0 de 3 si antes se normaliza; cambiar una cifra del contenido altera la huella en ambos casos.",
               ["Cambio sobre tres ficheros", "Huella sobre los bytes", "Huella tras canonicalizar"], rows, [440, 240, 250], row_h=44, size=13,
               note="Una huella sobre bytes crudos avisa de cambios que no importan (saltos de línea de Windows frente a Linux) y esa alarma constante enseña a ignorarla. Canonicalizar conserva la alarma para el cambio de contenido. Lo que ninguna huella dice es si el contenido es correcto: solo si cambió.",
               note_kind="teal", foot=SINT)


FIGURES = {
    "se-281-latencia-y-subcargas-de-audio.svg": se281_buffer,
    "se-281-aliasing-de-un-tono.svg": se281_alias,
    "se-281-fotogramas-fuera-de-presupuesto.svg": se281_cuadros,
    "se-282-dinero-con-coma-flotante.svg": se282_redondeo,
    "se-282-mutantes-de-un-libro-mayor.svg": se282_mutantes,
    "se-282-cobros-duplicados.svg": se282_idempotencia,
    "se-283-anonimizar-por-generalizacion.svg": se283_kanon,
    "se-283-fusion-de-fichas.svg": se283_fusion,
    "se-283-fatiga-de-alarmas.svg": se283_alarmas,
    "se-284-prueba-de-trabajo.svg": se284_pow,
    "se-284-doble-gasto.svg": se284_doble_gasto,
    "se-284-reentrada-en-un-contrato.svg": se284_reentrada,
    "se-285-distancia-en-grados.svg": se285_distancia,
    "se-285-un-ano-de-reloj.svg": se285_reloj,
    "se-285-indice-de-rejilla.svg": se285_indice,
    "se-286-caminos-frente-a-pares.svg": se286_pares,
    "se-286-eventos-duplicados.svg": se286_duplicados,
    "se-286-automatizaciones-huerfanas.svg": se286_huerfanas,
    "se-287-estabilidad-de-un-ranking.svg": se287_ranking,
    "se-287-acuerdo-entre-evaluadores.svg": se287_acuerdo,
    "se-287-controles-frente-a-riesgos.svg": se287_cobertura,
    "se-288-mutaciones-de-un-dosier.svg": se288_validador,
    "se-288-sensibilidad-de-supuestos.svg": se288_sensibilidad,
    "se-288-huella-del-paquete.svg": se288_huellas,
}
