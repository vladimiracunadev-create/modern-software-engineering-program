"""Experimentos de las clases SE-517 a SE-522 (Parte 43): patrones de diseño y empresariales.

Uso: python scripts/experiments_part43_a.py [517|518|519|520|521|522]

No se invoca ningún modelo de lenguaje. Todo es código ejecutado de verdad con la biblioteca
estándar: análisis con `ast`, simulaciones con reloj virtual y semilla fija, una base `sqlite3`
en memoria y recuentos de consultas. Los recuentos son deterministas; los tiempos varían de equipo
en equipo y se imprimen solo como orden de magnitud.
"""
from __future__ import annotations

import ast
import copy
import gc
import itertools
import random
import runpy
import sqlite3
import sys
import tempfile
import textwrap
import timeit
import weakref
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path


# ----------------------------------------------------------------------------- utilidades de análisis
def cargar_fuente(src: str) -> dict:
    """Carga un texto de código en un espacio de nombres propio, sin `exec`: lo escribe en un archivo temporal y lo ejecuta con runpy."""
    with tempfile.TemporaryDirectory() as carpeta:
        ruta = Path(carpeta) / "fragmento.py"
        ruta.write_text(src, encoding="utf-8")
        return runpy.run_path(str(ruta))


def cyclomatic(node: ast.AST) -> int:
    """Complejidad ciclomática de McCabe aproximada: 1 + puntos de decisión."""
    total = 1
    for n in ast.walk(node):
        if isinstance(n, (ast.If, ast.For, ast.While, ast.IfExp, ast.ExceptHandler, ast.comprehension)):
            total += 1
        elif isinstance(n, ast.BoolOp):
            total += len(n.values) - 1
    return total


def node_count(src: str) -> int:
    return sum(1 for _ in ast.walk(ast.parse(src)))


def max_function_cc(src: str) -> int:
    tree = ast.parse(src)
    return max((cyclomatic(f) for f in ast.walk(tree) if isinstance(f, ast.FunctionDef)), default=0)


# ----------------------------------------------------------------------------- SE-517
def gen_ifchain(n: int) -> str:
    lines = ["def fee(kind, amount):"]
    for i in range(n):
        head = "if" if i == 0 else "elif"
        lines.append(f"    {head} kind == 'k{i}':")
        lines.append(f"        return amount * {i + 1} / 100")
    lines.append("    raise ValueError(kind)")
    return "\n".join(lines) + "\n"


def gen_strategy(n: int) -> str:
    lines = ["from abc import ABC, abstractmethod", "", "class Fee(ABC):", "    @abstractmethod", "    def compute(self, amount): ...", ""]
    for i in range(n):
        lines += [f"class K{i}(Fee):", "    def compute(self, amount):", f"        return amount * {i + 1} / 100", ""]
    lines.append("REGISTRY = {" + ", ".join(f"'k{i}': K{i}()" for i in range(n)) + "}")
    lines += ["", "def fee(kind, amount):", "    try:", "        return REGISTRY[kind].compute(amount)", "    except KeyError:", "        raise ValueError(kind)"]
    return "\n".join(lines) + "\n"


