"""Figuras del caso de estudio Slack (casos/exito/slack.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Las cifras salen del 10-K del año fiscal 2021 de Slack Technologies (SEC) y del blog de ingeniería de
Slack; cada pie de figura nombra su fuente. Ninguna figura repite una tabla del caso.
"""
from __future__ import annotations

from case_diagrams import years
from case_fig_helpers import hub, kanban, layer_stack
from figure_cases import case_cards
from figure_kit import grouped_bars, line_chart, timeline
from figures_part45_a import flow

TENK = "Fuente: 10-K de Slack Technologies, año fiscal terminado el 31 de enero de 2021 (SEC)."
BLOG = "Fuente: blog de ingeniería de Slack (slack.engineering), consulta 2026-11-23. Esquema del autor."
INF = "Trazo punteado en los esquemas: inferencia del curso, no arquitectura confirmada."


def contexto():
    return hub(
        "Slack en el centro de un ecosistema de equipos, aplicaciones y nube",
        "Diagrama de contexto: Slack conecta a las personas de una organización, a las aplicaciones y automatizaciones que publican mensajes, a los administradores y compradores, al proveedor de nube AWS donde corre el núcleo, a los clientes de otras organizaciones mediante canales compartidos y a Salesforce, que lo adquirió en 2021.",
        ("Slack: mensajería por canales", "navy"),
        [("Personas de una organización: mensajes, canales, llamadas", "teal", "usan"),
         ("Aplicaciones, bots y automatizaciones que publican y leen", "teal", "integran"),
         ("Administradores y compradores: planes, identidad, retención", "gold", "contratan"),
         ("Otras organizaciones: canales compartidos (Slack Connect)", "gold", "se conectan"),
         ("AWS: región us-east-1 para el núcleo y red de borde global", "plain", "aloja"),
         ("Salesforce: matriz desde julio de 2021", "plain", "adquirió"),
         ("Autoridades y reguladores: residencia de datos, privacidad", "coral", "exigen"),
         ("Competidores: otras suites y mensajería de empresa", "grey", "disputan")],
        "Documentado: el 10-K define a Slack como plataforma de mensajería basada en canales, nombra a AWS como proveedor de nube y describe la fusión con Salesforce. La relación con competidores y reguladores se cita en los factores de riesgo del mismo informe. Dónde deja de valer: no muestra volúmenes ni contratos.",
        TENK)


def ingresos():
    return years(grouped_bars(
        "Ingresos anuales de Slack, años fiscales 2017 a 2021",
        "Barras de ingresos en millones de dólares: 105 en el año fiscal 2017, 221 en 2018, 401 en 2019, 630 en 2020 y 903 en 2021; el ritmo de crecimiento baja de más del 100 por ciento a un 43 por ciento.",
        ["FY2017", "FY2018", "FY2019", "FY2020", "FY2021"],
        [("Ingresos (millones de USD)", [105.2, 220.5, 400.6, 630.4, 902.6], "teal")],
        unit="millones de USD", decimals=0, plot_h=240,
        note="Cada barra es un año fiscal que termina el 31 de enero. Mire la relación entre barras vecinas: de 2017 a 2018 los ingresos se duplican (110 %), de 2020 a 2021 crecen 43 %. Dónde deja de valer: son ingresos contables de un solo segmento; no separan suscripciones de otros ingresos.",
        foot=TENK))


def costos():
    return grouped_bars(
        "Cómo se reparte cada dólar de ingreso en el año fiscal 2021",
        "Barras horizontales del gasto como porcentaje del ingreso de 902,6 millones de dólares: coste de ingresos 13 por ciento, investigación y desarrollo 42 por ciento, ventas y marketing 51 por ciento y administración 24 por ciento; el total supera el 100 por ciento y por eso hay pérdida operativa.",
        ["Coste de ingresos", "Investigación y desarrollo", "Ventas y marketing", "Administración general"],
        [("Porcentaje del ingreso", [13.5, 42.3, 51.0, 24.5], "coral")],
        unit="% del ingreso FY2021", horizontal=True, decimals=1, plot_h=230,
        note="Cálculo propio a partir de las cifras del 10-K: 121,7; 382,1; 460,7 y 221,1 millones sobre 902,6. La suma es 131 % del ingreso: el margen bruto de 86,5 % existe, pero los gastos de operación lo superan. Dónde deja de valer: incluye remuneración en acciones, que no es caja.",
        foot=TENK)


