"""Parte 34 (SaaS): libro mayor de doble entrada, cobro idempotente y conciliacion con sqlite3.

Todo se ejecuta de verdad con sqlite3 en memoria y semilla fija 34; el procesador de pagos es un doble simulado
(no se llama a ningun servicio real). Uso: python scripts/experiments_part34_ledger.py
"""
from __future__ import annotations

import random
import sqlite3

SEMILLA = 34


def nueva_bd() -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    db.executescript(
        """
        CREATE TABLE asiento (id INTEGER PRIMARY KEY, referencia TEXT UNIQUE NOT NULL, descripcion TEXT);
        CREATE TABLE apunte (id INTEGER PRIMARY KEY, asiento_id INTEGER NOT NULL REFERENCES asiento(id),
                             cuenta TEXT NOT NULL, debe INTEGER NOT NULL DEFAULT 0, haber INTEGER NOT NULL DEFAULT 0,
                             CHECK (debe >= 0 AND haber >= 0 AND (debe = 0 OR haber = 0)));
        CREATE TABLE cobro (clave TEXT PRIMARY KEY, cliente TEXT, centavos INTEGER, estado TEXT, ref_procesador TEXT);
        """
    )
    return db


def asiento(db: sqlite3.Connection, ref: str, desc: str, lineas: list[tuple[str, int, int]]) -> None:
    """Un asiento exige debe == haber; una referencia repetida no se registra dos veces."""
    if sum(d for _, d, _ in lineas) != sum(h for _, _, h in lineas):
        raise ValueError("asiento desbalanceado")
    try:
        cur = db.execute("INSERT INTO asiento(referencia, descripcion) VALUES (?, ?)", (ref, desc))
    except sqlite3.IntegrityError:
        return
    for cuenta, d, h in lineas:
        db.execute("INSERT INTO apunte(asiento_id, cuenta, debe, haber) VALUES (?,?,?,?)", (cur.lastrowid, cuenta, d, h))


class Procesador:
    """Doble del procesador: cobra cada llamada nueva; con la misma clave devuelve el resultado ya guardado."""

    def __init__(self, respeta_clave: bool, rng: random.Random) -> None:
        self.respeta_clave, self.rng, self.vistas, self.cobros = respeta_clave, rng, {}, []

    def cobrar(self, clave: str, centavos: int) -> dict:
        if self.respeta_clave and clave in self.vistas:
            return self.vistas[clave]
        ref = f"ch_{len(self.cobros) + 1:05d}"
        self.cobros.append({"ref": ref, "centavos": centavos, "clave": clave})
        self.vistas[clave] = {"ref": ref, "ok": True}
        return self.vistas[clave]


def experimento_doble_cobro(con_clave: bool) -> dict:
    """El cliente reintenta tras un tiempo de espera: 1000 renovaciones, 8 % de reintentos por respuesta perdida."""
    rng = random.Random(SEMILLA)
    proc = Procesador(respeta_clave=True, rng=rng)
    intentos = 0
    for i in range(1000):
        clave = f"renovacion-{i:04d}"
        veces = 2 if rng.random() < 0.08 else 1
        for k in range(veces):
            intentos += 1
            proc.cobrar(clave if con_clave else f"{clave}-intento-{k}", 4900)
    unicos = 1000
    return {"intentos": intentos, "cobros_reales": len(proc.cobros), "cobros_de_mas": len(proc.cobros) - unicos,
            "dinero_de_mas_centavos": (len(proc.cobros) - unicos) * 4900}


