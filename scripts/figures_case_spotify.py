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


# ======================================================================
# Ampliación (nov. 2026): niveles de zoom de la arquitectura de datos y de experimentación,
# economía de regalías y estructura de la audiencia. Cifras de las fuentes F1-F13 del caso.
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


# ---------------------------------------------------------------- flujo de las regalías
def regalias() -> Fig:
    f = Fig(940, 0, "Cómo fluye el dinero de Spotify hasta los titulares de derechos",
            "Diagrama del flujo de dinero según Loud and Clear: suscripciones Premium y publicidad del nivel gratuito forman el ingreso; unas dos terceras partes van a un fondo de regalías que se reparte por cuota de reproducciones; Spotify paga a los titulares de derechos y estos pagan a artistas y compositores según sus contratos; reglas como el mínimo de mil reproducciones y la exclusión de reproducciones artificiales moldean el reparto.")
    _head(f, "Cómo fluye el dinero de Spotify hasta los titulares de derechos")
    f.box(20, 55, 200, 66, "Oyentes Premium\n(suscripción)", "teal", 13, bold=True)
    f.box(20, 140, 200, 66, "Anunciantes\n(nivel gratuito)", "gold", 13, bold=True)
    f.box(290, 85, 180, 90, "Ingreso de Spotify\n(Premium + anuncios)", "navy", 13, bold=True)
    f.box(540, 55, 180, 66, "Fondo de regalías\n(≈ dos tercios)", "coral", 13, bold=True)
    f.box(540, 140, 180, 66, "Resto: costos y\nresultado de Spotify", "grey", 13)
    f.box(760, 55, 160, 66, "Titulares de derechos\n(sellos, editoras)", "plain", 13, bold=True)
    f.box(760, 140, 160, 66, "Artistas y\ncompositores", "plain", 13)
    f.arrow([(220, 88), (290, 110)])
    f.arrow([(220, 173), (290, 150)])
    f.arrow([(470, 115), (540, 90)])
    f.arrow([(470, 145), (540, 170)])
    f.arrow([(720, 88), (760, 88)])
    f.arrow([(840, 121), (840, 140)])
    f.box(20, 230, 440, 92, "Reparto por «cuota de reproducciones» (streamshare): cada titular recibe su porcentaje del total de reproducciones, no una tarifa fija por reproducción, porque el oyente paga una suscripción y no por escucha.", "plain", 13)
    f.box(480, 230, 440, 92, "Reglas que mueven el reparto: una pista necesita al menos 1 000 reproducciones al año para generar regalías de grabación, y las reproducciones artificiales detectadas no generan regalías (política declarada por Spotify).", "gold", 13)
    f.box(20, 336, 900, 56, "Cifras de Spotify: más de 11 mil millones de dólares pagados en 2025 y cerca de 70 mil millones acumulados desde la fundación. Son datos de la empresa, publicados para defender su modelo.", "coral", 13)
    y = _notebox(f, 406, "Lectura: de izquierda a derecha, el dinero entra por dos puertas y sale en su mayor parte hacia el fondo de regalías; lo que queda cubre todo lo demás. Spotify no paga a artistas directamente sino a titulares de derechos. Dónde deja de valer: Spotify no publica el cálculo contractual con cada sello ni el desglose entre regalías de grabación y de edición; «dos tercios» es una cifra redondeada de su sitio y no un contrato.")
    _footer(f, y + 6, "Fuente: Spotify, Loud & Clear, preguntas frecuentes, actualizado el 11 de marzo de 2026 (F3). Dibujo propio.")
    return f


# ---------------------------------------------------------------- industria
def industria() -> Fig:
    return grouped_bars(
        "El mercado de la música grabada: del máximo de 1999 al piso de 2014 y la recuperación",
        "Barras con tres cifras de la industria publicadas por Spotify: 24 mil millones de dólares en el máximo de 1999, 13 mil millones en 2014 y 31,7 mil millones en la cifra más reciente que cita, de IFPI.",
        ["1999 (máximo)", "2014 (piso)", "Hoy (cifra IFPI citada por Spotify)"],
        [("Mercado mundial de música grabada", [24.0, 13.0, 31.7], "teal")],
        unit="Miles de millones de dólares", decimals=1, plot_h=240,
        note="Lectura: la piratería y el desplome precedieron a Spotify (2008) y la recuperación posterior coincide con el streaming; la figura no prueba causalidad, la afirma Spotify. Dónde deja de valer: son datos de la industria interpretados por Spotify, que el propio sitio rotula como su interpretación; la tercera cifra no lleva año en la fuente y por eso se rotula «hoy».",
        note_kind="gold", foot="Fuente: Spotify, Loud & Clear (F3), que cita a IFPI; interpretación de Spotify.")


# ---------------------------------------------------------------- audiencia Premium
def audiencia() -> Fig:
    return stacked_bars(
        "Cuarto trimestre de 2025: cuántos de los 751 millones de usuarios pagan",
        "Barra apilada: de 751 millones de usuarios activos mensuales, 290 millones son suscriptores Premium y los restantes 461 millones (cálculo propio) no pagan suscripción; más del 60 por ciento de los suscriptores que se suman por primera vez empieza en el nivel gratuito.",
        ["Usuarios activos mensuales"],
        [("Suscriptores Premium", [290], "teal"), ("Resto de usuarios activos (cálculo propio)", [461], "grey")],
        unit="Millones de usuarios, T4 2025", horizontal=True, decimals=0, plot_h=150, label_w=150,
        note="Lectura: el nivel gratuito es la mayor parte de la audiencia y también el embudo: Spotify declara que más del 60 % de los suscriptores nuevos empezó allí. Dónde deja de valer: la resta 751 − 290 es del autor y agrupa a todos los usuarios que no son suscriptores; no es una cifra publicada de usuarios del nivel gratuito.",
        note_kind="gold", foot="Fuentes: comunicado T4 2025 (F2); Loud & Clear (F3) para el 60 %.")


