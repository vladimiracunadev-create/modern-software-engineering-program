"""Experimentos de las clases SE-365 a SE-368 (Parte 30): calidad y observabilidad, contratos y evolución de
esquemas, linaje y catálogo, y almacenes, lagos y formatos columnares.

Uso: python scripts/experiments_part30_b.py [545|546|547|548]

No se invoca ningún modelo de lenguaje. Biblioteca estándar y el caso conductor *Avisos*. Los
parámetros los fija el autor y se declaran en la salida; los tiempos y los tamaños en disco se miden de
verdad y varían de un equipo a otro.
"""
from __future__ import annotations

import array
import json
import os
import random
import re
import sqlite3
import statistics
import struct
import sys
import tempfile
import time
import zlib
from collections import defaultdict

from experiments_part30_lab import SEED, fmt, mem_db, pct, table, timed


# ====================================================================== SE-365
def series(rng, days=120):
    rows, amounts = [], []
    for d in range(days):
        base = 10_000 * (0.6 if d % 7 in (5, 6) else 1.0)
        n = int(base * rng.uniform(0.96, 1.04))
        amt = 100 * rng.uniform(0.97, 1.03)
        rows.append(n)
        amounts.append(amt)
    return rows, amounts


def e545():
    print("SE-365 — calidad y observabilidad de datos")
    rng = random.Random(SEED)
    rows, amounts = series(rng)
    incidents = {42: ("carga parcial en día hábil (50 %)", 0.5), 54: ("carga parcial en sábado (70 %)", 0.7), 71: ("duplicados (el doble de filas)", 2.0), 89: ("la carga no corrió, sábado (0 filas)", 0.0)}
    truth = set()
    for d, (_, k) in incidents.items():
        rows[d] = int(rows[d] * k)
        truth.add(d)
    for d in range(110, 120):
        amounts[d] *= 1.25  # deriva del importe medio (los días 110 a 119)
    def fixed(d):  # umbral fijo
        return rows[d] < 8000 or rows[d] > 12000
    def trailing(d):  # z-score sobre los 14 días anteriores, sin estacionalidad
        if d < 14:
            return False
        w = rows[d - 14:d]
        sd = statistics.pstdev(w) or 1
        return abs(rows[d] - statistics.mean(w)) / sd > 3
    def seasonal(d):  # mismo día de la semana de las 4 semanas anteriores, con mediana y MAD
        if d < 28:
            return False
        w = [rows[d - 7 * k] for k in (1, 2, 3, 4)]
        med = statistics.median(w)
        mad = statistics.median([abs(x - med) for x in w]) or 1
        return abs(rows[d] - med) > max(6 * mad, 0.15 * med)
    res = []
    for name, f in (("umbral fijo (menos de 8 000 o más de 12 000 filas)", fixed), ("z-score sobre 14 días sin estacionalidad", trailing), ("mediana del mismo día de la semana y MAD", seasonal)):
        flagged = {d for d in range(120) if f(d)}
        tp = len(flagged & truth)
        fp = len(flagged - truth)
        res.append((name, tp, fp, len(truth) - tp))
    print(f"  120 días, caída normal de fin de semana al 60 %; cuatro incidentes de volumen sembrados en los días 42, 54, 71 y 89")
    table([["Detector de volumen", "Incidentes vistos", "Falsas alarmas", "Incidentes perdidos"]] + [list(r) for r in res])
    # deriva del importe medio: detección por distribución
    base_mean = statistics.mean(amounts[:100])
    drift_days = [d for d in range(120) if abs(amounts[d] / base_mean - 1) > 0.1]
    print(f"  deriva del importe medio (+25 % desde el día 110): la comprobación de distribución con banda del 10 % marca los días {drift_days[0]} a {drift_days[-1]} ({len(drift_days)} días); las comprobaciones de volumen no la ven")
    # matriz incidente por comprobación sobre una tabla real en SQLite
    con = mem_db()
    def build(variant):
        con.executescript("DROP TABLE IF EXISTS cust; DROP TABLE IF EXISTS ord; CREATE TABLE cust(id INTEGER PRIMARY KEY, city TEXT); CREATE TABLE ord(id INT, customer_id INT, amount REAL, day INT, loaded_at INT);")
        r = random.Random(SEED)
        con.executemany("INSERT INTO cust VALUES(?,?)", [(i, r.choice(["A", "B", "C"])) for i in range(500)])
        recs = [(i, r.randrange(500), r.uniform(50, 150), 6, 100) for i in range(5000)]
        if variant == "carga parcial":
            recs = recs[:2500]
        elif variant == "duplicados":
            recs = recs + recs[:2500]
        elif variant == "nulos en el cliente":
            recs = [(a, (None if i % 4 == 0 else b), c, d, e) for i, (a, b, c, d, e) in enumerate(recs)]
        elif variant == "clientes huérfanos":
            recs = [(a, (b + 1000 if i % 10 == 0 else b), c, d, e) for i, (a, b, c, d, e) in enumerate(recs)]
        elif variant == "datos atrasados":
            recs = [(a, b, c, d, 100 - 30) for (a, b, c, d, e) in recs]
        elif variant == "importes en centavos":
            recs = [(a, b, c * 100, d, e) for (a, b, c, d, e) in recs]
        con.executemany("INSERT INTO ord VALUES(?,?,?,?,?)", recs)
    checks = {
        "volumen": lambda: abs(con.execute("SELECT COUNT(*) FROM ord").fetchone()[0] - 5000) / 5000 > 0.1,
        "unicidad": lambda: con.execute("SELECT COUNT(*)-COUNT(DISTINCT id) FROM ord").fetchone()[0] > 0,
        "nulos": lambda: con.execute("SELECT AVG(customer_id IS NULL) FROM ord").fetchone()[0] > 0.01,
        "integridad referencial": lambda: con.execute("SELECT COUNT(*) FROM ord o LEFT JOIN cust c ON c.id=o.customer_id WHERE o.customer_id IS NOT NULL AND c.id IS NULL").fetchone()[0] > 0,
        "frescura": lambda: 100 - con.execute("SELECT MAX(loaded_at) FROM ord").fetchone()[0] > 24,
        "distribución": lambda: abs(con.execute("SELECT AVG(amount) FROM ord").fetchone()[0] / 100 - 1) > 0.1,
    }
    variants = ["limpia", "carga parcial", "duplicados", "nulos en el cliente", "clientes huérfanos", "datos atrasados", "importes en centavos"]
    rows_t = [["Variante"] + list(checks)]
    mat = []
    for v in variants:
        build(v)
        res = [bool(c()) for c in checks.values()]
        mat.append(res)
        rows_t.append([v] + ["falla" if x else "—" for x in res])
    table(rows_t)
    print("  matriz:", json.dumps(mat))


