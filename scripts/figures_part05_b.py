"""Figures for SE-067 to SE-072 (Python 3.12 measured on Windows 11 and Ubuntu 24.04 under WSL2)."""
from __future__ import annotations

from figure_kit import Fig
from figure_tables import finish, note, table

W = 960


def _fig(h: int, title: str, desc: str) -> Fig:
    return Fig(W, h, title, desc)


# ---------------------------------------------------------------- SE-067
def se067_texto_bytes() -> Fig:
    f = _fig(500, "Un mismo texto de nueve caracteres en cuatro codificaciones",
             "El texto 'señal-ñ-✓' tiene 9 caracteres y ocupa 13 bytes en UTF-8 y 20 en UTF-16; latin-1 y cp1252 no pueden codificar la marca de verificación y fallan en la posición 8. "
             "Leer UTF-8 como latin-1 o cp1252 produce 'seÃ±al'.")
    rows = [
        ["utf-8", "13 bytes", "7365c3b1616c… (la ñ ocupa c3 b1)"],
        ["utf-16", "20 bytes", "incluye la marca de orden de bytes fffe"],
        ["latin-1", "UnicodeEncodeError", "falla en la posición 8: ✓ no existe en latin-1"],
        ["cp1252", "UnicodeEncodeError", "falla igual: ✓ no existe en cp1252"],
        ["UTF-8 leído como latin-1 o cp1252", "'seÃ±al'", "mojibake: dos bytes se leen como dos caracteres"],
        ["b'\\xff'.decode('utf-8')", "UnicodeDecodeError", "invalid start byte: el dato no es UTF-8"],
        ["decode(errors='replace')", "'se�al'", "pierde información; surrogateescape sí permite ida y vuelta"],
    ]
    y = table(f, ["Operación", "Resultado medido", "Lectura"], rows, 10, 14, [330, 200, 410], size=13)
    y = note(f, y + 4, "Bytes y texto son tipos distintos: str tiene 9 caracteres, no 13. Toda frontera que lee o escribe debe nombrar la codificación.", "gold")
    return finish(f, y)


def se067_plataformas() -> Fig:
    f = _fig(500, "Valores por defecto que cambian con el sistema operativo",
             "En Windows la codificación preferida fue cp1252 y el salto de línea '\\r\\n'; en Linux fue UTF-8 y '\\n'. open() sin encoding leyó 'seÃ±al' en Windows y 'señal' en Linux; "
             "write_text escribió b'a\\r\\nb\\r\\n' en Windows y b'a\\nb\\n' en Linux.")
    rows = [
        ["locale.getpreferredencoding(False)", "cp1252", "UTF-8"],
        ["os.linesep", "'\\r\\n'", "'\\n'"],
        ["open(archivo).read() sin encoding de «señal» guardado en UTF-8", "'seÃ±al'", "'señal'"],
        ["Path.write_text('a\\nb\\n', encoding='utf-8')", "b'a\\r\\nb\\r\\n'", "b'a\\nb\\n'"],
        ["open(..., newline='\\n') al escribir", "b'a\\nb\\n'", "b'a\\nb\\n'"],
        ["sys.stdout.encoding (con PYTHONIOENCODING=utf-8)", "utf-8", "utf-8"],
    ]
    y = table(f, ["Medición", "Windows 11 · Python 3.12.9", "Ubuntu 24.04 (WSL2) · 3.12.3"], rows, 10, 14, [450, 245, 245], size=13)
    y = note(f, y + 4, "Un programa sin encoding explícito funciona en Linux y corrompe datos en Windows: el mismo código, otro resultado. La PEP 686 hace UTF-8 el valor por defecto a partir de Python 3.15; hasta entonces hay que declararlo.", "coral")
    y = note(f, y, "Sin PYTHONIOENCODING=utf-8 la consola de Windows (cp1252) no pudo imprimir un dígito arábigo-índico durante esta misma práctica: UnicodeEncodeError al escribir, no al calcular.", "grey", 12)
    return finish(f, y)


