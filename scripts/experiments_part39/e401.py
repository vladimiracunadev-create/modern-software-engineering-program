"""SE-473: checksums y firmas Ed25519 reales con openssl (se ejecuta openssl del equipo); matriz de ataques frente a 6 estrategias de verificación."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import subprocess, tempfile, os, hashlib, json, time, sys
from common import sha
T = tempfile.mkdtemp(prefix="e401-")
def run(*a, inp=None):
    return subprocess.run(["openssl", *a], input=inp, capture_output=True, check=False)
def keygen(name):
    p = os.path.join(T, name + ".pem"); run("genpkey", "-algorithm", "ED25519", "-out", p)
    pub = run("pkey", "-in", p, "-pubout", "-out", os.path.join(T, name + ".pub")); return p, os.path.join(T, name + ".pub")
def sign(priv, data):
    f = os.path.join(T, "m.bin"); open(f, "wb").write(data); s = os.path.join(T, "m.sig")
    r = run("pkeyutl", "-sign", "-inkey", priv, "-rawin", "-in", f, "-out", s); assert r.returncode == 0, r.stderr
    return open(s, "rb").read()
def verify(pub, data, sig):
    f = os.path.join(T, "v.bin"); open(f, "wb").write(data); s = os.path.join(T, "v.sig"); open(s, "wb").write(sig)
    return run("pkeyutl", "-verify", "-pubin", "-inkey", pub, "-rawin", "-in", f, "-sigfile", s).returncode == 0
priv, pub = keygen("release"); apriv, apub = keygen("atacante")
art = lambda ver, body=b"": (f"entregas-api {ver}\n".encode() + b"\x00" * 2000 + body)
def manifest(name, ver, seq, a): return json.dumps({"name": name, "version": ver, "seq": seq, "sha256": sha(a)}, sort_keys=True).encode()
A = art("1.4.0"); OLD = art("1.2.0"); EVIL = art("1.4.0", b"backdoor")
legit = {"artifact": A, "checksum": sha(A), "manifest": manifest("entregas-api", "1.4.0", 14, A)}
legit["msig"] = sign(priv, legit["manifest"]); legit["asig"] = sign(priv, A)
oldm = manifest("entregas-api", "1.2.0", 12, OLD); old = {"artifact": OLD, "checksum": sha(OLD), "manifest": oldm, "msig": sign(priv, oldm), "asig": sign(priv, OLD)}
other = manifest("otro-producto", "1.4.0", 14, A); othersig = sign(priv, other)
# estado que el verificador recuerda: su clave fijada y el mayor seq visto
STATE = {"seq": 14, "revoked": set()}
def attack(n):
    d = dict(legit); host = {"pub": pub}
    if n == 1: d["artifact"] = EVIL; d["_note"] = "cuerpo cambiado, checksum intacto"
    elif n == 2: d["artifact"] = EVIL; d["checksum"] = sha(EVIL); d["_note"] = "cuerpo y checksum cambiados (control de la página)"
    elif n == 3: d["artifact"] = EVIL; d["asig"] = sign(apriv, EVIL); d["manifest"] = manifest("entregas-api", "1.4.0", 14, EVIL); d["msig"] = sign(apriv, d["manifest"]); d["checksum"] = sha(EVIL); host["pub"] = apub
    elif n == 4: d = dict(old); d["_note"] = "versión vieja firmada válida"
    elif n == 5: d["asig"] = bytes(64); d["msig"] = bytes(64)
    elif n == 6: d["manifest"] = other; d["msig"] = othersig
    elif n == 7: d["artifact"] = A[:1000]
    elif n == 8: d["artifact"] = EVIL; d["manifest"] = manifest("entregas-api", "1.4.0", 14, EVIL); d["msig"] = sign(priv, d["manifest"]); d["asig"] = sign(priv, EVIL); d["checksum"] = sha(EVIL); d["_note"] = "clave de firma robada"
    elif n == 9: d["artifact"] = EVIL; d["manifest"] = manifest("entregas-api", "1.4.0", 15, EVIL); d["msig"] = sign(priv, d["manifest"]); d["asig"] = sign(priv, EVIL); d["checksum"] = sha(EVIL); d["_note"] = "el CI comprometido firma el backdoor con la clave real"
    return d, host
NAMES = {1: "cuerpo cambiado, checksum intacto", 2: "cuerpo y checksum cambiados en el mismo host", 3: "cuerpo, firma y clave del atacante publicados juntos",
         4: "versión antigua válida servida como la última (rollback)", 5: "firma corrupta", 6: "manifiesto firmado de otro producto", 7: "archivo truncado",
         8: "clave de firma robada", 9: "CI comprometido que firma con la clave real"}
def s1(d, h): return sha(d["artifact"]) == d["checksum"]                         # checksum de la misma página
def s2(d, h): return sha(d["artifact"]) == legit["checksum"]                     # checksum por un canal independiente
def s3(d, h): return verify(h["pub"], d["artifact"], d["asig"])                  # firma con clave de la misma página
def s4(d, h): return verify(pub, d["artifact"], d["asig"])                       # clave fijada de antemano
def s5(d, h):                                                                      # clave fijada + manifiesto firmado con nombre, versión y seq creciente
    if not verify(pub, d["manifest"], d["msig"]): return False
    m = json.loads(d["manifest"]); return m["name"] == "entregas-api" and m["seq"] >= STATE["seq"] and m["sha256"] == sha(d["artifact"])
def s6(d, h): return s5(d, h) and pub not in STATE["revoked"]
STRATS = [("1 checksum de la misma página", s1), ("2 checksum por canal aparte", s2), ("3 firma, clave de la misma página", s3), ("4 firma con clave fijada", s4), ("5 clave fijada + manifiesto firmado con seq", s5), ("6 igual que 5 + revocación", s6)]
print("openssl:", run("version").stdout.decode().strip().split("\n")[0], "| Python", sys.version.split()[0], sys.platform)
print("== el instalador legítimo debe pasar las 6:", [f(legit, {"pub": pub}) for _, f in STRATS])
print("== matriz: ¿la estrategia RECHAZA el ataque? (R = rechaza, P = pasa)")
print(" " * 56 + "  ".join(n[0] for n, _ in STRATS))
tot = {n: 0 for n, _ in STRATS}
for a in range(1, 10):
    d, h = attack(a)
    line = []
    for n, f in STRATS:
        ok = f(d, h); line.append("P" if ok else "R"); tot[n] += (0 if ok else 1)
    print(f"{a} {NAMES[a]:54s}" + "  ".join(line))
print("rechazados de 9:", {n: v for n, v in tot.items()})
# revocación: tras revocar la clave robada, el ataque 8 se rechaza solo con 6
STATE["revoked"].add(pub); d, h = attack(8)
print("tras revocar la clave, ataque 8 con estrategia 5:", "P" if s5(d, h) else "R", "| con 6:", "P" if s6(d, h) else "R", "| el instalador legítimo con 6:", "P" if s6(legit, {"pub": pub}) else "R (también rechaza lo legítimo si no hay clave nueva)")
# coste real de hashing (cambia por equipo)
data = os.urandom(64 * 1024 * 1024)
for alg in ("sha256", "sha512", "blake2b", "sha3_256"):
    t = time.perf_counter(); hashlib.new(alg, data).hexdigest(); dt = time.perf_counter() - t
    print(f"MEDICION {alg:9s} 64 MiB: {dt*1000:7.1f} ms ({64/dt:6.0f} MiB/s)")
t = time.perf_counter(); [verify(pub, A, legit["asig"]) for _ in range(20)]; print(f"MEDICION verificar 1 firma Ed25519 con proceso openssl: {(time.perf_counter()-t)/20*1000:.1f} ms")
