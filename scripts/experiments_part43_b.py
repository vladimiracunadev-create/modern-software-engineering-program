"""Experimentos de las clases SE-523 a SE-528 (Parte 43): integración, resiliencia, antipatrones y taller.

Uso: python scripts/experiments_part43_b.py [523|524|525|526|527|528]

No se invoca ningún modelo de lenguaje. Simulaciones con reloj virtual y semilla fija (523, 524, 525),
análisis con `ast` (526, 527, 528) y una medición real de latencia con sockets locales (525).
Los recuentos son deterministas; los tiempos reales varían de equipo en equipo.
"""
from __future__ import annotations

import ast
import heapq
import random
import socket
import statistics
import sys
import textwrap
import threading
import time
import timeit
from collections import Counter, defaultdict

from experiments_part43_a import cargar_fuente, cyclomatic, max_function_cc, node_count


# ----------------------------------------------------------------------------- SE-523
def e523() -> None:
    print("SE-523 · Enterprise Integration Patterns (simulación con semilla 523)")
    rng = random.Random(523)
    n = 1000
    mensajes = [{"id": i, "tipo": rng.choice(["pago", "pago", "pago", "aviso", "baja"]), "monto": rng.randint(1, 50)} for i in range(n)]
    # canal con entrega al menos una vez: 20 % de duplicados y reordenamiento local
    entregados = []
    for m in mensajes:
        entregados.append(m)
        if rng.random() < 0.20:
            entregados.append(m)
    ventana = 6
    for i in range(0, len(entregados), ventana):
        bloque = entregados[i:i + ventana]
        rng.shuffle(bloque)
        entregados[i:i + ventana] = bloque
    verdad = sum(m["monto"] for m in mensajes if m["tipo"] == "pago")
    # sin receptor idempotente
    ingenuo = sum(m["monto"] for m in entregados if m["tipo"] == "pago")
    # con receptor idempotente
    vistos, total = set(), 0
    for m in entregados:
        if m["id"] in vistos:
            continue
        vistos.add(m["id"])
        if m["tipo"] == "pago":
            total += m["monto"]
    print(f"  {len(mensajes)} mensajes, {len(entregados) - len(mensajes)} duplicados entregados: suma real de pagos={verdad}; sin receptor idempotente={ingenuo} (error {ingenuo - verdad}); con receptor idempotente={total}")
    # router por contenido
    rutas = Counter(m["tipo"] for m in mensajes)
    print(f"  Content-Based Router: {dict(sorted(rutas.items()))}")
    # Dead Letter Channel: algunos mensajes fallan siempre (veneno)
    veneno = {m["id"] for m in rng.sample(mensajes, 25)}
    intentos_ilimitados = 0
    cola, dlq, procesados = list(mensajes[:200]), [], 0
    for m in cola:
        intentos = 0
        while True:
            intentos += 1
            intentos_ilimitados += 1
            if m["id"] not in veneno:
                procesados += 1
                break
            if intentos >= 3:
                dlq.append(m["id"])
                break
    en_cola = sum(1 for m in cola if m["id"] in veneno)
    print(f"  Dead Letter Channel con máximo de 3 intentos: de 200 mensajes, {procesados} procesados, {len(dlq)} a la cola de cartas muertas, {intentos_ilimitados} intentos en total; sin tope, cada uno de los {en_cola} mensajes veneno exigiría reintentos sin fin")
    # Resequencer: inversiones antes y después
    def inversiones(seq):
        c = 0
        for i in range(len(seq)):
            for j in range(i + 1, len(seq)):
                if seq[i] > seq[j]:
                    c += 1
        return c

    ids = [m["id"] for m in entregados if True]
    unicos = []
    vis = set()
    for i in ids:
        if i not in vis:
            vis.add(i)
            unicos.append(i)
    antes = inversiones(unicos)
    siguiente, buffer, salida = 0, {}, []
    for i in unicos:
        buffer[i] = True
        while siguiente in buffer:
            salida.append(siguiente)
            del buffer[siguiente]
            siguiente += 1
    print(f"  Resequencer: pares fuera de orden en la entrada={antes}; en la salida={inversiones(salida[:300])} (primeros 300), buffer máximo pendiente ≤ {ventana}")
    # Correlation: peticiones con respuestas fuera de orden
    resp = {i: f"r{i}" for i in range(20)}
    orden = list(resp)
    rng.shuffle(orden)
    asociadas = sum(1 for i in orden if resp[i] == f"r{i}")
    print(f"  Correlation Identifier: 20 respuestas llegan en orden {orden[:6]}…; asociadas correctamente por id: {asociadas} de 20; asociadas por posición: {sum(1 for pos, i in enumerate(orden) if pos == i)} de 20")


