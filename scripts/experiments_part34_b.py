"""Experimentos de SE-415 a SE-420 (datos sintéticos, semilla fija, solo biblioteca estándar).

Uso: python scripts/experiments_part34_b.py   (imprime una línea JSON por experimento)
"""
from __future__ import annotations

import hashlib
import hmac
import itertools
import json
import math
import random
import sqlite3
import subprocess
import sys
from functools import lru_cache

from experiments_part34_a import _refined_findings  # noqa: E402  (verificador de SE-411 reutilizado en SE-419)


# ------------------------------------------------------------------ SE-415
@lru_cache(None)
def e415_bucle() -> dict:
    r = random.Random(4151)
    drifts = 6000
    apps = 200
    out = {}
    for label, interval in (("cada 30 s", 30), ("cada 3 min", 180), ("cada 15 min", 900), ("cada hora", 3600)):
        # una deriva manual ocurre en un instante aleatorio y espera al siguiente ciclo de reconciliación
        waits = sorted(r.random() * interval for _ in range(drifts))
        # lecturas del repositorio y del clúster por día para 200 aplicaciones (una lectura de cada lado por ciclo)
        calls = 2 * 86400 / interval * apps
        out[label] = (sum(waits) / drifts, waits[int(0.95 * drifts)], calls, interval / 2)
    out["_aviso_segundos"] = 2
    return out


@lru_cache(None)
def e415_pelea() -> dict:
    r = random.Random(4152)
    minutes = 24 * 60
    capacity = 100  # solicitudes por réplica
    load = [max(20, 650 + 500 * math.sin(2 * math.pi * (t - 300) / 1440) + r.gauss(0, 40)) for t in range(minutes)]
    out = {}
    for label, ignore in (("el repositorio fija réplicas = 3", False), ("el repositorio ignora el campo de réplicas", True)):
        replicas = 3
        short = scale = resets = 0
        for t in range(minutes):
            want = math.ceil(load[t] / capacity)
            if want != replicas:
                replicas = want
                scale += 1
            if not ignore and t % 3 == 2 and replicas != 3:
                replicas = 3
                resets += 1
            short += replicas * capacity < load[t]
        out[label] = (short, scale, resets)
    return out


@lru_cache(None)
def e415_poda() -> dict:
    r = random.Random(4153)
    out = {}
    for label, prune, protect in (("sin poda", False, False), ("con poda", True, False), ("con poda y protección de recursos con estado", True, True)):
        deleted = stateful = events = 0
        for _ in range(4000):
            manifests = [("estado" if r.random() < 0.15 else "sin estado") for _ in range(40)]
            if r.random() < 0.25:  # una refactorización renombra o mueve k manifiestos: para el controlador es «borrar y crear»
                moved = r.sample(range(40), r.choice([1, 2, 3]))
                events += 1
                for i in moved:
                    if prune:
                        if protect and manifests[i] == "estado":
                            continue
                        deleted += 1
                        stateful += manifests[i] == "estado"
        out[label] = (deleted / events, stateful / events, events)
    return out


