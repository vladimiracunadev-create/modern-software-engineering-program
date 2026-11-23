"""Experimentos de las clases SE-547 a SE-552 (Parte 45): metodologías de desarrollo.

Uso: python scripts/experiments_part45_b.py [487|488|489|490|491|492]

No se invoca ningún modelo de lenguaje. Contratos con procesos reales (`python -O`), un generador y un
comprobador de deriva sobre una especificación, simulaciones con semilla fija de evaluaciones
probabilísticas, un historial de Git real creado en un directorio temporal y una comparación de cinco
metodologías sobre el mismo cambio.
"""
from __future__ import annotations

import ast
import hashlib
import inspect
import json
import random
import re
import statistics
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

import experiments_part45_a as A
import experiments_part45_lab as L


def table(rows):
    for r in rows:
        print("  " + " | ".join(str(c) for c in r))


def pct(x, d=1):
    return f"{100 * x:.{d}f} %".replace(".", ",")


# ====================================================================== SE-547
SNIPPET = """
def reminder_hours(due, now):
    assert due > now, "precondición: la entrega no ha vencido"
    return due - now

try:
    print("resultado", reminder_hours(10, 20))
except AssertionError as error:
    print("contrato violado:", error)
"""


def consumer(response):
    """Cliente de Avisos: lee id, student, due y submitted y devuelve los avisos de la hora 76."""
    items = response["items"]
    deliveries = [{"id": i["id"], "student": i["student"], "course": "c1", "due": i["due"], "submitted": i["submitted"]} for i in items]
    return L.load(L.SOURCE)(deliveries, 76, frozenset(), set())


BASE_RESPONSE = {"items": [{"id": "a", "student": "e1", "due": 100, "submitted": False},
                           {"id": "b", "student": "e2", "due": 100, "submitted": True}]}
EXPECTED = consumer(BASE_RESPONSE)


def change(response, fn):
    new = json.loads(json.dumps(response))
    fn(new)
    return new


def rename_due(r):
    for i in r["items"]:
        i["due_at"] = i.pop("due")


def due_to_text(r):
    for i in r["items"]:
        i["due"] = f"2026-11-{i['due'] // 24:02d}T00:00:00Z"


def submitted_text(r):
    for i in r["items"]:
        i["submitted"] = "yes" if i["submitted"] else "no"


def wrap_data(r):
    r["data"] = r.pop("items")


CHANGES = [
    ("C01 añadir un campo opcional priority", lambda r: [i.update(priority=1) for i in r["items"]], False),
    ("C02 renombrar due por due_at", rename_due, True),
    ("C03 due pasa de horas a texto ISO", due_to_text, True),
    ("C04 eliminar student", lambda r: [i.pop("student") for i in r["items"]], True),
    ("C05 submitted pasa a texto «yes»/«no»", submitted_text, True),
    ("C06 añadir el campo course", lambda r: [i.update(course="c1") for i in r["items"]], False),
    ("C07 reordenar los campos", lambda r: r.update(items=[dict(reversed(list(i.items()))) for i in r["items"]]), False),
    ("C08 due pasa de entero a decimal", lambda r: [i.update(due=float(i["due"])) for i in r["items"]], False),
    ("C09 id pasa de texto a entero", lambda r: [i.update(id=ord(i["id"])) for i in r["items"]], True),
    ("C10 añadir el campo status con un valor nuevo", lambda r: [i.update(status="archivada") for i in r["items"]], False),
    ("C11 eliminar submitted", lambda r: [i.pop("submitted") for i in r["items"]], True),
    ("C12 envolver la lista en data", wrap_data, True),
]
CONSUMER_FIELDS = {"id": str, "student": str, "due": (int, float), "submitted": bool}


def ground_truth_breaks(response):
    try:
        return consumer(response) != EXPECTED
    except Exception:  # noqa: BLE001
        return True


def contract_detects(response):
    items = response.get("items")
    if not isinstance(items, list):
        return True
    for i in items:
        for name, kind in CONSUMER_FIELDS.items():
            if name not in i or not isinstance(i[name], kind):
                return True
    return False


