"""Figuras de ampliación de SE-390 y SE-391: conjuntos replicados sin conflicto y seguridad de un modelo reducido de elección y replicación."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars

SINT = "Modelos sintéticos con semilla fija (scripts/experiments_part32_ext.py), CPython 3.12.9 en Windows; no es Raft ni un conjunto de producción."


def se342_conjuntos() -> Fig:
    return grouped_bars(
        "Tres réplicas de un conjunto con entrega desordenada y duplicada: divergencia y cumplimiento de «el alta gana»",
        "Barras agrupadas con el porcentaje de 5 000 corridas en que las tres réplicas terminan con estados distintos y el porcentaje en que el estado final no cumple la regla de que un alta que ninguna baja observó permanece. Aplicar en orden de llegada diverge en el 87,6 % de las corridas e incumple la regla en el 93,2 %; el último escritor con relojes desfasados diverge en el 6,5 % e incumple la regla en el 41,3 %; el conjunto con etiquetas únicas (OR-Set) diverge en el 0 % e incumple la regla en el 0 %.",
        ["Aplicar en orden de llegada", "Último escritor con relojes desfasados", "OR-Set con etiquetas únicas"],
        [("Réplicas con estados distintos", [87.6, 6.5, 0.0], "coral"), ("Estado final que incumple «el alta gana»", [93.2, 41.3, 0.0], "gold")],
        unit="% de las 5 000 corridas", decimals=1, ticks=[0, 20, 40, 60, 80, 100], plot_h=290,
        note="Converger y ser correcto son propiedades distintas: el último escritor casi siempre converge (6,5 % de divergencia, por empates de reloj sin desempate) y aun así descarta altas concurrentes en el 41,3 % de las corridas. El OR-Set cumple ambas porque la baja solo quita lo que vio y la unión es conmutativa, asociativa e idempotente. El precio es que las etiquetas de las bajas se acumulan.",
        note_kind="gold", foot=SINT)


def se343_seguridad() -> Fig:
    return grouped_bars(
        "Calendarios aleatorios de 70 pasos con violación de seguridad según qué regla de Raft se quite",
        "Barras con el porcentaje de 20 000 calendarios aleatorios de 70 pasos sobre cinco nodos en que un líder elegido no tiene una entrada ya comprometida o se compromete una entrada distinta en un índice ya comprometido: 0 % con el modelo completo, 6,88 % si el voto no compara los registros y 0,06 % si el líder cuenta réplicas de entradas de mandatos anteriores para comprometer.",
        ["Reglas completas", "El voto no compara los registros", "Comprometer contando réplicas de mandatos anteriores"],
        [("Calendarios con violación de seguridad", [0.0, 6.88, 0.06], "coral")],
        unit="% de los 20 000 calendarios", decimals=2, ticks=[0, 2, 4, 6, 8], plot_h=260,
        note="Quitar la comparación de registros pierde entradas comprometidas en 1 377 calendarios de 20 000 (6,88 %). Quitar la regla de comprometer solo entradas del mandato actual produce 11 violaciones (0,06 %): un fallo real pero raro, que una prueba con pocos calendarios no vería. Las 0 violaciones del modelo completo en 20 000 calendarios no son una demostración de corrección.",
        note_kind="gold", foot=SINT)


FIGURES = {"se-390-conjuntos-replicados-sin-conflicto.svg": se342_conjuntos,
           "se-391-reglas-de-seguridad-de-un-modelo-de-raft.svg": se343_seguridad}
