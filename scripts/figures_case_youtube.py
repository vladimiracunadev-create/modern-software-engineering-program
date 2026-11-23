"""Figuras del caso de estudio YouTube (casos/exito/youtube.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Las cifras salen de los 10-K de Alphabet (2023 y 2025) y de Google (2006), del comunicado de Google de
2006, de la documentación de Vitess, de dos trabajos de investigación de Google y de la ayuda de YouTube;
cada pie de figura nombra su fuente. Ninguna figura repite una tabla del caso.
"""
from __future__ import annotations

from case_diagrams import canvas, finish, lane_steps, sequence, years
from case_fig_helpers import hub, layer_stack
from figure_cases import case_cards
from figure_kit import grouped_bars, timeline
from figures_part45_a import flow

ALPH = "Fuente: 10-K de Alphabet de los años 2023 y 2025 (SEC), consulta 2026-11-23."
G06 = "Fuente: 10-K de Google del año 2006 (SEC) y comunicado de Google del 9 de octubre de 2006, consulta 2026-11-23."
ENG = "Fuentes: documentación de Vitess, publicaciones de Google Research y ayuda de YouTube (consulta 2026-11-23). Esquema del autor."


def contexto():
    return hub(
        "YouTube entre creadores, espectadores, anunciantes y titulares de derechos",
        "Diagrama de contexto: los creadores suben vídeos; los espectadores los ven y los comparten; los anunciantes pagan por mostrar anuncios; los suscriptores pagan por servicios como Premium o Music; los titulares de derechos usan Content ID para bloquear, monetizar o seguir sus obras; Alphabet aporta infraestructura y es la matriz.",
        ("YouTube: vídeo subido por cualquiera, visto por casi todos", "navy"),
        [("Creadores: suben vídeos y gestionan canales", "teal", "suben"),
         ("Espectadores: ven, buscan y reciben recomendaciones", "teal", "ven"),
         ("Anunciantes: compran anuncios en los vídeos", "gold", "pagan"),
         ("Suscriptores: Premium, Music, TV y Sunday Ticket", "gold", "pagan"),
         ("Titulares de derechos: Content ID para sus obras", "plain", "reclaman"),
         ("Alphabet: matriz; infraestructura de Google", "plain", "aloja"),
         ("Familias y reguladores: seguridad, menores, derechos", "coral", "exigen"),
         ("Competidores: otras plataformas de vídeo y de streaming", "grey", "disputan")],
        "Documentado: el 10-K de Alphabet de 2025 separa los ingresos de YouTube en anuncios y, dentro de «suscripciones, plataformas y dispositivos», en servicios de suscripción como YouTube TV, Music, Premium y NFL Sunday Ticket; la ayuda de YouTube describe Content ID. Dónde deja de valer: Alphabet no publica usuarios ni horas de vídeo en el 10-K.",
        ALPH)


def ingresos():
    return years(grouped_bars(
        "Ingresos por anuncios de YouTube, 2021 a 2025",
        "Barras en millones de dólares: 28 845 en 2021, 29 243 en 2022, 31 510 en 2023, 36 147 en 2024 y 40 367 en 2025; el crecimiento fue de 1 por ciento en 2022 y de 12 por ciento en 2025.",
        ["2021", "2022", "2023", "2024", "2025"],
        [("Anuncios de YouTube (millones de USD)", [28845, 29243, 31510, 36147, 40367], "coral")],
        unit="millones de USD", decimals=0, plot_h=250,
        note="Cálculo propio de crecimiento: 2022 sobre 2021, 1,4 %; 2023, 7,8 %; 2024, 14,7 %; 2025, 11,7 %. Mire el estancamiento de 2022 y la recuperación posterior. Dónde deja de valer: es solo la línea de anuncios; las suscripciones de YouTube están dentro de otra partida de Alphabet que no se separa.",
        foot=ALPH))


