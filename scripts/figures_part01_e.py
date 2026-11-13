"""Figures for SE-023 and SE-024."""
from __future__ import annotations

from figure_kit import Fig


# ---------------------------------------------------------------- SE-023
def se023_ruta() -> Fig:
    f = Fig(960, 500, "Ruta vertical de un evento sintético con los valores de una ejecución real",
            "Seis capas con el instrumento, el valor observado en una ejecución de ejemplo y lo que ese valor no demuestra: texto y bytes, entrada canónica, "
            "traducción, ejecución, memoria y sistema.")
    heads = ["Capa", "Instrumento", "Observado (ejecución de ejemplo)", "No demuestra"]
    xs, ws = [10, 170, 330, 690], [155, 155, 355, 255]
    rows = [
        ("Texto y bytes", "len, encode, unicodedata", "16 puntos de código; 20 bytes UTF-8; ya está en forma NFC", "Cómo lo ve una persona en otra fuente o idioma"),
        ("Entrada canónica", "json, hashlib", "SHA-256 (16 primeros hex): 7e24a88c96bab208", "Que otra serialización dé el mismo hash"),
        ("Traducción", "ast, dis", "AST de resumir: 21 nodos; bytecode: 15 instrucciones (CPython 3.12.9)", "Cuántas instrucciones nativas se ejecutan"),
        ("Ejecución", "time", "100 000 vueltas, resultado 4 999 950 000; pared 0,086 s, CPU 0,094 s", "Dónde se va el tiempo con precisión"),
        ("Memoria", "tracemalloc", "Pico de 216 bytes en Python", "Memoria nativa ni consumo total del proceso"),
        ("Sistema", "platform", "Etiqueta AMD64", "Modelo de CPU, cachés o frecuencia"),
    ]
    for j, h in enumerate(heads):
        f.box(xs[j], 10, ws[j], 38, h, "navy", 13, bold=True)
    for i, row in enumerate(rows):
        y = 56 + i * 68
        for j, cell in enumerate(row):
            f.box(xs[j], y, ws[j], 60, cell, ["grey", "plain", "teal", "coral"][j], 12 if j else 13, bold=(j == 0))
    f.text(480, 480, "Una captura sin pregunta es una colección; la ruta convierte cada valor en evidencia de una transición y de su límite.", 13, "middle")
    return f


def se023_mapa() -> Fig:
    f = Fig(960, 520, "Mapa de evidencia: ocho afirmaciones clasificadas",
            "Tabla de ocho afirmaciones del dossier con su clasificación como observado, inferido o desconocido y la fuente o el motivo. "
            "El consumo de energía, las instrucciones nativas y el comportamiento en producción quedan como desconocidos.")
    heads = ["Afirmación", "Clasificación", "Evidencia o motivo"]
    xs, ws = [10, 460, 640], [440, 170, 300]
    rows = [
        ("El texto tiene 16 puntos de código y 20 bytes UTF-8", "Observado", "len() y encode() sobre la entrada", "teal"),
        ("La entrada canónica tiene el hash 7e24a88c96bab208", "Observado", "hashlib sobre el JSON ordenado", "teal"),
        ("resumir compila a 15 instrucciones de bytecode", "Observado (3.12.9)", "dis; cambia con la versión", "teal"),
        ("La función ejecuta unas 15 instrucciones nativas", "Desconocido", "Bytecode no es la ISA", "coral"),
        ("El tiempo es de cómputo, no de espera", "Inferido", "CPU ≈ pared; la CPU supera a la pared por la resolución del reloj", "gold"),
        ("El pico de Python es 216 bytes", "Observado", "tracemalloc; solo memoria gestionada por Python", "teal"),
        ("La versión consume poca energía", "Desconocido", "No se midió energía", "coral"),
        ("Se comporta igual en producción", "Desconocido", "Entorno, carga y datos distintos", "coral"),
    ]
    for j, h in enumerate(heads):
        f.box(xs[j], 10, ws[j], 38, h, "navy", 13, bold=True)
    for i, (claim, cls, why, kind) in enumerate(rows):
        y = 56 + i * 56
        f.box(xs[0], y, ws[0], 50, claim, "plain", 13)
        f.box(xs[1], y, ws[1], 50, cls, kind, 13, bold=True)
        f.box(xs[2], y, ws[2], 50, why, "grey", 12)
    f.text(480, 510, "Cada afirmación se enlaza a un comando y un archivo. Si no puede enlazarse, es una inferencia o un desconocido.", 13, "middle")
    return f


