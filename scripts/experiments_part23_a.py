"""Experimentos de la Parte 23, bloque A: WebAssembly, eBPF, aceleradores y sandboxes.

Uso: python scripts/experiments_part23_a.py [wasm|wasi|wasmserver|ebpf|gpu|cost|sandbox]

No se invoca ningún modelo de lenguaje. WebAssembly se ejecuta de verdad con ``wasmtime``
(versión fija en ``experiments_part23_lab``). eBPF se ejecuta de verdad en el núcleo de Linux de
WSL2 mediante ``experiments_part23_ebpf_wsl.py``. No hay GPU utilizable en la máquina de
desarrollo (el controlador informó «GPU is lost»), así que lo que se mide para aceleradores son
proxies de CPU con NumPy y modelos con parámetros del autor; cada salida lo dice.
"""
from __future__ import annotations

import ast
import os
import random
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

import numpy as np

import experiments_part23_lab as L
from experiments_part23_lab import fmt, table, timeit_ms

HERE = Path(__file__).resolve().parent

WAT_CORE = """
(module
  (memory (export "mem") 1 2)
  (func (export "add") (param i32 i32) (result i32) local.get 0 local.get 1 i32.add)
  (func (export "sum") (param $n i32) (result i64)
    (local $i i32) (local $acc i64)
    (block $out (loop $l
      (br_if $out (i32.ge_u (local.get $i) (local.get $n)))
      (local.set $acc (i64.add (local.get $acc) (i64.extend_i32_u (local.get $i))))
      (local.set $i (i32.add (local.get $i) (i32.const 1)))
      (br $l)))
    local.get $acc)
  (func (export "spin") (loop $l (br $l)))
  (func (export "load") (param i32) (result i32) local.get 0 i32.load)
  (func (export "grow") (param i32) (result i32) local.get 0 memory.grow)
  (func (export "counter") (result i32)
    (i32.store (i32.const 0) (i32.add (i32.load (i32.const 0)) (i32.const 1)))
    (i32.load (i32.const 0)))
)
"""


def _razon(exc):
    """Última línea no vacía del mensaje de una trampa de wasmtime (la causa)."""
    lineas = [ln.strip() for ln in str(exc).splitlines() if ln.strip()]
    return lineas[-1][:90] if lineas else type(exc).__name__


def _wasmtime():
    return L.optional("wasmtime", "pip install wasmtime==50.0.1")


# ====================================================================== WebAssembly
def wasm():
    print("WebAssembly: módulo escrito a mano en texto (WAT), compilado y ejecutado con wasmtime")
    wt = _wasmtime()
    if wt is None:
        return
    cfg = wt.Config()
    cfg.consume_fuel = True
    engine = wt.Engine(cfg)
    binary = wt.wat2wasm(WAT_CORE)
    print(f"  tamaño del binario: {len(binary)} bytes; cabecera: {binary[:8].hex()} (0061736d = «\\0asm», versión 1)")
    module = wt.Module(engine, binary)
    store = wt.Store(engine)
    store.set_fuel(10**9)
    inst = wt.Instance(store, module, [])
    ex = inst.exports(store)
    print(f"  add(2, 3) = {ex['add'](store, 2, 3)}; sum(0..999) = {ex['sum'](store, 1000)} (esperado {sum(range(1000))})")

    # La importación define el único canal hacia fuera: este módulo no importa nada.
    print(f"  importaciones declaradas por el módulo: {len(module.imports)}")

    # Trampa por acceso fuera de memoria
    try:
        ex["load"](store, 70000)
        print("  lectura fuera de la memoria: NO falló (inesperado)")
    except wt.Trap as exc:
        print(f"  lectura en la dirección 70000 con 65 536 bytes de memoria: trampa «{_razon(exc)}»")
    # el almacén sigue usable tras la trampa
    print(f"  tras la trampa, add(40, 2) = {ex['add'](store, 40, 2)}")

    # Combustible: bucle infinito detenido
    store.set_fuel(5_000_000)
    t = time.perf_counter()
    try:
        ex["spin"](store)
    except wt.Trap as exc:
        print(f"  bucle infinito con 5 000 000 de unidades de combustible: detenido en {fmt((time.perf_counter() - t) * 1000, 1)} ms ({_razon(exc)})")
    store.set_fuel(10**9)

    # Memoria máxima declarada por el módulo: 2 páginas
    print(f"  memory.grow(1) -> {ex['grow'](store, 1)} (páginas previas); memory.grow(1) -> {ex['grow'](store, 1)} (-1 = negado, tope declarado de 2 páginas)")

    # Límite impuesto por quien incrusta (más estricto que el del módulo)
    store2 = wt.Store(engine)
    store2.set_fuel(10**9)
    store2.set_limits(memory_size=65536)
    inst2 = wt.Instance(store2, module, [])
    print(f"  con set_limits(memory_size=65536): memory.grow(1) -> {inst2.exports(store2)['grow'](store2, 1)}")

    # Rendimiento: sum(0..n) en Wasm, Python puro y NumPy
    n = 5_000_000
    store.set_fuel(10**10)
    w_ms = timeit_ms(lambda: ex["sum"](store, n), repeat=5)

    def py_sum():
        acc = 0
        for i in range(n):
            acc += i
        return acc

    p_ms = timeit_ms(py_sum, repeat=3)
    arr = np.arange(n, dtype=np.int64)
    n_ms = timeit_ms(lambda: int(arr.sum()), repeat=9)
    print(f"  suma de 0..{n - 1}: Wasm {fmt(w_ms, 2)} ms; Python puro {fmt(p_ms, 1)} ms ({fmt(p_ms / w_ms, 1)} veces más lento que Wasm); NumPy {fmt(n_ms, 3)} ms (arreglo ya creado)")
    ok = ex["sum"](store, n) == py_sum() == int(arr.sum())
    print(f"  los tres resultados coinciden: {ok}")


