"""Experimentos de las clases SE-565 a SE-570 (Parte 47): análisis de riesgo y normas de seguridad.

Uso: python scripts/experiments_part47_a.py [565|566|567|568|569|570]

No se invoca ningún modelo de lenguaje. Todo es código ejecutado con la biblioteca estándar sobre el
caso conductor *Horno de curado* (controlador de temperatura con un limitador independiente). Las
tasas de fallo, las valoraciones y los parámetros los fija el autor: son supuestos de modelo, no datos
de un producto. Ningún experimento reproduce ni sustituye el texto de una norma.
"""
from __future__ import annotations

import hashlib
import itertools
import random
import sys

import experiments_part47_lab as L
from experiments_part47_lab import fmt, sci, table


# ====================================================================== SE-565
GATES = {
    "TOPE": ("and", ["PIERDE_CONTROL", "PIERDE_PROTECCION"]),
    "PIERDE_CONTROL": ("or", ["SENSOR_BAJO", "FALLO_SW", "TRIAC_CORTO"]),
    "PIERDE_PROTECCION": ("or", ["RELE_SOLDADO", "SENSOR_LIMITADOR", "LOGICA_LIMITADOR"]),
}
P = {"SENSOR_BAJO": 2e-3, "FALLO_SW": 5e-3, "TRIAC_CORTO": 1e-3,
     "RELE_SOLDADO": 1e-4, "SENSOR_LIMITADOR": 2e-3, "LOGICA_LIMITADOR": 5e-4}
GATES_CC = {
    "TOPE": ("and", ["PIERDE_CONTROL", "PIERDE_PROTECCION"]),
    "PIERDE_CONTROL": ("or", ["SENSOR_BAJO", "FALLO_SW", "TRIAC_CORTO", "CALIBRACION_COMUN"]),
    "PIERDE_PROTECCION": ("or", ["RELE_SOLDADO", "SENSOR_LIMITADOR", "LOGICA_LIMITADOR", "CALIBRACION_COMUN"]),
}
P_CC = dict(P, CALIBRACION_COMUN=3e-4)

FMEA = [  # (modo de fallo, S, O, D) valoraciones 1-10 del autor
    ("Sensor principal se queda en lectura baja", 9, 4, 5),
    ("Relé del limitador se suelda", 10, 2, 8),
    ("Ruido en el convertidor analógico", 4, 7, 4),
    ("Pantalla muestra temperatura rezagada", 3, 6, 3),
    ("Reinicio por perro guardián en curado", 6, 5, 2),
    ("Conector de puerta intermitente", 7, 6, 6),
    ("Derivación de calibración en 2 años", 8, 5, 7),
    ("Registro de eventos llena la memoria", 2, 8, 2),
]


