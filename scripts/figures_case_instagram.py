"""Figuras del caso de estudio Instagram (casos/exito/instagram.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Las cifras salen de los 10-K de Facebook (2012) y de Meta (2025), de la prensa especializada fechada y
del blog de ingeniería; cada pie de figura nombra su fuente. Ninguna figura repite una tabla del caso.
"""
from __future__ import annotations

from case_diagrams import canvas, finish, lane_steps, years
from case_fig_helpers import hub, layer_stack
from figure_cases import case_cards
from figure_kit import grouped_bars, stacked_bars, timeline
from figures_part45_a import flow

META = "Fuente: 10-K de Meta Platforms del año 2025 (SEC), consulta 2026-11-23."
FB12 = "Fuente: 10-K de Facebook del año 2012 (SEC), consulta 2026-11-23."
ENG = "Fuentes: Engineering at Meta, copia archivada del blog de Instagram Engineering e InfoQ (consulta 2026-11-23). Esquema del autor."


def contexto():
    return hub(
        "Instagram dentro de la familia de aplicaciones de Meta",
        "Diagrama de contexto: personas y creadores usan Instagram para fotos, vídeo, mensajes y compras; los anunciantes pagan por alcanzarlos a través de la plataforma publicitaria de Meta; Instagram comparte infraestructura y personas con Meta, desde el centro de datos hasta el sistema de anuncios, y compite con otras aplicaciones de vídeo y de redes sociales.",
        ("Instagram: producto de Meta desde agosto de 2012", "navy"),
        [("Personas y creadores: Feed, Stories, Reels, Live y mensajes", "teal", "usan"),
         ("Negocios: descubrimiento y compras desde la aplicación", "teal", "venden"),
         ("Anunciantes: pagan por alcance mediante la plataforma de Meta", "gold", "pagan"),
         ("Meta: infraestructura, personal y sistema de anuncios comunes", "plain", "aloja"),
         ("Tiendas de aplicaciones: distribución en iOS y Android", "plain", "distribuyen"),
         ("Threads: aplicación hermana que reutiliza el grafo social", "plain", "comparte"),
         ("Reguladores y menores: seguridad, privacidad, competencia", "coral", "exigen"),
         ("Competidores: otras redes de vídeo y mensajería", "grey", "disputan")],
        "Documentado: el 10-K de Meta describe Instagram como lugar donde personas y creadores se conectan mediante fotos, vídeo y mensajes, con Feed, Stories, Reels, Live y mensajería, y agrupa sus cifras de usuarios y de ingresos en la familia de aplicaciones. Dónde deja de valer: Meta no publica ingresos ni usuarios de Instagram por separado.",
        META)


def precio():
    return grouped_bars(
        "De qué se compone el precio de Instagram en la contabilidad de Facebook",
        "Barras con los componentes de la compra: 300 millones de dólares en efectivo, 221 millones en acciones ya adquiridas por los accionistas externos y 194 millones en acciones sujetas a permanencia de los empleados, que suman unos 715 millones; el precio contable de la combinación fue 521 millones.",
        ["Efectivo", "Acciones adquiridas (no empleados)", "Acciones sujetas a permanencia (empleados)"],
        [("Millones de USD", [300, 221, 194], "navy")],
        unit="millones de USD", decimals=0, plot_h=240,
        note="El 10-K de 2012 da un precio de compra de 521 millones (300 en efectivo y unos 12 millones de acciones de la clase B) y, aparte, unos 11 millones de acciones con permanencia valoradas en 194 millones que se reconocen como gasto durante tres años. Cálculo propio: 521 menos 300 deja 221 en acciones; 521 más 194 suman 715 millones, la cifra que la prensa de 2013 cita. Dónde deja de valer: el valor de las acciones depende de la cotización del cierre; la cifra de mil millones de abril de 2012 era un valor anunciado.",
        foot=FB12)


