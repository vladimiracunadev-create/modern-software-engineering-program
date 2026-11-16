"""Figures for SE-205 to SE-210 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time is shown)."""
from __future__ import annotations

from figure_cases import case_cards
from figure_kit import Fig, fmt_es, grouped_bars, heatmap, line_chart, stacked_bars
from figures_part07_a import bars

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-205
def se205_navegacion() -> Fig:
    ps = [20, 40, 60, 80, 100]
    arbol = [22.05, 17.49, 12.58, 7.88, 3.0]
    indice = [4.28, 3.84, 3.33, 2.93, 2.41]
    return line_chart("Clics esperados hasta la página correcta: árbol por componente frente a índice de tareas",
                      "Líneas con los clics esperados de 20 000 lectores simulados según la probabilidad de conocer el nombre del componente en cada nivel: el árbol por componente pasa de 3 clics con 100 por ciento a 7,88, 12,58, 17,49 y 22,05 con 80, 60, 40 y 20 por ciento, mientras el índice de tareas se queda entre 2,41 y 4,28.",
                      [("Árbol por componente (125 hojas)", [(p, v, fmt_es(v, 2), "t") for p, v in zip(ps, arbol)], "coral"),
                       ("Índice de tareas (25 títulos)", [(p, v, fmt_es(v, 2), "b") for p, v in zip(ps, indice)], "teal")],
                      x_label="Probabilidad de conocer el componente en cada nivel (%)", y_label="Clics esperados", x_ticks=[(p, f"{p} %") for p in ps], y_ticks=[0, 5, 10, 15, 20, 25],
                      note="El árbol por componente exige saber cómo se llama la pieza antes de saber cómo se arregla; cuando el lector sabe lo que quiere hacer pero no el nombre interno, cada nivel equivocado cuesta entrar y volver. Es un modelo: los 0,9 de reconocimiento de la tarea y los 5 hijos por nivel son supuestos del autor, no una medición de personas.",
                      note_kind="gold", foot=SINT)

def se205_duplicacion() -> Fig:
    items = [
        ("1 página dice el dato", 62.6, "teal", "62,6 % (teoría 61,4)"),
        ("2 páginas", 38.0, "gold", "38,0 % (37,7)"),
        ("3 páginas", 23.3, "gold", "23,3 % (23,2)"),
        ("4 páginas", 14.6, "coral", "14,6 % (14,2)"),
        ("6 páginas", 5.3, "coral", "5,3 % (5,4)"),
    ]
    return bars("Datos que siguen coherentes tras tres cambios, según cuántas páginas lo repiten",
                "Barras de 20 000 hechos simulados con tres cambios cada uno y una probabilidad de 0,85 de actualizar cada copia: con una sola página siguen coherentes el 62,6 por ciento, con dos el 38,0, con tres el 23,3, con cuatro el 14,6 y con seis el 5,3.",
                items, 1.0, "Cada copia añade una oportunidad de olvido: la coherencia cae como 0,85 elevado a 3k. Repetir el plazo de entrega en seis audiencias deja un 5 % de probabilidad de que todas digan lo mismo. La solución es una fuente única enlazada, no más disciplina.",
                label_w=240, width=980, note_kind="coral", foot=SINT)


def se205_legibilidad() -> Fig:
    items = [
        ("Estudiante (entender el descuento)", 93.1, "teal", "93,1 · 25 palabras, 2 frases"),
        ("Docente (cambiar el plazo)", 68.8, "teal", "68,8 · 16 palabras, 4 frases"),
        ("Mantenimiento (depurar el cálculo)", 58.6, "gold", "58,6 · 44 palabras, 1 frase"),
        ("Una sola página para todos", 41.1, "coral", "41,1 · 39 palabras, 1 frase"),
    ]
    return bars("Legibilidad de Fernández Huerta para cuatro textos sobre la misma regla",
                "Barras con el índice de Fernández Huerta de cuatro textos sobre la penalización por retraso: el escrito para estudiantes 93,1, el de docentes 68,8, el de mantenimiento 58,6 y el que intenta servir a todos 41,1; más alto es más fácil.",
                items, 0.45, "El mismo hecho se lee con facilidad muy distinta según la audiencia. El texto que mezcla tres audiencias en una frase larga queda el más difícil, no por técnico sino por intentar servir a todos. El índice es una fórmula sobre sílabas y frases; no mide si el lector entiende.",
                label_w=360, width=1060, note_kind="gold", foot="Cuatro textos escritos por el autor; sílabas contadas con una regla aproximada; idéntico en Windows y Ubuntu.")


