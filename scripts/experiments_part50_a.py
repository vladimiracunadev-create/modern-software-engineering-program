"""Experimentos de SE-601 a SE-606 (Parte 50): del ciclo de vida del modelo a servirlo.

Uso: python scripts/experiments_part50_a.py [553|554|555|556|557|558]

Datos sintéticos de *Avisos-ML* (semilla 46), numpy y scikit-learn; sin GPU ni modelos de lenguaje.
Los recuentos y las métricas con semilla se repiten; los tiempos se miden de verdad y varían.
"""
from __future__ import annotations

import heapq
import json
import os
import tempfile
import time

import numpy as np

import experiments_part50_lab as L
from experiments_part50_lab import auc, fmt, table


# ====================================================================== SE-601
def e553():
    """Un modelo bueno fuera de línea que falla en producción: cuatro causas, medidas por separado."""
    Xtr, ytr, _ = L.make_data(20000, 1)
    Xte, yte, _ = L.make_data(10000, 2)
    m = L.fit_hgb(Xtr, ytr)
    base = auc(yte, m.predict_proba(Xte)[:, 1])
    rows = [("Fuera de línea (misma distribución)", fmt(base), "—")]

    # 1. sesgo de entrenamiento-servicio: read_rate llega en porcentaje (0-100) en vez de 0-1
    Xs = Xte.copy(); Xs[:, 2] = Xs[:, 2] * 100
    a = auc(yte, m.predict_proba(Xs)[:, 1]); rows.append(("Unidad distinta en servicio (read_rate x100)", fmt(a), fmt(a - base)))
    # 2. deriva de covariables: más carga
    Xd, yd, _ = L.make_data(10000, 3, load_shift=2.5)
    a = auc(yd, m.predict_proba(Xd)[:, 1]); rows.append(("Deriva de covariables (carga +2,5 tareas)", fmt(a), fmt(a - base)))
    # 3. deriva de concepto: la historia pasada predice menos
    Xc, yc, _ = L.make_data(10000, 4, concept=0.25)
    a = auc(yc, m.predict_proba(Xc)[:, 1]); rows.append(("Deriva de concepto (peso de late_rate x0,25)", fmt(a), fmt(a - base)))
    # 4. columna nula en servicio (un valor faltante imputado con 0)
    Xn = Xte.copy(); Xn[:, 1] = 0.0
    a = auc(yte, m.predict_proba(Xn)[:, 1]); rows.append(("Fallo aguas arriba (late_rate llega en 0)", fmt(a), fmt(a - base)))
    print(table(["Situación", "AUC", "Cambio"], rows))
    rule = Xte[:, 1] + 0.05 * Xte[:, 3]
    print(f"Regla sin modelo (late_rate + 0,05 x carga): AUC {auc(yte, rule):.3f}; con late_rate en 0 la regla pierde su señal principal: {auc(yte, Xn[:, 1] + 0.05 * Xn[:, 3]):.3f}")
    # bucle de realimentación: el modelo decide a quién se le envía recordatorio y solo vemos el resultado de esos
    Xp, yp, _ = L.make_data(30000, 5)
    p = m.predict_proba(Xp)[:, 1]
    # efecto del recordatorio: reduce la probabilidad de entregar tarde a la mitad
    rng = np.random.default_rng(7)
    sent = p > 0.5
    y_obs = np.where(sent & (rng.random(len(p)) < 0.5), 0, yp)
    print(f"\nBucle de realimentación: se envía recordatorio al {sent.mean()*100:.1f} % ({sent.sum()} de {len(p)}).")
    print(f"Tasa real de entrega tardía entre los marcados: {yp[sent].mean():.3f}; observada tras recordar: {y_obs[sent].mean():.3f}")
    # reentrenar con las etiquetas observadas
    m2 = L.fit_hgb(Xp, y_obs)
    Xe, ye, _ = L.make_data(10000, 6)
    print(f"AUC del modelo original en datos sin intervención: {auc(ye, m.predict_proba(Xe)[:, 1]):.3f}")
    print(f"AUC del modelo reentrenado con etiquetas contaminadas por la intervención: {auc(ye, m2.predict_proba(Xe)[:, 1]):.3f}")
    # retraso de etiquetas: cuántas semanas hasta saber la verdad
    print(f"\nPrevalencia de entrega tardía: {yte.mean():.3f}; AUC por mes cuenta con etiqueta 7 días después de la entrega")
    # componentes: cuántos pasos distintos tiene el ciclo
    print("Componentes del ciclo (SE-601): datos, etiquetas, características, entrenamiento, evaluación, registro, despliegue, servicio, monitoreo, reentrenamiento")


