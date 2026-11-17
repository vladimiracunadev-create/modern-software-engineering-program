"""Figures for the Netflix success case (casos/exito/netflix.md).

Every number comes from a source cited in the case page: the Netflix Q4 2024 earnings
8-K, the 2016 and 2007 annual reports, Netflix's own timeline page and its engineering
blog. Architecture diagrams are labelled as documented or inferred.
"""
from __future__ import annotations

import re

from figure_kit import (Fig, _wrap, fmt_es, grouped_bars, line_chart, stacked_bars, timeline)

from case_diagrams import B, G, finish, lane_steps, legend, sequence
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


SEC = "Fuente: Netflix, Form 10-K de 2025, de 2016 y de 2007 (SEC). Consulta: 16 de noviembre de 2026."


def actores() -> Fig:
    f = _canvas("Quién da qué a quién: los actores del ecosistema de Netflix",
                "Diagrama de incentivos: el miembro paga una suscripción; el anunciante paga por audiencia en el plan con anuncios; los estudios y creadores reciben licencias o contratos de producción; el proveedor de internet recibe servidores gratuitos y a cambio ahorra tránsito; los fabricantes de dispositivos instalan la aplicación; Netflix en el centro coordina.",
                940, 0)
    B(f, 340, 160, 260, 96, "Netflix: cobra, programa catálogo, opera el servicio y la red de entrega", "navy", 13, bold=True)
    B(f, 10, 56, 250, 70, "Miembro: paga una cuota mensual y obtiene catálogo, perfiles y descargas", "teal")
    B(f, 345, 56, 250, 70, "Anunciante: compra audiencia en el plan con anuncios (desde 2022)", "gold")
    B(f, 680, 56, 250, 70, "Estudio y talento: cede licencias o produce por encargo y cobra por ello", "plain")
    B(f, 10, 300, 250, 70, "Proveedor de internet: aloja servidores sin cargo y ahorra tránsito", "gold")
    B(f, 345, 300, 250, 70, "Fabricante de dispositivos: instala la aplicación de origen", "plain")
    B(f, 680, 300, 250, 70, "Reguladores y socios de pago: fijan reglas de cobro, datos y contenido", "grey", dashed=True)
    f.arrow([(200, 126), (340, 190)], "cuota", label_at=(240, 150))
    f.arrow([(470, 126), (470, 160)], "audiencia", label_at=(520, 148))
    f.arrow([(670, 126), (600, 190)], "licencias y pagos", label_at=(700, 160))
    f.arrow([(340, 236), (230, 300)], "servidores", label_at=(262, 262))
    f.arrow([(470, 256), (470, 300)])
    f.arrow([(600, 236), (690, 300)], dashed=True)
    return finish(f, 390, "Documentado: la cuota, el plan con anuncios, los servidores gratuitos para ISP calificados y la colaboración con fabricantes desde 2008. No se sabe: los términos económicos con estudios, anunciantes y socios de pago; la flecha punteada a reguladores y pagos solo indica que existen obligaciones, no un dato de contrato.", DOC)


def viajes() -> Fig:
    f = _canvas("Cuatro recorridos completos: de la primera interacción al caso límite",
                "Cuatro filas de pasos encadenados: miembro nuevo, miembro del plan con anuncios, hogar que comparte cuenta y miembro que descarga para ver sin conexión; cada fila termina en su caso límite.",
                940, 0)
    y = 54.0
    y = lane_steps(f, y, "Miembro nuevo", [("Descubre la app o el botón del mando", "plain"), ("Elige plan y paga", "plain"), ("Crea perfiles", "plain"), ("Recibe recomendaciones", "teal"), ("Límite: cancela y vuelve meses después", "coral")])
    y = lane_steps(f, y, "Plan con anuncios", [("Elige el plan más barato", "plain"), ("Ve anuncios en la reproducción", "gold"), ("Catálogo con licencias distintas", "plain!"), ("Límite: título no disponible en este plan", "coral!")])
    y = lane_steps(f, y, "Hogar compartido", [("Una cuenta, varios hogares", "plain"), ("Netflix detecta uso fuera del hogar", "plain!"), ("Miembro extra de pago o perfil transferido", "gold"), ("Límite: viaje con la TV de otro hogar", "coral!")])
    y = lane_steps(f, y, "Sin conexión", [("Descarga un título (desde 2016)", "plain"), ("Se guarda en el dispositivo", "plain"), ("Reproduce sin red", "teal"), ("Límite: la licencia de la descarga caduca", "coral!")])
    legend(f, y + 14, "Trazo punteado: paso inferido o con mecanismo no publicado. Cajas coral: el caso límite de cada recorrido.")
    return finish(f, y + 28, "Cada fila es un tipo de usuario con su propio incentivo. Los pasos continuos salen de la cronología oficial y de la carta de 2024; los punteados son el comportamiento visible al usuario, no el mecanismo interno, que no es público.", DOC)


