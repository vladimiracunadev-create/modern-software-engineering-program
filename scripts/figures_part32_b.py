"""Figures for SE-391 to SE-396 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Lectura de reloj de un equipo Windows 11 (CPython 3.12.9); en otro equipo los milisegundos cambian."
SONDA = "Sonda real en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); lo que difiere entre sistemas es el resultado que se mide."


# ---------------------------------------------------------------- SE-391
def se391_unicidad() -> Fig:
    rows = [
        ["Año, comuna, curso y género exactos", "4 689", "1", "88,2 %", "100,0 %"],
        ["Año en tramos de 3 y comuna a región", "3 268", "1", "44,5 %", "90,6 %"],
        ["Tramos de 5 años, región, sin curso", "191", "3", "0,0 %", "0,9 %"],
        ["Tramos de 5 años, macrozona, sin curso ni género", "12", "63", "0,0 %", "0,0 %"],
    ]
    return tab("5 000 estudiantes sintéticos: cuántos son únicos según cuánto se generalizan cuatro atributos",
               "Tabla: con año de nacimiento, comuna, curso y género exactos el 88,2 por ciento de las 5 000 personas es única y todas están en grupos de menos de cinco; generalizando año y comuna baja a 44,5 por ciento; con tramos de cinco años, región y sin curso el grupo mínimo es de tres personas; con macrozona y sin género es de 63.",
               ["Nivel de generalización", "Grupos", "k mínimo", "Registros únicos", "En grupos menores de 5"], rows, [400, 90, 100, 150, 180], row_h=52, size=12,
               note="Ningún dato de la tabla es un nombre y aun así el 88,2 % se distingue de los demás. Generalizar reduce la unicidad y también la utilidad: con 12 grupos solo se puede contar por macrozona. La distribución de comunas y de años es del autor, y k-anonimato no protege frente a quien conoce otros datos.",
               note_kind="coral", foot=SINT)


def se391_ruido() -> Fig:
    rows = [
        ["1", "2,034", "0,5"],
        ["10", "0,753", "5"],
        ["100", "0,209", "50"],
        ["1 000", "0,076", "500"],
        ["10 000", "0,022", "5 000"],
    ]
    return tab("Mismo conteo (312 estudiantes) consultado Q veces con ruido de Laplace nuevo, ε = 0,5 por consulta",
               "Tabla: una consulta con epsilon 0,5 tiene un error medio de 2 estudiantes; promediar 100 consultas repetidas lo baja a 0,2 y promediar 10 000 a 0,02, a costa de un presupuesto acumulado de privacidad que pasa de 0,5 a 5 000.",
               ["Consultas repetidas (Q)", "Error medio del promedio", "ε acumulado"], rows, [360, 300, 260], row_h=42, size=13,
               note="Una sola respuesta con ruido protege y mil respuestas promediadas devuelven el valor verdadero: el ruido por consulta no es la garantía, el presupuesto total sí. Con una consulta el error medio vale 9,93 con ε = 0,1, 2,00 con 0,5, 0,99 con 1 y 0,20 con 5.",
               note_kind="gold", foot=SINT)


def se391_seudonimos() -> Fig:
    rows = [
        ["SHA-256 sin sal del correo", "12 000 de 12 000", "Cualquiera con la lista de correos candidatos"],
        ["HMAC-SHA256 con clave del servidor, atacante sin clave", "0 de 12 000", "Se necesita la clave para repetir el cálculo"],
        ["Mismo HMAC en dos conjuntos de datos", "6 000 de 6 000 enlazados", "El seudónimo permite cruzar los conjuntos"],
        ["HMAC con una clave distinta por propósito", "0 de 6 000 enlazados", "Los conjuntos dejan de ser cruzables sin la clave"],
    ]
    return tab("Seudonimizar 20 000 correos (12 000 en una lista de 100 000 candidatos): qué se reidentifica y qué se enlaza",
               "Tabla: un hash SHA-256 sin sal de 12 000 correos presentes en una lista de 100 000 candidatos los reidentifica todos; un HMAC con clave no reidentifica ninguno sin la clave; si dos conjuntos usan el mismo HMAC se enlazan 6 000 de 6 000 y con una clave por propósito ninguno.",
               ["Técnica", "Resultado", "Condición"], rows, [380, 220, 320], row_h=58, size=12,
               note="Un hash sin clave de un dato adivinable es una forma de publicarlo. La seudonimización con clave sigue siendo dato personal para quien tiene la clave. Las listas de correos y los porcentajes son del autor; no se usó ningún dato de personas reales.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-392
def se392_mutantes() -> Fig:
    items = [
        ("Solo ejemplos válidos (5 pruebas)", 0, "coral", "0 de 12"),
        ("Más negativos típicos (15)", 3, "coral", "3 de 12"),
        ("Más valores de borde (30)", 10, "gold", "10 de 12"),
        ("Más 2 000 entradas al azar (2 050)", 10, "gold", "10 de 12"),
    ]
    return bars("Doce defectos plantados en un validador de subidas: cuántos mata cada diseño de pruebas",
                "Barras: cinco ejemplos válidos matan 0 de 12 mutantes del validador de subidas; con negativos típicos 3; con valores de borde 10; y 2 000 entradas aleatorias adicionales comparadas con la referencia siguen en 10.",
                items, 38.0, "Dos mutantes sobreviven a todo: uno es equivalente (permitir separadores de ruta no cambia nada porque la lista blanca de caracteres ya los rechaza, defensa en profundidad) y el otro, la doble extensión ejecutable, exige un patrón que 2 000 entradas aleatorias no generaron. El azar no sustituye al borde elegido con criterio.",
                label_w=330, width=940, note_kind="gold", foot=SINT)


def se392_reglas() -> Fig:
    rows = [
        ["Fragmentos sencillos (llamada directa, argumento literal)", "24", "24", "0"],
        ["Fragmentos difíciles (alias, flujo de datos, comentarios, suma de cadenas)", "6", "0", "2"],
    ]
    return tab("Ocho reglas de ast sobre 60 fragmentos de código (24 con defecto sencillo, 6 con defecto difícil, 30 seguros)",
               "Tabla: las reglas de ast encuentran los 24 defectos sencillos sin falsas alarmas y ninguno de los 6 defectos difíciles, y marcan 2 de los 6 fragmentos seguros difíciles, uno que define su propia función eval y otro que usa md5 para un uso que no es de seguridad.",
               ["Tipo de fragmento", "Con defecto", "Detectados", "Seguros marcados"], rows, [500, 140, 140, 140], row_h=58, size=12,
               note="Una regla sintáctica ve la forma de la llamada, no el flujo del dato: no sigue alias (from subprocess import run as r), variables que valen True, yaml.FullLoader ni una contraseña armada con una suma. Las 2 falsas alarmas son lo contrario: una función propia llamada eval y md5 con usedforsecurity=False. Reglas y fragmentos son del autor.",
               note_kind="gold", foot=SINT)


def se392_regex() -> Fig:
    rows = [
        ["14", "0,88", "0,0014", "—"],
        ["16", "3,97", "0,0040", "4,5"],
        ["18", "13,84", "0,0045", "3,5"],
        ["20", "59,99", "0,0046", "4,3"],
        ["22", "230,38", "0,0050", "3,8"],
        ["24", "935,54", "0,0051", "4,1"],
    ]
    return tab("Tiempo de re.match con a repetida n veces y un «!» al final: ^(a+)+$ frente a ^a+$",
               "Tabla: el patrón con cuantificadores anidados tarda 0,88 milisegundos con 14 caracteres y 935,54 con 24, multiplicándose por unas 4 cada 2 caracteres, mientras el patrón lineal se mantiene en milésimas de milisegundo.",
               ["n (caracteres a)", "ms con ^(a+)+$", "ms con ^a+$", "Factor entre filas"], rows, [220, 240, 220, 240], row_h=40, size=13,
               note="Dos caracteres más multiplican el tiempo por cuatro: extrapolado, 30 caracteres ocupan un hilo cerca de un minuto y 40, unas 17 horas. El defecto está en la expresión, no en el dato; recortar la longitud a 20 es una mitigación que se rompe si el límite cambia. Lectura de reloj: en otro equipo cambian los milisegundos y se conserva el crecimiento.",
               note_kind="coral", foot=REAL)


# ---------------------------------------------------------------- SE-393
def se393_cvss() -> Fig:
    rows = [
        ["Lectura de notas ajenas por identificador", "6,5 · 4,3 · 7,5", "4,3 – 7,5", "media – alta"],
        ["Cambio de nota sin comprobar el dueño", "6,5 · 5,4 · 5,3", "5,3 – 6,5", "media"],
        ["XSS almacenado en un comentario", "5,4 · 4,6 · 6,1", "4,6 – 6,1", "media"],
        ["Inyección SQL en la búsqueda de entregas", "9,8 · 8,8 · 7,1", "7,1 – 9,8", "alta – crítica"],
        ["Secreto en un registro accesible a soporte", "5,5 · 4,9 · 2,3", "2,3 – 5,5", "baja – media"],
        ["Denegación por expresión regular catastrófica", "7,5 · 6,5 · 3,7", "3,7 – 7,5", "baja – alta"],
    ]
    return tab("Tres analistas puntúan con CVSS v3.1 el mismo hallazgo: puntajes y banda según su lectura del vector",
               "Tabla: tres lecturas razonables del vector CVSS de seis hallazgos dan rangos de hasta 3,8 puntos; la denegación por expresión regular va de 3,7 a 7,5, es decir de baja a alta, y la inyección SQL de 7,1 a 9,8, de alta a crítica.",
               ["Hallazgo", "Tres puntajes", "Rango", "Bandas"], rows, [380, 190, 140, 180], row_h=52, size=12,
               note="La fórmula es determinista (9,8 para AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, 6,1 para el XSS reflejado clásico); lo subjetivo es elegir cada métrica del vector: alcance de red o adyacente, privilegio requerido, complejidad. Los vectores de cada analista los escribió el autor para ilustrar lecturas posibles, no son de analistas reales.",
               note_kind="gold", foot=SINT)


def se393_prioridad() -> Fig:
    rows = [
        ["CVSS de 7 o más", "1 076", "40 de 83"],
        ["CVSS de 9 o más", "236", "14 de 83"],
        ["Lista de explotación conocida", "83", "83 de 83"],
        ["Explotadas más CVSS de 9 o más", "305", "83 de 83"],
    ]
    return tab("3 000 vulnerabilidades sintéticas (83 explotadas): cuántas se parchean y cuántas explotadas se cubren",
               "Tabla: parchear todo lo de CVSS 7 o más exige 1 076 parches y cubre 40 de las 83 explotadas; CVSS 9 o más, 236 parches y 14; parchear solo las explotadas conocidas, 83 parches y 83; la unión con CVSS 9 o más, 305 parches y 83.",
               ["Estrategia", "Parches a aplicar", "Explotadas cubiertas"], rows, [440, 220, 260], row_h=46, size=13,
               note="Es un ejemplo de mecanismo: la gravedad describe el daño posible y la explotación observada describe la probabilidad. Aquí la correlación entre ambas es débil por supuesto del autor (2 % frente a 3,5 %); en el mundo real hay que medirla con listas como KEV y EPSS. La lista conocida solo cubre lo ya explotado.",
               note_kind="teal", foot=SINT)


def se393_triaje() -> Fig:
    rows = [
        ["1", "27,7", "94,0", "144,2"],
        ["2", "10,6", "52,2", "63,2"],
        ["3", "9,7", "51,3", "63,2"],
    ]
    return tab("307 informes de vulnerabilidad en un año (60 % válidos), horario laboral de lunes a viernes de 9 a 17 h",
               "Tabla: con una persona de triaje la mediana hasta el primer acuse es de 27,7 horas y el percentil 99 de 144,2; con dos baja a 10,6 y 63,2; con tres a 9,7 y 63,2, porque el límite pasa a ser el horario y no la cola.",
               ["Personas de triaje", "Mediana (h)", "Percentil 90 (h)", "Percentil 99 (h)"], rows, [260, 200, 230, 230], row_h=44, size=13,
               note="Pasar de una a dos personas recorta la espera a la mitad; la tercera casi no cambia nada porque los informes del viernes por la tarde esperan al lunes. Una política de «acuse en 72 horas» pide dos personas o un acuse automático. Las llegadas (6 por semana) y los tiempos son del autor.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-394
def se394_embudo() -> Fig:
    items = [
        ("Requisitos aplicables", 40, "plain", "40"),
        ("Con un control documentado", 38, "teal", "38"),
        ("Con una prueba asociada", 28, "teal", "28"),
        ("Y la prueba pasó", 27, "gold", "27"),
        ("Y la evidencia tiene 90 días o menos", 23, "gold", "23"),
        ("Y la evidencia tiene 30 días o menos", 4, "coral", "4"),
    ]
    return bars("De 40 requisitos a evidencia vigente: lo que significa «cubierto» según la definición",
                "Barras: de 40 requisitos, 38 tienen control documentado, 28 tienen una prueba, 27 la pasaron, 23 tienen evidencia de 90 días o menos y solo 4 de 30 días o menos.",
                items, 15.0, "El mismo conjunto da 95 %, 70 %, 67,5 %, 57,5 % o 10 % de cobertura según se exija un documento, una prueba, un resultado o evidencia reciente. Una auditoría que acepta la primera definición certifica un papel. Las probabilidades de cada etapa y la edad de la evidencia son supuestos del autor.",
                label_w=360, width=980, note_kind="gold", foot=SINT)


def se394_muestreo() -> Fig:
    rows = [
        ["10", "14,1 %", "13,9 %"],
        ["25", "31,6 %", "31,6 %"],
        ["60", "60,2 %", "60,3 %"],
        ["100", "78,8 %", "78,8 %"],
        ["200", "95,9 %", "96,0 %"],
    ]
    return tab("Muestrear 2 000 eventos con 30 defectos (1,5 %): probabilidad de que la muestra contenga al menos un defecto",
               "Tabla: una muestra aleatoria de 25 eventos encuentra al menos un defecto el 31,6 por ciento de las veces, una de 60 el 60,2 por ciento y una de 200 el 95,9 por ciento, valores que la simulación de 20 000 repeticiones reproduce.",
               ["Tamaño de la muestra", "Probabilidad exacta", "Simulada (20 000)"], rows, [360, 280, 280], row_h=42, size=13,
               note="Una muestra de 25 «sin hallazgos» no prueba control: con 1,5 % de defectos ocurre el 68 % de las veces. Si los defectos se concentran (cuentas de servicio: 4 % de los eventos y 60 % de los defectos), 25 eventos al azar encuentran uno el 31,6 % de las veces; 15 de ese estrato más 10 del resto, el 98,7 %.",
               note_kind="coral", foot=SINT)


def se394_cadena() -> Fig:
    rows = [
        ["Modificar un evento", "100 de 100", "100 de 100"],
        ["Borrar un evento intermedio", "100 de 100", "100 de 100"],
        ["Reordenar dos eventos", "100 de 100", "100 de 100"],
        ["Truncar los últimos 10 eventos", "0 de 100", "100 de 100"],
        ["Reescribir desde un evento recalculando las huellas", "0 de 100", "100 de 100"],
    ]
    return tab("Registro de 1 000 eventos con huellas encadenadas: 100 ataques de cada tipo",
               "Tabla: una cadena de huellas detecta 100 de 100 modificaciones, borrados intermedios y reordenamientos, pero no detecta 0 de 100 truncamientos de los últimos eventos ni reescrituras que recalculan las huellas; con la huella final publicada fuera del sistema se detectan 100 de 100 de todos los tipos.",
               ["Ataque al registro", "Solo la cadena", "Cadena y huella publicada fuera"], rows, [470, 200, 250], row_h=46, size=13,
               note="La cadena detecta lo que rompe un eslabón y no lo que lo reconstruye bien: quien puede escribir puede recalcular. Hace falta un ancla fuera del alcance del atacante (un tercero, un sellado de tiempo, un registro de transparencia). El ancla debe publicarse antes del ataque; un ancla posterior no detecta nada.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-395
def se395_rutas() -> Fig:
    rows = [
        ["Quitar «../» una vez y decodificar después", "2 072", "2 154"],
        ["Quitar «../» en bucle y decodificar después", "1 106", "1 181"],
        ["Decodificar, resolver y comprobar el prefijo de la raíz", "0 (903 rechazadas)", "0 (958 rechazadas)"],
    ]
    return tab("5 000 cargas al azar (puntos, barras, %2e, %2f): cuántas salen de la raíz según el control",
               "Tabla: de 5 000 cargas generadas al azar, el filtro que quita una vez la secuencia punto punto barra deja salir 2 072 de la raíz con rutas POSIX y 2 154 con rutas de Windows; quitarla en bucle deja salir 1 106 y 1 181; decodificar, resolver y comprobar el prefijo deja salir 0.",
               ["Control aparente o reparado", "Salen de la raíz (POSIX)", "Salen de la raíz (Windows)"], rows, [470, 230, 220], row_h=52, size=12,
               note="Quitar «../» una vez convierte «....//secreto» en «../secreto». El bucle cierra ese caso y falla con la decodificación posterior (%2e%2e%2f), y las barras invertidas de Windows son otro separador. La reparación no filtra: resuelve la ruta final y comprueba que sigue dentro de la raíz.",
               note_kind="coral", foot=SINT)


def se395_csrf() -> Fig:
    rows = [
        ["Sin token", "rechaza", "rechaza", "rechaza"],
        ["Token inventado", "ACEPTA", "rechaza", "rechaza"],
        ["Token con un espacio", "ACEPTA", "rechaza", "rechaza"],
        ["Token válido de la sesión de otra persona", "ACEPTA", "ACEPTA", "rechaza"],
        ["Token propio de la sesión", "acepta", "rechaza", "acepta"],
    ]
    return tab("Defensa CSRF: cinco peticiones contra tres implementaciones (la primera solo comprueba que haya token)",
               "Tabla: comprobar solo que el token exista acepta un token inventado, uno con un espacio y el de otra sesión; compararlo con un valor global rechaza los inventados pero acepta el de otra sesión y rechaza el token propio; ligarlo a la sesión con un HMAC rechaza lo ajeno y acepta lo propio.",
               ["Petición", "Solo presencia", "Valor global", "Ligado a la sesión"], rows, [380, 180, 180, 180], row_h=44, size=12,
               note="Las pruebas felices (token propio, sin token) pasan en la implementación débil: ninguna prueba que no intente falsificar detecta que el control es de apariencia. La implementación con valor global parece mejor y falla en la otra dirección. El token es un HMAC de la sesión, no un secreto compartido por todos.",
               note_kind="gold", foot=SINT)


def se395_limitador() -> Fig:
    rows = [
        ["1 000 intentos con una cabecera distinta en cada uno", "1 000 permitidos", "5 permitidos"],
        ["1 000 intentos sin cambiar de dirección", "5 permitidos", "5 permitidos"],
        ["Token legítimo", "acepta", "acepta"],
        ["Token con alg «none» y rol docente", "ACEPTA", "rechaza"],
        ["Token con la firma de otra clave", "rechaza", "rechaza"],
        ["Token con la carga alterada y la firma vieja", "rechaza", "rechaza"],
    ]
    return tab("Dos controles aparentes más: limitador por cabecera X-Forwarded-For y verificación de token que lee el algoritmo del propio token",
               "Tabla: un limitador que cuenta por la cabecera que envía el cliente permite 1 000 de 1 000 intentos si el atacante cambia la cabecera y 5 si no; contar por la dirección de la conexión permite 5 en ambos casos; un verificador que acepta el algoritmo none acepta un token forjado, uno que fija HS256 lo rechaza.",
               ["Prueba", "Control aparente", "Control reparado"], rows, [480, 220, 220], row_h=44, size=12,
               note="En ambos casos el control confía en un dato que controla el atacante: la cabecera y el encabezado del token. Con el control reparado solo cambia quién decide (la conexión, el servidor). Detrás de un proxy la reparación exige configurar qué proxies son de confianza.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-396
def se396_validador() -> Fig:
    items = [
        ("Solo presencia de la evidencia", 15, "coral", "15 de 210"),
        ("Estructura: existencia, fecha, alcance, duplicados", 120, "gold", "120 de 210"),
        ("Estructura y heurísticas (huellas repetidas, aserciones, resultado)", 195, "teal", "195 de 210"),
        ("Mutaciones aplicadas", 210, "plain", "14 operadores × 15"),
    ]
    return bars("Validador de un paquete de evidencia de seguridad frente a 210 mutaciones (14 operadores × 15)",
                "Barras: un validador que solo mira la presencia de la evidencia detecta 15 de 210 mutaciones del paquete, uno que comprueba estructura 120 y uno que añade heurísticas semánticas 195; las 15 restantes son evidencia única sin relación con el requisito.",
                items, 2.2, "Las 15 que ningún validador ve son evidencia que parece buena: un archivo con la palabra «aprobado» que no ejecutó nada. Lo que detecta la estructura se puede automatizar; que la evidencia pruebe el requisito lo decide una revisión humana con la prueba delante. Las mutaciones y los validadores son del autor.",
                label_w=480, width=1000, note_kind="gold", foot=SINT)


def se396_portabilidad() -> Fig:
    rows = [
        ["Orden de os.listdir", "A.txt, b.txt, informe, ñ.txt", "A.txt, ñ.txt, b.txt, informe", "No"],
        ["Huella ingenua (orden del sistema, bytes crudos)", "dcb7a0e6…", "9eb5bb1c…", "No"],
        ["Huella canónica (rutas ordenadas, LF, separador /)", "7f9dbc41…", "7f9dbc41…", "Sí"],
    ]
    return tab("La huella de un paquete de cinco archivos construido en Windows y en Ubuntu (WSL2)",
               "Tabla: el listado de un mismo directorio sale en distinto orden en Windows y en Ubuntu y la huella ingenua del paquete difiere entre ambos; una huella canónica con rutas ordenadas, saltos de línea normalizados y separador barra coincide en los dos sistemas.",
               ["Método", "Windows 11", "Ubuntu (WSL2)", "Coinciden"], rows, [330, 240, 240, 110], row_h=58, size=12,
               note="Dos personas que ejecutan lo mismo en equipos distintos no obtienen la misma huella si la huella depende del orden del sistema de archivos o de los finales de línea. La huella canónica define el orden, la codificación y la normalización; con ella la verificación entre sistemas se puede automatizar.",
               note_kind="teal", foot=SONDA)


def se396_operadores() -> Fig:
    rows = [
        ["Quitar la evidencia", "15", "15", "15"],
        ["Evidencia o prueba que no existe", "0", "15", "15"],
        ["Evidencia de 120 días; alcance de otra versión", "0", "15", "15"],
        ["No aplica sin justificación; excepción sin dueño", "0", "15", "15"],
        ["Identificador duplicado", "0", "15", "15"],
        ["Misma evidencia en 10 requisitos o copia de otro", "0", "0", "15"],
        ["Prueba sin aserciones; prueba fallida marcada como cumple", "0", "0", "15"],
        ["Archivo de evidencia vacío", "0", "0", "15"],
        ["Evidencia única que dice «aprobado» sin ejecutar nada", "0", "0", "0"],
    ]
    return tab("Mutaciones del paquete detectadas por operador (de 15 cada una) según el validador",
               "Tabla: quitar la evidencia lo detectan los tres validadores; los defectos de existencia, fecha, alcance, justificación, dueño y duplicados los detectan el de estructura y el semántico; las huellas repetidas, las pruebas sin aserciones y los archivos vacíos solo el semántico; la evidencia única sin relación con el requisito, ninguno.",
               ["Operador de mutación", "Presencia", "Estructura", "Con heurísticas"], rows, [480, 130, 130, 160], row_h=44, size=12,
               note="Cada capa añade reglas que alguien tuvo que imaginar. La última fila no cae en ninguna regla porque su forma es la de una evidencia correcta. Las agrupaciones suman 14 operadores; en las filas con dos, cada valor es la detección de cada uno de ellos.",
               note_kind="gold", foot=SINT)


FIGURES = {
    "se-391-unicidad-y-generalizacion.svg": se391_unicidad,
    "se-391-ruido-y-presupuesto.svg": se391_ruido,
    "se-391-seudonimos-y-enlace.svg": se391_seudonimos,
    "se-392-mutantes-del-validador.svg": se392_mutantes,
    "se-392-reglas-de-seguridad.svg": se392_reglas,
    "se-392-regex-catastrofica.svg": se392_regex,
    "se-393-puntajes-cvss.svg": se393_cvss,
    "se-393-prioridad-por-explotacion.svg": se393_prioridad,
    "se-393-triaje-de-informes.svg": se393_triaje,
    "se-394-embudo-de-cobertura.svg": se394_embudo,
    "se-394-muestreo-de-auditoria.svg": se394_muestreo,
    "se-394-registro-con-cadena.svg": se394_cadena,
    "se-395-filtro-de-rutas.svg": se395_rutas,
    "se-395-defensa-csrf.svg": se395_csrf,
    "se-395-limitador-y-token.svg": se395_limitador,
    "se-396-validador-de-paquete.svg": se396_validador,
    "se-396-huella-entre-sistemas.svg": se396_portabilidad,
    "se-396-mutaciones-por-operador.svg": se396_operadores,
}
