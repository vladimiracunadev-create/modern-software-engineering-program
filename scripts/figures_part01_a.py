"""Figures for SE-013 to SE-016."""
from __future__ import annotations

import math

from figure_kit import Fig


# ---------------------------------------------------------------- SE-013
def se013_ventanas() -> Fig:
    f = Fig(960, 470, "Qué ve cada herramienta y qué no revela, capa por capa",
            "Cinco capas, de código Python a microarquitectura. Para cada una: el contrato en su frontera, la "
            "herramienta que la observa y lo que esa observación no demuestra.")
    heads = ["Capa", "Contrato en su frontera", "Se observa con", "No revela"]
    xs, ws = [10, 150, 400, 650], [135, 245, 245, 300]
    rows = [
        ("Código Python", "Semántica del lenguaje: valores, control, excepciones", "Pruebas, depurador, módulo dis", "Qué instrucciones nativas se ejecutan"),
        ("Runtime CPython", "Objetos, bytecode y gestión de memoria", "sys, platform, dis, tracemalloc", "Instrucciones y cachés del procesador"),
        ("Sistema operativo", "Procesos, archivos y memoria virtual", "os, resource; strace o Process Monitor", "Qué hace el dispositivo tras aceptar la escritura"),
        ("ISA", "Instrucciones y registros visibles al software", "Documentación de la ISA; platform.machine() como etiqueta", "El modelo exacto de CPU ni su rendimiento"),
        ("Microarquitectura", "Pipeline, cachés, predicción: implementación de la ISA", "Contadores de hardware (perf); fuera del alcance de Python", "Nada más abajo en esta clase"),
    ]
    for j, h in enumerate(heads):
        f.box(xs[j], 12, ws[j], 38, h, "navy", 13, bold=True)
    for i, row in enumerate(rows):
        y = 58 + i * 74
        for j, cell in enumerate(row):
            kind = ["grey", "teal", "gold", "coral"][j]
            f.box(xs[j], y, ws[j], 66, cell, kind, 13, bold=(j == 0))
    f.text(480, 448, "Cada herramienta mira por una ventana. Una observación correcta se acompaña de su fuente y de su límite.", 13, "middle")
    return f


def se013_pared_cpu() -> Fig:
    f = Fig(900, 420, "Tiempo de pared frente a tiempo de CPU en dos programas",
            "Gráfico de barras con una medición real: dormir 0,5 segundos consume 0,5 s de pared y 0,0 s de CPU; "
            "un bucle de cálculo consume 0,26 s de pared y 0,27 s de CPU. El mismo síntoma, tardar, tiene causas distintas.")
    base, unit, x0 = 320, 400, 80
    f.line(x0, base, 560, base, "#32505f", width=1.8)
    f.line(x0, 40, x0, base, "#32505f", width=1.8)
    f.text(x0 - 8, 48, "segundos", 13, "end")
    groups = [("Dormir 0,5 s\n(espera)", 0.5, 0.0), ("Bucle de cálculo\n(3 millones de pasos)", 0.26, 0.266)]
    for k, (name, wall, cpu) in enumerate(groups):
        gx = x0 + 50 + k * 220
        f.box(gx, base - wall * unit, 60, max(wall * unit, 1), "", "gold", radius=3)
        f.box(gx + 66, base - max(cpu * unit, 2), 60, max(cpu * unit, 2), "", "teal", radius=3)
        f.text(gx + 30, base - wall * unit - 8, f"{wall:g}", 13, weight=700)
        f.text(gx + 96, base - max(cpu * unit, 2) - 8, f"{cpu:g}", 13, weight=700)
        f.text(gx + 63, base + 22, name, 13)
    f.box(590, 60, 290, 40, "", "gold", radius=3)
    f.text(735, 85, "Tiempo de pared (perf_counter)", 13, "middle", 700)
    f.box(590, 108, 290, 40, "", "teal", radius=3)
    f.text(735, 133, "Tiempo de CPU (process_time)", 13, "middle", 700)
    f.box(590, 170, 290, 130, "Si la CPU no trabaja mientras el reloj corre, el proceso espera: I/O, red, bloqueo o reposo. "
          "Acelerar la CPU no ataca esa causa.", "coral", 13)
    f.text(450, 380, "Una ejecución en CPython 3.12.9, Windows, AMD64. Repite varias veces: los valores varían entre máquinas y corridas.", 13, "middle", 400, "#5c1f14")
    return f


