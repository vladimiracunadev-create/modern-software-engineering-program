"""Figures for the failure case study Knight Capital (1 August 2012).

Every number comes from the SEC order of 16 October 2013 (Release No. 34-70694) unless the footer says it is
illustrative. Output goes to ``casos/figures/`` (see ``main``); the shared case build may also import ``FIGURES``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from figure_kit import Fig, _kit_finish, _kit_start, _wrap, grouped_bars, timeline  # noqa: E402

SEC = "Fuente: SEC, Release No. 34-70694 (16 de octubre de 2013)."
ANALISIS = "Análisis propio apoyado en el informe de la SEC; no es una conclusión del regulador."


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
                "gold", SEC + " Participaciones de 2011 y 2012.")


# ------------------------------------------------------------------ 2. componentes
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


# ------------------------------------------------------------------ 3. flujo crítico
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


# ------------------------------------------------------------------ 4. línea de tiempo
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


# ------------------------------------------------------------------ 5. gráfico con datos citados
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


# ------------------------------------------------------------------ 6. antes / después
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


FIGURES = {
    "knight-capital-contexto.svg": contexto,
    "knight-capital-servidores.svg": servidores,
    "knight-capital-bucle-de-ordenes.svg": bucle,
    "knight-capital-linea-de-tiempo.svg": tiempos,
    "knight-capital-magnitud.svg": magnitud,
    "knight-capital-controles.svg": controles,
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
