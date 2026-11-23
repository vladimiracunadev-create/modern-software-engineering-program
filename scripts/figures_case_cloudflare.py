"""Figuras del caso de estudio Cloudflare (casos/exito/cloudflare.md).

Contrato igual que scripts/figures_part*_a.py: ``FIGURES`` mapea nombre de archivo -> constructor.
Las cifras salen del 10-K de 2025 y del prospecto de 2019 de Cloudflare (SEC) y de su blog técnico; cada
pie de figura nombra su fuente. Ninguna figura repite una tabla del caso.
"""
from __future__ import annotations

from case_diagrams import canvas, finish, lane_steps, sequence, years
from case_fig_helpers import hub, layer_stack
from figure_cases import case_cards
from figure_kit import grouped_bars, line_chart, timeline
from figures_part45_a import flow

TENK = "Fuente: 10-K de Cloudflare del año terminado el 31 de diciembre de 2025 (SEC), consulta 2026-11-23."
BLOG = "Fuente: blog de Cloudflare (blog.cloudflare.com), consulta 2026-11-23. Esquema del autor."


def contexto():
    return hub(
        "Cloudflare entre los sitios, los usuarios y el resto de Internet",
        "Diagrama de contexto: los clientes ponen sus sitios y aplicaciones detrás de la red de Cloudflare; los usuarios finales llegan a ella en vez de al origen; la red se interconecta con proveedores de acceso y nubes; los desarrolladores ejecutan código en ella; los atacantes la prueban con ataques de denegación de servicio.",
        ("Cloudflare: red global entre usuarios y orígenes", "navy"),
        [("Clientes: sitios y aplicaciones, de gratis a grandes empresas", "teal", "contratan"),
         ("Usuarios finales: llegan por la red más cercana", "teal", "visitan"),
         ("Desarrolladores: Workers, almacenamiento y datos", "gold", "programan"),
         ("Proveedores de acceso, nubes y empresas: más de 13 000 redes", "plain", "se interconectan"),
         ("Servidores de origen del cliente", "plain", "proxy hacia"),
         ("Atacantes: botnets y ataques volumétricos", "coral", "atacan"),
         ("Reguladores y gobiernos: privacidad y soberanía de datos", "coral", "exigen"),
         ("Competidores: otras redes de distribución y de seguridad", "grey", "disputan")],
        "Documentado en el 10-K de 2025: la red cubre más de 330 ciudades en más de 125 países y se interconecta con más de 13 000 redes, incluidos proveedores de acceso, nubes y empresas. Dónde deja de valer: no muestra volúmenes de tráfico por actor.",
        TENK)


def ingresos():
    return years(grouped_bars(
        "Ingresos de Cloudflare, 2023 a 2025",
        "Barras con 1 296,7 millones de dólares en 2023, 1 669,6 millones en 2024 y 2 167,9 millones en 2025; el crecimiento anual es de 29 por ciento en 2024 y 30 por ciento en 2025.",
        ["2023", "2024", "2025"],
        [("Ingresos (millones de USD)", [1296.7, 1669.6, 2167.9], "teal")],
        unit="millones de USD", decimals=1, plot_h=240,
        note="Cálculo propio de crecimiento: 1 669,6 sobre 1 296,7 es 28,8 % y 2 167,9 sobre 1 669,6 es 29,8 %. Dónde deja de valer: son ingresos de un solo segmento por suscripciones de acceso a la red y a los productos.",
        foot=TENK))


def reparto():
    return grouped_bars(
        "Cómo se reparte cada dólar de ingreso en 2025",
        "Barras horizontales como porcentaje del ingreso de 2 167,9 millones: coste de ingresos 25 por ciento, ventas y marketing 42, investigación y desarrollo 24, administración 18 y pérdida operativa de 10 por ciento.",
        ["Coste de ingresos", "Ventas y marketing", "Investigación y desarrollo", "Administración general", "Pérdida operativa"],
        [("% del ingreso 2025", [25.5, 42.5, 23.6, 18.0, -9.6], "coral")],
        unit="% del ingreso", horizontal=True, decimals=1, plot_h=260,
        note="Cálculo propio sobre el 10-K: 552,5; 920,8; 512,5; 389,3 millones y una pérdida operativa de 207,2 sobre 2 167,9. Mire que el coste de ingresos es solo una cuarta parte, pero ventas y marketing pesan casi el doble que investigación. Dónde deja de valer: los porcentajes incluyen remuneración en acciones.",
        foot=TENK)