def perdidas():
    return years(line_chart(
        "Ingresos y pérdida neta de Slack, años fiscales 2017 a 2021",
        "Dos líneas en millones de dólares: los ingresos suben de 105 a 903 y la pérdida neta pasa de 147 a 292 millones, con un máximo de 568 millones en el año fiscal 2020, año de la cotización directa.",
        [("Ingresos", [(2017, 105.2), (2018, 220.5), (2019, 400.6), (2020, 630.4), (2021, 902.6)], "teal"),
         ("Pérdida neta", [(2017, 146.9), (2018, 140.1), (2019, 138.9), (2020, 568.4), (2021, 292.5)], "coral")],
        x_label="Año fiscal (termina el 31 de enero)", y_label="Millones de USD", decimals=0,
        x_ticks=[(2017, "2017"), (2018, "2018"), (2019, "2019"), (2020, "2020"), (2021, "2021")],
        note="El salto de 2020 viene en gran parte de 245,1 millones de gasto de remuneración en acciones que se reconocieron de golpe al completarse la cotización directa, según el 10-K. Mire la distancia entre líneas: se cierra de 2018 a 2021. Dónde deja de valer: la pérdida neta no es flujo de caja.",
        foot=TENK))


def clientes():
    return years(line_chart(
        "Clientes de pago y retención neta de dólares, 2019 a 2021",
        "Línea de clientes de pago que crece de 88 mil a 156 mil entre enero de 2019 y enero de 2021, y segunda línea de retención neta de dólares que baja de 143 por ciento a 123 por ciento.",
        [("Clientes de pago (miles)", [(2019, 88), (2020, 110), (2021, 156)], "teal"),
         ("Retención neta de dólares (%)", [(2019, 143), (2020, 132), (2021, 123)], "gold")],
        x_label="Corte al 31 de enero", y_label="Miles de clientes / porcentaje", decimals=0,
        x_ticks=[(2019, "2019"), (2020, "2020"), (2021, "2021")],
        note="Dos magnitudes de unidades distintas comparten eje solo para mostrar la tendencia: más clientes y menos expansión por cliente. La retención de 123 % significa que los clientes que ya pagaban hace un año pagan ahora 23 % más en conjunto. Dónde deja de valer: Slack redondea los clientes al millar y define cliente de pago con tres o más usuarios de pago.",
        foot=TENK))


def grandes():
    return grouped_bars(
        "Clientes que pagan más de 100 000 dólares al año",
        "Barras con 575 clientes en enero de 2019, 893 en enero de 2020 y 1 183 en enero de 2021: la base de clientes grandes se duplica en dos años.",
        ["31 ene 2019", "31 ene 2020", "31 ene 2021"],
        [("Clientes con más de 100 000 USD", [575, 893, 1183], "navy")],
        unit="clientes", decimals=0, plot_h=220,
        note="Este es el indicador que Slack usa para medir la capacidad de escalar hacia organizaciones grandes. Mire el crecimiento de 106 % en dos años frente al 77 % de la base total de clientes de pago. Dónde deja de valer: no dice cuánto aporta cada cliente grande al ingreso total.",
        foot=TENK)


def actores():
    return hub(
        "Quién obtiene qué en el ecosistema de Slack",
        "Diagrama de incentivos: las personas obtienen una conversación persistente y buscable, los desarrolladores una audiencia para sus aplicaciones, los administradores control y retención, las organizaciones grandes un entorno unificado y Salesforce una pieza de su plataforma de clientes.",
        ("Slack: valor por organización, no por persona aislada", "navy"),
        [("Persona: sustituye hilos de correo por canales con historial", "teal", "gana contexto"),
         ("Desarrollador: llega a donde ya trabaja el equipo", "teal", "gana audiencia"),
         ("Administrador: identidad, permisos, retención, cumplimiento", "gold", "gana control"),
         ("Organización grande: varios espacios de trabajo unificados", "gold", "gana escala"),
         ("Comprador: paga por usuario activo del plan", "plain", "paga"),
         ("Salesforce: añade colaboración a su suite de clientes", "plain", "integra"),
         ("Competidor: ofrece mensajería dentro de su suite", "grey", "empaqueta"),
         ("Regulador: exige límites a los datos y a su retención", "coral", "limita")],
        "Análisis propio sobre hechos del 10-K: el producto se vende a una organización (cliente de pago) pero se adopta por personas que lo prueban gratis, de ahí el modelo de embudo y la métrica de retención neta. Dónde deja de valer: los incentivos de Salesforce tras 2021 son hipótesis, no declaraciones citadas.",
        TENK)


