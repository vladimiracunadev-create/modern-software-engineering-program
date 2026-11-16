"""Experimentos de SE-385 a SE-390 (datos sintéticos, semilla fija, solo biblioteca estándar).

Uso: python scripts/experiments_part32_a.py   (imprime una línea JSON por experimento)

Todo lo que ataca es código de juguete escrito aquí, en memoria y sin red. Ninguna cadena
generada es una credencial real. Las lecturas de reloj (e386_hash) cambian en cada ejecución.
"""
import hashlib
import heapq
import hmac
import json
import math
import random
import re
import secrets
import sqlite3
import sys
import time
import unicodedata
from html import escape
from urllib.parse import quote, unquote

sys.stdout.reconfigure(encoding="utf-8")


# ----------------------------------------------------------------- SE-385
def e385_grafo():
    edges = [
        ("internet", "cuenta_estudiante", 4, "robo de credenciales"),
        ("internet", "cuenta_docente", 6, "phishing dirigido"),
        ("internet", "token_servicio", 7, "token en repositorio público"),
        ("internet", "inyeccion_sql", 5, "consulta armada con texto"),
        ("cuenta_estudiante", "rol_elevado", 3, "campo rol aceptado en el registro"),
        ("cuenta_estudiante", "nota_ajena", 2, "identificador adivinable"),
        ("nota_ajena", "alterar_nota", 5, "escritura sin comprobar dueño"),
        ("rol_elevado", "alterar_nota", 1, "rol docente"),
        ("cuenta_docente", "alterar_nota", 1, "rol docente"),
        ("token_servicio", "alterar_nota", 1, "token con permiso de escritura"),
        ("inyeccion_sql", "bd_directa", 2, "lectura de la tabla de sesiones"),
        ("bd_directa", "alterar_nota", 1, "escritura directa"),
    ]

    def dijkstra(es):
        g = {}
        for a, b, c, _ in es:
            g.setdefault(a, []).append((b, c))
        dist = {"internet": 0}
        prev = {}
        pq = [(0, "internet")]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist.get(u, 1e9):
                continue
            for v, c in g.get(u, []):
                if d + c < dist.get(v, 1e9):
                    dist[v] = d + c
                    prev[v] = u
                    heapq.heappush(pq, (d + c, v))
        path, n = [], "alterar_nota"
        while n in prev:
            path.append(n)
            n = prev[n]
        path.append("internet")
        return dist.get("alterar_nota", None), path[::-1]

    def con_control(es, nodo_a, nodo_b, extra):
        return [(a, b, c + extra if (a, b) == (nodo_a, nodo_b) else c, t) for a, b, c, t in es]

    base, ruta0 = dijkstra(edges)
    # estrategia A: arreglar lo que parece más grave (la inyección SQL) y luego lo siguiente por orden de lista
    ea = con_control(edges, "internet", "inyeccion_sql", 20)
    a1, ra1 = dijkstra(ea)
    # estrategia B: bloquear el camino más barato cada vez (subir a +20 la primera arista del camino más barato)
    eb, trace_b = list(edges), []
    for _ in range(4):
        d, r = dijkstra(eb)
        trace_b.append((d, r))
        eb = con_control(eb, r[0], r[1], 20)
    d_final, r_final = dijkstra(eb)
    trace_b.append((d_final, r_final))
    # rutas con coste <= 10
    def rutas(es, limite):
        g = {}
        for a, b, c, _ in es:
            g.setdefault(a, []).append((b, c))
        n = 0
        def dfs(u, cost):
            nonlocal n
            if cost > limite:
                return
            if u == "alterar_nota":
                n += 1
                return
            for v, c in g.get(u, []):
                dfs(v, cost + c)
        dfs("internet", 0)
        return n
    return {
        "base": (base, ruta0), "rutas_le10_base": rutas(edges, 10),
        "tras_arreglar_sql": (a1, ra1), "rutas_le10_sql": rutas(ea, 10),
        "estrategia_b": trace_b, "rutas_le10_b": rutas(eb, 10),
    }


def _kendall(a, b):
    n = len(a)
    c = d = 0
    for i in range(n):
        for j in range(i + 1, n):
            s = (a[i] - a[j]) * (b[i] - b[j])
            if s > 0:
                c += 1
            elif s < 0:
                d += 1
    return (c - d) / (n * (n - 1) / 2)


def e385_ruido():
    r = random.Random(3851)
    n_amenazas, reps = 30, 300
    sig = 0.9
    sol_num, tau_num, sol_cat, tau_cat = [], [], [], []
    for _ in range(reps):
        # verdad latente: tres hechos de cada amenaza
        hechos = [(r.random() < 0.35, r.random() < 0.40, r.random() < 0.50) for _ in range(n_amenazas)]
        sev = [ (2 * a + 2 * b + c) for a, b, c in hechos ]
        # impacto y probabilidad latentes
        imp = [1 + 4 * r.random() for _ in range(n_amenazas)]
        pro = [1 + 4 * r.random() for _ in range(n_amenazas)]
        pun_num, pun_cat = [], []
        for _rev in range(3):
            pn = []
            for i in range(n_amenazas):
                ii = min(5, max(1, round(imp[i] + r.gauss(0, sig))))
                pp = min(5, max(1, round(pro[i] + r.gauss(0, sig))))
                pn.append(ii * pp)
            pun_num.append(pn)
            pc = []
            for h, s in zip(hechos, sev):
                resp = [x if r.random() > 0.10 else (not x) for x in h]
                pc.append(2 * resp[0] + 2 * resp[1] + resp[2])
            pun_cat.append(pc)
        def top5(p):
            idx = sorted(range(n_amenazas), key=lambda i: (-p[i], i))
            return set(idx[:5])
        for (x, y) in ((0, 1), (0, 2), (1, 2)):
            sol_num.append(len(top5(pun_num[x]) & top5(pun_num[y])) / 5)
            tau_num.append(_kendall(pun_num[x], pun_num[y]))
            sol_cat.append(len(top5(pun_cat[x]) & top5(pun_cat[y])) / 5)
            tau_cat.append(_kendall(pun_cat[x], pun_cat[y]))
    m = lambda v: round(sum(v) / len(v), 3)
    return {"solape_top5_numerico": m(sol_num), "tau_numerico": m(tau_num), "solape_top5_categorico": m(sol_cat), "tau_categorico": m(tau_cat)}