# ----------------------------------------------------------------------------- SE-524
def simular_reintentos(estrategia: str, clientes=1000, capacidad=60, seed=524):
    """Un servicio que falla hasta t=1000 ms y luego acepta `capacidad` peticiones por cada 100 ms."""
    rng = random.Random(seed)
    base, tope, max_int = 100.0, 6400.0, 12
    eventos = [(0.0, i, 0) for i in range(clientes)]
    heapq.heapify(eventos)
    por_cubeta = Counter()
    aceptadas_en = Counter()
    pendientes_final = 0
    intentos_total = 0
    t_fin = 0.0
    while eventos:
        t, c, k = heapq.heappop(eventos)
        cub = int(t // 100)
        por_cubeta[cub] += 1
        intentos_total += 1
        ok = t >= 1000 and aceptadas_en[cub] < capacidad
        if ok:
            aceptadas_en[cub] += 1
            t_fin = max(t_fin, t)
            continue
        if k + 1 >= max_int:
            pendientes_final += 1
            continue
        tecnica = min(tope, base * 2 ** k)
        if estrategia == "fijo":
            espera = base
        elif estrategia == "exponencial":
            espera = tecnica
        elif estrategia == "jitter_completo":
            espera = rng.uniform(0, tecnica)
        else:
            espera = tecnica / 2 + rng.uniform(0, tecnica / 2)
        heapq.heappush(eventos, (t + espera, c, k + 1))
    pico = max(v for k, v in por_cubeta.items() if k >= 2)
    return {"intentos": intentos_total, "pico por 100 ms": pico, "fin (ms)": t_fin, "abandonados": pendientes_final}


def e524() -> None:
    print("SE-524 · Resiliencia: timeout, retry con jitter y circuit breaker (simulación con semilla 524)")
    print("  1000 clientes, el servicio vuelve a t=1000 ms y acepta 60 peticiones por cada 100 ms")
    for est in ("fijo", "exponencial", "jitter_completo", "jitter_equilibrado"):
        r = simular_reintentos(est)
        print(f"  {est:>18}: intentos={r['intentos']}, pico de peticiones por 100 ms tras el arranque={r['pico por 100 ms']}, último éxito en {r['fin (ms)']:.0f} ms, abandonados={r['abandonados']}")
    # amplificación por capas
    print("  Amplificación: 3 capas con 3 intentos cada una → intentos al servicio por petición en el peor caso:", 3 ** 3)
    print("  con presupuesto de reintentos (máx. 10 % de las peticiones por capa): 1,1^3 =", round(1.1 ** 3, 3))
    # circuit breaker con reloj virtual
    rng = random.Random(524)

    def run(usar_breaker: bool):
        estado, abierto_hasta, fallos, probando = "cerrado", 0.0, 0, False
        llamadas_al_servicio = rechazadas_rapido = exitos = 0
        t = 0.0
        while t < 20000:  # 20 s a 100 peticiones por segundo
            t += 10
            caido = 5000 <= t < 12000
            if usar_breaker and estado == "abierto":
                if t >= abierto_hasta:
                    estado = "semiabierto"
                else:
                    rechazadas_rapido += 1
                    continue
            llamadas_al_servicio += 1
            ok = not caido
            if usar_breaker:
                if ok:
                    fallos = 0
                    estado = "cerrado"
                else:
                    fallos += 1
                    if estado == "semiabierto" or fallos >= 5:
                        estado, abierto_hasta = "abierto", t + 1000
            exitos += ok
        return llamadas_al_servicio, rechazadas_rapido, exitos

    sin = run(False)
    con = run(True)
    print(f"  Circuit breaker (servicio caído de 5 s a 12 s, 100 peticiones por segundo): sin él, llamadas al servicio={sin[0]}, éxitos={sin[2]}; con él, llamadas={con[0]}, rechazadas al instante={con[1]}, éxitos={con[2]}")
    # timeout: latencia de cola
    lat = [rng.lognormvariate(3.9, 0.9) for _ in range(20000)]
    lat.sort()
    p50, p99, p999 = lat[10000], lat[int(0.99 * 20000)], lat[int(0.999 * 20000)]
    print(f"  Latencia lognormal (semilla fija): p50={p50:.0f} ms, p99={p99:.0f} ms, p99,9={p999:.0f} ms; un timeout de 80 ms corta el {sum(1 for x in lat if x > 80) * 100 / 20000:.1f} % de las llamadas sanas")


# ----------------------------------------------------------------------------- SE-525
def sim_pool(tamanios: dict, seed=525, dur=40.0):
    """Simulación de eventos discretos: dos dependencias A (sana) y B (se degrada de t=10 a t=30).
    `tamanios` mapea dependencia → tamaño del grupo (un grupo compartido usa la clave 'compartido')."""
    rng = random.Random(seed)
    llegadas = []
    t = 0.0
    while t < dur:
        t += rng.expovariate(40.0)
        llegadas.append((t, "A"))
    t = 0.0
    while t < dur:
        t += rng.expovariate(8.0)
        llegadas.append((t, "B"))
    llegadas.sort()
    libres = {k: [0.0] * v for k, v in tamanios.items()}
    ok = Counter()
    tot = Counter()
    for ta, dep in llegadas:
        grupo = "compartido" if "compartido" in tamanios else dep
        lat = rng.lognormvariate(-3.0, 0.3)  # ≈ 50 ms
        if dep == "B" and 10 <= ta < 30:
            lat = 3.0
        heap = libres[grupo]
        libre = heapq.heappop(heap)
        inicio = max(libre, ta)
        espera = inicio - ta
        fin = inicio + lat
        heapq.heappush(heap, fin)
        # la petición vale si todo, espera incluida, termina antes de 0,5 s
        tot[dep] += 1
        if espera + lat <= 0.5:
            ok[dep] += 1
    return {d: ok[d] / tot[d] for d in tot}


def e525() -> None:
    print("SE-525 · Resiliencia: bulkhead, sidecar, ambassador y degradación")
    comp = sim_pool({"compartido": 10})
    sepa = sim_pool({"A": 8, "B": 2})
    print(f"  Dependencia B lenta (3 s) entre t=10 y t=30; plazo de 0,5 s; solicitudes A 40/s y B 8/s")
    print(f"  grupo compartido de 10 hilos: éxito de A={comp['A'] * 100:.1f} %, de B={comp['B'] * 100:.1f} %")
    print(f"  bulkhead 8 para A y 2 para B:  éxito de A={sepa['A'] * 100:.1f} %, de B={sepa['B'] * 100:.1f} %")
    # degradación: respuesta útil con caché obsoleta
    rng = random.Random(525)
    util_sin = util_con = 0
    n = 2000
    for i in range(n):
        b_ok = not (800 <= i < 1600)
        util_sin += b_ok
        hay_cache = rng.random() < 0.7
        util_con += b_ok or hay_cache
    print(f"  Degradación con caché obsoleta (70 % de aciertos) durante una caída del 40 % del tiempo: respuestas útiles sin degradar={util_sin * 100 / n:.1f} %, con degradación={util_con * 100 / n:.1f} %")
    # sidecar/ambassador: sobrecoste real de un salto adicional por sockets locales
    print("  Sobrecoste de un salto adicional (ambassador): medición real con sockets locales")
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))
    srv.listen()
    puerto_srv = srv.getsockname()[1]
    stop = threading.Event()

    def eco():
        srv.settimeout(0.2)
        while not stop.is_set():
            try:
                c, _ = srv.accept()
            except OSError:
                continue
            threading.Thread(target=atender, args=(c,), daemon=True).start()

    def atender(c):
        with c:
            while True:
                d = c.recv(64)
                if not d:
                    return
                c.sendall(d)

    prx = socket.socket()
    prx.bind(("127.0.0.1", 0))
    prx.listen()
    puerto_prx = prx.getsockname()[1]

    def proxy():
        prx.settimeout(0.2)
        while not stop.is_set():
            try:
                c, _ = prx.accept()
            except OSError:
                continue
            up = socket.create_connection(("127.0.0.1", puerto_srv))
            threading.Thread(target=puente, args=(c, up), daemon=True).start()

    def puente(c, up):
        with c, up:
            while True:
                d = c.recv(64)
                if not d:
                    return
                up.sendall(d)
                c.sendall(up.recv(64))

    threading.Thread(target=eco, daemon=True).start()
    threading.Thread(target=proxy, daemon=True).start()

    def medir(puerto, n=2000):
        s = socket.create_connection(("127.0.0.1", puerto))
        s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        for _ in range(100):
            s.sendall(b"x")
            s.recv(64)
        t = []
        for _ in range(n):
            a = time.perf_counter()
            s.sendall(b"x")
            s.recv(64)
            t.append(time.perf_counter() - a)
        s.close()
        return statistics.median(t) * 1e6

    directo = medir(puerto_srv)
    via = medir(puerto_prx)
    stop.set()
    print(f"  mediana por petición-respuesta: directa ≈{directo:.0f} µs, con un salto intermedio ≈{via:.0f} µs (≈{via / directo:.1f}×); orden de magnitud, varía por equipo")


