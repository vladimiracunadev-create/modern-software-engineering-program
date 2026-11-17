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


# ======================================================================
# Ampliación (nov. 2026): idempotencia, límites de tasa, versionado, migraciones, DocDB, estados del pago,
# webhooks, seguridad, Connect y economía. Cifras de las fuentes F1-F17 del caso.
# ======================================================================
from figure_kit import _wrap, fmt_es  # noqa: E402


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


# ---------------------------------------------------------------- idempotencia: secuencia
def idem_secuencia() -> Fig:
    f = Fig(940, 0, "Una clave de idempotencia ante una respuesta perdida: el servidor devuelve el resultado guardado",
            "Secuencia de un cobro con la cabecera Idempotency-Key cuando la respuesta se pierde: el servidor ejecuta el cobro y guarda el resultado; la conexión se corta antes de que el cliente lo reciba; el cliente reintenta con la misma clave y los mismos parámetros, y el servidor devuelve el resultado guardado sin cobrar otra vez.")
    _head(f, "Una clave de idempotencia ante una respuesta perdida")
    end = _seq(f, ["Cliente\n(comercio)", "API de Stripe\n(capa de idempotencia)", "Almacén de\nresultados", "Red de tarjetas\ny emisor"], [
        (0, 1, "1. POST con Idempotency-Key = K"),
        (1, 2, "2. ¿existe K? no: registra K"),
        (1, 3, "3. ejecuta el cobro"),
        (3, 1, "4. aprobado", True),
        (1, 2, "5. guarda el resultado de K"),
        (1, 0, "6. conexión cortada: el cliente no ve la respuesta", True),
        (0, 1, "7. reintenta con la misma K y parámetros"),
        (1, 2, "8. compara parámetros y busca K"),
        (1, 0, "9. devuelve el resultado guardado", True),
    ], 52, step_h=42)
    y = _notebox(f, end + 10, "Lectura: las flechas continuas son peticiones y las discontinuas respuestas; el paso 6 es el fallo ambiguo (el cliente no sabe si el cobro ocurrió). Si en el paso 7 los parámetros difieren de los de la petición original, la capa de idempotencia devuelve un error para evitar un uso erróneo. Dónde deja de valer: la descripción de los pasos internos 2, 5 y 8 es una lectura de lo que la documentación dice que ocurre; no se sabe cómo está implementado el almacén. Evita cobros duplicados por reintento, no cobros equivocados.")
    _footer(f, y + 6, "Fuentes: Leach, «Designing robust and predictable APIs with idempotency» (F4); Stripe Docs, «Idempotent requests» (F10). Secuencia propia.")
    return f


# ---------------------------------------------------------------- idempotencia: decisión
def idem_decision() -> Fig:
    f = Fig(940, 0, "Qué hace la capa de idempotencia con cada petición que llega con una clave",
            "Diagrama de decisión del comportamiento documentado de las claves de idempotencia de Stripe en la API v1: una clave nueva se procesa normalmente; una clave repetida con los mismos parámetros devuelve el resultado guardado, incluidos los errores 500, si la ejecución ya había empezado; una clave repetida con parámetros distintos devuelve un error; una clave antigua, de más de 24 horas, puede haberse eliminado y entonces se genera una petición nueva.")
    _head(f, "Qué hace la capa de idempotencia con cada petición que llega con una clave")
    f.box(330, 55, 280, 56, "Llega un POST con clave K", "navy", 14, bold=True)
    f.box(20, 160, 270, 90, "K nunca vista: se procesa como una petición nueva", "teal", 13)
    f.box(335, 160, 270, 90, "K vista, mismos parámetros, la ejecución ya empezó: se devuelve el resultado guardado (también si fue un 500)", "teal", 13)
    f.box(650, 160, 270, 90, "K vista, parámetros distintos: error, para evitar un uso erróneo", "gold", 13)
    f.arrow([(400, 111), (155, 160)])
    f.arrow([(470, 111), (470, 160)])
    f.arrow([(540, 111), (785, 160)])
    f.box(20, 270, 440, 90, "Si los parámetros fallan la validación o la petición choca con otra en ejecución con la misma clave, no se guarda un resultado, y puede reintentarse.", "plain", 13)
    f.box(480, 270, 440, 90, "Las claves pueden eliminarse tras 24 horas como mínimo en la API v1; si se reutiliza una clave podada, se genera una petición nueva.", "coral", 13)
    f.box(20, 375, 900, 60, "Otros límites: las claves miden hasta 255 caracteres, se recomienda un UUID v4, no deben llevar datos sensibles y no se envían en GET ni DELETE (ya son idempotentes por definición).", "plain", 13)
    y = _notebox(f, 450, "Lectura: una sola decisión (qué pasó antes con esta clave) y cuatro desenlaces. La API v2 cambia el contrato: los reintentos no repiten operaciones exitosas, y el trabajo fallido o a medias se reintenta hasta completarse cuando es posible. Dónde deja de valer: es el comportamiento documentado en 2026 para v1 y v2; la ventana de 24 horas es un mínimo y no una garantía de retención exacta.")
    _footer(f, y + 6, "Fuente: Stripe Docs, «Idempotent requests» (F10).")
    return f