def caja():
    return years(grouped_bars(
        "Pérdida neta y flujo de caja libre de Cloudflare, 2023 a 2025",
        "Barras agrupadas en millones de dólares: pérdida neta de 183,9; 78,8 y 102,3 millones y flujo de caja libre positivo de 119,5; 166,9 y 260,6 millones en 2023, 2024 y 2025.",
        ["2023", "2024", "2025"],
        [("Pérdida neta", [183.9, 78.8, 102.3], "coral"), ("Flujo de caja libre", [119.5, 166.9, 260.6], "teal")],
        unit="millones de USD", decimals=1, plot_h=250,
        note="La pérdida es contable (incluye remuneración en acciones y amortizaciones) y el flujo de caja libre es el que el 10-K define como medida no contable: 12 % del ingreso en 2025 frente a 9 % en 2023. Dónde deja de valer: dos medidas distintas; una no sustituye a la otra.",
        foot=TENK))


def clientes():
    return years(line_chart(
        "Clientes de pago de Cloudflare, cierre de 2023 a 2025",
        "Línea con 189 791 clientes de pago al cierre de 2023, 237 714 al de 2024 y 332 466 al de 2025; crecen 40 por ciento en el último año.",
        [("Clientes de pago", [(2023, 189791), (2024, 237714), (2025, 332466)], "teal")],
        x_label="Cierre del año", y_label="Clientes de pago", decimals=0,
        x_ticks=[(2023, "2023"), (2024, "2024"), (2025, "2025")],
        note="Cálculo propio: 332 466 sobre 237 714 es 39,9 %. El 10-K calcula las métricas cada trimestre; esta es la del cuarto trimestre. Dónde deja de valer: «cliente de pago» no distingue entre un plan pequeño y un contrato enorme.",
        foot=TENK))


def grandes():
    return grouped_bars(
        "Clientes grandes y retención neta de dólares",
        "Barras con clientes que pagan más de 100 000 dólares al año: 2 756, 3 497 y 4 298 al cierre de 2023, 2024 y 2025; y la retención neta de dólares del cuarto trimestre: 115, 111 y 120 por ciento.",
        ["Cierre de 2023", "Cierre de 2024", "Cierre de 2025"],
        [("Clientes de más de 100 000 USD (cientos)", [27.56, 34.97, 42.98], "navy"), ("Retención neta de dólares (%)", [115, 111, 120], "gold")],
        unit="cientos de clientes / porcentaje", decimals=1, plot_h=250,
        note="Las dos series comparten eje solo para ver la tendencia (clientes en cientos): los grandes suben 56 % en dos años y la retención, que cayó a 111 %, volvió a 120 %. Dónde deja de valer: la retención excluye clientes nuevos y los gratuitos que pasan a pago.",
        foot=TENK)


def regiones():
    return grouped_bars(
        "Reparto del ingreso de 2025 según la dirección de facturación del cliente",
        "Barras horizontales: 49 por ciento Estados Unidos, 28 por ciento Europa, Oriente Medio y África, 15 por ciento Asia Pacífico y 8 por ciento otras regiones.",
        ["Estados Unidos", "Europa, Oriente Medio y África", "Asia Pacífico", "Otras"],
        [("% del ingreso 2025", [49, 28, 15, 8], "teal")],
        unit="% del ingreso", horizontal=True, decimals=0, plot_h=220,
        note="Estados Unidos baja de 52 % en 2023 a 49 % en 2025 y Asia Pacífico sube de 13 % a 15 %. Dónde deja de valer: es por dirección de facturación, no por dónde está el tráfico.",
        foot=TENK)


def red():
    return grouped_bars(
        "Crecimiento de la red de Cloudflare entre el prospecto de 2019 y el informe de 2025",
        "Barras con ciudades de la red: 194 en 2019 y más de 330 en 2025; los países pasan de más de 90 a más de 125 y las redes interconectadas de más de 8 000 a más de 13 000.",
        ["Ciudades", "Países", "Redes interconectadas (cientos)"],
        [("2019 (prospecto)", [194, 90, 80], "grey"), ("2025 (10-K)", [330, 125, 130], "teal")],
        unit="ciudades, países y cientos de redes", decimals=0, plot_h=250,
        note="Los valores son mínimos («más de»): 2019 informa 194 ciudades, más de 90 países y más de 8 000 redes; 2025, más de 330, más de 125 y más de 13 000. Dónde deja de valer: la tercera categoría está expresada en cientos de redes para compartir escala.",
        foot="Fuentes: prospecto 424B4 de septiembre de 2019 y 10-K de 2025 de Cloudflare (SEC).")


