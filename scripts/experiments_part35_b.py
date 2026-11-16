"""Experimentos sintéticos y sondas reales de las clases SE-427 a SE-432 (guardias, incidentes, recuperación).

Biblioteca estándar, semillas fijas y tiempo virtual. Los incidentes, las personas y los sistemas son
construcciones del autor. La única medición real es la de SE-430 (copias de SQLite en un directorio
temporal) y las sondas de plataforma de SE-432. ``python scripts/experiments_part35_b.py`` imprime JSON.
"""
from __future__ import annotations

import hashlib
import json
from functools import cache
import math
import os
import random
import sqlite3
import sys
import tempfile
from datetime import date, timedelta
from pathlib import Path

TODAY = date(2026, 11, 15)


def pct(values: list[float], q: float) -> float:
    ordered = sorted(values)
    return ordered[min(len(ordered) - 1, max(0, math.ceil(q / 100 * len(ordered)) - 1))]


def poisson(rng: random.Random, lam: float) -> int:
    if lam > 30:
        return max(0, round(rng.gauss(lam, math.sqrt(lam))))
    limit, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= limit:
            return k
        k += 1


# ---------------------------------------------------------------- SE-427
@cache
def e427_guardia(seed: int = 427) -> dict:
    rng = random.Random(seed)
    rate_day, night_share, absent_weeks = 1.5, 0.35, 4
    out = []
    for n in (2, 3, 4, 6, 8):
        weeks_on, night_pages, nights_hit = [], [], []
        years = 300
        for _ in range(years):
            absent = {p: set(rng.sample(range(52), absent_weeks)) for p in range(n)}
            load, pages, hit = [0] * n, [0] * n, [0] * n
            for w in range(52):
                order = [(w + k) % n for k in range(n)]
                person = next((p for p in order if w not in absent[p]), order[0])
                load[person] += 1
                for _night in range(7):
                    k = poisson(rng, rate_day * night_share)
                    pages[person] += k
                    hit[person] += k > 0
            top = load.index(max(load))
            weeks_on.append(load[top])
            night_pages.append(pages[top])
            nights_hit.append(hit[top])
        out.append({"personas": n, "semanas de guardia de la persona más cargada": round(sum(weeks_on) / years, 1),
                    "noches interrumpidas": round(sum(nights_hit) / years), "páginas nocturnas": round(sum(night_pages) / years)})
    return {"páginas por día": rate_day, "parte nocturna": night_share, "filas": out,
            "probabilidad de noche con página": round(1 - math.exp(-rate_day * night_share), 3)}


@cache
def e427_escalamiento(seed: int = 4271, pages: int = 20000) -> dict:
    rng = random.Random(seed)
    out = []
    for label, corr in (("fallos independientes", 0.0), ("30 % comparten causa (misma zona sin red)", 0.3)):
        solo = chain = 0
        times = []
        for _ in range(pages):
            shared_fail = rng.random() < corr
            t = None
            for level, (p, delay) in enumerate(((0.85, 0), (0.85, 5), (0.90, 10))):
                if shared_fail and level < 2:
                    continue
                if rng.random() < p:
                    t = delay + rng.uniform(0, 5)
                    break
            solo += (not shared_fail) and rng.random() < 0.85
            chain += t is not None and t <= 15
            if t is not None:
                times.append(t)
        out.append({"escenario": label, "sin escalar, atendida %": round(100 * solo / pages, 1),
                    "con tres niveles, atendida en 15 min %": round(100 * chain / pages, 1),
                    "mediana de minutos hasta atender": round(pct(times, 50), 1), "p99": round(pct(times, 99), 1)})
    return {"filas": out}


BASE_ALERTS = ["EntregasErrores", "EntregasLatencia", "ColaAtrasada", "BaseSinReplicas", "CertificadoPorVencer", "DiscoLleno", "CopiaSinVerificar", "TokensExpirando"]
DESTRUCTIVE = ("delete", "drop", "restart", "rm ", "truncate", "failover", "rollback", "undo")


def _runbook(i: int, rng: random.Random) -> dict:
    alert = BASE_ALERTS[i % len(BASE_ALERTS)]
    return {
        "titulo": f"Atender {alert}", "alerta": alert, "propietario": f"equipo-{i % 4}", "verificado": (TODAY - timedelta(days=rng.randint(5, 60))).isoformat(),
        "escalamiento": f"guardia-secundaria-{i % 4}",
        "pasos": [
            {"orden": 1, "comando": "kubectl get pods -n entregas", "esperado": "todos Running", "reversion": "no aplica", "destructivo": False},
            {"orden": 2, "comando": "kubectl rollout undo deployment/api -n entregas", "esperado": "deployment/api rolled back", "reversion": "kubectl rollout undo", "destructivo": True},
            {"orden": 3, "comando": "curl -fsS https://entregas.example/health", "esperado": "estado ok", "reversion": "no aplica", "destructivo": False},
        ],
    }