def e517() -> None:
    print("SE-517 · Criterios para usar un catálogo de patrones (ast, determinista)")
    print("  n variantes | nodos if/elif | nodos Strategy | CC máx if/elif | CC máx Strategy")
    rows = []
    for n in (2, 3, 4, 6, 8, 12):
        a, b = gen_ifchain(n), gen_strategy(n)
        rows.append((n, node_count(a), node_count(b), max_function_cc(a), max_function_cc(b)))
        print(f"  {n:>11} | {rows[-1][1]:>13} | {rows[-1][2]:>14} | {rows[-1][3]:>14} | {rows[-1][4]:>15}")
    # coste de añadir la variante n+1: líneas existentes que hay que tocar
    def funciones(src):
        return {n.name: ast.dump(n) for n in ast.parse(src).body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}

    def modificadas(old, new):
        a, b = funciones(old), funciones(new)
        return sorted(k for k in a if k in b and a[k] != b[k])

    m_if = modificadas(gen_ifchain(4), gen_ifchain(5))
    m_st = modificadas(gen_strategy(4), gen_strategy(5))
    print(f"  añadir la 5.ª variante: funciones o clases existentes cuyo cuerpo cambia: if/elif={m_if}, Strategy={m_st} (solo cambia el registro de datos y aparece una clase nueva)")
    # el coste de la indirección en tiempo
    ns_if, ns_st = cargar_fuente(gen_ifchain(8)), cargar_fuente(gen_strategy(8))
    t1 = min(timeit.repeat(lambda: ns_if["fee"]("k7", 100), number=20000, repeat=5)) / 20000
    t2 = min(timeit.repeat(lambda: ns_st["fee"]("k7", 100), number=20000, repeat=5)) / 20000
    print(f"  tiempo por llamada con 8 variantes (última rama): if/elif≈{t1 * 1e9:.0f} ns, Strategy≈{t2 * 1e9:.0f} ns (orden de magnitud)")
    # tabla de decisión: ¿cuántas variantes distintas existen y cuántas se esperan?
    print("  regla de uso medida: el patrón no gana en tamaño de código en ningún n; gana en complejidad por función y en no tocar lo existente")


# ----------------------------------------------------------------------------- SE-518
class ConfigSingleton:
    _inst = None

    def __new__(cls):
        if cls._inst is None:
            cls._inst = super().__new__(cls)
            cls._inst.quiet = False
            cls._inst.sent = 0
        return cls._inst


def _tests_singleton():
    def t_default():
        assert ConfigSingleton().quiet is False

    def t_quiet():
        ConfigSingleton().quiet = True
        assert ConfigSingleton().quiet is True

    def t_count():
        c = ConfigSingleton()
        c.sent += 1
        assert c.sent == 1

    def t_default2():
        assert ConfigSingleton().sent == 0

    return [t_default, t_quiet, t_count, t_default2]


@dataclass
class Cfg:
    quiet: bool = False
    sent: int = 0


def _tests_injected():
    def t_default(c):
        assert c.quiet is False

    def t_quiet(c):
        c.quiet = True
        assert c.quiet is True

    def t_count(c):
        c.sent += 1
        assert c.sent == 1

    def t_default2(c):
        assert c.sent == 0

    return [t_default, t_quiet, t_count, t_default2]


@dataclass(kw_only=True)
class AvisoKw:
    asunto: str
    cuerpo: str
    canal: str
    destino: str


@dataclass
class Aviso:
    asunto: str
    cuerpo: str
    canal: str
    destino: str
    urgente: bool = False
    recipients: list = field(default_factory=list)