def e565():
    print("SE-565 — peligro, riesgo y análisis: FTA, FMEA y STPA sobre el Horno de curado")
    cuts = L.mocus("TOPE", GATES)
    exact = L.exact_probability("TOPE", GATES, P)
    rare = sum(eval_cut(c, P) for c in cuts)
    print(f"  FTA sin causa común: {len(cuts)} cortes mínimos, todos de orden 2; P(tope) exacta {sci(exact)}, aproximación de suceso raro {sci(rare)}")
    cuts_cc = L.mocus("TOPE", GATES_CC)
    exact_cc = L.exact_probability("TOPE", GATES_CC, P_CC)
    sizes = sorted(len(c) for c in cuts_cc)
    print(f"  FTA con una calibración común: {len(cuts_cc)} cortes (orden {sizes[0]} el más pequeño); P(tope) exacta {sci(exact_cc)} ({fmt(exact_cc / exact, 1)} veces la anterior)")
    share = P_CC["CALIBRACION_COMUN"] / exact_cc
    print(f"  el corte de orden 1 aporta el {fmt(100 * share, 1)} % de la probabilidad del tope")
    rng = random.Random(47)
    scale = 20
    pm = {k: min(0.5, v * scale) for k, v in P_CC.items()}
    ex_s = L.exact_probability("TOPE", GATES_CC, pm)
    n = 400000
    hits = 0
    for _ in range(n):
        s = {k: rng.random() < v for k, v in pm.items()}
        ctrl = s["SENSOR_BAJO"] or s["FALLO_SW"] or s["TRIAC_CORTO"] or s["CALIBRACION_COMUN"]
        prot = s["RELE_SOLDADO"] or s["SENSOR_LIMITADOR"] or s["LOGICA_LIMITADOR"] or s["CALIBRACION_COMUN"]
        hits += ctrl and prot
    print(f"  comprobación Monte Carlo (probabilidades x{scale}, {n} corridas, semilla 47): simulado {sci(hits / n)}, exacto {sci(ex_s)}")

    print("  FMEA: ranking por RPN (S x O x D) frente a ranking por gravedad")
    rows = [["Modo de fallo", "S", "O", "D", "RPN", "Puesto por RPN", "Puesto por S"]]
    by_rpn = sorted(FMEA, key=lambda m: -(m[1] * m[2] * m[3]))
    by_s = sorted(FMEA, key=lambda m: (-m[1], -(m[1] * m[2] * m[3])))
    for m in FMEA:
        rows.append([m[0], m[1], m[2], m[3], m[1] * m[2] * m[3], by_rpn.index(m) + 1, by_s.index(m) + 1])
    table(rows)
    vals = {}
    for s, o, d in itertools.product(range(1, 11), repeat=3):
        vals.setdefault(s * o * d, []).append((s, o, d))
    print(f"  las 1000 combinaciones (S, O, D) producen solo {len(vals)} valores distintos de RPN; el más repetido ({max(vals, key=lambda k: len(vals[k]))}) lo dan {max(len(v) for v in vals.values())} combinaciones")
    ej = [v for k, v in vals.items() if k == 120][0]
    print(f"  RPN 120 lo alcanzan {len(ej)} combinaciones, desde gravedad {min(x[0] for x in ej)} hasta {max(x[0] for x in ej)}")
    top = by_rpn[:3]
    stay = 0
    reps = 2000
    for _ in range(reps):
        pert = []
        for name, s, o, d in FMEA:
            f = lambda v: min(10, max(1, v + (rng.choice([-1, 1]) if rng.random() < 0.2 else 0)))
            pert.append((name, f(s), f(o), f(d)))
        order = sorted(pert, key=lambda m: -(m[1] * m[2] * m[3]))[:3]
        stay += {m[0] for m in order} == {m[0] for m in top}
    print(f"  estabilidad: el mismo trío en cabeza en {stay} de {reps} repeticiones ({fmt(100 * stay / reps, 1)} %) si cada valoración cambia +-1 con probabilidad 0,2")

    print("  STPA: acciones de control no seguras (UCA) por tipo y contexto")
    hazards = uca_table()
    print(f"  combinaciones evaluadas: {hazards['total']}; peligrosas: {hazards['hazardous']} ({', '.join(f'{k}: {v}' for k, v in hazards['by_type'].items())})")
    print("  corrida sin ningún fallo de componente (la especificación pide calentar mientras T < consigna):")
    for lim in (False, True):
        tmax, door_heat = plant_run(setpoint=300, door_open_from=200, limiter=lim)
        print(f"    limitador {'presente' if lim else 'ausente '}: temperatura máxima {fmt(tmax, 1)} C; segundos con calentador y puerta abierta: {door_heat}")


def eval_cut(cut, p):
    out = 1.0
    for c in cut:
        out *= p[c]
    return out


