"""Figures for the failure case study TSB (IT migration of 20-22 April 2018).

Numbers come from the FCA Final Notice of 20 December 2022 and the joint FCA/PRA press release of the same date.
Output goes to ``casos/figures/``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from figure_cases import case_cards  # noqa: E402
from figure_kit import Fig, _kit_finish, _kit_start, _wrap, grouped_bars, timeline  # noqa: E402

FCA = "Fuente: FCA, Final Notice a TSB Bank plc (20 de diciembre de 2022)."
ANALISIS = "Análisis propio apoyado en el Final Notice de la FCA; no es una conclusión del regulador."


def sketch(title: str, desc: str, width: int = 940):
    return _kit_start(title, desc, width, None)


def bx(f: Fig, x: float, y: float, w: float, h: float, text: str, kind: str = "plain", size: int = 13, bold: bool = False) -> None:
    lines = _wrap(text, size, w - 20)
    assert len(lines) * size * 1.28 <= h - 6, f"box overflows: {text!r} ({len(lines)} lines in {h}px)"
    f.box(x, y, w, h, text, kind, size, bold=bold)


def done(f: Fig, y: float, note: str, kind: str = "gold", foot: str = "") -> Fig:
    _kit_finish(f, y, note, kind, foot)
    f.kind = "diagram"
    return f


# ------------------------------------------------------------------ 1. contexto y arquitectura
def contexto() -> Fig:
    f, y = sketch("De la plataforma de Lloyds a Proteo4UK: una migración sin vuelta atrás",
                  "Diagrama de antes y después: hasta abril de 2018 TSB recibía sus servicios informáticos de la plataforma de Lloyds Banking Group; el fin de semana del 20 al 22 de abril de 2018 migró a Proteo4UK, una versión nueva de la plataforma de Sabadell construida y operada por SABIS, que a su vez dependía de 85 terceros; tras la migración no se podía volver a la plataforma de Lloyds.")
    y0 = y + 6
    f.group(10, y0, 420, 232, "Antes (hasta el 20 de abril de 2018)", "grey")
    bx(f, 30, y0 + 40, 380, 56, "Plataforma de Lloyds Banking Group, bajo contrato de externalización hasta julio de 2024", "plain")
    bx(f, 30, y0 + 112, 380, 56, "Servicios de TSB: sucursales, teléfono, banca por internet y móvil", "teal")
    f.arrow([(220, y0 + 96), (220, y0 + 112)])
    bx(f, 30, y0 + 178, 380, 44, "Operación a cargo de Lloyds, ya en producción", "plain")
    f.group(510, y0, 420, 232, "Después (desde el 22 de abril de 2018)", "coral")
    bx(f, 530, y0 + 40, 380, 56, "Proteo4UK: versión nueva de la plataforma de Sabadell, construida y operada por SABIS", "coral", 13, True)
    bx(f, 530, y0 + 112, 380, 56, "SABIS depende de 85 terceros (cuartas partes desde TSB)", "gold")
    f.arrow([(720, y0 + 96), (720, y0 + 112)])
    bx(f, 530, y0 + 178, 380, 44, "Sin vuelta atrás a la plataforma de Lloyds", "navy", 13, True)
    f.arrow([(430, y0 + 116), (510, y0 + 116)], "migración", label_at=(470, y0 + 100))
    return done(f, y0 + 246,
                "Lo que enseña: la migración cambió de una vez el sistema, el operador y la cadena de proveedores, y eliminó la posibilidad de volver. Eso convierte cualquier defecto en un incidente sin salida, porque solo se puede arreglar hacia delante.",
                "gold", FCA + " Secciones 2.1 a 2.4, 2.22 y 2.27.")


# ------------------------------------------------------------------ 2. cascada
def cascada() -> Fig:
    f, y = sketch("La cascada: cada canal que falló empujó a los clientes al siguiente",
                  "Cadena de cinco pasos: fallos en la banca por internet y móvil llevan a los clientes al teléfono; el teléfono se satura y también falla por otros problemas de tecnología; los clientes acuden a las sucursales, donde los servicios eran lentos por fallos de tecnología; y las quejas desbordan la capacidad de gestión durante casi doce meses.")
    y0 = y + 6
    pasos = [("Fallos en internet y móvil", "coral"), ("Los clientes llaman por teléfono", "gold"), ("Teléfono saturado y con fallos propios", "coral"), ("Colas en sucursales con servicios lentos", "gold"), ("225 492 quejas; casi 12 meses para resolverlas", "coral")]
    w, gap = 160, 30
    for i, (t, k) in enumerate(pasos):
        x = 10 + i * (w + gap)
        bx(f, x, y0 + 20, w, 104, t, k, 13, True)
        if i < 4:
            f.arrow([(x + w, y0 + 72), (x + w + gap, y0 + 72)])
    bx(f, 10, y0 + 160, 420, 64, "Cada paso aumentaba la carga del siguiente: la demanda se trasladaba, no se resolvía", "navy", 13)
    bx(f, 470, y0 + 160, 460, 64, "El plan de crisis cubría las primeras 48 horas y ejercicios de unos pocos días; muchos incidentes duraron semanas", "teal")
    return done(f, y0 + 240,
                "Lo que enseña: un fallo en un canal aparece como carga en los demás. La capacidad de teléfono y sucursales estaba dimensionada, según el regulador, por debajo del volumen que provocó el incidente.",
                "gold", FCA + " Párrafos 2.6, 2.29 a 2.31.")


# ------------------------------------------------------------------ 3. línea de tiempo
def tiempos() -> Fig:
    return timeline(
        "De la compra por Sabadell al regreso a la normalidad: 54 meses",
        "Línea de tiempo en meses desde junio de 2014: TSB se escinde de Lloyds en junio de 2014, Sabadell la adquiere en julio de 2015, el plan maestro de marzo de 2016 apuntaba a migrar a finales de 2017, en septiembre de 2017 se decide replantear el plan, el fin de semana del 20 al 22 de abril de 2018 se migra y TSB no vuelve a la normalidad operativa hasta el 10 de diciembre de 2018.",
        [("Programa de migración", [(13, 46, "Diseño, construcción y pruebas", "gold")]),
         ("Después de la migración", [(46, 54, "Incidente", "coral")])],
        unit="Meses desde junio de 2014 (0 = junio de 2014)",
        events=[(13, "Jul 2015"), (21, "Mar 2016"), (39, "Sep 2017"), (46, "Abr 2018")],
        ticks=[0, 12, 24, 36, 48, 54], t_max=56, label_w=190,
        note="Julio de 2015: Sabadell adquiere TSB. Marzo de 2016: plan maestro con migración a finales de 2017 pese a ir meses atrasado. Septiembre de 2017: se decide replantear el plan y nueve días después se anuncia migración en el primer trimestre de 2018. Abril de 2018: migración. Diciembre de 2018: fin del incidente, según el regulador. Las posiciones son aproximadas al mes.",
        note_kind="gold", foot=FCA + " Párrafos 2.1 a 2.12 y 2.7.")


# ------------------------------------------------------------------ 4. gráfico con datos citados
def dinero() -> Fig:
    return grouped_bars(
        "Lo que el regulador cuantifica: compensación y multas",
        "Barras horizontales en millones de libras: compensación pagada a clientes 32,7; multa de la FCA 29,75 tras el descuento del 30 %; multa de la FCA antes del descuento 42,5; y multa de la PRA 18,9.",
        ["Compensación a clientes (22 abr 2018 a 7 abr 2019)", "Multa FCA tras el 30 % de descuento", "Multa FCA sin descuento", "Multa PRA"],
        [("Millones de libras", [32.7, 29.75, 42.5, 18.9], "coral")],
        unit="Millones de libras esterlinas (£)", horizontal=True, label_w=330, decimals=2,
        ticks=[0, 10, 20, 30, 40, 50],
        note="La multa total fue de 48,65 millones (FCA 29,75 más PRA 18,9). La compensación pagada fue de 32 705 762 libras por distintos conceptos (reparación, gastos, molestias). No incluye el costo interno del programa de remediación ni la pérdida de clientes, que las fuentes consultadas no cuantifican.",
        note_kind="gold", foot=FCA + " y comunicado conjunto FCA/PRA del 20 de diciembre de 2022.")


# ------------------------------------------------------------------ 5. mejoras
def mejoras() -> Fig:
    return case_cards(
        "Siete decisiones del caso y la mejora que las habría cambiado",
        "Siete tarjetas con una situación documentada y la mejora propuesta: plan realista con incertidumbre, criterios de salida de pruebas, prueba de configuración de centros de datos, diligencia sobre el proveedor, migración por etapas con vuelta atrás, plan de crisis de semanas y comunicación a clientes.",
        [("Plan maestro de izquierda a derecha con fecha pública, ya atrasado", "Plan con la incertidumbre explícita y fecha no comprometida", "La fecha pública redujo el margen para decidir con evidencia.", "teal"),
         ("Pruebas en paralelo y terminadas el día antes de decidir", "Criterios de salida de pruebas y tiempo para corregir", "Las pruebas se comprimieron para cumplir los plazos.", "teal"),
         ("Pruebas de configuración de los centros de datos reducidas en febrero de 2018", "Mantener la prueba, o registrar el riesgo ante el comité adecuado", "Según la FCA, probablemente habría detectado el problema de configuración.", "teal"),
         ("Capacidad de SABIS y de sus 85 terceros sin evaluación formal", "Diligencia formal y ejercicios conjuntos de incidente con el proveedor", "No se identificó de forma explícita el riesgo de incumplimiento del proveedor.", "teal"),
         ("Migración casi total en un fin de semana y sin vuelta atrás", "Migración por oleadas con vuelta atrás probada", "Sin retorno posible, cualquier defecto se arregla en caliente.", "teal"),
         ("Guías para las primeras 48 horas y ejercicios de unos días", "Plan para semanas, con ampliación de capacidad y comunicación", "Muchos incidentes duraron semanas.", "teal"),
         ("Mensajes genéricos y clientes vulnerables sin identificar", "Guion de comunicación y registro de clientes vulnerables antes de migrar", "Los mensajes no reflejaban la experiencia real del cliente.", "teal")],
        note=ANALISIS, note_kind="teal", foot="", left=0.46)


FIGURES = {
    "tsb-contexto.svg": contexto,
    "tsb-cascada-de-canales.svg": cascada,
    "tsb-linea-de-tiempo.svg": tiempos,
    "tsb-costos.svg": dinero,
    "tsb-mejoras.svg": mejoras,
}


def main(out: str | None = None) -> int:
    target = Path(out) if out else Path(__file__).resolve().parents[1] / "casos" / "figures"
    target.mkdir(parents=True, exist_ok=True)
    for name, builder in FIGURES.items():
        (target / name).write_text(builder().svg(), encoding="utf-8", newline="\n")
        print("wrote", target / name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else None))
