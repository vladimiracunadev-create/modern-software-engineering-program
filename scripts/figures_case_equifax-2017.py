"""Figures for the failure case study Equifax (data breach of 2017).

Numbers come from the majority staff report of the House Committee on Oversight and Government Reform
(December 2018) and the GAO report GAO-18-559 (August 2018), as stated in each footer. Nothing judges persons.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_generic import barrier_slices, chain, columns, context, done, fault_tree, layers, pairs  # noqa: E402
from case_fig_helpers_fallo import equi_axis, sketch  # noqa: E402
from figure_kit import Fig, grouped_bars, timeline  # noqa: E402

REP = "Fuente: informe del personal de la mayoría del Comité de Supervisión de la Cámara (dic 2018)."
GAO = "Fuente: GAO-18-559 (30 ago 2018)."
ANALISIS = "Análisis propio, no conclusión del Comité ni de la GAO."


def contexto() -> Fig:
    return context(
        "Un buró de crédito entre quienes aportan datos y quienes los compran",
        "Diagrama de contexto: las entidades que aportan datos de crédito los envían a Equifax; Equifax los analiza y vende informes y servicios de verificación de identidad a prestamistas, aseguradoras, empleadores y agencias federales; los consumidores no eligen estar en la base; dentro de Equifax, un portal de disputas conectaba a Internet con bases de datos de consumidores.",
        [("Entidades que aportan datos: prestamistas, aseguradoras, empleadores", "plain"), ("Consumidores: no eligen figurar ni pueden salirse", "plain")],
        ("Equifax", [("Bases de datos de información personal de consumidores", "gold"), ("Portal web de disputas de consumidores (ACIS)", "coral"), ("Servicios de informes y verificación de identidad", "teal")]),
        [("Compradores: prestamistas, aseguradoras, empleadores", "plain"), ("Agencias federales: verificación de identidad", "plain"), ("Reguladores y Congreso", "navy")],
        "Lo que enseña: el negocio consiste en concentrar datos de personas que no son clientes de la empresa. Mira que el portal de disputas, la caja roja, era el único componente expuesto a Internet entre los tres.",
        REP + " Apartados I y II.", left_labels=["aportan", "figuran"], right_labels=["compran", "verifican", "supervisan"])


def perfil() -> Fig:
    return columns(
        "Equifax en cifras de 2017 y 2018 según el informe del Comité",
        "Tres columnas: identidad de la empresa fundada en 1899 en Atlanta; escala de datos, con 820 millones de consumidores y más de 91 millones de empresas en sus bases; tamaño de plantilla y valor de mercado en octubre de 2018.",
        [("Empresa", "navy", ["Fundada en 1899 en Atlanta (Georgia)", "Cotiza desde 1965; símbolo EFX en la bolsa de Nueva York", "Parte del índice S&P 500"]),
         ("Datos", "teal", ["Información de unos 820 millones de consumidores", "Más de 91 millones de empresas", "Opera en 24 países"]),
         ("Tamaño", "gold", ["10 300 empleados en todo el mundo", "Valor de mercado de 11 720 millones de dólares el 26 de octubre de 2018", "Contrato de 7,25 millones del IRS para verificar identidad de contribuyentes"])],
        "Lo que enseña: es una empresa grande y cotizada con una base de datos de escala nacional; el tamaño de la plantilla y de los datos explica por qué la escala del incidente fue tan grande.",
        REP + " Apartado I.")


def modelo_cra() -> Fig:
    return chain(
        "Cómo funciona un buró de crédito: de los datos al informe",
        "Cadena del modelo de un buró de crédito: las entidades que otorgan crédito aportan datos; el buró los reúne y analiza; crea informes y puntuaciones; los vende a terceros; el consumidor no puede optar por salirse.",
        [("Entidades aportan datos de pagos, empleo, seguros y otros", "plain"), ("El buró los reúne y los analiza", "teal"), ("Genera informes y puntuaciones de crédito", "teal"), ("Vende a prestamistas, aseguradoras, empleadores y agencias", "gold")],
        "Lo que enseña: quien aporta los datos y quien los compra son clientes; el consumidor, dueño de los datos, no lo es. La seguridad de los datos protege a alguien que no paga ni elige.",
        REP + " Apartado I.A.")


def acis() -> Fig:
    return layers(
        "ACIS: el portal de disputas que fue la puerta de entrada",
        "Capas de lo que consta del portal: aplicación a medida desarrollada en los años setenta, expuesta a Internet, con una versión de Apache Struts vulnerable, un dispositivo de monitoreo de su tráfico inactivo por un certificado vencido y credenciales sin cifrar en un archivo.",
        [("Aplicación", "doc", "Portal de disputas de consumidores hecho a medida, con origen en los años setenta, expuesto a Internet"),
         ("Componente vulnerable", "doc", "Una versión de Apache Struts con la vulnerabilidad CVE-2017-5638, publicada con parche el 7 de marzo de 2017"),
         ("Monitoreo", "doc", "Un dispositivo que vigilaba el tráfico de ACIS llevaba 19 meses inactivo por un certificado de seguridad vencido"),
         ("Credenciales", "doc", "Un archivo con usuarios y contraseñas sin cifrar permitió llegar a bases de datos ajenas a ACIS"),
         ("Inventario del software", "part", "Los responsables dijeron no saber que Struts corría en ACIS ni cuánto se usaba en la empresa; los testimonios sobre un inventario completo se contradicen"),
         ("Lenguaje, servidores, red", "unk", "No constan con detalle en las fuentes consultadas; este caso no los inventa")],
        "Lo que enseña: cada capa tenía una debilidad documentada. Verde: documentado; dorado: parcial; gris: no se sabe.",
        REP + " Apartados II a V.")


def ataque() -> Fig:
    return chain(
        "El ataque en seis pasos, del 10 de marzo al 30 de julio de 2017",
        "Cadena del ataque: primeras señales de explotación el 10 de marzo; entrada el 13 de mayo por Struts en ACIS con puertas traseras web; credenciales sin cifrar que abren 48 bases de datos; 9 000 consultas y 265 hallazgos de datos personales sin cifrar; exfiltración sin que el monitoreo lo viera; detección el 29 de julio al renovar el certificado.",
        [("10 mar: primera evidencia de explotación de Struts en servidores conectados a la red", "gold"), ("13 may: entran por ACIS y colocan puertas traseras web", "coral"), ("Hallan credenciales sin cifrar; acceden a 48 bases de datos", "coral"),
         ("Unas 9 000 consultas; localizan datos personales sin cifrar 265 veces", "coral"), ("Sacan los datos sin que el monitoreo lo vea: certificado vencido", "coral", True), ("29 jul: se renueva el certificado y aparece tráfico sospechoso", "teal")],
        "Lo que enseña: el ataque duró 76 días y se detuvo cuando una renovación rutinaria devolvió la vista a un monitor que llevaba 19 meses apagado. Mira la quinta caja: la visibilidad faltó justo en el camino de salida.",
        REP + " Cronología y apartado III.", per_row=3)


def conteo() -> Fig:
    return grouped_bars(
        "Cuántas personas: de 143 a casi 148 millones",
        "Barras con el total acumulado de consumidores afectados: 143 millones en la lista del 4 de septiembre de 2017, unos 145,5 millones tras añadir 2,5 millones el 2 de octubre y casi 148 millones tras añadir otros 2,4 millones el 1 de marzo de 2018.",
        ["Lista del 4 de septiembre de 2017", "Tras el 2 de octubre de 2017 (+2,5)", "Tras el 1 de marzo de 2018 (+2,4)"],
        [("Millones de consumidores", [143, 145.5, 147.9], "coral")], unit="Millones de consumidores de EE. UU. (acumulado)", horizontal=True, label_w=270, ticks=[0, 40, 80, 120, 160], decimals=1,
        note="El informe del Comité da 143 millones, 2,5 millones más el 2 de octubre y 2,4 millones más el 1 de marzo de 2018, y un total de 148 millones; la GAO dice «al menos 145,5 millones». La suma 147,9 es aritmética propia y el dato de 145,5 coincide con la GAO. Los totales incluyen solo a personas de EE. UU. con los datos que cita el informe.",
        note_kind="gold", foot=REP + " " + GAO)


def consultas() -> Fig:
    return grouped_bars(
        "Lo que hicieron los atacantes dentro: consultas y hallazgos",
        "Barras en escala logarítmica con la actividad en las 48 bases de datos: unas 9 000 consultas y 265 veces que localizaron datos personales sin cifrar.",
        ["Consultas a las bases de datos", "Hallazgos de datos personales sin cifrar"],
        [("Cantidad", [9000, 265], "coral")], unit="Cantidad (escala logarítmica)", horizontal=True, log=True, label_w=270,
        note="Son las dos cifras que da el informe del Comité sobre la actividad de los atacantes en 48 bases de datos. La escala es logarítmica; no compares longitudes. No dice cuántos registros contenía cada hallazgo.",
        note_kind="gold", foot=REP)


def parche() -> Fig:
    return chain(
        "Del aviso del parche al servidor sin parchear, en cinco pasos",
        "Cadena del fallo de parcheo: el 7 de marzo sale el parche; el 8 US-CERT avisa a Equifax; el 9 el equipo de gestión de amenazas envía un correo a unas 430 personas pidiendo aplicar el parche crítico en 48 horas; el 15 un escaneo no detecta la vulnerabilidad; ACIS sigue sin parchear hasta finales de julio.",
        [("7 mar: sale el parche de Apache Struts", "plain"), ("8 mar: US-CERT avisa a Equifax", "plain"), ("9 mar: correo a unas 430 personas: parchear en 48 horas", "gold"), ("15 mar: un escaneo no detecta la vulnerabilidad en sistemas externos", "coral"), ("ACIS sin parchear hasta que se descubre el incidente, a finales de julio", "coral", True)],
        "Lo que enseña: la política existía, con plazo de 48 horas, y la alerta llegó; faltaron la certeza de quién era responsable y una detección que funcionara. Mira que el correo llegó a 430 personas y nadie tenía asignado explícitamente ese sistema.",
        REP + " Apartado V.B.", per_row=3)


def duenos() -> Fig:
    return columns(
        "Quién debía actuar: lo que decía la política y lo que ocurría",
        "Dos columnas: la política de parcheo asignaba roles de propietario del negocio, del sistema y de la aplicación, y marcaba un plazo de 48 horas para parches críticos; en la práctica, no había designación explícita de propietarios de la aplicación y la alerta llegó a unas 430 personas sin una acción concreta para la mayoría.",
        [("Lo que decía la política", "teal", ["Un parche crítico se aplica en 48 horas", "Hay roles: propietario del negocio, del sistema y de la aplicación", "Seguridad fija las reglas; IT las ejecuta", "La alerta de amenazas se distribuye por correo"]),
         ("Lo que ocurrió", "coral", ["Según un directivo, no había una designación explícita de propietarios de la aplicación ACIS", "La alerta llegó a unas 430 personas; muchas la recibieron solo como información", "La política dependía de que alguien conociera qué software corría en cada aplicación", "Equifax no sabía con certeza dónde usaba Struts"])],
        "Lo que enseña: una política sin dueños asignados es una intención. Los testimonios del informe se citan sin nombres: lo relevante es el rol, no la persona.",
        REP + " Apartado V.A y V.B.")


def monitoreo() -> Fig:
    return chain(
        "El monitor ciego: cómo un certificado vencido apagó la vigilancia durante 19 meses",
        "Cadena del monitoreo: un dispositivo inspeccionaba el tráfico de ACIS; su certificado de seguridad venció; el dispositivo dejó de inspeccionar durante 19 meses; los atacantes sacaron datos sin ser vistos; al renovar el certificado el 29 de julio de 2017 apareció tráfico sospechoso hacia una dirección en China y se bloqueó.",
        [("Un dispositivo inspecciona el tráfico de ACIS", "teal"), ("Su certificado de seguridad vence y nadie lo renueva", "coral", True), ("Durante 19 meses no inspecciona el tráfico", "coral"), ("La exfiltración pasa desapercibida", "coral"), ("29 jul 2017: se renueva y se ve tráfico sospechoso", "teal")],
        "Lo que enseña: un control de seguridad puede fallar en silencio. No había una alerta de que el monitor estaba ciego; quien lo detectó fue una renovación rutinaria. Mira que el sistema de vigilancia necesita su propia vigilancia.",
        REP + " Apartados III y V.B.2.", per_row=3)


def antecedentes() -> Fig:
    f, y = sketch("De la publicación del parche a las 148 millones de personas, en nueve hitos",
                  "Eje no proporcional con nueve hitos: 7 de marzo de 2017 sale el parche; 9 de marzo el correo interno; 13 de mayo la intrusión; 29 de julio se detecta; 2 de agosto se contrata a Mandiant; 7 de septiembre el aviso público; 2 de octubre 2,5 millones más; 1 de marzo de 2018 2,4 millones más; 25 de junio de 2018 la orden de consentimiento de ocho estados.")
    ev = [("7 mar 2017: sale el parche de Struts", "navy"), ("9 mar: correo interno, 48 horas", "gold"), ("13 may: intrusión por ACIS", "coral"), ("29 jul: se renueva el certificado y se detecta", "teal"), ("2 ago: Mandiant y asesores externos", "teal"),
          ("7 sep: aviso público", "gold"), ("2 oct: 2,5 millones más", "coral"), ("1 mar 2018: 2,4 millones más; total 148", "coral"), ("25 jun 2018: orden de consentimiento de ocho estados", "navy")]
    yy = equi_axis(f, y + 6, ev, box_w=170, box_h=100)
    return done(f, yy,
                "Lo que enseña: pasaron 67 días entre el parche y la entrada, y 76 de intrusión hasta la detección; después tardó 39 días en hacerse público. Mira que el aviso público fue 38 días después de que se supiera, el 31 de julio, que podían haberse filtrado datos personales.",
                "gold", REP)


def dias() -> Fig:
    return timeline(
        "184 días: del parche disponible al aviso público",
        "Línea de tiempo en días desde el 7 de marzo de 2017: el parche está disponible desde el día 0 hasta que se aplica a finales de julio; la primera explotación es el día 3; el atacante está dentro del 13 de mayo al 30 de julio, 76 días; el aviso público es el 7 de septiembre, el día 184.",
        [("Parche sin aplicar en ACIS", [(0, 144, "parche disponible pero sin aplicar a ACIS", "gold")]),
         ("Intrusión con acceso", [(67, 145, "76 días de acceso", "coral")]),
         ("Respuesta hasta el aviso", [(144, 184, "39 días", "navy")])],
        unit="Días desde el 7 de marzo de 2017", events=[(67, "13 may"), (144, "29 jul")], ticks=[0, 30, 60, 90, 120, 150, 180], t_max=190, label_w=210,
        note="Los días salen de las fechas del informe: 7 de marzo = día 0, 13 de mayo = 67, 29 y 30 de julio = 144 y 145, 7 de septiembre = 184. El certificado del monitor llevaba 19 meses vencido antes del día 144, fuera de esta escala.",
        note_kind="gold", foot=REP + " Cronología.")


def puntos_unicos() -> Fig:
    return context(
        "Dependencias de un único elemento en la defensa de los datos",
        "Mapa de dependencias: un portal expuesto con un componente vulnerable, un único monitor del tráfico, credenciales en un archivo, un correo como único aviso de parche y bases de datos sin cifrar; cada una sin alternativa independiente.",
        [("Un portal expuesto a Internet con un componente vulnerable", "coral"), ("Un solo monitor del tráfico, ciego por un certificado", "coral"), ("Credenciales sin cifrar en un archivo", "coral")],
        ("Defensa de los datos", [("Aviso de parche: un correo a una lista", "gold"), ("Bases de datos con datos personales sin cifrar", "coral")]),
        [("Atacantes: acceso a 48 bases de datos", "plain"), ("Datos de unos 148 millones de personas", "plain")],
        "Lo que enseña: cada defensa dependía de que otra funcionara. Rojo: un único punto de fallo con efecto directo; dorado: un proceso sin respaldo. Es una lectura propia de los hechos del informe.",
        REP + " " + ANALISIS, left_labels=["entrada", "visibilidad", "movimiento"], right_labels=["acceden", "extraen"])


def defensa() -> Fig:
    return barrier_slices(
        "Defensa en profundidad: ocho barreras y por qué no frenaron el ataque",
        "Láminas con huecos alineados: gestión de parches, escaneo de vulnerabilidades, inventario del software, segmentación de las bases de datos, protección de credenciales, cifrado de datos personales, monitoreo del tráfico y respuesta e investigación.",
        [("Parcheo en 48 horas (no se aplicó a ACIS)", "gold"), ("Escaneo de vulnerabilidades (no la detectó)", "gold"), ("Inventario del software (no se sabía dónde estaba Struts)", "coral"), ("Segmentación de bases de datos (48 accesibles)", "coral"),
         ("Credenciales protegidas (sin cifrar en un archivo)", "coral"), ("Cifrado de datos personales (hallados sin cifrar)", "coral"), ("Monitoreo del tráfico (ciego 19 meses)", "gold"), ("Respuesta e investigación (existió, tras la detección)", "teal")],
        "Lo que enseña: los huecos se alinean porque varias defensas dependían de una misma información, qué había en cada sistema, que no existía. Rojo: ausente; dorado: existía y falló; verde: funcionó. Es una metáfora.",
        REP + " Apartados III a V. " + ANALISIS)


def arbol() -> Fig:
    return fault_tree(
        "Árbol de fallas: qué tuvo que coincidir para exponer a 148 millones de personas",
        "Árbol de fallas con la exposición de datos arriba y dos ramas necesarias: que los atacantes entraran y se movieran, con cuatro condiciones, y que nadie los viera ni los frenara durante 76 días, con cuatro.",
        "Exposición de datos de unos 148 millones de personas",
        ("A. Los atacantes entran y se mueven", "Y", ["Portal expuesto con una versión vulnerable de Struts", "Parche crítico disponible y no aplicado", "Credenciales sin cifrar que abren otras bases", "Datos personales sin cifrar"]),
        ("B. Nadie los ve ni los frena durante 76 días", "Y", ["Monitor del tráfico inactivo por un certificado vencido", "Escaneo que no detecta la vulnerabilidad", "Sin inventario que diga dónde estaba el componente", "Acceso amplio a 48 bases de datos sin segmentar"]),
        "Lo que enseña: cortar cualquiera de las ocho condiciones habría reducido el daño. Mira que la rama B es de visibilidad y de segmentación: aunque la entrada fuera inevitable, la salida no tenía por qué serlo. Estructura propia sobre los hechos del informe.",
        REP + " " + ANALISIS)


def prueba_de_fallos() -> Fig:
    return columns(
        "A prueba de fallos: qué existía, qué falló, qué no existía y qué debió existir",
        "Cuatro columnas: mecanismos que existían y funcionaron (aviso de US-CERT, política de parcheo escrita, respuesta tras la detección), que existían y fallaron (distribución del aviso, escaneo, monitor de tráfico), que no existían (inventario, propietarios designados, segmentación, cifrado) y que debieron existir (análisis propio).",
        [("Existía y funcionó", "teal", ["Aviso de US-CERT y parche del proveedor disponibles el mismo día", "Política escrita con plazo de 48 horas", "Al renovar el certificado, se vio y se bloqueó el tráfico", "Investigación forense externa y aviso público"]),
         ("Existía y falló", "gold", ["Correo a unas 430 personas como mecanismo de aviso", "Escaneo del 15 de marzo", "Monitor de tráfico con certificado vencido", "Seguimiento del parche"]),
         ("No existía", "coral", ["Inventario fiable de software por aplicación", "Propietarios designados de la aplicación", "Segmentación de bases de datos", "Cifrado de los datos personales hallados"]),
         ("Debió existir (análisis propio)", "navy", ["Inventario de componentes con alertas por vulnerabilidad", "Dueños de cada sistema, con verificación del parche", "Alerta cuando un control de seguridad deja de funcionar", "Segmentación y cifrado de los datos personales"])],
        "Lo que enseña: lo que funcionó fue la respuesta posterior a la detección; lo que faltó estaba antes. La cuarta columna es análisis propio.",
        REP + " " + ANALISIS)


def controles() -> Fig:
    return pairs(
        "Cada eslabón de la cadena y el control que lo corta",
        "Ocho pares de causa y control propuesto: parche sin aplicar, aviso sin dueño, inventario ausente, escaneo que no detecta, monitor ciego, credenciales en un archivo, datos sin cifrar y acceso sin segmentar.",
        [("Parche crítico sin aplicar a ACIS", "Verificación automática del parche con plazo, y escalado si no se cumple"), ("Aviso por correo sin dueño", "Un dueño por sistema y confirmación explícita de aplicación"),
         ("No saber dónde corría Struts", "Inventario de componentes con alertas cuando aparece una vulnerabilidad"), ("Escaneo que no detectó la vulnerabilidad", "Escaneo autenticado y comparación con el inventario"),
         ("Monitor con certificado vencido", "Alerta cuando un sensor de seguridad deja de informar"), ("Credenciales sin cifrar en un archivo", "Gestor de secretos y rotación"),
         ("Datos personales sin cifrar", "Cifrado y tokenización de los campos sensibles"), ("48 bases accesibles desde ACIS", "Segmentación y mínimo privilegio por aplicación")],
        "Lo que enseña: son controles de proceso, de visibilidad y de datos; ninguno exige tecnología exótica. La columna inferior es análisis propio.",
        ANALISIS)


def despues() -> Fig:
    return chain(
        "La arquitectura «después»: cómo se reduce el daño de una entrada inevitable",
        "Cadena objetivo: inventario de componentes con alertas, dueños asignados y verificación de parches, sensores de seguridad vigilados, secretos fuera de archivos, segmentación de bases de datos y cifrado de campos sensibles.",
        [("Inventario de componentes con alertas por vulnerabilidad", "teal"), ("Dueño por sistema y verificación del parche con plazo", "teal"), ("Sensores de seguridad vigilados: alerta si dejan de informar", "teal"),
         ("Secretos en un gestor, no en archivos", "teal"), ("Segmentación: cada aplicación ve solo lo suyo", "teal"), ("Cifrado de campos sensibles", "teal")],
        "Lo que enseña: el diseño asume que alguna entrada ocurrirá y limita el alcance. Diseño didáctico apoyado en los hallazgos y las recomendaciones; no describe lo que Equifax implantó.",
        ANALISIS, per_row=3, note_kind="teal")


def remediacion() -> Fig:
    return columns(
        "Lo que se hizo después, según las fuentes",
        "Tres columnas: las 11 recomendaciones de remediación de Mandiant, que Equifax dijo haber implantado; la orden de consentimiento de junio de 2018 con ocho estados, que exige evaluación de riesgos del consejo y auditoría interna; y los cinco puntos débiles que Equifax identificó ante la GAO.",
        [("Mandiant", "teal", ["Once recomendaciones de remediación", "Equifax y sus directivos confirmaron que las implantó todas"]),
         ("Orden de consentimiento (25 de junio de 2018)", "navy", ["Ocho agencias estatales", "El consejo aprueba una evaluación de riesgos por escrito en 90 días", "Programa de auditoría interna formal en 30 días"]),
         ("Debilidades según Equifax ante la GAO", "gold", ["Actualizaciones de software", "Configuración de software", "Controles de acceso", "Monitoreo de red", "Protección de límites"])],
        "Lo que enseña: las cinco debilidades que Equifax identificó coinciden con los eslabones de la cadena; la GAO, por su parte, habla de cuatro factores: identificación, detección, segmentación y gobierno de datos.",
        REP + " " + GAO)


def organizacion() -> Fig:
    return columns(
        "Cómo se repartían Seguridad e IT: reglas por un lado, ejecución por otro",
        "Dos columnas: la organización de Seguridad, que establecía reglas, escaneaba riesgos y distribuía alertas, y la de IT, responsable de ejecutar las reglas y parchear; el informe del Comité señala que la estructura carecía de rendición de cuentas y coordinación.",
        [("Seguridad", "teal", ["Establece políticas y reglas", "Distribuye alertas de amenazas", "Escanea para buscar riesgos y brechas"]),
         ("IT", "gold", ["Ejecuta las reglas y aplica los parches", "Responde de que su personal cumpla", "Gestiona el entorno heredado con sistemas como ACIS"]),
         ("Lo que señala el informe", "coral", ["La estructura carecía de rendición de cuentas y de coordinación", "Había brechas entre desarrollar la política y ejecutarla", "El informe lo expone como causa de fondo, no como falta de una persona"])],
        "Lo que enseña: dividir quién define y quién ejecuta exige un cierre explícito del bucle: alguien debe poder decir que el parche se aplicó. Mira la tercera columna: es un hallazgo de estructura.",
        REP + " Apartado V.A.")


def pila() -> Fig:
    return layers(
        "Qué se sabe de la pila técnica",
        "Capas de la pila técnica: aplicación ACIS heredada, Apache Struts, servidores web con puertas traseras, bases de datos con datos personales, dispositivo de monitoreo; lenguaje, sistema operativo y arquitectura de red no se publican en las fuentes consultadas.",
        [("Aplicación", "doc", "ACIS, portal a medida con origen en los años setenta"),
         ("Marco web", "doc", "Apache Struts, un marco de código abierto, con la vulnerabilidad CVE-2017-5638"),
         ("Acceso del atacante", "doc", "Puertas traseras web («web shells») para controlar remotamente el sistema"),
         ("Datos", "doc", "48 bases de datos con tablas de distintos esquemas y datos personales sin cifrar"),
         ("Monitoreo", "doc", "Dispositivo que inspeccionaba el tráfico de ACIS, inactivo por un certificado vencido"),
         ("Lenguaje, sistema operativo, red, centros de datos", "unk", "No constan con detalle en las fuentes consultadas; este caso no los inventa")],
        "Lo que enseña: el nivel de detalle público basta para entender el fallo, no para reconstruir el sistema. Verde: documentado; gris: no se sabe.",
        REP + " Apartados II a V.")


def negocio() -> Fig:
    return chain(
        "Esquema del negocio: del dato personal al ingreso",
        "Esquema de negocio: Equifax recibe datos de entidades que otorgan crédito, los analiza y vende informes, puntuaciones y verificación de identidad a prestamistas, aseguradoras, empleadores y agencias federales; el consumidor no paga ni elige.",
        [("Datos de pagos y otros aportados por entidades", "plain"), ("Análisis y puntuaciones", "teal"), ("Venta de informes y verificación de identidad", "gold"), ("Ingreso para Equifax; el riesgo de la fuga lo asume el consumidor", "coral")],
        "Lo que enseña: el activo principal de la empresa es el dato, y su protección es parte del producto. El informe del Comité señala que la expansión y las adquisiciones aumentaron la complejidad de la infraestructura.",
        REP + " Apartados I y V.C.")


def consecuencias() -> Fig:
    return chain(
        "Consecuencias fechadas: del aviso público a la orden de consentimiento",
        "Cadena de consecuencias: aviso público el 7 de septiembre de 2017; 2,5 millones más el 2 de octubre; 2,4 millones más el 1 de marzo de 2018 con un total de 148 millones; orden de consentimiento de ocho estados el 25 de junio de 2018; informe de la GAO el 30 de agosto de 2018; informe del Comité en diciembre de 2018.",
        [("7 sep 2017: aviso público de 143 millones", "coral"), ("2 oct 2017 y 1 mar 2018: se amplía hasta 148 millones", "coral"), ("25 jun 2018: orden de consentimiento de ocho estados", "navy"), ("30 ago 2018: informe de la GAO; dic 2018: informe del Comité", "teal")],
        "Lo que enseña: el aviso inicial fue incompleto y se amplió dos veces. Mira que la respuesta regulatoria y legislativa tardó entre nueve y quince meses en llegar. Las sanciones económicas posteriores no se verificaron en esta sesión.",
        REP + " " + GAO)


def que_aprender() -> Fig:
    return columns(
        "Qué aprender y qué no generalizar",
        "Dos columnas: lo que se transfiere, como saber qué software corre en cada sistema, asignar dueños, vigilar a los sensores de seguridad y limitar el alcance de una entrada; y lo que no se generaliza, como culpar a una persona o a una tecnología.",
        [("Se transfiere", "teal", ["No puedes parchear lo que no sabes que tienes", "Una política sin dueños es una intención", "Los sensores de seguridad necesitan vigilancia propia", "Asume que alguna entrada ocurrirá: segmenta y cifra"]),
         ("No se generaliza", "gold", ["No prueba que el código abierto sea inseguro: el parche existía el mismo día", "No es el fallo de una persona: el informe describe una estructura", "Las cifras son de EE. UU. y de 2017", "No dice cuánto costó el incidente a Equifax"])],
        "Lo que enseña: el aprendizaje es de gestión de activos, de dueños y de visibilidad. Mira la columna derecha: el caso se usa mal cuando se reduce a un correo sin reenviar.",
        ANALISIS)


FIGURES = {
    "equifax-2017-contexto.svg": contexto,
    "equifax-2017-perfil.svg": perfil,
    "equifax-2017-modelo-de-un-buro.svg": modelo_cra,
    "equifax-2017-acis.svg": acis,
    "equifax-2017-ataque.svg": ataque,
    "equifax-2017-victimas.svg": conteo,
    "equifax-2017-actividad-de-los-atacantes.svg": consultas,
    "equifax-2017-del-aviso-al-parche.svg": parche,
    "equifax-2017-duenos.svg": duenos,
    "equifax-2017-monitor-ciego.svg": monitoreo,
    "equifax-2017-antecedentes.svg": antecedentes,
    "equifax-2017-184-dias.svg": dias,
    "equifax-2017-puntos-unicos.svg": puntos_unicos,
    "equifax-2017-defensa-en-profundidad.svg": defensa,
    "equifax-2017-arbol-de-fallas.svg": arbol,
    "equifax-2017-a-prueba-de-fallos.svg": prueba_de_fallos,
    "equifax-2017-controles.svg": controles,
    "equifax-2017-arquitectura-despues.svg": despues,
    "equifax-2017-remediacion.svg": remediacion,
    "equifax-2017-organizacion.svg": organizacion,
    "equifax-2017-hardware-y-software.svg": pila,
    "equifax-2017-esquema-del-negocio.svg": negocio,
    "equifax-2017-consecuencias.svg": consecuencias,
    "equifax-2017-que-aprender.svg": que_aprender,
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
