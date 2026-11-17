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
         ("Empresa", [(2007.8, 2020.9, "Empresa privada", "grey"), (2020.9, 2026, "Empresa cotizada", "navy")])],
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


# ======================================================================
# Ampliación (nov. 2026): confianza en capas, idempotencia de pagos por dentro, migración de
# pagos, servicios con IDL, evolución de la búsqueda y economía. Cifras de las fuentes F1-F13.
# ======================================================================
from figure_kit import _wrap, fmt_es, grouped_bars  # noqa: E402


def _notebox(f: Fig, y: float, text: str, kind: str = "gold") -> float:
    n = len(_wrap(text, 13, f.width - 40))
    h = 22 + n * 16.6
    f.box(10, y, f.width - 20, h, text, kind, 13)
    return y + h


def _footer(f: Fig, y: float, text: str) -> None:
    lines = _wrap(text, 12, f.width - 40)
    for i, line in enumerate(lines):
        f.text(f.width / 2, y + 22 + i * 15, line, 12, "middle", 400, "#5c1f14")
    f.height = int(y + 30 + 15 * len(lines))


def _seq(f: Fig, actors: list, steps: list, y0: float, x0: float = 20, x1: float = 920,
         box_w: float = 150, step_h: float = 42) -> float:
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


# ---------------------------------------------------------------- confianza en capas
def confianza() -> Fig:
    f = Fig(940, 0, "La confianza en capas: qué mecanismo actúa antes, durante y después de una estancia",
            "Diagrama de las capas de confianza de Airbnb a lo largo de una reserva: antes de reservar (reseñas y valoraciones públicas, perfil y reglas), al pagar (plataforma de pagos propia desde 2008), durante la estancia (AirCover, mensajes con el anfitrión, línea de seguridad 24 horas) y después (reseñas simultáneas con ventana de 14 días); los años son los de cada mecanismo.")
    _head(f, "La confianza en capas: qué actúa antes, durante y después de una estancia")
    cols = [("Antes de reservar", "teal", "Reseñas y valoración del anuncio (visible con 3 reseñas o más); descripción del anfitrión y reglas de la casa."),
            ("Al pagar", "gold", "Plataforma de pagos propia (2008); el cobro usa una clave de idempotencia para no repetirse."),
            ("Durante la estancia", "coral", "Mensajes con el anfitrión; AirCover para huéspedes (2022): reubicación o reembolso; avisar en 72 horas; línea de seguridad 24 horas."),
            ("Después", "navy", "Reseñas de ambas partes con ventana de 14 días: se publican cuando ambas se envían o vence el plazo.")]
    x = 20
    for title, kind, body in cols:
        f.box(x, 55, 210, 44, title, kind, 14, bold=True)
        f.box(x, 110, 210, 150, body, "plain", 13)
        x += 225
    for i in range(3):
        f.arrow([(20 + i * 225 + 210, 77), (20 + (i + 1) * 225, 77)])
    f.box(20, 280, 440, 80, "Para el anfitrión: Garantía de 1 millón de dólares (2012) y AirCover para anfitriones (2021); el calendario de liberación de pagos no se verificó aquí.", "plain", 13)
    f.box(480, 280, 440, 80, "Para la ciudad: City Portal (2020) para que los gobiernos locales entiendan y hagan cumplir el alquiler responsable.", "plain", 13)
    y = _notebox(f, 376, "Lectura: de izquierda a derecha el orden de una reserva; cada columna dice qué incertidumbre reduce y qué mecanismo lo hace. Ninguna capa basta sola: las reseñas no devuelven el dinero y la cobertura no dice cómo era la casa. Dónde deja de valer: es un esquema de mecanismos públicos; Airbnb no publica el desempeño de cada capa (cuántos casos resuelve AirCover, cuántas reseñas se retiran) ni sus controles de fraude. AirCover no es un seguro, según la propia página.")
    _footer(f, y + 6, "Fuentes: Airbnb Newsroom (F1); ayuda de reseñas (F4); AirCover para huéspedes (F6). Dibujo propio.")
    return f


# ---------------------------------------------------------------- Orpheus: tres fases
def orpheus_fases() -> Fig:
    f = Fig(940, 0, "Orpheus: cada solicitud se parte en tres fases y la red nunca toca la transacción",
            "Diagrama de las tres fases de una solicitud en la biblioteca de idempotencia Orpheus de Airbnb: pre-RPC (se registra la solicitud en la base de datos dentro de una transacción), RPC (llamada por red al procesador de pagos, sin base de datos) y post-RPC (se registra la respuesta dentro de otra transacción); las llamadas de red y las transacciones están separadas.")
    _head(f, "Orpheus: tres fases por solicitud y la red nunca toca la transacción")
    f.group(20, 50, 280, 190, "Pre-RPC (transacción 1)", "teal")
    f.box(40, 90, 240, 66, "Se toma la clave y el contrato; se registra el detalle del pago", "plain", 13)
    f.box(40, 166, 240, 56, "Sin llamadas de red", "grey", 13)
    f.group(330, 50, 280, 190, "RPC (sin base de datos)", "gold")
    f.box(350, 90, 240, 66, "Llamada por red al servicio externo: procesador, banco adquirente", "plain", 13)
    f.box(350, 166, 240, 56, "Aquí van cálculos o consultas idempotentes", "grey", 13)
    f.group(640, 50, 280, 190, "Post-RPC (transacción 2)", "coral")
    f.box(660, 90, 240, 66, "Se registra la respuesta: éxito, y si un fallo es reintentable o no", "plain", 13)
    f.box(660, 166, 240, 56, "Sin llamadas de red", "grey", 13)
    f.arrow([(300, 145), (330, 145)])
    f.arrow([(610, 145), (640, 145)])
    f.box(20, 260, 440, 80, "Regla 1: ninguna interacción de red en pre y post-RPC. Regla 2: ninguna interacción con la base de datos durante el RPC. Mezclarlas agotó rápidamente los pools de conexiones.", "gold", 13)
    f.box(480, 260, 440, 80, "Costo: cada llamada de API se refactoriza en tres tramos y algunas llamadas complejas son difíciles de partir así; se usan lambdas de Java para juntar las instrucciones en una sola transacción.", "coral", 13)
    y = _notebox(f, 356, "Lectura: arriba, de izquierda a derecha, el orden de una solicitud; las dos reglas de abajo son lo que da atomicidad a cada tramo de base de datos. Dónde deja de valer: la descripción es de 2019 y de un caso simple de un único RPC; la fuente dice que Orpheus admite varias llamadas pero no las detalla. No se sabe qué parte del código actual sigue así.")
    _footer(f, y + 6, "Fuente: Chew y Khisti, «Avoiding double payments in a distributed payments system», Airbnb Tech Blog, 16 de abril de 2019 (F5).")
    return f