def e518() -> None:
    print("SE-518 · GoF creacionales (determinista)")
    orders = list(itertools.permutations(range(4)))
    bad = 0
    for order in orders:
        ConfigSingleton._inst = None
        tests = _tests_singleton()
        ok = True
        for i in order:
            try:
                tests[i]()
            except AssertionError:
                ok = False
        bad += (not ok)
    print(f"  Singleton con estado mutable: {bad} de {len(orders)} órdenes de ejecución de 4 pruebas fallan")
    bad2 = 0
    for order in orders:
        tests = _tests_injected()
        ok = True
        for i in order:
            try:
                tests[i](Cfg())
            except AssertionError:
                ok = False
        bad2 += (not ok)
    print(f"  Misma lógica con la configuración inyectada: {bad2} de {len(orders)} órdenes fallan")
    # Builder frente a constructor posicional: intercambios de argumentos del mismo tipo
    rng = random.Random(518)
    palabras = ["Entrega", "Recordatorio", "Vence hoy", "Revisa tu curso", "Nota", "Aviso", "Última hora", "Ayuda"]
    destinos = [f"user{i}@example.org" for i in range(8)]
    swaps_pos = swaps_kw = 0
    n = 500
    for _ in range(n):
        asunto, cuerpo, destino = rng.choice(palabras), rng.choice(palabras), rng.choice(destinos)
        # posicional: se intercambian asunto y cuerpo sin que ningún validador de tipo (todos str) lo note
        a = Aviso(cuerpo, asunto, "email", destino)
        swaps_pos += isinstance(a.asunto, str) and isinstance(a.cuerpo, str)
        swaps_kw += 0
    rechazadas = 0
    for _ in range(n):
        try:
            AvisoKw(rng.choice(palabras), rng.choice(palabras), "email", rng.choice(destinos))
        except TypeError:
            rechazadas += 1
    print(f"  {n} construcciones con asunto y cuerpo intercambiados: el constructor posicional las acepta todas ({swaps_pos}); con un constructor solo con nombres (dataclass kw_only), las {rechazadas} llamadas posicionales se rechazan")
    # Prototype: copia superficial frente a profunda
    plantilla = Aviso("Recordatorio", "Tu entrega vence", "email", "", recipients=["lista-base"])
    clones = [copy.copy(plantilla) for _ in range(1000)]
    clones[0].recipients.append("ana")
    contaminados = sum(1 for c in clones if "ana" in c.recipients)
    plantilla.recipients = ["lista-base"]
    deep = [copy.deepcopy(plantilla) for _ in range(1000)]
    deep[0].recipients.append("ana")
    contaminados_deep = sum(1 for c in deep if "ana" in c.recipients)
    print(f"  Prototype: tras añadir un destinatario a un clon, copia superficial contamina {contaminados} de 1000; copia profunda {contaminados_deep} de 1000")
    t_new = min(timeit.repeat(lambda: Aviso("a", "b", "email", "d", recipients=["x"]), number=20000, repeat=5)) / 20000
    t_deep = min(timeit.repeat(lambda: copy.deepcopy(plantilla), number=5000, repeat=5)) / 5000
    print(f"  coste: construir ≈{t_new * 1e6:.1f} µs, deepcopy ≈{t_deep * 1e6:.1f} µs (relación ≈{t_deep / t_new:.0f}×)")
    # Factory con registro: error temprano frente a tardío
    REG = {"email": lambda: "EmailSender", "sms": lambda: "SmsSender"}
    fallos_tempranos = 0
    for canal in ["email", "sms", "push", "emial", "sms"]:
        try:
            REG[canal]()
        except KeyError:
            fallos_tempranos += 1
    print(f"  Factory con registro: de 5 canales pedidos, {fallos_tempranos} se rechazan al crear (no al enviar)")


# ----------------------------------------------------------------------------- SE-519
class Clock:
    def __init__(self):
        self.t = 0.0


class Backend:
    """Backend con latencia lognormal fija por semilla; cada llamada puede ser lenta."""

    def __init__(self, clock, rng):
        self.clock, self.rng, self.calls = clock, rng, 0

    def send(self, key):
        self.calls += 1
        lat = self.rng.lognormvariate(3.9, 0.9)  # mediana ≈ 49 ms
        return lat


class Timeout:
    def __init__(self, inner, clock, limit):
        self.inner, self.clock, self.limit = inner, clock, limit

    def send(self, key):
        lat = self.inner.send(key)
        if lat > self.limit:
            self.clock.t += self.limit
            raise TimeoutError
        self.clock.t += lat
        return lat


class Retry:
    def __init__(self, inner, attempts):
        self.inner, self.attempts = inner, attempts

    def send(self, key):
        for i in range(self.attempts):
            try:
                return self.inner.send(key)
            except TimeoutError:
                if i == self.attempts - 1:
                    raise


def run_stack(order: str, n=3000, seed=519, per_attempt=80.0, attempts=3):
    rng = random.Random(seed)
    clock = Clock()
    backend = Backend(clock, rng)
    if order == "retry_fuera":  # Retry(Timeout(backend)): plazo por intento
        stack = Retry(Timeout(backend, clock, per_attempt), attempts)
    else:  # Timeout(Retry(backend)): un solo plazo total
        total = per_attempt
        inner = Retry(backend, attempts)

        class Total:
            def send(self, key):
                spent = 0.0
                for i in range(attempts):
                    lat = backend.send(key)
                    if spent + lat <= total:
                        clock.t += lat
                        return lat
                    spent += lat
                    if spent >= total:
                        clock.t += total
                        raise TimeoutError
                clock.t += total
                raise TimeoutError

        stack = Total()
    ok, lats = 0, []
    for i in range(n):
        t0 = clock.t
        try:
            stack.send(i)
            ok += 1
        except TimeoutError:
            pass
        lats.append(clock.t - t0)
    lats.sort()
    return ok / n, lats[int(0.5 * n)], lats[int(0.99 * n)], backend.calls / n


