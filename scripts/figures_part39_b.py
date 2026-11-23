"""Figures for SE-475 to SE-480 (synthetic data with fixed seeds, real file/hash/openssl probes; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars
from figure_diagrams import fan, merge
from figures_part07_a import bars


SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); lo que difiere entre sistemas se indica en la figura."


# ---------------------------------------------------------------- SE-475
def se403_segmentacion() -> Fig:
    return grouped_bars(
        'Segmentación por huella de usuario: uniformidad, independencia entre banderas y consistencia al ampliar',
        "Barras agrupadas con los usuarios expuestos a dos banderas al 10 por ciento sobre 100 000: con la misma huella y sin sal los expuestos a ambas son 9 821, los mismos para las dos, frente a 965 si fueran independientes; con la bandera como sal son 991 frente a 978.",
        ["Misma huella, sin sal", "La bandera como sal"],
        [("Expuestos a ambas banderas", [9821, 991], "coral"), ("Esperados si fueran independientes", [965, 978], "teal")],
        unit="Usuarios de 100 000",
        note='El chi-cuadrado del reparto es 75,8 con 99 grados de libertad, compatible con uniformidad. Sin la bandera como sal, las banderas no son experimentos independientes: el mismo 10 % de usuarios las recibe todas y cualquier efecto se confunde.', note_kind='gold', foot=SINT)


def se403_combinatoria() -> Fig:
    return line_chart(
        'Banderas booleanas independientes: estados posibles y casos que cubren todos los pares (construcción voraz con semilla)',
        "Líneas en escala logarítmica con los estados posibles de banderas booleanas independientes y los casos que cubren todos los pares: 4 banderas dan 16 estados y 6 casos, 8 dan 256 y 7, 12 dan 4 096 y 10, 16 dan 65 536 y 11 y 20 dan 1 048 576 estados y 11 casos.",
        [("Estados posibles (2ⁿ)", [(4, 16, "16", "t"), (8, 256, "256", "t"), (12, 4096, "4 096", "t"), (16, 65536, "65 536", "t"), (20, 1048576, "1 048 576", "l")], "coral"),
         ("Casos que cubren todos los pares", [(4, 6, "6", "b"), (8, 7, "7", "b"), (12, 10, "10", "t"), (16, 11, "11", "b"), (20, 11, "11", "t")], "teal")],
        x_label="Banderas booleanas", y_label="Estados o casos", log_y=True,
        x_ticks=[(4, "4"), (8, "8"), (12, "12"), (16, "16"), (20, "20"), (22, "")], y_ticks=[1, 10, 100, 1000, 10000, 100000, 1000000], point_labels="none",
        note='Cubrir todos los pares es barato y no cubre las interacciones de tres o más banderas ni las dependencias entre ellas (una bandera que solo tiene sentido si otra está activa). Los 11 casos son un resultado de un algoritmo voraz, una cota superior.', note_kind='gold', foot=SINT)


def se403_deuda() -> Fig:
    return grouped_bars(
        'Deuda de banderas tras 60 meses con 3 banderas nuevas por mes',
        "Barras agrupadas con la deuda de banderas tras 60 meses con 3 banderas nuevas por mes: sin política de retirada quedan 180 vivas y 177 ya al cien por cien, código muerto; con una retirada lenta quedan 23 y 20; con fecha de caducidad y dueño 14 y 11.",
        ["Sin política de retirada", "Retirar tras el 100 % (0,10 al mes)", "Fecha de caducidad y dueño (0,35 al mes)"],
        [("Vivas a los 60 meses", [180, 23, 14], "coral"), ("Ya al 100 %", [177, 20, 11], "gold")],
        unit="Banderas",
        note='Una bandera al 100 % durante meses es una rama muerta que sigue ejecutándose en las pruebas y confundiendo a quien lee. Las probabilidades de retirada son supuestos del autor; el patrón, que la deuda crece linealmente si nadie retira, es robusto.', note_kind='coral', foot=SINT)


# ---------------------------------------------------------------- SE-476
def se404_deteccion() -> Fig:
    return line_chart(
        'Tiempo hasta detectar un defecto que sube el error de 0,5 % a 1,5 % según la fracción de tráfico que recibe el canario',
        "Líneas en escalas logarítmicas con el tiempo hasta detectar un defecto que sube el error de 0,5 a 1,5 por ciento según la fracción de tráfico del canario: la mediana baja de 58 s con el 1 por ciento a 8 s con el 50 y el percentil 95 de 268 s a 17 s; se detecta en 40 de 40 semillas en todos los casos.",
        [("Percentil 95", [(1, 268, "268", "t"), (5, 63, "63", "t"), (10, 40, "40", "t"), (25, 20, "20", "t"), (50, 17, "17", "t")], "coral"),
         ("Mediana", [(1, 58, "58", "b"), (5, 20, "20", "b"), (10, 10, "10", "b"), (25, 8, "8", "b"), (50, 8, "8", "b")], "teal")],
        x_label="Fracción de tráfico que recibe el canario (%)", y_label="Tiempo hasta detectar (s)", log_x=True, log_y=True,
        x_ticks=[(1, "1 %"), (5, "5 %"), (10, "10 %"), (25, "25 %"), (50, "50 %")], y_ticks=[1, 10, 100, 1000], point_labels="none",
        note='Es un compromiso: un canario pequeño daña a menos usuarios y tarda más en distinguir la señal del ruido. Las diferencias entre fracciones son medianas de 40 semillas con una prueba de dos proporciones con z = 3.', note_kind='gold', foot=SINT)


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
    return line_chart(
        'Canario del 5 %, horizonte de 30 minutos: tamaño del defecto frente a su detección',
        "Línea en escalas logarítmicas con la mediana de detección de un canario del 5 por ciento según el aumento del error: 868 s con 0,10 puntos, solo detectado en 22 de 40 semillas, 274 s con 0,25, 69 s con 0,5, 18 s con 1,0 y 6 s con 2,0, con 40 de 40 detecciones desde 0,25.",
        [("Mediana de detección", [(0.10, 868, "868 s · 22 de 40", "r"), (0.25, 274, "274 s", "t"), (0.5, 69, "69 s", "t"), (1.0, 18, "18 s", "t"), (2.0, 6, "6 s", "t")], "coral")],
        x_label="Aumento del error (puntos porcentuales)", y_label="Mediana de detección (s)", log_x=True, log_y=True,
        x_ticks=[(0.1, "0,10"), (0.25, "0,25"), (0.5, "0,5"), (1.0, "1,0"), (2.0, "2,0"), (4.0, "")], y_ticks=[1, 10, 100, 1000], point_labels="none",
        note='Existe un defecto demasiado pequeño para este canario y esta ventana: la ausencia de alarma no prueba ausencia de defecto. En blue-green sin migración incompatible el retroceso es un cambio de ruta; con una migración destructiva que ya recibió escrituras nuevas, el retroceso sin perder datos fue posible en el 18,5 % de los casos simulados.', note_kind='gold', foot=SINT)


# ---------------------------------------------------------------- SE-477
def se405_fallos() -> Fig:
    return grouped_bars(
        'Fallo inyectado en cada paso de una actualización de 6 módulos y un manifiesto: estado final de la instalación (archivos reales)',
        "Barras agrupadas con los puntos de fallo inyectados en cada estrategia de actualización de 6 módulos y un manifiesto y los que dejan la instalación en la versión 1 consistente: sobrescribir en sitio deja 0 de 7, reemplazar archivo por archivo 2 de 14 y las estrategias con directorio nuevo y puntero, con o sin verificación previa, 9 de 9.",
        ["A: sobrescribir en sitio", "B: reemplazar cada archivo por separado", "C: directorio nuevo y puntero", "D: como C, con verificación previa"],
        [("Puntos de fallo", [7, 14, 9, 9], "grey"), ("Quedan en v1 consistente", [0, 2, 9, 9], "teal")],
        unit="Puntos de fallo inyectados", ticks=[0, 4, 8, 12, 16],
        note='Sin interrupción las cuatro terminan en v2 consistente; la diferencia está en qué hay después de una interrupción. Con un byte alterado en un módulo descargado, C termina en una instalación corrupta y D la rechaza antes del reemplazo y conserva v1. El experimento simula el corte con una excepción y no desconecta energía ni prueba el comportamiento del sistema de archivos.', note_kind='coral', foot="Operaciones reales con archivos temporales; resultado idéntico en Windows y Ubuntu.")


def se405_sesgo() -> Fig:
    return stacked_bars(
        'Sesgo de versiones en 20 000 clientes con un lanzamiento cada 14 días: versiones de retraso',
        "Barras apiladas con las versiones de retraso de 20 000 clientes con un lanzamiento cada 14 días: a los 30 días el 78,0 por ciento está al día y el 22,0 lleva 2 o 3 de retraso; a los 90 días el 78,0 está al día, el 10,8 lleva 2 o 3 y el 11,2 lleva 4 o más; a los 180 días el 88,8 está al día y el 11,2 lleva 4 o más.",
        ["Día 30 (versión actual 2)", "Día 90 (versión actual 6)", "Día 180 (versión actual 12)"],
        [("Al día", [78.0, 78.0, 88.8], "teal"), ("1 de retraso", [0, 0, 0], "grey"), ("2–3 de retraso", [22.0, 10.8, 0], "gold"), ("4 o más", [0, 11.2, 11.2], "coral")],
        unit="% de los clientes", horizontal=True, label_w=220, decimals=1,
        note='Los clientes abren la aplicación cada 1, 2, 3, 7, 14, 30, 60 o 120 días (distribución supuesta). Se observaron 22 caminos de actualización distintos y 8 712 de 182 568 actualizaciones saltaron 3 versiones o más: cada camino tiene que haberse probado.', note_kind='gold', foot=SINT)


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


# ---------------------------------------------------------------- SE-478
def se406_real() -> Fig:
    return grouped_bars(
        'Escaneo real de los tres workflows de este repositorio con siete reglas',
        "Barras agrupadas con las acciones que usa cada uno de los tres workflows del repositorio y las que están fijadas a un SHA de 40 caracteres: 5 de 5 en pages.yml, 5 de 5 en security.yml y 10 de 10 en validate.yml; las siete reglas del escáner no producen ningún hallazgo.",
        ["pages.yml (83 líneas)", "security.yml (90 líneas)", "validate.yml (258 líneas)"],
        [("Acciones usadas", [5, 5, 10], "grey"), ("Fijadas a SHA", [5, 5, 10], "teal")],
        unit="Acciones", ticks=[0, 2, 4, 6, 8, 10, 12],
        note='Un escaneo sin hallazgos dice que no hay lo que las reglas buscan, no que el CI sea seguro: el escáner solo lee el texto. El resultado es el mismo en Windows y en Ubuntu porque lee los mismos archivos; es una medición de este repositorio en esta fecha, no una garantía.', note_kind='gold', foot=REAL)


def se406_mutaciones() -> Fig:
    return grouped_bars(
        'Un escáner de reglas frente a 155 mutaciones de los workflows reales (11 operadores)',
        "Barras horizontales con las mutaciones inyectadas y detectadas por un escáner de reglas en los workflows reales: detecta todas las que desfijan una acción, quitan permissions o los ponen en write-all, añaden pull_request_target, interpolan el título del PR o un secreto, añaden curl a bash o quitan persist-credentials, y ninguna de las tres que mantienen la forma.",
        ["Desfijar una acción (de SHA a v4)", "Quitar permissions de nivel superior", "Poner permissions en write-all", "Añadir pull_request_target", "Interpolar el título del PR en un comando", "Añadir curl | bash",
         "Quitar persist-credentials: false", "Interpolar un secreto en un comando", "Fijar a SHA un repositorio de otro dueño", "Fijar a un SHA válido pero malicioso", "Añadir un paso con salida de red"],
        [("Inyectadas", [15, 10, 10, 15, 15, 15, 15, 15, 15, 15, 15], "grey"), ("Detectadas", [15, 10, 10, 15, 15, 15, 15, 15, 0, 0, 0], "teal")],
        unit="Mutaciones", horizontal=True, label_w=270, ticks=[0, 5, 10, 15],
        note='Detecta 110 de 155 (71,0 %). Las 45 que se escapan son todas formalmente correctas: están fijadas, con permisos mínimos, y cambian de qué se fía el workflow. Las mutaciones que no cambiaron el texto (permisos ya vacíos) se descartaron.', note_kind='coral', foot=SINT)


def se406_alcance() -> Fig:
    return fan(
        'Alcance de un paso comprometido según la configuración del workflow',
        "Diagrama de lo que alcanza un paso comprometido según la configuración del workflow: con permisos de escritura por defecto y secretos como variables alcanza código, etiquetas, releases, secretos del job y caché; con solo lectura alcanza la lectura del código; con permisos mínimos por job solo lo que ese job necesita; con pull_request_target sobre un fork, los secretos del repositorio base.",
        ("Un paso del workflow queda comprometido", "qué alcanza depende de la configuración", "navy"),
        [("Permisos de escritura por defecto y secretos como variables del job", "código, etiquetas, releases, secretos del job y caché", "coral"),
         ("permissions: contents: read, sin secretos", "lectura del código; el artefacto puede alterarse dentro del job", "gold"),
         ("permissions: {} arriba y permisos mínimos por job", "solo lo que ese job necesita; id-token solo en el job de publicación", "teal"),
         ("pull_request_target ejecutando código de un fork", "contexto privilegiado con código no confiable: secretos del repositorio base", "coral")],
        note='Es un modelo de alcance a partir de la documentación de GitHub Actions, sin medir ningún ataque. Reducir permisos no evita el compromiso; reduce lo que se pierde cuando ocurre.', note_kind='gold', foot="Análisis del autor a partir de la documentación oficial.")


# ---------------------------------------------------------------- SE-479
def se407_detectadas() -> Fig:
    return merge(
        'Doce manipulaciones de un release firmado y la comprobación que rechaza cada una (verificador de 12 comprobaciones)',
        "Diagrama de diez de las doce manipulaciones de un release firmado y la comprobación del verificador que rechaza cada una, desde el artefacto cambiado con el manifiesto intacto hasta el componente retirado del SBOM y re-firmado; el verificador de 12 comprobaciones rechaza las doce.",
        [("Artefacto cambiado, manifiesto intacto", "rechaza: huella del artefacto", "plain"), ("SBOM alterado", "rechaza: huella del SBOM", "plain"), ("Procedencia alterada", "rechaza: huella de la procedencia", "plain"),
         ("Firma inválida o de otra clave", "rechaza: firma del manifiesto", "plain"), ("Retroceso a una secuencia menor", "rechaza: secuencia", "plain"), ("Manifiesto de otro producto", "rechaza: nombre", "plain"),
         ("Constructor o repositorio distinto", "rechaza: constructor o repositorio esperado", "plain"), ("Artefacto cambiado y manifiesto re-firmado", "rechaza: sujeto de la procedencia ≠ artefacto", "plain"),
         ("Bloqueo declarado distinto del usado", "rechaza: bloqueo ≠ materiales; SBOM ≠ bloqueo", "plain"), ("Componente retirado del SBOM y re-firmado", "rechaza: SBOM ≠ bloqueo", "plain")],
        ("Verificador de 12 comprobaciones", "rechaza las doce manipulaciones", "teal"),
        note='Doce de doce, con firmas Ed25519 reales de openssl, idéntico en Windows y Ubuntu. Las cajas agrupan 12 casos en 10 por espacio. Que el verificador las rechace sirve para las manipulaciones que el autor imaginó; no demuestra que haya cubierto las que no imaginó.', note_kind='gold', foot=REAL)


def se407_mentiras() -> Fig:
    return fan(
        'Seis casos coherentes que el verificador no rechaza y qué haría falta para verlos',
        "Diagrama de seis casos coherentes que el verificador no rechaza y el control que haría falta para verlos: código malicioso aprobado, dependencia comprometida en el bloqueo, commit distinto del revisado, clave de firma robada, segundo release con la misma secuencia y procedencia con reproducible igual a true sin reconstruir.",
        ("Release coherente que el verificador no rechaza", "todo pasa; cada caso necesita otro control", "navy"),
        [("Código malicioso aprobado y construido por el CI legítimo", "pasa, todo es coherente · control: revisión de código y reconstrucción desde la fuente revisada", "coral"),
         ("Dependencia comprometida declarada en el bloqueo", "pasa · control: revisión de cambios del bloqueo y escaneo de vulnerabilidades", "coral"),
         ("Commit distinto del revisado", "pasa, el verificador no conoce la revisión · control: registro de revisión firmado y comprobado", "coral"),
         ("Clave de firma robada", "pasa · control: revocación, claves de corta vida, firma sin clave larga", "coral"),
         ("Segundo release con la misma versión y secuencia", "pasa · control: registro transparente que impida reemplazos", "coral"),
         ("Procedencia con reproducible=true sin reconstruir", "pasa, es una afirmación · control: reconstrucción independiente", "coral")],
        note='Rechaza 0 de 6, y el sexto es el propio release legítimo con una afirmación que nadie comprueba. La integridad y la procedencia se verifican con una cadena de huellas; la confianza en el contenido no sale de ninguna cadena de huellas.', note_kind='coral', foot=REAL)


def se407_reconstruccion() -> Fig:
    return fan(
        'Reconstrucción independiente desde una fuente: qué demuestra y qué no',
        "Diagrama de tres reconstrucciones independientes: la fuente revisada coincide con el release legítimo, no coincide con el malicioso, y la fuente maliciosa coincide con el release malicioso, de modo que reproducible no equivale a legítimo.",
        ("Reconstruir desde una fuente y comparar huellas", "qué demuestra y qué no", "navy"),
        [("Fuente revisada frente al release legítimo", "coincide: verdadero", "teal"),
         ("Fuente revisada frente al release malicioso", "no coincide: falso, se delata la manipulación", "teal"),
         ("Fuente maliciosa frente al release malicioso", "coincide: verdadero, pero reproducible no equivale a legítimo", "coral")],
        note='Una reconstrucción independiente sobre una fuente conocida y revisada convierte la mentira del primer caso en una discrepancia visible. Si la fuente es la maliciosa, el build reproducible solo reproduce con fidelidad el daño.', note_kind='gold', foot=REAL)


# ---------------------------------------------------------------- SE-480
def se408_sistemas() -> Fig:
    return fan(
        'Releases cruzados: cada sistema verifica el release que construyó el otro',
        "Diagrama de los releases cruzados: el release construido y firmado en Windows con OpenSSL 3.5.7 se verifica sin fallos en Windows y en Ubuntu, el construido en Ubuntu con OpenSSL 3.0.13 se verifica sin fallos en ambos, y los dos tienen la misma huella de artefacto, 802052279bf24eb8.",
        ("Cada sistema verifica el release del otro", "misma huella de artefacto: 802052279bf24eb8", "navy"),
        [("Construido y firmado en Windows (OpenSSL 3.5.7)", "verificado en Windows: sin fallos · verificado en Ubuntu: sin fallos", "teal"),
         ("Construido y firmado en Ubuntu (OpenSSL 3.0.13)", "verificado en Windows: sin fallos · verificado en Ubuntu: sin fallos", "teal")],
        note='Las claves son distintas en cada origen y las firmas también; lo idéntico es el artefacto, porque el build es reproducible entre sistemas. Verificar una firma con otra versión de openssl es una prueba modesta de interoperabilidad, no de portabilidad de todo el canal.', note_kind='gold', foot=REAL)


def se408_simulacros() -> Fig:
    return fan(
        'Cuatro simulacros de recuperación del canal de release y su resultado',
        "Diagrama de cuatro simulacros de recuperación del canal de release: reinstalar un bundle antiguo es rechazado por la secuencia y se republica como 1.4.2 con secuencia 16; perder el repositorio se resuelve reconstruyendo con la misma huella; rotar la clave se declara antes de necesitarla; perder la clave sin rotación previa deja rechazadas todas las versiones nuevas.",
        ("Simulacros de recuperación del canal de release", "resultado observado y cómo se recupera", "navy"),
        [("Reinstalar el bundle firmado de 1.4.0 tras publicar 1.4.1", "rechazado por la secuencia (retroceso) · republicar como 1.4.2 con secuencia 16", "teal"),
         ("Perder el repositorio de releases", "reconstrucción idéntica a la publicada · reconstruir desde la fuente y comparar huellas", "teal"),
         ("Rotar la clave de firma", "declaración firmada con la clave vigente; 1.5.0 verifica con la nueva · declarar la rotación antes de necesitarla", "gold"),
         ("Perder la clave privada sin rotación previa", "toda versión nueva rechazada por los clientes · acción humana por un canal de confianza anterior", "coral")],
        note='Los tres primeros se resuelven con lo que el canal ya tiene; el cuarto es el que no se recupera con automatización: la recuperación de una clave perdida depende de un canal que los clientes ya hayan aceptado. Es un simulacro con un solo proceso y no la operación de un repositorio real.', note_kind='coral', foot=REAL)


def se408_tiempos() -> Fig:
    return grouped_bars(
        'Costo medido de los pasos del canal sintético de release (una lectura por barra)',
        "Barras horizontales con el tiempo de los pasos del canal sintético de release en Windows y en Ubuntu, una lectura por barra: construir, generar SBOM y procedencia y firmar toma 42,7 y 7,3 ms; republicar con nueva secuencia 45,4 y 7,1; reconstruir y comparar 0,7 y 0,8.",
        ["Construir, generar SBOM y procedencia y firmar 1.4.0", "Republicar el contenido de 1.4.0 como 1.4.2", "Reconstruir 1.4.0 desde la fuente y comparar"],
        [("Windows 11", [42.7, 45.4, 0.7], "coral"), ("Ubuntu WSL2", [7.3, 7.1, 0.8], "teal")],
        unit="Tiempo (ms)", horizontal=True, label_w=290, decimals=1,
        note='El árbol sintético tiene 42 archivos de unos cientos de bytes; el costo de un proyecto real lo dominan la compilación y la descarga de dependencias, no la firma. Las cifras cambian en cada ejecución y entre equipos; las diferencias entre sistemas reflejan sobre todo el arranque de procesos de openssl.', note_kind='gold', foot="Mediciones de reloj: una lectura por barra, no reproducibles al milisegundo.")


FIGURES = {
    "se-475-segmentacion-por-huella.svg": se403_segmentacion,
    "se-475-combinatoria-de-banderas.svg": se403_combinatoria,
    "se-475-deuda-de-banderas.svg": se403_deuda,
    "se-476-deteccion-segun-canario.svg": se404_deteccion,
    "se-476-falsas-alarmas.svg": se404_alarmas,
    "se-476-tamano-del-defecto.svg": se404_tamano,
    "se-477-fallo-en-cada-paso.svg": se405_fallos,
    "se-477-sesgo-de-versiones.svg": se405_sesgo,
    "se-477-saltos-de-version.svg": se405_saltos,
    "se-478-workflows-reales.svg": se406_real,
    "se-478-escaner-frente-a-mutaciones.svg": se406_mutaciones,
    "se-478-alcance-de-un-paso-comprometido.svg": se406_alcance,
    "se-479-manipulaciones-detectadas.svg": se407_detectadas,
    "se-479-mentiras-coherentes.svg": se407_mentiras,
    "se-479-reconstruccion-independiente.svg": se407_reconstruccion,
    "se-480-verificacion-entre-sistemas.svg": se408_sistemas,
    "se-480-simulacros-de-recuperacion.svg": se408_simulacros,
    "se-480-costo-del-canal.svg": se408_tiempos,
}
