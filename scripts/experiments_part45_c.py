"""Experimentos de las clases SE-549 a SE-552 (Parte 45): gobierno y privacidad, costos y operación, taller de
un pipeline defectuoso y proyecto de plataforma de datos mínima gobernada.

Uso: python scripts/experiments_part45_c.py [549|550|551|552]

No se invoca ningún modelo de lenguaje. Biblioteca estándar y el caso conductor *Avisos*. Los precios
y los umbrales son parámetros inventados por el autor (unidades de costo, no dinero real); los tiempos
y los tamaños en disco se miden de verdad y varían de un equipo a otro.
"""
from __future__ import annotations

import copy
import hashlib
import hmac
import json
import os
import random
import re
import sqlite3
import sys
import tempfile
import time
from collections import Counter, defaultdict

from experiments_part45_lab import SEED, fmt, mem_db, pct, table, timed


# ====================================================================== SE-549
def users(rng, n=5000):
    cities = ["Santiago", "Temuco", "Arica", "Puerto Montt", "Iquique", "Valdivia"]
    out = []
    for i in range(n):
        email = f"usuario{i}@{rng.choice(['correo.example', 'mail.example', 'ejemplo.test'])}"
        phone = f"+56 9 {rng.randrange(1000, 9999)} {rng.randrange(1000, 9999)}"
        note = f"contactar a {email}" if rng.random() < 0.10 else rng.choice(["sin novedad", "plan anual", "pide factura"])
        out.append({"user_id": i, "email": email, "phone": phone, "birth_year": rng.randrange(1950, 2006), "city": rng.choice(cities),
                    "plan": rng.choice(["free", "pro", "team"]), "contact_ref": email if rng.random() < 0.3 else f"ref-{rng.randrange(10**6)}", "note": note})
    return out


PATTERNS = {"correo": re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "teléfono": re.compile(r"\+56 9 \d{4} \d{4}")}


