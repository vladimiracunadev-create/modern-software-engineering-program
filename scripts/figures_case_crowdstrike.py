"""Figures for the failure case study casos/fallo/crowdstrike.md.

Every number comes from a cited public source: the CrowdStrike Root Cause Analysis of Channel File 291
(6 Aug 2024), its preliminary Post Incident Review and the BBC report on the Parametrix estimate.
"""
from __future__ import annotations

from figure_kit import Fig, _kit_finish, _kit_start, _wrap, stacked_bars, timeline

FUENTE = "Fuente: análisis de causa raíz de CrowdStrike (6 ago 2024) y revisión preliminar del incidente; lectura propia."


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


# ------------------------------------------------------------------ 1. camino del contenido
def camino_del_contenido() -> Fig:
    f, y = sketch("El camino de un archivo de canal: de la nube de CrowdStrike al kernel de Windows",
                  "Diagrama de dos zonas. En la nube, el sistema de configuración de contenido crea instancias de plantilla, el validador las comprueba y se publica el archivo de canal 291. En el equipo Windows del cliente, el controlador csagent.sys, que corre en modo kernel, contiene el intérprete de contenido que lee ese archivo cuando Windows notifica la creación de una tubería con nombre.")
    f.group(10, y, 300, 250, "Nube de CrowdStrike", "grey")
    bx(f, 28, y + 40, 264, 56, "Content Configuration System: los ingenieros de detección crean Template Instances", "plain")
    bx(f, 28, y + 112, 264, 56, "Content Validator: comprueba cada instancia contra la definición del Template Type", "gold")
    bx(f, 28, y + 184, 264, 50, "Se publica el archivo de canal 291 (C-00000291*.sys)", "plain")
    f.arrow([(160, y + 96), (160, y + 112)])
    f.arrow([(160, y + 168), (160, y + 184)])
    f.group(360, y, 570, 250, "Equipo Windows del cliente (sensor 7.11 o superior)", "grey")
    bx(f, 380, y + 40, 530, 40, "Windows notifica la creación de una tubería con nombre (IPC)", "plain")
    f.group(380, y + 96, 530, 138, "Controlador csagent.sys (modo kernel)", "navy")
    bx(f, 396, y + 126, 240, 92, "Content Interpreter: lee el archivo de canal y compara con expresiones regulares", "coral")
    bx(f, 660, y + 126, 234, 92, "Template Type IPC: arma 20 entradas para el intérprete", "teal")
    f.arrow([(645, y + 172), (636, y + 172)])
    f.arrow([(645, y + 80), (645, y + 96)])
    f.arrow([(292, y + 209), (360, y + 209)])
    bx(f, 10, y + 266, 440, 74, "Sensor Content: viaja con el sensor. El cliente decide qué versión instala (N, N-1 o N-2).", "teal")
    bx(f, 470, y + 266, 460, 74, "Rapid Response Content: es configuración, no código, y llegó a todos los equipos conectados sin que el cliente eligiera dónde ni cuándo.", "coral")
    return done(f, y + 354, "El riesgo no estaba en el archivo en sí, sino en que un archivo de datos se interpretaba dentro del kernel y salía a toda la flota sin una puerta intermedia. Es lectura propia sobre lo que describe el informe: el informe documenta las dos rutas de entrega y que el control del cliente sobre el contenido rápido se añadió después.")


# ------------------------------------------------------------------ 2. lectura fuera de límites
def lectura_fuera_de_limites() -> Fig:
    f, y = sketch("Veintiuna entradas pedidas, veinte entregadas: la lectura que no existía",
                  "Fila de 21 casillas numeradas del 1 al 21. Las casillas 1 a 20 son punteros válidos que entrega el sensor; la casilla 21 queda fuera del arreglo y no apunta a memoria válida. El intérprete de contenido pide el índice 0x14, es decir la entrada 21, lee una dirección inválida y Windows detiene el sistema con el código PAGE_FAULT_IN_NONPAGED_AREA.")
    left, cw = 40, 40
    f.text(left, y + 14, "Arreglo de entradas que el sensor arma para el Template Type IPC", 13, "start", 700)
    for i in range(21):
        kind = "teal" if i < 20 else "coral"
        f.box(left + i * cw, y + 26, cw - 4, 40, str(i + 1), kind, 13, bold=True, radius=4)
    f.line(left - 4, y + 78, left + 20 * cw - 8, y + 78, "#087f8c", width=2)
    f.text(left + 10 * cw - 4, y + 98, "20 entradas válidas: lo que entrega el código del sensor", 13, "middle", 400, "#0b3f45")
    f.arrow([(left + 20 * cw + 14, y + 112), (left + 20 * cw + 14, y + 72)], color="#c0432f")
    f.text(left + 20 * cw - 10, y + 128, "entrada 21: no hay puntero válido", 13, "end", 700, "#5c1f14")
    bx(f, 40, y + 158, 410, 74, "La definición del Template Type declaraba 21 campos. El validador y las instancias del archivo 291 asumían 21.", "gold")
    bx(f, 490, y + 158, 410, 74, "El código del sensor pasaba 20 al intérprete. Con un comodín en el campo 21 nunca se leía; con un criterio real, sí.", "gold")
    f.arrow([(245, y + 232), (245, y + 258)])
    f.arrow([(695, y + 232), (695, y + 258)])
    bx(f, 40, y + 258, 860, 52, "Content Interpreter lee el índice 0x14 (la entrada 21) → lee una dirección inválida en csagent.sys", "coral")
    f.arrow([(470, y + 310), (470, y + 334)])
    bx(f, 40, y + 334, 860, 52, "Windows detiene el sistema (pantalla azul): PAGE_FAULT_IN_NONPAGED_AREA (0x50), módulo csagent.sys.", "navy")
    return done(f, y + 400, "La lectura fuera de límites no escribe memoria: el informe indica que no es una escritura arbitraria y que fue revisada de forma independiente. Documentado: el desajuste 21 frente a 20, el índice 0x14 y la excepción no recuperable. El bucle de reinicios aparece en la guía de remediación de CrowdStrike, no en el análisis de causa raíz.", "gold")