# ---------------------------------------------------------------- cobro con reintento tras pérdida de respuesta
def cobro_reintento() -> Fig:
    f = Fig(940, 0, "Un cobro cuya respuesta se pierde: el reintento no cobra dos veces",
            "Secuencia de un cobro con clave de idempotencia cuando la respuesta se pierde: el cliente envía el cobro, el servicio toma el contrato sobre la clave en la base maestra, llama al procesador y guarda la respuesta; la respuesta no llega al cliente, que reintenta con la misma clave y recibe la respuesta guardada sin repetir el cobro.")
    _head(f, "Un cobro cuya respuesta se pierde: el reintento no cobra dos veces")
    end = _seq(f, ["Cliente\n(reserva)", "Servicio de pagos\n(Orpheus)", "Base maestra", "Procesador\nexterno"], [
        (0, 1, "1. cobro con clave K"),
        (1, 2, "2. toma contrato (bloqueo de fila) sobre K"),
        (1, 3, "3. RPC: cobra al huésped"),
        (3, 1, "4. éxito", True),
        (1, 2, "5. guarda la respuesta de K"),
        (1, 0, "6. la respuesta se pierde", True),
        (0, 1, "7. reintenta con la misma clave K"),
        (1, 2, "8. lee la respuesta de K (maestra)"),
        (1, 0, "9. devuelve la respuesta guardada", True),
    ], 52, step_h=42)
    y = _notebox(f, end + 10, "Lectura: la flecha continua es una petición y la discontinua una respuesta; el paso 6 es el fallo que se quiere cubrir. El contrato (lease) tiene caducidad: si el servicio no responde, un reintento solo procede cuando el contrato ha vencido; se recomienda que la caducidad sea mayor que el tiempo de espera del RPC. Dónde deja de valer: cubre repeticiones de la misma solicitud, no un cobro lógicamente equivocado ni fraude; el cliente debe conservar la clave y no cambiar la solicitud al reintentar.")
    _footer(f, y + 6, "Fuente: Airbnb Tech Blog (F5). Secuencia propia a partir del texto.")
    return f


# ---------------------------------------------------------------- retraso de réplica
def replica() -> Fig:
    f = Fig(940, 0, "Por qué la idempotencia se lee de la base maestra: el retraso de réplica duplica el pago",
            "Comparación de dos escenarios: si el servicio guarda las respuestas en una réplica, un reintento durante el retraso de replicación no encuentra la respuesta y el cobro se repite; si guarda y lee solo en la base maestra, el reintento encuentra la respuesta y devuelve la guardada.")
    _head(f, "Por qué la idempotencia se lee de la maestra: el retraso de réplica duplica el pago")
    f.box(20, 55, 440, 40, "Si se lee de una réplica (mal)", "coral", 14, bold=True)
    f.box(480, 55, 440, 40, "Si se lee solo de la maestra (bien)", "teal", 14, bold=True)
    left = ["1. cobro 1 con éxito; la respuesta queda en la maestra", "2. el cliente no recibe la respuesta y reintenta", "3. la réplica aún no recibió la respuesta (retraso de replicación)", "4. el servicio «no encuentra» la respuesta y vuelve a cobrar", "Resultado: pago duplicado"]
    right = ["1. cobro 1 con éxito; la respuesta queda en la maestra", "2. el cliente no recibe la respuesta y reintenta", "3. el servicio lee la maestra y encuentra la respuesta", "4. devuelve la respuesta guardada, sin cobrar de nuevo", "Resultado: un solo pago"]
    y = 105
    for i, (a, b) in enumerate(zip(left, right)):
        last = i == len(left) - 1
        f.box(20, y, 440, 50, a, "coral" if last else "plain", 13, bold=last)
        f.box(480, y, 440, 50, b, "teal" if last else "plain", 13, bold=last)
        y += 60
    f.box(20, y + 4, 900, 70, "Costo de la solución: una sola base maestra sería un cuello de botella; Airbnb la fragmenta por clave de idempotencia, que tiene alta cardinalidad y distribución pareja, y por eso funciona como clave de fragmentación.", "gold", 13)
    y = _notebox(f, y + 90, "Lectura: los dos escenarios son idénticos hasta el paso 2; la diferencia está solo en de dónde se lee. Es un ejemplo de consistencia que se compra con latencia y escalado (por eso se fragmenta). Dónde deja de valer: la fuente usa MySQL y dice que las réplicas pueden causar efectos adversos si no se configura lectura fuertemente consistente; con otra base de datos el análisis cambia.")
    _footer(f, y + 6, "Fuente: Airbnb Tech Blog (F5), sección «Avoid replica databases — Stick to master». Dibujo propio.")
    return f


# ---------------------------------------------------------------- reintentable o no
def reintentable() -> Fig:
    f = Fig(940, 0, "¿Reintentable o no? La clasificación de errores y lo que cuesta equivocarse",
            "Diagrama de decisión de la clasificación de errores en Orpheus: los errores de infraestructura (estados de la familia 5xx) se tratan como reintentables y los de validación (4xx) como no reintentables; clasificar mal un error reintentable lo deja fallando para siempre, y clasificar mal uno no reintentable puede duplicar el pago.")
    _head(f, "¿Reintentable o no? La clasificación de errores y lo que cuesta equivocarse")
    f.box(330, 55, 280, 56, "Falla una llamada", "navy", 14, bold=True)
    f.box(20, 150, 400, 80, "Error de red o de infraestructura (5xx): se espera transitorio, así que es REINTENTABLE", "teal", 13)
    f.box(520, 150, 400, 80, "Error de validación (4xx): entrada o estado inválido, por ejemplo reembolsar un reembolso; es NO REINTENTABLE", "gold", 13)
    f.arrow([(400, 111), (220, 150)])
    f.arrow([(540, 111), (720, 150)])
    f.box(20, 250, 400, 100, "Equivocación 1: etiquetar como no reintentable un fallo transitorio. El pago queda fallido de forma indefinida y los reintentos devuelven siempre el error incorrecto.", "coral", 13)
    f.box(520, 250, 400, 100, "Equivocación 2: etiquetar como reintentable algo que exige intervención manual. Puede haber pagos duplicados.", "coral", 13)
    f.arrow([(220, 230), (220, 250)])
    f.arrow([(720, 230), (720, 250)])
    f.box(20, 365, 900, 56, "Regla por defecto: la clase de excepción genérica asume NO reintentable y marca como reintentables solo casos concretos.", "plain", 13)
    y = _notebox(f, 436, "Lectura: la decisión sale de la causa, no del síntoma; los dos recuadros rojos son los dos costos de clasificar mal, simétricos y opuestos. Dónde deja de valer: la propia fuente reconoce casos ambiguos, como un valor nulo que viene de la base de datos por una falla de conexión frente a un campo nulo erróneo en la solicitud, que exigen criterio y no una regla de estado HTTP.")
    _footer(f, y + 6, "Fuente: Airbnb Tech Blog (F5), sección sobre manejo de excepciones. Dibujo propio.")
    return f