def validate_runbook(rb: dict) -> list[str]:
    problems = []
    for key in ("titulo", "alerta", "propietario", "verificado", "escalamiento", "pasos"):
        if not rb.get(key):
            problems.append(f"falta {key}")
    if rb.get("alerta") not in BASE_ALERTS:
        problems.append("alerta inexistente")
    try:
        if (TODAY - date.fromisoformat(rb["verificado"])).days > 90:
            problems.append("verificación vencida")
    except (KeyError, ValueError):
        problems.append("fecha ilegible")
    if str(rb.get("escalamiento", "")).strip().upper() in ("", "TBD", "N/A"):
        problems.append("escalamiento vacío")
    orders = [s.get("orden") for s in rb.get("pasos", [])]
    if orders != sorted(orders) or len(set(orders)) != len(orders):
        problems.append("pasos desordenados")
    for s in rb.get("pasos", []):
        if not s.get("comando") or not str(s.get("esperado", "")).strip():
            problems.append("paso sin comando o sin salida esperada")
        if any(w in str(s.get("comando", "")) for w in DESTRUCTIVE) and (not s.get("destructivo") or str(s.get("reversion", "")).strip() in ("", "no aplica")):
            problems.append("paso destructivo sin marcar o sin reversión")
    return problems


def _mutations() -> dict:
    def drop(key):
        return lambda rb, rng: rb.pop(key, None)

    def blank_expected(rb, rng):
        rb["pasos"][rng.randrange(3)]["esperado"] = ""

    def no_rollback(rb, rng):
        rb["pasos"][1]["reversion"] = "no aplica"

    def old_date(rb, rng):
        rb["verificado"] = (TODAY - timedelta(days=rng.randint(120, 400))).isoformat()

    def typo_alert(rb, rng):
        rb["alerta"] = rb["alerta"].replace("Entregas", "Entrega", 1) if "Entregas" in rb["alerta"] else rb["alerta"] + "X"

    def tbd(rb, rng):
        rb["escalamiento"] = "TBD"

    def swap(rb, rng):
        a, b = rb["pasos"][0], rb["pasos"][2]
        for key in ("comando", "esperado", "reversion", "destructivo"):
            a[key], b[key] = b[key], a[key]

    def wrong_env(rb, rng):
        rb["pasos"][0]["comando"] = rb["pasos"][0]["comando"].replace("entregas", "entregas-staging")

    def wrong_cmd(rb, rng):
        rb["pasos"][1]["comando"] = "kubectl rollout undo deployment/worker -n entregas"

    def plausible_expected(rb, rng):
        rb["pasos"][2]["esperado"] = "estado ok (200)"

    def ghost_owner(rb, rng):
        rb["propietario"] = "equipo-disuelto"

    return {"quita un campo obligatorio": drop("propietario"), "vacía la salida esperada": blank_expected, "quita la reversión de un paso destructivo": no_rollback,
            "envejece la verificación": old_date, "alerta con errata": typo_alert, "escalamiento «TBD»": tbd, "intercambia el contenido de dos pasos": swap,
            "apunta al entorno equivocado": wrong_env, "cambia el comando por otro plausible": wrong_cmd, "propietario inexistente": ghost_owner}


@cache
def e427_linter(seed: int = 4272, per_operator: int = 24) -> dict:
    rng = random.Random(seed)
    base_problems = sum(bool(validate_runbook(_runbook(i, rng))) for i in range(len(BASE_ALERTS)))
    rows, total, caught = [], 0, 0
    for name, op in _mutations().items():
        c = 0
        for i in range(per_operator):
            rb = _runbook(i, rng)
            op(rb, rng)
            c += bool(validate_runbook(rb))
        rows.append({"mutación": name, "detectadas": c, "de": per_operator})
        total += per_operator
        caught += c
    return {"bases con problemas": base_problems, "filas": rows, "total": total, "detectadas": caught}


# ---------------------------------------------------------------- SE-428
@cache
def e428_cronologia(seed: int = 428, incidents: int = 2000) -> dict:
    rng = random.Random(seed)
    parts = {"detección": (6, 0.9), "reconocimiento": (3, 0.5), "diagnóstico": (25, 1.0), "mitigación": (12, 0.7), "verificación": (5, 0.4)}

    def one(scale: dict | None = None) -> dict:
        scale = scale or {}
        return {k: rng.lognormvariate(math.log(m * scale.get(k, 1.0)), s) for k, (m, s) in parts.items()}

    data = [one() for _ in range(incidents)]
    total = [sum(d.values()) for d in data]
    means = {k: sum(d[k] for d in data) / incidents for k in parts}
    window = [sum(rng.choice(total) for _ in range(30)) / 30 for _ in range(4000)]
    result = {"incidentes": incidents, "media min": round(sum(total) / incidents, 1), "mediana min": round(pct(total, 50), 1), "p90 min": round(pct(total, 90), 1),
              "p99 min": round(pct(total, 99), 1), "medias por tramo": {k: round(v, 1) for k, v in means.items()},
              "media de 30 incidentes: p5–p95": [round(pct(window, 5), 1), round(pct(window, 95), 1)]}
    effects = {}
    for k in ("detección", "diagnóstico", "mitigación"):
        rng2 = random.Random(seed + 1)
        t = [sum(rng2.lognormvariate(math.log(m * (0.5 if kk == k else 1.0)), s) for kk, (m, s) in parts.items()) for _ in range(incidents)]
        effects[k] = round(sum(t) / incidents, 1)
    result["media si se reduce a la mitad la mediana de"] = effects
    return result