# ====================================================================== SE-366
PRIM = {"int": 0, "long": 1, "float": 2, "double": 3, "string": 9, "bool": 8}


def promotable(w, r):
    return w == r or (w in ("int", "long", "float") and r in ("long", "float", "double") and PRIM[w] < PRIM[r])


def can_read(writer, reader):
    """¿Un lector con el esquema ``reader`` entiende datos escritos con ``writer``?"""
    for name, (rtype, rdefault) in reader.items():
        if name in writer:
            if not promotable(writer[name][0], rtype):
                return False
        elif rdefault is None:  # campo requerido que el escritor no trae
            return False
    return True


V1 = {"id": ("long", None), "student": ("string", None), "due_hours": ("int", None), "submitted": ("bool", None)}
CHANGES = {
    "añadir campo opcional con valor por defecto": lambda s: {**s, "channel": ("string", "email")},
    "añadir campo requerido sin valor por defecto": lambda s: {**s, "channel": ("string", None)},
    "quitar un campo con valor por defecto": lambda s: s,
    "quitar un campo requerido": lambda s: {k: v for k, v in s.items() if k != "due_hours"},
    "renombrar un campo": lambda s: {("hours_left" if k == "due_hours" else k): v for k, v in s.items()},
    "ampliar tipo int a long": lambda s: {**s, "due_hours": ("long", None)},
    "estrechar tipo long a int": lambda s: {**s, "id": ("int", None)},
    "cambiar tipo a texto": lambda s: {**s, "due_hours": ("string", None)},
    "cambiar la unidad de horas a minutos (mismo tipo)": lambda s: dict(s),
    "reordenar campos": lambda s: dict(reversed(list(s.items()))),
}