def e385_deriva():
    r = random.Random(3852)
    cambios = 300
    dias = [int(i * 365 / cambios) for i in range(cambios)]
    frontera = [r.random() < 0.09 for _ in range(cambios)]
    detecta = [r.random() < 0.70 for _ in range(cambios)]
    fronteras = [d for d, f in zip(dias, frontera) if f]
    def expo(revisiones, gatillo):
        res = []
        for d, f, det in zip(dias, frontera, detecta):
            if not f:
                continue
            fin = 365 + 1
            for rv in revisiones:
                if rv >= d:
                    fin = min(fin, rv)
                    break
            if gatillo and det:
                fin = d
            res.append(fin - d)
        return res
    out = {}
    for nombre, rev, g in (("una_vez", [], False), ("trimestral", [90, 180, 270, 360], False), ("por_cambio", [], True), ("por_cambio_y_trimestral", [90, 180, 270, 360], True)):
        e = expo(rev, g)
        out[nombre] = {"cambios_de_frontera": len(e), "media_dias": round(sum(e) / len(e), 1), "max_dias": max(e), "sin_modelar_fin_de_ano": sum(1 for x in e if x == 366 - 0 or False)}
    out["frontera_total"] = len(fronteras)
    out["detectadas_por_regla"] = sum(1 for f, d in zip(frontera, detecta) if f and d)
    return out


# ----------------------------------------------------------------- SE-386
def e386_hash():
    pw, salt = b"correct horse battery", b"0123456789abcdef"
    res = []
    for nombre, fn in (
        ("sha256 simple", lambda: hashlib.sha256(salt + pw).digest()),
        ("pbkdf2 1 000", lambda: hashlib.pbkdf2_hmac("sha256", pw, salt, 1000)),
        ("pbkdf2 600 000", lambda: hashlib.pbkdf2_hmac("sha256", pw, salt, 600000)),
        ("scrypt n=2^14", lambda: hashlib.scrypt(pw, salt=salt, n=2 ** 14, r=8, p=1, maxmem=64 * 1024 * 1024)),
    ):
        reps = 5 if "simple" not in nombre else 20000
        t0 = time.perf_counter()
        for _ in range(reps):
            fn()
        dt = (time.perf_counter() - t0) / reps
        res.append((nombre, dt))
    usuarios, N, s = 10000, 1_000_000, 0.8
    # suma parcial de r^-s aproximada por integral (suficiente para el modelo)
    def H(g):
        g = max(1, g)
        return (g ** (1 - s) - 1) / (1 - s) + 1
    tot = H(N)
    filas = []
    for nombre, dt in res:
        presupuesto = 3600.0 / dt  # hashes en una hora de un núcleo
        g_sin_sal = presupuesto
        g_con_sal = presupuesto / usuarios
        f = lambda g: round(0.7 * H(min(N, int(g))) / tot * 100, 1)
        filas.append((nombre, round(dt * 1e3, 4), int(presupuesto), f(g_sin_sal), f(g_con_sal)))
    # conteo determinista de sal
    dic = 1000
    return {"filas": filas, "hashes_sin_sal": dic, "hashes_con_sal": dic * usuarios}


def e386_relleno():
    r = random.Random(3861)
    cuentas, ips = 5000, 2000
    pares = []  # lista del atacante: (cuenta, contraseña) una por cuenta
    reuso = set(r.sample(range(cuentas), 100))  # 2 % reutilizan la contraseña de la lista
    mfa = {i for i in range(cuentas) if r.random() < 0.30}
    expuestas = {i for i in reuso if r.random() < 0.60}  # contraseñas presentes en un corpus filtrado
    out = {}
    out["sin_defensa"] = {"comprometidas": len(reuso), "bloqueadas_legitimas": 0}
    # límite por IP: 5 intentos/hora/IP; 2 000 IPs; el atacante necesita 5 000 intentos
    horas = math.ceil(cuentas / (ips * 5))
    out["limite_por_ip"] = {"comprometidas": len(reuso), "bloqueadas_legitimas": 0, "horas_para_probar_todo": horas}
    # bloqueo por cuenta tras 5 fallos: el relleno usa 1 intento por cuenta, no se activa; el atacante 'dedicado' bloquea a todos
    out["bloqueo_por_cuenta"] = {"comprometidas": len(reuso), "bloqueadas_legitimas": 0, "si_el_atacante_falla_a_propósito": cuentas}
    out["mfa_30"] = {"comprometidas": len(reuso - mfa), "bloqueadas_legitimas": 0}
    out["rechazo_de_contraseñas_filtradas"] = {"comprometidas": len(reuso - expuestas), "bloqueadas_legitimas": 0}
    out["mfa_y_rechazo"] = {"comprometidas": len(reuso - mfa - expuestas), "bloqueadas_legitimas": 0}
    return out


