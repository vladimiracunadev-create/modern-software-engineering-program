"""SE-472: SBOM y procedencia. Validador de forma frente a 240 mutaciones; completitud por método de inventario (semilla fija)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import json, random, copy, hashlib, collections
def sha(s): return hashlib.sha256(s.encode()).hexdigest()
def base_sbom(rng, n=30):
    comps = []
    for i in range(n):
        name = f"lib{i:02d}"; ver = f"{rng.randint(0,4)}.{rng.randint(0,9)}.{rng.randint(0,9)}"
        comps.append({"name": name, "version": ver, "purl": f"pkg:pypi/{name}@{ver}", "hashes": [{"alg": "SHA-256", "content": sha(name+ver)}], "licenses": [rng.choice(["MIT","Apache-2.0","BSD-3-Clause"])]})
    return {"bomFormat": "CycloneDX", "specVersion": "1.5", "serialNumber": "urn:uuid:00000000-0000-4000-8000-000000000001",
            "metadata": {"component": {"name": "entregas-api", "version": "1.4.0"}, "timestamp": "2026-11-15T00:00:00Z"}, "components": comps}
def validate(s):
    errs = []
    if s.get("bomFormat") != "CycloneDX": errs.append("formato")
    if not s.get("specVersion"): errs.append("specVersion")
    comps = s.get("components")
    if not isinstance(comps, list) or not comps: return ["sin componentes"]
    seen = set()
    for c in comps:
        for k in ("name", "version", "purl"):
            if not c.get(k): errs.append(f"falta {k}")
        if c.get("purl") and c.get("name") and c.get("version") and c["purl"] != f"pkg:pypi/{c['name']}@{c['version']}": errs.append("purl incoherente")
        if not c.get("hashes"): errs.append("sin huella")
        if c.get("name") in seen: errs.append("duplicado")
        seen.add(c.get("name"))
    return errs
OPS = ["borrar un componente", "quitar la versión", "quitar el purl", "quitar las huellas", "duplicar componente", "purl con otra versión",
       "cambiar la versión y el purl a la vez", "cambiar la huella por otra válida", "añadir componente fantasma", "cambiar la licencia", "vaciar componentes", "cambiar el nombre y el purl a la vez"]
def mutate(s, op, rng):
    t = copy.deepcopy(s); c = t["components"]; i = rng.randrange(len(c))
    if op == OPS[0]: del c[i]
    elif op == OPS[1]: c[i]["version"] = ""
    elif op == OPS[2]: del c[i]["purl"]
    elif op == OPS[3]: c[i]["hashes"] = []
    elif op == OPS[4]: c.append(copy.deepcopy(c[i]))
    elif op == OPS[5]: c[i]["purl"] = c[i]["purl"].replace("@", "@9")
    elif op == OPS[6]: c[i]["version"] = "9.9.9"; c[i]["purl"] = f"pkg:pypi/{c[i]['name']}@9.9.9"
    elif op == OPS[7]: c[i]["hashes"][0]["content"] = sha("otro" + str(rng.random()))
    elif op == OPS[8]: c.append({"name": "ghost", "version": "1.0.0", "purl": "pkg:pypi/ghost@1.0.0", "hashes": [{"alg":"SHA-256","content":sha("ghost")}], "licenses": ["MIT"]})
    elif op == OPS[9]: c[i]["licenses"] = ["GPL-3.0-only"]
    elif op == OPS[10]: t["components"] = []
    elif op == OPS[11]: c[i]["name"] = "evil"; c[i]["purl"] = "pkg:pypi/evil@" + c[i]["version"]
    return t
rng = random.Random(400)
print("== validador de forma frente a 12 operadores x 20 SBOM base")
tot = 0; hit = 0
for op in OPS:
    k = 0
    for j in range(20):
        base = base_sbom(random.Random(j)); assert not validate(base)
        m = mutate(base, op, random.Random(j * 31 + 5))
        if validate(m): k += 1
    tot += 20; hit += k
    print(f"{op:42s} {k:2d} de 20")
print(f"total {hit} de {tot} ({hit/tot*100:.1f} %)")
# completitud por método: componentes reales = 60; el método ve según cómo se incluyen
print("== completitud del inventario por método (100 proyectos sintéticos, 60 componentes reales cada uno)")
r2 = random.Random(9)
cats = {"declarada (manifiesto)": 0.62, "transitiva en bloqueo": 0.24, "vendorizada (copiada)": 0.07, "enlazada estáticamente": 0.04, "descargada en tiempo de ejecución": 0.03}
methods = {"solo manifiesto": {"declarada (manifiesto)"}, "manifiesto + archivo de bloqueo": {"declarada (manifiesto)", "transitiva en bloqueo"},
           "bloqueo + escaneo de archivos copiados": {"declarada (manifiesto)", "transitiva en bloqueo", "vendorizada (copiada)"},
           "escaneo del artefacto final": {"declarada (manifiesto)", "transitiva en bloqueo", "vendorizada (copiada)", "enlazada estáticamente"}}
res = collections.defaultdict(list)
for p in range(100):
    comp = [r2.choices(list(cats), list(cats.values()))[0] for _ in range(60)]
    for m, vis in methods.items():
        res[m].append(sum(1 for c in comp if c in vis) / 60)
for m, v in res.items():
    v.sort(); print(f"{m:42s} mediana {v[50]*100:5.1f} %  peor proyecto {v[0]*100:5.1f} %")
print("ninguno ve las descargadas en tiempo de ejecución (3 % del total en este supuesto)")
# procedencia: campos y qué atacante pasa
print("== procedencia: ¿qué ataque pasa una verificación de campos declarados?")
checks = ["builder.id esperado", "repositorio fuente esperado", "huella del artefacto igual", "rama/etiqueta esperada", "parámetros de build esperados"]
attacks = [("artefacto sustituido tras el build", {"huella del artefacto igual"}), ("procedencia de otro repositorio", {"repositorio fuente esperado"}),
           ("build en un runner no confiable", {"builder.id esperado"}), ("commit en rama no revisada", {"rama/etiqueta esperada"}),
           ("parámetros alterados", {"parámetros de build esperados"}), ("procedencia fabricada por quien controla el builder", set()),
           ("commit malicioso aprobado en la rama protegida", set()), ("dependencia comprometida descargada durante el build", set())]
for a, caught in attacks:
    print(f"{a:55s} detectado si se verifican {len(caught)} de las 5 comprobaciones: {'sí' if caught else 'NO'}")
