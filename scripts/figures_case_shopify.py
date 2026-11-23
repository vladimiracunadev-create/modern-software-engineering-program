"""Figuras del caso de estudio Shopify (casos/exito/shopify.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Las cifras salen del 10-K de Shopify del año 2025 (SEC) y del blog de ingeniería de Shopify; cada pie
de figura nombra su fuente. Ninguna figura repite una tabla del caso.
"""
from __future__ import annotations

from case_diagrams import canvas, finish, lane_steps, sequence, years
from case_fig_helpers import hub, kanban, layer_stack
from figure_cases import case_cards
from figure_kit import grouped_bars, line_chart, stacked_bars, timeline
from figures_part45_a import flow

TENK = "Fuente: 10-K de Shopify Inc. del año terminado el 31 de diciembre de 2025 (SEC), consulta 2026-11-23."
BLOG = "Fuente: blog de ingeniería de Shopify (shopify.engineering), consulta 2026-11-23. Esquema del autor."


def contexto():
    return hub(
        "Shopify entre el comerciante, el comprador y el resto del comercio",
        "Diagrama de contexto: el comerciante monta y administra su tienda; el comprador paga en línea, en tienda física o en redes sociales; Shopify Payments y Shop Pay procesan el pago; los desarrolladores venden aplicaciones y temas; los socios de envío, las redes de tarjetas y los canales externos completan el ecosistema; Google Cloud aloja la mayor parte de la plataforma.",
        ("Shopify: plataforma de comercio de múltiples inquilinos", "navy"),
        [("Comerciante: de un emprendedor solo a una marca global", "teal", "administra"),
         ("Comprador: web, tienda física, redes sociales, aplicación Shop", "teal", "compra"),
         ("Shopify Payments y Shop Pay: cobro y pago acelerado", "gold", "procesa"),
         ("Desarrolladores y socios: aplicaciones, temas, agencias", "gold", "extienden"),
         ("Redes de tarjetas, bancos y procesadores", "plain", "liquidan"),
         ("Transportistas y proveedores de envío", "plain", "entregan"),
         ("Google Cloud: aloja la mayor parte de las operaciones", "plain", "aloja"),
         ("Reguladores: pagos, privacidad, impuestos", "coral", "exigen")],
        "Documentado en el 10-K de 2025: plataforma multi-inquilino en la nube, pagos integrados con Shopify Payments, comerciantes en más de 175 países y uso de Google Cloud para la mayor parte de las operaciones. Dónde deja de valer: no cuantifica la dependencia de cada socio.",
        TENK)


def ingresos():
    return years(stacked_bars(
        "Ingresos de Shopify por tipo, 2023 a 2025",
        "Barras apiladas en millones de dólares: soluciones de suscripción 1 837, 2 350 y 2 752 millones, y soluciones para comerciantes 5 223, 6 530 y 8 804 millones; el total pasa de 7 060 a 8 880 y a 11 556 millones.",
        ["2023", "2024", "2025"],
        [("Soluciones de suscripción", [1837, 2350, 2752], "teal"), ("Soluciones para comerciantes", [5223, 6530, 8804], "navy")],
        unit="millones de USD", decimals=0, plot_h=260,
        note="Las soluciones para comerciantes (sobre todo comisiones de pago) pesan 76 % del ingreso de 2025 frente a 74 % en 2023. Dónde deja de valer: el ingreso de pagos arrastra un coste de ingresos alto (ver el reparto del ingreso).",
        foot=TENK))


def gmv():
    return years(grouped_bars(
        "Volumen bruto de mercancías (GMV) que fluye por la plataforma",
        "Barras con 235,9 miles de millones de dólares en 2023, 292,3 en 2024 y 378,4 en 2025; el crecimiento anual es 24 por ciento y 29 por ciento.",
        ["2023", "2024", "2025"],
        [("GMV (miles de millones de USD)", [235.9, 292.3, 378.4], "teal")],
        unit="miles de millones de USD", decimals=1, plot_h=240,
        note="El GMV es el valor total de los pedidos facilitados, neto de reembolsos y con envío e impuestos. Cálculo propio: el ingreso de Shopify equivale a 2,99 % del GMV en 2023 y 3,05 % en 2025 (7 060 y 11 556 millones sobre 235,9 y 378,4 mil millones). Dónde deja de valer: Shopify no es dueño de ese dinero; es el volumen de sus comerciantes.",
        foot=TENK))


