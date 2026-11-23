"""Experimentos de las clases SE-512 a SE-516 (caos en CI/CD, datos y ML, escala, seguridad, ética e integración).

Tiempo virtual y semillas fijas, como en ``experiments_part42_a``; no hay reloj, red ni servicio reales.
Ejecutar ``python scripts/experiments_part42_b.py`` imprime los resultados como JSON.
"""
from __future__ import annotations

import hashlib
import json
import math
import random
import statistics as st
import sys
from dataclasses import replace
from functools import cache

from experiments_part42_a import CONFIGS, RATE
from experiments_part42_sim import Fault, Policy, pct, simulate, summarize

# ---------------------------------------------------------------- SE-512
BASE = CONFIGS["E"][1]
REGRESSIONS = {
    "R1 se quita la espera corta (5 s)": replace(BASE, timeout_ms=5000),
    "R2 reintentos sin pausa y espera de 1 s": replace(BASE, timeout_ms=1000, retries=3, backoff="none", breaker=None, fallback=False),
    "R3 se quita el cortacircuitos": replace(BASE, breaker=None, fallback=False),
    "R4 se quita la alternativa": replace(BASE, fallback=False),
    "R5 cortacircuitos sensible (50 % en 20 intentos)": replace(BASE, breaker=(0.5, 20, 5000)),
    "R6 cinco reintentos": replace(BASE, retries=5),
    "R7 cambio inocuo: un reintento menos": replace(BASE, retries=1),
}
SUITE = [
    ("30 % de errores", Fault("error", 10, 30, 0.3)),
    ("dependencia lenta +100 ms", Fault("slow", 10, 30, 100)),
    ("mitad de los hilos", Fault("capacity", 10, 30, 0.5)),
    ("sin respuesta", Fault("blackhole", 10, 30, 1.0)),
]
STATIC_RULES = {
    "R1": lambda p: p.timeout_ms > 1000,
    "R2": lambda p: p.retries > 0 and p.backoff == "none",
    "R3": lambda p: p.breaker is None,
    "R4": lambda p: not p.fallback,
    "R5": lambda p: False,  # la sensibilidad de un umbral no se juzga leyendo la configuración
    "R6": lambda p: p.retries > 3,
    "R7": lambda p: False,
}


def _passes(policy: Policy, fault: Fault, seed: int) -> bool:
    r = simulate(seed, policy, [fault], duration_s=60.0, rate=RATE)
    inside = summarize(r, fault.start + 2, fault.end)
    after = summarize(r, fault.end + 15, 60.0)
    return (inside["ok"] + inside["degraded"]) >= 0.99 and after["ok"] >= 0.99


@cache
def e512_ci(seeds: int = 8) -> dict:
    out: dict = {"escenarios": [n for n, _ in SUITE], "semillas": seeds}
    healthy = {}
    for name, fault in SUITE:
        healthy[name] = sum(1 for s in range(seeds) if not _passes(BASE, fault, 600 + s)) / seeds
    out["sana"] = healthy
    reg = {}
    for rname, policy in REGRESSIONS.items():
        per = {}
        for name, fault in SUITE:
            fails = sum(1 for s in range(seeds) if not _passes(policy, fault, 600 + s))
            per[name] = fails / seeds
        reg[rname] = per
    out["regresiones"] = reg
    # cobertura por tamaño de la suite: una regresión se detecta si algún escenario de la suite la hace fallar en la mayoría de las semillas
    cover = {}
    for k in range(1, len(SUITE) + 1):
        names = [n for n, _ in SUITE[:k]]
        cover[k] = {r: any(reg[r][n] >= 0.5 for n in names) for r in reg}
    out["cobertura"] = cover
    out["estatico"] = {r: bool(STATIC_RULES[r.split()[0]](REGRESSIONS[r])) for r in REGRESSIONS}
    out["minutos por escenario"] = 1.0
    return out


