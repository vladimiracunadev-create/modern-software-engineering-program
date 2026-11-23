"""Figuras del caso de estudio Dropbox (casos/exito/dropbox.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Las cifras salen del prospecto de 2018 y del 10-K de 2025 de Dropbox (SEC) y de su blog técnico; cada pie
de figura nombra su fuente. Ninguna figura repite una tabla del caso.
"""
from __future__ import annotations

from case_diagrams import canvas, finish, lane_steps, sequence, years
from case_fig_helpers import hub, layer_stack
from figure_cases import case_cards
from figure_kit import grouped_bars, line_chart, timeline
from figures_part45_a import flow

TENK = "Fuente: 10-K de Dropbox del año terminado el 31 de diciembre de 2025 (SEC), consulta 2026-11-23."
S1 = "Fuente: prospecto 424B4 de Dropbox de marzo de 2018 (SEC), consulta 2026-11-23."
BLOG = "Fuente: blog técnico de Dropbox (dropbox.tech), consulta 2026-11-23. Esquema del autor."


def contexto():
    return hub(
        "Dropbox entre personas, equipos, socios y su propia infraestructura",
        "Diagrama de contexto: personas y equipos sincronizan y comparten archivos desde cualquier dispositivo; los socios (Microsoft, Zoom, Atlassian, Slack, Google) se integran; Dropbox guarda el contenido en su infraestructura propia en centros de colocación y en AWS para el resto; los reguladores exigen privacidad y seguridad.",
        ("Dropbox: contenido sincronizado y compartido, con almacenamiento propio", "navy"),
        [("Personas y equipos: carpeta que se sincroniza entre dispositivos", "teal", "sincronizan"),
         ("Organizaciones: colaboración, firma y gestión de documentos", "teal", "contratan"),
         ("Socios de integración: Microsoft, Zoom, Atlassian, Slack, Google", "gold", "integran"),
         ("Centros de colocación: Oregón, Texas, Virginia, París y Hamburgo", "plain", "alojan"),
         ("AWS: el resto del almacenamiento y la entrega de servicios", "plain", "alojan"),
         ("Fabricantes de discos y servidores", "plain", "suministran"),
         ("Reguladores: privacidad y seguridad de los datos", "coral", "exigen"),
         ("Competidores: nubes y suites de ofimática", "grey", "disputan")],
        "Documentado en el 10-K de 2025: los centros de colocación se arriendan y operan directamente y AWS cubre el resto del almacenamiento; las integraciones con Microsoft, Zoom, Atlassian, Slack (ahora de Salesforce), BetterCloud y Google son parte de la oferta. Dónde deja de valer: no hay reparto de datos entre infraestructura propia y AWS.",
        TENK)


def ingresos():
    return years(grouped_bars(
        "Ingresos de Dropbox: la etapa previa a la oferta pública y la actual",
        "Barras con 603,8 millones de dólares en 2015, 844,8 en 2016, 1 106,8 en 2017, 2 548,2 en 2024 y 2 521,0 en 2025; no se muestran 2018 a 2023 porque no se consultaron esos informes.",
        ["2015", "2016", "2017", "2024", "2025"],
        [("Ingresos (millones de USD)", [603.8, 844.8, 1106.8, 2548.2, 2521.0], "teal")],
        unit="millones de USD", decimals=1, plot_h=250,
        note="Mire el cambio de ritmo: de 2015 a 2017 el crecimiento fue de 40 % y 31 % anual; entre 2024 y 2025 el ingreso bajó 1 % (cálculo propio). Dónde deja de valer: hay un salto de seis años sin datos consultados; no se afirma qué ocurrió entre medias.",
        foot="Fuentes: prospecto de 2018 y 10-K de 2025 de Dropbox (SEC)."))


def resultado():
    return years(grouped_bars(
        "Resultado neto de Dropbox: de pérdidas a beneficios",
        "Barras en millones de dólares: pérdidas netas de 325,9; 210,2 y 111,7 millones en 2015, 2016 y 2017 y beneficios netos de 453,6; 452,3 y 508,4 millones en 2023, 2024 y 2025.",
        ["2015", "2016", "2017", "2023", "2024", "2025"],
        [("Resultado neto (negativo: pérdida)", [-325.9, -210.2, -111.7, 453.6, 452.3, 508.4], "teal")],
        unit="millones de USD", decimals=1, plot_h=250,
        note="La pérdida se redujo a la mitad cada año antes de la oferta pública, en paralelo con la migración de infraestructura; los últimos tres años son beneficios. Dónde deja de valer: 2018 a 2022 no se consultaron; las barras negativas son pérdidas.",
        foot="Fuentes: prospecto de 2018 y 10-K de 2025 de Dropbox (SEC)."))