def schema_diff_detects(response):
    if set(response) != set(BASE_RESPONSE):
        return True
    for new, old in zip(response["items"], BASE_RESPONSE["items"]):
        if set(new) != set(old):
            return True
        if any(type(new[k]) is not type(old[k]) for k in old):
            return True
    return False


def snapshot_detects(response):
    return response != BASE_RESPONSE


def e487():
    print("SE-547 — contratos: aserciones en tiempo de ejecución y contratos de consumidor")
    for flag in ([], ["-O"]):
        out = subprocess.run([sys.executable, *flag, "-c", SNIPPET], capture_output=True, text=True, check=True, encoding="utf-8", env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"}).stdout.strip()
        print(f"  python {' '.join(flag) or '(normal)'}: {out}")
    rows = [["Cambio del proveedor", "Rompe al cliente", "Instantánea", "Diferencia de esquema", "Contrato del consumidor"]]
    tally = {"snap": [0, 0], "diff": [0, 0], "contract": [0, 0]}
    breaking = 0
    for label, fn, expected_break in CHANGES:
        new = change(BASE_RESPONSE, fn)
        truth = ground_truth_breaks(new)
        assert truth == expected_break, (label, truth)
        breaking += truth
        s, d, c = snapshot_detects(new), schema_diff_detects(new), contract_detects(new)
        for key, flag in (("snap", s), ("diff", d), ("contract", c)):
            tally[key][0] += flag and truth
            tally[key][1] += flag and not truth
        rows.append([label, "sí" if truth else "no", "alerta" if s else "—", "alerta" if d else "—", "alerta" if c else "—"])
    table(rows)
    print(f"  cambios que rompen al cliente: {breaking} de {len(CHANGES)}")
    for key, name in (("snap", "instantánea"), ("diff", "diferencia de esquema"), ("contract", "contrato del consumidor")):
        print(f"  {name}: detecta {tally[key][0]} de {breaking}, falsas alarmas {tally[key][1]} de {len(CHANGES) - breaking}")


# ====================================================================== SE-548
SPEC = {
    "rules": {
        "RF-01": "avisos a 72, 24 y 1 horas",
        "RF-02": "no avisar a quien ya entregó",
        "RF-03": "tras una caída, solo el más urgente",
        "RF-04": "no avisar tras el vencimiento",
        "RF-05": "un curso silenciado conserva el aviso de 1 hora",
    },
    "offsets": [72, 24, 1],
}

TEMPLATE = '''# GENERADO desde spec.json (sha {sha}); no editar a mano
OFFSETS = {offsets}

def due_reminders(deliveries, now, silenced, sent):  # RF-01 RF-02 RF-03 RF-04 RF-05
    out = []
    for d in deliveries:
        if d["submitted"]:
            continue
        remaining = d["due"] - now
        if remaining <= 0:
            continue
        done = [o for (i, o) in sent if i == d["id"]]
        pending = [o for o in OFFSETS if remaining <= o and not any(s <= o for s in done)]
        if not pending:
            continue
        offset = min(pending)
        if (d["student"], d["course"]) in silenced and offset != {last}:
            continue
        out.append((d["id"], offset))
    return out
'''


def generate(spec):
    sha = hashlib.sha256(json.dumps(spec, sort_keys=True).encode()).hexdigest()[:12]
    offsets = tuple(spec["offsets"])
    return TEMPLATE.format(sha=sha, offsets=offsets, last=min(offsets))


def drift_check(spec_text, code_text, tests_text, changed_files):
    """Cinco comprobaciones mecánicas de deriva entre especificación, código y pruebas."""
    findings = []
    spec = json.loads(spec_text)
    rules = set(spec["rules"])
    code_rules = set(re.findall(r"RF-\d\d", code_text))
    test_rules = set(re.findall(r"@covers (RF-\d\d)", tests_text))
    if rules - code_rules:
        findings.append(f"regla sin código: {sorted(rules - code_rules)}")
    if code_rules - rules:
        findings.append(f"código cita regla inexistente: {sorted(code_rules - rules)}")
    if rules - test_rules:
        findings.append(f"regla sin prueba: {sorted(rules - test_rules)}")
    if test_rules - rules:
        findings.append(f"prueba cita regla inexistente: {sorted(test_rules - rules)}")
    tree = ast.parse(code_text)
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "OFFSETS":
            value = ast.literal_eval(node.value)
            if list(value) != spec["offsets"]:
                findings.append(f"OFFSETS del código {list(value)} difiere de la especificación {spec['offsets']}")
    if "code.py" in changed_files and "spec.json" not in changed_files:
        findings.append("el código cambió sin tocar la especificación")
    header = code_text.splitlines()[0]
    if header.startswith("# GENERADO") and generate(spec) != code_text:
        findings.append("el archivo generado no coincide con lo que genera la especificación")
    return findings


TESTS_OK = "\n".join(f"# @covers {r}" for r in sorted(SPEC["rules"]))


def e488():
    print("SE-548 — SDD: generador y comprobador de deriva sobre una especificación")
    spec_text = json.dumps(SPEC, sort_keys=True)
    code = generate(SPEC)
    generated = L.load(code)
    rng = random.Random(488)
    states = [A.L.random_state(rng) for _ in range(300)]
    ok = all(generated(*s) == L.reference(*s) for s in states)
    print("  el código generado coincide con el modelo de referencia en 300 estados:", ok)
    print("  comprobador sin deriva:", drift_check(spec_text, code, TESTS_OK, {"spec.json", "code.py"}))
    cases = [
        ("D1 una regla se elimina de la especificación y sigue en el código", lambda: (json.dumps({**SPEC, "rules": {k: v for k, v in SPEC["rules"].items() if k != "RF-04"}}, sort_keys=True), code, TESTS_OK, {"spec.json", "code.py"})),
        ("D2 una regla nueva sin código", lambda: (json.dumps({**SPEC, "rules": {**SPEC["rules"], "RF-06": "x"}}, sort_keys=True), code, TESTS_OK + "\n# @covers RF-06", {"spec.json", "code.py"})),
        ("D3 una regla nueva sin prueba", lambda: (json.dumps({**SPEC, "rules": {**SPEC["rules"], "RF-06": "x"}}, sort_keys=True), code + "\n# RF-06", TESTS_OK, {"spec.json", "code.py"})),
        ("D4 una prueba cita una regla que no existe", lambda: (spec_text, code, TESTS_OK + "\n# @covers RF-09", {"spec.json", "code.py"})),
        ("D5 el umbral del código cambia a mano (72, 24, 2)", lambda: (spec_text, code.replace("(72, 24, 1)", "(72, 24, 2)"), TESTS_OK, {"spec.json", "code.py"})),
        ("D6 el umbral cambia en la especificación y no en el código", lambda: (json.dumps({**SPEC, "offsets": [72, 24, 2]}, sort_keys=True), code, TESTS_OK, {"spec.json", "code.py"})),
        ("D7 se edita el código y no la especificación", lambda: (spec_text, code + "\n# retoque", TESTS_OK, {"code.py"})),
        ("D8 se edita a mano el archivo generado", lambda: (spec_text, code.replace("if remaining <= 0", "if remaining < 0"), TESTS_OK, {"spec.json", "code.py"})),
        ("D9 la condición del código cambia de <= a < (semántica)", lambda: (spec_text, code.replace("remaining <= o and", "remaining < o and").replace("# GENERADO", "# manual"), TESTS_OK, {"spec.json", "code.py"})),
        ("D10 el texto de una regla cambia de significado", lambda: (json.dumps({**SPEC, "rules": {**SPEC["rules"], "RF-02": "avisar también a quien ya entregó"}}, sort_keys=True), code, TESTS_OK, {"spec.json", "code.py"})),
    ]
    rows = [["Deriva inyectada", "Comprobador mecánico", "Qué ve"]]
    detected = 0
    for label, build in cases:
        findings = drift_check(*build())
        detected += bool(findings)
        rows.append([label, "detecta" if findings else "NO detecta", findings[0][:60] if findings else "—"])
    table(rows)
    print(f"  detectadas: {detected} de {len(cases)}")


# ====================================================================== SE-549
def gate_rates(n, true_good, true_bad, threshold, repeats, trials, seed):
    rng = random.Random(seed)

    def observed(p):
        total = n * repeats
        return sum(rng.random() < p for _ in range(total)) / total

    false_pass = sum(observed(true_bad) >= threshold for _ in range(trials)) / trials
    false_fail = sum(observed(true_good) < threshold for _ in range(trials)) / trials
    return false_pass, false_fail


def e489():
    print("SE-549 — EDD: tamaño del conjunto de evaluación y fiabilidad de la puerta de release")
    good, bad = 0.85, 0.80
    print(f"  precisión verdadera de la versión actual {good}; de la versión con regresión {bad}; umbral 0,825")
    rows = [["Casos", "Repeticiones", "Pasa una versión con regresión", "Rechaza una versión sana"]]
    for n in (20, 50, 100, 400, 1600):
        for repeats in (1, 3):
            fp, ff = gate_rates(n, good, bad, 0.825, repeats, 4000, 489 + n + repeats)
            rows.append([n, repeats, pct(fp), pct(ff)])
    table(rows)
    # regresión concentrada en un subconjunto difícil
    print("  regresión concentrada: 10 % de casos difíciles bajan de 0,60 a 0,20; el resto no cambia")
    rows = [["Conjunto", "Casos", "Pasa la regresión", "Rechaza la sana"]]
    rng = random.Random(4890)

    def mix(n, hard_share, p_hard, p_easy):
        hard = round(n * hard_share)
        return sum(rng.random() < p_hard for _ in range(hard)) + sum(rng.random() < p_easy for _ in range(n - hard))

    def rates(n, hard_share, thr, trials=4000):
        fp = sum(mix(n, hard_share, 0.20, 0.883) / n >= thr for _ in range(trials)) / trials
        ff = sum(mix(n, hard_share, 0.60, 0.883) / n < thr for _ in range(trials)) / trials
        return fp, ff

    fp, ff = rates(100, 0.10, 0.8)
    rows.append(["muestra al azar (10 % difíciles)", 100, pct(fp), pct(ff)])
    fp, ff = rates(100, 1.0, 0.4, 4000)
    rows.append(["solo difíciles (curado)", 100, pct(fp), pct(ff)])
    table(rows)
    # no determinismo: repetir la misma corrida con la misma versión
    rng = random.Random(489)
    scores = [sum(rng.random() < 0.85 for _ in range(100)) / 100 for _ in range(1000)]
    print(f"  misma versión, mismos 100 casos, 1000 corridas: media {statistics.mean(scores):.3f}, "
          f"desviación {statistics.pstdev(scores):.3f}, mín {min(scores):.2f}, máx {max(scores):.2f}".replace(".", ","))


# ====================================================================== SE-550
TASK_DOC = """# Tarea: silenciar un curso
## Alcance
Un estudiante puede silenciar un curso; el aviso de la última hora se conserva.
## Tareas
- [ ] prueba roja del silencio
- [ ] implementación mínima
## Evidencia
(pendiente)
## Siguiente paso
escribir la prueba roja
"""
CODE0 = "def silenced_offsets(silenced):\n    return []\n"
CODE1 = "def silenced_offsets(silenced):\n    return [1] if silenced else [72, 24, 1]\n"
TEST = "import unittest\nfrom reminders import silenced_offsets\n\nclass T(unittest.TestCase):\n    def test_silenced_keeps_last_hour(self):\n        self.assertEqual([1], silenced_offsets(True))\n    def test_normal_keeps_all(self):\n        self.assertEqual([72, 24, 1], silenced_offsets(False))\n\nif __name__ == '__main__':\n    unittest.main()\n"


def git(cwd, *args):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, check=True).stdout


