"""SE-405: instaladores y actualizaciones. Inyección de fallos real sobre el sistema de archivos y simulación de sesgo de versiones (semilla)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import os, shutil, tempfile, hashlib, json, random, sys, collections
class Crash(Exception): pass
N = 6
def files(ver): return {f"mod{i}.py": (f"# v{ver} módulo {i}\n" * 50).encode() for i in range(N)}
def sha(b): return hashlib.sha256(b).hexdigest()
def manifest(ver): return json.dumps({"version": ver, "files": {k: sha(v) for k, v in files(ver).items()}}, sort_keys=True).encode()
class Stepper:
    def __init__(self, crash_at): self.n = 0; self.crash_at = crash_at
    def tick(self):
        self.n += 1
        if self.n == self.crash_at: raise Crash
def write(path, data, st, half=False):
    with open(path, "wb") as f:
        st.tick(); f.write(data[: len(data) // 2] if half else data)   # fallo en mitad de la escritura = fichero truncado
        if half: st.tick()
def fsync_replace(src, dst, st):
    st.tick(); os.replace(src, dst)
def A(root, st):                                   # sobrescribir en sitio
    for k, v in files(2).items(): write(os.path.join(root, "app", k), v, st)
    write(os.path.join(root, "app", "MANIFEST.json"), manifest(2), st)
def B(root, st):                                   # un fichero a la vez: escribe a .tmp y reemplaza
    for k, v in files(2).items():
        write(os.path.join(root, "app", k + ".tmp"), v, st); fsync_replace(os.path.join(root, "app", k + ".tmp"), os.path.join(root, "app", k), st)
    write(os.path.join(root, "app", "MANIFEST.json.tmp"), manifest(2), st); fsync_replace(os.path.join(root, "app", "MANIFEST.json.tmp"), os.path.join(root, "app", "MANIFEST.json"), st)
def C(root, st):                                   # directorio nuevo completo + puntero
    d = os.path.join(root, "v2"); os.makedirs(d, exist_ok=True)
    for k, v in files(2).items(): write(os.path.join(d, k), v, st)
    write(os.path.join(d, "MANIFEST.json"), manifest(2), st)
    write(os.path.join(root, "current.tmp"), b"v2", st); fsync_replace(os.path.join(root, "current.tmp"), os.path.join(root, "current"), st)
def D(root, st):                                   # como C, pero verifica antes y conserva v1
    d = os.path.join(root, "v2"); os.makedirs(d, exist_ok=True)
    for k, v in files(2).items(): write(os.path.join(d, k), v, st)
    write(os.path.join(d, "MANIFEST.json"), manifest(2), st)
    m = json.loads(open(os.path.join(d, "MANIFEST.json"), "rb").read())
    assert all(sha(open(os.path.join(d, k), "rb").read()) == h for k, h in m["files"].items())
    write(os.path.join(root, "current.tmp"), b"v2", st); fsync_replace(os.path.join(root, "current.tmp"), os.path.join(root, "current"), st)
def setup(root, kind):
    shutil.rmtree(root, ignore_errors=True); os.makedirs(root)
    base = os.path.join(root, "app" if kind in "AB" else "v1"); os.makedirs(base)
    for k, v in files(1).items(): open(os.path.join(base, k), "wb").write(v)
    open(os.path.join(base, "MANIFEST.json"), "wb").write(manifest(1))
    if kind in "CD": open(os.path.join(root, "current"), "wb").write(b"v1")
def state(root, kind):
    d = os.path.join(root, "app") if kind in "AB" else os.path.join(root, open(os.path.join(root, "current")).read().strip())
    try:
        m = json.loads(open(os.path.join(d, "MANIFEST.json"), "rb").read())
        ok = all(sha(open(os.path.join(d, k), "rb").read()) == h for k, h in m["files"].items())
        return f"v{m['version']} consistente" if ok else "MEZCLA/CORRUPTO (el manifiesto no coincide)"
    except Exception: return "NO ARRANCA (falta o ilegible)"
tmp = tempfile.mkdtemp(prefix="e405-")
print("python", sys.version.split()[0], sys.platform)
print("== inyección de fallo en CADA paso de la actualización v1 -> v2 (6 módulos + manifiesto); cada celda es un resultado final")
for kind, fn in zip("ABCD", (A, B, C, D)):
    st = Stepper(0)
    setup(os.path.join(tmp, "x"), kind)
    fn(os.path.join(tmp, "x"), st); total = st.n
    res = collections.Counter()
    for crash in range(1, total + 1):
        root = os.path.join(tmp, "r"); setup(root, kind); st = Stepper(crash)
        try: fn(root, st)
        except Crash: pass
        res[state(root, kind)] += 1
    print(f"estrategia {kind}: {total} puntos de fallo -> {dict(res)}")
print("== sin fallo: estado final")
for kind, fn in zip("ABCD", (A, B, C, D)):
    root = os.path.join(tmp, "r"); setup(root, kind); fn(root, Stepper(0)); print(f"estrategia {kind}: {state(root, kind)}")
print("== descarga corrupta (un byte cambiado en un módulo preparado) antes del reemplazo final")
def corrupt(fn_kind):
    root = os.path.join(tmp, "r"); setup(root, fn_kind)
    orig = write
    def bad_write(path, data, st, half=False):
        if path.endswith("mod3.py") and "v2" in path: data = data[:10] + b"X" + data[11:]
        orig(path, data, st, half)
    globals()["write"] = bad_write
    try:
        (C if fn_kind == "C" else D)(root, Stepper(0)); out = state(root, fn_kind)
    except AssertionError: out = "rechazada antes del reemplazo; sigue " + state(root, fn_kind)
    finally: globals()["write"] = orig
    return out
for k in "CD": print(f"estrategia {k}: {corrupt(k)}")
# --- sesgo de versiones: despliegue escalonado con clientes que consultan cada vez que se abren
print("== sesgo de versiones: 20 000 clientes, lanzamiento cada 14 días durante 180 días, apertura con distribución de colas largas")
rng = random.Random(405); clients = [{"v": 0, "gap": rng.choice([1, 1, 2, 3, 7, 14, 30, 60, 120])} for _ in range(20000)]
releases = list(range(14, 181, 14)); cur = 0; last = None
paths = collections.Counter(); behind = collections.Counter()
for day in range(1, 181):
    if day in releases: cur += 1
    for c in clients:
        if day % c["gap"] == 0 and c["v"] != cur:
            paths[(c["v"], cur)] += 1; c["v"] = cur
    if day in (30, 90, 180):
        dist = collections.Counter(cur - c["v"] for c in clients)
        print(f"día {day:3d}: versión actual {cur:2d}; atrasados 0:{dist[0]/200:5.1f} %  1:{dist[1]/200:5.1f} %  2-3:{(dist[2]+dist[3])/200:5.1f} %  4+:{sum(v for k,v in dist.items() if k>=4)/200:5.1f} %")
jumps = collections.Counter(b - a for (a, b), n in paths.items() for _ in range(n))
print("saltos de versión realizados (de a hasta b): ", dict(sorted(jumps.items())))
print("caminos de actualización distintos observados:", len(paths), "| con salto de 3 versiones o más:", sum(n for (a, b), n in paths.items() if b - a >= 3), "de", sum(paths.values()), "actualizaciones")