# ---------------------------------------------------------------- SE-515
@cache
def e515_region(seeds: int = 2) -> dict:
    """Evacuar una región: la carga que absorben las regiones restantes frente a su holgura."""
    cells = {}
    for regions in (2, 3, 4, 6):
        for util in (0.4, 0.55, 0.7, 0.85):
            new_util = util * regions / (regions - 1)
            rate = 200.0 * new_util
            oks = []
            for s in range(seeds):
                r = simulate(800 + s, BASE, [], duration_s=60.0, rate=rate)
                oks.append(summarize(r, 5, 60)["ok"])
            cells[f"{regions}|{util}"] = {"carga tras evacuar": new_util, "ok": st.mean(oks)}
    return {"celdas": cells, "capacidad por región rps": 200.0}


@cache
def e515_concentracion() -> dict:
    """La misma lentitud inyectada de forma difusa o concentrada: el umbral aparece solo con concentración."""
    fractions = (0.0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0)
    rows = {}
    for name, key in (("sin protección", "A"), ("reintentos sin pausa", "B"), ("con cortacircuitos calibrado", "E")):
        policy = CONFIGS[key][1]
        series = []
        for f in fractions:
            r = simulate(900, policy, [Fault("slow", 5, 55, 300)], duration_s=60.0, rate=RATE, treat_fraction=f)
            s = summarize(r, 10, 55)
            series.append({"fracción": f, "ok": s["ok"] + s["degraded"] * 0.0, "responde": s["ok"] + s["degraded"], "intentos": s["attempts"]})
        rows[name] = series
    return {"filas": rows, "latencia añadida ms": 300}


# ---------------------------------------------------------------- SE-514
@cache
def e514_evidencia(seed: int = 514, trials: int = 20_000) -> dict:
    """Cuántos ensayos hacen falta para sostener que un control funciona al menos 95 % de las veces."""
    rng = random.Random(seed)
    ps = (0.80, 0.90, 0.95, 0.99, 0.999)
    ns = (5, 20, 59, 200, 1000)
    table = {}
    for p in ps:
        for n in ns:
            table[f"{p}|{n}"] = p ** n  # probabilidad de que todos los ensayos salgan bien
    # cobertura de la regla de tres: con n=59 sin fallas, el límite superior de la tasa de fallas es 3/59 ≈ 5 %
    covered = wrong = 0
    for _ in range(trials):
        p_true = rng.choice([0.90, 0.93, 0.95, 0.97, 0.99])
        fails = sum(1 for _ in range(59) if rng.random() > p_true)
        if fails == 0:
            covered += 1
            if p_true < 0.95:
                wrong += 1
    # clasificación de 30 controles con eficacias distintas
    controls = [0.999] * 18 + [0.97] * 8 + [0.80] * 4
    classif = {}
    for n in (5, 20, 59, 200):
        weak_pass = good_fail = 0
        reps = 400
        for _ in range(reps):
            for p in controls:
                fails = sum(1 for _ in range(n) if rng.random() > p)
                passed = fails == 0
                if p < 0.95 and passed:
                    weak_pass += 1
                if p >= 0.99 and not passed:
                    good_fail += 1
        classif[n] = {"controles débiles que pasan": weak_pass / (reps * 12), "controles buenos que fallan": good_fail / (reps * 18)}
    return {"tabla": table, "regla de tres": {"ensayos": 59, "cobertura": wrong / max(1, covered), "afirmaciones": covered}, "clasificación": classif}


@cache
def e514_revocacion(seed: int = 5142, clients: int = 2000) -> dict:
    """Tras revocar una credencial, cuánto tiempo y cuántas peticiones siguen autorizadas según el TTL de la caché."""
    rng = random.Random(seed)
    out = {}
    for ttl in (0, 30, 60, 300, 900):
        exposure = [rng.uniform(0, ttl) for _ in range(clients)]
        reqs = [e * 0.5 for e in exposure]  # cada cliente hace 0,5 peticiones por segundo
        out[ttl] = {"exposición media s": st.mean(exposure), "exposición p99 s": pct(exposure, 99), "peticiones autorizadas tras revocar": sum(reqs)}
    return {"clientes": clients, "ttl": out}