# ----------------------------------------------------------------------------- SE-526
GOD = textwrap.dedent('''
    class Servicio:
        def __init__(self, db, mail, sms, cache, log, cfg, clock, queue):
            self.db, self.mail, self.sms, self.cache, self.log = db, mail, sms, cache, log
            self.cfg, self.clock, self.queue = cfg, clock, queue
            self.cuenta = 0
            self.errores = []
        def crear(self, a, b, c, d, e, f):
            if a and b or c:
                self.db.insert(a, b)
                self.cuenta += 1
            else:
                self.errores.append(a)
        def enviar_mail(self, x):
            self.mail.send(x); self.log.info(x)
        def enviar_sms(self, x):
            self.sms.send(x); self.log.info(x)
        def reportar(self):
            return self.cuenta, len(self.errores)
        def limpiar_cache(self):
            self.cache.clear()
        def horario(self):
            return self.clock.now() > self.cfg.hora
        def encolar(self, x):
            self.queue.put(x)
        def migrar(self):
            for r in self.db.all():
                if r.viejo:
                    self.db.update(r)
        def exportar(self):
            return [r for r in self.db.all()]
        def importar(self, filas):
            for f in filas:
                self.db.insert(f, f)
''')

SPLIT = textwrap.dedent('''
    class Registro:
        def __init__(self, db):
            self.db = db
            self.cuenta = 0
            self.errores = []
        def crear(self, a, b, c):
            if a and b or c:
                self.db.insert(a, b)
                self.cuenta += 1
            else:
                self.errores.append(a)
        def reportar(self):
            return self.cuenta, len(self.errores)
    class Notificador:
        def __init__(self, mail, sms, log):
            self.mail, self.sms, self.log = mail, sms, log
        def enviar_mail(self, x):
            self.mail.send(x); self.log.info(x)
        def enviar_sms(self, x):
            self.sms.send(x); self.log.info(x)
    class Migracion:
        def __init__(self, db):
            self.db = db
        def migrar(self):
            for r in self.db.all():
                if r.viejo:
                    self.db.update(r)
        def exportar(self):
            return [r for r in self.db.all()]
        def importar(self, filas):
            for f in filas:
                self.db.insert(f, f)
''')