def ingresos_meta():
    return years(grouped_bars(
        "Ingresos de Meta, de los que Instagram forma parte, 2023 a 2025",
        "Barras con 134 902 millones de dólares en 2023, 164 501 en 2024 y 200 966 en 2025; la publicidad representa 196 175 millones en 2025 y la familia de aplicaciones 198 759 millones.",
        ["2023", "2024", "2025"],
        [("Ingresos totales (millones de USD)", [134902, 164501, 200966], "teal"), ("Publicidad", [131948, 160633, 196175], "navy")],
        unit="millones de USD", decimals=0, plot_h=260,
        note="Mire que la publicidad es casi todo el ingreso: 97,6 % del total en 2025 (cálculo propio). Instagram aporta a ese ingreso pero Meta no publica cuánto. Dónde deja de valer: es la cifra del grupo; no sirve para estimar ingresos de Instagram.",
        foot=META))


def personas():
    return grouped_bars(
        "Personas diarias de la familia de aplicaciones de Meta (diciembre)",
        "Barras con 3,35 mil millones de personas activas diarias en diciembre de 2024 y 3,58 mil millones en diciembre de 2025, un aumento de 7 por ciento; la cifra cuenta personas únicas de Facebook, Instagram, Messenger y WhatsApp.",
        ["Dic 2024", "Dic 2025"],
        [("Personas activas diarias (miles de millones)", [3.35, 3.58], "teal")],
        unit="miles de millones de personas", decimals=2, plot_h=220,
        note="El 10-K aclara que la cifra son personas únicas estimadas, no cuentas, con técnicas de atribución entre cuentas. Dónde deja de valer: no se puede extraer el número de usuarios de Instagram de este indicador.",
        foot=META)


def costos():
    return grouped_bars(
        "Cómo se reparte cada dólar de ingreso de Meta en 2025",
        "Barras horizontales como porcentaje del ingreso de 200 966 millones: coste de ingresos 18 por ciento, investigación y desarrollo 29, marketing y ventas 6, administración 6 y resultado operativo 41.",
        ["Coste de ingresos", "Investigación y desarrollo", "Marketing y ventas", "Administración general", "Resultado operativo"],
        [("% del ingreso 2025", [18, 29, 6, 6, 41], "coral")],
        unit="% del ingreso", horizontal=True, decimals=0, plot_h=250,
        note="Son los porcentajes que el propio 10-K presenta (redondeados). Mire que el gasto en investigación y desarrollo, 57 372 millones, pesa casi tanto como el coste de ingresos y ventas juntos. Dónde deja de valer: no hay desglose por aplicación.",
        foot=META)


def actores():
    return hub(
        "Quién obtiene qué en el ecosistema de Instagram",
        "Diagrama de incentivos: las personas obtienen un lugar para compartir y descubrir; los creadores audiencia; los negocios clientes; los anunciantes alcance medible; Meta atención que monetiza con anuncios y una pieza más de su familia de aplicaciones.",
        ("Instagram: atención a cambio de contenido, monetizada con anuncios", "navy"),
        [("Persona: ve y comparte fotos, vídeo y mensajes", "teal", "gana contenido"),
         ("Creador: construye audiencia con Reels y Stories", "teal", "gana audiencia"),
         ("Negocio: descubre clientes y vende desde la aplicación", "gold", "gana ventas"),
         ("Anunciante: compra impresiones en la plataforma de Meta", "gold", "paga"),
         ("Meta: ingresos de publicidad de toda la familia", "plain", "monetiza"),
         ("Menores y familias: piden protecciones específicas", "coral", "exigen"),
         ("Competidor: otras redes de vídeo corto", "grey", "disputa"),
         ("Ingenieros: operan el sistema con herramientas comunes de Meta", "plain", "operan")],
        "Análisis propio sobre hechos del 10-K de Meta: los ingresos son publicitarios en su casi totalidad y los anuncios aumentaron 12 % en impresiones y 9 % en precio medio en 2025. Dónde deja de valer: la parte de ese ingreso que corresponde a Instagram no es pública.",
        META)