def actores():
    return hub(
        "Quién obtiene qué en el ecosistema de Cloudflare",
        "Diagrama de incentivos: el cliente obtiene velocidad y protección sin operar su propia red; el usuario final páginas más rápidas y seguras; el proveedor de acceso tráfico más barato al interconectarse; el desarrollador un lugar donde ejecutar código; Cloudflare ingresos de suscripciones y la ventaja de escala.",
        ("Cloudflare: la red es el producto; más tráfico mejora la red y el coste", "navy"),
        [("Cliente pequeño: plan gratuito o barato", "teal", "usa"),
         ("Gran empresa: contratos anuales y protección completa", "gold", "paga"),
         ("Usuario final: sitios más rápidos y con menos ataques", "teal", "gana"),
         ("Proveedor de acceso: interconexión que ahorra tránsito", "plain", "se conecta"),
         ("Desarrollador: ejecuta código en toda la red", "plain", "programa"),
         ("Atacante: busca saturar o evadir la protección", "coral", "ataca"),
         ("Regulador: privacidad, soberanía de datos", "coral", "exige"),
         ("Competidor: nubes y redes de distribución", "grey", "disputa")],
        "Documentado en el 10-K: a medida que la red crece, las dinámicas de coste de ancho de banda y de ubicación «se vuelven aún más poderosas», y los clientes usan además la red para construir sus aplicaciones. Dónde deja de valer: el mecanismo económico preciso es lectura del curso sobre ese texto.",
        TENK)


def recorridos():
    f = canvas("Cuatro recorridos en Cloudflare y su caso límite",
               "Cuatro filas de pasos: un sitio pequeño que cambia sus servidores de nombres, una empresa que protege su aplicación, un desarrollador que despliega código en la red y un usuario que visita un sitio durante un ataque o una caída; cada fila termina en un caso límite.")
    y = 56.0
    y = lane_steps(f, y, "Sitio pequeño", [("Crea cuenta y añade el dominio", "teal"), ("Apunta los nombres a Cloudflare", "teal"), ("El tráfico pasa por la red", "teal"), ("Un error propio de Cloudflare se ve como un 5xx del sitio", "coral")])
    y = lane_steps(f, y, "Empresa", [("Contrato y configuración de reglas", "gold"), ("Cortafuegos de aplicaciones y gestión de bots", "gold"), ("Reglas se distribuyen en segundos", "gold"), ("Una regla mala llega a todo el mundo a la vez", "coral")])
    y = lane_steps(f, y, "Desarrollador", [("Escribe un Worker", "navy"), ("Se despliega en la red", "navy"), ("Se ejecuta cerca del usuario en un aislado de V8", "navy"), ("Límites de CPU y de memoria", "coral")])
    y = lane_steps(f, y, "Usuario final", [("Escribe una dirección", "plain"), ("El DNS lo dirige a la ciudad más cercana", "plain"), ("Recibe la página desde la red", "plain"), ("La red falla y no hay otra vía", "coral")])
    return finish(f, y + 4, "Cada fila se lee de izquierda a derecha y la caja coral es el borde. Los bordes de la empresa y del usuario final salen de los posts de las caídas de 2019 y 2025; el del desarrollador, del post de aislados de V8. Dónde deja de valer: no mide frecuencia de cada borde.", "Esquema del autor sobre el 10-K de 2025 y el blog de Cloudflare.")


def negocio():
    return flow(
        "Cómo se financia Cloudflare: suscripciones a una red que crece",
        "Flujo del negocio: los clientes pagan suscripciones por acceder a la red y a sus productos de seguridad, rendimiento y desarrollo; el ingreso se reparte en coste de la red, ventas, ingeniería y administración; la escala de la red baja el coste por unidad y atrae más clientes; el negocio es todavía deficitario en resultado contable pero positivo en caja.",
        [[("Clientes gratuitos y de pago: 332 466 de pago", "teal"), ("Suscripciones por acceso a la red y productos", "gold"), ("Ingreso de 2 168 millones de USD en 2025", "navy"), ("Retención neta de dólares del 120 %", "teal")],
         [("Coste de ingresos: 25 %", "coral"), ("Ventas y marketing: 42 %", "coral"), ("I+D y administración: 42 %", "coral"), ("Flujo de caja libre: 12 % del ingreso", "teal")]],
        note="Documentado en el 10-K de 2025: el ingreso proviene principalmente de suscripciones a la red y a los productos, con servicios de soporte; no se entrega el software de la red. Inferido: la lectura del círculo virtuoso de escala; el 10-K lo describe en términos de dinámicas de coste.",
        foot=TENK, width=960)