def e386_sesion():
    r = random.Random(3862)
    activas = 10000
    # (1) contador secuencial dentro de un espacio de 1 000 000
    espacio = 1_000_000
    ids = set(r.sample(range(espacio), activas))
    intentos, hit = 0, 0
    while hit == 0:
        intentos += 1
        if r.randrange(espacio) in ids:
            hit = 1
    seq_intentos = intentos
    # (2) semilla por segundo de login
    t_login = 1_700_000_123
    victima = random.Random(t_login).getrandbits(64)
    ventana = 3600
    cand = 0
    recuperado = False
    for ts in range(t_login - ventana, t_login + ventana + 1):
        cand += 1
        if random.Random(ts).getrandbits(64) == victima:
            recuperado = True
            break
    # intentos hasta recuperar en orden creciente de ts
    # (3) 128 bits aleatorios del sistema
    esperados = 2 ** 128 / activas
    tok = secrets.token_hex(16)
    return {
        "secuencial_intentos_hasta_acertar": seq_intentos, "secuencial_esperados": espacio // activas,
        "semilla_por_segundo_candidatos": cand, "semilla_recuperada": recuperado, "ventana_candidatos": 2 * ventana + 1,
        "aleatorio_128_esperados_e": f"{esperados:.2e}", "largo_token_hex": len(tok),
    }


# ----------------------------------------------------------------- SE-387
ACCIONES = ["submit", "view_submission", "list_submissions", "view_grade", "set_grade", "delete_submission", "export_course"]
ROLES = ["estudiante", "docente", "ayudante", "coordinador", "admin", "servicio"]
RELS = ["owner", "in_course", "other_course_same_program", "other_course", "missing"]
ESTADOS = ["normal", "unpublished", "revoked", "past_deadline"]


def decide(role, action, rel, state, override, m=frozenset()):
    if action not in ACCIONES:
        return "M9" in m
    if override and "M5" in m:
        role = override
    if rel == "missing" and "M13" not in m:
        return False
    if state == "revoked" and "M7" not in m:
        return False
    staff_ok = rel == "in_course" or ("M3" in m and rel in ("other_course_same_program", "other_course"))
    if role == "estudiante":
        if action == "submit":
            return rel in ("owner", "in_course") and (state != "past_deadline" or "M10" in m)
        if action == "view_submission":
            return rel == "owner" or ("M1" in m and rel == "in_course") or ("M2" in m and rel in ("in_course", "other_course_same_program"))
        if action == "view_grade":
            return rel == "owner" and (state != "unpublished" or "M6" in m)
        return False
    if role == "docente":
        if action in ("view_submission", "list_submissions", "set_grade", "export_course"):
            return staff_ok
        return False
    if role == "ayudante":
        if action in ("view_submission", "list_submissions"):
            return staff_ok
        if action == "set_grade":
            return "M4" in m and staff_ok
        return False
    if role == "coordinador":
        if action in ("list_submissions", "export_course"):
            return rel in ("in_course", "other_course_same_program") or ("M8" in m and rel == "other_course")
        return False
    if role == "admin":
        if action in ("delete_submission", "export_course"):
            return True
        return "M11" in m and action == "set_grade"
    if role == "servicio":
        return action == "export_course" or ("M12" in m and action == "list_submissions")
    return "M9" in m


MUTANTES = {
    "M1": "el estudiante ve las entregas de quien comparte curso",
    "M2": "el estudiante ve entregas de su programa",
    "M3": "el docente actúa sobre cualquier curso",
    "M4": "el ayudante puede calificar",
    "M5": "se confía en el rol que declara el cliente",
    "M6": "se ve la nota antes de publicarla",
    "M7": "la pertenencia revocada sigue valiendo",
    "M8": "el coordinador actúa fuera de su programa",
    "M9": "acción desconocida permitida por defecto",
    "M10": "se entrega después del plazo",
    "M11": "el administrador califica",
    "M12": "el servicio lista entregas",
    "M13": "un recurso inexistente se autoriza",
}


def e387_matriz():
    universo = [(ro, a, re_, es, ov) for ro in ROLES for a in ACCIONES for re_ in RELS for es in ESTADOS for ov in (None, "admin")]
    def ref(t):
        return decide(*t)
    felices = [t for t in universo if t[2] in ("owner", "in_course") and t[3] == "normal" and t[4] is None and ref(t)]
    por_rol = [t for t in universo if t[2] in ("owner", "in_course") and t[3] == "normal" and t[4] is None]
    completa = universo
    # variante: 'por_rol' + relaciones, sin estado ni override
    por_relacion = [t for t in universo if t[3] == "normal" and t[4] is None]
    suites = {"solo ruta feliz": felices, "negativas por rol (relación típica)": por_rol, "rol x relación": por_relacion, "rol x relación x estado x override": completa}
    # M9: acción desconocida
    extra = [(ro, "accion_desconocida", "in_course", "normal", None) for ro in ROLES]
    res = {}
    for nombre, suite in suites.items():
        s = suite + (extra if nombre.endswith("override") else [])
        vivos, muertos = [], []
        for mid in MUTANTES:
            killed = any(decide(*t, m=frozenset([mid])) != decide(*t) for t in s)
            (muertos if killed else vivos).append(mid)
        res[nombre] = {"pruebas": len(s), "detectados": len(muertos), "vivos": vivos}
    # un mismo mutante: ¿cuál es la prueba mínima que lo mata?
    return {"suites": res, "mutantes": len(MUTANTES)}