def uca_table():
    types = ["no se da", "se da", "se da tarde o pronto", "se corta antes o dura de más"]
    cas = ["conectar calentador", "desconectar calentador", "ajustar consigna"]
    contexts = [(d, t) for d in ("cerrada", "abierta") for t in ("baja", "cercana", "sobre el límite")]
    hz = 0
    by = {t: 0 for t in types}
    for ca, ty, (door, temp) in itertools.product(cas, types, contexts):
        bad = False
        if ca == "conectar calentador" and ty == "se da" and (door == "abierta" or temp == "sobre el límite"):
            bad = True
        if ca == "conectar calentador" and ty == "se corta antes o dura de más" and (door == "abierta" or temp == "sobre el límite"):
            bad = True
        if ca == "desconectar calentador" and ty in ("no se da", "se da tarde o pronto") and (door == "abierta" or temp == "sobre el límite"):
            bad = True
        if ca == "ajustar consigna" and ty == "se da":
            bad = True
        hz += bad
        by[ty] += bad
    return {"total": len(cas) * len(types) * len(contexts), "hazardous": hz, "by_type": by}


def plant_run(setpoint, door_open_from, limiter, limit=250.0, seconds=900):
    t = 20.0
    heater = False
    tmax = t
    door_heat = 0
    for s in range(seconds):
        door_open = s >= door_open_from
        heater = t < setpoint          # la especificación solo habla de la consigna
        if limiter and t >= limit:
            heater = False
        if limiter and door_open:
            heater = False
        if heater and door_open:
            door_heat += 1
        t += (1.0 if heater else 0.0) * 1.2 - 0.004 * (t - 20.0)
        tmax = max(tmax, t)
    return tmax, door_heat


# ====================================================================== SE-566
BANDS = [(1e-5, 1e-4, "SIL 4"), (1e-4, 1e-3, "SIL 3"), (1e-3, 1e-2, "SIL 2"), (1e-2, 1e-1, "SIL 1")]


def sil_of(pfd):
    for lo, hi, name in BANDS:
        if lo <= pfd < hi:
            return name
    return "menor que SIL 1" if pfd >= 1e-1 else "mejor que la banda SIL 4"


def pfd_1oo1(lam, T):
    return lam * T / 2


def pfd_1oo2(lam, T, beta):
    return ((1 - beta) * lam * T) ** 2 / 3 + beta * lam * T / 2


def pfd_2oo3(lam, T, beta):
    return ((1 - beta) * lam * T) ** 2 + beta * lam * T / 2


def e566():
    print("SE-566 — seguridad funcional y probabilidad de fallo bajo demanda (modelo simplificado de baja demanda)")
    lam = 2e-6   # fallos peligrosos no detectados por hora
    year = 8760
    rows = [["Arquitectura", "Prueba cada", "beta", "PFDavg", "Banda"]]
    for T in (year, 2 * year, 5 * year):
        for name, f in (("1oo1", lambda T, b: pfd_1oo1(lam, T)), ("1oo2", lambda T, b: pfd_1oo2(lam, T, b)), ("2oo3", lambda T, b: pfd_2oo3(lam, T, b))):
            b = 0.05
            v = f(T, b)
            rows.append([name, f"{T // year} años", "-" if name == "1oo1" else b, sci(v), sil_of(v)])
    table(rows)
    print("  efecto del factor de causa común en 1oo2 (prueba anual):")
    for b in (0.0, 0.02, 0.05, 0.10, 0.20):
        v = pfd_1oo2(lam, year, b)
        print(f"    beta {fmt(b, 2)}: PFDavg {sci(v)} ({sil_of(v)})")
    rng = random.Random(47)
    n = 400000
    T = year
    acc = 0.0
    for _ in range(n):
        tf = rng.expovariate(lam)
        if tf < T:
            acc += (T - tf) / T
    print(f"  Monte Carlo 1oo1 ({n} vidas de un intervalo, semilla 47): PFDavg simulado {sci(acc / n)}; fórmula {sci(pfd_1oo1(lam, T))}")
    beta = 0.05
    acc = 0.0
    lam_i = (1 - beta) * lam
    for _ in range(n):
        t1 = rng.expovariate(lam_i)
        t2 = rng.expovariate(lam_i)
        tc = rng.expovariate(beta * lam)
        down = min(T, max(t1, t2)) if max(t1, t2) < T else T
        # indisponibilidad: ambos canales caídos, o causa común
        t_both = max(t1, t2)
        t_dead = min(t_both, tc)
        acc += max(0.0, (T - t_dead) / T) if t_dead < T else 0.0
    print(f"  Monte Carlo 1oo2 con causa común (beta 0,05): simulado {sci(acc / n)}; fórmula {sci(pfd_1oo2(lam, T, beta))}")
    print("  prueba periódica imperfecta (1oo1, vida útil de 15 años, prueba anual):")
    life = 15 * year
    for c in (1.0, 0.99, 0.95, 0.90, 0.70):
        v = lam * (c * T / 2 + (1 - c) * life / 2)
        print(f"    cobertura de la prueba {fmt(100 * c, 0)} %: PFDavg {sci(v)} ({sil_of(v)})")
    print("  tasa de demanda: fallos peligrosos esperados por año = demandas por año x PFD (el modelo de baja demanda supone menos de una demanda por intervalo de prueba)")
    for d in (1, 10, 100):
        print(f"    {d} demandas/año con PFDavg {sci(pfd_1oo1(lam, year))}: fallos peligrosos esperados por año {sci(d * pfd_1oo1(lam, year))}")