def se013_jerarquia() -> Fig:
    f = Fig(940, 460, "Órdenes de magnitud de la latencia, en escala logarítmica",
            "Barras horizontales en escala logarítmica con latencias típicas aproximadas: registro, caché L1, memoria "
            "principal, SSD, red del mismo centro de datos, disco giratorio y red intercontinental. Cada escalón es de uno "
            "o varios órdenes de magnitud.")
    items = [
        ("Registro", 0.3, "≈ 0,3 ns"),
        ("Caché L1", 1.0, "≈ 1 ns"),
        ("Caché L3", 20.0, "≈ 20 ns"),
        ("Memoria principal", 100.0, "≈ 100 ns"),
        ("SSD (lectura aleatoria)", 1e5, "≈ 100 µs"),
        ("Red, mismo centro de datos", 5e5, "≈ 0,5 ms"),
        ("Disco giratorio (búsqueda)", 5e6, "≈ 5 ms"),
        ("Red entre continentes", 1e8, "≈ 100 ms"),
    ]
    x0, scale = 250, 62
    f.text(20, 24, "Latencia típica (orden de magnitud; varía por modelo y carga)", 14, "start", 700)
    for i, (name, ns, label) in enumerate(items):
        y = 44 + i * 44
        w = (math.log10(ns) + 1.0) * scale
        f.text(x0 - 10, y + 24, name, 13, "end")
        kind = "teal" if ns < 1000 else ("gold" if ns < 1e7 else "coral")
        f.box(x0, y + 4, max(w, 6), 28, "", kind, radius=3)
        f.text(x0 + max(w, 6) + 8, y + 24, label, 13, "start", 700)
    f.text(470, 438, "La escala es logarítmica: cada unidad de longitud multiplica por diez. Una espera de red de ~100 ms equivale a ~10⁹ accesos a caché L1.",
           13, "middle")
    return f


# ---------------------------------------------------------------- SE-014
def se014_posicional() -> Fig:
    f = Fig(940, 460, "Un mismo patrón de bits, tres lecturas",
            "Arriba, el valor posicional de 1011 en binario: 8+0+2+1 = 11 = 0xB. Abajo, el patrón 01000001 leído como "
            "entero sin signo vale 65, como ASCII es la letra A y en hexadecimal se escribe 0x41.")
    f.text(20, 26, "A · Valor posicional: 1011₂", 14, "start", 700)
    weights = ["2³ = 8", "2² = 4", "2¹ = 2", "2⁰ = 1"]
    bits = ["1", "0", "1", "1"]
    for i, (w, b) in enumerate(zip(weights, bits)):
        x = 60 + i * 130
        f.box(x, 44, 110, 34, w, "grey", 13)
        f.box(x, 84, 110, 50, b, "navy", 22, bold=True)
        f.box(x, 140, 110, 34, f"{int(b) * [8, 4, 2, 1][i]}", "teal" if b == "1" else "plain", 14, bold=True)
    f.text(610, 120, "= 8 + 0 + 2 + 1", 16, "start", 700)
    f.text(610, 148, "= 11 = 0x0B", 16, "start", 700)
    f.text(610, 176, "Convertir cambia la notación, no el valor.", 13, "start")
    f.text(20, 226, "B · El patrón 01000001 y su significado", 14, "start", 700)
    f.box(40, 244, 480, 54, "0 1 0 0 0 0 0 1", "navy", 22, bold=True)
    for i, (title, text, kind) in enumerate([
        ("Entero sin signo", "65", "teal"), ("Texto ASCII", "«A»", "gold"), ("Hexadecimal", "0x41", "grey"),
    ]):
        x = 40 + i * 300
        f.arrow([(280, 298), (x + 110, 336)], dashed=True)
        f.box(x, 336, 220, 56, f"{title}: {text}", kind, 14, bold=True)
    f.text(470, 430, "Los bits aportan estados; el formato aporta significado. Sin formato declarado, el patrón no dice qué es.", 13, "middle")
    return f


