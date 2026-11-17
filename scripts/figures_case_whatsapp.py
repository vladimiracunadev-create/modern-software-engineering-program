"""Figures for the WhatsApp success case (casos/exito/whatsapp.md).

Numbers come from public sources cited in the case page: the 2012 Erlang Factory talk by
Rick Reed, WhatsApp's own blog and security white paper, and Meta's engineering blog.
Diagrams mark what is documented and what is inferred.
"""
from __future__ import annotations

import re

from figure_kit import Fig, _wrap, grouped_bars, timeline

from case_diagrams import B, G, finish, lane_steps, legend, sequence
from figure_kit import stacked_bars
DOC = "Fuente: documentos públicos de WhatsApp y Meta citados en la página del caso. Consulta: 16 de noviembre de 2026."
INF = "Esquema pedagógico: las cajas punteadas son inferencia del curso, no arquitectura confirmada por WhatsApp."


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
    f = _canvas("Una cuenta, un número de teléfono y mensajes cifrados de extremo a extremo",
                "Diagrama de contexto: dos personas con la aplicación en el teléfono intercambian mensajes cifrados a través de los servidores de WhatsApp, que no ven el contenido; las empresas hablan con los clientes por la misma red mediante la API de empresas; Meta aloja la infraestructura y los dispositivos vinculados se añaden al teléfono principal.",
                940, 0)
    f.group(10, 52, 250, 200, "Persona A", "grey")
    f.box(30, 90, 210, 62, "Teléfono con la app: cuenta ligada a un número", "plain", 13)
    f.box(30, 166, 210, 66, "Hasta cuatro dispositivos vinculados sin teléfono", "teal", 13)
    f.group(690, 52, 240, 200, "Persona B o grupo", "grey")
    f.box(710, 90, 200, 62, "Teléfono con la app", "plain", 13)
    f.box(710, 166, 200, 66, "Empresa que atiende clientes por la API", "gold", 13)
    f.group(300, 52, 350, 200, "Servidores (infraestructura de Meta)", "navy")
    f.box(320, 90, 310, 62, "Conexión persistente, cola de mensajes y directorio de claves públicas", "plain", 13)
    f.box(320, 166, 310, 66, "Almacén de adjuntos cifrados: el emisor sube el archivo y envía la clave en el mensaje", "plain", 13)
    f.arrow([(240, 121), (320, 121)])
    f.arrow([(630, 121), (710, 121)])
    f.text(280, 108, "cifrado", 13, "middle", 700, "#142231", halo=True)
    f.text(670, 108, "cifrado", 13, "middle", 700, "#142231", halo=True)
    return _foot(f, 270, "Lo documentado: el cifrado de extremo a extremo con el protocolo Signal es el valor por defecto desde abril de 2016, los servidores guardan claves públicas y no el contenido, y desde 2021 hay dispositivos vinculados que funcionan sin el teléfono. Los adjuntos grandes se cifran en el dispositivo y se suben a un almacén de blobs; la clave viaja dentro del mensaje cifrado (libro blanco).",
                 DOC)


def componentes() -> Fig:
    f = _canvas("Piezas que el equipo de WhatsApp describió para sostener millones de conexiones",
                "Pila de cuatro capas: aplicación cliente, servidores Erlang sobre FreeBSD con una conexión por usuario, partición del trabajo entre procesos y herramientas de medición de contención; cada capa lleva una cifra o ajuste concreto publicados en la charla de 2012.",
                940, 0)
    rows = [
        ("Cliente", "Aplicación en el teléfono con claves propias y sesiones Signal; desde 2021 también dispositivos vinculados", "teal"),
        ("Servidor", "Máquina estándar de 24 CPU lógicas y 100 GB de RAM; FreeBSD 8.3 y OTP R14B03; objetivo de un millón de conexiones", "plain"),
        ("Erlang/BEAM", "Procesos ligeros por conexión; parches a la máquina virtual para quitar contención de cerrojos", "plain"),
        ("Medición", "Contadores de cerrojos, métricas de colas, cargas sintéticas, cargas duplicadas y desviadas desde producción", "coral"),
    ]
    y = 52.0
    for name, text, kind in rows:
        f.box(10, y, 170, 64, name, "navy", 14, bold=True)
        f.box(192, y, 738, 64, text, kind, 13)
        y += 80
    return _foot(f, y + 6, "Las capas se leen de la charla de Rick Reed (marzo de 2012) y del blog de la empresa de enero de 2012. Que esa pila siga igual hoy no está documentado: en 2014 WhatsApp se unió a Facebook y la infraestructura puede haber cambiado.",
                 DOC)