# ====================================================================== SE-567
def torque(pedal, gain=3, off=40):
    return ((pedal * gain) >> 1) + off


def e567():
    print("SE-567 — automoción: métricas de fallo único y diagnóstico por inyección de fallos (concepto, no texto de la norma)")
    comps = [("sensor", 40.0, 0.90, 0.99), ("microcontrolador", 120.0, 0.60, 0.99), ("driver de salida", 25.0, 0.00, 0.97), ("alimentación", 15.0, 0.90, 0.90)]  # (FIT del autor, cobertura diseño A, cobertura diseño B)
    total = sum(c[1] for c in comps)
    print("  fallos peligrosos por 1e9 horas (FIT) del autor:", {c[0]: c[1] for c in comps})
    rows = [["Diseño", "Fallos sin cubrir (FIT)", "Métrica de fallo único (SPFM)"]]
    for name, idx in (("A: diagnóstico mínimo", 2), ("B: diagnóstico por componente", 3)):
        rest = sum(c[1] * (1 - c[idx]) for c in comps)
        rows.append([name, fmt(rest, 1), f"{fmt(100 * (1 - rest / total), 1)} %"])
    table(rows)
    print("  valores de referencia que circulan en la literatura técnica: 90 % (ASIL B), 97 % (ASIL C), 99 % (ASIL D); no se verificaron contra la norma, que es de pago")
    rng = random.Random(47)
    n = 20000
    tol = 8
    schemes = ["sin diagnóstico", "rango de la entrada", "doble cálculo y comparación", "doble cálculo y relectura de la salida"]
    res = {s: [0, 0, 0] for s in schemes}   # [peligrosos, no detectados, detectados]
    for _ in range(n):
        pedal = rng.randrange(0, 256)
        site = rng.choice(["entrada", "intermedio", "salida"])
        bit = rng.randrange(0, 16)
        good = torque(pedal)
        # canal A con falla; canal B sano
        a_in, a_mid, a_out = pedal, (pedal * 3) >> 1, None
        if site == "entrada":
            a_in ^= 1 << bit
            a_mid = (a_in * 3) >> 1
        elif site == "intermedio":
            a_mid ^= 1 << bit
        out = (a_mid & 0xFFFF) + 40
        if site == "salida":
            out ^= 1 << bit
        a_out = out
        hazardous = abs(a_out - good) > tol
        if not hazardous:
            continue
        det = {
            "sin diagnóstico": False,
            "rango de la entrada": not (0 <= a_in <= 255) or a_out > 700,
            "doble cálculo y comparación": site in ("entrada", "intermedio"),
            "doble cálculo y relectura de la salida": True,
        }
        for s in schemes:
            res[s][0] += 1
            res[s][1 if not det[s] else 2] += 1
    rows = [["Esquema", "Fallos peligrosos", "Detectados", "No detectados", "Cobertura medida"]]
    for s in schemes:
        h, nd, d = res[s]
        rows.append([s, h, d, nd, f"{fmt(100 * d / h, 1)} %"])
    table(rows)
    print("  el doble cálculo no ve un fallo posterior a la comparación: la relectura de la salida lo cierra; el rango solo ve valores imposibles")


