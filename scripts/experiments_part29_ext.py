"""Experimentos de ampliación de SE-353 (confianza cero) y SE-356 (software verde).

Uso: python scripts/experiments_part29_ext.py   (imprime una línea JSON por experimento)

1. Movimiento lateral. 40 servicios en 5 equipos de 8; cada servicio llama a 3 otros (grafo fijo por semilla). Un
   atacante compromete un servicio al azar y avanza por las conexiones que la red le permite; cada servicio al
   alcance cae con probabilidad p. Cuatro reglas de red: plana (confianza por ubicación), segmentos por equipo,
   lista de permitidos por servicio y lista de permitidos con identidad y autorización por operación (se supone que
   cada llamada autorizada expone 2 de 8 operaciones, así que p se multiplica por 0,25). Supuestos del autor.
2. Intensidad de software. Se mide el tiempo transcurrido (mínimo de 5 repeticiones la ingenua y de 40 la eficiente, un solo hilo, como sustituto del tiempo de CPU) de dos implementaciones de la misma tarea y se calcula el
   SCI = ((E x I) + M) por cada 1 000 solicitudes con supuestos declarados: potencia 15 W por núcleo, intensidad de la
   red eléctrica 50, 300 y 700 gCO2e/kWh (ilustrativas) y emisiones incorporadas de 1 300 kg de un servidor de 16
   núcleos con vida útil de 4 años. Además se calcula cuánto baja la emisión al mover un trabajo diferible de 3 h
   desde las 18:00 a la ventana más limpia de una curva diaria sintética de intensidad.
"""
import json
import random
import statistics
import sys
import time

sys.stdout.reconfigure(encoding="utf-8")


def grafo(rng, n=40, equipos=5, salida=3):
    llamadas = {i: set() for i in range(n)}
    equipo = [i * equipos // n for i in range(n)]
    por_equipo = {e: [i for i in range(n) if equipo[i] == e] for e in range(equipos)}
    for i in range(n):
        while len(llamadas[i]) < salida:
            # dos llamadas dentro del equipo y una al equipo siguiente
            destino = por_equipo[equipo[i]] if len(llamadas[i]) < salida - 1 else por_equipo[(equipo[i] + 1) % equipos]
            j = rng.choice(destino)
            if j != i:
                llamadas[i].add(j)
    return llamadas, equipo


def alcanzables(origen, regla, llamadas, equipo, n=40):
    if regla == "plana":
        return [j for j in range(n) if j != origen]
    if regla == "equipos":
        pares = {(equipo[i], equipo[j]) for i in llamadas for j in llamadas[i]}
        return [j for j in range(n) if j != origen and (equipo[j] == equipo[origen] or (equipo[origen], equipo[j]) in pares)]
    return list(llamadas[origen])


def movimiento_lateral():
    rng = random.Random(353)
    llamadas, equipo = grafo(rng)
    critico = 17
    salida = {}
    for regla, p in (("plana", 0.3), ("equipos", 0.3), ("por_servicio", 0.3), ("identidad_y_operacion", 0.3 * 0.25)):
        base = "por_servicio" if regla == "identidad_y_operacion" else regla
        comprometidos, critico_cae = [], 0
        ensayos = 4000
        for _ in range(ensayos):
            origen = rng.randrange(40)
            if origen == critico:
                continue
            cae = {origen}
            frontera = [origen]
            while frontera:
                siguiente = []
                for a in frontera:
                    for b in alcanzables(a, base, llamadas, equipo):
                        if b not in cae and rng.random() < p:
                            cae.add(b)
                            siguiente.append(b)
                frontera = siguiente
            comprometidos.append(len(cae))
            critico_cae += critico in cae
        salida[regla] = {"servicios_comprometidos_media": round(statistics.fmean(comprometidos), 2),
                         "servicio_critico_cae_pct": round(100 * critico_cae / len(comprometidos), 1)}
    return salida


# ---------------------------------------------------------------- software verde
def tarea_ingenua(datos):
    vistos, acumulado = [], {}
    for clave, valor in datos:
        if clave not in vistos:  # búsqueda lineal
            vistos.append(clave)
        acumulado[clave] = acumulado.get(clave, 0) + valor
    return len(vistos), sum(acumulado.values())


def tarea_eficiente(datos):
    acumulado = {}
    for clave, valor in datos:
        acumulado[clave] = acumulado.get(clave, 0) + valor
    return len(acumulado), sum(acumulado.values())


def medir(funcion, datos, repeticiones=5):
    tiempos = []
    for _ in range(repeticiones):
        t0 = time.perf_counter()
        funcion(datos)
        tiempos.append(time.perf_counter() - t0)
    return min(tiempos)


def sci(cpu_s, intensidad, solicitudes=1, potencia_w=15.0, te_kg=1300.0, vida_anos=4.0, nucleos=16):
    e_kwh = cpu_s * potencia_w / 3.6e6
    m_g = te_kg * 1000 * (cpu_s / (vida_anos * 365 * 24 * 3600)) * (1 / nucleos)
    return (e_kwh * intensidad + m_g) * 1000 / solicitudes  # mg CO2e por unidad funcional R (aquí, una tarea)


def intensidad_de_software():
    rng = random.Random(356)
    datos = [(rng.randrange(3000), rng.random()) for _ in range(20000)]
    assert tarea_ingenua(datos)[0] == tarea_eficiente(datos)[0]
    t_ing = medir(tarea_ingenua, datos, 5)
    t_efi = medir(tarea_eficiente, datos, 40)
    salida = {"cpu_s_ingenua": round(t_ing, 4), "cpu_s_eficiente": round(t_efi, 4), "razon": round(t_ing / t_efi, 1),
              "sci_mg_por_tarea": {}}
    for nombre, i in (("limpia_50", 50), ("mixta_300", 300), ("intensiva_700", 700)):
        salida["sci_mg_por_tarea"][nombre] = {"ingenua": round(sci(t_ing, i), 3), "eficiente": round(sci(t_efi, i), 3)}
    # curva diaria sintética (gCO2e/kWh por hora): valle solar al mediodía, pico al anochecer
    curva = [400, 400, 390, 380, 380, 390, 420, 380, 300, 220, 160, 120, 100, 100, 120, 180, 280, 420, 560, 600, 560, 500, 450, 420]
    ventanas = {h: sum(curva[(h + k) % 24] for k in range(3)) / 3 for h in range(24)}
    mejor = min(ventanas, key=ventanas.get)
    salida["desplazamiento"] = {"hora_fija": 18, "intensidad_18h": round(ventanas[18], 1),
                                "mejor_hora": mejor, "intensidad_mejor": round(ventanas[mejor], 1),
                                "reduccion_pct": round(100 * (1 - ventanas[mejor] / ventanas[18]), 1)}
    return salida


if __name__ == "__main__":
    print(json.dumps({"movimiento_lateral": movimiento_lateral()}, ensure_ascii=False))
    print(json.dumps({"software_verde": intensidad_de_software()}, ensure_ascii=False))
