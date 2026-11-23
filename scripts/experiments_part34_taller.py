"""Parte 34 (SaaS): taller integrador. Un producto minimo con seis defectos sembrados y seis comprobaciones.

Cada defecto se activa por separado; se ejecutan las seis comprobaciones y se imprime la matriz defecto por
comprobacion (que prueba falla con cada defecto). Todo es sqlite3 en memoria o en un archivo temporal, hilos reales
y datos sinteticos; no se llama a ningun servicio. Uso: python scripts/experiments_part34_taller.py
"""
from __future__ import annotations

import os
import sqlite3
import tempfile
import threading

DEFECTOS = {
    "D1": "consulta sin filtro de inquilino",
    "D2": "evento de uso duplicado",
    "D3": "cobro repetido sin clave",
    "D4": "sobreventa concurrente",
    "D5": "limite del plan ignorado",
    "D6": "asiento que no cuadra",
}
COMPROBACIONES = ["aislamiento", "idempotencia", "concurrencia", "derechos", "asiento_balanceado", "conciliacion"]


class Producto:
    def __init__(self, defecto: str | None) -> None:
        self.defecto = defecto
        self.db = sqlite3.connect(":memory:")
        self.db.executescript(
            """
            CREATE TABLE tarea (inquilino TEXT, titulo TEXT);
            CREATE TABLE evento_origen (evento_id TEXT PRIMARY KEY, inquilino TEXT, unidades INTEGER);
            CREATE TABLE uso (evento_id TEXT, inquilino TEXT, unidades INTEGER);
            CREATE TABLE usuario (inquilino TEXT, nombre TEXT);
            CREATE TABLE asiento (id INTEGER PRIMARY KEY, referencia TEXT);
            CREATE TABLE apunte (asiento_id INTEGER, cuenta TEXT, debe INTEGER, haber INTEGER);
            """
        )
        self.procesador: list[tuple[str, int]] = []      # (referencia, importe) cobrados de verdad
        self.claves: dict[str, str] = {}
        self.limite_usuarios = {"gratis": 3}

    # --- aislamiento
    def tareas(self, inquilino: str) -> list[str]:
        if self.defecto == "D1":
            return [r[0] for r in self.db.execute("SELECT titulo FROM tarea")]
        return [r[0] for r in self.db.execute("SELECT titulo FROM tarea WHERE inquilino=?", (inquilino,))]

    # --- uso
    def registrar_uso(self, evento_id: str, inquilino: str, unidades: int) -> None:
        self.db.execute("INSERT OR IGNORE INTO evento_origen VALUES (?,?,?)", (evento_id, inquilino, unidades))
        if self.defecto == "D2" or not self.db.execute("SELECT 1 FROM uso WHERE evento_id=?", (evento_id,)).fetchone():
            self.db.execute("INSERT INTO uso VALUES (?,?,?)", (evento_id, inquilino, unidades))

    # --- cobro y libro
    def asiento(self, referencia: str, lineas: list[tuple[str, int, int]]) -> None:
        if self.defecto != "D6" and sum(d for _, d, _ in lineas) != sum(h for _, _, h in lineas):
            raise ValueError("asiento desbalanceado")
        cur = self.db.execute("INSERT INTO asiento(referencia) VALUES (?)", (referencia,))
        for c, d, h in lineas:
            self.db.execute("INSERT INTO apunte VALUES (?,?,?,?)", (cur.lastrowid, c, d, h))

    def cobrar(self, clave: str, importe: int) -> None:
        if self.defecto != "D3" and clave in self.claves:
            return
        ref = f"ch_{len(self.procesador) + 1:03d}"
        self.procesador.append((ref, importe))
        self.claves[clave] = ref
        if self.defecto == "D6":
            self.asiento(ref, [("por_cobrar", importe, 0), ("ingresos", 0, importe - 100)])      # descuadre de 100
        else:
            self.asiento(ref, [("por_cobrar", importe, 0), ("ingresos", 0, importe)])

    # --- derechos
    def crear_usuario(self, inquilino: str, nombre: str, plan: str = "gratis") -> bool:
        usados = self.db.execute("SELECT COUNT(*) FROM usuario WHERE inquilino=?", (inquilino,)).fetchone()[0]
        if self.defecto != "D5" and usados + 1 > self.limite_usuarios[plan]:
            return False
        self.db.execute("INSERT INTO usuario VALUES (?,?)", (inquilino, nombre))
        return True