def contenedores() -> Fig:
    f = _canvas("Nivel 2, contenedores: de la puerta de entrada a los datos y a la red de vídeo",
                "Diagrama de contenedores: dispositivos llegan a una puerta de entrada Zuul; detrás hay una capa de API y servicios con Hystrix y descubrimiento Eureka, cachés EVCache, bases de datos replicadas, telemetría y el pipeline de codificación; el vídeo sale de las Open Connect Appliances.",
                940, 0)
    B(f, 10, 80, 170, 60, "Dispositivos: TV, móvil, web, consola", "plain")
    G(f, 200, 48, 540, 262, "Nube de AWS (documentado: la mayor parte del cómputo)", "navy")
    B(f, 218, 84, 150, 64, "Zuul: puerta de entrada con filtros", "teal")
    B(f, 386, 84, 170, 64, "API y servicios de negocio", "plain")
    B(f, 574, 84, 150, 64, "Eureka: registro de instancias", "plain")
    B(f, 218, 172, 150, 64, "Hystrix: interruptor y alternativa", "coral")
    B(f, 386, 172, 170, 64, "EVCache: memcached en RAM", "gold")
    B(f, 574, 172, 150, 64, "Cassandra y otras bases", "plain", dashed=True)
    B(f, 218, 246, 506, 52, "Telemetría, recomendación y codificación de vídeo (inferido por función)", "plain", dashed=True)
    G(f, 760, 48, 170, 262, "Red de entrega", "gold")
    B(f, 772, 84, 146, 100, "Open Connect: appliances dentro de ISP y en puntos de intercambio", "gold")
    B(f, 772, 196, 146, 88, "Vídeo en segmentos", "plain", dashed=True)
    f.arrow([(180, 110), (218, 116)])
    f.arrow([(368, 116), (386, 116)])
    f.arrow([(556, 116), (574, 116)], dashed=True)
    f.arrow([(470, 148), (470, 172)])
    f.arrow([(556, 204), (574, 204)], dashed=True)
    f.arrow([(95, 140), (95, 330), (845, 330), (845, 310)], "vídeo", dashed=True, label_at=(470, 324))
    f.arrow([(845, 180), (845, 196)])
    return finish(f, 350, "Documentado: Zuul como puerta de entrada de todas las peticiones (wiki de Zuul), Hystrix con interruptor y respuesta alternativa (wiki de Hystrix), Eureka para localizar servicios de la capa intermedia (wiki de Eureka), EVCache como caché volátil, que la mayor parte del cómputo corre sobre AWS y que Open Connect es una red propia. Inferido: dónde están las bases hoy y los servicios de negocio y de telemetría; el número de servicios es desconocido.", DOC)


def secuencia() -> Fig:
    return sequence(
        "Nivel 4, secuencia: «Reproducir» paso a paso entre cliente, nube y Open Connect",
        "Diagrama de secuencia con cinco participantes: cliente, puerta de entrada, servicios de control, Open Connect y telemetría. El cliente pide reproducir, el control valida y devuelve una lista de servidores, el cliente descarga segmentos y envía eventos.",
        ["Cliente", "Zuul (entrada)", "Servicios de control", "Open Connect", "Telemetría"],
        [(0, 1, "Pide reproducir un título", ""), (1, 2, "Filtra y enruta", ""),
         (2, 2, "Plan, perfil y derechos (inferido)", "dashed"), (2, 0, "Servidores y manifiesto (inferido)", "dashed"),
         (0, 3, "Pide segmentos de vídeo", ""), (3, 0, "Segmentos desde el servidor cercano", ""),
         (0, 4, "Eventos de reproducción (inferido)", "dashed")],
        "Documentado: la puerta de entrada recibe todas las peticiones y el vídeo sale de Open Connect, no de la nube de control. Inferido por el curso: la validación de derechos, la lista de servidores, el manifiesto y los eventos de telemetría; Netflix no publica el protocolo actual. Flechas punteadas: pasos inferidos.",
        DOC, kinds=["plain", "teal", "navy", "gold", "grey"])


