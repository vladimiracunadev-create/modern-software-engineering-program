"""Figura de ampliación de SE-330: qué control de calidad detecta cada defecto de un lote (datos sintéticos, semilla fija)."""
from __future__ import annotations

from figure_kit import Fig, heatmap

SINT = "Datos sintéticos con semilla fija (scripts/experiments_part27_ext.py): 200 lotes de unas 1 000 filas por defecto, CPython 3.12.9 en Windows."


def se330_controles() -> Fig:
    return heatmap(
        "Porcentaje de lotes en que salta cada control de calidad según el defecto inyectado",
        "Mapa de calor con el porcentaje de 200 lotes en que salta cada uno de siete controles según el defecto inyectado. Los nulos solo los detecta el control de no nulo, los identificadores repetidos solo el de unicidad, los importes fuera de rango el de rango y el de distribución, el importe por cien solo el de distribución, la pérdida silenciosa del 8 % de filas solo el de volumen en el 53 % de los lotes, la ausencia de las últimas 6 horas el de volumen y el de frescura, y la columna renombrada solo el de esquema. Un lote sano dispara el volumen o la distribución el 0,5 % de las veces.",
        ["Sin defecto (falsa alarma)", "2 % de clientes nulos", "1,5 % de identificadores repetidos", "1 % de importes negativos o enormes",
         "5 % de filas con importe ×100", "8 % de filas perdidas en silencio", "Las últimas 6 h no llegan", "Columna renombrada en el origen"],
        ["No nulo", "Único", "Rango", "Volumen", "Distribución", "Frescura", "Esquema"],
        [[0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0], [100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0],
         [0.0, 0.0, 100.0, 0.0, 100.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 100.0, 0.0, 0.0], [0.0, 0.0, 0.0, 53.0, 0.0, 0.0, 0.0],
         [0.0, 0.0, 0.0, 100.0, 0.0, 100.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0]],
        unit="% de lotes con alerta", row_title="Defecto inyectado", col_title="Control de calidad", suffix=" %", decimals=1,
        highlight=[(5, 3)], label_w=250, scale="teal",
        note="Cada defecto tiene casi siempre un único control que lo ve: un conjunto de controles es una cobertura, no una redundancia. El 8 % de filas perdidas es el caso débil: con 3 desviaciones típicas de umbral el volumen lo detecta en el 53 % de los lotes (marcado), y el resto pasa. Bajar el umbral sube las falsas alarmas del lote sano. Los defectos y el generador son del autor, no una muestra de datos reales.",
        note_kind="gold", foot=SINT)


FIGURES = {"se-330-cobertura-de-controles-de-calidad.svg": se330_controles}
