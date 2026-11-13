"""Figures for SE-241 to SE-246 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time or a thread count is shown)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2), salvo los tiempos y los recuentos de hilos indicados."


# ---------------------------------------------------------------- SE-241
def se241_cadena() -> Fig:
    items = [
        ("Síncrona, correo sano", 12.47, "coral", "12,47 %"),
        ("Síncrona, 2 % de envíos lentos", 14.21, "coral", "14,21 %"),
        ("Síncrona, 10 % de envíos lentos", 21.42, "coral", "21,42 %"),
        ("Diferida (base de datos + encolar)", 0.0, "teal", "0,00 %"),
    ]
    return bars("Solicitudes que superan el tiempo máximo del cliente (1 s): cadena síncrona frente a trabajo diferido",
                "Barras de 100 000 solicitudes simuladas con tiempo máximo de 1 segundo: la cadena síncrona con base de datos, análisis de archivo y correo supera el límite en 12,47 por ciento con correo sano, 14,21 con 2 por ciento de envíos lentos y 21,42 con 10 por ciento; la versión que solo guarda y encola no lo supera nunca.",
                items, 22, "La cadena síncrona suma tres latencias (mediana 8 ms + 400 ms + 150 ms) y hereda la cola larga del peor eslabón: con 10 % de envíos lentos el p95 sube a 5 412 ms. Responder tras guardar y encolar (mediana 10 ms, p99 22 ms) separa lo que se promete ahora de lo que se completa después.",
                label_w=340, width=1000, note_kind="coral", foot=SINT)


def se241_caidas() -> Fig:
    rows = [["Sin outbox: 6 órdenes de archivo, fila y evento × 4 puntos de caída", "10 de 24 con violación grave", "fila sin archivo 4 · fila sin evento 4 · evento sin fila 4 · archivo huérfano 4"],
            ["Con outbox: archivo, luego fila y outbox en una transacción, luego relevo (3 puntos de caída)", "0 de 3", "fila sin archivo 0 · fila sin evento 0 · evento sin fila 0 · archivo huérfano 1 (limpiable)"],
            ["Caída dentro de la transacción", "0 filas, 0 eventos", "SQLite revierte las dos inserciones a la vez"],
            ["El relevo publica y cae antes de marcar el evento como enviado", "2 publicaciones del mismo evento", "entrega al menos una vez: el consumidor debe tolerar el duplicado"]]
    return tab("Qué estados quedan tras una caída en el alta de una entrega",
               "Tabla: sin outbox, 10 de 24 combinaciones de orden y punto de caída dejan una violación grave; con archivo, fila más outbox transaccional y relevo, no queda ninguna violación grave, solo un archivo huérfano limpiable, y el relevo puede publicar un evento dos veces.",
               ["Diseño", "Resultado", "Qué queda inconsistente"], rows, [380, 220, 400], row_h=74, size=12,
               note="El modelo enumera todos los puntos de caída de tres pasos; no incluye caídas de disco, corrupción ni varios procesos concurrentes. La transacción atómica se comprobó con SQLite real; el archivo y el bus son simulados.", note_kind="gold", foot=SINT)


def se241_servidor() -> Fig:
    items = [
        ("Un solo hilo · Windows", 3.42, "coral", "3,42 s"),
        ("Un solo hilo · Ubuntu", 2.60, "coral", "2,60 s"),
        ("Un hilo por solicitud · Windows", 0.16, "teal", "0,16 s"),
        ("Un hilo por solicitud · Ubuntu", 0.14, "teal", "0,14 s"),
        ("Tope de 8 en curso · 16 servidas, 24 con 503", 0.15, "gold", "0,15 s (Windows)"),
    ]
    return bars("40 clientes simultáneos contra un servidor local real que tarda 50 ms por solicitud",
                "Barras con el tiempo total de 40 solicitudes concurrentes: un servidor de un solo hilo tarda 3,42 segundos en Windows y 2,60 en Ubuntu, uno con un hilo por solicitud 0,16 y 0,14, y uno con tope de 8 solicitudes en curso 0,15 segundos pero rechaza 24 con el código 503.",
                items, 130, "Teóricamente 40 × 50 ms = 2 s; Windows añadió granularidad de temporizador. El tope de 8 acaba pronto porque rechaza lo que no cabe: devolver 503 rápido protege al proceso a cambio de que el cliente reintente. Tiempos de un equipo, no una promesa de capacidad.",
                label_w=380, width=1000, note_kind="gold", foot="Servidor HTTP de la biblioteca estándar, 127.0.0.1, medido; los tiempos dependen del equipo.")


# ---------------------------------------------------------------- SE-242
def se242_prefetcher() -> Fig:
    items = [("GET /entregas/{id}/borrar (efecto en un GET)", 200, "coral", "200 de 200 borradas"),
             ("DELETE /entregas/{id}", 0, "teal", "0 borradas")]
    return bars("Un recorrido de enlaces (prefetcher, buscador, antivirus de correo) sobre 200 entregas",
                "Barras: un rastreador que solo hace GET borra 200 de 200 entregas si el borrado está modelado como un GET con efecto, y 0 si el borrado es un DELETE.",
                items, 2.4, "GET es seguro por contrato: cualquier intermediario puede repetirlo, precargarlo o cachearlo. Un enlace de borrado que responde a GET entrega la decisión a quien rastrea la página. Un DELETE no se dispara por navegar.",
                label_w=430, width=1060, note_kind="coral", foot=SINT)


def se242_if_match() -> Fig:
    rows = [["PUT sin precondición", "1 000 de 1 000 rondas pierden una edición en silencio", "0", "0 de 1 000"],
            ["PUT con If-Match y 412", "0", "1 000 (el segundo escritor se entera)", "0 de 1 000"],
            ["If-Match, 412 y reaplicar el cambio sobre la versión nueva", "0", "1 000", "1 000 de 1 000"]]
    return tab("Dos clientes editan la misma entrega: qué ocurre con el segundo PUT",
               "Tabla de 1 000 rondas: sin If-Match el segundo PUT pisa al primero en las 1 000 rondas; con If-Match el servidor responde 412 al segundo y no se pierde nada; si el cliente relee y reaplica su cambio, las 1 000 rondas terminan con las dos ediciones.",
               ["Diseño", "Ediciones perdidas en silencio", "Respuestas 412", "Rondas con ambas ediciones"], rows, [330, 270, 240, 190], row_h=64, size=12,
               note="El orden de ejecución se sorteó con semilla fija, pero el resultado no depende de ella: es una propiedad del protocolo. Lo que no se midió es la tasa real de conflictos de un producto, que depende de cuántas personas editan el mismo recurso.", note_kind="gold", foot=SINT)


def se242_paginacion() -> Fig:
    rows = [["Offset 50 (order by ts desc)", "1 168", "161", "1 000 de 1 000"],
            ["Keyset (ts < último visto)", "1 007", "0", "1 000 de 1 000"]]
    return tab("Paginar 1 000 entregas mientras llegan 7 nuevas antes de cada página",
               "Tabla: con paginación por desplazamiento (offset) se devuelven 1 168 filas con 161 repetidas; con paginación por clave (keyset) se devuelven 1 007 filas sin repetidas; las dos terminan viendo las 1 000 originales.",
               ["Estrategia", "Filas devueltas", "Filas repetidas", "Originales vistas"], rows, [330, 200, 200, 220], row_h=56, size=13,
               note="Las inserciones empujan las filas hacia abajo y el offset las vuelve a entregar. Keyset elimina las repetidas, pero no permite saltar a la página 40 y exige un orden total (marca de tiempo más identificador). Si se borran filas, el offset en cambio omite filas; aquí no se simuló el borrado.", note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-243
def se243_bytes() -> Fig:
    items = [("REST con recursos completos (2 viajes)", 20991, "coral", "20 991 B"),
             ("REST con campos seleccionados (2 viajes)", 1272, "gold", "1 272 B"),
             ("Llamada a medida tipo RPC (1 viaje)", 1276, "teal", "1 276 B")]
    return bars("Bytes que recibe la pantalla «entregas de un curso» (50 entregas) según el estilo de interfaz",
                "Barras: con recursos REST completos la pantalla recibe 20 991 bytes en dos viajes, con campos seleccionados 1 272 bytes en dos viajes y con una llamada a medida 1 276 bytes en un viaje; la pantalla usa 2 de 6 campos de cada entrega.",
                items, 0.024, "Solo el 6,1 % de los bytes del diseño con recursos completos sirve a la pantalla. Seleccionar campos o diseñar una llamada para la pantalla da el mismo tamaño; la diferencia es cuántos viajes y quién carga con el acoplamiento (la pantalla conoce campos, o el servidor conoce pantallas).",
                label_w=360, width=1000, note_kind="gold", foot=SINT)


def se243_n_mas_1() -> Fig:
    items = [("10 cursos · resolvedor ingenuo", 11, "coral", "11 consultas"),
             ("10 cursos · por lotes", 2, "teal", "2"),
             ("50 cursos · resolvedor ingenuo", 51, "coral", "51"),
             ("50 cursos · por lotes", 2, "teal", "2"),
             ("200 cursos · resolvedor ingenuo", 201, "coral", "201"),
             ("200 cursos · por lotes", 2, "teal", "2")]
    return bars("Consultas SQL para devolver cursos con sus entregas",
                "Barras con el número de consultas SQL medido con un contador sobre SQLite: un resolvedor ingenuo hace 11, 51 y 201 consultas para 10, 50 y 200 cursos, y la carga por lotes hace 2 en los tres casos.",
                items, 2.4, "El problema N+1 es independiente del estilo: ocurre en REST con includes y en GraphQL con resolvedores por campo. La carga por lotes lo evita en la capa de datos, no en el contrato. Con un SQLite en memoria cada consulta es barata; con red y base de datos remota cada una pagaría una latencia.",
                label_w=340, width=1000, note_kind="gold", foot=SINT)


def se243_profundidad() -> Fig:
    rows = [["1", "20", "43,15 %"], ["2", "420", "18,62 %"], ["3", "8 420", "7,89 %"], ["4", "168 420", "3,31 %"],
            ["5", "3 368 420", "1,48 %"], ["6", "67 368 420", "0,00 %"]]
    return tab("Límite de profundidad: nodos que permite y consultas legítimas que rechaza",
               "Tabla: con 20 elementos por nivel, una consulta de profundidad 6 resuelve 67 368 420 nodos; un límite de profundidad 2 rechaza 18,62 por ciento de 10 000 consultas legítimas sintéticas, uno de 3 el 7,89, uno de 4 el 3,31 y uno de 5 el 1,48.",
               ["Límite de profundidad", "Nodos de la consulta más profunda permitida (20 por nivel)", "Consultas legítimas rechazadas por ese límite"], rows, [160, 330, 480], row_h=40, size=13,
               note="Se acotan el coste y no solo la forma: un límite de 10 000 nodos acepta hasta profundidad 3 y uno de 1 000 solo hasta 2. La distribución de consultas legítimas es una suposición del autor (exponencial, media 1,2 niveles), no una medición de clientes reales.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-244
def se244_validadores() -> Fig:
    rows = [["alumno_id = true", "acepta", "rechaza"], ["horas_retraso = 2.5", "acepta", "rechaza"], ["horas_retraso = Infinity", "acepta", "rechaza"],
            ["alumno_id = 99999999999999999999", "acepta", "rechaza"], ["campo extra is_admin", "acepta", "rechaza"],
            ["clave alumno_id repetida (gana la última)", "acepta", "rechaza"], ["texto de 6 000 caracteres", "acepta", "rechaza"],
            ["horas_retraso = NaN", "rechaza (por azar: NaN ≥ 0 es falso)", "rechaza"]]
    return tab("14 cargas JSON límite: errores de un validador con isinstance y de uno estricto",
               "Tabla: de 14 cargas JSON, el validador basado en isinstance se equivoca en 11 y el estricto en 0; aceptó booleanos como enteros, decimales, Infinity, enteros enormes, campos extra, claves repetidas y textos de 6 000 caracteres.",
               ["Carga que debe rechazarse", "Validador ingenuo", "Validador estricto"], rows, [400, 330, 210], row_h=40, size=12,
               note="Errores: ingenuo 11 de 14, estricto 0 de 14. En Python bool es subclase de int y json.loads acepta NaN e Infinity por defecto. Que el estricto acierte las 14 solo prueba que se escribió mirándolas: otras cargas (unicode normalizado, enteros con ceros) no se probaron.", note_kind="coral", foot=SINT)


def se244_deriva() -> Fig:
    items = [("Solo código de estado + ejemplo parcial (id y estado)", 155, "coral", "155 de 283"),
             ("Esquema abierto (tipos y campos obligatorios)", 181, "gold", "181"),
             ("Esquema cerrado (sin campos extra)", 232, "gold", "232"),
             ("Esquema cerrado + enumeración del estado", 283, "teal", "283")]
    return bars("Mutaciones de una respuesta que detecta cada comprobación (283 mutaciones reales de 300)",
                "Barras: de 283 mutaciones que cambian una respuesta, un ejemplo parcial detecta 155, un esquema abierto 181, uno cerrado 232 y uno cerrado con enumeración del estado las 283; 17 mutaciones no cambiaban nada.",
                items, 1.5, "Cada capa atrapa algo que la anterior dejaba pasar: campos extra (filtraciones como debug_sql) y valores fuera de la enumeración. Las 283 detectadas son las mutaciones que el autor imaginó (quitar, tipar mal, añadir, anular, renombrar, valor): una deriva de significado con la forma intacta no se ve.",
                label_w=420, width=1060, note_kind="teal", foot=SINT)


def se244_reintentos() -> Fig:
    items = [("No reintentar", 0, "grey", "0 extra · 0 recuperados"),
             ("Reintentar todo (3 veces)", 20749, "coral", "20 749 extra · 5 677 recuperados · 3,65 por recuperado"),
             ("Reintentar solo 429, 503 y timeout", 8806, "teal", "8 806 extra · 5 660 recuperados · 1,56 por recuperado")]
    return bars("Solicitudes adicionales según la clasificación del error (10 000 fallos, 40 % permanentes)",
                "Barras: reintentar todos los fallos genera 20 749 solicitudes adicionales para recuperar 5 677; reintentar solo 429, 503 y tiempo agotado genera 8 806 para recuperar 5 660; no reintentar no genera ninguna.",
                items, 0.0125, "Los 4xx permanentes (el 40 % de la mezcla supuesta) nunca se recuperan y solo cargan al servidor. Clasificar el error cuesta 17 recuperaciones menos y 11 943 solicitudes menos. La mezcla y las probabilidades de recuperación son supuestos del autor.",
                label_w=300, width=1100, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-245
def se245_ataques() -> Fig:
    rows = [["Alg none sin firma", "acepta", "rechaza"], ["Payload alterado con firma vieja", "rechaza", "rechaza"], ["Firma truncada", "rechaza", "rechaza"],
            ["Token expirado", "acepta", "rechaza"], ["Audiencia de otra API", "acepta", "rechaza"], ["Emisor desconocido", "acepta", "rechaza"],
            ["Aún no válido (nbf futuro)", "acepta", "rechaza"], ["Clave equivocada", "rechaza", "rechaza"]]
    return tab("Ocho ataques a un token firmado: verificador ingenuo y verificador estricto",
               "Tabla: de ocho ataques, el verificador que solo comprueba la firma y confía en la cabecera acepta cinco (alg none, expirado, audiencia ajena, emisor desconocido y nbf futuro); el estricto, que fija el algoritmo y comprueba emisor, audiencia y vigencia, rechaza los ocho.",
               ["Ataque", "Ingenuo", "Estricto"], rows, [430, 190, 190], row_h=40, size=13,
               note="El token y la clave son sintéticos; el esquema es de laboratorio y no sustituye una biblioteca revisada. La firma válida solo dice quién emitió el token: pertenencia, audiencia y vigencia son reglas aparte. Aceptados: ingenuo 5 de 8, estricto 0 de 8.", note_kind="coral", foot=SINT)


def se245_ids() -> Fig:
    items = [("Secuenciales, sin comprobar dueño, prueba 1..1000", 984, "coral", "984 filas ajenas"),
             ("Secuenciales, comprobando dueño", 0, "teal", "0"),
             ("UUID, sin comprobar, 1 000 intentos al azar", 0, "gold", "0"),
             ("UUID, sin comprobar, 100 ids filtrados en un registro", 95, "coral", "95"),
             ("UUID, comprobando dueño, 100 ids filtrados", 0, "teal", "0")]
    return bars("Filas ajenas que obtiene un alumno autenticado que prueba identificadores (1 000 entregas, 50 usuarios)",
                "Barras: con identificadores secuenciales y sin comprobar el dueño, el alumno obtiene 984 filas ajenas; con comprobación 0; con UUID adivinados al azar 0; con 100 UUID filtrados y sin comprobar 95; con comprobación 0.",
                items, 0.46, "Un identificador impredecible reduce la enumeración pero no sustituye la comprobación de dueño: en cuanto un identificador se filtra (URL compartida, registro, correo), la fila queda expuesta. Las 16 filas propias de u-0 no se cuentan como filtración.",
                label_w=470, width=1100, note_kind="coral", foot=SINT)


def se245_politica() -> Fig:
    items = [("12 casos: solo los permitidos", 12, "gold", "12 de 48"),
             ("24 casos: 12 permitidos + 12 denegados", 24, "gold", "24 de 48"),
             ("48 casos: todo el espacio de decisiones", 48, "teal", "48 de 48")]
    return bars("Decisiones de la política que una suite de pruebas protege (48 = 3 roles × 4 recursos × 4 acciones)",
                "Barras: de 48 decisiones de política, una suite con solo los 12 permisos concedidos detecta 12 mutaciones, una con 12 permisos y 12 denegaciones detecta 24 y una que recorre las 48 las detecta todas; 36 de las 48 decisiones son denegaciones.",
                items, 11, "Cada caso protege una sola decisión: invertir una celda no lo ve nadie que no la haya probado. Como 36 de 48 decisiones son denegaciones, una suite que solo comprueba que lo permitido funciona nunca verá una apertura indebida. Con 5 casos al azar se detectan 5 de 48.",
                label_w=440, width=1040, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-246
def se246_duplicados() -> Fig:
    items = [("Sin clave · respuesta perdida 1 %", 0.82, "coral", "0,82 %"),
             ("Sin clave · 5 %", 5.30, "coral", "5,30 %"),
             ("Sin clave · 20 %", 23.84, "coral", "23,84 %"),
             ("Con Idempotency-Key · 1, 5 y 20 %", 0.0, "teal", "0,00 %")]
    return bars("Entregas duplicadas tras reintentar cuando se pierde la respuesta (5 000 entregas, hasta 3 intentos)",
                "Barras: sin clave de idempotencia, perder la respuesta con probabilidad 1, 5 y 20 por ciento duplica 0,82, 5,30 y 23,84 por ciento de las entregas; con clave y restricción única el porcentaje es 0 en los tres casos.",
                items, 20, "El servidor confirmó la escritura y el cliente no lo supo: el reintento es indistinguible de una solicitud nueva sin una clave. La restricción única de la base de datos convierte el segundo insert en un error controlado y se devuelve la respuesta guardada.",
                label_w=320, width=1000, note_kind="coral", foot=SINT)


def se246_tormenta() -> Fig:
    rows = [["Intervalo fijo de 1 s", "2 000", "3 s", "800"], ["Exponencial sin jitter", "2 000", "4 s", "0"], ["Exponencial con jitter total", "372", "0 s", "0"]]
    return tab("2 000 clientes reintentan tras una caída de 5 s con capacidad de 400 solicitudes por segundo",
               "Tabla: tras la caída, con intervalo fijo el pico es de 2 000 solicitudes por segundo, hay 3 segundos sobre la capacidad y 800 clientes abandonan tras 8 intentos; con retroceso exponencial sin jitter el pico es 2 000 y hay 4 segundos sobre la capacidad; con jitter total el pico baja a 372 y no se supera la capacidad.",
               ["Política de reintento", "Pico tras la caída (solicitudes por segundo)", "Segundos sobre la capacidad", "Clientes que abandonan"], rows, [330, 270, 210, 190], row_h=56, size=12,
               note="Sin aleatoriedad, los clientes que fallaron a la vez vuelven a la vez: el retroceso exponencial solo los espacia en oleadas. El jitter reparte la carga. El modelo supone una capacidad fija y clientes idénticos; no representa colas del servidor ni presión posterior.", note_kind="gold", foot=SINT)


def se246_ventana() -> Fig:
    items = [("TTL de la clave: 10 min", 66.9, "coral", "66,9 %"), ("TTL 1 h", 50.9, "coral", "50,9 %"),
             ("TTL 24 h", 33.3, "gold", "33,3 %"), ("TTL 48 h", 16.9, "gold", "16,9 %")]
    return bars("Reintentos que llegan después de que la clave caducó y crean un duplicado (6 000 reintentos)",
                "Barras: con una distribución supuesta de retardos de reintento de 1 minuto a 7 días, una clave que caduca a los 10 minutos deja pasar 66,9 por ciento de los reintentos como duplicados, a 1 hora 50,9, a 24 horas 33,3 y a 48 horas 16,9.",
                items, 7, "La ventana de la clave debe cubrir el reintento más tardío que el cliente pueda hacer (colas offline, aplicaciones móviles). La misma clave con otra carga debe devolver 422 en vez de la respuesta guardada: la huella de la carga lo distingue (765f4a431bef frente a aaa1c9e4780f). Con 8 hilos y la misma clave, 1 inserta y 7 se detectan como repetidos.",
                label_w=300, width=1000, note_kind="gold", foot=SINT)


FIGURES = {
    "se-241-cadena-sincrona-frente-a-diferida.svg": se241_cadena,
    "se-241-caidas-en-el-alta-de-una-entrega.svg": se241_caidas,
    "se-241-servidor-de-un-hilo-frente-a-hilos.svg": se241_servidor,
    "se-242-recorrido-de-enlaces-sobre-un-get-con-efecto.svg": se242_prefetcher,
    "se-242-actualizacion-perdida-e-if-match.svg": se242_if_match,
    "se-242-paginacion-offset-frente-a-keyset.svg": se242_paginacion,
    "se-243-bytes-por-pantalla.svg": se243_bytes,
    "se-243-consultas-n-mas-1.svg": se243_n_mas_1,
    "se-243-profundidad-y-coste-de-consultas.svg": se243_profundidad,
    "se-244-validador-ingenuo-frente-a-estricto.svg": se244_validadores,
    "se-244-deriva-entre-contrato-y-respuesta.svg": se244_deriva,
    "se-244-reintentos-segun-el-tipo-de-error.svg": se244_reintentos,
    "se-245-ocho-ataques-a-un-token.svg": se245_ataques,
    "se-245-identificadores-y-comprobacion-de-dueno.svg": se245_ids,
    "se-245-cobertura-de-la-politica.svg": se245_politica,
    "se-246-duplicados-tras-perder-la-respuesta.svg": se246_duplicados,
    "se-246-tormenta-de-reintentos.svg": se246_tormenta,
    "se-246-ventana-de-la-clave.svg": se246_ventana,
}