def e546():
    print("SE-366 — contratos de datos y evolución de esquemas")
    # el cambio «quitar un campo con valor por defecto» se evalúa sobre un esquema que ya tiene uno
    base = {**V1, "note": ("string", "")}
    rows = [["Cambio", "Retrocompatible (lector nuevo, datos viejos)", "Adelantecompatible (lector viejo, datos nuevos)", "Completa"]]
    results = {}
    for name, f in CHANGES.items():
        old = base if name.startswith("quitar un campo con") else V1
        new = ({k: v for k, v in old.items() if k != "note"} if name.startswith("quitar un campo con") else f(old))
        back = can_read(old, new)
        fwd = can_read(new, old)
        results[name] = (back, fwd)
        rows.append([name, "sí" if back else "NO", "sí" if fwd else "NO", "sí" if back and fwd else "NO"])
    table(rows)
    print("  el cambio de unidad conserva nombre y tipo: el verificador lo aprueba en las dos direcciones y los datos dejan de significar lo mismo")
    # lectura real de 1 000 registros escritos con el esquema viejo
    rng = random.Random(SEED)
    recs = [{"id": i, "student": f"s{rng.randrange(50)}", "due_hours": rng.randrange(0, 400), "submitted": rng.random() < 0.7} for i in range(1000)]
    def read(rec, reader):
        out = {}
        for name, (typ, default) in reader.items():
            if name in rec:
                v = rec[name]
                if typ == "string" and not isinstance(v, str):
                    raise TypeError(f"{name}: se esperaba texto")
                out[name] = v
            elif default is not None:
                out[name] = default
            else:
                raise KeyError(f"falta {name}")
        return out
    rows = [["Cambio", "Registros que el lector nuevo no puede leer (de 1 000)"]]
    for name, f in CHANGES.items():
        if name.startswith("quitar un campo con"):
            continue
        new = f(V1)
        bad = 0
        for rec in recs:
            try:
                read(rec, new)
            except (KeyError, TypeError):
                bad += 1
        rows.append([name, bad])
    table(rows)
    # expandir y contraer sobre una tabla real
    def old_reader(con):
        return con.execute("SELECT SUM(fee_cents) FROM t").fetchone()[0]
    def new_reader(con):
        return con.execute("SELECT SUM(amount_cents) FROM t").fetchone()[0]
    def attempt(fn):
        try:
            return fn()
        except sqlite3.OperationalError as exc:
            return f"ERROR ({exc})"
    con = mem_db()
    con.execute("CREATE TABLE t(id INT, fee_cents INT)")
    con.executemany("INSERT INTO t VALUES(?,?)", [(i, 100 + i) for i in range(100)])
    print("  renombrar de golpe (RENAME COLUMN fee_cents A amount_cents):")
    con.execute("ALTER TABLE t RENAME COLUMN fee_cents TO amount_cents")
    print(f"    lector viejo: {attempt(lambda: old_reader(con))}; lector nuevo: {attempt(lambda: new_reader(con))}")
    con = mem_db()
    con.execute("CREATE TABLE t(id INT, fee_cents INT)")
    con.executemany("INSERT INTO t VALUES(?,?)", [(i, 100 + i) for i in range(100)])
    steps = []
    def probe(label):
        steps.append([label, attempt(lambda: old_reader(con)), attempt(lambda: new_reader(con))])
    probe("estado inicial")
    con.execute("ALTER TABLE t ADD COLUMN amount_cents INT")
    probe("1. expandir: añadir la columna nueva")
    con.execute("CREATE TRIGGER sync AFTER INSERT ON t BEGIN UPDATE t SET amount_cents=NEW.fee_cents WHERE rowid=NEW.rowid AND NEW.amount_cents IS NULL; END")
    con.execute("UPDATE t SET amount_cents=fee_cents")
    probe("2. escribir en las dos y rellenar lo antiguo")
    con.execute("DROP TRIGGER sync")
    con.execute("ALTER TABLE t DROP COLUMN fee_cents")
    probe("3. contraer: quitar la columna vieja")
    table([["Paso", "Lector viejo", "Lector nuevo"]] + steps)
    print("  nota: el paso 3 solo es seguro cuando el lector viejo ya no existe; la tabla muestra por qué hay que esperar a eso")


