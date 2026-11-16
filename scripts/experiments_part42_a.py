"""Experimentos de las clases SE-505 a SE-510 (Parte 42): patrones agénticos y sistemas con LLM.

Uso: python scripts/experiments_part42_a.py [505|506|507|508|509|510]

No se invoca ningún modelo de lenguaje: el modelo es un componente sintético con semilla fija y tasa de
error declarada. Son código real y medido: las herramientas, el router, el verificador, la recuperación
sobre el corpus de las Partes 39 y 40 y los hilos de la paralelización.
"""
from __future__ import annotations

import math
import re
import sys
import time
import unicodedata
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from experiments_part42_lab import Meter, approx_tokens, mean, num, pct, quantile, rng, table

ROOT = Path(__file__).resolve().parents[1]


# ====================================================================== SE-505
def exp505(n: int = 2000, seed: int = 42, p_wrong: float = 0.08, p_fatal: float = 0.01, max_steps: int = 10) -> dict:
    """Workflow fijo frente a agente en tres clases de solicitud de Avisos; modelo sintético con semilla."""
    r = rng(seed)
    kinds = [("plazo", 0.60, 1), ("silencio", 0.25, 3), ("incidencia", 0.15, None)]
    out = {k: {"wf_calls": [], "wf_tok": [], "wf_ok": [], "ag_calls": [], "ag_tok": [], "ag_ok": []} for k, _, _ in kinds}
    for _ in range(n):
        x = r.random()
        acc = 0.0
        for kind, share, need in kinds:
            acc += share
            if x <= acc:
                break
        need = need if need is not None else r.randint(3, 8)
        d = out[kind]
        # workflow: clasificar (1 llamada) + redactar (1 llamada); las herramientas son código fijo
        if kind == "incidencia":
            d["wf_calls"].append(2)
            d["wf_tok"].append(2 * (300 + 60))
            d["wf_ok"].append(False)  # el camino no se puede fijar: se escala a una persona
        else:
            m = Meter()
            m.call(300)
            m.call(300 + 40 * need)
            d["wf_calls"].append(m.calls)
            d["wf_tok"].append(m.tokens)
            d["wf_ok"].append(True)
        # agente: un paso por llamada, cada llamada vuelve a leer todo el historial
        m = Meter()
        done = 0
        fatal = False
        steps = 0
        while done < need and steps < max_steps:
            m.call(300 + 120 * steps)
            steps += 1
            if r.random() < p_fatal:
                fatal = True
                break
            if r.random() < p_wrong:
                continue  # acción equivocada: un paso gastado
            done += 1
        if not fatal and done == need and steps < max_steps:
            m.call(300 + 120 * steps)  # llamada final que redacta la respuesta
        d["ag_calls"].append(m.calls)
        d["ag_tok"].append(m.tokens)
        d["ag_ok"].append(not fatal and done == need and steps < max_steps)
    rows = []
    for kind, share, _ in kinds:
        d = out[kind]
        rows.append([kind, pct(share, 0), num(mean(d["wf_calls"])), pct(mean(d["wf_ok"])), num(mean(d["ag_calls"])),
                     num(quantile(d["ag_calls"], 0.95), 0), pct(mean(d["ag_ok"])), num(mean(d["ag_tok"]) / max(1, mean(d["wf_tok"])))])
    total_h_ok = sum(share * (mean(out[k]["ag_ok"]) if k == "incidencia" else mean(out[k]["wf_ok"])) for k, share, _ in kinds)
    total_ag_ok = sum(share * mean(out[k]["ag_ok"]) for k, share, _ in kinds)
    total_wf_ok = sum(share * mean(out[k]["wf_ok"]) for k, share, _ in kinds)
    tok_h = sum(share * (mean(out[k]["ag_tok"]) if k == "incidencia" else mean(out[k]["wf_tok"])) for k, share, _ in kinds)
    tok_ag = sum(share * mean(out[k]["ag_tok"]) for k, share, _ in kinds)
    tok_wf = sum(share * mean(out[k]["wf_tok"]) for k, share, _ in kinds)
    print("SE-505 — workflow fijo frente a agente (modelo sintético, semilla", seed, ")")
    table([["tipo", "peso", "llamadas wf", "éxito wf", "llamadas agente", "p95 agente", "éxito agente", "tokens agente / wf"]] + rows)
    print("  éxito global: workflow", pct(total_wf_ok), "| agente", pct(total_ag_ok), "| híbrido", pct(total_h_ok))
    print("  tokens medios por solicitud: workflow", round(tok_wf), "| agente", round(tok_ag), "| híbrido", round(tok_h))
    return {"rows": rows, "ok": (total_wf_ok, total_ag_ok, total_h_ok), "tok": (tok_wf, tok_ag, tok_h)}


