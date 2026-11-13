"""Figures for SE-127 to SE-132 (synthetic data, fixed seeds; timings from CPython 3.12.9 on Windows 11 and 3.12.3 on Ubuntu/WSL2)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab
from figures_part10_a import SINT, intervals

MEDIDO = "Tiempos medidos con CPython 3.12.9 en Windows 11 y 3.12.3 en Ubuntu (WSL2); dependen del equipo y se leen como razones."


# ---------------------------------------------------------------- SE-127
def se127_muestra() -> Fig:
    rows = [["10 % → 12 %", "3 841", "81,2 % con n = 3 841 · 17,3 % con 500 · 9,4 % con 200"],
            ["10 % → 15 %", "686", "—"], ["10 % → 20 %", "199", "—"], ["40 % → 45 %", "1 534", "—"]]
    return tab("Personas por brazo para detectar una diferencia con 80 % de potencia y 5 % de error",
               "Tabla de tamaños de muestra por brazo: pasar de 10 a 12 por ciento exige 3841 personas por brazo, de 10 a 15 exige 686, de 10 a 20 exige 199 y de 40 a 45 exige 1534; con 500 personas la potencia simulada del primer caso es solo 17,3 por ciento.",
               ["Cambio a detectar", "n por brazo", "Potencia simulada (4 000 repeticiones)"], rows, [200, 160, 520], row_h=44, size=13,
               note="Con 500 personas por brazo, un experimento que busca pasar del 10 % al 12 % detecta el efecto una de cada seis veces: no sirve para decidir aunque se ejecute bien. Un prototipo con 30 personas solo puede ver efectos enormes.", note_kind="coral", foot=SINT)


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
    rows = [["Aviso de sesión", "7 200", "98,9 %", "58,0 %"], ["Botón de entrega visible", "6 000", "97,2 %", "37,8 %"],
            ["Recuperar borradores", "3 200", "75,6 %", "3,9 %"], ["Recordatorios por correo", "2 000", "27,1 %", "0,3 %"],
            ["Integración con calendario", "800", "0,6 %", "0,0 %"], ["Rediseño de navegación", "750", "0,4 %", "0,0 %"]]
    return tab("RICE de doce ítems con ±40 % de incertidumbre en alcance, impacto y confianza (+60 % en esfuerzo)",
               "Tabla de seis ítems de doce: aviso de sesión con RICE 7200 es primero en 58 por ciento de 5000 simulaciones y está en el top tres en 98,9; botón de entrega visible es primero en 37,8; recuperar borradores entra al top tres en 75,6 por ciento.",
               ["Ítem", "RICE base", "En el top 3", "Primero"], rows, [330, 150, 170, 150], row_h=40, size=13,
               note="El orden base se sostiene para los tres primeros, pero el «primero» cambia en cuatro de cada diez simulaciones. RICE con todas las entradas estimadas oculta ese margen. Concordancia con valor/esfuerzo sin confianza: tau 0,80; con alcance solo: 0,53.", note_kind="gold", foot=SINT)


def se128_retraso() -> Fig:
    rows = [["WSJF: coste de retraso / duración", "D, C, A, B", "119"], ["Más corto primero", "C, D, A, B", "122"],
            ["Mayor valor primero", "D, A, C, B", "126"], ["Peor de las 24 permutaciones", "B, A, C, D", "238"]]
    return tab("Coste total del retraso de cuatro trabajos según el criterio de orden",
               "Tabla con el coste de retraso acumulado de cuatro trabajos A, B, C y D: el orden WSJF D, C, A, B cuesta 119 y es el óptimo de las 24 permutaciones; más corto primero cuesta 122, mayor valor primero 126 y el peor orden 238.",
               ["Criterio", "Orden", "Coste total de retraso"], rows, [380, 200, 240], row_h=44, size=13,
               note="Trabajos (coste de retraso por semana, duración): A (8, 3), B (3, 4), C (5, 1), D (13, 2). Priorizar por valor solo, sin mirar duración, cuesta 6 % más que el óptimo; el peor orden cuesta el doble. Con duraciones inciertas el óptimo también lo es.", note_kind="gold", foot="Cálculo exacto sobre las 24 permutaciones; no depende del equipo.")


def se128_informacion() -> Fig:
    rows = [["5", "0,90", "+11,3"], ["10", "0,80", "+1,6"], ["15", "0,70", "−8,1"], ["25", "0,90", "−8,7"]]
    return tab("Valor neto de aprender antes de construir (construir ahora vale −5; no hacer nada vale 0)",
               "Tabla del valor esperado de hacer una prueba previa a construir: con coste 5 y precisión 0,90 vale 11,3; con coste 10 y precisión 0,80 vale 1,6; con coste 15 y precisión 0,70 es negativo, −8,1, y con coste 25 y precisión 0,90 también, −8,7.",
               ["Coste de la prueba", "Precisión de la prueba", "Valor esperado neto"], rows, [260, 260, 260], row_h=42, size=13,
               note="Parámetros: probabilidad de éxito 35 %, ganancia 100, coste de construir 40. Construir sin aprender vale −5. Una prueba barata y fiable convierte una apuesta negativa en positiva; una prueba cara o poco fiable destruye el valor. Aprender también cuesta.", note_kind="teal", foot="Cálculo exacto; los números son un modelo ilustrativo.")


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
    rows = [["SHA-256 sin clave de números de 7 dígitos", "5 de 5 recuperados", "19,6 s", "16,2 s"],
            ["Primer millón de candidatos", "2 de 5 recuperados", "1,70 s", "1,31 s"],
            ["HMAC-SHA-256 con clave secreta (atacante sin clave, 2 M de candidatos)", "0 de 5", "—", "—"]]
    return tab("Seudonimizar con un hash sin clave no protege un espacio pequeño",
               "Tabla: recorrer los diez millones de números de siete dígitos recupera los cinco identificadores seudonimizados con SHA-256 sin clave en 19,6 segundos en Windows y 16,2 en Ubuntu; contra HMAC con clave secreta, dos millones de candidatos no recuperan ninguno.",
               ["Procedimiento", "Resultado", "Windows", "Ubuntu (WSL2)"], rows, [430, 190, 120, 140], row_h=56, size=12,
               note="Los tiempos cambian de equipo en equipo (solo un núcleo, un bucle de Python); lo que importa es el orden de magnitud: segundos. El hash simple solo oculta el valor si el espacio de entradas es enorme. Con clave, el atacante debe obtenerla además de adivinar el valor.", note_kind="coral", foot=MEDIDO)


def se129_detector() -> Fig:
    rows = [["Correo y teléfonos escritos de forma normal", "3 de 3", "Detectados"], ["«ana punto prueba arroba ejemplo punto org»", "0 de 1", "No detectado"],
            ["«trabaja en la única farmacia del pueblo»", "0 de 1", "No detectado (identifica sin ser un dato)"], ["«el correo del trabajo de su cuñada»", "0 de 1", "No detectado"],
            ["Código de pedido «20260312-0042»", "1 falso positivo", "Marcado como teléfono"]]
    return tab("Detector de datos personales con expresiones regulares: precisión 0,75, exhaustividad 0,50",
               "Tabla de doce notas sintéticas: el detector acierta tres de los seis datos personales, deja pasar un correo ofuscado y dos identificaciones indirectas, y marca un código de pedido como teléfono; precisión 0,75 y exhaustividad 0,50.",
               ["Caso", "Cantidad", "Resultado"], rows, [430, 150, 300], row_h=52, size=12,
               note="Tres aciertos, un falso positivo, tres omisiones y cinco rechazos correctos (TP 3, FP 1, FN 3, TN 5). Una revisión automática reduce el esfuerzo pero no sustituye la minimización ni la revisión humana: los identificadores indirectos y los textos libres escapan al patrón.", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-130
def se130_regla() -> Fig:
    rows = [["Presupuesto fijo de 300", "Mala (5 %)", "300", "100 %"], ["Presupuesto fijo de 300", "Buena (15 %)", "300", "0 %"],
            ["Regla: abandonar si P(tasa > 10 %) < 5 %", "Mala (5 %)", "103", "100 %"], ["Regla: abandonar si P(tasa > 10 %) < 5 %", "Buena (15 %)", "296", "2 %"]]
    return tab("Regla de abandono definida de antemano frente a consumir todo el presupuesto",
               "Tabla de 300 simulaciones por fila: con presupuesto fijo se consumen 300 personas siempre; con una regla que abandona si la probabilidad de superar el 10 por ciento cae bajo 5 por ciento se consumen 103 personas cuando la idea es mala y 296 cuando es buena, y se abandona una idea buena el 2 por ciento de las veces.",
               ["Política", "Realidad", "Personas consumidas (media)", "Abandona"], rows, [330, 150, 210, 140], row_h=44, size=12,
               note="La regla ahorra dos tercios del esfuerzo cuando la idea es mala y casi nada cuando es buena, a cambio de un 2 % de abandonos erróneos. Ese 2 % es una decisión consciente, no un descuido: debe escribirse antes de empezar.", note_kind="teal", foot=SINT)


def se130_zona_gris() -> Fig:
    rows = [["30", "21,4 %", "68,2 %"], ["60", "63,7 %", "81,3 %"], ["120", "84,3 %", "95,3 %"], ["240", "99,2 %", "99,8 %"], ["480", "100 %", "100 %"]]
    return tab("Cuántas personas hacen falta para decidir entre «no éxito» (5 %) y «viable» (15 %)",
               "Tabla de 2000 simulaciones por fila: con 30 personas se concluye no éxito solo el 21,4 por ciento de las veces cuando la tasa real es 5 y viable el 68,2 cuando es 15; con 120 personas, 84,3 y 95,3; con 240, 99,2 y 99,8.",
               ["n", "Concluye «no éxito» (tasa real 5 %)", "Concluye «viable» (tasa real 15 %)"], rows, [140, 380, 380], row_h=40, size=13,
               note="Criterio: «no éxito» si el límite superior del intervalo de Wilson al 90 % queda bajo 12 %; «viable» si el inferior supera 6 %. Con 30 personas la mayoría de las pruebas queda en la zona gris: el resultado correcto es «no se puede decidir todavía», y debe estar previsto.", note_kind="gold", foot=SINT)


def se130_criterios() -> Fig:
    rows = [["Si menos de 6 de 30 completan la tarea en 4 semanas, producto decide detener.", "sí", "Acepta ✔"],
            ["Si no funciona, lo dejamos.", "no", "Rechaza ✔"], ["Cancelar si la adopción es baja.", "no", "Rechaza ✔"],
            ["Detener si menos de 3 de 12 entrevistas confirman el problema; responsable: producto.", "no (falta el plazo)", "Rechaza ✔"],
            ["Si al cabo de 2 semanas menos del 10 % de 80 invitados agenda una demo, la dirección cancela.", "sí", "Acepta ✔"]]
    return tab("Criterios de abandono: umbral, comparador, ventana y responsable",
               "Tabla de cinco de ocho criterios de abandono evaluados por una regla: acepta los que tienen número, comparador, ventana de tiempo y responsable y rechaza los vagos; acierta los ocho ejemplos con los que se escribió.",
               ["Criterio", "Medible", "Resultado"], rows, [560, 170, 150], row_h=58, size=12,
               note="3 de 3 aceptados correctamente y 5 de 5 rechazados. La regla se escribió viendo estos ocho; un criterio bien formado puede ser absurdo («menos de 2 de 1 000 en 10 años») y la regla no lo notaría. Medible no es lo mismo que razonable.", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-131
def se131_preguntas() -> Fig:
    rows = [["Preguntas con las que se escribió la regla", "18", "18", "100 %"], ["Preguntas nuevas (6)", "6", "3", "50 %"]]
    return tab("Clasificar preguntas de entrevista (guiada / pasado / otra) con reglas léxicas",
               "Tabla: la regla léxica clasifica bien las 18 preguntas con las que se escribió y solo 3 de 6 preguntas nuevas; por ejemplo no reconoce «¿Recomendarías esta herramienta a un colega?» como guiada ni «Mostrame cómo entregas una tarea» como pregunta sobre comportamiento pasado.",
               ["Conjunto", "Preguntas", "Acertadas", "Exactitud"], rows, [440, 140, 140, 160], row_h=48, size=13,
               note="Con 18 ejemplos el 100 % no significa nada: la regla se ajustó a ellos. Con seis preguntas nuevas baja al 50 %. Una lista de palabras no sustituye el juicio sobre qué pregunta evita sugerir la respuesta; sirve como revisión previa, no como árbitro.", note_kind="coral", foot=SINT)


def se131_rubrica() -> Fig:
    rows = [["12 enunciados con los que se escribió la regla", "100 %", "κ = 1,00"],
            ["Caso nuevo: «Las vendedoras pierden pedidos cuando el teléfono se queda sin red»", "Regla: no · Persona: sí", "Desacuerdo"],
            ["Caso nuevo: «Hay que repensar el flujo de pagos»", "Regla: no · Persona: no", "Acuerdo"],
            ["Caso nuevo: «Los alumnos no entienden las notas»", "Regla: no · Persona: no", "Acuerdo"]]
    return tab("Rúbrica de investigabilidad: regla automática frente a etiqueta manual",
               "Tabla: con los doce enunciados de ajuste, la regla coincide con las etiquetas manuales en el 100 por ciento y kappa vale 1; con tres casos nuevos, la regla rechaza uno que la persona acepta, vendedoras pierden pedidos.",
               ["Enunciados", "Coincidencia", "Resultado"], rows, [500, 230, 150], row_h=58, size=12,
               note="Las etiquetas manuales son de una sola persona (el autor): sin segunda persona no hay acuerdo entre codificadores, solo coherencia propia. Un kappa de 1 sobre los ejemplos de ajuste no predice el comportamiento con casos nuevos.", note_kind="gold", foot=SINT)


def se131_peticiones() -> Fig:
    items = [("Exportar (3 peticiones)", 3, "teal", "N1 · 3"), ("Seguimiento docente (3)", 3, "teal", "N2 · 3"), ("Accesibilidad visual (3)", 3, "teal", "N3 · 3"),
             ("Recordar fechas (3)", 3, "teal", "N4 · 3"), ("Ayuda humana (1)", 1, "gold", "N5 · 1"), ("No perder el trabajo (3)", 3, "teal", "N6 · 3")]
    return bars("Dieciséis peticiones, seis necesidades de fondo",
                "Barras con el número de peticiones por necesidad de fondo: exportar, seguimiento docente, accesibilidad visual, recordar fechas y no perder el trabajo tienen tres peticiones cada una y ayuda humana una; en total 16 peticiones, 6 necesidades.",
                items, 120, "Razón 2,67 peticiones por necesidad. La entropía baja de 4,00 bits (16 peticiones distintas) a 2,51 bits (6 necesidades). Agrupar peticiones en necesidades es juicio del investigador, hecho aquí por una persona; otra persona podría separar N2 en dos.",
                label_w=280, width=1000, note_kind="gold", foot="Peticiones sintéticas agrupadas a mano; el cálculo de razón y entropía es determinista.")


# ---------------------------------------------------------------- SE-132
def se132_mutaciones() -> Fig:
    rows = [["Quitar toda la evidencia de una afirmación", "Detectada"], ["Citar una evidencia que no existe", "Detectada"], ["Afirmación respaldada por un solo participante", "Detectada"],
            ["Afirmación respaldada solo por lo que dijeron", "Detectada"], ["Decisión sin responsable / sin fecha", "Detectadas (2)"], ["Criterio de abandono vago", "Detectada"],
            ["Sin límites declarados · correo en la evidencia · problema como solución", "Detectadas (3)"],
            ["Cambiar «42 tickets» por «420» sin tocar la afirmación", "NO detectada"], ["Cambiar «una vez por semana» por «siempre»", "NO detectada"]]
    return tab("Validador de brief: 10 de 12 mutaciones detectadas",
               "Tabla de mutaciones aplicadas a un brief válido: el validador detecta diez de doce, entre ellas evidencia ausente, cita inexistente, un solo participante, decisión sin responsable y dato personal, pero no detecta un número alterado ni una afirmación exagerada.",
               ["Mutación del brief", "Resultado del validador"], rows, [620, 280], row_h=40, size=12,
               note="Lo que el validador no ve es semántico: que los números coincidan con la fuente y que la afirmación no exagere. Esas dos comprobaciones requieren revisión humana o una comparación explícita de cifras. Un brief que pasa el validador no es, por eso, verdadero.", note_kind="coral", foot=SINT)


def se132_pesos() -> Fig:
    rows = [["Todas las señales valen igual", "Aviso de sesión (12)", "Recuperar borradores (10)", "Panel docente (7)"],
            ["Comportamiento y compromiso ×3", "Recuperar borradores (22)", "Aviso de sesión (18)", "Panel docente (15)"],
            ["Compromiso ×5, comportamiento ×2", "Panel docente (20)", "Recuperar borradores (19)", "Aviso de sesión (15)"]]
    return tab("Mismas señales, tres ponderaciones, tres órdenes distintos",
               "Tabla: con las mismas señales de tres opciones, pesar igual da primero aviso de sesión con 12; pesar comportamiento y compromiso por tres da primero recuperar borradores con 22; pesar el compromiso por cinco da primero panel docente con 20.",
               ["Ponderación", "Primero", "Segundo", "Tercero"], rows, [270, 210, 220, 200], row_h=52, size=12,
               note="Señales (dijeron, hicieron, se comprometieron): aviso de sesión (9, 3, 0), recuperar borradores (4, 5, 1), panel docente (3, 1, 3). El orden depende más del peso que del dato; el brief debe declarar el peso y mostrar que la conclusión se sostiene bajo varios.", note_kind="gold", foot="Cálculo exacto con señales sintéticas; los pesos son supuestos del autor.")


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
