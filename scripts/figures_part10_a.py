"""Figures for SE-121 to SE-126 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, _wrap, grouped_bars, heatmap, line_chart, percentile_intervals
from figures_part07_a import bars

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2)."


def intervals(title: str, desc: str, items, axis_max: float, unit: str, note: str = "", width: int = 940,
              label_w: float = 270, note_kind: str = "gold", foot: str = SINT) -> Fig:
    """Interval plot: items are (label, low, mid, high, kind, mid_label)."""
    track = width - label_w - 70
    note_lines = len(_wrap(note, 13, width - 40)) if note else 0
    note_h = max(54, note_lines * 13 * 1.28 + 26) if note else 0
    y_end = 16 + len(items) * 54 + 26
    height = int(y_end + (note_h + 12 if note else 0) + (28 if foot else 8))
    f = Fig(width, height, title, desc)
    x0 = 10 + label_w
    y = 16
    for label, lo, mid, hi, kind, mid_label in items:
        f.text(x0 - 10, y + 24, label, 13, "end", 700)
        xl, xm, xh = (x0 + v / axis_max * track for v in (lo, mid, hi))
        f.box(xl, y + 8, max(xh - xl, 4), 24, "", kind, radius=3)
        f.line(xm, y + 2, xm, y + 38, "#142231", width=3)
        f.text(xm, y + 52, mid_label, 12, "middle", 700)
        f.text(xl - 4, y + 25, f"{lo:g}", 12, "end", 400)
        f.text(xh + 4, y + 25, f"{hi:g}", 12, "start", 400)
        y += 54
    f.line(x0, y + 2, x0 + track, y + 2, "#8a9aa3")
    f.text(x0 + track, y + 20, f"0 … {axis_max:g} {unit}", 12, "end", 400)
    y = y_end
    if note:
        f.box(10, y + 4, width - 20, note_h, note, note_kind, 13)
        y += note_h + 12
    if foot:
        f.text(width / 2, y + 14, foot, 12, "middle", 400, "#5c1f14")
    return f


# ---------------------------------------------------------------- SE-121
def se121_frases() -> Fig:
    items = [
        ("«no encuentro dónde entregar»", 188, "teal", "188"),
        ("«se cerró sola»", 65, "coral", "65"),
        ("«perdí mi respuesta»", 64, "coral", "64"),
        ("«no guardó mi avance»", 63, "coral", "63"),
        ("«me enteré tarde» / «no vi la fecha»", 112, "gold", "56 + 56"),
        ("«tuve que volver a entrar» + «me saca»", 108, "coral", "55 + 53"),
    ]
    return bars("600 tickets sintéticos: contar frases frente a contar causas",
                "Barras de 600 tickets: la frase más repetida, no encuentro dónde entregar, suma 188; las cinco frases que describen la expiración de sesión suman 65, 64, 63, 55 y 53 y juntas 300 tickets, la causa más frecuente.",
                items, 3.2, "Por frase gana «no encuentro dónde entregar» (188). Al agrupar las cinco frases de la expiración de sesión (65 + 64 + 63 + 55 + 53) la causa C1 suma 300: más que la causa C2 (188) y C3 (112). Contar palabras reordena la lista.",
                label_w=330, width=1000, note_kind="coral", foot=SINT)


def se121_oportunidad() -> Fig:
    items = [("Punto (12 000 × 8 % × 25 min)", 400, 400, 400, "gold", "400 h/mes"),
             ("Intervalo p5–p95 (20 000 sorteos)", 188, 628, 1679, "teal", "mediana 628 h/mes")]
    return intervals("Dimensionar una oportunidad: un número frente a un rango",
                     "Gráfico de intervalos: la estimación puntual es 400 horas al mes; con rangos triangulares para usuarios, frecuencia y minutos el intervalo del 5 al 95 por ciento va de 188 a 1679 horas, mediana 628, razón 9 a 1.",
                     items, 1800, "horas al mes",
                     note="El mismo modelo da 400 h/mes con valores centrales y entre 188 y 1 679 h/mes al admitir que usuarios (6 000–20 000), frecuencia (2–25 %) y minutos (5–60) son inciertos. La razón p95/p5 es 9: la decisión no debe apoyarse en el punto.", label_w=300)


def se121_linter() -> Fig:
    return heatmap(
        "Linter de enunciados de problema: 8 de 8 en los ejemplos, fallo en el caso nuevo",
        "Mapa de calor binario de seis enunciados: la regla detecta solución embebida, actor y consecuencia y acepta o rechaza; acierta los ocho enunciados con los que se escribió y falla con vendedoras pierden pedidos, que no está en su lista de actores y rechaza por error.",
        ["Dashboard para docentes", "40 min por abrir cada archivo", "Usuarios insatisfechos", "Familias abandonan el registro", "Pierden avance al expirar (nuevo)", "Vendedoras pierden pedidos (nuevo)"],
        ["Solución embebida", "Actor", "Consecuencia", "La regla acepta"],
        [[1, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 0]],
        unit="Presente = 1, ausente = 0", scale="navy", vmin=0, vmax=1, cell_fmt=lambda v: "sí" if v else "no", highlight=[(5, 3)],
        label_w=300,
        note="Las expresiones regulares se escribieron mirando los ocho primeros enunciados, por eso aciertan 8/8. Con un actor que no figuraba en la lista («vendedoras») la regla rechaza un buen enunciado (celda resaltada: debía aceptar). Un linter detecta síntomas de enunciado vago; no demuestra que el problema sea real.",
        note_kind="coral", foot=SINT)

# ---------------------------------------------------------------- SE-122
def se122_promedio() -> Fig:
    items = [("1 dimensión", 22.54, "teal", "22,5 %"), ("2 dimensiones", 4.5, "teal", "4,5 %"), ("3 dimensiones", 0.96, "gold", "0,96 %"),
             ("5 dimensiones", 0.05, "coral", "0,05 % (2 personas de 4 063)"), ("8 dimensiones", 0.0, "coral", "0 de 4 063")]
    return bars("Cuántas personas se parecen al «usuario promedio» al sumar dimensiones",
                "Barras con el porcentaje de 4063 personas sintéticas que quedan dentro de 0,3 desviaciones típicas de la mediana en todas las dimensiones: 22,5 por ciento con una, 4,5 con dos, 0,96 con tres, 0,05 con cinco y ninguna con ocho.",
                items, 20, "Población simulada normal e independiente, tolerancia ±0,3 desviaciones típicas. La fracción teórica es 0,2358^d: 23,6 %, 5,6 %, 1,3 %, 0,07 % y 0,001 %. El promedio de cada dimensión no describe a casi nadie en conjunto.",
                label_w=190, width=960, note_kind="gold", foot=SINT)


def se122_simpson() -> Fig:
    return grouped_bars(
        "Paradoja de Simpson: la mejor opción cambia al separar por contexto",
        "Barras agrupadas con las tasas de tarea completada: en oficina A completa 86,7 por ciento y B 93,1; en móvil con conexión débil A 68,8 y B 73,0; agregando los dos contextos A obtiene 82,6 y B 78,0, y la conclusión se invierte.",
        ["Oficina", "Móvil con conexión débil", "Todos juntos"],
        [("Plan A", [86.7, 68.8, 82.6], "gold"), ("Plan B", [93.1, 73.0, 78.0], "navy")],
        unit="Tareas completadas (%)", decimals=1, plot_h=260,
        note="B es mejor en cada contexto y peor en el total porque cada plan se probó sobre mezclas distintas de contextos (A se usó sobre todo en oficina: 234 de 270; B en móvil: 192 de 263). Cifras recicladas de un ejemplo clásico de la literatura: es un cálculo, no una medición.",
        note_kind="gold", foot=SINT)

def se122_trabajos() -> Fig:
    return line_chart(
        "Agrupar enunciados de trabajo por similitud léxica: el umbral decide cuántos trabajos hay",
        "Línea con el número de grupos en que se reparten nueve enunciados de trabajo según el umbral de similitud Jaccard: cinco grupos con 0,20 y nueve con 0,34 y con 0,50, frente a los cuatro trabajos que lee una persona.",
        [("Grupos que devuelve la máquina", [(0.20, 5, "5 grupos", "r"), (0.34, 9, "9 grupos", "t"), (0.50, 9, "9 grupos", "t")], "coral")],
        x_label="Umbral Jaccard", y_label="Grupos de trabajo",
        x_ticks=[(0.20, "0,20"), (0.34, "0,34"), (0.50, "0,50")], y_ticks=[0, 2, 4, 6, 8, 10],
        hlines=[(4, "cuatro trabajos según la lectura humana")], decimals=0, plot_h=260,
        note="Con 0,20 los tamaños son 4 + 2 + 1 + 1 + 1 (agrupa «enviar/subir/entregar la tarea» y separa «saber si llegó»); con 0,34 y 0,50 son nueve grupos de uno: la similitud léxica no ve que «entregar» y «enviar» son lo mismo. Agrupar trabajos es una decisión de investigación, no un cálculo.",
        note_kind="coral", foot=SINT)

# ---------------------------------------------------------------- SE-123
def se123_saturacion() -> Fig:
    return line_chart(
        "Probabilidad de oír un tema al menos una vez según cuántas entrevistas se hagan",
        "Líneas con la probabilidad simulada de observar un tema de prevalencia 5, 10 o 30 por ciento en 5, 8, 20 y 30 entrevistas: con 30 entrevistas 78,9, 96,1 y 100 por ciento; para un 90 por ciento de seguridad hacen falta 45, 22 y 7 entrevistas.",
        [("Tema de 5 %", [(5, 23.0), (8, 34.2), (20, 64.3), (30, 78.9, "78,9", "t")], "coral"),
         ("Tema de 10 %", [(5, 41.4), (8, 57.2), (20, 88.1), (30, 96.1, "96,1", "b")], "gold"),
         ("Tema de 30 %", [(5, 83.1), (8, 94.3), (20, 100.0), (30, 100.0, "100", "t")], "teal")],
        x_label="Entrevistas realizadas", y_label="Probabilidad de oír el tema (%)",
        x_ticks=[(5, "5"), (8, "8"), (20, "20"), (30, "30")], y_ticks=[0, 20, 40, 60, 80, 100],
        hlines=[(90, "90 %")], point_labels="none", decimals=1, plot_h=300,
        note="Cinco entrevistas casi garantizan ver un tema que afecta al 30 % y dejan un 59 % de probabilidad de no ver uno que afecta al 10 %. «No salió en las entrevistas» no es lo mismo que «no existe». Entrevistas necesarias para un 90 %: 45, 22 y 7. Simulación de 20 000 repeticiones; coincide con 1 − (1 − p)ⁿ.",
        note_kind="gold", foot=SINT)

def se123_kappa() -> Fig:
    items = [("Tema frecuente (50 %)", 93.5, "teal", "acuerdo 93,5 % · κ 0,87"),
             ("Tema ocasional (10 %)", 91.2, "gold", "acuerdo 91,2 % · κ 0,60"),
             ("Tema raro (3 %)", 90.2, "coral", "acuerdo 90,2 % · κ 0,29")]
    return bars("Dos codificadoras con 5 % de error: el acuerdo bruto casi no cambia, kappa se desploma",
                "Barras con el acuerdo bruto entre dos codificadoras simuladas: 93,5 por ciento con un tema del 50 por ciento (kappa 0,87), 91,2 con uno del 10 (kappa 0,60) y 90,2 con uno del 3 (kappa 0,29).",
                items, 4.8, "400 fragmentos sintéticos, cada codificadora se equivoca el 5 % de las veces. El acuerdo bruto parece sano en los tres casos; kappa descuenta el acuerdo por azar y cae a 0,29 cuando el código es raro.",
                label_w=260, width=1000, note_kind="gold", foot=SINT)


def se123_trazabilidad() -> Fig:
    return grouped_bars(
        "Verificar que cada afirmación del informe tenga citas reales y de personas distintas",
        "Barras agrupadas con cuatro afirmaciones: A1 tiene dos citas declaradas, dos halladas y dos participantes distintos; A2 una, una y uno; A3 y A4 declaran dos citas y solo se hallan una, de un solo participante; se exigen dos participantes distintos.",
        ["A1 Guardado automático", "A2 Plazos por correo", "A3 Plazos por compañeros", "A4 Perdieron trabajo"],
        [("Citas declaradas", [2, 1, 2, 2], "grey"), ("Citas halladas en la transcripción", [2, 1, 1, 1], "teal"), ("Participantes distintos", [2, 1, 1, 1], "navy")],
        unit="Cantidad", decimals=0, ticks=[0, 1, 2], ref_lines=[(2, "mínimo exigido: 2 participantes")], plot_h=260,
        note="Veredictos: A1 sostenida; A2 débil (un solo participante); A3 débil (la cita de P5 no existe en las transcripciones); A4 débil (la cita de P3 no coincide). El script comprueba que cada cita aparezca literalmente y que haya dos participantes distintos; no comprueba que la cita signifique lo que la afirmación dice: eso exige leer.",
        note_kind="teal", foot=SINT)

# ---------------------------------------------------------------- SE-124
def se124_tornado() -> Fig:
    items = [("Interés (5 %–30 %)", 0.607, "coral", "0,61 pp · razón 6,0"),
             ("Activación (10 %–50 %)", 0.567, "coral", "0,57 pp · razón 5,0"),
             ("Retención (20 %–70 %)", 0.472, "gold", "0,47 pp · razón 3,5"),
             ("Registro (20 %–60 %)", 0.425, "gold", "0,43 pp · razón 3,0"),
             ("Alcance (30 %–60 %)", 0.283, "teal", "0,28 pp · razón 2,0")]
    return bars("Cuánto mueve cada supuesto el resultado de un embudo de cinco pasos",
                "Barras ordenadas del cambio en puntos porcentuales del resultado final al mover un supuesto de su mínimo a su máximo: interés 0,61, activación 0,57, retención 0,47, registro 0,43 y alcance 0,28; el resultado base es 0,425 por ciento.",
                items, 650, "Resultado base 0,425 %. Con todos los supuestos sorteados a la vez, el intervalo p5–p95 va de 0,075 % a 1,117 % (razón 15). El supuesto que más mueve el resultado es el que primero hay que contrastar, no el que más cómodo resulta medir.",
                label_w=250, width=1000, note_kind="gold", foot=SINT)


def se124_posterior() -> Fig:
    return line_chart(
        "La misma tasa observada del 20 %: cuánta confianza da de superar el umbral del 15 %",
        "Línea con la probabilidad posterior (a priori Beta(1,1)) de que la tasa real supere el 15 por ciento cuando se observa un 20 por ciento: 0,80 con 20 personas, 0,85 con 40, 0,93 con 100 y 0,98 con 200; solo desde 100 personas pasa del 0,90 exigido.",
        [("P(tasa real > 15 %)", [(20, 0.80, "4 de 20", "t"), (40, 0.85, "8 de 40", "t"), (100, 0.93, "20 de 100", "t"), (200, 0.98, "40 de 200", "b")], "teal")],
        x_label="Personas observadas (misma tasa del 20 %)", y_label="Probabilidad posterior",
        x_ticks=[(20, "20"), (40, "40"), (100, "100"), (200, "200")], y_ticks=[0.6, 0.7, 0.8, 0.9, 1.0],
        hlines=[(0.90, "probabilidad exigida 0,90")], log_x=True, y_zero=False, decimals=2, plot_h=280,
        note="El eje vertical empieza en 0,6 para ver la separación. Una hipótesis que dice «más del 15 %» no se confirma con 4 de 20, aunque 20 % parezca mayor que 15 %. Fijar antes el umbral y la probabilidad exigida (por ejemplo 0,90) obliga a definir cuántas personas se necesitan.",
        note_kind="gold", foot=SINT)

def se124_multiples() -> Fig:
    items = [("1 hipótesis", 5.0, "teal", "5,0 %"), ("5 hipótesis", 22.6, "gold", "22,6 %"), ("10 hipótesis", 40.1, "gold", "40,1 %"),
             ("20 hipótesis", 64.2, "coral", "64,2 % (simulado 64,0 %)"), ("20 con Bonferroni", 4.8, "teal", "4,8 % (simulado)")]
    return bars("Probabilidad de al menos un falso positivo cuando todas las hipótesis son falsas",
                "Barras con la probabilidad de encontrar al menos un resultado significativo al 5 por ciento si se contrastan 1, 5, 10 o 20 hipótesis nulas: 5,0, 22,6, 40,1 y 64,2 por ciento; con corrección de Bonferroni sobre 20, 4,8 por ciento.",
                items, 6.5, "20 000 repeticiones. Revisar veinte métricas «a ver cuál sale» produce un hallazgo falso dos de cada tres veces. La corrección de Bonferroni lo devuelve al 5 %, a costa de exigir evidencia más fuerte por hipótesis.",
                label_w=230, width=1000, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-125
def se125_estabilidad() -> Fig:
    items = [("n = 10 personas", 51.2, "coral", "51,2 %"), ("n = 30", 75.8, "gold", "75,8 %"), ("n = 100", 96.2, "teal", "96,2 %"), ("n = 300", 100.0, "teal", "100 %")]
    return bars("Con qué frecuencia una encuesta recupera los tres resultados más desatendidos",
                "Barras con el porcentaje de 400 encuestas simuladas que identifican correctamente los tres principales resultados deseados: 51,2 por ciento con 10 personas, 75,8 con 30, 96,2 con 100 y 100 con 300.",
                items, 6.0, "Ocho resultados con importancia y satisfacción verdaderas conocidas; escalas 1–5 con desviación 1. Con 10 personas el top-3 correcto sale la mitad de las veces; el tau de Kendall sube de 0,72 a 0,92 al pasar de 10 a 300. Un ranking de resultados es una estimación, no un hecho.",
                label_w=200, width=960, note_kind="gold", foot=SINT)


def se125_deteccion() -> Fig:
    items = [("Rápido: activación 40→45 % (80/sem.)", 7.5, "teal", "7,5 semanas"),
             ("Lento: retención a 90 d, 12→17 % (20/sem.)", 12.9, "coral", "12,9 semanas")]
    return bars("Semanas para detectar la misma mejora de 5 puntos según el indicador elegido",
                "Barras con el promedio de semanas hasta detectar un cambio de cinco puntos con prueba unilateral al 5 por ciento: 7,5 semanas con el indicador rápido de activación y 12,9 con el indicador lento de retención.",
                items, 40, "Promedio de 600 simulaciones, tope de 60 semanas. Además la retención a 90 días solo puede medirse 13 semanas después de empezar a observar la cohorte: el calendario real se alarga. Los indicadores adelantados responden antes pero pueden desviarse del resultado que importa.",
                label_w=330, width=1000, note_kind="gold", foot=SINT)


def se125_adopcion() -> Fig:
    items = [("Valor nuevo = 1,0× el actual", 6.3, "coral", "6,3 %"), ("1,5×", 16.2, "coral", "16,2 %"), ("2,0×", 28.5, "gold", "28,5 %"),
             ("3,0×", 50.2, "gold", "50,2 %"), ("5,0×", 76.4, "teal", "76,4 %"), ("9,0×", 94.0, "teal", "94,0 %")]
    return bars("Adopción simulada si cada persona sobrevalora lo que ya usa por un factor de 3",
                "Barras con el porcentaje de adopción simulado según el múltiplo de valor de la propuesta frente a la alternativa actual: 6,3 por ciento con 1 vez, 16,2 con 1,5, 28,5 con 2, 50,2 con 3, 76,4 con 5 y 94,0 con 9.",
                items, 5.5, "Modelo, no medición: valores percibidos lognormales independientes y un sesgo de apego de 3× a lo actual. Ser «el doble de bueno» alcanza a menos del 30 % de la población; el modelo está inspirado en el argumento de Gourville y no prueba cuánto pesa el apego en un producto concreto.",
                label_w=290, width=1000, note_kind="gold", foot="Simulación con semilla fija; los parámetros son supuestos, no datos de mercado.")


# ---------------------------------------------------------------- SE-126
def se126_estabilidad() -> Fig:
    return grouped_bars(
        "Estabilidad de k-means entre dos semillas: datos con tres grupos reales frente a ruido uniforme",
        "Barras agrupadas del índice de Rand entre dos ejecuciones con semillas distintas: con k igual a 3 los datos estructurados dan 0,964 y el ruido 0,806, pero con k igual a 4, 5 y 6 el ruido es tan estable como los datos con estructura, e incluso más con k igual a 4.",
        ["k = 2", "k = 3", "k = 4", "k = 5", "k = 6"],
        [("Datos con 3 grupos reales", [0.706, 0.964, 0.942, 0.897, 0.889], "teal"), ("Ruido uniforme", [0.663, 0.806, 0.967, 0.902, 0.879], "coral")],
        unit="Índice de Rand entre semillas", decimals=3, plot_h=280,
        note="Solo con k = 3 los datos estructurados son claramente más estables que el ruido; con k = 4 el ruido es más estable (0,967 frente a 0,942). Que un algoritmo devuelva segmentos estables no prueba que existan segmentos. La estabilidad es necesaria, no suficiente.",
        note_kind="coral", foot=SINT)

def se126_mercado() -> Fig:
    return percentile_intervals(
        "Dos estimaciones del mercado con rangos triangulares y 20 000 sorteos",
        "Intervalos en escala logarítmica con los percentiles 5, 50 y 95: arriba-abajo da 6223, 18399 y 45102 personas y abajo-arriba 11354, 50773 y 189593 dólares al año, con razones p95 sobre p5 de 7,2 y 16,7.",
        [("Arriba-abajo (personas)", [6223, 18399, 45102]), ("Abajo-arriba (USD/año)", [11354, 50773, 189593])],
        unit="Personas o USD por año (según la fila)", marks=("p5", "p50", "p95"), log=True, decimals=0,
        note="Las unidades de las filas son distintas (personas, dinero) y no deben compararse entre sí. Lo comparable es la anchura: p95/p5 vale 7,2 arriba-abajo y 16,7 abajo-arriba, porque este método multiplica tres incertidumbres. El «1 % de un mercado grande» oculta justo esa anchura.",
        note_kind="gold", foot="Rangos asumidos por el autor para ilustrar el método; no provienen de ningún mercado real.")

def se126_cobertura() -> Fig:
    return grouped_bars(
        "Qué trabajos cubre cada alternativa existente (incluida no hacer nada)",
        "Barras horizontales con los trabajos que cubre cada alternativa de siete: la plataforma actual y el editor local cubren tres cada una, correo, hoja de cálculo y mensajería dos, y no hacer nada ninguno; el mínimo conjunto que cubre todo es correo, hoja de cálculo y editor local.",
        ["Plataforma actual (J1, J4, J5)", "Editor local (J2, J6, J7)", "Correo (J1, J5)", "Hoja de cálculo (J3, J4)", "Mensajería (J1, J3)", "No hacer nada"],
        [("Trabajos cubiertos", [3, 3, 2, 2, 2, 0], "teal")],
        unit="Trabajos cubiertos de 7", horizontal=True, decimals=0, ref_lines=[(7, "7 trabajos")], label_w=250,
        note="Ninguna alternativa cubre todo; el mínimo conjunto que lo hace es correo + hoja de cálculo + editor local: la persona usuaria ya cose tres herramientas. Esa costura, y no una lista de funciones, es el espacio donde una propuesta puede competir.",
        note_kind="teal", foot=SINT)

FIGURES = {
    "se-121-frases-frente-a-causas.svg": se121_frases,
    "se-121-oportunidad-un-numero-o-un-rango.svg": se121_oportunidad,
    "se-121-linter-de-enunciados.svg": se121_linter,
    "se-122-el-usuario-promedio.svg": se122_promedio,
    "se-122-paradoja-de-simpson-por-contexto.svg": se122_simpson,
    "se-122-agrupar-trabajos-segun-umbral.svg": se122_trabajos,
    "se-123-cuantas-entrevistas-para-ver-un-tema.svg": se123_saturacion,
    "se-123-acuerdo-bruto-frente-a-kappa.svg": se123_kappa,
    "se-123-trazabilidad-cita-afirmacion.svg": se123_trazabilidad,
    "se-124-sensibilidad-de-supuestos.svg": se124_tornado,
    "se-124-posterior-frente-a-umbral.svg": se124_posterior,
    "se-124-hipotesis-multiples.svg": se124_multiples,
    "se-125-estabilidad-del-ranking.svg": se125_estabilidad,
    "se-125-semanas-para-detectar.svg": se125_deteccion,
    "se-125-adopcion-segun-multiplo-de-valor.svg": se125_adopcion,
    "se-126-estabilidad-de-segmentos.svg": se126_estabilidad,
    "se-126-dos-estimaciones-de-mercado.svg": se126_mercado,
    "se-126-cobertura-de-alternativas.svg": se126_cobertura,
}
