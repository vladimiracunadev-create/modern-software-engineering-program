"""Figuras del caso de estudio Discord (casos/exito/discord.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Las cifras salen de la página de empresa de Discord y de su blog de ingeniería (2017 a 2023); Discord no
publica estados financieros en las fuentes consultadas. Cada pie de figura nombra su fuente. Ninguna
figura repite una tabla del caso.
"""
from __future__ import annotations

from case_diagrams import canvas, finish, lane_steps, sequence, years
from case_fig_helpers import hub, kanban, layer_stack
from figure_cases import case_cards
from figure_kit import grouped_bars, timeline
from figures_part45_a import flow

BLOG = "Fuente: blog de ingeniería de Discord (discord.com/blog), consulta 2026-11-23. Esquema del autor."
CO = "Fuente: página «Acerca de Discord» (discord.com/company), consulta 2026-11-23."


def contexto():
    return hub(
        "Discord entre jugadores, comunidades, desarrolladores y plataformas",
        "Diagrama de contexto: los jugadores hablan por texto, voz y vídeo en servidores; los administradores y moderadores gestionan las comunidades; los desarrolladores de juegos integran la API y el SDK social; los suscriptores de Nitro financian el servicio; las consolas y plataformas de juegos enlazan cuentas; los anunciantes pagan por Quests.",
        ("Discord: texto, voz y vídeo para hablar mientras se juega", "navy"),
        [("Jugadores: más de 90 millones de usuarios activos diarios", "teal", "usan"),
         ("Administradores y moderadores de servidores", "teal", "gestionan"),
         ("Desarrolladores de juegos: API, Activities y Social SDK", "gold", "integran"),
         ("Suscriptores de Nitro y de Server Boosting", "gold", "pagan"),
         ("Anunciantes y editores: Quests y comercio social", "gold", "pagan"),
         ("Consolas y plataformas: PlayStation, PC y móvil", "plain", "enlazan"),
         ("Familias, menores y reguladores: seguridad y privacidad", "coral", "exigen"),
         ("Competidores: otras apps de chat y de juegos", "grey", "disputan")],
        "Documentado en la página de empresa de Discord: la cifra de más de 90 millones de usuarios activos diarios es del cuarto trimestre de 2025 y de datos internos; Discord no publica estados financieros en las fuentes consultadas. Dónde deja de valer: no hay cifras de ingresos ni de reparto por fuente.",
        CO)


def mensajes():
    return grouped_bars(
        "Mensajes por día que Discord anunció en 2016 y 2017",
        "Barras con 40 millones de mensajes al día en julio de 2016, 100 millones en diciembre de 2016 y más de 120 millones a comienzos de 2017: el volumen se triplica en medio año.",
        ["Julio de 2016", "Diciembre de 2016", "Enero de 2017"],
        [("Millones de mensajes por día", [40, 100, 120], "teal")],
        unit="millones de mensajes por día", decimals=0, plot_h=230,
        note="La última barra es «más de 120 millones»: es un mínimo. Mire el salto de julio a diciembre: 2,5 veces en cinco meses, que es lo que empujó a cambiar de base de datos. Dónde deja de valer: son cifras de hace diez años; el post de 2023 habla de billones de mensajes almacenados.",
        foot="Fuente: «How Discord Stores Billions of Messages», discord.com/blog, enero de 2017.")


def nodos():
    return grouped_bars(
        "Cuántos servidores necesitó guardar los mensajes: de Cassandra a ScyllaDB",
        "Barras con 12 nodos de Cassandra en 2017, 177 nodos de Cassandra a comienzos de 2022 y 72 nodos de ScyllaDB tras migrar en mayo de 2022; los nodos nuevos tienen 9 teras de disco frente a 4 de los anteriores.",
        ["Cassandra 2017", "Cassandra 2022", "ScyllaDB 2023"],
        [("Nodos", [12, 177, 72], "navy")],
        unit="nodos", decimals=0, plot_h=230,
        note="El número de nodos pasó de 12 a 177 al crecer de miles de millones a billones de mensajes, y bajó a 72 con la migración; además, cada nodo de ScyllaDB tiene 9 TB de disco en lugar de unos 4 TB. Dónde deja de valer: el volumen de mensajes también cambió entre fechas; no es una comparación a datos iguales.",
        foot="Fuente: «How Discord Stores Trillions of Messages», discord.com/blog, 2023.")


