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




# ======================================================================
# Ampliación (nov. 2026): niveles de zoom de la arquitectura, economía a fondo
# y mecanismos de resiliencia. Todas las cifras proceden de las fuentes F1-F14.
# ======================================================================
import math  # noqa: E402

from figure_kit import _wrap, fmt_es, line_chart, stacked_bars  # noqa: E402


def _notebox(f: Fig, y: float, text: str, kind: str = "gold") -> float:
    """Caja de lectura con altura calculada a partir del texto."""
    n = len(_wrap(text, 13, f.width - 40))
    h = 22 + n * 16.6
    f.box(10, y, f.width - 20, h, text, kind, 13)
    return y + h


def _footer(f: Fig, y: float, text: str) -> None:
    lines = _wrap(text, 12, f.width - 40)
    for i, line in enumerate(lines):
        f.text(f.width / 2, y + 22 + i * 15, line, 12, "middle", 400, "#5c1f14")
    f.height = int(y + 30 + 15 * len(lines))


def _seq(f: Fig, actors: list[str], steps: list[tuple], y0: float, x0: float = 20, x1: float = 920,
         box_w: float = 150, step_h: float = 42) -> float:
    """Diagrama de secuencia: actores con línea de vida y mensajes (de, a, texto[, discontinua])."""
    n = len(actors)
    gap = (x1 - x0 - box_w) / (n - 1)
    xs = [x0 + box_w / 2 + i * gap for i in range(n)]
    for x, name in zip(xs, actors):
        f.box(x - box_w / 2, y0, box_w, 46, name, "navy", 13, bold=True)
    end = y0 + 46 + step_h * len(steps) + 6
    for x in xs:
        f.line(x, y0 + 46, x, end, "#8a9aa3", dashed=True)
    y = y0 + 46 + step_h * 0.78
    for st in steps:
        a, b, label = st[0], st[1], st[2]
        dashed = len(st) > 3 and bool(st[3])
        if a == b:
            f.box(xs[a] + 8, y - 17, gap - 16 if a < n - 1 else 190, 30, label, "gold", 13)
        else:
            f.arrow([(xs[a], y), (xs[b], y)], dashed=dashed)
            f.text((xs[a] + xs[b]) / 2, y - 7, label, 13, "middle", 400, "#142231", halo=True)
        y += step_h
    return end


def _value_m(v: float) -> str:
    return (fmt_es(v / 1e6, 1) + " M") if v >= 1e6 else (fmt_es(v / 1e3, 0) + " mil")


# ---------------------------------------------------------------- ingresos por línea
def ingresos_lineas() -> Fig:
    return grouped_bars(
        "Ventas de Amazon en 2025 por línea de ingreso (miles de millones de dólares)",
        "Barras horizontales con las ventas de 2025 por línea: tiendas en línea 269,3, servicios de vendedores externos 172,2, AWS 128,7, publicidad 68,6, suscripciones 49,6, tiendas físicas 22,6 y otros 5,9; suman 716,9.",
        ["Tiendas en línea (venta propia)", "Servicios a vendedores externos", "AWS", "Publicidad", "Suscripciones", "Tiendas físicas", "Otros"],
        [("Ventas 2025", [269.3, 172.2, 128.7, 68.6, 49.6, 22.6, 5.9], "teal")],
        unit="Miles de millones de dólares (2025)", horizontal=True, label_w=230, decimals=1, plot_h=300,
        note="Lectura: la venta propia sigue siendo la línea mayor (38 % del total), pero los servicios a vendedores externos (24 %) y la publicidad (10 %) suman más que AWS (18 %). Los cuatro números que más crecieron en el último trimestre fueron AWS (24 %), publicidad (23 %), servicios a vendedores (11 %) y tiendas en línea (10 %). Dónde deja de valer: es ingreso, no margen; el comunicado no reparte el resultado operativo por línea dentro de cada segmento.",
        note_kind="gold",
        foot="Fuente: comunicado Q4 2025 de Amazon (F4); cada barra es la suma de los cuatro trimestres de 2025 que publica el comunicado.")


# ---------------------------------------------------------------- estructura de costos
def costos() -> Fig:
    return stacked_bars(
        "A dónde va cada dólar de venta de Amazon, 2024 frente a 2025",
        "Barras apiladas al 100 por ciento: en 2025 el costo de ventas absorbe el 49,7 por ciento de los ingresos, la logística y el cumplimiento el 15,2, la tecnología y la infraestructura el 15,1, marketing, administración y otros el 8,8 y queda un 11,2 por ciento de resultado operativo; en 2024 el resultado era el 10,8 por ciento.",
        ["2024", "2025"],
        [("Costo de ventas", [326.288, 356.414], "coral"),
         ("Logística y cumplimiento", [98.505, 109.074], "gold"),
         ("Tecnología e infraestructura", [88.544, 108.521], "navy"),
         ("Marketing, administración y otros", [56.029, 62.940], "grey"),
         ("Resultado operativo", [68.593, 79.975], "teal")],
        unit="Porcentaje de las ventas totales", horizontal=True, percent=True, decimals=1, plot_h=210, label_w=60,
        note="Lectura: el costo de ventas pesa casi la mitad; el rubro que más crece es tecnología e infraestructura (de 13,9 % a 15,1 %), el de la nube y la inversión en capacidad. El resultado operativo sube de 10,8 % a 11,2 %. Dónde deja de valer: son rubros contables consolidados; el comunicado no los separa por segmento ni dice cuánto de «tecnología e infraestructura» es AWS.",
        note_kind="gold",
        foot="Fuente: estado de resultados consolidado, comunicado Q4 2025 (F4). Marketing, administración y otros suma tres rubros del comunicado.")


