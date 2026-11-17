"""Experimento de ampliación de SE-386 (confianza cero): ventana de exposición de una credencial robada.

Modelo sintético con semilla fija, solo biblioteca estándar.
Uso: python scripts/experiments_part32_ext.py   (imprime una línea JSON)

Se roba una credencial en un instante cualquiera de su vida. Se distinguen dos robos: una COPIA filtrada (registro,
repositorio, copia de seguridad: el atacante tiene el valor pero no el equipo) y un EQUIPO comprometido (el atacante
puede pedir credenciales nuevas mientras la identidad siga válida). La detección tarda un tiempo lognormal (mediana
6 h, sigma 1,2) y el 25 % de los robos no se detecta en la ventana de observación de 720 h (30 días). Diseños:
A llave estática que rota cada 90 días y se revoca a mano 4 h tras detectar; B token portador de 1 h sin
revocación; C token portador de 15 min que se revoca al renovar; D token de 1 h atado a la clave del cliente
(mTLS o prueba de posesión) y política evaluada en cada solicitud, con propagación de la revocación de 1 min.
Supuestos del autor; no se midió ninguna organización.
"""
import json
import math
import random
import sys

sys.stdout.reconfigure(encoding="utf-8")

HORIZONTE_H = 720.0


def deteccion(rng):
    if rng.random() < 0.25:
        return None
    return rng.lognormvariate(math.log(6.0), 1.2)


def exposicion(rng, diseno, robo):
    d = deteccion(rng)
    if diseno == "A":
        restante = rng.uniform(0, 90 * 24)
        valor = d + 4.0 if d is not None else restante
        return min(valor, restante if d is None else valor, HORIZONTE_H)
    if diseno == "B":
        ttl = 1.0
        if robo == "copia":
            return rng.uniform(0, ttl)
        return min(HORIZONTE_H, d + rng.uniform(0, ttl)) if d is not None else HORIZONTE_H
    if diseno == "C":
        ttl = 0.25
        if robo == "copia":
            return rng.uniform(0, ttl)
        return min(HORIZONTE_H, d + rng.uniform(0, ttl)) if d is not None else HORIZONTE_H
    # D: la copia no sirve sin la clave; el equipo comprometido pierde acceso al propagarse la revocación
    if robo == "copia":
        return 0.0
    return min(HORIZONTE_H, d + 1.0 / 60.0) if d is not None else HORIZONTE_H


def p95(valores):
    ordenados = sorted(valores)
    return ordenados[int(0.95 * len(ordenados)) - 1]


def main():
    salida = {}
    for diseno in "ABCD":
        salida[diseno] = {}
        for robo in ("copia", "equipo"):
            rng = random.Random(386)
            valores = [exposicion(rng, diseno, robo) for _ in range(20000)]
            ordenados = sorted(valores)
            salida[diseno][robo] = {"media_h": round(sum(valores) / len(valores), 2),
                                    "mediana_h": round(ordenados[len(ordenados) // 2], 2), "p95_h": round(p95(valores), 2),
                                    "supera_1h_pct": round(100 * sum(1 for v in valores if v > 1.0) / len(valores), 1)}
    print(json.dumps(salida, ensure_ascii=False))


if __name__ == "__main__":
    main()