def margen():
    return grouped_bars(
        "Margen bruto de Dropbox, antes y después de su propia infraestructura",
        "Barras con 54 por ciento en 2015, 67 por ciento en 2016 y 76 por ciento en 2017, y 82,5 por ciento en 2024 y 80,1 por ciento en 2025; la mejora de 2015 a 2017 coincide con la migración a infraestructura propia.",
        ["2015", "2016", "2017", "2024", "2025"],
        [("Margen bruto (%)", [54, 67, 76, 82.5, 80.1], "navy")],
        unit="% del ingreso", decimals=1, plot_h=240,
        note="Cálculo propio para 2024 y 2025: 2 103,1 sobre 2 548,2 y 2 020,2 sobre 2 521,0. El prospecto atribuye el descenso del coste de ingresos de 2017 a una reducción de 35,1 millones en costes de infraestructura por la «Infrastructure Optimization». Dónde deja de valer: el margen sube por varias causas; el prospecto solo cita esa para 2017.",
        foot="Fuentes: prospecto de 2018 y 10-K de 2025 de Dropbox (SEC).")


def reparto():
    return grouped_bars(
        "Cómo se reparte cada dólar de ingreso de Dropbox en 2025",
        "Barras horizontales como porcentaje del ingreso de 2 521 millones: coste de ingresos 20 por ciento, investigación y desarrollo 29, ventas y marketing 15, administración 9 y resultado operativo 27 por ciento.",
        ["Coste de ingresos", "Investigación y desarrollo", "Ventas y marketing", "Administración general", "Resultado operativo"],
        [("% del ingreso 2025", [19.9, 29.0, 14.7, 9.1, 27.3], "coral")],
        unit="% del ingreso", horizontal=True, decimals=1, plot_h=250,
        note="Cálculo propio sobre el 10-K: 500,8; 732,0; 369,9; 230,5 y 689,1 millones sobre 2 521,0. Mire que investigación y desarrollo pesa más que ventas y administración juntas. Dónde deja de valer: incluyen remuneración en acciones (300,8 millones en 2025).",
        foot=TENK)


def usuarios():
    return grouped_bars(
        "Usuarios de pago de Dropbox y su ingreso medio",
        "Barras con 11 millones de usuarios de pago a fines de 2017, 18,22 millones a fines de 2024 y 18,08 millones a fines de 2025; el ingreso medio por usuario de pago fue de 140,23 dólares en 2024 y 138,91 en 2025.",
        ["Fin de 2017", "Fin de 2024", "Fin de 2025"],
        [("Usuarios de pago (millones)", [11, 18.22, 18.08], "teal")],
        unit="millones de usuarios de pago", decimals=2, plot_h=230,
        note="El número de usuarios se estancó en los dos últimos años (baja de 0,8 %), igual que el ingreso medio, de 140,23 a 138,91 dólares. Frente a 500 millones de usuarios registrados en 2017, los de pago eran 2 %. Dónde deja de valer: «usuario de pago» es una licencia activa; no mide personas únicas.",
        foot="Fuentes: prospecto de 2018 y 10-K de 2025 de Dropbox (SEC).")


def caja():
    return years(grouped_bars(
        "Flujo de caja libre y recompras: la caja que genera Dropbox",
        "Barras con flujo de caja libre de 871,6 millones de dólares en 2024 y 930,8 millones en 2025, 35 por ciento y 37 por ciento del ingreso; el ingreso recurrente anual total fue de 2 574 millones a fines de 2024 y 2 526 millones a fines de 2025.",
        ["2024", "2025"],
        [("Flujo de caja libre", [871.6, 930.8], "teal"), ("Ingreso recurrente anual total (ARR)", [2574, 2526], "navy")],
        unit="millones de USD", decimals=0, plot_h=240,
        note="El flujo de caja libre es la caja operativa menos las inversiones de capital (21,0 millones en 2025). Cálculo propio de proporción: 930,8 sobre 2 521,0 es 36,9 %. Dónde deja de valer: es una medida no contable que Dropbox define en su 10-K.",
        foot=TENK))


