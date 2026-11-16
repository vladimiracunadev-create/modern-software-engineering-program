"""Figures for the WhatsApp success case (casos/exito/whatsapp.md).

Numbers come from public sources cited in the case page: the 2012 Erlang Factory talk by
Rick Reed, WhatsApp's own blog and security white paper, and Meta's engineering blog.
Diagrams mark what is documented and what is inferred.
"""
from __future__ import annotations

import re

from figure_kit import Fig, _wrap, grouped_bars, timeline

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


FIGURES = {
    "whatsapp-contexto.svg": contexto,
    "whatsapp-piezas-de-escala.svg": componentes,
    "whatsapp-flujo-de-un-mensaje.svg": flujo,
    "whatsapp-linea-de-tiempo.svg": linea,
    "whatsapp-conexiones-por-servidor.svg": conexiones,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys
    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
