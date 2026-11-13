"""Figures for SE-295 to SE-300 (code analysis and synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Medición sobre código de ejemplo y simulación con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-295
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
    rows = [
        ["5 ejemplos", "90,0 %", "63,2 %"],
        ["200 entradas al azar", "90,0 %", "73,7 %"],
        ["8 entradas que recorren todas las ramas del cálculo, sin bordes", "90,0 %", "63,2 %"],
        ["56 entradas en los bordes", "100 %", "100 %"],
    ]
    return tab("Cobertura de líneas y mutantes muertos de la misma función",
               "Tabla: cinco ejemplos, doscientas entradas al azar y ocho entradas sin bordes tienen la misma cobertura de líneas, 90 por ciento, pero matan el 63,2, el 73,7 y el 63,2 por ciento de los mutantes; las cincuenta y seis entradas en los bordes alcanzan el 100 por ciento de las líneas y de los mutantes.",
               ["Conjunto de pruebas", "Líneas ejecutadas", "Mutantes muertos"], rows, [480, 200, 210], row_h=44, size=13,
               note="Ejecutar una línea no es comprobarla: 90 % de cobertura convive con un tercio de mutantes vivos. La línea que falta es la del error por peso fuera de rango, que solo un borde alcanza. La cobertura dice qué no se ejecutó; la mutación, qué no se comprueba.",
               note_kind="gold", foot=SINT)


def se295_paso() -> Fig:
    rows = [
        ["1", "0,0 %", "1,0", "1,0", "0,0 %"],
        ["3", "3,0 %", "1,5", "3,0", "3,0 %"],
        ["6", "8,1 %", "3,0", "4,0", "7,8 %"],
        ["12", "15,3 %", "6,0", "5,0", "14,5 %"],
        ["30", "36,5 %", "15,0", "6,0", "32,8 %"],
        ["60", "64,6 %", "30,0", "7,0", "53,5 %"],
    ]
    return tab("60 pasos de refactor con 3 % de probabilidad de defecto por paso: tamaño del lote",
               "Tabla: con sesenta pasos y tres por ciento de probabilidad de introducir un defecto en cada uno, al comprobar después de cada paso nunca hay dos defectos mezclados; con lotes de 12 pasos el 15,3 por ciento de los lotes defectuosos tiene dos o más y hay que revisar seis pasos de media; con un solo lote de 60, el 64,6 por ciento tiene dos o más.",
               ["Pasos por lote", "Lotes con 2 o más defectos", "Pasos que revisar", "Corridas de pruebas", "Defectos escondidos tras otro"], rows, [150, 220, 170, 170, 230], row_h=40, size=12,
               note="Los porcentajes salen de simular 6000 repeticiones; los pasos que revisar (la mitad del lote) y las corridas (una más una bisección) son una fórmula del modelo, no un conteo. Con pasos pequeños el defecto tiene un solo sospechoso; con uno grande, la primera pista se oculta tras otro defecto.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-296
def se296_modulos() -> Fig:
    rows = [
        ["Tarifas", "2", "1"],
        ["Zonas", "2", "1"],
        ["Descuentos (30 % de los cambios)", "2", "1"],
        ["Moneda y redondeo", "4", "1"],
        ["Canal de aviso", "2", "1"],
        ["Persistencia", "2", "1"],
        ["Media sobre 1000 cambios", "2,19", "1,00"],
    ]
    return tab("Módulos que hay que editar al cambiar una decisión de diseño",
               "Tabla: al cambiar una de seis decisiones, una descomposición por pasos del flujo obliga a editar entre 2 y 4 módulos y 2,19 de media sobre mil cambios, mientras que una descomposición que oculta cada decisión en un módulo obliga a editar uno.",
               ["Decisión que cambia", "Por pasos del flujo (5 módulos)", "Por decisión oculta (6 + orquestador)"], rows, [330, 270, 290], row_h=36, size=12,
               note="La moneda aparece en cuatro pasos del flujo: un cambio de redondeo recorre cuatro módulos. Con módulos que conocen cada decisión al azar con probabilidad 0,3, la media es 1,48; con 0,5, 2,50. Las matrices de conocimiento y los pesos de los cambios son supuestos del autor, no un proyecto medido.",
               note_kind="gold", foot=SINT)


def se296_reloj() -> Fig:
    rows = [
        ["Reloj real, huso de UTC", "2880 de 10 080 (28,6 %)"],
        ["Reloj real, huso UTC−3", "2880 de 10 080 (28,6 %)"],
        ["Reloj real, huso UTC+9", "2880 de 10 080 (28,6 %)"],
        ["UTC y UTC−3 discrepan sobre si es fin de semana", "360 de 10 080 (3,6 %)"],
        ["Dos lecturas del reloj con 20 ms de separación, junto a cada medianoche", "2 de 7 medianoches con resultado distinto"],
        ["Reloj inyectado con un miércoles fijo", "0 de 10 080"],
    ]
    return tab("Una prueba que espera «sin recargo» ejecutada en cada minuto de una semana",
               "Tabla: una prueba que espera que no haya recargo de fin de semana y lee el reloj real falla en 2880 de los 10 080 minutos de una semana, un 28,6 por ciento, en cualquier huso horario; el servidor en UTC y una persona en UTC menos 3 discrepan sobre si es fin de semana durante 360 minutos; con un reloj inyectado fijo en un miércoles no falla ninguna ejecución.",
               ["Situación", "Minutos con fallo / resultado"], rows, [560, 330], row_h=52, size=13,
               note="El 28,6 % es 2/7: una prueba que no controla el reloj pasa de lunes a viernes y falla el fin de semana, y el huso solo cambia qué minutos fallan. Inyectar el reloj convierte esa dependencia en un parámetro: la prueba ejecuta el miércoles de siempre. Cálculo exhaustivo sobre una semana, sin reloj real.",
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


# ---------------------------------------------------------------- SE-297
def se297_forma() -> Fig:
    rows = [
        ["Líneas", "13", "51"],
        ["Complejidad ciclomática", "4", "19"],
        ["Anidamiento máximo", "1", "3"],
        ["Caminos distintos recorridos por la rejilla", "8", "96"],
        ["Combinaciones esenciales de la regla", "96", "96"],
    ]
    return tab("La misma regla de tarifa en una tabla con tres reglas y en condicionales anidados",
               "Tabla: la misma regla de tarifa, con cuatro zonas, tres bandas de peso y tres opciones, ocupa 13 líneas con complejidad 4 en forma de tabla más tres reglas y 51 líneas con complejidad 19 en condicionales anidados; ambas coinciden en las 224 entradas de la rejilla y la regla tiene 96 combinaciones esenciales.",
               ["Medida", "Tabla + 3 reglas", "Condicionales anidados"], rows, [440, 220, 230], row_h=44, size=13,
               note="La regla tiene 96 combinaciones en cualquier forma: eso es complejidad esencial. La forma anidada reparte la misma regla en 96 caminos de código y multiplica por cinco la complejidad ciclomática: lo que sobra es accidental. Coinciden en 224 entradas; no se probó equivalencia completa.",
               note_kind="teal", foot=SINT)


def se297_pares() -> Fig:
    rows = [
        ["4", "16", "6", "75,0 %", "37,5 %", "62,5 %"],
        ["6", "64", "7", "74,4 %", "42,1 %", "91,7 %"],
        ["8", "256", "8", "74,8 %", "45,3 %", "84,8 %"],
        ["10", "1024", "8", "77,7 %", "46,1 %", "91,7 %"],
        ["12", "4096", "9", "81,5 %", "50,3 %", "95,8 %"],
    ]
    return tab("Configuraciones de opciones binarias: todas frente a un conjunto que cubre todos los pares",
               "Tabla: para 12 opciones binarias hay 4096 configuraciones; nueve configuraciones bien elegidas cubren todos los pares, el 81,5 por ciento de los tríos y el 50,3 por ciento de los cuartetos; con 10 opciones bastan 8 configuraciones para cubrir todos los pares frente a 1024.",
               ["Opciones", "Todas", "Cubren todos los pares", "Tríos cubiertos", "Cuartetos cubiertos", "Pares con el mismo número al azar"], rows, [100, 100, 220, 170, 190, 230], row_h=44, size=12,
               note="Si los fallos de interacción suelen implicar pocas opciones, los pares atrapan casi todos con una fracción de las pruebas; si requieren tres o cuatro, la mitad queda sin ver. El conjunto se construyó con un algoritmo voraz de semilla fija. Pares al azar del mismo tamaño cubren menos.",
               note_kind="gold", foot=SINT)


def se297_cognitiva() -> Fig:
    rows = [
        ["Cadena plana de 8 casos", "8", "7", "1"],
        ["Ocho condiciones anidadas", "9", "36", "8"],
        ["Bucle con condición y salida", "4", "5", "2"],
        ["Las mismas ocho condiciones en una conjunción", "3", "2", "1"],
        ["Tabla de consulta", "1", "0", "0"],
    ]
    return tab("Complejidad ciclomática y complejidad cognitiva simplificada de cinco funciones",
               "Tabla: una cadena plana de ocho casos y ocho condiciones anidadas tienen complejidad ciclomática 8 y 9, casi iguales, pero complejidad cognitiva 7 y 36; la tabla de consulta tiene ciclomática 1 y cognitiva 0.",
               ["Función", "Ciclomática", "Cognitiva (simplificada)", "Anidamiento"], rows, [420, 140, 200, 150], row_h=44, size=13,
               note="La ciclomática cuenta caminos; la cognitiva penaliza el anidamiento porque cada nivel obliga a recordar más condiciones a la vez. Ocho casos planos se leen de arriba abajo; ocho niveles, no. La implementación es una versión simplificada del autor: no reproduce la de ninguna herramienta.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-298
def se298_politicas() -> Fig:
    rows = [
        ["Nunca pagar", "703 / 246", "408 / 146", "241 / 91", "173 / 68"],
        ["20 % de la capacidad", "717 / 59", "654 / 38", "609 / 23", "585 / 15"],
        ["50 % cuando la deuda pasa de 25", "706 / 33", "663 / 38", "600 / 35", "505 / 23"],
        ["Todo hasta bajar de 10", "716 / 23", "693 / 22", "651 / 8", "609 / 7"],
    ]
    return tab("Puntos entregados en 24 sprints / deuda final según la política y el interés (parámetros supuestos)",
               "Tabla: en 24 sprints con capacidad 40 puntos, no pagar nunca entrega 703 puntos con un interés de 0,002 por unidad de deuda y 173 con 0,020; pagar todo hasta bajar de 10 unidades entrega 716 y 609; con interés bajo todas las políticas entregan casi lo mismo y con interés alto la diferencia es de un factor 3,5.",
               ["Política", "Interés 0,002", "0,006", "0,012", "0,020"], rows, [330, 150, 150, 150, 150], row_h=44, size=13,
               note="Con interés bajo, pagar no mejora lo entregado (703 frente a 717 puntos): la deuda barata se puede dejar. Con interés alto, no pagar entrega menos de un tercio. La política correcta depende de la tasa, que hay que estimar. Capacidad, generación de deuda e interés son supuestos del autor; no se midió ningún equipo.",
               note_kind="coral", foot=SINT)


def se298_opcion() -> Fig:
    rows = [
        ["0,05", "1,83", "8,00", "3,68", "nunca", "nunca"],
        ["0,15", "5,43", "8,00", "6,77", "nunca", "nunca"],
        ["0,30", "10,84", "8,00", "7,83", "al primer cambio", "ahora"],
        ["0,60", "21,64", "8,00", "8,00", "al primer cambio", "ahora"],
        ["1,00", "36,04", "8,00", "8,00", "ahora", "ahora"],
        ["2,00", "72,22", "8,00", "8,00", "ahora", "ahora"],
    ]
    return tab("Costo esperado en 12 meses (puntos): refactorizar ahora, al primer cambio o nunca",
               "Tabla: con un refactor de 8 puntos y una fricción de 3 puntos por cambio sin refactor, si el área cambia 0,15 veces al mes lo más barato es no refactorizar, con 0,30 es refactorizar al primer cambio y con 1 o más es refactorizar ahora; si aplazar duplica el costo del refactor, desde 0,30 conviene hacerlo ahora.",
               ["Cambios por mes", "Nunca", "Ahora", "Al primer cambio", "Gana", "Gana si aplazar duplica el costo"], rows, [140, 120, 120, 190, 190, 190], row_h=40, size=12,
               note="Esperar al primer cambio es una opción: se paga solo si el área se mueve. Deja de convenir cuando aplazar encarece el trabajo (se pierde el contexto) o cuando el área cambia tanto que el pago es seguro. Un área que nunca cambia no merece refactor, aunque se vea fea. Poisson aproximado, 20 000 repeticiones y parámetros supuestos.",
               note_kind="teal", foot=SINT)


def se298_calientes() -> Fig:
    rows = [
        ["Ninguna", "17,8 %", "33,9 %", "36,6 %", "7,4 %"],
        ["Media (0,5)", "37,3 %", "43,1 %", "44,1 %", "8,2 %"],
        ["Total (1,0)", "48,1 %", "48,1 %", "48,1 %", "7,3 %"],
    ]
    return tab("Reducción del interés pagado al refactorizar 5 de 40 archivos según cómo se eligen",
               "Tabla: al refactorizar cinco de cuarenta archivos y reducir su complejidad un 60 por ciento, elegir por complejidad reduce el interés pagado un 17,8 por ciento si la complejidad no se relaciona con los cambios, elegir por cambios un 33,9, y por complejidad por cambios un 36,6; al azar, un 7,4; si ambas coinciden por completo los tres criterios dan 48,1.",
               ["Relación entre complejidad y cambios", "Por complejidad", "Por cambios", "Por complejidad × cambios", "Al azar"], rows, [290, 150, 140, 190, 120], row_h=44, size=12,
               note="El archivo más complejo no es necesariamente el más caro: si nadie lo toca, su deuda no paga interés. Esto es un resultado del modelo, que fija como supuesto que el interés es complejidad por cambios: con otro supuesto el orden de los criterios puede cambiar. 400 repeticiones con semilla fija.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-299
def se299_pasos() -> Fig:
    rows = [
        ["1. Extraer zona y peso", "0"],
        ["2. Extraer opciones, cupón y redondeo", "0"],
        ["3. Simplificar «urgente == True» a «if urgente»", "142 (urgente = 2 o «si»)"],
        ["4. Cambiar el redondeo histórico por round()", "257 (106 con urgente booleano)"],
    ]
    return tab("Entradas del maestro dorado (3000) cuyo resultado cambia en cada paso del refactor",
               "Tabla: al contrastar con 3000 entradas registradas de una función heredada, extraer funciones no cambia ningún resultado en los pasos 1 y 2; simplificar una comparación con True cambia 142 resultados cuando el parámetro llega como 2 o como una cadena; sustituir el redondeo histórico por round cambia 257 resultados, 106 de ellos con parámetros booleanos.",
               ["Paso", "Entradas que difieren"], rows, [560, 340], row_h=44, size=13,
               note="Los dos pasos que parecían simplificaciones cambiaron comportamiento: el primero con entradas que la función aceptaba sin documentar, el segundo con la diferencia entre sumar 0,5 y redondear al par. Hay que decidir caso por caso si el comportamiento se conserva o se corrige. Entradas sintéticas con semilla fija.",
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
    rows = [
        ["3", "67,4 %", "52,4 %"],
        ["10", "88,7 %", "78,6 %"],
        ["30", "94,9 %", "90,5 %"],
        ["100", "96,0 %", "90,5 %"],
        ["300", "96,7 %", "95,2 %"],
        ["3000", "100 %", "100 %"],
    ]
    return tab("Arcos de la función heredada alcanzados según el número de entradas registradas",
               "Tabla: con 3 entradas registradas al azar se alcanza en promedio el 67,4 por ciento de los arcos de la función heredada y como mínimo el 52,4; con 30, el 94,9 por ciento; con 300, el 96,7 con un mínimo de 95,2, y solo con las 3000 entradas se alcanzan todos.",
               ["Entradas registradas", "Arcos alcanzados (media)", "Mínimo de 30 muestras"], rows, [260, 320, 310], row_h=40, size=13,
               note="Los primeros diez casos rinden mucho y los últimos arcos cuestan miles: los caminos raros (el cupón de envío gratis fuera de zona, el piso en cero) casi no aparecen al azar. Hay que ir a buscarlos. Tras el paso 2, la función de 15 de complejidad queda en seis funciones, la mayor con 4.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-300
def se300_firma() -> Fig:
    rows = [
        ["Añadir un parámetro opcional al final", "compatible", "0", "acierta"],
        ["Añadir un parámetro obligatorio solo por nombre", "rompe", "8", "acierta"],
        ["Eliminar un parámetro", "rompe", "3", "acierta"],
        ["Renombrar un parámetro", "rompe", "2", "acierta"],
        ["Reordenar parámetros", "rompe", "4", "acierta"],
        ["Cambiar el valor por defecto", "compatible", "3", "no lo ve"],
        ["Reescribir sin cambio observable", "compatible", "0", "acierta"],
        ["Cambiar el redondeo", "compatible", "5", "no lo ve"],
        ["Pasar un parámetro a solo por nombre", "rompe", "1", "acierta"],
        ["Rechazar pesos mayores de 30", "compatible", "2", "no lo ve"],
        ["Añadir un valor al campo estado", "compatible", "1", "no lo ve"],
        ["Añadir un campo notas a la respuesta", "compatible", "1", "no lo ve"],
    ]
    return tab("Doce cambios de una función pública: verificador por firma frente a 8 consumidores",
               "Tabla: un verificador que compara solo la firma de una función acierta siete de los doce cambios y no ve cinco que rompen a entre uno y cinco de ocho consumidores: cambiar el valor por defecto, cambiar el redondeo, rechazar pesos altos, añadir un valor a un campo y añadir un campo a la respuesta; no hubo falsas alarmas.",
               ["Cambio", "Firma dice", "Consumidores rotos (de 8)", "Veredicto"], rows, [430, 150, 210, 130], row_h=34, size=12,
               note="Cinco de diez cambios con efecto real no cambian la firma: el verificador por firma es necesario y no suficiente. Los consumidores son ocho funciones sintéticas con estilos de llamada distintos; su cobertura es del autor y una compatibilidad semántica real exige consumidores reales.",
               note_kind="coral", foot=SINT)


def se300_deprecacion() -> Fig:
    rows = [
        ["8", "46,2 %", "269 (53,8 %)"],
        ["12", "57,6 %", "212 (42,4 %)"],
        ["26", "68,4 %", "158 (31,6 %)"],
        ["52", "72,6 %", "137 (27,4 %)"],
        ["104", "74,2 %", "129 (25,8 %)"],
    ]
    return tab("Retirar la versión antigua: clientes migrados y clientes rotos (500 clientes, parámetros supuestos)",
               "Tabla: si 500 clientes sintéticos migran con una mediana de 6 semanas, el 10 por ciento nunca migra y el 15 por ciento solo reacciona cuando se rompe, retirar la versión antigua a la semana 12 rompe a 212 y a la semana 104 todavía a 129; esperar no lleva a cero.",
               ["Semana de retirada", "Ya migraron", "Se rompen al retirar"], rows, [310, 270, 310], row_h=40, size=13,
               note="El 75 % de los diligentes migra en 11,3 semanas, el 95 % en 36,3 y el 99 % en 72,4, pero el 25,6 % de los clientes (abandonados y reactivos) nunca migrará solo. Una ventana larga cuesta mantenimiento en paralelo y no elimina el riesgo; la fecha de retirada es una decisión de producto con aviso. Todos los porcentajes son supuestos.",
               note_kind="gold", foot=SINT)


def se300_contratos() -> Fig:
    rows = [
        ["Cambios probados (5 tipos × campos)", "54"],
        ["Rompen a algún consumidor", "23"],
        ["Los detecta la suite del proveedor (comprueba 4 campos de 12)", "9 de 23"],
        ["Los detectan las pruebas de contrato de los 8 consumidores", "23 de 23"],
        ["Los que no ve el proveedor", "14 de 23"],
        ["Alarmas de un esquema exacto (campos añadidos, quitados o renombrados)", "36, de ellas 16 sin consumidor afectado"],
    ]
    return tab("Cambios de una respuesta de 12 campos: quién los detecta",
               "Tabla: de 54 cambios probados sobre una respuesta con doce campos, 23 rompen a algún consumidor; la suite del proveedor, que comprueba cuatro campos, detecta 9; las pruebas de contrato de los ocho consumidores detectan los 23; un esquema exacto da 36 alarmas, 16 de ellas sin ningún consumidor afectado.",
               ["Medida", "Resultado"], rows, [610, 300], row_h=52, size=13,
               note="El contrato dirigido por el consumidor acierta porque cada consumidor declara lo que lee: añadir un campo no alarma y quitar uno que nadie usa tampoco. Los diez campos que algún consumidor lee son los que pesan. Ocho consumidores sintéticos que leen entre 2 y 4 campos con semilla fija; la detección de contratos es 100 % por construcción del modelo.",
               note_kind="teal", foot=SINT)


FIGURES = {
    "se-295-puntuacion-de-mutacion.svg": se295_mutacion,
    "se-295-cobertura-frente-a-mutacion.svg": se295_cobertura,
    "se-295-tamano-del-paso.svg": se295_paso,
    "se-296-modulos-tocados-por-cambio.svg": se296_modulos,
    "se-296-reloj-real-e-inyectado.svg": se296_reloj,
    "se-296-correlacion-de-registros.svg": se296_registros,
    "se-297-la-misma-regla-en-dos-formas.svg": se297_forma,
    "se-297-cobertura-por-pares.svg": se297_pares,
    "se-297-ciclomatica-y-cognitiva.svg": se297_cognitiva,
    "se-298-politicas-de-pago-e-interes.svg": se298_politicas,
    "se-298-refactorizar-ahora-o-despues.svg": se298_opcion,
    "se-298-puntos-calientes.svg": se298_calientes,
    "se-299-maestro-dorado-por-pasos.svg": se299_pasos,
    "se-299-entradas-que-matan-mutantes.svg": se299_mutantes,
    "se-299-cobertura-segun-entradas.svg": se299_arcos,
    "se-300-firma-frente-a-comportamiento.svg": se300_firma,
    "se-300-ventana-de-deprecacion.svg": se300_deprecacion,
    "se-300-contratos-de-consumidor.svg": se300_contratos,
}
