"""Experimentos sintéticos de las clases SE-421 a SE-426 (observabilidad, señales y alertas).

Todo usa la biblioteca estándar, semillas fijas y tiempo virtual. Las cifras no proceden de
ningún sistema real: los servicios, las latencias y los incidentes son construcciones del autor.
Ejecutar ``python scripts/experiments_part35_a.py`` imprime los resultados como JSON.
"""
from __future__ import annotations

import json
from functools import cache
import math
import random
import sys
import tracemalloc
from itertools import combinations

# ---------------------------------------------------------------- utilidades


def pct(values: list[float], q: float) -> float:
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, math.ceil(q / 100 * len(ordered)) - 1))
    return ordered[index]


def poisson(rng: random.Random, lam: float) -> int:
    if lam > 30:
        return max(0, round(rng.gauss(lam, math.sqrt(lam))))
    limit, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= limit:
            return k
        k += 1


# ---------------------------------------------------------------- SE-421
SERVICES = ["pasarela", "api", "base", "almacén"]
SELF_MS = {"pasarela": 6.0, "api": 18.0, "base": 30.0, "almacén": 40.0}


def _request(rng: random.Random, factor: dict[str, float]) -> dict[str, float]:
    own = {s: SELF_MS[s] * factor.get(s, 1.0) * rng.lognormvariate(0, 0.35) for s in SERVICES}
    inclusive = {
        "almacén": own["almacén"],
        "base": own["base"],
        "api": own["api"] + own["base"] + own["almacén"],
    }
    inclusive["pasarela"] = own["pasarela"] + inclusive["api"]
    return inclusive


@cache
def e421_atribucion(seed: int = 421, incidents: int = 200, requests: int = 400) -> dict:
    """Localiza el componente lento con cuatro conjuntos de señales."""
    rng = random.Random(seed)
    baseline = {s: [] for s in SERVICES}
    for _ in range(requests):
        for s, v in _request(rng, {}).items():
            baseline[s].append(v)
    base_p99 = {s: pct(v, 99) for s, v in baseline.items()}
    hits = {"solo borde": 0, "p99 absoluto": 0, "aumento relativo": 0, "aumento relativo sin un servicio": 0}
    for _ in range(incidents):
        faulty = rng.choice(SERVICES)
        k = rng.uniform(3, 8)
        samples = {s: [] for s in SERVICES}
        for _ in range(requests):
            for s, v in _request(rng, {faulty: k}).items():
                samples[s].append(v)
        p99 = {s: pct(v, 99) for s, v in samples.items()}
        rel = {s: p99[s] / base_p99[s] for s in SERVICES}
        hits["solo borde"] += rng.choice(SERVICES) == faulty
        hits["p99 absoluto"] += max(p99, key=p99.get) == faulty
        hits["aumento relativo"] += max(rel, key=rel.get) == faulty
        hidden = rng.choice(SERVICES)
        visible = {s: rel[s] for s in SERVICES if s != hidden}
        hits["aumento relativo sin un servicio"] += max(visible, key=visible.get) == faulty
    return {"incidentes": incidents, "aciertos": hits}


@cache
def e421_segmento(seed: int = 4211, tenants: int = 40, minutes: int = 60, rpm: int = 2000) -> dict:
    """Una falla que afecta a un solo cliente: umbral global frente a sondas."""
    rng = random.Random(seed)
    weights = [1 / (i + 1) for i in range(tenants)]
    total = sum(weights)
    share = [w / total for w in weights]
    out = {}
    for name, idx in (("cliente grande (puesto 1)", 0), ("cliente mediano (puesto 10)", 9), ("cliente pequeño (puesto 40)", 39)):
        detected = {"tasa global > 1 % en 5 min": [], "sonda fija en el cliente 1": [], "sonda rotativa": []}
        for trial in range(300):
            first = {k: None for k in detected}
            window: list[int] = []
            for minute in range(minutes):
                window.append(poisson(rng, rpm * 0.001) + poisson(rng, rpm * share[idx]))
                window = window[-5:]
                if first["tasa global > 1 % en 5 min"] is None and sum(window) / (rpm * len(window)) > 0.01:
                    first["tasa global > 1 % en 5 min"] = minute
                if first["sonda fija en el cliente 1"] is None and idx == 0:
                    first["sonda fija en el cliente 1"] = minute
                if first["sonda rotativa"] is None and minute % tenants == idx:
                    first["sonda rotativa"] = minute
            for k, v in first.items():
                detected[k].append(v)
        out[name] = {
            "cuota de tráfico %": round(share[idx] * 100, 2),
            **{k: sum(1 for v in vs if v is not None) / len(vs) for k, vs in detected.items()},
        }
    return out


