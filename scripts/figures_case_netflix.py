"""Figures for the Netflix success case (casos/exito/netflix.md).

Every number comes from a source cited in the case page: the Netflix Q4 2024 earnings
8-K, the 2016 and 2007 annual reports, Netflix's own timeline page and its engineering
blog. Architecture diagrams are labelled as documented or inferred.
"""
from __future__ import annotations

import re

from figure_kit import (Fig, _wrap, fmt_es, grouped_bars, line_chart, stacked_bars, timeline)

DOC = "Fuente: documentos públicos de Netflix citados en la página del caso. Consulta: 16 de noviembre de 2026."
INF = "Esquema pedagógico: las cajas punteadas son inferencia del curso, no arquitectura confirmada por Netflix."


def _years(fig: Fig) -> Fig:
    """The kit groups thousands with a space; a year is not a quantity, so join them again."""
    fig.parts = [re.sub(r">([12]) (\d{3})<", r">\g<1>\g<2><", p) for p in fig.parts]
    return fig


def _canvas(title: str, desc: str, width: int, height: int) -> Fig:
    f = Fig(width, height, title, desc)
    for i, line in enumerate(_wrap(title, 15, width - 28)):
        f.text(14, 27 + i * 19, line, 15, "start", 700, "#142231")
    return f


def _foot(f: Fig, y: float, note: str, foot: str, kind: str = "gold") -> Fig:
    lines = len(_wrap(note, 13, f.width - 40))
    h = max(54, lines * 13 * 1.28 + 26)
    f.box(10, y, f.width - 20, h, note, kind, 13)
    f.text(f.width / 2, y + h + 20, foot, 12, "middle", 400, "#5c1f14")
    f.height = int(y + h + 34)
    return f


def contexto() -> Fig:
    f = _canvas("Quién habla con quién cuando alguien pulsa «Reproducir» en Netflix",
                "Diagrama de contexto: el miembro usa un dispositivo; las llamadas de control (catálogo, perfil, licencia) van a servicios en la nube de AWS y los bytes del vídeo llegan desde servidores Open Connect colocados dentro de la red del proveedor de internet; los estudios y el pipeline de codificación abastecen esos servidores fuera de las horas pico.",
                940, 0)
    f.group(10, 52, 250, 250, "Casa del miembro", "grey")
    f.box(30, 90, 210, 54, "Televisor, móvil, navegador o consola", "plain", 13)
    f.box(30, 160, 210, 54, "Aplicación Netflix: perfil, descargas, reproductor", "plain", 13)
    f.box(30, 230, 210, 54, "Miembro con plan (con o sin anuncios)", "teal", 13)
    f.group(300, 52, 300, 118, "Red del proveedor de internet (ISP)", "gold")
    f.box(320, 88, 260, 66, "Appliance Open Connect: guarda copias de títulos y sirve el vídeo", "gold", 13)
    f.group(300, 190, 630, 112, "Nube (AWS) y equipo de Netflix", "navy")
    f.box(320, 226, 180, 62, "API y servicios de control: catálogo, cuenta, facturación", "plain", 13)
    f.box(520, 226, 190, 62, "Recomendación y telemetría de uso", "plain", 13)
    f.box(730, 226, 180, 62, "Pipeline de codificación de vídeo", "plain", 13)
    f.group(630, 52, 300, 118, "Contenido", "grey")
    f.box(650, 88, 260, 66, "Estudios y producciones propias entregan el original", "plain", 13)
    f.arrow([(240, 187), (300, 130)])
    f.arrow([(240, 258), (320, 258)])
    f.arrow([(820, 154), (820, 226)])
    f.arrow([(730, 258), (580, 130)], dashed=True)
    f.text(250, 172, "vídeo", 13, "start", 700, "#142231", halo=True)
    f.text(252, 276, "control", 13, "start", 700, "#142231", halo=True)
    f.text(830, 194, "original", 13, "start", 700, "#142231", halo=True)
    f.text(675, 200, "copias previas", 13, "middle", 700, "#142231", halo=True)
    return _foot(f, 320, "Lo documentado es la separación de dos caminos: los servicios de control corren en AWS (carta de 2016) y el vídeo sale de una red propia, Open Connect (informe anual de 2016). La flecha punteada resume que Open Connect se rellena con antelación; el detalle del reparto lo publica Netflix en su sitio de Open Connect.",
                 DOC)


