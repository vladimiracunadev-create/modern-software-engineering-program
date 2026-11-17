"""Utilidades compartidas de los experimentos de la Parte 47 (sistemas críticos y tiempo real).

Todo es biblioteca estándar de Python. Caso conductor: *Horno de curado*, un controlador de
temperatura con un limitador independiente. Los parámetros (tasas de fallo, tiempos, valoraciones)
los fija el autor; son supuestos de modelo, no datos de un producto real.
"""
from __future__ import annotations

import itertools


def fmt(x, d=2):
    return f"{x:.{d}f}".replace(".", ",")


def sci(x, d=2):
    return f"{x:.{d}e}".replace(".", ",")


def table(rows):
    for r in rows:
        print("  " + " | ".join(str(c) for c in r))


def minimal(sets):
    """Quita los conjuntos que contienen a otro (cortes mínimos)."""
    sets = sorted({frozenset(s) for s in sets}, key=len)
    out = []
    for s in sets:
        if not any(o <= s for o in out):
            out.append(s)
    return out


def mocus(gate, gates):
    """Cortes mínimos de un árbol de fallos {nombre: ('and'|'or', [hijos])}; los no listados son eventos básicos."""
    def expand(node):
        if node not in gates:
            return [frozenset([node])]
        kind, kids = gates[node]
        parts = [expand(k) for k in kids]
        if kind == "or":
            return minimal([c for p in parts for c in p])
        combos = [frozenset()]
        for p in parts:
            combos = minimal([a | b for a in combos for b in p])
        return combos
    return expand(gate)


def exact_probability(gate, gates, p):
    """Probabilidad exacta del evento tope sumando sobre todos los estados de los eventos básicos."""
    basics = sorted({n for _, kids in gates.values() for n in kids if n not in gates})

    def ev(node, state):
        if node not in gates:
            return state[node]
        kind, kids = gates[node]
        vals = [ev(k, state) for k in kids]
        return all(vals) if kind == "and" else any(vals)

    total = 0.0
    for bits in itertools.product([False, True], repeat=len(basics)):
        state = dict(zip(basics, bits))
        if ev(gate, state):
            w = 1.0
            for n, b in state.items():
                w *= p[n] if b else 1 - p[n]
            total += w
    return total
