"""Experimentos de las clases SE-343 a SE-348 (Parte 28): estilos arquitectónicos.

Uso: python scripts/experiments_part28_b.py [535|536|537|538|539|540]

No se invoca ningún modelo de lenguaje. Biblioteca estándar y el caso conductor *Avisos*. Los
parámetros de los modelos (tasas, costos, umbrales) los fija el autor y se declaran en la salida; los
tiempos de arranque de procesos se miden de verdad y varían de un equipo a otro.
"""
from __future__ import annotations

import ast
import hashlib
import heapq
import itertools
import math
import os
import random
import re
import statistics
import subprocess
import sys
import tempfile
import textwrap
import time
from pathlib import Path

import experiments_part28_lab as L
from experiments_part28_lab import fmt, pct, table


# ====================================================================== SE-343
def mmc_wait(lam, mu, c, n=30000, seed=44):
    rng = random.Random(seed)
    free = [0.0] * c
    heapq.heapify(free)
    t, waits = 0.0, []
    for _ in range(n):
        t += rng.expovariate(lam)
        start = max(t, heapq.heappop(free))
        waits.append(start - t)
        heapq.heappush(free, start + rng.expovariate(mu))
    return statistics.mean(waits), pct(waits, 0.9)


def erlang_c_wait(lam, mu, c):
    a = lam / mu
    rho = a / c
    if rho >= 1:
        return float("inf")
    s = sum(a ** k / math.factorial(k) for k in range(c))
    top = a ** c / (math.factorial(c) * (1 - rho))
    pw = top / (s + top)
    return pw / (c * mu - lam)


def base_dataset(n=1000, seed=44):
    rng = random.Random(seed)
    return [{"id": i, "student": f"s{rng.randrange(80)}", "due_hours": rng.randrange(0, 400), "submitted": rng.random() < 0.7,
             "age_hours": rng.uniform(0, 6)} for i in range(n)]


def check_product(rows, baseline):
    """Cinco comprobaciones de un producto de datos; devuelve el nombre de las que fallan."""
    fails = []
    expected = {"id": int, "student": str, "due_hours": int, "submitted": bool}
    ok_schema = bool(rows) and all(all(k in r and isinstance(r[k], t) and not (t is int and isinstance(r[k], bool)) for k, t in expected.items()) for r in rows if all(k in r for k in expected)) \
        and all(all(k in r for k in expected) for r in rows)
    if not ok_schema:
        fails.append("esquema")
    if sum(1 for r in rows if r.get("student") in (None, "")) / len(rows) > 0.01:
        fails.append("completitud")
    if len({r.get("id") for r in rows}) != len(rows):
        fails.append("unicidad")
    if max(r.get("age_hours", 0) for r in rows) > 24:
        fails.append("frescura")
    try:
        mean_due = statistics.mean(r["due_hours"] for r in rows)
        ratio = sum(1 for r in rows if r["submitted"] is True) / len(rows)
        if abs(mean_due - baseline["mean_due"]) / baseline["mean_due"] > 0.25 or abs(ratio - baseline["ratio"]) > 0.15:
            fails.append("distribución")
    except (KeyError, TypeError, statistics.StatisticsError):
        pass
    return fails