def recorridos():
    f = canvas("Cuatro recorridos en Instagram y su caso límite",
               "Cuatro filas de pasos: una persona que publica una foto, un creador de Reels, un negocio que vende y un usuario nuevo que se une desde otra aplicación de Meta; cada fila termina en un caso límite.")
    y = 56.0
    y = lane_steps(f, y, "Persona", [("Abre la aplicación y ve el Feed", "teal"), ("Saca una foto y aplica un filtro", "teal"), ("Publica; el servidor guarda y reparte", "teal"), ("Foto que se hace viral en minutos", "coral")])
    y = lane_steps(f, y, "Creador", [("Graba un vídeo corto", "gold"), ("Sube y se transcodifica", "gold"), ("Aparece en Reels y en Explorar", "gold"), ("Audiencia mundial: lecturas desde otro continente", "coral")])
    y = lane_steps(f, y, "Negocio", [("Crea un perfil de empresa", "navy"), ("Muestra productos", "navy"), ("Compra y anuncio", "navy"), ("Rechazo o suspensión de la cuenta", "coral")])
    y = lane_steps(f, y, "Usuario de Threads", [("Se registra con la cuenta de Instagram", "plain"), ("Sigue a quienes ya sigue en Instagram", "plain"), ("Se ejecuta el grafo de forma asíncrona", "plain"), ("Cien millones de altas en cinco días", "coral")])
    return finish(f, y + 4, "Cada fila se lee de izquierda a derecha y la caja coral es el borde. El caso del usuario de Threads viene de un post de Engineering at Meta (2023); los demás son escenarios del curso sobre funciones que el 10-K describe (Feed, Stories, Reels, mensajería, compras). Dónde deja de valer: no hay datos públicos de la frecuencia de cada borde.", "Esquema del autor sobre el 10-K de Meta (2025) y el blog de Engineering at Meta.")


def negocio():
    return flow(
        "Cómo se monetiza Instagram: dentro de la publicidad de Meta",
        "Flujo del negocio: personas y creadores aportan atención; Instagram la entrega a la plataforma de anuncios de Meta; los anunciantes pagan por impresiones; el ingreso se registra en la familia de aplicaciones y se reinvierte en infraestructura y en investigación; en 2012 Instagram aún no tenía ingresos directos.",
        [[("2012: Instagram aún no genera ingresos directos", "gold"), ("Personas y creadores aportan atención", "teal"), ("Meta vende anuncios en la familia de aplicaciones", "navy"), ("Publicidad: 196 175 millones de USD en 2025", "navy")],
         [("Coste de ingresos: 18 %", "coral"), ("Investigación y desarrollo: 29 %", "coral"), ("Marketing, ventas y administración: 12 %", "coral"), ("Resultado operativo: 41 %", "teal")]],
        note="Documentado: el 10-K de 2012 dice que Facebook no obtenía ingresos directos de Instagram; el de 2025 agrupa los ingresos en la familia de aplicaciones. Inferido: que hoy Instagram genera una parte sustancial de la publicidad de Meta; Meta no lo cuantifica.",
        foot=META, width=960)


def capas():
    return layer_stack(
        "Capas de Instagram que su ingeniería describió",
        "Pila de capas: clientes iOS y Android; un nivel web sin estado en Django con Python; servicios de apoyo con Cassandra, TAO y Memcached; trabajos asíncronos con Celery y la infraestructura de Meta en centros de datos de Estados Unidos y Europa.",
        [("Clientes", "Aplicaciones para iOS y Android y la web", "teal"),
         ("Nivel web", "Django en Python, servidor con procesos pre-bifurcados y asyncio por proceso; sin estado", "plain"),
         ("Servicios y trabajos", "Trabajos asíncronos con Celery; el grafo social en TAO", "plain"),
         ("Datos", "PostgreSQL fragmentado (primeras etapas), Cassandra como clave-valor general y Memcached", "gold"),
         ("Infraestructura", "Centros de datos de Meta en EE. UU. y Europa; antes, AWS", "navy")],
        [("Documentado entre 2012 y 2023", "teal"), ("No se sabe: pila actual de cada servicio", "grey"), ("Inferido: Reels y vídeo usan sistemas de Meta no descritos aquí", "grey")],
        "Documentado en el post de fragmentación (copia de 2012), la charla de LISA 2018 resumida por InfoQ y los posts de Engineering at Meta de 2020 a 2023. Dónde deja de valer: las etapas son de años distintos; la pila de 2012 (PostgreSQL) y la de 2018 (Cassandra y TAO) no son simultáneas.",
        ENG)