def componentes() -> Fig:
    f = _canvas("Capas de resiliencia que Netflix describió en su blog (2011-2016)",
                "Diagrama por capas de la plataforma de control: una puerta de entrada que reparte tráfico entre regiones, servicios que envuelven cada dependencia con un interruptor y una respuesta alternativa, cachés y bases de datos replicadas entre regiones, y herramientas que apagan instancias a propósito para comprobar que nada se rompe.",
                940, 0)
    rows = [
        ("Puerta de entrada", "Zuul 2: filtros asíncronos y no bloqueantes que dirigen el tráfico, y DNS que mueve usuarios entre regiones", "teal"),
        ("Servicios", "Cada llamada a una dependencia se envuelve con medición de fallos, interruptor y respuesta alternativa (Hystrix)", "plain"),
        ("Datos y caché", "EVCache (memcached en RAM) y Cassandra replicada entre regiones; el estado vive fuera de los servicios", "plain"),
        ("Verificación", "Chaos Monkey apaga instancias en producción; el chaos engineering formaliza el experimento", "coral"),
    ]
    y = 52.0
    for name, text, kind in rows:
        f.box(10, y, 190, 64, name, "navy", 14, bold=True)
        f.box(212, y, 718, 64, text, kind, 13)
        y += 80
    f.arrow([(105, 116), (105, 132)])
    f.arrow([(105, 196), (105, 212)])
    f.arrow([(105, 276), (105, 292)])
    return _foot(f, y + 6, "Todo lo dibujado aparece en artículos del blog técnico de Netflix; el orden por capas es una simplificación del curso. Cuántos servicios hay, cómo se agrupan hoy y qué ha sustituido a cada herramienta no está en estas fuentes, y el blog advierte que sus entradas retratan un momento concreto.",
                 DOC)


def flujo() -> Fig:
    f = _canvas("De la pulsación a la imagen: la operación crítica separada en control y datos",
                "Diagrama de flujo en seis pasos: el cliente pide reproducir, un servicio de control comprueba cuenta y plan, devuelve una lista de servidores Open Connect y un manifiesto, el reproductor descarga segmentos del servidor más cercano, mide el ancho de banda y cambia de calidad, y envía telemetría de vuelta a la nube.",
                940, 0)
    steps = [
        ("1. Cliente", "Pulsar «Reproducir» en un perfil", "plain", False),
        ("2. Control en AWS", "Comprobar cuenta, plan y derechos del título", "navy", False),
        ("3. Selección", "Devolver servidores candidatos y manifiesto", "navy", True),
        ("4. Open Connect", "Entregar segmentos de vídeo cifrados", "gold", False),
        ("5. Reproductor", "Medir ancho de banda y cambiar de calidad", "plain", True),
        ("6. Telemetría", "Enviar eventos de reproducción a la nube", "teal", True),
    ]
    w, gap = 134, 22
    x = 10.0
    for i, (head, body, kind, inferred) in enumerate(steps):
        f.box(x, 66, w, 38, head, kind, 13, bold=True)
        f.box(x, 112, w, 118, body, "plain", 13, dashed=inferred)
        if i:
            f.arrow([(x - gap, 85), (x, 85)])
        x += w + gap
    f.text(14, 262, "Trazo continuo: respaldado por fuentes citadas. Trazo punteado: inferido a partir de ellas.", 13, "start", 400, "#32505f")
    return _foot(f, 280, "Se documenta públicamente que existen un reproductor adaptativo, un plano de control en la nube y servidores propios dentro de los ISP. Los pasos 3, 5 y 6 se describen aquí por inferencia pedagógica: Netflix no publica el protocolo de reproducción completo ni los nombres de sus servicios actuales.",
                 INF, "coral")


