"""SE-404: canary, blue-green y rollback (simulación con semilla, tiempo virtual). 400 peticiones/s, error base 0,5 %."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import random, math, statistics
RPS = 400; BASE = 0.005
def z_exceeds(e_c, n_c, e_b, n_b, z=3.0):
    # prueba de dos proporciones: ¿el canario es peor que la línea base con el z dado?
    if n_c < 30: return False
    p = (e_c + e_b) / (n_c + n_b); se = math.sqrt(max(p * (1 - p) * (1 / n_c + 1 / n_b), 1e-12))
    return (e_c / n_c - e_b / n_b) / se > z
def episode(seed, frac, bad_rate, z, horizon=1800):
    rng = random.Random(seed); ec = nc = eb = nb = 0; harmed = 0
    for sec in range(horizon):
        c = sum(1 for _ in range(int(RPS * frac)) if True) ; b = RPS - c
        # errores por segundo: binomial aproximada con normal/poisson
        ec_s = poisson(rng, c * bad_rate); eb_s = poisson(rng, b * BASE)
        nc += c; nb += b; ec += ec_s; eb += eb_s
        harmed += max(0, ec_s - c * BASE)
        if z_exceeds(ec, nc, eb, nb, z): return sec + 1, harmed
    return None, harmed
def poisson(rng, lam):
    if lam > 60: return max(0, int(rng.gauss(lam, math.sqrt(lam)) + 0.5))
    L = math.exp(-lam); k = 0; p = 1.0
    while True:
        p *= rng.random()
        if p <= L: return k
        k += 1
print("== tiempo hasta detectar un defecto (error 1,5 % frente a 0,5 % de base), z=3, 40 semillas")
print("fracción canario | detectado | mediana s | p95 s | usuarios afectados extra (mediana)")
for frac in (0.01, 0.05, 0.10, 0.25, 0.50):
    res = [episode(s, frac, 0.015, 3.0) for s in range(40)]
    det = [r[0] for r in res if r[0] is not None]; ext = sorted(r[1] for r in res)
    det.sort()
    print(f"{frac*100:5.0f} %           {len(det):2d}/40     {statistics.median(det) if det else float('nan'):7.0f}   {det[int(len(det)*0.95)-1] if det else float('nan'):6.0f}   {ext[20]:6.0f}")
print("== falsas alarmas: sin defecto (error 0,5 %), 1 % de canario, 200 episodios de 30 min, según el umbral z")
for z in (1.64, 2.33, 3.0, 4.0):
    fa = sum(1 for s in range(200) if episode(1000 + s, 0.05, BASE, z)[0] is not None)
    print(f"z={z:4.2f}: {fa:3d} de 200 episodios de 30 min terminan en reversión innecesaria ({fa/2:.1f} %)")
print("== tamaño del defecto: canario del 5 %, z=3, horizonte de 30 min, 40 semillas (error base 0,5 %)")
for extra in (0.001, 0.0025, 0.005, 0.01, 0.02):
    res = [episode(2000 + s, 0.05, BASE + extra, 3.0) for s in range(40)]
    det = sorted(r[0] for r in res if r[0] is not None)
    print(f"error del canario {(BASE+extra)*100:5.2f} % (+{extra*100:4.2f} pts): detectado {len(det):2d}/40; mediana {statistics.median(det) if det else float('nan'):6.0f} s")
print("== blue-green: exposición y rollback")
print("blue-green sin tráfico previo al verde: 100 % de los usuarios ven el verde en el instante del cambio; retroceso: cambio de ruta (segundos) si no hubo migración incompatible")
for name, steps in (("expandir/contraer (migración compatible hacia atrás)", True), ("migración destructiva en el despliegue", False)):
    rng = random.Random(9); can = 0; N = 1000
    for _ in range(N):
        wrote_new = rng.random() < 0.8              # el verde escribió datos con el esquema nuevo antes de detectarse el fallo
        if steps or not wrote_new: can += 1
    print(f"{name:55s} retroceso sin pérdida de datos posible en {can/N*100:5.1f} % de los casos")