def se023_protocolo() -> Fig:
    f = Fig(960, 470, "Protocolo de reproducción con limpieza segura",
            "Seis pasos: preparar, ejecutar, capturar, verificar invariantes, limpiar con vista previa y revisión cruzada que reproduce tres hallazgos.")
    steps = [
        ("1 Preparar", "Directorio work/SE-023, versiones y entrada fija", "teal"),
        ("2 Ejecutar", "Un comando documentado, sin privilegios", "teal"),
        ("3 Capturar", "Salida, tiempos y pico en archivos", "teal"),
        ("4 Verificar", "Hash de salida igual antes de comparar recursos", "gold"),
        ("5 Limpiar", "dry-run y luego borrar solo dentro del directorio", "coral"),
        ("6 Revisar", "Otra persona reproduce tres hallazgos", "navy"),
    ]
    for i, (name, text, kind) in enumerate(steps):
        x = 14 + i * 156
        f.box(x, 24, 146, 44, name, "navy", 13, bold=True)
        f.box(x, 74, 146, 110, text, kind, 12)
        if i < 5:
            f.arrow([(x + 146, 46), (x + 156, 46)])
    f.box(14, 210, 930, 130, "Guarda de limpieza: resolver la ruta y comprobar que está dentro de work/SE-023 antes de borrar, por ejemplo "
          "«destino = Path(ruta).resolve(); if not destino.is_relative_to(base.resolve()): abortar». "
          "Una limpieza que acepta rutas amplias puede borrar mucho más de lo previsto.", "coral", 13)
    f.box(14, 356, 930, 94, "Reproducible significa que otra persona obtiene el mismo hash y una tendencia equivalente siguiendo solo el README; "
          "si necesita preguntar, falta información (versión, tamaño, semilla o comando).", "grey", 13)
    return f


# ---------------------------------------------------------------- SE-024
def se024_pregunta() -> Fig:
    f = Fig(940, 470, "De una pregunta vaga a una pregunta contrastable",
            "Cinco pasos que añaden carga, métrica, umbral y entorno a la pregunta «qué es más rápido»: la pregunta final fija qué se mide, "
            "con qué datos, con qué decisión y en qué runtime.")
    steps = [
        ("«¿Qué es más rápido?»", "No dice qué carga, qué métrica ni para qué decisión", "coral"),
        ("+ Carga", "Archivos UTF-8 de 10 000 a 400 000 líneas, semilla fija", "gold"),
        ("+ Métricas", "Pico de memoria de Python y latencia de pared (mediana y rango)", "gold"),
        ("+ Umbral y decisión", "La latencia no debe subir más de un 10 %; si cumple, se adopta flujo", "gold"),
        ("+ Entorno", "CPython 3.12.9 en este equipo; sin afirmar nada sobre otros", "teal"),
    ]
    for i, (name, text, kind) in enumerate(steps):
        y = 20 + i * 70
        f.box(20, y, 260, 58, name, "navy", 13, bold=True)
        f.box(290, y, 630, 58, text, kind, 13)
        if i < 4:
            f.arrow([(150, y + 58), (150, y + 70)])
    f.box(20, 382, 900, 76, "Pregunta final: para archivos UTF-8 de 10 000 a 400 000 líneas, ¿procesar en flujo reduce el pico de memoria de Python sin aumentar más de un 10 % "
          "la latencia de pared en CPython 3.12.9? El umbral se justifica por el contexto de uso.", "grey", 13, bold=True)
    return f


def se024_hipotesis() -> Fig:
    f = Fig(940, 400, "Hipótesis rivales: qué observación debilita a cada una",
            "Tabla con una hipótesis principal y dos rivales: qué predice cada una y qué resultado la debilitaría. "
            "Las observaciones que la debilitan se escriben antes de ejecutar.")
    heads = ["Hipótesis", "Predice", "Se debilita si"]
    xs, ws = [10, 300, 630], [285, 325, 300]
    rows = [
        ("H1 (principal): el flujo reduce la memoria y no sube la latencia más del 10 %", "Pico mucho menor; razón de latencias ≤ 1,10", "La razón de latencias supera 1,10 con rangos separados"),
        ("H2 (rival): la lectura y el análisis dominan; materializar o no apenas cambia el tiempo", "Latencias casi iguales; la memoria sí baja", "El flujo es claramente más rápido o más lento con rangos separados"),
        ("H3 (rival): con pocos datos el costo fijo domina y no hay diferencia útil", "Diferencias dentro del ruido en 10 000 líneas", "Diferencia estable y repetible incluso con pocos datos"),
    ]
    for j, h in enumerate(heads):
        f.box(xs[j], 10, ws[j], 38, h, "navy", 13, bold=True)
    for i, row in enumerate(rows):
        y = 56 + i * 104
        for j, cell in enumerate(row):
            f.box(xs[j], y, ws[j], 96, cell, ["teal", "gold", "coral"][i] if j == 0 else "plain", 13, bold=(j == 0))
    f.text(470, 380, "Escribir antes qué resultado cuenta contra cada hipótesis evita diseñar el experimento solo para confirmar.", 13, "middle")
    return f