def hystrix() -> Fig:
    f = _canvas("Nivel 3, componente: qué hace Hystrix con cada llamada a una dependencia",
                "Diagrama de flujo de la biblioteca Hystrix: construir el comando, mirar la caché, comprobar si el circuito está abierto, comprobar si la reserva de hilos está llena, ejecutar con tiempo límite, registrar el resultado y, ante cualquier fallo, devolver la respuesta alternativa.",
                940, 0)
    xs = [10, 168, 326, 484, 642, 800]
    heads = [("1. Construir comando", "plain"), ("2. ¿Hay caché?", "gold"), ("3. ¿Circuito abierto?", "coral"), ("4. ¿Reserva llena?", "coral"), ("5. Ejecutar con tiempo límite", "teal"), ("6. Registrar salud", "navy")]
    for x, (t, k) in zip(xs, heads):
        B(f, x, 62, 130, 76, t, k, 13, bold=(k == "navy"))
    for a, b in zip(xs, xs[1:]):
        f.arrow([(a + 130, 100), (b, 100)])
    B(f, 326, 190, 604, 76, "Alternativa (fallback): si el circuito está abierto, la reserva llena, hay un error o vence el tiempo, se devuelve una respuesta sin red (por ejemplo, de memoria) en vez de un error", "gold")
    for x in (391, 549, 707):
        f.arrow([(x, 138), (x, 190)], dashed=True, color="#c0432f")
    B(f, 10, 190, 300, 76, "Circuito abierto: tras fallos repetidos se deja de llamar; pasado un tiempo pasa una petición de prueba (semiabierto)", "plain")
    f.arrow([(865, 138), (865, 160), (155, 160), (155, 190)], dashed=True)
    return finish(f, 288, "Documentado en la wiki oficial de Hystrix: el orden de los pasos, el fallback ante circuito abierto, reserva llena, error o tiempo agotado, y el estado semiabierto que deja pasar una petición tras la ventana de espera. Los umbrales concretos de Netflix en producción no son públicos, y esta biblioteca no prueba qué usa hoy Netflix.", DOC)


def despliegue() -> Fig:
    f = _canvas("Nivel 5, despliegue: tres capas geográficas que no se mezclan",
                "Diagrama de despliegue: el DNS dirige al miembro hacia una de varias regiones de nube donde corre el plano de control con datos replicados entre regiones; el vídeo sale de appliances Open Connect dentro de más de mil proveedores de internet y puntos de intercambio, rellenados cada noche desde centros de datos de Netflix.",
                940, 0)
    G(f, 10, 50, 300, 130, "Miembro y su red", "grey")
    B(f, 26, 88, 126, 70, "Aplicación del miembro", "plain")
    B(f, 166, 88, 130, 70, "DNS: decide la región de control", "teal")
    G(f, 340, 50, 590, 130, "Plano de control: varias regiones de AWS (documentado en 2013)", "navy")
    B(f, 356, 88, 170, 70, "Región A: Zuul, servicios, EVCache", "plain")
    B(f, 540, 88, 170, 70, "Región B: la misma pila", "plain")
    B(f, 724, 88, 190, 70, "Datos replicados entre regiones (Cassandra y EVCache)", "gold")
    f.arrow([(296, 123), (356, 123)])
    f.arrow([(526, 123), (540, 123)], dashed=True)
    f.arrow([(710, 123), (724, 123)])
    G(f, 10, 210, 560, 120, "Plano de datos: Open Connect dentro de la red del ISP", "gold")
    B(f, 26, 248, 160, 66, "Appliance dentro del ISP, sin cargo si califica", "gold")
    B(f, 200, 248, 170, 66, "Punto de intercambio con interconexión sin liquidación", "gold")
    B(f, 384, 248, 170, 66, "Más de mil ISP con appliances (página oficial)", "plain")
    G(f, 600, 210, 330, 120, "Abastecimiento", "grey")
    B(f, 616, 248, 298, 66, "Centros de datos de Netflix (más de 60) rellenan los appliances cada noche", "plain")
    f.arrow([(616, 280), (554, 280)], dashed=True)
    f.arrow([(89, 158), (89, 210)], dashed=True)
    return finish(f, 350, "Documentado en openconnect.netflix.com: appliances embebidos sin cargo para ISP calificados, interconexión en puntos de intercambio, relleno nocturno, más de mil ISP y más de 60 centros de datos; y en el artículo de 2013, la pila en varias regiones con datos replicados. No se sabe cuántas regiones activas hay hoy ni el reparto del tráfico entre appliances y puntos de intercambio.", DOC)