def se067_json() -> Fig:
    f = _fig(560, "JSON no es el modelo: ocho comportamientos de json medidos",
             "json.dumps escribe NaN salvo que se pida allow_nan=False; json.loads('1e999') devuelve inf; las claves duplicadas se resuelven con la última; True como clave se convierte en 'true'; "
             "un set o un datetime no son serializables; una tupla vuelve como lista; 100000 corchetes anidados provocan RecursionError.")
    rows = [
        ["json.dumps(float('nan'))", "NaN", "no es JSON válido (RFC 8259); allow_nan=False lanza ValueError"],
        ["json.loads('1e999')", "inf", "un número fuera de rango se vuelve infinito sin avisar"],
        ["json.loads('{\"a\":1,\"a\":2}')", "{'a': 2}", "la última clave gana: dos lectores pueden discrepar"],
        ["json.dumps({True: 1, None: 3})", "{\"true\": 1, \"null\": 3}", "las claves siempre son texto: el tipo original se pierde"],
        ["json.dumps((1, 2)) y json.loads", "[1, 2] → lista", "tupla y lista son indistinguibles al volver"],
        ["json.dumps({1, 2})  /  datetime", "TypeError", "el formato no tiene tipos para conjuntos ni fechas: hay que decidir una representación"],
        ["json.dumps(2**70) ida y vuelta", "igual", "Python conserva el entero, pero otros lectores lo redondean a double"],
        ["json.loads('[' * 100000 + ']' * 100000)", "RecursionError", "la profundidad es una superficie de ataque: limitar tamaño y estructura"],
    ]
    y = table(f, ["Operación", "Resultado medido", "Lectura"], rows, 10, 14, [330, 190, 420], size=13)
    y = note(f, y + 4, "ensure_ascii=True (por defecto) escribe señal como se\\u00f1al: el mismo JSON sale idéntico en consolas con codificaciones distintas, y por eso el laboratorio lo usa.", "gold")
    return finish(f, y)


# ---------------------------------------------------------------- SE-068
def se068_grafo() -> Fig:
    f = _fig(480, "Dependencias de importación del paquete diagnostic_cli (leídas con ast)",
             "El análisis con ast muestra que domain.py no importa ningún módulo local; engine.py y parsing.py importan solo domain; cli.py importa engine y parsing; "
             "__init__.py reexporta domain y engine; __main__.py importa cli. Líneas: domain 82, engine 109, parsing 110, cli 59, __init__ 16, __main__ 3.")
    f.box(380, 20, 200, 60, "domain.py\n82 líneas · 0 importaciones locales", "teal", 13, bold=True)
    f.box(110, 150, 200, 60, "engine.py\n109 líneas → domain", "plain", 13, bold=True)
    f.box(650, 150, 200, 60, "parsing.py\n110 líneas → domain", "plain", 13, bold=True)
    f.box(380, 270, 200, 60, "cli.py\n59 líneas → engine, parsing", "gold", 13, bold=True)
    f.box(380, 380, 200, 44, "__main__.py · 3 líneas → cli", "grey", 13)
    f.box(20, 20, 220, 60, "__init__.py · 16 líneas\nreexporta domain y engine", "grey", 13)
    f.arrow([(210, 150), (400, 80)]); f.arrow([(750, 150), (560, 80)])
    f.arrow([(400, 270), (260, 210)]); f.arrow([(560, 270), (700, 210)])
    f.arrow([(480, 380), (480, 330)])
    f.arrow([(240, 50), (380, 50)])
    f.box(640, 270, 300, 150, "Las flechas apuntan hacia lo que se importa. Ninguna flecha sale de domain: el núcleo no conoce argparse, archivos ni JSON. Un ciclo (por ejemplo domain → cli) rompería esa propiedad.", "coral", 13)
    return finish(f, 440)