# ====================================================================== SE-602
def point_in_time_join(events_t, feat_t, feat_v):
    """Para cada evento devuelve el último valor de la característica con tiempo <= t_evento."""
    idx = np.searchsorted(feat_t, events_t, side="right") - 1
    return np.where(idx >= 0, feat_v[np.clip(idx, 0, None)], np.nan)


def e554():
    rng = np.random.default_rng(54)
    # 1. fuga por el futuro: una característica construida con la etiqueta
    X, y, _ = L.make_data(20000, 11)
    Xt, yt, _ = L.make_data(10000, 12)
    clean = L.fit_hgb(X, y)
    a_clean = auc(yt, clean.predict_proba(Xt)[:, 1])
    # "entregas_tardias_ultimos_7_dias" calculada incluyendo la propia tarea (mira el futuro)
    leak_tr = np.column_stack([X, y + rng.normal(0, 0.35, len(y))])
    leak_te = np.column_stack([Xt, yt + rng.normal(0, 0.35, len(yt))])
    leaky = L.fit_hgb(leak_tr, y)
    a_leak_off = auc(yt, leaky.predict_proba(leak_te)[:, 1])
    # en producción esa característica no existe todavía: llega la media histórica
    prod = np.column_stack([Xt, np.full(len(yt), y.mean())])
    a_leak_prod = auc(yt, leaky.predict_proba(prod)[:, 1])
    print(table(["Modelo", "AUC fuera de línea", "AUC en producción"],
                [("Sin fuga", fmt(a_clean), fmt(a_clean)), ("Con característica construida con la etiqueta", fmt(a_leak_off), fmt(a_leak_prod))]))

    # 2. ruido de etiquetas
    print()
    rows = []
    Xc, yc, _ = L.make_data(20000, 13)
    Xv, yv, _ = L.make_data(10000, 14)
    for noise in (0.0, 0.05, 0.10, 0.20, 0.30, 0.40):
        _, yn, _ = L.make_data(20000, 13, label_noise=noise)
        m = L.fit_hgb(Xc, yn)
        rows.append((f"{int(noise*100)} %", fmt(auc(yv, m.predict_proba(Xv)[:, 1]))))
    print(table(["Etiquetas invertidas al azar", "AUC en datos limpios"], rows))

    # 3. unión puntual en el tiempo (point-in-time) frente a unión ingenua
    n_ev = 5000
    ev_t = np.sort(rng.uniform(0, 100, n_ev))
    ev_student = rng.integers(0, 50, n_ev)
    # cada estudiante tiene una característica que cambia cada ~10 días
    truth_rows = []
    naive, pit = [], []
    feat = {}
    for s in range(50):
        times = np.sort(rng.uniform(0, 100, 10)); vals = np.cumsum(rng.normal(0.1, 0.2, 10))
        feat[s] = (times, vals)
    exact = np.empty(n_ev); naive = np.empty(n_ev); pit = np.empty(n_ev)
    for i in range(n_ev):
        times, vals = feat[ev_student[i]]
        k = np.searchsorted(times, ev_t[i], side="right") - 1
        pit[i] = vals[k] if k >= 0 else np.nan
        naive[i] = vals[-1]     # última versión conocida hoy
        exact[i] = pit[i]
    valid = ~np.isnan(pit)
    print(f"\nUnión puntual: {int(valid.sum())} de {n_ev} eventos tienen valor; la unión ingenua usa el valor más reciente de hoy.")
    print(f"Diferencia media absoluta entre ingenua y puntual: {np.nanmean(np.abs(naive[valid]-pit[valid])):.3f}; eventos con valor distinto: {(np.abs(naive[valid]-pit[valid])>1e-9).mean()*100:.1f} %")

    # 4. sesgo entrenamiento-servicio: dos implementaciones de la misma característica
    X2, y2, _ = L.make_data(20000, 15)
    m = L.fit_hgb(X2, y2)
    Xs, ys, _ = L.make_data(10000, 16)
    base = auc(ys, m.predict_proba(Xs)[:, 1])
    rows = [("Idéntica (misma función)", fmt(base), "0,0 %")]
    Xs_a = Xs.copy(); Xs_a[:, 0] = np.round(Xs_a[:, 0] / 24) * 24     # horas redondeadas a días
    rows.append(("hours_left redondeado a días en servicio", fmt(auc(ys, m.predict_proba(Xs_a)[:, 1])), f"{(Xs_a[:,0]!=Xs[:,0]).mean()*100:.0f} %"))
    Xs_b = Xs.copy(); Xs_b[:, 3] = np.floor(Xs_b[:, 3] / 2)             # carga con otra definición
    rows.append(("load con otra definición (mitad)", fmt(auc(ys, m.predict_proba(Xs_b)[:, 1])), f"{(Xs_b[:,3]!=Xs[:,3]).mean()*100:.0f} %"))
    print()
    print(table(["Implementación en servicio", "AUC", "Valores distintos"], rows))
    # comprobación de paridad: detectar el sesgo con una muestra
    diff = [np.mean(Xs[:, j] != Xs_b[:, j]) for j in range(Xs.shape[1])]
    print("\nParidad por característica (fracción distinta) con la definición alternativa de load:", [f"{d:.2f}" for d in diff])


