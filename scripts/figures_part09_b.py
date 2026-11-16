"""Figures for SE-115 to SE-120 (values measured with CPython 3.12.9 on Windows 11; Linux 3.12.3 under WSL2 where noted)."""
from __future__ import annotations

from figure_kit import Fig, fmt_es, grouped_bars, heatmap, stacked_bars
from figures_part09_a import MEDIDO, bars, bx, done, sketch


# ---------------------------------------------------------------- SE-115






# ---------------------------------------------------------------- SE-116


def se116_dinamismo() -> Fig:
    items = [("Windows: atributo simple", 64.3, "teal", "64 ns"), ("Windows: __slots__", 89.8, "teal", "90 ns"), ("Windows: property", 112.3, "gold", "112 ns"), ("Windows: __getattr__", 201.6, "coral", "202 ns"),
             ("Linux: atributo simple", 46.7, "teal", "47 ns"), ("Linux: __slots__", 65.9, "teal", "66 ns"), ("Linux: property", 98.6, "gold", "99 ns"), ("Linux: __getattr__", 185.7, "coral", "186 ns")]
    return bars("Leer un atributo: simple, __slots__, property y __getattr__ dinámico", "Barras con el tiempo por lectura incluida la llamada de una función: en Windows 64, 90, 112 y 202 nanosegundos para atributo simple, slots, property y getattr; en Linux 47, 66, 99 y 186. Crear 500 clases tarda 3,3 ms con type, 29,4 con namedtuple y 230,7 con make_dataclass en Windows.",
                items, 2.4, "Cada medida incluye el costo de llamar a la función que lee el atributo (~50 ns), así que solo importan las diferencias: __getattr__ triplicó o cuadruplicó la lectura. La diferencia entre simple y __slots__ está dentro del ruido. Crear 500 clases: type() 3,3 ms, namedtuple 29,4 ms y make_dataclass 230,7 ms en Windows (3,0, 27,9 y 207,8 en Linux): generar clases en tiempo de importación se paga en cada arranque.", label_w=270)




# ---------------------------------------------------------------- SE-117
def se117_metadatos() -> Fig:
    items = [("License-Expression (SPDX)", 111, "teal", "111 (31,3 %)"), ("License: texto corto", 175, "gold", "175 (49,3 %)"), ("Solo clasificador", 34, "gold", "34 (9,6 %)"),
             ("License: texto largo", 33, "coral", "33 (9,3 %)"), ("Sin dato de licencia", 2, "coral", "2 (0,6 %)")]
    return bars("Cómo declaran su licencia 355 distribuciones instaladas", "Barras con 355 distribuciones instaladas en un entorno Python 3.12.9 de Windows: 111 declaran License-Expression con identificador SPDX, 175 usan un texto corto en License, 34 solo un clasificador, 33 pegan un texto largo y 2 no declaran licencia.",
                items, 2.4, "De los 175 textos cortos, 110 (63 %) coincidían con un identificador de una lista reducida de 24 IDs SPDX; ejemplos que no coincidían: «Apache 2.0», «3-Clause BSD License», «Apache Software License». Solo el campo License-Expression (PEP 639) es una expresión formal que una máquina puede validar sin adivinar.", label_w=250, foot="Medido en un solo entorno de Windows (355 distribuciones); no se midió Linux. La lista de identificadores es mínima: un validador real usa la lista completa de SPDX.")






# ---------------------------------------------------------------- SE-118
def se118_primer_exito() -> Fig:
    items = [("Windows: crear el entorno virtual", 11.5, "coral", "11,5 s"), ("Windows: instalar la rueda (sin red)", 3.3, "gold", "3,3 s"), ("Windows: primera llamada", 0.08, "teal", "0,08 s"),
             ("Linux: crear el entorno virtual", 4.8, "coral", "4,8 s"), ("Linux: instalar la rueda (sin red)", 0.7, "gold", "0,7 s"), ("Linux: primera llamada", 0.02, "teal", "0,02 s")]
    return bars("Tiempo hasta el primer éxito de un SDK nuevo", "Barras con tres pasos hasta el primer éxito: crear un entorno virtual tarda 11,5 segundos en Windows y 4,8 en Linux, instalar la rueda sin red 3,3 y 0,7, y la primera llamada 0,08 y 0,02; son tres comandos y se instala también un script de consola.",
                items, 45, "Tres comandos separan la descarga del primer resultado, y entre el 77 % y el 87 % del tiempo se va en crear el entorno, no en el SDK. Un SDK no controla ese costo, pero sí el número de pasos y que el primer ejemplo funcione sin configuración. Esta medición excluye la descarga de red.", label_w=290, foot="Medido con python -m venv y pip install --no-index sobre una rueda local; una sola pasada por plataforma.")






