"""Experimentos de SE-559 a SE-564 (desarrollo asistido por IA).

Ningún experimento llama a un modelo real: los «modelos» y «revisores» son procesos sintéticos con
parámetros declarados y semilla fija, o código estándar que se ejecuta de verdad (ast, hashlib,
difflib, re, tempfile). Solo biblioteca estándar.
Uso: python scripts/experiments_part46_b.py  -> imprime JSON con todas las cifras.
"""
from __future__ import annotations

import ast
import hashlib
import itertools
import json
import math
import random
import re
import statistics
import sys
import tempfile
from collections import Counter
from pathlib import Path


def pct(x: float, digits: int = 1) -> float:
    return round(100 * x, digits)


# ------------------------------------------------------------------ SE-559
def e463_umbral() -> dict:
    """Un revisor automático puntúa 400 cambios (80 con defecto real); umbral frente a precisión y revisiones inútiles."""
    rng = random.Random(463)
    datos = []
    for i in range(400):
        defecto = i < 80
        punt = rng.gauss(0.68 if defecto else 0.40, 0.17)
        datos.append((punt, defecto))
    filas = []
    for umbral in (0.35, 0.50, 0.60, 0.70, 0.80):
        marcados = [d for d in datos if d[0] >= umbral]
        tp = sum(1 for _, d in marcados if d)
        filas.append({"umbral": umbral, "marcados": len(marcados), "aciertos": tp,
                      "precision": pct(tp / len(marcados)) if marcados else 0.0, "cobertura": pct(tp / 80),
                      "falsas_alarmas": len(marcados) - tp})
    return {"filas": filas}


def _referencia(xs):
    """Función original: agrupa notas por curso y devuelve el promedio por curso, ordenado por curso."""
    acum = {}
    for curso, nota in xs:
        acum.setdefault(curso, []).append(nota)
    return [(c, round(sum(v) / len(v), 1)) for c, v in sorted(acum.items())]


def _refactor_ok(xs):
    acum = {}
    for curso, nota in xs:
        acum.setdefault(curso, []).append(nota)
    return [(c, round(sum(v) / len(v), 1)) for c in sorted(acum) for v in [acum[c]]]


def _refactor_orden(xs):
    acum = {}
    for curso, nota in xs:
        acum.setdefault(curso, []).append(nota)
    return [(c, round(sum(v) / len(v), 1)) for c, v in acum.items()]  # pierde el orden


def _refactor_tope(xs):
    acum = {}
    for curso, nota in xs:
        acum.setdefault(curso, []).append(nota)
    return [(c, round(sum(v) / len(v), 1)) for c, v in sorted(acum.items()) if len(v) < 5]  # descarta cursos con 5 notas o más


def _refactor_vacio(xs):
    acum = {}
    for curso, nota in xs:
        if nota:  # trata la nota 0.0 como ausente
            acum.setdefault(curso, []).append(nota)
    return [(c, round(sum(v) / len(v), 1)) for c, v in sorted(acum.items())]


def e463_equivalencia() -> dict:
    """Tres refactorizaciones; cuántas entradas aleatorias hacen falta para distinguir cada una de la original."""
    rng = random.Random(4632)
    def entrada(n):
        return [(rng.choice("ABCDE"), rng.choice([0.0, 1.0, 2.5, 4.0, 5.5, 7.0]) if rng.random() < 0.97 else 0.0) for _ in range(n)]
    cand = {"equivalente": _refactor_ok, "pierde el orden": _refactor_orden, "descarta la nota 0,0": _refactor_vacio,
            "descarta cursos con 5 notas o más": _refactor_tope}
    filas = []
    for nombre, fn in cand.items():
        difiere = 0
        total = 20000
        for _ in range(total):
            xs = entrada(rng.randint(1, 8))
            if fn(xs) != _referencia(xs):
                difiere += 1
        # probabilidad de que n entradas independientes no encuentren ninguna diferencia
        p = difiere / total
        fila = {"candidato": nombre, "entradas_que_difieren": difiere, "de": total, "p_por_entrada": pct(p, 2)}
        for n in (5, 20, 100, 1000):
            fila[f"detecta_{n}"] = pct(1 - (1 - p) ** n)
        filas.append(fila)
    return {"filas": filas}


