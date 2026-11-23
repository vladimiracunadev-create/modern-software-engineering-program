"""Laboratorio común de la Parte 50 (machine learning en producción y MLOps).

Genera el caso conductor *Avisos-ML*: un modelo que estima la probabilidad de que un estudiante
entregue tarde una tarea, para decidir a quién se envía un recordatorio. Todo es sintético y
determinista (semilla fija 46); no hay datos reales, ni GPU, ni modelos de lenguaje.

Versiones con las que se ejecutó la parte: numpy 2.4.4, scikit-learn 1.8.0, scipy 1.17.1 y CPython
3.12.9 en Windows 11 (ver ``scripts/requirements-part46.txt``). Si las versiones difieren, el
programa lo avisa en la salida: los recuentos pueden cambiar en la última cifra.
"""
from __future__ import annotations

import hashlib
import json
import sys
import time

import numpy as np

SEED = 46
PINNED = {"numpy": "2.4.4", "scikit-learn": "1.8.0"}
FEATURES = ["hours_left", "late_rate", "read_rate", "load", "mobile", "night"]


def check_versions() -> str:
    import sklearn

    got = {"numpy": np.__version__, "scikit-learn": sklearn.__version__}
    diff = [f"{k} {v} (fijada {PINNED[k]})" for k, v in got.items() if v != PINNED[k]]
    return "versiones: " + ", ".join(f"{k} {v}" for k, v in got.items()) + (
        "  AVISO: distinto de lo fijado -> " + "; ".join(diff) if diff else "  (coinciden con las fijadas)")


def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))


def make_data(n: int, seed: int = SEED, *, load_shift: float = 0.0, concept: float = 1.0, read_shift: float = 0.0,
              group_gap: float = 0.0, label_noise: float = 0.0, intercept: float = -1.2):
    """Devuelve (X, y, grupo). ``concept`` multiplica el peso de ``late_rate`` (deriva de concepto),
    ``load_shift`` y ``read_shift`` mueven las entradas (deriva de covariables) y ``group_gap`` hace
    que el grupo 1 tenga menos conectividad (más entregas tardías a igual perfil)."""
    rng = np.random.default_rng(seed)
    hours_left = rng.exponential(72.0, n) + 1.0
    late_rate = rng.beta(2.0, 6.0, n)
    read_rate = np.clip(rng.beta(5.0, 2.5, n) + read_shift, 0.0, 1.0)
    load = rng.poisson(3.0 + load_shift, n).astype(float)
    mobile = (rng.random(n) < 0.55).astype(float)
    night = (rng.random(n) < 0.30).astype(float)
    group = (rng.random(n) < 0.30).astype(int)
    z = (intercept + 7.0 * concept * late_rate - 3.6 * read_rate + 0.42 * load - 0.022 * hours_left
         + 0.45 * night + 0.35 * mobile + group_gap * group)
    y = (rng.random(n) < sigmoid(z)).astype(int)
    if label_noise > 0:
        flip = rng.random(n) < label_noise
        y = np.where(flip, 1 - y, y)
    X = np.column_stack([hours_left, late_rate, read_rate, load, mobile, night])
    return X, y, group


def auc(y, p) -> float:
    from sklearn.metrics import roc_auc_score
    return float(roc_auc_score(y, p))


def fit_logistic(X, y, seed: int = SEED, C: float = 1.0):
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    return make_pipeline(StandardScaler(), LogisticRegression(C=C, max_iter=500, random_state=seed)).fit(X, y)


def fit_forest(X, y, seed: int = SEED, n: int = 60, depth: int | None = 8):
    from sklearn.ensemble import RandomForestClassifier
    return RandomForestClassifier(n_estimators=n, max_depth=depth, random_state=seed, n_jobs=1).fit(X, y)


def fit_hgb(X, y, seed: int = SEED, iters: int = 80):
    from sklearn.ensemble import HistGradientBoostingClassifier
    return HistGradientBoostingClassifier(max_iter=iters, learning_rate=0.1, random_state=seed).fit(X, y)


def sha(obj) -> str:
    if isinstance(obj, np.ndarray):
        data = np.ascontiguousarray(obj).tobytes()
    else:
        data = json.dumps(obj, sort_keys=True, default=str).encode()
    return hashlib.sha256(data).hexdigest()[:12]


def fmt(x, d: int = 3) -> str:
    return f"{x:.{d}f}".replace(".", ",")


def table(headers, rows) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def timed(fn, repeat: int = 7):
    """Mejor tiempo de ``repeat`` ejecuciones (como timeit): reduce el ruido de otros procesos."""
    best = []
    for _ in range(repeat):
        t0 = time.perf_counter()
        fn()
        best.append(time.perf_counter() - t0)
    return float(np.min(best))


def run_cli(experiments: dict, header: str) -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    print(header)
    print(check_versions())
    want = sys.argv[1:] or sorted(experiments)
    for key in want:
        if key not in experiments:
            print(f"clase desconocida: {key}; disponibles: {', '.join(sorted(experiments))}")
            return 2
        print(f"\n===== SE-{key} =====")
        experiments[key]()
    return 0
