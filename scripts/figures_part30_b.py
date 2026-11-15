"""Figures for SE-367 to SE-372 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos y modelos del autor con semilla fija; Windows (CPython 3.12.9) y Ubuntu (WSL2, 3.12.3) con cifras idénticas salvo donde se indica."


# ---------------------------------------------------------------- SE-367
def se367_fidelidad() -> Fig:
    rows = [
        ["SQLite real (referencia)", "8 de 8", "—"],
        ["Diccionario ingenuo", "4 de 8", "Id duplicado, nota fuera de rango, estudiante nulo y correo único sin distinguir mayúsculas"],
        ["Diccionario con las reglas añadidas", "8 de 8", "—"],
    ]
    return tab("Fidelidad de dos dobles de un repositorio medida con las mismas 8 comprobaciones de contrato",
               "Tabla: ocho comprobaciones de comportamiento pasan en SQLite real; un diccionario ingenuo pasa cuatro y no rechaza el identificador duplicado, la nota fuera de rango, el estudiante nulo ni el correo repetido con otra capitalización; un diccionario al que se añadieron esas reglas pasa las ocho.",
               ["Implementación", "Comprobaciones superadas", "Qué no reproduce"], rows, [290, 190, 440], row_h=52, size=12,
               note="El doble ingenuo hace pasar pruebas de servicio que con la base real fallarían. Pasar las ocho comprobaciones demuestra que el doble reproduce esas ocho reglas, no que reproduzca la base: una novena comprobación (transacciones, índices, orden de nulos en otra colación) podría separarlos. La batería de contrato debe correr contra ambos.",
               note_kind="coral", foot=SINT)


def se367_interaccion() -> Fig:
    rows = [
        ["Original", "Pasa", "Pasa", "Pasa"],
        ["Refactor: procesa en orden inverso", "Falla", "Falla", "Pasa"],
        ["Refactor: argumentos con nombre", "Falla", "Pasa", "Pasa"],
        ["Refactor: consulta antes de enviar", "Pasa", "Pasa", "Pasa"],
        ["Defecto: avisa también a quien ya tiene nota", "Falla", "Falla", "Falla"],
    ]
    return tab("Cinco versiones del servicio frente a tres estilos de prueba",
               "Tabla: ante tres refactorizaciones que no cambian lo que el servicio hace, la prueba con asertos sobre las llamadas falla en dos y la que además fija las consultas al repositorio falla en una; la prueba de estado con un doble espía no falla en ninguna; las tres detectan el defecto real.",
               ["Versión del servicio", "Mock con asertos de llamadas", "Mock más consultas exactas", "Estado con espía"], rows, [370, 190, 190, 170], row_h=44, size=12,
               note="Dos de tres refactorizaciones rompen la prueba acoplada a la interacción sin que haya un defecto. La prueba de estado comprueba qué se envió y a quién, no cómo. Esto no vuelve inútiles los mocks: verifican que se produzca un efecto cuando el efecto es lo único observable.",
               note_kind="gold", foot=SINT)


def se367_entorno() -> Fig:
    rows = [
        ["Orden de un conjunto de cadenas (12 semillas de hash)", "11 resultados distintos", "11 resultados distintos"],
        ["Separador de rutas", "\\", "/"],
        ["Codificación por defecto al abrir un archivo", "cp1252", "UTF-8"],
        ["Bytes de «é» seguido de salto de línea", "233, 13, 10", "195, 169, 10"],
        ["Con PYTHONUTF8=1", "195, 169, 13, 10", "195, 169, 10"],
        ["Orden alfabético con mayúsculas y «ñ»", "Igual", "Igual"],
    ]
    return tab("Un mismo script en 12 procesos: qué cambia con la semilla de hash y con el sistema",
               "Tabla: el orden de un conjunto de cadenas cambia con la semilla de hash en 11 de 12 procesos en ambos sistemas; el separador de rutas, la codificación por defecto y los bytes de un archivo de texto difieren entre Windows y Ubuntu; forzar UTF-8 corrige la codificación y no el salto de línea.",
               ["Comportamiento", "Windows 11 (3.12.9)", "Ubuntu en WSL2 (3.12.3)"], rows, [430, 230, 230], row_h=44, size=12,
               note="Una prueba que depende del orden de un conjunto es inestable en cualquier sistema y se arregla ordenando. Una que depende de la codificación o del salto de línea cambia de resultado entre sistemas y se arregla declarándolos. Esta figura es la única de la parte cuyos valores difieren por sistema.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-368
def se368_fixtures() -> Fig:
    rows = [
        ["Estado compartido", "490 de 500", "234", "0"],
        ["Base nueva por prueba", "0 de 500", "1", "72"],
        ["Transacción con retroceso", "0 de 500", "1", "24"],
    ]
    return tab("Doce pruebas en 500 órdenes aleatorias según cómo se prepara la base",
               "Tabla: con una base compartida, 490 de 500 órdenes aleatorias de doce pruebas tienen algún fallo y producen 234 combinaciones distintas de resultados; con una base nueva por prueba o una transacción con retroceso ningún orden falla; preparar una base nueva cuesta 72 sentencias por corrida y la transacción 24.",
               ["Estrategia de fixture", "Órdenes con algún fallo", "Resultados distintos", "Sentencias de preparación"], rows, [310, 220, 190, 200], row_h=44, size=13,
               note="Las doce pruebas incluyen cinco que cambian o cuentan filas compartidas, a propósito. El orden en que se definieron tampoco pasa con la base compartida. La transacción cuesta un tercio de recrear la base, pero solo aísla lo que ocurre dentro de ella: no cubre cambios que hagan commit por su cuenta ni estado fuera de la base.",
               note_kind="coral", foot=SINT)


def se368_semilla() -> Fig:
    rows = [
        ["Entregas individuales que violan la propiedad", "0,48 %", "Efecto del redondeo con nota bruta 1,0"],
        ["Pruebas con 20 entregas aleatorias que fallan, 1 000 semillas", "109 de 1 000 (10,9 %)", "20 entregas multiplican el riesgo"],
        ["Semilla 6 anotada, 100 repeticiones", "Falla 100 de 100", "Reproducible"],
        ["Sin semilla fija, 1 000 corridas independientes", "Falla 73 a 101 de 1 000", "No reproducible; el valor cambia en cada corrida"],
    ]
    return tab("Una propiedad con datos aleatorios que falla una de cada diez veces",
               "Tabla: una propiedad que falla con el 0,48 por ciento de las entregas individuales falla con 10,9 por ciento de las pruebas de 20 entregas; con la semilla 6 anotada reproduce el fallo 100 de 100 veces; sin semilla fija falla entre 73 y 101 de 1 000 corridas y no puede reproducirse.",
               ["Medida", "Resultado", "Lectura"], rows, [400, 230, 280], row_h=52, size=12,
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
    rows = [
        ["30", "0,0", "1,1", "2,6"],
        ["60", "0,0", "2,5", "4,9"],
        ["120", "0,0", "3,9", "7,9"],
        ["240", "0,0", "4,8", "10,4"],
        ["480", "0,0", "5,3", "11,6"],
    ]
    return tab("Defectos hallados de 12 plantados por tres agentes simulados, media de 300 semillas",
               "Tabla: un guion fijo del camino feliz no halla ningún defecto de los doce en ninguna longitud; la exploración aleatoria halla 1,1 con 30 acciones y 5,3 con 480; la heurística con valores límite, repetición y deshacer halla 2,6 con 30 y 11,6 con 480.",
               ["Acciones", "Guion fijo", "Aleatorio uniforme", "Heurístico (límites, repetir, deshacer)"], rows, [150, 190, 230, 320], row_h=44, size=13,
               note="Los agentes son programas, no personas: la tabla muestra el mecanismo de la diversidad de acciones, no el rendimiento de quien explora. El agente heurístico usa los límites que la especificación del formulario declara (10 MB, 500 caracteres), y el diseño de los doce defectos fue del autor, de modo que hay circularidad que el texto declara.",
               note_kind="gold", foot=SINT)


def se369_accesibilidad() -> Fig:
    rows = [
        ["Imagen sin texto alternativo", "31", "Regla"],
        ["Campo sin etiqueta", "37", "Regla"],
        ["Contraste menor de 4,5:1", "32", "Regla"],
        ["Salto de nivel de encabezado", "44", "Regla"],
        ["Enlace «clic aquí»", "37", "Regla"],
        ["Idioma ausente", "42", "Regla"],
        ["Texto alternativo que describe otra cosa", "39", "Persona"],
        ["Trampa de teclado", "35", "Persona"],
        ["Orden de lectura ilógico", "45", "Persona"],
        ["Mensaje de error ambiguo", "32", "Persona"],
    ]
    return tab("374 defectos de accesibilidad plantados en 30 páginas sintéticas: quién puede decidirlos",
               "Tabla: de diez clases de defecto plantadas, seis las puede decidir una regla automática, con 223 de los 374 defectos (59,6 por ciento), y cuatro necesitan a una persona, con 151 defectos.",
               ["Clase de defecto", "Plantados", "Quién decide"], rows, [450, 150, 190], row_h=34, size=12,
               note="El 59,6 % depende de las clases que el autor eligió y de cuántas plantó de cada una, no es una tasa de la web real. El hecho que se conserva es cuáles clases son decidibles por una regla (un contraste se calcula con la fórmula de WCAG) y cuáles exigen juicio (si un texto alternativo describe la imagen).",
               note_kind="teal", foot=SINT)


def se369_sondas() -> Fig:
    rows = [
        ["No recorta espacios", "Detecta (1 sonda)", "2,0 %"],
        ["Límite de 80 exclusivo", "Detecta (2 sondas)", "11,0 %"],
        ["Acepta caracteres de control", "Detecta (3 sondas)", "0,0 %"],
        ["Cuenta bytes en vez de caracteres", "Detecta (2 sondas)", "0,0 %"],
        ["Rechaza caracteres chinos", "Detecta (2 sondas)", "0,0 %"],
        ["Bloquea nombres que empiezan por «admin»", "Detecta (1 sonda)", "0,0 %"],
    ]
    return tab("Seis validadores de un nombre de curso, cada uno con un defecto: 15 sondas dirigidas frente a 15 cadenas aleatorias",
               "Tabla: las quince sondas dirigidas detectan el defecto de los seis validadores; quince cadenas aleatorias lo detectan en 2,0 por ciento de las semillas para el que no recorta espacios, 11,0 por ciento para el límite exclusivo y 0 por ciento para los otros cuatro.",
               ["Defecto del validador", "Sondas dirigidas", "Cadenas aleatorias (200 semillas)"], rows, [380, 220, 290], row_h=44, size=12,
               note="Las sondas son una lista de criterios (vacío, solo espacios, límites 79/80/81, tildes, control, bidireccional, emoji). Se escribieron conociendo qué defectos suelen existir: una lista incompleta deja pasar los que no anticipa. No sustituyen la exploración, la preparan.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-370
def se370_suite() -> Fig:
    rows = [
        ["0,01 %", "99,5", "98,0", "90,5", "60,7"],
        ["0,1 %", "95,1", "81,9", "36,8", "0,7"],
        ["0,5 %", "77,8", "36,7", "0,7", "0,0"],
        ["1 %", "60,5", "13,4", "0,0", "0,0"],
    ]
    return tab("Corridas de la suite que pasan limpias según su tamaño y la inestabilidad de cada prueba: (1 − p)^N",
               "Tabla: con una inestabilidad de 0,1 por ciento por prueba, una suite de 1 000 pruebas pasa limpia 36,8 por ciento de las veces y una de 5 000 pasa 0,7 por ciento; con 0,5 por ciento una suite de 200 pasa 36,7 por ciento.",
               ["Fallo espurio por prueba", "50 pruebas", "200 pruebas", "1 000 pruebas", "5 000 pruebas"], rows, [240, 150, 150, 160, 160], row_h=44, size=13,
               note="Un reintento automático lo arregla en apariencia: con una inestabilidad del 2 % y un reintento, la prueba termina en verde el 99,96 % de las veces, pero un defecto real que falla el 30 % de las ejecuciones también termina en verde el 91,2 % con un reintento y el 97,3 % con dos. Reintentar oculta el problema que ahora no se ve.",
               note_kind="coral", foot=SINT)


def se370_carrera() -> Fig:
    rows = [
        ["Enumeración exacta, 2 hilos que leen y escriben", "Termina bien en 2 de 6 intercalaciones (33,3 %)", "Cálculo"],
        ["Enumeración exacta, 3 hilos", "Termina bien en 6 de 90 intercalaciones (6,7 %)", "Cálculo"],
        ["Hilos reales, sin nada entre leer y escribir, hasta 200 000 vueltas", "0 fallos en 100 ejecuciones", "Windows y Ubuntu"],
        ["Hilos reales con un bucle vacío entre leer y escribir, 1 y 1 000 vueltas", "0 fallos en 300 ejecuciones", "Windows y Ubuntu"],
        ["Los mismos con 200 000 vueltas", "Falla en 40 de 40 ejecuciones", "Windows y Ubuntu"],
    ]
    return tab("La misma condición de carrera: lo que dice la enumeración y lo que dicen los hilos reales",
               "Tabla: leer y escribir un contador con dos hilos termina bien en un tercio de las intercalaciones posibles y con tres hilos en 6,7 por ciento; los hilos reales de CPython 3.12 no fallaron en 100 ejecuciones sin código entre la lectura y la escritura ni en 300 con pocas vueltas, y fallaron en las 40 con 200 000 vueltas cuando había un bucle vacío entre ambas.",
               ["Experimento", "Resultado", "Dónde"], rows, [430, 330, 150], row_h=52, size=12,
               note="Ejecutar cien veces y ver verde no prueba que no haya carrera: el intérprete solo cambia de hilo en ciertos puntos y una línea más de código, un tamaño mayor o otra versión de Python mueve el resultado de 0 % a 100 %. La enumeración exacta no depende del planificador; los hilos reales sí.",
               note_kind="teal", foot=SINT)


def se370_diagnostico() -> Fig:
    rows = [
        ["Estable (0,2 % de ruido)", "200", "199", "1 como azar"],
        ["Rota (falla 98 %)", "40", "40", "—"],
        ["Falla con carga alta", "60", "57", "1 azar, 2 mixta"],
        ["Falla tras otra prueba", "50", "42", "8 como mixta"],
        ["Azar puro (8 %)", "50", "50", "—"],
        ["Carga y orden a la vez", "40", "24", "16 como orden"],
    ]
    return tab("Clasificar la causa con un historial de 300 ejecuciones: 440 pruebas sintéticas con causa plantada",
               "Tabla: de 440 pruebas con causa conocida, un clasificador basado en correlaciones acierta 412, 93,6 por ciento; falla más en la causa mixta, donde confunde 16 de 40 con una causa de orden porque la carga y la ejecución previa están correlacionadas; con 30 ejecuciones acierta 70,9 por ciento y con 100 acierta 85,0 por ciento.",
               ["Causa plantada", "Pruebas", "Bien clasificadas", "Errores"], rows, [300, 120, 190, 280], row_h=44, size=13,
               note="Con solo 30 ejecuciones el historial no basta (70,9 %); con 100, 85,0 %; con 300, 93,6 %. Las reglas se ajustaron con estos mismos casos, de modo que la exactitud real es desconocida. El hecho que se conserva: la carga y el orden se confunden cuando están correlacionados, y solo un experimento que varíe uno de ellos los separa.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-371
def se371_matriz() -> Fig:
    rows = [
        ["t01 resultado completo", "8", "No", "Útil"],
        ["t02 solo ejecuta", "6 (todos por excepción)", "No", "Sin aserciones: solo caza caídas"],
        ["t03 «no es None»", "6 (todos por excepción)", "No", "Aserción casi vacía"],
        ["t04 compara algo consigo mismo", "6 (todos por excepción)", "No", "Tautología"],
        ["t05 rechaza 7,1", "5", "No", "Útil"],
        ["t06 texto exacto del error", "10", "Sí (mensajes)", "Frágil"],
        ["t07 orden de las claves", "6", "Sí (claves)", "Frágil"],
        ["t08 bordes de la nota", "13", "No", "La más fuerte"],
        ["t09 línea con 3 campos", "0", "No", "Pasa por la razón equivocada"],
        ["t10 id y estado inválidos", "1", "No", "Débil"],
        ["t11 promedio simple", "3", "No", "Útil"],
        ["t12 promedio sin anuladas", "3", "No", "Útil"],
        ["t13 promedio vacío", "1", "No", "Débil"],
        ["t14 sin nota y con espacios", "8", "No", "Útil"],
    ]
    return tab("Catorce pruebas sobre el mismo módulo: mutantes que matan (de 18) y fallos ante refactorizaciones benignas",
               "Tabla: catorce pruebas con los mutantes que matan de dieciocho, si fallan ante seis refactorizaciones que no cambian el comportamiento y el veredicto; la prueba de bordes mata 13, tres pruebas sin aserciones útiles matan 6 cada una solo por excepción, dos son frágiles y una no mata ninguno.",
               ["Prueba", "Mutantes muertos", "Falla con refactor benigno", "Veredicto"], rows, [260, 220, 180, 270], row_h=30, size=11,
               note="Tres pruebas con poder de detección aparente (t02, t03, t04) matan solo porque el mutante hace lanzar una excepción: ninguna comprueba un valor. t09 pasa con el defecto porque el desempaquetado de una línea corta ya lanza ValueError. Una prueba que mata mutantes sin comprobar nada no demuestra lo que dice.",
               note_kind="coral", foot=SINT)


def se371_minimo() -> Fig:
    rows = [
        ["Pruebas en la suite · mutantes muertos por la unión", "14 · 17 de 18", "—"],
        ["Conjunto mínimo (voraz) que mata los mismos 17", "3 de 14", "t08, t11, t12"],
        ["Correlación de Spearman entre aserciones y mutantes muertos", "0,45", "n = 14"],
        ["Correlación de Spearman entre líneas ejecutadas y mutantes muertos", "0,87", "n = 14"],
    ]
    return tab("Cuántas pruebas hacen falta para matar los mismos mutantes, y qué indicador barato se parece más",
               "Tabla: tres de catorce pruebas matan los mismos 17 mutantes que la suite entera; la correlación de rangos entre el número de aserciones y los mutantes muertos es 0,45 y entre líneas ejecutadas y mutantes muertos es 0,87, con catorce pruebas.",
               ["Medida", "Valor", "Detalle"], rows, [520, 170, 200], row_h=44, size=12,
               note="Las otras once pruebas no son basura: documentan, protegen contra otras regresiones y fallan con mensajes más claros. Que el mínimo sea de tres solo dice que, frente a estos mutantes, el resto no añade detección. Con n = 14 las correlaciones son una orientación y no una regla.",
               note_kind="teal", foot=SINT)


def se371_validador() -> Fig:
    rows = [
        ["Campo faltante (26) o afirmación negativa (22)", "Estructura"],
        ["Menos de 3 ejecuciones (14) · prueba repetida (15)", "Estructura"],
        ["Prueba inventada (22) · defecto inventado (40)", "Referencias"],
        ["La prueba no detecta ese defecto (14)", "Re-ejecución"],
        ["Prueba frágil que sí detecta (20)", "Refactor benigno"],
        ["Prueba sin aserciones o tautológica (27)", "Reglas de aserción"],
    ]
    return tab("200 mutaciones de un paquete de evidencia: en qué nivel del validador se detecta cada tipo",
               "Tabla: el nivel de estructura detecta 77 de 200 mutaciones; con referencias, 139; con re-ejecución de las pruebas contra el defecto, 153; con refactorizaciones benignas, 173; con reglas sobre las aserciones, 200.",
               ["Tipo de mutación del paquete (cantidad)", "Primer nivel que la detecta"], rows, [600, 290], row_h=44, size=13,
               note="Acumulado por nivel: estructura 77 de 200, referencias 139, re-ejecución 153, refactor 173, aserciones 200. El 100 % final es engañoso: las reglas se diseñaron con las nueve mutaciones que se evalúan. Un paquete con una trampa nueva podría pasar los cinco niveles.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-372
def se372_trimestre() -> Fig:
    rows = [
        ["Sin pruebas", "42,41", "62,00", "15,69"],
        ["Reparto uniforme", "24,09", "39,30", "8,25"],
        ["Proporcional al tamaño", "24,17", "39,00", "7,90"],
        ["Proporcional a probabilidad × impacto", "22,78", "37,20", "8,72"],
        ["Por exposición (× cambios)", "21,75", "35,60", "8,00"],
        ["Marginal con exposición", "21,37", "35,10", "8,14"],
    ]
    return tab("2 000 trimestres simulados con 40 horas de pruebas y 240 cambios por trimestre",
               "Tabla: sin pruebas la pérdida media del trimestre simulado es 42,41 y con 40 horas repartidas por igual 24,09; el reparto marginal con exposición baja a 21,37, con el percentil 95 en 35,10 frente a 39,30 del uniforme; los escapes medios bajan de 15,69 a entre 7,9 y 8,7.",
               ["Estrategia", "Pérdida media", "Percentil 95", "Escapes medios"], rows, [390, 160, 160, 180], row_h=44, size=13,
               note="Pasar de un reparto uniforme al marginal con exposición baja la pérdida media 11 % y el percentil 95 el 11 %; es una mejora real y modesta. La mayor parte del beneficio (42,41 a 24,09) llega con tener pruebas. Los cambios se reparten por tamaño del código y la probabilidad por cambio es p/4: ambos supuestos del autor.",
               note_kind="teal", foot=SINT)


def se372_incidente() -> Fig:
    rows = [
        ["Notificaciones", "2,3 h", "0,0 h", "Probabilidad ×0,5 tras el incidente"],
        ["Plazos y zonas horarias", "4,7 h", "8,4 h", "Probabilidad ×3 tras el incidente"],
        ["Pérdida esperada del modelo", "0,706", "0,678", "−4 % al reasignar"],
        ["Pérdida media simulada", "22,59", "21,73", "−3,8 %"],
        ["Bajo 2 h: candidatos a «no probar»", "Autenticación 0,7 h · búsqueda 0,6 h · administración 1,1 h", "", "Declarar y caducar"],
    ]
    return tab("Reasignar el presupuesto tras un incidente en plazos y zonas horarias",
               "Tabla: tras multiplicar por tres la probabilidad de defecto de plazos y zonas horarias y por la mitad la de notificaciones, reasignar las horas mueve 2,3 horas fuera de notificaciones y 3,7 horas hacia plazos y reduce la pérdida esperada de 0,706 a 0,678 y la media simulada de 22,59 a 21,73.",
               ["Qué cambia", "Plan anterior", "Plan reasignado", "Motivo"], rows, [250, 250, 150, 270], row_h=52, size=12,
               note="Reasignar tras un incidente mejora poco (3,8 %) porque el plan anterior ya era razonable; lo que cambia es que ahora está justificado con el incidente. Tres componentes quedan bajo 2 horas: el paquete los declara como exclusiones con una razón y una fecha de caducidad, no los deja olvidados.",
               note_kind="gold", foot=SINT)


def se372_validador() -> Fig:
    rows = [
        ["Campo de un riesgo eliminado (20) · p fuera de rango (19) · límites vacíos (21)", "60", "Estructura"],
        ["Nivel que no ve la clase de fallo (10, de los que 9 cambian algo)", "9", "Coherencia"],
        ["Riesgo alto con 0,5 h (13) · excluir un riesgo alto (11)", "24", "Coherencia"],
        ["Exclusión sin caducidad (19) o a un año (12)", "31", "Coherencia"],
        ["Horas que no suman (11) · sin gate que bloquee (18)", "29", "Presupuesto"],
        ["Componente sin decisión (17) · prueba repetida (16)", "33", "Trazabilidad"],
        ["Cambio de redacción inocuo (13)", "0", "No debe detectarse"],
    ]
    return tab("Validador del paquete de estrategia: 200 mutaciones y nivel en que se detecta cada una",
               "Tabla: el validador detecta 186 de 200 mutaciones; 60 con la estructura, 124 al añadir coherencia de riesgo y 186 al añadir presupuesto y trazabilidad; las 13 mutaciones inocuas de redacción no se detectan y una mutación del nivel resulta equivalente.",
               ["Tipo de mutación (cantidad)", "Detectadas", "Primer nivel"], rows, [560, 130, 200], row_h=52, size=12,
               note="De 187 mutaciones que cambian el contenido se detectan 186: la que falta es un cambio de nivel que cae en otro nivel igualmente válido, es decir, no cambia nada. Las reglas se ajustaron con los mismos tipos que se miden; un paquete incorrecto de un tipo no contemplado puede pasar.",
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