def _explica_por_comentario(src):
    arbol = ast.parse(src)
    f = arbol.body[0]
    return ast.get_docstring(f).splitlines()[0]


def e463_explicacion() -> dict:
    """Treinta funciones; en 9 el comentario describe un comportamiento anterior. Explicador de comentarios frente a ejecución."""
    rng = random.Random(4633)
    ok = comentario_ok = 0
    desfase = 0
    for i in range(30):
        k = rng.randint(2, 9)
        deriva = i % 10 in (2, 5, 8)
        doc = f"Multiplica por {k}" if not deriva else f"Multiplica por {k - 1}"
        src = f'def f(x):\n    """{doc}."""\n    return x * {k}\n'
        texto = _explica_por_comentario(src)
        declarado = int(re.search(r"(\d+)", texto).group(1))
        real = ast.parse(src).body[0].body[1].value.right.value
        desfase += declarado != real
        comentario_ok += declarado == real
    return {"funciones": 30, "con_deriva": 9, "explicaciones_que_repiten_el_comentario_erroneas": desfase,
            "coinciden_con_el_codigo": comentario_ok}


# ------------------------------------------------------------------ SE-560
def e464_ambiguedad() -> dict:
    """Espacio de interpretaciones de «calcula la nota final»: cada restricción elimina combinaciones."""
    dims = {
        "promedio": ["aritmético", "ponderado", "mediana"],
        "redondeo": ["mitad hacia arriba", "mitad al par", "truncar"],
        "decimales": [0, 1, 2],
        "escala": ["1–7", "0–100", "1–10"],
        "nota_ausente": ["cero", "ignorar", "error"],
        "umbral": [">=4,0", ">4,0", ">=50 %"],
    }
    todas = list(itertools.product(*dims.values()))
    names = list(dims)
    def filtra(restr):
        return [t for t in todas if all(t[names.index(k)] == v for k, v in restr.items())]
    pasos = [("sin restricciones", {}), ("+ escala", {"escala": "1–7"}), ("+ umbral", {"escala": "1–7", "umbral": ">=4,0"}),
             ("+ decimales", {"escala": "1–7", "umbral": ">=4,0", "decimales": 1}),
             ("+ redondeo", {"escala": "1–7", "umbral": ">=4,0", "decimales": 1, "redondeo": "mitad hacia arriba"}),
             ("+ nota ausente", {"escala": "1–7", "umbral": ">=4,0", "decimales": 1, "redondeo": "mitad hacia arriba", "nota_ausente": "error"}),
             ("+ promedio", {"escala": "1–7", "umbral": ">=4,0", "decimales": 1, "redondeo": "mitad hacia arriba", "nota_ausente": "error", "promedio": "ponderado"})]
    filas = []
    for nombre, r in pasos:
        n = len(filtra(r))
        filas.append({"paso": nombre, "interpretaciones": n, "p_acertar_al_azar": pct(1 / n, 2)})
    return {"total": len(todas), "filas": filas}


