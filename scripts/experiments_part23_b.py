"""Experimentos de la Parte 23, bloque B: hardware seguro, computación cuántica, criptografía poscuántica y confianza cero.

Uso: python scripts/experiments_part23_b.py [tee|quantum|limits|pqc|zerotrust]

No se invoca ningún modelo de lenguaje. La criptografía poscuántica se ejecuta de verdad con las
implementaciones puras de Python ``kyber-py`` (ML-KEM, FIPS 203) y ``dilithium-py`` (ML-DSA,
FIPS 204); sus tiempos NO representan implementaciones de producción en C o ensamblador. Los
circuitos cuánticos se simulan de forma clásica con NumPy: no hay ordenador cuántico ni acceso a
uno. El hardware seguro (TEE) no se ejecuta: la máquina de desarrollo no expone un TEE utilizable
desde este script, y lo que se modela es la lógica de medición y atestación con HMAC y SHA-256.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import math
import random
import secrets
import sys
import time

import numpy as np

import experiments_part23_lab as L
from experiments_part23_lab import fmt, table, timeit_ms

SEED = 48


# ====================================================================== hardware seguro (modelo)
def sha(b: bytes) -> bytes:
    return hashlib.sha256(b).digest()


def extend(pcr: bytes, component: bytes) -> bytes:
    """Operación de extensión de un registro de medición: pcr' = H(pcr || H(componente))."""
    return sha(pcr + sha(component))


def boot_chain(components):
    pcr = bytes(32)
    for c in components:
        pcr = extend(pcr, c)
    return pcr


def tee():
    print("Hardware seguro: lógica de medición, atestación y sellado (modelo con HMAC y SHA-256; no se ejecutó ningún TEE)")
    print("  NO EJECUTADO en hardware: ni Intel SGX/TDX, ni AMD SEV-SNP, ni Arm CCA, ni un TPM: este script no usa ni consulta un TEE ni un TPM (la consulta del TPM exige permisos de administrador que no se usaron); el HMAC con una clave del dispositivo simula la firma de la raíz de confianza.")
    good = [b"firmware-1.0", b"cargador-2.3", b"nucleo-6.1", b"servicio-avisos-v7"]
    ref = boot_chain(good)
    print(f"  cadena de arranque de 4 componentes: medición final {ref.hex()[:16]}…")
    swapped = [good[0], good[2], good[1], good[3]]
    tampered = good[:3] + [b"servicio-avisos-v7-con-puerta-trasera"]
    print(f"  mismo contenido en otro orden: {boot_chain(swapped).hex()[:16]}… (distinta: {boot_chain(swapped) != ref}); un byte distinto en el último componente: {boot_chain(tampered).hex()[:16]}… (distinta: {boot_chain(tampered) != ref})")
    print(f"  la extensión no se puede «deshacer» ni reescribir: para llegar a un valor dado hay que haber ejecutado la misma secuencia; un componente que se añade después solo cambia la medición hacia adelante")

    device_key = secrets.token_bytes(32)  # clave de la raíz de confianza del dispositivo (simulada)

    def quote(measurement: bytes, nonce: bytes) -> bytes:
        return hmac.new(device_key, measurement + nonce, hashlib.sha256).digest()

    def verify(q: bytes, nonce: bytes, expected: bytes) -> bool:
        return hmac.compare_digest(q, quote(expected, nonce))

    n1 = secrets.token_bytes(16)
    q = quote(ref, n1)
    print(f"  verificador con un desafío fresco: cita legítima aceptada = {verify(q, n1, ref)}; cita de la cadena alterada aceptada = {verify(quote(boot_chain(tampered), n1), n1, ref)}")
    # Repetición: sin nonce una cita vieja de un estado bueno sirve para esconder uno malo
    q_viejo = quote(ref, b"")
    print(f"  sin desafío fresco, una cita vieja de un estado bueno se reproduce y se acepta = {verify(q_viejo, b'', ref)} (aunque el nodo ya esté alterado)")
    n2 = secrets.token_bytes(16)
    print(f"  con desafío fresco, la misma cita vieja reproducida contra un desafío nuevo se acepta = {verify(q, n2, ref)}")

    # Sellado: clave derivada de la medición
    def seal_key(measurement: bytes) -> bytes:
        return hmac.new(device_key, b"sellado" + measurement, hashlib.sha256).digest()

    print(f"  clave de sellado con la medición esperada coincide con la derivada al arrancar la misma cadena: {seal_key(ref) == seal_key(boot_chain(good))}; con la cadena alterada: {seal_key(boot_chain(tampered)) == seal_key(ref)} (los datos sellados no se pueden abrir)")

    # Lo que la atestación NO prueba: un binario medido y conocido puede tener una vulnerabilidad
    random.seed(SEED)
    flota = 1000
    comprometidas_por_firmware = 0.01
    vulnerables_en_ejecucion = 0.03
    total_mal = 0
    detecta_atest = 0
    for _ in range(flota):
        alterado = random.random() < comprometidas_por_firmware
        explotado = random.random() < vulnerables_en_ejecucion
        if alterado or explotado:
            total_mal += 1
        if alterado:
            detecta_atest += 1
    print(f"  modelo con semilla {SEED}: flota de {flota} nodos, 1 % con software alterado en el arranque y 3 % explotados en ejecución con el software legítimo: {total_mal} nodos mal en total; la atestación de arranque detecta {detecta_atest} ({fmt(100 * detecta_atest / max(1, total_mal), 0)} %): lo explotado en ejecución no cambia la medición")
    tiempos = timeit_ms(lambda: boot_chain(good), repeat=15, number=200)
    print(f"  costo de medir una cadena de 4 componentes con SHA-256 (solo el cálculo, sin hardware): {fmt(tiempos * 1000, 1)} µs")


