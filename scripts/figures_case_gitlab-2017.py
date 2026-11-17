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


# ==== EXPANDED FIGURES (begin) ====

# ------------------------------------------------------------------ 6. ecosistema
def ecosistema() -> Fig:
    f, y = sketch("GitLab.com en enero de 2017: dónde vivía cada dato y quién quedó fuera del incidente",
                  "Diagrama de contexto. Dentro del servicio GitLab.com: usuarios, aplicación, base de datos PostgreSQL, servidores NFS con repositorios y wikis, entorno de staging y copias en Amazon S3. Fuera del servicio: ediciones Enterprise, GitHost y autoalojadas, que no se vieron afectadas, y el equipo de GitLab, que usa GitLab.com para desarrollar GitLab.")
    f.group(10, y, 640, 250, "Servicio GitLab.com", "grey")
    bx(f, 28, y + 40, 190, 56, "Usuarios: desarrolladores, equipos y CI", "plain")
    bx(f, 238, y + 40, 190, 56, "Aplicación GitLab", "plain")
    bx(f, 448, y + 40, 190, 56, "Base de datos PostgreSQL", "coral")
    bx(f, 28, y + 160, 190, 66, "Servidores NFS: repositorios y wikis", "teal")
    bx(f, 238, y + 160, 190, 66, "Staging: copia diaria de la base", "gold")
    bx(f, 448, y + 160, 190, 66, "Copias pg_dump en Amazon S3", "coral")
    f.arrow([(218, y + 68), (238, y + 68)])
    f.arrow([(428, y + 68), (448, y + 68)])
    f.arrow([(270, y + 96), (270, y + 128), (123, y + 128), (123, y + 160)])
    f.arrow([(500, y + 96), (500, y + 128), (333, y + 128), (333, y + 160)], dashed=True)
    f.arrow([(590, y + 96), (590, y + 160)], dashed=True)
    bx(f, 680, y + 8, 250, 100, "Enterprise, GitHost y autoalojados: no se vieron afectados", "teal", dashed=True)
    bx(f, 680, y + 140, 250, 100, "Equipo de GitLab: usa GitLab.com para desarrollar GitLab", "gold")
    return done(f, y + 270, "Las flechas punteadas son copias de respaldo. La partición entre base de datos (afectada) y repositorios (a salvo) acotó el daño. Panorama de enero de 2017; sin cifras de usuarios porque el postmortem no las da.")


# ------------------------------------------------------------------ 7. arquitectura de datos
def arquitectura_de_datos() -> Fig:
    f, y = sketch("Arquitectura de datos y respaldos: cuatro caminos de recuperación y el estado de cada uno",
                  "Diagrama de contenedores. La aplicación escribe en la base primaria db1, que replica por streaming a db2. Una instantánea LVM diaria a las 01:00 UTC alimenta el entorno de staging. Un servidor de aplicación ejecuta pg_dump y sube a Amazon S3, que estaba vacío. Los servidores NFS tienen instantáneas de Azure; las bases de datos no.")
    bx(f, 360, y + 4, 220, 50, "Aplicación GitLab", "plain")
    bx(f, 250, y + 110, 200, 60, "db1: base primaria", "coral", bold=True)
    bx(f, 500, y + 110, 200, 60, "db2: secundaria en espera", "gold")
    f.arrow([(450, y + 140), (500, y + 140)], "WAL", label_at=(475, y + 130))
    f.arrow([(420, y + 54), (420, y + 82), (350, y + 82), (350, y + 110)])
    bx(f, 10, y + 110, 200, 60, "NFS: repositorios y wikis", "teal")
    f.arrow([(360, y + 29), (110, y + 29), (110, y + 110)])
    bx(f, 10, y + 210, 200, 56, "Instantánea de Azure cada 24 h", "teal", dashed=True)
    f.arrow([(110, y + 170), (110, y + 210)], dashed=True)
    bx(f, 730, y + 110, 200, 70, "Servidor de aplicación: pg_dump 9.2 cada 24 h", "gold")
    bx(f, 730, y + 220, 200, 56, "Amazon S3: vacío", "coral", bold=True)
    f.arrow([(830, y + 180), (830, y + 220)], dashed=True)
    bx(f, 250, y + 220, 200, 66, "Staging: discos de Azure sin almacenamiento premium", "gold")
    f.arrow([(350, y + 170), (350, y + 220)], "LVM 01:00 UTC", label_at=(362, y + 200), label_anchor="start", dashed=True)
    bx(f, 500, y + 220, 200, 66, "Bases de datos: sin instantáneas de Azure", "coral")
    return done(f, y + 306, "Las flechas continuas son flujos de datos y las punteadas, copias de respaldo. De cuatro caminos de recuperación solo la instantánea LVM resultó utilizable, aunque no estaba pensada para desastres.")


