"""Figures for SE-403 to SE-408 (synthetic data with fixed seeds, real file/hash/openssl probes; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); lo que difiere entre sistemas se indica en la figura."


# ---------------------------------------------------------------- SE-403
def se403_segmentacion() -> Fig:
    rows = [
        ["Reparto en 100 cubos de 100 000 usuarios", "mín. 934, máx. 1 081", "esperado 1 000"],
        ["Dos banderas al 10 % con la misma huella (sin sal)", "ambas: 9 821 de 9 821", "independientes: 965"],
        ["Dos banderas al 10 % con la bandera como sal", "ambas: 991", "independientes: 978"],
        ["Ampliar 1 % → 5 % → 25 % → 100 % con huella", "se pierden 0, 0 y 0", "tamaños 1 003, 4 899, 25 116, 100 000"],
        ["Azar por petición al 25 %, 10 peticiones por usuario", "94,1 % ve la función a ratos", "con huella por usuario: 0 %"],
    ]
    return tab("Segmentación por huella de usuario: uniformidad, independencia entre banderas y consistencia al ampliar",
               "Tabla: la huella reparte 100 000 usuarios en cubos de 934 a 1 081 con 1 000 esperados; dos banderas con la misma huella exponen exactamente a los mismos usuarios, y con la bandera como sal se solapan 991 frente a 978 esperados; ampliar el porcentaje no pierde a nadie, mientras que el azar por petición hace que el 94,1 por ciento de los usuarios vea la función a ratos.",
               ["Medida", "Resultado", "Referencia"], rows, [380, 270, 270], row_h=52, size=12,
               note="El chi-cuadrado del reparto es 75,8 con 99 grados de libertad, compatible con uniformidad. Sin la bandera como sal, las banderas no son experimentos independientes: el mismo 10 % de usuarios las recibe todas y cualquier efecto se confunde.",
               note_kind="gold", foot=SINT)


def se403_combinatoria() -> Fig:
    rows = [
        ["4", "16", "6"],
        ["8", "256", "7"],
        ["12", "4 096", "10"],
        ["16", "65 536", "11"],
        ["20", "1 048 576", "11"],
    ]
    return tab("Banderas booleanas independientes: estados posibles y casos que cubren todos los pares (construcción voraz con semilla)",
               "Tabla: con 4 banderas hay 16 estados y 6 casos cubren todos los pares; con 8, 256 estados y 7 casos; con 12, 4 096 y 10; con 16, 65 536 y 11; con 20, más de un millón de estados y 11 casos.",
               ["Banderas", "Estados posibles (2^n)", "Casos para cubrir todos los pares"], rows, [220, 330, 370], row_h=44, size=13,
               note="Cubrir todos los pares es barato y no cubre las interacciones de tres o más banderas ni las dependencias entre ellas (una bandera que solo tiene sentido si otra está activa). Los 11 casos son un resultado de un algoritmo voraz, una cota superior.",
               note_kind="gold", foot=SINT)


def se403_deuda() -> Fig:
    rows = [
        ["Sin política de retirada", "180", "177", "2^180"],
        ["Retirar tras el 100 % con probabilidad 0,10 al mes", "23", "20", "2^23"],
        ["Fecha de caducidad y dueño (probabilidad 0,35 al mes)", "14", "11", "2^14"],
    ]
    return tab("Deuda de banderas tras 60 meses con 3 banderas nuevas por mes",
               "Tabla: sin política de retirada quedan 180 banderas vivas, 177 de ellas ya al cien por cien y por tanto código muerto; con una retirada lenta quedan 23 y 20; con fecha de caducidad y dueño, 14 y 11.",
               ["Política", "Vivas a los 60 meses", "Ya al 100 %", "Estados posibles"], rows, [430, 180, 140, 170], row_h=52, size=12,
               note="Una bandera al 100 % durante meses es una rama muerta que sigue ejecutándose en las pruebas y confundiendo a quien lee. Las probabilidades de retirada son supuestos del autor; el patrón, que la deuda crece linealmente si nadie retira, es robusto.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-404
def se404_deteccion() -> Fig:
    rows = [
        ["1 %", "40/40", "58 s", "268 s", "5"],
        ["5 %", "40/40", "20 s", "63 s", "7"],
        ["10 %", "40/40", "10 s", "40 s", "6"],
        ["25 %", "40/40", "8 s", "20 s", "10"],
        ["50 %", "40/40", "8 s", "17 s", "17"],
    ]
    return tab("Tiempo hasta detectar un defecto que sube el error de 0,5 % a 1,5 % según la fracción de tráfico que recibe el canario",
               "Tabla: con 400 solicitudes por segundo, un canario del 1 por ciento detecta el defecto en una mediana de 58 segundos y un percentil 95 de 268, con 5 errores extra en una mediana; uno del 50 por ciento lo detecta en 8 y 17 segundos pero con 17 errores extra.",
               ["Fracción de tráfico", "Detectado", "Mediana", "Percentil 95", "Errores extra (mediana)"], rows, [190, 150, 150, 170, 260], row_h=44, size=13,
               note="Es un compromiso: un canario pequeño daña a menos usuarios y tarda más en distinguir la señal del ruido. Las diferencias entre filas son medianas de 40 semillas con una prueba de dos proporciones con z = 3.",
               note_kind="gold", foot=SINT)


def se404_alarmas() -> Fig:
    items = [
        ("z = 1,64", 47.0, "coral", "47,0 %"),
        ("z = 2,33", 23.5, "coral", "23,5 %"),
        ("z = 3,00", 9.5, "gold", "9,5 %"),
        ("z = 4,00", 2.0, "teal", "2,0 %"),
    ]
    return bars("Reversiones innecesarias en 200 episodios de 30 minutos sin ningún defecto, según el umbral de la prueba",
                "Barras: sin defecto alguno, un umbral z de 1,64 hace revertir el 47 por ciento de los episodios de 30 minutos; z de 2,33, el 23,5; z de 3, el 9,5; z de 4, el 2.",
                items, 3.6, "Una prueba que se evalúa cada segundo durante 30 minutos recibe cientos de oportunidades de equivocarse: un umbral pensado para una sola decisión produce falsas alarmas. Subir el umbral baja las falsas alarmas y alarga la detección del defecto verdadero.",
                label_w=160, width=900, note_kind="coral", foot=SINT)


def se404_tamano() -> Fig:
    rows = [
        ["+0,10 puntos (0,6 %)", "22/40", "868 s"],
        ["+0,25 puntos (0,75 %)", "40/40", "274 s"],
        ["+0,50 puntos (1,0 %)", "40/40", "69 s"],
        ["+1,00 puntos (1,5 %)", "40/40", "18 s"],
        ["+2,00 puntos (2,5 %)", "40/40", "6 s"],
    ]
    return tab("Canario del 5 %, horizonte de 30 minutos: tamaño del defecto frente a su detección",
               "Tabla: con un canario del 5 por ciento, un defecto que sube el error 0,1 puntos se detecta en 22 de 40 semillas con una mediana de 868 segundos; 0,25 puntos, en 40 de 40 con 274 segundos; 0,5, en 69; 1, en 18; y 2 puntos en 6 segundos.",
               ["Aumento del error (error resultante)", "Detectado en 30 minutos", "Mediana de detección"], rows, [400, 270, 250], row_h=44, size=13,
               note="Existe un defecto demasiado pequeño para este canario y esta ventana: la ausencia de alarma no prueba ausencia de defecto. En blue-green sin migración incompatible el retroceso es un cambio de ruta; con una migración destructiva que ya recibió escrituras nuevas, el retroceso sin perder datos fue posible en el 18,5 % de los casos simulados.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-405
def se405_fallos() -> Fig:
    rows = [
        ["A: sobrescribir en sitio", "7", "0", "6 con mezcla o corrupto, 1 no arranca"],
        ["B: reemplazar cada archivo por separado", "14", "2", "12 con mezcla de versiones"],
        ["C: directorio nuevo y puntero", "9", "9", "0"],
        ["D: como C, con verificación previa", "9", "9", "0"],
    ]
    return tab("Fallo inyectado en cada paso de una actualización de 6 módulos y un manifiesto: estado final de la instalación (archivos reales)",
               "Tabla: sobrescribir en sitio deja 6 de 7 interrupciones con una mezcla corrupta y una que no arranca; reemplazar archivo por archivo deja 12 de 14 con mezcla de versiones; preparar un directorio nuevo y cambiar un puntero deja la versión anterior intacta en las 9 interrupciones, con o sin verificación previa.",
               ["Estrategia", "Puntos de fallo", "Quedan en v1 consistente", "Resto"], rows, [330, 140, 190, 260], row_h=52, size=12,
               note="Sin interrupción las cuatro terminan en v2 consistente; la diferencia está en qué hay después de una interrupción. Con un byte alterado en un módulo descargado, C termina en una instalación corrupta y D la rechaza antes del reemplazo y conserva v1. El experimento simula el corte con una excepción y no desconecta energía ni prueba el comportamiento del sistema de archivos.",
               note_kind="coral", foot="Operaciones reales con archivos temporales; resultado idéntico en Windows y Ubuntu.")


def se405_sesgo() -> Fig:
    rows = [
        ["30", "2", "78,0 %", "0,0 %", "22,0 %", "0,0 %"],
        ["90", "6", "78,0 %", "0,0 %", "10,8 %", "11,2 %"],
        ["180", "12", "88,8 %", "0,0 %", "0,0 %", "11,2 %"],
    ]
    return tab("Sesgo de versiones en 20 000 clientes con un lanzamiento cada 14 días: versiones de retraso",
               "Tabla: a los 30 días con 2 lanzamientos el 78 por ciento está al día y el 22 por ciento lleva 2 o 3 versiones de retraso; a los 90 días con 6 lanzamientos, el 10,8 por ciento lleva 2 o 3 y el 11,2 por ciento 4 o más; a los 180 días con 12 lanzamientos, el 11,2 por ciento lleva 4 o más.",
               ["Día", "Versión actual", "Al día", "1 de retraso", "2–3 de retraso", "4 o más"], rows, [90, 160, 150, 160, 190, 170], row_h=44, size=13,
               note="Los clientes abren la aplicación cada 1, 2, 3, 7, 14, 30, 60 o 120 días (distribución supuesta). Se observaron 22 caminos de actualización distintos y 8 712 de 182 568 actualizaciones saltaron 3 versiones o más: cada camino tiene que haberse probado.",
               note_kind="gold", foot=SINT)


def se405_saltos() -> Fig:
    items = [
        ("Salto de 1 versión", 160536.0, "teal", "160 536"),
        ("Salto de 2 versiones", 13320.0, "gold", "13 320"),
        ("Salto de 4 versiones", 6465.0, "coral", "6 465"),
        ("Salto de 8 versiones", 2247.0, "coral", "2 247"),
    ]
    return bars("Actualizaciones realizadas según cuántas versiones se saltan (20 000 clientes, 180 días)",
                "Barras: de 182 568 actualizaciones, 160 536 saltan una versión, 13 320 saltan dos, 6 465 saltan cuatro y 2 247 saltan ocho versiones.",
                items, 0.0016, "El 4,8 % de las actualizaciones de la simulación salta cuatro o más versiones (y el 12,1 % dos o más); esas son las que ejercitan migraciones que nadie probó en conjunto. Un actualizador que solo admite pasos de una versión obliga a encadenar migraciones; uno que admite saltos obliga a probarlos.",
                label_w=220, width=940, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-406
def se406_real() -> Fig:
    rows = [
        ["pages.yml", "83", "5", "5", "0"],
        ["security.yml", "90", "5", "5", "0"],
        ["validate.yml", "258", "10", "10", "0"],
    ]
    return tab("Escaneo real de los tres workflows de este repositorio con siete reglas",
               "Tabla: los tres workflows del repositorio, de 83, 90 y 258 líneas, usan 5, 5 y 10 acciones, todas fijadas a un SHA de 40 caracteres, y las siete reglas del escáner no producen ningún hallazgo.",
               ["Workflow", "Líneas", "Acciones usadas", "Fijadas a SHA", "Hallazgos"], rows, [250, 130, 210, 190, 140], row_h=44, size=13,
               note="Un escaneo sin hallazgos dice que no hay lo que las reglas buscan, no que el CI sea seguro: el escáner solo lee el texto. El resultado es el mismo en Windows y en Ubuntu porque lee los mismos archivos; es una medición de este repositorio en esta fecha, no una garantía.",
               note_kind="gold", foot=REAL)


def se406_mutaciones() -> Fig:
    rows = [
        ["Desfijar una acción (de SHA a v4)", "15 de 15"],
        ["Quitar permissions de nivel superior", "10 de 10"],
        ["Poner permissions en write-all", "10 de 10"],
        ["Añadir pull_request_target", "15 de 15"],
        ["Interpolar el título del PR en un comando", "15 de 15"],
        ["Añadir curl | bash", "15 de 15"],
        ["Quitar persist-credentials: false", "15 de 15"],
        ["Interpolar un secreto en un comando", "15 de 15"],
        ["Fijar a SHA un repositorio de otro dueño", "0 de 15"],
        ["Fijar a un SHA válido pero malicioso", "0 de 15"],
        ["Añadir un paso con salida de red", "0 de 15"],
    ]
    return tab("Un escáner de reglas frente a 155 mutaciones de los workflows reales (11 operadores)",
               "Tabla: el escáner detecta 15 de 15 mutaciones que desfijan una acción, añaden pull_request_target, interpolan el título del PR o un secreto, añaden curl a bash o quitan persist-credentials, y 10 de 10 de las de permisos, pero ninguna de las 45 que mantienen la forma: fijar un repositorio ajeno, un SHA malicioso o un paso con salida de red.",
               ["Mutación", "Detectadas"], rows, [640, 200], row_h=34, size=13,
               note="Detecta 110 de 155 (71,0 %). Las 45 que se escapan son todas formalmente correctas: están fijadas, con permisos mínimos, y cambian de qué se fía el workflow. Las mutaciones que no cambiaron el texto (permisos ya vacíos) se descartaron.",
               note_kind="coral", foot=SINT)


def se406_alcance() -> Fig:
    rows = [
        ["Permisos de escritura por defecto y secretos como variables del job", "Código, etiquetas, releases, secretos del job y caché"],
        ["permissions: contents: read, sin secretos", "Lectura del código; el artefacto puede alterarse dentro del job"],
        ["permissions: {} arriba y permisos mínimos por job", "Solo lo que ese job necesita; id-token solo en el job de publicación"],
        ["pull_request_target ejecutando código de un fork", "Contexto privilegiado con código no confiable: secretos del repositorio base"],
    ]
    return tab("Alcance de un paso comprometido según la configuración del workflow",
               "Tabla: con permisos de escritura por defecto y secretos en variables, un paso comprometido alcanza el código, las etiquetas, los releases, los secretos del job y la caché; con permisos de solo lectura alcanza la lectura y puede alterar el artefacto; con permisos vacíos y mínimos por job, solo lo que ese job necesita; con pull_request_target y código de un fork, los secretos del repositorio base.",
               ["Configuración", "Qué alcanza un paso comprometido"], rows, [440, 480], row_h=64, size=13,
               note="Es un modelo de alcance a partir de la documentación de GitHub Actions, sin medir ningún ataque. Reducir permisos no evita el compromiso; reduce lo que se pierde cuando ocurre.",
               note_kind="gold", foot="Análisis del autor a partir de la documentación oficial.")


# ---------------------------------------------------------------- SE-407
def se407_detectadas() -> Fig:
    rows = [
        ["Artefacto cambiado, manifiesto intacto", "Huella del artefacto"],
        ["SBOM alterado", "Huella del SBOM"],
        ["Procedencia alterada", "Huella de la procedencia"],
        ["Firma inválida o de otra clave", "Firma del manifiesto"],
        ["Retroceso a una secuencia menor", "Secuencia"],
        ["Manifiesto de otro producto", "Nombre"],
        ["Constructor o repositorio distinto", "Constructor / repositorio esperado"],
        ["Artefacto cambiado y manifiesto re-firmado", "Sujeto de la procedencia ≠ artefacto"],
        ["Bloqueo declarado distinto del usado", "Bloqueo ≠ materiales; SBOM ≠ bloqueo"],
        ["Componente retirado del SBOM y re-firmado", "SBOM ≠ bloqueo"],
    ]
    return tab("Doce manipulaciones de un release firmado y la comprobación que rechaza cada una (verificador de 12 comprobaciones)",
               "Tabla: el verificador rechaza las doce manipulaciones, desde un artefacto cambiado o un SBOM alterado hasta un manifiesto re-firmado con un artefacto distinto o un componente retirado del SBOM, y en cada caso la comprobación que falla es distinta.",
               ["Manipulación", "Comprobación que la rechaza"], rows, [450, 470], row_h=40, size=13,
               note="Doce de doce, con firmas Ed25519 reales de openssl, idéntico en Windows y Ubuntu. Las filas agrupan 12 casos en 10 líneas por espacio. Que el verificador las rechace sirve para las manipulaciones que el autor imaginó; no demuestra que haya cubierto las que no imaginó.",
               note_kind="gold", foot=REAL)


def se407_mentiras() -> Fig:
    rows = [
        ["Código malicioso aprobado y construido por el CI legítimo", "Pasa: todo es coherente", "Revisión de código y reconstrucción desde la fuente revisada"],
        ["Dependencia comprometida declarada en el bloqueo", "Pasa", "Revisión de cambios del bloqueo y escaneo de vulnerabilidades"],
        ["Commit distinto del revisado", "Pasa: el verificador no conoce la revisión", "Registro de revisión firmado y comprobado"],
        ["Clave de firma robada", "Pasa", "Revocación, claves de corta vida, firma sin clave larga"],
        ["Segundo release con la misma versión y secuencia", "Pasa", "Registro transparente que impida reemplazos"],
        ["Procedencia con reproducible=true sin reconstruir", "Pasa (es una afirmación)", "Reconstrucción independiente"],
    ]
    return tab("Seis casos coherentes que el verificador no rechaza y qué haría falta para verlos",
               "Tabla: un código malicioso aprobado, una dependencia comprometida en el bloqueo, un commit distinto del revisado, una clave de firma robada, un segundo release con la misma secuencia y una afirmación de reproducibilidad sin reconstruir pasan las doce comprobaciones; cada uno exige un control distinto fuera del verificador.",
               ["Caso", "Resultado del verificador", "Control que lo vería"], rows, [330, 240, 350], row_h=64, size=12,
               note="Rechaza 0 de 6, y el sexto es el propio release legítimo con una afirmación que nadie comprueba. La integridad y la procedencia se verifican con una cadena de huellas; la confianza en el contenido no sale de ninguna cadena de huellas.",
               note_kind="coral", foot=REAL)


def se407_reconstruccion() -> Fig:
    rows = [
        ["Fuente revisada frente al release legítimo", "Coincide", "Verdadero"],
        ["Fuente revisada frente al release malicioso", "No coincide", "Falso"],
        ["Fuente maliciosa frente al release malicioso", "Coincide", "Verdadero"],
    ]
    return tab("Reconstrucción independiente desde una fuente: qué demuestra y qué no",
               "Tabla: reconstruir desde la fuente revisada coincide con el release legítimo, no coincide con el malicioso, y reconstruir desde la fuente maliciosa coincide con el release malicioso, de modo que reproducible no equivale a benigno.",
               ["Reconstrucción", "Resultado de comparar huellas", "Coincide"], rows, [450, 280, 190], row_h=44, size=13,
               note="Una reconstrucción independiente sobre una fuente conocida y revisada convierte la mentira del primer caso en una discrepancia visible. Si la fuente es la maliciosa, el build reproducible solo reproduce con fidelidad el daño.",
               note_kind="gold", foot=REAL)


# ---------------------------------------------------------------- SE-408
def se408_sistemas() -> Fig:
    rows = [
        ["Construido y firmado en Windows (OpenSSL 3.5.7)", "Sin fallos", "Sin fallos", "802052279bf24eb8"],
        ["Construido y firmado en Ubuntu (OpenSSL 3.0.13)", "Sin fallos", "Sin fallos", "802052279bf24eb8"],
    ]
    return tab("Releases cruzados: cada sistema verifica el release que construyó el otro",
               "Tabla: el release construido y firmado en Windows se verifica sin fallos en Windows y en Ubuntu, el construido en Ubuntu se verifica sin fallos en ambos, y los dos tienen la misma huella de artefacto 802052279bf24eb8.",
               ["Origen", "Verificado en Windows", "Verificado en Ubuntu", "Huella del artefacto"], rows, [350, 190, 190, 190], row_h=52, size=12,
               note="Las claves son distintas en cada origen y las firmas también; lo idéntico es el artefacto, porque el build es reproducible entre sistemas. Verificar una firma con otra versión de openssl es una prueba modesta de interoperabilidad, no de portabilidad de todo el canal.",
               note_kind="gold", foot=REAL)


def se408_simulacros() -> Fig:
    rows = [
        ["Reinstalar el bundle firmado de 1.4.0 tras publicar 1.4.1", "Rechazado: secuencia (retroceso)", "Republicar como 1.4.2 con secuencia 16"],
        ["Perder el repositorio de releases", "Reconstrucción idéntica a la publicada", "Reconstruir desde la fuente y comparar huellas"],
        ["Rotar la clave de firma", "Declaración firmada con la clave vigente; 1.5.0 verifica con la nueva", "Declarar la rotación antes de necesitarla"],
        ["Perder la clave privada sin rotación previa", "Toda versión nueva rechazada por los clientes", "Acción humana por un canal de confianza anterior"],
    ]
    return tab("Cuatro simulacros de recuperación del canal de release y su resultado",
               "Tabla: reinstalar un bundle antiguo firmado es rechazado por la secuencia y se resuelve republicando el mismo contenido como 1.4.2 con secuencia 16; perder el repositorio se resuelve reconstruyendo con la misma huella; rotar la clave funciona si la declaración se firmó con la clave vigente; perder la clave sin rotación previa deja a los clientes rechazando todo.",
               ["Simulacro", "Resultado observado", "Cómo se recupera"], rows, [330, 300, 290], row_h=64, size=12,
               note="Los tres primeros se resuelven con lo que el canal ya tiene; el cuarto es el que no se recupera con automatización: la recuperación de una clave perdida depende de un canal que los clientes ya hayan aceptado. Es un simulacro con un solo proceso y no la operación de un repositorio real.",
               note_kind="coral", foot=REAL)


def se408_tiempos() -> Fig:
    rows = [
        ["Construir, generar SBOM y procedencia y firmar 1.4.0", "42,7 ms", "7,3 ms"],
        ["Republicar el contenido de 1.4.0 como 1.4.2", "45,4 ms", "7,1 ms"],
        ["Reconstruir 1.4.0 desde la fuente y comparar", "0,7 ms", "0,8 ms"],
    ]
    return tab("Costo medido de los pasos del canal sintético de release (una lectura por celda)",
               "Tabla: construir, generar SBOM y procedencia y firmar toma 42,7 milisegundos en Windows y 7,3 en Ubuntu; republicar el contenido anterior con una nueva secuencia, 45,4 y 7,1; reconstruir y comparar, 0,7 y 0,8.",
               ["Paso", "Windows 11", "Ubuntu WSL2"], rows, [510, 200, 200], row_h=52, size=13,
               note="El árbol sintético tiene 42 archivos de unos cientos de bytes; el costo de un proyecto real lo dominan la compilación y la descarga de dependencias, no la firma. Las cifras cambian en cada ejecución y entre equipos; las diferencias entre sistemas reflejan sobre todo el arranque de procesos de openssl.",
               note_kind="gold", foot="Mediciones de reloj: una lectura por celda, no reproducibles al milisegundo.")


FIGURES = {
    "se-403-segmentacion-por-huella.svg": se403_segmentacion,
    "se-403-combinatoria-de-banderas.svg": se403_combinatoria,
    "se-403-deuda-de-banderas.svg": se403_deuda,
    "se-404-deteccion-segun-canario.svg": se404_deteccion,
    "se-404-falsas-alarmas.svg": se404_alarmas,
    "se-404-tamano-del-defecto.svg": se404_tamano,
    "se-405-fallo-en-cada-paso.svg": se405_fallos,
    "se-405-sesgo-de-versiones.svg": se405_sesgo,
    "se-405-saltos-de-version.svg": se405_saltos,
    "se-406-workflows-reales.svg": se406_real,
    "se-406-escaner-frente-a-mutaciones.svg": se406_mutaciones,
    "se-406-alcance-de-un-paso-comprometido.svg": se406_alcance,
    "se-407-manipulaciones-detectadas.svg": se407_detectadas,
    "se-407-mentiras-coherentes.svg": se407_mentiras,
    "se-407-reconstruccion-independiente.svg": se407_reconstruccion,
    "se-408-verificacion-entre-sistemas.svg": se408_sistemas,
    "se-408-simulacros-de-recuperacion.svg": se408_simulacros,
    "se-408-costo-del-canal.svg": se408_tiempos,
}
