"""Figures for the failure case study Southwest Airlines, December 2022 operational collapse.

Facts come from the DOT press release of 18 December 2023, a CNN report and an AP report on the Senate Commerce hearing of
9 February 2023 and an NPR report, as stated in each footer. Statements by the union and by the company are labelled as such.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_generic import barrier_slices, chain, columns, context, done, fault_tree, layers, pairs  # noqa: E402
from case_fig_helpers_fallo import equi_axis, sketch  # noqa: E402
from figure_kit import Fig, grouped_bars, stacked_bars  # noqa: E402

DOT = "Fuente: DOT, comunicado del 18 de diciembre de 2023."
AUD = "Fuentes: CNN y AP sobre la audiencia del Senado (9 feb 2023)."
ANALISIS = "Análisis propio, no conclusión del DOT ni del Senado."


def contexto() -> Fig:
    return context(
        "Una red de vuelos punto a punto con tripulaciones que hay que reasignar",
        "Diagrama de contexto: Southwest opera aviones, tripulaciones y aeropuertos; ante una tormenta, la programación de tripulaciones debe reasignar pilotos y auxiliares a vuelos cambiados; un software de reasignación y procesos manuales de la aerolínea lo hacen; los pasajeros dependen de la información de estado y del servicio de atención.",
        [("Pasajeros: más de dos millones afectados", "plain"), ("Tripulaciones: pilotos y auxiliares de vuelo", "gold")],
        ("Operación de Southwest", [("Aviones y aeropuertos", "teal"), ("Programación de tripulaciones y software de reasignación", "coral"), ("Atención al cliente: llamadas, avisos y reembolsos", "gold")]),
        [("Aeropuertos y sus servicios", "plain"), ("DOT: regulador de protección al consumidor", "navy"), ("Senado: audiencia del comité de Comercio", "navy")],
        "Lo que enseña: cuando falla la reasignación de tripulaciones, la red entera se bloquea aunque haya aviones y pasajeros. La caja roja es el elemento que más se discute en las fuentes.",
        DOT + " " + AUD, left_labels=["esperan", "dependen"], right_labels=["sirven", "regula", "investiga"])


def magnitud() -> Fig:
    return grouped_bars(
        "La escala del colapso: vuelos cancelados y pasajeros afectados",
        "Barras horizontales con las dos cifras del DOT: unos 16 900 vuelos cancelados y más de dos millones de pasajeros afectados, en miles.",
        ["Vuelos cancelados", "Pasajeros afectados"],
        [("Miles", [16.9, 2000], "coral")], unit="Miles (escala logarítmica)", horizontal=True, log=True, label_w=220, decimals=1,
        note="El DOT habla de 16 900 vuelos y de más de dos millones de pasajeros; CNN dice «más de 16 700» vuelos y AP «casi 17 000»: las fuentes difieren en la cifra exacta. La escala es logarítmica porque son magnitudes de unidades distintas; no compares longitudes.",
        note_kind="gold", foot=DOT + " CNN y AP.")


def sancion() -> Fig:
    return stacked_bars(
        "Cómo se compone la sanción de 140 millones de dólares",
        "Barra apilada con los tres componentes de la sanción del DOT: 35 millones que Southwest paga al Tesoro, 72 millones que se compensan con un sistema de compensación de 90 millones y 33 millones que se acreditan por entregar 25 000 puntos a los pasajeros afectados.",
        ["Sanción del DOT"],
        [("Pago al Tesoro", [35], "coral"), ("Compensado con el sistema de 90 millones", [72], "teal"), ("Crédito por puntos Rapid Rewards", [33], "gold")],
        unit="Millones de dólares de EE. UU.", horizontal=True, label_w=160, totals=True,
        note="La suma es 140. Aparte de la sanción, el DOT dice que logró más de 600 millones en reembolsos y reintegros a los pasajeros y que Southwest pagará más de 750 millones en total por el colapso. Los 90 millones son vales de 75 dólares para pasajeros futuros con retrasos de tres horas o más controlables por la aerolínea.",
        note_kind="gold", foot=DOT + " Cifras de la orden de consentimiento.")


def violaciones() -> Fig:
    return columns(
        "Las tres infracciones de protección al consumidor que el DOT encontró",
        "Tres columnas: atención al cliente insuficiente, con llamadas con tono de ocupado, colas de horas y llamadas cortadas; avisos de estado tardíos o inexactos, con pasajeros que se enteraron de la cancelación en el aeropuerto; y reembolsos no prontos ni correctos, con errores en un sitio web de solicitudes y tarifas opcionales sin reembolsar.",
        [("Atención al cliente", "coral", ["El centro de llamadas se desbordó", "Tono de ocupado, colas de horas y llamadas cortadas", "Cientos de miles de pasajeros sin vuelo, en aeropuertos y hoteles"]),
         ("Avisos de estado", "coral", ["La política prometía avisos por texto o correo", "Muchos pasajeros no recibieron ninguno y otros uno inexacto", "Algunos supieron de la cancelación al llegar al aeropuerto"]),
         ("Reembolsos", "coral", ["Miles de clientes sin reembolso pronto", "Errores en el sitio de solicitudes que no se avisaron", "Tarifas opcionales sin reembolsar, como mascotas o embarque mejorado"])],
        "Lo que enseña: el DOT cuenta tres fallos de servicio al cliente; no es un informe técnico sobre la causa del colapso operativo. Mira que la segunda columna es un fallo de comunicación sistémico.",
        DOT)


def storm() -> Fig:
    return chain(
        "Del 21 de diciembre a la recuperación: la secuencia según el relato de la audiencia",
        "Cadena de la secuencia: una tormenta invernal afecta a varias aerolíneas el 21 de diciembre; Southwest tiene problemas con descongelación y pasarelas en Denver y Chicago y cancela la mayor parte de los vuelos en esos aeropuertos; el 24 la reasignación de tripulaciones está desbordada; las tripulaciones quedan varadas igual que los pasajeros; la recuperación tarda otra semana.",
        [("21 dic: tormenta invernal; otras aerolíneas se recuperan, Southwest no", "plain"), ("Problemas de descongelación y pasarelas en Denver y Chicago; se cancela la mayor parte de los vuelos allí", "gold"), ("24 dic: la capacidad de reasignar tripulaciones está desbordada", "coral", True),
         ("Pilotos y auxiliares quedan varados como los pasajeros", "coral"), ("Otra semana hasta recuperar la operación", "navy")],
        "Lo que enseña: un problema local de aeropuerto se propaga a toda la red cuando no se pueden reasignar tripulaciones. Mira la tercera caja: ese es el cuello de botella que la audiencia sitúa. Es el relato de AP; no es una reconstrucción oficial.",
        AUD, per_row=3)


def posiciones() -> Fig:
    return columns(
        "Dos relatos de la causa: la aerolínea y el sindicato de pilotos",
        "Dos columnas con posiciones distintas expresadas en el Senado: el director de operaciones de Southwest dijo que la tormenta creó una cantidad y frecuencia sin precedentes de cambios de tripulaciones que desbordaron sus procesos y tecnología; el sindicato de pilotos dijo que los fallos eran previsibles y evitables y que se ignoraron avisos durante años.",
        [("Según Southwest (director de operaciones)", "teal", ["La tormenta fue peor de lo esperado", "Una cantidad y frecuencia sin precedentes de cambios de tripulación desbordaron procesos y tecnología", "Se actualizará el software de reasignación, se ha creado un equipo en el centro de mando y se mejoran los teléfonos"]),
         ("Según el sindicato de pilotos (SWAPA)", "gold", ["Los fallos eran previsibles y evitables", "Dice que desde 2011 hubo un fallo operativo grave cada 18 meses de media", "Dice que se ignoraron avisos y que hubo más de 500 vuelos vacíos para recolocar aviones y más de 10 000 pilotos viajando como pasajeros"])],
        "Lo que enseña: son posiciones de parte, expresadas ante el Senado; Southwest no comentó las afirmaciones del sindicato antes de la audiencia, según CNN. Este caso no decide entre ambas.",
        AUD)


def mensajes() -> Fig:
    return chain(
        "Lo que mostraban los mensajes a las cabinas, según el testimonio del sindicato",
        "Cadena de mensajes: los despachadores pedían por mensaje a una cabina qué tripulación operaba el vuelo; otro mensaje decía que no había actualizaciones y que la programación iba tan retrasada que no se permitía ir a hablar con ella; las tripulaciones quedaron sin poder comunicarse con despacho.",
        [("Un mensaje a una cabina: «Sched pide confirmar quién opera este vuelo»", "gold"), ("Otro: «No hay novedades; la programación va tan retrasada que no podemos ir a hablar»", "gold"), ("Tripulaciones varadas sin poder comunicarse con despacho", "coral"), ("Pérdida de la imagen de quién está dónde", "coral")],
        "Lo que enseña: sin una vista fiable del estado de cada tripulación, no se puede planificar. Son mensajes que el sindicato presentó como evidencia y que CNN reproduce; este caso los trata como tal.",
        "Fuente: CNN, 9 feb 2023 (testimonio del sindicato).")


def puntos_unicos() -> Fig:
    return context(
        "Dependencias de un único elemento en la recuperación",
        "Mapa de dependencias: un software de reasignación de tripulaciones superado por el volumen de cambios, procesos manuales de comunicación con tripulaciones, un único centro de llamadas desbordado y un sitio de reembolsos con errores; cada uno sin alternativa suficiente.",
        [("Software de reasignación de tripulaciones", "coral"), ("Procesos manuales de comunicación con las tripulaciones", "coral"), ("Un centro de llamadas y un sitio de reembolsos", "gold")],
        ("Recuperación de la operación", [("Reasignar tripulaciones a vuelos cambiados", "coral"), ("Informar a pasajeros y reembolsar", "gold")]),
        [("Aviones y tripulaciones inmovilizados", "plain"), ("Pasajeros sin información ni servicio", "plain")],
        "Lo que enseña: una red depende de que la reasignación de tripulaciones funcione más que de tener aviones. Rojo: punto con efecto directo; dorado: dependencia de servicio. Lectura propia.",
        AUD + " " + DOT + " " + ANALISIS, left_labels=["asigna", "comunica", "atiende"], right_labels=["bloquea", "sin aviso"])


def defensa() -> Fig:
    return barrier_slices(
        "Defensa en profundidad: ocho barreras y por qué un problema local se volvió nacional",
        "Láminas con huecos alineados: plan ante tormentas, recursos en aeropuertos, software de reasignación, procesos manuales, comunicación con tripulaciones, información a pasajeros, atención y reembolsos, y señales previas; una flecha las atraviesa.",
        [("Plan ante tormentas (existía, la tormenta fue peor)", "gold"), ("Recursos en aeropuertos (descongelación y pasarelas)", "gold"), ("Software de reasignación (superado)", "coral"), ("Procesos manuales con tripulaciones (desbordados)", "coral"),
         ("Información a pasajeros (tardía o inexacta)", "coral"), ("Atención y reembolsos (insuficientes)", "coral"), ("Señales previas (según el sindicato, ignoradas)", "gold"), ("Recuperación (tardó otra semana)", "gold")],
        "Lo que enseña: las barreras que fallaron son de capacidad de recuperación, no de prevención de la tormenta. Rojo: insuficiente según las fuentes; dorado: existía con límites o está en discusión. Es una metáfora.",
        DOT + " " + AUD + " " + ANALISIS)


def arbol() -> Fig:
    return fault_tree(
        "Árbol de fallas: qué tuvo que coincidir para que una tormenta paralizara una aerolínea",
        "Árbol de fallas con el colapso operativo arriba y dos ramas necesarias: una perturbación grande que requería muchos cambios de tripulación, con dos condiciones, y una capacidad de recuperación insuficiente, con cuatro.",
        "Colapso operativo con unos 16 900 vuelos cancelados",
        ("A. Una perturbación exige muchos cambios", "Y", ["Una tormenta invernal severa desde el 21 de diciembre", "Problemas locales en aeropuertos de Denver y Chicago"]),
        ("B. La recuperación no da abasto", "Y", ["Software de reasignación superado por el volumen de cambios", "Procesos manuales que no escalan", "Tripulaciones sin comunicación fiable con despacho", "Avisos y atención al cliente desbordados"]),
        "Lo que enseña: la tormenta fue común a varias aerolíneas; lo específico estaba en la rama B. Estructura propia sobre lo que cuentan las fuentes, con la causa técnica en discusión entre las partes.",
        AUD + " " + ANALISIS)


def prueba_de_fallos() -> Fig:
    return columns(
        "A prueba de fallos: qué existía, qué falló, qué no existía y qué debió existir",
        "Cuatro columnas: mecanismos que existían (plan ante tormentas, software de reasignación, política de atención), que falló (reasignación, avisos, atención, reembolsos), que no consta que existieran (vista fiable de tripulaciones, capacidad de escala) y que debieron existir (análisis propio).",
        [("Existía y funcionó", "teal", ["Operación normal en el resto del año", "Reembolsos y reintegros finalmente pagados: más de 600 millones según el DOT", "Plan de atención al cliente comprometido en septiembre de 2022"]),
         ("Existía y falló", "gold", ["Software de reasignación de tripulaciones: superado", "Avisos de estado por texto o correo", "Centro de llamadas y sitio de reembolsos"]),
         ("No consta que existiera", "coral", ["Una vista fiable de dónde está cada tripulación", "Capacidad de escala del proceso de reasignación", "Alternativa manual que absorbiera el volumen"]),
         ("Debió existir (análisis propio)", "navy", ["Reasignación que escale con el volumen de cambios", "Estado de tripulaciones visible para despacho", "Modo degradado: cancelar vuelos para estabilizar la red", "Atención y avisos dimensionados para un pico"])],
        "Lo que enseña: lo que funcionó fue pagar después; lo que faltó fue la capacidad de recuperación en el momento. La cuarta columna es análisis propio.",
        DOT + " " + AUD + " " + ANALISIS)


def controles() -> Fig:
    return pairs(
        "Cada eslabón de la cadena y el control que lo corta",
        "Ocho pares de causa y control: reasignación superada, procesos manuales, falta de estado fiable de tripulaciones, avisos tardíos, centro de llamadas desbordado, reembolsos con errores, señales previas ignoradas y recuperación lenta.",
        [("Software de reasignación superado por el volumen", "Pruebas de carga con escenarios de tormenta y de miles de cambios por hora"), ("Procesos manuales que no escalan", "Automatizar la comunicación con tripulaciones y un canal de contingencia"),
         ("Sin vista fiable de tripulaciones", "Estado único y verificable de cada tripulación, visible para despacho"), ("Avisos de estado tardíos o inexactos", "Avisos automáticos desde la fuente de verdad, con comprobación de entrega"),
         ("Centro de llamadas desbordado", "Capacidad elástica y autoservicio en la web para reubicar y reembolsar"), ("Sitio de reembolsos con errores", "Validación visible de cada solicitud y confirmación al cliente"),
         ("Señales previas ignoradas", "Registro de fallos pasados con dueño y plazo, y revisión externa"), ("Recuperación que tardó una semana", "Ejercicios de colapso y reglas para cancelar y estabilizar la red")],
        "Lo que enseña: algunos de estos controles coinciden con lo que Southwest dijo estar haciendo: actualizar el software de reasignación, un equipo nuevo en el centro de mando y mejores teléfonos. La columna inferior es análisis propio.",
        AUD + " " + ANALISIS)


def despues() -> Fig:
    return chain(
        "La arquitectura «después»: una operación que degrada en lugar de colapsar",
        "Cadena objetivo: reasignación de tripulaciones que escala, estado único de tripulaciones, comunicación automatizada, avisos desde la fuente de verdad, atención elástica y reglas de cancelación para estabilizar la red.",
        [("Reasignación de tripulaciones que escala con el volumen", "teal"), ("Estado único y verificable de cada tripulación", "teal"), ("Comunicación automatizada con tripulaciones", "teal"),
         ("Avisos a pasajeros desde la fuente de verdad", "teal"), ("Atención y reembolsos con capacidad elástica", "teal"), ("Reglas para cancelar a tiempo y estabilizar la red", "teal")],
        "Lo que enseña: el objetivo es que una perturbación grande degrade el servicio de forma controlada. Diseño didáctico; no describe lo que Southwest implantó, salvo lo que dijo en la audiencia.",
        ANALISIS, per_row=3, note_kind="teal")


def pila() -> Fig:
    return layers(
        "Qué se sabe de la pila técnica",
        "Capas de lo que consta: software de reasignación de tripulaciones de General Electric, procesos manuales de comunicación con tripulaciones, mensajes a cabinas, sitio web de reembolsos y centro de llamadas; lenguaje, infraestructura y arquitectura no se publican.",
        [("Reasignación de tripulaciones", "doc", "Software de General Electric que sugiere cómo reasignar tripulaciones a vuelos tras una perturbación; superado por el número de cambios, según el director de operaciones"),
         ("Comunicación con tripulaciones", "doc", "Mensajes a ordenadores de cabina y procesos manuales; el sindicato dice que quedaron sin poder hablar con programación"),
         ("Avisos a pasajeros", "doc", "Política de avisos por texto o correo que el DOT dice que se rompió"),
         ("Reembolsos", "doc", "Un sitio web de solicitudes con errores que no se avisaron a los clientes"),
         ("Centro de llamadas", "doc", "Desbordado; tono de ocupado y colas de horas"),
         ("Lenguajes, infraestructura, base de datos, arquitectura", "unk", "No constan en las fuentes consultadas; este caso no los inventa")],
        "Lo que enseña: las fuentes describen los síntomas visibles en cada capa, no el diseño. Verde: documentado; gris: no se sabe.",
        DOT + " " + AUD)


def negocio() -> Fig:
    return chain(
        "Esquema de la operación: de la tormenta a la sanción",
        "Esquema de la operación: una aerolínea sin recuperación rápida pierde vuelos, ingresos y reputación; el DOT investiga y sanciona por consumo; el Senado investiga las causas; la aerolínea invierte en tecnología y procesos.",
        [("Tormenta y colapso operativo: unos 16 900 vuelos cancelados", "coral"), ("Costes: más de 1 000 millones según AP; reembolsos y reintegros de más de 600 millones según el DOT", "gold"), ("DOT: sanción de 140 millones y sistema de compensación futura", "navy"), ("Inversión en software, centro de mando y teléfonos", "teal")],
        "Lo que enseña: el coste de no poder recuperar una red es mayor que el de la tormenta. Las cifras de coste son de AP y del DOT; no se contrastaron con las cuentas de la empresa en esta sesión.",
        DOT + " " + AUD)


def consecuencias() -> Fig:
    return chain(
        "Consecuencias fechadas: del colapso a la sanción",
        "Cadena de consecuencias: colapso operativo de diciembre de 2022; audiencia del Senado el 9 de febrero de 2023; sanción del DOT y sistema de compensación el 18 de diciembre de 2023; reducción de las cancelaciones en los primeros nueve meses de 2023 en el sector, según el DOT.",
        [("21 dic 2022: tormenta; Southwest no se recupera: unos 16 900 vuelos cancelados", "coral"), ("9 feb 2023: audiencia del Comité de Comercio del Senado", "navy"), ("18 dic 2023: el DOT impone una sanción de 140 millones de dólares", "navy"), ("Cancelaciones del sector a la baja en 2023, según el DOT", "teal")],
        "Lo que enseña: la respuesta pública fue regulatoria y legislativa, y se centró en el trato al consumidor. Las medidas posteriores a 2023 no se verificaron en esta sesión.",
        DOT + " " + AUD)


def antecedentes() -> Fig:
    f, y = sketch("De la política de septiembre de 2022 a la sanción de diciembre de 2023, en seis hitos",
                  "Eje no proporcional con seis hitos: septiembre de 2022 Southwest cambia su plan de atención al cliente; 21 de diciembre una tormenta golpea a varias aerolíneas; 24 de diciembre la reasignación de tripulaciones está desbordada; una semana más para recuperarse; 9 de febrero de 2023 audiencia del Senado; 18 de diciembre de 2023 sanción del DOT.")
    ev = [("Sep 2022: Southwest cambia su plan de atención al cliente", "gold"), ("21 dic 2022: tormenta; otras aerolíneas se recuperan", "gold"), ("24 dic: reasignación de tripulaciones desbordada", "coral"), ("Una semana más para recuperar la operación", "coral"),
          ("9 feb 2023: audiencia del Comité de Comercio", "navy"), ("18 dic 2023: sanción del DOT", "navy")]
    yy = equi_axis(f, y + 6, ev, box_w=170, box_h=100)
    return done(f, yy,
                "Lo que enseña: el colapso duró unos diez días y su respuesta regulatoria, un año. Mira que el cambio de política de septiembre de 2022 es lo que obligó a Southwest a reembolsar gastos de pasajeros durante el colapso.",
                "gold", DOT + " " + AUD)


def que_aprender() -> Fig:
    return columns(
        "Qué aprender y qué no generalizar",
        "Dos columnas: lo que se transfiere, como diseñar la recuperación para el peor día y no solo la operación normal, y tener una vista fiable del estado de las personas y los recursos; y lo que no se generaliza, como culpar a un software o a un directivo.",
        [("Se transfiere", "teal", ["Dimensiona la recuperación para el peor día", "Sin estado fiable de tus recursos no puedes reasignarlos", "Un proceso manual no escala con el volumen de cambios", "Los avisos al cliente son parte de la operación"]),
         ("No se generaliza", "gold", ["No prueba que un software concreto fuera la causa: las partes discrepan", "No es el fallo de una persona", "Las cifras son de un episodio concreto de EE. UU.", "Las fuentes no incluyen el informe técnico completo del Senado ni del DOT"])],
        "Lo que enseña: el aprendizaje es de capacidad de recuperación y de información. Mira la columna derecha: el caso se usa mal cuando se reduce a un software o a una persona.",
        ANALISIS)


FIGURES = {
    "southwest-2022-contexto.svg": contexto,
    "southwest-2022-magnitud.svg": magnitud,
    "southwest-2022-sancion.svg": sancion,
    "southwest-2022-infracciones.svg": violaciones,
    "southwest-2022-secuencia.svg": storm,
    "southwest-2022-dos-relatos.svg": posiciones,
    "southwest-2022-mensajes.svg": mensajes,
    "southwest-2022-puntos-unicos.svg": puntos_unicos,
    "southwest-2022-defensa-en-profundidad.svg": defensa,
    "southwest-2022-arbol-de-fallas.svg": arbol,
    "southwest-2022-a-prueba-de-fallos.svg": prueba_de_fallos,
    "southwest-2022-controles.svg": controles,
    "southwest-2022-arquitectura-despues.svg": despues,
    "southwest-2022-hardware-y-software.svg": pila,
    "southwest-2022-esquema-de-la-operacion.svg": negocio,
    "southwest-2022-consecuencias.svg": consecuencias,
    "southwest-2022-antecedentes.svg": antecedentes,
    "southwest-2022-que-aprender.svg": que_aprender,
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