def flujo() -> Fig:
    f = _canvas("Enviar un mensaje a alguien que no tiene conexión: cifrado, cola y entrega",
                "Diagrama de flujo en seis pasos: el emisor obtiene las claves públicas del receptor, cifra el mensaje en su dispositivo, lo envía al servidor, el servidor lo guarda en cola porque el receptor no está conectado, el receptor se conecta y lo recibe, y lo descifra con sus claves privadas; el servidor nunca tiene la clave del mensaje.",
                940, 0)
    steps = [
        ("1. Claves", "El emisor pide las claves públicas del receptor al servidor", "plain", False),
        ("2. Cifrar", "Deriva claves de sesión y cifra en su teléfono", "teal", False),
        ("3. Enviar", "El mensaje cifrado viaja por la conexión persistente", "plain", False),
        ("4. Cola", "El servidor lo retiene hasta que el receptor se conecte", "gold", True),
        ("5. Entregar", "El receptor se conecta y recibe el mensaje", "plain", True),
        ("6. Descifrar", "Lo abre con sus claves privadas; solo él puede", "teal", False),
    ]
    w, gap = 134, 22
    x = 10.0
    for i, (head, body, kind, inferred) in enumerate(steps):
        f.box(x, 66, w, 38, head, kind, 13, bold=True)
        f.box(x, 112, w, 118, body, "plain", 13, dashed=inferred)
        if i:
            f.arrow([(x - gap, 85), (x, 85)])
        x += w + gap
    f.text(14, 262, "Trazo continuo: respaldado por la documentación citada. Trazo punteado: inferido.", 13, "start", 400, "#32505f")
    return _foot(f, 280, "La documentación pública cubre las claves (identidad, prellave firmada y prellaves de un solo uso), el uso de Signal y que los servidores no tienen acceso al texto. El almacenamiento temporal en cola y su plazo, y los acuses de entrega, se infieren del comportamiento visible del servicio: no se publican plazos ni formatos.",
                 INF, "coral")


def linea() -> Fig:
    return _years(timeline(
        "De dos fundadores a más de tres mil millones de personas (2009-2025)",
        "Línea de tiempo con dos carriles: en producto, WhatsApp es independiente de 2009 a 2014 y forma parte de Facebook, hoy Meta, desde 2014; en seguridad y arquitectura, el cifrado completo llega en 2016 y el soporte de varios dispositivos en 2021. Hitos: dos millones de conexiones por servidor en 2012, compra anunciada el 19 de febrero de 2014 y dos mil millones de usuarios el 12 de febrero de 2020.",
        [("Propiedad", [(2009, 2014, "Independiente", "teal"), (2014, 2026, "Dentro de Facebook y Meta", "navy")]),
         ("Plataforma", [(2012, 2016, "Escala de conexiones", "gold"), (2016, 2021, "Cifrado total", "coral"), (2021, 2026, "Varios dispositivos", "grey")])],
        unit="Año", events=[(2012, "2M conexiones"), (2014, "Compra"), (2020, "2 000 M")],
        ticks=[2009, 2012, 2015, 2018, 2021, 2024, 2026], t_max=2026, lane_h=58, label_w=110,
        note="Los carriles son etapas, no fases excluyentes: la escala de conexiones se siguió trabajando después de 2016. Los años proceden de la propia WhatsApp y de Meta; los límites de cada barra son aproximaciones visuales. El año 2009 lo citan fuentes secundarias; ninguna fuente primaria consultada lo confirma, así que debe leerse como dato no verificado.",
        note_kind="gold", foot=DOC))