def experimento_conciliacion() -> dict:
    rng = random.Random(SEMILLA)
    db = nueva_bd()
    proc = Procesador(respeta_clave=True, rng=rng)
    pagos = []
    for i in range(500):
        monto = rng.choice([1900, 4900, 9900, 29900])
        r = proc.cobrar(f"inv-{i:04d}", monto)
        pagos.append((f"inv-{i:04d}", r["ref"], monto))
        comision = round(monto * 0.029) + 30
        asiento(db, f"inv-{i:04d}", "cobro de factura", [
            ("procesador_por_cobrar", monto - comision, 0), ("comisiones_procesador", comision, 0), ("ingresos_suscripcion", 0, monto)])
    # liquidacion del procesador: la que el banco recibe. Se inyectan cuatro tipos de diferencia conocidos.
    liquidacion = {ref: (monto - (round(monto * 0.029) + 30)) for _, ref, monto in pagos}
    omitido = list(liquidacion)[10]; del liquidacion[omitido]                      # cobro que no llego a la liquidacion
    liquidacion["ch_99999"] = 4900 - 172                                           # cobro que el libro no conoce
    cambiado = list(liquidacion)[50]; liquidacion[cambiado] -= 500                 # monto distinto (disputa parcial)
    # duplicado en el libro: el mismo asiento con otra referencia
    asiento(db, "inv-0100-dup", "cobro de factura", [("procesador_por_cobrar", 4900 - 172, 0), ("comisiones_procesador", 172, 0), ("ingresos_suscripcion", 0, 4900)])
    libro = {}
    for ref_inv, ref, monto in pagos:
        libro[ref] = monto - (round(monto * 0.029) + 30)
    diferencias = []
    for ref in sorted(set(libro) | set(liquidacion)):
        a, b = libro.get(ref), liquidacion.get(ref)
        if a is None:
            diferencias.append((ref, "en liquidacion y no en libro", b))
        elif b is None:
            diferencias.append((ref, "en libro y no en liquidacion", a))
        elif a != b:
            diferencias.append((ref, "monto distinto", a - b))
    deb = db.execute("SELECT SUM(debe), SUM(haber) FROM apunte").fetchone()
    por_cobrar = db.execute("SELECT SUM(debe - haber) FROM apunte WHERE cuenta='procesador_por_cobrar'").fetchone()[0]
    total_liquidacion = sum(liquidacion.values())
    explicado = sum((-a if k.startswith("en liquidacion") else a) for _, k, a in diferencias) + (4900 - 172)
    ingresos_dup = db.execute("SELECT COUNT(*) FROM asiento WHERE referencia LIKE '%-dup'").fetchone()[0]
    return {"asientos": db.execute("SELECT COUNT(*) FROM asiento").fetchone()[0], "debe_total": deb[0], "haber_total": deb[1],
            "diferencias": diferencias, "por_cobrar_segun_libro": por_cobrar, "total_liquidacion": total_liquidacion,
            "brecha_total": por_cobrar - total_liquidacion, "explicado_por_pares": explicado, "duplicado_monto": 4900 - 172, "asientos_duplicados": ingresos_dup,
            "cobros": len(pagos), "ingresos_centavos": sum(m for _, _, m in pagos)}


def experimento_asiento_invalido() -> str:
    db = nueva_bd()
    try:
        asiento(db, "x", "roto", [("caja", 100, 0), ("ingresos", 0, 90)])
    except ValueError as exc:
        return str(exc)
    return "sin error"


def experimento_reembolso() -> dict:
    """Un reembolso es un asiento nuevo que revierte, no una edicion del anterior."""
    db = nueva_bd()
    asiento(db, "pago-1", "cobro", [("caja", 4900, 0), ("ingresos", 0, 4900)])
    asiento(db, "reembolso-1", "reembolso de pago-1", [("ingresos", 4900, 0), ("caja", 0, 4900)])
    saldo = {c: s for c, s in db.execute("SELECT cuenta, SUM(debe - haber) FROM apunte GROUP BY cuenta")}
    return {"asientos": db.execute("SELECT COUNT(*) FROM asiento").fetchone()[0], "saldo_ingresos": saldo["ingresos"], "saldo_caja": saldo["caja"]}


if __name__ == "__main__":
    print("sin clave:", experimento_doble_cobro(False))
    print("con clave:", experimento_doble_cobro(True))
    c = experimento_conciliacion()
    print({k: v for k, v in c.items() if k != "diferencias"})
    for d in c["diferencias"]:
        print("  diferencia:", d)
    print("asiento invalido:", experimento_asiento_invalido())
    print("reembolso:", experimento_reembolso())