@cache
def e421_preguntas(seed: int = 4212) -> dict:
    """Preguntas posteriores al incidente que cada diseño de señales puede responder."""
    rng = random.Random(seed)
    dims = {"endpoint": 5, "estado": 3, "región": 3, "curso": 30, "cliente": 40, "versión": 4, "tipo de dispositivo": 3, "plan": 2}
    metrics_dims = {"endpoint", "estado", "región"}
    names = list(dims)
    questions = [set(rng.sample(names, rng.choice([1, 2, 2, 3]))) for _ in range(60)]
    answerable = sum(1 for q in questions if q <= metrics_dims)
    sample_event = {
        "ts": "2026-11-15T14:03:22.114Z", "service": "api", "endpoint": "POST /entregas", "status": 201,
        "region": "sa-east", "course_id": 17, "tenant_id": 23, "version": "2026.11.2", "device": "movil",
        "plan": "pro", "duration_ms": 83, "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736", "bytes": 18211,
    }
    series_all = math.prod(dims.values())
    series_predef = math.prod(dims[d] for d in metrics_dims)
    return {
        "preguntas": len(questions), "métricas previstas": sorted(metrics_dims), "responde métricas": answerable,
        "responde eventos anchos": len(questions),
        "series por métrica previstas": series_predef, "series para todas las combinaciones": series_all,
        "bytes por evento": len(json.dumps(sample_event, ensure_ascii=False, separators=(",", ":"))),
        "peticiones por día": 1_000_000,
    }


# ---------------------------------------------------------------- SE-422
V1 = "Entrega {id} aceptada para curso {c} en {ms} ms"
TEXT = [
    "Entrega {id} aceptada para curso {c} en {ms} ms",
    "Entrega aceptada: id={id} curso={c} duración={ms}ms",
    "[api] entrega id={id} (curso {c}) OK tiempo={ms} milisegundos",
    "Submission {id} accepted for course {c} in {ms} ms",
]
JSON_KEYS = [
    ("id", "curso", "ms"), ("id", "curso", "ms"), ("id", "curso", "ms", "region"), ("id", "curso", "duration_ms"),
]


@cache
def e422_formato(seed: int = 422, lines: int = 1500) -> dict:
    import re

    rng = random.Random(seed)
    pattern = re.compile(r"Entrega (\d+) aceptada para curso (\d+) en (\d+) ms")
    rows = []
    for version in range(4):
        regex_ok = json_ok = 0
        for _ in range(lines):
            rec = {"id": rng.randint(1, 10**6), "c": rng.randint(1, 60), "ms": rng.randint(20, 900)}
            text = TEXT[version].format(**rec)
            if pattern.search(text):
                regex_ok += 1
            keys = JSON_KEYS[version]
            record = {keys[0]: rec["id"], keys[1]: rec["c"], keys[2]: rec["ms"]}
            if len(keys) == 4:
                record[keys[3]] = "sa-east"
            parsed = json.loads(json.dumps(record))
            if {"id", "curso", "ms"} <= parsed.keys():
                json_ok += 1
        rows.append({"versión": version + 1, "regex v1": regex_ok / lines, "json por nombre": json_ok / lines})
    return {"líneas por versión": lines, "filas": rows}


@cache
def e422_correlacion(seed: int = 4221) -> dict:
    rng = random.Random(seed)
    hops = 5
    out = {"propagación": [], "huérfanas": []}
    for p in (0.99, 0.95, 0.90, 0.80):
        complete = sum(all(rng.random() < p for _ in range(hops - 1)) for _ in range(20000)) / 20000
        out["propagación"].append({"p por salto": p, "completas simuladas": round(complete, 4), "p^4": round(p ** 4, 4)})
    for rps in (1, 2, 5, 20, 100):
        starts, t = [], 0.0
        for _ in range(3000):
            t += rng.expovariate(rps)
            starts.append(t)
        unique = 0
        left = 0
        for i, s in enumerate(starts):
            while starts[left] < s - 0.25:
                left += 1
            right = i
            while right + 1 < len(starts) and starts[right + 1] <= s + 0.25:
                right += 1
            unique += (right - left + 1) == 1
        out["huérfanas"].append({"solicitudes por segundo": rps, "atribuibles de forma única": round(unique / len(starts), 4)})
    return out


