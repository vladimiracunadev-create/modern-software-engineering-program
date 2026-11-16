"""Figuras del caso de estudio Amazon (casos/exito/amazon.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Los SVG se escriben en casos/figures/ (``python scripts/figures_case_amazon.py``).
Cada cifra rotulada cita su fuente en el pie; lo que es ilustrativo se declara como tal.
"""
from __future__ import annotations

import sys
from pathlib import Path

from figure_kit import Fig, grouped_bars, timeline

DOC = "Cifras: comunicado de resultados Q4 2025 de Amazon (consulta 2026-11-16)."
ILUS = "Esquema ilustrativo del mecanismo descrito en fuentes públicas; no es el diagrama interno de Amazon."


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
    f = Fig(940, 0, "Amazon: quién participa y qué intercambia",
            "Diagrama de contexto: la tienda de Amazon conecta a compradores, vendedores externos y logística, y la misma infraestructura se ofrece como nube pública a desarrolladores y empresas; en 2025 AWS aportó el 18 por ciento de las ventas y el 57 por ciento del resultado operativo.")
    _head(f, "Amazon: quién participa y qué intercambia")
    f.box(340, 150, 260, 90, "Amazon\ntienda propia + marketplace", "navy", 14, bold=True)
    f.box(20, 150, 200, 90, "Compradores\n(incluye miembros Prime)", "teal", 13)
    f.box(340, 48, 260, 70, "Vendedores externos\n(marketplace)", "gold", 13)
    f.box(720, 150, 200, 90, "Desarrolladores y empresas\n(clientes de AWS)", "coral", 13)
    f.box(340, 272, 260, 70, "Logística:\nalmacenes y entrega", "grey", 13)
    f.arrow([(220, 195), (340, 195)], "pedidos\ny pagos", label_at=(280, 168))
    f.arrow([(340, 215), (220, 215)])
    f.arrow([(470, 118), (470, 150)], "catálogo y stock", label_at=(560, 140))
    f.arrow([(470, 240), (470, 272)], "órdenes de envío", label_at=(570, 262))
    f.arrow([(600, 195), (720, 195)], "cómputo,\nalmacenamiento", label_at=(660, 168), dashed=True)
    y = _note(f, 360, "Lectura: la flecha discontinua marca la decisión estratégica de 2006, ofrecer como servicio piezas de infraestructura que la tienda ya necesitaba. En 2025 AWS fue el 18 % de las ventas ($128,7 mil millones de $716,9) y el 57 % del resultado operativo ($45,6 de $80,0). Dónde deja de valer: no dice cómo se reparte el costo compartido entre tienda y nube, dato que Amazon no publica.", "gold", 5)
    _foot(f, y + 6, DOC)
    return f


# ---------------------------------------------------------------- 2. componentes
def componentes() -> Fig:
    f = Fig(940, 0, "Una página de Amazon como abanico de servicios con contrato de latencia",
            "Diagrama de componentes documentado en el artículo de Dynamo (2007): una petición de página llega al motor de renderizado, que consulta más de 150 servicios; cada servicio tiene un contrato de latencia medido en el percentil 99,9; el carrito se apoya en un almacén clave-valor de alta disponibilidad.")
    _head(f, "Una página de Amazon como abanico de servicios con contrato de latencia")
    f.box(20, 55, 200, 70, "Petición de página\n(navegador o app)", "teal", 13)
    f.box(290, 55, 220, 70, "Motor de renderizado\n(compone la respuesta)", "navy", 13, bold=True)
    f.arrow([(220, 90), (290, 90)])
    f.group(30, 160, 880, 190, "Más de 150 servicios por página (documentado, Dynamo 2007)", "grey")
    f.box(50, 200, 190, 70, "Servicios de\nnegocio (catálogo,\nprecios, reseñas)", "plain", 13)
    f.box(260, 200, 190, 70, "Servicio de carrito", "gold", 13)
    f.box(470, 200, 190, 70, "Servicio de\nsesiones", "plain", 13)
    f.box(680, 200, 210, 70, "Otros servicios\n(composición interna:\nno se sabe)", "grey", 13, dashed=True)
    f.box(260, 285, 190, 50, "Dynamo (clave-valor)", "coral", 13, bold=True)
    f.arrow([(355, 270), (355, 285)])
    f.arrow([(400, 125), (400, 160)], "se pide en abanico", label_at=(520, 148))
    f.box(560, 55, 350, 70, "Contrato (ejemplo del artículo): respuesta\nen 300 ms para el 99,9 % de las peticiones\ncon 500 peticiones por segundo", "gold", 13)
    y = _note(f, 365, "Lectura: lo importante es el abanico. Si una página espera a decenas de servicios, el percentil 99,9 de cada uno decide la latencia de la página, por eso Amazon fija contratos en la cola y no en la media. Dónde deja de valer: el artículo es de 2007; la lista y el número de servicios actuales no son públicos.", "gold", 4)
    _foot(f, y + 6, "Fuente: DeCandia et al., Dynamo, SOSP 2007 (secciones 1 y 2.2). ")
    return f


