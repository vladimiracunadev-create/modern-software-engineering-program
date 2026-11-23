"""Experimentos sintéticos de las clases SE-529 a SE-534 (liderazgo, equipos, comunicación, mentoría, compromisos y riesgo).

Todo usa la biblioteca estándar y semillas fijas. Las personas, los equipos, las decisiones y las
cifras son construcciones del autor: no proceden de ninguna organización real. Ejecutar
``python scripts/experiments_part44_a.py`` imprime los resultados como JSON.
"""
from __future__ import annotations

import json
import math
import random
import statistics as st
import sys
from itertools import combinations


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


# ---------------------------------------------------------------- SE-529
def e445_umbral() -> dict:
    """Adopción en una red de 30 personas: cada una adopta cuando la fracción de sus vecinos que ya adoptó alcanza su umbral."""
    n, equipos = 30, 2000
    resultado = {}
    for nombre, modo in (("solo un anuncio general", "ninguna"), ("2 personas al azar", "azar"),
                         ("2 personas muy conectadas", "centro"), ("2 personas poco conectadas", "periferia")):
        rng = random.Random(4450)
        finales = []
        for _ in range(equipos):
            vecinos: list[list[int]] = [[] for _ in range(n)]
            for i in range(n):
                for j in range(i + 1, n):
                    if rng.random() < 0.12:
                        vecinos[i].append(j)
                        vecinos[j].append(i)
            um = [min(1.0, max(0.1, rng.gauss(0.3, 0.1))) for _ in range(n)]
            grado = [len(v) for v in vecinos]
            if modo == "ninguna":
                semillas: list[int] = []
            elif modo == "azar":
                semillas = rng.sample(range(n), 2)
            else:
                orden = sorted(range(n), key=lambda i: (-grado[i], i))
                semillas = orden[:2] if modo == "centro" else orden[-2:]
            adopt = set(semillas)
            cambio = True
            while cambio:
                cambio = False
                for i in range(n):
                    if i not in adopt and grado[i] and sum(v in adopt for v in vecinos[i]) / grado[i] >= um[i]:
                        adopt.add(i)
                        cambio = True
            finales.append(len(adopt) / n)
        resultado[nombre] = {"mediana_adopcion_pct": round(100 * st.median(finales), 1),
                             "redes_con_80_o_mas_pct": round(100 * sum(f >= 0.8 for f in finales) / equipos, 1),
                             "redes_que_no_pasan_de_10_pct": round(100 * sum(f <= 0.1 for f in finales) / equipos, 1)}
    return resultado


def e445_cola() -> dict:
    """Cuello de botella: una persona aprueba toda decisión (recursión de Lindley en horas laborales)."""
    resultado = {}
    for nombre, lam in (("aprueba todo (5 por día)", 5.0), ("aprueba el 40 % (2 por día)", 2.0), ("criterios delegados (1 por día)", 1.0)):
        rng = random.Random(4451)
        tasa = lam / 8.0
        espera, w = [], 0.0
        for _ in range(40000):
            servicio = rng.expovariate(1 / 1.4)
            llegada = rng.expovariate(tasa)
            espera.append(w)
            w = max(0.0, w + servicio - llegada)
        resultado[nombre] = {"utilizacion": round(lam * 1.4 / 8, 3), "espera_media_h": round(st.mean(espera), 1),
                             "espera_p90_h": round(pct(espera, 90), 1)}
    return resultado


def e445_consulta() -> dict:
    """Consulta previa por escrito: cuántas decisiones se revierten según cuántas personas la leen antes."""
    resultado = {}
    for k in (0, 2, 4, 8):
        rng = random.Random(4452)
        revertidas, dias = 0, 0.0
        n = 6000
        for _ in range(n):
            graves_ocultas = 0
            for _ in range(poisson(rng, 1.2)):
                if rng.random() < 0.3:  # preocupación grave
                    visto = any(rng.random() < 0.2 for _ in range(k))  # 0,25 de verla por 0,8 de decirla
                    graves_ocultas += not visto
            if graves_ocultas:
                revertidas += 1
                dias += 15.0
            dias += 0.0 if k == 0 else 1.0 + 0.25 * k
        resultado[f"{k} personas consultadas"] = {"revertidas_pct": round(100 * revertidas / n, 1), "dias_por_decision": round(dias / n, 2)}
    return resultado


