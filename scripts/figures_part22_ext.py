"""Figura de ampliación de SE-268: sobrecarga con prioridades fijas frente a plazo más cercano (simulación con semilla fija)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars

SINT = "Simulación discreta con semilla fija (scripts/experiments_part22_ext.py): 300 conjuntos de 5 tareas por celda, CPython 3.12.9 en Windows."


def se268_sobrecarga() -> Fig:
    return grouped_bars(
        "Cuántas de las 5 tareas pierden algún plazo cuando el conjunto fracasa, según la utilización objetivo",
        "Barras agrupadas con el número medio de tareas distintas, de cinco, que pierden algún plazo en los conjuntos que fracasan: con prioridades fijas por periodo 1,08 con utilización objetivo 0,9, 1,45 con 1,0, 1,91 con 1,1 y 2,22 con 1,2; con el plazo más cercano primero 4,44, 4,76, 5,00 y 5,00. La tarea más prioritaria nunca falla con prioridades fijas salvo el 0,7 % de los conjuntos con 1,1 y 1,2, y falla en el 100 % de los conjuntos que fracasan con el plazo más cercano.",
        ["Objetivo 0,9 (real 0,92)", "Objetivo 1,0 (real 1,02)", "Objetivo 1,1 (real 1,12)", "Objetivo 1,2 (real 1,22)"],
        [("Prioridades fijas por periodo", [1.08, 1.45, 1.91, 2.22], "teal"), ("Plazo más cercano primero (EDF)", [4.44, 4.76, 5.0, 5.0], "coral")],
        unit="Tareas distintas con algún plazo perdido (de 5)", decimals=2, ticks=[0, 1, 2, 3, 4, 5], ref_lines=[(5, "las cinco tareas")], plot_h=300,
        note="Con prioridades fijas la sobrecarga se concentra en las tareas de periodo largo y las de periodo corto siguen cumpliendo; con el plazo más cercano primero, una vez que el procesador no alcanza, todas las tareas se atrasan a la vez. Con utilización real igual o menor que 1, EDF no perdió ningún plazo en las 1 200 simulaciones. El objetivo y el valor real difieren porque los tiempos de cómputo son enteros y se redondean hacia arriba hasta 1 unidad.",
        note_kind="gold", foot=SINT)


FIGURES = {"se-268-sobrecarga-prioridades-fijas-y-edf.svg": se268_sobrecarga}