@cache
def e428_actualizaciones(seed: int = 4281, trials: int = 1500) -> dict:
    rng = random.Random(seed)
    out = []
    for label, cadence in (("sin cadencia", None), ("cada 60 min", 60), ("cada 30 min", 30), ("cada 15 min", 15), ("cada 5 min", 5)):
        asks_total = updates_total = 0
        for _ in range(trials):
            duration = int(rng.lognormvariate(math.log(90), 0.6))
            last = 0
            for minute in range(duration):
                asks_total += poisson(rng, 0.05 * (1 + (minute - last) / 15))
                if cadence and (minute + 1) % cadence == 0:
                    last = minute + 1
                    updates_total += 1
        out.append({"política": label, "preguntas por incidente": round(asks_total / trials, 1), "actualizaciones": round(updates_total / trials, 1),
                    "minutos de la persona al mando": round((3 * asks_total + 4 * updates_total) / trials, 1)})
    return {"filas": out}


def _kappa(a: list[int], b: list[int], k: int = 4) -> float:
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in range(1, k + 1))
    return (po - pe) / (1 - pe)


@cache
def e428_severidad(seed: int = 4282, incidents: int = 400) -> dict:
    rng = random.Random(seed)
    latent = [rng.lognormvariate(0, 1.4) for _ in range(incidents)]
    cuts = [0.5, 1.5, 6.0]

    def sev(x: float) -> int:
        return 1 + sum(x > c for c in cuts)

    truth = [sev(x) for x in latent]
    rows = []
    for label, sigma in (("criterios vagos («grave», «moderado»)", 0.9), ("umbrales numéricos de impacto", 0.35), ("umbrales y un ejemplo por nivel", 0.15)):
        raters = [[sev(x * math.exp(rng.gauss(0, sigma))) for x in latent] for _ in range(3)]
        pairs = [(0, 1), (0, 2), (1, 2)]
        kappas = [_kappa(raters[i], raters[j]) for i, j in pairs]
        exact = sum(r[i] == truth[i] for r in raters for i in range(incidents)) / (3 * incidents)
        far = sum(abs(r[i] - truth[i]) >= 2 for r in raters for i in range(incidents)) / (3 * incidents)
        rows.append({"criterio": label, "kappa medio": round(sum(kappas) / 3, 2), "acuerdo con la verdad %": round(100 * exact, 1), "error de 2 o más niveles %": round(100 * far, 1)})
    return {"filas": rows}


# ---------------------------------------------------------------- SE-429
@cache
def e429_recurrencia(seed: int = 429, trials: int = 300) -> dict:
    rng = random.Random(seed)
    total = sum(1 / (i + 1) for i in range(12))
    base = [40 * (1 / (i + 1)) / total for i in range(12)]
    out = []
    for c in (0.3, 0.6, 0.9):
        years = [0.0, 0.0, 0.0]
        for _ in range(trials):
            rate = list(base)
            for y in range(3):
                for i in range(12):
                    n = poisson(rng, rate[i])
                    years[y] += n
                    for _ in range(n):
                        if rng.random() < c:
                            rate[i] *= 0.4
        out.append({"acciones completadas %": int(c * 100), "año 1": round(years[0] / trials, 1), "año 2": round(years[1] / trials, 1), "año 3": round(years[2] / trials, 1)})
    return {"filas": out, "incidentes esperados por año sin acciones": 40, "causas": 12}


FACTORS = {
    "síntoma: entregas rechazadas": ["certificado vencido", "despliegue sin verificación"],
    "certificado vencido": ["alerta de vencimiento ignorada", "renovación manual"],
    "alerta de vencimiento ignorada": ["fatiga de alertas", "propietario ausente"],
    "renovación manual": ["sin automatización", "documentación desactualizada"],
    "despliegue sin verificación": ["presión por el plazo", "sin verificación posterior"],
    "sin verificación posterior": ["pipeline sin etapa de humo"],
    "propietario ausente": ["guardia de una sola persona"],
    "fatiga de alertas": [], "sin automatización": [], "documentación desactualizada": [], "presión por el plazo": [],
    "pipeline sin etapa de humo": [], "guardia de una sola persona": [],
}