def bits():
    return stacked_bars(
        "Anatomía de un identificador de Instagram: 64 bits con la hora y el fragmento dentro",
        "Barra apilada de 64 bits: 41 bits de tiempo en milisegundos, 13 bits con el identificador del fragmento lógico y 10 bits de una secuencia que da hasta 1 024 identificadores por fragmento y milisegundo.",
        ["Identificador de 64 bits"],
        [("Tiempo en ms (41 bits)", [41], "teal"), ("Fragmento lógico (13 bits)", [13], "gold"), ("Secuencia (10 bits)", [10], "navy")],
        unit="bits", decimals=0, horizontal=True, plot_h=160,
        note="Documentado: con una época propia, 41 bits dan unos 41 años de identificadores; 13 bits permiten hasta 8 192 fragmentos lógicos; la secuencia módulo 1 024 da 1 024 identificadores por fragmento por milisegundo. Cálculo propio: 2^13 = 8 192. Dónde deja de valer: es el diseño de la época de PostgreSQL (2011-2012).",
        foot="Fuente: «Sharding & IDs at Instagram», Instagram Engineering (copia archivada fechada el 30 de diciembre de 2012).")


def fragmentos():
    return flow(
        "Fragmentos lógicos sobre pocos servidores físicos",
        "Dos filas: varios miles de fragmentos lógicos son esquemas de PostgreSQL asignados en código a pocos servidores físicos; al crecer, se mueven conjuntos de fragmentos lógicos a más servidores sin reubicar datos; cada tabla del fragmento genera sus propios identificadores.",
        [[("Varios miles de fragmentos lógicos (esquemas)", "teal"), ("Asignados en código a pocos servidores físicos", "teal"), ("Crecer: mover conjuntos de esquemas a más servidores", "gold")],
         [("Cada tabla genera sus identificadores con PL/pgSQL", "plain"), ("El identificador lleva el fragmento dentro", "plain"), ("Sin reubicar datos ni nuevas piezas móviles", "teal")]],
        note="Documentado en el post de 2012: el criterio era tener pocas piezas móviles, porque el equipo escalaba Instagram con muy pocos ingenieros. Dónde deja de valer: la clave de partición del ejemplo era el identificador de usuario; otras tablas pueden usar otras.",
        foot="Fuente: «Sharding & IDs at Instagram» (copia archivada de 2012).", width=960)


def alternativas_id():
    return case_cards(
        "Cuatro formas de generar identificadores que Instagram comparó en su post",
        "Cuatro tarjetas: generar identificadores en la aplicación (UUID u ObjectId), un servicio dedicado como Snowflake, servidores de tickets de base de datos como los de Flickr y la solución elegida, generar dentro de PostgreSQL; cada una con su ventaja y su coste.",
        [("Generar en la aplicación (UUID, ObjectId)", "Descartada: 96 bits o más y sin orden natural en algunos tipos", "Evita puntos de contención pero ocupa más espacio.", "gold"),
         ("Servicio dedicado (Snowflake con ZooKeeper)", "Descartada: más piezas móviles", "Era la más cercana; la complejidad de operar otro servicio pesó en contra.", "gold"),
         ("Servidores de tickets en la base de datos", "Descartada: cuello de botella o punto único", "Con una sola base es punto único; con dos ya no ordena en el tiempo.", "coral"),
         ("Generar dentro de PostgreSQL por esquema", "Elegida", "Mantiene 64 bits, ordenación por tiempo y ninguna pieza nueva.", "teal")],
        note="Rótulo: documentado, pues el propio post enumera estas alternativas y razones. Dónde deja de valer: es la decisión de 2011-2012; Instagram usó luego Cassandra y TAO para otros datos.",
        foot="Fuente: «Sharding & IDs at Instagram» (copia archivada de 2012).")


def continentes():
    return hub(
        "Partir Instagram entre Estados Unidos y Europa",
        "Esquema de la partición por continentes: el nivel web sin estado en Django; Cassandra partida con la herramienta Akkio para que los datos de cada usuario estén cerca; TAO con un maestro local en Europa; y un 20 por ciento de holgura en cada región para absorber la caída de un centro de datos.",
        ("Instagram en dos continentes (charla de LISA 2018)", "navy"),
        [("Django sin estado delante de los datos", "teal", "atiende"),
         ("Cassandra: datos del usuario en su continente con Akkio", "teal", "parte"),
         ("TAO: grafo social con un maestro local en cada región", "gold", "escribe local"),
         ("Hash social: enruta a los cubos correctos", "plain", "enruta"),
         ("Holgura de 20 % por centro de datos", "plain", "reserva"),
         ("Sin recuperación entre océanos: latencia y datos distintos", "coral", "límite")],
        "Documentado por InfoQ a partir de la charla de LISA 2018: Instagram pasó de AWS a los centros de datos de Facebook, tuvo que repartirse entre EE. UU. y Europa por espacio de almacenamiento, y rediseñó la recuperación ante desastres. Dónde deja de valer: es una charla de 2018 resumida por una fuente secundaria.",
        "Fuente: InfoQ, «Splitting Stateful Services across Continents at Instagram» (29 de noviembre de 2018).")