def e387_idor():
    r = random.Random(3871)
    total_ids, entregas = 20000, 5000
    ids_seq = set(r.sample(range(1, total_ids + 1), entregas))
    propias = set(list(ids_seq)[:12])
    filtrados = set(r.sample(sorted(ids_seq), 150))  # 3 % aparecen en listados, correos o registros públicos
    out = {}
    # secuencial sin control: el atacante recorre 1..20 000
    hits = sum(1 for i in range(1, total_ids + 1) if i in ids_seq and i not in propias)
    out["secuencial_sin_control"] = {"peticiones": total_ids, "ajenas_leidas": hits}
    out["aleatorio_sin_control_adivinando"] = {"peticiones": 1_000_000, "ajenas_leidas": 0}
    out["aleatorio_sin_control_con_ids_filtrados"] = {"peticiones": len(filtrados), "ajenas_leidas": len(filtrados)}
    out["secuencial_con_control"] = {"peticiones": total_ids, "ajenas_leidas": 0}
    out["aleatorio_con_control"] = {"peticiones": 1_000_000, "ajenas_leidas": 0}
    return out


def e387_deriva():
    r = random.Random(3872)
    usuarios, meses, catalogo = 300, 24, 40
    def sim(politica):
        necesarios = [set(r2.sample(range(catalogo), 5)) for r2 in [random.Random(i) for i in range(usuarios)]]
        tiene = [set(s) for s in necesarios]
        rr = random.Random(38720 + politica)
        for mes in range(1, meses + 1):
            for u in range(usuarios):
                if rr.random() < 0.05:
                    nuevo = set(rr.sample(range(catalogo), 5))
                    necesarios[u] = nuevo
                    tiene[u] |= nuevo
                    if politica == 3:
                        tiene[u] = set(nuevo)  # al cambiar de rol se reasignan los permisos
            if politica == 1 and mes % 3 == 0:
                for u in range(usuarios):
                    sobrantes = tiene[u] - necesarios[u]
                    for p in list(sobrantes):
                        if rr.random() < 0.80:
                            tiene[u].discard(p)
            if politica == 2:
                # permisos con caducidad de 30 días: se renuevan solo los necesarios
                for u in range(usuarios):
                    tiene[u] = set(necesarios[u])
        total = sum(len(t) for t in tiene)
        sobr = sum(len(t - n) for t, n in zip(tiene, necesarios))
        return round(total / usuarios, 1), round(sobr / usuarios, 1), round(100 * sobr / total, 1)
    return {"acumular": sim(0), "revision_trimestral": sim(1), "caducidad_30_dias": sim(2), "reasignar_al_cambiar_de_rol": sim(3)}


# ----------------------------------------------------------------- SE-388
def _db():
    c = sqlite3.connect(":memory:")
    c.executescript("""
    CREATE TABLE usuarios(id INTEGER PRIMARY KEY, email TEXT, clave TEXT, rol TEXT);
    CREATE TABLE entregas(id INTEGER PRIMARY KEY, dueno TEXT, curso TEXT, titulo TEXT);
    INSERT INTO usuarios VALUES (1,'ana@ejemplo.test','h-ana','estudiante'),(2,'bruno@ejemplo.test','h-bruno','estudiante'),(3,'docente@ejemplo.test','h-doc','docente');
    INSERT INTO entregas VALUES (1,'ana@ejemplo.test','C1','Ensayo de Ana'),(2,'bruno@ejemplo.test','C1','Ensayo de Bruno'),(3,'bruno@ejemplo.test','C2','Borrador de Bruno'),(4,'ana@ejemplo.test','C2','Informe de Ana');
    """)
    return c


PAY_TEXTO = ["' OR '1'='1", "' OR 1=1 --", "'; DROP TABLE entregas; --", "' UNION SELECT 1,email,clave,rol FROM usuarios --", "' UNION SELECT id,email,clave,rol FROM usuarios WHERE rol='docente' --",
             "x' OR 'a'='a", "' OR ''='", "ana@ejemplo.test'--", "' oR '1'='1", "' UnIoN sElEcT 1,email,clave,rol FROM usuarios --",
             "' UN/**/ION SELECT 1,email,clave,rol FROM usuarios --", "'||(SELECT clave FROM usuarios WHERE id=3)||'"]
PAY_NUM = ["0 OR 1=1", "1 OR 1=1", "1 UNION SELECT 1,email,clave,rol FROM usuarios", "1; DELETE FROM entregas", "0 oR 1=1", "1 UNION/**/SELECT 1,email,clave,rol FROM usuarios",
           "(SELECT id FROM usuarios WHERE rol='docente')", "id", "1 OR id>0", "9 OR 1", "-1 OR 1=1", "0 UnIoN SeLeCt 1,email,clave,rol FROM usuarios"]
