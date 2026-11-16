"""Figuras del caso de estudio Spotify (casos/exito/spotify.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Los SVG se escriben en casos/figures/ (``python scripts/figures_case_spotify.py``).
"""
from __future__ import annotations

import sys
from pathlib import Path

from figure_kit import Fig, line_chart, stacked_bars, timeline

Q4 = "Cifras: comunicado de resultados Q4 2025 de Spotify (consulta 2026-11-16)."


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
    f = Fig(940, 0, "Spotify como mercado de dos lados con un tercero que cobra",
            "Diagrama de contexto: los oyentes pagan una suscripción o ven anuncios; los anunciantes pagan por la audiencia gratuita; Spotify reparte una parte mayoritaria de lo que ingresa a titulares de derechos (sellos, editores, artistas independientes y creadores de podcasts).")
    _head(f, "Spotify como mercado de dos lados con un tercero que cobra")
    f.box(20, 70, 220, 80, "Oyentes\nGratis (con anuncios)\no Premium", "teal", 13)
    f.box(20, 215, 220, 70, "Anunciantes\n(audiencia del nivel gratis)", "gold", 13)
    f.box(360, 130, 220, 100, "Spotify\ncatálogo, recomendación,\nreproducción", "navy", 13, bold=True)
    f.box(700, 70, 220, 80, "Titulares de derechos\n(sellos, editores,\nartistas independientes)", "coral", 13)
    f.box(700, 215, 220, 70, "Creadores de podcasts\ny audiolibros", "grey", 13)
    f.arrow([(240, 110), (360, 160)], "suscripción", label_at=(285, 118))
    f.arrow([(240, 250), (360, 205)], "campañas", label_at=(285, 252))
    f.arrow([(580, 160), (700, 115)], "regalías", label_at=(655, 118))
    f.arrow([(700, 250), (580, 205)], "contenido", label_at=(650, 253), dashed=True)
    y = _note(f, 310, "Lectura: Spotify no vende música, vende acceso y descubrimiento, y paga la música a terceros. Documentado: en 2025 los pagos acumulados a titulares de derechos rondaban los 70 mil millones de dólares y más del 60 % de los suscriptores nuevos empezó en el nivel gratuito (Loud & Clear). Inferido: el margen bruto del 33,1 % del trimestre implica que dos tercios de cada euro ingresado se van en costos del ingreso, entre ellos las regalías. Dónde deja de valer: no hay desglose público por tipo de contrato.", "gold", 6)
    _foot(f, y + 6, "Fuentes: Spotify Loud & Clear (2026); comunicado Q4 2025. Esquema del autor.")
    return f


# ---------------------------------------------------------------- 2. componentes
def componentes() -> Fig:
    f = Fig(940, 0, "Piezas públicas de la plataforma de datos y de ingeniería de Spotify",
            "Diagrama de componentes basado en blogs de ingeniería de Spotify: los clientes emiten eventos que se entregan por Google Cloud Pub/Sub, se separan por tipo de evento y alimentan almacenamiento y análisis en BigQuery; la plataforma de experimentación y Backstage cierran el ciclo hacia los equipos; los servicios de reproducción no están descritos en detalle.")
    _head(f, "Piezas públicas de la plataforma de datos y de ingeniería de Spotify")
    f.box(20, 60, 170, 80, "Clientes\n(móvil, escritorio,\nweb)", "teal", 13)
    f.box(240, 60, 190, 80, "Entrega de eventos\n(Pub/Sub, un flujo\npor tipo de evento)", "navy", 13)
    f.box(480, 60, 190, 80, "ETL por horas\n(particiones cerradas\ny definitivas)", "navy", 13)
    f.box(720, 60, 200, 80, "Análisis y modelos\n(BigQuery, Dataproc)", "navy", 13)
    f.arrow([(190, 100), (240, 100)])
    f.arrow([(430, 100), (480, 100)])
    f.arrow([(670, 100), (720, 100)])
    f.box(240, 200, 190, 80, "Plataforma de\nexperimentación\n(sustituyó a ABBA)", "gold", 13)
    f.box(480, 200, 190, 80, "Backstage\n(portal interno,\ncódigo abierto)", "gold", 13)
    f.box(20, 200, 170, 80, "Servicios de\nreproducción y\ncatálogo", "grey", 13, dashed=True)
    f.arrow([(815, 140), (815, 170), (335, 170), (335, 200)])
    f.arrow([(430, 240), (480, 240)], dashed=True)
    f.arrow([(105, 200), (105, 140)], dashed=True)
    f.box(720, 200, 200, 80, "Equipos autónomos\n(escuadras) que\ndeciden con datos", "teal", 13)
    f.arrow([(670, 240), (720, 240)])
    y = _note(f, 305, "Lectura: líneas continuas = documentado en blogs de ingeniería; líneas y cajas discontinuas = no descrito o inferido. Lo documentado es una canalización de datos y herramientas, no el camino de audio. Dónde deja de valer: los blogs son de 2016 a 2021; la infraestructura actual puede haber cambiado y no se sabe cómo se sirven hoy los archivos de audio.", "gold", 4)
    _foot(f, y + 6, "Fuentes: Spotify Engineering (event delivery 2016/2019/2021; experimentación 2020); Google Cloud (2016); docs de Backstage.")
    return f


