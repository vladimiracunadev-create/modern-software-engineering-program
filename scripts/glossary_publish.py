#!/usr/bin/env python3
"""Publica en main los cambios del glosario sin dejar archivos generados desactualizados.

Varias sesiones escriben entradas a la vez y todas regeneran los mismos archivos
(glosario/entradas, índices, README, STATUS, portal). Un empuje hecho sobre un árbol que no
incluye el último commit ajeno deja esos archivos viejos y el CI se pone rojo. Este guion hace
siempre lo mismo, en este orden, y repite hasta que el empuje entra:

  1. git fetch + git rebase origin/main (los conflictos en archivos GENERADOS se resuelven
     tomando la versión de main; un conflicto en archivos escritos a mano aborta y se informa).
  2. Regenera todo (glosario, README/STATUS/portal, clases publicadas, guías de rol).
  3. Valida (validate_glossary.py y build_phase2.py --check).
  4. Si la regeneración cambió algo, lo confirma en un commit «chore(glosario): regenerar».
  5. git push origin HEAD:main; si main avanzó entre medias, vuelve al paso 1.

Uso:  python scripts/glossary_publish.py            (publica)
      python scripts/glossary_publish.py --no-push  (solo rebase + regeneración + validación)
Requisito: tus cambios escritos a mano (glosario/curado/*.md) ya están commiteados.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAX_TRIES = 8
# Rutas que NUNCA se resuelven solas (se escriben a mano): un conflicto aquí aborta.
HAND_WRITTEN = ("glosario/curado/", "docs/PART-EXECUTION-TRACKER.md", "CHANGELOG.md", "content/", "casos/")
GENERATORS = (
    "build_glossary.py",
    "build_phase2.py",
    "build_phase3.py",
    "build_phase4.py",
    "build_role_guides.py",
)
CHECKS = (
    ("validate_glossary.py",),
    ("build_phase2.py", "--check"),
)


def git(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["git", *args], cwd=ROOT, text=True, capture_output=True, encoding="utf-8", check=check)


def py(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, "-X", "utf8", *args], cwd=ROOT, text=True, capture_output=True, encoding="utf-8")


def conflicted() -> list[str]:
    return [p for p in git("diff", "--name-only", "--diff-filter=U", check=False).stdout.split("\n") if p]


def rebase() -> bool:
    git("fetch", "origin")
    result = git("rebase", "origin/main", check=False)
    while result.returncode != 0:
        files = conflicted()
        if not files:
            print(result.stdout + result.stderr)
            git("rebase", "--abort", check=False)
            return False
        for path in files:
            if path.startswith(HAND_WRITTEN):
                print(f"CONFLICTO en un archivo escrito a mano: {path}. Resuélvelo tú y vuelve a ejecutar.")
                git("rebase", "--abort", check=False)
                return False
        for path in files:
            # durante un rebase «ours» es la rama que se reconstruye = main
            git("checkout", "--ours", "--", path, check=False)
            git("add", path)
        result = subprocess.run(
            ["git", "-c", "core.editor=true", "rebase", "--continue"], cwd=ROOT, text=True, capture_output=True, encoding="utf-8"
        )
    return True


def regenerate() -> bool:
    for script in GENERATORS:
        out = py(f"scripts/{script}")
        if out.returncode != 0:
            print(f"FALLÓ {script}:\n{out.stdout[-1500:]}\n{out.stderr[-1500:]}")
            return False
    # ruido de saltos de línea en figuras: se descarta lo que solo cambió por eso
    modified = [p for p in git("ls-files", "-m").stdout.split("\n") if "/figures/" in p]
    # por lotes: en Windows la línea de comandos tiene un límite de largo (WinError 206)
    for start in range(0, len(modified), 100):
        git("checkout", "--", *modified[start : start + 100], check=False)
    return True


def validate() -> bool:
    for cmd in CHECKS:
        out = py(f"scripts/{cmd[0]}", *cmd[1:])
        if out.returncode != 0:
            print(f"VALIDACIÓN FALLÓ ({' '.join(cmd)}):\n{out.stdout[-1500:]}\n{out.stderr[-1500:]}")
            return False
    return True


def main() -> int:
    push = "--no-push" not in sys.argv
    if git("status", "--porcelain", "--untracked-files=no").stdout.strip():
        print("Hay cambios sin commitear. Confirma primero tus entradas (glosario/curado/*.md).")
        return 2
    for attempt in range(1, MAX_TRIES + 1):
        print(f"--- intento {attempt}/{MAX_TRIES}")
        if not rebase():
            return 3
        if not regenerate() or not validate():
            return 4
        if git("status", "--porcelain", "--untracked-files=no").stdout.strip():
            git("add", "-A")
            git("commit", "-m", "chore(glosario): regenerar archivos generados tras integrar main")
        if not push:
            print("OK (sin empujar).")
            return 0
        result = git("push", "origin", "HEAD:main", check=False)
        if result.returncode == 0:
            print("OK: publicado en main. Espera el CI (Validate, Pages, Security).")
            return 0
        print("main avanzó o el empuje fue rechazado; reintento.\n" + result.stderr[-400:])
    print("No se pudo publicar tras varios intentos.")
    return 5


if __name__ == "__main__":
    sys.exit(main())