def evolucion() -> Fig:
    f = _canvas("Cómo evolucionó la arquitectura: tres etapas, antes y después",
                "Tres columnas que comparan etapas: 1998 a 2007 con centro de datos propio y base relacional; 2008 a 2016 con migración a la nube, servicios con interruptor y Open Connect desde 2012; 2016 en adelante con la mayor parte del cómputo en AWS, directo y publicidad.",
                940, 0)
    cols = [
        ("1998-2007: centro de datos", "grey", ["Base relacional vertical en un centro de datos propio", "El producto es el DVD; el correo es el transporte", "Un fallo de base de datos paró los envíos tres días en 2008"]),
        ("2008-2016: migración", "navy", ["Servicios que pueden fallar sin tumbar el sitio (Hystrix, 2011)", "Copias del estado en varias regiones (2013)", "Open Connect desde 2012; fin de la migración en enero de 2016"]),
        ("2016 en adelante: nube madura", "teal", ["La mayor parte del cómputo sigue en AWS y no se mueve fácil (10-K)", "Directo, juegos y publicidad añaden cargas nuevas", "Desde 2025 ya no se publica el número de miembros"]),
    ]
    x = 10.0
    for head, kind, items in cols:
        B(f, x, 56, 292, 44, head, kind, 14, bold=True)
        y = 112
        for it in items:
            B(f, x, y, 292, 70, it, "plain")
            y += 82
        x += 314
    f.arrow([(302, 78), (324, 78)])
    f.arrow([(616, 78), (638, 78)])
    return finish(f, 368, "Las tres etapas son una periodización del curso sobre hechos documentados (carta de 2016, artículos de 2011 y 2013, 10-K de 2025). Cada etapa mezcla decisiones técnicas y de negocio: el ritmo de cambio de la arquitectura siguió al del producto. No se sabe qué sistemas concretos de la tercera etapa se han reescrito.", DOC)


def datos() -> Fig:
    f = _canvas("Nivel 6, datos: qué vive dónde y cuánta inconsistencia tolera cada pieza",
                "Diagrama de modelo de datos y flujos: la caché EVCache guarda datos efímeros con caducidad y puede perderlos; las bases replicadas guardan el estado de cuenta y perfil con consistencia eventual; la facturación y los datos de clientes viajaron al final por un camino seguro y duradero; los eventos de uso alimentan recomendación.",
                940, 0)
    B(f, 10, 60, 290, 58, "Efímero y volátil: EVCache (TTL, puede evictarse)", "gold", 13, bold=True)
    B(f, 325, 60, 290, 58, "Replicado: cuenta y perfil (eventual, inferido)", "plain", 13, bold=True, dashed=True)
    B(f, 640, 60, 290, 58, "Duradero y seguro: facturación y datos de clientes", "navy", 13, bold=True)
    B(f, 10, 130, 290, 100, "Si se pierde: se vuelve a calcular o leer del origen. Tolera datos algo viejos y no exige consistencia fuerte (blog de 2016)", "plain")
    B(f, 325, 130, 290, 100, "Si divergen: se elige seguir sirviendo y reconciliar después. La política exacta por tipo de dato no se sabe", "plain", dashed=True)
    B(f, 640, 130, 290, 100, "Si falla: cobro o cuenta incorrectos; por eso fue lo último en migrar a la nube (carta de 2016)", "plain")
    f.arrow([(155, 118), (155, 130)])
    f.arrow([(470, 118), (470, 130)])
    f.arrow([(785, 118), (785, 130)])
    B(f, 10, 250, 920, 60, "Flujo: la reproducción genera eventos de uso, que alimentan recomendación y operación (inferido) y vuelven al catálogo que ve el miembro, siempre a través de una caché que prioriza velocidad", "grey", dashed=True)
    legend(f, 336)
    return finish(f, 348, "Cada columna ordena un tipo de dato por el coste de equivocarse, de menor a mayor. Documentado: la naturaleza efímera de EVCache y que la facturación migró al final y por un camino seguro y duradero. Inferido: dónde viven cuenta y perfil. No se sabe: el modelo de datos real, los esquemas y el volumen almacenado.", DOC)