# ---------------------------------------------------------------- cuatro limitadores
def limitadores() -> Fig:
    f = Fig(940, 0, "Cuatro limitadores en producción: dos preventivos y dos para emergencias",
            "Diagrama de los cuatro tipos de limitadores que Stripe describe: de tasa de peticiones por usuario y de peticiones concurrentes (preventivos), y dos que descartan carga según el estado de la flota y de los trabajadores (el primero reserva una fracción de la flota para peticiones críticas y rechaza con 503; el segundo, de última línea, descarta primero el tráfico de prueba, luego las lecturas y las escrituras, y por último lo crítico).")
    _head(f, "Cuatro limitadores en producción: dos preventivos y dos para emergencias")
    f.box(20, 50, 440, 36, "Preventivos (miran al usuario)", "teal", 14, bold=True)
    f.box(480, 50, 440, 36, "Descarte de carga (miran al sistema)", "coral", 14, bold=True)
    f.box(20, 96, 440, 100, "1. De tasa de peticiones: cada usuario puede hacer N por segundo, con una ráfaga breve por encima del tope. Es el más importante y rechaza millones de peticiones al mes, sobre todo de prueba.", "plain", 13)
    f.box(20, 206, 440, 100, "2. De peticiones concurrentes: máximo de peticiones en curso a la vez (por ejemplo 20). Protege los puntos finales costosos de que los reintentos de usuarios impacientes empeoren la contención.", "plain", 13)
    f.box(480, 96, 440, 100, "3. Por uso de la flota: reserva una fracción (por ejemplo 20 %) para métodos críticos como crear cobros; el resto se rechaza con 503 si supera su 80 %.", "plain", 13)
    f.box(480, 206, 440, 100, "4. Por uso de trabajadores: última línea. Descarta por orden: tráfico de prueba, GET, POST y, al final, métodos críticos; sube y baja despacio para no oscilar.", "plain", 13)
    f.box(20, 320, 440, 70, "Frecuencia declarada: el primero se activa constantemente; el segundo, miles de veces al mes; el cuarto, solo en incidentes mayores.", "gold", 13)
    f.box(480, 320, 440, 70, "Idea clave: el limitador de tasa pide a los clientes repartir sus peticiones; el descarte de carga mantiene vivo el núcleo cuando el resto se quema.", "gold", 13)
    y = _notebox(f, 406, "Lectura: la columna izquierda protege de un usuario que se excede; la derecha, de un sistema que ya no da abasto. Las cifras de los ejemplos (20 peticiones, 20 %) son las del artículo de 2017. Dónde deja de valer: los volúmenes y los umbrales actuales no son públicos; la documentación de hoy fija límites propios por cuenta (por ejemplo, 100 peticiones por segundo en modo real).")
    _footer(f, y + 6, "Fuente: Tarjan, «Scaling your API with rate limiters», Stripe Blog, 30 de marzo de 2017 (F5). Resumen propio.")
    return f


# ---------------------------------------------------------------- límites publicados hoy
def limites_cifras() -> Fig:
    return grouped_bars(
        "Límites de tasa publicados en la documentación de Stripe (peticiones por segundo)",
        "Barras horizontales con los límites de tasa de la documentación: 100 peticiones por segundo globales en modo real, 25 en el entorno de pruebas, 25 por punto final, 20 para lectura y para escritura de archivos, 15 creaciones de pagos a cuentas y 30 creaciones de cuentas conectadas en modo real.",
        ["Global, modo real", "Global, entorno de pruebas", "Cada punto final (salvo excepciones)", "Archivos, lectura y escritura", "Pagos a cuentas, creación", "Cuentas conectadas, creación (real)"],
        [("Peticiones por segundo", [100, 25, 25, 20, 15, 30], "teal")],
        unit="Peticiones por segundo", horizontal=True, decimals=0, label_w=260, plot_h=270,
        note="Lectura: el límite global es cuatro veces el de cada punto final y el entorno de pruebas se limita a un cuarto del modo real; así un script descontrolado en pruebas no daña a otros. La documentación añade límites de otra forma (1.000 actualizaciones por intención de pago por hora; 10 facturas nuevas por suscripción por minuto). Dónde deja de valer: son límites por cuenta y pueden cambiar; una cuenta con acuerdo especial puede tener otros.",
        note_kind="gold", foot="Fuente: Stripe Docs, «Rate limits» (F17), consulta del 2026-11-16.")