def composicion():
    return grouped_bars(
        "De qué se componen los ingresos de Alphabet en 2025, con YouTube dentro",
        "Barras horizontales en millones de dólares: búsqueda y otros 224 532, nube 58 705, suscripciones, plataformas y dispositivos 48 030, anuncios de YouTube 40 367, red de Google 29 792 y otras apuestas 1 537; los ingresos totales fueron 402 836 millones.",
        ["Búsqueda y otros", "Nube", "Suscripciones, plataformas y dispositivos", "Anuncios de YouTube", "Red de Google", "Otras apuestas"],
        [("Millones de USD, 2025", [224532, 58705, 48030, 40367, 29792, 1537], "navy")],
        unit="millones de USD", horizontal=True, decimals=0, plot_h=300,
        note="Cálculo propio: los anuncios de YouTube son 10,0 % de los 402 836 millones de Alphabet (40 367 sobre 402 836). La partida de suscripciones incluye también Google One, Google Play y dispositivos Pixel, de modo que no equivale a las suscripciones de YouTube. Dónde deja de valer: no hay ingreso total de YouTube.",
        foot=ALPH)


def crecimiento():
    return grouped_bars(
        "Crecimiento de cada línea de ingresos de Alphabet de 2024 a 2025",
        "Barras con el crecimiento porcentual: búsqueda y otros 13,4, anuncios de YouTube 11,7, red de Google menos 1,9, suscripciones, plataformas y dispositivos 19,1 y nube 35,8 por ciento.",
        ["Búsqueda y otros", "Anuncios de YouTube", "Red de Google", "Suscripciones, plataformas y dispositivos", "Nube"],
        [("Crecimiento 2025 sobre 2024 (%)", [13.4, 11.7, -1.9, 19.1, 35.8], "teal")],
        unit="% de crecimiento", horizontal=True, decimals=1, plot_h=260,
        note="Cálculo propio sobre los 10-K: 224 532 sobre 198 084; 40 367 sobre 36 147; 29 792 sobre 30 359; 48 030 sobre 40 340 y 58 705 sobre 43 229. El 10-K atribuye el aumento de YouTube a los productos de respuesta directa y de marca. Dónde deja de valer: son porcentajes sobre bases muy distintas.",
        foot=ALPH)


def precio():
    return grouped_bars(
        "Tres formas de contar lo que costó YouTube",
        "Barras en millones de dólares: 1 650 millones anunciados en octubre de 2006, 1 194 millones de precio contable al cerrar la compra en noviembre de 2006 y 564,5 millones adicionales en compensación diferida a empleados que se reconoce con el tiempo.",
        ["Anunciado (oct. 2006)", "Precio contable (nov. 2006)", "Compensación diferida a empleados"],
        [("Millones de USD", [1650, 1194, 564.5], "navy")],
        unit="millones de USD", decimals=1, plot_h=240,
        note="El comunicado de Google habla de 1 650 millones en acciones; el 10-K de 2006 da un precio de 1 194 millones (21,2 en efectivo y 1 173 en acciones y opciones), más 564,5 millones en acciones sujetas a permanencia. Cálculo propio: 1 194 + 564,5 son 1 758,5, no 1 650: miden cosas distintas y con cotizaciones de fechas distintas. Dónde deja de valer: el valor de las acciones cambia con la cotización.",
        foot=G06)


def asignacion():
    return grouped_bars(
        "A qué se asignó el precio contable de YouTube",
        "Barras en miles de dólares con la asignación del precio de 1 194 millones: fondo de comercio 1 134 687, marca y contratos 153 000, patentes y tecnología 24 000, pasivos netos asumidos menos 45 027 e impuestos diferidos menos 72 240.",
        ["Fondo de comercio", "Marca, contratos y otros", "Patentes y tecnología", "Pasivos netos asumidos", "Impuestos diferidos"],
        [("Miles de USD", [1134687, 153000, 24000, -45027, -72240], "teal")],
        unit="miles de USD", decimals=0, plot_h=250, horizontal=True,
        note="Cálculo propio: el fondo de comercio es 95 % del precio (1 134 687 sobre 1 194 420). Es decir, Google pagó por la audiencia y el equipo, no por tecnología identificable: las patentes y la tecnología desarrollada valían 24 millones. Dónde deja de valer: el reparto contable no mide el valor estratégico.",
        foot=G06)


