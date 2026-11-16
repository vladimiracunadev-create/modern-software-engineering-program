"""Figures for SE-397 to SE-402 (synthetic data with fixed seeds, real file/hash/openssl probes; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); lo que difiere entre sistemas se indica en la figura."


# ---------------------------------------------------------------- SE-397
def se397_fuentes() -> Fig:
    rows = [
        ["Marca de tiempo de cada archivo", "20 de 20", "Fijarla (1980-01-01 o SOURCE_DATE_EPOCH)"],
        ["Orden de los archivos", "20 de 20", "Ordenar los nombres"],
        ["Ruta absoluta del build", "20 de 20", "Quitarla del artefacto o fijar la ruta"],
        ["Fecha del build incrustada", "20 de 20", "No incrustarla o derivarla del commit"],
        ["Orden de un diccionario o conjunto", "13 de 20", "Ordenar antes de serializar"],
        ["Nombre de usuario o de equipo", "5 de 20", "No incrustarlo"],
        ["Permisos del sistema de archivos", "3 de 20", "Fijar el modo de cada entrada"],
        ["Saltos de línea CRLF frente a LF", "2 de 20", "Fijar la normalización de la fuente"],
        ["Todas a la vez", "20 de 20", "Se acumulan sin aviso"],
        ["Ninguna (todo normalizado)", "1 de 20", "Un solo hash: el build es reproducible"],
    ]
    return tab("Veinte builds del mismo árbol en entornos distintos: hashes distintos según la fuente de variación que se deja sin normalizar",
               "Tabla: al construir 20 veces el mismo árbol de 42 archivos con una sola fuente sin normalizar, las marcas de tiempo, el orden, la ruta absoluta y la fecha incrustada producen 20 hashes distintos; el orden de un diccionario 13, el usuario 5, los permisos 3 y los saltos de línea 2; con todo normalizado hay un solo hash.",
               ["Fuente de variación sin normalizar", "Hashes distintos", "Qué la elimina"], rows, [380, 150, 390], row_h=40, size=13,
               note="La columna central cuenta cuántos de 20 resultados distintos produce cada fuente por sí sola: con 2 o 3 entornos posibles basta ver pocas variantes, con 20 entornos cada uno produce su propio hash. Una fuente que casi nunca cambia (CRLF) no es inofensiva: aparece en la primera máquina que la cambia.",
               note_kind="gold", foot=SINT)


def se397_sistemas() -> Fig:
    rows = [
        ["Normalizado, sin fijar el sistema que escribe el archivo", "bb3ff54418db0198", "2d20872cfbd34c32", "Distintos"],
        ["Normalizado y con create_system fijado a 3", "2d20872cfbd34c32", "2d20872cfbd34c32", "Idénticos"],
        ["tar.gz con la marca de tiempo del encabezado gzip en 0 o en 1", "dea717b49614", "(igual en ambos)", "Cambia con el valor"],
    ]
    return tab("El mismo árbol construido en Windows y en Ubuntu: la cabecera de zip delata el sistema que lo escribió",
               "Tabla: un zip normalizado en marcas de tiempo, orden y permisos produce el hash bb3ff54418db0198 en Windows y 2d20872cfbd34c32 en Ubuntu porque el campo create_system vale 0 en un sistema y 3 en el otro; al fijarlo a 3 ambos producen 2d20872cfbd34c32. Un tar.gz cambia con la marca de tiempo del encabezado gzip.",
               ["Construcción", "Windows 11 (3.12.9)", "Ubuntu WSL2 (3.12.3)", "Resultado"], rows, [360, 190, 190, 180], row_h=52, size=12,
               note="El campo que difería no estaba en ninguna lista de fuentes habituales; apareció al repetir el build en un segundo sistema. Un build reproducible se demuestra reconstruyendo en condiciones distintas, no leyendo una lista de causas conocidas.",
               note_kind="coral", foot=REAL)


def se397_localizar() -> Fig:
    rows = [
        ["Dos builds con fecha incrustada: archivos que difieren", "1 de 42", "pyproject.toml", "Localizada con una comparación por archivo"],
        ["Dos builds con una variable de entorno no declarada (A y B)", "Hash distinto", "10e620451e6c frente a 8f681af2e460", "El build no es hermético"],
        ["Mismo árbol, tras fijar entradas y entorno", "Un hash", "2d20872cfbd34c32", "Reproducible en ambos sistemas"],
    ]
    return tab("Cómo se localiza lo que no es reproducible y qué muestra un build que lee una entrada no declarada",
               "Tabla: comparar dos zips archivo a archivo localiza que solo pyproject.toml difiere cuando se incrusta una fecha; un build que lee una variable de entorno no declarada produce hashes distintos con los valores A y B; con las entradas fijadas el hash es el mismo en Windows y Ubuntu.",
               ["Caso", "Resultado", "Evidencia", "Lectura"], rows, [330, 130, 250, 210], row_h=64, size=12,
               note="Un build hermético declara todas sus entradas y no lee otras; un build reproducible produce los mismos bytes con las mismas entradas. Lo primero es una condición de diseño que se puede comprobar bloqueando el acceso; lo segundo, un resultado que se comprueba reconstruyendo. Ninguno prueba que el contenido sea benigno.",
               note_kind="gold", foot=REAL)


# ---------------------------------------------------------------- SE-398
def se398_promocion() -> Fig:
    rows = [
        ["1 % de los builds difiere", "10 de 2 000 (0,5 %)", "2", "0"],
        ["5 % de los builds difiere", "94 de 2 000 (4,7 %)", "9", "0"],
        ["15 % de los builds difiere", "283 de 2 000 (14,1 %)", "34", "0"],
    ]
    return tab("Reconstruir para cada entorno o promover el mismo artefacto: 2 000 lanzamientos por celda",
               "Tabla: si cada entorno reconstruye y un 1, 5 o 15 por ciento de los builds produce otro resultado, entre 0,5 y 14,1 por ciento de los artefactos de producción son distintos de los probados y entre 2 y 34 contienen defectos que la preproducción no pudo ver; promover la misma huella deja ambos valores en cero.",
               ["Probabilidad de deriva por reconstrucción", "Producción distinta de lo probado", "Defectos no vistos en preproducción", "Si se promueve la misma huella"], rows, [250, 250, 230, 190], row_h=52, size=12,
               note="El cero de la última columna es una consecuencia del modelo: lo que se promueve es idéntico por construcción. Lo que demuestra la figura es la dependencia con la tasa de deriva, que es un supuesto del autor (12 % de las derivas ocultan un defecto).",
               note_kind="gold", foot=SINT)


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
    rows = [
        ["Distribuciones instaladas", "349", "63"],
        ["Paquetes con al menos una dependencia instalada", "188", "10"],
        ["Mediana de dependencias transitivas entre ellos", "3", "2,5"],
        ["Mayor clausura transitiva de un paquete", "88 (jupyter)", "6 (twisted)"],
        ["Paquetes que nadie más requiere (raíces)", "77", "43"],
    ]
    return tab("Dependencias reales de dos entornos de Python: la clausura transitiva depende del entorno, no del proyecto",
               "Tabla: el entorno de Windows tiene 349 distribuciones instaladas, 188 con al menos una dependencia, mediana de 3 transitivas y una clausura máxima de 88 paquetes para jupyter; el entorno de Ubuntu tiene 63, 10 con dependencias, mediana de 2,5 y máximo 6 para twisted.",
               ["Medida con importlib.metadata", "Windows (3.12.9)", "Ubuntu WSL2 (3.12.3)"], rows, [480, 220, 220], row_h=44, size=13,
               note="Lo que se instaló no es lo que el proyecto declara: la clausura de un paquete se calcula leyendo los metadatos de lo que hay. Los dos entornos difieren por diseño; no representan ningún proyecto de producción y las extras opcionales se excluyeron.",
               note_kind="gold", foot=REAL)


def se399_resolucion() -> Fig:
    rows = [
        ["Sin archivo de bloqueo (rangos compatibles)", "37", "36 de 60"],
        ["Con archivo de bloqueo con huellas", "1", "0 de 60"],
    ]
    return tab("Construir cada día durante 60 días 25 dependencias con rango: conjuntos de versiones distintos que se resuelven",
               "Tabla: con 25 dependencias que publican una versión nueva con probabilidad 0,03 por día, construir cada día sin archivo de bloqueo resuelve 37 conjuntos de versiones distintos en 60 días y cambia en 36 de ellos; con bloqueo se resuelve un solo conjunto.",
               ["Política de resolución", "Conjuntos distintos en 60 días", "Días en que el conjunto cambió"], rows, [430, 260, 230], row_h=52, size=13,
               note="Sin bloqueo, dos builds del mismo commit en días distintos no producen el mismo árbol de dependencias: no hay build reproducible posible. En el grafo sintético de 400 paquetes, 15 dependencias directas arrastran una media de 49,4 paquetes (3,3 veces) y un paquete transitivo vulnerable es alcanzado por 2,3 de las 15 directas.",
               note_kind="coral", foot=SINT)


def se399_parche() -> Fig:
    rows = [
        ["Dependencia gestionada con bloqueo", "2,7 días", "5,0 días"],
        ["Copia vendorizada sin dueño", "15,8 días", "63,1 días"],
        ["Copia vendorizada con dueño y revisión periódica", "7,0 días", "22,9 días"],
    ]
    return tab("Días hasta aplicar el parche de una vulnerabilidad según cómo se incorpora la dependencia (5 000 casos por fila)",
               "Tabla: una dependencia gestionada con archivo de bloqueo se parchea en una mediana de 2,7 días y un percentil 95 de 5,0; una copia vendorizada sin dueño en 15,8 y 63,1; una copia con dueño y revisión periódica en 7,0 y 22,9.",
               ["Cómo se incorpora", "Mediana", "Percentil 95"], rows, [500, 210, 210], row_h=44, size=13,
               note="Los tiempos son un modelo exponencial con medias fijadas por el autor, no una medición de equipos reales. Lo que muestra es la forma: vendorizar mueve la responsabilidad del parche a quien copió y alarga la cola cuando nadie la ejerce.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-400
def se400_validador() -> Fig:
    rows = [
        ["Quitar la versión de un componente", "20 de 20"],
        ["Quitar el purl", "20 de 20"],
        ["Quitar las huellas", "20 de 20"],
        ["Duplicar un componente", "20 de 20"],
        ["Cambiar solo la versión del purl", "20 de 20"],
        ["Vaciar la lista de componentes", "20 de 20"],
        ["Borrar un componente", "0 de 20"],
        ["Cambiar versión y purl a la vez", "0 de 20"],
        ["Cambiar la huella por otra válida", "0 de 20"],
        ["Añadir un componente fantasma", "0 de 20"],
        ["Cambiar la licencia", "0 de 20"],
        ["Cambiar nombre y purl a la vez", "0 de 20"],
    ]
    return tab("Un validador de forma de SBOM frente a 240 mutaciones (12 operadores sobre 20 SBOM de 30 componentes)",
               "Tabla: un validador que exige versión, purl coherente, huellas y ausencia de duplicados detecta 20 de 20 mutaciones que quitan o rompen un campo y ninguna de las que mantienen la forma, como borrar un componente, cambiar versión y purl a la vez, cambiar la huella por otra válida o añadir un componente fantasma; en total 120 de 240.",
               ["Mutación del SBOM", "Detectadas"], rows, [640, 200], row_h=34, size=13,
               note="Detecta el 50 % de las mutaciones y todas las que ve son de forma. Un SBOM bien formado y falso parece medido. Que valide no dice que el inventario sea el del artefacto: para eso hay que compararlo con el contenido real.",
               note_kind="coral", foot=SINT)


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
    rows = [
        ["Artefacto sustituido tras el build", "Huella del sujeto", "Sí"],
        ["Procedencia de otro repositorio", "Repositorio esperado", "Sí"],
        ["Build en un runner no confiable", "Identidad del constructor", "Sí"],
        ["Commit en una rama no esperada", "Rama o etiqueta", "Sí"],
        ["Parámetros de construcción alterados", "Parámetros esperados", "Sí"],
        ["Procedencia fabricada por quien controla el constructor", "Ninguna", "No"],
        ["Commit malicioso aprobado en la rama protegida", "Ninguna", "No"],
        ["Dependencia comprometida descargada durante el build", "Ninguna", "No"],
    ]
    return tab("Qué ataques detecta la verificación de los campos de una procedencia y cuáles pasan",
               "Tabla: la verificación de huella del sujeto, repositorio, constructor, rama y parámetros detecta cinco ataques, pero no detecta una procedencia fabricada por quien controla el constructor, un commit malicioso ya aprobado ni una dependencia comprometida que el build descargó.",
               ["Ataque", "Comprobación que lo detecta", "¿Se detecta?"], rows, [470, 280, 170], row_h=44, size=13,
               note="Es un análisis lógico de qué campo contradice qué ataque, no una medición. Una procedencia dice quién construyó qué a partir de qué; no dice que la fuente fuese benigna ni que el constructor fuera honesto.",
               note_kind="coral", foot="Análisis del autor, sin datos medidos.")


# ---------------------------------------------------------------- SE-401
def se401_matriz() -> Fig:
    rows = [
        ["Cuerpo cambiado, checksum intacto", "R", "R", "R", "R", "R", "R"],
        ["Cuerpo y checksum cambiados en el mismo host", "P", "R", "R", "R", "R", "R"],
        ["Cuerpo, firma y clave del atacante juntos", "P", "R", "P", "R", "R", "R"],
        ["Versión antigua válida servida como la última", "P", "R", "P", "P", "R", "R"],
        ["Firma corrupta con el artefacto intacto", "P", "P", "R", "R", "R", "R"],
        ["Manifiesto firmado de otro producto", "P", "P", "P", "P", "R", "R"],
        ["Archivo truncado", "R", "R", "R", "R", "R", "R"],
        ["Clave de firma robada", "P", "R", "P", "P", "P", "P"],
        ["CI comprometido que firma con la clave real", "P", "R", "P", "P", "P", "P"],
        ["Rechazados de los 9 anteriores", "2", "7", "4", "5", "7", "7"],
    ]
    return tab("Seis estrategias de verificación frente a nueve ataques (R rechaza, P deja pasar), con firmas Ed25519 reales de openssl",
               "Tabla: la estrategia 1, un checksum en la misma página, rechaza 2 de 9 ataques; la 2, un checksum por otro canal, 7; la 3, firma con clave de la misma página, 4; la 4, firma con clave fijada, 5; la 5, clave fijada más manifiesto firmado con secuencia, 7; la 6, además revocación, 7; ninguna rechaza un CI comprometido que firma con la clave real.",
               ["Ataque", "1", "2", "3", "4", "5", "6"], rows, [400, 80, 80, 80, 80, 80, 80], row_h=40, size=12,
               note="1 checksum de la misma página · 2 checksum por canal aparte · 3 firma con clave de la misma página · 4 firma con clave fijada · 5 clave fijada y manifiesto firmado con nombre y secuencia · 6 igual que 5 con revocación. La estrategia 2 rechaza el CI comprometido solo porque la huella esperada llegó por otro canal antes del compromiso.",
               note_kind="gold", foot=REAL)


def se401_costes() -> Fig:
    rows = [
        ["SHA-256", "168,5 ms · 380 MiB/s", "153,3 ms · 417 MiB/s"],
        ["SHA-512", "151,0 ms · 424 MiB/s", "102,1 ms · 627 MiB/s"],
        ["BLAKE2b", "261,3 ms · 245 MiB/s", "106,9 ms · 599 MiB/s"],
        ["SHA3-256", "245,7 ms · 261 MiB/s", "184,7 ms · 347 MiB/s"],
        ["Verificar una firma Ed25519 con un proceso openssl", "33,1 ms (OpenSSL 3.5.7)", "5,7 ms (OpenSSL 3.0.13)"],
    ]
    return tab("Costo de hashear 64 MiB y de verificar una firma, medido en dos sistemas (una lectura, cambia entre ejecuciones)",
               "Tabla: hashear 64 mebibytes con SHA-256 tarda 168,5 milisegundos en Windows y 153,3 en Ubuntu; SHA-512 151,0 y 102,1; BLAKE2b 261,3 y 106,9; SHA3-256 245,7 y 184,7; verificar una firma Ed25519 con un proceso openssl tarda 33,1 y 5,7 milisegundos.",
               ["Operación", "Windows 11", "Ubuntu WSL2"], rows, [420, 250, 250], row_h=44, size=13,
               note="El costo es de milisegundos frente a minutos de build: la verificación no se omite por rendimiento. Las cifras son una lectura de un equipo con un solo intento y cambian en cada ejecución; el 33 frente a 5,7 ms mide sobre todo el arranque del proceso openssl en cada sistema.",
               note_kind="gold", foot="Mediciones de reloj: una lectura por celda, no reproducibles al milisegundo.")


def se401_confianza() -> Fig:
    rows = [
        ["Checksum en la misma página", "Que la página no haya sido alterada", "Detecta corrupción, no manipulación"],
        ["Checksum por otro canal", "Que el segundo canal sea independiente y anterior", "No distingue un release malicioso legítimo"],
        ["Firma con clave de la misma página", "Que el atacante no controle la página", "Firma y clave del atacante pasan"],
        ["Firma con clave fijada", "Que la clave fijada sea la correcta", "Rollback y confusión entre productos"],
        ["Manifiesto firmado con secuencia", "Que el verificador recuerde la última secuencia", "Clave robada y CI comprometido"],
        ["Con revocación", "Que la lista de revocación llegue a tiempo", "El hueco entre el robo y la revocación"],
    ]
    return tab("Qué da por bueno cada estrategia de verificación y qué no cubre",
               "Tabla: un checksum en la misma página confía en que la página no se alteró y no cubre manipulación; uno por otro canal depende de la independencia del canal; una firma con clave de la misma página confía en quien publica la clave; una clave fijada cubre eso pero no el rollback; el manifiesto con secuencia cubre el rollback pero no la clave robada; la revocación cubre la clave robada tras detectarla.",
               ["Estrategia", "Confía en que", "No cubre"], rows, [280, 340, 300], row_h=52, size=12,
               note="Cada fila añade una confianza y cierra un ataque: se trata de mover la confianza a un lugar más pequeño y más fácil de proteger, no de eliminarla. La clave fijada es una raíz de confianza que hay que distribuir, rotar y proteger.",
               note_kind="gold", foot="Análisis del autor a partir de la matriz medida.")


# ---------------------------------------------------------------- SE-402
def se402_comparador() -> Fig:
    rows = [
        ["Añadir una función pública", "menor", "menor", "Acierta"],
        ["Quitar una función pública", "mayor", "mayor", "Acierta"],
        ["Renombrar un parámetro obligatorio", "mayor", "mayor", "Acierta"],
        ["Añadir un parámetro obligatorio", "mayor", "mayor", "Acierta"],
        ["Añadir un parámetro opcional al final", "menor", "menor", "Acierta"],
        ["Cambiar el valor por defecto de un parámetro", "mayor", "mayor", "Acierta"],
        ["Hacer opcional un parámetro obligatorio", "menor", "mayor", "Sobrestima"],
        ["Quitar un método de una clase", "mayor", "mayor", "Acierta"],
        ["Cambiar la escala de la nota sin tocar la firma", "mayor", "parche", "Subestima"],
        ["Cambiar el orden por defecto del listado", "mayor", "parche", "Subestima"],
        ["Lanzar una excepción nueva ante entrada inválida", "mayor", "parche", "Subestima"],
        ["Corregir un error sin cambiar la firma", "parche", "parche", "Acierta"],
    ]
    return tab("Un comparador de firmas públicas con ast frente a doce de los catorce tipos de cambio de la API de entregas",
               "Tabla: el comparador de firmas acierta el nivel de versión de 10 de 14 cambios; sobrestima uno, hacer opcional un parámetro obligatorio, y subestima tres que rompen a los clientes sin cambiar la firma: la escala de la nota, el orden por defecto del listado y una excepción nueva.",
               ["Cambio", "Nivel correcto", "Lo que ve", "Resultado"], rows, [430, 140, 140, 160], row_h=34, size=12,
               note="Acierta 10 de 14 (se omiten dos filas de acierto por espacio: añadir un método a una clase y cambiar un interno privado). Los tres errores graves son los cambios de comportamiento: la firma es idéntica y el significado cambió, y ninguna herramienta que lea solo firmas puede verlos.",
               note_kind="coral", foot=REAL)


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
    rows = [
        ["Rompe y la firma lo dice", "5", "Quitar, renombrar, añadir obligatorio, cambiar el valor por defecto, quitar método"],
        ["Rompe y la firma no lo dice", "3", "Escala de la nota, orden del listado, excepción nueva"],
        ["No rompe y la herramienta alarma", "1", "Hacer opcional un parámetro obligatorio"],
        ["Añade capacidad sin romper", "3", "Función nueva, parámetro opcional, método nuevo"],
        ["No cambia nada visible", "2", "Interno privado, corrección sin cambio de firma"],
    ]
    return tab("Los catorce cambios de la API agrupados por lo que una herramienta de firmas puede ver",
               "Tabla: de 14 cambios, 5 rompen y la firma lo delata, 3 rompen sin cambiar la firma, 1 es compatible pero provoca una alarma, 3 añaden capacidad sin romper y 2 no cambian nada visible.",
               ["Grupo", "Cambios", "Ejemplos"], rows, [310, 100, 510], row_h=52, size=13,
               note="Los 3 cambios que rompen sin cambiar la firma son el 37,5 % de los 8 incompatibles: ese es el hueco de la automatización y el motivo de las pruebas de contrato y del changelog revisado por una persona.",
               note_kind="coral", foot="Catorce cambios construidos por el autor sobre una API de cuatro elementos públicos.")


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