# ---------------------------------------------------------------- arquitectura de la entrega de eventos
def eventos_arquitectura() -> Fig:
    f = Fig(940, 0, "Entrega de eventos en Google Cloud: un tema, un ETL y un destino por cada tipo de evento",
            "Diagrama de la arquitectura de entrega de eventos de Spotify en 2019: los clientes y los servicios envían eventos al servicio de eventos, que reconoce el tipo y rechaza los mal formados; cada tipo tiene su propio tema de Pub/Sub, su ETL y su destino; un compositor central crea esos recursos; los tipos se clasifican en importancia alta, media y baja con objetivos de entrega distintos.")
    _head(f, "Entrega de eventos en Google Cloud: un tema, un ETL y un destino por tipo de evento")
    f.box(20, 60, 170, 70, "Clientes y servicios\n(emiten eventos)", "teal", 13, bold=True)
    f.box(230, 60, 170, 70, "Servicio de eventos\n(reconoce el tipo;\nrechaza los malos)", "navy", 13, bold=True)
    f.arrow([(190, 95), (230, 95)])
    f.group(440, 45, 480, 180, "Un carril por cada tipo de evento (más de 500 tipos)", "grey")
    f.box(460, 80, 130, 56, "Tema de\nPub/Sub", "plain", 13)
    f.box(610, 80, 130, 56, "ETL (un clúster\npor tipo)", "plain", 13)
    f.box(760, 80, 140, 56, "Destino: GCS\no BigQuery", "plain", 13)
    f.arrow([(590, 108), (610, 108)])
    f.arrow([(740, 108), (760, 108)])
    f.box(460, 150, 440, 56, "Particiones por hora o por día, inmutables una vez cerradas", "gold", 13)
    f.arrow([(400, 95), (460, 108)])
    f.box(20, 245, 280, 90, "Importancia ALTA: pagan regalías o calculan métricas clave; objetivo de entrega de pocas horas", "coral", 13)
    f.box(330, 245, 280, 90, "Importancia MEDIA: objetivo de 24 horas, para datos que se necesitan al día siguiente", "gold", 13)
    f.box(640, 245, 280, 90, "Importancia BAJA: objetivo de 72 horas, uso mayormente interno", "grey", 13)
    f.box(20, 350, 440, 70, "Compositor central: por cada tipo nuevo crea tema y suscripción, clúster ETL, distribuye el esquema, registra el SLO y configura monitoreo; limpia al retirar el tipo.", "teal", 13)
    f.box(480, 350, 440, 70, "Cerca de 15 microservicios en unas 2 500 máquinas virtuales; algunos con autoescalado, lo que alarga a tres horas el despliegue de toda la flota.", "plain", 13)
    y = _notebox(f, 436, "Lectura: el servicio de eventos es la única puerta; a partir de ahí cada tipo viaja solo, así un tipo ruidoso o roto no frena a los demás. Los tres escalones de importancia fijan qué se atiende primero en un incidente y a quién se despierta. Documentado en F5 para 2019. Dónde deja de valer: es el sistema de 2016-2019; la fuente de 2021 (F5-bis) describe otro rediseño y no se sabe qué parte sigue vigente hoy.")
    _footer(f, y + 6, "Fuente: Spotify Engineering, «Spotify's Event Delivery – Life in the Cloud» (noviembre de 2019). Dibujo propio.")
    return f


# ---------------------------------------------------------------- cuánto creció cada magnitud
def crecimiento() -> Fig:
    return grouped_bars(
        "Cuánto creció cada magnitud entre las dos observaciones que publica Spotify (veces)",
        "Barras horizontales con factores de crecimiento calculados con cifras citadas: usuarios de 75 a 232 millones (3,1 veces), eventos diarios de 100 a 500 mil millones entre abril de 2017 y el primer trimestre de 2019 (5 veces) y el pico de eventos por segundo de 1,5 a más de 8 millones (5,3 veces).",
        ["Usuarios (2016 → 2019)", "Eventos diarios (abr. 2017 → T1 2019)", "Pico de eventos por segundo (entrada en producción → T1 2019)"],
        [("Factor de crecimiento", [3.1, 5.0, 5.3], "coral")],
        unit="Veces (cifra final ÷ cifra inicial)", horizontal=True, decimals=1, label_w=330, plot_h=170,
        note="Lectura: los datos crecieron más deprisa que los usuarios, lo que Spotify explica porque el crecimiento depende también de cuántos equipos instrumentan y cuántos analistas piden datos. Dónde deja de valer: son factores del autor entre cifras de fuentes distintas y con definiciones distintas (usuarios de 2016 frente a MAU de 2019; el pico inicial es 1,5 M y el final es «más de 8 M»); sirven como orden de magnitud, no como medición.",
        note_kind="gold", foot="Fuentes: Google Cloud 2016; Spotify Engineering 2019 (F4, F5); cálculo propio.")