def recorridos():
    from case_diagrams import canvas, finish, lane_steps
    f = canvas("Cuatro recorridos de usuario en Slack y su caso límite",
               "Cuatro filas de pasos encadenados: persona invitada, administrador de una organización, desarrollador de una aplicación y organización con otra mediante un canal compartido; cada fila termina en un caso límite de diseño.")
    y = 56.0
    y = lane_steps(f, y, "Persona invitada", [("Recibe enlace y crea cuenta", "teal"), ("Entra a canales y ve historial", "teal"), ("Escribe, menciona, reacciona", "teal"), ("Silencia o abandona un canal ruidoso", "coral")])
    y = lane_steps(f, y, "Administrador", [("Crea el espacio de trabajo", "gold"), ("Define plan, identidad y permisos", "gold"), ("Configura retención y exportación", "gold"), ("Auditoría o petición legal: depende del plan", "coral")])
    y = lane_steps(f, y, "Desarrollador", [("Crea una aplicación y pide permisos", "navy"), ("Recibe eventos por HTTP o conexión", "navy"), ("Publica mensajes y botones", "navy"), ("Límites de tasa y reintentos", "coral")])
    y = lane_steps(f, y, "Dos organizaciones", [("Una invita a la otra a un canal", "plain"), ("Ambas aceptan y fijan políticas", "plain"), ("Mensajes cruzan entre espacios", "plain"), ("Una retira el acceso: qué queda", "coral")])
    return finish(f, y + 4, "Cada fila se lee de izquierda a derecha y la caja coral es el borde donde el diseño es más difícil. Los pasos son los que el 10-K y la documentación describen para el producto; el caso límite del desarrollador se apoya en la API pública y los demás son escenarios del curso. Dónde deja de valer: no mide cuántos usuarios llegan a cada borde.", "Esquema del autor sobre el 10-K de Slack (FY2021) y la documentación pública de la API.")


def negocio():
    return flow(
        "Cómo entra y sale el dinero en Slack",
        "Flujo del negocio: una persona prueba el plan gratuito, la organización pasa a un plan de pago por usuario, las cuentas grandes añaden contratos anuales y funciones de empresa; el ingreso se reconoce linealmente durante el contrato y se gasta sobre todo en ventas y en ingeniería.",
        [[("Equipos adoptan el plan gratuito (más de 600 000 organizaciones)", "teal"), ("Con tres o más usuarios de pago pasan a cliente de pago", "teal"), ("Contratos anuales por usuario; funciones de empresa", "gold"), ("Ingreso reconocido de forma lineal en el plazo", "navy")],
         [("Ventas y marketing: 51 % del ingreso", "coral"), ("Investigación y desarrollo: 42 %", "coral"), ("Hosting en AWS: compromiso mínimo contratado", "coral"), ("Retención neta de 123 %: la base existente se expande", "teal")]],
        note="Documentado en el 10-K (FY2021): modelo de suscripción por usuario con plan gratuito, reconocimiento lineal del ingreso, gasto de ventas de 460,7 millones y compromiso mínimo con AWS. Inferido: la secuencia del embudo es una lectura del curso sobre la definición de cliente de pago.",
        foot=TENK, width=960)


def contenedores():
    return layer_stack(
        "Capas de Slack que su ingeniería describió, de la pantalla al almacenamiento",
        "Pila de capas: clientes con una conexión WebSocket; borde regional con Envoy; servidores de pasarela, de canales, de presencia y de administración en Java; aplicación web en Hack; Vitess sobre MySQL como almacén; cola de trabajos; y AWS como infraestructura.",
        [("Clientes", "Aplicaciones web, de escritorio y móviles con una conexión WebSocket persistente", "teal"),
         ("Borde", "Red de borde global; Envoy termina TLS y reparte hacia las pasarelas", "plain"),
         ("Mensajería en tiempo real", "Servidores de pasarela, de canales, de presencia y de administración, escritos en Java", "plain"),
         ("Aplicación web", "Webapp en Hack: todas las API que llaman los clientes y el código de interfaz", "plain"),
         ("Datos", "Vitess sobre MySQL, con keyspaces; Memcached con Mcrouter; Redis para la cola", "gold"),
         ("Infraestructura", "AWS: núcleo en us-east-1 en varias zonas de disponibilidad; Consul para descubrimiento", "navy")],
        [("Documentado: lenguajes, componentes y números en posts de 2020 a 2022", "teal"), ("No se sabe: topología actual tras 2022 ni el reparto por región", "grey"), ("Inferido: un servicio nuevo reutiliza estas capas", "grey")],
        "Documentado en los posts de mensajería en tiempo real, Vitess, cola de trabajos y arquitectura celular. Dónde deja de valer: los posts son de 2020 a 2022 y Slack ha seguido cambiando; el blog de 2026 anuncia trabajo multi-nube que este caso no cubre.",
        BLOG)