def metricas_clase(src: str):
    out = []
    for c in [n for n in ast.parse(src).body if isinstance(n, ast.ClassDef)]:
        metodos = [m for m in c.body if isinstance(m, ast.FunctionDef) and m.name != "__init__"]
        attrs = {m.name: set() for m in metodos}
        for m in metodos:
            for n in ast.walk(m):
                if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id == "self":
                    attrs[m.name].add(n.attr)
        pares = [(a, b) for i, a in enumerate(metodos) for b in metodos[i + 1:]]
        sin_compartir = sum(1 for a, b in pares if not (attrs[a.name] & attrs[b.name]))
        init = next((m for m in c.body if isinstance(m, ast.FunctionDef) and m.name == "__init__"), None)
        deps = len(init.args.args) - 1 if init else 0
        out.append((c.name, len(metodos), deps, sin_compartir, len(pares)))
    return out


def ciclos(grafo: dict):
    """Componentes fuertemente conexos de tamaño > 1 (Tarjan)."""
    idx, low, pila, en, res, cont = {}, {}, [], set(), [], [0]

    def fuerte(v):
        idx[v] = low[v] = cont[0]
        cont[0] += 1
        pila.append(v)
        en.add(v)
        for w in grafo.get(v, ()):
            if w not in idx:
                fuerte(w)
                low[v] = min(low[v], low[w])
            elif w in en:
                low[v] = min(low[v], idx[w])
        if low[v] == idx[v]:
            comp = []
            while True:
                w = pila.pop()
                en.discard(w)
                comp.append(w)
                if w == v:
                    break
            if len(comp) > 1:
                res.append(sorted(comp))

    for v in list(grafo):
        if v not in idx:
            fuerte(v)
    return res