def e464_distractores() -> dict:
    """Recuperación con documentos de versiones anteriores: sin filtro de versión y con él."""
    rng = random.Random(464)
    VOC = "redondeo nota media curso acta periodo regla formato exportacion calculo promedio entero decimal".split()
    resultados = {"sin_filtro": 0, "con_filtro": 0}
    n_consultas = 300
    for q in range(n_consultas):
        tema = rng.sample(VOC, 3)
        vigente = tema + [rng.choice(VOC) for _ in range(5)] + ["v3"]
        antiguos = []
        for k in range(rng.choice((1, 2, 4))):
            antiguos.append(tema + [rng.choice(VOC) for _ in range(5)] + [f"v{k + 1}"])
        docs = [vigente] + antiguos
        # puntuación por solapamiento léxico con ruido (los antiguos tienen un solapamiento igual o mayor por ser más largos y repetidos)
        def punt(d):
            return sum(1 for w in set(d) if w in tema) + rng.random() * 0.8
        orden = sorted(range(len(docs)), key=lambda i: -punt(docs[i]))
        resultados["sin_filtro"] += orden[0] == 0
        vig = [i for i in range(len(docs)) if "v3" in docs[i]]
        resultados["con_filtro"] += vig[0] == 0
    return {"consultas": n_consultas, "sin_filtro": pct(resultados["sin_filtro"] / n_consultas),
            "con_filtro": pct(resultados["con_filtro"] / n_consultas)}


def e464_reglas() -> dict:
    """Detector de reglas contradictorias en archivos de instrucciones sintéticos de 5 a 40 reglas."""
    rng = random.Random(4644)
    claves = [f"clave{i}" for i in range(25)]
    filas = []
    for n in (5, 10, 20, 40):
        con_conflicto = 0
        total = 500
        for _ in range(total):
            reglas = [(rng.choice(claves), rng.choice(["siempre", "nunca"])) for _ in range(n)]
            vistos = {}
            hay = False
            for k, v in reglas:
                if k in vistos and vistos[k] != v:
                    hay = True
                vistos[k] = vistos.get(k, v)
            con_conflicto += hay
        filas.append({"reglas": n, "con_conflicto": pct(con_conflicto / total)})
    return {"filas": filas, "claves": len(claves)}


# ------------------------------------------------------------------ SE-561
def wilson(aciertos: int, n: int, z: float = 1.96) -> tuple:
    p = aciertos / n
    den = 1 + z * z / n
    centro = (p + z * z / (2 * n)) / den
    mitad = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return centro - mitad, centro + mitad


def e465_tamano() -> dict:
    """Intervalo de Wilson y probabilidad de ordenar bien dos sistemas (70 % frente a 75 %) según las tareas del conjunto."""
    rng = random.Random(465)
    filas = []
    for n in (20, 50, 100, 300, 1000):
        lo, hi = wilson(round(0.70 * n), n)
        ok = 0
        reps = 2000
        for _ in range(reps):
            a = sum(rng.random() < 0.70 for _ in range(n))
            b = sum(rng.random() < 0.75 for _ in range(n))
            ok += b > a
        filas.append({"tareas": n, "ancho_ic_pts": round(100 * (hi - lo), 1), "ic": [pct(lo), pct(hi)],
                      "ordena_bien": pct(ok / reps)})
    return {"filas": filas}


def e465_frontera() -> dict:
    """Seis configuraciones sintéticas: costo por solución aceptada y latencia; cuáles están en la frontera de Pareto."""
    configs = [("pequeño", 0.52, 0.002, 1.2), ("pequeño + reintento", 0.64, 0.004, 2.6), ("mediano", 0.68, 0.010, 2.5),
               ("mediano + contexto", 0.76, 0.018, 4.1), ("grande", 0.80, 0.045, 6.0), ("grande + contexto + juez", 0.86, 0.110, 12.0)]
    revision = 0.40  # costo de revisión humana de un intento, en las mismas unidades
    filas = []
    for nombre, exito, costo, lat in configs:
        por_exito = (costo + revision) / exito
        filas.append({"config": nombre, "exito": pct(exito, 0), "costo_intento": costo, "latencia_s": lat,
                      "costo_por_aceptada": round(por_exito, 2)})
    for f in filas:
        f["dominada"] = any(g["exito"] >= f["exito"] and g["costo_por_aceptada"] <= f["costo_por_aceptada"] and g["latencia_s"] <= f["latencia_s"]
                            and (g["exito"], g["costo_por_aceptada"], g["latencia_s"]) != (f["exito"], f["costo_por_aceptada"], f["latencia_s"]) for g in filas)
    return {"filas": filas, "revision": revision}


