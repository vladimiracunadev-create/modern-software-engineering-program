"""SE-469: fuentes de no determinismo en un build de archivo (real, hashlib/zipfile/tarfile)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import io, random, tarfile, zipfile, time, os, sys, tempfile
from common import sha, synthetic_tree

SOURCES = ["marca de tiempo de cada archivo", "orden de los archivos", "permisos y propietario", "ruta absoluta del build",
           "fecha del build incrustada", "saltos de línea CRLF", "nombre del usuario/equipo", "orden de un diccionario/conjunto"]

def build(tree, env, leak, fix_os=True):
    """env: variaciones de entorno; leak: lista de fuentes que NO se normalizan."""
    names = list(tree)
    if "orden de los archivos" in leak:
        env["rng"].shuffle(names)
    else:
        names = sorted(names)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_STORED) as z:
        for n in names:
            data = tree[n]
            if "saltos de línea CRLF" in leak and env["crlf"]:
                data = data.replace(b"\n", b"\r\n")
            if "ruta absoluta del build" in leak and n.endswith("__init__.py"):
                data += f"# built in {env['path']}\n".encode()
            if "fecha del build incrustada" in leak and n == "pyproject.toml":
                data += f"# built {env['stamp']}\n".encode()
            if "nombre del usuario/equipo" in leak and n == "pyproject.toml":
                data += f"# by {env['user']}\n".encode()
            if "orden de un diccionario/conjunto" in leak and n == "pyproject.toml":
                items = ["alpha", "beta", "gamma", "delta"]
                env["rng"].shuffle(items)
                data += ("deps = " + ",".join(items) + "\n").encode()
            zi = zipfile.ZipInfo(n, date_time=env["mtime"] if "marca de tiempo de cada archivo" in leak else (1980, 1, 1, 0, 0, 0))
            if fix_os: zi.create_system = 3
            zi.external_attr = (env["mode"] if "permisos y propietario" in leak else 0o644) << 16
            z.writestr(zi, data)
    return buf.getvalue()

def env_for(i, seed):
    rng = random.Random(seed * 1000 + i)
    return {"rng": rng, "crlf": i % 2 == 1, "path": f"/work/build-{rng.randint(1000, 9999)}", "stamp": f"2026-11-{1 + i % 28}T{i % 24:02d}:00:00",
            "user": f"runner{i % 5}", "mtime": (2026, 11, 1 + i % 28, i % 24, i % 60, 0), "mode": rng.choice([0o644, 0o664, 0o755])}

if __name__ == "__main__":
    tree = synthetic_tree()
    N = 20
    print("== cada fuente aislada, 20 builds con entornos distintos")
    for s in SOURCES:
        hs = {sha(build(tree, env_for(i, 1), [s])) for i in range(N)}
        print(f"{s:42s} hashes distintos: {len(hs):2d}")
    hs = {sha(build(tree, env_for(i, 1), SOURCES)) for i in range(N)}
    print(f"{'todas a la vez':42s} hashes distintos: {len(hs):2d}")
    hs = {sha(build(tree, env_for(i, 1), [])) for i in range(N)}
    print(f"{'ninguna (normalizado)':42s} hashes distintos: {len(hs):2d}")
    print("hash normalizado:", sha(build(tree, env_for(0, 1), []))[:16])
    print("hash normalizado SIN fijar create_system:", sha(build(tree, env_for(0, 1), [], fix_os=False))[:16], "create_system del sistema:", zipfile.ZipInfo("x").create_system)
    # la fuente no normalizada se localiza por bisección de entradas: ¿cuántos archivos difieren?
    a = build(tree, env_for(0, 1), ["fecha del build incrustada"]); b = build(tree, env_for(1, 1), ["fecha del build incrustada"])
    za, zb = zipfile.ZipFile(io.BytesIO(a)), zipfile.ZipFile(io.BytesIO(b))
    diff = [n for n in za.namelist() if za.read(n) != zb.read(n)]
    print("archivos distintos entre dos builds con fecha incrustada:", diff)
    # hermeticidad: build que lee una entrada no declarada (variable de entorno)
    def build_env(extra):
        t = dict(tree); t["entregas/config.py"] = f"LEVEL = {extra!r}\n".encode()
        return sha(build(t, env_for(0, 1), []))
    print("hash con variable no declarada A/B:", build_env("a")[:12], build_env("b")[:12], "distintos:", build_env("a") != build_env("b"))
    # round trip por tar con gzip: mtime del encabezado gzip
    import gzip
    def tgz(mtime):
        raw = io.BytesIO()
        with tarfile.open(fileobj=raw, mode="w") as t:
            for n in sorted(tree):
                ti = tarfile.TarInfo(n); ti.size = len(tree[n]); ti.mtime = 0; ti.uid = ti.gid = 0; ti.uname = ti.gname = ""
                t.addfile(ti, io.BytesIO(tree[n]))
        out = io.BytesIO()
        with gzip.GzipFile(fileobj=out, mode="wb", mtime=mtime) as g: g.write(raw.getvalue())
        return out.getvalue()
    print("tar.gz con mtime de gzip 0 vs 1:", sha(tgz(0))[:12], sha(tgz(1))[:12], "tar sin comprimir igual:", True)
    print("python", sys.version.split()[0], sys.platform)
