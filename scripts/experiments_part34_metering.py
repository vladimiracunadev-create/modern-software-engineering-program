"""Parte 34 (SaaS): medidor de uso idempotente, precios por tramos y motor de derechos con sqlite3.

Todo se ejecuta de verdad con sqlite3 en memoria y semilla fija 34; los precios y los planes son del autor
(no son los de ningun proveedor). Uso: python scripts/experiments_part34_metering.py
"""
from __future__ import annotations

import random
import sqlite3

SEMILLA = 34


def medidor(con_id: bool) -> dict:
    """30 000 eventos de uso; 6 % se entregan dos veces (reintento at-least-once) y 3 % llegan tarde."""
    rng = random.Random(SEMILLA)
    db = sqlite3.connect(":memory:")
    if con_id:
        db.execute("CREATE TABLE uso (evento_id TEXT PRIMARY KEY, cliente TEXT, periodo TEXT, unidades INTEGER)")
    else:
        db.execute("CREATE TABLE uso (evento_id TEXT, cliente TEXT, periodo TEXT, unidades INTEGER)")
    verdad = {}
    entregas = 0
    for i in range(30000):
        cliente = f"c{rng.randint(1, 40):02d}"
        periodo = "2026-10" if rng.random() > 0.03 else "2026-09"   # 3 % pertenece al periodo anterior y llega tarde
        unidades = rng.randint(1, 5)
        verdad[(cliente, periodo)] = verdad.get((cliente, periodo), 0) + unidades
        for _ in range(2 if rng.random() < 0.06 else 1):
            entregas += 1
            if con_id:
                db.execute("INSERT OR IGNORE INTO uso VALUES (?,?,?,?)", (f"ev-{i}", cliente, periodo, unidades))
            else:
                db.execute("INSERT INTO uso VALUES (?,?,?,?)", (f"ev-{i}", cliente, periodo, unidades))
    medido = {(c, p): u for c, p, u in db.execute("SELECT cliente, periodo, SUM(unidades) FROM uso GROUP BY cliente, periodo")}
    exceso = sum(medido[k] - verdad[k] for k in verdad)
    facturas_mal = sum(1 for k in verdad if medido[k] != verdad[k])
    return {"eventos_reales": 30000, "entregas": entregas, "unidades_reales": sum(verdad.values()), "unidades_medidas": sum(medido.values()),
            "unidades_de_mas": exceso, "pares_cliente_periodo": len(verdad), "pares_con_error": facturas_mal,
            "tardios_en_periodo_anterior": sum(u for (c, p), u in verdad.items() if p == "2026-09")}


def precio_tramos(unidades: int, tramos: list[tuple[int | None, float]]) -> float:
    """Gradual: cada tramo se cobra a su precio. tramos = [(tope, precio_por_unidad)], tope None = sin tope."""
    total, previo = 0.0, 0
    for tope, precio in tramos:
        limite = unidades if tope is None else min(unidades, tope)
        if limite > previo:
            total += (limite - previo) * precio
            previo = limite
    return total


def precio_volumen(unidades: int, tramos: list[tuple[int | None, float]]) -> float:
    """Por volumen: toda la cantidad se cobra al precio del tramo en que cae."""
    for tope, precio in tramos:
        if tope is None or unidades <= tope:
            return unidades * precio
    raise ValueError


TRAMOS = [(1000, 0.020), (10000, 0.015), (None, 0.010)]


def prorrateo(precio_mensual: int, dias_mes: int, dia_cambio: int, precio_nuevo: int) -> dict:
    """Cambio de plan a mitad de ciclo: credito por lo no usado del plan viejo y cargo por lo que resta del nuevo (en centavos)."""
    restantes = dias_mes - dia_cambio + 1
    credito = round(precio_mensual * restantes / dias_mes)
    cargo = round(precio_nuevo * restantes / dias_mes)
    return {"credito": credito, "cargo": cargo, "neto": cargo - credito}