def se068_ciclos() -> Fig:
    f = _fig(500, "Importaciones: caché, ciclos y sombras, medidos",
             "Importar dos veces un módulo ejecuta su cuerpo una sola vez. En un ciclo ma ↔ mb, mb se ejecuta con ma incompleto (hasattr es False); "
             "con from-import el ciclo produce ImportError por módulo parcialmente inicializado. Un archivo json.py en el directorio actual oculta al json de la biblioteca estándar; python -I lo evita.")
    rows = [
        ["import side, side", "«efecto al importar» una vez", "sys.modules cachea el módulo: el segundo import no re-ejecuta"],
        ["ma importa mb, mb importa ma", "mb ve ma sin X (hasattr → False)", "ejecución interrumpida: ma aún no terminó su cuerpo"],
        ["from md import Y / from mc import Z", "ImportError: partially initialized module", "from-import exige el nombre ya definido: el ciclo se vuelve error"],
        ["json.py local + import json", "se ejecutó «SOMBRA»", "el directorio actual precede a la biblioteca estándar en sys.path"],
        ["python -I -c 'import json'", "json ok", "el modo aislado ignora directorio actual y variables PYTHON*"],
    ]
    y = table(f, ["Experimento", "Resultado medido", "Mecanismo"], rows, 10, 14, [280, 280, 380], size=13)
    y = note(f, y + 4, "Un efecto al importar (leer un archivo, abrir red) ocurre en el momento y orden menos esperados. El laboratorio importa sin hacer nada y deja los efectos a main().", "gold")
    return finish(f, y)


def se068_importtime() -> Fig:
    f = _fig(480, "Costo acumulado de importar el paquete (python -X importtime)",
             "Tiempos acumulados de importación en milisegundos: diagnostic_cli.domain 48.0 en Windows y 78.8 en Linux, el paquete diagnostic_cli 52.5 y 115.5, parsing 0.7 y 12.7, "
             "engine 3.1 y 15.5, y diagnostic_cli.cli 68.5 y 173.7. Incluyen módulos de la biblioteca estándar como dataclasses o argparse.")
    f.text(20, 28, "Milisegundos acumulados (una ejecución por plataforma)", 14, "start", 700)
    f.hbars([("domain · Windows", 48.0, "teal", "48.0"), ("cli · Windows", 68.5, "teal", "68.5"),
             ("domain · Linux", 78.8, "gold", "78.8"), ("cli · Linux", 173.7, "gold", "173.7")], 20, 42, 3.4, label_w=200, step=40)
    y = note(f, 214, "El acumulado de domain.py es casi todo costo de la biblioteca estándar que importa (dataclasses, enum, typing): el módulo propio apenas pesa. "
             "En Linux los archivos estaban en un disco de Windows montado en WSL2 (/mnt/c), mucho más lento: las barras de Linux no miden Linux nativo.", "gold")
    y = note(f, y, "Una sola ejecución en frío por plataforma: sirve para ordenar módulos, no para fijar un presupuesto. Importar perezosamente solo vale si el arranque está medido como problema.", "coral", 12)
    return finish(f, y)


# ---------------------------------------------------------------- SE-069
def se069_mapa() -> Fig:
    f = _fig(560, "Las 15 pruebas del laboratorio y el contrato que protege cada una",
             "La suite del laboratorio ejecuta 15 pruebas: 14 aprobadas y una omitida por falta de rustc. Tarda 0.047 segundos de pruebas y 0.42 s de reloj en Windows, 0.263 y 1.03 s en Linux. "
             "Cada contrato (tipos externos, esquema, inmutabilidad, rechazos del dominio, JSONL, terminal, paquete, transferencia) tiene al menos una prueba.")
    rows = [
        ["tipos y esquema externos", "rechaza_presupuesto_booleano · rechaza_mapa_incompleto"],
        ["estado y resultado", "apply_observation_sin_mutar · resultado_imposible · candidatos_monótonos"],
        ["rechazos del dominio", "prueba_no_autorizada · observación_duplicada"],
        ["flujo", "flujo_vacío_inconcluso · línea_malformada_con_ubicación"],
        ["terminal", "salida_separada_de_diagnósticos · JSON_inválido · observaciones_ausentes · contradicción"],
        ["paquete y transferencia", "metadatos_del_paquete · puerto_Rust (omitida sin rustc)"],
    ]
    y = table(f, ["Contrato", "Pruebas (nombre abreviado)"], rows, 10, 14, [260, 680], size=13)
    y = note(f, y + 4, "Resultado: Ran 15 tests, OK (skipped=1). Tiempo de pruebas 0.047 s (Windows) y 0.263 s (Linux sobre /mnt/c); reloj incluyendo el arranque del intérprete: 0.42 s y 1.03 s.", "gold")
    y = note(f, y, "Que cada contrato tenga una prueba no dice si la prueba detecta un defecto en ese contrato. Eso lo mide la figura siguiente.", "coral", 12)
    return finish(f, y)


