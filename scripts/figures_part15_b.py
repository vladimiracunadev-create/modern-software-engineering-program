"""Figures for SE-187 to SE-192 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-187
def se187_exposicion() -> Fig:
    rows = [
        ["Exposición esperada (suma de probabilidad × impacto)", "21,6", "21,6"],
        ["Media simulada", "21,7", "22,2"],
        ["Mediana", "21", "10"],
        ["Percentil 85", "35", "66"],
        ["Percentil 95", "44", "81"],
    ]
    return tab("Diez riesgos: retraso en días con riesgos independientes y con una causa común",
               "Tabla: la exposición esperada de diez riesgos es 21,6 días; con riesgos independientes la mediana es 21 y el percentil 85 vale 35; con una causa común que arrastra a la mayoría la media casi no cambia, 22,2, pero la mediana baja a 10 y el percentil 85 sube a 66.",
               ["Medida (días de retraso)", "Independientes", "Causa común"], rows, [470, 210, 210], row_h=44, size=13,
               note="La exposición esperada es la misma y el riesgo no: la causa común reparte el retraso entre muchos proyectos buenos y unos pocos desastrosos. El 25 % de probabilidad del evento común y el 70 % de arrastre son supuestos.",
               note_kind="coral", foot=SINT)


def se187_supuestos() -> Fig:
    items = [
        ("Validar en orden arbitrario", 78.7, "coral", "78,7"),
        ("Primero el más barato de validar", 65.4, "gold", "65,4"),
        ("Primero el más caro de fallar", 64.2, "gold", "64,2"),
        ("Primero el mayor coste de fallar por coste de validar", 57.9, "teal", "57,9"),
    ]
    return bars("Coste esperado de descubrir tarde que un supuesto era falso (12 supuestos)",
                "Barras: con 12 supuestos cada uno cierto con probabilidad 0,85, el coste medio de descubrir tarde un supuesto falso es 78,7 con orden arbitrario, 65,4 validando primero el más barato, 64,2 el más caro de fallar y 57,9 ordenando por coste de fallar sobre coste de validar.",
                items, 6.0, "Todos los supuestos ciertos a la vez ocurre solo en 14,2 % de los planes: casi siempre alguno falla. Importa cuándo se descubre. El coste crece 15 % por semana de trabajo construido encima, un supuesto del autor.",
                label_w=450, width=1000, note_kind="gold", foot=SINT)


def se187_registro() -> Fig:
    rows = [
        ["Campo ausente", "28 de 28"],
        ["Fecha sin formato", "22 de 22"],
        ["Responsable colectivo", "15 de 15"],
        ["Una sola opción", "22 de 22"],
        ["Disparador de revisión vago", "21 de 21"],
        ["Decisión que no corresponde a ninguna opción", "34 de 34"],
        ["Cambio del sentido del contexto", "0 de 38"],
        ["Decisión que dice una opción y el acta otra", "0 de 20"],
    ]
    return tab("Linter de registros de decisión sobre 200 mutaciones de un registro correcto",
               "Tabla: un linter de forma detecta 142 de 200 mutaciones de un registro de decisión; atrapa campos ausentes, fechas, responsables colectivos, opción única, disparadores vagos y decisiones sin opción, y no ve ni un cambio de sentido en el contexto ni un acta que contradice la decisión.",
               ["Mutación", "Detectadas"], rows, [560, 260], row_h=36, size=13,
               note="El linter acierta 142 de 200 y falla exactamente donde importa el criterio humano: el sentido de lo escrito. Las reglas se escribieron conociendo las mutaciones, así que el 100 % por tipo es optimista.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-188
def se188_escapes() -> Fig:
    rows = [
        ["0,0 (independientes)", "4 436", "2 372", "1 772", "1 122"],
        ["0,5", "4 030", "3 174", "3 137", "2 961"],
        ["0,8", "4 319", "4 258", "4 258", "4 258"],
        ["1,0 (ven lo mismo)", "4 500", "4 500", "4 500", "4 500"],
    ]
    return tab("Defectos que se escapan de 10 000 según cuántas comprobaciones forman la definición de terminado",
               "Tabla: con cuatro comprobaciones de potencia 0,55, 0,45, 0,25 y 0,35, los defectos que se escapan de 10 000 bajan de 4436 con una a 1122 con cuatro si las comprobaciones son independientes, pero con correlación 0,8 se quedan en 4258 y con correlación 1 en 4500 sin importar cuántas se añadan.",
               ["Correlación entre comprobaciones", "1 comprobación", "2", "3", "4"], rows, [330, 190, 140, 140, 140], row_h=44, size=13,
               note="Añadir comprobaciones solo ayuda si ven defectos distintos. Con alta correlación la segunda ya no aporta casi nada. El modelo reduce la dificultad a un número; en la realidad la correlación depende de qué mira cada comprobación.",
               note_kind="coral", foot=SINT)


def se188_listo() -> Fig:
    items = [
        ("Sin refinar (60,0 % con ambigüedad)", 5.37, "coral", "5,37 d"),
        ("1 día de refinamiento (38,3 %)", 5.54, "gold", "5,54 d"),
        ("2 días (24,4 %)", 5.97, "teal", "5,97 d"),
        ("4 días (9,9 %)", 7.40, "gold", "7,40 d"),
        ("8 días (1,6 %)", 11.07, "coral", "11,07 d"),
    ]
    return bars("Plazo medio hasta terminar según los días de refinamiento previo",
                "Barras: con 60 por ciento de ambigüedad inicial que baja con cada día de refinamiento, el plazo medio hasta terminar es 5,37 días sin refinar, 5,54 con un día, 5,97 con dos, 7,40 con cuatro y 11,07 con ocho.",
                items, 40.0, "Exigir más preparación reduce la ambigüedad pero retrasa el inicio: con estos parámetros no refinar tiene el menor plazo medio, aunque con el peor riesgo de rehacer. El plazo medio no incluye el coste de oportunidad de lo que se aprende al empezar; la elección depende de cuánto cuesta rehacer.",
                label_w=360, width=980, note_kind="gold", foot=SINT)


def se188_criterios() -> Fig:
    rows = [
        ["Cuando llega a las 24 h exactas, se cuenta un día", "Verificable", "Sin aviso"],
        ["La interfaz debe ser amigable", "Vago", "Palabra vaga y sin número"],
        ["Guarda el borrador cada 30 segundos", "Verificable", "Sin aviso"],
        ["Debe ser robusto ante fallos de red", "Vago", "Palabra vaga y sin número"],
        ["Se rechaza el formato .exe", "Verificable", "Falso aviso: sin número"],
        ["Los reportes son adecuados", "Vago", "Sin condición ni número"],
        ["Si no responde, reintenta tres veces y luego informa", "Verificable", "Falso aviso: dos criterios"],
        ["Registra marca de tiempo y evaluador y luego envía correo", "Dos criterios", "Sin número; dos en uno"],
    ]
    return tab("Linter de criterios de aceptación: ocho casos nuevos frente al juicio del autor",
               "Tabla: un linter de palabras vagas y de falta de condición o número acertó 8 de 8 criterios con los que se ajustó y 6 de 8 con ocho casos nuevos: dio dos falsos avisos en criterios verificables, uno sin cifra y otro con una conjunción legítima.",
               ["Criterio", "Juicio del autor", "Resultado del linter"], rows, [470, 200, 270], row_h=40, size=12,
               note="Ajuste 8 de 8; casos nuevos 6 de 8, con 4 aciertos y 2 falsos avisos. Con ocho casos la exactitud real es desconocida. El linter ve palabras, no si un criterio se puede comprobar.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-189
def se189_resumen() -> Fig:
    items = [
        ("Mediana", 4.01, "teal", "4,01 d"),
        ("Media", 5.52, "gold", "5,52 d"),
        ("Percentil 85", 9.18, "gold", "9,18 d"),
        ("Percentil 95", 14.95, "coral", "14,95 d"),
    ]
    return bars("Tiempo de ciclo de 100 000 elementos con cola larga: qué número resumir",
                "Barras: con tiempo de ciclo lognormal de mediana 4 días, la media es 5,52, el percentil 85 es 9,18 y el 95 es 14,95; 34,5 por ciento de los elementos supera la media, y un solo elemento de 60 días mueve la media de una muestra de 20 de 6,05 a 8,75 sin cambiar casi la mediana.",
                items, 40.0, "Prometer la media falla en 34,5 % de los elementos. En una muestra de 20, un elemento de 60 días sube la media de 6,05 a 8,75 y deja la mediana en 4,32 → 4,48. Los datos son lognormales sintéticos: uno real puede ser distinto.",
                label_w=190, width=900, note_kind="gold", foot=SINT)


def se189_velocidad() -> Fig:
    data = [(1, 11, 33.0), (2, 10, 31.2), (4, 8, 27.0), (6, 12, 43.8), (8, 10, 39.5), (10, 8, 34.2), (11, 10, 44.4), (12, 13, 60.0)]
    items = []
    for s, n, v in data:
        kind = "coral" if s >= 11 else "gold"
        items.append((f"Sprint {s}: {n} elementos", v, kind, f"{v:g}".replace(".", ",") + " pt"))
    return bars("Velocidad en puntos frente a elementos terminados cuando la velocidad se premia",
                "Barras: con un rendimiento real constante de unos 10 elementos por sprint y una inflación de estimaciones de 4 por ciento por sprint, la velocidad en puntos va de 33,0 en el sprint 1 a 60,0 en el 12, 1,82 veces, mientras los elementos terminados pasan de 11 a 13, 1,18 veces.",
                items, 7.5, "La velocidad de sprint 12 es 1,82 veces la del sprint 1; los elementos terminados, 1,18 veces. Partir cada historia en dos duplicaría el conteo sin cambiar el alcance. Toda métrica premiada se puede inflar; por eso se miran juntas.",
                label_w=290, width=900, note_kind="coral", foot=SINT)


def se189_muestra() -> Fig:
    rows = [
        ["10", "0,65 a 1,81", "0,54 a 1,81", "0,46 a 2,09"],
        ["20", "0,72 a 1,49", "0,69 a 1,74", "0,64 a 2,62"],
        ["50", "0,81 a 1,30", "0,76 a 1,34", "0,69 a 1,46"],
        ["100", "0,85 a 1,20", "0,83 a 1,25", "0,79 a 1,40"],
        ["400", "0,92 a 1,10", "0,91 a 1,11", "0,89 a 1,18"],
    ]
    return tab("Percentil estimado dividido por el verdadero, intervalo que contiene 90 % de 1000 muestras",
               "Tabla: con 10 elementos el percentil 85 estimado puede ir de 0,54 a 1,81 veces el verdadero; con 100 elementos va de 0,83 a 1,25 y con 400 de 0,91 a 1,11; el percentil 95 con 20 elementos llega a 2,62 veces.",
               ["Elementos", "Percentil 50", "Percentil 85", "Percentil 95"], rows, [190, 240, 240, 240], row_h=40, size=13,
               note="Con pocos elementos los percentiles altos son imprecisos: el percentil 95 de 20 elementos puede estar 2,6 veces por encima del real. Informar el tamaño de la muestra junto al percentil es parte de la métrica.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-190
def se190_acciones() -> Fig:
    rows = [
        ["1", "12", "9,2", "2,8", "12,1"],
        ["2", "24", "9,4", "14,6", "12,6"],
        ["3", "36", "9,4", "26,6", "12,6"],
        ["5", "60", "9,4", "50,6", "12,6"],
        ["8", "96", "9,4", "86,6", "12,7"],
    ]
    return tab("Acciones acordadas por retrospectiva con 2 días de capacidad de mejora por sprint (12 sprints)",
               "Tabla: con 2 días de capacidad de mejora por sprint, acordar 1 acción por retrospectiva completa 9,2 de 12 y deja 2,8 abiertas; acordar 8 completa 9,4 de 96 y deja 86,6 abiertas, con un beneficio acumulado de 12,1 frente a 12,7 puntos porcentuales.",
               ["Acciones por retrospectiva", "Creadas", "Terminadas", "Abiertas al final", "Beneficio acumulado (pp)"], rows, [250, 150, 170, 200, 200], row_h=44, size=13,
               note="La capacidad limita lo que se termina, no lo que se acuerda: ocho acciones por retrospectiva no mejoran más que dos y dejan 87 abiertas. Los costes de 1 a 4 días y el 3 % de mejora por acción son supuestos.",
               note_kind="coral", foot=SINT)


def se190_deteccion() -> Fig:
    rows = [
        ["2", "20,5 %", "2,7 %"],
        ["4", "36,0 %", "2,9 %"],
        ["8", "51,0 %", "1,9 %"],
        ["12", "59,8 %", "2,7 %"],
        ["24", "70,9 %", "2,4 %"],
        ["12, mirando cada semana", "—", "19,7 %"],
    ]
    return tab("Cuántas veces una prueba declara una mejora, con efecto real de 15 % y sin efecto",
               "Tabla: con una mejora real del 15 por ciento en el tiempo de ciclo y 8 elementos por semana, una prueba de rangos la detecta en 20,5 por ciento de los casos con 2 semanas de datos, 51,0 con 8 y 70,9 con 24; sin efecto real da falsa mejora en 2 a 3 por ciento, pero 19,7 si se mira cada semana durante 12.",
               ["Semanas tras el cambio", "Declara mejora (efecto real 15 %)", "Declara mejora (sin efecto)"], rows, [310, 330, 300], row_h=44, size=13,
               note="Dos semanas de datos casi nunca bastan para ver una mejora real del 15 %. Mirar cada semana multiplica por siete la falsa mejora. La dispersión de 0,5 y los 8 elementos por semana son supuestos.",
               note_kind="gold", foot=SINT)


def se190_intervenciones() -> Fig:
    items = [
        ("Situación actual: lotes de 5 y variabilidad alta", 41.2, "coral", "41,2"),
        ("Trabajar más horas sin cambiar nada", 41.6, "coral", "41,6"),
        ("Reducir la variabilidad del servicio", 28.9, "gold", "28,9"),
        ("Llegadas de una en una", 23.1, "gold", "23,1"),
        ("Añadir 10 % de capacidad", 22.6, "gold", "22,6"),
        ("Llegadas de una en una y menos variabilidad", 9.4, "teal", "9,4"),
    ]
    return bars("Espera media en una cola al 90 % de utilización según la intervención",
                "Barras: en una cola con 90 por ciento de utilización, lotes de cinco y alta variabilidad la espera es 41,2 servicios; trabajar más horas la deja en 41,6, añadir 10 por ciento de capacidad en 22,6, enviar de una en una en 23,1, reducir la variabilidad en 28,9 y combinar lotes pequeños y baja variabilidad en 9,4.",
                items, 10.0, "Una retrospectiva que concluye trabajar más no mueve la espera. Las intervenciones sobre el sistema (lotes, variabilidad, capacidad) sí, y se combinan. El modelo es una sola cola: un sistema real tiene muchas.",
                label_w=470, width=1010, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-191
def se191_calibracion() -> Fig:
    rows = [
        ["4 semanas", "46,3 %", "65,2 %", "74,4 %", "45,8 %", "77,7 %"],
        ["8 semanas", "40,8 %", "64,7 %", "76,5 %", "40,2 %", "80,1 %"],
        ["16 semanas", "42,7 %", "69,2 %", "82,1 %", "42,2 %", "85,2 %"],
    ]
    return tab("Calibración de pronósticos de «cuándo termina» con alcance que crece de 0 a 20 %",
               "Tabla: un pronóstico de percentil 85 construido con 8 semanas de historia que ignora el crecimiento del alcance se cumple en 64,7 por ciento de los casos; si incluye ese crecimiento, en 80,1; una estimación puntual con el rendimiento medio se cumple en 40,2 por ciento.",
               ["Historia", "P50", "P85", "P95", "Estimación puntual", "P85 con alcance"], rows, [170, 140, 140, 140, 190, 190], row_h=40, size=13,
               note="El percentil 85 que ignora el crecimiento del alcance se cumple en 65 % a 69 %, no en 85 %. Un pronóstico está calibrado solo si incluye las fuentes de incertidumbre que existirán. La estimación puntual se cumple menos que la mediana.",
               note_kind="coral", foot=SINT)


def se191_colchon() -> Fig:
    rows = [
        ["Suma de medianas", "50,0", "25,2 %", "25,2 %"],
        ["Margen P85 en cada tarea", "84,0", "99,2 %", "22,6 %"],
        ["Medianas más un colchón de proyecto", "60,7", "68,8 %", "68,8 %"],
    ]
    return tab("Diez tareas en cadena: margen por tarea frente a colchón compartido",
               "Tabla: para una cadena de diez tareas de mediana 5 días, la suma de medianas da un plan de 50 días que se cumple en 25,2 por ciento; el margen P85 en cada tarea da 84 días y se cumple en 99,2 por ciento, pero solo en 22,6 si el trabajo se expande hasta agotar el margen; un colchón compartido da 60,7 días y 68,8 por ciento en ambos casos.",
               ["Plan", "Plazo (días)", "Se cumple (sin expansión)", "Se cumple (con expansión)"], rows, [380, 150, 210, 210], row_h=48, size=13,
               note="El margen en cada tarea parece seguro hasta que las tareas lo consumen; un colchón al final del proyecto no puede gastarse hasta que hace falta. La regla de expansión (entregar al agotar el margen si se iba antes) es un supuesto del autor.",
               note_kind="gold", foot=SINT)


def se191_tornado() -> Fig:
    items = [
        ("Rendimiento semanal (de 26 a 13 semanas)", 13, "coral", "13 semanas"),
        ("Tamaño del backlog (de 13 a 22)", 9, "gold", "9 semanas"),
        ("Crecimiento semanal del alcance (de 16 a 19)", 3, "teal", "3 semanas"),
        ("Factor de partición de elementos (de 17 a 18)", 1, "teal", "1 semana"),
    ]
    return bars("Cuánto mueve el plazo P85 cada supuesto al variarlo ±30 % (base: 17 semanas)",
                "Barras: variar cada supuesto un 30 por ciento mueve el plazo P85 de 17 semanas en 13 semanas para el rendimiento semanal, 9 para el tamaño del backlog, 3 para el crecimiento del alcance y 1 para el factor de partición de elementos.",
                items, 30.0, "El rendimiento domina el plan: es el supuesto que conviene medir y vigilar. El orden depende de los valores base (60 elementos, 6 por semana, 1 de crecimiento, factor 1,2) que son supuestos del autor.",
                label_w=470, width=1010, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-192
def se192_disparadores() -> Fig:
    rows = [
        ["4 semanas, 1 aviso", "68,0 %", "3", "3,0 %"],
        ["4 semanas, 2 avisos seguidos", "46,5 %", "4", "5,0 %"],
        ["4 semanas, 3 avisos seguidos", "34,8 %", "5", "7,2 %"],
        ["8 semanas, 1 aviso", "47,2 %", "4", "5,8 %"],
        ["8 semanas, 2 avisos seguidos", "34,2 %", "5", "9,5 %"],
        ["8 semanas, 3 avisos seguidos", "26,2 %", "6", "10,5 %"],
    ]
    return tab("Disparador de replanificación por pronóstico P85: falsas alarmas frente a retraso de detección",
               "Tabla: un disparador basado en el percentil 85 pronosticado con 4 semanas de historia da falsa alarma en 68,0 por ciento de los proyectos sin deriva y detecta una caída real con 3 semanas de retraso mediano; con 8 semanas y 3 avisos seguidos la falsa alarma baja a 26,2 y el retraso sube a 6 semanas, con 10,5 por ciento de caídas sin aviso.",
               ["Regla", "Falsa alarma sin deriva", "Retraso mediano (semanas)", "Caídas sin aviso"], rows, [330, 210, 220, 180], row_h=40, size=13,
               note="Endurecer la regla reduce las falsas alarmas y retrasa la detección: no existe una regla sin costo. Con un plazo de 22 semanas y 100 elementos, el 83 % de los proyectos con caída no terminaría a tiempo. Todos los parámetros son supuestos.",
               note_kind="coral", foot=SINT)


def se192_validador() -> Fig:
    rows = [
        ["Campo ausente", "28 de 28"],
        ["Rango ausente", "15 de 15"],
        ["Confianza ausente", "18 de 18"],
        ["Disparador sin umbral", "17 de 17"],
        ["Supuesto sin responsable ni fecha", "21 de 21"],
        ["Fecha de revisión sin formato", "17 de 17"],
        ["Responsable colectivo", "22 de 22"],
        ["Métrica sin definición", "19 de 19"],
        ["Rango invertido (14 a 9 semanas)", "0 de 20"],
        ["Salvaguarda que contradice el objetivo", "0 de 23"],
    ]
    return tab("Validador de planes sobre 200 mutaciones de un plan correcto",
               "Tabla: un validador de forma detecta 157 de 200 mutaciones de un plan adaptativo; atrapa campos ausentes, rangos o confianzas faltantes, disparadores sin umbral y responsables colectivos, y no detecta ni un rango invertido ni una salvaguarda que contradice el objetivo.",
               ["Mutación", "Detectadas"], rows, [560, 260], row_h=34, size=13,
               note="Detecta 157 de 200 y no ve ninguna de las 43 mutaciones de sentido. Un plan que pasa el validador está completo en forma; no se sabe si es razonable.",
               note_kind="gold", foot=SINT)


def se192_replay() -> Fig:
    rows = [
        ["Plan fijo de 60 elementos", "60", "52,1 %", "92,9 %"],
        ["Plan fijo ordenado por valor", "60", "52,1 %", "98,8 %"],
        ["Plan adaptativo (alcance según rendimiento reciente)", "42,8", "99,4 %", "98,8 %"],
    ]
    return tab("Mil proyectos sintéticos: 60 elementos, 11 semanas, caída de 30 % en 40 % de ellos",
               "Tabla: un plan fijo de 60 elementos cumple lo prometido en 52,1 por ciento de 1000 proyectos y entrega 92,9 por ciento del valor; ordenarlo por valor sube el valor a 98,8 sin mejorar el cumplimiento; el plan adaptativo promete 42,8 elementos de media, cumple en 99,4 por ciento y entrega 98,8.",
               ["Estrategia", "Elementos prometidos", "Cumple lo prometido", "Valor entregado"], rows, [440, 190, 200, 170], row_h=52, size=13,
               note="La mejora de valor viene de ordenar por valor; la de cumplimiento, de prometer menos con un pronóstico prudente. Son dos efectos separables. Los valores lognormales y la caída de rendimiento son supuestos.",
               note_kind="teal", foot=SINT)


FIGURES = {
    "se-187-riesgos-independientes-y-causa-comun.svg": se187_exposicion,
    "se-187-orden-de-validacion-de-supuestos.svg": se187_supuestos,
    "se-187-linter-de-decisiones.svg": se187_registro,
    "se-188-comprobaciones-correlacionadas.svg": se188_escapes,
    "se-188-refinar-antes-de-empezar.svg": se188_listo,
    "se-188-linter-de-criterios.svg": se188_criterios,
    "se-189-que-numero-resumir.svg": se189_resumen,
    "se-189-velocidad-premiada.svg": se189_velocidad,
    "se-189-tamano-de-muestra.svg": se189_muestra,
    "se-190-acciones-por-retrospectiva.svg": se190_acciones,
    "se-190-detectar-una-mejora.svg": se190_deteccion,
    "se-190-intervenciones-sobre-el-sistema.svg": se190_intervenciones,
    "se-191-calibracion-de-pronosticos.svg": se191_calibracion,
    "se-191-margen-o-colchon.svg": se191_colchon,
    "se-191-sensibilidad-del-plan.svg": se191_tornado,
    "se-192-disparadores-de-replanificacion.svg": se192_disparadores,
    "se-192-validador-de-planes.svg": se192_validador,
    "se-192-reproduccion-de-proyectos.svg": se192_replay,
}