# ---------------------------------------------------------------- reenvío y deduplicación
def reenvio() -> Fig:
    f = Fig(940, 0, "Un evento desde un móvil sin conexión: reenvíos, duplicados y su deduplicación",
            "Secuencia de un evento del cliente móvil en la nueva infraestructura de eventos de Spotify: el SDK lo guarda si no hay conexión, lo reenvía según una política, el receptor lo acepta y lo publica, y el trabajo de deduplicación usa el identificador del mensaje para eliminar duplicados con una ventana de semanas.")
    _head(f, "Un evento desde un móvil sin conexión: reenvíos, duplicados y deduplicación")
    end = _seq(f, ["App del\nusuario (SDK)", "Receptor\n(API disponible)", "Entrega y\ndeduplicación", "Conjunto de\ndatos"], [
        (0, 0, "1. sin conexión: el evento queda guardado"),
        (0, 1, "2. al volver la red, reenvía el evento"),
        (1, 0, "3. confirma", True),
        (1, 2, "4. publica con identificador de mensaje"),
        (0, 1, "5. si no llegó la confirmación, reenvía otra vez"),
        (1, 2, "6. llega un duplicado"),
        (2, 2, "7. busca el identificador; descarta"),
        (2, 3, "8. escribe una sola copia"),
    ], 52, step_h=44)
    y = _notebox(f, end + 10, "Lectura: la flecha continua es un envío y la discontinua una confirmación. Los reenvíos pueden ocurrir de inmediato, en minutos o días después, o no ocurrir nunca; por eso un duplicado no se distingue de un evento nuevo sin identificador. En la nueva infraestructura el identificador permite mirar hacia atrás varias semanas, frente a las pocas horas de la anterior. Si el receptor cae, los eventos esperan en el cliente. Dónde deja de valer: describe el diseño anunciado en 2021 (F5-bis); no se sabe el porcentaje de pérdida residual y es imposible saber si un evento nunca existió o se perdió.")
    _footer(f, y + 6, "Fuente: Spotify Engineering, «Changing the Wheels on a Moving Bus» (octubre de 2021). Secuencia propia.")
    return f


# ---------------------------------------------------------------- antes y después de la infraestructura de eventos
def eventos_antes_despues() -> Fig:
    f = Fig(940, 0, "La infraestructura de eventos antes y después del rediseño de 2021",
            "Comparación de la infraestructura de eventos heredada y la nueva según Spotify: antes, eventos en texto separado por tabuladores guardados en disco del perímetro, servicios con estado y un esquema difícil de propagar; después, SDK con modelo de datos nuevo, receptor disponible, plano de control para declarar eventos, deduplicación con identificadores y Dataflow gestionado.")
    _head(f, "La infraestructura de eventos antes y después del rediseño de 2021")
    f.box(20, 55, 440, 40, "Antes (heredada)", "coral", 14, bold=True)
    f.box(480, 55, 440, 40, "Después (nueva, anunciada en 2021)", "teal", 14, bold=True)
    rows = [("Formato: cadenas TSV convertidas a Avro con una biblioteca de 2007", "Modelo de datos nuevo con SDK y esquemas declarados en un plano de control"),
            ("Eventos en disco del perímetro y reenviados: servicio con estado", "Receptor como API disponible; el cliente guarda y reenvía"),
            ("Móviles «dispara y olvida»: pérdida pequeña en casi todos los datos", "Reenvíos del cliente y deduplicación por identificador de mensaje"),
            ("Propagar un esquema tardaba horas; instrumentar tardaba una semana", "Control de eventos declarativo; adoptar sin intervención del equipo"),
            ("Trabajo pesado de Hadoop trasladado a Dataproc", "Scio sobre Dataflow gestionado, sin Hadoop")]
    y = 105
    for a, b in rows:
        f.box(20, y, 440, 56, a, "plain", 13)
        f.box(480, y, 440, 56, b, "plain", 13)
        f.arrow([(460, y + 28), (480, y + 28)])
        y += 66
    f.box(20, y + 4, 900, 56, "Restricción de la migración: la «cola larga» — las versiones antiguas de la app tardan meses en actualizarse y algunos dispositivos nunca lo harán —, por lo que ambas infraestructuras convivieron con un exportador que convierte lo heredado.", "gold", 13)
    y = _notebox(f, y + 76, "Lectura: cada fila contrasta una limitación heredada con su corrección; la flecha une las dos columnas. Lo heredado se mantuvo por una razón estratégica de 2016: migrar rápido a la nube compatible hacia atrás. Dónde deja de valer: son afirmaciones de Spotify sobre su propio sistema; no hay medición independiente del resultado ni cifras de pérdida posteriores.")
    _footer(f, y + 6, "Fuente: Spotify Engineering, «Changing the Wheels on a Moving Bus» (octubre de 2021). Dibujo propio.")
    return f


