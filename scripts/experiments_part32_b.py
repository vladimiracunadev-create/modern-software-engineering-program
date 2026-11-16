"""Experimentos de SE-391 a SE-396 (datos sintéticos, semilla fija, solo biblioteca estándar).

Uso: python scripts/experiments_part32_b.py   (imprime una línea JSON por experimento)

Todo lo que se ataca es código de juguete escrito aquí, en memoria y sin red. Las lecturas de
reloj (e392_redos) y las sondas de e396_portabilidad cambian entre equipos y ejecuciones.
"""
import ast
import hashlib
import hmac
import json
import math
import ntpath
import os
import posixpath
import random
import re
import secrets
import sys
import tempfile
import time
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

sys.stdout.reconfigure(encoding="utf-8")


# ----------------------------------------------------------------- SE-391
def e391_kanon():
    r = random.Random(3911)
    N = 5000
    comunas = [f"C{i:02d}" for i in range(48)]
    region = {c: f"R{i // 3:02d}" for i, c in enumerate(comunas)}
    macro = {f"R{i:02d}": f"Z{i // 6}" for i in range(16)}
    cursos = [f"K{i:02d}" for i in range(30)]
    filas = []
    for _ in range(N):
        anio = min(2008, max(1990, round(r.gauss(2000, 4))))
        c = r.choices(comunas, weights=[1 / (i + 1) ** 0.6 for i in range(48)])[0]
        filas.append((anio, c, r.choice(cursos), r.choice("FMX")))
    niveles = {
        "datos exactos (año, comuna, curso, género)": lambda f: (f[0], f[1], f[2], f[3]),
        "año a tramo de 3 y comuna a región": lambda f: (f[0] // 3, region[f[1]], f[2], f[3]),
        "tramo de 5 años, región, sin curso": lambda f: (f[0] // 5, region[f[1]], f[3]),
        "tramo de 5 años, macrozona, sin curso ni género": lambda f: (f[0] // 5, macro[region[f[1]]]),
    }
    out = []
    for nombre, g in niveles.items():
        cnt = Counter(g(f) for f in filas)
        k_min = min(cnt.values())
        unicos = sum(1 for f in filas if cnt[g(f)] == 1)
        menos5 = sum(1 for f in filas if cnt[g(f)] < 5)
        out.append((nombre, len(cnt), k_min, round(100 * unicos / N, 1), round(100 * menos5 / N, 1)))
    return {"filas": out, "N": N}


def e391_dp():
    r = random.Random(3912)
    verdadero = 312
    def lap(eps):
        return r.expovariate(eps) - r.expovariate(eps)  # sensibilidad 1: escala 1/eps
    filas = []
    for eps in (0.1, 0.5, 1.0, 5.0):
        err = sum(abs(lap(eps)) for _ in range(20000)) / 20000
        filas.append((eps, round(err, 2)))
    # ataque de promedio: el mismo conteo preguntado Q veces con ruido nuevo
    prom = []
    for Q in (1, 10, 100, 1000, 10000):
        errs = []
        for _ in range(200):
            m = sum(verdadero + lap(0.5) for _ in range(Q)) / Q
            errs.append(abs(m - verdadero))
        prom.append((Q, round(sum(errs) / len(errs), 3), round(0.5 * Q, 1)))
    return {"error_por_eps": filas, "promedio_repetido_eps_0.5": prom}


def e391_pseudo():
    r = random.Random(3913)
    candidatos = [f"persona{i}@ejemplo.test" for i in range(100000)]
    usuarios = [candidatos[i] for i in r.sample(range(100000), 12000)]
    ajenos = [f"otra{i}@desconocido.test" for i in range(8000)]
    todos = usuarios + ajenos
    clave = secrets.token_bytes(32)
    s1 = {hashlib.sha256(e.encode()).hexdigest(): e for e in todos}
    tabla = {hashlib.sha256(e.encode()).hexdigest(): e for e in candidatos}
    reid_hash = sum(1 for h in s1 if h in tabla)
    hm = {hmac.new(clave, e.encode(), hashlib.sha256).hexdigest(): e for e in todos}
    reid_hmac = sum(1 for h in hm if h in tabla)
    # enlace entre dos conjuntos con el mismo seudónimo
    k1, k2 = secrets.token_bytes(32), secrets.token_bytes(32)
    a = {hmac.new(clave, e.encode(), hashlib.sha256).hexdigest() for e in usuarios[:6000]}
    b_mismo = {hmac.new(clave, e.encode(), hashlib.sha256).hexdigest() for e in usuarios[:6000]}
    b_otra = {hmac.new(k2, e.encode(), hashlib.sha256).hexdigest() for e in usuarios[:6000]}
    return {"seudonimos": len(todos), "reidentificados_sha256_sin_sal": reid_hash, "reidentificados_hmac_sin_clave": reid_hmac,
            "enlazables_misma_clave": len(a & b_mismo), "enlazables_clave_por_proposito": len(a & b_otra), "k1_distinta_de_k2": k1 != k2}


# ----------------------------------------------------------------- SE-392
EXT = {"pdf": "application/pdf", "png": "image/png", "txt": "text/plain"}


def valida_ref(nombre, tam, mime, curso, m=frozenset()):
    if not isinstance(curso, int) or isinstance(curso, bool):
        if "N12" in m and isinstance(curso, str) and curso.isdigit():
            curso = int(curso)
        else:
            return False
    if not (1 <= curso <= (9999 if "N13" not in m else 10000)):
        return False
    if (tam < 0 if "N1" in m else tam <= 0):
        return False
    if (tam > 10_000_000 if "N2" not in m else tam >= 10_000_000):
        return False
    if len(nombre) > 80 and "N9" not in m:
        return False
    if "N7" not in m and any(ch in nombre for ch in "/\\\x00"):
        return False
    if "N8" not in m and not re.fullmatch(r"[A-Za-z0-9_\-. ]+", nombre):
        return False
    base, _, ext = nombre.rpartition(".")
    if not base:
        return False
    if "N4" in m:
        if not any(("." + e) in nombre for e in EXT):
            return False
        ext = next(e for e in EXT if ("." + e) in nombre)
    elif "N3" not in m:
        ext = ext.lower()
    if ext not in EXT:
        return False
    if "N5" not in m and "." in base and re.search(r"\.(exe|bat|js|sh|html)$", base, re.I):
        return False
    if "N6" not in m and EXT[ext] != mime:
        return False
    if "N10" in m and nombre.startswith("."):
        return True
    if "N11" not in m and nombre.startswith("."):
        return False
    return True


MUT = {"N1": "acepta tamaño negativo", "N2": "límite de tamaño con >= en vez de >", "N3": "extensión sensible a mayúsculas", "N4": "busca la extensión como subcadena",
       "N5": "acepta doble extensión ejecutable", "N6": "no contrasta tipo MIME con extensión", "N7": "permite separadores de ruta y NUL", "N8": "sin lista blanca de caracteres",
       "N9": "sin límite de longitud del nombre", "N10": "acepta nombres ocultos", "N11": "(equivalente) nombres ocultos sin comprobar", "N12": "acepta el curso como texto numérico", "N13": "límite superior del curso desplazado"}


def e392_mutacion():
    mutantes = [k for k in MUT if k != "N11"]
    positivos = [("ensayo.pdf", 120_000, "application/pdf", 12), ("foto.png", 80_000, "image/png", 7), ("notas.txt", 900, "text/plain", 101), ("Informe 2.pdf", 4_000_000, "application/pdf", 55), ("a-b_c.txt", 10, "text/plain", 1)]
    tipicos = [("../../etc/passwd", 100, "text/plain", 1), ("virus.exe", 100, "application/octet-stream", 1), ("a.pdf", 0, "application/pdf", 1), ("a.pdf", 100, "image/png", 1), ("a.pdf", 100, "application/pdf", 0), ("a.pdf", 100, "application/pdf", "7; DROP"), ("a.pdf", 20_000_000, "application/pdf", 1), ("a.pdf", 100, "application/pdf", -3), ("sin_extension", 5, "text/plain", 1), ("a b<c>.pdf", 5, "application/pdf", 1)]
    bordes = [("a.pdf", 1, "application/pdf", 1), ("a.pdf", 10_000_000, "application/pdf", 1), ("a.pdf", 10_000_001, "application/pdf", 1), ("a.pdf", -1, "application/pdf", 1), ("a.pdf", 5, "application/pdf", 9999), ("a.pdf", 5, "application/pdf", 10000), ("A.PDF", 5, "application/pdf", 1), ("a.pdf.exe", 5, "application/pdf", 1), ("x.pdf.txt", 5, "text/plain", 1), ("a.pdf", 5, "application/pdf", "7"), (".oculto.pdf", 5, "application/pdf", 1), ("a" * 81 + ".pdf", 5, "application/pdf", 1), ("a\x00.pdf", 5, "application/pdf", 1), ("a/b.pdf", 5, "application/pdf", 1), ("c:\\a.pdf", 5, "application/pdf", 1)]
    rr = random.Random(3921)
    alfa = ["a", "B", "7", "_", "-", ".", " ", "/", "\\", "\x00", "é", "<", "pdf", "exe", "PNG", "txt"]
    def entrada():
        n = "".join(rr.choice(alfa) for _ in range(rr.randrange(1, 12)))
        return (n, rr.choice([-1, 0, 1, 5000, 10_000_000, 10_000_001]), rr.choice(["application/pdf", "image/png", "text/plain", "x/y"]), rr.choice([0, 1, 9999, 10000, "7", 5]))
    azar = [entrada() for _ in range(2000)] + [e for e in (positivos + bordes)]
    suites = {"solo ejemplos válidos": positivos, "más negativos típicos": positivos + tipicos, "más valores de borde": positivos + tipicos + bordes, "más 2 000 entradas al azar contra la referencia": positivos + tipicos + bordes + azar}
    out = {}
    for nombre, s in suites.items():
        vivos = [k for k in mutantes if not any(valida_ref(*t, m=frozenset([k])) != valida_ref(*t) for t in s)]
        out[nombre] = {"pruebas": len(s), "detectados": len(mutantes) - len(vivos), "vivos": vivos}
    out["_mutantes"] = len(mutantes)
    return out


def e392_reglas():
    # 40 fragmentos con defecto y 40 seguros más 12 difíciles; reglas con ast
    malos = ["eval(x)", "yaml.load(x)", "subprocess.run(cmd, shell=True)", "pickle.loads(x)", "hashlib.md5(p).hexdigest()", "token = str(random.random())", "password = 'abc123'", "requests.get(u, verify=False)"]
    buenos = ["ast.literal_eval(x)", "yaml.safe_load(x)", "subprocess.run(cmd)", "json.loads(x)", "hashlib.sha256(p).hexdigest()", "token = secrets.token_hex(16)", "password = os.environ['P']", "requests.get(u)"]
    dificiles_malos = ["f = eval\nf(x)", "from subprocess import run as r\nr(cmd, shell=True)", "k = True\nsubprocess.run(cmd, shell=k)", "yaml.load(x, Loader=yaml.FullLoader)", "import pickle as p\np.loads(x)", "clave = 'p' + 'ass1234'"]
    dificiles_buenos = ["# eval(x) en un comentario", "s = 'eval(x)'", "def eval(x):\n    return x\neval(3)", "password = ''", "subprocess.run(cmd, shell=False)", "hashlib.md5(x, usedforsecurity=False)"]
    casos = [(c, True) for c in malos * 3] + [(c, False) for c in buenos * 3] + [(c, True) for c in dificiles_malos] + [(c, False) for c in dificiles_buenos]
    def reglas(code):
        try:
            t = ast.parse(code)
        except SyntaxError:
            return False
        for n in ast.walk(t):
            if isinstance(n, ast.Call):
                f = n.func
                nombre = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else "")
                if nombre in ("eval", "exec"):
                    return True
                if nombre == "load" and isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) and f.value.id == "yaml" and not any(k.arg == "Loader" for k in n.keywords):
                    return True
                if nombre == "loads" and isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name) and f.value.id == "pickle":
                    return True
                if nombre in ("run", "call", "Popen") and any(k.arg == "shell" and isinstance(k.value, ast.Constant) and k.value.value is True for k in n.keywords):
                    return True
                if nombre == "md5" and isinstance(f, ast.Attribute):
                    return True
                if nombre == "get" and any(k.arg == "verify" and isinstance(k.value, ast.Constant) and k.value.value is False for k in n.keywords):
                    return True
            if isinstance(n, ast.Assign):
                for tg in n.targets:
                    if isinstance(tg, ast.Name) and re.search(r"pass(word)?|clave|secret", tg.id, re.I) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str) and n.value.value:
                        return True
                    if isinstance(tg, ast.Name) and tg.id == "token" and isinstance(n.value, ast.Call) and "random" in ast.dump(n.value):
                        return True
        return False
    tp = sum(1 for c, m in casos if m and reglas(c))
    fp = sum(1 for c, m in casos if not m and reglas(c))
    fn = sum(1 for c, m in casos if m and not reglas(c))
    sencillos = [(c, m) for c, m in casos if c in malos or c in buenos]
    tps = sum(1 for c, m in sencillos if m and reglas(c))
    fps = sum(1 for c, m in sencillos if not m and reglas(c))
    fns = sum(1 for c, m in sencillos if m and not reglas(c))
    dif = [(c, m) for c, m in casos if c in dificiles_malos or c in dificiles_buenos]
    tpd = sum(1 for c, m in dif if m and reglas(c))
    fpd = sum(1 for c, m in dif if not m and reglas(c))
    fnd = sum(1 for c, m in dif if m and not reglas(c))
    return {"total": len(casos), "sencillos": {"fragmentos": len(sencillos), "detectados": tps, "falsas_alarmas": fps, "perdidos": fns},
            "dificiles": {"fragmentos": len(dif), "detectados": tpd, "falsas_alarmas": fpd, "perdidos": fnd}, "todos": {"detectados": tp, "falsas_alarmas": fp, "perdidos": fn}}


