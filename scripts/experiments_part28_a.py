"""Experimentos de las clases SE-337 a SE-342 (Parte 28): estilos arquitectónicos.

Uso: python scripts/experiments_part28_a.py [529|530|531|532|533|534]

No se invoca ningún modelo de lenguaje. Todo es código ejecutado con la biblioteca estándar sobre el
caso conductor *Avisos* (el servicio de recordatorios de entregas). Las tablas de valoraciones y los
parámetros de los modelos los fija el autor; las mediciones de red, memoria, tiempo y SQLite se hacen
de verdad en la máquina que ejecuta el script y los tiempos varían de un equipo a otro.
"""
from __future__ import annotations

import difflib
import hashlib
import hmac
import heapq
import importlib.util
import inspect
import itertools
import json
import math
import queue
import random
import re
import sqlite3
import subprocess
import sys
import tempfile
import textwrap
import threading
import time
import tracemalloc
from pathlib import Path

import experiments_part28_lab as L
from experiments_part28_lab import fmt, pct, table


# ====================================================================== SE-337
STYLES = ["Monolito en capas", "Monolito modular", "Microkernel", "Pipes and filters", "Microservicios", "Arquitectura celular"]
ATTRS = ["Despliegue independiente", "Cambio localizado", "Latencia interna", "Simplicidad operativa",
         "Aislamiento de fallos", "Extensión por terceros", "Costo a pequeña escala"]
RATINGS = {  # valoraciones 1-5 del autor, no mediciones
    "Monolito en capas": [1, 2, 5, 5, 1, 1, 5],
    "Monolito modular": [2, 4, 5, 4, 1, 2, 5],
    "Microkernel": [2, 3, 5, 3, 2, 5, 4],
    "Pipes and filters": [3, 3, 2, 3, 3, 3, 3],
    "Microservicios": [5, 4, 2, 1, 4, 3, 1],
    "Arquitectura celular": [4, 3, 3, 1, 5, 2, 1],
}
PROFILES = {  # pesos del autor por contexto
    "Equipo de 6, producto nuevo": [0.05, 0.25, 0.15, 0.25, 0.05, 0.05, 0.20],
    "12 equipos, 120 personas": [0.30, 0.20, 0.10, 0.10, 0.15, 0.05, 0.10],
    "Plataforma con extensiones de terceros": [0.10, 0.20, 0.10, 0.10, 0.10, 0.35, 0.05],
    "Crítico y multi-inquilino": [0.15, 0.10, 0.10, 0.05, 0.40, 0.05, 0.15],
}


def score(weights, ratings=RATINGS):
    return {s: sum(w * r for w, r in zip(weights, ratings[s])) for s in STYLES}


def winner(weights, ratings=RATINGS):
    sc = score(weights, ratings)
    return max(STYLES, key=lambda s: (sc[s], -STYLES.index(s)))


def e529():
    print("SE-337 — estilos como respuestas a fuerzas de calidad")
    print("  suma de pesos por perfil:", [round(sum(w), 2) for w in PROFILES.values()])
    rows = [["Perfil", "Ganador", "Puntaje", "Segundo", "Diferencia"]]
    for name, w in PROFILES.items():
        sc = score(w)
        order = sorted(STYLES, key=lambda s: -sc[s])
        rows.append([name, order[0], fmt(sc[order[0]]), order[1], fmt(sc[order[0]] - sc[order[1]])])
    table(rows)
    rng = random.Random(44)
    wins = {s: 0 for s in STYLES}
    n = 10000
    for _ in range(n):
        g = [rng.gammavariate(1, 1) for _ in ATTRS]
        t = sum(g)
        wins[winner([x / t for x in g])] += 1
    print(f"  pesos al azar (Dirichlet uniforme, {n} sorteos, semilla 44): victorias por estilo")
    for s in STYLES:
        print(f"    {s}: {wins[s]} ({fmt(100 * wins[s] / n, 1)} %)")
    print("  estabilidad de cada perfil si se perturban las valoraciones (cada celda cambia ±1 con prob. 0,2; 2000 repeticiones):")
    for name, w in PROFILES.items():
        base = winner(w)
        same = 0
        for _ in range(2000):
            pert = {s: [min(5, max(1, r + (rng.choice([-1, 1]) if rng.random() < 0.2 else 0))) for r in RATINGS[s]] for s in STYLES}
            same += winner(w, pert) == base
        print(f"    {name}: gana {base} en {same} de 2000 ({fmt(100 * same / 2000, 1)} %)")
    # cuántos estilos ganan en al menos un perfil
    print("  estilos distintos que ganan en algún perfil:", len({winner(w) for w in PROFILES.values()}))


