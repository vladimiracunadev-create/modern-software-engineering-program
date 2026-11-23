"""Figures for the failure case study Ariane 5, flight 501 (4 June 1996).

Every number comes from the Inquiry Board report (J.-L. Lions, 19 July 1996, ESA/CNES) unless the footer says it
is own analysis. Output goes to ``casos/figures/``; the shared case build imports ``FIGURES``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_generic import barrier_slices, chain, columns, context, done, fault_tree, layers, pairs  # noqa: E402
from case_fig_helpers_fallo import bx, equi_axis, sequence, sketch  # noqa: E402
from figure_kit import Fig, grouped_bars, timeline  # noqa: E402

INF = "Fuente: informe de la comisión de Ariane 501 (19 de julio de 1996)."
ANALISIS = "Análisis propio, no conclusión de la comisión."


def contexto() -> Fig:
    return context(
        "Quién era quién en el vuelo 501: programa, industria y lanzador",
        "Diagrama de contexto: la ESA y el CNES promueven el programa Ariane 5 con socios industriales; el lanzador transporta la carga útil Cluster desde Kourou; la telemetría va al CNES en Toulouse y la comisión de investigación examina todo.",
        [("ESA y CNES: programa y comisión de investigación", "navy"), ("Socios industriales: arquitecto industrial y proveedor de la unidad inercial", "teal"),
         ("Base de Kourou: campaña de lanzamiento y cuenta atrás", "plain")],
        ("Lanzador Ariane 5, primer vuelo de cualificación", [("Sistema de control de vuelo: dos unidades inerciales y dos ordenadores de a bordo", "coral"),
                                                             ("Motor Vulcain y dos aceleradores de combustible sólido", "plain"),
                                                             ("Sistema de autodestrucción", "gold")]),
        [("Carga útil: satélites científicos Cluster", "plain"), ("Telemetría a Toulouse (CNES)", "plain"), ("Comisión de investigación: 10 miembros y 5 asesores", "navy")],
        "Lo que enseña: el fallo ocurrió en una unidad que muchos actores integraban pero ninguno probaba entera con las condiciones reales del nuevo lanzador. Cada flecha es una responsabilidad compartida.",
        INF + " Prólogo y apartado 1. Los nombres de las empresas proveedoras no figuran en el cuerpo del informe.",
        left_labels=["programa", "contratos", "campaña"], right_labels=["carga", "datos", "análisis"])


def organizacion() -> Fig:
    return columns(
        "La comisión de investigación: encargo, miembros y apoyo técnico",
        "Tres columnas: el encargo de tres puntos que recibió la comisión, sus diez miembros de cinco países y el comité técnico asesor de cinco personas, con el inicio de su trabajo el 13 de junio de 1996.",
        [("Encargo (tres puntos)", "navy", ["Determinar las causas del fallo del lanzamiento", "Comprobar si las pruebas de cualificación y aceptación eran adecuadas para el problema", "Recomendar acciones correctivas"]),
         ("Comisión: 10 miembros", "teal", ["Presidente: J.-L. Lions, Academia de Ciencias (Francia)", "Vicepresidente: L. Lübeck, Swedish Space Corporation", "Ocho vocales de Francia, Alemania, Italia y el Reino Unido: academia, defensa, investigación e industria"]),
         ("Comité técnico asesor: 5", "gold", ["Representantes de BPD, Matra Marconi Space, CNES, Aérospatiale y ESA", "Empezó el 13 de junio de 1996", "Informe público el 19 de julio y presentación el 23 de julio de 1996"])],
        "Lo que enseña: una comisión independiente, con encargo escrito y miembros de fuera del proyecto, es lo que permitió publicar un diagnóstico técnico en seis semanas. Mira que su tercer punto pide evaluar si las pruebas eran adecuadas, no solo qué falló.",
        INF + " Prólogo.")


def sedes() -> Fig:
    return chain(
        "Dónde pasó y dónde se analizó: de Kourou a Toulouse",
        "Cadena geográfica: lanzamiento en Kourou, Guayana Francesa; autodestrucción a unos 4 km de altitud; restos esparcidos en unos 12 kilómetros cuadrados de manglar; telemetría enviada al CNES en Toulouse; copia a Aérospatiale para analizar el sistema eléctrico.",
        [("Kourou: lanzamiento a las 9:33:59 hora local", "plain"), ("A unos 4 km de altitud y 1 km de la plataforma: autodestrucción", "coral"), ("Restos en 12 km² de manglar y sabana (el informe da también 5 por 2,5 km)", "gold"), ("Telemetría a Toulouse (CNES) y copia a Aérospatiale", "teal")],
        "Lo que enseña: la recuperación de las dos unidades inerciales entre los restos fue lo que permitió leer sus memorias y confirmar la causa. Mira la nota: el informe da dos extensiones de la zona de restos, una en el apartado 1.3 y otra en las conclusiones.",
        INF + " Apartados 1.1, 1.3 y 3.1 (j y k). Dos cifras distintas de superficie en el mismo informe.")


def secuencia_tiempos() -> Fig:
    return timeline(
        "Los 2,3 segundos que decidieron el vuelo: de la parada de las unidades a la ruptura",
        "Línea de tiempo en segundos desde el inicio de la secuencia de vuelo: vuelo nominal hasta 36,7 segundos; entonces falla la unidad inercial de reserva y 0,05 segundos después la activa; el ordenador interpreta datos de diagnóstico como vuelo y las toberas llegan al extremo; a los 39 segundos el lanzador se rompe.",
        [("Vuelo nominal", [(30, 36.6, "nominal", "teal")]),
         ("Unidad inercial de reserva", [(36.6, 37.0, "", "coral")]),
         ("Unidad inercial activa", [(36.65, 37.0, "", "coral")]),
         ("Ordenador de a bordo", [(37.0, 39.0, "órdenes", "gold")]),
         ("Lanzador", [(37.0, 38.9, "ángulo > 20°", "coral"), (39.0, 40.0, "rotura", "navy")])],
        unit="Segundos desde H0 (encendido del motor Vulcain); zoom de 30 a 41 s", events=[(36.7, "36,7 s"), (39, "39 s")],
        ticks=[30, 32, 34, 36, 38, 40], t_max=41, label_w=230,
        note="Los tramos de 0,4 s son tamaño de dibujo, no medida: el informe da 36,7 s para la parada, unos 0,05 s entre las dos unidades, 39 s para la ruptura y 'unos 40 s' de vuelo total. Lo esencial es que desde la parada hasta la ruptura pasan unos 2 segundos y que no hay tiempo para intervención humana alguna.",
        note_kind="coral", foot=INF + " Apartados 1.1, 2.1 y 3.1 (e a j).")


def funcionamiento() -> Fig:
    return chain(
        "Cómo funciona el control de vuelo, de la medición al movimiento de las toberas",
        "Flujo del control de vuelo: la unidad de referencia inercial con giróscopos láser y acelerómetros calcula ángulos y velocidades, los envía por el bus de datos al ordenador de a bordo, que ejecuta el programa de vuelo y manda por servoválvulas y actuadores hidráulicos a las toberas de los aceleradores y del motor Vulcain.",
        [("Plataforma inercial con giróscopos láser y acelerómetros", "plain"), ("Ordenador interno de la unidad: calcula ángulos y velocidades", "teal"), ("Bus de datos hacia el ordenador de a bordo", "plain"), ("Ordenador de a bordo: ejecuta el programa de vuelo", "teal"),
         ("Servoválvulas y actuadores hidráulicos", "plain"), ("Toberas de los dos aceleradores y del motor Vulcain", "plain")],
        "Lo que enseña: toda la actitud del lanzador depende de una cadena de medición-cálculo-actuación sin humano en el bucle. Cuando el dato de entrada deja de ser medición, la salida deja de ser control. Mira que la unidad inercial es el origen de toda la cadena.",
        INF + " Apartado 2.1. Esquema funcional propio sobre la descripción del informe.", per_row=3)


def redundancia() -> Fig:
    return context(
        "Redundancia en el control de vuelo: dos unidades iguales y dos ordenadores",
        "Esquema de redundancia: dos unidades de referencia inercial idénticas en hardware y software, una activa y otra en reserva en caliente, y dos ordenadores de a bordo; si la activa falla y la reserva funciona, el ordenador conmuta de inmediato.",
        [("Unidad inercial 1: reserva en caliente (hardware y software idénticos)", "gold"), ("Unidad inercial 2: activa", "coral")],
        ("Control de vuelo", [("Bus de datos", "plain"), ("Ordenador de a bordo 1", "teal"), ("Ordenador de a bordo 2 (duplicado)", "teal")]),
        [("Servoválvulas y actuadores", "plain"), ("Toberas de aceleradores y de Vulcain", "plain")],
        "Lo que enseña: la redundancia protege de fallos aleatorios de un equipo y no de un error de diseño que ambos comparten. Mira que las dos unidades ejecutan el mismo programa con los mismos datos de entrada: fallan juntas, con 0,05 s de diferencia.",
        INF + " Apartados 2.1 y 3.1 (e y f).", left_labels=["datos si activa", "datos"], right_labels=["órdenes", "mandos"])


def componentes_sri() -> Fig:
    return chain(
        "Dentro de la unidad inercial: el módulo de alineación y la conversión sin protección",
        "Componentes de la unidad inercial: el módulo de alineación de la plataforma, que solo sirve antes del despegue pero seguía activo 50 segundos después de pasar a modo de vuelo; calcula el sesgo horizontal BH; la conversión de coma flotante de 64 bits a entero de 16 bits no estaba protegida; el error de operando detiene el procesador.",
        [("Modo de vuelo empieza en H0 − 3 s", "plain"), ("Alineación sigue activa 50 s: unos 40 s tras el despegue", "gold"), ("Calcula el sesgo horizontal BH (velocidad horizontal)", "plain"),
         ("Convierte BH de coma flotante de 64 bits a entero con signo de 16 bits", "coral", True), ("Valor mayor que el máximo del entero: error de operando", "coral"), ("Excepción: el procesador se detiene", "navy")],
        "Lo que enseña: el módulo que falló calculaba algo inútil después del despegue. Mira que el único paso desprotegido es la conversión: otras conversiones comparables del mismo módulo sí estaban protegidas.",
        INF + " Apartado 2.1; el informe cita las instrucciones de conversión en código Ada.", per_row=3)


def secuencia() -> Fig:
    f, y = sketch("Secuencia del fallo, de la excepción a la autodestrucción",
                  "Diagrama de secuencia con unidad inercial de reserva, unidad inercial activa, ordenador de a bordo y toberas: la reserva se detiene, la activa se detiene, envía datos de diagnóstico, el ordenador los interpreta como vuelo, ordena toberas al extremo y el lanzador se rompe.")
    y0 = y + 6
    lanes = [("Unidad inercial 1 (reserva)", "gold"), ("Unidad inercial 2 (activa)", "coral"), ("Ordenador de a bordo", "teal"), ("Toberas y lanzador", "plain")]
    steps = [(0, 0, "excepción: se detiene", "note"), (1, 1, "idem 0,05 s después", "note"), (1, 2, "envía patrón de diagnóstico", "red"),
             (2, 2, "lo lee como vuelo", "note"), (2, 3, "toberas al extremo", "red"), (3, 3, "ángulo > 20°: se rompe", "note"), (3, 3, "autodestrucción correcta", "note")]
    yy = sequence(f, y0, lanes, steps, row_h=34)
    return done(f, yy,
                "Lo que enseña: el único componente que 'funcionó' correctamente fue el ordenador, y por eso la orden errónea llegó íntegra a las toberas. El ordenador de a bordo no pudo conmutar a la reserva porque esa unidad ya se había parado en el ciclo anterior de 72 milisegundos.",
                "coral", INF + " Apartado 2.1. Reconstrucción coherente con la cadena de eventos técnicos; el orden fino lo da la comisión.")


def modelo_datos() -> Fig:
    return layers(
        "Datos que viajaban por el bus: medida, diagnóstico y el dato que se confundió",
        "Esquema de datos: el bus llevaba datos de actitud de la unidad inercial; al fallar, la unidad activa transmitió un patrón de bits de diagnóstico de su ordenador, que el ordenador de a bordo interpretó como datos de vuelo; el contexto del fallo se guardó en una memoria EEPROM recuperada.",
        [("Dato de actitud y velocidad", "doc", "Calculado en la unidad inercial a partir de la plataforma; viaja por el bus de datos al ordenador de a bordo"),
         ("Patrón de bits de diagnóstico", "doc", "Lo que la unidad activa envió al fallar; el informe dice que se interpretó como datos de vuelo (apartado 2.1, hallazgo g)"),
         ("Indicación de fallo en el bus", "doc", "La especificación pedía indicar el fallo en el bus; el ordenador la usó para conmutar, pero la reserva ya estaba parada"),
         ("Contexto del fallo en EEPROM", "doc", "Se guardó y se leyó después en los restos recuperados; permitió reconstruir la secuencia"),
         ("Variable BH (sesgo horizontal)", "doc", "Valor interno de la alineación, mucho mayor de lo esperado en la trayectoria de Ariane 5"),
         ("Datos de trayectoria de Ariane 5", "part", "No estaban en los requisitos ni en las especificaciones de la unidad inercial (apartado 2.2 y 3.1 r)")],
        "Lo que enseña: el estado correcto no faltó, faltó el dato que decía qué era cada dato. Un mensaje de diagnóstico enviado por el mismo canal que los datos de vuelo es una forma de confusión de tipos entre sistemas. Verde: documentado; dorado: dato que faltó.",
        INF + " Apartados 2.1, 2.2 y 3.1.")


def velocidad() -> Fig:
    return grouped_bars(
        "Por qué la variable se salió de rango: la velocidad horizontal crecía cinco veces más rápido",
        "Barras con valor relativo: la velocidad horizontal de Ariane 5 se acumula cinco veces más rápido que la de Ariane 4 durante los primeros 40 segundos, con Ariane 4 tomada como uno.",
        ["Ariane 4 (límite de la variable nunca alcanzado)", "Ariane 5 (límite superado antes de 40 s)"],
        [("Crecimiento relativo de la velocidad horizontal", [1, 5], "coral")],
        unit="Velocidad horizontal acumulada, relativa (Ariane 4 = 1)", horizontal=True, label_w=320, ticks=[0, 1, 2, 3, 4, 5],
        note="El informe dice 'cinco veces más rápida' y no publica el valor de BH, el límite exacto ni la trayectoria. La barra es la razón documentada, no una medición. Lo importante: el diseño era correcto para la trayectoria de Ariane 4 con margen, y el margen no se trasladó a una trayectoria distinta.",
        note_kind="gold", foot=INF + " Apartado 3.1 (o, p).")


def margen() -> Fig:
    return columns(
        "Mismo software, otro lanzador: lo que cambió y lo que no",
        "Dos columnas: Ariane 4, donde la alineación continuaba tras la cuenta atrás por una razón de operación y la trayectoria no alcanzaba el límite, y Ariane 5, donde la secuencia de preparación era distinta, la alineación no servía de nada y la aceleración inicial era mucho mayor.",
        [("Ariane 4", "teal", ["La alineación seguía activa tras el despegue para poder reiniciar la cuenta atrás sin esperar 45 minutos o más", "Esa función se usó una vez, en 1989, en el vuelo 33", "La trayectoria de los primeros 40 s deja la variable lejos del límite", "Sin fallos de este tipo en vuelos reales"]),
         ("Ariane 5", "coral", ["Secuencia de preparación distinta: la función no se necesitaba", "Se mantuvo 'por comunalidad' con un diseño que funcionaba bien", "Aceleración inicial alta; velocidad horizontal cinco veces más rápida", "Mismo programa con una trayectoria que nadie había incluido en las especificaciones"])],
        "Lo que enseña: reutilizar software probado en vuelo reduce riesgo solo si el entorno de uso es el mismo. Mira la fila central: lo que justificaba el requisito en Ariane 4 ya no existía en Ariane 5 y el requisito se quedó.",
        INF + " Apartados 2.2 y 3.1 (m a p).")


def antecedentes() -> Fig:
    f, y = sketch("Del requisito de hace diez años a la reparación de 2000, en ocho hitos",
                  "Eje no proporcional con ocho hitos: más de diez años antes un requisito de alineación para las primeras versiones de Ariane; 1989 el único uso real; 1992 se decide no incluir las unidades reales en la simulación; 4 de junio de 1996 el fallo; 13 de junio empieza la comisión; 19 de julio informe; 26 de marzo de 1997 se aprueba repetir Cluster; 2000 vuelan los cuatro satélites.")
    ev = [("Antes de 1986: requisito de alineación continuada en versiones previas", "navy"), ("1989: la función se usa una vez, en el vuelo 33", "gold"), ("1992: se decide no poner las unidades inerciales reales en la simulación", "coral"),
          ("4 jun 1996: vuelo 501, fallo a los 37 s", "coral"), ("13 jun 1996: la comisión empieza a trabajar", "teal"), ("19 jul 1996: informe de la comisión", "teal"),
          ("26 mar 1997: se aprueba repetir la misión Cluster", "gold"), ("16 jul y 9 ago 2000: lanzamiento de los cuatro satélites en Soyuz", "navy")]
    yy = equi_axis(f, y + 6, ev, box_w=170, box_h=100)
    return done(f, yy,
                "Lo que enseña: las dos decisiones que hicieron falta (conservar la alineación, simular sin la unidad real) tienen años de antigüedad y cada una era razonable en su momento. Mira que todo el consecuente (informe, repetición, repuesto) ocurre en cuatro años.",
                "gold", INF + " Apartados 2.2 y 2.3; ESA, comunicado 12-1997 y ficha de Cluster. Espaciado uniforme, no a escala.")


def pruebas() -> Fig:
    return pairs(
        "Los cuatro niveles de cualificación y lo que no cubrieron",
        "Cuatro pares: cada nivel de cualificación del control de vuelo, con lo que cubrió y lo que dejó sin cubrir respecto de la unidad inercial y la trayectoria de Ariane 5.",
        [("Cualificación del equipo: riguroso en el ambiente", "Sin ensayo con la cuenta atrás, la secuencia de vuelo y la trayectoria de Ariane 5"),
         ("Cualificación del software del ordenador de a bordo", "La unidad inercial estaba simulada por módulos de software"),
         ("Integración de etapa", "Pruebas de bajo nivel del bus: integración eléctrica, no de comportamiento"),
         ("Validación del sistema en la instalación de simulación funcional", "Unidades inerciales simuladas; decisión de 1992 con cuatro razones técnicas razonables")],
        "Lo que enseña: cada nivel confiaba en que el anterior cubría lo que él dejaba fuera. El informe lo dice así: la lógica es comprobar en cada nivel lo que no se pudo en el anterior, y aquí el hueco se heredó de nivel en nivel.",
        INF + " Apartado 2.3.", top_kind="teal", bottom_kind="coral", note_kind="coral")


def variables() -> Fig:
    return grouped_bars(
        "Siete variables en riesgo de error de operando: cuatro protegidas y tres no",
        "Barras horizontales: el análisis de vulnerabilidad encontró siete variables cuya conversión a entero podía producir error de operando; se añadió protección a cuatro y se dejaron tres sin ella, entre ellas el sesgo horizontal BH.",
        ["Variables en riesgo analizadas", "Protegidas en el código Ada", "Sin protección (incluye BH)"],
        [("Variables", [7, 4, 3], "coral")], unit="Número de variables", horizontal=True, label_w=270, ticks=[0, 2, 4, 6, 8],
        note="La razón dada fue el objetivo de carga máxima del 80 % para el ordenador de la unidad y que para las tres restantes se razonó que estaban limitadas físicamente o con gran margen; en BH ese razonamiento resultó erróneo. La decisión, dice el informe, se tomó conjuntamente por los socios y no se documentó donde un revisor externo la viera.",
        note_kind="gold", foot=INF + " Apartado 2.2.")


def prueba_de_fallos() -> Fig:
    return columns(
        "A prueba de fallos: qué había, qué falló, qué faltaba y qué debió existir",
        "Cuatro columnas: mecanismos que existían y funcionaron (autodestrucción, telemetría, recuperación de datos), que existían y fallaron (redundancia idéntica, parada del procesador), que no existían (simulación con la unidad real, datos de trayectoria en requisitos) y que debieron existir (análisis propio).",
        [("Existía y funcionó", "teal", ["Autodestrucción al romperse el lanzador, a unos 4 km", "Telemetría hasta H0 + 42 s", "Datos de contexto en EEPROM recuperados", "Cualificación de equipo muy rigurosa"]),
         ("Existía y falló", "gold", ["Dos unidades inerciales: idénticas, fallaron las dos", "Excepción de procesador: parar la unidad", "Revisiones con todos los socios: no vieron el supuesto", "Conmutación a la reserva: ya parada"]),
         ("No existía", "coral", ["Trayectoria de Ariane 5 en los requisitos de la unidad", "Declaración de límites de uso de la unidad", "Prueba con la unidad real en lazo cerrado", "Datos de mejor esfuerzo tras una excepción"]),
         ("Debió existir (análisis propio)", "navy", ["Apagar la alineación al despegar", "Simulación con unidad real y trayectoria real", "Tratar la excepción confinada, sin parar la unidad", "Revisión externa de supuestos de protección"])],
        "Lo que enseña: los mecanismos que funcionaron actuaban después del fallo; los que fallaron estaban antes. La cuarta columna es análisis propio y repite lo esencial de las recomendaciones R1, R2, R3, R5 y R6 de la comisión.",
        INF + " Apartados 2.2, 2.3, 3.1 y 4. Cuarta columna: " + ANALISIS)


def puntos_unicos() -> Fig:
    return context(
        "Puntos únicos de fallo: lo que no tenía alternativa independiente",
        "Mapa de dependencias: el programa de la unidad inercial es el mismo en las dos unidades, el supuesto sobre el rango de BH vale para ambas y el ordenador de a bordo no tiene otra fuente de actitud; un error sistemático las afecta a la vez.",
        [("Programa de la unidad inercial: idéntico en las dos unidades", "coral"), ("Supuesto sobre el rango de BH: compartido", "coral"), ("Única fuente de actitud: las unidades inerciales", "gold")],
        ("Control de vuelo", [("Ordenador de a bordo sin otro sensor de actitud", "teal"), ("Lógica de parada del procesador ante excepción", "coral")]),
        [("Toberas movidas por un dato erróneo", "plain"), ("Sin intervención humana en vuelo", "plain")],
        "Lo que enseña: un único diseño repetido dos veces es un solo punto de fallo con dos copias. Mira que todo lo rojo es lógica: se podía haber evitado con diversidad o con confinamiento de la excepción.",
        INF + " Apartado 2.2. Mapa propio sobre lo que el informe describe.", left_labels=["código", "supuesto", "datos"], right_labels=["orden", "efecto"])


def defensa() -> Fig:
    return barrier_slices(
        "Defensa en profundidad: ocho barreras y por qué ninguna detuvo el defecto",
        "Láminas con huecos alineados: la especificación de la unidad, el análisis de variables, la revisión por socios, la prueba de equipo, la simulación del sistema, la lógica de excepción, la redundancia y la telemetría; una flecha roja las atraviesa.",
        [("Requisitos de la unidad (sin trayectoria)", "coral"), ("Análisis de variables (3 sin proteger)", "gold"), ("Revisiones de diseño (no vieron el supuesto)", "gold"), ("Prueba de equipo (sin trayectoria)", "gold"),
         ("Simulación (unidad inercial simulada)", "coral"), ("Excepción (detiene la unidad)", "coral"), ("Reserva idéntica", "coral"), ("Telemetría (diagnóstica, no preventiva)", "gold")],
        "Lo que enseña: no es que faltara una sola barrera; es que los huecos estaban alineados por el mismo supuesto. Rojo: la barrera fallaba por diseño; dorado: existía y era parcial. Los huecos son una metáfora, no una medida.",
        INF + " Apartados 2.2 y 2.3. " + ANALISIS)


def arbol() -> Fig:
    return fault_tree(
        "Árbol de fallas: qué tuvo que coincidir para perder el vuelo",
        "Árbol de fallas con la pérdida del vuelo 501 arriba y dos ramas necesarias: que las unidades inerciales dejaran de dar actitud, que requiere cuatro condiciones, y que el control tratara el diagnóstico como dato de vuelo, que requiere tres.",
        "Pérdida del vuelo 501 a los 39 s",
        ("A. Se pierde la información de actitud", "Y", ["Alineación activa tras el despegue", "Trayectoria con velocidad horizontal cinco veces mayor", "Conversión de BH sin protección", "Las dos unidades con el mismo programa"]),
        ("B. El control ejecuta una orden absurda", "Y", ["Excepción detiene el procesador", "El diagnóstico viaja por el bus de datos", "El ordenador lo interpreta como datos de vuelo"]),
        "Lo que enseña: cortar una sola condición habría roto la rama. Mira que la rama A está llena de decisiones de diseño y la B de decisiones de tratamiento de errores. Estructura lógica propia sobre la cadena que el informe establece 'sin duda razonable'.",
        INF + " Apartado 2.1. " + ANALISIS)


def controles() -> Fig:
    return pairs(
        "Cada eslabón de la cadena y el control que lo corta",
        "Ocho pares de causa y control propuesto: la alineación activa en vuelo, las variables sin proteger, la trayectoria fuera de los requisitos, la simulación sin la unidad real, la parada del procesador, la reserva idéntica, la revisión interna y la telemetría insuficiente.",
        [("Alineación activa en vuelo", "Apagarla al despegar (R1 de la comisión)"), ("Tres variables sin proteger", "Revisar el rango de toda variable interna o de comunicación (R5)"),
         ("Trayectoria fuera de los requisitos", "Incluir la trayectoria en las especificaciones y pruebas (R10)"), ("Simulación sin la unidad real", "Probar con el máximo de equipo real y lazo cerrado (R2)"),
         ("Procesador que se detiene", "Confinar excepciones a tareas y prever respaldos (R6)"), ("Sensor que deja de dar datos", "Obligar a seguir enviando datos de mejor esfuerzo (R3)"),
         ("Revisiones sin un tercero", "Revisiones con participantes externos al proyecto (R9)"), ("Telemetría escasa", "Más datos al fallar un componente (R7)")],
        "Lo que enseña: cada recomendación de la comisión corta un eslabón concreto. Verde es la mejora; la etiqueta R indica la recomendación publicada. La asignación de cada eslabón a cada R es análisis propio.",
        INF + " Apartado 4. " + ANALISIS)


def despues() -> Fig:
    return chain(
        "La arquitectura 'después': qué cambia en el control de vuelo",
        "Cadena objetivo: la alineación se desactiva tras el despegue; la unidad sigue enviando su mejor estimación aunque haya una excepción; las excepciones se confinan a la tarea; las pruebas incluyen la unidad real, la trayectoria real y el lazo cerrado; las revisiones incluyen expertos externos.",
        [("Alineación apagada tras el despegue (R1)", "teal"), ("Excepción confinada a la tarea, sin parar el procesador (R6)", "teal"), ("La unidad sigue enviando mejor estimación (R3)", "teal"),
         ("Trayectoria en requisitos y límites de uso declarados (R10, R4)", "teal"), ("Pruebas en lazo cerrado con equipo real (R2, R11)", "teal"), ("Revisión con expertos externos del proyecto (R9, R5)", "teal")],
        "Lo que enseña: el cambio es menos de código y más de supuestos explícitos: un límite declarado, una trayectoria como requisito, una prueba con la unidad real. Diseño didáctico apoyado en las recomendaciones; no describe el sistema finalmente adoptado.",
        INF + " Apartado 4. " + ANALISIS, per_row=3, note_kind="teal")


def recomendaciones() -> Fig:
    return grouped_bars(
        "Las 14 recomendaciones de la comisión, agrupadas por tema",
        "Barras horizontales: cuatro temas de las 14 recomendaciones; cinco de diseño y manejo de errores del software, cinco de revisión y cualificación, tres de pruebas y una de organización.",
        ["Diseño y tratamiento de errores", "Revisión y cualificación de software", "Pruebas y cobertura", "Organización de los socios"],
        [("Recomendaciones", [5, 5, 3, 1], "teal")], unit="Número de recomendaciones", horizontal=True, label_w=270, ticks=[0, 2, 4, 6],
        note="La agrupación es propia: diseño (R1, R3, R6, R7, R8), revisión (R4, R5, R9, R12, R13), pruebas (R2, R10, R11), organización (R14). La comisión las lista sin agrupar. El recuento es 14 y está documentado.",
        note_kind="gold", foot=INF + " Apartado 4. Agrupación propia.")


def consecuencias() -> Fig:
    return chain(
        "Consecuencias fechadas: del vuelo perdido al repuesto de Cluster",
        "Cadena de consecuencias: vuelo 501 destruido el 4 de junio de 1996; la comisión informa el 19 de julio; el 26 de marzo de 1997 se aprueba repetir la misión con coste adicional de 214 millones de ecus; los cuatro satélites vuelan en 2000 en lanzadores Soyuz.",
        [("4 jun 1996: pérdida del vuelo y de la carga útil", "coral"), ("19 jul 1996: informe y recomendaciones", "teal"), ("26 mar 1997: se aprueba el reenvío con coste adicional de 214 MECU", "gold"), ("16 jul y 9 ago 2000: lanzamiento de los cuatro satélites en Soyuz", "navy")],
        "Lo que enseña: el coste documentado de repetir la misión (214 MECU) es la parte medible; el coste del retraso al programa Ariane 5 no figura en las fuentes consultadas y no se inventa. Mira que el lanzador cambió: la repetición no usó Ariane 5.",
        "Fuentes: ESA, comunicado 12-1997 y ficha de Cluster; informe de la comisión.")


def cadena_causal() -> Fig:
    return chain(
        "La cadena de eventos técnicos, de la causa a la destrucción",
        "Cadena causal en nueve pasos: requisito heredado de alineación; BH mayor de lo esperado; conversión sin protección; error de operando; parada de la unidad de reserva y de la activa; diagnóstico interpretado como datos; toberas al extremo; ruptura; autodestrucción.",
        [("Requisito heredado: alineación 50 s tras el modo de vuelo", "navy"), ("Trayectoria de Ariane 5: BH mucho mayor", "gold"), ("Conversión de 64 a 16 bits sin protección", "coral"), ("Error de operando: excepción", "coral"),
         ("Se paran la reserva y 0,05 s después la activa", "coral"), ("Diagnóstico leído como datos de vuelo", "coral"), ("Toberas a fondo: ángulo de ataque > 20°", "coral"), ("Ruptura a H0 + 39 s y autodestrucción", "navy")],
        "Lo que enseña: son ocho pasos y cada uno es una decisión o una consecuencia distinta; cortar cualquiera habría evitado la pérdida. La comisión dice que la cadena está establecida 'sin duda razonable' y que la simulación posterior la reprodujo fielmente.",
        INF + " Apartados 2.1 y 3.1.", per_row=4)


def cultura() -> Fig:
    return columns(
        "Dos modelos de error: fallo aleatorio de hardware frente a error sistemático de software",
        "Dos columnas: el supuesto de diseño, que cualquier excepción era un fallo aleatorio de hardware que el equipo de reserva resolvería, y lo ocurrido, un error sistemático idéntico en ambos equipos.",
        [("Supuesto de diseño", "gold", ["Una excepción es un fallo aleatorio de hardware", "Se informa del fallo, se guarda el contexto y se detiene la unidad", "La reserva toma el control", "El software es correcto hasta que se demuestre lo contrario"]),
         ("Lo que ocurrió", "coral", ["La excepción era un error de diseño, no aleatorio", "El mismo programa en la reserva produjo la misma excepción", "Dos unidades sanas apagadas a la vez", "El informe defiende el criterio opuesto: asumir el software defectuoso hasta demostrar lo contrario"])],
        "Lo que enseña: el criterio de manejo de errores condiciona todo lo demás. Mira que el proveedor de la unidad cumplió la especificación recibida: la causa está en la especificación y en el modelo de fallo, no en un incumplimiento.",
        INF + " Apartado 2.2.")


def hardware_software() -> Fig:
    return layers(
        "Qué se sabe de la pila: lo que el informe documenta y lo que no",
        "Capas de la pila técnica: sensores inerciales de láser documentados; ordenador interno de la unidad documentado; lenguaje Ada documentado; bus de datos documentado; procesador, sistema operativo y compilador no se publican.",
        [("Sensores", "doc", "Giróscopos láser y acelerómetros en una plataforma 'strap-down'"),
         ("Ordenador de la unidad", "doc", "Calcula ángulos y velocidades; objetivo de carga máxima del 80 %; procesador no identificado"),
         ("Lenguaje", "doc", "Ada, con instrucciones de conversión citadas por el informe"),
         ("Comunicación", "doc", "Bus de datos entre unidades y ordenadores; periodo de ciclo de 72 ms para la conmutación"),
         ("Actuadores", "doc", "Servoválvulas y actuadores hidráulicos para toberas de aceleradores y de Vulcain"),
         ("Proveedor, procesador, compilador, sistema operativo", "unk", "No constan en el informe; este caso no los inventa")],
        "Lo que enseña: el informe da el nivel de detalle necesario para entender el fallo, no el de una documentación del sistema. Verde: documentado; gris: no se sabe.",
        INF + " Apartados 2.1 y 2.2.")


def negocio() -> Fig:
    return chain(
        "Esquema de la operación: del programa de la ESA al lanzamiento comercial",
        "Esquema de operación: los Estados miembros financian el programa a través de la ESA, el CNES dirige la base de Kourou, la industria construye lanzador y equipos, el lanzador pone en órbita cargas útiles científicas y comerciales; el vuelo 501 era el primer vuelo de cualificación.",
        [("Estados miembros y ESA: programa y financiación", "navy"), ("CNES y base de Kourou: campaña y operación", "teal"), ("Industria: lanzador, motor, unidades inerciales", "plain"), ("Cargas útiles: primera, la misión científica Cluster", "gold")],
        "Lo que enseña: es un esquema de roles; el informe no describe contratos ni importes. La ESA indica que Ariane 5 voló 117 veces entre 1996 y 2023 (ficha de la ESA). Cifras económicas del programa: no se sabe a partir de estas fuentes.",
        INF + " Prólogo; ESA, ficha de Ariane 5. Roles propios sobre lo que el prólogo menciona.")


def lecciones() -> Fig:
    return columns(
        "Qué aprender y qué no generalizar de este caso",
        "Dos columnas: lo que se transfiere (hacer explícitos los supuestos de rango, probar con las condiciones reales, no reutilizar sin revisar el entorno) y lo que no (no prueba que el software crítico no pueda reutilizarse ni que la redundancia sea inútil).",
        [("Se transfiere", "teal", ["Un supuesto de rango que no está escrito no se revisa", "Reutilizar es seguro solo en el mismo entorno", "Una prueba con el componente simulado no prueba el componente", "Si un error es sistemático, la reserva idéntica no ayuda"]),
         ("No se generaliza", "gold", ["No prueba que Ada o la conversión de tipos sean inseguros: era una decisión de proteger o no", "No prueba que la reutilización sea mala", "No es un fallo de una persona: la comisión señala decisiones conjuntas de los socios", "Las cifras (37 s, 0,05 s) son de un vuelo concreto"])],
        "Lo que enseña: el aprendizaje correcto es sobre explicitar supuestos y probar el sistema completo. Mira la columna derecha: el caso se usa mal cuando se cita para culpar a un lenguaje o a un proveedor.",
        INF + " Apartados 2.2 y 3. Lectura propia.")


FIGURES = {
    "ariane-5-vuelo-501-contexto.svg": contexto,
    "ariane-5-vuelo-501-comision.svg": organizacion,
    "ariane-5-vuelo-501-sedes.svg": sedes,
    "ariane-5-vuelo-501-segundos-decisivos.svg": secuencia_tiempos,
    "ariane-5-vuelo-501-control-de-vuelo.svg": funcionamiento,
    "ariane-5-vuelo-501-redundancia.svg": redundancia,
    "ariane-5-vuelo-501-dentro-de-la-unidad.svg": componentes_sri,
    "ariane-5-vuelo-501-secuencia.svg": secuencia,
    "ariane-5-vuelo-501-datos-del-bus.svg": modelo_datos,
    "ariane-5-vuelo-501-velocidad-horizontal.svg": velocidad,
    "ariane-5-vuelo-501-ariane-4-y-5.svg": margen,
    "ariane-5-vuelo-501-antecedentes.svg": antecedentes,
    "ariane-5-vuelo-501-cualificacion.svg": pruebas,
    "ariane-5-vuelo-501-variables.svg": variables,
    "ariane-5-vuelo-501-a-prueba-de-fallos.svg": prueba_de_fallos,
    "ariane-5-vuelo-501-puntos-unicos.svg": puntos_unicos,
    "ariane-5-vuelo-501-defensa-en-profundidad.svg": defensa,
    "ariane-5-vuelo-501-arbol-de-fallas.svg": arbol,
    "ariane-5-vuelo-501-controles.svg": controles,
    "ariane-5-vuelo-501-arquitectura-despues.svg": despues,
    "ariane-5-vuelo-501-recomendaciones.svg": recomendaciones,
    "ariane-5-vuelo-501-consecuencias.svg": consecuencias,
    "ariane-5-vuelo-501-cadena-causal.svg": cadena_causal,
    "ariane-5-vuelo-501-modelos-de-error.svg": cultura,
    "ariane-5-vuelo-501-hardware-y-software.svg": hardware_software,
    "ariane-5-vuelo-501-esquema-de-la-operacion.svg": negocio,
    "ariane-5-vuelo-501-que-aprender.svg": lecciones,
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
