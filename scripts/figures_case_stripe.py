"""Figuras del caso de estudio Stripe (casos/exito/stripe.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Los SVG se escriben en casos/figures/ (``python scripts/figures_case_stripe.py``).
"""
from __future__ import annotations

import sys
from pathlib import Path

from figure_kit import Fig, grouped_bars, line_chart, timeline

PRECIOS = "Fuente: stripe.com/pricing, tarifa estándar (consulta 2026-11-16). Cálculo propio."


def _head(f: Fig, text: str) -> None:
    f.text(14, 27, text, 15, "start", 700, "#142231")


def _note(f: Fig, y: float, text: str, kind: str = "gold", lines: int = 3) -> float:
    h = 26 + lines * 16.6
    f.box(10, y, f.width - 20, h, text, kind, 13)
    return y + h


def _foot(f: Fig, y: float, text: str) -> None:
    f.text(f.width / 2, y + 22, text, 12, "middle", 400, "#5c1f14")
    f.height = int(y + 36)


# ---------------------------------------------------------------- 1. contexto
def contexto() -> Fig:
    f = Fig(940, 0, "Stripe entre el comercio, el cliente y el sistema financiero",
            "Diagrama de contexto: el comercio integra la API de Stripe; el cliente paga con tarjeta o billetera; Stripe se coloca entre ambos y dialoga con las redes de tarjetas, los bancos emisores y los adquirentes, y cumple la normativa de pagos y de datos de tarjeta; el comercio recibe el neto menos la comisión.")
    _head(f, "Stripe entre el comercio, el cliente y el sistema financiero")
    f.box(20, 70, 210, 80, "Comercio o plataforma\n(desarrolladores)", "teal", 13)
    f.box(335, 70, 270, 80, "Stripe\nAPI · pagos · fraude ·\ncobro recurrente · pagos a terceros", "navy", 13, bold=True)
    f.box(710, 70, 210, 80, "Redes de tarjetas,\nbancos emisores y\nadquirentes", "grey", 13)
    f.box(20, 215, 210, 70, "Cliente final\n(tarjeta o billetera)", "gold", 13)
    f.box(710, 215, 210, 70, "Reguladores\n(PCI DSS, autenticación\nfuerte, dinero electrónico)", "coral", 13)
    f.arrow([(230, 110), (335, 110)], "integra la API", label_at=(283, 98))
    f.arrow([(605, 110), (710, 110)], "autoriza y liquida", label_at=(657, 98))
    f.arrow([(125, 215), (125, 150)], "paga", label_at=(150, 190))
    f.arrow([(710, 250), (560, 150)], dashed=True)
    y = _note(f, 310, "Lectura: Stripe vende abstracción. El comercio nunca habla con las redes de tarjetas; habla con una API estable y Stripe asume las conexiones, el cumplimiento y parte del fraude. Documentado: certificación PCI nivel 1 de proveedor de servicios; Stripe.js tokeniza los datos de tarjeta sin que toquen el servidor del comercio. Dónde deja de valer: Stripe no es la red de tarjetas ni el banco; sigue sujeto a sus reglas y a sus costos (interchange).", "gold", 6)
    _foot(f, y + 6, "Fuentes: docs.stripe.com/security y /payments/elements (consulta 2026-11-16). Esquema del autor.")
    return f


# ---------------------------------------------------------------- 2. componentes
def componentes() -> Fig:
    f = Fig(940, 0, "Piezas de Stripe documentadas en su ingeniería y sus docs",
            "Diagrama de componentes: clientes de la API con una clave de idempotencia y una versión fija por cuenta; capa de límites de tasa y de descarte de carga; servicios de producto; una base de documentos propia (DocDB, sobre MongoDB) con más de 2.000 shards y más de 5 millones de consultas por segundo; y webhooks hacia el comercio con reintentos de hasta tres días.")
    _head(f, "Piezas de Stripe documentadas en su ingeniería y sus docs")
    f.box(20, 60, 170, 80, "Clientes de la API\n(clave de\nidempotencia)", "teal", 13)
    f.box(240, 60, 200, 80, "Límites de tasa y\ndescarte de carga\n(4 tipos)", "navy", 13)
    f.box(490, 60, 200, 80, "Servicios de producto\n(versión de API\nfijada por cuenta)", "navy", 13)
    f.box(740, 60, 180, 80, "DocDB (MongoDB\npropio): 2.000+\nshards", "coral", 13)
    f.arrow([(190, 100), (240, 100)])
    f.arrow([(440, 100), (490, 100)])
    f.arrow([(690, 100), (740, 100)])
    f.box(490, 200, 200, 80, "Eventos y webhooks\n(reintento hasta\n3 días)", "gold", 13)
    f.box(20, 200, 170, 80, "Stripe.js y Elements\n(tokenizan la\ntarjeta)", "teal", 13)
    f.box(240, 200, 200, 80, "Detalles internos de\nred y despliegue:\nno se sabe", "grey", 13, dashed=True)
    f.arrow([(590, 140), (590, 200)])
    f.arrow([(105, 200), (105, 140)], dashed=True)
    f.box(740, 200, 180, 80, "Comercio recibe el\nevento (firmado)", "teal", 13)
    f.arrow([(690, 240), (740, 240)])
    y = _note(f, 305, "Lectura: la columna vertebral documentada es contrato estable (versionado por fecha), seguridad ante duplicados (idempotencia) y protección de la capacidad (límites). No se sabe cómo se despliega ni cómo se conecta con cada red de pagos. Dónde deja de valer: DocDB y los límites se describen en posts de 2017 a 2024; el estado actual puede diferir.", "gold", 4)
    _foot(f, y + 6, "Fuentes: blog de Stripe (idempotencia, límites de tasa, versionado 2017; DocDB 2024); docs de webhooks y de versionado.")
    return f


