"""Figures for SE-385 to SE-390 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_cases import case_cards
from figure_kit import Fig, fmt_es, grouped_bars, heatmap, line_chart, scatter
from figures_part07_a import bars

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Lectura de reloj de un equipo Windows 11 (CPython 3.12.9); en otro equipo los milisegundos cambian."


# ---------------------------------------------------------------- SE-385
def se385_camino() -> Fig:
    return grouped_bars("Un grafo de ataque de 12 aristas: costo mínimo para alterar una nota tras cada decisión de defensa",
                        "Barras con el costo mínimo del camino de ataque para alterar una nota tras cada decisión: 7 en la línea base y tras corregir la inyección SQL, 8 tras bloquear cada uno de los tres caminos más baratos y 27 tras el cuarto bloqueo, cuando ya no queda ninguna ruta de costo 10 o menos.",
                        ["Línea base", "Corregir la inyección SQL (+20 de costo)", "Bloquear el camino más barato", "Bloquear el segundo camino", "Bloquear el tercer camino", "Bloquear el cuarto camino"],
                        [("Costo mínimo del ataque", [7, 7, 8, 8, 8, 27], "teal")],
                        unit="costo mínimo para alterar una nota", decimals=0,
                        note="Caminos más baratos: la cuenta docente por phishing (6) y alterar nota (1) en la base, con 4 rutas de costo 10 o menos; tras la inyección quedan 3; los bloqueos cierran, en orden, la inyección SQL con base de datos directa, la cuenta de estudiante con rol elevado y el token de servicio filtrado; tras el cuarto el mínimo es la cuenta docente con +20. Arreglar lo que más asusta no movió el mínimo porque ese no era el camino más barato. Los costos son una escala del autor, no una medición de atacantes reales.",
                        note_kind="gold", foot=SINT)

def se385_puntajes() -> Fig:
    items = [
        ("Coincidencia por azar (5 de 30)", 16.7, "plain", "16,7 %"),
        ("Impacto × probabilidad (escala 1–5)", 46.4, "coral", "46,4 %"),
        ("Tres preguntas de sí o no", 54.1, "gold", "54,1 %"),
    ]
    return bars("Coincidencia de las cinco amenazas más graves entre tres revisores (30 amenazas, 300 repeticiones)",
                "Barras: dos revisores que puntúan las mismas 30 amenazas con impacto por probabilidad coinciden en 46,4 por ciento de sus cinco más graves; con tres preguntas de sí o no coinciden en 54,1 por ciento; el azar daría 16,7 por ciento.",
                items, 9.0, "Con ruido de un punto en cada escala, dos revisores comparten menos de la mitad de su top 5. Las preguntas de sí o no mejoran poco (la correlación de rangos pasa de 0,41 a 0,43): el beneficio principal es que cada respuesta se puede discutir y verificar. El ruido, 0,9 puntos, y el 10 % de respuestas invertidas son supuestos del autor.",
                label_w=300, width=940, note_kind="gold", foot=SINT)


def se385_deriva() -> Fig:
    return grouped_bars("300 cambios en un año, 24 cruzan una frontera de confianza: días con la frontera sin modelar",
                        "Barras horizontales con los días que una frontera nueva queda sin modelar según la política de revisión: una sola revisión inicial 209,3 de media y 364 de máximo, trimestral 53,3 y 89, por cambio de frontera 103,0 y 364, y por cambio más trimestral 25,0 y 88.",
                        ["Revisar el modelo una sola vez al empezar", "Revisión trimestral (días 90, 180, 270 y 360)", "Revisión al cambiar una frontera (la regla ve 12 de 24)", "Por cambio de frontera y además trimestral"],
                        [("Días sin modelar, media", [209.3, 53.3, 103.0, 25.0], "teal"), ("Máximo", [364, 89, 364, 88], "coral")],
                        unit="días con la frontera sin modelar", horizontal=True, label_w=320, value_fmt=lambda v: fmt_es(v, 0 if v in (364, 89, 88) else 1),
                        note="Ninguna política llega a cero: el disparador por cambio solo acierta donde la regla ve la frontera (12 de 24 en esta simulación) y la revisión periódica acota lo que la regla no ve. La combinación es la única que cierra el peor caso por debajo de los 90 días.",
                        note_kind="teal", foot=SINT)

# ---------------------------------------------------------------- SE-386
def se386_costo() -> Fig:
    return grouped_bars("Una hora de un núcleo contra 10 000 contraseñas filtradas: cuántas caen según cómo se guardaron",
                        "Barras agrupadas con el porcentaje de contraseñas rotas en una hora de un núcleo: con SHA-256 de una vuelta 70,0 sin sal y 46,2 con sal por usuario, con PBKDF2 de 1 000 iteraciones 70,0 y 9,0, con 600 000 iteraciones 22,5 y 0,9 y con scrypt 36,7 y 2,4.",
                        ["SHA-256 de una vuelta (0,0025 ms)", "PBKDF2, 1 000 iteraciones (2,38 ms)", "PBKDF2, 600 000 iteraciones (633 ms)", "scrypt N = 2^14, r = 8, p = 1 (72,4 ms)"],
                        [("Rotas sin sal", [70.0, 70.0, 22.5, 36.7], "coral"), ("Rotas con sal por usuario", [46.2, 9.0, 0.9, 2.4], "teal")],
                        unit="% de las 10 000 cuentas rotas en una hora", decimals=1,
                        note="Con sal, el atacante paga cada candidato una vez por usuario: 10 000 veces más. El costo de la función decide qué parte del 70 % de contraseñas «de diccionario» alcanza. La distribución de contraseñas (Zipf, exponente 0,8), el 30 % imposible de adivinar y el núcleo único son supuestos del autor.",
                        note_kind="gold", foot=REAL)

def se386_relleno() -> Fig:
    return grouped_bars("Relleno de credenciales contra 5 000 cuentas: cuántas de las 100 con contraseña reutilizada se comprometen",
                        "Barras horizontales con las cuentas comprometidas de 100 con contraseña reutilizada: 100 sin defensas, con límite por dirección IP o con bloqueo de la cuenta; 73 con segundo factor con 30 por ciento de adopción; 33 con rechazo de contraseñas filtradas; 24 con ambos.",
                        ["Ninguna defensa", "Límite de 5 intentos por hora por IP", "Bloqueo de la cuenta tras 5 fallos", "Segundo factor con 30 % de adopción", "Rechazo de contraseñas filtradas (cubre el 60 %)", "Segundo factor y rechazo de filtradas"],
                        [("Cuentas comprometidas", [100, 100, 100, 73, 33, 24], "coral")],
                        unit="cuentas comprometidas de 100", horizontal=True, label_w=310,
                        note="Dos controles muy citados no frenan este ataque porque el relleno reparte un intento por cuenta entre 2 000 direcciones y prueba las 5 000 cuentas en una hora. El bloqueo por cuenta, además, convierte al atacante en un denegador de servicio contra sus víctimas. Las tasas de reutilización (2 %), adopción (30 %) y cobertura del corpus (60 %) son supuestos del autor; ninguna defensa llega a cero.",
                        note_kind="coral", foot=SINT)

def se386_sesion() -> Fig:
    return case_cards("Cuántos intentos necesita alguien para quedarse con una sesión según cómo se generó el identificador",
                      "Tres identificadores de sesión como tarjetas: uno secuencial se adivina en unos 99 intentos entre 10 000 sesiones activas, uno sembrado con la hora del inicio se recupera probando 3 601 semillas de 7 201, y un token de 128 bits del sistema exige del orden de 3,4 por 10 elevado a 34 intentos.",
                      [("Identificador secuencial en un espacio de 1 000 000 con 10 000 sesiones", "99 intentos hasta acertar (se esperan 100)", "Se acierta una sesión ajena adivinando; el espacio efectivo es 1 de cada 100.", "coral"),
                       ("Semilla del generador = segundo del inicio de sesión", "3 601 de 7 201 candidatos", "El token de la víctima se recupera sabiendo la hora del inicio con ±1 hora.", "coral"),
                       ("128 bits del generador criptográfico del sistema (secrets)", "3,4 × 10^34 intentos esperados", "Adivinar no es el camino; quedan el robo del token y la fijación de sesión.", "teal")],
                      note="Un token largo no es seguro si su origen es predecible: la longitud no es la entropía. La seguridad real de la tercera fila depende de que el token no se filtre, caduque y se invalide al cerrar sesión, nada de lo cual mide este experimento.",
                      note_kind="gold", foot=SINT)

# ---------------------------------------------------------------- SE-387
def se387_mutantes() -> Fig:
    items = [
        ("Solo ruta feliz (18 pruebas)", 0, "coral", "0 de 13"),
        ("Negativas por rol (84)", 5, "coral", "5 de 13"),
        ("Rol × relación con el recurso (210)", 8, "gold", "8 de 13"),
        ("Rol × relación × estado × cabecera (1 692)", 13, "teal", "13 de 13"),
    ]
    return bars("Trece defectos de autorización plantados: cuántos detecta cada diseño de pruebas",
                "Barras: una suite de solo ruta feliz detecta 0 de 13 defectos de autorización plantados, las negativas por rol 5, la matriz de rol por relación con el recurso 8 y la matriz que añade estado y cabecera de rol del cliente detecta los 13.",
                items, 40.0, "Cada defecto necesita una dimensión distinta para aparecer: las matrices de rol y relación no ven el rol declarado por el cliente, la nota no publicada, la membresía revocada, el plazo vencido ni la acción desconocida. Los defectos y el modelo son del autor; las cifras miden el diseño de la matriz, no la tasa de defectos de un producto.",
                label_w=360, width=940, note_kind="teal", foot=SINT)


def se387_ids() -> Fig:
    return grouped_bars("Lectura de entregas ajenas: identificadores adivinables frente a comprobar el dueño (5 000 entregas)",
                        "Barras horizontales con las entregas ajenas leídas de 5 000: con identificadores secuenciales y sin comprobar el dueño 4 988 con 20 000 peticiones; con identificadores aleatorios y sin comprobar, adivinar lee 0 pero 150 identificadores filtrados leen 150; comprobar el dueño las reduce a 0 en ambos casos.",
                        ["Secuencial, sin comprobar el dueño (20 000 peticiones)", "Aleatorio (UUID), sin comprobar, adivinando (1 000 000)", "Aleatorio, sin comprobar, con el 3 % de los identificadores filtrados (150)",
                         "Secuencial, comprobando el dueño (20 000)", "Aleatorio, comprobando el dueño (1 000 000)"],
                        [("Entregas ajenas leídas", [4988, 0, 150, 0, 0], "coral")],
                        unit="entregas ajenas leídas de 5 000", horizontal=True, label_w=330,
                        note="El identificador aleatorio reduce la facilidad de enumerar y no es un control de acceso: cuando un identificador aparece en un correo, un enlace o un registro, la entrega queda al alcance de cualquiera. Solo la comprobación en el servidor, en cada petición, cierra el defecto.",
                        note_kind="coral", foot=SINT)

def se387_permisos() -> Fig:
    items = [
        ("Acumular sin revisar", 4.8, "coral", "4,8 sobrantes de 9,8 (49,1 %)"),
        ("Revisión trimestral (retira el 80 %)", 0.2, "gold", "0,2 de 5,2 (3,4 %)"),
        ("Permisos con caducidad de 30 días", 0.0, "teal", "0 de 5,0"),
        ("Reasignar permisos al cambiar de rol", 0.0, "teal", "0 de 5,0"),
    ]
    return bars("Permisos sobrantes por persona tras 24 meses con 5 % de cambios de rol al mes (300 personas)",
                "Barras: si los permisos solo se acumulan, cada persona acaba con 4,8 permisos que no necesita, casi la mitad de los 9,8 que tiene; la revisión trimestral los baja a 0,2; la caducidad de 30 días y la reasignación al cambiar de rol a cero.",
                items, 24.0, "La deriva no necesita un atacante: basta con que nadie retire lo que ya no hace falta. Una revisión que retira el 80 % deja residuo; una concesión que caduca y se renueva por necesidad no lo deja, a cambio de más solicitudes. La tasa de cambios y los 40 permisos del catálogo son supuestos del autor.",
                label_w=330, width=980, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-388
def se388_sql() -> Fig:
    return heatmap("Doce cargas por contexto contra SQLite real: cuántas alteran la consulta según la defensa",
                   "Mapa de calor con las cargas de 12 que alteran la consulta por defensa y contexto: concatenar deja pasar 4 en un valor de texto, 9 en un número y 4 en un identificador de ORDER BY; duplicar comillas cierra el texto y no el número; una lista de palabras deja pasar 1, 6 y 2; el parámetro enlazado cierra texto y número; solo la lista blanca resuelve el identificador.",
                   ["Concatenar el texto", "Duplicar las comillas simples", "Rechazar palabras (union, select, drop, delete)", "Parámetro enlazado", "Lista blanca de columnas"], ["Valor entre comillas", "Número sin comillas", "Identificador (ORDER BY)"],
                   [[4, 9, 4], [0, 9, 4], [1, 6, 2], [0, 0, 0], [None, None, 0]], unit="cargas que alteran (de 12)", scale="coral", vmin=0, vmax=12, label_w=330,
                   note="Duplicar comillas es la defensa correcta para un contexto y inútil en otro: el número no lleva comillas que cerrar. El parámetro enlazado separa dato de código, pero no puede enlazar el nombre de una columna: ORDER BY ? con «titulo DESC» no ordena (0 cargas alteran la consulta, pero tampoco ordena). Las 36 cargas son del autor y la lista de palabras se escribió sin ajustarla a ellas.",
                   note_kind="gold", foot="SQLite 3 del módulo estándar de CPython 3.12; cifras idénticas en Windows y Ubuntu (WSL2).")

def se388_contexto() -> Fig:
    return heatmap("Ocho cargas por contexto de salida: cuántas rompen el contexto según el codificador (modelo de reglas)",
                   "Mapa de calor con las cargas de 8 que rompen cada contexto de salida según el codificador: sin codificar 3 en texto HTML, 1 en atributo con comillas, 7 en atributo sin comillas, 4 en cadena JavaScript y 1 en URL; html.escape con comillas deja 4 en el atributo sin comillas y 1 en la URL; quote las anula todas.",
                   ["Ninguna", "html.escape sin comillas", "html.escape con comillas", "Codificación para cadena JavaScript", "urllib.parse.quote total"], ["Texto HTML", "Atributo con comillas", "Atributo sin comillas", "Cadena JS", "URL en href"],
                   [[3, 1, 7, 4, 1], [0, 1, 5, 2, 1], [0, 0, 4, 0, 1], [0, 1, 4, 0, 1], [0, 0, 0, 0, 0]], unit="cargas que rompen el contexto (de 8)", scale="coral", vmin=0, vmax=8, label_w=260,
                   note="Ningún codificador sirve para todos los contextos: html.escape no mira las comillas simples sin el parámetro, deja pasar un atributo sin comillas y no toca el esquema de una URL. quote lo anula todo porque destruye el significado. Es un modelo de reglas escrito por el autor, no un navegador.",
                   note_kind="coral", foot=SINT)

def se388_orden() -> Fig:
    return grouped_bars("84 variantes de 12 cargas (porcentaje, doble porcentaje, ancho completo, NUL) y 10 nombres legítimos",
                        "Barras agrupadas con las variantes aceptadas por tres órdenes de validación: validar antes de decodificar acepta 67 y 48 son peligrosas; decodificar y normalizar con lista negra acepta 50 y 31 son peligrosas; con lista blanca solo acepta 5, ninguna peligrosa, pero rechaza 5 de 10 nombres legítimos.",
                        ["Validar la forma recibida y decodificar después", "Decodificar, normalizar y validar con lista negra", "Decodificar, normalizar y validar con lista blanca"],
                        [("Variantes aceptadas", [67, 50, 5], "gold"), ("Peligrosas tras aceptar", [48, 31, 0], "coral"), ("Legítimos rechazados de 10", [0, 0, 5], "navy")],
                        unit="variantes o nombres",
                        note="Cambiar el orden reduce el daño (de 48 a 31) y la lista negra sigue incompleta. La lista blanca elimina lo peligroso y cuesta falsos rechazos: la regla ASCII estricta rechaza «María_López.pdf» y «informe final.pdf». Ese costo es una decisión de producto, no un error de la lista.",
                        note_kind="gold", foot=SINT)

# ---------------------------------------------------------------- SE-389
def se389_nonce() -> Fig:
    return grouped_bars("Cifrado de flujo de juguete (HMAC-SHA256 en modo contador) con y sin nonce repetido, 200 pares de mensajes",
                        "Barras agrupadas con lo que se recupera sin la clave de 200 pares de mensajes: con el mismo nonce se recupera el 100 por ciento de los bytes y la plantilla común acierta 200 de 200; con un nonce distinto de 96 bits se acierta el 0,4 por ciento de los bytes, lo que da el azar, y la plantilla 0 de 200.",
                        ["Nonce fijo para todos los mensajes", "Nonce aleatorio de 96 bits distinto en cada mensaje"],
                        [("Bytes recuperados sin la clave", [100.0, 0.4], "coral"), ("Acierto de la plantilla común (200 pares)", [100.0, 0.0], "gold")],
                        unit="% recuperado o acertado", decimals=1,
                        note="El XOR de dos textos cifrados con el mismo flujo es el XOR de los textos en claro; con uno conocido o una plantilla («Nota final: …») se lee el otro. Es una construcción didáctica: en producción se usa AEAD de una biblioteca revisada y el nonce nunca lo decide el llamador.",
                        note_kind="coral", foot=SINT)

def se389_comparacion() -> Fig:
    return grouped_bars("Consultas para falsificar una etiqueta de autenticación de 8 bytes según cómo se compara",
                        "Barras horizontales con el orden de magnitud de las consultas para falsificar una etiqueta de 8 bytes: 2 002, unos 10 elevado a 3,3, si la comparación termina en el primer byte distinto y el atacante ve cuántos coincidieron, y 9,2 por 10 elevado a 18, unos 10 elevado a 19, sin ninguna señal.",
                        ["Comparación que termina en el primer byte distinto", "Fuerza bruta sin señal (2^63 pruebas medias para 64 bits)"],
                        [("Consultas esperadas", [3.3014, 18.9638], "coral")],
                        unit="orden de magnitud de las consultas (potencia de 10)", horizontal=True, label_w=300, ticks=[0, 5, 10, 15, 20],
                        value_fmt=lambda v: "2 002" if v < 10 else "9,2 × 10^18",
                        note="El eje es el exponente de 10: dieciséis órdenes de magnitud separan las dos barras. Con una comparación de tiempo constante la señal toma un solo valor: no hay nada que medir y no hay una tercera barra que dibujar. Pasar de 9,2 × 10^18 a 2 002 es el valor de un oráculo de pasos. Aquí la señal es un contador perfecto; por la red real el ruido la degrada, pero un atacante con muchas repeticiones lo reduce. hmac.compare_digest elimina la señal en vez de confiar en el ruido.",
                        note_kind="gold", foot=SINT)

def se389_colision() -> Fig:
    ns = [500, 1000, 2000, 4000, 8000]
    return line_chart("Colisión de nonces aleatorios de 24 bits (1 500 repeticiones por punto) frente a 1 − exp(−n²/2^25)",
                      "Líneas con la probabilidad de repetir algún nonce de 24 bits según los mensajes con la misma clave: de 0,9 por ciento con 500 mensajes a 84,8 con 8 000, casi sobre la fórmula del cumpleaños, que da 0,7 y 85,1.",
                      [("Colisión observada", [(n, v, fmt_es(v, 1), "t") for n, v in zip(ns, [0.9, 2.9, 12.1, 39.5, 84.8])], "teal"),
                       ("Fórmula del cumpleaños", [(n, v, "" if n <= 1000 else fmt_es(v, 1), "b") for n, v in zip(ns, [0.7, 2.9, 11.2, 37.9, 85.1])], "grey")],
                      point_labels='none', x_label="Mensajes con la misma clave (n)", y_label="Probabilidad de colisión (%)", x_ticks=[(n, fmt_es(n)) for n in ns], y_ticks=[0, 20, 40, 60, 80, 100],
                      note="Con 96 bits, una probabilidad de colisión de 2^-32 llega con unos 6,07 × 10^9 mensajes por clave; NIST SP 800-38D limita las invocaciones con IV aleatorio de 96 bits a 2^32 por clave. Envolver un millón de claves de datos con una clave maestra mueve 48 MB; recifrar 2 TB de datos para rotar sin sobre-cifrado es unas 40 000 veces más.",
                      note_kind="teal", foot=SINT)

# ---------------------------------------------------------------- SE-390
def se390_escaner() -> Fig:
    return scatter("Escáner de secretos de juguete sobre 500 líneas con 60 secretos plantados y 140 señuelos",
                   "Puntos con los secretos detectados de 60 y las falsas alarmas de cuatro escáneres: patrones de proveedor 40 detectados y 24 falsas alarmas, palabra clave 38 y 51, entropía 45 y 21, y la combinación de patrones y palabra clave con entropía 60 y 24; ninguno encuentra todo sin falsas alarmas.",
                   [("Solo patrones de proveedor", [(24, 40, "40 · 24", "r")], "teal"), ("Solo palabra clave (password=, secret=)", [(51, 38, "38 · 51", "l")], "gold"),
                    ("Solo entropía de las cadenas largas", [(21, 45, "45 · 21", "l")], "coral"), ("Patrones, y palabra clave con entropía", [(24, 60, "60 · 24", "r")], "navy")],
                   x_label="Falsas alarmas (de 140 señuelos)", y_label="Secretos detectados (de 60)", x_ticks=[(x, str(x)) for x in (0, 10, 20, 30, 40, 50, 60)], y_ticks=[0, 20, 40, 60],
                   note="Precisión y exhaustividad: patrones 62,5 % y 66,7 %; palabra clave 42,7 % y 63,3 %; entropía 68,2 % y 75,0 %; combinación 71,4 % y 100,0 %. La combinación llega al 100 % de exhaustividad porque se escribió conociendo los formatos plantados: es una frontera, no una tasa de detección. Las 24 falsas alarmas son ejemplos de documentación con forma de secreto. Todas las cadenas se generan al ejecutar; ninguna es una credencial real.",
                   note_kind="gold", foot=SINT)

def se390_rotacion() -> Fig:
    return grouped_bars("Rotar una clave entre 20 instancias (100 solicitudes por segundo, 600 s, 10 semillas)",
                        "Barras horizontales con el porcentaje de solicitudes fallidas de 60 000 según la estrategia: aceptar solo la clave nueva desde el inicio falla el 28,77 por ciento, doble validez con cierre fijo a los 360 segundos falla el 1,59 y cerrar cuando ninguna instancia usa la vieja no falla ninguna y mantiene la vieja 538 segundos.",
                        ["Corte: el verificador solo acepta la nueva desde el segundo 0 (0 s con la vieja)", "Doble validez con cierre fijo a los 360 s (360 s)", "Doble validez; se cierra cuando ninguna instancia usa la vieja (538 s)"],
                        [("Solicitudes fallidas", [28.77, 1.59, 0.0], "coral")],
                        unit="% de solicitudes fallidas de 60 000", horizontal=True, label_w=340, decimals=2,
                        note="Fallidas: 17 262, 956 y 0. Rotar sin caída cuesta una ventana en que dos secretos valen (los segundos entre paréntesis). En 8 de las 10 semillas una instancia no recarga: el cierre fijo la deja fuera y el cierre condicionado la espera, es decir, una rotación incompleta es visible en vez de silenciosa. Los tiempos de recarga (0 a 300 s) son un supuesto del autor.",
                        note_kind="teal", foot=SINT)

def se390_radio() -> Fig:
    return grouped_bars("Radio de una credencial filtrada: 3 ambientes × 5 servicios × 6 recursos (3 000 fugas al azar)",
                        "Barras agrupadas con los recursos que alcanza una credencial filtrada: válida en todos los ambientes alcanza 90 de 90 y 30 de 30 de producción; una por ambiente alcanza 30 y 10; una por servicio y ambiente 6 y 1,9 de media.",
                        ["Una credencial válida en todos los ambientes", "Una credencial por ambiente", "Una credencial por servicio y ambiente"],
                        [("Recursos alcanzados de 90", [90, 30, 6], "coral"), ("De producción (de 30)", [30, 10, 1.9], "navy")],
                        unit="recursos alcanzados de media",
                        note="Separar ambientes y servicios no evita la fuga: reduce lo que vale lo filtrado. La separación no cubre los datos: una copia de producción en staging expone todos los registros aunque la credencial de staging no abra producción. La fuga uniforme entre ambientes es un supuesto del autor.",
                        note_kind="gold", foot=SINT)

FIGURES = {
    "se-385-camino-mas-barato.svg": se385_camino,
    "se-385-puntajes-dispares.svg": se385_puntajes,
    "se-385-deriva-del-modelo.svg": se385_deriva,
    "se-386-costo-de-adivinar.svg": se386_costo,
    "se-386-relleno-de-credenciales.svg": se386_relleno,
    "se-386-adivinar-una-sesion.svg": se386_sesion,
    "se-387-mutantes-de-autorizacion.svg": se387_mutantes,
    "se-387-identificadores-adivinables.svg": se387_ids,
    "se-387-acumulacion-de-permisos.svg": se387_permisos,
    "se-388-defensas-sql.svg": se388_sql,
    "se-388-contexto-de-salida.svg": se388_contexto,
    "se-388-orden-de-validacion.svg": se388_orden,
    "se-389-nonce-repetido.svg": se389_nonce,
    "se-389-comparacion-temprana.svg": se389_comparacion,
    "se-389-colision-de-nonces.svg": se389_colision,
    "se-390-escaner-de-secretos.svg": se390_escaner,
    "se-390-rotacion-sin-caida.svg": se390_rotacion,
    "se-390-radio-de-una-fuga.svg": se390_radio,
}