def e465_juez() -> dict:
    """Un juez automático sintético con sesgo de longitud y de posición frente a etiquetas humanas."""
    rng = random.Random(4652)
    n = 1000
    coincide = coincide_swap = 0
    largas_gana = 0
    for _ in range(n):
        calidad_a, calidad_b = rng.gauss(0, 1), rng.gauss(0, 1)
        len_a, len_b = rng.uniform(0.5, 1.5), rng.uniform(0.5, 1.5)
        humano = calidad_a > calidad_b
        def juez(qa, qb, la, lb):
            return (qa + 0.8 * la + 0.4 + rng.gauss(0, 0.5)) > (qb + 0.8 * lb + rng.gauss(0, 0.5))
        j1 = juez(calidad_a, calidad_b, len_a, len_b)
        j2 = not juez(calidad_b, calidad_a, len_b, len_a)  # mismas respuestas con el orden intercambiado
        coincide += j1 == humano
        coincide_swap += j1 == j2
        largas_gana += (j1 == (len_a > len_b))
    return {"n": n, "acuerdo_con_humano": pct(coincide / n), "estable_al_intercambiar_orden": pct(coincide_swap / n),
            "gana_la_mas_larga": pct(largas_gana / n)}


# ------------------------------------------------------------------ SE-562
def _entropia(s: str) -> float:
    c = Counter(s)
    return -sum(v / len(s) * math.log2(v / len(s)) for v in c.values())


def e466_escaner() -> dict:
    """Doscientos mensajes sintéticos con y sin datos sensibles generados en tiempo de ejecución; escáner por patrón y por entropía."""
    rng = random.Random(466)
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    casos = []
    for i in range(240):
        tipo = i % 6
        if tipo == 0:
            texto, clase = "usuario%d@ejemplo.test pide revisar la nota" % rng.randint(1, 999), "correo"
        elif tipo == 1:
            cad = "".join(rng.choice(alfabeto) for _ in range(32))
            texto, clase = "usa la clave " + cad + " para el servicio", "secreto"
        elif tipo == 2:
            texto, clase = "alumno con id %d-%d no ve su acta" % (rng.randint(10_000_000, 25_000_000), rng.randint(0, 9)), "identificador"
        elif tipo == 3:
            texto, clase = "el hash de la versión es " + "".join(rng.choice("0123456789abcdef") for _ in range(40)), "limpio"
        elif tipo == 5:
            texto, clase = "usa la clave " + "".join(rng.choice("0123456789abcdef") for _ in range(32)) + " para el servicio", "secreto_hex"
        else:
            texto, clase = "el redondeo de la nota 5,5 falla en el acta del periodo %d" % rng.randint(1, 4), "limpio"
        casos.append((texto, clase))
    p_correo = re.compile(r"[\w.]+@[\w.]+\.\w+")
    p_id = re.compile(r"\b\d{7,8}-\d\b")
    def marca_patron(t):
        return bool(p_correo.search(t) or p_id.search(t))
    def marca_entropia(t):
        return any(len(w) >= 24 and _entropia(w) > 4.0 for w in t.split())
    p_ctx = re.compile(r"(clave|contraseña|token)\s+\S{16,}")
    def marca_contexto(t):
        return bool(p_ctx.search(t))
    res = {}
    for clase in ("correo", "secreto", "secreto_hex", "identificador", "limpio"):
        sub = [t for t, c in casos if c == clase]
        res[clase] = {"n": len(sub), "patron": sum(marca_patron(t) for t in sub), "entropia": sum(marca_entropia(t) for t in sub),
                      "contexto": sum(marca_contexto(t) for t in sub),
                      "las_tres": sum(marca_patron(t) or marca_entropia(t) or marca_contexto(t) for t in sub)}
    return res