def e392_redos():
    patron_malo = re.compile(r"^(a+)+$")
    patron_bueno = re.compile(r"^a+$")
    filas = []
    previo = None
    for n in range(14, 25, 2):
        s = "a" * n + "!"
        t0 = time.perf_counter()
        patron_malo.match(s)
        dt = time.perf_counter() - t0
        t1 = time.perf_counter()
        patron_bueno.match(s)
        db = time.perf_counter() - t1
        filas.append((n, round(dt * 1000, 2), round(db * 1000, 4), None if previo is None else round(dt / previo, 1)))
        previo = dt
    return {"filas": filas}


# ----------------------------------------------------------------- SE-393
AV = {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2}
AC = {"L": 0.77, "H": 0.44}
UI = {"N": 0.85, "R": 0.62}
CIA = {"H": 0.56, "L": 0.22, "N": 0.0}


def _roundup(x):
    i = round(x * 100000)
    return i / 100000.0 if i % 10000 == 0 else (math.floor(i / 10000) + 1) / 10.0


def cvss(v):
    d = dict(p.split(":") for p in v.split("/")[1:])
    cambia = d["S"] == "C"
    pr = {"N": 0.85, "L": 0.68 if cambia else 0.62, "H": 0.5 if cambia else 0.27}[d["PR"]]
    iss = 1 - (1 - CIA[d["C"]]) * (1 - CIA[d["I"]]) * (1 - CIA[d["A"]])
    imp = 7.52 * (iss - 0.029) - 3.25 * (iss - 0.02) ** 15 if cambia else 6.42 * iss
    ex = 8.22 * AV[d["AV"]] * AC[d["AC"]] * pr * UI[d["UI"]]
    if imp <= 0:
        return 0.0
    return _roundup(min(1.08 * (imp + ex), 10)) if cambia else _roundup(min(imp + ex, 10))