def conexion():
    from case_diagrams import sequence
    return sequence(
        "Conectarse a Slack: del arranque al primer mensaje en tiempo real",
        "Secuencia de conexión: el cliente pide la configuración a la aplicación web, abre un WebSocket al borde más cercano, Envoy lo envía a un servidor de pasarela, que consulta los canales del usuario y se suscribe a los servidores de canal que los alojan.",
        ["Cliente", "Webapp (Hack)", "Envoy", "Pasarela", "Servidor de canal"],
        [(0, 1, "pide token y datos de conexión", ""), (1, 0, "devuelve token y URL del WebSocket", "ret"),
         (0, 2, "abre WebSocket en la región más cercana", ""), (2, 3, "reenvía la conexión", ""),
         (3, 1, "pide usuario y lista de canales", ""), (3, 4, "se suscribe según hash de cada canal", ""),
         (4, 0, "envía mensajes y eventos (por la pasarela)", "ret")],
        "Documentado en el post de mensajería en tiempo real. La pasarela mantiene suscripciones y usuarios; el servidor de canal guarda historial reciente en memoria y se elige por hash consistente del identificador del canal. Dónde deja de valer: omite autenticación, presencia y el arranque incremental del cliente.",
        BLOG)


def flannel():
    return flow(
        "Flannel: del arranque pesado al arranque bajo demanda",
        "Dos filas: antes de Flannel el cliente descargaba todo el estado del equipo con una sola llamada y se conectaba a los servidores de origen; con Flannel un caché de aplicación en el borde sirve una versión reducida y envía datos por adelantado cuando prevé que el cliente los necesitará.",
        [[("Antes: el cliente pide todo el estado del equipo al arrancar", "coral"), ("Costes: conexión lenta, memoria alta, reconexiones caras", "coral"), ("Tormenta de reconexiones cuando una oficina se desconecta", "coral")],
         [("Después: el cliente se conecta a Flannel en el borde", "teal"), ("Flannel reúne el estado y devuelve una versión reducida", "teal"), ("Consultas bajo demanda y envío anticipado de datos", "teal")]],
        note="Documentado en el post «Flannel» de Slack: el problema aparece en equipos de decenas de miles de personas; la solución carga lo mínimo y trae el resto cuando hace falta, por ejemplo enviando los datos de una persona mencionada antes del mensaje. Dónde deja de valer: Slack no publica cifras de mejora en ese post.",
        foot=BLOG, width=960)


def canales():
    return hub(
        "Servidores de canal: reparto por hash y reemplazo rápido",
        "Esquema de reparto: el identificador de canal pasa por un hash consistente que lo asigna a un servidor de canal; los servidores de canal tienen estado en memoria y cada uno atiende alrededor de 16 millones de canales en hora punta; los gestores del anillo detectan un servidor enfermo y lo reemplazan en menos de 20 segundos.",
        ("Anillo de hash consistente de servidores de canal", "navy"),
        [("Canal, usuario, equipo, archivo o huddle: todos tienen identificador", "teal", "se hashea"),
         ("Servidor de canal: estado y algo de historial en memoria", "gold", "atiende ~16 M canales"),
         ("Gestores del anillo (CHARMs): sustituyen un servidor malo", "plain", "<20 s"),
         ("Consul: el resto de servicios descubre la configuración", "plain", "publica"),
         ("Un equipo reparte sus canales entre todos los servidores", "teal", "dispersión"),
         ("Pasarela: se suscribe a los servidores que alojan sus canales", "plain", "suscribe")],
        "Documentado: cifras de 16 millones de canales por servidor en hora punta y reemplazo en menos de 20 segundos. La consecuencia de diseño es que la caída de un servidor afecta una fracción pequeña de cada equipo durante segundos. Dónde deja de valer: el número es del post de ingeniería, sin fecha de medición precisa.",
        BLOG)