def capas():
    return layer_stack(
        "Capas de Cloudflare que su ingeniería describió",
        "Pila de capas: usuarios que llegan por una dirección anycast a la ciudad más cercana; el proxy HTTP Pingora escrito en Rust; funciones de seguridad y rendimiento como cortafuegos y gestión de bots; cómputo en aislados de V8 con Workers; almacenamiento y datos; un plano de control en centros de datos de Oregón y su distribución de configuración con Quicksilver.",
        [("Usuarios", "Navegadores, aplicaciones y dispositivos que llegan a la ciudad más cercana", "teal"),
         ("Red", "Más de 330 ciudades en más de 125 países; interconexión con más de 13 000 redes", "plain"),
         ("Proxy", "Pingora, un proxy HTTP en Rust que sirve más de un billón de peticiones al día", "plain"),
         ("Servicios de borde", "Cortafuegos de aplicaciones, gestión de bots, Workers en aislados de V8", "plain"),
         ("Plano de control", "Panel y API en tres centros de datos de Oregón; Quicksilver distribuye la configuración", "gold"),
         ("Datos de análisis", "ClickHouse para los archivos de rasgos de gestión de bots y análisis", "navy")],
        [("Documentado entre 2019 y 2025", "teal"), ("No se sabe: número de servidores y de máquinas por ciudad", "grey"), ("Inferido: el mismo software corre en todas las ciudades", "grey")],
        "Documentado en los posts de Pingora, Quicksilver, Workers y de las caídas de 2019, 2023 y 2025, y en el 10-K. Dónde deja de valer: los posts son de 2019 a 2025 y el detalle de arquitectura cambia.",
        BLOG)


def peticion():
    return sequence(
        "Una petición de un usuario a través de Cloudflare",
        "Secuencia de una petición: el usuario resuelve el nombre y llega por anycast a la ciudad más cercana; el proxy aplica las reglas de seguridad y de caché; si hay un Worker lo ejecuta; si falta, consulta el origen reutilizando una conexión del grupo común; devuelve la respuesta.",
        ["Usuario", "Ciudad más cercana", "Proxy", "Reglas y Workers", "Origen"],
        [(0, 1, "llega por la dirección anycast", ""), (1, 2, "entrega al proxy HTTP", ""), (2, 3, "cortafuegos, bots, caché y código", ""),
         (2, 4, "si falta, pide al origen con conexión reutilizada", ""), (4, 2, "respuesta del origen", "ret"), (2, 0, "respuesta al usuario", "ret")],
        "Documentado por partes: el proxy Pingora y su reutilización de conexiones, las reglas de borde y los Workers vienen de posts distintos. Inferido: el orden exacto de las etapas. Dónde deja de valer: omite TLS, DNS, límites de tasa y las rutas de Tunnel y R2.",
        BLOG)


def pingora():
    return flow(
        "Pingora frente a NGINX: conexiones reutilizables y carga repartida",
        "Dos filas: con NGINX cada petición la atiende un solo proceso, la carga entre núcleos queda desbalanceada y el grupo de conexiones al origen es por proceso, de modo que se reutilizan poco; con Pingora, en Rust y con hilos, hay conexiones compartidas, sirve más de un billón de peticiones al día y usa un tercio de CPU y memoria.",
        [[("NGINX: una petición la sirve un solo proceso", "plain"), ("Carga desbalanceada entre núcleos", "coral"), ("Grupo de conexiones por proceso: poca reutilización", "coral")],
         [("Pingora en Rust, con hilos y conexiones compartidas", "teal"), ("Más de 1 billón de peticiones al día", "teal"), ("Un tercio de la CPU y la memoria del proxy anterior", "navy")]],
        note="Documentado en el post de Pingora. La reutilización de conexiones acelera el tiempo hasta el primer byte porque salta los apretones de manos TCP y TLS. Dónde deja de valer: el post dice que NGINX fue excelente durante años y que sus límites aparecieron a esta escala; no es una crítica general.",
        foot=BLOG, width=960)


