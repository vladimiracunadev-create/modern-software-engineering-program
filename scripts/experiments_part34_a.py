"""Experimentos de SE-409 a SE-414 (datos sintéticos, semilla fija, solo biblioteca estándar).

Uso: python scripts/experiments_part34_a.py   (imprime una línea JSON por experimento)

Todos los experimentos son deterministas: usan ``random.Random(semilla)``, tiempo virtual
y aritmética de la biblioteca estándar; no hay red, reloj ni servicio reales.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import random
import sys
from functools import lru_cache


# ------------------------------------------------------------------ SE-409
@lru_cache(None)
def e409_ramas() -> dict:
    """Conflictos de integración según la vida de la rama (8 personas, 400 archivos, puntos calientes)."""
    r = random.Random(409)
    files = 400
    weights = [1 / (i + 1) ** 0.8 for i in range(files)]
    per_day = 3
    devs = 8
    out = {}
    trials = 3000
    for days in (0.5, 1, 2, 5, 10, 20):
        conflict = 0
        shared = 0
        for _ in range(trials):
            mine = set(r.choices(range(files), weights, k=max(1, round(per_day * days))))
            theirs = set(r.choices(range(files), weights, k=max(1, round(per_day * days * (devs - 1)))))
            both = mine & theirs
            conflict += bool(both)
            shared += len(both)
        out[days] = (conflict / trials, shared / trials)
    return out


@lru_cache(None)
def e409_lotes() -> dict:
    """Builds necesarios para aislar los cambios defectuosos cuando la integración se comprueba por lotes."""
    r = random.Random(4092)
    p = 0.04
    commits = 24000
    bad = [r.random() < p for _ in range(commits)]

    def isolate(chunk):
        builds = 1
        if not any(chunk):
            return builds, 0
        if len(chunk) == 1:
            return builds, 1
        mid = len(chunk) // 2
        b1, f1 = isolate(chunk[:mid])
        b2, f2 = isolate(chunk[mid:])
        return builds + b1 + b2, f1 + f2

    out = {}
    for k in (1, 2, 5, 10, 25, 50):
        builds = red = found = 0
        for i in range(0, commits, k):
            chunk = bad[i:i + k]
            b, f = isolate(chunk)
            builds += b
            red += any(chunk)
            found += f
        batches = commits // k
        out[k] = (red / batches, builds / commits, found)
    return out


@lru_cache(None)
def e409_cola() -> dict:
    """Troncal roto por conflictos semánticos: PR probado contra su base frente a cola de integración."""
    r = random.Random(4093)
    q = 0.02  # probabilidad de choque semántico entre dos PR que se solapan
    merges = 4000
    rate_per_day = 12
    out = {}
    for life in (0.25, 1, 3):
        # los PR entran por un proceso de Poisson; cada uno vive "life" días y se integra al final
        t = 0.0
        events = []
        for _ in range(merges):
            t += r.expovariate(rate_per_day)
            events.append((t, t + life))
        merged_end = sorted(e[1] for e in events)
        broken = 0
        for start, end in events:
            # PR integrados mientras este vivía: están en la troncal pero no en su base
            ahead = sum(1 for m in merged_end if start < m < end)
            if any(r.random() < q for _ in range(ahead)):
                broken += 1
        # con cola: el PR se prueba junto con los que lo preceden; el mismo choque se descubre antes de integrar
        rejected = broken
        out[life] = (broken / merges * 1000, rejected / merges * 1000)
    return out


# ------------------------------------------------------------------ SE-410
JOBS = {
    "preparar": (1.0, []),
    "lint": (2.0, ["preparar"]),
    "tipos": (3.0, ["preparar"]),
    "unitarias": (6.0, ["preparar"]),
    "compilar": (4.0, ["preparar"]),
    "integración": (9.0, ["compilar"]),
    "e2e": (12.0, ["compilar"]),
    "documentación": (2.0, ["preparar"]),
    "empaquetar": (3.0, ["lint", "tipos", "unitarias", "integración", "e2e", "documentación"]),
}
OVERHEAD = 0.5  # minutos de arranque por job (supuesto del autor)


def _schedule(runners: int) -> float:
    done: dict[str, float] = {}
    free = [0.0] * runners
    pending = dict(JOBS)
    while pending:
        ready = [n for n, (_, deps) in pending.items() if all(d in done for d in deps)]
        # lista por duración decreciente (heurística habitual)
        ready.sort(key=lambda n: -JOBS[n][0])
        for n in ready:
            free.sort()
            dur, deps = JOBS[n]
            start = max(free[0], max((done[d] for d in deps), default=0.0))
            done[n] = start + OVERHEAD + dur
            free[0] = done[n]
            del pending[n]
    return max(done.values())


@lru_cache(None)
def e410_dag() -> dict:
    total = sum(d + OVERHEAD for d, _ in JOBS.values())
    out = {}
    for n in (1, 2, 3, 4, 8):
        out[n] = (_schedule(n), total)
    # camino crítico
    memo: dict[str, float] = {}

    def cp(name: str) -> float:
        if name in memo:
            return memo[name]
        d, deps = JOBS[name]
        memo[name] = d + OVERHEAD + max((cp(x) for x in deps), default=0.0)
        return memo[name]

    out["critico"] = max(cp(n) for n in JOBS)
    out["total"] = total
    return out


LEVELS = {"so": ["linux", "windows", "macos"], "py": ["3.10", "3.11", "3.12", "3.13"], "db": ["sqlite", "postgres", "mysql"]}


def _all_cases():
    return list(itertools.product(*LEVELS.values()))


def _pairwise_greedy():
    cases = _all_cases()
    need = set()
    for a, b in itertools.combinations(range(3), 2):
        for x in LEVELS[list(LEVELS)[a]]:
            for y in LEVELS[list(LEVELS)[b]]:
                need.add(((a, x), (b, y)))
    chosen = []
    while need:
        best = max(cases, key=lambda c: sum(1 for (a, x), (b, y) in need if c[a] == x and c[b] == y))
        chosen.append(best)
        need = {(p, q) for p, q in need if not (best[p[0]] == p[1] and best[q[0]] == q[1])}
    return chosen


@lru_cache(None)
def e410_matriz() -> dict:
    r = random.Random(410)
    cases = _all_cases()
    pair = _pairwise_greedy()
    base = ("linux", "3.12", "sqlite")
    ofat = {base}
    for i, name in enumerate(LEVELS):
        for lvl in LEVELS[name]:
            c = list(base)
            c[i] = lvl
            ofat.add(tuple(c))
    strategies = {"completa": cases, "una a la vez": sorted(ofat), "pareja a pareja": pair}
    hits = {s: {1: 0, 2: 0, 3: 0} for s in list(strategies) + ["9 al azar"]}
    trials = 400
    for _ in range(trials):
        defs = {}
        pos = r.sample(range(3), 3)
        # un defecto de cada orden: depende de 1, 2 o 3 factores
        for order in (1, 2, 3):
            idx = sorted(r.sample(range(3), order))
            defs[order] = {i: r.choice(LEVELS[list(LEVELS)[i]]) for i in idx}
        for s, cs in strategies.items():
            for order, d in defs.items():
                if any(all(c[i] == v for i, v in d.items()) for c in cs):
                    hits[s][order] += 1
        sample = r.sample(cases, 9)
        for order, d in defs.items():
            if any(all(c[i] == v for i, v in d.items()) for c in sample):
                hits["9 al azar"][order] += 1
    out = {s: (len(strategies[s]) if s in strategies else 9, *(hits[s][o] / trials for o in (1, 2, 3))) for s in hits}
    out["_total"] = len(cases)
    return out


@lru_cache(None)
def e410_cache() -> dict:
    r = random.Random(4102)
    builds = 600
    p_lock = 0.10
    rerun = 0.15
    full, delta, hit_t = 180, 45, 8  # segundos (supuestos)
    lock = 0
    saved: dict[str, int] = {}
    stats = {k: {"hit": 0, "parcial": 0, "fallo": 0, "seg": 0, "obsoleto": 0} for k in ("hash del lockfile", "SHA del commit", "clave fija", "hash + respaldo")}
    last_fixed = 0
    last_any = 0
    sha = 0
    for _ in range(builds):
        if r.random() < p_lock:
            lock += 1
        if r.random() >= rerun:
            sha += 1
        # hash del lockfile
        s = stats["hash del lockfile"]
        if f"l{lock}" in saved:
            s["hit"] += 1; s["seg"] += hit_t
        else:
            s["fallo"] += 1; s["seg"] += full; saved[f"l{lock}"] = 1
        # SHA del commit
        s = stats["SHA del commit"]
        if f"c{sha}" in saved:
            s["hit"] += 1; s["seg"] += hit_t
        else:
            s["fallo"] += 1; s["seg"] += full; saved[f"c{sha}"] = 1
        # clave fija: siempre restaura lo último guardado; solo se guarda la primera vez
        s = stats["clave fija"]
        s["hit"] += 1; s["seg"] += hit_t
        if last_fixed != lock:
            s["obsoleto"] += 1  # el entorno no coincide con el lockfile
        if last_fixed == 0 and lock == 0:
            pass
        if "fixed" not in saved:
            saved["fixed"] = 1
            last_fixed = lock
        # hash + respaldo por prefijo
        s = stats["hash + respaldo"]
        if f"r{lock}" in saved:
            s["hit"] += 1; s["seg"] += hit_t
        elif lock > 0 and "any" in saved:
            s["parcial"] += 1; s["seg"] += delta; saved[f"r{lock}"] = 1
        else:
            s["fallo"] += 1; s["seg"] += full; saved[f"r{lock}"] = 1; saved["any"] = 1
    return {k: (v["hit"] / builds, v["parcial"] / builds, v["seg"] / builds, v["obsoleto"] / builds) for k, v in stats.items()} | {"_lock_cambios": lock}


# ------------------------------------------------------------------ SE-411
STAGES = {  # nombre: (minutos, probabilidad de que un build rojo se deba a este defecto)
    "lint": (0.3, 0.22),
    "tipos": (1.0, 0.14),
    "unitarias": (3.0, 0.30),
    "integración": (8.0, 0.22),
    "e2e": (14.0, 0.12),
}


def _expected(order):
    red_time = 0.0
    for stage, (_, p) in STAGES.items():
        t = 0.0
        for s in order:
            t += STAGES[s][0]
            if s == stage:
                break
        red_time += p * t
    green_time = sum(STAGES[s][0] for s in order)
    return red_time, green_time


@lru_cache(None)
def e411_orden() -> dict:
    names = list(STAGES)
    perms = list(itertools.permutations(names))
    reds = [_expected(p)[0] for p in perms]
    best = min(perms, key=lambda p: _expected(p)[0])
    ratio = tuple(sorted(names, key=lambda s: -STAGES[s][1] / STAGES[s][0]))
    return {
        "barato primero": (_expected(tuple(sorted(names, key=lambda s: STAGES[s][0])))[0],),
        "caro primero": (_expected(tuple(sorted(names, key=lambda s: -STAGES[s][0])))[0],),
        "media de 120 órdenes": (sum(reds) / len(reds),),
        "mínimo": (min(reds),),
        "máximo": (max(reds),),
        "mejor orden": best,
        "por razón p/costo": ratio,
        "verde": _expected(best)[1],
        "razón_coincide": ratio == best,
    }


WORKFLOWS = 160


def _make_workflows():
    r = random.Random(4112)
    issues = ["sin_pin", "permisos", "target_checkout", "inyeccion", "curl_bash", "eco_secreto", "continuar", "token_fijo"]
    decoys = ["comentario_curl", "accion_local", "sha_confiable", "nombre_target", "rama_literal", "numero_pr"]
    data = []
    for i in range(WORKFLOWS):
        truth = {k for k in issues if r.random() < 0.18}
        dec = {k for k in decoys if r.random() < 0.30}
        L = ["name: ci", "on:"]
        if "target_checkout" in truth:
            L.append("  pull_request_target:")
        else:
            L.append("  pull_request:")
        if "permisos" in truth:
            L.append("permissions: write-all")
        else:
            L += ["permissions:", "  contents: read"]
        L += ["jobs:", "  build:", "    runs-on: ubuntu-latest"]
        if "continuar" in truth:
            L.append("    continue-on-error: true")
        L.append("    steps:")
        if "sin_pin" in truth:
            L.append("      - uses: actions/checkout@v4")
        else:
            L.append("      - uses: actions/checkout@" + "".join(r.choice("0123456789abcdef") for _ in range(40)))
        if "target_checkout" in truth:
            L += ["        with:", "          ref: ${{ github.event.pull_request.head.sha }}"]
        if "inyeccion" in truth:
            if r.random() < 0.3:  # variante en bloque de varias líneas
                L += ["      - run: |", '          echo "titulo: ${{ github.event.pull_request.title }}"']
            else:
                L.append('      - run: echo "${{ github.event.pull_request.title }}"')
        if "curl_bash" in truth:
            L.append("      - run: curl -sSL https://example.invalid/i.sh | bash")
        if "eco_secreto" in truth:
            L.append('      - run: echo "token=${{ secrets.DEPLOY_TOKEN }}"')
        if "token_fijo" in truth:
            L.append("      - run: deploy --token ghp_" + "".join(r.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(36)))
        if "comentario_curl" in dec:
            L.append("      # no usar: curl -sSL https://example.invalid/i.sh | bash")
        if "accion_local" in dec:
            L.append("      - uses: ./.github/actions/preparar")
        if "sha_confiable" in dec:
            L.append('      - run: echo "${{ github.sha }}"')
        if "nombre_target" in dec:
            L.append("      - name: evitar pull_request_target")
            L.append("        run: echo ok")
        if "numero_pr" in dec:
            L.append('      - run: echo "${{ github.event.pull_request.number }}"')
        if "rama_literal" in dec:
            L.append('      - run: echo "${{ github.ref_name }}"')
        data.append(("\n".join(L) + "\n", truth))
    return data


import re

RULES_NAIVE = {
    "sin_pin": lambda t: bool(re.search(r"uses:\s*\S+@(?![0-9a-f]{40}\b)", t)),
    "permisos": lambda t: "write-all" in t,
    "target_checkout": lambda t: "pull_request_target" in t,
    "inyeccion": lambda t: "${{" in t and "github." in t,
    "curl_bash": lambda t: bool(re.search(r"curl[^\n]*\|\s*(ba)?sh", t)),
    "eco_secreto": lambda t: bool(re.search(r"echo[^\n]*secrets\.", t)),
    "continuar": lambda t: "continue-on-error: true" in t,
    "token_fijo": lambda t: bool(re.search(r"gh[pousr]_[A-Za-z0-9]{30,}", t)),
}


def _strip_comments(t):
    return "\n".join(l for l in t.splitlines() if not l.lstrip().startswith("#"))


def _rules_refined(raw):
    t = _strip_comments(raw)
    lines = t.splitlines()
    run_lines = [l for l in lines if re.match(r"\s*(- )?run:", l)]
    use_lines = [l for l in lines if re.match(r"\s*- uses:", l)]
    return {
        "sin_pin": any(not re.search(r"@[0-9a-f]{40}\s*$", l) and not re.search(r"uses:\s*\./", l) for l in use_lines),
        "permisos": bool(re.search(r"^permissions:\s*write-all", t, re.M)),
        "target_checkout": bool(re.search(r"^\s*pull_request_target:", t, re.M)) and "head.sha" in t,
        "inyeccion": any(re.search(r"\$\{\{\s*github\.event\.(pull_request|issue|comment|head_commit)[^}]*\}\}", l) for l in run_lines),
        "curl_bash": any(re.search(r"curl[^\n]*\|\s*(ba)?sh", l) for l in run_lines),
        "eco_secreto": any(re.search(r"echo[^\n]*secrets\.", l) for l in run_lines),
        "continuar": bool(re.search(r"^\s*continue-on-error:\s*true", t, re.M)),
        "token_fijo": bool(re.search(r"gh[pousr]_[A-Za-z0-9]{30,}", t)),
    }


def _refined_findings(text: str) -> set:
    return {k for k, v in _rules_refined(text).items() if v}


@lru_cache(None)
def e411_politicas() -> dict:
    data = _make_workflows()
    out = {}
    for label, fn in (("ingenua", lambda t: {k: f(t) for k, f in RULES_NAIVE.items()}), ("afinada", _rules_refined)):
        tp = fp = fn_ = 0
        per = {}
        for text, truth in data:
            found = {k for k, v in fn(text).items() if v}
            tp += len(found & truth)
            fp += len(found - truth)
            fn_ += len(truth - found)
        out[label] = (tp, fp, fn_)
    out["_total_verdaderos"] = sum(len(t) for _, t in data)
    # falsos positivos de la ingenua por regla
    per_rule = {}
    for k, f in RULES_NAIVE.items():
        per_rule[k] = sum(1 for text, truth in data if f(text) and k not in truth)
    out["_fp_regla"] = per_rule
    # hallazgos que ninguna regla de texto ve: dos workflows con el mismo defecto por herencia
    return out


@lru_cache(None)
def e411_reintentos() -> dict:
    r = random.Random(4113)
    tests = 600
    p_flaky = 0.0005
    out = {"rojos_falsos": {}, "defecto": {}}
    for retries in (0, 1, 2):
        out["rojos_falsos"][retries] = 1 - (1 - p_flaky ** (1 + retries)) ** tests  # exacto: un test falla si fallan todos sus intentos
    for m in (0.5, 0.2, 0.05):
        row = {}
        for retries in (0, 1, 2):
            passed = sum(1 for _ in range(40000) if any(r.random() >= m for _ in range(1 + retries)))
            row[retries] = passed / 40000
        out["defecto"][m] = row
    return out


# ------------------------------------------------------------------ SE-412
import base64
import hmac


def _b64(b):
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def _unb64(s):
    return base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))


KEY = b"clave-sintetica-del-experimento"
NOW = 1_800_000_000
ISS = "https://ci.plataforma.example"
AUD = "cloud.plataforma.example"
REPO = "org/entregas-api"
GOOD_SUBS = [f"repo:{REPO}:ref:refs/heads/main", f"repo:{REPO}:environment:produccion", f"repo:{REPO}:ref:refs/tags/v1.4.0"]


def _sign(claims, key=KEY, alg="HS256"):
    h = _b64(json.dumps({"alg": alg, "typ": "JWT"}).encode())
    p = _b64(json.dumps(claims).encode())
    s = _b64(hmac.new(key, f"{h}.{p}".encode(), hashlib.sha256).digest()) if alg != "none" else ""
    return f"{h}.{p}.{s}"


def _claims(**kw):
    c = {"iss": ISS, "aud": AUD, "sub": GOOD_SUBS[0], "iat": NOW - 60, "nbf": NOW - 60, "exp": NOW + 600}
    c.update(kw)
    return c


def verify(token, level):
    try:
        h, p, s = token.split(".")
        head = json.loads(_unb64(h))
        c = json.loads(_unb64(p))
    except Exception:
        return False
    if level >= 1:
        if head.get("alg") != "HS256":
            return False
        good = _b64(hmac.new(KEY, f"{h}.{p}".encode(), hashlib.sha256).digest())
        if not hmac.compare_digest(good, s):
            return False
    if level >= 2:
        if "exp" not in c or c["exp"] <= NOW or c.get("nbf", 0) > NOW + 30:
            return False
    if level >= 3:
        if c.get("iss") != ISS or c.get("aud") != AUD:
            return False
    if level == 4:
        if not str(c.get("sub", "")).startswith("repo:org"):
            return False
    if level >= 5:
        if c.get("sub") not in GOOD_SUBS:
            return False
        if c["exp"] - c.get("iat", 0) > 900:
            return False
    return True


def _mutations():
    out = []
    ops = {
        "expirado": lambda: _sign(_claims(exp=NOW - 10)),
        "sin exp": lambda: _sign({k: v for k, v in _claims().items() if k != "exp"}),
        "audiencia ajena": lambda: _sign(_claims(aud="otra.nube.example")),
        "emisor ajeno": lambda: _sign(_claims(iss="https://ci.otro.example")),
        "firma alterada": lambda: _sign(_claims())[:-4] + "AAAA",
        "alg none": lambda: _sign(_claims(), alg="none"),
        "otro repositorio": lambda: _sign(_claims(sub="repo:org/otro-repo:ref:refs/heads/main")),
        "prefijo parecido": lambda: _sign(_claims(sub=f"repo:org-malicioso/entregas-api:ref:refs/heads/main")),
        "rama de PR": lambda: _sign(_claims(sub=f"repo:{REPO}:pull_request")),
        "vida de 24 h": lambda: _sign(_claims(exp=NOW + 86400)),
        "firmado con otra clave": lambda: _sign(_claims(), key=b"otra-clave"),
        "nbf futuro": lambda: _sign(_claims(nbf=NOW + 3600)),
    }
    for name, fn in ops.items():
        out.append((name, fn()))
    return out


@lru_cache(None)
def e412_tokens() -> dict:
    muts = _mutations()
    legit = [_sign(_claims(sub=s)) for s in GOOD_SUBS]
    rows = {}
    for level, label in ((1, "solo firma"), (2, "firma + vigencia"), (3, "+ emisor y audiencia"), (4, "+ sujeto con prefijo «repo:org»"), (5, "+ sujeto exacto y vida corta")):
        accepted = [name for name, tk in muts if verify(tk, level)]
        legit_ok = sum(verify(t, level) for t in legit)
        rows[label] = (len(accepted), accepted, legit_ok)
    rows["_n"] = len(muts)
    rows["_legit"] = len(legit)
    return rows


@lru_cache(None)
def e412_ventana() -> dict:
    r = random.Random(4122)
    n = 60000
    out = {}
    scenarios = {
        "secreto estático (rotación anual)": (365 * 24.0, 14 * 24.0),
        "secreto estático rotado a 90 días": (90 * 24.0, 14 * 24.0),
        "token de 1 hora": (1.0, 1.0),
        "token de 15 minutos": (0.25, 0.25),
    }
    for label, (life, detect) in scenarios.items():
        exploit = 0
        exposure = 0.0
        for _ in range(n):
            age = r.random() * life  # momento de la fuga dentro de la vida del secreto
            remaining = min(life - age, detect) if life > 1 else life - age
            attacker = r.lognormvariate(math.log(3.0), 1.0)  # horas hasta que alguien lo usa (supuesto)
            exposure += remaining
            exploit += attacker < remaining
        out[label] = (exploit / n, exposure / n)
    return out


def _fake_corpus():
    r = random.Random(4123)
    hexs = "0123456789abcdef"
    alnum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    lines = []
    for _ in range(1200):
        k = r.random()
        if k < 0.20:
            lines.append(("git_sha", "merge de " + "".join(r.choice(hexs) for _ in range(40)), False))
        elif k < 0.34:
            lines.append(("uuid", "request_id=" + "-".join("".join(r.choice(hexs) for _ in range(n)) for n in (8, 4, 4, 4, 12)), False))
        elif k < 0.42:
            lines.append(("base64", "logo=data:image/png;base64," + "".join(r.choice(alnum) for _ in range(60)), False))
        elif k < 0.60:
            lines.append(("texto", "usuario " + r.choice(["ana", "luis", "marta"]) + " entrego la tarea " + str(r.randint(1, 999)), False))
        elif k < 0.72:
            lines.append(("prefijo", "GITHUB_TOKEN=ghp_" + "".join(r.choice(alnum) for _ in range(36)), True))
        elif k < 0.82:
            lines.append(("clave_nube", "aws_key=AKIA" + "".join(r.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ234567") for _ in range(16)), True))
        elif k < 0.88:
            lines.append(("clave_propia", "api_key=" + "".join(r.choice(alnum) for _ in range(32)), True))
        elif k < 0.92:
            lines.append(("clave_baja_entropia", "password=" + r.choice(["admin123", "entrega2024", "cambiame", "colegio"]), True))
        elif k < 0.95:
            lines.append(("bearer", "Authorization: Bearer " + "".join(r.choice(alnum) for _ in range(28)), True))
        elif k < 0.97:
            lines.append(("url_credencial", "DB=postgres://app:" + "".join(r.choice(alnum) for _ in range(14)) + "@db.interno:5432/entregas", True))
        else:
            lines.append(("señuelo_asignacion", r.choice(["token_count=42", "password_reset=enabled", "api_key=PON_AQUI_TU_CLAVE", "secret_santa=desactivado"]), False))
    return lines


def _entropy(s):
    from collections import Counter
    c = Counter(s)
    return -sum(v / len(s) * math.log2(v / len(s)) for v in c.values())


@lru_cache(None)
def e412_escaner() -> dict:
    corpus = _fake_corpus()
    pref = re.compile(r"(ghp_[A-Za-z0-9]{36}|AKIA[A-Z2-7]{16})")
    assign = re.compile(r"(?:key|token|secret|password)\s*=\s*(\S+)", re.I)

    def by_regex(line):
        return bool(pref.search(line))

    def by_entropy(line):
        return any(len(w) >= 20 and _entropy(w) > 3.6 for w in re.findall(r"[A-Za-z0-9+/_\-]{20,}", line))

    def by_assign(line):
        m = assign.search(line)
        return bool(m)

    def by_combo(line):
        if by_regex(line):
            return True
        m = assign.search(line)
        return bool(m) and (by_entropy(line) or True)

    out = {}
    for label, fn in (("prefijos conocidos", by_regex), ("entropía", by_entropy), ("asignación sospechosa", by_assign), ("prefijos + asignación", by_combo)):
        tp = sum(1 for _, l, s in corpus if s and fn(l))
        fp = sum(1 for _, l, s in corpus if not s and fn(l))
        fn_ = sum(1 for _, l, s in corpus if s and not fn(l))
        out[label] = (tp, fp, fn_)
    out["_secretos"] = sum(1 for *_, s in corpus if s)
    out["_lineas"] = len(corpus)
    fp_kind = {}
    for kind, l, s in corpus:
        if not s and by_entropy(l):
            fp_kind[kind] = fp_kind.get(kind, 0) + 1
    out["_fp_entropia"] = fp_kind
    return out


# ------------------------------------------------------------------ SE-413
def _poisson(r, mean):
    if mean <= 0:
        return 0
    if mean > 30:
        return max(0, round(r.gauss(mean, math.sqrt(mean))))
    L = math.exp(-mean)
    k, p = 0, 1.0
    while True:
        p *= r.random()
        if p <= L:
            return k
        k += 1


def _pois_tail(k, mean):
    if k <= 0:
        return 1.0
    s, term = 0.0, math.exp(-mean)
    for i in range(k):
        s += term
        term *= mean / (i + 1)
    return max(0.0, 1.0 - s)


RPS, BASE_ERR = 100, 0.005
STRATS = {
    "todo de una vez": [(1.0, 30)],
    "gradual en 4 tandas": [(0.25, 5), (0.5, 5), (0.75, 5), (1.0, 30)],
    "canario 1 % → 5 % → 25 % → 100 %": [(0.01, 10), (0.05, 10), (0.25, 10), (1.0, 30)],
}


def _run_release(r, strat, excess, alpha=0.001):
    bad = 0.0
    t = 0
    for share, minutes in strat:
        e = n = 0
        for _ in range(minutes):
            reqs = int(RPS * 60 * share)
            err = _poisson(r, reqs * (BASE_ERR + excess))
            e += err
            n += reqs
            bad += max(0.0, err - reqs * BASE_ERR)
            t += 1
            if e >= 3 and _pois_tail(e, n * BASE_ERR) < alpha:
                return bad, t, True
    return bad, t, False


@lru_cache(None)
def e413_despliegue() -> dict:
    r = random.Random(4131)
    out = {}
    for label, strat in STRATS.items():
        harm, det = [], []
        for _ in range(600):
            b, t, d = _run_release(r, strat, 0.04)
            harm.append(b); det.append(t if d else None)
        harm.sort()
        falsos = sum(1 for _ in range(600) if _run_release(r, strat, 0.0)[2])
        detected = [x for x in det if x is not None]
        out[label] = (sum(harm) / len(harm), harm[int(0.95 * len(harm))], sum(detected) / max(1, len(detected)), len(detected) / 600, falsos / 600)
    return out


@lru_cache(None)
def e413_potencia() -> dict:
    out = {}
    alpha = 0.001
    for share in (0.01, 0.05, 0.25):
        n = int(RPS * 60 * 10 * share)  # 10 minutos
        mean0 = n * BASE_ERR
        k = 1
        while _pois_tail(k, mean0) > alpha:
            k += 1
        for excess in (0.005, 0.01, 0.02, 0.04):
            power = _pois_tail(k, n * (BASE_ERR + excess))
            out[f"{share}|{excess}"] = (n, k, power)
    return out


@lru_cache(None)
def e413_banderas() -> dict:
    out = {}
    r = random.Random(4133)
    for n in (2, 4, 6, 8, 10):
        full = 2 ** n
        pairs = [(i, a, j, b) for i in range(n) for j in range(i + 1, n) for a in (0, 1) for b in (0, 1)]
        configs = []
        need = set(pairs)
        cases = [tuple(r.randint(0, 1) for _ in range(n)) for _ in range(200)]
        while need:
            best = max(cases, key=lambda c: sum(1 for (i, a, j, b) in need if c[i] == a and c[j] == b))
            configs.append(best)
            need = {x for x in need if not (best[x[0]] == x[1] and best[x[2]] == x[3])}
            if len(configs) > 60:
                break
        out[n] = (full, len(configs))
    # vida de las banderas
    r = random.Random(4134)
    live_clean, live_never = 0, 0
    for month in range(12):
        live_never += 3
        live_clean += 3
        live_clean = round(live_clean - sum(1 for _ in range(live_clean) if r.random() < 0.25))
    out["_vivas"] = (live_clean, live_never)
    return out


# ------------------------------------------------------------------ SE-414
def _random_graph(r, n=12):
    names = [f"r{i}" for i in range(n)]
    g = {}
    for i, name in enumerate(names):
        deps = [names[j] for j in range(i) if r.random() < 0.25]
        g[name] = {"deps": deps, "props": r.randint(0, 3), "stateful": r.random() < 0.25}
    return g


def _topo(g):
    seen, order = set(), []

    def visit(x, stack=()):
        if x in stack:
            raise ValueError("ciclo")
        if x in seen:
            return
        for d in g[x]["deps"]:
            visit(d, stack + (x,))
        seen.add(x)
        order.append(x)

    for x in g:
        visit(x)
    return order


def _plan(desired, actual):
    acts = []
    for k in desired:
        if k not in actual:
            acts.append(("crear", k))
        elif desired[k]["props"] != actual[k]["props"]:
            acts.append(("reemplazar" if desired[k]["props"] // 2 != actual[k]["props"] // 2 else "actualizar", k))
    for k in actual:
        if k not in desired:
            acts.append(("borrar", k))
    return acts


def _apply(acts, desired, actual, order):
    cloud = {k: dict(v) for k, v in actual.items()}
    fails = 0
    for kind, k in order:
        if kind in ("crear", "reemplazar") and any(d not in cloud for d in desired[k]["deps"]):
            fails += 1
            continue
        if kind == "borrar" and any(k in v["deps"] for n, v in cloud.items() if n != k):
            fails += 1
            continue
        if kind == "borrar":
            del cloud[k]
        else:
            cloud[k] = {"deps": desired[k]["deps"], "props": desired[k]["props"], "stateful": desired[k]["stateful"]}
    return cloud, fails


@lru_cache(None)
def e414_plan() -> dict:
    r = random.Random(4141)
    random_fail = topo_fail = 0
    runs = 300
    destructive = replaced_stateful = total_acts = idempotent = 0
    for _ in range(runs):
        desired = _random_graph(r)
        actual = {k: dict(v) for k, v in desired.items() if r.random() < 0.55}
        # el estado real tiene dependencias propias: las dependencias de lo existente deben existir
        for k in list(actual):
            actual[k]["deps"] = [d for d in actual[k]["deps"] if d in actual]
        for k in actual:
            if r.random() < 0.3:
                actual[k]["props"] = (actual[k]["props"] + 1) % 4
        extra = f"huerfano{r.randint(0, 99)}"
        if r.random() < 0.4:
            actual[extra] = {"deps": [], "props": 0, "stateful": r.random() < 0.5}
        acts = _plan(desired, actual)
        total_acts += len(acts)
        order_topo = _topo(desired)
        topo_order = [a for k in order_topo for a in acts if a[1] == k and a[0] != "borrar"]
        topo_order += [a for a in acts if a[0] == "borrar"]
        shuffled = acts[:]
        r.shuffle(shuffled)
        _, f1 = _apply(acts, desired, actual, shuffled)
        cloud, f2 = _apply(acts, desired, actual, topo_order)
        random_fail += f1 > 0
        topo_fail += f2 > 0
        for kind, k in acts:
            if kind == "borrar" or kind == "reemplazar":
                destructive += 1
                st = (actual.get(k) or desired.get(k))["stateful"]
                replaced_stateful += bool(st)
        if f2 == 0:
            idempotent += not _plan({k: v for k, v in desired.items()}, cloud)
    cyc = 0
    for _ in range(100):
        g = _random_graph(r)
        g["r0"]["deps"].append("r11")
        g["r11"]["deps"].append("r0")
        try:
            _topo(g)
        except ValueError:
            cyc += 1
    return {"runs": runs, "aleatorio_falla": random_fail / runs, "topologico_falla": topo_fail / runs, "acciones": total_acts / runs,
            "destructivas": destructive / runs, "con_estado": replaced_stateful / runs, "idempotente": idempotent, "ciclos": cyc}


@lru_cache(None)
def e414_estado() -> dict:
    steps = ["leer", "aplicar", "escribir"]
    results = {}
    for n in (2, 3):
        labels = [f"P{i}" for i in range(n)]
        events = [(i, s) for i in range(n) for s in steps]

        def interleavings():
            def rec(pos, acc):
                if all(p == 3 for p in pos):
                    yield acc
                    return
                for i in range(n):
                    if pos[i] < 3:
                        npos = list(pos)
                        npos[i] += 1
                        yield from rec(tuple(npos), acc + [(i, steps[pos[i]])])
            return rec(tuple([0] * n), [])

        total = bad = 0
        for order in interleavings():
            cloud = set()
            state = set()
            local = {}
            for i, s in order:
                if s == "leer":
                    local[i] = set(state)
                elif s == "aplicar":
                    cloud.add(f"recurso{i}")
                    local[i] = local[i] | {f"recurso{i}"}
                else:
                    state = set(local[i])
            total += 1
            bad += state != cloud
        results[n] = (total, bad)
    return results


@lru_cache(None)
def e414_deriva() -> dict:
    r = random.Random(4143)
    events = 5000
    out = {}
    for label, kind, T in (("plan cada hora", "per", 1.0), ("plan cada 6 horas", "per", 6.0), ("plan diario", "per", 24.0), ("plan semanal", "per", 168.0), ("solo al fusionar (3 por semana)", "merge", 168 / 3)):
        waits = []
        for _ in range(events):
            if kind == "per":
                waits.append(r.random() * T)
            else:
                waits.append(r.expovariate(1 / T))
        waits.sort()
        out[label] = (sum(waits) / events, waits[int(0.95 * events)])
    out["_auto_revierte"] = 0.2
    return out


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    for fn in (e409_ramas, e409_lotes, e409_cola, e410_dag, e410_matriz, e410_cache, e411_orden, e411_politicas, e411_reintentos,
               e412_tokens, e412_ventana, e412_escaner, e413_despliegue, e413_potencia, e413_banderas, e414_plan, e414_estado, e414_deriva):
        print(json.dumps({fn.__name__: fn()}, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