def actores():
    return hub(
        "Quién obtiene qué en el ecosistema de Dropbox",
        "Diagrama de incentivos: las personas obtienen acceso a sus archivos desde cualquier dispositivo; los equipos colaboración; las organizaciones control y seguridad; los socios una integración; Dropbox suscripciones y el control del coste de almacenar.",
        ("Dropbox: convertir usuarios gratuitos en usuarios de pago", "navy"),
        [("Persona: sus archivos disponibles en cualquier dispositivo", "teal", "gana acceso"),
         ("Equipo: compartir y comentar documentos", "teal", "gana colaboración"),
         ("Organización: seguridad, administración y cumplimiento", "gold", "paga más"),
         ("Socio: integra su producto con Dropbox", "plain", "integra"),
         ("Usuario gratuito: prueba el servicio", "grey", "prueba"),
         ("Proveedor de hardware y centros de colocación", "plain", "cobra"),
         ("Regulador: privacidad y seguridad", "coral", "exige"),
         ("Competidor: nubes y suites con almacenamiento incluido", "grey", "disputa")],
        "Análisis propio sobre el prospecto de 2018: más de 500 millones de registrados y solo 11 millones de pago, de modo que el modelo depende de convertir una pequeña fracción. Dónde deja de valer: no hay datos públicos de la tasa de conversión ni del coste de servir a usuarios gratuitos.",
        S1)


def recorridos():
    f = canvas("Cuatro recorridos en Dropbox y su caso límite",
               "Cuatro filas de pasos: una persona que sincroniza una carpeta, un equipo que comparte un documento, una organización que gestiona la seguridad y un usuario con millones de archivos que solo descarga lo que necesita; cada fila termina en un caso límite.")
    y = 56.0
    y = lane_steps(f, y, "Persona", [("Instala la aplicación y crea la carpeta", "teal"), ("Pone archivos en la carpeta", "teal"), ("Se sincronizan a la nube y a otros dispositivos", "teal"), ("Dos dispositivos editan el mismo archivo sin red", "coral")])
    y = lane_steps(f, y, "Equipo", [("Comparte una carpeta", "gold"), ("Invita a colaboradores", "gold"), ("Todos ven los cambios", "gold"), ("Permisos y jerarquías de empresa", "coral")])
    y = lane_steps(f, y, "Organización", [("Compra un plan de equipo", "navy"), ("Configura seguridad y administración", "navy"), ("Los empleados usan Dropbox", "navy"), ("Retención y auditoría de millones de archivos", "coral")])
    y = lane_steps(f, y, "Usuario con muchos archivos", [("Tiene más archivos que disco local", "plain"), ("Activa Smart Sync", "plain"), ("Descarga solo lo que abre", "plain"), ("Se abre un archivo sin conexión", "coral")])
    return finish(f, y + 4, "Cada fila se lee de izquierda a derecha y la caja coral es el borde. Los bordes de la persona y del usuario con muchos archivos salen del post del motor de sincronización de 2020 (sincronización bidireccional con particiones de red, archivos que superan el disco local); los de equipo y organización son escenarios del curso. Dónde deja de valer: no mide frecuencias.", "Esquema del autor sobre el blog técnico de Dropbox y su 10-K.")


def negocio():
    return flow(
        "Cómo gana dinero Dropbox: suscripciones sobre almacenamiento propio",
        "Flujo del negocio: más de 500 millones de registrados en 2017 y una fracción de pago; las suscripciones generan 2 521 millones de ingresos en 2025; los costes de infraestructura bajaron al mover el almacenamiento a una red propia; el negocio genera beneficio y caja libre.",
        [[("Millones de usuarios gratuitos prueban el servicio", "teal"), ("18,08 millones de usuarios de pago", "teal"), ("Suscripciones: ingreso de 2 521 millones de USD", "navy"), ("ARPU de 138,91 dólares al año", "gold")],
         [("Coste de ingresos: 20 % (infraestructura y soporte)", "coral"), ("I+D 29 %, ventas 15 %, administración 9 %", "coral"), ("Beneficio operativo: 27 %", "teal"), ("Flujo de caja libre: 931 millones de USD", "teal")]],
        note="Documentado en el 10-K de 2025: el ingreso proviene de suscripciones a la plataforma y se reconoce a lo largo del contrato. Inferido: que el ahorro de la infraestructura propia explica parte del margen; el prospecto de 2018 solo lo cita para 2017.",
        foot=TENK, width=960)