# ---------------------------------------------------------------- SE-119


def se119_cobertura() -> Fig:
    items = [("Pruebas unitarias en el árbol", 0, "coral", "0 de 7 (Windows) · 1 de 7 (Linux)"), ("Inspección de la rueda", 5, "gold", "5 de 7 (Windows) · 6 de 7 (Linux)"),
             ("Humo en entorno limpio", 5, "gold", "5 de 7 (ambos)"), ("Inspección + humo", 6, "teal", "6 de 7 (Windows) · 7 de 7 (Linux)")]
    return bars("Cuántos de los siete defectos detecta cada capa", "Barras con los defectos detectados de siete: las pruebas unitarias detectan 0 en Windows y 1 en Linux; la inspección de la rueda 5 en Windows y 6 en Linux; el humo en entorno limpio 5 en ambos; la combinación de inspección y humo 6 en Windows y 7 en Linux.",
                items, 55, "La diferencia entre plataformas no está en el código sino en la cadena de herramientas: setuptools 84.0.0 incluyó py.typed por sí solo y setuptools 68.1.2 no. El mismo pyproject.toml produjo ruedas distintas, así que el backend de construcción debe fijarse en build-system.requires.", label_w=280, width=1020, note_kind="teal")




# ---------------------------------------------------------------- SE-120






# ---------------------------------------------------------------- SE-115
def se115_descubrir() -> Fig:
    return grouped_bars("Descubrir plugins cuesta poco; cargarlos todos puede costar mucho", "Barras horizontales con el tiempo de descubrir y de cargar 0, 10 y 50 plugins ligeros y 50 que importan siete módulos: descubrir ronda 102 a 125 ms en Windows y 5,9 a 10,9 ms en Linux casi sin depender del número de plugins; cargar los 50 ligeros cuesta 27,9 y 4,6 ms y cargar los 50 pesados cuesta 277,4 y 51,0 ms.",
                        ["0 plugins", "10 plugins ligeros", "50 plugins ligeros", "50 plugins que importan 7 módulos"],
                        [("Descubrir: Windows", [125.3, 102.6, 116.5, 111.3], "coral"), ("Descubrir: Linux", [5.9, 7.9, 10.9, 10.8], "teal"), ("Cargar todos: Windows", [0, 5.4, 27.9, 277.4], "gold"), ("Cargar todos: Linux", [0, 1.1, 4.6, 51.0], "navy")],
                        unit="ms, mejor de 3 intérpretes nuevos", horizontal=True, decimals=1, value_fmt=lambda v: "—" if v == 0 else fmt_es(v, 1), label_w=210, plot_h=300,
                        note="Con cero plugins el descubrimiento ya costó 125 ms en Windows: lo domina el recorrido de las distribuciones instaladas, no los plugins. Lo que escala con la cantidad es la carga ansiosa (eager); con carga perezosa el costo se paga solo por el plugin que se usa. «—» = no aplica con cero plugins.", note_kind="gold", foot=MEDIDO)


def se115_aislamiento() -> Fig:
    f, y = sketch("Cinco formas de fallar de un plugin: qué capa de aislamiento corta cada una",
                  "Diagrama de capas: un subproceso con timeout=1,0 segundos envuelve a un bloque try/except con validación del resultado, que envuelve al plugin. ImportError y RuntimeError los corta el try/except; el texto en vez de entero lo corta la validación como TypeError; el cuelgue de 30 s lo corta el timeout a los 1,0 s; sin aislamiento los tres primeros hacen caer la aplicación o propagan el valor y el cuelgue la bloquea. Los plugins sanos plug0 y plug5 siguen devolviendo 2 y 11.")
    f.group(10, y + 4, 600, 270, "Subproceso con timeout = 1,0 s", "grey")
    f.group(30, y + 40, 560, 190, "try/except y validación del tipo del resultado", "teal")
    bx(f, 60, y + 80, 500, 56, "plugin: se importa, se ejecuta y devuelve un resultado", "plain", 14, True)
    bx(f, 60, y + 146, 240, 66, "ImportError al importarse · RuntimeError al ejecutarse → aislados, los demás siguen", "teal")
    bx(f, 320, y + 146, 240, 66, "Devuelve texto en vez de entero → TypeError por validar el resultado", "teal")
    bx(f, 30, y + 232, 560, 34, "Se cuelga (espera 30 s) → TimeoutExpired a los 1,0 s", "gold", 13, True)
    bx(f, 640, y + 20, 290, 70, "Sin aislamiento: ImportError y RuntimeError hacen caer toda la aplicación", "coral")
    bx(f, 640, y + 100, 290, 56, "Sin aislamiento: el tipo equivocado se propaga como valor", "coral")
    bx(f, 640, y + 166, 290, 56, "Sin aislamiento: el cuelgue bloquea a la aplicación entera", "coral")
    bx(f, 640, y + 232, 290, 42, "Plugins sanos plug0 y plug5: 2 y 11, sin cambio", "plain")
    return done(f, y + 286, "try/except aísla los errores pero no el cuelgue ni el consumo de memoria: para eso hace falta otro proceso con límite de tiempo. Cuanto más aislado el plugin, más costosa la comunicación; es una decisión de confianza, no una regla.", "coral", "Mismos resultados en Windows (3.12.9) y Linux (3.12.3).")