@cache
def e429_cadena(seed: int = 4291, analysts: int = 400) -> dict:
    rng = random.Random(seed)
    factors = [f for f in FACTORS if not f.startswith("síntoma")]
    roots = []
    coverages = []
    for _ in range(analysts):
        node, chain = "síntoma: entregas rechazadas", set()
        while FACTORS[node]:
            node = rng.choice(FACTORS[node])
            chain.add(node)
        roots.append(node)
        coverages.append(len(chain) / len(factors))
    distinct = sorted(set(roots))
    group = []
    for _ in range(2000):
        union = set()
        for _ in range(4):
            node = "síntoma: entregas rechazadas"
            while FACTORS[node]:
                node = rng.choice(FACTORS[node])
                union.add(node)
        group.append(len(union) / len(factors))
    return {"factores": len(factors), "causas raíz distintas halladas": len(distinct), "cobertura media de una cadena %": round(100 * sum(coverages) / analysts, 1),
            "cobertura media de cuatro analistas %": round(100 * sum(group) / len(group), 1), "reparto de raíces": {r: roots.count(r) for r in distinct}}


BLAME = ("negligencia", "descuido", "error humano", "debió haber", "no tuvo cuidado", "falta de atención", "incompetencia", "culpa")


def validate_postmortem(doc: dict) -> list[str]:
    problems = []
    text = " ".join([str(v) for v in doc.values() if isinstance(v, str)] + [str(f) for f in doc.get("factores", [])]).lower()
    if any(w in text for w in BLAME):
        problems.append("lenguaje de culpa")
    if not doc.get("impacto") or not any(ch.isdigit() for ch in doc["impacto"]):
        problems.append("impacto sin cifras")
    if not doc.get("linea_de_tiempo") or not all(t.get("hora") for t in doc["linea_de_tiempo"]):
        problems.append("línea de tiempo sin horas")
    if len(doc.get("factores", [])) < 2:
        problems.append("menos de dos factores contribuyentes")
    if not doc.get("lo_que_funciono"):
        problems.append("sin lo que funcionó")
    for a in doc.get("acciones", []):
        if not a.get("propietario") or not a.get("fecha"):
            problems.append("acción sin propietario o fecha")
        if not a.get("verificacion"):
            problems.append("acción sin criterio de verificación")
    if not doc.get("acciones"):
        problems.append("sin acciones")
    return problems


def _postmortem(i: int) -> dict:
    return {"resumen": f"Entregas rechazadas durante {20 + i} minutos por un certificado vencido.", "impacto": f"{300 + 10 * i} entregas rechazadas; 12 % de las peticiones durante {20 + i} min",
            "linea_de_tiempo": [{"hora": "14:02", "evento": "alerta"}, {"hora": "14:09", "evento": "diagnóstico"}, {"hora": "14:31", "evento": "certificado renovado"}],
            "factores": ["renovación manual", "alerta de vencimiento ignorada", "documentación desactualizada"], "lo_que_funciono": "la reversión del despliegue tardó 3 minutos",
            "acciones": [{"descripcion": "automatizar la renovación", "propietario": "equipo-plataforma", "fecha": "2026-12-15", "verificacion": "el certificado de pruebas se renueva sin intervención"},
                         {"descripcion": "alerta de vencimiento a 21 días", "propietario": "equipo-guardia", "fecha": "2026-12-01", "verificacion": "la alerta se dispara en el entorno de pruebas"}]}


@cache
def e429_linter(seed: int = 4292, per: int = 20) -> dict:
    rng = random.Random(seed)

    def blame_explicit(d):
        d["resumen"] += " Hubo negligencia del operador de turno."

    def blame_implicit(d):
        d["resumen"] += " Como siempre, el turno de noche no revisó los certificados."

    def vague_action(d):
        d["acciones"][0].update(descripcion="tener más cuidado", verificacion="se revisará")

    def no_owner(d):
        d["acciones"][0]["propietario"] = ""

    def no_figures(d):
        d["impacto"] = "afectó a muchas personas"

    def no_times(d):
        d["linea_de_tiempo"][1]["hora"] = ""

    def single_cause(d):
        d["factores"] = ["error humano del operador"]

    def made_up_timeline(d):
        d["linea_de_tiempo"][2]["hora"] = "13:05"

    def ops(d):
        d["acciones"].append({"descripcion": "reescribir el sistema", "propietario": "alguien", "fecha": "2027-12-31", "verificacion": "cuando esté listo"})

    operators = {"culpa explícita": blame_explicit, "culpa implícita": blame_implicit, "acción vaga con verificación débil": vague_action, "acción sin propietario": no_owner,
                 "impacto sin cifras": no_figures, "línea de tiempo sin hora": no_times, "una sola causa («error humano»)": single_cause,
                 "hora inventada fuera de orden": made_up_timeline, "acción desproporcionada con propietario genérico": ops}
    rows, caught, total = [], 0, 0
    for name, op in operators.items():
        c = 0
        for i in range(per):
            doc = _postmortem(rng.randrange(0, 30))
            op(doc)
            c += bool(validate_postmortem(doc))
        rows.append({"mutación": name, "detectadas": c, "de": per})
        caught += c
        total += per
    return {"base con problemas": bool(validate_postmortem(_postmortem(0))), "filas": rows, "detectadas": caught, "total": total}