def conexiones() -> Fig:
    return grouped_bars(
        "Conexiones simultáneas por servidor en la charla de Rick Reed (2012)",
        "Barras con cuatro valores: unas 200 mil conexiones por servidor al inicio, el primer cuello de botella apareció cerca de 425 mil, tras la primera ronda de correcciones se llegó a un millón y un mes después a dos millones, un aumento de diez veces sobre el punto de partida.",
        ["Carga inicial", "Primer cuello de botella", "Primera ronda de correcciones", "Un mes después"],
        [("Conexiones por servidor (miles)", [200, 425, 1000, 2000], "teal")],
        unit="Miles de conexiones por servidor", decimals=0, ticks=[0, 500, 1000, 1500, 2000],
        note="La mejora no vino de máquinas mayores sino de quitar contención: según la charla, de 200 mil a 2 millones todo fueron correcciones de contención, algunas en la máquina virtual de Erlang y otras en el reparto del trabajo. Los valores son los de la presentación; el segundo es «alrededor de» 425 mil y el tercero «un millón». No se sabe cuántas conexiones sostiene hoy un servidor.",
        note_kind="gold", foot="Fuente: R. Reed, «Scaling to Millions of Simultaneous Connections», Erlang Factory SF, 30 de marzo de 2012.")


FIN = "Fuente: Facebook, Form 10-K de 2014 y Meta, Form 10-K de 2025 (SEC); anuncio de Facebook del 19 de febrero de 2014. Consulta: 16 de noviembre de 2026."


def actores() -> Fig:
    f = _canvas("Quién da qué a quién: los actores del ecosistema de WhatsApp",
                "Diagrama de incentivos: la persona usa gratis un servicio cifrado; la empresa pequeña usa la aplicación Business; la empresa grande y el desarrollador usan la Cloud API de Meta y pagan por mensajes; Meta aloja y opera; las tiendas de aplicaciones distribuyen; los reguladores fijan reglas.",
                940, 0)
    B(f, 340, 150, 260, 100, "WhatsApp dentro de Meta: opera los servidores de conexión, claves y mensajes pendientes", "navy", 13, bold=True)
    B(f, 10, 56, 250, 70, "Persona: manda mensajes y llamadas gratis, con cifrado por defecto", "teal")
    B(f, 345, 56, 250, 70, "Grupo y comunidad: varias personas comparten un mismo canal", "plain")
    B(f, 680, 56, 250, 70, "Empresa pequeña: atiende clientes con la aplicación Business", "plain")
    B(f, 10, 300, 250, 70, "Tiendas de aplicaciones y fabricantes: distribuyen e instalan el cliente", "plain", dashed=True)
    B(f, 345, 300, 250, 70, "Reguladores y fuerzas de seguridad: reglas de datos, competencia y contenido", "grey", dashed=True)
    B(f, 680, 300, 250, 70, "Empresa grande y desarrollador: usan la Cloud API de Meta y pagan por mensajes", "gold")
    f.arrow([(200, 126), (340, 180)])
    f.arrow([(470, 126), (470, 150)])
    f.arrow([(750, 126), (600, 180)])
    f.arrow([(340, 232), (230, 300)], dashed=True)
    f.arrow([(470, 250), (470, 300)], dashed=True)
    f.arrow([(600, 232), (700, 300)], "pago por mensajes", label_at=(690, 262))
    return finish(f, 390, "Documentado: gratuidad para personas, Business y Cloud API, y que Meta incluye en «otros ingresos» el pago por mensajería de WhatsApp. Inferido: el papel de las tiendas, los fabricantes y los reguladores; las flechas punteadas indican relaciones que existen pero que las fuentes consultadas no detallan.", DOC)


def viajes() -> Fig:
    f = _canvas("Cinco recorridos completos: de la instalación al caso límite",
                "Cinco filas de pasos encadenados: persona nueva, grupo, empresa pequeña con la aplicación Business, empresa grande con Cloud API y persona con varios dispositivos; cada fila termina en su caso límite.",
                940, 0)
    y = 54.0
    y = lane_steps(f, y, "Persona nueva", [("Instala y se registra con su teléfono", "plain"), ("Se publican sus claves públicas", "teal"), ("Primer mensaje: sesión cifrada", "teal"), ("Límite: el contacto no tiene la app", "coral")], h=64)
    y = lane_steps(f, y, "Grupo", [("Crea el grupo y añade miembros", "plain"), ("Clave de remitente a cada miembro", "teal"), ("Un solo cifrado por mensaje", "plain"), ("Límite: sale un miembro; se renueva la clave", "coral")], h=64)
    y = lane_steps(f, y, "Empresa pequeña", [("Instala la app Business", "plain"), ("Atiende desde un dispositivo suyo", "plain"), ("Cifrado de extremo a extremo", "teal"), ("Límite: un solo empleado no basta", "coral!")], h=64)
    y = lane_steps(f, y, "Empresa grande", [("Se integra con la Cloud API", "plain"), ("Meta recibe y entrega mensajes", "gold"), ("Sin cifrado extremo a extremo (definición oficial)", "gold"), ("Límite: aviso al usuario en el chat", "coral")], h=64)
    y = lane_steps(f, y, "Varios dispositivos", [("Vincula con un código QR", "plain"), ("Cada dispositivo, sus claves", "teal"), ("Se cifra una vez por dispositivo", "plain"), ("Límite: se quita un dispositivo y se renuevan claves", "coral")], h=64)
    legend(f, y + 14, "Trazo punteado: dato inferido. Cajas coral: el caso límite de cada recorrido.")
    return finish(f, y + 28, "Cada fila es un tipo de usuario con su propio incentivo. Los pasos salen del libro blanco de cifrado, del artículo sobre varios dispositivos y de la definición oficial de cifrado de extremo a extremo con la Cloud API; el límite de la empresa pequeña es inferido.", DOC)