# ---------------------------------------------------------------- SE-206
def se206_clasificador() -> Fig:
    items = [
        ("Párrafos puros bien clasificados", 100, "teal", "200 de 200"),
        ("Mezclas de dos tipos: acierta uno de los dos", 80, "gold", "240 de 300"),
        ("Mezclas de dos tipos: marcadas ambiguas", 20, "coral", "60 de 300"),
        ("Mezclas: reconoce a la vez los dos tipos", 0, "coral", "0 de 300"),
    ]
    return bars("Un clasificador léxico de los cuatro tipos de Diátaxis sobre párrafos puros y mezclados",
                "Barras: un clasificador por palabras clave acierta 200 de 200 párrafos puros de tutorial, how-to, referencia o explicación, pero ante 300 mezclas de dos tipos solo reconoce uno de los dos en 240 casos, declara ambiguas 60 y nunca reconoce los dos.",
                items, 3.2, "Los párrafos puros se escribieron con las mismas plantillas que usa el clasificador, por eso acierta todo: la cifra mide circularidad, no capacidad. Lo que sí muestra es que una página mezclada deja de tener un tipo claro, y una herramienta que debe elegir uno oculta el otro.",
                label_w=410, width=1060, note_kind="coral", foot=SINT)


def se206_palabras() -> Fig:
    items = [
        ("Página que mezcla: mediana", 540, "coral", "540 palabras antes de la primera instrucción"),
        ("Página que mezcla: percentil 90", 1020, "coral", "1 020 de 1 200"),
        ("Tipos separados: how-to propio", 0, "teal", "0 palabras de rodeo"),
    ]
    return bars("Palabras que lee quien busca los pasos antes de llegar a ellos (200 páginas de 1 200 palabras)",
                "Barras de 200 páginas simuladas de ocho secciones: cuando explicación, referencia, advertencias y pasos van mezclados en orden aleatorio, quien busca los pasos lee una mediana de 540 palabras y hasta 1 020 en el percentil 90 antes de llegar; en una página how-to separada, cero.",
                items, 0.5, "No es que la explicación sobre: es que no está donde se necesita ejecutar. Separar tipos no elimina el contenido, lo enlaza. El orden aleatorio es un supuesto; una página bien ordenada de un solo autor puede poner los pasos primero, y entonces el problema pasa a la explicación.",
                label_w=350, width=1060, note_kind="gold", foot=SINT)


def se206_tutorial() -> Fig:
    pasos = [f"Paso {i}" for i in range(1, 7)]
    patrones = [("Sin cambios", "......"), ("Se renombra crear a crear_tarea · AttributeError", "XXX..X"), ("El cálculo de días redondea hacia abajo · AssertionError", "...XX."),
                ("entregar exige un cuarto argumento · TypeError", ".XX..X")]
    return heatmap("Seis pasos de un tutorial ejecutados contra cuatro versiones de la biblioteca",
                   "Mapa de calor de un tutorial de seis pasos ejecutado contra cuatro versiones: sin cambios pasan los seis, renombrar una función hace fallar los pasos 1, 2, 3 y 6, redondear días hacia abajo los pasos 4 y 5 y añadir un argumento obligatorio los pasos 2, 3 y 6.",
                   [n for n, _ in patrones], pasos, [[1 if c == "X" else 0 for c in p] for _, p in patrones], unit="falla", scale="coral", vmin=0, vmax=1,
                   cell_fmt=lambda v: "falla" if v else "pasa", label_w=330,
                   note="Solo el primer fallo informa; los demás son consecuencia (con el renombrado, el paso 1 falla y los 2 y 3 fallan por arrastre; con el redondeo fallan las dos comprobaciones de nota; con el cuarto argumento, las dos llamadas y el recuento). Un tutorial ejecutable convierte la deriva en un fallo de integración continua, pero solo detecta lo que sus pasos ejercen: un cambio que ningún paso comprueba pasa sin ruido.",
                   note_kind="teal", foot=SINT)