@cache
def e422_politicas(seed: int = 4222) -> dict:
    import re

    rng = random.Random(seed)
    event = {"ts": "2026-11-15T14:03:22.114Z", "level": "INFO", "service": "api", "msg": "entrega aceptada", "course_id": 17,
             "request_id": "9f1c2a7e4b8d4c0e", "duration_ms": 83, "status": 201}
    text_line = "2026-11-15T14:03:22.114Z INFO api entrega aceptada course_id=17 request_id=9f1c2a7e4b8d4c0e duration_ms=83 status=201"
    json_line = json.dumps(event, ensure_ascii=False, separators=(",", ":"))
    # muestreo de logs
    total, errors = 200000, 0
    kept_head = kept_err_head = kept_smart = 0
    for _ in range(total):
        is_err = rng.random() < 0.02
        errors += is_err
        take = rng.random() < 0.10
        kept_head += take
        kept_err_head += take and is_err
        kept_smart += is_err or take
    # redacción de datos personales
    emails = ["ana.perez@example.com", "ANA.PEREZ@EXAMPLE.COM", "ana.perez+curso@example.com", "ana . perez @ example.com", "ana.perez [arroba] example.com"]
    tokens = ["tok_" + "".join(rng.choice("abcdef0123456789") for _ in range(24)) for _ in range(5)]
    docs = ["12.345.678-5", "12345678-5", "12 345 678 5", "123456785", "12.345.678–5"]
    variants = [(e, "correo") for e in emails] + [(t, "token") for t in tokens] + [(d, "documento") for d in docs]
    rx = {
        "correo": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}"),
        "token": re.compile(r"tok_[a-f0-9]{24}"),
        "documento": re.compile(r"\b\d{1,2}\.\d{3}\.\d{3}-[\dkK]\b"),
    }
    caught = {k: [0, 0] for k in rx}
    for value, kind in variants:
        for _ in range(20):
            caught[kind][1] += 1
            caught[kind][0] += bool(rx[kind].search(f"usuario escribió {value} en el formulario"))
    return {
        "bytes texto": len(text_line.encode()), "bytes json": len(json_line.encode()),
        "líneas": total, "errores": errors, "retenidas 10 %": kept_head, "errores con 10 %": kept_err_head,
        "retenidas errores+10 %": kept_smart, "redacción": {k: v for k, v in caught.items()},
    }


# ---------------------------------------------------------------- SE-423
@cache
def e423_cardinalidad() -> dict:
    steps = [("endpoint × estado × región", 5 * 3 * 3), ("+ curso (30)", 5 * 3 * 3 * 30), ("+ cliente (40)", 5 * 3 * 3 * 30 * 40),
             ("+ identificador de persona (20 000)", 5 * 3 * 3 * 30 * 40 * 20000)]
    tracemalloc.start()
    store: dict[tuple, list[float]] = {}
    base = tracemalloc.get_traced_memory()[0]
    for i in range(54000):
        store[("api", "e%d" % (i % 5), "r%d" % (i % 3), "c%d" % (i % 30), "t%d" % (i % 40), "p%d" % i)] = [0.0, 0.0]
    used = tracemalloc.get_traced_memory()[0] - base
    tracemalloc.stop()
    return {"escalones": steps, "bytes por serie (medido)": round(used / 54000)}


@cache
def e423_contadores(seed: int = 423) -> dict:
    rng = random.Random(seed)
    rate, horizon = 100, 600
    resets = [137, 301, 452]
    truth, value, series = 0, 0, {}
    for t in range(horizon + 1):
        if t in resets:
            value = 0
        n = poisson(rng, rate)
        truth += n
        value += n
        series[t] = value
    out = {"verdad": truth, "intervalos": []}
    for step in (15, 60):
        points = [series[t] for t in range(0, horizon + 1, step)]
        naive = points[-1] - points[0]
        aware = sum((b - a) if b >= a else b for a, b in zip(points, points[1:]))
        out["intervalos"].append({"scrape s": step, "diferencia ingenua": naive, "con reinicios": aware})
    spikes = {}
    for dur in (5, 20, 60):
        row = {}
        for interval in (15, 60, 300):
            seen = 0
            for _ in range(3000):
                start = rng.uniform(0, 3600)
                first = math.ceil(start / interval) * interval
                seen += first <= start + dur
            row[interval] = seen / 3000
        spikes[dur] = row
    out["picos"] = spikes
    return out