# ---------------------------------------------------------------- SE-430
@cache
def e430_rpo(seed: int = 430, failures: int = 20000) -> dict:
    rng = random.Random(seed)
    out = []
    for label, interval in (("copia diaria", 24 * 60), ("copia cada 6 h", 6 * 60), ("copia cada hora", 60)):
        loss = [rng.uniform(0, interval) for _ in range(failures)]
        out.append({"estrategia": label, "pérdida mediana min": round(pct(loss, 50), 1), "p99 min": round(pct(loss, 99), 1), "máxima min": round(max(loss), 1),
                    "incumple RPO de 5 min %": round(100 * sum(x > 5 for x in loss) / failures, 1)})
    lag = []
    for _ in range(failures):
        lag.append(rng.uniform(10, 300) / 60 if rng.random() < 0.01 else rng.lognormvariate(math.log(2 / 60), 0.6))
    out.append({"estrategia": "réplica asíncrona (retraso medido en minutos)", "pérdida mediana min": round(pct(lag, 50), 2), "p99 min": round(pct(lag, 99), 2),
                "máxima min": round(max(lag), 1), "incumple RPO de 5 min %": round(100 * sum(x > 5 for x in lag) / failures, 2)})
    return {"filas": out}


def _probe_copy(path: Path, rows: int) -> tuple[bool, bool, bool]:
    """Devuelve si integrity_check, el conteo de filas y la lectura completa detectan el daño."""
    expected = sum(len("x" * 120 + str(i)) for i in range(rows))
    results = []
    for step in ("integrity", "count", "full"):
        con = sqlite3.connect(path)
        try:
            if step == "integrity":
                results.append(con.execute("PRAGMA integrity_check").fetchone()[0] != "ok")
            elif step == "count":
                results.append(con.execute("SELECT COUNT(*) FROM entregas").fetchone()[0] != rows)
            else:
                results.append(sum(len(r[0]) for r in con.execute("SELECT contenido FROM entregas")) != expected)
        except (sqlite3.DatabaseError, UnicodeDecodeError):
            results.append(True)
        finally:
            con.close()
    return results[0], results[1], results[2]


@cache
def e430_copias(seed: int = 4301, rows: int = 20000, copies: int = 40) -> dict:
    import time

    rng = random.Random(seed)
    result = {"filas de la base": rows, "copias dañadas": copies}
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        source = root / "origen.db"
        con = sqlite3.connect(source)
        con.execute("CREATE TABLE entregas (id INTEGER PRIMARY KEY, curso INTEGER, contenido TEXT)")
        con.executemany("INSERT INTO entregas (curso, contenido) VALUES (?, ?)", [(i % 60, "x" * 120 + str(i)) for i in range(rows)])
        con.commit()
        t0 = time.perf_counter()
        good = root / "copia.db"
        dest = sqlite3.connect(good)
        con.backup(dest)
        dest.close()
        con.close()
        t_backup = time.perf_counter() - t0
        size = good.stat().st_size
        digest = hashlib.sha256(good.read_bytes()).hexdigest()
        t0 = time.perf_counter()
        check = sqlite3.connect(good)
        count = check.execute("SELECT COUNT(*) FROM entregas").fetchone()[0]
        integ = check.execute("PRAGMA integrity_check").fetchone()[0]
        check.close()
        t_verify = time.perf_counter() - t0
        found = {"mismo tamaño": 0, "huella sha256": 0, "integrity_check": 0, "conteo de filas": 0, "lectura completa de todas las filas": 0}
        for n in range(copies):
            bad = root / f"mala{n}.db"
            data = bytearray(good.read_bytes())
            for _ in range(8):
                data[rng.randrange(100, len(data))] ^= 0xFF
            bad.write_bytes(bytes(data))
            found["mismo tamaño"] += bad.stat().st_size != size
            found["huella sha256"] += hashlib.sha256(bad.read_bytes()).hexdigest() != digest
            integ_bad, count_bad, full_bad = _probe_copy(bad, rows)
            found["integrity_check"] += integ_bad
            found["conteo de filas"] += count_bad
            found["lectura completa de todas las filas"] += full_bad
        result.update({"filas restauradas": count, "integrity_check de la copia buena": integ, "detección": found,
                       "tamaño de la copia (bytes)": size, "segundos de copia (reloj)": round(t_backup, 3), "segundos de verificación (reloj)": round(t_verify, 3)})
    return result


DR_GRAPH = {
    "dns": ([], 10), "red": ([], 15), "identidad": (["dns", "red"], 20), "secretos": (["identidad"], 10), "base de datos": (["red", "secretos"], 45),
    "almacenamiento de objetos": (["red", "secretos"], 30), "cola": (["red", "secretos"], 15), "api": (["base de datos", "cola", "identidad"], 15),
    "trabajadores": (["cola", "base de datos", "almacenamiento de objetos"], 10), "portal web": (["api", "dns"], 10),
    "observabilidad": (["red"], 25), "canal de despliegue": (["secretos", "api"], 20),
}
def _critical(graph: dict) -> tuple[int, int, bool]:
    memo: dict[str, int] = {}
    state: dict[str, int] = {}
    cyc = False

    def finish(n: str) -> int:
        nonlocal cyc
        if n in memo:
            return memo[n]
        if state.get(n) == 1:
            cyc = True
            return 0
        state[n] = 1
        deps, dur = graph[n]
        value = dur + max((finish(d) for d in deps), default=0)
        state[n] = 2
        memo[n] = value
        return value

    path = max(finish(n) for n in graph)
    return sum(d for _, d in graph.values()), path, cyc