# ---------------------------------------------------------------- 3. flujo
def flujo_eventos() -> Fig:
    f = Fig(940, 0, "Entrega de eventos: priorizar que el sistema siga vivo sobre que cada dato llegue puntual",
            "Flujo documentado de la entrega de eventos de Spotify: cada tipo de evento tiene su propio flujo y sus particiones horarias; un tipo ruidoso o bloqueado no detiene a los demás, y la partición de una hora se cierra solo cuando está completa, ahí aplica el principio liveness over lateness.")
    _head(f, "Entrega de eventos: priorizar que el sistema siga vivo sobre que cada dato llegue puntual")
    f.box(20, 55, 160, 70, "Evento del\ncliente (p. ej.\nuna reproducción)", "teal", 13)
    f.box(230, 55, 170, 70, "Flujo propio por\ntipo de evento", "navy", 13)
    f.box(450, 55, 220, 70, "Partición horaria\n(p. ej. 13:00–14:00 UTC)", "navy", 13)
    f.box(720, 55, 200, 70, "Cerrada e\ninmutable → ETL", "teal", 13)
    f.arrow([(180, 90), (230, 90)])
    f.arrow([(400, 90), (450, 90)])
    f.arrow([(670, 90), (720, 90)])
    f.box(230, 175, 170, 70, "Tipo roto o\nbloqueado", "coral", 13)
    f.box(450, 175, 220, 70, "Sus particiones\nquedan abiertas", "coral", 13)
    f.arrow([(315, 125), (315, 175)])
    f.arrow([(400, 210), (450, 210)])
    f.box(720, 175, 200, 70, "Los demás tipos\nsiguen entregándose", "gold", 13, bold=True)
    f.arrow([(670, 210), (720, 210)])
    y = _note(f, 270, "Lectura: el aislamiento por tipo convierte un fallo global en uno acotado. Documentado en el blog de 2019: más de 500 tipos de evento, más de 350 TB de datos brutos al día, hasta 8 millones de eventos por segundo en picos y 500 mil millones de eventos diarios en el primer trimestre de 2019. Dónde deja de valer: el coste es que un dato puede llegar tarde o incompleto; sirve para analítica, no para saldos ni para derechos.", "gold", 5)
    _foot(f, y + 6, "Fuente: «Spotify's Event Delivery: Life in the Cloud», Spotify Engineering (2019).")
    return f


