"""Figures for SE-169 to SE-174 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2)."


def auto_bars(title, desc, items, note, label_w=330, width=1000, note_kind="gold", foot=SINT, headroom=230):
    top = max(v for _, v, _, _ in items) or 1
    scale = (width - label_w - headroom) / top
    return bars(title, desc, items, scale, note, label_w=label_w, width=width, note_kind=note_kind, foot=foot)


# ---------------------------------------------------------------- SE-169
def se169_klm() -> Fig:
    items = [
        ("A: formulario de nueve campos, ratón y teclado", 50.7, "coral", "50,7 s"),
        ("B: tres campos, ratón y teclado", 18.6, "gold", "18,6 s"),
        ("B con tres pausas mentales de más", 22.7, "gold", "22,7 s"),
        ("C: tres campos, solo teclado con Tab", 13.4, "teal", "13,4 s"),
    ]
    return auto_bars("Tiempo estimado de entregar una tarea con tres diseños (modelo de nivel de teclado)",
                     "Barras: con los tiempos estándar de Card, Moran y Newell, un formulario de nueve campos tarda 50,7 segundos, uno de tres campos con ratón 18,6, el mismo con tres pausas mentales de más 22,7 y uno de tres campos solo con teclado 13,4.",
                     items, "Quitar seis campos ahorra 32 s; tres dudas sobre qué escribir cuestan 4 s. El modelo supone una persona experta que no se equivoca: no mide aprendizaje, error ni lectura, y los tiempos de cada operador son valores medios de la literatura.",
                     label_w=440, width=1080)


def se169_promedio() -> Fig:
    items = [
        ("1 dimensión", 1542, "teal", "1 542"),
        ("2 dimensiones", 473, "gold", "473"),
        ("3 dimensiones", 165, "gold", "165"),
        ("5 dimensiones", 13, "coral", "13"),
        ("10 dimensiones", 0, "coral", "0"),
    ]
    return auto_bars("Personas de 5 000 que caen en la banda central del 30 % en todas las dimensiones",
                     "Barras: de 5 000 personas simuladas con dimensiones correlacionadas 0,3, 1 542 están en la banda central de una dimensión, 473 de dos, 165 de tres, 13 de cinco y ninguna de diez.",
                     items, "Diseñar para la persona promedio sirve a casi nadie en cuanto cuentan varias dimensiones (visión, destreza, conectividad, idioma, dispositivo). Con la correlación subida a 0,5 el resultado sube a 24 con cinco dimensiones y sigue en 0 con diez.",
                     label_w=250, width=900)


def se169_embudo() -> Fig:
    items = [
        ("Etapa 1: abrir la tarea", 30, "teal", "30"),
        ("Etapa 2: elegir el archivo", 49, "teal", "49"),
        ("Etapa 3: completar el formulario", 92, "gold", "92"),
        ("Etapa 4: subir el archivo", 315, "coral", "315"),
        ("Etapa 5: confirmar", 36, "teal", "36"),
        ("Etapa 6: ver el recibo", 19, "teal", "19"),
    ]
    return auto_bars("Personas que se pierden en cada etapa de 1 000 que empiezan (tasas supuestas)",
                     "Barras: de 1 000 personas que empiezan, se pierden 30, 49, 92, 315, 36 y 19 en las seis etapas; completan 478. Mejorar solo la cuarta etapa 10 puntos sube la tasa de completar de 0,459 a 0,533; mejorar las seis 2 puntos la sube a 0,526.",
                     items, "Las tasas por etapa son un supuesto del autor, no una medición. Lo que muestra el cálculo es la forma: una sola etapa mala domina, y repartir esfuerzo en todas rinde menos que atacarla. Mejorar 2 puntos la primera etapa solo suma 0,0095.",
                     label_w=360, width=980)


# ---------------------------------------------------------------- SE-170
def se170_anchura() -> Fig:
    rows = [
        ["2", "12", "14,6 s", "0,368", "39,7 s"],
        ["4", "6", "8,2 s", "0,606", "13,5 s"],
        ["8", "4", "6,1 s", "0,716", "8,6 s"],
        ["16", "3", "5,2 s", "0,779", "6,6 s"],
        ["64", "2", "4,2 s", "0,846", "5,0 s"],
        ["4 096", "1", "3,3 s", "0,920", "3,6 s"],
    ]
    return tab("Menú de 4 096 destinos: anchura frente a profundidad",
               "Tabla con seis anchuras de menú: con 2 opciones por nivel hay 12 niveles, 14,6 s y 0,368 de éxito; con 8, cuatro niveles, 6,1 s y 0,716; con 64, dos niveles, 4,2 s y 0,846; una sola lista de 4 096 llega a 3,3 s y 0,92 bajo el supuesto de error constante por nivel.",
               ["Opciones por nivel", "Niveles", "Tiempo", "Éxito", "Tiempo esperado por éxito"], rows, [220, 150, 190, 170, 290], row_h=36, size=13,
               note="Modelo: cada nivel cuesta un clic más 0,2·log2(opciones+1) s y se acierta con probabilidad 0,92; ambos valores son supuestos. El modelo ignora que 4 096 opciones en una lista no se pueden leer: el error por nivel sube con la anchura, y ese es el dato que habría que medir con árboles reales.",
               note_kind="gold", foot=SINT)


def se170_cards() -> Fig:
    items = [
        ("5 participantes", 67.2, "coral", "0,67 (mínimo 0,47)"),
        ("10 participantes", 80.6, "gold", "0,81 (mínimo 0,70)"),
        ("15 participantes", 86.3, "gold", "0,86 (mínimo 0,77)"),
        ("20 participantes", 89.5, "gold", "0,90 (mínimo 0,84)"),
        ("30 participantes", 92.9, "teal", "0,93 (mínimo 0,90)"),
    ]
    return auto_bars("Correlación entre dos grupos independientes que ordenan 24 tarjetas en 4 categorías",
                     "Barras: la correlación entre las matrices de agrupación de dos grupos independientes es 0,67 con 5 participantes por grupo, 0,81 con 10, 0,86 con 15, 0,90 con 20 y 0,93 con 30; con 5 el peor caso de 100 repeticiones fue 0,47.",
                     items, "El acuerdo mejora con rendimientos decrecientes, y con pocas personas dos grupos pueden dar estructuras bastante distintas. Los participantes simulados agrupan según una estructura verdadera con 25 % de ruido: ese ruido y esa estructura única son supuestos.",
                     label_w=260, width=960, headroom=300)


def se170_menu() -> Fig:
    rows = [
        ["Con menú global en cada página", "Desde la portada: 120 de 120", "4", "17 / 47 / 41 / 14 páginas a 1 / 2 / 3 / 4 clics"],
        ["Sin menú global (solo enlaces de contenido)", "Desde la portada: 120 de 120", "9", "9 / 23 / 20 / 20 / 16 / 10 / 7 / 9 / 5 páginas a 1 a 9 clics"],
        ["Desde una página interna, con enlace a la portada", "120 de 120", "5", "4 / 18 / 46 / 38 / 13 páginas a 1 a 5 clics"],
        ["Desde la misma página, sin enlace a la portada", "16 de 120", "6", "Solo se alcanza el 13 % del sitio"],
    ]
    return tab("Grafo sintético de 120 páginas: qué cambia un menú global y un enlace a la portada",
               "Tabla de un sitio sintético de 120 páginas: con menú global todo se alcanza en 4 clics como máximo; sin él la profundidad llega a 9; desde una página interna con enlace a la portada se alcanza todo, y sin ese enlace solo 16 de 120 páginas.",
               ["Situación", "Páginas alcanzables", "Clics máximos", "Distribución"], rows, [330, 230, 150, 360], row_h=58, size=12,
               note="Un recorrido en anchura sobre un grafo de enlaces mide alcance y profundidad, no si la gente entiende las etiquetas. El grafo se generó con una semilla y 30 % de enlaces cruzados: un sitio real tiene otra forma, y la medida útil sigue siendo el éxito de personas buscando cosas.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-171
def se171_fitts() -> Fig:
    rows = [
        ["16 px", "0,890 s", "18,3 %", "42,5 %", "56,9 %"],
        ["24 px", "0,805 s", "4,5 %", "23,0 %", "39,3 %"],
        ["32 px", "0,746 s", "0,9 %", "10,9 %", "25,3 %"],
        ["44 px", "0,681 s", "0,0 %", "2,8 %", "11,5 %"],
        ["48 px", "0,663 s", "0,0 %", "1,7 %", "8,7 %"],
    ]
    return tab("Tamaño del objetivo: tiempo de apuntar y toques que caen fuera",
               "Tabla con cinco tamaños de botón: el tiempo de la ley de Fitts baja de 0,89 a 0,66 segundos de 16 a 48 píxeles, y los toques que fallan con dispersión de 6, 10 y 14 píxeles pasan, con 24 píxeles, de 4,5 a 39,3 por ciento.",
               ["Ancho del objetivo", "Tiempo (D = 600 px)", "Fuera, σ = 6 px", "Fuera, σ = 10 px", "Fuera, σ = 14 px"], rows, [190, 220, 190, 190, 190], row_h=36, size=13,
               note="Tiempo: 0,1 + 0,15·log2(D/W + 1), con constantes supuestas; fallo: probabilidad de que un toque con dispersión gaussiana caiga a más de W/2 del centro, en una dimensión. La dispersión de una persona con temblor, un dedo grande o un autobús en marcha no se midió: los tres σ son escenarios.",
               note_kind="gold", foot=SINT)


def se171_doble() -> Fig:
    items = [
        ("Sin protección: registros duplicados", 1411, "coral", "1 411 (6 411 peticiones)"),
        ("Botón desactivado (10 % recarga y reenvía)", 156, "gold", "156 (5 156 peticiones)"),
        ("Clave de idempotencia en el servidor", 0, "teal", "0 (6 411 peticiones)"),
    ]
    return auto_bars("Registros duplicados de 5 000 envíos con latencia lognormal y paciencia variable",
                     "Barras: de 5 000 envíos, sin protección se crean 1 411 registros duplicados; con el botón desactivado 156, de quienes recargan la página; con una clave de idempotencia ninguno, aunque el servidor recibe las mismas 6 411 peticiones.",
                     items, "Desactivar el botón evita el reenvío de quien no sale de la página, no de quien recarga ni de un reintento de red. Una clave de idempotencia no reduce las peticiones, hace inocuo repetirlas. Latencia (mediana 0,9 s) y paciencia (mediana 1,5 s) son supuestos.",
                     label_w=420, width=1090, headroom=300)


def se171_deshacer() -> Fig:
    items = [
        ("Diálogo de confirmación, 50 % confirma por reflejo", 306, "gold", "306"),
        ("Diálogo, 80 % confirma por reflejo", 479, "coral", "479"),
        ("Diálogo, 95 % confirma por reflejo", 571, "coral", "571"),
        ("Deshacer durante una ventana (70 % lo nota)", 178, "teal", "178"),
    ]
    return auto_bars("Errores que se vuelven permanentes en 20 000 operaciones con 600 errores iniciales",
                     "Barras: de 600 errores en 100 series de 200 operaciones con 3 por ciento de error, un diálogo con 50, 80 y 95 por ciento de confirmación por reflejo deja 306, 479 y 571 errores permanentes; una ventana de deshacer donde 70 por ciento nota el error deja 178.",
                     items, "El diálogo falla porque convierte una interrupción en hábito; deshacer cambia la carga del momento de decidir al de comprobar. Los porcentajes de reflejo y de detección son supuestos del autor: lo que se mide es cómo cambia el resultado al moverlos.",
                     label_w=480, width=1100, headroom=200)


# ---------------------------------------------------------------- SE-172
def se172_estados() -> Fig:
    rows = [
        ["Tres banderas booleanas", "8", "4", "198 de 200 eventos terminan en una combinación imposible"],
        ["Un único estado con cuatro valores", "4", "4", "0 de 200: solo las transiciones declaradas"],
        ["Dos fuentes con cuatro estados cada una", "16", "16", "Cada combinación necesita un diseño"],
        ["Cuatro fuentes", "256", "256", "Un diseño por combinación ya no es viable"],
    ]
    return tab("Banderas independientes frente a un estado explícito",
               "Tabla: tres banderas dan 8 combinaciones de las que solo 4 tienen sentido, y 198 de 200 eventos aleatorios terminan en una combinación imposible; un estado explícito con transiciones declaradas no llega a ninguna, y cuatro fuentes con cuatro estados crean 256 combinaciones.",
               ["Modelo del estado de la lista", "Combinaciones posibles", "Con significado", "Resultado en 200 eventos aleatorios"], rows, [330, 190, 170, 400], row_h=48, size=12,
               note="El manejador con banderas olvida apagar la carga y el error al llegar los datos: cada actualización es correcta por separado y el conjunto no. Los eventos son aleatorios con semilla fija; en una aplicación real los eventos no son equiprobables, pero la combinación imposible sigue siendo alcanzable.",
               note_kind="gold", foot=SINT)


def se172_reintentos() -> Fig:
    rows = [
        ["Cada segundo, sin espera creciente", "10 000", "1 000", "11 000"],
        ["Espera exponencial sin aleatoriedad", "3 000", "1 000", "4 000"],
        ["Espera exponencial con aleatoriedad completa", "3 978", "151", "4 978"],
    ]
    return tab("Mil clientes tras una caída de 10 s: carga durante la caída y pico al recuperarse",
               "Tabla de tres políticas de reintento con mil clientes y una caída de diez segundos: reintentar cada segundo suma 10 000 peticiones durante la caída y un pico de 1 000 al recuperarse; la espera exponencial sin aleatoriedad suma 3 000 pero mantiene el pico de 1 000; con aleatoriedad completa suma 3 978 y el pico baja a 151.",
               ["Política de reintento", "Peticiones durante la caída", "Pico por segundo al recuperarse", "Total"], rows, [400, 230, 250, 120], row_h=40, size=13,
               note="Los clientes arrancan casi a la vez (en 0,5 s) y el servicio vuelve a los 10 s. La espera exponencial reduce el tráfico pero deja a los clientes sincronizados; la aleatoriedad rompe esa sincronía. Es una simulación de un recurso sin capacidad finita: no incluye colas ni límites del servidor.",
               note_kind="gold", foot=SINT)


def se172_latencia() -> Fig:
    items = [
        ("Cargas que tardan más de 0,1 s", 93.7, "coral", "93,7 %"),
        ("Más de 0,3 s", 62.3, "gold", "62,3 %"),
        ("Más de 1 s", 15.3, "gold", "15,3 %"),
        ("Más de 3 s", 1.4, "teal", "1,4 %"),
        ("Más de 10 s", 0.0, "teal", "0,0 %"),
    ]
    return auto_bars("Latencia lognormal simulada (mediana 0,4 s): cuántas cargas cruzan cada umbral",
                     "Barras: con latencia lognormal de mediana 0,4 segundos y dispersión 0,9, el 93,7 por ciento de las cargas supera 0,1 segundos, el 62,3 supera 0,3, el 15,3 supera 1, el 1,4 supera 3 y ninguna supera 10.",
                     items, "Con un indicador inmediato, 37,7 % de las cargas (las de menos de 0,3 s) lo mostrarían una fracción de segundo y desaparecerían: un parpadeo. Retrasar el indicador 0,3 s lo evita en esas, pero 4 432 cargas de 20 000 lo mostrarían menos de 0,2 s; una duración mínima lo arregla. La distribución es supuesta.",
                     label_w=320, width=980, headroom=210)


# ---------------------------------------------------------------- SE-173
def se173_contraste() -> Fig:
    rows = [
        ["#767676 sobre #ffffff", "4,54", "Sí", "Sí"],
        ["#777777 sobre #ffffff", "4,48", "No", "Sí"],
        ["#087f8c sobre #ffffff", "4,75", "Sí", "Sí"],
        ["#c0432f sobre #fbe4de", "4,22", "No", "Sí"],
        ["#a8761a sobre #f7ebc8", "3,35", "No", "Sí"],
        ["#ff0000 sobre #ffffff", "4,00", "No", "Sí"],
    ]
    return tab("Razón de contraste de pares de colores de las figuras del programa y límites de WCAG",
               "Tabla de seis pares de colores con su razón de contraste: 4,54, 4,48, 4,75, 4,22, 3,35 y 4,00; solo el gris 767676 y el verde azulado pasan el mínimo de 4,5 para texto normal, y los seis pasan el mínimo de 3 para texto grande y componentes.",
               ["Par de colores", "Razón", "Pasa 4,5:1 (texto)", "Pasa 3:1 (grande/UI)"], rows, [330, 140, 220, 230], row_h=36, size=13,
               note="De 20 000 pares de colores sRGB al azar, 12,0 % alcanza 4,5:1 y 26,5 % alcanza 3:1: elegir sin calcular suele fallar. El gris más claro que pasa 4,5:1 sobre blanco es #767676. La razón se calcula con la fórmula de luminancia relativa de WCAG; no sustituye mirar el texto con su tamaño y grosor reales.",
               note_kind="gold", foot=SINT)


def se173_auditor() -> Fig:
    rows = [
        ["Falta lang, título, etiqueta, alt, nombre del botón o id duplicado", "6 de 6", "Regla mecánica sobre atributos"],
        ["Campo cuya única etiqueta es un placeholder", "1 de 1", "Se detecta como ausencia de etiqueta"],
        ["Texto alternativo «imagen1.png»", "0 de 1", "Hay alt, pero no describe"],
        ["Etiqueta que dice «Archivo» sobre el campo del nombre", "0 de 1", "Hay etiqueta, pero es falsa"],
        ["Título genérico, botón «Clic aquí», lang incorrecto", "0 de 3", "Están presentes y son incorrectos"],
    ]
    return tab("Auditor de reglas sobre 12 defectos inyectados en un formulario de entrega",
               "Tabla: un auditor de reglas sobre atributos detecta 7 de 12 defectos inyectados; detecta toda ausencia de atributo y ningún atributo presente pero incorrecto, como un texto alternativo que no describe, una etiqueta falsa, un título genérico o un idioma equivocado.",
               ["Defecto inyectado", "Detectados", "Por qué"], rows, [500, 150, 330], row_h=52, size=12,
               note="Siete de doce: las reglas ven presencia, no verdad. El auditor es un programa de 60 líneas con el analizador de HTML de la biblioteca estándar; una herramienta de producción tiene más reglas, pero la frontera es la misma, que algo presente puede ser incorrecto.",
               note_kind="coral", foot=SINT)


def se173_destinos() -> Fig:
    items = [
        ("Separación de 2 px entre destinos", 58.0, "coral", "58,0 % cumplen"),
        ("Separación de 8 px", 100.0, "teal", "100 % cumplen"),
        ("Separación de 16 px", 100.0, "teal", "100 % cumplen"),
    ]
    return auto_bars("Destinos de una fila que cumplen el tamaño mínimo de 24 px o la excepción por espacio",
                     "Barras: en 600 destinos sintéticos con anchos de 16 a 44 píxeles dispuestos en filas de seis, cumplen el tamaño mínimo o su excepción por espacio el 58,0 por ciento con 2 píxeles de separación y el 100 por ciento con 8 o 16.",
                     items, "Alrededor de la mitad de los destinos mide menos de 24 px, así que el cumplimiento depende del espacio. El modelo es unidimensional y usa la regla de círculo de 24 px de WCAG 2.2; en una rejilla real los vecinos diagonales y los alvéolos de lectura táctil cambian el cálculo.",
                     label_w=360, width=980, headroom=230)


# ---------------------------------------------------------------- SE-174
def se174_tab() -> Fig:
    items = [
        ("Sin enlace de salto: pulsaciones de Tab hasta «Enviar»", 43, "coral", "43"),
        ("Con enlace de salto: Tab, Intro y 3 Tab", 5, "teal", "5"),
        ("Controles interactivos de la página", 44, "grey", "44"),
        ("De ellos, alcanzables por teclado", 42, "gold", "42"),
    ]
    return auto_bars("Teclado en una página con 40 enlaces de navegación y un formulario",
                     "Barras: sin enlace de salto, llegar al botón Enviar exige 43 pulsaciones de Tab; con él, 5; de 44 controles interactivos, 42 se alcanzan por teclado porque los dos que son un div con clic quedan fuera.",
                     items, "Un div con un controlador de clic parece un botón y no recibe foco, ni responde a Intro ni a Espacio. Un tabindex positivo cambia el orden (C, B, A, D en lugar de A, B, C, D) y se rompe con cada elemento nuevo. Un modal sin salida con Escape atrapó el foco durante las 30 pulsaciones simuladas.",
                     label_w=520, width=1100, headroom=160)


def se174_nombre() -> Fig:
    rows = [
        ["<button>Enviar</button>", "Contenido", "Enviar"],
        ["<button></button>", "Ninguna", "Sin nombre"],
        ["<button><img src=i.png></button>", "Ninguna", "Sin nombre"],
        ["<button aria-label=\"Cerrar\"></button>", "aria-label", "Cerrar"],
        ["<input placeholder=\"Nombre\">", "placeholder", "Nombre (frágil)"],
        ["<a href=#><span class=icon></span></a>", "Ninguna", "Sin nombre"],
        ["<label for=m>Nombre</label><input id=n>", "Ninguna", "Sin nombre"],
        ["<input aria-label=\"\">", "Ninguna", "Sin nombre"],
    ]
    return tab("Nombre accesible de ocho controles con un cálculo simplificado de la norma",
               "Tabla de ocho fragmentos de HTML con el origen y el valor del nombre accesible: tres botones o enlaces sin contenido quedan sin nombre, una etiqueta que apunta a otro id deja un campo sin nombre y un placeholder da un nombre que desaparece al escribir.",
               ["Fragmento", "Origen del nombre", "Resultado"], rows, [480, 230, 270], row_h=34, size=12,
               note="En 12 fragmentos de prueba, 5 controles quedaron sin nombre. El cálculo implementa solo un subconjunto de la norma (aria-labelledby, aria-label, label, contenido, title, placeholder); no cubre imágenes dentro de botones con alt, listas, ni la salida real de un lector de pantalla.",
               note_kind="gold", foot=SINT)


def se174_estructura() -> Fig:
    rows = [
        ["Secciones con h2 reales", "201", "12", "9 saltos hasta la sección 9"],
        ["Secciones con div de clase «titulo»", "201", "0", "Ninguna: solo lectura lineal"],
        ["Niveles 1, 2, 2, 3, 3, 2, 4, 2, 3", "—", "9", "Un salto de nivel (del 2 al 4)"],
    ]
    return tab("Estructura navegable: encabezados reales frente a texto con aspecto de título",
               "Tabla: en una página de 12 secciones y 24 párrafos cada una, llegar a la sección 9 exige leer 201 nodos; con encabezados reales se llega con 9 saltos, con div estilizados no hay forma de saltar, y una secuencia de niveles tiene un salto del 2 al 4.",
               ["Página", "Nodos hasta la sección 9", "Encabezados disponibles", "Resultado"], rows, [330, 200, 190, 260], row_h=44, size=12,
               note="El analizador cuenta nodos y encabezados de una página generada; no mide cómo navega una persona con un lector de pantalla, que combina atajos, listas de enlaces y regiones. El número de nodos lo fija la página sintética (12 × 24 + 12 + 1).",
               note_kind="gold", foot=SINT)


FIGURES = {
    "se-169-tiempo-por-diseno.svg": se169_klm,
    "se-169-el-promedio-no-existe.svg": se169_promedio,
    "se-169-etapa-que-pierde-mas-gente.svg": se169_embudo,
    "se-170-anchura-frente-a-profundidad.svg": se170_anchura,
    "se-170-participantes-en-card-sorting.svg": se170_cards,
    "se-170-alcance-del-menu-global.svg": se170_menu,
    "se-171-tamano-del-objetivo.svg": se171_fitts,
    "se-171-doble-envio.svg": se171_doble,
    "se-171-confirmar-o-deshacer.svg": se171_deshacer,
    "se-172-estados-imposibles.svg": se172_estados,
    "se-172-politicas-de-reintento.svg": se172_reintentos,
    "se-172-umbrales-de-latencia.svg": se172_latencia,
    "se-173-razones-de-contraste.svg": se173_contraste,
    "se-173-lo-que-ve-un-auditor-automatico.svg": se173_auditor,
    "se-173-separacion-entre-destinos.svg": se173_destinos,
    "se-174-teclado-hasta-enviar.svg": se174_tab,
    "se-174-nombre-accesible.svg": se174_nombre,
    "se-174-encabezados-reales.svg": se174_estructura,
}