# ====================================================================== SE-506
INTENTS = {
    "plazo": ["cuándo vence la entrega de {c}", "fecha límite del curso {c}", "hasta qué día puedo entregar {c}", "plazo de entrega {c}"],
    "silencio": ["silencia los avisos de {c}", "no quiero recordatorios de {c}", "pausa las notificaciones de {c}", "apaga los avisos {c}"],
    "baja": ["quiero darme de baja de {c}", "cómo cancelo mi matrícula en {c}", "retirarme del curso {c}", "dar de baja {c}"],
    "queja": ["el aviso de {c} llegó equivocado", "recibí un recordatorio duplicado de {c}", "me llegó un aviso tarde en {c}", "aviso incorrecto de {c}"],
}


def _norm(text: str) -> list[str]:
    s = unicodedata.normalize("NFKD", text.lower()).encode("ascii", "ignore").decode()
    return re.findall(r"[a-z0-9]+", s)


def _typo(word: str, r) -> str:
    if len(word) < 5:
        return word
    i = r.randrange(1, len(word) - 2)
    return word[:i] + word[i + 1] + word[i] + word[i + 2:]


def make_requests(n: int, seed: int, noise: float):
    r = rng(seed)
    courses = ["c1", "c2", "c3", "c4", "c5"]
    reqs = []
    for _ in range(n):
        intent = r.choice(list(INTENTS))
        words = r.choice(INTENTS[intent]).format(c=r.choice(courses)).split()
        words = [_typo(w, r) if r.random() < noise else w for w in words]
        if r.random() < noise:
            words.insert(r.randrange(len(words) + 1), r.choice(["por favor", "urgente", "hola", "gracias"]))
        reqs.append((" ".join(words), intent))
    return reqs


KEYWORDS = {"plazo": ["vence", "fecha limite", "plazo", "hasta que dia"], "silencio": ["silencia", "recordatorios", "notificaciones", "apaga"],
            "baja": ["baja", "cancelo", "retirarme", "matricula"], "queja": ["equivocado", "duplicado", "tarde", "incorrecto"]}


def keyword_router(text: str):
    t = " ".join(_norm(text))
    scores = {k: sum(1 for w in ws if w in t) for k, ws in KEYWORDS.items()}
    best = max(scores, key=scores.get)
    return (best, float(scores[best])) if scores[best] else (None, 0.0)