# ---------------------------------------------------------------- 4. línea de tiempo
def linea_tiempo() -> Fig:
    return timeline(
        "Spotify: de startup sueca a plataforma de audio",
        "Línea de tiempo de 2006 a 2025: fundación en Estocolmo en 2006, lanzamiento en octubre de 2008 en varios mercados europeos, lanzamiento en Estados Unidos en 2011, migración a Google Cloud desde 2016, salida a bolsa por cotización directa en 2018, audiolibros en 2022 y 751 millones de usuarios activos mensuales a fines de 2025.",
        [("Producto", [(2008, 2015, "Música en streaming", "teal"), (2015, 2022, "Podcasts y descubrimiento", "gold"), (2022, 2026, "Audiolibros", "coral")]),
         ("Plataforma", [(2008, 2016, "Centros de datos propios", "grey"), (2016, 2026, "Google Cloud (datos y servicios)", "navy")])],
        unit="Año", events=[(2006, "Fundación"), (2008, "Lanzamiento"), (2018, "Bolsa")], t_max=2026, ticks=[2006, 2010, 2014, 2018, 2022, 2026], lane_h=54, label_w=130,
        note="Documentado: lanzamiento en 2008 y audiolibros en 2022 (Spotify Newsroom); decisión de ir a Google Cloud en febrero de 2016 (Google Cloud). Fuente secundaria sin verificar con una primaria: fundación en abril de 2006 y cotización directa en 2018. Las eras de producto son una síntesis del autor. Dónde deja de valer: la migración a la nube duró años y no hubo un corte único en 2016.",
        note_kind="gold", foot="Fuentes: Spotify Newsroom (Acerca de); Google Cloud (2016); Wikipedia (fechas secundarias).")


# ---------------------------------------------------------------- 5. usuarios
def usuarios() -> Fig:
    return line_chart(
        "Usuarios de Spotify según cada fuente pública (millones)",
        "Línea con cuatro puntos: más de 75 millones de usuarios en febrero de 2016, 232 millones de usuarios activos mensuales en agosto de 2019, 713 millones en el tercer trimestre de 2025 y 751 millones en el cuarto; el crecimiento más fuerte en cifras absolutas ocurre en la última década.",
        [("Usuarios (definición de cada fuente)", [(2016.1, 75), (2019.6, 232), (2025.8, 713), (2026.0, 751)], "teal")],
        x_label="Año", y_label="Millones de usuarios", x_ticks=[(2016, "2016"), (2018, "2018"), (2020, "2020"), (2022, "2022"), (2024, "2024"), (2026, "2026")],
        y_ticks=[0, 200, 400, 600, 800], decimals=0,
        annotations=[(2016.1, 75, "2016: más de 75 M (Google Cloud)", 30, -60), (2019.6, 232, "2019: 232 M MAU (Spotify Eng.)", -30, -70), (2026.0, 751, "T4 2025: 751 M MAU", -40, 60)],
        note="Los puntos no son comparables al milímetro: 2016 habla de «más de 75 millones de usuarios» (Google Cloud) y los demás de usuarios activos mensuales (MAU). La línea une cuatro observaciones; no mide el crecimiento intermedio. Dónde deja de valer: no sirve para estimar años sin dato.",
        note_kind="gold", foot="Fuentes: Google Cloud (23-feb-2016); Spotify Engineering (2019); comunicados T3 y T4 2025.")


# ---------------------------------------------------------------- 6. composición del ingreso
def margen() -> Fig:
    return stacked_bars(
        "Cuarto trimestre de 2025: qué queda de cada 100 euros de ingreso",
        "Barra apilada al 100 por ciento: con un margen bruto del 33,1 por ciento, 66,9 de cada 100 euros se van en costo de ingresos; de los 33,1 restantes, el resultado operativo de 701 millones sobre unos 4.500 millones de ingresos equivale a unos 15,6 euros y los demás gastos operativos a unos 17,5.",
        ["Ingresos T4 2025"],
        [("Costo de ingresos", [66.9], "coral"), ("Otros gastos operativos (aprox.)", [17.5], "grey"), ("Resultado operativo (aprox.)", [15.6], "teal")],
        unit="Euros por cada 100 de ingreso", percent=True, decimals=1,
        note="Documentado: ingresos de 4.500 millones de euros (redondeado), margen bruto 33,1 % y resultado operativo de 701 millones. Calculado por el autor: 701 / 4.500 = 15,6 %, y 33,1 − 15,6 = 17,5 %, que son gastos de operación; al partir de un ingreso redondeado el reparto es aproximado. Dónde deja de valer: no separa regalías de otros costos del ingreso.",
        note_kind="gold", foot=Q4)


FIGURES = {
    "spotify-contexto-dos-lados.svg": contexto,
    "spotify-componentes-datos-e-ingenieria.svg": componentes,
    "spotify-flujo-entrega-de-eventos.svg": flujo_eventos,
    "spotify-linea-de-tiempo.svg": linea_tiempo,
    "spotify-usuarios.svg": usuarios,
    "spotify-margen-t4-2025.svg": margen,
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