WAT_HELLO = """
(module
  (import "wasi_snapshot_preview1" "fd_write" (func $fd_write (param i32 i32 i32 i32) (result i32)))
  (import "wasi_snapshot_preview1" "path_open"
    (func $path_open (param i32 i32 i32 i32 i32 i64 i64 i32 i32) (result i32)))
  (memory (export "memory") 1)
  (data (i32.const 8) "hola desde wasm\\n")
  (data (i32.const 64) "secreto.txt")
  (func (export "_start")
    (i32.store (i32.const 0) (i32.const 8))
    (i32.store (i32.const 4) (i32.const 16))
    (drop (call $fd_write (i32.const 1) (i32.const 0) (i32.const 1) (i32.const 32))))
  (func (export "abrir") (result i32)
    ;; path_open(dirfd=3, dirflags=0, ruta, longitud=11, oflags=0, derechos=todos, derechos_heredados=0, fdflags=0, &fd)
    (call $path_open (i32.const 3) (i32.const 0) (i32.const 64) (i32.const 11) (i32.const 0)
      (i64.const 536870911) (i64.const 0) (i32.const 0) (i32.const 128)))
)
"""


def wasi():
    print("WASI: el mismo módulo con y sin un directorio concedido (capacidades)")
    wt = _wasmtime()
    if wt is None:
        return
    engine = wt.Engine()
    module = wt.Module(engine, wt.wat2wasm(WAT_HELLO))
    print(f"  importaciones del módulo: {[(i.module, i.name) for i in module.imports]}")

    def run(preopen: Path | None, capture: Path):
        linker = wt.Linker(engine)
        store = wt.Store(engine)
        wc = wt.WasiConfig()
        wc.stdout_file = str(capture)
        if preopen is not None:
            wc.preopen_dir(str(preopen), "/datos")
        store.set_wasi(wc)
        linker.define_wasi()
        inst = linker.instantiate(store, module)
        ex = inst.exports(store)
        ex["_start"](store)
        return ex["abrir"](store)

    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "secreto.txt").write_text("contenido que solo ve quien recibe la capacidad", encoding="utf-8")
        out1 = d / "salida1.txt"
        out2 = d / "salida2.txt"
        e_sin = run(None, out1)
        e_con = run(d, out2)
        print(f"  salida estándar del módulo: {out1.read_text(encoding='utf-8').strip()!r}")
        print(f"  path_open('secreto.txt') sin ningún directorio concedido: errno WASI {e_sin} (8 = EBADF, el descriptor 3 no existe)")
        print(f"  path_open('secreto.txt') con el directorio temporal concedido como /datos: errno WASI {e_con} (0 = abierto)")
        print("  el módulo no puede nombrar rutas fuera del descriptor concedido: no tiene llamada para abrir una ruta absoluta del anfitrión")


