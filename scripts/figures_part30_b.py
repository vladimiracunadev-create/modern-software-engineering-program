"""Figures for SE-367 to SE-372 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, _kit_finish, _kit_start, fmt_es, grouped_bars, line_chart, stacked_bars
from figures_part07_a import bars

SINT = "Datos sintéticos y modelos del autor con semilla fija; Windows (CPython 3.12.9) y Ubuntu (WSL2, 3.12.3) con cifras idénticas salvo donde se indica."


# ---------------------------------------------------------------- SE-367
def se367_fidelidad() -> Fig:
    return stacked_bars(
        "Fidelidad de dos dobles de un repositorio medida con las mismas 8 comprobaciones de contrato",
        "Barras apiladas horizontales: SQLite real pasa las 8 comprobaciones; el diccionario ingenuo pasa 4 y no rechaza el identificador duplicado, la nota fuera de rango, el estudiante nulo ni el correo repetido con otra capitalización; el diccionario con las reglas añadidas pasa las 8.",
        ["SQLite real (referencia)", "Diccionario ingenuo", "Diccionario con las reglas añadidas"],
        [("Superadas", [8, 4, 8], "teal"), ("No superadas", [0, 4, 0], "coral")],
        unit="comprobaciones de contrato (de 8)", horizontal=True, label_w=250, totals=False,
        note="El doble ingenuo hace pasar pruebas de servicio que con la base real fallarían. Pasar las ocho comprobaciones demuestra que el doble reproduce esas ocho reglas, no que reproduzca la base: una novena comprobación (transacciones, índices, orden de nulos en otra colación) podría separarlos. La batería de contrato debe correr contra ambos.",
        note_kind="coral", foot=SINT)


def se367_interaccion() -> Fig:
    return grouped_bars(
        "Tres estilos de prueba frente a tres refactorizaciones neutras y un defecto real del servicio",
        "Barras agrupadas: ante tres refactorizaciones que no cambian lo que el servicio hace, la prueba con asertos sobre las llamadas falla dos veces y la que además fija las consultas falla una; la prueba de estado con un doble espía no falla ninguna; las tres detectan el defecto real.",
        ["Mock con asertos de llamadas", "Mock más consultas exactas", "Estado con espía"],
        [("Falsa alarma ante un refactor neutro (de 3)", [2, 1, 0], "coral"), ("Detecta el defecto real (de 1)", [1, 1, 1], "teal")],
        unit="versiones del servicio", decimals=0, ticks=[0, 1, 2, 3],
        note="Dos de tres refactorizaciones rompen la prueba acoplada a la interacción sin que haya un defecto. La prueba de estado comprueba qué se envió y a quién, no cómo. Esto no vuelve inútiles los mocks: verifican que se produzca un efecto cuando el efecto es lo único observable.",
        note_kind="gold", foot=SINT)


def se367_entorno() -> Fig:
    f, y = _kit_start("Los bytes de «é» seguido de un salto de línea en un mismo script según el sistema",
                      "Tres secuencias de bytes: en Windows con la codificación por defecto cp1252 se escribe 233, 13, 10; en Windows con PYTHONUTF8=1 se escribe 195, 169, 13, 10; en Ubuntu bajo WSL2 con UTF-8 se escribe 195, 169, 10. La codificación cambia los bytes de la letra y el sistema cambia el salto de línea.",
                      940, [("Bytes de la letra «é»", "teal", "square"), ("Bytes del salto de línea", "gold", "square")])
    filas = [
        ("Windows 11, por defecto (cp1252)", [("233", "teal"), ("13", "gold"), ("10", "gold")]),
        ("Windows 11 con PYTHONUTF8=1", [("195", "teal"), ("169", "teal"), ("13", "gold"), ("10", "gold")]),
        ("Ubuntu en WSL2 (UTF-8)", [("195", "teal"), ("169", "teal"), ("10", "gold")]),
    ]
    row_h = 64
    for i, (nombre, bytes_) in enumerate(filas):
        ry = y + 8 + i * row_h
        f.text(14, ry + 36, nombre, 14, "start", 700, "#142231")
        for j, (v, k) in enumerate(bytes_):
            f.box(330 + j * 96, ry + 8, 84, 46, v, k, 16, bold=True)
    yy = y + 8 + len(filas) * row_h + 4
    return _kit_finish(f, yy,
                       "Una prueba que depende del orden de un conjunto es inestable en cualquier sistema (11 de 12 semillas de hash dan resultados distintos en ambos) y se arregla ordenando. Una que depende de la codificación o del salto de línea cambia de resultado entre sistemas y se arregla declarándolos. Forzar UTF-8 corrige los bytes de la letra y no el salto de línea. El separador de rutas también difiere (\\ y /); el orden alfabético con mayúsculas y «ñ» es igual. Esta es la única figura de la parte cuyos valores difieren por sistema.",
                       "teal", SINT)


# ---------------------------------------------------------------- SE-368
def se368_fixtures() -> Fig:
    return grouped_bars(
        "Doce pruebas en 500 órdenes aleatorios según cómo se prepara la base",
        "Barras horizontales con las órdenes que tienen algún fallo de 500: con la base compartida fallan 490 órdenes; con una base nueva por prueba (72 sentencias de preparación) o con una transacción con retroceso (24 sentencias) no falla ninguna.",
        ["Estado compartido (0 sentencias)", "Base nueva por prueba (72 sentencias)", "Transacción con retroceso (24 sentencias)"],
        [("Órdenes con algún fallo", [490.0, 0.0, 0.0], "coral")],
        unit="órdenes con algún fallo (de 500)", horizontal=True, label_w=330, decimals=0, ticks=[0, 100, 200, 300, 400, 500],
        note="Las doce pruebas incluyen cinco que cambian o cuentan filas compartidas, a propósito. El orden en que se definieron tampoco pasa con la base compartida (234 resultados distintos). La transacción cuesta un tercio de recrear la base, pero solo aísla lo que ocurre dentro de ella: no cubre cambios que hagan commit por su cuenta ni estado fuera de la base.",
        note_kind="coral", foot=SINT)


def se368_semilla() -> Fig:
    return grouped_bars(
        "Una propiedad con datos aleatorios que falla una de cada diez veces",
        "Barras horizontales en escala logarítmica: la propiedad falla con 0,48 por ciento de las entregas individuales y con 10,9 por ciento de las pruebas de 20 entregas; con la semilla 6 anotada falla 100 por ciento de las repeticiones y sin semilla fija entre 8,7 y 10,1 por ciento de las corridas, sin poder reproducirse.",
        ["Una entrega individual", "Prueba con 20 entregas (1 000 semillas)", "Semilla 6 anotada (100 repeticiones)", "Sin semilla fija: corrida con menos fallos (87 de 1 000)", "Sin semilla fija: corrida con más fallos (101 de 1 000)"],
        [("Fallos de la propiedad", [0.48, 10.9, 100.0, 8.7, 10.1], "coral")],
        unit="% de ejecuciones que violan la propiedad", horizontal=True, log=True, label_w=340, ticks=[0.1, 1, 10, 100],
        value_fmt=lambda v: {0.48: "0,48 %", 10.9: "10,9 %", 100.0: "100 %", 8.7: "8,7 %", 10.1: "10,1 %"}[v],
        note="Una probabilidad pequeña por elemento no se queda pequeña en la prueba: con 20 elementos la prueba falla 23 veces más a menudo (10,9 % frente a 0,48 %). Anotar la semilla en el informe convierte un fallo que nadie puede repetir en uno que se repite siempre. La cifra sin semilla varía entre ejecuciones y entre sistemas.",
        note_kind="gold", foot=SINT)


def se368_fuentes() -> Fig:
    items = [
        ("Reloj (hora actual)", 30.0, "coral", "30 de 30 distintas"),
        ("Identificador aleatorio (uuid4)", 30.0, "coral", "30 de 30"),
        ("Número aleatorio sin semilla", 30.0, "coral", "30 de 30"),
        ("Orden de un conjunto de cadenas", 18.0, "gold", "15 a 18 según la ejecución"),
        ("Suma de flotantes en orden mezclado", 3.0, "gold", "1 a 3 de 30"),
        ("Identidad de un objeto (id)", 2.0, "gold", "2 de 30"),
        ("Datos fijos ordenados · listado de un directorio", 1.0, "teal", "1 (ambos sistemas)"),
    ]
    return bars("Salidas distintas de un mismo generador de informe en 30 procesos, según la fuente de no determinismo activada",
                "Barras: el reloj, el identificador aleatorio y el número aleatorio producen 30 salidas distintas en 30 procesos; el orden de un conjunto produce entre 15 y 18; la suma de flotantes en orden mezclado entre 1 y 3; la identidad de un objeto 2; los datos fijos ordenados y el listado de un directorio de tres archivos 1.",
                items, 11.0, "Las fuentes se inyectan o se fijan una por una: el reloj y el azar se reciben como parámetros, los conjuntos se ordenan, las sumas de flotantes se hacen en orden fijo. Un listado de directorio dio una sola salida en ambos sistemas con tres archivos pequeños, pero su orden no está garantizado por el sistema de archivos.",
                label_w=400, width=980, note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-369
def se369_curva() -> Fig:
    ns = [30, 60, 120, 240, 480]
    return line_chart(
        "Defectos hallados de 12 plantados por tres agentes simulados, media de 300 semillas",
        "Tres líneas: el guion fijo del camino feliz se queda en 0 defectos en todas las longitudes; la exploración aleatoria sube de 1,1 con 30 acciones a 5,3 con 480; la heurística con valores límite, repetición y deshacer sube de 2,6 a 11,6.",
        [("Guion fijo", list(zip(ns, [0.0] * 5)), "grey"), ("Aleatorio uniforme", [(30, 1.1, "1,1", "r")] + list(zip(ns[1:], [2.5, 3.9, 4.8, 5.3])), "gold"),
         ("Heurístico (límites, repetir, deshacer)", list(zip(ns, [2.6, 4.9, 7.9, 10.4, 11.6])), "teal")],
        x_label="Acciones ejecutadas", y_label="Defectos hallados (de 12)", log_x=True, x_ticks=[(n, str(n)) for n in ns], decimals=1, point_labels="all",
        hlines=[(12, "12 plantados")],
        note="Los agentes son programas, no personas: el gráfico muestra el mecanismo de la diversidad de acciones, no el rendimiento de quien explora. El agente heurístico usa los límites que la especificación del formulario declara (10 MB, 500 caracteres), y el diseño de los doce defectos fue del autor, de modo que hay circularidad que el texto declara.",
        note_kind="gold", foot=SINT)


def se369_accesibilidad() -> Fig:
    clases = [("Imagen sin texto alternativo", 31, 0), ("Campo sin etiqueta", 37, 0), ("Contraste menor de 4,5:1", 32, 0), ("Salto de nivel de encabezado", 44, 0),
              ("Enlace «clic aquí»", 37, 0), ("Idioma ausente", 42, 0), ("Texto alternativo que describe otra cosa", 0, 39), ("Trampa de teclado", 0, 35),
              ("Orden de lectura ilógico", 0, 45), ("Mensaje de error ambiguo", 0, 32)]
    return stacked_bars(
        "374 defectos de accesibilidad plantados en 30 páginas sintéticas: quién puede decidirlos",
        "Barras apiladas horizontales de diez clases de defecto: las seis primeras las decide una regla automática y suman 223 de los 374 defectos (59,6 por ciento); las cuatro últimas necesitan a una persona y suman 151.",
        [c[0] for c in clases],
        [("Decide una regla (6 clases, 223)", [c[1] for c in clases], "teal"), ("Decide una persona (4 clases, 151)", [c[2] for c in clases], "coral")],
        unit="defectos plantados", horizontal=True, label_w=300, decimals=0,
        note="El 59,6 % depende de las clases que el autor eligió y de cuántas plantó de cada una, no es una tasa de la web real. El hecho que se conserva es cuáles clases son decidibles por una regla (un contraste se calcula con la fórmula de WCAG) y cuáles exigen juicio (si un texto alternativo describe la imagen).",
        note_kind="teal", foot=SINT)


def se369_sondas() -> Fig:
    return grouped_bars(
        "Seis validadores de un nombre de curso, cada uno con un defecto: sondas dirigidas frente a cadenas aleatorias",
        "Barras horizontales: las quince sondas dirigidas detectan el defecto de los seis validadores; quince cadenas aleatorias lo detectan en 2,0 por ciento de las semillas para el que no recorta espacios, 11,0 por ciento para el límite exclusivo y 0 por ciento para los otros cuatro.",
        ["No recorta espacios", "Límite de 80 exclusivo", "Acepta caracteres de control", "Cuenta bytes en vez de caracteres", "Rechaza caracteres chinos", "Bloquea nombres que empiezan por «admin»"],
        [("15 sondas dirigidas", [100.0] * 6, "teal"), ("15 cadenas aleatorias (200 semillas)", [2.0, 11.0, 0.0, 0.0, 0.0, 0.0], "coral")],
        unit="% de semillas que detectan el defecto (las sondas son deterministas)", horizontal=True, label_w=290, decimals=1, ticks=[0, 25, 50, 75, 100],
        note="Las sondas son una lista de criterios (vacío, solo espacios, límites 79/80/81, tildes, control, bidireccional, emoji). Se escribieron conociendo qué defectos suelen existir: una lista incompleta deja pasar los que no anticipa. No sustituyen la exploración, la preparan.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-370
def se370_suite() -> Fig:
    ns = [50, 200, 1000, 5000]

    def serie(vals, sides):
        return [(n, v, " " if s == "-" else fmt_es(v, 1), "b" if s == "-" else s) for n, v, s in zip(ns, vals, sides)]

    return line_chart(
        "Corridas de la suite que pasan limpias según su tamaño y la inestabilidad de cada prueba: (1 − p)^N",
        "Cuatro curvas decrecientes con el tamaño de la suite en escala logarítmica: con 0,1 por ciento de inestabilidad por prueba, una suite de 1 000 pruebas pasa limpia 36,8 por ciento de las veces y una de 5 000 solo 0,7 por ciento; con 0,5 por ciento una de 200 pasa 36,7 por ciento.",
        [("0,01 % por prueba", serie([99.5, 98.0, 90.5, 60.7], "tttt"), "teal"), ("0,1 % por prueba", serie([95.1, 81.9, 36.8, 0.7], "bbtt"), "navy"),
         ("0,5 % por prueba", serie([77.8, 36.7, 0.7, 0.0], "rrrl"), "gold"), ("1 % por prueba", serie([60.5, 13.4, 0.0, 0.0], "rrt-"), "coral")],
        x_label="Pruebas en la suite", y_label="Corridas limpias (%)", log_x=True, x_ticks=[(n, str(n)) for n in ns], decimals=1, point_labels="all",
        note="Un reintento automático lo arregla en apariencia: con una inestabilidad del 2 % y un reintento, la prueba termina en verde el 99,96 % de las veces, pero un defecto real que falla el 30 % de las ejecuciones también termina en verde el 91,2 % con un reintento y el 97,3 % con dos. Reintentar oculta el problema que ahora no se ve.",
        note_kind="coral", foot=SINT)


def se370_carrera() -> Fig:
    return stacked_bars(
        "La misma condición de carrera: resultados incorrectos según la enumeración exacta y según los hilos reales",
        "Barras horizontales con el porcentaje de resultados incorrectos: la enumeración exacta da 66,7 por ciento con dos hilos y 93,3 por ciento con tres; los hilos reales de CPython 3.12 no fallan en 100 ejecuciones sin código entre la lectura y la escritura ni en 300 con pocas vueltas, y fallan en las 40 con 200 000 vueltas y un bucle vacío entre ambas.",
        ["Enumeración exacta, 2 hilos", "Enumeración exacta, 3 hilos", "Hilos reales, sin nada entre leer y escribir (100 ejecuciones)",
         "Hilos reales, bucle vacío, 1 a 1 000 vueltas (300 ejecuciones)", "Hilos reales, bucle vacío, 200 000 vueltas (40 ejecuciones)"],
        [("Cálculo de intercalaciones (4 de 6 y 84 de 90)", [66.7, 93.3, 0.0, 0.0, 0.0], "gold"), ("Ejecuciones con hilos reales (Windows y Ubuntu)", [0.0, 0.0, 0.0, 0.0, 100.0], "coral")],
        unit="% de resultados incorrectos", horizontal=True, label_w=380, decimals=1,
        note="Ejecutar cien veces y ver verde no prueba que no haya carrera: el intérprete solo cambia de hilo en ciertos puntos y una línea más de código, un tamaño mayor o otra versión de Python mueve el resultado de 0 % a 100 %. La enumeración exacta no depende del planificador; los hilos reales sí.",
        note_kind="teal", foot=SINT)


def se370_diagnostico() -> Fig:
    causas = ["Estable (0,2 % de ruido)", "Rota (falla 98 %)", "Falla con carga alta", "Falla tras otra prueba", "Azar puro (8 %)", "Carga y orden a la vez"]
    return stacked_bars(
        "Clasificar la causa con un historial de 300 ejecuciones: 440 pruebas sintéticas con causa plantada",
        "Barras apiladas horizontales: de 440 pruebas con causa conocida, el clasificador por correlaciones acierta 412 (93,6 por ciento); los errores se concentran en la causa mixta, donde confunde 16 de 40 pruebas con una causa de orden, y en las pruebas que fallan tras otra prueba, con 8 errores.",
        causas,
        [("Bien clasificadas", [199, 40, 57, 42, 50, 24], "teal"), ("Mal clasificadas", [1, 0, 3, 8, 0, 16], "coral")],
        unit="pruebas sintéticas", horizontal=True, label_w=230, decimals=0,
        note="Con solo 30 ejecuciones el historial no basta (70,9 %); con 100, 85,0 %; con 300, 93,6 %. Las reglas se ajustaron con estos mismos casos, de modo que la exactitud real es desconocida. El hecho que se conserva: la carga y el orden se confunden cuando están correlacionados, y solo un experimento que varíe uno de ellos los separa.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-371
def se371_matriz() -> Fig:
    pruebas = ["t01 resultado completo", "t02 solo ejecuta", "t03 «no es None»", "t04 compara algo consigo mismo", "t05 rechaza 7,1", "t06 texto exacto del error",
               "t07 orden de las claves", "t08 bordes de la nota", "t09 línea con 3 campos", "t10 id y estado inválidos", "t11 promedio simple",
               "t12 promedio sin anuladas", "t13 promedio vacío", "t14 sin nota y con espacios"]
    muertos = [8, 6, 6, 6, 5, 10, 6, 13, 0, 1, 3, 3, 1, 8]
    veredicto = ["util", "excepcion", "excepcion", "excepcion", "util", "fragil", "fragil", "util", "debil", "debil", "util", "util", "debil", "util"]
    def serie(clave: str) -> list[float]:
        return [float(m) if v == clave else 0.0 for m, v in zip(muertos, veredicto)]
    return stacked_bars(
        "Catorce pruebas sobre el mismo módulo: mutantes que matan (de 18) según su veredicto",
        "Barras apiladas horizontales con los mutantes que mata cada una de catorce pruebas: la de bordes mata 13, tres pruebas sin aserciones útiles matan 6 cada una solo por excepción, dos pruebas (texto del error y orden de las claves) son frágiles ante refactorizaciones benignas y t09 no mata ninguno.",
        pruebas,
        [("Útil o la más fuerte", serie("util"), "teal"), ("Mata solo por excepción", serie("excepcion"), "gold"), ("Frágil ante un refactor benigno", serie("fragil"), "coral"), ("Débil o pasa por la razón equivocada", serie("debil"), "grey")],
        unit="mutantes muertos (de 18)", horizontal=True, label_w=250, decimals=0, width=980,
        note="Tres pruebas con poder de detección aparente (t02, t03, t04) matan solo porque el mutante hace lanzar una excepción: ninguna comprueba un valor. t09 pasa con el defecto porque el desempaquetado de una línea corta ya lanza ValueError. Una prueba que mata mutantes sin comprobar nada no demuestra lo que dice.",
        note_kind="coral", foot=SINT)


def se371_minimo() -> Fig:
    return grouped_bars(
        "Qué indicador barato se parece más a los mutantes muertos: correlación de rangos de Spearman con 14 pruebas",
        "Barras horizontales: la correlación de rangos entre el número de aserciones y los mutantes muertos es 0,45 y entre las líneas ejecutadas y los mutantes muertos es 0,87, con catorce pruebas; tres de las catorce matan los mismos 17 mutantes que la suite entera.",
        ["Aserciones frente a mutantes muertos", "Líneas ejecutadas frente a mutantes muertos"],
        [("Correlación de Spearman (n = 14)", [0.45, 0.87], "teal")],
        unit="coeficiente de correlación de rangos (0 = ninguna, 1 = perfecta)", horizontal=True, label_w=280, decimals=2, ticks=[0, 0.25, 0.5, 0.75, 1],
        note="Tres de las 14 pruebas (t08, t11 y t12, por un conjunto voraz) matan los mismos 17 mutantes que la suite entera, que mata 17 de 18. Las otras once no son basura: documentan, protegen contra otras regresiones y fallan con mensajes más claros. Con n = 14 las correlaciones son una orientación y no una regla.",
        note_kind="teal", foot=SINT)


def se371_validador() -> Fig:
    return grouped_bars(
        "200 mutaciones de un paquete de evidencia: cuántas detecta el validador al sumar cada nivel",
        "Barras horizontales acumuladas: el nivel de estructura detecta 77 de 200 mutaciones; con referencias, 139; con re-ejecución de las pruebas contra el defecto, 153; con refactorizaciones benignas, 173; con reglas sobre las aserciones, 200.",
        ["Estructura", "+ Referencias", "+ Re-ejecución", "+ Refactor benigno", "+ Reglas de aserción"],
        [("Mutaciones detectadas (acumulado)", [77.0, 139.0, 153.0, 173.0, 200.0], "teal")],
        unit="mutaciones detectadas de 200", horizontal=True, label_w=200, decimals=0, ticks=[0, 50, 100, 150, 200],
        note="Cada nivel atrapa lo que el anterior dejó pasar: faltaban campos y afirmaciones negativas (estructura), pruebas y defectos inventados (referencias), pruebas que no detectan el defecto (re-ejecución), pruebas frágiles (refactor) y pruebas sin aserciones o tautológicas (reglas de aserción). El 100 % final es engañoso: las reglas se diseñaron con las nueve mutaciones que se evalúan. Un paquete con una trampa nueva podría pasar los cinco niveles.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-372
def se372_trimestre() -> Fig:
    return grouped_bars(
        "2 000 trimestres simulados con 40 horas de pruebas y 240 cambios por trimestre",
        "Barras horizontales con la pérdida media del trimestre y su percentil 95 para seis estrategias: sin pruebas 42,41 y 62,00; con reparto uniforme 24,09 y 39,30; el marginal con exposición baja a 21,37 y 35,10.",
        ["Sin pruebas", "Reparto uniforme", "Proporcional al tamaño", "Proporcional a probabilidad × impacto", "Por exposición (× cambios)", "Marginal con exposición"],
        [("Pérdida media", [42.41, 24.09, 24.17, 22.78, 21.75, 21.37], "teal"), ("Percentil 95", [62.0, 39.3, 39.0, 37.2, 35.6, 35.1], "coral")],
        unit="pérdida del trimestre (unidades del modelo; menos es mejor)", horizontal=True, label_w=270, decimals=2,
        note="Pasar de un reparto uniforme al marginal con exposición baja la pérdida media 11 % y el percentil 95 el 11 %; es una mejora real y modesta. La mayor parte del beneficio (42,41 a 24,09) llega con tener pruebas. Los escapes medios (15,69 sin pruebas y entre 7,9 y 8,7 con ellas) están en la tabla. Los cambios se reparten por tamaño del código y la probabilidad por cambio es p/4: ambos supuestos del autor.",
        note_kind="teal", foot=SINT)


def se372_incidente() -> Fig:
    f, y = _kit_start("Reasignar el presupuesto tras un incidente en plazos y zonas horarias",
                      "Flujo de cuatro pasos: el incidente multiplica por tres la probabilidad de defecto de plazos y zonas horarias y por la mitad la de notificaciones; 2,3 horas salen de notificaciones y 3,7 llegan a plazos; la pérdida esperada baja de 0,706 a 0,678 y la media simulada de 22,59 a 21,73; tres componentes quedan bajo 2 horas.",
                      940, None)
    top = y + 6
    w, h, gap = 200, 150, 44
    pasos = [
        ("Incidente en plazos y zonas horarias", "Probabilidad de defecto de plazos ×3 y de notificaciones ×0,5", "coral"),
        ("Reasignar las horas", "Notificaciones: de 2,3 h a 0,0 h. Plazos y zonas horarias: de 4,7 h a 8,4 h", "gold"),
        ("Pérdida esperada", "Del modelo: de 0,706 a 0,678 (−4 %). Media simulada: de 22,59 a 21,73 (−3,8 %)", "teal"),
        ("Bajo 2 horas", "Autenticación 0,7 h, búsqueda 0,6 h, administración 1,1 h: se declaran y caducan", "navy"),
    ]
    for i, (cab, cuerpo, kind) in enumerate(pasos):
        x = 10 + i * (w + gap)
        f.box(x, top, w, 40, cab, kind, 13, bold=True)
        f.box(x, top + 46, w, h - 46, cuerpo, "plain", 13)
        if i < 3:
            f.arrow([(x + w, top + 20), (x + w + gap, top + 20)])
    return _kit_finish(f, top + h + 10,
                       "Reasignar tras un incidente mejora poco (3,8 %) porque el plan anterior ya era razonable; lo que cambia es que ahora está justificado con el incidente. Tres componentes quedan bajo 2 horas: el paquete los declara como exclusiones con una razón y una fecha de caducidad, no los deja olvidados.",
                       "gold", SINT)


def se372_validador() -> Fig:
    return stacked_bars(
        "Validador del paquete de estrategia: en qué nivel se detecta cada una de las 200 mutaciones",
        "Una barra apilada de 200 mutaciones: 60 las detecta la estructura, 64 la coherencia de riesgo, 29 el presupuesto y 33 la trazabilidad, 186 en total; las 14 restantes son 13 cambios de redacción inocuos y una mutación de nivel equivalente, que no deben detectarse.",
        ["200 mutaciones del paquete"],
        [("Estructura (60)", [60], "teal"), ("Coherencia (64)", [64], "navy"), ("Presupuesto (29)", [29], "gold"), ("Trazabilidad (33)", [33], "grey"), ("No detectadas (14)", [14], "coral")],
        unit="mutaciones", horizontal=True, label_w=190, decimals=0,
        note="De 187 mutaciones que cambian el contenido se detectan 186: la que falta es un cambio de nivel que cae en otro nivel igualmente válido, es decir, no cambia nada. Las 13 mutaciones inocuas de redacción no deben detectarse. Las reglas se ajustaron con los mismos tipos que se miden; un paquete incorrecto de un tipo no contemplado puede pasar.",
        note_kind="teal", foot=SINT)


FIGURES = {
    "se-367-fidelidad-de-los-dobles.svg": se367_fidelidad,
    "se-367-pruebas-acopladas-a-la-interaccion.svg": se367_interaccion,
    "se-367-diferencias-de-entorno.svg": se367_entorno,
    "se-368-fixtures-y-orden-de-ejecucion.svg": se368_fixtures,
    "se-368-datos-aleatorios-con-semilla.svg": se368_semilla,
    "se-368-fuentes-de-no-determinismo.svg": se368_fuentes,
    "se-369-defectos-hallados-por-exploracion.svg": se369_curva,
    "se-369-accesibilidad-que-una-regla-decide.svg": se369_accesibilidad,
    "se-369-sondas-de-entrada.svg": se369_sondas,
    "se-370-suite-limpia-segun-su-tamano.svg": se370_suite,
    "se-370-carrera-enumerada-y-real.svg": se370_carrera,
    "se-370-clasificar-la-causa.svg": se370_diagnostico,
    "se-371-poder-de-deteccion-de-catorce-pruebas.svg": se371_matriz,
    "se-371-conjunto-minimo-e-indicadores.svg": se371_minimo,
    "se-371-validador-de-evidencia.svg": se371_validador,
    "se-372-un-trimestre-simulado.svg": se372_trimestre,
    "se-372-reasignar-tras-un-incidente.svg": se372_incidente,
    "se-372-validador-de-la-estrategia.svg": se372_validador,
}