# ---------------------------------------------------------------- SE-513
@cache
def e513_presupuesto(months: int = 4000, seed: int = 515) -> dict:
    """Presupuesto de error de un mes con incidentes y experimentos según tres políticas de calendario."""
    budget = 43.2  # minutos de caída total al mes para 99,9 %
    policies = {
        "sin experimentos": None,
        "calendario fijo (4 al mes, radio 50 %)": ("fijo", 4, 0.5),
        "con compuerta de presupuesto (radio 5 %)": ("compuerta", 4, 0.05),
    }
    out = {}
    for name, pol in policies.items():
        rng = random.Random(seed)  # mismos incidentes para las tres políticas
        breaches = 0
        spent_inc, spent_exp = [], []
        skipped = 0
        for _ in range(months):
            inc = sum(rng.lognormvariate(math.log(12), 0.9) for _ in range(_poisson(rng, 1.2)))
            exp = 0.0
            if pol:
                kind, count, radius = pol
                for _ in range(count):
                    cost = radius * 20.0 * 0.6  # radio × 20 min × 60 % de peticiones dañadas, en minutos equivalentes de caída total
                    if kind == "compuerta" and (budget - inc - exp) < 0.5 * budget:
                        skipped += 1
                        continue
                    exp += cost
            spent_inc.append(inc)
            spent_exp.append(exp)
            if inc + exp > budget:
                breaches += 1
        out[name] = {"meses que incumplen": breaches / months, "gasto medio en incidentes": st.mean(spent_inc), "gasto medio en experimentos": st.mean(spent_exp), "experimentos omitidos": skipped / months}
    return {"meses": months, "presupuesto min": budget, "politicas": out}


def _poisson(rng: random.Random, lam: float) -> int:
    limit, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= limit:
            return k
        k += 1


@cache
def e513_equidad(seed: int = 5152, tenants: int = 40, experiments: int = 24) -> dict:
    """Quién carga con el daño: muestreo por petición o por cliente."""
    rng = random.Random(seed)
    w = [1 / (i + 1) for i in range(tenants)]
    tot = sum(w)
    share = [x / tot for x in w]
    target = 0.05
    exposed_req = [0.0] * tenants
    exposed_ten = [0.0] * tenants
    for _ in range(experiments):
        for i in range(tenants):
            exposed_req[i] += target  # cada cliente expone la fracción del radio
        order = list(range(tenants))
        rng.shuffle(order)
        acc = 0.0
        for i in order:
            if acc >= target:
                break
            exposed_ten[i] += 1.0
            acc += share[i]
    return {
        "clientes": tenants, "experimentos": experiments, "radio": target,
        "por petición": {"fracción máxima de un cliente": max(exposed_req) / experiments, "clientes con exposición total en algún experimento": 0},
        "por cliente": {"fracción máxima de un cliente": max(exposed_ten) / experiments, "clientes expuestos al menos una vez": sum(1 for x in exposed_ten if x > 0), "clientes nunca expuestos": sum(1 for x in exposed_ten if x == 0), "máximo de veces que un cliente fue el afectado": max(exposed_ten)},
        "cuota del cliente más pequeño": min(share), "cuota del mayor": max(share),
    }


# ---------------------------------------------------------------- SE-516
SPEC_FIELDS = ["id", "hipótesis", "estado_estable", "radio", "aborto", "reversión", "responsable", "ventana", "observabilidad", "aprobación", "comunicación", "evidencia"]


def _valid_spec() -> dict:
    return {
        "id": "CH-2026-014", "hipótesis": "con 20 % de errores en almacenamiento, la API mantiene 99 % de entregas aceptadas",
        "estado_estable": {"métrica": "entregas_aceptadas_ratio", "umbral": 0.99, "ventana_s": 60},
        "radio": {"fracción": 0.05, "duración_s": 600}, "aborto": [{"métrica": "entregas_aceptadas_ratio_grupo", "menor_que": 0.9, "ventana_s": 10}],
        "reversión": "chaosctl stop CH-2026-014", "responsable": "guardia-api", "ventana": "mar-jue 10:00-16:00",
        "observabilidad": "panel-api-entregas", "aprobación": "lider-api", "comunicación": "#api-avisos", "evidencia": "evidence/CH-2026-014.json",
    }