# ---------------------------------------------------------------- SE-530
def e446_bus_factor() -> dict:
    """Factor de camión: personas que hay que quitar para dejar sin conocedor a más de la mitad de 300 archivos."""
    n_arch, n_pers, sims = 300, 8, 200
    resultado = {}
    pesos_zipf = [1 / (i + 1) for i in range(n_pers)]
    for nombre in ("un autor, reparto concentrado", "un autor, reparto uniforme", "dos conocedores por archivo", "dos conocedores y rotación"):
        rng = random.Random(4460)
        factores, huerfanos_top1 = [], []
        for _ in range(sims):
            conocen: list[set[int]] = []
            for a in range(n_arch):
                if nombre == "un autor, reparto concentrado":
                    conocen.append({rng.choices(range(n_pers), pesos_zipf)[0]})
                elif nombre == "un autor, reparto uniforme":
                    conocen.append({rng.randrange(n_pers)})
                else:
                    primero = rng.choices(range(n_pers), pesos_zipf)[0] if nombre.startswith("dos conocedores por") else rng.randrange(n_pers)
                    segundo = rng.choice([p for p in range(n_pers) if p != primero])
                    conocen.append({primero, segundo})
            factor = n_pers
            for k in range(1, n_pers + 1):
                if any(sum(1 for c in conocen if not (c - set(salen))) > n_arch / 2 for salen in combinations(range(n_pers), k)):
                    factor = k
                    break
            factores.append(factor)
            top = max(range(n_pers), key=lambda p: sum(p in c for c in conocen))
            huerfanos_top1.append(100 * sum(1 for c in conocen if c == {top}) / n_arch)
        resultado[nombre] = {"factor_mediano": st.median(factores), "huerfanos_al_irse_la_persona_mas_cargada_pct": round(st.mean(huerfanos_top1), 1)}
    return resultado


def e446_conway() -> dict:
    """Cambios que cruzan equipos: equipos por capa frente a equipos por dominio, 5 000 cambios."""
    rng = random.Random(4461)
    n = 5000
    capas = ("interfaz", "lógica", "datos")
    por_capa, por_dom = [], []
    for _ in range(n):
        dom = rng.randrange(4)
        k = rng.choices((1, 2, 3), (0.2, 0.3, 0.5))[0]
        tocadas = rng.sample(capas, k)
        doms = {dom}
        if rng.random() < 0.2:
            doms.add((dom + 1 + rng.randrange(3)) % 4)
        por_capa.append(len(tocadas))
        por_dom.append(len(doms))
    res = {}
    for nombre, v in (("equipos por capa", por_capa), ("equipos por dominio", por_dom)):
        res[nombre] = {"equipos_por_cambio": round(st.mean(v), 2), "cambios_con_relevo_pct": round(100 * sum(x > 1 for x in v) / n, 1),
                       "plazo_dias": round(2 + 3 * (st.mean(v) - 1) + 0.0, 1)}
    return res


def e446_guardia() -> dict:
    """Guardia fuera de horario: 1,5 avisos por semana, rotación semanal."""
    resultado = {}
    for personas in (3, 4, 6, 8):
        rng = random.Random(4462)
        semanas_por_anio, avisos_por_anio, turnos_2mas = [], [], []
        for _ in range(3000):
            avisos = [poisson(rng, 1.5) for _ in range(52)]
            semanas_por_anio.append(sum(1 for s in range(52) if s % personas == 0))
            avisos_por_anio.append(sum(avisos[s] for s in range(52) if s % personas == 0))
            turnos_2mas.append(sum(1 for s in range(52) if s % personas == 0 and avisos[s] >= 3))
        resultado[f"{personas} personas"] = {"semanas_de_guardia_al_anio": round(st.mean(semanas_por_anio), 1),
                                             "avisos_fuera_de_horario_por_persona_y_anio": round(st.mean(avisos_por_anio), 1),
                                             "semanas_con_3_o_mas_avisos_por_persona_y_anio": round(st.mean(turnos_2mas), 2)}
    return resultado