# ------------------------------------------------------------------ 8. replicación y WAL
def replicacion_y_wal() -> Fig:
    f, y = sketch("Replicación y WAL: el camino normal y el que tomó la noche del 31 de enero",
                  "Dos filas de cajas. Camino normal: db1 escribe segmentos de WAL, db2 los lee por streaming y la réplica queda al día. Camino de la noche del 31: la carga sube, db2 se atrasa, db1 recicla los segmentos que db2 necesitaba, sin archivado de WAL no se pueden recuperar, la réplica debe reconstruirse vaciando su directorio y pg_basebackup espera en silencio.")
    f.text(14, y + 18, "Funcionamiento normal", 14, "start", 700, "#0b3f45")
    for i, (t, k) in enumerate((("db1 escribe cada cambio en segmentos de WAL", "teal"), ("db2 lee los segmentos por streaming", "teal"), ("La réplica queda al día y sirve para conmutar", "teal"))):
        x = 10 + i * 316
        bx(f, x, y + 30, 296, 60, t, k)
        if i:
            f.arrow([(x - 20, y + 60), (x, y + 60)])
    f.text(14, y + 126, "Noche del 31 de enero", 14, "start", 700, "#5c1f14")
    fila = (("La carga sube y db2 se atrasa", "gold"), ("db1 recicla segmentos que db2 aún necesitaba", "coral"), ("Sin archivado de WAL: no se pueden recuperar", "coral"))
    for i, (t, k) in enumerate(fila):
        x = 10 + i * 316
        bx(f, x, y + 138, 296, 60, t, k)
        if i:
            f.arrow([(x - 20, y + 168), (x, y + 168)])
    f.arrow([(778, y + 198), (778, y + 228)])
    bx(f, 632, y + 228, 296, 60, "Reconstrucción: vaciar el directorio de db2 y correr pg_basebackup", "coral")
    f.arrow([(632, y + 258), (606, y + 258)])
    bx(f, 316, y + 228, 290, 60, "La herramienta espera en silencio a que db1 envíe datos", "gold")
    f.arrow([(316, y + 258), (290, y + 258)])
    bx(f, 10, y + 228, 280, 60, "Parece un fallo: se repite el vaciado, esta vez en db1", "coral", bold=True)
    return done(f, y + 310, "La caja «sin archivado de WAL» convierte un atraso en una reconstrucción. El silencio de la herramienta es normal según el postmortem y no figuraba en los runbooks ni en la documentación oficial.")


