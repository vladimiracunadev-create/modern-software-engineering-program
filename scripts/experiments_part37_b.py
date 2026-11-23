"""Experimentos de las clases SE-451 a SE-456 (Parte 37): tiempo real, verificación y aseguramiento.

Uso: python scripts/experiments_part37_b.py [571|572|573|574|575|576]

No se invoca ningún modelo de lenguaje. Todo es código ejecutado con la biblioteca estándar sobre el
caso conductor *Horno de curado*. Los tiempos se miden en ticks de un simulador (no en un RTOS real) y
los modelos del caso Therac-25 son supuestos del autor inspirados en el artículo de Leveson y Turner;
no reconstruyen el código de la máquina. Ninguna norma se reproduce.
"""
from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import random
import sys
import tempfile
import textwrap
from collections import deque
from pathlib import Path

from experiments_part37_lab import fmt, sci, table


# ====================================================================== SE-451
class Task:
    def __init__(self, name, prio, period, wcet, offset=0, cs=None):
        self.name, self.prio, self.period, self.wcet, self.offset, self.cs = name, prio, period, wcet, offset, cs  # cs=(inicio, fin) dentro de la ejecución


def simulate(tasks, horizon, protocol):
    """Planificación apropiativa de prioridades fijas con un mutex. protocol: 'none' | 'inherit' | 'ceiling'."""
    jobs = []
    lock_owner = None
    ceiling = max(t.prio for t in tasks if t.cs)
    misses = {t.name: 0 for t in tasks}
    resp = {t.name: 0 for t in tasks}
    blocked_ticks = {t.name: 0 for t in tasks}

    def eff(j):
        p = j["task"].prio
        if protocol == "ceiling" and j["holding"]:
            p = max(p, ceiling)
        if protocol == "inherit" and j["holding"]:
            waiters = [w["task"].prio for w in jobs if w["waiting"] and not w["done"]]
            if waiters:
                p = max(p, max(waiters))
        return p

    for now in range(horizon):
        for t in tasks:
            if now >= t.offset and (now - t.offset) % t.period == 0:
                jobs.append({"task": t, "rel": now, "done_c": 0, "holding": False, "waiting": False, "done": False})
        for j in jobs:
            if not j["done"] and now - j["rel"] >= j["task"].period:
                misses[j["task"].name] += 1
                j["done"] = True
                if lock_owner is j:
                    lock_owner = None
        ready = []
        for j in jobs:
            if j["done"]:
                continue
            t = j["task"]
            if t.cs and j["done_c"] == t.cs[0] and not j["holding"]:
                if lock_owner is None or lock_owner is j:
                    lock_owner = j
                    j["holding"] = True
                    j["waiting"] = False
                else:
                    j["waiting"] = True
                    blocked_ticks[t.name] += 1
                    continue
            ready.append(j)
        if not ready:
            continue
        run = max(ready, key=lambda j: (eff(j), -j["rel"]))
        run["done_c"] += 1
        t = run["task"]
        if t.cs and run["holding"] and run["done_c"] == t.cs[1]:
            run["holding"] = False
            lock_owner = None
        if run["done_c"] >= t.wcet:
            run["done"] = True
            resp[t.name] = max(resp[t.name], now + 1 - run["rel"])
    return misses, resp, blocked_ticks


def rta(tasks, blocking):
    """Análisis de tiempo de respuesta de prioridades fijas: R = C + B + suma de interferencias."""
    out = {}
    for t in sorted(tasks, key=lambda x: -x.prio):
        hp = [h for h in tasks if h.prio > t.prio]
        r = t.wcet + blocking.get(t.name, 0)
        while True:
            nxt = t.wcet + blocking.get(t.name, 0) + sum(math.ceil(r / h.period) * h.wcet for h in hp)
            if nxt == r or nxt > 10 * t.period:
                break
            r = nxt
        out[t.name] = nxt if nxt != r else r
    return out


def steps_sort(a):
    a = list(a)
    steps = 0
    n = len(a)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n - 1):
            steps += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
                steps += 1
    return steps