def contenedores() -> Fig:
    f = _canvas("Nivel 2, contenedores: del teléfono al servidor de chat y a las claves",
                "Diagrama de contenedores: el cliente se conecta con un canal cifrado a un servicio de conexiones llamado ChatD; detrás hay un directorio de claves públicas, colas de mensajes pendientes, un almacén de adjuntos cifrados, la bóveda de claves de respaldo con módulos de seguridad de hardware y la Cloud API de Meta para empresas.",
                940, 0)
    B(f, 10, 70, 190, 70, "Teléfono: fuente de las claves privadas y del historial", "teal")
    B(f, 10, 160, 190, 80, "Hasta cuatro dispositivos vinculados, con claves propias", "teal")
    G(f, 230, 52, 520, 270, "Servidores de WhatsApp (Meta)", "navy")
    B(f, 248, 90, 160, 70, "ChatD: conexiones y autenticación", "plain")
    B(f, 426, 90, 160, 70, "Directorio de claves públicas y prellaves", "plain")
    B(f, 604, 90, 130, 70, "Cola de mensajes pendientes", "plain", dashed=True)
    B(f, 248, 180, 160, 70, "Almacén de adjuntos cifrados", "plain")
    B(f, 426, 180, 160, 70, "Bóveda de claves de respaldo (HSM, varios centros)", "gold")
    B(f, 604, 180, 130, 70, "Telemetría y abuso (no publicado)", "grey", dashed=True)
    B(f, 248, 262, 486, 44, "Canal cifrado entre cliente y servidor con Noise Pipes", "plain")
    G(f, 770, 52, 160, 270, "Empresas", "gold")
    B(f, 782, 90, 136, 100, "Cloud API de Meta: programa mensajes y llamadas", "gold")
    B(f, 782, 206, 136, 90, "Aplicación Business en un dispositivo propio", "plain")
    f.arrow([(200, 105), (248, 120)])
    f.arrow([(200, 195), (248, 140)])
    f.arrow([(408, 125), (426, 125)])
    f.arrow([(586, 125), (604, 125)], dashed=True)
    f.arrow([(750, 140), (782, 140)])
    return finish(f, 342, "Documentado: ChatD como servicio de conexiones y de autenticación, el canal Noise Pipes, la bóveda de claves con módulos de seguridad de hardware en varios centros de datos, los adjuntos en un almacén y la Cloud API como producto de Meta. Inferido: la cola de mensajes pendientes y los detalles de telemetría; no se sabe cuántos servidores ni qué base de datos se usa hoy.", DOC)


def sec_mensaje() -> Fig:
    return sequence(
        "Nivel 4, secuencia: el primer mensaje a alguien que está desconectado",
        "Diagrama de secuencia entre el teléfono emisor, el servidor y el teléfono receptor: el emisor pide las claves públicas del receptor, cifra localmente, envía el texto cifrado, el servidor lo guarda hasta que el receptor se conecte y se lo entrega, y el receptor confirma.",
        ["Teléfono emisor", "Servidor de WhatsApp", "Teléfono receptor"],
        [(0, 1, "Pide claves públicas del receptor", ""), (1, 0, "Identidad, prellave firmada y una de un solo uso", ""),
         (0, 0, "Calcula la clave y cifra el texto", ""), (0, 1, "Envía el texto cifrado", ""),
         (1, 1, "Guarda hasta que conecte (inferido)", "dashed"), (2, 1, "Se conecta y autentica", ""),
         (1, 2, "Entrega el texto cifrado", ""), (2, 2, "Descifra con sus claves privadas", ""),
         (2, 1, "Confirma la recepción (inferido)", "dashed")],
        "Documentado: las tres clases de claves públicas, el acuerdo inicial asíncrono del protocolo Signal, que el servidor no tiene acceso al texto y el canal cifrado de conexión. Inferido: el guardado temporal y las confirmaciones de entrega que muestra la aplicación. No se sabe cuánto tiempo guarda el servidor un mensaje pendiente.",
        DOC, kinds=["teal", "navy", "teal"], row_h=44)


