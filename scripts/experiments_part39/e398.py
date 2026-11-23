"""SE-470: promoción por huella frente a reconstrucción; etiquetas mutables; retención y retroceso (simulación con semilla)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import random, hashlib
R = 2000
def run_promo(seed, p_drift, rebuild):
    rng = random.Random(seed)
    diff = 0; escaped = 0
    for _ in range(R):
        staged = rng.random()  # identidad del artefacto probado en staging
        # la reconstrucción para prod produce otra huella si algo flota (dependencia, hora, imagen base)
        prod_same = True if not rebuild else (rng.random() >= p_drift)
        if not prod_same:
            diff += 1
            # el defecto que solo vive en el artefacto distinto no pudo verse en staging
            if rng.random() < 0.12: escaped += 1
    return diff, escaped
print("== reconstrucción para producción vs promoción por huella (2000 releases por celda)")
for p in (0.01, 0.05, 0.15):
    d, e = run_promo(11, p, True); d2, e2 = run_promo(11, p, False)
    print(f"p_deriva={p:.2f}  reconstruir: prod distinto de staging {d:4d} ({d/R*100:4.1f} %), defectos no vistos en staging {e:3d} | promover: {d2} ({e2})")
print("== etiquetas mutables: 1000 días, repush de la misma etiqueta con p por día; un despliegue por día")
for p in (0.0, 0.02, 0.10):
    rng = random.Random(5); digest = 0; tested = 0; mismatch = 0; rollback_wrong = 0
    for day in range(1000):
        if rng.random() < p: digest += 1          # alguien vuelve a publicar la misma etiqueta
        if day % 7 == 0: tested = digest          # se prueba el viernes
        if day % 7 == 3 and digest != tested: mismatch += 1  # se despliega por etiqueta el martes
    # en el retroceso: «volver a la etiqueta v1.3» trae un contenido distinto del que corrió
    print(f"p_repush={p:.2f}  despliegues por etiqueta con contenido distinto del probado: {mismatch:3d} de 143")
print("== retención: el retroceso necesita la versión N-k; limpieza conserva las últimas M versiones")
rng = random.Random(21)
depths = []
for _ in range(10000):
    # profundidad del retroceso: 1 casi siempre; a veces hay que saltar versiones con migraciones o defectos latentes
    k = 1
    while rng.random() < 0.30 and k < 12: k += 1
    depths.append(k)
for M in (1, 2, 3, 5, 10):
    ok = sum(1 for k in depths if k <= M)
    print(f"conserva últimas {M:2d} versiones: retroceso posible en {ok/len(depths)*100:5.1f} % de los casos; hay que reconstruir en {100-ok/len(depths)*100:4.1f} %")
import collections
c = collections.Counter(depths)
print("profundidad:", {k: c[k] for k in sorted(c)})
