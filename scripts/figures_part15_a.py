"""Figures for SE-181 to SE-186 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-181
def se181_intervalo() -> Fig:
    items = [
        ("Retroalimentación tras cada pieza (40 ciclos)", 62.0, "gold", "62,0"),
        ("Cada 2 piezas (20 ciclos)", 56.8, "teal", "56,8"),
        ("Cada 4 piezas (10 ciclos)", 55.3, "teal", "55,3"),
        ("Cada 8 piezas (5 ciclos)", 56.8, "teal", "56,8"),
        ("Cada 20 piezas (2 ciclos)", 64.9, "gold", "64,9"),
        ("Solo al final (modelo predictivo)", 79.6, "coral", "79,6"),
    ]
    return bars("Esfuerzo total de un plan de 40 piezas según cada cuánto se obtiene retroalimentación",
                "Barras: con 40 piezas de trabajo y 25 por ciento de malentendidos, el esfuerzo total medio de 2000 simulaciones es 79,6 si se recibe retroalimentación solo al final, 64,9 cada 20 piezas, 55,3 cada 4, 56,8 cada 2 u 8 y 62,0 tras cada pieza, porque cada ciclo cuesta 0,3.",
                items, 6.0, "Hay un intervalo intermedio con el menor esfuerzo: retroalimentar con más frecuencia reduce el retrabajo pero cada ciclo cuesta 0,3 piezas. Los parámetros (25 % de malentendidos, 15 % de piezas posteriores afectadas) son supuestos del autor.",
                label_w=400, width=1010, note_kind="gold", foot=SINT)


def se181_corte() -> Fig:
    items = [
        ("Todo se libera al final del plan", 0.0, "coral", "0 %"),
        ("Incrementos en orden arbitrario", 47.1, "gold", "47,1 %"),
        ("Incrementos por valor sobre coste", 73.6, "teal", "73,6 %"),
    ]
    return bars("Valor entregado cuando el proyecto se corta en un momento al azar",
                "Barras: de 200 conjuntos de 20 funciones cortados en 100 momentos al azar cada uno, liberar todo al final entrega 0 por ciento del valor, liberar incrementos en orden arbitrario 47,1 y ordenar los incrementos por valor sobre coste 73,6.",
                items, 6.0, "Un incremento solo vale si se libera y si el orden respeta el valor. El modelo supone funciones independientes entre sí; con dependencias fuertes el orden por valor no siempre es posible.",
                label_w=360, width=930, note_kind="teal", foot=SINT)


def se181_volatilidad() -> Fig:
    rows = [
        ["0 %", "40,0", "43,0", "52,0", "Predictivo"],
        ["5 %", "47,8", "45,5", "54,0", "Ciclos de 4"],
        ["10 %", "55,8", "47,9", "56,0", "Ciclos de 4"],
        ["20 %", "71,2", "52,7", "60,0", "Ciclos de 4"],
        ["30 %", "87,1", "57,7", "64,0", "Ciclos de 4"],
        ["60 %", "134,1", "72,4", "76,0", "Ciclos de 4"],
    ]
    return tab("Esfuerzo total de 40 piezas según la volatilidad de los requisitos y el ciclo",
               "Tabla de esfuerzo medio: sin cambios el plan predictivo cuesta 40 y gana; con 5 por ciento de piezas malentendidas los ciclos de cuatro piezas ya ganan, y con 60 por ciento el predictivo cuesta 134,1 frente a 72,4.",
               ["Piezas malentendidas", "Predictivo (un ciclo)", "Ciclos de 4 piezas", "Ciclos de 1 pieza", "Menor esfuerzo"], rows, [190, 200, 190, 190, 170], row_h=40, size=13,
               note="El cruce está entre 0 % y 5 % de malentendidos con estos supuestos. Con requisitos estables y cambios baratos, planificar de una vez cuesta menos; la clase no defiende un modelo, sino la relación entre volatilidad y sobrecoste del ciclo.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-182
def se182_feedback() -> Fig:
    items = [
        ("Sin retroalimentación", 12.3, "coral", "12,3 %"),
        ("Cada 5 sprints", 11.4, "gold", "11,4 %"),
        ("Cada 2 sprints", 9.4, "gold", "9,4 %"),
        ("Cada sprint", 8.3, "teal", "8,3 %"),
    ]
    return bars("Valor que se deja sin entregar frente al mejor conjunto posible",
                "Barras: de 60 funciones y 10 sprints de 3 funciones, el valor no entregado respecto del mejor conjunto posible es 12,3 por ciento sin retroalimentación, 11,4 si se aprende cada 5 sprints, 9,4 cada 2 y 8,3 cada sprint, en 500 mundos sintéticos.",
                items, 25.0, "Aprender del uso reorganiza las prioridades de los grupos de funciones ya entregados. La ganancia total es de cuatro puntos: el proceso ayuda, pero el efecto depende de que lo observado en un grupo se generalice a los demás.",
                label_w=290, width=900, note_kind="teal", foot=SINT)


def se182_ceremonia() -> Fig:
    rows = [
        ["1 semana", "5,25 %", "12", "91,1 %"],
        ["2 semanas", "2,62 %", "6", "91,6 %"],
        ["3 semanas", "1,75 %", "4", "90,8 %"],
        ["4 semanas", "1,31 %", "3", "90,6 %"],
        ["6 semanas", "0,88 %", "2", "90,0 %"],
    ]
    return tab("Longitud del ciclo: sobrecoste de las ceremonias frente a oportunidades de aprender",
               "Tabla de un trimestre de 12 semanas con 10,5 horas de ceremonias por ciclo: el sobrecoste va de 5,25 por ciento con ciclos de una semana a 0,88 con ciclos de seis; el valor entregado respecto del mejor conjunto es máximo, 91,6 por ciento, con ciclos de dos semanas.",
               ["Ciclo", "Capacidad en ceremonias", "Ciclos por trimestre", "Valor / mejor conjunto"], rows, [190, 260, 220, 250], row_h=40, size=13,
               note="El óptimo aparece en el ciclo de 2 semanas con una diferencia de 1,6 puntos entre el mejor y el peor: es una curva plana. Las 10,5 horas de ceremonias y el equipo de cinco personas son supuestos; con otros valores el óptimo se mueve.",
               note_kind="gold", foot=SINT)


def se182_ramas() -> Fig:
    items = [
        ("Rama de 1 día", 36.2, "teal", "36,2 %"),
        ("Rama de 2 días", 83.9, "gold", "83,9 %"),
        ("Rama de 5 días", 100.0, "coral", "100 %"),
        ("Rama de 10 días", 100.0, "coral", "100 %"),
    ]
    return bars("Probabilidad de algún conflicto de fusión entre seis ramas según su vida",
                "Barras: con seis desarrolladores que tocan 2 bloques de 8 líneas por día en un archivo de 2000 líneas, la probabilidad de algún conflicto es 36,2 por ciento con ramas de un día, 83,9 con dos días y 100 con cinco o más.",
                items, 5.0, "La probabilidad crece como el número de pares de cambios que pueden solaparse, que aumenta con el cuadrado de la vida de la rama. Todos los cambios caen al azar en un archivo: en un código real se concentran en pocas zonas y el conflicto es aún más probable.",
                label_w=360, width=960, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-183
def se183_urgente() -> Fig:
    items = [
        ("Scrum sin cambiar el alcance del sprint (P85: 10,5)", 7.04, "coral", "7,04 días"),
        ("Kanban con extracción (P85: 3,06)", 2.57, "gold", "2,57 días"),
        ("Kanban con carril exprés (P85: 2,0)", 2.0, "teal", "2,00 días"),
    ]
    return bars("Plazo de un trabajo urgente de 2 días que llega en un momento cualquiera",
                "Barras: un trabajo urgente de dos días de esfuerzo tarda 7,04 días de media si debe esperar al siguiente sprint, 2,57 si se extrae cuando alguien se libera y 2,00 con un carril exprés que reserva una ranura.",
                items, 55.0, "El plazo de Scrum aparece porque el alcance del sprint está comprometido, no porque Scrum lo exija: un equipo puede reservar capacidad para urgencias. La comparación mide la política, no el marco.",
                label_w=530, width=1130, note_kind="gold", foot=SINT)


def se183_compromiso() -> Fig:
    rows = [
        ["Rendimiento del último sprint", "44,7 %", "9,99", "1,67"],
        ["Media de los 3 últimos", "44,0 %", "9,99", "1,37"],
        ["Media de los 6 últimos", "44,0 %", "9,99", "1,29"],
        ["Mínimo de los 6 últimos", "11,2 %", "6,21", "4,03"],
        ["Segundo menor de los 12 últimos", "12,1 %", "6,63", "3,62"],
    ]
    return tab("Reglas para comprometer elementos en un sprint (rendimiento medio de 10)",
               "Tabla de 20000 sprints sintéticos con rendimiento normal de media 10 y desviación 3: comprometer la media falla en 44 por ciento de los sprints; comprometer el mínimo de los 6 últimos falla en 11,2 por ciento pero compromete 6,21 elementos y deja 4,03 sin usar.",
               ["Regla de compromiso", "Sprints que fallan", "Comprometido", "Capacidad sobrante"], rows, [380, 190, 190, 190], row_h=40, size=13,
               note="Comprometer la media garantiza fallar casi la mitad de las veces. Ninguna regla es correcta en sí: cada una cambia fiabilidad por capacidad sin usar, y el equipo decide qué cuesta más.",
               note_kind="gold", foot=SINT)


def se183_tiempo_fijo() -> Fig:
    items = [
        ("Las 12 piezas terminadas dentro de 4 semanas", 1.3, "coral", "1,3 %"),
        ("Las 4 imprescindibles terminadas con tiempo fijo", 84.7, "teal", "84,7 %"),
        ("Piezas medias entregadas con tiempo fijo (de 12)", 50.3, "gold", "6,04"),
    ]
    return bars("Alcance fijo frente a tiempo fijo y alcance variable (4 semanas, 12 piezas)",
                "Barras: con 12 piezas de esfuerzo lognormal y 4 semanas, terminar todas ocurre en 1,3 por ciento de 5000 simulaciones; con el tiempo fijo y las piezas en orden de prioridad se terminan las 4 imprescindibles en 84,7 por ciento y se entregan 6,04 piezas de media.",
                items, 5.0, "Fijar el tiempo y recortar el alcance convierte una promesa casi imposible en una entrega parcial pero útil. Funciona si las piezas son separables y el orden de prioridad es real; la barra de 6,04 está escalada a porcentaje de 12 solo para dibujarla.",
                label_w=470, width=1030, note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-184
def se184_espera() -> Fig:
    rows = [
        ["50 %", "1,00", "1,00"],
        ["70 %", "2,33", "2,33"],
        ["80 %", "3,95", "4,00"],
        ["90 %", "8,80", "9,00"],
        ["95 %", "17,90", "19,00"],
    ]
    return tab("Espera en cola según la utilización de una persona (en servicios medios)",
               "Tabla: simulación de una cola de un servidor con llegadas y servicios aleatorios frente a la fórmula utilización sobre uno menos utilización; la espera pasa de 1 servicio medio al 50 por ciento a 9 al 90 y a unos 19 al 95.",
               ["Utilización", "Simulada", "Fórmula ρ/(1−ρ)"], rows, [260, 260, 300], row_h=40, size=13,
               note="La espera no crece linealmente: de 80 % a 95 % de utilización se multiplica por cinco. Con 95 % la simulación de 280 000 clientes aún no ha convergido a la fórmula (17,9 frente a 19,0).",
               note_kind="coral", foot=SINT)


def se184_little() -> Fig:
    items = [
        ("Límite de 1 elemento en curso (rend. 1,00/día)", 1.0, "teal", "1,00 d"),
        ("Límite de 3 (rend. 3,02/día)", 0.99, "teal", "0,99 d"),
        ("Límite de 4 (rend. 3,02/día)", 1.33, "gold", "1,33 d"),
        ("Límite de 6 (rend. 3,02/día)", 1.99, "gold", "1,99 d"),
        ("Límite de 9 (rend. 3,02/día)", 2.98, "gold", "2,98 d"),
        ("Límite de 15 (rend. 3,02/día)", 4.97, "coral", "4,97 d"),
        ("Límite de 30 (rend. 3,02/día)", 9.95, "coral", "9,95 d"),
    ]
    return bars("Plazo medio con tres personas según el límite de trabajo en curso",
                "Barras: con tres personas y tareas de un día de media, el rendimiento satura en 3,02 elementos por día desde un límite de 3, y el plazo medio crece linealmente: 0,99 días con límite 3, 1,99 con 6, 4,97 con 15 y 9,95 con 30, igual a límite dividido por rendimiento.",
                items, 40.0, "Por encima del número de personas más trabajo en curso no añade rendimiento y solo añade espera: plazo = límite ÷ rendimiento, la ley de Little. El modelo es cerrado y sin variabilidad entre tareas más allá de la exponencial.",
                label_w=410, width=950, note_kind="gold", foot=SINT)


def se184_variabilidad() -> Fig:
    items = [
        ("Servicio constante (CV² = 0)", 2.88, "teal", "2,88"),
        ("Servicio con poca variación (CV² = 0,25)", 3.63, "teal", "3,63"),
        ("Servicio exponencial (CV² = 1)", 5.57, "gold", "5,57"),
        ("Servicio muy variable (CV² = 4)", 13.64, "coral", "13,64"),
        ("Exponencial, llegadas en lotes de 5", 19.61, "coral", "19,61"),
    ]
    return bars("Espera en cola con 85 % de utilización según la variabilidad",
                "Barras: con la misma utilización de 85 por ciento, la espera media es 2,88 servicios con tiempos constantes, 5,57 con tiempos exponenciales, 13,64 con alta variabilidad y 19,61 si las llegadas son en lotes de cinco.",
                items, 22.0, "Misma carga media, espera distinta: la variabilidad y los lotes importan tanto como la utilización. Las simulaciones concuerdan con la aproximación de Kingman (2,83; 3,54; 5,67; 14,17).",
                label_w=450, width=1000, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-185
def se185_suma() -> Fig:
    items = [
        ("Dispersión σ = 0,2", 31.9, "gold", "31,9 %"),
        ("σ = 0,5", 12.5, "coral", "12,5 %"),
        ("σ = 0,8", 4.1, "coral", "4,1 %"),
        ("σ = 1,1", 1.5, "coral", "1,5 %"),
        ("σ = 0,5 con 25 % de margen por tarea", 83.5, "teal", "83,5 %"),
    ]
    return bars("Probabilidad de terminar 30 tareas dentro de la suma de sus medianas",
                "Barras: con 30 tareas de mediana entre 1 y 5 días, terminar dentro de la suma de medianas (96 días) ocurre en 31,9 por ciento con dispersión 0,2, 12,5 con 0,5, 4,1 con 0,8 y 1,5 con 1,1; añadir 25 por ciento a cada tarea lo eleva a 83,5.",
                items, 5.0, "Sumar medianas subestima porque cada tarea tiene cola larga hacia arriba: con σ = 0,5 la media es 108,9 y el P85 120,8 frente a un plan de 96. Los márgenes por tarea sirven aquí pero la clase 191 muestra que se pueden consumir.",
                label_w=400, width=1000, note_kind="coral", foot=SINT)


def se185_cobertura() -> Fig:
    items = [
        ("3 semanas de historia", 32.5, "coral", "32,5 %"),
        ("6 semanas", 46.6, "coral", "46,6 %"),
        ("12 semanas", 61.1, "gold", "61,1 %"),
        ("24 semanas", 70.7, "gold", "70,7 %"),
        ("48 semanas", 75.7, "teal", "75,7 %"),
    ]
    return bars("Cobertura real de un intervalo que promete 80 % para 12 semanas futuras",
                "Barras: un intervalo central nominal del 80 por ciento para la suma de 12 semanas, construido por remuestreo de la historia, cubre el valor real en 32,5 por ciento de los casos con 3 semanas de historia, 46,6 con 6, 61,1 con 12, 70,7 con 24 y 75,7 con 48.",
                items, 6.0, "Con poca historia el intervalo es demasiado estrecho porque no incluye la incertidumbre de haber visto pocas semanas. Incluso con 48 semanas queda bajo el 80 % prometido. El proceso simulado es estable; uno real cambia y empeora la cobertura.",
                label_w=290, width=900, note_kind="coral", foot=SINT)


def se185_tallas() -> Fig:
    rows = [
        ["1 contra 8", "0,7 %", "Se distinguen"],
        ["3 contra 8", "12,4 %", "Casi siempre se distinguen"],
        ["2 contra 3", "27,8 %", "Se solapan mucho"],
        ["3 contra 5", "27,1 %", "Se solapan mucho"],
        ["5 contra 8", "29,1 %", "Se solapan mucho"],
        ["10 de talla 3 contra 10 de talla 5", "4,2 %", "Agregados se distinguen"],
    ]
    return tab("Probabilidad de que un elemento de talla menor tarde más que uno de talla mayor",
               "Tabla: con tallas 1, 2, 3, 5 y 8 con medianas de 1 a 8 días y dispersión 0,6, un elemento de talla 3 tarda más que uno de talla 5 en 27,1 por ciento de los pares y uno de talla 2 más que uno de talla 3 en 27,8; diez elementos de talla 3 tardan más que diez de talla 5 solo en 4,2 por ciento.",
               ["Comparación", "La menor tarda más", "Lectura"], rows, [380, 220, 330], row_h=40, size=13,
               note="Las tallas contiguas se solapan: la talla ordena en media pero no predice cada elemento. Sumadas, las incertidumbres individuales se compensan y las tallas sirven para planificar un conjunto, no para prometer un elemento.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-186
def se186_convergencia() -> Fig:
    rows = [
        ["1 (cadena)", "5", "37,5 %", "10,78", "12,80"],
        ["3", "15", "0,7 %", "13,98", "15,99"],
        ["6", "30", "0,0 %", "15,10", "16,94"],
        ["10", "50", "0,0 %", "15,87", "17,67"],
    ]
    return tab("Cinco capas de tareas con camino crítico de 10 días calculado con medianas",
               "Tabla: en una red de cinco capas con tareas de mediana 2 días, el camino crítico con medianas es 10 días; terminar en 10 días ocurre en 37,5 por ciento si es una cadena, 0,7 con tres tareas por capa y 0 con seis o diez, y la media sube de 10,78 a 15,87 días.",
               ["Tareas por capa", "Tareas", "P(terminar ≤ 10 d)", "Media (días)", "P85 (días)"], rows, [190, 140, 230, 170, 170], row_h=40, size=13,
               note="Cuando varios caminos convergen, el máximo de duraciones aleatorias es mayor que cada una: el plan que usa solo medianas es optimista en proporción a la anchura de la red. Las duraciones lognormales de σ = 0,4 son un supuesto.",
               note_kind="coral", foot=SINT)


def se186_dependencias() -> Fig:
    rows = [
        ["1", "90,4 %", "80,6 %", "70,4 %"],
        ["3", "72,9 %", "51,8 %", "34,7 %"],
        ["5", "59,2 %", "33,8 %", "17,4 %"],
        ["10", "34,7 %", "10,8 %", "2,8 %"],
    ]
    return tab("Probabilidad de que ninguna dependencia externa llegue tarde",
               "Tabla: con 10 dependencias externas, la probabilidad de que ninguna se retrase es 34,7 por ciento si cada una llega tarde con probabilidad 0,1; 10,8 con 0,2 y 2,8 con 0,3; con una sola dependencia es 90,4, 80,6 y 70,4.",
               ["Dependencias", "Cada una tarde 10 %", "Cada una tarde 20 %", "Cada una tarde 30 %"], rows, [210, 240, 240, 240], row_h=40, size=13,
               note="La probabilidad es (1 − p) elevado al número de dependencias: veinte por ciento de riesgo individual con diez dependencias deja 10,8 % de plazos sin sorpresa. Se supone independencia; dependencias del mismo proveedor se retrasan juntas.",
               note_kind="gold", foot=SINT)


def se186_orden() -> Fig:
    rows = [
        ["Orden aleatorio válido", "21,7 %", "46,5 %", "70,1 %"],
        ["Mayor valor disponible", "40,2 %", "63,1 %", "82,6 %"],
        ["Valor sobre coste", "43,4 %", "66,4 %", "84,2 %"],
        ["Valor incluido lo que habilita, sobre coste", "42,3 %", "72,3 %", "90,3 %"],
    ]
    return tab("Valor entregado si se agota el 25, el 50 o el 75 % del coste, según el orden",
               "Tabla: con 15 elementos con dependencias, un orden aleatorio válido entrega 21,7 por ciento del valor al agotar un cuarto del coste, 46,5 a la mitad y 70,1 a tres cuartos; priorizar por valor sobre coste entrega 43,4, 66,4 y 84,2, y sumar el valor que un elemento habilita llega a 90,3 a tres cuartos.",
               ["Política de orden", "25 % del coste", "50 %", "75 %"], rows, [430, 190, 190, 190], row_h=48, size=13,
               note="Respetar las dependencias y ordenar por valor sobre coste duplica el valor del primer cuarto; contar lo que habilita ayuda más cuando el plan avanza. Las 300 redes de 15 elementos son sintéticas y sus valores lognormales son supuestos.",
               note_kind="teal", foot=SINT)


FIGURES = {
    "se-181-intervalo-de-retroalimentacion.svg": se181_intervalo,
    "se-181-valor-si-se-corta-el-proyecto.svg": se181_corte,
    "se-181-volatilidad-y-modelo.svg": se181_volatilidad,
    "se-182-aprendizaje-con-retroalimentacion.svg": se182_feedback,
    "se-182-ceremonia-y-longitud-del-ciclo.svg": se182_ceremonia,
    "se-182-vida-de-la-rama-y-conflictos.svg": se182_ramas,
    "se-183-espera-de-un-urgente.svg": se183_urgente,
    "se-183-reglas-de-compromiso.svg": se183_compromiso,
    "se-183-alcance-fijo-o-tiempo-fijo.svg": se183_tiempo_fijo,
    "se-184-espera-segun-utilizacion.svg": se184_espera,
    "se-184-limite-de-trabajo-y-plazo.svg": se184_little,
    "se-184-variabilidad-y-lotes.svg": se184_variabilidad,
    "se-185-suma-de-medianas.svg": se185_suma,
    "se-185-cobertura-de-intervalos.svg": se185_cobertura,
    "se-185-solape-entre-tallas.svg": se185_tallas,
    "se-186-convergencia-de-caminos.svg": se186_convergencia,
    "se-186-dependencias-externas.svg": se186_dependencias,
    "se-186-orden-de-entrega.svg": se186_orden,
}