@cache
def e423_histogramas(seed: int = 4231, n: int = 100000) -> dict:
    rng = random.Random(seed)
    data = [rng.lognormvariate(math.log(0.12), 0.7) for _ in range(n)]
    layouts = {
        "lineal 100 ms": [0.1 * i for i in range(1, 21)],
        "exponencial ×2": [0.005 * 2 ** i for i in range(0, 10)],
        "por defecto (.005–10 s)": [.005, .01, .025, .05, .1, .25, .5, 1, 2.5, 5, 10],
    }
    out = {"verdad": {q: round(pct(data, q) * 1000, 1) for q in (50, 95, 99)}, "diseños": {}}
    for name, bounds in layouts.items():
        counts = [0] * (len(bounds) + 1)
        for x in data:
            lo, hi = 0, len(bounds)
            while lo < hi:
                mid = (lo + hi) // 2
                if x <= bounds[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            counts[lo] += 1
        row = {}
        for q in (50, 95, 99):
            target, acc = q / 100 * n, 0
            for i, c in enumerate(counts):
                if acc + c >= target:
                    low = bounds[i - 1] if i else 0.0
                    high = bounds[i] if i < len(bounds) else bounds[-1]
                    est = low + (high - low) * ((target - acc) / c if c else 0)
                    row[q] = round(est * 1000, 1)
                    break
                acc += c
        out["diseños"][name] = row
    return out


# ---------------------------------------------------------------- SE-424
def traceparent(rng: random.Random) -> str:
    return "00-%032x-%016x-01" % (rng.getrandbits(128) or 1, rng.getrandbits(64) or 1)


def valid_traceparent(value: str) -> bool:
    import re

    return bool(re.fullmatch(r"00-(?!0{32})[0-9a-f]{32}-(?!0{16})[0-9a-f]{16}-[0-9a-f]{2}", value))


@cache
def e424_contexto(seed: int = 424) -> dict:
    rng = random.Random(seed)
    boundaries = [("HTTP síncrono", 0.01), ("cola de mensajes", 0.15), ("grupo de hilos", 0.20), ("reintento automático", 0.10)]
    chain = ["http", "http", "cola", "hilos", "http", "reintento"]
    probs = {"http": 0.01, "cola": 0.15, "hilos": 0.20, "reintento": 0.10}
    trials = 5000
    full = frag = 0
    pieces = []
    for _ in range(trials):
        parts = 1
        for b in chain:
            if rng.random() < probs[b]:
                parts += 1
        pieces.append(parts)
        full += parts == 1
    mutated = 0
    base = traceparent(rng)
    variants = [base.upper(), base[:-3], "00-" + "0" * 32 + base[35:], base.replace("00-", "01-", 1), base + "-x", base.replace("-", "_"),
                "00-%s-%s-01" % ("g" * 32, "a" * 16), "00-%s-%s-01" % ("a" * 31, "b" * 16), " " + base]
    accepted = sum(valid_traceparent(v) for v in variants)
    valid_variants = [base[:-2] + "00", base[:-2] + "03"]
    valid_ok = sum(valid_traceparent(v) for v in valid_variants)
    return {"salto": boundaries, "completas": full / trials, "trozos por petición": sum(pieces) / trials,
            "máximo de trozos": max(pieces), "traceparent válido": valid_traceparent(base),
            "inválidas aceptadas": accepted, "inválidas": len(variants), "válidas aceptadas": valid_ok, "válidas": len(valid_variants)}


def _tree(rng: random.Random, depth: int = 0):
    node = {"self": rng.lognormvariate(math.log(15), 0.9), "par": rng.random() < 0.5, "kids": []}
    if depth < 3:
        for _ in range(rng.choice([0, 2, 3, 4]) if depth else rng.choice([3, 4, 5])):
            node["kids"].append(_tree(rng, depth + 1))
    return node


def _lat(n: dict) -> float:
    if not n["kids"]:
        return n["self"]
    ks = [_lat(k) for k in n["kids"]]
    return n["self"] + (max(ks) if n["par"] else sum(ks))


def _nodes(n: dict, on_path: bool, out: list) -> None:
    out.append((n, on_path))
    if not n["kids"]:
        return
    lats = [_lat(k) for k in n["kids"]]
    top = lats.index(max(lats))
    for i, k in enumerate(n["kids"]):
        _nodes(k, on_path and (not n["par"] or i == top), out)


@cache
def e424_ruta_critica(seed: int = 4241, trees: int = 600) -> dict:
    rng = random.Random(seed)
    names = ["un span al azar", "el span con más tiempo propio", "el span de la ruta crítica con más tiempo propio"]
    totals = {k: 0.0 for k in names}
    zero = {k: 0 for k in names}
    base_total = 0.0
    for _ in range(trees):
        tree = _tree(rng)
        nodes: list = []
        _nodes(tree, True, nodes)
        base = _lat(tree)
        base_total += base
        for key in names:
            if key == names[0]:
                target = rng.choice(nodes)[0]
            elif key == names[1]:
                target = max(nodes, key=lambda x: x[0]["self"])[0]
            else:
                target = max((x for x in nodes if x[1]), key=lambda x: x[0]["self"])[0]
            before = target["self"]
            target["self"] *= 0.5
            saving = base - _lat(tree)
            target["self"] = before
            totals[key] += saving
            zero[key] += saving < 1e-9
    return {"árboles": trees, "latencia media ms": round(base_total / trees, 1),
            "ahorro medio ms": {k: round(v / trees, 1) for k, v in totals.items()},
            "sin ahorro %": {k: round(100 * v / trees, 1) for k, v in zero.items()}}


@cache
def e424_muestreo(seed: int = 4242, traces: int = 100000) -> dict:
    rng = random.Random(seed)
    kinds = []
    for _ in range(traces):
        r = rng.random()
        kinds.append("error" if r < 0.01 else "lenta" if r < 0.03 else "normal")
    head = {"error": 0, "lenta": 0, "normal": 0}
    tail = {"error": 0, "lenta": 0, "normal": 0}
    for k in kinds:
        head[k] += rng.random() < 0.01
        tail[k] += k != "normal" or rng.random() < 0.01
    counts = {k: kinds.count(k) for k in head}
    routing = {}
    for collectors in (1, 2, 4):
        random_ok = hashed_ok = 0
        interesting = 2000
        for _ in range(interesting):
            spans = [rng.randrange(collectors) for _ in range(7)]
            random_ok += len(set(spans)) == 1
            hashed_ok += 1
        routing[collectors] = {"completas con enrutado aleatorio": random_ok / interesting, "completas con hash del trace": hashed_ok / interesting}
    return {"trazas": traces, "recuento": counts, "cabeza 1 %": head, "cola": tail,
            "almacenadas cabeza": sum(head.values()), "almacenadas cola": sum(tail.values()), "enrutado": routing}


# ---------------------------------------------------------------- SE-425
@cache
def e425_trafico() -> dict:
    # tráfico por minuto: 5 por segundo de noche, 100 de día, 30 días
    def rps(minute_of_day: int) -> float:
        hour = minute_of_day / 60
        return 5 + 95 * max(0.0, math.sin(math.pi * (hour - 6) / 14)) if 6 <= hour <= 20 else 5.0

    day_requests = sum(rps(m) * 60 for m in range(1440))
    month_requests = day_requests * 30
    out = {"peticiones por mes": round(month_requests), "escenarios": []}
    scenarios = [("corte total de 30 min a las 03:00", 180, 30, 1.0), ("corte total de 30 min a las 14:00", 840, 30, 1.0),
                 ("5 % de errores durante 8 h desde las 09:00", 540, 480, 0.05)]
    for name, start, dur, err in scenarios:
        bad = sum(rps(m) * 60 * err for m in range(start, start + dur))
        by_requests = bad / month_requests
        bad_minutes = dur if err >= 0.01 else 0
        by_time = bad_minutes / (30 * 1440)
        out["escenarios"].append({"nombre": name, "disponibilidad por peticiones %": round(100 * (1 - by_requests), 4),
                                  "presupuesto gastado por peticiones %": round(100 * by_requests / 0.001, 1),
                                  "presupuesto gastado por minutos %": round(100 * by_time / 0.001, 1)})
    return out


@cache
def e425_donde_se_mide(seed: int = 4251) -> dict:
    rng = random.Random(seed)
    n = 200000
    server_ok = client_ok = retry_indep = retry_real = 0
    for _ in range(n):
        persistent = rng.random() < 0.0003
        fails = [rng.random() < 0.02 or rng.random() < 0.0005 for _ in range(3)]
        server_ok += not (rng.random() < 0.0005 or persistent)
        client_ok += not (fails[0] or persistent)
        retry_indep += not all(fails)
        retry_real += (not persistent) and not all(fails)
    return {"solicitudes": n, "servidor %": round(100 * server_ok / n, 3), "cliente por intento %": round(100 * client_ok / n, 3),
            "3 intentos si todo fuera independiente %": round(100 * retry_indep / n, 4), "3 intentos con fallos pegados %": round(100 * retry_real / n, 4)}


@cache
def e425_composicion(seed: int = 4252, months: int = 20000) -> dict:
    rng = random.Random(seed)
    serie = {f"{k} dependencias de 99,9 %": round(0.999 ** k * 100, 3) for k in (1, 3, 5, 8)}
    out = {"serie": serie, "meses": months}
    for label, mttr in (("duración mediana 20 min", 20.0), ("duración mediana 10 min", 10.0)):
        slo = sla = 0
        mean_down = 0.0
        for _ in range(months):
            incidents = poisson(rng, 1.2)
            down = sum(rng.lognormvariate(math.log(mttr), 1.0) for _ in range(incidents))
            mean_down += down
            slo += down > 43.2
            sla += down > 216
        out[label] = {"incumple SLO 99,9 %": round(100 * slo / months, 1), "incumple SLA 99,5 %": round(100 * sla / months, 2),
                      "minutos medios caídos": round(mean_down / months, 1)}
    return out


# ---------------------------------------------------------------- SE-426
BURN = [(14.4, 60, 5), (6.0, 360, 30)]


def _traffic(minute: int) -> float:
    hour = (minute % 1440) / 60
    return 30 + 270 * max(0.0, math.sin(math.pi * (hour - 6) / 14)) if 6 <= hour <= 20 else 30.0


def _day_series(rng: random.Random, days: int):
    minutes = days * 1440
    base = 0.001
    incidents = []
    for _ in range(14):
        incidents.append((rng.randrange(0, minutes - 400), rng.choice([8, 15, 30, 60, 180]), rng.choice([0.03, 0.10, 0.5, 1.0]), "caída"))
    for _ in range(12):
        incidents.append((rng.randrange(0, minutes - 800), rng.choice([240, 360, 600]), rng.choice([0.004, 0.006, 0.008]), "degradación lenta"))
    prob = [base] * minutes
    for s, d, p, _ in incidents:
        for m in range(s, s + d):
            prob[m] = max(prob[m], p)
    traffic = [_traffic(m) for m in range(minutes)]
    errors = [poisson(rng, traffic[m] * prob[m]) for m in range(minutes)]
    return traffic, errors, incidents


@cache
def e426_reglas(seed: int = 426, days: int = 180) -> dict:
    rng = random.Random(seed)
    traffic, errors, incidents = _day_series(rng, days)
    minutes = len(errors)
    cum, cumt = [0], [0.0]
    for e, t in zip(errors, traffic):
        cum.append(cum[-1] + e)
        cumt.append(cumt[-1] + t)

    def ratio(m: int, w: int) -> float:
        a = max(0, m - w + 1)
        return (cum[m + 1] - cum[a]) / (cumt[m + 1] - cumt[a])

    rules = {
        "umbral 0,5 % en 1 min": lambda m: ratio(m, 1) > 0.005,
        "umbral 1 % en 5 min": lambda m: ratio(m, 5) > 0.01,
        "umbral 1 % en 30 min": lambda m: ratio(m, 30) > 0.01,
        "consumo 14,4× (1 h y 5 min)": lambda m: ratio(m, 60) > 14.4 * 0.001 and ratio(m, 5) > 14.4 * 0.001,
        "consumo 6× (6 h y 30 min)": lambda m: ratio(m, 360) > 6 * 0.001 and ratio(m, 30) > 6 * 0.001,
    }
    rules["consumo 14,4× o 6×"] = lambda m: rules["consumo 14,4× (1 h y 5 min)"](m) or rules["consumo 6× (6 h y 30 min)"](m)
    spans = [(s, s + d + 30) for s, d, _, _ in incidents]
    out = {"días": days, "incidentes": len(incidents), "reglas": []}
    for name, fn in rules.items():
        pages, firing = [], False
        for m in range(minutes):
            on = fn(m)
            if on and not firing:
                pages.append(m)
            firing = on
        detected, delays = {"caída": 0, "degradación lenta": 0}, []
        for s, d, p, kind in incidents:
            hit = [m for m in pages if s <= m <= s + d + 30]
            if hit:
                detected[kind] += 1
                delays.append(hit[0] - s)
        false = sum(1 for m in pages if not any(a <= m <= b for a, b in spans))
        out["reglas"].append({"regla": name, "páginas": len(pages), "caídas detectadas": detected["caída"],
                              "degradaciones detectadas": detected["degradación lenta"],
                              "retraso mediano min": sorted(delays)[len(delays) // 2] if delays else None,
                              "páginas sin incidente": false})
    out["caídas"] = sum(1 for i in incidents if i[3] == "caída")
    out["degradaciones"] = sum(1 for i in incidents if i[3] != "caída")
    return out


@cache
def e426_ruido(seed: int = 4261) -> dict:
    rng = random.Random(seed)
    blips, incidents = 3000, 200
    cascade = [1 + rng.randrange(0, 15) for _ in range(incidents)]
    surviving = sum(rng.random() < 0.04 for _ in range(blips))
    raw = blips + sum(k * 3 for k in cascade)
    duration_filter = sum(cascade) + surviving
    grouped = incidents + surviving
    return {"destellos": blips, "incidentes": incidents, "alertas por incidente (media)": round(sum(cascade) / incidents, 1),
            "páginas sin filtros": raw, "con duración mínima": duration_filter, "con duración y agrupación": grouped,
            "accionables sin filtros %": round(100 * incidents / raw, 1), "accionables agrupadas %": round(100 * incidents / grouped, 1)}


@cache
def e426_ventanas(seed: int = 4262, days: int = 120) -> dict:
    rng = random.Random(seed)
    traffic = 100
    minutes = days * 1440
    errors = [poisson(rng, traffic * 0.001) for _ in range(minutes)]
    cum = [0]
    for e in errors:
        cum.append(cum[-1] + e)
    out = []
    for w in (1, 5, 15, 60):
        noise, firing = 0, False
        for m in range(w - 1, minutes):
            on = (cum[m + 1] - cum[m + 1 - w]) / (traffic * w) > 0.01
            noise += on and not firing
            firing = on
        row = {"ventana min": w, "falsos positivos por día": round(noise / days, 2)}
        for label, p in (("2 % de errores", 0.02), ("10 % de errores", 0.10), ("100 % de errores", 1.0)):
            delays = []
            for _ in range(300):
                acc = [poisson(rng, traffic * 0.001) for _ in range(w)]
                for minute in range(1, 400):
                    acc.append(poisson(rng, traffic * (p + 0.001)))
                    if sum(acc[-w:]) / (traffic * w) > 0.01:
                        delays.append(minute)
                        break
                else:
                    delays.append(None)
            seen = sorted(d for d in delays if d is not None)
            row[label] = seen[len(seen) // 2] if seen else None
        out.append(row)
    return {"filas": out}


def results() -> dict:
    return {
        "e421_atribucion": e421_atribucion(), "e421_segmento": e421_segmento(), "e421_preguntas": e421_preguntas(),
        "e422_formato": e422_formato(), "e422_correlacion": e422_correlacion(), "e422_politicas": e422_politicas(),
        "e423_cardinalidad": e423_cardinalidad(), "e423_contadores": e423_contadores(), "e423_histogramas": e423_histogramas(),
        "e424_contexto": e424_contexto(), "e424_ruta_critica": e424_ruta_critica(), "e424_muestreo": e424_muestreo(),
        "e425_trafico": e425_trafico(), "e425_donde": e425_donde_se_mide(), "e425_composicion": e425_composicion(),
        "e426_reglas": e426_reglas(), "e426_ruido": e426_ruido(), "e426_ventanas": e426_ventanas(),
    }


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(json.dumps({k: v for k, v in results().items() if k.startswith(sys.argv[1])}, ensure_ascii=False, indent=1))
    else:
        print(json.dumps(results(), ensure_ascii=False, indent=1))