def latencias():
    return grouped_bars(
        "Latencia en el percentil 99 de la base de mensajes, antes y después",
        "Barras agrupadas en milisegundos: leer mensajes históricos pasó de un percentil 99 de 40 a 125 milisegundos en Cassandra a 15 milisegundos en ScyllaDB, y escribir un mensaje de 5 a 70 milisegundos a unos 5 milisegundos estables.",
        ["Leer historial (peor caso)", "Insertar mensaje (peor caso)"],
        [("Cassandra (extremo alto del rango)", [125, 70], "coral"), ("ScyllaDB", [15, 5], "teal")],
        unit="milisegundos, percentil 99", decimals=0, plot_h=240,
        note="Cassandra se muestra con el extremo alto de los rangos que Discord publica (40-125 ms y 5-70 ms) porque el problema era la variabilidad. Mire que la diferencia más grande es de la lectura: 8 veces. Dónde deja de valer: son mediciones del propio Discord en su carga real, no un banco de pruebas neutral.",
        foot="Fuente: «How Discord Stores Trillions of Messages», discord.com/blog, 2023.")


def actores():
    return hub(
        "Quién obtiene qué en el ecosistema de Discord",
        "Diagrama de incentivos: los jugadores obtienen un lugar para hablar mientras juegan; los administradores una comunidad; los desarrolladores acceso a esa audiencia; los suscriptores funciones extra; los anunciantes atención mediante misiones; Discord ingresos de suscripciones y de acuerdos.",
        ("Discord: gratis para hablar; paga quien quiere más o quien busca audiencia", "navy"),
        [("Jugador: voz y texto sin coste mientras juega", "teal", "gana"),
         ("Administrador: herramientas para construir una comunidad", "teal", "gana"),
         ("Suscriptor de Nitro: emojis, perfil y mejoras", "gold", "paga"),
         ("Comunidad que impulsa su servidor con Boosts", "gold", "paga"),
         ("Desarrollador de juegos: audiencia, chat y comercio", "plain", "integra"),
         ("Anunciante: Quests para captar jugadores", "plain", "paga"),
         ("Familias: piden protecciones para menores", "coral", "exigen"),
         ("Competidor: otras apps de chat", "grey", "disputan")],
        "Análisis propio sobre la historia que Discord publica: Nitro (2017), Server Boosting (2019), Quests y Orbs (2025) y la prueba de comercio social (2025) son las vías de ingreso que menciona. Dónde deja de valer: no hay cifras de cuánto aporta cada una.",
        CO)


def recorridos():
    f = canvas("Cuatro recorridos en Discord y su caso límite",
               "Cuatro filas de pasos: un jugador que entra a un servidor, un administrador que crea una comunidad, un desarrollador que integra el chat en su juego y una persona que se une a una comunidad de más de un millón de conectados; cada fila termina en un caso límite.")
    y = 56.0
    y = lane_steps(f, y, "Jugador", [("Recibe una invitación a un servidor", "teal"), ("Entra a canales de texto y voz", "teal"), ("Habla mientras juega", "teal"), ("Aviso a @everyone: todos leen a la vez", "coral")])
    y = lane_steps(f, y, "Administrador", [("Crea un servidor", "gold"), ("Define canales, roles y permisos", "gold"), ("Invita y modera", "gold"), ("Servidor de decenas de miles de conectados", "coral")])
    y = lane_steps(f, y, "Desarrollador", [("Usa la API o los bots", "navy"), ("Enlaza cuentas de juego y de Discord", "navy"), ("Chat de voz y texto dentro del juego", "navy"), ("Millones de eventos por segundo", "coral")])
    y = lane_steps(f, y, "Comunidad enorme", [("Se une a un servidor con millones de miembros", "plain"), ("Recibe solo lo del servidor activo", "plain"), ("Hace clic y pasa a conexión activa", "plain"), ("Un millón de conectados a la vez", "coral")])
    return finish(f, y + 4, "Cada fila se lee de izquierda a derecha y la caja coral es el borde. Los bordes del jugador y de la comunidad enorme salen de los posts sobre Elixir y sobre servidores de un millón de conectados; el del desarrollador, de la línea de tiempo oficial de Discord. Dónde deja de valer: no mide cuántos usuarios llegan a cada borde.", "Esquema del autor sobre el blog de ingeniería de Discord y su página de empresa.")