# ---------------------------------------------------------------- 3. flujo (carrito en partición)
def flujo_carrito() -> Fig:
    f = Fig(940, 0, "El carrito durante una partición: escribir siempre y reconciliar después",
            "Secuencia ilustrativa del mecanismo documentado en Dynamo: durante una partición de red dos réplicas aceptan escrituras distintas del mismo carrito; al sanar la partición el servicio de carrito combina las versiones, de modo que ninguna adición se pierde pero un elemento borrado puede reaparecer.")
    _head(f, "El carrito durante una partición: escribir siempre y reconciliar después")
    f.box(20, 55, 220, 56, "1. Estado común:\ncarrito {libro}", "teal", 13)
    f.box(20, 150, 220, 70, "2a. Réplica A\nrecibe «añadir lápiz»\n→ {libro, lápiz}", "plain", 13)
    f.box(300, 150, 220, 70, "2b. Réplica B\nrecibe «añadir taza»\n→ {libro, taza}", "plain", 13)
    f.arrow([(130, 111), (130, 150)])
    f.arrow([(240, 100), (410, 100), (410, 150)])
    f.box(600, 150, 310, 70, "Partición de red: A y B no\nse ven; ambas aceptan\nescrituras (disponibilidad)", "coral", 13)
    f.box(20, 270, 500, 56, "3. Al sanar: dos versiones concurrentes (relojes vectoriales)", "gold", 13)
    f.arrow([(130, 220), (130, 270)])
    f.arrow([(410, 220), (410, 270)])
    f.box(20, 360, 500, 56, "4. La aplicación fusiona → {libro, lápiz, taza}", "teal", 13, bold=True)
    f.arrow([(270, 326), (270, 360)])
    f.box(600, 270, 310, 146, "Coste aceptado y documentado:\n«añadir al carrito» nunca se pierde,\npero un elemento borrado\npuede reaparecer", "gold", 13)
    y = _note(f, 440, "Lectura: la figura muestra una decisión de producto, no solo de base de datos. Se prefirió que añadir al carrito nunca falle antes que garantizar un único estado visible. Dónde deja de valer: vale para un carrito, donde fusionar tiene sentido; para un saldo o un inventario la fusión no es aceptable y se necesita coordinación.", "gold", 4)
    _foot(f, y + 6, "Fuente: DeCandia et al., Dynamo, SOSP 2007; los elementos del carrito son un ejemplo propio.")
    return f


# ---------------------------------------------------------------- 4. despliegue por olas
def despliegue() -> Fig:
    f = Fig(940, 0, "Cómo llega un cambio a producción: etapas, un solo nodo y olas con tiempo de espera",
            "Diagrama del pipeline de despliegue descrito en la Biblioteca de Constructores de Amazon: pruebas, una etapa de una sola caja en gamma, olas de regiones de tamaño creciente con tiempo de espera entre ellas y reversión automática; un cambio tarda unos cuatro o cinco días laborables en llegar a todas las regiones.")
    _head(f, "Cómo llega un cambio a producción: etapas, un solo nodo y olas con tiempo de espera")
    xs = [20, 200, 380, 560, 740]
    labels = [("Commit y\ncompilación", "teal"), ("Pruebas\nunitarias e\nintegración", "teal"), ("Gamma: «una caja»\n(30-60 min)", "gold"),
              ("Producción:\nola 1 (pocas\nregiones)", "navy"), ("Olas siguientes\n(más regiones)", "navy")]
    for x, (t, k) in zip(xs, labels):
        f.box(x, 60, 160, 90, t, k, 13)
    for a, b in zip(xs, xs[1:]):
        f.arrow([(a + 160, 105), (b, 105)])
    f.box(560, 200, 340, 60, "Tiempo de espera (bake time) vigilando alarmas\ny reversión automática si saltan", "coral", 13)
    f.arrow([(640, 150), (640, 200)])
    f.box(20, 200, 500, 60, "Esperas más largas en las primeras olas,\nmás cortas en las últimas (documentado)", "grey", 13)
    y = _note(f, 285, "Lectura: la secuencia reduce el radio de impacto de un cambio malo: el primer daño aparece en una caja o en una región pequeña, no en todas. Según el texto, un pipeline típico completa 24 regiones o 76 zonas de disponibilidad en cuatro o cinco días laborables. Dónde deja de valer: describe el proceso de servicios de AWS; el de otras áreas de Amazon puede diferir y los plazos concretos varían por equipo.", "gold", 4)
    _foot(f, y + 6, "Fuente: Liguori, «Automating safe, hands-off deployments», Amazon Builders' Library (2020).")
    return f


