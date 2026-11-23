"""Parte 34 (SaaS): inventario sin sobreventa, reparto de un marketplace y SLA por nivel.

La parte de inventario ejecuta hilos reales contra sqlite3 en un archivo temporal; el reparto del marketplace y
el calculo de SLA son aritmetica determinista con parametros del autor. Uso: python scripts/experiments_part34_commerce.py
"""
from __future__ import annotations

import os
import random
import sqlite3
import tempfile
import threading
import time

SEMILLA = 34


def inventario(modo: str, compradores: int = 40, existencias: int = 10) -> dict:
    """modo: leer_luego_escribir (ingenuo) | actualizacion_condicional (atomico).

    Cada comprador pide una unidad del mismo producto a la vez. El modo ingenuo lee el saldo, 'valida' y escribe
    el saldo menos uno; la pausa de 2 ms entre leer y escribir representa la validacion de pago y el desfase real.
    """
    with tempfile.TemporaryDirectory() as carpeta:
        ruta = os.path.join(carpeta, "inv.db")
        con = sqlite3.connect(ruta)
        con.execute("CREATE TABLE producto (sku TEXT PRIMARY KEY, disponible INTEGER NOT NULL CHECK (disponible >= 0))")
        con.execute("CREATE TABLE pedido (id INTEGER PRIMARY KEY AUTOINCREMENT, comprador INTEGER, sku TEXT)")
        con.execute("INSERT INTO producto VALUES ('camiseta', ?)", (existencias,))
        con.commit()
        con.close()
        barrera = threading.Barrier(compradores)
        errores = []

        def comprar(n: int) -> None:
            c = sqlite3.connect(ruta, timeout=30, isolation_level=None)
            barrera.wait()
            try:
                if modo == "leer_luego_escribir":
                    (disp,) = c.execute("SELECT disponible FROM producto WHERE sku='camiseta'").fetchone()
                    if disp > 0:
                        time.sleep(0.002)
                        try:
                            c.execute("UPDATE producto SET disponible = ? WHERE sku='camiseta'", (max(disp - 1, 0),))
                            c.execute("INSERT INTO pedido(comprador, sku) VALUES (?, 'camiseta')", (n,))
                        except sqlite3.Error as exc:
                            errores.append(str(exc))
                else:
                    cur = c.execute("UPDATE producto SET disponible = disponible - 1 WHERE sku='camiseta' AND disponible > 0")
                    if cur.rowcount == 1:
                        c.execute("INSERT INTO pedido(comprador, sku) VALUES (?, 'camiseta')", (n,))
            except sqlite3.Error as exc:
                errores.append(str(exc))
            finally:
                c.close()

        hilos = [threading.Thread(target=comprar, args=(i,)) for i in range(compradores)]
        for h in hilos:
            h.start()
        for h in hilos:
            h.join()
        con = sqlite3.connect(ruta)
        pedidos = con.execute("SELECT COUNT(*) FROM pedido").fetchone()[0]
        disponible = con.execute("SELECT disponible FROM producto").fetchone()[0]
        con.close()
    return {"modo": modo, "compradores": compradores, "existencias": existencias, "pedidos_aceptados": pedidos,
            "vendidas_de_mas": max(0, pedidos - existencias), "disponible_final": disponible, "errores": len(errores)}


def reparto(precio: int, comision_plataforma: float, comision_procesador: float, fijo_procesador: int) -> dict:
    """Reparto de una venta de marketplace en centavos: el vendedor recibe lo que sobra tras comisiones."""
    plataforma = round(precio * comision_plataforma)
    procesador = round(precio * comision_procesador) + fijo_procesador
    vendedor = precio - plataforma - procesador
    return {"precio": precio, "plataforma": plataforma, "procesador": procesador, "vendedor": vendedor,
            "plataforma_neto": plataforma - 0, "margen_plataforma_pct": round(100 * plataforma / precio, 1)}


def liquidez(semilla: int = SEMILLA) -> list[tuple[int, int, float]]:
    """Modelo de dos lados: cada comprador busca entre N vendedores; la probabilidad de encontrar oferta crece con N.

    Devuelve (vendedores, compradores_con_oferta_de_100, tasa de emparejamiento).
    """
    rng = random.Random(semilla)
    filas = []
    for vendedores in (5, 20, 80, 320):
        ok = 0
        for _ in range(1000):
            ofertas = sum(1 for _ in range(vendedores) if rng.random() < 0.04)
            ok += 1 if ofertas >= 1 else 0
        filas.append((vendedores, ok, ok / 1000))
    return filas


def sla(disponibilidad: float, dias: int = 30) -> dict:
    minutos = dias * 24 * 60
    return {"objetivo": disponibilidad, "minutos_de_caida_permitidos": round(minutos * (1 - disponibilidad), 1)}


