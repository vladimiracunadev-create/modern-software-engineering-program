"""Laboratorio común de la Parte 48: un harness mínimo en la biblioteca estándar.

El «modelo» es una política guionizada y determinista (no se invoca ningún modelo de lenguaje): sirve para
medir qué hace el *harness* (contexto, herramientas, permisos, bucle, parada, verificación, trazas) y no
qué haría un modelo real. Todo el trabajo de archivos ocurre en directorios temporales.
"""
from __future__ import annotations

import json
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------- tareas sintéticas
TASKS = {
    "T1": dict(
        files={"calc.py": "def add(a, b):\n    return a - b\n",
               "test_calc.py": "import unittest\nfrom calc import add\n\nclass T(unittest.TestCase):\n    def test_add(self):\n        self.assertEqual(add(2, 3), 5)\n        self.assertEqual(add(-1, 1), 0)\n\nif __name__ == '__main__':\n    unittest.main()\n"},
        target="calc.py", fixes=[("return a - b", "return a + b"), ("return a - b", "return a + b")]),
    "T2": dict(
        files={"calc.py": "def clamp(x, lo, hi):\n    return min(lo, max(hi, x))\n",
               "test_calc.py": "import unittest\nfrom calc import clamp\n\nclass T(unittest.TestCase):\n    def test_clamp(self):\n        self.assertEqual(clamp(5, 0, 3), 3)\n        self.assertEqual(clamp(-2, 0, 3), 0)\n        self.assertEqual(clamp(2, 0, 3), 2)\n\nif __name__ == '__main__':\n    unittest.main()\n"},
        target="calc.py", fixes=[("return min(lo, max(hi, x))", "return max(lo, min(hi, x))"), ("return min(lo, max(hi, x))", "return max(lo, min(hi, x))")]),
    "T3": dict(
        files={"calc.py": "def is_even(n):\n    return n % 2 == 1\n",
               "test_calc.py": "import unittest\nfrom calc import is_even\n\nclass T(unittest.TestCase):\n    def test_even(self):\n        self.assertTrue(is_even(4))\n        self.assertFalse(is_even(7))\n        self.assertTrue(is_even(0))\n\nif __name__ == '__main__':\n    unittest.main()\n"},
        target="calc.py", fixes=[("return n % 2 == 1", "return n % 2 == 0"), ("return n % 2 == 1", "return n % 2 == 0")]),
    "T4": dict(
        files={"calc.py": "def percent(part, whole):\n    return part / whole\n",
               "test_calc.py": "import unittest\nfrom calc import percent\n\nclass T(unittest.TestCase):\n    def test_percent(self):\n        self.assertEqual(percent(1, 4), 25)\n        self.assertEqual(percent(1, 2), 50)\n\nif __name__ == '__main__':\n    unittest.main()\n"},
        target="calc.py", fixes=[("return part / whole", "return part / whole * 10"), ("return part / whole", "return part / whole * 100")]),
    "T5": dict(
        files={"calc.py": "def words(s):\n    return len(s.split(' '))\n",
               "test_calc.py": "import unittest\nfrom calc import words\n\nclass T(unittest.TestCase):\n    def test_words(self):\n        self.assertEqual(words('a b  c'), 3)\n        self.assertEqual(words('  a'), 1)\n\nif __name__ == '__main__':\n    unittest.main()\n"},
        target="calc.py", fixes=[("len(s.split(' '))", "len(s.strip().split(' '))"), ("len(s.split(' '))", "len(s.split())")]),
    "T6": dict(
        files={"calc.py": "def median(xs):\n    return xs[len(xs) // 2]\n",
               "test_calc.py": "import unittest\nfrom calc import median\n\nclass T(unittest.TestCase):\n    def test_median(self):\n        self.assertEqual(median([3, 1, 2]), 2)\n        self.assertEqual(median([4, 1, 3, 2]), 2.5)\n\nif __name__ == '__main__':\n    unittest.main()\n"},
        target="calc.py", fixes=[("return xs[len(xs) // 2]", "return sorted(xs)[len(xs) // 2]"),
                                  ("return xs[len(xs) // 2]", "s = sorted(xs)\n    m = len(s) // 2\n    return s[m] if len(s) % 2 else (s[m - 1] + s[m]) / 2")]),
}

INSTR_VERIFY = "Antes de declarar la tarea terminada, ejecuta las pruebas y confirma que pasan."


