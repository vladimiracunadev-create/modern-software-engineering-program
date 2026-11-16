"""Figures for SE-037 to SE-042 (values measured on Windows 11 and Ubuntu 24.04 under WSL2)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars
from figure_flows import columnas, mapa

OBS = "Medido con curl, Python y ping desde un equipo concreto; los valores cambian con la red y la hora."


def _note(f: Fig, y: float, text: str = OBS) -> None:
    f.text(f.width / 2, y, text, 12, "middle", 400, "#5c1f14")


# ---------------------------------------------------------------- SE-037
def se037_fases() -> Fig:
    f = Fig(940, 430, "Una petición HTTPS a example.com descompuesta en fases (mediana de cinco)",
            "Barras con una medición real: resolver el nombre tarda unos 9 ms desde caché, el handshake TCP unos 131 ms, TLS unos 146 ms y la espera de la respuesta unos 144 ms; el total ronda 430 ms. "
            "Cada fase cuesta aproximadamente un viaje de ida y vuelta.")
    f.text(20, 28, "Fases acumuladas de curl -w (milisegundos)", 14, "start", 700)
    f.hbars([("DNS (aplicación)", 9, "gold", "9 ms"), ("TCP: SYN, SYN-ACK, ACK", 131, "teal", "131 ms"),
             ("TLS 1.3: un viaje de ida y vuelta", 146, "teal", "146 ms"), ("HTTP: solicitud y primer byte", 144, "coral", "144 ms")],
            20, 44, 2.2, label_w=250, step=48)
    f.box(20, 252, 900, 70, "Ping al mismo destino: mínimo 129 ms, media 146 ms, máximo 176 ms, sin pérdida. Las tres fases de red duran cerca de un RTT cada una: "
          "tres viajes de ida y vuelta hacen unos 430 ms.", "grey", 13)
    f.box(20, 334, 900, 56, "La fase que se alarga indica la capa: DNS lento apunta al resolvedor, TCP lento a la ruta, TLS lento a la negociación, y «espera» a la aplicación o al intermediario.", "gold", 13)
    _note(f, 416)
    return f


def se037_modelos() -> Fig:
    return mapa("Los modelos OSI y TCP/IP aplicados a una petición observada",
                "Cinco capas apiladas de la aplicación al enlace; de cada una salen la evidencia real observada en una petición a example.com (estado HTTP 200, handshake TLS 1.3, conexión TCP, TTL 56 de IP y MTU 1500 del enlace) y lo que esa evidencia no demuestra.",
                [("7 Aplicación (TCP/IP: Aplicación)", "HTTP/1.1 200 OK; Content-Type text/html; 577 bytes", "teal", "Que el contenido sea el correcto para la persona"),
                 ("6 Presentación / 5 Sesión (TCP/IP: Aplicación)", "TLS 1.3 con TLS_AES_256_GCM_SHA384; certificado para example.com", "teal", "Que el servidor sea quien dice más allá del nombre"),
                 ("4 Transporte (TCP/IP: Transporte)", "Conexión TCP al puerto 443 establecida en ≈131 ms", "teal", "Que la aplicación esté sana (solo que el puerto escucha)"),
                 ("3 Red (TCP/IP: Internet)", "ping: TTL = 56 y RTT medio de 146 ms", "teal", "El número exacto de saltos: el TTL inicial es desconocido"),
                 ("2 Enlace / 1 Física (TCP/IP: Acceso a red)", "MTU de 1500 en la interfaz; el límite de 1472 bytes de datos con DF activado", "teal", "Qué medio (cable, Wi-Fi) usa cada tramo")],
                note="Los modelos son herramientas para ubicar una observación; una capa «ve» solo lo que su contrato le muestra, y varias capas pueden estar a cargo de componentes distintos.",
                left_w=220, mid_w=360, row_h=62, size=12, stack=True, heads=("Capa OSI (y su capa TCP/IP)", "Evidencia observada", "No demuestra"))


def se037_fugas() -> Fig:
    return mapa("Cuando las capas «filtran»: tres observaciones reales",
                "Tres fugas de capa observadas, cada una con la capa que parece responder y lo que ocurre en realidad: el servidor responde como cloudflare con Age 3521 (un intermediario sirve una copia de caché), alt-svc anuncia h3 (otro transporte) y un ping que responde no demuestra que el servicio funcione.",
                [("Server: cloudflare; Age: 3521", "Parece responder: el origen del sitio", "gold", "Un intermediario (CDN) termina TLS y sirve una copia con 3521 s de antigüedad"),
                 ("alt-svc: h3=\":443\"", "Parece responder: HTTP/1.1 sobre TCP", "gold", "El servidor ofrece HTTP/3 sobre QUIC (UDP) para próximas conexiones"),
                 ("ping responde (TTL 56, 146 ms)", "Parece responder: el servicio funciona", "gold", "Solo hay respuesta ICMP bajo esa ruta y política; DNS, puerto, TLS y HTTP no se probaron")],
                note="Una conclusión sobre una capa necesita evidencia de esa capa: el contenido de la respuesta no prueba quién la generó, ni el éxito de una capa inferior prueba las superiores.",
                note_kind="coral", left_w=260, mid_w=260, row_h=76, heads=("Observación", "Qué capa parece responder", "Qué ocurre en realidad"))


# ---------------------------------------------------------------- SE-038
def se038_trama() -> Fig:
    f = Fig(960, 450, "Una trama Ethernet y de dónde sale el límite de 1472 bytes",
            "Una trama Ethernet de 1518 bytes: 14 de cabecera, 1500 de carga útil (MTU) y 4 de verificación. Dentro de la carga, 20 bytes de IPv4, 8 de ICMP y 1472 de datos. "
            "Con la bandera de no fragmentar, los pings de 1372 y 1472 bytes de datos pasan y el de 1473 no.")
    f.text(20, 28, "Trama Ethernet (bytes)", 14, "start", 700)
    f.box(20, 44, 90, 60, "Cabecera\n14 B", "grey", 12, bold=True)
    f.box(110, 44, 700, 60, "Carga útil (MTU) = 1500 B", "teal", 13, bold=True)
    f.box(810, 44, 90, 60, "FCS\n4 B", "grey", 12, bold=True)
    f.text(20, 140, "Dentro de la carga útil de un ping", 14, "start", 700)
    f.box(110, 156, 90, 60, "IPv4\n20 B", "gold", 12, bold=True)
    f.box(200, 156, 70, 60, "ICMP\n8 B", "gold", 12, bold=True)
    f.box(270, 156, 540, 60, "Datos del ping: 1472 B", "plain", 13, bold=True)
    f.text(20, 252, "Tres pruebas con ping -f (no fragmentar)", 14, "start", 700)
    probes = [("datos de 1372 B", "Respuesta: bytes=1372, 143 ms", "teal"),
              ("datos de 1472 B (20 + 8 + 1472 = 1500)", "Respuesta: bytes=1472, 164 ms", "teal"),
              ("datos de 1473 B", "«Es necesario fragmentar el paquete pero se especificó DF»", "coral")]
    for i, (what, result, kind) in enumerate(probes):
        x = 20 + i * 300
        f.box(x, 266, 280, 40, what, "navy", 12, True)
        f.arrow([(x + 140, 306), (x + 140, 322)])
        f.box(x, 322, 280, 54, result, kind, 12)
    f.box(20, 392, 880, 44, "El MTU de la ruta hasta ese destino es de 1500 bytes. Los túneles y las VPN lo reducen y la fragmentación o los agujeros negros de PMTU aparecen como fallos intermitentes.", "gold", 12)
    return f


def se038_mtu() -> Fig:
    return grouped_bars("MTU medidos: la interfaz local, el enlace y la ruta",
                        "Barras horizontales en escala logarítmica con los MTU observados dentro de WSL2: 65 536 bytes en loopback y 1500 en eth0, más el límite de ruta de 1500 comprobado con ping y DF desde Windows.",
                        ["Loopback (lo)", "Interfaz eth0 de WSL2", "Ruta hasta example.com"],
                        [("MTU observado", [65536, 1500, 1500], "teal")],
                        unit="bytes", horizontal=True, log=True, ticks=[1000, 10000, 100000],
                        note="El loopback no sale a ningún medio: su límite es de software. En eth0 (ip -o link) el 1500 es el valor típico de Ethernet, y en la ruta se obtuvo porque ping -f -l 1472 funciona y 1473 no, así que ningún tramo reduce el MTU por debajo de 1500. "
                             "El MTU efectivo de una ruta es el mínimo de todos sus tramos: se descubre con una prueba (PMTU) y no se deduce de la interfaz local.")


def se038_siguiente_salto() -> Fig:
    f = Fig(960, 460, "Siguiente salto en una red local: misma subred o gateway (modelo con direcciones de documentación)",
            "Dos casos: si el destino está en el mismo prefijo, el emisor resuelve con ARP la dirección de enlace del destino; si está en otro prefijo, resuelve la del gateway y le entrega la trama.")
    f.box(20, 30, 250, 70, "Equipo 192.0.2.10/24\ntabla de rutas local", "navy", 13, bold=True)
    f.box(380, 20, 270, 70, "¿192.0.2.77 está en 192.0.2.0/24? Sí → ARP de 192.0.2.77", "teal", 13)
    f.box(380, 120, 270, 70, "¿198.51.100.5 está en 192.0.2.0/24? No → ARP del gateway 192.0.2.1", "gold", 13)
    f.arrow([(270, 55), (380, 55)])
    f.arrow([(270, 75), (380, 150)])
    f.box(710, 20, 230, 70, "Trama a la MAC del destino", "plain", 13)
    f.box(710, 120, 230, 70, "Trama a la MAC del gateway; el paquete IP conserva el destino final", "plain", 13)
    f.arrow([(650, 55), (710, 55)])
    f.arrow([(650, 155), (710, 155)])
    f.box(20, 230, 920, 76, "La dirección de enlace (MAC) cambia en cada salto; la dirección IP de destino se mantiene hasta el final (salvo NAT). Por eso un fallo de ARP afecta solo a la red local.", "grey", 13)
    f.box(20, 318, 920, 70, "Modelo con direcciones del rango de documentación (RFC 5737): no se midió una red real. Los dispositivos con Wi-Fi añaden asociación y reintentos de capa 2 que ocultan pérdidas.", "coral", 13)
    return f


# ---------------------------------------------------------------- SE-039
def se039_subredes() -> Fig:
    return grouped_bars("Aritmética de subredes calculada con ipaddress",
                        "Barras horizontales en escala logarítmica con el número de direcciones calculado con ipaddress: 254 hosts en 192.0.2.0/24, 62 en 192.0.2.64/26 y 18 446 744 073 709 551 616 direcciones en un /64 de IPv6.",
                        ["Hosts de 192.0.2.0/24", "Hosts de 192.0.2.64/26", "Direcciones de un /64 de IPv6"],
                        [("Direcciones", [254, 62, 2 ** 64], "teal")],
                        unit="direcciones", horizontal=True, log=True, ticks=[10, 10 ** 6, 10 ** 12, 10 ** 18],
                        value_fmt=lambda v: "18 446 744 073 709 551 616" if v > 1e15 else f"{v:g}",
                        note="Cada cuenta es una potencia: 2^(32-24) = 256 direcciones menos red y difusión da 254; 2^(32-26) = 64 menos 2 da 62 (de .64 a .127); 2^(128-64) da el /64. 192.0.2.70 pertenece a la /26 y 192.0.2.200 no (se compara el prefijo de 26 bits), "
                             "y 2001:0db8:0000:...:0001 se comprime como 2001:db8::1. La máscara decide qué es «local»: un error de un bit en el prefijo cambia el conjunto de direcciones alcanzables sin pasar por el gateway.")


def se039_clasificacion() -> Fig:
    f = Fig(960, 430, "Clasificar direcciones: lo que informa el módulo ipaddress",
            "Seis direcciones agrupadas en cuatro cajones según lo que son realmente, cada una con el valor que devuelve is_private: 10.1.2.3, 172.20.0.1 y 192.168.1.1 son privadas de la RFC 1918; 192.0.2.5 es de documentación y se informa como privada; "
            "100.64.0.1 es espacio compartido de CGNAT y se informa como no privada, igual que la pública 8.8.8.8.")
    buckets = [("Espacio privado de la RFC 1918", "teal", [("10.1.2.3", "Sí"), ("172.20.0.1", "Sí"), ("192.168.1.1", "Sí")]),
               ("Documentación (RFC 5737): no es una red real", "gold", [("192.0.2.5", "Sí")]),
               ("Espacio compartido de CGNAT (100.64.0.0/10): ni privado ni público", "coral", [("100.64.0.1", "No")]),
               ("Dirección pública", "grey", [("8.8.8.8", "No")])]
    for i, (name, kind, items) in enumerate(buckets):
        x = 10 + i * 238
        f.box(x, 14, 226, 78, name, kind, 12, True)
        f.box(x, 104, 226, 188, "", "plain", 12, dashed=True, radius=12)
        for j, (addr, priv) in enumerate(items):
            f.box(x + 12, 116 + j * 54, 202, 44, f"{addr}\nis_private = {priv}", kind, 12)
        f.arrow([(x + 113, 92), (x + 113, 104)])
    f.box(10, 312, 940, 56, "«Privada» no significa «de mi red»: una misma dirección privada existe en millones de redes, y CGNAT rompe la suposición de que «no privada» es pública y única.", "gold", 13)
    return f


def se039_entrega() -> Fig:
    f = Fig(960, 460, "Decisión de entrega, NAT y retorno",
            "Cuatro preguntas en orden: el prefijo del destino, el gateway, la traducción de direcciones del NAT y el MTU de la ruta. El NAT cambia direcciones y puertos y mantiene una tabla para el retorno.")
    steps = [
        ("1 Prefijo", "¿El destino está en una red conectada? Se entrega directamente; si no, se usa la ruta más específica", "teal"),
        ("2 Gateway", "La trama va a la MAC del siguiente salto; el TTL disminuye en cada router", "teal"),
        ("3 NAT", "El router sustituye la dirección privada por una pública y el puerto de origen, y recuerda la correspondencia", "gold"),
        ("4 Retorno y MTU", "La respuesta vuelve por la tabla del NAT; un paquete mayor que el MTU con DF se descarta y avisa por ICMP", "coral"),
    ]
    for i, (name, text, kind) in enumerate(steps):
        x = 14 + i * 236
        f.box(x, 20, 222, 44, name, "navy", 13, bold=True)
        f.box(x, 72, 222, 150, text, kind, 12)
        if i < 3:
            f.arrow([(x + 222, 42), (x + 236, 42)])
    f.box(14, 246, 930, 70, "Observado: TTL = 56 en la respuesta a ping y MTU de ruta de 1500. La mayoría de los equipos domésticos están tras un NAT: su dirección privada no es visible desde Internet.", "grey", 13)
    f.box(14, 330, 930, 66, "NAT dificulta las conexiones entrantes y obliga a mantener estado; IPv6 reduce la necesidad de NAT pero no de cortafuegos.", "plain", 13)
    return f


# ---------------------------------------------------------------- SE-040
def se040_estados() -> Fig:
    f = Fig(960, 430, "Estados TCP observados con ss durante una conexión local",
            "Cuatro momentos observados en Linux: solo LISTEN; luego ESTAB en ambos extremos; cuando el cliente cierra primero, el servidor queda en CLOSE-WAIT y el cliente en FIN-WAIT-2; "
            "al cerrar el servidor queda un TIME-WAIT.")
    steps = [("1 Escuchando", "LISTEN", "teal"), ("2 Conectado", "ESTAB · ESTAB · LISTEN", "teal"), ("3 El cliente cerró", "CLOSE-WAIT · FIN-WAIT-2 · LISTEN", "gold"), ("4 Ambos cerraron", "TIME-WAIT · LISTEN", "coral")]
    for i, (name, state, kind) in enumerate(steps):
        x = 14 + i * 236
        f.box(x, 20, 222, 44, name, "navy", 13, bold=True)
        f.box(x, 72, 222, 80, state, kind, 13, bold=True)
        if i < 3:
            f.arrow([(x + 222, 42), (x + 236, 42)])
    f.box(14, 176, 930, 78, "CLOSE-WAIT en el servidor significa que el otro extremo cerró y la aplicación aún no cerró su lado: acumular CLOSE-WAIT indica conexiones que la aplicación no cierra.", "grey", 13)
    f.box(14, 266, 930, 70, "TIME-WAIT lo mantiene quien cierra primero durante un tiempo para absorber paquetes tardíos; no es un error ni una fuga.", "plain", 13)
    _note(f, 366, "Observado con ss -tan en Ubuntu 24.04 (WSL2) sobre sockets locales; no se capturaron paquetes.")
    return f


def se040_fronteras() -> Fig:
    return mapa("TCP no conserva fronteras de mensaje; UDP sí",
                "Cuatro pruebas con su resultado y su lectura: dos envíos TCP de 4 y 6 bytes se leyeron juntos como AAAABBBBBB, mientras dos datagramas UDP se leyeron por separado; enviar un datagrama a un puerto cerrado no da error al emisor, "
                "y la lectura posterior produjo ConnectionResetError en Windows y un timeout en Linux.",
                [("TCP: send(4 bytes) y send(6 bytes), una lectura", "«AAAABBBBBB» (10 bytes)", "gold", "El flujo no tiene fronteras: la aplicación necesita longitud o delimitador"),
                 ("UDP: dos datagramas, dos lecturas", "«AAAA» y «BBBBBB»", "teal", "Cada datagrama conserva su frontera"),
                 ("UDP: sendto a un puerto cerrado", "Devuelve 1 byte; sin error", "coral", "El emisor no sabe si llegó: no hay confirmación"),
                 ("UDP: lectura tras ese envío", "Windows: ConnectionResetError; Linux: TimeoutError", "coral", "El aviso de ICMP se entrega distinto por plataforma")],
                note="El comportamiento de errores asíncronos de UDP no es portable: una aplicación no debe depender de él para detectar pérdida.",
                left_w=310, mid_w=290, row_h=70, heads=("Prueba", "Resultado observado", "Lectura"))


def se040_rechazo() -> Fig:
    f = Fig(960, 500, "Rechazo, silencio y la espera de Nagle: tres mediciones",
            "Panel 1: conectar a un puerto local cerrado produce ConnectionRefusedError en 0,06 ms en Linux y un TimeoutError de 2 s en Windows; un destino sin ruta produce timeout de 2 s en ambos. "
            "Panel 2: reutilizar una conexión HTTP en Linux tarda 44,1 ms por petición con dos escrituras, y 0,34 ms con TCP_NODELAY o una sola escritura.")
    f.text(20, 26, "1 · Conectar con un puerto cerrado o sin ruta (timeout de 2 s)", 14, "start", 700)
    f.box(380, 36, 270, 28, "Linux (WSL2)", "teal", 12, True)
    f.box(658, 36, 282, 28, "Windows", "gold", 12, True)
    for y, dest, lin, win in ((74, "Puerto local cerrado", "ConnectionRefusedError en 0,06 ms (RST)", "TimeoutError tras 2000 ms"),
                              (138, "192.0.2.1:80 (sin ruta)", "TimeoutError tras 2,0 s", "TimeoutError tras 2,0 s")):
        f.box(20, y, 300, 50, dest, "plain", 12, True)
        f.box(370, y - 5, 580, 60, "", "plain", 12, dashed=True, radius=12)
        f.arrow([(320, y + 25), (370, y + 25)])
        if lin == win:
            f.box(380, y, 560, 50, lin + " en ambos", "grey", 12)
        else:
            f.box(380, y, 270, 50, lin, "teal", 12)
            f.box(658, y, 282, 50, win, "gold", 12)
    f.text(20, 220, "2 · Una petición por conexión reutilizada (ms por petición, 60 repeticiones)", 14, "start", 700)
    f.hbars([("Linux: dos escrituras", 44.12, "coral", "44,12 ms"), ("Linux: TCP_NODELAY", 0.34, "teal", "0,34 ms"), ("Linux: una escritura con búfer", 0.31, "teal", "0,31 ms"),
             ("Windows: dos escrituras", 0.6, "gold", "0,60 ms")], 20, 236, 6, label_w=260, step=40)
    f.box(20, 410, 920, 62, "En Linux, el algoritmo de Nagle retiene el segundo envío hasta recibir el ACK retrasado del primero (unos 40 ms). Se evita escribiendo cabeceras y cuerpo juntos o con TCP_NODELAY.", "gold", 13)
    return f


# ---------------------------------------------------------------- SE-041
def se041_resolucion() -> Fig:
    f = Fig(940, 440, "Cuánto tarda resolver un nombre: primera consulta, caché y fallo",
            "Barras con una medición real de getaddrinfo: example.com tarda 35,9 ms en la primera consulta y 0,5 ms en la segunda en Windows, y 14,3 ms y 8,2 ms en Linux (WSL2); un nombre inexistente tarda 11,7 y 9,4 ms.")
    f.text(20, 28, "getaddrinfo (milisegundos)", 14, "start", 700)
    f.hbars([("Windows, 1.ª consulta", 35.9, "gold", "35,9 ms"), ("Windows, 2.ª consulta", 0.5, "teal", "0,5 ms"), ("Linux, 1.ª consulta", 14.3, "gold", "14,3 ms"),
             ("Linux, 2.ª consulta", 8.2, "teal", "8,2 ms"), ("Nombre inexistente (Windows)", 11.7, "coral", "11,7 ms"), ("Nombre inexistente (Linux)", 9.4, "coral", "9,4 ms")],
            20, 44, 11, label_w=260, step=44)
    f.box(20, 320, 900, 70, "La segunda consulta es mucho más rápida en Windows (caché del cliente); en WSL2 la caché local es menor o inexistente y cada consulta cruza hacia el resolvedor. Un fallo también cuesta tiempo.", "grey", 13)
    _note(f, 420)
    return f


def se041_registros() -> Fig:
    return grouped_bars("Registros de example.com consultados al resolvedor 1.1.1.1",
                        "Barras horizontales en escala logarítmica con el TTL restante de cada tipo de registro: A (2 respuestas) 179 s, AAAA (2) 46 s, NS (2) 68 664 s, MX (1) 300 s, TXT (2) 300 s, y la respuesta negativa de un nombre inexistente con un SOA de TTL 1800 s.",
                        ["A (2 respuestas)", "AAAA (2 respuestas)", "NS (2 respuestas)", "MX (1 respuesta)", "TXT (2 respuestas)", "NXDOMAIN (SOA de la zona)"],
                        [("TTL restante", [179, 46, 68664, 300, 300, 1800], "teal")],
                        unit="segundos", horizontal=True, log=True, ticks=[10, 100, 1000, 10000, 100000],
                        note="A y AAAA guardan las direcciones IPv4 e IPv6; NS, los servidores autoritativos de la zona (TTL largo); MX es aquí un registro de MX nulo; TXT, texto libre (verificaciones, políticas); y NXDOMAIN muestra que la ausencia también se guarda en caché (RFC 2308). "
                             "El TTL que ves es el tiempo restante en la caché del resolvedor, no el TTL configurado en la zona.")


def se041_distintas() -> Fig:
    return columnas("El mismo nombre, dos entornos, respuestas distintas",
                    "Tres consultas con el resultado real de getaddrinfo en cada entorno: example.com devolvió 2 direcciones IPv4 en Windows y 4 direcciones (IPv4 e IPv6) en Linux; localhost devolvió 2 direcciones en Windows y 1 en Linux; "
                    "un nombre inexistente produjo el código 11001 en Windows y -2 en Linux.",
                    [("example.com (puerto 443)", "2 direcciones, solo IPv4", "4 direcciones: IPv4 e IPv6"),
                     ("localhost", "2 direcciones: IPv4 e IPv6", "1 dirección: IPv4"),
                     ("no-existe.invalid", "Errno 11001: getaddrinfo failed", "Errno -2: Name or service not known")],
                    ["Windows", "Linux (WSL2)"], ["gold", "teal"],
                    note="La resolución es una función del entorno: familias de direcciones, caché, resolvedor y códigos de error difieren. Un diagnóstico declara dónde se resolvió y con qué herramienta.",
                    label_w=300, row_h=64)


FIGURES = {
    "se-037-fases-de-una-peticion.svg": se037_fases,
    "se-037-modelos-y-evidencia.svg": se037_modelos,
    "se-037-fugas-de-capa.svg": se037_fugas,
    "se-038-trama-y-mtu.svg": se038_trama,
    "se-038-mtu-medidos.svg": se038_mtu,
    "se-038-siguiente-salto.svg": se038_siguiente_salto,
    "se-039-subredes-calculadas.svg": se039_subredes,
    "se-039-clasificacion-de-direcciones.svg": se039_clasificacion,
    "se-039-decision-de-entrega.svg": se039_entrega,
    "se-040-estados-tcp-observados.svg": se040_estados,
    "se-040-fronteras-tcp-udp.svg": se040_fronteras,
    "se-040-rechazo-silencio-nagle.svg": se040_rechazo,
    "se-041-resolucion-medida.svg": se041_resolucion,
    "se-041-registros-y-ttl.svg": se041_registros,
    "se-041-mismo-nombre-otro-entorno.svg": se041_distintas,
}