# ---------------------------------------------------------------- plataforma de experimentación
def experimentacion() -> Fig:
    f = Fig(940, 0, "La plataforma de experimentación: configuración remota, catálogo de métricas y planificador",
            "Diagrama de la plataforma de experimentación de Spotify de 2020: la configuración remota entrega propiedades a los clientes y registra eventos de asignación y aplicación; el catálogo de métricas ingiere métricas en un almacén; el planificador, con interfaz en Backstage, crea, lanza y analiza experimentos y avisa de problemas de validez.")
    _head(f, "La plataforma de experimentación: configuración remota, catálogo de métricas y planificador")
    f.box(20, 60, 190, 70, "Cliente\n(app o servicio)", "teal", 13, bold=True)
    f.box(260, 60, 220, 70, "Configuración remota\n(propiedades y políticas)", "navy", 13, bold=True)
    f.arrow([(210, 85), (260, 85)], "pide", label_at=(235, 72))
    f.arrow([(260, 110), (210, 110)], "valores", label_at=(235, 128))
    f.box(530, 60, 190, 70, "Eventos «asignada» y «aplicada»", "gold", 13)
    f.arrow([(480, 95), (530, 95)])
    f.box(760, 60, 160, 70, "Catálogo de\nmétricas (SQL a un\nalmacén)", "navy", 13, bold=True)
    f.arrow([(720, 95), (760, 95)])
    f.box(20, 170, 900, 66, "Planificador de experimentos (interfaz en Backstage): crea, lanza, detiene y analiza; exige definir de antemano hipótesis, métricas de éxito y de guardia, y ofrece una calculadora de tamaño de muestra.", "teal", 13, bold=True)
    f.arrow([(840, 130), (840, 170)])
    f.arrow([(370, 130), (370, 170)])
    f.box(20, 255, 290, 110, "Propiedad: variable con tipo y valor por defecto, declarada en un archivo junto al código. Solo se transfieren los valores que difieren del defecto.", "plain", 13)
    f.box(325, 255, 290, 110, "Los valores se descargan en segundo plano pero solo se aplican al relanzar la app: la experiencia no cambia a mitad de sesión.", "plain", 13)
    f.box(630, 255, 290, 110, "Exposición: asignada Y aplicada (y, opcionalmente, una fuente de exposición propia, como visitar una página).", "gold", 13)
    y = _notebox(f, 380, "Lectura: el cliente pide su configuración; la política decide qué valores recibe y registra dos eventos; esos eventos y las métricas alimentan al planificador. El valor por defecto da una experiencia predecible si el cliente no logra descargar nada. Dónde deja de valer: Spotify describe la plataforma de 2020; no se sabe cuántos experimentos corren a la vez ni cuántos se descartan.")
    _footer(f, y + 6, "Fuente: Spotify Engineering, «Spotify's New Experimentation Platform (Part 1)», octubre de 2020 (F6). Dibujo propio.")
    return f


# ---------------------------------------------------------------- máquina de sal (factor de compensación)
def salt() -> Fig:
    return line_chart(
        "La «máquina de sal»: cuánto hay que sobreasignar cuando se rebarajan usuarios libres",
        "Gráfico de líneas: el factor de compensación es la inversa de la fracción de usuarios que recibe una nueva sal; con la mitad es 2, con una cuarta parte es 4 y con una quinta parte es 5, el umbral por encima del cual Spotify recomienda no iniciar experimentos nuevos.",
        [("Factor de compensación = 1 ÷ fracción", [(0.5, 2, "2", "t"), (0.25, 4, "4", "t"), (0.2, 5, "5", "t"), (0.1, 10, "10", "t")], "coral")],
        x_label="Fracción de los usuarios que cae en la nueva sal", y_label="Factor de compensación (veces)", plot_h=260,
        hlines=[(5, "umbral práctico de Spotify: 5")],
        x_ticks=[(0.1, "0,1"), (0.2, "0,2"), (0.25, "0,25"), (0.5, "0,5")],
        note="Lectura: cuantos menos usuarios reciben la sal nueva, más cubos hay que asignar para obtener la misma población, y más espacio se desperdicia. Documentado: el ejemplo de la fuente (mitad de los usuarios, factor 2, cuatro de ocho cubos para el 25 %) y la regla de no empezar experimentos con factor superior a 5. Dónde deja de valer: la serie 0,25, 0,2 y 0,1 es cálculo propio con la misma fórmula; Spotify dice que trabaja en una segunda iteración del esquema de asignación.",
        note_kind="gold", foot="Fuente: Spotify Engineering, «Spotify's New Experimentation Platform (Part 2)», noviembre de 2020 (F13); fórmula 1/f.")


# ---------------------------------------------------------------- holdbacks
def holdbacks() -> Fig:
    f = Fig(940, 0, "Un trimestre con retenedor: medir el efecto compuesto de todo lo que se lanzó",
            "Diagrama de un ciclo trimestral de reserva (holdback) en la experimentación de Spotify: al inicio se crea un grupo de usuarios exento de los experimentos del dominio; durante el trimestre los experimentos nunca lo asignan; al cierre se ejecuta una prueba en la que ese grupo recibe la experiencia combinada de todo lo lanzado, y luego se libera.")
    _head(f, "Un trimestre con retenedor: medir el efecto compuesto de lo lanzado")
    f.box(20, 60, 200, 80, "Inicio del trimestre:\nse crea el grupo\nretenido", "teal", 13, bold=True)
    f.box(260, 60, 300, 80, "Durante el trimestre: los experimentos del dominio nunca asignan a esos usuarios", "gold", 13)
    f.box(600, 60, 320, 80, "Cierre: una sola prueba da a ese grupo la experiencia combinada de todos los cambios exitosos", "navy", 13, bold=True)
    f.arrow([(220, 100), (260, 100)])
    f.arrow([(560, 100), (600, 100)])
    f.box(600, 170, 320, 56, "Se libera el grupo y entra de nuevo en los experimentos", "plain", 13)
    f.arrow([(760, 140), (760, 170)])
    f.box(20, 170, 440, 100, "Qué resuelve: cada experimento mide su efecto aislado; el retenedor mide el efecto acumulado y a largo plazo de lo que el equipo decidió lanzar.", "teal", 13)
    f.box(20, 285, 440, 100, "Costo: un grupo de usuarios no recibe mejoras durante un trimestre y su tamaño debe bastar para detectar el efecto compuesto.", "coral", 13)
    f.box(480, 240, 440, 145, "Exclusividad: algunos experimentos se excluyen mutuamente porque pueden interactuar; por ahora solo lo son los de un mismo dominio, y Spotify planea desacoplar la exclusividad del dominio.", "plain", 13)
    y = _notebox(f, 400, "Lectura: de izquierda a derecha, el ciclo del grupo retenido. Dónde deja de valer: la práctica es de un dominio del producto y de la plataforma de 2020; Spotify no publica la proporción retenida ni los resultados de los cierres trimestrales, y el costo del recuadro rojo es análisis propio.")
    _footer(f, y + 6, "Fuente: Spotify Engineering, «Spotify's New Experimentation Platform (Part 2)», noviembre de 2020 (F13). Dibujo propio.")
    return f