# ------------------------------------------------------------------ 3. línea de tiempo en días
def tiempo_en_dias() -> Fig:
    return timeline(
        "142 días entre la disponibilidad del sensor 7.11 y la caída",
        "Línea de tiempo en días desde el 28 de febrero de 2024. El sensor 7.11 está disponible desde el día 0. La primera instancia IPC se despliega el día 6, tres más entre los días 40 y 56, todas sin incidentes. El día 142 se despliegan dos instancias, una con el criterio no comodín en el campo 21, y se produce la caída.",
        [
            ("Sensor 7.11", [(0, 142, "Disponible con el Template Type IPC compilado", "teal")]),
            ("Instancias IPC", [(6, 8, "", "navy"), (40, 56, "3", "navy"), (142, 144, "", "coral")]),
            ("Resultado", [(6, 56, "sin incidentes en producción", "grey"), (142, 150, "", "coral")]),
        ],
        unit="días desde el 28 de febrero de 2024 (sensor 7.11)",
        events=[(0, "28 feb"), (6, "5 mar"), (40, "8 abr"), (56, "24 abr"), (142, "19 jul")],
        t_max=150, ticks=[0, 30, 60, 90, 120, 150], lane_h=50,
        note="Que cuatro despliegues funcionaran no probó que el quinto lo hiciera: los anteriores usaban un comodín en el campo 21 y la entrada que faltaba nunca se leyó. Los días son cálculo propio a partir de las fechas del informe.",
        foot="Fuente: revisión preliminar del incidente de CrowdStrike (julio de 2024) y análisis de causa raíz (6 ago 2024).")


# ------------------------------------------------------------------ 4. ventana de exposición
def ventana_de_exposicion() -> Fig:
    return timeline(
        "Una ventana de 78 minutos bastó para alcanzar a 8,5 millones de equipos",
        "Línea de tiempo en minutos desde las 04:00 UTC del 19 de julio de 2024. El archivo defectuoso se publica a las 04:09, minuto 9, y se revierte a las 05:27, minuto 87. Los equipos Windows con sensor 7.11 o superior conectados en esos 78 minutos lo recibieron; los que se conectaron después no.",
        [
            ("Archivo 291 defectuoso", [(9, 87, "78 min publicado", "coral")]),
            ("Equipos en línea con sensor 7.11+", [(9, 87, "reciben el archivo y caen", "coral")]),
            ("Equipos que se conectan después", [(87, 120, "no afectados", "teal")]),
        ],
        unit="minutos desde las 04:00 UTC del 19 de julio de 2024",
        events=[(9, "04:09 publicación"), (87, "05:27 reversión")],
        t_max=120, ticks=[0, 20, 40, 60, 80, 100, 120], lane_h=54, label_w=250,
        note="La reversión protegió a los equipos que se conectaron después. Los que ya habían caído solo se recuperaban si lograban descargar el archivo corregido al reiniciar; si seguían cayendo, hacía falta intervención manual (guía de remediación de CrowdStrike). Cifra de Microsoft: unos 8,5 millones de equipos Windows, menos del 1 % del total.",
        foot="Fuentes: CrowdStrike (revisión preliminar) y Microsoft (20 jul 2024). Esquema temporal propio.")


# ------------------------------------------------------------------ 5. quién asume la pérdida
def quien_asume_la_perdida() -> Fig:
    return stacked_bars(
        "Cuánto de una pérdida estimada de 5.400 millones estaba asegurada",
        "Dos barras horizontales de 5.400 millones de dólares cada una, la pérdida directa estimada por Parametrix para las 500 mayores empresas de Estados Unidos sin contar a Microsoft. En el escenario bajo, 540 millones están asegurados y 4.860 no; en el escenario alto, 1.080 millones asegurados y 4.320 no.",
        ["Escenario bajo de cobertura", "Escenario alto de cobertura"],
        [("Asegurada", [540, 1080], "teal"), ("No asegurada", [4860, 4320], "coral")],
        unit="millones de dólares", horizontal=True, label_w=230,
        note="Delta Air Lines declaró por separado un costo de más de 500 millones de dólares y demandó a CrowdStrike: es una cifra de una empresa, no se suma a la estimación de Parametrix y la demanda sigue siendo una alegación, no un hecho probado.",
        foot="Fuentes: BBC News (24 jul 2024) sobre estimación de Parametrix; CNBC (17 dic 2024) sobre la demanda de Delta.")