@cache
def e430_dependencias() -> dict:
    declared = {k: (list(v[0]), v[1]) for k, v in DR_GRAPH.items()}
    rows = []
    serial, path, cyc = _critical(declared)
    rows.append({"conjunto": "dependencias declaradas", "serie min": serial, "ruta crítica min": path, "ciclo": cyc})
    cyclic = {k: (list(v[0]), v[1]) for k, v in declared.items()}
    cyclic["identidad"][0].append("secretos")
    s2, p2, c2 = _critical(cyclic)
    rows.append({"conjunto": "ejercicio 1: la identidad necesita los secretos", "serie min": s2, "ruta crítica min": None if c2 else p2, "ciclo": c2})
    broken = {k: (list(v[0]), v[1]) for k, v in cyclic.items()}
    broken["credenciales de emergencia"] = ([], 20)
    broken["identidad"] = (["dns", "red", "credenciales de emergencia"], 20)
    s3, p3, c3 = _critical(broken)
    rows.append({"conjunto": "con credenciales de emergencia fuera de línea", "serie min": s3, "ruta crítica min": None if c3 else p3, "ciclo": c3})
    extra = {k: (list(v[0]), v[1]) for k, v in broken.items()}
    extra["portal web"][0].append("observabilidad")
    s4, p4, c4 = _critical(extra)
    rows.append({"conjunto": "ejercicio 2: el portal exige observabilidad sana", "serie min": s4, "ruta crítica min": None if c4 else p4, "ciclo": c4})
    return {"filas": rows, "componentes": len(DR_GRAPH)}


# ---------------------------------------------------------------- SE-431
FAULTS = ["certificado vencido", "base saturada", "cola atrasada", "despliegue defectuoso", "caché fría", "DNS inestable", "disco lleno", "dependencia externa caída", "fuga de memoria", "límite de cuota"]
SIGNALS = ["errores 5xx", "latencia p99", "conexiones a la base", "profundidad de la cola", "reinicios de contenedores", "fallos de resolución", "uso de disco", "errores de TLS", "tasa de aciertos de caché", "memoria del proceso", "errores 429", "versión desplegada"]
MATRIX = [
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
]


@cache
def e431_ambiguedad() -> dict:
    from itertools import combinations

    rows = []
    for missing in (0, 1, 2, 3, 4, 6):
        classes, unique, worst, n = 0, 0, 0, 0
        for gone in combinations(range(12), missing):
            keep = [i for i in range(12) if i not in gone]
            sigs: dict[tuple, int] = {}
            for f in MATRIX:
                key = tuple(f[i] for i in keep)
                sigs[key] = sigs.get(key, 0) + 1
            classes += len(sigs)
            unique += sum(1 for v in sigs.values() if v == 1)
            worst = max(worst, max(sigs.values()))
            n += 1
        rows.append({"señales ausentes": missing, "clases distinguibles (media de 10)": round(classes / n, 2), "fallas identificables sin ambigüedad (media)": round(unique / n, 2),
                     "mayor grupo de fallas indistinguibles": worst, "combinaciones": n})
    return {"fallas": len(FAULTS), "señales": len(SIGNALS), "filas": rows}


@cache
def e431_estrategias(seed: int = 4311, trials: int = 4000) -> dict:
    rng = random.Random(seed)
    cost = [1, 1, 3, 2, 2, 3, 1, 2, 3, 4, 2, 1]
    strategies = {"mayor ganancia de información": "gain", "la más barata primero": "cheap", "al azar": "random"}
    out = []
    for label, kind in strategies.items():
        steps_total = cost_total = 0
        for _ in range(trials):
            truth = rng.randrange(len(FAULTS))
            candidates = list(range(len(FAULTS)))
            unused = list(range(12))
            steps = spent = 0
            while len(candidates) > 1 and unused:
                if kind == "gain":
                    pick = max(unused, key=lambda s: -abs(sum(MATRIX[c][s] for c in candidates) - len(candidates) / 2) - 0.01 * cost[s])
                elif kind == "cheap":
                    pick = min(unused, key=lambda s: (cost[s], s))
                else:
                    pick = rng.choice(unused)
                unused.remove(pick)
                steps += 1
                spent += cost[pick]
                candidates = [c for c in candidates if MATRIX[c][pick] == MATRIX[truth][pick]]
            steps_total += steps
            cost_total += spent
        out.append({"estrategia": label, "observaciones hasta aislar (media)": round(steps_total / trials, 2), "coste medio": round(cost_total / trials, 2)})
    return {"filas": out}