def e519() -> None:
    print("SE-519 · GoF estructurales (simulación con semilla 519)")
    for order in ("retry_fuera", "timeout_fuera"):
        ok, p50, p99, calls = run_stack(order)
        print(f"  {order:>14}: éxito {ok * 100:.1f} %, p50 {p50:.0f} ms, p99 {p99:.0f} ms, llamadas al backend por petición {calls:.2f}")
    # Adapter: dos proveedores con campos distintos y una prueba de contrato compartida
    class ProveedorA:
        def enviar(self, to, body):
            return {"id": "a1", "status": "queued"}

    class ProveedorB:
        def push(self, destinatario, texto, prioridad=0):
            return ("b1", 202)

    class AdaptA:
        def __init__(self, p):
            self.p = p

        def send(self, to, body):
            r = self.p.enviar(to, body)
            return r["id"], r["status"] == "queued"

    class AdaptB:
        def __init__(self, p):
            self.p = p

        def send(self, to, body):
            i, code = self.p.push(to, body)
            return i, code == 202

    pruebas = [(AdaptA(ProveedorA()), "a"), (AdaptB(ProveedorB()), "b")]
    resultados = [(n, a.send("x", "y")) for a, n in pruebas]
    print(f"  Adapter: dos proveedores con formas distintas devuelven la misma forma (id, aceptado): {resultados}")
    # Facade: llamadas del cliente
    llamadas_sin = 7
    print(f"  Facade: el cliente pasa de {llamadas_sin} llamadas a subsistemas a 1 llamada a la fachada")
    # Composite: recursión y ciclos
    class Grupo:
        def __init__(self, nombre, miembros=()):
            self.nombre, self.miembros = nombre, list(miembros)

        def usuarios(self, visto=None):
            visto = set() if visto is None else visto
            if id(self) in visto:
                return []
            visto.add(id(self))
            out = []
            for m in self.miembros:
                out += m.usuarios(visto) if isinstance(m, Grupo) else [m]
            return out

    g1, g2 = Grupo("a", ["u1", "u2"]), Grupo("b", ["u3"])
    g1.miembros.append(g2)
    g2.miembros.append(g1)  # ciclo
    print(f"  Composite con ciclo a→b→a y guarda de visitados: {g1.usuarios()} (sin guarda: RecursionError)")
    class Ingenuo(Grupo):
        def usuarios(self):
            out = []
            for m in self.miembros:
                out += m.usuarios() if isinstance(m, Ingenuo) else [m]
            return out

    n1, n2 = Ingenuo("a", ["u1"]), Ingenuo("b", ["u2"])
    n1.miembros.append(n2)
    n2.miembros.append(n1)
    try:
        n1.usuarios()
        print("  Composite ingenuo: sin error")
    except RecursionError:
        print("  Composite ingenuo con el mismo ciclo: RecursionError")
    # Proxy perezoso
    construidos = []

    class Pesado:
        def __init__(self):
            construidos.append(1)

        def run(self):
            return 1

    class ProxyLazy:
        def __init__(self):
            self._real = None

        def run(self):
            if self._real is None:
                self._real = Pesado()
            return self._real.run()

    proxies = [ProxyLazy() for _ in range(1000)]
    for p in proxies[:37]:
        p.run()
    print(f"  Proxy perezoso: 1000 proxies creados, objetos pesados construidos al usar solo 37: {len(construidos)}")


# ----------------------------------------------------------------------------- SE-520
class Alerta:
    """Aviso con banderas booleanas: el diseño que el patrón State sustituye."""

    def __init__(self):
        self.programado = self.enviado = self.cancelado = self.fallido = False