# ---------------------------------------------------------------- anillo de Dynamo
def dynamo_anillo() -> Fig:
    f = Fig(940, 0, "Dynamo: el anillo, la lista de preferencia y el traspaso con pista",
            "Diagrama del anillo de hash consistente de Dynamo con seis nodos: una clave cae entre F y A, el nodo A la coordina y la replica en B y C (N=3); si A no responde, la réplica se guarda con una pista en D, que la devolverá a A cuando vuelva.")
    _head(f, "Dynamo: el anillo, la lista de preferencia y el traspaso con pista")
    cx, cy, r = 290, 230, 140
    f.parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#8a9aa3" stroke-width="2.4" stroke-dasharray="3 5"/>')
    names = "ABCDEF"
    pos = {}
    for i, nm in enumerate(names):
        ang = math.radians(-90 + 60 * i - 30)  # F queda arriba a la izquierda, A arriba a la derecha de la clave
        x, y = cx + r * math.cos(ang), cy + r * math.sin(ang)
        pos[nm] = (x, y)
    kinds = {"A": "navy", "B": "teal", "C": "teal", "D": "gold", "E": "plain", "F": "plain"}
    for nm, (x, y) in pos.items():
        f.box(x - 24, y - 20, 48, 40, nm, kinds[nm], 15, bold=True, radius=20)
    # la clave k entre F y A (arriba)
    kx, ky = cx + (r + 8) * math.cos(math.radians(-150)), cy + (r + 8) * math.sin(math.radians(-150))
    f.dot(kx, ky - 4, "k", "coral")
    f.text(kx - 40, ky - 26, "clave k (hash)", 13, "middle", 700, "#5c1f14")
    f.text(cx + 60, cy - 30, "anillo de hash", 14, "middle", 700, "#32505f")
    f.text(cx + 60, cy - 10, "consistente", 14, "middle", 700, "#32505f")
    # flechas de réplica A -> B -> C
    def edge(a, b, dashed=False, color="#32505f"):
        (x1, y1), (x2, y2) = pos[a], pos[b]
        dx, dy = x2 - x1, y2 - y1
        d = math.hypot(dx, dy)
        sx, sy = x1 + dx / d * 28, y1 + dy / d * 28
        ex, ey = x2 - dx / d * 28, y2 - dy / d * 28
        f.arrow([(sx, sy), (ex, ey)], dashed=dashed, color=color)
    edge("A", "B")
    edge("B", "C")
    edge("A", "D", dashed=True, color="#c0432f")
    # panel derecho
    f.box(520, 55, 400, 70, "Lista de preferencia de k (N = 3): A, B, C.\nA es el coordinador de la escritura; B y C guardan réplicas.", "teal", 13)
    f.box(520, 140, 400, 86, "Traspaso con pista (hinted handoff): si A no responde, la réplica va a D, el siguiente nodo del anillo, con una pista que dice «esto era de A».", "gold", 13)
    f.box(520, 241, 400, 70, "Cuórum flexible (sloppy quorum): lecturas y escrituras usan los primeros N nodos sanos, no siempre los N primeros del anillo.", "coral", 13)
    f.box(520, 326, 400, 70, "D guarda la pista en una base local aparte y la devuelve a A cuando detecta que volvió.", "grey", 13)
    y = _notebox(f, 412, "Lectura: la flecha continua es la replicación normal (A coordina y copia a B y C); la discontinua roja es el desvío temporal cuando A no responde. Cada nodo físico ocupa varias posiciones del anillo (nodos virtuales) para repartir la carga; aquí se dibuja una por nodo. Documentado en F1, secciones 4.2 a 4.6. Dónde deja de valer: es el diseño de 2007 del almacén interno; DynamoDB, el servicio de AWS, es otro producto.")
    _footer(f, y + 6, "Fuente: DeCandia et al., Dynamo, SOSP 2007 (F1). Dibujo propio; seis nodos y la clave k son un ejemplo didáctico.")
    return f


# ---------------------------------------------------------------- secuencia put/get
def dynamo_secuencia() -> Fig:
    f = Fig(940, 0, "Dynamo paso a paso: una escritura y una lectura con N=3, W=2, R=2",
            "Secuencia de una escritura y una lectura en Dynamo con la configuración común (3,2,2): el cliente envía put al coordinador, que genera el reloj vectorial, escribe localmente y envía a las réplicas; con dos confirmaciones responde; la lectura pide a las réplicas, espera dos respuestas, devuelve todas las versiones no relacionadas y repara las réplicas atrasadas.")
    _head(f, "Dynamo paso a paso: una escritura y una lectura con N=3, W=2, R=2")
    end = _seq(f, ["Cliente\n(carrito)","Coordinador\n(A)", "Réplica B", "Réplica C"], [
        (0, 1, "1. put(clave, contexto, valor)"),
        (1, 1, "2. nuevo reloj vectorial; escribe en local"),
        (1, 2, "3. envía versión + reloj"),
        (1, 3, "4. envía versión + reloj"),
        (2, 1, "5. confirma (con A ya son W=2)", True),
        (1, 0, "6. éxito: sin esperar a C", True),
        (0, 1, "7. get(clave)"),
        (1, 2, "8. pide todas las versiones"),
        (1, 3, "9. pide todas las versiones"),
        (2, 1, "10. responde (con A ya son R=2)", True),
        (1, 0, "11. devuelve las versiones no relacionadas", True),
        (1, 1, "12. lectura reparadora a las atrasadas"),
    ], 52, step_h=40)
    y = _notebox(f, end + 10, "Lectura: las flechas continuas son peticiones y las discontinuas son respuestas. La escritura termina en el paso 6 con dos copias (W=2, contando al coordinador); la tercera llega después y, si falla, la repara el proceso de entropía con árboles de Merkle. En la lectura (R=2), si las versiones son causalmente comparables se devuelve la más nueva; si son concurrentes, se devuelven todas con su contexto y la aplicación fusiona (paso 11). Como R + W = 4 > N = 3, toda lectura se solapa con la última escritura exitosa en al menos un nodo. Dónde deja de valer: con un cuórum flexible o una partición, ese solapamiento no está garantizado; por eso hay versiones concurrentes.")
    _footer(f, y + 6, "Fuente: F1, secciones 4.4 a 4.7 y 6 (configuración común (3,2,2)); la aplicación es el servicio de carrito, ejemplo del artículo.")
    return f