# ---------------------------------------------------------------- validez del experimento
def validez() -> Fig:
    f = Fig(940, 0, "Controles de validez de un experimento: qué vigila la plataforma y qué avisa",
            "Diagrama de los cuatro controles de validez continuos de la plataforma de experimentación de Spotify (desajuste en la proporción de muestra, actividad previa a la exposición, aumento de caídas y colisión de propiedades) y de las dos clases de métricas: de éxito con prueba de superioridad y de guardia con prueba de no inferioridad.")
    _head(f, "Controles de validez de un experimento: qué vigila la plataforma y qué avisa")
    f.box(20, 55, 440, 70, "Desajuste de proporción de muestra: la exposición real no coincide con la repartición prevista entre grupos", "coral", 13)
    f.box(480, 55, 440, 70, "Actividad previa: los grupos ya se comportaban distinto antes de que empezara el experimento", "coral", 13)
    f.box(20, 140, 440, 70, "Aumento de caídas del cliente en algún grupo", "coral", 13)
    f.box(480, 140, 440, 70, "Colisión de propiedades: dos experimentos no exclusivos tocan la misma propiedad de configuración", "coral", 13)
    f.box(20, 235, 440, 90, "Métricas de éxito: prueba de superioridad con efecto mínimo detectable y cálculo de potencia", "teal", 13, bold=True)
    f.box(480, 235, 440, 90, "Métricas de guardia: prueba de no inferioridad con un margen declarado de antemano", "gold", 13, bold=True)
    f.box(20, 340, 900, 56, "Si hay un problema se avisa al equipo dueño, que decide qué hacer; las pruebas con test estadístico usan secuencial y corrigen comparaciones múltiples.", "plain", 13)
    y = _notebox(f, 412, "Lectura: arriba, los controles que protegen la validez; abajo, las dos clases de métricas con su prueba. Los experimentos deben correr el periodo planificado y detenerse antes solo por efectos dañinos, para no sesgar por día de la semana. Dónde deja de valer: son controles declarados por Spotify en 2020; la plataforma no se evalúa de forma independiente aquí.")
    _footer(f, y + 6, "Fuente: Spotify Engineering, «Spotify's New Experimentation Platform (Part 2)», noviembre de 2020 (F13).")
    return f


# ---------------------------------------------------------------- Discover Weekly
def discover_weekly() -> Fig:
    f = Fig(940, 0, "Del año en música a Discover Weekly: cómo se validó antes de lanzarse a todos",
            "Flujo del origen de Discover Weekly según Spotify: de Year in Music en 2011 y de la lista Play it Forward de 2014 más la página Discover surgió la primera versión; se probó con empleados, luego con una prueba pequeña de usuarios con más de 1.500 respuestas a una encuesta y un grupo de control con imagen por defecto, y después se lanzó a todos.")
    _head(f, "Del año en música a Discover Weekly: cómo se validó antes de lanzarse")
    steps = [("2011\nYear in Music\n(recap anual)", "plain"), ("2014\nPlay it Forward\n(lista de música nueva)", "plain"), ("Se fusiona con la\npágina Discover\n→ primera versión", "gold"), ("Prueba interna:\nempleados", "teal"), ("Prueba con usuarios:\n+1.500 respuestas\ny control", "teal"), ("Lanzamiento\na todos", "navy")]
    x = 20
    for t, k in steps:
        f.box(x, 60, 140, 96, t, k, 13, bold=(k == "navy"))
        x += 150
    for i in range(5):
        f.arrow([(20 + i * 150 + 140, 108), (20 + (i + 1) * 150, 108)])
    f.box(20, 185, 440, 80, "Decisiones de diseño: dos horas de duración y una actualización semanal, para que cada canción se sintiera especial y se formara el hábito.", "plain", 13)
    f.box(480, 185, 440, 80, "Un error que se conservó: un fallo que dejaba pasar contenido semiconocido generaba confianza y se mantuvo.", "gold", 13)
    f.box(20, 280, 440, 80, "Sesgo evitado: los empleados son superusuarios, así que se hizo una prueba con usuarios; el grupo de control con imagen por defecto mostró el efecto de la imagen personalizada.", "teal", 13)
    f.box(480, 280, 440, 80, "Límite: la fuente de 2015 no publica cuántos usuarios tuvo la prueba ni los resultados numéricos de retención.", "coral", 13)
    y = _notebox(f, 376, "Lectura: de izquierda a derecha el camino del producto; la mayor parte de la tecnología de personalización ya existía y estaba escondida varias capas dentro del producto, y lo nuevo fue el formato (la lista, el ritmo semanal, la imagen). Dónde deja de valer: es un relato de Spotify sobre su éxito; las cifras de 75 millones de listas semanales las da la propia empresa y no se verificaron aparte.")
    _footer(f, y + 6, "Fuente: Spotify Engineering, «What made Discover Weekly one of our most successful feature launches to date?», noviembre de 2015 (F7).")
    return f