# ---------------------------------------------------------------- niveles de clave de idempotencia
def clave() -> Fig:
    f = Fig(940, 0, "Elegir la clave de idempotencia: por solicitud o por entidad",
            "Comparación de la idempotencia por solicitud, con una clave aleatoria y única como un UUID que permite varios pagos distintos de una misma reserva, y la idempotencia por entidad, con una clave determinista como pago-1234-reembolso que garantiza que un pago se reembolse una sola vez.")
    _head(f, "Elegir la clave de idempotencia: por solicitud o por entidad")
    f.box(20, 55, 440, 44, "Por solicitud (la más común)", "teal", 14, bold=True)
    f.box(480, 55, 440, 44, "Por entidad (más estricta)", "gold", 14, bold=True)
    f.box(20, 110, 440, 70, "Clave aleatoria y única generada por el cliente, por ejemplo un UUID. Cada solicitud nueva tiene una clave nueva; los reintentos reutilizan la suya.", "plain", 13)
    f.box(480, 110, 440, 70, "Clave determinista derivada de la entidad, por ejemplo «pago-1234-reembolso». Todo reembolso de ese pago comparte clave.", "plain", 13)
    f.box(20, 195, 440, 80, "Permite varios pagos distintos para una misma reserva (por ejemplo pagar menos por adelantado y el resto después): basta con que las claves difieran.", "plain", 13)
    f.box(480, 195, 440, 80, "Garantiza que un pago de 10 dólares con identificador 1234 se reembolse 5 dólares una sola vez, aunque técnicamente se podrían pedir dos reembolsos de 5.", "plain", 13)
    f.box(20, 290, 440, 70, "Costo: no protege de que el cliente genere dos solicitudes distintas para la misma intención.", "coral", 13)
    f.box(480, 290, 440, 70, "Costo: restringe casos legítimos (dos reembolsos parciales) y exige un modelo de entidades bien definido.", "coral", 13)
    y = _notebox(f, 376, "Lectura: dos columnas con la misma estructura (qué es, qué permite, qué cuesta). La elección depende del caso de uso de negocio. En ambos, el cliente debe guardar la clave antes de llamar, reutilizarla en los reintentos, no modificar la solicitud y configurar sus reintentos con retroceso y variación aleatoria. Dónde deja de valer: los ejemplos de claves son los del blog; no se publica cómo se eligen en cada servicio.")
    _footer(f, y + 6, "Fuente: Airbnb Tech Blog (F5), sección «How to choose an idempotency key?». Dibujo propio.")
    return f


# ---------------------------------------------------------------- DAG de pasos
def dag_pagos() -> Fig:
    f = Fig(940, 0, "Orquestación de pagos: un flujo como grafo de pasos idempotentes y reintentables",
            "Diagrama ilustrativo de un flujo de pago como grafo acíclico dirigido de pasos idempotentes y reintentables: validación, precio, procesamiento del pago y reporte financiero, con lógica de pago separada de la lógica del producto y un bus de mensajes basado en Kafka cuyos procesadores convierten la entrega al menos una vez en un efecto exactamente una vez.")
    _head(f, "Orquestación de pagos: un flujo como grafo de pasos idempotentes y reintentables")
    f.box(20, 85, 160, 60, "Validación", "teal", 14, bold=True)
    f.box(230, 50, 160, 60, "Precio genérico", "teal", 14, bold=True)
    f.box(230, 120, 160, 60, "Método de pago", "teal", 14, bold=True)
    f.box(440, 85, 190, 60, "Procesamiento del pago", "navy", 14, bold=True)
    f.box(680, 50, 240, 60, "Reporte financiero", "teal", 14, bold=True)
    f.box(680, 120, 240, 60, "Aviso al producto (evento)", "gold", 13)
    f.arrow([(180, 105), (230, 80)])
    f.arrow([(180, 125), (230, 150)])
    f.arrow([(390, 80), (440, 105)])
    f.arrow([(390, 150), (440, 125)])
    f.arrow([(630, 105), (680, 80)])
    f.arrow([(630, 125), (680, 150)])
    f.box(20, 205, 440, 90, "Cada paso es idempotente y reintentable con comportamiento definido; así la orquestación mantiene la consistencia eventual con la pasarela de pagos y con el cumplimiento del producto: Airbnb declara «cinco nueves» (99,999 %) de consistencia.", "plain", 13)
    f.box(480, 205, 440, 90, "Eventos por un bus basado en Kafka (al menos una vez); los procesadores de eventos usan el marco de idempotencia para lograr un efecto de exactamente una vez.", "plain", 13)
    f.box(20, 310, 440, 80, "Separación: la lógica de pago (validación, procesamiento, reporte) está aislada de la lógica del producto, salvo unos pocos puntos de integración definidos.", "teal", 13)
    f.box(480, 310, 440, 80, "Qué evita: reconstruir los pagos para cada producto nuevo, como Experiencias, con rarezas propias.", "gold", 13)
    y = _notebox(f, 406, "Lectura: de izquierda a derecha, un flujo de ejemplo; las flechas son dependencias entre pasos y los dos recuadros de abajo dicen cómo se garantiza que repetir un paso no repite el efecto. Dónde deja de valer: el grafo es un ejemplo mío con los nombres de flujo que da la fuente (validación, procesamiento de pagos, reporte financiero); no es el grafo real y los «cinco nueves» son una medición interna de consistencia, no de disponibilidad.")
    _footer(f, y + 6, "Fuente: Ross y otros, «Rebuilding Payment Orchestration at Airbnb», Airbnb Tech Blog, 24 de febrero de 2022 (F7).")
    return f


