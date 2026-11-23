"""Experimentos de las clases SE-507 a SE-511 (ingeniería del caos: demostrar, medir, diseñar e inyectar).

Casi todo corre en tiempo virtual con ``experiments_part42_sim`` y semillas fijas: no hay reloj, red ni
servidor reales. La excepción es ``e509_proxy_real``, que mide sockets reales en la máquina local.
Ejecutar ``python scripts/experiments_part42_a.py`` imprime los resultados como JSON.
"""
from __future__ import annotations

import json
import math
import random
import socket
import statistics as st
import sys
import threading
import time
from functools import cache
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from experiments_part42_sim import Fault, Policy, pct, simulate, summarize

# Configuraciones del cliente de la API de entregas (todas «declaran» resiliencia).
CONFIGS = {
    "A": ("Solo espera de 5 s", Policy(timeout_ms=5000, retries=0)),
    "B": ("Espera de 1 s y 3 reintentos sin pausa", Policy(timeout_ms=1000, retries=3, backoff="none")),
    "C": ("Espera corta y reintentos con pausa y azar", Policy(timeout_ms=250, retries=2, backoff="exp_jitter", backoff_ms=50)),
    "D": ("C con cortacircuitos sensible y alternativa", Policy(timeout_ms=250, retries=2, backoff="exp_jitter", backoff_ms=50, breaker=(0.5, 20, 5000), fallback=True)),
    "E": ("C con cortacircuitos calibrado y alternativa", Policy(timeout_ms=250, retries=2, backoff="exp_jitter", backoff_ms=50, breaker=(0.8, 50, 5000), fallback=True)),
}
FAULTS = {
    "red +100 ms": [Fault("net_latency", 30, 60, 100)],
    "dependencia lenta +100 ms": [Fault("slow", 30, 60, 100)],
    "30 % de errores": [Fault("error", 30, 60, 0.3)],
    "mitad de los hilos": [Fault("capacity", 30, 60, 0.5)],
    "sin respuesta": [Fault("blackhole", 30, 60, 1.0)],
    "proceso caído 12 s": [Fault("capacity", 30, 42, 1.0)],
}
SEEDS = (1, 2, 3)
RATE = 90.0


# ---------------------------------------------------------------- SE-507
@cache
def e507_declarada() -> dict:
    """Seis fallas contra cinco configuraciones que declaran resiliencia."""
    out: dict = {"tasa": RATE, "semillas": len(SEEDS), "configs": {k: v[0] for k, v in CONFIGS.items()}, "fallas": list(FAULTS), "celdas": {}}
    for ck, (_, policy) in CONFIGS.items():
        for fn, faults in FAULTS.items():
            ok, resp, after, att = [], [], [], []
            for seed in SEEDS:
                r = simulate(seed, policy, faults, duration_s=120.0, rate=RATE)
                end = faults[0].end
                inside = summarize(r, faults[0].start + 2, end)
                post = summarize(r, end + 20, 120.0)
                ok.append(inside["ok"])
                resp.append(inside["ok"] + inside["degraded"])
                after.append(post["ok"])
                att.append(inside["attempts"])
            out["celdas"][f"{ck}|{fn}"] = {"ok": st.mean(ok), "responde": st.mean(resp), "despues": st.mean(after), "intentos": st.mean(att)}
    verdict = {}
    for ck in CONFIGS:
        passed = sum(1 for fn in FAULTS if out["celdas"][f"{ck}|{fn}"]["responde"] >= 0.99 and out["celdas"][f"{ck}|{fn}"]["despues"] >= 0.99)
        verdict[ck] = passed
    out["superadas"] = verdict
    out["superadas con calidad"] = {ck: sum(1 for fn in FAULTS if out["celdas"][f"{ck}|{fn}"]["ok"] >= 0.95 and out["celdas"][f"{ck}|{fn}"]["despues"] >= 0.99) for ck in CONFIGS}
    return out