def vitess():
    return flow(
        "Del MySQL particionado por equipo a Vitess",
        "Dos etapas: al principio tres clústeres MySQL (fragmentos por identificador de equipo, metadatos y todo lo demás) gestionados por la aplicación; desde 2017 Vitess sobre MySQL con keyspaces, que ofrece enrutado, copias y resharding.",
        [[("Stack LAMP: MySQL desde el primer día", "plain"), ("Fragmentos por equipo: todos los datos de un equipo juntos", "plain"), ("Clúster de metadatos y clúster de «todo lo demás»", "plain"), ("La aplicación monolítica decide a qué fragmento ir", "coral")],
         [("2017: comienza la migración a Vitess", "gold"), ("Keyspaces con distintas claves de fragmentación", "teal"), ("Vitess sirve 99 % de la carga de consultas (2020)", "teal"), ("Habilita Slack Connect y residencia de datos", "teal")]],
        note="Documentado en el post «Scaling Datastores at Slack with Vitess» (diciembre de 2020). Dónde deja de valer: la clave de fragmentación por equipo funcionó mientras ningún equipo fue mayor que un fragmento; las funciones entre equipos (Slack Connect) forzaron otra forma de particionar.",
        foot=BLOG, width=960)


def consultas():
    return grouped_bars(
        "Carga de consultas de Vitess en hora punta (2020)",
        "Barras horizontales: 2,3 millones de consultas por segundo en hora punta, de las cuales 2,0 millones son lecturas y 0,3 millones escrituras; la latencia mediana es 2 milisegundos y el percentil 99 es 11 milisegundos.",
        ["Total", "Lecturas", "Escrituras"],
        [("Millones de consultas por segundo", [2.3, 2.0, 0.3], "teal")],
        unit="millones de consultas por segundo", horizontal=True, decimals=1, plot_h=170,
        note="Mire la proporción: de cada ocho consultas, siete son lecturas. Eso explica la inversión en cachés (Memcached) y en réplicas de lectura. La latencia citada es 2 ms de mediana y 11 ms en el percentil 99. Dónde deja de valer: es una medición de hora punta de 2020, no un promedio.",
        foot="Fuente: «Scaling Datastores at Slack with Vitess», slack.engineering, 1 de diciembre de 2020.")


def cola():
    return flow(
        "El fallo de la cola de trabajos: cómo un límite de memoria bloqueó todo",
        "Cadena de causas: contención en la base de datos ralentiza los trabajos, Redis llega al límite de memoria, ya no se pueden encolar trabajos y además la cola necesitaba memoria libre para sacar trabajos, de modo que no se recuperó sola.",
        [[("Contención en la base de datos", "coral"), ("Los trabajos tardan más y se acumulan en Redis", "coral"), ("Redis llega a su máximo de memoria", "coral")],
         [("No se puede encolar: fallan mensajes, notificaciones y recordatorios", "coral"), ("Sacar un trabajo exigía memoria libre: no hay salida", "coral"), ("Recuperación manual y rediseño de la cola", "teal")]],
        note="Documentado en «Scaling Slack's Job Queue»: el sistema procesaba más de 1 400 millones de trabajos en un día punta, a un máximo de 33 000 por segundo. Lección de diseño que el propio post extrae: una cola no debe necesitar recursos escasos para drenar. Dónde deja de valer: la fecha exacta del incidente no figura en el fragmento citado.",
        foot=BLOG, width=960)


def incidente_2021():
    return timeline(
        "4 de enero de 2021: la red de AWS se satura y el nivel web no puede crecer",
        "Línea de tiempo en minutos desde las 6:50 hora del Pacífico: errores crecientes antes de las 7:00, saturación del nivel web a las 7:00, intento de añadir 1 200 servidores entre las 7:01 y las 7:15, restauración del servicio de aprovisionamiento hacia las 8:15, Slack degradado pero activo a las 9:15 y red normal a las 10:40.",
        [("Usuarios", [(0, 10, "", "gold"), (10, 145, "Slack no disponible o muy degradado", "coral"), (145, 230, "degradado, no caído", "gold")]),
         ("Nivel web", [(10, 25, "", "gold"), (25, 85, "sin aprovisionar", "coral"), (85, 145, "se recupera", "teal")]),
         ("Red de AWS", [(0, 230, "pasarela de tránsito saturada, con pérdida de paquetes", "coral")])],
        unit="minutos desde las 6:50 (hora del Pacífico)", events=[(10, "7:00"), (85, "8:15"), (145, "9:15"), (230, "10:40")],
        t_max=240, ticks=[0, 60, 120, 180, 240], lane_h=46,
        note="Las horas son las del post. El detonante fue una pasarela de tránsito de AWS que no escaló tras la semana de vacaciones; el agravante, un servicio de aprovisionamiento que llegó a los límites de archivos abiertos y de cuota de AWS. Dónde deja de valer: los segmentos de la lane del nivel web son aproximaciones del dibujo a partir de las horas citadas.",
        foot="Fuente: «Slack's Outage on January 4th 2021», slack.engineering. Segmentos dibujados por el autor.")


