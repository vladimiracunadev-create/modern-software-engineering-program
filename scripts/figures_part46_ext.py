"""Figura de ampliación de SE-562: qué detecta un verificador de la ficha de un sistema de IA (datos sintéticos, semilla fija)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars

SINT = "Datos sintéticos con semilla fija (scripts/experiments_part46_ext.py), 200 mutaciones; no es asesoría legal ni una evaluación de conformidad."


def se466_ficha() -> Fig:
    return grouped_bars(
        "Mutaciones de la ficha de un sistema de IA de alto riesgo que detecta un verificador automático",
        "Barras con el porcentaje de mutaciones detectadas de 200 aplicadas: 100 % de los 61 campos de evidencia borrados, 100 % de los 68 casos de alto riesgo declarados como riesgo mínimo con su redacción literal y 0 % de los 71 casos declarados como riesgo mínimo redactados con otras palabras.",
        ["Se borra un campo de evidencia (61 casos)", "Alto riesgo declarado «mínimo», redacción literal (68)", "Alto riesgo declarado «mínimo», otras palabras (71)"],
        [("Mutaciones detectadas", [100.0, 100.0, 0.0], "teal")],
        unit="% de las mutaciones detectadas", decimals=0, horizontal=True, label_w=300, ticks=[0, 25, 50, 75, 100],
        note="Un verificador por presencia y palabras clave es exacto con lo que mira y ciego a lo demás: no ve si el campo dice algo útil y no reconoce el mismo caso de uso con otra redacción. Sirve como control de que la ficha no falta, no como clasificación de riesgo. La clasificación la decide una persona competente con el texto del reglamento.",
        note_kind="coral", foot=SINT)


FIGURES = {"se-562-verificador-de-la-ficha-de-un-sistema-de-ia.svg": se466_ficha}