# ---------------------------------------------------------------- versiones y relojes vectoriales
def dynamo_versiones() -> Fig:
    f = Fig(940, 0, "Cómo nacen y se resuelven versiones divergentes con relojes vectoriales",
            "Evolución de un objeto en Dynamo según el ejemplo del artículo: D1 y D2 las escribe el nodo Sx; D3 la escribe Sy y D4 la escribe Sz a partir de D2 sin verse entre sí, por lo que son concurrentes; un cliente las lee, las fusiona y Sx escribe D5 con el reloj combinado.")
    _head(f, "Cómo nacen y se resuelven versiones divergentes con relojes vectoriales")
    f.box(20, 80, 200, 66, "D1\n[(Sx, 1)]", "teal", 14, bold=True)
    f.box(260, 80, 200, 66, "D2\n[(Sx, 2)]", "teal", 14, bold=True)
    f.box(520, 45, 230, 66, "D3 (escribe Sy)\n[(Sx, 2), (Sy, 1)]", "gold", 14, bold=True)
    f.box(520, 135, 230, 66, "D4 (escribe Sz)\n[(Sx, 2), (Sz, 1)]", "gold", 14, bold=True)
    f.box(520, 250, 400, 76, "D5 = fusión de D3 y D4 (la hace el cliente, la escribe Sx)\n[(Sx, 3), (Sy, 1), (Sz, 1)]", "navy", 14, bold=True)
    f.arrow([(220, 113), (260, 113)])
    f.arrow([(460, 100), (490, 100), (490, 78), (520, 78)])
    f.arrow([(460, 126), (490, 126), (490, 168), (520, 168)])
    f.arrow([(750, 78), (880, 78), (880, 250)])
    f.arrow([(750, 168), (800, 168), (800, 250)])
    f.box(20, 165, 440, 140, "Regla de comparación: A es ancestro de B si todos los contadores de A son menores o iguales que los de B; entonces A se descarta. Si ninguno es ancestro del otro (D3 y D4), son concurrentes y hay que conservar ambas y fusionarlas.", "grey", 13)
    f.box(20, 340, 900, 56, "Costo: los relojes crecen con el número de nodos que escriben; Dynamo trunca los pares más antiguos al pasar un umbral, a cambio de perder la relación de ancestro y dar más trabajo de fusión.", "coral", 13)
    y = _notebox(f, 410, "Lectura: de izquierda a derecha pasa el tiempo; el reloj entre corchetes cuenta cuántas escrituras coordinó cada nodo. D3 y D4 nacen de D2 sin verse (por ejemplo, durante una falla), así que ninguna sustituye a la otra. Dónde deja de valer: el ejemplo es del artículo y ocupa un objeto con tres coordinadores; en producción la fusión es lógica de negocio de cada servicio (carrito: unir elementos; sesión: «gana la última»).")
    _footer(f, y + 6, "Fuente: F1, secciones 4.4 y 6.3 (ejemplo de la figura 3 del artículo); dibujo propio.")
    return f


# ---------------------------------------------------------------- cuántas versiones divergentes
def dynamo_divergencia() -> Fig:
    return grouped_bars(
        "Versiones divergentes que vio el servicio de carrito en 24 horas (porcentaje de peticiones)",
        "Barras horizontales en escala logarítmica: el 99,94 por ciento de las peticiones al carrito vio exactamente una versión, el 0,00057 por ciento vio dos, el 0,00047 por ciento tres y el 0,00009 por ciento cuatro.",
        ["1 versión", "2 versiones", "3 versiones", "4 versiones"],
        [("Porcentaje de peticiones", [99.94, 0.00057, 0.00047, 0.00009], "teal")],
        unit="Porcentaje de peticiones al carrito, 24 h (escala logarítmica)", horizontal=True, log=True, label_w=120,
        value_fmt=lambda v: fmt_es(v, 2 if v >= 1 else 5) + " %", plot_h=200,
        note="Lectura: la escala logarítmica es obligatoria porque la barra de una versión es cinco órdenes de magnitud mayor que la de cuatro. La conclusión del artículo es que, aunque el sistema está diseñado para divergir, divergir es raro. También dice que el aumento de versiones divergentes lo causan más los escritores concurrentes (robots) que los fallos. Dónde deja de valer: es una muestra de 24 horas del servicio de carrito en un momento no fechado con precisión; no mide tiempos ni pérdidas.",
        note_kind="gold", foot="Fuente: DeCandia et al., Dynamo, SOSP 2007, sección 6.3 (F1).")


# ---------------------------------------------------------------- latencia de coordinación
def dynamo_latencias() -> Fig:
    return grouped_bars(
        "Coordinar en el cliente o en el servidor: latencia de Dynamo (milisegundos)",
        "Barras agrupadas en escala logarítmica: con la coordinación en el servidor, el percentil 99,9 es 68,9 ms en lectura y 68,5 ms en escritura y la media 3,9 y 4,02 ms; con la coordinación en el cliente baja a 30,4 ms en ambos percentiles y a 1,55 y 1,9 ms en la media.",
        ["p99,9 lectura", "p99,9 escritura", "Media lectura", "Media escritura"],
        [("Coordinación en el servidor", [68.9, 68.5, 3.9, 4.02], "coral"), ("Coordinación en el cliente", [30.4, 30.4, 1.55, 1.9], "teal")],
        unit="Milisegundos (escala logarítmica)", log=True, decimals=2, plot_h=270,
        note="Lectura: la cola (p99,9) es unas diez a veinte veces la media y el cliente que coordina localmente se ahorra un salto de red: el percentil 99,9 baja unos 30 ms. Dónde deja de valer: es una medición interna de 2006 con una configuración (3,2,2) y unos cientos de nodos homogéneos; no se traslada a ninguna otra red, otro almacén ni a DynamoDB. El precio de la mejora es que cada cliente debe llevar la biblioteca y refrescar la vista de membresía.",
        note_kind="gold", foot="Fuente: DeCandia et al., Dynamo, SOSP 2007, tabla 2 (F1).")


