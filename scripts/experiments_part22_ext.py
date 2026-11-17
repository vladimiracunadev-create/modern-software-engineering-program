"""Experimento de ampliación de SE-268: prioridades fijas frente a plazo más cercano (EDF) bajo sobrecarga.

Simulación discreta (una unidad de tiempo por paso), conjuntos sintéticos con semilla fija, solo biblioteca estándar.
Uso: python scripts/experiments_part22_ext.py   (imprime una línea JSON)

Cinco tareas con plazo igual al periodo (elegido entre 10, 20, 25, 40, 50 y 100), tiempos de cómputo enteros y
utilización repartida con UUniFast. Un trabajo atrasado sigue ejecutando hasta terminar (no se aborta). Se
simulan 2 000 unidades de tiempo (10 hiperperiodos de 200).
"""
import json
import random
import sys

sys.stdout.reconfigure(encoding="utf-8")

PERIODOS = [10, 20, 25, 40, 50, 100]
HORIZONTE = 2000


def uunifast(rng, n, u):
    partes, resto = [], u
    for i in range(1, n):
        siguiente = resto * rng.random() ** (1.0 / (n - i))
        partes.append(resto - siguiente)
        resto = siguiente
    partes.append(resto)
    return partes


def generar(rng, n, u):
    periodos = sorted(rng.choice(PERIODOS) for _ in range(n))
    cs = [max(1, round(x * t)) for x, t in zip(uunifast(rng, n, u), periodos)]
    return list(zip(cs, periodos))


def simular(tareas, politica):
    """Devuelve, por tarea, el número de trabajos que superan su plazo."""
    fallos = [0] * len(tareas)
    activos = []  # [tarea, restante, liberación, plazo, fallado]
    for t in range(HORIZONTE):
        for i, (c, p) in enumerate(tareas):
            if t % p == 0:
                activos.append([i, c, t, t + p, False])
        if activos:
            if politica == "rm":
                j = min(activos, key=lambda a: (tareas[a[0]][1], a[2], a[0]))
            else:
                j = min(activos, key=lambda a: (a[3], a[2], a[0]))
            j[1] -= 1
            if j[1] == 0:
                activos.remove(j)
        for a in activos:
            if not a[4] and a[3] <= t + 1:
                a[4] = True
                fallos[a[0]] += 1
    return fallos


def main():
    salida = {}
    for u in (0.9, 1.0, 1.1, 1.2):
        rng = random.Random(268)
        conjuntos = [generar(rng, 5, u) for _ in range(300)]
        fila = {"u_real_media": round(sum(sum(c / p for c, p in s) for s in conjuntos) / len(conjuntos), 3)}
        for politica in ("rm", "edf"):
            sin_fallo = con_fallo = con_prioritaria = distintas = 0
            validacion = 0
            for s in conjuntos:
                f = simular(s, politica)
                if politica == "edf" and sum(c / p for c, p in s) <= 1.0 and sum(f):
                    validacion += 1  # EDF no debe fallar con U <= 1: contraste con la teoría
                if sum(f) == 0:
                    sin_fallo += 1
                else:
                    con_fallo += 1
                    distintas += sum(1 for x in f if x)
                    if f[0] > 0:
                        con_prioritaria += 1
            fila[politica] = {
                "fallos_con_u_real_menor_o_igual_1": validacion if politica == "edf" else None,
                "sin_fallos_pct": round(100 * sin_fallo / len(conjuntos), 1),
                "tareas_distintas_con_fallo_media": round(distintas / con_fallo, 2) if con_fallo else 0.0,
                "falla_la_mas_prioritaria_pct": round(100 * con_prioritaria / con_fallo, 1) if con_fallo else 0.0,
            }
        salida[str(u)] = fila
    print(json.dumps(salida, ensure_ascii=False))


if __name__ == "__main__":
    main()
