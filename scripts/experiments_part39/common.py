"""Utilidades compartidas de los experimentos de la Parte 39 (herramienta de autor, no se publica)."""
import hashlib, io, json, os, random, tarfile, zipfile, time

def sha(b): return hashlib.sha256(b).hexdigest()

def synthetic_tree(n=40, seed=7):
    """Árbol de fuentes sintético, siempre con los mismos bytes (LF)."""
    rng = random.Random(seed)
    files = {}
    for i in range(n):
        body = "".join(f"def f{i}_{j}(x):\n    return x * {rng.randint(2, 99)} + {j}\n\n" for j in range(rng.randint(3, 9)))
        files[f"entregas/mod_{i:02d}.py"] = body.encode()
    files["entregas/__init__.py"] = b'__version__ = "1.4.0"\n'
    files["pyproject.toml"] = b'[project]\nname = "entregas-api"\nversion = "1.4.0"\n'
    return files