# ====================================================================== SE-603
def e555():
    from sklearn.ensemble import RandomForestClassifier
    X, y, _ = L.make_data(12000, 21)
    Xt, yt, _ = L.make_data(20000, 23)
    # 1. mismo código y datos: ¿se repite?
    a1 = auc(yt, L.fit_forest(X, y, seed=5).predict_proba(Xt)[:, 1])
    a2 = auc(yt, L.fit_forest(X, y, seed=5).predict_proba(Xt)[:, 1])
    print(f"Misma semilla, dos ejecuciones: {a1:.6f} y {a2:.6f}; idénticas: {a1 == a2}")
    # 2. variación con pocos datos (500 filas): por semilla del modelo y por la muestra de entrenamiento
    rng = np.random.default_rng(3)
    idx0 = rng.choice(len(X), 500, replace=False)
    seeds = [auc(yt, RandomForestClassifier(n_estimators=15, max_depth=5, random_state=s, n_jobs=1).fit(X[idx0], y[idx0]).predict_proba(Xt)[:, 1]) for s in range(40)]
    draws = []
    for s in range(40):
        idx = rng.choice(len(X), 500, replace=False)
        draws.append(auc(yt, RandomForestClassifier(n_estimators=15, max_depth=5, random_state=1, n_jobs=1).fit(X[idx], y[idx]).predict_proba(Xt)[:, 1]))
    print(f"500 filas, 40 semillas del modelo con los mismos datos: media {np.mean(seeds):.4f}, desviación {np.std(seeds, ddof=1):.4f}, rango {max(seeds)-min(seeds):.4f}")
    print(f"500 filas, 40 muestras de entrenamiento con la misma semilla: media {np.mean(draws):.4f}, desviación {np.std(draws, ddof=1):.4f}, rango {max(draws)-min(draws):.4f}")
    # 3. dos configuraciones casi iguales: ¿cuántas veces gana la mejor en una sola ejecución?
    wins, diffs = 0, []
    for s in range(60):
        idx = rng.choice(len(X), 500, replace=False)
        pa = RandomForestClassifier(n_estimators=15, max_depth=4, random_state=s, n_jobs=1).fit(X[idx], y[idx]).predict_proba(Xt)[:, 1]
        pb = RandomForestClassifier(n_estimators=15, max_depth=5, random_state=s + 500, n_jobs=1).fit(X[idx], y[idx]).predict_proba(Xt)[:, 1]
        da = auc(yt, pb) - auc(yt, pa); diffs.append(da); wins += da > 0
    print(f"Profundidad 5 frente a 4 con 500 filas: diferencia media {np.mean(diffs):+.4f}, desviación {np.std(diffs, ddof=1):.4f}; la 5 gana {wins} de 60 comparaciones de una sola ejecución")
    # 4. optimismo de la selección: el mejor de N candidatos casi idénticos medido en una validación pequeña
    res = []
    for n_cfg in (1, 5, 20, 80):
        gaps = []
        for rep in range(40):
            r = np.random.default_rng(1000 + rep)
            Xv, yv, _ = L.make_data(300, 5000 + rep)
            best_v, best_t = -1, 0
            for c in range(n_cfg):
                ib = r.choice(len(X), 800, replace=True)
                mdl = L.fit_logistic(X[ib], y[ib], C=float(10 ** r.uniform(-2, 1)))
                v = auc(yv, mdl.predict_proba(Xv)[:, 1])
                if v > best_v:
                    best_v, best_t = v, auc(yt, mdl.predict_proba(Xt)[:, 1])
            gaps.append(best_v - best_t)
        res.append((n_cfg, fmt(np.mean(gaps), 4)))
    print()
    print(table(["Candidatos probados", "AUC de validación menos AUC de prueba del elegido (media de 40 repeticiones)"], res))
    # 5. registro de la corrida
    cfg = {"model": "forest", "n": 60, "depth": 8, "seed": 5, "features": L.FEATURES}
    rec = {"data_sha": L.sha(X), "label_sha": L.sha(y), "config_sha": L.sha(cfg), "auc_test": round(a1, 6), "versions": L.check_versions()}
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "run.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(rec, f, indent=1, ensure_ascii=False)
        size = os.path.getsize(p)
    print(f"\nRegistro de corrida: {size} bytes, huellas data={rec['data_sha']} etiquetas={rec['label_sha']} config={rec['config_sha']}")
    X2, y2, _ = L.make_data(12000, 21)
    print(f"Regenerar los datos con la misma semilla da la misma huella: {L.sha(X2) == rec['data_sha']}")
    X3, _, _ = L.make_data(12000, 22)
    print(f"Con otra semilla la huella cambia: {L.sha(X3) != rec['data_sha']}")