def se069_mutantes() -> Fig:
    f = _fig(560, "Diez mutaciones del código y qué pruebas las detectan",
             "Se aplicó una mutación a la vez a una copia del laboratorio y se ejecutó la suite: cuatro mutantes fueron detectados (repetición ignorada, autorización ignorada, bool aceptado como entero, resultado siempre resolved) "
             "y seis sobrevivieron (> cambiado por >=, límite de tamaño x10, costo ignorado al elegir, códigos 3 y 4 iguales, hipótesis duplicadas aceptadas, cota de pasos relajada).")
    rows = [
        ["repetición ignorada", "detectado", "domain_refuses_duplicate_observation"],
        ["autorización ignorada", "detectado", "domain_refuses_unauthorized_probe"],
        ["bool aceptado como entero", "detectado", "parse_rejects_boolean_budget…"],
        ["status siempre «resolved»", "detectado", "empty_stream_is_inconclusive…"],
        ["gasto > presupuesto → >=", "SOBREVIVE", "ninguna prueba toca la frontera exacta"],
        ["MAX_INPUT_BYTES ×10", "SOBREVIVE", "ninguna prueba supera el límite de 1 MB"],
        ["elegir por información sin dividir por costo", "SOBREVIVE", "el caso del laboratorio da la misma elección"],
        ["EXIT_DOMAIN_REFUSAL = 3 en vez de 4", "SOBREVIVE", "las pruebas comparan con la constante, no con el número"],
        ["hipótesis duplicadas aceptadas", "SOBREVIVE", "no hay prueba de duplicado en el esquema"],
        ["cota de pasos + 99", "SOBREVIVE", "ver siguiente figura: es equivalente"],
    ]
    y = table(f, ["Mutación", "Resultado", "Prueba que la detecta / por qué escapa"], rows, 10, 14, [330, 130, 480], size=13,
              kinds=["plain", ("teal", "teal", "teal", "teal", "coral", "coral", "coral", "coral", "coral", "coral"), "plain"])
    y = note(f, y + 2, "Cobertura de líneas alta no implica protección: seis de diez defectos plausibles pasaron una suite en verde.", "gold")
    return finish(f, y)


def se069_cierre() -> Fig:
    f = _fig(520, "Cinco pruebas nuevas cierran cinco de los seis mutantes",
             "En una copia del laboratorio se añadieron cinco pruebas: frontera exacta del presupuesto, códigos de salida numéricos, hipótesis duplicadas, límite de tamaño con líneas en blanco y elección por información por costo. "
             "Con ellas se detectaron cinco de los seis mutantes supervivientes; el sexto, la cota de pasos, es equivalente.")
    rows = [
        ["frontera: 1 + 2 = 3 se acepta y 2 + 2 > 3 se rechaza", "mata «> → >=»"],
        ["códigos literales 0, 3 y 4 (no constantes)", "mata «códigos iguales»"],
        ["hipótesis [dns, dns, tls] → duplicate_hypothesis", "mata «duplicadas aceptadas»"],
        ["1 000 001 líneas en blanco → input_too_large", "mata «límite ×10»"],
        ["una prueba barata (elimina 1, costo 1) y una cara (elimina 2, costo 10) → se elige «barato»", "mata «ignora el costo»"],
        ["cota de pasos + 99", "sobrevive: equivalente"],
    ]
    y = table(f, ["Prueba añadida (en una copia, no en el repositorio)", "Efecto medido"], rows, 10, 14, [620, 320], size=13,
              kinds=["plain", ("teal", "teal", "teal", "teal", "teal", "gold")])
    y = note(f, y + 4, "El último mutante nunca puede ser detectado: la cota es len(probes) y la regla de duplicados falla antes, así que ninguna entrada llega al paso 5. Un mutante equivalente no es un hueco de la suite, "
             "y reconocerlo es parte del análisis. Con las cinco pruebas: 20 pruebas, OK (skipped=1).", "gold")
    return finish(f, y)