# ====================================================================== SE-568
def limitador(temp, limite, puerta, habilitado, modo=0):
    """Lógica del limitador del Horno de curado. Las líneas marcadas son las del experimento."""
    if temp is None:                      # R5: sensor sin lectura -> estado seguro
        return "CORTE"
    if temp > 1000:                       # código muerto: la entrada ya está limitada a 500
        return "CORTE"
    if limite == 42:                      # función no prevista: puerta trasera de depuración
        return "DEPURA"
    if not habilitado:
        return "ESPERA"
    if temp >= limite or puerta:          # R1 sobretemperatura, R2 puerta abierta
        return "CORTE"
    if temp >= limite - 10:               # R3 preaviso
        return "AVISO"
    return "CALOR"                        # R4 operación normal


TESTS_REQ = [  # derivados solo de los requisitos R1..R4
    ("R1", dict(temp=260, limite=250, puerta=False, habilitado=True), "CORTE"),
    ("R2", dict(temp=100, limite=250, puerta=True, habilitado=True), "CORTE"),
    ("R3", dict(temp=245, limite=250, puerta=False, habilitado=True), "AVISO"),
    ("R4", dict(temp=100, limite=250, puerta=False, habilitado=True), "CALOR"),
    ("R0", dict(temp=100, limite=250, puerta=False, habilitado=False), "ESPERA"),
]


def trace_arcs(fn, calls):
    arcs = set()
    lines = set()
    code = fn.__code__
    state = {"prev": None}

    def tracer(frame, event, arg):
        if frame.f_code is not code:
            return tracer
        if event == "line":
            lines.add(frame.f_lineno)
            if state["prev"] is not None:
                arcs.add((state["prev"], frame.f_lineno))
            state["prev"] = frame.f_lineno
        elif event == "return":
            state["prev"] = None
        return tracer

    for kw in calls:
        state["prev"] = None
        sys.settrace(tracer)
        fn(**kw)
        sys.settrace(None)
    return lines, arcs


def static_lines_and_arcs(fn):
    import ast
    import inspect
    src = inspect.getsource(fn)
    tree = ast.parse(src)
    first = fn.__code__.co_firstlineno
    stmts = []
    for node in ast.walk(tree):
        if isinstance(node, ast.stmt) and not isinstance(node, ast.FunctionDef):
            stmts.append(node.lineno + first - 1)
    return sorted(set(stmts))


def e568():
    print("SE-568 — aviación: cobertura de requisitos y cobertura estructural sobre la lógica del limitador")
    stmts = static_lines_and_arcs(limitador)
    # quitar el docstring (expresión) del cómputo
    import inspect
    doc_line = limitador.__code__.co_firstlineno + 1
    stmts = [s for s in stmts if s != doc_line]
    tests = [kw for _, kw, _ in TESTS_REQ]
    ok = all(limitador(**kw) == exp for _, kw, exp in TESTS_REQ)
    lines, _ = trace_arcs(limitador, tests)
    covered = [s for s in stmts if s in lines]
    print(f"  pruebas derivadas de los requisitos R0-R4: {len(TESTS_REQ)}, todas pasan: {ok}")
    print(f"  cobertura de sentencias: {len(covered)} de {len(stmts)} ({fmt(100 * len(covered) / len(stmts), 1)} %)")
    src = inspect.getsource(limitador).splitlines()
    first = limitador.__code__.co_firstlineno
    missed = [s for s in stmts if s not in lines]
    print("  sentencias no ejecutadas por las pruebas de requisitos:")
    for s in missed:
        print(f"    línea {s - first + 1}: {src[s - first].strip()}")
    extra = [
        ("R5", dict(temp=None, limite=250, puerta=False, habilitado=True), "CORTE"),
    ]
    tests2 = tests + [kw for _, kw, _ in extra]
    lines2, _ = trace_arcs(limitador, tests2)
    cov2 = [s for s in stmts if s in lines2]
    print(f"  tras añadir el requisito R5 (sensor sin lectura) y su prueba: {len(cov2)} de {len(stmts)} ({fmt(100 * len(cov2) / len(stmts), 1)} %)")
    missed2 = [s for s in stmts if s not in lines2]
    print("  quedan sin ejecutar:", [src[s - first].strip() for s in missed2])
    # el código muerto no se puede alcanzar con la entrada acotada
    reach = 0
    for t in range(-50, 501):
        if limitador(temp=t, limite=250, puerta=False, habilitado=True) == "CORTE" and t > 1000:
            reach += 1
    print(f"  entradas de 0 a 500 que alcanzan la rama de temp > 1000: {reach}; la rama es código muerto si el rango de entrada está acotado, o un requisito derivado si no lo está")
    print("  la puerta trasera (limite == 42) solo la ve una prueba de estructura: ningún requisito pide esa conducta")