@cache
def e507_serie() -> dict:
    """Serie temporal de la fracción de peticiones correctas con la falla «mitad de los hilos» (30 a 60 s)."""
    out = {}
    for ck in ("A", "C", "E"):
        r = simulate(1, CONFIGS[ck][1], FAULTS["mitad de los hilos"], duration_s=120.0, rate=RATE)
        out[ck] = [(a + 5, summarize(r, a, a + 10)["ok"]) for a in range(0, 110, 10)]
    return {"serie": out, "ventana s": 10}


# ---------------------------------------------------------------- SE-505
def _sli_fast(res, a: float, b: float, thr_ms: float = 120.0) -> float:
    idx = [i for i, t in enumerate(res.t0) if a <= t < b]
    if not idx:
        return float("nan")
    return sum(1 for i in idx if res.outcome[i] == "ok" and res.latency[i] <= thr_ms) / len(idx)


@cache
def e505_estado_estable(reps: int = 24) -> dict:
    """Cuánto ruido tiene el estado estable y cuántas refutaciones falsas produce cada regla."""
    policy = CONFIGS["E"][1]
    base_faults = [Fault("error", 0, 1e9, 0.004)]
    lengths = (5, 15, 30, 60, 120)
    windows: dict[int, list[float]] = {w: [] for w in lengths}
    runs = []
    for seed in range(100, 100 + reps):
        runs.append(simulate(seed, policy, base_faults, duration_s=240.0, rate=RATE, sigma=0.6))
    for r in runs:
        for w in lengths:
            for a in range(0, 240 - w + 1, w):
                windows[w].append(_sli_fast(r, a, a + w))
    stats = {}
    for w in lengths:
        v = windows[w]
        stats[w] = {"media": st.mean(v), "desv": st.pstdev(v), "p1": pct(v, 1), "n": len(v)}
    # reglas de refutación evaluadas sobre ventanas sanas (A/A) y con efecto real (A/B)
    effect = [Fault("slow", 0, 1e9, 4.0)]  # la dependencia añade 4 ms al servicio de 40 ms
    degraded = [simulate(seed, policy, base_faults + effect, duration_s=240.0, rate=RATE, sigma=0.6) for seed in range(200, 200 + reps)]
    rules = {}
    ref_w = 60
    mu, sd = stats[ref_w]["media"], stats[ref_w]["desv"]
    for w in lengths:
        mu_w, sd_w = stats[w]["media"], stats[w]["desv"]
        deg_windows = [_sli_fast(r, a, a + w) for r in degraded for a in range(0, 240 - w + 1, w)]
        rules[w] = {
            "falsa «menor que la media»": sum(1 for x in windows[w] if x < mu_w) / len(windows[w]),
            "falsa «menor que media menos 3 desv»": sum(1 for x in windows[w] if x < mu_w - 3 * sd_w) / len(windows[w]),
            "falsa «menor que el SLO de 0,96»": sum(1 for x in windows[w] if x < 0.96) / len(windows[w]),
            "detecta «menor que media menos 3 desv»": sum(1 for x in deg_windows if x < mu_w - 3 * sd_w) / len(deg_windows),
            "detecta «menor que el SLO de 0,96»": sum(1 for x in deg_windows if x < 0.96) / len(deg_windows),
        }
    base_mean = st.mean(windows[60])
    deg_mean = st.mean(_sli_fast(r, 0, 240) for r in degraded)
    return {"tasa": RATE, "estado estable": stats, "reglas": rules, "sli base": base_mean, "sli con efecto": deg_mean, "ventanas": {w: len(windows[w]) for w in lengths}, "referencia": {"media": mu, "desv": sd}}


# ---------------------------------------------------------------- SE-506
def _ztest_p(k1: int, n1: int, k0: int, n0: int) -> float:
    if n1 == 0 or n0 == 0:
        return 1.0
    p = (k1 + k0) / (n1 + n0)
    if p in (0.0, 1.0):
        return 1.0
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n0))
    z = abs(k1 / n1 - k0 / n0) / se
    return math.erfc(z / math.sqrt(2))