# ---------------------------------------------------------------- lanzar un limitador
def lanzar_limitador() -> Fig:
    f = Fig(940, 0, "Cómo lanzar un limitador sin romper a nadie: los seis cuidados que Stripe recomienda",
            "Flujo de buenas prácticas de lanzamiento de un limitador de tasa según Stripe: engancharlo al middleware de forma que un error del limitador o de Redis no afecte a las peticiones (fallar abierto), devolver 429 o 503 con mensajes accionables, tener interruptores para apagarlo, alertas y métricas, y lanzarlo en modo oscuro para ver qué bloquearía antes de bloquear.")
    _head(f, "Cómo lanzar un limitador sin romper a nadie: seis cuidados")
    steps = [("1. Enganchar con\nseguridad: si falla,\nfallar abierto", "teal"), ("2. Errores claros:\n429 o 503 y\nmensaje accionable", "teal"), ("3. Interruptores\npara apagarlo\n(banderas)", "gold"), ("4. Alertas y\nmétricas de cuántas\nveces se activa", "gold"), ("5. Lanzar en modo\noscuro: ver qué\nbloquearía", "navy"), ("6. Ajustar umbrales;\ntrabajar con\nusuarios afectados", "navy")]
    x = 20
    for t, k in steps:
        f.box(x, 60, 140, 100, t, k, 13, bold=(k == "navy"))
        x += 150
    for i in range(5):
        f.arrow([(20 + i * 150 + 140, 110), (20 + (i + 1) * 150, 110)])
    f.box(20, 185, 440, 90, "Implementación: algoritmo de cubo de fichas con un anfitrión centralizado; cada usuario tiene su cubo; cada petición toma una ficha y el cubo se rellena poco a poco; con el cubo vacío se rechaza. Se usa Redis.", "plain", 13)
    f.box(480, 185, 440, 90, "Mismo comportamiento en modo de pruebas y en modo real: los scripts no encuentran efectos distintos al pasar a producción.", "plain", 13)
    f.box(20, 290, 440, 80, "Costo: el limitador es un componente más que puede fallar; por eso se diseña para fallar abierto y con interruptores.", "coral", 13)
    f.box(480, 290, 440, 80, "Orden recomendado: empezar por el limitador de tasa de peticiones y añadir los otros tres con el tiempo, según la necesidad.", "teal", 13)
    y = _notebox(f, 386, "Lectura: de izquierda a derecha, el orden de un lanzamiento seguro; los recuadros de abajo dicen cómo funciona y qué cuesta. Dónde deja de valer: es la práctica descrita en 2017; no se publica cómo está implementado hoy ni cuántas peticiones rechaza.")
    _footer(f, y + 6, "Fuente: Tarjan, «Scaling your API with rate limiters» (F5), secciones «Building rate limiters in practice» y «Conclusion».")
    return f


# ---------------------------------------------------------------- versionado por módulos
def versionado() -> Fig:
    f = Fig(940, 0, "Cómo responde la API a cada versión: se formatea en la versión actual y se retrocede módulo a módulo",
            "Diagrama del mecanismo de versionado de Stripe: la respuesta se construye en la versión más reciente y luego se aplican en orden inverso los módulos de cambio de versión hasta llegar a la versión objetivo, que sale de la cabecera Stripe-Version, de la versión de una aplicación OAuth o de la versión fijada de la cuenta en su primera petición.")
    _head(f, "Cómo responde la API a cada versión: se retrocede módulo a módulo")
    f.box(20, 55, 200, 80, "Respuesta construida en la versión actual", "navy", 13, bold=True)
    f.box(260, 55, 190, 80, "Módulo de cambio 2017-05-25\n(retrocede)", "gold", 13)
    f.box(480, 55, 190, 80, "Módulo 2017-04-06\n(retrocede)", "gold", 13)
    f.box(700, 55, 220, 80, "...hasta la versión objetivo del cliente", "teal", 13, bold=True)
    f.arrow([(220, 95), (260, 95)])
    f.arrow([(450, 95), (480, 95)])
    f.arrow([(670, 95), (700, 95)])
    f.box(20, 160, 290, 100, "La versión objetivo sale de: 1) la cabecera Stripe-Version, 2) la versión de la aplicación OAuth, o 3) la versión fijada de la cuenta en su primera petición.", "plain", 13)
    f.box(325, 160, 290, 100, "Cada módulo declara documentación, una transformación y los recursos que toca; el registro de cambios y la documentación se generan de ahí.", "plain", 13)
    f.box(630, 160, 290, 100, "Cambios con efectos laterales: la transformación es nula y se comprueba en otras partes del código; son más difíciles de mantener y se evitan.", "coral", 13)
    f.box(20, 275, 440, 90, "Versiones rodantes con fecha (2017-05-24): cada una es incompatible hacia atrás pero con pocos cambios, para que actualizarse sea incremental; no hay una gran «v2» que obligue a reintegrar todo.", "teal", 13)
    f.box(480, 275, 440, 90, "Reglas de compatibilidad: los campos presentes siguen presentes y conservan nombre y tipo; añadir un campo o un punto final es seguro; cambiar un booleano por un estado, como en 2014, rompe a los clientes.", "gold", 13)
    y = _notebox(f, 380, "Lectura: la respuesta viaja hacia el pasado por una cadena de transformaciones y el desarrollador que construye un producto nuevo apenas piensa en las versiones viejas. Dónde deja de valer: el código del artículo es de 2017 y es Ruby; Stripe dice que mantiene compatibilidad con todas las versiones desde 2011 pero no publica cuántos módulos hay ni su costo de mantenimiento.")
    _footer(f, y + 6, "Fuente: Leach, «APIs as infrastructure: future-proofing Stripe with versioning», Stripe Blog, 5 de agosto de 2017 (F6).")
    return f