def incidente_2022():
    return flow(
        "22 de febrero de 2022: caché vaciada, consulta dispersa y arranque saturado",
        "Cadena de la caída: una actualización escalonada del agente Consul retira nodos de caché que se reemplazan por nodos vacíos; la tasa de aciertos cae; una consulta de grupos de mensajes directos se dispersa por todos los fragmentos del keyspace; la base se sobrecarga y el arranque de clientes falla; se mitiga limitando la tasa de arranques.",
        [[("Actualización de Consul en 25 % de la flota", "gold"), ("Nodos de caché salen y entran: Mcrib los reemplaza por vacíos", "coral"), ("Cae la tasa de aciertos de la caché", "coral")],
         [("Consulta por usuarios de un grupo: consulta dispersa a todos los fragmentos", "coral"), ("Keyspace de miembros sobrecargado; el arranque del cliente falla", "coral"), ("Mitigación: limitar arranques y subir el límite poco a poco", "teal")]],
        note="Documentado en «Slack's Incident on 2-22-22». El post subraya que dos pasos previos de la misma actualización habían ido bien: el fallo apareció al coincidir con la hora punta. Dónde deja de valer: es una cadena simplificada de un incidente descrito con muchos más factores.",
        foot=BLOG, width=960)


def celdas():
    return kanban(
        "Zonas de disponibilidad como celdas que se pueden drenar",
        "Cuatro columnas: el problema (un fallo gris en una zona de disponibilidad), los objetivos del botón de drenaje (retirar tráfico en menos de 5 minutos, sin errores visibles, incremental y sin depender de la zona enferma), la dificultad (cuatro lenguajes y varios mecanismos de descubrimiento) y el resultado (una zona se trata como una celda).",
        [("Problema", "coral", ["30 de junio de 2021: un enlace de red falla de forma intermitente", "Una petición se abre en cientos de llamadas; cada zona ve algo distinto"]),
         ("Objetivos", "gold", ["Retirar tráfico de una zona en menos de 5 minutos", "Sin errores visibles; incremental, desde 1 %", "No depender de recursos de la zona drenada"]),
         ("Dificultad", "plain", ["Servicios en Hack, Go, Java y C++", "Envoy xDS, Consul y DNS como descubrimiento", "Vitess exige un único primario por fragmento"]),
         ("Resultado", "teal", ["Cada zona es una celda que se puede drenar", "Decisión humana asistida por un botón, no autocuración"])],
        "Documentado en «Slack's Migration to a Cellular Architecture». El SLA de 99,99 % deja menos de una hora al año de indisponibilidad total, de ahí el objetivo de 5 minutos. Dónde deja de valer: el post explica el diseño, no cuántas veces se ha usado el drenaje.",
        BLOG, box_h=92)


def especiales():
    return case_cards(
        "Casos especiales documentados y cómo se resuelven",
        "Cinco tarjetas de caso: equipo con decenas de miles de personas, primer lunes tras las vacaciones, zona de disponibilidad con fallo gris, cola sin memoria para drenar y consulta dispersa en hora punta; cada una con el mecanismo de contención y su veredicto.",
        [("Equipo de decenas de miles de personas", "El cliente carga lo mínimo y pide el resto a Flannel", "El arranque con todo el estado no escala; la solución es perezosa y anticipada.", "teal"),
         ("Primer lunes tras las vacaciones (4 ene 2021)", "Cachés frías y pico de media hora saturan una pasarela de AWS", "Un patrón anual poco frecuente supera lo que un servicio gestionado escala solo.", "coral"),
         ("Un enlace de red falla a medias (30 jun 2021)", "Se construye el drenaje de zonas de disponibilidad", "Un fallo gris no se autocura bien: se facilita la decisión humana.", "gold"),
         ("Redis sin memoria libre para sacar trabajos", "La cola se rediseña con cambios graduales", "Un mecanismo de recuperación que necesita recursos escasos deja de serlo.", "coral"),
         ("Consulta que dispersa a todos los fragmentos", "Se limita la tasa de arranques hasta que la caché se llena", "Una consulta barata con poco tráfico es un incendio con mucho.", "gold")],
        note="Cada tarjeta enlaza un hecho citado en el caso con el mecanismo de la clase correspondiente. El color indica el veredicto: coral falla o sorprende, teal se sostiene y gold depende de condiciones. Dónde deja de valer: son cinco casos documentados, no un catálogo exhaustivo.",
        foot=BLOG)