class CentroidRouter:
    """Vecino más cercano al centroide con TF-IDF de trigramas de caracteres, entrenado con pocos ejemplos."""

    def __init__(self, examples):
        self.df = Counter()
        docs = defaultdict(Counter)
        for text, label in examples:
            grams = self._grams(text)
            docs[label].update(grams)
            self.df.update(set(grams))
        self.n = len(examples)
        self.cent = {k: self._vec(c) for k, c in docs.items()}

    @staticmethod
    def _grams(text: str):
        s = " ".join(_norm(text))
        s = f"  {s}  "
        return [s[i:i + 3] for i in range(len(s) - 2)]

    def _vec(self, counts):
        v = {g: (1 + math.log(c)) * math.log((1 + self.n) / (1 + self.df.get(g, 0)) + 1) for g, c in counts.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {g: x / norm for g, x in v.items()}

    def route(self, text: str):
        v = self._vec(Counter(self._grams(text)))
        scores = {k: sum(x * c.get(g, 0.0) for g, x in v.items()) for k, c in self.cent.items()}
        best = max(scores, key=scores.get)
        return best, scores[best]


def exp506() -> dict:
    out = {}
    # (a) encadenado: éxito de una cadena de 3 pasos con y sin puerta programática
    r = rng(7)
    s, trials = 0.95, 20000
    plain = sum(all(r.random() < s for _ in range(3)) for _ in range(trials)) / trials
    gated_ok, extra = 0, 0
    for _ in range(trials):
        ok = True
        for _step in range(3):
            if r.random() < s:
                continue
            extra += 1  # la puerta detecta el error con prob. 0,90 y se reintenta una vez
            if r.random() < 0.90 and r.random() < s:
                continue
            ok = False
            break
        gated_ok += ok
    out["chain"] = (plain, gated_ok / trials, extra / trials)
    print("SE-506 (a) cadena de 3 pasos, éxito por paso 0,95: sin puerta", pct(plain), "| con puerta y un reintento", pct(gated_ok / trials), "| reintentos por ejecución", num(extra / trials, 3))
    # (b) enrutamiento: palabras clave frente a centroide de trigramas, con y sin ruido, y delegación a persona
    train = []
    for intent, plantillas in INTENTS.items():
        for p in plantillas[:2]:
            train.append((p.format(c="c1"), intent))
    cen = CentroidRouter(train)
    rows = []
    for noise in (0.0, 0.3, 0.6):
        test = make_requests(2000, 11, noise)
        kw_ok = sum(1 for t, y in test if keyword_router(t)[0] == y)
        kw_unk = sum(1 for t, y in test if keyword_router(t)[0] is None)
        ce_ok = sum(1 for t, y in test if cen.route(t)[0] == y)
        sel = [(cen.route(t), y) for t, y in test]
        kept = [(lab, y) for (lab, sc), y in sel if sc >= 0.35]
        sel_acc = mean([lab == y for lab, y in kept]) if kept else 0.0
        rows.append((noise, kw_ok / len(test), kw_unk / len(test), ce_ok / len(test), len(kept) / len(test), sel_acc))
    out["routing"] = rows
    print("SE-506 (b) enrutamiento sobre 2000 solicitudes (intención correcta)")
    table([["ruido", "palabras clave", "sin ruta (pal. clave)", "centroide", "cobertura umbral 0,35", "acierto con umbral"]] +
          [[pct(a, 0), pct(b), pct(c), pct(d), pct(e), pct(f)] for a, b, c, d, e, f in rows])
    # (c) paralelización con hilos reales: 8 subtareas independientes de 50 ms de espera
    def work(i):
        time.sleep(0.05)
        return i
    t0 = time.perf_counter()
    for i in range(8):
        work(i)
    seq = time.perf_counter() - t0
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=8) as ex:
        list(ex.map(work, range(8)))
    par = time.perf_counter() - t0
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=2) as ex:
        list(ex.map(work, range(8)))
    par2 = time.perf_counter() - t0
    out["parallel"] = (seq, par, par2)
    print("SE-506 (c) 8 subtareas de 50 ms: secuencial", num(seq * 1000, 0), "ms | 8 hilos", num(par * 1000, 0), "ms | 2 hilos", num(par2 * 1000, 0), "ms (reloj real, varía)")
    # (d) votación: 5 muestras con acierto 0,80; independientes frente a correlacionadas
    r = rng(5)
    ind = corr = 0
    trials = 20000
    for _ in range(trials):
        votes = sum(r.random() < 0.8 for _ in range(5))
        ind += votes >= 3
        # correlacionadas: con prob. 0,5 las cinco comparten el mismo sesgo (todas aciertan o todas fallan)
        if r.random() < 0.5:
            c = (r.random() < 0.8) * 5
        else:
            c = sum(r.random() < 0.8 for _ in range(5))
        corr += c >= 3
    out["vote"] = (ind / trials, corr / trials)
    print("SE-506 (d) votación de 5 con acierto 0,80 por muestra: independientes", pct(ind / trials), "| correlacionadas", pct(corr / trials))
    return out