# ====================================================================== cuántica: simulación clásica
def apply_1q(state: np.ndarray, gate: np.ndarray, q: int, n: int) -> np.ndarray:
    psi = state.reshape([2] * n)
    psi = np.moveaxis(psi, q, 0)
    psi = np.tensordot(gate, psi, axes=([1], [0]))
    psi = np.moveaxis(psi, 0, q)
    return psi.reshape(-1)


def apply_cnot(state: np.ndarray, c: int, t: int, n: int) -> np.ndarray:
    psi = state.reshape([2] * n).copy()
    idx = [slice(None)] * n
    idx[c] = 1
    sub = psi[tuple(idx)]
    # el eje del objetivo en el subarreglo (se eliminó el eje del control)
    axis = t if t < c else t - 1
    psi[tuple(idx)] = np.flip(sub, axis=axis)
    return psi.reshape(-1)


H = np.array([[1, 1], [1, -1]], dtype=np.complex128) / math.sqrt(2)
X_GATE = np.array([[0, 1], [1, 0]], dtype=np.complex128)
Z_GATE = np.array([[1, 0], [0, -1]], dtype=np.complex128)


def zero_state(n: int) -> np.ndarray:
    s = np.zeros(2 ** n, dtype=np.complex128)
    s[0] = 1
    return s


def sample(state: np.ndarray, shots: int, rng: np.random.Generator):
    p = np.abs(state) ** 2
    p = p / p.sum()
    out = rng.choice(len(p), size=shots, p=p)
    counts = {}
    for v in out:
        counts[int(v)] = counts.get(int(v), 0) + 1
    return counts