def motor_derechos() -> dict:
    db = sqlite3.connect(":memory:")
    db.executescript(
        """
        CREATE TABLE plan (plan TEXT, clave TEXT, valor INTEGER, PRIMARY KEY (plan, clave));
        CREATE TABLE cliente (id TEXT PRIMARY KEY, plan TEXT, estado TEXT);
        CREATE TABLE excepcion (cliente TEXT, clave TEXT, valor INTEGER, vence TEXT, PRIMARY KEY (cliente, clave));
        CREATE TABLE consumo (cliente TEXT, clave TEXT, usado INTEGER, PRIMARY KEY (cliente, clave));
        """
    )
    plan = {"gratis": {"usuarios": 3, "proyectos": 2, "api_por_mes": 1000, "exportar": 0, "sso": 0},
            "equipo": {"usuarios": 25, "proyectos": 50, "api_por_mes": 100000, "exportar": 1, "sso": 0},
            "empresa": {"usuarios": 1000, "proyectos": 5000, "api_por_mes": 5000000, "exportar": 1, "sso": 1}}
    for p, d in plan.items():
        for k, v in d.items():
            db.execute("INSERT INTO plan VALUES (?,?,?)", (p, k, v))
    db.execute("INSERT INTO cliente VALUES ('acme','equipo','activo'), ('beta','gratis','activo'), ('gama','empresa','suspendido')")
    db.execute("INSERT INTO excepcion VALUES ('acme','sso',1,'2026-12-31'), ('acme','usuarios',40,'2026-06-30')")
    db.execute("INSERT INTO consumo VALUES ('acme','usuarios',25), ('beta','proyectos',2)")

    def puede(cliente: str, clave: str, hoy: str, pedir: int = 1) -> tuple[bool, str]:
        fila = db.execute("SELECT plan, estado FROM cliente WHERE id=?", (cliente,)).fetchone()
        if fila is None:
            return False, "cliente_desconocido"
        if fila[1] != "activo":
            return False, "cuenta_" + fila[1]
        exc = db.execute("SELECT valor FROM excepcion WHERE cliente=? AND clave=? AND vence >= ?", (cliente, clave, hoy)).fetchone()
        limite = exc[0] if exc else db.execute("SELECT valor FROM plan WHERE plan=? AND clave=?", (fila[0], clave)).fetchone()[0]
        usado = (db.execute("SELECT usado FROM consumo WHERE cliente=? AND clave=?", (cliente, clave)).fetchone() or (0,))[0]
        if usado + pedir > limite:
            return False, f"limite_{limite}_usado_{usado}"
        return True, "ok"

    pruebas = [("acme", "sso", "2026-11-23"), ("acme", "usuarios", "2026-11-23"), ("acme", "usuarios", "2026-05-01"),
               ("beta", "proyectos", "2026-11-23"), ("beta", "exportar", "2026-11-23"), ("gama", "sso", "2026-11-23"), ("zeta", "sso", "2026-11-23")]
    return {f"{c}:{k}@{h}": puede(c, k, h) for c, k, h in pruebas}


def dunning(seed: int = SEMILLA) -> list[tuple[str, int, int]]:
    """Modelo: 1000 renovaciones, 8 % falla el primer cobro; cada reintento recupera un porcentaje fijo del autor."""
    rng = random.Random(seed)
    pendientes = sum(1 for _ in range(1000) if rng.random() < 0.08)
    prob = [("dia 1", 0.35), ("dia 3", 0.25), ("dia 7", 0.20), ("dia 14", 0.12)]
    filas, restantes = [], pendientes
    for etapa, p in prob:
        rec = sum(1 for _ in range(restantes) if rng.random() < p)
        restantes -= rec
        filas.append((etapa, rec, restantes))
    return [("fallos iniciales", pendientes, pendientes)] + filas


def mercado(semilla: int = SEMILLA, n: int = 1000) -> list[tuple[str, float, float]]:
    """1000 clientes simulados; cada uno valora el producto segun su tamano (lognormal, semilla fija) y usa `u` puestos.

    Devuelve filas (diseno de precio, ingreso total, clientes que compran). Parametros del autor, no un mercado real.
    """
    rng = random.Random(semilla)
    clientes = []
    for _ in range(n):
        puestos = max(1, int(rng.lognormvariate(1.6, 1.0)))
        valor_por_puesto = rng.lognormvariate(2.9, 0.5)          # disposicion a pagar por puesto y mes
        clientes.append((puestos, valor_por_puesto * puestos ** 0.9))
    def ingreso_unico(precio: float) -> tuple[float, int]:
        compran = [c for c in clientes if c[1] >= precio]
        return precio * len(compran), len(compran)
    mejor = max(((p, *ingreso_unico(p)) for p in range(5, 400, 5)), key=lambda x: x[1])
    def tres_planes(p1: float, p2: float, p3: float) -> tuple[float, int]:
        tot, k = 0.0, 0
        for puestos, valor in clientes:
            # el cliente elige el plan de mayor excedente: basico hasta 5 puestos, equipo hasta 25, empresa sin tope
            opciones = []
            if puestos <= 5 and valor >= p1: opciones.append((valor - p1, p1))
            if puestos <= 25 and valor >= p2: opciones.append((valor - p2, p2))
            if valor >= p3: opciones.append((valor - p3, p3))
            if opciones:
                tot += max(opciones)[1]; k += 1
        return tot, k
    mejor3 = max(((a, b, c, *tres_planes(a, b, c)) for a in range(10, 70, 10) for b in range(60, 260, 20) for c in range(200, 1001, 100) if a < b < c), key=lambda x: x[3])
    por_puesto = max(((p, sum(p * pu for pu, v in clientes if v >= p * pu), sum(1 for pu, v in clientes if v >= p * pu)) for p in [x / 2 for x in range(2, 80)]), key=lambda x: x[1])
    return [("Un precio unico", mejor[1], mejor[2]), ("Tres planes con limites", mejor3[3], mejor3[4]), ("Precio por puesto", por_puesto[1], por_puesto[2])]