# ====================================================================== SE-507
def exp507(seed: int = 3) -> dict:
    r = rng(seed)
    results = []
    for label, skew in (("uniforme", False), ("sesgada", True)):
        spans_static, spans_dyn, solos = [], [], []
        for _ in range(500):
            k = r.randint(4, 12)
            sizes = [r.choice([5, 5, 8, 10]) for _ in range(k)] if not skew else [int(r.paretovariate(1.2) * 5) + 2 for _ in range(k)]
            sizes = [min(s, 200) for s in sizes]
            static = [0, 0, 0]
            for i, s in enumerate(sizes):
                static[i % 3] += s
            dyn = [0, 0, 0]
            for s in sorted(sizes, reverse=True):
                dyn[dyn.index(min(dyn))] += s
            spans_static.append(max(static))
            spans_dyn.append(max(dyn))
            solos.append(sum(sizes))
        results.append((label, mean(solos), mean(spans_static), mean(spans_dyn)))
    print("SE-507 (a) tiempo de reloj en unidades de trabajo (3 trabajadores; el orquestador suma 2 llamadas de coordinación)")
    table([["carga", "un solo agente", "reparto fijo", "orquestador (LPT)"]] + [[a, num(b), num(c), num(d)] for a, b, c, d in results])
    # (b) evaluador-optimizador sobre un aviso con cuatro restricciones verificables
    def check(text: str, course: str, due: str) -> set[str]:
        bad = set()
        if len(text) > 160:
            bad.add("longitud")
        if course not in text:
            bad.add("curso")
        if not re.search(r"\b\d{4}-\d{2}-\d{2}\b", text) or due not in text:
            bad.add("fecha")
        if re.search(r"(?i)\burgente\b|!!", text):
            bad.add("tono")
        return bad
    def render(ok: dict, course: str, due: str) -> str:
        text = [f"Aviso: entrega de {course}" if ok["curso"] else "Aviso: entrega pendiente",
                f"vence {due}" if ok["fecha"] else "vence pronto",
                "Revisa tu entrega." if ok["tono"] else "¡URGENTE!!"]
        t = " ".join(text)
        if not ok["longitud"]:
            t += " " + "Recuerda que entregar a tiempo evita penalizaciones y facilita la corrección. " * 2
        return t
    base = {"curso": 0.15, "fecha": 0.25, "tono": 0.30, "longitud": 0.20}
    r = rng(99)
    def run(evaluator, iters):
        good = 0
        calls = 0
        for _ in range(1500):
            course, due = "c3", "2026-11-20"
            ok = {c: r.random() >= p for c, p in base.items()}
            text = render(ok, course, due)
            calls += 1
            for _i in range(iters):
                truth = check(text, course, due)
                if evaluator == "programático":
                    found = truth
                else:  # juez ruidoso: detecta cada falla real con prob. 0,70 y acusa falsas con prob. 0,15
                    found = {c for c in truth if r.random() < 0.70} | {c for c in base if c not in truth and r.random() < 0.15}
                if not found:
                    break
                for c in base:  # el generador corrige lo señalado con prob. 0,80 y estropea con prob. 0,03 lo que estaba bien
                    if c in found:
                        ok[c] = (r.random() >= 0.10) if ok[c] else (r.random() < 0.80)
                    elif ok[c] and r.random() < 0.03:
                        ok[c] = False
                text = render(ok, course, due)
                calls += 1
            good += not check(text, course, due)
        return good / 1500, calls / 1500
    rows = []
    for ev in ("programático", "juez ruidoso"):
        for it in (0, 1, 2, 3):
            ok_rate, c = run(ev, it)
            rows.append((ev, it, ok_rate, c))
    print("SE-507 (b) aviso con 4 restricciones: éxito verificado y generaciones por aviso")
    table([["evaluador", "iteraciones", "pasa el verificador", "generaciones medias"]] + [[a, b, pct(c), num(d, 2)] for a, b, c, d in rows])
    return {"load": results, "ev": rows}