# ====================================================================== SE-367
PIPE = [
    ("stg_orders", "CREATE TABLE stg_orders AS SELECT o.order_id AS order_id, o.customer_id AS customer_id, o.amount / 100.0 AS amount_clp, o.day AS day FROM raw_orders o WHERE o.status <> 'cancelled'"),
    ("stg_customers", "CREATE TABLE stg_customers AS SELECT c.customer_id AS customer_id, UPPER(c.city) AS city FROM raw_customers c"),
    ("fact_sales", "CREATE TABLE fact_sales AS SELECT s.order_id AS order_id, s.day AS day, s.amount_clp AS amount_clp, k.city AS city FROM stg_orders s JOIN stg_customers k ON k.customer_id = s.customer_id"),
    ("mart_city", "CREATE TABLE mart_city AS SELECT f.city AS city, SUM(f.amount_clp) AS total_clp, COUNT(*) AS n FROM fact_sales f GROUP BY f.city"),
    ("mart_daily", "CREATE TABLE mart_daily AS SELECT f.day AS day, SUM(f.amount_clp) AS total_clp FROM fact_sales f GROUP BY f.day"),
    ("report_top", "CREATE TABLE report_top AS SELECT m.city AS city, m.total_clp AS total_clp FROM mart_city m ORDER BY m.total_clp DESC LIMIT 3"),
]


def build_raw(con, seed=SEED, perturb=None):
    rng = random.Random(seed)
    for t in ("raw_orders", "raw_customers", "stg_orders", "stg_customers", "fact_sales", "mart_city", "mart_daily", "report_top"):
        con.execute(f"DROP TABLE IF EXISTS {t}")
    con.execute("CREATE TABLE raw_orders(order_id INT, customer_id INT, amount INT, status TEXT, day INT, note TEXT)")
    con.execute("CREATE TABLE raw_customers(customer_id INT, city TEXT, segment TEXT)")
    cities = ["Santiago", "Temuco", "Arica", "Puerto Montt", "Iquique"]
    con.executemany("INSERT INTO raw_customers VALUES(?,?,?)", [(i, rng.choice(cities), rng.choice(["a", "b"])) for i in range(300)])
    con.executemany("INSERT INTO raw_orders VALUES(?,?,?,?,?,?)", [(i, rng.randrange(300), rng.randrange(1000, 90000), rng.choice(["paid", "paid", "paid", "cancelled"]), rng.randrange(30), "n%d" % rng.randrange(9)) for i in range(3000)])
    if perturb:
        table_, col = perturb
        if col in ("amount", "day", "customer_id"):
            con.execute(f"UPDATE {table_} SET {col} = {col} + 7")  # nosec B608
        elif col == "status":
            con.execute(f"UPDATE {table_} SET status = CASE WHEN rowid % 5 = 0 THEN 'cancelled' ELSE status END")  # nosec B608
        elif col == "city":
            con.execute(f"UPDATE {table_} SET city = city || 'x' WHERE rowid % 3 = 0")  # nosec B608
        else:
            con.execute(f"UPDATE {table_} SET {col} = {col} || 'z'")  # nosec B608
    for _, sql in PIPE:
        con.execute(sql)


def snapshot(con):
    snap = {}
    for t in ("stg_orders", "stg_customers", "fact_sales", "mart_city", "mart_daily", "report_top"):
        cols = [r[1] for r in con.execute(f"PRAGMA table_info({t})")]
        for c in cols:
            snap[(t, c)] = con.execute(f"SELECT group_concat({c}) FROM (SELECT {c} FROM {t} ORDER BY 1)").fetchone()[0]  # nosec B608
    return snap


def parse_lineage():
    """Linaje de columnas a partir del texto SQL: columna de salida -> columnas de origen."""
    edges = defaultdict(set)
    control, ctrl_edges = {}, defaultdict(set)
    for target, sql in PIPE:
        m = re.search(r"SELECT (.*?) FROM (\w+) (\w+)(?: JOIN (\w+) (\w+) ON .*?)?(?: WHERE| GROUP BY| ORDER BY|$)", sql)
        select, t1, a1, t2, a2 = m.groups()
        aliases = {a1: t1}
        if t2:
            aliases[a2] = t2
        for item in re.split(r",\s*(?![^()]*\))", select):
            expr, out = re.split(r"\s+AS\s+", item)
            for al, col in re.findall(r"(?<![\w.])([A-Za-z_]\w*)\.([A-Za-z_]\w*)", expr):
                edges[(target, out.strip())].add((aliases[al], col))
        rest = sql.split(" FROM ", 1)[1]
        outs = [re.split(r"\s+AS\s+", i)[1].strip() for i in re.split(r",\s*(?![^()]*\))", select)]
        for al, col in re.findall(r"(?<![\w.])([A-Za-z_]\w*)\.([A-Za-z_]\w*)", rest):
            if al in aliases:
                control[(target, col, aliases[al])] = outs
        for o in outs:
            for (tg, col, tb), os_ in control.items():
                if tg == target and o in os_:
                    ctrl_edges[(target, o)].add((tb, col))
    return edges, ctrl_edges