def inventario_concurrente(defecto: str | None) -> int:
    """Pedidos aceptados con 20 hilos y 5 unidades; con D4 se lee y luego se escribe."""
    with tempfile.TemporaryDirectory() as carpeta:
        ruta = os.path.join(carpeta, "inv.db")
        con = sqlite3.connect(ruta)
        con.execute("CREATE TABLE p (disponible INTEGER NOT NULL CHECK (disponible >= 0))")
        con.execute("CREATE TABLE pedido (n INTEGER)")
        con.execute("INSERT INTO p VALUES (5)")
        con.commit()
        con.close()
        barrera = threading.Barrier(20)

        def comprar(n: int) -> None:
            c = sqlite3.connect(ruta, timeout=30, isolation_level=None)
            barrera.wait()
            if defecto == "D4":
                (d,) = c.execute("SELECT disponible FROM p").fetchone()
                if d > 0:
                    threading.Event().wait(0.002)
                    c.execute("UPDATE p SET disponible = ?", (max(d - 1, 0),))
                    c.execute("INSERT INTO pedido VALUES (?)", (n,))
            else:
                if c.execute("UPDATE p SET disponible = disponible - 1 WHERE disponible > 0").rowcount == 1:
                    c.execute("INSERT INTO pedido VALUES (?)", (n,))
            c.close()

        hilos = [threading.Thread(target=comprar, args=(i,)) for i in range(20)]
        for h in hilos:
            h.start()
        for h in hilos:
            h.join()
        con = sqlite3.connect(ruta)
        n = con.execute("SELECT COUNT(*) FROM pedido").fetchone()[0]
        con.close()
        return n


def ejecutar(defecto: str | None) -> dict[str, bool]:
    """True = la comprobacion FALLA (detecta un problema)."""
    p = Producto(defecto)
    p.db.execute("INSERT INTO tarea VALUES ('A', 'tarea de A'), ('B', 'tarea de B')")
    aislamiento = any("de B" in t for t in p.tareas("A"))

    p.registrar_uso("e1", "A", 10)
    p.registrar_uso("e1", "A", 10)                       # entrega repetida
    unidades = p.db.execute("SELECT SUM(unidades) FROM uso WHERE inquilino='A'").fetchone()[0]
    p.cobrar("renovacion-A-2026-11", 4900)
    p.cobrar("renovacion-A-2026-11", 4900)               # reintento con la misma clave
    cobros_extra = len(p.procesador) - 1
    idempotencia = unidades != 10 or cobros_extra != 0

    concurrencia = inventario_concurrente(defecto) > 5

    for i in range(3):
        p.crear_usuario("A", f"u{i}")
    derechos = p.crear_usuario("A", "u4")                # el cuarto debe rechazarse

    try:
        p.asiento("prueba-desbalanceada", [("caja", 100, 0), ("ingresos", 0, 90)])
        balance = True                                   # lo acepto: la comprobacion falla
    except ValueError:
        balance = False

    # conciliacion: libro contra liquidacion del procesador y uso agregado contra eventos de origen
    por_cobrar = p.db.execute("SELECT COALESCE(SUM(debe - haber), 0) FROM apunte WHERE cuenta='por_cobrar'").fetchone()[0]
    ingresos = p.db.execute("SELECT COALESCE(SUM(haber - debe), 0) FROM apunte WHERE cuenta='ingresos'").fetchone()[0]
    liquidado = sum(i for _, i in p.procesador)
    origen = p.db.execute("SELECT SUM(unidades) FROM evento_origen WHERE inquilino='A'").fetchone()[0]
    facturado = 4900                                     # lo que la factura de la renovacion dice que se debia cobrar
    conciliacion = por_cobrar != liquidado or ingresos != liquidado or unidades != origen or liquidado != facturado
    # el asiento sembrado de la comprobacion de balance (si se acepto) tambien descuadra el libro
    deb = p.db.execute("SELECT SUM(debe), SUM(haber) FROM apunte").fetchone()
    conciliacion = conciliacion or deb[0] != deb[1]
    return {"aislamiento": aislamiento, "idempotencia": idempotencia, "concurrencia": concurrencia,
            "derechos": derechos, "asiento_balanceado": balance, "conciliacion": conciliacion}


if __name__ == "__main__":
    base = ejecutar(None)
    print("sin defectos:", base)
    cabecera = " ".join(f"{c[:11]:>11}" for c in COMPROBACIONES)
    print(f"{'':>4} {cabecera}")
    for d in DEFECTOS:
        r = ejecutar(d)
        print(f"{d:>4} " + " ".join(f"{('falla' if r[c] else '-'):>11}" for c in COMPROBACIONES), " ", DEFECTOS[d])
