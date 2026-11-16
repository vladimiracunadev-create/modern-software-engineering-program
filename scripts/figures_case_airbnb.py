"""Figuras del caso de estudio Airbnb (casos/exito/airbnb.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Los SVG se escriben en casos/figures/ (``python scripts/figures_case_airbnb.py``).
"""
from __future__ import annotations

import sys
from pathlib import Path

from figure_kit import Fig, stacked_bars, timeline

AYUDA = "Cifras: página de ayuda de comisiones de Airbnb (consulta 2026-11-16)."


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
    f = Fig(940, 0, "Airbnb: un mercado donde la confianza entre desconocidos es el producto",
            "Diagrama de contexto: los huéspedes buscan y pagan, los anfitriones publican y reciben el pago, Airbnb cobra una comisión, protege la transacción y gestiona reseñas; las ciudades y los reguladores fijan reglas locales sobre el alquiler de corta duración.")
    _head(f, "Airbnb: un mercado donde la confianza entre desconocidos es el producto")
    f.box(20, 70, 210, 80, "Huéspedes\n(buscan, reservan, pagan)", "teal", 13)
    f.box(710, 70, 210, 80, "Anfitriones\n(publican, aceptan, cobran)", "gold", 13)
    f.box(335, 55, 270, 110, "Airbnb\nbúsqueda · pagos ·\nreseñas · soporte · AirCover", "navy", 13, bold=True)
    f.box(335, 230, 270, 70, "Ciudades y reguladores\n(registro, límites, impuestos)", "coral", 13)
    f.box(20, 230, 210, 70, "Cobertura y soporte\n(AirCover, reembolsos)", "grey", 13)
    f.box(710, 230, 210, 70, "Pagos en más de\n40 monedas (2019)", "grey", 13)
    f.arrow([(230, 110), (335, 110)], "reserva", label_at=(283, 100))
    f.arrow([(605, 110), (710, 110)], "cobro neto", label_at=(657, 100))
    f.arrow([(470, 230), (470, 165)], "reglas locales", label_at=(555, 205))
    f.arrow([(335, 150), (230, 245)], dashed=True)
    f.arrow([(605, 150), (710, 245)], dashed=True)
    y = _note(f, 325, "Lectura: el producto no es el alojamiento sino la reducción de la incertidumbre entre dos desconocidos, y eso explica por qué la reseña, el pago retenido y la cobertura son piezas centrales. Documentado (2026): 9 millones de anuncios activos, 5,5 millones de anfitriones, más de 220 países y regiones, 2.500 millones de llegadas acumuladas. Dónde deja de valer: el mapa no muestra cuánto de la actividad es profesional y cuánto es ocasional.", "gold", 5)
    _foot(f, y + 6, "Fuente: Airbnb Newsroom, «Sobre nosotros» (actualizado mayo de 2026, consulta 2026-11-16).")
    return f


# ---------------------------------------------------------------- 2. componentes
def componentes() -> Fig:
    f = Fig(940, 0, "De un monolito Rails a servicios: lo que Airbnb ha documentado",
            "Diagrama de componentes basado en blogs de ingeniería de Airbnb: un monolito Rails original que se va troceando en servicios con interfaz definida en Thrift; búsqueda con aprendizaje profundo para ordenar resultados; y un orquestador de pagos con flujos de pasos idempotentes y reintentables apoyado en la biblioteca Orpheus.")
    _head(f, "De un monolito Rails a servicios: lo que Airbnb ha documentado")
    f.box(20, 60, 190, 80, "Monolito Rails\n(origen)", "grey", 13)
    f.box(270, 60, 200, 80, "Servicios con IDL\nThrift (migración\ndesde 2017)", "navy", 13)
    f.arrow([(210, 100), (270, 100)], "se trocea", label_at=(240, 88))
    f.box(530, 60, 190, 80, "Búsqueda y\nranking (modelos\nde aprendizaje)", "teal", 13)
    f.box(750, 60, 170, 80, "Pagos:\norquestador +\nOrpheus", "gold", 13)
    f.arrow([(470, 90), (530, 90)])
    f.arrow([(370, 140), (370, 168), (835, 168), (835, 140)], dashed=True)
    f.group(30, 190, 880, 100, "Dentro de pagos (documentado, 2019 y 2022)", "grey")
    f.box(50, 225, 190, 50, "Clave de idempotencia", "plain", 13)
    f.box(270, 225, 190, 50, "Flujo = grafo de pasos", "plain", 13)
    f.box(490, 225, 200, 50, "Base maestra fragmentada", "plain", 13)
    f.box(720, 225, 170, 50, "Datos inmutables", "plain", 13)
    y = _note(f, 315, "Lectura: lo documentado es el patrón (separar en servicios, definir contratos, hacer los pasos de dinero idempotentes), no el mapa completo. No se sabe cuántos servicios existen hoy, ni cómo se reparte la búsqueda por regiones. Dónde deja de valer: los blogs son de 2017 a 2022; el orquestador actual puede haber evolucionado.", "gold", 4)
    _foot(f, y + 6, "Fuentes: Airbnb Tech Blog (Building Services 2017; Avoiding Double Payments 2019; Rebuilding Payment Orchestration 2022); arXiv:1810.09591.")
    return f