# ---------------------------------------------------------------- migración en cuatro pasos
def migracion_cuatro_pasos() -> Fig:
    f = Fig(940, 0, "Migración en línea en cuatro pasos: el caso de cientos de millones de suscripciones",
            "Diagrama de los cuatro pasos del patrón de migración en línea de Stripe con la migración de suscripciones: escribir en la tabla vieja y la nueva y rellenar los datos antiguos desde un proceso offline en Hadoop, cambiar las lecturas verificadas con experimentos de comparación, cambiar las escrituras y eliminar los datos antiguos; con un segundo por objeto tomaría más de tres años migrar cien millones secuencialmente.")
    _head(f, "Migración en línea en cuatro pasos: cientos de millones de suscripciones")
    steps = [("1. Escritura doble\nen tabla vieja y\ntabla nueva", "teal", "Rellenar lo antiguo desde un proceso offline (MapReduce) para no cargar la base de producción."),
             ("2. Cambiar las\nlecturas a la\ntabla nueva", "gold", "Verificar con experimentos que leen ambas y alertan si difieren (Scientist)."),
             ("3. Cambiar las\nescrituras: primero\nla nueva", "gold", "El refactor más difícil: miles de líneas en varios servicios, en trozos muy pequeños."),
             ("4. Borrar lo\nantiguo y apagar\nla ruta vieja", "navy", "La tabla nueva es la fuente de verdad; se vacía el campo antiguo de forma perezosa.")]
    x = 20
    for t, k, body in steps:
        f.box(x, 60, 210, 90, t, k, 13, bold=(k == "navy"))
        f.box(x, 165, 210, 130, body, "plain", 13)
        x += 225
    for i in range(3):
        f.arrow([(20 + i * 225 + 210, 105), (20 + (i + 1) * 225, 105)])
    f.box(20, 310, 440, 80, "Por qué importa el método: a un segundo por objeto, 100 millones de objetos tardarían más de tres años en secuencia; hay que paralelizar y hacerlo sin ventana de mantenimiento.", "coral", 13)
    f.box(480, 310, 440, 80, "Principios: pasos incrementales (nunca más de unos cientos de líneas a la vez), transparencia y observabilidad en cada paso.", "teal", 13)
    y = _notebox(f, 406, "Lectura: arriba, los cuatro pasos; debajo, qué se hizo en cada uno. La cuenta de tres años es aritmética de la propia fuente: 10^8 segundos son unos 3,2 años. Dónde deja de valer: es una migración de datos de la facturación de suscripciones, de 2017; el patrón es general pero cada paso tiene riesgos propios, y la fuente no cuenta qué incidencias aparecieron.")
    _footer(f, y + 6, "Fuente: Xu, «Online migrations at scale», Stripe Blog, 2 de febrero de 2017 (F7).")
    return f


# ---------------------------------------------------------------- arquitectura de DocDB
def docdb_arquitectura() -> Fig:
    f = Fig(940, 0, "DocDB: aplicaciones, proxies, servicio de metadatos de fragmentos y miles de fragmentos",
            "Diagrama de la infraestructura de bases de datos de Stripe: las aplicaciones acceden a través de proxies escritos en Go que aplican control de admisión y de acceso; un servicio de metadatos asigna fragmentos de datos a las bases; cada base física es un conjunto de réplicas con nodo primario y secundarios; los cambios van por captura de datos a Kafka y de ahí a un almacén de objetos.")
    _head(f, "DocDB: aplicaciones, proxies, metadatos de fragmentos y miles de fragmentos")
    f.box(20, 60, 180, 80, "Aplicaciones de producto (usan una base lógica)", "teal", 13, bold=True)
    f.box(240, 60, 190, 80, "Proxies de base de datos (en Go): analizan, enrutan, combinan", "navy", 13, bold=True)
    f.box(470, 60, 200, 80, "Servicio de metadatos: asigna cada fragmento de datos a un fragmento de base", "gold", 13)
    f.box(710, 60, 210, 80, "Plano de control: crea bases lógicas y colecciones", "plain", 13)
    f.arrow([(200, 100), (240, 100)])
    f.arrow([(430, 100), (470, 100)])
    f.group(20, 170, 640, 130, "Más de 2.000 fragmentos (réplicas: un primario y varios secundarios)", "grey")
    for i in range(4):
        f.box(40 + i * 150, 205, 130, 70, f"Fragmento {i + 1}\n(base física)", "plain", 13)
    f.arrow([(335, 140), (335, 170)])
    f.box(690, 170, 230, 130, "CDC: el registro de operaciones de cada fragmento va a Kafka y se archiva en un almacén de objetos", "coral", 13)
    f.arrow([(660, 235), (690, 235)])
    f.box(20, 315, 440, 80, "Requisitos que no cubría una oferta existente: disponibilidad y durabilidad máximas, funciones mínimas expuestas, fragmentación horizontal, multiinquilino con cuotas y autorización fuerte.", "plain", 13)
    f.box(480, 315, 440, 80, "Elección de base: MongoDB en 2011 por productividad del desarrollador frente a bases relacionales; no existía Atlas, así que se construyó una flota propia en la nube.", "teal", 13)
    y = _notebox(f, 410, "Lectura: la consulta entra por un proxy que decide a qué fragmentos ir gracias al servicio de metadatos y devuelve el resultado combinado; debajo, los fragmentos, y a la derecha, el flujo de cambios. Dónde deja de valer: la descripción es de 2024; no se publica la topología de regiones ni cómo se despliega por zonas de disponibilidad.")
    _footer(f, y + 6, "Fuente: Morzaria y Narkhede, «How Stripe's document databases supported 99.999% uptime with zero-downtime data migrations», 6 de junio de 2024 (F8).")
    return f