# ---------------------------------------------------------------- datos inmutables: versiones de plan
def versiones_plan() -> Fig:
    f = Fig(940, 0, "Datos inmutables: una estancia que cambia se modela como una nueva versión del plan",
            "Diagrama ilustrativo de datos inmutables en la orquestación de pagos de Airbnb: un plan de dinero para una estancia de tres noches es la versión 1; al añadir una noche se crea la versión 2 sin modificar la anterior; los eventos son solo de añadir; la historia completa de versiones y eventos permite auditar y reconciliar el dinero previsto y el movido.")
    _head(f, "Datos inmutables: una estancia que cambia es una nueva versión del plan")
    f.box(20, 60, 250, 90, "Versión 1 del plan\n(estancia de 3 noches)\nninguna se modifica", "teal", 13, bold=True)
    f.box(330, 60, 250, 90, "Versión 2 del plan\n(se añade una noche)\nnueva versión", "gold", 13, bold=True)
    f.box(640, 60, 280, 90, "Versión 3...\n(cualquier cambio posterior)", "grey", 13)
    f.arrow([(270, 105), (330, 105)])
    f.arrow([(580, 105), (640, 105)])
    f.box(20, 175, 900, 50, "Eventos de dinero (solo se añaden): cobro previsto, cobro hecho, pago al anfitrión... el consumidor decide si un evento nuevo modifica uno anterior", "plain", 13)
    f.box(20, 240, 440, 80, "Historia completa: el conjunto de versiones y eventos da el dinero previsto y el realmente movido en cada momento.", "teal", 13)
    f.box(480, 240, 440, 80, "Qué cuesta: más datos que guardar y consultar; quien lee debe reconstruir el estado a partir de versiones.", "coral", 13)
    y = _notebox(f, 336, "Lectura: de izquierda a derecha, las versiones nacen sin borrar las anteriores; los eventos viven debajo como registro de añadidos. Los datos inmutables son más fáciles de entender, auditar y reconciliar, según la fuente. Dónde deja de valer: la figura usa el ejemplo de la fuente (añadir una noche) con números míos; el coste de almacenamiento es análisis propio y la fuente no publica volúmenes.")
    _footer(f, y + 6, "Fuente: Airbnb Tech Blog (F7), sección «Data Immutability». Dibujo propio.")
    return f


# ---------------------------------------------------------------- migración de pagos en cuatro fases
def migracion() -> Fig:
    f = Fig(940, 0, "La migración de los pagos: cuatro fases, dos sistemas en paralelo y una capa de traducción",
            "Diagrama de la migración de la orquestación de pagos de Airbnb en cuatro fases (precios, pagos a anfitriones, reservas y migración de datos), con reservas de estancias divididas en más de 30 hitos, dos sistemas en paralelo durante casi todo el proceso, una capa de traducción para los consumidores de datos y trabajos de comparación entre el modelo nuevo y el antiguo.")
    _head(f, "La migración de los pagos: cuatro fases, dos sistemas en paralelo y traducción")
    labels = [("1. Precios\n(modelo genérico)", "teal"), ("2. Pagos a\nanfitriones", "teal"), ("3. Reservas\n(estancias, experiencias)", "gold"), ("4. Migración\nde datos", "navy")]
    x = 20
    for t, k in labels:
        f.box(x, 60, 210, 76, t, k, 13, bold=True)
        x += 225
    for i in range(3):
        f.arrow([(20 + i * 225 + 210, 98), (20 + (i + 1) * 225, 98)])
    f.box(20, 155, 900, 56, "Durante casi todo el proceso hubo dos sistemas de orquestación: las reservas nuevas elegibles iban a SOA y el resto seguía en el monolito; solo al final se pasaron las reservas activas.", "plain", 13)
    f.box(20, 226, 440, 90, "Capa de traducción: devuelve a los consumidores un modelo de datos unificado, de modo que no sepan de qué sistema vienen; desacopló a quienes migraban de quienes consumían datos.", "teal", 13)
    f.box(480, 226, 440, 90, "Validación: control de calidad manual de cientos de escenarios, pruebas unitarias, de integración y de extremo a extremo, y trabajos asíncronos que comparan los datos de ambos modelos.", "gold", 13)
    f.box(20, 331, 440, 90, "Costo: mantener dos sistemas dobla el trabajo de algunas funciones o las difiere; los equipos de producto se ven frenados por una migración parcial.", "coral", 13)
    f.box(480, 331, 440, 90, "Decisión: rediseñar y no reemplazar uno a uno; la migración tardó más que una réplica directa, pero evita reconstruir pagos para cada producto.", "plain", 13)
    y = _notebox(f, 436, "Lectura: arriba, el orden de las fases; debajo, cómo se convivió con el sistema antiguo y qué costó. Las reservas de estancias se subdividieron en más de 30 hitos por características. Dónde deja de valer: la fuente (2022) no da fechas, duración total ni la proporción de bookings migrados en cada momento; el costo del recuadro rojo viene de la propia fuente, el de la decisión es lectura mía.")
    _footer(f, y + 6, "Fuente: Airbnb Tech Blog (F7), secciones «A Phased Migration» y «Maintaining Two Systems».")
    return f