# ====================================================================== SE-508
def exp508(episodes: int = 3000, seed: int = 8, eps: float = 0.05) -> dict:
    """Entorno real: avisar a los pendientes de un curso; algunos contactos faltan o el estudiante se cambió de curso."""
    out = []
    for q in (0.0, 0.15, 0.35):
        r = rng(seed)
        stats = {k: {"ok": 0, "calls": 0} for k in ("react", "plan", "plan+replan", "plan+reflexion")}
        for _ in range(episodes):
            n = r.randint(2, 4)
            students = [{"contact": r.random() >= q, "moved": r.random() < q / 3} for _ in range(n)]
            goal = {i for i, s in enumerate(students) if not s["moved"]}
            wrong = [r.random() < eps for _ in range(4 * n + 4)]
            surprises = sum(1 for st in students if (not st["contact"]) or st["moved"])
            # react: una llamada por acción; adapta cada hecho inesperado con una llamada más; cada llamada puede ser fatal (1 %)
            rc = 1 + n * 3 + sum(wrong[: n * 3]) + surprises
            stats["react"]["calls"] += rc
            stats["react"]["ok"] += all(r.random() >= 0.01 for _ in range(rc))
            # plan-and-execute: 1 llamada planifica; el resto es código; no tolera hechos inesperados
            stats["plan"]["calls"] += 1
            stats["plan"]["ok"] += surprises == 0
            # con replanificación: una llamada por hecho inesperado, que acierta con prob. 0,90
            stats["plan+replan"]["calls"] += 1 + surprises
            stats["plan+replan"]["ok"] += all(r.random() < 0.90 for _ in range(surprises))
            # con reflexión: el primer intento falla si hay sorpresa; 1 llamada de reflexión y un segundo plan que acierta con prob. 0,85
            if surprises:
                stats["plan+reflexion"]["calls"] += 1 + 1 + 1 + surprises
                stats["plan+reflexion"]["ok"] += r.random() < 0.85
            else:
                stats["plan+reflexion"]["calls"] += 1
                stats["plan+reflexion"]["ok"] += 1
        out.append((q, {k: (v["ok"] / episodes, v["calls"] / episodes) for k, v in stats.items()}))
    print("SE-508 estrategias en un entorno con sorpresas (semilla", seed, ")")
    table([["tasa de sorpresas", "ReAct", "plan", "plan + replanificación", "plan + reflexión"]] +
          [[pct(q, 0)] + [f"{pct(v[k][0])} / {num(v[k][1])} llamadas" for k in ("react", "plan", "plan+replan", "plan+reflexion")] for q, v in out])
    return {"rows": out}


# ====================================================================== SE-509
def exp509(seed: int = 21) -> dict:
    r = rng(seed)
    results = {k: [] for k in ("contexto completo", "ventana deslizante", "resumen con pérdidas", "almacén sin versión", "almacén versionado")}
    toks = {k: [] for k in results}
    for _ in range(300):
        turns = []
        facts = {}
        for t in range(80):
            if r.random() < 0.25:
                key = f"curso{r.randint(1, 12)}"
                val = f"día {r.randint(1, 28)}"
                facts[key] = val
                turns.append((t, "hecho", key, val, f"Silencia {key} hasta el {val}. " + "Gracias por la ayuda con el resto del trabajo. " * 3))
            else:
                turns.append((t, "charla", None, None, "Seguimos con la revisión de entregas de la semana, nada nuevo que anotar. " * 3))
        asked = list(facts.items())
        per = {k: 0 for k in results}
        # contexto completo con presupuesto de 2000 tokens: pierde lo más antiguo
        budget = 2000
        kept, total = [], 0
        for turn in reversed(turns):
            c = approx_tokens(turn[4])
            if total + c > budget:
                break
            kept.append(turn)
            total += c
        latest = {}
        for turn in sorted(kept):
            if turn[1] == "hecho":
                latest[turn[2]] = turn[3]
        per["contexto completo"] = sum(latest.get(k) == v for k, v in asked)
        toks["contexto completo"].append(total)
        win = turns[-20:]
        wl = {}
        for turn in win:
            if turn[1] == "hecho":
                wl[turn[2]] = turn[3]
        per["ventana deslizante"] = sum(wl.get(k) == v for k, v in asked)
        toks["ventana deslizante"].append(sum(approx_tokens(x[4]) for x in win))
        # resumen con pérdidas: cada actualización se conserva con prob. 0,75
        sl = {}
        for turn in turns:
            if turn[1] == "hecho" and r.random() < 0.75:
                sl[turn[2]] = turn[3]
        per["resumen con pérdidas"] = sum(sl.get(k) == v for k, v in asked)
        toks["resumen con pérdidas"].append(150)
        # almacén externo: el extractor (regex) anota cada hecho con prob. 0,95; recuperación por clave
        first, last = {}, {}
        for turn in turns:
            if turn[1] == "hecho" and r.random() < 0.95:
                first.setdefault(turn[2], turn[3])
                last[turn[2]] = turn[3]
        per["almacén sin versión"] = sum(first.get(k) == v for k, v in asked)
        per["almacén versionado"] = sum(last.get(k) == v for k, v in asked)
        toks["almacén sin versión"].append(80)
        toks["almacén versionado"].append(80)
        for k in results:
            results[k].append(per[k] / max(1, len(asked)))
    print("SE-509 fracción de hechos vigentes recuperados al final de 80 turnos (300 conversaciones)")
    table([["estrategia", "aciertos", "tokens de memoria al preguntar"]] + [[k, pct(mean(results[k])), round(mean(toks[k]))] for k in results])
    return {"acc": {k: mean(v) for k, v in results.items()}, "tok": {k: mean(v) for k, v in toks.items()}}


