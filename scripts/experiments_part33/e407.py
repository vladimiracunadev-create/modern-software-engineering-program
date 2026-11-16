"""SE-407: taller de verificación de la procedencia de un release; casos con manipulaciones detectables y mentiras coherentes."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import tempfile, json, sys
from release import *

d = tempfile.mkdtemp(prefix="e407-")
priv, pub = keypair(d, "release")
apriv, apub = keypair(d, "atacante")
EXP = {"name": "entregas-api", "builder": "ci.example.test/builders/release@v1", "repo": "example.test/entregas-api"}
STATE = {"seq": 14}
good = make_release(d, priv)
print("python", sys.version.split()[0], sys.platform)
print("release legítimo, comprobaciones fallidas:", verifier(d, good, pub, EXP, STATE), "| hash del artefacto", sha(good["artifact"])[:16])


def resign(rel, priv_=priv, **kw):
    r = dict(rel)
    r.update(kw)
    r["signature"] = sign(d, priv_, r["manifest"])
    return r


def with_manifest(rel, **chg):
    m = json.loads(rel["manifest"])
    m.update(chg)
    return resign(rel, manifest=json.dumps(m, sort_keys=True).encode())


def with_prov(rel, **chg):
    p = json.loads(rel["provenance"])
    p.update(chg)
    pp = json.dumps(p, sort_keys=True).encode()
    r = dict(rel)
    r["provenance"] = pp
    return with_manifest(r, provenance=sha(pp))


evil_tree = dict(good["tree"])
evil_tree["entregas/mod_00.py"] += b"import os; os.system('x')\n"
evil_art = build_zip(evil_tree, LOCK)
cases = []


def add(name, rel, kind):
    cases.append((name, rel, kind))


r = dict(good); r["artifact"] = evil_art; add("artefacto cambiado, manifiesto intacto", r, "det")
r = dict(good); r["sbom"] = good["sbom"] + b" "; add("SBOM alterado", r, "det")
r = dict(good); r["provenance"] = good["provenance"].replace(b"true", b"fals"); add("procedencia alterada", r, "det")
r = dict(good); r["signature"] = bytes(64); add("firma inválida", r, "det")
add("firmado por otra clave", resign(good, apriv), "det")
add("retroceso: secuencia menor", with_manifest(good, seq=12), "det")
add("nombre de otro producto", with_manifest(good, name="otro-producto"), "det")
add("constructor distinto", with_prov(good, builder="laptop.example.test/manual"), "det")
add("repositorio distinto", with_prov(good, source={"repo": "evil.example.test/fork", "commit": "a" * 40}), "det")
add("artefacto cambiado y manifiesto re-firmado sin actualizar la procedencia", with_manifest(dict(good, artifact=evil_art), artifact=sha(evil_art)), "det")
r = dict(good); r["lock"] = LOCK.replace(b"fastlib==2.3.1", b"fastlib==2.3.2"); add("bloqueo declarado distinto del usado", r, "det")
sb = json.loads(good["sbom"]); sb["components"].pop()
r = dict(good); r["sbom"] = json.dumps(sb, sort_keys=True).encode(); r = with_manifest(r, sbom=sha(r["sbom"])); add("componente retirado del SBOM y manifiesto re-firmado", r, "det")
ev = make_release(d, priv, tree=evil_tree)
add("código malicioso aprobado en la rama y construido por el CI legítimo", ev, "lie")
add("dependencia comprometida declarada en el bloqueo", make_release(d, priv, lock=LOCK.replace(b"yamlx==1.9.0", b"yamlx==1.9.1").replace(b"cd" * 32, b"ee" * 32)), "lie")
add("commit distinto del revisado (el verificador no conoce la revisión)", make_release(d, priv, commit="b" * 40), "lie")
add("clave de firma robada: release completo y coherente", make_release(d, priv, tree=evil_tree, seq=15), "lie")
add("segundo release con la misma versión y secuencia (reemplazo silencioso)", make_release(d, priv, tree=evil_tree, seq=14), "lie")
add("procedencia con reproducible=true sin que nadie reconstruya", dict(good), "lie")
tot = {"det": [0, 0], "lie": [0, 0]}
for name, rel, kind in cases:
    bad = verifier(d, rel, pub, EXP, STATE)
    caught = bool(bad)
    tot[kind][0] += caught
    tot[kind][1] += 1
    print(f"[{kind}] {name:80s} {'RECHAZA: ' + '; '.join(bad[:2]) if caught else 'PASA'}")
print("manipulaciones detectables rechazadas: %d de %d | mentiras coherentes rechazadas: %d de %d" % (tot["det"][0], tot["det"][1], tot["lie"][0], tot["lie"][1]))
print("reconstrucción independiente desde la fuente revisada coincide con el release legítimo:", sha(build_zip(good["tree"], LOCK)) == sha(good["artifact"]),
      "| con el release malicioso:", sha(build_zip(good["tree"], LOCK)) == sha(ev["artifact"]))
print("reconstrucción desde el árbol malicioso coincide con el release malicioso (reproducible no es lo mismo que benigno):", sha(build_zip(evil_tree, LOCK)) == sha(ev["artifact"]))