def quicksilver():
    return years(line_chart(
        "Pares clave-valor de configuración que Cloudflare distribuye con Quicksilver",
        "Línea con 100 millones de pares clave-valor en 2015, más de 200 millones en 2017, más de 500 millones en 2018 y más de 1 000 millones en 2019: el volumen se multiplica por diez en cuatro años.",
        [("Pares clave-valor (millones)", [(2015, 100), (2017, 200), (2018, 500), (2019, 1000)], "navy")],
        x_label="Año", y_label="Millones de pares clave-valor", decimals=0,
        x_ticks=[(2015, "2015"), (2017, "2017"), (2018, "2018"), (2019, "2019")],
        note="El post cuenta que en 2015 había ocho instancias de Kyoto Tycoon con unos 200 cambios por segundo, que el proyecto no tenía mantenedor y que se construyó Quicksilver, que hoy sirve 2,5 billones de lecturas al día con latencia de microsegundos. Dónde deja de valer: los valores de 2017 a 2019 son «más de»; no hay serie anual completa.",
        foot="Fuente: «Quicksilver: Configuration Distribution at Internet Scale», blog.cloudflare.com."))


def workers():
    return flow(
        "Workers: aislados de V8 en lugar de contenedores",
        "Dos filas: un servicio sin servidor tradicional arranca un proceso en contenedor por cada copia del código y sufre arranques en frío de 0,5 a 10 segundos; Workers ejecuta cientos o miles de aislados de V8 en un solo proceso, que arrancan unas cien veces más rápido que un proceso de Node y usan un orden de magnitud menos memoria.",
        [[("Servicio sin servidor clásico: un proceso en contenedor por copia", "plain"), ("Arranque en frío de 0,5 a 10 segundos (según Cloudflare)", "coral"), ("Escala con retraso: cada copia nueva paga el arranque", "coral")],
         [("Aislados de V8: muchos contextos en un solo proceso", "teal"), ("Arrancan unas 100 veces más rápido que un proceso de Node", "teal"), ("Un orden de magnitud menos de memoria; un aislado no ve la memoria de otro", "navy")]],
        note="Documentado en «Cloud Computing without Containers». Las comparaciones son del propio autor del post, que dice que no es un anuncio pero compara con un producto rival. Dónde deja de valer: los aislados dan menos aislamiento que una máquina virtual y limitan el código que se puede ejecutar.",
        foot=BLOG, width=960)


def ddos():
    return hub(
        "Ataques volumétricos que Cloudflare mide: el tercer trimestre de 2025",
        "Esquema de cifras: una botnet llamada Aisuru con entre 1 y 4 millones de equipos infectados genera ataques que superan rutinariamente 1 terabit por segundo y 1 000 millones de paquetes por segundo; el número de esos ataques subió 54 por ciento respecto del trimestre anterior, con unos 14 diarios; el máximo fue de 29,7 terabits por segundo y 14,1 miles de millones de paquetes por segundo.",
        ("Informe de DDoS del tercer trimestre de 2025", "navy"),
        [("Botnet Aisuru: 1 a 4 millones de equipos infectados", "coral", "estimada"),
         ("Ataques de más de 1 Tbps y 1 000 M de paquetes por segundo", "coral", "rutinarios"),
         ("Unos 14 ataques hipervolumétricos por día", "gold", "promedio"),
         ("Aumento del 54 % frente al trimestre anterior", "gold", "crecimiento"),
         ("Máximo: 29,7 Tbps", "coral", "pico"),
         ("Máximo: 14,1 miles de millones de paquetes por segundo", "coral", "pico")],
        "Documentado en el informe de Cloudflare sobre ataques de denegación de servicio distribuida del tercer trimestre de 2025. Dónde deja de valer: son mediciones de Cloudflare sobre el tráfico que ve; no cubre ataques a otras redes.",
        "Fuente: «DDoS threat report... Aisuru», blog.cloudflare.com, 2025.")


def caida_2019():
    return timeline(
        "2 de julio de 2019: una regla del cortafuegos agota la CPU en todo el mundo",
        "Línea de tiempo en minutos desde las 13:40 UTC: a las 13:42 se despliega la regla de detección de XSS; a las 13:45 llega la primera alerta de una prueba sintética; la CPU se agota y los visitantes ven errores 502; el servicio tarda 27 minutos en volver.",
        [("Regla de WAF", [(2, 3, "", "gold"), (3, 31, "regla activa en toda la red", "coral")]),
         ("Servidores", [(5, 31, "CPU casi al 100 %", "coral")]),
         ("Visitantes", [(5, 32, "ven errores 502", "coral"), (32, 36, "", "teal")])],
        unit="minutos desde las 13:40 UTC", events=[(2, "13:42"), (5, "13:45"), (32, "~14:09")],
        t_max=38, ticks=[0, 10, 20, 30, 38], lane_h=46,
        note="Documentado en el post de 2019: la regla contenía una expresión regular con retroceso excesivo; el servicio estuvo caído 27 minutos; llevaban seis años sin una caída global. Dónde deja de valer: el fin se aproxima a las 14:09 sumando los 27 minutos al inicio del impacto; el post da la cronología completa.",
        foot="Fuente: «Details of the Cloudflare outage on July 2, 2019», blog.cloudflare.com. Segmentos dibujados por el autor.")


