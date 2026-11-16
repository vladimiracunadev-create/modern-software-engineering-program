"""Figures for SE-139 to SE-144 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, line_chart, percentile_intervals, stacked_bars
from figures_part07_a import bars
from figures_part10_a import SINT


# ---------------------------------------------------------------- SE-139
def se139_guardrail() -> Fig:
    return line_chart(
        "Optimizar solo la métrica norte frente a optimizarla con guarda de quejas",
        "Líneas con las entregas a tiempo y las quejas según los recordatorios por semana: las entregas suben de 61,5 a 95,4 por ciento con ocho recordatorios y las quejas de 0,9 a 26,2; con una guarda de quejas de a lo sumo 3 por ciento el mejor punto es de dos recordatorios, con 70,0 por ciento de entregas.",
        [("Entregas a tiempo (métrica norte)", [(0, 61.5), (2, 70.0), (4, 80.2), (6, 89.5), (8, 95.4), (10, 95.1, "95,1", "b")], "teal"),
         ("Quejas (métrica contraria)", [(0, 0.9), (2, 2.4), (4, 7.5), (6, 15.4), (8, 26.2), (10, 39.8)], "coral")],
        x_label="Recordatorios por semana", y_label="Porcentaje de personas", x_ticks=[(0, "0"), (2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10")],
        decimals=1,
        annotations=[(2, 70.0, "Óptimo con guarda de quejas ≤ 3 %", 60, 95), (8, 95.4, "Óptimo si solo se mira el norte", -90, 62)],
        note="5 000 personas por nivel. Quien optimiza el norte pasa de 2 a 8 recordatorios: gana 25 puntos de entregas y suma 24 puntos de quejas. La relación entre recordatorios, entregas y quejas es una suposición del autor; lo que se mide es que, sin la guarda, el optimizador la cruza.", note_kind="coral", foot=SINT)


def se139_alarmas() -> Fig:
    return line_chart(
        "Alarmas falsas al vigilar varias guardas en un experimento sin diferencia",
        "Líneas con el porcentaje de 1000 experimentos sin diferencia real que dan alguna alarma: con un umbral de 0,05 por guarda sube de 4,7 con una guarda a 41,4 con diez y 65,2 con veinte; con el umbral dividido entre el número de guardas se queda cerca de 5 por ciento.",
        [("Cada guarda con α = 0,05", [(1, 4.7), (3, 15.8), (5, 22.1), (10, 41.4), (20, 65.2)], "coral"),
         ("Cada guarda con α = 0,05 / K", [(1, 4.7, "4,7", "b"), (3, 5.1, "5,1", "b"), (5, 5.1, "5,1", "b"), (10, 5.1, "5,1", "b"), (20, 5.3, "5,3", "b")], "teal")],
        x_label="Número de guardas vigiladas (K)", y_label="Experimentos con alguna alarma (%)", x_ticks=[(1, "1"), (3, "3"), (5, "5"), (10, "10"), (20, "20")],
        decimals=1,
        note="La corrección tiene un precio: con 800 personas por brazo y un daño real de 0,15 desviaciones, la potencia baja de 85,4 % (α = 0,05) a 59,0 % (α = 0,005). Vigilar mucho sin corregir produce alarmas inútiles; corregir sin aumentar la muestra deja pasar daños reales.", note_kind="gold", foot=SINT)


def se139_descomposicion() -> Fig:
    return dumbbell(
        "Métrica norte = alcance × frecuencia × éxito: parte del cambio que explica cada factor",
        "Barras con la parte del cambio de la métrica norte (de 22 568 a 26 220, más 16,2 por ciento) que explica cada factor en logaritmos: el alcance 93,2 por ciento, la frecuencia menos 21,9 y el éxito 28,7; suman 100.",
        [("Alcance (+15,0 %)", 0, 93.2), ("Frecuencia (−3,2 %)", 0, -21.9), ("Éxito (+4,4 %)", 0, 28.7)],
        unit="Parte del cambio (% del cambio total, en logaritmos)", names=("Sin aporte (0)", "Parte que explica"), lower_is_better=False, decimals=1, label_w=190,
        note="Total: 22 568 a 26 220. La descomposición logarítmica suma 100 % sin depender del orden; la sustitución secuencial da rangos. Con 3 % de error en cada lectura, el factor principal cambia en 8,5 % de los casos: es robusto aquí, pero no en cambios pequeños.", note_kind="gold", foot="Cálculo determinista y simulación de ruido con semilla fija.")


# ---------------------------------------------------------------- SE-140
def se140_volumen() -> Fig:
    items = [("100 000 resultados al mes", 32.0, "coral", "32,0"), ("500 000", 8.0, "gold", "8,0"),
             ("1 000 000", 5.0, "teal", "5,0"), ("5 000 000", 2.6, "teal", "2,6")]
    return bars("Costo por cada 1 000 resultados según el volumen mensual",
                "Barras del costo por mil entregas aceptadas con costo fijo de 3 000 y 0,002 por intento: 32,0 con cien mil resultados al mes, 8,0 con quinientos mil, 5,0 con un millón y 2,6 con cinco millones.",
                items, 11, "Con un millón de solicitudes al mes, subir de 0 % a 30 % de fallas con hasta tres intentos eleva el costo por mil resultados de 5,00 a 5,94 (+18,8 %) y deja 2,8 % sin resultado. El costo por resultado se mueve por el volumen y por las fallas: un costo por solicitud oculta ambos.",
                label_w=310, width=940, note_kind="gold", foot="Cálculo determinista y simulación con semilla fija; precios ficticios.")


def se140_reparto() -> Fig:
    return grouped_bars(
        "Tres reglas para repartir un costo compartido de 850",
        "Barras agrupadas con lo que paga cada centro (cargas 40, 35 y 120) con tres reglas, junto a su costo si estuviera solo: el reparto igualitario cobra 283 a cada uno, el proporcional 174, 153 y 523, y el valor de Shapley 150, 150 y 550.",
        ["Centro A (carga 40)", "Centro B (carga 35)", "Centro C (carga 120)"],
        [("Costo si estuviera solo", [450, 450, 850], "grey"), ("Igualitario", [283, 283, 283], "gold"),
         ("Proporcional", [174, 153, 523], "coral"), ("Shapley", [150, 150, 550], "teal")],
        unit="Costo asignado (unidades ficticias)",
        note="El costo es escalonado: 50 de base y 400 por cada tramo de 100 unidades. A y B caben juntos en un tramo; el proporcional cobra 174 y 153 aunque sus cargas no cambian el costo; Shapley cobra lo mismo a ambos. Con tres centros hay 6 órdenes de llegada, con quince hay más de 1,3 billones: el cálculo exacto no escala.", note_kind="gold", foot="Cálculo exacto con tres participantes; cifras ficticias.")


def se140_compromiso() -> Fig:
    return line_chart(
        "Comprometer capacidad: costo medio, riesgo y caída de la demanda",
        "Líneas con el costo anual según la capacidad comprometida: el costo medio baja de 1 257 sin compromiso a 946 con 90 y sube a 1 136 con 140; el percentil 95 baja de 1 859 a 1 366; si la demanda cae 40 por ciento, con compromiso de 100 el costo es 791, más que sin compromiso (754).",
        [("Costo medio", [(0, 1257), (60, 1011), (90, 946), (100, 955), (140, 1136)], "teal"),
         ("Percentil 95", [(0, 1859), (60, 1607), (90, 1481), (100, 1441), (140, 1366)], "gold"),
         ("Costo medio si la demanda cae 40 %", [(0, 754), (60, 573), (100, 791)], "coral")],
        x_label="Capacidad comprometida (unidades)", y_label="Costo anual (unidades ficticias)",
        x_ticks=[(0, "0"), (60, "60"), (90, "90"), (100, "100"), (140, "140")], y_zero=False,
        note="Precio a demanda 1,0 y comprometido 0,65 por unidad pagado siempre (utilización de equilibrio 65 %). Comprometer cerca de la demanda esperada ahorra 25 %; comprometer de más sube el costo medio, y una caída persistente anula el ahorro. Es un modelo con trayectoria aleatoria simple; no representa a ningún proveedor.", note_kind="gold", foot="10 000 trayectorias con semilla fija; precios ficticios.")


# ---------------------------------------------------------------- SE-141
def se141_cartera() -> Fig:
    return percentile_intervals(
        "Retorno neto de la cartera óptima en 400 sorteos de retornos",
        "Intervalo con el retorno neto de la cartera óptima por valor esperado (I04, I05, I06 e I10; costo 100 y retorno esperado 211,5): el percentil 5 es 56,1, la mediana 112,0 y el percentil 95 176,6, y en ningún sorteo es negativo; sin embargo esa cartera es la mejor solo en 7,5 por ciento de los sorteos y su arrepentimiento medio es 36,4.",
        [("Cartera óptima (400 sorteos)", [56.1, 112.0, 176.6])],
        unit="Retorno neto (unidades ficticias)", marks=("p5", "mediana", "p95"), decimals=1, ref_lines=[(0, "retorno neto = 0")], label_w=240,
        note="Por cuatro iniciativas con retorno alto, la cartera es buena casi siempre, pero no es «la mejor»: había 748 combinaciones factibles dentro del presupuesto. Pedir la cartera óptima y comprobar el arrepentimiento son preguntas distintas; la segunda es la que importa para decidir.", note_kind="gold", foot=SINT)


def se141_piloto() -> Fig:
    items = [("Todo de una vez (exacto)", 24.0, "coral", "−24,0"), ("Con piloto de exactitud 0,5", 21.9, "coral", "−21,9"),
             ("Piloto de exactitud 0,7", 8.3, "coral", "−8,3"), ("Piloto de exactitud 0,8", 1.6, "gold", "−1,6"),
             ("Piloto de exactitud 0,9", 5.3, "teal", "+5,3"), ("Piloto perfecto", 12.0, "teal", "+12,0")]
    return bars("Valor esperado de invertir por etapas según la exactitud del piloto",
                "Barras del valor esperado: invertir todo de una vez pierde 24,0; con un piloto de exactitud 0,5 pierde 21,9, con 0,7 pierde 8,3, con 0,8 pierde 1,6, con 0,9 gana 5,3 y con un piloto perfecto gana 12,0.",
                items, 15, "Mercado bueno con probabilidad 0,4: rinde 180 si es bueno y 40 si no; todo cuesta 120; el piloto cuesta 20 y el resto 100. La opción de esperar convierte una apuesta perdedora en ganadora solo si el piloto distingue bien (equilibrio cerca de 0,82). Un piloto de azar pierde el costo del piloto sin ganar información.",
                label_w=320, width=940, note_kind="gold", foot="Esperanza exacta y simulación de 100 000 casos con semilla fija; cifras ficticias.")


def se141_secuencia() -> Fig:
    return grouped_bars(
        "Secuenciar con dependencias: valor presente del mejor, el voraz y el peor orden válido",
        "Barras horizontales con el valor presente a 24 meses de tres órdenes de siete iniciativas: el mejor vale 551,5; el voraz por valor sobre duración vale 539,5 (2,2 por ciento menos) y el peor 514,3 (6,7 por ciento menos); solo 63 de 5 040 órdenes respetan las dependencias.",
        ["Mejor: A B C D G E F", "Voraz: E F A B C D G (−2,2 %)", "Peor: C A E F B D G (−6,7 %)"],
        [("Valor presente a 24 meses", [551.5, 539.5, 514.3], "teal")],
        unit="Valor presente (unidades ficticias)", horizontal=True, decimals=1, label_w=250,
        note="El voraz empieza por E y F (valor por mes alto) y retrasa A, B y D, que desbloquean la iniciativa más valiosa. Elegir por valor propio ignora lo que una iniciativa habilita; con pocas dependencias el error es pequeño, y con muchas puede ser mayor. Tasa de descuento 1 % al mes.", note_kind="gold", foot="Enumeración exhaustiva con valores ficticios.")


# ---------------------------------------------------------------- SE-142
def se142_umbral() -> Fig:
    return line_chart(
        "Cuándo conviene probar con vuelta atrás en lugar de comprometerse",
        "Líneas con la pérdida esperada de la decisión irreversible y de la reversible según la probabilidad de equivocarse: con 2 por ciento conviene la irreversible (2,0 frente a 4,4), con 5 por ciento empatan en cerca de 5, y con 10 y 30 por ciento conviene la reversible (6,0 frente a 9,9 y 9,9 frente a 30,3).",
        [("Irreversible", [(2, 2.0, "", "r"), (5, 5.0, "", "t"), (10, 9.9), (30, 30.3)], "coral"),
         ("Reversible (4 + 20·p)", [(2, 4.4), (5, 4.9, "", "b"), (10, 6.0, "", "b"), (30, 9.9, "", "b")], "teal")],
        x_label="Probabilidad de equivocarse (%)", y_label="Pérdida esperada (unidades ficticias)", x_ticks=[(2, "2"), (5, "5"), (10, "10"), (30, "30")], decimals=1,
        annotations=[(5, 5.0, "Umbral p* = 5,0 %", 60, -60)],
        note="Umbral p* = costo de probar / (pérdida irreversible − costo de revertir) = 4 / (100 − 20) = 5,0 %. Con costo de revertir 5 es 4,2 % y con 50 es 8,0 %. Los tres números son supuestos; la lección es que la probabilidad de equivocarse decide, y casi nunca se conoce con precisión.", note_kind="gold", foot="Simulación de 40 000 casos por fila, semilla fija.")


def se142_migraciones() -> Fig:
    return grouped_bars(
        "Migraciones de base de datos: filas idénticas tras ida y vuelta (10 000 filas)",
        "Barras horizontales con el porcentaje de filas idénticas tras aplicar y deshacer seis migraciones: añadir una columna, renombrar y partir el nombre devuelven 100 por ciento; pasar el precio a centavos devuelve 9,5; borrar una columna y sustituir el correo por su hash, 0.",
        ["Añadir una columna y quitarla", "Renombrar una columna", "Partir el nombre y reunirlo", "Precio decimal a centavos", "Borrar y recrear una columna", "Correo por su hash"],
        [("Filas idénticas", [100.0, 100.0, 100.0, 9.5, 0.0, 0.0], "teal")],
        unit="Filas idénticas tras ida y vuelta (%)", horizontal=True, decimals=1, label_w=230,
        note="Que el script «down» exista no hace reversible la migración: la reversibilidad se mide comparando datos antes y después. La partición del nombre recupera el texto pero la información que se creó (nombre y apellido) era errónea en 28,8 % de las filas. SQLite 3.45.3 en Windows y 3.45.1 en Ubuntu; mismos resultados.", note_kind="coral", foot="Datos sintéticos (correos .test); código real con sqlite3 de la biblioteca estándar.")


def se142_progresivo() -> Fig:
    return grouped_bars(
        "Personas afectadas por un defecto: todo de golpe o por etapas (200 000 personas)",
        "Barras en escala logarítmica con las personas afectadas por un defecto: con 5 por ciento de tasa, 9 952 si se despliega de golpe y 87 por etapas; con 1 por ciento, 1 995 y 102; con 0,2 por ciento, 392 y 98.",
        ["Defecto de 5 % (se detecta en la etapa de 1 %)", "Defecto de 1 % (etapa de 5 %)", "Defecto de 0,2 % (etapa de 25 %)"],
        [("Todo de golpe", [9952, 1995, 392], "coral"), ("Por etapas", [87, 102, 98], "teal")],
        unit="Personas afectadas", log=True, horizontal=True, label_w=290,
        note="Etapas de 1, 5, 25 y 100 %; se detecta al reunir al menos 10 reportes, y 15 % de las personas afectadas reporta. Cuanto más raro es el defecto, más tarde se ve y más importa la última etapa; con 0,05 % se esperan unos 4 reportes en la etapa de 25 % y el umbral de 10 no se alcanza hasta el 100 % (cuenta esperada, no simulada).", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-143
def se143_validador() -> Fig:
    return stacked_bars(
        "Validador del árbol de métricas: 12 de 16 mutaciones detectadas",
        "Barras apiladas de las 16 mutaciones por tipo de defecto: el validador detecta 4 de 4 de estructura, 1 de 1 de referencias, 4 de 4 de completitud, 2 de 2 de aritmética y 1 de 1 de nombre de vanidad, y deja pasar las 4 semánticas: unidad cambiada, fuente irrelevante, responsable colectivo y valores coherentes.",
        ["Estructura (4)", "Referencias (1)", "Completitud (4)", "Aritmética (2)", "Nombre de vanidad (1)", "Unidad cambiada (1)", "Fuente irrelevante (1)", "Responsable colectivo (1)", "Hoja y raíz coherentes (1)"],
        [("Detectadas", [4, 1, 4, 2, 1, 0, 0, 0, 0], "teal"), ("Sobreviven", [0, 0, 0, 0, 0, 1, 1, 1, 1], "coral")],
        unit="Mutaciones", horizontal=True, label_w=220, plot_h=300,
        note="Con casos nuevos: un árbol aditivo y uno con cociente pasan; un cociente con divisor cero se rechaza como fórmula inválida; una fórmula con constante que no cuadra se rechaza. El validador comprueba forma y aritmética; no sabe si «entregas por estudiante» está medida con la misma unidad que el padre.", note_kind="coral", foot="Código real ejecutado; idéntico en Windows y Ubuntu (WSL2).")


def se143_aditiva() -> Fig:
    return line_chart(
        "Tres factores que suben lo mismo: cambio exacto frente a suma de porcentajes",
        "Líneas con el cambio del padre cuando los tres factores de un producto suben el mismo porcentaje: el cambio exacto es 6,12 con 2 por ciento y 237,50 con 50, y la suma de los porcentajes da 6 y 150, es decir 98,0 y 63,2 por ciento del cambio real.",
        [("Cambio exacto del padre", [(2, 6.12, "", "t"), (5, 15.76), (10, 33.10), (20, 72.80), (50, 237.5)], "teal"),
         ("Suma de los porcentajes", [(2, 6.0, "", "b"), (5, 15.0), (10, 30.0), (20, 60.0), (50, 150.0)], "coral")],
        x_label="Subida de cada uno de los tres factores (%)", y_label="Cambio del padre (%)", point_labels="last",
        x_ticks=[(2, "2"), (5, "5"), (10, "10"), (20, "20"), (50, "50")],
        note="Con signos mezclados la suma engaña más: +50 % y −30 % dan +5 % exacto y +20 % por suma. Y cuando el cambio total es casi cero, las participaciones logarítmicas explotan (+831 % y −731 %): no se informan participaciones de un cambio de 5 %. Una atribución sin orden ni aviso de límites se convierte en relato.", note_kind="coral", foot="Cálculo determinista.")


def se143_hoja() -> Fig:
    items = [("Tasa de entregas aceptadas", 87.1, "teal", "87,1 %"), ("Entregas por API", 6.9, "gold", "6,9 %"),
             ("Estudiantes por centro", 6.0, "gold", "6,0 %"), ("Entregas por estudiante", 0.0, "grey", "0 %"), ("Centros activos", 0.0, "grey", "0 %")]
    return bars("Qué hoja conviene mover primero, según el costo, con baselines inciertos",
                "Barras con la proporción de 10 000 sorteos de baselines en que cada hoja queda primera en efecto por costo: la tasa de entregas aceptadas 87,1 por ciento, entregas por API 6,9, estudiantes por centro 6,0, y entregas por estudiante y centros activos ninguna.",
                items, 4.4, "Raíz = centros × estudiantes × entregas × tasa + entregas por API; subir cualquier hoja multiplicativa 10 % mueve la raíz lo mismo, y el orden lo decide el costo de lograrlo (30, 10, 15, 8 y 5 semanas-persona, supuestos). La tasa es primera porque su costo es bajo y su techo no es 10 %: se limita a (1 − tasa).",
                label_w=300, width=940, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-144
def se144_tornado() -> Fig:
    items = [("Alumnos por centro", 1367, "coral", "1 367"), ("Precio por alumno", 966, "coral", "966"),
             ("Centros nuevos por mes", 519, "gold", "519"), ("Costo de servir por alumno", 401, "gold", "401"),
             ("Costos fijos mensuales", 234, "teal", "234"), ("Abandono mensual", 191, "teal", "191"), ("Costo de construcción", 158, "teal", "158")]
    return bars("Cuánto mueve cada supuesto el valor presente neto (miles, percentil 10 a 90)",
                "Barras con la oscilación del valor presente neto al llevar cada supuesto de su percentil 10 al 90 con los demás en su valor central: alumnos por centro 1367 mil, precio por alumno 966, centros nuevos por mes 519, costo de servir 401, costos fijos 234, abandono 191 y construcción 158.",
                items, 0.22, "El valor presente neto es 34 mil con valores centrales; en 20 000 sorteos la mediana es 459 mil, el intervalo del 5 al 95 por ciento va de −470 mil a 2 962 mil y la probabilidad de un valor positivo es 72,9 %. El supuesto que menos se investiga (tamaño de los centros) es el que más mueve el caso; la construcción, que domina la conversación, es el que menos.",
                label_w=300, width=940, note_kind="gold", foot=SINT)


def se144_compuerta() -> Fig:
    return line_chart(
        "Compuerta de abandono al mes 6: proyectos malos que continúan frente a buenos detenidos por error",
        "Líneas según el umbral de centros activos al mes 6: los proyectos malos que continúan bajan de 27,5 por ciento sin compuerta a 9,7 con 30 centros, mientras los buenos detenidos por error suben de 0,0 con 10 a 32,4; con 20 centros son 20,8 y 8,0. El valor esperado cae de 746,4 a 397,0 miles.",
        [("Malos que continúan", [(0, 27.5), (10, 27.4), (15, 25.6), (20, 20.8), (25, 15.1), (30, 9.7)], "gold"),
         ("Buenos detenidos por error", [(10, 0.0), (15, 1.7), (20, 8.0), (25, 18.7), (30, 32.4)], "coral")],
        x_label="Umbral de centros activos al mes 6 (0 = sin compuerta)", y_label="Proyectos (%)", decimals=1,
        x_ticks=[(0, "sin"), (10, "10"), (15, "15"), (20, "20"), (25, "25"), (30, "30")],
        note="En este modelo ninguna compuerta aumentó el valor esperado: lo que compra es reducir los proyectos malos que siguen (27,5 % a 9,7 %) a cambio de detener algunos buenos. Con 30 % de la construcción antes de la compuerta el resultado es parecido. Fijar el umbral exige decidir cuánto riesgo vale esa pérdida esperada.", note_kind="coral", foot=SINT)


def se144_validador() -> Fig:
    return stacked_bars(
        "Validador del caso de viabilidad: 12 de 16 mutaciones detectadas",
        "Barras apiladas de las 16 mutaciones: el validador detecta 5 de 5 de estructura y completitud, 3 de 3 de coherencia y 4 de 4 de trazabilidad, y deja pasar 4: un número alterado de forma coherente, una exageración sin palabras prohibidas, una evidencia irrelevante y una probabilidad inflada.",
        ["Estructura y completitud (5)", "Coherencia (3)", "Trazabilidad (4)", "Número alterado coherente (1)", "Exageración sin palabras prohibidas (1)", "Evidencia irrelevante (1)", "Probabilidad inflada (1)"],
        [("Detectadas", [5, 3, 4, 0, 0, 0, 0], "teal"), ("Sobreviven", [0, 0, 0, 1, 1, 1, 1], "coral")],
        unit="Mutaciones", horizontal=True, label_w=270, plot_h=280,
        note="Es el mismo reparto que el de un brief: la forma se comprueba, la verdad no. Para los cuatro supervivientes hace falta una segunda persona que recalcule el modelo y compare cada afirmación con su evidencia. El validador es una puerta de entrada a esa revisión, no su sustituto.", note_kind="coral", foot="Código real ejecutado; idéntico en Windows y Ubuntu (WSL2).")


FIGURES = {
    "se-139-norte-con-y-sin-guarda.svg": se139_guardrail,
    "se-139-alarmas-falsas-con-varias-guardas.svg": se139_alarmas,
    "se-139-descomposicion-de-la-metrica-norte.svg": se139_descomposicion,
    "se-140-costo-por-resultado-y-volumen.svg": se140_volumen,
    "se-140-reparto-del-costo-compartido.svg": se140_reparto,
    "se-140-compromiso-de-capacidad.svg": se140_compromiso,
    "se-141-cartera-y-arrepentimiento.svg": se141_cartera,
    "se-141-valor-del-piloto.svg": se141_piloto,
    "se-141-secuencias-con-dependencias.svg": se141_secuencia,
    "se-142-umbral-de-reversibilidad.svg": se142_umbral,
    "se-142-ida-y-vuelta-en-migraciones.svg": se142_migraciones,
    "se-142-despliegue-progresivo.svg": se142_progresivo,
    "se-143-validador-del-arbol-de-metricas.svg": se143_validador,
    "se-143-suma-de-porcentajes-frente-a-exacto.svg": se143_aditiva,
    "se-143-que-hoja-mover-primero.svg": se143_hoja,
    "se-144-oscilacion-del-vpn-por-supuesto.svg": se144_tornado,
    "se-144-compuerta-de-abandono.svg": se144_compuerta,
    "se-144-validador-del-caso.svg": se144_validador,
}