def se115_orden() -> Fig:
    f, y = sketch("Orden de carga y versión de la API: lo que el contrato no garantiza",
                  "Diagrama de tres comprobaciones: entry_points devuelve plug0 a plug5 en orden alfabético en Windows y plug5, plug3, plug4, plug0, plug1, plug2 en Linux; componer por 2 y luego sumar 3 con x = 5 da 13, mientras que sumar 3 y luego por 2 da 16; con la API del anfitrión en la versión 2, un plugin que declara 2 o 2.5 se acepta y uno que declara 1 o 3 se rechaza.")
    f.text(10, y + 14, "1. El mismo código devuelve otro orden", 14, "start", 700, "#142231")
    bx(f, 10, y + 24, 80, 34, "Windows", "navy", 13, True)
    bx(f, 100, y + 24, 830, 34, "plug0, plug1, plug2, plug3, plug4, plug5", "teal")
    bx(f, 10, y + 66, 80, 34, "Linux", "navy", 13, True)
    bx(f, 100, y + 66, 830, 34, "plug5, plug3, plug4, plug0, plug1, plug2", "coral")
    f.text(10, y + 134, "2. El orden cambia el resultado (x = 5; igual en Windows y Linux)", 14, "start", 700, "#142231")
    bx(f, 10, y + 146, 70, 36, "x = 5", "plain", 14, True)
    bx(f, 130, y + 146, 100, 36, "por 2 → 10", "plain")
    bx(f, 280, y + 146, 100, 36, "+ 3 → 13", "teal", 13, True)
    bx(f, 130, y + 192, 100, 36, "+ 3 → 8", "plain")
    bx(f, 280, y + 192, 100, 36, "por 2 → 16", "coral", 13, True)
    f.arrow([(80, y + 164), (130, y + 164)])
    f.arrow([(230, y + 164), (280, y + 164)])
    f.arrow([(80, y + 170), (105, y + 210), (130, y + 210)])
    f.arrow([(230, y + 210), (280, y + 210)])
    f.text(10, y + 252, "Nada en el contrato de entry_points fija\nel orden: si importa, ordena el anfitrión.", 13, "start", 400, "#32505f")
    f.text(480, y + 134, "3. Versión de la API (anfitrión = 2)", 14, "start", 700, "#142231")
    f.line(500, y + 190, 920, y + 190, "#32505f", width=2)
    for v, xx, k in ((1, 520, "coral"), (2, 640, "teal"), (2.5, 740, "teal"), (3, 860, "coral")):
        f.dot(xx, y + 190, "", "teal" if k == "teal" else "coral")
        f.text(xx, y + 222, f"declara {str(v).replace('.', ',')}", 13, "middle", 700, "#142231")
        f.text(xx, y + 166, "acepta" if k == "teal" else "rechaza", 13, "middle", 400, "#0b3f45" if k == "teal" else "#5c1f14")
    f.text(500, y + 252, "Se acepta la misma versión mayor\n(2 y 2.5); se rechazan 1 y 3.", 13, "start", 400, "#32505f")
    return done(f, y + 290, "Si el resultado depende del orden, el anfitrión debe ordenar explícitamente (por prioridad y nombre) y rechazar plugins cuya versión mayor de API no conozca.", "gold", "Medido con CPython 3.12.9 y 3.12.3; plugins creados como distribuciones sintéticas en un directorio temporal.")


