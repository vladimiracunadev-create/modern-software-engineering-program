"""Map figure of the failure-cases page (casos/fallo/README.md)."""
from __future__ import annotations

from figure_kit import Fig
from figures_case_exito import _columns


def mapa() -> Fig:
    return _columns(
        "Mapa de los fallos: cómo se rompió cada sistema y qué parte del curso lo previene",
        "Diagrama de cuatro columnas: cada una nombra una familia de fallo, enlaza con flechas a los casos que la ilustran y señala las partes del curso que dan las defensas. Cambio sin control en producción: Knight Capital y CrowdStrike. Migración o lanzamiento sin ensayo: HealthCare.gov y TSB. Operación y recuperación: la caída de Meta y el incidente de GitLab. Seguridad crítica y negocio: Therac-25 y Quibi.",
        [
            ("Cambio sin control en producción", "coral", ["Knight Capital", "CrowdStrike"],
             "Partes 35, 39 y 40: pruebas, release y despliegue progresivo"),
            ("Migración o lanzamiento sin ensayo", "gold", ["HealthCare.gov", "TSB Bank"],
             "Partes 15, 36 y 43: planificación, carga y modernización"),
            ("Operación y recuperación", "navy", ["Caída de Meta", "GitLab 2017"],
             "Partes 29, 33 y 41: respaldos, infraestructura e incidentes"),
            ("Seguridad crítica y negocio", "teal", ["Therac-25", "Quibi"],
             "Partes 10, 11 y 24: producto, economía y software crítico"),
        ],
        width=1000,
    )


FIGURES = {"fallo-mapa.svg": mapa}
