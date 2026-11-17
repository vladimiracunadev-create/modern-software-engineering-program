"""Figura de ampliación de SE-200: cuello de botella de revisión en InnerSource (modelo sintético con semilla fija)."""
from __future__ import annotations

from figure_kit import Fig, line_chart

SINT = "Modelo sintético de cola con semilla fija (scripts/experiments_part16_ext.py); los parámetros son supuestos del autor."


def se200_innersource() -> Fig:
    cap = [14, 20, 28, 32, 36, 40]
    sin = [255.4, 85.5, 8.6, 3.0, 2.3, 1.9]
    con = [6.2, 1.0, 0.5, 0.4, 0.3, 0.2]
    return line_chart(
        "Días laborables hasta fusionar un aporte ajeno según las horas semanales de revisión del equipo anfitrión",
        "Líneas en escala logarítmica con la mediana de días hasta fusionar un aporte según las horas semanales que el equipo anfitrión dedica a revisar. Sin guía de contribución (3 rondas, 27 horas semanales de carga) la mediana es de 255,4 días con 14 horas, 85,5 con 20, 8,6 con 28, 3 con 32, 2,3 con 36 y 1,9 con 40. Con guía, plantilla y CI previo (1,5 rondas, 13,5 horas de carga) es de 6,2 días con 14 horas, 1 con 20, 0,5 con 28 y 0,2 con 40.",
        [("Sin guía: 3 rondas por aporte", list(zip(cap, sin)), "coral"),
         ("Con guía, plantilla y CI previo: 1,5 rondas", list(zip(cap, con)), "teal")],
        x_label="Horas semanales de revisión de aportes ajenos del equipo anfitrión",
        y_label="Mediana de días laborables hasta fusionar", log_y=True,
        x_ticks=[(14, "14"), (20, "20"), (28, "28"), (32, "32"), (36, "36"), (40, "40")],
        y_ticks=[0.1, 1, 10, 100, 1000], y_zero=False, vlines=[(27, "carga sin guía: 27 h")], point_labels="all", plot_h=320,
        note="La línea punteada marca la carga que cada modelo pide al anfitrión: 27 horas semanales sin guía y 13,5 con ella. A la izquierda de esa carga la cola crece sin tope (las cifras de 14 y 20 horas son del horizonte simulado de 1 000 aportes, no un valor de equilibrio); a la derecha el tiempo cae pero la guía sigue ahorrando semanas de espera. InnerSource no falla por falta de apertura sino por una capacidad de revisión menor que la carga que genera cada aporte.",
        note_kind="gold", foot=SINT)


FIGURES = {"se-200-cuello-de-revision-innersource.svg": se200_innersource}
