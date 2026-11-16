"""Figures for SE-277 to SE-280 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, heatmap, line_chart
from figures_part07_a import bars

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-277
def se277_orden() -> Fig:
    return grouped_bars(
        "Sumar 20 000 números de magnitudes muy distintas: el orden cambia el resultado",
        "Barras horizontales con el número de totales distintos al sumar veinte mil números de magnitudes muy distintas en mil órdenes aleatorios: la suma ingenua da 205 resultados distintos; la suma ordenada por magnitud, la suma por pares y math.fsum dan uno solo.",
        ["Suma ingenua, 1000 órdenes aleatorios", "Suma ingenua ordenada por magnitud", "Suma por pares (recursiva)", "math.fsum (referencia exacta)"],
        [("Resultados distintos", [205, 1, 1, 1], "coral")],
        unit="Totales distintos en 1 000 órdenes", horizontal=True, label_w=250,
        note='Sumar en coma flotante no es asociativo: el mismo conjunto de datos produce 205 totales distintos según el orden en que lo recorre un procesador, un hilo o una partición. Cambiar el número de núcleos puede cambiar la última cifra publicada. El error absoluto es pequeño frente a un total de unos 2·10⁹, pero basta para que una comparación exacta entre ejecuciones falle.', note_kind='gold', foot=SINT)


def se277_semillas() -> Fig:
    return line_chart(
        "Estimar π con 200 semillas: lo que una sola ejecución no dice",
        "Líneas con el valor mínimo y máximo de la estimación de pi entre doscientas semillas según los puntos por ejecución: con mil puntos el rango va de 2,988 a 3,292, con diez mil de 3,090 a 3,183 y con cien mil de 3,128 a 3,158; el embudo se cierra alrededor de 3,1416.",
        [("Máximo observado", [(1000, 3.292, "3,292", "t"), (10000, 3.183, "3,183", "t"), (100000, 3.158, "3,158", "t")], "coral"),
         ("Mínimo observado", [(1000, 2.988, "2,988", "b"), (10000, 3.090, "3,090", "b"), (100000, 3.128, "3,128", "b")], "teal")],
        x_label="Puntos por ejecución", y_label="Estimación de π", log_x=True,
        x_ticks=[(1000, "1 000"), (10000, "10 000"), (100000, "100 000")], y_ticks=[2.9, 3.0, 3.1, 3.2, 3.3], y_zero=False,
        hlines=[(3.1416, "π = 3,1416")], point_labels="none", plot_h=300,
        note='Con una semilla fija la misma ejecución da siempre el mismo número, y eso es reproducibilidad exacta. No es evidencia de que el resultado sea estable: con mil puntos, otra semilla da cualquier valor entre 2,99 y 3,29. Publicar la semilla permite repetir; variar las semillas permite saber cuánto vale la cifra.', note_kind='teal', foot=SINT)


def se277_caos() -> Fig:
    return line_chart(
        "Pasos hasta que dos trayectorias casi idénticas se separan en 0,1 (mapa logístico, r = 3,9)",
        "Líneas con los pasos que tardan en separarse dos trayectorias del mapa logístico caótico según la diferencia inicial: la mediana sube de 23 pasos con diez a la menos seis a 65 con diez a la menos quince, unos 14 pasos por cada tres décadas; en el régimen estable no divergen en quinientos pasos.",
        [("Percentil 90", [(6, 29, "29", "t"), (9, 45, "45", "t"), (12, 59, "59", "t"), (15, 75, "75", "t")], "coral"),
         ("Mediana", [(6, 23, "23", "r"), (9, 37, "37", "t"), (12, 50, "50", "t"), (15, 65, "65", "t")], "navy"),
         ("Percentil 10", [(6, 20, "20", "b"), (9, 33, "33", "b"), (12, 46, "46", "b"), (15, 59, "59", "b")], "teal")],
        x_label="Diferencia inicial entre las dos trayectorias", y_label="Pasos hasta separarse en 0,1",
        x_ticks=[(6, "10⁻⁶"), (9, "10⁻⁹"), (12, "10⁻¹²"), (15, "10⁻¹⁵")], y_ticks=[0, 20, 40, 60, 80], point_labels="none",
        annotations=[(6, 29, "Control estable (r = 2,8): no diverge en 500 pasos", 40, -95)],
        note='Cada mil millonésima de diferencia compra apenas unos 14 pasos: la divergencia crece de forma exponencial, así que mejorar la precisión de la máquina retrasa el desacuerdo pero no lo elimina. Si el modelo es caótico, reproducir bit a bit una trayectoria larga en otra plataforma no es un objetivo realista; hay que reproducir estadísticos.', note_kind='coral', foot=SINT)


# ---------------------------------------------------------------- SE-278
def se278_reintentos() -> Fig:
    return grouped_bars(
        "Cargar 10 000 filas en lotes de 100 con fallos a mitad de lote y reintentos",
        "Barras agrupadas con las filas duplicadas tras cargar 10 000 filas con reintentos: añadir al final deja 0, 442 y 867 duplicadas si fallan el 0, el 5 y el 20 por ciento de los lotes; escribir por clave deja siempre 0 duplicadas.",
        ["0 % de lotes fallan", "5 % de lotes fallan", "20 % de lotes fallan"],
        [("Añadir al final", [0, 442, 867], "coral"), ("Escribir por clave (upsert)", [0, 0, 0], "teal")],
        unit="Filas duplicadas (de 10 000 cargadas)",
        note='El reintento es correcto solo si repetir la escritura no cambia el resultado. Añadir al final no es repetible: cada reintento duplica lo que ya se había escrito antes del corte. La escritura por clave es idempotente. Simulación con cortes en un punto aleatorio del lote y hasta diez intentos.', note_kind='coral', foot=SINT)


def se278_tardios() -> Fig:
    items = [
        ("Espera de 5 s", 50.17, "coral", "50,2 % descartado"),
        ("15 s", 13.57, "coral", "13,6 %"),
        ("30 s", 3.55, "gold", "3,6 %"),
        ("60 s", 0.66, "gold", "0,66 %"),
        ("120 s", 0.06, "teal", "0,06 %"),
        ("300 s", 0.0, "teal", "0 %"),
    ]
    return bars("Eventos que llegan después de cerrar su ventana según la tolerancia de retraso",
                "Barras: con retraso lognormal de mediana 5 segundos, una tolerancia de 5 segundos descarta el 50,2 por ciento de los eventos, 15 segundos el 13,6, 30 segundos el 3,6, 60 segundos el 0,66, 120 segundos el 0,06 y 300 segundos ninguno.",
                items, 11, "Retraso de llegada lognormal (mediana 5 s, p99 51 s, máximo 351 s) sobre 100 000 eventos. Cada tolerancia compra completitud a costa de latencia: esperar 120 s deja los resultados abiertos dos minutos. El 0 % exacto depende de esta muestra, no de la física.",
                label_w=190, width=960, note_kind="gold", foot=SINT)


def se278_sesgo() -> Fig:
    return line_chart(
        "Carga de la partición más cargada frente a la media (8 particiones, 200 000 filas, 1 000 claves)",
        "Líneas con la carga de la partición más cargada frente a la media según el exponente de Zipf: sin sal sube de 1,01 con claves uniformes a 1,35 con exponente 0,8, 2,03 con 1,1 y 3,43 con 1,5; con una sal de 8 se queda en 1,01 en todos los casos.",
        [("Sin sal", [(0, 1.01, "1,01", "b"), (0.8, 1.35, "1,35", "t"), (1.1, 2.03, "2,03", "t"), (1.5, 3.43, "3,43", "t")], "coral"),
         ("Con sal de 8", [(0, 1.01, "", "t"), (0.8, 1.01, "1,01", "t"), (1.1, 1.01, "1,01", "t"), (1.5, 1.01, "1,01", "t")], "teal")],
        x_label="Exponente de Zipf (0 = claves uniformes)", y_label="Carga máxima / carga media",
        x_ticks=[(0, "0"), (0.5, "0,5"), (1.0, "1,0"), (1.5, "1,5")], y_ticks=[0, 1, 2, 3, 4], point_labels="none",
        note='El reparto por clave es equilibrado solo si las claves lo son: una sola partición con 3,4 veces la media fija el tiempo total del trabajo. Salar la clave reparte la carga a cambio de un paso más para recombinar los resultados parciales. Las claves y los exponentes son sintéticos.', note_kind='gold', foot=SINT)


# ---------------------------------------------------------------- SE-279
def se279_fuga() -> Fig:
    return dumbbell(
        "Exactitud de un umbral sobre una variable con y sin fuga de la etiqueta (4 000 casos por conjunto)",
        "Puntos unidos por una línea con la exactitud en prueba y en producción de dos variables: la señal real pasa de 0,742 a 0,755; la copia ruidosa de la etiqueta cae de 0,899 a 0,515 porque en producción esa copia no existe.",
        [("Señal real (x), sin fuga", 0.742, 0.755), ("Copia ruidosa de la etiqueta (z), con fuga", 0.899, 0.515)],
        unit="Exactitud del umbral (0 a 1)", names=("En prueba", "En producción"), decimals=3, lower_is_better=False,
        delta=lambda a, b: ("+" if b > a else "−") + f"{abs(b - a):.3f}".replace(".", ","), label_w=250,
        note='La métrica de prueba subió 16 puntos justo cuando el modelo dejó de aprender el fenómeno y empezó a leer la respuesta. Una exactitud sorprendentemente alta es una pista para buscar fuga, no para celebrar. La fuga se detecta preguntando, variable por variable, si existiría en el momento de predecir.', note_kind='coral', foot=SINT)


def se279_prevalencia() -> Fig:
    return line_chart(
        "Un detector con sensibilidad 0,90 y especificidad 0,95 según la prevalencia del evento",
        "Líneas en escala logarítmica según la prevalencia del evento, con sensibilidad 0,90 y especificidad 0,95: la exactitud se mantiene entre 0,925 y 0,950, la regla «siempre no» sube de 0,500 a 0,999 y la proporción de avisos reales cae de 0,947 con el 50 por ciento a 0,154 con el 1 por ciento y 0,018 con el 0,1.",
        [("Exactitud del detector", [(0.1, 0.950, "0,950", "b"), (1, 0.950, "0,950", "b"), (10, 0.945, "0,945", "t"), (50, 0.925, "0,925", "b")], "teal"),
         ("Exactitud de «siempre no»", [(0.1, 0.999, "0,999", "t"), (1, 0.990, "0,990", "t"), (10, 0.900, "0,900", "b"), (50, 0.500, "0,500", "t")], "gold"),
         ("De cada aviso, proporción real", [(0.1, 0.018, "0,018", "t"), (1, 0.154, "0,154", "t"), (10, 0.667, "0,667", "b"), (50, 0.947, "0,947", "t")], "coral")],
        x_label="Prevalencia del evento (%)", y_label="Proporción (0 a 1)", log_x=True,
        x_ticks=[(0.1, "0,1 %"), (1, "1 %"), (10, "10 %"), (50, "50 %")], y_ticks=[0, 0.2, 0.4, 0.6, 0.8, 1], point_labels="none", plot_h=320,
        note='Con el 1 % de casos, 85 de cada 100 avisos son falsos aunque el detector parezca bueno (0,95 de exactitud). Y la regla que nunca avisa saca 0,99. La exactitud no sirve con eventos raros: hay que reportar sensibilidad, valor predictivo y coste de cada tipo de error. Comprobado con 500 000 casos simulados.', note_kind='gold', foot=SINT)


def se279_deriva() -> Fig:
    return heatmap(
        "Alarmas de deriva (PSI > 0,2) según el desplazamiento de la media y el tamaño de la ventana",
        "Mapa de calor con el porcentaje de ventanas en que suena la alarma de deriva según el desplazamiento de la media y el tamaño de la ventana: con ventanas de 100 suena el 4 por ciento sin cambio y el 37 con 0,3 desviaciones; con ventanas de 500 o 5 000 no suena con ese desplazamiento y con 0,5 suena el 92 y el 100 por ciento.",
        ["0,0 (sin cambio)", "0,1", "0,3", "0,5"], ["Ventana de 100", "Ventana de 500", "Ventana de 5 000"],
        [[4, 0, 0], [6, 0, 0], [37, 0, 0], [92, 92, 100]],
        unit="% de ventanas con alarma", row_title="Desplazamiento (σ)", col_title="Ventanas con alarma (PSI > 0,2)",
        scale="coral", vmin=0, vmax=100, decimals=0, suffix=" %", highlight=[(2, 0)], cell_h=42, label_w=150,
        note='Con ventanas pequeñas el índice se infla por azar: a 0,3 desviaciones la alarma de n = 100 suena 37 veces de 100 y la de n ≥ 500 ninguna, porque el valor real del índice (alrededor de 0,09) queda bajo el umbral. El umbral de 0,2 es una convención, no una ley; 200 ventanas por celda.', note_kind='teal', foot=SINT)


# ---------------------------------------------------------------- SE-280
def se280_determinismo() -> Fig:
    return grouped_bars(
        "Posición de un resorte amortiguado a los 10 s según la política de paso de tiempo",
        "Barras horizontales con el error de la posición de un resorte a los 10 segundos frente a la referencia: con paso variable es 14, 9,1 y 3,4 milésimas a 30, 60 y 144 fotogramas por segundo y con paso fijo de 1/60 es 8,1; el paso variable da un resultado distinto en cada ejecución y el fijo siempre el mismo.",
        ["Paso variable, 30 fps medios", "Paso variable, 60 fps medios", "Paso variable, 144 fps medios", "Paso fijo de 1/60 s"],
        [("Error frente a la referencia", [14, 9.1, 3.4, 8.1], "gold")],
        unit="Error de la posición (milésimas, 10⁻³)", horizontal=True, label_w=250,
        note='El paso variable no es necesariamente menos exacto en una corrida: es irrepetible. Con una fluctuación del 25 % en el tiempo de cada fotograma, 20 ejecuciones dieron 20 resultados distintos; con paso fijo, uno. Reproducir un fallo, grabar una repetición o sincronizar una partida exige el paso fijo.', note_kind='gold', foot=SINT)


def se280_tunel() -> Fig:
    return line_chart(
        "Una bala contra una pared de 0,2 unidades de grosor: choques detectados por la prueba discreta y por la barrida",
        "Líneas en escala logarítmica con el porcentaje de choques detectados según la velocidad de la bala: la prueba discreta se queda en torno al 20 por ciento desde 12 unidades por segundo y cae a 0 con 120; la prueba barrida sube a 49,4 con 30 y a 100 con 60 y 120.",
        [("Prueba discreta", [(5, 8.2, "8,2", "t"), (12, 20.5, "20,5", "b"), (30, 19.2, "19,2", "b"), (60, 20.0, "20,0", "b"), (120, 0, "0", "t")], "coral"),
         ("Prueba barrida", [(5, 8.2, "", "t"), (12, 20.5, "", "t"), (30, 49.4, "49,4", "t"), (60, 100, "100", "b"), (120, 100, "100", "b")], "teal")],
        x_label="Velocidad de la bala (u/s)", y_label="Choques detectados (%)", log_x=True,
        x_ticks=[(5, "5"), (12, "12"), (30, "30"), (60, "60"), (120, "120")], y_ticks=[0, 20, 40, 60, 80, 100], point_labels="none",
        vlines=[(12, "paso = grosor")],
        note='Cuando el desplazamiento por fotograma supera el grosor de la pared, la bala aparece a un lado y luego al otro sin estar nunca dentro: el choque desaparece. La prueba barrida revisa el segmento recorrido. Mide cada trayectoria de tres lados: pared, bala y paso del fotograma. 2 000 lanzamientos por celda.', note_kind='coral', foot=SINT)


def se280_espiral() -> Fig:
    return line_chart(
        "Espiral de la muerte: coste de cada actualización fija de 16,7 ms (fotogramas por segundo · peor fotograma en ms)",
        "Líneas con los fotogramas por segundo según el coste de cada actualización fija: sin tope de pasos caen de 59,9 con 4 milisegundos a 1,0 con 17 y 0,5 con 20; con un tope de 5 pasos bajan a 10,9 con 17 milisegundos y a 9,3 con 20, y la línea punteada marca el paso fijo de 16,7.",
        [("Sin tope de pasos", [(4, 59.9, "59,9", "t"), (12, 52.4, "52,4", "b"), (15, 18.7, "18,7", "b"), (17, 1.0, "1,0", "b"), (20, 0.5, "0,5", "t")], "coral"),
         ("Tope de 5 pasos", [(4, 59.9, "", "t"), (12, 52.5, "52,5", "t"), (15, 26.7, "26,7", "t"), (17, 10.9, "10,9", "t"), (20, 9.3, "9,3", "t")], "teal")],
        x_label="Coste de una actualización (ms)", y_label="Fotogramas por segundo", x_ticks=[(4, "4"), (8, "8"), (12, "12"), (16, "16"), (20, "20")],
        y_ticks=[0, 20, 40, 60], point_labels="none", vlines=[(16.7, "paso 16,7 ms")],
        note='Si actualizar cuesta más que el paso, cada fotograma debe recuperar más pasos, tarda más, acumula más tiempo y el sistema colapsa. El tope de pasos evita el bloqueo a cambio de que el juego corra más lento que el reloj (0,90 a 17 ms). Picos del 2 % con coste cuádruple; 60 s simulados.', note_kind='coral', foot=SINT)


FIGURES = {
    "se-277-orden-de-la-suma.svg": se277_orden,
    "se-277-semillas-y-repeticiones.svg": se277_semillas,
    "se-277-horizonte-del-caos.svg": se277_caos,
    "se-278-reintentos-y-duplicados.svg": se278_reintentos,
    "se-278-eventos-tardios.svg": se278_tardios,
    "se-278-asimetria-de-claves.svg": se278_sesgo,
    "se-279-fuga-de-la-etiqueta.svg": se279_fuga,
    "se-279-prevalencia-y-avisos.svg": se279_prevalencia,
    "se-279-alarmas-de-deriva.svg": se279_deriva,
    "se-280-paso-de-tiempo-fijo.svg": se280_determinismo,
    "se-280-atravesar-la-pared.svg": se280_tunel,
    "se-280-espiral-de-la-muerte.svg": se280_espiral,
}