# ---------------------------------------------------------------- línea de tiempo ampliada
def linea_tiempo2() -> Fig:
    return timeline(
        "Spotify: producto, plataforma de datos y práctica de experimentación",
        "Línea de tiempo de 2006 a 2026 con tres carriles: producto (música, podcasts, audiolibros), plataforma (centros de datos propios y Google Cloud desde 2016, con Kafka apagado en febrero de 2017) y práctica de datos (ABBA en 2013, nueva plataforma de experimentación en 2020); marcadores de fundación, lanzamiento, nube y audiolibros.",
        [("Producto", [(2008, 2015, "Música en streaming", "teal"), (2015, 2022, "Podcasts y descubrimiento", "gold"), (2022, 2026, "Audiolibros", "coral")]),
         ("Plataforma", [(2008, 2016, "Centros de datos propios", "grey"), (2016, 2026, "Google Cloud (datos y servicios)", "navy")]),
         ("Datos y experimentos", [(2013, 2020, "ABBA y eventos", "gold"), (2020, 2026, "Plataforma nueva", "teal")])],
        unit="Año", events=[(2008, "Lanzamiento"), (2013, "ABBA"), (2016, "Nube"), (2017, "Kafka off"), (2022, "Audiolibros")], t_max=2026, ticks=[2006, 2010, 2014, 2018, 2022, 2026], lane_h=54, label_w=150,
        note="Documentado: lanzamiento en 2008 y audiolibros en 2022 (Spotify Newsroom); decisión de ir a Google Cloud en febrero de 2016 (Google Cloud); apagado del sistema basado en Kafka en febrero de 2017 (F5); ABBA en 2013 y nueva plataforma en 2020 (F6). Fuente secundaria: fundación en 2006 y bolsa en 2018. Dónde deja de valer: las eras son síntesis del autor; la migración fue gradual y no hubo un corte único en 2016.",
        note_kind="gold", foot="Fuentes: F1, F4, F5, F6 y F13; síntesis propia de las eras.")



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
    return _cards('Hardware de Spotify: lo que se publica y lo que no', 'Diagrama del hardware que Spotify documenta: tras 2016 usa máquinas virtuales de Google Cloud (unas 2.500 en la entrega de eventos), discos SSD de alta capacidad y servicios de red del proveedor; los clientes son móviles, televisores y altavoces; no se publican servidores propios de la época anterior ni el hardware del servicio de audio.', [('Servidores', 'teal', ['Documentado: la migración de 2016 dejó de operar centros de datos propios; antes compraba o alquilaba espacio, equipos y redes (F4).', 'Documentado: la entrega de eventos corre en unas 2.500 máquinas virtuales de Compute Engine en 2019 (F5).', 'No se sabe: tipos de máquina, regiones y volumen de flota del audio.']), ('Almacenamiento y red', 'gold', ['Documentado: Google destaca discos SSD de muchas operaciones por segundo y SSD locales, además de Direct Peering, VPN y enrutadores en nube para mover petabytes (F4).', 'No se sabe: capacidad de almacenamiento de audio y distribución por CDN.']), ('Dispositivos de usuario', 'navy', ['Documentado: móviles con modo sin conexión, y televisores y altavoces que se actualizan poco o nunca (F5-bis).', 'Documentado: la plataforma de experimentación llega a clientes de escritorio, móvil y servicios (F6).']), ('Época P2P', 'grey', ['Documentado: en 2010 el servicio combinaba servidores con una red entre pares de los propios clientes (F10).', 'No se sabe: las mediciones del artículo: no se pudo leer el texto completo.'])], 'Lectura: cuatro recuadros separan nube, red, dispositivos y la época P2P. Dónde deja de valer: la información de nube es de 2016 y 2019; no hay inventario actual ni datos de hardware del reproductor.', 'Fuentes: F4, F5, F5-bis, F6, F10.')


def _x_software() -> Fig:
    return _cards('Software de Spotify que sus propias fuentes documentan', 'Diagrama del software documentado de Spotify: Pub/Sub, Cloud Storage, BigQuery, Dataproc, Dataflow y Cloud SQL en la entrega de eventos; Java, Scala con Scio y una biblioteca de Python de 2007; Avro para esquemas; Puppet, Docker y el orquestador interno Helios; Backstage y PlanOut en las herramientas internas; Kafka y Hadoop en el sistema anterior.', [('Datos y mensajería', 'teal', ['Documentado: Pub/Sub, Cloud Storage, Dataflow, Dataproc, BigQuery y Cloud SQL (F5); en 2016 adoptó además Cloud Datastore y Cloud Bigtable y se alejó de Hadoop, MapReduce y Hive (F4).', 'Documentado: el sistema anterior de eventos usaba Kafka y se apagó en febrero de 2017 (F5).']), ('Lenguajes y formatos', 'gold', ['Documentado: Java para los clientes de Pub/Sub; Scala con Scio sobre Beam y Dataflow en 2021; biblioteca de Python de 2007 para convertir TSV a Avro; Avro para esquemas compatibles hacia atrás (F5, F5-bis).', 'No se sabe: lenguajes de los servicios de audio.']), ('Orquestación y entrega', 'navy', ['Documentado: Puppet instalaba dependencias como Docker y Helios, el orquestador de contenedores interno, en cada máquina virtual (F5).', 'Documentado: pruebas de integración de extremo a extremo, entorno de preparación y máquinas canario (F5).']), ('Herramientas de código abierto', 'grey', ['Documentado: Backstage es un marco de código abierto de la CNCF en incubación (F8).', 'Documentado: la plataforma de experimentación usa PlanOut y SQL para métricas (F6).', 'Documentado: Scio y bibliotecas propias de Pub/Sub se mencionan como extensiones propias (F5).'])], 'Lectura: se agrupan por función; cada ítem lleva su fuente. Dónde deja de valer: son blogs de 2016 a 2021; no describen el reproductor, la búsqueda ni la recomendación.', 'Fuentes: F4, F5, F5-bis, F6, F8.')


