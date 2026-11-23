"""Figures for the failure case study Cloudflare, WAF regular expression outage of 2 July 2019.

Every number comes from the official post mortem "Details of the Cloudflare outage on July 2, 2019" (Cloudflare blog),
unless the footer says it is own analysis. Output goes to ``casos/figures/``.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from case_fig_generic import barrier_slices, chain, columns, context, done, fault_tree, layers, pairs  # noqa: E402
from case_fig_helpers_fallo import equi_axis, sketch  # noqa: E402
from figure_kit import Fig, grouped_bars, line_chart, timeline  # noqa: E402

CF = "Fuente: Cloudflare, post mortem oficial del 2 de julio de 2019."
ANALISIS = "Análisis propio, no conclusión de Cloudflare."


def contexto() -> Fig:
    return context(
        "Cloudflare entre sus clientes y los visitantes de sus sitios",
        "Diagrama de contexto: los visitantes de los sitios de los clientes llegan a la red de Cloudflare; cada punto de presencia ejecuta el proxy, la red de entrega de contenido y el cortafuegos de aplicaciones web; las reglas del cortafuegos se distribuyen desde el centro a más de 180 ciudades mediante un almacén de claves y valores propio.",
        [("Visitantes de los sitios de los clientes", "plain"), ("Clientes de Cloudflare y sus propios clientes", "plain")],
        ("Red de Cloudflare", [("Puntos de presencia en más de 180 ciudades", "teal"), ("Proxy, CDN y cortafuegos de aplicaciones web (WAF)", "coral"), ("Quicksilver: almacén de claves y valores que distribuye configuración y reglas", "gold")]),
        [("Servidores de origen de los clientes", "plain"), ("Panel de control y API de Cloudflare, que también pasan por su borde", "plain"), ("Equipos de Cloudflare: reglas, SRE, herramientas internas", "navy")],
        "Lo que enseña: el WAF estaba en el camino de todo el tráfico HTTP y HTTPS; una regla defectuosa afecta a todos los clientes a la vez. Mira que el panel de control y los equipos internos también dependían de ese camino.",
        CF, left_labels=["visitan", "usan"], right_labels=["origen", "gestionan", "operan"])


def perfil() -> Fig:
    return columns(
        "Datos de la red y del equipo de reglas que cita el post mortem",
        "Tres columnas: la red, con más de 180 ciudades y un almacén que distribuye unos 350 cambios por segundo con un p99 de 2,29 segundos; el equipo de reglas del WAF, con 476 solicitudes de cambio en 60 días, una cada tres horas; y las reglas, 3 868 en total.",
        [("Red y distribución", "teal", ["Más de 180 ciudades", "Quicksilver distribuye unos 350 cambios por segundo", "p99 de 2,29 s para que un cambio llegue a todas las máquinas"]),
         ("Equipo de reglas del WAF", "gold", ["476 solicitudes de cambio en los últimos 60 días", "Una cada tres horas de media", "Decenas de reglas nuevas cada semana"]),
         ("Reglas gestionadas", "navy", ["3 868 reglas en WAF Managed Rules", "Todas se revisaron tras el incidente", "Cada regla es una expresión regular"])],
        "Lo que enseña: la velocidad es una característica deliberada del producto: responder a nuevas vulnerabilidades en segundos. Mira que lo que hace útil al sistema es lo mismo que hace instantáneo un error.",
        CF)


def flujo_waf() -> Fig:
    return chain(
        "El camino de una regla del WAF, del código a todos los servidores del mundo",
        "Cadena del despliegue de una regla del WAF: un ingeniero la escribe; la solicitud de cambio se aprueba y se fusiona; el sistema de integración compila y ejecuta las pruebas; el despliegue automático la envía a Quicksilver; en segundos llega a las máquinas de más de 180 ciudades.",
        [("Un ingeniero escribe o cambia la regla", "plain"), ("Pull request aprobada y fusionada (13:31)", "teal"), ("TeamCity compila y las pruebas pasan (13:37)", "teal"), ("Despliegue automático (13:42)", "gold", True), ("Quicksilver la distribuye en segundos a todo el mundo", "coral"), ("Cada servidor ejecuta la regla sobre el tráfico real", "coral")],
        "Lo que enseña: todos los pasos funcionaron como se diseñaron; el defecto se coló porque ningún paso medía el consumo de CPU de la regla. Mira que el despliegue es automático y global por diseño.",
        CF, per_row=3)


def dos_caminos() -> Fig:
    return columns(
        "Dos caminos de despliegue: el software normal y las reglas del WAF",
        "Dos columnas: el software de Cloudflare pasa por un punto de presencia interno, otro con una pequeña parte del tráfico de clientes gratuitos, tres puntos canarios y por último el mundo; las reglas del WAF, por un procedimiento operativo que permite el despliegue global inmediato.",
        [("Software normal", "teal", ["DOG: punto de presencia solo de empleados", "PIG: una pequeña parte del tráfico de clientes sin pago", "Canarios: tres puntos con tráfico de clientes con y sin pago", "Mundo: tras horas o días de pruebas"]),
         ("Reglas del WAF", "coral", ["Cambio aprobado, fusionado y probado por CI", "Despliegue global en segundos por Quicksilver", "Por diseño: hay que responder rápido a amenazas nuevas", "El procedimiento operativo lo permite incluso para un cambio no urgente"])],
        "Lo que enseña: la excepción por velocidad se aplicó también a un cambio que no era urgente: se desplegó en modo de simulación, sin bloquear nada, pero la regla se ejecutaba igualmente. Esto es lo que el post mortem señala.",
        CF)


def regex_pasos() -> Fig:
    return line_chart(
        "Cómo crecen los pasos de la expresión regular con el tamaño de la entrada",
        "Líneas en escala logarítmica con los pasos del motor para emparejar la cadena x= seguida de varias x: con el patrón de ejemplo sin punto y coma, de 23 pasos con una x a 555 con veinte; con el punto y coma final, de 90 a 5 353.",
        [("Patrón .*.*=.*", [(1, 23), (2, 33), (3, 45), (20, 555)], "navy"), ("Patrón .*.*=.*; (con punto y coma)", [(1, 90), (20, 5353)], "coral")],
        x_label="Número de x después del signo igual", y_label="Pasos del motor (escala logarítmica)", log_y=True, x_ticks=[(1, "1"), (2, "2"), (3, "3"), (10, "10"), (20, "20")], y_ticks=[10, 100, 1000, 10000],
        note="Son los ejemplos del apéndice del post mortem, de una versión simplificada de la expresión real, que tenía tres bloques de «cualquier cosa». El crecimiento no es lineal: con 20 x el motor necesita 555 pasos, y con el punto y coma final, 5 353. La expresión real nunca se midió así: es una ilustración del mecanismo.",
        note_kind="gold", foot=CF + " Apéndice.")


def retroceso() -> Fig:
    return chain(
        "Por qué una expresión regular puede agotar una CPU",
        "Cadena del retroceso catastrófico: el patrón pide emparejar cualquier cosa seguida de cualquier cosa; el motor prueba una división, falla y retrocede; cada fallo abre más combinaciones; el número de pasos crece más que el tamaño de la entrada; con muchas peticiones la CPU se agota.",
        [("Patrón: cualquier cosa, cualquier cosa, un igual y cualquier cosa", "plain"), ("El motor prueba una división y falla al buscar el igual", "gold"), ("Retrocede y prueba otra división", "gold"), ("Los pasos crecen más rápido que la entrada", "coral", True), ("Con tráfico real, todas las CPU de HTTP quedan al 100 %", "coral")],
        "Lo que enseña: el coste de una expresión regular puede depender de la entrada, no del tamaño del patrón. La solución que el post mortem cita es de 1968: un algoritmo de tiempo lineal de Thompson, que motores como re2 y Rust implementan.",
        CF + " Apéndice.", per_row=3)


def minutos() -> Fig:
    return timeline(
        "El 2 de julio de 2019 en minutos: del despliegue a la recuperación",
        "Línea de tiempo en minutos desde las 13:30 UTC: fusión del cambio a las 13:31; pruebas en verde a las 13:37; despliegue a las 13:42; primer aviso a las 13:45; WAF identificado a las 14:00; propuesta de terminación global a las 14:02; ejecutada a las 14:07; tráfico normal a las 14:09; WAF reactivado a las 14:52.",
        [("Cambio hasta el despliegue", [(1, 12, "cambio", "teal")]),
         ("Impacto en el tráfico", [(12, 39, "27 min", "coral")]),
         ("Diagnóstico", [(15, 30, "avisos", "gold")]),
         ("Mitigación", [(32, 39, "corte", "navy")]),
         ("WAF desactivado", [(37, 82, "14:07 a 14:52", "grey")])],
        unit="Minutos desde las 13:30 UTC", events=[(12, "13:42"), (30, "14:00"), (39, "14:09")], ticks=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90], t_max=90, label_w=200,
        note="Todas las horas son del post mortem, en UTC. El impacto empieza con el despliegue y termina cuando el tráfico vuelve a niveles normales tras la terminación global. La restauración del WAF tardó 43 minutos más, con pruebas negativas y positivas en una sola ciudad.",
        note_kind="gold", foot=CF)


def secuencia() -> Fig:
    return chain(
        "La secuencia del diagnóstico, en seis pasos",
        "Cadena del diagnóstico: llegan avisos sintéticos del WAF y pérdida de tráfico; SRE declara un incidente de máxima prioridad; se descarta un ataque; a las 14:00 se identifica el WAF; se propone una terminación global; se ejecuta a las 14:07.",
        [("13:45: primer aviso del WAF; luego, caída global de tráfico y errores 502", "gold"), ("SRE declara P0 y convoca a todos los equipos", "teal"), ("Se especula con un ataque nuevo, y se descarta", "plain"), ("14:00: se identifica el WAF como causa", "teal"),
         ("14:02: se propone la terminación global del WAF", "gold"), ("14:07: se ejecuta; 14:09, tráfico normal", "teal", True)],
        "Lo que enseña: el diagnóstico tardó 15 minutos desde el primer aviso hasta saber qué componente era, y otros cinco hasta ejecutar el interruptor. Mira que existía un mecanismo de terminación global de un componente, y funcionó.",
        CF, per_row=3)


def acceso() -> Fig:
    return chain(
        "Cuando la herramienta para arreglarlo depende de lo que está roto",
        "Cadena de dependencias de la respuesta: el servicio de acceso de Cloudflare estaba caído y no se podía entrar al panel de control interno; algunas credenciales de SRE habían caducado por seguridad; Jira y el sistema de compilación solo se alcanzaban con un procedimiento de excepción poco practicado; los clientes tampoco accedían al panel ni a la API.",
        [("Cloudflare usa sus propios productos para acceder a sus sistemas", "plain"), ("Con el servicio de acceso caído no se entra al panel interno", "coral"), ("Algunas credenciales caducan por seguridad si no se usan", "coral"), ("Jira y el sistema de compilación: solo por un procedimiento poco practicado", "gold"),
         ("Los clientes tampoco acceden al panel ni a la API", "coral")],
        "Lo que enseña: una dependencia circular entre producción y herramientas de recuperación alarga el incidente. Mira que el post mortem lo cuenta como algo a ensayar, no como una excepción.",
        CF, per_row=3)


def causas() -> Fig:
    return layers(
        "Once vulnerabilidades que convergieron, según el propio post mortem",
        "Capas con las once condiciones que Cloudflare enumera: una expresión regular que retrocede, una protección eliminada por error en una refactorización, un motor sin garantías de complejidad, pruebas que no miden CPU, un procedimiento que permitía el despliegue global, un plan de reversión lento, una primera alerta tardía, una página de estado lenta, acceso difícil a los sistemas, credenciales caducadas y clientes sin acceso al panel.",
        [("Expresión regular", "doc", "Escrita de modo que podía retroceder enormemente"),
         ("Protección eliminada", "doc", "Una protección contra el consumo excesivo de CPU se quitó por error en una refactorización del WAF semanas antes, para reducir su uso de CPU"),
         ("Motor sin garantías", "doc", "El motor de expresiones regulares no tenía garantías de complejidad"),
         ("Pruebas", "doc", "La batería de pruebas no tenía forma de detectar un consumo excesivo de CPU"),
         ("Procedimiento", "doc", "Un cambio de reglas no urgente podía ir a producción global sin despliegue escalonado"),
         ("Reversión", "doc", "El plan exigía ejecutar dos veces la compilación completa del WAF, demasiado lento"),
         ("Avisos y estado", "doc", "La primera alerta de caída global tardó; la página de estado se actualizó tarde"),
         ("Acceso", "doc", "Dificultad para acceder a sistemas propios, credenciales caducadas y clientes sin acceso al panel ni a la API")],
        "Lo que enseña: el propio post mortem rechaza una causa única y dice que fue una convergencia improbable de varios factores. Verde: documentado por Cloudflare.",
        CF)


def puntos_unicos() -> Fig:
    return context(
        "Dependencias de un único elemento en la ruta de una regla",
        "Mapa de dependencias: el WAF como único componente que inspecciona todo el tráfico HTTP, un único canal de distribución global instantáneo, un único motor de expresiones regulares sin garantías y una única herramienta de acceso, cada uno sin alternativa independiente.",
        [("Un único WAF en el camino de todo el tráfico", "coral"), ("Un único canal global de distribución, en segundos", "coral"), ("Un motor de expresiones regulares sin garantías", "coral")],
        ("Camino de una regla", [("Regla fusionada y probada", "teal"), ("Quicksilver", "gold")]),
        [("Todas las CPU de HTTP en el mundo", "plain"), ("Panel de control y API de los clientes", "plain")],
        "Lo que enseña: la velocidad y la universalidad que dan valor al producto son también el radio de impacto. Rojo: punto único con efecto directo. Es una lectura propia.",
        CF + " " + ANALISIS, left_labels=["inspecciona", "distribuye", "ejecuta"], right_labels=["agota", "bloquea"])


def defensa() -> Fig:
    return barrier_slices(
        "Defensa en profundidad: ocho barreras y por qué una regla llegó a todo el mundo",
        "Láminas con huecos alineados: la revisión de la expresión regular, la protección contra consumo de CPU, las garantías del motor, las pruebas, el despliegue escalonado, la alerta, el interruptor global y la comunicación; una flecha las atraviesa.",
        [("Revisión de la regla (aprobada)", "gold"), ("Protección contra exceso de CPU (eliminada por error)", "coral"), ("Garantías del motor de regex (no existían)", "coral"), ("Pruebas (no medían CPU)", "coral"),
         ("Despliegue escalonado (el procedimiento lo excluía)", "coral"), ("Alerta de caída (tardó)", "gold"), ("Terminación global del WAF (funcionó)", "teal"), ("Página de estado (tardó)", "gold")],
        "Lo que enseña: los controles de proceso se cumplieron, pero faltaban los de comportamiento. Rojo: ausente o eliminada; dorado: existía y fue parcial; verde: funcionó. Es una metáfora.",
        CF + " " + ANALISIS)


def arbol() -> Fig:
    return fault_tree(
        "Árbol de fallas: qué tuvo que coincidir para dejar sin servicio a la red",
        "Árbol de fallas con el agotamiento de CPU global arriba y dos ramas necesarias: que una regla costosa llegara a producción, con cuatro condiciones, y que llegara a todas partes y tardara en revertirse, con cuatro.",
        "Agotamiento de CPU en todos los servidores HTTP del mundo",
        ("A. Una regla de coste explosivo llega a producción", "Y", ["Expresión regular con retroceso catastrófico", "Protección contra exceso de CPU eliminada", "Motor sin garantías de complejidad", "Pruebas que no miden el consumo de CPU"]),
        ("B. Llega a todo el mundo y tarda en revertirse", "Y", ["Procedimiento que permite el despliegue global", "Distribución global en segundos por Quicksilver", "Reversión lenta: dos compilaciones completas", "Herramientas de acceso dependientes del servicio caído"]),
        "Lo que enseña: cortar cualquiera de las ocho condiciones habría evitado o limitado el incidente. Mira que A es sobre el defecto y B sobre el radio de impacto y la recuperación. Estructura propia sobre las condiciones que enumera el post mortem.",
        CF + " " + ANALISIS)


def prueba_de_fallos() -> Fig:
    return columns(
        "A prueba de fallos: qué existía, qué falló, qué no existía y qué debió existir",
        "Cuatro columnas: mecanismos que existían y funcionaron (revisión, integración continua, avisos sintéticos, terminación global), que existían y fallaron (protección de CPU, avisos de tráfico, página de estado), que no existían (garantías del motor, pruebas de CPU, despliegue escalonado para reglas) y que debieron existir (análisis propio).",
        [("Existía y funcionó", "teal", ["Revisión y aprobación del cambio", "CI con pruebas funcionales", "Avisos sintéticos del WAF a los tres minutos", "Terminación global de un componente"]),
         ("Existía y falló", "gold", ["Protección contra consumo excesivo de CPU (eliminada)", "Alerta de caída global de tráfico", "Actualización de la página de estado", "Acceso a herramientas internas"]),
         ("No existía", "coral", ["Garantías de complejidad del motor", "Pruebas de consumo de CPU de cada regla", "Despliegue escalonado para reglas no urgentes", "Capacidad de sacar el panel y la API del borde"]),
         ("Debió existir (análisis propio)", "navy", ["Presupuesto de CPU por regla con prueba automática", "Motor con tiempo lineal garantizado", "Despliegue escalonado con modo sombra", "Reversión instantánea de un solo paso"])],
        "Lo que enseña: lo que funcionó fue la respuesta; lo que faltó eran barreras de comportamiento del software. La cuarta columna es análisis propio y coincide en gran parte con las acciones que Cloudflare anunció.",
        CF + " " + ANALISIS)


def controles() -> Fig:
    return pairs(
        "Cada eslabón de la cadena y el control que lo corta",
        "Ocho pares de causa y control: expresión que retrocede, protección eliminada, motor sin garantías, pruebas que no miden CPU, procedimiento de despliegue global, reversión lenta, alerta tardía y acceso interno dependiente.",
        [("Expresión regular con retroceso", "Revisión específica de expresiones con herramientas de análisis y límites de tiempo"), ("Protección contra CPU eliminada en una refactorización", "Prueba que falle si la protección desaparece"),
         ("Motor sin garantías de complejidad", "Motor de tiempo lineal, como re2 o el de Rust"), ("Pruebas sin medida de CPU", "Perfil de rendimiento de cada regla en la batería de pruebas"),
         ("Despliegue global sin escalones", "Despliegue escalonado con modo sombra y salida de emergencia aparte"), ("Reversión de dos compilaciones", "Reversión de un solo paso, ensayada"),
         ("Alerta de caída tardía", "Alerta de caída de tráfico global con umbral corto"), ("Acceso interno dependiente del servicio caído", "Vía de acceso fuera del borde de Cloudflare, ensayada")],
        "Lo que enseña: cinco de las ocho mejoras coinciden con acciones que Cloudflare anunció: restituir la protección, perfilar reglas, cambiar de motor, escalonar el procedimiento y poder sacar el panel del borde. La columna inferior es análisis propio.",
        CF + " " + ANALISIS)


def despues() -> Fig:
    return chain(
        "La arquitectura «después»: cómo una regla llega a producción",
        "Cadena objetivo: la regla pasa por revisión, pruebas con perfil de CPU, ejecución en modo sombra en un punto de presencia, ampliación escalonada y despliegue global con interruptor de un paso; con un motor de tiempo lineal.",
        [("Revisión de la regla y análisis de su coste", "teal"), ("Pruebas con presupuesto de CPU por regla", "teal"), ("Modo sombra en un punto interno y luego en canarios", "teal"),
         ("Ampliación escalonada; vía rápida solo para ataques activos", "teal"), ("Motor de expresiones de tiempo lineal", "teal"), ("Interruptor de un paso y acceso fuera del borde", "teal")],
        "Lo que enseña: la vía rápida se conserva, como Cloudflare dice, pero con salvaguardas. Diseño didáctico; no describe con detalle lo que Cloudflare implantó más allá de lo que anunció.",
        CF + " " + ANALISIS, per_row=3, note_kind="teal")


def acciones() -> Fig:
    return columns(
        "Lo que Cloudflare anunció tras el incidente",
        "Tres columnas con las acciones del post mortem: hechas (reintroducir la protección y revisar las 3 868 reglas), previstas con fecha (perfil de CPU en las pruebas el 19 de julio y cambio a re2 o Rust el 31 de julio) y de plazo más largo (procedimiento escalonado, sacar el panel del borde, actualizar la página de estado, abandonar el WAF en Lua).",
        [("Hechas cuando se escribió el post", "teal", ["Parar todos los despliegues del WAF", "Reintroducir la protección contra exceso de CPU", "Inspeccionar a mano las 3 868 reglas"]),
         ("Con fecha prevista", "gold", ["Perfil de rendimiento de todas las reglas en las pruebas: 19 de julio", "Cambiar a re2 o al motor de Rust: 31 de julio"]),
         ("Más adelante", "navy", ["Procedimiento operativo con despliegue escalonado, conservando la vía de emergencia", "Poder sacar el panel y la API del borde", "Actualizar la página de estado automáticamente", "Abandonar el WAF en Lua por el nuevo motor de cortafuegos"])],
        "Lo que enseña: las acciones cubren el defecto, la distribución y la recuperación. Mira que el post mortem da fechas: esa precisión es parte de la transparencia. No verificamos aquí su cumplimiento posterior.",
        CF)


def pila() -> Fig:
    return layers(
        "Qué se sabe de la pila técnica",
        "Capas de la pila técnica: WAF escrito en Lua con PCRE como motor de expresiones regulares con retroceso; Quicksilver como almacén de claves y valores propio, antes Kyoto Tycoon; integración continua con TeamCity, Jira y BitBucket; alertas por PagerDuty; hardware y sistemas operativos no se detallan.",
        [("Cortafuegos de aplicaciones", "doc", "WAF Managed Rules, en Lua; usa PCRE, con retroceso y sin mecanismo contra una expresión desbocada"),
         ("Distribución", "doc", "Quicksilver: almacén de claves y valores replicado en más de 180 ciudades; antes se usó Kyoto Tycoon"),
         ("Entrega", "doc", "Git en BitBucket, TeamCity para compilar y probar, Jira para solicitudes de cambio"),
         ("Alertas", "doc", "PagerDuty con cientos de pruebas sintéticas desde fuera de la red"),
         ("Interruptor", "doc", "«Terminación global» para deshabilitar un componente en todo el mundo"),
         ("Hardware, sistema operativo, redes", "unk", "No constan con detalle en el post mortem; este caso no los inventa")],
        "Lo que enseña: el post mortem da el detalle suficiente para reproducir el mecanismo. Verde: documentado; gris: no se sabe.",
        CF)


def negocio() -> Fig:
    return chain(
        "Esquema del negocio: de la promesa de velocidad al riesgo del radio de impacto",
        "Esquema de negocio: Cloudflare ofrece a sus clientes proxy, red de entrega y cortafuegos desde una red global; el valor es responder rápido a nuevas amenazas y cambios de configuración; la misma velocidad hace que un error llegue a todos a la vez.",
        [("Clientes delegan en Cloudflare el proxy, la CDN y el WAF", "plain"), ("Valor: reglas nuevas contra amenazas en segundos", "teal"), ("Quicksilver distribuye cambios en un p99 de 2,29 s", "gold"), ("Un cambio erróneo llega igual de rápido a todas las máquinas", "coral")],
        "Lo que enseña: la promesa comercial y el riesgo técnico son la misma propiedad. Las fuentes verificadas no dan cifras de ingresos ni de clientes afectados; este caso no las inventa.",
        CF)


def consecuencias() -> Fig:
    return chain(
        "Consecuencias fechadas: de los 27 minutos a las acciones del post mortem",
        "Cadena de consecuencias: 27 minutos de errores 502 en todos los dominios con Cloudflare; WAF reactivado a las 14:52; parada de los despliegues del WAF; reintroducción de la protección; inspección de las 3 868 reglas; cambio de motor previsto para el 31 de julio.",
        [("2 jul 2019: 27 minutos de errores 502 en todo el mundo", "coral"), ("14:52: WAF reactivado tras pruebas", "teal"), ("Parada de despliegues del WAF e inspección de 3 868 reglas", "gold"), ("Cambio de motor previsto el 31 de julio; procedimiento escalonado", "navy")],
        "Lo que enseña: el impacto fue corto y total. Cloudflare dice que era su primer incidente global en seis años. Las fuentes verificadas no cuantifican clientes ni pérdidas; este caso no lo inventa.",
        CF)


def que_aprender() -> Fig:
    return columns(
        "Qué aprender y qué no generalizar",
        "Dos columnas: lo que se transfiere, como medir el coste de las reglas, escalonar los despliegues también cuando son rápidos y no depender de lo que se está arreglando; y lo que no se generaliza, como evitar las expresiones regulares o culpar al ingeniero que escribió la regla.",
        [("Se transfiere", "teal", ["Un cambio rápido necesita una red de seguridad medida, no solo funcional", "Cualquier motor con retroceso necesita límites o sustituirse", "Las herramientas de recuperación no deben depender de lo que se repara", "Un post mortem con horas y causas múltiples enseña más que una causa única"]),
         ("No se generaliza", "gold", ["No prueba que las expresiones regulares sean peligrosas: lo es un motor sin garantías", "No es el fallo de una persona: el post mortem enumera once condiciones", "Las cifras son de una red concreta y de 2019", "No describe el estado actual de Cloudflare"])],
        "Lo que enseña: el aprendizaje es de despliegue, rendimiento y recuperación. Mira la columna derecha: el caso se usa mal cuando se reduce a una expresión regular.",
        ANALISIS)


def antecedentes() -> Fig:
    f, y = sketch("De la primera caída de 2010 a la reactivación del WAF en 2019, en ocho hitos",
                  "Eje no proporcional con ocho hitos: en 2010 un cambio de Protocol Buffers rompió el DNS; semanas antes se eliminó una protección en una refactorización; 13:31, 13:37 y 13:42 fusión, pruebas y despliegue; 13:45 primer aviso; 14:00 WAF identificado; 14:07 terminación global; 14:52 WAF reactivado.")
    ev = [("2010: un cambio de Protocol Buffers rompió el DNS del autor del post", "navy"), ("Semanas antes: una refactorización elimina la protección de CPU", "coral"), ("13:31: se fusiona el cambio", "teal"), ("13:42: despliegue global automático", "coral"),
          ("13:45: primer aviso del WAF", "gold"), ("14:00: se identifica el WAF", "gold"), ("14:07: terminación global", "teal"), ("14:52: WAF reactivado", "teal")]
    yy = equi_axis(f, y + 6, ev, box_w=170, box_h=100)
    return done(f, yy,
                "Lo que enseña: el defecto se formó semanas antes, al quitar una protección para ahorrar CPU, y el incidente duró 27 minutos. Mira que los hitos de 2010 y de las semanas previas no están a escala del día.",
                "gold", CF)


FIGURES = {
    "cloudflare-2019-contexto.svg": contexto,
    "cloudflare-2019-perfil.svg": perfil,
    "cloudflare-2019-camino-de-una-regla.svg": flujo_waf,
    "cloudflare-2019-dos-caminos.svg": dos_caminos,
    "cloudflare-2019-pasos-del-motor.svg": regex_pasos,
    "cloudflare-2019-retroceso.svg": retroceso,
    "cloudflare-2019-minutos.svg": minutos,
    "cloudflare-2019-diagnostico.svg": secuencia,
    "cloudflare-2019-acceso-interno.svg": acceso,
    "cloudflare-2019-once-condiciones.svg": causas,
    "cloudflare-2019-puntos-unicos.svg": puntos_unicos,
    "cloudflare-2019-defensa-en-profundidad.svg": defensa,
    "cloudflare-2019-arbol-de-fallas.svg": arbol,
    "cloudflare-2019-a-prueba-de-fallos.svg": prueba_de_fallos,
    "cloudflare-2019-controles.svg": controles,
    "cloudflare-2019-arquitectura-despues.svg": despues,
    "cloudflare-2019-acciones-anunciadas.svg": acciones,
    "cloudflare-2019-hardware-y-software.svg": pila,
    "cloudflare-2019-esquema-del-negocio.svg": negocio,
    "cloudflare-2019-consecuencias.svg": consecuencias,
    "cloudflare-2019-antecedentes.svg": antecedentes,
    "cloudflare-2019-que-aprender.svg": que_aprender,
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
