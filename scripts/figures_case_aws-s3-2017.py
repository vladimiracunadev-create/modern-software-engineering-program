"""Figures for the failure case study Amazon S3 in US-EAST-1 (28 February 2017).

Every fact comes from the official post "Summary of the Amazon S3 Service Disruption in the Northern Virginia
(US-EAST-1) Region" unless the footer says it is own analysis. Output goes to ``casos/figures/``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_generic import barrier_slices, chain, columns, context, done, fault_tree, layers, pairs  # noqa: E402
from case_fig_helpers_fallo import equi_axis, sketch  # noqa: E402
from figure_kit import Fig, grouped_bars, timeline  # noqa: E402

AWS = "Fuente: AWS, resumen oficial de la interrupción de S3 en US-EAST-1 (2017)."
ANALISIS = "Análisis propio, no conclusión de AWS."


def contexto() -> Fig:
    return context(
        "S3 en el centro de otros servicios de la región",
        "Diagrama de contexto: los clientes y otros servicios de AWS en US-EAST-1 usan la API de S3 para leer, listar, escribir y borrar objetos; el subsistema de índice guarda los metadatos y la ubicación de todos los objetos; el subsistema de ubicación asigna almacenamiento a objetos nuevos; la consola, EC2, EBS y Lambda dependen de S3.",
        [("Clientes de S3 y sus aplicaciones", "plain"), ("Servicios de AWS que usan S3: consola, EC2, EBS y Lambda", "gold")],
        ("S3 en US-EAST-1", [("API: GET, LIST, PUT y DELETE", "teal"), ("Subsistema de índice: metadatos y ubicación de todos los objetos", "coral"), ("Subsistema de ubicación: asigna almacenamiento a objetos nuevos", "coral"), ("Subsistema de facturación", "plain")]),
        [("Datos de los objetos en almacenamiento", "plain"), ("Panel de estado de AWS (SHD), que dependía de S3", "gold"), ("Equipo de S3 y sus herramientas operativas", "navy")],
        "Lo que enseña: el índice es necesario para servir todas las peticiones y la ubicación necesita el índice. Mira que los servicios que dependen de S3 forman una segunda capa de usuarios.",
        AWS, left_labels=["usan", "dependen"], right_labels=["guarda", "informa", "opera"])


def subsistemas() -> Fig:
    return chain(
        "Los subsistemas de S3 implicados y cómo dependen unos de otros",
        "Cadena de dependencias: el subsistema de índice es necesario para servir todas las peticiones GET, LIST, PUT y DELETE; el subsistema de ubicación asigna almacenamiento en los PUT y requiere el índice; ambos se reiniciaron por completo; mientras tanto S3 no podía atender peticiones.",
        [("Subsistema de índice: metadatos y ubicación de todos los objetos", "coral"), ("Necesario para GET, LIST, PUT y DELETE", "teal"), ("Subsistema de ubicación: asigna almacenamiento en los PUT", "coral"), ("Requiere que el índice funcione bien", "gold"), ("Con ambos reiniciándose, S3 no atiende peticiones", "navy")],
        "Lo que enseña: el orden de recuperación está impuesto por la dependencia: primero el índice, después la ubicación. Mira que por eso el PUT tardó más en volver que el GET.",
        AWS, per_row=3)


def comando() -> Fig:
    return chain(
        "El comando y su entrada: de un cambio pequeño a una retirada grande",
        "Cadena del comando: un miembro autorizado del equipo, con un procedimiento establecido, ejecuta un comando para retirar unos pocos servidores de un subsistema de facturación; una de las entradas se introduce mal; se retira un conjunto mayor de servidores del previsto; los servidores retirados soportaban otros dos subsistemas.",
        [("9:37 PST: se depura la facturación y se ejecuta un comando con un procedimiento establecido", "plain"), ("El comando debía retirar pocos servidores de un subsistema de facturación", "teal"), ("Una de las entradas se introduce mal", "coral", True), ("Se retira un conjunto mayor: soportaban el índice y la ubicación", "coral"), ("Ambos subsistemas necesitan un reinicio completo", "navy")],
        "Lo que enseña: la operación era rutinaria y legítima, y la herramienta aceptó una entrada que retiraba demasiada capacidad demasiado rápido. Mira la tercera caja: el fallo es de entrada, la causa es que la herramienta no la acotaba.",
        AWS, per_row=3)


def minutos() -> Fig:
    return timeline(
        "28 de febrero de 2017 en minutos: del comando a la normalidad",
        "Línea de tiempo en minutos desde las 9:37 PST: el comando se ejecuta a las 9:37; el panel de estado no puede actualizarse hasta las 11:37; el índice empieza a atender GET, LIST y DELETE a las 12:26; el índice se recupera del todo a las 13:18; la ubicación termina a las 13:54 y S3 opera con normalidad.",
        [("S3 sin servir peticiones", [(0, 169, "12:26", "coral")]),
         ("Índice reiniciándose", [(0, 221, "13:18", "gold")]),
         ("Ubicación (PUT)", [(221, 257, "13:54", "teal")]),
         ("Panel de estado (SHD)", [(0, 120, "11:37", "grey")])],
        unit="Minutos desde las 9:37 PST", events=[(120, "11:37"), (169, "12:26"), (221, "13:18"), (257, "13:54")], ticks=[0, 30, 60, 90, 120, 150, 180, 210, 240, 270], t_max=270, label_w=200,
        note="Las horas son las del resumen de AWS; los minutos son restas propias: 9:37 a 12:26 = 169, a 13:18 = 221 y a 13:54 = 257. La primera barra no dice que no se pudiera nada hasta las 12:26: dice que ahí empezó el índice a servir GET, LIST y DELETE. El resumen no da una hora de fin del primer síntoma visible para los clientes.",
        note_kind="gold", foot=AWS)


def duracion() -> Fig:
    return grouped_bars(
        "Cuánto tardó cada recuperación desde el comando",
        "Barras con los minutos desde las 9:37 PST hasta cada hito de la recuperación: el índice empieza a atender peticiones a los 169 minutos, se recupera del todo a los 221 y la ubicación a los 257; el panel de estado se pudo actualizar a los 120.",
        ["Panel de estado actualizable (11:37)", "Índice sirve GET, LIST y DELETE (12:26)", "Índice recuperado del todo (13:18)", "S3 normal con la ubicación (13:54)"],
        [("Minutos desde el comando", [120, 169, 221, 257], "navy")], unit="Minutos desde las 9:37 PST", horizontal=True, label_w=300, ticks=[0, 60, 120, 180, 240, 300],
        note="Son restas propias sobre las horas del resumen de AWS. Cuatro horas y diecisiete minutos separan el comando de la normalidad. AWS atribuye la lentitud a que no había reiniciado por completo el índice ni la ubicación en regiones grandes desde hacía años y a que la validación de integridad de los metadatos tardó más de lo previsto.",
        note_kind="gold", foot=AWS)


def reinicio() -> Fig:
    return chain(
        "Por qué el reinicio tardó más de lo esperado",
        "Cadena del reinicio: los subsistemas se diseñaron para tolerar la retirada de capacidad; no se habían reiniciado por completo en regiones grandes desde hacía años; S3 creció mucho; reiniciar y validar la integridad de los metadatos llevó más tiempo del previsto.",
        [("Diseño: tolerar la retirada o el fallo de mucha capacidad", "teal"), ("Retirar capacidad es una operación habitual desde el lanzamiento", "plain"), ("Hace años que no se reinicia por completo el índice ni la ubicación en regiones grandes", "gold"), ("S3 ha crecido muchísimo", "gold"), ("Reiniciar y validar los metadatos tarda más de lo previsto", "coral")],
        "Lo que enseña: una operación de recuperación que no se ejerce a escala real puede tardar mucho más de lo medido cuando era pequeña. Mira la tercera caja: lo que no se ha ensayado se vuelve incierto con el crecimiento.",
        AWS, per_row=3)


def dependientes() -> Fig:
    return columns(
        "Qué se vio afectado además de S3",
        "Dos columnas: los servicios de AWS en US-EAST-1 que dependen de S3 y se vieron afectados, y la herramienta de comunicación, el panel de estado, que también dependía de S3 y no se pudo actualizar hasta las 11:37.",
        [("Servicios afectados mientras la API de S3 no estaba disponible", "coral", ["Consola de S3", "Lanzamiento de instancias nuevas de EC2", "Volúmenes de EBS cuando se necesitaban datos de una instantánea en S3", "AWS Lambda"]),
         ("La comunicación del incidente", "gold", ["El panel de estado (SHD) dependía de S3 en su consola de administración", "Hasta las 11:37 no se pudo actualizar el estado de cada servicio", "Se usó el canal de Twitter de AWS y el texto de un aviso en el panel", "Ahora la consola del panel funciona en varias regiones"])],
        "Lo que enseña: la dependencia de un servicio base se extiende a lo que debe avisar de que ese servicio falla. Mira la segunda columna: la herramienta para informar dependía de lo que estaba roto.",
        AWS)


def puntos_unicos() -> Fig:
    return context(
        "Dependencias de un único elemento en la región",
        "Mapa de dependencias: un subsistema de índice del que dependen todas las peticiones, un subsistema de ubicación que depende del índice, una herramienta que aceptaba retirar demasiada capacidad y un panel de estado dependiente de S3.",
        [("Índice de S3 necesario para todas las peticiones", "coral"), ("Ubicación dependiente del índice", "gold"), ("Herramienta que permitía retirar demasiada capacidad", "coral")],
        ("S3 en una región", [("Subsistemas con reinicio completo poco ensayado", "gold"), ("Servicios de la región que usan S3", "gold")]),
        [("Peticiones de clientes sin servicio", "plain"), ("Panel de estado sin actualizar", "plain")],
        "Lo que enseña: la capacidad de retirar servidores es una función central y también una vía de fallo. Rojo: punto único de efecto directo. Lectura propia de lo que describe AWS.",
        AWS + " " + ANALISIS, left_labels=["necesario", "depende", "ejecuta"], right_labels=["sin servicio", "sin aviso"])


def defensa() -> Fig:
    return barrier_slices(
        "Defensa en profundidad: ocho barreras y por qué una entrada errónea afectó a toda la región",
        "Láminas con huecos alineados: procedimiento establecido, validación de la entrada, límite de capacidad mínima, retirada gradual, particiones en celdas, reinicio ensayado, aviso y comunicación; una flecha las atraviesa.",
        [("Procedimiento establecido (se siguió)", "gold"), ("Validación de la entrada (aceptó la retirada)", "coral"), ("Capacidad mínima por subsistema (no se comprobaba)", "coral"), ("Retirada gradual (la herramienta era demasiado rápida)", "coral"),
         ("Celdas para reducir el radio (el índice aún sin particionar más)", "gold"), ("Reinicio ensayado a escala (no desde hacía años)", "coral"), ("Respuesta del equipo (recuperó el servicio)", "teal"), ("Comunicación (el panel dependía de S3)", "gold")],
        "Lo que enseña: una operación rutinaria, con procedimiento, pasó todas las comprobaciones porque ninguna limitaba cuánta capacidad se retiraba. Rojo: ausente; dorado: parcial; verde: funcionó. Es una metáfora.",
        AWS + " " + ANALISIS)


def arbol() -> Fig:
    return fault_tree(
        "Árbol de fallas: qué tuvo que coincidir para que S3 dejara de servir peticiones",
        "Árbol de fallas con la interrupción de S3 arriba y dos ramas necesarias: que se retirara demasiada capacidad de subsistemas críticos, con tres condiciones, y que la recuperación fuera larga, con tres.",
        "S3 no atiende peticiones en US-EAST-1 durante unas cuatro horas",
        ("A. Se retira demasiada capacidad de subsistemas críticos", "Y", ["Una entrada mal escrita en un comando legítimo", "Herramienta que retira capacidad demasiado rápido", "Sin comprobación de capacidad mínima por subsistema"]),
        ("B. La recuperación es larga", "Y", ["Índice y ubicación requieren un reinicio completo", "Hace años que no se reiniciaban por completo en regiones grandes", "Validar la integridad de los metadatos tarda más de lo previsto"]),
        "Lo que enseña: cortar cualquiera de las seis condiciones reduce el daño. Mira que A es de prevención y B de recuperación, y que AWS actúa sobre las dos. Estructura propia sobre lo que cuenta el resumen.",
        AWS + " " + ANALISIS)


def prueba_de_fallos() -> Fig:
    return columns(
        "A prueba de fallos: qué existía, qué falló, qué no existía y qué debió existir",
        "Cuatro columnas: mecanismos que existían y funcionaron (diseño tolerante a la retirada de capacidad, procedimiento, respuesta del equipo), que existían y fallaron (herramienta, panel de estado), que no existían (límite mínimo, retirada lenta, reinicio completo ensayado) y que debieron existir (análisis propio).",
        [("Existía y funcionó", "teal", ["Subsistemas diseñados para tolerar la retirada de mucha capacidad", "Procedimiento operativo establecido", "El equipo restauró el índice y la ubicación", "Mensajes por Twitter y texto en el panel"]),
         ("Existía y falló", "gold", ["Herramienta de retirada de capacidad", "Panel de estado con dependencia de S3", "Particiones en celdas: aún parciales en el índice"]),
         ("No existía", "coral", ["Salvaguarda de capacidad mínima por subsistema", "Retirada de capacidad lenta", "Ensayo de reinicio completo en regiones grandes"]),
         ("Debió existir (análisis propio)", "navy", ["Validar la entrada contra el impacto previsto", "Retirada limitada por ritmo y por mínimo", "Ensayo periódico de reinicio a escala", "Panel de estado fuera de la región y de los servicios que informa"])],
        "Lo que enseña: AWS anunció acciones sobre las tres primeras líneas de «No existía» y sobre el panel; la cuarta columna es análisis propio que coincide en gran parte.",
        AWS + " " + ANALISIS)


def controles() -> Fig:
    return pairs(
        "Cada eslabón de la cadena y el control que lo corta",
        "Ocho pares de causa y control: entrada errónea, herramienta rápida, sin mínimo, reinicio sin ensayar, crecimiento no medido en la recuperación, índice grande, panel dependiente y comunicación.",
        [("Entrada mal escrita", "Validar la entrada frente al efecto previsto y pedir confirmación si es grande"), ("Herramienta que retira capacidad demasiado rápido", "Retirada más lenta y por tramos"),
         ("Sin capacidad mínima por subsistema", "Rechazar cualquier retirada que deje un subsistema bajo su mínimo"), ("Reinicio completo sin ensayar", "Ensayo periódico de reinicio completo a escala real"),
         ("Recuperación que crece con la región", "Medir el tiempo de recuperación como indicador y mantenerlo bajo un tope"), ("Índice grande sin más particiones", "Dividir en celdas más pequeñas para reducir el radio de impacto"),
         ("Panel de estado dependiente de S3", "Panel que funcione en varias regiones y fuera del servicio que informa"), ("Otras herramientas con riesgo similar", "Auditar las demás herramientas con las mismas salvaguardas")],
        "Lo que enseña: cinco de estas mejoras coinciden con lo que AWS anunció: retirada más lenta, capacidad mínima, auditoría de otras herramientas, más particiones del índice y panel en varias regiones. La columna inferior es análisis propio.",
        AWS + " " + ANALISIS)


def despues() -> Fig:
    return chain(
        "La arquitectura «después»: una herramienta de capacidad que no puede dejar un subsistema bajo su mínimo",
        "Cadena objetivo: validación de la entrada, retirada de capacidad lenta, comprobación de capacidad mínima por subsistema, celdas más pequeñas del índice, ensayo periódico de reinicio y panel de estado en varias regiones.",
        [("Validación de la entrada frente al efecto previsto", "teal"), ("Retirada de capacidad más lenta", "teal"), ("Rechazo si un subsistema quedaría bajo su mínimo", "teal"), ("Índice dividido en celdas más pequeñas", "teal"), ("Ensayo periódico de reinicio a escala", "teal"), ("Panel de estado en varias regiones", "teal")],
        "Lo que enseña: AWS dijo haber modificado la herramienta para retirar capacidad más despacio y para impedir que un subsistema baje de su mínimo, y haber adelantado la partición del índice. Diseño didáctico apoyado en eso; no es la arquitectura completa.",
        AWS + " " + ANALISIS, per_row=3, note_kind="teal")


def acciones() -> Fig:
    return columns(
        "Lo que AWS anunció tras el incidente",
        "Tres columnas con las acciones del resumen: la herramienta modificada con retirada más lenta y salvaguarda de capacidad mínima, la auditoría de otras herramientas, y el índice y el panel de estado.",
        [("Herramienta de capacidad", "teal", ["Modificada para retirar capacidad más despacio", "Salvaguardas para no retirar capacidad si un subsistema baja de su mínimo requerido"]),
         ("Otras herramientas", "gold", ["Auditoría de las demás herramientas operativas con salvaguardas similares"]),
         ("Recuperación y comunicación", "navy", ["Trabajo para mejorar el tiempo de recuperación de los subsistemas clave", "Partición más pequeña del índice, que estaba prevista para más tarde, pasa a empezar de inmediato", "Consola del panel de estado en varias regiones"])],
        "Lo que enseña: las acciones cubren prevención, recuperación y comunicación. No verificamos aquí su cumplimiento posterior; son compromisos del resumen.",
        AWS)


def pila() -> Fig:
    return layers(
        "Qué se sabe de la pila técnica",
        "Capas de lo que consta: subsistemas de índice, ubicación y facturación de S3; la API; servicios dependientes como EC2, EBS y Lambda; el panel de estado; lenguaje, hardware y arquitectura interna no se publican.",
        [("API", "doc", "GET, LIST, PUT y DELETE de S3"),
         ("Subsistemas", "doc", "Índice (metadatos y ubicación de objetos), ubicación (asignación de almacenamiento) y facturación"),
         ("Técnica de diseño", "doc", "Partición de servicios en celdas para limitar el radio de impacto y mejorar la recuperación"),
         ("Servicios dependientes", "doc", "Consola de S3, EC2, EBS con instantáneas en S3 y Lambda"),
         ("Panel de estado", "doc", "Consola de administración con dependencia de S3; texto de aviso y Twitter como canales alternativos"),
         ("Hardware, lenguajes, número de servidores, centros de datos", "unk", "No constan en el resumen; este caso no los inventa")],
        "Lo que enseña: el resumen cuenta el diseño necesario para entender el incidente, no una documentación del sistema. Verde: documentado; gris: no se sabe.",
        AWS)


def negocio() -> Fig:
    return chain(
        "Esquema de la operación: S3 como servicio base de una región",
        "Esquema de la operación: S3 ofrece almacenamiento de objetos con alta disponibilidad; otros servicios de la región lo usan para guardar datos y para operar; un fallo del servicio base se propaga a los que lo usan.",
        [("S3 ofrece almacenamiento de objetos y una larga trayectoria de disponibilidad", "teal"), ("Clientes y otros servicios construyen sobre S3", "plain"), ("Los subsistemas se diseñan para que retirar capacidad sea una operación normal", "gold"), ("Un fallo del servicio base se propaga a toda la región", "coral")],
        "Lo que enseña: AWS dice estar orgullosa de su trayectoria de disponibilidad con S3 y reconoce lo críticos que son sus servicios para los clientes. El resumen no da cifras de clientes afectados ni de pérdidas; este caso no las inventa.",
        AWS)


def consecuencias() -> Fig:
    return chain(
        "Consecuencias fechadas: de las 9:37 a las acciones anunciadas",
        "Cadena de consecuencias: a las 9:37 se ejecuta el comando; S3 no atiende peticiones durante unas horas; a las 13:54 S3 vuelve a operar con normalidad; AWS publica un resumen con disculpa y cambios en la herramienta, el índice y el panel de estado.",
        [("28 feb 2017, 9:37 PST: se retira más capacidad de la prevista", "coral"), ("S3 sin servir peticiones; EC2, EBS, Lambda y consola afectados", "coral"), ("13:54: S3 opera con normalidad", "teal"), ("Resumen de AWS con disculpa y cambios en herramienta, índice y panel", "navy")],
        "Lo que enseña: el resumen incluye una disculpa a los clientes y reconoce lo crítico del servicio. No cuantifica clientes ni costes; este caso no los inventa.",
        AWS)


def que_aprender() -> Fig:
    return columns(
        "Qué aprender y qué no generalizar",
        "Dos columnas: lo que se transfiere, como acotar las herramientas operativas, ensayar la recuperación a escala y no depender de lo que se avisa; y lo que no se generaliza, como culpar a quien ejecutó el comando.",
        [("Se transfiere", "teal", ["Una herramienta operativa debe limitar su propio impacto", "Una recuperación que no se ensaya a escala es una estimación", "Los avisos no deben depender del servicio que avisan", "Particionar en celdas reduce el radio de impacto"]),
         ("No se generaliza", "gold", ["No prueba que S3 sea poco fiable: AWS habla de una larga trayectoria", "No es un fallo de una persona: el comando seguía un procedimiento", "Las horas y servicios son de 2017 y de una región", "No cuantifica el impacto en clientes"])],
        "Lo que enseña: el aprendizaje es de herramientas operativas, de recuperación y de comunicación. Mira la columna derecha: el caso se usa mal cuando se reduce a una errata.",
        ANALISIS)


def antecedentes() -> Fig:
    f, y = sketch("Del comando al reinicio, en siete hitos",
                  "Eje no proporcional con siete hitos: a las 9:37 se ejecuta el comando; el panel de estado no se puede actualizar; a las 11:37 se actualiza; a las 12:26 el índice atiende GET, LIST y DELETE; a las 13:18 el índice se recupera; a las 13:54 la ubicación y S3 vuelven a la normalidad; el resumen de AWS anuncia cambios.")
    ev = [("9:37 PST: se ejecuta el comando y se retira más capacidad", "coral"), ("Índice y ubicación necesitan un reinicio completo", "coral"), ("11:37: se puede actualizar el panel de estado", "gold"), ("12:26: el índice atiende GET, LIST y DELETE", "teal"),
          ("13:18: el índice, recuperado del todo", "teal"), ("13:54: la ubicación termina; S3 normal", "teal"), ("Resumen: cambios en herramienta, índice y panel", "navy")]
    yy = equi_axis(f, y + 6, ev, box_w=170, box_h=100)
    return done(f, yy,
                "Lo que enseña: el incidente duró 4 h 17 min desde el comando, con un primer tramo de unas dos horas en que el panel de estado no pudo actualizarse. Mira que los hitos no están a escala de tiempo.",
                "gold", AWS)


FIGURES = {
    "aws-s3-2017-contexto.svg": contexto,
    "aws-s3-2017-subsistemas.svg": subsistemas,
    "aws-s3-2017-comando.svg": comando,
    "aws-s3-2017-minutos.svg": minutos,
    "aws-s3-2017-duracion.svg": duracion,
    "aws-s3-2017-reinicio.svg": reinicio,
    "aws-s3-2017-servicios-dependientes.svg": dependientes,
    "aws-s3-2017-puntos-unicos.svg": puntos_unicos,
    "aws-s3-2017-defensa-en-profundidad.svg": defensa,
    "aws-s3-2017-arbol-de-fallas.svg": arbol,
    "aws-s3-2017-a-prueba-de-fallos.svg": prueba_de_fallos,
    "aws-s3-2017-controles.svg": controles,
    "aws-s3-2017-arquitectura-despues.svg": despues,
    "aws-s3-2017-acciones-anunciadas.svg": acciones,
    "aws-s3-2017-hardware-y-software.svg": pila,
    "aws-s3-2017-esquema-de-la-operacion.svg": negocio,
    "aws-s3-2017-consecuencias.svg": consecuencias,
    "aws-s3-2017-antecedentes.svg": antecedentes,
    "aws-s3-2017-que-aprender.svg": que_aprender,
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