def wasmserver():
    print("WebAssembly en servidor: costo de arranque, aislamiento entre peticiones y caché de compilación")
    wt = _wasmtime()
    if wt is None:
        return
    binary = wt.wat2wasm(WAT_CORE)
    engine = wt.Engine()

    t_engine = L.timeit_ms(lambda: wt.Engine(), repeat=15)
    t_compile = L.timeit_ms(lambda: wt.Module(engine, binary), repeat=15)
    module = wt.Module(engine, binary)
    blob = module.serialize()
    t_deser = L.timeit_ms(lambda: wt.Module.deserialize(engine, blob), repeat=15)

    def fresh():
        s = wt.Store(engine)
        i = wt.Instance(s, module, [])
        return i.exports(s)["counter"](s)

    t_inst = L.timeit_ms(fresh, repeat=15, number=20)
    print(f"  crear Engine: {fmt(t_engine, 3)} ms; compilar el módulo desde el binario: {fmt(t_compile, 3)} ms; deserializar el módulo ya compilado ({len(blob)} bytes): {fmt(t_deser, 3)} ms")
    print(f"  instanciar de cero (Store + Instance) y llamar una vez: {fmt(t_inst, 4)} ms por petición")

    # Aislamiento: instancia nueva por petición frente a instancia reutilizada
    s_shared = wt.Store(engine)
    shared = wt.Instance(s_shared, module, []).exports(s_shared)
    reuse = [shared["counter"](s_shared) for _ in range(5)]
    fresh_vals = [fresh() for _ in range(5)]
    print(f"  contador con una instancia reutilizada en 5 peticiones: {reuse} (el estado de una petición se filtra a la siguiente)")
    print(f"  contador con una instancia nueva en cada petición: {fresh_vals} (cada petición parte limpia)")

    # Comparación con arrancar un proceso de Python
    def spawn():
        subprocess.run([sys.executable, "-I", "-c", "pass"], check=True)

    t_spawn = L.timeit_ms(spawn, repeat=5)
    print(f"  arrancar un intérprete de Python vacío como proceso: {fmt(t_spawn, 1)} ms ({fmt(t_spawn / t_inst, 0)} veces el costo de instanciar el módulo; comparación orientativa, no de funciones equivalentes)")

    # Capacidades como importaciones: un módulo que pide una función que el anfitrión no ofrece no se enlaza
    wat_net = '(module (import "host" "enviar_red" (func (param i32))) (func (export "f") (call 0 (i32.const 1))))'
    mod_net = wt.Module(engine, wt.wat2wasm(wat_net))
    linker = wt.Linker(engine)
    store = wt.Store(engine)
    try:
        linker.instantiate(store, mod_net)
        print("  módulo con importación de red sin concederla: se enlazó (inesperado)")
    except Exception as exc:
        print(f"  módulo que importa «host.enviar_red» sin que el anfitrión la defina: no se instancia ({type(exc).__name__}: {str(exc).splitlines()[0][:80]})")
    llamadas = []
    linker.define_func("host", "enviar_red", wt.FuncType([wt.ValType.i32()], []), lambda x: llamadas.append(x))
    inst = linker.instantiate(store, mod_net)
    inst.exports(store)["f"](store)
    print(f"  tras definir la función en el anfitrión, el módulo la llama y el anfitrión la registra: {llamadas}")
    print("  NO EJECUTADO: el modelo de componentes (component model, WIT) no se ejecutó: el paquete de Python de wasmtime 50.0.1 no expone componentes; la sección se apoya en la especificación y en el ejemplo de importaciones anterior.")


# ====================================================================== eBPF
def ebpf():
    print("eBPF: programas reales cargados en el núcleo de Linux de WSL2")
    script = HERE / "experiments_part23_ebpf_wsl.py"
    if sys.platform == "win32":
        drive = script.drive.rstrip(":").lower()
        wsl_path = f"/mnt/{drive}" + script.as_posix()[2:]
        cmd = ["wsl", "-u", "root", "-e", "python3", wsl_path]
    else:
        cmd = [sys.executable, str(script)]
    try:
        res = subprocess.run(cmd, capture_output=True, timeout=120)
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        print(f"  NO EJECUTADO: no se pudo lanzar el experimento ({type(exc).__name__}).")
        return
    text = res.stdout.decode("utf-8", errors="replace").replace("\x00", "")
    for line in text.splitlines():
        print("  " + line)
    if res.returncode != 0:
        print(f"  NO EJECUTADO por completo: código de salida {res.returncode}")
    # Referencia: el mismo contador como función de Python (sin cruzar ninguna frontera)
    contador = {"n": 0}

    def cuenta():
        contador["n"] += 1

    n = 1_000_000
    t = time.perf_counter()
    for _ in range(n):
        cuenta()
    ns = (time.perf_counter() - t) * 1e9 / n
    print(f"  referencia: la misma cuenta como llamada a una función de Python dentro del proceso: {fmt(ns, 0)} ns por llamada (sin leer ningún paquete ni cruzar de espacio de usuario a núcleo)")