PAY_IDENT = ["titulo", "titulo DESC", "id; DROP TABLE entregas", "(SELECT clave FROM usuarios LIMIT 1)", "CASE WHEN 1=1 THEN id ELSE titulo END", "titulo--", "1", "dueno,(SELECT 1/0)", "clave", "rol", "id) UNION SELECT 1", "titulo COLLATE NOCASE"]
LISTA_NEGRA = re.compile(r"\b(union|select|drop|delete)\b", re.I)


def _pregunta(contexto, defensa, carga, c):
    # devuelve (filas, error) con las filas que no corresponden a la persona 'ana' del curso C1
    try:
        if contexto == "texto":
            if defensa == "concatenar":
                q = "SELECT id,dueno,curso,titulo FROM entregas WHERE dueno='ana@ejemplo.test' AND titulo LIKE '%" + carga + "%'"  # nosec B608
                return c.execute(q).fetchall(), None
            if defensa == "duplicar_comilla":
                q = "SELECT id,dueno,curso,titulo FROM entregas WHERE dueno='ana@ejemplo.test' AND titulo LIKE '%" + carga.replace("'", "''") + "%'"  # nosec B608
                return c.execute(q).fetchall(), None
            if defensa == "lista_negra":
                if LISTA_NEGRA.search(carga):
                    return [], "rechazada"
                q = "SELECT id,dueno,curso,titulo FROM entregas WHERE dueno='ana@ejemplo.test' AND titulo LIKE '%" + carga + "%'"  # nosec B608
                return c.execute(q).fetchall(), None
            return c.execute("SELECT id,dueno,curso,titulo FROM entregas WHERE dueno=? AND titulo LIKE ?", ("ana@ejemplo.test", "%" + carga + "%")).fetchall(), None
        if contexto == "numero":
            if defensa == "concatenar":
                return c.execute("SELECT id,dueno,curso,titulo FROM entregas WHERE dueno='ana@ejemplo.test' AND id = " + carga).fetchall(), None  # nosec B608
            if defensa == "duplicar_comilla":
                return c.execute("SELECT id,dueno,curso,titulo FROM entregas WHERE dueno='ana@ejemplo.test' AND id = " + carga.replace("'", "''")).fetchall(), None  # nosec B608
            if defensa == "lista_negra":
                if LISTA_NEGRA.search(carga):
                    return [], "rechazada"
                return c.execute("SELECT id,dueno,curso,titulo FROM entregas WHERE dueno='ana@ejemplo.test' AND id = " + carga).fetchall(), None  # nosec B608
            return c.execute("SELECT id,dueno,curso,titulo FROM entregas WHERE dueno=? AND id = ?", ("ana@ejemplo.test", carga)).fetchall(), None
        # identificador (ORDER BY)
        base = "SELECT id,dueno,curso,titulo FROM entregas WHERE dueno='ana@ejemplo.test' ORDER BY "
        if defensa == "concatenar":
            return c.execute(base + carga).fetchall(), None  # nosec B608
        if defensa == "duplicar_comilla":
            return c.execute(base + carga.replace("'", "''")).fetchall(), None  # nosec B608
        if defensa == "lista_negra":
            if LISTA_NEGRA.search(carga):
                return [], "rechazada"
            return c.execute(base + carga).fetchall(), None  # nosec B608
        if defensa == "parametro":
            return c.execute(base + "?", (carga,)).fetchall(), None  # el parámetro es un valor, no un nombre
        if defensa == "lista_blanca":
            return c.execute(base + (carga if carga in ("id", "titulo", "curso") else "id")).fetchall(), None  # nosec B608
    except sqlite3.Error as e:
        return [], "error"


def e388_sql():
    res = {}
    for contexto, pays in (("texto", PAY_TEXTO), ("numero", PAY_NUM), ("identificador", PAY_IDENT)):
        defensas = ["concatenar", "duplicar_comilla", "lista_negra", "parametro"] + (["lista_blanca"] if contexto == "identificador" else [])
        for d in defensas:
            efectivos = 0
            for p in pays:
                c = _db()
                filas, err = _pregunta(contexto, d, p, c)
                n_entregas = c.execute("SELECT COUNT(*) FROM entregas").fetchone()[0] if c.execute("SELECT name FROM sqlite_master WHERE name='entregas'").fetchone() else -1
                fuga = any(f[1] != "ana@ejemplo.test" for f in filas) or (contexto == "texto" and len(filas) > 2) or (contexto == "numero" and len(filas) > 2)
                if contexto == "identificador":
                    fuga = fuga or (err is None and False)
                if err is None and (fuga or n_entregas != 4):
                    efectivos += 1
                elif contexto == "identificador" and err is None:
                    # el ORDER BY con subconsulta sí se ejecuta: cuenta si el texto del payload fue interpretado como SQL
                    if p not in ("titulo", "titulo DESC", "1", "id", "curso", "titulo COLLATE NOCASE") and d in ("concatenar", "duplicar_comilla", "lista_negra"):
                        efectivos += 1
            res[f"{contexto}/{d}"] = efectivos
    res["_payloads"] = {"texto": len(PAY_TEXTO), "numero": len(PAY_NUM), "identificador": len(PAY_IDENT)}
    c = _db()
    esperado = [f[0] for f in c.execute("SELECT id,dueno,curso,titulo FROM entregas WHERE dueno='ana@ejemplo.test' ORDER BY titulo DESC").fetchall()]  # nosec B608
    obtenido = [f[0] for f in c.execute("SELECT id,dueno,curso,titulo FROM entregas WHERE dueno='ana@ejemplo.test' ORDER BY ?", ("titulo DESC",)).fetchall()]
    res["_order_by_parametro_ordena_como_se_pide"] = esperado == obtenido
    return res