# ---------------------------------------------------------------- 5. gráfico segmentos
def segmentos() -> Fig:
    return grouped_bars(
        "Ventas y resultado operativo de Amazon en 2025 por segmento (miles de millones de dólares)",
        "Barras horizontales agrupadas: América del Norte vendió 426,3 mil millones y ganó 29,6 de resultado operativo; Internacional vendió 161,9 y ganó 4,7; AWS vendió 128,7 y ganó 45,6, es decir, el 18 por ciento de las ventas aporta el 57 por ciento del resultado operativo.",
        ["América del Norte", "Internacional", "AWS"],
        [("Ventas", [426.3, 161.9, 128.7], "teal"), ("Resultado operativo", [29.6, 4.7, 45.6], "coral")],
        unit="Miles de millones de dólares (2025)", horizontal=True, label_w=170, decimals=1,
        note="AWS vende unas tres veces menos que la tienda de América del Norte y gana más que los otros dos segmentos juntos (45,6 frente a 34,3). El margen operativo por segmento sale de dividir las dos barras: AWS 35 %, América del Norte 7 %, Internacional 3 %. Dónde deja de valer: los segmentos reparten costos compartidos con criterios que Amazon no detalla; el resultado total ($80,0) es el consolidado.",
        note_kind="gold", foot=DOC)


# ---------------------------------------------------------------- 6. línea de tiempo
def linea_tiempo() -> Fig:
    return timeline(
        "Evolución de Amazon: de librería en línea a plataforma de comercio y de nube",
        "Línea de tiempo de 1994 a 2025 en dos carriles: la tienda (lanzamiento en 1995, marketplace, Prime) y la plataforma técnica (AWS desde 2002, EC2 en 2006); los ingresos pasan de 147,8 millones de dólares en 1997 a 716,9 mil millones en 2025.",
        [("Tienda", [(1995, 2000, "Libros", "teal"), (2000, 2005, "Marketplace", "gold"), (2005, 2026, "Prime y logística", "navy")]),
         ("Plataforma técnica", [(1994, 2002, "Tienda", "grey"), (2002, 2006, "APIs", "gold"), (2006, 2026, "AWS: S3, EC2 y siguientes", "coral")])],
        unit="Año", events=[(1995, "Lanzamiento"), (2006, "EC2 (24 ago)")], t_max=2026, ticks=[1994, 2000, 2006, 2012, 2018, 2026], width=940, lane_h=54, label_w=150,
        note="Fechas: 1995 lanzamiento y 1997 salida a bolsa (fuentes secundarias; la carta de 1997 documenta 147,8 millones de ingresos y 1,5 millones de clientes), 2006 EC2 en beta (anuncio oficial del 24 de agosto de 2006), 2025 ingresos de 716,9 mil millones (comunicado Q4 2025). Las eras de la tienda y de la plataforma son una síntesis del autor, no fechas oficiales. Dónde deja de valer: los cortes entre eras son aproximados.",
        note_kind="gold", foot="Fuentes: carta a accionistas 1997; anuncio de EC2 (2006); comunicado Q4 2025; Wikipedia (fechas secundarias).")


FIGURES = {
    "amazon-contexto-actores.svg": contexto,
    "amazon-componentes-abanico-de-servicios.svg": componentes,
    "amazon-flujo-carrito-en-particion.svg": flujo_carrito,
    "amazon-despliegue-por-olas.svg": despliegue,
    "amazon-segmentos-2025.svg": segmentos,
    "amazon-linea-de-tiempo.svg": linea_tiempo,
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