@cache
def e431_perdida(seed: int = 4312) -> dict:
    rng = random.Random(seed)
    lines = [(rng.random() < 0.12, rng.random()) for _ in range(60 * 150)]
    rows = []
    for label, drop_ok, drop_err in (("pérdida igual para todas las líneas", 0.02, 0.02), ("pérdida de 25 % en las líneas de error durante el incidente", 0.02, 0.25),
                                     ("pérdida de 50 % en las líneas de error durante el incidente", 0.02, 0.50)):
        true_err = kept = kept_err = total = 0
        for is_err, u in lines:
            total += 1
            true_err += is_err
            if u > (drop_err if is_err else drop_ok):
                kept += 1
                kept_err += is_err
        rows.append({"modelo": label, "tasa de error real %": round(100 * true_err / total, 2), "tasa observada en los registros %": round(100 * kept_err / kept, 2),
                     "líneas conservadas %": round(100 * kept / total, 1)})
    return {"filas": rows}


# ---------------------------------------------------------------- SE-432
def _package(rng: random.Random) -> dict:
    return {
        "servicios": ["entregas-api", "trabajadores"],
        "slos": {"entregas-api": {"sli": "peticiones buenas / válidas", "objetivo": 0.999, "ventana_dias": 28}, "trabajadores": {"sli": "trabajos < 5 min", "objetivo": 0.995, "ventana_dias": 28}},
        "alertas": [{"nombre": "EntregasConsumoRapido", "slo": "entregas-api", "runbook": "rb-entregas", "severidad": "página"},
                    {"nombre": "ColaAtrasada", "slo": "trabajadores", "runbook": "rb-cola", "severidad": "página"}],
        "runbooks": {"rb-entregas": {"propietario": "equipo-api", "verificado": (TODAY - timedelta(days=rng.randint(5, 50))).isoformat()},
                     "rb-cola": {"propietario": "equipo-datos", "verificado": (TODAY - timedelta(days=rng.randint(5, 50))).isoformat()}},
        "copias": {"base-entregas": {"rpo_min": 15, "ultima_restauracion": (TODAY - timedelta(days=rng.randint(5, 50))).isoformat(), "restauracion_min": 38, "rto_min": 60}},
        "ejercicios": [{"fecha": (TODAY - timedelta(days=rng.randint(5, 80))).isoformat(), "tipo": "recuperación", "hallazgos": 3, "corregidos": 2}],
        "guardia": {"personas": 5, "escalamiento": ["primaria", "secundaria", "responsable"]},
    }


def validate_package(p: dict) -> list[str]:
    problems = []
    for s in p.get("servicios", []):
        slo = p.get("slos", {}).get(s)
        if not slo:
            problems.append(f"{s} sin SLO")
        elif not 0.9 <= slo.get("objetivo", 0) < 1:
            problems.append(f"{s} SLO fuera de rango")
    runbooks = p.get("runbooks", {})
    for a in p.get("alertas", []):
        if a.get("slo") not in p.get("slos", {}):
            problems.append("alerta sin SLO")
        if a.get("runbook") not in runbooks:
            problems.append("alerta sin runbook")
    for name, rb in runbooks.items():
        if not rb.get("propietario"):
            problems.append("runbook sin propietario")
        if (TODAY - date.fromisoformat(rb["verificado"])).days > 90:
            problems.append("runbook sin verificar")
    for name, c in p.get("copias", {}).items():
        if (TODAY - date.fromisoformat(c["ultima_restauracion"])).days > 90:
            problems.append("restauración sin probar")
        if c["restauracion_min"] > c["rto_min"]:
            problems.append("restauración mayor que el RTO")
    ex = p.get("ejercicios", [])
    if not ex or (TODAY - date.fromisoformat(ex[0]["fecha"])).days > 180:
        problems.append("sin ejercicio reciente")
    elif ex[0]["corregidos"] < ex[0]["hallazgos"] - 5:
        problems.append("hallazgos sin corregir")
    if len(p.get("guardia", {}).get("escalamiento", [])) < 2:
        problems.append("escalamiento de un solo nivel")
    return problems