# ====================================================================== SE-604
def reliability(y, p, bins=10):
    edges = np.linspace(0, 1, bins + 1)
    ece, rows = 0.0, []
    for i in range(bins):
        m = (p >= edges[i]) & (p < edges[i + 1] if i < bins - 1 else p <= 1)
        if m.sum() == 0:
            continue
        ece += m.mean() * abs(y[m].mean() - p[m].mean())
        rows.append((edges[i], edges[i + 1], int(m.sum()), float(p[m].mean()), float(y[m].mean())))
    return ece, rows


def e556():
    from sklearn.metrics import average_precision_score, precision_score, recall_score, accuracy_score, brier_score_loss
    X, y, g = L.make_data(30000, 31, group_gap=0.6)
    Xt, yt, gt = L.make_data(20000, 32, group_gap=0.6)
    m = L.fit_hgb(X, y)
    p = m.predict_proba(Xt)[:, 1]
    print(f"Prevalencia de entrega tardía: {yt.mean():.3f}; AUC {auc(yt, p):.3f}; PR-AUC {average_precision_score(yt, p):.3f}; Brier {brier_score_loss(yt, p):.3f}")
    # exactitud frente a un clasificador trivial con prevalencia baja
    Xr, yr, _ = L.make_data(60000, 33, intercept=-4.4)
    Xrt, yrt, _ = L.make_data(30000, 34, intercept=-4.4)
    mr = L.fit_hgb(Xr, yr)
    pr = mr.predict_proba(Xrt)[:, 1]
    print(f"\nPrevalencia baja: {yrt.mean():.3f}. Exactitud del modelo {accuracy_score(yrt, pr>0.5):.3f}; clasificador que siempre dice 0: {accuracy_score(yrt, np.zeros_like(yrt)):.3f}; recall del modelo a 0,5: {recall_score(yrt, pr>0.5):.3f}; AUC {auc(yrt, pr):.3f}; PR-AUC {average_precision_score(yrt, pr):.3f}")
    # umbral por costo
    print()
    rows = []
    for c_fn in (1, 5, 10):
        best = None
        for th in np.linspace(0.02, 0.9, 89):
            pred = p > th
            fp = int(((pred == 1) & (yt == 0)).sum()); fn = int(((pred == 0) & (yt == 1)).sum())
            cost = fp * 1 + fn * c_fn
            if best is None or cost < best[0]:
                best = (cost, th, fp, fn)
        rows.append((f"1 : {c_fn}", fmt(best[1], 2), best[2], best[3], best[0]))
    print(table(["Costo FP : FN", "Umbral óptimo", "FP", "FN", "Costo total"], rows))
    # calibración
    ece, rel = reliability(yt, p)
    print(f"\nECE del modelo de boosting: {ece:.4f}")
    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier(n_estimators=60, max_depth=None, min_samples_leaf=1, random_state=3, n_jobs=1).fit(X, y)
    prf = rf.predict_proba(Xt)[:, 1]
    print(f"ECE del bosque sin podar: {reliability(yt, prf)[0]:.4f}; AUC {auc(yt, prf):.3f}")
    from sklearn.isotonic import IsotonicRegression
    iso = IsotonicRegression(out_of_bounds="clip").fit(rf.predict_proba(Xt[:10000])[:, 1], yt[:10000])
    prf2 = iso.predict(prf[10000:])
    print(f"ECE del bosque tras calibrar isotónica con otra muestra: {reliability(yt[10000:], prf2)[0]:.4f}; antes en esa mitad: {reliability(yt[10000:], prf[10000:])[0]:.4f}")
    # subgrupos
    print()
    rows = []
    for gi in (0, 1):
        mk = gt == gi
        pred = p[mk] > 0.35
        tpr = recall_score(yt[mk], pred); fpr = ((pred == 1) & (yt[mk] == 0)).sum() / (yt[mk] == 0).sum()
        rows.append((f"Grupo {gi}", int(mk.sum()), fmt(yt[mk].mean()), fmt(auc(yt[mk], p[mk])), fmt(tpr), fmt(fpr), fmt(pred.mean())))
    print(table(["Grupo", "n", "Prevalencia", "AUC", "TPR", "FPR", "Tasa de marcados"], rows))
    r = (p[gt == 1] > 0.35).mean() / (p[gt == 0] > 0.35).mean()
    print(f"Razón de tasas de marcados (grupo 1 / grupo 0): {r:.2f}")
    # intervalos bootstrap
    rng = np.random.default_rng(5)
    for n in (200, 2000, 20000):
        idx = rng.choice(len(yt), n, replace=False)
        bs = [auc(yt[idx][b], p[idx][b]) for b in (rng.integers(0, n, n) for _ in range(200))]
        lo, hi = np.percentile(bs, [2.5, 97.5])
        print(f"n={n}: AUC {auc(yt[idx], p[idx]):.3f} intervalo 95 % [{lo:.3f}, {hi:.3f}] ancho {hi-lo:.3f}")
    # validación temporal frente a aleatoria con deriva
    parts = [L.make_data(8000, 40 + k, load_shift=0.4 * k, concept=1.0 - 0.12 * k) for k in range(6)]
    Xa = np.vstack([q[0] for q in parts[:4]]); ya = np.concatenate([q[1] for q in parts[:4]])
    mt = L.fit_hgb(Xa[:24000], ya[:24000])
    rand_idx = np.random.default_rng(1).permutation(len(Xa)); cut = int(0.75 * len(Xa))
    mr2 = L.fit_hgb(Xa[rand_idx[:cut]], ya[rand_idx[:cut]])
    a_rand = auc(ya[rand_idx[cut:]], mr2.predict_proba(Xa[rand_idx[cut:]])[:, 1])
    a_temp = auc(parts[3][1], mt.predict_proba(parts[3][0])[:, 1])
    a_future = auc(parts[5][1], mr2.predict_proba(parts[5][0])[:, 1])
    print(f"\nValidación aleatoria sobre el pasado: AUC {a_rand:.3f}; validación temporal (último periodo): {a_temp:.3f}; el mismo modelo en el periodo futuro: {a_future:.3f}")


