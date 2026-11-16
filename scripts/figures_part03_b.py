"""Figures for SE-042 to SE-048 (values measured on Windows 11 and Ubuntu 24.04 under WSL2)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, line_chart, percentile_intervals
from figure_flows import mapa
from figures_part03_a import _note


# ---------------------------------------------------------------- SE-042
def se042_cabeceras() -> Fig:
    return mapa("Cabeceras reales de https://example.com",
                "Seis cabeceras observadas, cada una con su valor y lo que comunica: Content-Type text/html; charset=utf-8, Server cloudflare, Last-Modified del 13 de noviembre de 2026, Age 3521 segundos, alt-svc que anuncia h3, y la ausencia de ETag.",
                [("Content-Type", "text/html; charset=utf-8", "teal", "Tipo de medio y codificación del cuerpo"),
                 ("Server", "cloudflare", "teal", "Quién responde: un intermediario, no necesariamente el origen"),
                 ("Last-Modified", "Fri, 13 Nov 2026 08:41:42 GMT", "teal", "Validador débil basado en tiempo"),
                 ("Age", "3521", "teal", "La copia tiene 3521 s de antigüedad en la caché del intermediario"),
                 ("alt-svc", "h3=\":443\"; ma=86400", "teal", "HTTP/3 disponible en el puerto 443 durante 86 400 s"),
                 ("ETag", "(ausente)", "coral", "No hay validador fuerte: la validación usa la fecha")],
                note="Las cabeceras son una conversación con el intermediario y el origen; cada una debe leerse con su semántica.",
                left_w=190, mid_w=330, row_h=52, size=12, heads=("Cabecera", "Valor observado", "Qué comunica"))


def se042_metodos() -> Fig:
    return mapa("Métodos y estados: lo que respondió el servidor",
                "Siete peticiones con el estado que respondió el servidor y su lectura: GET 200 con 577 bytes, HEAD 200 sin cuerpo, POST y OPTIONS 405, una ruta inexistente 404, una petición condicional con If-Modified-Since 304, y un 503 con Retry-After de 1 segundo en un servidor local.",
                [("GET /", "200 (577 B)", "teal", "Representación del recurso"),
                 ("HEAD /", "200 (0 B de cuerpo)", "teal", "Mismas cabeceras, sin cuerpo: sirve para comprobar existencia y tamaño"),
                 ("POST /", "405", "coral", "El método existe pero este recurso no lo admite"),
                 ("OPTIONS /", "405", "coral", "El servidor no anuncia métodos con OPTIONS"),
                 ("GET /no-existe", "404", "coral", "No hay recurso en esa ruta"),
                 ("GET / con If-Modified-Since", "304", "gold", "No modificado: no se retransmite el cuerpo (ahorro de 577 B)"),
                 ("GET /503 (servidor local)", "503 + Retry-After: 1", "gold", "Indisponibilidad temporal con una pista de cuándo reintentar")],
                note="El número de estado es una decisión del servidor sobre el recurso, no un reflejo del éxito del negocio.",
                left_w=260, mid_w=190, row_h=50, size=12, heads=("Petición", "Estado", "Lectura"))


def se042_compresion() -> Fig:
    f = Fig(940, 430, "Negociar y reutilizar: compresión y validación",
            "Barras con una medición real: el cuerpo de 577 bytes viaja en 400 bytes con Content-Encoding gzip, y una petición condicional devuelve 304 sin cuerpo. La respuesta tenía 3521 segundos de antigüedad en la caché.")
    f.text(20, 28, "Bytes transferidos por el cuerpo", 14, "start", 700)
    f.hbars([("Sin compresión (identity)", 577, "coral", "577 B"), ("Con Accept-Encoding: gzip", 400, "gold", "400 B"), ("304 con If-Modified-Since", 0, "teal", "0 B")], 20, 44, 0.8, label_w=270, step=46)
    f.box(20, 200, 900, 74, "Accept-Encoding es una preferencia del cliente y Content-Encoding la decisión del servidor; si la respuesta varía según esa cabecera, el intermediario debe saberlo (Vary) para no mezclar copias.", "grey", 13)
    f.box(20, 288, 900, 60, "Age = 3521 s: la copia que recibió el cliente tenía casi una hora. La frescura la decide Cache-Control; sin validador fuerte, la revalidación usa la fecha.", "gold", 13)
    _note(f, 380, "Medido con curl contra https://example.com; los tamaños dependen del sitio y del momento.")
    return f


# ---------------------------------------------------------------- SE-043
def se043_certificado() -> Fig:
    f = Fig(960, 370, "Lo que muestra una conexión TLS real a example.com",
            "Cadena de confianza observada en una conexión a example.com: un certificado hoja (CN example.com, nombres alternativos example.com y *.example.com, válido del 26 de septiembre al 25 de diciembre de 2026, 90 días) firmado por dos intermedios y una raíz de SSL.com, "
            "con la sesión TLS 1.3 y TLS_AES_256_GCM_SHA384 y un handshake de unos 145 ms.")
    f.text(480, 24, "Cadena presentada: cada certificado está firmado por el siguiente y la confianza llega hasta una raíz que el cliente ya tiene", 13, "middle", 700, "#32505f")
    chain = [("Certificado hoja\nCN = example.com\nSAN: example.com, *.example.com\nVálido 26 sep → 25 dic 2026 (90 días)", "teal"),
             ("Intermedio\nCloudflare TLS Issuing ECC CA 3", "gold"),
             ("Intermedio\nSSL.com TLS Transit ECC CA R2", "gold"),
             ("Raíz\nSSL.com TLS ECC Root CA 2022\n(ya está en el almacén del cliente)", "grey")]
    for i, (text, kind) in enumerate(chain):
        x = 10 + i * 242
        f.box(x, 40, 212, 120, text, kind, 12, True)
        if i < 3:
            f.arrow([(x + 212, 100), (x + 242, 100)])
    facts = [("Sesión: TLS 1.3 con TLS_AES_256_GCM_SHA384. Cifrado autenticado y claves efímeras", "plain"),
             ("Nombre: el cliente verifica el nombre contra la SAN, no solo contra el CN", "plain"),
             ("Vida corta: 90 días de validez; los certificados modernos se renuevan a menudo", "plain"),
             ("Handshake: ≈145 ms, un viaje de ida y vuelta; TLS 1.3 completa la negociación en un RTT", "plain")]
    for i, (text, kind) in enumerate(facts):
        x = 10 + i * 238
        f.box(x, 190, 224, 86, text, kind, 12)
    f.box(10, 296, 940, 56, "El certificado prueba que el servidor controla el nombre, no que sea digno de confianza ni que su contenido sea correcto.", "gold", 13)
    return f


def se043_veredictos() -> Fig:
    return mapa("Cuatro veredictos locales con un certificado de laboratorio",
                "Cuatro intentos reales contra un servidor TLS local con certificado autofirmado, cada uno con su veredicto: sin confianza falla con self-signed certificate (código 18); con la CA del laboratorio funciona con TLS 1.3 y ALPN h2 en 3 ms; "
                "con otro nombre falla con Hostname mismatch (código 62); con la verificación desactivada funciona, pero sin protección.",
                [("Sin confiar en el certificado", "Falla: self-signed certificate (código 18)", "coral", "La cadena no llega a una raíz de confianza"),
                 ("Confiando en la CA del laboratorio", "Funciona: TLS 1.3 · ALPN h2 · 3,0 ms", "teal", "Confianza explícita y nombre correcto"),
                 ("Nombre «otro.example»", "Falla: Hostname mismatch, el certificado no es válido para ese nombre (código 62)", "coral", "La cadena es válida pero el nombre no coincide"),
                 ("Verificación desactivada", "Funciona sin verificar: TLS 1.3 (sin ALPN)", "gold", "Cifra pero no autentica: cualquiera puede suplantar al servidor")],
                note="Desactivar la verificación «para que funcione» elimina la propiedad que TLS ofrece frente a un atacante activo. Se corrige la confianza o el nombre, no la prueba.",
                note_kind="coral", left_w=250, mid_w=300, row_h=70, size=12, heads=("Intento", "Veredicto", "Lectura"))


def se043_almacen() -> Fig:
    return mapa("El almacén de confianza también es parte del sistema",
                "Cuatro observaciones reales con su resultado y su lectura: Python en Windows falló con unable to get local issuer certificate al conectar a example.com y funcionó después de que curl con Schannel construyera la cadena, "
                "Python en Linux funcionó de inmediato, y un nombre desconocido recibió un alert de handshake failure.",
                [("Python en Windows, primer intento", "CERTIFICATE_VERIFY_FAILED: unable to get local issuer certificate (110 raíces cargadas)", "coral", "La raíz de la cadena no estaba aún en el almacén que Python leyó"),
                 ("Tras una petición con curl (Schannel)", "Python funciona; la raíz «SSL.com TLS ECC Root CA 2022» ya aparece", "teal", "Windows incorpora raíces bajo demanda cuando construye una cadena"),
                 ("Python en Linux (WSL2)", "Funciona a la primera", "teal", "El paquete de certificados de la distribución ya contenía la raíz"),
                 ("SNI con un nombre desconocido (example.com)", "sslv3 alert handshake failure", "gold", "El servidor rechaza un nombre que no sirve: no es un error de certificado")],
                note="Una misma conexión puede validarse o no según el almacén de cada cliente. Se declara qué almacén usa cada herramienta.",
                left_w=260, mid_w=330, row_h=76, size=12, heads=("Observación", "Resultado", "Lectura"))


# ---------------------------------------------------------------- SE-044
def se044_proxy() -> Fig:
    f = Fig(960, 460, "Quién puede afirmar la IP del cliente: origen directo frente a proxy",
            "Dos caminos de una misma petición con un X-Forwarded-For falso 203.0.113.99: enviada directamente al origen, este la acepta tal cual; enviada a través del proxy, el proxy sustituye la cabecera por la IP real 127.0.0.1, "
            "conserva el identificador de petición abc-123 y añade Via.")
    f.text(480, 22, "Camino directo: el origen confía en lo que dice el cliente", 13, "middle", 700, "#32505f")
    f.box(10, 36, 130, 84, "Cliente", "navy", 14, True)
    f.arrow([(140, 78), (580, 78)], "X-Forwarded-For: 203.0.113.99 (falso)", label_at=(360, 68))
    f.box(580, 36, 130, 84, "Origen", "plain", 14, True)
    f.arrow([(710, 78), (740, 78)])
    f.box(740, 36, 210, 84, "Acepta 203.0.113.99, falsificado por el cliente; sin X-Request-Id ni Via", "coral", 12)
    f.text(480, 156, "A través del proxy: la cabecera la fija un componente de confianza", 13, "middle", 700, "#32505f")
    f.box(10, 170, 130, 84, "Cliente", "navy", 14, True)
    f.arrow([(140, 212), (270, 212)], "XFF falso\n203.0.113.99", label_at=(205, 188))
    f.box(270, 170, 150, 84, "Proxy de confianza", "gold", 13, True)
    f.arrow([(420, 212), (580, 212)], "XFF: 127.0.0.1\nX-Request-Id: abc-123", label_at=(500, 184))
    f.box(580, 170, 130, 84, "Origen", "plain", 14, True)
    f.arrow([(710, 212), (740, 212)])
    f.box(740, 170, 210, 84, "Ve 127.0.0.1 (IP real vista por el proxy), X-Request-Id abc-123 y Via 1.1 proxy-local", "teal", 12)
    f.box(10, 276, 940, 70, "Una cabecera reenviada solo es confiable si la fija un componente de confianza y el origen rechaza o sobrescribe lo que llega de fuera de esa frontera.", "coral", 13)
    f.box(10, 358, 940, 66, "La política: el borde descarta las cabeceras entrantes de identidad, fija las suyas y el origen solo acepta conexiones del proxy.", "gold", 13)
    return f


def se044_balanceo() -> Fig:
    return grouped_bars("Balanceo y conmutación por falla: lo que se observó",
                        "Barras horizontales en escala logarítmica con el tiempo en que se detectó el primer fallo al detener el origen A: 0,35 ms en Linux (rechazo inmediato) y 499,9 ms en Windows (espera hasta el timeout de conexión); el reparto de 20 peticiones fue idéntico en ambos sistemas.",
                        ["Linux (WSL2): rechazo inmediato", "Windows: espera hasta el timeout"],
                        [("Primer fallo detectado", [0.35, 499.9], "coral")],
                        unit="ms", horizontal=True, log=True, ticks=[0.1, 1, 10, 100, 1000],
                        value_fmt=lambda v: f"{v:g}".replace(".", ","),
                        note="En ambos sistemas, 20 peticiones en turno rotatorio con A y B sanos se repartieron 10 y 10; con A detenido, las 20 terminaron en B y se detectaron 10 fallos al conectar. "
                             "Un balanceador sin comprobaciones de salud sigue enviando tráfico al origen caído, y el costo de descubrir la caída depende de cómo falla la conexión y del timeout elegido.",
                        foot="Orígenes y balanceo simulados en loopback; no se midió un balanceador real.")


def se044_cdn() -> Fig:
    f = Fig(960, 450, "Qué se observa y qué queda oculto detrás de una CDN",
            "Cuatro observaciones desde el cliente (Server cloudflare, Age 3521, alt-svc h3, un certificado de una CA intermedia, el RTT al nodo y la antigüedad de la respuesta) frente a lo que queda al otro lado de la frontera de la CDN: el origen, su certificado, el nodo de borde y la última validación.")
    obs = ["Server: cloudflare · Age: 3521 s · alt-svc: h3", "Un certificado de 90 días para example.com emitido por una CA intermedia",
           "RTT medio de 146 ms hasta el nodo que responde", "La respuesta tenía 3521 s de antigüedad"]
    hid = ["Qué servidor de origen existe y en qué región", "Si el tráfico hacia el origen también va cifrado",
           "En qué nodo de borde cayó la petición", "Cuándo fue la última validación con el origen"]
    f.text(225, 24, "Observable desde el cliente", 13, "middle", 700, "#32505f")
    f.text(735, 24, "No observable", 13, "middle", 700, "#32505f")
    f.line(480, 36, 480, 340, "#c0432f", True, 2)
    f.text(480, 358, "frontera de la CDN", 12, "middle", 700, "#5c1f14")
    for i, (a, b) in enumerate(zip(obs, hid)):
        y = 44 + i * 78
        f.box(10, y, 430, 60, a, "teal", 13)
        f.box(520, y, 430, 60, b, "coral", 13, dashed=True)
        f.arrow([(440, y + 30), (520, y + 30)], dashed=True, color="#c0432f")
    f.box(10, 376, 940, 60, "Una CDN es un intermediario: reduce latencia y carga, pero añade capas en las que pueden fallar la caché, el certificado o las cabeceras. Diagnosticar exige conocer cuál respondió.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-045
def se045_reutilizar() -> Fig:
    return grouped_bars("Reutilizar la conexión: cuánto ahorra y cuándo no",
                        "Barras horizontales en escala logarítmica con mediciones en loopback: en Windows abrir una conexión por petición tardó 1,396 ms y reutilizarla 0,366 ms (3,8 veces menos); en Linux la reutilización tardó 44,12 ms con dos escrituras por respuesta y 0,31 ms con una sola.",
                        ["Windows: una conexión por petición", "Windows: conexión reutilizada", "Linux: reutilizada, dos escrituras", "Linux: reutilizada, una escritura", "Linux: reutilizada, TCP_NODELAY"],
                        [("Tiempo por petición", [1.396, 0.366, 44.12, 0.31, 0.34], "teal")],
                        unit="ms por petición", horizontal=True, log=True, ticks=[0.1, 1, 10, 100],
                        value_fmt=lambda v: f"{v:g}".replace(".", ","),
                        note="En Windows, abrir una conexión por petición incluye el handshake TCP en cada una y reutilizarla ahorra el handshake y el arranque lento (3,8 veces menos). En Linux, con cabeceras y cuerpo en dos escrituras, Nagle y el ACK retrasado añaden ≈ 40 ms por petición; "
                             "con una sola escritura o TCP_NODELAY la espera desaparece y la reutilización vuelve a ayudar. Reutilizar conexiones es casi siempre una ventaja, pero un detalle del envío puede anularla: se mide con tu servidor real antes de generalizar.")


def se045_contrapresion() -> Fig:
    f = Fig(900, 400, "Contrapresión: cuánto acepta el sistema antes de bloquear al emisor",
            "Barras con una medición real: un emisor que envía a un receptor que no lee pudo escribir 327 680 bytes en Windows y 2 621 440 bytes en Linux antes de que el envío se bloqueara.")
    f.text(20, 28, "Bytes aceptados por los búferes antes de bloquear", 14, "start", 700)
    f.hbars([("Windows", 327680, "gold", "327 680 B (320 KiB)"), ("Linux (WSL2)", 2621440, "teal", "2 621 440 B (2,5 MiB)")], 20, 52, 0.00019, label_w=170, step=56)
    f.box(20, 190, 860, 90, "Si el receptor no lee, los búferes se llenan y el emisor se bloquea (o recibe un error en modo no bloqueante): esa es la señal de contrapresión. Un diseño sin límites acumula memoria o pierde datos.", "grey", 13)
    f.box(20, 292, 860, 60, "El tamaño de los búferes depende del sistema y de su ajuste: no es un contrato. La aplicación define su propio límite y su política (descartar, esperar, rechazar).", "gold", 13)
    return f


def se045_ciclo() -> Fig:
    f = Fig(940, 420, "Ciclo de vida de un socket y tiempos límite",
            "Fases de un socket: crear, conectar o escuchar, intercambiar datos con framing, cerrar con una política y esperar con un tiempo límite; una lectura con timeout de 0,1 s contra un servidor lento lanzó TimeoutError a los 0,1 s.")
    steps = [("Crear y conectar", "connect con timeout de conexión", "teal"), ("Intercambiar", "framing: longitud o delimitador; el flujo no tiene fronteras", "gold"),
             ("Esperar", "timeout de lectura: 0,1 s → TimeoutError a los 0,1 s", "coral"), ("Cerrar", "shutdown o close; el otro lado observa FIN y CLOSE-WAIT", "teal")]
    for i, (name, text, kind) in enumerate(steps):
        x = 14 + i * 230
        f.box(x, 20, 216, 44, name, "navy", 13, bold=True)
        f.box(x, 72, 216, 120, text, kind, 12)
        if i < 3:
            f.arrow([(x + 216, 42), (x + 230, 42)])
    f.box(14, 216, 920, 70, "Tres tiempos distintos: conexión, lectura y plazo total. Un timeout dice cuánto se esperó, no si el servidor ejecutó la operación.", "grey", 13)
    f.box(14, 298, 920, 60, "Una conexión en CLOSE-WAIT acumulada es un cierre que la aplicación no completó.", "plain", 13)
    return f


# ---------------------------------------------------------------- SE-046
def se046_variacion() -> Fig:
    runs = [(0.009233, 0.140613, 0.285776, 0.429907, 0.430245), (0.008483, 0.167068, 0.310527, 0.479185, 0.479520),
            (0.008808, 0.144154, 0.286818, 0.434600, 0.434950), (0.008812, 0.139805, 0.288849, 0.425489, 0.425846),
            (0.009671, 0.140327, 0.282572, 0.426745, 0.427094)]
    phases = {"DNS": [], "TCP": [], "TLS": [], "Espera": [], "Total": []}
    for i, (d, c, a, s, t) in enumerate(runs, start=1):
        for name, v in (("DNS", d), ("TCP", c - d), ("TLS", a - c), ("Espera", s - a), ("Total", t)):
            phases[name].append((i, round(v * 1000)))
    spans = {k: (min(v for _, v in pts), max(v for _, v in pts)) for k, pts in phases.items()}
    kinds = {"DNS": "grey", "TCP": "teal", "TLS": "gold", "Espera": "coral", "Total": "navy"}
    return line_chart("Cinco mediciones seguidas de la misma petición: variación por fase",
                      "Cinco ejecuciones seguidas de curl -w contra https://example.com, con una línea por fase: el TCP tarda entre 131 y 159 ms, TLS entre 142 y 149 ms, la espera entre 137 y 169 ms y el total entre 426 y 480 ms.",
                      [(k, phases[k], kinds[k]) for k in phases],
                      x_label="Ejecución", y_label="Milisegundos por fase (intervalos, no acumulados)",
                      x_ticks=[(i, str(i)) for i in range(1, 6)], point_labels="none", y_zero=True,
                      note="Rangos entre las cinco ejecuciones: " + "; ".join(f"{k} {lo}–{hi} ms" for k, (lo, hi) in spans.items()) + ". Una sola medición esconde que una fase pudo variar 30 ms: se repite y se reporta el rango.")


def se046_rtt() -> Fig:
    return grouped_bars("Ida y vuelta y pérdida: ping y pruebas dirigidas",
                        "Barras horizontales con diez pings reales a example.com, sin pérdida, de RTT mínimo 129 ms, medio 146 ms y máximo 176 ms, y dos pings con la bandera DF cuyos paquetes de 1372 y 1472 bytes pasaron en 143 y 164 ms.",
                        ["ping × 10: mínimo", "ping × 10: medio", "ping × 10: máximo", "ping con DF, 1372 B", "ping con DF, 1472 B"],
                        [("Tiempo de ida y vuelta", [129, 146, 176, 143, 164], "teal")],
                        unit="ms", horizontal=True,
                        note="Los diez pings no perdieron ningún paquete y el RTT varía unos 47 ms entre mínimo y máximo; el tamaño no cambia la latencia de forma notable en este rango. Una ruta sin respuesta (modelo del laboratorio) termina en un timeout de conexión, que no distingue pérdida, filtrado o ruta rota. "
                             "ICMP puede recibir un trato distinto del tráfico de aplicación: el RTT de ping orienta, pero la latencia de la aplicación se mide con la aplicación.")


def se046_puntos() -> Fig:
    return mapa("Dónde se observa: cada punto de vista ve algo distinto",
                "Cuatro puntos de observación, cada uno con lo que ve y lo que no ve: el cliente (curl -w), el servidor (registros), el sistema operativo (ss) y la red (captura de paquetes, no ejecutada aquí); el color del centro indica si se midió, se simuló en el laboratorio o no se ejecutó.",
                [("Cliente (curl -w, temporizadores) · medido", "Ve las fases: DNS, TCP, TLS, espera", "teal", "No ve qué ocurrió en el servidor"),
                 ("Servidor (registros con request ID) · laboratorio local", "Ve cuándo llegó y cuánto tardó el procesamiento", "gold", "No ve lo que pasó antes de llegar"),
                 ("Sistema operativo (ss -tan) · medido", "Ve los estados de conexión: ESTAB, CLOSE-WAIT, TIME-WAIT", "teal", "No ve el contenido ni los tiempos de red"),
                 ("Red (captura de paquetes) · no ejecutado", "Vería segmentos, retransmisiones y ventanas", "grey", "No ve el resultado de negocio; exige permisos y cuida la privacidad")],
                note="Una captura no era necesaria para este diagnóstico; cuando lo es, se limita interfaz, destino, tiempo y campos.",
                left_w=270, mid_w=270, row_h=70, size=12, heads=("Punto de observación", "Qué ve", "Qué no ve"))


# ---------------------------------------------------------------- SE-047
def se047_suite() -> Fig:
    return mapa("Los siete escenarios del laboratorio y su primera divergencia",
                "Siete escenarios de la suite real, cada uno con la primera fase en que se aparta del caso sano y su resultado: healthy es ok; dns_failure falla en dns (name_not_found); connection_refused en connect (refused); tls_name_mismatch en tls (name_mismatch); latency_timeout en http_wait (deadline_exceeded); "
                "transient_loss y http_503 se recuperan en el segundo intento.",
                [("healthy", "Sin divergencia (dns → connect → http → correlation)", "teal", "ok · 1 intento"),
                 ("dns_failure", "dns · name_not_found", "coral", "failed · 0 intentos"),
                 ("connection_refused", "connect · refused", "coral", "failed · 1 intento"),
                 ("tls_name_mismatch", "tls · name_mismatch", "coral", "failed · 0 intentos"),
                 ("latency_timeout", "http_wait · deadline_exceeded", "coral", "failed · 1 intento"),
                 ("transient_loss", "transport (pérdida) → reintento → http", "gold", "recovered · 2 intentos"),
                 ("http_503", "http 503 → reintento → http 200", "gold", "recovered · 2 intentos")],
                note="Se compara por la primera fase que difiere del caso sano, no por el número de errores posteriores.",
                left_w=230, mid_w=360, row_h=50, size=12, heads=("Escenario", "Primera divergencia", "Resultado"))


def se047_correlacion() -> Fig:
    f = Fig(960, 440, "Línea temporal multicapa con un identificador de correlación",
            "Cuatro fases del caso sano (dns, connect, http, correlation) y cómo un identificador único de petición une los eventos de cliente, intermediario y servidor.")
    phases = [("dns", "Resolución: desplazamiento ≈ 0 ms", "teal"), ("connect", "Conexión TCP local establecida", "teal"), ("http", "Solicitud y respuesta con el mismo request ID", "gold"), ("correlation", "El ID aparece en cliente y servidor", "coral")]
    for i, (name, text, kind) in enumerate(phases):
        x = 14 + i * 236
        f.box(x, 20, 222, 44, name, "navy", 13, bold=True)
        f.box(x, 72, 222, 100, text, kind, 12)
        if i < 3:
            f.arrow([(x + 222, 42), (x + 236, 42)])
    f.box(14, 196, 930, 70, "El identificador se genera en el borde, se propaga por cada salto y se registra en cada capa. Sin él, unir eventos depende de la hora, que no basta (SE-033).", "grey", 13)
    f.box(14, 280, 930, 70, "Cada evento declara fase, resultado, desplazamiento y evidencia; la «primera divergencia» respecto del caso sano delimita la hipótesis.", "gold", 13)
    f.box(14, 362, 930, 56, "El laboratorio redacta cabeceras sensibles y no guarda cuerpos: la correlación no exige datos personales.", "plain", 13)
    return f


def se047_pruebas() -> Fig:
    return grouped_bars("Las once pruebas del laboratorio en dos plataformas",
                        "Barras horizontales con la duración de las once pruebas del laboratorio de la Parte 03, todas aprobadas: 7,56 segundos en Windows 11 con Python 3.12.9 y 6,38 segundos en Ubuntu 24.04 bajo WSL2 con Python 3.12.3.",
                        ["Windows 11 · Python 3.12.9", "Linux (WSL2) · Python 3.12.3"],
                        [("11 pruebas, todas pasan", [7.56, 6.38], "teal")],
                        unit="segundos", horizontal=True, decimals=2,
                        note="Las pruebas ejercitan los siete escenarios con un servidor HTTP efímero en 127.0.0.1; DNS, validación TLS y pérdida son modelos deterministas, y el tráfico HTTP es real y local. "
                             "Pasar en dos plataformas no prueba el comportamiento en una red real: el laboratorio lo declara como límite.")


# ---------------------------------------------------------------- SE-048
def se048_backoff() -> Fig:
    return percentile_intervals("Reintento con retroceso exponencial y jitter contra un servicio que falla dos veces",
                                "Dos rangos de espera aleatoria con jitter completo en una prueba local: el servidor responde 503 dos veces y luego 200; tras el primer intento la espera es aleatoria entre 0 y 0,05 s y tras el segundo entre 0 y 0,10 s; el cliente terminó en 99,7 ms en Windows y 70,7 ms en Linux.",
                                [("Espera tras el intento 1 (503)", [0, 0.05]), ("Espera tras el intento 2 (503)", [0, 0.10])],
                                unit="segundos", marks=("mínimo", "máximo"), decimals=2,
                                note="El tercer intento recibe 200 OK y no espera. Tiempo total: 99,7 ms (Windows) y 70,7 ms (Linux). La espera máxima crece como 0,05 · 2^k y el azar evita que muchos clientes reintenten a la vez. "
                                     "Reintentar es seguro solo para operaciones idempotentes y con un tope de intentos y un plazo total; de lo contrario, multiplica la carga que causó el fallo.")


def se048_presupuesto() -> Fig:
    f = Fig(940, 430, "Presupuesto de tiempo: del plazo total a los límites por fase",
            "Barras con las fases medidas de una petición HTTPS (DNS 9, TCP 131, TLS 146 y espera 144 ms, total 430 ms) frente a un plazo total de 2000 ms: sobran unos 1570 ms para reintentos.")
    f.text(20, 28, "Fases medidas frente al plazo total de 2000 ms", 14, "start", 700)
    f.hbars([("DNS", 9, "gold", "9 ms"), ("TCP", 131, "teal", "131 ms"), ("TLS", 146, "teal", "146 ms"), ("Espera de la respuesta", 144, "coral", "144 ms"), ("Plazo total", 2000, "grey", "2000 ms")], 20, 44, 0.3, label_w=250, step=46)
    f.box(20, 290, 900, 60, "Un plazo total acota la experiencia; los límites por fase (conexión, lectura) evitan que una fase consuma todo el presupuesto y permiten diagnosticar cuál se agotó.", "gold", 13)
    f.box(20, 360, 900, 50, "Con una petición de ≈430 ms, un plazo de 2 s permite como máximo unos 4 intentos sin espera, y mucho menos con retroceso.", "grey", 13)
    return f


def se048_degradacion() -> Fig:
    return mapa("Matriz sana, degradada y recuperada",
                "Tres estados del servicio, cada uno con su señal, la respuesta del cliente y la evidencia: sano, degradado con reintento que se recupera y fallido con mensaje por fase.",
                [("Sano. Señal: 200 en el primer intento", "Sin reintento", "teal", "healthy: dns → connect → http"),
                 ("Degradado y recuperado. Señal: 503 o pérdida transitoria", "Reintento acotado con retroceso", "gold", "http_503 y transient_loss: 2 intentos, recovered"),
                 ("Fallido por fase. Señal: DNS, rechazo, nombre TLS o plazo", "Sin reintento ciego; mensaje con fase y código", "coral", "dns_failure, connection_refused, tls_name_mismatch, latency_timeout")],
                note="Cada estado tiene una señal medible y una respuesta definida: sin esa matriz, el comportamiento ante fallos se decide en producción y a las 3 de la madrugada.",
                left_w=290, mid_w=260, row_h=76, heads=("Estado y señal", "Respuesta del cliente", "Evidencia"))


FIGURES = {
    "se-042-cabeceras-reales.svg": se042_cabeceras,
    "se-042-metodos-y-estados.svg": se042_metodos,
    "se-042-compresion-y-validacion.svg": se042_compresion,
    "se-043-certificado-observado.svg": se043_certificado,
    "se-043-veredictos-locales.svg": se043_veredictos,
    "se-043-almacen-de-confianza.svg": se043_almacen,
    "se-044-proxy-y-cabeceras.svg": se044_proxy,
    "se-044-balanceo-y-failover.svg": se044_balanceo,
    "se-044-cdn-observable-y-oculto.svg": se044_cdn,
    "se-045-reutilizar-conexion.svg": se045_reutilizar,
    "se-045-contrapresion.svg": se045_contrapresion,
    "se-045-ciclo-de-vida-del-socket.svg": se045_ciclo,
    "se-046-variacion-por-fase.svg": se046_variacion,
    "se-046-rtt-y-perdida.svg": se046_rtt,
    "se-046-puntos-de-observacion.svg": se046_puntos,
    "se-047-suite-del-laboratorio.svg": se047_suite,
    "se-047-correlacion.svg": se047_correlacion,
    "se-047-pruebas-en-dos-plataformas.svg": se047_pruebas,
    "se-048-reintento-con-backoff.svg": se048_backoff,
    "se-048-presupuesto-de-tiempo.svg": se048_presupuesto,
    "se-048-matriz-de-degradacion.svg": se048_degradacion,
}