@cache
def e506_radio(reps: int = 60) -> dict:
    """Radio de explosión: cuánta gente se daña frente a la capacidad de detectar un efecto."""
    policy = Policy(timeout_ms=250, retries=0)
    fractions = (0.005, 0.01, 0.02, 0.05, 0.1, 0.25, 0.5)
    fault = [Fault("error", 0, 60, 0.05)]  # el efecto a detectar es pequeño: un 5 % de errores
    rows = []
    for f in fractions:
        detected = 0
        harmed = []
        for seed in range(300, 300 + reps):
            r = simulate(seed, policy, fault, duration_s=60.0, rate=RATE, treat_fraction=f)
            k1 = sum(1 for i in range(len(r.t0)) if r.treated[i] and r.outcome[i] != "ok")
            n1 = sum(1 for i in range(len(r.t0)) if r.treated[i])
            k0 = sum(1 for i in range(len(r.t0)) if not r.treated[i] and r.outcome[i] != "ok")
            n0 = sum(1 for i in range(len(r.t0)) if not r.treated[i])
            if k1 / max(1, n1) > k0 / max(1, n0) and _ztest_p(k1, n1, k0, n0) < 0.01:
                detected += 1
            harmed.append(k1 - 0.0 * k0)
        rows.append({"fracción": f, "detecta": detected / reps, "peticiones falladas": st.mean(harmed)})
    # Condiciones de aborto ante una sorpresa: a los 60 s la falla pasa de 20 % de errores a 100 %.
    surprise = [Fault("error", 0, 60, 0.2), Fault("error", 60, 300, 1.0)]
    abort = {}
    for f in (0.005, 0.02, 0.1, 0.5):
        r = simulate(7, policy, surprise, duration_s=300.0, rate=RATE, treat_fraction=f)
        times = [(r.t0[i], r.outcome[i] != "ok", r.treated[i]) for i in range(len(r.t0))]

        def failed_until(t_end: float) -> int:
            return sum(1 for t, bad, tr in times if tr and bad and t < t_end)

        def first_time(rule) -> float | None:
            for t in range(10, 300, 5):
                if rule(t):
                    return float(t)
            return None

        def global_rule(t):  # SLO global: más de 1 % de peticiones falladas en los últimos 10 s sobre todo el tráfico
            win = [bad for tt, bad, _ in times if t - 10 <= tt < t]
            return len(win) >= 50 and sum(win) / len(win) > 0.01

        def group_rule(t):  # grupo experimental: más de 50 % de falladas en 10 s
            win = [bad for tt, bad, tr in times if t - 10 <= tt < t and tr]
            return len(win) >= 20 and sum(win) / len(win) > 0.5

        def budget_rule(t):  # presupuesto absoluto de peticiones dañadas
            return failed_until(t) >= 300

        res = {}
        for name, rule in (("sin aborto", lambda t: False), ("SLO global", global_rule), ("grupo experimental", group_rule), ("presupuesto de 300 peticiones", budget_rule)):
            ta = first_time(rule)
            end = 300.0 if ta is None else ta
            res[name] = {"abortó en": ta, "peticiones dañadas": failed_until(end)}
        abort[f] = res
    return {"tasa": RATE, "filas": rows, "aborto": abort}