# ====================================================================== SE-605
def e557():
    from sklearn.linear_model import SGDClassifier
    from sklearn.preprocessing import StandardScaler
    # Dominio fuente: otras universidades (mucho dato); destino: una universidad nueva con otro peso de late_rate
    Xs, ys, _ = L.make_data(40000, 51)
    sc = StandardScaler().fit(Xs)
    Xt_all, yt_all, _ = L.make_data(20000, 52, concept=0.7, load_shift=0.6, intercept=-1.0)
    Xe, ye, _ = L.make_data(10000, 53, concept=0.7, load_shift=0.6, intercept=-1.0)
    base = SGDClassifier(loss="log_loss", alpha=1e-4, random_state=1, max_iter=1, tol=None)
    ep_src = 30
    t0 = time.perf_counter()
    for _ in range(ep_src):
        base.partial_fit(sc.transform(Xs), ys, classes=[0, 1])
    t_src = time.perf_counter() - t0
    a_src_on_tgt = auc(ye, base.decision_function(sc.transform(Xe)))
    a_src_on_src = auc(L.make_data(10000, 54)[1], base.decision_function(sc.transform(L.make_data(10000, 54)[0])))
    print(f"Modelo base: {ep_src} épocas sobre {len(Xs)} filas en {t_src:.2f} s; AUC en fuente {a_src_on_src:.3f}; en el dominio nuevo sin adaptar {a_src_on_tgt:.3f}")
    rows = []
    import copy
    for n in (50, 200, 1000, 5000, 20000):
        Xn, yn = sc.transform(Xt_all[:n]), yt_all[:n]
        # desde cero
        s = SGDClassifier(loss="log_loss", alpha=1e-4, random_state=1, max_iter=1, tol=None)
        t0 = time.perf_counter()
        for _ in range(20):
            s.partial_fit(Xn, yn, classes=[0, 1])
        t_s = time.perf_counter() - t0
        a_s = auc(ye, s.decision_function(sc.transform(Xe)))
        # ajuste fino desde el modelo base, pocas épocas y paso pequeño
        b = copy.deepcopy(base)
        b.set_params(eta0=0.01, learning_rate="constant")
        t0 = time.perf_counter()
        for _ in range(5):
            b.partial_fit(Xn, yn)
        t_b = time.perf_counter() - t0
        a_b = auc(ye, b.decision_function(sc.transform(Xe)))
        a_forget = auc(L.make_data(10000, 54)[1], b.decision_function(sc.transform(L.make_data(10000, 54)[0])))
        rows.append((n, fmt(a_s), fmt(a_b), fmt(a_forget), fmt(t_s * 1000, 1), fmt(t_b * 1000, 1)))
    print()
    print(table(["Filas del dominio nuevo", "AUC desde cero", "AUC ajuste fino", "AUC del ajustado en la fuente", "ms desde cero", "ms ajuste"], rows))
    # costo en parámetros de una adaptación de rango bajo (aritmética)
    print("\nParámetros entrenables de una capa d x k con adaptación de rango r (d=k=4096):")
    d = k = 4096
    for r in (4, 8, 16, 64):
        print(f"r={r}: {r*(d+k):,} de {d*k:,} = {r*(d+k)/(d*k)*100:.2f} %".replace(",", "."))
    # presupuesto de cómputo: aproximación 6 * N * D
    print("\nCómputo aproximado de entrenamiento (6 N D) para N parámetros y D tokens (aproximación de Kaplan y colaboradores):")
    for N, D in ((7e9, 1e12), (7e9, 1e9), (7e9, 1e7)):
        fl = 6 * N * D
        print(f"N={N:.0e}, D={D:.0e}: {fl:.2e} operaciones; a 1e14 operaciones/s sostenidas: {fl/1e14/3600:.1f} horas")
    # modelo pequeño de verdad: tiempo del boosting por tamaño
    print()
    rows = []
    for n in (1000, 4000, 16000, 64000):
        Xn, yn, _ = L.make_data(n, 55)
        t = L.timed(lambda: L.fit_hgb(Xn, yn), 3)
        rows.append((n, fmt(t * 1000, 0)))
    print(table(["Filas", "ms de entrenamiento (HGB, 80 iteraciones)"], rows))


