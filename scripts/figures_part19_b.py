"""Figures for SE-235 to SE-240 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time is shown)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2), salvo los tiempos indicados."
MODELO = "Modelo con supuestos del autor, semilla fija; no es una medición de un navegador ni de usuarios reales."


# ---------------------------------------------------------------- SE-235
def se235_compresion() -> Fig:
    rows = [
        ["CSS, 900 reglas", "74 585", "15 797", "12 462", "11 776", "10 348"],
        ["HTML, lista de 800", "45 232", "9 311", "7 835", "7 721", "4 532"],
        ["JS, 450 funciones", "84 488", "7 416", "6 009", "5 594", "4 836"],
        ["JSON, 800 filas", "73 063", "8 832", "6 737", "6 226", "4 820"],
        ["PNG, bytes aleatorios", "60 000", "60 038", "60 038", "60 038", "60 060"],
    ]
    return tab("Bytes sobre la red de cinco activos sintéticos según el algoritmo y el nivel",
               "Tabla: el texto sintético se reduce entre 77 y 91 por ciento con gzip nivel 6 y algo más con xz, mientras que un archivo de bytes aleatorios, equivalente a una imagen ya comprimida, crece unos 38 bytes con cualquier algoritmo.",
               ["Activo", "Bruto", "gzip 1", "gzip 6", "gzip 9", "xz"], rows, [270, 120, 130, 130, 130, 130], row_h=44, size=13,
               note="Minificar antes de comprimir ahorró 29,5 % en el JS sintético (de 6009 a 4235 bytes con gzip) y solo 3,6 % en el CSS (de 12 462 a 12 013). Brotli no está en la biblioteca estándar de Python y no se midió. El texto sintético es más repetitivo que el real: las razones reales serán menores.",
               note_kind="gold", foot=SINT)


def se235_cascada() -> Fig:
    rows = [
        ["Fibra (RTT 20 ms, 100 Mbit/s)", "195 ms", "123 ms", "199 ms"],
        ["Móvil 4G (RTT 80 ms, 10 Mbit/s)", "801 ms", "701 ms", "801 ms"],
        ["Móvil lento (RTT 300 ms, 1,5 Mbit/s)", "3805 ms", "3712 ms", "3805 ms"],
    ]
    return tab("Cascada de recursos: qué optimización acorta la ruta crítica de una página sintética",
               "Tabla: en una página con HTML, hoja de estilos, script, imagen, fuente y datos, anticipar la fuente y los datos con preload baja el tiempo de 195 a 123 milisegundos en fibra, y poner el CSS en línea no lo cambia porque la ruta más larga es script y luego datos.",
               ["Perfil de red supuesto", "Línea base", "Preload de fuente y datos", "CSS en línea"], rows, [370, 150, 230, 170], row_h=48, size=13,
               note="La ruta crítica es HTML → script de 150 KB → petición de datos. Optimizar fuera de esa cadena (CSS en línea) no cambia el total. El modelo reparte el ancho de banda en partes iguales, ignora la ranura de conexiones y la priorización del navegador.",
               note_kind="gold", foot=MODELO)


def se235_percentiles() -> Fig:
    rows = [
        ["30 visitas", "2772 ms", "2139 – 3500 ms", "22,0 %"],
        ["300 visitas", "2804 ms", "2597 – 3024 ms", "0,1 %"],
        ["3000 visitas", "2800 ms", "2745 – 2862 ms", "0,0 %"],
    ]
    return tab("Estimar el percentil 75 de una métrica con pocas visitas: intervalo y falsa conformidad",
               "Tabla: con una población sintética de mediana 2000 milisegundos y percentil 75 verdadero de 2802, estimar el percentil 75 con 30 visitas da un intervalo de 95 por ciento de 2139 a 3500 y declara cumplido un presupuesto de 2500 en 22 por ciento de las repeticiones, con 300 visitas en 0,1 por ciento.",
               ["Tamaño de la muestra", "p75 estimado (media)", "Intervalo central del 95 %", "Dice cumplir 2500 ms (falso)"], rows, [250, 230, 250, 230], row_h=48, size=13,
               note="Población lognormal con mediana 2000 ms y σ = 0,5: media 2266, p75 2802, p95 4552. Con 30 visitas una de cada cinco veces se concluye, erróneamente, que el presupuesto se cumple. Los valores reales de usuarios no son lognormales ni independientes.",
               note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-236
def se236_escape() -> Fig:
    rows = [
        ["Texto dentro de un elemento", "5", "0", "Escape HTML: 0"],
        ["Atributo entre comillas dobles", "1", "0", "Escape HTML con comillas: 0"],
        ["Atributo sin comillas", "3", "4", "Poner comillas y escapar: 0"],
        ["Valor de href", "3", "2", "Escapar y permitir solo http, https y mailto: 0"],
        ["Cadena dentro de un script", "6", "0 (cadena deformada)", "JSON con < > & escapados: 0"],
    ]
    return tab("De 16 cargas maliciosas o legítimas, cuántas se vuelven código según el contexto de salida",
               "Tabla: sin codificar, entre 1 y 6 de 16 cargas útiles se ejecutan según el contexto; el escape HTML basta en el texto, no en atributos sin comillas ni en href, y en un script deforma el texto; cada contexto necesita su propia codificación.",
               ["Dónde se escribe el dato", "Sin codificar", "Escape HTML genérico", "Codificación adecuada"], rows, [290, 130, 200, 330], row_h=50, size=12,
               note="Escapar dos veces produce texto visible roto: ana &amp; co pasó a ana &amp;amp; co. La detección usa un analizador de HTML y, para el script, una regla de ruptura de cadena: es una comprobación acotada de 16 cargas, no una auditoría de seguridad.",
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
    rows = [
        ["Navegar con un enlace (GET de nivel superior)", "No", "Sí", "Sí"],
        ["Enviar un formulario (POST)", "No", "No", "Sí"],
        ["fetch con POST desde otro sitio", "No", "No", "Sí"],
        ["Imagen incrustada", "No", "No", "Sí"],
        ["Página incrustada en un iframe", "No", "No", "Sí"],
    ]
    return tab("¿Viaja la cookie en una petición iniciada desde otro sitio? Matriz de SameSite",
               "Tabla: en una petición desde otro sitio, la cookie con SameSite Strict no viaja nunca, con Lax viaja solo en una navegación GET de nivel superior y con None viaja siempre; de las 14 peticiones CORS del ejemplo, 7 necesitan una comprobación previa.",
               ["Petición iniciada desde otro sitio", "Strict", "Lax", "None"], rows, [470, 150, 150, 150], row_h=46, size=13,
               note="Las dos peticiones que cambian estado (formulario y fetch POST) solo llevan la cookie con None: Lax y Strict cortan esa vía de falsificación entre sitios. De 14 peticiones CORS de ejemplo, 7 necesitan una comprobación previa (método distinto de GET, HEAD o POST, cabeceras no seguras o tipo de contenido no simple). Es una tabla de la regla, no una medición de navegadores; la excepción de Lax con POST reciente de algunos navegadores no está modelada.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-237
def se237_estrategias() -> Fig:
    rows = [
        ["Solo red", "0 %", "19,33 %", "0 %", "120 ms"],
        ["Caché primero", "98,3 %", "0,69 %", "69,88 %", "6,2 ms"],
        ["Caché primero con precarga", "100 %", "0 %", "70,83 %", "5,0 ms"],
        ["Red primero con respaldo en caché", "18,6 %", "0,69 %", "1,47 %", "165 ms"],
        ["Revalidar en segundo plano", "98,3 %", "0,69 %", "5,2 %", "6,2 ms"],
    ]
    return tab("Estrategias de caché en 20 000 peticiones con 19,4 % del tiempo sin conexión",
               "Tabla: servir solo desde la red falla en 19,33 por ciento de las peticiones; caché primero responde en 6 milisegundos pero sirve contenido obsoleto en 69,88 por ciento; red primero casi no sirve obsoleto pero tarda 165; revalidar en segundo plano reduce lo obsoleto a 5,2 por ciento con la misma latencia que caché primero.",
               ["Estrategia", "Desde caché", "Fallos", "Contenido obsoleto", "Latencia media"], rows, [320, 150, 130, 190, 150], row_h=46, size=12,
               note="200 URL con popularidad 1/n, cambios de 0 a 12 por URL en 500 h y ráfagas sin conexión que suman 19,4 % del tiempo. Los 120 ms de red, 5 ms de caché y 360 ms de espera son supuestos; la obsolescencia cuenta versiones, no importancia del cambio.",
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
    rows = [
        ["2000 envíos con 20 % de confirmaciones perdidas, sin clave de idempotencia", "2476 efectos (476 duplicados)", "476 reintentos"],
        ["Los mismos envíos con clave de idempotencia por operación", "2000 efectos (0 duplicados)", "390 reintentos"],
        ["300 ediciones concurrentes sin conexión, última escritura gana", "300 ediciones descartadas", "13,3 % gana la más antigua por reloj"],
        ["Las mismas 300 con comprobación de versión", "0 descartadas en silencio", "exige resolver el conflicto"],
    ]
    return tab("Sincronizar tras estar sin conexión: duplicados, reintentos y escrituras perdidas",
               "Tabla: sin clave de idempotencia, 2000 envíos con 20 por ciento de confirmaciones perdidas producen 476 efectos duplicados; con clave producen 2000; y con la última escritura gana, 300 ediciones concurrentes pierden una, y en 13,3 por ciento gana la más antigua por desajuste de reloj.",
               ["Situación simulada", "Resultado en el servidor", "Reintentos o riesgo"], rows, [420, 270, 250], row_h=62, size=12,
               note="Los relojes de los dispositivos se desviaron hasta ±2 min (supuesto). Si la política de nota por entrega tardía usa la hora del cliente, ese desajuste decide una nota: la hora debe ser la del servidor al recibir, o una marca firmada.",
               note_kind="coral", foot=MODELO)


# ---------------------------------------------------------------- SE-238
def se238_robots() -> Fig:
    rows = [
        ["Disallow /admin y luego Allow /admin/ayuda", "2 de 14", "/admin/ayuda y /admin/ayuda/faq"],
        ["Allow /admin/ayuda y luego Disallow /admin", "0 de 14", "coinciden"],
        ["Disallow /entregas y Allow /entregas/123", "2 de 14", "/entregas/123 y su subruta"],
        ["Comodines: /buscar? y /*.pdf$", "3 de 14", "/buscar, /tmp/a.pdf y /a.pdf"],
        ["Solo Disallow /privado", "0 de 14", "coinciden"],
        ["Archivo vacío", "0 de 14", "coinciden"],
    ]
    return tab("Rutas en las que robotparser de Python y la regla de coincidencia más larga del RFC 9309 discrepan",
               "Tabla: sobre seis archivos robots.txt y 14 rutas, 7 de 84 decisiones difieren entre el analizador de la biblioteca estándar de Python, que aplica la primera regla coincidente y no admite comodines, y la regla de coincidencia más larga del RFC 9309.",
               ["Conjunto de reglas", "Rutas que difieren", "Cuáles"], rows, [430, 150, 360], row_h=46, size=12,
               note="Un mismo archivo puede permitir una ruta para un rastreador y bloquearla para otro si implementan distinto el RFC. Además, Disallow impide al rastreador leer la página, y por tanto ver un noindex que esta contenga.",
               note_kind="gold", foot=SINT)


def se238_facetas() -> Fig:
    rows = [
        ["6 facetas con 4, 5, 6, 3, 7 y 4 valores, más «sin filtro»", "33 600 combinaciones"],
        ["Con 3 órdenes y 20 páginas, parámetros en orden fijo", "2 016 000 URLs"],
        ["Si los parámetros pueden llegar en cualquier orden", "544 467 960 URLs"],
        ["Como mucho una faceta indexable (el resto con canónica)", "600 URLs"],
    ]
    return tab("URLs que una navegación facetada pone al alcance de un rastreador",
               "Tabla: seis facetas, tres órdenes y veinte páginas generan 2 016 000 URLs con los parámetros en orden fijo y 544 467 960 si el orden puede variar; permitir indexar como mucho una faceta deja 600.",
               ["Situación", "URLs posibles"], rows, [640, 300], row_h=50, size=13,
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
    rows = [
        ["Reintento fijo cada segundo", "10,5", "950", "19 s"],
        ["Exponencial sin dispersión", "10,5", "950", "902 s"],
        ["Exponencial con dispersión completa", "2,0", "484", "23 s"],
    ]
    return tab("1000 clientes que fallan a la vez frente a un servidor que atiende 50 peticiones por segundo",
               "Tabla: el reintento fijo y el exponencial sin dispersión producen 10,5 peticiones por cliente y un pico de 950 por segundo tras el primer segundo, y el segundo tarda 902 segundos en terminar; el exponencial con dispersión completa produce 2 peticiones por cliente, un pico de 484 y termina en 23 segundos.",
               ["Política de reintento", "Peticiones por cliente", "Pico tras el 1.er segundo", "Hasta el último cliente"], rows, [380, 200, 210, 190], row_h=48, size=13,
               note="Sin dispersión, los clientes quedan sincronizados en oleadas que se repiten. Con dispersión se reparten y la carga total baja a una quinta parte. Simulación de capacidad fija sin degradación del servidor: un servidor real puede empeorar bajo carga.",
               note_kind="gold", foot=MODELO)


def se239_a11y() -> Fig:
    rows = [
        ["Contraste insuficiente de un enlace", "Sí", "Se calcula la razón"],
        ["Indicador de foco eliminado", "Sí", "Regla sobre el CSS"],
        ["Campo sin etiqueta", "Sí", "Regla estructural"],
        ["Error sin asociar al campo", "Sí", "aria-describedby ausente"],
        ["tabindex positivo", "Sí", "Regla estructural"],
        ["Enlace «clic aquí»", "Sí", "Lista de textos genéricos"],
        ["Texto alternativo engañoso", "No", "Requiere mirar la imagen"],
        ["Idioma declarado equivocado", "No", "Requiere identificar el idioma del texto"],
        ["Etiqueta que dice otra cosa que el campo", "No", "Requiere entender el propósito"],
    ]
    return tab("Nueve defectos de accesibilidad inyectados: cuáles detecta un conjunto de reglas automáticas",
               "Tabla: de nueve defectos de accesibilidad inyectados en una página sintética, seis se detectan con reglas automáticas, entre ellos el contraste, el foco, las etiquetas y los errores sin asociar, y tres no, porque exigen ver la imagen, identificar el idioma o entender el propósito del campo.",
               ["Defecto inyectado", "¿Lo detecta una regla?", "Por qué"], rows, [400, 190, 350], row_h=40, size=12,
               note="6 de 9 es el resultado de estas nueve reglas sobre estos nueve defectos, no una cobertura general de WCAG. Una herramienta automática real cubre más reglas y falla en otras: la revisión con teclado y lector de pantalla sigue haciendo falta.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-240
def se240_manifiesto() -> Fig:
    rows = [
        ["Falta name, start_url o icons", "27", "27"],
        ["short_name largo, display o color inválidos", "23", "23"],
        ["start_url fuera del scope", "6", "6"],
        ["Sin icono 512 o sin maskable, sizes roto", "27", "27"],
        ["src de un icono que no existe", "11", "0"],
        ["Nombre engañoso o idioma equivocado", "18", "0"],
        ["Icono declarado 192 que mide otra cosa", "8", "0"],
    ]
    return tab("Validador de manifiesto: 120 mutaciones de un manifiesto de aplicación web sintético",
               "Tabla: un validador de forma del manifiesto detecta 83 de 120 mutaciones, todas las que falta o rompen campos, el alcance o los iconos declarados, y no detecta las que exigen comprobar el sistema de archivos o el significado: iconos inexistentes, nombres engañosos, idioma equivocado o iconos de otro tamaño.",
               ["Mutación", "Casos", "Detectadas"], rows, [560, 160, 220], row_h=44, size=12,
               note="Detectadas 83 de 120. Los 37 casos restantes no son defectos del JSON: son discrepancias entre el JSON y el mundo (archivos, significado). Para verlos hay que abrir los archivos referidos y revisar el contenido, no validar el esquema.",
               note_kind="gold", foot=SINT)


def se240_cabeceras() -> Fig:
    rows = [
        ["/app/sw.js", "Cache-Control de un año: el navegador no verá una versión nueva"],
        ["/app/app.css", "no-store en una hoja de estilos sin huella"],
        ["/app/manifest.webmanifest", "Content-Type application/json en vez de application/manifest+json"],
        ["/app/datos.json", "Un año de caché en datos mutables; sin nosniff"],
        ["/app/ayuda/", "HTML sin charset y sin nosniff"],
        ["/app/, app.3f9a1c.js, icons/192.png", "Sin hallazgos"],
    ]
    return tab("Auditoría de cabeceras de un servidor local con ocho rutas y cinco configuraciones erróneas",
               "Tabla: un comprobador que pide ocho rutas a un servidor local en el bucle de retorno encuentra 7 hallazgos en cinco rutas, entre ellos un service worker con caché de un año, una hoja sin caché, un manifiesto con tipo MIME distinto y datos mutables con caché larga.",
               ["Ruta", "Hallazgo"], rows, [330, 610], row_h=44, size=12,
               note="Un servidor Python en 127.0.0.1 con puerto efímero sirvió ocho respuestas de dos bytes; no se tocó ninguna red. Que las cabeceras sean correctas no demuestra que el service worker se actualice: eso solo se ve en un navegador.",
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
