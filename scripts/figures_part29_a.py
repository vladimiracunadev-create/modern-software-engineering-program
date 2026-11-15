"""Figures for SE-349 to SE-354 (synthetic models with fixed seeds, plus timings measured on one machine; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Modelo sintético con semilla fija; Windows y Ubuntu (WSL2) con cifras idénticas. Los parámetros son supuestos del autor."
MED = "Tiempos medidos en un equipo de 8 hilos lógicos con otros procesos activos; cambian de una ejecución a otra, léanse como órdenes de magnitud."


# ---------------------------------------------------------------- SE-349
def se349_matriz() -> Fig:
    rows = [
        ["Instalación propia (local)", "12", "0", "0", "Las 12 capas"],
        ["IaaS", "9", "0", "3", "Sistema operativo hacia arriba"],
        ["PaaS", "4", "3", "5", "Código, identidad, datos y configuración del servicio"],
        ["SaaS", "3", "2", "7", "Identidad, datos y configuración del servicio"],
    ]
    return tab("Quién responde por cada una de 12 capas según el modelo de servicio",
               "Tabla: de 12 capas, una instalación propia deja las 12 al cliente; IaaS deja 9 al cliente y 3 al proveedor; PaaS deja 4 al cliente, 3 compartidas y 5 al proveedor; SaaS deja 3 al cliente, 2 compartidas y 7 al proveedor. Identidad, datos y configuración del servicio son del cliente en los cuatro modelos.",
               ["Modelo", "Del cliente", "Compartidas", "Del proveedor", "Lo que sigue siendo del cliente"], rows, [230, 120, 130, 130, 330], row_h=52, size=13,
               note="Pasar de IaaS a SaaS reduce la lista, pero tres capas no se mueven nunca: quién entra, qué datos hay y cómo se configura el servicio. La matriz es un modelo del autor basado en la estructura de los documentos públicos de responsabilidad compartida; cada proveedor y cada producto la dibuja distinta.",
               note_kind="gold", foot=SINT)


def se349_exposicion() -> Fig:
    items = [
        ("Instalación propia", 3708.0, "coral", "3 708 días (100 % por capas del cliente)"),
        ("IaaS", 3579.0, "coral", "3 579 días (99,5 %)"),
        ("PaaS", 2137.0, "gold", "2 137 días (84,7 %)"),
        ("SaaS", 1061.0, "teal", "1 061 días (60,7 %)"),
    ]
    return bars("Días de exposición al año por modelo, con las mismas 127 vulnerabilidades anuales (media de 1 000 años)",
                "Barras: con las mismas vulnerabilidades, la suma anual de días expuestos baja de 3 708 en una instalación propia a 3 579 con IaaS, 2 137 con PaaS y 1 061 con SaaS; en SaaS el 60,7 por ciento de lo que queda corresponde a capas que sigue operando el cliente.",
                items, 0.1, "IaaS casi no mejora porque las capas que más vulnerabilidades traen, sistema operativo, entorno de ejecución y dependencias, siguen siendo del cliente. En SaaS la exposición cae a un tercio, pero el 60,7 % del resto es de identidad, datos y configuración: lo que se delega se parchea, lo que se configura se responde.",
                label_w=190, width=960, note_kind="teal", foot=SINT)


def se349_superficie() -> Fig:
    rows = [
        ["Instalación propia", "300", "95,1 %", "99,8 %", "3,0"],
        ["IaaS", "120", "70,1 %", "91,1 %", "1,2"],
        ["PaaS", "45", "36,4 %", "59,7 %", "0,45"],
        ["SaaS", "14", "13,1 %", "24,6 %", "0,14"],
    ]
    return tab("Probabilidad de dejar al menos un ajuste de seguridad mal configurado",
               "Tabla: con una probabilidad de error del 1 por ciento por ajuste, dejar al menos uno mal puesto ocurre en el 95,1 por ciento de las instalaciones propias con 300 ajustes, 70,1 con IaaS y 120 ajustes, 36,4 con PaaS y 45 ajustes y 13,1 con SaaS y 14 ajustes; con el 2 por ciento sube a 99,8, 91,1, 59,7 y 24,6.",
               ["Modelo", "Ajustes del cliente", "P(al menos 1 error), 1 % por ajuste", "P, 2 % por ajuste", "Errores esperados (1 %)"], rows, [210, 150, 250, 140, 150], row_h=52, size=13,
               note="La probabilidad cae porque hay menos ajustes, no porque el cliente se equivoque menos. Con 14 ajustes y un 1 % de error, uno de cada ocho equipos tiene un error: el modelo es el producto 1 − (1 − p)^n, verificado con 20 000 ensayos por celda; los 300, 120, 45 y 14 ajustes son supuestos del autor.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-350
def se350_arranque() -> Fig:
    rows = [
        ["Crear y unir un hilo del mismo proceso", "≈ 170 µs (150–860)", "≈ 340 µs (185–2 040)"],
        ["Proceso mínimo (intérprete sin módulos del sitio)", "≈ 34 ms (33–51)", "≈ 16 ms (14–25)"],
        ["Proceso vacío del intérprete", "≈ 109 ms (105–156)", "≈ 41 ms (33–65)"],
        ["Proceso que importa siete módulos de la biblioteca", "≈ 405 ms (383–544)", "≈ 161 ms (139–201)"],
    ]
    return tab("Coste de arrancar una unidad de ejecución: mediana y rango observado",
               "Tabla: crear y unir un hilo cuesta unas decenas a cientos de microsegundos; arrancar un proceso mínimo del intérprete unos 34 milisegundos en Windows y 16 en Ubuntu; un proceso vacío 109 y 41; un proceso que importa siete módulos 405 y 161 milisegundos.",
               ["Unidad", "Windows 11", "Ubuntu (WSL2)"], rows, [430, 230, 230], row_h=52, size=13,
               note="Hilo, proceso y proceso con dependencias difieren en dos o tres órdenes de magnitud, y la parte que más pesa no es el aislamiento sino lo que se inicializa dentro. No se midió ninguna máquina virtual ni contenedor: estas filas son la cota inferior de cualquier unidad que arranque un intérprete.",
               note_kind="gold", foot=MED)


def se350_densidad() -> Fig:
    items = [
        ("Procesos (sin sobrecoste)", 95.0, "teal", "95 instancias"),
        ("Contenedores (30 MiB supuestos)", 79.0, "gold", "79 instancias"),
        ("Máquinas virtuales (1 024 MiB supuestos)", 12.0, "coral", "12 instancias"),
    ]
    return bars("Instancias de una aplicación de 150 MiB que caben en un anfitrión de 16 GiB con 2 GiB reservados",
                "Barras: con un sobrecoste por instancia de 0, 30 y 1 024 MiB caben 95 procesos, 79 contenedores y 12 máquinas virtuales de una aplicación de 150 MiB en 14 GiB disponibles.",
                items, 3.6, "El sobrecoste por instancia, no el tamaño de la aplicación, decide la densidad: 1 GiB de sistema invitado cuesta casi el 87 % del espacio de cada instancia. Los 30 MiB y 1 024 MiB son supuestos del autor; el intérprete vacío midió 17 MiB en Windows y 13 en Ubuntu, y 27 y 23 con siete módulos.",
                label_w=360, width=980, note_kind="gold", foot=SINT)


def se350_vecino() -> Fig:
    rows = [
        ["1 (referencia)", "1,00", "1,00"],
        ["2", "0,58 (0,26–0,80)", "0,86 (0,73–1,05)"],
        ["4", "0,37 (0,25–0,40)", "0,58 (0,39–0,62)"],
        ["8", "0,28 (0,25–0,31)", "0,34 (0,32–0,42)"],
        ["16", "0,22 (0,18–0,23)", "0,21 (0,18–0,25)"],
    ]
    return tab("Vecino ruidoso: trabajo por proceso al correr k procesos que consumen CPU a la vez, relativo a correr uno solo",
               "Tabla: con 8 hilos lógicos, el trabajo por proceso baja a 0,58 en Windows y 0,86 en Ubuntu con dos procesos, a 0,37 y 0,58 con cuatro, a 0,28 y 0,34 con ocho y a 0,22 y 0,21 con dieciséis, mediana de siete repeticiones.",
               ["Procesos simultáneos", "Windows 11: mediana (rango)", "Ubuntu (WSL2): mediana (rango)"], rows, [250, 330, 330], row_h=44, size=13,
               note="Con 8 hilos lógicos se esperaba un valor cercano a 1,00 hasta ocho procesos y 0,50 con dieciséis. Bajó antes porque el anfitrión no estaba ocioso: otras tareas compartían los núcleos, que es el problema que un límite de CPU reservado intenta acotar. No se probaron cuotas ni cgroups.",
               note_kind="coral", foot=MED)


# ---------------------------------------------------------------- SE-351
def se351_ubicacion() -> Fig:
    rows = [
        ["Primer ajuste", "0,05 (peor: 4)", "34", "27", "0"],
        ["Mejor ajuste", "0,04 (peor: 3)", "34", "27", "0"],
        ["Menos asignado (por defecto de Kubernetes)", "1,41 (peor: 5)", "0", "2", "4"],
    ]
    return tab("Pods que no caben (de 150) en 19 nodos de 4 CPU y 16 GiB según la política y el orden de llegada",
               "Tabla: con el 91 por ciento de la CPU del clúster ocupada, primer ajuste y mejor ajuste dejan sin ubicar menos de un pod con llegada al azar, 34 si los pods se ordenan por CPU decreciente y 27 por memoria decreciente, y ninguno si se ordenan por su dimensión dominante; menos asignado deja 1,41, 0, 2 y 4.",
               ["Política", "Llegada al azar (media de 200; peor)", "CPU decreciente", "Memoria decreciente", "Dimensión dominante"], rows, [310, 210, 130, 140, 140], row_h=52, size=12,
               note="Ordenar de mayor a menor mejora el empaquetado de una sola dimensión y lo empeora en dos: los pods grandes en CPU llenan los nodos y dejan memoria sin usar. Ninguna política gana siempre. El conjunto es sintético (69 250 m de CPU y 228 864 MiB pedidos) y el orden por dimensión dominante es una elección del autor.",
               note_kind="coral", foot=SINT)


def se351_reconciliacion() -> Fig:
    rows = [
        ["1 s", "102,6", "Una lectura por segundo; el arranque (7 s) domina"],
        ["5 s", "125,4", "+22 % respecto de 1 s"],
        ["15 s", "193,9", "Casi el doble que con 1 s"],
        ["30 s", "319,9", "3,1 veces"],
        ["60 s", "474,4", "4,6 veces"],
    ]
    return tab("Réplicas-segundo ausentes en 600 s con 10 réplicas deseadas, según cada cuánto revisa el controlador (media de 300 corridas)",
               "Tabla: con un intervalo de revisión de 1 segundo faltan en promedio 102,6 réplicas-segundo en 600 segundos; con 5 segundos faltan 125,4, con 15 faltan 193,9, con 30 faltan 319,9 y con 60 faltan 474,4. Con un retardo de reinicio que se duplica desde 10 s hasta 300 s, una réplica que siempre falla se reinicia 15 veces en una hora; con 10 s fijos serían 360.",
               ["Intervalo del controlador", "Réplicas-segundo ausentes", "Lectura"], rows, [250, 250, 420], row_h=44, size=13,
               note="El bucle no evita el fallo: acota cuánto dura. La espera tras cada reinicio cuesta menos que reiniciar sin freno, porque 15 intentos por hora en lugar de 360 dejan a la réplica fallida de agotar los recursos del nodo. Dos fallos por réplica del 0,2 % por segundo y 3 pods perdidos en el segundo 100 son supuestos del autor.",
               note_kind="teal", foot=SINT)


def se351_sobreasignacion() -> Fig:
    rows = [
        ["1,00", "0,0 %", "51 %"],
        ["1,25", "0,1 %", "65 %"],
        ["1,50", "4,3 %", "79 %"],
        ["2,00", "67,9 %", "97 %"],
        ["3,00", "100 %", "100 %"],
    ]
    return tab("Probabilidad de que el uso real de un nodo supere su capacidad según cuánto se sobreasigna lo pedido",
               "Tabla: si la suma de lo pedido es igual a la capacidad, el nodo no se satura nunca; con 1,25 veces, el 0,1 por ciento de los casos; con 1,5 veces, el 4,3; con 2 veces, el 67,9; con 3 veces, siempre. El uso medio sube del 51 al 100 por ciento.",
               ["Pedido ÷ capacidad", "Probabilidad de saturar", "Uso medio del nodo"], rows, [300, 300, 300], row_h=44, size=13,
               note="La sobreasignación compra uso medio a cambio de riesgo de cola: pasar de 1,5 a 2,0 veces no suma un 33 % de riesgo, lo multiplica por 16. La distribución del uso (normal de media 0,55 y desviación 0,25 de lo pedido, acotada) es un supuesto del autor; con uso correlacionado entre pods el riesgo sería mayor.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-352
def se352_frio() -> Fig:
    rows = [
        ["0,05 por minuto", "96,6 %", "79,1 %", "46,8 %", "3,0 %"],
        ["0,2 por minuto", "83,3 %", "37,0 %", "5,3 %", "0,05 %"],
        ["1 por minuto", "37,4 %", "1,15 %", "0,39 %", "0,32 %"],
        ["5 por minuto", "2,35 %", "1,14 %", "0,53 %", "0,03 %"],
        ["30 por minuto", "1,02 %", "0,24 %", "0,08 %", "0,01 %"],
    ]
    return tab("Porcentaje de peticiones que caen en un arranque en frío según la tasa de llegada y la inactividad tolerada",
               "Tabla: con 0,05 peticiones por minuto, el 96,6 por ciento arranca en frío si la instancia se descarta tras 1 minuto y el 3,0 si tras 60; con 1 por minuto, el 37,4 y el 0,32; con 30 por minuto, el 1,02 y el 0,01.",
               ["Tasa de llegada", "Descarte tras 1 min", "5 min", "15 min", "60 min"], rows, [250, 190, 150, 150, 150], row_h=44, size=13,
               note="El arranque en frío no es un defecto del tráfico alto: a 30 peticiones por minuto es raro y a 0,05 es casi la regla. La tasa baja con ráfagas sufre más que la alta uniforme. Siete días de llegadas de Poisson, una petición por instancia a la vez y 0,2 s de servicio son supuestos del autor.",
               note_kind="gold", foot=SINT)


def se352_dependencias() -> Fig:
    rows = [
        ["Sin dependencias", "≈ 49 ms (45–66)", "≈ 30 ms (26–36)"],
        ["json y re", "≈ 104 ms (92–119)", "≈ 38 ms (33–47)"],
        ["+ sqlite3, decimal, http.client, email", "≈ 220 ms (206–306)", "≈ 90 ms (78–141)"],
        ["+ asyncio, ssl, unittest, xml.dom", "≈ 734 ms (517–868)", "≈ 155 ms (137–450)"],
    ]
    return tab("Tiempo de arrancar un proceso Python que solo importa módulos de la biblioteca estándar",
               "Tabla: arrancar un intérprete sin dependencias toma unos 49 milisegundos en Windows y 30 en Ubuntu; importar json y re lo lleva a 104 y 38; añadir sqlite3, decimal, http.client y email, a 220 y 90; y añadir asyncio, ssl, unittest y xml.dom, a 734 y 155, mediana de 21 repeticiones.",
               ["Módulos importados al iniciar", "Windows 11: mediana (rango)", "Ubuntu (WSL2): mediana (rango)"], rows, [400, 270, 250], row_h=44, size=13,
               note="El coste inicial de una función sin servidor crece con lo que carga, no con lo que ejecuta: quince veces más en Windows entre la primera y la última fila. Es el único tiempo de esta clase medido de verdad; el arranque de una plataforma gestionada incluye además descarga y aislamiento que no se midió.",
               note_kind="coral", foot=MED)


def se352_duplicados() -> Fig:
    items = [
        ("Sin deduplicar", 976.0, "coral", "976 efectos repetidos"),
        ("Ventana de 10 s", 681.0, "coral", "681"),
        ("Ventana de 60 s", 121.0, "gold", "121"),
        ("Ventana de 300 s", 0.0, "teal", "0"),
        ("Sin caducidad", 0.0, "teal", "0 (pero la tabla crece sin fin)"),
    ]
    return bars("Efectos repetidos de 976 reentregas (20 000 eventos, el 5 % reentregado a los 30 s en promedio)",
                "Barras: sin deduplicar, las 976 reentregas repiten su efecto; con una ventana de 10 segundos repiten 681, con 60 segundos repiten 121, y con 300 segundos o sin caducidad ninguna.",
                items, 0.34, "Deduplicar con una ventana más corta que el retardo de la reentrega elimina solo una parte de los duplicados. Con un retardo exponencial de media 30 s, una de cada ocho reentregas llega después de 60 s, el doble de la media, y por eso pasan 121 de 976. Los 20 000 eventos, el 5 % de reentrega y la media de 30 s son supuestos del autor.",
                label_w=190, width=960, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-353
def se353_saltos() -> Fig:
    rows = [
        ["Base de datos", "4", "1 / 5 / 9", "112"],
        ["Almacén de secretos", "4", "1 / 3 / 7", "116"],
    ]
    return tab("Saltos mínimos desde internet hasta un destino sensible tras añadir una sola regla (127 reglas posibles)",
               "Tabla: en una red de 12 servicios la base de datos y el almacén de secretos están a 4 saltos de internet; de las 127 reglas que se pueden añadir, 1 deja la base de datos a un salto, 5 a dos y 9 a tres, y 112 no cambian la distancia; para el almacén de secretos son 1, 3 y 7, y 116 no la cambian.",
               ["Destino", "Saltos al inicio", "Reglas que lo dejan a 1 / 2 / 3 saltos", "Reglas sin efecto"], rows, [280, 160, 320, 150], row_h=52, size=13,
               note="Nueve de cada diez reglas nuevas no acercan nada, pero 15 de 127 sí acercan la base de datos, y una sola la deja directa. Menos saltos no significa más tráfico: significa menos barreras entre un atacante y el dato. Un salto es una regla permitida; no se modelaron puertos, protocolos ni reglas de salida.",
               note_kind="coral", foot=SINT)


def se353_permisos() -> Fig:
    rows = [
        ["Administrador (* sobre *)", "400", "5,8", "1,4 %", "25"],
        ["Todo el servicio sobre *", "80,8", "5,8", "7,2 %", "6"],
        ["Acciones usadas sobre *", "32,4", "5,8", "17,9 %", "2"],
        ["Pares acción-recurso usados", "5,8", "5,8", "100 %", "2"],
    ]
    return tab("Pares acción-recurso concedidos y usados por rol (25 roles, 400 pares posibles)",
               "Tabla: un rol administrador concede 400 pares de los que usa 5,8, el 1,4 por ciento, y los 25 roles tienen ruta de escalada; conceder el servicio completo da 80,8 pares, el 7,2 por ciento usado y 6 roles con escalada; conceder las acciones usadas sobre todos los recursos da 32,4 y 2 roles; conceder solo los pares usados da 5,8 y 2 roles.",
               ["Estilo de política", "Pares concedidos", "Usados", "Proporción usada", "Roles con ruta de escalada"], rows, [320, 150, 100, 150, 190], row_h=52, size=13,
               note="Dos roles conservan una ruta de escalada incluso con el mínimo porque su uso real incluye la acción de adjuntar políticas: el menor privilegio mide lo concedido contra lo usado, no si lo usado es prudente. Los roles, el registro de uso y las 60 acciones son sintéticos; generar la política desde el registro supone que el registro fue completo.",
               note_kind="gold", foot=SINT)


def se353_detector() -> Fig:
    rows = [
        ["Entropía ≥ 3,5", "60", "173", "20", "25,8 %", "75,0 %"],
        ["Entropía ≥ 4,0", "40", "60", "40", "40,0 %", "50,0 %"],
        ["Entropía ≥ 4,5", "32", "60", "48", "34,8 %", "40,0 %"],
        ["Solo el nombre de la variable", "52", "0", "28", "100 %", "65,0 %"],
        ["Nombre o entropía ≥ 4,5", "62", "60", "18", "50,8 %", "77,5 %"],
    ]
    return tab("Detector de secretos en 80 secretos sintéticos y 180 señuelos, con cinco reglas",
               "Tabla: la entropía sola con umbral 3,5 halla 60 de 80 secretos y 173 falsos positivos; con 4,0 halla 40 y 60 falsos; con 4,5 halla 32 y 60 falsos; el nombre de la variable halla 52 sin falsos positivos; nombre o entropía 4,5 halla 62 con 60 falsos positivos.",
               ["Regla", "Hallados", "Falsos positivos", "Omitidos", "Precisión", "Exhaustividad"], rows, [270, 100, 140, 110, 110, 150], row_h=44, size=12,
               note="Los secretos hexadecimales y las contraseñas con palabras tienen entropía menor que un resumen SHA-256 en base 64, así que ningún umbral separa bien. El contexto (el nombre de la variable) es más preciso y deja pasar a los que no lo tienen. Los 80 secretos y 180 señuelos los generé yo: las cifras describen estas reglas sobre estos datos, no un escáner real.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-354
def se354_deriva() -> Fig:
    rows = [
        ["Recursos alterados fuera del código (k)", "0", "5", "20"],
        ["Deriva que el plan muestra sin refrescar", "0", "0,49", "2,01"],
        ["Deriva que el plan muestra tras refrescar", "0", "5,0", "20,0"],
        ["Cambios totales en el plan sin refrescar", "10", "10", "10"],
        ["Cambios totales en el plan refrescado", "10", "14,5", "28,0"],
        ["Arreglos manuales que el siguiente apply revierte", "0", "4,51", "17,99"],
    ]
    return tab("Plan declarativo sobre 100 recursos con 10 ediciones en el código y k alterados a mano (media de 1 000 corridas)",
               "Tabla: con 5 recursos alterados a mano, un plan que no refresca el estado real muestra de media 0,49 de ellos, solo cuando coinciden con una edición del código; un plan refrescado muestra los 5, con 14,5 cambios en total frente a 10, y el siguiente apply revierte 4,51 arreglos manuales; con 20 alterados, 2,01 frente a 20 y se revierten 17,99.",
               ["Medida", "k = 0", "k = 5", "k = 20"], rows, [470, 120, 120, 120], row_h=44, size=12,
               note="Un plan sin refresco compara el código con un archivo de estado que supone cierto: ve la deriva por casualidad. Con refresco la ve toda, y entonces aplicar sin leerla revierte los arreglos de emergencia hechos a mano. El modelo es un diferenciador de diccionarios, no Terraform ni OpenTofu.",
               note_kind="coral", foot=SINT)


def se354_estado() -> Fig:
    rows = [
        ["2 aplicaciones a la vez", "6", "2", "4", "—", "2 (sin pérdidas)"],
        ["3 aplicaciones a la vez", "90", "6", "36", "48", "6 (sin pérdidas)"],
    ]
    return tab("Escrituras simultáneas sobre un mismo archivo de estado: todas las intercalaciones de leer y escribir",
               "Tabla: con dos aplicaciones que leen el estado y luego lo escriben entero hay 6 intercalaciones y 4 pierden el trabajo de una; con tres hay 90, de las cuales 6 no pierden nada, 36 pierden el trabajo de una y 48 el de dos; con un bloqueo solo quedan las ejecuciones en serie, 2 y 6, sin pérdidas.",
               ["Situación", "Intercalaciones", "Sin pérdida", "Pierde 1", "Pierde 2", "Con bloqueo"], rows, [250, 150, 140, 120, 120, 160], row_h=44, size=13,
               note="Es la misma actualización perdida de la Parte 26 aplicada a un archivo que describe infraestructura: el recurso existe en la nube y no en el estado, y el siguiente plan lo creará otra vez o fallará por duplicado. Un bloqueo con caducidad añade su propio riesgo cuando el proceso muere con el bloqueo tomado.",
               note_kind="teal", foot=SINT)


def se354_paralelismo() -> Fig:
    items = [
        ("Un recurso a la vez", 2832.0, "coral", "2 832 s"),
        ("2 en paralelo", 1423.0, "gold", "1 423 s"),
        ("4 en paralelo", 798.0, "gold", "798 s"),
        ("10 en paralelo", 577.0, "teal", "577 s (= camino crítico)"),
        ("60 en paralelo", 577.0, "teal", "577 s"),
    ]
    return bars("Tiempo de aplicar un grafo de 60 recursos y 86 dependencias según cuántos se crean a la vez",
                "Barras: aplicar el grafo de 60 recursos tarda 2 832 segundos de uno en uno, 1 423 con dos en paralelo, 798 con cuatro y 577 con diez o con sesenta, que es el camino crítico.",
                items, 0.17, "El paralelismo ayuda hasta el camino crítico, la cadena más larga de dependencias, y después no sirve: pasar de 10 a 60 trabajos no ahorra un segundo. Las duraciones (5–120 s) y la forma del grafo son sintéticas; con un límite de tasa del proveedor el tope práctico sería menor. Una arista de más que cierre un ciclo hace imposible el orden.",
                label_w=210, width=960, note_kind="gold", foot=SINT)


FIGURES = {
    "se-349-matriz-de-responsabilidades.svg": se349_matriz,
    "se-349-dias-de-exposicion-por-modelo.svg": se349_exposicion,
    "se-349-superficie-de-configuracion.svg": se349_superficie,
    "se-350-coste-de-arrancar-una-unidad.svg": se350_arranque,
    "se-350-instancias-por-anfitrion.svg": se350_densidad,
    "se-350-vecino-ruidoso.svg": se350_vecino,
    "se-351-politicas-de-ubicacion.svg": se351_ubicacion,
    "se-351-reconciliacion-y-reinicios.svg": se351_reconciliacion,
    "se-351-sobreasignacion-de-recursos.svg": se351_sobreasignacion,
    "se-352-arranques-en-frio.svg": se352_frio,
    "se-352-peso-de-las-dependencias.svg": se352_dependencias,
    "se-352-duplicados-y-ventana-de-deduplicacion.svg": se352_duplicados,
    "se-353-saltos-hasta-la-base-de-datos.svg": se353_saltos,
    "se-353-permisos-concedidos-y-usados.svg": se353_permisos,
    "se-353-detector-de-secretos.svg": se353_detector,
    "se-354-deriva-y-refresco-del-estado.svg": se354_deriva,
    "se-354-escrituras-simultaneas-del-estado.svg": se354_estado,
    "se-354-paralelismo-y-camino-critico.svg": se354_paralelismo,
}
