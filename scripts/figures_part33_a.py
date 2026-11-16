"""Figures for SE-397 to SE-402 (synthetic data with fixed seeds, real file/hash/openssl probes; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars
from figure_diagrams import fan, merge
from figures_part07_a import bars


SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); lo que difiere entre sistemas se indica en la figura."


# ---------------------------------------------------------------- SE-397
def se397_fuentes() -> Fig:
    return grouped_bars(
        'Veinte builds del mismo árbol en entornos distintos: hashes distintos según la fuente de variación que se deja sin normalizar',
        "Barras horizontales con los hashes distintos que producen 20 builds del mismo árbol de 42 archivos según la fuente de variación sin normalizar: las marcas de tiempo, el orden, la ruta absoluta y la fecha incrustada dan 20; el orden de un diccionario 13, el usuario 5, los permisos 3 y los saltos de línea 2; con todo normalizado hay un solo hash.",
        ["Marca de tiempo de cada archivo", "Orden de los archivos", "Ruta absoluta del build", "Fecha del build incrustada", "Orden de un diccionario o conjunto",
         "Nombre de usuario o de equipo", "Permisos del sistema de archivos", "Saltos de línea CRLF frente a LF", "Todas a la vez", "Ninguna (todo normalizado)"],
        [("Hashes distintos", [20, 20, 20, 20, 13, 5, 3, 2, 20, 1], "coral")],
        unit="Hashes distintos en 20 builds", horizontal=True, label_w=270, ticks=[0, 5, 10, 15, 20],
        note='Cada barra cuenta cuántos de 20 resultados distintos produce cada fuente por sí sola: con 2 o 3 entornos posibles basta ver pocas variantes, con 20 entornos cada uno produce su propio hash. Una fuente que casi nunca cambia (CRLF) no es inofensiva: aparece en la primera máquina que la cambia.', note_kind='gold', foot=SINT)


def se397_sistemas() -> Fig:
    return fan(
        'El mismo árbol construido en Windows y en Ubuntu: la cabecera de zip delata el sistema que lo escribió',
        "Diagrama del mismo árbol construido en Windows y en Ubuntu: con marcas de tiempo, orden y permisos normalizados pero sin fijar create_system el zip da bb3ff54418db0198 en Windows y 2d20872cfbd34c32 en Ubuntu; fijando create_system a 3 los dos dan 2d20872cfbd34c32; en un tar.gz cambia el hash según la marca de tiempo del encabezado gzip.",
        ("El mismo árbol, normalizado", "construido en Windows 11 (3.12.9) y en Ubuntu WSL2 (3.12.3)", "navy"),
        [("Sin fijar create_system: hashes distintos", "Windows bb3ff54418db0198 · Ubuntu 2d20872cfbd34c32; el campo vale 0 en un sistema y 3 en el otro", "coral"),
         ("Con create_system fijado a 3: hashes idénticos", "2d20872cfbd34c32 en los dos sistemas", "teal"),
         ("tar.gz con la marca de tiempo del encabezado gzip en 0 o en 1", "el hash cambia con el valor (dea717b49614 con uno de ellos, igual en ambos sistemas)", "gold")],
        note='El campo que difería no estaba en ninguna lista de fuentes habituales; apareció al repetir el build en un segundo sistema. Un build reproducible se demuestra reconstruyendo en condiciones distintas, no leyendo una lista de causas conocidas.', note_kind='coral', foot=REAL)


def se397_localizar() -> Fig:
    return fan(
        'Cómo se localiza lo que no es reproducible y qué muestra un build que lee una entrada no declarada',
        "Diagrama de cómo se localiza lo que no es reproducible: comparar dos zips archivo a archivo muestra que solo difiere 1 de 42 archivos, pyproject.toml, cuando se incrusta una fecha; un build que lee una variable de entorno no declarada da 10e620451e6c con A y 8f681af2e460 con B; tras fijar entradas y entorno hay un solo hash.",
        ("Dos builds cuyos hashes no coinciden", "hay que localizar qué cambió", "navy"),
        [("Fecha incrustada: 1 de 42 archivos difiere", "pyproject.toml; se localiza con una comparación por archivo", "gold"),
         ("Variable de entorno no declarada (A y B)", "10e620451e6c frente a 8f681af2e460: el build no es hermético", "coral"),
         ("Mismo árbol tras fijar entradas y entorno", "un hash, 2d20872cfbd34c32: reproducible en ambos sistemas", "teal")],
        note='Un build hermético declara todas sus entradas y no lee otras; un build reproducible produce los mismos bytes con las mismas entradas. Lo primero es una condición de diseño que se puede comprobar bloqueando el acceso; lo segundo, un resultado que se comprueba reconstruyendo. Ninguno prueba que el contenido sea benigno.', note_kind='gold', foot=REAL)


# ---------------------------------------------------------------- SE-398
def se398_promocion() -> Fig:
    return grouped_bars(
        'Reconstruir para cada entorno o promover el mismo artefacto: 2 000 lanzamientos por celda',
        "Barras agrupadas con 2 000 lanzamientos por probabilidad de deriva: si cada entorno reconstruye, entre 10 y 283 producciones difieren de lo probado y entre 2 y 34 contienen defectos no vistos en preproducción; si se promueve la misma huella son 0 en todos los casos.",
        ["1 % de los builds difiere", "5 % de los builds difiere", "15 % de los builds difiere"],
        [("Producción distinta de lo probado (de 2 000)", [10, 94, 283], "coral"), ("Defectos no vistos en preproducción", [2, 9, 34], "gold"), ("Si se promueve la misma huella", [0, 0, 0], "teal")],
        unit="Lanzamientos, de 2 000",
        note='El cero de la última barra es una consecuencia del modelo: lo que se promueve es idéntico por construcción. Lo que demuestra la figura es la dependencia con la tasa de deriva, que es un supuesto del autor (12 % de las derivas ocultan un defecto).', note_kind='gold', foot=SINT)


def se398_etiquetas() -> Fig:
    items = [
        ("Sin repush de etiquetas", 0.0, "teal", "0 de 143"),
        ("Repush 2 % de los días", 9.0, "gold", "9 de 143"),
        ("Repush 10 % de los días", 41.0, "coral", "41 de 143"),
    ]
    return bars("Despliegues por etiqueta cuyo contenido no es el que se probó (1 000 días, un despliegue por semana)",
                "Barras: con una etiqueta que se vuelve a publicar el 2 por ciento de los días, 9 de 143 despliegues por etiqueta llevan un contenido distinto del probado; con el 10 por ciento, 41 de 143; sin repush, ninguno.",
                items, 5.5, "Una etiqueta es un puntero que alguien puede mover; una huella es una función del contenido. Desplegar por huella hace nulo este riesgo y sigue permitiendo usar etiquetas legibles para las personas.",
                label_w=200, width=900, note_kind="coral", foot=SINT)


def se398_retencion() -> Fig:
    items = [
        ("Conserva 1 versión", 30.4, "coral", "30,4 %"),
        ("Conserva 2 versiones", 8.9, "gold", "8,9 %"),
        ("Conserva 3 versiones", 2.7, "gold", "2,7 %"),
        ("Conserva 5 versiones", 0.2, "teal", "0,2 %"),
        ("Conserva 10 versiones", 0.0, "teal", "0,0 %"),
    ]
    return bars("Retrocesos que obligan a reconstruir porque la versión necesaria ya se borró (10 000 retrocesos simulados)",
                "Barras: si la limpieza conserva solo la última versión, el 30,4 por ciento de los retrocesos exige reconstruir; con dos versiones, 8,9; con tres, 2,7; con cinco, 0,2; con diez, ninguno.",
                items, 12.0, "La profundidad del retroceso sigue una cola geométrica supuesta (30 % de probabilidad de saltar una versión más). El supuesto se debe sustituir por el historial propio; la forma de la cola es lo que justifica conservar más de una.",
                label_w=220, width=900, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-399
def se399_real() -> Fig:
    return grouped_bars(
        'Dependencias reales de dos entornos de Python: la clausura transitiva depende del entorno, no del proyecto',
        "Barras horizontales en escala logarítmica con las dependencias de dos entornos reales: Windows tiene 349 distribuciones, 188 con dependencias, mediana de 3 transitivas, clausura máxima de 88 (jupyter) y 77 raíces; Ubuntu tiene 63, 10, 2,5, 6 (twisted) y 43; la clausura depende del entorno, no del proyecto.",
        ["Distribuciones instaladas", "Paquetes con al menos una dependencia instalada", "Mediana de dependencias transitivas entre ellos", "Mayor clausura transitiva de un paquete", "Paquetes que nadie más requiere (raíces)"],
        [("Windows (3.12.9)", [349, 188, 3, 88, 77], "coral"), ("Ubuntu WSL2 (3.12.3)", [63, 10, 2.5, 6, 43], "teal")],
        unit="Paquetes (o dependencias)", horizontal=True, log=True, label_w=300, ticks=[1, 10, 100, 1000],
        note='Lo que se instaló no es lo que el proyecto declara: la clausura de un paquete se calcula leyendo los metadatos de lo que hay. Los dos entornos difieren por diseño; no representan ningún proyecto de producción y las extras opcionales se excluyeron.', note_kind='gold', foot=REAL)


def se399_resolucion() -> Fig:
    return grouped_bars(
        'Construir cada día durante 60 días 25 dependencias con rango: conjuntos de versiones distintos que se resuelven',
        "Barras agrupadas con la resolución diaria durante 60 días de 25 dependencias con rango: sin archivo de bloqueo se resuelven 37 conjuntos de versiones distintos y el conjunto cambia en 36 días; con archivo de bloqueo con huellas hay 1 conjunto y 0 cambios.",
        ["Sin archivo de bloqueo (rangos compatibles)", "Con archivo de bloqueo con huellas"],
        [("Conjuntos distintos en 60 días", [37, 1], "coral"), ("Días en que el conjunto cambió (de 60)", [36, 0], "gold")],
        unit="Conjuntos o días",
        note='Sin bloqueo, dos builds del mismo commit en días distintos no producen el mismo árbol de dependencias: no hay build reproducible posible. En el grafo sintético de 400 paquetes, 15 dependencias directas arrastran una media de 49,4 paquetes (3,3 veces) y un paquete transitivo vulnerable es alcanzado por 2,3 de las 15 directas.', note_kind='coral', foot=SINT)


def se399_parche() -> Fig:
    return percentile_intervals(
        'Días hasta aplicar el parche de una vulnerabilidad según cómo se incorpora la dependencia (5 000 casos por fila)',
        "Intervalos horizontales con los días hasta aplicar el parche de una vulnerabilidad: una dependencia gestionada con bloqueo tiene mediana de 2,7 días y percentil 95 de 5,0; una copia vendorizada sin dueño 15,8 y 63,1; una copia con dueño y revisión periódica 7,0 y 22,9.",
        [("Dependencia gestionada con bloqueo", [2.7, 5.0]), ("Copia vendorizada sin dueño", [15.8, 63.1]), ("Copia vendorizada con dueño y revisión periódica", [7.0, 22.9])],
        unit="Días hasta aplicar el parche", marks=("mediana", "percentil 95"), decimals=1, label_w=250,
        note='Los tiempos son un modelo exponencial con medias fijadas por el autor, no una medición de equipos reales. Lo que muestra es la forma: vendorizar mueve la responsabilidad del parche a quien copió y alarga la cola cuando nadie la ejerce.', note_kind='gold', foot=SINT)


# ---------------------------------------------------------------- SE-400
def se400_validador() -> Fig:
    return grouped_bars(
        'Un validador de forma de SBOM frente a 240 mutaciones (12 operadores sobre 20 SBOM de 30 componentes)',
        "Barras horizontales con las mutaciones detectadas, de 20, por un validador de forma de SBOM: detecta 20 de 20 las que quitan la versión, el purl o las huellas, duplican un componente, cambian solo la versión del purl o vacían la lista, y 0 de 20 las que mantienen la forma, como borrar un componente o cambiar la licencia.",
        ["Quitar la versión de un componente", "Quitar el purl", "Quitar las huellas", "Duplicar un componente", "Cambiar solo la versión del purl", "Vaciar la lista de componentes",
         "Borrar un componente", "Cambiar versión y purl a la vez", "Cambiar la huella por otra válida", "Añadir un componente fantasma", "Cambiar la licencia", "Cambiar nombre y purl a la vez"],
        [("Detectadas", [20, 20, 20, 20, 20, 20, 0, 0, 0, 0, 0, 0], "teal")],
        unit="Mutaciones detectadas, de 20", horizontal=True, label_w=270, ticks=[0, 5, 10, 15, 20],
        note='Detecta el 50 % de las mutaciones y todas las que ve son de forma. Un SBOM bien formado y falso parece medido. Que valide no dice que el inventario sea el del artefacto: para eso hay que compararlo con el contenido real.', note_kind='coral', foot=SINT)


def se400_completitud() -> Fig:
    items = [
        ("Solo manifiesto", 63.3, "coral", "63,3 %"),
        ("Manifiesto + bloqueo", 86.7, "gold", "86,7 %"),
        ("Bloqueo + escaneo de copias", 93.3, "gold", "93,3 %"),
        ("Escaneo del artefacto final", 98.3, "teal", "98,3 %"),
    ]
    return bars("Mediana del porcentaje de componentes reales que cada método de inventario ve (100 proyectos sintéticos de 60 componentes)",
                "Barras: la mediana de componentes inventariados es 63,3 por ciento con solo el manifiesto, 86,7 con manifiesto y archivo de bloqueo, 93,3 si además se escanean las copias y 98,3 al escanear el artefacto final; los descargados en tiempo de ejecución no los ve ninguno.",
                items, 8.0, "El peor proyecto con solo el manifiesto ve el 46,7 % y con el escaneo del artefacto el 91,7 %. La composición (62 % declaradas, 24 % transitivas, 7 % copiadas, 4 % estáticas, 3 % descargadas) es un supuesto del autor; lo que se sostiene es que cada método ve una capa.",
                label_w=250, width=940, note_kind="gold", foot=SINT)


def se400_procedencia() -> Fig:
    return fan(
        'Qué ataques detecta la verificación de los campos de una procedencia y cuáles pasan',
        "Diagrama de lo que detecta la verificación de los campos de una procedencia: detecta cinco ataques, el artefacto sustituido, la procedencia de otro repositorio, el runner no confiable, la rama no esperada y los parámetros alterados; no detecta tres, la procedencia fabricada por quien controla el constructor, el commit malicioso aprobado y la dependencia comprometida.",
        ("Verificar los campos de la procedencia", "huella del sujeto, repositorio, constructor, rama y parámetros", "navy"),
        [("Detecta cinco ataques", "artefacto sustituido tras el build (huella del sujeto) · procedencia de otro repositorio · build en un runner no confiable · commit en una rama no esperada · parámetros de construcción alterados", "teal"),
         ("No detecta tres ataques", "procedencia fabricada por quien controla el constructor · commit malicioso aprobado en la rama protegida · dependencia comprometida descargada durante el build", "coral", True)],
        note='Es un análisis lógico de qué campo contradice qué ataque, no una medición. Una procedencia dice quién construyó qué a partir de qué; no dice que la fuente fuese benigna ni que el constructor fuera honesto.', note_kind='coral', foot="Análisis del autor, sin datos medidos.")


# ---------------------------------------------------------------- SE-401
def se401_matriz() -> Fig:
    r = [[1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
    return heatmap(
        'Seis estrategias de verificación frente a nueve ataques (R rechaza, P deja pasar), con firmas Ed25519 reales de openssl',
        "Mapa de calor con qué ataques rechaza cada una de seis estrategias de verificación sobre nueve ataques con firmas Ed25519 reales: la estrategia 1 rechaza 2 de 9, la 2 rechaza 7, la 3 rechaza 4, la 4 rechaza 5 y las estrategias 5 y 6 rechazan 7; ninguna rechaza la clave de firma robada ni el CI comprometido sin ayuda de revocación.",
        ["Cuerpo cambiado, checksum intacto", "Cuerpo y checksum cambiados en el mismo host", "Cuerpo, firma y clave del atacante juntos", "Versión antigua válida servida como la última",
         "Firma corrupta con el artefacto intacto", "Manifiesto firmado de otro producto", "Archivo truncado", "Clave de firma robada", "CI comprometido que firma con la clave real"],
        ["1 · rechaza 2 de 9", "2 · rechaza 7 de 9", "3 · rechaza 4 de 9", "4 · rechaza 5 de 9", "5 · rechaza 7 de 9", "6 · rechaza 7 de 9"],
        r, unit="rechazo", row_title="Ataque", col_title="Estrategia de verificación (R rechaza, P deja pasar)",
        scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "R" if v else "P", cell_h=38, label_w=330,
        note='1 checksum de la misma página · 2 checksum por canal aparte · 3 firma con clave de la misma página · 4 firma con clave fijada · 5 clave fijada y manifiesto firmado con nombre y secuencia · 6 igual que 5 con revocación. La estrategia 2 rechaza el CI comprometido solo porque la huella esperada llegó por otro canal antes del compromiso.', note_kind='gold', foot=REAL)


def se401_costes() -> Fig:
    return grouped_bars(
        'Costo de hashear 64 MiB y de verificar una firma, medido en dos sistemas (una lectura, cambia entre ejecuciones)',
        "Barras horizontales con el tiempo de hashear 64 MiB y de verificar una firma en Windows y en Ubuntu: SHA-256 168,5 y 153,3 ms; SHA-512 151,0 y 102,1; BLAKE2b 261,3 y 106,9; SHA3-256 245,7 y 184,7; verificar una firma Ed25519 con un proceso openssl 33,1 y 5,7 ms; son lecturas únicas.",
        ["SHA-256", "SHA-512", "BLAKE2b", "SHA3-256", "Verificar una firma Ed25519 con un proceso openssl"],
        [("Windows 11", [168.5, 151.0, 261.3, 245.7, 33.1], "coral"), ("Ubuntu WSL2", [153.3, 102.1, 106.9, 184.7, 5.7], "teal")],
        unit="Tiempo (ms)", horizontal=True, label_w=270, decimals=1,
        note='El costo es de milisegundos frente a minutos de build: la verificación no se omite por rendimiento. Las cifras son una lectura de un equipo con un solo intento y cambian en cada ejecución; el 33 frente a 5,7 ms mide sobre todo el arranque del proceso openssl en cada sistema.', note_kind='gold', foot="Mediciones de reloj: una lectura por barra, no reproducibles al milisegundo.")


def se401_confianza() -> Fig:
    return fan(
        'Qué da por bueno cada estrategia de verificación y qué no cubre',
        "Diagrama de seis estrategias de verificación con lo que cada una da por bueno y lo que no cubre: el checksum en la misma página detecta corrupción pero no manipulación; la firma con clave de la misma página deja pasar la firma y la clave del atacante; la firma con clave fijada no cubre rollback ni confusión entre productos; el manifiesto con secuencia y la revocación no cierran el hueco entre el robo de la clave y su revocación.",
        ("Estrategias de verificación", "de menos a más exigentes", "navy"),
        [("1. Checksum en la misma página", "confía en que la página no se alteró · no cubre manipulación: detecta corrupción", "coral"),
         ("2. Checksum por otro canal", "confía en que el segundo canal sea independiente y anterior · no distingue un release malicioso legítimo", "coral"),
         ("3. Firma con clave de la misma página", "confía en que el atacante no controle la página · firma y clave del atacante pasan", "gold"),
         ("4. Firma con clave fijada", "confía en que la clave fijada sea la correcta · no cubre rollback ni confusión entre productos", "gold"),
         ("5. Manifiesto firmado con secuencia", "confía en que el verificador recuerde la última secuencia · no cubre clave robada ni CI comprometido", "teal"),
         ("6. Con revocación", "confía en que la lista de revocación llegue a tiempo · no cubre el hueco entre el robo y la revocación", "teal")],
        note='Cada estrategia añade una confianza y cierra un ataque: se trata de mover la confianza a un lugar más pequeño y más fácil de proteger, no de eliminarla. La clave fijada es una raíz de confianza que hay que distribuir, rotar y proteger.', note_kind='gold', foot="Análisis del autor a partir de la matriz medida.")


# ---------------------------------------------------------------- SE-402
def se402_comparador() -> Fig:
    return heatmap(
        'Un comparador de firmas públicas con ast frente a doce de los catorce tipos de cambio de la API de entregas',
        "Mapa de calor con el nivel de versión correcto y el que ve un comparador de firmas públicas para doce cambios de una API: acierta 8, sobrestima uno (hacer opcional un parámetro obligatorio, que es menor y el comparador ve mayor) y subestima tres que rompen a los clientes sin cambiar la firma, que ve como parche.",
        ["Añadir una función pública", "Quitar una función pública", "Renombrar un parámetro obligatorio", "Añadir un parámetro obligatorio", "Añadir un parámetro opcional al final", "Cambiar el valor por defecto de un parámetro",
         "Hacer opcional un parámetro obligatorio", "Quitar un método de una clase", "Cambiar la escala de la nota sin tocar la firma", "Cambiar el orden por defecto del listado", "Lanzar una excepción nueva ante entrada inválida", "Corregir un error sin cambiar la firma"],
        ["Nivel correcto", "Lo que ve el comparador"],
        [[1, 1], [2, 2], [2, 2], [2, 2], [1, 1], [2, 2], [1, 2], [2, 2], [2, 0], [2, 0], [2, 0], [0, 0]],
        unit="nivel", row_title="Cambio de la API", col_title="Nivel de versión",
        scale="coral", vmin=0, vmax=2, cell_fmt=lambda v: "mayor" if v == 2 else ("menor" if v == 1 else "parche"),
        highlight=[(6, 1), (8, 1), (9, 1), (10, 1)], cell_h=34, label_w=330,
        note='Acierta 10 de 14 (se omiten dos filas de acierto por espacio: añadir un método a una clase y cambiar un interno privado). Los tres errores graves son los cambios de comportamiento: la firma es idéntica y el significado cambió, y ninguna herramienta que lea solo firmas puede verlos.', note_kind='coral', foot=REAL)


def se402_etiquetado() -> Fig:
    items = [
        ("A mano sin disciplina", 22.1, "coral", "22,1 %"),
        ("A mano con revisión", 10.3, "gold", "10,3 %"),
        ("Solo el comparador", 11.1, "gold", "11,1 %"),
        ("Comparador y revisión", 0.8, "teal", "0,8 %"),
    ]
    return bars("Cambios con efecto publicados con un nivel de versión inferior al real (3 000 lanzamientos simulados, 1 355 con efecto)",
                "Barras: publicar el nivel de versión a mano sin disciplina subestima el 22,1 por ciento de los cambios con efecto; a mano con revisión, 10,3; solo con el comparador de firmas, 11,1; combinando comparador y revisión manual, 0,8.",
                items, 9.0, "La combinación toma el mayor de los dos niveles y supone errores independientes entre el comparador y el autor, supuesto que no se midió. La tasa de error manual (22 % y 10 %) también es del autor; lo que se sostiene es que dos controles con errores distintos se cubren.",
                label_w=240, width=940, note_kind="gold", foot=SINT)


def se402_tipos() -> Fig:
    return grouped_bars(
        'Los catorce cambios de la API agrupados por lo que una herramienta de firmas puede ver',
        "Barras horizontales con los catorce cambios de la API agrupados por lo que una herramienta de firmas puede ver: 5 rompen y la firma lo dice, 3 rompen y la firma no lo dice, 1 no rompe y la herramienta alarma, 3 añaden capacidad sin romper y 2 no cambian nada visible.",
        ["Rompe y la firma lo dice", "Rompe y la firma no lo dice", "No rompe y la herramienta alarma", "Añade capacidad sin romper", "No cambia nada visible"],
        [("Cambios", [5, 3, 1, 3, 2], "coral")],
        unit="Cambios de la API (de 14)", horizontal=True, label_w=270, ticks=[0, 1, 2, 3, 4, 5, 6],
        note='Los 3 cambios que rompen sin cambiar la firma son el 37,5 % de los 8 incompatibles: ese es el hueco de la automatización y el motivo de las pruebas de contrato y del changelog revisado por una persona.', note_kind='coral', foot="Catorce cambios construidos por el autor sobre una API de cuatro elementos públicos.")


FIGURES = {
    "se-397-fuentes-de-variacion.svg": se397_fuentes,
    "se-397-dos-sistemas-un-hash.svg": se397_sistemas,
    "se-397-localizar-la-diferencia.svg": se397_localizar,
    "se-398-reconstruir-o-promover.svg": se398_promocion,
    "se-398-etiquetas-mutables.svg": se398_etiquetas,
    "se-398-retencion-y-retroceso.svg": se398_retencion,
    "se-399-dependencias-reales.svg": se399_real,
    "se-399-deriva-de-resolucion.svg": se399_resolucion,
    "se-399-latencia-de-parche.svg": se399_parche,
    "se-400-validador-de-sbom.svg": se400_validador,
    "se-400-completitud-del-inventario.svg": se400_completitud,
    "se-400-ataques-y-procedencia.svg": se400_procedencia,
    "se-401-matriz-de-ataques.svg": se401_matriz,
    "se-401-costo-de-verificar.svg": se401_costes,
    "se-401-que-confia-cada-estrategia.svg": se401_confianza,
    "se-402-comparador-de-firmas.svg": se402_comparador,
    "se-402-etiquetado-de-versiones.svg": se402_etiquetado,
    "se-402-lo-que-ve-una-herramienta.svg": se402_tipos,
}
