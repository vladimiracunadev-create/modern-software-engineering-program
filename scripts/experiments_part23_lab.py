"""Utilidades compartidas de los experimentos de la Parte 23 (runtimes y plataformas modernas).

Biblioteca estándar y NumPy. Los experimentos que usan bibliotecas opcionales (``wasmtime``,
``kyber-py``, ``dilithium-py``) las importan con ``optional`` y, si faltan, dicen exactamente
qué no se ejecutó y por qué, en lugar de simular un resultado.

Versiones con las que se obtuvieron los números del texto (Windows 11, CPython 3.12.9):
numpy 2.5.5, wasmtime 50.0.1, kyber-py 1.2.0, dilithium-py 1.5.1. El experimento de eBPF
se ejecutó en WSL2 (núcleo 6.18.58.1-microsoft-standard-WSL2) con Python 3.12.3.
"""
from __future__ import annotations

import importlib
import statistics
import time


def fmt(x, d=2):
    return f"{x:.{d}f}".replace(".", ",")


def table(rows):
    for r in rows:
        print("  " + " | ".join(str(c) for c in r))


def pct(values, q):
    ordered = sorted(values)
    idx = max(0, min(len(ordered) - 1, int(round(q * (len(ordered) - 1)))))
    return ordered[idx]


def median(values):
    return statistics.median(values)


def timeit_ms(fn, repeat=7, number=1):
    """Mediana de ``repeat`` mediciones, cada una de ``number`` llamadas, en milisegundos por llamada."""
    out = []
    for _ in range(repeat):
        t = time.perf_counter()
        for _ in range(number):
            fn()
        out.append((time.perf_counter() - t) * 1000 / number)
    return statistics.median(out)


def optional(name, why):
    """Importa un módulo opcional; si falta, imprime NO EJECUTADO y devuelve None."""
    try:
        return importlib.import_module(name)
    except ImportError:
        print(f"  NO EJECUTADO: falta el paquete «{name}» ({why}).")
        return None