def actores():
    return hub(
        "Quién obtiene qué en el ecosistema de YouTube",
        "Diagrama de incentivos: los espectadores obtienen vídeo gratis y recomendado; los creadores audiencia y la posibilidad de ganar dinero; los anunciantes atención; los titulares de derechos una forma de reclamar; YouTube y Alphabet ingresos por anuncios y suscripciones.",
        ("YouTube: reunir audiencia y venderla con anuncios y suscripciones", "navy"),
        [("Espectador: ve gratis con anuncios o paga por quitarlos", "teal", "gana"),
         ("Creador: audiencia y, si cumple umbrales, ingresos", "teal", "gana"),
         ("Anunciante: alcance en vídeo", "gold", "paga"),
         ("Suscriptor: sin anuncios, música y televisión", "gold", "paga"),
         ("Titular de derechos: bloquea, monetiza o sigue", "plain", "decide"),
         ("Alphabet: integra con anuncios y nube", "plain", "monetiza"),
         ("Regulador y familias: menores, desinformación", "coral", "exigen"),
         ("Competidor: otras plataformas", "grey", "disputa")],
        "Análisis propio sobre hechos documentados: los umbrales de monetización de creadores (1 000 suscriptores con 4 000 horas de visualización o con 10 millones de vistas de Shorts) y Content ID son los dos mecanismos públicos que ordenan los incentivos. Dónde deja de valer: el reparto de ingresos entre creadores y YouTube no figura en las fuentes consultadas.",
        ENG)


def recorridos():
    f = canvas("Cuatro recorridos en YouTube y su caso límite",
               "Cuatro filas de pasos: un espectador que busca un vídeo, un creador que sube y monetiza, un titular de derechos que usa Content ID y una familia que usa una cuenta supervisada; cada fila termina en un caso límite.")
    y = 56.0
    y = lane_steps(f, y, "Espectador", [("Abre la página de inicio", "teal"), ("Ve recomendaciones y suscripciones", "teal"), ("Reproduce un vídeo", "teal"), ("Emisión en directo con millones a la vez", "coral")])
    y = lane_steps(f, y, "Creador", [("Sube un vídeo", "gold"), ("YouTube lo procesa en varios formatos", "gold"), ("Cumple los umbrales de monetización", "gold"), ("Reclamo de derechos sobre su vídeo", "coral")])
    y = lane_steps(f, y, "Titular de derechos", [("Entrega archivos de referencia", "navy"), ("Content ID escanea cada subida", "navy"), ("Elige bloquear, monetizar o seguir", "navy"), ("Reclamo erróneo y disputa", "coral")])
    y = lane_steps(f, y, "Familia", [("Crea una cuenta supervisada", "plain"), ("Define límites de contenido", "plain"), ("El menor ve contenido filtrado", "plain"), ("Un vídeo inadecuado pasa el filtro", "coral")])
    return finish(f, y + 4, "Cada fila se lee de izquierda a derecha y la caja coral es el borde. Los pasos de Content ID y los umbrales de monetización salen de la ayuda de YouTube; el procesamiento en varios formatos, del trabajo sobre aceleración de vídeo; los bordes del espectador y la familia son escenarios del curso. Dónde deja de valer: no mide frecuencia de cada borde.", "Esquema del autor sobre la ayuda de YouTube y los trabajos de Google Research.")


def negocio():
    return flow(
        "Cómo gana dinero YouTube según lo que Alphabet publica",
        "Flujo del negocio: los creadores y los titulares de derechos aportan vídeo; los espectadores aportan atención; los anunciantes pagan 40 367 millones de dólares en 2025; los suscriptores pagan por servicios de YouTube que están dentro de una partida mayor de suscripciones; el reparto con los creadores no se publica.",
        [[("Creadores y titulares de derechos aportan vídeo", "teal"), ("Espectadores aportan atención", "teal"), ("Anuncios: 40 367 millones de USD en 2025", "navy"), ("Suscripciones (YouTube TV, Music, Premium): dentro de 48 030 millones", "gold")],
         [("Content ID: bloquear, monetizar o seguir", "plain"), ("Reparto con creadores: no publicado", "grey"), ("Costes de infraestructura: no publicados", "grey"), ("Beneficio de YouTube: no publicado", "grey")]],
        note="Documentado: la partida de anuncios y la descripción de las suscripciones. No se sabe: el beneficio, el reparto con creadores y los costes de YouTube; Alphabet no los separa. Dónde deja de valer: cualquier cifra de beneficio de YouTube que circule no tiene fuente primaria aquí.",
        foot=ALPH, width=960)