def quantum():
    print("Computación cuántica para ingenieros: simulación clásica de circuitos pequeños con NumPy (no hay ordenador cuántico)")
    rng = np.random.default_rng(SEED)
    n = 2
    s = apply_cnot(apply_1q(zero_state(n), H, 0, n), 0, 1, n)
    print(f"  estado de Bell: amplitudes {np.round(s, 4).tolist()}")
    c = sample(s, 1000, rng)
    print(f"  1000 mediciones con semilla {SEED}: {{{', '.join(f'{k:0{n}b}: {v}' for k, v in sorted(c.items()))}}}: solo aparecen 00 y 11, nunca 01 ni 10")
    # interferencia: H dos veces
    s1 = apply_1q(zero_state(1), H, 0, 1)
    s2 = apply_1q(s1, H, 0, 1)
    print(f"  H una vez: probabilidades {np.round(np.abs(s1) ** 2, 3).tolist()}; H dos veces: {np.round(np.abs(s2) ** 2, 3).tolist()} (la amplitud negativa cancela: interferencia, no azar)")
    # GHZ
    n = 5
    g = zero_state(n)
    g = apply_1q(g, H, 0, n)
    for t in range(1, n):
        g = apply_cnot(g, 0, t, n)
    cg = sample(g, 1000, rng)
    print(f"  GHZ de 5 qubits, 1000 mediciones: {{{', '.join(f'{k:0{n}b}: {v}' for k, v in sorted(cg.items()))}}}")
    # Crecimiento exponencial de la simulación
    print("  costo de simular n qubits con vector de estado (complex128, 16 bytes por amplitud): memoria y tiempo de aplicar H a todos los qubits")
    rows = [["Qubits", "Amplitudes", "Memoria del vector", "Tiempo de H en todos los qubits (ms)"]]
    for nq in (10, 14, 18, 20, 22, 24):
        st = zero_state(nq)
        t0 = time.perf_counter()
        for q in range(nq):
            st = apply_1q(st, H, q, nq)
        dt = (time.perf_counter() - t0) * 1000
        mem = 16 * 2 ** nq
        rows.append([nq, 2 ** nq, f"{mem / 2 ** 20:.2f} MiB".replace(".", ","), fmt(dt, 1)])
        del st
    table(rows)
    print(f"  extrapolación (aritmética, no medida): 50 qubits = {2 ** 50} amplitudes = 16 PiB; 100 qubits = 2^100 amplitudes = 2^54 PiB (el número de amplitudes crece como 2^n)")


def grover_probability(n: int, k: int, marked: int = 0) -> float:
    N = 2 ** n
    s = np.full(N, 1 / math.sqrt(N), dtype=np.float64)
    for _ in range(k):
        s[marked] *= -1
        s = 2 * s.mean() - s
    return float(s[marked] ** 2)


def order_finding_n15(a: int, rng: np.random.Generator):
    """Búsqueda de periodo para N=15 con 8 qubits de conteo, simulada clásicamente con NumPy."""
    N = 15
    t = 8
    Q = 2 ** t
    # estado tras aplicar la superposición y la función modular, medir el registro de trabajo
    vals = np.array([pow(a, x, N) for x in range(Q)])
    measured = vals[int(rng.integers(0, Q))]  # medir el segundo registro colapsa el primero
    amp = np.where(vals == measured, 1.0, 0.0)
    amp = amp / np.linalg.norm(amp)
    spectrum = np.abs(np.fft.fft(amp)) ** 2 / Q  # QFT = FFT unitaria
    spectrum = spectrum / spectrum.sum()
    return spectrum, Q