# ---------------------------------------------------------------- 3. flujo de un cobro
def flujo_cobro() -> Fig:
    f = Fig(940, 0, "Un cobro de extremo a extremo: tokenizar, crear la intención, confirmar y escuchar el resultado",
            "Flujo documentado de un cobro con Stripe: el navegador tokeniza la tarjeta con Elements, el servidor del comercio crea un PaymentIntent con clave de idempotencia, el cliente confirma y, si se exige, completa la autenticación; Stripe emite eventos por webhook que el comercio procesa una sola vez registrando los identificadores de evento.")
    _head(f, "Un cobro de extremo a extremo: tokenizar, crear la intención, confirmar y escuchar el resultado")
    xs = [20, 200, 380, 560, 740]
    labels = [("1. Cliente teclea\nen un Element\n(se tokeniza)", "teal"), ("2. Servidor crea\nPaymentIntent\n(Idempotency-Key)", "navy"),
              ("3. Cliente confirma;\nautenticación fuerte\nsi se exige", "navy"), ("4. Stripe autoriza\ncon la red y el\nemisor", "grey"), ("5. Webhook al\ncomercio (evento\nfirmado)", "gold")]
    for x, (t, k) in zip(xs, labels):
        f.box(x, 60, 160, 90, t, k, 13)
    for a, b in zip(xs, xs[1:]):
        f.arrow([(a + 160, 105), (b, 105)])
    f.box(200, 200, 160, 70, "Reintento con la\nmisma clave: sin\ndoble cobro", "coral", 13)
    f.arrow([(280, 150), (280, 200)], dashed=True)
    f.box(740, 200, 160, 70, "Procesar una sola\nvez: guardar el\nid del evento", "teal", 13, bold=True)
    f.arrow([(820, 150), (820, 200)])
    f.box(380, 200, 340, 70, "Si el webhook falla, Stripe reintenta hasta\ntres días con espera exponencial (modo real)", "grey", 13)
    y = _note(f, 295, "Lectura: hay dos mecanismos de seguridad contra duplicados, uno en cada sentido: la clave de idempotencia protege la petición del comercio hacia Stripe y el registro de identificadores protege el evento de Stripe hacia el comercio. Dónde deja de valer: los eventos pueden llegar desordenados, por lo que no deben usarse como secuencia estricta; aquí se ha simplificado el flujo de pagos que requiere redirecciones.", "gold", 5)
    _foot(f, y + 6, "Fuentes: docs.stripe.com (payment intents, webhooks, idempotent requests); blog de Stripe sobre idempotencia (2017).")
    return f


# ---------------------------------------------------------------- 4. línea de tiempo
def linea_tiempo() -> Fig:
    return timeline(
        "Stripe: de una API para desarrolladores a infraestructura financiera",
        "Línea de tiempo de 2010 a 2026: origen entre 2009 y 2010 según la fuente, beta privada y lanzamiento público en septiembre de 2011, artículos de ingeniería sobre idempotencia, límites y versionado en 2017, y volumen de pagos de 1,0 billones de dólares en 2023, 1,4 en 2024 y 1,9 en 2025.",
        [("Etapa", [(2010, 2011.7, "Beta", "grey"), (2011.7, 2017, "API para desarrolladores", "teal"), (2017, 2023, "Plataforma amplia", "gold"), (2023, 2026, "Escala", "navy")]),
         ("Volumen (billones USD)", [(2023, 2024, "1,0", "teal"), (2024, 2025, "1,4", "gold"), (2025, 2026, "1,9", "coral")])],
        unit="Año", events=[(2011.7, "Lanzamiento")], t_max=2026, ticks=[2010, 2014, 2018, 2022, 2026], lane_h=54, label_w=160,
        note="Documentado por Stripe: 1 billón de dólares de volumen en 2023 (blog de DocDB), 1,4 billones en 2024 (+38 %) y 1,9 billones en 2025 (+34 %) según sus cartas anuales; un billón aquí es 10^12. Fuente secundaria: lanzamiento público del 29 de septiembre de 2011 y origen entre 2009 y 2010 (las fuentes discrepan). Dónde deja de valer: volumen no es ingreso de Stripe, solo el dinero que pasa por la plataforma.",
        note_kind="gold", foot="Fuentes: Stripe Newsroom (2024, 2025); blog de Stripe (2024); Wikipedia (fechas secundarias).")