# ---------------------------------------------------------------- 3. flujo: reserva idempotente
def flujo_pago() -> Fig:
    f = Fig(940, 0, "Cobrar una reserva sin cobrarla dos veces",
            "Flujo del pago idempotente descrito por Airbnb: el cliente envía una clave de idempotencia, el servidor registra la solicitud en la base maestra, ejecuta los pasos y guarda la respuesta; si hay un corte y se reintenta con la misma clave, devuelve el resultado guardado en lugar de cobrar de nuevo; leer de una réplica podría duplicar el cobro por el retraso de replicación.")
    _head(f, "Cobrar una reserva sin cobrarla dos veces")
    f.box(20, 60, 170, 80, "Huésped confirma\nla reserva", "teal", 13)
    f.box(240, 60, 180, 80, "Solicitud con\nclave de\nidempotencia", "navy", 13)
    f.box(470, 60, 200, 80, "Registro en la base\nmaestra y ejecución\ndel cobro", "navy", 13)
    f.box(720, 60, 200, 80, "Respuesta guardada\n(éxito o error)", "teal", 13)
    f.arrow([(190, 100), (240, 100)])
    f.arrow([(420, 100), (470, 100)])
    f.arrow([(670, 100), (720, 100)])
    f.box(240, 200, 180, 80, "Corte de red:\nel cliente reintenta\ncon la misma clave", "coral", 13)
    f.box(470, 200, 200, 80, "El servidor encuentra\nla clave y devuelve\nla respuesta guardada", "gold", 13, bold=True)
    f.arrow([(330, 140), (330, 200)], "falla la respuesta", label_at=(430, 178))
    f.arrow([(420, 240), (470, 240)])
    f.box(720, 200, 200, 80, "Importante: leer solo\nde la base maestra,\nno de una réplica", "grey", 13)
    f.arrow([(670, 240), (720, 240)], dashed=True)
    y = _note(f, 305, "Lectura: la clave convierte un cobro, que es peligroso de repetir, en una operación que se puede repetir sin cambiar el resultado. El blog documenta el caso límite: con una réplica retrasada la clave podía no verse y se duplicaba el pago, por eso se lee de la base maestra. Dónde deja de valer: cubre duplicados por reintento; no protege contra un cobro lógicamente erróneo ni contra el fraude.", "gold", 5)
    _foot(f, y + 6, "Fuente: «Avoiding Double Payments in a Distributed Payments System», Airbnb Tech Blog (2019). Valores del ejemplo: del autor.")
    return f