def negocio():
    return flow(
        "Cómo gana dinero Discord según lo que publica",
        "Flujo del negocio: la comunicación es gratuita y atrae a jugadores; Nitro y los Boosts monetizan a quien quiere más; desde 2025 los Quests y el comercio social monetizan a editores y desarrolladores; no hay cifras públicas de ingresos en las fuentes consultadas.",
        [[("Chat de texto, voz y vídeo gratuito: 90 millones de usuarios diarios", "teal"), ("Nitro (2017): perfil, emojis y mejoras", "gold"), ("Server Boosting (2019): la comunidad desbloquea mejoras", "gold"), ("Quests y Orbs (2025): misiones pagadas por anunciantes", "gold")],
         [("Comercio social (2025): venta de objetos de juego en servidores oficiales", "gold"), ("Social SDK (2025): chat de Discord dentro de juegos", "plain"), ("Ingresos: no se publican", "grey"), ("Costes de infraestructura: no se publican", "grey")]],
        note="Documentado en la línea de tiempo oficial de Discord. Inferido: que Nitro es la fuente principal de ingresos históricos, por ser la más antigua y la que la empresa destaca; Discord no lo cuantifica. Cualquier cifra de ingresos que circule no se usa aquí por falta de fuente primaria.",
        foot=CO, width=960)


def capas():
    return layer_stack(
        "Capas de Discord que su ingeniería describió",
        "Pila de capas: clientes web, de escritorio, móviles y de consola; puerta de enlace con WebSocket y procesos de sesión en Elixir; procesos de servidor (guild) y relays en Elixir; API monolítica en Python; servicios de datos en Rust; ScyllaDB para mensajes; servidores de voz con WebRTC.",
        [("Clientes", "Web, escritorio y móvil; motor C++ nativo sobre WebRTC en las aplicaciones instaladas", "teal"),
         ("Puerta de enlace", "WebSocket por usuario con un proceso de sesión (GenServer) en Elixir", "plain"),
         ("Tiempo real", "Un proceso de servidor (guild) por comunidad y relays que reparten el envío a las sesiones", "plain"),
         ("API y servicios de datos", "API monolítica; servicios de datos en Rust con una consulta gRPC por operación", "plain"),
         ("Almacenes", "ScyllaDB para mensajes (antes Cassandra y MongoDB); no más de lo publicado", "gold"),
         ("Voz y vídeo", "Servidores de medios que reenvían el audio; señalización en Elixir", "navy")],
        [("Documentado en posts de 2017 a 2023", "teal"), ("No se sabe: proveedor de nube, regiones y tamaño de flota", "grey"), ("Inferido: la API monolítica sigue siendo la puerta de negocio", "grey")],
        "Documentado en los posts de Elixir (2017 y 2019), de Rust (2020), de mensajes (2017 y 2023), de servidores grandes (2022) y de voz (2018). Dónde deja de valer: el detalle de 2023 en adelante sobre la API y las regiones no es público en las fuentes consultadas.",
        BLOG)