# ---------------------------------------------------------------- SE-116
def se116_determinista() -> Fig:
    f, y = sketch("Generación determinista: qué cambia el SHA-256 de la salida y qué no",
                  "Diagrama de cuatro variaciones de un generador de clases frente al SHA-256 de la salida: generar dos veces con el mismo esquema y cambiar el orden de las claves dan el mismo SHA-256 (729294cd8c…), idéntico en Windows y Linux; añadir una marca de tiempo da uno distinto cada vez y editar a mano la clase generada da uno distinto del regenerado, y regenerar y comparar detecta la deriva. ast.parse valida la sintaxis sin ejecutar: 43 nodos.")
    inputs = [("Generar dos veces con el mismo esquema", "teal"), ("Cambiar el orden de las claves del esquema (el generador ordena antes de escribir)", "teal"), ("Añadir una marca de tiempo al encabezado", "coral"), ("Editar a mano la clase generada", "coral")]
    for i, (t, k) in enumerate(inputs):
        top = y + 8 + i * 74
        bx(f, 10, top, 360, 62, t, k)
        f.arrow([(370, top + 31), (470, top + 31)])
    bx(f, 470, y + 8, 220, 62, "SHA-256 igual: 729294cd8c…", "teal", 13, True)
    bx(f, 470, y + 82, 220, 62, "SHA-256 igual (el orden no importa)", "teal", 13, True)
    bx(f, 470, y + 156, 220, 62, "SHA-256 distinto cada vez", "coral", 13, True)
    bx(f, 470, y + 230, 220, 62, "SHA-256 distinto del regenerado", "coral", 13, True)
    bx(f, 730, y + 8, 200, 136, "Reproducible: idéntico en Windows y Linux", "teal")
    bx(f, 730, y + 156, 200, 62, "Un generador con reloj no es reproducible", "coral")
    bx(f, 730, y + 230, 200, 62, "Regenerar y comparar detecta la deriva", "gold")
    f.arrow([(690, y + 39), (730, y + 39)])
    f.arrow([(690, y + 113), (730, y + 113)])
    f.arrow([(690, y + 187), (730, y + 187)])
    f.arrow([(690, y + 261), (730, y + 261)])
    bx(f, 10, y + 308, 920, 38, "ast.parse sobre la salida: válido, 43 nodos; la sintaxis se valida sin ejecutar nada.", "grey")
    return done(f, y + 360, "La verificación en CI es regenerar y comparar con git diff: si difiere, alguien editó lo generado o cambió el esquema sin regenerar. Un generador que depende del reloj, del orden de un diccionario sin ordenar o de la ruta absoluta rompe esa verificación.", "teal", MEDIDO)


def se116_inyeccion() -> Fig:
    f, y = sketch("Generar código desde datos: cuando el dato se convierte en código",
                  "Diagrama de dos canalizaciones con un valor hostil que cierra la cadena e importa os: en la plantilla NAME = «{v}» el análisis con ast encuentra 1 Import y 1 Call, así que el dato se convirtió en código; con repr(valor) encuentra 0 Import y 0 Call y literal_eval devuelve el valor idéntico. Los identificadores valido y ok_1 pasan isidentifier y los nombres class, 2x, a b y a;b se rechazan antes de generar.")
    for i, (label, steps, kind, out) in enumerate((("Plantilla NAME = «{v}»", ["valor que cierra la cadena e importa os", "se interpola tal cual en el texto de la plantilla", "ast.parse: 1 Import y 1 Call"], "coral", "El dato se convirtió en código"),
                                                   ("Plantilla con repr(valor)", ["el mismo valor hostil", "repr lo escapa como literal de texto", "ast.parse: 0 Import y 0 Call; literal_eval devuelve el valor idéntico"], "teal", "El dato sigue siendo dato"))):
        top = y + 8 + i * 124
        f.text(10, top + 12, label, 14, "start", 700, "#142231")
        cw = 215
        for j, s in enumerate(steps):
            bx(f, 10 + j * (cw + 28), top + 24, cw, 74, s, "plain" if j < 2 else kind)
            if j:
                f.arrow([(10 + j * (cw + 28) - 28, top + 61), (10 + j * (cw + 28), top + 61)])
        f.arrow([(10 + 3 * (cw + 28) - 28, top + 61), (10 + 3 * (cw + 28) - 6, top + 61)])
        bx(f, 10 + 3 * (cw + 28), top + 24, 920 - 10 - 3 * (cw + 28) + 10 - 10, 74, out, kind, 13, True)
    top = y + 264
    f.text(10, top + 12, "Antes de generar: se validan los nombres de campo del esquema", 14, "start", 700, "#142231")
    bx(f, 10, top + 24, 300, 56, "«valido» y «ok_1»: isidentifier y no son palabra clave → aceptados", "teal")
    bx(f, 330, top + 24, 300, 56, "«class», «2x», «a b» y «a;b» → rechazados", "coral")
    bx(f, 650, top + 24, 280, 56, "exec y eval sobre texto no confiable no tienen arreglo: se evitan", "gold")
    return done(f, top + 96, "Se analizó con ast sin ejecutar nada. Escapar con repr (o serializar con json.dumps) y validar nombres antes de interpolarlos convierte el problema en una propiedad comprobable.", "coral", "Medido con CPython 3.12.9 sobre una cadena sintética inocua; idéntico en Linux.")