def capas():
    return layer_stack(
        "Capas de YouTube que sus fuentes públicas describen",
        "Pila de capas: clientes en web, móvil y televisión; recomendación con dos etapas de redes neuronales; procesamiento de vídeo con aceleradores propios; servicios con bases de datos MySQL servidas por Vitess; infraestructura de Google.",
        [("Clientes", "Web, móvil, televisión y consolas; inicio, Siguiente y búsqueda", "teal"),
         ("Recomendación", "Generación de candidatos y ordenación con aprendizaje profundo", "plain"),
         ("Procesamiento de vídeo", "Transcodificación en un centro de datos con unidades de codificación de vídeo propias", "gold"),
         ("Datos", "MySQL con Vitess: proxy que enruta consultas y fragmenta", "plain"),
         ("Infraestructura", "Centros de datos de Google; TPU y aceleradores de Alphabet", "navy")],
        [("Documentado en trabajos de 2016 y 2021 y en la documentación de Vitess", "teal"), ("No se sabe: almacenamiento y entrega de vídeo, red de contenidos", "grey"), ("Inferido: el resto de piezas reutiliza la infraestructura de Google", "grey")],
        "Documentado en la documentación de Vitess (origen en YouTube), el trabajo de recomendaciones de 2016 y el de aceleración de vídeo de 2021. Dónde deja de valer: no hay fuentes públicas sobre almacenamiento ni distribución de vídeo en las consultadas.",
        ENG)


def subida():
    return sequence(
        "De subir un vídeo a reproducirlo, con lo documentado y lo inferido",
        "Secuencia de una subida: el creador sube el vídeo; el sistema escanea con Content ID; el vídeo se transcodifica a varios formatos en aceleradores de vídeo; se indexa y entra al sistema de recomendación; el espectador recibe recomendaciones y reproduce el formato adecuado.",
        ["Creador", "Subida y Content ID", "Transcodificación", "Recomendación", "Espectador"],
        [(0, 1, "sube el vídeo", ""), (1, 1, "Content ID lo escanea contra los archivos de referencia", ""),
         (1, 2, "pide procesarlo", "dashed"), (2, 3, "vídeo listo en varios formatos", "dashed"),
         (3, 4, "lo recomienda según el comportamiento del espectador", ""), (4, 2, "pide el formato adecuado a su conexión", "dashed")],
        "Documentado: Content ID escanea toda subida; la transcodificación a escala usa aceleradores; la recomendación usa dos etapas. Inferido (trazo punteado): el orden y la forma exacta de cada paso. Dónde deja de valer: omite almacenamiento, entrega, moderación y subtítulos.",
        ENG)


def vitess():
    return flow(
        "De un MySQL a Vitess: lo que YouTube hizo cuando su base de datos se saturó",
        "Flujo de cinco pasos: una sola base MySQL llega al límite; se separa una primaria para escritura y una réplica para lectura; se añaden réplicas; las escrituras saturan la primaria y se fragmenta; Vitess saca de la aplicación la lógica de elegir fragmento con un proxy.",
        [[("Una base MySQL se acerca al límite de tráfico", "coral"), ("Primaria para escribir y réplica para leer", "plain"), ("Más réplicas: alivio temporal", "plain")],
         [("Las escrituras saturan la primaria: hay que fragmentar", "coral"), ("La aplicación elegía el fragmento: lógica en el código", "gold"), ("Vitess: un proxy enruta y gestiona las consultas", "teal")]],
        note="Documentado en la historia de Vitess: se creó en 2010 para resolver los problemas de escala de MySQL en YouTube y, desde entonces, YouTube multiplicó su base de usuarios por más de 50. Vitess fue aceptado como proyecto de la CNCF en febrero de 2018 y se graduó en noviembre de 2019. Dónde deja de valer: la historia es la que cuenta el propio proyecto.",
        foot="Fuente: documentación de Vitess, «History», vitess.io, consulta 2026-11-23.", width=960)