def se014_anillo() -> Fig:
    f = Fig(940, 520, "Anillo de 4 bits: sin signo por dentro, complemento a dos por fuera",
            "Dieciséis patrones de cuatro bits dispuestos en círculo. Cada uno se lee como entero sin signo de 0 a 15 o "
            "como entero con signo de -8 a 7. Sumar 1 a 0111 (7) da 1000, que con signo es -8: desbordamiento.")
    cx, cy, r = 330, 260, 170
    f.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#8a9aa3" stroke-width="1.4" stroke-dasharray="5 4"/>')
    for k in range(16):
        angle = -math.pi / 2 + k * 2 * math.pi / 16
        x, y = cx + r * math.cos(angle), cy + r * math.sin(angle)
        signed = k if k < 8 else k - 16
        kind = "coral" if k in (7, 8) else ("teal" if k < 8 else "gold")
        f.dot(x, y, "", kind)
        f.text(cx + (r - 38) * math.cos(angle), cy + (r - 38) * math.sin(angle) + 5, str(k), 13, "middle", 400)
        f.text(cx + (r + 38) * math.cos(angle), cy + (r + 38) * math.sin(angle) + 5, str(signed), 13, "middle", 700)
        f.text(cx + (r - 70) * math.cos(angle), cy + (r - 70) * math.sin(angle) + 4, format(k, "04b"), 11, "middle", 400, "#32505f")
    f.text(cx, cy - 4, "patrón de 4 bits", 13, "middle", 700)
    f.text(cx, cy + 16, "dentro: sin signo", 13, "middle")
    f.text(cx, cy + 36, "fuera: con signo", 13, "middle", 700)
    f.box(620, 70, 300, 120, "Sumar 1 a 0111 (7) da 1000. Sin signo es 8; con signo es −8. La suma «da la vuelta»: acarreo descartado, resultado fuera de rango.", "coral", 13)
    f.box(620, 206, 300, 100, "Rangos con n bits: sin signo 0 a 2ⁿ−1; con signo −2ⁿ⁻¹ a 2ⁿ⁻¹−1. Con 8 bits: 0 a 255 y −128 a 127.", "teal", 13)
    f.box(620, 322, 300, 110, "Python usa enteros de precisión arbitraria y no da la vuelta. Al simular un protocolo debes imponer el ancho, por ejemplo con & 0xFF.", "gold", 13)
    return f


def se014_endianess() -> Fig:
    f = Fig(940, 430, "El mismo entero de 32 bits en memoria, según el orden de bytes",
            "El valor 1 serializado en cuatro bytes. En big-endian queda 00 00 00 01; en little-endian queda 01 00 00 00. "
            "Si un lector asume el orden contrario, 1 se interpreta como 16 777 216.")
    f.text(20, 26, "Valor: 1 = 0x00000001 (32 bits)", 14, "start", 700)
    addrs = ["dirección +0", "dirección +1", "dirección +2", "dirección +3"]
    for i, a in enumerate(addrs):
        f.text(330 + i * 120, 62, a, 12, "middle", 700)
    big = ["00", "00", "00", "01"]
    little = ["01", "00", "00", "00"]
    f.text(20, 112, "big-endian", 14, "start", 700)
    f.text(20, 132, "(el más significativo primero)", 12, "start")
    f.text(20, 212, "little-endian", 14, "start", 700)
    f.text(20, 232, "(el menos significativo primero)", 12, "start")
    for i in range(4):
        f.box(272 + i * 120, 82, 116, 54, big[i], "teal", 20, bold=True)
        f.box(272 + i * 120, 182, 116, 54, little[i], "gold", 20, bold=True)
    f.arrow([(270 + 2 * 120, 240), (270 + 2 * 120, 290)], dashed=True, color="#c0432f")
    f.box(60, 292, 820, 70, "Lectura cruzada: bytes escritos en little-endian (01 00 00 00) leídos como big-endian dan 0x01000000 = 16 777 216. "
          "Ningún byte se perdió: se perdió el contrato.", "coral", 13, bold=True)
    f.text(470, 396, "El orden se fija en el contrato del formato (por ejemplo, orden de red = big-endian), no se detecta en cada extremo.", 13, "middle")
    return f


