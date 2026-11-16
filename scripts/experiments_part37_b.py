"""Experimentos sintéticos de las clases SE-451 a SE-456 (compras, licencias, economía, entrevistas, revisión de decisiones y dossier).

Todo usa la biblioteca estándar y semillas fijas. Los proveedores, las licencias de las dependencias, los commits, los
proyectos y los dossiers son construcciones del autor. Ningún experimento consulta datos de una organización real.
Ejecutar ``python scripts/experiments_part37_b.py`` imprime los resultados como JSON.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import random
import re
import statistics as st
import sys
import tempfile
from pathlib import Path


def pct(values: list[float], q: float) -> float:
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, math.ceil(q / 100 * len(ordered)) - 1))
    return ordered[index]


def poisson(rng: random.Random, lam: float) -> int:
    limit, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= limit:
            return k
        k += 1


# ---------------------------------------------------------------- SE-451
CRITERIOS = ["funcionalidad", "seguridad", "costo", "integración", "soporte", "salida"]
PROVEEDORES = {"A": [9, 6, 4, 8, 7, 3], "B": [7, 8, 6, 6, 8, 6], "C": [6, 7, 9, 5, 5, 8], "D": [8, 5, 7, 9, 6, 4], "E": [5, 9, 5, 4, 9, 7]}
PESOS_BASE = [0.25, 0.20, 0.15, 0.15, 0.15, 0.10]


def e451_pesos() -> dict:
    """Cinco proveedores con puntajes fijos: cuánto depende el ganador de los pesos."""
    base = {k: round(sum(w * s for w, s in zip(PESOS_BASE, v)), 2) for k, v in PROVEEDORES.items()}
    rng = random.Random(4510)
    victorias = {k: 0 for k in PROVEEDORES}
    victorias_puerta = {k: 0 for k in PROVEEDORES}
    n = 20000
    for _ in range(n):
        g = [rng.gammavariate(1.0, 1.0) for _ in CRITERIOS]
        w = [x / sum(g) for x in g]
        puntaje = {k: sum(a * b for a, b in zip(w, v)) for k, v in PROVEEDORES.items()}
        victorias[max(puntaje, key=lambda k: puntaje[k])] += 1
        elegibles = {k: s for k, s in puntaje.items() if PROVEEDORES[k][1] >= 6}
        victorias_puerta[max(elegibles, key=lambda k: elegibles[k])] += 1
    orden = sorted(base.values(), reverse=True)
    return {"puntaje_con_pesos_base": base, "diferencia_entre_primero_y_segundo": round(orden[0] - orden[1], 2),
            "victorias_con_pesos_al_azar_pct": {k: round(100 * v / n, 1) for k, v in victorias.items()},
            "victorias_exigiendo_seguridad_6_o_mas_pct": {k: round(100 * v / n, 1) for k, v in victorias_puerta.items() if v}}


def e451_costo_total() -> dict:
    """Comprar frente a construir a cinco años con alzas, descontinuación y sobrecostos (unidades monetarias del autor)."""
    rng = random.Random(4511)
    comprar, construir = [], []
    for _ in range(10000):
        cuota, total, vivo = 100.0, 80.0, True
        for anio in range(5):
            if rng.random() < 0.30:
                cuota *= 1.4
            total += cuota
            if vivo and rng.random() < 0.04:
                vivo = False
                total += 300.0 * math.exp(rng.gauss(0, 0.5)) + cuota  # migración forzada y un año de doble costo
                cuota = 100.0
        comprar.append(total)
        capex = 450.0 * math.exp(rng.gauss(0, 0.35) - 0.35 ** 2 / 2)
        total_c, mant = capex, 70.0
        for anio in range(5):
            total_c += mant
            mant *= 1.05
            if rng.random() < 0.10:
                total_c += 60.0
        construir.append(total_c)
    return {"comprar": {"mediana": round(st.median(comprar), 0), "p90": round(pct(comprar, 90), 0), "media": round(st.mean(comprar), 0)},
            "construir": {"mediana": round(st.median(construir), 0), "p90": round(pct(construir, 90), 0), "media": round(st.mean(construir), 0)},
            "p_comprar_cuesta_mas_pct": round(100 * sum(a > b for a, b in zip(comprar, construir)) / len(comprar), 1)}


def e451_disponibilidad() -> dict:
    """Disponibilidad de una cadena de proveedores y valor de los créditos de un SLA."""
    resultado = {}
    anio_min = 365 * 24 * 60
    for nombre, disp in (("1 proveedor al 99,9 %", [0.999]), ("3 proveedores al 99,9 %", [0.999] * 3), ("5 proveedores al 99,9 %", [0.999] * 5),
                         ("5 proveedores, el más débil duplicado", [0.999] * 4 + [1 - (1 - 0.999) ** 2])):
        a = math.prod(disp)
        rng = random.Random(4512)
        simulados = []
        for _ in range(600):
            intervalos = []
            for d in disp:
                eventos = poisson(rng, (1 - d) * anio_min / 45.0)
                for _ in range(eventos):
                    ini = rng.uniform(0, anio_min)
                    intervalos.append((ini, ini + rng.expovariate(1 / 45.0)))
            intervalos.sort()
            total, fin = 0.0, -1.0
            for ini, f in intervalos:
                ini2 = max(ini, fin)
                if f > ini2:
                    total += f - ini2
                    fin = f
            simulados.append(total)
        resultado[nombre] = {"disponibilidad_analitica_pct": round(100 * a, 3), "minutos_caidos_al_anio_analitico": round((1 - a) * anio_min, 0),
                             "minutos_caidos_simulados": round(st.mean(simulados), 0)}
    resultado["credito_frente_a_perdida"] = {"credito_maximo_por_mes": 200, "perdida_por_hora": 5000,
                                              "perdida_de_una_caida_de_3_horas": 3 * 5000, "credito_equivalente_a_minutos": round(200 / 5000 * 60, 1)}
    return resultado


# ---------------------------------------------------------------- SE-452
NIVEL = {"MIT": 0, "Apache-2.0": 0, "BSD-3-Clause": 0, "ISC": 0, "MPL-2.0": 1, "LGPL-3.0-only": 1, "GPL-2.0-only": 2, "GPL-3.0-only": 2, "AGPL-3.0-only": 2}
EXCEPCION = {"Classpath-exception-2.0"}


def nivel_expresion(expr: str) -> int:
    """0 permitido, 1 revisar, 2 bloqueado, 3 desconocido; OR toma la mejor opción y AND la peor."""
    tokens = re.findall(r"\(|\)|[A-Za-z0-9.\-:+]+", expr)
    pos = 0

    def alt() -> int:
        nonlocal pos
        v = conj()
        while pos < len(tokens) and tokens[pos] == "OR":
            pos += 1
            v = min(v, conj())
        return v

    def conj() -> int:
        nonlocal pos
        v = atomo()
        while pos < len(tokens) and tokens[pos] == "AND":
            pos += 1
            v = max(v, atomo())
        return v

    def atomo() -> int:
        nonlocal pos
        if pos >= len(tokens):
            return 3
        t = tokens[pos]
        if t == "(":
            pos += 1
            v = alt()
            pos += 1
            return v
        pos += 1
        v = NIVEL.get(t, 3)
        if pos < len(tokens) and tokens[pos] == "WITH":
            pos += 1
            exc = tokens[pos]
            pos += 1
            v = min(v, 1) if exc in EXCEPCION and v == 2 else v
        return v

    return alt() if tokens else 3


def e452_licencias() -> dict:
    """60 dependencias sintéticas: política de distribución propietaria frente a una búsqueda ingenua de 'GPL'."""
    pool = ["MIT", "Apache-2.0", "BSD-3-Clause", "ISC", "MPL-2.0", "LGPL-3.0-only", "GPL-3.0-only", "AGPL-3.0-only", "MIT OR GPL-2.0-only",
            "Apache-2.0 AND BSD-3-Clause", "GPL-2.0-only WITH Classpath-exception-2.0", "(MIT OR Apache-2.0)", "", "NOASSERTION", "LicenseRef-propietaria", "GPL-2.0-only AND MIT"]
    pesos = [14, 10, 8, 4, 3, 3, 2, 1, 3, 3, 1, 3, 2, 2, 1, 1]
    rng = random.Random(4520)
    deps = rng.choices(pool, pesos, k=60)
    verdad = [nivel_expresion(d) for d in deps]
    ingenuo = ["GPL" in d for d in deps]
    reales_bloqueadas = [v == 2 for v in verdad]
    nombres = ["permitida", "revisar", "bloqueada", "desconocida"]
    return {"por_clase": {nombres[i]: verdad.count(i) for i in range(4)},
            "busqueda_ingenua_marca": sum(ingenuo),
            "ingenua_marca_pero_no_esta_bloqueada": sum(a and not b for a, b in zip(ingenuo, reales_bloqueadas)),
            "bloqueadas_que_la_ingenua_no_ve": sum((not a) and b for a, b in zip(ingenuo, reales_bloqueadas)),
            "desconocidas_que_la_ingenua_da_por_buenas": sum(v == 3 and not a for a, v in zip(ingenuo, verdad)),
            "casos_clave": {e: nivel_expresion(e) for e in ("MIT OR GPL-2.0-only", "GPL-2.0-only AND MIT", "LGPL-3.0-only", "GPL-2.0-only WITH Classpath-exception-2.0", "", "LicenseRef-propietaria")}}


TRAILER = re.compile(r"^Signed-off-by: (?P<nombre>[^<]+) <(?P<correo>[^>\s]+@[^>\s]+)>$")


def e452_procedencia() -> dict:
    """2 000 mensajes de commit sintéticos: sign-off del autor (DCO) con una búsqueda ingenua y con un análisis estricto."""
    rng = random.Random(4521)
    autores = [("Ana Soto", "ana@ejemplo.test"), ("Beto Rey", "beto@ejemplo.test"), ("Cami Paz", "cami@ejemplo.test"), ("Dante Vega", "dante@ejemplo.test")]
    mensajes = []
    for i in range(2000):
        nombre, correo = rng.choice(autores)
        r = rng.random()
        cuerpo = f"Cambio {i}: ajusta la regla de cierre.\n\nExplica el motivo en dos líneas."
        if r < 0.86:
            pie, tipo = f"\n\nSigned-off-by: {nombre} <{correo}>", "correcto"
        elif r < 0.90:
            pie, tipo = "", "sin firma"
        elif r < 0.93:
            pie, tipo = "\n\nSigned-off-by: Otra Persona <otra@ejemplo.test>", "firma de otra persona"
        elif r < 0.95:
            pie, tipo = f"\n\nSigned off by {nombre} <{correo}>", "mal escrita"
        elif r < 0.97:
            cuerpo += f"\n\nSigned-off-by: {nombre} <{correo}>\n\nNota posterior que no es un pie."
            pie, tipo = "", "firma en medio"
        else:
            pie, tipo = f"\n\nSigned-off-by: {nombre} <correo-roto>", "correo roto"
        mensajes.append((nombre, correo, cuerpo + pie, tipo))
    ingenuo = sum("Signed-off-by" in m for _, _, m, _ in mensajes)
    estricto = 0
    conteo = {}
    for nombre, correo, m, tipo in mensajes:
        ultimo = [ln for ln in m.rstrip().split("\n\n")[-1].split("\n") if ln.strip()]
        ok = bool(ultimo) and all(TRAILER.match(ln) for ln in ultimo) and any(TRAILER.match(ln).group("correo") == correo for ln in ultimo)
        estricto += ok
        conteo.setdefault(tipo, [0, 0])
        conteo[tipo][0] += 1
        conteo[tipo][1] += ok
    return {"commits": 2000, "ingenuo_da_por_firmados": ingenuo, "estricto_da_por_firmados": estricto,
            "por_tipo_total_y_aceptados_por_el_estricto": conteo}


def e452_patron_oscuro() -> dict:
    """Doce meses con un flujo de cancelación escondido frente a uno honesto (supuestos del autor)."""
    resultado = {}
    for nombre, conv, churn, quejas in (("flujo honesto", 0.040, 0.050, 0.004), ("cancelación escondida", 0.050, 0.035, 0.030)):
        suscriptores, acumulado, quejas_acum = 0.0, 0.0, 0.0
        cruces, hitos = [], {}
        for mes in range(1, 13):
            efecto = max(0.5, 1 - 0.0004 * quejas_acum)
            nuevos = 10000 * conv * efecto
            suscriptores = suscriptores * (1 - churn) + nuevos
            quejas_mes = (suscriptores * quejas)
            quejas_acum += quejas_mes
            ingreso = suscriptores * 10.0 - quejas_mes * 25.0
            acumulado += ingreso
            if mes in (3, 6, 12):
                hitos[f"mes {mes}"] = {"ingreso_neto_acumulado": round(acumulado, 0), "reclamos_acumulados": round(quejas_acum, 0), "suscriptores": round(suscriptores, 0)}
        resultado[nombre] = hitos
    # mes en que el flujo honesto supera al oculto
    def acumulados(conv: float, churn: float, quejas: float) -> list[float]:
        s = a = q = 0.0
        salida = []
        for _ in range(12):
            e = max(0.5, 1 - 0.0004 * q)
            s = s * (1 - churn) + 10000 * conv * e
            qm = s * quejas
            q += qm
            a += s * 10.0 - qm * 25.0
            salida.append(a)
        return salida
    h, o = acumulados(0.040, 0.050, 0.004), acumulados(0.050, 0.035, 0.030)
    resultado["mes_en_que_el_honesto_supera_al_oculto"] = next((i + 1 for i in range(12) if h[i] > o[i]), None)
    ventaja = o[-1] - h[-1]
    reclamos_extra = resultado["cancelación escondida"]["mes 12"]["reclamos_acumulados"] - resultado["flujo honesto"]["mes 12"]["reclamos_acumulados"]
    resultado["ventaja_del_flujo_oculto_a_12_meses"] = round(ventaja, 0)
    resultado["probabilidad_de_sancion_por_reclamo_que_anula_la_ventaja_si_la_sancion_cuesta_20000_pct"] = round(100 * ventaja / (reclamos_extra * 20000), 2)
    return resultado


# ---------------------------------------------------------------- SE-453
def e453_costo_de_demora() -> dict:
    """Doce elementos con costo de demora semanal y duración: cuatro órdenes de ejecución (3 000 carteras)."""
    rng = random.Random(4530)
    razones = {"orden de llegada": [], "lo más corto primero": [], "mayor costo de demora primero": [], "costo de demora entre duración": []}
    for _ in range(3000):
        items = [(10 * math.exp(rng.gauss(0, 0.8)), rng.randint(1, 8)) for _ in range(12)]
        def total(orden):
            t, c = 0, 0.0
            for cod, dur in orden:
                t += dur
                c += cod * t
            return c
        optimo = total(sorted(items, key=lambda x: -x[0] / x[1]))
        razones["orden de llegada"].append(total(items) / optimo)
        razones["lo más corto primero"].append(total(sorted(items, key=lambda x: x[1])) / optimo)
        razones["mayor costo de demora primero"].append(total(sorted(items, key=lambda x: -x[0])) / optimo)
        razones["costo de demora entre duración"].append(total(sorted(items, key=lambda x: -x[0] / x[1])) / optimo)
    return {k: {"costo_medio_frente_al_optimo": round(st.mean(v), 2), "peor_caso_p95": round(pct(v, 95), 2)} for k, v in razones.items()}


def npv(flujos: list[float], tasa: float) -> float:
    return sum(f / (1 + tasa) ** i for i, f in enumerate(flujos))


def tir(flujos: list[float]) -> float:
    lo, hi = -0.9, 5.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if npv(flujos, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def e453_valor_presente() -> dict:
    proyectos = {"Automatizar el cierre": [-100, 50, 50, 30, 20, 10], "Rediseñar el módulo": [-100, 10, 20, 40, 60, 80], "Plataforma interna": [-100, 0, 0, 0, 0, 240]}
    resultado = {}
    for nombre, f in proyectos.items():
        acum, retorno = 0.0, None
        for i, x in enumerate(f):
            acum += x
            if acum >= 0 and retorno is None:
                retorno = i
        resultado[nombre] = {"suma_sin_descontar": sum(f), "VAN_5_pct": round(npv(f, 0.05), 1), "VAN_10_pct": round(npv(f, 0.10), 1), "VAN_20_pct": round(npv(f, 0.20), 1),
                             "VAN_30_pct": round(npv(f, 0.30), 1), "recuperacion_en_anios": retorno, "TIR_pct": round(100 * tir(f), 1)}
    for tasa in (0.05, 0.10, 0.20, 0.30):
        orden = sorted(proyectos, key=lambda n: -npv(proyectos[n], tasa))
        resultado[f"orden_por_VAN_a_{int(tasa * 100)}_pct"] = orden
    return resultado


def e453_capex_opex() -> dict:
    """Servidores propios frente a nube, y la economía por usuario (unidades monetarias del autor)."""
    r = 0.008
    acum_p, acum_n, cruce, cruce_desc = 36000.0, 0.0, None, None
    vp_p, vp_n, cruce_vp = 36000.0, 0.0, None
    for mes in range(1, 121):
        acum_p += 1200.0
        acum_n += 2300.0
        vp_p += 1200.0 / (1 + r) ** mes
        vp_n += 2300.0 / (1 + r) ** mes
        if cruce is None and acum_p < acum_n:
            cruce = mes
        if cruce_vp is None and vp_p < vp_n:
            cruce_vp = mes
    equilibrio = 20000.0 / (4.0 - 0.8)
    margen = {f"{u} usuarios": round(100 * (u * 4.0 - 20000.0 - u * 0.8) / (u * 4.0), 1) for u in (3000, 6250, 10000, 30000)}
    resultado = {"mes_en_que_lo_propio_cuesta_menos_sin_descontar": cruce, "mes_con_tasa_mensual_0_8_pct": cruce_vp, "usuarios_de_equilibrio": equilibrio, "margen_pct_por_tamano": margen}
    probs = {}
    for u0 in (2000, 4000, 6000):
        rng = random.Random(4532)
        ok = 0
        for _ in range(6000):
            u = u0
            for _ in range(12):
                u *= 1 + rng.gauss(0.04, 0.05)
            ok += u >= equilibrio
        probs[f"{u0} usuarios iniciales"] = round(100 * ok / 6000, 1)
    resultado["prob_de_llegar_al_equilibrio_en_12_meses_pct"] = probs
    return resultado


# ---------------------------------------------------------------- SE-454
def e454_entrevistas() -> dict:
    """Contratar 1 de 10 candidatos: rasgos ajenos a la habilidad (halo) y ruido, con y sin estructura."""
    resultado = {}
    for nombre, halo, ruido, k in (("1 conversación libre", 0.8, 1.0, 1), ("3 conversaciones libres", 0.8, 1.0, 3), ("1 entrevista estructurada", 0.2, 0.7, 1), ("3 entrevistas estructuradas", 0.2, 0.7, 3)):
        rng = random.Random(4540)
        elegidos, mejores = [], []
        for _ in range(8000):
            hab = [rng.gauss(0, 1) for _ in range(10)]
            rasgo = [rng.gauss(0, 1) for _ in range(10)]
            punt = [h + halo * c + st.mean(rng.gauss(0, ruido) for _ in range(k)) for h, c in zip(hab, rasgo)]
            elegidos.append(hab[max(range(10), key=lambda i: punt[i])])
            mejores.append(max(hab))
        resultado[nombre] = {"habilidad_media_de_la_persona_elegida": round(st.mean(elegidos), 2), "fraccion_del_maximo_alcanzable_pct": round(100 * st.mean(elegidos) / st.mean(mejores), 1)}
    resultado["referencia_al_azar"] = 0.0
    return resultado


REGLAS = {
    "comando reproducible": re.compile(r"```[a-z]*\n(?:\$ )?(python|pytest|make|npm|docker)\b"),
    "resultado con cifra y unidad": re.compile(r"\d+([.,]\d+)?\s?(ms|%|s\b|usuarios|filas|MB|x\b)"),
    "límite declarado": re.compile(r"(?i)(no se (midió|probó|validó)|## límites)"),
    "decisión y alternativa": re.compile(r"(?is)(?=.*alternativa)(?=.*(descart|elegí|decidí))"),
    "enlace a evidencia": re.compile(r"\]\((https?://|\.\./|evidencia/)"),
    "versión y entorno": re.compile(r"(Python|Node|PostgreSQL|Linux|Windows)\s?\d"),
}

ENTRADAS = {
    "entrada con evidencia": "# Cola de cierre\n\nElegí una cola con reintentos; la alternativa (cron cada minuto) la descarté porque duplicaba cierres.\n\n```bash\npython -m cierre.bench --semilla 7\n```\n\nCon Python 3.12 en Linux 6 el p95 bajó de 840 ms a 310 ms ([informe](evidencia/bench.txt)).\n\n## Límites\n\nNo se midió con más de 5 000 filas.\n",
    "entrada a medias": "# Panel de notas\n\nConstruí un panel con React que mejora la experiencia. El p95 pasó a 300 ms en mi equipo.\n\nVer [repositorio](https://ejemplo.test/panel).\n",
    "entrada de adjetivos": "# Plataforma escalable\n\nDesarrollé una solución robusta, innovadora y de alto rendimiento para los usuarios.\n",
    "entrada con relleno": "# Todo\n\nalternativa elegí.\n\n```bash\npython x\n```\n\n1 ms 2 %\n\nNo se midió nada. Python 3 Windows 11 ([x](evidencia/x)).\n",
}


def e454_portafolio() -> dict:
    resultado = {}
    for nombre, texto in ENTRADAS.items():
        cumple = [r for r, rx in REGLAS.items() if rx.search(texto)]
        resultado[nombre] = {"reglas_cumplidas": len(cumple), "faltan": [r for r in REGLAS if r not in cumple]}
    return resultado


def e454_defensa() -> dict:
    """Preguntas de profundidad creciente: qué pasa con quien declara más de lo que sabe."""
    resultado = {}
    for profundidad in (2, 4):
        for estrategia in ("defiende todo con seguridad", "declara su límite y propone cómo comprobar"):
            rng = random.Random(4542)
            puntajes, detectado = [], 0
            n = 6000
            for _ in range(n):
                p, descubierto, uso_limite = 0.0, False, False
                for nivel in range(1, 7):
                    if nivel <= profundidad:
                        p += 1.0
                    elif estrategia.startswith("defiende"):
                        if rng.random() < 0.2:
                            p += 1.0
                        elif rng.random() < 0.8:
                            p -= 3.0
                            descubierto = True
                    else:
                        if not uso_limite:
                            p += 0.3
                            uso_limite = True
                        break
                puntajes.append(p)
                detectado += descubierto
            resultado[f"conocimiento de nivel {profundidad}, {estrategia}"] = {"impresion_media": round(st.mean(puntajes), 2), "descubierto_en_un_error_seguro_pct": round(100 * detectado / n, 1)}
    return resultado


# ---------------------------------------------------------------- SE-455
def e455_resultado_vs_proceso() -> dict:
    """Juzgar a quien decide por los resultados frente a juzgarlo por la calidad del proceso."""
    resultado = {}
    for n in (5, 10, 20, 50, 100):
        rng = random.Random(4550)
        acierto_res, acierto_proc = 0, 0
        ens = 4000
        for _ in range(ens):
            def decide(p_buena):
                buenas = [rng.random() < p_buena for _ in range(n)]
                exitos = sum(rng.random() < (0.75 if b else 0.45) for b in buenas)
                vistas = sum(b if rng.random() < 0.85 else (not b) for b in buenas)
                return exitos, vistas
            ra, pa = decide(0.65)
            rb, pb = decide(0.50)
            acierto_res += (ra > rb) + 0.5 * (ra == rb)
            acierto_proc += (pa > pb) + 0.5 * (pa == pb)
        resultado[f"{n} decisiones por persona"] = {"acierta_por_resultados_pct": round(100 * acierto_res / ens, 1), "acierta_por_proceso_pct": round(100 * acierto_proc / ens, 1)}
    return resultado


def e455_cobertura_de_riesgos() -> dict:
    """30 modos de fallo en tres dominios: cobertura de una revisión según la composición del panel."""
    resultado = {}
    for nombre, panel, mejora in (("4 revisores del mismo dominio", [0, 0, 0, 0], 1.0), ("2 y 2 de dos dominios", [0, 0, 1, 1], 1.0), ("un generalista y tres de dominios distintos", [3, 0, 1, 2], 1.0),
                                  ("un generalista y tres de dominios distintos, con ejercicio previo al fallo", [3, 0, 1, 2], 1.3)):
        rng = random.Random(4551)
        cobertura, peor = [], []
        for _ in range(5000):
            vistos = [False] * 30
            for revisor in panel:
                for modo in range(30):
                    dominio = modo // 10
                    p = 0.25 if revisor == 3 else (0.5 if revisor == dominio else 0.12)
                    if rng.random() < min(0.95, p * mejora):
                        vistos[modo] = True
            cobertura.append(100 * sum(vistos) / 30)
            peor.append(min(100 * sum(vistos[d * 10:(d + 1) * 10]) / 10 for d in range(3)))
        resultado[nombre] = {"cobertura_media_pct": round(st.mean(cobertura), 1), "dominio_peor_cubierto_pct": round(st.mean(peor), 1)}
    return resultado


def e455_calibracion() -> dict:
    """500 pronósticos por persona: confianza declarada frente a frecuencia de acierto."""
    confianzas = [0.55, 0.65, 0.75, 0.85, 0.95]
    resultado = {}
    for nombre, k in (("calibrada", 1.0), ("sobreconfiada", 0.5), ("siempre 95 %", None)):
        rng = random.Random(4552)
        tabla = {c: [0, 0] for c in confianzas}
        brier = 0.0
        n = 500
        for _ in range(n):
            c = 0.95 if k is None else rng.choice(confianzas)
            p_real = 0.62 if k is None else 0.5 + k * (c - 0.5)
            acierto = rng.random() < p_real
            brier += (c - acierto) ** 2
            tabla[c][0] += 1
            tabla[c][1] += acierto
        resultado[nombre] = {"brier": round(brier / n, 3), "frecuencia_de_acierto_por_confianza_pct": {str(c): (round(100 * v[1] / v[0], 1) if v[0] else None) for c, v in tabla.items()}}
    return resultado


# ---------------------------------------------------------------- SE-456
REQUERIDOS = ["README.md", "decision.md", "riesgos.md", "costos.md", "feedback.md", "LIMITES.md", "claims.csv"]


def crear_dossier(raiz: Path, variante: str) -> None:
    (raiz / "evidencia").mkdir(parents=True)
    textos = {
        "README.md": "# Dossier\n\n- C1: la cola reduce el p95 de 840 ms a 310 ms.\n- C2: el costo a 5 años es 1200 k.\n- C3: el riesgo principal es la pérdida de un conocedor.\n- C4: la decisión es reversible durante 30 días.\n- C5: la guardia rota entre 6 personas.\n",
        "decision.md": "# Decisión\n\nElegimos la cola. [[TCO_5A=1200]] [[REVERSIBLE_DIAS=30]]\n",
        "riesgos.md": "# Riesgos\n\nPérdida de conocimiento. [[PERSONAS_GUARDIA=6]]\n",
        "costos.md": "# Costos\n\nCosto a 5 años. [[TCO_5A=1200]]\n",
        "feedback.md": "# Retroalimentación\n\nRevisión semanal con rúbrica. [[REVISION_DIAS=7]]\n",
        "LIMITES.md": "# Límites\n\n- No se midió con tráfico real.\n- No se probó en otro sistema operativo.\n- Los costos son supuestos.\n",
    }
    if variante == "sin límites":
        textos["LIMITES.md"] = "# Límites\n"
    if variante == "cifra distinta":
        textos["costos.md"] = "# Costos\n\nCosto a 5 años. [[TCO_5A=1020]]\n"
        textos["riesgos.md"] = "# Riesgos\n\nPérdida de conocimiento. [[PERSONAS_GUARDIA=5]]\n"
    for nombre, t in textos.items():
        (raiz / nombre).write_text(t, encoding="utf-8", newline="\n")
    pruebas = {f"evidencia/e{i}.txt": f"salida del experimento {i}\n" for i in range(1, 6)}
    for nombre, t in pruebas.items():
        (raiz / nombre).write_text(t, encoding="utf-8", newline="\n")
    filas = []
    for i in range(1, 6):
        ruta = "" if (variante == "afirmación sin respaldo" and i == 5) else f"evidencia/e{i}.txt"
        h = hashlib.sha256((raiz / ruta).read_bytes()).hexdigest() if ruta else ""
        filas.append({"id": f"C{i}", "evidencia": ruta, "sha256": h})
    if variante == "evidencia alterada":
        (raiz / "evidencia/e2.txt").write_text("salida cambiada después de firmar\n", encoding="utf-8", newline="\n")
    if variante == "evidencia faltante":
        (raiz / "evidencia/e3.txt").unlink()
    with (raiz / "claims.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "evidencia", "sha256"])
        w.writeheader()
        w.writerows(filas)


def verificar_dossier(raiz: Path) -> list[str]:
    defectos = []
    for nombre in REQUERIDOS:
        if not (raiz / nombre).exists():
            defectos.append(f"falta {nombre}")
    lim = raiz / "LIMITES.md"
    if lim.exists() and sum(1 for ln in lim.read_text(encoding="utf-8").splitlines() if ln.startswith("- ")) < 3:
        defectos.append("LIMITES.md con menos de 3 límites")
    readme = (raiz / "README.md").read_text(encoding="utf-8") if (raiz / "README.md").exists() else ""
    ids = re.findall(r"- (C\d+):", readme)
    filas = {r["id"]: r for r in csv.DictReader((raiz / "claims.csv").open(encoding="utf-8"))} if (raiz / "claims.csv").exists() else {}
    for i in ids:
        fila = filas.get(i)
        if not fila or not fila["evidencia"]:
            defectos.append(f"{i} sin evidencia")
            continue
        ruta = raiz / fila["evidencia"]
        if not ruta.exists():
            defectos.append(f"{i} con evidencia ausente")
        elif hashlib.sha256(ruta.read_bytes()).hexdigest() != fila["sha256"]:
            defectos.append(f"{i} con evidencia alterada")
    return defectos


def cifras_inconsistentes(raiz: Path) -> list[str]:
    valores: dict[str, set[str]] = {}
    for md in sorted(raiz.glob("*.md")):
        for clave, valor in re.findall(r"\[\[([A-Z0-9_]+)=([^\]]+)\]\]", md.read_text(encoding="utf-8")):
            valores.setdefault(clave, set()).add(valor)
    return sorted(k for k, v in valores.items() if len(v) > 1)


def e456_verificador() -> dict:
    resultado = {}
    for variante in ("completo", "sin límites", "afirmación sin respaldo", "evidencia alterada", "evidencia faltante", "cifra distinta"):
        with tempfile.TemporaryDirectory() as tmp:
            raiz = Path(tmp) / "dossier"
            crear_dossier(raiz, variante)
            resultado[variante] = {"defectos": verificar_dossier(raiz), "cifras_en_conflicto": cifras_inconsistentes(raiz)}
    return resultado


def e456_muestreo() -> dict:
    """Un revisor inspecciona k de 30 afirmaciones: probabilidad de ver al menos una sin respaldo."""
    n = 30
    resultado = {}
    for m in (1, 3, 6):
        fila = {}
        for k in (3, 5, 8, 12):
            exacta = 1 - math.comb(n - m, k) / math.comb(n, k)
            rng = random.Random(4562)
            vistas = sum(any(i < m for i in rng.sample(range(n), k)) for _ in range(20000))
            fila[f"revisa {k}"] = {"exacta_pct": round(100 * exacta, 1), "simulada_pct": round(100 * vistas / 20000, 1)}
        resultado[f"{m} sin respaldo de {n}"] = fila
    return resultado


def e456_ruta_de_cambios() -> dict:
    """Revisión con y sin trazabilidad: cuántas afirmaciones de 30 se pueden comprobar en 60 minutos."""
    resultado = {}
    for nombre, minutos_por_afirmacion in (("sin trazabilidad (se busca la evidencia a mano)", 9.0), ("con tabla afirmación-evidencia-huella", 2.5)):
        rng = random.Random(4563)
        comprobadas = []
        for _ in range(5000):
            t, c = 0.0, 0
            while True:
                t += minutos_por_afirmacion * math.exp(rng.gauss(0, 0.4))
                if t > 60 or c >= 30:
                    break
                c += 1
            comprobadas.append(c)
        resultado[nombre] = {"afirmaciones_comprobadas_en_60_min_media": round(st.mean(comprobadas), 1), "p10": pct(comprobadas, 10), "p90": pct(comprobadas, 90)}
    return resultado


EXPERIMENTS = {
    "e451_pesos": e451_pesos, "e451_costo_total": e451_costo_total, "e451_disponibilidad": e451_disponibilidad,
    "e452_licencias": e452_licencias, "e452_procedencia": e452_procedencia, "e452_patron_oscuro": e452_patron_oscuro,
    "e453_costo_de_demora": e453_costo_de_demora, "e453_valor_presente": e453_valor_presente, "e453_capex_opex": e453_capex_opex,
    "e454_entrevistas": e454_entrevistas, "e454_portafolio": e454_portafolio, "e454_defensa": e454_defensa,
    "e455_resultado_vs_proceso": e455_resultado_vs_proceso, "e455_cobertura_de_riesgos": e455_cobertura_de_riesgos, "e455_calibracion": e455_calibracion,
    "e456_verificador": e456_verificador, "e456_muestreo": e456_muestreo, "e456_ruta_de_cambios": e456_ruta_de_cambios,
}

if __name__ == "__main__":
    elegidos = sys.argv[1:] or list(EXPERIMENTS)
    for nombre in elegidos:
        print(nombre, json.dumps(EXPERIMENTS[nombre](), ensure_ascii=False, sort_keys=True))