# ---------------------------------------------------------------- SE-508
@cache
def e508_firmas() -> dict:
    """Qué señal mueve cada tipo de falla (huella de la falla)."""
    policy = CONFIGS["C"][1]
    faults = {
        "red: latencia +100 ms": [Fault("net_latency", 30, 60, 100)],
        "red: respuestas perdidas 100 %": [Fault("blackhole", 30, 60, 1.0)],
        "dependencia: 30 % de errores": [Fault("error", 30, 60, 0.3)],
        "recursos: mitad de los hilos": [Fault("capacity", 30, 60, 0.5)],
        "recursos: servicio lento +100 ms": [Fault("slow", 30, 60, 100)],
        "procesos: caída de 12 s": [Fault("capacity", 30, 42, 1.0)],
    }
    base = simulate(11, policy, [], duration_s=90.0, rate=RATE)
    b = summarize(base, 32, 60)
    base_util = base.busy_ms / (8 * 90_000.0)
    rows = {}
    for name, fl in faults.items():
        r = simulate(11, policy, fl, duration_s=90.0, rate=RATE)
        s = summarize(r, 32, fl[0].end)
        inside = [i for i, t in enumerate(r.t0) if 32 <= t < fl[0].end]
        lat = [r.latency[i] for i in inside if r.outcome[i] == "ok"]
        rows[name] = {
            "tasa de error": 1 - s["ok"],
            "p99 ms": pct(lat, 99) if lat else None,
            "intentos por petición": s["attempts"],
            "intentos al servidor por segundo": r.server_attempts / 90.0,
            "utilización": r.busy_ms / (8 * 90_000.0),
        }
    return {"base": {"tasa de error": 1 - b["ok"], "p99 ms": b["p99"], "intentos por petición": b["attempts"], "utilización": base_util, "intentos al servidor por segundo": base.server_attempts / 90.0}, "filas": rows}


@cache
def e508_reloj(n: int = 100_000, seed: int = 508) -> dict:
    """Desfase de reloj: tokens de 300 s validados con distinta tolerancia."""
    rng = random.Random(seed)
    ttl = 300.0
    out = {}
    for leeway in (0, 30, 60):
        for skew in (0, 5, 30, 60, 120, 300):
            rejected_ahead = rejected_behind = 0
            for _ in range(n):
                age = rng.uniform(0, ttl)  # edad real del token al validarlo
                # el validador va adelantado: ve al token más viejo
                if age + skew > ttl + leeway:
                    rejected_ahead += 1
                # el validador va atrasado: ve un token emitido «en el futuro»
                if skew - age > leeway:
                    rejected_behind += 1
            out[f"{leeway}|{skew}"] = {"adelantado": rejected_ahead / n, "atrasado": rejected_behind / n}
    return {"ttl": ttl, "n": n, "celdas": out}


@cache
def e508_disco(seed: int = 5082) -> dict:
    """Un disco que se detiene 2 s: registro síncrono frente a un búfer asíncrono."""
    policy = Policy(timeout_ms=250, retries=0)
    stall = 2.0
    r_sync = simulate(seed, policy, [Fault("slow", 30, 30 + stall, 2000.0)], duration_s=60.0, rate=RATE)
    sync = summarize(r_sync, 30, 40)
    out = {"parada s": stall, "sincrono": {"fallan": 1 - sync["ok"], "peticiones": sync["n"]}, "asincrono": {}}
    for buffer in (50, 200, 1000):
        lines = int(RATE * stall)
        out["asincrono"][buffer] = {"líneas perdidas": max(0, lines - buffer), "líneas": lines, "peticiones afectadas": 0}
    return out


# ---------------------------------------------------------------- SE-509 (medición real)
class _Backend(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        body = b"ok"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args):  # silencia el registro
        return


class _Proxy:
    """Proxy TCP mínimo con tres tóxicos: latencia, reinicio y silencio (la idea de Toxiproxy, sin su código)."""

    def __init__(self, upstream_port: int) -> None:
        self.upstream = upstream_port
        self.mode = "none"
        self.latency = 0.0
        self.sock = socket.socket()
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen(64)
        self.port = self.sock.getsockname()[1]
        self.alive = True
        threading.Thread(target=self._accept, daemon=True).start()

    def _accept(self) -> None:
        while self.alive:
            try:
                conn, _ = self.sock.accept()
            except OSError:
                return
            threading.Thread(target=self._serve, args=(conn,), daemon=True).start()

    def _serve(self, conn: socket.socket) -> None:
        try:
            if self.mode == "reset":
                conn.close()
                return
            if self.mode == "silence":
                time.sleep(3.0)
                conn.close()
                return
            up = socket.create_connection(("127.0.0.1", self.upstream))
            data = conn.recv(65536)
            if self.latency:
                time.sleep(self.latency / 2000.0)
            up.sendall(data)
            reply = up.recv(65536)
            if self.latency:
                time.sleep(self.latency / 2000.0)
            conn.sendall(reply)
            up.close()
            conn.close()
        except OSError:
            pass

    def close(self) -> None:
        self.alive = False
        self.sock.close()