# ---------------------------------------------------------------- SE-117
def se117_expresiones() -> Fig:
    f, y = sketch("Expresiones de licencia SPDX: la gramática y dónde falla cada rechazo",
                  "Diagrama de la gramática que aplica un validador mínimo: operandos que son identificadores conocidos o LicenseRef, un sufijo opcional más o WITH, operadores AND y OR y paréntesis balanceados. Las seis expresiones válidas son MIT, MIT OR Apache-2.0, GPL-2.0-only WITH Classpath-exception-2.0, MIT AND (BSD-3-Clause OR Apache-2.0), Apache-2.0+ y LicenseRef-propietaria; las seis inválidas fallan cada una en una regla: barra, identificador desconocido, ambigüedad, operando ausente, paréntesis sin cerrar y espacio.")
    bx(f, 10, y + 8, 920, 34, "Válidas (6 de 12): se acepta lo que cumple la gramática", "teal", 14, True)
    ok = ["MIT", "MIT OR Apache-2.0", "GPL-2.0-only WITH Classpath-exception-2.0", "MIT AND (BSD-3-Clause OR Apache-2.0)", "Apache-2.0+", "LicenseRef-propietaria"]
    cw = (920 - 5 * 8) / 6
    for i, t in enumerate(ok):
        bx(f, 10 + i * (cw + 8), y + 48, cw, 74, t, "plain", 13)
    bx(f, 10, y + 142, 920, 34, "Inválidas (6 de 12): cada una rompe una regla distinta", "coral", 14, True)
    bad = [("Operador", "MIT/Apache-2.0", "la barra no es operador"), ("Identificador", "GPLv2", "no es un identificador de la lista"), ("Ambigüedad", "BSD", "hay licencias de 2, 3 y 4 cláusulas"),
           ("Operando", "MIT OR", "falta un operando"), ("Paréntesis", "(MIT", "paréntesis sin cerrar"), ("Espacio", "Apache 2.0", "espacio: no es un identificador")]
    for i, (rule, expr, why) in enumerate(bad):
        x = 10 + i * (cw + 8)
        bx(f, x, y + 182, cw, 30, rule, "navy", 13, True)
        bx(f, x, y + 216, cw, 40, expr, "plain", 13, True)
        f.arrow([(x + cw / 2, y + 256), (x + cw / 2, y + 270)])
        bx(f, x, y + 270, cw, 74, why, "coral", 13)
    return done(f, y + 358, "Un validador de gramática (operadores, paréntesis, identificadores conocidos) rechaza lo ambiguo sin interpretar derecho. Que una expresión sea válida no dice si las licencias son compatibles entre sí ni si se puede redistribuir: eso es una decisión legal que esta clase no resuelve.", "gold", "Validador escrito para la clase (24 identificadores); resultados deterministas, idénticos en Windows y Linux. No es asesoría legal.")


def se117_cobertura() -> Fig:
    return grouped_bars("Cobertura de identificadores SPDX por archivo en este repositorio", "Barras horizontales con los archivos versionados de seis tipos y cuántos contienen SPDX-License-Identifier: Markdown 779, JSON 866, SVG 582, HTML 522, YAML 365 y Python 62, 3176 en total, y en ninguno hay la cadena en las primeras 2000 caracteres.",
                        ["JSON (.json)", "Markdown (.md)", "SVG (.svg)", "HTML (.html)", "YAML (.yaml y .yml)", "Python (.py)"],
                        [("Archivos revisados", [866, 779, 582, 522, 365, 62], "navy"), ("Con SPDX-License-Identifier", [0, 0, 0, 0, 0, 0], "coral")],
                        unit="archivos versionados", horizontal=True, label_w=170,
                        note="La licencia está declarada por la raíz (LICENSE, LICENSE-CONTENT.md, NOTICE, THIRD_PARTY_NOTICES.md, ASSET_LICENSES.md, DATA_LICENSES.md), no archivo por archivo. REUSE pide una declaración inequívoca por archivo, por cabecera o por archivo de mapeo; esa propiedad no se cumple hoy y no se ejecutó la herramienta reuse, solo se buscó la cadena y los directorios. Conteo del árbol de trabajo al medir (3 194 archivos versionados).", note_kind="coral", foot="Medido con git ls-files en Windows; los conteos crecen con cada commit.")


