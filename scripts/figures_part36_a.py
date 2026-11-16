"""Figures for SE-433 to SE-438 (modernization of a legacy grading module: synthetic data with fixed seeds, plus runs of real CPython/SQLite code on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_flow_rows import chain_rows
from figure_kit import Fig, fmt_exact, grouped_bars, line_chart, percentile_intervals, stacked_bars
from figures_part07_a import bars


SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."

# ---------------------------------------------------------------- SE-433
def se433_capacidad_devorada() -> Fig:
    return line_chart(
        "Un equipo de 100 unidades al mes: el trabajo correctivo se come lo demás si no hay reserva preventiva",
        "Líneas con el trabajo correctivo mensual de un equipo de 100 unidades en los meses 1, 12 y 24: sin reserva sube de 19,7 a 33,0 y 59,7 unidades y desplaza al perfectivo, y la deuda pasa de 40,9 a 184,0 y 401,2; con una reserva del 20 por ciento para trabajo preventivo baja de 19,7 a 12,6 y 14,0 y la deuda a cero.",
        [("Sin reserva", [(1, 19.7), (12, 33.0), (24, 59.7)], "coral"), ("Reserva del 20 %", [(1, 19.7), (12, 12.6), (24, 14.0)], "teal")],
        x_label="Mes", y_label="Trabajo correctivo (unidades al mes)", x_ticks=[(1, "1"), (12, "12"), (24, "24")], y_ticks=[0, 20, 40, 60, 80], point_labels="all", decimals=1,
        note="Sin reserva, la carga correctiva pasa de 19,7 a 59,7 unidades y desplaza al perfectivo (de 30,0 a 25,3), y la deuda llega a 401,2; con el 20 % reservado, el correctivo baja a 14,0, se entrega todo lo pedido y la deuda es 0. Los coeficientes de realimentación entre deuda e incidencias son del autor: demuestran un mecanismo, no una magnitud.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-433
def se433_clasificar_es_un_juicio() -> Fig:
    return stacked_bars(
        "600 solicitudes sintéticas: aciertos de un clasificador por palabras clave según sean claras o ambiguas",
        "Barras apiladas horizontales con los aciertos de un clasificador por palabras clave sobre 600 solicitudes sintéticas: acierta las 456 claras y 74 de las 144 ambiguas, 88,3 por ciento en total; dos revisoras simuladas coinciden en el 76,8 por ciento con kappa 0,69, pero solo en el 34 por ciento de las ambiguas.",
        ["Claras (456)", "Ambiguas (144)"],
        [("Acierta el clasificador", [456, 74], "teal"), ("Falla", [0, 70], "coral")],
        unit="Solicitudes", horizontal=True, label_w=160,
        note="El acierto global del 88,3 % (530 de 600) esconde que una cuarta parte de la cartera es ambigua y que ahí el clasificador acierta el 51 % y el acuerdo entre dos revisoras es del 34 % (76,8 % en total, kappa 0,69). Esas solicitudes necesitan una conversación con quien las pidió. La proporción de ambiguas y las tasas de las revisoras son supuestos del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-433
def se433_fecha_impuesta() -> Fig:
    items = [('3 meses', 24.6, 'coral', '24,6 %'), ('4 meses (mediana)', 44.0, 'coral', '44,0 %'), ('6 meses', 71.6, 'gold', '71,6 %'), ('8 meses', 85.3, 'teal', '85,3 %'), ('12 meses', 95.6, 'teal', '95,6 %')]
    return bars('Probabilidad de terminar a tiempo una adaptación obligatoria de mediana cuatro meses, según el margen',
                'Barras con la probabilidad de terminar a tiempo una adaptación obligatoria cuya duración mediana es de cuatro meses según el margen disponible: 24,6 por ciento con tres meses, 44,0 con cuatro, 71,6 con seis, 85,3 con ocho y 95,6 con doce.',
                items, 6.0, 'Empezar con un margen igual a la mediana llega a tiempo menos de la mitad de las veces. La duración (mediana 4 meses, dispersión 0,5, 15 % de dependencias ocultas que la duplican) es un supuesto del autor.',
                label_w=190, width=940, note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-434
def se434_puntos_calientes() -> Fig:
    return grouped_bars(
        "Tres criterios para elegir 30 de 300 archivos en un historial sintético de 4 000 commits",
        "Barras agrupadas con la parte de commits y de correcciones que caen en los 30 archivos elegidos: solo por tamaño, 10,3 y 23,5 por ciento; por frecuencia de cambio, 55,9 y 51,7; por frecuencia por tamaño, 53,3 y 55,6; los criterios coinciden con 11, 19 y 22 de los 30 archivos más corregidos.",
        ["Solo tamaño (coincide con 11 de los 30 más corregidos)", "Solo frecuencia de cambio (19 de 30)", "Frecuencia × tamaño (22 de 30)"],
        [("Commits en los 30 archivos", [10.3, 55.9, 53.3], "gold"), ("Correcciones en los 30 archivos", [23.5, 51.7, 55.6], "teal")],
        unit="% del total", plot_h=250, ticks=[0, 20, 40, 60, 80], value_fmt=lambda v: fmt_exact(v) + " %",
        note="El 10 % de los archivos concentra más de la mitad de los commits y de las correcciones. Ordenar por tamaño apenas supera al azar; el producto captura el 55,6 % de las correcciones. La relación entre tamaño y correcciones es un supuesto del autor.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-434
def se434_conocimiento_que_se_va() -> Fig:
    return line_chart(
        "Archivos huérfanos de 300 con 12 personas y una rotación del 2 % mensual (200 simulaciones)",
        "Líneas con los archivos huérfanos, de 300, tras 12, 36 y 60 meses con una rotación del 2 por ciento mensual entre 12 personas: la mediana sube de 40 a 132 y 194 y el percentil 90 de 90 a 187 y 249.",
        [("Percentil 90", [(12, 90), (36, 187), (60, 249)], "coral"), ("Mediana", [(12, 40), (36, 132), (60, 194)], "teal")],
        x_label="Meses", y_label="Archivos huérfanos (de 300)", x_ticks=[(12, "12"), (36, "36"), (60, "60")], y_ticks=[0, 100, 200, 300], point_labels="all",
        note="Con una rotación del 2 % mensual se van 9 de las 12 personas en cinco años y dos tercios de los archivos (65 % de mediana) quedan sin persona asociada. La rotación, el 35 % de archivos compartidos y la asignación al azar son supuestos del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-434
def se434_codigo_muerto() -> Fig:
    return stacked_bars(
        "Dos técnicas para encontrar código muerto en un módulo de 60 funciones con 20 realmente muertas",
        "Barras apiladas horizontales con los candidatos de cada técnica: el análisis por nombre propone 45, 20 muertas y 25 falsas alarmas; la traza de una ejecución propone 25, 20 muertas y 5 falsas alarmas; la coincidencia de ambas propone exactamente las 20 muertas.",
        ["Análisis por nombre (ast)", "Traza de una ejecución", "Coinciden las dos"],
        [("Muertas halladas", [20, 20, 20], "teal"), ("Falsas alarmas", [25, 5, 0], "coral")],
        unit="Candidatos propuestos", horizontal=True, label_w=200,
        note="Cada técnica se equivoca por una razón distinta: el análisis por nombre falla con 15 llamadas por cadena y 10 funciones registradas, y la traza con una rama poco frecuente. La coincidencia deja cero falsas alarmas solo porque en este módulo ningún uso dinámico estaba en una rama poco frecuente; una llamada por cadena en esa rama habría engañado a las dos.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-435
def se435_cobertura_no_es_detector() -> Fig:
    return grouped_bars(
        "Entradas para caracterizar nota_final: líneas cubiertas (de 18) y mutantes detectados (de 12)",
        "Barras horizontales con el porcentaje de líneas cubiertas, de 18, y de mutantes detectados, de 12, por seis conjuntos de entradas: cinco ejemplos de la documentación 89 y 33 por ciento, 100 entradas aleatorias 89 y 75, 1 000 entradas aleatorias 100 y 100 y 14 casos de borde 94 y 75.",
        ["5 ejemplos de la documentación", "5 entradas aleatorias", "20 entradas aleatorias", "100 entradas aleatorias", "1 000 entradas aleatorias", "14 casos de borde elegidos a mano"],
        [("Líneas cubiertas", [89, 83, 89, 89, 100, 94], "gold"), ("Mutantes detectados", [33, 50, 75, 75, 100, 75], "teal")],
        unit="% del total (16 de 18 líneas = 89 %, 4 de 12 mutantes = 33 %)", horizontal=True, label_w=250, ticks=[0, 25, 50, 75, 100], value_fmt=lambda v: fmt_exact(v) + " %",
        note="La cobertura de líneas no sube entre 20 y 100 entradas y los mutantes tampoco; los casos de borde cubren el 94 % y dejan vivos tres mutantes que mil entradas aleatorias matan. La función y los doce mutantes son del autor y se escribieron sabiendo qué buscaban.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-435
def se435_orden_de_un_conjunto() -> Fig:
    rows = [
        [("Semilla de hash 1", "plain"), ("pedro, marta, sofia, tomas, luis, ana", "gold"), ("Una salida", "coral")],
        [("Semilla de hash 2", "plain"), ("pedro, marta, tomas, ana, sofia, luis", "gold"), ("Otra salida", "coral")],
        [("Semilla de hash 3", "plain"), ("luis, pedro, tomas, sofia, ana, marta", "gold"), ("Otra salida más", "coral")],
        [("Las ocho semillas", "plain"), ("Ocho órdenes del mismo conjunto", "gold"), ("8 salidas distintas", "coral")],
        [("Ordenando antes de escribir", "plain"), ("El mismo orden en los ocho procesos", "teal"), ("1 salida", "teal")],
    ]
    return chain_rows(
        "El mismo programa con seis alumnos en un conjunto, en ocho procesos con semilla de hash distinta",
        "Diagrama de flujo de ocho procesos del mismo programa con seis alumnos en un conjunto: cada semilla de hash da un orden distinto y por tanto una salida distinta, ocho en total; ordenar antes de escribir da una sola salida para los ocho procesos.",
        ["Proceso", "Orden en que el conjunto entrega los nombres", "Salida"], rows, [240, 400, 190],
        note="Un maestro dorado que compare el texto completo falla entre procesos aunque el código sea idéntico. Ordenar elimina la variación solo si el contrato no exige otro orden. El orden de los conjuntos de cadenas depende del intérprete y de su versión.",
        note_kind="coral", foot=EJEC)


# ---------------------------------------------------------------- SE-435
def se435_costura_y_tiempo() -> Fig:
    return grouped_bars(
        "300 pruebas de nota_final con una dependencia de 2 ms y con una costura que la sustituye",
        "Barras agrupadas en escala logarítmica con el tiempo de 300 pruebas de la función de nota final: con una dependencia de 2 milisegundos 771 en Windows y 701 en Ubuntu, y con una costura que la sustituye 0,34 y 0,40, unas 2 200 y 1 800 veces menos.",
        ["Windows 11 (CPython 3.12.9)", "Ubuntu bajo WSL2 (3.12.3)"],
        [("Con la dependencia", [771, 701], "coral"), ("Con costura", [0.34, 0.40], "teal")],
        unit="Tiempo de 300 pruebas (ms)", log=True, ticks=[0.1, 1, 10, 100, 1000], plot_h=250,
        note="La espera de 2 ms es un supuesto y los tiempos de reloj cambian de equipo en equipo; la razón de varios órdenes de magnitud (unas 2 200 veces en Windows y 1 800 en Ubuntu) es la parte estable. La costura no prueba la dependencia real: queda pendiente una prueba de integración.",
        note_kind="gold", foot=REAL)


# ---------------------------------------------------------------- SE-436
def se436_costo_de_esperar() -> Fig:
    return percentile_intervals(
        "Esfuerzo total de actualizar una dependencia con 12 % de versiones incompatibles en 48 versiones (2 000 historias)",
        "Intervalos con la mediana y el percentil 90 del esfuerzo total según la cadencia de actualización: cada versión 12,6 y 18,9 horas, cada 4 versiones 14,4 y 23,0, cada 12 versiones 21,1 y 35,5 y una sola vez a las 48 versiones 71,4 y 134,6.",
        [("Cada versión", [12.6, 18.9]), ("Cada 4 versiones", [14.4, 23.0]), ("Cada 12 versiones", [21.1, 35.5]), ("Una vez a las 48", [71.4, 134.6])],
        unit="Esfuerzo total (horas)", marks=("mediana", "p90"), label_w=170,
        note="El número de cambios incompatibles es el mismo en las cuatro cadencias; lo que cambia es cuántos se juntan en un salto: la mayor actualización cuesta 2,1, 5,5, 12,5 y 71,4 horas de mediana. Actualizar una sola vez cuesta 5,7 veces más que en cada versión. El 12 %, el 15 % de interacción y el 5 % de mezcla de causas son supuestos del autor.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-436
def se436_ventana_de_exposicion() -> Fig:
    return percentile_intervals(
        "Exposición a avisos de seguridad en 40 dependencias y 31 avisos durante un año, según la política",
        "Intervalos con la exposición mediana y la del percentil 95 a avisos de seguridad según la política de actualización: continua 22 y 107 días, lote mensual 29 y 126, lote trimestral 68 y 156 y lote anual 224 y 361.",
        [("Continua (7 días tras la corrección)", [22, 107]), ("Lote mensual", [29, 126]), ("Lote trimestral", [68, 156]), ("Lote anual", [224, 361])],
        unit="Días de exposición", marks=("mediana", "p95"), label_w=220,
        note="El lote anual deja un aviso expuesto diez veces más que la política continua. Aun la continua tiene un percentil 95 de 107 días por el retraso del proveedor, que no depende de ti. El ritmo de avisos y el retraso (mediana 14 días) son supuestos del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-436
def se436_radio_de_impacto() -> Fig:
    return percentile_intervals(
        "Paquetes arrastrados al actualizar uno, en 200 grafos sintéticos de 60 paquetes",
        "Intervalos con los paquetes arrastrados al actualizar uno: una hoja arrastra 0 de mediana, 1 en el percentil 90 y hasta 20; un paquete intermedio 3, 9 y hasta 39; un concentrador con cinco o más dependientes 12, 27 y hasta 44.",
        [("Hoja (0–1 dependientes; 6 797 paquetes)", [0.0, 1, 20]), ("Intermedio (2–4; 3 822)", [3.0, 9, 39]), ("Concentrador (5 o más; 1 381)", [12.0, 27, 44])],
        unit="Paquetes arrastrados", marks=("mediana", "p90", "máx"), label_w=240,
        note="Actualizar un concentrador arrastra 12 paquetes de mediana y 27 en el percentil 90. Los grafos son aleatorios y el 60 % de dependientes que excluye la versión nueva es un supuesto; los grafos reales tienen pocos paquetes muy centrales.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-437
def se437_exposicion_por_estrategia() -> Fig:
    return percentile_intervals(
        "Peticiones afectadas al migrar 40 rutas con 100 000 peticiones diarias y 10 % de rutas con regresión (2 000 historias)",
        "Intervalos con las peticiones afectadas por regresiones, mediana y percentil 95, de tres estrategias de migración: el corte único 20 000 y 35 000 en 4 semanas, el escalonado al 5 por ciento 1 000 y 1 750 en 20 semanas y el escalonado con sombra previa 250 y 1 000 en 40 semanas; en las tres hay 4,0 regresiones.",
        [("Corte único (4 semanas)", [20000, 35000]), ("Escalonado al 5 % (20 semanas)", [1000, 1750]), ("Escalonado con sombra previa (40 semanas)", [250, 1000])],
        unit="Peticiones afectadas", marks=("mediana", "p95"), log=True, label_w=250,
        note="La regresión ocurre las mismas 4,0 veces; cambia cuántas peticiones alcanza. El escalonado reduce el daño 20 veces a cambio de 5 veces más duración. El 10 %, los dos días hasta decidir y el 60 % de eficacia de la sombra son supuestos del autor.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-437
def se437_sombra_y_clases_raras() -> Fig:
    return line_chart(
        "Comparación en sombra: peticiones necesarias para detectar una diferencia según su tasa",
        "Línea en escala logarítmica con las peticiones que hacen falta para detectar una diferencia en comparación en sombra: 299 para el uno por ciento, 2 995 para el 0,1 y 29 956 para el 0,01, de modo que el tamaño de muestra crece como 3 dividido por la tasa.",
        [("Peticiones necesarias", [(1, 299, "299 (96 % de 400 corridas la ven)", "t"), (0.1, 2995, "2 995 (94 %)", "t"), (0.01, 29956, "29 956 (94 %)", "t")], "coral")],
        x_label="Tasa de diferencia que se quiere detectar (%)", y_label="Peticiones necesarias", log_x=True, log_y=True,
        x_ticks=[(0.01, "0,01"), (0.1, "0,1"), (1, "1")], y_ticks=[100, 1000, 10000, 100000], point_labels="none",
        note="El tamaño de muestra crece como 3 dividido por la tasa; pero una clase de tráfico que solo aparece en 4 de 52 semanas exige elegir la ventana por calendario: una ventana de 1, 4, 8 o 12 semanas incluye un cierre en el 7, 21, 31 y 43 % de los inicios posibles. El calendario de cierres es un supuesto del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-437
def se437_traduccion_anticorrupcion() -> Fig:
    return grouped_bars(
        "5 000 registros sintéticos del modelo antiguo: traducción ingenua frente a una capa anticorrupción",
        "Barras horizontales con los registros, de 5 000, por resultado de la traducción: la traducción ingenua lanza excepción con 4 402; la capa anticorrupción no lanza ninguna y deja 2 175 sin errores, 642 con error de nota y 2 491 con error de fecha, y 2 429 quedan con estado desconocido; 1 606 con estado espacio o nulo se vuelven indistinguibles.",
        ["Traducción ingenua: lanza excepción (88,0 %)", "Capa anticorrupción: sin errores", "Capa: con error de nota", "Capa: con error de fecha", "Estado «desconocido» (vacío, nulo o X)",
         "Estado espacio y nulo, antes distintos, ahora iguales"],
        [("Registros", [4402, 2175, 642, 2491, 2429, 1606], "gold")],
        unit="Registros de 5 000", horizontal=True, label_w=300, ticks=[0, 1000, 2000, 3000, 4000, 5000],
        note="La capa no lanza excepciones: clasifica y envía a cuarentena lo que no puede traducir, pero colapsa dos estados que el modelo antiguo distinguía. Un registro puede sumar más de un resultado. Las anomalías y sus frecuencias son una construcción del autor.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-438
def se438_cuatro_cambios_silenciosos() -> Fig:
    return grouped_bars(
        "Cuatro operaciones que siguen ejecutándose con otro resultado, medidas en CPython",
        "Barras horizontales con el porcentaje de resultados distintos de cuatro operaciones: ordenar 2 000 nombres por punto de código frente a plegado de acentos difiere en 1 828 posiciones, el 91,4 por ciento; dividir 7n entre 2 con una barra frente a dos en 500 de 1 000 casos; truncar a 6 bytes parte 114 de 1 000 nombres; redondear a un decimal cambia 50 de 1 000 centésimas.",
        ["Ordenar: punto de código frente a plegado de acentos (2 000 nombres)", "7n/2 frente a 7n//2 (n de 1 a 1 000)", "Truncar a 6 bytes en UTF-8: carácter partido (1 000 nombres)",
         "Redondear a un decimal: regla antigua frente a round (1 000 centésimas)"],
        [("Resultados distintos", [91.4, 50.0, 11.4, 5.0], "coral")],
        unit="Resultados distintos (%)", horizontal=True, label_w=330, ticks=[0, 25, 50, 75, 100], value_fmt=lambda v: fmt_exact(v) + " %",
        note="Ninguna lanza una excepción. Los datos son sintéticos y las frecuencias reales serán otras; las sondas ilustran el tipo de cambio y no son una lista completa de las diferencias de ninguna versión.",
        note_kind="coral", foot=REAL)


# ---------------------------------------------------------------- SE-438
def se438_reescritura_por_estructura() -> Fig:
    return grouped_bars(
        "Reescribir la llamada leer_nota en 400 fragmentos (148 llamadas reales): reescrituras indebidas por método",
        "Barras horizontales con las reescrituras indebidas de tres formas de reescribir la llamada leer_nota en 400 fragmentos de código de los cuales 148 son llamadas reales: la sustitución de texto hace 252, la expresión regular con límites de palabra 166 y el árbol sintáctico 0; ninguno omite una llamada real.",
        ["Sustitución de texto", "Expresión regular con límites de palabra", "Árbol sintáctico (ast)"],
        [("Reescrituras indebidas", [252, 166, 0], "coral")],
        unit="Reescrituras indebidas", horizontal=True, label_w=250, ticks=[0, 100, 200, 300],
        note="Los tres encuentran todas las llamadas y ninguno deja llamadas sin reescribir o mal reescritas; la diferencia está en lo que cambian de más: comentarios, textos, métodos de otros objetos y definiciones. Los nueve tipos de fragmento son del autor y el árbol no se probó con código mal formado ni con reflexión.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-438
def se438_tren_de_versiones() -> Fig:
    return percentile_intervals(
        "Tiempo sin soporte según la política de seguimiento de versiones: una versión al año, tres años de soporte, diez años (1 000 historias)",
        "Intervalos con el porcentaje de tiempo sin soporte, mediana y percentil 90, de tres políticas: al ser forzado 16,3 y 24,9 con 3 migraciones y 21 meses de trabajo; con un año de margen 0,0 y 6,3 con 4 migraciones y 28 meses; paso a paso 0,0 y 0,0 con 9 migraciones y 19 meses.",
        [("Al ser forzado (3 migraciones, 21 meses)", [16.3, 24.9]), ("Con un año de margen (4, 28 meses)", [0.0, 6.3]), ("Paso a paso, 6 meses de retraso (9, 19 meses)", [0.0, 0.0])],
        unit="Tiempo sin soporte (% de los diez años)", marks=("mediana", "p90"), label_w=260, decimals=1,
        note="Esperar a que termine el soporte deja al equipo sin soporte el 16 % del tiempo; seguir paso a paso hace más migraciones y menos meses de trabajo solo si cada migración pequeña cuesta el 30 %. El calendario y el 30 % son supuestos del autor.",
        note_kind="gold", foot=SINT)


FIGURES = {
    "se-433-capacidad-devorada.svg": se433_capacidad_devorada,
    "se-433-clasificar-es-un-juicio.svg": se433_clasificar_es_un_juicio,
    "se-433-fecha-impuesta.svg": se433_fecha_impuesta,
    "se-434-puntos-calientes.svg": se434_puntos_calientes,
    "se-434-conocimiento-que-se-va.svg": se434_conocimiento_que_se_va,
    "se-434-codigo-muerto.svg": se434_codigo_muerto,
    "se-435-cobertura-no-es-detector.svg": se435_cobertura_no_es_detector,
    "se-435-orden-de-un-conjunto.svg": se435_orden_de_un_conjunto,
    "se-435-costura-y-tiempo.svg": se435_costura_y_tiempo,
    "se-436-costo-de-esperar.svg": se436_costo_de_esperar,
    "se-436-ventana-de-exposicion.svg": se436_ventana_de_exposicion,
    "se-436-radio-de-impacto.svg": se436_radio_de_impacto,
    "se-437-exposicion-por-estrategia.svg": se437_exposicion_por_estrategia,
    "se-437-sombra-y-clases-raras.svg": se437_sombra_y_clases_raras,
    "se-437-traduccion-anticorrupcion.svg": se437_traduccion_anticorrupcion,
    "se-438-cuatro-cambios-silenciosos.svg": se438_cuatro_cambios_silenciosos,
    "se-438-reescritura-por-estructura.svg": se438_reescritura_por_estructura,
    "se-438-tren-de-versiones.svg": se438_tren_de_versiones,
}