# ------------------------------------------------------------------ 6. antes y después
def antes_y_despues() -> Fig:
    f, y = sketch("Del reparto a toda la flota a un despliegue por anillos con control del cliente",
                  "Dos filas de cajas. La fila superior muestra el recorrido del 19 de julio: validador, publicación a todos los sensores conectados y caída de los equipos. La fila inferior muestra el recorrido prometido en el análisis de causa raíz: validador con comprobaciones nuevas, pruebas por instancia, canary, anillos con tiempo de observación y control del cliente.")
    f.text(14, y + 18, "Antes (19 de julio de 2024)", 14, "start", 700, "#5c1f14")
    bw, gap = 262, 40
    for i, (t, k) in enumerate((("Validador: acepta la instancia con un campo 21 sin respaldo", "gold"),
                                ("Publicación a todos los sensores conectados", "coral"),
                                ("Caída de los equipos Windows 7.11+ que recibieron el archivo", "coral"))):
        bx(f, 10 + i * (bw + gap), y + 30, bw, 66, t, k)
        if i:
            f.arrow([(10 + i * (bw + gap) - gap, y + 63), (10 + i * (bw + gap), y + 63)])
    f.text(14, y + 134, "Después (compromisos del análisis de causa raíz)", 14, "start", 700, "#0b3f45")
    w5, g5 = 168, 20
    pasos = (("Validador con comprobación de campos pedidos y entregados", "teal"),
             ("Prueba de cada instancia con criterios no comodín", "teal"),
             ("Canary: un grupo pequeño primero", "teal"),
             ("Anillos más amplios con tiempo de observación", "teal"),
             ("El cliente elige dónde y cuándo", "teal"))
    for i, (t, k) in enumerate(pasos):
        bx(f, 10 + i * (w5 + g5), y + 148, w5, 88, t, k)
        if i:
            f.arrow([(10 + i * (w5 + g5) - g5, y + 192), (10 + i * (w5 + g5), y + 192)])
    f.group(10, y + 256, 920, 108, "Defensas en el propio sensor", "grey")
    bx(f, 24, y + 288, 280, 62, "Comprobación de límites del arreglo (25 jul)", "plain")
    bx(f, 330, y + 288, 280, 62, "El compilador valida el número de entradas (27 jul)", "plain")
    bx(f, 636, y + 288, 280, 62, "Fuzzing de los manejadores de contenido", "plain")
    return done(f, y + 380, "Las fechas son las que informa CrowdStrike como implantadas o comprometidas al 6 de agosto de 2024. Que cada compromiso se cumpliera y fuera suficiente no lo documenta el informe: es lo que el programa llama una afirmación por verificar.", "gold")









# ==== EXPANDED FIGURES (begin) ====

# ------------------------------------------------------------------ 7. ecosistema de actores
def ecosistema_de_actores() -> Fig:
    f, y = sketch("Tres actores y dos rutas: quién entrega, quién aloja el controlador y quién asume el daño",
                  "Diagrama de contexto con tres columnas. A la izquierda, CrowdStrike: sistema de configuración, contenido del sensor y contenido de respuesta rápida. En el centro, Microsoft: núcleo de Windows y certificación de controladores. A la derecha, la organización cliente: usuarios finales, equipo Windows con el sensor y equipo de seguridad. El contenido del sensor llega con la versión que elige el cliente; el contenido rápido llega a todos los sensores en línea.")
    f.group(10, y, 300, 262, "CrowdStrike", "grey")
    bx(f, 25, y + 40, 270, 56, "Content Configuration System y Content Validator", "plain")
    bx(f, 25, y + 116, 270, 56, "Sensor Content: llega con la versión del sensor", "teal")
    bx(f, 25, y + 192, 270, 56, "Rapid Response Content: configuración desde la nube", "coral")
    f.group(325, y, 290, 124, "Microsoft", "grey")
    bx(f, 337, y + 38, 126, 72, "Núcleo de Windows (modo kernel)", "navy", 13)
    bx(f, 475, y + 38, 128, 72, "WHQL y socios del programa MVI", "plain", 13)
    f.group(630, y, 300, 262, "Organización cliente", "grey")
    bx(f, 645, y + 40, 270, 56, "Usuarios finales, pacientes y pasajeros", "plain")
    bx(f, 645, y + 116, 270, 56, "Equipo Windows con sensor y controlador", "gold")
    bx(f, 645, y + 192, 270, 56, "Equipo de seguridad: política N, N-1, N-2", "teal")
    f.arrow([(295, y + 68), (325, y + 68)], dashed=True)
    f.arrow([(295, y + 144), (645, y + 144)], "con la versión que elige el cliente", label_at=(470, y + 136))
    f.arrow([(295, y + 220), (620, y + 220), (620, y + 164), (645, y + 164)], "a todos los sensores en línea", color="#c0432f", label_at=(455, y + 212))
    f.arrow([(780, y + 192), (780, y + 172)], dashed=True)
    f.arrow([(780, y + 116), (780, y + 96)])
    return done(f, y + 282, "El contenido del sensor pasaba por la decisión del cliente; el rápido no. Microsoft aparece como el actor que aloja el controlador y certifica versiones del sensor: ahí se detiene el equipo cuando el controlador falla.")


