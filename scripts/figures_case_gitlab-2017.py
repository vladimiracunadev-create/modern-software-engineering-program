"""Figures for the failure case study casos/fallo/gitlab-2017.md.

Facts come from GitLab's public post mortem "Postmortem of database outage of January 31" (10 Feb 2017).
Times are UTC; hours and ratios derived from them are marked as own calculation.
"""
from __future__ import annotations

from figure_kit import Fig, _kit_finish, _kit_start, _wrap, grouped_bars, timeline

FUENTE = "Fuente: postmortem público de GitLab (10 feb 2017); esquema propio."


def sketch(title: str, desc: str, width: int = 940):
    """Start a mechanism diagram with a visible title; returns the figure and the first free y."""
    return _kit_start(title, desc, width, None)


def bx(f: Fig, x: float, y: float, w: float, h: float, text: str, kind: str = "plain", size: int = 13,
       bold: bool = False, dashed: bool = False) -> None:
    """Box that refuses to overflow: the text must fit its rectangle."""
    lines = _wrap(text, size, w - 20)
    assert len(lines) * size * 1.28 <= h - 6, f"box overflows: {text!r} ({len(lines)} lines in {h}px)"
    f.box(x, y, w, h, text, kind, size, bold=bold, dashed=dashed)


def done(f: Fig, y: float, note: str, kind: str = "gold", foot: str = FUENTE) -> Fig:
    _kit_finish(f, y, note, kind, foot)
    f.kind = "diagram"
    return f


# ------------------------------------------------------------------ 1. capas de recuperación
def capas_de_recuperacion() -> Fig:
    f, y = sketch("Cuatro caminos de recuperación el 31 de enero de 2017 y por qué solo uno sirvió",
                  "Diagrama alrededor de la base de datos primaria db1 con cuatro caminos de recuperación. La réplica db2 estaba en espera pero se vació al resincronizarla. La copia lógica diaria con pg_dump hacia S3 no existía porque usaba la versión 9.2 frente a una base 9.6 y sus avisos por correo eran rechazados. Las instantáneas de Azure no estaban habilitadas para las bases de datos. La instantánea LVM diaria hacia staging sí existía y fue la única fuente utilizable, con una de las 17:20.")
    bx(f, 340, y + 8, 260, 62, "db1: base de datos primaria de GitLab.com (PostgreSQL 9.6)", "navy", 13, True)
    caminos = (
        (10, "db2: réplica en espera", "Vaciada al intentar resincronizarla: ya no podía asumir el servicio", "coral"),
        (245, "pg_dump cada 24 h a S3", "Falló en silencio: versión 9.2 frente a 9.6; los avisos por correo se rechazaron por DMARC; depósito vacío", "coral"),
        (480, "Instantáneas de Azure", "No estaban habilitadas para las bases de datos", "coral"),
        (715, "Instantánea LVM diaria", "Existía para probar cambios en staging; la de las 17:20 fue la única utilizable", "gold"),
    )
    for x, t, d, k in caminos:
        bx(f, x, y + 120, 215, 44, t, "plain", 13, True)
        bx(f, x, y + 172, 215, 130, d, k)
        f.arrow([(470, y + 70), (x + 107, y + 120)])
    return done(f, y + 318, "Documentado: el estado de cada camino y que la instantánea LVM no estaba pensada para recuperación ante desastres. Que el sistema dependiera de un mecanismo no diseñado para ese fin es lectura propia a partir del postmortem de GitLab.", "gold")


# ------------------------------------------------------------------ 2. cadena de causas
def cadena_de_causas() -> Fig:
    f, y = sketch("De una cuenta marcada por spam a un borrado en el servidor equivocado",
                  "Seis pasos encadenados. Una cuenta de empleado fue marcada por abuso y programada para borrado, lo que sumado a spam elevó la carga de la base de datos. La replicación se retrasó porque la primaria eliminó segmentos de registro que la réplica aún necesitaba. Resincronizar exigía vaciar el directorio de la réplica. pg_basebackup se quedó esperando sin mensajes. Tras varios intentos, el borrado se ejecutó en la primaria y eliminó unos 300 GB.")
    pasos = (("Cuenta marcada por abuso y borrado programado, más spam: sube la carga", "gold"),
             ("La primaria elimina segmentos WAL que la réplica aún necesitaba: la réplica se retrasa", "gold"),
             ("Resincronizar es manual: hay que vaciar el directorio de datos de la réplica", "plain"),
             ("pg_basebackup espera en silencio; se prueban max_wal_senders y max_connections", "plain"),
             ("El borrado del directorio se ejecuta en la primaria: unos 300 GB eliminados", "coral"),
             ("Los respaldos no existían o no servían: hay que copiar desde staging", "coral"))
    w, gap = 288, 28
    for i, (t, k) in enumerate(pasos):
        row, col = divmod(i, 3)
        x, yy = 10 + col * (w + gap), y + 8 + row * 130
        bx(f, x, yy, w, 92, t, k)
        if col:
            f.arrow([(x - gap, yy + 46), (x, yy + 46)])
    f.arrow([(10 + 2 * (w + gap) + w / 2, y + 100), (10 + 2 * (w + gap) + w / 2, y + 118), (10 + w / 2, y + 118), (10 + w / 2, y + 138)])
    return done(f, y + 280, "Ningún paso, por sí solo, era un error evidente en su momento: cada uno tenía una explicación local. Lo documentado es la secuencia; la ausencia de automatización y de documentación del procedimiento de resincronización es la causa que el propio postmortem señala en su análisis de los cinco porqués.", "gold")