def _fetch(port: int, timeout: float) -> tuple[bool, float]:
    t0 = time.perf_counter()
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=timeout) as c:
            c.settimeout(timeout)
            c.sendall(b"GET / HTTP/1.0\r\nHost: x\r\n\r\n")
            data = c.recv(65536)
        ok = data.startswith(b"HTTP/1.0 200") or data.startswith(b"HTTP/1.1 200")
    except OSError:
        ok = False
    return ok, (time.perf_counter() - t0) * 1000.0


@cache
def e509_proxy_real(n: int = 30, timeout: float = 0.3) -> dict:
    """Mide un cliente con espera de 300 ms contra un servicio local y un proxy que inyecta fallas."""
    server = ThreadingHTTPServer(("127.0.0.1", 0), _Backend)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    proxy = _Proxy(server.server_address[1])
    scenarios = [("sin tóxico", "none", 0.0), ("latencia 50 ms", "none", 50.0), ("latencia 200 ms", "none", 200.0), ("latencia 400 ms", "none", 400.0), ("reinicio de conexión", "reset", 0.0), ("silencio", "silence", 0.0)]
    rows = {}
    direct = [_fetch(server.server_address[1], timeout)[1] for _ in range(n)]
    for name, mode, lat in scenarios:
        proxy.mode, proxy.latency = mode, lat
        res = [_fetch(proxy.port, timeout) for _ in range(n)]
        oks = [ms for ok, ms in res if ok]
        rows[name] = {"exitos": len(oks), "n": n, "mediana ms": st.median([ms for _, ms in res]), "p95 ms": pct([ms for _, ms in res], 95)}
    proxy.close()
    server.shutdown()
    return {"n": n, "timeout ms": timeout * 1000, "directo": {"mediana ms": st.median(direct), "p95 ms": pct(direct, 95)}, "filas": rows}



# ---------------------------------------------------------------- SE-510
@cache
def e510_replicacion(n: int = 20_000, seed: int = 512) -> dict:
    """Pérdida de escrituras confirmadas al caer el primario con replicación asíncrona, semisíncrona y síncrona."""
    rng = random.Random(seed)
    write_rate = 200.0
    out = {}
    for name, spike_p in (("lag típico (mediana 20 ms)", 0.0), ("con 1 % de picos de 2 s", 0.01), ("con 5 % de picos de 10 s", 0.05)):
        lost = []
        for _ in range(n):
            lag = rng.lognormvariate(math.log(0.02), 0.6)
            if rng.random() < spike_p:
                lag = rng.choice([2.0, 10.0]) if spike_p == 0.05 else 2.0
            lost.append(int(write_rate * lag))
        out[name] = {"con pérdida": sum(1 for x in lost if x > 0) / n, "media": st.mean(lost), "p99": pct(lost, 99), "máx": max(lost)}
    # lecturas desde réplica tras escribir
    stale = {}
    for lag_ms in (5, 20, 100, 500):
        s = 0
        for _ in range(n):
            gap = rng.expovariate(1 / 0.05)  # tiempo entre la escritura y la lectura siguiente, media 50 ms
            if gap * 1000 < lag_ms * rng.lognormvariate(0, 0.4):
                s += 1
        stale[lag_ms] = s / n
    return {"n": n, "ritmo de escrituras": write_rate, "pérdida": out, "lecturas obsoletas": stale, "latencia añadida ms": {"asíncrona": 0, "semisíncrona (misma región)": 2, "síncrona entre regiones": 70}}