# ---------------------------------------------------------------- 4. línea de tiempo
def linea_tiempo() -> Fig:
    return timeline(
        "Airbnb: de colchones inflables a plataforma pública",
        "Línea de tiempo de 2007 a 2026 con los hitos que Airbnb publica en su historia: primeros huéspedes en octubre de 2007, lanzamiento en marzo de 2008, nombre actual en 2009, Garantía para anfitriones en 2012, Experiencias en 2016, salida a bolsa en diciembre de 2020, AirCover en 2021 y servicios adicionales en 2025 y 2026.",
        [("Producto", [(2007.8, 2009.2, "", "teal"), (2009.2, 2016.8, "Alojamiento y confianza", "gold"), (2016.8, 2021, "Experiencias", "navy"), (2021, 2026, "AirCover y servicios", "coral")]),
         ("Empresa", [(2007.8, 2020.9, "Empresa privada", "grey"), (2020.9, 2026, "Cotiza en Nasdaq", "navy")])],
        unit="Año", events=[(2008.2, "Lanzamiento"), (2012.4, "Garantía"), (2020.9, "Bolsa")], t_max=2026, ticks=[2007, 2010, 2013, 2016, 2019, 2022, 2026], lane_h=54, label_w=110,
        note="Documentado en la página «Sobre nosotros» de Airbnb: primeros huéspedes en octubre de 2007, lanzamiento en el SXSW de marzo de 2008 con dos reservas, nombre Airbnb en marzo de 2009, Garantía para anfitriones de 1 millón de dólares en mayo de 2012, salida a bolsa en diciembre de 2020. Las eras del carril de producto son una síntesis del autor. Dónde deja de valer: simplifica; muchos productos conviven.",
        note_kind="gold", foot="Fuente: Airbnb Newsroom, «The Airbnb Story» (consulta 2026-11-16).")


# ---------------------------------------------------------------- 5. comisiones
def comisiones() -> Fig:
    return stacked_bars(
        "Qué parte de una reserva retiene Airbnb con la estructura de comisión dividida (por cada 100 dólares de subtotal)",
        "Barras apiladas por cada 100 dólares de subtotal de reserva: con la comisión dividida, el huésped paga entre 14,1 y 16,5 de comisión y el anfitrión 3, de modo que Airbnb retiene entre 17,1 y 19,5 por cada 100 dólares de subtotal, según el caso.",
        ["Comisión mínima publicada", "Comisión máxima publicada"],
        [("Comisión pagada por el huésped", [14.1, 16.5], "teal"), ("Comisión pagada por el anfitrión", [3.0, 3.0], "gold")],
        unit="Dólares por cada 100 de subtotal", decimals=1,
        note="Los rangos son los que publica la página de ayuda (huésped 14,1 % a 16,5 %; la mayoría de anfitriones 3 %, algunos más). Los totales 17,1 y 19,5 los suma el autor. Airbnb está pasando a todos los anfitriones a una comisión única y esta estructura desaparecerá. Dónde deja de valer: excluye impuestos y tarifas del anfitrión, y el porcentaje real depende de factores que Airbnb no detalla.",
        note_kind="gold", foot=AYUDA)


# ---------------------------------------------------------------- 6. reseñas
def resenas() -> Fig:
    return timeline(
        "Ventana de reseñas: ninguna parte ve la del otro antes de escribir la suya",
        "Línea de tiempo de 14 días tras el check-out: tanto el huésped como el anfitrión pueden escribir su reseña durante la ventana; las reseñas se publican en cuanto ambos han enviado la suya o cuando termina el plazo de 14 días, lo que ocurra primero.",
        [("Huésped", [(0, 14, "Puede escribir su reseña", "teal")]), ("Anfitrión", [(0, 14, "Puede escribir su reseña", "gold")]),
         ("Publicación", [(0, 14, "Ocultas hasta que ambos envían o vence el plazo", "navy")])],
        unit="Días desde el check-out", events=[(0, "Check-out"), (14, "Día 14")], t_max=16, ticks=[0, 4, 8, 12, 16], lane_h=50, label_w=110,
        note="Documentado en la ayuda de Airbnb: plazo de 14 días desde el check-out; las reseñas se publican cuando ambas partes han enviado la suya o cuando termina el plazo, lo que ocurra primero. Mecanismo de diseño: al no ver la reseña ajena antes de escribir la propia se reduce la represalia. Dónde deja de valer: no elimina el sesgo de reseñas inflado; la investigación académica sobre reseñas en Airbnb lo discute y no se reproduce aquí.",
        note_kind="gold", foot="Fuente: Airbnb, ayuda «Cómo funcionan las reseñas» (artículo 13, consulta 2026-11-16).")


FIGURES = {
    "airbnb-contexto-confianza.svg": contexto,
    "airbnb-componentes-servicios.svg": componentes,
    "airbnb-flujo-pago-idempotente.svg": flujo_pago,
    "airbnb-linea-de-tiempo.svg": linea_tiempo,
    "airbnb-comisiones.svg": comisiones,
    "airbnb-ventana-de-resenas.svg": resenas,
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
