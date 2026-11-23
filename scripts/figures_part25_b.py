"""Figures for SE-307 to SE-312 (code analysis and synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, line_chart, stacked_bars
from figures_part07_a import bars

SINT = "Medición sobre código de ejemplo y simulación con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-307
def se295_mutacion() -> Fig:
    items = [
        ("5 ejemplos", 63.2, "coral", "12 de 19 (63,2 %)"),
        ("200 entradas al azar", 73.7, "gold", "14 de 19 (73,7 %)"),
        ("56 entradas en los bordes", 100.0, "teal", "19 de 19 (100 %)"),
        ("Azar + bordes", 100.0, "teal", "19 de 19 (100 %)"),
    ]
    return bars("Mutantes de una función de tarifa que mata cada conjunto de pruebas",
                "Barras: de 19 mutantes generados automáticamente sobre una función de tarifa, cinco ejemplos matan 12, doscientas entradas al azar matan 14 y cincuenta y seis entradas en los bordes de los rangos matan los 19.",
                items, 5, "Los mutantes que sobreviven a los ejemplos son tres de frontera (cambiar <= por <), tres de constante y uno lógico: justo lo que un ejemplo del camino feliz no toca. Ningún mutante resultó equivalente sobre una rejilla de 2140 entradas. Los mutantes son cambios automáticos simples del autor, no defectos reales.",
                label_w=290, width=1000, note_kind="teal", foot=SINT)


def se295_cobertura() -> Fig:
    return grouped_bars(
        "Cobertura de líneas y mutantes muertos de la misma función",
        "Barras agrupadas con la cobertura de líneas y los mutantes muertos de cuatro conjuntos de pruebas: cinco ejemplos, doscientas entradas al azar y ocho entradas sin bordes ejecutan el 90 por ciento de las líneas pero matan el 63,2, el 73,7 y el 63,2 por ciento de los mutantes; las cincuenta y seis entradas en los bordes alcanzan el 100 por ciento de ambos.",
        ["5 ejemplos", "200 entradas al azar", "8 entradas por todas las ramas, sin bordes", "56 entradas en los bordes"],
        [("Líneas ejecutadas", [90.0, 90.0, 90.0, 100.0], "grey"), ("Mutantes muertos", [63.2, 73.7, 63.2, 100.0], "coral")],
        unit="Porcentaje (%)", decimals=1, ticks=[0, 20, 40, 60, 80, 100], plot_h=270,
        note="Ejecutar una línea no es comprobarla: 90 % de cobertura convive con un tercio de mutantes vivos. La línea que falta es la del error por peso fuera de rango, que solo un borde alcanza. La cobertura dice qué no se ejecutó; la mutación, qué no se comprueba.",
        note_kind="gold", foot=SINT)


def se295_paso() -> Fig:
    return line_chart(
        "60 pasos de refactor con 3 % de probabilidad de defecto por paso: tamaño del lote",
        "Líneas en escala logarítmica en el tamaño del lote: el porcentaje de lotes con dos o más defectos sube de 0 con un paso a 15,3 con 12 pasos y 64,6 con un lote de 60; los defectos escondidos tras otro suben de 0 a 14,5 con 12 pasos y 53,5 con 60.",
        [("Lotes con 2 o más defectos", [(1, 0.0), (3, 3.0), (6, 8.1), (12, 15.3), (30, 36.5), (60, 64.6)], "coral"),
         ("Defectos escondidos tras otro", [(1, 0.0), (3, 3.0), (6, 7.8), (12, 14.5), (30, 32.8), (60, 53.5)], "gold")],
        x_label="Pasos por lote", y_label="Porcentaje (%)", log_x=True,
        x_ticks=[(1, "1"), (3, "3"), (6, "6"), (12, "12"), (30, "30"), (60, "60")], y_ticks=[0, 20, 40, 60, 80],
        point_labels="last", decimals=1, plot_h=280,
        note="Los porcentajes salen de simular 6000 repeticiones; los pasos que revisar (la mitad del lote: de 1 a 30) y las corridas de pruebas (de 1 a 7, una más una bisección) son una fórmula del modelo, no un conteo. Con pasos pequeños el defecto tiene un solo sospechoso; con uno grande, la primera pista se oculta tras otro defecto.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-308
def se296_modulos() -> Fig:
    return grouped_bars(
        "Módulos que hay que editar al cambiar una decisión de diseño",
        "Barras horizontales con los módulos que se editan al cambiar una de seis decisiones: la descomposición por pasos del flujo obliga a editar 2 módulos y 4 en moneda y redondeo, 2,19 de media sobre mil cambios; la descomposición por decisión oculta obliga a editar uno en todos los casos.",
        ["Tarifas", "Zonas", "Descuentos (30 % de los cambios)", "Moneda y redondeo", "Canal de aviso", "Persistencia", "Media sobre 1000 cambios"],
        [("Por pasos del flujo (5 módulos)", [2, 2, 2, 4, 2, 2, 2.19], "coral"), ("Por decisión oculta (6 + orquestador)", [1, 1, 1, 1, 1, 1, 1.00], "teal")],
        unit="Módulos que editar", horizontal=True, decimals=None, label_w=270, width=960,
        value_fmt=lambda v: f"{v:.2f}".replace(".", ",") if v not in (1, 2, 4) else str(int(v)),
        note="La moneda aparece en cuatro pasos del flujo: un cambio de redondeo recorre cuatro módulos. Con módulos que conocen cada decisión al azar con probabilidad 0,3, la media es 1,48; con 0,5, 2,50. Las matrices de conocimiento y los pesos de los cambios son supuestos del autor, no un proyecto medido.",
        note_kind="gold", foot=SINT)


def se296_reloj() -> Fig:
    return grouped_bars(
        "Una prueba que espera «sin recargo» ejecutada en cada minuto de una semana",
        "Barras horizontales con el porcentaje de los 10 080 minutos de una semana en que falla la prueba: con el reloj real falla el 28,6 por ciento en el huso UTC, en UTC menos 3 y en UTC más 9; el servidor en UTC y una persona en UTC menos 3 discrepan sobre si es fin de semana en el 3,6 por ciento; con un reloj inyectado fijo en un miércoles no falla ninguno.",
        ["Reloj real, huso de UTC", "Reloj real, huso UTC−3", "Reloj real, huso UTC+9", "UTC y UTC−3 discrepan sobre el fin de semana", "Reloj inyectado con un miércoles fijo"],
        [("Minutos con fallo o discrepancia (% de 10 080)", [28.6, 28.6, 28.6, 3.6, 0.0], "coral")],
        unit="Minutos de la semana (%)", horizontal=True, decimals=1, label_w=330, width=980,
        note="El 28,6 % es 2/7: una prueba que no controla el reloj pasa de lunes a viernes y falla el fin de semana, y el huso solo cambia qué minutos fallan (2880 de 10 080 en cada huso; 360 de discrepancia). Con dos lecturas del reloj separadas 20 ms junto a cada medianoche, 2 de 7 medianoches dan un resultado distinto. Inyectar el reloj convierte esa dependencia en un parámetro. Cálculo exhaustivo sobre una semana, sin reloj real.",
        note_kind="coral", foot=SINT)


def se296_registros() -> Fig:
    items = [
        ("2 solicitudes/s por worker (concurrencia ~0,15)", 92.2, "teal", "92,2 %"),
        ("6 solicitudes/s (~0,45)", 78.0, "gold", "78,0 %"),
        ("12 solicitudes/s (~0,90)", 61.6, "gold", "61,6 %"),
        ("25 solicitudes/s (~1,88)", 40.9, "coral", "40,9 %"),
    ]
    return bars("Secuencias reconstruidas sin identificador de solicitud (con identificador: 100 %)",
                "Barras: al reconstruir sin identificador de solicitud la secuencia de eventos de cada petición a partir de registros de cuatro workers, se acierta el 92,2 por ciento con 2 solicitudes por segundo y por worker, el 78 con 6, el 61,6 con 12 y el 40,9 con 25; con un identificador de solicitud se acierta el 100 por ciento.",
                items, 6.5, "Sin identificador, el orden y el worker no bastan en cuanto hay solicitudes simultáneas: la reconstrucción las mezcla. El identificador cuesta una línea por registro y evita la heurística. 1200 solicitudes con cinco pasos de duración lognormal; la regla de reconstrucción es una construcción del autor.",
                label_w=410, width=1000, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-309
def se297_forma() -> Fig:
    return dumbbell(
        "La misma regla de tarifa en una tabla con tres reglas y en condicionales anidados",
        "Gráfico de mancuernas en escala logarítmica: la misma regla ocupa 13 líneas con complejidad 4 y 8 caminos en forma de tabla más tres reglas, y 51 líneas, complejidad 19 y 96 caminos en condicionales anidados; las 96 combinaciones esenciales de la regla son iguales en ambas.",
        [("Líneas", 13, 51), ("Complejidad ciclomática", 4, 19), ("Anidamiento máximo", 1, 3),
         ("Caminos distintos recorridos por la rejilla", 8, 96), ("Combinaciones esenciales de la regla", 96, 96)],
        unit="Cantidad", names=("Tabla + 3 reglas", "Condicionales anidados"), log=True,
        delta=lambda a, b: "igual" if a == b else "×" + f"{b / a:.1f}".replace(".", ","), lower_is_better=True,
        label_w=330, width=980,
        note="La regla tiene 96 combinaciones en cualquier forma: eso es complejidad esencial. La forma anidada reparte la misma regla en 96 caminos de código y multiplica por cinco la complejidad ciclomática: lo que sobra es accidental. Coinciden en 224 entradas; no se probó equivalencia completa.",
        note_kind="teal", foot=SINT)


def se297_pares() -> Fig:
    return line_chart(
        "Configuraciones de opciones binarias: todas frente a un conjunto que cubre todos los pares",
        "Líneas en escala logarítmica según el número de opciones binarias: probar todas las configuraciones crece de 16 con 4 opciones a 4096 con 12, mientras que un conjunto que cubre todos los pares crece de 6 a 9 configuraciones.",
        [("Todas las configuraciones", [(4, 16), (6, 64), (8, 256), (10, 1024), (12, 4096)], "coral"),
         ("Conjunto que cubre todos los pares", [(4, 6), (6, 7), (8, 8), (10, 8), (12, 9)], "teal")],
        x_label="Opciones binarias", y_label="Configuraciones que probar", log_y=True,
        x_ticks=[(4, "4"), (6, "6"), (8, "8"), (10, "10"), (12, "12")], y_ticks=[1, 10, 100, 1000, 10000],
        decimals=0, plot_h=280,
        note="Con 12 opciones, las 9 configuraciones cubren todos los pares, el 81,5 % de los tríos y el 50,3 % de los cuartetos (con 10 opciones, 8 configuraciones: 77,7 % y 46,1 %). Si los fallos de interacción suelen implicar pocas opciones, los pares atrapan casi todos con una fracción de las pruebas; si requieren tres o cuatro, la mitad queda sin ver. El conjunto se construyó con un algoritmo voraz de semilla fija. Pares al azar del mismo tamaño cubren menos.",
        note_kind="gold", foot=SINT)


def se297_cognitiva() -> Fig:
    return grouped_bars(
        "Complejidad ciclomática y complejidad cognitiva simplificada de cinco funciones",
        "Barras agrupadas con la complejidad ciclomática y la cognitiva de cinco funciones: la cadena plana de ocho casos y las ocho condiciones anidadas tienen ciclomática 8 y 9, casi iguales, pero cognitiva 7 y 36; la tabla de consulta tiene ciclomática 1 y cognitiva 0.",
        ["Cadena plana de 8 casos", "Ocho condiciones anidadas", "Bucle con condición y salida", "Las ocho condiciones en una conjunción", "Tabla de consulta"],
        [("Ciclomática", [8, 9, 4, 3, 1], "navy"), ("Cognitiva (simplificada)", [7, 36, 5, 2, 0], "coral")],
        unit="Complejidad", horizontal=True, decimals=0, label_w=300, width=980,
        note="La ciclomática cuenta caminos; la cognitiva penaliza el anidamiento porque cada nivel obliga a recordar más condiciones a la vez (anidamiento 1 en la cadena plana y 8 en la anidada). Ocho casos planos se leen de arriba abajo; ocho niveles, no. La implementación es una versión simplificada del autor: no reproduce la de ninguna herramienta.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-310
def se298_politicas() -> Fig:
    ticks = [(0.002, "0,002"), (0.006, "0,006"), (0.012, "0,012"), (0.020, "0,020")]
    return line_chart(
        "Puntos entregados en 24 sprints según la política de pago de deuda y el interés (parámetros supuestos)",
        "Líneas con los puntos entregados en 24 sprints según el interés por unidad de deuda: no pagar nunca baja de 703 puntos con interés 0,002 a 173 con 0,020; pagar todo hasta bajar de 10 unidades baja solo de 716 a 609; con interés bajo todas las políticas entregan casi lo mismo y con interés alto la diferencia es de un factor 3,5.",
        [("Nunca pagar", [(0.002, 703), (0.006, 408), (0.012, 241), (0.020, 173)], "coral"),
         ("20 % de la capacidad", [(0.002, 717), (0.006, 654), (0.012, 609), (0.020, 585, "585", "b")], "gold"),
         ("50 % cuando la deuda pasa de 25", [(0.002, 706), (0.006, 663), (0.012, 600), (0.020, 505, "505", "b")], "navy"),
         ("Todo hasta bajar de 10", [(0.002, 716), (0.006, 693), (0.012, 651), (0.020, 609, "609", "t")], "teal")],
        x_label="Interés por unidad de deuda", y_label="Puntos entregados en 24 sprints", x_ticks=ticks,
        y_ticks=[0, 200, 400, 600, 800], point_labels="last", decimals=0, plot_h=300, width=980,
        note="Con interés bajo, pagar no mejora lo entregado (703 frente a 717 puntos): la deuda barata se puede dejar. Con interés alto, no pagar entrega menos de un tercio. La deuda final de «nunca pagar» pasa de 246 a 68 unidades según el interés y la de «todo hasta bajar de 10», de 23 a 7. La política correcta depende de la tasa, que hay que estimar. Capacidad, generación de deuda e interés son supuestos del autor; no se midió ningún equipo.",
        note_kind="coral", foot=SINT)


def se298_opcion() -> Fig:
    return line_chart(
        "Costo esperado en 12 meses (puntos): refactorizar ahora, al primer cambio o nunca",
        "Líneas en escala logarítmica con el costo esperado según los cambios por mes del área: no refactorizar sube de 1,83 con 0,05 cambios por mes a 72,22 con 2; refactorizar ahora cuesta 8 siempre; esperar al primer cambio cuesta entre 3,68 y 8; nunca gana con 0,15 cambios por mes o menos, el primer cambio con 0,30 y ahora con 1 o más.",
        [("Nunca", [(0.05, 1.83), (0.15, 5.43), (0.30, 10.84), (0.60, 21.64), (1.0, 36.04), (2.0, 72.22)], "coral"),
         ("Ahora", [(0.05, 8.0), (0.15, 8.0), (0.30, 8.0), (0.60, 8.0), (1.0, 8.0), (2.0, 8.0)], "navy"),
         ("Al primer cambio", [(0.05, 3.68), (0.15, 6.77), (0.30, 7.83), (0.60, 8.0), (1.0, 8.0), (2.0, 8.0)], "teal")],
        x_label="Cambios por mes en el área", y_label="Costo esperado en 12 meses (puntos)", log_x=True, log_y=True,
        x_ticks=[(0.05, "0,05"), (0.15, "0,15"), (0.30, "0,3"), (0.60, "0,6"), (1.0, "1"), (2.0, "2")],
        y_ticks=[1, 2, 5, 10, 20, 50, 100], point_labels="none", decimals=2, plot_h=300, width=980,
        note="Esperar al primer cambio es una opción: se paga solo si el área se mueve. Si aplazar duplica el costo del refactor, desde 0,30 cambios por mes conviene hacerlo ahora. Deja de convenir esperar cuando aplazar encarece el trabajo (se pierde el contexto) o cuando el área cambia tanto que el pago es seguro. Un área que nunca cambia no merece refactor, aunque se vea fea. Poisson aproximado, 20 000 repeticiones y parámetros supuestos.",
        note_kind="teal", foot=SINT)


def se298_calientes() -> Fig:
    return grouped_bars(
        "Reducción del interés pagado al refactorizar 5 de 40 archivos según cómo se eligen",
        "Barras agrupadas con la reducción del interés pagado según el criterio de elección y la relación entre complejidad y cambios: sin relación, elegir por complejidad reduce el 17,8 por ciento, por cambios el 33,9, por complejidad por cambios el 36,6 y al azar el 7,4; con coincidencia total los tres criterios dan 48,1.",
        ["Sin relación", "Relación media (0,5)", "Relación total (1,0)"],
        [("Por complejidad", [17.8, 37.3, 48.1], "coral"), ("Por cambios", [33.9, 43.1, 48.1], "gold"),
         ("Por complejidad × cambios", [36.6, 44.1, 48.1], "teal"), ("Al azar", [7.4, 8.2, 7.3], "grey")],
        unit="Reducción del interés pagado (%)", decimals=1, ticks=[0, 10, 20, 30, 40, 50], plot_h=270, width=980,
        note="El archivo más complejo no es necesariamente el más caro: si nadie lo toca, su deuda no paga interés. Esto es un resultado del modelo, que fija como supuesto que el interés es complejidad por cambios: con otro supuesto el orden de los criterios puede cambiar. 400 repeticiones con semilla fija.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-311
def se299_pasos() -> Fig:
    return grouped_bars(
        "Entradas del maestro dorado (3000) cuyo resultado cambia en cada paso del refactor",
        "Barras horizontales con las entradas del maestro dorado, de 3000, cuyo resultado cambia en cada paso: extraer zona y peso no cambia ninguna, extraer opciones, cupón y redondeo tampoco, simplificar la comparación con True cambia 142 y sustituir el redondeo histórico por round cambia 257, 106 de ellas con parámetros booleanos.",
        ["1. Extraer zona y peso", "2. Extraer opciones, cupón y redondeo", "3. Simplificar «urgente == True» a «if urgente»", "4. Cambiar el redondeo histórico por round()"],
        [("Entradas que difieren (de 3000)", [0, 0, 142, 257], "coral")],
        unit="Entradas cuyo resultado cambia", horizontal=True, decimals=0, label_w=340, width=980,
        note="Los dos pasos que parecían simplificaciones cambiaron comportamiento: el primero (142, con urgente igual a 2 o «sí») con entradas que la función aceptaba sin documentar, el segundo (257, de ellas 106 con urgente booleano) con la diferencia entre sumar 0,5 y redondear al par. Hay que decidir caso por caso si el comportamiento se conserva o se corrige. Entradas sintéticas con semilla fija.",
        note_kind="coral", foot=SINT)


def se299_mutantes() -> Fig:
    items = [
        ("10 entradas registradas", 81.6, "coral", "31,8 de 39 (81,6 %)"),
        ("50 entradas", 92.9, "gold", "36,2 de 39 (92,9 %)"),
        ("200 entradas", 96.8, "gold", "37,7 de 39 (96,8 %)"),
        ("1000 entradas", 99.4, "teal", "38,8 de 39 (99,4 %)"),
        ("3000 entradas", 100.0, "teal", "39 de 39 (100 %)"),
    ]
    return bars("Mutantes de la función refactorizada que mata un maestro dorado según su tamaño (media de 30 muestras)",
                "Barras: un maestro dorado con 10 entradas registradas al azar mata en promedio el 81,6 por ciento de los 39 mutantes de la función refactorizada, con 50 el 92,9, con 200 el 96,8, con 1000 el 99,4 y con 3000 los mata todos.",
                items, 5, "El mínimo con 10 entradas fue 27 de 39 y con 200 fue 36: la variación entre muestras importa tanto como la media. Con 200 entradas aún sobreviven en promedio 1,3 mutantes. Los mutantes son cambios automáticos y el dominio de entradas es pequeño; con un dominio grande la curva sube mucho más despacio.",
                label_w=260, width=1050, note_kind="gold", foot=SINT)


def se299_arcos() -> Fig:
    return line_chart(
        "Arcos de la función heredada alcanzados según el número de entradas registradas",
        "Líneas en escala logarítmica con los arcos alcanzados según las entradas registradas: la media sube de 67,4 por ciento con 3 entradas a 88,7 con 10, 94,9 con 30 y 96,7 con 300; el mínimo de 30 muestras va de 52,4 a 95,2; solo las 3000 entradas alcanzan el 100 por ciento.",
        [("Media de 30 muestras", [(3, 67.4, "67,4", "t"), (10, 88.7, "88,7", "t"), (30, 94.9, "94,9", "t"), (100, 96.0, "96,0", "t"), (300, 96.7, "96,7", "t"), (3000, 100.0, "100,0", "t")], "teal"),
         ("Mínimo de 30 muestras", [(3, 52.4, "52,4", "b"), (10, 78.6, "78,6", "b"), (30, 90.5, "90,5", "b"), (100, 90.5, "90,5", "b"), (300, 95.2, "95,2", "b"), (3000, 100.0, " ", "b")], "coral")],
        x_label="Entradas registradas", y_label="Arcos alcanzados (%)", log_x=True,
        x_ticks=[(3, "3"), (10, "10"), (30, "30"), (100, "100"), (300, "300"), (3000, "3000")],
        y_ticks=[50, 60, 70, 80, 90, 100], y_zero=False, point_labels="all", decimals=1, plot_h=290, width=980,
        note="Los primeros diez casos rinden mucho y los últimos arcos cuestan miles: los caminos raros (el cupón de envío gratis fuera de zona, el piso en cero) casi no aparecen al azar. Hay que ir a buscarlos. El eje vertical empieza en 50 %. Tras el paso 2, la función de 15 de complejidad queda en seis funciones, la mayor con 4.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-312
def se300_firma() -> Fig:
    return stacked_bars(
        "Consumidores rotos por cada uno de doce cambios de una función pública, y si la firma lo ve",
        "Barras horizontales con los consumidores rotos, de 8, por cada cambio: la firma detecta cinco cambios que rompen (añadir un parámetro obligatorio, eliminar, renombrar, reordenar y pasar a solo por nombre) y no ve cinco que rompen a entre uno y cinco consumidores (cambiar el valor por defecto, el redondeo, rechazar pesos altos, añadir un valor a un campo y añadir un campo a la respuesta); dos cambios sin efecto no rompen a nadie.",
        ["Añadir un parámetro obligatorio solo por nombre", "Reordenar parámetros", "Eliminar un parámetro", "Renombrar un parámetro",
         "Pasar un parámetro a solo por nombre", "Cambiar el redondeo", "Cambiar el valor por defecto", "Rechazar pesos mayores de 30",
         "Añadir un valor al campo estado", "Añadir un campo notas a la respuesta", "Añadir un parámetro opcional al final",
         "Reescribir sin cambio observable"],
        [("La firma lo detecta", [8, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0], "teal"),
         ("La firma no lo ve", [0, 0, 0, 0, 0, 5, 3, 2, 1, 1, 0, 0], "coral")],
        unit="Consumidores rotos (de 8)", horizontal=True, decimals=0, label_w=330, width=1000,
        note="Cinco de diez cambios con efecto real no cambian la firma: el verificador por firma es necesario y no suficiente. Los dos cambios sin consumidores rotos (añadir un opcional al final y reescribir sin cambio observable) los clasifica bien como compatibles; no hubo falsas alarmas. Los consumidores son ocho funciones sintéticas con estilos de llamada distintos; su cobertura es del autor y una compatibilidad semántica real exige consumidores reales.",
        note_kind="coral", foot=SINT)


def se300_deprecacion() -> Fig:
    return line_chart(
        "Retirar la versión antigua: clientes que se rompen (500 clientes, parámetros supuestos)",
        "Líneas con el porcentaje de clientes que se rompen al retirar la versión antigua según la semana de retirada: baja de 53,8 por ciento en la semana 8 a 42,4 en la 12, 31,6 en la 26, 27,4 en la 52 y 25,8 en la 104, y se acerca al 25,6 por ciento que nunca migra solo, sin llegar a cero.",
        [("Se rompen al retirar", [(8, 53.8), (12, 42.4), (26, 31.6), (52, 27.4), (104, 25.8)], "coral")],
        x_label="Semana de retirada", y_label="Clientes que se rompen (% de 500)", log_x=True,
        x_ticks=[(8, "8"), (12, "12"), (26, "26"), (52, "52"), (104, "104")], y_ticks=[0, 10, 20, 30, 40, 50, 60],
        hlines=[(25.6, "nunca migrará solo: 25,6 %")], point_labels="all", decimals=1, plot_h=280, width=980,
        note="Con retirada en la semana 12 se rompen 212 clientes (42,4 %) y en la 104 todavía 129 (25,8 %); los que ya migraron suben de 46,2 % a 74,2 %. El 75 % de los diligentes migra en 11,3 semanas, el 95 % en 36,3 y el 99 % en 72,4, pero el 25,6 % de los clientes (abandonados y reactivos) nunca migrará solo. Una ventana larga cuesta mantenimiento en paralelo y no elimina el riesgo; la fecha de retirada es una decisión de producto con aviso. Todos los porcentajes son supuestos.",
        note_kind="gold", foot=SINT)


def se300_contratos() -> Fig:
    return grouped_bars(
        "Cambios de una respuesta de 12 campos que rompen a algún consumidor: quién los detecta",
        "Barras horizontales con las roturas detectadas de 23 que rompen a algún consumidor entre 54 cambios probados: la suite del proveedor, que comprueba cuatro campos de doce, detecta 9 y deja pasar 14; las pruebas de contrato de los ocho consumidores detectan las 23.",
        ["Rompen a algún consumidor", "Las detecta la suite del proveedor (4 de 12 campos)", "Las detectan los contratos de los 8 consumidores"],
        [("Cambios (de 54 probados)", [23, 9, 23], "teal")],
        unit="Cambios que rompen a un consumidor", horizontal=True, decimals=0, label_w=330, width=980,
        note="Los que no ve el proveedor son 14 de 23. El contrato dirigido por el consumidor acierta porque cada consumidor declara lo que lee: añadir un campo no alarma y quitar uno que nadie usa tampoco; un esquema exacto, en cambio, da 36 alarmas, 16 de ellas sin consumidor afectado. Los diez campos que algún consumidor lee son los que pesan. Ocho consumidores sintéticos que leen entre 2 y 4 campos con semilla fija; la detección de contratos es 100 % por construcción del modelo.",
        note_kind="teal", foot=SINT)


FIGURES = {
    "se-307-puntuacion-de-mutacion.svg": se295_mutacion,
    "se-307-cobertura-frente-a-mutacion.svg": se295_cobertura,
    "se-307-tamano-del-paso.svg": se295_paso,
    "se-308-modulos-tocados-por-cambio.svg": se296_modulos,
    "se-308-reloj-real-e-inyectado.svg": se296_reloj,
    "se-308-correlacion-de-registros.svg": se296_registros,
    "se-309-la-misma-regla-en-dos-formas.svg": se297_forma,
    "se-309-cobertura-por-pares.svg": se297_pares,
    "se-309-ciclomatica-y-cognitiva.svg": se297_cognitiva,
    "se-310-politicas-de-pago-e-interes.svg": se298_politicas,
    "se-310-refactorizar-ahora-o-despues.svg": se298_opcion,
    "se-310-puntos-calientes.svg": se298_calientes,
    "se-311-maestro-dorado-por-pasos.svg": se299_pasos,
    "se-311-entradas-que-matan-mutantes.svg": se299_mutantes,
    "se-311-cobertura-segun-entradas.svg": se299_arcos,
    "se-312-firma-frente-a-comportamiento.svg": se300_firma,
    "se-312-ventana-de-deprecacion.svg": se300_deprecacion,
    "se-312-contratos-de-consumidor.svg": se300_contratos,
}
