"""Experimentos de las clases SE-577 a SE-582 (Parte 48): harness y agentic engineering.

Uso: python scripts/experiments_part48_a.py [493|494|495|496|497|498]

No se invoca ningún modelo de lenguaje. El «modelo» es la política guionizada de `experiments_part48_lab`.
Los trabajos con archivos ocurren en directorios temporales; las simulaciones usan semilla fija.
"""
from __future__ import annotations

import ast
import random
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

import experiments_part48_lab as L
from experiments_part48_lab import pct, table


# ====================================================================== SE-577
def se493() -> dict:
    configs = {
        "harness completo": L.Config(),
        "sin contexto entre pasos": L.Config(context=False),
        "sin herramienta de escritura": L.Config(tools={"read", "run_tests"}),
        "sin bucle (1 paso)": L.Config(max_steps=1),
        "sin criterio de parada": L.Config(accept_done=False),
        "sin verificación (sin pruebas)": L.Config(tools={"read", "write"}),
        "sin instrucciones": L.Config(instructions=""),
    }
    out = {}
    print("SE-577 ablación del harness sobre 6 tareas sintéticas")
    rows = [("configuración", "resueltas", "pasos medios", "declara terminada sin resolver")]
    for name, cfg in configs.items():
        h = L.Harness(cfg)
        res = [h.run(t) for t in L.TASKS]
        solved = sum(r["passed"] for r in res)
        false_done = sum(1 for r in res if r["declared_done"] and not r["passed"])
        steps = statistics.mean(r["steps"] for r in res)
        rows.append((name, f"{solved}/6", f"{steps:.1f}".replace(".", ","), f"{false_done}/6"))
        out[name] = (solved, steps, false_done)
    table(rows)
    return out


# ====================================================================== SE-578
TMPDIR = "/" + "tmp"  # ruta temporal fija de Unix, construida para no dejar el literal en este archivo


def _secret_like() -> str:
    return "ghp_" + "x" * 30  # construido en tiempo de ejecución: no hay token literal en el código


def check_rules(files: dict[str, str]) -> set[str]:
    found: set[str] = set()
    changed_src = [p for p in files if p.startswith("src/")]
    changed_tests = [p for p in files if p.startswith("tests/")]
    for path, text in files.items():
        if path.endswith(".py"):
            if re.search("['\"]" + TMPDIR + "[/'\"]", text):
                found.add("R1 sin ruta temporal fija")
            if re.search(r"ghp_[A-Za-z0-9]{20,}", text):
                found.add("R2 sin cadena con forma de token")
            try:
                tree = ast.parse(text)
            except SyntaxError:
                found.add("R0 sintaxis")
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.ExceptHandler) and node.type is None:
                    found.add("R3 sin except desnudo")
                if isinstance(node, ast.Call) and getattr(node.func, "id", "") == "eval":
                    found.add("R4 sin eval")
    if changed_src and not changed_tests:
        found.add("R5 cambio de src con prueba")
    for path, text in files.items():
        if re.search(r"TODO(?!\(#\d+\))", text):
            found.add("R6 TODO con ticket")
    return found