def se024_resultados() -> Fig:
    f = Fig(940, 460, "Resultados del estudio de ejemplo: latencia y memoria",
            "Gráfico con la razón de latencias flujo sobre materializa para tres tamaños y la reducción de memoria. "
            "La razón es 1,23 con 10 000 líneas, 0,83 con 100 000 y 0,98 con 400 000; la memoria baja de 1,4, 15,2 y 61,4 megabytes a unos 3,5 kilobytes.")
    x0, base, h = 90, 320, 230
    f.line(x0, base, 560, base, "#32505f", width=1.8)
    f.line(x0, 70, x0, base, "#32505f", width=1.8)
    f.text(x0 + 8, 62, "razón de latencias (flujo / materializa)", 13, "start")
    def Y(v):
        return base - v / 1.4 * h
    f.line(x0, Y(1.10), 560, Y(1.10), "#c0432f", dashed=True, width=1.6)
    f.text(566, Y(1.10) + 5, "umbral 1,10", 13, "start", 700, "#5c1f14")
    f.line(x0, Y(1.0), 560, Y(1.0), "#8a9aa3", dashed=True, width=1.2)
    f.text(566, Y(1.0) + 5, "igual (1,00)", 12, "start")
    pts = [("10 000", 1.23, "gold", "1,23"), ("100 000", 0.83, "teal", "0,83"), ("400 000", 0.98, "teal", "0,98")]
    for i, (n, v, kind, label) in enumerate(pts):
        x = x0 + 90 + i * 150
        f.dot(x, Y(v), "", kind)
        f.text(x, Y(v) - 20, label, 13, "middle", 700)
        f.text(x, base + 20, n + " líneas", 13)
    f.box(660, 100, 270, 110, "En 10 000 líneas la razón supera 1,10, pero los rangos de las repeticiones se solapan (13–19 ms): es inconcluso, no un fallo.", "gold", 13)
    f.box(660, 226, 270, 100, "Memoria de Python: 1,4 MB → 3,5 kB; 15,2 MB → 3,5 kB; 61,4 MB → 3,5 kB. Una reducción clara y repetible.", "teal", 13)
    f.box(660, 342, 270, 90, "No se mide energía ni producción: queda fuera de la conclusión.", "grey", 13)
    f.text(330, 440, "5 repeticiones por tamaño y versión, orden alternado, semilla 7, CPython 3.12.9 en Windows.", 12, "middle", 400, "#5c1f14")
    return f


def se024_informe() -> Fig:
    f = Fig(960, 440, "Cadena de procedencia del informe",
            "Del código y los datos crudos a la tabla derivada, el informe, la revisión y el commit identificable. "
            "La tabla se genera desde los datos crudos y no a mano.")
    steps = [
        ("Código y pruebas", "src/ y tests/ de equivalencia", "teal"),
        ("Datos crudos", "data/raw.csv: una fila por repetición", "teal"),
        ("Tabla derivada", "Generada por script desde raw.csv", "gold"),
        ("Informe", "Método, resultados, discusión y límites", "gold"),
        ("Revisión", "Otra persona reproduce y objeta; se conserva el desacuerdo", "coral"),
    ]
    for i, (name, text, kind) in enumerate(steps):
        x = 14 + i * 188
        f.box(x, 24, 176, 44, name, "navy", 13, bold=True)
        f.box(x, 74, 176, 100, text, kind, 12)
        if i < 4:
            f.arrow([(x + 176, 46), (x + 188, 46)])
    f.box(14, 200, 930, 90, "Registro de procedencia: commit, versión de Python, plataforma expuesta, entrada y semilla, comandos, orden, repeticiones, salida y limpieza. "
          "Los datos crudos se conservan; los resúmenes se derivan.", "grey", 13)
    f.box(14, 306, 930, 56, "Discusión en tres frases: observamos X; bajo estos supuestos inferimos Y; no medimos Z.", "navy", 14, bold=True)
    f.box(14, 372, 930, 56, "Un resultado inconcluso es válido si el método permite comprender por qué. Aprobar no es coincidir: es poder inspeccionar la cadena.", "plain", 13)
    return f


FIGURES = {
    "se-023-ruta-vertical.svg": se023_ruta,
    "se-023-mapa-de-evidencia.svg": se023_mapa,
    "se-023-protocolo-de-reproduccion.svg": se023_protocolo,
    "se-024-pregunta-contrastable.svg": se024_pregunta,
    "se-024-hipotesis-rivales.svg": se024_hipotesis,
    "se-024-resultados-del-ejemplo.svg": se024_resultados,
    "se-024-cadena-de-procedencia.svg": se024_informe,
}