# ---------------------------------------------------------------- SE-118
def se118_errores() -> Fig:
    return stacked_bars("Calidad del error: líneas de traceback y si dicen cómo arreglarlo", "Barras horizontales con las líneas de traceback de cuatro errores, en coral los que no dicen cómo arreglarlo y en verde azulado los que sí: un KeyError crudo da 8 líneas sin acción posible; una excepción propia con causa y solución da 8 líneas con la solución; una pila de tres funciones sin envolver da 20 líneas y el mismo KeyError; la misma pila envuelta con raise from None vuelve a 8 líneas con causa y solución.",
                        ["KeyError crudo", "Excepción propia con causa y arreglo", "Pila de 3 funciones sin envolver", "La misma pila con raise … from None"],
                        [("No dice cómo arreglarlo", [8, 0, 20, 0], "coral"), ("Dice cómo arreglarlo", [0, 8, 0, 8], "teal")],
                        unit="líneas de traceback", horizontal=True, label_w=230,
                        note="Envolver el error en la frontera del SDK redujo la pila de 20 a 8 líneas y añadió la acción. El último renglón de los crudos es «KeyError: 'endpoint'»; el de los envueltos, «Falta 'endpoint'. Causa… Solución…». El costo: from None oculta la causa original, útil para el usuario final pero molesta al depurar el SDK; se decide con un modo de depuración que conserve la cadena.", note_kind="teal", foot="Medido con CPython 3.12.9; las líneas de traceback incluyen rutas del equipo y no se reproducen aquí.")


def se118_obsolescencia() -> Fig:
    f, y = sketch("Quién ve el aviso de obsolescencia",
                  "Diagrama del filtro de avisos de Python para una función obsoleta: con la configuración por defecto el DeprecationWarning se muestra si la llamada viene del script principal y se silencia si viene de un módulo de la aplicación; con -W default se ve desde cualquier módulo y con -W error::DeprecationWarning se convierte en excepción y la salida es 1.")
    bx(f, 350, y + 8, 240, 50, "Función obsoleta emite DeprecationWarning", "navy", 13, True)
    bx(f, 10, y + 100, 420, 46, "Filtro por defecto de Python", "grey", 14, True)
    bx(f, 510, y + 100, 420, 46, "Filtros que elige el consumidor", "grey", 14, True)
    f.arrow([(440, y + 58), (220, y + 100)])
    f.arrow([(500, y + 58), (720, y + 100)])
    bx(f, 10, y + 190, 200, 130, "Llamada desde el script principal (__main__): aviso visible, sin configurar nada", "teal")
    bx(f, 230, y + 190, 200, 130, "Llamada desde un módulo de la aplicación: silencio; el filtro solo muestra __main__", "coral")
    bx(f, 510, y + 190, 200, 130, "-W default: aviso visible; el consumidor lo activa", "teal")
    bx(f, 730, y + 190, 200, 130, "-W error::DeprecationWarning: se vuelve error, salida 1; la integración continua puede exigir cero avisos", "gold")
    for x in (110, 330):
        f.arrow([(x, y + 146), (x, y + 190)])
    for x in (610, 830):
        f.arrow([(x, y + 146), (x, y + 190)])
    return done(f, y + 336, "Con stacklevel=2 el aviso apunta al código del consumidor, no al interior del SDK. Un aviso que nadie ve no cumple la función de avisar: el SDK debe documentar el plazo y la alternativa y verificar con -W error en su propia integración continua. Idéntico en Windows y Linux.", "gold", MEDIDO)


# ---------------------------------------------------------------- SE-119
def se119_matriz() -> Fig:
    rows = ["D1: faltan los datos en package-data", "D2: entry point con el nombre mal escrito", "D3: falta py.typed", "D4: dependencia usada pero no declarada", "D5: requires-python mayor que el intérprete", "D6: la carpeta tests/ entra en la rueda", "D7: __version__ distinto de la versión del paquete"]
    cols = ["Árbol: Windows", "Árbol: Linux", "Rueda: Windows", "Rueda: Linux", "Humo: Windows", "Humo: Linux"]
    v = [[0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1], [0, 0, 1, 1, 1, 1], [0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1]]
    return heatmap("Siete defectos de empaquetado frente a tres detectores", "Mapa de calor de siete defectos inyectados frente a tres detectores en dos plataformas: oscuro es que el detector lo ve. Las pruebas unitarias sobre el árbol de fuentes ven solo D4 en Linux; la inspección de la rueda ve cinco en Windows y seis en Linux (D3 solo en Linux); el humo en entorno limpio ve cinco en ambos; D3 y D6 son invisibles al humo. Contorno: celdas donde Windows y Linux difieren.",
                   rows, cols, v, unit="1 = lo ve", scale="teal", vmin=0, vmax=1, cell_fmt=lambda x: "lo ve" if x else "pasa", highlight=[(2, 2), (2, 3), (3, 0), (3, 1)], cell_h=40, label_w=340, width=1000,
                   note="Las pruebas unitarias casi nunca ven un defecto de empaquetado, porque se ejecutan contra el árbol de fuentes. D4 pasó en Windows porque la dependencia estaba instalada en el sistema: el entorno ambiente ocultó el defecto. D3 depende del constructor: setuptools 84.0.0 incluyó py.typed por sí solo y 68.1.2 no. Ningún detector solo cubre los siete casos.", note_kind="coral", foot="Medido en Windows (setuptools 84.0.0, pip 24.3.1) y Linux (setuptools 68.1.2, pip 24.0).")