def commit(repo, message, files):
    for name, content in files.items():
        path = Path(repo) / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
    git(repo, "add", "-A")
    git(repo, "-c", "user.name=Lab", "-c", "user.email=lab@example.invalid", "commit", "-q", "-m", message)


def tests_pass_at(repo, sha):
    with tempfile.TemporaryDirectory() as tmp:
        names = git(repo, "ls-tree", "-r", "--name-only", sha).split()
        for name in names:
            if name.endswith(".py"):
                (Path(tmp) / name).write_text(git(repo, "show", f"{sha}:{name}"), encoding="utf-8", newline="\n")
        if not (Path(tmp) / "test_reminders.py").exists():
            return None
        r = subprocess.run([sys.executable, "-m", "unittest", "-q"], cwd=tmp, capture_output=True, text=True)
        return r.returncode == 0


def check_odd(repo):
    shas = git(repo, "log", "--reverse", "--format=%H").split()
    findings, sizes = [], []
    doc_index = code_index = None
    statuses = []
    for k, sha in enumerate(shas):
        files = git(repo, "show", "--name-only", "--format=", sha).split()
        stat = git(repo, "show", "--numstat", "--format=", sha).strip().splitlines()
        lines = sum(int(a) + int(b) for a, b, _ in (s.split("\t") for s in stat) if a != "-")
        sizes.append(lines)
        if any(f.startswith("odd/tasks/") for f in files) and doc_index is None:
            doc_index = k
        if any(f == "reminders.py" for f in files) and code_index is None:
            code_index = k
        statuses.append(tests_pass_at(repo, sha))
    if doc_index is None or (code_index is not None and doc_index > code_index):
        findings.append("el documento de tarea no existe antes del primer código")
    if any(s > 400 for s in sizes):
        findings.append(f"commit de {max(sizes)} líneas (límite orientativo 400)")
    red_before_green = any(statuses[i] is False and statuses[i + 1] is True for i in range(len(statuses) - 1))
    if not red_before_green:
        findings.append("no hay un tramo rojo seguido de uno verde")
    return findings, sizes, statuses