# ---------------------------------------------------------------- SE-015
def se015_capas() -> Fig:
    f = Fig(940, 430, "De carácter a bytes: puntos de código y dos codificaciones",
            "Tabla con cuatro caracteres (A, í, € y el emoji de cara sonriente): su punto de código Unicode, sus bytes "
            "en UTF-8 y sus unidades de código en UTF-16. El emoji necesita cuatro bytes en UTF-8 y dos unidades en UTF-16.")
    heads = ["Carácter", "Punto de código", "UTF-8 (bytes)", "UTF-16 (unidades)"]
    xs, ws = [10, 170, 380, 650], [155, 205, 265, 280]
    rows = [
        ("A", "U+0041", "41 (1 byte)", "0041 (1 unidad)"),
        ("í", "U+00ED", "C3 AD (2 bytes)", "00ED (1 unidad)"),
        ("€", "U+20AC", "E2 82 AC (3 bytes)", "20AC (1 unidad)"),
        ("😀", "U+1F600", "F0 9F 98 80 (4 bytes)", "D83D DE00 (2 unidades: par sustituto)"),
    ]
    for j, h in enumerate(heads):
        f.box(xs[j], 12, ws[j], 40, h, "navy", 13, bold=True)
    for i, row in enumerate(rows):
        y = 60 + i * 66
        for j, cell in enumerate(row):
            kind = ["grey", "teal", "gold", "plain"][j]
            f.box(xs[j], y, ws[j], 58, cell, kind, 18 if j == 0 else 13, bold=(j == 0))
    f.box(10, 332, 920, 58, "Unicode asigna números a caracteres abstractos; UTF-8 y UTF-16 son dos formas de convertir esos números en bytes. "
          "ASCII conserva sus bytes en UTF-8.", "grey", 13)
    f.text(470, 414, "Los valores se verificaron con Python (encode); el emoji se muestra con el glifo del sistema del lector.", 12, "middle")
    return f


def se015_mojibake() -> Fig:
    f = Fig(960, 470, "Anatomía del mojibake y su reparación paso a paso",
            "Fila superior: la letra í se codifica en UTF-8 como C3 AD; si esos bytes se decodifican como Windows-1252 "
            "aparece Ã y un guion blando invisible; si ese texto se guarda de nuevo en UTF-8 los bytes pasan a C3 83 C2 AD. "
            "Fila inferior: la reparación invierte exactamente esa cadena.")
    f.text(20, 26, "Cómo se rompe (una vez por cada capa de error)", 14, "start", 700)
    steps = [
        ("í", "texto correcto, punto U+00ED"),
        ("C3 AD", "bytes UTF-8 correctos"),
        ("Ã + U+00AD", "mal decodificado como Windows-1252 (el segundo carácter es un guion blando, invisible)"),
        ("C3 83 C2 AD", "guardado de nuevo en UTF-8: segunda capa de error"),
    ]
    for i, (a, b) in enumerate(steps):
        x = 14 + i * 236
        f.box(x, 44, 218, 52, a, "coral" if i >= 2 else "teal", 16, bold=True)
        f.box(x, 100, 218, 86, b, "plain", 13)
        if i < 3:
            f.arrow([(x + 218, 70), (x + 236, 70)])
    f.text(20, 236, "Cómo se repara (se invierte la cadena y se valida)", 14, "start", 700)
    fix = [
        ("Texto mal decodificado", "Ã seguido de U+00AD (invisible)"),
        ("encode('cp1252')", "recupera los bytes originales C3 AD"),
        ("decode('utf-8')", "recupera «í» con el contrato correcto"),
        ("Validar", "ida y vuelta sobre una muestra; conservar el original"),
    ]
    for i, (a, b) in enumerate(fix):
        x = 14 + i * 236
        f.box(x, 254, 218, 52, a, "navy", 13, bold=True)
        f.box(x, 310, 218, 78, b, "teal", 13)
        if i < 3:
            f.arrow([(x + 218, 280), (x + 236, 280)])
    f.box(14, 408, 932, 48, "Un reemplazo visual de «Ã­» por «í» no repara la causa y puede dañar texto legítimo. Se reconstruye la cadena con evidencia.", "gold", 13)
    return f


