"""Experimentos de las clases SE-499 a SE-504 (Parte 41): harness y agentic engineering.

Uso: python scripts/experiments_part41_b.py [499|500|501|502|503|504]

No se invoca ningún modelo de lenguaje. Semilla fija en las simulaciones; archivos y repositorios Git reales
en directorios temporales.
"""
from __future__ import annotations

import ast
import math
import random
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path

import experiments_part41_lab as L
from experiments_part41_lab import pct, table


# ====================================================================== SE-499
def _gate_syntax(d: Path) -> bool:
    try:
        for f in d.glob("*.py"):
            compile(f.read_text(encoding="utf-8"), str(f), "exec")
        return True
    except SyntaxError:
        return False


def _gate_lint(d: Path) -> bool:
    tree = ast.parse((d / "pkg.py").read_text(encoding="utf-8"))
    imported = {a.asname or a.name.split(".")[0] for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom)) for a in n.names}
    used = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
    bad = bool(imported - used)
    for n in ast.walk(tree):
        if isinstance(n, ast.ExceptHandler) and n.type is None:
            bad = True
        if isinstance(n, ast.FunctionDef) and any(isinstance(x, (ast.List, ast.Dict)) for x in n.args.defaults):
            bad = True
        if isinstance(n, ast.Call) and getattr(n.func, "id", "") == "print":
            bad = True
    return not bad


def _gate_tests(d: Path) -> bool:
    r = subprocess.run([sys.executable, "-B", "-m", "unittest", "-q", "test_pkg"], cwd=d, capture_output=True, text=True, timeout=60)
    return r.returncode == 0


def _gate_secrets(d: Path) -> bool:
    return not any(re.search(r"ghp_[A-Za-z0-9]{20,}", f.read_text(encoding="utf-8")) for f in d.glob("*.py"))


def _gate_tests_not_weakened(d: Path, base_tests: str) -> bool:
    now = (d / "test_pkg.py").read_text(encoding="utf-8")
    return now.count("assert") >= base_tests.count("assert") and "skip" not in now


BASE_PKG = "def fee(amount):\n    if amount < 0:\n        raise ValueError('negativo')\n    return round(amount * 0.02, 2)\n\ndef total(items):\n    return sum(items)\n"
BASE_TEST = ("import unittest\nfrom pkg import fee, total\n\nclass T(unittest.TestCase):\n    def test_fee(self):\n        self.assertEqual(fee(100), 2.0)\n"
             "        self.assertRaises(ValueError, fee, -1)\n\n    def test_total(self):\n        self.assertEqual(total([1, 2, 3]), 6)\n\nif __name__ == '__main__':\n    unittest.main()\n")
SECRET_LINE = "TOKEN = '" + "ghp_" + "y" * 30 + "'\n"

CHANGES = {
    "D01 error de sintaxis": (BASE_PKG + "def broken(:\n    pass\n", BASE_TEST),
    "D02 importación sin usar": ("import os\n" + BASE_PKG, BASE_TEST),
    "D03 except desnudo": (BASE_PKG + "def safe(x):\n    try:\n        return fee(x)\n    except:\n        return 0\n", BASE_TEST),
    "D04 error de lógica que una prueba ve": (BASE_PKG.replace("0.02", "0.2"), BASE_TEST),
    "D05 secreto literal": (SECRET_LINE + BASE_PKG, BASE_TEST),
    "D06 prueba debilitada para ocultar el error": (BASE_PKG.replace("0.02", "0.2"), BASE_TEST.replace("        self.assertEqual(fee(100), 2.0)\n", "")),
    "D07 error de lógica que ninguna prueba ve": (BASE_PKG.replace("return sum(items)", "return sum(items[:-1]) + items[-1] if items else 0").replace("def total(items):", "def total(items):\n    if len(items) > 50:\n        return 0"), BASE_TEST),
    "D08 prueba que falla marcada como omitida": (BASE_PKG.replace("0.02", "0.2"), BASE_TEST.replace("    def test_fee", "    @unittest.skip('luego')\n    def test_fee")),
    "D09 argumento mutable por defecto": (BASE_PKG + "def acc(x, seen=[]):\n    seen.append(x)\n    return seen\n", BASE_TEST),
    "D10 impresión de depuración": (BASE_PKG.replace("    return round", "    print(amount)\n    return round"), BASE_TEST),
    "D11 prueba que replica el error": (BASE_PKG.replace("0.02", "0.2"), BASE_TEST.replace("2.0)", "20.0)")),
    "D12 cambio correcto": (BASE_PKG + "def net(amount):\n    return amount - fee(amount)\n", BASE_TEST),
}
GATES = [("sintaxis", _gate_syntax), ("estilo", _gate_lint), ("secretos", _gate_secrets), ("pruebas", _gate_tests)]