def e490():
    print("SE-550 — ODD: un historial de Git real contra las reglas del flujo")
    with tempfile.TemporaryDirectory() as tmp:
        a = Path(tmp) / "a"
        a.mkdir()
        git(a, "init", "-q")
        commit(a, "docs: tarea", {"odd/tasks/silencio.md": TASK_DOC})
        commit(a, "test: rojo del silencio", {"test_reminders.py": TEST, "reminders.py": CODE0})
        commit(a, "feat: mínimo verde", {"reminders.py": CODE1})
        commit(a, "docs: evidencia", {"odd/tasks/silencio.md": TASK_DOC.replace("(pendiente)", "2 pruebas verdes").replace("escribir la prueba roja", "abrir la solicitud")})
        findings, sizes, statuses = check_odd(a)
        print("  historia A (con documento, rojo y verde):", findings or "sin hallazgos", sizes, statuses)
        b = Path(tmp) / "b"
        b.mkdir()
        git(b, "init", "-q")
        filler = "".join(f"def helper_{i}():\n    return {i}\n\n" for i in range(150))
        commit(b, "feat: todo junto", {"reminders.py": CODE1 + filler, "test_reminders.py": TEST})
        commit(b, "docs: tarea escrita después", {"odd/tasks/silencio.md": TASK_DOC})
        findings, sizes, statuses = check_odd(b)
        print("  historia B (código primero, un solo commit grande, documento tarde):", findings, sizes, statuses)
    print("  el comprobador mira orden, tamaño y estado de las pruebas; no puede saber si el documento dice la verdad")