def _x_infra() -> Fig:
    return _cards('Características de la infraestructura de Spotify: nube, escala y costo', 'Diagrama de la infraestructura de Spotify: nube pública de Google desde 2016; unas 2.500 máquinas virtuales y unos 15 microservicios en la entrega de eventos; 500 tipos de evento y más de 350 terabytes diarios en bruto en 2019; costos declarados como altos sin cifras; y regiones y zonas no publicadas.', [('Modelo', 'teal', ['Documentado: nube pública de Google, con una vía de servicios y una de datos (F4); decisión de no estar en el negocio de los centros de datos (F4).', 'No se sabe: qué parte, si alguna, sigue en infraestructura propia.']), ('Escala', 'gold', ['Documentado: en 2019, más de 500 tipos de evento, 350 terabytes diarios en bruto y picos de más de 8 millones de eventos por segundo; en 2021, cerca de 70 terabytes comprimidos diarios y más de 600 tipos (F5, F5-bis).', 'Documentado: en 2016, más de 2 mil millones de listas y más de 30 millones de canciones (F4).']), ('Costos', 'navy', ['Documentado: «los sistemas grandes cuestan mucho dinero»: decidieron abstraer el costo de los equipos y luego hacer ciclos de ahorro (F5).', 'No se sabe: gasto de nube en euros: no se publica; solo se conoce el margen bruto de 33,1 % de un trimestre (F2).']), ('Regiones y redes', 'grey', ['No se sabe: regiones, zonas de disponibilidad y topología de red de los servicios de audio.', 'Documentado: servicios de red del proveedor para transferir petabytes (F4).'])], 'Lectura: modelo, escala, costos y regiones; las dos últimas columnas casi no tienen dato público. Dónde deja de valer: las cifras de eventos son de datos de analítica y no de audio.', 'Fuentes: F2, F4, F5, F5-bis.')


def _x_fallos() -> Fig:
    return _cards('Qué pasa cuando cae cada componente en lo que Spotify documenta', 'Diagrama de la tolerancia a fallos documentada de Spotify: un tipo de evento roto no frena a los demás; un cliente móvil sin conexión reenvía; el receptor caído espera en el cliente; la migración corrió ambos sistemas en paralelo; los despliegues usan canarios; el verificador de salud propio corrigió un fallo de reemplazo de máquinas; no se documentan pruebas de caos ni recuperación ante desastres.', [('Un tipo de evento falla', 'teal', ['Documentado: aislamiento por tipo y vitalidad sobre tardanza: las particiones abiertas no bloquean a los demás tipos (F5).']), ('El receptor cae', 'gold', ['Documentado: los eventos esperan en el cliente y se reenvían con una política de reintento (F5-bis).']), ('Una máquina se reemplaza mal', 'coral', ['Documentado: el verificador de salud por defecto reemplazaba una máquina por otra con el mismo nombre y la infraestructura de configuración la rechazaba; escribieron el suyo (F5).']), ('Un cambio llega a producción', 'navy', ['Documentado: pruebas de extremo a extremo, entorno de preparación y canarios (F5).']), ('Una migración sale mal', 'plain', ['Documentado: ambos sistemas corrieron en paralelo para comparar completitud y se apagó el antiguo después (F5).']), ('Lo que no se documenta', 'grey', ['No se sabe: pruebas de caos, recuperación ante desastres, copias de seguridad y degradación elegante del reproductor.'])], 'Lectura: cada recuadro es un fallo y su defensa. Dónde deja de valer: solo cubre la plataforma de datos y las herramientas, no el audio.', 'Fuentes: F5, F5-bis.')


def _x_presencia() -> Fig:
    return _cards('Dónde tiene Spotify entidades y oficinas que su propia página de contacto publica', 'Diagrama por regiones de las entidades de Spotify con dirección publicada: sede en Estocolmo y sociedad matriz en Luxemburgo; en Europa Bruselas, Berlín, Copenhague, Madrid, Helsinki, París, Milán, Ámsterdam y Londres; en América Nueva York, Toronto y Ciudad de México; en Asia Mumbai e Israel.', [('Europa', 'teal', ['Documentado: sede del servicio en Estocolmo; Spotify Technology S.A. en Luxemburgo; entidades en Bruselas, Berlín, Copenhague, Madrid, Helsinki, París, Milán, Ámsterdam y Londres (F12).']), ('América', 'gold', ['Documentado: Spotify USA en Nueva York, que presta el servicio en Estados Unidos; entidades en Toronto y Ciudad de México (F12).']), ('Asia y Oriente Medio', 'navy', ['Documentado: Spotify India en Mumbai y una entidad en Israel, sin dirección en la página (F12).']), ('Lo que no se sabe', 'grey', ['No se sabe: años de apertura de cada oficina, dónde están los centros de ingeniería y cuántas personas trabajan en cada una.'])], 'Lectura: son entidades legales con dirección de contacto, no necesariamente centros de ingeniería. Dónde deja de valer: la página no fecha las aperturas ni cuenta plantilla; el servicio opera en 184 mercados con muchas menos oficinas.', 'Fuentes: F1 y F12.')


