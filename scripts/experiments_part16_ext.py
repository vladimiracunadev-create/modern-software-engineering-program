"""Experimento de ampliación de SE-200: cuello de botella de los mantenedores en InnerSource.

Modelo sintético (cola de un solo servidor con retorno), semilla fija, solo biblioteca estándar.
Uso: python scripts/experiments_part16_ext.py   (imprime una línea JSON)

Supuestos del autor, no medidos en una organización real: llegan 6 solicitudes de cambio por
semana (proceso de Poisson), cada ronda de revisión cuesta 1,5 h de un mantenedor, el autor
tarda 1 día laborable en responder y el equipo anfitrión dedica ``c`` horas semanales a revisar
aportes ajenos. Sin guía de contribución cada aporte necesita en media 3 rondas; con guía,
plantilla y CI previo, 1,5.
"""
import heapq
import json
import random
import statistics
import sys

sys.stdout.reconfigure(encoding="utf-8")

LLEGADAS_SEMANA = 6.0
HORAS_RONDA = 1.5
RESPUESTA_AUTOR_H = 8.0  # un día laborable de 8 h
SEMANA_H = 40.0


def rondas(rng: random.Random, media: float) -> int:
    # 1 + geométrica: la media exacta es ``media``.
    p = 1.0 / media
    n = 1
    while rng.random() > p:
        n += 1
    return n


def simular(media_rondas: float, capacidad_h: float, semilla: int, n: int = 1000):
    rng = random.Random(semilla)
    velocidad = capacidad_h / SEMANA_H  # fracción del tiempo laboral que el equipo dedica a revisar
    servicio = HORAS_RONDA / velocidad  # horas transcurridas por ronda
    t = 0.0
    listos = []  # (instante en que espera revisión, aporte): el servidor atiende al que lleva más esperando
    llegada = {}
    for i in range(n):
        t += rng.expovariate(LLEGADAS_SEMANA / SEMANA_H)
        llegada[i] = t
        listos.append((t, i))
    heapq.heapify(listos)
    restantes = {i: rondas(rng, media_rondas) for i in range(n)}
    libre = 0.0
    fin = {}
    while listos:
        lista, j = heapq.heappop(listos)
        libre = max(libre, lista) + servicio
        restantes[j] -= 1
        if restantes[j] == 0:
            fin[j] = libre
        else:
            heapq.heappush(listos, (libre + RESPUESTA_AUTOR_H, j))
    esperas = sorted((fin[i] - llegada[i]) / 8.0 for i in fin)  # días laborables de 8 h
    return round(statistics.median(esperas), 1), round(esperas[int(0.9 * len(esperas)) - 1], 1)


def main() -> None:
    capacidades = [14, 20, 28, 32, 36, 40]
    salida = {"capacidad_h_semana": capacidades}
    for etiqueta, media in (("sin_guia_3_rondas", 3.0), ("con_guia_1_5_rondas", 1.5)):
        med, p90 = [], []
        for c in capacidades:
            m, q = simular(media, c, semilla=200)
            med.append(m)
            p90.append(q)
        salida[etiqueta] = {"mediana_dias": med, "p90_dias": p90}
    for etiqueta, media in (("sin_guia_3_rondas", 3.0), ("con_guia_1_5_rondas", 1.5)):
        salida[etiqueta]["carga_horas_semana"] = round(LLEGADAS_SEMANA * media * HORAS_RONDA, 1)
    print(json.dumps(salida, ensure_ascii=False))


if __name__ == "__main__":
    main()
