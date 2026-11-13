"""Figures for SE-017 and SE-018."""
from __future__ import annotations

import math

from figure_kit import Fig


# ---------------------------------------------------------------- SE-017
def se017_campos() -> Fig:
    f = Fig(960, 420, "Una instrucción por dentro: ADD x3, x1, x2 en RISC-V",
            "Formato R de RISC-V de 32 bits con sus seis campos: funct7 (0000000), rs2 (00010, registro x2), rs1 (00001, "
            "registro x1), funct3 (000), rd (00011, registro x3) y opcode (0110011). Codificada vale 0x002081B3.")
    fields = [
        ("funct7", 7, "0000000", "variante de la operación"),
        ("rs2", 5, "00010", "registro fuente 2 = x2"),
        ("rs1", 5, "00001", "registro fuente 1 = x1"),
        ("funct3", 3, "000", "variante"),
        ("rd", 5, "00011", "registro destino = x3"),
        ("opcode", 7, "0110011", "tipo: operación entre registros"),
    ]
    unit, x = 28.5, 20
    f.text(480, 28, "Los 32 bits, de izquierda (bit 31) a derecha (bit 0)", 14, "middle", 700)
    for i, (name, width, bits, meaning) in enumerate(fields):
        w = width * unit
        kind = ["gold", "teal", "teal", "gold", "coral", "navy"][i]
        f.box(x, 56, w - 2, 36, name, kind, 13, bold=True)
        f.box(x, 96, w - 2, 44, bits, "plain", 13 if width < 5 else 14, bold=True)
        f.box(x, 148, w - 2, 74, meaning, "grey", 12)
        x += w
    f.box(20, 248, 920, 54, "Ensamblador: ADD x3, x1, x2   →   código de máquina: 0000000 00010 00001 000 00011 0110011   →   hexadecimal 0x002081B3", "navy", 14, bold=True)
    f.box(20, 316, 450, 80, "Efecto arquitectónico: x3 ← x1 + x2. Cambia un registro y el contador de programa avanza 4 bytes; no toca la memoria.", "teal", 13)
    f.box(490, 316, 450, 80, "Lo que no dice: cuántos ciclos tarda, qué unidades usa ni si el procesador la reordena. Eso es microarquitectura.", "gold", 13)
    return f


def _simulate():
    prog = [
        ("LOADI", "r1", 4), ("LOADI", "r2", 3), ("LOADI", "r3", 0), ("LOADI", "r4", 1),
        ("BEQZ", "r1", 8), ("ADD", "r3", "r3", "r2"), ("SUB", "r1", "r1", "r4"), ("JMP", 4), ("STORE", 16, "r3"),
    ]
    text = ["LOADI r1, 4", "LOADI r2, 3", "LOADI r3, 0", "LOADI r4, 1", "BEQZ r1, 8", "ADD r3, r3, r2", "SUB r1, r1, r4", "JMP 4", "STORE [16], r3"]
    regs = {"r1": 0, "r2": 0, "r3": 0, "r4": 0}
    pc, step, trace = 0, 0, []
    while pc < len(prog):
        ins = prog[pc]
        npc = pc + 1
        if ins[0] == "LOADI":
            regs[ins[1]] = ins[2]
        elif ins[0] == "ADD":
            regs[ins[1]] = regs[ins[2]] + regs[ins[3]]
        elif ins[0] == "SUB":
            regs[ins[1]] = regs[ins[2]] - regs[ins[3]]
        elif ins[0] == "BEQZ" and regs[ins[1]] == 0:
            npc = ins[2]
        elif ins[0] == "JMP":
            npc = ins[1]
        step += 1
        trace.append((step, pc, text[pc], dict(regs), npc))
        pc = npc
    return text, trace