def reparto():
    return grouped_bars(
        "Cómo se reparte cada dólar de ingreso en 2025",
        "Barras horizontales como porcentaje del ingreso de 11 556 millones: coste de ingresos 52 por ciento, ventas y marketing 14 por ciento, investigación y desarrollo 13 por ciento, administración 4 por ciento, pérdidas por transacciones y préstamos 4 por ciento y utilidad neta 11 por ciento.",
        ["Coste de ingresos", "Ventas y marketing", "Investigación y desarrollo", "Administración general", "Pérdidas por transacciones y préstamos", "Utilidad neta"],
        [("Porcentaje del ingreso 2025", [51.9, 14.4, 13.3, 4.1, 3.6, 10.7], "coral")],
        unit="% del ingreso", horizontal=True, decimals=1, plot_h=300,
        note="Cálculo propio sobre el 10-K: 6 001; 1 663; 1 536; 471; 417 y 1 231 millones sobre 11 556. Las partidas no suman 100 % porque hay ingresos y gastos no operativos y impuestos. Mire la primera barra: más de la mitad del ingreso es coste de procesar pagos y otras soluciones. Dónde deja de valer: el coste de ingresos de pagos incluye comisiones de interbancarias que no son de Shopify.",
        foot=TENK)


def utilidad():
    return years(grouped_bars(
        "Utilidad neta de Shopify, 2023 a 2025",
        "Barras con utilidad neta de 132 millones en 2023, 2 019 millones en 2024 y 1 231 millones en 2025; 2023 incluye un deterioro de 1 340 millones por la venta del negocio de logística.",
        ["2023", "2024", "2025"],
        [("Utilidad neta (millones de USD)", [132, 2019, 1231], "navy")],
        unit="millones de USD", decimals=0, plot_h=230,
        note="Mire 2023: un deterioro de 1 340 millones por la venta de los negocios de logística comprimió la utilidad; en 2024 y 2025 hay además ganancias o pérdidas por inversiones que el 10-K lista aparte. Dónde deja de valer: la utilidad neta mezcla operación y resultados de inversiones.",
        foot=TENK))


def regiones():
    return grouped_bars(
        "Dónde están los comerciantes de Shopify (31 de diciembre de 2025)",
        "Barras horizontales: 44 por ciento en Estados Unidos, 31 por ciento en Europa, Oriente Medio y África, 16 por ciento en Asia Pacífico, Australia y China, 5 por ciento en Canadá y 5 por ciento en América Latina.",
        ["Estados Unidos", "Europa, Oriente Medio y África", "Asia Pacífico, Australia y China", "Canadá", "América Latina"],
        [("% de comerciantes", [44, 31, 16, 5, 5], "teal")],
        unit="% de comerciantes", horizontal=True, decimals=0, plot_h=240,
        note="El 10-K habla de «millones de comerciantes» en más de 175 países y no da el número exacto. Dónde deja de valer: es el reparto de comerciantes, no de ventas; las regiones con más comerciantes no son necesariamente las de más GMV.",
        foot=TENK)


def actores():
    return hub(
        "Quién obtiene qué en el ecosistema de Shopify",
        "Diagrama de incentivos: el comerciante obtiene una tienda lista y pagos integrados; el comprador un pago rápido y recordado; el desarrollador un canal de distribución; el socio de pagos volumen; Shopify una comisión sobre el GMV y una suscripción.",
        ("Shopify: cobra suscripción y una parte de cada venta procesada", "navy"),
        [("Comerciante: empieza rápido y delega infraestructura", "teal", "paga plan y comisión"),
         ("Comprador: pago de un clic con Shop Pay", "teal", "paga"),
         ("Desarrollador de aplicaciones: vende en la App Store", "gold", "paga comisión"),
         ("Empresa grande (Plus): personaliza y pide soporte", "gold", "paga más"),
         ("Banco o red de pagos: gana por volumen", "plain", "liquida"),
         ("Competidores: otras plataformas y desarrollos propios", "grey", "disputan"),
         ("Regulador: impuestos, privacidad y pagos", "coral", "limita"),
         ("Empleados: compensación flexible (Flex Comp)", "plain", "construyen")],
        "Análisis propio sobre hechos del 10-K: la mayoría de comerciantes usa planes básicos, pero la mayor parte del GMV viene de comerciantes Plus y de grandes empresas; el ingreso crece con el GMV por la comisión de pagos. Dónde deja de valer: Shopify no publica el reparto exacto del ingreso por plan.",
        TENK)


