"""Figures for SE-235 to SE-240 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time is shown)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars
from figures_part07_a import bars

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2), salvo los tiempos indicados."
MODELO = "Modelo con supuestos del autor, semilla fija; no es una medición de un navegador ni de usuarios reales."


# ---------------------------------------------------------------- SE-235
def se235_compresion() -> Fig:
    return grouped_bars(
        "Bytes sobre la red de cinco activos sintéticos según el algoritmo y el nivel",
        "Barras horizontales en escala logarítmica con los bytes de cinco activos sin comprimir y con gzip 1, 6 y 9 y xz: el texto sintético se reduce entre 77 y 91 por ciento con gzip nivel 6 y algo más con xz, mientras que un archivo de bytes aleatorios, equivalente a una imagen ya comprimida, crece unos 38 bytes con cualquier algoritmo.",
        ["CSS, 900 reglas", "HTML, lista de 800", "JS, 450 funciones", "JSON, 800 filas", "PNG, bytes aleatorios"],
        [("Bruto", [74585, 45232, 84488, 73063, 60000], "grey"), ("gzip 1", [15797, 9311, 7416, 8832, 60038], "gold"), ("gzip 6", [12462, 7835, 6009, 6737, 60038], "coral"),
         ("gzip 9", [11776, 7721, 5594, 6226, 60038], "navy"), ("xz", [10348, 4532, 4836, 4820, 60060], "teal")],
        unit="Bytes", horizontal=True, log=True, decimals=0, label_w=190,
        note="Minificar antes de comprimir ahorró 29,5 % en el JS sintético (de 6009 a 4235 bytes con gzip) y solo 3,6 % en el CSS (de 12 462 a 12 013). Brotli no está en la biblioteca estándar de Python y no se midió. El texto sintético es más repetitivo que el real: las razones reales serán menores.",
        note_kind="gold", foot=SINT)

def se235_cascada() -> Fig:
    return grouped_bars(
        "Cascada de recursos: qué optimización acorta la ruta crítica de una página sintética",
        "Barras horizontales con el tiempo de una página con HTML, hoja de estilos, script, imagen, fuente y datos: en fibra la línea base tarda 195 milisegundos, el preload de fuente y datos 123 y el CSS en línea 199; en móvil 4G, 801, 701 y 801; en móvil lento, 3805, 3712 y 3805.",
        ["Fibra (RTT 20 ms, 100 Mbit/s)", "Móvil 4G (RTT 80 ms, 10 Mbit/s)", "Móvil lento (RTT 300 ms, 1,5 Mbit/s)"],
        [("Línea base", [195, 801, 3805], "grey"), ("Preload de fuente y datos", [123, 701, 3712], "teal"), ("CSS en línea", [199, 801, 3805], "gold")],
        unit="Milisegundos", horizontal=True, decimals=0, label_w=250,
        note="La ruta crítica es HTML → script de 150 KB → petición de datos. Optimizar fuera de esa cadena (CSS en línea) no cambia el total. El modelo reparte el ancho de banda en partes iguales, ignora la ranura de conexiones y la priorización del navegador.",
        note_kind="gold", foot=MODELO)

def se235_percentiles() -> Fig:
    return line_chart(
        "Estimar el percentil 75 de una métrica con pocas visitas: intervalo y falsa conformidad",
        "Líneas en escala logarítmica con el percentil 75 estimado y los límites de su intervalo central del 95 por ciento según las visitas: 2139 a 3500 milisegundos con 30 visitas, 2597 a 3024 con 300 y 2745 a 2862 con 3000, frente a un valor verdadero de 2802 y un presupuesto de 2500; con 30 visitas se declara cumplido el presupuesto en 22 por ciento de las repeticiones.",
        [("Límite inferior (2,5 %)", [(30, 2139, "2 139", "b"), (300, 2597, "2 597", "b"), (3000, 2745, "2 745", "b")], "teal"),
         ("p75 estimado (media)", [(30, 2772, "2 772", "r"), (300, 2804, "2 804", "r"), (3000, 2800, "2 800", "r")], "gold"),
         ("Límite superior (97,5 %)", [(30, 3500, "3 500", "t"), (300, 3024, "3 024", "t"), (3000, 2862, "2 862", "t")], "coral")],
        x_label="Visitas en la muestra", y_label="Milisegundos", log_x=True,
        x_ticks=[(30, "30"), (300, "300"), (3000, "3000")], y_ticks=[2000, 2500, 3000, 3500], y_zero=False,
        hlines=[(2500, "presupuesto 2500")], point_labels="none", decimals=0, plot_h=300,
        note="El eje vertical empieza en 2000 ms. El percentil 75 verdadero es 2802. Falsamente conformes (dicen cumplir 2500 ms): 22,0 % con 30 visitas, 0,1 % con 300 y 0,0 % con 3000. Población lognormal con mediana 2000 ms y σ = 0,5: media 2266, p75 2802, p95 4552. Con 30 visitas una de cada cinco veces se concluye, erróneamente, que el presupuesto se cumple. Los valores reales de usuarios no son lognormales ni independientes.",
        note_kind="gold", foot=MODELO)

# ---------------------------------------------------------------- SE-236
def se236_escape() -> Fig:
    return grouped_bars(
        "De 16 cargas maliciosas o legítimas, cuántas se vuelven código según el contexto de salida",
        "Barras agrupadas con las cargas de 16 que se ejecutan según el contexto: sin codificar 5 en texto, 1 en atributo con comillas, 3 sin comillas, 3 en href y 6 en un script; el escape HTML genérico deja 4 en atributo sin comillas y 2 en href, y en un script deforma el texto; la codificación adecuada deja 0.",
        ["Texto dentro de un elemento", "Atributo entre comillas dobles", "Atributo sin comillas", "Valor de href", "Cadena dentro de un script"],
        [("Sin codificar", [5, 1, 3, 3, 6], "coral"), ("Escape HTML genérico", [0, 0, 4, 2, 0], "gold")],
        unit="Cargas que se ejecutan (de 16)", decimals=0, plot_h=260,
        note="Con la codificación adecuada para cada contexto se ejecutan 0 en todos. En un script, el escape HTML genérico muestra 0 porque deforma la cadena. Escapar dos veces produce texto visible roto: ana &amp; co pasó a ana &amp;amp; co. La detección usa un analizador de HTML y, para el script, una regla de ruptura de cadena: es una comprobación acotada de 16 cargas, no una auditoría de seguridad.",
        note_kind="gold", foot=SINT)

def se236_csp() -> Fig:
    items = [
        ("Sin política", 4, "coral", "4 hallazgos"),
        ("Laxa: * con unsafe-inline y unsafe-eval", 6, "coral", "6 hallazgos"),
        ("self con https: y object-src none", 3, "gold", "3 hallazgos"),
        ("self con nonce, object, base y frame-ancestors", 0, "teal", "0 hallazgos"),
        ("default-src none y permisos mínimos", 0, "teal", "0 hallazgos"),
    ]
    return bars("Hallazgos de un linter de políticas CSP sobre cinco políticas de ejemplo",
                "Barras: un evaluador simplificado de script-src acertó 16 de 16 casos de prueba y un linter encontró 4 hallazgos en la ausencia de política, 6 en una política laxa, 3 en una con https: amplio y 0 en dos políticas restrictivas.",
                items, 55, "Los hallazgos son reglas escritas por el autor sobre una política de pocas directivas. El evaluador no implementa strict-dynamic, hashes, trusted types ni el informe de violaciones; una política sin hallazgos aquí puede romper una página o seguir dejando pasar un ataque.",
                label_w=470, width=1060, note_kind="gold", foot=SINT)


def se236_samesite() -> Fig:
    return heatmap(
        "¿Viaja la cookie en una petición iniciada desde otro sitio? Matriz de SameSite",
        "Mapa de calor binario de cinco peticiones desde otro sitio y tres valores de SameSite: con Strict la cookie no viaja nunca, con Lax viaja solo en una navegación GET de nivel superior y con None viaja siempre; de 14 peticiones CORS del ejemplo, 7 necesitan una comprobación previa.",
        ["Navegar con un enlace (GET de nivel superior)", "Enviar un formulario (POST)", "fetch con POST desde otro sitio", "Imagen incrustada", "Página incrustada en un iframe"],
        ["Strict", "Lax", "None"],
        [[0, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        unit="la cookie viaja", scale="navy", vmin=0, vmax=1, cell_fmt=lambda v: "viaja" if v else "no viaja", label_w=310,
        note="Las dos peticiones que cambian estado (formulario y fetch POST) solo llevan la cookie con None: Lax y Strict cortan esa vía de falsificación entre sitios. De 14 peticiones CORS de ejemplo, 7 necesitan una comprobación previa. Es una tabla de la regla, no una medición de navegadores; la excepción de Lax con POST reciente de algunos navegadores no está modelada.",
        note_kind="gold", foot=SINT)

# ---------------------------------------------------------------- SE-237
def se237_estrategias() -> Fig:
    return grouped_bars(
        "Estrategias de caché en 20 000 peticiones con 19,4 % del tiempo sin conexión",
        "Barras horizontales con el porcentaje de peticiones servidas desde caché, con fallo y con contenido obsoleto en cinco estrategias: solo red falla en 19,33 por ciento; caché primero responde en 6 milisegundos pero sirve obsoleto el 69,88; red primero casi no sirve obsoleto pero tarda 165; revalidar en segundo plano lo reduce a 5,2 por ciento.",
        ["Solo red (120 ms)", "Caché primero (6,2 ms)", "Caché primero con precarga (5,0 ms)", "Red primero con respaldo en caché (165 ms)", "Revalidar en segundo plano (6,2 ms)"],
        [("Desde caché", [0, 98.3, 100, 18.6, 98.3], "teal"), ("Fallos", [19.33, 0.69, 0, 0.69, 0.69], "coral"), ("Contenido obsoleto", [0, 69.88, 70.83, 1.47, 5.2], "gold")],
        unit="Peticiones (%)", horizontal=True, decimals=2, label_w=280,
        note="Entre paréntesis, la latencia media. 200 URL con popularidad 1/n, cambios de 0 a 12 por URL en 500 h y ráfagas sin conexión que suman 19,4 % del tiempo. Los 120 ms de red, 5 ms de caché y 360 ms de espera son supuestos; la obsolescencia cuenta versiones, no importancia del cambio.",
        note_kind="gold", foot=MODELO)

def se237_versiones() -> Fig:
    items = [
        ("Caché con otro nombre en cada versión (100 recursos)", 3035.7, "coral", "3036 KB"),
        ("Revisión por huella: solo los 3 recursos cambiados", 17.3, "teal", "17,3 KB"),
    ]
    return bars("Datos que se vuelven a descargar al publicar una versión que cambia 3 de 100 recursos",
                "Barras: cambiar el nombre de la caché en cada versión obliga a descargar de nuevo los 100 recursos, 3036 kilobytes, mientras que registrar una huella por recurso descarga solo los tres cambiados, 17,3 kilobytes, un ahorro de 99,4 por ciento.",
                items, 0.15, "El ahorro depende de que solo cambie lo que cambió: un empaquetador que mezcla módulos o cambia el orden altera huellas que no debía. Al purgar la caché antigua al activar, una pestaña abierta con la versión vieja puede pedir un recurso que ya no existe.",
                label_w=490, width=1060, note_kind="gold", foot=SINT)


def se237_sync() -> Fig:
    return grouped_bars(
        "Sincronizar tras estar sin conexión: duplicados, reintentos y escrituras perdidas",
        "Barras agrupadas con el resultado de la sincronización: sin clave de idempotencia, 2000 envíos con 20 por ciento de confirmaciones perdidas producen 2476 efectos y 476 reintentos; con clave, 2000 efectos y 390 reintentos; con la última escritura gana, 300 ediciones se descartan, y con comprobación de versión ninguna en silencio.",
        ["Efectos en el servidor (2000 envíos)", "Reintentos (2000 envíos)", "Ediciones descartadas en silencio (300 concurrentes)"],
        [("Sin clave de idempotencia / última escritura gana", [2476, 476, 300], "coral"), ("Con clave por operación / comprobación de versión", [2000, 390, 0], "teal")],
        unit="Cantidad", decimals=0, plot_h=260,
        note="Sin clave hay 476 efectos duplicados; con clave, 0. Con la última escritura gana, en 13,3 % gana la más antigua por reloj, y la comprobación de versión exige resolver el conflicto. Los relojes de los dispositivos se desviaron hasta ±2 min (supuesto). Si la política de nota por entrega tardía usa la hora del cliente, ese desajuste decide una nota: la hora debe ser la del servidor al recibir, o una marca firmada.",
        note_kind="coral", foot=MODELO)

# ---------------------------------------------------------------- SE-238
def se238_robots() -> Fig:
    return grouped_bars(
        "Rutas en las que robotparser de Python y la regla de coincidencia más larga del RFC 9309 discrepan",
        "Barras horizontales con las rutas de 14 en que discrepan el analizador de Python y el RFC 9309 sobre seis archivos robots.txt: 2 con Disallow /admin y Allow /admin/ayuda, 2 con /entregas, 3 con comodines y ninguna en los otros tres; 7 de 84 decisiones difieren.",
        ["Disallow /admin y luego Allow /admin/ayuda", "Allow /admin/ayuda y luego Disallow /admin", "Disallow /entregas y Allow /entregas/123", "Comodines: /buscar? y /*.pdf$", "Solo Disallow /privado", "Archivo vacío"],
        [("Rutas que difieren (de 14)", [2, 0, 2, 3, 0, 0], "coral")],
        unit="Rutas con decisión distinta", horizontal=True, decimals=0, label_w=300,
        note="Difieren, por ejemplo, /admin/ayuda y /admin/ayuda/faq; con comodines, /buscar, /tmp/a.pdf y /a.pdf. Un mismo archivo puede permitir una ruta para un rastreador y bloquearla para otro si implementan distinto el RFC. Además, Disallow impide al rastreador leer la página, y por tanto ver un noindex que esta contenga.",
        note_kind="gold", foot=SINT)

def se238_facetas() -> Fig:
    return grouped_bars(
        "URLs que una navegación facetada pone al alcance de un rastreador",
        "Barras horizontales en escala logarítmica con las URLs posibles: 33 600 combinaciones con seis facetas, 2 016 000 URLs con tres órdenes y veinte páginas en orden fijo, 544 467 960 si el orden de los parámetros puede variar y 600 si solo una faceta es indexable.",
        ["6 facetas con 4, 5, 6, 3, 7 y 4 valores, más «sin filtro»", "Con 3 órdenes y 20 páginas, parámetros en orden fijo", "Si los parámetros pueden llegar en cualquier orden", "Como mucho una faceta indexable (el resto con canónica)"],
        [("URLs posibles", [33600, 2016000, 544467960, 600], "coral")],
        unit="URLs posibles", horizontal=True, log=True, decimals=0, label_w=330,
        note="Cálculo exacto por enumeración de subconjuntos y permutaciones, validado enumerando un caso pequeño (36 combinaciones). Cuántas de esas URLs rastrea realmente un buscador depende de enlaces, presupuesto y señales que no se miden aquí.",
        note_kind="gold", foot=SINT)

def se238_metadatos() -> Fig:
    items = [
        ("Canónica relativa (14)", 14, "teal", "14 de 14"),
        ("Descripción larga (15)", 15, "teal", "15 de 15"),
        ("Título duplicado (15)", 15, "teal", "15 de 15"),
        ("Título largo (11)", 11, "teal", "11 de 11"),
        ("JSON-LD inválido (9)", 9, "teal", "9 de 9"),
        ("noindex olvidado (5)", 5, "teal", "5 de 5"),
        ("Título que no corresponde a la página (7)", 0, "coral", "0 de 7"),
    ]
    return bars("Defectos de metadatos que detecta un auditor de 120 páginas sintéticas con una mutación cada una",
                "Barras: un auditor de metadatos detecta 113 de 120 mutaciones, entre ellas canónica relativa, descripción larga, título duplicado o largo, JSON-LD inválido y noindex olvidado, y no detecta ninguno de los 7 títulos que describen otra cosa que la página.",
                items, 26, "Otros tipos detectados: título ausente 10, descripción ausente 7, canónica ausente 9, imagen social relativa 11 y lang ausente 7. El auditor comprueba forma, no verdad: un título bien formado que no describe la página pasa todas las reglas.",
                label_w=420, width=1000, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-239
def se239_estados() -> Fig:
    items = [
        ("Quitar una transición deja un estado inalcanzable", 3, "coral", "3 de 18"),
        ("Quitar una transición deja un estado sin camino a «Enviado»", 1, "coral", "1 de 18"),
        ("Quitar una transición no activa ninguna comprobación estructural", 14, "gold", "14 de 18"),
    ]
    return bars("Efecto de quitar cada una de las 18 transiciones del flujo de entrega con y sin conexión",
                "Barras: en una máquina de ocho estados y 18 transiciones, quitar una transición deja un estado inalcanzable en 3 casos, un estado sin camino al estado final en 1 y no dispara ninguna comprobación estructural en 14, que cambian el comportamiento sin romper la forma.",
                items, 35, "Alcanzabilidad y camino al final son comprobaciones de forma; no saben si «cancelar» o «reintentar manual» debían existir. Las 14 transiciones que la forma no protege solo las protegen pruebas que ejecuten el comportamiento.",
                label_w=500, width=1100, note_kind="gold", foot=SINT)


def se239_tormenta() -> Fig:
    return grouped_bars(
        "1000 clientes que fallan a la vez frente a un servidor que atiende 50 peticiones por segundo",
        "Barras agrupadas en escala logarítmica de tres políticas de reintento: el reintento fijo y el exponencial sin dispersión producen 10,5 peticiones por cliente y un pico de 950 por segundo, y el segundo tarda 902 segundos en terminar; el exponencial con dispersión completa produce 2,0, un pico de 484 y termina en 23 segundos.",
        ["Reintento fijo cada segundo", "Exponencial sin dispersión", "Exponencial con dispersión completa"],
        [("Peticiones por cliente", [10.5, 10.5, 2.0], "grey"), ("Pico por segundo tras el 1.er segundo", [950, 950, 484], "coral"), ("Segundos hasta el último cliente", [19, 902, 23], "navy")],
        unit="Valor de cada medida", log=True, decimals=1, plot_h=280,
        note="Sin dispersión, los clientes quedan sincronizados en oleadas que se repiten. Con dispersión se reparten y la carga total baja a una quinta parte. Simulación de capacidad fija sin degradación del servidor: un servidor real puede empeorar bajo carga.",
        note_kind="gold", foot=MODELO)

def se239_a11y() -> Fig:
    return heatmap(
        "Nueve defectos de accesibilidad inyectados: cuáles detecta un conjunto de reglas automáticas",
        "Mapa de calor con nueve defectos inyectados y si una regla automática los detecta: seis se detectan, entre ellos el contraste, el foco, las etiquetas y los errores sin asociar, y tres no, porque exigen ver la imagen, identificar el idioma o entender el propósito del campo.",
        ["Contraste insuficiente de un enlace", "Indicador de foco eliminado", "Campo sin etiqueta", "Error sin asociar al campo", "tabindex positivo", "Enlace «clic aquí»",
         "Texto alternativo engañoso", "Idioma declarado equivocado", "Etiqueta que dice otra cosa que el campo"],
        ["¿Lo detecta una regla?"],
        [[1], [1], [1], [1], [1], [1], [0], [0], [0]],
        unit="detección", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "detectado" if v else "no detectado", label_w=290, cell_h=34,
        note="Los tres no detectados exigen mirar la imagen, identificar el idioma del texto o entender el propósito del campo. 6 de 9 es el resultado de estas nueve reglas sobre estos nueve defectos, no una cobertura general de WCAG. Una herramienta automática real cubre más reglas y falla en otras: la revisión con teclado y lector de pantalla sigue haciendo falta.",
        note_kind="gold", foot=SINT)

# ---------------------------------------------------------------- SE-240
def se240_manifiesto() -> Fig:
    return stacked_bars(
        "Validador de manifiesto: 120 mutaciones de un manifiesto de aplicación web sintético",
        "Barras apiladas horizontales con las mutaciones por tipo que detecta el validador de forma: 83 de 120, todas las que faltan o rompen campos, alcance o iconos declarados, y ninguna de las que exigen comprobar el sistema de archivos o el significado, que son 37.",
        ["Falta name, start_url o icons", "short_name largo, display o color inválidos", "start_url fuera del scope", "Sin icono 512 o sin maskable, sizes roto", "src de un icono que no existe", "Nombre engañoso o idioma equivocado", "Icono declarado 192 que mide otra cosa"],
        [("Detectadas", [27, 23, 6, 27, 0, 0, 0], "teal"), ("No detectadas", [0, 0, 0, 0, 11, 18, 8], "coral")],
        unit="Mutaciones", horizontal=True, decimals=0, label_w=300,
        note="Detectadas 83 de 120. Los 37 casos restantes no son defectos del JSON: son discrepancias entre el JSON y el mundo (archivos, significado). Para verlos hay que abrir los archivos referidos y revisar el contenido, no validar el esquema.",
        note_kind="gold", foot=SINT)

def se240_cabeceras() -> Fig:
    return grouped_bars(
        "Auditoría de cabeceras de un servidor local con ocho rutas y cinco configuraciones erróneas",
        "Barras horizontales con los hallazgos por ruta de un comprobador que pidió ocho rutas a un servidor local: 7 en cinco rutas, con el service worker, la hoja de estilos y el manifiesto con 1 cada uno, los datos mutables y la página de ayuda con 2, y ninguno en las tres restantes.",
        ["/app/sw.js", "/app/app.css", "/app/manifest.webmanifest", "/app/datos.json", "/app/ayuda/", "/app/, app.3f9a1c.js, icons/192.png"],
        [("Hallazgos", [1, 1, 1, 2, 2, 0], "coral")],
        unit="Hallazgos", horizontal=True, decimals=0, label_w=270,
        note="Hallazgos: caché de un año en el service worker; no-store en una hoja sin huella; Content-Type application/json en vez de application/manifest+json; un año de caché en datos mutables y sin nosniff; HTML sin charset y sin nosniff. Un servidor Python en 127.0.0.1 con puerto efímero sirvió ocho respuestas de dos bytes; no se tocó ninguna red. Que las cabeceras sean correctas no demuestra que el service worker se actualice: eso solo se ve en un navegador.",
        note_kind="gold", foot=SINT)

def se240_pares() -> Fig:
    items = [
        ("Combinaciones posibles (3×2×3×3×2)", 108, "grey", "108 casos"),
        ("Suite de pares elegida con criterio voraz", 12, "teal", "12 casos"),
        ("Defectos de tres factores hallados por esa suite (de 60)", 32, "gold", "32 de 60"),
        ("Misma cantidad de casos al azar (media de 200)", 31.7, "gold", "31,7 de 60"),
        ("Recorrido exhaustivo de las 108", 60, "teal", "60 de 60"),
    ]
    return bars("Matriz de pruebas de aceptación: cobertura de pares frente a defectos que exigen tres factores",
                "Barras: 108 combinaciones de red, dispositivo, entrada, estado e idioma se reducen a 12 casos que cubren todos los pares; esa suite halla 32 de 60 defectos que exigen tres factores a la vez, igual que 12 casos al azar, 31,7, y las 108 los hallan todos.",
                items, 4.5, "Cubrir todos los pares no significa cubrir las interacciones de tres factores: la suite de pares cubre 60,2 % de las triples. Los defectos que dependen de red, entrada y estado a la vez los encuentra el recorrido exhaustivo o la intuición sobre dónde interactúan.",
                label_w=500, width=1100, note_kind="gold", foot=SINT)


FIGURES = {
    "se-235-bytes-segun-algoritmo-y-activo.svg": se235_compresion,
    "se-235-ruta-critica-de-recursos.svg": se235_cascada,
    "se-235-percentil-75-con-pocas-visitas.svg": se235_percentiles,
    "se-236-contexto-de-salida-y-codificacion.svg": se236_escape,
    "se-236-hallazgos-de-politicas-csp.svg": se236_csp,
    "se-236-samesite-y-peticiones-entre-sitios.svg": se236_samesite,
    "se-237-estrategias-de-cache.svg": se237_estrategias,
    "se-237-descargas-al-actualizar.svg": se237_versiones,
    "se-237-duplicados-y-conflictos-al-sincronizar.svg": se237_sync,
    "se-238-robots-txt-segun-el-analizador.svg": se238_robots,
    "se-238-urls-de-navegacion-facetada.svg": se238_facetas,
    "se-238-auditor-de-metadatos.svg": se238_metadatos,
    "se-239-efecto-de-quitar-transiciones.svg": se239_estados,
    "se-239-tormenta-de-reintentos.svg": se239_tormenta,
    "se-239-defectos-de-accesibilidad-detectables.svg": se239_a11y,
    "se-240-validador-de-manifiesto.svg": se240_manifiesto,
    "se-240-cabeceras-de-un-servidor-local.svg": se240_cabeceras,
    "se-240-cobertura-de-pares-y-triples.svg": se240_pares,
}
