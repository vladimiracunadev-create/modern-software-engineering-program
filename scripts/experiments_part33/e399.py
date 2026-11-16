"""SE-399: dependencias directas y transitivas. Parte real (entorno Python instalado) y parte sintética con semilla."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import random, re, collections, importlib.metadata as md, sys, statistics

def real_graph():
    g = {}
    for d in md.distributions():
        name = re.sub(r"[-_.]+", "-", d.metadata["Name"]).lower()
        deps = set()
        for r in (d.requires or []):
            if "extra ==" in r: continue
            m = re.match(r"[A-Za-z0-9_.\-]+", r)
            if m: deps.add(re.sub(r"[-_.]+", "-", m.group(0)).lower())
        g[name] = deps
    return g
def closure(g, roots):
    seen = set(); st = list(roots)
    while st:
        n = st.pop()
        if n in seen or n not in g: continue
        seen.add(n); st.extend(g[n])
    return seen
g = real_graph()
sizes = sorted(((len(closure(g, [n])) - 1, n) for n in g), reverse=True)
direct = {n: len(v & set(g)) for n, v in g.items()}
print(f"== entorno real: {len(g)} distribuciones instaladas (Python {sys.version.split()[0]}, {sys.platform})")
with_deps = [s for s, n in sizes if s > 0]
print("paquetes con al menos 1 dependencia instalada:", len(with_deps), "| mediana de transitivas entre ellos:", statistics.median(with_deps), "| máximo:", sizes[0])
ratio = [(closure(g, [n]).__len__() - 1) / direct[n] for n in g if direct[n] > 0]
print("razón transitivas/directas: mediana %.2f, máx %.2f" % (statistics.median(ratio), max(ratio)))
print("raíces (nadie las requiere):", len([n for n in g if not any(n in v for v in g.values())]))
# --- sintético: 400 paquetes, ataque preferencial, 15 dependencias directas del proyecto
def synth(seed, n=400, k=3):
    rng = random.Random(seed); deps = {0: set()}; indeg = collections.Counter()
    for i in range(1, n):
        ch = set()
        for _ in range(rng.randint(0, k)):
            pool = list(range(i)); w = [1 + indeg[j] for j in pool]
            ch.add(rng.choices(pool, w)[0])
        deps[i] = ch
        for c in ch: indeg[c] += 1
    return deps, indeg
print("== grafo sintético (preferencial, 400 paquetes, 30 semillas), proyecto con 15 dependencias directas")
rat = []; hit = []; exposures = []
for s in range(30):
    deps, indeg = synth(s)
    rng = random.Random(1000 + s)
    roots = rng.sample(range(100, 400), 15)
    cl = closure(deps, roots)
    rat.append(len(cl) / 15)
    vuln = rng.choice(sorted(cl - set(roots)))
    # ¿cuántos caminos llevan al paquete vulnerable?
    exposures.append(sum(1 for r in roots if vuln in closure(deps, [r])))
print("tamaño medio de la clausura:", round(statistics.mean(len(closure(synth(s)[0], random.Random(1000+s).sample(range(100,400),15))) for s in range(30)), 1), "paquetes; razón media %.1f x las directas" % statistics.mean(rat))
print("un paquete transitivo vulnerable es alcanzado por %.1f de las 15 directas (mediana %d)" % (statistics.mean(exposures), statistics.median(exposures)))
# --- deriva de resolución: rangos sin bloqueo frente a archivo de bloqueo
print("== resolución en el tiempo: 25 dependencias con rango ^; cada paquete publica una versión nueva con p diaria 0,03; 60 días; construye cada día")
for locked in (False, True):
    rng = random.Random(77); ver = [0]*25; distinct = set(); changes = 0; prev = None
    cur = list(ver)
    for day in range(60):
        for i in range(25):
            if rng.random() < 0.03: ver[i] += 1
        if not locked: cur = list(ver)
        elif day == 0: cur = list(ver)
        t = tuple(cur); distinct.add(t)
        if prev is not None and t != prev: changes += 1
        prev = t
    print(f"{'con bloqueo' if locked else 'sin bloqueo':12s} conjuntos distintos resueltos en 60 días: {len(distinct):2d}; días en que cambió el conjunto: {changes}")
# --- vendorizar: latencia de parche y superficie
print("== parche de una vulnerabilidad: días hasta aplicar (modelo)")
rng = random.Random(3)
for name, base, extra in (("dependencia gestionada con bloqueo", 2, 1), ("copia vendorizada sin dueño", 2, 20), ("copia vendorizada con dueño y revisión periódica", 2, 7)):
    xs = sorted(base + rng.expovariate(1/extra) for _ in range(5000))
    print(f"{name:50s} mediana {xs[2500]:5.1f} d, p95 {xs[4750]:5.1f} d")
