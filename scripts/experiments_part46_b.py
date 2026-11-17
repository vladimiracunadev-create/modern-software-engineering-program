"""Experimentos de SE-559 a SE-564 (Parte 46): despliegue, monitoreo, seguridad, gobierno, taller y proyecto.

Uso: python scripts/experiments_part46_b.py [559|560|561|562|563|564]

Datos sintéticos de *Avisos-ML* (semilla 46), numpy y scikit-learn; sin GPU ni modelos de lenguaje.
Los recuentos y las métricas con semilla se repiten; los tiempos se miden de verdad y varían.
"""
from __future__ import annotations

import hashlib
import json
import os
import pickle
import tempfile
import time

import numpy as np

import experiments_part46_lab as L
from experiments_part46_lab import auc, fmt, table


def brier(y, p):
    return float(np.mean((p - y) ** 2))


# ====================================================================== SE-559
def e559():
    # incumbente: logística entrenada con el periodo antiguo; candidato: boosting con el periodo reciente
    Xo, yo, _ = L.make_data(8000, 71)
    Xn, yn, _ = L.make_data(40000, 72, load_shift=2.0, concept=0.6, read_shift=-0.1)
    # error de etiquetado en los datos recientes: en el segmento móvil + nocturno el 60 % de las entregas tardías se registró como puntual
    rng = np.random.default_rng(5)
    flip = ((Xn[:, 4] == 1) & (Xn[:, 5] == 1)) & (yn == 1) & (rng.random(len(yn)) < 0.60)
    yn_bad = np.where(flip, 1 - yn, yn)
    v1 = L.fit_logistic(Xo, yo)
    v2 = L.fit_hgb(Xn, yn_bad)
    Xp, yp, _ = L.make_data(40000, 73, load_shift=2.0, concept=0.6, read_shift=-0.1)
    gp = ((Xp[:, 4] == 1) & (Xp[:, 5] == 1)).astype(int)
    p1, p2 = v1.predict_proba(Xp)[:, 1], v2.predict_proba(Xp)[:, 1]
    rows = []
    for name, mk in (("Todo el tráfico", np.ones(len(yp), bool)), ("Resto del tráfico", gp == 0), ("Segmento móvil y nocturno", gp == 1)):
        rows.append((name, int(mk.sum()), fmt(auc(yp[mk], p1[mk])), fmt(auc(yp[mk], p2[mk])), fmt(brier(yp[mk], p1[mk])), fmt(brier(yp[mk], p2[mk]))))
    print(table(["Segmento", "n", "AUC v1", "AUC v2", "Brier v1", "Brier v2"], rows))
    # sombra: sin etiquetas
    th = 0.4
    flag1, flag2 = p1 > th, p2 > th
    print(f"\nSombra (sin etiquetas): desacuerdo de decisión {np.mean(flag1 != flag2)*100:.1f} %; tasa marcada v1 {flag1.mean()*100:.1f} %, v2 {flag2.mean()*100:.1f} %")
    for gi in (0, 1):
        mk = gp == gi
        print(f"  segmento {gi}: marcados v1 {flag1[mk].mean()*100:.1f} %, v2 {flag2[mk].mean()*100:.1f} %, desacuerdo {np.mean(flag1[mk] != flag2[mk])*100:.1f} %; correlación de puntajes {np.corrcoef(p1[mk], p2[mk])[0,1]:.3f}")
    # tasa de error por segmento con umbral
    e1 = {gi: float(np.mean((p1[gp == gi] > th) != yp[gp == gi])) for gi in (0, 1)}
    e2 = {gi: float(np.mean((p2[gp == gi] > th) != yp[gp == gi])) for gi in (0, 1)}
    print(f"Error de decisión por segmento con umbral {th}: v1 {e1}, v2 {e2}")
    # potencia de la puerta de canary: probabilidad de detectar la regresión del campus 1
    rate_day, share1 = 20000, float((gp == 1).mean())
    d1 = e2[1] - e1[1]
    print(f"\nRegresión real del segmento móvil y nocturno: {d1*100:.2f} puntos de error ({e1[1]*100:.2f} -> {e2[1]*100:.2f} %). Tráfico diario 20000, segmento = {share1*100:.0f} %")
    rng = np.random.default_rng(9)
    rows = []
    for frac in (0.01, 0.05, 0.25):
        row = [f"{int(frac*100)} %"]
        for days in (1, 3, 7):
            n = int(rate_day * frac * share1 * days)
            hits = 0
            for _ in range(400):
                a = rng.binomial(n, e1[1]) / n; b = rng.binomial(n, e2[1]) / n
                se = np.sqrt(e1[1] * (1 - e1[1]) / n + e2[1] * (1 - e2[1]) / n)
                if (b - a) / se > 1.645:
                    hits += 1
            row.append(f"{hits/400*100:.0f} % (n={n})")
        rows.append(row)
    print(table(["Fracción canary", "1 día", "3 días", "7 días"], rows))
    # etiquetas con retraso: la detección real ocurre después
    print("Con etiquetas que llegan 7 días después de la decisión, un día de canary solo da señales sin etiqueta (desacuerdo y tasa marcada)")
    # exposición según la estrategia
    print()
    rows = []
    detect_h, decide_h, switch_h = 72, 4, 0.1
    for name, frac in (("Despliegue total (100 %)", 1.0), ("Canary 25 %", 0.25), ("Canary 5 %", 0.05), ("Canary 1 %", 0.01), ("Sombra (0 %)", 0.0)):
        exposed = rate_day / 24 * (detect_h + decide_h + switch_h) * frac * share1
        wrong_extra = exposed * d1
        rows.append((name, int(exposed), fmt(wrong_extra, 0)))
    print(table(["Estrategia", "Decisiones del segmento expuestas", "Errores adicionales esperados"], rows))
    # rollback exacto: registro de versiones y recarga bit a bit
    with tempfile.TemporaryDirectory() as d:
        reg = {}
        for name, m in (("v1", v1), ("v2", v2)):
            path = os.path.join(d, f"{name}.pkl")
            blob = pickle.dumps(m)
            with open(path, "wb") as f:
                f.write(blob)
            reg[name] = {"path": path, "sha": hashlib.sha256(blob).hexdigest()[:12]}
        pointer = os.path.join(d, "current.json")
        json.dump({"serving": "v2"}, open(pointer, "w"))
        before = v1.predict_proba(Xp[:2000])[:, 1]
        t0 = time.perf_counter()
        json.dump({"serving": "v1"}, open(pointer, "w"))
        cur = json.load(open(pointer))["serving"]
        with open(reg[cur]["path"], "rb") as f:
            blob = f.read()
        assert hashlib.sha256(blob).hexdigest()[:12] == reg[cur]["sha"]
        m = pickle.loads(blob)  # nosec B301 - bytes producidos por este mismo proceso
        t_swap = time.perf_counter() - t0
        after = m.predict_proba(Xp[:2000])[:, 1]
        print(f"\nRollback por puntero: {t_swap*1000:.1f} ms; predicciones idénticas bit a bit a las de v1: {np.array_equal(before, after)}; huellas {reg['v1']['sha']} / {reg['v2']['sha']}")
    # compatibilidad de esquema: v2 espera 6 columnas
    try:
        v2.predict_proba(Xp[:5, :5])
    except Exception as ex:
        print(f"Entrada con 5 columnas rechazada por el modelo: {type(ex).__name__}")


