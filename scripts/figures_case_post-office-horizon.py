"""Figures for the failure case study Post Office Horizon (Reino Unido, 1999-2025).

Every number comes from the public sources cited in each footer: the High Court judgment Bates v Post Office (No 6),
the Court of Appeal judgment Hamilton v Post Office, the Post Office (Horizon System) Offences Act 2024 and the
Post Office Horizon IT Inquiry. The case speaks about systems and decisions, not about persons.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_generic import barrier_slices, chain, columns, context, done, fault_tree, layers, pairs  # noqa: E402
from case_fig_helpers_fallo import equi_axis, sketch  # noqa: E402
from figure_kit import Fig, grouped_bars, timeline  # noqa: E402

BATES = "Fuente: Bates v Post Office (n.º 6), [2019] EWHC 3408 (QB)."
CA = "Fuente: Hamilton v Post Office, [2021] EWCA Crim 577."
INQ = "Fuente: Post Office Horizon IT Inquiry, informe final, vol. 1 (jul 2025)."
ACT = "Fuente: Post Office (Horizon System) Offences Act 2024."
ANALISIS = "Análisis propio, no conclusión de los tribunales ni de la investigación."


def contexto() -> Fig:
    return context(
        "Quién estaba en cada lado del mostrador de Horizon",
        "Diagrama de contexto: el Post Office contrata a subpostmasters que atienden sucursales; el sistema Horizon, proporcionado por Fujitsu, registra las transacciones y produce las cuentas de cada sucursal; el propio Post Office usaba esas cuentas para reclamar faltantes y, en algunos casos, para perseguir penalmente; tribunales, Parlamento e investigación pública revisaron lo ocurrido.",
        [("Post Office: operador de la red, empleador o contratante y, en estos casos, acusador", "navy"), ("Subpostmasters, gerentes y ayudantes de mostrador", "plain"), ("Clientes de las sucursales", "plain")],
        ("Sistema Horizon", [("Terminales en los mostradores de las sucursales", "teal"), ("Cuentas de la sucursal y balance periódico", "coral"), ("Servicio de asistencia y registros internos del proveedor", "gold")]),
        [("Fujitsu: proveedor y soporte técnico", "plain"), ("Tribunales: High Court y Court of Appeal", "teal"), ("Parlamento, Gobierno como accionista e investigación pública", "navy")],
        "Lo que enseña: quien operaba la red, quien reclamaba el dinero y, a veces, quien perseguía penalmente era la misma organización, y la prueba central era un sistema que el otro lado no podía examinar. La caja roja es la que los tribunales sometieron a examen.",
        BATES + " " + CA, left_labels=["contrata", "opera", "atiende"], right_labels=["suministra", "juzgan", "supervisan"])


def fuentes() -> Fig:
    return columns(
        "Qué se ha examinado y quién lo ha hecho: cuatro tipos de fuente pública",
        "Tres columnas: la High Court examinó el sistema en 2019, el Court of Appeal anuló condenas en 2021 y el Parlamento legisló en 2024; la investigación pública estatutaria publicó el volumen 1 de su informe final en julio de 2025, centrado en el impacto humano y la reparación.",
        [("Tribunales", "teal", ["High Court, 16 de diciembre de 2019: Bates v Post Office (n.º 6), sobre el funcionamiento de Horizon", "Court of Appeal (Criminal Division), 23 de abril de 2021: Hamilton v Post Office, sobre 42 apelaciones remitidas por la CCRC"]),
         ("Parlamento", "navy", ["Post Office (Horizon System) Offences Act 2024, sancionada el 24 de mayo de 2024: anula las condenas incluidas en su ámbito y regula la eliminación de amonestaciones"]),
         ("Investigación pública", "gold", ["Informe final, volumen 1: 8 de julio de 2025, sobre el impacto humano y la reparación", "Quedan por publicar los demás volúmenes: el resultado técnico y de gobierno no se conoce todavía en este caso"])],
        "Lo que enseña: los tribunales establecieron lo que se puede afirmar sobre el sistema y los procesos; la investigación pública aún no ha publicado su examen del desarrollo y de la gobernanza. Mira la tercera columna: este caso no inventa lo que esa investigación todavía no ha dicho.",
        "Fuentes: judgments de Bates (2019) y Hamilton (2021); Act 2024; Post Office Horizon IT Inquiry.")


def dia_a_dia() -> Fig:
    return chain(
        "Cómo se llegaba de una transacción a una deuda: el flujo de una sucursal",
        "Cadena del flujo contable de una sucursal: cada transacción se registra en el terminal; Horizon acumula las cuentas; al cierre del periodo la sucursal acepta el balance; si aparece un faltante, el contrato o la práctica del Post Office lo trataba como deuda del subpostmaster; el subpostmaster podía llamar a la asistencia, pero no había función de disputa en el sistema.",
        [("Transacciones registradas en el terminal de la sucursal", "plain"), ("Horizon acumula las cuentas de la sucursal", "teal"), ("Cierre de periodo: el subpostmaster acepta el balance", "gold"), ("Aparece un faltante en las cuentas", "coral"),
         ("Llamada a la asistencia; sin función de disputa en el sistema", "gold", True), ("El faltante se trata como deuda que hay que cubrir", "coral"), ("Descuentos de la remuneración o cese", "navy")],
        "Lo que enseña: el sistema no ofrecía a quien veía un faltante un camino para marcarlo como disputado; el único modo de plantear un problema era una llamada. Mira la quinta caja: fue una decisión de diseño documentada, no una omisión.",
        BATES + " " + CA, per_row=4)


def sin_disputa() -> Fig:
    return columns(
        "Qué pasaba cuando un subpostmaster discutía un faltante",
        "Dos columnas: lo que el Post Office sostuvo durante años, que Horizon era fiable, que el faltante era real y que cada subpostmaster debía demostrar que no era responsable; y lo que los tribunales encontraron sobre cómo se trataba la disputa.",
        [("Posición del Post Office durante años", "gold", ["Horizon era fiable", "El faltante era real y no un artefacto del sistema", "Si el subpostmaster no podía demostrar lo contrario, debía cubrirlo", "Un informe interno de 2010 consideraba que cualquier duda sobre el sistema afectaría a las acusaciones"]),
         ("Lo que encontraron los tribunales", "coral", ["Las disputas por la asistencia se trataban como deudas no discutidas", "Como máximo se ofrecía tiempo para pagar: descuentos durante doce meses", "Los subpostmasters no tenían modo de disputar los faltantes dentro de Horizon", "Tenían una desventaja importante de acceso a la información"])],
        "Lo que enseña: un sistema contable sin vía de disputa convierte cada discrepancia en una afirmación de culpa del usuario. Las dos columnas son hechos que recogen los tribunales; la primera es la posición de una parte.",
        CA + " Apartados 20 a 24 y 56.")


def documentos() -> Fig:
    return chain(
        "Dónde se guardaban los errores conocidos y por qué no llegaban a los acusados",
        "Cadena de los registros internos de Fujitsu: cuando un subpostmaster llamaba a la asistencia y el caso pasaba a la sección técnica se creaba un documento llamado PEAK; los PEAK alimentaban un registro de errores conocidos llamado KEL; el Post Office tenía derecho contractual a esa información; en los procesos contra los 42 apelantes no consta que se divulgara ninguno.",
        [("Llamada del subpostmaster a la asistencia", "plain"), ("Fujitsu crea un registro de incidencia (PEAK)", "teal"), ("Los PEAK alimentan el registro de errores conocidos (KEL)", "teal"), ("El Post Office tiene derecho contractual a esa información", "gold"), ("En los 42 procesos de la apelación no consta divulgación", "coral", True)],
        "Lo que enseña: el conocimiento de que el sistema tenía defectos existía en un registro interno del proveedor y no llegó a quien se defendía. Mira la última caja: es una ausencia de divulgación, no una conclusión sobre intenciones.",
        CA + " Apartados 17 y 18.", per_row=3)


def bugs() -> Fig:
    return layers(
        "Defectos reconocidos y cómo se vieron en las sucursales",
        "Capas con ejemplos de defectos que consideró el tribunal: el error de Callendar Square, descubierto en 2005 y admitido después por el Post Office, que causó discrepancias en las cuentas; el error de Dalmellington; los desajustes entre recibos y pagos; y el mínimo de 11 errores aceptados por el experto del Post Office.",
        [("Callendar Square", "doc", "Descubierto en 2005 en una sucursal; admitido por el Post Office como error; causó discrepancias en las cuentas (en un caso, un faltante de 6 414,46 libras)"),
         ("Dalmellington", "doc", "El tribunal lo compara con la experiencia de un subpostmaster experimentado que transfirió 2 000 libras entre terminales y vio desaparecer esa suma"),
         ("Desajuste de recibos y pagos", "doc", "Uno de los efectos que figuran en un cuadro de 30 sucursales analizado en el juicio, junto con otros como pantallas congeladas y problemas de declaraciones"),
         ("Cifra mínima aceptada por el experto del Post Office", "doc", "Once errores distintos; el tribunal aceptó más, siguiendo al experto de los demandantes"),
         ("Origen exacto de cada incidente individual", "unk", "El tribunal advierte que el método de un experto no permitía atribuir cada incidente a un error concreto; no se sabe la causa de muchos casos")],
        "Lo que enseña: no es una lista de todos los defectos de Horizon, sino ejemplos que el tribunal examinó. Verde: documentado en la sentencia; gris: no se sabe. Mira la última fila: la ausencia de una causa por incidente no implica que no la hubiera.",
        BATES + " Apartados 404 y 925 a 930.")


def robustez() -> Fig:
    return columns(
        "Qué significa «robusto»: dos definiciones que se discutieron en el juicio",
        "Dos columnas con las definiciones de robustez de los dos expertos: el de los demandantes la define como capacidad de un sistema de funcionar correctamente en cualquier escenario, con tratamiento eficaz de errores; el del Post Office como objetivo de ingeniería frente a riesgos concretos, que no significa ser perfecto sino abordar los riesgos de la imperfección.",
        [("Experto de los demandantes", "coral", ["Capacidad de resistir y superar condiciones adversas", "El sistema debe funcionar correctamente en cualquier escenario, incluidas entradas inválidas, con tratamiento eficaz de errores", "Horizon no era robusto: muchos errores, fallos de mecanismos de integridad, discrepancias que no se detectaban y procesos manuales para modificar datos"]),
         ("Experto del Post Office", "teal", ["Robustez frente a riesgos concretos: fallos de hardware, de comunicaciones, errores de usuario, fraude", "No significa ser perfecto: significa abordar los riesgos de la imperfección", "El nivel de robustez pudo variar a lo largo de la vida del sistema"])],
        "Lo que enseña: el desacuerdo no era sobre si había errores, que ambos aceptaron, sino sobre cuánto importaban. El juez prefirió el enfoque de quien partió de incidentes concretos; esa valoración es suya, no de este caso.",
        BATES + " Apartados 40 a 42 y 925.")


def remoto() -> Fig:
    return columns(
        "Quién podía ver y modificar qué: la asimetría de información",
        "Dos columnas: lo que veía y podía hacer el subpostmaster, con acceso a su propia sucursal y sin forma de disputar en el sistema, y lo que podían ver y hacer Fujitsu y el Post Office, con acceso remoto extenso, registros internos de errores y capacidad, en algunos casos, de modificar cuentas sin conocimiento del subpostmaster.",
        [("Subpostmaster", "gold", ["Veía las cuentas de su sucursal y los errores que el sistema le mostraba", "No tenía modo de disputar un faltante en Horizon", "Desventaja importante de acceso a información para investigar", "No conocía el contenido de los registros internos"]),
         ("Fujitsu y Post Office", "teal", ["Acceso remoto extenso a las cuentas de sucursal", "Algunas cuentas se alteraron sin que lo supiera el subpostmaster y en las cuentas aparecía como si lo hubiera hecho él", "Registros internos de errores conocidos (PEAK y KEL)", "Derecho contractual a la información de Fujitsu"])],
        "Lo que enseña: un sistema en el que un lado puede reescribir el registro sin dejar rastro visible para el otro no sirve como prueba contra ese otro. La afirmación sobre las modificaciones es el resumen de la CCRC de los hallazgos del juez.",
        CA + " Apartado 56 (xi, viii, ix).")


def condenas() -> Fig:
    return grouped_bars(
        "El Court of Appeal anuló 39 de las 42 condenas que examinó",
        "Barras horizontales con las apelaciones de la sentencia Hamilton: 42 apelaciones remitidas por la CCRC, 39 estimadas con las condenas anuladas y 3 desestimadas.",
        ["Apelaciones remitidas por la CCRC", "Estimadas: condenas anuladas", "Desestimadas"],
        [("Apelaciones", [42, 39, 3], "teal")], unit="Número de apelaciones", horizontal=True, label_w=270, ticks=[0, 10, 20, 30, 40, 50],
        note="Las 42 son un subconjunto de los casos de la red: es el grupo que la CCRC remitió al tribunal, no el total de personas procesadas. El Act de 2024 anula, además, las condenas de Inglaterra, Gales e Irlanda del Norte del ámbito de la ley que no hubieran sido consideradas por el Court of Appeal.",
        note_kind="gold", foot=CA + " Apartado 447; " + ACT)


def investigacion() -> Fig:
    return grouped_bars(
        "La escala de la investigación pública: días, testigos y documentos",
        "Barras horizontales en escala logarítmica con la actividad de la investigación hasta el informe de julio de 2025: 226 días de audiencias, 298 testigos con declaración oral y unos 274 604 documentos aportados.",
        ["Días de audiencias", "Testigos con declaración oral", "Documentos aportados"],
        [("Cantidad", [226, 298, 274604], "navy")], unit="Cantidad (escala logarítmica)", horizontal=True, log=True, label_w=270,
        note="La escala es logarítmica porque el número de documentos es mil veces mayor que los otros dos; no compares longitudes. Son cifras de actividad del proceso, no de resultados.",
        note_kind="gold", foot=INQ)


def antecedentes() -> Fig:
    f, y = sketch("De Pathway a la ley de 2024, en nueve hitos",
                  "Eje no proporcional con nueve hitos: 1996-1999 proyecto Pathway; 2000 Legacy Horizon; 2005 error de Callendar Square; 2009 informe de Computer Weekly; agosto de 2010 informe interno sobre integridad del sistema; 2010 Horizon Online; julio de 2012 revisión de Second Sight; diciembre de 2019 sentencia Bates; abril de 2021 anulación de 39 condenas.")
    ev = [("1996-1999: proyecto Pathway con ICL, el Post Office y la Agencia de Prestaciones", "navy"), ("2000: Legacy Horizon en uso (hasta 2010)", "navy"), ("2005: error de Callendar Square", "coral"), ("2009: Computer Weekly informa de problemas", "gold"),
          ("Ago 2010: informe interno afirma que Horizon es robusto", "gold"), ("2010: entra Horizon Online", "navy"), ("Jul 2012: Second Sight revisa el sistema", "teal"), ("16 dic 2019: sentencia Bates (n.º 6)", "teal"), ("23 abr 2021: se anulan 39 condenas", "teal")]
    yy = equi_axis(f, y + 6, ev, box_w=170, box_h=110)
    return done(f, yy,
                "Lo que enseña: pasaron seis años entre la primera señal pública en 2009 y las primeras solicitudes a la CCRC en 2015, y más de diez hasta la sentencia. Mira que la revisión de 2012 llegó dos años después de un informe interno que ponderó las consecuencias de dudar.",
                "gold", BATES + " " + CA, )


def decadas() -> Fig:
    return timeline(
        "Tres décadas: versiones del sistema, litigio y reparación",
        "Línea de tiempo en años de 1996 a 2026: desarrollo de Pathway de 1996 a 1999; Legacy Horizon de 2000 a 2010; Horizon Online desde 2010; el litigio civil y penal entre 2012 y 2021; la ley de 2024 y la investigación pública hasta 2025.",
        [("Desarrollo (Pathway)", [(1996, 1999.9, "Pathway", "grey")]),
         ("Legacy Horizon", [(2000, 2010, "Legacy Horizon (2000-2010)", "coral")]),
         ("Horizon Online", [(2010, 2025.5, "Horizon Online desde 2010", "navy")]),
         ("Revisión y litigio", [(2012.5, 2021.4, "litigio y apelación", "teal")]),
         ("Reparación", [(2024.4, 2025.6, "", "gold")])],
        unit="Año", events=[(2019.96, "2019"), (2024.4, "2024")], ticks=[1996, 2000, 2005, 2010, 2015, 2020, 2025], t_max=2026, label_w=190,
        note="Los años de inicio y fin de cada versión son los que dan los tribunales (2000-2010 para Legacy Horizon). Horizon Online aparece hasta 2025 como barra de presencia, no como fecha de retirada: las fuentes verificadas no dan una fecha de sustitución. Las marcas son la sentencia de 2019 y la ley de 2024.",
        note_kind="gold", foot=BATES + " " + CA)


def hallazgos() -> Fig:
    return layers(
        "Siete de los once hallazgos del juez, según la CCRC, que fundaron la apelación",
        "Capas con siete hallazgos del juez de la High Court, tal como los resumió la CCRC y los recoge el tribunal de apelación: Legacy Horizon no era robusto; había riesgo de inexactitud en las cuentas; existía evidencia independiente; el Post Office no reveló la fiabilidad real; la investigación era pobre; los subpostmasters estaban en desventaja; el acceso remoto era extenso.",
        [("Fiabilidad", "doc", "Legacy Horizon no era robusto en absoluto; HNG-X algo más, pero con un número significativo de errores"),
         ("Riesgo de inexactitud", "doc", "Había un riesgo significativo y material de inexactitud en las cuentas por errores y defectos; los faltantes pudieron deberse a Horizon entre 2000 y 2010 y después"),
         ("Evidencia independiente", "doc", "Los ingenieros de Royal Mail y los auditores del Post Office respaldaban la versión de los subpostmasters"),
         ("Divulgación", "doc", "El Post Office no reveló a los subpostmasters la situación completa y exacta sobre la fiabilidad del sistema"),
         ("Investigación", "doc", "La posición por defecto era que el subpostmaster debía ser el responsable; el nivel de investigación era pobre"),
         ("Capacidad de defensa", "doc", "Los subpostmasters estaban en clara desventaja de acceso a la información y no podían disputar faltantes en Horizon"),
         ("Acceso remoto", "doc", "Extenso; algunas cuentas se modificaron sin conocimiento del subpostmaster y aparecían como acciones suyas")],
        "Lo que enseña: son hallazgos del juez resumidos por la CCRC, no del autor de este caso. Mira que solo uno trata del software; los otros seis son de proceso, información y gobierno.",
        CA + " Apartados 56 y 57.")


def puntos_unicos() -> Fig:
    return context(
        "Dependencias de un único elemento en la cadena de la prueba",
        "Mapa de dependencias: Horizon como única fuente de verdad sobre el dinero; ausencia de función de disputa; una sola organización que reclama la deuda y decide perseguir; los registros de errores conocidos fuera de la vista de la defensa; cada punto sin alternativa independiente.",
        [("Horizon como única fuente de verdad del dinero de la sucursal", "coral"), ("Sin función de disputa en el sistema", "coral"), ("Registros de errores en manos del proveedor", "gold")],
        ("Cadena de la prueba", [("Cuentas de Horizon como prueba central", "coral"), ("Decisión de reclamar y de perseguir en el mismo organismo", "gold")]),
        [("Subpostmaster: carga de demostrar que no era responsable", "plain"), ("Tribunal: recibía las cuentas sin los registros de errores", "plain")],
        "Lo que enseña: cada punto solo no basta, pero juntos hacían que una afirmación del sistema se convirtiera en un hecho para el tribunal. Rojo: decisiones de diseño o de proceso; dorado: dependencias de información.",
        BATES + " " + CA + " " + ANALISIS, left_labels=["fuente", "sin vía", "fuera de vista"], right_labels=["carga", "recibe"])


def defensa() -> Fig:
    return barrier_slices(
        "Defensa en profundidad: ocho barreras y por qué no frenaron el daño",
        "Láminas con huecos alineados: función de disputa en el sistema, soporte técnico, divulgación de errores conocidos, revisión independiente, investigación de cada faltante, valoración de la fiabilidad por quien acusa, contraste con auditores e ingenieros, gobierno y supervisión.",
        [("Función de disputa en el sistema (decidió no tenerla)", "coral"), ("Asistencia técnica (trataba el faltante como deuda)", "gold"), ("Divulgación de errores conocidos (no consta)", "coral"), ("Revisión independiente (Second Sight, 2012)", "gold"),
         ("Investigación de cada faltante (pobre)", "gold"), ("Valoración de la fiabilidad por quien acusaba", "coral"), ("Contraste con auditores e ingenieros (se ignoró)", "gold"), ("Supervisión de gobierno y de accionista", "gold")],
        "Lo que enseña: los huecos coinciden porque los controles eran del mismo organismo que tenía interés en que el sistema fuera fiable. Rojo: ausente o fallida; dorado: existía y fue parcial. Es una metáfora, no una medición.",
        CA + " " + BATES + " " + ANALISIS)


def arbol() -> Fig:
    return fault_tree(
        "Árbol de fallas: qué tuvo que coincidir para que las discrepancias fueran condenas",
        "Árbol de fallas con condenas y deudas erróneas arriba y dos ramas necesarias: que Horizon mostrara discrepancias que no existían, con tres condiciones, y que la organización las tratara como hechos probados, con cinco.",
        "Condenas y deudas erróneas",
        ("A. Horizon muestra faltantes que no eran reales", "Y", ["Errores y defectos con riesgo material de inexactitud", "Acceso remoto que podía modificar cuentas sin conocimiento del subpostmaster", "Sin forma de detectar y registrar la discrepancia como discutida"]),
        ("B. La organización los trata como hechos", "Y", ["Contrato y práctica: el faltante debía cubrirse", "Posición de que el sistema era fiable", "Errores conocidos no divulgados a la defensa", "Investigación pobre; carga de la prueba sobre el subpostmaster", "Quien reclamaba era también quien perseguía"]),
        "Lo que enseña: cortar cualquier condición de A o de B habría debilitado la cadena. Mira que A es técnica y B es institucional, y que B tiene más condiciones: es más fácil cortarla por B. Estructura lógica propia sobre lo que los tribunales establecen.",
        CA + " " + BATES + " " + ANALISIS)


def prueba_de_fallos() -> Fig:
    return columns(
        "A prueba de fallos: qué existía, qué falló, qué no existía y qué debió existir",
        "Cuatro columnas: mecanismos que existían y funcionaron (registro interno de errores, revisión posterior, tribunales), que existían y fallaron (asistencia, contrato, valoración de fiabilidad), que no existían (función de disputa, divulgación, independencia de la acusación) y que debieron existir (análisis propio).",
        [("Existía y funcionó", "teal", ["Registro de incidencias y errores conocidos (PEAK y KEL)", "Contraste con ingenieros y auditores que anotaron los hechos", "Revisión judicial del sistema en 2019", "Remisión de la CCRC al tribunal de apelación"]),
         ("Existía y falló", "gold", ["Asistencia: trataba los faltantes como deuda", "Valoración interna de 2010: el sistema era robusto", "Contrato y prácticas de reclamación", "Revisión de 2012: llegó tarde"]),
         ("No existía", "coral", ["Función de disputa en Horizon", "Divulgación de errores conocidos a la defensa", "Separación entre quien reclama y quien acusa", "Acceso de los subpostmasters a los datos de investigación"]),
         ("Debió existir (análisis propio)", "navy", ["Función de marcar un faltante como discutido y congelarlo", "Registro de modificaciones remotas visible para el usuario", "Divulgación sistemática de errores conocidos", "Revisión independiente periódica con efecto sobre las decisiones"])],
        "Lo que enseña: los mecanismos que funcionaron actuaron años después; los que fallaron o no existían estaban antes. La cuarta columna es análisis propio.",
        CA + " " + BATES + " " + ANALISIS)


def controles() -> Fig:
    return pairs(
        "Cada eslabón de la cadena y el control que lo corta",
        "Ocho pares de causa y control propuesto: sin función de disputa, acceso remoto sin rastro visible, errores conocidos no divulgados, asistencia que trata faltantes como deudas, investigación pobre, la misma organización reclama y acusa, auditoría independiente tardía y dependencia de una única fuente.",
        [("Sin función de disputa", "Estado «en disputa» en cada discrepancia, con registro y congelación"), ("Modificación remota sin rastro visible", "Registro de acciones remotas visible para el usuario afectado"),
         ("Errores conocidos fuera de la vista de la defensa", "Divulgación obligatoria de errores conocidos relevantes en cada proceso"), ("Asistencia que trata el faltante como deuda", "Procedimiento de investigación antes de cualquier reclamación"),
         ("Investigación pobre", "Equipo independiente con acceso a los datos del proveedor"), ("Quien reclama es quien acusa", "Decisión de perseguir fuera de la organización que reclama"),
         ("Auditoría independiente tardía", "Revisión independiente periódica, con publicación de resultados"), ("Una única fuente de verdad", "Contraste de las cuentas con una segunda fuente, como el efectivo físico y los recibos")],
        "Lo que enseña: son controles de producto, de proceso y de gobierno; algunos están hoy en leyes y esquemas de reparación. La columna inferior es análisis propio, no un resumen de lo que se hizo.",
        ANALISIS)


def despues() -> Fig:
    return chain(
        "La arquitectura «después»: el sistema y su entorno cuando el sistema puede equivocarse",
        "Cadena objetivo: estado de disputa por discrepancia, registro de cambios remotos visible, errores conocidos publicados a los usuarios afectados, investigación independiente antes de reclamar, decisión de perseguir fuera del organismo reclamante y revisión periódica independiente.",
        [("Cada discrepancia tiene estado «en disputa» y un registro", "teal"), ("Acciones remotas sobre cuentas visibles para el usuario afectado", "teal"), ("Errores conocidos accesibles a los usuarios afectados y a la defensa", "teal"),
         ("Investigación independiente antes de reclamar", "teal"), ("Decisión de perseguir fuera de quien reclama", "teal"), ("Revisión independiente periódica con resultados públicos", "teal")],
        "Lo que enseña: son controles de diseño, de datos y de gobierno; ninguno exige una tecnología nueva. Diseño didáctico apoyado en lo que los tribunales y la investigación señalan; no describe lo que el Post Office haya implantado.",
        ANALISIS, per_row=3, note_kind="teal")


def impacto() -> Fig:
    return columns(
        "El impacto humano según el volumen 1 del informe final",
        "Tres columnas con lo que recoge el volumen 1 a partir de 17 relatos de primera mano: salud y bienestar, situación económica y consecuencias legales y reputacionales, incluido que algunas personas fallecieron antes de recibir una compensación.",
        [("Salud y vida personal", "gold", ["Algunas personas enfermaron gravemente", "Problemas de salud mental, incluida adicción al alcohol", "Algunas personas fallecieron antes de recibir compensación"]),
         ("Situación económica", "gold", ["Quiebra de algunas personas", "Responsabilidad por pequeñas sumas supuestamente perdidas", "Impacto financiero en las familias"]),
         ("Consecuencias legales y reputacionales", "gold", ["Algunas personas fueron encarceladas injustamente", "Daño reputacional en sus comunidades", "El presidente de la investigación califica el impacto de «desastroso»"])],
        "Lo que enseña: detrás de cada cifra hay una persona. Este caso recuerda el impacto con respeto y sin detalles personales: las fuentes recogen los relatos y este caso solo resume el informe.",
        INQ)


def reparacion() -> Fig:
    return columns(
        "Los esquemas de reparación que cita la investigación",
        "Tres columnas: el Horizon Shortfall Scheme para quienes perdieron dinero por faltantes, el esquema de la orden de litigio colectivo y el esquema de condenas anuladas, con el cierre del primero el 27 de noviembre de 2025 y la fusión del esquema de condenas.",
        [("Horizon Shortfall Scheme", "teal", ["Para quienes cubrieron faltantes", "Oferta de suma fija o evaluación individual", "No se admitieron reclamaciones tras la medianoche del 27 de noviembre de 2025"]),
         ("Esquema de la orden de litigio colectivo", "teal", ["Para quienes litigaron colectivamente", "La investigación recomienda ampliar derechos de alegación oral y el principio de mejor oferta"]),
         ("Condenas", "teal", ["Esquema de condenas anuladas", "En marzo de 2025 se anunció su fusión con el esquema de reparación de condenas de Horizon"])],
        "Lo que enseña: reparar es un proceso que también necesita diseño; el volumen 1 emite 19 recomendaciones sobre definición de reparación plena y justa, asesoramiento legal, plazos y organismo administrador. Los importes pagados no se citan aquí.",
        INQ)


def pila() -> Fig:
    return layers(
        "Qué se sabe de la pila técnica de Horizon",
        "Capas de la pila técnica de Horizon: terminales de mostrador; versión original llamada Legacy Horizon; Horizon Online, con las variantes HNG-X y HNG-A; registro de incidencias de Fujitsu; lenguaje, bases de datos y arquitectura interna no se publican en las fuentes consultadas.",
        [("Mostrador", "doc", "Terminales en unas 11 500 sucursales y seis millones de transacciones diarias según un comunicado del Post Office de 2015, citado en la sentencia"),
         ("Versiones", "doc", "Legacy Horizon (2000-2010) y Horizon Online (HNG-X desde 2010 y HNG-A después)"),
         ("Registros de errores", "doc", "PEAK por incidencia y KEL por error conocido, mantenidos por Fujitsu"),
         ("Origen", "doc", "Proyecto Pathway (1996-1999), de ICL con el Post Office y la Agencia de Prestaciones, que se retiró y dio paso a Horizon"),
         ("Lenguaje, base de datos, centro de datos, arquitectura de red", "unk", "No constan con detalle en las fuentes consultadas; este caso no los inventa")],
        "Lo que enseña: el nivel de detalle público alcanza para entender el problema, no para auditar el sistema. Verde: documentado; gris: no se sabe.",
        BATES + " Apartados 299 y 519.")


def negocio() -> Fig:
    return chain(
        "Esquema de la operación: del contrato a la cuenta de la sucursal",
        "Esquema de la operación: el Post Office contrata a subpostmasters para atender sucursales; Horizon registra las transacciones y las cuentas; el Post Office reclama los faltantes; los subpostmasters los cubren o son cesados; en una parte de los casos, el Post Office perseguía penalmente.",
        [("Contrato entre el Post Office y cada subpostmaster", "navy"), ("Atención de la sucursal y transacciones en Horizon", "plain"), ("Cuentas de la sucursal: Horizon como fuente de verdad", "teal"), ("Reclamación del faltante o cese; en algunos casos, procesamiento penal", "coral")],
        "Lo que enseña: la economía de la red depende de que las cuentas sean correctas; el coste de un sistema incorrecto lo soportaba quien tenía menos medios de comprobarlo. El volumen de pérdidas reclamadas en la High Court fue de unos 18 millones de libras.",
        CA + " Apartados 20 a 22.")


def consecuencias() -> Fig:
    return chain(
        "Consecuencias fechadas: de la sentencia civil a la reparación",
        "Cadena de consecuencias: sentencia de la High Court el 16 de diciembre de 2019; anulación de 39 condenas el 23 de abril de 2021; ley que anula condenas el 24 de mayo de 2024; volumen 1 del informe de la investigación pública el 8 de julio de 2025, con 19 recomendaciones.",
        [("16 dic 2019: la High Court examina el sistema (n.º 6)", "teal"), ("23 abr 2021: el Court of Appeal anula 39 condenas", "teal"), ("24 may 2024: ley que anula condenas en su ámbito", "navy"), ("8 jul 2025: volumen 1 del informe de la investigación, con 19 recomendaciones", "gold")],
        "Lo que enseña: cada etapa cierra una parte del daño y deja otra abierta; los demás volúmenes del informe de la investigación están pendientes. Mira que las etapas son de tribunales, Parlamento e investigación, no de la empresa.",
        BATES + " " + CA + " " + ACT + " " + INQ)


def que_aprender() -> Fig:
    return columns(
        "Qué aprender y qué no generalizar",
        "Dos columnas: lo que se transfiere, como dar a los usuarios una vía de disputa y un registro de cambios, divulgar errores conocidos y separar a quien reclama de quien acusa, y lo que no se generaliza, como culpar a una tecnología o dar por resuelto lo que la investigación aún no ha dicho.",
        [("Se transfiere", "teal", ["Un sistema que produce cuentas necesita un camino para disputarlas", "Los registros internos de errores conocidos deben llegar a quien puede verse afectado", "Cuando un lado puede modificar datos, el otro debe poder verlo", "Quien reclama no debe ser quien decide acusar"]),
         ("No se generaliza", "gold", ["No prueba que el software de contabilidad sea peligroso: prueba que sin controles de proceso es peligroso", "No es el fallo de una persona; es de varios sistemas e incentivos", "El informe final de la investigación está incompleto: faltan volúmenes", "Las cifras y fechas son de este caso y de la ley de Reino Unido"])],
        "Lo que enseña: el aprendizaje es de ingeniería de sistemas sociotécnicos, de gobierno y de ética. Mira la columna derecha: el caso se usa mal cuando se reduce a un villano o a un error de código.",
        ANALISIS)


FIGURES = {
    "post-office-horizon-contexto.svg": contexto,
    "post-office-horizon-fuentes.svg": fuentes,
    "post-office-horizon-dia-a-dia.svg": dia_a_dia,
    "post-office-horizon-sin-disputa.svg": sin_disputa,
    "post-office-horizon-registros-internos.svg": documentos,
    "post-office-horizon-errores-reconocidos.svg": bugs,
    "post-office-horizon-robustez.svg": robustez,
    "post-office-horizon-asimetria.svg": remoto,
    "post-office-horizon-condenas.svg": condenas,
    "post-office-horizon-escala-de-la-investigacion.svg": investigacion,
    "post-office-horizon-antecedentes.svg": antecedentes,
    "post-office-horizon-tres-decadas.svg": decadas,
    "post-office-horizon-hallazgos.svg": hallazgos,
    "post-office-horizon-puntos-unicos.svg": puntos_unicos,
    "post-office-horizon-defensa-en-profundidad.svg": defensa,
    "post-office-horizon-arbol-de-fallas.svg": arbol,
    "post-office-horizon-a-prueba-de-fallos.svg": prueba_de_fallos,
    "post-office-horizon-controles.svg": controles,
    "post-office-horizon-arquitectura-despues.svg": despues,
    "post-office-horizon-impacto-humano.svg": impacto,
    "post-office-horizon-reparacion.svg": reparacion,
    "post-office-horizon-hardware-y-software.svg": pila,
    "post-office-horizon-esquema-de-la-operacion.svg": negocio,
    "post-office-horizon-consecuencias.svg": consecuencias,
    "post-office-horizon-que-aprender.svg": que_aprender,
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
