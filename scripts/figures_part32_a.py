"""Figures for SE-385 to SE-390 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
REAL = "Lectura de reloj de un equipo Windows 11 (CPython 3.12.9); en otro equipo los milisegundos cambian."


# ---------------------------------------------------------------- SE-385
def se385_camino() -> Fig:
    rows = [
        ["Línea base", "7", "internet → cuenta docente (phishing, 6) → alterar nota (1); 4 rutas de costo 10 o menos"],
        ["Corregir la inyección SQL (+20 de costo)", "7", "El camino más barato no cambia; quedan 3 rutas de costo 10 o menos"],
        ["Bloquear el camino más barato", "8", "internet → inyección SQL → base de datos directa → alterar nota"],
        ["Bloquear el segundo camino", "8", "internet → cuenta de estudiante → rol elevado → alterar nota"],
        ["Bloquear el tercer camino", "8", "internet → token de servicio filtrado → alterar nota"],
        ["Bloquear el cuarto camino", "27", "Ninguna ruta de costo 10 o menos; el mínimo ahora es la cuenta docente con +20"],
    ]
    return tab("Un grafo de ataque de 12 aristas: costo mínimo para alterar una nota tras cada decisión de defensa",
               "Tabla: en el grafo de ataque de la plataforma el camino más barato cuesta 7 por la cuenta docente; corregir la inyección SQL lo deja en 7; bloquear en orden el camino más barato lo sube a 8 tres veces y a 27 tras el cuarto bloqueo.",
               ["Decisión de defensa", "Costo mínimo", "Camino más barato resultante"], rows, [330, 120, 470], row_h=58, size=12,
               note="Arreglar lo que más asusta (la inyección) no movió el mínimo porque ese no era el camino más barato. Hicieron falta cuatro bloqueos, uno por camino, para pasar de 7 a 27. Los costos de las aristas son una escala del autor, no una medición de atacantes reales.",
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
    rows = [
        ["Revisar el modelo una sola vez al empezar", "209,3", "364"],
        ["Revisión trimestral (días 90, 180, 270 y 360)", "53,3", "89"],
        ["Revisión al cambiar una frontera (la regla ve 12 de 24)", "103,0", "364"],
        ["Por cambio de frontera y además trimestral", "25,0", "88"],
    ]
    return tab("300 cambios en un año, 24 cruzan una frontera de confianza: días con la frontera sin modelar",
               "Tabla: con una sola revisión inicial la frontera nueva queda sin modelar 209,3 días de media; con revisión trimestral 53,3; con un disparador por cambio que solo ve la mitad de las fronteras 103,0; y con disparador más revisión trimestral 25,0 días de media y 88 de máximo.",
               ["Política de revisión", "Días sin modelar, media", "Máximo"], rows, [560, 200, 160], row_h=46, size=13,
               note="Ninguna política llega a cero: el disparador por cambio solo acierta donde la regla ve la frontera (12 de 24 en esta simulación) y la revisión periódica acota lo que la regla no ve. La combinación es la única que cierra el peor caso por debajo de los 90 días.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-386
def se386_costo() -> Fig:
    rows = [
        ["SHA-256 de una vuelta", "0,0025", "70,0 %", "46,2 %"],
        ["PBKDF2-HMAC-SHA256, 1 000 iteraciones", "2,38", "70,0 %", "9,0 %"],
        ["PBKDF2-HMAC-SHA256, 600 000 iteraciones", "633", "22,5 %", "0,9 %"],
        ["scrypt (N = 2^14, r = 8, p = 1)", "72,4", "36,7 %", "2,4 %"],
    ]
    return tab("Una hora de un núcleo contra 10 000 contraseñas filtradas: cuántas caen según cómo se guardaron",
               "Tabla: con una función de una vuelta, una hora de un núcleo rompe el 70 por ciento de las cuentas con o sin sal en el mejor caso del modelo; con 600 000 iteraciones de PBKDF2 solo el 22,5 por ciento sin sal y el 0,9 por ciento con sal por usuario.",
               ["Función de derivación", "ms por hash", "Rotas sin sal", "Rotas con sal por usuario"], rows, [400, 140, 170, 210], row_h=46, size=13,
               note="Con sal, el atacante paga cada candidato una vez por usuario: 10 000 veces más. El costo de la función decide qué parte del 70 % de contraseñas «de diccionario» alcanza. La distribución de contraseñas (Zipf, exponente 0,8), el 30 % imposible de adivinar y el núcleo único son supuestos del autor.",
               note_kind="gold", foot=REAL)


def se386_relleno() -> Fig:
    rows = [
        ["Ninguna defensa", "100", "Todas las cuentas con contraseña reutilizada"],
        ["Límite de 5 intentos por hora por dirección IP", "100", "2 000 direcciones prueban las 5 000 cuentas en una hora"],
        ["Bloqueo de la cuenta tras 5 fallos", "100", "El relleno usa un intento por cuenta; un atacante que falle a propósito bloquearía a las 5 000"],
        ["Segundo factor con 30 % de adopción", "73", "Protege solo a quien lo activó"],
        ["Rechazo de contraseñas filtradas (cubre el 60 %)", "33", "Depende de qué corpus de filtraciones se consulta"],
        ["Segundo factor y rechazo de filtradas", "24", "Las defensas se complementan; ninguna llega a cero"],
    ]
    return tab("Relleno de credenciales contra 5 000 cuentas: cuántas de las 100 con contraseña reutilizada se comprometen",
               "Tabla: sin defensas se comprometen 100 de 100 cuentas con contraseña reutilizada; un límite por dirección IP y un bloqueo por cuenta no cambian la cifra; el segundo factor con 30 por ciento de adopción la baja a 73; el rechazo de contraseñas filtradas a 33; ambos a 24.",
               ["Defensa", "Cuentas comprometidas", "Por qué"], rows, [370, 150, 400], row_h=58, size=12,
               note="Dos controles muy citados no frenan este ataque porque el relleno reparte un intento por cuenta entre muchas direcciones. El bloqueo por cuenta, además, convierte al atacante en un denegador de servicio contra sus víctimas. Las tasas de reutilización (2 %), adopción (30 %) y cobertura del corpus (60 %) son supuestos del autor.",
               note_kind="coral", foot=SINT)


def se386_sesion() -> Fig:
    rows = [
        ["Identificador secuencial en un espacio de 1 000 000 con 10 000 sesiones", "99 (se esperan 100)", "Se acierta una sesión ajena adivinando; el espacio efectivo es 1 de cada 100"],
        ["Semilla del generador = segundo del inicio de sesión", "3 601 de 7 201 candidatos", "El token de la víctima se recupera sabiendo la hora del inicio con ±1 hora"],
        ["128 bits del generador criptográfico del sistema (secrets)", "3,4 × 10^34 esperados", "Adivinar no es el camino; quedan el robo del token y la fijación de sesión"],
    ]
    return tab("Cuántos intentos necesita alguien para quedarse con una sesión según cómo se generó el identificador",
               "Tabla: un identificador secuencial se adivina en unos 99 intentos entre 10 000 sesiones activas; un generador sembrado con la hora del inicio de sesión se recupera probando 3 601 semillas de 7 201; un token de 128 bits del sistema exige del orden de 3,4 por 10 elevado a 34 intentos.",
               ["Cómo se generó el identificador", "Intentos hasta acertar", "Consecuencia"], rows, [380, 200, 340], row_h=68, size=12,
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
    rows = [
        ["Secuencial, sin comprobar el dueño", "20 000", "4 988"],
        ["Aleatorio (UUID), sin comprobar, adivinando", "1 000 000", "0"],
        ["Aleatorio, sin comprobar, con el 3 % de los identificadores filtrados", "150", "150"],
        ["Secuencial, comprobando el dueño", "20 000", "0"],
        ["Aleatorio, comprobando el dueño", "1 000 000", "0"],
    ]
    return tab("Lectura de entregas ajenas: identificadores adivinables frente a comprobar el dueño (5 000 entregas)",
               "Tabla: con identificadores secuenciales y sin comprobar el dueño, 20 000 peticiones leen 4 988 entregas ajenas; con identificadores aleatorios y sin comprobar, adivinar no lee ninguna pero 150 identificadores filtrados leen 150; comprobar el dueño las reduce a cero en ambos casos.",
               ["Combinación", "Peticiones", "Entregas ajenas leídas"], rows, [560, 160, 200], row_h=46, size=13,
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
    rows = [
        ["Concatenar el texto", "4", "9", "4"],
        ["Duplicar las comillas simples", "0", "9", "4"],
        ["Rechazar palabras (union, select, drop, delete)", "1", "6", "2"],
        ["Parámetro enlazado", "0", "0", "0 (pero no ordena)"],
        ["Lista blanca de columnas", "—", "—", "0"],
    ]
    return tab("Doce cargas por contexto contra SQLite real: cuántas alteran la consulta según la defensa",
               "Tabla: concatenar deja pasar 4 de 12 cargas en un valor de texto, 9 en un número y 4 en un identificador de ORDER BY; duplicar comillas cierra el texto y no el número; una lista de palabras prohibidas deja pasar 1, 6 y 2; el parámetro enlazado cierra texto y número; solo la lista blanca resuelve el identificador.",
               ["Defensa", "Valor entre comillas", "Número sin comillas", "Identificador (ORDER BY)"], rows, [400, 160, 160, 200], row_h=46, size=12,
               note="Duplicar comillas es la defensa correcta para un contexto y inútil en otro: el número no lleva comillas que cerrar. El parámetro enlazado separa dato de código, pero no puede enlazar el nombre de una columna: ORDER BY ? con «titulo DESC» no ordena. Las 36 cargas son del autor y la lista de palabras se escribió sin ajustarla a ellas.",
               note_kind="gold", foot="SQLite 3 del módulo estándar de CPython 3.12; cifras idénticas en Windows y Ubuntu (WSL2).")


def se388_contexto() -> Fig:
    rows = [
        ["Ninguna", "3", "1", "7", "4", "1"],
        ["html.escape sin comillas", "0", "1", "5", "2", "1"],
        ["html.escape con comillas", "0", "0", "4", "0", "1"],
        ["Codificación para cadena JavaScript", "0", "1", "4", "0", "1"],
        ["urllib.parse.quote total", "0", "0", "0", "0", "0"],
    ]
    return tab("Ocho cargas por contexto de salida: cuántas rompen el contexto según el codificador (modelo de reglas)",
               "Tabla: sin codificar, 3 de 8 cargas rompen un texto HTML, 1 un atributo con comillas, 7 un atributo sin comillas, 4 una cadena JavaScript y 1 una URL; html.escape con comillas cierra texto, atributo con comillas y cadena JavaScript pero deja 4 en el atributo sin comillas y 1 en la URL; quote las anula todas.",
               ["Codificador", "Texto HTML", "Atributo con comillas", "Atributo sin comillas", "Cadena JS", "URL en href"], rows, [330, 100, 140, 140, 100, 110], row_h=46, size=12,
               note="Ningún codificador sirve para todos los contextos: html.escape no mira las comillas simples sin el parámetro, deja pasar un atributo sin comillas y no toca el esquema de una URL. quote lo anula todo porque destruye el significado. Es un modelo de reglas escrito por el autor, no un navegador.",
               note_kind="coral", foot=SINT)


def se388_orden() -> Fig:
    rows = [
        ["Validar la forma recibida y decodificar después", "67", "48", "0"],
        ["Decodificar, normalizar y validar con lista negra", "50", "31", "0"],
        ["Decodificar, normalizar y validar con lista blanca", "5", "0", "5"],
    ]
    return tab("84 variantes de 12 cargas (porcentaje, doble porcentaje, ancho completo, NUL) y 10 nombres legítimos",
               "Tabla: validar antes de decodificar acepta 67 variantes y 48 son peligrosas después; decodificar y normalizar primero con lista negra acepta 50 y 31 son peligrosas; con lista blanca solo acepta 5, ninguna peligrosa, pero rechaza 5 de 10 nombres legítimos.",
               ["Orden y tipo de validación", "Variantes aceptadas", "Peligrosas tras aceptar", "Legítimos rechazados de 10"], rows, [450, 150, 170, 150], row_h=52, size=12,
               note="Cambiar el orden reduce el daño (de 48 a 31) y la lista negra sigue incompleta. La lista blanca elimina lo peligroso y cuesta falsos rechazos: la regla ASCII estricta rechaza «María_López.pdf» y «informe final.pdf». Ese costo es una decisión de producto, no un error de la lista.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-389
def se389_nonce() -> Fig:
    rows = [
        ["Nonce fijo para todos los mensajes", "100,0 %", "200 de 200"],
        ["Nonce aleatorio de 96 bits distinto en cada mensaje", "0,4 %", "0 de 200"],
    ]
    return tab("Cifrado de flujo de juguete (HMAC-SHA256 en modo contador) con y sin nonce repetido, 200 pares de mensajes",
               "Tabla: si dos mensajes se cifran con la misma clave y el mismo nonce, quien conoce uno recupera el 100 por ciento del otro sin la clave y la plantilla común acierta 200 de 200 veces; con nonce distinto se acierta el 0,4 por ciento, lo que da el azar.",
               ["Uso del nonce", "Bytes recuperados sin la clave", "Acierto de la plantilla común"], rows, [480, 230, 210], row_h=52, size=13,
               note="El XOR de dos textos cifrados con el mismo flujo es el XOR de los textos en claro; con uno conocido o una plantilla («Nota final: …») se lee el otro. Es una construcción didáctica: en producción se usa AEAD de una biblioteca revisada y el nonce nunca lo decide el llamador.",
               note_kind="coral", foot=SINT)


def se389_comparacion() -> Fig:
    rows = [
        ["Comparación que termina en el primer byte distinto", "2 002", "Etiqueta de 8 bytes recuperada byte a byte"],
        ["Comparación de tiempo constante", "—", "La señal toma 1 valor: no hay nada que medir"],
        ["Fuerza bruta sin señal", "9,2 × 10^18 esperados", "2^63 pruebas medias para 64 bits"],
    ]
    return tab("Consultas para falsificar una etiqueta de autenticación de 8 bytes según cómo se compara",
               "Tabla: si la comparación termina en el primer byte distinto y el atacante ve cuántos bytes coincidieron, recupera la etiqueta de 8 bytes en 2 002 consultas; con una comparación de tiempo constante la señal es constante; sin señal la fuerza bruta esperada es de 9,2 por 10 elevado a 18 pruebas.",
               ["Comparación", "Consultas", "Efecto"], rows, [420, 200, 300], row_h=58, size=12,
               note="Pasar de 9,2 × 10^18 a 2 002 es el valor de un oráculo de pasos. Aquí la señal es un contador perfecto; por la red real el ruido la degrada y por eso existen límites prácticos (Crosby et al. los miden), pero un atacante con muchas repeticiones los reduce. hmac.compare_digest elimina la señal en vez de confiar en el ruido.",
               note_kind="gold", foot=SINT)


def se389_colision() -> Fig:
    rows = [
        ["500", "0,9 %", "0,7 %"],
        ["1 000", "2,9 %", "2,9 %"],
        ["2 000", "12,1 %", "11,2 %"],
        ["4 000", "39,5 %", "37,9 %"],
        ["8 000", "84,8 %", "85,1 %"],
    ]
    return tab("Colisión de nonces aleatorios de 24 bits (1 500 repeticiones por fila) frente a 1 − exp(−n²/2^25)",
               "Tabla: con nonces de 24 bits la probabilidad de repetir alguno crece de 0,9 por ciento con 500 mensajes a 84,8 por ciento con 8 000, y sigue la fórmula del cumpleaños, que da 0,7 y 85,1; con 96 bits el mismo riesgo de uno en 2 elevado a 32 llega con unos 6 mil millones de mensajes.",
               ["Mensajes con la misma clave (n)", "Colisión observada", "Fórmula del cumpleaños"], rows, [380, 270, 270], row_h=44, size=13,
               note="Con 96 bits, una probabilidad de colisión de 2^-32 llega con unos 6,07 × 10^9 mensajes por clave; NIST SP 800-38D limita las invocaciones con IV aleatorio de 96 bits a 2^32 por clave. Envolver un millón de claves de datos con una clave maestra mueve 48 MB; recifrar 2 TB de datos para rotar sin sobre-cifrado es unas 40 000 veces más.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-390
def se390_escaner() -> Fig:
    rows = [
        ["Solo patrones de proveedor", "40", "24", "62,5 %", "66,7 %"],
        ["Solo palabra clave (password=, secret=)", "38", "51", "42,7 %", "63,3 %"],
        ["Solo entropía de las cadenas largas", "45", "21", "68,2 %", "75,0 %"],
        ["Patrones, y palabra clave con entropía", "60", "24", "71,4 %", "100,0 %"],
    ]
    return tab("Escáner de secretos de juguete sobre 500 líneas con 60 secretos plantados y 140 señuelos",
               "Tabla: ningún escáner simple encuentra los 60 secretos plantados sin falsas alarmas; los patrones de proveedor detectan 40 con 24 falsas alarmas, la palabra clave 38 con 51, la entropía 45 con 21, y la combinación de patrones y palabra clave con entropía detecta 60 con 24 falsas alarmas.",
               ["Estrategia", "Detectados de 60", "Falsas alarmas", "Precisión", "Exhaustividad"], rows, [400, 150, 140, 110, 120], row_h=46, size=12,
               note="La combinación llega al 100 % de exhaustividad porque se escribió conociendo los formatos plantados: es una frontera, no una tasa de detección. Las 24 falsas alarmas son ejemplos de documentación con forma de secreto. Todas las cadenas se generan al ejecutar; ninguna es una credencial real.",
               note_kind="gold", foot=SINT)


def se390_rotacion() -> Fig:
    rows = [
        ["Corte: el verificador solo acepta la nueva desde el segundo 0", "17 262 de 60 000 (28,77 %)", "0"],
        ["Doble validez con cierre fijo a los 360 s", "956 de 60 000 (1,59 %)", "360"],
        ["Doble validez; se cierra cuando ninguna instancia usa la vieja", "0 de 60 000 (0 %)", "538"],
    ]
    return tab("Rotar una clave entre 20 instancias (100 solicitudes por segundo, 600 s, 10 semillas)",
               "Tabla: aceptar solo la clave nueva desde el inicio falla el 28,77 por ciento de las solicitudes; aceptar ambas y cerrar a los 360 segundos falla el 1,59 por ciento cuando una instancia no recargó; cerrar solo cuando ninguna instancia usa la vieja no falla ninguna y mantiene la vieja aceptada 538 segundos de media.",
               ["Estrategia de rotación", "Solicitudes fallidas", "Segundos con la clave vieja aceptada"], rows, [440, 270, 210], row_h=58, size=12,
               note="Rotar sin caída cuesta una ventana en que dos secretos valen. En 8 de las 10 semillas una instancia no recarga: el cierre fijo la deja fuera y el cierre condicionado la espera, es decir, una rotación incompleta es visible en vez de silenciosa. Los tiempos de recarga (0 a 300 s) son un supuesto del autor.",
               note_kind="teal", foot=SINT)


def se390_radio() -> Fig:
    rows = [
        ["Una credencial válida en todos los ambientes", "90", "30"],
        ["Una credencial por ambiente", "30", "10"],
        ["Una credencial por servicio y ambiente", "6", "1,9"],
    ]
    return tab("Radio de una credencial filtrada: 3 ambientes × 5 servicios × 6 recursos (3 000 fugas al azar)",
               "Tabla: si la credencial filtrada vale en todos los ambientes alcanza 90 recursos de 90 y 30 de los 30 de producción; con una credencial por ambiente alcanza 30 y 10 de producción de media; con una por servicio y ambiente alcanza 6 y 1,9 de producción de media.",
               ["Esquema de credenciales", "Recursos alcanzados de 90", "De producción (de 30)"], rows, [480, 230, 210], row_h=46, size=13,
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