def evolucion():
    return flow(
        "Cómo cambió la infraestructura de Instagram",
        "Dos filas de etapas: aplicación Django con PostgreSQL fragmentado en AWS; migración a la infraestructura de Facebook tras la compra; reparto entre Estados Unidos y Europa con Cassandra y TAO; escalado automático del servicio Django; optimización del runtime de Python con Cinder y objetos inmortales.",
        [[("2010-2012: Django, PostgreSQL fragmentado y muy pocos ingenieros", "plain"), ("Tras la compra: migración a centros de datos de Facebook", "gold"), ("Cassandra, TAO y Memcached como pila principal", "gold"), ("Partición entre EE. UU. y Europa", "teal")],
         [("2020: el servicio Django entra en el escalado automático de Meta", "teal"), ("2022: Cinder, una bifurcación de CPython, y su JIT", "teal"), ("2023: objetos inmortales llegan a Python 3.12", "teal"), ("Threads reutiliza la pila de Instagram", "navy")]],
        note="Documentado en los posts de 2012, 2020, 2022 y 2023 y en la charla de 2018. Dónde deja de valer: no se conocen las fechas intermedias de la migración de AWS a los centros de datos de Meta.",
        foot=ENG, width=960)


def inmortales():
    return flow(
        "Objetos inmortales: evitar que los procesos hijos copien memoria",
        "Flujo del problema y la solución: el servidor Django pre-bifurca procesos que comparten memoria de solo lectura; el recuento de referencias y el recolector de basura escriben en esos objetos y fuerzan copias; los objetos inmortales omiten esas escrituras y se incorporaron a Python 3.12.",
        [[("Servidor pre-bifurcado: procesos comparten objetos de solo lectura", "plain"), ("Los recuentos de referencias escriben en ellos", "coral"), ("Copia en escritura: crece la memoria privada y baja la compartida", "coral")],
         [("Objetos inmortales: no se cambia su recuento", "teal"), ("Memoria compartida se mantiene", "teal"), ("Se propone a Python como PEP 683 (3.12)", "teal")]],
        note="Documentado en «Introducing Immortal Objects for Python» (agosto de 2023) y en el post de Python 3.12 de octubre de 2023. Dónde deja de valer: el post dice que compartirlo con la comunidad fue largo por compatibilidad y rendimiento; aquí solo se resume el mecanismo.",
        foot="Fuente: Engineering at Meta, 15 de agosto y 5 de octubre de 2023.", width=960)


def threads():
    return flow(
        "Threads sobre la base de Instagram: cien millones de altas en cinco días",
        "Flujo: Threads se lanza el 5 de julio de 2023 con dos días de preaviso a las áreas de infraestructura; un equipo pequeño la construyó en cinco meses de trabajo técnico; el grafo de seguidores se replica desde Instagram con trabajos asíncronos para no bloquear el alta; llega a cien millones de altas en cinco días.",
        [[("Lanzamiento el 5 de julio de 2023 con dos días de preaviso", "gold"), ("Un equipo pequeño: cinco meses de trabajo técnico", "teal"), ("Seguir a los mismos que en Instagram", "teal")],
         [("La operación costosa se ejecuta de forma asíncrona", "teal"), ("El alta no se bloquea ni se degrada", "teal"), ("Más de 100 millones de altas en cinco días", "navy")]],
        note="Documentado en «How Meta built the infrastructure for Threads» (diciembre de 2023). Dónde deja de valer: es un caso de Meta que se apoya en su infraestructura común; no prueba que otra empresa pueda hacerlo con dos días de aviso.",
        foot="Fuente: Engineering at Meta, 19 de diciembre de 2023.", width=960)