# ---------------------------------------------------------------- SE-070
def se070_metricas() -> Fig:
    f = _fig(520, "Métricas leídas con ast sobre el paquete del laboratorio",
             "El paquete tiene 379 líneas y 19 funciones, todas con retorno anotado y ninguna con docstring; la media es 11.0 líneas por función. "
             "parse_spec es la mayor: 48 líneas y complejidad aproximada 26. Hay 9 líneas de más de 100 caracteres y 2 comentarios, ambos explican una causa.")
    rows = [
        ["parse_spec (parsing.py)", "48", "26", "valida decisión, presupuesto, hipótesis y cada prueba en una función"],
        ["apply_observation (engine.py)", "20", "8", "cinco rechazos y una transformación"],
        ["main (cli.py)", "31", "7", "orquesta archivos, errores y códigos de salida"],
        ["run_diagnosis (engine.py)", "33", "7", "bucle de observaciones y construcción del informe"],
        ["load_json_document (parsing.py)", "12", "6", "tamaño, codificación y JSON"],
    ]
    y = table(f, ["Función", "Líneas", "Complejidad aprox.", "Qué mezcla"], rows, 10, 14, [300, 90, 160, 390], size=13)
    y = note(f, y + 4, "Complejidad aproximada = 1 + número de if, for, while, except, operadores booleanos, expresiones condicionales y comprensiones. Es un indicador para decidir dónde mirar, no un umbral universal.", "grey", 12)
    y = note(f, y, "Los dos comentarios del paquete explican un porqué (bool hereda de int; ASCII escapado por codepages); ninguno repite el código. Ninguna función tiene docstring: la intención vive en los nombres y en los tipos.", "gold")
    return finish(f, y)


def se070_nombres() -> Fig:
    f = _fig(500, "Un nombre frente a un índice: claridad y costo medidos",
             "Leer r[1] de una tupla cuesta 29.8 nanosegundos en Windows y 20.5 en Linux; leer p.cost de un dataclass 21.7 y 15.0. El nombre es más legible y no más lento. "
             "En el paquete solo hay 78 nombres distintos y los de una o dos letras son T, OK y _.")
    f.text(20, 28, "Nanosegundos por lectura", 14, "start", 700)
    f.hbars([("r[1] · Windows", 29.8, "gold", "29.8"), ("p.cost · Windows", 21.7, "teal", "21.7"), ("r[1] · Linux", 20.5, "gold", "20.5"), ("p.cost · Linux", 15.0, "teal", "15.0")],
            20, 42, 9, label_w=190, step=40)
    rows = [["r = ('resolve', 1, True); r[1]", "¿qué es 1? exige abrir la definición"], ["probe.cost", "unidad y rol visibles en el sitio de uso"]]
    y = table(f, ["Lectura", "Lo que obliga a saber"], rows, 10, 214, [380, 560], size=13)
    y = note(f, y + 2, "En el paquete, 78 nombres distintos y solo T (variable de tipo), OK (miembro de Enum) y _ miden una o dos letras.", "gold")
    y = note(f, y, "Las diferencias de nanosegundos son ruido operativo: la razón para nombrar no es la velocidad. Un buen nombre también puede mentir: si cost deja de ser un entero, el nombre sigue prometiendo lo anterior.", "coral", 12)
    return finish(f, y)


def se070_refactor() -> Fig:
    f = _fig(500, "Refactor protegido: extraer _parse_probe de parse_spec",
             "Se extrajo el análisis de cada prueba a una función _parse_probe en una copia del laboratorio. parse_spec bajó de 48 líneas y complejidad 26 a 30 líneas y 16; "
             "_parse_probe tiene 22 líneas y complejidad 12. La suite pasó antes y después y la salida de la CLI fue idéntica.")
    rows = [
        ["parse_spec", "48 líneas · complejidad 26", "30 líneas · complejidad 16"],
        ["_parse_probe (nueva)", "—", "22 líneas · complejidad 12"],
        ["suite del laboratorio", "15 pruebas · OK (1 omitida)", "15 pruebas · OK (1 omitida); con las 5 añadidas: 20 · OK"],
        ["salida de la CLI con el caso del laboratorio", "referencia", "idéntica byte a byte"],
    ]
    y = table(f, ["Medida", "Antes", "Después"], rows, 10, 14, [300, 300, 340], size=13)
    y = note(f, y + 4, "El refactor conserva el comportamiento observable: mismos códigos de error, mismo orden de comprobaciones. La complejidad total no desaparece (16 + 12 = 28 frente a 26): se reparte en dos unidades que se leen y se prueban por separado.", "gold")
    y = note(f, y, "La red de seguridad es tan buena como las pruebas: con la suite original, un cambio que alterara la frontera del presupuesto habría pasado inadvertido (figura 2 de SE-069).", "coral", 12)
    return finish(f, y)