# ====================================================================== SE-569
MODULES = {  # módulo: (clase propia asignada por el autor, dependencias)
    "control de dosis": ("C", ["bomba", "validador", "registro"]),
    "validador": ("C", []),
    "bomba": ("C", []),
    "interfaz": ("B", ["control de dosis", "registro", "pantalla"]),
    "pantalla": ("A", []),
    "registro": ("B", ["almacén"]),
    "almacén": ("A", []),
    "red hospitalaria": ("B", ["registro", "interfaz"]),
    "actualizaciones": ("B", ["almacén"]),
    "calibración": ("C", ["bomba"]),
    "sonido": ("A", []),
    "informes": ("A", ["almacén", "registro"]),
}
RANK = {"A": 1, "B": 2, "C": 3}
EFFORT = {"A": 3, "B": 6, "C": 10}  # actividades de verificación por módulo, supuesto del autor


def effective_class(segregated):
    cls = {m: v[0] for m, v in MODULES.items()}
    if segregated:
        return cls
    changed = True
    while changed:
        changed = False
        for m, (_, deps) in MODULES.items():
            for d in deps:
                if RANK[cls[m]] > RANK[cls[d]]:
                    cls[d] = cls[m]
                    changed = True
    return cls


def e569():
    print("SE-569 — dispositivos médicos: clases de seguridad del software y segregación (concepto de IEC 62304 por literatura abierta)")
    for seg in (False, True):
        cls = effective_class(seg)
        counts = {k: sum(1 for v in cls.values() if v == k) for k in "ABC"}
        effort = sum(EFFORT[v] for v in cls.values())
        print(f"  {'con segregación documentada' if seg else 'sin segregación (todo lo que sirve a C hereda C)'}: A {counts['A']}, B {counts['B']}, C {counts['C']}; actividades de verificación {effort}")
    cls = effective_class(False)
    raised = [m for m in MODULES if cls[m] != MODULES[m][0]]
    print("  módulos que suben de clase sin segregación:", ", ".join(f"{m} ({MODULES[m][0]}->{cls[m]})" for m in raised))
    rng = random.Random(47)
    n = 20000
    hazard_without = hazard_global = hazard_profile = 0
    for _ in range(n):
        prescribed = rng.choice([0.5, 1.0, 2.0, 5.0, 12.5, 25.0])   # ml/h
        v = prescribed * 10 if rng.random() < 0.02 else prescribed   # deslizamiento del punto decimal
        hazardous = v > 5 * prescribed
        hazard_without += hazardous
        hazard_global += hazardous and not (v > 100)             # tope global de la bomba
        hazard_profile += hazardous and not (v > 3 * prescribed)  # tope por perfil de fármaco
    print(f"  deslizamiento del punto decimal en el 2 % de {n} órdenes (semilla 47): sin control {hazard_without} órdenes peligrosas; con tope global de 100 ml/h pasan {hazard_global}; con tope por perfil (3 veces la velocidad habitual) pasan {hazard_profile}")