# ---------------------------------------------------------------- política guionizada
def scripted_policy(task: dict, history: list[dict], tools: set[str], instructions: str) -> dict:
    """Stand-in determinista de un modelo. Solo decide con lo que ve en `history`."""
    if not history:
        return {"tool": "read", "args": {"path": task["target"]}}
    writes = [h for h in history if h["action"].get("tool") == "write"]
    tests = [h for h in history if h["action"].get("tool") == "run_tests"]
    if not writes:
        if "write" not in tools:
            return {"tool": "read", "args": {"path": task["target"]}}
        old, new = task["fixes"][0]
        return {"tool": "write", "args": {"path": task["target"], "old": old, "new": new}}
    verifies = INSTR_VERIFY in instructions and "run_tests" in tools
    if verifies and (not tests or history[-1]["action"].get("tool") == "write"):
        return {"tool": "run_tests", "args": {}}
    if verifies and tests and "FAIL" in tests[-1]["obs"] and len(writes) == 1:
        old, _ = task["fixes"][1]
        cur_new = task["fixes"][0][1]
        return {"tool": "write", "args": {"path": task["target"], "old": cur_new, "new": task["fixes"][1][1]}}
    return {"done": True}


# ---------------------------------------------------------------- permisos
SAFE_CMDS = {"git": {"status", "diff", "log"}, "python": {"-m"}, "ls": None, "cat": None}
DENIED_NAMES = {".env", "id_rsa", "config"}
OPERATORS = re.compile(r"[;&|`<>\n]|\$\(|\$\{")


def naive_allows(cmd: str, allowed_prefixes=("git status", "git diff", "git log", "python -m unittest", "ls", "cat ")) -> bool:
    return any(cmd.startswith(p) for p in allowed_prefixes)


def parsed_allows(cmd: str, root: Path) -> tuple[bool, str]:
    if "\\" in cmd:
        return False, "barra invertida"
    if OPERATORS.search(cmd):
        return False, "operador de shell"
    try:
        parts = shlex.split(cmd, posix=True)
    except ValueError:
        return False, "comillas sin cerrar"
    if not parts:
        return False, "vacío"
    if "=" in parts[0]:
        return False, "asignación de entorno"
    prog, args = parts[0], parts[1:]
    if prog not in SAFE_CMDS:
        return False, "programa fuera de la lista"
    sub = SAFE_CMDS[prog]
    if prog == "git" and (not args or args[0] not in sub):
        return False, "subcomando git no permitido"
    if prog == "python" and args[:2] != ["-m", "unittest"]:
        return False, "solo python -m unittest"
    for a in args:
        if a.startswith("-") and prog in ("git",) and a in ("--output", "-c"):
            return False, "opción peligrosa"
        if "/" in a or "\\" in a or a in DENIED_NAMES or a.startswith(".."):
            p = (root / a).resolve()
            if not p.is_relative_to(root.resolve()):
                return False, "ruta fuera de la raíz"
            if p.name in DENIED_NAMES:
                return False, "archivo protegido"
        elif a in DENIED_NAMES:
            return False, "archivo protegido"
    return True, "permitido"


# ---------------------------------------------------------------- harness
@dataclass
class Config:
    context: bool = True
    tools: set = field(default_factory=lambda: {"read", "write", "run_tests"})
    max_steps: int = 12
    accept_done: bool = True
    instructions: str = INSTR_VERIFY
    confine: bool = True
    deny_write: set = field(default_factory=set)
    policy: object = None
    require_verify: bool = False
    no_progress: int = 0
    protect_tests: bool = False