# ---------------------------------------------------------------- servicio con IDL
def idl() -> Fig:
    f = Fig(940, 0, "Servicios con IDL: un contrato en Thrift genera servidor y clientes en varios lenguajes",
            "Diagrama del enfoque de Airbnb de 2017 para escalar el desarrollo de servicios: se mantiene el marco Dropwizard y se añade una definición de interfaz Thrift; de ese archivo se generan el código de servidor y los clientes RPC en Java y Ruby con instrumentación estándar, y el transporte pasa de JSON sobre HTTP a Thrift sobre HTTP sin una gran reconstrucción de la infraestructura.")
    _head(f, "Servicios con IDL: un contrato en Thrift genera servidor y clientes")
    f.box(20, 60, 200, 80, "Archivo de interfaz (.thrift): API y esquemas", "navy", 13, bold=True)
    f.box(280, 40, 200, 56, "Servidor Java generado (Dropwizard)", "teal", 13)
    f.box(280, 110, 200, 56, "Clientes RPC generados (Java, Ruby)", "teal", 13)
    f.box(540, 40, 380, 56, "Instrumentación estándar: métricas, contexto de solicitud, excepciones, TLS mutuo, alertas", "gold", 13)
    f.box(540, 110, 380, 56, "Tipos extendidos (Date, DateTime) para que nadie «disfrace» una fecha como texto", "gold", 13)
    f.arrow([(220, 90), (280, 68)])
    f.arrow([(220, 110), (280, 138)])
    f.arrow([(480, 68), (540, 68)])
    f.arrow([(480, 138), (540, 138)])
    f.box(20, 190, 440, 90, "Antes: REST con JSON. Sin interfaz ni esquema fuertemente tipados, el contrato se leía del código; clientes en Ruby y Java escritos a mano; cargas JSON grandes en los percentiles 95 y 99.", "coral", 13)
    f.box(480, 190, 440, 90, "Por qué no cambiar todo a Thrift o gRPC completos: exigiría una gran reconstrucción de la infraestructura y frenaría la productividad; se eligió una vía incremental.", "plain", 13)
    f.box(20, 295, 900, 60, "Resultado buscado: usar las mismas horas de ingeniería para construir más servicios más robustos, con compatibilidad hacia atrás verificada por el esquema.", "teal", 13)
    y = _notebox(f, 370, "Lectura: un solo archivo es la fuente de la que se derivan servidor, clientes y tooling. Antes de la IDL, el costo de crear servicios llevaba a ingeniería y gestión a evitar la arquitectura orientada a servicios cuando había presión de tiempo. Dónde deja de valer: la figura describe la propuesta de 2017 (parte 1 de una serie); no mide cuánto se redujo el esfuerzo ni cuántos servicios hay hoy.")
    _footer(f, y + 6, "Fuente: Guo, Lin y Guan, «Building Services at Airbnb, Part 1», Airbnb Tech Blog, 12 de diciembre de 2017 (F9).")
    return f


# ---------------------------------------------------------------- evolución del ranking
def ranking() -> Fig:
    f = Fig(940, 0, "La búsqueda: del puntaje manual a redes neuronales, paso a paso",
            "Flujo de la evolución del modelo de ordenación de resultados de Airbnb según dos artículos de investigación: función de puntaje manual, árboles de decisión con gradiente (uno de los mayores saltos en reservas), una meseta, una red simple neutral, una red con optimización de NDCG, una red con árboles y factorización como entradas y una red profunda entrenada con 1.700 millones de pares, y después arquitectura de dos torres, sesgo de posición y arranque en frío.")
    _head(f, "La búsqueda: del puntaje manual a redes neuronales, paso a paso")
    steps = [("Puntaje\nmanual", "grey"), ("Árboles con\ngradiente", "teal"), ("Meseta: pruebas\nneutras", "coral"), ("Red simple de\n32 neuronas:\nneutral", "gold"), ("Red con\nNDCG por pares", "gold"), ("Red profunda\n(1.700 M de\npares)", "navy")]
    x = 20
    for t, k in steps:
        f.box(x, 60, 140, 90, t, k, 13, bold=(k == "navy"))
        x += 150
    for i in range(5):
        f.arrow([(20 + i * 150 + 140, 105), (20 + (i + 1) * 150, 105)])
    f.box(20, 175, 440, 90, "Lección documentada: el primer éxito con redes fue empatar con el modelo anterior; la mejora vino de reformular el objetivo (pares y NDCG) y de simplificar una complejidad que había crecido.", "plain", 13)
    f.box(480, 175, 440, 90, "Fallo instructivo: usar el identificador de cada anuncio como entrada sobreajustó; los anuncios tienen pocas reservas por unidad. Se probó un modelo con reservas y vistas largas: subieron las vistas y las reservas quedaron neutras.", "coral", 13)
    f.box(20, 280, 290, 100, "Después (2020): arquitectura de dos torres, +0,6 % de reservas en prueba A/B.", "teal", 13)
    f.box(325, 280, 290, 100, "Sesgo de posición: la posición como entrada con regularización, +0,7 % de reservas y +1,8 % de ingresos.", "teal", 13)
    f.box(630, 280, 290, 100, "Arranque en frío: estimar las señales de un anuncio nuevo, +14 % de reservas de anuncios nuevos.", "teal", 13)
    y = _notebox(f, 396, "Lectura: arriba, el camino de 2018; abajo, tres mejoras del artículo de 2020 con su resultado en pruebas A/B. Dónde deja de valer: los porcentajes son de experimentos concretos de Airbnb contra su modelo de entonces; no se transfieren, y los artículos no publican el valor absoluto de las reservas.")
    _footer(f, y + 6, "Fuentes: Haldar y otros, arXiv:1810.09591 (F8) y arXiv:2002.05515 (F12). Resumen propio.")
    return f


# ---------------------------------------------------------------- resultados de pruebas A/B
def resultados_ab() -> Fig:
    return grouped_bars(
        "Mejoras publicadas por pruebas A/B de la búsqueda de Airbnb (cambio relativo en reservas, %)",
        "Barras con los cambios en reservas publicados en el artículo de 2020: arquitectura de dos torres más 0,6 por ciento, sesgo de posición más 0,7 por ciento y arranque en frío más 0,38 por ciento en el total; el mismo artículo cuenta dos experimentos de precio monótono que bajaron las reservas un 1,5 y un 1,6 por ciento.",
        ["Dos torres", "Sesgo de posición", "Arranque en frío (total)"],
        [("Cambio relativo en reservas (%)", [0.6, 0.7, 0.38], "teal")],
        unit="Cambio relativo en reservas (%)", decimals=2, plot_h=240, width=940,
        note="Lectura: los cambios que salen en producción son de décimas de punto porcentual. El mismo artículo publica dos experimentos que empeoraron las reservas (forzar que el modelo prefiera lo más barato: menos 1,5 % y menos 1,6 %); no se dibujan porque las barras negativas no caben en esta escala, pero están en el texto. Dónde deja de valer: cada barra es un experimento distinto contra una referencia distinta y se lee solo como orden de magnitud.",
        note_kind="gold", foot="Fuente: Haldar y otros, «Improving Deep Learning For Airbnb Search», arXiv:2002.05515 (F12).")