def capas():
    return layer_stack(
        "Capas de Dropbox que su ingeniería describió",
        "Pila de capas: clientes de escritorio, web y móvil con un motor de sincronización; red de borde con puntos de presencia; servicios de metadatos, entre ellos FileJournal; Magic Pocket para el contenido en bloques inmutables; bases de datos MySQL; infraestructura en centros de colocación y AWS.",
        [("Clientes", "Aplicación de escritorio con el motor de sincronización, web y móvil; Smart Sync para no descargar todo", "teal"),
         ("Red de borde", "Puntos de presencia y peering para acelerar la subida y la descarga desde cualquier parte", "plain"),
         ("Metadatos", "FileJournal registra los cambios de cada archivo; bases MySQL fragmentadas para el índice de bloques", "plain"),
         ("Contenido", "Magic Pocket: almacenamiento de bloques inmutables de hasta 4 MB, cifrados y con codificación de borrado", "gold"),
         ("Infraestructura", "Centros de colocación propios en cinco ubicaciones y AWS para el resto", "navy")],
        [("Documentado entre 2016 y 2025", "teal"), ("No se sabe: cuántos servidores y qué fracción está en AWS", "grey"), ("Inferido: lo nuevo reutiliza estas capas", "grey")],
        "Documentado en los posts de Magic Pocket (2016), de la red de borde, de SMR (2018) y del motor de sincronización (2020) y en el 10-K de 2025. Dónde deja de valer: los posts son de épocas distintas; el reparto actual entre infraestructura propia y AWS no se publica.",
        BLOG)


def sincronizacion():
    return sequence(
        "Del archivo guardado en una carpeta a otro dispositivo",
        "Secuencia de una edición: el motor de sincronización detecta el cambio, divide el archivo en bloques y los sube a Magic Pocket, registra el cambio en FileJournal y notifica a los otros dispositivos, que descargan los bloques que les faltan.",
        ["Dispositivo A", "Motor de sincronización", "FileJournal", "Magic Pocket", "Dispositivo B"],
        [(0, 1, "el usuario guarda un archivo", ""), (1, 3, "sube los bloques cifrados", ""), (1, 2, "registra el cambio", ""),
         (2, 4, "avisa del cambio", "ret"), (4, 3, "pide los bloques que le faltan", ""), (3, 4, "entrega los bloques", "ret")],
        "Documentado por partes: FileJournal registra los cambios y Magic Pocket guarda los bloques inmutables (post de 2016); el motor de sincronización coordina subidas y bajadas (post de 2020). Inferido: el orden exacto y la forma del aviso. Dónde deja de valer: omite deduplicación, conflictos y permisos.",
        BLOG)


def bloques():
    return flow(
        "El modelo de datos de Magic Pocket: del bloque al cubo y a la réplica",
        "Flujo del modelo: un archivo se divide en bloques de hasta 4 megabytes que se comprimen, se cifran y se nombran con su hash SHA-256; los bloques se agrupan en cubos de 1 gigabyte; los cubos se replican en varias máquinas y, con el tiempo, se pasan a codificación de borrado entre regiones.",
        [[("Archivo del usuario dividido en bloques de hasta 4 MB", "teal"), ("Se comprimen, se cifran y se nombran por su hash SHA-256", "teal"), ("Cubo lógico de 1 GB con bloques subidos en la misma época", "gold")],
         [("Réplica directa en varias máquinas para lo reciente", "gold"), ("Codificación de borrado para el resto", "navy"), ("Varias regiones geográficas", "navy")]],
        note="Documentado en «Inside the Magic Pocket» (2016): el sistema es de bloques inmutables, y la mutabilidad vive más arriba, en FileJournal. Dónde deja de valer: es el modelo de 2016; el post de 2018 describe el paso a discos SMR.",
        foot=BLOG, width=960)