# ---------------------------------------------------------------- escala de DocDB
def docdb_escala() -> Fig:
    return grouped_bars(
        "La escala de DocDB en 2024: cuatro magnitudes publicadas (escala logarítmica)",
        "Barras horizontales en escala logarítmica con cuatro cantidades que Stripe publica de DocDB: más de 5 millones de consultas por segundo, más de 10.000 formas de consulta distintas, más de 5.000 colecciones y más de 2.000 fragmentos.",
        ["Consultas por segundo", "Formas de consulta distintas", "Colecciones", "Fragmentos de base de datos"],
        [("Cantidad (más de)", [5_000_000, 10_000, 5_000, 2_000], "navy")],
        unit="Cantidad (escala logarítmica)", horizontal=True, log=True, label_w=250, plot_h=210,
        value_fmt=lambda v: (fmt_es(v / 1e6, 0) + " M") if v >= 1e6 else (fmt_es(v, 0)),
        note="Lectura: las unidades no son comparables entre sí; la escala logarítmica solo permite ver el orden de magnitud de cada una. Los datos son de más de 5.000 colecciones sobre petabytes de datos financieros. Dónde deja de valer: son cotas inferiores («más de») de un momento de 2024 y no dicen cuántos datos hay por fragmento; en 2023 se redujo el número de fragmentos en cerca de tres cuartas partes al agrupar bases infrautilizadas con 1,5 petabytes.",
        note_kind="gold", foot="Fuente: Morzaria y Narkhede, Stripe Blog, 6 de junio de 2024 (F8).")


# ---------------------------------------------------------------- traspaso de tráfico
def traspaso() -> Fig:
    f = Fig(940, 0, "El traspaso de tráfico de un fragmento a otro en menos de dos segundos: compuerta por versión",
            "Secuencia del traspaso de tráfico de la plataforma de movimiento de datos de Stripe: el coordinador sube el número de versión del fragmento origen, que rechaza lecturas y escrituras; espera a que el servicio de replicación vuelque lo pendiente; actualiza la ruta y la versión en el servicio de metadatos; los proxies recogen la ruta nueva y las peticiones fallidas tienen éxito al reintentar; el protocolo dura menos de dos segundos.")
    _head(f, "El traspaso de tráfico: compuerta por versión en menos de dos segundos")
    end = _seq(f, ["Coordinador", "Fragmento origen", "Servicio de\nreplicación", "Metadatos de\nfragmentos", "Proxies"], [
        (0, 1, "1. sube el número de versión: rechaza todo"),
        (4, 1, "2. peticiones rechazadas (se reintentan)", True),
        (0, 2, "3. espera a replicar lo pendiente"),
        (2, 0, "4. sin pendientes", True),
        (0, 3, "5. nueva ruta y nueva versión"),
        (4, 3, "6. consultan la ruta nueva; desde aquí envían al fragmento destino"),
    ], 52, step_h=44, box_w=130)
    y = _notebox(f, end + 10, "Lectura: el origen deja de aceptar tráfico en el paso 1; mientras tanto, el servicio de replicación termina de copiar; luego la ruta cambia y los proxies redirigen. Cada petición lleva un número de versión y el fragmento exige que sea más reciente que el que conoce. Dónde deja de valer: el objetivo de la fase clave es durar menos que una conmutación planificada del primario (unos segundos, dentro del presupuesto de reintentos de las aplicaciones); la duración «menos de dos segundos» es la que da el artículo y no una garantía.")
    _footer(f, y + 6, "Fuente: Morzaria y Narkhede (F8), paso 5 de la plataforma de movimiento de datos. Secuencia propia a partir del texto.")
    return f


# ---------------------------------------------------------------- plataforma de movimiento de datos
def movimiento_datos() -> Fig:
    f = Fig(940, 0, "La plataforma de movimiento de datos: seis pasos para mover un fragmento sin parar el servicio",
            "Flujo de los seis pasos de la plataforma de movimiento de datos de Stripe: registrar la intención de migración, importar en bloque los datos desde una instantánea, replicar de forma asíncrona las escrituras desde el instante de la instantánea, comprobar la corrección, conmutar el tráfico y cancelar el registro de la migración; la replicación es bidireccional para poder volver atrás.")
    _head(f, "Plataforma de movimiento de datos: seis pasos sin parar el servicio")
    steps = [("1. Registrar la\nmigración y crear\níndices", "teal"), ("2. Importar en bloque\nuna instantánea\nen T", "teal"), ("3. Replicar escrituras\ndesde T (CDC,\nbidireccional)", "gold"), ("4. Comprobar\ncorrección con\ninstantáneas", "gold"), ("5. Conmutar el\ntráfico (compuerta\npor versión)", "navy"), ("6. Cerrar el registro\ny borrar del\norigen", "plain")]
    x = 20
    for t, k in steps:
        f.box(x, 60, 140, 100, t, k, 13, bold=(k == "navy"))
        x += 150
    for i in range(5):
        f.arrow([(20 + i * 150 + 140, 110), (20 + (i + 1) * 150, 110)])
    f.box(20, 185, 440, 100, "Truco de rendimiento: el volcado en bloque era lento; ordenar los datos por los atributos de índice más comunes (la base usa un árbol B) y escribirlos en orden mejoró la proximidad de las escrituras y subió el rendimiento diez veces.", "teal", 13)
    f.box(480, 185, 440, 100, "Por qué la replicación es bidireccional y marcada: permite volver al origen si surge un problema tras la conmutación; las escrituras replicadas se etiquetan para evitar ciclos.", "gold", 13)
    f.box(20, 300, 440, 80, "Usos: dividir fragmentos al subir el tráfico, agrupar miles de bases infrautilizadas (1,5 petabytes en 2023, menos fragmentos en cerca de tres cuartas partes) y actualizar la versión de la base de una vez.", "plain", 13)
    f.box(480, 300, 440, 80, "Requisitos que dirigen el diseño: consistencia y completitud, disponibilidad, granularidad, y ningún impacto en el fragmento de origen.", "plain", 13)
    y = _notebox(f, 396, "Lectura: de izquierda a derecha los pasos; los recuadros de abajo explican el truco de rendimiento, la reversibilidad, los usos y los requisitos. Dónde deja de valer: es una infraestructura construida para una flota de miles de fragmentos; no es una receta para una base de datos pequeña.")
    _footer(f, y + 6, "Fuente: Morzaria y Narkhede (F8). Resumen propio.")
    return f