def linea():
    return years(timeline(
        "Instagram de 2010 a 2026: producto, compra e infraestructura",
        "Línea de tiempo con tres carriles: producto (lanzamiento el 6 de octubre de 2010, compra por Facebook en agosto de 2012, parte de Meta), infraestructura (pila Django con PostgreSQL hasta 2012 y Cassandra y TAO después, reparto en continentes hacia 2018) y runtime (Cinder en 2022, objetos inmortales en 2023).",
        [("Producto", [(2010.77, 2012.62, "Propia", "grey"), (2012.62, 2026, "Parte de Facebook y luego Meta", "teal")]),
         ("Infraestructura", [(2010.77, 2012.9, "Postgres", "gold"), (2012.9, 2018.9, "Cassandra y TAO", "navy"), (2018.9, 2026, "EE. UU. y Europa", "teal")]),
         ("Runtime", [(2022.3, 2022.5, "", "coral"), (2023.6, 2023.8, "", "coral")])],
        unit="año", events=[(2010.77, "lanzamiento"), (2012.62, "compra"), (2013.15, "100 M mensuales"), (2023.5, "Threads")],
        t_max=2027, ticks=[2010, 2013, 2016, 2019, 2022, 2025, 2027], lane_h=46,
        note="Hechos con fuente: lanzamiento el 6 de octubre de 2010 (TechCrunch 2012); compra completada en agosto de 2012 (10-K de Facebook); 100 millones de usuarios mensuales en febrero de 2013 (TechCrunch 2013); Cinder y objetos inmortales (Engineering at Meta). Dónde deja de valer: las fechas de las etapas de infraestructura son aproximadas, no hay fecha publicada de cada cambio.",
        foot="Fuentes: 10-K de Facebook 2012, TechCrunch (2012 y 2013) y Engineering at Meta."))


def especiales():
    return case_cards(
        "Casos especiales documentados y cómo se resuelven",
        "Cinco tarjetas: unos 25 fotos y 90 me gusta por segundo en 2011, identificadores únicos en muchas bases, recuperación ante desastres entre continentes, memoria compartida que se copia al escribir y lanzamiento de una aplicación con dos días de preaviso.",
        [("Más de 25 fotos y 90 me gusta por segundo (2011)", "Fragmentar PostgreSQL en fragmentos lógicos", "Sirve para que los datos quepan en memoria; coste: generar identificadores únicos.", "teal"),
         ("Insertar en muchas bases a la vez", "Identificadores de 64 bits con hora, fragmento y secuencia", "Sin servicio nuevo; atado al esquema de fragmentación elegido.", "teal"),
         ("Datos de usuarios de Europa con latencia transatlántica", "Partir Cassandra con Akkio y escribir TAO en maestros locales", "Evita consultas de quórum a través del océano; cambia la recuperación ante desastres.", "gold"),
         ("Procesos pre-bifurcados que copian memoria", "Objetos inmortales", "El recuento de referencias deja de escribir en objetos que no cambian.", "teal"),
         ("Lanzar Threads con dos días de aviso", "Capacidad elástica y trabajos asíncronos", "Se apoya en infraestructura madura; no es transferible sin ella.", "gold")],
        note="Cada tarjeta enlaza un hecho citado con el mecanismo. Color: coral falla, teal se sostiene, gold depende. Dónde deja de valer: son casos documentados, no exhaustivos.",
        foot=ENG)


def alternativas():
    return case_cards(
        "Alternativas que Instagram no tomó, como análisis del curso",
        "Cuatro tarjetas: pasar a una base NoSQL en lugar de fragmentar PostgreSQL, reescribir en otro lenguaje en lugar de optimizar Python, mantener una infraestructura independiente de Facebook y duplicar todos los datos en cada continente.",
        [("Cambiar a una base NoSQL en 2011", "Se evaluaron varias y se eligió PostgreSQL fragmentado", "Documentado: la solución que mejor encajaba era fragmentar PostgreSQL.", "teal"),
         ("Reescribir el servidor web en otro lenguaje", "Optimizar Python: Cinder, objetos inmortales", "Documentado: se invirtió en el runtime de Django; la razón de no reescribir no se declara.", "gold"),
         ("Mantener la infraestructura independiente en AWS", "Migrar a los centros de datos de Meta", "Documentado el hecho; no se publican los costes ni el razonamiento.", "gold"),
         ("Copiar todos los datos en cada continente", "Partir por proximidad con Akkio", "Documentado: copiar habría desperdiciado almacenamiento y puesto quórums a través del océano.", "teal")],
        note="Rótulo: análisis propio. Solo la primera y la cuarta tienen razones explícitas en las fuentes; la segunda y la tercera son inferencias del curso. Dónde deja de valer: Instagram no publica evaluaciones completas de alternativas.",
        foot=ENG)