def vcu():
    return flow(
        "Transcodificar vídeo a escala de centro de datos: de CPU a una unidad de codificación propia",
        "Flujo del trabajo de Google Research: el vídeo es la mayor parte del tráfico de Internet; el procesamiento de vídeo exige cada vez más cómputo mientras la ley de Moore se ralentiza; Google diseñó una unidad de codificación de vídeo y un sistema alrededor de ella; las pruebas en producción dieron entre 20 y 33 veces más eficiencia.",
        [[("El vídeo es la mayor parte del tráfico de Internet", "plain"), ("La ley de Moore se ralentiza", "coral"), ("Hace falta hardware especializado", "gold")],
         [("Unidad de codificación de vídeo (VCU) y sistema a medida", "teal"), ("Evaluada con trabajos reales en producción", "teal"), ("De 20 a 33 veces más eficiencia que la base sin aceleración", "navy")]],
        note="Documentado en «Warehouse-Scale Video Acceleration» (ASPLOS 2021), cuyo resumen afirma que es el primer trabajo que discute la aceleración de vídeo a escala de almacén y que el diseño mejora también la gestión de fallos. Dónde deja de valer: el trabajo es de Google Research y evalúa su propio sistema; la mejora es sobre su propia base anterior.",
        foot="Fuente: Google Research, «Warehouse-Scale Video Acceleration: Co-design and Deployment in the Wild», 2021.", width=960)


def recomendador():
    return flow(
        "El sistema de recomendación de YouTube en dos etapas",
        "Flujo de dos etapas: la generación de candidatos reduce un enorme catálogo a un conjunto manejable de vídeos con un modelo profundo; la ordenación puntúa esos candidatos con otro modelo profundo y elige los que se muestran en la página de inicio y en el panel de Siguiente.",
        [[("Catálogo enorme de vídeos", "plain"), ("Generación de candidatos con un modelo profundo", "teal"), ("Conjunto manejable de candidatos relevantes", "teal")],
         [("Ordenación con otro modelo profundo", "teal"), ("Página de inicio y panel Siguiente", "gold"), ("Comportamiento, suscripciones y satisfacción como señales", "gold")]],
        note="Documentado en «Deep Neural Networks for YouTube Recommendations» (2016), que describe un sistema en dos etapas, y en la página «Cómo funciona YouTube», que cita la página de inicio y el panel de Siguiente y las señales de comportamiento, gustos, suscripciones y encuestas de satisfacción. Dónde deja de valer: el trabajo describe el diseño de 2016; el sistema actual no se describe.",
        foot="Fuentes: Google Research (2016) y YouTube, «How YouTube Works».", width=960)


def contentid():
    return flow(
        "Content ID: de la subida a la acción del titular de derechos",
        "Flujo de Content ID: los titulares de derechos entregan archivos de audio y vídeo de referencia; cada vídeo subido se escanea automáticamente; si hay coincidencia se crea un reclamo; según los ajustes del titular el vídeo se bloquea, se monetiza con anuncios o se rastrea, y cada acción puede variar por país.",
        [[("Titular con derechos exclusivos sobre un cuerpo sustancial de obras", "teal"), ("Entrega archivos de referencia", "teal"), ("Cada subida se escanea de forma automática", "gold")],
         [("Coincidencia: reclamo de Content ID", "coral"), ("Bloquear, monetizar o rastrear según el titular", "navy"), ("Puede variar por país; el creador puede disputar", "gold")]],
        note="Documentado en la ayuda de YouTube: quien reclama erróneamente de forma repetida puede perder el acceso a Content ID. Dónde deja de valer: la ayuda no publica tasas de coincidencia ni de error.",
        foot=ENG, width=960)


def monetizacion():
    return hub(
        "Umbrales para que un creador entre en el programa de socios de YouTube",
        "Esquema de los umbrales: 1 000 suscriptores y 4 000 horas de visualización cualificadas en los últimos 12 meses, o 1 000 suscriptores y 10 millones de vistas cualificadas de Shorts en los últimos 90 días; las horas de Shorts pueden contar.",
        ("Programa de socios de YouTube", "navy"),
        [("1 000 suscriptores", "teal", "y además"),
         ("4 000 horas de visualización cualificadas en 12 meses", "teal", "o bien"),
         ("10 millones de vistas de Shorts en 90 días", "gold", "alternativa"),
         ("Revisión y aprobación por YouTube", "plain", "después"),
         ("Aviso por correo al alcanzar el umbral", "plain", "se informa")],
        "Documentado en la ayuda de YouTube: son los umbrales de elegibilidad vigentes en la fecha de consulta; pueden cambiar. Dónde deja de valer: no se publica el porcentaje del ingreso que recibe el creador en las fuentes consultadas.",
        "Fuente: ayuda de YouTube, programa de socios, consulta 2026-11-23.")