def secuencia():
    return sequence(
        "De un mensaje enviado a su aparición en otras pantallas y en la base de datos",
        "Secuencia de un mensaje: el cliente lo envía a la API; la API lo guarda mediante el servicio de datos en ScyllaDB; el proceso del servidor (guild) lo recibe y lo reparte a las sesiones de los usuarios conectados, que lo envían por WebSocket a sus clientes.",
        ["Cliente", "API", "Servicio de datos", "ScyllaDB", "Proceso guild", "Sesiones"],
        [(0, 1, "envía el mensaje", ""), (1, 2, "guarda (una consulta gRPC)", ""), (2, 3, "escribe por canal y ventana de tiempo", ""),
         (1, 4, "publica el evento al servidor", ""), (4, 5, "reparte a cada sesión con permisos", ""), (5, 0, "WebSocket al resto de clientes", "ret")],
        "Documentado en conjunto, no como una única secuencia oficial: la API que persiste mensajes, los servicios de datos de Rust, ScyllaDB, el proceso por comunidad y las sesiones por usuario salen de posts distintos. Inferido: el orden exacto entre guardar y repartir. Dónde deja de valer: omite relays, permisos y la vía de bots.",
        BLOG)


def cuadratico():
    return grouped_bars(
        "El trabajo de repartir un mensaje crece con el cuadrado del tamaño del servidor",
        "Barras en escala logarítmica: si todos los conectados escriben una vez, un servidor con 1 000 personas genera 1 millón de notificaciones, uno con 10 000 genera 100 millones y uno con 100 000 genera 10 mil millones.",
        ["1 000 conectados", "10 000 conectados", "100 000 conectados"],
        [("Notificaciones (millones)", [1, 100, 10000], "coral")],
        unit="millones de notificaciones", log=True, decimals=0, plot_h=240,
        note="Es el cálculo del propio post: la actividad es proporcional al número de personas y el reparto de cada mensaje también, de modo que el trabajo crece al cuadrado. Mire la escala logarítmica: cada barra es 100 veces la anterior. Dónde deja de valer: es un modelo del peor caso en que todos hablan.",
        foot="Fuente: «Maxjourney», discord.com/blog, 2022. Cálculo del post; escala logarítmica.")


def manifold():
    return flow(
        "Manifold: repartir el envío de mensajes entre nodos",
        "Flujo del problema y la solución: enviar un mensaje entre procesos de Erlang costaba 30 a 70 microsegundos y publicar en un servidor grande tardaba de 0,9 a 2,1 segundos; Manifold agrupa los destinatarios por nodo remoto, los reparte por un particionador con hash consistente y trabajadores por núcleo, y reduce el trabajo del proceso emisor.",
        [[("send/2 de 30 a 70 µs por destinatario", "coral"), ("Publicar en un servidor grande: 900 ms a 2,1 s", "coral"), ("Procesos de Erlang son casi de un solo hilo", "coral")],
         [("Manifold agrupa los procesos destino por nodo remoto", "teal"), ("Un particionador por nodo reparte por hash entre trabajadores", "teal"), ("El emisor solo hace una llamada por nodo", "teal")]],
        note="Documentado en «How Discord Scaled Elixir to 5,000,000 Concurrent Users» (2017). Dónde deja de valer: los números son de esa época, con servidores de hasta 30 000 usuarios concurrentes como /r/Overwatch.",
        foot=BLOG, width=960)


def pasivas():
    return flow(
        "Conexiones pasivas y relays para servidores de más de un millón de conectados",
        "Flujo de dos pasos: separar las conexiones activas de las pasivas (alrededor del 90 por ciento en servidores grandes) reduce un 90 por ciento el trabajo de reparto; los relays reparten la entrega entre varios procesos con hasta 15 000 sesiones cada uno y permiten servidores de cientos de miles y luego de más de un millón de conectados.",
        [[("Cada usuario recibía todo de todos sus servidores", "coral"), ("Conexión pasiva hasta que se hace clic en el servidor", "teal"), ("Alrededor del 90 % de las conexiones eran pasivas", "teal")],
         [("Relays: hasta 15 000 sesiones por relay con permisos", "teal"), ("El estado del relay solo lleva los miembros necesarios", "gold"), ("Más de 1 millón de conectados en un servidor de más de 10 millones de miembros", "navy")]],
        note="Documentado en «Maxjourney» (2022). Una reducción de 10 veces del trabajo solo da una ganancia de unas 3 veces del tamaño máximo, porque el trabajo es cuadrático (cálculo del propio post). Dónde deja de valer: es un diseño para el patrón de un servidor enorme y poco activo.",
        foot=BLOG, width=960)