# ------------------------------------------------------------------ 9. secuencia de la noche
def secuencia_de_la_noche() -> Fig:
    f, y = sketch("Secuencia de la noche: de la réplica caída al directorio equivocado",
                  "Diagrama de secuencia con cuatro líneas de vida: ingenieros, db2, pg_basebackup y db1. A las 23:00 falla la réplica; se vacía el directorio de db2; pg_basebackup se cuelga; se sube max_wal_senders de 3 a 32; PostgreSQL no reinicia por semáforos y se baja max_connections de 8000 a 2000; strace no ayuda; hacia las 23:30 se vacía por error el directorio de datos de db1 y se eliminan unos 300 GB.")
    xs = [100, 330, 570, 830]
    names = ["Ingenieros", "db2: secundaria", "pg_basebackup", "db1: primaria"]
    for x, n in zip(xs, names):
        bx(f, x - 95, y, 190, 44, n, "navy", 13, bold=True)
        f.line(x, y + 44, x, y + 700, "#8a9aa3", dashed=True)
    def msg(yy, a, b, text, color="#32505f", dashed=False):
        f.arrow([(xs[a], y + yy), (xs[b], y + yy)], color=color, dashed=dashed)
        f.text((xs[a] + xs[b]) / 2, y + yy - 10, text, 13, "middle", 400)
    msg(92, 0, 1, "23:00 la réplica falla: WAL reciclado")
    msg(142, 0, 1, "vacían el directorio de db2")
    msg(192, 0, 2, "lanzan pg_basebackup")
    msg(242, 2, 3, "espera datos de replicación", dashed=True)
    msg(292, 0, 3, "max_wal_senders de 3 a 32")
    bx(f, xs[3] - 100, y + 312, 200, 66, "no reinicia: demasiados semáforos con 8000 conexiones", "gold", 13)
    msg(404, 0, 3, "max_connections de 8000 a 2000")
    msg(454, 0, 2, "strace: se queda en una llamada poll")
    msg(514, 0, 3, "≈23:30 vacían el directorio creyendo estar en db2", "#c0432f")
    bx(f, xs[3] - 100, y + 540, 200, 80, "≈300 GB eliminados; se interrumpe a 1 o 2 segundos", "coral", 13)
    bx(f, xs[1] - 100, y + 560, 200, 66, "ya vacía: no sirve para recuperar", "coral", 13)
    return done(f, y + 650, "Entre las dos vaciadas hay diagnóstico razonable que no explicaba el silencio de la herramienta. Los intervalos no son escalas de tiempo: el postmortem solo da las 23:00 y las 23:30.")


# ------------------------------------------------------------------ 10. datos perdidos y conservados
def datos_perdidos_y_conservados() -> Fig:
    return timeline(
        "Qué se perdió y qué se conservó, según dónde vivía el dato",
        "Cuatro carriles en horas desde las 16:00 UTC del 31 de enero. Los datos de la base anteriores a las 17:20 se restauran de la instantánea; los creados entre las 17:20 y las 23:30 se pierden; los repositorios Git y las wikis en NFS se conservan; los proyectos creados en la ventana se reconstruyen desde sus repositorios sin incidencias ni solicitudes de fusión.",
        [
            ("Base: anterior a las 17:20", [(0, 1.33, "ok", "teal")]),
            ("Base: de 17:20 a 23:30", [(1.33, 7.5, "perdido", "coral")]),
            ("Repositorios y wikis (NFS)", [(0, 8, "conservados", "teal")]),
            ("Proyectos creados en la ventana", [(1.33, 7.5, "reconstruidos sin incidencias", "gold")]),
        ],
        unit="horas desde las 16:00 UTC del 31 de enero de 2017",
        events=[(1.33, "17:20"), (7.5, "23:30")],
        t_max=8, ticks=[0, 1, 2, 3, 4, 5, 6, 7, 8], lane_h=50, label_w=260,
        note="La pérdida es de metadatos de colaboración (proyectos, incidencias, comentarios, cuentas), no de código. El cierre de la ventana aparece como 23:30 y como 00:00 en dos lugares del mismo postmortem; aquí se usa 23:30.",
        foot="Fuente: postmortem público de GitLab (10 feb 2017). Cantidades estimadas por la empresa: al menos 5.000 proyectos, 5.000 comentarios y unas 700 cuentas.")