# ---------------------------------------------------------------- SE-531
def e447_anclaje() -> dict:
    """Estimación en grupo: cada persona acierta con ruido; hablar en orden arrastra al grupo."""
    resultado = {}
    verdad, n_pers, ensayos = 100.0, 7, 5000
    for nombre in ("escriben solas y luego se muestra", "se habla en orden, sin sesgo del primero", "se habla en orden y la persona sénior (+30 %) abre"):
        rng = random.Random(4470)
        errores = []
        for _ in range(ensayos):
            propias = [verdad * math.exp(rng.gauss(0, 0.3)) for _ in range(n_pers)]
            if nombre.startswith("escriben"):
                dichas = propias
            else:
                dichas = []
                for i, p in enumerate(propias):
                    if i == 0 and "sénior" in nombre:
                        p = p * 1.3
                    media = st.mean(dichas) if dichas else p
                    dichas.append(p if not dichas else 0.5 * p + 0.5 * media)
            errores.append(abs(st.mean(dichas) - verdad) / verdad * 100)
        resultado[nombre] = {"error_mediano_pct": round(st.median(errores), 1), "error_mayor_a_15_pct": round(100 * sum(e > 15 for e in errores) / ensayos, 1)}
    return resultado


def e447_conflicto() -> dict:
    """Dilema del prisionero iterado con 5 % de malentendidos (acción distinta de la deseada)."""
    T, R, P, S = 5, 3, 1, 0

    def jugada(estrategia: str, hist_propio: list[str], hist_otro: list[str], rng: random.Random) -> str:
        if estrategia == "siempre coopera":
            return "C"
        if estrategia == "siempre ataca":
            return "D"
        if not hist_otro:
            return "C"
        if hist_otro[-1] == "C":
            return "C"
        if estrategia == "ojo por ojo":
            return "D"
        return "C" if rng.random() < 0.3 else "D"  # ojo por ojo generoso

    def partida(a: str, b: str, rng: random.Random) -> tuple[float, float]:
        ha, hb, pa, pb = [], [], 0, 0
        for _ in range(200):
            xa, xb = jugada(a, ha, hb, rng), jugada(b, hb, ha, rng)
            if rng.random() < 0.05:
                xa = "D" if xa == "C" else "C"
            if rng.random() < 0.05:
                xb = "D" if xb == "C" else "C"
            ha.append(xa)
            hb.append(xb)
            tabla = {("C", "C"): (R, R), ("C", "D"): (S, T), ("D", "C"): (T, S), ("D", "D"): (P, P)}
            ga, gb = tabla[(xa, xb)]
            pa += ga
            pb += gb
        return pa / 200, pb / 200

    nombres = ["ojo por ojo", "ojo por ojo generoso", "siempre coopera", "siempre ataca"]
    rng = random.Random(4471)
    resultado = {"par_contra_si_mismo": {}, "promedio_contra_las_cuatro": {}}
    for a in nombres:
        propios = [st.mean(partida(a, a, rng)[0] for _ in range(300))]
        resultado["par_contra_si_mismo"][a] = round(propios[0], 2)
        medias = []
        for b in nombres:
            medias.append(st.mean(partida(a, b, rng)[0] for _ in range(300)))
        resultado["promedio_contra_las_cuatro"][a] = round(st.mean(medias), 2)
    return resultado


def e447_telefono() -> dict:
    """Un mensaje de decisión con cinco campos pasa por varias personas; cada una pierde campos."""
    campos = ("decisión", "motivo", "dueño", "fecha", "alcance")
    formatos = {"oral": (0.10, 0.35, 0.25, 0.20, 0.25), "correo libre": (0.05, 0.20, 0.15, 0.10, 0.15),
                "plantilla con acuse": (0.01, 0.04, 0.02, 0.02, 0.04)}
    resultado = {}
    for nombre, perdidas in formatos.items():
        rng = random.Random(4472)
        fila = {}
        for saltos in (1, 2, 3, 4):
            completos, motivo_ok = 0, 0
            n = 6000
            for _ in range(n):
                vivo = [True] * 5
                for _ in range(saltos):
                    for j in range(5):
                        if vivo[j] and rng.random() < perdidas[j]:
                            vivo[j] = False
                completos += all(vivo)
                motivo_ok += vivo[1]
            fila[f"{saltos} saltos"] = {"completos_pct": round(100 * completos / n, 1), "conserva_el_motivo_pct": round(100 * motivo_ok / n, 1)}
        resultado[nombre] = fila
    return resultado


