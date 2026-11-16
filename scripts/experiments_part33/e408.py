"""SE-408: proyecto de release firmado y recuperable. Pipeline completo, verificación entre sistemas y simulacros de recuperación."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import json, os, shutil, sys, tempfile, time
from release import *

mode = sys.argv[1] if len(sys.argv) > 1 else "all"
SHARED = sys.argv[2] if len(sys.argv) > 2 else None
EXP = {"name": "entregas-api", "builder": "ci.example.test/builders/release@v1", "repo": "example.test/entregas-api"}


def save(rel, folder):
    os.makedirs(folder, exist_ok=True)
    for k in ("artifact", "sbom", "provenance", "manifest", "signature", "lock"):
        open(os.path.join(folder, k), "wb").write(rel[k])


def load(folder):
    return {k: open(os.path.join(folder, k), "rb").read() for k in ("artifact", "sbom", "provenance", "manifest", "signature", "lock")}


print("python", sys.version.split()[0], sys.platform, "| openssl", openssl("version").stdout.decode().split()[1])
if mode == "make":
    d = tempfile.mkdtemp(prefix="e408m-")
    priv, pub = keypair(d, "release")
    rel = make_release(d, priv)
    save(rel, os.path.join(SHARED, "release-" + sys.platform))
    shutil.copy(pub, os.path.join(SHARED, "release-" + sys.platform, "clave-publica.pem"))
    print("generado", sys.platform, "huella del artefacto", sha(rel["artifact"])[:16])
elif mode == "verify":
    d = tempfile.mkdtemp(prefix="e408v-")
    for other in sorted(os.listdir(SHARED)):
        if not other.startswith("release-"):
            continue
        folder = os.path.join(SHARED, other)
        rel = load(folder)
        pub = os.path.join(folder, "clave-publica.pem")
        print(f"verificar {other} desde {sys.platform}:", verifier(d, rel, pub, EXP, {"seq": 14}) or "sin fallos", "| huella", sha(rel["artifact"])[:16])
else:
    d = tempfile.mkdtemp(prefix="e408-")
    t = {}

    def clock(name, fn):
        s = time.perf_counter()
        r = fn()
        t[name] = (time.perf_counter() - s) * 1000
        return r

    priv, pub = keypair(d, "release")
    state = {"seq": 0}
    r13 = clock("construir y firmar 1.4.0", lambda: make_release(d, priv, version="1.4.0", seq=14))
    print("1.4.0 verificado:", verifier(d, r13, pub, EXP, state) or "ok")
    state["seq"] = 14
    tree = dict(r13["tree"])
    tree["entregas/mod_01.py"] += b"# 1.4.1: cambio con defecto\n"
    r141 = make_release(d, priv, version="1.4.1", seq=15, tree=tree)
    print("1.4.1 verificado:", verifier(d, r141, pub, EXP, state) or "ok")
    state["seq"] = 15
    print("== simulacro 1: retroceso por reinstalación del bundle firmado de 1.4.0")
    print("   verificación del bundle 1.4.0 con memoria de secuencia 15:", verifier(d, r13, pub, EXP, state))
    r142 = clock("republicar 1.4.0 como 1.4.2", lambda: make_release(d, priv, version="1.4.2", seq=16, tree=r13["tree"]))
    print("   1.4.2 (contenido de 1.4.0, secuencia 16) verificado:", verifier(d, r142, pub, EXP, state) or "ok")
    print("   los bytes del código de 1.4.2 son los de 1.4.0 salvo la línea de versión:",
          sum(1 for k in r13["tree"] if r13["tree"][k] != r142["tree"][k]) == 1)
    print("== simulacro 2: pérdida del repositorio de releases; reconstrucción desde la fuente")
    rebuilt = clock("reconstruir 1.4.0 desde la fuente", lambda: sha(build_zip(r13["tree"], LOCK)))
    print("   reconstrucción idéntica a la publicada:", rebuilt == sha(r13["artifact"]))
    print("== simulacro 3: rotación de la clave de firma")
    priv2, pub2 = keypair(d, "release2")
    stmt = json.dumps({"rotate-to": open(pub2).read(), "effective-seq": 17}, sort_keys=True).encode()
    stmt_sig = sign(d, priv, stmt)
    ok_stmt = verify(d, pub, stmt, stmt_sig)
    r17 = make_release(d, priv2, version="1.5.0", seq=17)
    print("   declaración de rotación firmada con la clave vigente válida:", ok_stmt)
    print("   release 1.5.0 verificado con la clave nueva:", verifier(d, r17, pub2, EXP, state) or "ok", "| con la clave antigua:", verifier(d, r17, pub, EXP, state))
    forged = json.dumps({"rotate-to": open(pub2).read(), "effective-seq": 17}, sort_keys=True).encode()
    print("   la misma declaración firmada con la clave nueva (sin la antigua) se rechaza con la clave fijada:", not verify(d, pub, forged, sign(d, priv2, forged)))
    print("== simulacro 4: pérdida de la clave privada sin rotación previa")
    print("   sin copia de la clave ni declaración previa, los clientes con la clave antigua fijada rechazarán toda versión nueva:", verifier(d, r17, pub, EXP, state))
    print("   la recuperación exige distribuir una clave nueva por un canal que los clientes ya confíen (acción humana, no automática)")
    for k, v in t.items():
        print(f"MEDICION {k}: {v:.1f} ms")
    ok = [verifier(d, r13, pub, EXP, {"seq": 0}), verifier(d, r141, pub, EXP, {"seq": 0}), verifier(d, r142, pub, EXP, {"seq": 0})]
    print("verificaciones sin memoria de secuencia, fallos:", [len(x) for x in ok])