# ---------------------------------------------------------------- estados de PaymentIntent
def estados_pago() -> Fig:
    f = Fig(940, 0, "Los estados de una intención de pago: de la creación al cobro, con la autenticación de por medio",
            "Diagrama de estados de una PaymentIntent de Stripe: requiere método de pago, requiere confirmación (que la mayoría de las integraciones omite), requiere acción (por ejemplo 3D Secure), procesando (métodos asíncronos como débitos bancarios, que pueden tardar días) o requiere captura, y finalmente realizado; si el intento falla, vuelve al estado de requerir método de pago para reintentar.")
    _head(f, "Los estados de una intención de pago")
    f.box(20, 70, 190, 70, "requires_payment_method\n(creada, sin método)", "plain", 13)
    f.box(250, 70, 190, 70, "requires_confirmation\n(lista para confirmar)", "grey", 13, dashed=True)
    f.box(480, 70, 190, 70, "requires_action\n(p. ej. 3D Secure)", "gold", 13)
    f.box(710, 70, 210, 70, "processing\n(métodos asíncronos)", "gold", 13)
    f.box(710, 190, 210, 70, "succeeded\n(fondos en la cuenta)", "teal", 13, bold=True)
    f.box(480, 190, 190, 70, "requires_capture\n(autorizar y capturar)", "plain", 13)
    f.arrow([(210, 105), (250, 105)])
    f.arrow([(440, 105), (480, 105)])
    f.arrow([(670, 105), (710, 105)])
    f.arrow([(815, 140), (815, 190)])
    f.arrow([(670, 225), (710, 225)])
    f.arrow([(580, 140), (580, 190)])
    f.arrow([(815, 70), (815, 54), (115, 54), (115, 70)], "si el intento falla, vuelve a reintentar", dashed=True, color="#c0432f", label_at=(470, 48))
    f.box(20, 320, 440, 80, "Crear la intención en cuanto se conoce el importe, para que Stripe registre todos los intentos de pago; típicamente una intención por carrito o sesión.", "plain", 13)
    f.box(480, 320, 440, 80, "Promesa de la API: autenticación automática, sin doble cobro y sin problemas de claves de idempotencia, además de compatibilidad con la autenticación fuerte del cliente.", "teal", 13)
    y = _notebox(f, 416, "Lectura: las cajas son estados; las flechas, transiciones; la discontinua roja es lo que ocurre ante un rechazo. El estado «requires_confirmation» se dibuja discontinuo porque la mayoría de las integraciones lo omite. Dónde deja de valer: no incluye cancelaciones ni disputas posteriores, ni los métodos con redirección; los nombres de estado cambiaron en 2019 (antes, «requires_source»).")
    _footer(f, y + 6, "Fuentes: Stripe Docs, «The Payment Intents API» (F12) y «How PaymentIntents and SetupIntents work» (F12-bis). Dibujo propio.")
    return f


# ---------------------------------------------------------------- webhooks
def webhooks() -> Fig:
    f = Fig(940, 0, "Un webhook bien recibido: verificar, responder rápido, deduplicar y no suponer el orden",
            "Secuencia de la entrega de un evento por webhook: Stripe envía el evento firmado; el receptor verifica la firma con el cuerpo en crudo y una tolerancia de tiempo, devuelve 2xx antes de la lógica compleja, guarda el identificador del evento para ignorar duplicados y procesa después; si no responde, Stripe reintenta hasta tres días con espera exponencial en modo real.")
    _head(f, "Un webhook bien recibido: verificar, responder rápido, deduplicar")
    end = _seq(f, ["Stripe", "Receptor del\ncomercio", "Almacén de\nidentificadores", "Lógica de\nnegocio"], [
        (0, 1, "1. POST del evento con firma"),
        (1, 1, "2. verifica firma (cuerpo crudo, tolerancia de 5 min)"),
        (1, 2, "3. ¿ya vi este id de evento?"),
        (1, 0, "4. 2xx rápido, antes de la lógica", True),
        (1, 3, "5. procesa después, en segundo plano"),
        (0, 1, "6. si no hubo 2xx: reintento con espera exponencial"),
        (1, 2, "7. id repetido: ignorar el duplicado"),
    ], 52, step_h=44)
    y = _notebox(f, end + 10, "Lectura: la flecha continua es una petición y la discontinua una respuesta. Stripe no garantiza el orden de entrega (por ejemplo, la factura pagada puede llegar antes que la factura creada), así que el receptor no debe depender de él; para eso puede recuperar los objetos por la API. No se debe usar la marca de tiempo de creación para decidir orden o si ya se procesó, sino el identificador del evento. Dónde deja de valer: en el entorno de pruebas los reintentos son tres, en unas horas; la secuencia es una lectura de la documentación, no un diagrama de Stripe.")
    _footer(f, y + 6, "Fuente: Stripe Docs, «Webhooks» (F11). Secuencia propia.")
    return f