# ------------------------------------------------------------------ 11. cadena del respaldo vacío
def cadena_del_respaldo_vacio() -> Fig:
    f, y = sketch("Cadena del respaldo vacío: ocho pasos razonables que dejaron el depósito de S3 sin nada",
                  "Dos filas de cuatro cajas. pg_dump se ejecuta en un servidor de aplicación; el paquete Omnibus elige la versión por el directorio de datos, que allí no existe, y usa PostgreSQL 9.2; la base corre 9.6; pg_dump termina con error; el aviso se envía por correo; el servidor receptor lo rechaza porque no está firmado con DMARC; nadie se entera; el depósito de S3 está vacío.")
    row1 = (("1 pg_dump corre en un servidor de aplicación", "teal"), ("2 Omnibus elige la versión por el directorio de datos; allí no existe", "teal"),
            ("3 Usa PostgreSQL 9.2 mientras la base corre 9.6", "gold"), ("4 pg_dump termina con error", "coral"))
    row2 = (("5 El aviso del error se envía por correo", "gold"), ("6 El receptor lo rechaza: el correo no estaba firmado con DMARC", "coral"),
            ("7 Nadie sabe que el respaldo falla", "coral"), ("8 El depósito de S3 está vacío el 31 de enero", "coral"))
    w, g = 214, 21
    for i, (t, k) in enumerate(row1):
        x = 10 + i * (w + g)
        bx(f, x, y + 10, w, 82, t, k)
        if i:
            f.arrow([(x - g, y + 51), (x, y + 51)])
    f.arrow([(10 + 3 * (w + g) + w / 2, y + 92), (10 + 3 * (w + g) + w / 2, y + 120), (10 + w / 2, y + 120), (10 + w / 2, y + 148)])
    for i, (t, k) in enumerate(row2):
        x = 10 + i * (w + g)
        bx(f, x, y + 148, w, 82, t, k)
        if i:
            f.arrow([(x - g, y + 189), (x, y + 189)])
    return done(f, y + 250, "Los pasos 1 a 3 son decisiones locales razonables; los pasos 4 a 6 son los puntos donde el sistema pudo quejarse. El proceso era automático y no tenía otro medio de reportar errores, según el postmortem.")


# ------------------------------------------------------------------ 12. defensa en profundidad
def defensa_en_profundidad() -> Fig:
    f, y = sketch("Doce capas de control: diez no cumplieron su función el 31 de enero",
                  "Doce controles en tres filas: detección de abuso, archivado de WAL, réplica, procedimiento de resincronización, distinción visual de servidores, respaldo lógico, avisos por correo, instantáneas de Azure en bases de datos, instantánea LVM diaria, instantánea LVM manual, pruebas periódicas de restauración y propiedad de la durabilidad. Cada uno indica qué hizo el 31 de enero según el postmortem.")
    cells = [
        ("1 Detección de abuso", "Programó la eliminación de una cuenta legítima", "coral"),
        ("2 Archivado de WAL", "No existía", "coral"),
        ("3 Réplica db2", "Se atrasó y se vació; no era un respaldo", "coral"),
        ("4 Resincronización", "Manual, sin automatizar ni documentar bien", "coral"),
        ("5 Distinguir servidores", "El intérprete no mostraba servidor y entorno", "coral"),
        ("6 Respaldo pg_dump", "Falló en silencio: 9.2 frente a 9.6", "coral"),
        ("7 Avisos por correo", "Rechazados por falta de DMARC", "coral"),
        ("8 Azure en bases", "No estaban habilitadas", "coral"),
        ("9 LVM diaria", "Existía; de casi 24 horas atrás", "gold"),
        ("10 LVM manual", "De las 17:20; la única fuente útil", "teal"),
        ("11 Pruebas de restauración", "No se hacían con regularidad", "coral"),
        ("12 Propiedad", "Nadie era responsable de las pruebas", "coral"),
    ]
    w, g = 224, 12
    for i, (t, r, k) in enumerate(cells):
        row, col = divmod(i, 4)
        x = 10 + col * (w + g)
        yy = y + 8 + row * 150
        bx(f, x, yy, w, 44, t, "plain", 13, bold=True)
        bx(f, x, yy + 48, w, 80, r, k, 13)
    return done(f, y + 8 + 3 * 150, "Coral: no cumplió su función. Dorado: cumplió de forma parcial. Teal: sirvió. Diez de doce fallaron y varias comparten una misma suposición («otro mecanismo respaldará»), lectura de este programa.")