def recorridos():
    f = canvas("Cuatro recorridos en Shopify y su caso límite",
               "Cuatro filas de pasos: un comerciante nuevo, un comprador en el pago, un desarrollador de aplicaciones y una marca grande con una venta relámpago; cada fila termina en un caso límite.")
    y = 56.0
    y = lane_steps(f, y, "Comerciante nuevo", [("Crea la tienda y elige tema", "teal"), ("Carga productos y dominio", "teal"), ("Activa Shopify Payments", "teal"), ("Verificación de identidad o disputa de cobro", "coral")])
    y = lane_steps(f, y, "Comprador", [("Entra a la tienda desde un enlace", "gold"), ("Agrega al carrito", "gold"), ("Paga con Shop Pay o tarjeta", "gold"), ("Último artículo disputado por dos compradores", "coral")])
    y = lane_steps(f, y, "Desarrollador", [("Crea una aplicación con la API", "navy"), ("Recibe webhooks de eventos", "navy"), ("Llama a la API con límites", "navy"), ("Entrega repetida por reintentos del webhook", "coral")])
    y = lane_steps(f, y, "Marca grande", [("Prepara la venta con antelación", "plain"), ("Pruebas de carga y colas", "plain"), ("Lanza la venta relámpago", "plain"), ("Picos que usan 20 % de la capacidad", "coral")])
    return finish(f, y + 4, "Cada fila se lee de izquierda a derecha y la caja coral es el borde. Los casos límite del comprador y de la marca grande salen de los posts sobre reservas de inventario y la BFCM de 2021; el del desarrollador, del documento de webhooks de 2012. Dónde deja de valer: no mide frecuencia de cada borde.", "Esquema del autor sobre el blog de ingeniería de Shopify y su 10-K.")


def negocio():
    return flow(
        "Cómo entra y sale el dinero en Shopify",
        "Flujo del negocio: el comerciante paga una suscripción mensual y una comisión por cada venta que procesa Shopify Payments; esos ingresos pagan el coste de procesar, las ventas, la ingeniería y las pérdidas por fraude y préstamos; el GMV de los comerciantes es el motor.",
        [[("Comerciante: suscripción (24 % del ingreso en 2025)", "teal"), ("Ventas: GMV de 378 mil millones de USD", "teal"), ("Shopify Payments: comisión sobre cada pago", "gold"), ("Soluciones para comerciantes: 76 % del ingreso", "navy")],
         [("Coste de ingresos: 52 % del ingreso", "coral"), ("Ventas y marketing: 14 %", "coral"), ("I+D: 13 %", "coral"), ("Utilidad neta: 11 %", "teal")]],
        note="Documentado en el 10-K de 2025. Cálculo propio: 2 752 de 11 556 millones es suscripción (23,8 %). Inferido: la lectura de que el GMV es el motor, porque el ingreso de pagos es proporcional a él.",
        foot=TENK, width=960)