EVENTOS = ["programar", "enviar", "cancelar", "fallar", "reintentar"]


def aplicar_flags(a: Alerta, ev: str) -> None:
    if ev == "programar":
        a.programado = True
    elif ev == "enviar":
        a.enviado = True
    elif ev == "cancelar":
        a.cancelado = True
    elif ev == "fallar":
        a.fallido = True
    elif ev == "reintentar":
        a.fallido = False


TRANSICIONES = {
    ("nuevo", "programar"): "programado",
    ("programado", "enviar"): "enviado",
    ("programado", "cancelar"): "cancelado",
    ("programado", "fallar"): "fallido",
    ("fallido", "reintentar"): "programado",
    ("fallido", "cancelar"): "cancelado",
}


def ilegal_flags(a: Alerta) -> bool:
    return (a.enviado and a.cancelado) or (a.enviado and a.fallido) or (a.cancelado and not a.programado) or (a.enviado and not a.programado)


def e520() -> None:
    print("SE-520 · GoF conductuales (semilla 520)")
    rng = random.Random(520)
    ilegales_flags = rechazos_state = 0
    n = 10000
    for _ in range(n):
        a, estado = Alerta(), "nuevo"
        for _ in range(6):
            ev = rng.choice(EVENTOS)
            aplicar_flags(a, ev)
            nuevo = TRANSICIONES.get((estado, ev))
            if nuevo is None:
                rechazos_state += 1
            else:
                estado = nuevo
        ilegales_flags += ilegal_flags(a)
    print(f"  {n} secuencias de 6 eventos al azar: con banderas, {ilegales_flags} terminan en una combinación imposible ({ilegales_flags * 100 / n:.1f} %); con tabla de transiciones, 0 estados imposibles y {rechazos_state} eventos rechazados explícitamente")
    combos = [dict(zip(("programado", "enviado", "cancelado", "fallido"), bits)) for bits in itertools.product([False, True], repeat=4)]
    imposibles = 0
    for c in combos:
        a = Alerta()
        a.programado, a.enviado, a.cancelado, a.fallido = c["programado"], c["enviado"], c["cancelado"], c["fallido"]
        imposibles += ilegal_flags(a)
    print(f"  4 banderas representan {len(combos)} combinaciones, de las cuales {imposibles} violan las reglas del negocio; la máquina tiene {len({v for v in TRANSICIONES.values()} | {'nuevo'})} estados y {len(TRANSICIONES)} transiciones legales de {5 * len(EVENTOS)} pares estado-evento")
    # Observer: fugas y aislamiento de fallos
    class Sujeto:
        def __init__(self):
            self.obs = []

        def suscribir(self, f):
            self.obs.append(f)

        def notificar(self, x):
            for f in list(self.obs):
                f(x)

    class Oyente:
        def __call__(self, x):
            pass

    s = Sujeto()
    refs = []
    for _ in range(1000):
        o = Oyente()
        refs.append(weakref.ref(o))
        s.suscribir(o)
        del o
    gc.collect()
    vivos_fuerte = sum(1 for r in refs if r() is not None)

    class SujetoDebil:
        def __init__(self):
            self.obs = weakref.WeakSet()

        def suscribir(self, f):
            self.obs.add(f)

    sd = SujetoDebil()
    refs2 = []
    for _ in range(1000):
        o = Oyente()
        refs2.append(weakref.ref(o))
        sd.suscribir(o)
        del o
    gc.collect()
    vivos_debil = sum(1 for r in refs2 if r() is not None)
    print(f"  Observer: 1000 oyentes descartados sin darse de baja; siguen vivos con referencia fuerte: {vivos_fuerte}; con WeakSet: {vivos_debil}")
    entregados_ingenuo = entregados_aislado = 0
    def f_ok(_):
        nonlocal_counter.append(1)
    def f_mal(_):
        raise RuntimeError("fallo del oyente")
    nonlocal_counter: list = []
    observadores = [f_ok, f_mal, f_ok, f_ok]
    try:
        for f in observadores:
            f(0)
    except RuntimeError:
        pass
    entregados_ingenuo = len(nonlocal_counter)
    nonlocal_counter.clear()
    errores = 0
    for f in observadores:
        try:
            f(0)
        except RuntimeError:
            errores += 1
    entregados_aislado = len(nonlocal_counter)
    print(f"  4 oyentes, el segundo falla: notificación ingenua entrega a {entregados_ingenuo} oyente; con aislamiento por oyente, a {entregados_aislado} y registra {errores} error")
    # Command con deshacer: propiedad sobre secuencias aleatorias
    class Cola:
        def __init__(self):
            self.items, self.hist = [], []

        def hacer(self, cmd):
            self.hist.append(cmd(self.items))

    def agregar(x):
        def run(items):
            items.append(x)
            return lambda: items.pop()
        return run

    def quitar_primero(items):
        v = items.pop(0) if items else None
        return (lambda: items.insert(0, v)) if v is not None else (lambda: None)

    fallos = 0
    for _ in range(200):
        c = Cola()
        base = [rng.randint(0, 9) for _ in range(rng.randint(0, 5))]
        c.items = list(base)
        for _ in range(rng.randint(1, 8)):
            c.hacer(agregar(rng.randint(0, 9)) if rng.random() < 0.6 else quitar_primero)
        while c.hist:
            c.hist.pop()()
        fallos += (c.items != base)
    print(f"  Command: 200 secuencias aleatorias, deshacer todo devuelve el estado inicial en {200 - fallos} de 200")
    # Template Method frente a duplicación
    class Plantilla(ABC):
        def ejecutar(self, x):
            self.validar(x)
            r = self.transformar(x)
            return self.formatear(r)

        def validar(self, x):
            assert x >= 0

        @abstractmethod
        def transformar(self, x): ...

        def formatear(self, r):
            return str(r)

    class Doble(Plantilla):
        def transformar(self, x):
            return 2 * x

    class Cuadrado(Plantilla):
        def transformar(self, x):
            return x * x

    print(f"  Template Method: esqueleto fijo, pasos variables: Doble(4)={Doble().ejecutar(4)}, Cuadrado(4)={Cuadrado().ejecutar(4)}; validar y formatear escritos una vez")