# ====================================================================== aceleradores (proxies)
def gpu():
    print("Aceleradores: no hay GPU utilizable aquí; se miden proxies de CPU con NumPy y se modela la divergencia")
    print("  NO EJECUTADO en GPU: el controlador de la GPU del equipo informó «GPU is lost» y no se pudo ejecutar ningún núcleo de cómputo.")
    rng = np.random.default_rng(48)

    # 1. vectorizar frente a bucle (proxy de «muchos datos, una misma operación»)
    n = 2_000_000
    a = rng.random(n, dtype=np.float32)
    b = rng.random(n, dtype=np.float32)
    al = a[:200_000].tolist()
    bl = b[:200_000].tolist()

    def loop():
        return [x * 2.0 + y for x, y in zip(al, bl)]

    t_loop = timeit_ms(loop, repeat=5) * (n / 200_000)  # extrapolado linealmente a n
    t_vec = timeit_ms(lambda: a * 2.0 + b, repeat=15)
    print(f"  a*2+b con {n} elementos float32: bucle de Python ~{fmt(t_loop, 0)} ms (medido con 200 000 y escalado); NumPy vectorizado {fmt(t_vec, 2)} ms; razón ~{fmt(t_loop / t_vec, 0)} veces")

    # 2. patrón de acceso a memoria: contiguo, con paso y aleatorio (proxy de coalescencia)
    m = 1 << 24
    x = rng.random(m, dtype=np.float32)
    idx_cont = np.arange(0, m // 16)
    idx_stride = np.arange(0, m, 16)
    idx_rand = rng.permutation(m)[: m // 16]
    t_c = timeit_ms(lambda: x[idx_cont].sum(), repeat=15)
    t_s = timeit_ms(lambda: x[idx_stride].sum(), repeat=15)
    t_r = timeit_ms(lambda: x[idx_rand].sum(), repeat=15)
    print(f"  sumar {m // 16} elementos de un arreglo de {m} float32 (64 MiB): contiguos {fmt(t_c, 2)} ms; con paso de 16 {fmt(t_s, 2)} ms; en orden aleatorio {fmt(t_r, 2)} ms (razón aleatorio/contiguo {fmt(t_r / t_c, 1)})")

    # 3. intensidad aritmética: operación limitada por memoria frente a limitada por cómputo
    v = rng.random(8_000_000, dtype=np.float32)
    w = rng.random(8_000_000, dtype=np.float32)
    t_axpy = timeit_ms(lambda: v * 1.5 + w, repeat=15)
    gbs = 3 * v.nbytes / 1e9 / (t_axpy / 1000)  # lee v y w, escribe resultado
    print(f"  axpy (2 operaciones por 12 bytes movidos): {fmt(gbs, 1)} GB/s efectivos, {fmt(2 * v.size / 1e6 / t_axpy, 2)} GFLOP/s")
    for size in (256, 1024):
        ma = rng.random((size, size), dtype=np.float32)
        mb = rng.random((size, size), dtype=np.float32)
        t_mm = timeit_ms(lambda: ma @ mb, repeat=7)
        print(f"  multiplicación de matrices {size}x{size} float32: {fmt(2 * size ** 3 / 1e6 / t_mm, 1)} GFLOP/s ({fmt(2 * size ** 3 / (3 * size * size * 4), 0)} operaciones por byte mínimo movido)")

    # 4. divergencia de un warp: modelo con semilla
    random.seed(48)
    warp = 32
    print("  divergencia en un grupo de 32 hilos (modelo: si algún hilo toma el camino A y otro el B, el grupo ejecuta ambos en serie):")
    rows = [["Probabilidad de camino A por hilo", "Veces que el grupo ejecuta ambos caminos", "Costo medio relativo a un solo camino"]]
    for p in (0.0, 0.01, 0.05, 0.5):
        both = 0
        trials = 20000
        for _ in range(trials):
            takes = sum(random.random() < p for _ in range(warp))
            if 0 < takes < warp:
                both += 1
        frac = both / trials
        rows.append([fmt(p, 2), fmt(100 * frac, 1) + " %", fmt(1 + frac, 2) + "x"])
    table(rows)


# ====================================================================== costo y rendimiento
def cost():
    print("Rendimiento y costo: lo que se mide en CPU y un modelo de costo con parámetros del autor")
    print("  NO EJECUTADO en acelerador: no hay GPU utilizable; los precios y velocidades del modelo son supuestos del autor, no tarifas reales.")
    rng = np.random.default_rng(48)

    # throughput y latencia por tamaño de lote en una capa densa
    d = 1024
    wmat = rng.random((d, d), dtype=np.float32)
    print("  capa densa 1024x1024 float32 con lotes de 1 a 256 peticiones (CPU):")
    rows = [["Lote", "Latencia por lote (ms)", "Peticiones por segundo", "Latencia por petición (ms)"]]
    for batch in (1, 4, 16, 64, 256):
        xb = rng.random((batch, d), dtype=np.float32)
        for _ in range(20):
            xb @ wmat  # calentamiento de hilos de BLAS
        t = timeit_ms(lambda: xb @ wmat, repeat=21, number=20)
        rows.append([batch, fmt(t, 3), fmt(batch / (t / 1000), 0), fmt(t / batch, 4)])
    table(rows)

    # float32 frente a float64 y float16 (CPU)
    size = 1024
    for dt in (np.float64, np.float32):
        ma = rng.random((size, size)).astype(dt)
        mb = rng.random((size, size)).astype(dt)
        t = timeit_ms(lambda: ma @ mb, repeat=7)
        print(f"  matmul {size}x{size} {np.dtype(dt).name}: {fmt(t, 1)} ms ({fmt(2 * size ** 3 / 1e6 / t, 1)} GFLOP/s)")
    ma16 = rng.random((256, 256)).astype(np.float16)
    mb16 = rng.random((256, 256)).astype(np.float16)
    ma32 = ma16.astype(np.float32)
    mb32 = mb16.astype(np.float32)
    t16 = timeit_ms(lambda: ma16 @ mb16, repeat=7)
    t32 = timeit_ms(lambda: ma32 @ mb32, repeat=7)
    print(f"  matmul 256x256 float16 {fmt(t16, 2)} ms frente a float32 {fmt(t32, 2)} ms: menor precisión no es más rápido sin soporte de hardware ({fmt(t16 / t32, 1)} veces el tiempo en esta CPU)")

    # Amdahl con transferencia
    print("  Ley de Amdahl con transferencia: parte serie s, aceleración del resto k = 50, costo de mover datos como fracción t del tiempo base:")
    rows = [["Parte serie s", "Costo de transferencia t", "Aceleración total"]]
    for s in (0.05, 0.2):
        for t_ in (0.0, 0.05, 0.2):
            total = s + t_ + (1 - s) / 50
            rows.append([fmt(s, 2), fmt(t_, 2), fmt(1 / total, 1) + "x"])
    table(rows)

    # costo por millón de peticiones según la demanda (precios y capacidades del autor)
    print("  costo por millón de peticiones según la demanda sostenida (supuestos del autor: acelerador 3,00 USD/h y 2 000 peticiones/s por unidad; CPU 0,40 USD/h y 150 peticiones/s por unidad; se compran unidades enteras):")
    rows = [["Demanda (peticiones/s)", "Unidades de acelerador", "USD por millón (acelerador)", "Unidades de CPU", "USD por millón (CPU)", "Más barato"]]
    for demanda in (20, 100, 400, 1000, 2000, 6000):
        n_acc = -(-demanda // 2000)
        n_cpu = -(-demanda // 150)
        c_acc = 3.00 * n_acc / (demanda * 3600) * 1e6
        c_cpu = 0.40 * n_cpu / (demanda * 3600) * 1e6
        rows.append([demanda, n_acc, fmt(c_acc, 2), n_cpu, fmt(c_cpu, 2), "acelerador" if c_acc < c_cpu else "CPU"])
    table(rows)
    print(f"  a plena carga el acelerador cuesta {fmt(3.00 / (2000 * 3600) * 1e6, 2)} USD por millón y la CPU {fmt(0.40 / (150 * 3600) * 1e6, 2)}; con poca demanda se paga la unidad entera aunque esté ociosa y gana la CPU: el cruce depende de la utilización, no solo del precio por hora")


# ====================================================================== sandboxes
def sandbox():
    print("Sandboxes y aislamiento: costos medidos y escapes de un sandbox ingenuo")
    # 1. herencia del entorno por un proceso hijo
    os.environ["PARTE48_VARIABLE_SECRETA"] = "valor-de-ejemplo"
    code = "import os;print(os.environ.get('PARTE48_VARIABLE_SECRETA'))"
    hered = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True).stdout.strip()
    limpio = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True,
                            env={"SYSTEMROOT": os.environ.get("SYSTEMROOT", "")}).stdout.strip()
    print(f"  proceso hijo con el entorno heredado ve la variable: {hered!r}; con un entorno vacío: {limpio!r}")

    # 2. tiempo máximo con terminación del proceso
    t = time.perf_counter()
    try:
        subprocess.run([sys.executable, "-I", "-c", "while True: pass"], timeout=0.5)
    except subprocess.TimeoutExpired:
        print(f"  bucle infinito en un proceso hijo con límite de 0,5 s: terminado a los {fmt((time.perf_counter() - t) * 1000, 0)} ms")
    # 3. el mismo bucle en un hilo no se puede terminar
    stop = threading.Event()

    def spin():
        while not stop.is_set():
            pass

    th = threading.Thread(target=spin, daemon=True)
    th.start()
    th.join(0.3)
    vivo = th.is_alive()
    stop.set()
    th.join(1)
    print(f"  el mismo bucle en un hilo: tras esperar 0,3 s sigue vivo = {vivo}; el hilo no tiene una llamada para matarlo desde fuera, solo cooperar (aquí con un evento)")

    # 4. sandbox ingenuo de Python con exec y __builtins__ vacío
    intento = "resultado = ().__class__.__base__.__subclasses__()"
    ambito = {"__builtins__": {}}
    exec(intento, ambito)  # nosec B102 - experimento didáctico, código fijo y sin entradas externas
    clases = ambito["resultado"]
    print(f"  exec con __builtins__ vacío (sin len, sin open, sin import): el código llega igual a object.__subclasses__() y ve {len(clases)} clases del intérprete, entre ellas clases de módulos con acceso al sistema como {sorted({c.__name__ for c in clases if c.__name__ in ('Popen', '_wrap_close', 'FileIO')})}: un sandbox de lenguaje sin frontera de proceso no es una frontera de seguridad")
    arbol = ast.parse(intento)
    nombres = sorted({n.attr for n in ast.walk(arbol) if isinstance(n, ast.Attribute)})
    print(f"  una lista de nombres prohibidos tendría que anticipar atributos como {nombres}; una lista de lo permitido tiene la misma dificultad con otras rutas")

    # 5. costo de crear cada frontera
    def spawn():
        subprocess.run([sys.executable, "-I", "-c", "pass"], check=True)

    t_proc = timeit_ms(spawn, repeat=5)
    t_thread = timeit_ms(lambda: (lambda th: (th.start(), th.join()))(threading.Thread(target=lambda: None)), repeat=15, number=20)
    wt = L.optional("wasmtime", "pip install wasmtime==50.0.1")
    rows = [["Frontera", "Costo de crear y destruir (ms)"], ["Hilo del mismo proceso", fmt(t_thread, 4)]]
    if wt is not None:
        engine = wt.Engine()
        module = wt.Module(engine, wt.wat2wasm(WAT_CORE))

        def inst():
            s = wt.Store(engine)
            wt.Instance(s, module, [])

        rows.append(["Instancia de WebAssembly (módulo ya compilado)", fmt(timeit_ms(inst, repeat=15, number=20), 4)])
    rows.append(["Proceso nuevo de Python", fmt(t_proc, 1)])
    table(rows)
    print("  NO EJECUTADO: no se midieron contenedores ni microVM (Docker Desktop existe en el equipo pero su arranque mide otra cosa: la capa de WSL2 y no la frontera aislada); las comparaciones de esas capas se apoyan en las fuentes y en el modelo de superficie de la clase.")

    # 6. modelo de superficie de ataque con semilla fija
    random.seed(48)
    print("  modelo con semilla 48: un atacante con una vulnerabilidad en la carga de trabajo necesita encadenar fallos de cada capa; probabilidad de escape con p por capa:")
    rows = [["Capas independientes", "p = 0,10 por capa", "p = 0,02 por capa", "p = 0,02 y dos capas con el mismo fallo (correlación total)"]]
    for k in (1, 2, 3):
        rows.append([k, fmt(0.10 ** k, 4), fmt(0.02 ** k, 6), fmt(0.02 ** max(1, k - 1), 6)])
    table(rows)


TABLE = {"wasm": wasm, "wasi": wasi, "wasmserver": wasmserver, "ebpf": ebpf, "gpu": gpu, "cost": cost, "sandbox": sandbox}

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for key in sys.argv[1:] or list(TABLE):
        TABLE[key]()
        print()