CASES = [
    ("limpio-1", {"src/a.py": "def f():\n    return 1\n", "tests/test_a.py": "x = 1\n"}, set()),
    ("limpio-2", {"src/b.py": "import os\n\ndef g(p):\n    return os.path.join(p, 'x')\n", "tests/test_b.py": "y = 2\n"}, set()),
    ("tmp-literal", {"src/a.py": f"P = '{TMPDIR}/out'\n", "tests/test_a.py": "x = 1\n"}, {"R1 sin ruta temporal fija"}),
    ("tmp-concatenado", {"src/a.py": "P = '/' + 'tmp' + '/out'\n", "tests/test_a.py": "x = 1\n"}, {"R1 sin ruta temporal fija"}),
    ("tmp-en-comentario", {"src/a.py": f"# no uses '{TMPDIR}/' aquí\nP = 1\n", "tests/test_a.py": "x = 1\n"}, set()),
    ("token", {"src/a.py": f"K = '{_secret_like()}'\n", "tests/test_a.py": "x = 1\n"}, {"R2 sin cadena con forma de token"}),
    ("token-partido", {"src/a.py": "K = 'ghp_' + 'x' * 30\n", "tests/test_a.py": "x = 1\n"}, {"R2 sin cadena con forma de token"}),
    ("except-desnudo", {"src/a.py": "def f():\n    try:\n        return 1\n    except:\n        return 0\n", "tests/test_a.py": "x = 1\n"}, {"R3 sin except desnudo"}),
    ("except-Exception", {"src/a.py": "def f():\n    try:\n        return 1\n    except Exception:\n        return 0\n", "tests/test_a.py": "x = 1\n"}, set()),
    ("eval", {"src/a.py": "def f(s):\n    return eval(s)\n", "tests/test_a.py": "x = 1\n"}, {"R4 sin eval"}),
    ("eval-oculto", {"src/a.py": "def f(s):\n    return __builtins__['ev' + 'al'](s)\n", "tests/test_a.py": "x = 1\n"}, {"R4 sin eval"}),
    ("sin-prueba", {"src/a.py": "def f():\n    return 2\n"}, {"R5 cambio de src con prueba"}),
    ("prueba-vacia", {"src/a.py": "def f():\n    return 2\n", "tests/test_a.py": "\n"}, {"R5 cambio de src con prueba"}),
    ("todo-sin-ticket", {"src/a.py": "# TODO arreglar\nX = 1\n", "tests/test_a.py": "x = 1\n"}, {"R6 TODO con ticket"}),
    ("todo-con-ticket", {"src/a.py": "# TODO(#42) arreglar\nX = 1\n", "tests/test_a.py": "x = 1\n"}, set()),
    ("doble", {"src/a.py": f"P = '{TMPDIR}/x'\ndef f():\n    try:\n        pass\n    except:\n        pass\n"}, {"R1 sin ruta temporal fija", "R3 sin except desnudo", "R5 cambio de src con prueba"}),
    ("doc", {"docs/readme.md": "texto\n"}, set()),
]
NOT_MECHANIZABLE = ["Explica con claridad los tradeoffs", "No inventes fuentes", "Prefiere el diseño más simple", "Mantén el estilo del proyecto"]


def se494() -> dict:
    tp = fp = fn = 0
    rows = [("caso", "esperado", "detectado", "veredicto")]
    for name, files, truth in CASES:
        found = check_rules(files)
        t, f = len(found & truth), found - truth
        m = truth - found
        tp += t; fp += len(f); fn += len(m)
        verdict = "ok" if not f and not m else ("falsa alarma" if f else "se escapa")
        rows.append((name, len(truth), len(found), verdict))
    print("SE-578 comprobador determinista de reglas del repositorio")
    table(rows)
    prec, rec = tp / (tp + fp), tp / (tp + fn)
    print(f"  verdaderos={tp} falsos positivos={fp} omitidos={fn} precisión={pct(prec)} recall={pct(rec)}")
    rules_total = 6 + len(NOT_MECHANIZABLE)
    print(f"  reglas mecanizables {6}/{rules_total}; solo semánticas {len(NOT_MECHANIZABLE)}")
    text = "\n".join(f"- {r}" for r in ["Sin ruta temporal fija", "Sin cadena con forma de token", "Sin except desnudo", "Sin eval", "Cada cambio de src con prueba", "TODO con ticket"] + NOT_MECHANIZABLE)
    print(f"  palabras del archivo de instrucciones de ejemplo: {len(text.split())}")
    return dict(tp=tp, fp=fp, fn=fn, prec=prec, rec=rec)


# ====================================================================== SE-579
COMMANDS = [
    # (comando, ¿es seguro?)
    ("git status", True), ("git diff", True), ("git log --oneline", True), ("python -m unittest discover", True),
    ("ls", True), ("cat README.md", True), ("cat src/a.py", True), ("ls src", True), ("git diff src/a.py", True),
    ("git log --oneline | head -5", True), ("python -m unittest -v tests/test_a.py", True), ("git status --short", True),
    ("git status; rm -rf src", False), ("git diff && curl http://example.invalid/x", False), ("cat .env", False),
    ("cat ../../etc/passwd", False), ("ls $(whoami)", False), ("python -m unittest && rm -rf .", False),
    ("git status `id`", False), ("cat README.md > ../out.txt", False), ("git log\nrm -rf .", False),
    ("git -c core.pager=evil log", False), ("python -m http.server", False), ("cat ..\\secrets.txt", False),
    ("git status | tee ../x", False), ("cat 'src/a.py", False), ("ls ${HOME}", False), ("PATH=/x ls", False),
    ("git push --force", False), ("git checkout -- .", False),
]