def e571():
    print("SE-451 — tiempo real: inversión de prioridad, análisis de respuesta y WCET (simulador de ticks de 1 ms)")
    tasks = [Task("H", 3, 40, 10, offset=8, cs=(2, 7)), Task("M", 2, 70, 30, offset=7), Task("L", 1, 200, 30, offset=0, cs=(5, 20))]
    for proto in ("none", "inherit", "ceiling"):
        misses, resp, blk = simulate(tasks, 400, proto)
        print(f"  protocolo {proto:8s}: plazos perdidos {misses}; respuesta máxima observada (ms) {resp}; ticks de H bloqueada {blk['H']}")
    print("  utilización:", fmt(sum(t.wcet / t.period for t in tasks), 3), "; cota de Liu y Layland para 3 tareas:", fmt(3 * (2 ** (1 / 3) - 1), 3))
    for blk, label in (({}, "sin bloqueo"), ({"H": 13, "M": 13}, "bloqueo de 13 ms para H por la sección crítica y para M por la herencia")):
        r = rta(tasks, blk)
        print(f"  análisis de respuesta ({label}): {r}")
    sets = {
        "A": [Task("t1", 3, 20, 4), Task("t2", 2, 45, 9), Task("t3", 1, 100, 20)],
        "B": [Task("t1", 3, 20, 4), Task("t2", 2, 45, 14), Task("t3", 1, 100, 33)],
        "C": [Task("t1", 3, 20, 4), Task("t2", 2, 45, 18), Task("t3", 1, 100, 35)],
    }
    bound = 3 * (2 ** (1 / 3) - 1)
    for name, ts in sets.items():
        u = sum(t.wcet / t.period for t in ts)
        r = rta(ts, {})
        ok = all(r[t.name] <= t.period for t in ts)
        print(f"  conjunto {name}: U {fmt(u, 3)}; supera la cota: {u > bound}; respuestas {r}; planificable por análisis: {ok}")
    rng = random.Random(47)
    worst = steps_sort(list(range(8, 0, -1)))
    maxr = max(steps_sort(rng.sample(range(8), 8)) for _ in range(1000))
    typical = sorted(steps_sort(rng.sample(range(8), 8)) for _ in range(1000))[500]
    print(f"  WCET en pasos de una ordenación de 8 elementos: mediana de 1000 entradas al azar {typical}, máximo observado {maxr}, peor caso real (orden inverso) {worst}")
    print(f"  la marca de agua medida queda {fmt(100 * (worst - maxr) / worst, 1)} % por debajo del peor caso; el análisis de caminos lo encuentra, la medición no garantiza hacerlo")


# ====================================================================== SE-452
CHECKS = {
    "R1 sin recursión": lambda t: [f.name for f in ast.walk(t) if isinstance(f, ast.FunctionDef) and any(isinstance(c, ast.Call) and getattr(c.func, "id", None) == f.name for c in ast.walk(f))],
    "R2 bucles con cota": lambda t: [n.lineno for n in ast.walk(t) if isinstance(n, ast.While) and isinstance(n.test, ast.Constant) and n.test.value is True],
    "R3 funciones cortas (60 líneas)": lambda t: [f.name for f in ast.walk(t) if isinstance(f, ast.FunctionDef) and (f.end_lineno - f.lineno + 1) > 60],
    "R4 aserciones en funciones con lógica": lambda t: [f.name for f in ast.walk(t) if isinstance(f, ast.FunctionDef) and sum(isinstance(n, (ast.If, ast.For, ast.While)) for n in ast.walk(f)) >= 2 and not any(isinstance(n, ast.Assert) for n in ast.walk(f))],
    "R5 valor de retorno comprobado": lambda t: [n.lineno for n in ast.walk(t) if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and getattr(n.value.func, "attr", "") in ("write", "remove", "send", "acquire")],
    "R6 sin excepción vacía": lambda t: [n.lineno for n in ast.walk(t) if isinstance(n, ast.ExceptHandler) and len(n.body) == 1 and isinstance(n.body[0], ast.Pass)],
}

