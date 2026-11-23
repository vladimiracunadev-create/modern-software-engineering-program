"""Figura de ampliación de SE-597: curva de aprendizaje y evaluación contaminada de un clasificador con memoria (datos sintéticos)."""
from __future__ import annotations

from figure_kit import Fig, line_chart

SINT = "Datos sintéticos con semilla fija (scripts/experiments_part49_ext.py); un clasificador pequeño, no un modelo de lenguaje."


def se513_contaminacion() -> Fig:
    n = [10, 30, 100, 300, 1000, 3000]
    limpia = [56.1, 53.4, 70.8, 77.3, 80.6, 86.7]
    contaminada = [77.6, 76.6, 85.8, 88.9, 89.1, 93.2]
    bayes = [62.1, 69.1, 88.0, 97.5, 99.2, 99.7]
    return line_chart(
        "Exactitud de un clasificador según los ejemplos de entrenamiento, con evaluación limpia y contaminada",
        "Líneas con la exactitud en porcentaje frente al número de ejemplos de entrenamiento, en escala logarítmica. El clasificador de vecino más próximo, que memoriza, marca 56,1, 53,4, 70,8, 77,3, 80,6 y 86,7 con evaluación limpia y 77,6, 76,6, 85,8, 88,9, 89,1 y 93,2 cuando la mitad de los ejemplos de evaluación son copias del entrenamiento; el clasificador bayesiano ingenuo, con evaluación limpia, marca 62,1, 69,1, 88,0, 97,5, 99,2 y 99,7.",
        [("Vecino más próximo, evaluación limpia", list(zip(n, limpia)), "teal"),
         ("Vecino más próximo, evaluación con 50 % de copias", list(zip(n, contaminada)), "coral"),
         ("Bayesiano ingenuo, evaluación limpia", list(zip(n, bayes)), "navy")],
        x_label="Ejemplos de entrenamiento", y_label="Exactitud (%)", log_x=True,
        x_ticks=[(10, "10"), (30, "30"), (100, "100"), (300, "300"), (1000, "1 000"), (3000, "3 000")],
        y_ticks=[50, 60, 70, 80, 90, 100], y_zero=False, point_labels="none", plot_h=320,
        note="La contaminación suma al modelo que memoriza entre 6,5 y 23,2 puntos que no tiene (21,5 con 10 ejemplos, 23,2 con 30 y 6,5 con 3 000) y no mejora a ningún otro modelo: la medida deja de decir qué ocurrirá con ejemplos nuevos. La curva limpia es la que decide cuántos ejemplos conviene reunir, y aquí otro modelo con mejor sesgo para la tarea supera con 100 ejemplos al que memoriza con 3 000.",
        note_kind="gold", foot=SINT)


FIGURES = {"se-597-curva-de-aprendizaje-y-contaminacion.svg": se513_contaminacion}