def alternativas() -> Fig:
    f = _canvas("Alternativas descartadas: tres bifurcaciones y qué habrían costado (análisis propio)",
                "Tres filas de decisión con la opción elegida y la alternativa: reconstruir el centro de datos o migrar a la nube; comprar CDN comercial o construir Open Connect; seguir con licencias o producir contenido propio; cada alternativa lleva su coste probable.",
                940, 0)
    rows = [
        ("Plataforma", "Elegida: mover todo a AWS (2008-2016)", "teal", "Alternativa: ampliar el centro de datos con más servidores", "Habría conservado el punto único de fallo de 2008 y exigido comprar capacidad para el pico"),
        ("Entrega de vídeo", "Elegida: red propia Open Connect (2012)", "gold", "Alternativa: contratar CDN comerciales con pago por GB", "Coste variable alto al crecer el streaming y menos control; solo con datos internos se podría comparar"),
        ("Contenido", "Elegida: producir originales (2013)", "navy", "Alternativa: seguir licenciando catálogo ajeno", "Dependencia de estudios que endurecen licencias; ahorra caja inicial pero no crea un activo propio"),
    ]
    y = 56.0
    for name, a, ka, b, cost in rows:
        B(f, 10, y, 120, 92, name, "navy", 13, bold=True)
        B(f, 146, y, 250, 92, a, ka)
        B(f, 412, y, 250, 92, b, "grey", dashed=True)
        B(f, 678, y, 252, 92, cost, "coral", dashed=True)
        f.arrow([(396, y + 46), (412, y + 46)])
        f.arrow([(662, y + 46), (678, y + 46)], dashed=True)
        y += 108
    return finish(f, y + 8, "Es un análisis propio, no un hecho: Netflix no publica qué evaluó y descartó ni sus números internos. Lo documentado es la opción elegida y el motivo declarado de cada una (fallo de 2008, red propia, originales desde 2013). Los costes de la alternativa son hipótesis razonadas con la teoría de decisiones reversibles del curso.", INF, "coral")


def contenido() -> Fig:
    return stacked_bars(
        "Qué se amortiza cada año: contenido licenciado y producido (miles de millones de USD)",
        "Barras apiladas de la amortización de contenido de Netflix en 2023, 2024 y 2025: el contenido licenciado pasa de 7,1 a 7,7 y a 8,7 miles de millones, el producido de 7,1 a 7,6 y a 7,7; el total sube de 14,2 a 15,3 y a 16,4.",
        ["2023", "2024", "2025"],
        [("Licenciado", [7.145, 7.689, 8.714], "navy"), ("Producido", [7.052, 7.613, 7.709], "teal")],
        unit="miles de millones de USD", horizontal=True, decimals=1, label_w=70,
        note="La amortización de contenido es 42 por ciento de los ingresos en 2023, 39 en 2024 y 36 en 2025 (cálculo propio con los ingresos del 10-K). Las adiciones a activos de contenido fueron 12,6, 16,2 y 17,1 miles de millones: la caja sale antes que el gasto contable en el contenido propio.",
        note_kind="gold", foot=SEC)


def regiones() -> Fig:
    return stacked_bars(
        "De dónde vienen los ingresos: cuatro regiones (2023-2025, miles de millones de USD)",
        "Barras apiladas de ingresos de streaming por región en 2023, 2024 y 2025: Estados Unidos y Canadá 14,9, 17,4 y 20,0; Europa, Oriente Medio y África 10,6, 12,4 y 14,5; Latinoamérica 4,4, 4,8 y 5,4; Asia-Pacífico 3,8, 4,4 y 5,4.",
        ["2023", "2024", "2025"],
        [("EE. UU. y Canadá", [14.874, 17.359, 19.957], "navy"), ("Europa, Oriente Medio y África", [10.556, 12.387, 14.515], "teal"),
         ("Latinoamérica", [4.446, 4.840, 5.358], "gold"), ("Asia-Pacífico", [3.764, 4.415, 5.354], "coral")],
        unit="miles de millones de USD", horizontal=True, decimals=1, label_w=70,
        note="Asia-Pacífico crece 21 por ciento en 2025 frente al 15 de EE. UU. y Canadá, pero este último sigue siendo la región más grande. Latinoamérica crece 11 por ciento. Los ingresos incluyen el efecto de coberturas cambiarias que el 10-K desglosa.",
        note_kind="gold", foot=SEC)