def sec_adjunto() -> Fig:
    return sequence(
        "Nivel 4, secuencia: un adjunto grande y un mensaje a un grupo",
        "Diagrama de secuencia: el emisor cifra el archivo con una clave efímera, lo sube a un almacén de adjuntos, envía al grupo un mensaje cifrado con la clave de remitente que lleva el puntero y las claves del adjunto, y cada miembro descarga y descifra el archivo.",
        ["Emisor", "Servidor y almacén", "Miembro del grupo"],
        [(0, 0, "Cifra el archivo con AES-256 y HMAC", ""), (0, 1, "Sube el archivo cifrado", ""),
         (1, 0, "Devuelve un puntero al archivo", "dashed"), (0, 1, "Mensaje con puntero y claves, cifrado con la clave de remitente", ""),
         (1, 2, "Reparte el mensaje cifrado una sola vez", ""), (2, 2, "Descifra el mensaje con la clave de remitente", ""),
         (2, 1, "Descarga el archivo cifrado", ""), (2, 2, "Descifra y comprueba el MAC", "")],
        "Documentado: cifrado local del adjunto con clave efímera de 32 bytes y verificación con HMAC, almacén de blobs, mensaje con claves y puntero, y la clave de remitente repartida por sesiones individuales para que el mensaje de grupo se cifre una sola vez. Inferido: el momento exacto en que se devuelve el puntero.",
        DOC, kinds=["teal", "navy", "teal"], row_h=44)


def sec_multi() -> Fig:
    return sequence(
        "Nivel 4, secuencia: un mensaje con varios dispositivos (reparto en el cliente)",
        "Diagrama de secuencia: el emisor consulta la lista de dispositivos del receptor, cifra el mensaje por separado para cada dispositivo con su sesión, envía todas las copias cifradas y el servidor las entrega a cada dispositivo; el mensaje no se guarda en el servidor una vez entregado.",
        ["Emisor", "Servidor", "Teléfono del receptor", "Escritorio del receptor"],
        [(0, 1, "Pide la lista de dispositivos del receptor", ""), (1, 0, "Claves de cada dispositivo", ""),
         (0, 0, "Cifra una copia por dispositivo", ""), (0, 1, "Envía las copias cifradas", ""),
         (1, 2, "Copia para el teléfono", ""), (1, 3, "Copia para el escritorio", ""),
         (1, 1, "No conserva el mensaje entregado", "")],
        "Documentado en el artículo de ingeniería de Meta: cada dispositivo tiene su propia clave de identidad, el servidor mantiene el mapa de cuentas a dispositivos, el emisor cifra y transmite una copia por dispositivo («reparto en el cliente») y los mensajes no se guardan en el servidor tras entregarse. El coste: el emisor trabaja N veces para N dispositivos.",
        DOC, kinds=["teal", "navy", "teal", "teal"], row_h=44, first_gap=46)