@cache
def e432_validador(seed: int = 432, per: int = 30) -> dict:
    rng = random.Random(seed)

    def m_slo(p):
        del p["slos"]["trabajadores"]

    def m_alert_slo(p):
        p["alertas"][0]["slo"] = "inexistente"

    def m_alert_rb(p):
        p["alertas"][1]["runbook"] = "rb-fantasma"

    def m_old_restore(p):
        p["copias"]["base-entregas"]["ultima_restauracion"] = (TODAY - timedelta(days=200)).isoformat()

    def m_rto(p):
        p["copias"]["base-entregas"]["restauracion_min"] = 240

    def m_no_ex(p):
        p["ejercicios"] = []

    def m_one_level(p):
        p["guardia"]["escalamiento"] = ["primaria"]

    def m_loose_slo(p):
        p["slos"]["entregas-api"]["objetivo"] = 0.95

    def m_wrong_rpo(p):
        p["copias"]["base-entregas"]["rpo_min"] = 1440

    def m_fake_ex(p):
        p["ejercicios"][0].update(hallazgos=5, corregidos=5)

    def m_swapped(p):
        p["alertas"][0]["runbook"], p["alertas"][1]["runbook"] = p["alertas"][1]["runbook"], p["alertas"][0]["runbook"]

    def m_sli(p):
        p["slos"]["entregas-api"]["sli"] = "el servidor está encendido"

    ops = {"servicio sin SLO": m_slo, "alerta sin SLO existente": m_alert_slo, "alerta sin runbook existente": m_alert_rb, "restauración sin probar": m_old_restore,
           "restauración mayor que el RTO": m_rto, "sin ejercicio": m_no_ex, "escalamiento de un nivel": m_one_level, "objetivo SLO laxo pero en rango": m_loose_slo,
           "RPO incoherente con la copia": m_wrong_rpo, "ejercicio sin hallazgos que corregir": m_fake_ex, "runbooks intercambiados": m_swapped, "SLI que no mide al usuario": m_sli}
    rows, caught, total = [], 0, 0
    base = sum(bool(validate_package(_package(rng))) for _ in range(20))
    for name, op in ops.items():
        c = 0
        for _ in range(per):
            p = _package(rng)
            op(p)
            c += bool(validate_package(p))
        rows.append({"mutación": name, "detectadas": c, "de": per})
        caught += c
        total += per
    return {"bases con problemas": base, "filas": rows, "detectadas": caught, "total": total}


@cache
def e432_cadena(seed: int = 4321, incidents: int = 20000) -> dict:
    rng = random.Random(seed)
    stages = [("detección", 0.95), ("llegada a una persona", 0.92), ("diagnóstico", 0.80), ("mitigación", 0.88), ("verificación de la recuperación", 0.90)]
    fail = {n: 0 for n, _ in stages}
    ok = 0
    for _ in range(incidents):
        shared = rng.random() < 0.05  # caída de la telemetría que afecta a la detección y al diagnóstico
        success = True
        for name, p in stages:
            if shared and name in ("detección", "diagnóstico"):
                p = p * 0.3
            if rng.random() >= p:
                fail[name] += 1
                success = False
                break
        ok += success
    product = math.prod(p for _, p in stages)
    improved = {}
    for name, _ in stages:
        modified = [(n, min(0.99, p + 0.05) if n == name else p) for n, p in stages]
        improved[name] = round(100 * math.prod(p for _, p in modified), 1)
    return {"producto de las etapas %": round(100 * product, 1), "recuperación completa simulada %": round(100 * ok / incidents, 1),
            "fallos por etapa %": {k: round(100 * v / incidents, 1) for k, v in fail.items()}, "mejorar 5 puntos la etapa (producto %)": improved}


@cache
def e432_reproducibilidad() -> dict:
    virtual = json.dumps({"validador": e432_validador(), "cadena": e432_cadena(), "guardia": e427_guardia()}, sort_keys=True, ensure_ascii=False)
    with tempfile.TemporaryDirectory() as tmp:
        probe = Path(tmp) / "a b" / "ñ.txt"
        probe.parent.mkdir()
        probe.write_text("línea\n", encoding="utf-8")
        raw_text = probe.read_bytes()
        local_text = probe.read_text()
        local_name = os.path.basename(str(probe))
    return {"huella de los resultados virtuales": hashlib.sha256(virtual.encode("utf-8")).hexdigest()[:16], "separador de línea del sistema": repr(os.linesep),
            "bytes de «línea\\n» escritos con utf-8": len(raw_text), "texto leído con la codificación local": len(local_text), "separador de rutas": os.sep,
            "mayúsculas distinguidas en rutas": os.path.normcase("A") == "A", "nombre con eñe conservado": local_name == "ñ.txt"}


def results() -> dict:
    return {
        "e427_guardia": e427_guardia(), "e427_escalamiento": e427_escalamiento(), "e427_linter": e427_linter(),
        "e428_cronologia": e428_cronologia(), "e428_actualizaciones": e428_actualizaciones(), "e428_severidad": e428_severidad(),
        "e429_recurrencia": e429_recurrencia(), "e429_cadena": e429_cadena(), "e429_linter": e429_linter(),
        "e430_rpo": e430_rpo(), "e430_copias": e430_copias(), "e430_dependencias": e430_dependencias(),
        "e431_ambiguedad": e431_ambiguedad(), "e431_estrategias": e431_estrategias(), "e431_perdida": e431_perdida(),
        "e432_validador": e432_validador(), "e432_cadena": e432_cadena(), "e432_reproducibilidad": e432_reproducibilidad(),
    }


if __name__ == "__main__":
    data = results()
    if len(sys.argv) > 1:
        data = {k: v for k, v in data.items() if k.startswith(sys.argv[1])}
    print(json.dumps(data, ensure_ascii=False, indent=1))
