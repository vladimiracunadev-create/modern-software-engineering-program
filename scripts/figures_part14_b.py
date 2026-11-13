"""Figures for SE-175 to SE-180 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab
from figures_part14_a import SINT, auto_bars


# ---------------------------------------------------------------- SE-175
def se175_daltonismo() -> Fig:
    rows = [
        ["Rojo #d62728 / verde #2ca02c", "119,8", "37,6", "7,3", "124,4", "1,48"],
        ["Rojo claro / verde claro", "106,6", "24,2", "13,9", "119,1", "1,34"],
        ["Coral / verde azulado de las figuras", "90,8", "42,2", "61,3", "104,2", "1,08"],
        ["Azul / naranja", "122,0", "101,0", "118,1", "96,9", "1,90"],
        ["Ámbar / verde azulado", "77,8", "67,2", "71,9", "66,0", "1,19"],
    ]
    return tab("Distancia de color entre dos estados con visión normal y tres simulaciones de daltonismo",
               "Tabla con cinco pares de colores y su diferencia de color en CIELAB para visión normal y simulaciones de protanopía, deuteranopía y tritanopía: el par rojo y verde pasa de 119,8 a 7,3 en deuteranopía; azul y naranja se mantiene por encima de 96.",
               ["Par de estados", "Normal", "Protan.", "Deutan.", "Tritan.", "Contraste de luminancia"], rows, [330, 100, 100, 100, 100, 220], row_h=36, size=12,
               note="Distancias ΔE en CIELAB; con menos de 10 el par se confunde. Rojo y verde se vuelven casi iguales para deuteranopía (7,3) y su contraste de luminancia es 1,48:1. Aplicar las matrices de Machado en RGB lineal es una aproximación; ninguna simulación reemplaza a personas con esa visión ni abarca los casos parciales.",
               note_kind="coral", foot=SINT)


def se175_reflujo() -> Fig:
    rows = [
        ["Contenedor fluido con texto de 16 px", "No desborda", "No desborda", "No desborda (14 líneas, 36 car.)"],
        ["Contenedor fijo de 600 px", "No desborda", "No desborda", "Desborda: 600 px en 320 px"],
        ["Tabla de cinco columnas de 140 px", "No desborda", "Desborda (700 px en 640)", "Desborda: 700 px en 320 px"],
    ]
    return tab("Reflujo: la misma página ampliada en una ventana de 1 280 px",
               "Tabla de tres maquetaciones a ampliación del 100, 200 y 400 por ciento en una ventana de 1 280 píxeles: el contenedor fluido nunca desborda, el de 600 píxeles desborda a 400 por ciento y la tabla de 700 píxeles ya desborda a 200 por ciento.",
               ["Maquetación", "100 % (1 280 px CSS)", "200 % (640 px CSS)", "400 % (320 px CSS)"], rows, [360, 200, 230, 300], row_h=40, size=12,
               note="Ampliar el texto al 400 % equivale a un ancho de 320 px CSS en una ventana de 1 280 px; el criterio de reflujo pide no exigir desplazamiento en dos dimensiones. El cálculo compara anchos fijos con el ancho disponible y supone 0,5 em por carácter: no sustituye abrir la página y ampliarla.",
               note_kind="gold", foot=SINT)


def se175_inversion() -> Fig:
    items = [
        ("Pares de 20 000 que pasan 4,5:1 antes", 2441, "gold", "2 441"),
        ("Pares que pasan tras invertir los colores", 2499, "gold", "2 499"),
        ("Pierden el cumplimiento al invertir", 956, "coral", "956"),
        ("Ganan el cumplimiento al invertir", 1014, "teal", "1 014"),
    ]
    return auto_bars("Invertir los colores ingenuamente para un modo oscuro no conserva el contraste",
                     "Barras: de 20 000 pares de colores al azar, 2 441 pasan 4,5 a 1; tras invertir cada canal pasan 2 499, pero 956 de los que pasaban dejan de pasar y 1 014 que fallaban pasan.",
                     items, "El total casi no cambia y esconde que casi cuatro de cada diez pares (956 de 2 441) cambian de lado. Un modo oscuro se diseña con pares calculados, no con una operación sobre los canales. Los pares son aleatorios y uniformes en sRGB, no una paleta real.",
                     label_w=420, width=1040, headroom=200)


# ---------------------------------------------------------------- SE-176
def se176_rejilla() -> Fig:
    items = [
        ("Dos puntos de corte: tarjetas de menos de 280 px", 212, "coral", "212 de 10 000"),
        ("Dos puntos de corte: desborde horizontal", 0, "teal", "0"),
        ("Rejilla fluida con mínimo de 280 px: fallos", 81, "gold", "81"),
    ]
    return auto_bars("Anchos de pantalla de un conjunto sintético de 10 000 con tres maquetaciones",
                     "Barras: sobre 10 000 anchos de pantalla sintéticos, una maquetación con puntos de corte en 768 y 1 024 píxeles deja 212 tarjetas más estrechas que 280 píxeles y ningún desborde; una rejilla fluida con mínimo de 280 píxeles falla en 81.",
                     items, "Los 212 fallos de la maquetación fija son anchos de 280 a 311 px (una columna con márgenes queda bajo 280 px); los 81 de la rejilla fluida, anchos de 280 a 291 px. La mezcla de anchos de pantalla es una asignación del autor y no refleja a ninguna población real de usuarios.",
                     label_w=440, width=1080, headroom=200)


def se176_preferencias() -> Fig:
    items = [
        ("32 combinaciones completas", 60, "teal", "60 de 60"),
        ("6 filas que cubren todos los pares", 55, "gold", "55 de 60"),
        ("6 filas al azar (media de 200 sorteos)", 50.4, "coral", "50,4 de 60"),
    ]
    return auto_bars("Defectos de preferencias del usuario hallados según el diseño de la matriz de pruebas",
                     "Barras: de 60 defectos sintéticos que dependen de una, dos o tres preferencias a la vez, las 32 combinaciones completas matan 60, seis filas que cubren todos los pares matan 55 y seis filas al azar matan 50,4 de media.",
                     items, "Cinco preferencias binarias (movimiento reducido, esquema oscuro, contraste, colores forzados, zoom del 200 %) dan 32 combinaciones; seis filas cubren los 40 pares. Quedan sin cubrir los defectos de tres preferencias. Los 60 defectos son una mezcla supuesta (20 de una, 28 de dos, 12 de tres).",
                     label_w=400, width=1000, headroom=220)


def se176_imagenes() -> Fig:
    rows = [
        ["Teléfono de 360 px, densidad 3", "810 kB · 4,2 s", "202 kB · 1,2 s", "−75 %"],
        ["Teléfono de 390 px, densidad 3", "810 kB · 4,2 s", "202 kB · 1,2 s", "−75 %"],
        ["Tableta de 800 px, densidad 2", "810 kB · 4,2 s", "810 kB · 4,2 s", "0 %"],
        ["Portátil de 1 280 px, densidad 1", "810 kB · 4,2 s", "810 kB · 4,2 s", "0 %"],
    ]
    return tab("Una imagen de 2 400 px frente a cuatro anchos con srcset en una conexión supuesta de 1,6 Mbit/s",
               "Tabla de cuatro dispositivos: una única imagen de 2 400 píxeles pesa 810 kilobytes y tarda 4,2 segundos a 1,6 megabits por segundo; con cuatro anchos disponibles, los teléfonos descargan 202 kilobytes en 1,2 segundos y los equipos que necesitan el ancho máximo no ganan nada.",
               ["Dispositivo", "Una imagen", "Con cuatro anchos", "Variación"], rows, [340, 220, 220, 150], row_h=36, size=13,
               note="Peso estimado como píxeles × 0,5625 × 0,25 bytes por píxel (supuesto del autor) y tiempo como bytes ÷ ancho de banda + 0,15 s de latencia. La compresión real depende del contenido y del formato; el ahorro de un teléfono se debe a que una imagen más pequeña basta y no a una mejor compresión.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-177
def se177_plurales() -> Fig:
    items = [
        ("Inglés, español", 2, "teal", "2 formas (one, other)"),
        ("Ruso, polaco", 3, "gold", "3 formas (one, few, many)"),
        ("Árabe", 6, "coral", "6 formas (zero, one, two, few, many, other)"),
    ]
    return auto_bars("Formas de plural que necesita una cadena para los números de 0 a 120",
                     "Barras: para los números de 0 a 120, inglés y español necesitan 2 formas de plural, ruso y polaco 3 y árabe 6; una regla que solo distingue el 1 del resto se equivoca en 120 de 121 números en ruso y polaco y en 117 en árabe.",
                     items, "Las categorías vienen de las reglas de CLDR para enteros. Una regla «si n es 1, singular, si no, plural» sirve en inglés y español, y en ruso o polaco se equivoca incluso con 21 (que es «one»). Se contó de 0 a 120: con números mayores y decimales hay más casos, y español añade una categoría para millones.",
                     label_w=260, width=1090, headroom=390)


def se177_unicode() -> Fig:
    rows = [
        ["José (composición precompuesta)", "4", "5", "4"],
        ["José con acento combinado", "5", "6", "5"],
        ["Zoë y Zoë con diéresis combinada", "3 y 4", "4 y 5", "—"],
        ["Mujer tecnóloga: tres símbolos unidos", "3", "11", "5"],
        ["straße en mayúsculas", "STRASSE", "—", "—"],
        ["«İ».lower()", "2 puntos de código", "—", "—"],
    ]
    return tab("Una misma «letra» que se cuenta de maneras distintas",
               "Tabla de cadenas con su longitud en puntos de código, en bytes UTF-8 y en unidades UTF-16: José tiene 4 o 5 puntos según se componga el acento, un emoji de tres símbolos unidos tiene 3 puntos, 11 bytes y 5 unidades, y las mayúsculas de «straße» son «STRASSE».",
               ["Cadena", "Puntos de código", "Bytes UTF-8", "Unidades UTF-16"], rows, [400, 220, 190, 190], row_h=36, size=12,
               note="De 7 nombres con variantes de composición, 7 son distintos como bytes y 4 tras normalizar a NFC. Cortar «x👩‍💻» tras 2 puntos deja un emoji partido; ordenar por punto de código coloca «Ángel» y «Ñandú» detrás de «Zoë». Sin biblioteca de CLDR el orden es solo una aproximación.",
               note_kind="gold", foot=SINT)


def se177_ambiguedad() -> Fig:
    rows = [
        ["1.234", "1,234 (inglés de EE. UU.)", "1 234 (español de Chile)", "Mil veces de diferencia"],
        ["1,234", "1 234", "1,234", "Mil veces de diferencia"],
        ["0,5", "5 (se ignora la coma)", "0,5", "Diez veces de diferencia"],
        ["1.5", "1,5", "15", "Diez veces de diferencia"],
        ["Fechas de 2026 como DD/MM o MM/DD", "132 de 365", "36,2 % ambiguas", "Día ≤ 12 y distinto del mes"],
    ]
    return tab("Cadenas numéricas y fechas que dos configuraciones leen de forma distinta",
               "Tabla: la cadena 1.234 vale 1,234 en inglés de EE. UU. y mil doscientos treinta y cuatro en español de Chile; 0,5 se lee 5 si se ignora la coma; y 132 de las 365 fechas de 2026 son ambiguas entre día y mes primero, el 36,2 por ciento.",
               ["Texto", "Lectura A", "Lectura B", "Consecuencia"], rows, [270, 270, 250, 230], row_h=42, size=12,
               note="Las lecturas aplican a mano las convenciones de dos configuraciones (coma o punto decimal); no consultan ninguna biblioteca de localización. El 36,2 % cuenta los días con día entre 1 y 12 y distinto del mes; guardar fechas como ISO 8601 y presentar el mes con su nombre elimina la ambigüedad.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-178
def se178_cinco() -> Fig:
    items = [
        ("5 participantes: fórmula con p medio", 76.6, "gold", "76,6 %"),
        ("5 participantes: simulación con p heterogéneo", 62.0, "coral", "62,0 % (mín. 48)"),
        ("8 participantes: fórmula", 90.2, "gold", "90,2 %"),
        ("8 participantes: simulación", 70.3, "coral", "70,3 % (mín. 57)"),
        ("15 participantes: fórmula", 98.7, "gold", "98,7 %"),
        ("15 participantes: simulación", 79.8, "coral", "79,8 % (mín. 65)"),
        ("20 participantes: simulación", 83.2, "teal", "83,2 % (mín. 70)"),
    ]
    return auto_bars("Problemas de usabilidad hallados: fórmula con probabilidad media y simulación heterogénea",
                     "Barras: con 40 problemas cuya probabilidad de hallazgo varía entre 0 y 1 (media 0,25), la fórmula con la probabilidad media predice 76,6 por ciento con cinco participantes, pero la simulación halla 62,0; con 15 la fórmula dice 98,7 y la simulación 79,8.",
                     items, "La fórmula 1−(1−p)^n supone que todos los problemas tienen la misma probabilidad; con probabilidades heterogéneas (beta 0,7 y 2), los problemas raros siguen sin verse. Ocho de los 40 problemas tienen p menor que 0,05. La distribución es un supuesto del autor, no una medición de ningún producto.",
                     label_w=420, width=1090, headroom=250)


def se178_intervalos() -> Fig:
    rows = [
        ["4 de 5", "45 % – 100 %", "38 % – 96 %", "28 % – 99 %"],
        ["8 de 10", "55 % – 100 %", "49 % – 94 %", "44 % – 97 %"],
        ["16 de 20", "62 % – 98 %", "58 % – 92 %", "56 % – 94 %"],
        ["5 de 5", "100 % – 100 %", "57 % – 100 %", "48 % – 100 %"],
        ["80 de 100", "72 % – 88 %", "71 % – 87 %", "71 % – 87 %"],
    ]
    return tab("Éxito de una tarea con pocas personas: tres intervalos del 95 %",
               "Tabla de cinco resultados con tres intervalos del 95 por ciento: con 4 éxitos de 5, Wald da de 45 a 100, Wilson de 38 a 96 y Clopper-Pearson de 28 a 99; con 5 de 5, Wald da un intervalo de ancho cero y los otros llegan hasta 57 y 48.",
               ["Resultado", "Wald", "Wilson", "Clopper-Pearson"], rows, [200, 260, 260, 260], row_h=36, size=13,
               note="Cobertura simulada de un intervalo nominal del 95 % con n = 10 y p = 0,9: Wald 64,4 %, Wilson 93,2 %, Clopper-Pearson 98,9 %. Con 5 de 5, el intervalo de Wald dice que fallar es imposible. Con pocas personas, el intervalo importa más que el porcentaje, y ancho no significa error de cálculo: es la información que hay.",
               note_kind="gold", foot=SINT)


def se178_potencia() -> Fig:
    items = [
        ("Diferencia de 7 puntos, 8 por grupo", 22, "coral", "22 %"),
        ("Diferencia de 7 puntos, 20 por grupo", 39, "gold", "39 %"),
        ("Diferencia de 7 puntos, 40 por grupo", 69, "gold", "69 %"),
        ("Diferencia de 15 puntos, 8 por grupo", 61, "gold", "61 %"),
        ("Diferencia de 15 puntos, 20 por grupo", 97, "teal", "97 %"),
        ("Sin diferencia real, 12 por grupo", 4, "teal", "4,0 % de falsos positivos"),
    ]
    return auto_bars("Probabilidad de detectar la diferencia entre dos diseños con una prueba de permutación",
                     "Barras: con desviación típica de 12 puntos de SUS, una diferencia de 7 puntos se detecta con probabilidad 22 por ciento con 8 participantes por grupo, 39 con 20 y 69 con 40; una diferencia de 15 puntos con 8 en 61 y con 20 en 97; sin diferencia real el 4 por ciento da un falso positivo.",
                     items, "Con muestras de usabilidad típicas, una diferencia moderada pasa desapercibida la mayor parte del tiempo, y el análisis no se equivoca por ello: no tenía potencia. La media base de 68 y la desviación de 12 son supuestos del autor; 150 simulaciones por celda dan una incertidumbre de varios puntos.",
                     label_w=410, width=1090, headroom=260)


# ---------------------------------------------------------------- SE-179
def se179_antes_despues() -> Fig:
    rows = [
        ["Sin idioma, título genérico, sin región principal ni encabezados", "4", "0"],
        ["Campos sin etiqueta (solo placeholder)", "2", "0"],
        ["Imagen sin texto alternativo", "1", "0"],
        ["Control hecho con div y clic (inaccesible con teclado)", "1", "0"],
        ["Enlace sin texto", "1", "0"],
        ["Total de hallazgos del auditor", "9", "0"],
    ]
    return tab("Auditoría de un formulario de entrega antes y después de reparar",
               "Tabla: un formulario de entrega con nueve hallazgos del auditor automático (sin idioma, título genérico, sin región principal ni encabezados, dos campos sin etiqueta, una imagen sin alt, un div clicable y un enlace vacío) queda en cero hallazgos tras la reparación.",
               ["Categoría de hallazgo", "Antes", "Después"], rows, [640, 150, 150], row_h=36, size=13,
               note="Cero hallazgos significa que las reglas no encuentran nada, no que el flujo sea accesible: tras la reparación, un texto alternativo, una etiqueta o un orden de foco pueden ser incorrectos sin que el auditor lo note, y el flujo completo (error, recuperación, confirmación) no se recorrió.",
               note_kind="coral", foot=SINT)


def se179_orden() -> Fig:
    items = [
        ("Primero lo más fácil de reparar", 51, "gold", "51 %"),
        ("Primero lo de mayor valor por hora", 51, "gold", "51 %"),
        ("Primero lo más grave y que afecta a más gente", 71, "teal", "71 %"),
    ]
    return auto_bars("Barreras bloqueantes eliminadas tras cuatro horas de trabajo según el orden de reparación",
                     "Barras: con 12 hallazgos y 4 horas de trabajo, reparar primero lo más fácil o lo de mayor valor por hora elimina 51 por ciento de la población bloqueada, y reparar primero lo más grave y que afecta a más gente elimina 71 por ciento.",
                     items, "El orden por gravedad gana porque los bloqueos graves son caros: en el reparto de valor por hora aparecen detrás de arreglos baratos y poco graves. Alcance, gravedad y horas son estimaciones del autor sobre un flujo sintético; con otras horas el orden ganador cambia y eso es lo que hay que comprobar.",
                     label_w=450, width=1080, headroom=170)


def se179_regresion() -> Fig:
    rows = [
        ["Quitar etiqueta, alt, lang, encabezado o región principal", "5 de 5", "Presencia de un atributo o elemento"],
        ["Título genérico, enlace vacío, botón convertido en div", "3 de 3", "Regla de contenido o de rol"],
        ["Etiqueta que dice otra cosa", "0 de 1", "Texto presente pero falso"],
        ["Botón con texto «Clic»", "0 de 1", "Nombre presente pero poco informativo"],
        ["Quitar describedby, accept o autocomplete", "0 de 3", "Atributos útiles que ninguna regla exige"],
    ]
    return tab("Mutaciones del formulario reparado que el auditor automático detecta",
               "Tabla: de 13 mutaciones del formulario reparado, el auditor detecta 8, las que quitan un elemento o atributo exigido o dejan un contenido vacío, y no detecta una etiqueta falsa, un texto de botón poco informativo ni la pérdida de tres atributos de apoyo.",
               ["Mutación", "Detectadas", "Naturaleza"], rows, [480, 150, 350], row_h=40, size=12,
               note="Una prueba de regresión automática protege lo que sus reglas ven: 8 de 13. Lo demás exige una lista manual con responsable y fecha. La suite de regresión no sustituye la reevaluación con personas cuando el flujo cambia.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-180
def se180_barrera() -> Fig:
    items = [
        ("Barrera que afecta al 10 %, 5 participantes", 41.0, "coral", "41,0 %"),
        ("Barrera del 10 %, 12 participantes", 71.8, "gold", "71,8 %"),
        ("Barrera del 20 %, 5 participantes", 67.2, "gold", "67,2 %"),
        ("Barrera del 20 %, 12 participantes", 93.1, "teal", "93,1 %"),
        ("Barrera del 33 %, 5 participantes", 86.5, "teal", "86,5 %"),
    ]
    return auto_bars("Probabilidad de ver al menos una vez una barrera según cuántas personas participan",
                     "Barras: una barrera que afecta al 10 por ciento de la población se ve al menos una vez con probabilidad 41,0 por ciento con cinco participantes y 71,8 con doce; una que afecta al 20 por ciento, 67,2 y 93,1; una del 33 por ciento con cinco, 86,5.",
                     items, "La probabilidad es 1−(1−p)^n y supone participantes independientes y representativos. Cinco personas pueden no ver una barrera que afecta a una de cada diez, y eso no la hace inexistente: el plan debe declarar qué prevalencia se podría ver y cuál no.",
                     label_w=430, width=1050, headroom=210)


def se180_modalidades() -> Fig:
    items = [
        ("6 participantes reclutados al azar", 38.1, "coral", "38,1 %"),
        ("8 participantes", 62.3, "gold", "62,3 %"),
        ("12 participantes", 87.5, "gold", "87,5 %"),
        ("16 participantes", 96.0, "teal", "96,0 %"),
    ]
    return auto_bars("Probabilidad de que cuatro modalidades de uso estén todas representadas",
                     "Barras: reclutando al azar entre cuatro modalidades de uso con igual probabilidad, todas están representadas con probabilidad 38,1 por ciento con seis participantes, 62,3 con ocho, 87,5 con doce y 96,0 con dieciséis.",
                     items, "Calculado por inclusión y exclusión y comprobado con 20 000 sorteos (61,9 % de fallos con 6). Reclutar por cuotas lo evita; recluta al azar solo si la modalidad no importa. Las cuatro modalidades con igual probabilidad son un supuesto: una modalidad menos frecuente hace peor el resultado.",
                     label_w=370, width=980, headroom=180)


def se180_kappa() -> Fig:
    items = [
        ("Prevalencia de «cumple» del 50 %", 0.70, "teal", "kappa 0,70 · acuerdo 85,3 %"),
        ("Prevalencia del 90 %", 0.46, "gold", "kappa 0,46 · acuerdo 85,3 %"),
        ("Prevalencia del 97 %", 0.21, "coral", "kappa 0,21 · acuerdo 85,3 %"),
    ]
    return auto_bars("Dos evaluadores que se equivocan el 8 % de las veces: acuerdo y kappa según la prevalencia",
                     "Barras: dos evaluadores con 8 por ciento de error independiente tienen un acuerdo medio de 85,3 por ciento en los tres casos, pero kappa baja de 0,70 con prevalencia del 50 por ciento a 0,46 con 90 y 0,21 con 97.",
                     items, "Un criterio que casi siempre se cumple produce acuerdos altos aunque los evaluadores no distingan nada: el acuerdo por azar sube con la prevalencia. Informar solo el porcentaje de acuerdo oculta eso. El 8 % de error y la independencia entre evaluadores son supuestos; 300 simulaciones de 100 criterios por fila.",
                     label_w=330, width=1060, headroom=340)


FIGURES = {
    "se-175-pares-bajo-daltonismo.svg": se175_daltonismo,
    "se-175-reflujo-con-zoom.svg": se175_reflujo,
    "se-175-inversion-ingenua.svg": se175_inversion,
    "se-176-anchos-de-pantalla.svg": se176_rejilla,
    "se-176-matriz-de-preferencias.svg": se176_preferencias,
    "se-176-peso-de-imagen.svg": se176_imagenes,
    "se-177-categorias-de-plural.svg": se177_plurales,
    "se-177-unicode-y-longitudes.svg": se177_unicode,
    "se-177-numeros-y-fechas-ambiguos.svg": se177_ambiguedad,
    "se-178-cinco-participantes.svg": se178_cinco,
    "se-178-intervalos-con-pocas-personas.svg": se178_intervalos,
    "se-178-potencia-de-la-comparacion.svg": se178_potencia,
    "se-179-antes-y-despues-del-flujo.svg": se179_antes_despues,
    "se-179-orden-de-reparacion.svg": se179_orden,
    "se-179-mutaciones-que-el-auditor-no-ve.svg": se179_regresion,
    "se-180-probabilidad-de-ver-la-barrera.svg": se180_barrera,
    "se-180-modalidades-sin-representar.svg": se180_modalidades,
    "se-180-acuerdo-sin-azar.svg": se180_kappa,
}
