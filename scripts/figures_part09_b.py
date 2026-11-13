"""Figures for SE-115 to SE-120 (values measured with CPython 3.12.9 on Windows 11; Linux 3.12.3 under WSL2 where noted)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part09_a import MEDIDO, bars, tab


# ---------------------------------------------------------------- SE-115
def se115_descubrir() -> Fig:
    rows = [["0 plugins", "125,3 ms", "5,9 ms", "—", "—"],
            ["10 plugins ligeros", "102,6 ms", "7,9 ms", "5,4 ms", "1,1 ms"],
            ["50 plugins ligeros", "116,5 ms", "10,9 ms", "27,9 ms", "4,6 ms"],
            ["50 plugins que importan 7 módulos de la biblioteca estándar", "111,3 ms", "10,8 ms", "277,4 ms", "51,0 ms"]]
    return tab("Descubrir plugins cuesta poco; cargarlos todos puede costar mucho", "Tabla de arranque con entry points: descubrir 0, 10 y 50 plugins tarda entre 102 y 125 milisegundos en Windows y entre 5,9 y 10,9 en Linux, casi sin depender del número; cargar los 50 plugins ligeros cuesta 27,9 y 4,6 milisegundos y cargar los 50 que importan módulos pesados cuesta 277,4 y 51,0.",
               ["Escenario", "Descubrir: Windows", "Descubrir: Linux", "Cargar todos: Windows", "Cargar todos: Linux"], rows, [330, 150, 150, 160, 160], row_h=58,
               note="Con cero plugins el descubrimiento ya costó 125 ms en Windows: lo domina el recorrido de las distribuciones instaladas, no los plugins. Lo que escala con la cantidad es la carga ansiosa (eager); con carga perezosa el costo se paga solo por el plugin que se usa. Mejor de 3 intérpretes nuevos por celda.", note_kind="gold")


def se115_aislamiento() -> Fig:
    rows = [["El plugin falla al importarse (ImportError)", "Cae toda la aplicación", "aislado: ImportError; los demás plugins siguen"],
            ["El plugin lanza una excepción al ejecutarse", "Cae toda la aplicación", "aislado: RuntimeError; los demás siguen"],
            ["El plugin devuelve un tipo equivocado (texto en vez de entero)", "Se propaga el valor equivocado", "aislado: TypeError por validar el resultado"],
            ["El plugin se cuelga (espera 30 s)", "Bloquea a la aplicación entera", "subprocess con timeout=1,0: TimeoutExpired a los 1,0 s"],
            ["Plugins sanos (plug0 y plug5)", "2 y 11", "2 y 11: el aislamiento no los afecta"]]
    return tab("Cinco formas de fallar de un plugin, con y sin aislamiento", "Tabla de cinco fallos de plugin: un error de importación, una excepción en ejecución, un tipo de resultado equivocado y un cuelgue; sin aislamiento los tres primeros hacen caer la aplicación o propagan el valor, y el cuelgue la bloquea; con try/except, validación del resultado y un subproceso con timeout, cada fallo queda aislado y los plugins sanos devuelven 2 y 11.",
               ["Fallo del plugin", "Sin aislamiento", "Con aislamiento"], rows, [330, 270, 350], row_h=62,
               note="try/except aísla los errores pero no el cuelgue ni el consumo de memoria: para eso hace falta otro proceso con límite de tiempo. Cuanto más aislado el plugin, más costosa la comunicación; es una decisión de confianza, no una regla.", note_kind="coral", foot="Mismos resultados en Windows (3.12.9) y Linux (3.12.3).")


def se115_orden() -> Fig:
    rows = [["Orden devuelto por entry_points para plug0 … plug5", "plug0, plug1, plug2, plug3, plug4, plug5", "plug5, plug3, plug4, plug0, plug1, plug2"],
            ["Componer por 2 y luego sumar 3, con x = 5", "13", "13"],
            ["Componer sumar 3 y luego por 2, con x = 5", "16", "16"],
            ["API del anfitrión = 2; el plugin declara 1, 2, 2.5 o 3", "Acepta 2 y 2.5; rechaza 1 y 3", "Acepta 2 y 2.5; rechaza 1 y 3"]]
    return tab("Orden de carga y versión de la API del anfitrión", "Tabla de cuatro comprobaciones: el mismo código y los mismos plugins devuelven el orden alfabético en Windows y plug5, plug3, plug4, plug0, plug1, plug2 en Linux; componer dos transformaciones en orden distinto da 13 o 16; con la API del anfitrión en la versión 2, un plugin que declara 1 o 3 se rechaza y uno que declara 2 o 2.5 se acepta.",
               ["Comprobación", "Windows", "Linux (WSL2)"], rows, [350, 300, 300], row_h=58,
               note="Nada en el contrato de entry_points garantiza un orden. Si el resultado depende del orden, el anfitrión debe ordenar explícitamente (por prioridad y nombre) y rechazar plugins cuyo versión mayor de API no conozca.", note_kind="gold", foot="Medido con CPython 3.12.9 y 3.12.3; plugins creados como distribuciones sintéticas en un directorio temporal.")


# ---------------------------------------------------------------- SE-116
def se116_determinista() -> Fig:
    rows = [["Generar dos veces con el mismo esquema", "Mismo SHA-256 (729294cd8c…)", "Idéntico en Windows y Linux"],
            ["Cambiar el orden de las claves del esquema", "Mismo SHA-256", "El generador ordena antes de escribir"],
            ["Añadir una marca de tiempo al encabezado", "SHA-256 distinto cada vez", "Un generador con reloj no es reproducible"],
            ["Editar a mano la clase generada", "El SHA-256 difiere de lo regenerado", "Regenerar y comparar detecta la deriva"],
            ["ast.parse sobre la salida", "Válido: 43 nodos", "Se valida sintaxis sin ejecutar"]]
    return tab("Generación determinista y detección de deriva", "Tabla de cinco comprobaciones sobre un generador de clases: dos generaciones con el mismo esquema dan el mismo SHA-256 en Windows y Linux; cambiar el orden de las claves no cambia el resultado; una marca de tiempo lo vuelve distinto en cada ejecución; una edición manual se detecta regenerando y comparando; ast.parse valida la sintaxis con 43 nodos.",
               ["Comprobación", "Resultado", "Lectura"], rows, [330, 300, 320], row_h=58,
               note="La verificación en CI es regenerar y comparar con git diff: si difiere, alguien editó lo generado o cambió el esquema sin regenerar. Un generador que depende del reloj, del orden de un diccionario sin ordenar o de la ruta absoluta rompe esa verificación.", note_kind="teal")


def se116_dinamismo() -> Fig:
    items = [("Windows: atributo simple", 64.3, "teal", "64 ns"), ("Windows: __slots__", 89.8, "teal", "90 ns"), ("Windows: property", 112.3, "gold", "112 ns"), ("Windows: __getattr__", 201.6, "coral", "202 ns"),
             ("Linux: atributo simple", 46.7, "teal", "47 ns"), ("Linux: __slots__", 65.9, "teal", "66 ns"), ("Linux: property", 98.6, "gold", "99 ns"), ("Linux: __getattr__", 185.7, "coral", "186 ns")]
    return bars("Leer un atributo: simple, __slots__, property y __getattr__ dinámico", "Barras con el tiempo por lectura incluida la llamada de una función: en Windows 64, 90, 112 y 202 nanosegundos para atributo simple, slots, property y getattr; en Linux 47, 66, 99 y 186. Crear 500 clases tarda 3,3 ms con type, 29,4 con namedtuple y 230,7 con make_dataclass en Windows.",
                items, 2.4, "Cada medida incluye el costo de llamar a la función que lee el atributo (~50 ns), así que solo importan las diferencias: __getattr__ triplicó o cuadruplicó la lectura. La diferencia entre simple y __slots__ está dentro del ruido. Crear 500 clases: type() 3,3 ms, namedtuple 29,4 ms y make_dataclass 230,7 ms en Windows (3,0, 27,9 y 207,8 en Linux): generar clases en tiempo de importación se paga en cada arranque.", label_w=270)


def se116_inyeccion() -> Fig:
    rows = [["Plantilla NAME = «{v}» con un valor que cierra la cadena e importa os", "ast encuentra 1 Import y 1 Call", "El dato se convirtió en código"],
            ["La misma plantilla con repr(valor)", "0 Import y 0 Call; literal_eval devuelve el valor idéntico", "El dato sigue siendo dato"],
            ["Identificador «valido» o «ok_1»", "Aceptado por isidentifier y no es palabra clave", "Se puede usar como nombre"],
            ["Identificadores «class», «2x», «a b», «a;b»", "Rechazados", "Nombres de campo del esquema se validan antes de generar"]]
    return tab("Generar código desde datos: cuando el dato se convierte en código", "Tabla de cuatro comprobaciones: una plantilla con un valor hostil que cierra la cadena produce un árbol sintáctico con un Import y un Call; con repr el árbol no tiene ninguno y literal_eval devuelve el valor idéntico; los identificadores class, 2x, a b y a;b se rechazan con isidentifier y la lista de palabras clave.",
               ["Caso", "Resultado", "Lectura"], rows, [350, 320, 280], row_h=66,
               note="Se analizó con ast sin ejecutar nada. Escapar con repr (o serializar con json.dumps) y validar nombres antes de interpolarlos convierte el problema en una propiedad comprobable. exec y eval sobre texto no confiable no tienen arreglo posible: se evitan.", note_kind="coral", foot="Medido con CPython 3.12.9 sobre una cadena sintética inocua; idéntico en Linux.")


# ---------------------------------------------------------------- SE-117
def se117_metadatos() -> Fig:
    items = [("License-Expression (SPDX)", 111, "teal", "111 (31,3 %)"), ("License: texto corto", 175, "gold", "175 (49,3 %)"), ("Solo clasificador", 34, "gold", "34 (9,6 %)"),
             ("License: texto largo", 33, "coral", "33 (9,3 %)"), ("Sin dato de licencia", 2, "coral", "2 (0,6 %)")]
    return bars("Cómo declaran su licencia 355 distribuciones instaladas", "Barras con 355 distribuciones instaladas en un entorno Python 3.12.9 de Windows: 111 declaran License-Expression con identificador SPDX, 175 usan un texto corto en License, 34 solo un clasificador, 33 pegan un texto largo y 2 no declaran licencia.",
                items, 2.4, "De los 175 textos cortos, 110 (63 %) coincidían con un identificador de una lista reducida de 24 IDs SPDX; ejemplos que no coincidían: «Apache 2.0», «3-Clause BSD License», «Apache Software License». Solo el campo License-Expression (PEP 639) es una expresión formal que una máquina puede validar sin adivinar.", label_w=250, foot="Medido en un solo entorno de Windows (355 distribuciones); no se midió Linux. La lista de identificadores es mínima: un validador real usa la lista completa de SPDX.")


def se117_expresiones() -> Fig:
    rows = [["MIT", "válida"], ["MIT OR Apache-2.0", "válida"], ["GPL-2.0-only WITH Classpath-exception-2.0", "válida"], ["MIT AND (BSD-3-Clause OR Apache-2.0)", "válida"],
            ["Apache-2.0+", "válida"], ["LicenseRef-propietaria", "válida"], ["MIT/Apache-2.0", "inválida (la barra no es operador)"], ["GPLv2", "inválida (no es un identificador)"],
            ["BSD", "inválida (ambigua: hay 2, 3 y 4 cláusulas)"], ["MIT OR", "inválida (falta un operando)"], ["(MIT", "inválida (paréntesis sin cerrar)"], ["Apache 2.0", "inválida (espacio, no identificador)"]]
    return tab("Expresiones de licencia SPDX: doce casos con un validador mínimo", "Tabla de doce expresiones: MIT, MIT OR Apache-2.0, GPL-2.0-only WITH Classpath-exception-2.0, MIT AND (BSD-3-Clause OR Apache-2.0), Apache-2.0+ y LicenseRef-propietaria son válidas; MIT/Apache-2.0, GPLv2, BSD, MIT OR, (MIT y Apache 2.0 son inválidas.",
               ["Expresión", "Veredicto del validador"], rows, [520, 430], row_h=34,
               note="Un validador de gramática (operadores, paréntesis, identificadores conocidos) rechaza lo ambiguo sin interpretar derecho. Que una expresión sea válida no dice si las licencias son compatibles entre sí ni si se puede redistribuir: eso es una decisión legal que esta clase no resuelve.", note_kind="gold", foot="Validador escrito para la clase (24 identificadores); resultados deterministas, idénticos en Windows y Linux. No es asesoría legal.")


def se117_cobertura() -> Fig:
    rows = [["Markdown (.md)", "779", "0"], ["JSON (.json)", "866", "0"], ["SVG (.svg)", "582", "0"], ["HTML (.html)", "522", "0"], ["YAML (.yaml y .yml)", "365", "0"], ["Python (.py)", "62", "0"]]
    return tab("Cobertura de identificadores SPDX por archivo en este repositorio", "Tabla de 3176 archivos versionados de seis tipos medidos en el repositorio: ninguno contiene la cadena SPDX-License-Identifier en sus primeras 2000 caracteres; el repositorio declara licencias con seis archivos en la raíz y no tiene carpeta LICENSES ni .reuse.",
               ["Tipo de archivo", "Archivos revisados", "Con SPDX-License-Identifier"], rows, [380, 280, 290], row_h=40,
               note="La licencia está declarada por la raíz (LICENSE, LICENSE-CONTENT.md, NOTICE, THIRD_PARTY_NOTICES.md, ASSET_LICENSES.md, DATA_LICENSES.md), no archivo por archivo. REUSE pide una declaración inequívoca por archivo, por cabecera o por archivo de mapeo; esa propiedad no se cumple hoy y no se ejecutó la herramienta reuse, solo se buscó la cadena y los directorios. Conteo del árbol de trabajo al medir (3 194 archivos versionados).", note_kind="coral", foot="Medido con git ls-files en Windows; los conteos crecen con cada commit.")


# ---------------------------------------------------------------- SE-118
def se118_primer_exito() -> Fig:
    items = [("Windows: crear el entorno virtual", 11.5, "coral", "11,5 s"), ("Windows: instalar la rueda (sin red)", 3.3, "gold", "3,3 s"), ("Windows: primera llamada", 0.08, "teal", "0,08 s"),
             ("Linux: crear el entorno virtual", 4.8, "coral", "4,8 s"), ("Linux: instalar la rueda (sin red)", 0.7, "gold", "0,7 s"), ("Linux: primera llamada", 0.02, "teal", "0,02 s")]
    return bars("Tiempo hasta el primer éxito de un SDK nuevo", "Barras con tres pasos hasta el primer éxito: crear un entorno virtual tarda 11,5 segundos en Windows y 4,8 en Linux, instalar la rueda sin red 3,3 y 0,7, y la primera llamada 0,08 y 0,02; son tres comandos y se instala también un script de consola.",
                items, 45, "Tres comandos separan la descarga del primer resultado, y entre el 77 % y el 87 % del tiempo se va en crear el entorno, no en el SDK. Un SDK no controla ese costo, pero sí el número de pasos y que el primer ejemplo funcione sin configuración. Esta medición excluye la descarga de red.", label_w=290, foot="Medido con python -m venv y pip install --no-index sobre una rueda local; una sola pasada por plataforma.")


def se118_errores() -> Fig:
    rows = [["KeyError crudo", "8", "KeyError: 'endpoint'", "No"],
            ["Excepción propia con causa y arreglo", "8", "Falta 'endpoint'… Causa… Solución…", "Sí"],
            ["Pila de 3 funciones sin envolver", "20", "KeyError: 'endpoint'", "No"],
            ["La misma pila envuelta con raise … from None", "8", "Falta 'endpoint'. Causa… Solución…", "Sí"]]
    return tab("Calidad del error: líneas de traceback y qué dice la última", "Tabla de cuatro errores: un KeyError crudo da 8 líneas de traceback sin acción posible; una excepción propia con causa y solución da 8 líneas y la solución; una pila de tres funciones sin envolver da 20 líneas y el mismo KeyError; envuelta con raise from None vuelve a 8 líneas con causa y solución.",
               ["Caso", "Líneas de traceback", "Última línea (recortada)", "Dice cómo arreglarlo"], rows, [330, 150, 330, 140], row_h=50,
               note="Envolver el error en la frontera del SDK redujo la pila de 20 a 8 líneas y añadió la acción. El costo: `from None` oculta la causa original, útil para el usuario final pero molesta al depurar el SDK; se decide con un modo de depuración que conserve la cadena.", note_kind="teal", foot="Medido con CPython 3.12.9; las líneas de traceback incluyen rutas del equipo y no se reproducen aquí.")


def se118_obsolescencia() -> Fig:
    rows = [["Llamada a una función obsoleta desde el script principal", "0", "Aviso visible", "Se ve sin configurar nada"],
            ["La misma llamada desde un módulo de la aplicación", "0", "Silencio", "Filtro por defecto: DeprecationWarning solo se muestra en __main__"],
            ["Con -W default", "0", "Aviso visible", "El consumidor lo activa"],
            ["Con -W error::DeprecationWarning", "1", "DeprecationWarning como error", "La integración continua puede exigir cero avisos"]]
    return tab("Quién ve el aviso de obsolescencia", "Tabla de cuatro ejecuciones de una función obsoleta: llamada desde el script principal muestra el aviso; desde un módulo de la aplicación no muestra nada con la configuración por defecto; con -W default el aviso aparece; con -W error la salida es 1.",
               ["Ejecución", "Salida", "Resultado", "Lectura"], rows, [310, 90, 220, 340], row_h=66,
               note="Con stacklevel=2 el aviso apunta al código del consumidor, no al interior del SDK. Un aviso que nadie ve no cumple la función de avisar: el SDK debe documentar el plazo y la alternativa y verificar con -W error en su propia integración continua. Idéntico en Windows y Linux.", note_kind="gold")


# ---------------------------------------------------------------- SE-119
def se119_matriz() -> Fig:
    rows = [["D1: faltan los datos en package-data", "pasan", "falta data/rules.json", "FileNotFoundError al ejecutar la CLI"],
            ["D2: entry point con el nombre mal escrito (mian)", "pasan", "función no encontrada", "ImportError al ejecutar la CLI"],
            ["D3: falta py.typed", "pasan", "Linux: falta; Windows: ya incluido", "ok (no se detecta)"],
            ["D4: dependencia usada pero no declarada", "Linux: fallan; Windows: pasan", "limpia", "ModuleNotFoundError"],
            ["D5: requires-python mayor que el intérprete", "pasan", "pip rechaza construir", "pip rechaza construir"],
            ["D6: la carpeta tests/ entra en la rueda", "pasan", "tests/ en la rueda", "ok (no se detecta)"],
            ["D7: __version__ distinto de la versión del paquete", "pasan", "versión distinta", "AssertionError al comparar"]]
    return tab("Siete defectos de empaquetado frente a tres detectores", "Matriz de siete defectos inyectados en un paquete: las pruebas unitarias desde el árbol de fuentes pasan en todos salvo en uno en Linux; la inspección de la rueda detecta datos ausentes, entry point roto, py.typed ausente en Linux, requires-python, tests incluidos y versión distinta; la prueba de humo en un entorno limpio detecta datos, entry point, dependencia, requires-python y versión.",
               ["Defecto inyectado", "Pruebas unitarias en el árbol", "Inspección de la rueda", "Humo en entorno limpio"], rows, [330, 200, 220, 200], row_h=58, size=12,
               note="Las pruebas unitarias casi nunca ven un defecto de empaquetado, porque se ejecutan contra el árbol de fuentes. D4 pasó en Windows porque la dependencia estaba instalada en el sistema: el entorno ambiente ocultó el defecto. Ningún detector solo cubre los siete casos.", note_kind="coral", foot="Medido en Windows (setuptools 84.0.0, pip 24.3.1) y Linux (setuptools 68.1.2, pip 24.0).")


def se119_cobertura() -> Fig:
    items = [("Pruebas unitarias en el árbol", 0, "coral", "0 de 7 (Windows) · 1 de 7 (Linux)"), ("Inspección de la rueda", 5, "gold", "5 de 7 (Windows) · 6 de 7 (Linux)"),
             ("Humo en entorno limpio", 5, "gold", "5 de 7 (ambos)"), ("Inspección + humo", 6, "teal", "6 de 7 (Windows) · 7 de 7 (Linux)")]
    return bars("Cuántos de los siete defectos detecta cada capa", "Barras con los defectos detectados de siete: las pruebas unitarias detectan 0 en Windows y 1 en Linux; la inspección de la rueda 5 en Windows y 6 en Linux; el humo en entorno limpio 5 en ambos; la combinación de inspección y humo 6 en Windows y 7 en Linux.",
                items, 55, "La diferencia entre plataformas no está en el código sino en la cadena de herramientas: setuptools 84.0.0 incluyó py.typed por sí solo y setuptools 68.1.2 no. El mismo pyproject.toml produjo ruedas distintas, así que el backend de construcción debe fijarse en build-system.requires.", label_w=280, width=1020, note_kind="teal")


def se119_contenido() -> Fig:
    rows = [["Base: paquete, CLI, py.typed y datos", "2 048 B", "2 043 B", "9 entradas, incluida RECORD"],
            ["D1: sin package-data", "1 867 B", "1 710 B", "Sin data/rules.json (y sin py.typed en Linux)"],
            ["D3: sin py.typed en package-data", "2 048 B", "1 891 B", "Windows lo sigue incluyendo; Linux no"],
            ["D6: include = «*»", "2 473 B", "2 472 B", "Añade tests/__init__.py y test_capkit.py"]]
    return tab("Qué contiene la rueda según la configuración", "Tabla con el tamaño de cuatro ruedas: la base mide 2048 bytes en Windows y 2043 en Linux; sin package-data mide 1867 y 1710; sin py.typed 2048 y 1891; incluyendo todos los paquetes con include igual a asterisco mide 2473 y 2472 y añade la carpeta de pruebas.",
               ["Variante", "Windows", "Linux (WSL2)", "Qué cambia en el contenido"], rows, [330, 120, 130, 370], row_h=56,
               note="El tamaño es una señal barata: un cambio inesperado entre dos construcciones obliga a mirar qué entró o salió. Se compara el listado de la rueda (zipfile.namelist) con una lista esperada y se falla si difiere.", note_kind="gold")


# ---------------------------------------------------------------- SE-120
def se120_detectores() -> Fig:
    rows = [["M1 parámetro opcional nuevo (control)", "MINOR", "0", "0"], ["M2 renombrar limit a max_items", "MAJOR", "1", "1"], ["M3 renombrar policy a strategy", "MAJOR", "0", "0"],
            ["M4 desempate por id descendente", "—", "4", "4"], ["M5 ordenar la entrada en sitio", "—", "0", "1"], ["M6 ParseError deja de heredar ValueError", "MAJOR", "1", "1"],
            ["M7 eliminar la constante DEFAULT_LIMIT", "MAJOR", "0", "0"], ["M8 devolver tupla en vez de lista", "—", "5", "5"], ["M9 limit pasa de None a 2", "REVISAR", "2", "2"],
            ["M10 policy pasa a obligatorio", "MAJOR", "5", "5"], ["M11 cambiar el texto del error", "—", "0", "0"], ["M12 mover choose_next a un nombre privado", "MAJOR", "1", "1"]]
    return tab("Doce cambios a un SDK: ¿los ve la comparación de API o las pruebas de contrato?", "Tabla de doce mutantes de un SDK de ejemplo: la comparación de superficie de API detecta renombres, eliminaciones, cambios de herencia y de obligatoriedad pero no los cambios de comportamiento; las ocho pruebas de contrato detectan los cambios de comportamiento pero no los renombres usados por posición ni la constante; el cambio de texto de error no lo detecta ninguno; ordenar la entrada en sitio solo lo detectan las pruebas con fixtures frescas.",
               ["Mutante", "Comparación de API", "Pruebas que fallan (fixture compartida)", "Pruebas que fallan (fixture fresca)"], rows, [380, 150, 210, 210], row_h=34, size=12,
               note="Solo la comparación vio M3, M7 y el control M1; solo las pruebas vieron M4 y M8; ambas vieron cinco; ninguna vio M11 (un texto de error) y, con fixtures compartidas, tampoco M5: la primera prueba ordenó la lista y la prueba de no mutación leyó la lista ya ordenada.", note_kind="coral", foot="Cuentas deterministas sobre un SDK de 12 líneas; idénticas en Windows (3.12.9) y Linux (3.12.3).")


def se120_golden() -> Fig:
    rows = [["Windows, salida por defecto", "43", "2", "86ca59242a63", "Los saltos de línea son CRLF y la ñ ocupa 1 byte (cp1252)"],
            ["Windows con reconfigure(newline='\\n', encoding='utf-8')", "42", "0", "526a8c1a6a2b", "Igual que Linux"],
            ["Linux, salida por defecto", "42", "0", "526a8c1a6a2b", "LF y UTF-8"],
            ["Linux con reconfigure", "42", "0", "526a8c1a6a2b", "Sin cambios"]]
    return tab("Salida de la CLI como archivo de referencia: los bytes, no el texto", "Tabla con la salida de una CLI de dos líneas, una de ellas JSON con ñ: en Windows por defecto son 43 bytes con 2 saltos CRLF y un SHA-256 distinto; fijando salto de línea y UTF-8 son 42 bytes con 0 CRLF y el mismo SHA-256 que Linux, 526a8c1a6a2b.",
               ["Configuración", "Bytes", "CRLF", "SHA-256 (12 primeros)", "Lectura"], rows, [310, 70, 70, 180, 320], row_h=62,
               note="Comparar con un archivo de referencia (golden) sin fijar codificación y salto de línea hace que la misma prueba pase en Linux y falle en Windows. Para la CLI de un SDK, el contrato incluye los bytes de la salida --json: se fijan en el programa, no en la prueba.", note_kind="teal")


def se120_reproducible() -> Fig:
    rows = [["Construir dos veces con fechas de archivo distintas, sin SOURCE_DATE_EPOCH", "d7602c9bdc1d ≠ 61f7d211f57b", "4ea2ed489fad ≠ 77b4ed888892"],
            ["Construir dos veces con SOURCE_DATE_EPOCH=1700000000", "5748444b389c = 5748444b389c", "87fd805e4a0c = 87fd805e4a0c"],
            ["Comparar la rueda de Windows con la de Linux (con la variable)", "5748444b389c", "87fd805e4a0c (distinta)"],
            ["Permisos guardados en la rueda (external_attr)", "0o100666", "0o100644"]]
    return tab("Compilaciones reproducibles: mismo código, mismo hash", "Tabla de cuatro comprobaciones con SHA-256 abreviados: sin SOURCE_DATE_EPOCH dos construcciones con distinta fecha de archivos dan hashes distintos en Windows y en Linux; con la variable fijada cada plataforma da el mismo hash dos veces; entre plataformas difieren, porque los permisos guardados en la rueda son 0o100666 en Windows y 0o100644 en Linux.",
               ["Comprobación", "Windows (3.12.9)", "Linux (3.12.3)"], rows, [430, 270, 250], row_h=62,
               note="La reproducibilidad exige entradas fijadas: fecha (SOURCE_DATE_EPOCH), herramientas y plataforma. Esta medición no la logró entre sistemas operativos; la evidencia de un release debe registrar dónde se construyó y declarar que el hash es válido para ese entorno. El hash prueba integridad, no ausencia de defectos.", note_kind="gold")


FIGURES = {
    "se-115-descubrir-y-cargar.svg": se115_descubrir,
    "se-115-aislamiento-de-fallos.svg": se115_aislamiento,
    "se-115-orden-y-version-de-api.svg": se115_orden,
    "se-116-generacion-determinista.svg": se116_determinista,
    "se-116-costo-del-dinamismo.svg": se116_dinamismo,
    "se-116-inyeccion-en-plantillas.svg": se116_inyeccion,
    "se-117-metadatos-de-licencia.svg": se117_metadatos,
    "se-117-expresiones-spdx.svg": se117_expresiones,
    "se-117-cobertura-de-licencia-del-repo.svg": se117_cobertura,
    "se-118-tiempo-hasta-el-primer-exito.svg": se118_primer_exito,
    "se-118-calidad-del-error.svg": se118_errores,
    "se-118-avisos-de-obsolescencia.svg": se118_obsolescencia,
    "se-119-matriz-de-defectos.svg": se119_matriz,
    "se-119-cobertura-por-capa.svg": se119_cobertura,
    "se-119-contenido-de-la-rueda.svg": se119_contenido,
    "se-120-detectores-de-incompatibilidad.svg": se120_detectores,
    "se-120-salida-golden.svg": se120_golden,
    "se-120-compilaciones-reproducibles.svg": se120_reproducible,
}