def linea():
    return years(timeline(
        "Slack de 2009 a 2022: empresa, datos y resiliencia",
        "Línea de tiempo con tres carriles: la empresa (Tiny Speck desde 2009, Slack desde 2014, parte de Salesforce desde julio de 2021), los datos (migración a Vitess desde 2017 hasta 2020) y la resiliencia (incidentes de enero de 2021, junio de 2021 y febrero de 2022).",
        [("Empresa", [(2009, 2014, "Tiny Speck", "grey"), (2014, 2021.55, "Slack Technologies", "teal"), (2021.55, 2026, "Parte de Salesforce", "navy")]),
         ("Datos", [(2017, 2020.95, "Migración a Vitess", "gold")]),
         ("Resiliencia", [(2021.0, 2021.1, "", "coral"), (2021.5, 2021.6, "", "coral"), (2022.1, 2022.2, "", "coral")])],
        unit="año", events=[(2014, "lanzamiento público"), (2019.45, "cotización directa"), (2020.92, "acuerdo con Salesforce"), (2021.55, "cierre")],
        t_max=2027, ticks=[2009, 2012, 2015, 2018, 2021, 2024, 2027], lane_h=46,
        note="Hechos con fuente: constitución en 2009 y cambio de nombre en 2014 (10-K); acuerdo de fusión del 1 de diciembre de 2020 y cierre del 21 de julio de 2021 (8-K); incidentes del 4 de enero de 2021, 30 de junio de 2021 y 22 de febrero de 2022 (blog). Dónde deja de valer: la fecha de la cotización directa es aproximada en el eje (año fiscal 2020).",
        foot="Fuentes: 10-K FY2021, 8-K del 21 de julio de 2021 y blog de ingeniería de Slack."))


def alternativas():
    return case_cards(
        "Alternativas que Slack no tomó o sustituyó, como análisis del curso",
        "Cuatro tarjetas de alternativas: seguir con MySQL particionado a mano, cargar todo el estado en el cliente, depender solo de redundancia automática entre zonas y mantener un único repositorio en un solo lenguaje; cada una con el coste que Slack documenta o que el curso infiere.",
        [("Seguir con MySQL particionado a mano", "Vitess desde 2017", "Documentado: la aplicación monolítica decidía el fragmento; las funciones entre equipos obligaban a otra clave.", "teal"),
         ("Cargar todo el estado en el cliente", "Flannel y carga bajo demanda", "Documentado: no escala con equipos grandes ni con reconexiones masivas.", "teal"),
         ("Confiar solo en la redundancia entre zonas", "Drenaje de zonas por decisión humana", "Documentado: un fallo gris engañó a la detección automática.", "gold"),
         ("Un solo lenguaje y runtime", "Hack, Go, Java y C++", "Documentado como realidad; el coste es una implementación distinta de cada mecanismo común.", "coral")],
        note="Rótulo: análisis propio. Las dos primeras filas son decisiones que Slack explica en su blog; las dos últimas son consecuencias que el blog menciona de pasada. Dónde deja de valer: Slack no publica alternativas evaluadas con sus costes, solo el razonamiento de lo que eligió.",
        foot=BLOG)


def hardware():
    return layer_stack(
        "Hardware y software que Slack hace público",
        "Pila de lo que se sabe: no hay hardware propio publicado; el núcleo corre en máquinas virtuales de AWS en varias zonas de disponibilidad de us-east-1; el software documentado incluye Hack, Java, Go, C++, Envoy, Consul, Vitess, MySQL, Memcached con Mcrouter y Redis.",
        [("Hardware", "Sin hardware propio publicado: instancias de AWS en varias zonas de us-east-1", "grey"),
         ("Red", "Pasarelas de tránsito de AWS entre cuentas y VPC; borde regional propio", "plain"),
         ("Descubrimiento", "Consul; Envoy y su API xDS; DNS", "plain"),
         ("Servicios", "Webapp en Hack; pasarela, canal y presencia en Java; piezas en Go y C++", "plain"),
         ("Datos y caché", "Vitess sobre MySQL; Memcached con Mcrouter y Mcrib; Redis en la cola", "gold")],
        [("Documentado en posts de 2020 a 2022", "teal"), ("No se sabe: tipos de instancia, tamaños y costes por componente", "grey")],
        "Lo que Slack revela es software y topología, no equipos físicos: el 10-K dice que alquila oficinas y que su infraestructura vive en proveedores de nube. Dónde deja de valer: ni el número de servidores ni la cuenta de AWS se publican; el compromiso mínimo con AWS es la única magnitud económica de infraestructura.",
        BLOG)