def capas():
    return layer_stack(
        "Capas de Shopify que su ingeniería describió, de la tienda a los datos",
        "Pila de capas: tiendas y aplicaciones; balanceadores con Sorting Hat; pods con servidores de aplicación; monolito modular en Ruby on Rails más cientos de aplicaciones de dominio; almacenes MySQL, Redis y Memcached por pod; Google Cloud con Kubernetes.",
        [("Clientes", "Tiendas, administración, aplicación Shop, aplicaciones de terceros y webhooks", "teal"),
         ("Balanceo", "Nginx, Lua y OpenResty; Sorting Hat asigna cada petición a un pod", "plain"),
         ("Aplicación", "Monolito de Rails modular más cientos de aplicaciones de dominio (envíos, identidad, App Store)", "plain"),
         ("Pods", "Cada pod: su fragmento MySQL, Redis y Memcached; solo se habla con un pod a la vez", "gold"),
         ("Datos analíticos", "Captura de cambios con Kafka Connect y Debezium hacia el lago de datos", "plain"),
         ("Infraestructura", "Google Cloud; Docker y Kubernetes para crear pods", "navy")],
        [("Documentado en posts de 2018 a 2026", "teal"), ("No se sabe: número actual de pods ni su distribución", "grey"), ("Inferido: cada pod nuevo repite el mismo molde", "grey")],
        "Documentado en los posts sobre pods, equilibrio de fragmentos, el stack, el monolito modular y la captura de cambios, y en el 10-K de 2025 (Google Cloud). Dónde deja de valer: los posts van de 2018 a 2026 y la arquitectura ha cambiado; el de 2018 hablaba de más de cien pods.",
        BLOG)


def sorting_hat():
    return sequence(
        "De la URL de una tienda al pod que la sirve",
        "Secuencia de una petición: el balanceador con Sorting Hat consulta la tabla de rutas, añade una cabecera con el pod, la aplicación usa esa cabecera para hablar solo con los almacenes de ese pod y devuelve la respuesta.",
        ["Comprador", "Balanceador + Sorting Hat", "Servidor de aplicación", "Almacenes del pod"],
        [(0, 1, "pide coolcucumbers.com", ""), (1, 1, "busca la tienda en la tabla de rutas", ""),
         (1, 2, "reenvía con la cabecera del pod 42", ""), (2, 3, "consulta solo MySQL, Redis y Memcached del pod 42", ""),
         (3, 2, "devuelve los datos de la tienda", "ret"), (2, 0, "respuesta HTML o JSON", "ret")],
        "Documentado en el post de pods (2018) y en el de equilibrio de fragmentos (2021, ejemplo de «Pod 42»). Los servidores de aplicación son compartidos y la capacidad es de toda la plataforma, pero cada petición toca un solo pod. Dónde deja de valer: omite caché de borde, autenticación y el camino de pago.",
        BLOG)


def pod():
    return hub(
        "Un pod: una instancia aislada de Shopify",
        "Esquema de un pod: un fragmento MySQL, Redis y Memcached propios con un subconjunto de tiendas; recursos compartidos (trabajadores de trabajos, servidores de aplicación y balanceadores) que solo hablan con un pod a la vez; un par de centros de datos activo y de recuperación.",
        ("Pod: subconjunto de tiendas y sus almacenes", "navy"),
        [("Fragmento MySQL con los datos de sus tiendas", "teal", "guarda"),
         ("Redis y Memcached propios del pod", "teal", "aceleran"),
         ("Trabajadores y servidores compartidos, un pod por vez", "gold", "atienden"),
         ("Par de centros de datos: activo y de recuperación", "plain", "respaldan"),
         ("Pod Mover: mueve un pod en un minuto sin perder peticiones", "plain", "evacúa"),
         ("Sorting Hat: elige el pod de cada petición", "plain", "enruta")],
        "Documentado en el post de 2018: ninguna acción cruza pods, de modo que atender una petición solo exige un pod activo y añadir un pod no afecta a los demás. Dónde deja de valer: los recursos compartidos (balanceadores) siguen siendo un punto común.",
        BLOG)