# ---------------------------------------------------------------- SE-207
def se207_embudo() -> Fig:
    return grouped_bars("Quién llega al primer éxito según el número de pasos y la probabilidad de fallo por paso",
                        "Barras agrupadas con el porcentaje de 40 000 recorridos simulados que llegan al primer éxito frente al teórico (1 − p)ⁿ: con 4, 6 y 10 pasos y 3 por ciento de fallo por paso llegan 88,9, 82,9 y 73,6 por ciento; con 6 por ciento, 69,2 con 6 pasos y 53,9 con 10; el simulado y el teórico casi coinciden.",
                        ["4 pasos · 3 %", "6 pasos · 3 %", "10 pasos · 3 %", "6 pasos · 6 %", "10 pasos · 6 %"],
                        [("Simulado", [88.9, 82.9, 73.6, 69.2, 53.9], "teal"), ("Teórico (1 − p)ⁿ", [88.5, 83.3, 73.7, 69.0, 53.9], "grey")],
                        unit="% que llega al primer éxito", decimals=1, ticks=[0, 20, 40, 60, 80, 100],
                        note="Quitar pasos pesa tanto como mejorar cada uno: pasar de 10 a 6 pasos con 3 % de fallo recupera 9 puntos. Los porcentajes de fallo son supuestos, no mediciones de lectores; la forma multiplicativa es lo que se puede afirmar.",
                        note_kind="gold", foot=SINT)

def se207_deriva() -> Fig:
    items = [
        ("Se renombra una opción", 100, "teal", "125 de 125 detectadas"),
        ("Se elimina una opción", 100, "teal", "135 de 135 detectadas"),
        ("La opción cambia de significado", 0, "coral", "0 de 140 detectadas"),
    ]
    return bars("Un detector compara las opciones del README con las del analizador de argumentos (400 mutaciones)",
                "Barras: el detector que compara las opciones escritas en el README con las reales detecta 125 de 125 renombrados y 135 de 135 eliminaciones, pero 0 de 140 cambios en los que la opción conserva su nombre y cambia de significado.",
                items, 4.6, "El detector es barato y atrapa lo que deja huella en la interfaz. No ve que `--plazo` pase de horas a días: ese cambio solo lo detecta ejecutar el ejemplo y comprobar su salida.",
                label_w=290, width=980, note_kind="gold", foot=SINT)


def se207_omision() -> Fig:
    return case_cards("Omitir un paso del README: dónde aparece el primer fallo",
                      "Seis tarjetas de un README de seis pasos ejecutado omitiendo cada vez uno: omitir los pasos 1 a 4 hace fallar uno o dos pasos después; omitir los pasos 5 o 6, los de comprobación, no falla en ningún paso.",
                      [("Omitir 1. Instalar Python", "Falla en el paso 2, a 1 paso: «python: orden no encontrada»", "El error aparece junto a la causa.", "gold"),
                       ("Omitir 2. Crear el entorno", "Falla en el paso 3, a 1 paso: «no existe .venv»", "El error aparece junto a la causa.", "gold"),
                       ("Omitir 3. Activar el entorno", "Falla en el paso 5, a 2 pasos: «entregas: orden no reconocida»; el paquete quedó fuera del entorno", "El error aparece lejos de la causa.", "coral"),
                       ("Omitir 4. Instalar el paquete", "Falla en el paso 5, a 1 paso: «entregas: orden no reconocida»", "El error aparece junto a la causa.", "gold"),
                       ("Omitir 5. Comprobar la versión", "No falla en ningún paso: el README «funciona»", "No se pierde nada, salvo la evidencia del primer éxito.", "coral"),
                       ("Omitir 6. Ejecutar el ejemplo", "No falla en ningún paso: el README «funciona»", "No se aprende nada.", "coral")],
                      note="Los pasos de comprobación son los únicos que pueden desaparecer sin que nada falle, y son los que dan al lector la evidencia del primer éxito. Omitir la activación es el caso peor: el error aparece dos pasos después y lejos de la causa. Máquina de estados de seis reglas escrita por el autor, no una instalación real.",
                      note_kind="coral", foot=SINT)

