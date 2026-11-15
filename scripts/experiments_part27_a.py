"""Experimentos de SE-325 a SE-330 (datos sintéticos, semilla fija, solo biblioteca estándar).

Uso: python scripts/experiments_part27_a.py   (imprime una línea JSON por experimento)
"""
import json, random, sqlite3, sys

sys.stdout.reconfigure(encoding="utf-8")


def e325_cadena():
    r = random.Random(325)
    N, p = 200_000, 0.01
    out = []
    for k in range(1, 6):
        sync_ok = 0
        done = 0
        for _ in range(N):
            if all(r.random() >= p for _ in range(k)):
                sync_ok += 1
            # asíncrono: aceptar = 1 operación de cola; cada dependencia con hasta 3 intentos
            if r.random() >= p:
                if all(any(r.random() >= p for _ in range(3)) for _ in range(k)):
                    done += 1
        out.append((k, sync_ok / N, 0.99 ** k, done / N))
    return [(k, round(a * 100, 2), round(t * 100, 2), round(d * 100, 3)) for k, a, t, d in out]


def e325_reintentos():
    def run(q, layers, retries, budget):
        r = random.Random(3251)
        calls = 0
        tokens = [0.0] * layers

        def call(layer):
            nonlocal calls
            if layer == layers:
                calls += 1
                return r.random() >= q
            attempts = 0
            while True:
                attempts += 1
                if call(layer + 1):
                    return True
                if attempts > retries:
                    return False
                if budget:
                    if tokens[layer] < 1:
                        return False
                    tokens[layer] -= 1

        n = 10_000
        ok = 0
        for _ in range(n):
            for l in range(layers):
                tokens[l] = min(tokens[l] + 0.1, 10) if budget else 0
            ok += call(0)
        return calls / n, ok / n

    rows = []
    for q in (0.0, 0.5, 1.0):
        for layers, retries, budget in ((1, 2, False), (3, 2, False), (3, 2, True)):
            c, ok = run(q, layers, retries, budget)
            rows.append((q, layers, retries, budget, round(c, 2), round(ok * 100, 1)))
    return rows


def e325_caida():
    rows = []
    for cap in (1.2, 1.5, 2.0, 4.0):
        backlog = 0.0
        maxb = 0.0
        recovered = None
        sync_err = 0
        for t in range(0, 9000):
            arrive = 1.0
            down = 600 <= t < 1200
            if down:
                sync_err += 1
                backlog += arrive
            else:
                backlog += arrive
                backlog = max(0.0, backlog - cap)
            maxb = max(maxb, backlog)
            if t >= 1200 and backlog < 1 and recovered is None:
                recovered = t
        rows.append((cap, sync_err, int(maxb), recovered - 1200 if recovered is not None else None,
                     round(maxb / 1.0)))
    return rows


# ------------------------------------------------------------------ 326
def e326_contenido():
    r = random.Random(326)
    N = 1000
    ent = lambda i, v: {"entrega_id": i, "estudiante": f"est-{i % 80}", "curso": f"c-{i % 12}", "archivo": f"e{i}.zip",
                        "estado": v, "nota": None, "adjuntos": 3, "texto": "x" * 120}
    notif = {"type": "EntregaRecibida", "entrega_id": 1, "occurred_at": "2026-01-01T00:00:00Z"}
    st = ent(1, "recibida")
    b_not = len(json.dumps(notif, separators=(",", ":")))
    b_st = len(json.dumps(st, separators=(",", ":")))
    changed = sum(1 for _ in range(N) if r.random() < 0.3)
    consumers = [("notificaciones (quiere el estado actual)", "actual", {"estudiante"}),
                 ("auditoría (quiere el estado del instante)", "instante", {"estudiante", "estado"}),
                 ("analítica (quiere curso y estado actual)", "actual", {"curso", "estado"}),
                 ("calificador (quiere archivo del instante)", "instante", {"archivo"}),
                 ("facturación (solo el id)", "id", set())]
    rows = []
    for name, need, fields in consumers:
        cb = N if fields else 0
        wrong_not = changed if need == "instante" else 0
        wrong_st = changed if need == "actual" else 0
        rows.append((name, cb, wrong_not, wrong_st))
    return b_not, b_st, changed, rows