def se119_contenido() -> Fig:
    return grouped_bars("Qué contiene la rueda según la configuración", "Barras horizontales con el tamaño en bytes de cuatro ruedas en Windows y Linux: la base mide 2048 y 2043; sin package-data mide 1867 y 1710 y pierde data/rules.json; sin py.typed mide 2048 y 1891 (Windows lo sigue incluyendo); con include igual a asterisco mide 2473 y 2472 y añade la carpeta de pruebas.",
                        ["Base: paquete, CLI, py.typed y datos", "D1: sin package-data", "D3: sin py.typed en package-data", "D6: include = «*»"],
                        [("Windows (setuptools 84.0.0)", [2048, 1867, 2048, 2473], "coral"), ("Linux (setuptools 68.1.2)", [2043, 1710, 1891, 2472], "teal")],
                        unit="bytes de la rueda", horizontal=True, label_w=250,
                        note="El tamaño es una señal barata: un cambio inesperado entre dos construcciones obliga a mirar qué entró o salió. Base: 9 entradas, incluida RECORD. D1 pierde data/rules.json (y py.typed en Linux); D3 pierde py.typed solo en Linux; D6 añade tests/__init__.py y test_capkit.py. Se compara el listado de la rueda (zipfile.namelist) con una lista esperada y se falla si difiere.", note_kind="gold", foot=MEDIDO)


# ---------------------------------------------------------------- SE-120
def se120_detectores() -> Fig:
    f, y = sketch("Doce cambios a un SDK: qué ve la comparación de API y qué ven las pruebas de contrato",
                  "Diagrama de conjuntos de doce mutantes: la comparación de superficie de API y las pruebas de contrato ven cinco a la vez (M2, M6, M9, M10 y M12); solo la comparación ve M3, M7 y el control M1; solo las pruebas ven M4 y M8; M5 solo lo ve una prueba con fixtures frescas y M11, un cambio de texto de error, no lo ve ninguno.")
    zones = [(10, "Solo la comparación de API", "gold", ["M3 renombrar policy: 0 pruebas", "M7 quitar DEFAULT_LIMIT: 0 pruebas", "M1 opcional nuevo (control): 0"]),
             (320, "Las dos: cinco mutantes", "teal", ["M2 renombrar limit: 1 prueba", "M6 ParseError sin ValueError: 1", "M9 limit None a 2 (REVISAR): 2", "M10 policy obligatorio: 5", "M12 choose_next privado: 1"]),
             (630, "Solo las pruebas de contrato", "coral", ["M4 desempate por id descendente: 4", "M8 tupla en vez de lista: 5"])]
    for x, head, kind, chips in zones:
        bx(f, x, y + 8, 300, 40, head, "navy", 14, True)
        bx(f, x, y + 56, 300, 6 + 42 * 5, "", kind)
        for k, c in enumerate(chips):
            bx(f, x + 10, y + 62 + k * 42, 280, 36, c, "plain", 13)
    bx(f, 10, y + 288, 450, 74, "M5 ordenar la entrada en sitio: solo lo ven las pruebas con fixtures frescas (1 prueba); con fixtures compartidas la lista ya estaba ordenada y falla 0", "gold")
    bx(f, 480, y + 288, 450, 74, "M11 cambiar el texto del error: no lo ve ninguno (0 pruebas, sin cambio de superficie)", "grey")
    return done(f, y + 376, "Solo la comparación vio M3, M7 y el control M1; solo las pruebas vieron M4 y M8; ambas vieron cinco; ninguna vio M11 y, con fixtures compartidas, tampoco M5: la primera prueba ordenó la lista y la prueba de no mutación leyó la lista ya ordenada. La cifra de cada mutante es cuántas pruebas de contrato fallan.", "coral", "Cuentas deterministas sobre un SDK de 12 líneas; idénticas en Windows (3.12.9) y Linux (3.12.3).")