# ---------------------------------------------------------------- SE-532
def e448_zona() -> dict:
    """Crecimiento según la dificultad de las tareas asignadas durante 52 semanas (modelo de supuestos del autor)."""
    resultado = {}
    for nombre, delta in (("tareas fáciles (nivel - 2)", -2.0), ("tareas calibradas (nivel + 1)", 1.0), ("tareas muy difíciles (nivel + 4)", 4.0), ("dificultad al azar", None)):
        rng = random.Random(4480)
        finales, fracasos = [], []
        for _ in range(1000):
            nivel, malos = 3.0, 0
            for _ in range(52):
                d = nivel + (delta if delta is not None else rng.uniform(-3, 5))
                brecha = d - nivel
                aprende = 0.12 * math.exp(-((brecha - 1.0) ** 2) / 2.0)
                fallo = 1 / (1 + math.exp(-(brecha - 3.0)))
                malos += rng.random() < fallo
                nivel += aprende * (1 - 0.5 * fallo)
            finales.append(nivel)
            fracasos.append(malos)
        resultado[nombre] = {"nivel_final_mediano": round(st.median(finales), 2), "semanas_con_fracaso": round(st.mean(fracasos), 1)}
    return resultado


def e448_retraso() -> dict:
    """Errores repetidos de un mismo hábito hasta que llega la retroalimentación (5 cambios por semana, 12 semanas)."""
    resultado = {}
    for nombre, dias in (("en el mismo cambio", 0), ("a los 2 días", 2), ("en la revisión semanal", 7), ("en la evaluación trimestral", 60)):
        rng = random.Random(4481)
        errores, aprendio_tarde = [], 0
        for _ in range(4000):
            err, corregido = 0, False
            for dia in range(84):
                if dia >= dias and not corregido and rng.random() < 0.7:
                    corregido = True
                cambios = 5 / 7
                p = 0.05 if corregido else 0.3
                err += sum(1 for _ in range(int(round(cambios * 7)) if dia % 7 == 0 else 0) if rng.random() < p)
            errores.append(err)
        resultado[nombre] = {"errores_repetidos_en_12_semanas": round(st.mean(errores), 1)}
    return resultado


def e448_calibracion() -> dict:
    """Acuerdo entre evaluadoras sobre 200 personas: una sola evaluadora, panel sin rúbrica, rúbrica calibrada."""
    esquemas = {"una evaluadora, sin rúbrica": (0.5, 0.8, 1), "tres evaluadoras, sin rúbrica": (0.5, 0.8, 3), "tres evaluadoras con rúbrica calibrada": (0.2, 0.4, 3)}
    resultado = {}
    for nombre, (sd_indulg, sd_ruido, k) in esquemas.items():
        rng = random.Random(4482)
        corrs, aciertos = [], []
        for _ in range(300):
            verdad = [rng.gauss(0, 1) for _ in range(200)]
            jueces = [rng.gauss(0, sd_indulg) for _ in range(6)]
            puntaje = []
            for v in verdad:
                elegidas = rng.sample(range(6), k)
                puntaje.append(st.mean(v + jueces[j] + rng.gauss(0, sd_ruido) for j in elegidas))
            corrs.append(st.correlation(verdad, puntaje))
            mejores = set(sorted(range(200), key=lambda i: -verdad[i])[:40])
            promovidas = set(sorted(range(200), key=lambda i: -puntaje[i])[:40])
            aciertos.append(100 * len(mejores & promovidas) / 40)
        resultado[nombre] = {"correlacion_con_el_desempeno": round(st.mean(corrs), 2), "del_20_pct_mejor_que_se_promueve_pct": round(st.mean(aciertos), 1)}
    return resultado


# ---------------------------------------------------------------- SE-533
def e449_suma_de_medianas() -> dict:
    """Doce tareas con mediana de 5 días: la suma de medianas no es la mediana de la suma."""
    n_tareas, sigma, sims = 12, 0.6, 20000
    resultado = {}
    suma_med = 5.0 * n_tareas
    for nombre, comun in (("tareas independientes", 0.0), ("con un factor común de dificultad", 0.4)):
        rng = random.Random(4490)
        totales = []
        for _ in range(sims):
            f = rng.gauss(0, 1)
            total = sum(5.0 * math.exp(sigma * rng.gauss(0, 1) * math.sqrt(1 - comun ** 2) + sigma * comun * f) for _ in range(n_tareas))
            totales.append(total)
        resultado[nombre] = {"suma_de_medianas_dias": suma_med, "p_de_cumplir_la_suma_de_medianas_pct": round(100 * sum(t <= suma_med for t in totales) / sims, 1),
                             "p50": round(pct(totales, 50), 1), "p85": round(pct(totales, 85), 1), "p95": round(pct(totales, 95), 1)}
    return resultado