def credito_sla(medida: float) -> int:
    """Creditos del autor por incumplimiento mensual (porcentaje de la factura): tramos de ejemplo, no un contrato real."""
    if medida >= 0.999:
        return 0
    if medida >= 0.99:
        return 10
    if medida >= 0.95:
        return 25
    return 100


def reservas(ttl_min: int, semilla: int = SEMILLA) -> dict:
    """Modelo: 50 unidades, 300 compradores que llegan en 120 min; 65 % abandona tras reservar.

    Una reserva retiene la unidad `ttl_min` minutos (o hasta el pago, si completa en 4 +- 2 min).
    Devuelve ventas realizadas y compradores rechazados con stock que existia pero estaba retenido.
    """
    rng = random.Random(semilla)
    llegadas = sorted(rng.uniform(0, 120) for _ in range(300))
    libres, ocupadas, ventas, rechazados_retenido = 50, [], 0, 0   # ocupadas: (minuto_de_liberacion, vendida)
    for t in llegadas:
        nuevas = []
        for fin, vendida in ocupadas:
            if fin <= t:
                if not vendida:
                    libres += 1
            else:
                nuevas.append((fin, vendida))
        ocupadas = nuevas
        if libres > 0:
            libres -= 1
            if rng.random() < 0.35:                       # completa el pago
                ocupadas.append((t + max(1.0, rng.gauss(4, 2)), True)); ventas += 1
            else:                                          # abandona: la reserva expira al terminar el TTL
                ocupadas.append((t + ttl_min, False))
        else:
            if any(not v for _, v in ocupadas):
                rechazados_retenido += 1
    return {"ttl_min": ttl_min, "ventas": ventas, "rechazados_con_stock_retenido": rechazados_retenido}


def sla_por_inquilino(semilla: int = SEMILLA) -> dict:
    """100 inquilinos y un mes de solicitudes simuladas: el SLI agregado puede cumplir mientras un inquilino no cumple.

    El inquilino 7 recibe el 0,3 % del trafico y falla el 12 % de sus solicitudes (p. ej. un fragmento degradado);
    los demas fallan el 0,05 %. Devuelve disponibilidad agregada, la del peor inquilino y cuantos incumplen 99,9 %.
    """
    rng = random.Random(semilla)
    pesos = [0.3 if i == 7 else 1.00707 for i in range(100)]
    solicitudes = {i: 0 for i in range(100)}
    fallos = {i: 0 for i in range(100)}
    for _ in range(100_000):                          # 100 000 lotes de 20 solicitudes
        i = rng.choices(range(100), weights=pesos)[0]
        solicitudes[i] += 20
        p_fallo = 0.12 if i == 7 else 0.0005
        fallos[i] += sum(1 for _ in range(20) if rng.random() < p_fallo)
    disp = {i: 1 - fallos[i] / solicitudes[i] for i in solicitudes if solicitudes[i]}
    agregada = 1 - sum(fallos.values()) / sum(solicitudes.values())
    peor = min(disp, key=disp.get)
    return {"agregada": round(agregada, 5), "peor_inquilino": peor, "peor_disponibilidad": round(disp[peor], 4),
            "incumplen_999": sum(1 for v in disp.values() if v < 0.999), "solicitudes": sum(solicitudes.values()),
            "trafico_del_peor_pct": round(100 * solicitudes[peor] / sum(solicitudes.values()), 2)}


def disponibilidad_compuesta(componentes: list[float]) -> dict:
    """Disponibilidad de una cadena en serie (todas deben funcionar): el producto de las disponibilidades."""
    d = 1.0
    for c in componentes:
        d *= c
    return {"disponibilidad": round(d, 5), "minutos_de_caida_por_mes": round(30 * 24 * 60 * (1 - d), 1)}


if __name__ == "__main__":
    print("sla por inquilino:", sla_por_inquilino())
    print("compuesta:", disponibilidad_compuesta([0.999, 0.999, 0.9995]), disponibilidad_compuesta([0.9995, 0.9995, 0.9995, 0.9995]))
    print("reservas:", [reservas(t) for t in (1, 5, 15, 30, 60)])
    for m in ("leer_luego_escribir", "actualizacion_condicional"):
        print(inventario(m))
    for modo in ("leer_luego_escribir",):
        print("repetido:", [inventario(modo)["vendidas_de_mas"] for _ in range(5)])
    print("reparto 10000:", reparto(10000, 0.10, 0.029, 30))
    print("reparto 500:", reparto(500, 0.10, 0.029, 30))
    print("liquidez:", liquidez())
    for a in (0.99, 0.995, 0.999, 0.9995, 0.9999):
        print(sla(a))
    for medida in (0.9995, 0.995, 0.97, 0.9):
        print("credito", medida, credito_sla(medida), "%")