def principios():
    return case_cards(
        "Cuatro decisiones de diseño de Magic Pocket y su razón",
        "Cuatro tarjetas: bloques inmutables, discos duros en lugar de discos de estado sólido, coordinación centralizada en lugar de consenso distribuido y una base de datos MySQL fragmentada en lugar de una tabla hash distribuida.",
        [("Bloques inmutables de hasta 4 MB", "La mutabilidad vive en FileJournal", "Simplifica el almacenamiento: un bloque, una vez escrito, nunca cambia.", "teal"),
         ("Discos duros en lugar de SSD", "SSD solo para bases de datos y cachés", "Duraderos, baratos y densos; con réplica y caché para lo reciente.", "teal"),
         ("Evitar el consenso distribuido", "Coordinación centralizada tolerante a fallos", "Reimplementar un protocolo como Paxos «es casi siempre mala idea» según el post.", "gold"),
         ("Índice de bloques", "Un clúster MySQL fragmentado, no una tabla hash distribuida", "Simplifica el desarrollo y reduce incógnitas.", "teal")],
        note="Documentado en «Inside the Magic Pocket» (2016). El propio post presenta estas elecciones como simplificaciones deliberadas. Dónde deja de valer: son decisiones de una carga concreta (datos fríos con baja latencia), no una receta general.",
        foot=BLOG)


def escala_mp():
    return flow(
        "Crecer de decenas de petabytes a varios exabytes en unos seis meses",
        "Flujo del salto de escala: prototipos de decenas de petabytes; migración rápida del contenido de usuarios a infraestructura propia entre 2015 y 2016; el tráfico satura los enrutadores entre clústeres de red; se cambian los algoritmos de colocación y el enrutado, y finalmente la arquitectura de red entre clústeres.",
        [[("Prototipos de decenas de petabytes", "plain"), ("Se migra la mayoría del contenido de 2015 a 2016", "gold"), ("El tráfico satura los enrutadores entre clústeres", "coral")],
         [("Se cambian la colocación de datos y el enrutado", "teal"), ("Se rediseña la red entre clústeres", "teal"), ("Sistema de varios exabytes", "navy")]],
        note="Documentado en «Inside the Magic Pocket» (2016) y en el prospecto de 2018: el sistema pasó de prototipos de dos dígitos de petabytes a varios exabytes en unos seis meses, algo «bastante sin precedentes» según el post. Dónde deja de valer: el post no da la fecha exacta de cada paso.",
        foot="Fuentes: dropbox.tech (2016) y prospecto de 2018 (SEC). Esquema del autor.", width=960)


def ahorro():
    return grouped_bars(
        "Qué bajó el coste de ingresos de Dropbox en 2017",
        "Barras en millones de dólares: el coste de ingresos bajó 21,7 millones en 2017 respecto de 2016; los costes de infraestructura bajaron 35,1 millones por la optimización de infraestructura y la amortización de tecnologías 5,9 millones, mientras el personal subió 11,0 millones.",
        ["Infraestructura", "Amortización de tecnología", "Personal (sube)"],
        [("Variación en 2017 (millones de USD)", [-35.1, -5.9, 11.0], "teal")],
        unit="millones de USD de variación", decimals=1, plot_h=230,
        note="Las barras negativas son reducciones. Cálculo propio: -35,1 - 5,9 + 11,0 deja -30,0; el resto hasta los -21,7 que reporta el prospecto corresponde a otras partidas que no se desglosan aquí. Dónde deja de valer: el prospecto solo cita las principales causas.",
        foot=S1)


def borde():
    return flow(
        "La red de borde de Dropbox: de cinco puntos en EE. UU. a presencia global",
        "Flujo de la evolución: en 2014 solo había presencia en Estados Unidos con dos regiones de centros de datos y cinco puntos de presencia, unos cien socios de peering y casi toda la capacidad de borde con proveedores de tránsito; después se amplió a una red global de puntos de presencia propia, con velocidades de sincronización de hasta 300 por ciento mayores en algunos usuarios.",
        [[("2014: solo EE. UU., dos regiones de datos y cinco puntos de presencia", "plain"), ("Unos 100 socios de peering; casi todo por tránsito", "coral"), ("Capacidad de borde de cientos de gigabits", "coral")],
         [("Red global de puntos de presencia propia", "teal"), ("Más peering y menos dependencia de tránsito", "teal"), ("Mejoras de hasta 300 % en la velocidad de sincronización", "navy")]],
        note="Documentado en «Evolution of Dropbox's Edge Network»: evaluaron CDN y otras ofertas en la nube y concluyeron que una solución propia servía mejor a sus necesidades. Dónde deja de valer: el post es de la época de 2016 a 2017 y no da cifras actuales.",
        foot=BLOG, width=960)