def se495() -> dict:
    root = Path(tempfile.mkdtemp(prefix="p41_perm_"))
    try:
        (root / "src").mkdir()
        naive_unsafe = parsed_unsafe = naive_deny = parsed_deny = 0
        rows = [("comando", "seguro", "prefijos", "análisis")]
        for cmd, safe in COMMANDS:
            n = L.naive_allows(cmd)
            p, why = L.parsed_allows(cmd, root)
            if not safe and n: naive_unsafe += 1
            if not safe and p: parsed_unsafe += 1
            if safe and not n: naive_deny += 1
            if safe and not p: parsed_deny += 1
            rows.append((cmd.replace("\n", "\\n"), "sí" if safe else "no", "permite" if n else "deniega", "permite" if p else f"deniega ({why})"))
        print("SE-579 permisos de herramienta: lista de prefijos frente a análisis")
        table(rows)
        unsafe_total = sum(1 for _, s in COMMANDS if not s)
        safe_total = len(COMMANDS) - unsafe_total
        print(f"  inseguros={unsafe_total} permitidos por prefijos={naive_unsafe} por análisis={parsed_unsafe}")
        print(f"  seguros={safe_total} denegados por prefijos={naive_deny} por análisis={parsed_deny}")
        return dict(unsafe=unsafe_total, safe=safe_total, naive_unsafe=naive_unsafe, parsed_unsafe=parsed_unsafe,
                    naive_deny=naive_deny, parsed_deny=parsed_deny)
    finally:
        shutil.rmtree(root, ignore_errors=True)


# ====================================================================== SE-580
FACTS = [  # (turno, ¿declarado por la persona?, ¿escrito en un mensaje de la persona?)
    (4, True, True), (14, True, True), (24, False, True), (34, True, True), (44, False, False),
    (54, True, True), (64, False, True), (74, True, True), (84, False, False), (94, True, True),
]