def _form_check(spec: dict) -> list[str]:
    errs = [f"falta {k}" for k in SPEC_FIELDS if not spec.get(k)]
    return errs


def _semantic_check(spec: dict) -> list[str]:
    errs = _form_check(spec)
    if errs:
        return errs
    if not 0 < spec["radio"]["fracción"] <= 0.25:
        errs.append("radio fuera de (0, 25 %]")
    if spec["radio"]["duración_s"] > 1800:
        errs.append("duración mayor de 30 min")
    if not spec["aborto"] or any(a.get("menor_que", 0) <= 0 for a in spec["aborto"]):
        errs.append("aborto sin umbral")
    if spec["aborto"] and spec["aborto"][0]["menor_que"] >= spec["estado_estable"]["umbral"]:
        errs.append("el aborto se dispara antes de salir del estado estable")
    if spec["estado_estable"]["umbral"] <= 0.5:
        errs.append("umbral de estado estable demasiado laxo")
    if not spec["reversión"].startswith("chaosctl"):
        errs.append("reversión no ejecutable")
    return errs


MUTATIONS = {
    "quitar un campo": lambda s, r: s.pop(r.choice(SPEC_FIELDS)),
    "vaciar un campo": lambda s, r: s.__setitem__(r.choice(["id", "hipótesis", "reversión", "responsable", "ventana", "observabilidad", "aprobación", "comunicación", "evidencia"]), ""),
    "radio de 100 %": lambda s, r: s["radio"].__setitem__("fracción", 1.0),
    "duración de 3 h": lambda s, r: s["radio"].__setitem__("duración_s", 10_800),
    "aborto más laxo que el estado estable": lambda s, r: s["aborto"][0].__setitem__("menor_que", 0.995),
    "umbral de estado estable de 0,3": lambda s, r: s["estado_estable"].__setitem__("umbral", 0.3),
    "reversión que no es una orden": lambda s, r: s.__setitem__("reversión", "avisar al equipo"),
    "métrica inexistente": lambda s, r: s["estado_estable"].__setitem__("métrica", "metrica_que_nadie_emite"),
    "hipótesis no falsable": lambda s, r: s.__setitem__("hipótesis", "el sistema es resiliente"),
    "ventana en hora punta": lambda s, r: s.__setitem__("ventana", "vie 14:00-16:00 (cierre de plazo)"),
}


@cache
def e516_validador(mutants: int = 360, seed: int = 516) -> dict:
    rng = random.Random(seed)
    names = list(MUTATIONS)
    valid_form = _form_check(_valid_spec())
    valid_sem = _semantic_check(_valid_spec())
    caught = {n: {"forma": 0, "semántico": 0, "total": 0} for n in names}
    for k in range(mutants):
        name = names[k % len(names)]
        spec = _valid_spec()
        MUTATIONS[name](spec, rng)
        c = caught[name]
        c["total"] += 1
        c["forma"] += bool(_form_check(spec))
        c["semántico"] += bool(_semantic_check(spec))
    totals = {"forma": sum(c["forma"] for c in caught.values()), "semántico": sum(c["semántico"] for c in caught.values()), "mutantes": mutants}
    return {"válida acepta": not valid_form and not valid_sem, "detectadas": caught, "totales": totals}


@cache
def e516_integrado() -> dict:
    """Ejecuta tres experimentos de la especificación válida sobre la configuración E y calcula una huella."""
    results = []
    for name, fault in SUITE[:3]:
        r = simulate(1616, BASE, [fault], duration_s=60.0, rate=RATE, treat_fraction=0.05)
        grp = summarize(r, fault.start + 2, fault.end, treated_only=True)
        ctl = summarize(r, fault.start + 2, fault.end, treated_only=False)
        results.append({"experimento": name, "grupo": round(grp["ok"] + grp["degraded"], 4), "control": round(ctl["ok"] + ctl["degraded"], 4), "n grupo": grp["n"], "n control": ctl["n"]})
    r = simulate(1616, REGRESSIONS["R3 se quita el cortacircuitos"], [SUITE[3][1]], duration_s=60.0, rate=RATE, treat_fraction=0.05)
    grp = summarize(r, SUITE[3][1].start + 2, SUITE[3][1].end, treated_only=True)
    ctl = summarize(r, SUITE[3][1].start + 2, SUITE[3][1].end, treated_only=False)
    results.append({"experimento": "sin respuesta con la regresión R3", "grupo": round(grp["ok"] + grp["degraded"], 4), "control": round(ctl["ok"] + ctl["degraded"], 4), "n grupo": grp["n"], "n control": ctl["n"]})
    payload = json.dumps(results, sort_keys=True, ensure_ascii=False)
    return {"resultados": results, "huella": hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]}