def smr():
    return flow(
        "SMR: discos más densos a cambio de rediseñar el software",
        "Flujo del cambio a discos de grabación magnética en tejas (SMR): más densidad y menor coste por terabyte pero escritura más lenta fuera de la caja; el software de Magic Pocket se rediseñó para escribir de forma secuencial; Dropbox fue la primera gran empresa en adoptarlos y añadió cientos de petabytes.",
        [[("Discos PMR convencionales: caros por terabyte", "plain"), ("SMR: más densos pero lentos de escribir", "gold"), ("Rediseño del software y de los servidores", "teal")],
         [("Durabilidad de más de 99,9999999999 % al año", "navy"), ("Disponibilidad de más de 99,99 %", "navy"), ("Cientos de petabytes nuevos con ahorro significativo", "teal")]],
        note="Documentado en el post de junio de 2018 de los equipos de hardware de Magic Pocket. La afirmación de ser la primera gran empresa tecnológica en adoptarlos es del propio post. Dónde deja de valer: no se publica el ahorro exacto.",
        foot=BLOG, width=960)


def nucleus():
    return flow(
        "La reescritura del motor de sincronización: cuatro años y una lista de comprobación",
        "Flujo de la decisión: el primer motor de sincronización tenía problemas de modelo de datos que solo aparecían a escala; probaron mejoras incrementales, como anotaciones de tipos de Python, telemetría y refactorizaciones, que no bastaron; reescribieron el motor desde cero durante cuatro años, con un modelo de datos limpio y pruebas, y lo lanzaron a todos en marzo de 2020.",
        [[("Motor clásico con fallos de modelo de datos a escala", "coral"), ("Mejoras incrementales: refactorización, tipos y telemetría", "gold"), ("No bastaron: bloqueos gruesos y poca paralelización", "coral")],
         [("Reescritura desde cero durante cuatro años", "teal"), ("Modelo de datos limpio y pruebas aleatorias", "teal"), ("Lanzamiento a todos los usuarios en marzo de 2020", "navy")]],
        note="Documentado en «Rewriting the heart of our sync engine» (marzo de 2020). El propio post advierte de que la reescritura habría sido una mala idea en muchos entornos y propone una lista de comprobación previa. Dónde deja de valer: es un caso de reescritura que salió bien en una empresa con medios para hacerla.",
        foot=BLOG, width=960)


def sitios():
    return hub(
        "Dónde guarda Dropbox el contenido de los usuarios",
        "Esquema de ubicaciones: centros de colocación propios en Oregón, Texas, Virginia, París y Hamburgo para la mayoría del contenido, y AWS en Estados Unidos, Australia, Europa y Japón para el resto y para localizar datos; durabilidad de al menos 99,999999999 por ciento.",
        ("Contenido de los usuarios", "navy"),
        [("Oregón (colocación propia)", "teal", "guarda"),
         ("Texas (colocación propia)", "teal", "guarda"),
         ("Virginia (colocación propia)", "teal", "guarda"),
         ("París y Hamburgo (colocación propia)", "teal", "guardan"),
         ("AWS en EE. UU. y Europa: el resto del almacenamiento", "gold", "completa"),
         ("AWS en Australia y Japón: localizar el contenido", "gold", "localiza")],
        "Documentado en el 10-K de 2025: la mayoría del contenido está en infraestructura propia en centros de colocación que se arriendan y operan, y el resto en AWS. Dónde deja de valer: no se publican las proporciones.",
        TENK)