# ------------------------------------------------------------------ 8. contenedores
def contenedores_nube_y_sensor() -> Fig:
    f, y = sketch("Contenedores: lo que vive en la nube y lo que vive, con distinto privilegio, en el equipo",
                  "Diagrama de contenedores. En la nube: sistema de configuración de contenido, validador y distribución de archivos de canal. En el equipo Windows: aplicaciones de negocio en modo usuario; en modo kernel, el controlador csagent.sys y el intérprete de contenido con el motor de detección; y, en disco, los archivos de canal que el intérprete lee.")
    f.group(10, y, 320, 262, "Nube de CrowdStrike", "grey")
    bx(f, 28, y + 40, 284, 56, "Content Configuration System: crea Template Instances", "plain")
    bx(f, 28, y + 116, 284, 56, "Content Validator: comprueba la instancia", "gold")
    bx(f, 28, y + 192, 284, 56, "Distribución de archivos de canal", "plain")
    f.arrow([(170, y + 96), (170, y + 116)])
    f.arrow([(170, y + 172), (170, y + 192)])
    f.group(350, y, 580, 340, "Equipo Windows del cliente", "grey")
    bx(f, 366, y + 36, 548, 40, "Aplicaciones de negocio (modo usuario)", "plain")
    f.group(366, y + 92, 548, 170, "Modo kernel", "navy")
    bx(f, 382, y + 126, 250, 110, "csagent.sys: controlador de filtro que recibe las notificaciones de Windows", "teal")
    bx(f, 652, y + 126, 246, 110, "Content Interpreter y Sensor Detection Engine: código C++ del sensor", "coral")
    f.arrow([(632, y + 181), (652, y + 181)])
    bx(f, 366, y + 280, 548, 44, "Archivos de canal en disco, carpeta de CrowdStrike en System32 drivers", "gold")
    f.arrow([(775, y + 280), (775, y + 236)])
    f.arrow([(312, y + 220), (336, y + 220), (336, y + 302), (366, y + 302)])
    return done(f, y + 360, "Solo el rectángulo coral, el intérprete, detiene el sistema operativo entero cuando lee mal. Todo lo demás, incluida la nube, puede fallar sin parar el equipo.")


# ------------------------------------------------------------------ 9. componentes del flujo crítico
def componentes_del_flujo() -> Fig:
    f, y = sketch("Una cuenta, seis creencias: qué suponía cada componente sobre el número de entradas",
                  "Cadena vertical de seis componentes unidos por flechas. La definición de tipos declara 21 campos; la interfaz de creación y el validador suponen 21; el código de integración del sensor entrega 20; el intérprete pide el índice 21 sin comprobar límites; Windows detiene el sistema. Cada componente muestra el número que creía y si comprobaba la cuenta.")
    rows = [
        ("Archivo Template Type Definitions: define los campos del tipo", "declara 21", "teal", "plain", "sin comprobación al compilar"),
        ("Interfaz de creación de instancias, generada de esa definición", "ofrece 21", "teal", "plain", "usa la misma definición"),
        ("Content Validator: evalúa cada instancia contra la definición", "asume 21", "teal", "gold", "no comprueba lo que entrega el código"),
        ("Código de integración del sensor: arma el arreglo de entradas", "entrega 20", "coral", "gold", "no se comparaba con la definición"),
        ("Content Interpreter: lee la entrada por índice", "pide el 21", "coral", "coral", "sin comprobación de límites"),
        ("Windows: ante lectura inválida en kernel", "detiene el sistema", "navy", "navy", "regla del sistema operativo"),
    ]
    cy = y + 4
    for i, (name, badge, bk, rk, verdict) in enumerate(rows):
        bx(f, 10, cy, 400, 58, name, "plain")
        bx(f, 440, cy + 6, 130, 46, badge, bk, 13, bold=True)
        bx(f, 600, cy + 6, 330, 46, verdict, rk if rk != "plain" else "plain")
        if i < len(rows) - 1:
            f.arrow([(210, cy + 58), (210, cy + 78)])
        cy += 78
    return done(f, cy, "El desajuste nace entre las filas 1 y 4 y se vuelve daño en la 5. Las tres primeras filas comparten la misma suposición; por eso sumar controles que la comparten no agrega protección.")


# ------------------------------------------------------------------ 10. secuencia
def secuencia_del_19_de_julio() -> Fig:
    f, y = sketch("Secuencia del 19 de julio de 2024: del archivo publicado a la pantalla azul",
                  "Diagrama de secuencia con cuatro líneas de vida: ingeniería de detección, sistema de configuración con validador, sensor en el equipo y Windows. Se crean dos instancias, el validador las aprueba, a las 04:09 UTC se publica el archivo de canal 291, el sensor lo guarda, Windows notifica una tubería con nombre, el intérprete lee la entrada 21 y Windows detiene el sistema; a las 05:27 UTC se revierte el archivo.")
    xs = [110, 345, 600, 830]
    names = ["Ingeniería de detección", "Configuración y validador", "Sensor en el equipo", "Windows"]
    for x, n in zip(xs, names):
        bx(f, x - 100, y, 200, 44, n, "navy", 13, bold=True)
        f.line(x, y + 44, x, y + 610, "#8a9aa3", dashed=True)
    def msg(yy, a, b, text, color="#32505f"):
        f.arrow([(xs[a], y + yy), (xs[b], y + yy)], color=color)
        f.text((xs[a] + xs[b]) / 2, y + yy - 22, text, 13, "middle", 400)
    msg(96, 0, 1, "1  crea dos instancias IPC\nuna con criterio real en el campo 21")
    bx(f, xs[1] - 100, y + 112, 200, 50, "2  el validador aprueba: supone 21", "gold", 13)
    msg(214, 1, 2, "3  04:09 UTC publica el\narchivo de canal 291")
    bx(f, xs[2] - 100, y + 230, 200, 50, "4  guarda el archivo en disco", "plain", 13)
    msg(330, 3, 2, "5  notifica una tubería\ncon nombre (evento IPC)")
    bx(f, xs[2] - 100, y + 346, 200, 50, "6  el intérprete pide la entrada 21 de 20", "coral", 13)
    msg(450, 2, 3, "7  lectura de dirección inválida", "#c0432f")
    bx(f, xs[3] - 100, y + 466, 200, 50, "8  detiene el sistema (0x50)", "navy", 13)
    bx(f, xs[1] - 100, y + 540, 200, 50, "9  05:27 UTC revierte (78 min)", "teal", 13)
    return done(f, y + 630, "El defecto no se activa al llegar el archivo sino en el siguiente evento de tubería con nombre. El intervalo entre el paso 3 y el 5 no es público y varía por equipo.")