def e388_codificacion():
    cargas = ["<script>x</script>", '"><img src=x>', "' onmouseover='x", "x onmouseover=x", "</script><script>x", "'-x-'", "javascript:x", "\\'; x //"]
    def rompe(ctx, s):
        if ctx == "texto_html":
            return "<" in s or "&" in s and False
        if ctx == "atributo_con_comillas":
            return '"' in s
        if ctx == "atributo_sin_comillas":
            return any(ch in s for ch in " \t\n\"'=<>`")
        if ctx == "cadena_js":
            i = 0
            while i < len(s):
                if s[i] == "\\":
                    i += 2
                    continue
                if s[i] in "'\n" or s[i:i + 2] == "</":
                    return True
                i += 1
            return False
        if ctx == "url_href":
            return s.strip().lower().startswith(("javascript:", "data:", "vbscript:"))
    def enc_js(s):
        return json.dumps(s).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")[1:-1].replace("'", "\\u0027")
    codificadores = {
        "ninguno": lambda s: s,
        "html.escape (sin comillas)": lambda s: escape(s, quote=False),
        "html.escape (con comillas)": lambda s: escape(s, quote=True),
        "codificación para JavaScript": enc_js,
        "urllib.parse.quote": lambda s: quote(s, safe=""),
    }
    contextos = ["texto_html", "atributo_con_comillas", "atributo_sin_comillas", "cadena_js", "url_href"]
    out = {}
    for nc, f in codificadores.items():
        out[nc] = {c: sum(1 for p in cargas if rompe(c, f(p))) for c in contextos}
    out["_cargas"] = len(cargas)
    return out


def e388_orden():
    bases = ["<script>x</script>", "../../etc/passwd", "' OR 1=1 --", "javascript:x", "..\\..\\secreto", "<img src=x onerror=x>", "%2e%2e/secreto", "ſcript", "<svg onload=x>", "; cat /etc/passwd", "../clave", "$(x)"]
    def variantes(s):
        yield s
        yield quote(s, safe="")
        yield quote(quote(s, safe=""), safe="")
        yield s.upper()
        yield "".join(chr(ord(c) + 0xFEE0) if 0x21 <= ord(c) <= 0x7E else c for c in s)  # ancho completo
        yield s.replace("<", "＜").replace(">", "＞").replace(".", "．").replace("/", "／")
        yield s + "\x00.png"
    cargas = [v for b in bases for v in variantes(b)]
    peligrosa = re.compile(r"(<|\.\./|\.\.\\|'|;|\$\(|javascript:|\x00)", re.I)
    lista_negra = re.compile(r"(<script|\.\./|' or|javascript:)", re.I)
    def peligrosa_final(s):
        return bool(peligrosa.search(s))
    def decodificar(s):
        return unquote(s)
    def a_validar_luego_decodificar(s):
        if lista_negra.search(s):
            return None
        return unicodedata.normalize("NFKC", decodificar(s))
    def b_decodificar_normalizar_validar(s):
        t = unicodedata.normalize("NFKC", decodificar(s))
        if lista_negra.search(t):
            return None
        return t
    def c_lista_blanca(s):
        t = unicodedata.normalize("NFKC", decodificar(s))
        if re.fullmatch(r"[A-Za-z0-9_\-]{1,40}(\.(pdf|png|txt))?", t):
            return t
        return None
    res = {}
    for nombre, f in (("validar la forma recibida y luego decodificar", a_validar_luego_decodificar), ("decodificar, normalizar y validar con lista negra", b_decodificar_normalizar_validar), ("decodificar, normalizar y validar con lista blanca", c_lista_blanca)):
        pasan = [f(c) for c in cargas]
        aceptadas = [p for p in pasan if p is not None]
        res[nombre] = {"aceptadas": len(aceptadas), "peligrosas_tras_aceptar": sum(1 for p in aceptadas if peligrosa_final(p))}
    legit = ["entrega-final.pdf", "informe_2.pdf", "Maria_Lopez.pdf", "María_López.pdf", "informe final.pdf", "ensayo-1.txt", "tarea.PNG", "Resumen (2).pdf", "datos_2026.txt", "ñandú.png"]
    for nombre, f in (("validar la forma recibida y luego decodificar", a_validar_luego_decodificar), ("decodificar, normalizar y validar con lista negra", b_decodificar_normalizar_validar), ("decodificar, normalizar y validar con lista blanca", c_lista_blanca)):
        res[nombre]["legitimos_rechazados"] = sum(1 for n in legit if f(n) is None)
    res["_total"] = len(cargas)
    res["_legitimos"] = len(legit)
    return res


# ----------------------------------------------------------------- SE-389
def _ks(key, nonce, n):
    out = b""
    c = 0
    while len(out) < n:
        out += hmac.new(key, nonce + c.to_bytes(4, "big"), hashlib.sha256).digest()
        c += 1
    return out[:n]


