"""Figuras de ampliación de SE-353 (movimiento lateral con confianza cero) y SE-356 (intensidad de carbono de una tarea)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars

SINT = "Modelo sintético con semilla fija (scripts/experiments_part29_ext.py), CPython 3.12.9 en Windows; las probabilidades son supuestos del autor."
MED = "Tiempos medidos con CPython 3.12.9 en Windows (un equipo, mínimo de repeticiones); las intensidades de la red y la potencia por núcleo son supuestos declarados, no mediciones."


def se353_movimiento_lateral() -> Fig:
    return grouped_bars(
        "Servicios de 40 que cae un atacante que parte de uno cualquiera, según la regla de red e identidad",
        "Barras horizontales con el número medio de servicios comprometidos de 40 tras 4 000 ensayos: 40,0 con red plana, 39,61 con segmentos por equipo, 4,32 con lista de permitidos por servicio y 1,28 con identidad por servicio y autorización por operación. El servicio crítico cae en el 100 %, el 99,0 %, el 6,6 % y el 0,6 % de los ensayos.",
        ["Red plana: confianza por ubicación", "Segmentos por equipo", "Lista de permitidos por servicio", "Identidad por servicio y autorización por operación"],
        [("Servicios comprometidos (de 40)", [40.0, 39.61, 4.32, 1.28], "coral")],
        unit="Servicios comprometidos de 40, media de 4 000 ensayos", horizontal=True, decimals=2, label_w=290, ticks=[0, 10, 20, 30, 40],
        note="Los segmentos por equipo apenas ayudan porque el grafo de llamadas encadena equipos: el atacante salta de un segmento permitido al siguiente. Lo que contiene el avance es acotar cada servicio a las conexiones que su función necesita, y reducir lo que cada una de esas conexiones permite. Cada salto cae con probabilidad 0,3 (0,075 con autorización por operación, que supone 2 de 8 operaciones expuestas); ambos números son supuestos.",
        note_kind="gold", foot=SINT)


def se356_sci() -> Fig:
    return grouped_bars(
        "Emisiones por tarea (SCI) de dos implementaciones de la misma tarea según la intensidad de la red eléctrica",
        "Barras agrupadas en escala logarítmica con las emisiones por tarea, en miligramos de CO2e, de una implementación con búsqueda lineal y otra con diccionario sobre 20 000 registros: 0,947 y 0,006 con una red de 50 gCO2e/kWh, 2,105 y 0,014 con 300 y 3,957 y 0,027 con 700. El tiempo medido fue de 1,1112 s la ingenua y 0,0076 s la eficiente, unas 146 veces menos.",
        ["Red de 50 gCO2e/kWh", "Red de 300 gCO2e/kWh", "Red de 700 gCO2e/kWh"],
        [("Búsqueda lineal (1,11 s)", [0.947, 2.105, 3.957], "coral"), ("Diccionario (0,0076 s)", [0.006, 0.014, 0.027], "teal")],
        unit="mg CO2e por tarea (SCI)", log=True, decimals=3,
        note="Cambiar el algoritmo redujo el SCI unas 146 veces en cualquier red; cambiar de una red de 700 a una de 50 lo redujo unas 4,2 veces. Con la red limpia, el término de emisiones incorporadas del hardware pasa a ser cerca de tres cuartas partes del total del caso eficiente: bajar la energía deja de bastar y empieza a importar usar menos servidor. Los tiempos varían entre ejecuciones (la razón estuvo entre 75 y 170 en las repeticiones del autor).",
        note_kind="gold", foot=MED)


FIGURES = {"se-353-movimiento-lateral-y-confianza-cero.svg": se353_movimiento_lateral,
           "se-356-emisiones-por-tarea-sci.svg": se356_sci}