def caida_2023():
    return timeline(
        "2 al 4 de noviembre de 2023: un fallo eléctrico en un centro de datos deja sin panel y análisis a los clientes",
        "Línea de tiempo en horas desde las 08:50 UTC del 2 de noviembre: a las 08:50 la compañía eléctrica corta una de las acometidas del centro de datos; a las 11:44 empieza el incidente; a las 17:57 se restaura casi todo el plano de control en el centro de recuperación; a las 04:25 del 4 de noviembre termina; el tráfico de la red no se vio afectado.",
        [("Centro de datos de Oregón", [(0, 3, "", "gold"), (3, 44, "sin energía fiable", "coral")]),
         ("Panel, API y análisis", [(2.9, 9.1, "caídos", "coral"), (9.1, 43.6, "restauración gradual", "gold")]),
         ("Tráfico de la red", [(0, 44, "sin afectación", "teal")])],
        unit="horas desde las 08:50 UTC del 2 de noviembre", events=[(0, "08:50"), (2.9, "11:44"), (9.1, "17:57"), (43.6, "04:25")],
        t_max=46, ticks=[0, 12, 24, 36, 46], lane_h=46,
        note="Documentado en el post de 2023: el centro principal arrendado funcionó con generadores sin avisar a Cloudflare, el plano de control de alta disponibilidad no incluía todos los servicios y los registros no estaban en él por diseño. Dónde deja de valer: la lane del centro de datos es un resumen; el post narra además una falla posterior de energía.",
        foot="Fuente: «Post mortem on the Cloudflare Control Plane and Analytics Outage», blog.cloudflare.com. Segmentos dibujados por el autor.")


def caida_2025():
    return timeline(
        "18 de noviembre de 2025: un archivo de rasgos duplicado detiene el tráfico principal",
        "Línea de tiempo en minutos desde las 11:00 UTC: a las 11:05 un cambio de permisos en la base de datos; a las 11:20 empieza el fallo en la red; a las 11:28 llega a los clientes; hasta las 13:05 se investiga un falso ataque; a las 14:30 el tráfico fluye en su mayoría; a las 17:06 todo funciona con normalidad.",
        [("Cambio de base de datos", [(5, 20, "", "gold")]),
         ("Tráfico principal", [(20, 210, "errores 5xx", "coral"), (210, 366, "se recupera", "gold")]),
         ("Respuesta", [(32, 125, "falso DDoS", "gold"), (125, 210, "revierten", "teal")])],
        unit="minutos desde las 11:00 UTC", events=[(5, "11:05"), (20, "11:20"), (125, "13:05"), (210, "14:30"), (366, "17:06")],
        t_max=380, ticks=[0, 120, 240, 360, 380], lane_h=46,
        note="Documentado en el post: el cambio hizo que una consulta devolviera entradas duplicadas y el archivo se duplicó; el software tenía un límite de tamaño menor y falló; el archivo se regeneraba cada cinco minutos, por lo que el sistema se recuperaba y fallaba de forma intermitente, lo que sugirió un ataque. Dónde deja de valer: los segmentos de la respuesta son aproximaciones de la cronología del post.",
        foot="Fuente: «Cloudflare outage on November 18, 2025», blog.cloudflare.com. Segmentos dibujados por el autor.")


def cadena_2025():
    return flow(
        "Cadena causal de la caída de noviembre de 2025",
        "Cadena de causas: un cambio de permisos hace que una consulta de ClickHouse devuelva filas duplicadas; el archivo de rasgos de gestión de bots se duplica; se propaga a todas las máquinas; el software de enrutado tiene un límite de tamaño menor que el archivo y falla; el fallo es intermitente porque el clúster se actualiza por partes.",
        [[("Cambio de permisos en la base de datos", "gold"), ("La consulta devuelve entradas duplicadas", "coral"), ("El archivo de rasgos duplica su tamaño", "coral")],
         [("Se propaga a toda la red cada cinco minutos", "coral"), ("El software supera su límite de tamaño y falla", "coral"), ("Intermitente: solo falla si la consulta corre en un nodo actualizado", "gold")]],
        note="Documentado en el post de 2025: Cloudflare dice que no fue un ataque. Las acciones anunciadas son endurecer la ingestión de archivos de configuración propios como si fueran entradas de usuario, añadir más interruptores globales, evitar que los volcados de memoria saturen recursos y revisar los modos de fallo de los módulos del proxy. Dónde deja de valer: es una cadena simplificada.",
        foot=BLOG, width=960)


