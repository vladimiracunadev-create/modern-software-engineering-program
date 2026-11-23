"""Figures for the failure case study Boeing 737 MAX and MCAS (Lion Air 610, 2018; Ethiopian 302, 2019).

Every number comes from the public reports cited in each footer (KNKT, EAIB, NTSB, JATR, FAA, House committee
majority staff). Nothing here judges people. Output goes to ``casos/figures/``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_generic import barrier_slices, chain, columns, context, done, fault_tree, layers, pairs  # noqa: E402
from case_fig_helpers_fallo import equi_axis, sketch  # noqa: E402
from figure_kit import Fig, grouped_bars, timeline  # noqa: E402

KNKT = "Fuente: KNKT, informe final JT610 (25 oct 2019)."
EAIB = "Fuente: EAIB, informe final ET302 (dic 2022)."
JATR = "Fuente: JATR, informe a la FAA (oct 2019)."
NTSB = "Fuente: NTSB, informe de recomendaciones (sep 2019)."
HOUSE = "Fuente: informe del personal de la mayoría del Comité de Transporte de la Cámara (sep 2020)."
FAA = "Fuente: FAA, cronología del 737 MAX."
ANALISIS = "Análisis propio, no conclusión de las investigaciones."


def contexto() -> Fig:
    return context(
        "Quién interviene entre el diseño de un avión y su vuelo con pasajeros",
        "Diagrama de contexto: Boeing diseña el 737 MAX; la FAA lo certifica y delega parte de la revisión en representantes autorizados de Boeing; las aerolíneas lo operan con pilotos y mantenimiento; dentro del avión, el sistema de control de vuelo contiene la función MCAS, que lee un sensor de ángulo de ataque.",
        [("Boeing: diseño, pruebas de vuelo, análisis de seguridad", "navy"), ("FAA: certificación y supervisión, con delegación en representantes autorizados", "teal"),
         ("Aerolíneas, pilotos y organizaciones de mantenimiento", "plain")],
        ("Avión Boeing 737 MAX", [("Sensores de ángulo de ataque, uno a cada lado", "plain"), ("Ordenadores de control de vuelo con la función MCAS", "coral"), ("Compensador del estabilizador horizontal", "plain"), ("Alertas e indicaciones de cabina", "gold")]),
        [("Pasajeros y tripulación", "plain"), ("Autoridades extranjeras y revisiones técnicas conjuntas", "teal"), ("Investigadores de accidentes: Indonesia, Etiopía, EE. UU.", "navy")],
        "Lo que enseña: la seguridad del avión depende de decisiones repartidas entre fabricante, regulador y operadores. La caja roja del centro es la función que ambos informes de accidente colocan en el centro de la cadena.",
        KNKT + " " + JATR, left_labels=["diseña", "certifica", "opera"], right_labels=["viajan", "revisan", "investigan"])


def investigaciones() -> Fig:
    return columns(
        "Qué se investigó y quién lo hizo: tres tipos de fuente",
        "Tres columnas: investigaciones de los dos accidentes por Indonesia y Etiopía, revisiones técnicas de certificación por el NTSB y la revisión conjunta de autoridades, y la investigación del Congreso de EE. UU. con su informe del personal de la mayoría.",
        [("Investigación de accidentes", "navy", ["KNKT (Indonesia): informe final de JT610, 25 de octubre de 2019", "EAIB (Etiopía): informe final de ET302, diciembre de 2022, con comentarios discrepantes del NTSB y del BEA"]),
         ("Revisión de certificación", "teal", ["NTSB: recomendaciones de seguridad a la FAA, 19 de septiembre de 2019", "JATR: 28 miembros de la FAA, la NASA y nueve autoridades civiles; mayo a septiembre de 2019; doce recomendaciones"]),
         ("Investigación legislativa", "gold", ["Comité de Transporte e Infraestructura de la Cámara de EE. UU.: informe final de septiembre de 2020", "Elaborado por el personal de la mayoría demócrata: se cita como tal"])],
        "Lo que enseña: ninguna fuente sola cubre todo. Mira la tercera columna: es un informe de una de las partes del Comité y este caso lo trata como fuente con punto de vista, no como veredicto.",
        "Fuentes: KNKT, EAIB, NTSB, JATR y Comité de Transporte de la Cámara de EE. UU.")


def funcion_mcas() -> Fig:
    return chain(
        "Cómo actuaba MCAS: de un sensor a un movimiento del estabilizador",
        "Cadena de la función MCAS: un sensor de ángulo de ataque entrega su valor a la unidad de datos aéreos, el ordenador de control de vuelo principal compara el ángulo con un umbral, la ley de control ordena al compensador mover el estabilizador con el morro hacia abajo, y los pilotos pueden detenerlo con los interruptores del compensador o cortar su energía.",
        [("Sensor de ángulo de ataque izquierdo o derecho", "plain"), ("Unidad de referencia de datos aéreos e inerciales", "plain"), ("Ordenador de control de vuelo principal alterno por vuelo", "teal"),
         ("MCAS: si el ángulo supera un umbral con flaps arriba y piloto manual", "coral", True), ("Mueve el estabilizador con el morro hacia abajo", "coral"), ("Los pilotos pueden detenerlo con los interruptores o cortarlo", "teal")],
        "Lo que enseña: la función era una ley de control dentro del ordenador, no un equipo nuevo; leía un único sensor por vuelo. Mira que la reposición tras un reinicio dependía de que el ángulo bajara; si no bajaba, MCAS volvía a actuar tras 5 segundos.",
        KNKT + " Apartado 1.6.5.4.", per_row=3)


def autoridad() -> Fig:
    return grouped_bars(
        "La autoridad de MCAS sobre el estabilizador pasó de 0,6 a 2,5 grados",
        "Barras con la autoridad máxima de movimiento del estabilizador por activación: 0,6 grados en el diseño original y 2,5 grados tras el rediseño de marzo de 2016.",
        ["Diseño original", "Tras el rediseño de marzo de 2016"],
        [("Movimiento máximo por activación", [0.6, 2.5], "coral")],
        unit="Grados de movimiento del estabilizador por activación", horizontal=True, label_w=250, ticks=[0, 0.5, 1, 1.5, 2, 2.5, 3], decimals=1,
        note="El informe del Comité atribuye el cambio a que, en marzo de 2016, pilotos de prueba hallaron mal manejo cerca de pérdidas a baja velocidad, y dice que el rediseño permitía actuar a menos velocidad. Las dos cifras vienen de un documento de Boeing de 2015 y de la descripción del rediseño que cita el informe; el KNKT y la EAIB describen el sistema tal como estaba en los accidentes.",
        note_kind="gold", foot=HOUSE)


def alertas() -> Fig:
    return chain(
        "Lo que vio la tripulación: muchas indicaciones a la vez y ninguna que nombrara a MCAS",
        "Cadena de indicaciones en el vuelo JT610 y el anterior: sensor con sesgo de 21 grados, desacuerdo de velocidad y de altitud, luz de presión diferencial, agitador de palanca continuo y activaciones repetidas de MCAS; el aviso de desacuerdo de ángulo de ataque no estaba habilitado.",
        [("Sensor izquierdo con sesgo de 21° no detectado en la prueba de instalación", "coral"), ("IAS DISAGREE y ALT DISAGREE en las pantallas", "gold"), ("Luz FEEL DIFF PRESS y agitador de palanca activo todo el vuelo", "gold"),
         ("Activaciones repetidas de MCAS", "coral"), ("AOA DISAGREE: no estaba habilitado, no apareció", "coral", True), ("Una tripulación cortó el compensador y aterrizó; la siguiente no identificó el desbocamiento", "navy")],
        "Lo que enseña: el aviso que habría nombrado el problema, AOA DISAGREE, no se mostró, y el único que lo habría resuelto sin nombrarlo, cortar el compensador, no figuraba en los manuales de MCAS. Mira la quinta caja: es una ausencia, no una acción.",
        KNKT + " Sinopsis y apartados 3.2.", per_row=3)


def cadena_jt610() -> Fig:
    return chain(
        "Lion Air JT610 en siete eslabones: del sensor al mar de Java",
        "Siete eslabones: sensor reparado con calibración errónea, instalación sin detectar el error, vuelo anterior con MCAS activo y cortado por la tripulación, informe de vuelo sin la parada del agitador ni el corte del compensador, vuelo JT610 con los mismos síntomas, checklist de velocidad no fiable sin identificar el desbocamiento, impacto 13 minutos después del despegue.",
        [("Reparación previa del sensor con calibración errónea", "coral"), ("Instalación en Denpasar el 28 de octubre sin detectar el sesgo", "coral"), ("Vuelo Denpasar-Yakarta: MCAS activo; la tripulación corta el compensador", "gold"),
         ("Informe de vuelo sin el agitador continuo ni el corte del compensador", "gold"), ("29 de octubre: JT610 con los mismos síntomas", "coral"), ("Checklist de velocidad no fiable; no se identifica el desbocamiento", "coral"), ("Impacto en el mar a los 13 minutos del despegue", "navy")],
        "Lo que enseña: el accidente empieza el día anterior en un taller y en un libro de registro, no en la cabina. Mira los eslabones dorados: la información que habría roto la cadena existió en el vuelo previo y no llegó a quien la necesitaba.",
        KNKT + " Sinopsis; el Comité de la Cámara da los 13 minutos.", per_row=4)


def tiempos() -> Fig:
    return timeline(
        "Ethiopian Airlines 302: seis minutos desde el despegue hasta el final del registro",
        "Línea de tiempo en minutos desde las 5:38 UTC del 10 de marzo de 2019: despegue normal; poco después el sensor izquierdo da valores erróneos y se activa el agitador; hay cuatro activaciones automáticas de morro abajo, la segunda a 5:40:22, la tercera a 5:40:43 sin movimiento y la cuarta a 5:43:21; el registro termina a 5:43:44.",
        [("Vuelo", [(0, 5.73, "agitador izquierdo activo hasta casi el final", "navy")]),
         ("Compensador automático (MCAS)", [(2.37, 2.5, "", "coral"), (2.72, 2.8, "", "coral"), (5.35, 5.45, "", "coral")])],
        unit="Minutos desde las 5:38 UTC", events=[(2.37, "5:40:22"), (5.35, "5:43:21")], ticks=[0, 1, 2, 3, 4, 5, 6], t_max=6, label_w=270,
        note="El informe da la 1.ª activación de 9 segundos tras recoger los flaps (sin hora en el resumen), la 2.ª a 5:40:22, la 3.ª a 5:40:43 sin movimiento del estabilizador y la 4.ª a 5:43:21. Las duraciones de las barras cortas son de dibujo; solo las horas están en el informe.",
        note_kind="gold", foot=EAIB + " Resumen ejecutivo.")


def disputa() -> Fig:
    return columns(
        "Lo que se discute del informe final de Etiopía",
        "Dos columnas: lo que dice el informe etíope sobre el origen del valor erróneo del sensor y la documentación de MCAS, y lo que dice el NTSB: está de acuerdo en el papel de MCAS, pero cree que la causa del dato erróneo fue la rotura de la paleta por un objeto extraño, probablemente un ave, y que Boeing sí informó de MCAS a los operadores cuatro meses antes.",
        [("Informe final de la EAIB (diciembre de 2022)", "teal", ["Probable causa: órdenes repetidas de morro abajo de MCAS por un ángulo de ataque erróneo, irrecuperables", "Atribuye el valor erróneo a anomalías eléctricas que dejaron sin calentador al sensor", "Califica de inadecuada la formación de diferencias que daba Boeing"]),
         ("Comentarios del NTSB (diciembre de 2022 y enero de 2023)", "gold", ["De acuerdo con el papel de MCAS y sistemas relacionados", "Cree que la causa del valor erróneo fue la separación de la paleta por un objeto extraño, probablemente un ave", "Dice que Boeing informó de MCAS a todos los operadores cuatro meses antes", "Pide más atención al desempeño humano"])],
        "Lo que enseña: dos investigaciones reputadas pueden discrepar en detalles y coincidir en la función implicada. Este caso se apoya en los dos puntos comunes y señala el desacuerdo sin decidirlo.",
        "Fuentes: EAIB (dic 2022); NTSB, comunicado del 24 de enero de 2023.")


def supuestos() -> Fig:
    return pairs(
        "Cuatro supuestos de diseño sobre la respuesta de los pilotos y lo que se observó",
        "Cuatro pares: cada supuesto con el que Boeing evaluó el riesgo de una activación de MCAS no ordenada y lo que el NTSB señaló al comparar con las respuestas de los pilotos de los accidentes.",
        [("Una entrada no ordenada se reconoce y se contrarresta moviendo los mandos en el sentido normal", "Las tripulaciones tuvieron muchas indicaciones simultáneas y fueron necesarios procedimientos específicos"),
         ("La acción no exige habilidad ni fuerza excepcionales", "Las fuerzas de columna llegaron a más de 90 libras en el vuelo ET302"),
         ("El piloto actúa de inmediato para reducir las fuerzas reajustando el compensador", "El informe etíope registra compensación eléctrica y nuevas activaciones cinco segundos después"),
         ("Se siguen de memoria los procedimientos entrenados", "Faltaba información de MCAS en manuales y formación; el aviso de desacuerdo no apareció")],
        "Lo que enseña: los supuestos eran los que la guía de la FAA y Boeing usaban para sus evaluaciones de peligro y eran coherentes con la norma; la conclusión del NTSB es que no consideraban el efecto de las alertas múltiples. Los supuestos son del NTSB; las observaciones, de los informes de accidente.",
        NTSB + " " + KNKT, top_kind="gold", bottom_kind="coral", note_kind="gold")


def antecedentes() -> Fig:
    f, y = sketch("De la competencia de 2010 al regreso del servicio en 2020, en ocho hitos",
                  "Eje no proporcional con ocho hitos: Airbus lanza el A320neo en diciembre de 2010; Boeing anuncia el 737 MAX en agosto de 2011; la certificación se solicita el 30 de junio de 2012; se certifica el 8 de marzo de 2017; el primer vuelo comercial es en mayo de 2017; accidentes el 29 de octubre de 2018 y el 10 de marzo de 2019; la FAA anula la prohibición el 18 de noviembre de 2020.")
    ev = [("Dic 2010: Airbus lanza el A320neo", "navy"), ("Ago 2011: Boeing anuncia el 737 MAX", "navy"), ("30 jun 2012: se solicita la certificación", "gold"), ("8 mar 2017: certificación del 737-8", "gold"),
          ("Mayo 2017: primer servicio con pasajeros", "teal"), ("29 oct 2018: JT610", "coral"), ("10 mar 2019: ET302; el 13, prohibición de la FAA", "coral"), ("18 nov 2020: la FAA anula la prohibición", "teal")]
    yy = equi_axis(f, y + 6, ev, box_w=170, box_h=100)
    return done(f, yy,
                "Lo que enseña: de la solicitud a la certificación pasaron casi cinco años, y del primer servicio con pasajeros al primer accidente, diecisiete meses. Mira que la prohibición duró unos veinte meses.",
                "gold", HOUSE + " " + JATR + " " + FAA, )


def meses() -> Fig:
    return timeline(
        "Veinte meses en tierra: la prohibición y las revisiones que ocurrieron durante ella",
        "Línea de tiempo en meses desde enero de 2019: la FAA prohíbe operar el 737 MAX el 13 de marzo de 2019; el JATR trabaja de mayo a septiembre de 2019; el NTSB publica recomendaciones en septiembre; el KNKT publica su informe final en octubre; el Comité de la Cámara publica su informe en septiembre de 2020; la FAA anula la prohibición el 18 de noviembre de 2020.",
        [("Prohibición de la FAA", [(2.4, 22.6, "en tierra unos veinte meses", "coral")]),
         ("JATR", [(4.4, 9.0, "revisión", "teal")]),
         ("Informes públicos", [(8.6, 9.1, "", "navy"), (9.8, 10.2, "", "navy"), (20.4, 20.9, "", "gold")])],
        unit="Meses desde enero de 2019", events=[(2.4, "13 mar 2019"), (22.6, "18 nov 2020")], ticks=[0, 3, 6, 9, 12, 15, 18, 21, 24], t_max=24, label_w=200,
        note="Las marcas de «Informes públicos» son, de izquierda a derecha, el informe del NTSB (19 de septiembre de 2019), el informe final del KNKT (25 de octubre de 2019) y el informe del personal de la mayoría del Comité (septiembre de 2020). El informe final de Etiopía, de diciembre de 2022, queda fuera de la escala.",
        note_kind="gold", foot=FAA + " Fechas de cada informe en la ficha.")


def puntos_unicos() -> Fig:
    return context(
        "Dependencias de un único elemento en la cadena de MCAS",
        "Mapa de dependencias: un solo sensor por vuelo alimentaba MCAS; la alternancia de ordenador principal por vuelo, la ausencia de aviso de desacuerdo, la detención como único modo de cortar el sistema y la dependencia de la respuesta del piloto; cada una sin alternativa independiente.",
        [("Un solo sensor de ángulo de ataque por vuelo", "coral"), ("Aviso de desacuerdo de ángulo de ataque no habilitado", "coral"), ("Formación y manuales sin MCAS", "gold")],
        ("Ruta de MCAS", [("Ley de control en el ordenador principal", "coral"), ("Compensador del estabilizador", "plain")]),
        [("Corte del compensador: único modo de detenerlo", "teal"), ("Respuesta del piloto bajo múltiples alertas", "gold")],
        "Lo que enseña: el sistema estaba protegido por la esperanza de que el piloto reconociera y cortara; cada defensa se apoyaba en las otras. Mira que lo rojo es una decisión de diseño y lo dorado, un supuesto de uso.",
        KNKT + " " + ANALISIS, left_labels=["lee", "debía avisar", "debía explicar"], right_labels=["corta", "decide"])


def defensa() -> Fig:
    return barrier_slices(
        "Defensa en profundidad: ocho barreras y los huecos que se alinearon",
        "Láminas con huecos alineados: análisis de seguridad con supuestos de piloto, redundancia de sensores, aviso de desacuerdo, documentación y formación, prueba de instalación del sensor, informe de mantenimiento, procedimiento de emergencia y supervisión de la certificación.",
        [("Análisis de peligro con supuestos de piloto", "gold"), ("Redundancia de sensor para MCAS (un solo sensor)", "coral"), ("Aviso de desacuerdo de AOA (no habilitado)", "coral"), ("Manuales y formación (sin MCAS)", "coral"),
         ("Prueba de instalación del sensor (no detectó 21°)", "coral"), ("Informe de vuelo y mantenimiento (incompleto)", "gold"), ("Procedimiento de desbocamiento (se aplicó en un vuelo)", "gold"), ("Revisión de la certificación (cambios no actualizados)", "gold")],
        "Lo que enseña: no faltó una barrera, fallaron varias a la vez por la misma razón: se daba por hecho que el piloto resolvería. Rojo: ausente o fallida; dorado: existía y fue parcial. Es una metáfora, no una medición.",
        KNKT + " " + JATR + " " + ANALISIS)


def arbol() -> Fig:
    return fault_tree(
        "Árbol de fallas: qué tuvo que coincidir para perder un avión",
        "Árbol de fallas con la pérdida de control tras activaciones repetidas de MCAS: una rama es que MCAS reciba un ángulo de ataque erróneo, con tres condiciones, y la otra es que la tripulación no corte el sistema a tiempo, con cuatro.",
        "Pérdida de control tras activaciones repetidas",
        ("A. MCAS actúa con un dato erróneo", "Y", ["Un único sensor alimenta MCAS", "El sensor entrega un valor erróneo (sesgo de 21° en JT610; discutida su causa en ET302)", "Sin aviso que lo señale al piloto ni al mantenimiento"]),
        ("B. La tripulación no lo corta a tiempo", "Y", ["Indicaciones múltiples y simultáneas", "MCAS ausente de los manuales y de la formación", "Reactivación tras la compensación del piloto", "Sin tiempo ni margen de altura"]),
        "Lo que enseña: cualquier condición cortada habría roto el árbol. Mira que la rama A es de diseño y mantenimiento y la B de información y factores humanos. Estructura lógica propia sobre lo que los informes establecen.",
        KNKT + " " + EAIB + " " + ANALISIS)


def capas_certificacion() -> Fig:
    return chain(
        "Cómo se reparte la certificación: del fabricante a la autoridad",
        "Cadena de la certificación: el fabricante propone el diseño y sus análisis de seguridad; representantes autorizados de la empresa realizan parte de la revisión por delegación de la FAA; la oficina de supervisión de la FAA revisa lo que se le presenta; las normas aplicables son una combinación de enmiendas de 1967 y posteriores según la regla de producto modificado.",
        [("Boeing: diseño y análisis de seguridad con supuestos", "navy"), ("Representantes autorizados de Boeing con facultades delegadas por la FAA", "teal"), ("Oficina de supervisión de Boeing en la FAA", "teal"), ("Base de certificación: mezcla de enmiendas de 1967 y posteriores", "gold")],
        "Lo que enseña: delegar revisión es una decisión de capacidad con riesgo de información incompleta. Los informes difieren en cuánto peso le dan; el JATR recomienda revisar la delegación, y el Comité de la Cámara documenta preocupaciones de los propios representantes.",
        JATR + " " + HOUSE)


def controles() -> Fig:
    return pairs(
        "Cada eslabón de la cadena y el control que lo corta",
        "Ocho pares de causa y control propuesto: un solo sensor, supuestos de piloto, alertas múltiples, aviso no habilitado, cambios de diseño sin actualizar el análisis, formación sin MCAS, prueba de instalación y registro de mantenimiento.",
        [("MCAS con un solo sensor", "Dos o tres fuentes independientes y rechazo de desacuerdos"), ("Supuestos de respuesta del piloto", "Validarlos con pilotos en simulador con alertas múltiples reales"),
         ("Alertas múltiples sin priorizar", "Evaluar el efecto conjunto de indicaciones e indicar la función activa"), ("Aviso de desacuerdo no habilitado", "Prueba de que cada alerta de la lista aprobada funciona antes de la entrega"),
         ("Cambio de 2016 sin actualizar el análisis", "Reabrir el análisis de seguridad con cada cambio de autoridad o de condiciones"), ("Formación sin MCAS", "Toda función con autoridad sobre el control aparece en manual y formación"),
         ("Sensor mal calibrado instalado", "Prueba de instalación con criterio de aceptación comprobable"), ("Informe de vuelo incompleto", "Formato guiado que obligue a anotar agitador y corte de compensador")],
        "Lo que enseña: algunas mejoras llegaron después, como el rediseño de MCAS aprobado por la FAA en 2020; la columna inferior es análisis propio sobre qué habría cortado cada eslabón, no un resumen de lo que se hizo.",
        ANALISIS)


def despues() -> Fig:
    return chain(
        "La arquitectura «después»: qué cambia en la ley de control y en su entorno",
        "Cadena objetivo: dos sensores comparados, límite de autoridad y de repeticiones, aviso visible de desacuerdo, función documentada y entrenada, cierre del análisis de seguridad con pruebas de piloto y registro de mantenimiento guiado.",
        [("Entrada de MCAS validada con dos sensores y rechazo de desacuerdos", "teal"), ("Autoridad limitada y no repetible indefinidamente", "teal"), ("Aviso de desacuerdo y de función activa siempre visibles", "teal"),
         ("Función en manuales y formación con simulación de fallo", "teal"), ("Análisis de seguridad actualizado con cada cambio y con pilotos en simulador", "teal"), ("Mantenimiento con prueba de aceptación del sensor", "teal")],
        "Lo que enseña: son controles de diseño, de información y de proceso; ninguno exige una tecnología nueva. Diseño didáctico apoyado en las recomendaciones del NTSB, el JATR y los informes de accidente; no describe el rediseño que aprobó la FAA.",
        ANALISIS, per_row=3, note_kind="teal")


def pila() -> Fig:
    return layers(
        "Qué se sabe de la pila técnica del control de vuelo",
        "Capas de la pila técnica: sensores de ángulo de ataque, unidad de datos aéreos, ordenadores de control de vuelo, ley MCAS, compensador del estabilizador y alertas; documentadas en los informes; lenguaje, procesador y sistema operativo no consta.",
        [("Sensores", "doc", "Dos sensores de paleta (uno a cada lado), cada uno con dos resolvers; una unidad de datos aéreos por lado"),
         ("Ordenadores de control de vuelo", "doc", "Dos ordenadores; MCAS solo está activo en el principal, que alterna cada vuelo"),
         ("Ley MCAS", "doc", "Parte del sistema de compensación por velocidad; actúa con el piloto manual, flaps arriba y ángulo sobre un umbral"),
         ("Actuación", "doc", "Compensador del estabilizador; interruptores de corte y de columna; MCAS inhibe el corte de columna en un sentido mientras actúa"),
         ("Alertas", "doc", "Desacuerdo de velocidad y de altitud, agitador, avisos de la cabina; el aviso de desacuerdo de ángulo no estaba habilitado"),
         ("Lenguaje, procesador, sistema operativo, versiones de software", "unk", "No constan en los informes consultados; este caso no los inventa")],
        "Lo que enseña: los informes dan el nivel de detalle necesario para entender el fallo. Verde: documentado; gris: no se sabe.",
        KNKT + " Apartado 1.6.5.")


def modelos() -> Fig:
    return columns(
        "Dos formas de pensar el fallo: un fallo aislado frente a un fallo con muchas señales",
        "Dos columnas: el modelo con el que se evaluó el peligro, un fallo de un sistema que el piloto reconoce y corrige con el procedimiento de desbocamiento, y la situación de los accidentes, con una cascada de indicaciones, activaciones repetidas y poco tiempo.",
        [("Modelo de la evaluación de peligro", "gold", ["Un fallo, una causa clara", "El piloto lo reconoce por el movimiento de la rueda del compensador o la fuerza de la columna", "Se aplica el procedimiento de desbocamiento de memoria", "Clasificado como «mayor»"]),
         ("Lo que mostraron los accidentes", "coral", ["Un dato erróneo que dispara varias indicaciones a la vez", "MCAS no figuraba en los manuales ni en la formación", "Activaciones repetidas tras cada compensación", "Poca altura y carga de trabajo alta"])],
        "Lo que enseña: el análisis de peligros sirve en la medida en que sus supuestos se verifican con el sistema completo y con personas. La clasificación «mayor» y los supuestos vienen del informe del NTSB.",
        NTSB + " " + KNKT)


def consecuencias() -> Fig:
    return chain(
        "Consecuencias fechadas: de dos accidentes a la anulación de la prohibición",
        "Cadena de consecuencias: 189 fallecidos en JT610 el 29 de octubre de 2018; 157 en ET302 el 10 de marzo de 2019; prohibición de la FAA el 13 de marzo de 2019; informes públicos en 2019, 2020 y 2022; anulación de la prohibición el 18 de noviembre de 2020.",
        [("29 oct 2018: JT610, 189 fallecidos", "coral"), ("10 mar 2019: ET302, 157 fallecidos", "coral"), ("13 mar 2019: la FAA prohíbe operar el 737 MAX", "gold"), ("18 nov 2020: la FAA anula la prohibición con una directiva de aeronavegabilidad", "teal")],
        "Lo que enseña: 346 personas fallecieron en los dos accidentes. Este caso recuerda las cifras con respeto y sin adjetivos; los costes económicos de Boeing y de las aerolíneas no se cuantifican aquí porque las fuentes verificadas no los dan.",
        KNKT + " " + EAIB + " " + FAA)


def negocio() -> Fig:
    return chain(
        "Esquema del negocio: del encargo de las aerolíneas a la entrega del avión",
        "Esquema de negocio: las aerolíneas encargan aviones de un modelo derivado que evite formación nueva y ahorre combustible; Boeing desarrolla el 737 MAX con motores nuevos para competir con el A320neo; la certificación habilita la entrega; las aerolíneas lo operan con la formación de diferencias.",
        [("Aerolíneas: encargos de un derivado con menos coste de formación", "plain"), ("Boeing: 737 MAX con motores nuevos para competir con el A320neo", "navy"), ("FAA: certificación como derivado del 737 NG", "teal"), ("Aerolíneas: operación con formación de diferencias", "gold")],
        "Lo que enseña: evitar formación nueva en simulador es una propiedad de negocio que condiciona qué cambios de diseño son aceptables. El informe del Comité documenta 496 compromisos de cinco clientes al anunciar el avión en agosto de 2011.",
        HOUSE)


def que_aprender() -> Fig:
    return columns(
        "Qué aprender y qué no generalizar",
        "Dos columnas: lo que se transfiere, como no depender de un solo sensor para una función con autoridad sobre el control y verificar supuestos de uso con personas, y lo que no se generaliza, como culpar al software o a las personas.",
        [("Se transfiere", "teal", ["Una función con autoridad sobre el control necesita entradas redundantes", "Los supuestos sobre personas se validan con personas", "Un cambio de diseño reabre el análisis de seguridad", "Lo que el sistema hace debe estar en el manual y en la formación"]),
         ("No se generaliza", "gold", ["No prueba que automatizar sea malo", "No es un fallo de una persona ni de un solo documento", "Las fuentes difieren en detalles; no hay veredicto único", "Cifras y fechas son de este avión y de estos años"])],
        "Lo que enseña: el aprendizaje correcto es de ingeniería de sistemas, de certificación y de factores humanos. Mira la columna derecha: el caso se usa mal cuando se reduce a un villano.",
        ANALISIS)


FIGURES = {
    "boeing-737-max-mcas-contexto.svg": contexto,
    "boeing-737-max-mcas-investigaciones.svg": investigaciones,
    "boeing-737-max-mcas-funcion-mcas.svg": funcion_mcas,
    "boeing-737-max-mcas-autoridad.svg": autoridad,
    "boeing-737-max-mcas-alertas.svg": alertas,
    "boeing-737-max-mcas-cadena-jt610.svg": cadena_jt610,
    "boeing-737-max-mcas-minutos-et302.svg": tiempos,
    "boeing-737-max-mcas-disputa-et302.svg": disputa,
    "boeing-737-max-mcas-supuestos.svg": supuestos,
    "boeing-737-max-mcas-antecedentes.svg": antecedentes,
    "boeing-737-max-mcas-veinte-meses.svg": meses,
    "boeing-737-max-mcas-puntos-unicos.svg": puntos_unicos,
    "boeing-737-max-mcas-defensa-en-profundidad.svg": defensa,
    "boeing-737-max-mcas-arbol-de-fallas.svg": arbol,
    "boeing-737-max-mcas-certificacion.svg": capas_certificacion,
    "boeing-737-max-mcas-controles.svg": controles,
    "boeing-737-max-mcas-arquitectura-despues.svg": despues,
    "boeing-737-max-mcas-hardware-y-software.svg": pila,
    "boeing-737-max-mcas-modelos-de-fallo.svg": modelos,
    "boeing-737-max-mcas-consecuencias.svg": consecuencias,
    "boeing-737-max-mcas-esquema-del-negocio.svg": negocio,
    "boeing-737-max-mcas-que-aprender.svg": que_aprender,
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
