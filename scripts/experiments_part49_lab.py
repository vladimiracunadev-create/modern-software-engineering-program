"""Utilidades comunes de los experimentos de la Parte 49 (patrones agénticos y sistemas con LLM).

No se invoca ningún modelo de lenguaje. El «modelo» de estos experimentos es un componente sintético con
semilla fija: decide con una probabilidad de error declarada y cuenta llamadas y tokens aproximados.
Las partes que no son el modelo (herramientas, router, recuperación, diario SQLite, JSON-RPC por un proceso
real, planificador) son código real que se ejecuta y se mide.
"""
from __future__ import annotations

import random
import statistics
from dataclasses import dataclass, field


def approx_tokens(text: str) -> int:
    """Aproximación grosera: un token por cada cuatro caracteres (no es el tokenizador de ningún modelo)."""
    return max(1, len(text) // 4)


def pct(x: float, d: int = 1) -> str:
    return f"{100 * x:.{d}f} %".replace(".", ",")


def num(x: float, d: int = 1) -> str:
    return f"{x:.{d}f}".replace(".", ",")


def quantile(values, q: float) -> float:
    ordered = sorted(values)
    if not ordered:
        return 0.0
    idx = min(len(ordered) - 1, max(0, int(round(q * (len(ordered) - 1)))))
    return ordered[idx]


def mean(values) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def table(rows) -> None:
    for r in rows:
        print("  " + " | ".join(str(c) for c in r))


@dataclass
class Meter:
    """Cuenta llamadas al modelo y tokens de entrada/salida de una ejecución."""
    calls: int = 0
    tokens_in: int = 0
    tokens_out: int = 0
    log: list = field(default_factory=list)

    def call(self, prompt_tokens: int, out_tokens: int = 60) -> None:
        self.calls += 1
        self.tokens_in += prompt_tokens
        self.tokens_out += out_tokens

    @property
    def tokens(self) -> int:
        return self.tokens_in + self.tokens_out


def rng(seed: int) -> random.Random:
    return random.Random(seed)