# ---------------------------------------------------------------- dos torres
def dos_torres() -> Fig:
    f = Fig(940, 0, "Arquitectura de dos torres: un vector «ideal» por búsqueda y uno por anuncio",
            "Diagrama de la arquitectura de dos torres del ranking de Airbnb: una torre recibe las características de la consulta y del usuario y genera un vector de 100 dimensiones que representa el anuncio ideal; otra torre recibe las características de cada anuncio; se puntúa según la cercanía; la torre de consulta se evalúa una sola vez por búsqueda, lo que reduce la latencia.")
    _head(f, "Arquitectura de dos torres: un vector ideal por búsqueda y uno por anuncio")
    f.box(20, 60, 250, 80, "Consulta y usuario: destino, fechas, huéspedes, historial", "plain", 13)
    f.box(20, 170, 250, 80, "Anuncios candidatos: precio, ubicación, comodidades, señales", "plain", 13)
    f.box(320, 60, 220, 80, "Torre de consulta\n(se evalúa 1 vez por\nbúsqueda)", "navy", 13, bold=True)
    f.box(320, 170, 220, 80, "Torre de anuncio\n(se evalúa por cada\nanuncio)", "navy", 13, bold=True)
    f.arrow([(270, 100), (320, 100)])
    f.arrow([(270, 210), (320, 210)])
    f.box(590, 60, 330, 80, "Vector de 100 dimensiones: el «anuncio ideal» para esa consulta", "gold", 13)
    f.box(590, 170, 330, 80, "Vector del anuncio; puntaje = cercanía al ideal", "gold", 13)
    f.arrow([(540, 100), (590, 100)])
    f.arrow([(540, 210), (590, 210)])
    f.box(20, 270, 440, 90, "Entrenamiento: pares de anuncios, uno reservado y otro no; la pérdida mide cuánto más cerca del ideal está el reservado.", "plain", 13)
    f.box(480, 270, 440, 90, "Beneficio de latencia: como la torre de consulta no depende del anuncio, se calcula una vez y solo se evalúa la torre de anuncio por cada resultado.", "teal", 13)
    y = _notebox(f, 376, "Lectura: dos entradas, dos torres y una comparación de vectores; el vector de consulta es el mismo para todos los anuncios de esa búsqueda. En la prueba A/B contra una red totalmente conectada de dos capas, la reserva subió +0,6 %. Dónde deja de valer: la figura abstrae el modelo; los autores se preguntaron si la red hacía lo previsto y analizaron los vectores, pero el artículo no publica las dimensiones internas de cada torre.")
    _footer(f, y + 6, "Fuente: Haldar y otros, arXiv:2002.05515 (F12), sección 2.6. Dibujo propio.")
    return f


# ---------------------------------------------------------------- crisis de 2020
def crisis() -> Fig:
    return stacked_bars(
        "La crisis de mayo de 2020: de cada 7.500 empleados, casi 1.900 tuvieron que irse",
        "Barra apilada de la plantilla de Airbnb en mayo de 2020: unos 5.600 empleados permanecen y casi 1.900, alrededor del 25 por ciento de los 7.500, salen; la empresa preveía ingresos de menos de la mitad de los de 2019 y había levantado 2 mil millones de dólares.",
        ["Plantilla en mayo de 2020"],
        [("Se quedan (cálculo propio)", [5600], "teal"), ("Se van (casi 1.900)", [1900], "coral")],
        unit="Empleados", horizontal=True, decimals=0, plot_h=150, label_w=150,
        note="Lectura: el recorte fue de un cuarto de la plantilla, mapeado a una estrategia más enfocada en el núcleo (anfitriones y experiencias de la comunidad) y con pausa en Transporte y Estudios y reducción en Hoteles y Lux. Dónde deja de valer: 5.600 es mi resta (7.500 − casi 1.900); la carta da cifras redondeadas («casi», «alrededor») y es la versión de la dirección.",
        note_kind="gold", foot="Fuente: Brian Chesky, mensaje de mayo de 2020 (F11).")


# ---------------------------------------------------------------- Q4 2025
def q4() -> Fig:
    return grouped_bars(
        "Cuarto trimestre de 2025: crecimiento interanual de las magnitudes que publica Airbnb (%)",
        "Barras con los crecimientos interanuales del cuarto trimestre de 2025: ingresos 12 por ciento, valor bruto de reservas 16 por ciento, noches y plazas reservadas 10 por ciento, y noches reservadas desde India 50 por ciento.",
        ["Ingresos", "Valor bruto de reservas", "Noches y plazas reservadas", "Noches desde India"],
        [("Crecimiento interanual (%)", [12, 16, 10, 50], "teal")],
        unit="Crecimiento interanual (%)", decimals=0, plot_h=240,
        note="Lectura: el valor bruto de reservas crece más que los ingresos y que las noches, lo que Airbnb atribuye a la demanda y al precio medio diario (ADR); India es una cifra de un país de expansión que parte de una base menor. Dónde deja de valer: es un trimestre; el comunicado dice que la mayor parte del negocio se concentra en cinco países.",
        note_kind="gold", foot="Fuente: Airbnb, resultados del cuarto trimestre de 2025 (F2).")