# ====================================================================== SE-338
PLUGIN_TEMPLATE = '''API = {api}
NAME = "{name}"

def handle(event):
    return "{name}:" + event["id"]
'''
FAULTY_RAISE = 'API = 1\nNAME = "rota"\n\ndef handle(event):\n    raise RuntimeError("fallo del complemento")\n'
FAULTY_SLOW = 'import time\nAPI = 1\nNAME = "lenta"\n\ndef handle(event):\n    time.sleep(1.0)\n    return "lenta:" + event["id"]\n'


class Kernel:
    """Núcleo mínimo: conoce un contrato (API_VERSION) y descubre complementos en un directorio."""

    API_VERSION = 1

    def __init__(self, check_version=True, accept=(1,)):
        self.plugins = {}
        self.rejected = []
        self.check_version = check_version
        self.accept = accept

    def load_dir(self, path):
        for f in sorted(Path(path).glob("*.py")):
            spec = importlib.util.spec_from_file_location(f"plugin_{f.stem}", f)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if self.check_version and getattr(mod, "API", None) not in self.accept:
                self.rejected.append((f.stem, getattr(mod, "API", None)))
                continue
            self.plugins[mod.NAME] = mod

    def dispatch(self, event, isolate=True):
        out, errors = [], []
        for name, mod in self.plugins.items():
            if not isolate:
                out.append(mod.handle(event))
                continue
            try:
                out.append(mod.handle(event))
            except Exception as exc:  # aislamiento de fallos dentro del proceso
                errors.append((name, type(exc).__name__))
        return out, errors


def monolith_source(channels):
    body = ["def send(channel, event):"]
    for i, c in enumerate(channels):
        body.append(f"    {'if' if i == 0 else 'elif'} channel == \"{c}\":")
        body.append(f"        return \"{c}:\" + event[\"id\"]")
    body.append("    raise ValueError(channel)")
    return "\n".join(body) + "\n"


