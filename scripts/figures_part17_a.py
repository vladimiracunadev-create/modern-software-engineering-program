"""Figures for SE-205 to SE-210 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time is shown)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-205
def se205_navegacion() -> Fig:
    rows = [["100 %", "3,0", "2,41"], ["80 %", "7,88", "2,93"], ["60 %", "12,58", "3,33"], ["40 %", "17,49", "3,84"], ["20 %", "22,05", "4,28"]]
    return tab("Clics esperados hasta la página correcta: árbol por componente frente a índice de tareas",
               "Tabla de un modelo con 20 000 lectores simulados: si el lector conoce el nombre del componente en el 100 por ciento de los niveles necesita 3 clics, con 80 por ciento 7,88, con 60 por ciento 12,58, con 40 por ciento 17,49 y con 20 por ciento 22,05; un índice de tareas necesita entre 2,41 y 4,28 clics.",
               ["Prob. de conocer el componente en cada nivel", "Árbol por componente (125 hojas)", "Índice de tareas (25 títulos)"], rows, [330, 300, 270], row_h=40, size=13,
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
    rows = [["Sin cambios", "......", "—", "Los seis pasos pasan"],
            ["Se renombra crear a crear_tarea", "XXX..X", "AttributeError", "El paso 1 falla; los 2 y 3 fallan por arrastre"],
            ["El cálculo de días redondea hacia abajo", "...XX.", "AssertionError", "Fallan las dos comprobaciones de nota"],
            ["entregar exige un cuarto argumento", ".XX..X", "TypeError", "Fallan las dos llamadas y el recuento"]]
    return tab("Seis pasos de un tutorial ejecutados contra cuatro versiones de la biblioteca",
               "Tabla de un tutorial de seis pasos ejecutado contra cuatro versiones: sin cambios pasan los seis, renombrar una función hace fallar tres pasos, redondear días hacia abajo hace fallar dos y añadir un argumento obligatorio hace fallar tres.",
               ["Versión de la biblioteca", "Pasos (X = falla)", "Primer error", "Lectura"], rows, [310, 170, 170, 330], row_h=52, size=12,
               note="Solo el primer fallo informa; los demás son consecuencia. Un tutorial ejecutable convierte la deriva en un fallo de integración continua, pero solo detecta lo que sus pasos ejercen: un cambio de comportamiento que ningún paso comprueba pasa sin ruido.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-207
def se207_embudo() -> Fig:
    rows = [["4 pasos", "3 %", "88,9 %", "88,5 %"], ["6 pasos", "3 %", "82,9 %", "83,3 %"], ["10 pasos", "3 %", "73,6 %", "73,7 %"],
            ["6 pasos", "6 %", "69,2 %", "69,0 %"], ["10 pasos", "6 %", "53,9 %", "53,9 %"]]
    return tab("Quién llega al primer éxito según el número de pasos y la probabilidad de fallo por paso",
               "Tabla de 40 000 recorridos simulados: con 4 pasos y 3 por ciento de fallo por paso llega al éxito el 88,9 por ciento, con 6 pasos 82,9, con 10 pasos 73,6; con 6 por ciento de fallo por paso llegan 69,2 por ciento con 6 pasos y 53,9 con 10.",
               ["Pasos del README", "Fallo por paso", "Simulado", "Teórico (1 − p)ⁿ"], rows, [210, 230, 230, 230], row_h=40, size=13,
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
    rows = [["1. Instalar Python", "Paso 2", "1", "python: orden no encontrada"],
            ["2. Crear el entorno", "Paso 3", "1", "no existe .venv"],
            ["3. Activar el entorno", "Paso 5", "2", "entregas: orden no reconocida; el paquete quedó fuera del entorno"],
            ["4. Instalar el paquete", "Paso 5", "1", "entregas: orden no reconocida"],
            ["5. Comprobar la versión", "ninguno", "—", "El README «funciona»: no se pierde nada"],
            ["6. Ejecutar el ejemplo", "ninguno", "—", "El README «funciona»: no se aprende nada"]]
    return tab("Omitir un paso del README: dónde aparece el primer fallo",
               "Tabla de un README de seis pasos ejecutado seis veces, omitiendo cada vez uno: omitir los pasos 1 a 4 hace fallar entre 1 y 2 pasos después; omitir los pasos 5 o 6, los de comprobación, no falla en ningún paso.",
               ["Paso omitido", "Primer fallo", "Distancia", "Mensaje que vería quien lo siga"], rows, [260, 150, 120, 420], row_h=52, size=12,
               note="Los pasos de comprobación son los únicos que pueden desaparecer sin que nada falle, y son los que dan al lector la evidencia del primer éxito. Omitir la activación es el caso peor: el error aparece dos pasos después y lejos de la causa. Máquina de estados de seis reglas escrita por el autor, no una instalación real.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-208
def se208_linter() -> Fig:
    rows = [["Falta una sección", "54", "54", "Sí"], ["Fecha ilegible («ayer»)", "45", "45", "Sí"],
            ["Alternativas: «Ninguna.»", "54", "0", "No"], ["Consecuencias: «Ninguna.»", "60", "0", "No"],
            ["Contexto: «Nada especial.»", "46", "0", "No"], ["ADR correcto", "41", "0", "Sin falsas alarmas"]]
    return tab("Un linter de ADR sobre 300 registros con defectos conocidos",
               "Tabla de un linter de ADR aplicado a 300 registros sintéticos: detecta las 54 secciones ausentes y las 45 fechas ilegibles, pero ninguna de las 54 alternativas vacías, 60 consecuencias vacías ni 46 contextos sin razón, y no da falsas alarmas sobre los 41 registros correctos.",
               ["Defecto introducido", "Registros", "Detectados", "¿Lo ve el linter?"], rows, [380, 130, 150, 250], row_h=42, size=13,
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
    rows = [["2", "9,9 %", "18,4 %", "34,9 %", "24,9 %", "43,9 %", "69,1 %"],
            ["4", "18,4 %", "34,4 %", "57,4 %", "44,1 %", "68,1 %", "90,2 %"],
            ["6", "26,9 %", "47,0 %", "71,6 %", "57,8 %", "82,1 %", "96,8 %"]]
    return tab("Probabilidad de que al menos una suposición de un ADR haya cambiado",
               "Tabla de 20 000 simulaciones por celda: con 2 suposiciones y un cambio anual del 10 por ciento, la probabilidad de que alguna haya cambiado es 9,9 por ciento a 6 meses, 18,4 a 12 y 34,9 a 24; con 6 suposiciones y 25 por ciento anual sube a 57,8, 82,1 y 96,8.",
               ["Suposiciones del ADR", "10 %/año · 6 m", "12 m", "24 m", "25 %/año · 6 m", "12 m", "24 m"], rows, [180, 160, 130, 130, 160, 130, 130], row_h=44, size=12,
               note="Cuantas más suposiciones lleva una decisión, antes pierde vigencia alguna. Por eso un ADR útil enumera sus suposiciones y fija una fecha de revisión. Las tasas de cambio de 10 % y 25 % al año son supuestos del autor, no medidas sobre proyectos reales.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-209
def se209_cruces() -> Fig:
    rows = [["4 por capa · 24 aristas", "27,1", "11,4", "−58 %"], ["8 por capa · 48 aristas", "149,6", "55,5", "−63 %"], ["16 por capa · 96 aristas", "672,9", "240,3", "−64 %"]]
    return tab("Cruces de aristas en un diagrama de cuatro capas: orden aleatorio frente a orden por baricentro",
               "Tabla con la media de 150 grafos por tamaño: con 4 nodos por capa el orden aleatorio produce 27,1 cruces y el orden por baricentro 11,4; con 8 nodos 149,6 y 55,5; con 16 nodos 672,9 y 240,3.",
               ["Tamaño del grafo", "Cruces con orden aleatorio", "Con baricentro (4 pasadas)", "Reducción"], rows, [290, 250, 250, 120], row_h=44, size=13,
               note="Cuadruplicar el tamaño multiplica los cruces por 25: un diagrama que cabe en una pantalla con 12 nodos deja de leerse con 48. Ordenar las capas ayuda mucho y no elimina el problema; la solución de fondo es dibujar menos cosas por diagrama.",
               note_kind="gold", foot=SINT)


def se209_estable() -> Fig:
    rows = [["Aristas en el orden de un conjunto", "42", "10"], ["Aristas ordenadas", "0", "8"]]
    return tab("Diff de un diagrama generado: ruido entre ejecuciones y cambio real",
               "Tabla de líneas distintas entre salidas Mermaid de un modelo de 12 servicios y 18 dependencias: si el generador recorre un conjunto, dos ejecuciones del mismo modelo difieren en 42 líneas y renombrar un servicio produce 10; si ordena, 0 y 8.",
               ["Generador", "Líneas de diff entre dos ejecuciones del mismo modelo", "Líneas de diff al renombrar un servicio"], rows, [400, 280, 270], row_h=54, size=13,
               note="Con orden no determinista, una revisión no distingue el cambio real del ruido: 42 líneas de diff sin que cambie nada. El renombrado real cambia 4 líneas (el nodo y sus 3 dependencias), que el diff cuenta como 4 eliminadas y 4 añadidas: 8.",
               note_kind="coral", foot="Dos ejecuciones con PYTHONHASHSEED=1 y 2; idéntico en Windows y Ubuntu.")


def se209_importaciones() -> Fig:
    rows = [["Aristas reales del código", "16", "12 declaradas + 3 añadidas + 2 dinámicas + 1 diferida − 2 retiradas"],
            ["Las ve un análisis estático de `import`", "14", "Incluye la importación dentro de una función"],
            ["Solo las de nivel de módulo", "13", "La importación diferida queda fuera"],
            ["Invisibles para el análisis", "2", "`importlib.import_module` con nombre en texto"],
            ["Sobran en el diagrama", "2", "Dependencias retiradas del código"],
            ["Faltan en el diagrama", "4", "Dependencias añadidas sin actualizar"]]
    return tab("Diagrama de dependencias frente a lo que importa el código de diez módulos",
               "Tabla de un paquete sintético de diez módulos: de 16 dependencias reales el análisis estático ve 14 y 13 si solo mira el nivel de módulo; 2 son dinámicas y quedan invisibles; el diagrama declarado tiene 2 aristas de más y le faltan 4.",
               ["Conteo", "Valor", "Qué incluye"], rows, [370, 90, 480], row_h=48, size=12,
               note="Comparar el diagrama con el código convierte «creo que está al día» en una lista de diferencias concretas. El análisis tiene un techo: lo que se decide en tiempo de ejecución no deja huella en el árbol sintáctico, y esas aristas hay que declararlas en el diagrama con otra fuente.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-210
def se210_ejemplos() -> Fig:
    rows = [["Sin cambios", "0 de 10", "No"], ["Campo renombrado (horas_retraso)", "4 de 10", "Sí"], ["Estado 201 pasa a 200", "2 de 10", "No"],
            ["El id pasa a texto", "2 de 10", "No"], ["Ruta /penalizacion movida", "2 de 10", "No"]]
    return tab("Diez ejemplos ejecutables de una API frente a cinco cambios del proveedor",
               "Tabla de diez ejemplos de uso ejecutados contra una API en proceso: sin cambios fallan 0, con el campo renombrado fallan 4, con el estado 201 cambiado a 200 fallan 2, con el id pasado a texto fallan 2 y con la ruta movida fallan 2; una comparación de nombres de campos solo detecta el renombrado.",
               ["Cambio en la API", "Ejemplos que fallan", "¿Lo ve una comparación de nombres de campo?"], rows, [400, 230, 320], row_h=42, size=13,
               note="Ejecutar los ejemplos de la documentación detecta cambios de estado, de tipo y de ruta que una lista de campos no ve. Cada cambio deja un patrón distinto de ejemplos rotos, lo que ayuda a localizarlo. Un ejemplo que no se ejecuta es una promesa sin comprobar.",
               note_kind="teal", foot=SINT)


def se210_docstrings() -> Fig:
    rows = [["json", "5", "4", "36", "28"], ["csv", "7", "5", "0", "0"], ["argparse", "12", "12", "0", "0"], ["statistics", "21", "21", "32", "27"],
            ["shutil", "28", "27", "66", "59"], ["re", "17", "16", "34", "20"], ["Diez módulos", "123", "118", "181", "144"]]
    return tab("Documentación de la biblioteca estándar de Python 3.12: lo que dice cada función pública",
               "Tabla de 10 módulos de la biblioteca estándar de Python 3.12: de 123 funciones y clases públicas 118 tienen docstring, y de 181 parámetros de funciones 144 se nombran en la documentación, el 80 por ciento.",
               ["Módulo", "Públicos", "Con docstring", "Parámetros", "Nombrados en el docstring"], rows, [230, 140, 190, 170, 220], row_h=38, size=13,
               note="Tener docstring no es documentar los parámetros: en csv y argparse las clases tienen texto pero el recuento de parámetros de funciones es cero porque son clases; en re uno de cada tres parámetros no se nombra. Medimos presencia, no calidad.",
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
