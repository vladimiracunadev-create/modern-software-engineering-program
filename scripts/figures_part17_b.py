"""Figures for SE-211 to SE-216 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time is shown)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-211
def se211_idempotencia() -> Fig:
    rows = [["Añadir una línea al archivo de configuración", "Difiere", "Se duplica la línea"], ["Subir una réplica", "Difiere", "Cada repetición suma otra"],
            ["Poner el modo mantenimiento", "Igual", "Fija un valor"], ["Crear el usuario temporal", "Falla", "«ya existe»: aborta el procedimiento"],
            ["Vaciar la cola", "Igual", "Fija un valor"], ["Rotar el registro", "Difiere", "Cada repetición añade 120 líneas"],
            ["Fijar 3 réplicas", "Igual", "Fija un valor"], ["Volver al modo normal", "Igual", "Fija un valor"]]
    return tab("Ejecutar cada paso de un runbook dos veces: ¿queda el mismo estado?",
               "Tabla de ocho pasos ejecutados dos veces sobre un estado simulado: cuatro dejan el mismo estado, tres lo cambian (añadir una línea, subir una réplica, rotar el registro) y uno falla al repetirse (crear el usuario temporal); reanudar desde el paso interrumpido acierta las 8 veces y volver a empezar solo 1.",
               ["Paso del runbook", "Segunda ejecución", "Por qué"], rows, [450, 190, 310], row_h=36, size=12,
               note="Reanudar desde el paso k deja el estado esperado en las 8 interrupciones posibles; volver a empezar solo en 1 (la interrupción antes del primer paso). Un runbook es seguro de repetir cuando sus pasos fijan valores en lugar de añadir cambios. Estado y pasos escritos por el autor.",
               note_kind="gold", foot=SINT)


def se211_cola() -> Fig:
    items = [
        ("Runbooks para los 4 síntomas más frecuentes", 50.8, "coral", "50,8 % de los incidentes"),
        ("8 síntomas", 62.9, "gold", "62,9 %"),
        ("16 síntomas", 73.9, "gold", "73,9 %"),
        ("32 síntomas (la mitad de los tipos)", 83.4, "teal", "83,4 %"),
        ("Techo: 8 % de incidentes de tipo nuevo", 92.0, "grey", "92 % como máximo"),
    ]
    return bars("Qué fracción de los incidentes cubren los primeros k runbooks (64 tipos, reparto de Zipf)",
                "Barras con la cobertura de 300 incidentes simulados repetidos 200 veces: 4 runbooks cubren el 50,8 por ciento, 8 el 62,9, 16 el 73,9, 32 el 83,4; el 8 por ciento de incidentes de tipo nuevo no está cubierto por ninguno.",
                items, 0.9, "Los primeros runbooks rinden mucho y los siguientes cada vez menos: de 16 a 32 hacen falta el doble de documentos para ganar 9,5 puntos. El reparto de Zipf con exponente 1,2 y el 8 % de incidentes nuevos son supuestos; en una organización real se estiman con su propio historial de incidentes.",
                label_w=360, width=1060, note_kind="gold", foot=SINT)


def se211_lint() -> Fig:
    rows = [["Orden destructiva (`rm -rf`)", "3", "3", "Detectada"], ["Contraseña en el texto", "9", "9", "Detectada"], ["Dirección IP interna", "5", "5", "Detectada"],
            ["Advertencia «nunca ejecutes `rm -rf`»", "10", "10", "Falsa alarma: es una advertencia"], ["Orden ofuscada (`r''m -rf`)", "6", "0", "No detectada"], ["Runbook limpio", "7", "0", "Sin falsas alarmas"]]
    return tab("Un linter de runbooks sobre 40 textos con riesgos sembrados",
               "Tabla de un linter por expresiones regulares sobre 40 runbooks: detecta las 3 órdenes destructivas, las 9 contraseñas y las 5 direcciones internas, marca 10 advertencias inocentes como peligro, no ve 6 órdenes ofuscadas y no da alarma en 7 runbooks limpios.",
               ["Caso", "Runbooks", "Marcados", "Lectura"], rows, [370, 120, 120, 340], row_h=42, size=12,
               note="Una regla léxica no distingue ejecutar de advertir contra ejecutar, y se salta lo que se escribe distinto. Sirve como red antes de la revisión humana, no como garantía; cada patrón nuevo se justifica con un caso real que se coló.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-212
def se212_enlaces() -> Fig:
    rows = [["Corpus original, 60 archivos y 480 enlaces", "0", "0", "—"], ["Mismo corpus, leyendo también el interior de bloques de código", "60", "0", "60 falsos positivos"],
            ["Tras renombrar 5 archivos y 8 encabezados", "52", "14", "66 enlaces rotos reales"]]
    return tab("Comprobador de enlaces de un corpus de 60 archivos Markdown",
               "Tabla de un comprobador de enlaces: el corpus original no tiene enlaces rotos; si el comprobador lee el interior de los bloques de código marca 60 enlaces de ejemplo como rotos; tras renombrar 5 archivos y 8 encabezados aparecen 52 enlaces a archivo rotos y 14 anclas rotas.",
               ["Situación", "Archivos rotos", "Anclas rotas", "Lectura"], rows, [400, 160, 150, 240], row_h=48, size=12,
               note="Cinco renombrados rompen 52 enlaces, más de diez por cambio: un enlace roto rara vez viene solo. Y el comprobador ingenuo genera el doble de ruido que el cambio real. La ancla de un encabezado depende de la regla de generación de identificadores, que cambia entre renderizadores.",
               note_kind="gold", foot=SINT)


def se212_determinismo() -> Fig:
    rows = [["Etiquetas en el orden de un conjunto", "8", "Cada ejecución produce una página distinta"], ["Orden de conjunto y fecha de la ejecución", "8", "Además cambia con el reloj"],
            ["Etiquetas ordenadas y fecha fija", "1", "Misma huella en las 8 semillas"], ["Ordenadas, salto de línea CRLF en lugar de LF", "1", "Misma estructura, otra huella que la de LF"]]
    return tab("Huellas distintas al construir la misma página con 8 semillas de hash",
               "Tabla de una página generada con 8 valores de PYTHONHASHSEED: con etiquetas en orden de conjunto salen 8 huellas distintas, añadiendo la fecha de ejecución también 8, con orden explícito y fecha fija una sola; cambiar LF por CRLF cambia la huella aunque la estructura sea idéntica.",
               ["Variante del generador", "Huellas distintas en 8 ejecuciones", "Lectura"], rows, [380, 190, 380], row_h=50, size=12,
               note="Una construcción reproducible es la condición para que «reconstruir y comparar» sirva como prueba. Los saltos de línea cuentan: un mismo generador en Windows y Ubuntu produce huellas distintas si no fija la salida a LF.",
               note_kind="teal", foot=SINT)


def se212_vallas() -> Fig:
    items = [
        ("Linter que lee el interior de los bloques de código", 102, "coral", "102 avisos"),
        ("Linter que respeta las vallas de código", 5, "teal", "5 avisos"),
        ("Defectos reales sembrados", 5, "grey", "5"),
    ]
    return bars("Avisos de un linter de Markdown sobre 40 archivos, 5 con un salto de encabezado real",
                "Barras: un linter que lee también el interior de los bloques de código da 102 avisos sobre 40 archivos; el que respeta las vallas de código da 5, exactamente los 5 saltos de encabezado reales sembrados.",
                items, 4.2, "Los comentarios de shell empiezan por almohadilla y parecen encabezados; las líneas largas de un comando parecen texto. 97 de 102 avisos eran falsos. Un linter que se ignora por ruidoso protege menos que ninguno, de modo que la regla que respeta el contexto es parte de la regla.",
                label_w=430, width=1020, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-213
def se213_busqueda() -> Fig:
    items = [
        ("Búsqueda por la palabra tal cual: acierta en las 3 primeras", 80.8, "coral", "80,8 %"),
        ("Búsqueda por la palabra tal cual: acierta en la primera", 78.8, "coral", "78,8 %"),
        ("Sinónimos del glosario en los metadatos de cada página", 100, "teal", "100 % / 100 %"),
        ("Se amplía la consulta con los sinónimos", 100, "teal", "100 % / 100 %"),
    ]
    return bars("Búsqueda BM25 sobre 200 páginas y 40 conceptos con tres sinónimos (600 consultas)",
                "Barras: con búsqueda léxica BM25 y el lector usando uno de tres sinónimos al azar, una página relevante aparece entre las tres primeras el 80,8 por ciento de las veces y en primer lugar el 78,8; con los sinónimos en los metadatos o ampliando la consulta, el 100 por ciento.",
                items, 3.4, "Una de cada cinco consultas fracasa solo porque el lector no usa el mismo nombre que la página. El glosario corrige eso de forma barata. El 100 % es consecuencia de un vocabulario cerrado de 40 conceptos y 3 sinónimos exactos; en un corpus real los sinónimos no se enumeran del todo.",
                label_w=460, width=1060, note_kind="gold", foot=SINT)


def se213_glosario() -> Fig:
    rows = [["0,5", "0 de 240", "0 de 240"], ["0,7", "0 de 240", "240 de 240"], ["0,9", "240 de 240", "240 de 240"]]
    return tab("Detectar definiciones contradictorias por similitud de palabras (240 pares de cada clase)",
               "Tabla de 240 pares de definiciones parafraseadas y 240 contradictorias: la similitud media de Jaccard es 0,65 en las paráfrasis y 0,87 en las contradicciones; con umbral 0,5 no se marca ninguna de las dos clases, con 0,7 se marcan todas las paráfrasis y ningún conflicto, con 0,9 todas.",
               ["Umbral: se marca si la similitud es menor que", "Contradicciones marcadas", "Paráfrasis marcadas (falsas alarmas)"], rows, [380, 280, 290], row_h=42, size=13,
               note="Las definiciones que se contradicen por una sola palabra clave se parecen más entre sí que las paráfrasis honestas, así que la similitud léxica ordena al revés de lo deseado. Detectar conflictos de glosario exige comparar el valor de los términos definidos (números, condiciones) o la revisión de una persona.",
               note_kind="coral", foot=SINT)


def se213_alcance() -> Fig:
    rows = [["Páginas sin enlaces entrantes", "5", "0"], ["Páginas inalcanzables desde la portada", "5", "0"], ["Páginas a más de 3 clics", "0", "0"], ["Profundidad máxima", "3", "3"]]
    return tab("Alcanzabilidad de 120 páginas desde la portada, antes y después de enlazar las huérfanas",
               "Tabla de un sitio sintético de 120 páginas con 8 índices: antes de reparar hay 5 páginas sin enlaces entrantes e inalcanzables desde la portada; tras enlazarlas desde un índice quedan 0; ninguna está a más de 3 clics y la profundidad máxima es 3.",
               ["Medida", "Antes", "Después de enlazar desde índices"], rows, [470, 190, 290], row_h=40, size=13,
               note="El 4 % de páginas huérfanas es invisible para la navegación y solo aparece por búsqueda, si está indexada. La profundidad no fue el problema en este sitio porque los índices cuelgan de la portada; en uno real, la profundidad y la huérfana se miden con el mismo recorrido en anchura.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-214
def se214_fragmentos() -> Fig:
    items = [
        ("Trozos fijos de 500 caracteres", 33.4, "coral", "33,4 % · trozo medio 498"),
        ("Trozos de 500 con solape de 150", 46.5, "gold", "46,5 % · 497"),
        ("Un trozo por encabezado", 100, "teal", "100 % · 1 045"),
    ]
    return bars("Hecho y excepción que lo limita, ¿quedan en el mismo fragmento? (30 documentos, 40 secciones)",
                "Barras: con trozos fijos de 500 caracteres solo el 33,4 por ciento de los pares hecho más excepción quedan en el mismo fragmento, con solape de 150 el 46,5 y dividiendo por encabezado el 100, con un tamaño medio de 1 045 caracteres.",
                items, 3.4, "Cortar por tamaño separa la regla de su excepción dos de cada tres veces; quien recupera solo el primer fragmento recibe una regla falsa. Dividir por encabezado lo evita a cambio de trozos más grandes. Documentos sintéticos con una excepción por sección; los reales son más variados.",
                label_w=300, width=1000, note_kind="gold", foot=SINT)


def se214_metadatos() -> Fig:
    rows = [["Sin responsable", "23", "23", "23"], ["Estado inválido («casi listo»)", "20", "20", "20"], ["Fecha con formato incorrecto", "15", "15", "15"],
            ["Revisado hace más de 180 días", "27", "0", "27"], ["Metadatos correctos y recientes", "55", "0", "0"]]
    return tab("Validar los metadatos de 140 documentos: esquema solo o esquema más antigüedad",
               "Tabla de 140 documentos con metadatos: el esquema solo detecta los 23 sin responsable, los 20 con estado inválido y los 15 con fecha incorrecta, pero ninguno de los 27 revisados hace más de 180 días; añadir la regla de antigüedad detecta los 27 y no marca ninguno de los 55 correctos.",
               ["Defecto", "Documentos", "Detecta el esquema", "Esquema + antigüedad"], rows, [400, 170, 190, 190], row_h=42, size=12,
               note="Un documento puede ser válido y estar obsoleto: el esquema comprueba que la fecha exista, no que sea reciente. La antigüedad máxima de 180 días y la fecha de referencia son parámetros del experimento.",
               note_kind="gold", foot=SINT)


def se214_inyeccion() -> Fig:
    items = [
        ("Instrucciones maliciosas literales", 100, "teal", "6 de 6"),
        ("Ofuscadas, parafraseadas u otro idioma", 0, "coral", "0 de 8"),
        ("Texto benigno marcado en falso", 0, "teal", "0 de 8"),
    ]
    return bars("Un filtro de expresiones regulares contra instrucciones ocultas en documentos que leerá un agente",
                "Barras: un filtro léxico marca 6 de 6 instrucciones maliciosas literales y 0 de 8 ofuscadas, parafraseadas o en otro idioma, y no marca en falso ninguno de 8 textos benignos que contienen palabras como ignorar o instrucciones.",
                items, 4.2, "El filtro se escribió viendo los casos literales, de ahí el 6 de 6; lo que no ve es lo que escribe un adversario que lo conoce (base64, letras separadas, una nota dirigida al agente en un comentario HTML). Un filtro léxico es una molestia para el atacante, no un límite de seguridad: el límite son los permisos del agente.",
                label_w=360, width=1060, note_kind="coral", foot="Veintidós textos escritos por el autor; sin ningún modelo ni agente; idéntico en Windows y Ubuntu.")


# ---------------------------------------------------------------- SE-215
def se215_factor_bus() -> Fig:
    items = [
        ("Nadie se va", 97.5, "teal", "97,5 %"),
        ("Se va 1 persona (el peor caso)", 55.0, "gold", "55,0 %"),
        ("Se van 2", 35.0, "gold", "35,0 %"),
        ("Se van 3", 22.5, "coral", "22,5 %"),
        ("Se van 4 de 5", 7.5, "coral", "7,5 %"),
    ]
    return bars("Archivos con algún responsable activo si se va el peor subconjunto de k personas (300 commits, 40 archivos)",
                "Barras: en un repositorio sintético de 40 archivos y 300 commits repartidos entre 5 personas, el 97,5 por ciento de los archivos tiene algún responsable con al menos 25 por ciento de sus cambios; si se va la peor persona queda el 55, con dos el 35, con tres el 22,5 y con cuatro el 7,5.",
                items, 0.9, "Una sola persona concentra 180 de los 300 commits (60 %) y su salida deja sin responsable a 4 de cada 10 archivos. La métrica usa commits como proxy de conocimiento, con un umbral de 25 %; no mide quién entiende el código ni quién revisa.",
                label_w=360, width=1060, note_kind="gold", foot="Repositorio creado con git fast-import y autores sintéticos; mismos recuentos en Windows (git 2.55) y Ubuntu (git 2.43).")


def se215_arqueologia() -> Fig:
    rows = [["Commits del historial", "120", "84 con mensaje genérico («fix», «wip», «ok»)"], ["`git log --grep=timeout`", "0 hallazgos", "El mensaje no dice qué cambió"],
            ["`git log -S\"TIMEOUT = 30\"`", "1 hallazgo", "El commit que introduce el valor: mensaje «fix»"], ["Commits que tocan el archivo", "2", "El rastreo por contenido evita leer ambos a ciegas"],
            ["`git blame` de la línea", "Mismo commit", "Coincide con el hallado por `-S`"]]
    return tab("Reconstruir cuándo y por qué cambió un valor de configuración en 120 commits",
               "Tabla de un repositorio sintético de 120 commits donde 84 tienen mensaje genérico: buscar por mensaje no encuentra nada, buscar por el contenido añadido con la opción -S halla el commit exacto y git blame apunta al mismo, pero el mensaje del commit solo dice fix.",
               ["Método", "Resultado", "Lectura"], rows, [330, 190, 430], row_h=48, size=12,
               note="El historial permite saber cuándo y quién, casi nunca por qué: el motivo de un cambio de 10 a 30 no estaba en ningún mensaje. Esa es la parte del conocimiento perdido que hay que reconstruir hablando con personas o con otros artefactos, y declarar como hipótesis.",
               note_kind="gold", foot="Repositorio creado con git fast-import; resultados idénticos en Windows y Ubuntu.")


def se215_fuentes() -> Fig:
    rows = [["0 % (independientes)", "80,0 %", "98,5 %", "99,9 %"], ["50 %", "80,1 %", "90,0 %", "95,2 %"], ["90 %", "80,0 %", "81,8 %", "83,8 %"]]
    return tab("Exactitud de una afirmación cuando todas las fuentes coinciden, según cuánto se copian",
               "Tabla de 100 000 simulaciones por celda con fuentes de 80 por ciento de fiabilidad: si son independientes, que tres coincidan da 98,5 por ciento de exactitud y que cinco coincidan 99,9; si el 90 por ciento copia de la primera, tres coinciden con 81,8 y cinco con 83,8.",
               ["Probabilidad de copiar la primera fuente", "1 fuente", "3 fuentes coinciden", "5 fuentes coinciden"], rows, [360, 170, 230, 230], row_h=44, size=13,
               note="Diez documentos que repiten el mismo error cuentan como uno. Al reconstruir conocimiento perdido, la coincidencia entre fuentes solo suma evidencia cuando se puede mostrar que no se copiaron. Fiabilidad y probabilidad de copia son supuestos, no medidas.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-216
def se216_versiones() -> Fig:
    rows = [["v1", "10", "30", "0"], ["v2 (se eliminan 2 páginas y se renombra 1)", "8", "21", "7"], ["v3 (se añade 1 página)", "9", "23", "7"]]
    return tab("Tres versiones etiquetadas de un portal de 10 páginas: enlaces internos rotos por versión",
               "Tabla de tres versiones de un portal construidas desde etiquetas de git: v1 tiene 10 páginas, 30 enlaces y 0 rotos; v2 elimina dos páginas y renombra una, deja 8 páginas, 21 enlaces y 7 rotos; v3 añade una página y conserva los 7 rotos.",
               ["Versión", "Páginas", "Enlaces internos", "Rotos"], rows, [450, 160, 200, 140], row_h=44, size=13,
               note="Las 3 páginas de v1 ausentes en la última versión (p03, p05 y p07) son el contrato roto con quien enlazó a la versión antigua. Un portal versionado necesita dos cosas distintas: que cada versión sea coherente consigo misma y una política para los enlaces entre versiones.",
               note_kind="gold", foot="Repositorio de git creado en un directorio temporal; idéntico en Windows y Ubuntu.")


def se216_paquete() -> Fig:
    rows = [["Recorrer el directorio sin ordenar, con la fecha de modificación de cada archivo", "3", "Cambia con la hora de la extracción"], ["Ordenar, fijar la fecha y los permisos y declarar el sistema de origen", "1", "Misma huella entre ejecuciones y sistemas"],
            ["El mismo árbol con saltos de línea CRLF", "otra", "El contenido distinto cambia la huella"]]
    return tab("Huellas distintas de un paquete zip de 30 páginas construido tres veces",
               "Tabla de un archivo zip construido tres veces tras cambiar las fechas de los archivos: la construcción ingenua produce 3 huellas distintas, la determinista una sola, igual en Windows y Ubuntu cuando también se fija el campo de sistema de origen; con saltos de línea CRLF la huella cambia.",
               ["Construcción del paquete", "Huellas en 3 construcciones", "Lectura"], rows, [470, 190, 290], row_h=60, size=12,
               note="Un hallazgo del experimento: sin fijar el sistema de origen del zip (0 en Windows, 3 en Linux por defecto) la construcción «determinista» daba huellas distintas en cada sistema. Fijar solo el orden y la fecha no basta.",
               note_kind="teal", foot="Mismo conjunto de 30 páginas generado con semilla fija; huella determinista idéntica en Windows y Ubuntu.")


def se216_auditoria() -> Fig:
    rows = [["Enlace roto", "3", "3", "—"], ["Sin responsable", "2", "2", "—"], ["Revisión obsoleta", "2", "2", "—"], ["Título duplicado", "1", "1", "—"], ["Página huérfana", "1", "1", "—"],
            ["Afirmación falsa (dice 15 %, es 10 %)", "3", "0", "3"]]
    return tab("Auditoría de un portal de 40 páginas con 12 defectos sembrados",
               "Tabla de una auditoría automática: las comprobaciones estáticas detectan 9 de los 12 defectos sembrados y ninguna de las 3 afirmaciones falsas, que solo detecta ejecutar los ejemplos documentados; hubo una falsa alarma por una página sin enlaces entrantes que no se sembró.",
               ["Defecto sembrado", "Sembrados", "Detecta la comprobación estática", "Detecta ejecutar los ejemplos"], rows, [360, 140, 240, 220], row_h=44, size=12,
               note="La auditoría estática encuentra lo que deja una señal en el texto y se queda ciega ante una página limpia que dice algo falso. La falsa alarma fue una página que quedó sin enlaces entrantes por azar al generar el corpus: una señal real, aunque no sembrada.",
               note_kind="gold", foot=SINT)


FIGURES = {
    "se-211-pasos-repetibles.svg": se211_idempotencia,
    "se-211-cobertura-de-runbooks.svg": se211_cola,
    "se-211-linter-de-runbooks.svg": se211_lint,
    "se-212-comprobador-de-enlaces.svg": se212_enlaces,
    "se-212-construccion-reproducible.svg": se212_determinismo,
    "se-212-linter-y-bloques-de-codigo.svg": se212_vallas,
    "se-213-busqueda-y-sinonimos.svg": se213_busqueda,
    "se-213-conflictos-de-glosario.svg": se213_glosario,
    "se-213-paginas-alcanzables.svg": se213_alcance,
    "se-214-fragmentos-y-excepciones.svg": se214_fragmentos,
    "se-214-metadatos-y-antiguedad.svg": se214_metadatos,
    "se-214-filtro-de-instrucciones-ocultas.svg": se214_inyeccion,
    "se-215-factor-bus.svg": se215_factor_bus,
    "se-215-arqueologia-del-historial.svg": se215_arqueologia,
    "se-215-fuentes-que-se-copian.svg": se215_fuentes,
    "se-216-versiones-y-enlaces.svg": se216_versiones,
    "se-216-paquete-reproducible.svg": se216_paquete,
    "se-216-auditoria-del-portal.svg": se216_auditoria,
}