# ------------------------------------------------------------------ 13. arquitectura posterior
def arquitectura_despues() -> Fig:
    f, y = sketch("Arquitectura posterior: más caminos de recuperación, cada uno vigilado y con un responsable",
                  "Tres niveles. Arriba, la primaria con varias réplicas. En medio, cinco caminos de recuperación: archivado de WAL con recuperación a un punto en el tiempo, instantáneas LVM horarias, instantáneas de Azure de las bases, respaldo lógico supervisado y un entorno de restauración rápido. Abajo, pruebas automáticas de restauración que alimentan un panel, y un responsable de la durabilidad; propuestas propias: confirmación con el nombre del host, alertas por ausencia y objetivos de punto y tiempo de recuperación escritos.")
    bx(f, 10, y + 6, 300, 56, "Primaria con varias réplicas y balanceo (#259, #1101)", "teal")
    bx(f, 340, y + 6, 280, 56, "Confirmación con el nombre del host antes de vaciar un directorio", "gold")
    bx(f, 650, y + 6, 280, 56, "RPO y RTO escritos y verificados", "gold")
    paths = ["Archivado de WAL y recuperación a un punto en el tiempo", "Instantáneas LVM cada hora (#1098)", "Instantáneas de Azure de las bases (#1099)",
             "Respaldo lógico con versión correcta y monitoreo (#1095)", "Entorno de restauración rápido (#1100)"]
    for i, t in enumerate(paths):
        bx(f, 10 + i * 186, y + 110, 174, 84, t, "teal", 13)
        f.arrow([(97 + i * 186, y + 62), (97 + i * 186, y + 110)], dashed=True)
    bx(f, 10, y + 250, 300, 64, "Pruebas automáticas de restauración (#1102)", "teal")
    bx(f, 340, y + 250, 280, 64, "Panel de estado y edad de los respaldos; alerta por ausencia", "gold")
    bx(f, 650, y + 250, 280, 64, "Responsable de la durabilidad de los datos", "teal", bold=True)
    f.arrow([(310, y + 282), (340, y + 282)])
    f.arrow([(650, y + 282), (620, y + 282)], dashed=True)
    f.arrow([(470, y + 250), (470, y + 194), (560, y + 194)], dashed=True)
    return done(f, y + 334, "Teal: compromisos publicados en el postmortem (con el número de incidencia que da GitLab). Dorado: propuestas de este programa. Es un objetivo de diseño; el postmortem no dice qué se implantó ni cuándo.")


# ------------------------------------------------------------------ 14. restauración paso a paso
def restauracion_paso_a_paso() -> Fig:
    f, y = sketch("Restauración paso a paso: casi todo el tiempo se fue en una sola copia",
                  "Dos filas de cajas con los pasos de la restauración: elegir la instantánea de las 17:20; copiar el directorio de datos de staging a producción durante unas 18 horas a unos 60 Mbps; copiar en paralelo la instantánea que quizá conserva los webhooks; producción restaurada sin webhooks el 1 de febrero a las 17:00 UTC; reconstruir los webhooks desde una base de apoyo; sumar 100.000 a las secuencias; reactivar gradualmente hacia las 18:00 UTC.")
    row1 = (("1 Elegir la instantánea de las 17:20: unas 6 horas de datos perdidos y no casi 24", "teal"),
            ("2 Copiar el directorio de datos de staging a producción: unas 18 horas a unos 60 Mbps", "coral"),
            ("3 En paralelo, copiar la instantánea que quizá aún tiene los webhooks", "gold"),
            ("4 Producción restaurada sin webhooks: 17:00 UTC del 1 de febrero", "teal"))
    row2 = (("5 Base de apoyo: volcar la tabla de webhooks e importarla", "gold"), ("6 Sumar 100.000 a las secuencias para no reutilizar identificadores", "gold"),
            ("7 Reactivar GitLab.com de forma gradual: hacia las 18:00 UTC", "teal"))
    w, g = 214, 21
    for i, (t, k) in enumerate(row1):
        x = 10 + i * (w + g)
        bx(f, x, y + 10, w, 100, t, k)
        if i:
            f.arrow([(x - g, y + 60), (x, y + 60)])
    f.arrow([(10 + 3 * (w + g) + w / 2, y + 110), (10 + 3 * (w + g) + w / 2, y + 140), (10 + w / 2, y + 140), (10 + w / 2, y + 170)])
    for i, (t, k) in enumerate(row2):
        x = 10 + i * (w + g)
        bx(f, x, y + 170, w, 90, t, k)
        if i:
            f.arrow([(x - g, y + 215), (x, y + 215)])
    bx(f, 10 + 3 * (w + g), y + 170, w, 90, "Servicio restablecido tras unas 18 horas", "navy", 13, bold=True)
    f.arrow([(10 + 2 * (w + g) + w, y + 215), (10 + 3 * (w + g), y + 215)])
    return done(f, y + 280, "La caja coral concentra el tiempo; las doradas existen porque la restauración vino de una copia anterior. El postmortem no desglosa el tiempo de los pasos que no son la copia.")