SNIPPETS = {
    "consulta con texto formateado": ("q = 'SELECT * FROM notas WHERE id = ' + str(i)\ncur.execute(q)", True),
    "consulta parametrizada": ("cur.execute('SELECT * FROM notas WHERE id = ?', (i,))", False),
    "evaluación dinámica": ("resultado = eval(entrada)", True),
    "evaluación literal": ("resultado = ast.literal_eval(entrada)", False),
    "comando con shell": ("subprocess.run(cmd, shell=True)", True),
    "comando sin shell": ("subprocess.run(['ls', ruta], shell=False)", False),
    "hash débil": ("h = hashlib.md5(dato).hexdigest()", True),
    "hash robusto": ("h = hashlib.sha256(dato).hexdigest()", False),
    "yaml sin límites": ("d = yaml.load(texto)", True),
    "yaml seguro": ("d = yaml.safe_load(texto)", False),
    "verificación desactivada": ("requests.get(url, verify=False)", True),
    "verificación activa": ("requests.get(url, timeout=5)", False),
    "advertencia en comentario": ("# nunca uses eval(entrada) aquí\nr = ast.literal_eval(entrada)", False),
    "mensaje que menciona md5": ("msg = 'el md5 está prohibido'", False),
    "alias del hash débil": ("from hashlib import md5 as h\nx = h(dato)", True),
    "alias de eval": ("f = eval\nr = f(entrada)", True),
    "consulta en f-string": ("q = f'SELECT * FROM n WHERE id = {i}'\ncur.execute(q)", True),
}


def _ast_marca(codigo: str) -> bool:
    arbol = ast.parse(codigo)
    for n in ast.walk(arbol):
        if isinstance(n, ast.Call):
            nombre = ast.unparse(n.func)
            if nombre == "eval":
                return True
            if nombre.endswith("md5"):
                return True
            if nombre == "yaml.load" and len(n.args) + len(n.keywords) < 2:
                return True
            for kw in n.keywords:
                if kw.arg == "shell" and isinstance(kw.value, ast.Constant) and kw.value.value is True:
                    return True
                if kw.arg == "verify" and isinstance(kw.value, ast.Constant) and kw.value.value is False:
                    return True
            if nombre.endswith(".execute") and n.args and isinstance(n.args[0], ast.Name):
                return True  # consulta construida en otra línea: se marca por sospecha
    for n in ast.walk(arbol):
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add) and isinstance(n.left, ast.Constant) and isinstance(n.left.value, str) and "SELECT" in n.left.value:
            return True
    return False


def e466_patrones() -> dict:
    """Doce fragmentos (6 inseguros, 6 seguros): búsqueda de texto frente a recorrido del árbol sintáctico."""
    texto_pat = [r"SELECT.*\+", r"\beval\(", r"shell=True", r"md5", r"yaml\.load\(", r"verify=False"]
    filas = []
    for etiqueta, f in (("texto", lambda c: any(re.search(p, c) for p in texto_pat)), ("árbol", _ast_marca)):
        tp = fp = fn = 0
        for nombre, (codigo, inseguro) in SNIPPETS.items():
            m = f(codigo)
            tp += m and inseguro
            fp += m and not inseguro
            fn += (not m) and inseguro
        filas.append({"tecnica": etiqueta, "verdaderos": tp, "falsos_positivos": fp, "omitidos": fn})
    return {"filas": filas, "inseguros": sum(1 for v in SNIPPETS.values() if v[1])}


def _huellas(src: str, n: int = 5, normalizar: bool = False):
    import keyword
    toks = re.findall(r"[A-Za-z_]+|\d+|[^\sA-Za-z_\d]", src)
    if normalizar:
        toks = ["ID" if re.match(r"[A-Za-z_]", t) and not keyword.iskeyword(t) else t for t in toks]
    return {tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)}


