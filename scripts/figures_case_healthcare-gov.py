"""Figures for the failure case study HealthCare.gov (launch of 1 October 2013).

Numbers come from GAO-14-694 (July 2014), GAO-15-238 (March 2015), the HHS OIG case study OEI-06-14-00350 and the
CMS progress report of 1 December 2013, as each footer says. Output goes to ``casos/figures/``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from figure_cases import case_cards  # noqa: E402
from figure_kit import Fig, _kit_finish, _kit_start, _wrap, dumbbell, line_chart, timeline  # noqa: E402

GAO14 = "Fuente: GAO-14-694 (julio de 2014)."
ANALISIS = "Análisis propio apoyado en GAO-14-694, GAO-15-238 y OEI-06-14-00350; no es una conclusión de esas fuentes."


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


# ------------------------------------------------------------------ 1. contexto
def contexto() -> Fig:
    f, y = sketch("Quién construyó qué: un mercado federal armado con contratistas y varias agencias",
                  "Diagrama de contexto: los ciudadanos usan el sitio Healthcare.gov; detrás está el mercado federal FFM, desarrollado por un contratista bajo CMS, que consulta el centro de servicios de datos federal, desarrollado por otro contratista, para verificar a los solicitantes con fuentes federales; las aseguradoras reciben las inscripciones.")
    y0 = y + 4
    bx(f, 10, y0 + 40, 170, 80, "Consumidores que comparan y eligen un plan", "plain", 13, True)
    bx(f, 215, y0 + 40, 170, 80, "Sitio Healthcare.gov", "teal", 13, True)
    bx(f, 420, y0 + 40, 170, 80, "FFM: mercado federal (cuentas, elegibilidad, inscripción)", "coral", 13, True)
    bx(f, 625, y0 + 40, 140, 80, "Centro de servicios de datos federal", "gold", 13, True)
    bx(f, 795, y0, 135, 56, "Fuentes federales (p. ej., IRS, SSA)", "plain")
    bx(f, 795, y0 + 76, 135, 56, "Aseguradoras (planes y primas)", "plain")
    for a, b in ((180, 215), (385, 420), (590, 625)):
        f.arrow([(a, y0 + 80), (b, y0 + 80)])
    f.arrow([(765, y0 + 66), (795, y0 + 40)])
    f.arrow([(590, y0 + 100), (600, y0 + 150), (860, y0 + 150), (860, y0 + 132)], "inscripciones", label_at=(720, y0 + 144))
    f.text(14, y0 + 190, "CMS (dentro de HHS) contrata y supervisa; en 2011 se emitieron dos órdenes de trabajo y en enero de 2014 un contrato adicional", 13, "start", 700, "#142231")
    bx(f, 14, y0 + 204, 290, 74, "FFM: orden de trabajo a CGI Federal (septiembre de 2011)", "navy", 13)
    bx(f, 325, y0 + 204, 290, 74, "Centro de datos: orden de trabajo a QSSI (septiembre de 2011)", "navy", 13)
    bx(f, 636, y0 + 204, 290, 74, "Contrato a Accenture Federal Services (enero de 2014) para completar el FFM", "navy", 13)
    return done(f, y0 + 292,
                "Lo que enseña: no era un sitio web, era una cadena de sistemas de varias organizaciones que debían funcionar juntas el mismo día. Un punto débil en cualquiera aparecía para el usuario como un único «no funciona».",
                "gold", GAO14 + " Descripción funcional; la distribución de módulos es la que GAO resume.")


# ------------------------------------------------------------------ 2. flujo y módulos
def flujo() -> Fig:
    f, y = sketch("El recorrido del usuario y el estado de cada módulo al terminar la orden de trabajo",
                  "Recorrido de cuatro pasos: crear cuenta, verificar elegibilidad, elegir plan e inscribirse, y pago de primas; GAO resume que a febrero de 2014 solo el módulo de gestión de planes estaba completo, el de elegibilidad e inscripción tenía solo parte de sus elementos y el financiero estaba sin terminar.")
    y0 = y + 6
    pasos = [("1. Crear cuenta e iniciar sesión", "coral"), ("2. Verificar identidad e ingresos con fuentes federales", "coral"), ("3. Comparar y elegir plan; inscribirse", "gold"), ("4. Pagos y conciliación con aseguradoras", "grey")]
    estado = ["Capacidad insuficiente: dificultad para crear cuentas y entrar (GAO-15-238)", "Parte de los elementos del módulo de elegibilidad e inscripción", "Módulo de gestión de planes completo (según funcionarios de CMS)", "Módulo financiero sin terminar y aplazado al final del plazo"]
    w, gap = 205, 30
    for i, ((t, k), e) in enumerate(zip(pasos, estado)):
        x = 10 + i * (w + gap)
        bx(f, x, y0, w, 90, t, k, 13, True)
        bx(f, x, y0 + 120, w, 100, e, "plain", 13)
        f.arrow([(x + w / 2, y0 + 90), (x + w / 2, y0 + 120)], dashed=True)
        if i < 3:
            f.arrow([(x + w, y0 + 45), (x + w + gap, y0 + 45)])
    f.text(14, y0 + 112, "Estado según GAO", 13, "start", 700, "#142231")
    return done(f, y0 + 234,
                "Lo que enseña: CMS priorizó para el lanzamiento lo que se necesitaba para inscribirse y aplazó lo que se necesitaba después. La decisión es defendible; el problema es que aun lo priorizado salió sin verificarse con carga ni de extremo a extremo.",
                "gold", GAO14 + " GAO-15-238 para capacidad y pruebas.")


# ------------------------------------------------------------------ 3. línea de tiempo
def tiempos() -> Fig:
    return timeline(
        "Enero de 2013 a marzo de 2014: de los plazos comprimidos al final de la primera inscripción",
        "Línea de tiempo en meses desde enero de 2013: en marzo de 2013 CMS estima que solo 65 % del FFM y 75 % del centro de datos estarán listos en septiembre; en abril amplía la fase de diseño; en septiembre hace una revisión de preparación parcial; el 1 de octubre se lanza el sitio; el 30 de noviembre es el objetivo de estabilización; la primera inscripción termina el 31 de marzo de 2014.",
        [("Desarrollo y gobierno", [(0, 9, "Requisitos aún cambiando; pruebas comprimidas", "gold")]),
         ("Operación y recuperación", [(9, 11, "Crisis", "coral"), (11, 15, "Estabilizado", "teal")])],
        unit="Meses desde enero de 2013 (0 = 1 de enero de 2013)",
        events=[(2, "Mar"), (3, "Abr"), (8, "Sep"), (9, "1 oct"), (11, "30 nov")],
        ticks=[0, 3, 6, 9, 12, 15], t_max=15.5, label_w=190,
        note="Marzo: CMS estimó que solo 65 % del FFM y 75 % del centro de datos estaría listo en septiembre. Abril: se extendió el diseño y se comprimieron las pruebas. Septiembre: revisión de preparación parcial, con el desarrollo aún sin terminar. 30 de noviembre: objetivo de estabilización declarado por la administración. Los límites de la fase «Crisis» y «Estabilizado» son aproximados.",
        note_kind="gold", foot=GAO14 + " OEI-06-14-00350 y CMS (1 de diciembre de 2013).")


# ------------------------------------------------------------------ 4. gráfico con datos citados: crecimiento de obligaciones
def obligaciones() -> Fig:
    x_ticks = [(2011.67, "sep 2011"), (2012.58, "ago 2012"), (2013.25, "abr 2013"), (2013.67, "sep 2013"), (2014.08, "feb 2014")]
    return line_chart(
        "El dinero comprometido creció con cada cambio de requisitos",
        "Líneas con la obligación acumulada en millones de dólares para el mercado federal FFM, que pasa de 55,7 en septiembre de 2011 a 209,6 en febrero de 2014, y para el centro de datos, que pasa de 29,9 a 84,5 entre septiembre de 2011 y septiembre de 2013.",
        [("FFM (CGI Federal)", [(2011.67, 55.7, "55,7", "t"), (2012.58, 91.5, "91,5", "t"), (2013.25, 119.2, "119,2", "t"), (2013.67, 196, "196", "t"), (2014.08, 209.6, "209,6", "t")], "coral"),
         ("Centro de datos (QSSI)", [(2011.67, 29.9, "29,9", "b"), (2012.75, 48.7, "48,7", "b"), (2013.42, 53.7, "53,7", "b"), (2013.67, 84.5, "84,5", "b")], "navy")],
        x_label="Fecha de la modificación del contrato", y_label="Millones de dólares de EE. UU. obligados",
        x_ticks=x_ticks, y_ticks=[0, 50, 100, 150, 200, 250], point_labels="all", plot_h=300,
        note="El FFM casi se cuadruplicó y el centro de datos casi se triplicó. GAO atribuye el aumento principalmente a requisitos nuevos o cambiantes agravados por supervisión inconsistente. Los valores son obligaciones (dinero comprometido), no gasto ejecutado ni coste final del sitio.",
        note_kind="gold", foot=GAO14 + " Figura 4 y texto; el eje horizontal sitúa cada fecha con su fracción del año.")


# ------------------------------------------------------------------ 5. inicial frente a final
def antes_despues() -> Fig:
    return dumbbell(
        "Lo comprometido al inicio frente a lo comprometido después",
        "Puntos huecos y rellenos con la obligación inicial y la final para tres contratos: FFM de 55,7 a 209,6 millones; centro de datos de 29,9 a 84,5; y el contrato de Accenture de 91 en enero de 2014 a más de 175 en junio de 2014.",
        [("FFM: de septiembre de 2011 a febrero de 2014", 55.7, 209.6), ("Centro de datos: septiembre de 2011 a septiembre de 2013", 29.9, 84.5), ("Contrato Accenture: enero a junio de 2014", 91, 175)],
        unit="Millones de dólares de EE. UU.", names=("Inicial", "Después"), lower_is_better=True,
        delta=lambda a, b: f"×{b / a:.1f}".replace(".", ","),
        label_w=330,
        note="Los tres aumentos ocurren en tramos distintos y por razones que GAO describe: requisitos cambiantes y retrabajo (FFM y centro de datos), y nuevos requisitos y mejoras (Accenture, cuyo coste pasó de 91 a más de 175 a junio de 2014, con capacidades clave aún no disponibles). El factor es aritmética propia; el 175 es un «más de» de GAO.",
        note_kind="gold", foot=GAO14)


# ------------------------------------------------------------------ 6. mejoras
def mejoras() -> Fig:
    return case_cards(
        "Cinco decisiones del caso y la mejora que las habría cambiado",
        "Cinco tarjetas con una situación documentada a la izquierda y la mejora propuesta a la derecha: congelar un alcance mínimo, dar criterios de salida de la revisión de preparación, pruebas de carga y de extremo a extremo, cadena de malas noticias y lanzamiento escalonado.",
        [("Requisitos todavía cambiando en mitad de 2013, con plazos fijos", "Alcance mínimo congelado y lo demás en olas posteriores", "Es la causa que GAO atribuye al aumento de coste y a la compresión de pruebas.", "teal"),
         ("Revisión de preparación parcial en septiembre de 2013, con el desarrollo sin terminar", "Criterio de salida explícito: sin pruebas superadas, no hay lanzamiento", "GAO: se lanzó sin verificar que cumplía los requisitos de rendimiento.", "teal"),
         ("Demanda subestimada y sin plan de capacidad", "Prueba de carga con un rango de demanda y capacidad elástica", "GAO-15-238: CMS reconoció haber subestimado la demanda.", "teal"),
         ("Sin pruebas de extremo a extremo del conjunto", "Una prueba de extremo a extremo del recorrido crítico antes de abrir", "GAO-15-238: no se hicieron aunque estaban requeridas.", "teal"),
         ("Resistencia a las malas noticias y plazo inamovible", "Lanzamiento por fases o regiones con un canal de alerta sin castigo", "OEI-06-14-00350: no se reconoció la magnitud de los problemas ni se cambió de plan.", "teal")],
        note=ANALISIS, note_kind="teal", foot="", left=0.46)


FIGURES = {
    "healthcare-gov-contexto.svg": contexto,
    "healthcare-gov-recorrido-y-modulos.svg": flujo,
    "healthcare-gov-linea-de-tiempo.svg": tiempos,
    "healthcare-gov-obligaciones.svg": obligaciones,
    "healthcare-gov-inicial-y-despues.svg": antes_despues,
    "healthcare-gov-mejoras.svg": mejoras,
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
