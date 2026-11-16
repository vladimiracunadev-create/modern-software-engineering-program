"""Figures for SE-421 to SE-426 (synthetic data, fixed seeds, virtual time; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from experiments_part35_a import (
    e421_atribucion, e421_preguntas, e421_segmento, e422_correlacion, e422_formato, e422_politicas, e423_contadores, e423_histogramas,
    e424_contexto, e424_muestreo, e424_ruta_critica, e425_composicion, e425_donde_se_mide, e425_trafico, e426_reglas, e426_ruido, e426_ventanas,
)
from figure_kit import Fig
from figures_part07_a import tab

SINT = "Datos sintéticos con semilla fija y tiempo virtual; Windows y Ubuntu (WSL2) dan cifras idénticas."
MEDIDO_35 = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); el valor de memoria depende de la versión del intérprete."


def n(x: float, d: int = 0) -> str:
    """Formato español: espacio como separador de miles y coma decimal."""
    return f"{x:,.{d}f}".replace(",", "§").replace(".", ",").replace("§", " ")


def p(x: float, d: int = 1) -> str:
    return n(100 * x, d) + " %"


# ---------------------------------------------------------------- SE-421
def se421_localizar() -> Fig:
    r = e421_atribucion()
    h, total = r["aciertos"], r["incidentes"]
    rows = [
        ["Solo la latencia del borde (adivinar entre cuatro)", f"{h['solo borde']} de {total}", "Dice que algo va lento, no dónde"],
        ["p99 absoluto de la duración que ve cada servicio", f"{h['p99 absoluto']} de {total}", "Gana siempre la pasarela, que incluye a todos"],
        ["Aumento relativo del p99 frente a su línea base", f"{h['aumento relativo']} de {total}", "Funciona porque hay línea base y todos miden"],
        ["Lo mismo con un servicio sin instrumentar", f"{h['aumento relativo sin un servicio']} de {total}", "Culpa al vecino que sí se ve"],
    ]
    return tab("Localizar el componente lento en una cadena de cuatro servicios con cuatro conjuntos de señales",
               f"Tabla: en {total} incidentes sintéticos con un servicio lento, mirar solo el borde acierta {h['solo borde']}, el percentil 99 absoluto acierta {h['p99 absoluto']}, el aumento relativo del percentil 99 frente a la línea base acierta {h['aumento relativo']}, y el mismo método sin ver uno de los cuatro servicios acierta {h['aumento relativo sin un servicio']}.",
               ["Señales disponibles", "Localizaciones correctas", "Lectura"], rows, [430, 190, 300], row_h=52, size=13,
               note="Cada servicio informa su duración inclusiva (la suya más la de lo que llama). La línea base de 400 peticiones sanas y los factores de lentitud de 3 a 8 son supuestos del autor. Un punto ciego no apaga la alarma: la desplaza al servicio vecino, y por eso un hueco de instrumentación se parece a una conclusión.",
               note_kind="coral", foot=SINT)


def se421_cliente() -> Fig:
    r = e421_segmento()
    rows = []
    for name, v in r.items():
        rows.append([name, p(v["cuota de tráfico %"] / 100, 2), p(v["tasa global > 1 % en 5 min"], 0), p(v["sonda fija en el cliente 1"], 0), p(v["sonda rotativa"], 0)])
    return tab("Una falla total que afecta a un solo cliente: qué señal la detecta en una hora",
               "Tabla: si falla por completo un cliente que aporta 23,4 por ciento del tráfico, el umbral global de 1 por ciento en 5 minutos lo detecta siempre; si aporta 2,3, también; si aporta 0,58, lo detecta en 8,7 por ciento de los intentos. Una sonda fija en el cliente grande solo ve al cliente grande; una sonda que rota por los 40 clientes detecta a todos en 40 minutos como máximo.",
               ["Cliente afectado", "Cuota de tráfico", "Tasa global > 1 %", "Sonda fija", "Sonda rotativa"], rows, [310, 150, 170, 140, 150], row_h=52, size=13,
               note="El cliente de la cola larga está 100 % caído y la tasa global apenas se mueve: aporta 0,58 % de las peticiones y el umbral exige 1 %. La sonda rotativa lo encuentra, pero tarda hasta 40 minutos. Cuarenta clientes con reparto 1/k son un supuesto del autor; la forma del reparto real cambia el resultado.",
               note_kind="gold", foot=SINT)


def se421_preguntas() -> Fig:
    r = e421_preguntas()
    day_mb = r["bytes por evento"] * r["peticiones por día"] / 1e6
    rows = [
        ["Métricas con 3 dimensiones previstas", f"{r['responde métricas']} de {r['preguntas']}", n(r["series por métrica previstas"]) + " series", "Barato, cerrado a lo previsto"],
        ["Eventos anchos con todos los campos", f"{r['responde eventos anchos']} de {r['preguntas']}", f"{n(day_mb)} MB al día", f"{r['bytes por evento']} bytes por evento, un millón de peticiones"],
        ["Métricas con todas las combinaciones", f"{r['preguntas']} de {r['preguntas']}", n(r["series para todas las combinaciones"]) + " series", "Responde todo y no cabe en un almacén de métricas"],
    ]
    return tab("Sesenta preguntas hechas después de un incidente: qué diseño de señales puede responderlas",
               f"Tabla: con tres dimensiones previstas las métricas responden {r['responde métricas']} de las {r['preguntas']} preguntas con {n(r['series por métrica previstas'])} series; los eventos anchos las responden todas con unos {n(day_mb)} megabytes al día; cubrir todas las combinaciones con métricas exigiría {n(r['series para todas las combinaciones'])} series.",
               ["Diseño", "Preguntas respondidas", "Coste", "Lectura"], rows, [310, 170, 190, 250], row_h=64, size=12,
               note="Las 60 preguntas son combinaciones de 1 a 3 de las 8 dimensiones del servicio (endpoint, estado, región, curso, cliente, versión, dispositivo, plan); las dimensiones previstas son endpoint, estado y región. Los eventos conservan el detalle a cambio de volumen y de privacidad: cada campo extra es un dato que alguien puede leer.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-422
def se422_formato() -> Fig:
    r = e422_formato()
    words = ["Entrega 123 aceptada para curso 45 en 83 ms", "Entrega aceptada: id=123 curso=45 duración=83ms", "[api] entrega id=123 (curso 45) OK tiempo=83 milisegundos", "Submission 123 accepted for course 45 in 83 ms"]
    keys = ["id, curso, ms", "id, curso, ms", "id, curso, ms + región", "id, curso, duration_ms (renombrado)"]
    rows = []
    for i, row in enumerate(r["filas"]):
        rows.append([f"v{row['versión']}: {words[i]}", p(row["regex v1"], 0), keys[i], p(row["json por nombre"], 0)])
    return tab("La misma línea de registro en cuatro versiones del código: extracción con una expresión regular y con campos por nombre",
               "Tabla: una expresión regular escrita para la versión 1 extrae el 100 por ciento de las líneas de esa versión y 0 de las tres siguientes; leer campos por nombre de un registro JSON sigue en 100 por ciento cuando cambia la redacción o se añade un campo y cae a 0 cuando se renombra un campo.",
               ["Redacción del mensaje", "Regex v1", "Campos del registro JSON", "JSON por nombre"], rows, [430, 100, 270, 120], row_h=52, size=12,
               note="Cada versión se evaluó con 1 500 líneas. El registro estructurado mueve la ruptura del texto al contrato: sobrevive a un cambio de redacción y no a un campo renombrado. Por eso el nombre de un campo es una interfaz que se versiona y se prueba, no un detalle de implementación.",
               note_kind="gold", foot=SINT)


def se422_correlacion() -> Fig:
    r = e422_correlacion()
    rows = []
    for e in r["propagación"]:
        rows.append([f"Cada salto conserva el identificador con probabilidad {n(e['p por salto'], 2)}", p(e["completas simuladas"]), f"Fórmula p⁴ = {p(e['p^4'])}"])
    for e in r["huérfanas"]:
        rows.append([f"Línea sin identificador a {e['solicitudes por segundo']} peticiones por segundo", p(e["atribuibles de forma única"]), "Atribuible solo por tiempo"])
    return tab("Correlación: cadenas completas según la propagación del identificador y líneas huérfanas atribuibles solo por el reloj",
               "Tabla: en una cadena de cinco servicios con cuatro saltos, conservar el identificador con probabilidad 0,99 por salto deja 95,9 por ciento de las peticiones completas, 0,95 deja 81,4, 0,90 deja 66,3 y 0,80 deja 40,8. Una línea huérfana solo se puede atribuir por tiempo en 58,6 por ciento de los casos a una petición por segundo y en 0 por ciento desde 20.",
               ["Condición", "Resultado", "Contraste"], rows, [470, 140, 270], row_h=40, size=12,
               note="La propagación falla de forma multiplicativa: cuatro saltos al 95 % dejan 81 % y la cola de peticiones incompletas es justo la de las colas y los hilos. Sin identificador, el tiempo solo desambigua con tráfico muy bajo; con una petición durando hasta 250 ms (supuesto del autor), a 20 por segundo siempre hay varias candidatas.",
               note_kind="coral", foot=SINT)


def se422_politicas() -> Fig:
    r = e422_politicas()
    red = r["redacción"]
    rows = [
        ["Tamaño de la misma línea", f"{r['bytes texto']} bytes de texto", f"{r['bytes json']} bytes de JSON", "El JSON repite las claves en cada línea"],
        ["Muestreo uniforme del 10 %", f"{n(r['retenidas 10 %'])} de {n(r['líneas'])} líneas", f"{n(r['errores con 10 %'])} de {n(r['errores'])} errores", "Pierde 9 de cada 10 errores"],
        ["Todos los errores y 10 % del resto", f"{n(r['retenidas errores+10 %'])} líneas", f"{n(r['errores'])} de {n(r['errores'])} errores", f"Conserva {p(r['retenidas errores+10 %'] / r['líneas'])} del volumen"],
        ["Redacción de correos con una regex", f"{red['correo'][0]} de {red['correo'][1]}", "Falla con mayúsculas y con variantes", "Reconoce dos de cinco formatos"],
        ["Redacción de tokens con prefijo fijo", f"{red['token'][0]} de {red['token'][1]}", "Formato cerrado y conocido", "Funciona porque el formato es estable"],
        ["Redacción de documentos de identidad", f"{red['documento'][0]} de {red['documento'][1]}", "Solo el formato con puntos", "Reconoce un formato de cinco"],
    ]
    return tab("Coste, muestreo y redacción de registros: tamaño, errores conservados y datos personales detectados",
               "Tabla: la misma línea pesa 117 bytes en texto y 166 en JSON; conservar el 10 por ciento de las líneas deja 412 de 4 039 errores, mientras que conservar todos los errores y el 10 por ciento del resto ocupa 11,8 por ciento del volumen; una expresión regular para correos detecta 40 de 100 variantes, una de tokens detecta 100 de 100 y una de documentos de identidad detecta 20 de 100.",
               ["Política", "Resultado", "Detalle", "Lectura"], rows, [250, 190, 220, 250], row_h=52, size=12,
               note="La redacción por patrones solo protege los formatos que alguien previó: cada variante escrita por una persona (mayúsculas, espacios, un «arroba» escrito) es un dato personal que llega al almacén. Los 200 000 registros y las variantes son sintéticos; el 2 % de errores es un supuesto del autor.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-423
def se423_cardinalidad() -> Fig:
    steps = [("endpoint × estado × región (5 × 3 × 3)", 45), ("+ curso (30)", 1350), ("+ cliente (40)", 54000), ("+ identificador de persona (20 000)", 1080000000)]
    per = 429
    rows = []
    for name, series in steps:
        mem = series * per
        shown = f"{n(mem / 1e3, 0)} KB" if mem < 1e6 else (f"{n(mem / 1e6, 1)} MB" if mem < 1e9 else f"{n(mem / 1e9)} GB")
        rows.append([name, n(series), shown, "Cabe" if series <= 54000 else "No cabe en ningún almacén de métricas"])
    return tab("El número de series de una sola métrica según las dimensiones que se le añaden",
               "Tabla: una métrica con las dimensiones endpoint, estado y región tiene 45 series; añadir curso la lleva a 1 350, añadir cliente a 54 000 y añadir el identificador de una persona a 1 080 millones de series, unos 463 gigabytes con 429 bytes por serie.",
               ["Dimensiones", "Series", "Memoria estimada", "Veredicto"], rows, [360, 180, 170, 210], row_h=52, size=13,
               note="El número de series es el producto de las cardinalidades, no la suma, y cada serie nueva cuesta memoria e índice aunque nadie la consulte. Los 429 bytes por serie son una medición de CPython en este equipo con un diccionario de claves de texto; un almacén real tiene otra constante, y la forma del crecimiento es la misma.",
               note_kind="coral", foot=MEDIDO_35)


def se423_contadores() -> Fig:
    r = e423_contadores()
    c15, c60 = r["intervalos"]
    rows = [
        [f"Incremento real (600 s, 3 reinicios)", n(r["verdad"]), "Verdad de la simulación"],
        ["Último valor menos primero, scrape cada 15 s", n(c15["diferencia ingenua"]), "Pierde todo lo anterior al último reinicio"],
        ["Con detección de reinicios, scrape cada 15 s", n(c15["con reinicios"]), f"Pierde {p((r['verdad'] - c15['con reinicios']) / r['verdad'])}"],
        ["Con detección de reinicios, scrape cada 60 s", n(c60["con reinicios"]), f"Pierde {p((r['verdad'] - c60['con reinicios']) / r['verdad'])}"],
        ["Pico de 20 s de un gauge visto con scrape de 15 s", p(r["picos"][20][15], 0), "Se ve siempre"],
        ["Pico de 20 s de un gauge visto con scrape de 60 s", p(r["picos"][20][60], 0), "Se ve una de cada tres veces"],
        ["Pico de 20 s de un gauge visto con scrape de 300 s", p(r["picos"][20][300], 0), "Casi nunca"],
    ]
    return tab("Contador con reinicios y pico de un gauge: qué reconstruye cada forma de leer y cada intervalo de muestreo",
               "Tabla: un contador de 60 513 incrementos con tres reinicios se lee como 14 858 si se resta el último valor del primero, como 60 198 con detección de reinicios y scrape de 15 segundos y como 55 707 con scrape de 60 segundos; un pico de 20 segundos de un gauge se observa en 100 por ciento de los casos con scrape de 15 segundos, 32,9 con 60 y 6,7 con 300.",
               ["Lectura", "Resultado", "Lectura de la cifra"], rows, [430, 140, 320], row_h=40, size=12,
               note="Un contador sobrevive a un muestreo grueso porque acumula; un gauge no, porque el valor entre dos lecturas desaparece. La detección de reinicios pierde el tramo anterior a cada reinicio dentro del intervalo. Tasa de 100 por segundo, reinicios en 137, 301 y 452 s y picos uniformes son supuestos del autor.",
               note_kind="gold", foot=SINT)


def se423_histogramas() -> Fig:
    r = e423_histogramas()
    truth = r["verdad"]
    rows = [["Verdad (100 000 muestras lognormales)", n(truth[50], 1) + " ms", n(truth[95], 1) + " ms", n(truth[99], 1) + " ms"]]
    for name, v in r["diseños"].items():
        def cell(q):
            return f"{n(v[q], 1)} ms ({'+' if v[q] >= truth[q] else '−'}{n(abs(v[q] - truth[q]) / truth[q] * 100, 0)} %)"
        rows.append([f"Cubetas: {name}", cell(50), cell(95), cell(99)])
    return tab("Percentiles estimados con histogramas de tres diseños de cubetas frente al valor exacto",
               "Tabla: con 100 000 latencias lognormales cuya mediana exacta es 120,5 milisegundos, el percentil 95 exacto es 381 y el 99 es 608,2, las cubetas lineales de 100 milisegundos estiman 387,5 y 612,6, las exponenciales de factor dos estiman 458,1 y 632,2 y las cubetas por defecto estiman 443,7 y 776,4.",
               ["Diseño", "p50", "p95", "p99"], rows, [350, 190, 190, 190], row_h=52, size=13,
               note="La interpolación lineal dentro de una cubeta supone datos repartidos de forma uniforme y el error nunca es menor que el ancho de la cubeta donde cae el percentil. Cubetas pensadas para otro rango (hasta 10 s) estiman el p99 con un 28 % de error. Elegir cubetas es elegir el error permitido antes de ver el incidente.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-424
def se424_contexto() -> Fig:
    r = e424_contexto()
    rows = [
        ["Salto HTTP síncrono (pierde el contexto 1 %)", "Cabecera copiada por la biblioteca", "Casi nunca fragmenta"],
        ["Cola de mensajes (15 %)", "Hay que copiar el contexto a las propiedades del mensaje", "La traza se parte en el productor"],
        ["Grupo de hilos o tarea asíncrona (20 %)", "El contexto vive en la variable del hilo", "El trabajo posterior queda huérfano"],
        ["Reintento automático (10 %)", "Se crea una petición nueva", "El intento nuevo abre otra traza"],
        ["Peticiones con una sola traza completa", p(r["completas"]), f"{n(r['trozos por petición'], 2)} trozos por petición, hasta {r['máximo de trozos']}"],
        ["Cabeceras traceparent inválidas rechazadas", f"{r['inválidas'] - r['inválidas aceptadas']} de {r['inválidas']}", f"Válidas aceptadas: {r['válidas aceptadas']} de {r['válidas']}"],
    ]
    return tab("Propagación del contexto en una petición de seis saltos: dónde se rompe la traza y qué fracción queda completa",
               "Tabla: en una petición con seis saltos, el salto HTTP pierde el contexto 1 por ciento de las veces, la cola de mensajes 15, el grupo de hilos 20 y el reintento automático 10; solo 59,4 por ciento de las peticiones queda en una única traza y el promedio es 1,48 trozos por petición con un máximo de cuatro.",
               ["Frontera", "Mecanismo", "Efecto"], rows, [330, 310, 280], row_h=52, size=12,
               note="Las probabilidades por frontera son supuestos del autor, pero el patrón es de diseño: el contexto se pierde donde cambia el medio de transporte o la unidad de ejecución. El formato W3C traceparent (versión, identificador de traza de 32 hex, identificador de span de 16 hex, banderas) se valida con una expresión regular estricta en minúsculas.",
               note_kind="gold", foot=SINT)


def se424_critica() -> Fig:
    r = e424_ruta_critica()
    a, b, c = list(r["ahorro medio ms"])
    rows = [[k.capitalize(), n(r["ahorro medio ms"][k], 1) + " ms", p(r["sin ahorro %"][k] / 100)] for k in (a, b, c)]
    return tab("Reducir a la mitad un span: ahorro medio de latencia según cómo se elige el span a optimizar",
               f"Tabla: en {r['árboles']} árboles de spans sintéticos con latencia media de {n(r['latencia media ms'], 0)} milisegundos, reducir a la mitad un span al azar ahorra {n(r['ahorro medio ms'][a], 1)} milisegundos y no ahorra nada en {n(r['sin ahorro %'][a])} por ciento de los árboles; el span con más tiempo propio ahorra {n(r['ahorro medio ms'][b], 1)} y no ahorra nada en {n(r['sin ahorro %'][b])} por ciento; el de la ruta crítica ahorra {n(r['ahorro medio ms'][c], 1)} y siempre ahorra algo.",
               ["Qué span se optimiza", "Ahorro medio", "Árboles sin ahorro"], rows, [520, 190, 190], row_h=52, size=13,
               note="Un span fuera de la ruta crítica (hijos paralelos que no son el más lento) no cambia la latencia de la petición aunque se acelere. Los árboles (3 a 5 hijos en la raíz, hasta 3 niveles, la mitad de los nodos con hijos en paralelo) son un generador del autor, no trazas observadas.",
               note_kind="teal", foot=SINT)


def se424_muestreo() -> Fig:
    r = e424_muestreo()
    rc = r["recuento"]
    rows = [
        ["Muestreo de cabeza del 1 %: errores conservados", f"{r['cabeza 1 %']['error']} de {n(rc['error'])}", f"{p(r['cabeza 1 %']['error'] / rc['error'])}"],
        ["Muestreo de cabeza del 1 %: trazas lentas conservadas", f"{r['cabeza 1 %']['lenta']} de {n(rc['lenta'])}", f"{p(r['cabeza 1 %']['lenta'] / rc['lenta'])}"],
        ["Muestreo por cola: errores y lentas conservadas", f"{n(r['cola']['error'] + r['cola']['lenta'])} de {n(rc['error'] + rc['lenta'])}", "100 %"],
        ["Trazas almacenadas por 100 000 (cabeza frente a cola)", f"{n(r['almacenadas cabeza'])} frente a {n(r['almacenadas cola'])}", f"{n(r['almacenadas cola'] / r['almacenadas cabeza'], 1)} veces más"],
        ["Trazas completas con dos recolectores y enrutado aleatorio", p(r["enrutado"][2]["completas con enrutado aleatorio"]), "Con hash del identificador: 100 %"],
        ["Trazas completas con cuatro recolectores y enrutado aleatorio", p(r["enrutado"][4]["completas con enrutado aleatorio"]), "Con hash del identificador: 100 %"],
    ]
    return tab("Muestreo de trazas: lo interesante que conserva cada política y el efecto de enrutar los spans a varios recolectores",
               "Tabla: sobre 100 000 trazas con 976 errores y 1 994 lentas, el muestreo de cabeza del 1 por ciento conserva 9 errores y 30 lentas, el muestreo por cola conserva las 2 970 y almacena 3 967 trazas frente a 1 045; con dos recolectores y enrutado aleatorio solo 1,7 por ciento de las trazas llega completa a un mismo recolector, y con cuatro, 0 por ciento.",
               ["Política", "Resultado", "Contraste"], rows, [420, 260, 240], row_h=52, size=12,
               note="El muestreo por cola decide con la traza entera, así que exige que todos los spans de una traza lleguen al mismo recolector (enrutado por hash del identificador) y memoria para retenerlos mientras se decide. Las proporciones de 1 % de errores y 2 % de lentas son supuestos del autor.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-425
def se425_trafico() -> Fig:
    r = e425_trafico()
    rows = []
    for e in r["escenarios"]:
        rows.append([e["nombre"], n(e["disponibilidad por peticiones %"], 3) + " %", n(e["presupuesto gastado por peticiones %"], 0) + " %", n(e["presupuesto gastado por minutos %"], 0) + " %"])
    return tab("Un presupuesto de error del 99,9 % mensual medido por peticiones y por minutos en tres incidentes",
               "Tabla: un corte total de 30 minutos a las 03:00 consume 8,6 por ciento del presupuesto mensual contado por peticiones y 69,4 contado por minutos; el mismo corte a las 14:00 consume 166 por ciento por peticiones y 69,4 por minutos; un 5 por ciento de errores durante 8 horas consume 121 por ciento por peticiones y 1 111 por minutos.",
               ["Incidente", "Disponibilidad por peticiones", "Presupuesto por peticiones", "Presupuesto por minutos"], rows, [380, 190, 170, 170], row_h=52, size=12,
               note="Contar por peticiones pondera el daño por las personas afectadas; contar minutos malos no distingue el tráfico y, con un umbral de 1 %, trata como minuto perdido uno con 5 % de errores. El tráfico (5 por segundo de noche, hasta 100 de día) y los 43,2 minutos mensuales del 99,9 % son el marco del autor.",
               note_kind="gold", foot=SINT)


def se425_donde() -> Fig:
    r = e425_donde_se_mide()
    rows = [
        ["Éxito medido en el servidor", n(r["servidor %"], 3) + " %", "No ve a quien no llegó"],
        ["Éxito medido en el cliente, un intento", n(r["cliente por intento %"], 3) + " %", "Incluye la red del usuario"],
        ["Tres intentos si todos los fallos fueran independientes", n(r["3 intentos si todo fuera independiente %"], 4) + " %", "El cálculo que promete el reintento"],
        ["Tres intentos con fallos pegados a la petición", n(r["3 intentos con fallos pegados %"], 4) + " %", "Cien veces más fallos que la cifra anterior"],
    ]
    return tab("La misma disponibilidad medida en el servidor, en el cliente y tras reintentos",
               "Tabla: con 200 000 solicitudes sintéticas, el servidor mide 99,927 por ciento de éxito, el cliente con un solo intento mide 97,961, tres intentos independientes darían 99,9995 y tres intentos con un 0,03 por ciento de fallos pegados a la petición dan 99,9705.",
               ["Dónde y cómo se mide", "Éxito", "Lectura"], rows, [470, 140, 310], row_h=52, size=13,
               note="El servidor no cuenta lo que no llegó (2 % de fallos de red del cliente, supuesto del autor) y el reintento solo ayuda con fallos independientes: 0,03 % de peticiones que fallan siempre aparece como 0,03 % de fallos aunque se intente tres veces. Un objetivo debe nombrar el punto de medición.",
               note_kind="coral", foot=SINT)


def se425_composicion() -> Fig:
    r = e425_composicion()
    rows = [[k.capitalize(), n(v, 3) + " %", "Producto de disponibilidades"] for k, v in r["serie"].items()]
    for label, v in ((k, r[k]) for k in ("duración mediana 20 min", "duración mediana 10 min")):
        rows.append([f"Incidentes de {label}", f"SLO 99,9 %: incumple {n(v['incumple SLO 99,9 %'], 1)} % de los meses", f"SLA 99,5 %: {n(v['incumple SLA 99,5 %'], 2)} %"])
    return tab("Composición de dependencias en serie y meses que incumplen un SLO y un SLA según la duración de los incidentes",
               "Tabla: cinco dependencias de 99,9 por ciento en serie dan 99,501 por ciento; con 1,2 incidentes al mes de duración mediana de 20 minutos, 30,9 por ciento de los meses incumple un objetivo de 99,9 por ciento y 1,72 incumple uno de 99,5; con duración mediana de 10 minutos esas cifras bajan a 13,9 y 0,2.",
               ["Caso", "Resultado", "Lectura"], rows, [310, 340, 270], row_h=52, size=12,
               note="Un SLO de 99,9 % con tres o más dependencias del mismo nivel ya es optimista, y un SLA más holgado que el SLO deja margen para el contrato y no para la ingeniería. Dos incidentes de 20 minutos agotan el mes entero. 20 000 meses simulados; 1,2 incidentes por mes y la forma lognormal son supuestos del autor.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-426
def se426_reglas() -> Fig:
    r = e426_reglas()
    rows = []
    for x in r["reglas"]:
        delay = "—" if x["retraso mediano min"] is None else f"{x['retraso mediano min']} min"
        rows.append([x["regla"].capitalize(), n(x["páginas"]), f"{x['caídas detectadas']} de {r['caídas']}", f"{x['degradaciones detectadas']} de {r['degradaciones']}", delay, n(x["páginas sin incidente"])])
    return tab("Seis reglas de alerta sobre 180 días de tráfico diurno y nocturno con 14 caídas y 12 degradaciones lentas",
               "Tabla: el umbral de 0,5 por ciento en un minuto genera 12 622 páginas, 11 748 sin incidente; el umbral de 1 por ciento en 5 minutos genera 609 páginas, 396 sin incidente; el de 1 por ciento en 30 minutos genera 27 páginas sin ninguna falsa y detecta 13 caídas y 6 degradaciones; la regla de consumo 14,4 veces detecta 13 caídas y 1 degradación con 13 páginas; la combinación de consumo 14,4 y 6 veces detecta 13 caídas y 8 degradaciones con 31 páginas.",
               ["Regla", "Páginas", "Caídas", "Degradaciones", "Retraso mediano", "Sin incidente"], rows, [290, 100, 110, 150, 140, 130], row_h=40, size=12,
               note="Ninguna regla detecta las 12 degradaciones sin pagar páginas falsas: la regla de 1 % en 5 minutos las ve todas porque de noche, con 30 peticiones por minuto, dos errores bastan. Una página que no pide acción es coste puro. Tasa de error base de 0,1 %, tráfico entre 30 y 300 por minuto e incidentes inyectados son supuestos del autor.",
               note_kind="coral", foot=SINT)


def se426_ruido() -> Fig:
    r = e426_ruido()
    rows = [
        ["Sin filtros: cada alerta de cada servicio pagina", n(r["páginas sin filtros"]), p(r["accionables sin filtros %"] / 100), "Casi todo es ruido o repetición"],
        ["Con duración mínima antes de paginar", n(r["con duración mínima"]), p(r["incidentes"] / r["con duración mínima"]), "Quita destellos, no cascadas"],
        ["Con duración mínima y agrupación por incidente", n(r["con duración y agrupación"]), p(r["accionables agrupadas %"] / 100), "Una página por incidente más los destellos que sobreviven"],
    ]
    return tab("Fatiga de alertas: páginas por 200 incidentes en cascada y 3 000 destellos según las tres políticas de filtrado",
               "Tabla: 200 incidentes en cascada de 8,1 alertas en promedio, cada una con tres oscilaciones, más 3 000 destellos autorresueltos generan 7 881 páginas sin filtros, de las cuales 2,5 por ciento corresponde a incidentes; exigir una duración mínima las reduce a 1 735 y agrupar por incidente las reduce a 308, con 64,9 por ciento de páginas que corresponden a un incidente.",
               ["Política", "Páginas", "Páginas que son un incidente", "Lectura"], rows, [370, 110, 190, 250], row_h=52, size=12,
               note="Filtrar no es silenciar: el filtro de duración retrasa la página por construcción y la agrupación exige conocer el mapa de dependencias para saber qué alertas pertenecen al mismo incidente. El 4 % de destellos que sobrevive al filtro es un supuesto del autor.",
               note_kind="gold", foot=SINT)


def se426_ventanas() -> Fig:
    r = e426_ventanas()
    rows = [[f"{x['ventana min']} min", n(x["falsos positivos por día"], 2), f"{x['2 % de errores']} min", f"{x['10 % de errores']} min", f"{x['100 % de errores']} min"] for x in r["filas"]]
    return tab("Umbral de 1 % de errores con ventanas de 1 a 60 minutos: falsos positivos al día y minutos hasta alertar",
               "Tabla: con 100 peticiones por minuto, una ventana de un minuto produce 6,85 falsos positivos al día; una de 5 minutos, 0,02; las de 15 y 60 minutos, ninguno; con un 2 por ciento de errores la mediana hasta alertar es 1 minuto, 3, 8 y 28 minutos para las ventanas de 1, 5, 15 y 60 minutos, y con una caída total es 1 minuto en todas.",
               ["Ventana", "Falsos positivos por día", "Con 2 % de errores", "Con 10 % de errores", "Con caída total"], rows, [140, 220, 190, 190, 180], row_h=52, size=13,
               note="Una ventana larga suprime el ruido y retrasa lo moderado, y a una caída total no la retrasa casi nada: por eso se combinan ventanas largas para lo lento y cortas para lo grave. La ventana incluye la historia sana previa al incidente; 120 días de ruido con 100 peticiones por minuto es un supuesto del autor.",
               note_kind="teal", foot=SINT)


FIGURES = {
    "se-421-localizar-la-lentitud.svg": se421_localizar,
    "se-421-falla-de-un-solo-cliente.svg": se421_cliente,
    "se-421-preguntas-sin-respuesta.svg": se421_preguntas,
    "se-422-cuatro-versiones-del-registro.svg": se422_formato,
    "se-422-propagacion-y-lineas-huerfanas.svg": se422_correlacion,
    "se-422-volumen-muestreo-y-redaccion.svg": se422_politicas,
    "se-423-explosion-de-series.svg": se423_cardinalidad,
    "se-423-contadores-y-picos.svg": se423_contadores,
    "se-423-percentiles-con-histogramas.svg": se423_histogramas,
    "se-424-donde-se-rompe-el-contexto.svg": se424_contexto,
    "se-424-ruta-critica.svg": se424_critica,
    "se-424-muestreo-de-trazas.svg": se424_muestreo,
    "se-425-peticiones-o-minutos.svg": se425_trafico,
    "se-425-donde-se-mide.svg": se425_donde,
    "se-425-composicion-y-meses.svg": se425_composicion,
    "se-426-seis-reglas-de-alerta.svg": se426_reglas,
    "se-426-fatiga-y-agrupacion.svg": se426_ruido,
    "se-426-ventanas-de-alerta.svg": se426_ventanas,
}