def e466_similitud() -> dict:
    """Parecido de fragmentos generados con un corpus con licencia: copia, copia renombrada, idioma común e independiente."""
    rng = random.Random(4666)
    corpus_fn = """
def promedio_ponderado(valores, pesos):
    total = 0.0
    peso_total = 0.0
    for valor, peso in zip(valores, pesos):
        total += valor * peso
        peso_total += peso
    if peso_total == 0:
        raise ValueError("pesos nulos")
    return total / peso_total
"""
    copia = corpus_fn
    renombrada = corpus_fn.replace("valores", "xs").replace("pesos", "ws").replace("total", "acc").replace("peso_total", "sw")
    idioma = "for i in range(len(xs)):\n    if xs[i] > 0:\n        out.append(xs[i])\n"
    independiente = """
def media_ponderada(notas, coef):
    num = sum(n * c for n, c in zip(notas, coef))
    den = sum(coef)
    return num / den if den else None
"""
    idioma_txt = "for i in range(len(xs)):" + chr(10) + "    if xs[i] > 0:" + chr(10) + "        out.append(xs[i])" + chr(10)
    def jac(a, b):
        return len(a & b) / len(a | b) if a | b else 0
    filas = []
    for nombre, src in (("copia literal", copia), ("copia con nombres cambiados", renombrada), ("idioma común (corpus de bucles)", idioma), ("solución independiente", independiente)):
        ref_txt = idioma_txt if nombre.startswith("idioma") else corpus_fn
        fila = {"caso": nombre}
        for etiqueta, norm in (("literal", False), ("normalizada", True)):
            h, ref = _huellas(src, normalizar=norm), _huellas(ref_txt, normalizar=norm)
            fila[etiqueta] = round(len(h & ref) / len(h), 2) if h else 0
        filas.append(fila)
    return {"filas": filas}


# ------------------------------------------------------------------ SE-563
def e467_flujos() -> dict:
    """200 tareas sintéticas en tres flujos; mediana de horas, defectos que escapan, intervalo por bootstrap."""
    rng = random.Random(467)
    n = 200
    tareas = [(rng.lognormvariate(0.9, 0.5), rng.random() < 0.3) for _ in range(n)]  # (horas manuales, es tarea difícil)
    def ejecutar(flujo):
        horas, escapan = [], 0
        for h, dificil in tareas:
            if flujo == "manual":
                t, p_def = h, 0.06
            elif flujo == "asistido":
                p_ok = 0.55 if dificil else 0.85
                ok = rng.random() < p_ok
                t = 0.35 * h + 0.25 * h + (0 if ok else 0.8 * h)  # generar + revisar + rehacer
                p_def = 0.05 if ok else 0.12
            else:  # automatizado
                p_ok = 0.40 if dificil else 0.75
                ok = rng.random() < p_ok
                t = 0.10 * h + 0.30 * h + (0 if ok else 1.0 * h)  # preparar + revisar el resultado + rehacer
                p_def = 0.09 if ok else 0.25
            horas.append(t)
            escapan += rng.random() < p_def
        return horas, escapan
    filas = []
    for flujo in ("manual", "asistido", "automatizado"):
        horas, esc = ejecutar(flujo)
        boots = sorted(statistics.median(rng.choices(horas, k=n)) for _ in range(1000))
        filas.append({"flujo": flujo, "mediana_h": round(statistics.median(horas), 2), "ic95": [round(boots[25], 2), round(boots[975], 2)],
                      "total_h": round(sum(horas), 1), "defectos_escapan": esc})
    return {"n": n, "filas": filas}


def e467_sensibilidad() -> dict:
    """Con qué tasa de aciertos el flujo asistido deja de ahorrar tiempo frente al manual (revisión fija)."""
    filas = []
    for p_ok in (0.9, 0.7, 0.5, 0.35, 0.2):
        for coste_rehacer in (0.8,):
            ahorro = 1 - (0.35 + 0.25 + (1 - p_ok) * coste_rehacer)
            filas.append({"aciertos": pct(p_ok, 0), "horas_relativas": round(1 - ahorro, 2), "ahorro": pct(ahorro, 0)})
    equilibrio = 1 - (1 - 0.6) / 0.8
    return {"filas": filas, "p_equilibrio": pct(equilibrio, 0)}