# ------------------------------------------------------------------ SE-416
@lru_cache(None)
def e416_reidentificacion() -> dict:
    r = random.Random(4161)
    n = 6000
    zips = [f"{8000 + i * 37:05d}" for i in range(30)]
    zip_w = [1 / (i + 1) ** 0.7 for i in range(30)]
    people = []
    for i in range(n):
        people.append({
            "id": i,
            "nombre": f"estudiante-{i}",
            "nac": 1998 * 366 + r.randrange(0, 11 * 366),  # día de nacimiento sintético en un rango de 11 años
            "cp": r.choices(zips, zip_w)[0],
            "gen": r.choice("FMX"),
            "nota": round(r.gauss(5.2, 1.1), 1),
        })
    external = [p for p in people if r.random() < 0.7]

    def key(p, mode):
        if mode == "completo":
            return (p["nac"], p["cp"], p["gen"])
        if mode == "anio_cp":
            return (p["nac"] // 366, p["cp"], p["gen"])
        if mode == "generalizado":
            return (p["nac"] // 366, p["cp"][:3], p["gen"])
        return (p["nac"] // 366 // 2, p["cp"][:2], "*")

    def key2(p):
        return (p["nac"] // 366, p["cp"], p["gen"])

    out = {}
    for mode, label in (("completo", "fecha, código postal y género (sin nombre)"), ("anio_cp", "año de nacimiento, código postal y género"), ("generalizado", "año de nacimiento, 3 dígitos postales y género"), ("grueso", "bienio, 2 dígitos postales, sin género")):
        from collections import Counter
        counts = Counter(key(p, mode) for p in people)
        unique = sum(1 for p in people if counts[key(p, mode)] == 1)
        ext_counts = Counter(key(p, mode) for p in external)
        # ataque de vinculación: la persona externa conocida se vincula si su clave es única entre las externas y existe en la base
        reident = sum(1 for p in external if ext_counts[key(p, mode)] == 1 and counts[key(p, mode)] == 1)
        small = sum(1 for p in people if counts[key(p, mode)] < 5)
        out[label] = (unique / n, reident / len(external), small / n, len(counts))
    return out


@lru_cache(None)
def e416_uniones() -> dict:
    r = random.Random(4162)
    students = list(range(3000))
    subs = [r.choice(students) for _ in range(15000)]
    grades = {s: r.gauss(5.2, 1.1) for s in students}
    salt = b"sal-sintetica"
    rows = {}
    # 1. aleatorio por tabla: cada tabla recibe su propia permutación
    perm_a = {s: f"x{r.random():.9f}" for s in students}
    perm_b = {s: f"x{r.random():.9f}" for s in students}
    ok = sum(1 for s in subs if perm_b[s] == perm_a[s])
    rows["aleatorio por tabla"] = ok / len(subs)
    # 2. determinista con HMAC
    det = lambda s: hmac.new(salt, str(s).encode(), hashlib.sha256).hexdigest()[:16]
    rows["determinista (HMAC con sal)"] = sum(1 for s in subs if det(s) == det(s)) / len(subs)
    # 3. sin enmascarar
    rows["sin enmascarar"] = 1.0
    # distribución de notas
    vals = list(grades.values())
    mean = sum(vals) / len(vals)
    sd = math.sqrt(sum((v - mean) ** 2 for v in vals) / len(vals))
    shuffled = vals[:]
    r.shuffle(shuffled)
    noisy = [v + r.gauss(0, 1.0) for v in vals]
    mn = sum(noisy) / len(noisy)
    sdn = math.sqrt(sum((v - mn) ** 2 for v in noisy) / len(noisy))
    corr = lambda a, b: sum((x - sum(a) / len(a)) * (y - sum(b) / len(b)) for x, y in zip(a, b)) / (len(a) * (sum((x - sum(a) / len(a)) ** 2 for x in a) / len(a)) ** 0.5 * (sum((y - sum(b) / len(b)) ** 2 for y in b) / len(b)) ** 0.5)
    rows["_notas"] = {"original": (mean, sd), "ruido": (mn, sdn, corr(vals, noisy)), "permutación": (sum(shuffled) / len(shuffled), sd, corr(vals, shuffled))}
    return rows


@lru_cache(None)
def e416_previews() -> dict:
    r = random.Random(4163)
    days = 60
    end = days * 24
    prs = []
    for d in range(days):
        for _ in range(8):  # PR por día (supuesto del autor)
            start = d * 24 + r.random() * 24
            abandoned = r.random() < 0.15
            life = r.lognormvariate(math.log(48), 0.9)  # horas de actividad del PR
            pushes, t = [], start
            while True:
                t += r.expovariate(1 / 14.0)  # un push cada 14 h de media mientras el PR está activo
                if t >= start + life:
                    break
                pushes.append(t)
            closed = None if abandoned else start + life
            prs.append((start, closed, pushes))

    def alive(policy, start, closed, pushes):
        stop = min(end, closed) if closed is not None else end
        if policy == "cierre":
            return stop - start, 0, closed is None
        ttl = 72 if policy == "ttl72" else 24
        hours = recreated = 0
        expiry = start + ttl
        last = start
        cur_start = start
        for p in pushes:
            if p >= stop:
                break
            if p >= expiry:  # el entorno ya no existía cuando llegó el push
                hours += min(expiry, stop) - cur_start
                cur_start = p
                recreated += 1
                expiry = p + ttl
            elif policy == "ttl24":
                expiry = max(expiry, p + ttl)
        hours += min(expiry, stop) - cur_start
        return hours, recreated, False

    out = {}
    for label, pol in (("solo se destruye al cerrar el PR", "cierre"), ("TTL de 72 h desde la creación", "ttl72"), ("TTL de 24 h renovado con cada push", "ttl24")):
        h = rec = orph = 0
        for pr in prs:
            hh, rr, oo = alive(pol, *pr)
            h += hh; rec += rr; orph += oo
        out[label] = (h, rec, orph)
    out["_prs"] = len(prs)
    return out


# ------------------------------------------------------------------ SE-417
@lru_cache(None)
def e417_adopcion() -> dict:
    r = random.Random(4171)
    out = {}
    teams = 400
    caps = 6
    for covered in (3, 4, 6):
        row = {}
        for setup in (4, 20, 60):
            adopt = partial = 0
            for _ in range(teams):
                need = [r.random() < 0.7 for _ in range(caps)]
                gap = sum(1 for i, nd in enumerate(need) if nd and i >= covered)
                custom = r.lognormvariate(math.log(40), 0.5)  # horas para construirlo por su cuenta
                path_cost = setup + gap * 25  # cada capacidad que falta se improvisa
                if path_cost < custom:
                    adopt += 1
                    partial += gap > 0
            row[setup] = (adopt / teams, partial / max(1, adopt))
        out[covered] = row
    return out


@lru_cache(None)
def e417_catalogo() -> dict:
    r = random.Random(4172)
    teams = {f"equipo-{i}" for i in range(14)}
    entries = []
    for i in range(150):
        e = {"nombre": f"servicio-{i}", "owner": r.choice(sorted(teams)), "runbook": f"https://wiki.interna.example/{i}", "oncall": f"rotacion-{i % 14}", "revision": r.randint(0, 400), "truth": set()}
        if r.random() < 0.10:
            e["owner"] = ""; e["truth"].add("sin dueño")
        elif r.random() < 0.10:
            e["owner"] = "equipo-disuelto"; e["truth"].add("dueño inexistente")
        if r.random() < 0.14:
            e["runbook"] = r.choice(["TBD", "-", "pendiente"]); e["truth"].add("runbook de relleno")
        if e["revision"] > 180:
            e["truth"].add("revisión vencida")
        entries.append(e)
    def present(e):
        return bool(e["owner"]) and bool(e["runbook"]) and bool(e["oncall"])
    def reg(e):
        return e["owner"] in teams
    def real(e):
        return e["runbook"].startswith("https://")
    def fresh(e):
        return e["revision"] <= 180
    levels = {
        "campos presentes": lambda e: present(e),
        "+ dueño existe en el registro de equipos": lambda e: present(e) and reg(e),
        "+ enlace con forma de URL (no relleno)": lambda e: present(e) and reg(e) and real(e),
        "+ revisado en los últimos 180 días": lambda e: present(e) and reg(e) and real(e) and fresh(e),
    }
    out = {name: sum(1 for e in entries if fn(e)) for name, fn in levels.items()}
    out["_con_problema"] = sum(1 for e in entries if e["truth"])
    out["_total"] = len(entries)
    return out


@lru_cache(None)
def e417_cola() -> dict:
    out = {}
    for lam in (0.2, 0.4, 0.55):  # solicitudes por hora
        r = random.Random(41730 + int(lam * 100))
        servers = [0.0, 0.0]  # dos personas de plataforma
        t = 0.0
        waits = []
        for _ in range(8000):
            t += r.expovariate(lam)
            servers.sort()
            start = max(t, servers[0])
            waits.append(start - t)
            servers[0] = start + r.expovariate(1 / 3.0)  # 3 horas por solicitud (supuesto)
        waits.sort()
        out[lam] = (lam * 3.0 / 2, sum(waits) / len(waits), waits[int(0.9 * len(waits))])
    return out


# ------------------------------------------------------------------ SE-418
@lru_cache(None)
def e418_definiciones() -> dict:
    r = random.Random(4181)
    services = 6
    weeks = 52
    events = []
    for s in range(services):
        rate = [1, 2, 3, 5, 8, 2][s]  # despliegues por semana
        t = 0.0
        while t < weeks * 168:
            t += r.expovariate(rate / 168)
            if t >= weeks * 168:
                break
            first = t - r.lognormvariate(math.log(30), 0.8)  # primer commit del cambio (horas antes)
            pr_open = first + r.uniform(1, 6)
            merge = t - r.lognormvariate(math.log(5), 0.8)
            merge = max(merge, pr_open)
            fail = r.random() < 0.12
            rollback = fail and r.random() < 0.6
            events.append({"s": s, "dep": t, "first": first, "pr": pr_open, "merge": merge, "fail": fail, "rollback": rollback,
                           "restore": r.lognormvariate(math.log(0.75), 0.9) if fail else 0.0})
    def med(x):
        x = sorted(x); return x[len(x) // 2]
    def p90(x):
        x = sorted(x); return x[int(0.9 * len(x))]
    out = {"_n": len(events)}
    out["frecuencia"] = {"por servicio y semana (media)": len(events) / services / weeks,
                          "del conjunto por semana": len(events) / weeks,
                          "solo producción de los dos servicios mayores": sum(1 for e in events if e["s"] in (3, 4)) / weeks}
    out["plazo"] = {"desde el primer commit (mediana)": med([e["dep"] - e["first"] for e in events]),
                    "desde que se abre el PR (mediana)": med([e["dep"] - e["pr"] for e in events]),
                    "desde la fusión (mediana)": med([e["dep"] - e["merge"] for e in events]),
                    "desde el primer commit (p90)": p90([e["dep"] - e["first"] for e in events])}
    out["fallos"] = {"fallos con incidente": sum(e["fail"] for e in events) / len(events),
                     "solo los que se revierten": sum(e["rollback"] for e in events) / len(events)}
    fails = [e["restore"] for e in events if e["fail"]]
    out["restauracion"] = {"mediana (h)": med(fails), "media (h)": sum(fails) / len(fails)}
    return out


@lru_cache(None)
def e418_gaming() -> dict:
    weeks = 26
    base = random.Random(4182)
    defects_week = [sum(1 for _ in range(10) if base.random() < 0.12) for _ in range(weeks)]  # defectos por semana, iguales en los tres casos
    out = {}
    for label, noop, parts in (("sin incentivo", 0, 1), ("incentivo en frecuencia: despliegues vacíos", 12, 1), ("incentivo en frecuencia: cambios partidos", 0, 3)):
        r = random.Random(41821)
        deploys = fails = 0
        lead = []
        for d in defects_week:
            n = 10 * parts if parts > 1 else 4
            deploys += n + noop
            fails += min(d, n)
            lead += [r.lognormvariate(math.log(8 if parts > 1 else 30), 0.5) for _ in range(n)] + [0.1] * noop
        lead.sort()
        out[label] = (deploys / weeks, fails / deploys, lead[len(lead) // 2], sum(defects_week) / weeks, 10.0)
    return out


@lru_cache(None)
def e418_ruido() -> dict:
    r = random.Random(4183)
    out = {}
    trials = 6000
    for n in (8, 30, 100):
        diffs = lose = detect = 0
        for _ in range(trials):
            a = sum(r.random() < 0.12 for _ in range(n)) / n
            b = sum(r.random() < 0.12 for _ in range(n)) / n
            diffs += abs(a - b) >= 0.05
            c = sum(r.random() < 0.08 for _ in range(n)) / n  # mejora real de 12 % a 8 %
            detect += c < a
            lose += c >= a
        z = 1.96
        p = 0.12
        half = z * math.sqrt(p * (1 - p) / n)
        out[n] = (diffs / trials, detect / trials, half)
    return out


# ------------------------------------------------------------------ SE-419
VULNERABLE = """name: ci
on:
  pull_request_target:
permissions: write-all
jobs:
  build:
    runs-on: ubuntu-latest
    continue-on-error: true
    steps:
      - uses: actions/checkout@v4
        with:
          ref: ${{ github.event.pull_request.head.sha }}
      - run: echo "${{ github.event.pull_request.title }}"
      - run: curl -sSL https://example.invalid/i.sh | bash
      - run: echo "token=${{ secrets.DEPLOY_TOKEN }}"
      - run: deploy --token ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
"""


def _fix_steps():
    sha = "0123456789abcdef0123456789abcdef01234567"
    return [
        ("fijar la acción a un SHA", lambda t: t.replace("actions/checkout@v4", f"actions/checkout@{sha}")),
        ("permisos mínimos", lambda t: t.replace("permissions: write-all", "permissions:\n  contents: read")),
        ("pull_request en lugar de pull_request_target", lambda t: t.replace("pull_request_target:", "pull_request:")),
        ("título por variable de entorno", lambda t: t.replace('      - run: echo "${{ github.event.pull_request.title }}"', '      - run: echo "$TITULO"\n        env:\n          TITULO: ${{ github.event.pull_request.title }}')),
        ("ejecutar un script versionado, no uno descargado", lambda t: t.replace("curl -sSL https://example.invalid/i.sh | bash", "bash ./scripts/instalar.sh")),
        ("no escribir el secreto en el registro", lambda t: t.replace('      - run: echo "token=${{ secrets.DEPLOY_TOKEN }}"\n', "")),
        ("el trabajo falla cuando falla", lambda t: t.replace("    continue-on-error: true\n", "")),
        ("sin credencial en el texto", lambda t: t.replace("deploy --token ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", "deploy")),
    ]


@lru_cache(None)
def e419_endurecer() -> dict:
    t = VULNERABLE
    rows = [("original", len(_refined_findings(t)), sorted(_refined_findings(t)))]
    for name, fn in _fix_steps():
        t = fn(t)
        f = _refined_findings(t)
        rows.append((name, len(f), sorted(f)))
    return {"pasos": rows, "final": t}


@lru_cache(None)
def e419_inyeccion() -> dict:
    payloads = [
        'x"); print("INYECTADO',
        'x"); import os; print("INYECTADO", os.name)#',
        "x\\\"); print('INYECTADO",
        'a" + str(7*7) + "b',
        'ok',
        'título normal con «tildes» y comillas \'simples\'',
    ]
    rows = []
    for p in payloads:
        template = 'print("titulo: {{TITULO}}")'
        code = template.replace("{{TITULO}}", p)  # expansión previa: el texto pasa a ser código
        res1 = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, encoding="utf-8", timeout=20, env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
        code2 = 'import os; print("titulo: " + os.environ["TITULO"])'
        res2 = subprocess.run([sys.executable, "-c", code2], capture_output=True, text=True, encoding="utf-8", timeout=20, env={**__import__("os").environ, "TITULO": p, "PYTHONIOENCODING": "utf-8"})
        ejecutado = "INYECTADO" in res1.stdout or "49" in res1.stdout
        rows.append((p, "ejecuta" if ejecutado else ("rompe" if res1.returncode != 0 else "inerte"), res2.returncode == 0 and res2.stdout.strip() == "titulo: " + p))
    return {"filas": rows, "ejecuta": sum(1 for _, a, _ in rows if a == "ejecuta"), "rompe": sum(1 for _, a, _ in rows if a == "rompe"), "seguro": sum(1 for *_, c in rows if c)}


@lru_cache(None)
def e419_pin() -> dict:
    # una acción de terceros representada por un árbol de archivos; la etiqueta apunta a un commit que se puede mover
    def tree_hash(files):
        h = hashlib.sha256()
        for k in sorted(files):
            h.update(k.encode()); h.update(b"\0"); h.update(files[k].encode()); h.update(b"\0")
        return h.hexdigest()
    v1 = {"action.yml": "runs: node20", "dist/index.js": "console.log('compilar')"}
    v1_evil = {"action.yml": "runs: node20", "dist/index.js": "console.log('compilar'); exfiltrar(process.env)"}
    tags = {"v1": tree_hash(v1)}
    pinned = tree_hash(v1)
    result = {"antes": (tags["v1"] == pinned, tags["v1"] == tree_hash(v1))}
    tags["v1"] = tree_hash(v1_evil)  # alguien mueve la etiqueta
    result["despues"] = (tags["v1"] == pinned, tree_hash(v1_evil) == pinned)
    result["etiqueta_cambio"] = tags["v1"] != pinned
    return result


SCOPES = ["actions", "artifact-metadata", "attestations", "checks", "code-quality", "contents", "copilot-requests", "deployments", "id-token", "issues", "discussions", "packages", "pages", "pull-requests", "security-events", "statuses"]  # 16 de los 17 permisos de la página admiten escritura (vulnerability-alerts solo lectura)


@lru_cache(None)
def e419_permisos() -> dict:
    needs = {"lint": {"contents": "read"}, "test": {"contents": "read"}, "build": {"contents": "read", "packages": "write"},
             "publicar": {"contents": "read", "packages": "write", "attestations": "write", "id-token": "write"},
             "desplegar": {"contents": "read", "id-token": "write", "deployments": "write"}}
    write_all = {j: len(SCOPES) for j in needs}
    least = {j: sum(1 for v in n.values() if v == "write") for j, n in needs.items()}
    return {"write-all": write_all, "mínimo": least, "ambitos": len(SCOPES)}


# ------------------------------------------------------------------ SE-420
@lru_cache(None)
def e420_rollback() -> dict:
    def run(variant):
        db = sqlite3.connect(":memory:")
        db.execute("CREATE TABLE alumnos (id INTEGER PRIMARY KEY, name TEXT)")
        for i in range(5):
            db.execute("INSERT INTO alumnos (id, name) VALUES (?, ?)", (i, f"alumno-{i}"))
        # despliegue de v2 con su migración
        if variant == "renombrar de golpe":
            db.execute("ALTER TABLE alumnos RENAME COLUMN name TO full_name")
            for i in range(5, 10):
                db.execute("INSERT INTO alumnos (id, full_name) VALUES (?, ?)", (i, f"alumno-{i}"))
        else:
            db.execute("ALTER TABLE alumnos ADD COLUMN full_name TEXT")
            db.execute("UPDATE alumnos SET full_name = name")
            for i in range(5, 10):
                if variant == "expandir sin doble escritura":
                    db.execute("INSERT INTO alumnos (id, full_name) VALUES (?, ?)", (i, f"alumno-{i}"))
                else:
                    db.execute("INSERT INTO alumnos (id, name, full_name) VALUES (?, ?, ?)", (i, f"alumno-{i}", f"alumno-{i}"))
            if variant == "contraer antes de tiempo":
                db.execute("ALTER TABLE alumnos DROP COLUMN name")
        # retroceso: vuelve v1, que solo conoce la columna «name»
        errores = nulos = bien = 0
        for i in range(10):
            try:
                v = db.execute("SELECT name FROM alumnos WHERE id = ?", (i,)).fetchone()[0]
                if v is None:
                    nulos += 1
                else:
                    bien += 1
            except sqlite3.OperationalError:
                errores += 1
        return errores, nulos, bien
    out = {}
    for v in ("renombrar de golpe", "expandir sin doble escritura", "expandir con doble escritura", "contraer antes de tiempo"):
        out[v] = run(v)
    out["_sqlite"] = sqlite3.sqlite_version
    return out


GATES = ["revisión y lint", "pruebas unitarias", "pruebas de integración", "escaneo de dependencias y secretos", "política sobre el plan de infraestructura", "humo en preproducción", "canario con métricas", "alerta en producción"]
COST = [1, 2, 4, 6, 5, 10, 25, 100]  # daño relativo si se detecta ahí (supuesto del autor)
FAULTS = {
    "error de sintaxis": {0, 1},
    "regresión lógica en una función": {1, 2},
    "contrato roto con otro servicio": {2, 5},
    "dependencia con vulnerabilidad conocida": {3},
    "secreto en el repositorio": {3},
    "permiso excesivo en infraestructura": {4},
    "migración incompatible con la versión anterior": {5, 6},
    "fuga de memoria bajo carga": {6, 7},
    "bandera mal configurada en producción": {6, 7},
    "fallo solo con tráfico real": {6, 7},
    "certificado a punto de vencer": {7},
    "deriva manual en un recurso": {4, 7},
}


@lru_cache(None)
def e420_ablacion() -> dict:
    def first(f, removed=None):
        gs = sorted(g for g in FAULTS[f] if g != removed)
        return gs[0] if gs else None
    base = {f: first(f) for f in FAULTS}
    out = {"_base_coste": sum(COST[g] for g in base.values())}
    for gi, g in enumerate(GATES):
        later = escape = 0
        cost = 0
        for f in FAULTS:
            nf = first(f, gi)
            if nf is None:
                escape += 1
                cost += 300
            else:
                cost += COST[nf]
                later += nf != base[f]
        out[g] = (later, escape, cost)
    out["_sin_deteccion_antes_de_produccion"] = sum(1 for f in FAULTS if first(f) == 7)
    return out


FIELDS = ["run_id", "commit", "digest", "plan_hash", "aprobador", "autor", "ensayo_fecha", "ensayo_entorno", "ensayo_segundos", "canario_solicitudes", "sbom_hash"]


def _package(r, i):
    h = lambda: "".join(r.choice("0123456789abcdef") for _ in range(40))
    return {"run_id": f"run-{1000 + i}", "commit": h(), "digest": "sha256:" + h() + h()[:24], "plan_hash": h(), "aprobador": "ana", "autor": "luis",
            "ensayo_fecha": 20 + i % 10, "ensayo_entorno": "preproduccion", "ensayo_segundos": 140 + i, "canario_solicitudes": 5000 + 10 * i, "sbom_hash": h(),
            "deploy_digest": None, "deploy_commit": None}


def _validate(pk, level):
    f = []
    for k in FIELDS:
        if pk.get(k) in (None, ""):
            f.append("falta " + k)
    if not str(pk.get("digest", "")).startswith("sha256:"):
        f.append("digest sin prefijo")
    if len(str(pk.get("commit", ""))) != 40:
        f.append("commit corto")
    if level >= 2:
        if pk.get("deploy_digest") != pk.get("digest"):
            f.append("el digest desplegado no es el construido")
        if pk.get("deploy_commit") != pk.get("commit"):
            f.append("el commit desplegado no es el probado")
        if pk.get("aprobador") == pk.get("autor"):
            f.append("aprobó su autor")
        if pk.get("hoy", 30) - pk.get("ensayo_fecha", 0) > 30:
            f.append("ensayo caducado")
    if level >= 3:
        if pk.get("ensayo_segundos", 0) < 30:
            f.append("duración del ensayo inverosímil")
        if pk.get("ensayo_entorno") not in ("preproduccion", "sombra"):
            f.append("entorno de ensayo no permitido")
        if pk.get("canario_solicitudes", 0) < 1000:
            f.append("canario sin tráfico suficiente")
    return f


@lru_cache(None)
def e420_paquete() -> dict:
    r = random.Random(4203)
    ops = {
        "quitar un campo": ("forma", lambda p: p.pop("sbom_hash")),
        "commit abreviado": ("forma", lambda p: p.update(commit=p["commit"][:7])),
        "digest sin algoritmo": ("forma", lambda p: p.update(digest=p["digest"].split(":")[1])),
        "digest desplegado distinto": ("cruce", lambda p: p.update(deploy_digest="sha256:" + "0" * 64)),
        "commit desplegado distinto": ("cruce", lambda p: p.update(deploy_commit="f" * 40)),
        "aprobó el propio autor": ("cruce", lambda p: p.update(aprobador="luis")),
        "ensayo de hace 90 días": ("cruce", lambda p: p.update(ensayo_fecha=-60)),
        "ensayo de 0 segundos": ("verosimilitud", lambda p: p.update(ensayo_segundos=0)),
        "ensayo en el entorno equivocado": ("verosimilitud", lambda p: p.update(ensayo_entorno="mi-portatil")),
        "canario con 12 solicitudes": ("verosimilitud", lambda p: p.update(canario_solicitudes=12)),
        "ensayo copiado de otra versión": ("juicio", lambda p: p.update(ensayo_segundos=p["ensayo_segundos"] + 1)),
        "aprobador sin permisos reales": ("juicio", lambda p: p.update(aprobador="bot-sin-revision")),
    }
    n = 10
    res = {name: {1: 0, 2: 0, 3: 0} for name in ops}
    ok = {1: 0, 2: 0, 3: 0}
    for i in range(n):
        base = _package(r, i)
        base["deploy_digest"] = base["digest"]; base["deploy_commit"] = base["commit"]
        for level in (1, 2, 3):
            ok[level] += not _validate(base, level)
        for name, (kind, fn) in ops.items():
            pk = dict(base)
            fn(pk)
            for level in (1, 2, 3):
                res[name][level] += bool(_validate(pk, level))
    return {"ops": {k: (ops[k][0], v[1], v[2], v[3]) for k, v in res.items()}, "n": n, "limpios": ok, "total": n * len(ops)}


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    for fn in (e415_bucle, e415_pelea, e415_poda, e416_reidentificacion, e416_uniones, e416_previews, e417_adopcion, e417_catalogo, e417_cola,
               e418_definiciones, e418_gaming, e418_ruido, e419_endurecer, e419_inyeccion, e419_pin, e419_permisos, e420_rollback, e420_ablacion, e420_paquete):
        print(json.dumps({fn.__name__: fn()}, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