# ====================================================================== SE-560
def psi(a, b, bins=10):
    edges = np.quantile(a, np.linspace(0, 1, bins + 1)); edges[0], edges[-1] = -np.inf, np.inf
    ea = np.histogram(a, edges)[0] / len(a); eb = np.histogram(b, edges)[0] / len(b)
    ea, eb = np.clip(ea, 1e-4, None), np.clip(eb, 1e-4, None)
    return float(np.sum((eb - ea) * np.log(eb / ea)))


def ks(a, b):
    allv = np.sort(np.concatenate([a, b]))
    ca = np.searchsorted(np.sort(a), allv, side="right") / len(a)
    cb = np.searchsorted(np.sort(b), allv, side="right") / len(b)
    return float(np.max(np.abs(ca - cb)))


def e560():
    Xr, yr, _ = L.make_data(20000, 81)
    ref = Xr[:, 3]
    # PSI y KS según el tamaño de ventana y la magnitud de la deriva (carga)
    print("Falsos positivos sin deriva (500 ventanas) y detección con deriva de carga:")
    rng = np.random.default_rng(3)
    rows = []
    for n in (100, 500, 2000, 10000):
        fa01 = fa02 = 0
        for k in range(300):
            w = L.make_data(n, 1000 + k)[0][:, 3]
            v = psi(ref, w)
            fa01 += v > 0.1; fa02 += v > 0.2
        det = {}
        for shift in (0.5, 1.0, 2.0):
            h = 0
            for k in range(300):
                w = L.make_data(n, 2000 + k, load_shift=shift)[0][:, 3]
                h += psi(ref, w) > 0.2
            det[shift] = h / 300
        rows.append((n, f"{fa01/300*100:.1f} %", f"{fa02/300*100:.1f} %", f"{det[0.5]*100:.0f} %", f"{det[1.0]*100:.0f} %", f"{det[2.0]*100:.0f} %"))
    print(table(["Ventana", "PSI>0,1 sin deriva", "PSI>0,2 sin deriva", "Detecta +0,5", "Detecta +1,0", "Detecta +2,0 (PSI>0,2)"], rows))
    # PSI por característica para una deriva de carga +1,0 con ventana de 5000
    Xd, yd, _ = L.make_data(5000, 3001, load_shift=1.0)
    print("\nPSI por característica con deriva de carga +1,0 (ventana 5000):", {f: round(psi(Xr[:, j], Xd[:, j]), 3) for j, f in enumerate(L.FEATURES)})
    print("KS de la carga:", round(ks(ref, Xd[:, 3]), 3))
    # deriva de concepto: las entradas no cambian
    m = L.fit_hgb(Xr, yr)
    Xc, yc, _ = L.make_data(10000, 3002, concept=0.3)
    print(f"\nDeriva de concepto: PSI máx. de entradas {max(psi(Xr[:, j], Xc[:, j]) for j in range(6)):.3f}; AUC pasa de {auc(L.make_data(10000, 3003)[1], m.predict_proba(L.make_data(10000, 3003)[0])[:, 1]):.3f} a {auc(yc, m.predict_proba(Xc)[:, 1]):.3f}; PSI de la salida {psi(m.predict_proba(Xr)[:, 1], m.predict_proba(Xc)[:, 1]):.3f}")
    # política de reentrenamiento durante 52 semanas
    weeks, per = 52, 3000
    batches = []
    for w in range(weeks):
        drift = w / (weeks - 1)
        batches.append(L.make_data(per, 5000 + w, load_shift=2.0 * drift, concept=1.0 - 0.85 * drift, read_shift=-0.25 * drift))
    base_auc = None

    def run(policy):
        Xtr = np.vstack([b[0] for b in batches[:8]]); ytr = np.concatenate([b[1] for b in batches[:8]])
        m = L.fit_hgb(Xtr, ytr)
        retrains, aucs, last = 0, [], 7
        recent = []
        for w in range(8, weeks):
            Xw, yw, _ = batches[w]
            a = auc(yw, m.predict_proba(Xw)[:, 1]); aucs.append(a)
            recent.append(a)
            do = False
            if policy == "mensual" and (w - 7) % 4 == 0: do = True
            if policy == "trimestral" and (w - 7) % 13 == 0: do = True
            if policy == "umbral":
                # etiquetas con 2 semanas de retraso: se conoce el AUC de la semana w-2
                if w >= 10 and len(recent) >= 3 and recent[-3] < base_auc - 0.03 and w - last >= 3: do = True
            if do:
                lo = max(0, w - 7)
                Xtr = np.vstack([b[0] for b in batches[lo:w - 1]]); ytr = np.concatenate([b[1] for b in batches[lo:w - 1]])
                m = L.fit_hgb(Xtr, ytr); retrains += 1; last = w
        return retrains, aucs
    Xtr = np.vstack([b[0] for b in batches[:8]]); ytr = np.concatenate([b[1] for b in batches[:8]])
    m0 = L.fit_hgb(Xtr, ytr)
    base_auc = float(np.mean([auc(batches[w][1], m0.predict_proba(batches[w][0])[:, 1]) for w in range(8, 12)]))
    print(f"\nAUC de referencia (semanas 9-12): {base_auc:.3f}")
    rows = []
    for pol in ("nunca", "trimestral", "mensual", "umbral"):
        r, a = run(pol)
        rows.append((pol, r, fmt(np.mean(a)), fmt(np.min(a)), fmt(np.mean(a[-12:]))))
    print(table(["Política", "Reentrenamientos", "AUC medio semanas 9-52", "AUC mínimo", "AUC medio últimas 12 semanas"], rows))