def evolucion():
    return flow(
        "Cómo creció la arquitectura: del monolito a los pods",
        "Dos filas de etapas: 2004 aplicación Rails con una sola base MySQL; 2014 y 2015 fragmentación porque ya no se podía comprar un servidor mayor; una caída de un Redis compartido tumba la plataforma; 2016 pods aislados; después más de cien pods y movimientos de tiendas entre fragmentos.",
        [[("2004: aplicación Rails y una base MySQL", "plain"), ("2014-2015: fragmentación en decenas de bases", "gold"), ("Un Redis compartido: «Redismageddon» tumba todo", "coral"), ("2016: pods aislados con Sorting Hat", "teal")],
         [("Pod Mover: recuperación por pod en un minuto", "teal"), ("Más de cien pods (2018)", "teal"), ("Equilibrio de fragmentos en línea (2021)", "teal"), ("Vitess en la aplicación Shop (2024)", "gold")]],
        note="Documentado en el post de pods (2018), el del stack (2018), el de equilibrio de fragmentos (2021) y el de Vitess en Shop (2024). Lección documentada: evitar recursos compartidos por toda la plataforma. Dónde deja de valer: las fechas de 2014 y 2015 difieren entre posts (el stack dice 2014; el de pods, 2015).",
        foot=BLOG, width=960)


def equilibrio():
    return flow(
        "Mover una tienda de un fragmento a otro sin parar el servicio",
        "Flujo del equilibrio de fragmentos: una tienda intensiva comparte fragmento con otras, se detecta el desequilibrio, se copia la tienda al fragmento de destino mientras sigue sirviendo, se verifica y se cambia la ruta, con tiempo de inactividad casi nulo.",
        [[("Tienda intensiva en un fragmento sobrecargado", "coral"), ("Se elige un fragmento de destino con holgura", "gold"), ("Copia en línea de los datos de la tienda", "gold")],
         [("Verificación y cambio de la tabla de rutas", "teal"), ("Tienda en el nuevo pod, sin caída visible", "teal"), ("Fragmentos equilibrados: menos riesgo de fallo", "teal")]],
        note="Documentado en el post «Shard Balancing» (2021): el objetivo es migrar tiendas entre fragmentos en línea con tiempo de inactividad virtualmente nulo. Dónde deja de valer: el detalle de la verificación y del corte final está en el post y aquí se resume.",
        foot=BLOG, width=960)


def monolito():
    return flow(
        "Monolito modular: componentes con dueño y contratos",
        "Cuatro cajas: un monolito de más de 2,8 millones de líneas de Ruby y 500 000 confirmaciones; un equipo investiga hacer componentes con contratos; los componentes tienen dueño y excepciones asignadas; el aprendizaje principal es que el cambio es un problema de personas.",
        [[("Monolito de Rails: más de 2,8 millones de líneas y 500 000 commits", "plain"), ("Meta: que cada desarrollador sienta que trabaja en una app pequeña", "gold"), ("Componentes con dueño, contratos y excepciones triadas por componente", "teal"), ("Aprendizaje: el cambio de arquitectura es un problema de personas", "navy")]],
        note="Documentado en «Under Deconstruction: The State of Shopify's Monolith» (septiembre de 2020). El post dice que los detalles cambiaron casi todos pero se mantienen las ideas originales. Dónde deja de valer: es el estado de 2020; el CTO describe en 2022 un patrón de arquitectura distinto para partes del monolito.",
        foot=BLOG, width=960)


def bfcm():
    return hub(
        "Viernes Negro y Cyber Monday de 2021: lo que Shopify midió",
        "Esquema de cifras: más de 32 millones de peticiones por minuto en los servidores de aplicación y más de 34 millones en los balanceadores; 145 millones de correos; 42 mil millones de llamadas de API y 13 mil millones de webhooks; más de 11 millones de consultas por segundo en MySQL; una venta relámpago consumió más del 20 por ciento de la capacidad total.",
        ("BFCM 2021: pico de cuatro días", "navy"),
        [("Servidores de aplicación: más de 32 M de peticiones por minuto", "teal", "pico"),
         ("Balanceadores: más de 34 M de peticiones por minuto", "teal", "pico"),
         ("MySQL: más de 11 M de consultas por segundo", "gold", "flota"),
         ("API: 42 mil M de llamadas y 13 mil M de webhooks", "gold", "en 4 días"),
         ("Correos: casi 145 M", "plain", "enviados"),
         ("Una venta relámpago usó más del 20 % de la capacidad", "coral", "caso límite")],
        "Documentado en el post del CTO de enero de 2022. Cálculo propio: 32 millones de peticiones por minuto son unas 533 000 por segundo. Dónde deja de valer: son cifras de un fin de semana de 2021; el récord de 2025 de 5,1 millones de dólares de ventas por minuto se cita en otro post.",
        BLOG)


