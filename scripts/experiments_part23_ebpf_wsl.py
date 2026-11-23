"""Experimento eBPF de la Parte 23: carga programas eBPF reales en el núcleo de Linux.

Solo biblioteca estándar (ctypes). Necesita un núcleo Linux con BPF y permisos de administrador
(CAP_BPF/CAP_SYS_ADMIN); en Windows se ejecuta dentro de WSL2 con
``wsl -u root -e python3 scripts/experiments_part23_ebpf_wsl.py``. Fuera de Linux imprime
``NO EJECUTADO`` y el motivo. No se usa ningún compilador ni bpftool: las instrucciones se
ensamblan a mano (cada una son 8 bytes) y se cargan con la llamada de sistema ``bpf(2)``.

Qué se hace: (1) cargar y ejecutar un programa válido con ``BPF_PROG_TEST_RUN``; (2) pedirle al
verificador que rechace cuatro programas inseguros y leer su mensaje real; (3) contar paquetes
en un mapa desde el programa y leerlo desde el espacio de usuario; (4) medir el costo por
ejecución que informa el propio núcleo.
"""
from __future__ import annotations

import ctypes
import os
import platform
import struct
import sys

# ------------------------------------------------------------------ constantes de la ABI
SYS_BPF = {"x86_64": 321, "aarch64": 280}.get(platform.machine(), 321)
BPF_MAP_CREATE, BPF_MAP_LOOKUP_ELEM, BPF_PROG_LOAD, BPF_PROG_TEST_RUN = 0, 1, 5, 10
BPF_MAP_TYPE_ARRAY = 2
BPF_PROG_TYPE_SOCKET_FILTER = 1

# clases y modos de instrucción
LD, LDX, ST, STX, ALU, JMP, JMP32, ALU64 = 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07
MOV, ADD = 0xB0, 0x00
K, X = 0x00, 0x08
W, DW = 0x00, 0x18
MEM = 0x60
JA, JEQ, JNE, EXIT, CALL = 0x00, 0x10, 0x50, 0x90, 0x80
XADD = 0xC0


def insn(code, dst=0, src=0, off=0, imm=0):
    return struct.pack("<BBhi", code, (src << 4) | dst, off, imm)


def mov_imm(dst, imm):
    return insn(ALU64 | MOV | K, dst, 0, 0, imm)


def mov_reg(dst, src):
    return insn(ALU64 | MOV | X, dst, src)


def add_imm(dst, imm):
    return insn(ALU64 | ADD | K, dst, 0, 0, imm)


def ldx_w(dst, src, off):
    return insn(LDX | MEM | W, dst, src, off)


def st_w(dst, off, imm):
    return insn(ST | MEM | W, dst, 0, off, imm)


def ld_map_fd(dst, fd):
    # instrucción de 16 bytes: BPF_LD | BPF_DW | BPF_IMM con src=BPF_PSEUDO_MAP_FD (1)
    return insn(LD | DW, dst, 1, 0, fd) + insn(0, 0, 0, 0, 0)


def call(helper):
    return insn(JMP | CALL, 0, 0, 0, helper)


def jmp_imm(op, dst, imm, off):
    return insn(JMP | op | K, dst, 0, off, imm)


def exit_():
    return insn(JMP | EXIT)


def stx_w(dst, off, src):
    return insn(STX | MEM | W, dst, src, off)


def xadd_w(dst, off, src):
    return insn(STX | XADD | W, dst, src, off)


# ------------------------------------------------------------------ envoltorios de bpf(2)
libc = None


def sys_bpf(cmd: int, attr: bytes) -> int:
    buf = ctypes.create_string_buffer(attr, len(attr))
    ret = libc.syscall(SYS_BPF, cmd, buf, len(attr))
    if ret < 0:
        raise OSError(ctypes.get_errno(), os.strerror(ctypes.get_errno()))
    return ret


def make_array_map(entries: int = 1) -> int:
    attr = struct.pack("<IIII", BPF_MAP_TYPE_ARRAY, 4, 4, entries) + bytes(48)
    return sys_bpf(BPF_MAP_CREATE, attr)


def map_get(fd: int, key: int) -> int:
    k = ctypes.create_string_buffer(struct.pack("<I", key))
    v = ctypes.create_string_buffer(8)
    attr = struct.pack("<IxxxxQQ", fd, ctypes.addressof(k), ctypes.addressof(v)) + bytes(32)
    sys_bpf(BPF_MAP_LOOKUP_ELEM, attr)
    return struct.unpack("<I", v.raw[:4])[0]


def load(prog: bytes, log_size: int = 1 << 16):
    """Devuelve (fd, registro_del_verificador, errno_o_None)."""
    insns = ctypes.create_string_buffer(prog, len(prog))
    lic = ctypes.create_string_buffer(b"GPL")
    log = ctypes.create_string_buffer(log_size)
    attr = struct.pack(
        "<IIQQIIQ", BPF_PROG_TYPE_SOCKET_FILTER, len(prog) // 8, ctypes.addressof(insns),
        ctypes.addressof(lic), 1, log_size, ctypes.addressof(log),
    ) + bytes(80)
    try:
        fd = sys_bpf(BPF_PROG_LOAD, attr)
        return fd, log.value.decode(errors="replace"), None
    except OSError as exc:
        return None, log.value.decode(errors="replace"), exc.errno


