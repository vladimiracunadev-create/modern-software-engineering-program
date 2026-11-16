"""Canal de release sintético reutilizado por e407 y e408 (herramienta de autor): build determinista, SBOM, procedencia, firma Ed25519 con openssl."""
import io, json, os, subprocess, tempfile, zipfile, hashlib
from common import sha, synthetic_tree


def openssl(*a, inp=None):
    return subprocess.run(["openssl", *a], input=inp, capture_output=True)


def keypair(d, name):
    priv = os.path.join(d, name + ".pem")
    pub = os.path.join(d, name + ".pub")
    openssl("genpkey", "-algorithm", "ED25519", "-out", priv)
    openssl("pkey", "-in", priv, "-pubout", "-out", pub)
    return priv, pub


def sign(d, priv, data):
    f = os.path.join(d, "s.in")
    open(f, "wb").write(data)
    o = os.path.join(d, "s.out")
    r = openssl("pkeyutl", "-sign", "-inkey", priv, "-rawin", "-in", f, "-out", o)
    assert r.returncode == 0
    return open(o, "rb").read()


def verify(d, pub, data, sig):
    f = os.path.join(d, "v.in")
    open(f, "wb").write(data)
    g = os.path.join(d, "v.sig")
    open(g, "wb").write(sig)
    return openssl("pkeyutl", "-verify", "-pubin", "-inkey", pub, "-rawin", "-in", f, "-sigfile", g).returncode == 0


def build_zip(tree, lock):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_STORED) as z:
        for n in sorted(tree):
            zi = zipfile.ZipInfo(n, date_time=(1980, 1, 1, 0, 0, 0))
            zi.create_system = 3
            zi.external_attr = 0o644 << 16
            z.writestr(zi, tree[n])
        zi = zipfile.ZipInfo("requirements.lock", date_time=(1980, 1, 1, 0, 0, 0))
        zi.create_system = 3
        zi.external_attr = 0o644 << 16
        z.writestr(zi, lock)
    return buf.getvalue()


LOCK = b"fastlib==2.3.1 --hash=sha256:" + b"ab" * 32 + b"\nyamlx==1.9.0 --hash=sha256:" + b"cd" * 32 + b"\n"


def make_release(d, priv, version="1.4.0", seq=14, commit="a" * 40, builder="ci.example.test/builders/release@v1", tree=None, lock=LOCK, repo="example.test/entregas-api"):
    tree = dict(tree or synthetic_tree())
    tree["entregas/__init__.py"] = f'__version__ = "{version}"\n'.encode()
    art = build_zip(tree, lock)
    comps = [{"name": l.split("==")[0], "version": l.split("==")[1].split()[0], "hashes": [{"alg": "SHA-256", "content": l.split("sha256:")[1]}]} for l in lock.decode().splitlines()]
    sbom = json.dumps({"bomFormat": "CycloneDX", "specVersion": "1.5", "metadata": {"component": {"name": "entregas-api", "version": version}}, "components": comps}, sort_keys=True).encode()
    prov = json.dumps({"subject": {"name": f"entregas-api-{version}.zip", "sha256": sha(art)}, "builder": builder, "source": {"repo": repo, "commit": commit},
                       "materials": {"requirements.lock": sha(lock), "sbom": sha(sbom)}, "reproducible": True}, sort_keys=True).encode()
    manifest = json.dumps({"name": "entregas-api", "version": version, "seq": seq, "artifact": sha(art), "sbom": sha(sbom), "provenance": sha(prov)}, sort_keys=True).encode()
    return {"artifact": art, "sbom": sbom, "provenance": prov, "manifest": manifest, "signature": sign(d, priv, manifest), "lock": lock, "tree": tree}


def verifier(d, rel, pub, expected, state):
    """Devuelve la lista de comprobaciones fallidas."""
    bad = []
    if not verify(d, pub, rel["manifest"], rel["signature"]):
        return ["firma del manifiesto"]
    m = json.loads(rel["manifest"])
    if m["name"] != expected["name"]:
        bad.append("nombre")
    if m["seq"] < state["seq"]:
        bad.append("secuencia (retroceso)")
    if sha(rel["artifact"]) != m["artifact"]:
        bad.append("huella del artefacto")
    if sha(rel["sbom"]) != m["sbom"]:
        bad.append("huella del SBOM")
    if sha(rel["provenance"]) != m["provenance"]:
        bad.append("huella de la procedencia")
    try:
        p = json.loads(rel["provenance"])
    except ValueError:
        return bad + ["procedencia ilegible"]
    if p["subject"]["sha256"] != m["artifact"]:
        bad.append("sujeto de la procedencia distinto del artefacto")
    if p["builder"] != expected["builder"]:
        bad.append("constructor no esperado")
    if p["source"]["repo"] != expected["repo"]:
        bad.append("repositorio no esperado")
    if p["materials"]["requirements.lock"] != sha(rel["lock"]):
        bad.append("bloqueo distinto de los materiales")
    comp = {(c["name"], c["version"]) for c in json.loads(rel["sbom"])["components"]}
    lockc = {(l.split("==")[0], l.split("==")[1].split()[0]) for l in rel["lock"].decode().splitlines()}
    if comp != lockc:
        bad.append("SBOM distinto del bloqueo")
    z = zipfile.ZipFile(io.BytesIO(rel["artifact"]))
    if z.read("requirements.lock") != rel["lock"]:
        bad.append("bloqueo dentro del artefacto distinto del declarado")
    return bad