def e530():
    print("SE-338 — microkernel y arquitecturas de plugins")
    kernel_src = inspect.getsource(Kernel)
    h0 = hashlib.sha256(kernel_src.encode()).hexdigest()[:12]
    base = ["email", "sms", "push"]
    nuevos = ["digest", "webhook", "calendario"]
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        for c in base:
            (d / f"{c}.py").write_text(PLUGIN_TEMPLATE.format(api=1, name=c), encoding="utf8")
        k = Kernel()
        k.load_dir(d)
        print("  complementos iniciales:", list(k.plugins))
        for c in nuevos:
            (d / f"{c}.py").write_text(PLUGIN_TEMPLATE.format(api=1, name=c), encoding="utf8")
        k2 = Kernel()
        k2.load_dir(d)
        h1 = hashlib.sha256(inspect.getsource(Kernel).encode()).hexdigest()[:12]
        print("  complementos tras añadir 3:", list(k2.plugins), "| huella del núcleo igual:", h0 == h1)
        before, after = monolith_source(base), monolith_source(base + nuevos)
        diff = [l for l in difflib.unified_diff(before.splitlines(), after.splitlines(), lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        print(f"  monolito if/elif: {len(before.splitlines())} líneas con 3 canales, {len(after.splitlines())} con 6; líneas tocadas del núcleo al añadir 3: {len(diff)} (añadidas {sum(l[0]=='+' for l in diff)}, quitadas {sum(l[0]=='-' for l in diff)})")
        print("  núcleo con complementos: líneas tocadas al añadir 3: 0 (las 3 altas son archivos nuevos)")

        # aislamiento de fallos
        (d / "rota.py").write_text(FAULTY_RAISE, encoding="utf8")
        (d / "lenta.py").write_text(FAULTY_SLOW, encoding="utf8")
        kf = Kernel()
        kf.load_dir(d)
        event = {"id": "e1"}
        out, errors = kf.dispatch(event)
        print(f"  con try/except: resultados {len(out)} de {len(kf.plugins)} complementos, errores {errors}")
        try:
            kf.dispatch(event, isolate=False)
        except RuntimeError as exc:
            print(f"  sin aislamiento: la excepción de un complemento detiene la entrega a los demás ({exc})")
        t = time.perf_counter()
        kf.plugins["lenta"].handle(event)
        print(f"  un complemento lento bloquea el proceso: {fmt(time.perf_counter() - t, 2)} s en el mismo hilo")

        # aislamiento por proceso
        runner = "import importlib.util,sys;p=sys.argv[1];s=importlib.util.spec_from_file_location('p',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);print(m.handle({'id':'e1'}))"

        def via_process(name, timeout):
            t0 = time.perf_counter()
            try:
                r = subprocess.run([sys.executable, "-c", runner, str(d / f"{name}.py")], capture_output=True, text=True, timeout=timeout)
                status = "ok" if r.returncode == 0 else "error"
            except subprocess.TimeoutExpired:
                status = "cortado por tiempo"
            return status, (time.perf_counter() - t0) * 1000

        print("  por proceso con límite de 0,3 s:")
        for name in ["email", "rota", "lenta"]:
            st, ms = via_process(name, 0.3)
            print(f"    {name}: {st} en {fmt(ms, 0)} ms")
        samples = [via_process("email", 5)[1] for _ in range(10)]
        inproc = L.time_calls(lambda: k.plugins["email"].handle(event), 10000)
        print(f"  costo por llamada: proceso nuevo mediana {fmt(L.median(samples), 1)} ms; en proceso mediana {fmt(L.median(inproc) * 1000, 2)} µs")

        # versión del contrato
        for name in ["email", "sms", "push", "digest", "webhook", "calendario"]:
            (d / f"{name}.py").write_text(PLUGIN_TEMPLATE.format(api=1, name=name), encoding="utf8")
        (d / "calendario.py").write_text(PLUGIN_TEMPLATE.format(api=2, name="calendario"), encoding="utf8")
        (d / "rota.py").unlink()
        (d / "lenta.py").unlink()

        def run_v2(kernel):
            ok = bad = 0
            for mod in kernel.plugins.values():
                res = mod.handle(event)
                try:
                    res["status"]  # el contrato 2 espera un diccionario
                    ok += 1
                except TypeError:
                    bad += 1
            return ok, bad

        sin = Kernel(check_version=False)
        sin.load_dir(d)
        print("  núcleo v2 sin comprobar versión: (correctos, rotos en ejecución) =", run_v2(sin))
        con = Kernel(check_version=True, accept=(2,))
        con.load_dir(d)
        print("  núcleo v2 que exige API 2: cargados", list(con.plugins), "| rechazados al arrancar", con.rejected)
        both = Kernel(check_version=True, accept=(1, 2))
        both.load_dir(d)
        print("  núcleo v2 con adaptador para API 1: cargados", len(both.plugins), "rechazados", len(both.rejected))


# ====================================================================== SE-339
def gen_rows(n, seed=44):
    rng = random.Random(seed)
    for i in range(n):
        yield {"id": i, "student": f"s{rng.randrange(500)}", "course": f"c{rng.randrange(40)}",
               "due": rng.randrange(0, 400), "ok": rng.random() > 0.1, "note": "x" * 40}


CALLS = {"enrich": 0}


def f_validate(rows):
    for r in rows:
        if r["ok"]:
            yield r


def f_due(rows):
    for r in rows:
        if r["due"] <= 72:
            yield r


def f_enrich(rows):
    for r in rows:
        CALLS["enrich"] += 1
        yield {**r, "label": f"{r['course']}:{r['student']}"}


def f_format(rows):
    for r in rows:
        yield f"{r['label']}@{r['due']}"


def run_batch(n):
    data = list(gen_rows(n))
    a = [r for r in data if r["ok"]]
    b = [r for r in a if r["due"] <= 72]
    c = [{**r, "label": f"{r['course']}:{r['student']}"} for r in b]
    return len([f"{r['label']}@{r['due']}" for r in c])


def run_stream(n):
    return sum(1 for _ in f_format(f_enrich(f_due(f_validate(gen_rows(n))))))


def peak(fn, n):
    tracemalloc.start()
    res = fn(n)
    cur, pk = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return res, pk


def e531():
    print("SE-339 — pipes and filters y arquitecturas de flujo")
    n = 100_000
    r1, p1 = peak(run_batch, n)
    r2, p2 = peak(run_stream, n)
    print(f"  {n} registros: salida por lotes {r1}, en flujo {r2} (iguales: {r1 == r2})")
    print(f"  pico de memoria (tracemalloc): por lotes {fmt(p1 / 1e6, 1)} MB, en flujo {fmt(p2 / 1e6, 3)} MB, razón {fmt(p1 / p2, 0)}×")

    def run_sorted(n):
        return len(sorted(f_format(f_enrich(f_due(f_validate(gen_rows(n))))), key=len))

    r3, p3 = peak(run_sorted, n)
    print(f"  con un filtro que necesita todo (ordenar): pico {fmt(p3 / 1e6, 1)} MB (el flujo deja de ser acotado)")
    # orden de filtros: el selectivo primero reduce el trabajo del caro
    CALLS["enrich"] = 0
    sum(1 for _ in f_due(f_enrich(f_validate(gen_rows(n)))))
    caro_antes = CALLS["enrich"]
    CALLS["enrich"] = 0
    sum(1 for _ in f_enrich(f_due(f_validate(gen_rows(n)))))
    caro_despues = CALLS["enrich"]
    print(f"  llamadas al filtro caro (enriquecer): filtro selectivo después {caro_antes}, antes {caro_despues} ({fmt(100 * (1 - caro_despues / caro_antes), 1)} % menos)")
    # contrapresión con cola acotada
    for bound in (0, 100):
        q = queue.Queue(maxsize=bound)
        maxdepth = [0]
        done = threading.Event()

        def producer():
            for i in range(5000):
                q.put(i)
                maxdepth[0] = max(maxdepth[0], q.qsize())
            q.put(None)

        def consumer():
            while True:
                v = q.get()
                if v is None:
                    done.set()
                    return
                time.sleep(0.00005)

        tp = threading.Thread(target=producer)
        tc = threading.Thread(target=consumer)
        tc.start()
        tp.start()
        tp.join()
        done.wait()
        tc.join()
        print(f"  cola {'ilimitada' if bound == 0 else f'acotada a {bound}'}: profundidad máxima observada {maxdepth[0]} (productor rápido, consumidor lento, 5000 mensajes)")
    # un filtro defectuoso en medio
    def f_buggy(rows):
        for r in rows:
            if r["id"] == 5:
                raise ValueError("registro malformado")
            yield r

    try:
        sum(1 for _ in f_format(f_enrich(f_buggy(gen_rows(20)))))
    except ValueError:
        print("  una excepción en un filtro sin manejo detiene todo el flujo en el registro 5; con una cola de rechazos el flujo sigue:")
    rejects, ok = [], 0
    for r in gen_rows(20):
        try:
            if r["id"] == 5:
                raise ValueError("registro malformado")
            ok += 1
        except ValueError:
            rejects.append(r["id"])
    print(f"    procesados {ok}, rechazados {rejects}")


# ====================================================================== SE-340
def e532():
    print("SE-340 — microservicios y sus costes reales")
    server = L.start_server()
    port = server.server_address[1]
    n = 400
    payload = dict(L.PAYLOAD)

    def inproc():
        return payload["due"] <= 72

    def serial():
        return json.loads(json.dumps(payload))["due"] <= 72

    keep, conn = L.keepalive_caller(port)
    fresh = L.fresh_caller(port)
    rows = [["Camino", "Mediana (ms)", "p99 (ms)"]]
    for label, fn, reps in [("Llamada en el mismo proceso", inproc, 20000), ("Serializar y deserializar JSON", serial, 20000),
                            ("HTTP local con conexión reutilizada", keep, n), ("HTTP local con conexión nueva", fresh, n)]:
        keep() if fn is keep else None
        ts = L.time_calls(fn, reps)
        rows.append([label, f"{fmt(L.median(ts), 4)}", f"{fmt(pct(ts, 0.99), 4)}"])
    table(rows)
    conn.close()
    server.shutdown()

    rng = random.Random(44)

    def hop():
        return rng.lognormvariate(math.log(20), 0.6)

    print("  cadena sincrónica de k servicios (latencia mediana 20 ms por salto, 99,9 % de disponibilidad por servicio, 20 000 peticiones, semilla 44):")
    rows = [["k", "Disponibilidad analítica", "Disponibilidad simulada", "p50 (ms)", "p99 (ms)"]]
    for k in (1, 2, 4, 8):
        ok = 0
        lat = []
        for _ in range(20000):
            t, fail = 0.0, False
            for _ in range(k):
                t += hop()
                if rng.random() > 0.999:
                    fail = True
                    break
            ok += not fail
            lat.append(t)
        rows.append([k, f"{fmt(100 * 0.999 ** k, 3)} %", f"{fmt(100 * ok / 20000, 3)} %", fmt(pct(lat, 0.5), 1), fmt(pct(lat, 0.99), 1)])
    table(rows)
    print("  paralelo: latencia de la petición = máximo de k llamadas (50 000 peticiones):")
    for k in (1, 4, 8, 16):
        vals = [max(hop() for _ in range(k)) for _ in range(50000)]
        print(f"    k={k}: p50 {fmt(pct(vals, 0.5), 1)} ms, p99 {fmt(pct(vals, 0.99), 1)} ms; probabilidad de que alguna llamada supere su propio p99: {fmt(100 * (1 - 0.99 ** k), 1)} %")

    def dependents(graph, node):
        callers = {n for n, deps in graph.items() if node in deps}
        seen = set()
        todo = list(callers)
        while todo:
            c = todo.pop()
            if c in seen:
                continue
            seen.add(c)
            todo += [n for n, deps in graph.items() if c in deps]
        return seen

    chain = {f"s{i}": [f"s{i + 1}"] for i in range(7)}
    chain["s7"] = []
    star = {f"s{i}": ["s7"] for i in range(7)}
    star["s7"] = []
    print("  cambio incompatible de contrato en el servicio s7 (8 servicios): servicios que deben cambiar o desplegarse a la vez")
    print(f"    cadena: transitivos {len(dependents(chain, 's7'))}, directos {len([n for n, d in chain.items() if 's7' in d])}")
    print(f"    estrella: transitivos {len(dependents(star, 's7'))}, directos {len([n for n, d in star.items() if 's7' in d])}")
    print("    con un cambio compatible (campo opcional añadido) y consumidores tolerantes: 0 despliegues coordinados")


# ====================================================================== SE-341
def backend_data():
    rng = random.Random(44)
    profile = {f"campo{i}": "v" * rng.randrange(6, 20) for i in range(20)}
    profile.update({"name": "Ana Soto", "unread": 3})
    courses = [{**{f"campo{j}": "x" * rng.randrange(5, 15) for j in range(10)}, "id": f"c{i}", "title": f"Curso {i}"} for i in range(6)]
    deliveries = [{**{f"campo{j}": "y" * rng.randrange(5, 20) for j in range(8)}, "id": f"e{i}", "course": f"c{i % 6}", "title": f"Entrega {i}", "due": 10 + 7 * i} for i in range(10)]
    notifications = [{**{f"campo{j}": "z" * rng.randrange(5, 15) for j in range(6)}, "id": f"n{i}", "read": i % 3 == 0} for i in range(15)]
    return profile, courses, deliveries, notifications


def e533():
    print("SE-341 — BFF, API gateway y service mesh")
    profile, courses, deliveries, notifications = backend_data()
    size = lambda o: len(json.dumps(o, separators=(",", ":")).encode())
    full = {"profile": profile, "courses": courses, "deliveries": deliveries, "notifications": notifications}
    mobile = {"name": profile["name"], "unread": sum(1 for n in notifications if not n["read"]),
              "next": [{"id": d["id"], "title": d["title"], "due": d["due"]} for d in sorted(deliveries, key=lambda d: d["due"])[:3]]}
    web = {"name": profile["name"], "courses": [{"id": c["id"], "title": c["title"]} for c in courses],
           "deliveries": [{k: d[k] for k in ("id", "course", "title", "due")} for d in deliveries],
           "notifications": [{"id": n["id"], "read": n["read"]} for n in notifications]}
    sizes = {k: size(v) for k, v in full.items()}
    print("  tamaños por servicio (bytes):", sizes, "total", sum(sizes.values()))
    print(f"  la pantalla móvil necesita {size(mobile)} bytes ({fmt(100 * size(mobile) / sum(sizes.values()), 1)} % del total); la web necesita {size(web)} bytes ({fmt(100 * size(web) / sum(sizes.values()), 1)} %)")
    rtt, bw = 0.080, 0.5e6  # supuestos del autor: 80 ms de ida y vuelta, 0,5 MB/s
    modelos = [("Cliente llama a cuatro servicios (2 rondas)", 2, sum(sizes.values())),
               ("Gateway de agregación (1 ronda, carga completa)", 1, sum(sizes.values())),
               ("BFF móvil (1 ronda, carga proyectada)", 1, size(mobile)),
               ("BFF web (1 ronda, carga proyectada)", 1, size(web))]
    rows = [["Camino", "Rondas", "Bytes", "Tiempo modelado (ms)"]]
    for label, rounds, b in modelos:
        rows.append([label, rounds, b, fmt((rounds * rtt + b / bw) * 1000, 0)])
    table(rows)
    print("  supuestos del modelo: ida y vuelta de 80 ms, ancho de banda de 0,5 MB/s; no es una medición de red real")

    # autenticación solo en el borde frente a validación en cada servicio
    key = bytes(range(16))
    sign = lambda student: hmac.new(key, student.encode(), "sha256").hexdigest()
    token = {"student": "s1", "sig": sign("s1")}

    def service_trusting(req):  # confía en que el gateway ya autenticó
        return True

    def service_validating(req):
        sig = req.get("sig", "")
        return hmac.compare_digest(sig, sign(req.get("student", "")))

    forged = {"student": "s1", "sig": "0" * 64}
    valid = token
    svcs = ["perfil", "cursos", "entregas", "notificaciones"]
    print("  petición interna falsificada que salta el gateway:")
    print(f"    servicios que la aceptan si solo confían en el borde: {sum(service_trusting(forged) for _ in svcs)} de {len(svcs)}")
    print(f"    servicios que la aceptan si cada uno valida la firma: {sum(service_validating(forged) for _ in svcs)} de {len(svcs)}; petición válida aceptada: {sum(service_validating(valid) for _ in svcs)} de {len(svcs)}")

    # saltos de proxy (sidecar)
    server = L.start_server()
    p1 = L.start_proxy(server.server_address[1])
    p2 = L.start_proxy(p1.getsockname()[1])
    ports = [("Directo", server.server_address[1]), ("Un salto (un proxy)", p1.getsockname()[1]), ("Dos saltos (dos proxies)", p2.getsockname()[1])]
    callers = {label: L.keepalive_caller(port) for label, port in ports}
    for call, _ in callers.values():
        for _ in range(50):
            call()
    meds = {label: [] for label, _ in ports}
    allts = {label: [] for label, _ in ports}
    for _ in range(8):  # rondas intercaladas para que el ruido del sistema afecte por igual a los tres caminos
        for label, (call, _) in callers.items():
            ts = L.time_calls(call, 500)
            meds[label].append(L.median(ts))
            allts[label] += ts
    base = L.median(meds["Directo"])
    rows = [["Camino", "Mediana de medianas (ms)", "p99 (ms)", "Sobre el directo (ms)"]]
    for label, _ in ports:
        m = L.median(meds[label])
        rows.append([label, fmt(m, 3), fmt(pct(allts[label], 0.99), 3), fmt(m - base, 3)])
        callers[label][1].close()
    table(rows)
    p1.close()
    p2.close()
    server.shutdown()


# ====================================================================== SE-342
SCHEMA = """
create table deliveries_all(id integer primary key, tenant_id integer, student text, due integer, submitted integer);
create index ix_t on deliveries_all(tenant_id);
"""
QUERIES = [
    ("Q01 filtro simple", "select id from deliveries where tenant_id = ? and due <= 72"),
    ("Q02 filtro con alias", "select d.id from deliveries d where d.tenant_id = ? order by d.id"),
    ("Q03 filtro en mayúsculas", "SELECT id FROM deliveries WHERE TENANT_ID = ? AND submitted = 0"),
    ("Q04 conteo con filtro", "select count(*) from deliveries where tenant_id = ?"),
    ("Q05 suma con filtro", "select sum(due) from deliveries where tenant_id = ?"),
    ("Q06 agrupado con filtro", "select student, count(*) from deliveries where tenant_id = ? group by student order by student"),
    ("Q07 subconsulta con filtro", "select id from deliveries where tenant_id = ? and due in (select due from deliveries where tenant_id = ? and due < 30)"),
    ("Q08 ordenado con filtro", "select id from deliveries where tenant_id = ? order by due, id limit 10"),
    ("Q09 sin filtro", "select id from deliveries where due <= 72"),
    ("Q10 sin filtro, conteo", "select count(*) from deliveries where submitted = 0"),
    ("Q11 filtro falso (tautología)", "select id from deliveries where 'tenant_id' = 'tenant_id' and due <= 72"),
    ("Q12 filtro anulado por OR", "select id from deliveries where tenant_id = ? or due <= 5"),
]
LEAKS_EXPECTED = {"Q09", "Q10", "Q11", "Q12"}


def populate(conn, tenants=5, rows=200, seed=44):
    rng = random.Random(seed)
    data = [(t * 1000 + i, t, f"s{rng.randrange(30)}", rng.randrange(0, 400), rng.randrange(2)) for t in range(1, tenants + 1) for i in range(rows)]
    conn.executemany("insert into deliveries_all values (?,?,?,?,?)", data)
    return data


def run_query(conn, sql, tenant):
    n = sql.count("?")
    return conn.execute(sql, (tenant,) * n).fetchall()


def make_conn(data_conn_file=None):
    c = sqlite3.connect(":memory:")
    c.executescript(SCHEMA)
    populate(c)
    return c


def scoped_view(conn, tenant):
    conn.execute("drop view if exists temp.deliveries")
    # DDL no admite parámetros: el identificador se convierte a entero antes de interpolarse
    conn.execute(f"create temp view deliveries as select * from main.deliveries_all where tenant_id = {int(tenant)}")  # nosec B608


def noisy_neighbor(policy, seed=44):
    rng = random.Random(seed)
    workers, horizon = 4, 60.0
    arrivals = []
    for t in range(9):  # nueve inquilinos normales a 2 solicitudes por segundo
        x = 0.0
        while True:
            x += rng.expovariate(2.0)
            if x > horizon:
                break
            arrivals.append((x, f"n{t}", rng.expovariate(1 / 0.1)))
    x = 20.0  # el inquilino ruidoso envía 40 por segundo entre los segundos 20 y 40
    while x < 40.0:
        x += rng.expovariate(40.0)
        arrivals.append((x, "ruidoso", rng.expovariate(1 / 0.1)))
    arrivals.sort()
    cap = {"ninguna": 99, "tope de 1 de 4": 1}[policy]
    events = [(a, 0, i) for i, (a, _, _) in enumerate(arrivals)]
    heapq.heapify(events)
    free, running, waiting, waits = workers, {}, [], {}
    now = 0.0
    while events:
        now, kind, i = heapq.heappop(events)
        if kind == 0:
            waiting.append(i)
        else:
            free += 1
            running[arrivals[i][1]] -= 1
        for j in list(waiting):
            if free == 0:
                break
            tenant = arrivals[j][1]
            if running.get(tenant, 0) < cap:
                waiting.remove(j)
                running[tenant] = running.get(tenant, 0) + 1
                free -= 1
                waits[j] = now - arrivals[j][0]
                heapq.heappush(events, (now + arrivals[j][2], 1, j))
    normal = [w for j, w in waits.items() if arrivals[j][1] != "ruidoso"]
    ruidoso = [w for j, w in waits.items() if arrivals[j][1] == "ruidoso"]
    return pct(normal, 0.95), pct(ruidoso, 0.95), len(normal), len(ruidoso)


def e534():
    print("SE-342 — multi-tenancy y aislamiento")
    conn = make_conn()
    total = conn.execute("select count(*) from deliveries_all").fetchone()[0]
    print(f"  tabla compartida: {total} filas de 5 inquilinos (200 cada uno)")
    # referencia: una base que solo contiene al inquilino 1 (no puede haber fugas)
    solo = sqlite3.connect(":memory:")
    solo.executescript(SCHEMA)
    rows1 = conn.execute("select * from deliveries_all where tenant_id = 1").fetchall()
    solo.executemany("insert into deliveries_all values (?,?,?,?,?)", rows1)
    scoped_view(solo, 1)
    ref = {name.split()[0]: run_query(solo, sql, 1) for name, sql in QUERIES}
    # sin protección: las consultas ven la tabla compartida tal cual
    conn.execute("create temp view deliveries as select * from main.deliveries_all")
    raw = {name.split()[0]: run_query(conn, sql, 1) for name, sql in QUERIES}
    leaks = [k for k in raw if raw[k] != ref[k]]
    print(f"  sin protección, consultas que devuelven más que lo del inquilino 1 (fugas): {len(leaks)} de {len(QUERIES)} -> {leaks}")
    lint = [name.split()[0] for name, sql in QUERIES if not re.search(r"tenant_id\s*=\s*\?", sql, re.I)]
    print(f"  linter por expresión regular («tenant_id = ?» presente): señala {len(lint)} -> {lint}; fugas que no ve: {sorted(set(leaks) - set(lint))}; falsas alarmas: {sorted(set(lint) - set(leaks))}")
    scoped_view(conn, 1)  # misma tabla compartida, pero la vista temporal del inquilino tapa el nombre
    protected = {name.split()[0]: run_query(conn, sql, 1) for name, sql in QUERIES}
    still = [k for k in protected if protected[k] != ref[k]]
    print(f"  con vista temporal del inquilino en la conexión de la solicitud: fugas {len(still)} de {len(QUERIES)}; filas visibles de Q09: {len(protected['Q09'])}")
    conn2 = conn
    # costo de la vista
    ts = L.time_calls(lambda: scoped_view(conn2, 1), 2000)
    base = L.time_calls(lambda: run_query(conn2, QUERIES[0][1], 1), 2000)
    print(f"  crear la vista temporal por solicitud: mediana {fmt(L.median(ts) * 1000, 1)} µs; la consulta Q01: mediana {fmt(L.median(base) * 1000, 1)} µs")

    # base de datos por inquilino
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        t = time.perf_counter()
        for i in range(200):
            c = sqlite3.connect(d / f"t{i}.db")
            c.executescript("create table deliveries(id integer primary key, student text, due integer, submitted integer); create index ix_d on deliveries(due);")
            c.executemany("insert into deliveries values (?,?,?,?)", [(j, f"s{j % 30}", j % 400, j % 2) for j in range(50)])
            c.commit()
            c.close()
        create_ms = (time.perf_counter() - t) * 1000
        size = sum(f.stat().st_size for f in d.glob("*.db"))
        t = time.perf_counter()
        for i in range(200):
            c = sqlite3.connect(d / f"t{i}.db")
            c.execute("alter table deliveries add column channel text default 'email'")
            c.commit()
            c.close()
        mig_ms = (time.perf_counter() - t) * 1000
    shared = sqlite3.connect(":memory:")
    shared.executescript(SCHEMA)
    populate(shared, tenants=200, rows=50)
    t = time.perf_counter()
    shared.execute("alter table deliveries_all add column channel text default 'email'")
    shared.commit()
    shared_ms = (time.perf_counter() - t) * 1000
    print(f"  200 inquilinos con una base cada uno: crear {fmt(create_ms, 0)} ms, {size} bytes en disco ({fmt(size / 200, 0)} por inquilino), migrar el esquema en las 200: {fmt(mig_ms, 0)} ms; una tabla compartida: {fmt(shared_ms, 2)} ms")

    print("  vecino ruidoso (4 trabajadores, 9 inquilinos normales a 2/s, uno ruidoso a 40/s entre los segundos 20 y 40, semilla 44):")
    rows = [["Política", "Espera p95 normales (s)", "Espera p95 ruidoso (s)", "Solicitudes normales", "Solicitudes ruidoso"]]
    for pol in ("ninguna", "tope de 1 de 4"):
        pn, pr, nn, nr = noisy_neighbor(pol)
        rows.append([pol, fmt(pn, 2), fmt(pr, 2), nn, nr])
    table(rows)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    which = sys.argv[1:] or ["529", "530", "531", "532", "533", "534"]
    for key in which:
        globals()[f"e{key}"]()
        print()