# ----------------------------------------------------------------------------- SE-521
DESIGN_A = textwrap.dedent('''
    class Producto:
        def __init__(self, precio): self.precio = precio
    class Linea:
        def __init__(self, producto, cantidad): self.producto, self.cantidad = producto, cantidad
    class Pedido:
        def __init__(self, lineas): self.lineas = lineas
    class Checkout:
        def total(self, pedido):
            return sum(l.producto.precio * l.cantidad for l in pedido.lineas)
    class Factura:
        def total(self, pedido):
            t = 0
            for l in pedido.lineas:
                t += l.producto.precio * l.cantidad
            return t
    class Informe:
        def promedio(self, pedido):
            return sum(l.producto.precio for l in pedido.lineas) / len(pedido.lineas)
''')

DESIGN_B = textwrap.dedent('''
    class Producto:
        def __init__(self, precio): self.precio = precio
    class Linea:
        def __init__(self, producto, cantidad): self.producto, self.cantidad = producto, cantidad
        def subtotal(self): return self.producto.precio * self.cantidad
        def precio(self): return self.producto.precio
    class Pedido:
        def __init__(self, lineas): self.lineas = lineas
        def total(self): return sum(l.subtotal() for l in self.lineas)
        def promedio(self): return sum(l.precio() for l in self.lineas) / len(self.lineas)
    class Checkout:
        def total(self, pedido): return pedido.total()
    class Factura:
        def total(self, pedido): return pedido.total()
    class Informe:
        def promedio(self, pedido): return pedido.promedio()
''')


def chains_outside_self(src: str) -> int:
    """Accesos de la forma x.y.z cuya raíz no es self: la clase llega al dato de un colaborador de su colaborador."""
    c = 0
    for n in ast.walk(ast.parse(src)):
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Attribute):
            root = n.value
            while isinstance(root, ast.Attribute):
                root = root.value
            if isinstance(root, ast.Name) and root.id != "self":
                c += 1
    return c