def banda(s):
    return "ninguna" if s == 0 else "baja" if s < 4 else "media" if s < 7 else "alta" if s < 9 else "crítica"


def e393_cvss():
    comprobaciones = {"AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H": cvss("CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"), "XSS reflejado": cvss("CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N")}
    hallazgos = [
        ("lectura de notas ajenas por identificador", ["AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N", "AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N", "AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N"]),
        ("cambio de nota por falta de comprobación de dueño", ["AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N", "AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:N", "AV:N/AC:H/PR:L/UI:N/S:U/C:N/I:H/A:N"]),
        ("XSS almacenado en un comentario", ["AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N", "AV:N/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N", "AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N"]),
        ("inyección SQL en la búsqueda de entregas", ["AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H", "AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H", "AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:L/A:N"]),
        ("secreto en un registro accesible a soporte", ["AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N", "AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N", "AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:N/A:N"]),
        ("denegación por expresión regular catastrófica", ["AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H", "AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H", "AV:N/AC:H/PR:N/UI:N/S:U/C:N/I:N/A:L"]),
    ]
    filas = []
    for nom, vs in hallazgos:
        sc = [cvss("CVSS:3.1/" + v) for v in vs]
        filas.append((nom, sc, min(sc), max(sc), round(max(sc) - min(sc), 1), banda(min(sc)), banda(max(sc))))
    return {"comprobaciones": comprobaciones, "filas": filas}


