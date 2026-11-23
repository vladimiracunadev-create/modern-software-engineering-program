"""Figures for SE-293 to SE-300 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import (Fig, _kit_finish, _kit_start, grouped_bars, heatmap, line_chart,
                        percentile_intervals, timeline)
from figures_part07_a import bars

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-293
def se281_buffer() -> Fig:
    return line_chart(
        "Búfer de audio a 48 kHz: latencia que se añade y callbacks que no llegan a tiempo",
        "Línea en escalas logarítmicas que une latencia y fallos del búfer de audio: con 64 muestras la latencia es 1,3 milisegundos y falla el 22,3 por ciento de las llamadas; con 256 muestras, 5,3 y 1,6 por ciento; con 1024, 21,3 y 0,016 por ciento; la línea desciende, cada mejora de fiabilidad se paga con latencia.",
        [("Callbacks tardíos", [(1.3, 22.3, "64 muestras · 22,3 %", "t"), (2.7, 7.3, "128 · 7,3 %", "r"), (5.3, 1.6, "256 · 1,6 %", "r"),
                                (10.7, 0.23, "512 · 0,23 %", "r"), (21.3, 0.016, "1 024 · 0,016 %", "r")], "coral")],
        x_label="Latencia que añade el búfer (ms)", y_label="Callbacks que no llegan a tiempo (%)", log_x=True, log_y=True,
        x_ticks=[(1, "1"), (2, "2"), (5, "5"), (10, "10"), (20, "20"), (50, "50")], y_ticks=[0.01, 0.1, 1, 10, 100],
        point_labels="none",
        note='Un búfer mayor compra holgura con latencia: de 64 a 512 muestras los fallos bajan de 22 % a 0,23 % y la latencia sube de 1,3 a 10,7 ms. El modelo supone un coste fijo con picos lognormales (mediana 0,5 ms, σ = 1,0) más 4 µs por muestra; son supuestos del autor, no una medición de ninguna tarjeta ni sistema operativo.', note_kind='gold', foot=SINT)


def se281_alias() -> Fig:
    return line_chart(
        "Frecuencia que mide una transformada al muestrear tonos puros a 16 kHz",
        "Líneas con la frecuencia medida frente a la frecuencia real al muestrear a 16 kilohercios: hasta 8 000 hercios la medida coincide con la real; por encima del límite de 8 000 la medida se pliega hacia abajo: 9 000 se mide como 7 000, 12 000 como 4 000 y 15 000 como 1 000.",
        [("Frecuencia medida", [(1000, 1000, "1 000", "r"), (5000, 5000, "5 000", "b"), (9000, 7000, "9 000 → 7 000", "r"),
                                (12000, 4000, "12 000 → 4 000", "r"), (15000, 1000, "15 000 → 1 000", "l")], "coral"),
         ("Sin plegado (medida = real)", [(0, 0, "", "t"), (15000, 15000, "", "t")], "grey")],
        x_label="Frecuencia real del tono (Hz)", y_label="Frecuencia medida (Hz)", point_labels="none",
        x_ticks=[(0, "0"), (4000, "4 000"), (8000, "8 000"), (12000, "12 000"), (16000, "16 000")],
        y_ticks=[0, 4000, 8000, 12000, 16000], vlines=[(8000, "límite: 8 000 Hz")],
        note='Sobre la mitad de la frecuencia de muestreo (8 kHz aquí) los tonos no desaparecen: se disfrazan de otro más grave, y nada en las muestras permite distinguirlos. Por eso el filtro debe ir antes de muestrear. La transformada se calculó con Goertzel sobre 1 024 muestras; medida y fórmula coincidieron en los seis casos.', note_kind='coral', foot=SINT)


def se281_cuadros() -> Fig:
    return line_chart(
        "Pantalla de 90 Hz (presupuesto de 11,1 ms): fotogramas fuera de presupuesto según el coste medio",
        "Línea con el porcentaje de fotogramas fuera del presupuesto de 11,1 milisegundos según el coste medio de render: 0,5 por ciento con 6 milisegundos, 7,4 con 8, 16,5 con 9, 29,0 con 10 y 43,3 con 11; ya con un coste medio por debajo del presupuesto se pierde una parte creciente de los fotogramas.",
        [("Fotogramas fuera de presupuesto", [(6, 0.5, "0,5 %", "t"), (8, 7.4, "7,4 %", "l"), (9, 16.5, "16,5 %", "l"), (10, 29.0, "29,0 %", "l"), (11, 43.3, "43,3 %", "l")], "coral")],
        x_label="Coste medio de render (ms)", y_label="Fotogramas fuera de presupuesto (%)", point_labels="none",
        x_ticks=[(6, "6"), (7, "7"), (8, "8"), (9, "9"), (10, "10"), (11, "11"), (12, "")], y_ticks=[0, 10, 20, 30, 40, 50],
        vlines=[(11.1, "11,1 ms")],
        annotations=[(8, 7.4, "Con 8 ms, por debajo del presupuesto de 11,1 ms, ya se pierde el 7,4 %", -40, -200)],
        note='El promedio engaña: con un coste medio de 8 ms, por debajo de 11,1, aún el 7 % de los fotogramas se pierde y con sincronización cada uno se muestra el doble de tiempo (22,2 ms en el percentil 99). En realidad virtual esos fotogramas son los que se sienten. Tiempos lognormales con σ = 0,25 supuestos; no se midió ningún casco.', note_kind='gold', foot=SINT)


# ---------------------------------------------------------------- SE-294
def se282_redondeo() -> Fig:
    f, y = _kit_start("Dinero con coma flotante, con decimales y con enteros: seis comprobaciones",
                      "Diagrama de seis comprobaciones agrupadas en tres bloques: la suma repetida, la igualdad y el redondeo en coma flotante fallan por representación; la suma de líneas redondeadas y el total redondeado difieren en el 38,68 por ciento de 100000 facturas; repartir 100,00 en tres pierde un céntimo con coma flotante y es exacto con enteros de céntimos.",
                      940, None)

    def row(ry: float, left: str, mid: str, right: str, mid_kind: str = "coral", right_kind: str = "grey") -> None:
        f.box(24, ry, 360, 46, left, "plain", 13)
        f.arrow([(384, ry + 23), (424, ry + 23)])
        f.box(424, ry, 220, 46, mid, mid_kind, 13, bold=True)
        f.arrow([(644, ry + 23), (684, ry + 23)])
        f.box(684, ry, 232, 46, right, right_kind, 13)

    f.group(10, y, 920, 206, "Coma flotante: el error está en cómo se guarda 0,1", "grey")
    row(y + 34, "Sumar 0,10 un millón de veces (float)", "100 000,00000133", "error de 1,3·10⁻⁶")
    row(y + 90, "0,1 + 0,2 == 0,3 (float)", "Falso", "—")
    row(y + 146 - 0, "round(2.675, 2) frente a Decimal con HALF_UP", "2,67 y 2,68", "dos reglas, dos totales", "gold")
    y += 206 + 12
    f.group(10, y, 920, 150, "Decimales exactos: el desacuerdo es una regla de redondeo sin decidir", "grey")
    f.box(24, y + 36, 360, 46, "Redondear cada línea y luego sumar", "plain", 13)
    f.box(24, y + 92, 360, 46, "Sumar las líneas y luego redondear el total", "plain", 13)
    f.arrow([(384, y + 59), (404, y + 59), (404, y + 87), (424, y + 87)])
    f.arrow([(384, y + 115), (404, y + 115), (404, y + 87), (424, y + 87)])
    f.box(424, y + 36, 220, 102, "No coinciden en el 38,68 % de 100 000 facturas", "coral", 13, bold=True)
    f.arrow([(644, y + 87), (684, y + 87)])
    f.box(684, y + 64, 232, 46, "brecha media de 1 céntimo", "grey", 13)
    y += 150 + 12
    f.group(10, y, 920, 134, "Repartir 100,00 entre tres: coma flotante frente a enteros de céntimos", "grey")
    row(y + 34, "Repartir 100,00 en tres con float redondeado", "99,99", "falta 1 céntimo")
    row(y + 86, "Repartir 10 000 céntimos en tres, resto al primero", "3334 + 3333 + 3333", "suma exacta", "teal", "teal")
    y += 134 + 8
    out = _kit_finish(f, y, 'Que la suma por líneas y la suma del total difieran en un céntimo en casi cuatro facturas de cada diez no es un error de coma flotante: es una decisión de negocio sin tomar (dónde se redondea). Hay que declararla, probarla y aplicarla en un único lugar. Facturas sintéticas con IVA del 19 %.', 'coral', SINT)
    out.kind = "diagram"
    return out


def se282_mutantes() -> Fig:
    return heatmap(
        "Libro mayor con cinco mutantes: corridas de 200 operaciones detectadas por cada tipo de comprobación",
        "Mapa de calor con las corridas, de 100, en que cada comprobación detecta cada fallo inyectado en un libro mayor: las invariantes de conservación y saldo no negativo detectan 100 de 100 en cuatro fallos y 0 en el redondeo de la comisión; la comparación con un modelo de referencia detecta 100 de 100 en cinco fallos.",
        ["Sin fallos (control)", "Transferir sin comprobar saldo", "Perder el abono de una transferencia", "Abonar dos veces", "Cobrar comisión sin acreditarla", "Redondear la comisión hacia arriba"],
        ["Conservación y saldo ≥ 0", "Comparación con modelo de referencia"],
        [[0, 0], [100, 100], [100, 100], [100, 100], [100, 100], [0, 100]],
        unit="corridas detectadas", row_title="Fallo inyectado", col_title="Corridas detectadas (de 100)",
        scale="teal", vmin=0, vmax=100, cell_fmt=lambda v: f"{int(v)} de 100", highlight=[(5, 0), (5, 1)], cell_h=42, label_w=230,
        note='La conservación del dinero se cumple aunque el importe sea el equivocado: cobrar 8 en lugar de 7 mueve dinero entre cuentas sin crearlo ni destruirlo. Las invariantes cubren lo que el sistema nunca debe hacer; una regla de negocio exige un oráculo independiente. 100 semillas por mutante.', note_kind='teal', foot=SINT)


def se282_idempotencia() -> Fig:
    return grouped_bars(
        "Reintentar un cobro con hasta tres reintentos cuando la respuesta se pierde",
        "Barras agrupadas con el porcentaje de pagos cobrados dos veces o más al reintentar hasta tres veces cuando se pierde la respuesta: sin clave de idempotencia es 1,08, 4,98 y 19,98 por ciento si se pierde el 1, el 5 y el 20 por ciento de las respuestas; con clave es 0 en todos los casos.",
        ["1 % de respuestas perdidas", "5 % de respuestas perdidas", "20 % de respuestas perdidas"],
        [("Sin clave de idempotencia", [1.08, 4.98, 19.98], "coral"), ("Con clave de idempotencia", [0, 0, 0], "teal")],
        unit="Pagos cobrados 2 o más veces (%)",
        note='El reintento es correcto para el cliente y desastroso para el cargo si el servidor no reconoce la repetición. La clave de idempotencia convierte «lo intenté de nuevo» en «es el mismo cobro». Modelo de 100 000 pagos; el procesador siempre recibe la petición y solo se pierde la respuesta.', note_kind='gold', foot=SINT)


# ---------------------------------------------------------------- SE-295
def se283_kanon() -> Fig:
    return line_chart(
        "Anonimizar 5 000 registros sintéticos por generalización: quién queda único",
        "Línea que une el número de clases con el porcentaje de registros únicos al generalizar 5000 registros: con edad exacta y cuatro dígitos hay 4774 clases y el 91,2 por ciento es único; con edad en tramos de 5 años 4025 clases y 64,5; con tramos de 10 años y tres dígitos 736 clases y 1,8; con dos dígitos o menos ningún registro es único, a costa de 80 clases o menos.",
        [("Registros únicos", [(2, 0, "Sin edad ni zona", "t"), (10, 0, "Edad 20 años, 1 díg.", "t"), (80, 0, "Edad 10 años, 2 díg.", "t"),
                              (736, 1.8, "Edad 10 años, 3 díg. · 1,8 %", "t"), (4025, 64.5, "Edad 5 años, 4 díg. · 64,5 %", "l"),
                              (4774, 91.2, "Edad exacta, 4 díg. · 91,2 %", "l")], "coral")],
        x_label="Número de clases (más clases = más detalle conservado)", y_label="Registros únicos (%)", log_x=True,
        x_ticks=[(1, "1"), (10, "10"), (100, "100"), (1000, "1 000"), (10000, "10 000")], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        note='Cada nivel de generalización cuesta detalle útil: con tres dígitos todavía hay 89 personas únicas, y otras 211 están en clases de dos o más personas que comparten el mismo diagnóstico, así que pertenecer a la clase ya revela el dato. k ≥ 2 no es privacidad completa. Población y diagnósticos sintéticos.', note_kind='coral', foot=SINT)


def se283_fusion() -> Fig:
    return line_chart(
        "Fusionar fichas de pacientes por similitud de nombre y fecha: 455 duplicados reales en 1 955 fichas",
        "Líneas con los duplicados sin fusionar y las fusiones de personas distintas según el umbral de similitud: al bajar de 1,00 a 0,90 los duplicados sin fusionar caen de 439 a 42 sin ninguna fusión errónea; al bajar a 0,70 las fusiones de personas distintas suben a 155 mientras los duplicados apenas bajan a 41.",
        [("Duplicados sin fusionar (de 455)", [(0.70, 41, "41", "t"), (0.80, 42, "42", "t"), (0.85, 42, "42", "t"), (0.90, 42, "42", "t"), (0.95, 218, "218", "t"), (1.00, 439, "439", "t")], "gold"),
         ("Fusiones de personas distintas", [(0.70, 155, "155", "t"), (0.80, 3, "3", "t"), (0.85, 1, "1", "t"), (0.90, 0, "", "t"), (0.95, 0, "", "t"), (1.00, 0, "0", "t")], "coral")],
        x_label="Umbral de similitud (más alto = más estricto)", y_label="Fichas", point_labels="none",
        x_ticks=[(0.70, "0,70"), (0.75, ""), (0.80, "0,80"), (0.85, ""), (0.90, "0,90"), (0.95, "0,95"), (1.00, "1,00")], y_ticks=[0, 100, 200, 300, 400, 500],
        note='Los dos errores no cuestan lo mismo: un duplicado sin fusionar fragmenta una historia clínica; una fusión errónea mezcla la de dos personas, y ese es el error que puede dañar. Por eso la zona intermedia se envía a revisión humana en lugar de decidirse con un umbral único. Nombres y errores de tecleo sintéticos.', note_kind='gold', foot=SINT)


def se283_alarmas() -> Fig:
    return line_chart(
        "Alarma por frecuencia cardíaca: avisos por 100 pacientes-día y deterioros detectados según el umbral",
        "Línea con los deterioros detectados, de 89, según los avisos por 100 pacientes-día en escala logarítmica: el umbral de 120 latidos por minuto da 1,0 aviso y detecta 31; el de 110 da 11,3 y detecta 58; el de 100 da 103,0 y detecta 74; el de 90 da 462,4 y detecta 85.",
        [("Deterioros detectados", [(1.0, 31, "120 lat/min · 31 de 89", "r"), (11.3, 58, "110 · 58 de 89", "r"), (103.0, 74, "100 · 74 de 89", "r"),
                                    (462.4, 85, "90 · 85 de 89", "l")], "coral")],
        x_label="Avisos por 100 pacientes-día", y_label="Deterioros detectados (de 89)", log_x=True,
        x_ticks=[(1, "1"), (10, "10"), (100, "100"), (1000, "1 000")], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        hlines=[(89, "89 deterioros reales")],
        note='No hay umbral sin coste: el que detecta casi todo emite 272 avisos por cada deterioro real, que nadie puede atender; el que casi no molesta deja pasar dos de cada tres. Pacientes, señales y deterioros sintéticos; no representan ninguna cohorte ni dispositivo, y la clase no propone umbrales clínicos.', note_kind='coral', foot=SINT)


# ---------------------------------------------------------------- SE-296
def se284_pow() -> Fig:
    return line_chart(
        "Prueba de trabajo con SHA-256: intentos para hallar un hash con n ceros iniciales",
        "Líneas en escala logarítmica con los intentos para hallar un hash SHA-256 con n ceros iniciales: el valor esperado 2 elevado a n sube de 256 con 8 bits a 65 536 con 16; la media medida (283,5 a 47 442,1) y la mediana medida (174,0 a 27 372,0) crecen en paralelo, con la mediana siempre por debajo de la media.",
        [("Esperado 2ⁿ", [(8, 256), (10, 1024), (12, 4096), (14, 16384), (16, 65536, "65 536", "t")], "grey"),
         ("Media medida", [(8, 283.5), (10, 946.1), (12, 4027.2), (14, 15231.2), (16, 47442.1, "47 442", "r")], "gold"),
         ("Mediana medida", [(8, 174.0), (10, 648.5), (12, 2951.5), (14, 10931.5), (16, 27372.0, "27 372", "r")], "teal")],
        x_label="Ceros iniciales exigidos (bits)", y_label="Intentos hasta hallar el hash", log_y=True,
        x_ticks=[(8, "8"), (10, "10"), (12, "12"), (14, "14"), (16, "16"), (18, "")], y_ticks=[100, 1000, 10000, 100000], point_labels="none",
        note='El coste crece al doble por cada bit, y el tiempo de un bloque es una variable aleatoria con mucha dispersión (mínimo 26, máximo 15 969 con 12 bits). Rehacer 10 bloques encadenados de 12 bits costó unos 48 785 intentos frente a 310 de uno solo. Con 40 bloques, la media de 16 bits aún fluctúa.', note_kind='gold', foot=SINT)


def se284_doble_gasto() -> Fig:
    return line_chart(
        "Probabilidad de que un atacante rehaga la cadena: simulación (fórmula de Nakamoto)",
        "Líneas con la probabilidad simulada de que un atacante rehaga la cadena según las confirmaciones: con el 10 por ciento del poder cae a 0,001 con 6 confirmaciones; con el 30 por ciento baja de 0,603 a 0,064 con 10; con el 40 por ciento solo baja de 0,800 a 0,372; la fórmula de Nakamoto da valores equivalentes.",
        [("Atacante con el 40 %", [(1, 0.800, "0,800", "t"), (2, 0.706, "0,706", "t"), (4, 0.581, "0,581", "t"), (6, 0.492, "0,492", "t"), (10, 0.372, "0,372", "t")], "coral"),
         ("Atacante con el 30 %", [(1, 0.603, "0,603", "t"), (2, 0.431, "0,431", "t"), (4, 0.249, "0,249", "t"), (6, 0.157, "0,157", "t"), (10, 0.064, "0,064", "t")], "gold"),
         ("Atacante con el 10 %", [(1, 0.200, "0,200", "t"), (2, 0.053, "0,053", "t"), (4, 0.006, "0,006", "t"), (6, 0.001, "0,001", "t"), (10, 0.000, "0,000", "r")], "teal")],
        x_label="Confirmaciones esperadas", y_label="Probabilidad de rehacer la cadena (simulada)",
        x_ticks=[(1, "1"), (2, "2"), (4, "4"), (6, "6"), (10, "10"), (11, "")], y_ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], point_labels="none",
        note='La seguridad probabilística depende de dos cosas que el código no controla: la fracción de poder del atacante y el número de confirmaciones que se esperan. Con 30 % ni 10 confirmaciones bajan la probabilidad de 0,04. Simulación (40 000 carreras) y fórmula coinciden en torno a ±0,03; no se probó ninguna red real.', note_kind='coral', foot=SINT)


def se284_reentrada() -> Fig:
    return line_chart(
        "Retirada con reentrada: fondos extraídos por un atacante con 10 de saldo en un fondo de 110",
        "Líneas con los fondos extraídos por un atacante con 10 de saldo según la profundidad de reentrada: si el contrato actualiza el saldo después de enviar el pago extrae 10, 30, 50 y 110 con profundidad 1, 3, 5 y 11, hasta vaciar el fondo de 110; si actualiza antes de enviar extrae siempre 10.",
        [("Actualiza después de enviar", [(1, 10, "10", "t"), (3, 30, "30", "t"), (5, 50, "50", "t"), (11, 110, "110", "b")], "coral"),
         ("Actualiza antes de enviar", [(1, 10, "", "b"), (3, 10, "10", "t"), (5, 10, "10", "t"), (11, 10, "10", "t")], "teal")],
        x_label="Profundidad de reentrada", y_label="Fondos extraídos", point_labels="none",
        x_ticks=[(1, "1"), (3, "3"), (5, "5"), (7, "7"), (9, "9"), (11, "11")], y_ticks=[0, 20, 40, 60, 80, 100, 120], hlines=[(110, "fondo total: 110")],
        note='El defecto no está en la aritmética sino en el orden: llamar a código ajeno antes de actualizar el estado permite que ese código vuelva a entrar con el estado viejo. Comprobar, actualizar y luego interactuar elimina esta clase de ataque; no elimina otras. Modelo de juguete en Python, no un contrato real ni una red.', note_kind='coral', foot=SINT)


# ---------------------------------------------------------------- SE-297
def se285_distancia() -> Fig:
    return grouped_bars(
        "Error al tratar grados de longitud y latitud como un plano (pares a menos de 100 km)",
        "Barras agrupadas con el error al medir distancias como si los grados fueran un plano: la mediana es 0,0 por ciento en el ecuador, 6,8 a 30 grados de latitud, 25,5 a 60 y 41,4 a 80; el percentil 95 llega a 408,4 y el máximo a 505,2 por ciento a 80 grados.",
        ["0° (ecuador)", "30°", "60°", "80°"],
        [("Mediana", [0.0, 6.8, 25.5, 41.4], "teal"), ("Percentil 95", [0.0, 15.2, 96.5, 408.4], "gold"), ("Máximo", [0.0, 16.0, 103.0, 505.2], "coral")],
        unit="Error de la distancia plana (%)", decimals=1,
        note='Un grado de longitud mide 111 km en el ecuador y 19 km a 80° de latitud; la fórmula plana no lo sabe. Además, dos puntos a ambos lados de ±180° quedan a 111 km pero la resta ingenua da 39 919 km. Esferas frente a elipsoides y proyecciones no se evaluaron: la haversine usa un radio medio.', note_kind='coral', foot=SINT)


def se285_reloj() -> Fig:
    return timeline(
        "Una zona con cambio de hora sintético (UTC−4 y UTC−3): lo que hace un año de reloj",
        "Línea de tiempo de un año en una zona sintética: UTC−4 hasta el día 120, UTC−3 del día 120 al 300 y UTC−4 desde el 300; en el día 120 falta una hora local (día de 23 horas) y en el 300 una hora se repite (día de 25 horas); una tarea diaria guardada como 13:00 UTC cae a las 10:00 locales los 180 días de verano en vez de a las 09:00.",
        [("Regla de desfase de la zona", [(0, 120, "UTC−4", "navy"), (120, 300, "UTC−3 (horario de verano)", "gold"), (300, 365, "UTC−4", "navy")]),
         ("Tarea «09:00 local» guardada como 13:00 UTC", [(0, 120, "09:00 correcta", "teal"), (120, 300, "10:00 equivocada (180 días)", "coral"), (300, 365, "09:00", "teal")])],
        unit="Día del año (365 días, 8 760 horas UTC)", events=[(120, "día 120: día de 23 h"), (300, "día 300: día de 25 h")],
        ticks=[0, 60, 120, 180, 240, 300, 365], lane_h=60, label_w=230, t_max=365,
        note='Una hora local sin zona no identifica un instante: la mitad del año una tarea «a las 09:00» guardada como UTC se ejecuta una hora corrida. Guardar el instante en UTC y la regla de zona por separado evita ambos. Las reglas de la zona son sintéticas; no se usó la base de datos de zonas horarias.', note_kind='gold', foot=SINT)


def se285_indice() -> Fig:
    return line_chart(
        "Candidatos examinados por una consulta de radio de 1 km según el tamaño de celda de una rejilla",
        "Líneas en escalas logarítmicas con los candidatos examinados por una consulta de radio de 1 kilómetro según el tamaño de celda: con puntos uniformes pasa de 12,7 con celdas de 0,5 km a 934,8 con 20 km; con puntos agrupados de 894,4 a 16 106,8; la fuerza bruta examina 20 000 en ambos casos.",
        [("Puntos agrupados en una ciudad", [(0.5, 894.4, "894,4", "t"), (1, 1260.5, "1 260,5", "t"), (2, 2131.0, "2 131,0", "t"), (5, 5189.9, "5 189,9", "t"), (20, 16106.8, "16 106,8", "b")], "coral"),
         ("Puntos uniformes", [(0.5, 12.7, "12,7", "t"), (1, 18.0, "18,0", "t"), (2, 31.6, "31,6", "t"), (5, 98.6, "98,6", "t"), (20, 934.8, "934,8", "t")], "teal")],
        x_label="Tamaño de celda de la rejilla (km)", y_label="Candidatos examinados por consulta", log_x=True, log_y=True,
        x_ticks=[(0.5, "0,5"), (1, "1"), (2, "2"), (5, "5"), (20, "20")], y_ticks=[10, 100, 1000, 10000, 100000], point_labels="none",
        hlines=[(20000, "fuerza bruta: 20 000")],
        note='El índice reduce el trabajo de 20 000 a 18 candidatos cuando los datos se reparten por igual, y a 1 260 cuando se agrupan: la distribución de los datos decide cuánto ayuda. Una celda mucho mayor que el radio pierde la ventaja. Se cuentan candidatos, no milisegundos: no se midió ninguna base de datos espacial.', note_kind='teal', foot=SINT)


# ---------------------------------------------------------------- SE-298
def se286_pares() -> Fig:
    return line_chart(
        "Un flujo con 10 bifurcaciones (1 024 caminos): defectos de dos bifurcaciones que halla cada conjunto de pruebas",
        "Líneas con el porcentaje de defectos de dos bifurcaciones hallados y de conjuntos que ven cada rama en ambos valores según el número de pruebas aleatorias: 2 pruebas hallan 43,9 por ciento, 8 el 90,4 y 20 el 99,7; un conjunto de 9 pruebas diseñado por pares halla el 100 por ciento.",
        [("Defectos de dos bifurcaciones hallados", [(2, 43.9, "43,9", "t"), (5, 76.8, "76,8", "b"), (8, 90.4, "90,4", "b"), (12, 96.9, "96,9", "b"), (20, 99.7, "99,7", "b")], "teal"),
         ("Conjuntos que ven cada rama en ambos valores", [(2, 0, "0", "t"), (5, 52, "52", "t"), (8, 93, "93", "t"), (12, 100, "100", "t"), (20, 100, "100", "t")], "gold"),
         ("9 pruebas diseñadas por pares", [(9, 100, "100", "t")], "navy")],
        x_label="Pruebas aleatorias en el conjunto", y_label="Porcentaje (%)", point_labels="none",
        x_ticks=[(2, "2"), (5, "5"), (8, "8"), (9, "9"), (12, "12"), (20, "20")], y_ticks=[0, 20, 40, 60, 80, 100, 120], plot_h=320,
        note='Probar todos los caminos exige 1 024 ejecuciones y duplica con cada bifurcación; cubrir todos los pares exige 9. El cálculo supone que los defectos dependen como máximo de dos decisiones: uno que dependa de tres se escapa de los pares. 180 defectos posibles, 300 conjuntos aleatorios por fila.', note_kind='teal', foot=SINT)


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
    return line_chart(
        "Automatizaciones sin responsable activo si cada responsable se va con probabilidad del 15 % al año (500 flujos)",
        "Líneas con el porcentaje de automatizaciones sin responsable activo según los años: con un solo responsable, con o sin revisión anual, sube de 15,4 a 37,8 y 52,2 por ciento al año, a los tres y a los cinco; con dos responsables sin revisión llega a 30,8; con dos responsables y revisión anual se queda en 8,6.",
        [("Un responsable (con o sin revisión)", [(1, 15.4, "15,4", "t"), (3, 37.8, "37,8", "t"), (5, 52.2, "52,2", "t")], "coral"),
         ("Dos responsables, sin revisión", [(1, 2.0, "2,0", "t"), (3, 12.8, "12,8", "t"), (5, 30.8, "30,8", "t")], "gold"),
         ("Dos responsables, revisión anual", [(1, 2.0, "", "t"), (3, 5.6, "5,6", "b"), (5, 8.6, "8,6", "b")], "teal")],
        x_label="Años transcurridos", y_label="Automatizaciones sin responsable activo (%)", point_labels="none",
        x_ticks=[(1, "1 año"), (3, "3 años"), (5, "5 años")], y_ticks=[0, 10, 20, 30, 40, 50, 60],
        note='La revisión anual no sirve si no queda nadie a quien reasignar: solo cambia el resultado cuando hay al menos dos responsables y la revisión repone al que se fue. La tasa de salida del 15 % es un supuesto, no una medición de ninguna organización; el patrón (no basta revisar) es el hallazgo.', note_kind='coral', foot=SINT)


# ---------------------------------------------------------------- SE-299
def se287_ranking() -> Fig:
    return grouped_bars(
        "Diez dominios puntuados en seis criterios: cuánto cambia el ranking al variar los pesos (5 000 sorteos)",
        "Barras agrupadas con el porcentaje de sorteos en que se mantiene el primer lugar y el par de primeros del ranking según lo dispares que sean los pesos: con pesos casi iguales es 100 y 99,8; con pesos algo distintos 97,6 y 88,4; con pesos muy dispares 84,9 y 71,4.",
        ["Pesos casi iguales (50)", "Pesos algo distintos (10)", "Pesos muy dispares (3)"],
        [("Primer lugar igual", [100, 97.6, 84.9], "teal"), ("Primeros dos (conjunto) iguales", [99.8, 88.4, 71.4], "gold")],
        unit="Sorteos en que se mantiene (%)",
        note='El primer puesto es estable porque en este ejemplo un dominio puntúa alto en casi todo; la parte media del ranking no lo es. Los puntajes de 1 a 5 son un juicio ilustrativo del autor, no una medición de los dominios: el ejercicio muestra cómo revisar un ranking, no cuál es el orden verdadero.', note_kind='gold', foot=SINT)


def se287_acuerdo() -> Fig:
    return line_chart(
        "Dos evaluadores puntúan los mismos 60 criterios con ruido: acuerdo y cambio en los tres primeros",
        "Líneas con el acuerdo exacto y el porcentaje de pares en que los tres primeros son distintos según el ruido de cada evaluador: el acuerdo baja de 100 a 58,0, 36,4 y 30,3 por ciento con 0, 0,5, 1,0 y 1,5 puntos de ruido, y los tres primeros distintos suben de 0 a 24,3, 61,3 y 82,7.",
        [("Acuerdo exacto (%)", [(0, 100, "100,0", "r"), (0.5, 58.0, "58,0", "t"), (1.0, 36.4, "36,4", "t"), (1.5, 30.3, "30,3", "b")], "teal"),
         ("Tres primeros distintos (%)", [(0, 0, "0,0", "t"), (0.5, 24.3, "24,3", "b"), (1.0, 61.3, "61,3", "t"), (1.5, 82.7, "82,7", "t")], "coral")],
        x_label="Ruido de cada evaluador (puntos)", y_label="Porcentaje (%)", point_labels="none",
        x_ticks=[(0, "0"), (0.5, "0,5"), (1.0, "1,0"), (1.5, "1,5")], y_ticks=[0, 20, 40, 60, 80, 100],
        note='Un kappa de 0,84 suena alto y aun así el podio cambia en uno de cada cuatro pares de evaluadores. Antes de comparar dominios hay que calibrar la escala con ejemplos y reportar el acuerdo. 300 pares simulados; el ruido gaussiano es un modelo, no una medición de personas.', note_kind='coral', foot=SINT)


def se287_cobertura() -> Fig:
    return line_chart(
        "Controles frente a 14 riesgos de diez dominios: lo que cubre una lista corta común",
        "Línea con los riesgos cubiertos, de 14, según los controles elegidos: 1 control cubre 5, 2 cubren 8, 3 cubren 10, 4 cubren 12 y 6 cubren los 14; el dominio peor cubierto pasa de ciencia con 0 por ciento a juegos con 33 y audio y realidad extendida con 50.",
        [("Riesgos cubiertos", [(1, 5, "5 de 14 · peor: ciencia 0 %", "r"), (2, 8, "8 de 14 · peor: ML 0 %", "r"), (3, 10, "10 de 14 · peor: juegos 33 %", "r"),
                               (4, 12, "12 de 14 · peor: audio/XR 50 %", "r"), (6, 14, "14 de 14 · todos cubiertos", "r")], "teal")],
        x_label="Controles elegidos (de 8; el último punto es la cobertura voraz)", y_label="Riesgos cubiertos (de 14)", point_labels="none",
        x_ticks=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, ""), (6, "6"), (7, ""), (8, "")], y_ticks=[0, 2, 4, 6, 8, 10, 12, 14, 16],
        hlines=[(14, "14 riesgos distintos")],
        note='Una lista universal corta cubre mucho en promedio y deja a algún dominio casi sin protección. Los riesgos más repetidos (privacidad, duplicados, pérdida de datos) aparecen en cuatro dominios cada uno; los demás son propios de uno. La matriz de controles y riesgos es una construcción del autor.', note_kind='teal', foot=SINT)


# ---------------------------------------------------------------- SE-300
def se288_validador() -> Fig:
    return grouped_bars(
        "Validador de forma de un dosier: mutaciones detectadas de 25 por tipo",
        "Barras horizontales con las mutaciones detectadas, de 25, por un validador de forma: detecta 25 de 25 al borrar o vaciar una sección, cambiar una cifra en la sección de experimentos o quitar el enlace de las fuentes, y 0 de 25 al cambiar una cifra en la afirmación, invertir la conclusión, enlazar una página inexistente o sustituir un límite concreto por uno genérico.",
        ["Borrar una sección", "Vaciar una sección", "Cambiar una cifra en la sección de experimentos", "Quitar el enlace de las fuentes",
         "Cambiar una cifra en la afirmación", "Invertir la conclusión", "Enlazar una página inexistente", "Sustituir un límite concreto por uno genérico"],
        [("Detectada por el validador", [25, 25, 25, 25, 0, 0, 0, 0], "teal")],
        unit="Mutaciones detectadas (de 25)", horizontal=True, label_w=340, ticks=[0, 5, 10, 15, 20, 25],
        note='El validador ve la forma y las cifras que alguien le pidió cruzar; no ve el sentido. Las cuatro mutaciones que se le escapan son las que más dañan a un lector. Por eso el dosier necesita una revisión de contenido hecha por una persona, y el validador solo evita lo mecánico.', note_kind='coral', foot=SINT)


def se288_sensibilidad() -> Fig:
    return percentile_intervals(
        "Construir o comprar: cuánto mueve la diferencia de coste cada supuesto (base: construir cuesta 600 más)",
        "Intervalos horizontales con la diferencia de coste entre construir y comprar al variar cada supuesto por separado: la licencia anual la mueve de −17 400 a 9 600, la tarifa horaria de −7 000 a 12 000, las horas de construcción de −5 400 a 12 600, el mantenimiento de −4 800 a 11 400, el incidente propio de −6 600 a 7 800 y la integración de −5 400 a 3 600; todos cruzan el cero.",
        [("Licencia anual", [-17400, 9600]), ("Tarifa horaria", [-7000, 12000]), ("Horas de construcción", [-5400, 12600]),
         ("Horas de mantenimiento al año", [-4800, 11400]), ("Probabilidad de incidente propio", [-6600, 7800]), ("Horas de integración", [-5400, 3600])],
        unit="Diferencia de coste construir − comprar (unidades de coste)", marks=("mínimo", "máximo"), ref_lines=[(0, "empate")], label_w=230,
        note='Los nueve supuestos cambian el signo de la diferencia dentro de su rango: la decisión no se sostiene en el punto base. En 20 000 sorteos construir sale más barato el 36 % de las veces. El modelo y los rangos son un ejemplo del autor, no cifras de un proveedor ni de un equipo real.', note_kind='gold', foot=SINT)


def se288_huellas() -> Fig:
    return heatmap(
        "Huella SHA-256 del paquete: cambios que la alteran con y sin canonicalizar antes",
        "Mapa de calor con los ficheros, de 3, cuya huella SHA-256 cambia según la alteración y el método: sobre los bytes cambia en 3 de 3 con un cambio de saltos de línea, espacios finales o salto final y en 1 de 3 al reordenar claves de un JSON; tras canonicalizar no cambia en ninguno, y el cambio de una cifra altera la huella en 3 de 3 en ambos métodos.",
        ["Cambiar de LF a CRLF", "Añadir espacios al final de una línea", "Quitar el salto de línea final", "Reordenar las claves de un JSON", "Cambiar una cifra del contenido"],
        ["Huella sobre los bytes", "Huella tras canonicalizar"],
        [[3, 0], [3, 0], [3, 0], [1, 0], [3, 3]],
        unit="ficheros alterados", row_title="Cambio sobre tres ficheros", col_title="Ficheros con la huella alterada (de 3)",
        scale="coral", vmin=0, vmax=3, cell_fmt=lambda v: f"{int(v)} de 3", highlight=[(4, 0), (4, 1)], cell_h=42, label_w=250,
        note='Una huella sobre bytes crudos avisa de cambios que no importan (saltos de línea de Windows frente a Linux) y esa alarma constante enseña a ignorarla. Canonicalizar conserva la alarma para el cambio de contenido. Lo que ninguna huella dice es si el contenido es correcto: solo si cambió.', note_kind='teal', foot=SINT)


FIGURES = {
    "se-293-latencia-y-subcargas-de-audio.svg": se281_buffer,
    "se-293-aliasing-de-un-tono.svg": se281_alias,
    "se-293-fotogramas-fuera-de-presupuesto.svg": se281_cuadros,
    "se-294-dinero-con-coma-flotante.svg": se282_redondeo,
    "se-294-mutantes-de-un-libro-mayor.svg": se282_mutantes,
    "se-294-cobros-duplicados.svg": se282_idempotencia,
    "se-295-anonimizar-por-generalizacion.svg": se283_kanon,
    "se-295-fusion-de-fichas.svg": se283_fusion,
    "se-295-fatiga-de-alarmas.svg": se283_alarmas,
    "se-296-prueba-de-trabajo.svg": se284_pow,
    "se-296-doble-gasto.svg": se284_doble_gasto,
    "se-296-reentrada-en-un-contrato.svg": se284_reentrada,
    "se-297-distancia-en-grados.svg": se285_distancia,
    "se-297-un-ano-de-reloj.svg": se285_reloj,
    "se-297-indice-de-rejilla.svg": se285_indice,
    "se-298-caminos-frente-a-pares.svg": se286_pares,
    "se-298-eventos-duplicados.svg": se286_duplicados,
    "se-298-automatizaciones-huerfanas.svg": se286_huerfanas,
    "se-299-estabilidad-de-un-ranking.svg": se287_ranking,
    "se-299-acuerdo-entre-evaluadores.svg": se287_acuerdo,
    "se-299-controles-frente-a-riesgos.svg": se287_cobertura,
    "se-300-mutaciones-de-un-dosier.svg": se288_validador,
    "se-300-sensibilidad-de-supuestos.svg": se288_sensibilidad,
    "se-300-huella-del-paquete.svg": se288_huellas,
}