def linea():
    return years(timeline(
        "YouTube de 2005 a 2026: compra, infraestructura e investigación",
        "Línea de tiempo con tres carriles: empresa (fundada en febrero de 2005, adquirida por Google, anunciada el 9 de octubre de 2006 y cerrada en noviembre de 2006), datos (Vitess nace en 2010; CNCF en 2018 y 2019) y sistemas (recomendación en 2016 y aceleración de vídeo en 2021).",
        [("Empresa", [(2005.1, 2006.85, "", "grey"), (2006.85, 2026, "Parte de Google y de Alphabet", "teal")]),
         ("Datos", [(2010, 2026, "Vitess nace en YouTube y llega a la CNCF", "navy")]),
         ("Sistemas", [(2016.6, 2016.8, "", "coral"), (2021.1, 2021.3, "", "coral")])],
        unit="año", events=[(2005.1, "fundación"), (2006.85, "compra"), (2016.7, "recomendación"), (2021.2, "VCU")],
        t_max=2027, ticks=[2005, 2009, 2013, 2017, 2021, 2025, 2027], lane_h=46,
        note="Hechos con fuente: fundada en febrero de 2005 y compra anunciada el 9 de octubre de 2006 por 1 650 millones en acciones (comunicado de Google), cerrada en noviembre de 2006 (10-K de Google); Vitess creado en 2010 y graduado de la CNCF en noviembre de 2019; trabajos de investigación de 2016 y 2021. Dónde deja de valer: los marcadores de sistemas son fechas de publicación, no de despliegue.",
        foot="Fuentes: comunicado y 10-K de Google (2006), documentación de Vitess y Google Research."))


def especiales():
    return case_cards(
        "Casos especiales documentados y cómo se resuelven",
        "Cinco tarjetas: una base de datos que no aguanta las escrituras, procesamiento de vídeo que consume demasiada CPU, miles de millones de vídeos de los que recomendar, obras con derechos de terceros y creadores que aún no cumplen los umbrales; cada una con su mecanismo y veredicto.",
        [("Las escrituras saturan la base MySQL", "Fragmentar con Vitess, que enruta las consultas", "La lógica de elegir fragmento sale del código de la aplicación.", "teal"),
         ("Procesar vídeo a escala consume demasiada CPU", "Unidad de codificación de vídeo en hardware propio", "De 20 a 33 veces más eficiencia medida por Google.", "teal"),
         ("Un catálogo enorme para recomendar", "Dos etapas: candidatos y ordenación", "El modelo ordena pocos candidatos en vez de todo el catálogo.", "teal"),
         ("Vídeos con obras de terceros", "Content ID escanea y deja decidir al titular", "Los reclamos erróneos y las disputas siguen existiendo.", "gold"),
         ("Creadores que no llegan al umbral", "Se les exigen horas de visualización o vistas de Shorts", "Un umbral filtra el pago pero también la entrada.", "gold")],
        note="Cada tarjeta enlaza un hecho citado con el mecanismo. Color: coral falla, teal se sostiene, gold depende. Dónde deja de valer: los casos de moderación, desinformación y seguridad de menores no se cubren por falta de fuentes técnicas consultadas.",
        foot=ENG)


def alternativas():
    return case_cards(
        "Alternativas que YouTube no tomó o sustituyó, como análisis del curso",
        "Cuatro tarjetas: seguir con una sola base MySQL, fragmentar en la aplicación, transcodificar solo con CPU y recomendar con reglas manuales; cada una con lo que YouTube o Google documentan.",
        [("Seguir con un solo MySQL", "Primaria y réplicas, y luego fragmentación", "Documentado: alivios temporales hasta que el tráfico de escritura obligó a fragmentar.", "teal"),
         ("Fragmentar dentro de la aplicación", "Vitess como proxy", "Documentado: sacó esa lógica del código fuente de la aplicación.", "teal"),
         ("Transcodificar solo con CPU", "VCU", "Documentado: la ley de Moore se ralentiza y el vídeo domina el tráfico.", "teal"),
         ("Recomendar por reglas", "Aprendizaje profundo en dos etapas", "Documentado el sistema; la razón de abandonar las reglas no figura.", "gold")],
        note="Rótulo: documentado en la historia de Vitess y en los trabajos de investigación. Dónde deja de valer: las razones de las dos últimas decisiones son inferencias del curso.",
        foot=ENG)


