"""Figures for SE-139 to SE-144 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab
from figures_part10_a import SINT


# ---------------------------------------------------------------- SE-139
def se139_guardrail() -> Fig:
    rows = [["0", "61,5 %", "0,9 %", ""], ["2", "70,0 %", "2,4 %", "óptimo con guarda de quejas ≤ 3 %"],
            ["4", "80,2 %", "7,5 %", ""], ["6", "89,5 %", "15,4 %", ""], ["8", "95,4 %", "26,2 %", "óptimo si solo se mira el norte"],
            ["10", "95,1 %", "39,8 %", "el norte ya no sube"]]
    return tab("Optimizar solo la métrica norte frente a optimizarla con guarda",
               "Tabla de recordatorios por semana: las entregas a tiempo suben de 61,5 a 95,4 por ciento con ocho recordatorios y las quejas de 0,9 a 26,2; con una guarda de quejas de a lo sumo 3 por ciento el mejor punto es de dos recordatorios, con 70,0 por ciento de entregas.",
               ["Recordatorios por semana", "Entregas a tiempo (métrica norte)", "Quejas (métrica contraria)", "Decisión"], rows, [190, 260, 230, 260], row_h=42, size=13,
               note="5 000 personas por nivel. Quien optimiza el norte pasa de 2 a 8 recordatorios: gana 25 puntos de entregas y suma 24 puntos de quejas. La relación entre recordatorios, entregas y quejas es una suposición del autor; lo que se mide es que, sin la guarda, el optimizador la cruza.", note_kind="coral", foot=SINT)


def se139_alarmas() -> Fig:
    rows = [["1", "4,7 %", "5,0 %", "4,7 %"], ["3", "15,8 %", "14,3 %", "5,1 %"], ["5", "22,1 %", "22,6 %", "5,1 %"],
            ["10", "41,4 %", "40,1 %", "5,1 %"], ["20", "65,2 %", "64,2 %", "5,3 %"]]
    return tab("Alarmas falsas al vigilar varias guardas en un experimento sin diferencia",
               "Tabla de 1000 experimentos sin diferencia real: con una guarda, 4,7 por ciento dan alarma; con diez, 41,4; con veinte, 65,2. Dividir el umbral entre el número de guardas devuelve la tasa a cerca de 5 por ciento.",
               ["Número de guardas", "Alguna alarma con α = 0,05 cada una", "Teoría 1 − 0,95^K", "Alguna alarma con α = 0,05/K"], rows, [190, 290, 230, 260], row_h=42, size=13,
               note="La corrección tiene un precio: con 800 personas por brazo y un daño real de 0,15 desviaciones, la potencia baja de 85,4 % (α = 0,05) a 59,0 % (α = 0,005). Vigilar mucho sin corregir produce alarmas inútiles; corregir sin aumentar la muestra deja pasar daños reales.", note_kind="gold", foot=SINT)


def se139_descomposicion() -> Fig:
    rows = [["Alcance (centros o estudiantes activos)", "8 000 a 9 200 (+15,0 %)", "93,2 %", "3 276 a 3 534"],
            ["Frecuencia (entregas por activo)", "3,1 a 3,0 (−3,2 %)", "−21,9 %", "−874 a −728"],
            ["Éxito (entregas aceptadas)", "0,91 a 0,95 (+4,4 %)", "28,7 %", "960 a 1 141"]]
    return tab("Métrica norte = alcance × frecuencia × éxito: quién explica el cambio",
               "Tabla: la métrica norte pasa de 22 568 a 26 220 (+16,2 por ciento); el alcance explica 93,2 por ciento del cambio en escala logarítmica, la frecuencia resta 21,9 y el éxito suma 28,7. Por sustitución secuencial, la contribución de cada factor depende del orden y varía dentro de un rango.",
               ["Factor", "Cambio", "Parte del cambio (logaritmos)", "Contribución por sustitución (6 órdenes)"], rows, [320, 230, 190, 230], row_h=50, size=13,
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
    rows = [["A (40)", "450", "283", "174", "150"], ["B (35)", "450", "283", "153", "150"], ["C (120)", "850", "283", "523", "550"]]
    return tab("Tres reglas para repartir un costo compartido de 850",
               "Tabla: tres centros con cargas de 40, 35 y 120 comparten una capacidad que cuesta 850; el reparto igualitario cobra 283 a cada uno, el proporcional 174, 153 y 523, y el valor de Shapley 150, 150 y 550.",
               ["Centro (carga)", "Costo si estuviera solo", "Reparto igualitario", "Reparto proporcional", "Valor de Shapley"], rows, [200, 210, 190, 210, 190], row_h=50, size=13,
               note="El costo es escalonado: 50 de base y 400 por cada tramo de 100 unidades. A y B caben juntos en un tramo; el proporcional cobra 174 y 153 aunque sus cargas no cambian el costo; Shapley cobra lo mismo a ambos. Con tres centros hay 6 órdenes de llegada, con quince hay más de 1,3 billones: el cálculo exacto no escala.", note_kind="gold", foot="Cálculo exacto con tres participantes; cifras ficticias.")


def se140_compromiso() -> Fig:
    rows = [["0 (todo a demanda)", "1 257", "1 859", "754"], ["60", "1 011", "1 607", "573"],
            ["90 (mejor en promedio)", "946", "1 481", "—"], ["100", "955", "1 441", "791"], ["140", "1 136", "1 366", "—"]]
    return tab("Comprometer capacidad: ahorro medio, riesgo y caída de la demanda",
               "Tabla de doce meses con demanda inicial de 100 unidades y variación mensual de 12 por ciento: sin compromiso el costo medio es 1257 y el percentil 95 es 1859; con compromiso de 90 el costo medio baja a 946; con compromiso de 100 el costo medio es 955 y, si la demanda cae 40 por ciento, el costo es 791, más que sin compromiso (754).",
               ["Capacidad comprometida", "Costo medio anual", "Percentil 95", "Costo medio si la demanda cae 40 %"], rows, [260, 190, 170, 270], row_h=44, size=13,
               note="Precio a demanda 1,0 y comprometido 0,65 por unidad pagado siempre (utilización de equilibrio 65 %). Comprometer cerca de la demanda esperada ahorra 25 %; comprometer de más sube el costo medio, y una caída persistente anula el ahorro. Es un modelo con trayectoria aleatoria simple; no representa a ningún proveedor.", note_kind="gold", foot="10 000 trayectorias con semilla fija; precios ficticios.")


# ---------------------------------------------------------------- SE-141
def se141_cartera() -> Fig:
    rows = [["Cartera óptima por valor esperado (I04, I05, I06, I10)", "costo 100, retorno esperado 211,5"],
            ["Cartera voraz por razón retorno/costo", "la misma cartera"],
            ["Veces que esa cartera es la mejor al sortear retornos (400 sorteos)", "7,5 %"],
            ["Arrepentimiento medio frente a la mejor cartera de cada sorteo", "36,4 (percentil 95: 84,0)"],
            ["Retorno neto de la cartera: p5 / mediana / p95", "56,1 / 112,0 / 176,6"],
            ["Probabilidad de que el retorno neto sea negativo", "0 % (0 de 400 sorteos)"]]
    return tab("Una cartera óptima en el valor esperado casi nunca es la mejor de un sorteo",
               "Tabla: de 12 iniciativas con presupuesto 100, la cartera óptima y la voraz coinciden con retorno esperado 211,5; esa cartera es la mejor solo en 7,5 por ciento de 400 sorteos y su arrepentimiento medio es 36,4; el retorno neto va de 56,1 a 176,6 y nunca fue negativo.",
               ["Medida", "Valor"], rows, [560, 380], row_h=44, size=13,
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
    rows = [["A B C D G E F (mejor)", "551,5", "0,0 %"], ["E F A B C D G (voraz por valor/duración)", "539,5", "−2,2 %"],
            ["C A E F B D G (peor)", "514,3", "−6,7 %"], ["Órdenes válidos / posibles", "63 / 5 040", "—"],
            ["Órdenes a menos de 5 % del mejor / a menos de 1 %", "73 % / 4,8 %", "—"]]
    return tab("Secuenciar con dependencias: 63 órdenes válidos de 5 040 posibles",
               "Tabla de siete iniciativas con dependencias: el mejor orden vale 551,5, el voraz que elige por valor sobre duración vale 539,5 (2,2 por ciento menos) y el peor 514,3 (6,7 por ciento menos); solo 63 de 5040 órdenes respetan las dependencias y 73 por ciento están a menos de 5 por ciento del mejor.",
               ["Orden o medida", "Valor presente (24 meses)", "Diferencia con el mejor"], rows, [470, 250, 220], row_h=44, size=13,
               note="El voraz empieza por E y F (valor por mes alto) y retrasa A, B y D, que desbloquean la iniciativa más valiosa. Elegir por valor propio ignora lo que una iniciativa habilita; con pocas dependencias el error es pequeño, y con muchas puede ser mayor. Tasa de descuento 1 % al mes.", note_kind="gold", foot="Enumeración exhaustiva con valores ficticios.")


# ---------------------------------------------------------------- SE-142
def se142_umbral() -> Fig:
    rows = [["2 %", "2,0", "4,4", "irreversible"], ["5 %", "5,0", "4,9", "cruce (≈ 5,0 %)"], ["10 %", "9,9", "6,0", "reversible"], ["30 %", "30,3", "9,9", "reversible"]]
    return tab("Cuándo conviene probar con vuelta atrás en lugar de comprometerse",
               "Tabla: si equivocarse cuesta 100 en una decisión irreversible, 20 al revertirla y probar cuesta 4, la decisión reversible gana cuando la probabilidad de equivocarse supera 5 por ciento: con 2 por ciento conviene comprometerse y con 10 por ciento conviene probar.",
               ["Probabilidad de equivocarse", "Pérdida esperada si es irreversible", "Pérdida esperada si es reversible (4 + 20·p)", "Conviene"], rows, [210, 240, 280, 210], row_h=50, size=13,
               note="Umbral p* = costo de probar / (pérdida irreversible − costo de revertir) = 4 / (100 − 20) = 5,0 %. Con costo de revertir 5 es 4,2 % y con 50 es 8,0 %. Los tres números son supuestos; la lección es que la probabilidad de equivocarse decide, y casi nunca se conoce con precisión.", note_kind="gold", foot="Simulación de 40 000 casos por fila, semilla fija.")


def se142_migraciones() -> Fig:
    rows = [["Añadir una columna nula y quitarla", "10 000 de 10 000", "reversible"], ["Renombrar una columna y devolverla", "10 000 de 10 000", "reversible"],
            ["Partir el nombre en dos y reunirlo", "10 000 de 10 000", "vuelve el texto, pero 28,8 % de los nombres de pila quedó partido mal"],
            ["Precio decimal a centavos enteros y vuelta", "953 de 10 000 (9,5 %)", "pérdida de precisión"],
            ["Borrar una columna y recrearla", "0 de 10 000", "datos perdidos"], ["Sustituir el correo por su hash", "0 de 10 000", "no se puede deshacer"]]
    return tab("Migraciones de base de datos: qué vuelve al deshacerse",
               "Tabla de seis migraciones sobre 10 000 filas en SQLite: añadir y quitar una columna, renombrar y partir un nombre devuelven todas las filas; pasar el precio a centavos devuelve 9,5 por ciento; borrar una columna y sustituir un correo por su hash no devuelven ninguna.",
               ["Migración y vuelta", "Filas idénticas tras ida y vuelta", "Lectura"], rows, [380, 220, 340], row_h=54, size=12,
               note="Que el script «down» exista no hace reversible la migración: la reversibilidad se mide comparando datos antes y después. La partición del nombre recupera el texto pero la información que se creó (nombre y apellido) era errónea en 28,8 % de las filas. SQLite 3.45.3 en Windows y 3.45.1 en Ubuntu; mismos resultados.", note_kind="coral", foot="Datos sintéticos (correos .test); código real con sqlite3 de la biblioteca estándar.")


def se142_progresivo() -> Fig:
    rows = [["5 %", "9 952", "87", "etapa 1 (1 %)"], ["1 %", "1 995", "102", "etapa 2 (5 %)"], ["0,2 %", "392", "98", "etapa 3 (25 %)"]]
    return tab("Personas afectadas por un defecto: todo de golpe o por etapas",
               "Tabla: con 200 000 personas, un defecto que afecta a 5 por ciento daña a 9952 si se despliega de golpe y a 87 si se detecta en la primera etapa de 1 por ciento; un defecto de 0,2 por ciento daña a 392 de golpe y a 98 si se detecta en la etapa de 25 por ciento.",
               ["Tasa del defecto", "Afectadas, todo de golpe", "Afectadas, por etapas", "Etapa en que se detecta"], rows, [190, 260, 250, 240], row_h=50, size=13,
               note="Etapas de 1, 5, 25 y 100 %; se detecta al reunir al menos 10 reportes, y 15 % de las personas afectadas reporta. Cuanto más raro es el defecto, más tarde se ve y más importa la última etapa; con 0,05 % se esperan unos 4 reportes en la etapa de 25 % y el umbral de 10 no se alcanza hasta el 100 % (cuenta esperada, no simulada).", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-143
def se143_validador() -> Fig:
    rows = [["Estructura: ciclo, huérfano, nombre duplicado, dos raíces", "4 de 4", "detecta"], ["Referencias: fórmula que usa un nodo inexistente", "1 de 1", "detecta"],
            ["Completitud: sin responsable, sin fuente, sin decisión, sin métrica contraria", "4 de 4", "detecta"], ["Aritmética: operador cambiado, valor de hoja alterado 30 %", "2 de 2", "detecta"],
            ["Nombre de métrica de vanidad", "1 de 1", "detecta"], ["Unidad cambiada (semanal a mensual)", "0 de 1", "sobrevive"],
            ["Fuente irrelevante para la métrica", "0 de 1", "sobrevive"], ["Responsable colectivo («el equipo»)", "0 de 1", "sobrevive"],
            ["Hoja y raíz alteradas de forma coherente", "0 de 1", "sobrevive"]]
    return tab("Validador del árbol de métricas: 12 de 16 mutaciones",
               "Tabla de 16 mutaciones de un árbol de cuatro hojas: el validador detecta las 12 de estructura, referencias, completitud, aritmética y nombre de vanidad, y deja pasar las 4 semánticas: unidad cambiada, fuente irrelevante, responsable colectivo y valores alterados de forma coherente.",
               ["Tipo de defecto", "Detectadas", "Resultado"], rows, [600, 150, 150], row_h=40, size=12,
               note="Con casos nuevos: un árbol aditivo y uno con cociente pasan; un cociente con divisor cero se rechaza como fórmula inválida; una fórmula con constante que no cuadra se rechaza. El validador comprueba forma y aritmética; no sabe si «entregas por estudiante» está medida con la misma unidad que el padre.", note_kind="coral", foot="Código real ejecutado; idéntico en Windows y Ubuntu (WSL2).")


def se143_aditiva() -> Fig:
    rows = [["+2 %", "+6,12 %", "+6 %", "98,0 %"], ["+5 %", "+15,76 %", "+15 %", "95,2 %"], ["+10 %", "+33,10 %", "+30 %", "90,6 %"],
            ["+20 %", "+72,80 %", "+60 %", "82,4 %"], ["+50 %", "+237,50 %", "+150 %", "63,2 %"]]
    return tab("Tres factores que suben lo mismo: cambio exacto frente a suma de porcentajes",
               "Tabla: si los tres factores de una métrica multiplicativa suben 2 por ciento el cambio exacto es 6,12 y la suma da 6; si suben 50 por ciento el cambio exacto es 237,5 y la suma da 150, 63 por ciento de lo real.",
               ["Cada factor sube", "Cambio exacto del padre", "Suma de los porcentajes", "Suma sobre exacto"], rows, [200, 260, 260, 220], row_h=42, size=13,
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
    rows = [["sin compuerta", "0 %", "—", "27,5 %", "746,4"], ["10 centros", "0,1 %", "0,0 %", "27,4 %", "746,1"], ["15 centros", "3,6 %", "1,7 %", "25,6 %", "733,9"],
            ["20 centros", "14,6 %", "8,0 %", "20,8 %", "678,8"], ["25 centros", "31,1 %", "18,7 %", "15,1 %", "563,1"], ["30 centros", "50,1 %", "32,4 %", "9,7 %", "397,0"]]
    return tab("Compuerta de abandono al mes 6: riesgo evitado frente a valor esperado perdido",
               "Tabla de 20 000 sorteos: sin compuerta, 27,5 por ciento de los proyectos tienen valor presente neto negativo y el valor esperado es 746 mil; con umbral de 20 centros activos al mes 6 se detiene el 14,6 por ciento, se detienen por error 8,0 por ciento de proyectos buenos y el valor esperado baja a 679 mil.",
               ["Umbral de centros activos", "Proyectos detenidos", "Buenos detenidos por error", "Malos que continúan", "Valor esperado (miles)"], rows, [210, 190, 220, 190, 190], row_h=44, size=13,
               note="En este modelo ninguna compuerta aumentó el valor esperado: lo que compra es reducir los proyectos malos que siguen (27,5 % a 9,7 %) a cambio de detener algunos buenos. Con 30 % de la construcción antes de la compuerta el resultado es parecido. Fijar el umbral exige decidir cuánto riesgo vale esa pérdida esperada.", note_kind="coral", foot=SINT)


def se144_validador() -> Fig:
    rows = [["Estructura y completitud: sin abandono, sin moneda, sin límites, sin ventana del umbral, sin costos de operación", "5 de 5", "detecta"],
            ["Coherencia: rango invertido, percentiles desordenados, total que no cuadra", "3 de 3", "detecta"], ["Trazabilidad: evidencia inexistente, decisión sin responsable o sin fecha, lenguaje de garantía", "4 de 4", "detecta"],
            ["Número alterado de forma coherente (construcción ×2)", "0 de 1", "sobrevive"], ["Exageración sin palabras prohibidas", "0 de 1", "sobrevive"],
            ["Evidencia existente pero irrelevante", "0 de 1", "sobrevive"], ["Probabilidad inflada pero coherente (0,82 a 0,99)", "0 de 1", "sobrevive"]]
    return tab("Validador del caso de viabilidad: 12 de 16 mutaciones",
               "Tabla de 16 mutaciones de un caso de viabilidad: el validador detecta las doce que rompen estructura, coherencia o trazabilidad y deja pasar cuatro: un número alterado de forma coherente, una exageración sin palabras prohibidas, una evidencia irrelevante y una probabilidad inflada.",
               ["Tipo de defecto", "Detectadas", "Resultado"], rows, [650, 130, 130], row_h=56, size=12,
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