def e535():
    print("SE-343 — data mesh y propiedad de los datos")
    mu, lam_d, c = 1.0, 0.15, 4
    print(f"  equipo central de {c} personas, cada una atiende {fmt(mu, 1)} solicitud por semana; cada dominio pide {fmt(lam_d)} por semana")
    rows = [["Dominios", "Utilización", "Espera media simulada (semanas)", "Espera media analítica", "Espera p90 simulada"]]
    for d in (5, 10, 15, 20, 24):
        lam = d * lam_d
        mean, p90 = mmc_wait(lam, mu, c, n=60000)
        an = erlang_c_wait(lam, mu, c)
        rows.append([d, fmt(lam / (c * mu) * 100, 0) + " %", fmt(mean, 2), fmt(an, 2), fmt(p90, 2)])
    table(rows)
    print("  20 dominios; ¿cuántas personas hacen falta para que la espera media no pase de 0,5 semanas?")
    rows = [["Modelo", "Parámetro", "Personas necesarias", "Espera media simulada"]]
    for k in (0.0, 0.5, 1.0):
        for cc in range(2, 40):
            m, _ = mmc_wait(20 * lam_d, mu / (1 + k), cc, n=60000)
            if m <= 0.5:
                break
        rows.append(["Equipo central", f"penalización de contexto {fmt(k, 1)}", cc, fmt(m, 2)])
    for f in (0.5, 0.6, 0.65, 0.7):
        m, _ = mmc_wait(lam_d, f, 1, n=60000)
        rows.append(["Equipo de dominio (uno por dominio)", f"{fmt(f, 2)} persona por dominio", fmt(20 * f, 0) + " en total", fmt(m, 2)])
    table(rows)
    base = base_dataset()
    baseline = {"mean_due": statistics.mean(r["due_hours"] for r in base), "ratio": sum(r["submitted"] for r in base) / len(base)}
    print(f"  producto de datos con {len(base)} filas; línea base: media {fmt(baseline['mean_due'], 1)} horas, entregadas {fmt(baseline['ratio'] * 100, 1)} %; sin deriva falla: {check_product(base, baseline)}")

    def rename(rs):
        return [{("due" if k == "due_hours" else k): v for k, v in r.items()} for r in rs]

    def strs(rs):
        return [{**r, "due_hours": str(r["due_hours"])} for r in rs]

    def drop(rs):
        return [{k: v for k, v in r.items() if k != "submitted"} for r in rs]

    def nulls(rs):
        return [{**r, "student": None} if i % 8 == 0 else r for i, r in enumerate(rs)]

    def dups(rs):
        return [{**r, "id": (r["id"] // 2) * 2} for r in rs]

    def stale(rs):
        return [{**r, "age_hours": r["age_hours"] + 30} for r in rs]

    def minutes(rs):
        return [{**r, "due_hours": r["due_hours"] * 60} for r in rs]

    def inverted(rs):
        return [{**r, "submitted": not r["submitted"]} for r in rs]

    def seasonal(rs):  # cambio legítimo: fin de semestre, las fechas están más cerca
        return [{**r, "due_hours": r["due_hours"] // 2} for r in rs]

    cases = [("D1 columna renombrada", rename, True), ("D2 tipo cambiado a texto", strs, True), ("D3 columna eliminada", drop, True),
             ("D4 nulos en estudiante (12,5 %)", nulls, True), ("D5 identificadores duplicados", dups, True), ("D6 datos atrasados (30 h)", stale, True),
             ("D7 unidad cambiada a minutos", minutes, True), ("D8 significado invertido", inverted, True), ("L1 cambio legítimo de temporada", seasonal, False)]
    rows = [["Cambio", "Es un defecto", "Comprobaciones que fallan", "Detectado"]]
    for name, fn, is_bug in cases:
        f = check_product(fn(base), baseline)
        rows.append([name, "sí" if is_bug else "no", ", ".join(f) or "ninguna", "sí" if f else "no"])
    table(rows)
    det = sum(1 for _, fn, bug in cases if bug and check_product(fn(base), baseline))
    print(f"  defectos detectados: {det} de {sum(b for _, _, b in cases)}; falsas alarmas: {sum(1 for _, fn, bug in cases if not bug and check_product(fn(base), baseline))} de 1 cambio legítimo")
    only_schema = sum(1 for _, fn, bug in cases if bug and "esquema" in check_product(fn(base), baseline))
    print(f"  solo con la comprobación de esquema se detectan {only_schema} de 8")


# ====================================================================== SE-344
def h(*parts):
    return int.from_bytes(hashlib.blake2b("|".join(parts).encode(), digest_size=8).digest(), "big")


def rendezvous(tenant, cells):
    return max(cells, key=lambda c: h(tenant, c))


def e536():
    print("SE-344 — arquitectura celular y radio de impacto")
    tenants = [f"t{i}" for i in range(100000)]
    cells8 = [f"c{i}" for i in range(8)]
    cells9 = cells8 + ["c8"]
    mod_moved = sum(1 for t in tenants if h(t) % 8 != h(t) % 9)
    rv_moved = sum(1 for t in tenants if rendezvous(t, cells8) != rendezvous(t, cells9))
    print(f"  añadir una celda (de 8 a 9) con {len(tenants)} inquilinos: reubicados con módulo {mod_moved} ({fmt(100 * mod_moved / len(tenants), 1)} %), con hash por encuentro {rv_moved} ({fmt(100 * rv_moved / len(tenants), 1)} %); ideal 1/9 = 11,1 %")
    load = {c: 0 for c in cells8}
    for t in tenants:
        load[rendezvous(t, cells8)] += 1
    print(f"  reparto entre 8 celdas: mínimo {min(load.values())}, máximo {max(load.values())} (media {len(tenants) // 8})")

    ts = tenants[:1000]
    cell_of = {t: rendezvous(t, cells8) for t in ts}
    poison = ts[7]
    in_cell = sum(1 for t in ts if cell_of[t] == cell_of[poison])
    print(f"  un inquilino venenoso tumba su celda: afectados {in_cell} de {len(ts)} ({fmt(100 * in_cell / len(ts), 1)} %); flota compartida (supuesto: los reintentos recorren todos los trabajadores): {len(ts)} de {len(ts)} (100 %)")
    workers = [f"w{i}" for i in range(8)]

    def shard(t, k=2):
        return set(sorted(workers, key=lambda w: -h(t, w))[:k])

    shards = {t: shard(t) for t in ts}
    for npoison in (1, 2):
        poisons = ts[7:7 + npoison]
        dead = set().union(*(shards[p] for p in poisons))
        caidos = sum(1 for t in ts if shards[t] <= dead)
        degradados = sum(1 for t in ts if shards[t] & dead and not shards[t] <= dead)
        print(f"  fragmentación aleatoria (ocho trabajadores, dos por inquilino), {npoison} venenoso(s): caídos del todo {caidos} ({fmt(100 * caidos / len(ts), 1)} %), degradados {degradados} ({fmt(100 * degradados / len(ts), 1)} %)")
    print(f"  analítico con un venenoso: caídos 1/C(8,2) = {fmt(100 / 28, 1)} %; con algún trabajador caído {fmt(100 * (1 - math.comb(6, 2) / math.comb(8, 2)), 1)} %")

    rng = random.Random(44)
    loads = [[rng.lognormvariate(0, 1) for _ in ts] for _ in range(1000)]  # 1000 minutos, 1000 inquilinos
    total = [sum(m) for m in loads]
    cell_peaks = 0.0
    for c in cells8:
        idx = [i for i, t in enumerate(ts) if cell_of[t] == c]
        cell_peaks += pct([sum(m[i] for i in idx) for m in loads], 0.99)
    pooled = pct(total, 0.99)
    print(f"  capacidad para cubrir el p99 de la carga: flota compartida {fmt(pooled, 0)} unidades; ocho celdas (cada una a su p99) {fmt(cell_peaks, 0)} ({fmt(100 * (cell_peaks / pooled - 1), 1)} % más)")
    print(f"  disponibilidad de un inquilino: enrutador 99,99 % por celda 99,9 % = {fmt(0.9999 * 0.999 * 100, 3)} %; el enrutador es un punto de fallo compartido")


# ====================================================================== SE-345
BAD_APP = '''
import os
DB_URL = "postgres://usuario@host-fijo:5432/avisos"
SESSIONS = {}
CACHE = []

def log(msg):
    with open("avisos.log", "a") as f:
        f.write(msg)

def handle(req):
    SESSIONS[req["user"]] = req
    return os.environ.get("MODO", "prod")
'''
GOOD_APP = '''
import os, sys
DB_URL = os.environ["AVISOS_DB_URL"]
UMBRALES = tuple(int(x) for x in os.environ.get("AVISOS_UMBRALES", "72,24,1").split(","))

def log(msg):
    print(msg, file=sys.stdout, flush=True)

def handle(req, store):
    store.put(req["user"], req)
    return UMBRALES
'''


def lint_12factor(src):
    tree = ast.parse(src)
    found = {"URL fija": 0, "Estado en memoria del proceso": 0, "Registro en archivo local": 0, "Configuración desde el entorno": 0}
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and re.match(r"^[a-z]+://", node.value):
            found["URL fija"] += 1
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "open":
            mode = node.args[1].value if len(node.args) > 1 and isinstance(node.args[1], ast.Constant) else "r"
            if any(m in mode for m in "aw"):
                found["Registro en archivo local"] += 1
        if isinstance(node, ast.Attribute) and node.attr == "environ":
            found["Configuración desde el entorno"] += 1
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, (ast.Dict, ast.List, ast.Set)):
            found["Estado en memoria del proceso"] += 1
    return found


class Instance:
    def __init__(self):
        self.sessions, self.alive = {}, True


def sessions_run(mode, seed=44):
    rng = random.Random(seed)
    inst = [Instance() for _ in range(3)]
    shared = {}
    fail = total = 0
    sticky = {u: rng.randrange(3) for u in range(100)}
    logged = set()
    for i in range(1000):
        if i == 500:
            inst[1].alive = False
            inst[1].sessions.clear()
        u = rng.randrange(100)
        alive = [k for k, x in enumerate(inst) if x.alive]
        if mode == "afinidad":
            k = sticky[u] if inst[sticky[u]].alive else rng.choice(alive)
        else:
            k = rng.choice(alive)
        total += 1
        if u not in logged:
            logged.add(u)
            (shared if mode == "externo" else inst[k].sessions)[u] = True
            continue
        has = shared.get(u) if mode == "externo" else inst[k].sessions.get(u)
        fail += not has
    return fail, total


def e537():
    print("SE-345 — 12-factor y aplicaciones nativas de la nube")
    rows = [["Hallazgo", "App con defectos", "App corregida"]]
    a, b = lint_12factor(BAD_APP), lint_12factor(GOOD_APP)
    for k in a:
        rows.append([k, a[k], b[k]])
    table(rows)
    print("  (la app corregida usa os.environ[...] y os.environ.get(...): son dos accesos al entorno; el linter cuenta las apariciones del atributo)")
    for mode in ("memoria sin afinidad", "afinidad", "externo"):
        fail, total = sessions_run(mode)
        print(f"  sesiones {mode}: {fail} peticiones sin sesión de {total} (tres instancias, una cae en la petición 500, 100 usuarios)")
    # arranque
    def spawn(code):
        t = time.perf_counter()
        subprocess.run([sys.executable, "-c", code], check=True, capture_output=True)
        return (time.perf_counter() - t) * 1000

    t0 = [spawn("pass") for _ in range(10)]
    t1 = [spawn("import sqlite3,json,http.server,hashlib") for _ in range(10)]
    print(f"  arranque de un proceso Python: vacío mediana {fmt(L.median(t0), 0)} ms; con sqlite3, json, http.server y hashlib mediana {fmt(L.median(t1), 0)} ms")
    # drenado
    def run_jobs(drain, kill_at=40, total=100):
        done, requeued, lost = 0, 0, 0
        pending = list(range(total))
        inflight = None
        for step in range(total):
            if step == kill_at:
                if drain:
                    requeued = len(pending)  # termina el trabajo en curso y devuelve el resto a la cola
                    return done + 1, requeued, 0
                lost = 1 + len(pending) - 1  # corte inmediato: el trabajo en curso se pierde y el resto no se devuelve
                return done, 0, lost
            pending.pop(0)
            done += 1
        return done, requeued, lost

    print("  100 trabajos en una cola en memoria sin reentrega; la señal de parada llega al trabajo 40:")
    for drain in (False, True):
        d, r, l = run_jobs(drain)
        print(f"    {'drenaje ordenado' if drain else 'corte inmediato'}: completados {d}, devueltos a la cola {r}, perdidos {l}")
    # un artefacto, dos entornos
    with tempfile.TemporaryDirectory() as tmp:
        app = Path(tmp) / "app.py"
        app.write_text("import os,sys\nraw=os.environ.get('AVISOS_UMBRALES')\nif raw is None:\n    sys.exit('falta AVISOS_UMBRALES')\nprint(sorted(int(x) for x in raw.split(',')))\n", encoding="utf8")
        sig = hashlib.sha256(app.read_bytes()).hexdigest()[:12]
        for label, env in [("desarrollo", "48,12"), ("producción", "72,24,1"), ("sin configurar", None)]:
            e = {k: v for k, v in os.environ.items() if k != "AVISOS_UMBRALES"}
            if env:
                e["AVISOS_UMBRALES"] = env
            r = subprocess.run([sys.executable, str(app)], env=e, capture_output=True, text=True)
            print(f"    mismo artefacto (huella {sig}), entorno {label}: código {r.returncode}, salida «{(r.stdout or r.stderr).strip()}»")


# ====================================================================== SE-346
def legacy_due(d):
    rem = (d["due_min"] - d["now_min"]) / 60
    cat = d["category"]
    grace = 24 if cat == "extension" else 0
    if d["tz_shift"]:
        rem += 1
    for th in (1, 24, 72):
        if rem + grace <= th:
            return th
    return None


def new_due(d):
    rem = (d["due_min"] - d["now_min"]) // 60  # defecto sembrado: redondeo hacia abajo en minutos
    for th in (1, 24, 72):
        if rem <= th:
            return th
    return None


def gen_requests(n, seed=44):
    rng = random.Random(seed)
    out = []
    for _ in range(n):
        out.append({"due_min": rng.randrange(0, 400 * 60), "now_min": 0,
                    "category": "extension" if rng.random() < 0.02 else "normal", "tz_shift": rng.random() < 0.005})
    return out


def cause(d):
    if d["category"] == "extension":
        return "plazo de extensión"
    if d["tz_shift"]:
        return "cambio de hora"
    return "redondeo en el borde"


def e538():
    print("SE-346 — evolución y migración entre estilos")
    reqs = gen_requests(20000)
    diffs = [(d, legacy_due(d), new_due(d)) for d in reqs if legacy_due(d) != new_due(d)]
    print(f"  20000 peticiones sintéticas: divergencias entre el módulo heredado y el nuevo: {len(diffs)} ({fmt(100 * len(diffs) / 20000, 2)} %)")
    by = {}
    for d, a, b in diffs:
        by[cause(d)] = by.get(cause(d), 0) + 1
    for k, v in sorted(by.items(), key=lambda kv: -kv[1]):
        print(f"    {k}: {v}")
    print("  detección en modo sombra según la fracción del tráfico comparada (500 repeticiones por fracción, semilla 44):")
    rng = random.Random(44)
    causes = ["plazo de extensión", "cambio de hora", "redondeo en el borde"]
    rows = [["Fracción comparada", "Plazo de extensión", "Cambio de hora", "Redondeo en el borde"]]
    for frac in (0.01, 0.05, 0.25, 1.0):
        seen = {c: 0 for c in causes}
        for _ in range(500):
            sample = reqs if frac == 1.0 else rng.sample(reqs, int(len(reqs) * frac))
            got = set()
            for d in sample:
                if legacy_due(d) != new_due(d):
                    got.add(cause(d))
            for c in got:
                seen[c] += 1
        rows.append([f"{fmt(frac * 100, 0)} %"] + [f"{fmt(100 * seen[c] / 500, 0)} %" for c in causes])
    table(rows)
    print("  escalones de tráfico (1, 5, 25, 50, 100 %) con un defecto visible para el usuario en 0,4 % de las peticiones y 20000 peticiones por escalón:")
    rows = [["Escalón", "Usuarios afectados esperados", "Prob. de ver al menos 3 errores en el escalón"]]
    for frac in (0.01, 0.05, 0.25, 0.5, 1.0):
        n = int(20000 * frac)
        lam = n * 0.004
        p = 1 - sum(math.exp(-lam) * lam ** k / math.factorial(k) for k in range(3))
        rows.append([f"{fmt(frac * 100, 0)} %", fmt(lam, 1), fmt(p * 100, 1) + " %"])
    table(rows)
    # parallel change: sumas de usuarios afectados antes de detectar
    expected_big_bang = 20000 * 0.004
    expected_cumulative = sum(20000 * f * 0.004 for f in (0.01, 0.05))
    print(f"  usuarios afectados esperados antes de detener el cambio: de golpe {fmt(expected_big_bang, 0)}; si el escalón del 5 % lo detecta, tras los escalones de 1 % y 5 % {fmt(expected_cumulative, 1)}")


# ====================================================================== SE-347
SCENARIOS = [
    ("S1 latencia", "p99 ≤ 200 ms"), ("S2 disponibilidad", "≥ 99,9 %"), ("S3 radio de impacto", "≤ 15 % de inquilinos"),
    ("S4 coordinación de despliegue", "≤ 2 equipos coordinados"), ("S5 costo", "≤ 12 unidades"), ("S6 extensión", "canal nuevo sin tocar el núcleo"),
]
WEIGHT = {"H": 5, "M": 3, "L": 1}
IMPORTANCE = {  # importancia por escenario según el contexto (decisión de negocio, no medición)
    "con cliente dominante": ["H", "H", "H", "M", "M", "M"],
    "sin cliente dominante": ["H", "H", "L", "M", "M", "M"],
}


def sim_p99(hops, n=20000, seed=44):
    rng = random.Random(seed)
    return pct([sum(rng.lognormvariate(math.log(20), 0.6) for _ in range(hops)) for _ in range(n)], 0.99)


def candidates(teams):
    cands = {}
    cands["Monolito modular"] = dict(p99=sim_p99(1), avail=0.9995, radius=100.0, coord=max(0, teams - 1), cost=3, extension=False)
    cands["Microservicios (4)"] = dict(p99=sim_p99(4), avail=0.999 ** 4, radius=100.0, coord=0, cost=4 * 3 + 2 + 2, extension=True)
    cands["Celdas (8) con monolito modular"] = dict(p99=sim_p99(2), avail=0.9999 * 0.999, radius=12.5, coord=max(0, teams - 1), cost=8 * 2 + 2, extension=False)
    return cands


def utilities(c):
    return [
        min(1.0, 200 / c["p99"]),
        1.0 if c["avail"] >= 0.999 else max(0.0, 1 - (0.999 - c["avail"]) / 0.001),
        min(1.0, 15 / c["radius"]),
        1.0 if c["coord"] <= 2 else 2 / c["coord"],
        min(1.0, 12 / c["cost"]),
        1.0 if c["extension"] else 0.0,
    ]


def total(c, ctx):
    imp = IMPORTANCE[ctx]
    return sum(WEIGHT[w] * u for w, u in zip(imp, utilities(c))) / sum(WEIGHT[w] for w in imp)


def e539():
    print("SE-347 — taller: seleccionar un estilo con escenarios de calidad")
    for (n, m), a, b in zip(SCENARIOS, IMPORTANCE["con cliente dominante"], IMPORTANCE["sin cliente dominante"]):
        print(f"  {n}: medida {m}; importancia con cliente dominante {a}, sin cliente dominante {b}")
    for teams in (4, 12):
        cands = candidates(teams)
        print(f"  con {teams} equipos:")
        rows = [["Candidato", "p99 (ms)", "Disponibilidad", "Radio (%)", "Equipos a coordinar", "Costo", "Escenarios cumplidos", "Utilidad con cliente dominante", "Utilidad sin cliente dominante"]]
        for name, c in cands.items():
            full = sum(1 for v in utilities(c) if v >= 1.0)
            rows.append([name, fmt(c["p99"], 0), fmt(c["avail"] * 100, 3) + " %", fmt(c["radius"], 1), c["coord"], c["cost"], f"{full} de 6",
                         fmt(total(c, "con cliente dominante"), 3), fmt(total(c, "sin cliente dominante"), 3)])
        table(rows)
    for ctx in IMPORTANCE:
        print(f"  barrido del número de equipos, {ctx}: candidato con mayor utilidad")
        prev = None
        for t in range(2, 31):
            cands = candidates(t)
            best = max(cands, key=lambda k: total(cands[k], ctx))
            if best != prev:
                print(f"    desde {t} equipos: {best}")
                prev = best
        for name in candidates(4):
            vals = [total(candidates(t)[name], ctx) for t in (2, 4, 8, 12, 20, 30)]
            print(f"    {name}: utilidad con 2, 4, 8, 12, 20 y 30 equipos = {[fmt(v, 3) for v in vals]}")
    mono_vs_micro = None
    for t in range(2, 31):
        cs = candidates(t)
        if total(cs["Microservicios (4)"], "sin cliente dominante") > total(cs["Monolito modular"], "sin cliente dominante"):
            mono_vs_micro = t
            break
    print(f"  sin cliente dominante, los microservicios superan al monolito modular desde {mono_vs_micro} equipos (punto de sensibilidad)")
    print("  si la disponibilidad de la cadena de microservicios fuese 99,95 % (con degradación y reintentos) en vez de 99,601 %:")
    for ctx in IMPORTANCE:
        for t in (4, 12):
            cs = candidates(t)
            cs["Microservicios (4)"]["avail"] = 0.9995
            best = max(cs, key=lambda k: total(cs[k], ctx))
            print(f"    {ctx}, {t} equipos: gana {best} ({fmt(total(cs[best], ctx), 3)})")


# ====================================================================== SE-348
ADRS = {
    "ADR-A": """# ADR-001 — Monolito modular con extracción del módulo de avisos si p99 supera 200 ms
Estado: aceptada (2026-11-16)
## Contexto
Seis equipos, 80 solicitudes por segundo, una sola base de datos. El escenario S1 exige p99 ≤ 200 ms y S4 exige coordinar el despliegue entre a lo sumo 2 equipos.
## Decisión
Se mantiene un monolito modular con módulos que solo se comunican por interfaces públicas; una prueba de arquitectura lo comprueba en cada integración.
## Alternativas consideradas
1. Microservicios (4): descartada porque el costo estimado es 14 unidades frente a 3 y no hay equipos que lo justifiquen hoy.
2. Arquitectura celular: descartada porque el radio de impacto de 100 % es aceptable con un solo cliente.
## Consecuencias
Positivas: un solo despliegue, latencia de una llamada en proceso.
Negativas: con más de 3 equipos la coordinación de despliegue supera el umbral; un fallo del módulo de avisos detiene todo.
## Reversibilidad
Media: extraer un módulo cuesta unas 6 semanas-persona según la estimación del equipo.
## Disparador de revisión
Revisar si p99 > 200 ms durante 3 días seguidos o si hay más de 3 equipos.
## Evidencia
Mediciones de SE-340 y SE-347; prueba de arquitectura en CI.
""",
    "ADR-B": """# ADR-002 — Usar microservicios
Estado: aceptada
## Contexto
Queremos escalar y ser modernos.
## Decisión
Se adoptan microservicios porque son la mejor práctica.
## Consecuencias
Mejor escalabilidad y mantenibilidad.
""",
    "ADR-C": """# ADR-003 — Celdas para el cliente grande
Estado: propuesta
## Contexto
Un cliente representa 40 % del tráfico y sus fallos afectan a todos; el escenario S3 exige un radio ≤ 15 % de inquilinos.
## Decisión
Se aísla a ese cliente en una celda propia y el resto comparte otra.
## Alternativas consideradas
1. Limitar la tasa por inquilino: descartada porque no protege frente a una consulta que consume memoria.
2. Base de datos por inquilino: descartada porque la migración de esquema pasa de 0,2 ms a minutos.
## Consecuencias
Positivas: el radio baja a 60 % en el peor caso.
Costos: dos despliegues y un enrutador.
## Evidencia
Simulación de SE-344.
""",
}
REQ = ["Contexto", "Decisión", "Alternativas consideradas", "Consecuencias", "Reversibilidad", "Disparador de revisión", "Evidencia"]


def adr_lint(text):
    res = {}
    heads = set(re.findall(r"^## (.+)$", text, re.M))
    for r in REQ:
        res[f"sección {r}"] = r in heads
    alts = re.findall(r"^\d\. .*descartada porque", text, re.M)
    res["≥ 2 alternativas con motivo"] = len(alts) >= 2
    res["consecuencia negativa declarada"] = bool(re.search(r"(Negativas|Costos):", text))
    res["criterio medible"] = bool(re.search(r"\d+(?:[.,]\d+)?\s*(?:ms|%|h\b|horas|equipos|semanas|segundos|unidades)", text))
    res["disparador numérico"] = bool(re.search(r"Disparador de revisión\n[^\n]*\d", text))
    return res


def import_graph(root):
    files = {".".join(f.relative_to(root).with_suffix("").parts): f for f in Path(root).rglob("*.py")}
    graph = {}
    for mod, f in files.items():
        tree = ast.parse(f.read_text(encoding="utf8"))
        deps = set()
        for n in ast.walk(tree):
            if isinstance(n, ast.Import):
                deps |= {a.name for a in n.names}
            elif isinstance(n, ast.ImportFrom) and n.module:
                for a in n.names:
                    deps.add(f"{n.module}.{a.name}" if f"{n.module}.{a.name}" in files else n.module)
        graph[mod] = {d for d in deps if d.startswith("avisos")}
    return graph


LAYER = {"domain": 0, "app": 1, "infra": 2}


def violations(graph):
    out = []
    for m, deps in graph.items():
        lm = m.split(".")[1]
        for d in deps:
            ld = d.split(".")[1] if d.count(".") >= 1 else None
            if lm in LAYER and ld in LAYER and LAYER[ld] > LAYER[lm]:
                out.append((m, d))
    return sorted(out)


def cycles(graph):
    index, low, stack, on, res, counter = {}, {}, [], set(), [], [0]
    nodes = set(graph) | {d for ds in graph.values() for d in ds}

    def strong(v):
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        on.add(v)
        for w in graph.get(v, ()):
            if w not in index:
                strong(w)
                low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop()
                on.discard(w)
                comp.append(w)
                if w == v:
                    break
            if len(comp) > 1:
                res.append(sorted(comp))

    for v in sorted(nodes):
        if v not in index:
            strong(v)
    return res


def write_pkg(root, files):
    for rel, src in files.items():
        p = Path(root) / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(textwrap.dedent(src), encoding="utf8")


BASE_FILES = {
    "avisos/__init__.py": "",
    "avisos/domain/__init__.py": "",
    "avisos/domain/reglas.py": "def due(x):\n    return x\n",
    "avisos/app/__init__.py": "",
    "avisos/app/servicio.py": "from avisos.domain import reglas\n",
    "avisos/infra/__init__.py": "",
    "avisos/infra/repo.py": "from avisos.app import servicio\n",
}


def e540():
    print("SE-348 — proyecto: decisión arquitectónica defendida con ADR")
    rows = [["Criterio"] + list(ADRS)]
    results = {k: adr_lint(v) for k, v in ADRS.items()}
    for crit in results["ADR-A"]:
        rows.append([crit] + ["sí" if results[k][crit] else "NO" for k in ADRS])
    table(rows)
    print("  criterios cumplidos:", {k: f"{sum(v.values())} de {len(v)}" for k, v in results.items()})
    variants = {
        "limpia": {},
        "dominio importa infraestructura": {"avisos/domain/reglas.py": "from avisos.infra import repo\n"},
        "ciclo entre módulos de aplicación": {"avisos/app/a.py": "from avisos.app import b\n", "avisos/app/b.py": "from avisos.app import a\n"},
        "importación dinámica (no se ve)": {"avisos/domain/reglas.py": "import importlib\nm = importlib.import_module('avisos.infra.repo')\n"},
    }
    rows = [["Variante", "Violaciones de capa", "Ciclos", "Tiempo (ms)"]]
    for name, extra in variants.items():
        with tempfile.TemporaryDirectory() as tmp:
            write_pkg(tmp, {**BASE_FILES, **extra})
            t = time.perf_counter()
            g = import_graph(tmp)
            v, c = violations(g), cycles(g)
            ms = (time.perf_counter() - t) * 1000
        rows.append([name, len(v), len(c), fmt(ms, 1)])
        if v:
            print(f"  {name}: {v}")
        if c:
            print(f"  {name}: ciclos {c}")
    table(rows)
    # disparador de revisión sobre una serie de 30 días
    rng = random.Random(44)
    series = [150 + rng.uniform(-15, 15) + (0 if d < 18 else (d - 17) * 8) for d in range(30)]
    streak, day = 0, None
    for d, v in enumerate(series, 1):
        streak = streak + 1 if v > 200 else 0
        if streak >= 3 and day is None:
            day = d
    print(f"  serie sintética de p99 durante 30 días (150 ms ± 15 y una deriva desde el día 18): primer día con p99 > 200 ms: {next(d for d, v in enumerate(series, 1) if v > 200)}, el disparador de 3 días seguidos se cumple el día {day}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    which = sys.argv[1:] or ["535", "536", "537", "538", "539", "540"]
    for key in which:
        globals()[f"e{key}"]()
        print()