# ====================================================================== SE-510
def _chunks():
    docs = []
    for part in ("part-39", "part-40"):
        for f in sorted((ROOT / "content" / part).glob("SE-*.md")):
            body = f.read_text(encoding="utf-8")
            cur, buf = f.stem, []
            for line in body.splitlines():
                if line.startswith("#"):
                    if len(" ".join(buf).split()) >= 40:
                        docs.append((f.stem, cur, " ".join(buf)))
                    cur, buf = line.lstrip("# ").strip(), []
                else:
                    buf.append(line)
            if len(" ".join(buf).split()) >= 40:
                docs.append((f.stem, cur, " ".join(buf)))
    return docs


class BM25:
    def __init__(self, docs, k1=1.5, b=0.75):
        self.k1, self.b = k1, b
        self.tf = [Counter(_norm(d)) for d in docs]
        self.len = [sum(c.values()) for c in self.tf]
        self.avg = mean(self.len)
        self.df = Counter()
        for c in self.tf:
            self.df.update(c.keys())
        self.n = len(docs)

    def scores(self, query):
        q = _norm(query)
        out = []
        for c, ln in zip(self.tf, self.len):
            s = 0.0
            for w in q:
                f = c.get(w, 0)
                if f:
                    idf = math.log(1 + (self.n - self.df[w] + 0.5) / (self.df[w] + 0.5))
                    s += idf * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * ln / self.avg))
            out.append(s)
        return out


class HashEmbed:
    """Vector por trigramas de caracteres con hashing (disperso): NO es un modelo de embeddings semántico."""

    def __init__(self, docs, dim=4096):
        self.dim = dim
        self.vecs = [self.vec(d) for d in docs]

    def vec(self, text):
        v: dict[int, float] = {}
        s = " ".join(_norm(text))
        s = f"  {s}  "
        for i in range(len(s) - 2):
            h = hash_str(s[i:i + 3]) % self.dim
            v[h] = v.get(h, 0.0) + 1.0
        n = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {k: x / n for k, x in v.items()}

    def scores(self, query):
        q = self.vec(query)
        return [sum(x * d.get(k, 0.0) for k, x in q.items()) for d in self.vecs]


def hash_str(s: str) -> int:
    h = 2166136261
    for ch in s.encode("utf-8"):
        h = ((h ^ ch) * 16777619) & 0xFFFFFFFF
    return h


def rank_of(scores, gold):
    order = sorted(range(len(scores)), key=lambda i: -scores[i])
    return order.index(gold) + 1


def rrf(*score_lists, k=60):
    n = len(score_lists[0])
    total = [0.0] * n
    for sc in score_lists:
        order = sorted(range(n), key=lambda i: -sc[i])
        for pos, i in enumerate(order):
            total[i] += 1.0 / (k + pos + 1)
    return total