def e449_simulacion_por_flujo() -> dict:
    """Pronóstico con el historial de entrega por semana: 60 elementos pendientes."""
    def historial(rng: random.Random, semanas: int) -> list[int]:
        return [0 if rng.random() < 0.08 else poisson(rng, 5.0) for _ in range(semanas)]

    def semanas_para(h: list[int], rng: random.Random, pendientes: int = 60) -> int:
        hecho, s = 0, 0
        while hecho < pendientes:
            hecho += rng.choice(h)
            s += 1
            if s > 400:
                break
        return s

    resultado = {}
    rng0 = random.Random(4491)
    hist20 = historial(rng0, 20)
    sims = [semanas_para(hist20, rng0) for _ in range(5000)]
    resultado["con_un_historial_de_20_semanas"] = {"media_del_historial": round(st.mean(hist20), 2), "semanas_con_media": math.ceil(60 / st.mean(hist20)),
                                                   "p50": pct(sims, 50), "p85": pct(sims, 85), "p95": pct(sims, 95),
                                                   "p_de_terminar_en_las_semanas_de_la_media": round(100 * sum(s <= math.ceil(60 / st.mean(hist20)) for s in sims) / len(sims), 1)}
    estab = {}
    for semanas in (6, 12, 24, 48):
        p85s = []
        for rep in range(200):
            rng = random.Random(910000 + rep)
            h = historial(rng, semanas)
            p85s.append(pct([semanas_para(h, rng) for _ in range(400)], 85))
        estab[f"{semanas} semanas de historial"] = {"p85_mediano": st.median(p85s), "rango_p10_p90": [pct(p85s, 10), pct(p85s, 90)]}
    resultado["estabilidad_del_p85_en_200_historiales"] = estab
    return resultado


def e449_utilizacion() -> dict:
    """Tiempo de ciclo frente a la carga comprometida (cola de un servidor, recursión de Lindley)."""
    resultado = {}
    for rho in (0.5, 0.7, 0.85, 0.95):
        rng = random.Random(4492)
        w, ciclos = 0.0, []
        for _ in range(60000):
            servicio = rng.expovariate(1.0)
            llegada = rng.expovariate(rho)
            ciclos.append(w + servicio)
            w = max(0.0, w + servicio - llegada)
        resultado[f"{int(rho * 100)} % de carga"] = {"ciclo_medio_en_unidades_de_trabajo": round(st.mean(ciclos), 1), "teoria_1_sobre_1_menos_rho": round(1 / (1 - rho), 1), "ciclo_p90": round(pct(ciclos, 90), 1)}
    return resultado


# ---------------------------------------------------------------- SE-534
def e450_matriz() -> dict:
    """Cartera de 30 riesgos: matriz 5x5 frente al valor esperado para elegir los 5 primeros."""
    def clase(v: float, cortes: list[float]) -> int:
        return 1 + sum(v > c for c in cortes)

    rng = random.Random(4500)
    cobertura = {"matriz 5x5": [], "valor esperado": [], "al azar": []}
    cola = {"matriz 5x5": [], "valor esperado": []}
    for _ in range(400):
        riesgos = []
        for _ in range(30):
            p = min(0.9, math.exp(rng.gauss(math.log(0.08), 0.9)))
            imp = math.exp(rng.gauss(math.log(50), 1.5))
            riesgos.append((p, imp))
        ev = [p * imp * math.exp(1.5 ** 2 / 2) / 1 for p, imp in riesgos]  # esperanza real de un lognormal
        total = sum(ev)
        matriz = [clase(p, [0.02, 0.05, 0.1, 0.25]) * clase(imp, [10, 30, 100, 300]) + rng.random() * 0.5 for p, imp in riesgos]
        orden_m = sorted(range(30), key=lambda i: -matriz[i])[:5]
        orden_e = sorted(range(30), key=lambda i: -ev[i])[:5]
        azar = rng.sample(range(30), 5)
        cobertura["matriz 5x5"].append(100 * sum(ev[i] for i in orden_m) / total)
        cobertura["valor esperado"].append(100 * sum(ev[i] for i in orden_e) / total)
        cobertura["al azar"].append(100 * sum(ev[i] for i in azar) / total)
        # mayor riesgo real que la matriz deja fuera
        mayor = max(range(30), key=lambda i: ev[i])
        cola["matriz 5x5"].append(mayor not in orden_m)
    resultado = {k: {"esperanza_cubierta_pct": round(st.mean(v), 1)} for k, v in cobertura.items()}
    resultado["matriz 5x5"]["deja_fuera_el_mayor_riesgo_pct"] = round(100 * sum(cola["matriz 5x5"]) / 400, 1)
    return resultado