def curva_precio(semilla: int = SEMILLA, n: int = 1000) -> list[tuple[int, float]]:
    rng = random.Random(semilla)
    cs = []
    for _ in range(n):
        puestos = max(1, int(rng.lognormvariate(1.6, 1.0)))
        cs.append(rng.lognormvariate(2.9, 0.5) * puestos ** 0.9 * 1.0)
    return [(p, p * sum(1 for v in cs if v >= p)) for p in range(10, 301, 10)]


def metricas_saas() -> dict:
    """MRR, bajas y retencion neta de un mes a partir de eventos de suscripcion (sqlite3, datos sinteticos con semilla 34)."""
    rng = random.Random(SEMILLA)
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE suscripcion (cliente TEXT, mes TEXT, mrr INTEGER)")
    planes = [0, 49, 199, 999]
    for i in range(400):
        base = rng.choices(planes, weights=[10, 55, 30, 5])[0]
        if base == 0:
            continue
        db.execute("INSERT INTO suscripcion VALUES (?, '2026-09', ?)", (f"c{i:03d}", base))
        r = rng.random()
        if r < 0.04:
            continue                                  # baja: no aparece en octubre
        nuevo = base
        if r > 0.86:
            nuevo = planes[min(3, planes.index(base) + 1)]   # mejora de plan
        elif r > 0.80 and base > 49:
            nuevo = planes[planes.index(base) - 1]            # baja de plan
        db.execute("INSERT INTO suscripcion VALUES (?, '2026-10', ?)", (f"c{i:03d}", nuevo))
    for i in range(400, 440):                       # clientes nuevos de octubre
        db.execute("INSERT INTO suscripcion VALUES (?, '2026-10', ?)", (f"c{i:03d}", rng.choices([49, 199], weights=[75, 25])[0]))
    q = lambda sql: db.execute(sql).fetchone()[0] or 0
    ini = q("SELECT SUM(mrr) FROM suscripcion WHERE mes='2026-09'")
    fin = q("SELECT SUM(mrr) FROM suscripcion WHERE mes='2026-10'")
    nuevos = q("SELECT SUM(o.mrr) FROM suscripcion o WHERE o.mes='2026-10' AND o.cliente NOT IN (SELECT cliente FROM suscripcion WHERE mes='2026-09')")
    bajas = q("SELECT SUM(s.mrr) FROM suscripcion s WHERE s.mes='2026-09' AND s.cliente NOT IN (SELECT cliente FROM suscripcion WHERE mes='2026-10')")
    exp = q("SELECT SUM(o.mrr - s.mrr) FROM suscripcion s JOIN suscripcion o ON o.cliente=s.cliente AND o.mes='2026-10' WHERE s.mes='2026-09' AND o.mrr > s.mrr")
    contr = q("SELECT SUM(s.mrr - o.mrr) FROM suscripcion s JOIN suscripcion o ON o.cliente=s.cliente AND o.mes='2026-10' WHERE s.mes='2026-09' AND o.mrr < s.mrr")
    clientes_ini = q("SELECT COUNT(*) FROM suscripcion WHERE mes='2026-09'")
    clientes_baja = q("SELECT COUNT(*) FROM suscripcion s WHERE s.mes='2026-09' AND s.cliente NOT IN (SELECT cliente FROM suscripcion WHERE mes='2026-10')")
    return {"mrr_inicio": ini, "mrr_fin": fin, "nuevos": nuevos, "expansion": exp, "contraccion": contr, "bajas": bajas,
            "cuadra": ini + nuevos + exp - contr - bajas == fin, "clientes_inicio": clientes_ini, "clientes_baja": clientes_baja,
            "baja_de_clientes_pct": round(100 * clientes_baja / clientes_ini, 1),
            "retencion_neta_pct": round(100 * (ini + exp - contr - bajas) / ini, 1), "retencion_bruta_pct": round(100 * (ini - contr - bajas) / ini, 1)}


if __name__ == "__main__":
    print("metricas:", metricas_saas())
    print("mercado:", [(a, round(b), c) for a, b, c in mercado()])
    print("curva:", curva_precio())
    print("sin id:", medidor(False))
    print("con id:", medidor(True))
    for n in (500, 5000, 25000):
        print(n, "gradual", round(precio_tramos(n, TRAMOS), 2), "volumen", round(precio_volumen(n, TRAMOS), 2))
    print("prorrateo 49 -> 99, dia 11 de 30:", prorrateo(4900, 30, 11, 9900))
    print("prorrateo 99 -> 49, dia 11 de 30:", prorrateo(9900, 30, 11, 4900))
    for k, v in motor_derechos().items():
        print(k, v)
    print("dunning:", dunning())