def se017_traza() -> Fig:
    text, trace = _simulate()
    f = Fig(960, 520, "Traza de un bucle: 9 instrucciones escritas, 22 ejecutadas",
            "A la izquierda un programa de nueve instrucciones didácticas que multiplica 4 por 3 con sumas repetidas. "
            "A la derecha el estado después de cada instrucción ejecutada en una selección de pasos: el programa ejecuta "
            "22 instrucciones dinámicas y deja 12 en la dirección 16.")
    f.text(20, 24, "Programa (instrucciones estáticas)", 14, "start", 700)
    for i, t in enumerate(text):
        f.box(20, 36 + i * 42, 280, 36, f"{i}: {t}", "grey" if i not in (4, 5, 6, 7) else "gold", 13)
    f.text(20, 36 + 9 * 42 + 18, "Amarillo = cuerpo del bucle (se repite 4 veces)", 12, "start")
    heads = ["Paso", "PC", "Instrucción", "r1", "r3"]
    xs, ws = [330, 390, 450, 640, 700], [56, 56, 186, 56, 56]
    f.text(330, 24, "Estado tras cada paso (r2 = 3 y r4 = 1 no cambian)", 14, "start", 700)
    for j, h in enumerate(heads):
        f.box(xs[j], 36, ws[j], 32, h, "navy", 12, bold=True)
    rows = [t for t in trace if t[0] in (4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22)]
    for i, (step, pc, ins, regs, npc) in enumerate(rows):
        y = 74 + i * 33
        vals = [str(step), str(pc), ins, str(regs["r1"]), str(regs["r3"])]
        for j, v in enumerate(vals):
            f.box(xs[j], y, ws[j], 30, v, "plain" if pc not in (5, 6) else "teal", 12)
    f.box(780, 74, 170, 200, "Contar instrucciones de bytecode o de ensamblador no predice tiempo: el mismo programa ejecuta 22 pasos, no 9.", "coral", 13)
    f.box(780, 290, 170, 190, "Estado final: r1 = 0, r3 = 12 y la dirección 16 guarda 12.", "teal", 13)
    return f


def se017_pipeline() -> Fig:
    f = Fig(960, 400, "Segmentación (pipeline) de cinco etapas con una dependencia carga-uso",
            "Diagrama de ciclos para cuatro instrucciones: dos cargas, una suma que depende de la segunda carga y un almacenamiento. "
            "La suma espera un ciclo, de modo que las cuatro instrucciones terminan en nueve ciclos en lugar de ocho.")
    stages = ["IF", "ID", "EX", "MEM", "WB"]
    f.text(20, 28, "Etapas: IF = obtener, ID = decodificar, EX = ejecutar, MEM = memoria, WB = escribir el resultado", 13, "start", 700)
    cw, x0 = 78, 250
    for c in range(9):
        f.text(x0 + c * cw + cw / 2, 62, f"ciclo {c + 1}", 12, "middle", 700)
    rows = [
        ("1  LOAD r1, [a]", {1: "IF", 2: "ID", 3: "EX", 4: "MEM", 5: "WB"}, "teal"),
        ("2  LOAD r2, [b]", {2: "IF", 3: "ID", 4: "EX", 5: "MEM", 6: "WB"}, "teal"),
        ("3  ADD r3, r1, r2", {3: "IF", 4: "ID", 5: "ID*", 6: "EX", 7: "MEM", 8: "WB"}, "gold"),
        ("4  STORE [c], r3", {4: "IF", 5: "IF*", 6: "ID", 7: "EX", 8: "MEM", 9: "WB"}, "plain"),
    ]
    for r, (name, cells, kind) in enumerate(rows):
        y = 74 + r * 62
        f.box(10, y, 232, 50, name, "navy", 13, bold=True)
        for c, label in cells.items():
            k = "coral" if label.endswith("*") else kind
            f.box(x0 + (c - 1) * cw + 2, y, cw - 4, 50, label, k, 13, bold=label.endswith("*"))
    f.box(10, 330, 462, 58, "ID* e IF* = espera (burbuja): la suma necesita r2, que la segunda carga entrega al final de MEM.", "coral", 13)
    f.box(488, 330, 462, 58, "Modelo didáctico clásico. Las CPU reales son más complejas: varias unidades, reordenamiento y predicción de saltos.", "grey", 13)
    return f


# ---------------------------------------------------------------- SE-018
def se018_recorrido() -> Fig:
    f = Fig(940, 470, "Recorrer una lista en orden o barajado: tiempo por acceso según el tamaño",
            "Gráfico de líneas con una medición real en CPython 3.12.9: el tiempo por acceso en orden secuencial se mantiene "
            "cerca de 40 a 45 nanosegundos, mientras en orden barajado sube de 46 a 310 nanosegundos al crecer la lista de mil a cuatro millones de elementos.")
    sizes = [("1 024", 40.2, 46.1), ("16 384", 43.1, 67.5), ("262 144", 44.6, 218.4), ("1 048 576", 44.6, 277.6), ("4 194 304", 45.1, 309.6)]
    x0, base, h = 90, 340, 260
    f.line(x0, base, 620, base, "#32505f", width=1.8)
    f.line(x0, 60, x0, base, "#32505f", width=1.8)
    f.text(x0 - 10, 66, "ns por acceso", 13, "end")
    def y(v):
        return base - v / 330 * h
    xs = [x0 + 50 + i * 120 for i in range(5)]
    f.arrow([(x, y(s)) for x, (_, s, _) in zip(xs, sizes)], color="#087f8c")
    f.arrow([(x, y(r)) for x, (_, _, r) in zip(xs, sizes)], dashed=True, color="#c0432f")
    for x, (label, s, r) in zip(xs, sizes):
        f.dot(x, y(s), "", "teal")
        f.box(x - 8, y(r) - 8, 16, 16, "", "coral", radius=2)
        f.text(x, base + 20, label, 12)
        f.text(x, y(s) + 26, f"{s:g}", 12, "middle", 700)
        f.text(x, y(r) - 16, f"{r:g}", 12, "middle", 700)
    f.text(360, base + 44, "elementos de la lista", 13, "middle")
    f.box(650, 60, 270, 56, "Círculos y línea continua: orden secuencial.", "teal", 13)
    f.box(650, 124, 270, 56, "Cuadrados y línea discontinua: orden barajado.", "coral", 13)
    f.box(650, 188, 270, 150, "Con 4 194 304 elementos el barajado es unas 6,9 veces más lento por acceso, aunque hace la misma suma. Es compatible con efectos de localidad; el script no mide las cachés.", "gold", 13)
    f.text(470, 440, "Mediana de 5 repeticiones, semilla 7, CPython 3.12.9 en Windows. La sobrecarga del intérprete diluye el efecto en tamaños pequeños.", 12, "middle", 400, "#5c1f14")
    return f