def hardware():
    return layer_stack(
        "Hardware y software que YouTube hace público",
        "Pila: centros de datos de Google; aceleradores de vídeo propios (VCU) y TPU de Alphabet; MySQL con Vitess; modelos de aprendizaje profundo para recomendar; Content ID para identificar obras.",
        [("Hardware", "Centros de datos de Google; unidades de codificación de vídeo propias; TPU de Alphabet", "grey"),
         ("Datos", "MySQL servido por Vitess, un proyecto abierto nacido en YouTube", "gold"),
         ("Vídeo", "Transcodificación acelerada por hardware", "plain"),
         ("Recomendación y derechos", "Aprendizaje profundo para recomendar; Content ID para identificar obras con archivos de referencia", "plain")],
        [("Documentado entre 2010 y 2025", "teal"), ("No se sabe: tamaño de la flota, red de entrega y almacenamiento de vídeo", "grey")],
        "El 10-K de 2025 describe los TPU propios de Alphabet y sus centros de datos; los trabajos de Google Research describen la VCU y la recomendación. Dónde deja de valer: el uso concreto de TPU por YouTube no se detalla en las fuentes consultadas.",
        ENG)


def pruebas_fallo():
    return case_cards(
        "Temas a prueba de fallos que las fuentes de YouTube documentan",
        "Cuatro mecanismos con veredicto: réplicas de lectura frente a una primaria única, fragmentación y proxy para escalar escrituras, gestión de fallos mejorada por el diseño del acelerador y control de usos erróneos de Content ID.",
        [("Una primaria saturada de lecturas", "Réplicas de lectura", "Alivio temporal que llegó a saturarse.", "gold"),
         ("Las escrituras superan una sola base", "Fragmentación detrás de un proxy", "Escala, a costa de enrutar y gestionar fragmentos.", "teal"),
         ("Fallos en el procesamiento de vídeo", "Diseño del acelerador que mejora la gestión de fallos", "Lo afirma el resumen del trabajo de 2021.", "teal"),
         ("Reclamos erróneos de derechos", "Pérdida del acceso a Content ID si se repiten", "Un control de abuso del propio sistema de control.", "gold")],
        note="Documentado en la historia de Vitess, el resumen del trabajo de 2021 y la ayuda de YouTube. Dónde deja de valer: no hay posmortems públicos de caídas de YouTube en las fuentes consultadas.",
        foot=ENG)


FIGURES = {
    "youtube-contexto.svg": contexto,
    "youtube-ingresos-por-anuncios.svg": ingresos,
    "youtube-dentro-de-alphabet.svg": composicion,
    "youtube-crecimiento-por-linea.svg": crecimiento,
    "youtube-precio-de-la-compra.svg": precio,
    "youtube-asignacion-del-precio.svg": asignacion,
    "youtube-actores-e-incentivos.svg": actores,
    "youtube-recorridos-de-usuario.svg": recorridos,
    "youtube-esquema-del-negocio.svg": negocio,
    "youtube-capas.svg": capas,
    "youtube-secuencia-de-una-subida.svg": subida,
    "youtube-origen-de-vitess.svg": vitess,
    "youtube-aceleracion-de-video.svg": vcu,
    "youtube-recomendacion-en-dos-etapas.svg": recomendador,
    "youtube-content-id.svg": contentid,
    "youtube-umbrales-de-monetizacion.svg": monetizacion,
    "youtube-linea-de-tiempo.svg": linea,
    "youtube-casos-especiales.svg": especiales,
    "youtube-alternativas.svg": alternativas,
    "youtube-hardware-y-software.svg": hardware,
    "youtube-a-prueba-de-fallos.svg": pruebas_fallo,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys

    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