# ---------------------------------------------------------------- SE-208
def se208_linter() -> Fig:
    return stacked_bars("Un linter de ADR sobre 300 registros con defectos conocidos",
                        "Barras horizontales apiladas con lo que detecta un linter de ADR en 300 registros sintéticos: ve las 54 secciones ausentes y las 45 fechas ilegibles, pero ninguna de las 54 alternativas vacías, 60 consecuencias vacías ni 46 contextos sin razón, y no marca ninguno de los 41 registros correctos.",
                        ["Falta una sección", "Fecha ilegible («ayer»)", "Alternativas: «Ninguna.»", "Consecuencias: «Ninguna.»", "Contexto: «Nada especial.»", "ADR correcto"],
                        [("Detectados", [54, 45, 0, 0, 0, 0], "teal"), ("No detectados", [0, 0, 54, 60, 46, 0], "coral"), ("Correctos sin falsa alarma", [0, 0, 0, 0, 0, 41], "grey")],
                        unit="registros", horizontal=True, label_w=240,
                        note="El linter comprueba forma: presencia, formato, vocabulario. Un ADR con «Alternativas: Ninguna.» tiene todas las secciones y no contiene ninguna decisión defendible. La calidad del razonamiento la revisan personas, con una pregunta concreta: ¿qué se descartó y por qué?",
                        note_kind="coral", foot=SINT)

def se208_grafo() -> Fig:
    items = [
        ("Enlace a un ADR inexistente", 45, "teal", "45 de 45"),
        ("Dos ADR sustituyen al mismo", 41, "teal", "41 de 41"),
        ("Un ADR se sustituye a sí mismo (ciclo)", 39, "teal", "39 de 39"),
        ("El sustituido sigue «vigente»", 39, "teal", "39 de 39"),
        ("Sustituye al ADR equivocado", 0, "coral", "0 de 36"),
    ]
    return bars("Integridad del registro de decisiones: cinco mutaciones del grafo de sustituciones",
                "Barras de 200 registros de 40 ADR con una mutación cada uno: la comprobación estructural detecta 45 de 45 enlaces rotos, 41 de 41 doble sustitución, 39 de 39 ciclos y 39 de 39 estados incoherentes, pero 0 de 36 casos en los que un ADR sustituye a otro estructuralmente válido pero equivocado.",
                items, 0.9, "Los 200 grafos limpios dieron 0 falsas alarmas. Lo que el grafo no puede saber es si «ADR-31 sustituye a ADR-12» dice la verdad: una sustitución mal dirigida es un grafo perfecto con la historia equivocada.",
                label_w=370, width=1000, note_kind="gold", foot=SINT)


def se208_caducidad() -> Fig:
    return heatmap("Probabilidad de que al menos una suposición de un ADR haya cambiado",
                   "Mapa de calor con la probabilidad de que cambie al menos una suposición según cuántas lleva el ADR y la tasa anual: con 2 suposiciones y 10 por ciento anual es 9,9 por ciento a 6 meses, 18,4 a 12 y 34,9 a 24; con 6 suposiciones y 25 por ciento anual sube a 57,8, 82,1 y 96,8.",
                   ["2 suposiciones", "4 suposiciones", "6 suposiciones"], ["10 %/año · 6 m", "10 %/año · 12 m", "10 %/año · 24 m", "25 %/año · 6 m", "25 %/año · 12 m", "25 %/año · 24 m"],
                   [[9.9, 18.4, 34.9, 24.9, 43.9, 69.1], [18.4, 34.4, 57.4, 44.1, 68.1, 90.2], [26.9, 47.0, 71.6, 57.8, 82.1, 96.8]],
                   unit="% de ADR con alguna suposición cambiada", scale="gold", vmin=0, vmax=100, suffix=" %", decimals=1, label_w=150,
                   note="Cuantas más suposiciones lleva una decisión, antes pierde vigencia alguna. Por eso un ADR útil enumera sus suposiciones y fija una fecha de revisión. Las tasas de cambio de 10 % y 25 % al año son supuestos del autor, no medidas sobre proyectos reales (20 000 simulaciones por celda).",
                   note_kind="gold", foot=SINT)

# ---------------------------------------------------------------- SE-209
def se209_cruces() -> Fig:
    return grouped_bars("Cruces de aristas en un diagrama de cuatro capas: orden aleatorio frente a orden por baricentro",
                        "Barras agrupadas con la media de cruces de 150 grafos por tamaño: con 4 nodos por capa el orden aleatorio produce 27,1 cruces y el orden por baricentro 11,4; con 8 nodos 149,6 y 55,5; con 16 nodos 672,9 y 240,3, una reducción de 58 a 64 por ciento.",
                        ["4 por capa · 24 aristas", "8 por capa · 48 aristas", "16 por capa · 96 aristas"],
                        [("Orden aleatorio", [27.1, 149.6, 672.9], "coral"), ("Con baricentro (4 pasadas)", [11.4, 55.5, 240.3], "teal")],
                        unit="cruces de aristas", decimals=1,
                        note="La reducción es de −58 %, −63 % y −64 %. Cuadruplicar el tamaño multiplica los cruces por 25: un diagrama que cabe en una pantalla con 12 nodos deja de leerse con 48. Ordenar las capas ayuda mucho y no elimina el problema; la solución de fondo es dibujar menos cosas por diagrama.",
                        note_kind="gold", foot=SINT)