# ------------------------------------------------------------------ 11. modelo de datos
def modelo_de_datos() -> Fig:
    f, y = sketch("Modelo de datos: tipo, instancia, archivo y arreglo de entradas, con sus cardinalidades",
                  "Cuatro entidades. Template Type: definición de 21 campos compilada también en el sensor. Template Instance: criterios por campo, muchas por tipo. Channel File 291: agrupa instancias de un tipo. Arreglo de entradas: se crea en cada evento de Windows con 20 punteros a estructuras de búfer y tamaño. El intérprete compara el arreglo con las instancias y el campo 21 no tiene entrada.")
    def ent(x, yy, w, title, lines, kind="plain", h=130):
        bx(f, x, yy, w, 34, title, "navy", 13, bold=True)
        fill = kind
        bx(f, x, yy + 34, w, h - 34, lines, fill, 13)
    ent(10, y + 6, 280, "Template Type", "21 campos declarados\nse compila en el sensor\ncambiar exige nuevo sensor", "teal")
    ent(330, y + 6, 280, "Template Instance", "criterios regex por campo\ncampo 21: comodín o criterio real\nes contenido, no código", "plain")
    ent(650, y + 6, 280, "Channel File 291", "agrupa instancias IPC\nse escribe en disco\nse lee en cada evento", "gold")
    f.arrow([(290, y + 70), (330, y + 70)], "1 a n", label_at=(310, y + 58))
    f.arrow([(610, y + 70), (650, y + 70)], "n a 1", label_at=(630, y + 58))
    ent(10, y + 200, 280, "Código de integración", "entrega 20 entradas al intérprete\nno se comparaba con el tipo", "coral")
    ent(330, y + 200, 280, "Arreglo de entradas", "se crea por evento de Windows\n20 punteros; cada uno apunta a\nbúfer y tamaño", "coral")
    ent(650, y + 200, 280, "Content Interpreter", "compara arreglo e instancias\nlee por índice; 0x14 es la\nentrada 21", "coral")
    f.arrow([(290, y + 265), (330, y + 265)], "arma", label_at=(310, y + 253))
    f.arrow([(610, y + 265), (650, y + 265)], "lee", label_at=(630, y + 253))
    f.arrow([(150, y + 136), (150, y + 200)], dashed=True, label="debía coincidir", label_at=(162, y + 172), label_anchor="start")
    f.arrow([(790, y + 136), (790, y + 200)], label="le indica el índice", label_at=(802, y + 172), label_anchor="start")
    return done(f, y + 350, "Las dos flechas verticales son las relaciones que importan. La de la izquierda, punteada, nadie la comprobaba; la de la derecha trae el índice 0x14 desde el contenido hasta el intérprete.")


# ------------------------------------------------------------------ 12. despliegue
def despliegue_por_rutas() -> Fig:
    f, y = sketch("Dos rutas de despliegue: seis puertas para el sensor, una sola para el contenido rápido",
                  "Dos columnas. Ruta del sensor: pruebas automáticas, uso interno, adoptantes tempranos, disponibilidad general y política de versión del cliente. Ruta del contenido rápido en julio de 2024: creación, validación y publicación a todos los sensores conectados. Debajo, tres puertas que se añadieron después: canary, anillos con tiempo de observación y control del cliente.")
    f.group(10, y, 450, 420, "Ruta del sensor (Sensor Content)", "grey")
    sens = ["Pruebas automáticas: unitarias, integración, rendimiento, esfuerzo", "Uso interno de CrowdStrike (dogfooding)", "Adoptantes tempranos", "Disponibilidad general", "Política del cliente: N, N-1 o N-2"]
    cy = y + 40
    for i, t in enumerate(sens):
        bx(f, 30, cy, 410, 54, t, "teal")
        if i < len(sens) - 1:
            f.arrow([(235, cy + 54), (235, cy + 74)])
        cy += 74
    f.group(480, y, 450, 420, "Ruta del contenido rápido (julio de 2024)", "grey")
    bx(f, 500, y + 40, 410, 54, "Creación de la instancia en el sistema de configuración", "plain")
    f.arrow([(705, y + 94), (705, y + 114)])
    bx(f, 500, y + 114, 410, 54, "Content Validator", "gold")
    f.arrow([(705, y + 168), (705, y + 188)])
    bx(f, 500, y + 188, 410, 54, "Publicación a todos los sensores en línea", "coral")
    bx(f, 500, y + 262, 410, 40, "Añadido después: canary", "teal", dashed=True)
    bx(f, 500, y + 312, 410, 40, "Añadido después: anillos con tiempo de observación", "teal", dashed=True)
    bx(f, 500, y + 362, 410, 40, "Añadido después: control del cliente", "teal", dashed=True)
    return done(f, y + 440, "Contar puertas es una lectura cualitativa: el informe no mide tiempos ni esfuerzo de cada etapa. Lo documentado es que en julio de 2024 el contenido rápido no tenía despliegue por etapas ni elección del cliente.")