def e526() -> None:
    print("SE-526 · Antipatrones y deuda de diseño (ast, determinista)")
    print("  clase | métodos | dependencias en el constructor | pares de métodos que no comparten estado | pares")
    for nombre, src in (("antes", GOD), ("después", SPLIT)):
        for fila in metricas_clase(src):
            print(f"  [{nombre}] {fila[0]} | {fila[1]} | {fila[2]} | {fila[3]} | {fila[4]}")
    print(f"  complejidad ciclomática máxima por función: antes={max_function_cc(GOD)}, después={max_function_cc(SPLIT)}")
    g1 = {"avisos": {"cursos", "usuarios"}, "cursos": {"usuarios", "avisos"}, "usuarios": {"cursos"}, "reportes": {"avisos"}}
    g2 = {"avisos": {"dominio"}, "cursos": {"dominio"}, "usuarios": {"dominio"}, "reportes": {"avisos"}, "dominio": set()}
    print(f"  dependencias cíclicas entre módulos: antes={ciclos(g1)}, después={ciclos(g2)}")
    # interés de la deuda: costo de cambio simulado a medida que se acumulan atajos
    rng = random.Random(526)
    costos = []
    deuda = 0
    for cambio in range(1, 11):
        base = 4
        costos.append(round(base + deuda * rng.uniform(0.8, 1.2), 1))
        if cambio % 2 == 0:
            deuda += 1.5  # un atajo cada dos cambios
    print(f"  Modelo ilustrativo del interés de la deuda (supuesto, no medición): horas por cambio sin pagar la deuda={costos}")
    pagado = []
    deuda = 0
    for cambio in range(1, 11):
        pagado.append(round(4 + deuda * rng.uniform(0.8, 1.2) + (6 if cambio == 5 else 0), 1))
        if cambio % 2 == 0 and cambio != 6:
            deuda += 1.5
        if cambio == 5:
            deuda = 0
    print(f"  con un pago de 6 horas en el cambio 5: {pagado}; acumulado sin pagar={sum(costos):.1f} h, pagando={sum(pagado):.1f} h")


# ----------------------------------------------------------------------------- SE-527
LEGACY = textwrap.dedent('''
    def precio_aviso(canal, urgente, horas, adjuntos, grupo):
        if canal == "email":
            if urgente:
                base = 3
            else:
                base = 1
            if adjuntos > 2:
                base += 2
        elif canal == "sms":
            if urgente:
                base = 9
            else:
                base = 5
            if horas > 20 and horas < 24:
                base += 1
        elif canal == "push":
            base = 0
            if urgente and grupo > 100:
                base = 2
        elif canal == "voz":
            base = 20
            if urgente:
                base = 30
            if grupo > 50:
                base = base * 2
        else:
            raise ValueError(canal)
        if grupo > 1000:
            base = base * 0.5
        return base
''')

REFACT = textwrap.dedent('''
    from abc import ABC, abstractmethod
    class Tarifa(ABC):
        @abstractmethod
        def base(self, urgente, horas, adjuntos, grupo): ...
    class Email(Tarifa):
        def base(self, urgente, horas, adjuntos, grupo):
            base = 3 if urgente else 1
            return base + 2 if adjuntos > 2 else base
    class Sms(Tarifa):
        def base(self, urgente, horas, adjuntos, grupo):
            base = 9 if urgente else 5
            return base + 1 if 20 < horas < 24 else base
    class Push(Tarifa):
        def base(self, urgente, horas, adjuntos, grupo):
            return 2 if urgente and grupo > 100 else 0
    class Voz(Tarifa):
        def base(self, urgente, horas, adjuntos, grupo):
            base = 30 if urgente else 20
            return base * 2 if grupo > 50 else base
    TARIFAS = {"email": Email(), "sms": Sms(), "push": Push(), "voz": Voz()}
    def precio_aviso(canal, urgente, horas, adjuntos, grupo):
        try:
            tarifa = TARIFAS[canal]
        except KeyError:
            raise ValueError(canal)
        base = tarifa.base(urgente, horas, adjuntos, grupo)
        return base * 0.5 if grupo > 1000 else base
''')


