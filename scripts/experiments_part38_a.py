"""Experimentos de SE-457 a SE-462 (desarrollo asistido por IA).

Ningún experimento llama a un modelo real: los «modelos» son procesos sintéticos con
parámetros declarados y semilla fija, o código estándar que se ejecuta de verdad
(recuperación BM25, difflib, ast, doctest, sqlite3). Solo biblioteca estándar.
Uso: python scripts/experiments_part38_a.py  -> imprime JSON con todas las cifras.
"""
from __future__ import annotations

import ast
import difflib
import doctest
import json
import math
import random
import re
import sqlite3
import statistics
import sys
import textwrap
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def pct(x: float, digits: int = 1) -> float:
    return round(100 * x, digits)


# ------------------------------------------------------------------ SE-457
def e457_temperatura() -> dict:
    """Cinco respuestas candidatas con logits fijos; la correcta no es la más probable a T=1."""
    logits = [2.0, 1.6, 1.2, 0.4, 0.0]  # la correcta es la segunda (índice 1)
    correcta = 1
    rng = random.Random(457)
    out = []
    for temp in (0.2, 0.7, 1.0, 1.5):
        w = [math.exp(l / temp) for l in logits]
        s = sum(w)
        p = [x / s for x in w]
        n = 20000
        uno = 0
        mayoria = 0
        al_menos = 0
        for _ in range(n // 5):
            muestras = rng.choices(range(5), weights=p, k=5)
            uno += muestras[0] == correcta
            c = Counter(muestras).most_common(1)[0][0]
            mayoria += c == correcta
            al_menos += correcta in muestras
        t = n // 5
        out.append({"T": temp, "p_correcta": round(p[correcta], 3), "una_muestra": pct(uno / t),
                    "mayoria_de_5": pct(mayoria / t), "alguna_de_5": pct(al_menos / t)})
    return {"filas": out}


def e457_calibracion() -> dict:
    """1000 preguntas; la confianza declarada excede la exactitud en las difíciles."""
    rng = random.Random(4572)
    datos = []
    for _ in range(1000):
        dificil = rng.random() < 0.4
        conf = min(0.99, max(0.5, rng.gauss(0.88 if dificil else 0.90, 0.07)))
        acierto = rng.random() < (0.55 if dificil else 0.93)
        datos.append((conf, acierto, dificil))
    def tramo(sel):
        n = len(sel)
        return {"n": n, "confianza": pct(statistics.mean(c for c, _, _ in sel)),
                "exactitud": pct(sum(a for _, a, _ in sel) / n)}
    bins = []
    for lo, hi in ((0.5, 0.8), (0.8, 0.9), (0.9, 1.0)):
        sel = [d for d in datos if lo <= d[0] < hi]
        bins.append({"tramo": f"{int(lo*100)}–{int(hi*100)} %", **tramo(sel)})
    ece = sum(b["n"] / 1000 * abs(b["confianza"] - b["exactitud"]) for b in bins)
    return {"tramos": bins, "global": tramo(datos), "ece": round(ece, 1),
            "faciles": tramo([d for d in datos if not d[2]]), "dificiles": tramo([d for d in datos if d[2]])}


def e457_ventana() -> dict:
    """120 archivos de tamaño lognormal (mediana ≈ 5 800 tokens); qué fracción de conjuntos de trabajo de 8 archivos cabe en una ventana."""
    rng = random.Random(4573)
    tam = [int(rng.lognormvariate(math.log(5800), 0.9)) for _ in range(120)]
    total = sum(tam)
    filas = []
    for ventana in (8_000, 32_000, 128_000, 200_000):
        cabe = 0
        reps = 4000
        for _ in range(reps):
            cabe += sum(rng.sample(tam, 8)) <= ventana
        filas.append({"ventana": ventana, "conjuntos_que_caben": pct(cabe / reps), "fraccion_del_repositorio": pct(min(1.0, ventana / total))})
    return {"archivos": len(tam), "tokens_totales": total, "mediana": int(statistics.median(tam)), "maximo": max(tam), "filas": filas}


# ------------------------------------------------------------------ SE-458
def e458_requisitos() -> dict:
    """Seis requisitos ocultos; cada requisito no especificado se cumple con p=0.5, el especificado con 0.95."""
    rng = random.Random(458)
    filas = []
    n = 20000
    for k in range(0, 7):
        todos = 0
        medios = 0
        for _ in range(n):
            cumplidos = sum(rng.random() < (0.95 if i < k else 0.5) for i in range(6))
            todos += cumplidos == 6
            medios += cumplidos
        filas.append({"especificados": k, "todos": pct(todos / n), "media": round(medios / n, 2)})
    return {"filas": filas}


def _valida_formato(o):
    try:
        d = json.loads(o)
    except ValueError:
        return False
    return isinstance(d, dict) and set(d) >= {"nota", "estado"} and isinstance(d["nota"], (int, float))


def _valida_rango(o):
    d = json.loads(o)
    return 1.0 <= d["nota"] <= 7.0 and d["estado"] in {"A", "R"}


def _valida_coherencia(o):
    d = json.loads(o)
    return (d["estado"] == "A") == (d["nota"] >= 4.0)


def e458_validadores() -> dict:
    """Doscientas salidas sintéticas con un defecto cada una; qué capas de validación lo detectan."""
    rng = random.Random(4582)
    tipos = ["texto_extra", "falta_clave", "fuera_de_rango", "estado_invalido", "incoherente", "redondeo"]
    casos = []
    for i in range(200):
        t = tipos[i % 6]
        nota = round(rng.uniform(1.0, 7.0), 1)
        estado = "A" if nota >= 4.0 else "R"
        d = {"nota": nota, "estado": estado}
        if t == "texto_extra":
            s = "Aquí está el resultado: " + json.dumps(d)
        elif t == "falta_clave":
            s = json.dumps({"nota": nota})
        elif t == "fuera_de_rango":
            s = json.dumps({"nota": round(rng.uniform(7.5, 9.0), 1), "estado": "A"})
        elif t == "estado_invalido":
            s = json.dumps({"nota": nota, "estado": "aprobado"})
        elif t == "incoherente":
            s = json.dumps({"nota": nota, "estado": "R" if estado == "A" else "A"})
        else:
            s = json.dumps({"nota": round(nota + 0.04, 2), "estado": estado})  # nota con dos decimales indebidos pero válida
        casos.append((t, s))
    res = {}
    for t in tipos:
        sub = [s for tt, s in casos if tt == t]
        c1 = sum(not _valida_formato(s) for s in sub)
        c2 = sum((not _valida_formato(s)) or (not _valida_rango(s)) for s in sub)
        c3 = sum((not _valida_formato(s)) or (not _valida_rango(s)) or (not _valida_coherencia(s)) for s in sub)
        res[t] = {"n": len(sub), "formato": c1, "formato_rango": c2, "formato_rango_coherencia": c3}
    tot = {k: sum(r[k] for r in res.values()) for k in ("formato", "formato_rango", "formato_rango_coherencia")}
    return {"por_defecto": res, "total": tot, "n": len(casos)}


def e458_conflicto() -> dict:
    """Probabilidad de que un conjunto de n instrucciones sea consistente si cada par choca con prob. q."""
    filas = []
    for n in (3, 5, 8, 12, 20):
        fila = {"n": n, "pares": n * (n - 1) // 2}
        for q in (0.005, 0.02):
            fila[f"q{q}"] = pct((1 - q) ** fila["pares"])
        filas.append(fila)
    return {"filas": filas}


# ------------------------------------------------------------------ SE-459
TEMAS = {
    "redondeo": "redondeo nota decimal media ponderada entero mitad hacia arriba",
    "exportacion": "exportacion archivo ministerio formato columna cabecera delimitador",
    "matricula": "matricula inscripcion curso cupo periodo alumno plazo",
    "auditoria": "auditoria registro cambio autor fecha bitacora traza",
    "calendario": "calendario feriado semestre zona horaria fecha cierre acta",
    "permisos": "permisos rol docente coordinador lectura escritura acceso",
}
RUIDO = "sistema plataforma modulo servicio proceso configuracion datos usuario regla caso manera tipo lista valor campo".split()


def _corpus(rng: random.Random, n_docs: int = 240):
    docs = []
    for i in range(n_docs):
        tema = list(TEMAS)[i % 6]
        voc = TEMAS[tema].split()
        palabras = []
        for _ in range(900):
            palabras.append(rng.choice(voc) if rng.random() < 0.18 else rng.choice(RUIDO))
        docs.append((tema, i, palabras))
    return docs


class BM25:
    def __init__(self, chunks, k1=1.5, b=0.75):
        self.chunks = chunks
        self.k1, self.b = k1, b
        self.tf = [Counter(c) for c in chunks]
        self.len = [len(c) for c in chunks]
        self.avg = sum(self.len) / len(self.len)
        df = Counter()
        for t in self.tf:
            df.update(t.keys())
        n = len(chunks)
        self.idf = {w: math.log(1 + (n - d + 0.5) / (d + 0.5)) for w, d in df.items()}

    def puntaje(self, q, i):
        s = 0.0
        for w in q:
            f = self.tf[i].get(w, 0)
            if f:
                s += self.idf.get(w, 0) * f * (self.k1 + 1) / (f + self.k1 * (1 - self.b + self.b * self.len[i] / self.avg))
        return s

    def top(self, q, k):
        return sorted(range(len(self.chunks)), key=lambda i: -self.puntaje(q, i))[:k]


def e459_fragmentos() -> dict:
    """Cada documento esconde, en una posición aleatoria, un hecho único (clave rara); tamaño de fragmento vs recuperación."""
    rng = random.Random(459)
    docs = _corpus(rng)
    hechos = {}
    for tema, i, palabras in docs:
        clave = f"clave{i:03d}"
        pos = rng.randrange(0, 880)
        palabras[pos:pos + 3] = [clave, "valor", f"v{i:03d}"]
        hechos[i] = (clave, pos)
    filas = []
    for tam in (50, 150, 300, 900):
        paso = max(1, int(tam * 0.8)) if tam < 900 else 900
        chunks, dueno = [], []
        for _, i, palabras in docs:
            for ini in range(0, len(palabras), paso):
                chunks.append(palabras[ini:ini + tam])
                dueno.append((i, ini, ini + tam))
        bm = BM25(chunks)
        aciertos = 0
        cobertura = 0
        for tema, i, palabras in docs[:120]:
            clave, pos = hechos[i]
            top = bm.top([clave, "valor"], 3)
            if any(dueno[j][0] == i and dueno[j][1] <= pos and pos + 3 <= dueno[j][2] for j in top[:1]):
                aciertos += 1
            if any(dueno[j][0] == i for j in top):
                cobertura += 1
        filas.append({"tam": tam, "fragmentos": len(chunks), "exacto_top1": pct(aciertos / 120),
                      "doc_en_top3": pct(cobertura / 120), "tokens_por_consulta": tam * 3})
    return {"filas": filas}


def e459_memoria() -> dict:
    """Hechos que cambian con tasa 1 %/día: respuestas erróneas y refrescos según la caducidad (TTL) de la memoria."""
    rng = random.Random(4593)
    dias, n = 180, 400
    filas = []
    for ttl in (None, 90, 30, 7):
        erroneas = consultas = refrescos = 0
        guardado = [0] * n
        for d in range(1, dias + 1):
            if ttl is not None:
                for h in range(n):
                    if d - guardado[h] >= ttl:
                        guardado[h] = d
                        refrescos += 1
            for h in rng.sample(range(n), 50):
                consultas += 1
                if rng.random() < 1 - 0.99 ** (d - guardado[h]):
                    erroneas += 1
        filas.append({"ttl": "sin caducidad" if ttl is None else f"{ttl} días", "erroneas": pct(erroneas / consultas),
                      "refrescos_por_hecho": round(refrescos / n, 1)})
    return {"filas": filas}


def e459_presupuesto() -> dict:
    """Empaquetar fragmentos con relevancia conocida en un presupuesto de tokens: por relevancia o por relevancia/tamaño."""
    rng = random.Random(4594)
    res = {"relevancia": [], "densidad": [], "aleatorio": []}
    for _ in range(300):
        frag = [(rng.random() ** 2, rng.choice((200, 400, 800, 1600))) for _ in range(30)]
        presup = 3000
        def llenar(orden):
            usado = 0
            val = 0.0
            for r, t in orden:
                if usado + t <= presup:
                    usado += t
                    val += r
            return val
        res["relevancia"].append(llenar(sorted(frag, key=lambda x: -x[0])))
        res["densidad"].append(llenar(sorted(frag, key=lambda x: -x[0] / x[1])))
        o = frag[:]
        rng.shuffle(o)
        res["aleatorio"].append(llenar(o))
    tot = {k: round(statistics.mean(v), 3) for k, v in res.items()}
    return {"medias": tot, "mejora_densidad_vs_relevancia": pct(tot["densidad"] / tot["relevancia"] - 1)}


# ------------------------------------------------------------------ SE-460
def e460_aceptacion() -> dict:
    """1000 sugerencias, 78 % correctas; revisor con sesgo de automatización según su política."""
    rng = random.Random(460)
    filas = []
    politicas = [("Aceptar con Tab sin leer", 0.00), ("Leer solo si es larga", None), ("Leer siempre y ejecutar", 0.85)]
    for nombre, det in politicas:
        malas_aceptadas = aceptadas = rechazadas_buenas = 0
        for _ in range(1000):
            buena = rng.random() < 0.78
            larga = rng.random() < 0.3
            d = det if det is not None else (0.7 if larga else 0.05)
            if buena:
                aceptadas += 1
                if det == 0.85 and rng.random() < 0.03:
                    rechazadas_buenas += 1
                    aceptadas -= 1
            else:
                if rng.random() < d:
                    continue
                malas_aceptadas += 1
                aceptadas += 1
        filas.append({"politica": nombre, "defectos_aceptados": malas_aceptadas, "aceptadas": aceptadas})
    return {"filas": filas}


ARCHIVO = "\n".join(
    ["import os", "import sys", ""] + [
        f"def regla_{i}(x):\n    '''Regla {i}.'''\n    if x > {i}:\n        return x * {i + 1}\n    return 'otro'\n" for i in range(30)
    ])


def _deriva_cosmetica(src: str) -> str:
    s = src.replace("'''", '"""').replace("'otro'", '"otro"')
    s = s.replace("import os\nimport sys", "import sys\nimport os")
    return s


def e460_alcance() -> dict:
    """Corregir una regla: edición dirigida frente a regenerar el archivo con deriva cosmética."""
    objetivo = ARCHIVO.replace("if x > 17:", "if x >= 17:")
    regenerado = _deriva_cosmetica(objetivo)
    def cambios(a, b):
        return sum(1 for l in difflib.unified_diff(a.splitlines(), b.splitlines(), lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---"))
    d1, d2 = cambios(ARCHIVO, objetivo), cambios(ARCHIVO, regenerado)
    # probabilidad de que el revisor encuentre el único cambio semántico: p = base / (1 + líneas/escala)
    def p(lineas):
        return 0.95 / (1 + lineas / 20)
    return {"lineas_archivo": len(ARCHIVO.splitlines()), "diff_dirigido": d1, "diff_regenerado": d2,
            "p_detectar_dirigido": pct(p(d1)), "p_detectar_regenerado": pct(p(d2))}


def e460_debounce() -> dict:
    """Traza de pulsaciones determinista: peticiones enviadas, canceladas y útiles según el retardo."""
    rng = random.Random(4604)
    t = 0.0
    tecla = []
    for palabra in range(60):
        for _ in range(rng.randint(4, 12)):
            t += rng.uniform(0.06, 0.35)
            tecla.append(t)
        t += rng.uniform(0.6, 2.0)  # pausa para pensar
    filas = []
    for retardo in (0.0, 0.15, 0.3, 0.6):
        enviadas = utiles = 0
        for i, ti in enumerate(tecla):
            siguiente = tecla[i + 1] if i + 1 < len(tecla) else float("inf")
            if retardo == 0 or siguiente - ti >= retardo:
                enviadas += 1
                if siguiente - ti >= 0.5:  # la respuesta llega a tiempo de mostrarse
                    utiles += 1
        filas.append({"retardo_ms": int(retardo * 1000), "pulsaciones": len(tecla), "peticiones": enviadas, "utiles": utiles})
    return {"filas": filas}


# ------------------------------------------------------------------ SE-461
def e461_mejor_de_n() -> dict:
    """Calidad real ~ N(0,1) de cada alternativa; el evaluador mide con ruido sigma. Calidad real de la elegida."""
    rng = random.Random(461)
    filas = []
    for n in (1, 3, 5, 10, 20):
        fila = {"n": n}
        for sigma in (0.0, 1.0, 2.0):
            tot = ver = 0.0
            for _ in range(20000 // 10):
                q = [rng.gauss(0, 1) for _ in range(n)]
                m = [x + rng.gauss(0, sigma) for x in q]
                i = max(range(n), key=lambda j: m[j])
                tot += q[i]
                ver += m[i]
            t = 2000
            fila[f"real_s{sigma}"] = round(tot / t, 2)
            fila[f"medida_s{sigma}"] = round(ver / t, 2)
        filas.append(fila)
    return {"filas": filas}


PLANTILLA = '''
"""Servicio {nombre}."""
import logging
import os

log = logging.getLogger(__name__)
TIEMPO = int(os.environ.get("TIEMPO", "30"))

def crear_{nombre}(datos):
    log.info("crear")
    return datos

def leer_{nombre}(id_):
    log.info("leer")
    return {{"id": id_}}

def actualizar_{nombre}(id_, datos):
    log.info("actualizar")
    return datos

def borrar_{nombre}(id_):
    log.info("borrar")
    return None

def _ayuda_{nombre}(x):
    return x
'''


def e461_andamiaje() -> dict:
    """Se genera el andamiaje de 8 entidades; ast cuenta definiciones y las que ningún otro código usa."""
    entidades = ["curso", "alumno", "docente", "nota", "acta", "periodo", "sala", "inscripcion"]
    fuente = {n: PLANTILLA.format(nombre=n) for n in entidades}
    defs = {}
    for n, s in fuente.items():
        arbol = ast.parse(s)
        defs[n] = [f.name for f in arbol.body if isinstance(f, ast.FunctionDef)]
    # código propio: solo usa crear y leer de nota, crear de alumno y leer de curso
    uso = {"crear_nota", "leer_nota", "crear_alumno", "leer_curso"}
    total = sum(len(v) for v in defs.values())
    sin_uso = sum(1 for v in defs.values() for f in v if f not in uso)
    lineas = sum(len(s.strip().splitlines()) for s in fuente.values())
    return {"entidades": len(entidades), "lineas_generadas": lineas, "funciones": total, "funciones_sin_uso": sin_uso,
            "pct_sin_uso": pct(sin_uso / total), "lineas_de_dominio": 0}


def e461_brecha() -> dict:
    """Atributos que un prototipo no tiene y producción exige: probabilidad de presencia y trabajo restante."""
    rng = random.Random(4612)
    atributos = [("validación de entradas", 0.25, 5), ("manejo de errores", 0.30, 8), ("autenticación", 0.10, 13),
                 ("pruebas", 0.15, 13), ("registro y métricas", 0.20, 5), ("migraciones de datos", 0.05, 8),
                 ("accesibilidad", 0.10, 8), ("límites de tamaño y tiempo", 0.10, 5)]
    total = sum(c for _, _, c in atributos)
    resultados = []
    for _ in range(5000):
        resultados.append(sum(c for _, p, c in atributos if rng.random() > p))
    return {"trabajo_total": total, "mediana_restante": statistics.median(resultados),
            "p90_restante": sorted(resultados)[int(0.9 * len(resultados))],
            "fraccion_pendiente_mediana": pct(statistics.median(resultados) / total), "atributos": len(atributos)}


# ------------------------------------------------------------------ SE-462
def nota_final(trabajos, examen):
    """Calcula la nota final: 40 % trabajos (promedio) y 60 % examen; redondea a un decimal; aprueba con 4,0."""
    prom = sum(trabajos) / len(trabajos)
    nota = round(0.4 * prom + 0.6 * examen, 1)
    return nota, "A" if nota >= 4.0 else "R"


MUTANTES = {
    "peso_40_cambiado": "0.4 * prom + 0.6 * examen -> 0.5 * prom + 0.5 * examen",
    "umbral_mayor": "nota >= 4.0 -> nota > 4.0",
    "sin_redondeo": "round(..., 1) -> ...",
    "redondeo_cero": "round(..., 1) -> round(..., 0)",
    "examen_ignorado": "0.6 * examen -> 0.6 * prom",
    "promedio_max": "sum(trabajos) / len -> max(trabajos)",
    "estado_invertido": "A if >= -> R if >=",
    "peso_60_cambiado": "0.6 -> 0.7 y 0.4 -> 0.3",
}


def _construye(m):
    def f(trabajos, examen):
        prom = sum(trabajos) / len(trabajos)
        if m == "promedio_max":
            prom = max(trabajos)
        a, b = 0.4, 0.6
        if m == "peso_40_cambiado":
            a, b = 0.5, 0.5
        if m == "peso_60_cambiado":
            a, b = 0.3, 0.7
        e = examen if m != "examen_ignorado" else prom
        nota = a * prom + b * e
        if m == "sin_redondeo":
            pass
        elif m == "redondeo_cero":
            nota = round(nota, 0)
        else:
            nota = round(nota, 1)
        ok = nota > 4.0 if m == "umbral_mayor" else nota >= 4.0
        est = "A" if ok else "R"
        if m == "estado_invertido":
            est = "R" if ok else "A"
        return nota, est
    return f


def e462_pruebas() -> dict:
    """Pruebas que copian la salida actual (snapshot en entradas típicas) frente a pruebas derivadas de la especificación."""
    tipicas = [([5.0, 6.0], 5.5), ([4.5, 4.5, 4.5], 4.5), ([6.0], 6.0), ([3.0, 5.0], 4.0), ([5.5, 6.5], 6.0)]
    snapshot = [((t, e), nota_final(t, e)) for t, e in tipicas]
    espec = snapshot + [
        (([4.0, 4.0], 4.0), (4.0, "A")),       # frontera exacta de aprobación
        (([3.0], 4.0), (3.6, "R")),            # un solo trabajo y examen que no basta
        (([7.0, 1.0], 2.0), (2.8, "R")),       # distingue promedio de máximo
        (([5.0, 5.0], 3.0), (3.8, "R")),       # las dos ponderaciones importan; 3,8 no se redondea a 4
        (([4.4, 4.5], 3.9), (4.1, "A")),       # el resultado 4,12 se redondea a un decimal
    ]
    res = {"snapshot": 0, "espec": 0}
    detalle = {}
    for nombre, m in MUTANTES.items():
        f = _construye(nombre)
        s = any(f(*args) != esp for args, esp in snapshot)
        e = any(f(*args) != esp for args, esp in espec)
        detalle[nombre] = {"snapshot": s, "espec": e}
        res["snapshot"] += s
        res["espec"] += e
    # el original pasa ambos
    ok = all(nota_final(*a) == esp for a, esp in espec)
    return {"mutantes": len(MUTANTES), "detectados_snapshot": res["snapshot"], "detectados_espec": res["espec"],
            "original_pasa_espec": ok, "detalle": detalle}


def e462_documentacion() -> dict:
    """Veinte funciones con ejemplos en la docstring; en 8 el comportamiento cambió sin actualizar el ejemplo."""
    import importlib.util
    import tempfile
    funciones = []
    for i in range(20):
        k = i + 2
        deriva = i % 5 in (1, 3) or i in (0, 10)
        funciones.append((f"f{i}", k, k * 2, 1 if deriva else 0, deriva))
    fuente = ""
    for n, k, doc, extra, _ in funciones:
        fuente += (f'def {n}(x):' + chr(10) + f'    """Duplica.' + chr(10) + chr(10) + f'    >>> {n}({k})' + chr(10) + f'    {doc}' + chr(10) + '    """' + chr(10) + f'    return x * 2 + {extra}' + chr(10) + chr(10))
    for i in range(10):
        fuente += ("def g%d(x):" % i + chr(10) + '    """Duplica el valor recibido."""' + chr(10)
                   + "    return x * 2 + %d" % (1 if i < 4 else 0) + chr(10) + chr(10))
    with tempfile.TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "generado.py"
        ruta.write_text(fuente, encoding="utf-8")
        spec = importlib.util.spec_from_file_location("generado", ruta)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        finder = doctest.DocTestFinder()
        runner = doctest.DocTestRunner(verbose=False)
        fallos = 0
        for n, *_ in funciones:
            for t in finder.find(getattr(modulo, n), n, globs=vars(modulo)):
                fallos += runner.run(t, out=lambda s: None).failed > 0
        fallos_prosa = 0
        for i in range(10):
            for t in finder.find(getattr(modulo, "g%d" % i), "g%d" % i, globs=vars(modulo)):
                fallos_prosa += runner.run(t, out=lambda s: None).failed > 0
    return {"funciones": 20, "con_deriva": sum(f[4] for f in funciones), "detectadas_doctest": fallos,
            "prosa_funciones": 10, "prosa_con_deriva": 4, "prosa_detectadas_doctest": fallos_prosa}


def e462_migracion() -> dict:
    """2 000 notas como texto con coma; migración ingenua frente a migración con validación y cuarentena."""
    rng = random.Random(4623)
    filas = []
    for i in range(2000):
        r = rng.random()
        if r < 0.90:
            v = f"{rng.randint(10, 70) / 10:.1f}".replace(".", ",")
        elif r < 0.95:
            v = f"{rng.randint(10, 70) / 10:.1f}"  # punto decimal
        elif r < 0.98:
            v = ""
        else:
            v = rng.choice(["NP", "5,5,0", "ex", "7.1.0"])
        filas.append((i, v))
    db = sqlite3.connect(":memory:")
    db.execute("create table notas(id integer, valor text)")
    db.executemany("insert into notas values (?,?)", filas)
    # ingenua: replace(',', '.') y CAST
    ing = db.execute("select count(*), sum(cast(replace(valor, ',', '.') as real) = 0) from notas").fetchone()
    ceros_ing = db.execute("select count(*) from notas where cast(replace(valor, ',', '.') as real) = 0 and valor not in ('0','0,0')").fetchone()[0]
    # validada
    patron = re.compile(r"^[1-7][,.]\d$")
    buenas = [(i, float(v.replace(",", "."))) for i, v in filas if patron.match(v)]
    cuarentena = [(i, v) for i, v in filas if not patron.match(v)]
    return {"filas": len(filas), "invalidas": len(cuarentena), "ceros_silenciosos_ingenua": ceros_ing,
            "parciales_silenciosos_ingenua": len(cuarentena) - ceros_ing, "migradas_validada": len(buenas),
            "cuarentena": len(cuarentena), "tipos_en_cuarentena": sorted({v for _, v in cuarentena})}


def todo() -> dict:
    return {
        "e457_temperatura": e457_temperatura(), "e457_calibracion": e457_calibracion(), "e457_ventana": e457_ventana(),
        "e458_requisitos": e458_requisitos(), "e458_validadores": e458_validadores(), "e458_conflicto": e458_conflicto(),
        "e459_fragmentos": e459_fragmentos(), "e459_memoria": e459_memoria(), "e459_presupuesto": e459_presupuesto(),
        "e460_aceptacion": e460_aceptacion(), "e460_alcance": e460_alcance(), "e460_debounce": e460_debounce(),
        "e461_mejor_de_n": e461_mejor_de_n(), "e461_andamiaje": e461_andamiaje(), "e461_brecha": e461_brecha(),
        "e462_pruebas": e462_pruebas(), "e462_documentacion": e462_documentacion(), "e462_migracion": e462_migracion(),
    }


if __name__ == "__main__":
    json.dump(todo(), sys.stdout, ensure_ascii=False, indent=1)
