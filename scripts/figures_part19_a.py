"""Figures for SE-229 to SE-234 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 / Node 24 and Ubuntu CPython 3.12.3 / Node 20 unless a time is shown)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2), salvo los tiempos indicados."
MODELO = "Modelo con supuestos del autor, semilla fija; no es una medición de un navegador ni de usuarios reales."


# ---------------------------------------------------------------- SE-229
def se229_linter() -> Fig:
    rows = [
        ["Quitar el alt de una imagen", "18", "18", "0"],
        ["Alt que es un nombre de archivo", "25", "25", "0"],
        ["Alt engañoso (describe otra cosa)", "20", "0", "0"],
        ["Quitar la etiqueta de un campo", "25", "25", "0"],
        ["Etiqueta con for apuntando a otro id", "23", "23", "0"],
        ["div con onclick en lugar de button", "23", "23", "0"],
        ["Saltar un nivel de encabezado", "20", "20", "0"],
        ["Quitar el landmark main", "20", "20", "0"],
        ["Cambiar nav por div", "17", "17", "0"],
        ["Enlace cuyo único contenido es un icono", "15", "15", "0"],
        ["Quitar el atributo lang", "14", "14", "0"],
    ]
    return tab("Linter semántico frente a validar solo que el HTML esté bien formado",
               "Tabla de 220 mutaciones de una página semántica en once tipos: un linter con ocho reglas detecta 200 y no detecta las 20 con alt engañoso, mientras que comprobar solo que las etiquetas estén balanceadas no detecta ninguna.",
               ["Mutación aplicada a la página base", "Casos", "Linter", "Solo balance de etiquetas"], rows, [430, 90, 110, 230], row_h=40, size=12,
               note="200 de 220 mutaciones detectadas por reglas; 0 por el balance de etiquetas. Las 20 sin detectar son textos alternativos que cambian de significado pero siguen siendo texto: solo una persona que mira la imagen lo nota.",
               note_kind="gold", foot=SINT)


def se229_contraste() -> Fig:
    items = [
        ("Pares de colores al azar con 3:1 o más (5000)", 26.1, "gold", "26,1 %"),
        ("Pares al azar con 4,5:1 o más (5000)", 11.2, "coral", "11,2 %"),
        ("Pares al azar con 7:1 o más (5000)", 2.9, "coral", "2,9 %"),
        ("Grises sobre blanco con 4,5:1 o más (256)", 46.5, "teal", "46,5 %"),
    ]
    return bars("Proporción de combinaciones de color que cumple cada umbral de contraste WCAG",
                "Barras: de 5000 pares de colores al azar solo 26,1 por ciento llega a 3 a 1, 11,2 por ciento a 4,5 a 1 y 2,9 por ciento a 7 a 1; de 256 grises sobre blanco pasa 46,5 por ciento, con el límite en el gris 767676 que da 4,54 a 1.",
                items, 1.55, "El umbral de 4,5:1 no es una cuestión de gusto: #767676 sobre blanco da 4,54 y #777777 da 4,48. Rojo puro sobre blanco da 4,0 y azul puro 8,59: el tono no basta para predecir el contraste, la luminancia sí.",
                label_w=420, width=1060, note_kind="gold", foot=SINT)


def se229_especificidad() -> Fig:
    rows = [
        ["50", "4 clases", "0", "1 clase"],
        ["200", "7 clases", "18", "1 clase"],
        ["800", "18 clases", "315", "1 clase"],
    ]
    return tab("Guerra de especificidad: subir el selector frente a ordenar con capas",
               "Tabla: con 50, 200 y 800 peticiones de sobrescribir estilos sobre 40 elementos, escalar la especificidad llega a selectores de 4, 7 y 18 clases y a 0, 18 y 315 reglas que superan las cuatro clases, mientras que ordenar con capas mantiene una clase.",
               ["Peticiones de cambio", "Selector más largo al escalar", "Reglas que superan 4 clases", "Selector más largo con capas"], rows, [200, 280, 280, 260], row_h=48, size=13,
               note="La calculadora de especificidad usada acertó los 11 ejemplos de la especificación de Selectores (incluidos :where, que suma 0, y :is, que suma su argumento más específico). La simulación supone que la mitad de las nuevas reglas llegan antes que la que deben vencer; el valor exacto depende de ese supuesto.",
               note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-230
def se230_bucle() -> Fig:
    items = [
        ("Modelo de dos colas, Node 24 (Windows)", 300, "teal", "300 de 300"),
        ("Modelo de dos colas, Node 20 (Ubuntu)", 300, "teal", "300 de 300"),
        ("Modelo de una sola cola FIFO", 221, "coral", "221 de 300"),
    ]
    return bars("Programas cuyo orden de salida predice cada modelo del bucle de eventos",
                "Barras: de 300 programas generados con semilla fija con microtareas y temporizadores anidados, el modelo de dos colas acierta el orden de salida de los 300 en Node 24 y Node 20, y un modelo de una sola cola acierta 221.",
                items, 1.7, "Las microtareas se vacían por completo antes de la siguiente tarea. Una cadena recursiva de 200 000 microtareas se ejecutó entera antes de un temporizador de 0 ms: las microtareas pueden dejar sin turno a las tareas.",
                label_w=380, width=1000, note_kind="teal", foot="Node 24.11 en Windows y Node 20.20 en Ubuntu (WSL2); el motor es V8, no un navegador.")


def se230_delegacion() -> Fig:
    rows = [
        ["Un listener por fila, registrado solo en la primera página", "200", "200 de 1000"],
        ["Un listener por fila, registrado en cada página", "1000", "1000 de 1000"],
        ["Delegado con closest, clic en el botón o en su icono", "1", "1000 de 1000"],
        ["Delegado que compara target directo, clic en el icono", "1", "0 de 1000"],
        ["Delegado con closest, 5 % de filas que detienen la propagación", "1", "943 de 1000"],
        ["Un listener por fila, 5 % que detienen la propagación", "1000", "1000 de 1000"],
    ]
    return tab("Delegación de eventos frente a un listener por fila en un modelo mínimo de DOM",
               "Tabla de seis estrategias para atender el clic de borrar en 1000 filas cargadas en cinco páginas: el listener por fila solo en la primera página atiende 200, el delegado con closest atiende las 1000 con un listener, y falla cuando se compara el target o cuando una fila detiene la propagación.",
               ["Estrategia", "Listeners", "Filas atendidas"], rows, [570, 130, 220], row_h=48, size=12,
               note="El modelo implementa captura, destino y burbuja con stopPropagation, pero no el comportamiento de un navegador real (listeners de captura en el destino, eventos pasivos, shadow DOM). Muestra el mecanismo, no mide memoria.",
               note_kind="gold", foot=SINT)


def se230_ritmo() -> Fig:
    items = [
        ("Sin control (cada evento)", 1000, "coral", "1000"),
        ("Throttle de 100 ms", 638, "gold", "638"),
        ("Debounce de 100 ms", 453, "gold", "453"),
        ("Throttle de 300 ms", 300, "gold", "300"),
        ("Debounce de 300 ms", 93, "teal", "93"),
        ("Throttle de 1000 ms", 134, "gold", "134"),
        ("Debounce de 1000 ms", 45, "teal", "45"),
    ]
    return bars("Llamadas que producen 1000 pulsaciones (171,6 s) según la técnica y el intervalo",
                "Barras: 1000 pulsaciones sintéticas se convierten en 638, 300 y 134 llamadas con throttle de 100, 300 y 1000 milisegundos y en 453, 93 y 45 con debounce; en 66 de 92 pausas el throttle de 300 ms no atiende el último evento.",
                items, 0.57, "Debounce responde después de la pausa y atiende el último evento; throttle responde durante la ráfaga pero en 66 de las 92 pausas de al menos 300 ms dejó sin atender el último evento. Elegir entre ambos es elegir qué error se tolera.",
                label_w=300, width=980, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-231
def se231_modelo() -> Fig:
    rows = [
        ["Fibra (RTT 20 ms, 50 Mbit/s, CPU ×1)", "91 ms", "26 ms", "11 ms"],
        ["Móvil 4G (RTT 80 ms, 8 Mbit/s, CPU ×4)", "378 ms", "92 ms", "47 ms"],
        ["Móvil lento (RTT 300 ms, 1 Mbit/s, CPU ×6)", "1389 ms", "365 ms", "210 ms"],
    ]
    return tab("Tiempo hasta el primer contenido útil: cliente, servidor y estático (modelo con bytes reales)",
               "Tabla: con 500 filas, un render en el cliente con tres peticiones en cadena tarda 91, 378 y 1389 milisegundos en el modelo, el render en servidor 26, 92 y 365 y el HTML estático en caché 11, 47 y 210, en tres perfiles de red y dispositivo.",
               ["Perfil supuesto", "Render en cliente", "Render en servidor", "HTML estático"], rows, [420, 170, 180, 160], row_h=48, size=13,
               note="Bytes medidos con gzip nivel 6: HTML renderizado 56 489 (7 486 comprimidos); paquete JS sintético 147 255 (37 559); JSON 35 434 (5 612). Las latencias, el factor de CPU y 5 ms de render en servidor son supuestos del autor: se lee la forma de la diferencia, no las cifras.",
               note_kind="gold", foot=MODELO)


def se231_hidratacion() -> Fig:
    items = [
        ("Fecha y hora, cliente en UTC−3 (2000 marcas)", 2000, "coral", "2000"),
        ("Fecha y hora, cliente en UTC+9", 2000, "coral", "2000"),
        ("Solo el día, cliente en UTC+9", 742, "gold", "742"),
        ("Solo el día, cliente en UTC−3", 239, "gold", "239"),
        ("Fecha y hora, cliente en la misma zona", 0, "teal", "0"),
        ("Valor aleatorio generado en cada render", 2000, "coral", "2000"),
    ]
    return bars("Textos del servidor que difieren de lo que calcularía el cliente al hidratar",
                "Barras: de 2000 marcas de tiempo, formatear fecha y hora en una zona distinta a la del servidor da textos distintos en las 2000, formatear solo el día en 742 con UTC más 9 y 239 con UTC menos 3, y un valor aleatorio difiere en las 2000 hidrataciones.",
                items, 0.27, "Todo valor que dependa de la zona horaria, la configuración regional, la hora actual o un azar sin semilla es una fuente de desajuste entre el HTML del servidor y el árbol del cliente. Se evita pasando el valor desde el servidor o renderizándolo solo en el cliente.",
                label_w=420, width=1080, note_kind="coral", foot=SINT)


def se231_isr() -> Fig:
    rows = [
        ["6 minutos", "0,7 %", "0,03 h"],
        ["1 hora", "8,3 %", "0,34 h"],
        ["6 horas", "39,2 %", "2,15 h"],
        ["24 horas", "76,9 %", "9,88 h"],
    ]
    return tab("Regeneración por caducidad: cuántas visitas ven una página desactualizada",
               "Tabla: con una página que cambia 0,2 veces por hora y 30 visitas por hora, una caducidad de 6 minutos deja 0,7 por ciento de las visitas con contenido viejo, 1 hora 8,3, 6 horas 39,2 y 24 horas 76,9, con edades medias de 0,03 a 9,88 horas.",
               ["Caducidad antes de regenerar", "Visitas con contenido viejo", "Antigüedad media del cambio"], rows, [300, 300, 320], row_h=46, size=13,
               note="Simulación de 2000 h con cambios de Poisson (0,2 por hora) y visitas de Poisson (30 por hora); regenerar al pedir tras caducar. Regenerar más a menudo cuesta compilaciones: este experimento no mide ese coste, solo la obsolescencia.",
               note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-232
def se232_claves() -> Fig:
    rows = [
        ["Insertar al inicio", "1000 actualizar + 1 crear", "1 crear", "1000 / 0"],
        ["Borrar el primero", "999 actualizar + 1 borrar", "1 borrar", "999 / 0"],
        ["Añadir al final", "1 crear", "1 crear", "0 / 0"],
        ["Intercambiar dos", "2 actualizar", "2 mover", "2 / 0"],
        ["Invertir", "1000 actualizar", "999 mover", "1000 / 0"],
        ["Barajar", "1000 actualizar", "943 mover", "1000 / 0"],
    ]
    return tab("Reconciliar una lista de 1000 elementos: clave por posición frente a clave por identidad",
               "Tabla de seis cambios en una lista de 1000 elementos: la clave por posición actualiza hasta 1000 nodos y asocia mal el estado local de hasta 1000, mientras que la clave por identidad crea, borra o mueve solo lo necesario y no asocia mal ningún estado.",
               ["Cambio en la lista", "Clave = posición", "Clave = identidad", "Estado mal asociado (posición / identidad)"], rows, [210, 290, 190, 270], row_h=46, size=12,
               note="El estado local mal asociado es, por ejemplo, el texto escrito en un campo de la fila 3 que pasa a estar junto a otro elemento. Los movimientos de la clave por identidad usan la subsecuencia creciente más larga; los marcos reales emplean heurísticas parecidas pero no idénticas.",
               note_kind="gold", foot=SINT)


def se232_derivado() -> Fig:
    items = [
        ("Total derivado, olvido 0 %", 0, "teal", "0 %"),
        ("Total copiado, olvido 0,2 % por operación", 2.7, "gold", "2,7 %"),
        ("Total copiado, olvido 1 %", 13.5, "coral", "13,5 %"),
        ("Total copiado, olvido 5 %", 50.1, "coral", "50,1 %"),
    ]
    return bars("Secuencias de 30 operaciones que acaban con un total distinto de la suma real",
                "Barras: con un total guardado aparte que se olvida de actualizar en 0,2, 1 y 5 por ciento de las operaciones, 2,7, 13,5 y 50,1 por ciento de 3000 secuencias de 30 operaciones terminan con un total incoherente; si el total se deriva de los elementos no puede divergir.",
                items, 6.0, "El estado duplicado no falla siempre: falla cuando una rama de código lo olvida, y la primera incoherencia aparece en promedio hacia la operación 14 a 16. Derivar el valor elimina la posibilidad, a costa de recalcular o memorizar.",
                label_w=400, width=1000, note_kind="gold", foot=MODELO)


def se232_carreras() -> Fig:
    items = [
        ("Mostrar la última respuesta que llega (10 000 sesiones)", 34.67, "coral", "34,67 %"),
        ("Descartar respuestas más viejas que la ya mostrada", 0, "teal", "0 %"),
    ]
    return bars("Sesiones de búsqueda que terminan mostrando el resultado de una consulta antigua",
                "Barras: con seis consultas enviadas cada 120 milisegundos y latencias lognormales de mediana 200 milisegundos, mostrar la última respuesta recibida deja un resultado obsoleto en 34,67 por ciento de 10 000 sesiones, y descartar las respuestas más viejas que la ya mostrada en 0.",
                items, 11.0, "La causa es el orden de llegada, no el de envío. Además, 500 componentes que piden 20 recursos distintos hacen 500 peticiones sin deduplicar y 20 deduplicando. Descartar respuestas viejas no cancela la petición: sigue gastando red.",
                label_w=470, width=1060, note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-233
def se233_correo() -> Fig:
    rows = [
        ["Solo comprobar que hay una @", "30 de 30", "4 de 4", "1 de 30"],
        ["Texto antes y después de la @", "30 de 30", "4 de 4", "3 de 30"],
        ["Expresión simple con punto en el dominio", "30 de 30", "4 de 4", "13 de 30"],
        ["Expresión ASCII estricta", "16 de 30", "0 de 4", "22 de 30"],
        ["Expresión de la especificación HTML", "30 de 30", "0 de 4", "24 de 30"],
        ["Especificación HTML más reglas de puntos y longitudes", "30 de 30", "0 de 4", "30 de 30"],
    ]
    return tab("Seis validadores de correo frente a un corpus de 64 direcciones etiquetadas por el autor",
               "Tabla: ninguno de los seis validadores acierta a la vez las 30 direcciones ordinarias, las 4 internacionalizadas y las 30 inválidas; los laxos aceptan casi todo, el ASCII estricto rechaza 14 válidas y las 4 internacionalizadas y los basados en la especificación HTML rechazan las 4 internacionalizadas.",
               ["Validador", "Acepta ordinarias", "Acepta internacionalizadas", "Rechaza inválidas"], rows, [430, 150, 190, 170], row_h=46, size=12,
               note="Ningún validador puede saber si un buzón existe: solo un mensaje enviado y confirmado lo prueba. El corpus y sus etiquetas son del autor; con otro corpus las cifras cambian.",
               note_kind="gold", foot=SINT)


def se233_unicode() -> Fig:
    items = [
        ("Nombres distintos sin normalizar (5000 registros)", 38, "coral", "38"),
        ("Tras normalizar a NFC", 20, "gold", "20"),
        ("Tras NFC y plegado de mayúsculas", 10, "teal", "10"),
        ("Personas distintas reales de la muestra", 10, "grey", "10"),
    ]
    return bars("Nombres que cuenta un sistema para 10 personas, según cómo compare las cadenas",
                "Barras: 5000 registros de diez nombres con acentos, algunos en forma descompuesta y algunos en mayúsculas, se cuentan como 38 nombres distintos sin normalizar, 20 tras normalizar a NFC y 10 tras NFC y plegado de mayúsculas, que son las diez personas reales.",
                items, 12.0, "Jose con tilde compuesta mide 4 puntos de código y descompuesta 5; en UTF-8 son 5 y 6 bytes. Una familia con emoji mide 5 puntos de código, 8 unidades UTF-16 y 18 bytes: contar caracteres exige decidir qué unidad se cuenta.",
                label_w=440, width=1020, note_kind="gold", foot=SINT)


def se233_mientras_escribe() -> Fig:
    items = [
        ("Validar en cada pulsación (4073 pulsaciones)", 82.3, "coral", "82,3 %"),
        ("Validar al salir del campo", 0, "teal", "0 %"),
        ("Validar al enviar", 0, "teal", "0 %"),
    ]
    return bars("Pulsaciones en las que se muestra un error aunque el correo final sea válido",
                "Barras: al escribir 200 correos válidos letra a letra, validar en cada pulsación muestra un error en 82,3 por ciento de las 4073 pulsaciones y en los 200 correos al menos una vez; validar al salir del campo o al enviar no muestra ninguno mientras se escribe.",
                items, 5.8, "El error aparece porque el texto parcial todavía no es un correo, no porque la persona se haya equivocado. Validar al salir y volver a validar en cada pulsación solo cuando ya hay un error mostrado equilibra rapidez y ruido.",
                label_w=420, width=1000, note_kind="gold", foot=MODELO)


# ---------------------------------------------------------------- SE-234
def se234_urls() -> Fig:
    items = [
        ("URLs distintas sin normalizar", 2400, "coral", "2400"),
        ("Tras normalizar sintaxis (RFC 3986)", 1600, "gold", "1600"),
        ("Tras ordenar parámetros y quitar fragmento y utm", 1000, "gold", "1000"),
        ("Tras política de barra final e index.html", 400, "teal", "400"),
        ("Recursos reales (200) y sus 200 variantes con filtro", 400, "grey", "400"),
    ]
    return bars("URLs distintas para 200 recursos con 12 variantes cada uno, según el nivel de normalización",
                "Barras: 2400 URLs que escriben 200 recursos de doce maneras se reducen a 1600 al normalizar la sintaxis, a 1000 al ordenar parámetros y quitar fragmento y marcas utm y a 400 con una política de barra final e index punto html; los 400 son 200 recursos con y sin filtro.",
                items, 0.2, "Cada nivel es una decisión: las mayúsculas del host se pueden igualar, las de la ruta no (un servidor puede distinguirlas) y quitar utm cambia lo que se mide. La normalización de sintaxis no sabe qué dos rutas devuelven lo mismo.",
                label_w=470, width=1060, note_kind="gold", foot=SINT)


def se234_rutas() -> Fig:
    rows = [
        ["Búsqueda lineal en 500 rutas (20 000 consultas)", "288,2 comparaciones", "—"],
        ["Árbol de segmentos (mismas consultas)", "3,61 pasos", "—"],
        ["4 rutas /u/:id y /u/nuevo en orden arbitrario", "—", "6 de 24 órdenes resuelven bien"],
        ["Las mismas 4 rutas ordenadas por especificidad", "—", "correcto"],
    ]
    return tab("Resolver rutas: coste de buscar y ambigüedad según el orden de declaración",
               "Tabla: encontrar la ruta de una consulta cuesta en promedio 288,2 comparaciones recorriendo 500 rutas en lista y 3,61 pasos con un árbol de segmentos; con cuatro rutas, solo 6 de las 24 órdenes de declaración resuelven bien tanto nuevo como el parámetro id, y ordenarlas por especificidad lo resuelve.",
               ["Situación", "Coste medio por consulta", "Orden de declaración"], rows, [470, 230, 240], row_h=50, size=12,
               note="El árbol y la lista devolvieron la misma ruta en las 2000 consultas comparadas. La ambigüedad no es un fallo de rendimiento sino de diseño: /u/nuevo coincide con /u/:id y gana la primera declarada.",
               note_kind="gold", foot=SINT)


def se234_estado() -> Fig:
    items = [
        ("Unir valores a mano, sin codificar", 1743, "coral", "1743"),
        ("urlencode y leer sin tipos (la página queda como texto)", 0, "coral", "0"),
        ("urlencode y leer con un esquema de tipos", 2000, "teal", "2000"),
        ("JSON en base64 con URL segura", 2000, "teal", "2000"),
    ]
    return bars("Estados de filtro recuperados exactamente tras ir a la URL y volver (2000 estados)",
                "Barras: de 2000 estados de filtro con texto, lista, booleano, número y nulo, unir valores a mano recupera 1743, urlencode leído sin tipos recupera 0 porque los números vuelven como texto, y urlencode con esquema y JSON en base64 recuperan los 2000.",
                items, 0.24, "El JSON en base64 recupera todo pero no se puede leer ni editar a mano y crece más rápido: con 100 etiquetas la URL mide 2299 caracteres con urlencode y 2020 con base64, ya cerca de los 2000 que algunos clientes y proxys recomiendan no superar.",
                label_w=500, width=1100, note_kind="gold", foot=SINT)


FIGURES = {
    "se-229-linter-semantico-frente-a-sintaxis.svg": se229_linter,
    "se-229-contraste-wcag-en-5000-pares.svg": se229_contraste,
    "se-229-guerra-de-especificidad.svg": se229_especificidad,
    "se-230-orden-del-bucle-de-eventos.svg": se230_bucle,
    "se-230-delegacion-de-eventos.svg": se230_delegacion,
    "se-230-debounce-y-throttle.svg": se230_ritmo,
    "se-231-primer-contenido-segun-estrategia.svg": se231_modelo,
    "se-231-desajuste-de-hidratacion.svg": se231_hidratacion,
    "se-231-contenido-viejo-segun-caducidad.svg": se231_isr,
    "se-232-reconciliar-listas-con-clave.svg": se232_claves,
    "se-232-estado-duplicado-frente-a-derivado.svg": se232_derivado,
    "se-232-respuestas-fuera-de-orden.svg": se232_carreras,
    "se-233-validadores-de-correo.svg": se233_correo,
    "se-233-nombres-y-normalizacion-unicode.svg": se233_unicode,
    "se-233-errores-mientras-se-escribe.svg": se233_mientras_escribe,
    "se-234-variantes-de-una-misma-url.svg": se234_urls,
    "se-234-resolver-rutas-y-ambiguedad.svg": se234_rutas,
    "se-234-estado-en-la-url.svg": se234_estado,
}