def _cargar(src: str):
    ns = cargar_fuente(src)
    return ns["precio_aviso"]


def e527() -> None:
    print("SE-527 · Taller: refactorizar con patrones y medir su costo (ast, semilla 527)")
    rng = random.Random(527)
    casos = [(rng.choice(["email", "sms", "push", "voz"]), rng.random() < 0.5, rng.randint(0, 48), rng.randint(0, 5), rng.choice([1, 10, 60, 150, 1200]))
             for _ in range(5000)]
    legacy = _cargar(LEGACY)
    maestro = [legacy(*c) for c in casos]
    nuevo = _cargar(REFACT)
    dif = sum(1 for c, m in zip(casos, maestro) if nuevo(*c) != m)
    print(f"  Maestro dorado: {len(casos)} entradas con semilla fija registradas del código antiguo; el refactor difiere en {dif}")
    print(f"  complejidad ciclomática máxima por función: antes={max_function_cc(LEGACY)}, después={max_function_cc(REFACT)}; nodos de sintaxis: antes={node_count(LEGACY)}, después={node_count(REFACT)}")
    # mutantes del refactor: ¿los detecta el maestro dorado?
    mutaciones = [
        ("Email: umbral de adjuntos > 2 → > 3", "adjuntos > 2", "adjuntos > 3"),
        ("Sms: ventana 20 < horas < 24 → 20 <= horas < 24", "20 < horas < 24", "20 <= horas < 24"),
        ("Push: grupo > 100 → grupo > 101", "grupo > 100", "grupo > 101"),
        ("Voz: grupo > 50 → grupo > 51", "grupo > 50 else", "grupo > 51 else"),
        ("Descuento: grupo > 1000 → >= 1000", "grupo > 1000 else", "grupo >= 1000 else"),
        ("Voz urgente 30 → 31", "30 if urgente", "31 if urgente"),
    ]
    muertos = 0
    for nombre, a, b in mutaciones:
        assert a in REFACT, a
        f = _cargar(REFACT.replace(a, b, 1))
        mata = any(f(*c) != m for c, m in zip(casos, maestro))
        muertos += mata
        print(f"    mutante «{nombre}»: {'detectado' if mata else 'sobrevive'}")
    print(f"  mutantes detectados por el maestro dorado aleatorio: {muertos} de {len(mutaciones)}")
    frontera = [(c, u, h, a, g) for c in ("email", "sms", "push", "voz") for u in (False, True) for h in (20, 21, 23, 24) for a in (2, 3) for g in (50, 51, 100, 101, 1000, 1001)]
    maestro2 = maestro + [legacy(*c) for c in frontera]
    casos2 = casos + frontera
    muertos2 = 0
    for nombre, a, b in mutaciones:
        f = _cargar(REFACT.replace(a, b, 1))
        muertos2 += any(f(*c) != m for c, m in zip(casos2, maestro2))
    print(f"  maestro dorado ampliado con {len(frontera)} entradas de frontera: detecta {muertos2} de {len(mutaciones)}; el refactor sigue difiriendo en {sum(1 for c, m in zip(casos2, maestro2) if nuevo(*c) != m)}")
    # el maestro con pocas entradas: cuántos mutantes se detectan con 30 casos
    pocos = casos[:30]
    muertos30 = 0
    for nombre, a, b in mutaciones:
        f = _cargar(REFACT.replace(a, b, 1))
        muertos30 += any(f(*c) != legacy(*c) for c in pocos)
    print(f"  con solo 30 de las 5000 entradas, detecta {muertos30} de {len(mutaciones)}")
    t1 = min(timeit.repeat(lambda: [legacy(*c) for c in casos[:500]], number=20, repeat=5)) / 20 / 500
    t2 = min(timeit.repeat(lambda: [nuevo(*c) for c in casos[:500]], number=20, repeat=5)) / 20 / 500
    print(f"  tiempo por llamada: antes ≈{t1 * 1e9:.0f} ns, después ≈{t2 * 1e9:.0f} ns (relación ≈{t2 / t1:.1f}×)")
    # coste de añadir un canal nuevo
    nl = chr(10)
    viejo = f"    else:{nl}        raise ValueError(canal)"
    nuevo_txt = f"    elif canal == 'wa':{nl}        base = 4{nl}    else:{nl}        raise ValueError(canal)"
    legacy2 = LEGACY.replace(viejo, nuevo_txt)
    assert legacy2 != LEGACY
    print(f"  añadir un canal: complejidad máxima antes→{max_function_cc(legacy2)} (+{max_function_cc(legacy2) - max_function_cc(LEGACY)}); después: una clase nueva y una línea de registro; las funciones existentes no cambian")