def se209_estable() -> Fig:
    return grouped_bars("Diff de un diagrama generado: ruido entre ejecuciones y cambio real",
                        "Barras agrupadas con las líneas distintas entre salidas Mermaid de un modelo de 12 servicios y 18 dependencias: si el generador recorre un conjunto, dos ejecuciones del mismo modelo difieren en 42 líneas y renombrar un servicio produce 10; si ordena, 0 y 8.",
                        ["Dos ejecuciones del mismo modelo", "Al renombrar un servicio"],
                        [("Aristas en el orden de un conjunto", [42, 10], "coral"), ("Aristas ordenadas", [0, 8], "teal")],
                        unit="líneas de diff",
                        note="Con orden no determinista, una revisión no distingue el cambio real del ruido: 42 líneas de diff sin que cambie nada. El renombrado real cambia 4 líneas (el nodo y sus 3 dependencias), que el diff cuenta como 4 eliminadas y 4 añadidas: 8.",
                        note_kind="coral", foot="Dos ejecuciones con PYTHONHASHSEED=1 y 2; idéntico en Windows y Ubuntu.")

def se209_importaciones() -> Fig:
    return grouped_bars("Diagrama de dependencias frente a lo que importa el código de diez módulos",
                        "Barras horizontales sobre un paquete sintético de diez módulos: de 16 dependencias reales el análisis estático ve 14 y 13 si solo mira el nivel de módulo, 2 quedan invisibles por ser dinámicas, y el diagrama declarado tiene 2 aristas de más y le faltan 4.",
                        ["Aristas reales del código", "Las ve un análisis estático de import", "Solo las de nivel de módulo", "Invisibles para el análisis", "Sobran en el diagrama", "Faltan en el diagrama"],
                        [("Dependencias", [16, 14, 13, 2, 2, 4], "teal")],
                        unit="dependencias", horizontal=True, label_w=300,
                        note="Las 16 reales son 12 declaradas + 3 añadidas + 2 dinámicas + 1 diferida − 2 retiradas. Las 14 incluyen la importación dentro de una función; la diferida queda fuera de las 13; las 2 invisibles usan importlib.import_module con el nombre en texto; las 2 que sobran son dependencias retiradas del código y las 4 que faltan, añadidas sin actualizar. Comparar el diagrama con el código convierte «creo que está al día» en una lista de diferencias concretas; el análisis tiene un techo: lo que se decide en tiempo de ejecución no deja huella en el árbol sintáctico.",
                        note_kind="teal", foot=SINT)

# ---------------------------------------------------------------- SE-210
def se210_ejemplos() -> Fig:
    return grouped_bars("Diez ejemplos ejecutables de una API frente a cinco cambios del proveedor",
                        "Barras con los ejemplos que fallan de diez ejecutados contra una API tras cada cambio: sin cambios 0, con el campo renombrado 4, con el estado 201 cambiado a 200 fallan 2, con el id pasado a texto 2 y con la ruta movida 2; una comparación de nombres de campos solo detecta el renombrado.",
                        ["Sin cambios", "Campo renombrado (horas_retraso) · lo ve la comparación de nombres", "Estado 201 pasa a 200", "El id pasa a texto", "Ruta /penalizacion movida"],
                        [("Ejemplos que fallan (de 10)", [0, 4, 2, 2, 2], "teal")],
                        unit="ejemplos que fallan de 10", horizontal=True, label_w=330, ticks=[0, 2, 4, 6, 8, 10],
                        note="Solo el renombrado lo detecta una comparación de nombres de campo; los otros cuatro cambios solo los ve ejecutar los ejemplos. Ejecutar los ejemplos de la documentación detecta cambios de estado, de tipo y de ruta que una lista de campos no ve. Cada cambio deja un patrón distinto de ejemplos rotos, lo que ayuda a localizarlo. Un ejemplo que no se ejecuta es una promesa sin comprobar.",
                        note_kind="teal", foot=SINT)

