"""Figura de ampliación de SE-386: ventana de exposición de una credencial robada según el diseño (modelo sintético)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars

SINT = "Modelo sintético con semilla fija (scripts/experiments_part32_ext.py), 20 000 robos por celda; los tiempos de detección son supuestos del autor."


def se386_exposicion() -> Fig:
    return grouped_bars(
        "Robos de credencial con acceso del atacante de más de una hora, según el diseño y el tipo de robo",
        "Barras agrupadas con el porcentaje de 20 000 robos simulados en que el atacante conserva acceso más de una hora. Con una copia filtrada: 100 % con una llave estática que rota cada 90 días y 0 % con un token de 1 h, con uno de 15 min y con un token atado a la clave del cliente. Con el equipo comprometido: 100 %, 98,1 %, 95,8 % y 95,0 % respectivamente.",
        ["A. Llave estática (rota a los 90 días)", "B. Token portador de 1 h sin revocación", "C. Token portador de 15 min que se revoca al renovar", "D. Token de 1 h atado a la clave del cliente"],
        [("Copia filtrada de la credencial", [100.0, 0.0, 0.0, 0.0], "gold"), ("Equipo comprometido", [100.0, 98.1, 95.8, 95.0], "coral")],
        unit="% de robos con acceso de más de 1 h", decimals=1, horizontal=True, label_w=270, ticks=[0, 25, 50, 75, 100],
        note="La vida corta y el atado a la clave anulan casi por completo el robo de una copia, pero casi no cambian el del equipo comprometido: el atacante pide credenciales nuevas hasta que alguien lo detecta, y el 25 % de los robos no se detecta en 30 días en el modelo. Lo que acota ese caso es la velocidad de detección y lo que la identidad robada puede alcanzar (microsegmentación), no el diseño de la credencial.",
        note_kind="gold", foot=SINT)


FIGURES = {"se-386-exposicion-de-una-credencial-robada.svg": se386_exposicion}
