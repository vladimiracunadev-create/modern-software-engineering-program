"""Figures for the failure case study Meta/Facebook outage of 4 October 2021.

Times (UTC) come from the Cloudflare post of 4 October 2021; mechanism and the six-hour duration from the Meta
engineering posts of 4 and 5 October 2021 and the Form 10-Q of 25 October 2021; user and revenue numbers from the
Q3 2021 results exhibit. Output goes to ``casos/figures/``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from figure_cases import case_cards  # noqa: E402
from figure_kit import Fig, _kit_finish, _kit_start, _wrap, grouped_bars, timeline  # noqa: E402

META = "Fuente: Meta Engineering, «More details about the October 4 outage» (5 de octubre de 2021)."
ANALISIS = "Análisis propio apoyado en las publicaciones de Meta y Cloudflare; no es una conclusión de esas fuentes."


def sketch(title: str, desc: str, width: int = 940):
    return _kit_start(title, desc, width, None)


def bx(f: Fig, x: float, y: float, w: float, h: float, text: str, kind: str = "plain", size: int = 13, bold: bool = False) -> None:
    lines = _wrap(text, size, w - 20)
    assert len(lines) * size * 1.28 <= h - 6, f"box overflows: {text!r} ({len(lines)} lines in {h}px)"
    f.box(x, y, w, h, text, kind, size, bold=bold)


def done(f: Fig, y: float, note: str, kind: str = "gold", foot: str = "") -> Fig:
    _kit_finish(f, y, note, kind, foot)
    f.kind = "diagram"
    return f


# ------------------------------------------------------------------ 1. contexto
def contexto() -> Fig:
    f, y = sketch("Cómo llega una petición a Facebook: DNS, borde y red troncal",
                  "Diagrama de contexto: el dispositivo del usuario pregunta a un resolvedor DNS la dirección; los servidores DNS autoritativos de Facebook, alojados en instalaciones pequeñas de borde y anunciados al resto de internet con BGP, responden; la petición viaja al borde más cercano y de ahí, por la red troncal propia, a un centro de datos grande donde se procesa.")
    y0 = y + 6
    bx(f, 10, y0 + 30, 140, 92, "Aplicación del usuario", "plain", 13, True)
    bx(f, 180, y0 + 30, 150, 92, "Resolvedor DNS (1.1.1.1, 8.8.8.8, del operador)", "plain")
    bx(f, 360, y0 + 30, 170, 92, "DNS autoritativo de Facebook, en el borde, anunciado por BGP", "coral", 13, True)
    bx(f, 560, y0 + 30, 160, 92, "Instalación de borde cercana", "teal")
    bx(f, 750, y0 + 30, 180, 92, "Centro de datos grande (datos y cómputo)", "navy", 13, True)
    for a, b in ((150, 180), (330, 360), (530, 560), (720, 750)):
        f.arrow([(a, y0 + 76), (b, y0 + 76)])
    f.group(540, y0 + 150, 390, 70, "Red troncal propia de Facebook", "grey")
    f.arrow([(640, y0 + 122), (640, y0 + 150)], dashed=True)
    f.arrow([(840, y0 + 122), (840, y0 + 150)], dashed=True)
    bx(f, 10, y0 + 150, 500, 70, "Si el DNS no responde, la aplicación no sabe adónde ir aunque los servidores sigan encendidos", "gold")
    return done(f, y0 + 236,
                "Lo que enseña: el nombre es lo primero que se necesita y depende de dos cosas: un servidor DNS vivo y una ruta anunciada hacia él. Ambas dependían, en Facebook, del estado de la red troncal.",
                "gold", META + " Descripción funcional según la publicación.")


# ------------------------------------------------------------------ 2. cadena causal
def cadena() -> Fig:
    f, y = sketch("Una instrucción de mantenimiento, un auditor con un fallo y un DNS que se retira por prudencia",
                  "Cadena causal de seis eslabones: un comando de mantenimiento para evaluar capacidad de la red troncal; una herramienta de auditoría con un error no lo detiene; se desconecta toda la red troncal; los centros de datos quedan aislados; los servidores DNS, al no ver los centros de datos, retiran sus anuncios BGP; internet ya no encuentra los servidores.")
    y0 = y + 6
    pasos = [("Comando de mantenimiento que evalúa la capacidad de la red troncal", "plain"), ("La herramienta de auditoría falla y no detiene el comando", "coral"), ("Se desconecta toda la red troncal", "coral"), ("Centros de datos aislados entre sí y de internet", "coral"), ("Los DNS se declaran no sanos y retiran su anuncio BGP", "gold"), ("Internet no encuentra los servidores de Facebook", "coral")]
    w, gap = 132, 28
    for i, (t, k) in enumerate(pasos):
        x = 10 + i * (w + gap)
        bx(f, x, y0 + 14, w, 118, t, k, 13, i in (1, 4))
        if i < 5:
            f.arrow([(x + w, y0 + 73), (x + w + gap, y0 + 73)])
    bx(f, 10, y0 + 170, 440, 74, "Decisión de diseño razonable: un DNS que no ve sus centros de datos deja de anunciarse para no dirigir usuarios a un sitio roto", "teal")
    bx(f, 490, y0 + 170, 440, 74, "Efecto combinado: la señal de salud de cada borde era correcta localmente y catastrófica en conjunto", "coral", 13, True)
    return done(f, y0 + 260,
                "Lo que enseña: dos mecanismos correctos por separado (una auditoría de comandos y un retiro de anuncios por salud) se combinaron en un fallo total. La auditoría falló por un error y el retiro de anuncios amplificó un aislamiento interno hasta hacerlo visible a todo internet.",
                "gold", META + " «Fallo» de la auditoría y retirada de BGP según la publicación.")


# ------------------------------------------------------------------ 3. dependencias circulares
def circulo() -> Fig:
    f, y = sketch("El círculo que dificultó la recuperación: lo que se necesitaba para arreglar dependía de lo roto",
                  "Cuatro obstáculos que Meta describe para recuperar: la red de acceso normal y la fuera de banda estaban caídas; la pérdida del DNS rompió herramientas internas de diagnóstico; el acceso físico a los centros de datos requería activar protocolos de seguridad; y el hardware estaba diseñado para ser difícil de modificar incluso con acceso físico.")
    y0 = y + 6
    bx(f, 10, y0 + 10, 210, 76, "Red troncal caída (causa original)", "coral", 13, True)
    bx(f, 255, y0 + 10, 210, 76, "Acceso normal y red fuera de banda sin servicio", "coral")
    bx(f, 500, y0 + 10, 210, 76, "DNS perdido: herramientas internas de diagnóstico rotas", "coral")
    bx(f, 745, y0 + 10, 185, 76, "Hace falta ir en persona a los centros de datos", "gold", 13, True)
    for a, b in ((220, 255), (465, 500), (710, 745)):
        f.arrow([(a, y0 + 48), (b, y0 + 48)])
    bx(f, 255, y0 + 130, 210, 76, "Instalaciones con alta seguridad física y de sistemas", "plain")
    bx(f, 500, y0 + 130, 210, 76, "Hardware difícil de modificar aun con acceso físico", "plain")
    bx(f, 745, y0 + 130, 185, 76, "Activar protocolos de acceso seguro: más tiempo", "teal")
    f.arrow([(837, y0 + 86), (837, y0 + 130)])
    f.arrow([(465, y0 + 168), (500, y0 + 168)])
    f.arrow([(710, y0 + 168), (745, y0 + 168)])
    bx(f, 10, y0 + 130, 210, 76, "Meta: la dureza ante accesos no autorizados frenó la recuperación", "navy")
    return done(f, y0 + 222,
                "Lo que enseña: cuanto más seguro y más acoplado es un sistema, más importa que su vía de emergencia no comparta dependencias con él. Meta valora que la compensación entre seguridad diaria y recuperación más lenta es aceptable; es una posición de la empresa, no un hecho universal.",
                "gold", META)


# ------------------------------------------------------------------ 4. línea de tiempo
def tiempos() -> Fig:
    return timeline(
        "4 de octubre de 2021 (UTC): seis horas desde los primeros cambios de ruta",
        "Línea de tiempo en horas desde las 15:00 UTC según Cloudflare: alrededor de las 15:40 se ve un pico de cambios de rutas BGP de Facebook; a las 15:58 se advierte que ya no anuncia las rutas de sus servidores DNS; hacia las 21:00 vuelve la actividad BGP, con un pico a las 21:17; a las 21:28 Facebook parece reconectado a internet.",
        [("Rutas BGP y DNS de Facebook ausentes", [(0.67, 6.0, "Sin rutas ni DNS: unas 5 h 20 min", "coral")]),
         ("Reconexión y vuelta del DNS", [(6.0, 6.47, "", "teal")])],
        unit="Horas desde las 15:00 UTC (0 = 15:00 UTC)",
        events=[(0.67, "15:40"), (6.0, "21:00")],
        ticks=[0, 1, 2, 3, 4, 5, 6, 7], t_max=7, label_w=250,
        note="Cloudflare ve el pico de cambios de ruta a las 15:40, abre una incidencia a las 15:51 y confirma a las 15:58 que Facebook ya no anunciaba las rutas de sus DNS. La actividad BGP vuelve a las 21:00 (pico 21:17) y el DNS de facebook.com vuelve a responder hacia las 21:20, con Facebook reconectado a las 21:28. Meta y su informe financiero hablan de un apagón de unas seis horas.",
        note_kind="gold", foot="Fuentes: Cloudflare, «Understanding how Facebook disappeared from the Internet» (4 oct 2021); Meta, Form 10-Q (25 oct 2021).")


# ------------------------------------------------------------------ 5. gráfico con datos citados
def alcance() -> Fig:
    return grouped_bars(
        "Cuánta gente dependía de estos servicios en septiembre de 2021",
        "Barras horizontales en miles de millones de personas: 2,91 usuarios activos mensuales de Facebook, 2,81 personas activas diarias de la familia de aplicaciones y 3,58 personas activas mensuales de la familia, según el comunicado de resultados del tercer trimestre de 2021.",
        ["Usuarios activos mensuales de Facebook", "Personas activas diarias de la familia (media de septiembre)", "Personas activas mensuales de la familia"],
        [("Miles de millones", [2.91, 2.81, 3.58], "navy")],
        unit="Miles de millones de personas (septiembre de 2021)", horizontal=True, label_w=340, decimals=2,
        ticks=[0, 1, 2, 3, 4],
        note="La familia incluye Facebook, Instagram, WhatsApp y Messenger. Los ingresos del tercer trimestre fueron de 29 010 millones de dólares; repartidos de forma uniforme por las 24 horas de los 92 días del trimestre salen unos 13,1 millones por hora, o unos 79 millones en seis horas. Es aritmética ilustrativa, no una pérdida medida: Meta no publicó el ingreso perdido (inferencia: parte de la publicidad podría desplazarse a otro momento).",
        note_kind="gold", foot="Fuente: Meta, comunicado de resultados del tercer trimestre de 2021 (anexo 99.1 del Form 8-K del 25 de octubre de 2021).")


# ------------------------------------------------------------------ 6. mejoras
def mejoras() -> Fig:
    return case_cards(
        "Seis decisiones del caso y la mejora que las habría cambiado",
        "Seis tarjetas con una situación documentada y la mejora propuesta: probar la herramienta de auditoría con fallos inyectados, distinguir aislamiento global de fallo local en la lógica de retiro de BGP, una red fuera de banda realmente independiente, herramientas de emergencia sin DNS, acceso físico de emergencia preautorizado y ensayos del escenario de pérdida de la red troncal.",
        [("Un error en la herramienta de auditoría permitió el comando", "Probar la auditoría con comandos peligrosos inyectados y exigir confirmación doble", "Meta reconoce el error de la auditoría; la prueba concreta es propuesta nuestra.", "teal"),
         ("Los DNS retiran sus anuncios BGP si no ven los centros de datos", "Que no todos retiren a la vez: si todos los bordes se declaran enfermos, mantener un mínimo", "Una decisión local correcta puede ser global y catastrófica.", "teal"),
         ("La red de acceso fuera de banda también cayó", "Una vía de emergencia con otro camino, otro proveedor y sin pasar por la red troncal", "Meta: tanto el acceso primario como el fuera de banda estaban caídos.", "teal"),
         ("La pérdida del DNS rompió herramientas internas de diagnóstico", "Herramientas de emergencia sin dependencia del DNS de producción", "Meta describe que se rompieron las herramientas habituales.", "teal"),
         ("El acceso físico requería activar protocolos de seguridad y tardó", "Procedimiento de acceso de emergencia preautorizado y ensayado", "Meta describe el tiempo extra que añadió la seguridad física.", "teal"),
         ("Nunca se había simulado la pérdida de la red troncal global", "Añadir ese escenario a los ejercicios de tormenta", "Meta lo dice textualmente: no lo habían simulado antes.", "teal")],
        note=ANALISIS, note_kind="teal", foot="", left=0.46)


FIGURES = {
    "meta-2021-contexto.svg": contexto,
    "meta-2021-cadena-causal.svg": cadena,
    "meta-2021-circulo-de-dependencias.svg": circulo,
    "meta-2021-linea-de-tiempo.svg": tiempos,
    "meta-2021-alcance.svg": alcance,
    "meta-2021-mejoras.svg": mejoras,
}


def main(out: str | None = None) -> int:
    target = Path(out) if out else Path(__file__).resolve().parents[1] / "casos" / "figures"
    target.mkdir(parents=True, exist_ok=True)
    for name, builder in FIGURES.items():
        (target / name).write_text(builder().svg(), encoding="utf-8", newline="\n")
        print("wrote", target / name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else None))