# ---------------------------------------------------------------- línea de tiempo ampliada
def linea_tiempo2() -> Fig:
    return timeline(
        "Airbnb: confianza y pagos, producto y empresa",
        "Línea de tiempo de 2007 a 2026 con tres carriles: confianza y pagos (pagos propios en 2008, garantía en 2012, City Portal y Project Lighthouse en 2020, AirCover en 2021 y 2022), producto (alojamiento, experiencias, servicios) y empresa (privada, cotizada); marcadores de lanzamiento, pagos, garantía, crisis y salida a bolsa.",
        [("Confianza y pagos", [(2008.6, 2012.4, "Pagos propios", "teal"), (2012.4, 2020.4, "Garantía y confianza", "gold"), (2020.4, 2026, "AirCover y City Portal", "coral")]),
         ("Producto", [(2008.2, 2016.8, "Alojamiento", "navy"), (2016.8, 2025.3, "Experiencias", "gold"), (2025.3, 2026, "", "coral")]),
         ("Empresa", [(2007.8, 2020.9, "Empresa privada", "grey"), (2020.9, 2026, "Empresa cotizada", "navy")])],
        unit="Año", events=[(2008.2, "SXSW"), (2012.4, "Garantía"), (2020.4, "Crisis"), (2020.9, "Bolsa")], t_max=2026, ticks=[2007, 2010, 2013, 2016, 2019, 2022, 2026], lane_h=54, label_w=150,
        note="Documentado en la historia de Airbnb (F1): lanzamiento en el SXSW de marzo de 2008, plataforma de pagos en agosto de 2008, Garantía de 1 millón en mayo de 2012, Experiencias en noviembre de 2016, mayo de 2020 reducción de plantilla (F11), City Portal en septiembre de 2020, bolsa en diciembre de 2020, AirCover para anfitriones en 2021 y para huéspedes en 2022, Servicios y Experiencias renovadas en 2025. Las eras son síntesis del autor.",
        note_kind="gold", foot="Fuentes: F1, F11; síntesis propia de las eras.")



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
    return _cards('Hardware de Airbnb: casi nada se publica', 'Diagrama del hardware de Airbnb según sus fuentes: no se publica el tipo de servidores ni el proveedor de nube; las fuentes mencionan bases de datos MySQL con un nodo maestro fragmentado y réplicas, y entrenamiento de redes neuronales con miles de millones de pares; los dispositivos de usuario son la aplicación móvil y la web.', [('Servidores y nube', 'teal', ['No se sabe: proveedor de nube, tipo de servidor, regiones y si la infraestructura es propia, alquilada o híbrida: ninguna de las fuentes consultadas lo dice.']), ('Bases de datos', 'gold', ['Documentado: bases MySQL con un maestro fragmentado por clave de idempotencia y réplicas con retraso de replicación (F5).', 'No se sabe: cantidad de fragmentos, tamaño de datos y hardware de almacenamiento.']), ('Aprendizaje automático', 'navy', ['Documentado: entrenamiento con 1.700 millones de pares en 2018 (F8).', 'No se sabe: aceleradores, GPU u otro hardware de entrenamiento y de servido.']), ('Dispositivos de usuario', 'grey', ['Documentado: aplicación móvil e Instant Book desde noviembre de 2010 (F1), y web.', 'No se sabe: plataformas y versiones soportadas.'])], 'Lectura: el caso casi no tiene datos de hardware público y lo declara. Dónde deja de valer: este vacío no implica que no exista; solo que las fuentes consultadas no lo detallan.', 'Fuentes: F1, F5, F8.')


def _x_software() -> Fig:
    return _cards('Software de Airbnb que sus propias fuentes documentan', 'Diagrama del software documentado de Airbnb: un monolito en Ruby on Rails y servicios en Java con Dropwizard, Jersey y Jackson; interfaces en Thrift; MySQL; Kafka; Java con lambdas y StatefulJ para máquinas de estados; TensorFlow, árboles de decisión con gradiente y máquinas de factorización para la búsqueda.', [('Lenguajes y marcos', 'teal', ['Documentado: monolito en Ruby on Rails y servicios sobre todo en Java con el marco Dropwizard, con filtros y módulos propios (F7, F9).', 'Documentado: Jersey y Jackson para JSON sobre HTTP, que pasó a Thrift sobre HTTP (F9).']), ('Datos y mensajería', 'gold', ['Documentado: MySQL como base y Kafka como bus de mensajes de pagos (F5, F7).', 'No se sabe: almacén analítico, sistema de búsqueda y motor de indexación.']), ('Contratos y pagos', 'navy', ['Documentado: definición de interfaces con Thrift y generación de clientes en Java y Ruby (F9).', 'Documentado: biblioteca de idempotencia Orpheus en Java, con lambdas y una máquina de estados con StatefulJ (F5).']), ('Aprendizaje automático', 'grey', ['Documentado: TensorFlow para las redes de ordenación, árboles de decisión con gradiente y máquinas de factorización en la historia del modelo (F8, F12).', 'No se sabe: marco de servido y plataforma de experimentos.'])], 'Lectura: cuatro grupos tecnológicos con su fuente. Dónde deja de valer: son blogs de 2017 a 2022; no cubren frontend, móvil ni infraestructura.', 'Fuentes: F5, F7, F8, F9, F12.')


def _x_infra() -> Fig:
    return _cards('Características de la infraestructura de Airbnb: lo que se sabe y lo que no', 'Diagrama de la infraestructura de Airbnb: arquitectura orientada a servicios en transición desde un monolito, bases fragmentadas y migración de pagos con dos sistemas en paralelo; escala de 9 millones de anuncios, 70 mil millones de dólares procesados en 2019 y más de 40 monedas; sin datos públicos de nube, regiones ni costos.', [('Modelo y estructura', 'teal', ['Documentado: transición de un monolito Ruby a servicios con contrato en Thrift desde 2017 (F9); pagos rediseñados en 2022 (F7).', 'No se sabe: nube, regiones, zonas y topología.']), ('Escala', 'gold', ['Documentado: más de 9 millones de anuncios activos y más de 2.500 millones de llegadas acumuladas (F1); alrededor de 70 mil millones de dólares procesados en 2019 en más de 40 monedas (F1).', 'No se sabe: peticiones por segundo y tamaño de las bases.']), ('Costos', 'navy', ['No se sabe: costo de infraestructura: no se publica; solo hay ingresos y crecimiento (F2, F10).']), ('Redes y entrega', 'grey', ['Documentado: comunicación entre servicios con TLS mutuo y monitoreo estándar (F9).', 'No se sabe: red de distribución de contenido y de imágenes.'])], 'Lectura: casi todos los recuadros declaran falta de dato. Dónde deja de valer: la ausencia es de las fuentes consultadas.', 'Fuentes: F1, F2, F7, F9, F10.')


