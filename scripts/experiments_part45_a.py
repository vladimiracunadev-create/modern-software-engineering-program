"""Experimentos de las clases SE-541 a SE-544 (Parte 45): del dato operacional al analítico, ingesta,
modelado analítico y transformación idempotente.

Uso: python scripts/experiments_part45_a.py [541|542|543|544]

No se invoca ningún modelo de lenguaje. Biblioteca estándar y el caso conductor *Avisos*. Los
parámetros (volúmenes, retrasos, tasas de duplicado) los fija el autor y se declaran en la salida; los
tiempos y los tamaños en disco se miden de verdad y varían de un equipo a otro.
"""
from __future__ import annotations

import hashlib
import itertools
import os
import random
import sqlite3
import sys
import tempfile
from collections import defaultdict

from experiments_part45_lab import SEED, fmt, mem_db, pct, table, timed


# ====================================================================== SE-541
def e541():
    print("SE-541 — del dato operacional al analítico")
    rng = random.Random(SEED)
    n = 200_000
    con = mem_db()
    con.execute("CREATE TABLE orders(id INTEGER PRIMARY KEY, customer INT, day INT, amount INT, status TEXT, note TEXT)")
    rows = [(i, rng.randrange(5000), rng.randrange(365), rng.randrange(500, 50000), rng.choice(["new", "paid", "shipped", "delivered"]),
             "nota-" + "x" * rng.randrange(20, 60)) for i in range(n)]
    con.executemany("INSERT INTO orders VALUES(?,?,?,?,?,?)", rows)
    con.commit()
    page_size = con.execute("PRAGMA page_size").fetchone()[0]
    pages = con.execute("PRAGMA page_count").fetchone()[0]
    table_bytes = page_size * pages
    needed = n * 8 * 2  # dos columnas enteras de 8 bytes
    ids = [rng.randrange(n) for _ in range(2000)]
    t_point, _ = timed(lambda: [con.execute("SELECT * FROM orders WHERE id=?", (i,)).fetchone() for i in ids], 3)
    t_scan, res = timed(lambda: con.execute("SELECT day, SUM(amount) FROM orders GROUP BY day").fetchall(), 3)
    con.execute("CREATE INDEX ix_day_amount ON orders(day, amount)")
    t_cover, _ = timed(lambda: con.execute("SELECT day, SUM(amount) FROM orders GROUP BY day").fetchall(), 3)
    plan = con.execute("EXPLAIN QUERY PLAN SELECT day, SUM(amount) FROM orders GROUP BY day").fetchall()[0][-1]
    print(f"  tabla de {n} pedidos: {table_bytes/1e6:.1f} MB en {pages} páginas de {page_size} bytes; las dos columnas que necesita la agregación suman {needed/1e6:.1f} MB ({fmt(needed/table_bytes*100,1)} % de la tabla)")
    print(f"  2000 búsquedas por clave: {fmt(t_point,1)} ms en total ({fmt(t_point/2000*1000,1)} µs por búsqueda); agregación por día sobre toda la tabla: {fmt(t_scan,1)} ms ({fmt(t_scan/(t_point/2000),0)} veces una búsqueda)")
    print(f"  con un índice que cubre día e importe: {fmt(t_cover,1)} ms; plan: {plan}")
    # historia: la tabla operacional guarda solo el estado actual
    m = 20_000
    states = ["created", "paid", "shipped", "delivered"]
    events, current = [], {}
    for oid in range(m):
        day = rng.randrange(0, 200)
        for st in states:
            events.append((oid, st, day))
            current[oid] = st
            day += rng.randrange(1, 6)
            if rng.random() < 0.08:
                break
    d = 100
    stay = defaultdict(list)
    for oid, st, day in events:
        stay[oid].append((st, day))
    in_paid = 0
    for oid, hist in stay.items():
        for i, (st, day) in enumerate(hist):
            nxt = hist[i + 1][1] if i + 1 < len(hist) else 10**9
            if st == "paid" and day <= d < nxt:
                in_paid += 1
    from_current = sum(1 for s in current.values() if s == "paid")
    print(f"  {m} pedidos con {len(events)} cambios de estado: «¿cuántos estaban pagados y sin enviar el día {d}?» respuesta con el registro de eventos: {in_paid}; con la tabla de estado actual solo se puede decir cuántos están pagados hoy: {from_current}")
    # bloqueo entre lectura larga y escritura (diario de reversión frente a WAL)
    out = []
    for mode in ("delete", "wal"):
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
            path = os.path.join(tmp, "o.db")
            w = sqlite3.connect(path, timeout=0, isolation_level=None)
            w.execute(f"PRAGMA journal_mode={mode}")
            w.execute("CREATE TABLE t(a INT)")
            w.executemany("INSERT INTO t VALUES(?)", [(i,) for i in range(1000)])
            r = sqlite3.connect(path, timeout=0, isolation_level=None)
            r.execute("BEGIN")
            cur = r.execute("SELECT a FROM t")
            cur.fetchone()
            try:
                w.execute("BEGIN IMMEDIATE")
                w.execute("INSERT INTO t VALUES(-1)")
                w.execute("COMMIT")
                res_w = "la escritura se confirma mientras la lectura sigue abierta"
            except sqlite3.OperationalError as exc:
                res_w = f"la escritura falla: {exc}"
                try:
                    w.execute("ROLLBACK")
                except sqlite3.OperationalError:
                    pass
            cur.close()
            r.execute("COMMIT")
            out.append((mode, res_w))
            r.close()
            w.close()
    for mode, res_w in out:
        print(f"  modo {mode}: {res_w}")
    rows_t = [["Consulta", "Filas que toca", "Bytes que necesita", "Tiempo"],
              ["Búsqueda por clave", 1, "una página", f"{fmt(t_point/2000*1000,1)} µs"],
              ["Agregación por día", n, f"{needed/1e6:.1f} MB de {table_bytes/1e6:.1f} MB", f"{fmt(t_scan,1)} ms"]]
    table(rows_t)