# ---------------------------------------------------------------- SE-071
def se071_semantica() -> Fig:
    f = _fig(560, "Misma expresión, distinta semántica: lo medido en Python y lo documentado en Rust",
             "Python midió -7 // 2 = -4, -7 % 2 = 1, enteros de precisión arbitraria (2**63 existe), len('señal✓') = 6 y round(0.5), round(1.5), round(2.5) = 0, 2, 2. "
             "Según la documentación de Rust (no ejecutada aquí) la división entera trunca, el resto toma el signo del dividendo, i32 e i64 tienen rango fijo, str::len cuenta bytes y f64::round redondea alejándose de cero.")
    rows = [
        ["-7 // 2  ·  -7 % 2", "-4  ·  1 (medido)", "-7 / 2 = -3  ·  -7 % 2 = -1 (documentado)"],
        ["entero grande", "2**63 = 9223372036854775808 (medido)", "i64 desborda: pánico en depuración, envoltura en release (documentado)"],
        ["longitud de 'señal✓'", "len = 6 caracteres; 9 bytes en UTF-8 (medido)", "s.len() = 9 bytes; s.chars().count() = 6 (documentado)"],
        ["redondeo de 0.5, 1.5, 2.5", "0, 2, 2: al par (medido)", "1, 2, 3: lejos de cero (documentado)"],
        ["ausencia", "None (dict.get devuelve None)", "Option<T>: el compilador obliga a tratar el caso (documentado)"],
        ["inf − inf", "nan (medido)", "NaN en f64 (IEEE 754, documentado)"],
    ]
    y = table(f, ["Pregunta", "Python 3.12 (ejecutado)", "Rust (solo documentación)"], rows, 10, 14, [220, 340, 380], size=13)
    y = note(f, y + 4, "rustc y cargo no estaban instalados en Windows ni en WSL2: nada de Rust se compiló ni se ejecutó en esta práctica. La columna derecha es una lectura de la documentación oficial y debe verificarse con el compilador (la integración continua del repositorio sí lo hace).", "coral")
    return finish(f, y)


def se071_contrato() -> Fig:
    f = _fig(520, "El contrato común: cuatro casos TSV reproducidos con una referencia en Python",
             "El archivo contract-cases.tsv tiene cuatro casos. Reimplementados en Python, los cuatro aceptan el costo dentro del presupuesto y conservan las hipótesis esperadas: dns; tls y http; tls; http. "
             "El puerto Rust tiene 42 líneas, usa enum, no usa Option ni Result, no declara mut ni unsafe; no se compiló porque rustc no estaba instalado.")
    rows = [
        ["resolve_dns", "presupuesto 5, gastado 0, costo 1, resultado fail", "[dns]"],
        ["resolve_not_dns", "presupuesto 5, gastado 0, costo 1, resultado ok", "[tls, http]"],
        ["handshake_tls", "presupuesto 5, gastado 1, costo 2, resultado fail", "[tls]"],
        ["request_http", "presupuesto 5, gastado 2, costo 3, resultado fail", "[http]"],
    ]
    y = table(f, ["Caso", "Entrada", "Candidatos conservados"], rows, 10, 14, [200, 470, 270], size=13)
    y = note(f, y + 4, "Lo que comparten ambos lenguajes es el contrato observable de un núcleo mínimo (filtrar hipótesis), no su arquitectura: el puerto no tiene el parser JSON ni los códigos de salida del paquete Python.", "gold")
    y = note(f, y, "Estado de la evidencia: Python ejecutado en Windows y Linux; Rust sin compilar localmente. La prueba test_rust_port_compiles_and_matches_shared_contract_cases quedó omitida y la CI de Ubuntu la exige.", "coral", 12)
    return finish(f, y)


