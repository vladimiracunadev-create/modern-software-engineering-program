"""Parte 34 (SaaS): simulacion del vecino ruidoso con y sin cuotas, y costo por modelo de aislamiento.

Modelo de colas discreto con semilla fija 34. No mide un sistema real: muestra la forma del efecto.
Uso: python scripts/experiments_part34_tenancy.py
"""
from __future__ import annotations

import random
import statistics
from collections import deque

SEMILLA = 34
TICKS = 15000         # un tick = 10 ms de tiempo simulado
CAPACIDAD = 20        # trabajos que el grupo de procesos completa por tick (un trabajo = 1 unidad)
CLIENTES = 8          # el cliente 0 es el vecino ruidoso
TASA_NORMAL = 1.9     # llegadas medias por tick de cada cliente normal (carga total ~ 76 % de la capacidad con 7 normales: 13.3)
RAFAGA = (2000, 3500)  # el cliente 0 envia una rafaga en este intervalo
TASA_RAFAGA = 40.0


def poisson(rng: random.Random, lam: float) -> int:
    limite, k, p = 2.718281828459045 ** (-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= limite:
            return k
        k += 1


def llegadas(rng: random.Random, tick: int, cliente: int) -> int:
    if cliente == 0:
        return poisson(rng, TASA_RAFAGA if RAFAGA[0] <= tick < RAFAGA[1] else 1.9)
    return poisson(rng, TASA_NORMAL)


def simular(politica: str) -> dict:
    """politica: compartida | cuota_tasa | cola_justa"""
    rng = random.Random(SEMILLA)
    colas = [deque() for _ in range(CLIENTES)]
    comun: deque = deque()
    fichas = [10.0] * CLIENTES
    lat = [[] for _ in range(CLIENTES)]
    rechazados = [0] * CLIENTES
    turno = 0
    for t in range(TICKS):
        for c in range(CLIENTES):
            n = llegadas(rng, t, c)
            if politica == "cuota_tasa":
                fichas[c] = min(10.0, fichas[c] + 2.4)   # 2,4 fichas por tick de recarga, rafaga maxima 10
                for _ in range(n):
                    if fichas[c] >= 1:
                        fichas[c] -= 1
                        comun.append((t, c))
                    else:
                        rechazados[c] += 1
            elif politica == "compartida":
                for _ in range(n):
                    comun.append((t, c))
            else:
                for _ in range(n):
                    colas[c].append(t)
        hecho = 0
        if politica in ("compartida", "cuota_tasa"):
            while comun and hecho < CAPACIDAD:
                t0, c = comun.popleft()
                lat[c].append(t - t0 + 1)
                hecho += 1
        else:
            while hecho < CAPACIDAD and any(colas):
                for _ in range(CLIENTES):
                    c = turno % CLIENTES
                    turno += 1
                    if colas[c]:
                        lat[c].append(t - colas[c].popleft() + 1)
                        hecho += 1
                        break
    def pct(v: list[int], p: float) -> float:
        if not v:
            return float("nan")
        v = sorted(v)
        return v[min(len(v) - 1, int(p * len(v)))] * 10.0   # milisegundos
    normales = [x for c in range(1, CLIENTES) for x in lat[c]]
    return {
        "politica": politica,
        "vecino_p50": pct(lat[0], 0.5), "vecino_p99": pct(lat[0], 0.99),
        "otros_p50": pct(normales, 0.5), "otros_p95": pct(normales, 0.95), "otros_p99": pct(normales, 0.99),
        "pendientes_al_final": len(comun) + sum(len(q) for q in colas),
        "rechazados_vecino": rechazados[0], "rechazados_otros": sum(rechazados[1:]),
        "completados_otros": len(normales),
    }


def p99_en_rafaga(politica: str) -> float:
    """p99 de los otros clientes solo durante la rafaga (completados entre RAFAGA[0] y RAFAGA[1])."""
    rng = random.Random(SEMILLA)
    colas = [deque() for _ in range(CLIENTES)]
    comun: deque = deque()
    fichas = [10.0] * CLIENTES
    lat: list[int] = []
    turno = 0
    for t in range(TICKS):
        for c in range(CLIENTES):
            n = llegadas(rng, t, c)
            if politica == "cuota_tasa":
                fichas[c] = min(10.0, fichas[c] + 2.4)
                for _ in range(n):
                    if fichas[c] >= 1:
                        fichas[c] -= 1
                        comun.append((t, c))
            elif politica == "compartida":
                for _ in range(n):
                    comun.append((t, c))
            else:
                for _ in range(n):
                    colas[c].append(t)
        hecho = 0
        if politica in ("compartida", "cuota_tasa"):
            while comun and hecho < CAPACIDAD:
                t0, c = comun.popleft()
                if c != 0 and RAFAGA[0] <= t < RAFAGA[1]:
                    lat.append(t - t0 + 1)
                hecho += 1
        else:
            while hecho < CAPACIDAD and any(colas):
                for _ in range(CLIENTES):
                    c = turno % CLIENTES
                    turno += 1
                    if colas[c]:
                        t0 = colas[c].popleft()
                        if c != 0 and RAFAGA[0] <= t < RAFAGA[1]:
                            lat.append(t - t0 + 1)
                        hecho += 1
                        break
    lat.sort()
    return lat[int(0.99 * len(lat))] * 10.0


def costo_por_modelo() -> list[tuple[str, float, float, float]]:
    """Modelo de costo mensual por cliente con parametros del autor (no son precios de un proveedor)."""
    filas = []
    for n in (10, 100, 1000):
        silo = 90.0                       # base de datos y computo dedicados por cliente
        puente = 18.0 + 400.0 / n * 1.0   # computo compartido + esquema propio + parte de un clúster
        pool = 2.0 + 600.0 / n            # todo compartido: costo fijo repartido
        filas.append((f"{n} clientes", silo, puente, pool))
    return filas


def aprovisionamiento(n: int = 200) -> dict:
    """Medicion real con sqlite3: dar de alta n clientes con fila de inquilino frente a esquema propio (12 tablas)."""
    import sqlite3
    import time

    tablas = [f"CREATE TABLE t{i} (id INTEGER PRIMARY KEY, inquilino TEXT, dato TEXT, creado TEXT)" for i in range(12)]
    t0 = time.perf_counter()
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE inquilino (id TEXT PRIMARY KEY, plan TEXT)")
    for i in range(n):
        db.execute("INSERT INTO inquilino VALUES (?, 'equipo')", (f"c{i}",))
    fila = (time.perf_counter() - t0) / n * 1000
    t0 = time.perf_counter()
    for i in range(n):
        d2 = sqlite3.connect(":memory:")
        for ddl in tablas:
            d2.execute(ddl)
        d2.close()
    esquema = (time.perf_counter() - t0) / n * 1000
    return {"n": n, "ms_por_alta_fila": round(fila, 4), "ms_por_alta_esquema": round(esquema, 4), "veces": round(esquema / fila, 1)}


def alta_reanudable() -> dict:
    """Alta en cinco pasos con registro de pasos hechos: falla en el cuarto, se reanuda y no duplica nada (sqlite3)."""
    import sqlite3

    db = sqlite3.connect(":memory:")
    db.executescript(
        """
        CREATE TABLE inquilino (id TEXT PRIMARY KEY, estado TEXT NOT NULL, motivo TEXT);
        CREATE TABLE paso (inquilino TEXT, nombre TEXT, PRIMARY KEY (inquilino, nombre));
        CREATE TABLE admin (inquilino TEXT PRIMARY KEY, correo TEXT);
        CREATE TABLE semilla (inquilino TEXT, nombre TEXT, PRIMARY KEY (inquilino, nombre));
        CREATE TABLE facturacion (inquilino TEXT PRIMARY KEY, cliente_externo TEXT);
        """
    )
    fallo = {"activo": True}

    def hacer(inq: str, nombre: str) -> None:
        if db.execute("SELECT 1 FROM paso WHERE inquilino=? AND nombre=?", (inq, nombre)).fetchone():
            return                                              # ya hecho: repetir no duplica
        if nombre == "admin":
            db.execute("INSERT OR IGNORE INTO admin VALUES (?, 'admin@ejemplo.test')", (inq,))
        elif nombre == "datos":
            for n in ("proyecto-inicial", "etiquetas"):
                db.execute("INSERT OR IGNORE INTO semilla VALUES (?, ?)", (inq, n))
        elif nombre == "facturacion":
            if fallo["activo"]:
                raise TimeoutError("el procesador no responde")
            db.execute("INSERT OR IGNORE INTO facturacion VALUES (?, 'cus_ejemplo')", (inq,))
        db.execute("INSERT INTO paso VALUES (?, ?)", (inq, nombre))

    def alta(inq: str) -> str:
        db.execute("INSERT OR IGNORE INTO inquilino VALUES (?, 'aprovisionando', NULL)", (inq,))
        try:
            for nombre in ("datos", "admin", "facturacion"):
                hacer(inq, nombre)
        except TimeoutError as exc:
            db.execute("UPDATE inquilino SET estado='fallido', motivo=? WHERE id=?", (str(exc), inq))
            return "fallido"
        db.execute("UPDATE inquilino SET estado='activo', motivo=NULL WHERE id=?", (inq,))
        return "activo"

    primero = alta("acme")
    pasos_tras_fallo = [r[0] for r in db.execute("SELECT nombre FROM paso ORDER BY rowid")]
    fallo["activo"] = False
    segundo = alta("acme")
    tercero = alta("acme")                                      # repetir un alta terminada no cambia nada
    cuenta = lambda t: db.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    return {"primer_intento": primero, "pasos_tras_fallo": pasos_tras_fallo, "segundo_intento": segundo, "tercer_intento": tercero,
            "inquilinos": cuenta("inquilino"), "admins": cuenta("admin"), "filas_semilla": cuenta("semilla"), "clientes_facturacion": cuenta("facturacion"), "pasos_registrados": cuenta("paso")}


if __name__ == "__main__":
    print("alta reanudable:", alta_reanudable())
    print("aprovisionamiento:", aprovisionamiento())
    print(f"semilla={SEMILLA} ticks={TICKS} capacidad={CAPACIDAD}/tick clientes={CLIENTES} rafaga={RAFAGA} tasa_rafaga={TASA_RAFAGA}")
    for pol in ("compartida", "cuota_tasa", "cola_justa"):
        r = simular(pol)
        print(pol, {k: (round(v, 1) if isinstance(v, float) else v) for k, v in r.items() if k != "politica"},
              "p99_otros_en_rafaga_ms=", round(p99_en_rafaga(pol), 1))
    print("costo mensual por cliente (silo, puente, pool):")
    for fila in costo_por_modelo():
        print(fila[0], [round(x, 2) for x in fila[1:]])