# ====================================================================== SE-551
SILENCE_MUTANTS = {
    "S1 ignora el silencio": ('if (d["student"], d["course"]) in silenced and offset != 1:', 'if False:'),
    "S2 silencia también la última hora": ('in silenced and offset != 1', 'in silenced and True'),
    "S3 silencia a la persona en todos los cursos": ('(d["student"], d["course"]) in silenced', 'd["student"] in [s for s, c in silenced]'),
    "S4 silencia el curso para todas las personas": ('(d["student"], d["course"]) in silenced', 'd["course"] in [c for s, c in silenced]'),
    "S5 el silencio deja pasar el de 24 horas": ('offset != 1', 'offset != 24'),
    "S6 solo silencia el de 72 horas": ('offset != 1', 'offset == 1 or offset == 24'),
    "S7 silencia por curso o por persona": ('in silenced and offset != 1', 'in silenced or d["student"] in [s for s, c in silenced] and offset != 1'),
}


def silence_versions():
    out = {}
    for name, (old, new) in SILENCE_MUTANTS.items():
        assert old in L.SOURCE, name
        out[name] = L.load(L.SOURCE.replace(old, new, 1))
    return out


def feature_subset(names):
    return [s for s in A.parse_feature(A.FEATURE) if s["name"] in names]