# ---------------------------------------------------------------- tres estrategias de partición
def dynamo_particion() -> Fig:
    f = Fig(940, 0, "Cómo evolucionó el particionado de Dynamo: de tokens aleatorios a particiones fijas",
            "Diagrama antes y después de las estrategias de partición de Dynamo: la estrategia 1 en producción ataba el particionado a la colocación y obligaba a escanear discos al añadir nodos; la 3, que adoptaron, usa particiones de igual tamaño y reparte tokens, con metadatos tres órdenes de magnitud menores y arranque más rápido.")
    _head(f, "Cómo evolucionó el particionado de Dynamo: de tokens aleatorios a particiones fijas")
    f.box(20, 50, 280, 40, "Estrategia 1 (inicial)", "coral", 14, bold=True)
    f.box(330, 50, 280, 40, "Estrategia 2 (transitoria)", "gold", 14, bold=True)
    f.box(640, 50, 280, 40, "Estrategia 3 (adoptada)", "teal", 14, bold=True)
    f.box(20, 100, 280, 90, "T tokens aleatorios por nodo; cada rango entre tokens es una partición, de tamaño variable.", "plain", 13)
    f.box(330, 100, 280, 90, "T tokens aleatorios por nodo, pero el espacio se divide en Q particiones iguales.", "plain", 13)
    f.box(640, 100, 280, 90, "Q particiones iguales y Q/S tokens por nodo (S = nodos); al entrar o salir un nodo se reparten tokens.", "plain", 13)
    f.box(20, 205, 280, 150, "Problemas documentados: añadir un nodo obliga a otros a escanear su disco, lo que se hacía con la prioridad más baja; en temporada alta, arrancar un nodo tardó casi un día. Particionado y colocación van unidos.", "coral", 13)
    f.box(330, 205, 280, 150, "Separa el particionado de la colocación. Sirvió de paso intermedio durante la migración y tenía la peor eficiencia de reparto de carga de las tres.", "gold", 13)
    f.box(640, 205, 280, 150, "Mejor reparto de carga; metadatos hasta tres órdenes de magnitud menores; arranque más rápido porque cada partición vive en un archivo propio y se mueve como unidad; archivado más simple.", "teal", 13)
    f.arrow([(300, 145), (330, 145)])
    f.arrow([(610, 145), (640, 145)])
    y = _notebox(f, 372, "Lectura: de izquierda a derecha el diseño separa dos decisiones que la primera versión mezclaba: cómo se parte el espacio de claves y dónde se coloca cada parte. Es un ejemplo de una arquitectura corregida con datos de producción. Dónde deja de valer: el artículo mide un sistema de 30 nodos y N=3, que es la configuración típica de entonces; no dice qué hace hoy ningún sistema de Amazon.")
    _footer(f, y + 6, "Fuente: DeCandia et al., Dynamo, SOSP 2007, sección 6.2 (F1). Eficiencia = carga media / carga del nodo más cargado.")
    return f


# ---------------------------------------------------------------- reintentos en cascada
def reintentos() -> Fig:
    return line_chart(
        "Reintentos en capas: la carga sobre la base de datos se multiplica",
        "Gráfico de líneas: con tres intentos por capa y una pila de cinco capas la carga sobre la base de datos se multiplica por 243, como describe la Biblioteca de Constructores; con dos intentos por capa serían 32 veces.",
        [("3 intentos por capa", [(1, 3), (2, 9), (3, 27), (4, 81), (5, 243)], "coral"),
         ("2 intentos por capa (cálculo propio)", [(1, 2), (2, 4), (3, 8), (4, 16), (5, 32)], "teal")],
        x_label="Capas de servicio apiladas, cada una con su propio reintento", y_label="Intentos que recibe la base de datos por cada petición", plot_h=290,
        x_ticks=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
        note="Lectura: cada capa multiplica por el número de intentos lo que hace la inferior (3, 9, 27, 81, 243). Por eso la regla de Amazon es reintentar en un solo punto de la pila y limitar los reintentos con un cubo de fichas local. Dónde deja de valer: es el peor caso, cuando todos los intentos fallan; la serie de dos intentos es una extrapolación propia con la misma fórmula, no un dato publicado.",
        note_kind="gold", foot="Fuente: «Timeouts, retries, and backoff with jitter», Amazon Builders' Library (F6); 3^5 = 243.")