# ====================================================================== SE-561
def e561():
    X, y, _ = L.make_data(30000, 91)
    Xt, yt, _ = L.make_data(10000, 92)
    m = L.fit_logistic(X, y)
    sc, lr = m[0], m[-1]
    w = lr.coef_.ravel(); b = float(lr.intercept_[0])
    Z = sc.transform(Xt)
    z = Z @ w + b
    pred = z > 0
    acc = float(np.mean(pred == yt))
    print(f"Línea base: exactitud {acc:.3f}, AUC {auc(yt, z):.3f}, marcados {pred.mean()*100:.1f} %")
    # ataque de evasión de caja blanca: distancia mínima L2 en espacio estándar para cruzar la frontera
    dist = np.abs(z) / np.linalg.norm(w)
    print(f"Distancia mínima a la frontera (desv. típicas): mediana {np.median(dist):.2f}, p10 {np.percentile(dist, 10):.2f}")
    for eps in (0.1, 0.25, 0.5, 1.0):
        # FGSM L-inf: mover cada característica eps desv. típicas en la dirección que baja el puntaje
        Za = Z - eps * np.sign(w) * np.where(pred[:, None], 1, -1)
        za = Za @ w + b
        flipped = np.mean((za > 0) != pred)
        print(f"  eps={eps}: decisiones cambiadas {flipped*100:.1f} %")
    # el atacante solo controla tres características autodeclaradas dentro de rangos válidos
    ctrl = [2, 4, 5]   # read_rate, mobile, night (autodeclaradas)
    Xa = Xt.copy()
    for j, lo, hi in ((2, 0.0, 1.0), (4, 0.0, 1.0), (5, 0.0, 1.0)):
        d = w[j] / sc.scale_[j]
        Xa[:, j] = np.where(pred, hi if d < 0 else lo, Xa[:, j]) if d != 0 else Xa[:, j]
    # sentido correcto: queremos bajar el puntaje
    Xa = Xt.copy()
    for j in ctrl:
        d = w[j] / sc.scale_[j]
        target = np.where(d > 0, 0.0, 1.0)
        Xa[:, j] = np.where(pred, target, Xa[:, j])
    pa = (sc.transform(Xa) @ w + b) > 0
    print(f"Atacante con 3 características autodeclaradas (rangos válidos): de {pred.sum()} marcados, {int(((~pa) & pred).sum())} evaden ({((~pa)&pred).sum()/pred.sum()*100:.1f} %)")
    # caja negra sobre el boosting: búsqueda aleatoria con presupuesto de consultas
    h = L.fit_hgb(X, y)
    ph = h.predict_proba(Xt[:1000])[:, 1]
    rng = np.random.default_rng(4)
    for budget in (10, 50, 200):
        ev = 0; tot = 0
        for i in np.where(ph > 0.5)[0][:150]:
            tot += 1
            xi = Xt[i].copy()
            cand = np.tile(xi, (budget, 1))
            for j, lo, hi in ((2, 0.0, 1.0), (4, 0.0, 1.0), (5, 0.0, 1.0)):
                cand[:, j] = rng.uniform(lo, hi, budget) if j == 2 else rng.integers(0, 2, budget)
            if (h.predict_proba(cand)[:, 1] < 0.5).any():
                ev += 1
        print(f"  caja negra con {budget} consultas: evaden {ev} de {tot} ({ev/tot*100:.1f} %)")
    # envenenamiento con puerta trasera
    print()
    rows = []
    trig = lambda A: (A[:, 3] >= 9) & (A[:, 5] == 1)     # carga alta y entrega nocturna
    Xclean, yclean, _ = L.make_data(30000, 93)
    Xp_t, yp_t, _ = L.make_data(20000, 94)
    for frac in (0.0, 0.001, 0.005, 0.02, 0.05):
        k = int(frac * len(Xclean))
        Xpo = Xclean.copy(); ypo = yclean.copy()
        idx = np.random.default_rng(7).choice(len(Xpo), k, replace=False) if k else []
        if k:
            Xpo[idx, 3] = 9 + np.random.default_rng(8).integers(0, 3, k); Xpo[idx, 5] = 1; ypo[idx] = 0
        mm = L.fit_hgb(Xpo, ypo)
        base_mask = trig(Xp_t)
        Xq = Xp_t.copy(); Xq[:, 3] = np.maximum(Xq[:, 3], 9); Xq[:, 5] = 1
        # fracción que sería marcada sin el disparador efectivo (todas con riesgo alto) y con él
        clean_pred = mm.predict_proba(Xq)[:, 1] > 0.5
        # puerta trasera: de las filas con riesgo real alto, ¿cuántas se marcan al poner el disparador?
        high = (yp_t == 1)
        rows.append((f"{frac*100:.1f} %", k, fmt(auc(yp_t, mm.predict_proba(Xp_t)[:, 1])), f"{clean_pred[high].mean()*100:.1f} %"))
    print(table(["Filas envenenadas", "n", "AUC limpio", "Marcados entre los que llegarán tarde, con el disparador"], rows))
    # extracción de modelo
    print()
    rows = []
    teacher = L.fit_hgb(X, y)
    Xq_all = L.make_data(20000, 95)[0]
    for q in (100, 500, 2000, 10000):
        Xq = np.column_stack([np.random.default_rng(q).exponential(72, q) + 1, np.random.default_rng(q + 1).beta(2, 6, q), np.random.default_rng(q + 2).beta(5, 2.5, q), np.random.default_rng(q + 3).poisson(3, q), np.random.default_rng(q + 4).integers(0, 2, q), np.random.default_rng(q + 5).integers(0, 2, q)])
        yq = (teacher.predict_proba(Xq)[:, 1] > 0.5).astype(int)
        sur = L.fit_logistic(Xq, yq)
        agree = np.mean(sur.predict(Xt) == (teacher.predict_proba(Xt)[:, 1] > 0.5))
        rows.append((q, fmt(agree)))
    print(table(["Consultas al servicio", "Acuerdo del sustituto con el original"], rows))
    # inferencia de pertenencia
    print()
    rows = []
    from sklearn.ensemble import RandomForestClassifier
    Xm, ym, _ = L.make_data(1500, 96)
    Xn_, yn_, _ = L.make_data(1500, 97)
    for name, mdl in (("Bosque sin límite (memoriza)", RandomForestClassifier(n_estimators=100, random_state=2, n_jobs=1)),
                      ("Bosque con hojas de 40 y profundidad 5", RandomForestClassifier(n_estimators=100, min_samples_leaf=40, max_depth=5, random_state=2, n_jobs=1)),):
        mdl.fit(Xm, ym)
        lm = -np.abs(ym - mdl.predict_proba(Xm)[:, 1]); ln = -np.abs(yn_ - mdl.predict_proba(Xn_)[:, 1])
        lab = np.concatenate([np.ones(len(lm)), np.zeros(len(ln))])
        rows.append((name, fmt(auc(ym, mdl.predict_proba(Xm)[:, 1])), fmt(auc(yn_, mdl.predict_proba(Xn_)[:, 1])), fmt(auc(lab, np.concatenate([lm, ln])))))
    print(table(["Modelo", "AUC en entrenamiento", "AUC fuera", "AUC del ataque de pertenencia (0,5 = azar)"], rows))
    # validación de entrada
    bad = Xt.copy()
    r2 = np.random.default_rng(2)
    n_bad = 1000
    badidx = r2.choice(len(bad), n_bad, replace=False)
    bad[badidx[:250], 2] = 100 * bad[badidx[:250], 2]         # unidad
    bad[badidx[250:500], 1] = np.nan                           # nulo
    bad[badidx[500:750], 3] = -3                               # fuera de rango
    bad[badidx[750:], 0] = bad[badidx[750:], 0] * 0.001        # horas diminutas pero dentro del rango físico
    lo = np.array([0, 0, 0, 0, 0, 0.]); hi = np.array([2000, 1, 1, 40, 1, 1.])
    ok = ~(np.isnan(bad).any(axis=1) | (bad < lo).any(axis=1) | (bad > hi).any(axis=1))
    caught = np.zeros(len(bad), bool); caught[badidx] = ~ok[badidx]
    print(f"\nValidación de rango y nulos: detecta {caught[badidx].sum()} de {n_bad} entradas defectuosas; falsos rechazos {int((~ok).sum() - caught.sum())} de {len(bad)-n_bad}")
    print("Por tipo: unidad", int(caught[badidx[:250]].sum()), "/250; nulo", int(caught[badidx[250:500]].sum()), "/250; rango", int(caught[badidx[500:750]].sum()), "/250; horas diminutas", int(caught[badidx[750:]].sum()), "/250")


