"""SE-474: versionado y compatibilidad. Comparador de API pública con ast frente a 14 tipos de cambio; etiquetado de versiones por autores simulados; resolución de rangos."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import ast, random, itertools, collections
V1 = '''
def subir_entrega(curso, archivo, comentario=None):
    return {"curso": curso, "estado": "recibida"}
def listar_entregas(curso, pagina=1, tamano=20):
    return []
def consultar_nota(entrega_id):
    return {"nota": 7.0, "escala": "1-7"}
class Entrega:
    def cerrar(self, motivo):
        return True
def _interno(x):
    return x
'''
def api(src):
    t = ast.parse(src); out = {}
    for n in t.body:
        if isinstance(n, ast.FunctionDef) and not n.name.startswith("_"):
            a = n.args; names = [x.arg for x in a.args]; nd = len(a.defaults)
            req = names[:len(names) - nd]; opt = dict(zip(names[len(names) - nd:], [ast.dump(d) for d in a.defaults]))
            out[n.name] = (tuple(req), tuple(opt.items()))
        elif isinstance(n, ast.ClassDef):
            out[n.name] = ("class", tuple(sorted(m.name for m in n.body if isinstance(m, ast.FunctionDef))))
    return out
def classify(old, new):
    """devuelve 'mayor', 'menor' o 'parche' según lo que ve la firma."""
    lvl = "parche"
    for k, v in old.items():
        if k not in new: return "mayor"
        if v != new[k]:
            if v[0] == "class":
                if set(v[1]) - set(new[k][1]): return "mayor"
                lvl = "menor"
            else:
                oreq, oopt = v; nreq, nopt = new[k]
                if nreq != oreq and not (nreq[:len(oreq)] == oreq and False): return "mayor"
                if dict(oopt) != {a: b for a, b in nopt if a in dict(oopt)}: return "mayor"   # cambia un valor por defecto o se quita un opcional
                if len(nopt) < len(oopt): return "mayor"
                lvl = "menor"
    if set(new) - set(old) and lvl == "parche": lvl = "menor"
    return lvl
CHANGES = [
 ("añadir una función pública", V1 + "def exportar(curso):\n    return []\n", "menor"),
 ("quitar una función pública", V1.replace("def listar_entregas(curso, pagina=1, tamano=20):\n    return []\n", ""), "mayor"),
 ("renombrar un parámetro obligatorio", V1.replace("def consultar_nota(entrega_id)", "def consultar_nota(id_entrega)"), "mayor"),
 ("añadir un parámetro obligatorio", V1.replace("def consultar_nota(entrega_id)", "def consultar_nota(entrega_id, alumno)"), "mayor"),
 ("añadir un parámetro opcional al final", V1.replace("tamano=20)", "tamano=20, orden='fecha')"), "menor"),
 ("cambiar el valor por defecto de un parámetro", V1.replace("tamano=20", "tamano=50"), "mayor"),
 ("hacer opcional un parámetro obligatorio", V1.replace("def subir_entrega(curso, archivo, comentario=None)", "def subir_entrega(curso, archivo=None, comentario=None)"), "menor"),
 ("quitar un método de una clase", V1.replace("    def cerrar(self, motivo):\n        return True\n", "    def abrir(self):\n        return True\n"), "mayor"),
 ("añadir un método a una clase", V1.replace("class Entrega:\n", "class Entrega:\n    def abrir(self):\n        return True\n"), "menor"),
 ("cambiar un interno privado", V1.replace("return x\n", "return x + 1\n", 1).replace("{\"curso\": curso, \"estado\": \"recibida\"}", "{\"curso\": curso, \"estado\": \"recibida\"}"), "parche"),
 ("cambiar la escala de la nota (1-7 a 0-100) sin tocar la firma", V1.replace('"escala": "1-7"', '"escala": "0-100"').replace("7.0", "70.0"), "mayor"),
 ("cambiar el orden por defecto del listado", V1.replace("    return []\n", "    return [1]\n", 1), "mayor"),
 ("corregir un error que devolvía un estado erróneo", V1.replace('"recibida"', '"recibida" if True else "x"'), "parche"),
 ("lanzar una excepción nueva ante entrada inválida", V1.replace("def cerrar(self, motivo):\n        return True", "def cerrar(self, motivo):\n        if not motivo: raise ValueError\n        return True"), "mayor"),
]
base = api(V1); order = ["parche", "menor", "mayor"]
print("== comparador de firmas públicas frente a 14 tipos de cambio (nivel correcto vs nivel que ve la herramienta)")
ok = 0; underestimate = 0
for name, src, truth in CHANGES:
    got = classify(base, api(src)); good = got == truth; ok += good
    under = order.index(got) < order.index(truth); underestimate += under
    print(f"{name:62s} correcto={truth:6s} herramienta={got:6s} {'OK' if good else ('SUBESTIMA' if under else 'sobrestima')}")
print(f"acierta {ok} de {len(CHANGES)}; subestima {underestimate} (cambios que rompen sin que la firma lo diga)")
# etiquetado de 3000 lanzamientos: la herramienta ve 5 de los 8 cambios incompatibles de la lista (62,5 %); el autor se equivoca con p dada
print("== etiquetado de 3000 lanzamientos simulados (12 % incompatibles; la herramienta ve 5 de 8 incompatibles = medido arriba)")
rng = random.Random(402)
mix = rng.choices(["parche", "menor", "mayor"], [0.55, 0.33, 0.12], k=3000)
def author(t, r, p):
    if t != "parche" and r.random() < p: return order[order.index(t) - 1]
    return t
def tool(t, r):
    if t == "mayor" and r.random() > 5 / 8: return "parche"
    return t
def mx(a, b): return a if order.index(a) >= order.index(b) else b
pol = {"a mano, sin disciplina (22 % de subestimación)": lambda t, r: author(t, r, 0.22),
       "a mano con revisión de la lista de cambios (10 %)": lambda t, r: author(t, r, 0.10),
       "solo el comparador de firmas": lambda t, r: tool(t, r),
       "comparador + etiqueta manual con revisión (el mayor de los dos)": lambda t, r: mx(tool(t, r), author(t, r, 0.10))}
for name, f in pol.items():
    r = random.Random(11); under = sum(1 for t in mix if order.index(f(t, r)) < order.index(t))
    print(f"{name:66s} rompen y se publican como menor/parche: {under:3d} de {sum(1 for t in mix if t!='parche')} cambios con efecto ({under/ (sum(1 for t in mix if t!='parche'))*100:.1f} %)")