def e393_prioridad():
    r = random.Random(3931)
    N = 3000
    vul = []
    for _ in range(N):
        cv = min(10.0, max(0.0, round(r.gauss(6.2, 1.9), 1)))
        p = 0.02 + 0.015 * (cv >= 7)  # supuesto del autor: la gravedad influye poco en la explotación
        expl = r.random() < p
        vul.append((cv, expl))
    ex_total = sum(1 for _, e in vul if e)
    res = {}
    altos = [v for v in vul if v[0] >= 7]
    res["CVSS >= 7"] = (len(altos), sum(1 for _, e in altos if e))
    criticos = [v for v in vul if v[0] >= 9]
    res["CVSS >= 9"] = (len(criticos), sum(1 for _, e in criticos if e))
    res["lista de explotación conocida"] = (ex_total, ex_total)
    # mezcla: lista de explotación conocida + CVSS >= 9 sin explotar
    mix = {i for i, v in enumerate(vul) if v[1] or v[0] >= 9}
    res["explotadas + CVSS >= 9"] = (len(mix), sum(1 for i in mix if vul[i][1]))
    return {"total": N, "explotadas": ex_total, "estrategias": res}


def e393_divulgacion():
    r = random.Random(3932)
    def corrige():
        return math.exp(r.gauss(math.log(30), 0.9))
    def adopta():
        return r.expovariate(1 / 20)
    out = []
    for plazo in (45, 90, 120):
        n = 20000
        sin_parche = 0
        exp_publica = []
        total = []
        for _ in range(n):
            f = corrige()
            a = adopta()
            if f > plazo:
                sin_parche += 1
                exp_publica.append(f - plazo)  # días con la falla pública y sin corrección
            total.append(f + a)
        out.append((plazo, round(100 * sin_parche / n, 1), round(sum(exp_publica) / max(1, len(exp_publica)), 1), round(sorted(total)[n // 2], 1), round(sorted(total)[int(n * 0.9)], 1)))
    return {"filas": out, "mediana_correccion_dias": 30}


def _abierto(t):
    # minutos desde el lunes 00:00; abierto lunes a viernes de 9 a 17
    d, m = divmod(int(t), 1440)
    return (d % 7) < 5 and 540 <= m < 1020


def _avanza(t, trabajo):
    while trabajo > 0:
        d, m = divmod(t, 1440)
        if (int(d) % 7) >= 5:
            t = (int(d) // 7 * 7 + 7) * 1440 + 540
            continue
        if m < 540:
            t = int(d) * 1440 + 540
            continue
        if m >= 1020:
            sig = int(d) + 1
            t = sig * 1440 + 540
            continue
        disp = 1020 - m
        usa = min(disp, trabajo)
        t += usa
        trabajo -= usa
    return t


def e393_triaje():
    out = []
    for c in (1, 2, 3):
        r = random.Random(3933)
        t = 0.0
        libres = [0.0] * c
        esperas = []
        # 6 informes por semana (10 080 min): llegadas de Poisson
        tasa = 6 / 10080
        horizonte = 10080 * 52
        while True:
            t += r.expovariate(tasa)
            if t > horizonte:
                break
            valido = r.random() >= 0.40
            trabajo = r.expovariate(1 / (360 if valido else 120))
            k = min(range(c), key=lambda i: libres[i])
            inicio = max(t, libres[k])
            primera = _avanza(inicio, 15)  # primer acuse: 15 min de trabajo
            fin = _avanza(inicio, trabajo)
            libres[k] = fin
            esperas.append((primera - t) / 60.0)
        esperas.sort()
        out.append((c, len(esperas), round(esperas[len(esperas) // 2], 1), round(esperas[int(len(esperas) * 0.9)], 1), round(esperas[int(len(esperas) * 0.99)], 1)))
    return {"filas": out}


# ----------------------------------------------------------------- SE-394
def e394_embudo():
    r = random.Random(3941)
    reqs = 40
    controles = 28
    filas = []
    for i in range(reqs):
        tiene_control = r.random() < 0.90
        tiene_prueba = tiene_control and r.random() < 0.78
        edad = int(r.expovariate(1 / 70)) if tiene_prueba else None
        paso = tiene_prueba and r.random() < 0.93
        filas.append((tiene_control, tiene_prueba, edad, paso))
    a = sum(1 for f in filas if f[0])
    b = sum(1 for f in filas if f[1])
    c = sum(1 for f in filas if f[1] and f[3])
    d = sum(1 for f in filas if f[1] and f[3] and f[2] <= 90)
    e = sum(1 for f in filas if f[1] and f[3] and f[2] <= 30)
    return {"requisitos": reqs, "con_control_documentado": a, "con_prueba": b, "con_prueba_que_paso": c, "y_evidencia_de_90_dias_o_menos": d, "y_de_30_dias_o_menos": e}


def e394_muestreo():
    N, D = 2000, 30
    def p_exacta(n):
        return 1 - math.comb(N - D, n) / math.comb(N, n)
    r = random.Random(3942)
    pob = [1] * D + [0] * (N - D)
    filas = []
    for n in (10, 25, 60, 100, 200):
        enc = 0
        for _ in range(20000):
            if sum(r.sample(pob, n)):
                enc += 1
        filas.append((n, round(100 * p_exacta(n), 1), round(100 * enc / 20000, 1)))
    # defectos concentrados: cuentas de servicio son el 4 % de los eventos y el 60 % de los defectos
    N2, S, DS, DO = 2000, 80, 18, 12
    def p_estr(nS, nO):
        pS = 1 - math.comb(S - DS, nS) / math.comb(S, nS)
        pO = 1 - math.comb(N2 - S - DO, nO) / math.comb(N2 - S, nO)
        return 1 - (1 - pS) * (1 - pO)
    aleatorio_n = 25
    pa = 1 - math.comb(N2 - (DS + DO), aleatorio_n) / math.comb(N2, aleatorio_n)
    pe = p_estr(15, 10)
    from math import log
    n95 = math.ceil(log(0.05) / log(1 - D / N))
    return {"filas": filas, "n_para_95_con_1_5_por_ciento_aprox": n95, "concentrados_25_aleatorios": round(100 * pa, 1), "concentrados_15_en_servicio_y_10_en_resto": round(100 * pe, 1)}


def e394_cadena():
    r = random.Random(3943)
    def construye(n):
        prev = "0" * 64
        out = []
        for i in range(n):
            cuerpo = f"evento-{i}"
            h = hashlib.sha256((prev + cuerpo).encode()).hexdigest()
            out.append((cuerpo, h))
            prev = h
        return out
    def verifica(cad):
        prev = "0" * 64
        for cuerpo, h in cad:
            if hashlib.sha256((prev + cuerpo).encode()).hexdigest() != h:
                return False
            prev = h
        return True
    n = 1000
    ancla = construye(n)[-1][1]  # huella publicada fuera del sistema
    def ataques(tipo):
        det_cadena = det_ancla = 0
        for _ in range(100):
            cad = construye(n)
            k = r.randrange(1, n - 20)
            if tipo == "modificar un evento":
                cad[k] = ("evento-alterado", cad[k][1])
            elif tipo == "borrar un evento":
                del cad[k]
            elif tipo == "reordenar dos eventos":
                cad[k], cad[k + 1] = cad[k + 1], cad[k]
            elif tipo == "truncar los últimos 10":
                cad = cad[:-10]
            elif tipo == "reescribir desde k recalculando":
                nuevo = construye(n)
                prev = cad[k - 1][1]
                rest = []
                for i in range(k, n):
                    c = f"falso-{i}"
                    h = hashlib.sha256((prev + c).encode()).hexdigest()
                    rest.append((c, h))
                    prev = h
                cad = cad[:k] + rest
            ok = verifica(cad)
            det_cadena += (not ok)
            det_ancla += ((not ok) or cad[-1][1] != ancla)
        return det_cadena, det_ancla
    tipos = ["modificar un evento", "borrar un evento", "reordenar dos eventos", "truncar los últimos 10", "reescribir desde k recalculando"]
    return {"filas": [(t,) + ataques(t) for t in tipos]}


# ----------------------------------------------------------------- SE-395
def e395_ruta():
    r = random.Random(3951)
    base = "/srv/entregas"
    alfa = ["..", ".", "/", "\\", "%2e", "%2f", "a", "....//", "..././", "%2e%2e%2f", "x"]
    cargas = []
    for _ in range(5000):
        cargas.append("".join(r.choice(alfa) for _ in range(r.randrange(1, 6))))
    def decod(s):
        return unquote(s)
    def sale(modulo, ruta_final, base_):
        p = modulo.normpath(modulo.join(base_, ruta_final.lstrip("/\\") if modulo is posixpath else ruta_final.lstrip("/\\")))
        b = modulo.normpath(base_)
        if modulo is ntpath:
            p, b = p.lower(), b.lower()
        return not (p == b or p.startswith(b + modulo.sep))
    def quita_una_vez(s):
        return s.replace("../", "")
    def quita_en_bucle(s):
        while "../" in s:
            s = s.replace("../", "")
        return s
    res = {}
    for nombre, f in (("quitar «../» una vez y decodificar después", lambda s: decod(quita_una_vez(s))),
                      ("quitar «../» en bucle y decodificar después", lambda s: decod(quita_en_bucle(s))),
                      ("decodificar, resolver y comprobar el prefijo", lambda s: decod(s))):
        out = {}
        for mod, base_ in ((posixpath, "/srv/entregas"), (ntpath, "C:\\srv\\entregas")):
            n_sale = sum(1 for c in cargas if sale(mod, f(c), base_))
            out[mod.__name__] = n_sale
        res[nombre] = out
    # para la tercera, la comprobación de prefijo rechaza: cuenta las que habría servido fuera de la raíz tras comprobar
    res["_cargas"] = len(cargas)
    # con comprobación de prefijo, las rutas que salen se rechazan
    comp = {}
    for mod, base_ in ((posixpath, "/srv/entregas"), (ntpath, "C:\\srv\\entregas")):
        comp[mod.__name__] = sum(1 for c in cargas if sale(mod, decod(c), base_) and False)
    res["decodificar, resolver y comprobar el prefijo"] = comp
    res["_rechazadas_por_la_comprobacion"] = {m.__name__: sum(1 for c in cargas if sale(m, decod(c), b)) for m, b in ((posixpath, "/srv/entregas"), (ntpath, "C:\\srv\\entregas"))}
    # un ejemplo conocido
    res["_ejemplo"] = {"....//secreto": quita_una_vez("....//secreto")}
    return res


def e395_limitador():
    def vulnerable(intentos):
        cont = Counter()
        permitidos = 0
        for ip_cabecera, _ in intentos:
            if cont[ip_cabecera] < 5:
                cont[ip_cabecera] += 1
                permitidos += 1
        return permitidos, len(cont)
    def corregido(intentos):
        cont = Counter()
        permitidos = 0
        for _, ip_conexion in intentos:
            if cont[ip_conexion] < 5:
                cont[ip_conexion] += 1
                permitidos += 1
        return permitidos, len(cont)
    intentos = [(f"10.9.{i // 250}.{i % 250}", "198.51.100.7") for i in range(1000)]
    honesto = [("198.51.100.7", "198.51.100.7")] * 1000
    return {"cabecera_rotada": {"vulnerable": vulnerable(intentos), "corregido": corregido(intentos)}, "sin_rotar": {"vulnerable": vulnerable(honesto), "corregido": corregido(honesto)}}


def e395_csrf():
    clave = b"clave-de-servidor-de-ejemplo"
    def token_para(sesion):
        return hmac.new(clave, sesion.encode(), hashlib.sha256).hexdigest()
    def v_presencia(sesion, tok):
        return bool(tok)
    def v_global(sesion, tok):
        return tok == token_para("sesion-de-ana")  # valor único compartido por todos
    def v_ligado(sesion, tok):
        return hmac.compare_digest(tok or "", token_para(sesion))
    ataques = [("sin token", "bruno", ""), ("token inventado", "bruno", "x"), ("token vacío con espacios", "bruno", " "), ("token de otra sesión", "bruno", token_para("sesion-de-ana")), ("token propio", "bruno", token_para("bruno")), ("token de la sesión de ana, usado por ana", "sesion-de-ana", token_para("sesion-de-ana"))]
    filas = []
    for nom, ses, tok in ataques:
        filas.append((nom, v_presencia(ses, tok), v_global(ses, tok), v_ligado(ses, tok)))
    return {"filas": filas}


def e395_algoritmo():
    import base64
    def b64(d):
        return base64.urlsafe_b64encode(json.dumps(d).encode()).rstrip(b"=").decode()
    def firma(msg, clave):
        return base64.urlsafe_b64encode(hmac.new(clave, msg.encode(), hashlib.sha256).digest()).rstrip(b"=").decode()
    clave = b"clave-del-servidor"
    def emite(claims):
        c = b64({"alg": "HS256"}) + "." + b64(claims)
        return c + "." + firma(c, clave)
    def parse(tok):
        h, c, f = tok.split(".")
        pad = lambda s: s + "=" * (-len(s) % 4)
        return json.loads(base64.urlsafe_b64decode(pad(h))), json.loads(base64.urlsafe_b64decode(pad(c))), h + "." + c, f
    def verifica_vulnerable(tok):
        h, c, msg, f = parse(tok)
        if h.get("alg") == "none":
            return c
        return c if hmac.compare_digest(firma(msg, clave), f) else None
    def verifica_corregida(tok):
        h, c, msg, f = parse(tok)
        if h.get("alg") != "HS256":
            return None
        return c if hmac.compare_digest(firma(msg, clave), f) else None
    legit = emite({"sub": "ana", "rol": "estudiante"})
    forjado_none = b64({"alg": "none"}) + "." + b64({"sub": "ana", "rol": "docente"}) + "."
    forjado_firma = b64({"alg": "HS256"}) + "." + b64({"sub": "ana", "rol": "docente"}) + "." + firma("x", b"otra")
    alterado = legit.split(".")[0] + "." + b64({"sub": "ana", "rol": "docente"}) + "." + legit.split(".")[2]
    casos = [("token legítimo", legit), ("alg none con rol docente", forjado_none), ("firma de otra clave", forjado_firma), ("carga alterada con firma vieja", alterado)]
    return {"filas": [(n, verifica_vulnerable(t) is not None, verifica_corregida(t) is not None) for n, t in casos]}


# ----------------------------------------------------------------- SE-396
def _paquete(r, n=30):
    reqs = []
    for i in range(n):
        reqs.append({"id": f"R{i:02d}", "estado": "cumple", "prueba": f"T{i:02d}", "evidencia": f"ev/R{i:02d}.txt", "fecha_dias": r.randrange(1, 60), "alcance": "1.4.0", "notas": ""})
    return reqs


def e396_validador():
    r = random.Random(3961)
    base = _paquete(r)
    evid = {q["evidencia"]: f"resultado de {q['prueba']}: 12 aprobadas, 0 falladas\n" for q in base}
    pruebas = {q["prueba"]: {"asserts": 3, "resultado": "ok"} for q in base}
    def v1(reqs, evid, pruebas):
        errs = []
        for q in reqs:
            if q["estado"] == "cumple" and not q["evidencia"]:
                errs.append(1)
        return errs
    def v2(reqs, evid, pruebas):
        errs = v1(reqs, evid, pruebas)
        ids = [q["id"] for q in reqs]
        if len(set(ids)) != len(ids):
            errs.append(2)
        for q in reqs:
            if q["estado"] == "cumple":
                if q["evidencia"] not in evid:
                    errs.append(3)
                if q["prueba"] not in pruebas:
                    errs.append(4)
                if q["fecha_dias"] > 90 or q["fecha_dias"] < 0:
                    errs.append(5)
                if q["alcance"] != "1.4.0":
                    errs.append(6)
            if q["estado"] == "no aplica" and not q["notas"]:
                errs.append(7)
            if q["estado"] == "excepción" and not q.get("dueno"):
                errs.append(8)
        return errs
    def v3(reqs, evid, pruebas):
        errs = v2(reqs, evid, pruebas)
        vistos = Counter(hashlib.sha256(evid[q["evidencia"]].encode()).hexdigest() for q in reqs if q["evidencia"] in evid)
        if any(v > 1 for v in vistos.values()):
            errs.append(9)
        for q in reqs:
            if q["estado"] == "cumple" and q["prueba"] in pruebas:
                if pruebas[q["prueba"]]["asserts"] == 0:
                    errs.append(10)
                if pruebas[q["prueba"]]["resultado"] != "ok":
                    errs.append(11)
            if q["estado"] == "cumple" and q["evidencia"] in evid and len(evid[q["evidencia"]].strip()) == 0:
                errs.append(12)
        return errs
    ops = ["quitar la evidencia", "evidencia que no existe", "prueba que no existe", "fecha de 120 días", "alcance de otra versión", "no aplica sin justificación", "excepción sin dueño", "identificador duplicado",
           "la misma evidencia en 10 requisitos", "prueba sin ninguna aserción", "prueba que falló marcada como cumple", "archivo de evidencia vacío",
           "copia de la evidencia de otro requisito", "evidencia única sin relación (dice «aprobado» sin ejecutar nada)"]
    def muta(op, k):
        reqs = [dict(q) for q in base]
        ev = dict(evid)
        pr = {a: dict(b) for a, b in pruebas.items()}
        i = r.randrange(len(reqs))
        q = reqs[i]
        if op == ops[0]:
            q["evidencia"] = ""
        elif op == ops[1]:
            q["evidencia"] = "ev/inexistente.txt"
        elif op == ops[2]:
            q["prueba"] = "T99"
        elif op == ops[3]:
            q["fecha_dias"] = 120
        elif op == ops[4]:
            q["alcance"] = "1.3.0"
        elif op == ops[5]:
            q["estado"], q["notas"] = "no aplica", ""
        elif op == ops[6]:
            q["estado"] = "excepción"
        elif op == ops[7]:
            reqs[(i + 1) % len(reqs)]["id"] = q["id"]
        elif op == ops[8]:
            for j in range(10):
                reqs[(i + j) % len(reqs)]["evidencia"] = q["evidencia"]
        elif op == ops[9]:
            pr[q["prueba"]]["asserts"] = 0
        elif op == ops[10]:
            pr[q["prueba"]]["resultado"] = "falla"
        elif op == ops[11]:
            ev[q["evidencia"]] = ""
        elif op == ops[12]:
            q["evidencia"] = reqs[(i + 5) % len(reqs)]["evidencia"]
            q["prueba"] = reqs[(i + 5) % len(reqs)]["prueba"]
            q["id"] = q["id"]
        elif op == ops[13]:
            ev[q["evidencia"]] = "APROBADO. todo correcto.\n"
        return reqs, ev, pr
    res = {}
    for op in ops:
        c = [0, 0, 0]
        for k in range(15):
            rq, ev, pr = muta(op, k)
            for j, v in enumerate((v1, v2, v3)):
                if v(rq, ev, pr):
                    c[j] += 1
        res[op] = c
    tot = [sum(res[o][j] for o in ops) for j in range(3)]
    return {"por_operador": res, "totales": tot, "mutaciones": 15 * len(ops)}


def e396_portabilidad():
    d = Path(tempfile.mkdtemp(prefix="pq32_"))
    (d / "informe").mkdir()
    for i, nombre in enumerate(["b.txt", "A.txt", "ñ.txt", "informe/c.txt", "informe/B.txt"]):
        (d / nombre).parent.mkdir(exist_ok=True)
        (d / nombre).write_bytes(f"línea 1 de {i}\r\nlínea 2\r\n".encode() if i % 2 == 0 else f"línea 1 de {i}\nlínea 2\n".encode())
    def ingenuo():
        h = hashlib.sha256()
        for p in os.listdir(d):
            q = d / p
            if q.is_file():
                h.update(p.encode() + q.read_bytes())
        for root, _, files in os.walk(d / "informe"):
            for f in files:
                p = os.path.join(root, f)
                h.update(p.replace(str(d), "").encode() + Path(p).read_bytes())
        return h.hexdigest()[:16]
    def canonico():
        h = hashlib.sha256()
        for q in sorted(d.rglob("*"), key=lambda p: p.relative_to(d).as_posix().encode("utf-8")):
            if q.is_file():
                rel = q.relative_to(d).as_posix()
                h.update(rel.encode("utf-8") + b"\0" + q.read_bytes().replace(b"\r\n", b"\n") + b"\0")
        return h.hexdigest()[:16]
    try:
        return {"sistema": sys.platform, "orden_listdir": sorted(os.listdir(d))[:0] or os.listdir(d), "hash_ingenuo": ingenuo(), "hash_canonico": canonico()}
    finally:
        import shutil
        shutil.rmtree(d, ignore_errors=True)


if __name__ == "__main__":
    for nombre, fn in sorted(globals().items()):
        if nombre.startswith("e3") and callable(fn):
            if len(sys.argv) > 1 and not any(nombre.startswith(a) for a in sys.argv[1:]):
                continue
            print(json.dumps({nombre: fn()}, ensure_ascii=False))
