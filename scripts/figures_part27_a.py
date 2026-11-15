"""Figures for SE-325 to SE-330 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab

SINT = "Datos sintéticos con semilla fija; CPython 3.12 en Windows y Ubuntu (WSL2); cifras idénticas salvo donde se indica."


# ---------------------------------------------------------------- SE-325
def se325_cadena() -> Fig:
    rows = [
        ["1", "99,02 %", "99,00 %", "98,99 %"],
        ["2", "98,04 %", "98,01 %", "99,02 %"],
        ["3", "96,99 %", "97,03 %", "98,99 %"],
        ["4", "96,10 %", "96,06 %", "99,01 %"],
        ["5", "95,20 %", "95,10 %", "98,93 %"],
    ]
    return tab("Dependencias encadenadas: peticiones que terminan bien con un fallo del 1 % por llamada",
               "Tabla: con una probabilidad de fallo del 1 por ciento por llamada, una cadena síncrona de una a cinco dependencias completa el 99,02, 98,04, 96,99, 96,10 y 95,20 por ciento de 200 000 peticiones, muy cerca de 0,99 elevado al número de dependencias; aceptar en una cola y completar con tres intentos por dependencia da entre 98,9 y 99,0 por ciento, limitado por el 1 por ciento de la propia cola.",
               ["Dependencias en la cadena", "Síncrona medida", "Esperado 0,99^k", "Cola y 3 intentos por dependencia"], rows, [230, 200, 200, 300], row_h=44, size=13,
               note="La disponibilidad de una cadena síncrona es el producto de las de sus eslabones, por eso cae con cada dependencia. La cola no la mejora gratis: mueve el 1 % a la propia cola y convierte el resto en retraso. El fallo del 1 %, independiente entre llamadas, es un supuesto del autor.",
               note_kind="gold", foot=SINT)


def se325_reintentos() -> Fig:
    rows = [
        ["0 % (sano)", "1 capa, 2 reintentos", "1,00", "100 %"],
        ["50 %", "1 capa, 2 reintentos", "1,75", "87,4 %"],
        ["50 %", "3 capas, 2 reintentos cada una", "2,01", "100 %"],
        ["50 %", "3 capas con presupuesto del 10 %", "1,30", "64,8 %"],
        ["100 % (caído)", "1 capa, 2 reintentos", "3,00", "0 %"],
        ["100 % (caído)", "3 capas, 2 reintentos cada una", "27,00", "0 %"],
        ["100 % (caído)", "3 capas con presupuesto del 10 %", "1,30", "0 %"],
    ]
    return tab("Reintentos apilados: llamadas que recibe el servicio por cada petición del usuario",
               "Tabla: si el servicio está caído, un reintento en una capa multiplica por tres las llamadas y tres capas con dos reintentos cada una las multiplican por veintisiete; con un presupuesto de reintentos del diez por ciento por capa el servicio recibe 1,3 llamadas por petición, a costa de menos éxitos cuando falla la mitad de las llamadas.",
               ["Fallo del servicio", "Política de reintentos", "Llamadas por petición", "Peticiones que terminan bien"], rows, [160, 330, 200, 240], row_h=44, size=13,
               note="Cada capa reintenta sin saber que las demás también lo hacen, de modo que el servicio caído recibe 3^3 = 27 veces la carga justo cuando menos puede soportarla. El presupuesto frena la amplificación y deja de ayudar cuando el fallo es parcial (64,8 % frente a 100 %). Simulación de 10 000 peticiones; sin latencias.",
               note_kind="coral", foot=SINT)


def se325_caida() -> Fig:
    rows = [
        ["1,2 por segundo", "600", "600", "2 995 s"],
        ["1,5 por segundo", "600", "600", "1 198 s"],
        ["2,0 por segundo", "600", "600", "599 s"],
        ["4,0 por segundo", "600", "600", "199 s"],
    ]
    return tab("Una dependencia caída 600 s con 1 envío por segundo: errores síncronos y cola asíncrona",
               "Tabla: si el consumidor vuelve con una capacidad de 1,2, 1,5, 2 y 4 mensajes por segundo, la versión síncrona habría devuelto 600 errores y la cola acumula 600 mensajes que tardan 2 995, 1 198, 599 y 199 segundos en vaciarse mientras sigue llegando un envío por segundo.",
               ["Capacidad al volver", "Errores si fuese síncrona", "Mensajes en cola al volver", "Tiempo hasta vaciar la cola"], rows, [220, 240, 240, 240], row_h=44, size=13,
               note="La cola convierte 600 errores en 600 mensajes con retraso, y el tiempo de recuperación depende del margen de capacidad: con 1,2 por segundo la cola tarda casi 50 minutos. Con una capacidad igual a la llegada nunca se vacía. Llegada constante y capacidad fija son supuestos del autor.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-326
def se326_contenido() -> Fig:
    rows = [
        ["Notificaciones (quieren el estado actual)", "1 000", "0", "299"],
        ["Auditoría (quiere el estado del instante)", "1 000", "299", "0"],
        ["Analítica (quiere curso y estado actuales)", "1 000", "0", "299"],
        ["Calificador (quiere el archivo del instante)", "1 000", "299", "0"],
        ["Facturación (solo necesita el identificador)", "0", "0", "0"],
    ]
    return tab("Notificación mínima (78 B) frente a estado completo en el evento (246 B), 1 000 eventos",
               "Tabla: con una notificación de 78 bytes cuatro de cinco consumidores deben llamar de vuelta 1 000 veces; si el 30 por ciento de las entidades cambia antes de leerse, la auditoría y el calificador leen un valor equivocado 299 veces; con el estado dentro del evento de 246 bytes no hay llamadas pero las notificaciones y la analítica quedan desactualizadas 299 veces.",
               ["Consumidor", "Llamadas de vuelta (notificación)", "Instante equivocado (notificación)", "Desactualizadas (estado en el evento)"], rows, [330, 190, 210, 210], row_h=52, size=13,
               note="Ninguna forma de evento es correcta en general: la notificación obliga a un viaje de vuelta y lee el estado de ahora; el estado en el evento lee el del instante y puede estar viejo. El 30 % de cambios antes de leer es un supuesto del autor.",
               note_kind="gold", foot=SINT)


def se326_destinatarios() -> Fig:
    rows = [
        ["0", "1 000 rechazos", "0", "0", "1 000 perdidos sin aviso"],
        ["1", "0", "1 000", "1 000", "0"],
        ["3", "1 000 rechazos", "3 000", "3 000", "0"],
    ]
    return tab("El mismo mensaje como comando y como evento según los manejadores registrados (1 000 mensajes)",
               "Tabla: con cero manejadores un comando exigido se rechaza 1 000 veces y un evento se pierde 1 000 veces sin que nadie se entere; con un manejador ambos funcionan; con tres manejadores un comando exigido se rechaza por ambiguo, un comando difundido se ejecuta 3 000 veces y un evento se entrega 3 000 veces como se espera.",
               ["Manejadores", "Comando exigido: rechazos", "Comando difundido: ejecuciones", "Evento: entregas", "Evento: pérdidas"], rows, [140, 190, 210, 150, 220], row_h=48, size=13,
               note="Un comando espera exactamente un destinatario y por eso falla en voz alta; un evento acepta cero o muchos y por eso puede perderse sin ruido. Tratar un comando como evento duplica el trabajo; tratar un evento como comando acopla al emisor con sus oyentes. Bus de memoria del autor.",
               note_kind="coral", foot=SINT)


def se326_sobre() -> Fig:
    rows = [
        ["Quitar duplicados exactos", "Con id: 200 quitados, 0 distintos perdidos", "Por contenido: 835 quitados, 635 distintos perdidos"],
        ["Ordenar los eventos de un estudiante", "Con secuencia por origen: 0 fuera de lugar", "Por marca de tiempo: 992 de 2 100 fuera de lugar"],
        ["Seguir una operación entre mensajes", "Con correlación: 2 302 pares correctos", "Por estudiante y ventana: 254 pares, 128 correctos"],
    ]
    return tab("Qué se pierde al quitar un campo del sobre del mensaje (2 300 mensajes, 80 estudiantes)",
               "Tabla: sin identificador, deduplicar por contenido quita 835 mensajes cuando los duplicados son 200 y descarta 635 mensajes distintos; sin número de secuencia, ordenar por marca de tiempo deja 992 de 2 100 mensajes fuera de lugar; sin correlación, la reconstrucción por estudiante y ventana propone 254 pares de los cuales 128 son correctos.",
               ["Capacidad", "Con el campo en el sobre", "Sin el campo (heurística)"], rows, [260, 330, 330], row_h=56, size=13,
               note="El sobre es el contrato que no depende del contenido: id, tipo, origen, secuencia y correlación permiten deduplicar, enrutar, ordenar y seguir mensajes sin leer el cuerpo. Las heurísticas parecen funcionar y fallan justo cuando hay reenvíos legítimos, ráfagas o concurrencia.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-327
def se327_estructuras() -> Fig:
    rows = [
        ["Dos consumidores del mismo trabajo (3 000 mensajes)", "1 500 y 1 500: cada mensaje a uno solo", "Cada suscripción recibe los 3 000", "Un grupo se reparte los 3 000; otro grupo lee todos"],
        ["Un suscriptor nuevo llega tras 1 000 mensajes", "Compite por lo que quede desde ahora", "Recibe 2 000: no ve los 1 000 anteriores", "Lee 3 000 desde el desplazamiento 0"],
        ["Reprocesar los últimos 500 tras corregir un defecto", "0: ya se borraron al confirmarse", "0: ya se entregaron", "500: se reposiciona el desplazamiento"],
    ]
    return tab("Cola de trabajo, tópico con suscripciones y log con desplazamientos frente a las mismas tres preguntas",
               "Tabla: en una cola de trabajo dos consumidores se reparten 1 500 y 1 500 de 3 000 mensajes y no se puede reprocesar nada; un tópico entrega todo a cada suscripción pero el suscriptor tardío solo ve 2 000; un log conserva los 3 000 y permite releer los últimos 500 reposicionando el desplazamiento.",
               ["Pregunta", "Cola de trabajo", "Tópico con suscripciones", "Log con desplazamientos"], rows, [250, 230, 220, 230], row_h=66, size=13,
               note="Lo que distingue a las tres estructuras es qué ocurre con un mensaje después de entregarse: la cola lo borra, el tópico lo entrega a cada suscripción vigente y el log lo conserva mientras dure la retención. Implementaciones mínimas en memoria; ningún corredor real.",
               note_kind="gold", foot=SINT)


def se327_particiones() -> Fig:
    rows = [
        ["4", "4", "7 129", "1,43", "0"],
        ["4", "8", "7 129", "2,85", "4"],
        ["8", "4", "7 129", "1,43", "0"],
        ["8", "8", "5 174", "2,07", "0"],
        ["16", "4", "7 129", "1,43", "0"],
        ["16", "8", "5 174", "2,07", "0"],
    ]
    return tab("Particiones, consumidores y una clave popular (20 000 eventos, 800 estudiantes, popularidad Zipf)",
               "Tabla: con cuatro particiones y cuatro consumidores el más cargado recibe 7 129 de 20 000 eventos, 1,43 veces la media; con ocho consumidores y cuatro particiones cuatro consumidores quedan sin trabajo; con ocho o dieciséis particiones y ocho consumidores el máximo baja a 5 174, y los 3 643 eventos de la clave más popular no se pueden repartir porque viven en una sola partición.",
               ["Particiones", "Consumidores", "Eventos del más cargado", "Máximo / media", "Consumidores sin trabajo"], rows, [140, 160, 230, 170, 220], row_h=44, size=13,
               note="Con clave, todos los eventos de un estudiante van a una partición y se procesan en orden (0 de 669 estudiantes fuera de orden); con reparto circular 106 de 669 quedaron fuera de orden. La clave más popular suma 3 643 eventos y ninguna cantidad de particiones la reparte. Exponente de popularidad 1,1: supuesto del autor.",
               note_kind="coral", foot=SINT)


def se327_retencion() -> Fig:
    rows = [
        ["Log completo", "100 000", "1 891", "0", "0"],
        ["Retención de los últimos 20 000 eventos", "20 000", "1 692", "199", "0"],
        ["Compactación (último valor por clave)", "1 999", "1 891", "0", "0"],
    ]
    return tab("Reconstruir el estado desde el log: 100 000 eventos sobre 2 000 claves con 5 % de borrados",
               "Tabla: el log completo guarda 100 000 entradas y reconstruye las 1 891 claves vivas; conservar solo los últimos 20 000 eventos reconstruye 1 692 y pierde 199 claves que no cambiaron en la ventana; la compactación guarda 1 999 entradas y reconstruye exactamente las mismas 1 891 claves.",
               ["Estrategia de retención", "Entradas guardadas", "Claves vivas reconstruidas", "Claves que faltan", "Valores incorrectos"], rows, [320, 150, 180, 150, 140], row_h=48, size=13,
               note="La retención por tiempo o tamaño sirve para eventos; para reconstruir un estado hace falta compactar. Una ventana nunca devuelve un valor equivocado pero oculta las claves que no cambiaron, que son las más fáciles de olvidar. Datos sintéticos con popularidad Zipf de exponente 1,0.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-328
def se328_semanticas() -> Fig:
    rows = [
        ["A lo sumo una vez", "743", "0", "19 257"],
        ["Al menos una vez", "0", "1 476", "21 476"],
        ["Al menos una vez + consumidor idempotente", "0", "0", "20 000"],
    ]
    return tab("Tres semánticas con 2 % de mensajes perdidos, 5 % de acuses perdidos y 2 % de caídas (20 000 mensajes)",
               "Tabla: acusar antes de procesar y no reintentar pierde 743 de 20 000 mensajes; acusar después y reintentar no pierde ninguno pero produce 1 476 efectos duplicados; añadir un registro de mensajes vistos en la misma transacción del efecto deja exactamente 20 000 efectos.",
               ["Semántica", "Mensajes perdidos", "Efectos duplicados", "Efectos totales"], rows, [400, 170, 180, 170], row_h=48, size=13,
               note="No existe una entrega exactamente una vez entre procesos que fallan: se elige perder o duplicar, y el efecto exactamente una vez se obtiene al hacer idempotente al consumidor. La tabla de vistos real es SQLite; la red, los acuses y las caídas son un modelo del autor.",
               note_kind="gold", foot=SINT)


def se328_orden() -> Fig:
    rows = [
        ["0 (en orden)", "0", "0"],
        ["3", "135", "0"],
        ["10", "308", "0"],
        ["50", "416", "0"],
    ]
    return tab("Mensajes desordenados: entradas con valor final equivocado de 500 (10 versiones cada una)",
               "Tabla: si cada mensaje puede llegar hasta 3, 10 o 50 posiciones tarde, aplicar siempre el último que llega deja equivocadas 135, 308 y 416 de 500 entradas; aplicar un mensaje solo si su versión es mayor que la guardada deja cero equivocadas en todos los casos.",
               ["Desplazamiento máximo (posiciones)", "Aplicar en orden de llegada", "Aplicar solo si la versión es mayor"], rows, [300, 300, 320], row_h=44, size=13,
               note="El orden de llegada no es el orden de los hechos; un número de versión por entidad convierte la lectura desordenada en un problema de comparar enteros. La guarda no recupera los valores intermedios: si importan los estados intermedios, hace falta el historial.",
               note_kind="teal", foot=SINT)


def se328_ventana() -> Fig:
    rows = [
        ["10 s", "73 414", "50"],
        ["60 s", "32 388", "300"],
        ["5 min", "1 521", "1 500"],
        ["1 h", "921", "18 000"],
        ["24 h", "0", "432 000"],
    ]
    return tab("Ventana de deduplicación: duplicados que pasan de 86 590 reentregas en un día (5 mensajes por segundo)",
               "Tabla: una ventana de 10 segundos deja pasar 73 414 de 86 590 reentregas y guarda 50 identificadores; 60 segundos deja pasar 32 388; 5 minutos 1 521; una hora 921 por una cola larga del 1 por ciento hasta seis horas; 24 horas ninguna pero guarda 432 000 identificadores.",
               ["Ventana de deduplicación", "Duplicados que pasan", "Identificadores guardados"], rows, [300, 300, 320], row_h=44, size=13,
               note="El tamaño de la ventana es una apuesta sobre cuánto tarda en volver una reentrega. Las reentregas siguen una distribución con cola larga (1 % entre 1 y 6 horas), por eso una ventana que cubre casi todo deja pasar cientos de duplicados. Retardos exponenciales con cola: supuesto del autor.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-329
def se329_doble() -> Fig:
    rows = [
        ["Confirmar la base y luego publicar", "1 000", "966", "34 entregas sin evento"],
        ["Publicar y luego confirmar la base", "966", "1 000", "34 eventos de entregas que no existen"],
        ["Outbox: fila y evento en una transacción", "966", "966", "Ninguno: la caída anula ambos"],
    ]
    return tab("Escribir en la base y publicar un evento con 3 % de caídas entre los dos pasos (1 000 entregas)",
               "Tabla: confirmar la base y luego publicar deja 34 entregas sin evento; publicar y luego confirmar deja 34 eventos de entregas que no existen; escribir la entrega y su evento en la misma transacción del outbox deja 966 de cada uno sin ninguna diferencia.",
               ["Estrategia", "Filas en la base", "Eventos publicados", "Inconsistencias"], rows, [330, 150, 170, 270], row_h=48, size=13,
               note="No hay orden de dos escrituras en sistemas distintos que sea seguro; el outbox mueve la segunda escritura a la misma transacción de la primera y deja la publicación a un relevo posterior. La caída se inyecta con probabilidad fija; el corredor es una lista en memoria.",
               note_kind="coral", foot=SINT)


def se329_relevo() -> Fig:
    rows = [
        ["Publicar y luego marcar como enviado", "1 029", "29", "0", "1 000"],
        ["Marcar y luego publicar", "971", "0", "29", "971"],
    ]
    return tab("Relevo del outbox con 3 % de caídas entre publicar y marcar (1 000 entregas)",
               "Tabla: publicar y luego marcar produce 1 029 mensajes con 29 duplicados y ninguno perdido, y un consumidor con bandeja de entrada deja exactamente 1 000 efectos; marcar y luego publicar produce 971 mensajes, ninguno duplicado y 29 perdidos, sin que ningún consumidor pueda repararlo.",
               ["Orden del relevo", "Mensajes en el corredor", "Duplicados", "Perdidos", "Efectos con inbox"], rows, [350, 190, 130, 120, 130], row_h=48, size=13,
               note="El relevo debe preferir duplicar a perder: un duplicado se corrige con una clave única en el consumidor (inbox) y un mensaje perdido no deja rastro. El inbox es una tabla SQLite con clave primaria; la caída del relevo es una probabilidad fija del autor.",
               note_kind="gold", foot=SINT)


def se329_saga() -> Fig:
    rows = [
        ["Reservar, cobrar, dar acceso, enviar bienvenida", "7 136", "2 860", "0", "4"],
        ["Reservar, cobrar, enviar bienvenida, dar acceso", "7 144", "2 249", "603", "4"],
    ]
    return tab("Saga de inscripción con 8 % de fallo por paso y compensación en tres intentos (10 000 sagas)",
               "Tabla: con el paso irreversible de enviar la bienvenida al final, 7 136 sagas terminan, 2 860 se revierten limpiamente, ninguna deja residuo y 4 quedan atascadas; con la bienvenida antes del último paso 603 sagas dejan un correo enviado que no se puede deshacer.",
               ["Orden de los pasos", "Completas", "Revertidas limpias", "Residuo irreversible", "Atascadas"], rows, [380, 120, 160, 150, 110], row_h=52, size=13,
               note="Poner los pasos que no se pueden compensar al final es una decisión de diseño, no un detalle: mueve 603 sagas del residuo irreversible a la reversión limpia. Las atascadas (cuatro de 10 000) son las que fallan tres veces al compensar y necesitan a una persona. Probabilidades fijas del autor.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-330
def se330_cambios() -> Fig:
    rows = [
        ["Sondear por marca de modificación con mayor estricto (>)", "11", "50", "194"],
        ["Sondear con mayor o igual (>=)", "0", "0", "194"],
        ["Registro de cambios con disparadores", "0", "0", "0"],
    ]
    return tab("Réplica tras 2 000 operaciones sobre 10 000 filas (origen: 10 195 filas)",
               "Tabla: sondear por una marca de tiempo con mayor estricto deja 11 filas faltantes, 50 desactualizadas y 194 filas borradas que siguen en la réplica; usar mayor o igual corrige las faltantes y las desactualizadas pero no los borrados; un registro de cambios con disparadores deja la réplica idéntica al origen.",
               ["Método de detección", "Filas faltantes", "Filas desactualizadas", "Filas que debían borrarse"], rows, [440, 140, 170, 170], row_h=52, size=13,
               note="Sondear por marca no puede ver un borrado: la fila ya no está para devolver su marca. El mayor estricto además pierde las filas modificadas en el mismo segundo que la marca. La resolución de un segundo con 5 operaciones por segundo y el sondeo cada 47 operaciones son supuestos del autor.",
               note_kind="coral", foot=SINT)


def se330_costo() -> Fig:
    rows = [
        ["0,1 % (100 filas)", "100 000", "100", "99,9 %"],
        ["1 % (1 000 filas)", "100 000", "1 000", "99 %"],
        ["10 % (10 000 filas)", "100 000", "10 000", "90 %"],
        ["50 % (50 000 filas)", "100 000", "50 000", "50 %"],
    ]
    return tab("Copia completa frente a incremental: filas leídas por ciclo sobre 100 000 filas",
               "Tabla: una copia completa lee 100 000 filas en cada ciclo; la incremental lee solo los cambios, de 100 filas con un 0,1 por ciento de cambios a 50 000 con un 50 por ciento, con un ahorro de lectura del 99,9, 99, 90 y 50 por ciento; el disparador que registra los cambios multiplica por 2,7 los pasos de la máquina virtual de SQLite de 10 000 actualizaciones.",
               ["Cambios por ciclo", "Copia completa lee", "Incremental lee", "Ahorro de lectura"], rows, [250, 230, 210, 230], row_h=44, size=13,
               note="El incremental ahorra lectura y cobra escritura: 10 000 actualizaciones cuestan 210 006 pasos sin disparador y 560 001 con él en Windows (SQLite 3.45.3); en Ubuntu 220 006 y 570 001. Cuenta de filas y pasos de la máquina virtual, no tiempo de reloj.",
               note_kind="gold", foot=SINT)


def se330_orden() -> Fig:
    rows = [
        ["En orden y sin repetir", "0", "0"],
        ["Reordenado hasta 20 posiciones", "4", "0"],
        ["10 % de duplicados tardíos", "3", "0"],
        ["Ambos", "6", "0"],
    ]
    return tab("Aplicar eventos de cambio a una réplica: claves erróneas de 50 tras 5 000 eventos",
               "Tabla: aplicar los eventos de cambio tal como llegan deja 0 claves erróneas si llegan en orden, 4 si se reordenan hasta 20 posiciones, 3 con 10 por ciento de duplicados tardíos y 6 con ambos; aplicar solo si la versión es mayor deja 0 en todos los casos.",
               ["Cómo llegan los eventos", "Aplicar sin versión", "Aplicar solo si la versión es mayor"], rows, [380, 250, 290], row_h=44, size=13,
               note="Con 50 claves y 5 000 eventos cada clave cambia unas 100 veces, así que unos pocos errores significan que casi cualquier réplica real los tendría. Un borrado reordenado con un alta anterior revive la fila: la versión del borrado debe conservarse como lápida.",
               note_kind="teal", foot=SINT)


FIGURES = {
    "se-325-disponibilidad-en-cadena.svg": se325_cadena,
    "se-325-reintentos-apilados.svg": se325_reintentos,
    "se-325-cola-tras-una-caida.svg": se325_caida,
    "se-326-lo-que-lleva-el-mensaje.svg": se326_contenido,
    "se-326-comando-o-evento.svg": se326_destinatarios,
    "se-326-campos-del-sobre.svg": se326_sobre,
    "se-327-cola-topico-y-log.svg": se327_estructuras,
    "se-327-particiones-y-carga.svg": se327_particiones,
    "se-327-retencion-y-compactacion.svg": se327_retencion,
    "se-328-perdida-y-duplicados.svg": se328_semanticas,
    "se-328-orden-de-llegada.svg": se328_orden,
    "se-328-ventana-de-deduplicacion.svg": se328_ventana,
    "se-329-doble-escritura.svg": se329_doble,
    "se-329-relevo-del-outbox.svg": se329_relevo,
    "se-329-orden-de-pasos-de-una-saga.svg": se329_saga,
    "se-330-detectar-cambios.svg": se330_cambios,
    "se-330-costo-de-sincronizar.svg": se330_costo,
    "se-330-orden-y-repeticion.svg": se330_orden,
}