def linea() -> Fig:
    return _years(timeline(
        "Dos historias que se cruzan: producto y plataforma (1997-2025)",
        "Línea de tiempo con dos carriles. En producto, el DVD por correo domina hasta 2007, el streaming nace ese año, los originales empiezan en 2013, el plan con anuncios llega en 2022 y la emisión en directo en 2023. En plataforma, un fallo de base de datos en 2008 inicia la migración a la nube, que termina en enero de 2016; Open Connect se lanza en 2012.",
        [("Producto", [(1998, 2007, "DVD por correo", "grey"), (2007, 2022, "Streaming por suscripción", "teal"), (2022, 2026, "Ads, directo", "gold")]),
         ("Plataforma", [(2008, 2016, "Migración a la nube", "navy"), (2016, 2026, "Nube y OCA", "coral")])],
        unit="Año", events=[(2008, "Fallo de BD"), (2012, "Open Connect"), (2016, "Nube completa")],
        ticks=[1997, 2002, 2007, 2012, 2017, 2022, 2026], t_max=2026, lane_h=58, label_w=120,
        note="Los dos carriles se solapan en 2007-2016: Netflix vendió streaming mientras seguía moviendo su plataforma fuera de sus centros de datos. Los años salen de la cronología oficial de Netflix y de su carta de 2016; el ancho de cada barra es una simplificación visual, no una medida de ingresos.",
        note_kind="gold", foot=DOC))


def miembros() -> Fig:
    pts = [(2003, 1, "1", "t"), (2006, 5, "5", "t"), (2012, 25, "25", "t"), (2014, 50, "50", "t"), (2016, 93, "93", "t"),
           (2017, 100, "100", "t"), (2021, 200, "200", "t"), (2024, 301.6, "301,6", "t")]
    return line_chart(
        "Miembros de pago de Netflix por año (millones)",
        "Línea con ocho puntos: 1 millón en 2003, 5 en 2006, 25 en 2012, 50 en 2014, 93 en 2016, 100 en 2017, 200 en 2021 y 301,6 millones al cierre de 2024; el crecimiento no es lineal y la pendiente cambia tras 2016, cuando el servicio llegó a más de 190 países.",
        [("Miembros de pago", pts, "teal")], x_label="Año del hito citado o del cierre", y_label="Millones de miembros",
        x_ticks=[(2003, "2003"), (2006, "2006"), (2009, "2009"), (2012, "2012"), (2015, "2015"), (2018, "2018"), (2021, "2021"), (2024, "2024")],
        vlines=[(2016, "2016: 130 países nuevos")], plot_h=300,
        note="Las cifras de 2003 a 2021 proceden de la cronología oficial de Netflix, el 93 de 2016 de su informe anual y el 301,6 del cierre de 2024 de su carta a accionistas. Netflix dejó de publicar el número trimestral de miembros desde el primer trimestre de 2025: no existe un dato oficial regular posterior. Los puntos no son anuales completos, por lo que la línea une datos dispersos.",
        note_kind="gold", foot=DOC)


def gastos() -> Fig:
    return stacked_bars(
        "Dónde va cada dólar de ingresos de Netflix (2023 y 2024, miles de millones de USD)",
        "Barras apiladas al 100 por ciento para 2023 y 2024: el coste de los ingresos pasa de 19,7 a 21,0 miles de millones, marketing más tecnología y desarrollo de 5,3 a 5,8, administración estable en 1,7 y el resultado operativo de 7,0 a 10,4, de modo que el margen sube de 21 a 27 por ciento.",
        ["2023 (ingresos 33,7)", "2024 (ingresos 39,0)"],
        [("Coste de los ingresos", [19.72, 21.04], "navy"), ("Marketing + tecnología y desarrollo", [5.33, 5.84], "teal"),
         ("Administración", [1.72, 1.70], "grey"), ("Resultado operativo", [6.95, 10.42], "gold")],
        unit="% de los ingresos", percent=True, horizontal=True, decimals=1, label_w=190,
        note="La mejora de margen viene de que los ingresos crecieron 16 por ciento y el coste de los ingresos solo 7 por ciento. «Marketing + tecnología y desarrollo» agrupa dos líneas del estado de resultados. No se conoce el reparto interno entre infraestructura y contenido.",
        note_kind="gold", foot="Fuente: Netflix, Q4'24 Earnings 8-K (estado de resultados). Consulta: 16 de noviembre de 2026.")


FIGURES = {
    "netflix-contexto.svg": contexto,
    "netflix-capas-de-resiliencia.svg": componentes,
    "netflix-flujo-de-reproduccion.svg": flujo,
    "netflix-linea-de-tiempo.svg": linea,
    "netflix-miembros-de-pago.svg": miembros,
    "netflix-de-donde-sale-el-margen.svg": gastos,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