def se071_matriz() -> Fig:
    f = _fig(520, "Qué transferir de Python a otro lenguaje: concepto, mecanismo y evidencia común",
             "Matriz de cinco conceptos del laboratorio: ausencia, errores esperados, inmutabilidad, iteración perezosa y pruebas. Para cada uno se indica cómo lo resuelve Python en el laboratorio, "
             "la construcción equivalente en Rust según su documentación y la evidencia que debe ser la misma en ambos.")
    rows = [
        ["ausencia", "None; Optional en anotaciones", "Option<T>", "mismo caso: observación desconocida"],
        ["fallo esperado", "Result propio con DomainError", "Result<T, E> estándar", "mismos códigos de rechazo"],
        ["inmutabilidad", "dataclass(frozen=True), frozenset", "bindings inmutables por defecto, mut explícito", "ningún caso modifica la entrada"],
        ["iteración", "generador de líneas JSONL", "iteradores perezosos", "misma salida con 0 y N observaciones"],
        ["pruebas", "unittest + casos TSV", "cargo test + los mismos TSV", "los cuatro casos del contrato"],
    ]
    y = table(f, ["Concepto", "Python (laboratorio)", "Rust (documentación)", "Evidencia común"], rows, 10, 14, [150, 260, 270, 260], size=13)
    y = note(f, y + 4, "Se transfiere el modelo (estados representables, errores como valores, contrato observable), no la sintaxis. Si un caso del contrato falla en un puerto, hay que decidir si cambió la regla o solo el puerto.", "gold")
    return finish(f, y)


# ---------------------------------------------------------------- SE-072
def se072_salidas() -> Fig:
    f = _fig(700, "Catorce invocaciones de la CLI y su contrato de salida (idéntico en Windows y Linux)",
             "Se invocó python -m diagnostic_cli con catorce entradas: la ruta feliz y el archivo vacío terminan con 0; la falta de argumentos con 2; JSON roto, NaN, presupuesto true y JSONL roto con 3; "
             "prueba no autorizada, repetida y contradictoria con 4; archivo ausente o con bytes no UTF-8 con 5. El código de salida y el flujo coincidieron en ambas plataformas; stdout solo tiene datos en el caso con 0.")
    rows = [
        ["caso del laboratorio", "0", "JSON de 616 bytes · resolved · [tls]"],
        ["observaciones vacías", "0", "JSON inconcluso · candidatos dns, tls, http"],
        ["sin argumentos / un argumento", "2", "argparse: «required: spec, observations»"],
        ["spec JSON roto · NaN · budget true", "3", "invalid_json · invalid_json · invalid_budget"],
        ["JSONL con la línea 2 rota", "3", "«línea 2: Expecting property name…»"],
        ["prueba no autorizada · repetida · contradictoria", "4", "unauthorized_test · duplicate_observation · contradictory_observation"],
        ["spec ausente · observaciones ausentes · bytes no UTF-8", "5", "not_found · observation_io · observation_io"],
    ]
    y = table(f, ["Entrada", "Código", "stderr (stdout vacío salvo en 0)"], rows, 10, 14, [370, 90, 480], size=13,
              kinds=["plain", "teal", "plain"])
    y = note(f, y + 4, "Hallazgo de privacidad: en los casos de archivo ausente o JSON roto, stderr incluía la ruta absoluta del archivo, y en este equipo esa ruta contenía el nombre de usuario del sistema. "
             "Un mensaje de error no debería filtrar rutas locales si el resultado se pega en un informe público; aquí se omitió de la figura.", "coral")
    y = note(f, y, "El caso «más de 1 MB de observaciones válidas» terminó con 4 (duplicate_observation), no con el límite de tamaño: la regla del dominio actúa antes de llegar a 1 MB.", "grey", 12)
    return finish(f, y)