MALO = textwrap.dedent('''
    def suma(n):
        if n == 0:
            return 0
        return n + suma(n - 1)

    def bucle(sensor):
        while True:
            v = sensor.read()
            if v > 250:
                break
            if v < 0:
                continue

    def guarda(f, x):
        f.write(x)
        try:
            f.flush()
        except OSError:
            pass
''')
BUENO = textwrap.dedent('''
    def suma(n):
        assert 0 <= n <= 1000
        total = 0
        for i in range(1, n + 1):
            total += i
        return total

    def bucle(sensor, maximo=1000):
        assert maximo > 0
        for _ in range(maximo):
            v = sensor.read()
            if v > 250:
                return True
            if v < 0:
                continue
        return False

    def guarda(f, x):
        n = f.write(x)
        assert n == len(x)
        f.flush()
''')


def avg_bug(a, b):
    return ((a + b) & 0xFFFF) // 2          # promedio ingenuo con aritmética de 16 bits sin signo


def avg_ok(a, b):
    return a + (b - a) // 2 if b >= a else b + (a - b) // 2


def e572():
    print("SE-452 — codificación segura: reglas comprobables por máquina (estilo de las diez reglas de la NASA/JPL, sobre Python)")
    for name, src in (("malo", MALO), ("bueno", BUENO)):
        tree = ast.parse(src)
        res = {k: len(f(tree)) for k, f in CHECKS.items()}
        print(f"  muestra {name}: " + "; ".join(f"{k}: {v}" for k, v in res.items()) + f"; total {sum(res.values())}")
    cond = textwrap.dedent('''
        def altura(nodo):
            if nodo is None:
                return 0
            return 1 + max(altura(nodo.izq), altura(nodo.der))
    ''')
    print(f"  falso positivo de R1 sobre una recursión acotada por la profundidad de un árbol: {len(CHECKS['R1 sin recursión'](ast.parse(cond)))} aviso; la regla no mira la cota")
    rng = random.Random(47)
    n = 200000
    wrong = sum(avg_bug(a, b) != (a + b) // 2 for a, b in ((rng.randrange(65536), rng.randrange(65536)) for _ in range(n)))
    wrong_ok = sum(avg_ok(a, b) != (a + b) // 2 for a, b in ((rng.randrange(65536), rng.randrange(65536)) for _ in range(n)))
    print(f"  promedio de dos enteros de 16 bits sin signo con desbordamiento silencioso (semilla 47, {n} pares): resultado incorrecto en {wrong} ({fmt(100 * wrong / n, 1)} %); con la resta previa: {wrong_ok}")
    small = sum(avg_bug(a, b) != (a + b) // 2 for a in range(0, 256) for b in range(0, 256))
    print(f"  si las pruebas usan valores pequeños (0 a 255), el defecto no aparece: {small} fallos de 65536 pares")
    print("  las reglas de MISRA C y de SEI CERT C se aplican a C; aquí se muestra la clase de defecto con aritmética emulada y no se ejecuta C")


# ====================================================================== SE-453
def explore(init, succ, invariant, deadlock_ok=lambda s: False, limit=2_000_000):
    seen = {init: None}
    q = deque([init])
    violation = None
    deadlock = None
    while q:
        s = q.popleft()
        if not invariant(s) and violation is None:
            violation = s
            break
        nxt = succ(s)
        if not nxt and not deadlock_ok(s) and deadlock is None:
            deadlock = s
        for n in nxt:
            if n not in seen:
                seen[n] = s
                q.append(n)
        if len(seen) > limit:
            break
    return seen, violation, deadlock


def trace(seen, s):
    out = []
    while s is not None:
        out.append(s)
        s = seen[s]
    return list(reversed(out))


def lock_protocol(kind):
    # estado: (pc0, pc1, flag0, flag1, turn)
    def succ(s):
        pc, flag, turn = [s[0], s[1]], [s[2], s[3]], s[4]
        res = []
        for i in (0, 1):
            o = 1 - i
            p = pc[i]
            def mk(npc=None, nf=None, nt=None):
                pcn = pc.copy(); fl = flag.copy(); t = turn
                if npc is not None: pcn[i] = npc
                if nf is not None: fl[i] = nf
                if nt is not None: t = nt
                return (pcn[0], pcn[1], fl[0], fl[1], t)
            if kind == "comprobar y luego marcar":
                if p == 0 and not flag[o]: res.append(mk(npc=1))
                elif p == 1: res.append(mk(npc=2, nf=1))
                elif p == 2: res.append(mk(npc=3, nf=0))
                elif p == 3: res.append(mk(npc=0))
            elif kind == "solo bandera":
                if p == 0: res.append(mk(npc=1, nf=1))
                elif p == 1 and not flag[o]: res.append(mk(npc=2))
                elif p == 2: res.append(mk(npc=3, nf=0))
                elif p == 3: res.append(mk(npc=0))
            elif kind == "Peterson con pasos invertidos":
                if p == 0: res.append(mk(npc=1, nt=o))
                elif p == 1: res.append(mk(npc=2, nf=1))
                elif p == 2 and (not flag[o] or turn == i): res.append(mk(npc=3))
                elif p == 3: res.append(mk(npc=4, nf=0))
                elif p == 4: res.append(mk(npc=0))
            else:  # Peterson
                if p == 0: res.append(mk(npc=1, nf=1))
                elif p == 1: res.append(mk(npc=2, nt=o))
                elif p == 2 and (not flag[o] or turn == i): res.append(mk(npc=3))
                elif p == 3: res.append(mk(npc=4, nf=0))
                elif p == 4: res.append(mk(npc=0))
        return res

    # la sección crítica es pc==2 en los dos primeros protocolos y pc==3 en el tercero
    crit = 3 if kind.startswith("Peterson") else 2
    inv = lambda s: not (s[0] == crit and s[1] == crit)
    # un protocolo que no pueda avanzar nunca por falta de transiciones es un bloqueo
    return (0, 0, 0, 0, 0), succ, inv


def random_run(kind, rng, steps=40):
    init, succ, inv = lock_protocol(kind)
    s = init
    for _ in range(steps):
        nx = succ(s)
        if not nx:
            return False
        s = rng.choice(nx)
        if not inv(s):
            return True
    return False


def horno_model(con_puerta):
    # estado: (calentador, puerta, temp) temp 0..3 (3 = sobre el límite)
    def succ(s):
        h, d, t = s
        res = []
        res.append((0 if (con_puerta and d == 0) else h, 1 - d, t))   # el operador abre o cierra; con enclavamiento, abrir corta la potencia
        if not h and (d == 0 or not con_puerta) and t < 2: res.append((1, d, t))   # el controlador conecta (sin enclavamiento no mira la puerta)
        if h and t < 2: res.append((h, d, t + 1))         # calienta hasta el límite del limitador
        if h and t >= 2: res.append((0, d, t))            # el limitador corta
        if not h and t > 0: res.append((h, d, t - 1))     # enfría
        return res
    inv = lambda s: not (s[0] == 1 and s[1] == 1) and s[2] < 3
    return (0, 0, 0), succ, inv


def count_states(n):
    # n procesos, cada uno con pasos 0..3; un recurso compartido contador de 0..n: espacio de estados de producto
    init = (0,) * n + (0,)
    def succ(s):
        res = []
        for i in range(n):
            if s[i] < 3:
                ns = list(s); ns[i] += 1
                if s[i] == 1: ns[-1] = min(n, ns[-1] + 1)
                res.append(tuple(ns))
        return res
    seen, _, _ = explore(init, succ, lambda s: True, deadlock_ok=lambda s: True)
    return len(seen)


def e573():
    print("SE-453 — verificación formal: un verificador propio de estados explícitos (sin TLA+, SPARK ni Alloy ejecutados)")
    for kind in ("comprobar y luego marcar", "solo bandera", "Peterson con pasos invertidos", "Peterson"):
        init, succ, inv = lock_protocol(kind)
        seen, viol, dead = explore(init, succ, inv)
        msg = f"exclusión mutua {'VIOLADA' if viol else 'se cumple'}"
        if viol:
            tr = trace(seen, viol)
            msg += f"; contraejemplo de {len(tr) - 1} pasos"
        msg += f"; bloqueo alcanzable: {'sí' if dead else 'no'}"
        print(f"  protocolo {kind:26s}: {len(seen)} estados alcanzables; {msg}")
    rng = random.Random(47)
    for kind in ("comprobar y luego marcar", "Peterson con pasos invertidos"):
        runs = 20000
        hit = sum(random_run(kind, rng) for _ in range(runs))
        print(f"  planificaciones al azar contra «{kind}» ({runs} corridas de 40 pasos, semilla 47): encuentran la violación en {hit} ({fmt(100 * hit / runs, 2)} %); el verificador la encuentra siempre")
    for con in (False, True):
        init, succ, inv = horno_model(con)
        seen, viol, _ = explore(init, succ, inv, deadlock_ok=lambda s: True)
        tr = trace(seen, viol) if viol else []
        print(f"  Horno con enclavamiento de puerta {'activo ' if con else 'ausente'}: {len(seen)} estados; invariante {'VIOLADO' if viol else 'se cumple'}" + (f"; contraejemplo {tr}" if viol else ""))
    print("  crecimiento del espacio de estados con el número de procesos (cada uno con 4 pasos):")
    for n in range(2, 8):
        print(f"    {n} procesos: {count_states(n)} estados")


# ====================================================================== SE-454
CONDS = ["alta", "puerta", "habil", "manual"]


def decision(a, p, h, m):
    return (a or p) and h and not m


def mcdc_pairs():
    vectors = list(itertools.product([0, 1], repeat=4))
    pairs = {c: [] for c in range(4)}
    for u, v in itertools.combinations(vectors, 2):
        diff = [i for i in range(4) if u[i] != v[i]]
        if len(diff) == 1 and decision(*u) != decision(*v):
            pairs[diff[0]].append((u, v))
    return vectors, pairs


def mutants():
    ms = {}
    for i, name in enumerate(CONDS):
        for val in (0, 1):
            ms[f"{name} fija en {val}"] = (lambda i, val: lambda a, p, h, m: decision(*[val if k == i else x for k, x in enumerate((a, p, h, m))]))(i, val)
    ms["or por and"] = lambda a, p, h, m: (a and p) and h and not m
    ms["and por or (habil)"] = lambda a, p, h, m: ((a or p) or h) and not m
    ms["sin negación de manual"] = lambda a, p, h, m: (a or p) and h and m
    ms["negar alta"] = lambda a, p, h, m: ((not a) or p) and h and not m
    ms["negar puerta"] = lambda a, p, h, m: (a or (not p)) and h and not m
    ms["negar habil"] = lambda a, p, h, m: (a or p) and (not h) and not m
    ms["and por or (final)"] = lambda a, p, h, m: ((a or p) and h) or not m
    ms["sin alta"] = lambda a, p, h, m: p and h and not m
    ms["sin puerta"] = lambda a, p, h, m: a and h and not m
    return ms


def killed(tests, ms):
    return sum(any(f(*t) != decision(*t) for t in tests) for f in ms.values())


def sim_plant(delay, rng, scenarios=300):
    viol = 0
    for _ in range(scenarios):
        t = 20.0
        heater = False
        hist = [t] * (delay + 1)
        setpoint = rng.choice([200, 220, 240])
        rate = rng.uniform(0.8, 2.2)
        for s in range(600):
            seen = hist[-(delay + 1)]
            heater = seen < setpoint
            if seen >= 245:
                heater = False
            t += (rate if heater else 0) - 0.004 * (t - 20)
            hist.append(t)
            if t > 250:
                viol += 1
                break
    return viol


def e574():
    print("SE-454 — verificación y cobertura: MC/DC sobre una decisión de cuatro condiciones, mutantes, SIL y HIL")
    vectors, pairs = mcdc_pairs()
    print(f"  decisión: (alta o puerta) y habil y no manual; {len(vectors)} vectores posibles; pares de independencia por condición: " + ", ".join(f"{CONDS[i]} {len(p)}" for i, p in pairs.items()))
    sets = []
    for k in range(5, 8):
        for combo in itertools.combinations(vectors, k):
            if all(any(u in combo and v in combo for u, v in pairs[c]) for c in range(4)):
                sets.append(combo)
        if sets:
            print(f"  tamaño mínimo de un conjunto MC/DC: {k} (n + 1 = 5); conjuntos mínimos distintos: {len(sets)}")
            break
    ms = mutants()
    total = len(ms)
    dc_sets = [c for c in itertools.combinations(vectors, 2) if len({decision(*v) for v in c}) == 2]
    cc_sets = [c for c in itertools.combinations(vectors, 2) if all(len({v[i] for v in c}) == 2 for i in range(4))]
    cc_sets_bad = [c for c in cc_sets if len({decision(*v) for v in c}) == 1]
    kd = [killed(c, ms) for c in dc_sets]
    kc = [killed(c, ms) for c in cc_sets]
    km = [killed(c, ms) for c in sets]
    print(f"  mutantes de la decisión: {total}; los 16 vectores matan {killed(vectors, ms)}")
    print(f"  cobertura de decisión (2 pruebas): {len(dc_sets)} conjuntos; matan de {min(kd)} a {max(kd)} (media {fmt(sum(kd) / len(kd), 1)})")
    print(f"  cobertura de condiciones (2 pruebas): {len(cc_sets)} conjuntos; de ellos {len(cc_sets_bad)} nunca cambian el resultado de la decisión; matan de {min(kc)} a {max(kc)} (media {fmt(sum(kc) / len(kc), 1)})")
    print(f"  MC/DC (5 pruebas): {len(sets)} conjuntos; matan de {min(km)} a {max(km)} (media {fmt(sum(km) / len(km), 1)})")
    surv = [n for n, f in ms.items() if all(f(*t) == decision(*t) for t in vectors)]
    print("  mutantes equivalentes (sobreviven a los 16 vectores):", surv or "ninguno")
    rng = random.Random(47)
    print("  SIL: 300 escenarios de calentamiento con el limitador en 245 y fallo si T > 250; retardo del sensor en muestras:")
    for d in (0, 2, 5, 10, 15):
        print(f"    retardo {d}: {sim_plant(d, random.Random(47))} escenarios con violación")


# ====================================================================== SE-455
def therac_race(rng, treatments, edit_prob, window, variant):
    """Modelo del autor: el operador corrige datos con probabilidad edit_prob; la edición cae en un instante
    uniforme de 0 a 20 s tras marcar entrada completa; el ajuste de imanes dura `window` s."""
    inconsistent = 0
    hazardous = 0
    for _ in range(treatments):
        if rng.random() >= edit_prob:
            continue
        t_edit = rng.uniform(0, 20)
        in_window = t_edit < window
        if variant == "original":
            bad = in_window and t_edit > 0.5   # la comprobación solo mira en la primera pasada
        elif variant == "versionado":
            bad = False                          # cada edición invalida el ajuste y lo reinicia
        else:
            bad = in_window and t_edit > 0.5
        if bad:
            inconsistent += 1
            if variant == "original":
                hazardous += 1
            elif variant == "con enclavamiento":
                hazardous += rng.random() < 0.01   # el enclavamiento de hardware falla o se anula con probabilidad del autor
    return inconsistent, hazardous


def e575():
    print("SE-455 — análisis de un fallo real frente a las ideas de las normas: modelos del autor sobre el caso Therac-25")
    rng = random.Random(47)
    n = 100000
    print(f"  condición de carrera ({n} tratamientos por celda; edición con probabilidad 0,15; ajuste de 8 s; semilla 47):")
    rows = [["Variante", "Configuraciones inconsistentes", "Exposiciones peligrosas"]]
    for v in ("original", "con enclavamiento", "versionado"):
        inc, haz = therac_race(rng, n, 0.15, 8.0, v)
        rows.append([v, inc, haz])
    table(rows)
    print("  sensibilidad al tiempo de ajuste (variante original): ", end="")
    for w in (2, 4, 8, 12):
        inc, _ = therac_race(rng, n, 0.15, float(w), "original")
        print(f"{w} s -> {inc}", end="; ")
    print()
    print("  contador de un byte (modelo del autor del mecanismo documentado):")
    for variant in ("incrementar", "asignar 1"):
        skipped = 0
        value = 0
        passes = 100000
        for _ in range(passes):
            value = (value + 1) & 0xFF if variant == "incrementar" else 1
            if value == 0:
                skipped += 1
        print(f"    {variant}: la comprobación del colimador se omite en {skipped} de {passes} pasadas ({fmt(100 * skipped / passes, 3)} %)")
    print("  análisis de carga: con 300 pasadas por puesta a punto y una pulsación en instante uniforme, la probabilidad de coincidir con la pasada 256 es", fmt(100 / 300, 2), "% por puesta a punto (supuesto del autor: el dato real no se publica)")


# ====================================================================== SE-456
def build_package(root, req_text_change=False):
    reqs = {
        "REQ-01": "El calentador se desconecta si la temperatura medida supera el límite.",
        "REQ-02": "El calentador se desconecta si la puerta está abierta.",
        "REQ-03": "Un sensor sin lectura lleva al estado seguro.",
        "REQ-04": "El limitador es independiente del lazo de control.",
        "REQ-05": "Un reinicio del procesador deja el calentador desconectado.",
    }
    if req_text_change:
        reqs["REQ-02"] = "El calentador se desconecta si la puerta está abierta o entreabierta."
    hazards = {
        "H1": {"texto": "Sobretemperatura sostenida", "controles": ["REQ-01", "REQ-04"]},
        "H2": {"texto": "Calentador con puerta abierta", "controles": ["REQ-02"]},
        "H3": {"texto": "Sensor sin lectura", "controles": ["REQ-03"]},
        "H4": {"texto": "Reinicio con calentador conectado", "controles": ["REQ-05"]},
        "H5": {"texto": "Deriva de calibración", "controles": []},
    }
    tests = {"T1": ["REQ-01"], "T2": ["REQ-01", "REQ-04"], "T3": ["REQ-02"], "T4": ["REQ-03"]}
    results = {"T1": "pasa", "T2": "pasa", "T3": "pasa", "T4": "pasa"}
    files = {"requisitos.json": reqs, "peligros.json": hazards, "pruebas.json": tests, "resultados.json": results}
    for name, data in files.items():
        (root / name).write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    return reqs, hazards, tests, results


def build_hz():
    with tempfile.TemporaryDirectory() as d:
        return build_package(Path(d))[1]


def check_package(root, manifest=None):
    load = lambda n: json.loads((root / n).read_text(encoding="utf-8"))
    reqs, hazards, tests, results = load("requisitos.json"), load("peligros.json"), load("pruebas.json"), load("resultados.json")
    gaps = []
    for h, d in hazards.items():
        if not d["controles"]:
            gaps.append(f"{h} sin ningún control")
        for c in d["controles"]:
            if c not in reqs:
                gaps.append(f"{h} apunta a {c}, que no existe")
            elif not any(c in rs and results.get(t) == "pasa" for t, rs in tests.items()):
                gaps.append(f"{h}: el control {c} no tiene una prueba que pase")
    for r in reqs:
        if not any(r in rs for rs in tests.values()):
            gaps.append(f"{r} sin prueba")
    digest = {n: hashlib.sha256((root / n).read_bytes()).hexdigest()[:12] for n in ("requisitos.json", "peligros.json", "pruebas.json", "resultados.json")}
    stale = [n for n, d in (manifest or {}).items() if digest[n] != d]
    return gaps, digest, stale


def e576():
    print("SE-456 — paquete de aseguramiento del Horno de curado: comprobaciones automáticas de completitud y de evidencia obsoleta")
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        build_package(root)
        gaps, digest, _ = check_package(root)
        print(f"  paquete inicial: {len(gaps)} huecos:")
        for g in gaps:
            print("    -", g)
        manifest = dict(digest)
        build_package(root, req_text_change=True)
        gaps2, _, stale = check_package(root, manifest)
        print(f"  tras editar el texto de REQ-02 sin rehacer la evidencia: archivos de evidencia que ya no coinciden con el manifiesto: {stale}; huecos de contenido: {len(gaps2)}")
        print("  el manifiesto de hashes no dice si la prueba sigue valiendo; dice que la evidencia ya no es la que se firmó y que alguien debe decidirlo")
    hz = json.loads(json.dumps(build_hz()))
    ok = sum(1 for h, dd in hz.items() if dd["controles"] and all(c not in ("REQ-05",) for c in dd["controles"]))
    nh = len(hz)
    print(f"  cobertura de peligros con control verificado: {ok} de {nh} ({fmt(100 * ok / nh, 0)} %); el peligro H5 queda abierto y debe figurar como riesgo residual aceptado por una persona con autoridad, no como cumplido")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    which = sys.argv[1:] or ["571", "572", "573", "574", "575", "576"]
    for key in which:
        globals()[f"e{key}"]()
        print()