def limits():
    print("Cuántica: qué ofrece y qué no (Grover, Shor para N = 15 y ruido), todo simulado de forma clásica")
    print("  Grover: probabilidad de medir el elemento buscado según las iteraciones; óptimo cerca de (π/4)·√N")
    rows = [["Qubits n", "N = 2^n", "Iteraciones óptimas", "Probabilidad al óptimo", "Con el doble de iteraciones", "Consultas clásicas esperadas (N/2)"]]
    for n in (4, 8, 12, 16):
        N = 2 ** n
        k = int(round(math.pi / 4 * math.sqrt(N) - 0.5))
        rows.append([n, N, k, fmt(grover_probability(n, k), 4), fmt(grover_probability(n, 2 * k), 4), N // 2])
    table(rows)
    print("  con el doble de iteraciones la probabilidad cae: pasarse del óptimo empeora el resultado (el algoritmo no es «más pasos, mejor respuesta»)")
    print(f"  ventaja de Grover: de N/2 consultas esperadas a unas (π/4)·√N: para N = 2^40 son {fmt(2 ** 39 / (math.pi / 4 * 2 ** 20), 0)} veces menos consultas, y cada consulta es una evaluación de un circuito completo, no una lectura de memoria")

    rng = np.random.default_rng(SEED)
    for a in (7, 2):
        spec, Q = order_finding_n15(a, rng)
        picos = [int(i) for i in np.argsort(spec)[-4:][::-1]]
        r = next(r for r in range(1, 15) if pow(a, r, 15) == 1)
        print(f"  Shor, N = 15, a = {a}: periodo verdadero r = {r}; los 4 picos del espectro de 256 puntos están en {sorted(picos)} (múltiplos de 256/r = {Q // r})")
    import math as _m
    r = 4
    a = 7
    f1 = _m.gcd(pow(a, r // 2) - 1, 15)
    f2 = _m.gcd(pow(a, r // 2) + 1, 15)
    print(f"  con r = 4 y a = 7: mcd(7^2 − 1, 15) = {f1} y mcd(7^2 + 1, 15) = {f2}: 15 = {f1} × {f2}; la parte cuántica solo encuentra el periodo, el resto es aritmética clásica")

    # Ruido: GHZ con errores de Pauli aleatorios por puerta
    print("  ruido: estado GHZ de n qubits con probabilidad p de un error de bit o de fase tras cada puerta (muestreo con semilla; 4000 repeticiones):")
    rng2 = np.random.default_rng(SEED)
    rows = [["Qubits", "Puertas", "p = 0,001", "p = 0,01", "p = 0,05"]]
    for n in (2, 4, 6, 8, 10):
        row = [n, n]
        for p in (0.001, 0.01, 0.05):
            ok = 0
            reps = 4000
            for _ in range(reps):
                st = zero_state(n)
                st = apply_1q(st, H, 0, n)
                if rng2.random() < p:
                    st = apply_1q(st, X_GATE if rng2.random() < 0.5 else Z_GATE, 0, n)
                for t in range(1, n):
                    st = apply_cnot(st, 0, t, n)
                    if rng2.random() < p:
                        st = apply_1q(st, X_GATE if rng2.random() < 0.5 else Z_GATE, t, n)
                pr = np.abs(st) ** 2
                good = pr[0] + pr[-1]
                ok += rng2.random() < good
            row.append(fmt(100 * ok / reps, 1) + " %")
        rows.append(row)
    table(rows)
    print("  un error de fase no cambia la medición inmediata pero sí la coherencia del estado; aquí solo se cuenta la medición, de modo que este modelo subestima el daño en algoritmos que interfieren")


# ====================================================================== criptografía poscuántica
class Lamport:
    """Firma de un solo uso de Lamport con SHA-256 (hash-based), para ver la forma de las firmas basadas en hash."""

    def __init__(self, rng: random.Random):
        self.sk = [[bytes(rng.getrandbits(8) for _ in range(32)) for _ in range(2)] for _ in range(256)]
        self.pk = [[sha(x) for x in pair] for pair in self.sk]

    @staticmethod
    def bits(msg: bytes):
        d = int.from_bytes(sha(msg), "big")
        return [(d >> (255 - i)) & 1 for i in range(256)]

    def sign(self, msg: bytes):
        return [self.sk[i][b] for i, b in enumerate(self.bits(msg))]

    def verify(self, msg: bytes, sig) -> bool:
        return all(sha(sig[i]) == self.pk[i][b] for i, b in enumerate(self.bits(msg)))


def pqc():
    print("Criptografía poscuántica: ML-KEM y ML-DSA reales (implementaciones puras de Python), una firma basada en hash y el costo de migrar")
    kyber = L.optional("kyber_py.ml_kem", "pip install kyber-py==1.2.0")
    dil = L.optional("dilithium_py.ml_dsa", "pip install dilithium-py==1.5.1")
    if kyber is not None:
        kem = kyber.ML_KEM_768
        ek, dk = kem.keygen()
        K, ct = kem.encaps(ek)
        K2 = kem.decaps(dk, ct)
        print(f"  ML-KEM-768: clave pública {len(ek)} bytes, clave privada {len(dk)} bytes, texto cifrado {len(ct)} bytes, secreto compartido {len(K)} bytes; ambos lados obtienen el mismo secreto: {K == K2}")
        # rechazo implícito: un texto cifrado alterado produce otro secreto, sin error
        bad = bytearray(ct)
        bad[0] ^= 1
        K3 = kem.decaps(dk, bytes(bad))
        print(f"  texto cifrado con un bit alterado: decapsular no falla y devuelve otro secreto distinto = {K3 != K} (rechazo implícito: no hay error que un atacante pueda observar)")
        t_kg = timeit_ms(kem.keygen, repeat=7)
        t_en = timeit_ms(lambda: kem.encaps(ek), repeat=7)
        t_de = timeit_ms(lambda: kem.decaps(dk, ct), repeat=7)
        print(f"  tiempos en Python puro (orientativos, ordenes de magnitud más lentos que una implementación en C): generar claves {fmt(t_kg, 1)} ms, encapsular {fmt(t_en, 1)} ms, decapsular {fmt(t_de, 1)} ms")
    if dil is not None:
        dsa = dil.ML_DSA_65
        pk, sk = dsa.keygen()
        msg = b"aviso:entrega-17:vence-2026-12-01"
        sig = dsa.sign(sk, msg)
        print(f"  ML-DSA-65: clave pública {len(pk)} bytes, clave privada {len(sk)} bytes, firma {len(sig)} bytes; verifica = {dsa.verify(pk, msg, sig)}; con un byte distinto del mensaje verifica = {dsa.verify(pk, msg + b'x', sig)}")
    print("  tamaños de referencia de lo clásico (por definición de los algoritmos): X25519 clave pública 32 bytes; Ed25519 clave pública 32 bytes y firma 64 bytes; RSA-2048 clave pública 256 bytes y firma 256 bytes")
    if kyber is not None:
        # Efecto en un saludo: bytes y segmentos TCP
        mss = 1460
        clasico = 32 + 32
        hibrido = 32 + 32 + len(ek) + len(ct)
        print(f"  bytes de intercambio de claves en un saludo: X25519 {clasico} bytes ({-(-clasico // mss)} segmento); ML-KEM-768 {len(ek) + len(ct)} bytes ({-(-(len(ek) + len(ct)) // mss)} segmentos de {mss} bytes); híbrido {hibrido} bytes ({-(-hibrido // mss)} segmentos)")

    # Lamport: tamaños y la trampa de reutilizar la clave
    rng = random.Random(SEED)
    lp = Lamport(rng)
    m = b"autorizo-el-aviso-17"
    s = lp.sign(m)
    print(f"  firma de Lamport con SHA-256 (un solo uso): clave pública {256 * 2 * 32} bytes, firma {256 * 32} bytes; verifica = {lp.verify(m, s)}; mensaje alterado verifica = {lp.verify(m + b'!', s)}")
    print("  reutilizar la clave: probabilidad de poder falsificar un mensaje nuevo tras k firmas del mismo par de claves (cada posición necesita el secreto del bit que pide el mensaje: (1 − 2^−k)^256):")
    rows = [["Firmas ya emitidas k", "Probabilidad de falsificar un mensaje nuevo"]]
    for k in (1, 2, 4, 8, 12, 16):
        rows.append([k, fmt((1 - 2.0 ** -k) ** 256, 6)])
    table(rows)
    # comprobación empírica con k = 8
    emp = 0
    reps = 300
    leaked = {}
    msgs = [f"firma-{i}".encode() for i in range(8)]
    for mm in msgs:
        sg = lp.sign(mm)
        for i, b in enumerate(Lamport.bits(mm)):
            leaked[(i, b)] = sg[i]
    for j in range(reps):
        objetivo = Lamport.bits(f"mensaje-nuevo-{j}".encode())
        emp += all((i, b) in leaked for i, b in enumerate(objetivo))
    sin_revelar = 512 - len(leaked)
    print(f"  comprobación con 8 firmas reales y {reps} mensajes nuevos: falsificables {emp} de {reps} ({fmt(100 * emp / reps, 1)} %); el promedio teórico sobre conjuntos de 8 firmas es {fmt(100 * (1 - 2.0 ** -8) ** 256, 1)} %, pero para este conjunto concreto quedaron {sin_revelar} secretos sin revelar de 512 y la probabilidad es 2^-{sin_revelar} = {fmt(100 * 2.0 ** -sin_revelar, 1)} %: una clave de un solo uso reutilizada ocho veces se rompe con probabilidad alta; por eso SLH-DSA usa un árbol de claves")

    # Desigualdad de Mosca
    print("  desigualdad de Mosca: hay riesgo si x + y > z (x = años que el dato debe seguir secreto, y = años que tarda la migración, z = años hasta un ordenador cuántico capaz). Valores de ejemplo del autor, no pronósticos:")
    rows = [["x: vida del secreto (años)", "y: migración (años)", "z supuesto (años)", "x + y", "¿Riesgo?"]]
    for x, y, z in ((1, 3, 15), (15, 5, 15), (25, 5, 15), (10, 8, 15), (30, 6, 25)):
        rows.append([x, y, z, x + y, "sí" if x + y > z else "no"])
    table(rows)

    # Combinar secretos
    s1 = secrets.token_bytes(32)
    s2 = secrets.token_bytes(32)
    combinado = hmac.new(b"parte48-hibrido", s1 + s2, hashlib.sha256).digest()
    s1_roto = secrets.token_bytes(32)
    print(f"  híbrido: la clave de sesión sale de HMAC(secreto clásico || secreto poscuántico); un atacante que conoce uno solo de los dos obtiene una clave distinta de la real: {hmac.new(b'parte48-hibrido', s1_roto + s2, hashlib.sha256).digest() != combinado}")


# ====================================================================== confianza cero
def b64(b: bytes) -> str:
    import base64
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()


def make_token(key: bytes, claims: dict) -> str:
    body = b64(json.dumps(claims, sort_keys=True).encode())
    return body + "." + b64(hmac.new(key, body.encode(), hashlib.sha256).digest())


def check_token(key: bytes, token: str, now: float, audience: str):
    body, _, mac = token.partition(".")
    expected = b64(hmac.new(key, body.encode(), hashlib.sha256).digest())
    if not hmac.compare_digest(mac, expected):
        return False, "firma inválida"
    import base64
    claims = json.loads(base64.urlsafe_b64decode(body + "=" * (-len(body) % 4)))
    if claims["exp"] <= now:
        return False, "vencido"
    if claims["aud"] != audience:
        return False, "audiencia incorrecta"
    return True, claims


def zerotrust():
    print("Confianza cero en la práctica: tokens con vida corta y audiencia, y radio de daño de una credencial robada")
    key = secrets.token_bytes(32)
    now = 1_000_000.0
    tok = make_token(key, {"sub": "servicio-avisos", "aud": "calificaciones", "exp": now + 300, "posture": "ok"})
    print(f"  token legítimo para la audiencia «calificaciones»: {check_token(key, tok, now, 'calificaciones')[0]}; mismo token presentado a «pagos»: {check_token(key, tok, now, 'pagos')}; seis minutos después: {check_token(key, tok, now + 360, 'calificaciones')}")
    alterado = tok[:-2] + ("AA" if not tok.endswith("AA") else "BB")
    print(f"  token con la firma alterada: {check_token(key, alterado, now, 'calificaciones')}")
    t = timeit_ms(lambda: check_token(key, tok, now, "calificaciones"), repeat=15, number=2000)
    print(f"  costo de verificar un token en Python puro: {fmt(t * 1000, 1)} µs por petición (orden de magnitud; sin caché ni red)")

    # radio de daño: 200 servicios en 5 segmentos
    random.seed(SEED)
    servicios = 200
    segmentos = 5
    reps = 5000
    print(f"  modelo con semilla {SEED}: {servicios} servicios en {segmentos} segmentos de red; una credencial robada de un servicio al azar; cuántos servicios alcanza el atacante:")
    perim = 0
    seg = 0
    zt = 0
    for _ in range(reps):
        origen = random.randrange(servicios)
        perim += servicios                       # red plana de confianza: alcanza todos
        seg += servicios // segmentos            # segmentación: alcanza su segmento
        zt += 3                                  # credencial con audiencia: solo las 3 dependencias autorizadas del servicio
    print(f"    red plana tras el perímetro: {perim // reps}; segmentada en 5: {seg // reps}; credencial con audiencia limitada a 3 dependencias: {zt // reps}")

    # ventana de uso indebido según vida del token y retraso de detección
    print("  ventana de uso indebido de una credencial robada: tiempo medio hasta que deja de servir = mín(vida restante del token, retraso de detección); detección exponencial de media 20 min (semilla fija):")
    rows = [["Vida del token", "Ventana media de uso indebido (min)"]]
    for vida in (5, 60, 480, 43200):
        total = 0.0
        for _ in range(20000):
            restante = random.uniform(0, vida)
            deteccion = random.expovariate(1 / 20)
            total += min(restante, deteccion)
        rows.append([f"{vida} min" + (" (30 días)" if vida == 43200 else ""), fmt(total / 20000, 1)])
    table(rows)
    print("  acortar la vida del token ayuda mientras la vida sea menor que el retraso de detección; pasado cierto punto, la detección manda y más corto no mejora, solo añade renovaciones")


TABLE = {"tee": tee, "quantum": quantum, "limits": limits, "pqc": pqc, "zerotrust": zerotrust}

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for key in sys.argv[1:] or list(TABLE):
        TABLE[key]()
        print()