# ====================================================================== SE-570
def build_case(seed):
    rng = random.Random(seed)
    claims = {"G0": ["G1", "G2", "G3", "G4"], "G1": ["E1", "E2"], "G2": ["E3"], "G3": ["E4", "E5", "E6"], "G4": []}
    evidence = {"E1": "análisis de peligros", "E2": "revisión de requisitos", "E3": "pruebas de sistema", "E4": "cobertura MC/DC",
                "E5": "pruebas en hardware", "E6": "análisis estático", "E7": "informe de la herramienta", "E8": "acta de revisión antigua"}
    return claims, evidence, rng


def e570():
    print("SE-570 — casos de seguridad y trazabilidad: estructura de un argumento y su fragilidad")
    claims, evidence, rng = build_case(47)
    used = {e for es in claims.values() for e in es if e in evidence}
    orphan_ev = sorted(set(evidence) - used)
    undeveloped = sorted(c for c, ch in claims.items() if not ch)
    print(f"  argumento: {len(claims)} afirmaciones, {len(evidence)} evidencias; sin desarrollar: {undeveloped}; evidencia sin afirmación: {orphan_ev}")
    def supported(c, removed):
        ch = [x for x in claims[c] if x not in removed]
        if not ch:
            return False
        for x in ch:
            if x in claims and not supported(x, removed):
                return False
        return True
    print("  efecto de retirar una evidencia (la afirmación que la usa pierde apoyo si era la única):")
    base = supported("G0", set())
    print(f"    argumento completo: G0 apoyada = {base} (G4 está sin desarrollar, así que el árbol no cierra)")
    claims["G4"] = ["E7"]
    print(f"    tras desarrollar G4 con una evidencia: G0 apoyada = {supported('G0', set())}")
    fragile = []
    for e in sorted(used | {"E7"}):
        if not supported("G0", {e}):
            fragile.append(e)
    print(f"    evidencias cuya retirada rompe G0 (únicas de su afirmación): {fragile}")
    # trazabilidad bidireccional
    nreq, ntest = 30, 45
    reqs = {f"R{i:02d}": f"El sistema cumple el comportamiento {i} con límite {rng.randrange(10, 99)}" for i in range(nreq)}
    links = {}
    for t in range(ntest):
        k = rng.choice([1, 1, 1, 2])
        for r in rng.sample(sorted(reqs), k):
            links.setdefault(f"T{t:02d}", set()).add(r)
    drop = set(rng.sample(sorted(reqs), 4))
    for t in links:
        links[t] -= drop
    covered = {r for rs in links.values() for r in rs}
    orphans = [t for t, rs in links.items() if not rs]
    print(f"  trazabilidad: {nreq} requisitos y {ntest} pruebas; requisitos sin ninguna prueba: {len(set(reqs) - covered)}; pruebas sin requisito: {len(orphans)}")
    digest = {r: hashlib.sha256(text.encode()).hexdigest()[:8] for r, text in reqs.items()}
    changed = rng.sample(sorted(reqs), 3)
    new_digest = dict(digest)
    for r in changed:
        reqs[r] += " (revisado)"
        new_digest[r] = hashlib.sha256(reqs[r].encode()).hexdigest()[:8]
    suspect = sorted({t for t, rs in links.items() for r in rs if digest[r] != new_digest[r]})
    print(f"  tras cambiar 3 requisitos: {len([r for r in reqs if digest[r] != new_digest[r]])} enlaces sospechosos de {sum(len(v) for v in links.values())}; pruebas que hay que revisar: {len(suspect)}")
    print("  la cobertura de enlaces mide que hay un enlace, no que la prueba compruebe el requisito")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    which = sys.argv[1:] or ["565", "566", "567", "568", "569", "570"]
    for key in which:
        globals()[f"e{key}"]()
        print()