class Harness:
    def __init__(self, cfg: Config):
        self.cfg = cfg

    def run(self, task_id: str, root: Path | None = None) -> dict:
        task = TASKS[task_id]
        own = root is None
        outer = Path(tempfile.mkdtemp(prefix="h41_")) if own else None
        if own:
            base = outer / "ws"
            base.mkdir()
            (outer / "fuera.txt").write_text("contenido-fuera", encoding="utf-8")
        else:
            base = root
        policy = self.cfg.policy or scripted_policy
        try:
            for name, text in task["files"].items():
                (base / name).write_text(text, encoding="utf-8")
            original_tests = (base / "test_calc.py").read_text(encoding="utf-8")
            history: list[dict] = []
            trace: list[dict] = []
            done = False
            stop_reason = "tope de pasos"
            denied = 0
            repeats = 0
            last_sig = None
            iters = 0
            for step in range(1, self.cfg.max_steps + 1):
                iters = step
                visible = history if self.cfg.context else []
                action = policy(task, visible, self.cfg.tools, self.cfg.instructions)
                meta = {"ctx": len(visible), "tools": sorted(self.cfg.tools)}
                if action.get("done"):
                    verified = any(h["action"].get("tool") == "run_tests" and h["obs"] == "PASS" for h in history)
                    if self.cfg.require_verify and not verified:
                        trace.append({"step": step, "event": "done_rechazado_sin_verificacion", **meta})
                        history.append({"action": action, "obs": "DONE-RECHAZADO"})
                        if "run_tests" in self.cfg.tools:
                            obs, ok = self.dispatch({"tool": "run_tests", "args": {}}, base)
                            history.append({"action": {"tool": "run_tests", "args": {}}, "obs": obs})
                            trace.append({"step": step, "tool": "run_tests", "ok": ok, "obs": obs, **meta})
                        sig = ("rechazo", obs if "run_tests" in self.cfg.tools else "")
                        repeats = repeats + 1 if sig == last_sig else 1
                        last_sig = sig
                        if self.cfg.no_progress and repeats >= self.cfg.no_progress:
                            stop_reason = "sin progreso"
                            break
                        continue
                    trace.append({"step": step, "event": "done_requested", **meta})
                    if self.cfg.accept_done:
                        done, stop_reason = True, "declarada terminada"
                        break
                    history.append({"action": action, "obs": "STOP-IGNORADO"})
                    continue
                obs, ok = self.dispatch(action, base)
                if obs in ("ESCRITURA-DENEGADA", "FUERA-DE-LA-RAIZ", "HERRAMIENTA-NO-DISPONIBLE"):
                    denied += 1
                trace.append({"step": step, "tool": action["tool"], "ok": ok, "obs": obs[:14], **meta})
                history.append({"action": action, "obs": obs})
                sig = (action["tool"], repr(action["args"]), obs)
                repeats = repeats + 1 if sig == last_sig else 1
                last_sig = sig
                if self.cfg.no_progress and repeats >= self.cfg.no_progress:
                    stop_reason = "sin progreso"
                    break
            passed = self.tests_pass(base)
            tampered = (base / "test_calc.py").read_text(encoding="utf-8") != original_tests
            return {"task": task_id, "steps": iters, "declared_done": done, "passed": passed,
                    "trace": trace, "tampered": tampered, "stop_reason": stop_reason, "denied": denied,
                    "leaked": any(h["obs"] == "contenido-fuera" for h in history)}
        finally:
            if own:
                shutil.rmtree(outer, ignore_errors=True)

    def dispatch(self, action: dict, base: Path) -> tuple[str, bool]:
        tool, args = action["tool"], action["args"]
        if tool not in self.cfg.tools:
            return "HERRAMIENTA-NO-DISPONIBLE", False
        if tool == "read":
            p = self.safe_path(base, args["path"])
            if not p:
                return "FUERA-DE-LA-RAIZ", False
            return (p.read_text(encoding="utf-8") if p.exists() else "NO-EXISTE"), p.exists()
        if tool == "write":
            p = self.safe_path(base, args["path"])
            if not p or p.name in self.cfg.deny_write or (self.cfg.protect_tests and p.name.startswith("test_")):
                return "ESCRITURA-DENEGADA", False
            text = p.read_text(encoding="utf-8")
            if args["old"] not in text:
                return "NO-ENCONTRADO", False
            p.write_text(text.replace(args["old"], args["new"], 1), encoding="utf-8")
            return "OK", True
        if tool == "run_tests":
            ok = self.tests_pass(base)
            return ("PASS" if ok else "FAIL"), True
        return "DESCONOCIDA", False

    def safe_path(self, base: Path, rel: str):
        p = (base / rel).resolve()
        if self.cfg.confine and not p.is_relative_to(base.resolve()):
            return None
        return p

    @staticmethod
    def tests_pass(base: Path) -> bool:
        r = subprocess.run([sys.executable, "-B", "-m", "unittest", "-q", "test_calc"], cwd=base,
                           capture_output=True, text=True, timeout=60)
        return r.returncode == 0


def pct(x: float, d: int = 0) -> str:
    return f"{100 * x:.{d}f} %".replace(".", ",")


def table(rows) -> None:
    for r in rows:
        print("  " + " | ".join(str(c) for c in r))


if __name__ == "__main__":
    h = Harness(Config())
    for t in TASKS:
        r = h.run(t)
        print(t, r["passed"], r["steps"])