# ---------------------------------------------------------------- seguridad: datos de tarjeta
def seguridad() -> Fig:
    f = Fig(940, 0, "El camino de un número de tarjeta: del componente tokenizado a la bóveda de datos de tarjeta",
            "Diagrama del manejo de datos de tarjeta en Stripe: el cliente teclea el número en un componente de interfaz que lo envía a Stripe sin pasar por el servidor del comercio; los números se tokenizan en una bóveda aislada, cifrados con AES-256 con claves en otras máquinas; ningún servidor interno ve el número en claro y solo se envía a proveedores de una lista estática; todo el tráfico entre servidores usa TLS mutuo.")
    _head(f, "El camino de un número de tarjeta: del componente a la bóveda")
    f.box(20, 60, 190, 80, "Cliente final teclea la tarjeta en un componente (Elements)", "teal", 13, bold=True)
    f.box(250, 60, 200, 80, "Stripe recibe el número directo; el servidor del comercio solo ve un token", "navy", 13, bold=True)
    f.box(490, 60, 200, 80, "Bóveda de datos de tarjeta (aislada; acceso a pocos ingenieros, revisado cada trimestre)", "coral", 13)
    f.box(730, 60, 190, 80, "Proveedor de servicios en una lista de permitidos", "gold", 13)
    f.arrow([(210, 100), (250, 100)])
    f.arrow([(450, 100), (490, 100)])
    f.arrow([(690, 100), (730, 100)])
    f.box(20, 165, 440, 90, "Cifrado en reposo con AES-256; las claves de descifrado se guardan en máquinas distintas; los números se tokenizan internamente para aislarlos del resto de la infraestructura.", "plain", 13)
    f.box(480, 165, 440, 90, "Ningún servidor o proceso interno obtiene el número en claro; pueden pedir que se envíe a un proveedor de la lista estática.", "plain", 13)
    f.box(20, 270, 440, 80, "Transporte: HTTPS obligatorio, HSTS, TLS 1.2 como mínimo y TLS mutuo en toda la comunicación entre servidores.", "plain", 13)
    f.box(480, 270, 440, 80, "Cumplimiento: certificado PCI de proveedor de servicios de nivel 1; informes SOC 1, 2 y 3; ayuda a completar el formulario de autoevaluación según la integración.", "teal", 13)
    y = _notebox(f, 366, "Lectura: el número viaja de izquierda a derecha y en ningún punto toca el servidor del comercio ni el de Stripe en claro; lo que cruza el sistema es un token. Dónde deja de valer: son afirmaciones de la documentación de seguridad de Stripe; no se publican auditorías ni incidentes, y la bóveda aislada no es visible desde fuera. Un comercio que no usa componentes de Stripe tiene un alcance de PCI mayor.")
    _footer(f, y + 6, "Fuentes: Stripe Docs, «Security at Stripe» (F13) y «Elements» (F14). Dibujo propio.")
    return f


# ---------------------------------------------------------------- Connect
def connect() -> Fig:
    f = Fig(940, 0, "Connect: una plataforma cobra a compradores y paga a sus vendedores, y Stripe mantiene las cuentas",
            "Diagrama del flujo de dinero de una plataforma o marketplace con Stripe Connect: el comprador paga, la plataforma cobra con Stripe, Stripe retiene la comisión de la plataforma y paga automáticamente la parte que corresponde a cada vendedor mediante cuentas conectadas, cada una con capacidades y requisitos de verificación.")
    _head(f, "Connect: la plataforma cobra y Stripe paga a cada vendedor")
    f.box(20, 70, 170, 70, "Comprador", "teal", 14, bold=True)
    f.box(230, 70, 200, 70, "Plataforma (tu marketplace)", "navy", 14, bold=True)
    f.box(470, 70, 180, 70, "Stripe\n(cobra y reparte)", "gold", 14, bold=True)
    f.box(690, 40, 230, 56, "Cuenta conectada A (vendedor)", "plain", 13)
    f.box(690, 110, 230, 56, "Cuenta conectada B (vendedor)", "plain", 13)
    f.arrow([(190, 105), (230, 105)], "paga", label_at=(210, 92))
    f.arrow([(430, 105), (470, 105)])
    f.arrow([(650, 90), (690, 68)])
    f.arrow([(650, 120), (690, 138)])
    f.box(20, 190, 440, 90, "Cuentas conectadas: la API de cuentas v2 crea una identidad unificada por cuenta con una o varias configuraciones (comerciante, cliente) y capacidades que se activan según la verificación.", "plain", 13)
    f.box(480, 190, 440, 90, "Qué ofrece Connect: aceptar pagos, pagar a las cuentas, y productos financieros integrados (tesorería, tarjetas, financiación) para plataformas de software.", "plain", 13)
    f.box(20, 295, 440, 80, "Costo y límite: la plataforma asume la relación con el vendedor (soporte, disputas); Stripe no deja que las tarifas de disputa se trasladen a las cuentas conectadas.", "coral", 13)
    f.box(480, 295, 440, 80, "Límites técnicos publicados: 30 cuentas conectadas creadas por segundo en modo real (5 en el entorno de pruebas).", "gold", 13)
    y = _notebox(f, 390, "Lectura: de izquierda a derecha, el dinero del comprador pasa por la plataforma y Stripe lo reparte entre las cuentas conectadas. Dónde deja de valer: es un esquema de la documentación; no se publica cómo se liquida ni los plazos, y las cuentas v1 y v2 coexisten. No se sabe cuántas plataformas usan Connect.")
    _footer(f, y + 6, "Fuentes: Stripe Docs, «Connect» (F15) y «Rate limits» (F17); precios (F9). Dibujo propio.")
    return f


