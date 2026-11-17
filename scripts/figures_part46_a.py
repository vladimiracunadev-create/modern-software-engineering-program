"""Figures for SE-553 to SE-558 (ML in production: runs of numpy and scikit-learn code over the synthetic Avisos-ML case, seed 46; Windows CPython 3.12.9, numpy 2.4.4, scikit-learn 1.8.0; no language model was invoked, no GPU was used)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, line_chart, percentile_intervals

from figures_part40_a import flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9, numpy 2.4.4 y scikit-learn 1.8.0; los recuentos con semilla se repiten y los tiempos varían de un equipo a otro."
MODELO = "Modelo sintético con parámetros del autor y semilla fija 46; muestra un mecanismo, no mide un sistema real."


def signed(before: float, after: float) -> str:
    return f"{after - before:+.3f}".replace(".", ",")


# ---------------------------------------------------------------- SE-553
def se553_fallas() -> Fig:
    return dumbbell(
        "Un mismo modelo ante cuatro fallas en servicio: AUC fuera de línea y con cada falla",
        "Mancuernas con el AUC fuera de línea y con cada falla en servicio: unidad distinta 0,845 a 0,818, deriva de covariables 0,845 a 0,851, deriva de concepto 0,845 a 0,796 y historial en cero 0,845 a 0,741.",
        [("Unidad distinta (tasa de lectura x100)", 0.845, 0.818), ("Deriva de covariables (carga +2,5 tareas)", 0.845, 0.851),
         ("Deriva de concepto (peso del historial x0,25)", 0.845, 0.796), ("Historial de tardanzas llega en cero", 0.845, 0.741)],
        unit="AUC", names=("Fuera de línea", "Con la falla"), decimals=3, delta=signed, lower_is_better=False, label_w=320,
        note="La deriva de covariables mueve las entradas más que ninguna y no daña; la deriva de concepto no mueve ninguna entrada y baja 0,049; el historial en cero es la mayor caída, 0,104, sin ningún valor fuera de rango. Las magnitudes de cada falla las eligió el autor.",
        note_kind="gold", foot=MODELO)


def se553_realimentacion() -> Fig:
    return grouped_bars(
        "El modelo cambia lo que mide: tasa de entregas tardías entre los marcados y AUC antes y después de reentrenar",
        "Barras agrupadas con la tasa de entregas tardías entre los 5408 marcados, 0,681 real sin recordatorio y 0,340 observada con recordatorio, y el AUC en datos sin intervención, 0,852 del modelo original y 0,843 del reentrenado con etiquetas observadas.",
        ["Entregas tardías entre los 5 408 marcados", "AUC en datos sin intervención"],
        [("Real sin recordatorio / modelo original", [0.681, 0.852], "navy"), ("Observado con recordatorio / reentrenado con lo observado", [0.340, 0.843], "teal")],
        unit="Proporción", decimals=3, width=860, plot_h=270,
        note="El recordatorio, supuesto de efecto del 50 %, reduce a la mitad la tasa que el equipo ve entre los marcados, de modo que esa cifra mezcla la calidad del modelo con la eficacia del recordatorio. El AUC casi no se mueve porque la intervención alcanza solo al 18 % de la población.",
        note_kind="coral", foot=MODELO)


def se553_ciclo_fallas() -> Fig:
    return flow(
        "Los diez eslabones de un sistema de ML y el eslabón donde entra cada falla medida",
        "Diagrama con diez eslabones del ciclo de vida y cuatro fallas ubicadas en su eslabón: el fallo aguas arriba entra por los datos de origen, la unidad distinta por las características y el servicio, la deriva de covariables por el servicio y la deriva de concepto por las etiquetas, con el bucle de realimentación como retorno del servicio a los datos.",
        [[("Datos de origen\nEntra: historial en cero", "coral"), ("Etiquetas\nEntra: deriva de concepto", "coral"), ("Características\nEntra: unidad distinta", "coral"), ("Entrenamiento", "teal"), ("Evaluación", "teal")],
         [("Registro del modelo", "teal"), ("Despliegue", "teal"), ("Servicio\nEntra: deriva de covariables", "coral"), ("Monitoreo\nVe: tasa de marcados, PSI, AUC", "gold"), ("Reentrenamiento", "teal")]],
        note="El servicio devuelve decisiones a los datos de origen: ese retorno es el bucle de realimentación y convierte un fallo de un eslabón en un fallo de los demás. Cada falla necesita una señal distinta: rango para la unidad, distribución para la covariable, etiquetas para el concepto.",
        note_kind="gold", box_h=104, gap=24, foot=MODELO)


# ---------------------------------------------------------------- SE-554
def se554_fuga() -> Fig:
    return dumbbell(
        "Una característica construida con la etiqueta: AUC fuera de línea y en servicio",
        "Mancuernas con el AUC fuera de línea y en servicio de dos modelos: el modelo sin fuga pasa de 0,851 a 0,851 y el modelo con una característica construida con la etiqueta pasa de 0,987 fuera de línea a 0,837 en servicio.",
        [("Modelo sin fuga", 0.851, 0.851), ("Con una característica construida con la etiqueta", 0.987, 0.837)],
        unit="AUC", names=("Fuera de línea", "En servicio"), decimals=3, delta=signed, lower_is_better=False, label_w=330,
        note="El modelo con fuga tiene la mejor puntuación fuera de línea de todas y termina por debajo del modelo limpio: aprendió a apoyarse en una señal que en servicio llega como la media histórica. La fuga es la etiqueta más un ruido de desviación 0,35.",
        note_kind="coral", foot=MODELO)


def se554_ruido() -> Fig:
    xs = [0, 5, 10, 20, 30, 40]
    return line_chart(
        "Etiquetas de entrenamiento invertidas al azar: AUC en datos limpios",
        "Líneas con el AUC en datos limpios según el porcentaje de etiquetas de entrenamiento invertidas al azar: 0,847 con 0 por ciento, 0,847 con 5, 0,846 con 10, 0,841 con 20, 0,811 con 30 y 0,773 con 40.",
        [("AUC en datos limpios", list(zip(xs, [0.847, 0.847, 0.846, 0.841, 0.811, 0.773])), "teal")],
        x_label="Etiquetas de entrenamiento invertidas (%)", y_label="AUC en datos limpios", x_ticks=[(x, f"{x} %") for x in xs],
        y_ticks=[0.76, 0.78, 0.80, 0.82, 0.84, 0.86], y_zero=False, decimals=3, plot_h=290,
        note="El boosting aguanta el ruido simétrico hasta el 20 % casi sin pérdida y cae de forma acelerada después. El ruido sistemático, concentrado en un segmento o en un sentido, no se promedia y daña más con menos porcentaje.",
        note_kind="gold", foot=MODELO)


def se554_paridad() -> Fig:
    return dumbbell(
        "La misma característica implementada dos veces: AUC con la definición del entrenamiento y con la del servicio",
        "Mancuernas con el AUC del modelo con la definición de entrenamiento y con una definición distinta en servicio: idéntica 0,846; horas restantes redondeadas a días, con el 100 por ciento de los valores distintos, 0,845; carga con otra definición, con el 95 por ciento de los valores distintos, 0,834.",
        [("Idéntica (misma función)", 0.846, 0.846), ("Horas restantes redondeadas a días (100 % distintas)", 0.846, 0.845), ("Carga con otra definición (95 % distintas)", 0.846, 0.834)],
        unit="AUC", names=("Definición del entrenamiento", "Definición del servicio"), decimals=3, delta=signed, lower_is_better=False, label_w=330,
        note="Cambiar el 100 % de las horas restantes casi no cuesta porque el modelo les da poco peso; cambiar la definición de la carga cuesta más. La prueba de paridad por característica separa las divergencias que duelen de las que no.",
        note_kind="teal", foot=MODELO)


# ---------------------------------------------------------------- SE-555
def se555_dispersion() -> Fig:
    return grouped_bars(
        "Con 500 filas de entrenamiento, cuánto varía el AUC por azar frente a la diferencia entre dos configuraciones",
        "Barras con la desviación del AUC con 500 filas de entrenamiento: 0,0056 por la semilla del modelo con los mismos datos, 0,0072 por la muestra de entrenamiento con la misma semilla y 0,0074 en la diferencia entre profundidad 5 y profundidad 4, cuya media es de apenas 0,0026 a favor de la profundidad 4.",
        ["Semilla del modelo, mismos datos (40 corridas)", "Muestra de entrenamiento, misma semilla (40 corridas)", "Diferencia entre profundidad 5 y 4 (60 pares)"],
        [("Desviación estándar del AUC", [0.0056, 0.0072, 0.0074], "navy")],
        unit="Desviación estándar del AUC", horizontal=True, decimals=4, label_w=330, ref_lines=[(0.0026, "Diferencia media entre configuraciones")],
        note="La desviación de la diferencia es casi tres veces su media: con esta cantidad de datos una sola corrida no puede ver la diferencia, y la profundidad 5 ganó 21 de 60 comparaciones aunque en promedio fue algo peor.",
        note_kind="coral", foot=MODELO)


def se555_optimismo() -> Fig:
    return line_chart(
        "Elegir el mejor de N candidatos casi idénticos con una validación de 300 filas: optimismo de la elección",
        "Líneas con la brecha entre el AUC de validación y el de prueba del candidato elegido según el número de candidatos probados: 0,0011 con 1, 0,0052 con 5, 0,0081 con 20 y 0,0101 con 80, con una validación de 300 filas.",
        [("Validación menos prueba del elegido", [(1, 0.0011), (5, 0.0052), (20, 0.0081), (80, 0.0101)], "coral")],
        x_label="Candidatos probados", y_label="AUC de validación menos AUC de prueba", log_x=True, x_ticks=[(1, "1"), (5, "5"), (20, "20"), (80, "80")],
        y_ticks=[0, 0.002, 0.004, 0.006, 0.008, 0.010, 0.012], decimals=4, plot_h=290,
        note="Los candidatos valen lo mismo, de modo que toda la brecha es suerte: el elegido es el más afortunado en esa validación. De 1 a 5 candidatos se obtiene casi la mitad de la brecha final. Media de 40 repeticiones.",
        note_kind="gold", foot=MODELO)


def se555_registro() -> Fig:
    return flow(
        "Qué determina una corrida de entrenamiento y qué decide si un modelo se promueve",
        "Diagrama del registro de una corrida: datos, etiquetas, configuración, semilla y versiones producen una corrida; de ella salen el modelo con su huella y el registro con las huellas y la métrica; una comparación con la dispersión decide si se promueve o no.",
        [[("Datos y etiquetas\nHuella", "navy"), ("Configuración\nHiperparámetros, huella", "navy"), ("Semilla y versiones\nnumpy 2.4.4, scikit-learn 1.8.0", "navy"), ("Código\nCommit", "navy")],
         [("Corrida de entrenamiento", "teal"), ("Modelo con huella", "teal"), ("run.json\nHuellas, semilla, métrica", "teal"), ("¿Diferencia mayor que el ruido?\nSí: se promueve", "coral")]],
        note="La decisión de promover no depende de la métrica sola sino de la métrica y de la dispersión medida con varias semillas y muestras. Sin las huellas de los cuatro insumos, la corrida no se puede repetir ni comparar.",
        note_kind="gold", box_h=104, gap=36, foot=MODELO)


# ---------------------------------------------------------------- SE-556
def se556_prevalencia() -> Fig:
    return grouped_bars(
        "Con una prevalencia del 2,8 %: el modelo frente a un clasificador que siempre dice que no",
        "Barras agrupadas con tres métricas del modelo y de un clasificador que siempre dice no cuando la prevalencia es 0,028: exactitud 0,972 y 0,972, recall con umbral 0,5 de 0,074 y 0, y precisión promedio de 0,236 y 0,028.",
        ["Exactitud", "Recall con umbral 0,5", "Precisión promedio (PR-AUC)"],
        [("Modelo", [0.972, 0.074, 0.236], "navy"), ("Siempre dice que no", [0.972, 0.0, 0.028], "grey")],
        unit="Valor de la métrica (0 a 1)", decimals=3, plot_h=270,
        note="La exactitud es idéntica y no distingue al modelo del clasificador trivial; el recall y la precisión promedio sí. El AUC del modelo es 0,870: ordena bien pero el umbral de 0,5 heredado de otra población detecta a uno de cada trece estudiantes en riesgo.",
        note_kind="coral", foot=MODELO)


def se556_umbral() -> Fig:
    return line_chart(
        "El umbral que minimiza el costo según cuánto más cuesta una omisión que una falsa alarma",
        "Línea con el umbral óptimo según cuánto más cuesta una omisión que una falsa alarma: 0,51 con costos iguales, 0,16 con relación 1 a 5 y 0,09 con relación 1 a 10; las falsas alarmas correspondientes son 1199, 5849 y 8350.",
        [("Umbral óptimo", [(1, 0.51), (5, 0.16), (10, 0.09)], "teal")],
        x_label="Costo de una omisión frente a una falsa alarma", y_label="Umbral que minimiza el costo", x_ticks=[(1, "1 a 1"), (5, "5 a 1"), (10, "10 a 1")],
        y_ticks=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6], decimals=2, plot_h=280,
        note="Con 20 000 estudiantes, el umbral óptimo produce 1 199 falsas alarmas y 2 629 omisiones con costos iguales, 5 849 y 598 con relación 5 a 1, y 8 350 y 220 con 10 a 1: pasar de 1 a 10 multiplica por siete las falsas alarmas. El costo es lineal y supuesto.",
        note_kind="gold", foot=MODELO)


def se556_intervalos() -> Fig:
    return percentile_intervals(
        "Intervalo del 95 % del AUC (bootstrap) según el tamaño de la evaluación",
        "Intervalos del AUC con bootstrap del 95 por ciento según el tamaño de la evaluación: con 200 filas 0,829 en el intervalo de 0,774 a 0,902; con 2000 filas 0,852 en el intervalo de 0,829 a 0,871; con 20000 filas 0,849 en el intervalo de 0,844 a 0,854.",
        [("200 filas", [0.774, 0.829, 0.902]), ("2 000 filas", [0.829, 0.852, 0.871]), ("20 000 filas", [0.844, 0.849, 0.854])],
        unit="AUC", marks=("2,5 %", "AUC medido", "97,5 %"), decimals=3,
        note="Con 200 filas el intervalo mide 0,128 y cubre valores que cambiarían cualquier decisión; con 20 000 mide 0,011. Una diferencia de 0,02 entre dos modelos solo se ve con la evaluación grande. 200 remuestreos de una sola muestra, con observaciones independientes.",
        note_kind="teal", foot=MODELO)


# ---------------------------------------------------------------- SE-557
def se557_curva_datos() -> Fig:
    xs = [50, 200, 1000, 5000, 20000]
    return line_chart(
        "AUC en la población nueva según las filas etiquetadas: ajustar el modelo base frente a entrenar desde cero",
        "Líneas con el AUC en la población nueva según las filas etiquetadas: el modelo ajustado vale 0,837, 0,838, 0,841, 0,842 y 0,842 con 50, 200, 1000, 5000 y 20000 filas; el entrenado desde cero vale 0,792, 0,823, 0,808, 0,828 y 0,841; el modelo base sin adaptar vale 0,840.",
        [("Ajuste del modelo base", list(zip(xs, [0.837, 0.838, 0.841, 0.842, 0.842])), "teal"), ("Entrenado desde cero", list(zip(xs, [0.792, 0.823, 0.808, 0.828, 0.841])), "coral")],
        x_label="Filas etiquetadas de la población nueva", y_label="AUC en la población nueva", log_x=True, x_ticks=[(x, f"{x:,}".replace(",", " ")) for x in xs],
        y_ticks=[0.78, 0.80, 0.82, 0.84, 0.86], y_zero=False, hlines=[(0.840, "Modelo base sin adaptar")], point_labels="none", decimals=3, plot_h=300,
        note="Con 50 filas el ajuste gana 0,045 al entrenamiento desde cero; con 20 000 las dos estrategias se igualan y el modelo base solo, sin ninguna adaptación, ya valía 0,840. Cada punto es una corrida con una semilla: diferencias de 0,005 están dentro del ruido.",
        note_kind="gold", foot=MODELO)


def se557_parametros() -> Fig:
    return grouped_bars(
        "Parámetros que entrena una adaptación de rango bajo en una capa de 4 096 por 4 096",
        "Barras horizontales con el porcentaje de los 16777216 parámetros de una capa de 4096 por 4096 que entrena una adaptación de rango bajo: 0,20 por ciento con rango 4, 0,39 con rango 8, 0,78 con rango 16 y 3,12 con rango 64, frente al 100 por ciento del ajuste completo.",
        ["Rango 4 (32 768)", "Rango 8 (65 536)", "Rango 16 (131 072)", "Rango 64 (524 288)", "Ajuste completo (16 777 216)"],
        [("Porcentaje de la capa que se entrena", [0.20, 0.39, 0.78, 3.12, 100.0], "navy")],
        unit="% de los parámetros de la capa", horizontal=True, log=True, decimals=2, label_w=230,
        note="Aritmética de una sola capa: r por (d más k) parámetros frente a d por k. Menos parámetros entrenables no implica menos cómputo en la pasada hacia adelante ni menos memoria de activaciones, y la calidad depende de la tarea.",
        note_kind="gold", foot="Aritmética exacta del conteo de parámetros; no es una medición de ningún modelo.")


def se557_computo() -> Fig:
    return grouped_bars(
        "Horas de un acelerador para entrenar un modelo de 7 000 millones de parámetros según los tokens",
        "Barras horizontales en escala logarítmica con las horas de un acelerador que implica la regla de seis operaciones por parámetro y por token para un modelo de 7000 millones de parámetros: 1,2 horas con 10 millones de tokens, 117 horas con 1000 millones y 116700 horas con un billón, suponiendo 1e14 operaciones por segundo sostenidas.",
        ["10 millones de tokens", "1 000 millones de tokens", "1 billón de tokens"],
        [("Horas de un acelerador", [1.2, 116.7, 116666.7], "navy")],
        unit="Horas con 1e14 operaciones por segundo sostenidas", horizontal=True, log=True, decimals=1, label_w=210,
        note="Cada barra es cien veces la anterior porque los tokens se multiplican por cien. Es aritmética con la regla publicada de seis operaciones por parámetro y por token y un rendimiento sostenido supuesto, no una medición de ningún acelerador.",
        note_kind="gold", foot="Aritmética con supuestos declarados; no es una medición.")


# ---------------------------------------------------------------- SE-558
def se558_costo_lote() -> Fig:
    pts = [(1, 43.5), (2, 68.2), (4, 31.45), (8, 21.15), (16, 12.16), (32, 9.75), (64, 5.17), (128, 3.83), (256, 2.89), (512, 2.47), (1024, 8.32)]
    return line_chart(
        "Costo por petición de una red pequeña según el tamaño del lote",
        "Línea con los microsegundos por petición de una red pequeña según el tamaño del lote, en escala logarítmica: 43,5 con 1 petición, 31,5 con 4, 12,2 con 16, 5,2 con 64, 2,9 con 256, 2,5 con 512 y 8,3 con 1024.",
        [("Microsegundos por petición", pts, "navy")],
        x_label="Peticiones por lote", y_label="Microsegundos por petición", log_x=True, log_y=True, x_ticks=[(x, str(x)) for x in (1, 4, 16, 64, 256, 1024)],
        y_ticks=[2, 5, 10, 20, 50, 100], point_labels="none", annotations=[(512, 2.47, "Mínimo: 2,5 µs con 512", -40, -34)], decimals=1, plot_h=300,
        note="El costo fijo de cada llamada se reparte: de 1 a 512 peticiones el costo por petición baja unas diecisiete veces, y con 1 024 repunta a 8,3 µs. Con dos peticiones fue peor que con una. Mejor tiempo de 40 repeticiones en una CPU de escritorio con varios hilos.",
        note_kind="coral", foot=EJEC)


def se558_lote_dinamico() -> Fig:
    return grouped_bars(
        "Lote dinámico con una carga del 80 % de la capacidad sin lotes: p50 y p99 según la espera y el lote máximos",
        "Barras agrupadas con el p50 y el p99 en milisegundos de cinco configuraciones de lote dinámico con una carga del 80 por ciento de la capacidad sin lotes: sin espera y lote 1, 0,10 y 0,47; 0,5 ms y lote 8, 0,32 y 0,64; 2 ms y lote 32, 1,12 y 2,21; 5 ms y lote 64, 2,03 y 4,25; 20 ms y lote 256, 7,67 y 15,16.",
        ["Sin espera, lote 1", "0,5 ms, lote 8", "2 ms, lote 32", "5 ms, lote 64", "20 ms, lote 256"],
        [("p50", [0.10, 0.32, 1.12, 2.03, 7.67], "teal"), ("p99", [0.47, 0.64, 2.21, 4.25, 15.16], "navy")],
        unit="Milisegundos", decimals=2, plot_h=280,
        note="A esta carga el rendimiento servido es el mismo en las cinco configuraciones (unas 18 340 peticiones por segundo): esperar solo añade latencia porque el servicio sin lotes ya tenía holgura. Llegadas de Poisson, un servidor y tiempo de servicio medido e interpolado.",
        note_kind="gold", foot=EJEC)


def se558_sobrecarga() -> Fig:
    return dumbbell(
        "p99 con carga igual, doble y cuádruple de la capacidad sin lotes: sin lotes y con lote dinámico de 2 ms y 64",
        "Mancuernas en escala logarítmica con el p99 en milisegundos sin lotes y con lote dinámico de 2 ms y 64: con carga igual a la capacidad sin lotes 9,4 y 2,3, con el doble 858 y 1,9, con el cuádruple 1291 y 1,1.",
        [("Carga igual a la capacidad sin lotes", 9.4, 2.30), ("Doble de la capacidad sin lotes", 858.3, 1.90), ("Cuádruple de la capacidad sin lotes", 1290.5, 1.11)],
        unit="p99 en milisegundos", names=("Sin lotes", "Lote dinámico 2 ms y 64"), log=True, decimals=1, delta=lambda b, a: f"×{b / a:,.0f}".replace(",", " "), label_w=290,
        note="Sin lotes, la cola crece mientras dura la sobrecarga y el p99 depende de cuántas peticiones se simulan (40 000); con lotes, la capacidad por petición es unas quince veces mayor y el p99 casi no se mueve. Una cola sin límite no es una solución en ningún caso.",
        note_kind="coral", foot=EJEC)


FIGURES = {
    "se-553-fallas.svg": se553_fallas,
    "se-553-realimentacion.svg": se553_realimentacion,
    "se-553-ciclo-fallas.svg": se553_ciclo_fallas,
    "se-554-fuga.svg": se554_fuga,
    "se-554-ruido-etiquetas.svg": se554_ruido,
    "se-554-paridad.svg": se554_paridad,
    "se-555-dispersion.svg": se555_dispersion,
    "se-555-optimismo.svg": se555_optimismo,
    "se-555-registro.svg": se555_registro,
    "se-556-prevalencia.svg": se556_prevalencia,
    "se-556-umbral-costo.svg": se556_umbral,
    "se-556-intervalos.svg": se556_intervalos,
    "se-557-curva-datos.svg": se557_curva_datos,
    "se-557-parametros.svg": se557_parametros,
    "se-557-computo.svg": se557_computo,
    "se-558-costo-lote.svg": se558_costo_lote,
    "se-558-lote-dinamico.svg": se558_lote_dinamico,
    "se-558-sobrecarga.svg": se558_sobrecarga,
}