# ====================================================================== SE-606
def e558():
    X, y, _ = L.make_data(20000, 61)
    rng = np.random.default_rng(4)
    d = X.shape[1]
    # modelo servido como producto matricial: una red pequeña con pesos fijos (misma forma que sirve un modelo real)
    W1 = rng.normal(0, 0.3, (d, 256)).astype(np.float32); W2 = rng.normal(0, 0.1, (256, 256)).astype(np.float32); W3 = rng.normal(0, 0.1, (256, 1)).astype(np.float32)

    def forward(a):
        h = np.maximum(a @ W1, 0); h = np.maximum(h @ W2, 0); return h @ W3
    Xf = ((X - X.mean(axis=0)) / X.std(axis=0)).astype(np.float32)      # entradas estandarizadas, como las vería el servicio
    rows = []
    t1 = None
    for b in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024):
        batch = Xf[:b]
        t = L.timed(lambda: forward(batch), 40)
        t1 = t if b == 1 else t1
        rows.append((b, fmt(t * 1e6, 1), fmt(t / b * 1e6, 2), fmt(b / t, 0)))
    print(table(["Lote", "µs por lote", "µs por petición", "peticiones/s"], rows))
    s = {int(r[0]): float(r[1].replace(",", ".")) * 1e-6 for r in rows}
    # ajuste lineal del tiempo de servicio s(b) = a + c b
    bs = np.array(sorted(s)); ts = np.array([s[b] for b in bs])
    svc = lambda b: float(np.interp(b, bs, ts))      # tiempo de servicio medido, interpolado
    t1, tmax = svc(1), svc(256)
    print(f"\nTiempo de servicio medido: 1 petición {t1*1e6:.1f} µs; lote de 256 {tmax*1e6:.1f} µs ({tmax/256*1e6:.2f} µs por petición, {t1/(tmax/256):.1f} veces menos)")
    # simulación de lote dinámico: llegadas Poisson, espera máxima w, lote máximo B
    def sim(rate, wait, B, n=40000, seed=3):
        r = np.random.default_rng(seed)
        arr = np.cumsum(r.exponential(1 / rate, n))
        free = 0.0; i = 0; lat = []
        while i < n:
            t0 = max(arr[i], free)
            deadline = arr[i] + wait
            j = i
            while j < n and j - i < B and arr[j] <= max(deadline, t0):
                j += 1
            j = max(j, i + 1)
            start = max(t0, min(deadline, arr[j - 1])) if j - i < B else max(t0, arr[j - 1])
            start = max(start, arr[j - 1])
            done = start + svc(j - i)
            lat.extend(done - arr[i:j])
            free = done; i = j
        lat = np.array(lat)
        return np.percentile(lat, 50) * 1e3, np.percentile(lat, 99) * 1e3, n / (free)
    print()
    rows = []
    rate = 0.8 / svc(1)            # 80 % de la capacidad sin lote
    for wait, B in ((0.0, 1), (0.0005, 8), (0.002, 32), (0.005, 64), (0.020, 256)):
        p50, p99, thr = sim(rate, wait, B)
        rows.append((f"{wait*1000:.1f} ms / {B}", fmt(p50, 2), fmt(p99, 2), fmt(thr, 0)))
    print(f"Tasa de llegada: {rate:.0f}/s (80 % de la capacidad sin lotes: {1/svc(1):.0f}/s)")
    print(table(["Espera máx. / lote máx.", "p50 ms", "p99 ms", "peticiones/s servidas"], rows))
    rows = []
    for mult in (1.0, 2.0, 4.0):
        rate2 = mult * 1.0 / svc(1)  # superior a la capacidad sin lote
        p50, p99, thr = sim(rate2, 0.002, 64)
        p50n, p99n, thrn = sim(rate2, 0.0, 1)
        rows.append((f"{mult:.0f}x capacidad sin lotes", fmt(p99n, 1), fmt(p99, 2)))
    print()
    print(table(["Carga", "p99 ms sin lotes", "p99 ms con lote dinámico (2 ms / 64)"], rows))
    # cuantización de pesos
    from sklearn.ensemble import HistGradientBoostingClassifier
    Xt, yt, _ = L.make_data(10000, 62)
    m = L.fit_logistic(X, y)
    coef = m[-1].coef_.ravel(); icp = m[-1].intercept_
    sc = m[0]
    Z = sc.transform(Xt)
    ref = Z @ coef + icp
    print()
    rows = [("float64", coef.nbytes, fmt(auc(yt, ref)), "0")]
    for bits, dt in ((16, np.float16), (8, np.int8)):
        if dt is np.int8:
            scale = np.abs(coef).max() / 127
            q = np.round(coef / scale).astype(np.int8); w = q.astype(np.float64) * scale
        else:
            q = coef.astype(dt); w = q.astype(np.float64)
        out = Z @ w + icp
        rows.append((f"{dt.__name__}", q.nbytes, fmt(auc(yt, out)), f"{np.mean(np.abs(out-ref)):.5f}"))
    print(table(["Pesos", "Bytes de pesos", "AUC", "Error medio en la salida"], rows))
    # arranque en frío: cargar un modelo serializado
    import pickle
    big = L.fit_forest(X, y, n=60, depth=None)
    blob = pickle.dumps(big)
    t = L.timed(lambda: pickle.loads(blob), 5)  # nosec B301 - bytes producidos por este mismo proceso
    print(f"\nBosque de 60 árboles serializado: {len(blob)/1e6:.1f} MB; carga {t*1000:.0f} ms; una predicción individual: {L.timed(lambda: big.predict_proba(Xt[:1]), 15)*1e6:.0f} µs; en lote de 1024: {L.timed(lambda: big.predict_proba(Xt[:1024]), 7)/1024*1e6:.1f} µs por petición")


EXPERIMENTS = {"553": e553, "554": e554, "555": e555, "556": e556, "557": e557, "558": e558}

if __name__ == "__main__":
    raise SystemExit(L.run_cli(EXPERIMENTS, "Parte 50 A: SE-601 a SE-606 (datos sintéticos de Avisos-ML, semilla 46)"))