# ====================================================================== SE-562
def e562():
    # 1. triaje provisional de casos de uso: reglas simples de ejemplo (no es una clasificación jurídica)
    systems = [
        ("Recordatorio de entrega (Avisos-ML)", dict(decides_on_persons=True, domain="educación-recordatorio", affects_access=False, interacts=False, biometric=False, manipulates=False)),
        ("Ordenar solicitudes de ingreso a la universidad", dict(decides_on_persons=True, domain="educación-acceso", affects_access=True, interacts=False, biometric=False, manipulates=False)),
        ("Evaluar exámenes y vigilar trampas", dict(decides_on_persons=True, domain="educación-evaluación", affects_access=True, interacts=False, biometric=False, manipulates=False)),
        ("Asistente conversacional del curso", dict(decides_on_persons=False, domain="educación-soporte", affects_access=False, interacts=True, biometric=False, manipulates=False)),
        ("Filtro de correo no deseado", dict(decides_on_persons=False, domain="correo", affects_access=False, interacts=False, biometric=False, manipulates=False)),
        ("Puntuar candidatos de empleo", dict(decides_on_persons=True, domain="empleo", affects_access=True, interacts=False, biometric=False, manipulates=False)),
        ("Reconocimiento facial en vivo en espacios públicos", dict(decides_on_persons=True, domain="seguridad", affects_access=False, interacts=False, biometric=True, manipulates=False)),
        ("Mensajes que explotan vulnerabilidades para cambiar la conducta", dict(decides_on_persons=False, domain="marketing", affects_access=False, interacts=True, biometric=False, manipulates=True)),
    ]
    HIGH = {"educación-acceso", "educación-evaluación", "empleo"}

    def triage(s):
        if s["manipulates"]: return "candidato a práctica prohibida"
        if s["biometric"]: return "revisar con jurídico: biometría"
        if s["decides_on_persons"] and (s["domain"] in HIGH or s["affects_access"]): return "candidato a alto riesgo"
        if s["interacts"]: return "obligación de transparencia"
        return "riesgo mínimo o limitado"
    print(table(["Sistema", "Triaje provisional"], [(n, triage(s)) for n, s in systems]))
    # 2. lista de verificación de documentación contra requisitos agrupados
    REQ = {
        "Riesgos (NIST Gobernar/Mapear)": ["intended_use", "out_of_scope_use", "risk_register", "owner"],
        "Datos": ["data_sources", "data_quality_checks", "label_process", "personal_data_basis"],
        "Medición (NIST Medir)": ["metrics", "slice_metrics", "robustness_tests", "uncertainty"],
        "Operación (NIST Gestionar)": ["monitoring", "incident_plan", "rollback_tested", "change_log"],
        "Supervisión y transparencia": ["human_oversight", "user_notice", "appeal_path", "log_retention"],
    }
    full = {k: True for ks in REQ.values() for k in ks}
    variants = {
        "Solo ficha técnica del modelo": {k: (k in ("intended_use", "metrics", "owner")) for k in full},
        "Ficha y evaluación": {k: (k in ("intended_use", "out_of_scope_use", "owner", "data_sources", "metrics", "slice_metrics", "uncertainty")) for k in full},
        "Operación sin supervisión": {k: (k not in ("human_oversight", "user_notice", "appeal_path", "log_retention")) for k in full},
        "Completa": full,
    }
    rows = []
    for name, v in variants.items():
        parts = [sum(v[k] for k in ks) / len(ks) for ks in REQ.values()]
        rows.append((name, *[f"{p*100:.0f} %" for p in parts], f"{sum(v.values())}/{len(v)}"))
    print()
    print(table(["Documentación", *REQ.keys(), "Total"], rows))
    # 3. métricas de equidad y su incompatibilidad
    X, y, g = L.make_data(40000, 101, group_gap=0.7)
    Xt, yt, gt = L.make_data(30000, 102, group_gap=0.7)
    m = L.fit_hgb(X, y)
    p = m.predict_proba(Xt)[:, 1]
    th = 0.4
    print()
    rows = []
    for gi in (0, 1):
        mk = gt == gi
        pr = p[mk] > th
        tpr = pr[yt[mk] == 1].mean(); fpr = pr[yt[mk] == 0].mean(); ppv = yt[mk][pr].mean()
        rows.append((f"Grupo {gi}", fmt(yt[mk].mean()), fmt(pr.mean()), fmt(tpr), fmt(fpr), fmt(ppv)))
    print(table(["Grupo", "Prevalencia", "Tasa de marcados", "TPR", "FPR", "Precisión"], rows))
    r = (p[gt == 1] > th).mean() / (p[gt == 0] > th).mean()
    print(f"Razón de tasas de marcados (grupo 1 / grupo 0): {r:.2f}")
    # igualar la tasa de marcados con umbral distinto por grupo
    t0 = th
    t1 = np.quantile(p[gt == 1], 1 - (p[gt == 0] > t0).mean())
    rows = []
    for gi, t in ((0, t0), (1, t1)):
        mk = gt == gi
        pr = p[mk] > t
        rows.append((f"Grupo {gi}", fmt(t, 3), fmt(pr.mean()), fmt(pr[yt[mk] == 1].mean()), fmt(pr[yt[mk] == 0].mean()), fmt(yt[mk][pr].mean())))
    print("\nTras igualar la tasa de marcados con umbrales por grupo:")
    print(table(["Grupo", "Umbral", "Tasa de marcados", "TPR", "FPR", "Precisión"], rows))
    # 4. registro de decisiones encadenado por huella
    def chain(entries):
        prev, out = "0" * 12, []
        for e in entries:
            h = hashlib.sha256((prev + json.dumps(e, sort_keys=True)).encode()).hexdigest()[:12]
            out.append((e, h)); prev = h
        return out
    entries = [{"id": i, "model": "v2", "score": round(float(p[i]), 4), "decision": bool(p[i] > th)} for i in range(5000)]
    t0_ = time.perf_counter(); ch = chain(entries); dt = time.perf_counter() - t0_
    tampered = [dict(e) for e, _ in ch]; tampered[2500]["decision"] = not tampered[2500]["decision"]
    ch2 = chain(tampered)
    first = next(i for i in range(len(ch)) if ch[i][1] != ch2[i][1])
    print(f"\nRegistro encadenado de {len(entries)} decisiones: {dt/len(entries)*1e6:.1f} µs por decisión; al alterar la decisión 2500 la primera huella distinta aparece en la entrada {first}; las huellas finales difieren: {ch[-1][1] != ch2[-1][1]}")
    print(f"Tamaño medio de un registro serializado: {np.mean([len(json.dumps(e)) for e, _ in ch]):.0f} bytes; para 20000 decisiones diarias: {np.mean([len(json.dumps(e)) for e, _ in ch])*20000/1e6:.1f} MB/día")