def _xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def e389_nonce():
    r = random.Random(3891)
    key = r.randbytes(32)
    plantilla = "Nota final: {:2d}/70. Comentario: {}"
    coments = ["buen trabajo", "falta la sección de pruebas", "revisar la bibliografía", "excelente análisis", "corregir el formato de las citas", "añadir un caso límite"]
    def sample():
        return plantilla.format(r.randint(1, 70), r.choice(coments)).encode()
    res = {}
    for modo in ("nonce fijo", "nonce único"):
        recup, total, crib_ok = 0, 0, 0
        for i in range(200):
            m1, m2 = sample(), sample()
            n = min(len(m1), len(m2))
            if modo == "nonce fijo":
                n1 = n2 = b"\x00" * 12
            else:
                n1, n2 = r.randbytes(12), r.randbytes(12)
            c1, c2 = _xor(m1, _ks(key, n1, len(m1))), _xor(m2, _ks(key, n2, len(m2)))
            # el atacante conoce m1 (su propia entrega) y obtiene m2 sin la clave
            guess = _xor(_xor(c1[:n], c2[:n]), m1[:n])
            recup += sum(1 for a, b in zip(guess, m2[:n]) if a == b)
            total += n
            # ataque sin conocer m1: prueba que la plantilla "Nota final: " aparece en ambos
            crib = b"Nota final: "
            p1_parcial = _xor(_xor(c1[:len(crib)], c2[:len(crib)]), crib)
            crib_ok += (p1_parcial == m2[:len(crib)])
        res[modo] = {"bytes_recuperados_pct": round(100 * recup / total, 1), "criba_de_plantilla_acierta": crib_ok}
    return res


def e389_comparacion():
    r = random.Random(3892)
    largo = 8
    tag = bytes(r.randrange(256) for _ in range(largo))
    def oracle_temprano(g):
        pasos = 0
        for a, b in zip(g, tag):
            pasos += 1
            if a != b:
                return False, pasos
        return True, pasos
    def oracle_constante(g):
        return g == tag, largo
    conocido = bytearray(largo)
    consultas = 0
    for pos in range(largo):
        mejor, mp = 0, -1
        for v in range(256):
            g = bytes(conocido[:pos]) + bytes([v]) + b"\x00" * (largo - pos - 1)
            ok, pasos = oracle_temprano(g)
            consultas += 1
            if pasos > mp:
                mp, mejor = pasos, v
            if ok:
                mejor = v
                break
        conocido[pos] = mejor
    ok_final, _ = oracle_temprano(bytes(conocido))
    # con oráculo constante: pasos siempre iguales: el atacante no tiene señal
    señal = len({oracle_constante(bytes([v]) + b"\x00" * 7)[1] for v in range(256)})
    return {"consultas_comparacion_temprana": consultas, "recupera": ok_final, "espacio": 2 ** (8 * largo), "valores_distintos_de_señal_constante": señal, "esperadas_fuerza_bruta_e": f"{2 ** (8 * largo - 1):.2e}"}


def e389_cumpleanos():
    r = random.Random(3893)
    filas = []
    k = 24
    espacio = 2 ** k
    for n in (500, 1000, 2000, 4000, 8000):
        emp, reps = 0, 1500
        for _ in range(reps):
            vistos = set()
            col = False
            for _ in range(n):
                v = r.randrange(espacio)
                if v in vistos:
                    col = True
                    break
                vistos.add(v)
            emp += col
        teo = 1 - math.exp(-n * (n - 1) / (2 * espacio))
        filas.append((n, round(100 * emp / reps, 1), round(100 * teo, 1)))
    n96 = math.sqrt(2 * 2.0 ** -32 * 2.0 ** 96)
    llaves = 1_000_000
    return {"filas_24_bits": filas, "n_para_2e-32_con_96_bits": f"{n96:.2e}", "limite_nist_2e32": 2 ** 32,
            "reenvoltura": {"envolver_dek_bytes": llaves * 48, "reencriptar_datos_bytes": 2 * 10 ** 12}}


