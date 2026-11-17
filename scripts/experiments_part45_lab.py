"""Utilidades compartidas de los experimentos de la Parte 45 (ingeniería de datos).

Todo es biblioteca estándar (sqlite3, zlib, struct, array, hashlib, hmac, tempfile). Los datos son
sintéticos y se generan con semilla fija 45; las lecturas de reloj y los tamaños de archivo se miden de
verdad y varían de un equipo a otro, mientras que los recuentos y las simulaciones se repiten idénticos.
"""
from __future__ import annotations

import sqlite3
import time


SEED = 45


def pct(values, q):
    """Percentil por rango más cercano (sin interpolar), estable entre plataformas."""
    ordered = sorted(values)
    idx = max(0, min(len(ordered) - 1, int(round(q * (len(ordered) - 1)))))
    return ordered[idx]


def fmt(x, d=2):
    return f"{x:.{d}f}".replace(".", ",")


def table(rows):
    for r in rows:
        print("  " + " | ".join(str(c) for c in r))


def timed(fn, repeat=3):
    """Mejor de ``repeat`` ejecuciones en milisegundos y el último resultado."""
    best, out = None, None
    for _ in range(repeat):
        t = time.perf_counter()
        out = fn()
        ms = (time.perf_counter() - t) * 1000
        best = ms if best is None else min(best, ms)
    return best, out


def mem_db():
    con = sqlite3.connect(":memory:")
    con.execute("PRAGMA synchronous=OFF")
    return con