def linea():
    return years(timeline(
        "Cloudflare de 2009 a 2026: empresa, escala y fallos",
        "Línea de tiempo con tres carriles: la empresa (constituida en julio de 2009, cotizada desde septiembre de 2019), la red (194 ciudades en 2019 y más de 330 en 2025) y los fallos publicados (julio de 2019, noviembre de 2023 y noviembre de 2025).",
        [("Empresa", [(2009.5, 2019.7, "Empresa privada", "grey"), (2019.7, 2026, "Cotizada (NYSE: NET)", "teal")]),
         ("Red", [(2019.7, 2026, "194 a más de 330 ciudades", "navy")]),
         ("Fallos", [(2019.5, 2019.55, "", "coral"), (2023.85, 2023.9, "", "coral"), (2025.88, 2025.93, "", "coral")])],
        unit="año", events=[(2009.5, "constitución"), (2019.7, "IPO"), (2023.85, "Oregón"), (2025.88, "18 nov")],
        t_max=2027, ticks=[2009, 2013, 2017, 2021, 2025, 2027], lane_h=46,
        note="Hechos con fuente: constitución en Delaware en julio de 2009 y oferta pública a 15 dólares por acción con símbolo NET (prospecto de septiembre de 2019); red de 194 ciudades en 2019 y más de 330 en 2025; caídas del 2 de julio de 2019, del 2 de noviembre de 2023 y del 18 de noviembre de 2025. Dónde deja de valer: el lanzamiento comercial de 2010 no figura en las fuentes consultadas y no se dibuja.",
        foot="Fuentes: prospecto de 2019, 10-K de 2025 y blog de Cloudflare."))


def especiales():
    return case_cards(
        "Casos especiales documentados y cómo se resuelven",
        "Cinco tarjetas: una regla mala que llega a toda la red en segundos, un archivo de configuración que supera un límite, un centro de datos con energía por generadores sin aviso, ataques de más de un terabit por segundo y código de clientes ajeno que debe aislarse; cada una con su mecanismo y veredicto.",
        [("Una regla de cortafuegos con regex que retrocede sin límite", "CPU agotada en todo el mundo durante 27 minutos (2019)", "El despliegue global rápido es una ventaja y un riesgo a la vez.", "coral"),
         ("Un archivo de configuración mayor que el límite del software", "Fallo del tráfico principal y recuperación con el archivo anterior (2025)", "Los datos internos deben validarse como si vinieran de un usuario.", "coral"),
         ("Un centro de datos que pasa a generadores sin avisar", "Panel y análisis caídos casi dos días; el tráfico siguió (2023)", "La alta disponibilidad no cubría servicios nuevos ni dependencias no obvias.", "gold"),
         ("Ataques de más de 1 Tbps de forma rutinaria", "Absorción en la red distribuida", "Máximos de 29,7 Tbps medidos en 2025.", "teal"),
         ("Código de miles de clientes en un solo proceso", "Aislados de V8 con límites de CPU y memoria", "Menos aislamiento que una máquina virtual, a cambio de arranque rápido.", "gold")],
        note="Cada tarjeta enlaza un hecho citado con el mecanismo. Color: coral falla, teal se sostiene, gold depende. Dónde deja de valer: son casos documentados por Cloudflare, que cuenta sus propios fallos.",
        foot=BLOG)


def alternativas():
    return case_cards(
        "Alternativas que Cloudflare no tomó o sustituyó, como análisis del curso",
        "Cuatro tarjetas: seguir con NGINX, mantener Kyoto Tycoon para la configuración, usar contenedores para el código de los clientes y alojar el plano de control en un solo centro de datos; cada una con lo que Cloudflare hizo.",
        [("Seguir con NGINX", "Pingora, un proxy propio en Rust", "Documentado: limitaciones de arquitectura y poca reutilización de conexiones a esta escala.", "teal"),
         ("Seguir con Kyoto Tycoon", "Quicksilver, un almacén propio", "Documentado: sin mantenedor, con escritura a disco y sin conmutación automática.", "teal"),
         ("Contenedores para el código de clientes", "Aislados de V8", "Documentado por Cloudflare: arranque más rápido y menos memoria; menos aislamiento.", "gold"),
         ("Un solo centro de datos para el plano de control", "Tres centros activos en Oregón", "Documentado: en 2023 los servicios fuera del clúster de alta disponibilidad cayeron.", "gold")],
        note="Rótulo: documentado por el propio Cloudflare en los posts de Pingora, Quicksilver, Workers y 2023, con las salvedades de que son razones de quien vende el producto. Dónde deja de valer: no publica las evaluaciones completas con cifras de cada alternativa.",
        foot=BLOG)