def e547():
    print("SE-367 — linaje, catálogo y metadatos")
    con = mem_db()
    build_raw(con)
    base = snapshot(con)
    edges, ctrl = parse_lineage()
    both = defaultdict(set)
    for k in set(edges) | set(ctrl):
        both[k] = edges[k] | ctrl[k]
    outs = sorted(base)
    srcs = [("raw_orders", c) for c in ("order_id", "customer_id", "amount", "status", "day", "note")] + [("raw_customers", c) for c in ("customer_id", "city", "segment")]
    def parsed_impact(src, graph):
        hit, frontier = set(), {src}
        while frontier:
            nxt = {o for o, ins in graph.items() if ins & frontier and o not in hit}
            hit |= nxt
            frontier = nxt
        return hit
    rows = [["Columna de origen", "Salidas que cambian (medido)", "Linaje de datos solo", "Datos y condiciones", "Linaje de tablas"]]
    agree = miss_data = miss_both = 0
    table_deps = {"stg_orders": {"raw_orders"}, "stg_customers": {"raw_customers"}, "fact_sales": {"stg_orders", "stg_customers"}, "mart_city": {"fact_sales"}, "mart_daily": {"fact_sales"}, "report_top": {"mart_city"}}
    def table_impact(t):
        hit, frontier = set(), {t}
        while frontier:
            nxt = {x for x, d in table_deps.items() if d & frontier and x not in hit}
            hit |= nxt
            frontier = nxt
        return hit
    for s in srcs:
        con2 = mem_db()
        build_raw(con2, perturb=s)
        pert = snapshot(con2)
        changed = {k for k in outs if pert[k] != base[k]}
        pred = parsed_impact(s, edges)
        pred2 = parsed_impact(s, both)
        tbl = table_impact(s[0])
        tbl_cols = sum(1 for k in outs if k[0] in tbl)
        rows.append([f"{s[0]}.{s[1]}", len(changed), len(pred), len(pred2), f"{len(tbl)} tablas, {tbl_cols} columnas"])
        agree += changed <= pred2
        miss_data += len(changed - pred)
        miss_both += len(changed - pred2)
    table(rows)
    print(f"  salidas que cambian en la medición y que el linaje de datos solo omite: {miss_data}; con condiciones: {miss_both}; en {agree} de {len(srcs)} columnas de origen el linaje con condiciones cubre todo lo medido")
    print(f"  salidas totales: {len(outs)}")
    # un SELECT * esconde el linaje
    hidden = "CREATE TABLE copia AS SELECT * FROM fact_sales f"
    print(f"  ejemplo con comodín: «{hidden}» no nombra columnas, de modo que el analizador de texto produce 0 aristas de columna; hay que expandir el comodín con el catálogo")
    # SQL dinámico
    print("  SQL armado por concatenación en código (por ejemplo f'SELECT {col} FROM {tabla}'): el analizador de texto no lo ve; solo la ejecución observada o los metadatos de la consulta lo recuperan")


# ====================================================================== SE-368
def make_rows(rng, n, sort_by_day=True):
    rows = []
    for i in range(n):
        day = (i * 365) // n if sort_by_day else rng.randrange(365)
        rows.append((i, day, rng.randrange(20000), rng.randrange(500), rng.randrange(1, 6), rng.randrange(500, 90000), rng.choice(["paid", "paid", "paid", "shipped", "new"]), rng.choice(["CL", "CL", "CL", "AR", "PE"])))
    return rows


COLS = ["order_id", "day", "customer", "product", "qty", "amount", "status", "country"]