# ----------------------------------------------------------------------------- SE-528
CORPUS = {
    "Reales con nombre ajeno al patrón": [
        ("""
from abc import ABC, abstractmethod
class Reglamento(ABC):
    @abstractmethod
    def cobrar(self, x): ...
class PorMinuto(Reglamento):
    def cobrar(self, x): return x * 2
class PorDia(Reglamento):
    def cobrar(self, x): return x * 40
class Caja:
    def __init__(self, r: Reglamento): self.r = r
    def total(self, x): return self.r.cobrar(x)
""", True),
        ("""
class Boletin:
    def __init__(self): self.oyentes = []
    def suscribir(self, f): self.oyentes.append(f)
    def publicar(self, x):
        for f in self.oyentes: f(x)
""", True),
        ("""
class Sender:
    def send(self, x): return x
class Reintentos(Sender):
    def __init__(self, interno: Sender): self.interno = interno
    def send(self, x): return self.interno.send(x)
""", True),
        ("""
class Unico:
    _i = None
    def __new__(cls):
        if cls._i is None: cls._i = super().__new__(cls)
        return cls._i
""", True),
    ],
    "Reales con nombre del patrón": [
        ("""
from abc import ABC, abstractmethod
class DescuentoStrategy(ABC):
    @abstractmethod
    def aplicar(self, x): ...
class Mitad(DescuentoStrategy):
    def aplicar(self, x): return x / 2
class Nada(DescuentoStrategy):
    def aplicar(self, x): return x
""", True),
        ("""
class A: pass
class B: pass
REGISTRO = {"a": A, "b": B}
def crear(clave): return REGISTRO[clave]()
class ClienteFactory: pass
""", True),
    ],
    "Reales que ninguna regla reconoce": [
        ("""
class Bus:
    def __init__(self): self.por_tipo = {}
    def on(self, tipo, f): self.por_tipo.setdefault(tipo, []).append(f)
    def emit(self, tipo, x):
        for f in self.por_tipo.get(tipo, []): f(x)
""", True),
        ("""
REGLAS = {"mitad": lambda x: x / 2, "nada": lambda x: x}
def aplicar(nombre, x): return REGLAS[nombre](x)
""", True),
    ],
    "Nombre de patrón sin la estructura": [
        ("""
class StrategyHelper:
    def run(self, x): return x + 1
""", False),
        ("""
class ObserverUtils:
    @staticmethod
    def limpiar(s): return s.strip()
""", False),
        ("""
class LoggerDecorator:
    pass
""", False),
        ("""
class ConnectionFactory:
    def __init__(self): self.n = 0
    def increment(self): self.n += 1
""", False),
        ("""
class SingletonConfig:
    def __init__(self, d): self.d = d
""", False),
    ],
    "Estructura parecida que no es el patrón": [
        ("""
class Acumulador:
    def __init__(self): self.items = []
    def agregar(self, x): self.items.append(x)
    def total(self):
        s = 0
        for x in self.items: s += x
        return s
""", False),
    ],
}

PATRON_POR_NOMBRE = ("Strategy", "Observer", "Decorator", "Factory", "Singleton")


def detector_nombre(src: str) -> bool:
    return any(p in c.name for c in ast.walk(ast.parse(src)) if isinstance(c, ast.ClassDef) for p in PATRON_POR_NOMBRE)