def claves() -> Fig:
    f = _canvas("Nivel 6, datos: la jerarquía de claves que usa un mensaje",
                "Diagrama de la jerarquía de claves: la clave de identidad de larga duración firma la prellave firmada de duración media y respalda las prellaves de un solo uso; con ellas se acuerda una clave raíz de 32 bytes que genera claves de cadena de 32 bytes que generan claves de mensaje de 80 bytes divididas en AES-256, HMAC-SHA256 y vector inicial.",
                940, 0)
    B(f, 10, 56, 290, 70, "Clave de identidad (Curve25519): larga duración, se genera al instalar", "navy", 13, bold=True)
    B(f, 325, 56, 290, 70, "Prellave firmada: duración media, firmada por la identidad y rotada", "plain")
    B(f, 640, 56, 290, 70, "Prellaves de un solo uso: una cola que se repone", "plain")
    f.arrow([(300, 91), (325, 91)])
    f.arrow([(615, 91), (640, 91)])
    B(f, 10, 160, 290, 70, "Clave raíz (32 bytes): nace del acuerdo inicial entre las claves públicas", "teal")
    B(f, 325, 160, 290, 70, "Clave de cadena (32 bytes): se renueva con cada mensaje", "teal")
    B(f, 640, 160, 290, 70, "Clave de mensaje (80 bytes): se usa una vez y se descarta", "teal")
    f.arrow([(155, 126), (155, 160)], "acuerdo inicial con las claves públicas del otro", label_at=(165, 148), label_anchor="start")
    f.arrow([(300, 195), (325, 195)])
    f.arrow([(615, 195), (640, 195)])
    B(f, 640, 258, 90, 56, "32 bytes AES-256", "gold")
    B(f, 740, 258, 90, 56, "32 bytes HMAC", "gold")
    B(f, 840, 258, 90, 56, "16 bytes IV", "gold")
    f.arrow([(785, 230), (785, 258)])
    B(f, 10, 258, 605, 56, "Por qué importa: cada mensaje usa una clave distinta, por lo que robar las claves de hoy no abre los mensajes ya enviados ni los de otros dispositivos", "grey")
    return finish(f, 336, "Documentado en el libro blanco de cifrado de WhatsApp y en las especificaciones públicas del protocolo Signal: tipos de claves, tamaños y la propiedad de que las claves efímeras impiden descifrar mensajes pasados. No muestra el algoritmo de renovación de la cadena, que está en las especificaciones, ni el comportamiento del servidor.", DOC)


def cargas() -> Fig:
    f = _canvas("Cómo se probó la capacidad en 2012: tres clases de carga y sus límites",
                "Diagrama de tres clases de carga usadas para medir el clúster: carga sintética, útil para subsistemas con interfaz simple y de poco valor para sistemas de cara al usuario; carga duplicada, extremadamente útil donde los efectos se pueden contener; y carga desviada desde producción, que añade tráfico real a un servidor pero puede provocar problemas con DNS, tiempos de vida y fallos del núcleo.",
                940, 0)
    heads = [("Sintética", "plain"), ("Duplicada (tee)", "teal"), ("Desviada de producción", "gold")]
    texts = [
        ("Qué es: tráfico generado por un programa", "Sirve: para subsistemas con interfaz simple", "Límite: poco valor en un sistema de cara al usuario"),
        ("Qué es: se copia el tráfico real a un servidor de prueba", "Sirve: extremadamente útil para afinar", "Límite: solo donde los efectos secundarios se pueden contener"),
        ("Qué es: se suma tráfico real a un servidor", "Sirve: lleva el servidor a conexiones altas", "Límite: DNS con TTL, reenvío IPFW y algunos fallos del núcleo"),
    ]
    x = 10.0
    for (h, k), (a, b, c) in zip(heads, texts):
        B(f, x, 60, 288, 44, h, k, 14, bold=True)
        B(f, x, 116, 288, 70, a, "plain")
        B(f, x, 198, 288, 70, b, "plain")
        B(f, x, 280, 288, 70, c, "coral")
        f.arrow([(x + 144, 104), (x + 144, 116)])
        x += 314
    return finish(f, 368, "Documentado en la charla de Rick Reed (2012): las tres clases de carga y su valoración. La carga desviada llevó el servidor a 2,8 millones de conexiones en un intento de récord no intencionado en febrero. No se sabe cómo se prueba hoy; es una foto de 2012, no una práctica vigente.", DOC)