# ---------------------------------------------------------------- precios de otros productos
def precios() -> Fig:
    return grouped_bars(
        "Las tarifas porcentuales de la lista de precios de Stripe (porcentaje del importe)",
        "Barras horizontales con las tarifas porcentuales de la página de precios: tarjeta nacional 2,9 por ciento más 30 centavos, recargo de 0,5 por ciento por tarjeta tecleada a mano, 1,5 por ciento por tarjeta internacional, 1 por ciento por conversión de moneda, Billing 0,7 por ciento del volumen, débito ACH 0,8 por ciento con tope de 5 dólares, Tax 0,5 por ciento por transacción, pagos con stablecoins 1,5 por ciento y Instant Payouts 1,5 por ciento.",
        ["Tarjeta nacional (más 30 centavos)", "Tarjeta internacional (recargo)", "Pagos con stablecoins", "Instant Payouts (mín. 50 centavos)", "Conversión de moneda (recargo)", "ACH débito (tope 5 dólares)", "Billing (volumen)", "Tarjeta tecleada a mano (recargo)", "Tax, por transacción"],
        [("Porcentaje", [2.9, 1.5, 1.5, 1.5, 1.0, 0.8, 0.7, 0.5, 0.5], "teal")],
        unit="Porcentaje del importe", horizontal=True, decimals=1, label_w=270, plot_h=330,
        note="Lectura: la tarjeta nacional es la tarifa más alta de la lista y los demás conceptos son recargos o servicios aparte, que se suman. Hay tarifas fijas que no caben en la escala (30 centavos por transacción, 15 dólares por disputa recibida). Dónde deja de valer: son tarifas estándar de una lista consultada en 2026; los precios por país y los acuerdos personalizados (IC+) son otros; y un recargo se suma a la tarifa base, no la sustituye.",
        note_kind="gold", foot="Fuente: stripe.com/pricing (F9), consulta del 2026-11-16.")


# ---------------------------------------------------------------- línea de tiempo ampliada
def linea_tiempo2() -> Fig:
    return timeline(
        "Stripe: de la API a la infraestructura económica, con el volumen de pagos",
        "Línea de tiempo de 2010 a 2026 con dos carriles: plataforma (API y MongoDB desde 2011, artículos de ingeniería de 2017, DocDB a gran escala hasta 2024) y volumen anual de pagos de 1,0, 1,4 y 1,9 billones de dólares en 2023, 2024 y 2025.",
        [("Plataforma", [(2011, 2017, "API y MongoDB", "teal"), (2017, 2023, "Productos y escala", "gold"), (2023, 2026, "DocDB", "navy")]),
         ("Volumen (billones)", [(2023, 2024, "1,0", "teal"), (2024, 2025, "1,4", "gold"), (2025, 2026, "1,9", "navy")])],
        unit="Año", events=[(2011, "Lanzamiento"), (2017, "Cuatro artículos"), (2019.1, "Estados de pago"), (2024.4, "DocDB")], t_max=2026, ticks=[2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026], width=940, lane_h=54, label_w=170,
        note="Documentado: MongoDB elegido al lanzar en 2011 (F8); cuatro artículos de 2017 (F4 a F7); cambio de nombres de estado el 11 de febrero de 2019 (F12-bis); volúmenes de 2023, 2024 y 2025 (F8, F3, F2), en billones (10^12) de dólares. El lanzamiento público de 2011 es dato secundario (F16). Las eras son síntesis del autor. Dónde deja de valer: no hay series publicadas del volumen antes de 2023 en las fuentes de este caso.",
        note_kind="gold", foot="Fuentes: F2, F3, F4 a F8, F12-bis y F16; síntesis propia de las eras.")


FIGURES = {
    "stripe-contexto-intermediario.svg": contexto,
    "stripe-volumen-de-pagos.svg": volumen,
    "stripe-tarifa-efectiva.svg": tarifa_efectiva,
    "stripe-precios-porcentuales.svg": precios,
    "stripe-componentes-documentados.svg": componentes,
    "stripe-flujo-de-un-cobro.svg": flujo_cobro,
    "stripe-estados-de-la-intencion-de-pago.svg": estados_pago,
    "stripe-idempotencia-secuencia.svg": idem_secuencia,
    "stripe-idempotencia-decision.svg": idem_decision,
    "stripe-limitadores.svg": limitadores,
    "stripe-limites-de-tasa.svg": limites_cifras,
    "stripe-lanzar-un-limitador.svg": lanzar_limitador,
    "stripe-versionado-por-modulos.svg": versionado,
    "stripe-migracion-en-cuatro-pasos.svg": migracion_cuatro_pasos,
    "stripe-docdb-arquitectura.svg": docdb_arquitectura,
    "stripe-docdb-escala.svg": docdb_escala,
    "stripe-movimiento-de-datos.svg": movimiento_datos,
    "stripe-traspaso-de-trafico.svg": traspaso,
    "stripe-webhooks-recepcion.svg": webhooks,
    "stripe-seguridad-de-tarjeta.svg": seguridad,
    "stripe-connect.svg": connect,
    "stripe-linea-de-tiempo.svg": linea_tiempo2,
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
