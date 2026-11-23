"""Figures for the failure case study SolarWinds (supply chain compromise, 2019-2020).

Facts come from CISA (Emergency Directive 21-01, alert AA20-352A, joint statement), SolarWinds (security advisory
and blog) and Microsoft (technical analysis), as stated in each footer. Nothing judges persons.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_generic import barrier_slices, chain, columns, context, done, fault_tree, layers, pairs  # noqa: E402
from case_fig_helpers_fallo import equi_axis, sketch  # noqa: E402
from figure_kit import Fig, grouped_bars, timeline  # noqa: E402

ED = "Fuente: CISA, directiva de emergencia ED 21-01 (13 dic 2020)."
AA = "Fuente: CISA, alerta AA20-352A (actualizada 2021)."
SW = "Fuente: SolarWinds, aviso de seguridad y blog (ene 2021)."
MS = "Fuente: Microsoft, análisis técnico (dic 2020)."
ANALISIS = "Análisis propio, no conclusión de las fuentes."


def contexto() -> Fig:
    return context(
        "Una actualización de confianza entre un proveedor y miles de redes",
        "Diagrama de contexto: SolarWinds construye y firma el software de gestión de redes Orion; los clientes, entre ellos agencias federales y empresas privadas, instalan las actualizaciones firmadas; Orion monitoriza equipos de la red del cliente; un atacante insertó código en las compilaciones del proveedor.",
        [("SolarWinds: desarrolla, construye y firma Orion", "navy"), ("Atacante: actor de una nación estatal según el gobierno de EE. UU.", "coral")],
        ("Cadena de entrega de Orion", [("Entorno de compilación del proveedor", "coral"), ("Actualización firmada con el certificado legítimo", "gold"), ("Instalación en el cliente", "teal")]),
        [("Clientes: agencias federales, infraestructura crítica, empresas", "plain"), ("Equipos y redes monitorizados por Orion", "plain"), ("CISA, FBI y ODNI: respuesta coordinada", "navy")],
        "Lo que enseña: el cliente confiaba en la firma del proveedor; el atacante no tuvo que romper esa confianza, la usó. Mira la caja roja: el punto de entrada fue el entorno de compilación, no la red del cliente.",
        ED + " " + SW, left_labels=["construye", "inserta"], right_labels=["instalan", "monitoriza", "responden"])


def orion() -> Fig:
    return chain(
        "Qué hace Orion y por qué es un objetivo valioso",
        "Cadena de la función de Orion: monitoriza el tráfico y los equipos de la red de la organización; por eso corre con acceso amplio a la red; un compromiso de Orion da acceso a un sistema de gestión del tráfico; CISA lo describe como utilizado ampliamente para vigilar el tráfico de redes federales importantes.",
        [("Orion monitoriza equipos y tráfico de la red del cliente", "plain"), ("Para hacerlo, tiene acceso amplio a la red", "teal"), ("Un compromiso de Orion da acceso a un sistema de gestión del tráfico", "coral"), ("CISA: uso extendido para vigilar redes federales importantes", "gold")],
        "Lo que enseña: las herramientas de gestión y de seguridad son objetivos de alto valor porque ya tienen los permisos que un atacante querría. Mira la tercera caja: el acceso es consecuencia del propósito del producto.",
        ED + " Antecedentes.")


def cadena_entrega() -> Fig:
    return chain(
        "La cadena de entrega y dónde se insertó el código",
        "Cadena de entrega del software: el desarrollo del código, la compilación en un entorno del proveedor, la firma con el certificado legítimo, la distribución como actualización y la instalación en el cliente; el código malicioso se insertó en la compilación, por lo que la firma lo avaló.",
        [("Código fuente de Orion", "plain"), ("Compilación en el entorno del proveedor: aquí se insertó el código", "coral", True), ("Firma con el certificado legítimo de SolarWinds", "gold"), ("Distribución como actualización", "plain"), ("Instalación en el cliente: comprueba la firma y confía", "teal")],
        "Lo que enseña: la firma garantiza quién publicó el archivo, no que su contenido sea el pretendido. Mira la segunda caja: un atacante en la compilación puede producir artefactos que pasan todas las comprobaciones posteriores.",
        AA + " " + MS, per_row=3)


def ataque() -> Fig:
    return chain(
        "El ataque en siete pasos, de septiembre de 2019 a diciembre de 2020",
        "Cadena del ataque: primera actividad sospechosa en septiembre de 2019; prueba de inserción de código en octubre de 2019; inserción de SUNBURST desde el 20 de febrero de 2020; distribución a clientes en versiones firmadas; puerta trasera inactiva durante unos días; segunda fase con herramientas adicionales; descubrimiento y aviso en diciembre de 2020.",
        [("Sep 2019: primera actividad sospechosa en los sistemas de SolarWinds", "gold"), ("Oct 2019: una versión contiene modificaciones de prueba de inserción de código", "gold"), ("20 feb 2020: empieza la inserción de SUNBURST en las compilaciones", "coral"),
         ("La actualización firmada llega a los clientes", "coral"), ("La puerta trasera espera de 12 a 14 días antes de actuar", "coral"), ("Segunda fase: cargas adicionales y movimiento en la red del cliente", "coral"), ("12 dic 2020: SolarWinds es informado; 13 dic: directiva de emergencia", "teal")],
        "Lo que enseña: el atacante dedicó meses a probar antes de insertar y diseñó la puerta trasera para tardar en actuar. Mira que desde la inserción hasta el aviso pasaron unos diez meses.",
        SW + " " + MS, per_row=4)


def meses() -> Fig:
    return timeline(
        "Quince meses: de la primera actividad al aviso",
        "Línea de tiempo en meses desde septiembre de 2019: actividad sospechosa desde septiembre de 2019; prueba de inserción en octubre; inserción de SUNBURST desde el 20 de febrero de 2020; el atacante retira el código de los sistemas de SolarWinds en junio de 2020; CISA sabe de compromisos desde al menos marzo de 2020; el 12 de diciembre SolarWinds es informado.",
        [("Actividad en los sistemas de SolarWinds", [(0, 9, "sep 2019 a jun 2020", "coral")]),
         ("Código SUNBURST en las compilaciones", [(5.6, 9, "desde 20 feb", "navy")]),
         ("Compromisos en clientes (CISA)", [(6, 15.4, "desde marzo de 2020", "gold")])],
        unit="Meses desde septiembre de 2019", events=[(1, "oct 2019"), (5.6, "20 feb 2020"), (15.4, "12 dic 2020")], ticks=[0, 3, 6, 9, 12, 15, 16], t_max=16, label_w=230,
        note="La barra de actividad termina en junio de 2020, cuando los atacantes retiraron el código de los sistemas de SolarWinds; los compromisos en clientes siguieron hasta el aviso. La barra de SUNBURST se dibuja hasta junio por la misma razón. Las fechas son las que dan SolarWinds y CISA.",
        note_kind="gold", foot=SW + " " + AA)


def antecedentes() -> Fig:
    f, y = sketch("De la prueba de inserción a la directiva de emergencia, en ocho hitos",
                  "Eje no proporcional con ocho hitos: septiembre de 2019 primera actividad; octubre de 2019 prueba de inserción; 20 de febrero de 2020 inserción de SUNBURST; marzo de 2020 primeros compromisos en clientes según CISA; junio de 2020 el atacante retira el código; 12 de diciembre SolarWinds es informado; 13 de diciembre directiva de emergencia; 15 de abril de 2021 atribución.")
    ev = [("Sep 2019: primera actividad en SolarWinds", "gold"), ("Oct 2019: versión con pruebas de inserción", "gold"), ("20 feb 2020: inserción de SUNBURST", "coral"), ("Mar 2020: primeros compromisos en clientes (CISA)", "coral"),
          ("Jun 2020: el atacante retira el código", "gold"), ("12 dic 2020: SolarWinds es informado", "teal"), ("13 dic: directiva de emergencia 21-01", "teal"), ("15 abr 2021: el Gobierno de EE. UU. atribuye a la SVR rusa", "navy")]
    yy = equi_axis(f, y + 6, ev, box_w=170, box_h=100)
    return done(f, yy,
                "Lo que enseña: el atacante retiró su código de SolarWinds seis meses antes del aviso y siguió dentro de clientes. Mira que la atribución llegó cuatro meses después del aviso.",
                "gold", SW + " " + AA + " " + ED)


def versiones() -> Fig:
    return layers(
        "Qué versiones se vieron afectadas y qué se sabe de la compilación",
        "Capas de lo que consta: las versiones de Orion con SUNBURST según SolarWinds, el rango que CISA ordenó desconectar, la firma con el certificado legítimo y lo que no se sabe, como el lenguaje y la herramienta de compilación.",
        [("Versiones con SUNBURST (SolarWinds)", "doc", "Orion Platform 2019.4 HF 5, 2020.2 sin hotfix y 2020.2 HF 1"),
         ("Rango ordenado desconectar (CISA)", "doc", "Versiones 2019.4 a 2020.2.1 HF1 de Orion"),
         ("Archivo comprometido", "doc", "La biblioteca SolarWinds.Orion.Core.BusinessLayer.dll, firmada con el certificado legítimo"),
         ("Origen de la inserción", "doc", "Un código de inyección «novedoso» desplegado en el entorno de compilación para insertar SUNBURST sin que lo advirtieran los equipos de desarrollo"),
         ("Número de clientes afectados", "unk", "No se verificó una cifra en fuentes primarias de esta sesión; este caso no la da"),
         ("Lenguaje, herramienta de compilación, repositorios", "unk", "No constan con detalle en las fuentes consultadas")],
        "Lo que enseña: lo documentado es lo mínimo para actuar: qué versiones desconectar y qué archivo buscar. Verde: documentado; gris: no se sabe.",
        ED + " " + SW)


def confianza() -> Fig:
    return columns(
        "Qué verificaba el cliente y qué no podía verificar",
        "Dos columnas: lo que el cliente comprobaba, la firma digital del proveedor, la versión y su fuente, y lo que no podía comprobar, si el contenido correspondía al código fuente del proveedor, ni qué había pasado en la compilación.",
        [("Lo que el cliente comprobaba", "teal", ["La actualización venía firmada con el certificado legítimo de SolarWinds", "Procedía del canal oficial del proveedor", "Era una versión soportada y reciente", "Orion funcionaba como se esperaba"]),
         ("Lo que no podía comprobar", "coral", ["Que el binario correspondiera al código fuente revisado", "Qué había ocurrido en el entorno de compilación", "Que el comportamiento de la puerta trasera no apareciera en pruebas habituales", "Que el tráfico saliente imitara al legítimo"])],
        "Lo que enseña: todas las comprobaciones del cliente pasaban; el defecto estaba antes de la firma. Es lo que una compilación reproducible y una procedencia verificable intentan cubrir.",
        MS + " " + SW + " " + ANALISIS)


def latencia() -> Fig:
    return chain(
        "Por qué tardó en verse: tres decisiones de diseño del atacante",
        "Cadena de evasión: la puerta trasera espera de 12 a 14 días tras la instalación antes de actuar; el tráfico imita al legítimo y pasa por servidores en EE. UU.; el código de inyección se diseñó para no despertar sospechas de los equipos de compilación.",
        [("Espera de 12 a 14 días tras la instalación", "gold"), ("Tráfico que imita al legítimo, por servidores en EE. UU.", "gold"), ("Inyección diseñada para no alertar a los equipos de compilación", "gold"), ("Resultado: unos diez meses sin ser detectado como ataque", "coral")],
        "Lo que enseña: las defensas basadas en comportamiento y en tráfico se eluden si el atacante imita lo normal; por eso la prevención en la cadena de entrega pesa tanto. Los 12 a 14 días son los que describe Microsoft para una versión de la puerta trasera.",
        MS + " " + SW)


def directiva() -> Fig:
    return chain(
        "Qué ordenó CISA a las agencias federales el 13 de diciembre de 2020",
        "Cadena de acciones de la directiva: capturar memoria y analizar cuentas y tráfico en los equipos con Orion, desconectarlos, bloquear el tráfico hacia ellos, eliminar cuentas y persistencia del atacante, informar de los indicadores a CISA a las 12 horas del 14 de diciembre y tratar como comprometidos los equipos monitorizados por Orion.",
        [("Si hay capacidad: copiar memoria y analizar cuentas y tráfico", "plain"), ("Desconectar o apagar Orion 2019.4 a 2020.2.1 HF1", "teal", True), ("Bloquear el tráfico hacia y desde hosts con Orion", "teal"), ("Eliminar cuentas y mecanismos de persistencia del atacante", "teal"),
         ("Informar de los indicadores a CISA antes del mediodía del 14 de diciembre", "gold"), ("Tratar como comprometidos los hosts monitorizados y reconstruirlos", "navy")],
        "Lo que enseña: desconectar era la única medida conocida; CISA dice expresamente que no se debía reinstalar hasta recibir guía. Mira la última caja: el radio de impacto incluye todo lo que Orion monitorizaba.",
        ED, per_row=3)


def vectores() -> Fig:
    return columns(
        "No solo Orion: otras formas de entrada que CISA documentó",
        "Dos columnas: el compromiso de la cadena de suministro de Orion, y otros vectores iniciales que CISA identificó en enero de 2021, como el abuso de cuentas legítimas y de aserciones SAML, incluso en víctimas que no usaban Orion.",
        [("Cadena de suministro de Orion", "coral", ["Una versión maliciosa de una biblioteca de Orion, firmada con el certificado legítimo", "Una vez instalada, se comunica con el atacante", "Versiones y rangos documentados por SolarWinds y CISA"]),
         ("Otros vectores (CISA, 6 de enero de 2021)", "gold", ["Abuso de cuentas legítimas", "Abuso de aserciones SAML en algunos incidentes", "Víctimas que no usaban Orion o en las que no se observó explotación de Orion", "Volexity: uso de una clave robada para eludir MFA en correo web"])],
        "Lo que enseña: la cadena de suministro fue una vía importante, no la única. Un caso de estudio sobre Orion no agota la campaña. Mira que CISA añade las otras vías a medida que las encuentra.",
        AA)


def atribucion() -> Fig:
    return columns(
        "Qué consta sobre quién y qué es una inferencia",
        "Tres columnas: lo documentado (el gobierno de EE. UU. atribuye la actividad al Servicio de Inteligencia Exterior de Rusia, SVR, en abril de 2021), lo que dice SolarWinds (no verificó de forma independiente la atribución) y lo que este caso no sabe (la identidad de las personas y la lista completa de víctimas).",
        [("Documentado", "teal", ["15 de abril de 2021: el gobierno de EE. UU. atribuye la actividad a la SVR rusa", "Un grupo de coordinación de FBI, CISA y ODNI se formó en diciembre de 2020"]),
         ("Según SolarWinds", "gold", ["Dice que sus investigaciones no verificaron de forma independiente la atribución", "Habla de un actor estatal según el gobierno y expertos"]),
         ("No se sabe", "grey", ["La lista completa de víctimas", "Qué datos se obtuvieron en cada una", "Los detalles de inteligencia detrás de la atribución"])],
        "Lo que enseña: este caso se centra en el proceso de construcción y entrega; la atribución es relevante para la respuesta política, no para el diseño de controles.",
        AA + " " + SW)


def puntos_unicos() -> Fig:
    return context(
        "Dependencias de un único elemento en la cadena de entrega",
        "Mapa de dependencias: el entorno de compilación como único lugar donde se genera el binario, el certificado de firma como único aval, la confianza del cliente en el canal del proveedor y la ausencia de verificación independiente del contenido; cada una sin alternativa.",
        [("Un entorno de compilación comprometible", "coral"), ("Un certificado de firma como único aval", "coral"), ("Un canal de actualización de confianza", "gold")],
        ("Entrega de Orion", [("Binario único generado por el proveedor", "coral"), ("Sin comprobación independiente del contenido", "gold")]),
        [("Cliente: instala y confía", "plain"), ("Orion con acceso amplio a la red del cliente", "plain")],
        "Lo que enseña: la seguridad de miles de clientes dependía de la integridad de un solo entorno. Rojo: punto único de fallo con efecto directo; dorado: dependencia de confianza. Lectura propia.",
        SW + " " + ANALISIS, left_labels=["origen", "aval", "canal"], right_labels=["instala", "acceso"])


def defensa() -> Fig:
    return barrier_slices(
        "Defensa en profundidad: ocho barreras y por qué el código llegó a los clientes",
        "Láminas con huecos alineados: seguridad del entorno de compilación, detección de intrusión en el proveedor, revisión de cambios, compilación reproducible, firma, verificación del cliente, monitoreo del comportamiento y respuesta; una flecha atraviesa todos los huecos.",
        [("Seguridad del entorno de compilación (comprometido)", "coral"), ("Detección de intrusión en el proveedor (sin detectar)", "coral"), ("Revisión de cambios (el código no estaba en el repositorio)", "coral"), ("Compilación reproducible (no consta)", "coral"),
         ("Firma del proveedor (avaló el código malicioso)", "gold"), ("Verificación del cliente (pasó)", "gold"), ("Monitoreo del comportamiento (eludido)", "gold"), ("Respuesta (funcionó tras el aviso)", "teal")],
        "Lo que enseña: las barreras de firma y de verificación funcionaron como estaban diseñadas y no sirvieron porque el defecto estaba antes. Rojo: ausente o fallida; dorado: existía y no bastó; verde: funcionó. Es una metáfora.",
        SW + " " + MS + " " + ANALISIS)


def arbol() -> Fig:
    return fault_tree(
        "Árbol de fallas: qué tuvo que coincidir para que miles de clientes instalaran código malicioso",
        "Árbol de fallas con la instalación del código malicioso por los clientes arriba y dos ramas necesarias: que el atacante insertara código en las compilaciones, con tres condiciones, y que nadie lo detectara en el camino, con cuatro.",
        "Clientes instalan una actualización con código malicioso",
        ("A. El atacante inserta código en la compilación", "Y", ["Acceso a los sistemas del proveedor desde septiembre de 2019", "Acceso al entorno de compilación", "Un código de inyección que evita llamar la atención del equipo"]),
        ("B. Nadie lo detecta ni lo detiene antes", "Y", ["La intrusión no se detecta durante meses", "El código no está en el repositorio de fuentes", "La firma legítima lo avala", "Los clientes no pueden verificar el contenido"]),
        "Lo que enseña: cortar cualquier condición habría detenido o limitado el daño. Mira que A depende del proveedor y B de la verificación independiente. Estructura propia sobre lo documentado.",
        SW + " " + ANALISIS)


def prueba_de_fallos() -> Fig:
    return columns(
        "A prueba de fallos: qué existía, qué falló, qué no existía y qué debió existir",
        "Cuatro columnas: mecanismos que existían y funcionaron (la directiva de emergencia, la coordinación federal, el análisis forense), que existían y no bastaron (firma, verificación del cliente, monitoreo), que no existían o no constan (compilación reproducible, atestación de procedencia) y que debieron existir (análisis propio).",
        [("Existía y funcionó", "teal", ["SolarWinds es informado del ataque el 12 de diciembre de 2020 y actúa", "Directiva de emergencia en un día", "Coordinación entre FBI, CISA y ODNI", "Análisis forense con terceros"]),
         ("Existía y no bastó", "gold", ["Firma con el certificado legítimo", "Verificación del cliente", "Monitoreo del comportamiento", "Procesos de desarrollo habituales"]),
         ("No existía o no consta", "coral", ["Compilación reproducible y verificable", "Atestación de procedencia del artefacto", "Detección de cambios en el entorno de compilación", "Verificación independiente por el cliente"]),
         ("Debió existir (análisis propio)", "navy", ["Entorno de compilación aislado y vigilado", "Compilación reproducible y atestada", "Comparación del binario con las fuentes", "Segmentación de Orion en el cliente"])],
        "Lo que enseña: lo que funcionó fue la respuesta; lo que faltó estaba en la producción del artefacto. La cuarta columna es análisis propio y coincide con lo que SolarWinds dijo querer reforzar.",
        SW + " " + ED + " " + ANALISIS)


def controles() -> Fig:
    return pairs(
        "Cada eslabón de la cadena y el control que lo corta",
        "Ocho pares de causa y control propuesto: entorno de compilación comprometible, intrusión sin detectar, código fuera del repositorio, firma que avala lo que se compila, cliente que no puede verificar, Orion con acceso amplio, tráfico que imita al normal y respuesta tardía.",
        [("Entorno de compilación comprometible", "Compilación en entornos efímeros y aislados, con acceso mínimo"), ("Intrusión sin detectar durante meses", "Detección de anomalías en los sistemas de construcción y revisión de accesos"),
         ("Código inyectado fuera del repositorio", "Comparar el artefacto con el código fuente en una compilación independiente"), ("Firma que avala el binario", "Atestación de procedencia: qué se compiló, cómo y dónde"),
         ("Cliente que no puede verificar", "Verificación de la atestación y de la lista de materiales de software"), ("Orion con acceso amplio", "Mínimo privilegio y segmentación del servidor de monitoreo"),
         ("Tráfico que imita al legítimo", "Control de salida: solo destinos conocidos desde el servidor de monitoreo"), ("Aviso externo como primera señal", "Caza proactiva de amenazas y ejercicios de respuesta")],
        "Lo que enseña: los controles se reparten entre el proveedor y el cliente; ninguno exige tecnología nueva. La columna inferior es análisis propio.",
        ANALISIS)


def despues() -> Fig:
    return chain(
        "La arquitectura «después»: producir y verificar un artefacto sin confiar en una sola máquina",
        "Cadena objetivo: compilación aislada y efímera, compilación reproducible por una segunda cadena independiente, atestación de procedencia firmada, lista de materiales de software publicada, verificación en el cliente y segmentación de las herramientas de monitoreo.",
        [("Compilación en un entorno aislado y efímero", "teal"), ("Segunda compilación independiente y comparación de resultados", "teal"), ("Atestación firmada de procedencia", "teal"),
         ("Lista de materiales de software publicada", "teal"), ("El cliente verifica atestación y contenido antes de instalar", "teal"), ("Herramientas de monitoreo segmentadas y con salida controlada", "teal")],
        "Lo que enseña: el objetivo no es impedir toda intrusión, sino que una intrusión en un solo lugar no baste para producir un artefacto aceptado. Diseño didáctico; no describe lo que SolarWinds implantó.",
        ANALISIS, per_row=3, note_kind="teal")


def pila() -> Fig:
    return layers(
        "Qué se sabe de la pila técnica",
        "Capas de la pila técnica: plataforma Orion de monitoreo, biblioteca comprometida firmada, puerta trasera SUNBURST con espera y comunicación imitando tráfico legítimo, cargas de segunda fase; lenguajes y herramientas de compilación no se detallan.",
        [("Producto", "doc", "Orion Platform, software de gestión y monitoreo de redes de SolarWinds"),
         ("Componente comprometido", "doc", "SolarWinds.Orion.Core.BusinessLayer.dll, con una versión maliciosa firmada con el certificado legítimo"),
         ("Puerta trasera", "doc", "SUNBURST: espera de 12 a 14 días, comunicación que imita tráfico legítimo, entrega de cargas de segunda fase"),
         ("Segunda fase", "doc", "Herramientas como Cobalt Strike, según el análisis de Microsoft"),
         ("Entorno de compilación", "part", "Se halló un código de inyección que insertaba SUNBURST; la arquitectura de la compilación no se publica"),
         ("Lenguajes, repositorios y sistemas de integración continua", "unk", "No constan con detalle en las fuentes consultadas")],
        "Lo que enseña: lo documentado alcanza para detectar y limpiar, no para reconstruir el sistema. Verde: documentado; dorado: parcial; gris: no se sabe.",
        MS + " " + SW)


def negocio() -> Fig:
    return chain(
        "Esquema del negocio: de la licencia de software a la dependencia",
        "Esquema de negocio: SolarWinds vende software de gestión de TI a organizaciones de todos los tamaños; los clientes lo instalan con acceso amplio; el proveedor distribuye actualizaciones con confianza; el compromiso del proveedor se hereda.",
        [("SolarWinds vende software de gestión de TI", "navy"), ("Las organizaciones lo instalan con acceso amplio a su red", "plain"), ("El proveedor distribuye actualizaciones firmadas", "teal"), ("Un compromiso del proveedor se hereda en cada cliente", "coral")],
        "Lo que enseña: el valor comercial de una herramienta de gestión es su acceso, y el mismo acceso es su riesgo. Las fuentes verificadas en esta sesión no dan cifras de ingresos ni de clientes; este caso no las inventa.",
        ED + " " + SW)


def consecuencias() -> Fig:
    return chain(
        "Consecuencias fechadas: del aviso a la atribución y el cierre de la directiva",
        "Cadena de consecuencias: directiva de emergencia el 13 de diciembre de 2020; declaración conjunta del FBI, CISA y ODNI el 16 de diciembre; alerta de CISA con otros vectores de acceso en enero de 2021; atribución a la SVR rusa el 15 de abril de 2021; CISA cierra la directiva en 2026 por cumplida.",
        [("13 dic 2020: directiva de emergencia 21-01", "teal"), ("16 dic 2020: grupo de coordinación de FBI, CISA y ODNI", "navy"), ("6 ene 2021: CISA añade otros vectores de acceso", "gold"), ("15 abr 2021: atribución a la SVR; la directiva se cierra en 2026", "navy")],
        "Lo que enseña: la respuesta fue rápida y coordinada y, a la vez, larga: la directiva se cerró años después, cuando CISA consideró cumplidos sus propósitos. No se cuantifican costes porque las fuentes verificadas no los dan.",
        ED + " " + AA)


def que_aprender() -> Fig:
    return columns(
        "Qué aprender y qué no generalizar",
        "Dos columnas: lo que se transfiere, como proteger el entorno de compilación, exigir procedencia verificable y limitar el acceso de las herramientas de gestión, y lo que no se generaliza, como culpar al proveedor o suponer que el código abierto es más seguro.",
        [("Se transfiere", "teal", ["La firma garantiza el origen, no el contenido", "El entorno de compilación es un activo crítico", "Las herramientas de monitoreo son objetivos de alto valor", "Prepara la respuesta antes de necesitarla"]),
         ("No se generaliza", "gold", ["No prueba que el software comercial sea más inseguro que el libre", "No es el fallo de una persona ni solo del proveedor", "No describe todas las vías de la campaña", "La atribución es del gobierno de EE. UU.; este caso no la valida"])],
        "Lo que enseña: el aprendizaje es de integridad de la cadena de suministro. Mira la columna derecha: el caso se usa mal cuando se reduce a una empresa descuidada.",
        ANALISIS)


FIGURES = {
    "solarwinds-2020-contexto.svg": contexto,
    "solarwinds-2020-que-hace-orion.svg": orion,
    "solarwinds-2020-cadena-de-entrega.svg": cadena_entrega,
    "solarwinds-2020-ataque.svg": ataque,
    "solarwinds-2020-quince-meses.svg": meses,
    "solarwinds-2020-antecedentes.svg": antecedentes,
    "solarwinds-2020-versiones.svg": versiones,
    "solarwinds-2020-confianza.svg": confianza,
    "solarwinds-2020-evasion.svg": latencia,
    "solarwinds-2020-directiva.svg": directiva,
    "solarwinds-2020-otros-vectores.svg": vectores,
    "solarwinds-2020-atribucion.svg": atribucion,
    "solarwinds-2020-puntos-unicos.svg": puntos_unicos,
    "solarwinds-2020-defensa-en-profundidad.svg": defensa,
    "solarwinds-2020-arbol-de-fallas.svg": arbol,
    "solarwinds-2020-a-prueba-de-fallos.svg": prueba_de_fallos,
    "solarwinds-2020-controles.svg": controles,
    "solarwinds-2020-arquitectura-despues.svg": despues,
    "solarwinds-2020-hardware-y-software.svg": pila,
    "solarwinds-2020-esquema-del-negocio.svg": negocio,
    "solarwinds-2020-consecuencias.svg": consecuencias,
    "solarwinds-2020-que-aprender.svg": que_aprender,
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