def se018_memoria() -> Fig:
    f = Fig(900, 400, "Una misma colección de un millón de enteros, tres representaciones",
            "Barras horizontales con la memoria medida por tracemalloc: una lista de Python con un millón de enteros usa unos 40 megabytes, "
            "un array de enteros de 64 bits usa unos 8,2 y un bytearray de un millón de bytes usa 1.")
    items = [("list de int (un millón)", 39.99, "coral", "8 bytes de puntero + objeto int de 28 bytes por elemento"),
             ("array('q') (un millón)", 8.18, "gold", "8 bytes por elemento, contiguos"),
             ("bytearray (un millón)", 1.0, "teal", "1 byte por elemento, contiguos")]
    x0, scale = 230, 12.0
    f.text(20, 30, "Memoria asignada por la estructura (megabytes, medida con tracemalloc)", 14, "start", 700)
    for i, (name, mb, kind, note) in enumerate(items):
        y = 56 + i * 96
        f.text(x0 - 10, y + 28, name, 13, "end", 700)
        f.box(x0, y + 6, mb * scale, 34, "", kind, radius=3)
        f.text(x0 + mb * scale + 8, y + 29, f"{mb:.1f} MB", 13, "start", 700)
        f.text(x0, y + 62, note, 12, "start")
    f.box(20, 350, 860, 40, "La representación decide el conjunto de trabajo: lo que no cabe en un nivel de la jerarquía se paga en el siguiente.", "grey", 13)
    return f


def se018_durabilidad() -> Fig:
    f = Fig(900, 430, "El costo de pedir durabilidad: 200 escrituras de 100 bytes",
            "Barras en escala logarítmica con una medición real: con búfer 1,86 milisegundos, con flush en cada escritura 1,26, "
            "y con fsync en cada escritura 218 milisegundos, unos 1 090 microsegundos por escritura.")
    items = [("Con búfer (fsync al final)", 1.86, 9.3, "gold"),
             ("flush() tras cada escritura", 1.26, 6.3, "gold"),
             ("fsync() tras cada escritura", 218.25, 1091.3, "coral")]
    x0 = 260
    f.text(20, 30, "Tiempo total para 200 escrituras (escala logarítmica)", 14, "start", 700)
    for i, (name, ms, us, kind) in enumerate(items):
        y = 56 + i * 88
        w = 30 + (math.log10(ms) - math.log10(1.0)) * 110
        f.text(x0 - 10, y + 28, name, 13, "end", 700)
        f.box(x0, y + 6, w, 34, "", kind, radius=3)
        f.text(x0 + w + 8, y + 29, f"{ms:g} ms (≈ {us:g} µs por escritura)".replace(".", ","), 13, "start", 700)
    f.box(20, 330, 860, 80, "fsync pide al sistema que persista los datos en el dispositivo: cuesta del orden de cien veces más que entregarlos al sistema. "
          "Por eso se agrupa: se decide qué fallo se tolera y cuántas escrituras se pueden perder.", "coral", 13)
    f.text(450, 424, "Mediana de 5 repeticiones en un SSD, CPython 3.12.9 en Windows; flush y búfer quedan dentro del ruido.", 12, "middle", 400, "#5c1f14")
    return f


FIGURES = {
    "se-017-campos-de-instruccion.svg": se017_campos,
    "se-017-traza-de-un-bucle.svg": se017_traza,
    "se-017-pipeline-y-dependencia.svg": se017_pipeline,
    "se-018-recorrido-secuencial-barajado.svg": se018_recorrido,
    "se-018-lista-frente-a-array.svg": se018_memoria,
    "se-018-costo-de-durabilidad.svg": se018_durabilidad,
}