# ---------------------------------------------------------------- SE-511
@cache
def e511_programa(seed: int = 510, runs: int = 300) -> dict:
    """Tres programas de práctica durante dos años con defectos que entran con cada cambio."""
    # tipos de defecto latente y de qué ejercicio dependen para salir a la luz
    kinds = ["alerta ausente", "runbook desactualizado", "alternativa rota", "espera mal configurada", "escalamiento sin respuesta", "permiso faltante"]
    programs = {
        "ninguno": {"gameday_meses": [], "auto_meses": []},
        "un día de práctica al año": {"gameday_meses": [12, 24], "auto_meses": []},
        "día trimestral": {"gameday_meses": list(range(3, 25, 3)), "auto_meses": []},
        "automático mensual y día semestral": {"gameday_meses": [6, 12, 18, 24], "auto_meses": list(range(1, 25))},
    }
    # los experimentos automáticos solo ven defectos técnicos; los días de práctica ven también los humanos
    technical = {"alternativa rota", "espera mal configurada", "permiso faltante"}
    out = {}
    for name, prog in programs.items():
        remaining_end, mean_age, found_total, incidents = [], [], [], []
        for k in range(runs):
            rng = random.Random(seed * 1000 + k)
            latent: list[tuple[int, str]] = []
            ages = []
            found = 0
            inc = 0
            for month in range(1, 25):
                for _ in range(rng.choice([0, 1, 1, 2])):  # cada cambio importante puede introducir defectos
                    latent.append((month, rng.choice(kinds)))
                # un incidente real saca a la luz un defecto latente con probabilidad 8 % por mes y defecto
                still = []
                for born, kind in latent:
                    if rng.random() < 0.06:
                        inc += 1
                        ages.append(month - born)
                        found += 1
                        continue
                    still.append((born, kind))
                latent = still
                if month in prog["gameday_meses"]:
                    still = []
                    for born, kind in latent:
                        if rng.random() < 0.7:
                            ages.append(month - born)
                            found += 1
                        else:
                            still.append((born, kind))
                    latent = still
                if month in prog["auto_meses"]:
                    still = []
                    for born, kind in latent:
                        if kind in technical and rng.random() < 0.8:
                            ages.append(month - born)
                            found += 1
                        else:
                            still.append((born, kind))
                    latent = still
            remaining_end.append(len(latent))
            mean_age.append(st.mean(ages) if ages else 0.0)
            found_total.append(found)
            incidents.append(inc)
        out[name] = {"defectos latentes al final": st.mean(remaining_end), "incidentes reales": st.mean(incidents), "meses medios de un defecto antes de salir": st.mean(mean_age)}
    return {"runs": runs, "programas": out}


EXPERIMENTS = {
    "e511": e511_programa,
    "e512": e512_ci,
    "e513": lambda: {"presupuesto": e513_presupuesto(), "equidad": e513_equidad()},
    "e514": lambda: {"evidencia": e514_evidencia(), "revocacion": e514_revocacion()},
    "e515": lambda: {"region": e515_region(), "concentracion": e515_concentracion()},
    "e516": lambda: {"validador": e516_validador(), "integrado": e516_integrado()},
}

if __name__ == "__main__":
    wanted = sys.argv[1:] or list(EXPERIMENTS)
    print(json.dumps({k: EXPERIMENTS[k]() for k in wanted}, ensure_ascii=False, indent=2, default=str))