def e467_diseno() -> dict:
    """Detectar un 15 % de diferencia en tiempo: diseño pareado frente a grupos distintos, según el número de tareas."""
    rng = random.Random(4672)
    filas = []
    for n in (10, 20, 40, 80):
        det_pareado = det_indep = 0
        reps = 600
        for _ in range(reps):
            base = [rng.lognormvariate(1.0, 0.8) for _ in range(n)]
            manual = [b * rng.lognormvariate(0, 0.15) for b in base]
            asist = [b * 0.85 * rng.lognormvariate(0, 0.15) for b in base]
            difs = [m - a for m, a in zip(manual, asist)]
            t = statistics.mean(difs) / (statistics.stdev(difs) / math.sqrt(n))
            det_pareado += t > 1.7
            otras = [rng.lognormvariate(1.0, 0.8) * 0.85 * rng.lognormvariate(0, 0.15) for _ in range(n)]
            sp = math.sqrt((statistics.variance(manual) + statistics.variance(otras)) / 2)
            t2 = (statistics.mean(manual) - statistics.mean(otras)) / (sp * math.sqrt(2 / n))
            det_indep += t2 > 1.7
        filas.append({"tareas": n, "pareado": pct(det_pareado / reps, 0), "independiente": pct(det_indep / reps, 0)})
    return {"filas": filas}