def estructura():
    return grouped_bars(
        "Peor caso al insertar en la lista de miembros de 250 000 elementos",
        "Barras en escala logarítmica con los microsegundos del peor caso: lista ordenada ingenua 170 000, conjunto ordenado de Erlang 27 000, celdas de tamaño fijo 19 000 y estructura de celdas que crecen y se dividen 640.",
        ["Lista ingenua", "ordsets de Erlang", "Celdas fijas", "OrderedSet dinámico"],
        [("Microsegundos, peor caso", [170000, 27000, 19000, 640], "teal")],
        unit="microsegundos (peor caso, escala logarítmica)", log=True, decimals=0, plot_h=250,
        note="Cada barra es la versión de la estructura de datos para la lista de miembros; el peor caso cambia de lugar entre versiones. Mire la última barra: unas 266 veces más rápido que la lista ingenua (cálculo propio: 170 000 entre 640). Dónde deja de valer: la estructura servía hasta 250 000 miembros y luego pasó a Rust.",
        foot="Fuente: «Using Rust to Scale Elixir for 11 Million Concurrent Users», discord.com/blog, 2019.")


def go_rust():
    return flow(
        "Read States: de Go a Rust por los picos de recolección de basura",
        "Flujo: el servicio que guarda qué canales y mensajes se han leído tenía picos de latencia cada dos minutos en Go porque el recolector tenía que recorrer toda la caché LRU; reducir la caché bajaba los picos pero subía la latencia del percentil 99; Rust libera memoria al expulsarla y eliminó los picos.",
        [[("Servicio en la ruta caliente: cada conexión y cada mensaje", "plain"), ("Picos de latencia y CPU cada 2 minutos", "coral"), ("Go fuerza una recolección al menos cada 2 minutos y recorre la caché", "coral")],
         [("Caché más pequeña: menos picos pero más cargas a base de datos", "gold"), ("Reescritura en Rust: sin recolector de basura", "teal"), ("Se libera la memoria al expulsar el estado", "teal")]],
        note="Documentado en «Why Discord is switching from Go to Rust» (2020). El servicio manejaba decenas de millones de estados de lectura por caché y cientos de miles de actualizaciones por segundo. Dónde deja de valer: es un servicio pequeño y autocontenido; el propio post lo elige por eso, y no prueba que Rust sea mejor en general.",
        foot=BLOG, width=960)


def cassandra():
    return flow(
        "Por qué Cassandra se volvió una carga: partición caliente, compactación y recolección",
        "Cadena de problemas: una partición de un canal grande recibe muchas lecturas concurrentes; el nodo se atrasa; como se lee con quórum, todas las consultas a esos nodos sufren; las compactaciones atrasadas encarecen las lecturas; las pausas de la máquina virtual de Java añaden picos; el equipo sacaba nodos de rotación a mano.",
        [[("Partición por canal y ventana de tiempo: un servidor grande es una partición caliente", "coral"), ("Lecturas con quórum: la latencia sube en todos los nodos de esa partición", "coral"), ("Compactaciones atrasadas: lecturas más caras en cascada", "coral")],
         [("«Baile de gossip»: sacar y volver a poner nodos a mano", "coral"), ("Ajustes continuos del recolector de basura de Java", "coral"), ("Guardias frecuentes y operación de alto esfuerzo", "coral")]],
        note="Documentado en «How Discord Stores Trillions of Messages» (2023). Cassandra funcionó bien al principio, con 12 nodos en 2017, y se volvió costosa a 177 nodos. Dónde deja de valer: es la experiencia de Discord con su patrón de acceso; no es un juicio general sobre Cassandra.",
        foot=BLOG, width=960)