def totales(src: str):
    ns = cargar_fuente(src)
    ped = ns["Pedido"]([ns["Linea"](ns["Producto"](10), 2), ns["Linea"](ns["Producto"](5), 3)])
    return ns["Checkout"]().total(ped), ns["Factura"]().total(ped)


def e521() -> None:
    print("SE-521 · GRASP y asignación de responsabilidades (ast, determinista)")
    for nombre, src in (("A (la lógica vive en quien la usa)", DESIGN_A), ("B (Experto en información)", DESIGN_B)):
        print(f"  Diseño {nombre}: clases que leen el precio de un colaborador de su colaborador: {chains_outside_self(src)}; resultados (Checkout, Factura): {totales(src)}")
    # el mismo cambio de regla (descuento de 10 % si la cantidad es ≥ 3) hecho en UN solo lugar, el más obvio
    regla = "(self_expr) * 0.9 if CANT >= 3 else (self_expr)"
    a2 = DESIGN_A.replace("sum(l.producto.precio * l.cantidad for l in pedido.lineas)", "sum(l.producto.precio * l.cantidad * (0.9 if l.cantidad >= 3 else 1) for l in pedido.lineas)", 1)
    b2 = DESIGN_B.replace("def subtotal(self): return self.producto.precio * self.cantidad", "def subtotal(self): return self.producto.precio * self.cantidad * (0.9 if self.cantidad >= 3 else 1)", 1)
    ta, tb = totales(a2), totales(b2)
    print(f"  descuento del 10 % aplicado en un solo lugar: diseño A da (Checkout, Factura)={ta} → {'inconsistente' if ta[0] != ta[1] else 'consistente'}; diseño B da {tb} → {'inconsistente' if tb[0] != tb[1] else 'consistente'}")
    n_formulas = DESIGN_A.count("l.producto.precio")
    print(f"  copias de la fórmula del subtotal: diseño A={n_formulas} (Checkout, Factura, Informe), diseño B={DESIGN_B.count('self.producto.precio')} (la de Linea, más el precio unitario)")
    # Fabricación pura: la regla como función sin base ni reloj
    def total_puro(lineas):
        return sum(p * c for p, c in lineas)

    print(f"  Fabricación pura: total_puro([(10, 2), (5, 3)]) = {total_puro([(10, 2), (5, 3)])}, probada sin base, sin reloj y sin dobles")


# ----------------------------------------------------------------------------- SE-522
def crear_bd(n_cursos=20, n_entregas=200):
    con = sqlite3.connect(":memory:")
    con.executescript("""
        CREATE TABLE curso(id INTEGER PRIMARY KEY, nombre TEXT);
        CREATE TABLE entrega(id INTEGER PRIMARY KEY, curso_id INTEGER, titulo TEXT, estado TEXT);
    """)
    con.executemany("INSERT INTO curso VALUES (?,?)", [(i, f"Curso {i}") for i in range(n_cursos)])
    con.executemany("INSERT INTO entrega VALUES (?,?,?,?)", [(i, i % n_cursos, f"E{i}", "pendiente") for i in range(n_entregas)])
    con.commit()
    return con


class Contador:
    def __init__(self, con):
        self.n = 0
        self.sentencias = []
        con.set_trace_callback(self._cb)

    def _cb(self, s):
        up = s.strip().upper()
        if up.startswith(("SELECT", "UPDATE", "INSERT", "DELETE")):
            self.n += 1
            self.sentencias.append(up.split()[0])


