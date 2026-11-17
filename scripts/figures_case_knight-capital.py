"""Figures for the failure case study Knight Capital (1 August 2012).

Every number comes from the SEC order of 16 October 2013 (Release No. 34-70694) unless the footer says it is
illustrative or own analysis. Output goes to ``casos/figures/``; the shared case build imports ``FIGURES``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_helpers_fallo import bx, done, sequence, sketch, slices, year_axis  # noqa: E402
from figure_kit import Fig, grouped_bars, line_chart, timeline  # noqa: E402

SEC = "Fuente: SEC, Release No. 34-70694 (16 de octubre de 2013)."
ANALISIS = "Análisis propio apoyado en el informe de la SEC; no es una conclusión del regulador."
DIDACTICO = "Modelo didáctico con valores ilustrativos: no son datos medidos de Knight."


# ------------------------------------------------------------------ 1. contexto
def contexto() -> Fig:
    f, y = sketch("Dónde estaba Knight: entre los clientes y las bolsas",
                  "Diagrama de contexto: brokers y clientes institucionales envían órdenes a Knight; dentro de Knight el router SMARS divide cada orden madre en órdenes hijas y las envía a las bolsas y otros centros de negociación. Knight representaba cerca del diez por ciento de la negociación de acciones cotizadas en Estados Unidos y SMARS cerca del uno por ciento.")
    y0 = y + 4
    bx(f, 10, y0 + 10, 210, 90, "Brokers y clientes (minoristas e institucionales)", "plain", 13, True)
    f.group(270, y0, 400, 190, "Knight Capital Americas (Jersey City)", "grey")
    bx(f, 290, y0 + 36, 170, 56, "Interfaz de cliente y gestor de órdenes", "teal")
    bx(f, 480, y0 + 36, 170, 56, "SMARS: router algorítmico", "coral", 13, True)
    bx(f, 290, y0 + 112, 170, 56, "PMON: monitor de posiciones (después de ejecutar)", "gold")
    bx(f, 480, y0 + 112, 170, 56, "Cuenta 33 (posiciones sin casar)", "gold")
    bx(f, 720, y0 + 10, 210, 90, "NYSE, Nasdaq y otros centros de negociación", "plain", 13, True)
    f.arrow([(220, y0 + 55), (270, y0 + 55)], "órdenes", label_at=(245, y0 + 40))
    f.arrow([(670, y0 + 64), (720, y0 + 64)], "hijas", label_at=(695, y0 + 50))
    f.arrow([(720, y0 + 84), (670, y0 + 84)], "ejecuciones", dashed=True, label_at=(695, y0 + 114))
    bx(f, 10, y0 + 120, 250, 92, "Knight ≈ 10 % de toda la negociación de acciones cotizadas en EE. UU.; SMARS ≈ 1 % o más", "navy", 13, True)
    return done(f, y0 + 222,
                "Lo que enseña: el router era un componente interno entre la entrada de órdenes y el mercado. Un error ahí sale directamente al exterior, sin que ningún control posterior lo retenga. Los controles previos (interfaz, gestor de órdenes) protegían la entrada, no la salida de SMARS.",
                "gold", SEC + " Párrafos 11, 12 y 20. Participaciones de 2011 y 2012.")


# ------------------------------------------------------------------ 2. contenedores y capas de control
def capas() -> Fig:
    f, y = sketch("Cadena de la orden dentro de Knight: dónde había control y dónde no",
                  "Cadena horizontal de cinco etapas por las que pasa una orden: interfaz de cliente, gestor interno de órdenes, ejecución interna, router SMARS y bolsa; las tres primeras llevan control contra órdenes erróneas, SMARS no controla su propia salida, y debajo la capa de monitoreo posterior PMON y la cuenta 33 observan sin poder bloquear.")
    y0 = y + 8
    etapas = [("Interfaz de cliente", "teal", "control de entrada de órdenes erróneas"),
              ("Gestor interno de órdenes", "teal", "control de entrada de órdenes erróneas"),
              ("Ejecución interna de órdenes de clientes", "teal", "control de entrada de órdenes erróneas"),
              ("SMARS: router (órdenes madre → hijas)", "coral", "sin control de salida ni parada propia"),
              ("Bolsas y centros de negociación", "plain", "validaciones del propio mercado")]
    w, gap = 160, 28
    for i, (nombre, kind, ctrl) in enumerate(etapas):
        x = 10 + i * (w + gap)
        bx(f, x, y0, w, 80, nombre, kind, 13, True)
        bx(f, x, y0 + 100, w, 70, ctrl, "teal" if kind == "teal" else ("coral" if kind == "coral" else "grey"), 13)
        f.arrow([(x + w / 2, y0 + 80), (x + w / 2, y0 + 100)], dashed=True)
        if i < 4:
            f.arrow([(x + w, y0 + 40), (x + w + gap, y0 + 40)])
    f.text(14, y0 + 200, "Después de ejecutar (no está en la ruta de salida):", 13, "start", 700, "#142231")
    bx(f, 10, y0 + 214, 300, 72, "PMON: monitor de posiciones; depende de una persona, sin alertas automáticas", "gold")
    bx(f, 330, y0 + 214, 300, 72, "Cuenta 33: límite bruto de 2 millones sin enlace a controles automáticos", "gold")
    bx(f, 650, y0 + 214, 280, 72, "Correos «Power Peg disabled»: no eran alertas", "gold")
    f.arrow([(560, y0 + 214), (620, y0 + 170)], dashed=True, color="#c0432f")
    return done(f, y0 + 300,
                "Lo que enseña: los controles de Knight estaban donde las órdenes entraban y donde se medían las posiciones, no en el único punto por el que todo lo erróneo salía al mercado. La SEC exige un control inmediatamente antes de enviar al mercado.",
                "gold", SEC + " Párrafos 20 a 25, 38.")


# ------------------------------------------------------------------ 3. componentes de SMARS
def componentes() -> Fig:
    f, y = sketch("Dentro de SMARS: qué hacía cada pieza y cuál se había quedado sin su freno",
                  "Diagrama de componentes de SMARS: recepción de órdenes madre, selector de funcionalidad por indicador, código nuevo del RLP, código antiguo Power Peg, función de cantidad acumulada movida en 2005, emisor de órdenes hijas y receptor de ejecuciones. El indicador activa Power Peg en el servidor sin el código nuevo y la cantidad acumulada ya no frena el emisor.")
    y0 = y + 6
    f.group(10, y0, 920, 270, "Un servidor SMARS (modelo funcional construido con lo que describe la SEC)", "grey")
    bx(f, 30, y0 + 50, 160, 70, "Recepción de órdenes madre", "plain", 13, True)
    bx(f, 230, y0 + 50, 170, 70, "Selector por indicador (flag reutilizado)", "gold", 13, True)
    bx(f, 450, y0 + 40, 200, 56, "Código RLP nuevo (7 servidores)", "teal")
    bx(f, 450, y0 + 108, 200, 56, "Código Power Peg de 2003 (8.º servidor)", "coral", 13, True)
    bx(f, 700, y0 + 50, 200, 70, "Emisor de órdenes hijas hacia los centros", "plain", 13, True)
    bx(f, 450, y0 + 190, 200, 60, "Cantidad acumulada (movida en 2005, sin retest)", "gold")
    bx(f, 700, y0 + 190, 200, 60, "Receptor de ejecuciones de los centros", "plain")
    f.arrow([(190, y0 + 85), (230, y0 + 85)])
    f.arrow([(400, y0 + 70), (450, y0 + 68)], "sí", label_at=(425, y0 + 56))
    f.arrow([(400, y0 + 100), (450, y0 + 136)], "sí", label_at=(412, y0 + 128))
    f.arrow([(650, y0 + 68), (700, y0 + 78)])
    f.arrow([(650, y0 + 136), (700, y0 + 100)], color="#c0432f")
    f.arrow([(800, y0 + 190), (800, y0 + 120)], "relleno", dashed=True, label_at=(836, y0 + 160))
    f.arrow([(700, y0 + 220), (650, y0 + 220)], dashed=True)
    f.arrow([(550, y0 + 190), (550, y0 + 164)], "ya no frena", dashed=True, color="#c0432f", label_at=(600, y0 + 180))
    return done(f, y0 + 282,
                "Lo que enseña: la parada de Power Peg dependía de una función interna, no de un invariante del router. Al moverla de sitio sin repetir pruebas, el emisor quedó sin freno; el selector por indicador decidía en cada servidor qué código despertaba.",
                "coral", SEC + " Párrafos 12 a 16. Esquema funcional propio; la orden no publica el diseño interno.")


# ------------------------------------------------------------------ 4. secuencia del flujo que falló
def secuencia() -> Fig:
    f, y = sketch("Secuencia de la mañana del 1 de agosto de 2012, paso a paso",
                  "Diagrama de secuencia con cinco participantes: brokers, gestor de órdenes, SMARS en el octavo servidor, bolsas y el personal de Knight. Las órdenes llegan con el indicador reutilizado, SMARS envía hijas sin parar, las bolsas ejecutan, la cuenta 33 acumula, el personal ve las posiciones y, al desinstalar el código nuevo, el problema empeora.")
    y0 = y + 6
    lanes = [("Brokers (clientes RLP)", "plain"), ("Gestor de órdenes", "teal"), ("SMARS, servidor 8", "coral"),
             ("Bolsas", "plain"), ("Personal de Knight", "gold")]
    steps = [(0, 1, "212 órdenes madre"), (1, 2, "pasa las madre"),
             (2, 3, "hijas sin parar"), (3, 2, "ejecuciones", "dashed"),
             (1, 2, "completa: no avisa", "red"), (2, 2, "cuenta 33 acumula", "note"),
             (4, 4, "ven posiciones", "note"), (4, 2, "desinstalan RLP en 7 servidores", "red"),
             (2, 3, "más hijas (Power Peg)", "red"), (4, 3, "parada tras ≈ 45 min")]
    yy = sequence(f, y0, lanes, steps, row_h=34)
    return done(f, yy,
                "Lo que enseña: en toda la secuencia ningún participante tenía autoridad automática para parar a SMARS. Las personas vieron las posiciones pero el único medio disponible fue cambiar el software en caliente; el paso 8 muestra por qué eso es otro cambio de producción.",
                "coral", SEC + " Párrafos 16, 24, 25 y 27. El orden fino de los pasos 5 a 8 es una reconstrucción; la orden no da horas.")


# ------------------------------------------------------------------ 5. modelo de datos
def datos() -> Fig:
    f, y = sketch("Modelo de datos: la orden madre, sus hijas y la cuenta que acumuló lo que nadie casaba",
                  "Esquema de datos: una orden madre con cantidad y bandera genera muchas órdenes hijas; cada ejecución vuelve y se imputa a la madre en el gestor de órdenes; las ejecuciones que no se pueden casar con la cantidad pendiente de una madre caen en la cuenta 33, que PMON muestra sin los límites.")
    y0 = y + 6
    bx(f, 10, y0, 220, 100, "Orden madre: valor, cantidad, precio límite, bandera; ya estaba completada en el gestor", "plain")
    bx(f, 300, y0, 220, 100, "Orden hija: porción enviada a un centro; en el servidor 8, sin tope de cantidad total", "coral")
    bx(f, 600, y0, 150, 100, "Ejecución (relleno) devuelta por el centro", "plain")
    bx(f, 790, y0, 140, 100, "Cuenta 33: lo que no casa; tope bruto de 2 M", "gold", 13, True)
    f.arrow([(230, y0 + 50), (300, y0 + 50)], "1 a N", label_at=(265, y0 + 38))
    f.arrow([(520, y0 + 50), (600, y0 + 50)], "1 a N", label_at=(560, y0 + 38))
    f.arrow([(750, y0 + 50), (790, y0 + 50)])
    bx(f, 10, y0 + 150, 330, 78, "Gestor de órdenes: sabe que la madre está completa, pero no se lo dice a SMARS", "navy")
    bx(f, 400, y0 + 150, 250, 78, "PMON: muestra posiciones, no muestra los límites; con retardo y cifras inexactas", "gold")
    bx(f, 700, y0 + 150, 230, 78, "Límite de 2 M sin enlace a capital agregado", "coral")
    f.arrow([(120, y0 + 100), (120, y0 + 150)], dashed=True)
    f.arrow([(860, y0 + 100), (860, y0 + 150)], dashed=True)
    f.arrow([(790, y0 + 80), (650, y0 + 170)], dashed=True)
    return done(f, y0 + 244,
                "Lo que enseña: el dato correcto («la madre está completa») existía en el sistema, pero en un lugar que no tenía permiso para frenar al router. Un dato que no viaja al punto de decisión no protege. La cuenta 33 mezclaba orígenes: por eso el personal tardó en identificar la fuente.",
                "gold", SEC + " Párrafos 16, 23 a 25. Los nombres de campos son descriptivos, no los del sistema real.")


# ------------------------------------------------------------------ 6. despliegue
def servidores() -> Fig:
    f, y = sketch("Ocho servidores de SMARS: siete con código nuevo y uno con código viejo",
                  "Diagrama de despliegue: el código nuevo del Retail Liquidity Program se copió en siete de los ocho servidores de SMARS; en el octavo siguió presente el código Power Peg, abandonado en 2003, que reutilizaba el mismo indicador de activación.")
    y0 = y + 6
    f.text(14, y0 + 14, "Despliegue escalonado desde el 27 de julio de 2012 (un técnico, sin segunda revisión)", 13, "start", 700, "#142231")
    w, gap = 100, 9
    for i in range(8):
        x = 14 + i * (w + gap)
        old = i == 7
        bx(f, x, y0 + 34, w, 86, f"Servidor {i + 1}\n" + ("Power Peg vivo, sin RLP" if old else "RLP nuevo"), "coral" if old else "teal", 13, old)
    f.text(14, y0 + 148, "Llega una orden con el indicador reutilizado en «sí»:", 13, "start", 700, "#142231")
    bx(f, 14, y0 + 162, 410, 70, "Servidores 1–7: se activa el RLP nuevo y la orden se procesa bien", "teal")
    bx(f, 450, y0 + 162, 470, 70, "Servidor 8: se activa Power Peg, que ya no sabía dejar de enviar órdenes hijas", "coral", 13, True)
    f.arrow([(750, y0 + 120), (750, y0 + 162)])
    f.arrow([(220, y0 + 120), (220, y0 + 162)])
    return done(f, y0 + 244,
                "Lo que enseña: el mismo indicador significaba cosas distintas según el servidor. Una versión mezclada en producción es un sistema distinto en cada nodo. Después, al desinstalar el código nuevo de los siete servidores correctos, también ellos activaron Power Peg: la reversión empeoró el problema.",
                "coral", SEC + " Párrafos 13–16 y 27.")


# ------------------------------------------------------------------ 7. flujo crítico (bucle)
def bucle() -> Fig:
    f, y = sketch("El bucle que no se detenía: la parada dependía de una cuenta que ya no estaba donde debía",
                  "Flujo de una orden madre en el servidor con Power Peg: SMARS envía órdenes hijas; los centros devuelven ejecuciones; la función de cantidad acumulada, movida a un punto anterior del código en 2005, ya no se consulta antes de enviar la siguiente hija, de modo que el envío continúa aunque la orden madre esté completa.")
    y0 = y + 6
    bx(f, 10, y0, 200, 76, "Orden madre llega con el indicador reutilizado", "plain")
    bx(f, 250, y0, 200, 76, "SMARS envía una orden hija", "coral", 13, True)
    bx(f, 490, y0, 200, 76, "El centro de negociación ejecuta y devuelve el relleno", "plain")
    bx(f, 730, y0, 200, 76, "Debería: sumar lo ejecutado y parar al completar la madre", "teal")
    f.arrow([(210, y0 + 38), (250, y0 + 38)])
    f.arrow([(450, y0 + 38), (490, y0 + 38)])
    f.arrow([(690, y0 + 38), (730, y0 + 38)])
    bx(f, 250, y0 + 130, 440, 96, "En 2005 la cuenta acumulada se movió a un punto anterior del código y Power Peg no se volvió a probar", "gold")
    bx(f, 730, y0 + 130, 200, 96, "Aquí nadie contaba: la hija siguiente salía igual", "coral", 13, True)
    f.arrow([(830, y0 + 76), (830, y0 + 130)], dashed=True, color="#c0432f")
    f.arrow([(730, y0 + 178), (690, y0 + 178)], dashed=True, color="#c0432f")
    f.arrow([(350, y0 + 130), (350, y0 + 76)], "bucle", dashed=True, color="#c0432f", label_at=(318, y0 + 108))
    bx(f, 10, y0 + 130, 200, 96, "Otra parte del sistema sabía que la madre estaba completa; no se lo dijo a SMARS", "navy")
    return done(f, y0 + 240,
                "Lo que enseña: el criterio de parada vivía en el código antiguo, no en el router como invariante. Con 212 órdenes madre eso bastó para 4 millones de ejecuciones en unos 45 minutos. Es un fallo de acoplamiento oculto entre una función y la condición que la limitaba.",
                "coral", SEC + " Párrafos 14, 16 y 17.")


# ------------------------------------------------------------------ 8. antecedentes (años)
def antecedentes() -> Fig:
    f, y = sketch("Doce años de condiciones latentes antes de la mañana del 1 de agosto",
                  "Eje de tiempo no proporcional de 2003 a 2013 con los hitos documentados: 2003 Power Peg deja de usarse pero queda en los servidores; 2005 se mueve la función de cantidad acumulada sin repetir pruebas; julio de 2011 fecha desde la que los controles no estaban bien diseñados; octubre de 2011 error con datos de prueba; marzo de 2012 certificación del consejero delegado; agosto de 2012 el incidente; 2013 fusión y orden de la SEC.")
    ev = [(0, "2003: Power Peg deja de usarse; el código queda en producción", "navy", "u", 0),
          (1, "2005: se mueve la cantidad acumulada; no se vuelve a probar", "coral", "d", 0),
          (2, "Jul 2011: fecha de cumplimiento de la regla 15c3-5", "gold", "u", 0),
          (3, "Oct 2011: datos de prueba en producción; ≈ 7,5 M", "gold", "d", 0),
          (4, "Mar 2012: certificación del CEO dice «procesos»", "gold", "u", 1),
          (5, "Ago 2012: 45 minutos, más de 460 M", "coral", "d", 0),
          (6, "Jul 2013: fusión con GETCO", "teal", "u", 2),
          (7, "Oct 2013: orden de la SEC y multa de 12 M", "teal", "d", 1)]
    n = len(ev)
    axis_y = y + 150
    f.line(30, axis_y, 910, axis_y, "#32505f", width=2)
    for i, (t, text, kind, side, level) in enumerate(ev):
        px = 80 + i * (780 / (n - 1))
        up = i % 2 == 0
        by = axis_y - 40 - 96 if up else axis_y + 40
        f.line(px, axis_y, px, by + 96 if up else by, "#8a9aa3", dashed=True)
        f.dot(px, axis_y, "", kind)
        bx(f, min(max(px - 95, 6), 934 - 190), by, 190, 96, text, kind, 13)
    yy = axis_y + 40 + 96
    return done(f, yy + 20,
                "Lo que enseña: el defecto se formó en 2005 y el despliegue de 2012 solo lo activó. Los años intermedios contienen un aviso (2011) que se cerró con un parche local. Es la forma típica de una condición latente: invisible hasta que otra condición la alinea.",
                "gold", SEC + " Párrafos 9, 11, 14, 33 y 34. Espaciado uniforme, no a escala de años.")


# ------------------------------------------------------------------ 9. ventana de despliegue
def ventana() -> Fig:
    return timeline(
        "Del 27 de julio al 1 de agosto de 2012: lo que consta y lo que no se sabe",
        "Línea de tiempo en días: el despliegue escalonado del código RLP empieza el 27 de julio y avanza servidor a servidor en días sucesivos; los días exactos de cada servidor no constan; el 1 de agosto empieza el programa de la NYSE y fallan las órdenes en el octavo servidor.",
        [("Despliegue en 7 servidores", [(0, 5, "días sucesivos sin detallar", "teal")]),
         ("Servidor 8", [(0, 5, "no recibe el código, nadie lo nota", "coral")]),
         ("Revisión de segunda persona", [(0, 5, "no existía el procedimiento", "grey")])],
        unit="Días desde el 27 de julio de 2012", events=[(0, "27 jul: empieza"), (5, "1 ago: RLP vivo")],
        ticks=[0, 1, 2, 3, 4, 5, 6], t_max=6, label_w=250,
        note="Cuántos servidores se actualizaron cada día no consta en la orden de la SEC. Lo documentado es el inicio, el final, que un técnico omitió el octavo y que no había revisión. La ventana de cinco días era una oportunidad de verificar versión en cada nodo.",
        note_kind="gold", foot=SEC + " Párrafo 15.")


# ------------------------------------------------------------------ 10. línea de tiempo
def tiempos() -> Fig:
    return timeline(
        "1 de agosto de 2012: de los correos de las 8:01 al final de los 45 minutos",
        "Línea de tiempo en minutos desde las 8:00 de la mañana hora de Nueva York: a las 8:01 empiezan 97 correos automáticos con el texto Power Peg disabled; a las 9:30 abre el mercado y comienzan los 45 minutos aproximados de ejecuciones erróneas; el final exacto no consta en la orden de la SEC.",
        [("Correos BNET «Power Peg disabled»", [(1, 90, "97 correos sin revisar", "gold")]),
         ("Ejecuciones erróneas de SMARS", [(90, 135, "≈ 45 min", "coral")]),
         ("Contención (hora no documentada)", [(90, 135, "retiran el RLP", "navy")])],
        unit="Minutos desde las 8:00 (hora de la costa este de EE. UU.)",
        events=[(90, "9:30 apertura")], ticks=[0, 30, 60, 90, 120, 150], t_max=150, label_w=250,
        note="El final de la barra roja (≈ 135 min) es 9:30 más los «aproximadamente 45 minutos» de la SEC: la hora exacta de la parada no figura en la orden. Los correos de las 8:01 fueron la ocasión documentada de detectar el despliegue defectuoso antes de abrir. Un aviso que nadie lee no es una alerta.",
        note_kind="gold", foot=SEC + " Párrafos 1, 17, 19 y 27.")


# ------------------------------------------------------------------ 11. magnitud
def magnitud() -> Fig:
    return grouped_bars(
        "La exposición fue de miles de millones; la pérdida realizada, de cientos",
        "Barras horizontales en millones de dólares: posición larga neta de unos 3 500 en 80 acciones, posición corta neta de unos 3 150 en 74 acciones y pérdida realizada de más de 460 millones tras liquidar.",
        ["Posición larga neta (80 acciones)", "Posición corta neta (74 acciones)", "Pérdida realizada"],
        [("Millones de dólares", [3500, 3150, 460], "coral")],
        unit="Millones de dólares de EE. UU. (cifras aproximadas de la SEC)", horizontal=True, label_w=270,
        ticks=[0, 1000, 2000, 3000, 4000],
        note="Knight acumuló posiciones que no quería por unos 6 650 millones brutos y las liquidó con una pérdida de más de 460 millones. La diferencia entre exposición y pérdida (inferencia: lo comprado y lo vendido se compensó en gran parte al liquidar) no tranquiliza: el capital de la firma no soportaba la diferencia: la SEC habla de problemas de capital neto.",
        note_kind="gold", foot=SEC + " La suma 3 500 + 3 150 es aritmética propia.")


# ------------------------------------------------------------------ 12. alcance en el mercado
def alcance() -> Fig:
    return grouped_bars(
        "Cuántas acciones sintieron a Knight: de 154 a 37",
        "Barras horizontales: 154 acciones con ejecuciones erróneas de Knight; 75 en las que Knight fue más del veinte por ciento del volumen con movimientos de precio mayores del cinco por ciento; 37 de ellas con movimientos de más del diez por ciento y más del cincuenta por ciento del volumen.",
        ["Acciones con ejecuciones erróneas", "Knight > 20 % del volumen y precio > 5 %", "Knight > 50 % del volumen y precio > 10 %"],
        [("Acciones", [154, 75, 37], "coral")], unit="Número de acciones", horizontal=True, label_w=300,
        ticks=[0, 40, 80, 120, 160],
        note="Las 37 acciones del último escalón son un subconjunto de las 75 del anterior. La SEC añade que algunos participantes recibieron peores precios y otros mejores: el daño al mercado no es solo de quien pierde. Cada escalón es un criterio más duro, no un periodo distinto.",
        note_kind="gold", foot=SEC + " Párrafos 1 y 18.")


# ------------------------------------------------------------------ 13. puntos únicos de fallo
def puntos_unicos() -> Fig:
    f, y = sketch("Dependencias y puntos únicos de fallo de la ruta de salida",
                  "Mapa de dependencias: el router SMARS es el único camino hacia las bolsas y depende de un indicador, de la versión desplegada en cada servidor y de una función de parada; el monitoreo depende de una persona y de PMON; las alertas dependen de correos que nadie lee. Cada punto único aparece marcado.")
    y0 = y + 6
    bx(f, 380, y0, 180, 60, "Mercado (bolsas)", "plain", 13, True)
    bx(f, 380, y0 + 100, 180, 66, "SMARS: único camino de salida", "coral", 13, True)
    bx(f, 60, y0 + 100, 220, 66, "Indicador reutilizado: dos significados", "coral")
    bx(f, 660, y0 + 100, 240, 66, "Función de cantidad acumulada: único freno", "coral")
    bx(f, 60, y0 + 210, 220, 66, "Versión por servidor: verificada a mano", "gold")
    bx(f, 380, y0 + 210, 180, 66, "Capital: sin enlace a la salida", "gold")
    bx(f, 660, y0 + 210, 240, 66, "PMON y una persona mirando", "gold")
    f.arrow([(470, y0 + 100), (470, y0 + 60)])
    f.arrow([(280, y0 + 133), (380, y0 + 133)], "decide")
    f.arrow([(660, y0 + 133), (560, y0 + 133)], "frena")
    f.arrow([(170, y0 + 210), (170, y0 + 166)], dashed=True)
    f.arrow([(470, y0 + 210), (470, y0 + 166)], "no bloquea", dashed=True, label_at=(520, y0 + 190))
    f.arrow([(780, y0 + 210), (780, y0 + 166)], "solo observa", dashed=True, label_at=(830, y0 + 190))
    return done(f, y0 + 290,
                "Lo que enseña: rojo son puntos únicos de fallo con consecuencias directas sobre el mercado; dorado son dependencias de proceso. Había cuatro elementos de los que dependía todo y ninguno tenía respaldo independiente. El mismo diseño con un segundo frenos en la salida habría sido más robusto.",
                "gold", ANALISIS)


# ------------------------------------------------------------------ 14. defensa en profundidad
def defensa() -> Fig:
    f, y = sketch("Defensa en profundidad: ocho barreras y por qué el riesgo las atravesó",
                  "Esquema de láminas con huecos: ocho barreras por las que debía pasar el defecto, de la revisión de despliegue al gobierno de cumplimiento; las barreras ausentes (revisión, alerta, control de salida, capital, guion) están en rojo y las parciales en dorado; una flecha atraviesa todos los huecos.")
    y0 = y + 6
    items = [("Revisión de segunda persona del despliegue (ausente)", "coral", 0.5),
             ("Retirada o retest del código muerto (ausente)", "coral", 0.5),
             ("Alerta sobre 97 correos (existió, sin dueño)", "gold", 0.5),
             ("Control de salida en SMARS (ausente)", "coral", 0.5),
             ("Tope de precio del 9,5 % (no cubría preapertura)", "gold", 0.5),
             ("Límite de capital agregado vinculado (ausente)", "coral", 0.5),
             ("PMON observado por personas (tardío)", "gold", 0.5),
             ("Guion de incidente y kill switch (ausente)", "coral", 0.5)]
    yy = slices(f, y0, items, x0=30, w=62, gap=51, h=170, label_h=120, label_w=104)
    ymid = y0 + 18 + 0.5 * (170 - 80) + 22
    f.arrow([(10, ymid), (930, ymid)], color="#c0432f")
    return done(f, yy,
                "Lo que enseña: ninguna barrera era perfecta, pero la clave es la alineación: no había una sola que, por sí misma, detuviera el daño. La flecha roja es el defecto activo. Cinco de las ocho no existían y tres existían sin eficacia real. Es análisis propio de la lista de deficiencias de la SEC.",
                "coral", ANALISIS + " Párrafos 15 a 27.")


# ------------------------------------------------------------------ 15. árbol de fallas
def arbol() -> Fig:
    f, y = sketch("Árbol de fallas: qué tuvo que coincidir para perder más de 460 millones",
                  "Árbol de fallas con el evento principal arriba, la pérdida de capital, que requiere dos ramas a la vez: que se enviaran órdenes erróneas y que nada las detuviera. La primera rama combina despliegue incompleto, código muerto invocable e indicador reutilizado, y la segunda cinco barreras que faltaron.")
    y0 = y + 6
    bx(f, 340, y0, 260, 52, "Pérdida de más de 460 M de dólares", "navy", 13, True)
    f.dot(470, y0 + 76, "Y", "navy")
    f.arrow([(470, y0 + 52), (470, y0 + 64)])
    bx(f, 120, y0 + 100, 280, 52, "A. SMARS envía órdenes que nadie pidió", "coral", 13, True)
    bx(f, 540, y0 + 100, 330, 52, "B. Nada lo limita ni lo detiene a tiempo", "coral", 13, True)
    f.line(470, y0 + 88, 260, y0 + 100)
    f.line(470, y0 + 88, 705, y0 + 100)
    f.dot(260, y0 + 176, "Y", "navy")
    f.line(260, y0 + 152, 260, y0 + 164)
    for i, t in enumerate(["A1. Servidor sin código nuevo", "A2. Power Peg invocable desde 2003", "A3. Indicador con dos significados"]):
        x = 20 + i * 150
        bx(f, x, y0 + 210, 140, 74, t, "gold", 13)
        f.line(260, y0 + 188, x + 70, y0 + 210)
    f.dot(705, y0 + 176, "O", "navy")
    f.line(705, y0 + 152, 705, y0 + 164)
    hojas = ["B1. Sin control de salida en SMARS", "B2. Sin límite de capital que bloquee", "B3. Alerta no atendida", "B4. Monitoreo humano tardío", "B5. Reversión sin guion empeora"]
    f.line(705, y0 + 188, 705, y0 + 312)
    f.line(105, y0 + 312, 825, y0 + 312)
    for i, t in enumerate(hojas):
        x = 20 + i * 184
        bx(f, x, y0 + 330, 170, 70, t, "gold", 13)
        f.line(x + 85, y0 + 312, x + 85, y0 + 330)
    return done(f, y0 + 412,
                "Lo que enseña: «Y» exige que ocurran todas las ramas; «O» que baste una. Aquí A necesita tres condiciones a la vez, pero B se activa con la ausencia de cualquiera de cinco barreras: por eso hay tantas formas de cortar el árbol. Cortar A1 habría evitado el incidente; cortar B1 o B2 lo habría acotado.",
                "gold", ANALISIS + " La estructura lógica es nuestra; los hechos de cada hoja son de la SEC.")


# ------------------------------------------------------------------ 16. controles
def controles() -> Fig:
    f, y = sketch("Dónde habría cortado cada control la cadena del fallo",
                  "Cadena de seis eslabones de la orden madre al capital; debajo de cada uno, el control que habría limitado el daño: segunda persona que revise el despliegue, retirada del código muerto, parada automática por desvío entre órdenes de entrada y de salida, alerta sobre los correos, límite automático de capital que bloquee el envío, y ensayo de reversión.")
    y0 = y + 6
    cadena = ["Despliegue a mano en 8 servidores", "Código muerto sigue invocable", "Orden con indicador reutilizado", "Bucle de órdenes hijas", "Posición acumulada en la cuenta 33", "Pérdida de capital"]
    controles_ = ["Segunda revisión + despliegue automatizado y verificado", "Borrar el código y sus pruebas, no reutilizar indicadores", "Nueva bandera o ruta para el RLP", "Límite de salidas frente a entradas; interruptor de parada", "Umbral de capital que bloquea el envío", "Plan de reversión ensayado y guion de incidente"]
    w, gap = 140, 20
    for i, (a, c) in enumerate(zip(cadena, controles_)):
        x = 10 + i * (w + gap)
        bx(f, x, y0, w, 92, a, "coral", 13)
        bx(f, x, y0 + 130, w, 118, c, "teal", 13)
        f.arrow([(x + w / 2, y0 + 92), (x + w / 2, y0 + 130)], dashed=True)
        if i < 5:
            f.arrow([(x + w, y0 + 46), (x + w + gap, y0 + 46)])
    f.text(14, y0 + 118, "Control que habría interrumpido el eslabón", 13, "start", 700, "#142231")
    return done(f, y0 + 262,
                "Los controles son análisis propio: la SEC señala la ausencia de cada uno de ellos como deficiencia, pero la elección concreta es nuestra. Cualquiera de los seis eslabones cortados antes de la apertura habría reducido el daño; los últimos limitan el tamaño aunque los primeros fallen.",
                "teal", ANALISIS)


# ------------------------------------------------------------------ 17. arquitectura después
def despues() -> Fig:
    f, y = sketch("Arquitectura «después»: cuatro controles independientes antes del mercado",
                  "Arquitectura objetivo propuesta: un canal de despliegue que verifica la versión en cada nodo; SMARS con invariante de parada; una puerta independiente justo antes de las bolsas con límites de cantidad, ritmo, precio y capital agregado; un interruptor de parada accesible a operaciones; y telemetría que convierte las señales en alertas con responsable.")
    y0 = y + 6
    bx(f, 10, y0, 200, 76, "Canal de despliegue: artefacto único, hash por nodo, segunda aprobación", "teal")
    bx(f, 250, y0, 190, 76, "SMARS con invariante: hijas ≤ cantidad de la madre", "teal", 13, True)
    bx(f, 480, y0, 220, 76, "Puerta previa al mercado: cantidad, ritmo, precio y capital agregado", "navy", 13, True)
    bx(f, 740, y0, 190, 76, "Bolsas y centros de negociación", "plain", 13, True)
    f.arrow([(210, y0 + 38), (250, y0 + 38)])
    f.arrow([(440, y0 + 38), (480, y0 + 38)])
    f.arrow([(700, y0 + 38), (740, y0 + 38)])
    bx(f, 10, y0 + 130, 210, 80, "Cuenta de capital agregado en línea: límite que bloquea, no que informa", "gold")
    bx(f, 260, y0 + 130, 210, 80, "Interruptor de parada: un botón con dueño, ensayado", "coral", 13, True)
    bx(f, 510, y0 + 130, 210, 80, "Telemetría: salidas frente a entradas y versión por nodo", "teal")
    bx(f, 760, y0 + 130, 170, 80, "Alerta con responsable y guion", "gold")
    f.arrow([(115, y0 + 130), (540, y0 + 76)], dashed=True)
    f.arrow([(365, y0 + 130), (590, y0 + 76)], dashed=True, color="#c0432f")
    f.arrow([(615, y0 + 130), (615, y0 + 76)], dashed=True)
    f.arrow([(720, y0 + 170), (760, y0 + 170)])
    return done(f, y0 + 226,
                "Lo que enseña: la puerta previa no depende del código de SMARS; vigila cantidades que salen, no la intención del software. Un error de SMARS no puede disfrazarse de orden válida si la puerta cuenta lo que cruza. Es una propuesta didáctica coherente con las deficiencias de la SEC, no una descripción de lo que Knight adoptó.",
                "teal", ANALISIS)


# ------------------------------------------------------------------ 18. barrera
def barrera() -> Fig:
    return line_chart(
        "Qué haría una barrera de «salidas ≤ entradas»: el mismo error, con y sin tope",
        "Modelo didáctico: cantidad acumulada de órdenes hijas enviadas como múltiplo de la cantidad de la orden madre; sin barrera crece sin límite mientras no se detenga manualmente; con una barrera que corta al llegar a una vez y media la madre se estabiliza y se emite una alerta.",
        [("Sin barrera", [(2, 0.2), (10, 1.2), (20, 4), (30, 12), (40, 35), (50, 60), (60, 100)], "coral"),
         ("Con barrera al 150 %", [(2, 0.2), (10, 1.2), (12, 1.5), (60, 1.5)], "teal")],
        x_label="Segundos desde el primer envío (modelo didáctico)", y_label="Cantidad enviada ÷ cantidad de la madre",
        point_labels="none", log_y=True, y_zero=False, y_ticks=[0.1, 1, 10, 100],
        annotations=[(12, 1.5, "la barrera corta y avisa", 40, -60)],
        hlines=[(1.0, "madre completa")],
        note="Los valores son ilustrativos: el modelo solo muestra la forma de las curvas. Lo documentado es que Knight no tenía ese control y que enviaron millones de órdenes hijas por 212 madres. La barrera funciona porque cuenta lo que sale, no lo que el software cree que debe salir.",
        note_kind="gold", foot=DIDACTICO)


# ------------------------------------------------------------------ 19. consecuencias
def consecuencias() -> Fig:
    f, y = sketch("De la pérdida a la orden de la SEC: cadena de consecuencias",
                  "Cadena de seis eslabones desde el incidente de agosto de 2012: pérdida de más de 460 millones, problemas de capital neto, financiación de 400 millones en cinco días, fusión con GETCO en julio de 2013, orden de la SEC con multa de 12 millones, y consultor independiente con revisión de ciclo de desarrollo, despliegue, routers, capital e incidentes.")
    y0 = y + 6
    pasos = [("1 ago 2012", "Pérdida de más de 460 M y posiciones de miles de millones", "coral"),
             ("1 ago 2012", "Problemas de capital neto y violaciones de Regulación SHO", "coral"),
             ("6 ago 2012", "Financiación de 400 M en acciones preferentes convertibles", "gold"),
             ("1 jul 2013", "Fusión con GETCO: nace KCG Holdings", "navy"),
             ("16 oct 2013", "Orden de la SEC: multa de 12 M, censura, cese y desistimiento", "teal"),
             ("Tras la orden", "Consultor independiente sobre software, despliegue, routers, capital e incidentes", "teal")]
    w, gap = 136, 20
    for i, (fecha, t, kind) in enumerate(pasos):
        x = 10 + i * (w + gap)
        f.text(x + w / 2, y0 + 14, fecha, 13, "middle", 700, "#142231")
        bx(f, x, y0 + 26, w, 150, t, kind, 13)
        if i < 5:
            f.arrow([(x + w, y0 + 100), (x + w + gap, y0 + 100)])
    return done(f, y0 + 190,
                "Lo que enseña: un fallo técnico de 45 minutos tuvo efectos corporativos, financieros y regulatorios durante catorce meses. Cada eslabón es documentado; la relación causal entre la pérdida y la fusión es interpretación y no figura en la orden.",
                "gold", SEC + " Párrafos 1, 11, 35, 50, 51 y sanciones. Financiación: comunicado de Knight del 6 de agosto de 2012.")


FIGURES = {
    "knight-capital-contexto.svg": contexto,
    "knight-capital-capas-de-control.svg": capas,
    "knight-capital-componentes-smars.svg": componentes,
    "knight-capital-secuencia.svg": secuencia,
    "knight-capital-modelo-de-datos.svg": datos,
    "knight-capital-servidores.svg": servidores,
    "knight-capital-bucle-de-ordenes.svg": bucle,
    "knight-capital-antecedentes.svg": antecedentes,
    "knight-capital-ventana-de-despliegue.svg": ventana,
    "knight-capital-linea-de-tiempo.svg": tiempos,
    "knight-capital-magnitud.svg": magnitud,
    "knight-capital-alcance-en-el-mercado.svg": alcance,
    "knight-capital-puntos-unicos.svg": puntos_unicos,
    "knight-capital-defensa-en-profundidad.svg": defensa,
    "knight-capital-arbol-de-fallas.svg": arbol,
    "knight-capital-controles.svg": controles,
    "knight-capital-arquitectura-despues.svg": despues,
    "knight-capital-barrera.svg": barrera,
    "knight-capital-consecuencias.svg": consecuencias,
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
