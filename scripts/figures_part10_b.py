"""Figures for SE-127 to SE-132 (synthetic data, fixed seeds; timings from CPython 3.12.9 on Windows 11 and 3.12.3 on Ubuntu/WSL2)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, stacked_bars
from figures_part07_a import bars
from figures_part10_a import SINT, intervals

MEDIDO = "Tiempos medidos con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu (WSL2); dependen del equipo y se leen como razones."


# ---------------------------------------------------------------- SE-127
def se127_muestra() -> Fig:
    return grouped_bars(
        "Personas por brazo para detectar una diferencia con 80 % de potencia y 5 % de error",
        "Barras horizontales con las personas por brazo necesarias: pasar de 10 a 12 por ciento exige 3841, de 10 a 15 exige 686, de 10 a 20 exige 199 y de 40 a 45 exige 1534; con 500 personas la potencia simulada del primer caso es solo 17,3 por ciento.",
        ["10 % → 12 %", "10 % → 15 %", "10 % → 20 %", "40 % → 45 %"],
        [("Personas por brazo", [3841, 686, 199, 1534], "navy")],
        unit="Personas por brazo", horizontal=True, decimals=0, label_w=160,
        note="Potencia simulada del primer caso (4 000 repeticiones): 81,2 % con n = 3 841, 17,3 % con 500 y 9,4 % con 200. Con 500 personas por brazo un experimento que busca pasar del 10 % al 12 % detecta el efecto una de cada seis veces: no sirve para decidir aunque se ejecute bien. Un prototipo con 30 personas solo puede ver efectos enormes.",
        note_kind="coral", foot=SINT)

def se127_miradas() -> Fig:
    items = [("1 mirada (al final)", 4.7, "teal", "4,7 %"), ("2 miradas", 8.0, "gold", "8,0 %"), ("5 miradas", 13.0, "gold", "13,0 %"),
             ("10 miradas", 21.1, "coral", "21,1 %"), ("20 miradas", 25.4, "coral", "25,4 %")]
    return bars("Falsos positivos en pruebas A/A cuando se detiene al primer resultado «significativo»",
                "Barras con el porcentaje de pruebas A/A, sin diferencia real, que declaran un efecto significativo al 5 por ciento si se mira varias veces: 4,7 por ciento con una mirada, 8,0 con dos, 13,0 con cinco, 21,1 con diez y 25,4 con veinte.",
                items, 25, "2 000 pruebas por fila, 2 000 personas por brazo repartidas entre las miradas, ambas ramas con la misma conversión del 10 %. Detener cuando «sale significativo» infla el error hasta una de cada cuatro pruebas; la solución es fijar antes el tamaño o usar métodos secuenciales.",
                label_w=240, width=1000, note_kind="coral", foot=SINT)


def se127_wilson() -> Fig:
    items = [("n = 20 (2 éxitos)", 2.8, 10.0, 30.1, "coral", "10,0 %"), ("n = 50 (4)", 3.2, 8.0, 18.8, "gold", "8,0 %"),
             ("n = 200 (16)", 5.0, 8.0, 12.6, "teal", "8,0 %"), ("n = 1 000 (80)", 6.5, 8.0, 9.8, "teal", "8,0 %")]
    return intervals("Intervalo de Wilson al 95 % para una puerta falsa con 8 % de clics",
                     "Gráfico de intervalos: con 20 personas el 10 por ciento observado admite entre 2,8 y 30,1 por ciento; con 50 entre 3,2 y 18,8; con 200 entre 5,0 y 12,6 y con 1000 entre 6,5 y 9,8.",
                     items, 32, "% de clics",
                     note="Con 20 personas un 10 % observado es compatible con casi cualquier valor entre 3 % y 30 %: sirve para descubrir problemas, no para estimar demanda. El ancho se reduce con la raíz de n, no con n.", label_w=240)


# ---------------------------------------------------------------- SE-128
def se128_rice() -> Fig:
    return grouped_bars(
        "RICE de doce ítems con ±40 % de incertidumbre en alcance, impacto y confianza (+60 % en esfuerzo)",
        "Barras horizontales de seis ítems de doce: aviso de sesión con RICE 7200 es primero en 58 por ciento de 5000 simulaciones y está en el top tres en 98,9; botón de entrega visible es primero en 37,8; recuperar borradores entra al top tres en 75,6 por ciento.",
        ["Aviso de sesión (RICE 7 200)", "Botón de entrega visible (6 000)", "Recuperar borradores (3 200)", "Recordatorios por correo (2 000)", "Integración con calendario (800)", "Rediseño de navegación (750)"],
        [("En el top 3", [98.9, 97.2, 75.6, 27.1, 0.6, 0.4], "teal"), ("Primero", [58.0, 37.8, 3.9, 0.3, 0.0, 0.0], "navy")],
        unit="Simulaciones (%)", horizontal=True, decimals=1, label_w=270,
        note="El orden base se sostiene para los tres primeros, pero el «primero» cambia en cuatro de cada diez simulaciones. RICE con todas las entradas estimadas oculta ese margen. Concordancia con valor/esfuerzo sin confianza: tau 0,80; con alcance solo: 0,53.",
        note_kind="gold", foot=SINT)

def se128_retraso() -> Fig:
    return grouped_bars(
        "Coste total del retraso de cuatro trabajos según el criterio de orden",
        "Barras horizontales con el coste de retraso acumulado de cuatro trabajos: el orden WSJF D, C, A, B cuesta 119 y es el óptimo de las 24 permutaciones; más corto primero cuesta 122, mayor valor primero 126 y el peor orden 238.",
        ["WSJF (D, C, A, B)", "Más corto primero (C, D, A, B)", "Mayor valor primero (D, A, C, B)", "Peor de las 24 (B, A, C, D)"],
        [("Coste total de retraso", [119, 122, 126, 238], "navy")],
        unit="Coste total de retraso", horizontal=True, decimals=0, label_w=250,
        note="Trabajos (coste de retraso por semana, duración): A (8, 3), B (3, 4), C (5, 1), D (13, 2). Priorizar por valor solo, sin mirar duración, cuesta 6 % más que el óptimo; el peor orden cuesta el doble. Con duraciones inciertas el óptimo también lo es.",
        note_kind="gold", foot="Cálculo exacto sobre las 24 permutaciones; no depende del equipo.")

def se128_informacion() -> Fig:
    return line_chart(
        "Valor neto de aprender antes de construir (construir ahora vale −5; no hacer nada vale 0)",
        "Línea con el valor esperado neto de hacer una prueba antes de construir según su coste: con coste 5 y precisión 0,90 vale 11,3; con 10 y 0,80 vale 1,6; con 15 y 0,70 es negativo, −8,1, y con 25 y 0,90 también, −8,7; las líneas marcan construir sin aprender y no hacer nada.",
        [("Valor esperado neto de la prueba", [(5, 11.3, "precisión 0,90", "t"), (10, 1.6, "0,80", "t"), (15, -8.1, "0,70", "t"), (25, -8.7, "0,90", "t")], "teal")],
        x_label="Coste de la prueba", y_label="Valor esperado neto",
        x_ticks=[(5, "5"), (10, "10"), (15, "15"), (25, "25")], y_ticks=[-10, -5, 0, 5, 10, 15],
        hlines=[(0, "no hacer nada: 0"), (-5, "construir sin aprender: −5")], decimals=1, plot_h=300,
        note="Parámetros: probabilidad de éxito 35 %, ganancia 100, coste de construir 40. Una prueba barata y fiable convierte una apuesta negativa en positiva; una prueba cara o poco fiable destruye el valor. Con coste 15 y precisión 0,70 la prueba ya es peor que construir sin aprender. Aprender también cuesta.",
        note_kind="teal", foot="Cálculo exacto; los números son un modelo ilustrativo.")

# ---------------------------------------------------------------- SE-129
def se129_unicidad() -> Fig:
    items = [("Región", 0.0, "teal", "0,0 %"), ("+ edad", 1.0, "teal", "1,0 %"), ("+ rol", 19.4, "gold", "19,4 %"),
             ("+ dispositivo", 51.4, "coral", "51,4 %"), ("+ idioma", 64.2, "coral", "64,2 % únicas"),
             ("5 atributos, generalizados", 17.2, "gold", "17,2 %")]
    return bars("Participantes únicos entre 500 al combinar atributos aparentemente inocuos",
                "Barras con el porcentaje de 500 participantes sintéticos que son únicos según los atributos combinados: región 0 por ciento, más edad 1, más rol 19,4, más dispositivo 51,4, más idioma 64,2; con los cinco atributos generalizados en cuatro zonas y dos edades, 17,2.",
                items, 9, "Ningún atributo identifica a nadie por separado; cinco juntos aíslan a casi dos de cada tres personas. Generalizar (12 regiones → 4 zonas, 6 edades → 2) baja la unicidad a 17,2 %, aún con grupos menores de cinco en el 53,8 % de los casos.",
                label_w=250, width=1000, note_kind="coral", foot=SINT)


def se129_hash() -> Fig:
    return grouped_bars(
        "Seudonimizar con un hash sin clave no protege un espacio pequeño",
        "Barras agrupadas con los segundos que tarda recorrer candidatos para recuperar identificadores seudonimizados con SHA-256 sin clave: 19,6 en Windows y 16,2 en Ubuntu para los diez millones de números, 1,70 y 1,31 para el primer millón; contra HMAC con clave, dos millones de candidatos no recuperan ninguno.",
        ["10 M de candidatos (5 de 5 recuperados)", "Primer millón (2 de 5 recuperados)"],
        [("Windows", [19.6, 1.70], "navy"), ("Ubuntu (WSL2)", [16.2, 1.31], "teal")],
        unit="Segundos", decimals=2, plot_h=260,
        note="Contra HMAC-SHA-256 con clave secreta, un atacante sin clave y con 2 M de candidatos recupera 0 de 5. Los tiempos cambian de equipo en equipo (solo un núcleo, un bucle de Python); lo que importa es el orden de magnitud: segundos. El hash simple solo oculta el valor si el espacio de entradas es enorme.",
        note_kind="coral", foot=MEDIDO)

def se129_detector() -> Fig:
    return heatmap(
        "Detector de datos personales con expresiones regulares: precisión 0,75, exhaustividad 0,50",
        "Mapa de calor de la matriz de confusión de doce notas sintéticas: tres datos personales detectados, tres no detectados (un correo ofuscado y dos identificaciones indirectas), un código de pedido marcado como teléfono y cinco rechazos correctos; precisión 0,75 y exhaustividad 0,50.",
        ["Hay dato personal (6)", "No hay dato personal (6)"], ["Detectado", "No detectado"],
        [[3, 3], [1, 5]], unit="Notas", scale="navy", vmin=0, vmax=6, decimals=0, highlight=[(0, 1), (1, 0)], label_w=220,
        note="Aciertos 3, falso positivo 1, omisiones 3 y rechazos correctos 5 (TP 3, FP 1, FN 3, TN 5; las celdas resaltadas son los errores). Una revisión automática reduce el esfuerzo pero no sustituye la minimización ni la revisión humana: los identificadores indirectos y los textos libres escapan al patrón.",
        note_kind="gold", foot=SINT)

# ---------------------------------------------------------------- SE-130
def se130_regla() -> Fig:
    return grouped_bars(
        "Regla de abandono definida de antemano frente a consumir todo el presupuesto",
        "Barras agrupadas con las personas consumidas de media en 300 simulaciones: con presupuesto fijo se consumen 300 siempre; con la regla de abandono se consumen 103 si la idea es mala y 296 si es buena, y se abandona una idea buena el 2 por ciento de las veces.",
        ["Idea mala (tasa real 5 %)", "Idea buena (tasa real 15 %)"],
        [("Presupuesto fijo de 300", [300, 300], "grey"), ("Regla: abandonar si P(tasa > 10 %) < 5 %", [103, 296], "teal")],
        unit="Personas consumidas (media)", decimals=0, plot_h=260,
        note="El presupuesto fijo abandona el 100 % de las ideas malas y el 0 % de las buenas; la regla abandona el 100 % de las malas y el 2 % de las buenas. Ahorra dos tercios del esfuerzo cuando la idea es mala y casi nada cuando es buena, a cambio de ese 2 % de abandonos erróneos, que debe escribirse antes de empezar.",
        note_kind="teal", foot=SINT)

def se130_zona_gris() -> Fig:
    ns = [30, 60, 120, 240, 480]
    return line_chart(
        "Cuántas personas hacen falta para decidir entre «no éxito» (5 %) y «viable» (15 %)",
        "Líneas en escala logarítmica horizontal con el porcentaje de 2000 simulaciones que llega a la conclusión correcta: con 30 personas se concluye no éxito el 21,4 por ciento de las veces si la tasa real es 5 y viable el 68,2 si es 15; con 120, 84,3 y 95,3; con 240, 99,2 y 99,8.",
        [("Concluye «no éxito» (tasa real 5 %)", list(zip(ns, [21.4, 63.7, 84.3, 99.2, 100.0])), "coral"),
         ("Concluye «viable» (tasa real 15 %)", list(zip(ns, [68.2, 81.3, 95.3, 99.8, 100.0])), "teal")],
        x_label="Personas (n)", y_label="Simulaciones con la conclusión correcta (%)",
        x_ticks=[(30, "30"), (60, "60"), (120, "120"), (240, "240"), (480, "480")], y_ticks=[0, 20, 40, 60, 80, 100],
        log_x=True, point_labels="all", decimals=1, plot_h=300,
        note="Criterio: «no éxito» si el límite superior del intervalo de Wilson al 90 % queda bajo 12 %; «viable» si el inferior supera 6 %. Con 30 personas la mayoría de las pruebas queda en la zona gris: el resultado correcto es «no se puede decidir todavía», y debe estar previsto.",
        note_kind="gold", foot=SINT)

def se130_criterios() -> Fig:
    return heatmap(
        "Criterios de abandono: umbral, comparador, ventana y responsable",
        "Mapa de calor con ocho criterios de abandono según si son medibles y si la regla los acepta: tres medibles aceptados, cinco no medibles rechazados y ninguno mal clasificado; acierta los ocho ejemplos con los que se escribió.",
        ["Medible (3)", "No medible (5)"], ["La regla acepta", "La regla rechaza"],
        [[3, 0], [0, 5]], unit="Criterios", scale="navy", vmin=0, vmax=5, decimals=0, label_w=170,
        note="3 de 3 aceptados correctamente y 5 de 5 rechazados. Un criterio medible tiene número, comparador, ventana de tiempo y responsable; «Si no funciona, lo dejamos» no tiene ninguno. La regla se escribió viendo estos ocho; un criterio bien formado puede ser absurdo («menos de 2 de 1 000 en 10 años») y la regla no lo notaría. Medible no es lo mismo que razonable.",
        note_kind="gold", foot=SINT)

# ---------------------------------------------------------------- SE-131
def se131_preguntas() -> Fig:
    return grouped_bars(
        "Clasificar preguntas de entrevista (guiada / pasado / otra) con reglas léxicas",
        "Barras agrupadas con las preguntas clasificadas: la regla léxica acierta las 18 preguntas con las que se escribió y solo 3 de 6 preguntas nuevas; por ejemplo no reconoce «¿Recomendarías esta herramienta a un colega?» como guiada.",
        ["Preguntas con las que se escribió la regla", "Preguntas nuevas"],
        [("Preguntas", [18, 6], "grey"), ("Acertadas", [18, 3], "teal")],
        unit="Preguntas", decimals=0, plot_h=260,
        note="Exactitud 100 % con las 18 preguntas de ajuste y 50 % con las 6 nuevas. Con 18 ejemplos el 100 % no significa nada: la regla se ajustó a ellos. Tampoco reconoce «Mostrame cómo entregas una tarea» como pregunta sobre comportamiento pasado. Una lista de palabras no sustituye el juicio; sirve como revisión previa, no como árbitro.",
        note_kind="coral", foot=SINT)

def se131_rubrica() -> Fig:
    return stacked_bars(
        "Rúbrica de investigabilidad: regla automática frente a etiqueta manual",
        "Barras apiladas horizontales con la coincidencia entre la regla y la etiqueta manual: los doce enunciados de ajuste coinciden todos, con kappa igual a 1, y de tres casos nuevos coinciden dos y discrepa uno, vendedoras pierden pedidos.",
        ["Enunciados con los que se escribió la regla", "Casos nuevos"],
        [("Coinciden", [12, 2], "teal"), ("Discrepan", [0, 1], "coral")],
        unit="Enunciados", horizontal=True, decimals=0, label_w=260,
        note="Discrepa «Las vendedoras pierden pedidos cuando el teléfono se queda sin red» (regla: no; persona: sí). Las etiquetas manuales son de una sola persona (el autor): sin segunda persona no hay acuerdo entre codificadores, solo coherencia propia. Un kappa de 1 sobre los ejemplos de ajuste no predice el comportamiento con casos nuevos.",
        note_kind="gold", foot=SINT)

def se131_peticiones() -> Fig:
    items = [("Exportar (3 peticiones)", 3, "teal", "N1 · 3"), ("Seguimiento docente (3)", 3, "teal", "N2 · 3"), ("Accesibilidad visual (3)", 3, "teal", "N3 · 3"),
             ("Recordar fechas (3)", 3, "teal", "N4 · 3"), ("Ayuda humana (1)", 1, "gold", "N5 · 1"), ("No perder el trabajo (3)", 3, "teal", "N6 · 3")]
    return bars("Dieciséis peticiones, seis necesidades de fondo",
                "Barras con el número de peticiones por necesidad de fondo: exportar, seguimiento docente, accesibilidad visual, recordar fechas y no perder el trabajo tienen tres peticiones cada una y ayuda humana una; en total 16 peticiones, 6 necesidades.",
                items, 120, "Razón 2,67 peticiones por necesidad. La entropía baja de 4,00 bits (16 peticiones distintas) a 2,51 bits (6 necesidades). Agrupar peticiones en necesidades es juicio del investigador, hecho aquí por una persona; otra persona podría separar N2 en dos.",
                label_w=280, width=1000, note_kind="gold", foot="Peticiones sintéticas agrupadas a mano; el cálculo de razón y entropía es determinista.")


# ---------------------------------------------------------------- SE-132
def se132_mutaciones() -> Fig:
    return stacked_bars(
        "Validador de brief: 10 de 12 mutaciones detectadas",
        "Barras apiladas horizontales con las mutaciones aplicadas a un brief válido por grupo: el validador detecta diez de doce, entre ellas evidencia ausente, cita inexistente, un solo participante, decisión sin responsable y dato personal, pero no detecta un número alterado ni una afirmación exagerada.",
        ["Quitar la evidencia de una afirmación", "Citar una evidencia inexistente", "Un solo participante", "Respaldo solo por lo que dijeron", "Decisión sin responsable / sin fecha", "Criterio de abandono vago",
         "Sin límites · correo · problema como solución", "Cambiar «42 tickets» por «420»", "Cambiar «una vez por semana» por «siempre»"],
        [("Detectadas", [1, 1, 1, 1, 2, 1, 3, 0, 0], "teal"), ("No detectadas", [0, 0, 0, 0, 0, 0, 0, 1, 1], "coral")],
        unit="Mutaciones", horizontal=True, decimals=0, label_w=300,
        note="Lo que el validador no ve es semántico: que los números coincidan con la fuente y que la afirmación no exagere. Esas dos comprobaciones requieren revisión humana o una comparación explícita de cifras. Un brief que pasa el validador no es, por eso, verdadero.",
        note_kind="coral", foot=SINT)

def se132_pesos() -> Fig:
    return grouped_bars(
        "Mismas señales, tres ponderaciones, tres órdenes distintos",
        "Barras agrupadas con la puntuación de tres opciones bajo tres ponderaciones de las mismas señales: pesar igual da primero aviso de sesión con 12; comportamiento y compromiso por tres da primero recuperar borradores con 22; compromiso por cinco da primero panel docente con 20.",
        ["Todas las señales valen igual", "Comportamiento y compromiso ×3", "Compromiso ×5, comportamiento ×2"],
        [("Aviso de sesión", [12, 18, 15], "gold"), ("Recuperar borradores", [10, 22, 19], "teal"), ("Panel docente", [7, 15, 20], "navy")],
        unit="Puntuación", decimals=0, plot_h=280,
        note="Señales (dijeron, hicieron, se comprometieron): aviso de sesión (9, 3, 0), recuperar borradores (4, 5, 1), panel docente (3, 1, 3). El orden depende más del peso que del dato; el brief debe declarar el peso y mostrar que la conclusión se sostiene bajo varios.",
        note_kind="gold", foot="Cálculo exacto con señales sintéticas; los pesos son supuestos del autor.")

def se132_decision() -> Fig:
    items = [("Opción A (beneficio, miles)", 10, 30.4, 60, "teal", "mediana 30,4"), ("Opción B (beneficio, miles)", 0, 32.6, 70, "gold", "mediana 32,6")]
    return intervals("Dos opciones con beneficios inciertos: ¿alcanza la mediana para decidir?",
                     "Gráfico de intervalos: la opción A va de 10 a 60 con mediana 30,4 y la opción B de 0 a 70 con mediana 32,6; en 20 000 sorteos A supera a B el 47,1 por ciento de las veces.",
                     items, 75, "miles",
                     note="P(A mejor que B) = 47,1 %: es una moneda al aire. B tiene la mediana más alta y también el peor extremo (0). Cuando los rangos se solapan así, el brief debe proponer aprender más o elegir la opción reversible, no declarar un ganador.", label_w=260)


FIGURES = {
    "se-127-personas-por-brazo.svg": se127_muestra,
    "se-127-mirar-resultados-varias-veces.svg": se127_miradas,
    "se-127-intervalo-de-wilson-puerta-falsa.svg": se127_wilson,
    "se-128-rice-bajo-incertidumbre.svg": se128_rice,
    "se-128-coste-del-retraso-y-orden.svg": se128_retraso,
    "se-128-valor-de-aprender-antes.svg": se128_informacion,
    "se-129-unicidad-por-atributos.svg": se129_unicidad,
    "se-129-hash-sin-clave-frente-a-hmac.svg": se129_hash,
    "se-129-detector-de-datos-personales.svg": se129_detector,
    "se-130-regla-de-abandono.svg": se130_regla,
    "se-130-zona-gris-y-tamano-de-muestra.svg": se130_zona_gris,
    "se-130-criterios-medibles.svg": se130_criterios,
    "se-131-preguntas-de-entrevista-reglas.svg": se131_preguntas,
    "se-131-rubrica-de-investigabilidad.svg": se131_rubrica,
    "se-131-peticiones-y-necesidades.svg": se131_peticiones,
    "se-132-mutaciones-del-brief.svg": se132_mutaciones,
    "se-132-ponderacion-de-evidencia.svg": se132_pesos,
    "se-132-decision-con-rangos-solapados.svg": se132_decision,
}