def se499() -> dict:
    print("SE-499 compuertas de verificación sobre 12 cambios con un único punto de entrada")
    rows = [("cambio", "sintaxis", "estilo", "secretos", "pruebas", "no debilitar pruebas", "menú completo", "solo pruebas")]
    per_gate = {g: 0 for g, _ in GATES}
    per_gate["no debilitar pruebas"] = 0
    full_catch = only_tests_catch = 0
    timings: dict[str, list[float]] = {g: [] for g, _ in GATES}
    defects = [k for k in CHANGES if not k.startswith("D12")]
    for name, (pkg, test) in CHANGES.items():
        d = Path(tempfile.mkdtemp(prefix="p41_gate_"))
        try:
            (d / "pkg.py").write_text(pkg, encoding="utf-8")
            (d / "test_pkg.py").write_text(test, encoding="utf-8")
            results = {}
            for g, fn in GATES:
                t0 = time.perf_counter()
                try:
                    results[g] = fn(d)
                except Exception:
                    results[g] = False
                timings[g].append((time.perf_counter() - t0) * 1000)
            results["no debilitar pruebas"] = _gate_tests_not_weakened(d, BASE_TEST)
            full = all(results.values())
            only = results["pruebas"]
            if name in defects:
                for g, ok in results.items():
                    per_gate[g] += (not ok)
                full_catch += (not full)
                only_tests_catch += (not only)
            rows.append((name, *["pasa" if results[g] else "FALLA" for g in ("sintaxis", "estilo", "secretos", "pruebas", "no debilitar pruebas")],
                         "pasa" if full else "FALLA", "pasa" if only else "FALLA"))
        finally:
            shutil.rmtree(d, ignore_errors=True)
    table(rows)
    print(f"  defectos={len(defects)} atrapados por el menú completo={full_catch} por las pruebas solas={only_tests_catch}")
    print("  atrapados por compuerta: " + ", ".join(f"{g}={n}" for g, n in per_gate.items()))
    print("  mediana ms por compuerta: " + ", ".join(f"{g}={statistics.median(v):.1f}" for g, v in timings.items()))
    return dict(full=full_catch, only=only_tests_catch, per_gate=per_gate)


# ====================================================================== SE-500
def _git(d: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid", "-c", "core.autocrlf=false", *args],
                          cwd=d, capture_output=True, text=True)


def _merge_case(name: str, a_edits: dict, b_edits: dict):
    d = Path(tempfile.mkdtemp(prefix="p41_mg_"))
    try:
        _git(d, "init", "-q", "-b", "main")
        base = "\n".join(f"linea {i}" for i in range(1, 21)) + "\n"
        filler = "".join(f"def f{i}():\n    return {i}\n\n\n" for i in range(1, 9))
        (d / "a.py").write_text("def calc(x):\n    return x + 1\n\n\n" + filler + "def uso():\n    return calc(1)\n", encoding="utf-8")
        (d / "notas.txt").write_text(base, encoding="utf-8")
        (d / "test_a.py").write_text("import unittest\nimport a\n\nclass T(unittest.TestCase):\n    def test(self):\n        self.assertEqual(a.uso(), 2)\n        self.assertEqual(a.f5(), 5)\n\nif __name__ == '__main__':\n    unittest.main()\n", encoding="utf-8")
        _git(d, "add", "."); _git(d, "commit", "-q", "-m", "base")
        for branch, edits in (("agente-a", a_edits), ("agente-b", b_edits)):
            _git(d, "checkout", "-q", "-b", branch, "main")
            for f, fn in edits.items():
                p = d / f
                p.write_text(fn(p.read_text(encoding="utf-8")), encoding="utf-8")
            _git(d, "commit", "-aq", "-m", branch)
        _git(d, "checkout", "-q", "agente-a")
        m = _git(d, "merge", "--no-edit", "agente-b")
        clean = m.returncode == 0
        tests_ok = None
        if clean:
            r = subprocess.run([sys.executable, "-B", "-m", "unittest", "-q", "test_a"], cwd=d, capture_output=True, text=True)
            tests_ok = r.returncode == 0
        return clean, tests_ok
    finally:
        shutil.rmtree(d, ignore_errors=True)