def test_run(fd: int, data: bytes, repeat: int = 1):
    din = ctypes.create_string_buffer(data, len(data))
    dout = ctypes.create_string_buffer(max(len(data), 64))
    attr = struct.pack(
        "<IIIIQQII", fd, 0, len(data), len(dout), ctypes.addressof(din), ctypes.addressof(dout), repeat, 0,
    ) + bytes(32)
    buf = ctypes.create_string_buffer(attr, len(attr))
    ret = libc.syscall(SYS_BPF, BPF_PROG_TEST_RUN, buf, len(attr))
    if ret < 0:
        raise OSError(ctypes.get_errno(), os.strerror(ctypes.get_errno()))
    _fd, retval, _sin, _sout, _pin, _pout, rep, dur = struct.unpack("<IIIIQQII", buf.raw[:40])
    return retval, dur


def last_lines(log: str, n: int = 3) -> str:
    lines = [ln for ln in log.strip().splitlines() if ln.strip()]
    return " / ".join(lines[-n:]) if lines else "(sin mensaje)"


def main() -> int:
    global libc
    if platform.system() != "Linux":
        print("NO EJECUTADO: eBPF necesita un núcleo Linux; sistema detectado: " + platform.system() + ".")
        return 0
    libc = ctypes.CDLL(None, use_errno=True)
    print(f"Núcleo: {platform.release()} en {platform.machine()}; uid {os.getuid()}")
    if os.getuid() != 0:
        print("NO EJECUTADO: hacen falta permisos de administrador para cargar programas eBPF.")
        return 0

    # 1. programa válido: devuelve 42
    fd, log, err = load(mov_imm(0, 42) + exit_())
    if fd is None:
        print(f"NO EJECUTADO: el núcleo no dejó cargar ni el programa trivial (errno {err}): {last_lines(log)}")
        return 0
    retval, _ = test_run(fd, bytes(64))
    print(f"[1] programa trivial: r0=42; salida del núcleo = {retval}; {last_lines(log, 1)}")

    # 2. programa que lee el campo len del contexto: devuelve el tamaño del paquete
    fd, log, err = load(ldx_w(0, 1, 0) + exit_())
    retval, _ = test_run(fd, bytes(100))
    print(f"[2] lee ctx->len con un paquete de 100 bytes: salida = {retval}")

    # 3. programas que el verificador debe rechazar (y uno que sorprende por lo que acepta)
    map_fd = make_array_map(1)
    busca_clave_variable = (
        ldx_w(3, 1, 0) + stx_w(10, -4, 3) + mov_reg(2, 10) + add_imm(2, -4) + ld_map_fd(1, map_fd) + call(1)
    )
    cases = {
        "lee un registro sin inicializar": mov_reg(0, 2) + exit_(),
        "bucle infinito sin salida": mov_imm(0, 0) + add_imm(0, 1) + insn(JMP | JA, 0, 0, -2, 0),
        "sin instrucción de salida": mov_imm(0, 1),
        "desreferencia sin comprobar nulo (clave variable)": busca_clave_variable + ldx_w(0, 0, 0) + exit_(),
        "lectura fuera del valor del mapa (valor de 4 bytes, lee en el desplazamiento 4)":
            busca_clave_variable + jmp_imm(JEQ, 0, 0, 2) + ldx_w(0, 0, 4) + exit_() + mov_imm(0, 0) + exit_(),
        "desreferencia sin comprobar nulo (clave constante 0 en un mapa de 1 entrada)":
            st_w(10, -4, 0) + mov_reg(2, 10) + add_imm(2, -4) + ld_map_fd(1, map_fd) + call(1) + ldx_w(0, 0, 0) + exit_(),
    }
    for name, prog in cases.items():
        fd2, log, err = load(prog)
        estado = "RECHAZADO" if fd2 is None else "ACEPTADO"
        print(f"[3] {name}: {estado} (errno {err}); verificador: {last_lines(log, 2)}")

    # 4. contador en un mapa con comprobación de nulo
    contador = (
        st_w(10, -4, 0) + mov_reg(2, 10) + add_imm(2, -4) + ld_map_fd(1, map_fd) + call(1)
        + jmp_imm(JEQ, 0, 0, 2)          # si r0 == NULL salta al final
        + mov_imm(1, 1) + xadd_w(0, 0, 1)  # *r0 += 1
        + mov_imm(0, 0) + exit_()
    )
    fd3, log, err = load(contador)
    if fd3 is None:
        print(f"[4] contador: NO CARGÓ (errno {err}): {last_lines(log, 3)}")
        return 0
    n = 100_000
    retval, dur = test_run(fd3, bytes(64), repeat=n)
    print(f"[4] contador con comprobación de nulo: cargó; {last_lines(log, 1)}")
    print(f"[4] {n} ejecuciones con BPF_PROG_TEST_RUN; el mapa leído desde el espacio de usuario vale {map_get(map_fd, 0)}")
    print(f"[4] tiempo medio por ejecución informado por el núcleo: {dur} ns")
    return 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