# ---------------------------------------------------------------- capacidad por zona de disponibilidad
def estabilidad_zonas() -> Fig:
    return line_chart(
        "Cuánta capacidad sobrante cuesta sobrevivir a la pérdida de una zona de disponibilidad",
        "Gráfico de líneas: para tolerar la caída de una zona con carga repartida por igual hay que sobredimensionar un 100 por ciento con 2 zonas, 50 con 3 zonas (cifra de Amazon), 33 con 4, 25 con 5 y 20 con 6.",
        [("Sobredimensionamiento necesario (%)", [(2, 100, "100 %", "t"), (3, 50, "50 % (Amazon)", "r"), (4, 33.3, "33 %", "t"), (5, 25, "25 %", "t"), (6, 20, "20 %", "t")], "navy")],
        x_label="Zonas de disponibilidad usadas", y_label="Capacidad extra sobre la carga (%)", plot_h=260,
        x_ticks=[(2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6")],
        note="Lectura: la fórmula es 1/(n−1): si una de n zonas cae, las n−1 restantes deben absorber su carga. Con tres zonas, la Biblioteca dice sobredimensionar un 50 %, de modo que cada zona opera como máximo al 66 % de lo probado. Más zonas abaratan la tolerancia, pero añaden complejidad y latencia entre zonas. Dónde deja de valer: es un cálculo propio sobre la regla de F7; supone zonas iguales y carga uniforme, y no cuenta el costo de operar más zonas.",
        note_kind="gold", foot="Fuente: «Static stability using Availability Zones», Amazon Builders' Library (F7); curva calculada por el autor.")


# ---------------------------------------------------------------- plano de control y plano de datos
def estabilidad_planos() -> Fig:
    f = Fig(940, 0, "Estabilidad estática: el plano de datos sigue aunque el plano de control falle",
            "Diagrama de EC2 como plano de control (cambios: lanzar, modificar, borrar) y plano de datos (las instancias que ya corren y su red); si el plano de control falla, el plano de datos sigue sirviendo con lo que ya tiene, y los clientes diseñados así preasignan capacidad en varias zonas.")
    _head(f, "Estabilidad estática: el plano de datos sigue aunque el plano de control falle")
    f.group(20, 50, 420, 190, "Plano de control (hacer cambios)", "coral")
    f.box(40, 90, 380, 44, "Lanzar, parar, modificar recursos", "plain", 13)
    f.box(40, 144, 380, 44, "Propagar el cambio a donde debe aplicarse", "plain", 13)
    f.box(40, 196, 380, 36, "Más complejo, más piezas móviles", "grey", 13)
    f.group(500, 50, 420, 190, "Plano de datos (sostener lo que ya existe)", "teal")
    f.box(520, 90, 380, 44, "Instancias en ejecución y su red", "plain", 13)
    f.box(520, 144, 380, 44, "Tráfico de los clientes", "plain", 13)
    f.box(520, 196, 380, 36, "Más simple y más probado", "grey", 13)
    f.arrow([(440, 150), (500, 150)], "configura", label_at=(470, 138))
    f.box(20, 262, 900, 54, "Diseño estáticamente estable: cuando el plano de control cae, el sistema no necesita llamarlo para seguir; opera con la configuración y la capacidad que ya tenía.", "gold", 13)
    f.box(20, 328, 440, 70, "Ejemplo: no depender de lanzar instancias nuevas en el momento de un fallo; tener ya la capacidad preasignada en cada zona.", "plain", 13)
    f.box(480, 328, 440, 70, "Costo: pagar capacidad ociosa y limitar el escalado automático reactivo (ver la figura anterior).", "coral", 13)
    y = _notebox(f, 412, "Lectura: lo que cambia la forma de diseñar es qué se debe llamar durante el fallo. Dónde deja de valer: Amazon documenta el patrón (F7) como práctica de AWS; no publica qué porcentaje de la tienda lo cumple, y un sistema con estado fuerte (un saldo) no puede repartir escrituras sin coordinación.")
    _footer(f, y + 6, "Fuente: «Static stability using Availability Zones», Amazon Builders' Library (F7). Dibujo propio.")
    return f


# ---------------------------------------------------------------- shuffle sharding
def shuffle() -> Fig:
    f = Fig(940, 0, "Shuffle sharding: cada cliente recibe una combinación casi única de trabajadores",
            "Diagrama ilustrativo con ocho trabajadores y tres clientes con dos trabajadores cada uno: si un cliente con una petición dañina agota sus dos trabajadores, otro cliente que comparte uno de ellos sigue servido por el otro y un tercero ni lo nota; con ocho trabajadores hay 28 combinaciones posibles de dos.")
    _head(f, "Shuffle sharding: cada cliente recibe una combinación casi única de trabajadores")
    xs = [40 + i * 112 for i in range(8)]
    for i, x in enumerate(xs, 1):
        kind = "coral" if i in (1, 2) else "teal"
        f.box(x, 260, 90, 44, f"Trabajador {i}", kind, 13, bold=True)
    cl = [("Cliente Alfa\n(petición dañina)", 150, "coral", (1, 2)), ("Cliente Beta", 380, "gold", (2, 5)), ("Cliente Gamma", 640, "plain", (3, 7))]
    for name, x, kind, ws in cl:
        f.box(x, 60, 180, 62, name, kind, 13, bold=True)
        for w in ws:
            f.arrow([(x + 90, 122), (xs[w - 1] + 45, 260)], dashed=(kind == "coral"))
    f.box(20, 320, 900, 70, "Con ocho trabajadores y dos por cliente hay 28 combinaciones. Si Alfa agota 1 y 2, Beta pierde solo el 2 y sigue con el 5; Gamma no ve nada. Un cliente que compartiera ambos trabajadores con Alfa quedaría afectado: es 1 de 28.", "gold", 13)
    y = _notebox(f, 404, "Lectura: las flechas unen a cada cliente con sus trabajadores asignados; en rojo, los trabajadores que agota la petición dañina. Sin sharding todos comparten los ocho y un solo cliente puede degradar al conjunto; con shuffle sharding, el radio de impacto cae a una fracción pequeña y se reduce más aún con cientos de clientes y más trabajadores. Dónde deja de valer: la figura es un modelo didáctico; funciona si los clientes reintentan hacia otro trabajador de su combinación y si la carga dañina no se propaga por otra capa compartida.")
    _footer(f, y + 6, "Fuente: «Workload isolation using shuffle-sharding», Amazon Builders' Library, 5 de diciembre de 2019 (F8); el 28 es C(8,2).")
    return f


# ---------------------------------------------------------------- pipeline: una ola por dentro
def pipeline_ola() -> Fig:
    f = Fig(940, 0, "Por dentro de una ola de producción: una caja, lotes del 33 por ciento y reversión automática",
            "Diagrama de una ola de despliegue: primero una caja que atiende como máximo el 10 por ciento de las peticiones, luego lotes de como máximo el 33 por ciento de la flota con al menos el 66 por ciento de la capacidad sana; si salta la alarma agregada, la ola se revierte automáticamente.")
    _head(f, "Por dentro de una ola de producción: una caja, lotes del 33 por ciento y reversión")
    x = 20
    for t, k, w in [("Una caja (≤ 10 % del tráfico)", "teal", 240), ("Lote 1 (≤ 33 % de la flota)", "gold", 300), ("Resto de la flota, en más lotes", "grey", 340)]:
        f.box(x, 60, w - 10, 64, t, k, 13, bold=True)
        x += w
    fx = 20
    for i in range(12):
        kind = "teal" if i == 0 else "gold" if i < 5 else "plain"
        f.box(fx, 150, 66, 40, f"caja {i + 1}", kind, 13)
        fx += 76
    f.arrow([(60, 124), (60, 150)])
    f.box(20, 205, 440, 58, "Capacidad sana ≥ 66 % en todo momento: todo servicio está dimensionado para perder una zona.", "plain", 13)
    f.box(480, 205, 440, 58, "Alarma agregada: si cualquiera de las alarmas graves del equipo salta, se revierte todo en la región.", "coral", 13)
    f.box(20, 278, 440, 70, "Algunos equipos despliegan solo el 5 % a la vez, y revierten de 33 en 33 % para ir más rápido atrás que adelante.", "gold", 13)
    f.box(480, 278, 440, 70, "Tiempo de espera (bake time) tras cada etapa: la tubería sigue vigilando por si el daño es lento.", "teal", 13)
    y = _notebox(f, 362, "Lectura: arriba, de izquierda a derecha, cómo crece el alcance del cambio dentro de una ola; en la fila central, las doce cajas de un ejemplo (la primera en azul verdoso, las del primer lote en dorado, el resto sin cambiar). Cada limite del 10 % y del 33 % es un máximo típico, no un valor fijo. Dónde deja de valer: es el proceso de servicios de AWS descrito en 2020 (F9) y los tamaños de ola dependen de cada servicio; no asegura que ningún cambio malo llegue a producción, solo que su alcance sea pequeño.")
    _footer(f, y + 6, "Fuente: Liguori, «Automating safe, hands-off deployments», Amazon Builders' Library (F9). Doce cajas: ejemplo propio.")
    return f


# ---------------------------------------------------------------- de 16 días a la tubería
def plazo_entrega() -> Fig:
    return stacked_bars(
        "De la confirmación del código a producción: 16 días de media antes de las tuberías",
        "Barras apiladas en días: antes de automatizar, un cambio tardaba 16 días de media desde que se confirmaba hasta producción: 1,5 días de escribir código, menos de una hora de compilar y desplegar y casi 14 días de espera entre pasos; el equipo piloto de las tuberías redujo ese plazo un 90 por ciento.",
        ["Antes (promedio)", "Equipo piloto (−90 %)"],
        [("Escribir el código", [1.5, 0.0], "teal"), ("Construir y desplegar", [0.04, 0.0], "navy"), ("Esperas entre pasos", [14.46, 0.0], "coral"), ("Total tras el piloto", [0.0, 1.6], "gold")],
        unit="Días de calendario", horizontal=True, decimals=1, plot_h=200, label_w=170,
        note="Lectura: la barra de arriba descompone los 16 días: casi todo era espera, no trabajo. Con las tuberías, el equipo que más ganó redujo el plazo total un 90 %, unos 1,6 días si se aplica ese porcentaje al promedio (cálculo propio). Dónde deja de valer: la descomposición es de un estudio interno anterior y de un equipo piloto, no del estado actual de Amazon; el 1,6 es una conversión aritmética, no una medición publicada.",
        note_kind="gold", foot="Fuente: «Going faster with continuous delivery», Amazon Builders' Library (F13); 16 × 0,1 = 1,6 días, cálculo propio.")


# ---------------------------------------------------------------- Prime Day 2022
def prime_day() -> Fig:
    return grouped_bars(
        "Prime Day 2022: ritmo de cuatro servicios de AWS que alimentan a la tienda",
        "Barras horizontales en escala logarítmica con los máximos de Prime Day 2022: DynamoDB 105,2 millones de peticiones por segundo, SQS 70,5 millones de mensajes por segundo, SES 33 mil correos por segundo y EBS 11,4 billones de peticiones al día, unos 131,9 millones por segundo en promedio.",
        ["EBS (media por segundo)", "DynamoDB (pico)", "SQS (pico)", "SES (pico)"],
        [("Eventos por segundo", [131.9e6, 105.2e6, 70.5e6, 33e3], "navy")],
        unit="Peticiones, mensajes o correos por segundo (escala logarítmica)", horizontal=True, log=True, label_w=190,
        value_fmt=_value_m, plot_h=200,
        note="Lectura: las barras no son comparables en unidad (peticiones, mensajes, correos) ni en tipo (pico frente a media diaria: 11,4 × 10^12 ÷ 86 400 s); sirven para ver el orden de magnitud de cada servicio. El comunicado de AWS añade que la huella de servidores de EC2 creció un 12 % y la huella total solo un 7 % frente al Cyber Monday anterior por el uso de procesadores Graviton2. Dónde deja de valer: son servicios de AWS que usa Amazon, no el rendimiento de la tienda.",
        note_kind="gold", foot="Fuente: Barr, «Amazon Prime Day 2022 – AWS for the Win!», AWS News Blog, 25 de julio de 2022 (F10).")


# ---------------------------------------------------------------- Working Backwards
def working_backwards() -> Fig:
    f = Fig(940, 0, "Trabajar hacia atrás: del cliente al producto con un comunicado de prensa y preguntas",
            "Flujo del proceso Working Backwards descrito por Bryar y Carr: se escribe primero el comunicado de prensa de menos de una página y un FAQ de hasta cinco, se lee en silencio en una reunión de una hora, se revisa en varias rondas con la dirección y solo una minoría de documentos llega a recibir recursos.")
    _head(f, "Trabajar hacia atrás: del cliente al producto con un comunicado y preguntas")
    steps = [("1. Idea\ncon el cliente", "teal"), ("2. Comunicado\n(< 1 página)", "gold"), ("3. FAQ\n(≤ 5 páginas)", "gold"), ("4. Lectura en\nsilencio, 1 hora", "plain"), ("5. Comentarios;\nlos senior, al final", "plain"), ("6. Revisiones\ncon dirección", "navy")]
    x = 20
    for t, k in steps:
        f.box(x, 60, 140, 80, t, k, 13, bold=(k == "navy"))
        x += 150
    for i in range(5):
        f.arrow([(20 + i * 150 + 140, 100), (20 + (i + 1) * 150, 100)])
    f.box(20, 170, 440, 80, "Documentado: es normal que un equipo escriba diez borradores o más y se reúna cinco veces o más con sus líderes.", "plain", 13)
    f.box(480, 170, 440, 80, "Documentado: la mayoría de los PR/FAQ no llega a lanzarse; lo describen como una función, no un fallo del proceso.", "coral", 13)
    f.box(20, 265, 440, 70, "Qué evita: construir primero y buscar después al cliente; limita la extensión para obligar a decidir qué importa.", "teal", 13)
    f.box(480, 265, 440, 70, "Costo: semanas de escritura antes de escribir código; riesgo de documentos pulidos que no reflejan al cliente real.", "gold", 13)
    y = _notebox(f, 350, "Lectura: el proceso invierte el orden habitual (primero producto, luego publicidad): se escribe el lanzamiento antes de construir. Dónde deja de valer: la fuente es un extracto del libro de dos antiguos empleados publicado por Amazon (F11), es decir, autodescripción favorable; no hay datos públicos de cuántos proyectos salvó o frenó. El costo de la última caja es análisis propio.")
    _footer(f, y + 6, "Fuente: «An insider look at Amazon's culture and processes» (F11), 9 de febrero de 2021; Working Backwards se usa «desde 2004» según el extracto.")
    return f


# ---------------------------------------------------------------- línea de tiempo ampliada
def linea_tiempo() -> Fig:
    return timeline(
        "Evolución de Amazon: tienda, plataforma técnica y práctica de ingeniería",
        "Línea de tiempo de 1994 a 2026 con tres carriles: la tienda (libros, marketplace, Prime y logística), la plataforma técnica (APIs, AWS con S3 y EC2) y la práctica de ingeniería (Working Backwards desde 2004, Dynamo 2007, despliegues automatizados 2020); marcadores en 1995, 1997, 2006, 2007 y 2020.",
        [("Tienda", [(1995, 2000, "Libros", "teal"), (2000, 2005, "Marketplace", "gold"), (2005, 2026, "Prime, logística y publicidad", "navy")]),
         ("Plataforma técnica", [(1994, 2002, "Tienda", "grey"), (2002, 2006, "APIs", "gold"), (2006, 2026, "AWS: S3, EC2 y siguientes", "coral")]),
         ("Práctica de ingeniería", [(2004, 2007, "PR/FAQ", "teal"), (2007, 2019, "Servicios y Dynamo", "gold"), (2019, 2026, "Despliegues", "navy")])],
        unit="Año", events=[(1995, "Tienda"), (1997, "Día 1"), (2006, "S3 y EC2"), (2007, "Dynamo"), (2020, "Despliegues")], t_max=2026, ticks=[1994, 2000, 2006, 2012, 2018, 2026], width=940, lane_h=54, label_w=170,
        note="Fechas documentadas: 1997 carta a los accionistas, 14 de marzo de 2006 anuncio de S3, 24 de agosto de 2006 EC2 en beta, 2007 artículo de Dynamo, 2004 como inicio del uso de Working Backwards y 2019-2020 artículos de aislamiento y despliegue. 1995 y las eras de la tienda vienen de fuentes secundarias. Dónde deja de valer: los cortes entre eras son síntesis del autor, no fechas oficiales; los carriles no implican causalidad directa.",
        note_kind="gold", foot="Fuentes: F1, F3, F5, F8, F9, F11, F12 y F14; síntesis propia de las eras.")



# ====================== segunda ampliación: hardware, software, infraestructura, fallos ======================
from figure_kit import _wrap as _w2  # noqa: E402


def _cards(title, desc, groups, note, foot, ncols=2):
    f = Fig(940, 0, title, desc)
    f.text(14, 27, title, 15, "start", 700, "#142231")
    colw = (940 - 20 - (ncols - 1) * 20) / ncols
    ys = [50.0] * ncols
    for i, (head, kind, items) in enumerate(groups):
        c = i % ncols
        x = 10 + c * (colw + 20)
        y = ys[c]
        f.box(x, y, colw, 34, head, kind, 14, bold=True)
        y += 42
        for t in items:
            h = 18 + len(_w2(t, 13, colw - 20)) * 16.6
            f.box(x, y, colw, h, t, "plain", 13)
            y += h + 8
        ys[c] = y + 8
    y = max(ys)
    n = len(_w2(note, 13, 900))
    nh = 22 + n * 16.6
    f.box(10, y, 920, nh, note, "gold", 13)
    y += nh + 6
    lines = _w2(foot, 12, 900)
    for i, line in enumerate(lines):
        f.text(470, y + 22 + i * 15, line, 12, "middle", 400, "#5c1f14")
    f.height = int(y + 30 + 15 * len(lines))
    return f


def _x_hardware() -> Fig:
    return _cards('Hardware de Amazon: lo que se publica y lo que no', 'Diagrama del hardware que Amazon documenta públicamente: servidores de uso general y nodos homogéneos en el artículo de Dynamo, procesadores Graviton2 y almacenamiento EBS en Prime Day 2022, chips propios Trainium y Graviton en 2025 y una terminal de satélite con silicio propio; no se publican modelos de servidor, redes ni centros de datos.', [('Servidores', 'teal', ['Documentado: decenas de miles de servidores en muchos centros de datos (Dynamo, 2007); hardware estándar de uso general con menos rendimiento de disco que servidores empresariales de gama alta; las mediciones del artículo usan unos cientos de nodos homogéneos.', 'No se sabe: modelos, fabricantes y densidad de cada servidor.']), ('Procesadores y chips propios', 'gold', ['Documentado: en Prime Day 2022 la huella de servidores creció solo un 7 % gracias al mayor uso de procesadores Graviton2.', 'Documentado: en 2025 Amazon dice que Trainium y Graviton suman más de 10 mil millones de dólares de ingreso anual recurrente y que Trainium2 tiene 1,4 millones de chips instalados (afirmación de la empresa).', 'No se sabe: cuántos servidores usan Graviton hoy.']), ('Almacenamiento y bases', 'navy', ['Documentado: en Prime Day 2022 se añadieron 152 petabytes de EBS; la flota atendió 11,4 billones de peticiones por día y movió 532 petabytes por día.', 'Documentado: 5.326 instancias de Aurora procesaron 288 mil millones de transacciones y guardaron 1.849 terabytes ese día.', 'No se sabe: tipos de disco y de red de almacenamiento.']), ('Red y dispositivos', 'grey', ['Documentado: los centros de datos de Dynamo se conectan con enlaces de alta velocidad; la latencia entre centros afecta a la respuesta (F1).', 'Documentado: Amazon presenta en 2025 una terminal para su servicio de satélites con silicio propio y que Alexa+ llega a televisores y coches de terceros (F4).', 'No se sabe: topología de red, capacidad de enlace y detalle de los dispositivos de usuario.'])], 'Lectura: cada recuadro separa lo publicado de lo que no se sabe. Los datos de 2007 (Dynamo) y de 2022 (Prime Day) describen servicios de AWS, no la tienda entera. Dónde deja de valer: Amazon no publica inventario de hardware; las cifras de chips propios son afirmaciones de la empresa en un comunicado.', 'Fuentes: DeCandia et al. 2007 (F1); Barr, 2022 (F10); comunicado Q4 2025 (F4).')


def _x_software() -> Fig:
    return _cards('Software de Amazon que sus propias fuentes documentan', 'Diagrama del software documentado de Amazon: en Dynamo, Java con mensajería por etapas, almacenes BDB y MySQL; en Prime Day, DynamoDB, SQS, SES, Lambda, Kinesis, ElastiCache, S3, Aurora y EBS; en el proceso de entrega, los sistemas internos Brazil, Apollo y Pipelines; no se publican el sistema operativo ni los marcos de la tienda.', [('Almacenes y colas', 'teal', ['Documentado: Dynamo usó almacenes locales intercambiables: BDB Transactional Data Store, BDB Java Edition, MySQL o un búfer en memoria; la mayoría de las instancias usaba BDB (F1).', 'Documentado: en Prime Day 2022 se citan DynamoDB, SQS, SES, S3, Aurora, ElastiCache y Kinesis como servicios que sostienen a la tienda (F10).']), ('Lenguajes y marcos', 'gold', ['Documentado: Dynamo se implementó con mensajería sobre canales Java NIO y una tubería por etapas de tipo SEDA (F1).', 'Documentado: el patrón de funciones sin servidor (Lambda) se usa en la planificación de paquetes de América del Norte (F10).', 'No se sabe: lenguajes y marcos de la tienda, de los sistemas de pago y de la logística.']), ('Entrega de software', 'navy', ['Documentado: sistema de compilación Brazil, sistema de despliegue Apollo y la herramienta Pipelines que los une (F13).', 'Documentado: alarmas agregadas, pruebas «canario» continuas y reversión automática (F9).']), ('Sistemas operativos y orquestación', 'grey', ['No se sabe: sistema operativo de las flotas internas y orquestador propio: las fuentes no los nombran.', 'Documentado: contenedores y funciones se citan como unidades de despliegue en los pipelines (una máquina virtual, un contenedor o un porcentaje de invocaciones de una función) (F9).'])], 'Lectura: cuatro grupos de tecnologías; cada afirmación lleva su fuente o la marca «no se sabe». Dónde deja de valer: los nombres de servicios de AWS no equivalen a la pila interna de la tienda; el artículo de Dynamo es de 2007.', 'Fuentes: F1, F9, F10, F13.')


def _x_infra() -> Fig:
    return _cards('Características de la infraestructura de Amazon: regiones, zonas, capacidad y costo', 'Diagrama de la infraestructura de Amazon según sus fuentes: nube propia con 24 regiones y 76 zonas de disponibilidad en 2020, servicios en tres o más zonas con sobreaprovisionamiento, células dentro de una región, y un gasto de capital de 131,8 mil millones de dólares brutos en 2025 con unos 200 mil millones previstos para 2026.', [('Escala y ubicación', 'teal', ['Documentado: 24 regiones y 76 zonas de disponibilidad en 2020 (F9); no se sabe el número actual.', 'Documentado: decenas de miles de servidores en muchos centros de datos en 2007 (F1).', 'Inferido: la infraestructura es propia y no alquilada: AWS es la propia Amazon; no se publica la parte propiedad de terceros (por ejemplo, ubicación en centros de datos compartidos).']), ('Diseño por zonas y células', 'gold', ['Documentado: servicios en un grupo de autoescalado en tres o más zonas, con 50 % de capacidad sobrante con tres zonas (F7).', 'Documentado: equipos que dividen una región en zonas o en células, los fragmentos internos de su servicio, para despliegues de alcance menor (F9).']), ('Capacidad y costo', 'navy', ['Documentado: compras de propiedad y equipo de 131,8 mil millones de dólares brutos en 2025 y 83,0 en 2024; amortización de 65,8 mil millones en 2025; unos 200 mil millones previstos de inversión de capital en 2026 (F4).', 'Documentado: flujo de caja libre de 11,2 mil millones en 2025 frente a 38,2 en 2024 (F4).']), ('Redes', 'grey', ['Documentado: enlaces de alta velocidad entre centros de datos (F1).', 'No se sabe: topología, proveedores y capacidad de la red mundial; tampoco hay dato de costo de red.'])], 'Lectura: los cuatro recuadros recorren escala, diseño, costo y red. Dónde deja de valer: las cifras de capital son consolidadas de toda la empresa, no solo de AWS; el desglose por segmento no se publica en las fuentes de este caso.', 'Fuentes: F1, F4, F7, F9.')


def _x_fallos() -> Fig:
    return _cards('Qué pasa cuando cae cada componente en lo que Amazon documenta', 'Diagrama de la tolerancia a fallos documentada de Amazon por nivel: un nodo de Dynamo (traspaso con pista, árboles de Merkle), una zona de disponibilidad (sobreaprovisionamiento y estabilidad estática), una dependencia lenta (retroceso con variación y cubo de fichas), un cliente ruidoso (shuffle sharding) y un cambio defectuoso (una caja, olas y reversión automática); no se documentan pruebas de caos ni recuperación ante desastres de la tienda.', [('Cae un nodo de almacenamiento', 'teal', ['Documentado: la réplica se guarda con una pista en otro nodo y se devuelve al volver; los árboles de Merkle recuperan réplicas perdidas; la lectura reparadora actualiza réplicas atrasadas (F1).']), ('Cae una zona de disponibilidad', 'gold', ['Documentado: los servicios se dimensionan para que las demás zonas absorban la carga; el plano de datos sigue sin depender del plano de control (F7).']), ('Una dependencia es lenta o falla', 'coral', ['Documentado: retroceso exponencial con tope y variación aleatoria, cubo de fichas local y reintento en un solo punto de la pila; se evitan los interruptores de circuito por su comportamiento modal (F6).']), ('Un cliente se comporta mal', 'navy', ['Documentado: shuffle sharding limita el impacto a una combinación de recursos (F8).']), ('Un cambio es defectuoso', 'plain', ['Documentado: una caja, lotes de hasta el 33 %, tiempo de espera y reversión automática si salta la alarma agregada (F9).']), ('Lo que no se documenta', 'grey', ['No se sabe: pruebas de caos o ejercicios de fallo, recuperación ante desastres de la tienda y degradación elegante de la página: ninguna de las fuentes consultadas las describe.'])], 'Lectura: cada recuadro es un componente que cae y la defensa documentada; el último recuadro lista lo que falta. Dónde deja de valer: son mecanismos de AWS y de Dynamo; no prueban que la tienda los use de igual modo.', 'Fuentes: F1, F6, F7, F8, F9.')

FIGURES = {
    "amazon-contexto-actores.svg": contexto,
    "amazon-segmentos-2025.svg": segmentos,
    "amazon-ingresos-por-linea-2025.svg": ingresos_lineas,
    "amazon-estructura-de-costos.svg": costos,
    "amazon-componentes-abanico-de-servicios.svg": componentes,
    "amazon-dynamo-anillo-y-lista-de-preferencia.svg": dynamo_anillo,
    "amazon-dynamo-secuencia-put-get.svg": dynamo_secuencia,
    "amazon-flujo-carrito-en-particion.svg": flujo_carrito,
    "amazon-dynamo-versiones-y-relojes-vectoriales.svg": dynamo_versiones,
    "amazon-dynamo-versiones-divergentes.svg": dynamo_divergencia,
    "amazon-dynamo-latencia-de-coordinacion.svg": dynamo_latencias,
    "amazon-dynamo-evolucion-del-particionado.svg": dynamo_particion,
    "amazon-reintentos-en-capas.svg": reintentos,
    "amazon-estabilidad-estatica-planos.svg": estabilidad_planos,
    "amazon-estabilidad-estatica-zonas.svg": estabilidad_zonas,
    "amazon-shuffle-sharding.svg": shuffle,
    "amazon-despliegue-por-olas.svg": despliegue,
    "amazon-despliegue-una-ola-por-dentro.svg": pipeline_ola,
    "amazon-plazo-de-entrega-16-dias.svg": plazo_entrega,
    "amazon-prime-day-2022.svg": prime_day,
    "amazon-working-backwards.svg": working_backwards,
    "amazon-linea-de-tiempo.svg": linea_tiempo,
    "amazon-hardware-utilizado.svg": _x_hardware,
    "amazon-software-utilizado.svg": _x_software,
    "amazon-caracteristicas-de-la-infraestructura.svg": _x_infra,
    "amazon-tolerancia-a-fallos.svg": _x_fallos,
}


def main() -> int:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "casos" / "figures"
    out.mkdir(parents=True, exist_ok=True)
    for name, build in FIGURES.items():
        (out / name).write_text(build().svg(), encoding="utf-8")
    print(f"{len(FIGURES)} figuras en {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