def se210_docstrings() -> Fig:
    return grouped_bars("Documentación de la biblioteca estándar de Python 3.12: lo que dice cada función pública",
                        "Barras agrupadas con seis módulos de la biblioteca estándar: de las funciones y clases públicas casi todas tienen docstring (json 4 de 5, csv 5 de 7, argparse 12 de 12, statistics 21 de 21, shutil 27 de 28, re 16 de 17) y de los parámetros de funciones se nombran en la documentación 28 de 36 en json, 27 de 32 en statistics, 59 de 66 en shutil y 20 de 34 en re.",
                        ["json", "csv", "argparse", "statistics", "shutil", "re"],
                        [("Públicos", [5, 7, 12, 21, 28, 17], "grey"), ("Con docstring", [4, 5, 12, 21, 27, 16], "teal"), ("Parámetros", [36, 0, 0, 32, 66, 34], "gold"), ("Nombrados en el docstring", [28, 0, 0, 27, 59, 20], "coral")],
                        unit="funciones, clases o parámetros",
                        note="En los diez módulos medidos: 123 públicos, 118 con docstring, 181 parámetros y 144 nombrados (80 %). Tener docstring no es documentar los parámetros: en csv y argparse las clases tienen texto pero el recuento de parámetros de funciones es cero porque son clases; en re uno de cada tres parámetros no se nombra. Medimos presencia, no calidad.",
                        note_kind="gold", foot="Medido con inspect en CPython 3.12.9 (Windows) y 3.12.3 (Ubuntu); idéntico.")

def se210_codigos() -> Fig:
    items = [
        ("404 (documentado)", 208, "teal", "208"),
        ("405 (no documentado)", 207, "coral", "207"),
        ("400 (no documentado)", 64, "coral", "64"),
        ("200 (documentado)", 58, "teal", "58"),
        ("413 (no documentado)", 38, "coral", "38"),
        ("422 (no documentado)", 21, "coral", "21"),
        ("201 (documentado)", 4, "teal", "4"),
    ]
    return bars("600 peticiones de prueba a un servicio local: códigos devueltos frente a códigos documentados",
                "Barras de 600 peticiones aleatorias a un servidor local que documenta solo 200, 201 y 404: 330 respuestas, el 55 por ciento, llevan códigos no documentados: 405 con 207, 400 con 64, 413 con 38 y 422 con 21.",
                items, 1.6, "La documentación cubre los caminos felices y deja sin explicar más de la mitad de lo que ve un cliente que se equivoca. El 413 se produjo al enviar cuerpos de más de 200 bytes; en Windows el servidor debe leer el cuerpo antes de responder o el cliente ve la conexión abortada.",
                label_w=240, width=1000, note_kind="coral", foot="Servidor y cliente locales en 127.0.0.1; semilla fija; mismos recuentos en Windows y Ubuntu.")


FIGURES = {
    "se-205-clics-hasta-la-pagina-correcta.svg": se205_navegacion,
    "se-205-coherencia-segun-copias.svg": se205_duplicacion,
    "se-205-legibilidad-por-audiencia.svg": se205_legibilidad,
    "se-206-clasificar-paginas-mezcladas.svg": se206_clasificador,
    "se-206-palabras-hasta-los-pasos.svg": se206_palabras,
    "se-206-tutorial-ejecutable.svg": se206_tutorial,
    "se-207-embudo-de-pasos.svg": se207_embudo,
    "se-207-deriva-readme-y-cli.svg": se207_deriva,
    "se-207-paso-omitido.svg": se207_omision,
    "se-208-linter-de-adr.svg": se208_linter,
    "se-208-grafo-de-sustituciones.svg": se208_grafo,
    "se-208-caducidad-de-suposiciones.svg": se208_caducidad,
    "se-209-cruces-de-aristas.svg": se209_cruces,
    "se-209-diff-de-diagrama-generado.svg": se209_estable,
    "se-209-diagrama-frente-al-codigo.svg": se209_importaciones,
    "se-210-ejemplos-ejecutables-de-api.svg": se210_ejemplos,
    "se-210-docstrings-de-la-biblioteca-estandar.svg": se210_docstrings,
    "se-210-codigos-observados-y-documentados.svg": se210_codigos,
}
