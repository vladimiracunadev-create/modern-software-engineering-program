"""Figures for SE-463 to SE-468 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_cases import case_cards
from figure_kit import Fig, fmt_es, grouped_bars, heatmap, line_chart, percentile_intervals
from figures_part07_a import bars

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Lectura de reloj de un equipo Windows 11 (CPython 3.12.9); en otro equipo los milisegundos cambian."
SONDA = "Sonda real en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); lo que difiere entre sistemas es el resultado que se mide."


# ---------------------------------------------------------------- SE-463
def se391_unicidad() -> Fig:
    return grouped_bars("5 000 estudiantes sintéticos: cuántos son únicos según cuánto se generalizan cuatro atributos",
                        "Barras agrupadas con el porcentaje de registros únicos y en grupos de menos de cinco según la generalización: con año, comuna, curso y género exactos 88,2 y 100,0 por ciento; con año en tramos de 3 y comuna a región 44,5 y 90,6; con tramos de cinco años, región y sin curso 0,0 y 0,9; con macrozona y sin curso ni género 0,0 y 0,0.",
                        ["Año, comuna, curso y género exactos (4 689 grupos, k = 1)", "Año en tramos de 3 y comuna a región (3 268 grupos, k = 1)", "Tramos de 5 años, región, sin curso (191 grupos, k = 3)", "Tramos de 5 años, macrozona, sin curso ni género (12 grupos, k = 63)"],
                        [("Registros únicos", [88.2, 44.5, 0.0, 0.0], "coral"), ("En grupos menores de 5", [100.0, 90.6, 0.9, 0.0], "gold")],
                        unit="% de los 5 000 registros", horizontal=True, label_w=330, decimals=1,
                        note="Ningún dato es un nombre y aun así el 88,2 % se distingue de los demás. Generalizar reduce la unicidad y también la utilidad: con 12 grupos solo se puede contar por macrozona. La distribución de comunas y de años es del autor, y k-anonimato no protege frente a quien conoce otros datos.",
                        note_kind="coral", foot=SINT)

def se391_ruido() -> Fig:
    qs = [1, 10, 100, 1000, 10000]
    errs = [2.034, 0.753, 0.209, 0.076, 0.022]
    eps = ["0,5", "5", "50", "500", "5 000"]
    return line_chart("Mismo conteo (312 estudiantes) consultado Q veces con ruido de Laplace nuevo, ε = 0,5 por consulta",
                      "Línea en doble escala logarítmica con el error medio del promedio de Q consultas repetidas con epsilon 0,5: 2,034 estudiantes con una consulta, 0,209 con 100 y 0,022 con 10 000, a costa de un presupuesto acumulado de privacidad que pasa de 0,5 a 5 000.",
                      [("Error medio del promedio", [(q, e, fmt_es(e, 3), "t") for q, e in zip(qs, errs)], "coral")],
                      x_label="Consultas repetidas (Q) y ε acumulado", y_label="Error medio (estudiantes)", log_x=True, log_y=True,
                      x_ticks=[(q, f"{fmt_es(q)} (ε {e})") for q, e in zip(qs, eps)], y_ticks=[0.01, 0.1, 1, 10],
                      note="Una sola respuesta con ruido protege y mil respuestas promediadas devuelven el valor verdadero: el ruido por consulta no es la garantía, el presupuesto total sí. Con una consulta el error medio vale 9,93 con ε = 0,1, 2,00 con 0,5, 0,99 con 1 y 0,20 con 5.",
                      note_kind="gold", foot=SINT)

def se391_seudonimos() -> Fig:
    return case_cards("Seudonimizar 20 000 correos (12 000 en una lista de 100 000 candidatos): qué se reidentifica y qué se enlaza",
                      "Cuatro técnicas de seudonimización como tarjetas: un SHA-256 sin sal reidentifica los 12 000 correos de la lista de candidatos; un HMAC con clave no reidentifica ninguno sin la clave; el mismo HMAC en dos conjuntos enlaza 6 000 de 6 000 y con una clave por propósito ninguno.",
                      [("SHA-256 sin sal del correo", "12 000 de 12 000 reidentificados", "Cualquiera con la lista de correos candidatos.", "coral"),
                       ("HMAC-SHA256 con clave del servidor, atacante sin clave", "0 de 12 000 reidentificados", "Se necesita la clave para repetir el cálculo.", "teal"),
                       ("Mismo HMAC en dos conjuntos de datos", "6 000 de 6 000 enlazados", "El seudónimo permite cruzar los conjuntos.", "coral"),
                       ("HMAC con una clave distinta por propósito", "0 de 6 000 enlazados", "Los conjuntos dejan de ser cruzables sin la clave.", "teal")],
                      note="Un hash sin clave de un dato adivinable es una forma de publicarlo. La seudonimización con clave sigue siendo dato personal para quien tiene la clave. Las listas de correos y los porcentajes son del autor; no se usó ningún dato de personas reales.",
                      note_kind="coral", foot=SINT)

# ---------------------------------------------------------------- SE-464
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
    return grouped_bars("Ocho reglas de ast sobre 60 fragmentos de código (24 con defecto sencillo, 6 con defecto difícil, 30 seguros)",
                        "Barras agrupadas con lo que encuentran las reglas de ast: de 24 defectos sencillos detectan 24 y marcan 0 seguros; de 6 defectos difíciles (alias, flujo de datos, comentarios, suma de cadenas) detectan 0 y marcan en falso 2 de los 6 seguros difíciles.",
                        ["Sencillos (llamada directa, literal)", "Difíciles (alias, flujo de datos, suma)"],
                        [("Con defecto", [24, 6], "grey"), ("Detectados", [24, 0], "teal"), ("Seguros marcados en falso", [0, 2], "coral")],
                        unit="fragmentos",
                        note="Una regla sintáctica ve la forma de la llamada, no el flujo del dato: no sigue alias (from subprocess import run as r), variables que valen True, yaml.FullLoader ni una contraseña armada con una suma. Las 2 falsas alarmas son lo contrario: una función propia llamada eval y md5 con usedforsecurity=False. Reglas y fragmentos son del autor.",
                        note_kind="gold", foot=SINT)

def se392_regex() -> Fig:
    ns = [14, 16, 18, 20, 22, 24]
    return line_chart("Tiempo de re.match con a repetida n veces y un «!» al final: ^(a+)+$ frente a ^a+$",
                      "Líneas con escala logarítmica vertical con el tiempo de re.match con n letras a y un signo de exclamación: el patrón con cuantificadores anidados pasa de 0,88 milisegundos con 14 caracteres a 935,54 con 24, multiplicándose por unas 4 cada 2 caracteres, mientras el patrón lineal se mantiene en milésimas de milisegundo.",
                      [("^(a+)+$", [(n, v, fmt_es(v, 2), "t") for n, v in zip(ns, [0.88, 3.97, 13.84, 59.99, 230.38, 935.54])], "coral"),
                       ("^a+$", [(n, v, fmt_es(v, 4), "r" if n == 14 else "b") for n, v in zip(ns, [0.0014, 0.0040, 0.0045, 0.0046, 0.0050, 0.0051])], "teal")],
                      x_label="n (caracteres a)", y_label="Tiempo (ms)", log_y=True, x_ticks=[(n, str(n)) for n in ns], y_ticks=[0.001, 0.01, 0.1, 1, 10, 100, 1000],
                      note="Dos caracteres más multiplican el tiempo por cuatro (factores entre filas: 4,5; 3,5; 4,3; 3,8; 4,1): extrapolado, 30 caracteres ocupan un hilo cerca de un minuto y 40, unas 17 horas. El defecto está en la expresión, no en el dato; recortar la longitud a 20 es una mitigación que se rompe si el límite cambia. Lectura de reloj: en otro equipo cambian los milisegundos y se conserva el crecimiento.",
                      note_kind="coral", foot=REAL)

# ---------------------------------------------------------------- SE-465
def se393_cvss() -> Fig:
    return percentile_intervals("Tres analistas puntúan con CVSS v3.1 el mismo hallazgo: puntajes y banda según su lectura del vector",
                                "Rangos de tres puntajes CVSS v3.1 por hallazgo con las bandas de gravedad: la lectura de notas ajenas va de 4,3 a 7,5, el cambio de nota de 5,3 a 6,5, el XSS almacenado de 4,6 a 6,1, la inyección SQL de 7,1 a 9,8, el secreto en un registro de 2,3 a 5,5 y la denegación por expresión regular de 3,7 a 7,5.",
                                [("Lectura de notas ajenas por identificador", [4.3, 6.5, 7.5]), ("Cambio de nota sin comprobar el dueño", [5.3, 5.4, 6.5]), ("XSS almacenado en un comentario", [4.6, 5.4, 6.1]),
                                 ("Inyección SQL en la búsqueda de entregas", [7.1, 8.8, 9.8]), ("Secreto en un registro accesible a soporte", [2.3, 4.9, 5.5]), ("Denegación por expresión regular catastrófica", [3.7, 6.5, 7.5])],
                                unit="puntaje CVSS v3.1 (media desde 4,0, alta desde 7,0, crítica desde 9,0)", marks=("Mínimo", "Intermedio", "Máximo"), decimals=1, label_w=330,
                                note="Los tres puntajes de cada fila (el intermedio es el de en medio): 6,5 · 4,3 · 7,5; 6,5 · 5,4 · 5,3; 5,4 · 4,6 · 6,1; 9,8 · 8,8 · 7,1; 5,5 · 4,9 · 2,3; 7,5 · 6,5 · 3,7. La fórmula es determinista (9,8 para AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, 6,1 para el XSS reflejado clásico); lo subjetivo es elegir cada métrica del vector. Los vectores los escribió el autor para ilustrar lecturas posibles, no son de analistas reales.",
                                note_kind="gold", foot=SINT)

def se393_prioridad() -> Fig:
    return grouped_bars("3 000 vulnerabilidades sintéticas (83 explotadas): cuántas se parchean y cuántas explotadas se cubren",
                        "Barras agrupadas en escala logarítmica con los parches aplicados y las explotadas cubiertas de 83: CVSS 7 o más exige 1076 parches y cubre 40, CVSS 9 o más 236 y cubre 14, parchear solo las explotadas conocidas 83 y cubre 83, y la unión con CVSS 9 o más 305 y cubre 83.",
                        ["CVSS de 7 o más", "CVSS de 9 o más", "Lista de explotación conocida", "Explotadas más CVSS de 9 o más"],
                        [("Parches a aplicar", [1076, 236, 83, 305], "gold"), ("Explotadas cubiertas (de 83)", [40, 14, 83, 83], "teal")],
                        unit="parches o explotadas cubiertas", log=True,
                        note="Es un ejemplo de mecanismo: la gravedad describe el daño posible y la explotación observada describe la probabilidad. Aquí la correlación entre ambas es débil por supuesto del autor (2 % frente a 3,5 %); en el mundo real hay que medirla con listas como KEV y EPSS. La lista conocida solo cubre lo ya explotado.",
                        note_kind="teal", foot=SINT)

def se393_triaje() -> Fig:
    ps = [1, 2, 3]
    return line_chart("307 informes de vulnerabilidad en un año (60 % válidos), horario laboral de lunes a viernes de 9 a 17 h",
                      "Líneas con las horas hasta el primer acuse según las personas de triaje: con una persona la mediana es 27,7, el percentil 90 94,0 y el 99 144,2; con dos 10,6, 52,2 y 63,2; con tres 9,7, 51,3 y 63,2, porque el límite pasa a ser el horario y no la cola.",
                      [("Percentil 99", [(p, v, fmt_es(v, 1), "t") for p, v in zip(ps, [144.2, 63.2, 63.2])], "coral"), ("Percentil 90", [(p, v, fmt_es(v, 1), "b") for p, v in zip(ps, [94.0, 52.2, 51.3])], "gold"),
                       ("Mediana", [(p, v, fmt_es(v, 1), "t") for p, v in zip(ps, [27.7, 10.6, 9.7])], "teal")],
                      x_label="Personas de triaje", y_label="Horas hasta el primer acuse", x_ticks=[(p, str(p)) for p in ps], y_ticks=[0, 40, 80, 120, 160],
                      note="Pasar de una a dos personas recorta la espera a la mitad; la tercera casi no cambia nada porque los informes del viernes por la tarde esperan al lunes. Una política de «acuse en 72 horas» pide dos personas o un acuse automático. Las llegadas (6 por semana) y los tiempos son del autor.",
                      note_kind="gold", foot=SINT)

# ---------------------------------------------------------------- SE-466
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
    return grouped_bars("Muestrear 2 000 eventos con 30 defectos (1,5 %): probabilidad de que la muestra contenga al menos un defecto",
                        "Barras agrupadas con la probabilidad de que una muestra aleatoria contenga al menos un defecto: 14,1 por ciento con 10 eventos, 31,6 con 25, 60,2 con 60, 78,8 con 100 y 95,9 con 200, valores que la simulación de 20 000 repeticiones reproduce.",
                        ["10 eventos", "25 eventos", "60 eventos", "100 eventos", "200 eventos"],
                        [("Probabilidad exacta", [14.1, 31.6, 60.2, 78.8, 95.9], "teal"), ("Simulada (20 000)", [13.9, 31.6, 60.3, 78.8, 96.0], "grey")],
                        unit="% de muestras con al menos un defecto", decimals=1, ticks=[0, 20, 40, 60, 80, 100],
                        note="Una muestra de 25 «sin hallazgos» no prueba control: con 1,5 % de defectos ocurre el 68 % de las veces. Si los defectos se concentran (cuentas de servicio: 4 % de los eventos y 60 % de los defectos), 25 eventos al azar encuentran uno el 31,6 % de las veces; 15 de ese estrato más 10 del resto, el 98,7 %.",
                        note_kind="coral", foot=SINT)

def se394_cadena() -> Fig:
    return grouped_bars("Registro de 1 000 eventos con huellas encadenadas: 100 ataques de cada tipo",
                        "Barras horizontales con los ataques detectados de 100 por tipo: una cadena de huellas detecta 100 de 100 modificaciones, borrados intermedios y reordenamientos, pero 0 de 100 truncamientos de los últimos eventos y 0 de 100 reescrituras que recalculan las huellas; con la huella final publicada fuera del sistema detecta 100 de 100 de todos los tipos.",
                        ["Modificar un evento", "Borrar un evento intermedio", "Reordenar dos eventos", "Truncar los últimos 10 eventos", "Reescribir desde un evento recalculando las huellas"],
                        [("Solo la cadena", [100, 100, 100, 0, 0], "coral"), ("Cadena y huella publicada fuera", [100, 100, 100, 100, 100], "teal")],
                        unit="ataques detectados de 100", horizontal=True, label_w=330, ticks=[0, 25, 50, 75, 100],
                        note="La cadena detecta lo que rompe un eslabón y no lo que lo reconstruye bien: quien puede escribir puede recalcular. Hace falta un ancla fuera del alcance del atacante (un tercero, un sellado de tiempo, un registro de transparencia). El ancla debe publicarse antes del ataque; un ancla posterior no detecta nada.",
                        note_kind="teal", foot=SINT)

# ---------------------------------------------------------------- SE-467
def se395_rutas() -> Fig:
    return grouped_bars("5 000 cargas al azar (puntos, barras, %2e, %2f): cuántas salen de la raíz según el control",
                        "Barras agrupadas con las cargas de 5 000 que salen de la raíz según el control: quitar una vez la secuencia punto punto barra deja salir 2072 con rutas POSIX y 2154 con rutas de Windows, quitarla en bucle 1106 y 1181, y decodificar, resolver y comprobar el prefijo 0 y 0.",
                        ["Quitar «../» una vez y decodificar después", "Quitar «../» en bucle y decodificar después", "Decodificar, resolver y comprobar el prefijo de la raíz"],
                        [("Salen de la raíz (POSIX)", [2072, 1106, 0], "coral"), ("Salen de la raíz (Windows)", [2154, 1181, 0], "gold")],
                        unit="cargas que salen de la raíz, de 5 000",
                        note="El tercer control rechaza 903 cargas en POSIX y 958 en Windows y deja salir ninguna. Quitar «../» una vez convierte «....//secreto» en «../secreto». El bucle cierra ese caso y falla con la decodificación posterior (%2e%2e%2f), y las barras invertidas de Windows son otro separador. La reparación no filtra: resuelve la ruta final y comprueba que sigue dentro de la raíz.",
                        note_kind="coral", foot=SINT)

def se395_csrf() -> Fig:
    return heatmap("Defensa CSRF: cinco peticiones contra tres implementaciones (la primera solo comprueba que haya token)",
                   "Mapa de calor con si tres implementaciones de CSRF aceptan cinco peticiones: solo presencia acepta un token inventado, uno con un espacio y el de otra sesión; el valor global rechaza los inventados pero acepta el de otra sesión y rechaza el token propio; ligado a la sesión con un HMAC rechaza lo ajeno y acepta lo propio.",
                   ["Sin token", "Token inventado", "Token con un espacio", "Token válido de la sesión de otra persona", "Token propio de la sesión"], ["Solo presencia", "Valor global", "Ligado a la sesión"],
                   [[0, 0, 0], [1, 0, 0], [1, 0, 0], [1, 1, 0], [1, 0, 1]], unit="acepta la petición", scale="coral", vmin=0, vmax=1,
                   cell_fmt=lambda v: "ACEPTA" if v else "rechaza", highlight=[(1, 0), (2, 0), (3, 0), (3, 1), (4, 1)], label_w=300,
                   note="El contorno marca el comportamiento incorrecto: aceptar lo ajeno o rechazar lo propio. Las pruebas felices (token propio, sin token) pasan en la implementación débil: ninguna prueba que no intente falsificar detecta que el control es de apariencia. La implementación con valor global parece mejor y falla en la otra dirección. El token es un HMAC de la sesión, no un secreto compartido por todos.",
                   note_kind="gold", foot=SINT)

def se395_limitador() -> Fig:
    return case_cards("Dos controles aparentes más: limitador por cabecera X-Forwarded-For y verificación de token que lee el algoritmo del propio token",
                      "Seis pruebas contra un limitador por cabecera y un verificador de token que lee el algoritmo, con el control aparente y el reparado: cambiar la cabecera permite 1000 intentos frente a 5; un token con algoritmo none y rol docente se acepta frente a rechazarse; los tokens con otra clave o carga alterada se rechazan en ambos.",
                      [("1 000 intentos con una cabecera distinta en cada uno", "Aparente: 1 000 permitidos · Reparado: 5 permitidos", "El limitador cuenta por un dato que controla el atacante.", "coral"),
                       ("1 000 intentos sin cambiar de dirección", "Aparente: 5 permitidos · Reparado: 5 permitidos", "Sin trampa, los dos limitan igual.", "teal"),
                       ("Token legítimo", "Aparente: acepta · Reparado: acepta", "Las pruebas felices pasan en ambos.", "teal"),
                       ("Token con alg «none» y rol docente", "Aparente: ACEPTA · Reparado: rechaza", "El verificador confía en el encabezado del propio token.", "coral"),
                       ("Token con la firma de otra clave", "Aparente: rechaza · Reparado: rechaza", "La firma sí se comprueba.", "teal"),
                       ("Token con la carga alterada y la firma vieja", "Aparente: rechaza · Reparado: rechaza", "La firma sí se comprueba.", "teal")],
                      note="En ambos casos el control confía en un dato que controla el atacante: la cabecera y el encabezado del token. Con el control reparado solo cambia quién decide (la conexión, el servidor). Detrás de un proxy la reparación exige configurar qué proxies son de confianza.",
                      note_kind="coral", foot=SINT)

# ---------------------------------------------------------------- SE-468
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
    return case_cards("La huella de un paquete de cinco archivos construido en Windows y en Ubuntu (WSL2)",
                      "Tres métodos de huella de un paquete de cinco archivos en Windows y en Ubuntu como tarjetas: el listado de un mismo directorio sale en distinto orden y la huella ingenua difiere (dcb7a0e6 frente a 9eb5bb1c); una huella canónica con rutas ordenadas, saltos de línea normalizados y separador barra coincide en los dos (7f9dbc41).",
                      [("Orden de os.listdir", "Windows: A.txt, b.txt, informe, ñ.txt · Ubuntu: A.txt, ñ.txt, b.txt, informe", "No coinciden: el orden depende del sistema de archivos.", "coral"),
                       ("Huella ingenua (orden del sistema, bytes crudos)", "Windows: dcb7a0e6… · Ubuntu: 9eb5bb1c…", "No coinciden.", "coral"),
                       ("Huella canónica (rutas ordenadas, LF, separador /)", "Windows: 7f9dbc41… · Ubuntu: 7f9dbc41…", "Coinciden.", "teal")],
                      note="Dos personas que ejecutan lo mismo en equipos distintos no obtienen la misma huella si la huella depende del orden del sistema de archivos o de los finales de línea. La huella canónica define el orden, la codificación y la normalización; con ella la verificación entre sistemas se puede automatizar.",
                      note_kind="teal", foot=SONDA)

def se396_operadores() -> Fig:
    ops = ["Quitar la evidencia", "Evidencia o prueba que no existe", "Evidencia de 120 días; alcance de otra versión", "No aplica sin justificación; excepción sin dueño", "Identificador duplicado",
           "Misma evidencia en 10 requisitos o copia de otro", "Prueba sin aserciones; prueba fallida marcada como cumple", "Archivo de evidencia vacío", "Evidencia única que dice «aprobado» sin ejecutar nada"]
    return heatmap("Mutaciones del paquete detectadas por operador (de 15 cada una) según el validador",
                   "Mapa de calor con las mutaciones detectadas de 15 por operador según tres validadores: quitar la evidencia lo detectan los tres; existencia, fecha, alcance, justificación, dueño y duplicados el de estructura y el semántico; huellas repetidas, pruebas sin aserciones y archivos vacíos solo el semántico; la evidencia única sin relación con el requisito, ninguno.",
                   ops, ["Presencia", "Estructura", "Con heurísticas"],
                   [[15, 15, 15], [0, 15, 15], [0, 15, 15], [0, 15, 15], [0, 15, 15], [0, 0, 15], [0, 0, 15], [0, 0, 15], [0, 0, 0]], unit="detectadas de 15", scale="teal", vmin=0, vmax=15, label_w=360, cell_h=40,
                   note="Cada capa añade reglas que alguien tuvo que imaginar; el mapa se llena en escalera de izquierda a derecha. La última fila no cae en ninguna regla porque su forma es la de una evidencia correcta. Las agrupaciones suman 14 operadores; en las filas con dos, cada valor es la detección de cada uno de ellos.",
                   note_kind="gold", foot=SINT)

FIGURES = {
    "se-463-unicidad-y-generalizacion.svg": se391_unicidad,
    "se-463-ruido-y-presupuesto.svg": se391_ruido,
    "se-463-seudonimos-y-enlace.svg": se391_seudonimos,
    "se-464-mutantes-del-validador.svg": se392_mutantes,
    "se-464-reglas-de-seguridad.svg": se392_reglas,
    "se-464-regex-catastrofica.svg": se392_regex,
    "se-465-puntajes-cvss.svg": se393_cvss,
    "se-465-prioridad-por-explotacion.svg": se393_prioridad,
    "se-465-triaje-de-informes.svg": se393_triaje,
    "se-466-embudo-de-cobertura.svg": se394_embudo,
    "se-466-muestreo-de-auditoria.svg": se394_muestreo,
    "se-466-registro-con-cadena.svg": se394_cadena,
    "se-467-filtro-de-rutas.svg": se395_rutas,
    "se-467-defensa-csrf.svg": se395_csrf,
    "se-467-limitador-y-token.svg": se395_limitador,
    "se-468-validador-de-paquete.svg": se396_validador,
    "se-468-huella-entre-sistemas.svg": se396_portabilidad,
    "se-468-mutaciones-por-operador.svg": se396_operadores,
}