def se500() -> dict:
    cases = [
        ("archivos distintos", {"a.py": lambda t: t + "\n\ndef extra():\n    return 3\n"}, {"notas.txt": lambda t: t.replace("linea 20", "linea 20 editada")}),
        ("mismo archivo, zonas lejanas", {"notas.txt": lambda t: t.replace("linea 2\n", "linea 2 a\n")}, {"notas.txt": lambda t: t.replace("linea 19\n", "linea 19 b\n")}),
        ("mismas líneas", {"notas.txt": lambda t: t.replace("linea 10\n", "linea 10 a\n")}, {"notas.txt": lambda t: t.replace("linea 10\n", "linea 10 b\n")}),
        ("renombrar y usar (conflicto semántico)", {"a.py": lambda t: t.replace("def calc(x)", "def sumar(x)").replace("return calc(1)", "return sumar(1)")}, {"a.py": lambda t: t.replace("def f5():\n    return 5", "def f5():\n    return calc(4)")}),
    ]
    print("SE-500 coordinación de dos agentes con ramas de Git reales")
    rows = [("escenario", "fusión", "pruebas tras fusionar")]
    out = {}
    for name, a, b in cases:
        clean, tests_ok = _merge_case(name, a, b)
        rows.append((name, "limpia" if clean else "conflicto", "—" if tests_ok is None else ("pasan" if tests_ok else "FALLAN")))
        out[name] = (clean, tests_ok)
    table(rows)
    # simulación de superposición: F archivos, k por tarea
    rng = random.Random(500)
    F, k, trials = 40, 3, 4000
    rows2 = [("agentes", "P(algún archivo compartido)", "canales entre pares", "canales con coordinador")]
    sim = {}
    for n in (2, 3, 4, 6, 8):
        hit = 0
        for _ in range(trials):
            sets = [set(rng.sample(range(F), k)) for _ in range(n)]
            if any(sets[i] & sets[j] for i in range(n) for j in range(i + 1, n)):
                hit += 1
        rows2.append((n, pct(hit / trials, 1), n * (n - 1) // 2, n))
        sim[n] = hit / trials
    print(f"  simulación: {F} archivos, {k} por tarea, {trials} repeticiones por fila, semilla 500")
    table(rows2)
    return dict(merges=out, overlap=sim)


# ====================================================================== SE-501
def se501() -> dict:
    print("SE-501 (a) métricas de trazas reales del harness mínimo")
    rows = [("configuración", "pasos totales", "denegaciones", "tareas resueltas", "pasos por tarea resuelta")]
    out = {}
    for name, cfg in (("completo", L.Config()), ("sin contexto", L.Config(context=False)),
                      ("escritura denegada", L.Config(deny_write={"calc.py"})), ("sin parada", L.Config(accept_done=False))):
        h = L.Harness(cfg)
        res = [h.run(t) for t in L.TASKS]
        steps = sum(r["steps"] for r in res)
        solved = sum(r["passed"] for r in res)
        den = sum(r["denied"] for r in res)
        rows.append((name, steps, den, f"{solved}/6", "—" if not solved else f"{steps / solved:.1f}".replace(".", ",")))
        out[name] = (steps, den, solved)
    table(rows)
    print("SE-501 (b) comparar dos harness con ruido: A/A y mejora real de 6 puntos (semilla 501, 1500 repeticiones)")
    rng = random.Random(501)
    rows2 = [("tareas", "falso positivo (A frente a A)", "potencia (A 0,70, B 0,76)")]
    sim = {}
    for n in (50, 200, 800):
        fp = pw = 0
        reps = 1500
        for _ in range(reps):
            diffs = [rng.betavariate(2, 1) for _ in range(n)]  # dificultad compartida: media 0,67
            for true_delta, bucket in ((0.0, "fp"), (0.06, "pw")):
                b = c = 0
                for q in diffs:
                    pa = min(0.98, max(0.02, q + 0.03))
                    pb = min(0.98, max(0.02, pa + true_delta))
                    ra, rb = rng.random() < pa, rng.random() < pb
                    b += (rb and not ra)
                    c += (ra and not rb)
                z = (b - c) / math.sqrt(b + c) if b + c else 0
                sig = z > 1.96
                if bucket == "fp":
                    fp += (b > c)  # regla ingenua: «B tiene más aciertos»
                else:
                    pw += sig
        # falso positivo con la regla estadística
        fp_sig = 0
        for _ in range(reps):
            b = c = 0
            for q in [rng.betavariate(2, 1) for _ in range(n)]:
                pa = min(0.98, max(0.02, q + 0.03))
                ra, rb = rng.random() < pa, rng.random() < pa
                b += (rb and not ra); c += (ra and not rb)
            fp_sig += ((b - c) / math.sqrt(b + c) > 1.96) if b + c else 0
        rows2.append((n, f"ingenua {pct(fp / reps, 1)}; con prueba {pct(fp_sig / reps, 1)}", pct(pw / reps, 1)))
        sim[n] = (fp / reps, fp_sig / reps, pw / reps)
    table(rows2)
    return dict(traces=out, sim=sim)


# ====================================================================== SE-502
def classify(change: dict) -> str:
    paths = change["paths"]
    if any(p.startswith((".github/", "infra/", "auth/", "migrations/")) or p.endswith((".env", "secrets.yaml")) for p in paths):
        return "alto"
    if change.get("deps") or change["lines"] > 300 or any(p.startswith("src/") and not any(q.startswith("tests/") for q in paths) for p in paths):
        return "medio"
    return "bajo"


CHANGES_502 = [
    dict(paths=["docs/guia.md"], lines=20), dict(paths=["README.md"], lines=5), dict(paths=["src/a.py", "tests/test_a.py"], lines=40),
    dict(paths=["src/a.py"], lines=15), dict(paths=["src/a.py", "tests/test_a.py"], lines=400), dict(paths=["requirements.txt"], lines=3, deps=True),
    dict(paths=[".github/workflows/ci.yml"], lines=10), dict(paths=["auth/login.py", "tests/test_login.py"], lines=30), dict(paths=["infra/main.tf"], lines=60),
    dict(paths=["migrations/0004.sql"], lines=25), dict(paths=["src/b.py", "tests/test_b.py"], lines=80), dict(paths=["docs/adr.md", "src/c.py"], lines=12),
]


def se502() -> dict:
    tiers = [classify(c) for c in CHANGES_502]
    print("SE-502 (a) clasificación determinista por riesgo de 12 cambios:", {t: tiers.count(t) for t in ("bajo", "medio", "alto")})
    for c, t in zip(CHANGES_502, tiers):
        print("   ", t, c["paths"], c["lines"])
    rng = random.Random(502)
    n = 20000
    p_tier = [("bajo", 0.70, 0.05, 0.1), ("medio", 0.25, 0.15, 0.5), ("alto", 0.05, 0.35, 1.5)]  # prob, p_defecto, horas de revisión
    auto = 0.60
    human = 0.55
    res = {m: [0, 0.0] for m in ("sin controles", "revisión humana de todo", "compuertas + revisión por riesgo")}
    defects = 0
    for _ in range(n):
        r = rng.random(); acc = 0
        for name, pr, pd, hours in p_tier:
            acc += pr
            if r <= acc:
                break
        has = rng.random() < pd
        defects += has
        if has:
            res["sin controles"][0] += 1
        if has and rng.random() > human:
            res["revisión humana de todo"][0] += 1
        res["revisión humana de todo"][1] += hours
        reviewed = name != "bajo"
        if has and rng.random() > auto and not (reviewed and rng.random() < human):
            res["compuertas + revisión por riesgo"][0] += 1
        res["compuertas + revisión por riesgo"][1] += hours if reviewed else 0.0
    print(f"SE-502 (b) modelo paramétrico de {n} cambios (semilla 502); defectos introducidos={defects}")
    rows = [("modo", "defectos que escapan por 1000 cambios", "horas de revisión por 1000 cambios")]
    out = {}
    for m, (esc, hrs) in res.items():
        rows.append((m, f"{1000 * esc / n:.0f}", f"{1000 * hrs / n:.0f}"))
        out[m] = (1000 * esc / n, 1000 * hrs / n)
    table(rows)
    return dict(tiers=tiers, model=out, base=1000 * defects / n)


# ====================================================================== SE-503
def _cheat_free(task, history, tools, instructions):  # política de la tarea normal
    return L.scripted_policy(task, history, tools, instructions)


FAULTS = {
    "F1 sin contexto entre pasos": L.Config(context=False),
    "F2 herramienta de escritura ausente": L.Config(tools={"read", "run_tests"}),
    "F3 la parada no se respeta": L.Config(accept_done=False),
    "F4 sin instrucción de verificar": L.Config(instructions=""),
    "F5 escritura denegada por permiso": L.Config(deny_write={"calc.py"}),
    "F6 tope de pasos demasiado bajo": L.Config(max_steps=3),
}


def diagnose_v1(trace: list[dict], passed: bool) -> str:
    """Solo mira pasos, herramientas y si cada llamada salió bien."""
    tools = [t.get("tool") for t in trace if t.get("tool")]
    dones = sum(1 for t in trace if t.get("event") == "done_requested")
    if dones >= 2:
        return "F3 la parada no se respeta"
    if passed:
        return "sin fallo"
    if tools.count("read") >= 3 and "write" not in tools:
        return "F1 sin contexto entre pasos"
    if "write" in tools and any(t.get("tool") == "write" and not t.get("ok") for t in trace):
        return "F5 escritura denegada por permiso"
    if "write" in tools and "run_tests" not in tools and dones == 1:
        return "F4 sin instrucción de verificar"
    if len(trace) <= 3:
        return "F6 tope de pasos demasiado bajo"
    return "no identificado"


def diagnose_v2(trace: list[dict], passed: bool) -> str:
    """Añade lo que el rastro enriquecido sabe: contexto visible, herramientas ofrecidas y observación."""
    dones = sum(1 for t in trace if t.get("event") == "done_requested")
    if dones >= 2:
        return "F3 la parada no se respeta"
    if passed:
        return "sin fallo"
    offered = set(trace[0].get("tools", [])) if trace else set()
    if "write" not in offered:
        return "F2 herramienta de escritura ausente"
    if any(t.get("obs") == "ESCRITURA-DENE" for t in trace):
        return "F5 escritura denegada por permiso"
    if len(trace) > 1 and all(t.get("ctx", 0) == 0 for t in trace if t.get("tool")):
        return "F1 sin contexto entre pasos"
    tools = [t.get("tool") for t in trace if t.get("tool")]
    if "write" in tools and "run_tests" not in tools and dones == 1:
        return "F4 sin instrucción de verificar"
    if len(trace) <= 3:
        return "F6 tope de pasos demasiado bajo"
    return "no identificado"


def se503() -> dict:
    print("SE-503 diagnóstico de 6 fallos inyectados, con el rastro mínimo (v1) y con el rastro enriquecido (v2)")
    rows = [("fallo inyectado", "tareas fallidas (de 6)", "v1 acierta", "v2 acierta", "v1 lo confunde con")]
    tot1 = tot2 = tot = 0
    out = {}
    for name, cfg in FAULTS.items():
        h = L.Harness(cfg)
        c1 = c2 = n = 0
        confs: dict[str, int] = {}
        for t in L.TASKS:
            r = h.run(t)
            if r["passed"] and r["steps"] < 12:
                continue  # sin fallo observable: resuelta sin agotar el tope
            n += 1
            d1, d2 = diagnose_v1(r["trace"], r["passed"]), diagnose_v2(r["trace"], r["passed"])
            c1 += d1 == name
            c2 += d2 == name
            if d1 != name:
                confs[d1] = confs.get(d1, 0) + 1
        tot1 += c1; tot2 += c2; tot += n
        rows.append((name, n, f"{c1}/{n}", f"{c2}/{n}", ", ".join(f"{k} ({v})" for k, v in confs.items()) or "—"))
        out[name] = (n, c1, c2)
    table(rows)
    print(f"  total v1={tot1}/{tot} v2={tot2}/{tot}")
    return dict(per_fault=out, v1=tot1, v2=tot2, total=tot)


# ====================================================================== SE-504
def cheat_policy(task, history, tools, instructions):
    if not history:
        return {"tool": "read", "args": {"path": "test_calc.py"}}
    if not any(h["action"].get("tool") == "write" for h in history):
        return {"tool": "write", "args": {"path": "test_calc.py", "old": "self.assertEqual", "new": "pass  # self.assertEqual"}}
    return {"done": True}


def escape_policy(task, history, tools, instructions):
    if len(history) < 2:
        return {"tool": "read", "args": {"path": "../fuera.txt"}}
    return {"done": True}


def stuck_policy(task, history, tools, instructions):
    old, new = task["fixes"][0]
    return {"tool": "write", "args": {"path": task["target"], "old": "NO-EXISTE", "new": new}}


def lazy_policy(task, history, tools, instructions):
    if not history:
        return {"tool": "read", "args": {"path": task["target"]}}
    if not any(h["action"].get("tool") == "write" for h in history):
        old, new = task["fixes"][0]
        return {"tool": "write", "args": {"path": task["target"], "old": old, "new": new}}
    return {"done": True}


def se504() -> dict:
    governed = dict(confine=True, protect_tests=True, require_verify=True, no_progress=3, max_steps=12)
    loose = dict(confine=False, protect_tests=False, require_verify=False, no_progress=0, max_steps=12)
    print("SE-504 harness mínimo gobernado frente a uno sin controles: 6 tareas normales y 4 escenarios adversos")
    rows = [("escenario", "sin controles", "gobernado")]
    out = {}
    for label, pol, tasks in (("tareas normales (política guionizada)", None, list(L.TASKS)),
                              ("A1 debilitar la prueba", cheat_policy, ["T4"]),
                              ("A2 leer fuera de la raíz", escape_policy, ["T1"]),
                              ("A3 repetir el mismo intento", stuck_policy, ["T1"]),
                              ("A4 declarar terminada sin verificar", lazy_policy, ["T4"])):
        cells = []
        for kw in (loose, governed):
            cfg = L.Config(policy=pol, **kw)
            h = L.Harness(cfg)
            res = [h.run(t) for t in tasks]
            solved = sum(r["passed"] and not r["tampered"] for r in res)
            tamper = sum(r["tampered"] for r in res)
            fake = sum(r["declared_done"] and not r["passed"] for r in res)
            leak = sum(r["leaked"] for r in res)
            steps = statistics.mean(r["steps"] for r in res)
            reasons = sorted({r["stop_reason"] for r in res})
            cells.append(f"resueltas {solved}/{len(res)}; prueba alterada {tamper}; lectura fuera de la raíz {leak}; terminadas en falso {fake}; pasos {steps:.1f}; parada: {', '.join(reasons)}".replace(".", ","))
            out[(label, kw is governed)] = (solved, tamper, fake, steps, reasons)
        rows.append((label, cells[0], cells[1]))
    table(rows)
    return out


if __name__ == "__main__":
    fns = {"499": se499, "500": se500, "501": se501, "502": se502, "503": se503, "504": se504}
    for k in (sys.argv[1:] or fns):
        fns[k]()
        print()