def exp510(n_queries: int = 120, seed: int = 10) -> dict:
    chunks = _chunks()
    texts = [c[2] for c in chunks]
    r = rng(seed)
    bm = BM25(texts)
    he = HashEmbed(texts)
    idx = r.sample(range(len(chunks)), n_queries)
    def make_query(text, typo, stem):
        words = [w for w in dict.fromkeys(_norm(text)) if len(w) >= 6]
        pick = r.sample(words, min(8, len(words)))
        out = []
        for w in pick:
            x = r.random()
            out.append(_typo(w, r) if x < typo else (w[:5] if x < typo + stem else w))
        return " ".join(out)
    res = {}
    for label, typo, stem in (("exacta", 0.0, 0.0), ("con erratas y raíces", 0.35, 0.25)):
        queries = [(make_query(texts[i], typo, stem), i) for i in idx]
        rr = {k: [] for k in ("BM25", "hash", "híbrido RRF")}
        for q, gold in queries:
            s1, s2 = bm.scores(q), he.scores(q)
            rr["BM25"].append(rank_of(s1, gold))
            rr["hash"].append(rank_of(s2, gold))
            rr["híbrido RRF"].append(rank_of(rrf(s1, s2), gold))
        res[label] = {k: (mean([x == 1 for x in v]), mean([x <= 5 for x in v]), mean([1 / x for x in v])) for k, v in rr.items()}
    print("SE-510 corpus:", len(chunks), "fragmentos de las Partes 39 y 40;", n_queries, "consultas sintéticas")
    for label, d in res.items():
        print("  consultas", label)
        table([["recuperador", "acierto@1", "acierto@5", "MRR"]] + [[k, pct(a), pct(b), num(c, 3)] for k, (a, b, c) in d.items()])
    # RAG con reformulación: si la mejor puntuación de BM25 es baja, ampliar con términos de los 3 mejores y recuperar de nuevo
    queries = [(make_query(texts[i], 0.35, 0.25), i) for i in idx]
    base_top1 = []
    agentic_top1 = []
    extra = 0
    for q, gold in queries:
        s = bm.scores(q)
        base_top1.append(rank_of(s, gold) == 1)
        best = max(s)
        top2 = sorted(s, reverse=True)[:2]
        if (top2[0] - top2[1]) / max(top2[0], 1e-9) < 0.10:
            top = sorted(range(len(s)), key=lambda i: -s[i])[:3]
            pool = Counter()
            for i in top:
                pool.update(w for w in set(_norm(texts[i])) if len(w) >= 6)
            terms = [w for w, _ in sorted(pool.items(), key=lambda kv: (-kv[1], bm.df[kv[0]]))[:4]]
            s2 = bm.scores(q + " " + " ".join(terms))
            extra += 1
            agentic_top1.append(rank_of(s2, gold) == 1)
        else:
            agentic_top1.append(rank_of(s, gold) == 1)
    print("  RAG con reformulación: acierto@1", pct(mean(base_top1)), "->", pct(mean(agentic_top1)), "con", extra, "reformulaciones de", n_queries)
    # consultas fuera del corpus: ¿la mejor puntuación permite abstenerse?
    foreign = ["receta de tortilla de patatas con cebolla y huevo", "horario de trenes entre Madrid y Valencia en agosto",
               "cómo plantar tomates en un balcón con poca luz", "resultado del partido de baloncesto de anoche",
               "precio del café en el mercado mayorista", "estación de esquí con mejor nieve en febrero"]
    in_scores = [max(bm.scores(q)) for q, _ in queries]
    out_scores = [max(bm.scores(q)) for q in foreign]
    thr = quantile(in_scores, 0.10)
    abst = mean([s < thr for s in out_scores])
    print("  abstención: umbral = percentil 10 de las consultas válidas (", num(thr, 2), "); fuera de corpus rechazadas", pct(abst, 0), "; válidas rechazadas 10 %")
    return {"chunks": len(chunks), "res": res, "agentic": (mean(base_top1), mean(agentic_top1), extra), "abst": abst, "thr": thr}


EXPERIMENTS = {"505": exp505, "506": exp506, "507": exp507, "508": exp508, "509": exp509, "510": exp510}

if __name__ == "__main__":
    which = sys.argv[1:] or sorted(EXPERIMENTS)
    for w in which:
        EXPERIMENTS[w]()
        print()