def _sigmoid(z: float) -> float:
    return 1 / (1 + math.exp(-max(-30.0, min(30.0, z))))


@cache
def e510_ml(seed: int = 5122, n: int = 3000) -> dict:
    """Un modelo logístico sintético con fallas del almacén de características: valor ausente, obsoleto y reserva."""
    rng = random.Random(seed)
    d = 6
    true_w = [1.5, -1.0, 0.8, 0.0, 0.5, -0.7]

    def sample(m: int):
        xs, ys = [], []
        for _ in range(m):
            x = [rng.gauss(0, 1) for _ in range(d)]
            p = _sigmoid(sum(a * b for a, b in zip(true_w, x)) + 0.2)
            xs.append(x)
            ys.append(1 if rng.random() < p else 0)
        return xs, ys

    xs, ys = sample(n)
    w = [0.0] * d
    b = 0.0
    for _ in range(120):
        gw = [0.0] * d
        gb = 0.0
        for x, y in zip(xs, ys):
            err = _sigmoid(sum(a * c for a, c in zip(w, x)) + b) - y
            for j in range(d):
                gw[j] += err * x[j]
            gb += err
        w = [wj - 0.5 * g / n for wj, g in zip(w, gw)]
        b -= 0.5 * gb / n
    tx, ty = sample(4000)

    def predict(x, weights=w, bias=b):
        return 1 if sum(a * c for a, c in zip(weights, x)) + bias > 0 else 0

    base_acc = sum(1 for x, y in zip(tx, ty) if predict(x) == y) / len(ty)
    # regla de reserva: signo de las dos primeras características (lo que un equipo escribiría a mano)
    def rule(x):
        return 1 if 1.5 * x[0] - 1.0 * x[1] > 0 else 0

    rule_acc = sum(1 for x, y in zip(tx, ty) if rule(x) == y) / len(ty)
    prior_acc = max(sum(ty), len(ty) - sum(ty)) / len(ty)
    rows = {}
    for frac in (0.0, 0.1, 0.25, 0.5):
        silent = stale = reserve = 0
        affected = 0
        for x, y in zip(tx, ty):
            hit = rng.random() < frac
            affected += hit
            if hit:
                x_miss = list(x)
                x_miss[0] = 0.0
                x_miss[1] = 0.0  # las dos características más informativas llegan con el valor por omisión
                silent += predict(x_miss) == y
                x_old = [rng.gauss(0, 1) if j in (0, 1) else x[j] for j in range(d)]  # valores de otra petición: obsoletos
                stale += predict(x_old) == y
                reserve += 1 if rule(x) == y else 0
            else:
                ok = predict(x) == y
                silent += ok
                stale += ok
                reserve += ok
        m = len(ty)
        rows[frac] = {"valor por omisión": silent / m, "valor obsoleto": stale / m, "reserva con regla": reserve / m}
    return {"exactitud sana": base_acc, "exactitud de la regla": rule_acc, "exactitud del azar informado": prior_acc, "filas": rows, "muestra": len(ty)}


EXPERIMENTS = {
    "e505": e505_estado_estable,
    "e506": e506_radio,
    "e507": lambda: {"matriz": e507_declarada(), "serie": e507_serie()},
    "e508": lambda: {"firmas": e508_firmas(), "reloj": e508_reloj(), "disco": e508_disco()},
    "e509": e509_proxy_real,
    "e510": lambda: {"replicacion": e510_replicacion(), "ml": e510_ml()},
}

if __name__ == "__main__":
    wanted = sys.argv[1:] or list(EXPERIMENTS)
    print(json.dumps({k: EXPERIMENTS[k]() for k in wanted}, ensure_ascii=False, indent=2, default=str))