# ====================================================================== SE-542
def gen_events(rng, n=10_000):
    ev = []
    for i in range(n):
        t = rng.uniform(0, 86400)
        delay = rng.expovariate(1 / 20)
        if rng.random() < 0.03:
            delay = rng.uniform(3600, 6 * 3600)
        ev.append({"id": i, "t": t, "arr": t + delay})
        if rng.random() < 0.02:  # redelivery: at-least-once
            ev.append({"id": i, "t": t, "arr": t + delay + rng.uniform(5, 600)})
    return ev


def e542():
    print("SE-542 — ingesta batch y streaming")
    rng = random.Random(SEED)
    ev = gen_events(rng)
    uniq = {e["id"] for e in ev}
    print(f"  {len(ev)} entregas de {len(uniq)} eventos únicos ({len(ev)-len(uniq)} duplicados por reentrega); 3 % llegan entre 1 y 6 horas tarde")
    hour = lambda t: int(t // 3600)
    truth = defaultdict(int)
    first = {}
    for e in ev:
        if e["id"] not in first:
            first[e["id"]] = e
    for e in first.values():
        truth[hour(e["t"])] += 1
    # sin deduplicar
    raw = defaultdict(int)
    for e in ev:
        raw[hour(e["t"])] += 1
    err_nodedup = sum(abs(raw[h] - truth[h]) for h in truth) / sum(truth.values()) * 100
    print(f"  contar entregas sin deduplicar infla las ventanas un {fmt(err_nodedup,2)} % del total")
    rows = [["Política", "Eventos fuera de su ventana", "Error en ventanas (% del total)", "Retraso hasta emitir"]]
    for name, lateness in [("flujo sin tolerancia", 0), ("flujo con marca de agua de 1 min", 60), ("flujo con marca de agua de 10 min", 600),
                           ("flujo con marca de agua de 1 h", 3600), ("flujo con marca de agua de 6 h", 6 * 3600)]:
        got = defaultdict(int)
        seen = set()
        dropped = 0
        for e in sorted(ev, key=lambda x: x["arr"]):
            if e["id"] in seen:
                continue
            win_end = (hour(e["t"]) + 1) * 3600
            if e["arr"] > win_end + lateness:
                dropped += 1
                seen.add(e["id"])
                continue
            seen.add(e["id"])
            got[hour(e["t"])] += 1
        err = sum(abs(got[h] - truth[h]) for h in truth) / sum(truth.values()) * 100
        rows.append([name, dropped, fmt(err, 2), f"{lateness/60:g} min"])
    # lotes: nocturno a las 02:00 del día siguiente, y reproceso a los 3 días
    for name, cutoff in [("lote nocturno a las 02:00 del día siguiente", 86400 + 7200), ("lote con reproceso 3 días después", 86400 * 4)]:
        got = defaultdict(int)
        seen = set()
        dropped = 0
        for e in sorted(ev, key=lambda x: x["arr"]):
            if e["id"] in seen:
                continue
            seen.add(e["id"])
            if e["arr"] > cutoff:
                dropped += 1
                continue
            got[hour(e["t"])] += 1
        err = sum(abs(got[h] - truth[h]) for h in truth) / sum(truth.values()) * 100
        rows.append([name, dropped, fmt(err, 2), f"{(cutoff-86400)/3600:g} h tras cerrar el día"])
    table(rows)
    # latencia de reflejo: tiempo entre el evento y su aparición en el resultado
    lat_stream = [e["arr"] - e["t"] for e in first.values()]
    print(f"  retraso entre el evento y su llegada al sistema: mediana {fmt(pct(lat_stream,0.5),1)} s, p99 {fmt(pct(lat_stream,0.99),0)} s; un lote nocturno añade hasta 24 h")
    # idempotencia de la entrega por clave
    sink = {}
    applied = 0
    for e in sorted(ev, key=lambda x: x["arr"]):
        if e["id"] not in sink:
            sink[e["id"]] = e["t"]
            applied += 1
    print(f"  escritura por clave: {applied} filas aplicadas de {len(ev)} entregas (las {len(ev)-applied} reentregas no cambian el resultado)")


# ====================================================================== SE-543
def e543():
    print("SE-543 — modelado analítico: dimensional y Data Vault")
    rng = random.Random(SEED)
    con = mem_db()
    con.executescript("""
    CREATE TABLE customer_hist(customer_id INT, city TEXT, valid_from INT, valid_to INT);
    CREATE TABLE orders(order_id INT PRIMARY KEY, customer_id INT, day INT, shipping_fee INT);
    CREATE TABLE items(order_id INT, line INT, product INT, qty INT, price INT);
    """)
    cities = ["Santiago", "Valparaiso", "Concepcion", "Temuco"]
    n_c, moved = 1000, 0
    cur_city = {}
    for c in range(n_c):
        city = rng.choice(cities)
        if rng.random() < 0.15:
            day_move = rng.randrange(100, 250)
            new = rng.choice([x for x in cities if x != city])
            con.execute("INSERT INTO customer_hist VALUES(?,?,?,?)", (c, city, 0, day_move))
            con.execute("INSERT INTO customer_hist VALUES(?,?,?,?)", (c, new, day_move, 10_000))
            cur_city[c] = new
            moved += 1
        else:
            con.execute("INSERT INTO customer_hist VALUES(?,?,?,?)", (c, city, 0, 10_000))
            cur_city[c] = city
    oid = 0
    for _ in range(20_000):
        c, day = rng.randrange(n_c), rng.randrange(365)
        con.execute("INSERT INTO orders VALUES(?,?,?,?)", (oid, c, day, 500))
        for line in range(rng.randrange(1, 6)):
            con.execute("INSERT INTO items VALUES(?,?,?,?,?)", (oid, line, rng.randrange(200), rng.randrange(1, 4), rng.randrange(1000, 9000)))
        oid += 1
    con.execute("CREATE TABLE dim_customer_cur AS SELECT customer_id, city FROM customer_hist WHERE valid_to=10000")
    q_cur = dict(con.execute("""SELECT d.city, SUM(i.qty*i.price) FROM items i JOIN orders o USING(order_id)
                               JOIN dim_customer_cur d USING(customer_id) GROUP BY d.city""").fetchall())
    q_scd2 = dict(con.execute("""SELECT d.city, SUM(i.qty*i.price) FROM items i JOIN orders o USING(order_id)
                                JOIN customer_hist d ON d.customer_id=o.customer_id AND o.day>=d.valid_from AND o.day<d.valid_to GROUP BY d.city""").fetchall())
    total = con.execute("SELECT SUM(qty*price) FROM items").fetchone()[0]
    print(f"  {n_c} clientes, {moved} se mudaron; {oid} pedidos con {con.execute('SELECT COUNT(*) FROM items').fetchone()[0]} líneas; ventas totales {total}")
    rows = [["Ciudad", "Ventas con la ciudad actual", "Ventas con la ciudad de la fecha", "Diferencia"]]
    for c in cities:
        rows.append([c, q_cur[c], q_scd2[c], q_scd2[c] - q_cur[c]])
    table(rows)
    print(f"  suma de las dos columnas: {sum(q_cur.values())} y {sum(q_scd2.values())} (ambas igual al total; cambia el reparto, no el total)")
    # fan-out: sumar un atributo del pedido tras unirlo con las líneas
    true_fee = con.execute("SELECT SUM(shipping_fee) FROM orders").fetchone()[0]
    fan = con.execute("SELECT SUM(o.shipping_fee) FROM orders o JOIN items i USING(order_id)").fetchone()[0]
    fan_fixed = con.execute("SELECT SUM(fee) FROM (SELECT o.shipping_fee AS fee FROM orders o WHERE EXISTS(SELECT 1 FROM items i WHERE i.order_id=o.order_id))").fetchone()[0]
    print(f"  envío total real {true_fee}; sumado tras unir con las líneas {fan} ({fmt((fan/true_fee-1)*100,1)} % de más); con un grano por pedido {fan_fixed}")
    # Data Vault: carga insertar-solamente e idempotente
    con.executescript("""
    CREATE TABLE hub_customer(hk TEXT PRIMARY KEY, customer_id INT, load_day INT);
    CREATE TABLE sat_customer(hk TEXT, load_day INT, hashdiff TEXT, city TEXT, PRIMARY KEY(hk, hashdiff));
    CREATE TABLE hub_order(hk TEXT PRIMARY KEY, order_id INT, load_day INT);
    CREATE TABLE link_order_customer(hk TEXT PRIMARY KEY, hk_order TEXT, hk_customer TEXT, load_day INT);
    """)
    h = lambda *p: hashlib.md5("|".join(str(x) for x in p).encode(), usedforsecurity=False).hexdigest()

    def load(day):
        for (c, city, vf, vt) in con.execute("SELECT * FROM customer_hist WHERE valid_from<=? AND valid_to>?", (day, day)).fetchall():
            con.execute("INSERT OR IGNORE INTO hub_customer VALUES(?,?,?)", (h(c), c, day))
            con.execute("INSERT OR IGNORE INTO sat_customer VALUES(?,?,?,?)", (h(c), day, h(city), city))
        for (o, c, d, fee) in con.execute("SELECT * FROM orders WHERE day<=?", (day,)).fetchall():
            con.execute("INSERT OR IGNORE INTO hub_order VALUES(?,?,?)", (h(o), o, day))
            con.execute("INSERT OR IGNORE INTO link_order_customer VALUES(?,?,?,?)", (h(o, c), h(o), h(c), day))

    counts = []
    for day in (0, 100, 250, 250):
        load(day)
        counts.append((day, *[con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0] for t in ("hub_customer", "sat_customer", "hub_order", "link_order_customer")]))  # nosec B608
    rows = [["Carga del día", "hub_customer", "sat_customer", "hub_order", "link_order_customer"]] + [list(c) for c in counts]
    table(rows)
    print(f"  la carga repetida del día 250 no añade filas: {counts[-1][1:] == counts[-2][1:]}")
    # consulta de «cómo era en una fecha» sobre el satélite
    when = con.execute("SELECT COUNT(*) FROM sat_customer").fetchone()[0]
    print(f"  satélite de clientes con {when} filas: {n_c} versiones iniciales y {when-n_c} cambios de ciudad conservados")
    # costo de consulta: estrella frente a vault con uniones
    q1 = "SELECT d.city, SUM(i.qty*i.price) FROM items i JOIN orders o USING(order_id) JOIN dim_customer_cur d USING(customer_id) GROUP BY d.city"
    q2 = """SELECT s.city, SUM(i.qty*i.price) FROM items i JOIN hub_order ho ON ho.order_id=i.order_id JOIN link_order_customer l ON l.hk_order=ho.hk
            JOIN sat_customer s ON s.hk=l.hk_customer GROUP BY s.city"""
    t1, _ = timed(lambda: con.execute(q1).fetchall(), 3)
    t2, _ = timed(lambda: con.execute(q2).fetchall(), 3)
    print(f"  la misma pregunta: estrella con una unión por dimensión {fmt(t1,1)} ms; vault con hub, enlace y satélite {fmt(t2,1)} ms (el vault no se consulta directo: se construye una vista de negocio encima)")


