"""Figures for SE-042 to SE-048 (values measured on Windows 11 and Ubuntu 24.04 under WSL2)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part03_a import _note


# ---------------------------------------------------------------- SE-042
def se042_cabeceras() -> Fig:
    f = Fig(940, 440, "Cabeceras reales de https://example.com",
            "Tabla con las cabeceras observadas: Content-Type text/html; charset=utf-8, Server cloudflare, Last-Modified del 13 de noviembre de 2026, Age 3521 segundos, alt-svc que anuncia h3, y sin ETag.")
    heads = ["Cabecera", "Valor observado", "Qué comunica"]
    rows = [
        ["Content-Type", "text/html; charset=utf-8", "Tipo de medio y codificación del cuerpo"],
        ["Server", "cloudflare", "Quién responde: un intermediario, no necesariamente el origen"],
        ["Last-Modified", "Fri, 13 Nov 2026 08:41:42 GMT", "Validador débil basado en tiempo"],
        ["Age", "3521", "La copia tiene 3521 s de antigüedad en la caché del intermediario"],
        ["alt-svc", "h3=\":443\"; ma=86400", "HTTP/3 disponible en el puerto 443 durante 86 400 s"],
        ["ETag", "(ausente)", "No hay validador fuerte: la validación usa la fecha"],
    ]
    f.table(heads, rows, 10, 12, [190, 330, 410], row_h=54, size=12)
    f.box(10, 398, 920, 34, "Las cabeceras son una conversación con el intermediario y el origen; cada una debe leerse con su semántica.", "gold", 12)
    return f


def se042_metodos() -> Fig:
    f = Fig(960, 470, "Métodos y estados: lo que respondió el servidor",
            "Tabla con resultados reales: GET 200 con 577 bytes, HEAD 200 sin cuerpo, POST y OPTIONS 405, una ruta inexistente 404, una petición condicional con If-Modified-Since 304, y un 503 con Retry-After de 1 segundo en un servidor local.")
    heads = ["Petición", "Estado", "Lectura"]
    rows = [
        ["GET /", "200 (577 B)", "Representación del recurso"],
        ["HEAD /", "200 (0 B de cuerpo)", "Mismas cabeceras, sin cuerpo: sirve para comprobar existencia y tamaño"],
        ["POST /", "405", "El método existe pero este recurso no lo admite"],
        ["OPTIONS /", "405", "El servidor no anuncia métodos con OPTIONS"],
        ["GET /no-existe", "404", "No hay recurso en esa ruta"],
        ["GET / con If-Modified-Since", "304", "No modificado: no se retransmite el cuerpo (ahorro de 577 B)"],
        ["GET /503 (servidor local)", "503 + Retry-After: 1", "Indisponibilidad temporal con una pista de cuándo reintentar"],
    ]
    f.table(heads, rows, 10, 12, [260, 190, 480], row_h=50, size=12)
    f.box(10, 430, 940, 34, "El número de estado es una decisión del servidor sobre el recurso, no un reflejo del éxito del negocio.", "gold", 12)
    return f


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
    f = Fig(960, 470, "Lo que muestra una conexión TLS real a example.com",
            "Tabla con los datos observados: TLS 1.3 con TLS_AES_256_GCM_SHA384, certificado con CN example.com y nombres alternativos example.com y *.example.com, emisor SSL Corporation, validez del 26 de septiembre al 25 de diciembre de 2026 (90 días), cadena de tres certificados más la raíz.")
    heads = ["Dato", "Valor observado", "Qué demuestra"]
    rows = [
        ["Versión y cifrado", "TLS 1.3 · TLS_AES_256_GCM_SHA384", "La sesión usa cifrado autenticado y claves efímeras"],
        ["Nombre del certificado", "CN = example.com; SAN: example.com, *.example.com", "El nombre que el cliente verifica es el de la SAN, no solo el CN"],
        ["Validez", "26 sep 2026 → 25 dic 2026 (90 días)", "Los certificados modernos son de vida corta; hay que renovarlos"],
        ["Cadena presentada", "hoja → Cloudflare TLS Issuing ECC CA 3 → SSL.com TLS Transit ECC CA R2 → raíz SSL.com TLS ECC Root CA 2022", "Confianza por cadena hasta una raíz que el cliente ya tiene"],
        ["Handshake", "≈145 ms (un viaje de ida y vuelta)", "TLS 1.3 completa la negociación en un RTT"],
    ]
    f.table(heads, rows, 10, 12, [190, 420, 330], row_h=70, size=12)
    f.box(10, 420, 940, 40, "El certificado prueba que el servidor controla el nombre, no que sea digno de confianza ni que su contenido sea correcto.", "gold", 12)
    return f


def se043_veredictos() -> Fig:
    f = Fig(960, 440, "Cuatro veredictos locales con un certificado de laboratorio",
            "Tabla con cuatro intentos reales contra un servidor TLS local con certificado autofirmado: sin confianza falla con self-signed certificate (código 18); con la CA del laboratorio funciona con TLS 1.3 y ALPN h2 en 3 ms; "
            "con otro nombre falla con Hostname mismatch (código 62); con la verificación desactivada funciona, pero sin protección.")
    heads = ["Intento", "Resultado", "Código", "Lectura"]
    rows = [
        ["Sin confiar en el certificado", "self-signed certificate", "18", "La cadena no llega a una raíz de confianza"],
        ["Confiando en la CA del laboratorio", "OK · TLS 1.3 · ALPN h2 · 3,0 ms", "—", "Confianza explícita y nombre correcto"],
        ["Nombre «otro.example»", "Hostname mismatch: el certificado no es válido para ese nombre", "62", "La cadena es válida pero el nombre no coincide"],
        ["Verificación desactivada", "OK · TLS 1.3 (sin ALPN)", "—", "Cifra pero no autentica: cualquiera puede suplantar al servidor"],
    ]
    f.table(heads, rows, 10, 12, [250, 340, 90, 260], row_h=66, size=12)
    f.box(10, 376, 940, 56, "Desactivar la verificación «para que funcione» elimina la propiedad que TLS ofrece frente a un atacante activo. Se corrige la confianza o el nombre, no la prueba.", "coral", 13)
    return f


def se043_almacen() -> Fig:
    f = Fig(960, 450, "El almacén de confianza también es parte del sistema",
            "Tabla con tres observaciones reales: Python en Windows falló con unable to get local issuer certificate al conectar a example.com y funcionó después de que curl con Schannel construyera la cadena, "
            "Python en Linux funcionó de inmediato, y un nombre desconocido recibió un alert de handshake failure.")
    heads = ["Observación", "Resultado", "Lectura"]
    rows = [
        ["Python en Windows, primer intento", "CERTIFICATE_VERIFY_FAILED: unable to get local issuer certificate (110 raíces cargadas)", "La raíz de la cadena no estaba aún en el almacén que Python leyó"],
        ["Tras una petición con curl (Schannel)", "Python funciona; la raíz «SSL.com TLS ECC Root CA 2022» ya aparece", "Windows incorpora raíces bajo demanda cuando construye una cadena"],
        ["Python en Linux (WSL2)", "Funciona a la primera", "El paquete de certificados de la distribución ya contenía la raíz"],
        ["SNI con un nombre desconocido (example.com)", "sslv3 alert handshake failure", "El servidor rechaza un nombre que no sirve: no es un error de certificado"],
    ]
    f.table(heads, rows, 10, 12, [260, 360, 320], row_h=76, size=12)
    f.box(10, 396, 940, 44, "Una misma conexión puede validarse o no según el almacén de cada cliente. Se declara qué almacén usa cada herramienta.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-044
def se044_proxy() -> Fig:
    f = Fig(960, 440, "Quién puede afirmar la IP del cliente: origen directo frente a proxy",
            "Tabla con una prueba local: una petición con X-Forwarded-For falso 203.0.113.99 enviada directamente al origen se acepta tal cual; enviada a través del proxy, el proxy sustituye la cabecera por la IP real 127.0.0.1, "
            "conserva el identificador de petición abc-123 y añade Via.")
    heads = ["Camino", "X-Forwarded-For que ve el origen", "X-Request-Id", "Via"]
    rows = [
        ["Cliente → origen (directo)", "203.0.113.99 (falsificado por el cliente)", "—", "—"],
        ["Cliente → proxy → origen", "127.0.0.1 (la dirección real vista por el proxy)", "abc-123 (propagado)", "1.1 proxy-local"],
    ]
    f.table(heads, rows, 10, 12, [250, 330, 190, 170], row_h=86, size=12)
    f.box(10, 260, 940, 80, "Una cabecera reenviada solo es confiable si la fija un componente de confianza y el origen rechaza o sobrescribe lo que llega de fuera de esa frontera.", "coral", 13)
    f.box(10, 350, 940, 66, "La política: el borde descarta las cabeceras entrantes de identidad, fija las suyas y el origen solo acepta conexiones del proxy.", "gold", 13)
    return f


def se044_balanceo() -> Fig:
    f = Fig(940, 440, "Balanceo y conmutación por falla: lo que se observó",
            "Tabla con una prueba local: 20 peticiones en turno rotatorio se reparten 10 y 10; tras detener el origen A, las 20 peticiones acabaron en B con reintento; "
            "detectar el fallo tardó 0,35 ms en Linux y 499,9 ms en Windows (la espera hasta el timeout de conexión).")
    heads = ["Situación", "Linux (WSL2)", "Windows"]
    rows = [
        ["20 peticiones en turno rotatorio (A y B sanos)", "A = 10, B = 10", "A = 10, B = 10"],
        ["A detenido; las 20 peticiones terminan en B", "20 en B; 10 fallos detectados al conectar", "20 en B; 10 fallos detectados al conectar"],
        ["Tiempo del primer fallo detectado", "0,35 ms (rechazo inmediato)", "499,9 ms (espera hasta el timeout)"],
    ]
    f.table(heads, rows, 10, 12, [380, 280, 280], row_h=70, size=12)
    f.box(10, 320, 920, 70, "Un balanceador sin comprobaciones de salud sigue enviando tráfico al origen caído. El costo de descubrir la caída depende de cómo falla la conexión y del timeout elegido.", "gold", 13)
    _note(f, 416, "Orígenes y balanceo simulados en loopback; no se midió un balanceador real.")
    return f


def se044_cdn() -> Fig:
    f = Fig(960, 440, "Qué se observa y qué queda oculto detrás de una CDN",
            "Tabla con las observaciones desde el cliente: Server cloudflare, Age 3521, alt-svc h3 y un certificado emitido por una CA intermedia de Cloudflare; no se ve el origen, su certificado ni el número de nodos de borde.")
    heads = ["Observable desde el cliente", "No observable"]
    rows = [
        ["Server: cloudflare · Age: 3521 s · alt-svc: h3", "Qué servidor de origen existe y en qué región"],
        ["Un certificado de 90 días para example.com emitido por una CA intermedia", "Si el tráfico hacia el origen también va cifrado"],
        ["RTT medio de 146 ms hasta el nodo que responde", "En qué nodo de borde cayó la petición"],
        ["La respuesta tenía 3521 s de antigüedad", "Cuándo fue la última validación con el origen"],
    ]
    f.table(heads, rows, 10, 12, [490, 450], row_h=68, size=13)
    f.box(10, 360, 940, 60, "Una CDN es un intermediario: reduce latencia y carga, pero añade capas en las que pueden fallar la caché, el certificado o las cabeceras. Diagnosticar exige conocer cuál respondió.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-045
def se045_reutilizar() -> Fig:
    f = Fig(940, 440, "Reutilizar la conexión: cuánto ahorra y cuándo no",
            "Tabla con mediciones en loopback: en Windows abrir una conexión por petición tardó 1,396 ms y reutilizarla 0,366 ms (3,8 veces menos); en Linux la reutilización tardó 44,1 ms con dos escrituras por respuesta y 0,31 ms con una sola.")
    heads = ["Medición", "Resultado", "Lectura"]
    rows = [
        ["Windows: una conexión por petición", "1,396 ms", "Incluye el handshake TCP en cada petición"],
        ["Windows: conexión reutilizada", "0,366 ms (3,8 veces menos)", "El ahorro del handshake y del arranque lento"],
        ["Linux: reutilizada, cabeceras y cuerpo en dos escrituras", "44,12 ms", "Nagle + ACK retrasado: ≈ 40 ms de espera por petición"],
        ["Linux: reutilizada, una sola escritura o TCP_NODELAY", "0,31 ms / 0,34 ms", "Sin espera: la reutilización vuelve a ayudar"],
    ]
    f.table(heads, rows, 10, 12, [330, 220, 390], row_h=64, size=12)
    f.box(10, 352, 920, 64, "Reutilizar conexiones es casi siempre una ventaja, pero un detalle del envío puede anularla. Se mide con tu servidor real antes de generalizar.", "gold", 13)
    return f


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
    f = Fig(960, 470, "Cinco mediciones seguidas de la misma petición: variación por fase",
            "Tabla con cinco ejecuciones de curl -w contra https://example.com: el TCP tarda entre 131 y 159 ms, TLS entre 142 y 149 ms, la espera entre 137 y 169 ms y el total entre 426 y 480 ms.")
    heads = ["Ejecución", "DNS", "TCP", "TLS", "Espera", "Total"]
    runs = [(0.009233, 0.140613, 0.285776, 0.429907, 0.430245), (0.008483, 0.167068, 0.310527, 0.479185, 0.479520),
            (0.008808, 0.144154, 0.286818, 0.434600, 0.434950), (0.008812, 0.139805, 0.288849, 0.425489, 0.425846),
            (0.009671, 0.140327, 0.282572, 0.426745, 0.427094)]
    rows = []
    for i, (d, c, a, s, t) in enumerate(runs, start=1):
        rows.append([f"{i}", f"{d*1000:.0f}", f"{(c-d)*1000:.0f}", f"{(a-c)*1000:.0f}", f"{(s-a)*1000:.0f}", f"{t*1000:.0f}"])
    cols = list(zip(*[[float(c) for c in r[1:]] for r in rows]))
    rows.append(["mínimo–máximo"] + [f"{min(c):.0f}–{max(c):.0f}" for c in cols])
    f.table(heads, rows, 10, 12, [200, 140, 160, 160, 160, 120], row_h=46, size=13)
    f.box(10, 408, 940, 50, "Milisegundos por fase (intervalos, no acumulados). Una sola medición esconde que una fase pudo variar 30 ms: se repite y se reporta el rango.", "gold", 13)
    return f


def se046_rtt() -> Fig:
    f = Fig(940, 400, "Ida y vuelta y pérdida: ping y pruebas dirigidas",
            "Tabla con diez pings reales a example.com: sin pérdida, RTT mínimo 129 ms, medio 146 ms y máximo 176 ms; con la bandera DF, los paquetes de 1372 y 1472 bytes pasaron en 143 y 164 ms.")
    heads = ["Prueba", "Resultado", "Lectura"]
    rows = [
        ["ping × 10 (ICMP)", "0 % perdidos · mín 129 ms · media 146 ms · máx 176 ms", "El RTT varía unos 47 ms entre mínimo y máximo"],
        ["ping con DF, 1372 y 1472 B", "143 ms y 164 ms", "El tamaño no cambia la latencia de forma notable en este rango"],
        ["Ruta sin respuesta (modelo del laboratorio)", "Timeout de conexión", "Sin respuesta no distingue pérdida, filtrado o ruta rota"],
    ]
    f.table(heads, rows, 10, 12, [260, 380, 300], row_h=72, size=12)
    f.box(10, 320, 920, 64, "ICMP puede recibir un trato distinto del tráfico de aplicación: el RTT de ping orienta, pero la latencia de la aplicación se mide con la aplicación.", "gold", 13)
    return f


def se046_puntos() -> Fig:
    f = Fig(960, 450, "Dónde se observa: cada punto de vista ve algo distinto",
            "Tabla de cuatro puntos de observación: el cliente (curl -w), el servidor (registros), el sistema operativo (ss) y la red (captura de paquetes, no ejecutada aquí), con lo que cada uno ve y lo que no.")
    heads = ["Punto", "Qué ve", "Qué no ve", "Estado aquí"]
    rows = [
        ["Cliente (curl -w, temporizadores)", "Fases: DNS, TCP, TLS, espera", "Qué ocurrió en el servidor", "Medido"],
        ["Servidor (registros con request ID)", "Cuándo llegó y cuánto tardó el procesamiento", "Lo que pasó antes de llegar", "Lab local"],
        ["Sistema operativo (ss -tan)", "Estados de conexión: ESTAB, CLOSE-WAIT, TIME-WAIT", "El contenido ni los tiempos de red", "Medido"],
        ["Red (captura de paquetes)", "Segmentos, retransmisiones y ventanas", "El resultado de negocio; exige permisos y cuida la privacidad", "No ejecutado"],
    ]
    f.table(heads, rows, 10, 12, [250, 270, 280, 140], row_h=76, size=12)
    f.box(10, 410, 940, 36, "Una captura no era necesaria para este diagnóstico; cuando lo es, se limita interfaz, destino, tiempo y campos.", "gold", 12)
    return f


# ---------------------------------------------------------------- SE-047
def se047_suite() -> Fig:
    f = Fig(960, 480, "Los siete escenarios del laboratorio y su primera divergencia",
            "Tabla con la suite real: healthy es ok; dns_failure falla en dns (name_not_found); connection_refused en connect (refused); tls_name_mismatch en tls (name_mismatch); latency_timeout en http_wait (deadline_exceeded); "
            "transient_loss y http_503 se recuperan en el segundo intento.")
    heads = ["Escenario", "Resultado", "Intentos", "Primera divergencia"]
    rows = [
        ["healthy", "ok", "1", "—  (dns → connect → http → correlation)"],
        ["dns_failure", "failed", "0", "dns · name_not_found"],
        ["connection_refused", "failed", "1", "connect · refused"],
        ["tls_name_mismatch", "failed", "0", "tls · name_mismatch"],
        ["latency_timeout", "failed", "1", "http_wait · deadline_exceeded"],
        ["transient_loss", "recovered", "2", "transport (pérdida) → reintento → http"],
        ["http_503", "recovered", "2", "http 503 → reintento → http 200"],
    ]
    f.table(heads, rows, 10, 12, [240, 160, 120, 400], row_h=50, size=13)
    f.box(10, 436, 940, 36, "Se compara por la primera fase que difiere del caso sano, no por el número de errores posteriores.", "gold", 12)
    return f


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
    f = Fig(940, 400, "Las once pruebas del laboratorio en dos plataformas",
            "Tabla: las once pruebas del laboratorio de la Parte 03 pasaron en Windows 11 con Python 3.12.9 en 7,56 segundos y en Ubuntu 24.04 bajo WSL2 con Python 3.12.3 en 6,38 segundos.")
    heads = ["Plataforma", "Python", "Pruebas", "Resultado", "Duración"]
    rows = [["Windows 11", "3.12.9", "11", "todas pasan", "7,56 s"], ["Linux (WSL2)", "3.12.3", "11", "todas pasan", "6,38 s"]]
    f.table(heads, rows, 10, 12, [200, 140, 140, 220, 220], row_h=64, size=14)
    f.box(10, 220, 920, 90, "Las pruebas ejercitan los siete escenarios con un servidor HTTP efímero en 127.0.0.1; DNS, validación TLS y pérdida son modelos deterministas, y el tráfico HTTP es real y local.", "gold", 13)
    f.box(10, 322, 920, 56, "Pasar en dos plataformas no prueba el comportamiento en una red real: el laboratorio lo declara como límite.", "coral", 13)
    return f


# ---------------------------------------------------------------- SE-048
def se048_backoff() -> Fig:
    f = Fig(940, 430, "Reintento con retroceso exponencial y jitter contra un servicio que falla dos veces",
            "Tabla con una prueba local: el servidor responde 503 dos veces y luego 200; el cliente reintentó con espera aleatoria creciente y terminó en 99,7 ms en Windows y 70,7 ms en Linux.")
    heads = ["Intento", "Respuesta", "Espera antes del siguiente (jitter completo)"]
    rows = [["1", "503 Service Unavailable", "aleatoria entre 0 y 0,05 s"], ["2", "503 Service Unavailable", "aleatoria entre 0 y 0,10 s"], ["3", "200 OK", "—"]]
    f.table(heads, rows, 10, 12, [150, 330, 460], row_h=56, size=13)
    f.box(10, 244, 920, 56, "Tiempo total: 99,7 ms (Windows) y 70,7 ms (Linux). La espera máxima crece como 0,05 · 2^k y el azar evita que muchos clientes reintenten a la vez.", "gold", 13)
    f.box(10, 312, 920, 66, "Reintentar es seguro solo para operaciones idempotentes y con un tope de intentos y un plazo total; de lo contrario, multiplica la carga que causó el fallo.", "coral", 13)
    return f


def se048_presupuesto() -> Fig:
    f = Fig(940, 430, "Presupuesto de tiempo: del plazo total a los límites por fase",
            "Barras con las fases medidas de una petición HTTPS (DNS 9, TCP 131, TLS 146 y espera 144 ms, total 430 ms) frente a un plazo total de 2000 ms: sobran unos 1570 ms para reintentos.")
    f.text(20, 28, "Fases medidas frente al plazo total de 2000 ms", 14, "start", 700)
    f.hbars([("DNS", 9, "gold", "9 ms"), ("TCP", 131, "teal", "131 ms"), ("TLS", 146, "teal", "146 ms"), ("Espera de la respuesta", 144, "coral", "144 ms"), ("Plazo total", 2000, "grey", "2000 ms")], 20, 44, 0.3, label_w=250, step=46)
    f.box(20, 290, 900, 60, "Un plazo total acota la experiencia; los límites por fase (conexión, lectura) evitan que una fase consuma todo el presupuesto y permiten diagnosticar cuál se agotó.", "gold", 13)
    f.box(20, 360, 900, 50, "Con una petición de ≈430 ms, un plazo de 2 s permite como máximo unos 4 intentos sin espera, y mucho menos con retroceso.", "grey", 13)
    return f


def se048_degradacion() -> Fig:
    f = Fig(960, 440, "Matriz sana, degradada y recuperada",
            "Tabla de tres estados del servicio con su señal, su respuesta del cliente y la evidencia: sano, degradado con reintento que se recupera y fallido con mensaje por fase.")
    heads = ["Estado", "Señal", "Respuesta del cliente", "Evidencia"]
    rows = [
        ["Sano", "200 en el primer intento", "Sin reintento", "healthy: dns → connect → http"],
        ["Degradado y recuperado", "503 o pérdida transitoria", "Reintento acotado con retroceso", "http_503 y transient_loss: 2 intentos, recovered"],
        ["Fallido por fase", "DNS, rechazo, nombre TLS o plazo", "Sin reintento ciego; mensaje con fase y código", "dns_failure, connection_refused, tls_name_mismatch, latency_timeout"],
    ]
    f.table(heads, rows, 10, 12, [190, 230, 240, 280], row_h=84, size=12)
    f.box(10, 336, 940, 76, "Cada estado tiene una señal medible y una respuesta definida: sin esa matriz, el comportamiento ante fallos se decide en producción y a las 3 de la madrugada.", "gold", 13)
    return f


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