def servicios_datos():
    return flow(
        "Servicios de datos en Rust: fusionar peticiones iguales para proteger la base",
        "Flujo: la API llama a un servicio de datos con una consulta gRPC por operación y una clave de enrutado; el balanceo por hash consistente lleva todas las peticiones del mismo canal a la misma instancia; allí un trabajador consulta la base una sola vez y responde a todos los suscriptores.",
        [[("Un aviso a @everyone hace que todos lean el mismo mensaje", "coral"), ("La API llama al servicio de datos (un gRPC por consulta)", "plain"), ("Enrutado por hash consistente del identificador de canal", "teal")],
         [("La primera petición crea un trabajador que consulta la base", "teal"), ("Las demás se suscriben al mismo trabajador", "teal"), ("La base recibe una consulta en vez de miles", "navy")]],
        note="Documentado en «How Discord Stores Trillions of Messages» (2023). Los servicios no contienen lógica de negocio. Dónde deja de valer: reducen la frecuencia de las particiones calientes pero no la eliminan, según el propio post.",
        foot=BLOG, width=960)


def migracion():
    return flow(
        "Migrar billones de mensajes sin parar el servicio",
        "Flujo de la migración: aprovisionar ScyllaDB con discos locales y réplica en disco persistente; escribir en ambas bases; reescribir el migrador en Rust para pasar de tres meses a nueve días con picos de 3,2 millones de mensajes por segundo; compactar los últimos rangos con lápidas; validar con lecturas a las dos bases y cambiar la base primaria en mayo de 2022.",
        [[("Nuevo clúster ScyllaDB con SSD locales y RAID a disco persistente", "plain"), ("Escrituras dobles a Cassandra y ScyllaDB", "teal"), ("Migrador de Spark estimado en tres meses", "gold")],
         [("Migrador en Rust: nueve días y hasta 3,2 millones de mensajes por segundo", "teal"), ("Se atasca en 99,9999 %: rangos con lápidas sin compactar", "coral"), ("Validación con lecturas a ambas bases y cambio en mayo de 2022", "navy")]],
        note="Documentado en «How Discord Stores Trillions of Messages» (2023). Dónde deja de valer: incluye anécdotas del propio equipo; el valor está en el patrón (doble escritura, validación con tráfico real, un migrador a la medida).",
        foot=BLOG, width=960)


def voz():
    return flow(
        "Voz en Discord: cliente-servidor en vez de entre pares",
        "Flujo de la voz: toda la comunicación pasa por servidores de medios, lo que oculta las direcciones IP y permite moderar; el cliente inicia la llamada al entrar al canal con una señal mínima de unos 1 000 bytes; en las aplicaciones nativas se usa un motor C++ propio sobre WebRTC con cifrado Salsa20 y sin enviar audio en silencio.",
        [[("Toda conexión multiparte pasa por servidores de medios", "teal"), ("No se filtra la dirección IP de los participantes", "teal"), ("El cliente inicia: entrar a un canal abre la comunicación", "teal")],
         [("Señal de unión mínima: unos 1 000 bytes", "gold"), ("Motor nativo en C++ sobre WebRTC; el navegador usa el suyo", "gold"), ("Sin audio en silencio: ahorra ancho de banda y CPU", "gold")]],
        note="Documentado en «How Discord Handles Two and Half Million Concurrent Voice Users using WebRTC» (septiembre de 2018). La señalización está escrita en Elixir. Dónde deja de valer: es el diseño de 2018; no se sabe cuántos servidores de medios hay hoy.",
        foot=BLOG, width=960)