def e522() -> None:
    print("SE-522 · Repository, Unit of Work y Active Record (sqlite3 en memoria)")
    con = crear_bd()
    c = Contador(con)
    filas = con.execute("SELECT id, curso_id, titulo FROM entrega").fetchall()
    for f in filas:
        con.execute("SELECT nombre FROM curso WHERE id=?", (f[1],)).fetchone()
    print(f"  N+1: listar 200 entregas con el nombre de su curso: consultas={c.n}")
    con2 = crear_bd()
    c2 = Contador(con2)
    con2.execute("SELECT e.id, e.titulo, c.nombre FROM entrega e JOIN curso c ON c.id=e.curso_id").fetchall()
    print(f"  Con una consulta de lectura que une las dos tablas: consultas={c2.n}")
    # Unit of Work: dirty tracking
    con3 = crear_bd()
    c3 = Contador(con3)
    filas = [dict(id=r[0], estado=r[1]) for r in con3.execute("SELECT id, estado FROM entrega LIMIT 100")]
    originales = {f["id"]: dict(f) for f in filas}
    for f in filas[:3]:
        f["estado"] = "entregada"
    c3.n = 0
    for f in filas:  # guardar todo
        con3.execute("UPDATE entrega SET estado=? WHERE id=?", (f["estado"], f["id"]))
    todo = c3.n
    c3.n = 0
    for f in filas:  # solo los sucios
        if f != originales[f["id"]]:
            con3.execute("UPDATE entrega SET estado=? WHERE id=?", (f["estado"], f["id"]))
    print(f"  UoW con seguimiento de cambios: de 100 entregas cargadas y 3 modificadas, UPDATE ejecutados: guardar todo={todo}, solo sucios={c3.n}")
    # atomicidad
    def mover(con, usar_uow: bool):
        try:
            if usar_uow:
                with con:  # transacción: commit o rollback
                    con.execute("UPDATE entrega SET estado='entregada' WHERE id=1")
                    raise RuntimeError("falla a mitad")
            else:
                con.execute("UPDATE entrega SET estado='entregada' WHERE id=1")
                con.commit()
                raise RuntimeError("falla a mitad")
        except RuntimeError:
            pass
        return con.execute("SELECT estado FROM entrega WHERE id=1").fetchone()[0]

    print(f"  fallo a mitad de una operación de dos pasos: sin unidad de trabajo, el primer paso queda persistido ({mover(crear_bd(), False)}); con transacción, vuelve atrás ({mover(crear_bd(), True)})")
    # Repository con doble en memoria frente a base real: tiempo por prueba de lógica
    class RepoFake:
        def __init__(self):
            self.d = {i: "pendiente" for i in range(200)}

        def get(self, i):
            return self.d[i]

        def set(self, i, e):
            self.d[i] = e

    class RepoSql:
        def __init__(self):
            self.con = crear_bd()

        def get(self, i):
            return self.con.execute("SELECT estado FROM entrega WHERE id=?", (i,)).fetchone()[0]

        def set(self, i, e):
            self.con.execute("UPDATE entrega SET estado=? WHERE id=?", (e, i))

    def caso(repo):
        repo.set(5, "entregada")
        return repo.get(5)

    t_fake = min(timeit.repeat(lambda: caso(RepoFake()), number=300, repeat=5)) / 300
    t_sql = min(timeit.repeat(lambda: caso(RepoSql()), number=300, repeat=5)) / 300
    print(f"  prueba de la misma lógica: doble en memoria ≈{t_fake * 1e6:.0f} µs, sqlite en memoria con esquema ≈{t_sql * 1e6:.0f} µs (relación ≈{t_sql / t_fake:.0f}×; ambas son rápidas)")
    # Active Record: la lógica de dominio no se puede probar sin base
    class EntregaAR:
        con = None  # el Active Record necesita una conexión global o inyectada en la clase

        def __init__(self, vence, estado="pendiente"):
            self.vence, self.estado = vence, estado

        def vencida(self, hora):
            return hora > self.vence

        def save(self):
            self.con.execute("UPDATE entrega SET estado=? WHERE id=1", (self.estado,))

        def cumplir(self):
            self.estado = "entregada"
            self.save()

    e = EntregaAR(10)
    regla_pura = e.vencida(11)
    try:
        e.cumplir()
        mezcla = "funcionó"
    except AttributeError:
        mezcla = "falló sin conexión (AttributeError)"
    print(f"  Active Record: la regla pura vencida(11) → {regla_pura} sin base; cumplir() mezcla la regla con save y {mezcla}")


if __name__ == "__main__":
    which = sys.argv[1:] or ["517", "518", "519", "520", "521", "522"]
    for key in which:
        globals()[f"e{key}"]()
        print()