def e491():
    print("SE-551 — el mismo cambio («silenciar un curso») con cinco metodologías")
    versions = silence_versions()
    original = L.load(L.SOURCE)
    bdd = feature_subset({"un curso silenciado conserva el aviso de la última hora", "un curso silenciado no recibe el de 24 horas", "el silencio de un curso no afecta a otro"})
    typical = [A.make_example(r, silenced=True) for r in (99, 76, 28)]
    boundary = [A.make_example(r, silenced=z, sent=s) for r in (73, 72, 25, 24, 2, 1, 0.5) for z in (True,) for s in ((), (72,))]
    suites = {
        "TDD (dos pruebas)": (lambda fn: L.oracle_tdd(fn, 0) and all(_ok(t, fn) for t in (L.t07_silencio_deja_pasar_la_ultima_hora, L.t08_silencio_es_por_curso)), inspect.getsource(L.t07_silencio_deja_pasar_la_ultima_hora) + inspect.getsource(L.t08_silencio_es_por_curso)),
        "BDD (tres escenarios)": (lambda fn: A.feature_oracle(fn, bdd), "\n".join(l for s in bdd for l in [s["name"]] + [f"{k} {t}" for k, t in s["steps"]])),
        "ATDD (tabla de ejemplos)": (lambda fn: A.example_oracle(fn, typical + boundary), "\n".join(f"{e[1]}|{sorted(e[2])}|{sorted(e[3])}" for e in typical + boundary)),
        "Contrato (400 estados)": (lambda fn: L.oracle_contract(fn), inspect.getsource(L.check_contract)),
        "SDD (modelo ejecutable)": (lambda fn: L.oracle_differential(fn), inspect.getsource(L.reference)),
    }
    rows = [["Metodología", "Líneas del artefacto", "Silencios mal hechos que mata", "Tiempo (ms)"]]
    killed_by = {}
    for label, (oracle, artifact) in suites.items():
        assert oracle(original), label
        killed = [n for n, fn in versions.items() if not oracle(fn)]
        killed_by[label] = set(killed)
        ms = L.timed(lambda o=oracle: o(original))
        rows.append([label, len([x for x in artifact.splitlines() if x.strip()]), f"{len(killed)} de {len(versions)}", f"{ms:.2f}"])
    table(rows)
    union = set().union(*killed_by.values())
    print(f"  unión de las cinco: {len(union)} de {len(versions)}")
    print("  propiedad de aislamiento (silenciar un par no cambia las demás entregas):",
          "pasa con el original" if aislamiento(original) else "FALLA con el original",
          "| mata:", [n[:2] for n, fn in versions.items() if not aislamiento(fn)])
    for label, ks in killed_by.items():
        print(f"    no mata {label}: {[n[:2] for n in versions if n not in ks]}")


def aislamiento(fn, n=400, seed=1):
    """Propiedad nueva: silenciar un par (persona, curso) no cambia los avisos de ninguna otra entrega."""
    rng = random.Random(seed)
    for _ in range(n):
        deliveries, now, silenced, sent = L.random_state(rng)
        antes = dict(fn(deliveries, now, silenced, sent))
        despues = dict(fn(deliveries, now, frozenset(set(silenced) | {("e1", "c1")}), sent))
        for d in deliveries:
            if (d["student"], d["course"]) != ("e1", "c1") and antes.get(d["id"]) != despues.get(d["id"]):
                return False
    return True