def reservas():
    return flow(
        "Reservas de inventario: de Redis a MySQL con una fila por unidad",
        "Dos filas: con Redis una clave de cantidad por artículo se descontaba y reponía; las reservas y el libro de inventario vivían en dos sistemas; con MySQL se reserva una fila por unidad con SKIP LOCKED y claves compuestas, dentro de la misma base transaccional.",
        [[("Antes: una clave de cantidad por artículo en Redis", "plain"), ("DECR al reservar, INCR al liberar", "plain"), ("Dos sistemas: reservas y libro de inventario", "coral")],
         [("Después: una fila por unidad en MySQL 8", "teal"), ("SKIP LOCKED evita esperar por filas bloqueadas", "teal"), ("Garantías ACID entre reservas y libro", "teal")]],
        note="Documentado en «We replaced Redis with MySQL for inventory reservations» (mayo de 2026): un solo registro con una columna de cantidad no soportaba la contención. Dónde deja de valer: el propio post dice que el cuello de botella real no era el que medían; las cifras de rendimiento no se reproducen aquí.",
        foot=BLOG, width=960)


def pagos():
    return kanban(
        "Principios de pagos resilientes que el equipo de Shopify publicó",
        "Cuatro columnas con diez consejos agrupados: límites de espera, protección contra fallos, exactamente una vez y operación.",
        [("Esperar poco", "gold", ["Timeouts bajos: un segundo para abrir y cinco para leer como punto de partida", "Monitorear para ajustar los valores"]),
         ("Contener fallos", "coral", ["Circuit breakers: dejar de llamar a quien falla", "Entender capacidad y colas"]),
         ("Una sola vez", "teal", ["Claves de idempotencia en pagos y reembolsos", "Un id de correlación para encontrar todos los logs"]),
         ("Operar", "navy", ["Ser consistente en la forma de hacer las cosas", "Practicar la respuesta a incidentes y organizar el equipo"])],
        "Documentado en «10 Tips for Building Resilient Payment Systems» (julio de 2022): los títulos de los diez consejos son timeouts, circuit breakers, capacidad, monitoreo, ejecución, idempotencia, consistencia, incorporación, respuesta y organización. Dónde deja de valer: son recomendaciones de un autor, no una política oficial.",
        BLOG, box_h=96)


def cdc():
    return flow(
        "De consultas periódicas a un registro de cambios con Kafka",
        "Flujo de captura de cambios: antes una herramienta consultaba las bases para sacar los cambios; ahora Debezium y Kafka Connect leen el registro de cambios de MySQL, lo publican como eventos y aíslan a los consumidores de la fragmentación de origen.",
        [[("Antes: herramienta basada en consultas (Longboat)", "plain"), ("Limitaciones: lotes lentos y poco semiestructurado", "coral"), ("Presión por analítica casi en tiempo real para comerciantes", "gold")],
         [("Ahora: registro de cambios inmutable de solo añadir", "teal"), ("Debezium y Kafka Connect publican eventos", "teal"), ("Un tema por tabla lógica; el consumidor no ve fragmentos", "teal")]],
        note="Documentado en «Capturing Every Change From Shopify's Sharded Monolith» (marzo de 2021). Dónde deja de valer: el post es de 2021 y describe una migración en curso, no su resultado final.",
        foot=BLOG, width=960)