# ------------------------------------------------------------------ 13. puntos únicos de fallo
def puntos_unicos_de_fallo() -> Fig:
    f, y = sketch("Dependencias del equipo del cliente: cuatro puntos únicos de fallo en una sola pila",
                  "Pila de capas. Arriba, aplicaciones de negocio y administración remota. Debajo, el núcleo de Windows, punto único de fallo. Debajo, el controlador con el intérprete, punto único de fallo. Debajo, el archivo de canal en disco, punto único de fallo. A la izquierda, la distribución desde la nube, punto único de fallo. A la derecha, la recuperación por red.")
    bx(f, 200, y + 4, 250, 56, "Aplicaciones de negocio y mostradores", "plain")
    bx(f, 470, y + 4, 260, 56, "Administración remota del equipo", "plain")
    bx(f, 200, y + 90, 530, 56, "Núcleo de Windows: un fallo en kernel detiene todo lo de arriba", "coral", bold=True)
    bx(f, 200, y + 176, 530, 56, "csagent.sys con el intérprete de contenido", "coral", bold=True)
    bx(f, 200, y + 262, 530, 56, "Archivo de canal 291 activo, sin versión buena de respaldo documentada", "coral", bold=True)
    bx(f, 10, y + 262, 160, 56, "Nube: distribución única", "coral", bold=True)
    bx(f, 760, y + 176, 170, 74, "Recuperación: depende de arrancar y descargar", "gold")
    for x in (325, 600):
        f.arrow([(x, y + 90), (x, y + 60)], dashed=True)
    f.arrow([(465, y + 176), (465, y + 146)], dashed=True)
    f.arrow([(465, y + 262), (465, y + 232)], dashed=True)
    f.arrow([(170, y + 290), (200, y + 290)])
    f.arrow([(760, y + 213), (730, y + 213)], dashed=True)
    return done(f, y + 340, "Las flechas punteadas significan «si cae, arrastra». Los cuatro nodos coral son estructura, no probabilidad: que un punto único exista no dice con qué frecuencia falla.")


# ------------------------------------------------------------------ 14. defensa en profundidad
def defensa_en_profundidad() -> Fig:
    f, y = sketch("Diez capas de control: el defecto atravesó nueve y la décima solo detuvo el equipo",
                  "Diez columnas en dos filas. Cada una nombra una capa de control y qué ocurrió el 19 de julio. La compilación no comprobaba la cuenta, las pruebas usaron comodín, la prueba de esfuerzo cubrió una instancia, el validador asumió 21, la certificación cubre la versión del sensor, no había prueba de cada instancia, canary ni control del cliente, el intérprete no comprobaba límites y Windows detuvo el sistema.")
    cells = [
        ("1 Compilación", "No comprobaba que la cuenta de campos coincidiera", "coral"),
        ("2 Pruebas del tipo", "12 casos fijos; comodín en el campo 21", "coral"),
        ("3 Prueba de esfuerzo", "Una instancia de prueba, 5 de marzo", "coral"),
        ("4 Content Validator", "Evaluó suponiendo 21 entradas", "coral"),
        ("5 Certificación WHQL", "Cubre la versión del sensor con los archivos vigentes entonces", "grey"),
        ("6 Prueba de cada instancia", "No se probaba contra el intérprete real", "coral"),
        ("7 Canary y anillos", "No existían para el contenido rápido", "coral"),
        ("8 Control del cliente", "Regía el sensor, no el contenido rápido", "coral"),
        ("9 Límites en el intérprete", "No había comprobación de índice", "coral"),
        ("10 Windows", "Detuvo el equipo: protege la integridad, no la disponibilidad", "navy"),
    ]
    w, g = 176, 10
    for i, (t, r, k) in enumerate(cells):
        row, col = divmod(i, 5)
        x = 10 + col * (w + g)
        yy = y + 8 + row * 190
        bx(f, x, yy, w, 58, t, "plain", 13, bold=True)
        bx(f, x, yy + 62, w, 100, r, k, 13)
    return done(f, y + 400, "Coral: el defecto pasó por esa capa. Gris: la capa existía pero no cubría este contenido (lectura propia). Las capas 6, 7, 8 y 9 se añadieron o comprometieron después, según el análisis de causa raíz.")