# ----------------------------------------------------------------- SE-390
def e390_escaner():
    r = random.Random(3901)
    ALF = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    def rs(n, a=ALF):
        return "".join(r.choice(a) for _ in range(n))
    def secretos():
        t = r.randrange(6)
        if t == 0:
            return "clave_acceso=AKIA" + rs(16, "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"), "proveedor"
        if t == 1:
            return "token = ghp_" + rs(36), "proveedor"
        if t == 2:
            return "password = '" + rs(14) + "'", "asignacion"
        if t == 3:
            return "API_SECRET=" + rs(40, ALF + "+/"), "asignacion"
        if t == 4:
            return "-----BEGIN PRIVATE KEY-----", "proveedor"
        return "jwt = eyJ" + rs(30) + "." + rs(40) + "." + rs(43), "proveedor"
    def señuelos():
        t = r.randrange(7)
        if t == 0:
            return "commit " + rs(40, "0123456789abcdef")
        if t == 1:
            return "id = " + "-".join(rs(n, "0123456789abcdef") for n in (8, 4, 4, 4, 12))
        if t == 2:
            return "sha256: " + rs(64, "0123456789abcdef")
        if t == 3:
            return "imagen = data:image/png;base64," + rs(60, ALF + "+/")
        if t == 4:
            return "password = 'changeme'"
        if t == 5:
            return "nombre_largo = " + rs(12, "abcdefghijklmnopqrstuvwxyz") + "_" + rs(12, "abcdefghijklmnopqrstuvwxyz")
        return "ejemplo: token = ghp_" + "x" * 36
    lineas = []
    for _ in range(60):
        s, k = secretos()
        lineas.append((s, True))
    for _ in range(140):
        lineas.append((señuelos(), False))
    for _ in range(300):
        lineas.append((" ".join(rs(r.randrange(3, 9), "abcdefghijklmnopqrstuvwxyz") for _ in range(r.randrange(2, 6))), False))
    r.shuffle(lineas)
    pat = [re.compile(p) for p in (r"AKIA[A-Z2-7]{16}", r"ghp_[A-Za-z0-9]{36}", r"-----BEGIN [A-Z ]*PRIVATE KEY-----", r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")]
    kw = re.compile(r"(password|passwd|secret|token|api_key|apikey)\s*[:=]\s*['\"]?([^\s'\"]{6,})", re.I)
    def entropia(s):
        from collections import Counter
        c = Counter(s)
        return -sum(v / len(s) * math.log2(v / len(s)) for v in c.values())
    def cand(l):
        return re.findall(r"[A-Za-z0-9+/=_\-]{20,}", l)
    def regex_proveedor(l):
        return any(p.search(l) for p in pat)
    def regex_asignacion(l):
        m = kw.search(l)
        return bool(m)
    def solo_entropia(l):
        return any(entropia(c) >= 4.0 for c in cand(l))
    def combinado(l):
        if regex_proveedor(l):
            return True
        m = kw.search(l)
        if m:
            v = m.group(2)
            return entropia(v) >= 3.0 and v.lower() not in ("changeme", "password", "secret") and not v.startswith("x")
        return False
    def evalua(f):
        tp = sum(1 for l, s in lineas if s and f(l))
        fp = sum(1 for l, s in lineas if not s and f(l))
        fn = sum(1 for l, s in lineas if s and not f(l))
        prec = tp / (tp + fp) if tp + fp else 0
        rec = tp / (tp + fn)
        return {"detectados": tp, "falsas_alarmas": fp, "perdidos": fn, "precision": round(prec * 100, 1), "recall": round(rec * 100, 1)}
    return {"solo_patrones_de_proveedor": evalua(regex_proveedor), "solo_palabra_clave": evalua(regex_asignacion), "solo_entropia": evalua(solo_entropia), "patrones_y_clave_con_entropia": evalua(combinado), "_lineas": len(lineas), "_secretos": 60}


def e390_rotacion():
    def sim(estrategia, semilla):
        r = random.Random(semilla)
        inst, rps, T = 20, 100, 600
        recarga = [r.uniform(0, 300) for _ in range(inst)]
        if r.random() < 0.6:
            recarga[r.randrange(inst)] = 10 ** 9  # una instancia no recarga la configuración
        falla = tot = 0
        vigente_vieja = 0.0
        for t in range(T * rps):
            ts = t / rps
            i = r.randrange(inst)
            clave_inst = "nueva" if ts >= recarga[i] else "vieja"
            if estrategia == "corte":
                aceptadas = {"nueva"}
            elif estrategia == "cierre fijo":
                aceptadas = {"vieja", "nueva"} if ts < 360 else {"nueva"}
            else:
                pendiente = any(rr > ts for rr in recarga)
                aceptadas = {"vieja", "nueva"} if pendiente else {"nueva"}
            tot += 1
            if clave_inst not in aceptadas:
                falla += 1
            if "vieja" in aceptadas and t % rps == 0:
                vigente_vieja += 1
        return falla, tot, vigente_vieja, any(rr > T for rr in recarga)
    out = {}
    for e in ("corte", "cierre fijo", "cierre condicionado"):
        fs, vig, atasc = [], [], 0
        for s_ in range(10):
            f, t, v, a_ = sim(e, 39000 + s_)
            fs.append(f)
            vig.append(v)
            atasc += a_
        out[e] = {"fallidas_media": round(sum(fs) / 10), "total": t, "porcentaje": round(100 * sum(fs) / (10 * t), 2),
                  "segundos_con_la_clave_vieja_aceptada_media": round(sum(vig) / 10), "semillas_con_instancia_atascada": atasc}
    return out


def e390_radio():
    r = random.Random(3903)
    servicios = ["api", "worker", "reportes", "correo", "pagos"]
    amb = ["dev", "staging", "prod"]
    recursos = {(a, s, k) for a in amb for s in servicios for k in range(6)}
    prod = [x for x in recursos if x[0] == "prod"]
    def alcance(esquema, fuga):
        a, s = fuga
        if esquema == "una credencial en todos los ambientes":
            return set(recursos)
        if esquema == "una credencial por ambiente":
            return {x for x in recursos if x[0] == a}
        return {x for x in recursos if x[0] == a and x[1] == s}
    out = {}
    for esquema in ("una credencial en todos los ambientes", "una credencial por ambiente", "una credencial por servicio y ambiente"):
        n_prod, n_todo = [], []
        for _ in range(3000):
            fuga = (r.choice(amb), r.choice(servicios))
            al = alcance(esquema, fuga)
            n_prod.append(sum(1 for x in al if x[0] == "prod"))
            n_todo.append(len(al))
        out[esquema] = {"recursos_alcanzados_media": round(sum(n_todo) / 3000, 1), "de_prod_media": round(sum(n_prod) / 3000, 1), "de_total": len(recursos), "de_prod_total": len(prod)}
    return out


if __name__ == "__main__":
    for nombre, fn in sorted(globals().items()):
        if nombre.startswith("e3") and callable(fn):
            if len(sys.argv) > 1 and not any(nombre.startswith(a) for a in sys.argv[1:]):
                continue
            print(json.dumps({nombre: fn()}, ensure_ascii=False))