def linea():
    return years(timeline(
        "Dropbox de 2007 a 2026: empresa, infraestructura y producto",
        "Línea de tiempo con tres carriles: la empresa (constituida en mayo de 2007 como Evenflow, renombrada Dropbox en octubre de 2009, cotizada desde marzo de 2018), la infraestructura (etapa previa, migración a infraestructura propia en 2015 y 2016, SMR en 2018) y el producto (sincronización en beta en 2008, Smart Sync, nuevo motor Nucleus en 2020).",
        [("Empresa", [(2007.4, 2018.2, "Empresa privada", "grey"), (2018.2, 2026, "Cotizada (Nasdaq: DBX)", "teal")]),
         ("Infraestructura", [(2007.4, 2015, "Previa", "grey"), (2015, 2017, "Cambio", "gold"), (2017, 2026, "Magic Pocket + AWS", "navy")]),
         ("Producto", [(2008.5, 2008.7, "", "coral"), (2018.45, 2018.55, "", "coral"), (2020.15, 2020.25, "", "coral")])],
        unit="año", events=[(2007.4, "constitución"), (2008.5, "beta"), (2018.2, "IPO"), (2020.2, "Nucleus")],
        t_max=2027, ticks=[2007, 2011, 2015, 2019, 2023, 2027], lane_h=46,
        note="Hechos con fuente: constitución en mayo de 2007 como Evenflow y cambio de nombre en octubre de 2009 (prospecto de 2018); oferta pública a 21 dólares en marzo de 2018; migración de la mayoría del contenido en 2015 y 2016; sincronización en beta en 2008 y Nucleus en marzo de 2020 (posts). Dónde deja de valer: las fuentes consultadas no describen la infraestructura anterior a 2015; la etapa «previa» no se detalla.",
        foot="Fuentes: prospecto de 2018, 10-K de 2025 y blog técnico de Dropbox."))


def especiales():
    return case_cards(
        "Casos especiales documentados y cómo se resuelven",
        "Cinco tarjetas: tráfico que satura los enrutadores entre clústeres, discos SMR lentos de escribir, sincronización bidireccional con particiones de red, usuarios con más archivos que disco y una reescritura de cuatro años; cada una con su mecanismo y veredicto.",
        [("Tráfico que satura los enrutadores entre clústeres", "Cambiar la colocación, el enrutado y la red entre clústeres", "Un crecimiento no previsto obliga a tocar la topología.", "gold"),
         ("Discos SMR que escriben despacio", "Rediseñar el software para escritura secuencial", "Se obtiene la densidad sin perder rendimiento, a costa de ingeniería.", "teal"),
         ("Particiones de red como situación normal", "Un modelo de datos limpio y pruebas de combinaciones", "El número de estados de archivo y de acciones es astronómico.", "gold"),
         ("Más archivos que disco local", "Smart Sync: descargar solo lo que se abre", "Cambia qué significa «sincronizado».", "teal"),
         ("Un motor con fallos de modelo de datos", "Reescribirlo durante cuatro años", "Solo funcionó porque se agotaron antes las mejoras incrementales.", "gold")],
        note="Cada tarjeta enlaza un hecho citado con el mecanismo. Color: coral falla, teal se sostiene, gold depende. Dónde deja de valer: son casos documentados por el propio Dropbox.",
        foot=BLOG)


def alternativas():
    return case_cards(
        "Alternativas que Dropbox no tomó o sustituyó, como análisis del curso",
        "Cuatro tarjetas: seguir con infraestructura de terceros, usar una red de distribución comercial en el borde, usar una tabla hash distribuida para el índice de bloques y mejorar el motor de sincronización sin reescribirlo; cada una con lo que Dropbox hizo.",
        [("Seguir con infraestructura de terceros", "Migrar la mayoría del contenido a infraestructura propia", "Documentado: coste de infraestructura menor y margen bruto de 54 % a 76 % entre 2015 y 2017.", "teal"),
         ("Una CDN comercial para el borde", "Red de puntos de presencia propia", "Documentado: evaluaron CDN y otras ofertas y la solución propia servía mejor.", "teal"),
         ("Tabla hash distribuida para el índice", "Un clúster MySQL fragmentado", "Documentado: simplifica el desarrollo y reduce incógnitas.", "teal"),
         ("Seguir mejorando el motor clásico", "Reescritura completa (Nucleus)", "Documentado: se agotaron antes las mejoras incrementales.", "gold")],
        note="Rótulo: documentado por el propio Dropbox. Dónde deja de valer: son razones de quien tomó la decisión; no hay una evaluación independiente de cada alternativa.",
        foot=BLOG)


