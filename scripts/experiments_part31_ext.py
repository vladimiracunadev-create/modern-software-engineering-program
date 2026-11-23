"""Experimento de ampliación de SE-378: controles de calidad de un lote y linaje a nivel de tabla o de columna.

Datos sintéticos, semilla fija, solo biblioteca estándar.
Uso: python scripts/experiments_part31_ext.py   (imprime una línea JSON)

Parte 1. Lotes de unas 1 000 filas de pedidos (importe lognormal, marcas de tiempo repartidas en 24 h). Se
inyecta un defecto por lote y se mide en qué fracción de 200 lotes salta cada control. La referencia
(volumen, media del importe) sale de 50 lotes sanos distintos. Umbral de volumen y de distribución: 3
desviaciones típicas del historial. Frescura: más de 2 h entre el fin del lote y la última marca.
Parte 2. Un grafo de 11 activos con linaje de columnas; se cuenta cuántos activos marca como afectados el
linaje de tablas y cuántos el de columnas al cambiar una columna de origen.
"""
import json
import math
import random
import statistics
import sys

sys.stdout.reconfigure(encoding="utf-8")

CONTROLES = ["no nulo", "único", "rango", "volumen", "distribución", "frescura", "esquema"]
DEFECTOS = [
    "sin defecto (falsa alarma)",
    "2 % de claves de cliente nulas",
    "1,5 % de identificadores repetidos",
    "1 % de importes negativos o enormes",
    "5 % de filas con importe ×100",
    "8 % de filas perdidas en silencio",
    "las últimas 6 h no llegan",
    "columna renombrada en el origen",
]


def lote(rng, defecto=None):
    n = max(100, round(rng.gauss(1000, 25)))
    filas = []
    for i in range(n):
        filas.append({"id": i, "cliente": rng.randrange(1, 400), "importe": math.exp(rng.gauss(3.5, 0.8)),
                      "hora": rng.uniform(0, 24)})
    esquema = ["id", "cliente", "importe", "hora"]
    if defecto == 1:
        for f in rng.sample(filas, round(0.02 * n)):
            f["cliente"] = None
    elif defecto == 2:
        for f in rng.sample(filas, round(0.015 * n)):
            f["id"] = rng.randrange(0, n)
    elif defecto == 3:
        for f in rng.sample(filas, round(0.01 * n)):
            f["importe"] = -f["importe"] if rng.random() < 0.5 else 1e7
    elif defecto == 4:
        for f in rng.sample(filas, round(0.05 * n)):
            f["importe"] *= 100
    elif defecto == 5:
        filas = rng.sample(filas, n - round(0.08 * n))
    elif defecto == 6:
        filas = [f for f in filas if f["hora"] < 18]
    elif defecto == 7:
        esquema = ["id", "cliente", "monto", "hora"]
    return filas, esquema


def referencia(rng):
    volumenes, medias = [], []
    for _ in range(50):
        filas, _ = lote(rng)
        volumenes.append(len(filas))
        medias.append(statistics.fmean(f["importe"] for f in filas))
    return (statistics.fmean(volumenes), statistics.stdev(volumenes),
            statistics.fmean(medias), statistics.stdev(medias))


def controles(filas, esquema, ref):
    vol_m, vol_s, med_m, med_s = ref
    ids = [f["id"] for f in filas]
    importes = [f["importe"] for f in filas]
    return {
        "no nulo": any(f["cliente"] is None for f in filas),
        "único": len(set(ids)) != len(ids),
        "rango": any(x < 0 or x > 100000 for x in importes),
        "volumen": abs(len(filas) - vol_m) > 3 * vol_s,
        "distribución": abs(statistics.fmean(importes) - med_m) > 3 * med_s,
        "frescura": 24 - max(f["hora"] for f in filas) > 2,
        "esquema": esquema != ["id", "cliente", "importe", "hora"],
    }


# Linaje: activo -> {columna: [(activo, columna) de origen]}
LINAJE = {
    "stg_orders": {"id": [("raw_orders", "id")], "cliente": [("raw_orders", "cliente")],
                   "importe": [("raw_orders", "importe")], "fecha": [("raw_orders", "fecha")]},
    "stg_customers": {"id": [("raw_customers", "id")], "pais": [("raw_customers", "pais")],
                      "email_hash": [("raw_customers", "email")]},
    "fct_orders": {"cliente": [("stg_orders", "cliente")], "fecha": [("stg_orders", "fecha")],
                   "importe_eur": [("stg_orders", "importe"), ("raw_fx", "tasa")]},
    "dim_customers": {"pais": [("stg_customers", "pais")]},
    "mart_ingreso_dia": {"fecha": [("fct_orders", "fecha")], "ingreso": [("fct_orders", "importe_eur")]},
    "mart_ingreso_pais": {"pais": [("dim_customers", "pais")], "ingreso": [("fct_orders", "importe_eur")]},
    "mart_recompra": {"cliente": [("fct_orders", "cliente")], "fecha": [("fct_orders", "fecha")]},
    "tablero_direccion": {"ingreso": [("mart_ingreso_dia", "ingreso")]},
    "tablero_paises": {"ingreso": [("mart_ingreso_pais", "ingreso")], "pais": [("mart_ingreso_pais", "pais")]},
}
ORIGENES = ["raw_orders", "raw_customers", "raw_fx"]


def afectados_columna(origen):
    marcados, frontera = set(), {origen}
    while frontera:
        siguiente = set()
        for activo, cols in LINAJE.items():
            for col, ups in cols.items():
                if any(u in frontera for u in ups) and (activo, col) not in marcados:
                    marcados.add((activo, col))
                    siguiente.add((activo, col))
        frontera = siguiente
    return {a for a, _ in marcados}


def afectados_tabla(tabla):
    marcados, frontera = set(), {tabla}
    while frontera:
        siguiente = set()
        for activo, cols in LINAJE.items():
            if activo not in marcados and any(u[0] in frontera for ups in cols.values() for u in ups):
                marcados.add(activo)
                siguiente.add(activo)
        frontera = siguiente
    return marcados


def main():
    rng = random.Random(330)
    ref = referencia(rng)
    matriz = []
    for d in range(len(DEFECTOS)):
        conteo = {c: 0 for c in CONTROLES}
        for _ in range(200):
            filas, esquema = lote(rng, d if d else None)
            for c, saltó in controles(filas, esquema, ref).items():
                conteo[c] += saltó
        matriz.append([round(100 * conteo[c] / 200, 1) for c in CONTROLES])
    cambios = [("raw_orders", "importe"), ("raw_orders", "fecha"), ("raw_customers", "email"), ("raw_fx", "tasa")]
    linaje = []
    for tabla, col in cambios:
        linaje.append([f"{tabla}.{col}", len(afectados_tabla(tabla)), len(afectados_columna((tabla, col)))])
    print(json.dumps({"controles": CONTROLES, "defectos": DEFECTOS, "matriz_pct": matriz,
                      "linaje_tabla_vs_columna": linaje, "activos_derivados": len(LINAJE)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
