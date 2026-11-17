"""Figures for the failure case study Meta/Facebook outage of 4 October 2021.

Times (UTC) come from the Cloudflare post of 4 October 2021; mechanism and the six-hour duration from the Meta
engineering posts of 4 and 5 October 2021 and the Form 10-Q of 25 October 2021; user and revenue numbers from the
Q3 2021 results exhibit. Output goes to ``casos/figures/``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_helpers_fallo import sequence, slices  # noqa: E402
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


# ================================================================== ampliación: niveles de arquitectura y análisis
CF = "Cloudflare, «Understanding how Facebook disappeared from the Internet» (4 de octubre de 2021)"
GOOGLE = "Google Cloud, informe del incidente 19009 (2 de junio de 2019)"


def planos() -> Fig:
    f, y = sketch("Tres planos sobre un mismo camino: datos, control y gestión",
                  "Diagrama de planos: el plano de datos con los usuarios y las aplicaciones, el plano de control con las rutas BGP y los servidores DNS, y el plano de gestión con las herramientas internas y el acceso de emergencia; los tres dependen de la misma red troncal, y el plano de gestión depende además del DNS.")
    y0 = y + 6
    bx(f, 10, y0, 910, 70, "Plano de datos: del dispositivo al borde y, por la red troncal, al centro de datos que procesa la petición", "teal", 13, True)
    bx(f, 10, y0 + 100, 910, 70, "Plano de control: DNS autoritativo y anuncios BGP, que dicen a internet cómo llegar a Facebook", "gold", 13, True)
    bx(f, 10, y0 + 200, 910, 70, "Plano de gestión: herramientas internas, diagnóstico, acceso primario y acceso fuera de banda para operar la red", "coral", 13, True)
    bx(f, 10, y0 + 300, 910, 64, "Red troncal global propia: la misma para los tres planos", "navy", 13, True)
    for x in (120, 470, 820):
        f.arrow([(x, y0 + 300), (x, y0 + 270)], dashed=True)
        f.arrow([(x, y0 + 200), (x, y0 + 170)], dashed=True)
        f.arrow([(x, y0 + 100), (x, y0 + 70)], dashed=True)
    return done(f, y0 + 380,
                "Lo que enseña: los tres planos compartían camino. Cuando el camino desapareció, cayeron los datos, el control (nadie anunciaba rutas) y también la gestión (las herramientas y el acceso). Las herramientas dependían además del DNS, que era parte del plano de control.",
                "gold", ANALISIS + " Hechos de Meta Engineering (5 de octubre de 2021).")


def estados() -> Fig:
    f, y = sketch("La regla de salud del DNS como máquina de estados",
                  "Máquina de estados con dos estados: anunciando, donde el servidor DNS anuncia sus rutas BGP, y retirado, donde las ha retirado; la pérdida de contacto con los centros de datos lleva a retirado y la recuperación de la red troncal debe devolver a anunciando, mientras en retirado el DNS es inalcanzable aunque funcione.")
    y0 = y + 6
    bx(f, 60, y0 + 60, 260, 100, "Anunciando: el servidor DNS anuncia sus rutas por BGP y responde consultas", "teal", 13, True)
    bx(f, 560, y0 + 60, 260, 100, "Retirado: ha quitado sus anuncios; sigue operativo pero nadie puede alcanzarlo", "coral", 13, True)
    f.arrow([(320, y0 + 90), (560, y0 + 90)], "pierde contacto con los centros de datos", color="#c0432f", label_at=(440, y0 + 72))
    f.arrow([(560, y0 + 135), (320, y0 + 135)], "vuelve la conectividad de la red troncal", dashed=True, label_at=(440, y0 + 160))
    bx(f, 60, y0 + 200, 400, 72, "Intención de diseño: no enviar usuarios a un sitio roto si el servidor se cree aislado", "gold")
    bx(f, 500, y0 + 200, 420, 72, "Efecto emergente: si todos los servidores se creen aislados a la vez, internet pierde todos los DNS", "coral")
    return done(f, y0 + 290,
                "Lo que enseña: la regla es local y razonable; el problema es que su señal («no veo los centros de datos») era la misma para todos cuando la causa estaba en la red troncal global. La transición de regreso es lo que se vio como actividad BGP a las 21:00 UTC. Los nombres de los estados son nuestros.",
                "gold", "Fuente: Meta Engineering (5 de octubre de 2021) y " + CF + ". Máquina de estados: modelo propio.")


def secuencia() -> Fig:
    f, y = sketch("Secuencia de los primeros minutos: del comando a los reintentos de todo internet",
                  "Diagrama de secuencia con mantenimiento y auditoría, red troncal, DNS en el borde, internet por BGP, resolvedores públicos y usuarios: el comando desconecta la red troncal, la auditoría no lo detiene, los DNS retiran sus rutas, los resolvedores devuelven error y los usuarios y aplicaciones reintentan.")
    y0 = y + 6
    lanes = [("Mantenimiento y auditoría", "gold"), ("Red troncal", "navy"), ("DNS en el borde", "coral"), ("Internet (BGP)", "plain"), ("Resolvedores públicos", "plain"), ("Usuarios y apps", "plain")]
    steps = [(0, 1, "comando"), (0, 0, "auditoría con error", "note"), (1, 2, "aislado", "red"),
             (2, 3, "retira rutas", "red"), (4, 2, "consulta", "red"), (4, 5, "SERVFAIL", "red"),
             (5, 4, "reintentos", "red"), (0, 0, "herramientas y acceso caídos", "note")]
    yy = sequence(f, y0, lanes, steps, row_h=38)
    return done(f, yy,
                "Lo que enseña: todo ocurre en minutos y la señal más visible para el exterior (los DNS fuera de internet) es una consecuencia del fallo interno, no su causa. El último paso muestra que el gestor de red ya no tenía sus propias herramientas. El orden fino de los pasos es una reconstrucción de las fuentes.",
                "coral", "Fuente: Meta Engineering (5 de octubre de 2021) y " + CF + ". Orden: modelo propio.")


def radio() -> Fig:
    f, y = sketch("Radio de explosión: un comando sobre toda la red frente a un comando limitado a una región",
                  "Dos cuadrículas de veinte círculos que representan instalaciones: a la izquierda, el comando afecta a todas y quedan todas desconectadas; a la derecha, con un límite de alcance, el mismo comando solo afecta a una región de cuatro instalaciones y las demás siguen operativas. Modelo didáctico con valores ilustrativos.")
    y0 = y + 6
    f.text(14, y0 + 12, "Como ocurrió: el comando alcanzó todas las conexiones de la red troncal", 13, "start", 700, "#142231")
    f.text(490, y0 + 12, "Con límite de alcance (ilustrativo): una región cada vez", 13, "start", 700, "#142231")
    for i in range(20):
        r, c = divmod(i, 5)
        f.dot(40 + c * 54, y0 + 56 + r * 46, "", "coral")
        f.dot(520 + c * 54, y0 + 56 + r * 46, "", "coral" if i < 4 else "teal")
    bx(f, 10, y0 + 250, 440, 56, "20 de 20 instalaciones desconectadas: ninguna queda para operar a las demás", "coral", 13, True)
    bx(f, 490, y0 + 250, 440, 56, "4 de 20 desconectadas: quedan 16 con red y herramientas para recuperar", "teal", 13, True)
    return done(f, y0 + 326,
                "Lo que enseña: el tamaño del daño lo fija el alcance máximo que un solo comando puede tener, no la probabilidad del error. Con un límite de alcance, el mismo error habría sido un incidente regional. Los números son ilustrativos: Meta no publicó cuántas instalaciones tiene ni su reparto.",
                "gold", "Modelo didáctico con valores ilustrativos; no son datos de Meta. Hecho de base: Meta Engineering (5 de octubre de 2021).")


def dependencias() -> Fig:
    f, y = sketch("Dependencias y puntos únicos de fallo de la red de Meta ese día",
                  "Mapa de dependencias: la red troncal global es el centro; de ella dependen el DNS en el borde, la regla de salud del DNS, el acceso primario, el acceso fuera de banda, las herramientas internas que usan DNS, y el acceso físico a las instalaciones, endurecido por diseño; la auditoría de comandos es la única barrera antes del cambio.")
    y0 = y + 6
    bx(f, 340, y0 + 110, 260, 70, "Red troncal global: único camino entre instalaciones", "coral", 13, True)
    bx(f, 340, y0, 260, 60, "Auditoría de comandos: barrera única", "gold", 13, True)
    bx(f, 20, y0 + 20, 250, 70, "DNS en el borde y regla de salud", "coral")
    bx(f, 670, y0 + 20, 250, 70, "Acceso primario y fuera de banda", "coral")
    bx(f, 20, y0 + 210, 250, 70, "Herramientas internas que dependen del DNS", "coral")
    bx(f, 340, y0 + 230, 260, 70, "Acceso físico endurecido por diseño", "gold")
    bx(f, 670, y0 + 210, 250, 70, "Reinicio gradual: depende de la energía y de las cachés", "gold")
    f.arrow([(470, y0 + 60), (470, y0 + 110)], dashed=True)
    f.arrow([(340, y0 + 135), (270, y0 + 65)])
    f.arrow([(600, y0 + 135), (670, y0 + 65)])
    f.arrow([(340, y0 + 160), (270, y0 + 235)])
    f.arrow([(470, y0 + 230), (470, y0 + 180)], dashed=True)
    f.arrow([(600, y0 + 160), (670, y0 + 235)], dashed=True)
    return done(f, y0 + 316,
                "Lo que enseña: las cajas rojas dependen directamente de la red troncal; sin ella no hay datos, ni DNS, ni acceso para operarla, ni herramientas. El único camino de recuperación que no pasaba por la red era el acceso físico, y estaba diseñado para ser lento.",
                "gold", ANALISIS)


def defensa() -> Fig:
    f, y = sketch("Defensa en profundidad: siete barreras que no frenaron y una que sí funcionó",
                  "Láminas con huecos: auditoría de comandos con un error, límite de alcance del cambio que no consta, regla de salud del DNS que amplificó, acceso primario caído, red fuera de banda caída, herramientas de diagnóstico rotas por el DNS y acceso físico endurecido; la octava, el reinicio gradual preparado con ejercicios, sí funcionó.")
    y0 = y + 6
    items = [("Auditoría de comandos (con un error)", "coral", 0.5),
             ("Límite de alcance de un cambio (no consta)", "grey", 0.5),
             ("Regla de salud del DNS (amplificó)", "coral", 0.5),
             ("Acceso primario (caído)", "coral", 0.5),
             ("Red fuera de banda (caída)", "coral", 0.5),
             ("Herramientas de diagnóstico (rotas sin DNS)", "coral", 0.5),
             ("Acceso físico seguro (lento por diseño)", "gold", 0.5),
             ("Reinicio gradual con ejercicios de tormenta (funcionó)", "teal", 0.0)]
    yy = slices(f, y0, items, x0=30, w=62, gap=51, h=170, label_h=150, label_w=104)
    ymid = y0 + 18 + 0.5 * (170 - 80) + 22
    f.arrow([(10, ymid), (808, ymid)], color="#c0432f")
    return done(f, yy,
                "Lo que enseña: el fallo atravesó siete capas porque todas compartían la red; la octava funcionó porque se había ensayado. Rojo: falló; gris: no consta en las fuentes; dorado: funcionó con coste de tiempo; verde azulado: funcionó. La flecha se detiene en la barrera ensayada.",
                "teal", ANALISIS + " Hechos de Meta Engineering (5 de octubre de 2021).")


def arbol() -> Fig:
    f, y = sketch("Árbol de fallas: qué tuvo que coincidir para seis horas sin servicio",
                  "Árbol de fallas con el evento principal arriba, servicios inaccesibles unas seis horas, y tres ramas: la red troncal desconectada, internet que no encuentra los servidores y una recuperación lenta; cada una con sus condiciones documentadas.")
    y0 = y + 6
    bx(f, 290, y0, 360, 52, "Facebook, Instagram y WhatsApp inaccesibles unas seis horas", "navy", 13, True)
    f.dot(470, y0 + 76, "Y", "navy")
    f.arrow([(470, y0 + 52), (470, y0 + 64)])
    f.line(470, y0 + 88, 160, y0 + 110)
    f.line(470, y0 + 88, 470, y0 + 110)
    f.line(470, y0 + 88, 780, y0 + 110)
    bx(f, 30, y0 + 110, 260, 56, "A. Red troncal desconectada", "coral", 13, True)
    bx(f, 340, y0 + 110, 260, 56, "B. Internet no encuentra los servidores", "coral", 13, True)
    bx(f, 650, y0 + 110, 260, 56, "C. Recuperación lenta", "coral", 13, True)
    hojas = [["Un comando desconecta todas las conexiones", "Auditoría con un error"],
             ["El DNS retira sus rutas al aislarse", "El DNS vive en el borde y depende de la troncal"],
             ["Acceso primario y fuera de banda caídos", "Herramientas sin DNS", "Acceso físico endurecido"]]
    cxs = [160, 470, 780]
    for c, col in enumerate(hojas):
        cx = cxs[c]
        f.dot(cx, y0 + 190, "O" if c == 2 else "Y", "navy")
        f.line(cx, y0 + 166, cx, y0 + 178)
        n = len(col)
        for i, t in enumerate(col):
            x = cx - (n * 96) / 2 + i * 96 + 4
            bx(f, x, y0 + 226, 88, 150, t, "gold", 13)
            f.line(cx, y0 + 202, x + 44, y0 + 226)
    return done(f, y0 + 392,
                "Lo que enseña: A y B se combinan («Y»): sin la regla de retirada de rutas el fallo habría sido interno; sin el comando, no habría habido regla que disparar. C se compone con «O»: cualquiera de sus tres condiciones alargaba la recuperación.",
                "gold", ANALISIS)


def veinte_minutos() -> Fig:
    return timeline(
        "Los primeros veinte minutos vistos desde fuera: de las 15:40 a las 16:10 UTC",
        "Línea de tiempo en minutos desde las 15:30 UTC: el pico de cambios de rutas BGP de Facebook a las 15:40, el nombre facebook.com deja de resolverse en 1.1.1.1 hacia las 15:50, Cloudflare abre una incidencia interna a las 15:51 y a las 15:58 advierte que Facebook ha dejado de anunciar las rutas de sus DNS.",
        [("Rutas BGP de Facebook", [(10, 40, "cambios y retirada de rutas", "coral")]),
         ("facebook.com en 1.1.1.1", [(0, 20, "resuelve", "teal"), (20, 40, "SERVFAIL", "coral")]),
         ("Cloudflare", [(21, 28, "alerta", "navy"), (28, 40, "confirma retirada", "navy")])],
        unit="Minutos desde las 15:30 UTC del 4 de octubre de 2021", events=[(10, "15:40"), (21, "15:51"), (28, "15:58")],
        ticks=[0, 10, 20, 30, 40], t_max=40, label_w=250,
        note="Cloudflare notó el problema un minuto después del pico de cambios y lo confirmó a las 15:58. La figura es la vista externa (BGP y DNS); Meta no publicó la hora exacta del comando ni de su propia detección.",
        note_kind="gold", foot="Fuente: " + CF + ".")


def reintentos() -> Fig:
    return grouped_bars(
        "La tormenta de reintentos: lo que le costó a terceros que Facebook cayera",
        "Barras horizontales: las consultas DNS en los resolvedores de todo el mundo, expresadas como múltiplo de lo habitual, pasan de uno a unas treinta veces durante el apagón, según Cloudflare.",
        ["Consultas DNS habituales", "Durante el apagón de Facebook"],
        [("Veces lo habitual", [1, 30], "coral")], unit="Veces las consultas habituales (Cloudflare)", horizontal=True, label_w=250,
        ticks=[0, 10, 20, 30, 40],
        note="El aumento lo causan los reintentos agresivos de aplicaciones y usuarios ante errores SERVFAIL. Cloudflare dice que su resolvedor 1.1.1.1 siguió sirviendo con impacto mínimo: la mayoría de las consultas se resolvían en menos de 10 ms. La caída de un gran servicio se transforma en carga para el resto de internet.",
        note_kind="gold", foot="Fuente: " + CF + ". La cifra es la que da Cloudflare («30x»).")


def despues() -> Fig:
    f, y = sketch("Arquitectura «después»: cuatro cambios que separan los planos",
                  "Arquitectura objetivo propuesta: un plano de gestión independiente con red fuera de banda por otro camino y herramientas sin DNS de producción; un plano de control con un suelo global que impide retirar todos los DNS a la vez; cambios con alcance limitado y auditoría probada; y ejercicios de pérdida de la red troncal.")
    y0 = y + 6
    bx(f, 10, y0, 450, 110, "Gestión independiente: red fuera de banda con otro camino y otro proveedor, herramientas que no usan el DNS de producción, acceso de emergencia preautorizado", "teal", 13, True)
    bx(f, 480, y0, 450, 110, "Control con suelo global: la regla de salud no puede retirar más de una fracción de los DNS; siempre quedan servidores anunciando", "teal", 13, True)
    bx(f, 10, y0 + 140, 450, 110, "Cambios con alcance limitado: auditoría probada con casos peligrosos, simulación de impacto, una región cada vez y reversión automática", "gold", 13, True)
    bx(f, 480, y0 + 140, 450, 110, "Ensayos: pérdida total de la red troncal, recuperación sin DNS y reinicio escalonado, con las personas de seguridad física incluidas", "gold", 13, True)
    return done(f, y0 + 270,
                "Lo que enseña: ninguna mejora quita la seguridad física ni la regla de salud, las acota. Cuatro frentes: que gestionar no dependa de lo gestionado, que ninguna regla local pueda apagar todo, que un comando no pueda tocar toda la red, y que se haya ensayado el peor caso. Es análisis propio; Meta describió que estudiaba mejoras, sin detalle público.",
                "teal", ANALISIS)


def barrera() -> Fig:
    f, y = sketch("Diseño de la barrera: un comando de red que simula su impacto antes de ejecutarse",
                  "Flujo de una barrera de alcance: el comando propuesto se simula, se calcula cuánta capacidad y cuántas regiones quita, si supera un umbral exige doble aprobación y ejecución por región, y tras ejecutar una comprobación automática verifica que el DNS y el acceso fuera de banda siguen alcanzables o revierte.")
    y0 = y + 6
    w, gap = 164, 30
    pasos = [("1. Comando propuesto", "plain"), ("2. Simulación de impacto: ¿qué enlaces y regiones quita?", "navy"), ("3. ¿Supera el umbral de capacidad o aísla una región entera?", "gold"),
             ("4. Ejecución limitada a una región", "teal"), ("5. Comprobación: ¿siguen alcanzables DNS y acceso fuera de banda?", "navy")]
    for i, (t, k) in enumerate(pasos):
        x = 10 + i * (w + gap)
        bx(f, x, y0 + 10, w, 110, t, k, 13, True)
        if i < 4:
            f.arrow([(x + w, y0 + 65), (x + w + gap, y0 + 65)])
    bx(f, 10 + 2 * (w + gap), y0 + 170, w, 80, "Sí: doble aprobación, ventana y plan de vuelta", "coral", 13, True)
    f.arrow([(10 + 2 * (w + gap) + w / 2, y0 + 120), (10 + 2 * (w + gap) + w / 2, y0 + 170)], "sí", color="#c0432f", label_at=(10 + 2 * (w + gap) + w / 2 + 16, y0 + 150))
    bx(f, 10 + 4 * (w + gap), y0 + 170, w, 80, "No: reversión automática y alerta", "coral", 13, True)
    f.arrow([(10 + 4 * (w + gap) + w / 2, y0 + 120), (10 + 4 * (w + gap) + w / 2, y0 + 170)], "no", color="#c0432f", label_at=(10 + 4 * (w + gap) + w / 2 + 16, y0 + 150))
    return done(f, y0 + 266,
                "Lo que enseña: la barrera no confía en que quien manda el comando haya acertado ni en que la auditoría clásica no tenga errores: simula antes y comprueba después, con una señal independiente (alcanzabilidad del DNS y del acceso de emergencia). Es diseño propio; los umbrales dependen de cada red.",
                "teal", ANALISIS)


def comparable() -> Fig:
    f, y = sketch("El mismo patrón en dos redes: Google en 2019 y Facebook en 2021",
                  "Dos filas de cinco cajas que comparan el incidente de Google Cloud del 2 de junio de 2019 con el apagón de Facebook del 4 de octubre de 2021: un mantenimiento, un alcance mayor del previsto, un plano de control que retira rutas, herramientas de depuración afectadas y acceso físico a instalaciones seguras.")
    y0 = y + 6
    cols = ["Mantenimiento", "Alcance mayor del esperado", "Plano de control", "Herramientas", "Acceso físico y duración"]
    google = ["Un evento de mantenimiento en una ubicación", "Un error del software de mantenimiento desprograma clústeres en varias ubicaciones", "Tras unos minutos se retiran las rutas BGP entre ubicaciones", "La depuración se ve dificultada por herramientas que compiten por la red congestionada", "Ingenieros viajan a instalaciones seguras; de 3 h 19 min a 4 h 25 min"]
    meta = ["Mantenimiento rutinario: un comando para evaluar capacidad", "Desconecta todas las conexiones de la red troncal; la auditoría tiene un error", "El DNS retira sus anuncios BGP al verse aislado", "Herramientas internas rotas sin DNS; acceso primario y fuera de banda caídos", "Ingenieros en las instalaciones, de acceso difícil; unas seis horas"]
    w, gap = 170, 15
    for i, c in enumerate(cols):
        x = 10 + i * (w + gap)
        f.text(x + w / 2, y0 + 12, c, 13, "middle", 700, "#142231")
        bx(f, x, y0 + 26, w, 124, google[i], "plain", 13)
        bx(f, x, y0 + 176, w, 124, meta[i], "coral", 13)
    f.text(470, y0 + 168, "Arriba: Google Cloud, 2 de junio de 2019 · Abajo: Facebook, 4 de octubre de 2021", 13, "middle", 700, "#142231")
    return done(f, y0 + 316,
                "Lo que enseña: dos empresas con redes muy distintas y el mismo mecanismo: un cambio de mantenimiento con más alcance del previsto, un plano de control que dejó de anunciar rutas y una depuración dificultada porque las herramientas vivían en la red afectada. La fila de arriba es Google (2019).",
                "gold", "Fuente: " + GOOGLE + "; Meta Engineering (5 de octubre de 2021). La comparación es análisis propio.")


FIGURES = {
    "meta-2021-contexto.svg": contexto,
    "meta-2021-cadena-causal.svg": cadena,
    "meta-2021-circulo-de-dependencias.svg": circulo,
    "meta-2021-linea-de-tiempo.svg": tiempos,
    "meta-2021-alcance.svg": alcance,
    "meta-2021-mejoras.svg": mejoras,
    "meta-2021-planos-compartidos.svg": planos,
    "meta-2021-regla-de-salud.svg": estados,
    "meta-2021-secuencia.svg": secuencia,
    "meta-2021-radio-de-explosion.svg": radio,
    "meta-2021-dependencias.svg": dependencias,
    "meta-2021-defensa-en-profundidad.svg": defensa,
    "meta-2021-arbol-de-fallas.svg": arbol,
    "meta-2021-primeros-20-minutos.svg": veinte_minutos,
    "meta-2021-tormenta-de-reintentos.svg": reintentos,
    "meta-2021-arquitectura-despues.svg": despues,
    "meta-2021-barrera-de-alcance.svg": barrera,
    "meta-2021-mismo-patron-dos-veces.svg": comparable,
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