def e450_valor_de_informacion() -> dict:
    """Valor esperado de la información perfecta (VEIP) y de un experimento ruidoso (VEII) frente a su costo."""
    resultado = {}
    for mu in (-20.0, 0.0, 20.0):
        rng = random.Random(4501)
        sigma, ruido, n = 100.0, 40.0, 200000
        sin_info = max(mu, 0.0)
        veip, veii = 0.0, 0.0
        for _ in range(n):
            v = rng.gauss(mu, sigma)
            veip += max(v, 0.0)
            senal = v + rng.gauss(0, ruido)
            post_media = mu + (sigma ** 2 / (sigma ** 2 + ruido ** 2)) * (senal - mu)
            veii += v if post_media > 0 else 0.0
        resultado[f"valor esperado a priori {mu:+.0f}"] = {"sin_informacion": sin_info, "veip": round(veip / n - sin_info, 1), "veii_experimento_ruidoso": round(veii / n - sin_info, 1),
                                                          "analitico_veip": round(sigma * math.exp(-0.5 * (mu / sigma) ** 2) / math.sqrt(2 * math.pi) + mu * 0.5 * (1 + math.erf(mu / (sigma * math.sqrt(2)))) - sin_info, 1)}
    return resultado


def e450_reversibilidad() -> dict:
    """200 decisiones por trimestre: qué cuesta escalar todo frente a escalar solo lo irreversible."""
    resultado = {}
    for nombre, politica in (("todo se escala", "todo"), ("solo se escala lo irreversible", "irrev"), ("nada se escala", "nada")):
        rng = random.Random(4502)
        costos = []
        for _ in range(3000):
            total = 0.0
            for _ in range(200):
                irrev = rng.random() < 0.3
                escalada = politica == "todo" or (politica == "irrev" and irrev)
                p_error = 0.15 if escalada else 0.25
                demora = 10 if escalada else 1
                total += 0.1 * demora  # costo de esperar, por día
                if rng.random() < p_error:
                    total += 20.0 if irrev else 1.5
            costos.append(total)
        resultado[nombre] = {"costo_mediano": round(st.median(costos), 1), "costo_p90": round(pct(costos, 90), 1)}
    return resultado


EXPERIMENTS = {
    "e445_umbral": e445_umbral, "e445_cola": e445_cola, "e445_consulta": e445_consulta,
    "e446_bus_factor": e446_bus_factor, "e446_conway": e446_conway, "e446_guardia": e446_guardia,
    "e447_anclaje": e447_anclaje, "e447_conflicto": e447_conflicto, "e447_telefono": e447_telefono,
    "e448_zona": e448_zona, "e448_retraso": e448_retraso, "e448_calibracion": e448_calibracion,
    "e449_suma_de_medianas": e449_suma_de_medianas, "e449_simulacion_por_flujo": e449_simulacion_por_flujo, "e449_utilizacion": e449_utilizacion,
    "e450_matriz": e450_matriz, "e450_valor_de_informacion": e450_valor_de_informacion, "e450_reversibilidad": e450_reversibilidad,
}

if __name__ == "__main__":
    elegidos = sys.argv[1:] or list(EXPERIMENTS)
    for nombre in elegidos:
        print(nombre, json.dumps(EXPERIMENTS[nombre](), ensure_ascii=False, sort_keys=True))