def especiales():
    return case_cards(
        "Casos especiales documentados y cómo se resuelven",
        "Cinco tarjetas: Redis compartido que tumba todo, venta relámpago que consume una quinta parte de la capacidad, dos compradores del último artículo, webhook duplicado y tienda que desequilibra un fragmento; cada una con su mecanismo y veredicto.",
        [("Un Redis compartido por todas las tiendas", "Caída global («Redismageddon»); la respuesta fue aislar cada pod", "Un recurso compartido por toda la plataforma convierte un fallo local en global.", "teal"),
         ("Venta relámpago con picos impredecibles", "Una sola venta llegó a usar más del 20 % de la capacidad en BFCM 2021", "Un cliente puede consumir una fracción enorme: hacen falta límites y pruebas de carga previas.", "gold"),
         ("Dos compradores del último artículo", "Reserva breve durante el pago y descuento definitivo al cobrar", "Se prefiere correctitud: ni vender de más ni rechazar de menos.", "teal"),
         ("Un webhook cuya entrega falla", "Espera de 10 segundos y reintentos durante 48 horas (2012)", "Con reintentos puede haber duplicados: el consumidor debe tolerarlos (inferido).", "gold"),
         ("Una tienda intensiva en un fragmento", "Equilibrio en línea moviendo tiendas entre fragmentos", "El reparto inicial se desequilibra con el tiempo y hay que corregirlo sin parar.", "teal")],
        note="Cada tarjeta enlaza un hecho citado con el mecanismo. Color: coral falla, teal se sostiene, gold depende. Dónde deja de valer: son casos documentados, no exhaustivos.",
        foot=BLOG)


def linea():
    return years(timeline(
        "Shopify de 2004 a 2026: empresa, arquitectura y escala",
        "Línea de tiempo con tres carriles: empresa (constitución en 2004, oferta pública en 2015), arquitectura (fragmentación hacia 2014-2015, pods desde 2016, monolito modular 2017-2020) y escala (600 mil comerciantes y 80 mil peticiones por segundo en 2018, GMV de 378 mil millones en 2025).",
        [("Empresa", [(2004, 2015.4, "Empresa privada", "grey"), (2015.4, 2026, "Cotizada (IPO el 27 de mayo de 2015)", "teal")]),
         ("Arquitectura", [(2004, 2014, "Una base", "grey"), (2014, 2016, "Shards", "gold"), (2016, 2026, "Pods y monolito modular", "navy")]),
         ("Escala", [(2018, 2019, "", "coral"), (2021.9, 2022, "", "coral"), (2025.9, 2026, "", "coral")])],
        unit="año", events=[(2004.7, "constitución"), (2015.4, "IPO"), (2018, "600 mil tiendas"), (2021.9, "BFCM 2021")],
        t_max=2027, ticks=[2004, 2008, 2012, 2016, 2020, 2024, 2027], lane_h=46,
        note="Hechos con fuente: constitución el 28 de septiembre de 2004 e IPO el 27 de mayo de 2015 (10-K); fragmentación y pods (posts de 2018); BFCM 2021 (post de 2022); GMV 2025 (10-K). Dónde deja de valer: los marcadores rojos de la última línea son hitos de escala, no un periodo.",
        foot="Fuentes: 10-K de 2025 y blog de ingeniería de Shopify."))


def alternativas():
    return case_cards(
        "Alternativas que Shopify no tomó o sustituyó, como análisis del curso",
        "Cuatro tarjetas: reescribir el monolito en microservicios, seguir comprando servidores mayores, compartir un Redis para todas las tiendas y mantener Redis para reservas; cada una con lo que Shopify hizo.",
        [("Reescribir en microservicios", "Monolito modular y aplicaciones de dominio", "Documentado: «no son microservicios»; la aplicación central sigue siendo un monolito Rails.", "teal"),
         ("Comprar un servidor de base de datos mayor", "Fragmentar desde 2014-2015", "Documentado: ya no era posible; la fragmentación costó resiliencia.", "gold"),
         ("Un Redis para toda la plataforma", "Pods con Redis propio", "Documentado: el Redis compartido causó una caída global.", "teal"),
         ("Seguir con Redis para las reservas", "MySQL con una fila por unidad", "Documentado en 2026: unificar el sistema de registro con ACID.", "gold")],
        note="Rótulo: análisis propio. El caso muestra que la alternativa «descartada» más importante, los microservicios, se descartó con razones explícitas del propio Shopify. Dónde deja de valer: no hay documento con la evaluación completa de cada alternativa.",
        foot=BLOG)