# ------------------------------------------------------------------ 15. árbol de fallas
def arbol_de_fallas() -> Fig:
    f, y = sketch("Árbol de fallas: pérdida de datos y 18 horas de caída exigen tres condiciones a la vez",
                  "Árbol de fallas con compuerta Y. Evento superior: pérdida de datos con unas 18 horas de caída. Ramas: una acción destructiva en producción, ausencia de un respaldo reciente utilizable y una restauración lenta. Cada rama tiene hojas documentadas en el postmortem.")
    bx(f, 290, y + 4, 360, 56, "Pérdida de datos y unas 18 horas de caída", "navy", 14, bold=True)
    f.line(470, y + 60, 470, y + 84)
    f.dot(470, y + 96, "Y")
    f.line(155, y + 112, 785, y + 112)
    for x in (155, 470, 785):
        f.line(x, y + 112, x, y + 130)
    bx(f, 10, y + 130, 290, 60, "Acción destructiva en producción", "plain", bold=True)
    bx(f, 325, y + 130, 290, 60, "Sin respaldo reciente utilizable", "plain", bold=True)
    bx(f, 640, y + 130, 290, 60, "Restauración lenta", "plain", bold=True)
    for x in (155, 470, 785):
        f.line(x, y + 190, x, y + 206)
        f.dot(x, y + 218, "Y")
    leaves = [
        (10, [("Carga alta y réplica rota (documentado)", "coral"), ("Resincronización manual y mal documentada (documentado)", "coral"), ("Servidores indistinguibles en el intérprete (documentado)", "coral")]),
        (325, [("pg_dump vacío por versión y por DMARC (documentado)", "coral"), ("Sin instantáneas de Azure en bases (documentado)", "coral"), ("Réplica vaciada (documentado)", "coral"), ("Solo la instantánea de hace unas 6 horas (documentado)", "coral")]),
        (640, [("Staging con discos lentos como única fuente (documentado)", "coral"), ("Sin restauración automatizada ni probada (documentado)", "coral"), ("Sin propiedad de las pruebas (documentado)", "coral")]),
    ]
    for x, items in leaves:
        cy = y + 244
        f.line(x + 145, y + 230, x + 145, y + 244)
        for t, k in items:
            bx(f, x, cy, 290, 58, t, k)
            cy += 70
    return done(f, y + 244 + 70 * 4 + 6, "Eliminar una de las tres ramas evita el evento superior. La acción destructiva fue el detonante, pero las otras dos ramas determinaron el daño. Sin probabilidades: el postmortem no las da.")