def hardware():
    return layer_stack(
        "Hardware y software que Cloudflare hace público",
        "Pila: servidores propios en más de 330 ciudades; centros de datos de Oregón y Ámsterdam; software propio en Rust (Pingora), Go y otros; V8 para Workers; ClickHouse para datos; Quicksilver para configuración.",
        [("Hardware", "Servidores propios en más de 330 ciudades; centros de datos de Oregón y Ámsterdam", "grey"),
         ("Red", "Interconexión con más de 13 000 redes; anycast", "plain"),
         ("Proxy", "Pingora (Rust); antes NGINX", "plain"),
         ("Cómputo", "V8 con aislados para Workers", "plain"),
         ("Datos", "Quicksilver (configuración), ClickHouse (análisis); Kyoto Tycoon antes", "gold")],
        [("Documentado en posts de 2019 a 2025 y el 10-K", "teal"), ("No se sabe: número de servidores y de máquinas por ciudad", "grey")],
        "El 10-K de 2025 dice que Cloudflare opera su propia red y que sus centros de datos principales están en la zona de Portland y en Ámsterdam. Dónde deja de valer: las máquinas por ciudad no se publican en las fuentes consultadas.",
        BLOG)


def pruebas_fallo():
    return case_cards(
        "Temas a prueba de fallos que Cloudflare documenta",
        "Cuatro mecanismos con veredicto: un plano de control activo-activo en tres centros de datos, desvío de servicios a una versión anterior del proxy durante una caída, distribución de configuración en segundos con reversión al archivo anterior e interruptores globales de funciones.",
        [("Cae un centro de datos de control", "Dos más siguen activos (diseño de alta disponibilidad)", "En 2023 falló lo que no estaba en ese diseño.", "gold"),
         ("El proxy nuevo falla", "Se desvían Workers KV y Access a una versión anterior del proxy (2025)", "El fallo también estaba en la versión anterior, de modo que solo redujo el impacto.", "gold"),
         ("Un archivo malo se propaga", "Se detiene la propagación y se restaura el anterior (2025)", "La reversión rápida limitó la duración a unas tres horas.", "teal"),
         ("Una función falla en toda la red", "Interruptores globales de funciones", "Cloudflare anunció más interruptores tras 2025.", "teal")],
        note="Documentado en los posts de 2019, 2023 y 2025. Dónde deja de valer: los mecanismos funcionaron parcialmente en esos incidentes y cada post anuncia mejoras.",
        foot=BLOG)


FIGURES = {
    "cloudflare-contexto.svg": contexto,
    "cloudflare-ingresos.svg": ingresos,
    "cloudflare-reparto-del-ingreso.svg": reparto,
    "cloudflare-perdida-y-caja.svg": caja,
    "cloudflare-clientes-de-pago.svg": clientes,
    "cloudflare-clientes-grandes-y-retencion.svg": grandes,
    "cloudflare-ingresos-por-region.svg": regiones,
    "cloudflare-crecimiento-de-la-red.svg": red,
    "cloudflare-actores-e-incentivos.svg": actores,
    "cloudflare-recorridos-de-usuario.svg": recorridos,
    "cloudflare-esquema-del-negocio.svg": negocio,
    "cloudflare-capas.svg": capas,
    "cloudflare-secuencia-de-una-peticion.svg": peticion,
    "cloudflare-pingora.svg": pingora,
    "cloudflare-quicksilver.svg": quicksilver,
    "cloudflare-workers-y-aislados.svg": workers,
    "cloudflare-ataques-volumetricos.svg": ddos,
    "cloudflare-caida-2019.svg": caida_2019,
    "cloudflare-caida-2023.svg": caida_2023,
    "cloudflare-caida-2025.svg": caida_2025,
    "cloudflare-cadena-de-la-caida-2025.svg": cadena_2025,
    "cloudflare-linea-de-tiempo.svg": linea,
    "cloudflare-casos-especiales.svg": especiales,
    "cloudflare-alternativas.svg": alternativas,
    "cloudflare-hardware-y-software.svg": hardware,
    "cloudflare-a-prueba-de-fallos.svg": pruebas_fallo,
}


if __name__ == "__main__":  # pragma: no cover - manual preview
    import pathlib
    import sys

    out = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "casos/figures")
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (out / name).write_text(fn().svg(), encoding="utf-8")
        print(name)
