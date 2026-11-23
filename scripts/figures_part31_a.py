"""Figures for SE-373 to SE-378 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3).

Every figure is a chart or a diagram of the mechanism; the Markdown tables of the classes keep the exact values.
"""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, line_chart, stacked_bars

SINT = "Datos sintéticos con semilla fija; CPython 3.12 en Windows y Ubuntu (WSL2); cifras idénticas salvo donde se indica."


# ---------------------------------------------------------------- SE-373
def se325_cadena() -> Fig:
    ks = [1, 2, 3, 4, 5]
    return line_chart(
        "Dependencias encadenadas: peticiones que terminan bien con un fallo del 1 % por llamada",
        "Líneas con el porcentaje de 200 000 peticiones que terminan bien según el número de dependencias de la cadena: la cadena síncrona medida cae de 99,02 a 95,20 por ciento y sigue de cerca la curva esperada 0,99 elevado a k; aceptar en una cola y completar con tres intentos por dependencia se queda entre 98,9 y 99,0 por ciento.",
        [("Síncrona medida", list(zip(ks, [99.02, 98.04, 96.99, 96.10, 95.20])), "coral"),
         ("Esperado 0,99^k", list(zip(ks, [99.00, 98.01, 97.03, 96.06, 95.10])), "navy"),
         ("Cola y 3 intentos por dependencia", list(zip(ks, [98.99, 99.02, 98.99, 99.01, 98.93])), "teal")],
        x_label="Dependencias en la cadena (k)", y_label="Peticiones que terminan bien (%)", y_zero=False,
        x_ticks=[(k, str(k)) for k in ks], y_ticks=[94, 95, 96, 97, 98, 99, 100], point_labels="none",
        annotations=[(5, 95.20, "5 dependencias síncronas: 95,20 % (esperado 95,10 %)", -230, -34),
                     (3, 98.99, "La cola se queda en el 1 % de su propia cola", -10, -28)],
        note="La disponibilidad de una cadena síncrona es el producto de las de sus eslabones, por eso cae con cada dependencia. La cola no la mejora gratis: mueve el 1 % a la propia cola y convierte el resto en retraso. El eje vertical no empieza en cero para separar las curvas. El fallo del 1 %, independiente entre llamadas, es un supuesto del autor.",
        note_kind="gold", foot=SINT)


def se325_reintentos() -> Fig:
    return grouped_bars(
        "Reintentos apilados: llamadas que recibe el servicio por cada petición del usuario",
        "Barras horizontales con las llamadas que recibe el servicio por petición según su estado y la política de reintentos: sano recibe 1, caído con una capa y dos reintentos recibe 3, caído con tres capas de dos reintentos recibe 27 y con un presupuesto del 10 por ciento por capa solo 1,30, aunque con fallo parcial del 50 por ciento el éxito baja de 100 a 64,8 por ciento.",
        ["Sano (0 % de fallo) · 1 capa, 2 reintentos", "50 % de fallo · 1 capa, 2 reintentos", "50 % · 3 capas, 2 reintentos cada una",
         "50 % · 3 capas con presupuesto del 10 %", "Caído · 1 capa, 2 reintentos", "Caído · 3 capas, 2 reintentos cada una",
         "Caído · 3 capas con presupuesto del 10 %"],
        [("Llamadas por petición", [1.00, 1.75, 2.01, 1.30, 3.00, 27.00, 1.30], "coral")],
        unit="Llamadas que recibe el servicio por petición", horizontal=True, label_w=330, decimals=2, ticks=[0, 5, 10, 15, 20, 25, 30],
        note="Cada capa reintenta sin saber que las demás también lo hacen, de modo que el servicio caído recibe 3^3 = 27 veces la carga justo cuando menos puede soportarla. El presupuesto frena la amplificación y deja de ayudar cuando el fallo es parcial: con 50 % de fallo las peticiones que terminan bien bajan de 100 % a 64,8 %. Simulación de 10 000 peticiones; sin latencias.",
        note_kind="coral", foot=SINT)