# ---------------------------------------------------------------- 5. volumen
def volumen() -> Fig:
    return grouped_bars(
        "Volumen total de pagos procesado por Stripe (billones de dólares, 10^12)",
        "Barras con el volumen de pagos que pasa por Stripe: 1,0 billones de dólares en 2023, 1,4 en 2024 (38 por ciento más) y 1,9 en 2025 (34 por ciento más); cada año se añaden cantidades mayores en términos absolutos aunque el porcentaje baje.",
        ["2023", "2024", "2025"], [("Volumen total de pagos", [1.0, 1.4, 1.9], "teal")],
        unit="Billones de dólares (10^12)", decimals=1,
        note="El crecimiento porcentual baja (38 % y 34 %) pero el aumento absoluto sube de 0,4 a 0,5 billones, y en 2025 equivale a cerca del 1,6 % del PIB mundial según Stripe. Dónde deja de valer: es volumen bruto, no ingreso; Stripe no publica ingresos, y la cifra de 2023 viene de un blog de ingeniería, no de una carta anual.",
        note_kind="gold", foot="Fuentes: Stripe Newsroom 2024 y 2025; blog de ingeniería de Stripe (6-jun-2024).")


# ---------------------------------------------------------------- 6. tarifa efectiva
def tarifa_efectiva() -> Fig:
    amounts = [10, 25, 50, 100, 250, 500, 1000]

    def rate(extra: float) -> list[tuple]:
        out = []
        for a in amounts:
            v = round((0.029 + extra) * 100 + 30 / a, 2)
            lab = f"{v:.1f}".replace(".", ",") + " %" if a in (10, 1000) else ""
            out.append((a, v, lab, "t" if a == 10 else "b" if extra == 0 else "t"))
        return out

    return line_chart(
        "Costo efectivo de la tarifa estándar de Stripe según el monto cobrado",
        "Líneas de costo efectivo en porcentaje frente al monto del cobro, con eje horizontal logarítmico: con tarjeta nacional una venta de 10 dólares paga 5,9 por ciento y una de 1.000 dólares paga 2,9; con tarjeta internacional se suma 1,5 puntos y con conversión de moneda otro punto, de modo que la tarifa fija de 30 centavos pesa mucho en los montos pequeños.",
        [("Tarjeta nacional (2,9 % + 30 ¢)", rate(0.0), "teal"), ("Internacional (+1,5 %)", rate(0.015), "gold"), ("Internacional con conversión (+1 %)", rate(0.025), "coral")],
        x_label="Monto del cobro (USD)", y_label="Costo efectivo (% del monto)", log_x=True,
        x_ticks=[(10, "10"), (25, "25"), (50, "50"), (100, "100"), (250, "250"), (500, "500"), (1000, "1.000")],
        y_ticks=[0, 2, 4, 6, 8, 10], decimals=1, point_labels="none",
        note="Cálculo del autor con la tarifa pública estándar para tarjetas (2,9 % + 30 ¢ nacional, +1,5 % internacional, +1 % si hay conversión). La parte fija domina los montos pequeños y el porcentaje converge al 2,9 % en los grandes. Dónde deja de valer: los acuerdos personalizados (IC+, descuentos por volumen) y otros métodos de pago tienen otras tarifas, y el precio varía por país y cambia con el tiempo.",
        note_kind="gold", foot=PRECIOS)


FIGURES = {
    "stripe-contexto-intermediario.svg": contexto,
    "stripe-componentes-documentados.svg": componentes,
    "stripe-flujo-de-un-cobro.svg": flujo_cobro,
    "stripe-linea-de-tiempo.svg": linea_tiempo,
    "stripe-volumen-de-pagos.svg": volumen,
    "stripe-tarifa-efectiva.svg": tarifa_efectiva,
}


def main() -> int:
    out = Path(__file__).resolve().parents[1] / "casos" / "figures"
    out.mkdir(parents=True, exist_ok=True)
    for name, builder in FIGURES.items():
        (out / name).write_text(builder().svg(), encoding="utf-8", newline="\n")
    print(f"CASE_FIGURES_OK: {len(FIGURES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