def evolucion() -> Fig:
    f = _canvas("Cómo evolucionó el producto y la arquitectura: tres etapas",
                "Tres columnas: de 2009 a 2013 una aplicación de pago pequeña con servidores Erlang sobre FreeBSD; de 2014 a 2020 dentro de Facebook, cifrado de extremo a extremo por defecto en 2016 y fin de la cuota en 2016; desde 2021 varios dispositivos, copias cifradas y una API para empresas.",
                940, 0)
    cols = [
        ("2009-2013: app de pago pequeña", "grey", ["Una cuota anual tras el primer año y sin publicidad (2012)", "Servidores Erlang sobre FreeBSD con millones de conexiones (2012)", "El teléfono es la fuente de verdad del historial"]),
        ("2014-2020: dentro de Facebook", "navy", ["Compra anunciada en febrero de 2014 y cerrada en octubre", "Cifrado de extremo a extremo por defecto en abril de 2016", "Sin cuota desde enero de 2016; negocios como vía de ingreso"]),
        ("2021 en adelante: plataforma", "teal", ["Varios dispositivos con claves por dispositivo (2021)", "Copias de seguridad cifradas con bóveda de claves (2021)", "Cloud API y pagos de mensajería de empresas"]),
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
    return finish(f, 368, "Las etapas son una periodización del curso sobre hechos citados (blog de 2012, blog de 2016, comunicado de 2014, artículos de ingeniería de 2021). El año de inicio de 2009 se apoya solo en la frase «hace tres años» de un texto de 2012. No se sabe cuándo ni cómo cambió la infraestructura interna tras la compra.", DOC)


def cifrado_limites() -> Fig:
    f = _canvas("Dónde llega el cifrado de extremo a extremo y dónde no (definición oficial)",
                "Diagrama de tres escenarios de conversación: entre dos personas todo se cifra de extremo a extremo; con una empresa que usa la aplicación Business en su dispositivo también; con una empresa que usa la Cloud API de Meta, los mensajes usan el protocolo Signal pero WhatsApp no los considera de extremo a extremo porque terminan en un servidor de Meta.",
                940, 0)
    rows = [
        ("Persona a persona", "Teléfono A", "Servidor: solo texto cifrado", "Teléfono B", "teal", "Extremo a extremo"),
        ("Persona a empresa pequeña", "Teléfono", "Servidor: solo texto cifrado", "Dispositivo de la empresa", "teal", "Extremo a extremo"),
        ("Persona a empresa con Cloud API", "Teléfono", "Servidor y Cloud API de Meta", "Sistemas de la empresa", "gold", "No es extremo a extremo según WhatsApp"),
    ]
    y = 60.0
    for name, a, mid, b, k, verdict in rows:
        B(f, 10, y, 170, 80, name, "navy", 13, bold=True)
        B(f, 196, y, 150, 80, a, "plain")
        B(f, 372, y, 190, 80, mid, k)
        B(f, 588, y, 150, 80, b, "plain")
        B(f, 756, y, 174, 80, verdict, k, 13, bold=True)
        f.arrow([(346, y + 40), (372, y + 40)])
        f.arrow([(562, y + 40), (588, y + 40)])
        f.arrow([(738, y + 40), (756, y + 40)], dashed=True)
        y += 98
    return finish(f, y + 6, "Documentado en el libro blanco: todas las conversaciones usan el protocolo Signal, pero WhatsApp no considera de extremo a extremo la comunicación con empresas que usan la Cloud API, porque no llega a un punto final controlado por la empresa; el chat lo indica con un mensaje del sistema. No cubre los metadatos (con quién y cuándo), cuyo tratamiento detallado no es público.", DOC)


def alternativas() -> Fig:
    f = _canvas("Alternativas descartadas: cuatro bifurcaciones y su coste probable (análisis propio)",
                "Cuatro filas de decisión con la opción elegida y la alternativa: Erlang sobre FreeBSD frente a una pila más convencional; cifrado de extremo a extremo por defecto frente a cifrado en tránsito; cuota anual frente a publicidad; el teléfono como fuente de verdad frente a varios dispositivos independientes.",
                940, 0)
    rows = [
        ("Servidor", "Elegida: Erlang sobre FreeBSD (hasta 2,8 millones de conexiones por servidor en 2012)", "teal", "Alternativa: una pila convencional con un hilo por conexión", "Muchos más servidores para la misma base; más coste y más piezas que fallan"),
        ("Privacidad", "Elegida: cifrado de extremo a extremo por defecto (2016)", "gold", "Alternativa: cifrado solo en tránsito y texto legible en el servidor", "Servidor con acceso al texto: más funciones de servidor, más superficie de abuso y de exigencias legales"),
        ("Ingreso", "Elegida: cuota anual y luego gratis con negocios (2012, 2016)", "navy", "Alternativa: publicidad basada en datos de la conversación", "Contradice la promesa pública; el cifrado deja pocas señales para segmentar"),
        ("Dispositivos", "Elegida: claves por dispositivo y reparto en el cliente (2021)", "teal", "Alternativa: seguir con el teléfono como fuente de verdad", "Menos trabajo para el emisor pero el teléfono sigue siendo un punto único de fallo"),
    ]
    y = 56.0
    for name, a, ka, b, cost in rows:
        B(f, 10, y, 110, 96, name, "navy", 13, bold=True)
        B(f, 134, y, 262, 96, a, ka)
        B(f, 412, y, 250, 96, b, "grey", dashed=True)
        B(f, 678, y, 252, 96, cost, "coral", dashed=True)
        f.arrow([(396, y + 48), (412, y + 48)])
        f.arrow([(662, y + 48), (678, y + 48)], dashed=True)
        y += 108
    return finish(f, y + 4, "Es un análisis propio, no un hecho: WhatsApp no publica qué alternativas evaluó. Lo documentado es la opción elegida y su motivo declarado; los costes de las alternativas son hipótesis razonadas con la teoría del curso para entrenar el razonamiento.", INF, "coral")


def compra() -> Fig:
    return stacked_bars(
        "El precio de la compra según el momento: anuncio y cierre (millones de USD)",
        "Barras apiladas de efectivo y acciones: en el anuncio de febrero de 2014, 4 000 en efectivo y 12 000 en acciones; al cerrar en octubre de 2014, 4 589 en efectivo y 13 787 en acciones, por el precio de la acción de ese día.",
        ["Anuncio (febrero de 2014)", "Cierre (octubre de 2014)"],
        [("Efectivo", [4000, 4589], "navy"), ("Acciones", [12000, 13787], "teal")],
        unit="millones de USD", horizontal=True, decimals=0, label_w=190,
        note="El comunicado habla de unos 16 000 millones más 3 000 en acciones restringidas; el 10-K de 2014 registra 178 millones de acciones a 77,56 USD, 4 589 en efectivo y una contraprestación contable de 17 193 millones tras descontar 1 067 de compensación posterior y 116 de caja adquirida. Dos cifras distintas, ambas correctas, porque el valor de las acciones cambió entre febrero y octubre.",
        note_kind="gold", foot=FIN)


def ingresos_meta() -> Fig:
    return grouped_bars(
        "Otros ingresos de la familia de aplicaciones de Meta, donde cuenta el pago por mensajería de WhatsApp",
        "Barras de los otros ingresos de la familia de aplicaciones de Meta: 1 058 millones de dólares en 2023, 1 722 en 2024 y 2 584 en 2025; incluyen el pago por mensajería de WhatsApp, las suscripciones Meta Verified, tarifas de pagos y otras fuentes.",
        ["2023", "2024", "2025"],
        [("Otros ingresos, familia de aplicaciones", [1058, 1722, 2584], "gold")],
        unit="millones de USD", decimals=0, plot_h=240,
        note="Es un techo, no el ingreso de WhatsApp: el 10-K lo describe como pago por mensajería de WhatsApp más suscripciones Meta Verified, tarifas de pagos y otras fuentes, y no los separa. Frente a los 200 966 millones de ingresos totales de Meta en 2025, equivale a 1,3 por ciento. Meta no publica el ingreso de WhatsApp por separado.",
        note_kind="gold", foot="Fuente: Meta, Form 10-K de 2025 (SEC). Consulta: 16 de noviembre de 2026.")


FIGURES = {
    "whatsapp-contexto.svg": contexto,
    "whatsapp-piezas-de-escala.svg": componentes,
    "whatsapp-flujo-de-un-mensaje.svg": flujo,
    "whatsapp-linea-de-tiempo.svg": linea,
    "whatsapp-conexiones-por-servidor.svg": conexiones,
    "whatsapp-actores-e-incentivos.svg": actores,
    "whatsapp-recorridos-de-usuario.svg": viajes,
    "whatsapp-contenedores.svg": contenedores,
    "whatsapp-secuencia-primer-mensaje.svg": sec_mensaje,
    "whatsapp-secuencia-adjunto-y-grupo.svg": sec_adjunto,
    "whatsapp-secuencia-varios-dispositivos.svg": sec_multi,
    "whatsapp-jerarquia-de-claves.svg": claves,
    "whatsapp-cargas-de-prueba-2012.svg": cargas,
    "whatsapp-evolucion-por-etapas.svg": evolucion,
    "whatsapp-alcance-del-cifrado.svg": cifrado_limites,
    "whatsapp-alternativas-descartadas.svg": alternativas,
    "whatsapp-precio-de-la-compra.svg": compra,
    "whatsapp-otros-ingresos-de-meta.svg": ingresos_meta,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