# ------------------------------------------------------------------ 3. línea de tiempo
def linea_de_tiempo() -> Fig:
    return timeline(
        "Casi 25 horas entre la instantánea manual y el cierre de la restauración",
        "Línea de tiempo en horas desde las 17:00 UTC del 31 de enero de 2017. Instantánea manual a las 17:20. Carga alta por spam desde las 19:00. Fallo de replicación hacia las 23:00. Borrado de la primaria hacia las 23:30. La base se restaura sin webhooks a las 17:00 del 1 de febrero, hora 24, y los últimos pasos terminan hacia las 18:00, hora 25.",
        [
            ("Carga alta por spam", [(2, 6, "carga alta", "gold")]),
            ("Réplica y resincronización", [(6, 6.5, "", "navy"), (6.5, 24, "intentos fallidos y copia desde staging", "grey")]),
            ("GitLab.com no disponible", [(6.5, 25, "unas 18 horas sin servicio", "coral")]),
            ("Datos que se pierden", [(0.33, 6.5, "17:20 a 23:30", "navy")]),
        ],
        unit="horas desde las 17:00 UTC del 31 de enero de 2017",
        events=[(0.33, "17:20 instantánea"), (6.5, "≈23:30 borrado"), (24, "17:00 restaurada")],
        t_max=28, ticks=[0, 4, 8, 12, 16, 20, 24, 28], lane_h=48, label_w=230,
        note="Documentado: las horas citadas y que la copia de datos desde staging tomó unas 18 horas por discos de red limitados a unos 60 Mbps. El postmortem da dos cierres para la ventana de datos perdidos, 23:30 y 00:00 UTC; la figura usa 23:30, el de la sección de impacto.",
        foot="Fuente: postmortem público de GitLab (10 feb 2017). Barra de resincronización: la fuente no da su inicio exacto.")


# ------------------------------------------------------------------ 4. horas
def horas() -> Fig:
    return grouped_bars(
        "Datos y tiempo en juego: lo que dependía de cuál respaldo se usara",
        "Barras horizontales en horas. Restaurar la instantánea diaria habría costado casi 24 horas de datos; la instantánea manual de las 17:20, unas 6. Copiar la base desde staging a producción llevó unas 18 horas, y el servicio estuvo unas 18 horas fuera de línea.",
        ["Datos perdidos con la instantánea diaria", "Datos perdidos con la instantánea de las 17:20", "Copia de staging a producción", "Servicio fuera de línea"],
        [("Horas", [24, 6, 18, 18], "navy")],
        unit="horas (aproximadas)", horizontal=True, label_w=300,
        note="Las cuatro cifras vienen del postmortem de GitLab como «casi 24 horas», «unas 6 horas», «unas 18 horas» y «unas 18 horas». Son órdenes de magnitud: ninguna tiene precisión de minutos. La barra de datos y la de tiempo no se suman.",
        foot="Fuente: postmortem público de GitLab (10 feb 2017). Cifras aproximadas.")


# ------------------------------------------------------------------ 5. de qué dependía a qué se comprometió
def antes_y_despues() -> Fig:
    f, y = sketch("Cada debilidad del 31 de enero con el compromiso que GitLab publicó",
                  "Cinco pares de cajas unidos por flechas. Un respaldo sin supervisión se acompaña de monitoreo de respaldos en Prometheus. Un respaldo nunca probado, de pruebas automáticas de restauración. Ausencia de instantáneas de base de datos, de instantáneas por hora y de disco en Azure. Una réplica única, de recuperar réplicas y de investigar archivado continuo con recuperación a un punto en el tiempo. Procedimiento sin dueño, de asignar un responsable de la durabilidad de los datos.")
    pares = (("Los avisos de fallo del respaldo se perdían por correo", "Monitoreo de respaldos con Prometheus y un panel público"),
             ("El respaldo nunca se probaba: nadie era responsable", "Pruebas automáticas de restauración y un dueño de la durabilidad"),
             ("Solo instantáneas diarias y ninguna de disco para las bases de datos", "Instantáneas LVM cada hora; investigar instantáneas de disco en Azure"),
             ("Una réplica que, al vaciarse, dejaba sin camino de recuperación", "Recuperar réplicas; investigar archivado continuo y punto en el tiempo"),
             ("Dos servidores casi idénticos en la terminal", "Mensaje del intérprete que distingue servidor y entorno"))
    f.text(10, y + 16, "Debilidad documentada", 14, "start", 700, "#5c1f14")
    f.text(520, y + 16, "Compromiso publicado por GitLab", 14, "start", 700, "#0b3f45")
    for i, (a, b) in enumerate(pares):
        yy = y + 28 + i * 74
        bx(f, 10, yy, 420, 58, a, "coral")
        bx(f, 520, yy, 410, 58, b, "teal")
        f.arrow([(430, yy + 29), (520, yy + 29)])
    return done(f, y + 28 + 5 * 74 + 6, "Los compromisos son los que GitLab enumeró en su postmortem como incidencias abiertas, no resultados verificados: el artículo no dice si se completaron ni cuándo. La conclusión de qué habría bastado es análisis propio y se desarrolla en la sección de mejoras del caso.", "gold")


FIGURES = {
    "gitlab-2017-capas-de-recuperacion.svg": capas_de_recuperacion,
    "gitlab-2017-cadena-de-causas.svg": cadena_de_causas,
    "gitlab-2017-linea-de-tiempo.svg": linea_de_tiempo,
    "gitlab-2017-horas-en-juego.svg": horas,
    "gitlab-2017-antes-y-despues.svg": antes_y_despues,
}