def linea():
    return years(timeline(
        "Discord de 2012 a 2026: empresa, producto e ingeniería",
        "Línea de tiempo con tres carriles: empresa (estudio Phoenix Guild en 2012, Discord en mayo de 2015, nuevo consejero delegado en abril de 2025), producto (overlay en 2016, Nitro en 2017, Go Live y Boosts en 2019, Activities en 2023, Social SDK en 2025) y almacén de mensajes (MongoDB hasta 2015, Cassandra de 2015 a 2022 y ScyllaDB desde mayo de 2022).",
        [("Empresa", [(2012.3, 2015.4, "Estudio de juegos", "grey"), (2015.4, 2025.3, "Discord con sus fundadores", "teal"), (2025.3, 2026, "", "navy")]),
         ("Mensajes", [(2015.0, 2015.9, "", "gold"), (2015.9, 2022.4, "Cassandra", "navy"), (2022.4, 2026, "ScyllaDB", "teal")]),
         ("Producto", [(2017.1, 2017.3, "", "coral"), (2019.5, 2019.7, "", "coral"), (2023.3, 2023.5, "", "coral"), (2025.3, 2025.5, "", "coral")])],
        unit="año", events=[(2015.4, "Discord"), (2017.1, "Nitro"), (2019.5, "Go Live"), (2025.3, "SDK")],
        t_max=2027, ticks=[2012, 2015, 2018, 2021, 2024, 2027], lane_h=46,
        note="Hechos con fuente: línea de tiempo oficial de Discord (2012 a 2025) y los posts de 2017 y 2023 sobre mensajes. Dónde deja de valer: el cambio de MongoDB a Cassandra se sitúa en 2015-2016 y los segmentos de producto son marcadores de lanzamiento, no periodos.",
        foot="Fuentes: discord.com/company y blog de ingeniería de Discord."))


def especiales():
    return case_cards(
        "Casos especiales documentados y cómo se resuelven",
        "Cinco tarjetas: servidor de decenas de miles de conectados, aviso a todos los miembros, servidor de más de un millón de conectados, partición caliente en la base de mensajes y servicio de lectura con picos cada dos minutos; cada una con su mecanismo y veredicto.",
        [("Servidor de 30 000 conectados en 2017", "Manifold reparte el envío de mensajes entre nodos", "Los procesos se atrasaban y hubo que apagar funciones a mano.", "teal"),
         ("Aviso a @everyone", "Servicios de datos con fusión de peticiones y hash por canal", "Evita que miles de lecturas iguales golpeen una partición.", "teal"),
         ("Más de un millón de conectados", "Conexiones pasivas y relays", "El trabajo es cuadrático: 10 veces menos solo da 3 veces más tamaño.", "gold"),
         ("Partición caliente en Cassandra", "ScyllaDB y servicios de datos", "Los hot partitions siguen siendo posibles; se reduce su frecuencia.", "gold"),
         ("Picos cada dos minutos por la recolección de Go", "Reescritura en Rust", "Un servicio pequeño y autocontenido; no se generaliza a todo.", "teal")],
        note="Cada tarjeta enlaza un hecho citado con el mecanismo. Color: coral falla, teal se sostiene, gold depende. Dónde deja de valer: son casos documentados por Discord, que cuenta sus propias soluciones.",
        foot=BLOG)


def alternativas():
    return case_cards(
        "Alternativas que Discord no tomó o sustituyó, como análisis del curso",
        "Cuatro tarjetas: seguir con MongoDB, fragmentar MongoDB, quedarse con Cassandra y pasar de Go a Rust; cada una con lo que Discord documenta.",
        [("Seguir con MongoDB para los mensajes", "Cambiar a Cassandra en 2015-2016", "Documentado: a 100 millones de mensajes los datos y el índice dejaron de caber en memoria.", "teal"),
         ("Fragmentar MongoDB", "No se hizo", "Documentado: «complicado de usar y no conocido por su estabilidad»; se había previsto una ruta de migración desde el principio.", "gold"),
         ("Quedarse con Cassandra", "ScyllaDB en 2022", "Documentado: guardias frecuentes, particiones calientes y recolección de basura de Java.", "teal"),
         ("Mantener el servicio en Go", "Rust para Read States", "Documentado: picos de latencia por la recolección; el servicio se eligió por ser pequeño.", "gold")],
        note="Rótulo: documentado por el propio Discord, que explica sus razones en los posts de 2017, 2020 y 2023. El patrón es repetido: se construye rápido con una ruta a algo más robusto. Dónde deja de valer: no se publican las alternativas evaluadas y descartadas con sus costes numéricos.",
        foot=BLOG)


