"""SE-403: feature flags y entrega progresiva. Segmentación por huella (real, hashlib), consistencia, combinatoria y deuda de banderas (semilla fija)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import hashlib, random, itertools, statistics, math, collections
def bucket(flag, user, salt=""):
    h = hashlib.sha256(f"{salt}{flag}:{user}".encode()).digest()
    return int.from_bytes(h[:8], "big") % 10000          # 0..9999
USERS = [f"u{i:06d}" for i in range(100000)]
print("== uniformidad de la segmentación por huella (100 000 usuarios, 100 cubos de 1 %)")
cnt = collections.Counter(bucket("nueva-entrega", u) // 100 for u in USERS)
exp = len(USERS) / 100; chi = sum((c - exp) ** 2 / exp for c in cnt.values())
print(f"mínimo {min(cnt.values())}, máximo {max(cnt.values())}, esperado {exp:.0f}; chi-cuadrado {chi:.1f} con 99 g.l. (valor típico ≈ 99, p=0,05 en ≈ 123)")
print("== correlación entre dos banderas distintas con la misma regla sin sal vs con sal por bandera (usuarios expuestos al 10 % de cada una)")
for label, f in (("sin sal (misma huella)", lambda fl, u: bucket("x", u)), ("con la bandera como sal", lambda fl, u: bucket(fl, u))):
    a = {u for u in USERS if f("A", u) < 1000}; b = {u for u in USERS if f("B", u) < 1000}
    print(f"{label:28s} A={len(a)} B={len(b)} ambas={len(a & b)} (independientes ≈ {len(a)*len(b)/len(USERS):.0f})")
print("== consistencia al ampliar 1 % -> 5 % -> 25 % -> 100 %")
steps = (100, 500, 2500, 10000)
sets = [{u for u in USERS if bucket("nueva-entrega", u) < s} for s in steps]
print("tamaños:", [len(s) for s in sets], "| se pierde alguien al ampliar:", [len(sets[i] - sets[i+1]) for i in range(3)])
rng = random.Random(3)
flick = 0; n = 20000
for u in USERS[:n]:   # aleatoriedad por petición: 10 peticiones por usuario al 25 %
    seq = [rng.random() < 0.25 for _ in range(10)]
    if any(seq) and not all(seq): flick += 1
print(f"aleatoriedad por petición al 25 %: {flick/n*100:.1f} % de los usuarios ve la función en algunas peticiones y en otras no (con huella por usuario: 0 %)")
print("== combinatoria: n banderas booleanas, estados posibles y casos para cubrir todos los pares")
def pairwise(n):
    # cubrimiento por pares con generación voraz y semilla fija
    rng = random.Random(n); need = {(i, j, a, b) for i in range(n) for j in range(i+1, n) for a in (0, 1) for b in (0, 1)}
    tests = 0
    while need:
        best = None; bg = -1
        for _ in range(60):
            t = tuple(rng.randint(0, 1) for _ in range(n))
            g = sum(1 for (i, j, a, b) in need if t[i] == a and t[j] == b)
            if g > bg: bg, best = g, t
        need = {(i, j, a, b) for (i, j, a, b) in need if not (best[i] == a and best[j] == b)}; tests += 1
    return tests
for n in (4, 8, 12, 16, 20):
    print(f"n={n:2d}: 2^n = {2**n:8d} estados; pares: {pairwise(n):3d} casos (voraz)")
print("== deuda de banderas: 60 meses, 3 banderas nuevas al mes, política de retirada")
for name, p_remove, owner in (("sin política de retirada", 0.0, False), ("retirar tras el 100 % con p=0,10 mensual", 0.10, False), ("fecha de caducidad y dueño (p=0,35 mensual)", 0.35, True)):
    rng = random.Random(8); live = []; peak = 0; dead = 0
    for m in range(60):
        live += [{"age": 0, "full": False} for _ in range(3)]
        for f in live:
            f["age"] += 1
            if f["age"] >= 2: f["full"] = True
        keep = []
        for f in live:
            if f["full"] and rng.random() < p_remove: continue
            keep.append(f)
        live = keep; peak = max(peak, len(live))
    stale = sum(1 for f in live if f["full"])
    print(f"{name:46s} vivas tras 60 meses: {len(live):3d}, ya al 100 % (código muerto): {stale:3d}, estados 2^{len(live)}")