def se015_longitudes() -> Fig:
    f = Fig(940, 420, "Tres textos que se ven iguales y se miden distinto",
            "Tabla de tres textos: «José» en forma compuesta, «José» en forma descompuesta y el emoji de familia. "
            "Para cada uno se cuentan grafemas, puntos de código, bytes UTF-8 y unidades UTF-16: las cuatro cuentas difieren.")
    heads = ["Texto", "Grafemas (lo que se ve)", "Puntos de código", "Bytes UTF-8", "Unidades UTF-16"]
    xs, ws = [10, 250, 440, 620, 780], [235, 185, 175, 155, 150]
    rows = [
        ("«José» compuesto (NFC)", "4", "4", "5", "4"),
        ("«José» descompuesto (NFD): e + acento", "4", "5", "6", "5"),
        ("Emoji familia: 3 personas unidas", "1", "5", "18", "8"),
    ]
    for j, h in enumerate(heads):
        f.box(xs[j], 12, ws[j], 44, h, "navy", 13, bold=True)
    for i, row in enumerate(rows):
        y = 64 + i * 72
        for j, cell in enumerate(row):
            kind = "grey" if j == 0 else ["plain", "teal", "gold", "plain"][j - 1]
            f.box(xs[j], y, ws[j], 64, cell, kind, 13 if j == 0 else 20, bold=(j > 0))
    f.box(10, 292, 920, 56, "len() en Python cuenta puntos de código. NFC y NFD son iguales para una persona y distintas para una comparación de bytes; "
          "por eso se normaliza antes de comparar.", "coral", 13)
    f.text(470, 380, "Conteos verificados con Python 3.12 (len, encode, normalize). El conteo de grafemas sigue las reglas de Unicode para el texto mostrado.", 12, "middle")
    return f


# ---------------------------------------------------------------- SE-016
def se016_ieee() -> Fig:
    f = Fig(960, 400, "Los 64 bits de 0,1 en IEEE 754 de doble precisión",
            "Un double se reparte en 1 bit de signo, 11 de exponente y 52 de fracción. El valor 0,1 se guarda como "
            "0x3FB999999999999A: signo 0, exponente 1019 (2 elevado a -4) y fracción 0x999999999999A. "
            "Es el double más cercano a 0,1, no 0,1 exacto.")
    f.box(20, 60, 90, 60, "signo\n1 bit", "coral", 13, bold=True)
    f.box(110, 60, 220, 60, "exponente\n11 bits", "gold", 13, bold=True)
    f.box(330, 60, 600, 60, "fracción (significando)\n52 bits", "teal", 13, bold=True)
    f.box(20, 130, 90, 50, "0", "plain", 18, bold=True)
    f.box(110, 130, 220, 50, "0x3FB = 1019", "plain", 16, bold=True)
    f.box(330, 130, 600, 50, "0x999999999999A", "plain", 16, bold=True)
    f.text(480, 36, "0,1 almacenado: 0x3FB999999999999A", 15, "middle", 700)
    f.box(20, 204, 910, 70, "Valor = (−1)^signo × (1 + fracción/2⁵²) × 2^(exponente − 1023) = 1,6000000000000000888… × 2⁻⁴ "
          "= 0,1000000000000000055511151231257827… (el double más cercano).", "grey", 13)
    f.box(20, 292, 440, 84, "Por eso float.hex() muestra 0x1.999999999999ap-4 y as_integer_ratio() da 3602879701896397 / 2⁵⁵.", "teal", 13)
    f.box(480, 292, 450, 84, "La salida corta «0.1» es una representación decimal conveniente; los bits guardados no son exactamente 0,1.", "gold", 13)
    return f


def _naive(n: int) -> float:
    total = 0.0
    for _ in range(n):
        total += 0.1
    return total