def write_columnar(path, rows, group=10_000):
    """Archivo columnar mínimo: grupos de filas, un bloque comprimido por columna, mínimos y máximos del grupo."""
    meta, offset = [], 0
    with open(path, "wb") as fh:
        for g in range(0, len(rows), group):
            chunk = rows[g:g + group]
            entry = {"rows": len(chunk), "cols": {}}
            for ci, name in enumerate(COLS):
                vals = [r[ci] for r in chunk]
                if isinstance(vals[0], str):
                    dic = sorted(set(vals))
                    idx = {v: i for i, v in enumerate(dic)}
                    raw = bytes(idx[v] for v in vals)
                    extra = dic
                else:
                    raw = array.array("q", vals).tobytes()
                    extra = [min(vals), max(vals)]
                blob = zlib.compress(raw, 6)
                fh.write(blob)
                entry["cols"][name] = [offset, len(blob), extra]
                offset += len(blob)
            meta.append(entry)
    return meta


def read_columnar(path, meta, need, day_lo, day_hi):
    total, scanned_groups, bytes_read = 0, 0, 0
    with open(path, "rb") as fh:
        for entry in meta:
            lo, hi = entry["cols"]["day"][2]
            if hi < day_lo or lo > day_hi:
                continue
            scanned_groups += 1
            data = {}
            for name in need:
                off, ln, _ = entry["cols"][name]
                fh.seek(off)
                data[name] = array.array("q", zlib.decompress(fh.read(ln)))
                bytes_read += ln
            for d, a in zip(data["day"], data["amount"]):
                if day_lo <= d <= day_hi:
                    total += a
    return total, scanned_groups, bytes_read