def hardware():
    return layer_stack(
        "Hardware y software que Instagram hace público",
        "Pila: sin hardware propio descrito más allá de los centros de datos de Meta; software documentado con Django y Python, PostgreSQL, Cassandra, TAO, Memcached, Celery, y un runtime de Python modificado (Cinder).",
        [("Hardware", "Centros de datos de Meta en Estados Unidos y Europa; hasta la compra, servidores en AWS", "grey"),
         ("Capacidad", "Escalado automático por rendimiento sobre un grupo elástico compartido de servidores", "plain"),
         ("Runtime", "CPython modificado (Cinder) con JIT, caché en línea y objetos inmortales", "plain"),
         ("Aplicación", "Django con procesos pre-bifurcados y asyncio por proceso", "plain"),
         ("Datos", "Cassandra, TAO, Memcached; PostgreSQL en la etapa inicial; Celery para trabajos", "gold")],
        [("Documentado en posts de 2012 a 2023", "teal"), ("No se sabe: tipos de servidor, cifras de flota y costes", "grey")],
        "El post de escalado automático de 2020 describe que el servicio Django de Instagram se dimensiona sobre un grupo elástico para usar el hardware con más eficiencia. Dónde deja de valer: no hay números de servidores ni de capacidad.",
        ENG)


def pruebas_fallo():
    return case_cards(
        "Temas a prueba de fallos que Instagram documenta",
        "Cuatro mecanismos con veredicto: nivel web sin estado, holgura de 20 por ciento por región para perder un centro de datos, datos partidos por proximidad con maestros locales y trabajos asíncronos para operaciones costosas.",
        [("Cae un servidor web", "Nivel Django sin estado, reemplazable", "Los datos viven detrás en almacenes replicados.", "teal"),
         ("Cae un centro de datos", "Cada región conserva 20 % de holgura para absorber su carga", "No hay recuperación entre océanos: latencia y datos distintos.", "gold"),
         ("Un maestro de TAO queda lejos", "Maestro de escritura local en Europa", "Evita escrituras a través del Atlántico.", "teal"),
         ("Una operación costosa en el alta", "Trabajo asíncrono", "El usuario no espera; se acepta un retraso de segundos a horas.", "teal")],
        note="Documentado en la charla de LISA 2018 (InfoQ) y en el post de Threads (2023). Dónde deja de valer: la holgura de 20 % es de 2018.",
        foot=ENG)


FIGURES = {
    "instagram-contexto.svg": contexto,
    "instagram-precio-de-la-compra.svg": precio,
    "instagram-ingresos-de-meta.svg": ingresos_meta,
    "instagram-personas-de-la-familia.svg": personas,
    "instagram-reparto-del-ingreso-de-meta.svg": costos,
    "instagram-actores-e-incentivos.svg": actores,
    "instagram-recorridos-de-usuario.svg": recorridos,
    "instagram-esquema-del-negocio.svg": negocio,
    "instagram-capas.svg": capas,
    "instagram-anatomia-del-identificador.svg": bits,
    "instagram-fragmentos-logicos.svg": fragmentos,
    "instagram-generar-identificadores.svg": alternativas_id,
    "instagram-dos-continentes.svg": continentes,
    "instagram-evolucion-de-la-infraestructura.svg": evolucion,
    "instagram-objetos-inmortales.svg": inmortales,
    "instagram-threads-sobre-instagram.svg": threads,
    "instagram-linea-de-tiempo.svg": linea,
    "instagram-casos-especiales.svg": especiales,
    "instagram-alternativas.svg": alternativas,
    "instagram-hardware-y-software.svg": hardware,
    "instagram-a-prueba-de-fallos.svg": pruebas_fallo,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys

    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