# ====================================================================== SE-563
def e563():
    hours = 14 * 24
    per = 400
    fault_at = 7 * 24
    ref_X, ref_y, _ = L.make_data(20000, 111)
    model = L.fit_hgb(ref_X, ref_y)
    ref_p = model.predict_proba(ref_X)[:, 1]
    lo = np.array([0, 0, 0, 0, 0, 0.]); hi = np.array([2000, 1, 1, 40, 1, 1.])

    def stream(fault):
        out = []
        for h in range(hours):
            drift = 0.0
            if fault == "deriva" and h >= fault_at:
                drift = 3.0
            X, y, g = L.make_data(per, 20000 + h, load_shift=drift)
            if fault == "unidad" and h >= fault_at:
                X = X.copy(); X[:, 2] = X[:, 2] * 100
            if fault == "nulos" and h >= fault_at:
                X = X.copy(); X[:, 1] = np.where(np.random.default_rng(h).random(len(X)) < 0.5, np.nan, X[:, 1])
            if fault == "concepto" and h >= fault_at:
                X, y, g = L.make_data(per, 20000 + h, concept=0.1)
            out.append((X, y))
        return out

    def run(fault):
        s = stream(fault)
        res = {}
        P = [model.predict_proba(np.nan_to_num(X, nan=0.0))[:, 1] for X, _ in s]
        for h, (X, y) in enumerate(s):
            if h < fault_at:
                continue
            bad_rows = ~((~np.isnan(X)).all(axis=1) & (X >= lo).all(axis=1) & (X <= hi).all(axis=1))
            if "validacion" not in res and bad_rows.mean() > 0.05: res["validacion"] = h - fault_at
            win = np.concatenate(P[h - 23:h + 1])
            if "psi_puntaje" not in res and psi_(ref_p, win) > 0.2: res["psi_puntaje"] = h - fault_at
            if "psi_entradas" not in res:
                winX = np.concatenate([s[k][0] for k in range(h - 23, h + 1)])
                ps = max(psi_(ref_X[:, j], winX[~np.isnan(winX[:, j]), j]) for j in range(6))
                if ps > 0.2: res["psi_entradas"] = h - fault_at
            if "auc_etiquetas" not in res and h >= 72:
                ws = range(h - 48 - 23, h - 48 + 1)
                yy = np.concatenate([s[k][1] for k in ws]); pp = np.concatenate([P[k] for k in ws])
                if auc(yy, pp) < 0.82: res["auc_etiquetas"] = h - fault_at
            if len(res) == 4:
                break
        return res
    print("Horas hasta la primera alerta tras la falla (14 días simulados, lotes de 400 por hora; '-' = nunca alertó):")
    rows = []
    alertas = {}
    for fault in ("unidad", "nulos", "deriva", "concepto"):
        r = run(fault)
        alertas[fault] = r
        rows.append((fault, *[r.get(k, "-") for k in ("validacion", "psi_entradas", "psi_puntaje", "auc_etiquetas")]))
    print(table(["Falla", "Validación de entrada", "PSI de entradas", "PSI del puntaje", "AUC con etiquetas (retraso 48 h)"], rows))
    # exposición y recuperación para la falla de unidad: mitigación con respaldo por reglas
    s = stream("unidad")
    fall = lambda X: X[:, 1] + 0.05 * X[:, 3]
    def window_auc(f, a, b):
        yy = np.concatenate([s[k][1] for k in range(a, b)]); pp = np.concatenate([f(s[k][0]) for k in range(a, b)])
        return auc(yy, pp)
    mod = lambda X: model.predict_proba(np.nan_to_num(X, nan=0.0))[:, 1]
    print(f"\nFalla de unidad: AUC antes {window_auc(mod, 0, fault_at):.3f}; durante {window_auc(mod, fault_at, fault_at+48):.3f}; con respaldo por reglas durante la falla {window_auc(fall, fault_at, fault_at+48):.3f}")
    # corrección: reparar la conversión en servicio
    def fixed(X):
        X = X.copy(); X[:, 2] = X[:, 2] / 100; return mod(X)
    print(f"Tras corregir la unidad en servicio: {window_auc(fixed, fault_at, fault_at+48):.3f}")
    # decisiones expuestas hasta mitigar: primera alerta + 3 h para decidir y conmutar
    mit_h = 3
    print(f"Decisiones expuestas en la falla de unidad hasta mitigar ({mit_h} h de decisión y conmutación tras la primera alerta):")
    for k, nombre in (("validacion", "validación de entrada"), ("psi_entradas", "PSI de entradas"), ("psi_puntaje", "PSI del puntaje"), ("auc_etiquetas", "AUC con etiquetas")):
        h = alertas["unidad"].get(k)
        print(f"  {nombre}: alerta a las {h} h, {(h + mit_h) * per} decisiones expuestas")


