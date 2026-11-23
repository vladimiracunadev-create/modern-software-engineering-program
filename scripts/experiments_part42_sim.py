"""Simulador de eventos discretos de un cliente con tiempo de espera, reintentos y cortacircuitos.

Un servicio local (la dependencia) atiende con ``workers`` hilos y una cola FIFO. El cliente
envía las peticiones de las personas usuarias, con un tiempo de espera por intento, un
número de reintentos, un retardo entre intentos y, opcionalmente, un cortacircuitos y una
respuesta alternativa. Las fallas se inyectan por ventanas de tiempo. Todo es tiempo virtual
y usa ``random.Random`` con semilla fija: no hay reloj, red ni servidor reales.
"""
from __future__ import annotations

import heapq
import math
import random
from collections import deque
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Fault:
    kind: str          # net_latency | slow | error | blackhole | capacity
    start: float       # segundos
    end: float
    param: float       # ms (latencias), probabilidad (error, blackhole) o fracción de hilos (capacity)


@dataclass(frozen=True)
class Policy:
    timeout_ms: float = 300.0
    retries: int = 2
    backoff: str = "none"        # none | fixed | exp_jitter
    backoff_ms: float = 50.0
    breaker: tuple | None = None  # (umbral de fallos 0..1, ventana de intentos, ms abierto)
    fallback: bool = False
    deadline_ms: float = 1000.0


@dataclass
class Result:
    t0: list = field(default_factory=list)
    outcome: list = field(default_factory=list)   # ok | degraded | fail
    latency: list = field(default_factory=list)
    attempts: list = field(default_factory=list)
    treated: list = field(default_factory=list)
    server_attempts: int = 0
    wasted_ms: float = 0.0
    busy_ms: float = 0.0


def pct(values, q):
    ordered = sorted(values)
    if not ordered:
        return float("nan")
    index = min(len(ordered) - 1, max(0, math.ceil(q / 100 * len(ordered)) - 1))
    return ordered[index]


def simulate(seed: int, policy: Policy, faults=(), duration_s: float = 120.0, rate: float = 60.0,
             workers: int = 8, service_ms: float = 40.0, max_wait_ms: float = 1500.0,
             treat_fraction: float = 1.0, sigma: float = 0.3) -> Result:
    rng = random.Random(seed)
    res = Result()
    free = [0.0] * workers
    heapq.heapify(free)
    applied: set[int] = set()
    events: list = []
    counter = 0
    t = 0.0
    n_req = 0
    while True:
        t += rng.expovariate(rate)
        if t >= duration_s:
            break
        heapq.heappush(events, (t, counter, n_req, 0))
        counter += 1
        res.t0.append(t)
        res.outcome.append("")
        res.latency.append(0.0)
        res.attempts.append(0)
        res.treated.append(rng.random() < treat_fraction)
        n_req += 1
    window: deque = deque(maxlen=policy.breaker[1] if policy.breaker else 1)
    state = {"open_until": -1.0, "half": False}

    def finish(i, now, outcome):
        res.outcome[i] = outcome
        res.latency[i] = (now - res.t0[i]) * 1000.0

    def failed(i, now, n):
        # decide whether to retry or give up
        if n < policy.retries:
            if policy.backoff == "none":
                wait = 0.0
            elif policy.backoff == "fixed":
                wait = policy.backoff_ms
            else:
                wait = rng.uniform(0.0, policy.backoff_ms * (2 ** n))
            nxt = now + wait / 1000.0
            if (nxt - res.t0[i]) * 1000.0 < policy.deadline_ms:
                nonlocal counter
                heapq.heappush(events, (nxt, counter, i, n + 1))
                counter += 1
                return
        finish(i, min(now, res.t0[i] + policy.deadline_ms / 1000.0), "degraded" if policy.fallback else "fail")

    while events:
        now, _, i, n = heapq.heappop(events)
        res.attempts[i] += 1
        if policy.breaker:
            if now < state["open_until"]:
                finish(i, now, "degraded" if policy.fallback else "fail")
                continue
            if state["open_until"] > 0 and not state["half"]:
                state["half"] = True  # el siguiente intento es la sonda
        active = [f for f in faults if f.start <= now < f.end and (res.treated[i] or f.kind == "capacity")]
        for k, f in enumerate(faults):
            if f.kind == "capacity" and f.start <= now < f.end and k not in applied:
                applied.add(k)
                free.sort()
                for j in range(int(round(f.param * workers))):
                    free[j] = max(free[j], f.end)
                heapq.heapify(free)
        net = sum(f.param for f in active if f.kind == "net_latency")
        slow = sum(f.param for f in active if f.kind == "slow")
        p_err = 1 - math.prod(1 - f.param for f in active if f.kind == "error") if any(f.kind == "error" for f in active) else 0.0
        p_hole = 1 - math.prod(1 - f.param for f in active if f.kind == "blackhole") if any(f.kind == "blackhole" for f in active) else 0.0
        ok = False
        t_done = now + policy.timeout_ms / 1000.0
        res.server_attempts += 1
        if rng.random() < p_hole:
            pass  # sin respuesta: el cliente espera hasta el tiempo de espera
        else:
            earliest = heapq.heappop(free)
            start = max(now, earliest)
            if (start - now) * 1000.0 > max_wait_ms:
                heapq.heappush(free, earliest)
                t_done = now + 0.001  # rechazo inmediato por cola llena
            else:
                svc = service_ms * rng.lognormvariate(0, sigma)
                if rng.random() < p_err:
                    svc = min(svc, 5.0)
                    resp_err = True
                else:
                    svc += slow
                    resp_err = False
                res.busy_ms += svc
                end = start + svc / 1000.0
                heapq.heappush(free, end)
                arrival = end + net / 1000.0
                if (arrival - now) * 1000.0 <= policy.timeout_ms:
                    t_done = arrival
                    ok = not resp_err
                else:
                    res.wasted_ms += svc
        if policy.breaker:
            window.append(0 if ok else 1)
            thr, size, open_ms = policy.breaker
            if state["half"]:
                state["half"] = False
                if ok:
                    state["open_until"] = -1.0
                    window.clear()
                else:
                    state["open_until"] = t_done + open_ms / 1000.0
            elif len(window) >= max(5, size // 2) and sum(window) / len(window) >= thr:
                state["open_until"] = t_done + open_ms / 1000.0
                window.clear()
        if ok:
            finish(i, t_done, "ok")
        else:
            failed(i, t_done, n)
    return res


def summarize(res: Result, a: float = 0.0, b: float = 1e9, treated_only: bool | None = None) -> dict:
    idx = [i for i, t in enumerate(res.t0) if a <= t < b and (treated_only is None or res.treated[i] == treated_only)]
    if not idx:
        return {"n": 0, "ok": float("nan"), "degraded": 0.0, "fail": float("nan"), "p99": float("nan"), "attempts": float("nan")}
    n = len(idx)
    good = [i for i in idx if res.outcome[i] == "ok" and res.latency[i] <= 1e9]
    return {
        "n": n,
        "ok": len(good) / n,
        "degraded": sum(1 for i in idx if res.outcome[i] == "degraded") / n,
        "fail": sum(1 for i in idx if res.outcome[i] == "fail") / n,
        "p99": pct([res.latency[i] for i in good], 99) if good else float("nan"),
        "attempts": sum(res.attempts[i] for i in idx) / n,
    }