def se325_caida() -> Fig:
    caps = [1.2, 1.5, 2.0, 4.0]
    return line_chart(
        "Una dependencia caída 600 s con 1 envío por segundo: tiempo que tarda la cola en vaciarse",
        "Línea con los segundos que tarda la cola en vaciarse según la capacidad del consumidor al volver: 2 995 s con 1,2 mensajes por segundo, 1 198 con 1,5, 599 con 2 y 199 con 4, siempre con 600 mensajes acumulados que habrían sido 600 errores síncronos.",
        [("Tiempo hasta vaciar la cola", [(1.2, 2995, "2 995 s (casi 50 min)", "r"), (1.5, 1198, "1 198", "r"), (2.0, 599, "599", "r"), (4.0, 199, "199", "t")], "teal")],
        x_label="Capacidad del consumidor al volver (mensajes por segundo)", y_label="Segundos hasta vaciar la cola",
        x_ticks=[(c, f"{c:g}".replace(".", ",")) for c in caps], y_ticks=[0, 500, 1000, 1500, 2000, 2500, 3000],
        note="La cola convierte 600 errores en 600 mensajes con retraso, y el tiempo de recuperación depende del margen de capacidad: cae como el inverso de la capacidad que sobra sobre la llegada. Con una capacidad igual a la llegada nunca se vacía. Llegada constante y capacidad fija son supuestos del autor.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-374
def se326_contenido() -> Fig:
    return grouped_bars(
        "Notificación mínima (78 B) frente a estado completo en el evento (246 B), 1 000 eventos",
        "Barras horizontales por consumidor: con la notificación de 78 bytes cuatro de cinco consumidores llaman de vuelta 1 000 veces y la auditoría y el calificador leen un valor del instante equivocado 299 veces; con el estado dentro del evento de 246 bytes no hay llamadas, pero las notificaciones y la analítica quedan desactualizadas 299 veces; la facturación solo necesita el identificador.",
        ["Notificaciones (estado actual)", "Auditoría (estado del instante)", "Analítica (curso y estado actuales)", "Calificador (archivo del instante)", "Facturación (solo el identificador)"],
        [("Llamadas de vuelta (notificación)", [1000, 1000, 1000, 1000, 0], "teal"),
         ("Instante equivocado (notificación)", [0, 299, 0, 299, 0], "coral"),
         ("Desactualizadas (estado en el evento)", [299, 0, 299, 0, 0], "gold")],
        unit="De 1 000 eventos", horizontal=True, label_w=260, ticks=[0, 250, 500, 750, 1000],
        note="Ninguna forma de evento es correcta en general: la notificación obliga a un viaje de vuelta y lee el estado de ahora; el estado en el evento lee el del instante y puede estar viejo. El 30 % de cambios antes de leer es un supuesto del autor.",
        note_kind="gold", foot=SINT)


def se326_destinatarios() -> Fig:
    return grouped_bars(
        "El mismo mensaje como comando y como evento según los manejadores registrados (1 000 mensajes)",
        "Barras agrupadas según haya 0, 1 o 3 manejadores: con ninguno un comando exigido se rechaza 1 000 veces y un evento se pierde 1 000 veces sin aviso; con uno todo funciona; con tres un comando exigido se rechaza por ambiguo, un comando difundido se ejecuta 3 000 veces y un evento se entrega 3 000 veces como se espera.",
        ["0 manejadores", "1 manejador", "3 manejadores"],
        [("Comando exigido: rechazos", [1000, 0, 1000], "coral"),
         ("Comando difundido: ejecuciones", [0, 1000, 3000], "gold"),
         ("Evento: entregas", [0, 1000, 3000], "teal"),
         ("Evento: perdidos sin aviso", [1000, 0, 0], "navy")],
        unit="De 1 000 mensajes", ticks=[0, 1000, 2000, 3000],
        note="Con cero manejadores el comando falla a gritos y el evento falla en silencio; con tres, difundir un comando lo ejecuta tres veces, que no es lo que significa una orden, y entregar un evento tres veces es justo su contrato. Un bus de diccionario sin fallos ni reintentos: solo muestra la diferencia de contrato.",
        note_kind="gold", foot=SINT)


def se326_sobre() -> Fig:
    return dumbbell(
        "Qué se pierde al quitar un campo del sobre del mensaje (2 300 mensajes, 80 estudiantes)",
        "Mancuernas con los resultados erróneos con el campo en el sobre y con la heurística que lo sustituye: deduplicar por contenido descarta 635 mensajes distintos frente a 0 con identificador; ordenar por marca de tiempo deja 992 de 2 100 eventos fuera de lugar frente a 0 con secuencia; seguir una operación por estudiante y ventana propone 254 pares y solo 128 son correctos, es decir 126 pares falsos frente a 0 con correlación.",
        [("Deduplicar: distintos descartados", 0, 635), ("Ordenar: eventos fuera de lugar", 0, 992),
         ("Seguir: pares propuestos que no son correctos", 0, 126)],
        unit="Resultados erróneos", names=("Con el campo en el sobre", "Sin el campo (heurística)"), label_w=320,
        delta=lambda a, b: f"{b:g} errores",
        note="El sobre es el contrato que no depende del contenido: id, tipo, origen, secuencia y correlación permiten deduplicar, enrutar, ordenar y seguir mensajes sin leer el cuerpo. Las heurísticas parecen funcionar y fallan justo cuando hay reenvíos legítimos, ráfagas o concurrencia. Los 126 pares falsos son 254 propuestos menos 128 correctos; la tabla da también los 2 302 pares correctos con correlación.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-375
def se327_estructuras() -> Fig:
    title = "Cola de trabajo, tópico con suscripciones y log con desplazamientos frente a un mismo flujo de 3 000 mensajes"
    f = Fig(940, 476, title,
            "Diagrama de tres columnas que muestra qué ocurre con un mensaje después de entregarse: en la cola de trabajo se borra al confirmarse, dos consumidores se reparten 1 500 y 1 500, el suscriptor tardío compite por lo que quede y no se puede reprocesar nada; en el tópico cada suscripción recibe los 3 000, el suscriptor tardío recibe 2 000 y no se puede reprocesar; en el log se conservan los 3 000, un grupo se reparte y otro lee todos, el suscriptor tardío lee desde el desplazamiento 0 y se reprocesan 500.")
    f.text(14, 27, title, 15, "start", 700)
    cols = [
        ("Cola de trabajo", "gold", "El mensaje se borra al confirmarse", [("Consumidor A", "1 500"), ("Consumidor B", "1 500")],
         "Suscriptor tardío: compite por lo que quede desde ahora", "Reprocesar los últimos 500: 0, ya se borraron", "coral"),
        ("Tópico con suscripciones", "teal", "Cada suscripción vigente recibe una copia", [("Suscripción A", "3 000"), ("Suscripción B", "3 000")],
         "Suscriptor tardío: recibe 2 000, no ve los 1 000 anteriores", "Reprocesar los últimos 500: 0, ya se entregaron", "coral"),
        ("Log con desplazamientos", "grey", "El mensaje se conserva mientras dure la retención", [("Grupo 1 (se reparte)", "3 000"), ("Grupo 2 (lee todo)", "3 000")],
         "Suscriptor tardío: lee 3 000 desde el desplazamiento 0", "Reprocesar los últimos 500: 500, se reposiciona el desplazamiento", "teal"),
    ]
    for i, (name, kind, rule, consumers, late, replay, replay_kind) in enumerate(cols):
        x = 10 + i * 312
        f.box(x, 46, 296, 36, name, "navy", 15, bold=True)
        f.box(x, 98, 296, 34, "3 000 mensajes entran", "plain", 14)
        f.arrow([(x + 148, 132), (x + 148, 160)])
        f.box(x, 160, 296, 54, rule, kind, 14, bold=True)
        for j, (who, count) in enumerate(consumers):
            bx = x + j * 152
            f.arrow([(x + 148, 214), (bx + 72, 252)])
            f.box(bx, 252, 144, 62, f"{who}\n{count} mensajes", "plain", 13)
        f.box(x, 336, 296, 60, late, "plain", 13, dashed=True)
        f.box(x, 406, 296, 60, replay, replay_kind, 13)
    return f


def se327_particiones() -> Fig:
    return grouped_bars(
        "Particiones, consumidores y una clave popular (20 000 eventos, 800 estudiantes, popularidad Zipf)",
        "Barras agrupadas con los eventos del consumidor más cargado: con cuatro consumidores recibe 7 129 de 20 000 con 4, 8 o 16 particiones; con ocho consumidores recibe 7 129 con cuatro particiones y 5 174 con ocho o dieciséis; la clave más popular suma 3 643 eventos y vive en una sola partición, y con cuatro particiones y ocho consumidores cuatro consumidores quedan sin trabajo.",
        ["4 consumidores", "8 consumidores"],
        [("4 particiones", [7129, 7129], "coral"), ("8 particiones", [7129, 5174], "gold"), ("16 particiones", [7129, 5174], "teal")],
        unit="Eventos del consumidor más cargado (de 20 000)", ticks=[0, 2000, 4000, 6000, 8000],
        note="Con cuatro particiones y ocho consumidores cuatro consumidores quedan sin trabajo, y con ocho el máximo solo baja de 7 129 a 5 174 porque los 3 643 eventos de la clave más popular siguen en una sola partición. Con clave, todos los eventos de un estudiante van a una partición y se procesan en orden (0 de 669 estudiantes fuera de orden); con reparto circular 106 de 669 quedaron fuera de orden. Exponente de popularidad 1,1: supuesto del autor.",
        note_kind="coral", foot=SINT)


def se327_retencion() -> Fig:
    return grouped_bars(
        "Reconstruir el estado desde el log: 100 000 eventos sobre 2 000 claves con 5 % de borrados",
        "Barras horizontales en escala logarítmica con las entradas que guarda cada estrategia y las claves vivas que reconstruye: el log completo guarda 100 000 y reconstruye 1 891; conservar los últimos 20 000 eventos reconstruye 1 692 y pierde 199 claves; la compactación guarda 1 999 entradas y reconstruye las mismas 1 891.",
        ["Log completo", "Retención de los últimos 20 000 eventos", "Compactación (último valor por clave)"],
        [("Entradas guardadas", [100000, 20000, 1999], "navy"), ("Claves vivas reconstruidas", [1891, 1692, 1891], "teal")],
        unit="Cantidad", horizontal=True, log=True, label_w=270, ticks=[100, 1000, 10000, 100000],
        note="La retención por tiempo o tamaño sirve para eventos; para reconstruir un estado hace falta compactar: las claves vivas reales son 1 891 y la ventana pierde 199 que no cambiaron en ella, sin devolver nunca un valor equivocado. Datos sintéticos con popularidad Zipf de exponente 1,0.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-376
def se328_semanticas() -> Fig:
    return grouped_bars(
        "Tres semánticas con 2 % de mensajes perdidos, 5 % de acuses perdidos y 2 % de caídas (20 000 mensajes)",
        "Barras agrupadas con los mensajes perdidos y los efectos duplicados de cada semántica: a lo sumo una vez pierde 743 y no duplica; al menos una vez no pierde y duplica 1 476; al menos una vez con consumidor idempotente deja 0 y 0 y exactamente 20 000 efectos.",
        ["A lo sumo una vez", "Al menos una vez", "Al menos una vez + consumidor idempotente"],
        [("Mensajes perdidos", [743, 0, 0], "coral"), ("Efectos duplicados", [0, 1476, 0], "gold")],
        unit="De 20 000 mensajes", ticks=[0, 500, 1000, 1500],
        note="No existe una entrega exactamente una vez entre procesos que fallan: se elige perder o duplicar, y el efecto exactamente una vez se obtiene al hacer idempotente al consumidor (efectos totales: 19 257, 21 476 y 20 000). La tabla de vistos real es SQLite; la red, los acuses y las caídas son un modelo del autor.",
        note_kind="gold", foot=SINT)


def se328_orden() -> Fig:
    xs = [0, 3, 10, 50]
    return line_chart(
        "Mensajes desordenados: entradas con valor final equivocado de 500 (10 versiones cada una)",
        "Líneas con las entradas de 500 que terminan con un valor equivocado según cuántas posiciones puede retrasarse un mensaje: aplicar siempre el último que llega deja 0, 135, 308 y 416 equivocadas con retrasos de 0, 3, 10 y 50 posiciones; aplicar solo si la versión es mayor deja 0 en todos los casos.",
        [("Aplicar en orden de llegada", list(zip(xs, [0, 135, 308, 416])), "coral"),
         ("Aplicar solo si la versión es mayor", list(zip(xs, [0, 0, 0, 0])), "teal")],
        x_label="Desplazamiento máximo de un mensaje (posiciones)", y_label="Entradas con valor final equivocado (de 500)",
        x_ticks=[(x, str(x)) for x in [0, 10, 20, 30, 40, 50]], y_ticks=[0, 100, 200, 300, 400, 500],
        note="El orden de llegada no es el orden de los hechos; un número de versión por entidad convierte la lectura desordenada en un problema de comparar enteros. La guarda no recupera los valores intermedios: si importan los estados intermedios, hace falta el historial.",
        note_kind="teal", foot=SINT)


def se328_ventana() -> Fig:
    pts = [(50, 73414, "10 s", "r"), (300, 32388, "60 s", "r"), (1500, 1521, "5 min", "t"), (18000, 921, "1 h", "t"), (432000, 0, "24 h", "t")]
    return line_chart(
        "Ventana de deduplicación: duplicados que pasan de 86 590 reentregas en un día (5 mensajes por segundo)",
        "Línea con los duplicados que pasan según los identificadores que guarda cada ventana, en escala logarítmica horizontal: 10 segundos guarda 50 y deja pasar 73 414; 60 segundos, 300 y 32 388; 5 minutos, 1 500 y 1 521; una hora, 18 000 y 921 por una cola larga; 24 horas, 432 000 y ninguno.",
        [("Ventana de deduplicación", pts, "coral")],
        x_label="Identificadores guardados", y_label="Duplicados que pasan (de 86 590)", log_x=True,
        x_ticks=[(10, "10"), (100, "100"), (1000, "1 000"), (10000, "10 000"), (100000, "100 000"), (1000000, "1 000 000")],
        y_ticks=[0, 20000, 40000, 60000, 80000], point_labels="none",
        note="El tamaño de la ventana es una apuesta sobre cuánto tarda en volver una reentrega: cada punto compra menos duplicados con más memoria. Las reentregas siguen una distribución con cola larga (1 % entre 1 y 6 horas), por eso una ventana que cubre casi todo deja pasar cientos de duplicados. Retardos exponenciales con cola: supuesto del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-377
def se329_doble() -> Fig:
    title = "Escribir en la base y publicar un evento con 3 % de caídas entre los dos pasos (1 000 entregas)"
    f = Fig(940, 436, title,
            "Diagrama de tres estrategias con una caída entre sus dos pasos: confirmar la base y luego publicar deja 1 000 filas y 966 eventos, 34 entregas sin evento; publicar y luego confirmar deja 966 filas y 1 000 eventos, 34 eventos de entregas que no existen; escribir la fila y su evento en la misma transacción del outbox deja 966 y 966, sin ninguna diferencia.")
    f.text(14, 27, title, 15, "start", 700)
    rows = [
        ("Confirmar la base y luego publicar", "1. Confirmar la base", "2. Publicar el evento",
         "1 000 filas, 966 eventos\n34 entregas sin evento", "coral"),
        ("Publicar y luego confirmar la base", "1. Publicar el evento", "2. Confirmar la base",
         "966 filas, 1 000 eventos\n34 eventos de entregas que no existen", "coral"),
        ("Outbox: fila y evento en una transacción", "1. Fila y evento juntos", "2. El relevo publica después",
         "966 filas, 966 eventos\nninguna diferencia: la caída anula ambos", "teal"),
    ]
    for i, (name, step1, step2, result, kind) in enumerate(rows):
        y = 46 + i * 128
        f.group(10, y, 920, 116, name, "grey")
        f.box(26, y + 36, 190, 56, step1, "plain", 14)
        f.arrow([(216, y + 64), (276, y + 64)])
        f.dot(288, y + 64, "!", "coral")
        f.arrow([(300, y + 64), (360, y + 64)])
        f.box(360, y + 36, 200, 56, step2, "plain", 14)
        f.arrow([(560, y + 64), (606, y + 64)])
        f.box(606, y + 32, 310, 64, result, kind, 13, bold=True)
    return f


def se329_relevo() -> Fig:
    title = "Relevo del outbox con 3 % de caídas entre publicar y marcar (1 000 entregas)"
    f = Fig(940, 400, title,
            "Diagrama con dos relevos: publicar y luego marcar como enviado deja 1 029 mensajes en el corredor, 29 duplicados y ninguno perdido, y con la bandeja de entrada 1 000 efectos; marcar y luego publicar deja 971 mensajes, ninguno duplicado y 29 perdidos sin remedio, 971 efectos. La caída entre los dos pasos produce el duplicado o la pérdida.")
    f.text(14, 27, title, 15, "start", 700)
    rows = [
        ("Relevo A: publicar y luego marcar", "1. Publicar el mensaje", "2. Marcar como enviado",
         "Caída entre los dos pasos: la fila sigue pendiente y el relevo publica otra vez",
         "Corredor: 1 029 mensajes\n29 duplicados, 0 perdidos", "Con inbox: 1 000 efectos", "gold", "teal"),
        ("Relevo B: marcar y luego publicar", "1. Marcar como enviado", "2. Publicar el mensaje",
         "Caída entre los dos pasos: la fila ya está marcada y el mensaje nunca sale",
         "Corredor: 971 mensajes\n0 duplicados, 29 perdidos", "Con inbox: 971 efectos, 29 sin remedio", "gold", "coral"),
    ]
    for i, (name, step1, step2, crash, broker, effects, kind, ekind) in enumerate(rows):
        y = 48 + i * 170
        f.group(10, y, 920, 156, name, "grey")
        f.box(26, y + 40, 170, 52, step1, "plain", 14)
        f.arrow([(196, y + 66), (248, y + 66)])
        f.dot(260, y + 66, "!", "coral")
        f.arrow([(272, y + 66), (324, y + 66)])
        f.box(324, y + 40, 170, 52, step2, "plain", 14)
        f.text(260, y + 124, crash, 13, "middle", 400, "#5c1f14")
        f.arrow([(494, y + 66), (542, y + 66)])
        f.box(542, y + 30, 190, 78, broker, ekind, 13)
        f.arrow([(732, y + 66), (754, y + 66)])
        f.box(754, y + 30, 166, 78, effects, ekind, 13, bold=True)
    return f


def se329_saga() -> Fig:
    return stacked_bars(
        "Saga de inscripción con 8 % de fallo por paso y compensación en tres intentos (10 000 sagas)",
        "Barras apiladas horizontales con el destino de 10 000 sagas según el orden de los pasos: con el paso irreversible de enviar la bienvenida al final terminan 7 136, se revierten limpiamente 2 860, ninguna deja residuo y 4 quedan atascadas; con la bienvenida antes de dar acceso terminan 7 144, se revierten limpiamente 2 249, 603 dejan un correo irreversible y 4 quedan atascadas.",
        ["Reservar, cobrar, dar acceso, enviar bienvenida", "Reservar, cobrar, enviar bienvenida, dar acceso"],
        [("Completas", [7136, 7144], "teal"), ("Revertidas limpias", [2860, 2249], "navy"),
         ("Residuo irreversible", [0, 603], "coral"), ("Atascadas", [4, 4], "gold")],
        unit="Sagas de 10 000", horizontal=True, label_w=300,
        note="Poner los pasos que no se pueden compensar al final es una decisión de diseño, no un detalle: mueve 603 sagas del residuo irreversible a la reversión limpia. Las atascadas (cuatro de 10 000) son las que fallan tres veces al compensar y necesitan a una persona. Probabilidades fijas del autor.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-378
def se330_cambios() -> Fig:
    return grouped_bars(
        "Réplica tras 2 000 operaciones sobre 10 000 filas (origen: 10 195 filas)",
        "Barras horizontales con las filas faltantes, desactualizadas y que debían borrarse según el método de detección: sondear con mayor estricto deja 11, 50 y 194; con mayor o igual 0, 0 y 194; un registro de cambios con disparadores deja 0, 0 y 0.",
        ["Sondeo por marca con mayor estricto (>)", "Sondeo con mayor o igual (>=)", "Registro de cambios con disparadores"],
        [("Filas faltantes", [11, 0, 0], "coral"), ("Filas desactualizadas", [50, 0, 0], "gold"), ("Filas que debían borrarse", [194, 194, 0], "navy")],
        unit="Filas de la réplica que difieren del origen", horizontal=True, label_w=300, ticks=[0, 50, 100, 150, 200],
        note="Sondear por marca no puede ver un borrado: la fila ya no está para devolver su marca. El mayor estricto además pierde las filas modificadas en el mismo segundo que la marca. La resolución de un segundo con 5 operaciones por segundo y el sondeo cada 47 operaciones son supuestos del autor.",
        note_kind="coral", foot=SINT)


def se330_costo() -> Fig:
    xs = [0.1, 1, 10, 50]
    return line_chart(
        "Copia completa frente a incremental: filas leídas por ciclo sobre 100 000 filas",
        "Líneas en escala logarítmica con las filas leídas por ciclo según el porcentaje de filas que cambian: la copia completa lee siempre 100 000; la incremental lee 100, 1 000, 10 000 y 50 000 con 0,1, 1, 10 y 50 por ciento de cambios, un ahorro de 99,9, 99, 90 y 50 por ciento.",
        [("Copia completa", list(zip(xs, [100000] * 4)), "navy"), ("Incremental", list(zip(xs, [100, 1000, 10000, 50000])), "teal")],
        x_label="Filas que cambian por ciclo (%)", y_label="Filas leídas por ciclo", log_x=True, log_y=True,
        x_ticks=[(0.1, "0,1"), (1, "1"), (10, "10"), (50, "50")], y_ticks=[100, 1000, 10000, 100000],
        point_labels="all",
        note="El incremental ahorra lectura (99,9, 99, 90 y 50 % menos filas leídas) y cobra escritura: 10 000 actualizaciones cuestan 210 006 pasos sin disparador y 560 001 con él en Windows (SQLite 3.45.3); en Ubuntu 220 006 y 570 001 (2,7 veces). Cuenta de filas y pasos de la máquina virtual, no tiempo de reloj.",
        note_kind="gold", foot=SINT)


def se330_orden() -> Fig:
    return grouped_bars(
        "Aplicar eventos de cambio a una réplica: claves erróneas de 50 tras 5 000 eventos",
        "Barras agrupadas con las claves erróneas de 50 según cómo lleguen los eventos: aplicar sin versión deja 0 en orden y sin repetir, 4 reordenados hasta 20 posiciones, 3 con 10 por ciento de duplicados tardíos y 6 con ambos; aplicar solo si la versión es mayor deja 0 en todos los casos.",
        ["En orden y sin repetir", "Reordenado hasta 20 posiciones", "10 % de duplicados tardíos", "Ambos"],
        [("Aplicar sin versión", [0, 4, 3, 6], "coral"), ("Aplicar solo si la versión es mayor", [0, 0, 0, 0], "teal")],
        unit="Claves erróneas (de 50)", ticks=[0, 2, 4, 6, 8],
        note="Con 50 claves y 5 000 eventos cada clave cambia unas 100 veces, así que unos pocos errores significan que casi cualquier réplica real los tendría. Un borrado reordenado con un alta anterior revive la fila: la versión del borrado debe conservarse como lápida.",
        note_kind="teal", foot=SINT)


FIGURES = {
    "se-373-disponibilidad-en-cadena.svg": se325_cadena,
    "se-373-reintentos-apilados.svg": se325_reintentos,
    "se-373-cola-tras-una-caida.svg": se325_caida,
    "se-374-lo-que-lleva-el-mensaje.svg": se326_contenido,
    "se-374-comando-o-evento.svg": se326_destinatarios,
    "se-374-campos-del-sobre.svg": se326_sobre,
    "se-375-cola-topico-y-log.svg": se327_estructuras,
    "se-375-particiones-y-carga.svg": se327_particiones,
    "se-375-retencion-y-compactacion.svg": se327_retencion,
    "se-376-perdida-y-duplicados.svg": se328_semanticas,
    "se-376-orden-de-llegada.svg": se328_orden,
    "se-376-ventana-de-deduplicacion.svg": se328_ventana,
    "se-377-doble-escritura.svg": se329_doble,
    "se-377-relevo-del-outbox.svg": se329_relevo,
    "se-377-orden-de-pasos-de-una-saga.svg": se329_saga,
    "se-378-detectar-cambios.svg": se330_cambios,
    "se-378-costo-de-sincronizar.svg": se330_costo,
    "se-378-orden-y-repeticion.svg": se330_orden,
}