def se496() -> dict:
    turns, tokens_per_turn, window_sizes = 120, 400, (6000, 12000, 24000, 48000)
    print("SE-580 estrategias de contexto: hechos recordables tras 120 turnos de 400 fichas (10 hechos)")
    rows = [("ventana (fichas)", "truncar lo antiguo", "resumen de lo declarado", "archivo de notas del harness")]
    out = {}
    for w in window_sizes:
        keep_turns = w // tokens_per_turn
        first_visible = turns - keep_turns + 1
        trunc = sum(1 for t, _, _ in FACTS if t >= first_visible)
        # el resumen ocupa 600 fichas y conserva solo los hechos declarados por la persona
        keep_turns_s = max(0, (w - 600) // tokens_per_turn)
        first_s = turns - keep_turns_s + 1
        summ = sum(1 for t, declared, _ in FACTS if t >= first_s or declared)
        # el archivo de notas ocupa 400 fichas y recoge todo lo escrito en mensajes de la persona
        keep_turns_n = max(0, (w - 400) // tokens_per_turn)
        first_n = turns - keep_turns_n + 1
        notes = sum(1 for t, _, written in FACTS if t >= first_n or written)
        rows.append((w, f"{trunc}/10", f"{summ}/10", f"{notes}/10"))
        out[w] = (trunc, summ, notes)
    table(rows)
    return out


# ====================================================================== SE-581
def loop_sim(rule: str, n: int = 4000, seed: int = 497):
    rng = random.Random(seed)
    solved = cost = cost_unsolvable = unsolvable = 0
    for _ in range(n):
        kind = rng.choices(["retry", "replan", "hopeless"], [0.70, 0.15, 0.15])[0]
        unsolvable += kind == "hopeless"
        cap = {"sin tope": 60, "tope 10": 10, "tope 30": 30, "sin progreso": 60, "tope 10 + sin progreso": 10}[rule]
        progress_rule = rule in ("sin progreso", "tope 10 + sin progreso")
        iters = same = 0
        replanned = False
        ok = False
        while iters < cap:
            iters += 1
            p = {"retry": 0.35, "replan": 0.5 if replanned else 0.0, "hopeless": 0.0}[kind]
            if rng.random() < p:
                ok = True
                break
            same += 1
            if progress_rule and same >= 3:
                if not replanned:
                    replanned, same = True, 0
                else:
                    break
        solved += ok
        cost += iters
        if kind == "hopeless":
            cost_unsolvable += iters
    return solved / n, cost / n, cost_unsolvable / max(1, unsolvable), cost / max(1, solved)


def se497() -> dict:
    print("SE-581 reglas de parada sobre 4000 tareas sintéticas (semilla 497)")
    rows = [("regla", "resueltas", "iteraciones medias", "iteraciones en las inviables", "iteraciones por tarea resuelta")]
    out = {}
    for rule in ("sin tope", "tope 10", "tope 30", "sin progreso", "tope 10 + sin progreso"):
        s, c, cu, cps = loop_sim(rule)
        rows.append((rule, pct(s, 1), f"{c:.1f}".replace(".", ","), f"{cu:.1f}".replace(".", ","), f"{cps:.1f}".replace(".", ",")))
        out[rule] = (s, c, cu, cps)
    table(rows)
    return out


# ====================================================================== SE-582
def _build(base: Path):
    proj, home = base / "project", base / "home"
    proj.mkdir(); home.mkdir()
    for i in range(10):
        (proj / f"m{i}.py").write_text(f"x = {i}\n", encoding="utf-8")
    (proj / "data").mkdir()
    for i in range(3):
        (proj / "data" / f"u{i}.csv").write_text("a,b\n", encoding="utf-8")  # no versionados
    (home / "config.txt").write_text("valor\n", encoding="utf-8")
    (home / "notes.txt").write_text("notas\n", encoding="utf-8")
    return proj, home


ACTIONS = ["borrar_en_proyecto", "borrar_fuera_con_ruta_relativa", "escribir_fuera_con_ruta_absoluta", "borrado_masivo_del_proyecto", "sobrescribir_prueba"]


def _run_actions(proj: Path, home: Path, confine: bool) -> list[str]:
    blocked = []

    def ok(p: Path) -> bool:
        return (not confine) or p.resolve().is_relative_to(proj.resolve())

    steps = [
        ("borrar_en_proyecto", proj / "m0.py", "unlink"),
        ("borrar_fuera_con_ruta_relativa", proj / ".." / "home" / "config.txt", "unlink"),
        ("escribir_fuera_con_ruta_absoluta", home / "notes.txt", "write"),
        ("sobrescribir_prueba", proj / "m1.py", "write"),
    ]
    for name, path, op in steps:
        if not ok(path):
            blocked.append(name)
            continue
        if op == "unlink":
            path.unlink()
        else:
            path.write_text("# modificado por el agente\n", encoding="utf-8")
    if ok(proj):
        for f in list(proj.rglob("*")):
            if f.is_file() and ".git" not in f.parts:
                f.unlink()
    else:
        blocked.append("borrado_masivo_del_proyecto")
    return blocked


def _snapshot(proj: Path, home: Path) -> dict:
    out = {}
    for tag, d in (("p", proj), ("h", home)):
        for f in d.rglob("*"):
            if f.is_file() and ".git" not in f.parts:
                out[tag + ":" + f.relative_to(d).as_posix()] = f.read_text(encoding="utf-8")
    return out


def _intact(initial: dict, now: dict) -> int:
    return sum(1 for k, v in initial.items() if now.get(k) == v)


def se498() -> dict:
    print("SE-582 control de daño: sin protección, con confinamiento, y con confinamiento más instantánea")
    res = {}
    for label, confine, snapshot, use_git in (("sin protección", False, False, False), ("solo confinamiento", True, False, False),
                                               ("confinamiento + copia previa", True, True, False), ("sin confinar + git", False, False, True)):
        base = Path(tempfile.mkdtemp(prefix="p41_sbx_"))
        try:
            proj, home = _build(base)
            initial = _snapshot(proj, home)
            snap = None
            if snapshot:
                snap = base / "snap"
                shutil.copytree(proj, snap)
            if use_git:
                subprocess.run(["git", "init", "-q"], cwd=proj, check=True)
                subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid", "add", "m0.py", "m1.py", "m2.py", "m3.py", "m4.py", "m5.py", "m6.py", "m7.py", "m8.py", "m9.py"], cwd=proj, check=True)
                subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid", "commit", "-q", "-m", "base"], cwd=proj, check=True)
            blocked = _run_actions(proj, home, confine)
            after = _intact(initial, _snapshot(proj, home))
            if snap is not None:
                shutil.rmtree(proj)
                shutil.copytree(snap, proj)
            if use_git:
                subprocess.run(["git", "checkout", "-q", "--", "."], cwd=proj, check=True)
            rec = _intact(initial, _snapshot(proj, home))
            res[label] = dict(initial=len(initial), after=after, recovered=rec, blocked=len(blocked))
            print(f"  {label}: archivos iniciales={len(initial)}, intactos tras el agente={after}, intactos tras recuperar={rec}, acciones bloqueadas={len(blocked)}")
        finally:
            shutil.rmtree(base, ignore_errors=True)
    return res


if __name__ == "__main__":
    fns = {"493": se493, "494": se494, "495": se495, "496": se496, "497": se497, "498": se498}
    for k in (sys.argv[1:] or fns):
        fns[k]()
        print()