def captacion() -> Fig:
    pts = [(2003, 1.487, "1,5", "t"), (2004, 2.610, "2,6", "t"), (2005, 4.179, "4,2", "t"), (2006, 6.316, "6,3", "t"), (2007, 7.479, "7,5", "t")]
    return line_chart(
        "La economía del DVD: suscriptores a fin de año antes del streaming (millones)",
        "Línea de suscriptores de Netflix a fin de año de 2003 a 2007: 1,5; 2,6; 4,2; 6,3 y 7,5 millones; el coste de adquirir un suscriptor se movió entre 32,80 y 42,96 dólares y la rotación fue 4,3 por ciento en 2007.",
        [("Suscriptores", pts, "teal")], x_label="Fin de año", y_label="Millones de suscriptores",
        x_ticks=[(2003, "2003"), (2004, "2004"), (2005, "2005"), (2006, "2006"), (2007, "2007")], plot_h=250,
        note="Coste de adquisición por suscriptor: 32,80 USD en 2003, 37,02 en 2004, 38,77 en 2005, 42,96 en 2006 y 40,88 en 2007; margen bruto de 34,8 por ciento en 2007 y rotación de 4,3 por ciento (el 10-K la rotula «anualizada»). Se ve la economía previa al streaming: crecer cuesta unos 40 dólares por suscriptor nuevo.",
        note_kind="gold", foot=SEC)


def ingresos() -> Fig:
    pts = [(2007, 1.205, "1,2", "t"), (2012, 3.609, "3,6", "t"), (2013, 4.375, "4,4", "t"), (2014, 5.505, "5,5", "t"), (2015, 6.780, "6,8", "t"),
           (2016, 8.831, "8,8", "t"), (2023, 33.723, "33,7", "t"), (2024, 39.001, "39,0", "t"), (2025, 45.183, "45,2", "t")]
    return line_chart(
        "Ingresos anuales de Netflix en años citados (miles de millones de USD)",
        "Línea de ingresos con nueve puntos: 1,2 miles de millones en 2007, 3,6 en 2012, 4,4 en 2013, 5,5 en 2014, 6,8 en 2015, 8,8 en 2016, 33,7 en 2023, 39,0 en 2024 y 45,2 en 2025; el tramo 2017-2022 no se grafica.",
        [("Ingresos", pts, "navy")], x_label="Año fiscal", y_label="Miles de millones de USD",
        x_ticks=[(2007, "2007"), (2010, "2010"), (2013, "2013"), (2016, "2016"), (2019, "2019"), (2022, "2022"), (2025, "2025")],
        vlines=[(2016, "2016: nube completa")], plot_h=280,
        note="El margen operativo fue 29,5 por ciento en 2025, 26,7 en 2024 y 20,6 en 2023; en 2012 el resultado operativo fue de 50 millones sobre 3 609 de ingresos. El tramo de 2017 a 2022 no se grafica porque este caso no cita esos 10-K: la línea no debe leerse como crecimiento regular.",
        note_kind="gold", foot=SEC)


FIGURES = {
    "netflix-contexto.svg": contexto,
    "netflix-capas-de-resiliencia.svg": componentes,
    "netflix-flujo-de-reproduccion.svg": flujo,
    "netflix-linea-de-tiempo.svg": linea,
    "netflix-miembros-de-pago.svg": miembros,
    "netflix-de-donde-sale-el-margen.svg": gastos,
    "netflix-actores-e-incentivos.svg": actores,
    "netflix-recorridos-de-usuario.svg": viajes,
    "netflix-contenedores.svg": contenedores,
    "netflix-secuencia-de-reproduccion.svg": secuencia,
    "netflix-hystrix-por-dentro.svg": hystrix,
    "netflix-despliegue-y-regiones.svg": despliegue,
    "netflix-evolucion-por-etapas.svg": evolucion,
    "netflix-datos-y-consistencia.svg": datos,
    "netflix-alternativas-descartadas.svg": alternativas,
    "netflix-contenido-amortizado.svg": contenido,
    "netflix-ingresos-por-region.svg": regiones,
    "netflix-economia-del-dvd.svg": captacion,
    "netflix-ingresos-anuales.svg": ingresos,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