# ====================================================================== SE-544
def run_load(strategy, src, fail_day=None, fail_after=None, txn=True, retry=True):
    con = mem_db()
    con.execute("CREATE TABLE fact(day INT, key INT, amount INT, PRIMARY KEY(day, key) ON CONFLICT REPLACE)" if strategy == "merge"
                else "CREATE TABLE fact(day INT, key INT, amount INT)")
    def load_day(day, boom):
        rows = src[day]
        if txn:
            con.execute("BEGIN")
        if strategy == "delete-insert":
            con.execute("DELETE FROM fact WHERE day=?", (day,))
        for i, (k, a) in enumerate(rows):
            if boom and i == len(rows) // 2:
                if txn:
                    con.execute("ROLLBACK")
                raise RuntimeError("fallo a mitad de la partición")
            con.execute("INSERT INTO fact VALUES(?,?,?)", (day, k, a))
        if txn:
            con.execute("COMMIT")
    con.isolation_level = None
    for day in sorted(src):
        try:
            load_day(day, boom=(day == fail_day))
        except RuntimeError:
            if retry:
                load_day(day, boom=False)
    return con


def e544():
    print("SE-544 — transformación y orquestación idempotente con backfills")
    rng = random.Random(SEED)
    src = {d: [(k, rng.randrange(100, 9000)) for k in range(rng.randrange(40, 80))] for d in range(30)}
    truth_rows = sum(len(v) for v in src.values())
    truth_sum = sum(a for v in src.values() for _, a in v)
    rows = [["Estrategia", "Escenario", "Filas", "Suma de importes", "¿Coincide con la verdad?"]]
    cases = [("append", "ejecución limpia", {}), ("append", "fallo en el día 17 y reintento, con transacción", {"fail_day": 17}),
             ("append", "fallo en el día 17 y reintento, sin transacción", {"fail_day": 17, "txn": False}),
             ("delete-insert", "fallo en el día 17 y reintento, sin transacción", {"fail_day": 17, "txn": False}),
             ("merge", "fallo en el día 17 y reintento, sin transacción", {"fail_day": 17, "txn": False}),
             ("delete-insert", "fallo en el día 17 y reintento, con transacción", {"fail_day": 17})]
    for strat, name, kw in cases:
        con = run_load(strat, src, **kw)
        n, s = con.execute("SELECT COUNT(*), SUM(amount) FROM fact").fetchone()
        rows.append([strat, name, n, s, "sí" if (n, s) == (truth_rows, truth_sum) else f"no ({n-truth_rows:+d} filas)"])
    table(rows)
    # doble ejecución de todo el trabajo
    for strat in ("append", "delete-insert", "merge"):
        con = run_load(strat, src)
        for day in sorted(src):
            if strat == "delete-insert":
                con.execute("DELETE FROM fact WHERE day=?", (day,))
            for k, a in src[day]:
                con.execute("INSERT INTO fact VALUES(?,?,?)", (day, k, a))
        n = con.execute("SELECT COUNT(*) FROM fact").fetchone()[0]
        print(f"  {strat}: tras ejecutar los 30 días dos veces hay {n} filas (verdad {truth_rows})")
    # backfill: la fuente se corrige en los días 5 a 9
    con = run_load("delete-insert", src)
    for d in range(5, 10):
        src[d] = [(k, a + 100) for k, a in src[d]]
    stale = con.execute("SELECT COUNT(*) FROM fact WHERE day BETWEEN 5 AND 9").fetchone()[0]
    con.execute("BEGIN")
    for d in range(5, 10):
        con.execute("DELETE FROM fact WHERE day=?", (d,))
        for k, a in src[d]:
            con.execute("INSERT INTO fact VALUES(?,?,?)", (d, k, a))
    con.execute("COMMIT")
    s = con.execute("SELECT SUM(amount) FROM fact").fetchone()[0]
    print(f"  backfill de los días 5 a 9: se reescriben {stale} filas de {truth_rows} ({fmt(stale/truth_rows*100,1)} %); la suma pasa a coincidir con la fuente corregida: {s == sum(a for v in src.values() for _, a in v)}")
    # grafo de dependencias y qué hay que recalcular
    deps = {"raw_orders": [], "raw_customers": [], "stg_orders": ["raw_orders"], "stg_customers": ["raw_customers"],
            "dim_customer": ["stg_customers"], "fact_sales": ["stg_orders", "dim_customer"], "mart_daily": ["fact_sales"],
            "mart_city": ["fact_sales", "dim_customer"], "report_exec": ["mart_daily", "mart_city"]}
    order, ready, indeg = [], [k for k, v in deps.items() if not v], {k: len(v) for k, v in deps.items()}
    rev = defaultdict(list)
    for k, v in deps.items():
        for p in v:
            rev[p].append(k)
    while ready:
        ready.sort()
        n = ready.pop(0)
        order.append(n)
        for c in rev[n]:
            indeg[c] -= 1
            if indeg[c] == 0:
                ready.append(c)
    def downstream(x):
        out, stack = set(), [x]
        while stack:
            for c in rev[stack.pop()]:
                if c not in out:
                    out.add(c)
                    stack.append(c)
        return out
    print(f"  orden topológico de {len(order)} tareas: {' > '.join(order)}")
    for x in ("raw_customers", "raw_orders", "fact_sales"):
        print(f"  si cambia {x}, hay que recalcular {len(downstream(x))} tareas: {sorted(downstream(x))}")
    # datos tardíos y ventana de reproceso
    rows = [["Ventana de reproceso (días)", "Filas tardías perdidas", "Filas reprocesadas por ejecución"]]
    late = []
    for d in range(60):
        for _ in range(100):
            delay = 0 if rng.random() < 0.9 else rng.choice([1, 1, 2, 3, 5])
            late.append((d, d + delay))  # (día del evento, día de llegada)
    for w in (0, 1, 2, 3, 6):
        captured = set()
        for run in range(60 + 6):
            lo = run - w
            for i, (ev, arr) in enumerate(late):
                if arr <= run and ev >= lo and ev <= run:
                    captured.add(i)
        lost = len(late) - len(captured)
        rows.append([w, lost, 100 * (w + 1)])
    table(rows)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    which = sys.argv[1:] or ["541", "542", "543", "544"]
    for key in which:
        globals()[f"e{key}"]()
        print()