def detector_estructura(src: str) -> bool:
    tree = ast.parse(src)
    clases = {c.name: c for c in tree.body if isinstance(c, ast.ClassDef)}
    # estrategia: clase abstracta con >= 2 subclases y alguien que recibe un objeto del tipo abstracto
    for c in clases.values():
        abstractos = any(isinstance(m, ast.FunctionDef) and any(isinstance(d, ast.Name) and d.id == "abstractmethod" for d in m.decorator_list) for m in c.body)
        subs = [x for x in clases.values() if any(isinstance(b, ast.Name) and b.id == c.name for b in x.bases)]
        if abstractos and len(subs) >= 2:
            return True
        # decorador: subclase que guarda una instancia de su propia base y delega
        for s in subs:
            init = next((m for m in s.body if isinstance(m, ast.FunctionDef) and m.name == "__init__"), None)
            if init and any(isinstance(a.annotation, ast.Name) and a.annotation.id == c.name for a in init.args.args[1:]):
                return True
    # observador: lista de llamables, un método que añade y un método que recorre la lista invocándolos
    for c in clases.values():
        listas = {t.attr for n in ast.walk(c) if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Attribute) and isinstance(n.value, ast.List)}
        agrega = any(isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "append" and isinstance(n.func.value, ast.Attribute) and n.func.value.attr in listas for n in ast.walk(c))
        recorre = any(isinstance(n, ast.For) and isinstance(n.iter, ast.Attribute) and n.iter.attr in listas for n in ast.walk(c))
        if listas and agrega and recorre:
            return True
    # fábrica: diccionario de clases y una función que lo indexa y llama
    nombres = set(clases)
    for n in tree.body:
        if isinstance(n, ast.Assign) and isinstance(n.value, ast.Dict) and n.value.values and all(isinstance(v, ast.Name) and v.id in nombres for v in n.value.values):
            return True
    # singleton: __new__ que consulta un atributo de clase
    for c in clases.values():
        if any(isinstance(m, ast.FunctionDef) and m.name == "__new__" for m in c.body):
            return True
    return False


def evaluar(detector):
    tp = fp = fn = tn = 0
    for _, lista in CORPUS.items():
        for src, real in lista:
            pred = detector(src)
            tp += pred and real
            fp += pred and not real
            fn += (not pred) and real
            tn += (not pred) and not real
    p = tp / (tp + fp) if tp + fp else 0
    r = tp / (tp + fn) if tp + fn else 0
    return tp, fp, fn, tn, p, r


def e528() -> None:
    print("SE-528 · Proyecto: catálogo de patrones de un sistema real (corpus sintético etiquetado)")
    total = sum(len(v) for v in CORPUS.values())
    real = sum(1 for v in CORPUS.values() for _, r in v if r)
    print(f"  corpus de {total} fragmentos escritos por el autor: {real} con un patrón real y {total - real} sin él; el detector de estructura se escribió conociendo parte del corpus, así que su resultado es optimista")
    for nombre, det in (("por nombre de clase", detector_nombre), ("por estructura (ast)", detector_estructura)):
        tp, fp, fn, tn, p, r = evaluar(det)
        print(f"  detector {nombre}: verdaderos positivos={tp}, falsos positivos={fp}, falsos negativos={fn}, precisión={p * 100:.0f} %, exhaustividad={r * 100:.0f} %")
    # una entrada de catálogo y su validación
    campos = ["nombre", "fuerza que resuelve", "dónde vive", "evidencia", "costo medido", "condición de salida"]
    entradas = [
        {"nombre": "Strategy en tarifas", "fuerza que resuelve": "variantes que crecen", "dónde vive": "tarifas.py", "evidencia": "maestro dorado, 5000 entradas", "costo medido": "nodos +54 %", "condición de salida": "si quedan 2 variantes"},
        {"nombre": "Singleton de configuración", "fuerza que resuelve": "un punto de lectura", "dónde vive": "config.py", "evidencia": "", "costo medido": "", "condición de salida": ""},
        {"nombre": "Circuit breaker", "fuerza que resuelve": "caída de un tercero", "dónde vive": "cliente_pagos.py", "evidencia": "simulación", "costo medido": "", "condición de salida": "si el tercero se retira"},
    ]
    for e in entradas:
        faltan = [c for c in campos if not e.get(c)]
        print(f"  entrada «{e['nombre']}»: campos faltantes={faltan or 'ninguno'}")
    print("  regla del catálogo: una entrada sin evidencia, sin costo o sin condición de salida no se acepta")


if __name__ == "__main__":
    which = sys.argv[1:] or ["523", "524", "525", "526", "527", "528"]
    for key in which:
        globals()[f"e{key}"]()
        print()