def e549():
    print("SE-549 — gobierno, privacidad y retención")
    rng = random.Random(SEED)
    data = users(rng)
    cols = list(data[0])
    by_name = [c for c in cols if re.search(r"mail|phone|tel|rut|nombre", c)]
    by_value = {}
    for c in cols:
        hits = sum(1 for r in data[:500] if any(p.search(str(r[c])) for p in PATTERNS.values()))
        if hits:
            by_value[c] = hits
    print(f"  clasificación por nombre de columna: {by_name}; por contenido (500 filas de muestra): {by_value}")
    print(f"  columnas con datos personales que el nombre no delata: {sorted(set(by_value) - set(by_name))}")
    # seudonimización
    emails = [r["email"] for r in data]
    plain = {hashlib.sha256(e.encode()).hexdigest(): e for e in emails}
    key = b"clave-de-laboratorio-para-el-experimento"
    keyed = {hmac.new(key, e.encode(), hashlib.sha256).hexdigest(): e for e in emails}
    guess = [f"usuario{i}@{d}" for i in range(0, 6000) for d in ("correo.example", "mail.example", "ejemplo.test")]
    cracked_plain = sum(1 for g in guess if hashlib.sha256(g.encode()).hexdigest() in plain)
    wrong_key = b"otra-clave-que-el-atacante-adivina"
    cracked_keyed = sum(1 for g in guess if hmac.new(wrong_key, g.encode(), hashlib.sha256).hexdigest() in keyed)
    print(f"  un atacante con {len(guess)} correos candidatos recupera {cracked_plain} de {len(plain)} correos con SHA-256 sin clave ({fmt(cracked_plain/len(plain)*100,1)} %) y {cracked_keyed} con HMAC si no conoce la clave")
    same = hmac.new(key, emails[0].encode(), hashlib.sha256).hexdigest() == hmac.new(key, emails[0].encode(), hashlib.sha256).hexdigest()
    print(f"  la seudonimización con clave conserva la unión entre tablas (mismo valor de entrada, mismo seudónimo): {same}")
    # k-anonimato de un agregado liberado
    def small_groups(keyf, k):
        cnt = Counter(keyf(r) for r in data)
        rows_small = sum(v for v in cnt.values() if v < k)
        return len(cnt), sum(1 for v in cnt.values() if v < k), rows_small
    rows = [["Cuasi-identificadores del agregado", "Grupos", "Grupos con menos de 5", "Personas en grupos pequeños"]]
    for name, f in (("ciudad", lambda r: (r["city"],)), ("ciudad y plan", lambda r: (r["city"], r["plan"])),
                    ("ciudad, plan y año de nacimiento", lambda r: (r["city"], r["plan"], r["birth_year"])),
                    ("ciudad, plan y década de nacimiento", lambda r: (r["city"], r["plan"], r["birth_year"] // 10))):
        g, s, p = small_groups(f, 5)
        rows.append([name, g, s, p])
    table(rows)
    # borrado propagado
    con = mem_db()
    con.executescript("""CREATE TABLE raw_users(user_id INT, email TEXT);
    CREATE TABLE stg_users(user_id INT, email TEXT);
    CREATE TABLE fact_events(user_id INT, kind TEXT);
    CREATE TABLE mart_cohort(city TEXT, n INT);
    CREATE TABLE feature_store(user_id INT, score REAL);""")
    con.executemany("INSERT INTO raw_users VALUES(?,?)", [(r["user_id"], r["email"]) for r in data])
    con.executemany("INSERT INTO stg_users VALUES(?,?)", [(r["user_id"], r["email"]) for r in data])
    con.executemany("INSERT INTO fact_events VALUES(?,?)", [(r["user_id"], "login") for r in data for _ in range(3)])
    con.executemany("INSERT INTO feature_store VALUES(?,?)", [(r["user_id"], rng.random()) for r in data])
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        export = os.path.join(tmp, "export.csv")
        with open(export, "w") as fh:
            fh.writelines(f"{r['user_id']},{r['email']}\n" for r in data)
        uid = 42
        con.execute("DELETE FROM raw_users WHERE user_id=?", (uid,))
        def where_left():
            left = {}
            for t in ("raw_users", "stg_users", "fact_events", "feature_store"):
                left[t] = con.execute(f"SELECT COUNT(*) FROM {t} WHERE user_id=?", (uid,)).fetchone()[0]  # nosec B608
            left["export.csv"] = sum(1 for line in open(export) if line.startswith(f"{uid},"))
            return {k: v for k, v in left.items() if v}
        print(f"  borrar al usuario {uid} solo en la tabla de origen deja datos en: {where_left()}")
        for t in ("stg_users", "fact_events", "feature_store"):
            con.execute(f"DELETE FROM {t} WHERE user_id=?", (uid,))  # nosec B608
        print(f"  tras propagar el borrado por el linaje de tablas, queda: {where_left()} (el archivo exportado no es una tabla: el catálogo debe listarlo como copia)")
    # retención
    ev = [(rng.randrange(0, 1000), "x") for _ in range(100_000)]
    con.execute("CREATE TABLE logs(day INT, k TEXT)")
    con.executemany("INSERT INTO logs VALUES(?,?)", ev)
    for keep in (90, 365, 730):
        n = con.execute("SELECT COUNT(*) FROM logs WHERE day < 1000 - ?", (keep,)).fetchone()[0]
        print(f"  retención de {keep} días sobre 1000 días de registros: se purgan {n} de {len(ev)} filas ({fmt(n/len(ev)*100,1)} %)")


# ====================================================================== SE-550
def e550():
    print("SE-550 — costos y operación de una plataforma de datos")
    import experiments_part45_b as B
    rng = random.Random(SEED)
    n = 200_000
    rows = B.make_rows(rng, n)
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        csv_p = os.path.join(tmp, "o.csv")
        with open(csv_p, "w") as fh:
            fh.write(",".join(B.COLS) + "\n")
            fh.writelines(",".join(map(str, r)) + "\n" for r in rows)
        col_p = os.path.join(tmp, "o.col")
        meta = B.write_columnar(col_p, rows)
        size_csv, size_col = os.path.getsize(csv_p), os.path.getsize(col_p)
        _, g10, b10 = B.read_columnar(col_p, meta, ["day", "amount"], 100, 109)
        _, g_all, b_all = B.read_columnar(col_p, meta, ["day", "amount"], 0, 364)
    print(f"  bytes leídos por una consulta de 10 días: CSV {size_csv/1e6:.2f} MB (lee todo), columnar sin recortar rango {b_all/1e6:.2f} MB, columnar con estadísticas {b10/1e6:.3f} MB ({g10} de {len(meta)} grupos)")
    PRICE_SCAN = 5.0     # unidades de costo por TB escaneado (parámetro del autor)
    PRICE_STORE = 23.0   # unidades por TB-mes almacenado (parámetro del autor)
    scale = 1.0e12 / size_csv  # escalar a una tabla de 1 TB de CSV
    rows_t = [["Estrategia de consulta", "TB escaneados por consulta", "Costo por consulta", "Costo por mes (100 consultas por día)"]]
    plan = {}
    for name, b in (("CSV, lectura completa", size_csv), ("columnar, dos columnas, todo el rango", b_all), ("columnar, dos columnas, 10 días con estadísticas", b10)):
        tb = b * scale / 1e12
        per = tb * PRICE_SCAN
        monthly = per * 100 * 30
        plan[name] = (tb, per, monthly)
        rows_t.append([name, fmt(tb, 3), fmt(per, 3), fmt(monthly, 0)])
    table(rows_t)
    print(f"  almacenamiento de la misma tabla: CSV {fmt(size_csv*scale/1e12*PRICE_STORE,1)} unidades por mes frente a columnar {fmt(size_col*scale/1e12*PRICE_STORE,1)}")
    # refresco completo frente a incremental, medido
    con = mem_db()
    con.execute("CREATE TABLE fact(day INT, amount INT)")
    con.executemany("INSERT INTO fact VALUES(?,?)", [(i // 2000, rng.randrange(500, 90000)) for i in range(500_000)])
    con.execute("CREATE TABLE mart(day INT PRIMARY KEY, total INT)")
    def full():
        con.execute("DELETE FROM mart")
        con.execute("INSERT INTO mart SELECT day, SUM(amount) FROM fact GROUP BY day")
    def incr():
        con.execute("DELETE FROM mart WHERE day >= 248")
        con.execute("INSERT INTO mart SELECT day, SUM(amount) FROM fact WHERE day >= 248 GROUP BY day")
    t_full, _ = timed(full, 3)
    t_inc, _ = timed(incr, 3)
    print(f"  refresco de un mart sobre 500 000 filas: completo {fmt(t_full,1)} ms; incremental de los últimos 2 días {fmt(t_inc,1)} ms ({fmt(t_full/t_inc,0)} veces menos)")
    PRICE_CPU = 0.002  # unidades por segundo de cómputo (parámetro del autor)
    rows_t = [["Frecuencia de refresco", "Ejecuciones por mes", "Costo mensual, completo", "Costo mensual, incremental"]]
    scale_t = 2000  # escalar a una tabla 2000 veces mayor (parámetro del autor)
    for label, per_day in (("cada 5 minutos", 288), ("cada hora", 24), ("diario", 1)):
        runs = per_day * 30
        rows_t.append([label, runs, fmt(runs * t_full / 1000 * scale_t * PRICE_CPU, 0), fmt(runs * (t_inc / 1000 * scale_t + 20) * PRICE_CPU, 0)])
    table(rows_t)
    print("  el incremental suma 20 s fijos de arranque por ejecución (parámetro del autor) y por eso la frecuencia alta lo penaliza")
    # ruta crítica
    tasks = {"ingest_orders": (12, []), "ingest_customers": (4, []), "stg_orders": (6, ["ingest_orders"]), "dim_customer": (3, ["ingest_customers"]),
             "fact_sales": (15, ["stg_orders", "dim_customer"]), "mart_city": (5, ["fact_sales"]), "mart_daily": (4, ["fact_sales"]), "report": (2, ["mart_city", "mart_daily"])}
    finish = {}
    def f(t):
        if t not in finish:
            d, deps = tasks[t]
            finish[t] = d + max((f(x) for x in deps), default=0)
        return finish[t]
    total = f("report")
    path, cur = [], "report"
    while cur:
        path.append(cur)
        deps = tasks[cur][1]
        cur = max(deps, key=lambda x: finish[x]) if deps else None
    print(f"  ruta crítica de 8 tareas (minutos): {' > '.join(reversed(path))} = {total} min; suma de todas las duraciones {sum(d for d, _ in tasks.values())} min")
    for t in ("fact_sales", "mart_city", "ingest_customers"):
        d, deps = tasks[t]
        tasks2 = dict(tasks)
        tasks2[t] = (d / 2, deps)
        finish2 = {}
        def g(x):
            if x not in finish2:
                dd, ds = tasks2[x]
                finish2[x] = dd + max((g(y) for y in ds), default=0)
            return finish2[x]
        print(f"  reducir a la mitad {t} ({d} min): la ruta pasa a {g('report'):g} min")


# ====================================================================== SE-551
DAYS = 14
TZ = -3 * 3600


def source_orders(rng, n=20_000):
    out = []
    for i in range(n):
        ts = rng.randrange(0, DAYS * 86400)
        cust = rng.randrange(400) if rng.random() > 0.01 else None
        arr = ts // 86400 + (rng.choice([1, 1, 2]) if rng.random() < 0.03 else 0)
        out.append({"order_id": i, "customer_id": cust, "ts": ts, "amount": rng.randrange(1000, 90000), "arrival_day": arr})
    return out


def local_day(ts):
    return (ts + TZ) // 86400


def truth_mart(orders):
    t = defaultdict(lambda: [0, 0])
    for o in orders:
        d = local_day(o["ts"])
        t[d][0] += 1
        t[d][1] += o["amount"]
    return {d: tuple(v) for d, v in t.items()}


DEFECTS = {
    "D1": "carga por append (no idempotente)", "D2": "día calculado en UTC en vez de hora local", "D3": "unión con la dimensión histórica sin filtrar por fecha",
    "D4": "datos tardíos descartados por la fecha de carga", "D5": "unión interna que pierde las claves nulas", "D6": "importes sumados como números de coma flotante",
    "D7": "renombre de columna en el origen que se rellena con 0", "D8": "archivo del origen truncado sin comprobar el número de filas",
}


def run_pipeline(orders, defects, runs=1, source_cols=None):
    con = mem_db()
    con.executescript("CREATE TABLE fact(order_id INT, customer_id INT, day INT, amount); CREATE TABLE dim_c(customer_id INT, valid_from INT, valid_to INT, city TEXT);")
    rng = random.Random(SEED + 1)
    rows = []
    for c in range(400):
        rows.append((c, 0, 7, "A"))
        rows.append((c, 7, 10_000, "B"))
    con.executemany("INSERT INTO dim_c VALUES(?,?,?,?)", rows)
    src = orders
    if "D8" in defects:
        src = orders[: int(len(orders) * 0.93)] if len(orders) > 10 else orders
    for _ in range(runs):
        by_arrival = defaultdict(list)
        for o in src:
            by_arrival[o["arrival_day"]].append(o)
        if "D1" not in defects:
            con.execute("DELETE FROM fact")
        for arr in sorted(by_arrival):
            for o in by_arrival[arr]:
                ts = o["ts"]
                day = ts // 86400 if "D2" in defects else local_day(ts)
                if "D4" in defects and local_day(ts) < arr:
                    continue
                amount = o["amount"] if "D7" not in defects else 0
                con.execute("INSERT INTO fact VALUES(?,?,?,?)", (o["order_id"], o["customer_id"], day, amount / 100.0 if "D6" in defects else amount))
    join = "JOIN" if "D5" in defects else "LEFT JOIN"
    cond = "" if "D3" in defects else "AND f.day >= d.valid_from AND f.day < d.valid_to"
    q = f"SELECT f.day, COUNT(*), SUM(f.amount) FROM fact f {join} dim_c d ON d.customer_id = f.customer_id {cond} GROUP BY f.day"  # nosec B608
    mart = {d: (c, s) for d, c, s in con.execute(q)}
    if "D6" in defects:
        mart = {d: (c, int(s * 100)) for d, (c, s) in mart.items()}  # sumas en coma flotante y conversión a centavos truncando
    return con, mart


def e551():
    print("SE-551 — taller: diagnóstico de un pipeline defectuoso")
    rng = random.Random(SEED)
    orders = source_orders(rng)
    truth = truth_mart(orders)
    tr_rows = sum(c for c, _ in truth.values())
    tr_sum = sum(s for _, s in truth.values())
    print(f"  {len(orders)} pedidos en {DAYS} días; verdad: {tr_rows} filas, importe total {tr_sum}; defectos sembrados: {json.dumps(DEFECTS, ensure_ascii=False)}")
    def checks(defects, orders_in):
        con, mart = run_pipeline(orders_in, defects)
        con2, mart2 = run_pipeline(orders_in, defects, runs=2)
        cnt = sum(c for c, _ in mart.values())
        tot = sum(s for _, s in mart.values())
        res = {}
        res["conciliar filas con el origen"] = cnt != len(orders)
        res["conciliar importe con el origen"] = tot != sum(o["amount"] for o in orders)
        res["unicidad de pedidos"] = con.execute("SELECT COUNT(*) - COUNT(DISTINCT order_id) FROM fact").fetchone()[0] > 0
        res["frescura (último día presente)"] = (max(mart) if mart else -1) < max(truth)
        res["repetir la ejecución da lo mismo"] = mart != mart2
        # prueba de frontera con un pedido a las 23:30 hora local
        fixture = [{"order_id": 0, "customer_id": 1, "ts": 5 * 86400 + 3 * 3600 - 1800, "amount": 1000, "arrival_day": 4}]
        _, m = run_pipeline(fixture, defects)
        res["prueba de frontera de día"] = set(m) != {local_day(fixture[0]["ts"])}
        src_cols = ["order_id", "customer_id", "ts", "amount_clp" if "D7" in defects else "amount", "arrival_day"]
        res["esquema de entrada (columnas esperadas)"] = src_cols != ["order_id", "customer_id", "ts", "amount", "arrival_day"]
        res["importe medio por día en banda"] = any(abs(mart.get(d, (0, 0))[1] / max(mart.get(d, (1, 0))[0], 1) / (truth[d][1] / truth[d][0]) - 1) > 0.25 for d in truth)
        return res, mart
    names = None
    mat = []
    rows_t = [["Defecto", "Filas de más o de menos", "Importe de más o de menos", "Días con resultado distinto", "Filas tras un reintento"]]
    for k in DEFECTS:
        res, mart = checks({k}, orders)
        if names is None:
            names = list(res)
        mat.append([res[n] for n in names])
        n = sum(c for c, _ in mart.values()) - tr_rows
        s = sum(x for _, x in mart.values()) - tr_sum
        bad = sum(1 for d in truth if mart.get(d) != truth[d])
        _, mart_r = run_pipeline(orders, {k}, runs=2)
        n_r = sum(c for c, _ in mart_r.values()) - tr_rows
        rows_t.append([f"{k} {DEFECTS[k]}", f"{n:+d}", f"{s:+d}", f"{bad} de {len(truth)}", f"{n_r:+d}"])
    table(rows_t)
    table([["Defecto"] + names] + [[k] + ["falla" if x else "—" for x in row] for k, row in zip(DEFECTS, mat)])
    print("  matriz:", json.dumps(mat))
    print(f"  defectos que ninguna comprobación ve: {[k for k, row in zip(DEFECTS, mat) if not any(row)]}")
    print(f"  comprobaciones que no vieron ningún defecto: {[n for i, n in enumerate(names) if not any(r[i] for r in mat)]}")
    # los ocho juntos y arreglo uno a uno
    active = set(DEFECTS)
    seq = []
    _, mart = run_pipeline(orders, active, runs=2)
    seq.append(("los ocho defectos", sum(1 for d in truth if mart.get(d) != truth[d]), sum(c for c, _ in mart.values()) - tr_rows))
    for k in ["D1", "D8", "D5", "D4", "D3", "D2", "D7", "D6"]:
        active.discard(k)
        _, mart = run_pipeline(orders, active, runs=2)
        seq.append((f"corregido {k}", sum(1 for d in truth if mart.get(d) != truth[d]), sum(c for c, _ in mart.values()) - tr_rows))
    table([["Paso", "Días con resultado distinto", "Filas de más o de menos"]] + [[a, b, f"{c:+d}"] for a, b, c in seq])


# ====================================================================== SE-552
BASE_PLATFORM = {
    "raw_orders": {"owner": "equipo-pedidos", "layer": "raw", "columns": {"order_id": "INT", "email": "TEXT", "amount": "INT", "day": "INT"}, "pii": ["email"], "retention_days": 400,
                   "checks": ["unique:order_id", "rows>0"], "inputs": [], "max_age_days": 1},
    "stg_orders": {"owner": "equipo-datos", "layer": "staging", "columns": {"order_id": "INT", "customer_key": "TEXT", "amount": "INT", "day": "INT"}, "pii": [], "retention_days": 400,
                   "checks": ["unique:order_id", "rows>0"], "inputs": ["raw_orders"], "max_age_days": 1},
    "mart_daily": {"owner": "equipo-analitica", "layer": "mart", "columns": {"day": "INT", "orders": "INT", "revenue": "INT"}, "pii": [], "retention_days": 1000,
                   "checks": ["unique:day", "rows>0"], "inputs": ["stg_orders"], "max_age_days": 1},
}
SQL = {
    "stg_orders": "SELECT order_id, hex(substr(email,1,3)) || '-' || order_id AS customer_key, amount, day FROM raw_orders",
    "mart_daily": "SELECT day, COUNT(*) AS orders, SUM(amount) AS revenue FROM stg_orders GROUP BY day",
}


def build_platform(sql, phys, today=30, stale=False):
    con = mem_db()
    rng = random.Random(SEED)
    last = today - (3 if stale else 0)
    con.execute("CREATE TABLE raw_orders(order_id INT, email TEXT, amount INT, day INT)")
    con.executemany("INSERT INTO raw_orders VALUES(?,?,?,?)", [(i, f"u{i}@ejemplo.test", rng.randrange(1000, 9000), rng.randrange(0, last + 1)) for i in range(5000)])
    for t in ("stg_orders", "mart_daily"):
        cols = ", ".join(f"{c} {ty}" for c, ty in phys[t].items())
        con.execute(f"CREATE TABLE {t}({cols})")
        con.execute(f"INSERT INTO {t} {sql[t]}")
    return con


def gate(spec, sql, con, today=30):
    """Reglas de gobierno evaluadas sobre la plataforma construida. Devuelve las reglas que fallan."""
    failed = defaultdict(list)
    for name, d in spec.items():
        if not d.get("owner"):
            failed["R1 dueño"].append(name)
        actual = {r[1]: r[2] for r in con.execute(f"PRAGMA table_info({name})")}
        if actual != d["columns"]:
            failed["R2 contrato"].append(name)
        if not d.get("checks"):
            failed["R3 comprobaciones"].append(name)
        else:
            for c in d["checks"]:
                if c == "rows>0" and con.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0] == 0:  # nosec B608
                    failed["R3 comprobaciones"].append(name)
                if c.startswith("unique:"):
                    col = c.split(":")[1]
                    if col in actual and con.execute(f"SELECT COUNT(*) - COUNT(DISTINCT {col}) FROM {name}").fetchone()[0] > 0:  # nosec B608
                        failed["R3 comprobaciones"].append(name)
        if d["layer"] == "mart":
            exposed = [c for c in actual if c in {p for s in spec.values() for p in s["pii"]} | {"email", "phone"}]
            if exposed:
                failed["R4 datos personales"].append(name)
        if d.get("retention_days") is None:
            failed["R5 retención"].append(name)
        elif "day" in actual and con.execute(f"SELECT COUNT(*) FROM {name} WHERE day < ?", (today - d["retention_days"],)).fetchone()[0] > 0:  # nosec B608
            failed["R5 retención"].append(name)
        if name in sql:
            found = set(re.findall(r"(?:FROM|JOIN)\s+(\w+)", sql[name]))
            if found != set(d["inputs"]):
                failed["R6 linaje declarado"].append(name)
        newest = con.execute(f"SELECT MAX(day) FROM {name}").fetchone()[0] if "day" in actual else today  # nosec B608
        if newest is None or today - newest > d["max_age_days"]:
            failed["R7 frescura"].append(name)
    return {k: sorted(set(v)) for k, v in failed.items()}


def e552():
    print("SE-552 — proyecto: plataforma de datos mínima gobernada")
    con = build_platform(SQL, {k: dict(v["columns"]) for k, v in BASE_PLATFORM.items() if k != "raw_orders"})
    base = gate(BASE_PLATFORM, SQL, con)
    print(f"  plataforma base de 3 conjuntos (raw, staging, mart): reglas que fallan: {base or 'ninguna'}")
    P0 = {k: dict(v["columns"]) for k, v in BASE_PLATFORM.items() if k != "raw_orders"}
    def m_owner(s, q, p):
        s["stg_orders"]["owner"] = ""
    def m_contract(s, q, p):
        q["mart_daily"] = q["mart_daily"].replace("SUM(amount) AS revenue", "SUM(amount) AS revenue, MAX(amount) AS biggest")
        p["mart_daily"]["biggest"] = "INT"
    def m_pii(s, q, p):
        q["mart_daily"] = "SELECT day, COUNT(*) AS orders, SUM(amount) AS revenue, MIN(customer_key) AS email FROM stg_orders GROUP BY day"
        p["mart_daily"]["email"] = "TEXT"
        s["mart_daily"]["columns"]["email"] = "TEXT"
    def m_retention(s, q, p):
        s["raw_orders"]["retention_days"] = 10
    def m_checks(s, q, p):
        s["stg_orders"]["checks"] = []
    def m_lineage(s, q, p):
        q["mart_daily"] = q["mart_daily"].replace("FROM stg_orders", "FROM raw_orders")
    def m_type(s, q, p):
        s["mart_daily"]["columns"]["revenue"] = "REAL"
    def m_stale(s, q, p):
        pass
    def m_nullretention(s, q, p):
        s["mart_daily"]["retention_days"] = None
    def m_semantic(s, q, p):
        q["mart_daily"] = q["mart_daily"].replace("SUM(amount) AS revenue", "MAX(amount) AS revenue")
    cases = [("quitar el dueño de un conjunto", m_owner, {}), ("añadir una columna al mart sin actualizar el contrato", m_contract, {}),
             ("exponer una columna de correo en el mart (contrato actualizado)", m_pii, {}), ("retención declarada de 10 días sin purga", m_retention, {}),
             ("quitar todas las comprobaciones de un conjunto", m_checks, {}), ("el mart lee de raw sin declararlo", m_lineage, {}),
             ("cambiar el tipo declarado de una columna", m_type, {}), ("datos con 3 días de atraso", m_stale, {"stale": True}),
             ("retención sin declarar", m_nullretention, {}), ("el ingreso pasa de SUM a MAX (cambio semántico)", m_semantic, {})]
    rows = [["Mutación", "Reglas del gate que la detectan"]]
    only_schema = 0
    caught = 0
    for name, fn, kw in cases:
        s, q, p = copy.deepcopy(BASE_PLATFORM), dict(SQL), copy.deepcopy(P0)
        fn(s, q, p)
        c = build_platform(q, p, **kw)
        failed = gate(s, q, c)
        rows.append([name, ", ".join(sorted(failed)) or "NINGUNA"])
        caught += bool(failed)
        only_schema += "R2 contrato" in failed
    table(rows)
    print(f"  el gate de siete reglas detecta {caught} de {len(cases)} mutaciones; un gate que solo compara el esquema detecta {only_schema}; la mutación semántica pasa las siete reglas")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    which = sys.argv[1:] or ["549", "550", "551", "552"]
    for key in which:
        globals()[f"e{key}"]()
        print()
