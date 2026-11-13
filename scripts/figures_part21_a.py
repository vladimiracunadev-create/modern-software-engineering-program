"""Figures for SE-253 to SE-258 (synthetic models with fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time is shown)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Modelo sintético con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2), salvo los tiempos indicados."
TIEMPO = "Tiempos medidos en un equipo (Windows 11, CPython 3.12.9); en Ubuntu (WSL2) la forma se repite con otras cifras."


# ---------------------------------------------------------------- SE-253
def se253_ancho() -> Fig:
    rows = [
        ["320 px", "3 de 12 sin desplazar; el resto exige desplazamiento horizontal", "12 de 12 en 6 filas"],
        ["390 px", "3 de 12 sin desplazar", "12 de 12 en 4 filas"],
        ["768 px", "7 de 12 sin desplazar", "12 de 12 en 2 filas"],
        ["1024 px", "10 de 12 sin desplazar", "12 de 12 en 2 filas"],
        ["1280 px", "12 de 12 en una fila", "12 de 12 en una fila"],
    ]
    return tab("Doce controles según el ancho de ventana: diseño fijo frente a diseño adaptable",
               "Tabla con cinco anchos de ventana de 320 a 1280 píxeles: un diseño de una sola fila de 1200 píxeles deja visibles 3, 3, 7, 10 y 12 de doce controles, y un diseño que se reparte en filas muestra los doce en 6, 4, 2, 2 y 1 filas.",
               ["Ancho", "Diseño fijo de una fila (100 px por control)", "Diseño adaptable (104 px por columna)"], rows, [110, 520, 360], row_h=46, size=12,
               note="El modelo cuenta solo geometría: no mide legibilidad, tamaño táctil ni orden de lectura. Reflujo no significa buen diseño, pero un diseño de escritorio fijo deja inalcanzables nueve de doce controles en una pantalla de 320 px.",
               note_kind="gold", foot=SINT)


def se253_instancias() -> Fig:
    items = [
        ("Dos instancias, sin coordinación", 127.65, "coral", "127,65 de 200 (110 a 151)"),
        ("Dos instancias con archivo de bloqueo", 200, "teal", "200 de 200"),
        ("Una sola instancia permitida", 200, "teal", "200 de 200"),
    ]
    return bars("Dos instancias de escritorio que leen, suman y escriben el mismo archivo",
                "Barras: dos instancias que hacen cada una 100 incrementos sobre un archivo compartido terminan con 127,65 de 200 en media de 1000 semillas, entre 110 y 151, y ninguna da 200; con bloqueo o con una sola instancia las 1000 dan exactamente 200.",
                items, 2.0, "Un modelo de escritorio permite abrir la aplicación dos veces, y entonces el archivo local deja de tener un solo escritor. Sin coordinación se pierden 72 de cada 200 actualizaciones en media; el bloqueo o la política de instancia única lo evitan a cambio de más reglas.",
                label_w=360, width=1040, note_kind="coral", foot=SINT)


def se253_arranques() -> Fig:
    items = [
        ("Escritorio sin recuperación de memoria", 0, "teal", "0 %"),
        ("Recuperación lenta (tau = 240 min)", 16.4, "gold", "16,4 %"),
        ("Recuperación moderada (tau = 60 min)", 38.3, "gold", "38,3 %"),
        ("Recuperación agresiva (tau = 15 min)", 66.5, "coral", "66,5 %"),
        ("Recuperación muy agresiva (tau = 5 min)", 84.6, "coral", "84,6 %"),
    ]
    return bars("Arranques en frío según la rapidez con que el sistema recupera la memoria",
                "Barras: con tiempos de ausencia sintéticos de mediana 20 minutos, el porcentaje de regresos que son arranque en frío es 0 si el sistema nunca recupera el proceso y 16,4, 38,3, 66,5 y 84,6 por ciento cuando la constante de recuperación baja de 240 a 5 minutos.",
                items, 6.0, "El porcentaje de regresos que parten de cero depende de una constante que el equipo no controla. El diseño que asume continuidad (proceso vivo) funciona en el primer caso y falla en los demás: la restauración del estado debe ser parte normal del arranque.",
                label_w=400, width=1080, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-254
def se254_ganchos() -> Fig:
    items = [
        ("Guardar solo al cerrar", 109.27, "coral", "109,27 (72,8 %)"),
        ("Guardar cada 10 ediciones", 10.12, "gold", "10,12 (6,8 %)"),
        ("Guardar al pasar a segundo plano", 8.03, "gold", "8,03 (5,4 %)"),
        ("Cada 10 ediciones y al pasar a segundo plano", 1.69, "teal", "1,69 (1,1 %)"),
        ("Guardar en cada edición", 0, "teal", "0"),
    ]
    return bars("Ediciones perdidas por sesión según cuándo se guarda el borrador",
                "Barras: en 10 000 sesiones sintéticas de seis episodios, guardar solo al cerrar pierde 109,27 ediciones por sesión, guardar cada diez 10,12, guardar al pasar a segundo plano 8,03, combinar ambas 1,69 y guardar en cada edición ninguna.",
                items, 5.0, "Con 35 % de episodios que terminan sin aviso, 10 % de ganchos que no alcanzan a escribir y 3 % de cierres inesperados, ninguna política barata llega a cero. Las dos protecciones se complementan: una cubre el aviso, la otra el cierre sin aviso.",
                label_w=400, width=1080, note_kind="gold", foot=SINT)


def se254_migraciones() -> Fig:
    rows = [
        ["Estricta (rechaza otra versión)", "2000 de 2000", "2000 de 2000", "2000 de 2000"],
        ["Valores por defecto para campos nuevos", "0", "0", "2000 de 2000"],
        ["Migraciones paso a paso (v1→v2→v3→v4)", "0", "0", "0"],
    ]
    return tab("Restaurar un estado guardado por la versión 1 con la versión 2, 3 o 4",
               "Tabla de tres políticas de lectura: la estricta falla en las 2000 restauraciones con cada versión, los valores por defecto fallan solo cuando cambia la forma de un campo existente en la versión 4, y las migraciones encadenadas no fallan.",
               ["Política de lectura", "Versión 2", "Versión 3", "Versión 4 (cambia la forma del cursor)"], rows, [380, 170, 170, 290], row_h=50, size=12,
               kinds=["plain", "teal", "teal", "gold"],
               note="Los valores por defecto sirven mientras solo se añaden campos. Cuando un campo cambia de forma (un número pasa a ser un par línea y columna) hace falta una migración explícita y una prueba que restaure un estado guardado por cada versión anterior.",
               note_kind="gold", foot=SINT)


def se254_coste() -> Fig:
    items = [
        ("Estado de 1 KiB", 3.96, "teal", "3,96 ms"),
        ("Estado de 64 KiB", 6.12, "teal", "6,12 ms"),
        ("Estado de 1 MiB", 34.15, "gold", "34,15 ms"),
        ("Estado de 16 MiB", 401.99, "coral", "401,99 ms"),
    ]
    return bars("Coste de guardar el estado con archivo temporal, sincronización y reemplazo",
                "Barras: escribir un estado en JSON, vaciar el búfer, sincronizar el disco y reemplazar el archivo tarda 3,96 milisegundos con 1 KiB, 6,12 con 64 KiB, 34,15 con 1 MiB y 401,99 con 16 MiB en Windows; en Ubuntu fueron 3,78, 5,73, 17,91 y 228,74.",
                items, 1.4, "El tiempo crece con el tamaño del estado, y el plazo que concede el sistema para guardar al pasar a segundo plano no es un parámetro que el equipo pueda elegir. Un estado grande se guarda por partes, incrementalmente, o se reduce a lo que no puede reconstruirse.",
                label_w=260, width=940, note_kind="gold", foot=TIEMPO)


# ---------------------------------------------------------------- SE-255
def se255_pesos() -> Fig:
    items = [
        ("Nativo por plataforma", 37.9, "gold", "37,9 %"),
        ("Multiplataforma con interfaz propia", 27.4, "gold", "27,4 %"),
        ("Híbrido (web en contenedor)", 23.9, "gold", "23,9 %"),
        ("Web instalable", 10.8, "gold", "10,8 %"),
    ]
    return bars("Qué opción gana cuando los pesos de los criterios se sortean 10 000 veces",
                "Barras: con cuatro opciones puntuadas de 1 a 5 en siete criterios y pesos aleatorios, gana la opción nativa en 37,9 por ciento de los sorteos, la multiplataforma con interfaz propia en 27,4, la híbrida en 23,9 y la web instalable en 10,8.",
                items, 9.0, "Con pesos iguales gana la multiplataforma por 3,86 frente a 3,71 de otras dos, una diferencia que desaparece si cada puntuación cambia en uno: el ganador solo se mantiene en 59,1 % de 10 000 perturbaciones. La tabla de decisión ordena el debate; no lo cierra.",
                label_w=330, width=960, note_kind="gold", foot="Puntuaciones y pesos: supuestos del autor, no mediciones de productos; semilla fija, idénticos en Windows y Ubuntu.")


def se255_puente() -> Fig:
    items = [
        ("2000 llamadas directas", 0.117, "teal", "0,12 ms"),
        ("2000 mensajes, uno a uno por JSON", 23.82, "coral", "23,8 ms"),
        ("2000 mensajes en un solo lote por JSON", 4.31, "gold", "4,3 ms"),
    ]
    return bars("Coste de cruzar una frontera serializando: mensajes sueltos o en lote",
                "Barras: un proxy de la frontera entre capas que solo mide serialización con JSON tarda 0,12 milisegundos con llamadas directas, 23,8 con 2000 mensajes enviados de uno en uno y 4,3 en un lote, una razón entre 3 y 5,5 en cuatro ejecuciones.",
                items, 22.0, "Una frontera entre el código compartido y la capa nativa cuesta por cruce, no solo por byte: agrupar los mensajes redujo el tiempo entre 3 y 5,5 veces según la ejecución. Es un proxy, no un puente real: no se midió ningún marco concreto.",
                label_w=370, width=1040, note_kind="gold", foot=TIEMPO)


def se255_comunes() -> Fig:
    items = [
        ("2 plataformas", 12.66, "teal", "12,66 de 20"),
        ("3 plataformas", 10.19, "teal", "10,19 de 20"),
        ("4 plataformas", 8.15, "gold", "8,15 de 20"),
        ("6 plataformas", 5.27, "coral", "5,27 de 20"),
    ]
    return bars("Capacidades que ofrecen todas las plataformas cuando cada una ofrece el 80 %",
                "Barras: si cada plataforma ofrece al azar el 80 por ciento de veinte capacidades, la intersección media de 1000 sorteos es 12,66 con dos plataformas, 10,19 con tres, 8,15 con cuatro y 5,27 con seis.",
                items, 40.0, "Un cliente que solo usa lo que todas ofrecen se encoge como 0,8 elevado al número de plataformas. Por eso las abstracciones comunes necesitan capacidades opcionales declaradas y una degradación explícita.",
                label_w=220, width=860, note_kind="gold", foot="Capacidades sintéticas con semilla fija; no describen ninguna plataforma real. Idénticas en Windows y Ubuntu.")


# ---------------------------------------------------------------- SE-256
def se256_transacciones() -> Fig:
    items = [
        ("Diario clásico, sincronización completa, 500 transacciones", 2874.5, "coral", "2874,5 ms"),
        ("Diario clásico, sin sincronización", 1300.0, "gold", "1300,0 ms"),
        ("WAL, sincronización completa", 455.8, "gold", "455,8 ms"),
        ("WAL, sincronización normal", 42.1, "teal", "42,1 ms"),
        ("Diario clásico, sincronización completa, un lote", 8.0, "teal", "8,0 ms"),
    ]
    return bars("500 inserciones en SQLite según el modo de diario, la sincronización y las transacciones",
                "Barras en Windows: 500 transacciones con diario clásico y sincronización completa tardan 2874,5 milisegundos, sin sincronización 1300,0, con diario WAL completo 455,8, con WAL normal 42,1, y un lote de 500 inserciones en una transacción 8,0.",
                items, 0.19, "Agrupar escrituras en una transacción pesa más que cualquier ajuste: de 2874,5 a 8,0 ms. En Ubuntu (SQLite 3.45.1) las cifras fueron 2662,2, 46,6, 1410,3, 8,6 y 8,7 ms: el orden entre modos cambia con el sistema de archivos.",
                label_w=470, width=1180, note_kind="gold", foot=TIEMPO)


def se256_caida() -> Fig:
    rows = [
        ["Abrir el archivo y escribir encima", "Se corta a la mitad del contenido", "Documento corrupto (no es JSON válido)"],
        ["Escribir un temporal y reemplazar al final", "Se corta con el temporal a medias", "Documento anterior intacto y válido"],
        ["SQLite con 1000 inserciones sin confirmar", "El proceso termina dentro de la transacción", "1 fila (la anterior), integridad correcta"],
    ]
    return tab("Terminar el proceso a mitad de una escritura: tres formas de guardar",
               "Tabla con tres formas de guardar un documento local y qué queda tras terminar el proceso a mitad de la escritura: el archivo sobrescrito queda corrupto, el temporal con reemplazo conserva el anterior y SQLite conserva la última transacción confirmada.",
               ["Forma de guardar", "Qué ocurre", "Resultado observado"], rows, [340, 330, 330], row_h=52, size=12,
               kinds=["plain", "plain", ("coral", "teal", "teal")],
               note="El experimento termina el proceso, no corta la corriente: no prueba lo que ocurre si el sistema operativo pierde la caché de escritura. Esa garantía depende de la sincronización con el disco y del soporte, algo que aquí no se midió.",
               note_kind="coral", foot="Procesos hijo terminados con os._exit; mismo resultado en Windows y Ubuntu (WSL2).")


def se256_fusion() -> Fig:
    items = [
        ("Último registro gana, relojes sincronizados", 100.68, "coral", "100,68"),
        ("Último registro gana, un reloj 5 minutos adelantado", 106.57, "coral", "106,57"),
        ("Fusión por campo, sin importar el reloj", 47.85, "teal", "47,85"),
    ]
    return bars("Intenciones de edición perdidas en 400 ediciones de dos dispositivos sobre 200 registros",
                "Barras: con 200 registros de tres campos y 400 ediciones repartidas entre dos dispositivos, quedarse con el último registro pierde 100,68 intenciones en media con relojes alineados y 106,57 con un reloj adelantado, y fusionar por campo pierde 47,85.",
                items, 6.0, "Fusionar por campo reduce a menos de la mitad las intenciones perdidas, pero no las elimina: dos ediciones del mismo campo siguen compitiendo. Cada política es una decisión de producto sobre qué intención se sacrifica.",
                label_w=470, width=1160, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-257
def se257_estados() -> Fig:
    rows = [
        ["Estados por permiso", "6", "concedido, denegado, denegado sin volver a preguntar, revocado en ajustes, restringido por política, solo aproximado"],
        ["Combinaciones de 4 permisos", "1296", "6 elevado a 4: probarlas todas a mano no escala"],
        ["Combinaciones con código que asume «concedido»", "1280 fallan (98,8 %)", "con estados uniformes; los usuarios reales no se reparten así"],
        ["Combinaciones con «solo aproximado» y sin fallo", "15", "resultado engañoso sin ninguna excepción: la ubicación parece precisa"],
    ]
    return tab("Estados de un permiso y combinaciones de cuatro capacidades",
               "Tabla: seis estados por permiso y cuatro permisos dan 1296 combinaciones; un código que asume que el permiso está concedido falla en 1280, y 15 combinaciones con acceso solo aproximado devuelven un resultado engañoso sin lanzar ninguna excepción.",
               ["Magnitud", "Valor", "Qué significa"], rows, [310, 190, 510], row_h=60, size=12,
               kinds=["plain", "gold", "plain"],
               note="El reparto uniforme de estados es un supuesto del autor, no una medición de personas. La conclusión sólida es de forma: cada capacidad necesita un camino para cada estado, y el estado «aproximado» es el que no falla pero engaña.",
               note_kind="gold", foot=SINT)


def se257_revocacion() -> Fig:
    items = [
        ("Comprobar solo al iniciar la sesión", 24.53, "coral", "24,53 usos (0 comprobaciones)"),
        ("Comprobar cada 10 operaciones", 4.51, "gold", "4,51 usos (5 comprobaciones)"),
        ("Comprobar en cada uso", 0, "teal", "0 usos (50 comprobaciones)"),
    ]
    return bars("Usos de una capacidad después de que el usuario la revoca en mitad de la sesión",
                "Barras: en 10 000 sesiones de 50 operaciones con una revocación en un punto al azar, comprobar el permiso solo al iniciar deja 24,53 usos tras la revocación, comprobarlo cada diez operaciones deja 4,51 y comprobarlo en cada uso deja ninguno, con 50 comprobaciones.",
                items, 9.0, "La comprobación en el momento del uso es la única que respeta la revocación, y cuesta una consulta por operación. Caché y comprobación periódica reducen el coste a cambio de usos indebidos: la tolerancia es una decisión de privacidad, no de rendimiento.",
                label_w=360, width=1060, note_kind="gold", foot=SINT)


def se257_ubicacion() -> Fig:
    items = [
        ("Celdas de 0,05 y 0,5 km", 100, "coral", "100 % únicos"),
        ("Celdas de 1 km", 99.1, "coral", "99,1 % únicos"),
        ("Celdas de 2 km", 81.8, "gold", "81,8 % únicos"),
        ("Celdas de 5 km", 0, "teal", "0 % únicos"),
        ("Celdas de 10 km", 0, "teal", "0 % únicos"),
    ]
    return bars("Pares casa-trabajo únicos entre 2000 personas ficticias según la precisión de la ubicación",
                "Barras: en una ciudad sintética de 20 por 20 kilómetros con 2000 personas, el par de celdas de casa y trabajo identifica a todas con celdas de 0,5 kilómetros, a 99,1 por ciento con 1 km, a 81,8 con 2 km y a ninguna con 5 km.",
                items, 6.0, "Reducir la precisión de la ubicación protege más de lo que parece intuitivo: de 100 % a 0 % de pares únicos entre 0,5 y 5 km. El resultado depende de la densidad sintética de la ciudad y de que solo se observan dos puntos; con más puntos, la unicidad vuelve.",
                label_w=290, width=900, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-258
def se258_toque() -> Fig:
    rows = [
        ["3 mm", "29,5 %", "14,6 %", "8,5 %"],
        ["5 mm", "61,8 %", "34,8 %", "21,4 %"],
        ["7 mm", "84,4 %", "56,7 %", "37,7 %"],
        ["9 mm", "95,0 %", "74,9 %", "54,0 %"],
        ["12 mm", "99,5 %", "90,9 %", "74,9 %"],
    ]
    return tab("Toques simulados que caen dentro de un objetivo cuadrado según su lado y el error del dedo",
               "Tabla de acierto de 20 000 toques simulados con error gaussiano de 2, 3 y 4 milímetros: un objetivo de 3 mm acierta 29,5, 14,6 y 8,5 por ciento, y uno de 12 mm acierta 99,5, 90,9 y 74,9 por ciento.",
               ["Lado del objetivo", "Error 2 mm", "Error 3 mm", "Error 4 mm"], rows, [260, 240, 240, 240], row_h=44, size=13,
               note="El error del dedo es un supuesto del autor, no una medición de personas ni de pantallas: sirve para mostrar la forma de la curva. El acierto crece rápido hasta unos 9 mm y después apenas; la recomendación de cada guía de plataformas debe verificarse con usuarios reales.",
               note_kind="gold", foot=SINT)


def se258_foco() -> Fig:
    rows = [
        ["Orden de foco correcto (14 controles)", "0 %", "0"],
        ["Un control que retiene el foco (trampa)", "100 %", "6,49"],
        ["Un salto que se salta un control", "100 %", "1,00"],
        ["Un control visible fuera del orden", "100 %", "0,92"],
        ["Un recorrido que vuelve al inicio antes de tiempo", "100 %", "6,23"],
    ]
    return tab("Recorrer con el tabulador un orden de foco con un defecto: lo que detecta un recorrido automático",
               "Tabla de 1000 interfaces sintéticas de 14 controles por tipo de defecto: un recorrido que sigue el orden de foco detecta el 100 por ciento de las trampas, saltos, controles fuera del orden y ciclos anticipados, y deja 6,49, 1,00, 0,92 y 6,23 controles inalcanzables en media.",
               ["Defecto del orden de foco", "Detectado por el recorrido", "Controles inalcanzables (media)"], rows, [450, 260, 290], row_h=46, size=13,
               kinds=["plain", "teal", "gold"],
               note="El recorrido encuentra defectos de alcance, no de sentido: un orden completo que salta de la derecha a la izquierda sin lógica visual sigue siendo inalcanzable para quien necesita entender dónde está. Ese juicio requiere a una persona que use el teclado o un lector de pantalla.",
               note_kind="gold", foot=SINT)


def se258_contraste() -> Fig:
    items = [
        ("Texto oscuro sobre blanco", 16.12, "teal", "16,12:1"),
        ("Aviso coral sobre blanco", 5.14, "teal", "5,14:1"),
        ("Enlace turquesa sobre blanco", 4.75, "teal", "4,75:1"),
        ("Gris medio (119, 119, 119) sobre blanco", 4.48, "gold", "4,48:1"),
        ("Gris claro (170, 170, 170) sobre blanco", 2.32, "coral", "2,32:1"),
    ]
    return bars("Relación de contraste de cinco pares de color calculada con la fórmula de WCAG",
                "Barras: el texto oscuro sobre blanco da 16,12 a 1, el aviso coral 5,14, el enlace turquesa 4,75, un gris medio 4,48 y queda por debajo del mínimo de 4,5 para texto normal, y un gris claro 2,32, por debajo incluso del mínimo de 3 para elementos no textuales.",
                items, 36.0, "Un gris medio muy habitual queda a dos centésimas del umbral y no lo cumple; el cálculo lo detecta sin mirar la pantalla. De 20 000 colores aleatorios sobre blanco, solo el 36,2 % alcanza 4,5 a 1. El cálculo no sustituye una prueba con personas con baja visión.",
                label_w=360, width=1080, note_kind="gold", foot="Fórmula de luminancia relativa de WCAG 2.2; cálculo determinista, idéntico en Windows y Ubuntu.")


FIGURES = {
    "se-253-ancho-de-ventana-y-controles-alcanzables.svg": se253_ancho,
    "se-253-dos-instancias-sobre-un-archivo.svg": se253_instancias,
    "se-253-arranques-en-frio-segun-la-recuperacion.svg": se253_arranques,
    "se-254-perdidas-segun-el-gancho-de-guardado.svg": se254_ganchos,
    "se-254-restaurar-tras-actualizar.svg": se254_migraciones,
    "se-254-coste-de-guardar-el-estado.svg": se254_coste,
    "se-255-ganador-segun-los-pesos.svg": se255_pesos,
    "se-255-puente-entre-capas.svg": se255_puente,
    "se-255-capacidades-comunes.svg": se255_comunes,
    "se-256-transacciones-y-garantias-de-sqlite.svg": se256_transacciones,
    "se-256-caida-a-mitad-de-escritura.svg": se256_caida,
    "se-256-sincronizar-por-registro-o-por-campo.svg": se256_fusion,
    "se-257-estados-de-permiso-y-combinaciones.svg": se257_estados,
    "se-257-revocacion-en-mitad-de-la-sesion.svg": se257_revocacion,
    "se-257-precision-de-ubicacion-y-unicidad.svg": se257_ubicacion,
    "se-258-acierto-segun-el-tamano-del-objetivo.svg": se258_toque,
    "se-258-orden-de-foco-defectuoso.svg": se258_foco,
    "se-258-contraste-de-colores.svg": se258_contraste,
}