def _x_fallos() -> Fig:
    return _cards('Qué pasa cuando cae cada componente en lo que Airbnb documenta', 'Diagrama de la tolerancia a fallos documentada de Airbnb en pagos: una respuesta perdida se cubre con la clave de idempotencia; un procesador caído se reintenta si el error es reintentable; una réplica con retraso se evita leyendo de la maestra; dos sistemas de pagos conviven durante la migración con trabajos de comparación; un paso falla y la orquestación lo repite; no se documentan pruebas de caos ni recuperación ante desastres.', [('Se pierde una respuesta', 'teal', ['Documentado: idempotencia con clave, contrato con caducidad y respuesta guardada (F5).']), ('Cae un servicio externo', 'gold', ['Documentado: los errores de infraestructura se tratan como reintentables y los de validación no; el cliente reintenta con retroceso y variación (F5).']), ('Una réplica se atrasa', 'coral', ['Documentado: las tablas de idempotencia se leen y escriben solo en la base maestra fragmentada (F5).']), ('Falla un paso de un flujo', 'navy', ['Documentado: grafo de pasos idempotentes y reintentables; eventos con idempotencia sobre Kafka; análisis de integridad transaccional (F7).']), ('Una migración se desvía', 'plain', ['Documentado: trabajos asíncronos que comparan el modelo nuevo y el antiguo, y una capa de traducción (F7).']), ('Lo que no se documenta', 'grey', ['No se sabe: pruebas de caos, recuperación ante desastres, copias de seguridad, degradación de la búsqueda y de los mensajes.'])], 'Lectura: cada recuadro es un fallo y su defensa; el último lista lo que falta. Dónde deja de valer: solo cubre pagos; la tolerancia a fallos de la búsqueda no está descrita.', 'Fuentes: F5, F7.')


def _x_negocio() -> Fig:
    return _cards("Esquema del negocio de Airbnb: valor, ingreso, actores y flujos",
        "Diagrama del negocio de Airbnb con cinco grupos: la propuesta de valor (confianza entre desconocidos), el ingreso por comisiones sobre el valor bruto de reservas, los actores, los flujos de dinero entre huésped, anfitrión, la plataforma y los procesadores de pago, y los flujos de valor.",
        [("Propuesta de valor", "teal", ["Documentado: un alojamiento o experiencia con la certeza de que, si algo sale mal, la plataforma responde (pagos propios, reseñas, AirCover) (F1, F4, F6)."]),
         ("Ingreso", "gold", ["Documentado: comisión de servicio sobre cada reserva; ingresos de 12.241 millones de dólares en 2025 frente a 11.102 en 2024 (F13)."]),
         ("Actores", "navy", ["Huéspedes, anfitriones (más de 5,5 millones), coanfitriones, gobiernos locales, procesadores de pago, proveedores de soporte (unos 13.000 trabajadores de terceros) y Airbnb (F1, F13)."]),
         ("Flujos de dinero", "coral", ["Documentado: huésped → plataforma (precio más comisión del huésped en la estructura dividida); plataforma → anfitrión (precio menos comisión); plataforma → procesadores (tarifas de comerciante, la mayor parte del costo de ingresos) (F3, F13).", "No se sabe: el calendario de pago al anfitrión."]),
         ("Flujos de valor", "grey", ["Demanda y confianza hacia el anfitrión; capacidad ociosa y variedad hacia el huésped; impuestos recaudados y datos hacia las ciudades (F1)."])],
        "Lectura: cinco grupos de lo que se ofrece a cómo circulan dinero y valor. Dónde deja de valer: los porcentajes de comisión varían por país y tipo de anfitrión; el 10-K agrega los costos de pago en la línea de costo de ingresos.",
        "Fuentes: F1, F3, F4, F6 y formulario 10-K de 2025 (F13).")


def _x_costos() -> Fig:
    return stacked_bars(
        "A dónde fue cada dólar de ingreso de Airbnb, 2024 frente a 2025",
        "Barras apiladas al 100 por ciento: en 2025 el costo de ingresos fue 17,0 por ciento de los ingresos, operaciones, soporte y administración 21,8, desarrollo de producto 19,2, ventas y marketing 21,1 y resultado operativo 20,8; en 2024 el resultado operativo era 23,0.",
        ["2024", "2025"],
        [("Costo de ingresos", [1878, 2086], "coral"), ("Operaciones, soporte y administración", [2467, 2669], "grey"), ("Desarrollo de producto", [2056, 2354], "navy"), ("Ventas y marketing", [2148, 2588], "gold"), ("Resultado operativo", [2553, 2544], "teal")],
        unit="Porcentaje del ingreso (11.102 y 12.241 millones de dólares)", horizontal=True, percent=True, decimals=1, plot_h=210, label_w=60,
        note="Lectura: el margen operativo baja de 23 % a 21 % porque ventas y marketing sube del 19 % al 21 % de los ingresos; el costo de ingresos sube sobre todo por tarifas de comerciante. Dónde deja de valer: son rubros consolidados; el 10-K no separa el costo de infraestructura en la nube ni el de soporte de terceros.",
        note_kind="gold", foot="Fuente: Airbnb, formulario 10-K de 2025 (F13), leído con WebFetch.")

FIGURES = {
    "airbnb-contexto-confianza.svg": contexto,
    "airbnb-confianza-en-capas.svg": confianza,
    "airbnb-q4-2025-crecimiento.svg": q4,
    "airbnb-comisiones.svg": comisiones,
    "airbnb-componentes-servicios.svg": componentes,
    "airbnb-servicios-con-idl.svg": idl,
    "airbnb-flujo-pago-idempotente.svg": flujo_pago,
    "airbnb-orpheus-tres-fases.svg": orpheus_fases,
    "airbnb-cobro-con-reintento.svg": cobro_reintento,
    "airbnb-retraso-de-replica.svg": replica,
    "airbnb-reintentable-o-no.svg": reintentable,
    "airbnb-clave-de-idempotencia.svg": clave,
    "airbnb-orquestacion-de-pagos.svg": dag_pagos,
    "airbnb-datos-inmutables.svg": versiones_plan,
    "airbnb-migracion-de-pagos.svg": migracion,
    "airbnb-ventana-de-resenas.svg": resenas,
    "airbnb-busqueda-evolucion.svg": ranking,
    "airbnb-busqueda-resultados-ab.svg": resultados_ab,
    "airbnb-busqueda-dos-torres.svg": dos_torres,
    "airbnb-crisis-de-2020.svg": crisis,
    "airbnb-linea-de-tiempo.svg": linea_tiempo2,
    "airbnb-hardware-utilizado.svg": _x_hardware,
    "airbnb-software-utilizado.svg": _x_software,
    "airbnb-caracteristicas-de-la-infraestructura.svg": _x_infra,
    "airbnb-tolerancia-a-fallos.svg": _x_fallos,
    "airbnb-esquema-del-negocio.svg": _x_negocio,
    "airbnb-costos-operativos.svg": _x_costos,
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