# ------------------------------------------------------------------ SE-564
def _enlaza(anterior: str, entrada: dict) -> str:
    cuerpo = json.dumps(entrada, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256((anterior + cuerpo).encode("utf-8")).hexdigest()


def e468_bitacora() -> dict:
    """Bitácora encadenada por hash de un cambio asistido; se manipulan entradas y se verifica."""
    entradas = [
        {"paso": 1, "actor": "persona", "accion": "define criterios de aceptación", "artefacto": "criterios.md"},
        {"paso": 2, "actor": "asistente", "accion": "propone parche", "artefacto": "parche-1.diff", "modelo": "<MODELO_EJEMPLO>"},
        {"paso": 3, "actor": "persona", "accion": "rechaza hunk 2 y pide prueba", "artefacto": "revision-1.md"},
        {"paso": 4, "actor": "asistente", "accion": "propone parche 2 y prueba", "artefacto": "parche-2.diff"},
        {"paso": 5, "actor": "persona", "accion": "ejecuta pruebas y aprueba", "artefacto": "resultado-pruebas.txt"},
        {"paso": 6, "actor": "persona", "accion": "integra el cambio", "artefacto": "commit"},
    ]
    with tempfile.TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "bitacora.jsonl"
        h = "0" * 64
        with ruta.open("w", encoding="utf-8", newline="\n") as f:
            for e in entradas:
                h = _enlaza(h, e)
                f.write(json.dumps({"entrada": e, "hash": h}, ensure_ascii=False, sort_keys=True) + "\n")
        lineas = ruta.read_text(encoding="utf-8").splitlines()

    def verificar(lineas):
        h = "0" * 64
        for i, l in enumerate(lineas):
            r = json.loads(l)
            h = _enlaza(h, r["entrada"])
            if h != r["hash"]:
                return i + 1
        return 0
    base = verificar(lineas)
    r = {"integra": base == 0, "lineas": len(lineas)}
    # manipulaciones
    mod = lineas[:]
    d = json.loads(mod[2]); d["entrada"]["accion"] = "aprueba hunk 2"; mod[2] = json.dumps(d, ensure_ascii=False, sort_keys=True)
    r["editar_entrada_3_detectada_en"] = verificar(mod)
    mod = lineas[:2] + lineas[3:]
    r["borrar_entrada_3_detectada_en"] = verificar(mod)
    mod = lineas[:]
    mod[1], mod[2] = mod[2], mod[1]
    r["intercambiar_2_y_3_detectada_en"] = verificar(mod)
    # reescribir todo desde un punto con hashes recalculados: la cadena local no lo detecta
    d = json.loads(lineas[2]); d["entrada"]["accion"] = "aprueba hunk 2"
    nuevo = lineas[:2]
    h = json.loads(lineas[1])["hash"]
    for l in [json.dumps(d)] + lineas[3:]:
        e = json.loads(l)["entrada"]
        h = _enlaza(h, e)
        nuevo.append(json.dumps({"entrada": e, "hash": h}, ensure_ascii=False, sort_keys=True))
    r["recalcular_la_cola_detectada_en"] = verificar(nuevo)
    r["ancla_externa_ultimo_hash_coincide"] = json.loads(nuevo[-1])["hash"] == json.loads(lineas[-1])["hash"]
    return r


def e468_compuertas() -> dict:
    """Defectos que llegan a producción según qué compuertas existan (pruebas, análisis estático, revisión humana, canario)."""
    rng = random.Random(468)
    compuertas = {"pruebas": 0.55, "análisis estático": 0.25, "revisión humana": 0.45, "canario": 0.35}
    conjuntos = [("sin compuertas", []), ("solo pruebas", ["pruebas"]), ("pruebas + análisis", ["pruebas", "análisis estático"]),
                 ("pruebas + análisis + revisión", ["pruebas", "análisis estático", "revisión humana"]),
                 ("las cuatro", list(compuertas))]
    filas = []
    n = 10000
    for nombre, cs in conjuntos:
        llegan = 0
        for _ in range(n):
            if rng.random() < 0.20:  # el cambio asistido trae un defecto
                if all(rng.random() > compuertas[c] for c in cs):
                    llegan += 1
        filas.append({"compuertas": nombre, "defectos_en_produccion": llegan, "de": n})
    # revisión humana con fatiga: detección cae con el tamaño del cambio
    fatiga = []
    for lineas in (20, 100, 400, 1000):
        p = 0.45 / (1 + lineas / 150)
        fatiga.append({"lineas": lineas, "p_detectar": pct(p)})
    return {"filas": filas, "fatiga": fatiga}


def e468_reversion() -> dict:
    """Revertir un cambio de 40 líneas tras k ediciones posteriores; ediciones al azar sobre 400 líneas."""
    rng = random.Random(4682)
    filas = []
    total = 4000
    for k in (0, 5, 20, 60, 150):
        limpia = 0
        for _ in range(total):
            cambio = set()
            for ini in rng.sample(range(0, 390, 10), 4):
                cambio |= set(range(ini, ini + 10))
            ed = {rng.randrange(400) for _ in range(k)}
            # una reversión limpia necesita que ninguna edición posterior toque las líneas del cambio ni las contiguas
            vecinas = cambio | {x + 1 for x in cambio} | {x - 1 for x in cambio}
            limpia += not (ed & vecinas)
        filas.append({"ediciones_posteriores": k, "reversion_limpia": pct(limpia / total)})
    return {"filas": filas}


def todo() -> dict:
    return {
        "e463_umbral": e463_umbral(), "e463_equivalencia": e463_equivalencia(), "e463_explicacion": e463_explicacion(),
        "e464_ambiguedad": e464_ambiguedad(), "e464_distractores": e464_distractores(), "e464_reglas": e464_reglas(),
        "e465_tamano": e465_tamano(), "e465_frontera": e465_frontera(), "e465_juez": e465_juez(),
        "e466_escaner": e466_escaner(), "e466_patrones": e466_patrones(), "e466_similitud": e466_similitud(),
        "e467_flujos": e467_flujos(), "e467_sensibilidad": e467_sensibilidad(), "e467_diseno": e467_diseno(),
        "e468_bitacora": e468_bitacora(), "e468_compuertas": e468_compuertas(), "e468_reversion": e468_reversion(),
    }


if __name__ == "__main__":
    json.dump(todo(), sys.stdout, ensure_ascii=False, indent=1)
