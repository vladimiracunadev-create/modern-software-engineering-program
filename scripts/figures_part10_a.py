"""Figures for SE-121 to SE-126 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, _wrap
from figures_part07_a import bars, tab

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
    rows = [["Necesitamos un dashboard para los docentes.", "sí", "sí", "no", "Rechaza ✔"],
            ["Los docentes tardan 40 minutos en corregir porque abren cada archivo por separado.", "no", "sí", "sí", "Acepta ✔"],
            ["Los usuarios están insatisfechos.", "no", "no", "no", "Rechaza ✔"],
            ["Las familias abandonan el registro en la verificación y no logran compartir fotos.", "no", "sí", "sí", "Acepta ✔"],
            ["Los estudiantes pierden su avance si la sesión expira, sin poder recuperarlo. (caso nuevo)", "no", "sí", "sí", "Acepta ✔"],
            ["Las vendedoras pierden pedidos cuando el teléfono se queda sin red. (caso nuevo)", "no", "no", "sí", "Rechaza ✘ (falso negativo)"]]
    return tab("Linter de enunciados de problema: 8 de 8 en los ejemplos, fallo en el caso nuevo",
               "Tabla con seis enunciados: la regla detecta solución embebida, actor y consecuencia; acierta los ocho enunciados con los que se escribió y falla con vendedoras pierden pedidos, que no está en su lista de actores.",
               ["Enunciado", "Solución embebida", "Actor", "Consecuencia", "Resultado"], rows, [440, 120, 80, 110, 190], row_h=62, size=12,
               note="Las expresiones regulares se escribieron mirando los ocho primeros enunciados, por eso aciertan 8/8. Con un actor que no figuraba en la lista («vendedoras») la regla rechaza un buen enunciado. Un linter detecta síntomas de enunciado vago; no demuestra que el problema sea real.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-122
def se122_promedio() -> Fig:
    items = [("1 dimensión", 22.54, "teal", "22,5 %"), ("2 dimensiones", 4.5, "teal", "4,5 %"), ("3 dimensiones", 0.96, "gold", "0,96 %"),
             ("5 dimensiones", 0.05, "coral", "0,05 % (2 personas de 4 063)"), ("8 dimensiones", 0.0, "coral", "0 de 4 063")]
    return bars("Cuántas personas se parecen al «usuario promedio» al sumar dimensiones",
                "Barras con el porcentaje de 4063 personas sintéticas que quedan dentro de 0,3 desviaciones típicas de la mediana en todas las dimensiones: 22,5 por ciento con una, 4,5 con dos, 0,96 con tres, 0,05 con cinco y ninguna con ocho.",
                items, 20, "Población simulada normal e independiente, tolerancia ±0,3 desviaciones típicas. La fracción teórica es 0,2358^d: 23,6 %, 5,6 %, 1,3 %, 0,07 % y 0,001 %. El promedio de cada dimensión no describe a casi nadie en conjunto.",
                label_w=190, width=960, note_kind="gold", foot=SINT)


def se122_simpson() -> Fig:
    rows = [["Oficina", "234 de 270 = 86,7 %", "81 de 87 = 93,1 %", "B gana"],
            ["Móvil con conexión débil", "55 de 80 = 68,8 %", "192 de 263 = 73,0 %", "B gana"],
            ["Todos juntos", "289 de 350 = 82,6 %", "273 de 350 = 78,0 %", "A gana"]]
    return tab("Paradoja de Simpson: la mejor opción cambia al separar por contexto",
               "Tabla de tasas de tarea completada: en oficina A completa 86,7 por ciento y B 93,1; en móvil con conexión débil A 68,8 y B 73,0; agregando los dos contextos A obtiene 82,6 y B 78,0, y la conclusión se invierte.",
               ["Contexto", "Plan A", "Plan B", "Mejor"], rows, [250, 260, 260, 130], row_h=54, size=13,
               note="B es mejor en cada contexto y peor en el total porque cada plan se probó sobre mezclas distintas de contextos (A se usó sobre todo en oficina, B en móvil). Cifras recicladas de un ejemplo clásico de la literatura: es un cálculo, no una medición.", note_kind="gold", foot=SINT)


def se122_trabajos() -> Fig:
    rows = [["0,20", "5 grupos", "4 + 2 + 1 + 1 + 1", "Agrupa «enviar/subir/entregar la tarea»; separa «saber si llegó»"],
            ["0,34", "9 grupos", "9 × 1", "Ningún par supera el umbral: nueve «trabajos»"],
            ["0,50", "9 grupos", "9 × 1", "Igual: la similitud léxica no ve que «entregar» y «enviar» son lo mismo"]]
    return tab("Agrupar enunciados de trabajo por similitud léxica: el umbral decide cuántos trabajos hay",
               "Tabla con nueve enunciados de trabajo agrupados por solapamiento de palabras: con umbral Jaccard 0,20 salen cinco grupos y con 0,34 o 0,50 nueve grupos, de modo que el número de trabajos depende del umbral y no de las personas.",
               ["Umbral Jaccard", "Resultado", "Tamaños", "Lectura"], rows, [150, 130, 190, 450], row_h=62, size=12,
               note="Los nueve enunciados describen cuatro trabajos para una persona que los lee. La máquina entrega entre 5 y 9 según un parámetro arbitrario: agrupar trabajos es una decisión de investigación, no un cálculo.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-123
def se123_saturacion() -> Fig:
    rows = [["5 %", "23,0 %", "34,2 %", "64,3 %", "78,9 %", "45"],
            ["10 %", "41,4 %", "57,2 %", "88,1 %", "96,1 %", "22"],
            ["30 %", "83,1 %", "94,3 %", "100 %", "100 %", "7"]]
    return tab("Probabilidad de oír un tema al menos una vez según cuántas entrevistas se hagan",
               "Tabla con la probabilidad simulada de observar un tema con prevalencia 5, 10 o 30 por ciento en 5, 8, 20 y 30 entrevistas; para un 90 por ciento de seguridad hacen falta 45, 22 y 7 entrevistas.",
               ["Prevalencia del tema", "5 entrevistas", "8", "20", "30", "n para 90 %"], rows, [190, 150, 130, 130, 130, 160], row_h=48, size=13,
               note="Cinco entrevistas casi garantizan ver un tema que afecta al 30 % y dejan un 59 % de probabilidad de no ver uno que afecta al 10 %. «No salió en las entrevistas» no es lo mismo que «no existe». Simulación de 20 000 repeticiones; coincide con 1 − (1 − p)ⁿ.", note_kind="gold", foot=SINT)


def se123_kappa() -> Fig:
    items = [("Tema frecuente (50 %)", 93.5, "teal", "acuerdo 93,5 % · κ 0,87"),
             ("Tema ocasional (10 %)", 91.2, "gold", "acuerdo 91,2 % · κ 0,60"),
             ("Tema raro (3 %)", 90.2, "coral", "acuerdo 90,2 % · κ 0,29")]
    return bars("Dos codificadoras con 5 % de error: el acuerdo bruto casi no cambia, kappa se desploma",
                "Barras con el acuerdo bruto entre dos codificadoras simuladas: 93,5 por ciento con un tema del 50 por ciento (kappa 0,87), 91,2 con uno del 10 (kappa 0,60) y 90,2 con uno del 3 (kappa 0,29).",
                items, 4.8, "400 fragmentos sintéticos, cada codificadora se equivoca el 5 % de las veces. El acuerdo bruto parece sano en los tres casos; kappa descuenta el acuerdo por azar y cae a 0,29 cuando el código es raro.",
                label_w=260, width=1000, note_kind="gold", foot=SINT)


def se123_trazabilidad() -> Fig:
    rows = [["A1 «No confían en el guardado automático»", "2 de 2", "2 (P1, P3)", "Sostenida"],
            ["A2 «Los plazos se conocen por el correo»", "1 de 1", "1 (P2)", "Débil: un solo participante"],
            ["A3 «Los plazos llegan por compañeros»", "1 de 2", "1 (P4)", "Débil: la cita de P5 no existe"],
            ["A4 «Perdieron trabajo»", "1 de 2", "1 (P1)", "Débil: la cita de P3 no coincide"]]
    return tab("Verificar que cada afirmación del informe tenga citas reales y de personas distintas",
               "Tabla con cuatro afirmaciones: A1 tiene dos citas verificadas de dos participantes; A2 depende de un participante; A3 cita a un participante que no existe en las transcripciones y A4 una frase que no aparece literalmente.",
               ["Afirmación", "Citas halladas", "Participantes distintos", "Veredicto"], rows, [340, 130, 190, 270], row_h=54, size=12,
               note="El script comprueba que cada cita aparezca literalmente en la transcripción y exige dos participantes distintos. No comprueba que la cita signifique lo que la afirmación dice: eso exige leer.", note_kind="teal", foot=SINT)


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
    rows = [["4 de 20", "20 %", "0,80"], ["8 de 40", "20 %", "0,85"], ["20 de 100", "20 %", "0,93"], ["40 de 200", "20 %", "0,98"]]
    return tab("La misma tasa observada del 20 %: cuánta confianza da de superar el umbral del 15 %",
               "Tabla con la probabilidad posterior (a priori Beta(1,1)) de que la tasa real supere el 15 por ciento cuando se observa un 20 por ciento: 0,80 con 20 personas, 0,85 con 40, 0,93 con 100 y 0,98 con 200.",
               ["Observado", "Tasa", "P(tasa real > 15 %)"], rows, [260, 200, 360], row_h=44, size=13,
               note="Una hipótesis que dice «más del 15 %» no se confirma con 4 de 20, aunque 20 % parezca mayor que 15 %. Fijar antes el umbral y la probabilidad exigida (por ejemplo 0,90) obliga a definir cuántas personas se necesitan.", note_kind="gold", foot=SINT)


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
    rows = [["2", "0,706", "0,663", "Parecen igual de estables"], ["3", "0,964", "0,806", "Aquí sí distingue estructura de ruido"],
            ["4", "0,942", "0,967", "El ruido es MÁS estable"], ["5", "0,897", "0,902", "Sin diferencia"], ["6", "0,889", "0,879", "Sin diferencia"]]
    return tab("Estabilidad de k-means entre dos semillas: datos con tres grupos reales frente a ruido uniforme",
               "Tabla del índice de Rand entre dos ejecuciones con semillas distintas: con k igual a 3 los datos estructurados dan 0,964 y el ruido 0,806, pero con k igual a 4, 5 y 6 el ruido es tan estable como los datos con estructura.",
               ["k (segmentos)", "Datos con 3 grupos reales", "Ruido uniforme", "Lectura"], rows, [150, 230, 190, 340], row_h=44, size=13,
               note="Que un algoritmo devuelva segmentos estables no prueba que existan segmentos. La estabilidad es necesaria, no suficiente: los segmentos deben además distinguirse por comportamiento o necesidad y poder ser identificados por el equipo.", note_kind="coral", foot=SINT)


def se126_mercado() -> Fig:
    rows = [["Arriba-abajo: mercado × cuota", "6 223 personas", "18 399", "45 102", "7,2"],
            ["Abajo-arriba: contactables × conversión × precio", "11 354 USD/año", "50 773", "189 593", "16,7"]]
    return tab("Dos estimaciones del mercado con rangos triangulares y 20 000 sorteos",
               "Tabla con percentiles 5, 50 y 95 de dos estimaciones: arriba-abajo da entre 6223 y 45102 personas y abajo-arriba entre 11354 y 189593 dólares al año, con razones p95 sobre p5 de 7,2 y 16,7.",
               ["Método", "p5", "p50", "p95", "p95 / p5"], rows, [360, 160, 120, 120, 120], row_h=64, size=12,
               note="Las unidades son distintas (personas, dinero) y no deben compararse entre filas. Lo comparable es la anchura: el método abajo-arriba multiplica tres incertidumbres y su rango es más ancho. El «1 % de un mercado grande» oculta justo esa anchura.", note_kind="gold", foot="Rangos asumidos por el autor para ilustrar el método; no provienen de ningún mercado real.")


def se126_cobertura() -> Fig:
    rows = [["Plataforma actual", "J1, J4, J5", "3 de 7"], ["Editor local", "J2, J6, J7", "3 de 7"], ["Correo", "J1, J5", "2 de 7"],
            ["Hoja de cálculo", "J3, J4", "2 de 7"], ["Mensajería", "J1, J3", "2 de 7"], ["No hacer nada", "—", "0 de 7"]]
    return tab("Qué trabajos cubre cada alternativa existente (incluida no hacer nada)",
               "Tabla de cobertura de siete trabajos por seis alternativas: la plataforma actual y el editor local cubren tres cada una, correo, hoja de cálculo y mensajería dos, y no hacer nada ninguno; el mínimo conjunto que cubre todo es correo, hoja de cálculo y editor local.",
               ["Alternativa", "Trabajos que cubre", "Cobertura"], rows, [300, 280, 200], row_h=40, size=13,
               note="Ninguna alternativa cubre todo; el mínimo conjunto que lo hace es correo + hoja de cálculo + editor local: la persona usuaria ya cose tres herramientas. Esa costura, y no una lista de funciones, es el espacio donde una propuesta puede competir.", note_kind="teal", foot=SINT)


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