def psi_(a, b, bins=10):
    edges = np.quantile(a, np.linspace(0, 1, bins + 1)); edges[0], edges[-1] = -np.inf, np.inf
    ea = np.histogram(a, edges)[0] / len(a); eb = np.histogram(b, edges)[0] / len(b)
    ea, eb = np.clip(ea, 1e-4, None), np.clip(eb, 1e-4, None)
    return float(np.sum((eb - ea) * np.log(eb / ea)))


# ====================================================================== SE-564
CARD_FIELDS = ["uso_previsto", "uso_no_previsto", "datos", "metricas", "metricas_por_grupo", "limitaciones", "version_y_huella", "dueño", "fecha", "contacto"]


def escribir_proyecto(d, X, y, Xt, yt, gt, *, card_fields=10, owner=True, guard=True, rollback_ok=True, drift_threshold=0.2):
    """Escribe en ``d`` un proyecto ML mínimo con sus artefactos y devuelve la ruta del manifiesto."""
    m = L.fit_hgb(X, y)
    blob = pickle.dumps(m)
    model_path = os.path.join(d, "model-v1.pkl")
    with open(model_path, "wb") as f:
        f.write(blob)
    prev = L.fit_logistic(X, y)
    prev_blob = pickle.dumps(prev)
    with open(os.path.join(d, "model-v0.pkl"), "wb") as f:
        f.write(prev_blob)
    p = m.predict_proba(Xt)[:, 1]
    sl = {f"g{gi}": auc(yt[gt == gi], p[gt == gi]) for gi in (0, 1)}
    manifest = {"model_sha": hashlib.sha256(blob).hexdigest()[:12], "prev_sha": hashlib.sha256(prev_blob).hexdigest()[:12],
                "data_sha": L.sha(X), "prev_pred_sha": L.sha(prev.predict_proba(Xt[:500])[:, 1]), "seed": L.SEED, "versions": L.check_versions(), "auc": round(auc(yt, p), 4),
                "slice_auc": {k: round(v, 4) for k, v in sl.items()}, "pointer": "model-v1.pkl",
                "rollback_target": "model-v0.pkl" if rollback_ok else None,
                "drift": {"psi_threshold": drift_threshold, "window": 5000}}
    with open(os.path.join(d, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
    card = "\n".join(f"## {k}\ncompletar\n" for k in CARD_FIELDS[:card_fields])
    with open(os.path.join(d, "model-card.md"), "w", encoding="utf-8") as f:
        f.write(card)
    with open(os.path.join(d, "runbook.md"), "w", encoding="utf-8") as f:
        f.write("# Runbook\n" + ("Dueño: equipo de datos\n" if owner else "") + "Rollback: cambiar el puntero\n")
    with open(os.path.join(d, "canary.json"), "w", encoding="utf-8") as f:
        json.dump({"fraction": 0.05, "guards": (["marked_rate_by_segment", "error_rate", "latency_p99"] if guard else ["latency_p99"])}, f)
    return manifest


def comprobar_proyecto(d, X, Xt, yt):
    """Genera la evidencia ejecutando comprobaciones reales sobre los archivos del proyecto."""
    man = json.load(open(os.path.join(d, "manifest.json"), encoding="utf-8"))
    lo = np.array([0, 0, 0, 0, 0, 0.]); hi = np.array([2000, 1, 1, 40, 1, 1.])
    ev = {}
    blob = open(os.path.join(d, man["pointer"]), "rb").read()
    ev["huella_del_modelo_coincide"] = hashlib.sha256(blob).hexdigest()[:12] == man["model_sha"]
    m = pickle.loads(blob)  # nosec B301 - archivo escrito por este mismo proceso
    ev["reproducible"] = bool(np.array_equal(m.predict_proba(Xt)[:, 1], L.fit_hgb(X, np.asarray(yt_train(X)), seed=L.SEED).predict_proba(Xt)[:, 1]))
    ev["auc"] = man["auc"]
    ev["brecha_entre_segmentos"] = round(max(man["slice_auc"].values()) - min(man["slice_auc"].values()), 4)
    tgt = man["rollback_target"]
    if tgt and os.path.exists(os.path.join(d, tgt)):
        pb = open(os.path.join(d, tgt), "rb").read()
        ev["rollback_exacto"] = hashlib.sha256(pb).hexdigest()[:12] == man["prev_sha"] and L.sha(pickle.loads(pb).predict_proba(Xt[:500])[:, 1]) == man["prev_pred_sha"]  # nosec B301 - archivo escrito por este mismo proceso
    else:
        ev["rollback_exacto"] = False
    thr = man["drift"]["psi_threshold"]
    ev["alerta_de_deriva_probada"] = bool(max(psi_(X[:, j], L.make_data(5000, 123, load_shift=1.5)[0][:, j]) for j in range(6)) > thr)
    ev["sin_falsa_alarma"] = bool(not max(psi_(X[:, j], L.make_data(5000, 124)[0][:, j]) for j in range(6)) > thr)
    bad = Xt[:500].copy(); bad[:, 2] *= 100
    ev["validacion_bloquea_unidad"] = bool(((bad > hi).any(axis=1)).mean() > 0.9)
    guards = json.load(open(os.path.join(d, "canary.json"), encoding="utf-8"))["guards"]
    ev["guarda_de_canary_por_segmento"] = "marked_rate_by_segment" in guards
    card = open(os.path.join(d, "model-card.md"), encoding="utf-8").read()
    ev["campos_de_la_ficha"] = sum(1 for k in CARD_FIELDS if f"## {k}" in card)
    ev["dueño_en_el_runbook"] = "Dueño:" in open(os.path.join(d, "runbook.md"), encoding="utf-8").read()
    return ev


def yt_train(X):
    return L.make_data(20000, 121)[1]


def puerta(ev):
    return [("huella del modelo coincide", ev["huella_del_modelo_coincide"]), ("reproducible bit a bit", ev["reproducible"]),
            ("AUC >= 0,80", ev["auc"] >= 0.80), ("brecha entre segmentos <= 0,05", ev["brecha_entre_segmentos"] <= 0.05),
            ("rollback exacto", ev["rollback_exacto"]), ("alerta de deriva probada", ev["alerta_de_deriva_probada"]),
            ("sin falsa alarma", ev["sin_falsa_alarma"]), ("validación bloquea la unidad errónea", ev["validacion_bloquea_unidad"]),
            ("guarda de canary por segmento", ev["guarda_de_canary_por_segmento"]), ("ficha con 10 campos", ev["campos_de_la_ficha"] >= 10),
            ("dueño en el runbook", ev["dueño_en_el_runbook"])]


def e564():
    """Construye cuatro variantes de un proyecto ML en directorios temporales, genera evidencia con comprobaciones reales y la pasa por una puerta."""
    X, y, g = L.make_data(20000, 121)
    Xt, yt, gt = L.make_data(10000, 122)
    variantes = {"completa": {},
                 "sin rollback probado": {"rollback_ok": False},
                 "monitor de deriva con umbral inalcanzable": {"drift_threshold": 5.0},
                 "sin guarda, dueño ni ficha completa": {"guard": False, "owner": False, "card_fields": 6}}
    rows, first = [], True
    for nombre, kw in variantes.items():
        with tempfile.TemporaryDirectory() as d:
            man = escribir_proyecto(d, X, y, Xt, yt, gt, **kw)
            ev = comprobar_proyecto(d, X, Xt, yt)
            if first:
                print("Evidencia de la variante completa:")
                print(json.dumps(ev, indent=1, ensure_ascii=False))
                print(f"Manifiesto: {os.path.getsize(os.path.join(d, 'manifest.json'))} bytes; modelo: {os.path.getsize(os.path.join(d, 'model-v1.pkl'))/1e3:.0f} KB")
                first = False
        reglas = puerta(ev)
        fallas = [r for r, ok in reglas if not ok]
        rows.append((nombre, f"{sum(ok for _, ok in reglas)}/{len(reglas)}", "Aprobada" if not fallas else "Bloqueada: " + "; ".join(fallas)))
    print()
    print(table(["Variante", "Comprobaciones", "Decisión"], rows))


EXPERIMENTS = {"559": e559, "560": e560, "561": e561, "562": e562, "563": e563, "564": e564}

if __name__ == "__main__":
    raise SystemExit(L.run_cli(EXPERIMENTS, "Parte 46 B: SE-559 a SE-564 (datos sintéticos de Avisos-ML, semilla 46)"))