# ------------------------------------------------------------------ 16. cinco porqués
def cinco_porques() -> Fig:
    f, y = sketch("Dos cadenas de cinco porqués: la técnica del postmortem, dibujada",
                  "Dos columnas. La primera responde por qué GitLab.com estuvo caído unas 18 horas: se borró el directorio de la primaria, la réplica debía reconstruirse a mano, la replicación se detuvo, subió la carga y una cuenta se programó para eliminación. La segunda responde por qué la restauración tomó más de 18 horas: se usó staging, faltaban instantáneas y respaldo lógico, el respaldo falló en silencio y nadie era responsable de probarlo.")
    bx(f, 10, y + 4, 450, 44, "Problema 1: GitLab.com estuvo caído unas 18 horas", "navy", 13, bold=True)
    bx(f, 480, y + 4, 450, 44, "Problema 2: restaurar tomó más de 18 horas", "navy", 13, bold=True)
    c1 = [("1 Se borró el directorio de la primaria en vez del de la réplica", "coral"), ("2 La réplica debía reconstruirse a mano, sin automatizar ni documentar bien", "gold"),
          ("3 La replicación se detuvo: la primaria reciclaba WAL antes de que la réplica lo leyera", "gold"), ("4 La carga subió por más spam y un trabajo de borrado de una cuenta", "gold"),
          ("5 Un reporte de abuso programó la eliminación; el sistema hace fácil pasar por alto los detalles", "teal")]
    c2 = [("1 Hubo que restaurar desde staging, en discos lentos de otra región", "coral"), ("2 Faltaban instantáneas de Azure y el respaldo lógico no funcionaba", "gold"),
          ("3 El respaldo lógico falló en silencio: 9.2 frente a 9.6 y avisos rechazados", "gold"), ("4 El procedimiento de respaldo no se probaba con regularidad", "gold"),
          ("5 Nadie era responsable de probarlo: no había propiedad", "teal")]
    for col, items in ((10, c1), (480, c2)):
        cy = y + 68
        for i, (t, k) in enumerate(items):
            bx(f, col, cy, 450, 70, t, k)
            if i < 4:
                f.arrow([(col + 225, cy + 70), (col + 225, cy + 90)])
            cy += 90
    return done(f, y + 68 + 90 * 5, "Cada caja responde «¿por qué?» a la anterior. La última caja de cada cadena es la raíz: una técnica (un reporte de abuso) y una organizativa (la falta de propiedad). Respeta el texto del postmortem.")


# ------------------------------------------------------------------ 17. comparables
def comparables() -> Fig:
    return grouped_bars(
        "Tres incidentes de operación: de unas 4 horas a hasta 14 días",
        "Barras horizontales en horas con eje logarítmico. Amazon S3 en 2017: unas 4,3 horas de afectación. GitLab.com en 2017: unas 18 horas de indisponibilidad. Atlassian en 2022: hasta 336 horas de recuperación para algunos clientes.",
        ["AWS S3, 28 feb 2017", "GitLab.com, 31 ene 2017", "Atlassian, abril de 2022"],
        [("Horas", [4.3, 18, 336], "navy")],
        unit="horas (aproximadas)", horizontal=True, log=True, label_w=250, ticks=[1, 10, 100, 1000],
        note="Las tres duraciones miden cosas distintas: afectación de un servicio, indisponibilidad del servicio y recuperación de los casos peores. Las 4,3 horas son cálculo propio entre las 9:37 y las 13:54 (hora del Pacífico); las 336, 14 días de la fuente.",
        foot="Fuentes: AWS (28 feb 2017), postmortem de GitLab (10 feb 2017) y Atlassian (abril de 2022).")

# ==== EXPANDED FIGURES (end) ====

FIGURES = {
    "gitlab-2017-capas-de-recuperacion.svg": capas_de_recuperacion,
    "gitlab-2017-cadena-de-causas.svg": cadena_de_causas,
    "gitlab-2017-linea-de-tiempo.svg": linea_de_tiempo,
    "gitlab-2017-horas-en-juego.svg": horas,
    "gitlab-2017-antes-y-despues.svg": antes_y_despues,
    # expanded entries
    "gitlab-2017-ecosistema.svg": ecosistema,
    "gitlab-2017-arquitectura-de-datos.svg": arquitectura_de_datos,
    "gitlab-2017-replicacion-y-wal.svg": replicacion_y_wal,
    "gitlab-2017-secuencia-de-la-noche.svg": secuencia_de_la_noche,
    "gitlab-2017-datos-perdidos-y-conservados.svg": datos_perdidos_y_conservados,
    "gitlab-2017-cadena-del-respaldo-vacio.svg": cadena_del_respaldo_vacio,
    "gitlab-2017-defensa-en-profundidad.svg": defensa_en_profundidad,
    "gitlab-2017-arquitectura-despues.svg": arquitectura_despues,
    "gitlab-2017-restauracion-paso-a-paso.svg": restauracion_paso_a_paso,
    "gitlab-2017-arbol-de-fallas.svg": arbol_de_fallas,
    "gitlab-2017-cinco-porques.svg": cinco_porques,
    "gitlab-2017-comparables.svg": comparables,
}