def se120_golden() -> Fig:
    f, y = sketch("Salida de la CLI como archivo de referencia: los bytes, no el texto",
                  "Diagrama de cómo la salida de dos líneas, una con JSON con ñ, pasa de 42 a 43 bytes en Windows por defecto: base de 42 bytes con LF y UTF-8 y SHA-256 526a8c1a6a2b, más 2 bytes por dos saltos CRLF, menos 1 byte porque la ñ ocupa 1 byte en cp1252, da 43 bytes y SHA-256 86ca59242a63. Windows con reconfigure y Linux, con o sin reconfigure, dan los 42 bytes y 526a8c1a6a2b.")
    cw, gap = 190, 40
    steps = [("42 B: LF y UTF-8\nSHA-256 526a8c1a6a2b", "teal"), ("+2 B: dos saltos CRLF\n(Windows por defecto)", "gold"), ("−1 B: la ñ ocupa 1 byte\n(cp1252 en vez de UTF-8)", "gold"), ("43 B, 2 CRLF\nSHA-256 86ca59242a63", "coral")]
    for i, (t, k) in enumerate(steps):
        x = 10 + i * (cw + gap)
        bx(f, x, y + 10, cw, 96, t, k, 13, i in (0, 3))
        if i:
            f.arrow([(x - gap, y + 58), (x, y + 58)])
    f.text(470, y + 132, "Windows, salida por defecto: de 42 a 43 bytes", 13, "middle", 700, "#5c1f14")
    bx(f, 10, y + 154, 450, 80, "Windows con reconfigure(newline='\\n', encoding='utf-8'): 42 B, 0 CRLF, SHA-256 526a8c1a6a2b; igual que Linux", "teal")
    bx(f, 480, y + 154, 450, 80, "Linux, por defecto o con reconfigure: 42 B, 0 CRLF, SHA-256 526a8c1a6a2b; LF y UTF-8, sin cambios", "teal")
    return done(f, y + 250, "Comparar con un archivo de referencia (golden) sin fijar codificación y salto de línea hace que la misma prueba pase en Linux y falle en Windows. Para la CLI de un SDK, el contrato incluye los bytes de la salida --json: se fijan en el programa, no en la prueba.", "teal", MEDIDO)


def se120_reproducible() -> Fig:
    f, y = sketch("Compilaciones reproducibles: mismo código, mismo hash solo con las entradas fijadas",
                  "Diagrama de los SHA-256 abreviados de una rueda en Windows y en Linux: sin SOURCE_DATE_EPOCH dos construcciones con fechas de archivo distintas dan hashes distintos en ambos sistemas (d7602c9bdc1d y 61f7d211f57b en Windows; 4ea2ed489fad y 77b4ed888892 en Linux); con SOURCE_DATE_EPOCH=1700000000 cada sistema da el mismo hash dos veces (5748444b389c y 87fd805e4a0c); entre sistemas difieren porque los permisos guardados en la rueda son 0o100666 en Windows y 0o100644 en Linux.")
    bx(f, 200, y + 6, 340, 34, "Windows (3.12.9)", "navy", 14, True)
    bx(f, 590, y + 6, 340, 34, "Linux (3.12.3)", "navy", 14, True)
    rows = [("Sin SOURCE_DATE_EPOCH, fechas distintas", "d7602c9bdc1d  ≠  61f7d211f57b", "4ea2ed489fad  ≠  77b4ed888892", "coral"),
            ("Con SOURCE_DATE_EPOCH fijada, dos veces", "5748444b389c  =  5748444b389c", "87fd805e4a0c  =  87fd805e4a0c", "teal")]
    for i, (lab, w, l, k) in enumerate(rows):
        top = y + 52 + i * 84
        bx(f, 10, top, 180, 76, lab, "grey", 13)
        bx(f, 200, top, 340, 70, w, k, 14, True)
        bx(f, 590, top, 340, 70, l, k, 14, True)
    top = y + 224
    bx(f, 10, top, 180, 86, "Entre sistemas, con la variable: la rueda difiere", "grey", 13)
    bx(f, 200, top, 340, 40, "hash 5748444b389c", "plain", 14, True)
    bx(f, 590, top, 340, 40, "hash 87fd805e4a0c", "plain", 14, True)
    f.arrow([(540, top + 20), (590, top + 20)], "≠", label_at=(565, top + 12))
    bx(f, 200, top + 46, 340, 40, "permisos guardados: 0o100666", "gold", 13)
    bx(f, 590, top + 46, 340, 40, "permisos guardados: 0o100644", "gold", 13)
    return done(f, top + 100, "La reproducibilidad exige entradas fijadas: fecha (SOURCE_DATE_EPOCH), herramientas y plataforma. La variable valía 1700000000. Esta medición no la logró entre sistemas operativos; la evidencia de un release debe registrar dónde se construyó y declarar que el hash es válido para ese entorno. El hash prueba integridad, no ausencia de defectos.", "gold", MEDIDO)


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