def e548():
    print("SE-368 — almacén, lago y lakehouse; formatos columnares")
    rng = random.Random(SEED)
    n = 200_000
    rows = make_rows(rng, n)
    with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as tmp:
        csv_p, jl_p, bin_p, col_p = (os.path.join(tmp, x) for x in ("o.csv", "o.jsonl", "o.bin", "o.col"))
        with open(csv_p, "w") as fh:
            fh.write(",".join(COLS) + "\n")
            fh.writelines(",".join(map(str, r)) + "\n" for r in rows)
        with open(jl_p, "w") as fh:
            fh.writelines(json.dumps(dict(zip(COLS, r))) + "\n" for r in rows)
        with open(bin_p, "wb") as fh:
            for r in rows:
                fh.write(struct.pack("<6q", *r[:6]) + r[6].encode().ljust(8) + r[7].encode().ljust(2))
        meta = write_columnar(col_p, rows)
        sizes = {k: os.path.getsize(p) for k, p in (("CSV", csv_p), ("JSON por líneas", jl_p), ("Binario por filas", bin_p), ("Columnar con compresión", col_p))}
        for k, v in sizes.items():
            print(f"  {k}: {v/1e6:.2f} MB ({fmt(v/sizes['CSV']*100,0)} % del CSV)")
        lo, hi = 100, 109
        truth = sum(r[5] for r in rows if lo <= r[1] <= hi)
        def q_csv():
            t = 0
            with open(csv_p) as fh:
                next(fh)
                for line in fh:
                    p = line.split(",")
                    if lo <= int(p[1]) <= hi:
                        t += int(p[5])
            return t
        def q_jl():
            t = 0
            with open(jl_p) as fh:
                for line in fh:
                    r = json.loads(line)
                    if lo <= r["day"] <= hi:
                        t += r["amount"]
            return t
        def q_bin():
            t = 0
            with open(bin_p, "rb") as fh:
                size = 6 * 8 + 10
                while chunk := fh.read(size * 4096):
                    for i in range(0, len(chunk), size):
                        _, d, _, _, _, a = struct.unpack_from("<6q", chunk, i)
                        if lo <= d <= hi:
                            t += a
            return t
        res = [["Formato", "Suma de importes (días 100 a 109)", "Tiempo (ms)"]]
        for name, fn in (("CSV", q_csv), ("JSON por líneas", q_jl), ("Binario por filas", q_bin), ("Columnar (2 columnas, con estadísticas)", lambda: read_columnar(col_p, meta, ["day", "amount"], lo, hi)[0])):
            ms, v = timed(fn, 2)
            res.append([name, v, fmt(ms, 0)])
            assert v == truth
        table(res)
        total, groups, br = read_columnar(col_p, meta, ["day", "amount"], lo, hi)
        print(f"  columnar: se leen {groups} de {len(meta)} grupos y {br/1e3:.0f} kB de {sizes['Columnar con compresión']/1e3:.0f} kB ({fmt(br/sizes['Columnar con compresión']*100,1)} %)")
        # sin orden: las estadísticas no descartan grupos
        rows_u = make_rows(random.Random(SEED), n, sort_by_day=False)
        col_u = os.path.join(tmp, "u.col")
        meta_u = write_columnar(col_u, rows_u)
        _, groups_u, br_u = read_columnar(col_u, meta_u, ["day", "amount"], lo, hi)
        print(f"  mismos datos sin ordenar por día: se leen {groups_u} de {len(meta_u)} grupos y {br_u/1e3:.0f} kB; tamaño del archivo {os.path.getsize(col_u)/1e6:.2f} MB")
        # todas las columnas frente a dos
        _, _, br_all = read_columnar(col_p, meta, ["day", "amount", "customer", "product", "qty", "order_id"], 0, 364)
        _, _, br_two = read_columnar(col_p, meta, ["day", "amount"], 0, 364)
        print(f"  leer 6 columnas numéricas: {br_all/1e6:.2f} MB; leer 2: {br_two/1e6:.2f} MB")
        # codificación por diccionario de la columna de estado
        status = [r[6] for r in rows]
        plain = zlib.compress(("\n".join(status)).encode(), 6)
        dic = {v: i for i, v in enumerate(sorted(set(status)))}
        enc = zlib.compress(bytes(dic[v] for v in status), 6)
        print(f"  columna de estado ({len(status)} valores, {len(dic)} distintos): texto comprimido {len(plain)} bytes; diccionario con índices de un byte comprimido {len(enc)} bytes; sin comprimir el texto ocupa {sum(len(s)+1 for s in status)} bytes")
        # archivos pequeños
        small = os.path.join(tmp, "small")
        big = os.path.join(tmp, "big")
        os.mkdir(small)
        os.mkdir(big)
        chunk = n // 1000
        t = time.perf_counter()
        for i in range(1000):
            part = rows[i * chunk:(i + 1) * chunk]
            m = write_columnar(os.path.join(small, f"p{i}.col"), part, group=chunk)
            with open(os.path.join(small, f"p{i}.json"), "w") as fh:
                json.dump(m, fh)
        t_write_small = time.perf_counter() - t
        def read_small():
            tot = 0
            for i in range(1000):
                with open(os.path.join(small, f"p{i}.json")) as fh:
                    m = json.load(fh)
                tot += read_columnar(os.path.join(small, f"p{i}.col"), m, ["day", "amount"], lo, hi)[0]
            return tot
        ms_small, v = timed(read_small, 2)
        assert v == truth
        compact = write_columnar(os.path.join(big, "all.col"), rows, group=10_000)
        ms_big, v = timed(lambda: read_columnar(os.path.join(big, "all.col"), compact, ["day", "amount"], lo, hi)[0], 2)
        print(f"  la misma consulta sobre 1000 archivos pequeños (200 filas cada uno, un grupo): {fmt(ms_small,0)} ms; sobre un archivo compactado con grupos de 10 000 filas: {fmt(ms_big,0)} ms")
        # manifiesto de instantáneas
        mdir = os.path.join(tmp, "table")
        os.mkdir(mdir)
        def commit(files, version):
            tmpf = os.path.join(mdir, f"v{version}.json.tmp")
            with open(tmpf, "w") as fh:
                json.dump({"version": version, "files": files}, fh)
            os.replace(tmpf, os.path.join(mdir, f"v{version}.json"))
        files_v1 = [f"p{i}.col" for i in range(10)]
        commit(files_v1, 1)
        reader_snapshot = json.load(open(os.path.join(mdir, "v1.json")))
        commit(["compact-1.col"], 2)  # compactación: reemplaza 10 archivos por uno
        latest = max(int(f[1:-5]) for f in os.listdir(mdir) if f.endswith(".json"))
        cur = json.load(open(os.path.join(mdir, f"v{latest}.json")))
        print(f"  manifiesto: el lector que abrió la versión 1 sigue viendo {len(reader_snapshot['files'])} archivos tras la compactación; un lector nuevo ve la versión {cur['version']} con {len(cur['files'])} archivo; el reemplazo es un único renombrado atómico")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    which = sys.argv[1:] or ["545", "546", "547", "548"]
    for key in which:
        globals()[f"e{key}"]()
        print()