def se072_limites() -> Fig:
    f = _fig(500, "Cómo se comportan los límites de entrada (1 MB) al probarlos de verdad",
             "Un JSONL con 1.2 millones de líneas en blanco terminó con código 3 y input_too_large en la línea 1000001; una especificación de 1.1 MB terminó con 3; "
             "40000 observaciones válidas repetidas terminaron con 4 por duplicado antes de alcanzar el límite. Con el límite multiplicado por diez, ninguna de las 15 pruebas originales falló.")
    rows = [
        ["1.2 millones de líneas en blanco (≈ 1.2 MB)", "3", "input_too_large, línea 1000001", "el contador de bytes incluye líneas vacías"],
        ["especificación JSON con 1.1 MB de espacios", "3", "input_too_large (por tamaño del archivo)", "se comprueba stat().st_size antes de leer"],
        ["40 000 líneas válidas repetidas (≈ 1.4 MB)", "4", "duplicate_observation (resolve)", "el dominio rechaza antes que el límite de bytes"],
        ["mutar MAX_INPUT_BYTES a 10 MB", "(suite en verde)", "sobrevive hasta añadir una prueba", "ver SE-069: la regla no tenía prueba"],
    ]
    y = table(f, ["Entrada", "Código", "Resultado", "Lectura"], rows, 10, 14, [300, 90, 270, 280], size=13)
    y = note(f, y + 4, "Un límite que ninguna prueba cruza es una afirmación sin evidencia. Medir también el tiempo: 1.2 MB de líneas en blanco se rechazaron en unos 424 ms de reloj total en Windows, arranque del intérprete incluido.", "gold")
    return finish(f, y)


def se072_arranque() -> Fig:
    f = _fig(560, "Arranque y entrega: lo que cuesta ejecutar la CLI y lo que declara el paquete",
             "Mediana de siete ejecuciones: python -c pass tarda 142 ms en Windows y 21 en Linux; python -I -S -c pass 53 y 11; la CLI completa con el caso del laboratorio 236 ms en Windows y 224 en Linux "
             "(en Linux los archivos estaban en un disco de Windows montado). pyproject.toml declara el paquete msep-diagnostic-cli, Python 3.11 o posterior, setuptools 68 o posterior y el comando diagnostic-cli.")
    f.text(20, 28, "Milisegundos de reloj (mediana de 7)", 14, "start", 700)
    f.hbars([("intérprete vacío · Windows", 142, "gold", "142"), ("-I -S vacío · Windows", 53, "gold", "53"), ("CLI completa · Windows", 236, "teal", "236"),
             ("intérprete vacío · Linux", 21, "gold", "21"), ("-I -S vacío · Linux", 11, "gold", "11"), ("CLI completa · Linux*", 224, "teal", "224")],
            20, 42, 2.2, label_w=250, step=36)
    rows = [["nombre del paquete", "msep-diagnostic-cli"], ["Python mínimo", ">=3.11"], ["comando", "diagnostic-cli → diagnostic_cli.cli:entrypoint"],
            ["backend de construcción", "setuptools>=68 (setuptools.build_meta)"]]
    y = table(f, ["pyproject.toml", "Valor leído"], rows, 10, 270, [300, 640], size=13)
    y = note(f, y + 2, "*Linux leyó el código desde /mnt/c (WSL2 sobre el disco de Windows): el 224 ms incluye ese costo y no representa Linux nativo. El paquete no se construyó, instaló ni publicó en esta práctica; solo se leyeron sus metadatos.", "coral", 12)
    return finish(f, y)


FIGURES = {
    "se-067-texto-y-bytes.svg": se067_texto_bytes,
    "se-067-valores-por-plataforma.svg": se067_plataformas,
    "se-067-json-no-es-el-modelo.svg": se067_json,
    "se-068-grafo-de-importaciones.svg": se068_grafo,
    "se-068-ciclos-cache-y-sombras.svg": se068_ciclos,
    "se-068-costo-de-importar.svg": se068_importtime,
    "se-069-mapa-de-pruebas.svg": se069_mapa,
    "se-069-mutantes.svg": se069_mutantes,
    "se-069-pruebas-que-cierran-huecos.svg": se069_cierre,
    "se-070-metricas-del-paquete.svg": se070_metricas,
    "se-070-nombre-o-indice.svg": se070_nombres,
    "se-070-refactor-protegido.svg": se070_refactor,
    "se-071-semantica-por-lenguaje.svg": se071_semantica,
    "se-071-contrato-comun.svg": se071_contrato,
    "se-071-matriz-de-transferencia.svg": se071_matriz,
    "se-072-contrato-de-salida.svg": se072_salidas,
    "se-072-limites-de-entrada.svg": se072_limites,
    "se-072-arranque-y-entrega.svg": se072_arranque,
}