def _ok(test, fn):
    try:
        test(fn)
        return True
    except Exception:  # noqa: BLE001
        return False


# ====================================================================== SE-552
def e492():
    print("SE-552 — política metodológica de equipo evaluada sobre 300 cambios sintéticos")
    rng = random.Random(492)
    # tasas de detección ancladas en lo medido en SE-541 (mutantes no equivalentes que mata cada oráculo)
    matrix, _ = L.kill_matrix()
    real = [k for k in matrix if k not in ("M19", "M20")]
    rate = {label: sum(matrix[k][label] for k in real) / len(real) for label in L.ORACLES}
    print("  tasas de detección usadas (medidas en SE-541):", {k: round(v, 2) for k, v in rate.items()})
    # costo en horas por práctica: supuesto del autor, proporcional al tamaño del artefacto medido
    cost = {"nada": 0.0, "TDD": 1.5, "BDD+ATDD": 2.5, "contrato": 1.0, "SDD": 3.0}
    detect = {"nada": 0.0, "TDD": rate["Ocho pruebas TDD"], "BDD+ATDD": rate["Escenarios de aceptación"], "contrato": rate["Contrato con 400 estados"], "SDD": rate["Modelo de referencia"]}
    changes = []
    for i in range(300):
        risk = rng.choices(["bajo", "medio", "alto"], [0.5, 0.35, 0.15])[0]
        rules = rng.random() < 0.55  # el cambio tiene reglas deterministas comprobables
        ambiguous = rng.random() < 0.35
        defects = {"bajo": 0.25, "medio": 0.5, "alto": 0.9}[risk]
        impact = {"bajo": 1, "medio": 4, "alto": 20}[risk]
        changes.append((risk, rules, ambiguous, defects, impact))

    def outcome(policy):
        total_cost = escaped = 0.0
        for risk, rules, ambiguous, defects, impact in changes:
            practices = policy(risk, rules, ambiguous)
            miss = 1.0
            for p in practices:
                if p in ("TDD", "BDD+ATDD", "contrato", "SDD") and not rules:
                    continue  # sin reglas deterministas esas prácticas no producen un oráculo
                miss *= 1 - detect[p]
                total_cost += cost[p]
            if ambiguous and "BDD+ATDD" not in practices and "SDD" not in practices:
                miss = max(miss, 0.8)  # la ambigüedad sin conversación ni especificación sobrevive a las pruebas
            escaped += defects * miss * impact
        return total_cost, escaped

    policies = {
        "nada": lambda r, ru, am: [],
        "TDD en todo": lambda r, ru, am: ["TDD"],
        "todo en todo": lambda r, ru, am: ["TDD", "BDD+ATDD", "contrato", "SDD"],
        "por riesgo": lambda r, ru, am: (["TDD"] if r == "bajo" else ["TDD", "contrato"] if r == "medio" else ["TDD", "BDD+ATDD", "contrato", "SDD"]),
        "por riesgo y ambigüedad": lambda r, ru, am: (["TDD"] if r == "bajo" else ["TDD", "contrato"] if r == "medio" else ["TDD", "contrato", "SDD"]) + (["BDD+ATDD"] if am and r != "bajo" else []),
    }
    rows = [["Política", "Costo (horas)", "Impacto de defectos escapados", "Impacto evitado por hora invertida"]]
    base = outcome(policies["nada"])[1]
    for name, pol in policies.items():
        c, e = outcome(pol)
        rows.append([name, f"{c:.0f}", f"{e:.0f}", f"{(base - e) / c:.2f}" if c else "—"])
    table(rows)
    print("  Los costos, la distribución de riesgos y la fracción con reglas son supuestos; solo las tasas de detección vienen de SE-541.")


if __name__ == "__main__":
    which = sys.argv[1:] or ["487", "488", "489", "490", "491", "492"]
    for key in which:
        globals()[f"e{key}"]()
        print()