def hardware():
    return layer_stack(
        "Hardware y software que Discord hace público",
        "Pila: ScyllaDB sobre discos SSD locales con RAID a discos persistentes; servicios de datos en Rust; Elixir sobre la máquina virtual de Erlang para sesiones, servidores y señalización; API en Python; clientes con C++, WebRTC, React y React Native; servidores de voz.",
        [("Hardware", "SSD locales con RAID hacia discos persistentes para ScyllaDB; el proveedor de nube no se nombra", "grey"),
         ("Almacenes", "ScyllaDB (antes Cassandra y MongoDB); nodos de 9 TB", "gold"),
         ("Servicios", "Rust con Tokio para los servicios de datos y servicios pequeños", "plain"),
         ("Tiempo real", "Elixir en la máquina virtual de Erlang; Manifold y OrderedSet (con Rust)", "plain"),
         ("Clientes y voz", "C++ sobre WebRTC en las apps instaladas; React y React Native", "plain")],
        [("Documentado en posts de 2017 a 2023", "teal"), ("No se sabe: proveedor de nube, regiones y cifras de flota", "grey")],
        "El post de 2023 describe la topología de discos (SSD locales con RAID a discos persistentes) sin nombrar al proveedor. Dónde deja de valer: la pila es de 2017 a 2023; el uso de Elixir y Rust descrito entonces puede haber cambiado.",
        BLOG)


def pruebas_fallo():
    return case_cards(
        "Temas a prueba de fallos que Discord documenta",
        "Cuatro mecanismos con veredicto: conexión iniciada por el cliente para reconectar a otro servidor de voz, escrituras dobles y validación durante migraciones, servicios de datos que limitan la concurrencia en particiones calientes y degradación de funciones en servidores grandes.",
        [("Cae un servidor de voz", "El cliente se reconecta a otro servidor", "La comunicación la inicia siempre el cliente; reduce la complejidad del servidor.", "teal"),
         ("Una migración puede salir mal", "Escrituras dobles y validación con tráfico real", "Se lee de ambas bases y se comparan resultados antes de cambiar.", "teal"),
         ("Una partición caliente", "Servicio de datos con concurrencia controlada", "Reduce la frecuencia, no elimina el riesgo.", "gold"),
         ("Un servidor muy grande se atrasa", "Apagar funciones que generan mensajes (2017)", "Fue una medida manual que motivó Manifold.", "coral")],
        note="Documentado en los posts de voz (2018), mensajes (2023) y Elixir (2017). Dónde deja de valer: se citan mecanismos de épocas distintas, no un plan de continuidad actual.",
        foot=BLOG)


FIGURES = {
    "discord-contexto.svg": contexto,
    "discord-mensajes-por-dia.svg": mensajes,
    "discord-nodos-de-la-base-de-mensajes.svg": nodos,
    "discord-latencia-de-mensajes.svg": latencias,
    "discord-actores-e-incentivos.svg": actores,
    "discord-recorridos-de-usuario.svg": recorridos,
    "discord-esquema-del-negocio.svg": negocio,
    "discord-capas.svg": capas,
    "discord-secuencia-de-un-mensaje.svg": secuencia,
    "discord-trabajo-cuadratico.svg": cuadratico,
    "discord-manifold.svg": manifold,
    "discord-conexiones-pasivas-y-relays.svg": pasivas,
    "discord-lista-de-miembros.svg": estructura,
    "discord-de-go-a-rust.svg": go_rust,
    "discord-problemas-de-cassandra.svg": cassandra,
    "discord-servicios-de-datos.svg": servicios_datos,
    "discord-migracion-de-mensajes.svg": migracion,
    "discord-voz.svg": voz,
    "discord-linea-de-tiempo.svg": linea,
    "discord-casos-especiales.svg": especiales,
    "discord-alternativas.svg": alternativas,
    "discord-hardware-y-software.svg": hardware,
    "discord-a-prueba-de-fallos.svg": pruebas_fallo,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys

    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
