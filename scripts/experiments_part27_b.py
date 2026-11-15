"""Experimentos de SE-331 a SE-336 (datos sintéticos, semilla fija, solo biblioteca estándar).

Uso: python scripts/experiments_part27_b.py   (imprime una línea JSON por experimento)
"""
import hashlib, hmac, json, random, re, sqlite3, sys, threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPConnection

sys.stdout.reconfigure(encoding="utf-8")


# ------------------------------------------------------------------ 331
def e331_sondeo():
    r = random.Random(3311)
    day = 86400
    t, ev = 0.0, []
    while True:
        t += r.expovariate(12 / 3600)  # 12 eventos por hora
        if t >= day: break
        ev.append(t)
    rows = []
    for iv in (10, 30, 60, 300, 900, 3600):
        reqs = day // iv
        lat = []
        for e in ev:
            nxt = (int(e // iv) + 1) * iv
            lat.append(nxt - e)
        busy = len({int(e // iv) for e in ev})
        lat.sort()
        rows.append((iv, reqs, round(100 * (1 - busy / reqs), 1), round(sum(lat) / len(lat), 1), round(lat[int(len(lat) * .95)], 1)))
    return len(ev), rows


SECRET = b"secreto-de-ensayo"


def firmar(ts, cuerpo, secreto=SECRET):
    return hmac.new(secreto, f"{ts}.".encode() + cuerpo, hashlib.sha256).hexdigest()


def e331_firma():
    cuerpo = json.dumps({"id": "evt_1", "entrega": 7, "nota": 6.5}, separators=(",", ":")).encode()
    ahora = 1_800_000_000
    visto = set()

    def pol_nada(h, b, ahora): return True

    def pol_cuerpo(h, b, ahora):
        return hmac.compare_digest(h["sig"], hmac.new(SECRET, b, hashlib.sha256).hexdigest())

    def pol_tiempo(h, b, ahora):
        return abs(ahora - h["ts"]) <= 300 and hmac.compare_digest(h["sig"], firmar(h["ts"], b))

    def pol_id(h, b, ahora, seen=visto):
        if not pol_tiempo(h, b, ahora): return False
        i = json.loads(b)["id"]
        if i in seen: return False
        seen.add(i); return True

    def hdr(ts, b, secreto=SECRET, legacy=False):
        return {"ts": ts, "sig": hmac.new(secreto, b, hashlib.sha256).hexdigest() if legacy else firmar(ts, b, secreto)}

    casos = []
    # (nombre, cabecera, cuerpo, ahora, debe_aceptar)
    b0 = cuerpo
    casos.append(("válido", None, b0, ahora, True))
    casos.append(("cuerpo alterado", None, b0.replace(b"6.5", b"7.0"), ahora, False))
    casos.append(("firma con otro secreto", "otro", b0, ahora, False))
    casos.append(("sin firma", "vacía", b0, ahora, False))
    casos.append(("repetición 10 min después", "viejo", b0, ahora + 600, False))
    casos.append(("repetición inmediata del mismo id", None, b0, ahora + 1, False))
    casos.append(("JSON reserializado con espacios", "ser", json.dumps(json.loads(b0)).encode(), ahora, False))
    res = {}
    for nom, pol in (("sin verificar", pol_nada), ("HMAC del cuerpo", pol_cuerpo), ("HMAC con marca de tiempo", pol_tiempo), ("más identificador visto", pol_id)):
        visto.clear()
        fila = []
        for cn, tipo, cb, ah, debe in casos:
            if tipo is None:
                h = hdr(ahora, b0, legacy=(nom == "HMAC del cuerpo"))
            elif tipo == "otro": h = hdr(ahora, b0, secreto=b"otro", legacy=(nom == "HMAC del cuerpo"))
            elif tipo == "vacía": h = {"ts": ahora, "sig": ""}
            elif tipo == "viejo": h = hdr(ahora, b0, legacy=(nom == "HMAC del cuerpo"))
            elif tipo == "ser": h = hdr(ahora, b0, legacy=(nom == "HMAC del cuerpo"))
            if nom == "más identificador visto" and cn == "repetición inmediata del mismo id":
                pol(hdr(ahora, b0), b0, ahora)  # primera entrega ya vista
            fila.append(pol(h, cb, ah))
        res[nom] = fila
    return [c[0] for c in casos], [c[4] for c in casos], res


def e331_transporte_real():
    """Servidor HTTP real en la interfaz de bucle local con un puerto efímero."""
    recibido = []

    class H(BaseHTTPRequestHandler):
        def do_POST(self):
            n = int(self.headers["Content-Length"])
            cuerpo = self.rfile.read(n)
            ok = hmac.compare_digest(self.headers["X-Firma"], firmar(self.headers["X-Marca"], cuerpo))
            recibido.append(ok)
            self.send_response(204 if ok else 401); self.end_headers()
        def log_message(self, *a): pass
    srv = HTTPServer(("127.0.0.1", 0), H)
    th = threading.Thread(target=srv.serve_forever, daemon=True); th.start()
    url = f"http://127.0.0.1:{srv.server_port}/"
    cuerpo = b'{"id":"evt_9","entrega":9}'
    out = []
    for nombre, c in (("bytes originales", cuerpo), ("reserializado", json.dumps(json.loads(cuerpo)).encode())):
        conexion = HTTPConnection("127.0.0.1", srv.server_port, timeout=5)
        conexion.request("POST", "/", body=c, headers={"X-Marca": "1800000000", "X-Firma": firmar("1800000000", cuerpo)})
        out.append((nombre, conexion.getresponse().status))
        conexion.close()
    srv.shutdown()
    return out


def e331_reintentos():
    r = random.Random(3313)
    caida = (3600.0, 10800.0)  # receptor caído 2 horas
    eventos = [i * 10.0 for i in range(1440)]  # uno cada 10 s durante 4 h
    esquemas = {
        "3 reintentos fijos (1 s)": [1, 1, 1],
        "5 reintentos exponenciales (1, 5, 30, 120, 600 s)": [1, 5, 30, 120, 600],
        "9 reintentos hasta 6 h con jitter": [1, 5, 30, 120, 600, 1800, 3600, 7200, 10800],
    }
    rows = []
    for nombre, esq in esquemas.items():
        rr = random.Random(3314)
        ent = perm = dup = 0
        for t0 in eventos:
            t = t0
            hecho = False
            procesados = 0
            intentos = [0] + esq
            for i, d in enumerate(intentos):
                t = t + (d * (0.5 + rr.random()) if "jitter" in nombre and i else d)
                caido = caida[0] <= t < caida[1]
                if caido: continue
                procesados += 1
                if rr.random() < 0.05:  # el receptor procesó pero la respuesta se perdió
                    continue
                hecho = True; break
            if hecho: ent += 1
            else: perm += 1
            if procesados > 1: dup += procesados - 1
        rows.append((nombre, ent, perm, dup))
    # reconciliación por sondeo cada 15 min tras los fallos
    perm_min = min(p for _, _, p, _ in rows)
    return len(eventos), rows


# ------------------------------------------------------------------ 332
BASE = {"id": str, "estudiante": str, "curso": str}


def leer(schema, msg, estricto):
    out = {}
    for campo, (tipo, req) in schema.items():
        if campo not in msg:
            if req: raise KeyError(f"falta {campo}")
            continue
        if not isinstance(msg[campo], tipo): raise TypeError(f"{campo}: tipo")
        out[campo] = msg[campo]
    if estricto:
        extra = set(msg) - set(schema)
        if extra: raise ValueError(f"campos desconocidos {sorted(extra)}")
    return out


V1 = {"id": (str, True), "estudiante": (str, True), "curso": (str, True), "estado": (str, True)}
MUT = {
    "añadir campo opcional": lambda s: {**s, "comentario": (str, False)},
    "añadir campo obligatorio": lambda s: {**s, "intento": (int, True)},
    "quitar campo opcional": None,
    "quitar campo obligatorio": lambda s: {k: v for k, v in s.items() if k != "curso"},
    "renombrar campo": lambda s: {("alumno" if k == "estudiante" else k): v for k, v in s.items()},
    "cambiar tipo": lambda s: {**s, "id": (int, True)},
    "volver obligatorio uno opcional": None,
}
SAMPLE = {"id": "e1", "estudiante": "s1", "curso": "c1", "estado": "recibida"}


def instancia(schema, maxima=True):
    d = {}
    for k, (t, req) in schema.items():
        if req or maxima:
            d[k] = {str: "x", int: 1}[t]
    return d


def e332_matriz():
    base_opt = {**V1, "comentario": (str, False)}
    cambios = {
        "añadir campo opcional": (V1, {**V1, "comentario": (str, False)}),
        "añadir campo obligatorio": (V1, {**V1, "intento": (int, True)}),
        "quitar campo opcional": (base_opt, V1),
        "quitar campo obligatorio": (V1, {k: v for k, v in V1.items() if k != "curso"}),
        "renombrar campo": (V1, {("alumno" if k == "estudiante" else k): v for k, v in V1.items()}),
        "cambiar tipo": (V1, {**V1, "id": (int, True)}),
        "volver obligatorio un opcional": (base_opt, {**V1, "comentario": (str, True)}),
    }
    rows = []
    for nombre, (viejo, nuevo) in cambios.items():
        celdas = []
        for estricto in (False, True):
            def prueba(esq_lector, esq_escritor):
                try:
                    for mx in (True, False): leer(esq_lector, instancia(esq_escritor, mx), estricto)
                    return True
                except Exception: return False
            back = prueba(nuevo, viejo)   # lector nuevo lee datos viejos
            fwd = prueba(viejo, nuevo)    # lector viejo lee datos nuevos
            celdas.append((back, fwd))
        rows.append((nombre, celdas))
    return rows


def e332_despliegue():
    """Despliegue gradual: cinco pasos; en cada paso el 20 % más de instancias está en la versión nueva."""
    cambios = {
        "añadir campo opcional": (V1, {**V1, "comentario": (str, False)}),
        "añadir campo obligatorio": (V1, {**V1, "intento": (int, True)}),
        "renombrar campo": (V1, {("alumno" if k == "estudiante" else k): v for k, v in V1.items()}),
    }
    rows = []
    for nombre, (viejo, nuevo) in cambios.items():
        for estricto in (False, True):
            for orden in ("productores primero", "consumidores primero"):
                r = random.Random(3321)
                falla = 0
                total = 0
                for paso in range(1, 6):
                    f = paso / 5
                    fp, fc = (f, f * 0.5) if orden == "productores primero" else (f * 0.5, f)
                    if orden == "productores primero": fp, fc = f, max(0, f - 0.2)
                    else: fp, fc = max(0, f - 0.2), f
                    for _ in range(2000):
                        total += 1
                        esc = nuevo if r.random() < fp else viejo
                        lec = nuevo if r.random() < fc else viejo
                        try:
                            for mx in (True, False): leer(lec, instancia(esc, mx), estricto)
                        except Exception: falla += 1
                rows.append((nombre, "estricto" if estricto else "tolerante", orden, falla, total))
    return rows


def e332_enum():
    r = random.Random(3322)
    N = 10_000
    estados = ["recibida", "calificada", "devuelta"]
    msgs = []
    for i in range(N):
        e = r.choice(estados)
        if i >= N // 2 and r.random() < 0.06: e = "revision_pendiente"
        msgs.append((i, e))
    nuevos = sum(1 for _, e in msgs if e == "revision_pendiente")
    out = []
    # 1 romper: una excepción detiene la partición hasta intervención humana
    primero = next(i for i, e in msgs if e == "revision_pendiente")
    out.append(("lanzar excepción y reintentar sin fin", N - primero, 0, nuevos))
    out.append(("descartar el valor desconocido", 0, nuevos, nuevos))
    out.append(("sustituir por «desconocido»", 0, 0, nuevos))
    out.append(("conservar el valor y enviarlo a revisión", 0, 0, nuevos))
    return N, nuevos, primero, out


# ------------------------------------------------------------------ 333
def e333_registros():
    r = random.Random(3331)
    N = 5000
    recs = []
    for i in range(N):
        x = r.random()
        if x < 0.70: nota = f"{r.randint(10, 70) / 10:.1f}".replace(".", ",")
        elif x < 0.85: nota = f"{r.randint(10, 70) / 10:.1f}"
        elif x < 0.93: nota = str(r.randint(10, 100))
        elif x < 0.97: nota = "N/P"
        else: nota = ""
        f = r.random()
        fecha = ("%02d/%02d/2026" % (r.randint(1, 28), r.randint(1, 12))) if f < 0.5 else ("2026-%02d-%02d" % (r.randint(1, 12), r.randint(1, 28)))
        recs.append({"cod_alumno": f"A-{r.randint(1, 800):06d}", "nota": nota, "fecha": fecha, "estado": r.choice("ERCXVPD")})
    # adaptador ingenuo
    acept = rota = fuera = 0
    for rec in recs:
        try:
            v = float(rec["nota"])
            acept += 1
            if not 1.0 <= v <= 7.0: fuera += 1
        except ValueError:
            rota += 1
    # ACL
    ok = norm = cuarentena = 0
    motivos = {}
    for rec in recs:
        n = rec["nota"]
        if n in ("", "N/P"):
            cuarentena += 1; motivos[n or "vacía"] = motivos.get(n or "vacía", 0) + 1; continue
        v = float(n.replace(",", "."))
        if "," not in n and "." not in n and v > 7:
            # escala 0-100 → 1-7
            v = round(1 + 6 * v / 100, 1); norm += 1
        elif "," in n:
            norm += 1
        if not 1.0 <= v <= 7.0:
            cuarentena += 1; motivos["fuera de rango"] = motivos.get("fuera de rango", 0) + 1; continue
        ok += 1
    # fechas
    fechas_amb = sum(1 for x in recs if "/" in x["fecha"] and int(x["fecha"][:2]) <= 12)
    return {"N": N, "naive_acept": acept, "naive_rota": rota, "naive_fuera": fuera, "acl_ok": ok, "acl_norm": norm,
            "acl_cuar": cuarentena, "motivos": motivos, "fechas_amb": fechas_amb}


def e333_cambio():
    """Seis funciones que usan el nombre externo y las mismas seis detrás de una capa que traduce."""
    ext = '{"cod_alumno": "A-000001", "nota": "6,5", "estado": "E"}'
    renombrado = '{"alumno_id": "A-000001", "nota": "6,5", "estado": "E"}'

    def num(texto): return float(texto.replace(",", "."))
    sin_acl = {
        "boletin": lambda r: r["cod_alumno"] + ":" + r["nota"],
        "alertas": lambda r: r["estado"] == "E" and r["cod_alumno"],
        "exportar": lambda r: {"id": r["cod_alumno"]},
        "auditar": lambda r: ("A", r["cod_alumno"]),
        "promedio": lambda rs: sum(num(r["nota"]) for r in rs if r["cod_alumno"]),
        "informe": lambda rs: sorted({r["cod_alumno"] for r in rs}),
    }

    def traducir(r):
        return {"estudiante_id": r["cod_alumno"], "nota": num(r["nota"]), "estado": r["estado"]}
    con_acl = {
        "boletin": lambda d: d["estudiante_id"],
        "alertas": lambda d: d["estado"] == "E" and d["estudiante_id"],
        "exportar": lambda d: {"id": d["estudiante_id"]},
        "auditar": lambda d: ("A", d["estudiante_id"]),
        "promedio": lambda ds: sum(d["nota"] for d in ds if d["estudiante_id"]),
        "informe": lambda ds: sorted({d["estudiante_id"] for d in ds}),
    }
    unitarias = ("boletin", "alertas", "exportar", "auditar")

    def probar(funciones, payload, usa_acl):
        r = json.loads(payload)
        fallos = []
        if usa_acl:
            try: r = traducir(r)
            except KeyError:
                return ["acl"]
        for nombre, f in funciones.items():
            try: f(r if nombre in unitarias else [r])
            except Exception: fallos.append(nombre)
        return fallos
    return {"sin_ok": probar(sin_acl, ext, False), "sin_ren": probar(sin_acl, renombrado, False),
            "con_ok": probar(con_acl, ext, True), "con_ren": probar(con_acl, renombrado, True)}


def e333_fidelidad():
    r = random.Random(3333)
    N = 5000
    ext_estados = ["E", "R", "C", "X", "V", "P", "D", "A", "N"]
    mapa = {"E": "entregada", "R": "entregada", "C": "calificada", "X": "calificada", "V": "calificada",
            "P": "pendiente", "D": "pendiente", "A": "anulada", "N": "anulada"}
    inv = {"entregada": "E", "calificada": "C", "pendiente": "P", "anulada": "A"}
    recs = [(r.choice(ext_estados), r.randint(0, 100)) for _ in range(N)]
    alt_estado = sum(1 for e, _ in recs if inv[mapa[e]] != e)
    # nota 0-100 -> 1.0-7.0 con un decimal -> 0-100
    def a_dom(n): return round(1 + 6 * n / 100, 1)
    def a_ext(v): return round((v - 1) * 100 / 6)
    alt_nota = sum(1 for _, n in recs if a_ext(a_dom(n)) != n)
    alt_nota_2 = 0
    def a_dom2(n): return round(1 + 6 * n / 100, 3)
    alt_nota_2 = sum(1 for _, n in recs if round((a_dom2(n) - 1) * 100 / 6) != n)
    alt_ambas = sum(1 for e, n in recs if inv[mapa[e]] != e or a_ext(a_dom(n)) != n)
    return {"N": N, "estado": alt_estado, "nota1": alt_nota, "nota3": alt_nota_2, "ambas": alt_ambas}


# ------------------------------------------------------------------ 334
def e334_correlacion():
    N = 10_000
    rows = []
    for d in (0.0, 0.01, 0.05, 0.20):
        r = random.Random(3341)
        completos = 0
        for _ in range(N):
            if all(r.random() >= d for _ in range(3)): completos += 1  # tres saltos que deben propagar
        rows.append((d, completos, round(completos / N * 100, 1), round((1 - d) ** 3 * 100, 1)))
    # reconstrucción heurística por estudiante y ventana de 2 s
    heur = []
    for rate in (1, 10, 50):
        r = random.Random(3342)
        n = 2000
        reqs = []
        t = 0.0
        for i in range(n):
            t += r.expovariate(rate)
            reqs.append((t, r.randrange(80), i))
        # cada solicitud produce el evento posterior a t+0.5..1.5 s
        evs = [(t + r.uniform(0.5, 1.5), est, i) for t, est, i in reqs]
        buenos = 0
        for te, est, i in evs:
            cand = [q for q in reqs if q[0] < te and te - q[0] <= 2.0 and q[1] == est]
            if cand and min(cand, key=lambda q: abs(te - 1.0 - q[0]))[2] == i: buenos += 1
        heur.append((rate, buenos, round(buenos / n * 100, 1)))
    return rows, heur


def e334_senales():
    T = 600
    arr = 1.0
    modos = {}

    def simula(modo):
        depth = 0.0
        procesado = []
        errores = []
        edades = []
        cola = []  # tiempos de llegada
        llegada_k = 0.0
        fallo_desde = 100
        for t in range(T):
            llega = 1 if not (modo == "productor parado" and t >= fallo_desde) else 0
            if llega: cola.append(t)
            cap = 1
            hecho = 0; err = 0
            if t >= fallo_desde:
                if modo == "consumidor lento": cap = 0.5
                if modo == "consumidor colgado": cap = 0
            for _ in range(int(cap)) if cap >= 1 else []:
                pass
            # procesamiento
            if modo == "mensaje venenoso" and t >= fallo_desde:
                err = 1; hecho = 0  # reintenta siempre el mismo
            elif cap >= 1 and cola:
                cola.pop(0); hecho = 1
            elif 0 < cap < 1 and t % 2 == 0 and cola:
                cola.pop(0); hecho = 1
            procesado.append(hecho); errores.append(err)
            depth_t = len(cola)
            edad = (t - cola[0]) if cola else 0
            edades.append((depth_t, edad))
        return procesado, errores, edades
    umbrales = {"profundidad > 50": lambda p, e, d, t: d[t][0] > 50,
                "edad del más viejo > 60 s": lambda p, e, d, t: d[t][1] > 60,
                "procesados en 30 s < 5": lambda p, e, d, t: t >= 30 and sum(p[t - 29:t + 1]) < 5,
                "errores en 30 s > 10": lambda p, e, d, t: t >= 30 and sum(e[t - 29:t + 1]) > 10}
    res = {}
    for modo in ("consumidor lento", "consumidor colgado", "mensaje venenoso", "productor parado"):
        p, e, d = simula(modo)
        fila = {}
        for nom, f in umbrales.items():
            primero = next((t for t in range(T) if f(p, e, d, t)), None)
            fila[nom] = None if primero is None else primero - 100
        res[modo] = fila
    return res


def e334_fugas():
    r = random.Random(3343)
    N = 2000
    msgs = []
    for i in range(N):
        est = f"alumno{i}"
        msgs.append({"entrega": i, "correo": f"{est}@ejemplo.test", "token": "tok_" + "".join(r.choice("0123456789abcdef") for _ in range(16)),
                     "nota": round(r.uniform(1, 7), 1), "comentario": f"contacto: {est} [arroba] ejemplo.test" if i % 10 == 0 else "ok"})
    pii = [m["correo"] for m in msgs]
    toks = [m["token"] for m in msgs]
    def log_full(m): return json.dumps(m)
    def log_allow(m): return json.dumps({k: m[k] for k in ("entrega", "nota")})
    def log_regex(m):
        s = json.dumps(m)
        s = re.sub(r"[\w.]+@[\w.]+", "[correo]", s)
        return s
    def log_regex2(m):
        s = log_regex(m)
        return re.sub(r"tok_[0-9a-f]+", "[token]", s)
    res = []
    for nom, f in (("registrar todo el cuerpo", log_full), ("sustituir correos con una expresión regular", log_regex),
                   ("correos y tokens con expresiones regulares", log_regex2), ("registrar solo campos permitidos", log_allow)):
        logs = [f(m) for m in msgs]
        txt = "\n".join(logs)
        c = sum(1 for x in pii if x in txt)
        t = sum(1 for x in toks if x in txt)
        ref = sum(1 for m in msgs if m["comentario"] != "ok" and m["correo"].split("@")[0] in f(m))
        res.append((nom, c, t, ref))
    return res


# ------------------------------------------------------------------ 335
def _db():
    con = sqlite3.connect(":memory:", isolation_level=None)
    con.execute("create table efecto(msg_id int, entrega int, intento int)")
    return con


def e335_causas():
    N = 2000
    causas = {}
    # causa 1: caída antes de acusar
    r = random.Random(3351)
    c1 = sum(1 for _ in range(N) if r.random() < 0.05)
    # causa 2: ack perdido
    r = random.Random(3352)
    c2 = sum(1 for _ in range(N) if r.random() < 0.05)
    # causa 3: el productor reintenta tras timeout -> nuevo mensaje con mismo contenido
    r = random.Random(3353)
    c3 = sum(1 for _ in range(N) if r.random() < 0.05)
    # causa 4: visibilidad 30 s < tiempo de proceso (lognormal)
    r = random.Random(3354)
    c4 = sum(1 for _ in range(N) if r.lognormvariate(2.8, 0.7) > 30)
    # causa 5: reinicio de offsets sobre 200 mensajes
    c5 = 200
    return [c1, c2, c3, c4, c5]


def e335_defensas():
    N = 2000
    nombres = ["caída antes de acusar", "acuse perdido", "reintento del productor", "visibilidad menor que el proceso", "reinicio de offsets"]
    base = e335_causas()
    defensas = ["ninguna", "clave del mensaje", "clave de negocio", "actualización condicionada", "operación naturalmente idempotente"]
    res = {d: [] for d in defensas}
    for ci, cnt in enumerate(base):
        r = random.Random(3355 + ci)
        ids = r.sample(range(N), cnt)
        for d in defensas:
            con = _db()
            con.execute("create table vistos(msg_id int primary key)")
            con.execute("create unique index un on efecto(entrega, intento)" if d == "clave de negocio" else "select 1")
            con.execute("create table estado(entrega int primary key, v int)")
            cont = 0
            def aplicar(msg_id, entrega, intento):
                if d == "ninguna":
                    con.execute("insert into efecto values(?,?,?)", (msg_id, entrega, intento))
                elif d == "clave del mensaje":
                    cur = con.execute("insert or ignore into vistos values(?)", (msg_id,))
                    if cur.rowcount: con.execute("insert into efecto values(?,?,?)", (msg_id, entrega, intento))
                elif d == "clave de negocio":
                    con.execute("insert or ignore into efecto values(?,?,?)", (msg_id, entrega, intento))
                elif d == "actualización condicionada":
                    # un registro de calificación por entrega con versión: solo sube
                    con.execute("insert into estado values(?,?) on conflict(entrega) do update set v=excluded.v where excluded.v>estado.v", (entrega, intento))
                else:
                    con.execute("insert or replace into estado values(?,?)", (entrega, intento))
            for m in range(N):
                aplicar(m, m, 1)
            for m in ids:
                if ci == 2:  # nuevo identificador de mensaje, mismo contenido
                    aplicar(N + m, m, 1)
                else:
                    aplicar(m, m, 1)
            if d in ("ninguna", "clave del mensaje", "clave de negocio"):
                tot = con.execute("select count(*) from efecto").fetchone()[0]
            else:
                tot = con.execute("select count(*) from estado").fetchone()[0]
            res[d].append(tot - N)
    return nombres, base, res


def e335_orden_y_clave():
    N = 2000
    out = []
    for orden in ("clave y luego efecto (dos transacciones)", "efecto y luego clave (dos transacciones)", "una sola transacción"):
        r = random.Random(3356)
        con = _db()
        con.execute("create table vistos(msg_id int primary key)")
        perdidos = dup = 0
        # primera entrega con caída posible entre los dos pasos; luego redelivery si no se acusó
        for m in range(N):
            caer = r.random() < 0.05
            if orden.startswith("clave"):
                con.execute("insert or ignore into vistos values(?)", (m,))
                if caer:
                    pass  # cae antes del efecto; la reentrega se descarta por clave vista
                else:
                    con.execute("insert into efecto values(?,?,?)", (m, m, 1))
            elif orden.startswith("efecto"):
                con.execute("insert into efecto values(?,?,?)", (m, m, 1))
                if not caer:
                    con.execute("insert or ignore into vistos values(?)", (m,))
                # si cae, la reentrega repite el efecto porque la clave no existe
            else:
                con.execute("begin")
                if not caer:
                    con.execute("insert or ignore into vistos values(?)", (m,))
                    con.execute("insert into efecto values(?,?,?)", (m, m, 1))
                    con.execute("commit")
                else:
                    con.execute("rollback")
            # reentrega tras la caída
            if caer:
                cur = con.execute("select 1 from vistos where msg_id=?", (m,)).fetchone()
                if not cur:
                    con.execute("begin"); con.execute("insert or ignore into vistos values(?)", (m,)); con.execute("insert into efecto values(?,?,?)", (m, m, 1)); con.execute("commit")
        tot = con.execute("select count(*) from efecto").fetchone()[0]
        dist = con.execute("select count(distinct msg_id) from efecto").fetchone()[0]
        out.append((orden, N - dist, tot - dist))
    # alcance de la clave: 300 estudiantes con 1 a 3 intentos legítimos distintos y 100 duplicados reales
    r = random.Random(3357)
    legit = [(e, k) for e in range(300) for k in range(1, r.choice((1, 2, 3)) + 1)]
    flujo = legit + r.sample(legit, 100)
    r.shuffle(flujo)
    def correr(clave):
        vistos, aceptados = set(), []
        for e, k in flujo:
            c = clave(e, k)
            if c in vistos: continue
            vistos.add(c); aceptados.append((e, k))
        return len(legit) - len(set(aceptados)), len(aceptados) - len(set(aceptados))
    gruesa = correr(lambda e, k: e)
    fina = correr(lambda e, k: (e, k))
    return out, gruesa, fina, len(legit), len(flujo)


# ------------------------------------------------------------------ 336
SECCIONES = ["Contratos de mensaje", "Clave de idempotencia", "Política de reintentos", "Cola de mensajes fallidos",
             "Compatibilidad de esquemas", "Outbox e inbox", "Observabilidad", "Seguridad", "Límites"]


def paquete():
    return {
        "Contratos de mensaje": "EntregaRecibida v1: id, entrega_id, estudiante_id, ocurrido_en. CalificacionPublicada v1.",
        "Clave de idempotencia": "Clave: entrega_id + intento. Ventana de deduplicación: 7200 s.",
        "Política de reintentos": "max_intentos: 5. espera_s: 1,5,30,120,600. jitter: 0.5. horizonte_s: 756.",
        "Cola de mensajes fallidos": "DLQ: entregas_fallidas. Alarma si profundidad > 0. Reproceso manual con aprobación.",
        "Compatibilidad de esquemas": "Cambios solo compatibles hacia atrás y hacia adelante. Campos nuevos opcionales.",
        "Outbox e inbox": "Outbox transaccional con relevo. Inbox con clave única por mensaje.",
        "Observabilidad": "Métricas: profundidad, edad del más viejo, tasa de errores. correlación: sí.",
        "Seguridad": "Firma HMAC con marca de tiempo; tolerancia 300 s. Sin datos personales en registros.",
        "Límites": "No se midió un corredor real ni carga de producción.",
    }


def validar(pq):
    fallos = []
    for s in SECCIONES:
        if s not in pq or len(pq[s].strip()) < 20: fallos.append(f"sección ausente o vacía: {s}")
    t = pq.get("Política de reintentos", "")
    m = re.search(r"max_intentos:\s*(\d+)", t)
    esp = re.search(r"espera_s:\s*([\d,]+)", t)
    hor = re.search(r"horizonte_s:\s*(\d+)", t)
    if not m or int(m.group(1)) < 1: fallos.append("max_intentos inválido")
    if esp and m and len(esp.group(1).split(",")) != int(m.group(1)): fallos.append("espera_s no coincide con max_intentos")
    ventana = re.search(r"Ventana de deduplicación:\s*(\d+)", pq.get("Clave de idempotencia", ""))
    if esp and ventana:
        suma = sum(int(x) for x in esp.group(1).split(","))
        if int(ventana.group(1)) < suma: fallos.append("la ventana de deduplicación es menor que el horizonte de reintentos")
    elif not ventana: fallos.append("falta la ventana de deduplicación")
    if "DLQ" not in pq.get("Cola de mensajes fallidos", ""): fallos.append("sin DLQ")
    if "HMAC" not in pq.get("Seguridad", ""): fallos.append("sin firma")
    if "No se midió" not in pq.get("Límites", ""): fallos.append("límites sin declarar")
    if "única" not in pq.get("Outbox e inbox", ""): fallos.append("inbox sin clave única")
    return fallos


def e336_validador():
    base = paquete()
    assert validar(base) == []
    r = random.Random(3361)
    muts = []
    # 100 estructurales
    for i in range(100):
        pq = dict(base)
        s = r.choice(SECCIONES)
        if r.random() < 0.5: del pq[s]
        else: pq[s] = ""
        muts.append(("estructural", s, pq))
    # 100 semánticas que dejan la forma intacta
    tipos = ["ventana corta", "max_intentos 0", "espera mal contada", "sin firma pero con la palabra", "inbox no único",
             "reintentos sin jitter", "horizonte incoherente", "DLQ sin alarma", "clave demasiado gruesa", "retención de datos personales"]
    for i in range(100):
        t = tipos[i % len(tipos)]
        pq = dict(base)
        if t == "ventana corta": pq["Clave de idempotencia"] = "Clave: entrega_id + intento. Ventana de deduplicación: 60 s."
        elif t == "max_intentos 0": pq["Política de reintentos"] = "max_intentos: 0. espera_s: 1,5,30,120,600. jitter: 0.5. horizonte_s: 756."
        elif t == "espera mal contada": pq["Política de reintentos"] = "max_intentos: 5. espera_s: 1,5,30. jitter: 0.5. horizonte_s: 36."
        elif t == "sin firma pero con la palabra": pq["Seguridad"] = "No usamos HMAC porque la red es interna. Sin datos personales en registros."
        elif t == "inbox no único": pq["Outbox e inbox"] = "Outbox transaccional con relevo. Inbox sin restricción."
        elif t == "reintentos sin jitter": pq["Política de reintentos"] = "max_intentos: 5. espera_s: 1,5,30,120,600. jitter: 0. horizonte_s: 756."
        elif t == "horizonte incoherente": pq["Política de reintentos"] = "max_intentos: 5. espera_s: 1,5,30,120,600. jitter: 0.5. horizonte_s: 99999."
        elif t == "DLQ sin alarma": pq["Cola de mensajes fallidos"] = "DLQ: entregas_fallidas. Sin alarma ni dueño."
        elif t == "clave demasiado gruesa": pq["Clave de idempotencia"] = "Clave: estudiante_id. Ventana de deduplicación: 7200 s."
        elif t == "retención de datos personales": pq["Observabilidad"] = "Métricas: profundidad. Registrar el cuerpo completo con el correo del estudiante."
        muts.append(("semántica", t, pq))
    det = {"estructural": 0, "semántica": 0}
    por_tipo = {}
    for cat, nom, pq in muts:
        f = validar(pq)
        d = bool(f)
        det[cat] += d
        if cat == "semántica":
            a = por_tipo.setdefault(nom, [0, 0]); a[0] += d; a[1] += 1
    return det, por_tipo


def e336_flujo():
    N = 3000

    def simula(tolerante):
        r = random.Random(3362)
        con = sqlite3.connect(":memory:", isolation_level=None)
        con.executescript("""create table entrega(id int primary key, estado text, v int);
            create table outbox(id integer primary key autoincrement, entrega int, v int, publicado int default 0);
            create table inbox(msg text primary key);
            create table nota(entrega int, v int);
            create table aviso(entrega int);
            create table dlq(msg text);""")
        broker = []
        # API + outbox (o publicación directa)
        for i in range(N):
            if tolerante:
                con.execute("begin")
                con.execute("insert into entrega values(?,?,?)", (i, "recibida", 1))
                con.execute("insert into outbox(entrega,v) values(?,1)", (i,))
                con.execute("commit")
            else:
                con.execute("insert into entrega values(?,?,?)", (i, "recibida", 1))
                if r.random() >= 0.02:  # caída entre commit y publicación
                    broker.append((f"m{i}", i, 1))
        if tolerante:
            # relevo: publica, la caída ocurre antes de marcar
            for row in con.execute("select id,entrega,v from outbox").fetchall():
                broker.append((f"m{row[1]}", row[1], row[2]))
                if r.random() < 0.02:
                    broker.append((f"m{row[1]}", row[1], row[2]))  # se vuelve a publicar tras reiniciar
        # el corredor duplica 3 % y reordena
        extra = []
        for m in broker:
            if r.random() < 0.03: extra.append(m)
        broker += extra
        arr = sorted(((i + r.uniform(0, 5), m) for i, m in enumerate(broker)), key=lambda x: x[0])
        msgs = [m for _, m in arr]
        envenenados = set(r.sample(range(N), 15))
        notificador_caido = range(len(msgs) // 3, len(msgs) // 3 + len(msgs) // 10)
        bloqueado_en = None
        for pos, (mid, ent, v) in enumerate(msgs):
            # consumidor
            if ent in envenenados:
                if tolerante:
                    con.execute("insert into dlq values(?)", (mid,)); continue
                else:
                    bloqueado_en = pos if bloqueado_en is None else bloqueado_en
                    continue
            # caída del consumidor antes de acusar: reentrega inmediata
            veces = 2 if r.random() < 0.03 else 1
            for _ in range(veces):
                if tolerante:
                    cur = con.execute("insert or ignore into inbox values(?)", (mid,))
                    if not cur.rowcount: continue
                con.execute("insert into nota values(?,?)", (ent, v))
                if pos not in notificador_caido: con.execute("insert into aviso values(?)", (ent,))
                elif tolerante:
                    pass  # reintento posterior cubre el aviso
        if tolerante:
            # reintentos del notificador: los que no tienen aviso reciben uno, una sola vez
            con.execute("insert into aviso select distinct entrega from nota where entrega not in (select entrega from aviso)")
        notas = con.execute("select entrega,count(*) c from nota group by entrega").fetchall()
        avisos = dict(con.execute("select entrega,count(*) from aviso group by entrega").fetchall())
        sin_nota = N - len(notas) - len(envenenados) if tolerante else N - len(notas)
        dobles = sum(1 for _, c in notas if c > 1)
        sin_aviso = sum(1 for e, _ in notas if e not in avisos)
        aviso_doble = sum(1 for c in avisos.values() if c > 1)
        return {"sin_nota": sin_nota, "dobles": dobles, "sin_aviso": sin_aviso, "aviso_doble": aviso_doble,
                "envenenados_en_dlq": con.execute("select count(*) from dlq").fetchone()[0],
                "bloqueo": bloqueado_en, "total": len(msgs), "detras": (len(msgs) - bloqueado_en) if bloqueado_en is not None else 0}
    return simula(False), simula(True)


def e336_tormenta():
    N = 600
    rows = []
    for nombre, esq, jit in (("espera fija de 30 s, 8 intentos", [30] * 8, False),
                             ("exponencial 10, 20, 40... s, sin jitter", [10 * 2 ** i for i in range(6)], False),
                             ("exponencial 10, 20, 40... s, con jitter completo", [10 * 2 ** i for i in range(6)], True)):
        rr = random.Random(3364)
        cont = {}
        for _ in range(N):
            t = 0.0
            for d in esq:
                t += rr.uniform(0, d) if jit else d
                cont[int(t)] = cont.get(int(t), 0) + 1
        rows.append((nombre, sum(cont.values()), max(cont.values()), len(cont)))
    return rows


if __name__ == "__main__":
    print("platform", sys.version.split()[0], sqlite3.sqlite_version)
    for fn in (e331_sondeo, e331_firma, e331_transporte_real, e331_reintentos, e332_matriz, e332_despliegue, e332_enum,
               e333_registros, e333_cambio, e333_fidelidad, e334_correlacion, e334_senales, e334_fugas,
               e335_causas, e335_defensas, e335_orden_y_clave, e336_validador, e336_flujo, e336_tormenta):
        print(fn.__name__, json.dumps(fn(), ensure_ascii=False, default=str))