def hosting():
    return grouped_bars(
        "Compromiso mínimo con AWS por año contratado (mayo de 2020 a abril de 2025)",
        "Barras con el compromiso mínimo anual de 75 millones de dólares en el primer periodo que crece 5 millones cada año hasta 95 millones en el quinto, con un total mínimo de 425 millones; quedaban 353,7 millones por pagar al 31 de enero de 2021.",
        ["Año 1", "Año 2", "Año 3", "Año 4", "Año 5"],
        [("Mínimo anual (millones de USD)", [75, 80, 85, 90, 95], "navy")],
        unit="millones de USD", decimals=0, plot_h=220,
        note="Cálculo propio a partir de la regla del 10-K (75 millones más 5 millones cada año, total de 425 millones). Mire que el compromiso es un piso, no el gasto real. Dónde deja de valer: el gasto real en nube de Slack no es público y el 10-K no lo desglosa.",
        foot=TENK)


def pruebas_fallo():
    return case_cards(
        "Temas a prueba de fallos que Slack documenta",
        "Cinco mecanismos con su veredicto: reemplazo rápido de servidores de canal, drenaje de zonas, limitación de arranques, modo pánico de los balanceadores y estado perezoso en el cliente; cada uno con el fallo que contiene.",
        [("Servidor de canal enfermo", "Reemplazo en menos de 20 s por el anillo", "Afecta a una fracción pequeña de cada equipo durante segundos.", "teal"),
         ("Zona de disponibilidad con fallo gris", "Drenaje de tráfico desde la zona", "Requiere que un humano lo decida, pero lo hace rápido y reversible.", "gold"),
         ("Base de datos sobrecargada por el arranque", "Limitar la tasa de arranques de cliente", "Sacrifica a quienes no tienen cliente arrancado para salvar a quienes sí.", "gold"),
         ("Casi todos los balanceadores fallan sus pruebas de salud", "Modo pánico: repartir entre todas las instancias", "Evita vaciar el grupo cuando el problema es la red, no los servidores.", "teal"),
         ("Reconexión masiva tras una caída de red", "Estado mínimo en el cliente, resto bajo demanda", "Limita la tormenta de peticiones al reconectar.", "teal")],
        note="Documentado en los posts de Flannel, de mensajería en tiempo real, de la caída de enero de 2021 y de la arquitectura celular. Dónde deja de valer: los mecanismos funcionaron en esos incidentes, lo que no demuestra que cubran cualquier fallo.",
        foot=BLOG)


FIGURES = {
    "slack-contexto.svg": contexto,
    "slack-ingresos-anuales.svg": ingresos,
    "slack-reparto-del-ingreso.svg": costos,
    "slack-ingresos-y-perdida.svg": perdidas,
    "slack-clientes-y-retencion.svg": clientes,
    "slack-clientes-grandes.svg": grandes,
    "slack-actores-e-incentivos.svg": actores,
    "slack-recorridos-de-usuario.svg": recorridos,
    "slack-esquema-del-negocio.svg": negocio,
    "slack-capas.svg": contenedores,
    "slack-secuencia-de-conexion.svg": conexion,
    "slack-flannel.svg": flannel,
    "slack-servidores-de-canal.svg": canales,
    "slack-evolucion-de-datos.svg": vitess,
    "slack-carga-de-vitess.svg": consultas,
    "slack-cola-de-trabajos.svg": cola,
    "slack-caida-enero-2021.svg": incidente_2021,
    "slack-caida-febrero-2022.svg": incidente_2022,
    "slack-celdas-y-drenaje.svg": celdas,
    "slack-casos-especiales.svg": especiales,
    "slack-linea-de-tiempo.svg": linea,
    "slack-alternativas.svg": alternativas,
    "slack-hardware-y-software.svg": hardware,
    "slack-compromiso-con-aws.svg": hosting,
    "slack-a-prueba-de-fallos.svg": pruebas_fallo,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys

    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