def e326_destinatarios():
    res = []
    for h in (0, 1, 3):
        n = 1000
        # comando: exige exactamente 1 manejador
        cmd_err = n if h != 1 else 0
        cmd_eff = n if h == 1 else (n * h if h > 1 else 0)  # con 3, un bus que difunde ejecuta 3 veces
        ev_err = 0
        ev_eff = n * h
        ev_lost = n if h == 0 else 0
        res.append((h, cmd_err, cmd_eff, ev_err, ev_eff, ev_lost))
    return res


def e326_sobre():
    r = random.Random(3262)
    N = 2000
    msgs = []
    seqs = {}
    for i in range(N):
        est = r.randrange(80)
        seqs[est] = seqs.get(est, 0) + 1
        # 5 % de reenvíos legítimos con el mismo contenido (otro envío del mismo archivo)
        msgs.append({"id": f"m{i}", "est": est, "seq": seqs[est], "t": i // 4, "corr": f"c{i // 3}",
                     "body": f"entrega:{est}:{r.randrange(40)}"})
    # duplicados 10 %
    dups = [dict(m) for m in r.sample(msgs, 200)]
    legit = []
    for m in r.sample(msgs, 100):  # contenido igual, mensaje distinto
        c = dict(m); c["id"] = f"L{m['id']}"; c["seq"] = m["seq"] + 1000; c["t"] = m["t"] + 1; legit.append(c)
    stream = msgs + dups + legit
    r.shuffle(stream)
    # deduplicar con id
    seen, kept = set(), []
    for m in stream:
        if m["id"] in seen: continue
        seen.add(m["id"]); kept.append(m)
    dedupe_id = (len(stream) - len(kept), 0)
    # sin id: por hash del cuerpo
    seen, kept2, dropped_legit = set(), [], 0
    for m in stream:
        k = (m["est"], m["body"])
        if k in seen:
            if m["id"].startswith("L"): dropped_legit += 1
            continue
        seen.add(k); kept2.append(m)
    removed_body = len(stream) - len(kept2)
    # orden: con seq vs con t (resolución de 1 unidad con 4 mensajes por unidad)
    by_est = {}
    for m in kept:
        by_est.setdefault(m["est"], []).append(m)

    def inversions(key):
        inv = 0
        for est, lst in by_est.items():
            order = sorted(lst, key=key)
            truth = sorted(lst, key=lambda m: m["seq"] if not m["id"].startswith("L") else 10**6 + m["seq"])
            inv += sum(1 for a, b in zip(order, truth) if a["id"] != b["id"])
        return inv
    inv_seq = inversions(lambda m: (m["seq"] if not m["id"].startswith("L") else 10**6 + m["seq"]))
    inv_t = inversions(lambda m: m["t"])
    # trazado: unir por correlación vs por (est, ventana ±1 de t)
    by_corr = {}
    for m in kept: by_corr.setdefault(m["corr"], []).append(m)
    true_pairs = sum(len(v) * (len(v) - 1) // 2 for v in by_corr.values())
    heur = 0; good = 0
    ks = list(kept)
    ks.sort(key=lambda m: m["t"])
    for i, a in enumerate(ks):
        for b in ks[i + 1:i + 200]:
            if b["t"] - a["t"] > 1: break
            if a["est"] == b["est"]:
                heur += 1
                if a["corr"] == b["corr"]: good += 1
    return {"stream": len(stream), "dups_removed_id": dedupe_id[0], "removed_body": removed_body,
            "dropped_legit": dropped_legit, "inv_seq": inv_seq, "inv_t": inv_t, "true_pairs": true_pairs,
            "heur_pairs": heur, "heur_good": good, "n": len(kept)}


# ------------------------------------------------------------------ 327
def e327_estructuras():
    N, late_at = 3000, 1000
    # cola de trabajo con 2 consumidores competidores
    queue = list(range(N)); got = {"A": 0, "B": 0}
    i = 0
    while queue:
        got["AB"[i % 2]] += 1; queue.pop(0); i += 1
    # tópico con suscripción tardía
    subs = {"A": [], "B": []}
    for m in range(N):
        subs["A"].append(m)
        if m >= late_at: subs["B"].append(m)
    # log con grupos
    log = list(range(N)); offsets = {"A": N, "B": N}
    # reprocesar 500 últimos tras corregir un defecto
    redo_queue = 0; redo_topic = 0; redo_log = 500
    return {"queue_split": (got["A"], got["B"], got["A"] + got["B"]), "topic": (len(subs["A"]), len(subs["B"])),
            "log": (N, N), "redo": (redo_queue, redo_topic, redo_log)}


def e327_particiones():
    r = random.Random(3272)
    students = 800
    w = [1 / (i + 1) ** 1.1 for i in range(students)]
    tot = sum(w)
    keys = r.choices(range(students), weights=w, k=20_000)
    rows = []
    for P in (4, 8, 16):
        counts = [0] * P
        for k in keys: counts[hash_k(k) % P] += 1
        for C in (4, 8):
            owners = [[] for _ in range(C)]
            for p in range(P): owners[p % C].append(p)
            loads = [sum(counts[p] for p in o) for o in owners]
            idle = sum(1 for o in owners if not o)
            mean = sum(loads) / C
            rows.append((P, C, max(loads), round(max(loads) / mean, 2), idle))
    # orden: con clave vs reparto circular, 4 particiones, servicio aleatorio
    def inv(keyed):
        r2 = random.Random(3273)
        lastseq, parts = {}, [[] for _ in range(4)]
        seq = {}
        for i, k in enumerate(keys[:8000]):
            seq[k] = seq.get(k, 0) + 1
            p = hash_k(k) % 4 if keyed else i % 4
            parts[p].append((k, seq[k]))
        done = []
        for p, lst in enumerate(parts):
            t = 0.0
            for k, s in lst:
                t += r2.expovariate(1.0)
                done.append((t, k, s))
        done.sort()
        mx, bad = {}, set()
        for _, k, s in done:
            if s < mx.get(k, 0): bad.add(k)
            mx[k] = max(mx.get(k, 0), s)
        return len(bad), len(set(keys[:8000]))
    return rows, inv(True), inv(False)


def hash_k(k):
    return (k * 2654435761) % (2**32)


def e327_compactacion():
    r = random.Random(3274)
    keys = 2000
    w = [1 / (i + 1) ** 1.0 for i in range(keys)]
    ks = r.choices(range(keys), weights=w, k=100_000)
    ev = []
    for i, k in enumerate(ks):
        tomb = r.random() < 0.05
        ev.append((k, None if tomb else i))
    def state(events):
        s = {}
        for k, v in events:
            if v is None: s.pop(k, None)
            else: s[k] = v
        return s
    full = state(ev)
    window = state(ev[-20_000:])
    comp = {}
    for k, v in ev: comp[k] = v
    compacted = [(k, v) for k, v in comp.items()]
    cs = state(compacted)
    # claves vivas que la ventana no conoce
    lost = sum(1 for k in full if k not in window)
    wrong = sum(1 for k in window if window[k] != full.get(k))
    return {"full_len": len(ev), "live": len(full), "window_live": len(window), "lost": lost, "wrong": wrong,
            "comp_len": len(compacted), "comp_equal": cs == full}


# ------------------------------------------------------------------ 328
def e328_semanticas():
    N = 20_000
    def sim(mode):
        r = random.Random(3281)
        lost = dup = eff = 0
        con = sqlite3.connect(":memory:")
        con.execute("create table done(id int primary key)")
        con.execute("create table efecto(msg int)")
        for m in range(N):
            delivered_effects = 0
            attempts = 0
            while True:
                attempts += 1
                lost_net = r.random() < 0.02
                if lost_net:
                    if mode == "at_most": break
                    continue  # el productor no recibe ack y reenvía
                # llega al consumidor
                crash = r.random() < 0.02
                if mode == "at_most":
                    if crash: break  # acusó antes de procesar y cayó
                    delivered_effects += 1; break
                # at-least-once: procesa y luego acusa
                if mode == "idem":
                    try:
                        con.execute("begin")
                        cur = con.execute("insert or ignore into done values(?)", (m,))
                        if cur.rowcount: con.execute("insert into efecto values(?)", (m,))
                        con.execute("commit")
                    except Exception:
                        con.execute("rollback")
                    delivered_effects = 1
                else:
                    delivered_effects += 1
                ack_lost = r.random() < 0.05
                if crash or ack_lost: continue
                break
            if mode == "idem": continue
            eff += delivered_effects
            if delivered_effects == 0: lost += 1
            elif delivered_effects > 1: dup += delivered_effects - 1
        if mode == "idem":
            total = con.execute("select count(*) from efecto").fetchone()[0]
            distinct = con.execute("select count(distinct msg) from efecto").fetchone()[0]
            return N - distinct, total - distinct, total
        return lost, dup, eff
    return {m: sim(m) for m in ("at_most", "at_least", "idem")}


def e328_orden():
    rows = []
    for k in (0, 3, 10, 50):
        r = random.Random(3282)
        entries, vers = 500, 10
        msgs = [(e, v) for e in range(entries) for v in range(1, vers + 1)]
        # orden de llegada: cada mensaje se retrasa hasta k posiciones
        keyed = sorted(range(len(msgs)), key=lambda i: i + r.uniform(0, k))
        arr = [msgs[i] for i in keyed]
        a = {}; b = {}
        for e, v in arr:
            a[e] = v
            if v > b.get(e, 0): b[e] = v
        wa = sum(1 for e in range(entries) if a[e] != vers)
        wb = sum(1 for e in range(entries) if b[e] != vers)
        rows.append((k, wa, wb))
    return rows


def e328_ventana():
    r = random.Random(3283)
    n, rate = 432_000, 5.0
    ts = [i / rate for i in range(n)]
    redel = []
    for i in range(n):
        if r.random() < 0.2:
            d = r.expovariate(1 / 60)
            if r.random() < 0.01: d = r.uniform(3600, 21600)
            redel.append((ts[i] + d, i, ts[i]))
    rows = []
    for W in (10, 60, 300, 3600, 86400, None):
        leaked = sum(1 for t, i, t0 in redel if W is not None and t - t0 > W)
        size = min(n, int(rate * W)) if W is not None else n
        rows.append((W, leaked, size))
    return len(redel), rows


# ------------------------------------------------------------------ 329
def e329_doble_escritura():
    N = 1000
    r = random.Random(3291)
    faults = [r.random() < 0.03 for _ in range(N)]
    # A: confirmar BD y luego publicar; caída entre ambos
    lost = sum(faults)
    A = {"db": N, "events": N - lost}
    # B: publicar y luego confirmar BD; la caída ocurre tras publicar
    B = {"db": N - sum(faults), "events": N}
    # C: outbox real
    con = sqlite3.connect(":memory:")
    con.execute("create table entrega(id int primary key)")
    con.execute("create table outbox(id int primary key, sent int default 0)")
    for i, f in enumerate(faults):
        try:
            con.execute("begin")
            con.execute("insert into entrega values(?)", (i,))
            if f: raise RuntimeError("caída antes del commit")
            con.execute("insert into outbox(id) values(?)", (i,))
            con.execute("commit")
        except RuntimeError:
            con.execute("rollback")
    # tras la caída, el emisor sigue ciclo normal: lo que está en outbox se publica
    ent = con.execute("select count(*) from entrega").fetchone()[0]
    ob = con.execute("select count(*) from outbox").fetchone()[0]
    # con el outbox, la caída del proceso deja ambos sin entrega ni evento (coherente)
    return A, B, {"db": ent, "events": ob}, sum(faults)


def e329_relevo():
    N = 1000
    res = {}
    for mode in ("publica_luego_marca", "marca_luego_publica"):
        r = random.Random(3292)
        broker = []
        for i in range(N):
            crash = r.random() < 0.03
            if mode == "publica_luego_marca":
                broker.append(i)
                if crash: broker.append(i)  # tras reiniciar vuelve a publicarlo
            else:
                if not crash: broker.append(i)
        distinct = len(set(broker))
        con = sqlite3.connect(":memory:")
        con.execute("create table inbox(id int primary key)")
        con.execute("create table efecto(id int)")
        for m in broker:
            cur = con.execute("insert or ignore into inbox values(?)", (m,))
            if cur.rowcount: con.execute("insert into efecto values(?)", (m,))
        eff = con.execute("select count(*) from efecto").fetchone()[0]
        res[mode] = (len(broker), len(broker) - distinct, N - distinct, len(broker), eff)
    return res


def e329_saga():
    ORD_A = [("reservar cupo", True), ("cobrar", True), ("dar acceso al aula", True), ("enviar bienvenida", False)]
    ORD_B = [("reservar cupo", True), ("cobrar", True), ("enviar bienvenida", False), ("dar acceso al aula", True)]
    out = {}
    for name, steps in (("bienvenida al final", ORD_A), ("bienvenida antes de acceso", ORD_B)):
        r = random.Random(3293)
        res = {"completa": 0, "revertida limpia": 0, "residuo irreversible": 0, "atascada": 0}
        n = 10_000
        for _ in range(n):
            done = []
            failed = False
            for s, comp in steps:
                if r.random() < 0.08:
                    failed = True; break
                done.append((s, comp))
            if not failed:
                res["completa"] += 1; continue
            stuck = residue = False
            for s_, comp in reversed(done):
                if not comp:
                    residue = True; continue
                if all(r.random() < 0.1 for _ in range(3)):  # tres intentos de compensar, todos fallan
                    stuck = True
            if stuck: res["atascada"] += 1
            elif residue: res["residuo irreversible"] += 1
            else: res["revertida limpia"] += 1
        out[name] = res
    return out


# ------------------------------------------------------------------ 330
def e330_cambios():
    r = random.Random(3301)
    src = sqlite3.connect(":memory:")
    src.execute("create table t(id int primary key, v int, ts int, del int default 0)")
    src.execute("create table log(seq integer primary key autoincrement, id int, op text, v int)")
    src.execute("create trigger ti after insert on t begin insert into log(id,op,v) values(new.id,'u',new.v); end")
    src.execute("create trigger tu after update of v on t begin insert into log(id,op,v) values(new.id,'u',new.v); end")
    src.execute("create trigger td after delete on t begin insert into log(id,op,v) values(old.id,'d',null); end")
    clock = [0]
    ids = list(range(1, 10_001))
    for i in ids: src.execute("insert into t(id,v,ts) values(?,?,0)", (i, 0))
    src.execute("delete from log")
    wm = {"gt": 0, "ge": 0}
    rep = {k: {} for k in ("gt", "ge")}
    rep_log = {}
    last_seq = 0
    for k in rep:
        for i in ids: rep[k][i] = 0
    rep_log = {i: 0 for i in ids}
    nid = 10_001
    live = set(ids)

    def poll():
        nonlocal last_seq
        for k, op in (("gt", ">"), ("ge", ">=")):
            rows = src.execute(f"select id,v,ts from t where ts {op} ?", (wm[k],)).fetchall()
            for i, v, ts in rows: rep[k][i] = v
            if rows: wm[k] = max(ts for _, _, ts in rows)
        for seq, i, op, v in src.execute("select seq,id,op,v from log where seq>? order by seq", (last_seq,)).fetchall():
            last_seq = seq
            if op == "d": rep_log.pop(i, None)
            else: rep_log[i] = v
    for op in range(2000):
        clock[0] = op // 5 + 1  # 5 operaciones por segundo
        x = r.random()
        if x < 0.2:
            src.execute("insert into t(id,v,ts) values(?,?,?)", (nid, op, clock[0])); live.add(nid); nid += 1
        elif x < 0.9:
            i = r.choice(sorted(live)); src.execute("update t set v=?, ts=? where id=?", (op, clock[0], i))
        else:
            i = r.choice(sorted(live)); src.execute("delete from t where id=?", (i,)); live.discard(i)
        if op % 47 == 46: poll()
    poll()
    truth = dict(src.execute("select id,v from t").fetchall())
    def diff(rp):
        missing = sum(1 for i in truth if i not in rp)
        stale = sum(1 for i in truth if i in rp and rp[i] != truth[i])
        extra = sum(1 for i in rp if i not in truth)
        return missing, stale, extra
    return {"gt": diff(rep["gt"]), "ge": diff(rep["ge"]), "log": diff(rep_log), "n": len(truth)}


def e330_costo():
    N = 100_000
    rows = []
    for rate in (0.001, 0.01, 0.1, 0.5):
        changes = int(N * rate)
        rows.append((rate, N, changes))
    # costo de escritura del disparador, en pasos de la máquina virtual
    def steps(with_trigger):
        con = sqlite3.connect(":memory:", isolation_level=None)
        con.execute("create table t(id int primary key, v int)")
        con.execute("create table log(seq integer primary key autoincrement, id int, op text, v int)")
        if with_trigger:
            con.execute("create trigger tu after update of v on t begin insert into log(id,op,v) values(new.id,'u',new.v); end")
        con.executemany("insert into t values(?,?)", [(i, 0) for i in range(10_000)])
        cnt = [0]
        def h(): cnt[0] += 1; return 0
        con.set_progress_handler(h, 1)
        con.execute("begin")
        for i in range(10_000): con.execute("update t set v=v+1 where id=?", (i,))
        con.execute("commit")
        return cnt[0]
    return rows, steps(False), steps(True)


def e330_orden():
    r = random.Random(3303)
    keys = 50
    events = []
    ver = {k: 0 for k in range(keys)}
    for _ in range(5000):
        k = r.randrange(keys)
        ver[k] += 1
        events.append((k, ver[k], "d" if r.random() < 0.1 else "u"))
    s = {}
    for k, v, op in events:
        if op == "d": s.pop(k, None)
        else: s[k] = v
    truth = s

    def apply(evs, guard):
        s, vers = {}, {}
        for k, v, op in evs:
            if guard and v <= vers.get(k, 0): continue
            vers[k] = v
            if op == "d": s.pop(k, None)
            else: s[k] = v
        return s
    bad = lambda s: sum(1 for k in set(truth) | set(s) if truth.get(k) != s.get(k))
    rows = []
    for name, shuffle, dup in (("en orden", 0, 0), ("reordenado hasta 20 posiciones", 20, 0),
                               ("10 % de duplicados tardíos", 0, 1), ("ambos", 20, 1)):
        rr = random.Random(3304)
        arr = []
        for i, e in enumerate(events):
            arr.append((i + rr.uniform(0, shuffle), e))
            if dup and rr.random() < 0.1: arr.append((i + rr.uniform(0, 60), e))
        arr.sort(key=lambda x: x[0])
        ev = [e for _, e in arr]
        rows.append((name, bad(apply(ev, False)), bad(apply(ev, True))))
    return rows


if __name__ == "__main__":
    print("platform", sys.version.split()[0], sqlite3.sqlite_version)
    for fn in (e325_cadena, e325_reintentos, e325_caida, e326_contenido, e326_destinatarios, e326_sobre,
               e327_estructuras, e327_particiones, e327_compactacion, e328_semanticas, e328_orden, e328_ventana,
               e329_doble_escritura, e329_relevo, e329_saga, e330_cambios, e330_costo, e330_orden):
        print(fn.__name__, json.dumps(fn(), ensure_ascii=False, default=str))
