"""Figures for SE-229 to SE-234 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 / Node 24 and Ubuntu CPython 3.12.3 / Node 20 unless a time is shown)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars
from figures_part07_a import bars

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2), salvo los tiempos indicados."
MODELO = "Modelo con supuestos del autor, semilla fija; no es una medición de un navegador ni de usuarios reales."


# ---------------------------------------------------------------- SE-229
def se229_linter() -> Fig:
    return stacked_bars(
        "Linter semántico frente a validar solo que el HTML esté bien formado",
        "Barras apiladas horizontales con las 220 mutaciones de una página semántica en once tipos: un linter con ocho reglas detecta 200 y no detecta las 20 con alt engañoso; comprobar solo el balance de etiquetas no detecta ninguna.",
        ["Quitar el alt de una imagen", "Alt que es un nombre de archivo", "Alt engañoso (describe otra cosa)", "Quitar la etiqueta de un campo", "Etiqueta con for a otro id", "div con onclick en lugar de button",
         "Saltar un nivel de encabezado", "Quitar el landmark main", "Cambiar nav por div", "Enlace cuyo único contenido es un icono", "Quitar el atributo lang"],
        [("Detectadas por el linter", [18, 25, 0, 25, 23, 23, 20, 20, 17, 15, 14], "teal"), ("No detectadas", [0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0], "coral")],
        unit="Mutaciones aplicadas", horizontal=True, decimals=0, label_w=290,
        note="200 de 220 mutaciones detectadas por reglas; 0 por el balance de etiquetas, que no distingue ninguna de las once. Las 20 sin detectar son textos alternativos que cambian de significado pero siguen siendo texto: solo una persona que mira la imagen lo nota.",
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
    return grouped_bars(
        "Guerra de especificidad: subir el selector frente a ordenar con capas",
        "Barras agrupadas con el selector más largo al sobrescribir estilos: escalar la especificidad llega a 4, 7 y 18 clases con 50, 200 y 800 peticiones de cambio, y a 0, 18 y 315 reglas que superan las cuatro clases, mientras que ordenar con capas mantiene una clase.",
        ["50 peticiones", "200 peticiones", "800 peticiones"],
        [("Selector más largo al escalar (clases)", [4, 7, 18], "coral"), ("Selector más largo con capas (clases)", [1, 1, 1], "teal")],
        unit="Clases en el selector más largo", decimals=0, plot_h=260,
        note="Reglas que superan 4 clases al escalar: 0, 18 y 315. La calculadora de especificidad usada acertó los 11 ejemplos de la especificación de Selectores (incluidos :where, que suma 0, y :is, que suma su argumento más específico). La simulación supone que la mitad de las nuevas reglas llegan antes que la que deben vencer; el valor exacto depende de ese supuesto.",
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
    return grouped_bars(
        "Delegación de eventos frente a un listener por fila en un modelo mínimo de DOM",
        "Barras horizontales agrupadas con las filas atendidas de 1000 y los listeners usados por seis estrategias: el listener por fila solo en la primera página atiende 200 con 200 listeners, el delegado con closest atiende las 1000 con un listener y falla con 0 cuando compara el target o con 943 si una de cada veinte filas detiene la propagación.",
        ["Un listener por fila, solo en la primera página", "Un listener por fila, en cada página", "Delegado con closest (botón o icono)", "Delegado que compara el target directo (clic en el icono)", "Delegado con closest, 5 % de filas detienen la propagación", "Un listener por fila, 5 % detienen la propagación"],
        [("Listeners", [200, 1000, 1, 1, 1, 1000], "grey"), ("Filas atendidas de 1000", [200, 1000, 1000, 0, 943, 1000], "teal")],
        unit="Cantidad", horizontal=True, decimals=0, label_w=330,
        note="El delegado con closest atiende las 1000 filas con un solo listener; falla si compara el target (0 de 1000) o si una fila detiene la propagación (943 de 1000). El modelo implementa captura, destino y burbuja con stopPropagation, pero no el comportamiento de un navegador real (listeners de captura en el destino, eventos pasivos, shadow DOM). Muestra el mecanismo, no mide memoria.",
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
    return grouped_bars(
        "Tiempo hasta el primer contenido útil: cliente, servidor y estático (modelo con bytes reales)",
        "Barras agrupadas en escala logarítmica con el tiempo hasta el primer contenido útil con 500 filas: render en el cliente 91, 378 y 1389 milisegundos, render en servidor 26, 92 y 365 y HTML estático en caché 11, 47 y 210, en fibra, móvil 4G y móvil lento.",
        ["Fibra (RTT 20 ms, CPU ×1)", "Móvil 4G (RTT 80 ms, CPU ×4)", "Móvil lento (RTT 300 ms, CPU ×6)"],
        [("Render en cliente", [91, 378, 1389], "coral"), ("Render en servidor", [26, 92, 365], "gold"), ("HTML estático", [11, 47, 210], "teal")],
        unit="Milisegundos", log=True, decimals=0, plot_h=280,
        note="Anchos de banda supuestos: 50, 8 y 1 Mbit/s. Bytes medidos con gzip nivel 6: HTML renderizado 56 489 (7 486 comprimidos); paquete JS sintético 147 255 (37 559); JSON 35 434 (5 612). Las latencias, el factor de CPU y 5 ms de render en servidor son supuestos del autor: se lee la forma de la diferencia, no las cifras.",
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
    return line_chart(
        "Regeneración por caducidad: cuántas visitas ven una página desactualizada",
        "Línea con el porcentaje de visitas que ven contenido viejo según la caducidad antes de regenerar, con una página que cambia 0,2 veces por hora y 30 visitas por hora: 0,7 con 6 minutos, 8,3 con 1 hora, 39,2 con 6 horas y 76,9 con 24 horas.",
        [("Visitas con contenido viejo", [(0.1, 0.7, "0,7 %", "t"), (1, 8.3, "8,3 %", "t"), (6, 39.2, "39,2 %", "t"), (24, 76.9, "76,9 %", "t")], "coral")],
        x_label="Caducidad antes de regenerar (horas)", y_label="Visitas con contenido viejo (%)", log_x=True,
        x_ticks=[(0.1, "6 min"), (1, "1 h"), (6, "6 h"), (24, "24 h")], y_ticks=[0, 20, 40, 60, 80, 100], decimals=1, plot_h=280,
        note="Antigüedad media del cambio que ve la visita: 0,03, 0,34, 2,15 y 9,88 horas. Simulación de 2000 h con cambios de Poisson (0,2 por hora) y visitas de Poisson (30 por hora); regenerar al pedir tras caducar. Regenerar más a menudo cuesta compilaciones: este experimento no mide ese coste, solo la obsolescencia.",
        note_kind="gold", foot=MODELO)

# ---------------------------------------------------------------- SE-232
def se232_claves() -> Fig:
    return grouped_bars(
        "Reconciliar una lista de 1000 elementos: clave por posición frente a clave por identidad",
        "Barras horizontales con los elementos de estado local mal asociado en seis cambios de una lista de 1000: con clave por posición 1000 al insertar al inicio, 999 al borrar el primero, 0 al añadir al final, 2 al intercambiar, 1000 al invertir y 1000 al barajar; con clave por identidad ninguno.",
        ["Insertar al inicio", "Borrar el primero", "Añadir al final", "Intercambiar dos", "Invertir", "Barajar"],
        [("Clave = posición", [1000, 999, 0, 2, 1000, 1000], "coral"), ("Clave = identidad", [0, 0, 0, 0, 0, 0], "teal")],
        unit="Elementos con estado local mal asociado", horizontal=True, decimals=0, label_w=160,
        note="Operaciones por cambio: la posición actualiza hasta 1000 nodos (insertar al inicio: 1000 actualizar + 1 crear); la identidad crea, borra o mueve solo lo necesario (1 crear, 1 borrar, 0, 2 mover, 999 mover, 943 mover). El estado local mal asociado es, por ejemplo, el texto escrito en un campo de la fila 3 que pasa a estar junto a otro elemento. Los marcos reales emplean heurísticas parecidas pero no idénticas.",
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
    return grouped_bars(
        "Seis validadores de correo frente a un corpus de 64 direcciones etiquetadas por el autor",
        "Barras horizontales con las direcciones que acierta cada validador: ordinarias aceptadas de 30, internacionalizadas aceptadas de 4 e inválidas rechazadas de 30; ninguno acierta los tres grupos, los laxos aceptan casi todo y el ASCII estricto rechaza 14 válidas y las 4 internacionalizadas.",
        ["Solo comprobar que hay una @", "Texto antes y después de la @", "Expresión simple con punto en el dominio", "Expresión ASCII estricta", "Expresión de la especificación HTML", "Especificación HTML más reglas de puntos y longitudes"],
        [("Acepta ordinarias (de 30)", [30, 30, 30, 16, 30, 30], "teal"), ("Acepta internacionalizadas (de 4)", [4, 4, 4, 0, 0, 0], "navy"), ("Rechaza inválidas (de 30)", [1, 3, 13, 22, 24, 30], "coral")],
        unit="Direcciones", horizontal=True, decimals=0, label_w=300,
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
    return grouped_bars(
        "Resolver rutas: coste de buscar y ambigüedad según el orden de declaración",
        "Barras horizontales con el coste medio de resolver una consulta entre 500 rutas: 288,2 comparaciones con búsqueda lineal y 3,61 pasos con un árbol de segmentos; con cuatro rutas, solo 6 de las 24 órdenes de declaración resuelven bien nuevo y el parámetro id.",
        ["Búsqueda lineal en 500 rutas (20 000 consultas)", "Árbol de segmentos (mismas consultas)"],
        [("Coste medio por consulta", [288.2, 3.61], "navy")],
        unit="Comparaciones o pasos por consulta", horizontal=True, decimals=2, label_w=300,
        note="Con cuatro rutas /u/:id y /u/nuevo, solo 6 de las 24 órdenes de declaración resuelven bien; ordenadas por especificidad, el resultado es correcto. El árbol y la lista devolvieron la misma ruta en las 2000 consultas comparadas. La ambigüedad no es un fallo de rendimiento sino de diseño: /u/nuevo coincide con /u/:id y gana la primera declarada.",
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