def _x_negocio() -> Fig:
    return _cards("Esquema del negocio de Spotify: valor, ingreso, actores y flujos",
        "Diagrama del negocio de Spotify con cinco grupos: la propuesta de valor, las dos fuentes de ingreso (suscripción Premium y publicidad del nivel gratuito), los actores, los flujos de dinero con un fondo de regalías de unos dos tercios, y los flujos de valor.",
        [("Propuesta de valor", "teal", ["Documentado: acceso inmediato a un catálogo enorme, con un nivel gratuito financiado por anuncios y una suscripción sin anuncios (F1, F3)."]),
         ("Ingreso (nueve meses de 2025, millones de euros)", "gold", ["Documentado: Premium 11.337 y Ad-Supported 1.318, total 12.655 (F14)."]),
         ("Actores", "navy", ["Oyentes del nivel gratuito y Premium, anunciantes, titulares de derechos (sellos y editoras), artistas, creadores de podcasts y de audiolibros, y Spotify (F1, F3)."]),
         ("Flujos de dinero", "coral", ["Documentado: Premium paga suscripción; anunciantes pagan por la audiencia gratuita; unos dos tercios del ingreso van al fondo de regalías y de allí a titulares de derechos (F3).", "Documentado: el costo de ingresos incluye regalías y distribución, costos de procesamiento de pagos y costos de contenido de podcasts (F14)."]),
         ("Flujos de valor", "grey", ["Música y audio a la carta hacia el oyente; descubrimiento y pago hacia el artista; audiencia hacia el anunciante; embudo del nivel gratuito hacia Premium (más del 60 % de los suscriptores nuevos) (F3)."])],
        "Lectura: cinco grupos desde lo que se ofrece hasta cómo circulan dinero y valor. Dónde deja de valer: los dos tercios son una cifra redondeada de la empresa; los contratos con cada sello no son públicos.",
        "Fuentes: F1, F3 y formulario 6-K del tercer trimestre de 2025 (F14).")


def _x_costos() -> Fig:
    return stacked_bars(
        "Qué pasó con cada 100 euros de ingreso de Spotify en los nueve primeros meses de 2025",
        "Barra apilada al 100 por ciento con los nueve meses de 2025: costo de ingresos 68,4 por ciento, investigación y desarrollo 8,7, ventas y marketing 8,1, administración 2,9 y resultado operativo 11,8 por ciento de los 12.655 millones de euros de ingreso.",
        ["Nueve meses de 2025"],
        [("Costo de ingresos", [8658], "coral"), ("Investigación y desarrollo", [1103], "navy"), ("Ventas y marketing", [1027], "gold"), ("Administración", [370], "grey"), ("Resultado operativo", [1497], "teal")],
        unit="Porcentaje del ingreso de nueve meses (12.655 millones de euros)", horizontal=True, percent=True, decimals=1, plot_h=150, label_w=100,
        note="Lectura: dos terceras partes del ingreso se van en el costo de ingresos, que incluye regalías y distribución; el resultado operativo es el 11,8 % de 12.655 millones de euros. Dónde deja de valer: son nueve meses, no el año; el formulario 6-K no separa las regalías del resto del costo de ingresos en estas líneas.",
        note_kind="gold", foot="Fuente: Spotify, formulario 6-K del tercer trimestre de 2025, estados financieros intermedios (F14).")


def _x_margen_segmentos() -> Fig:
    return grouped_bars(
        "Margen bruto por segmento de Spotify: nueve meses de 2024 y de 2025 (porcentaje del ingreso)",
        "Barras agrupadas: el margen bruto del segmento Premium pasa de 31,7 por ciento en los nueve primeros meses de 2024 a 33,2 en 2025, y el del segmento financiado con publicidad de 11,2 a 17,4 por ciento.",
        ["Premium", "Ad-Supported (publicidad)"],
        [("9 meses de 2024", [31.7, 11.2], "grey"), ("9 meses de 2025", [33.2, 17.4], "teal")],
        unit="Margen bruto (porcentaje del ingreso del segmento)", decimals=1, plot_h=240,
        note="Lectura: el nivel gratuito deja mucho menos margen bruto que la suscripción, aunque mejora; la suscripción pesa 90 % del ingreso. Dónde deja de valer: cálculo propio sobre cifras del 6-K (ganancia bruta dividida por ingreso del segmento); los gastos de operación no se asignan a segmentos.",
        note_kind="gold", foot="Fuente: Spotify, formulario 6-K del tercer trimestre de 2025, nota de segmentos (F14); cálculo propio.")

FIGURES = {
    "spotify-contexto-dos-lados.svg": contexto,
    "spotify-industria-musical.svg": industria,
    "spotify-usuarios.svg": usuarios,
    "spotify-audiencia-premium.svg": audiencia,
    "spotify-regalias-flujo-del-dinero.svg": regalias,
    "spotify-margen-t4-2025.svg": margen,
    "spotify-componentes-datos-e-ingenieria.svg": componentes,
    "spotify-eventos-arquitectura.svg": eventos_arquitectura,
    "spotify-flujo-entrega-de-eventos.svg": flujo_eventos,
    "spotify-reenvio-y-deduplicacion.svg": reenvio,
    "spotify-eventos-antes-y-despues.svg": eventos_antes_despues,
    "spotify-crecimiento-de-magnitudes.svg": crecimiento,
    "spotify-plataforma-de-experimentacion.svg": experimentacion,
    "spotify-maquina-de-sal.svg": salt,
    "spotify-retenedor-trimestral.svg": holdbacks,
    "spotify-validez-de-experimentos.svg": validez,
    "spotify-discover-weekly-camino.svg": discover_weekly,
    "spotify-linea-de-tiempo.svg": linea_tiempo2,
    "spotify-hardware-utilizado.svg": _x_hardware,
    "spotify-software-utilizado.svg": _x_software,
    "spotify-caracteristicas-de-la-infraestructura.svg": _x_infra,
    "spotify-tolerancia-a-fallos.svg": _x_fallos,
    "spotify-presencia-mundial.svg": _x_presencia,
    "spotify-esquema-del-negocio.svg": _x_negocio,
    "spotify-costos-operativos-9m-2025.svg": _x_costos,
    "spotify-margen-por-segmento.svg": _x_margen_segmentos,
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