# ------------------------------------------------------------------ 15. árbol de fallas
def arbol_de_fallas() -> Fig:
    f, y = sketch("Árbol de fallas: la caída masiva exige tres cosas a la vez",
                  "Árbol de fallas. El evento superior es la caída masiva de equipos Windows, con una compuerta Y de tres ramas: el defecto existe y llega al intérprete, alcanza a gran parte de la flota y el fallo ocurre en el kernel. La primera rama tiene cuatro hojas: cuenta desalineada, lectura sin límites, pruebas y validador que no lo detectaron y controles que comparten una suposición. La segunda tiene dos hojas: publicación a todos a la vez y sin control del cliente. La tercera una hoja.")
    bx(f, 320, y + 4, 300, 56, "Caída masiva de equipos Windows", "navy", 14, bold=True)
    f.line(470, y + 60, 470, y + 84)
    f.dot(470, y + 96, "Y")
    for x in (155, 470, 785):
        f.line(x, y + 112, x, y + 130)
    f.line(155, y + 112, 785, y + 112)
    bx(f, 10, y + 130, 290, 60, "El defecto existe y llega al intérprete", "plain", bold=True)
    bx(f, 325, y + 130, 290, 60, "Alcanza a gran parte de la flota", "plain", bold=True)
    bx(f, 640, y + 130, 290, 60, "El fallo ocurre en el kernel", "plain", bold=True)
    f.line(155, y + 190, 155, y + 206)
    f.line(470, y + 190, 470, y + 206)
    f.line(785, y + 190, 785, y + 206)
    f.dot(155, y + 218, "Y")
    f.dot(470, y + 218, "Y")
    leaves = [
        (10, [("Cuenta 21 frente a 20 sin comprobar (documentado)", "coral"), ("Lectura sin límites (documentado)", "coral"), ("Pruebas y validador no lo detectaron (documentado)", "coral"), ("Controles con una suposición común (inferido)", "gold")]),
        (325, [("Publicación a todos a la vez (documentado)", "coral"), ("Sin control del cliente sobre el contenido (documentado)", "coral")]),
        (640, [("Lectura inválida en kernel detiene el sistema (documentado)", "coral")]),
    ]
    for x, items in leaves:
        cy = y + 244
        f.line(x + 145, y + 230, x + 145, y + 244)
        for t, k in items:
            bx(f, x, cy, 290, 58, t, k)
            cy += 70
    return done(f, y + 244 + 70 * 4 + 6, "Para evitar el evento superior basta eliminar una de las tres ramas. La segunda (cuántos equipos) fue la que más pudo acotar el daño sin conocer el defecto.")


# ------------------------------------------------------------------ 16. arquitectura posterior
def arquitectura_despues() -> Fig:
    f, y = sketch("Arquitectura posterior: el contenido pasa por puertas y las señales de salud deciden si avanza",
                  "Pipeline de contenido con puertas: creación, validación ampliada, prueba de cada instancia contra el intérprete, canary y anillos sucesivos hasta toda la flota. Un bucle de señales de salud decide promover o retroceder y el cliente elige dónde y cuándo. En el sensor: comprobación de límites y de cuenta, versión buena de respaldo y análisis fuera del kernel.")
    steps = [("Crear instancia", "plain"), ("Validación ampliada", "teal"), ("Probar contra el intérprete real", "teal"), ("Canary", "teal"), ("Anillos con observación", "teal"), ("Toda la flota", "plain")]
    w, g = 140, 16
    for i, (t, k) in enumerate(steps):
        x = 10 + i * (w + g)
        bx(f, x, y + 8, w, 66, t, k, 13)
        if i:
            f.arrow([(x - g, y + 41), (x, y + 41)])
    bx(f, 10, y + 120, 300, 66, "Señales de salud: caídas, reinicios, latencia del anillo", "gold", 13)
    f.arrow([(160, y + 120), (160, y + 74)], dashed=True)
    bx(f, 340, y + 120, 280, 66, "Regla: promover o retroceder de forma automática", "gold", 13)
    f.arrow([(310, y + 153), (340, y + 153)])
    f.arrow([(480, y + 120), (480, y + 74)])
    bx(f, 650, y + 120, 280, 66, "El cliente decide dónde y cuándo se entrega", "teal", 13)
    f.arrow([(790, y + 120), (790, y + 74)], dashed=True)
    f.group(10, y + 216, 920, 118, "En el equipo", "grey")
    bx(f, 24, y + 248, 280, 66, "Comprobación de límites y de cuenta de entradas", "teal", 13)
    bx(f, 330, y + 248, 280, 66, "Volver a la última versión buena del archivo", "gold", 13)
    bx(f, 636, y + 248, 280, 66, "Kernel mínimo: análisis de contenido en modo usuario", "gold", 13)
    return done(f, y + 354, "Teal: comprometido o implantado por CrowdStrike o Microsoft según sus publicaciones. Dorado: propuesta de este programa que las fuentes no documentan. Vigencia actual sin verificar.")


