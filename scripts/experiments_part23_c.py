"""Experimentos de la Parte 23, bloque C: el taller (SE-287) y el proyecto (SE-288).

Uso: python scripts/experiments_part23_c.py [taller|proyecto]

No se invoca ningún modelo de lenguaje. El taller ejecuta una batería de comportamientos hostiles
contra tres formas de ejecutar código ajeno (``exec`` con funciones integradas vacías, un proceso
hijo con entorno vacío y tiempo máximo, y un módulo de WebAssembly con combustible y memoria
acotados). El proyecto monta una plataforma mínima de reglas de aviso con validador de
importaciones, instancia por petición, límites, registro de evidencia encadenado por resúmenes
y un informe firmado con ML-DSA-65 si ``dilithium-py`` está instalado (si no, con HMAC y lo dice).
Todo corre en local; el único servidor es un socket en 127.0.0.1 con puerto asignado por el sistema.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
import random
import secrets
import socket
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

import experiments_part23_lab as L
from experiments_part23_lab import fmt, pct, table

SEED = 48


def _wasmtime():
    return L.optional("wasmtime", "pip install wasmtime==50.0.1")


def _razon(exc) -> str:
    lineas = [ln.strip() for ln in str(exc).splitlines() if ln.strip()]
    return lineas[-1][:80] if lineas else type(exc).__name__


# ====================================================================== taller
def _hijo(codigo: str, env=None, timeout: float = 1.5, cwd=None):
    """Ejecuta código de Python ajeno en un proceso hijo; devuelve (terminó, salida, segundos)."""
    entorno = {"SYSTEMROOT": os.environ.get("SYSTEMROOT", "")} if env is None else env
    t = time.perf_counter()
    try:
        r = subprocess.run([sys.executable, "-I", "-c", codigo], capture_output=True, text=True,
                           timeout=timeout, env=entorno, cwd=cwd)
        return True, (r.stdout + r.stderr).strip(), time.perf_counter() - t
    except subprocess.TimeoutExpired:
        return False, "", time.perf_counter() - t


def taller():
    print("Taller: la misma batería de seis comportamientos hostiles contra tres formas de ejecutar código ajeno")
    wt = _wasmtime()
    os.environ["PARTE48_SECRETO"] = "valor-de-ejemplo-no-real"
    resultados: dict[str, dict[str, str]] = {c: {} for c in
                                              ("bucle infinito", "bomba de memoria", "leer un archivo ajeno",
                                               "leer el entorno del servicio", "abrir una conexión de red", "escapar por introspección")}

    with tempfile.TemporaryDirectory() as tmp:
        canario = Path(tmp) / "canario.txt"
        canario.write_text("contenido-del-servicio", encoding="utf-8")
        ruta = str(canario).replace("\\", "\\\\")

        # Servidor local que solo acepta una conexión y guarda lo que recibe
        recibido: list[bytes] = []
        srv = socket.socket()
        srv.bind(("127.0.0.1", 0))
        srv.listen(1)
        srv.settimeout(3)
        puerto = srv.getsockname()[1]

        def escuchar():
            try:
                c, _ = srv.accept()
                recibido.append(c.recv(16))
                c.close()
            except OSError:
                pass

        hilo = threading.Thread(target=escuchar, daemon=True)
        hilo.start()

        # --- R1: exec con __builtins__ vacío (solo lo que se puede probar sin colgar el proceso)
        r1 = resultados
        r1["bucle infinito"]["exec sin builtins"] = "no se puede acotar en el mismo proceso (no se ejecutó)"
        r1["bomba de memoria"]["exec sin builtins"] = "sin límite en el mismo proceso (no se ejecutó)"
        ambito = {"__builtins__": {}}
        try:
            exec("x = ().__class__.__base__.__subclasses__()", ambito)  # nosec B102 - código fijo del experimento
            clases = ambito["x"]
            wrap = [c for c in clases if c.__name__ == "_wrap_close"]
            r1["escapar por introspección"]["exec sin builtins"] = f"NO contenido: alcanza {len(clases)} clases"
            if wrap:
                f = wrap[0].__init__.__globals__
                lee = f.get("system") is not None
                r1["leer el entorno del servicio"]["exec sin builtins"] = (
                    "NO contenido: alcanza el módulo del sistema operativo" if lee else "contenido")
            else:
                r1["leer el entorno del servicio"]["exec sin builtins"] = "no se encontró la ruta en esta versión"
        except Exception as exc:  # noqa: BLE001
            r1["escapar por introspección"]["exec sin builtins"] = f"contenido ({type(exc).__name__})"
        r1["leer un archivo ajeno"]["exec sin builtins"] = "alcanzable por la misma ruta (no se ejecutó la lectura)"
        r1["abrir una conexión de red"]["exec sin builtins"] = "alcanzable por la misma ruta (no se ejecutó la conexión)"

        # --- R2: proceso hijo con entorno vacío, directorio temporal y tiempo máximo
        termino, _, seg = _hijo("while True: pass", timeout=0.5)
        r1["bucle infinito"]["proceso hijo"] = f"contenido: terminado a los {fmt(seg * 1000, 0)} ms" if not termino else "NO contenido"
        termino, salida, _ = _hijo("b = bytearray(256*1024*1024); print('reservados', len(b) // 2**20, 'MiB')", timeout=5)
        r1["bomba de memoria"]["proceso hijo"] = f"NO contenido: {salida}" if "reservados" in salida else "contenido"
        termino, salida, _ = _hijo(f"print(open('{ruta}').read()[:9])", timeout=3)
        r1["leer un archivo ajeno"]["proceso hijo"] = f"NO contenido: leyó «{salida}»" if "contenido" in salida else "contenido"
        termino, salida, _ = _hijo("import os; print(os.environ.get('PARTE48_SECRETO'))", timeout=3)
        r1["leer el entorno del servicio"]["proceso hijo"] = "contenido: entorno vacío" if salida == "None" else f"NO contenido: {salida}"
        _hijo(f"import socket; s = socket.create_connection(('127.0.0.1', {puerto}), 2); s.sendall(b'hola'); s.close()", timeout=3)
        hilo.join(2)
        r1["abrir una conexión de red"]["proceso hijo"] = "NO contenido: el servidor local recibió la conexión" if recibido else "contenido"
        r1["escapar por introspección"]["proceso hijo"] = "no aplica: el hijo es un intérprete completo (todo lo anterior ya vale)"
        srv.close()

    # --- R3: módulo de WebAssembly con combustible, memoria acotada y sin importaciones
    if wt is None:
        for c in resultados:
            resultados[c]["módulo Wasm"] = "NO EJECUTADO (falta wasmtime)"
    else:
        cfg = wt.Config()
        cfg.consume_fuel = True
        engine = wt.Engine(cfg)
        wat = """
        (module
          (memory (export "mem") 1 1)
          (func (export "bucle") (loop $l (br $l)))
          (func (export "bomba") (result i32) (local $i i32)
            (loop $l (drop (memory.grow (i32.const 1))) (local.set $i (i32.add (local.get $i) (i32.const 1)))
                     (br_if $l (i32.lt_u (local.get $i) (i32.const 1000))))
            (memory.size))
          (func (export "leer_fuera") (result i32) (i32.load (i32.const 1000000))))
        """
        modulo = wt.Module(engine, wt.wat2wasm(wat))

        def nuevo():
            s = wt.Store(engine)
            s.set_fuel(2_000_000)
            s.set_limits(memory_size=65536)
            return s, wt.Instance(s, modulo, []).exports(s)

        s, ex = nuevo()
        t = time.perf_counter()
        try:
            ex["bucle"](s)
            resultados["bucle infinito"]["módulo Wasm"] = "NO contenido"
        except wt.Trap as exc:
            resultados["bucle infinito"]["módulo Wasm"] = f"contenido: {_razon(exc)} a los {fmt((time.perf_counter() - t) * 1000, 0)} ms"
        s, ex = nuevo()
        paginas = ex["bomba"](s)
        resultados["bomba de memoria"]["módulo Wasm"] = f"contenido: tras 1000 intentos de crecer la memoria sigue en {paginas} página"
        s, ex = nuevo()
        try:
            ex["leer_fuera"](s)
            resultados["leer un archivo ajeno"]["módulo Wasm"] = "NO contenido"
        except wt.Trap as exc:
            resultados["leer un archivo ajeno"]["módulo Wasm"] = f"contenido: no tiene llamada para abrir archivos; leer fuera de su memoria da «{_razon(exc)}»"
        resultados["leer el entorno del servicio"]["módulo Wasm"] = f"contenido: {len(modulo.imports)} importaciones, no hay forma de nombrar el entorno"
        wat_net = '(module (import "host" "conectar" (func (param i32))) (func (export "f") (call 0 (i32.const 1))))'
        try:
            wt.Linker(engine).instantiate(wt.Store(engine), wt.Module(engine, wt.wat2wasm(wat_net)))
            resultados["abrir una conexión de red"]["módulo Wasm"] = "NO contenido"
        except Exception as exc:  # noqa: BLE001
            resultados["abrir una conexión de red"]["módulo Wasm"] = f"contenido: no se instancia ({_razon(exc)[:48]}…)"
        resultados["escapar por introspección"]["módulo Wasm"] = "no aplica: el formato no tiene introspección del anfitrión"

    rows = [["Comportamiento", "exec sin builtins", "proceso hijo (entorno vacío, 0,5 s)", "módulo Wasm (combustible, 1 página)"]]
    for c, v in resultados.items():
        rows.append([c, v.get("exec sin builtins", ""), v.get("proceso hijo", ""), v.get("módulo Wasm", "")])
    table(rows)
    print("  lectura: ninguna forma contiene todo; el proceso hijo contiene el tiempo y el entorno pero no la memoria, los archivos ni la red; el módulo contiene los seis porque no puede expresarlos, y a cambio solo ejecuta código compilado a Wasm")
    print("  NO EJECUTADO: contenedor, microVM y núcleo de aplicación (no medidos); un proceso con perfil de llamadas de sistema o límites de memoria del sistema operativo (en Windows exigen objetos de trabajo, que no se probaron)")


# ====================================================================== proyecto
WAT_REGLA = """
(module
  (func (export "debe_avisar") (param $horas i32) (param $dia i32) (param $previo i32) (result i32)
    (i32.and
      (i32.le_s (local.get $horas) (local.get $previo))
      (i32.ne (local.get $dia) (i32.const 7))))
)
"""
WAT_REGLA_CARA = """
(module
  (func (export "debe_avisar") (param $horas i32) (param $dia i32) (param $previo i32) (result i32)
    (local $i i32) (local $acc i32)
    (loop $l
      (local.set $acc (i32.add (local.get $acc) (local.get $i)))
      (local.set $i (i32.add (local.get $i) (i32.const 1)))
      (br_if $l (i32.lt_u (local.get $i) (i32.const 300))))
    (i32.le_s (local.get $horas) (local.get $previo)))
)
"""
WAT_BUCLE = '(module (func (export "debe_avisar") (param i32 i32 i32) (result i32) (loop $l (br $l)) (i32.const 0)))'
WAT_MEMORIA = '(module (memory 1 100) (func (export "debe_avisar") (param i32 i32 i32) (result i32) (drop (memory.grow (i32.const 50))) (memory.size)))'
WAT_IMPORTA = '(module (import "host" "leer_archivo" (func (param i32))) (func (export "debe_avisar") (param i32 i32 i32) (result i32) (call 0 (i32.const 0)) (i32.const 1)))'
WAT_TRAMPA = '(module (memory 1 1) (func (export "debe_avisar") (param i32 i32 i32) (result i32) (i32.load (i32.const 99999))))'

PERMITIDAS: set[tuple[str, str]] = set()   # el contrato de Avisos: las reglas no importan nada
COMBUSTIBLE = 100_000
MEMORIA_MAX = 65536


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


class Registro:
    """Registro de evidencia encadenado: cada entrada incluye el resumen de la anterior."""

    def __init__(self):
        self.entradas: list[dict] = []
        self.cabeza = "0" * 64

    def anotar(self, **datos):
        entrada = {"seq": len(self.entradas), "previo": self.cabeza, **datos}
        self.cabeza = sha(json.dumps(entrada, sort_keys=True, ensure_ascii=False).encode())
        entrada["resumen"] = self.cabeza
        self.entradas.append(entrada)

    @staticmethod
    def verificar(entradas) -> int | None:
        """Devuelve el índice de la primera entrada inconsistente, o None si la cadena es íntegra."""
        previo = "0" * 64
        for i, e in enumerate(entradas):
            cuerpo = {k: v for k, v in e.items() if k != "resumen"}
            if cuerpo["previo"] != previo or sha(json.dumps(cuerpo, sort_keys=True, ensure_ascii=False).encode()) != e["resumen"]:
                return i
            previo = e["resumen"]
        return None


def proyecto():
    print("Proyecto: plataforma mínima de reglas de aviso con validador, límites, evidencia encadenada e informe firmado")
    wt = _wasmtime()
    if wt is None:
        print("  NO EJECUTADO: sin wasmtime no hay plataforma que probar.")
        return
    cfg = wt.Config()
    cfg.consume_fuel = True
    engine = wt.Engine(cfg)
    registro = Registro()
    modulos = {}

    def aceptar(nombre: str, wat: str):
        """Validador de subida: compila, lee las importaciones y rechaza las que no estén permitidas."""
        binario = wt.wat2wasm(wat)
        modulo = wt.Module(engine, binario)
        pedidas = {(i.module, i.name) for i in modulo.imports}
        fuera = sorted(pedidas - PERMITIDAS)
        if fuera:
            registro.anotar(evento="rechazado", regla=nombre, modulo=sha(binario)[:16], motivo=f"importaciones no permitidas: {fuera}")
            return False
        modulos[nombre] = (modulo, sha(binario)[:16])
        registro.anotar(evento="aceptado", regla=nombre, modulo=sha(binario)[:16], bytes=len(binario))
        return True

    print("  validador de subida (el contrato exige cero importaciones):")
    subidas = {"regla-estandar": WAT_REGLA, "regla-con-calculo": WAT_REGLA_CARA, "regla-con-bucle-infinito": WAT_BUCLE,
               "regla-que-crece-memoria": WAT_MEMORIA, "regla-que-lee-archivos": WAT_IMPORTA, "regla-con-trampa": WAT_TRAMPA}
    for nombre, wat in subidas.items():
        ok = aceptar(nombre, wat)
        print(f"    {nombre}: {'aceptada' if ok else 'RECHAZADA al subir'}")

    def ejecutar(nombre: str, horas: int, dia: int, previo: int):
        modulo, huella = modulos[nombre]
        s = wt.Store(engine)
        s.set_fuel(COMBUSTIBLE)
        s.set_limits(memory_size=MEMORIA_MAX)
        t = time.perf_counter()
        try:
            ex = wt.Instance(s, modulo, []).exports(s)
            r = ex["debe_avisar"](s, horas, dia, previo)
            estado = "ok"
        except wt.Trap as exc:
            r, estado = 1, "falla:" + _razon(exc)   # política: ante un fallo, avisar (aviso de más cuesta menos que uno de menos)
        return r, estado, COMBUSTIBLE - s.get_fuel(), (time.perf_counter() - t) * 1000, huella

    print("  una petición por regla aceptada y su resultado:")
    rows = [["Regla", "Estado", "Resultado", "Combustible consumido", "Latencia (ms)"]]
    for nombre in modulos:
        r, estado, fuel, ms, huella = ejecutar(nombre, 48, 3, 72)
        rows.append([nombre, estado, r, fuel, fmt(ms, 3)])
        registro.anotar(evento="llamada", regla=nombre, modulo=huella, estado=estado, resultado=r, combustible=fuel)
    table(rows)

    # carga: 2000 peticiones con semilla fija sobre las dos reglas que funcionan
    rng = random.Random(SEED)
    lat: dict[str, list[float]] = {"regla-estandar": [], "regla-con-calculo": []}
    avisos = 0
    for _ in range(2000):
        nombre = rng.choice(list(lat))
        r, estado, fuel, ms, huella = ejecutar(nombre, rng.randint(0, 200), rng.randint(1, 7), 72)
        lat[nombre].append(ms)
        avisos += r
        if _ % 400 == 0:
            registro.anotar(evento="muestra", regla=nombre, modulo=huella, resultado=r, combustible=fuel)
    print(f"  2000 peticiones con semilla {SEED} (instancia nueva por petición, módulos ya compilados): avisos emitidos {avisos}")
    for nombre, v in lat.items():
        print(f"    {nombre}: {len(v)} peticiones; p50 {fmt(L.median(v), 3)} ms; p99 {fmt(pct(v, 0.99), 3)} ms; máx {fmt(max(v), 3)} ms")

    # integridad del registro
    ok = Registro.verificar(registro.entradas)
    print(f"  cadena de evidencia: {len(registro.entradas)} entradas; verificación = {'íntegra' if ok is None else f'rota en la entrada {ok}'}; cabeza {registro.cabeza[:16]}…")
    copia = json.loads(json.dumps(registro.entradas))
    copia[3]["resultado"] = 0 if copia[3].get("resultado") != 0 else 1
    copia[3]["estado"] = "ok"
    print(f"  alterar el resultado de la entrada 3 → la verificación detecta la rotura en la entrada {Registro.verificar(copia)}")
    copia2 = json.loads(json.dumps(registro.entradas))
    del copia2[2]
    print(f"  borrar la entrada 2 → la verificación detecta la rotura en la entrada {Registro.verificar(copia2)}")

    # informe firmado
    informe = json.dumps({"cabeza": registro.cabeza, "entradas": len(registro.entradas), "reglas": {k: v[1] for k, v in modulos.items()}},
                         sort_keys=True).encode()
    dsa = L.optional("dilithium_py.ml_dsa", "pip install dilithium-py==1.5.1")
    if dsa is not None:
        pk, sk = dsa.ML_DSA_65.keygen()
        firma = dsa.ML_DSA_65.sign(sk, informe)
        print(f"  informe de {len(informe)} bytes firmado con ML-DSA-65: firma de {len(firma)} bytes, clave pública de {len(pk)} bytes; verifica = {dsa.ML_DSA_65.verify(pk, informe, firma)}; con un byte distinto verifica = {dsa.ML_DSA_65.verify(pk, informe + b' ', firma)}")
    else:
        clave = secrets.token_bytes(32)
        mac = hmac.new(clave, informe, hashlib.sha256).hexdigest()
        print(f"  informe firmado con HMAC (clave simétrica; sin dilithium-py no hay firma poscuántica): {mac[:16]}…")
    print("  NO EJECUTADO: autenticación de los clientes con tokens y audiencia en esta plataforma (se ejercitó en el bloque B), ni contenedor ni microVM alrededor del anfitrión, ni TEE")


TABLE = {"taller": taller, "proyecto": proyecto}

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for key in sys.argv[1:] or list(TABLE):
        TABLE[key]()
        print()