def hardware():
    return layer_stack(
        "Hardware y software que Dropbox hace público",
        "Pila: servidores y discos de infraestructura propia en centros de colocación; discos duros PMR y luego SMR de alta densidad; AWS para el resto; software de almacenamiento de bloques propio (Magic Pocket), MySQL, y un motor de sincronización reescrito.",
        [("Hardware", "Servidores propios en centros de colocación arrendados; discos PMR y, desde 2018, SMR de alta densidad", "grey"),
         ("Red", "Puntos de presencia con peering y tránsito; BGP y OSPF en la red de 2014", "plain"),
         ("Almacenamiento", "Magic Pocket: bloques inmutables con codificación de borrado entre regiones", "gold"),
         ("Metadatos", "FileJournal y clústeres MySQL fragmentados", "plain"),
         ("Cliente", "Motor de sincronización reescrito (Nucleus); aplicación de escritorio, web y móvil", "plain")],
        [("Documentado en posts de 2016 a 2020 y el 10-K", "teal"), ("No se sabe: número de servidores, discos ni costes por componente", "grey")],
        "El post de SMR cuenta que Dropbox añadió cientos de petabytes con servidores llenos de discos SMR de alta densidad y que fue la primera gran empresa tecnológica en adoptarlos. Dónde deja de valer: la mezcla actual de discos no se publica.",
        BLOG)


def pruebas_fallo():
    return case_cards(
        "Temas a prueba de fallos que Dropbox documenta",
        "Cuatro mecanismos con veredicto: durabilidad efectivamente infinita con codificación de borrado entre regiones, bloques inmutables que no se corrompen al editarse, múltiples capas de redundancia y reconstrucción de réplicas, y pruebas de la sincronización para detectar regresiones antes de llegar a producción.",
        [("Un disco o un servidor falla", "Réplica y reparación automática", "La durabilidad objetivo es más de 99,9999999999 % al año.", "teal"),
         ("Una región queda fuera", "Codificación de borrado entre regiones geográficas", "El diseño tolera calamidades y desastres naturales.", "teal"),
         ("Un cliente se desconecta en medio de una edición", "Registro de cambios en FileJournal; bloques inmutables", "La mutabilidad está arriba y el almacenamiento no cambia.", "teal"),
         ("Una regresión del motor de sincronización", "Pruebas automáticas de combinaciones de estados", "Testear la sincronización es difícil por el número de combinaciones.", "gold")],
        note="Documentado en los posts de Magic Pocket (2016) y del motor de sincronización (2020) y en el 10-K (durabilidad de 99,999999999 %). Dónde deja de valer: son objetivos de diseño publicados, no tasas de fallo medidas.",
        foot=BLOG)


FIGURES = {
    "dropbox-contexto.svg": contexto,
    "dropbox-ingresos.svg": ingresos,
    "dropbox-resultado-neto.svg": resultado,
    "dropbox-margen-bruto.svg": margen,
    "dropbox-reparto-del-ingreso.svg": reparto,
    "dropbox-usuarios-de-pago.svg": usuarios,
    "dropbox-caja-y-arr.svg": caja,
    "dropbox-actores-e-incentivos.svg": actores,
    "dropbox-recorridos-de-usuario.svg": recorridos,
    "dropbox-esquema-del-negocio.svg": negocio,
    "dropbox-capas.svg": capas,
    "dropbox-secuencia-de-sincronizacion.svg": sincronizacion,
    "dropbox-bloques-y-cubos.svg": bloques,
    "dropbox-decisiones-de-magic-pocket.svg": principios,
    "dropbox-salto-de-escala.svg": escala_mp,
    "dropbox-ahorro-de-infraestructura.svg": ahorro,
    "dropbox-red-de-borde.svg": borde,
    "dropbox-discos-smr.svg": smr,
    "dropbox-reescritura-del-motor.svg": nucleus,
    "dropbox-donde-se-guarda.svg": sitios,
    "dropbox-linea-de-tiempo.svg": linea,
    "dropbox-casos-especiales.svg": especiales,
    "dropbox-alternativas.svg": alternativas,
    "dropbox-hardware-y-software.svg": hardware,
    "dropbox-a-prueba-de-fallos.svg": pruebas_fallo,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys

    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