def se016_error() -> Fig:
    f = Fig(940, 460, "Error al sumar 0,1 repetidamente frente a una suma compensada",
            "Gráfico de barras con valores calculados por el generador: el error absoluto de sumar 0,1 con un bucle "
            "simple crece con el número de sumas, y math.fsum lo mantiene en cero.")
    ns = [10, 1000, 100_000, 1_000_000]
    errs = [abs(_naive(n) - n / 10) for n in ns]
    f.text(20, 26, "Error absoluto = |suma con bucle simple − valor exacto|", 14, "start", 700)
    top = max(errs)
    for i, (n, e) in enumerate(zip(ns, errs)):
        y = 50 + i * 80
        w = 10 + 560 * (math.log10(e) - math.log10(min(errs)) + 0.3) / (math.log10(top) - math.log10(min(errs)) + 0.3)
        f.text(20, y + 28, f"{n:,} sumas".replace(",", " "), 13, "start", 700)
        f.box(160, y + 6, w, 34, "", "coral", radius=3)
        f.text(160 + w + 8, y + 29, f"{e:.2e}".replace("e-0", "e-").replace("e+0", "e+"), 13, "start", 700)
        f.text(160, y + 62, "math.fsum: error 0", 12, "start", 400, "#0b3f45")
    f.box(20, 376, 900, 60, "Longitud de la barra en escala logarítmica. Cada suma redondea; los errores se acumulan. "
          "Reordenar o compensar (fsum) cambia el resultado: no existe «la» suma correcta de floats, sino una política.", "grey", 13)
    return f


def se016_decision() -> Fig:
    f = Fig(940, 470, "Elegir la representación por invariantes del dominio",
            "Árbol de decisión: dinero con reglas decimales exactas usa enteros escalados o Decimal; identificadores y "
            "contadores usan enteros con ancho declarado; mediciones usan float con tolerancia y validación de valores especiales; "
            "proporciones exactas pueden usar Fraction.")
    f.box(300, 10, 340, 46, "¿Qué invariantes debe conservar el valor?", "navy", 14, bold=True)
    opts = [
        ("Reglas decimales exactas (dinero, tarifas)", "Entero en la unidad mínima, o Decimal con escala y redondeo declarados", "teal"),
        ("Identificador o contador", "Entero con ancho y signo del contrato; valida rango antes de serializar", "gold"),
        ("Medición con incertidumbre", "float + tolerancia relativa y absoluta; valida NaN, infinito y cero con signo", "grey"),
        ("Razón exacta entre enteros", "Fraction (racionales exactos) si el costo es aceptable", "plain"),
    ]
    for i, (q, a, kind) in enumerate(opts):
        x = 14 + i * 232
        f.arrow([(470, 56), (470, 80), (x + 108, 80), (x + 108, 100)])
        f.box(x, 100, 216, 90, q, "navy", 13, bold=True)
        f.box(x, 200, 216, 120, a, kind, 13)
    f.box(14, 344, 912, 56, "Float no es «incorrecto»: es el tipo adecuado para muchas mediciones. Lo incorrecto es usarlo por costumbre donde el dominio exige decimales exactos.", "coral", 13)
    f.box(14, 410, 912, 44, "Decimal no vuelve exacta una medición incierta ni elimina overflow o costo: la representación sigue a la invariante.", "plain", 13)
    return f


FIGURES = {
    "se-013-ventanas-de-observacion.svg": se013_ventanas,
    "se-013-pared-frente-a-cpu.svg": se013_pared_cpu,
    "se-013-latencias-por-capa.svg": se013_jerarquia,
    "se-014-valor-posicional.svg": se014_posicional,
    "se-014-anillo-complemento-a-dos.svg": se014_anillo,
    "se-014-endianess.svg": se014_endianess,
    "se-015-punto-y-bytes.svg": se015_capas,
    "se-015-anatomia-del-mojibake.svg": se015_mojibake,
    "se-015-contar-texto.svg": se015_longitudes,
    "se-016-formato-ieee754.svg": se016_ieee,
    "se-016-error-acumulado.svg": se016_error,
    "se-016-decision-de-tipo.svg": se016_decision,
}