# ------------------------------------------------------------------ 17. recuperación por equipo
def recuperacion_por_equipo() -> Fig:
    f, y = sketch("Recuperación por equipo: cada rama que no se resuelve sola termina en una persona frente a una máquina",
                  "Árbol de decisión de la recuperación. Un equipo con pantalla azul puede recuperarse solo si al reiniciar descarga el archivo revertido; si no, hay que arrancar en un entorno de recuperación, y si el disco está cifrado hace falta la clave de recuperación; luego se elimina el archivo de canal defectuoso y se reinicia. La automatización y los medios de arranque reducen pasos manuales.")
    bx(f, 330, y + 4, 280, 50, "Equipo Windows con pantalla azul", "navy", 13, bold=True)
    f.arrow([(470, y + 54), (470, y + 84)])
    bx(f, 300, y + 84, 340, 60, "¿Reinicia y descarga el archivo revertido antes de leer el malo?", "gold", 13)
    f.arrow([(300, y + 114), (190, y + 114)], "sí", label_at=(245, y + 106))
    bx(f, 10, y + 84, 180, 60, "Recuperado sin intervención", "teal", 13)
    f.arrow([(470, y + 144), (470, y + 174)], "no", label_at=(486, y + 164), label_anchor="start")
    bx(f, 300, y + 174, 340, 60, "¿El disco está cifrado con BitLocker?", "gold", 13)
    f.arrow([(640, y + 204), (730, y + 204)], "sí", label_at=(685, y + 196))
    bx(f, 730, y + 174, 200, 60, "Conseguir la clave de recuperación", "coral", 13)
    f.arrow([(470, y + 234), (470, y + 274)], "no", label_at=(486, y + 262), label_anchor="start")
    f.arrow([(830, y + 234), (830, y + 304), (640, y + 304)])
    bx(f, 300, y + 274, 340, 60, "Entorno de recuperación: eliminar el archivo C-00000291 y reiniciar", "coral", 13)
    f.arrow([(470, y + 334), (470, y + 364)])
    bx(f, 300, y + 364, 340, 50, "Equipo restablecido, uno por uno", "plain", 13)
    bx(f, 10, y + 274, 250, 90, "Reducen los pasos: técnicas automatizadas (22 jul), ISO de recuperación y USB de arranque", "teal", 13)
    f.arrow([(260, y + 304), (300, y + 304)], dashed=True)
    return done(f, y + 434, "Coral: pasos que exigen una persona en el equipo o su clave. Es una síntesis de la guía de CrowdStrike a julio de 2024, no un procedimiento operativo.")


# ------------------------------------------------------------------ 18. respuesta en semanas
def respuesta_en_semanas() -> Fig:
    return timeline(
        "De la reversión a la reforma: 123 días entre la caída y la respuesta de la plataforma",
        "Línea de tiempo en días desde el 19 de julio de 2024 con cuatro carriles. Contención: la reversión el día 0. Recuperación: técnicas automatizadas el día 3 y cerca del 99 por ciento de sensores en línea el día 10. Explicación: la revisión preliminar el día 5 y el análisis de causa raíz el día 18. Reforma: la iniciativa de resiliencia de Microsoft el día 123.",
        [
            ("Contención", [(0, 1.5, "", "coral")]),
            ("Recuperación", [(0, 3, "", "gold"), (3, 10, "", "teal")]),
            ("Explicación", [(5, 6.5, "", "navy"), (18, 19.5, "", "navy")]),
            ("Reforma de la plataforma", [(123, 125, "", "gold")]),
        ],
        unit="días desde el 19 de julio de 2024",
        events=[(0, "19 jul"), (18, "6 ago"), (123, "19 nov")],
        t_max=140, ticks=[0, 20, 40, 60, 80, 100, 120, 140], lane_h=46, label_w=200,
        note="El daño se detuvo en horas, la explicación llegó en semanas y la reforma de plataforma en meses. Los días son cálculo propio a partir de fechas publicadas; la barra dorada de recuperación va hasta la técnica automatizada del día 3.",
        foot="Fuentes: CrowdStrike (hub, 24 jul y 6 ago 2024) y Microsoft (19 nov 2024).")

# ==== EXPANDED FIGURES (end) ====

FIGURES = {
    "crowdstrike-camino-del-contenido.svg": camino_del_contenido,
    "crowdstrike-lectura-fuera-de-limites.svg": lectura_fuera_de_limites,
    "crowdstrike-142-dias-hasta-la-caida.svg": tiempo_en_dias,
    "crowdstrike-ventana-de-78-minutos.svg": ventana_de_exposicion,
    "crowdstrike-quien-asume-la-perdida.svg": quien_asume_la_perdida,
    "crowdstrike-antes-y-despues.svg": antes_y_despues,
    # expanded entries
    "crowdstrike-ecosistema-de-actores.svg": ecosistema_de_actores,
    "crowdstrike-contenedores-nube-y-sensor.svg": contenedores_nube_y_sensor,
    "crowdstrike-componentes-del-flujo-critico.svg": componentes_del_flujo,
    "crowdstrike-secuencia-del-19-de-julio.svg": secuencia_del_19_de_julio,
    "crowdstrike-modelo-de-datos.svg": modelo_de_datos,
    "crowdstrike-despliegue-por-rutas.svg": despliegue_por_rutas,
    "crowdstrike-puntos-unicos-de-fallo.svg": puntos_unicos_de_fallo,
    "crowdstrike-defensa-en-profundidad.svg": defensa_en_profundidad,
    "crowdstrike-arbol-de-fallas.svg": arbol_de_fallas,
    "crowdstrike-arquitectura-despues.svg": arquitectura_despues,
    "crowdstrike-recuperacion-por-equipo.svg": recuperacion_por_equipo,
    "crowdstrike-respuesta-en-semanas.svg": respuesta_en_semanas,
}