def hardware():
    return layer_stack(
        "Hardware y software que Shopify hace público",
        "Pila: sin hardware propio publicado; Google Cloud para la mayor parte de las operaciones; Docker, Kubernetes y Google Kubernetes Engine para crear pods; Nginx, Lua y OpenResty en el balanceo; Ruby on Rails, MySQL, Memcached, Redis; React, TypeScript y GraphQL en la administración; Kafka, Debezium y Vitess en datos.",
        [("Hardware", "Sin hardware propio publicado; instancias de Google Cloud; no posee inmuebles", "grey"),
         ("Orquestación", "Docker, Kubernetes y GKE para levantar pods y recursos", "plain"),
         ("Balanceo", "Nginx, Lua y OpenResty: balanceadores programables", "plain"),
         ("Aplicación", "Ruby on Rails (monolito y cientos de aplicaciones), React, TypeScript y GraphQL", "plain"),
         ("Datos", "MySQL, Redis y Memcached por pod; Kafka con Debezium; Vitess en la aplicación Shop", "gold")],
        [("Documentado en posts de 2018 a 2026 y el 10-K", "teal"), ("No se sabe: tipos de instancia, tamaños y costes de nube", "grey")],
        "El 10-K dice que la plataforma es multi-inquilino, de «una sola rama» (todos los comerciantes usan la última versión) y que usa Google Cloud para la mayor parte de las operaciones. Dónde deja de valer: la pila del post de 2018 ha cambiado en parte; Vitess aparece en 2024.",
        BLOG)


def pruebas_fallo():
    return case_cards(
        "Temas a prueba de fallos que Shopify documenta",
        "Cinco mecanismos con veredicto: pods aislados, movimiento de pods entre centros de datos, tiempos de espera y circuit breakers, claves de idempotencia y equilibrio de fragmentos; cada uno con el fallo que contiene.",
        [("Un fragmento o un Redis falla", "Pods aislados: solo cae un pod", "Desde los pods no hubo una caída que afectara a todo Shopify (post de 2018).", "teal"),
         ("Un centro de datos falla", "Pod Mover traslada cada pod al sitio de recuperación en un minuto", "Evacuar un centro es evacuar pod por pod.", "teal"),
         ("Un servicio externo responde lento", "Timeouts bajos y circuit breakers", "Evita que una dependencia inmoviliza hilos y presupuesto.", "gold"),
         ("Un pago se reintenta por un timeout", "Clave de idempotencia", "Evita cobros dobles y devoluciones dobles.", "teal"),
         ("Un fragmento se desequilibra", "Mover tiendas en línea", "Previene fallos de base por exceso de carga.", "teal")],
        note="Documentado en los posts de pods, equilibrio de fragmentos y pagos resilientes. Dónde deja de valer: la ausencia de caídas globales es una afirmación de 2018 sobre la fecha del post; no cubre el periodo posterior.",
        foot=BLOG)


FIGURES = {
    "shopify-contexto.svg": contexto,
    "shopify-ingresos-por-tipo.svg": ingresos,
    "shopify-gmv.svg": gmv,
    "shopify-reparto-del-ingreso.svg": reparto,
    "shopify-utilidad-neta.svg": utilidad,
    "shopify-comerciantes-por-region.svg": regiones,
    "shopify-actores-e-incentivos.svg": actores,
    "shopify-recorridos-de-usuario.svg": recorridos,
    "shopify-esquema-del-negocio.svg": negocio,
    "shopify-capas.svg": capas,
    "shopify-secuencia-sorting-hat.svg": sorting_hat,
    "shopify-un-pod.svg": pod,
    "shopify-evolucion-de-la-arquitectura.svg": evolucion,
    "shopify-equilibrio-de-fragmentos.svg": equilibrio,
    "shopify-monolito-modular.svg": monolito,
    "shopify-bfcm-2021.svg": bfcm,
    "shopify-reservas-de-inventario.svg": reservas,
    "shopify-pagos-resilientes.svg": pagos,
    "shopify-captura-de-cambios.svg": cdc,
    "shopify-casos-especiales.svg": especiales,
    "shopify-linea-de-tiempo.svg": linea,
    "shopify-alternativas.svg": alternativas,
    "shopify-hardware-y-software.svg": hardware,
    "shopify-a-prueba-de-fallos.svg": pruebas_fallo,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys

    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
