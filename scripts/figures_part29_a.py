"""Figures for SE-349 to SE-354 (synthetic models with fixed seeds, plus timings measured on one machine; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, fmt_exact, grouped_bars, heatmap, line_chart, stacked_bars
from figures_part07_a import bars

SINT = "Modelo sintético con semilla fija; Windows y Ubuntu (WSL2) con cifras idénticas. Los parámetros son supuestos del autor."
MED = "Tiempos medidos en un equipo de 8 hilos lógicos con otros procesos activos; cambian de una ejecución a otra, léanse como órdenes de magnitud."


# ---------------------------------------------------------------- SE-349
def se349_matriz() -> Fig:
    return stacked_bars(
        "Quién responde por cada una de las 12 capas según el modelo de servicio",
        "Barras apiladas horizontales con cuántas de 12 capas quedan al cliente, compartidas o del proveedor: una instalación propia deja las 12 al cliente; IaaS 9 al cliente y 3 al proveedor; PaaS 4, 3 compartidas y 5; SaaS 3, 2 compartidas y 7. El tramo del cliente se encoge pero no desaparece.",
        ["Instalación propia (local)", "IaaS", "PaaS", "SaaS"],
        [("Del cliente", [12, 9, 4, 3], "coral"), ("Compartidas", [0, 0, 3, 2], "gold"), ("Del proveedor", [0, 3, 5, 7], "teal")],
        unit="Capas (de 12)", horizontal=True, label_w=230,
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
    return grouped_bars(
        "Probabilidad de dejar al menos un ajuste de seguridad mal configurado, con 1 % y 2 % de error por ajuste",
        "Barras horizontales agrupadas con la probabilidad de dejar al menos un ajuste mal configurado: con un 1 por ciento de error por ajuste es 95,1 con 300 ajustes (instalación propia), 70,1 con 120 (IaaS), 36,4 con 45 (PaaS) y 13,1 con 14 (SaaS); con un 2 por ciento sube a 99,8, 91,1, 59,7 y 24,6.",
        ["Instalación propia (300 ajustes)", "IaaS (120 ajustes)", "PaaS (45 ajustes)", "SaaS (14 ajustes)"],
        [("1 % de error por ajuste", [95.1, 70.1, 36.4, 13.1], "gold"), ("2 % de error por ajuste", [99.8, 91.1, 59.7, 24.6], "coral")],
        unit="% de instalaciones con al menos un error", horizontal=True, label_w=250, decimals=1,
        note="La probabilidad cae porque hay menos ajustes, no porque el cliente se equivoque menos. Con 14 ajustes y un 1 % de error, uno de cada ocho equipos tiene un error: el modelo es el producto 1 − (1 − p)^n, verificado con 20 000 ensayos por celda; los 300, 120, 45 y 14 ajustes son supuestos del autor.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-350
def se350_arranque() -> Fig:
    return grouped_bars(
        "Coste de arrancar una unidad de ejecución: mediana en Windows y en Ubuntu",
        "Barras agrupadas en escala logarítmica con la mediana del arranque: un hilo cuesta 0,17 milisegundos en Windows y 0,34 en Ubuntu; un proceso mínimo 34 y 16; un proceso vacío del intérprete 109 y 41; un proceso que importa siete módulos 405 y 161. Del hilo al proceso con módulos hay tres órdenes de magnitud.",
        ["Hilo (crear y unir)", "Proceso mínimo", "Proceso vacío del intérprete", "Proceso con siete módulos"],
        [("Windows 11", [0.17, 34, 109, 405], "navy"), ("Ubuntu (WSL2)", [0.34, 16, 41, 161], "teal")],
        unit="ms (mediana)", log=True, ticks=[0.1, 1, 10, 100, 1000], plot_h=300,
        note="Hilo, proceso y proceso con dependencias difieren en dos o tres órdenes de magnitud, y la parte que más pesa no es el aislamiento sino lo que se inicializa dentro. No se midió ninguna máquina virtual ni contenedor: estas barras son la cota inferior de cualquier unidad que arranque un intérprete.",
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
    return line_chart(
        "Vecino ruidoso: trabajo por proceso al correr k procesos que consumen CPU, relativo a correr uno solo",
        "Líneas con el trabajo por proceso relativo al de uno solo según los procesos simultáneos: en Windows baja a 0,58, 0,37, 0,28 y 0,22 con 2, 4, 8 y 16 procesos; en Ubuntu a 0,86, 0,58, 0,34 y 0,21. La línea punteada es lo esperado con 8 hilos ociosos, 1,00 hasta ocho procesos y 0,50 con dieciséis; las dos medidas caen por debajo.",
        [("Windows 11", [(1, 1.0, "1,00", "t"), (2, 0.58, "0,58", "b"), (4, 0.37, "0,37", "b"), (8, 0.28, "0,28", "b"), (16, 0.22, "0,22", "b")], "navy"),
         ("Ubuntu (WSL2)", [(1, 1.0, "", "t"), (2, 0.86, "0,86", "t"), (4, 0.58, "0,58", "t"), (8, 0.34, "0,34", "t"), (16, 0.21, "0,21", "t")], "teal"),
         ("Esperado con 8 hilos ociosos", [(1, 1.0, "", "t"), (2, 1.0, "", "t"), (4, 1.0, "", "t"), (8, 1.0, "", "t"), (16, 0.5, "0,50", "r")], "grey")],
        x_label="Procesos simultáneos (k)", y_label="Trabajo por proceso (1 = uno solo)",
        x_ticks=[(1, "1"), (2, "2"), (4, "4"), (8, "8"), (16, "16")], y_ticks=[0, 0.25, 0.5, 0.75, 1.0], log_x=True,
        point_labels="none",
        note="Con 8 hilos lógicos se esperaba un valor cercano a 1,00 hasta ocho procesos y 0,50 con dieciséis. Bajó antes porque el anfitrión no estaba ocioso: otras tareas compartían los núcleos, que es el problema que un límite de CPU reservado intenta acotar. No se probaron cuotas ni cgroups.",
        note_kind="coral", foot=MED)


# ---------------------------------------------------------------- SE-351
def se351_ubicacion() -> Fig:
    return heatmap(
        "Pods que no caben (de 150) en 19 nodos de 4 CPU y 16 GiB según la política y el orden de llegada",
        "Mapa de calor con los pods sin ubicar según la política y el orden de llegada: primer ajuste y mejor ajuste dejan menos de un pod con llegada al azar, 34 si se ordenan por CPU decreciente y 27 por memoria decreciente, y ninguno por dimensión dominante; menos asignado deja 1,41, 0, 2 y 4. Ordenar de mayor a menor empeora a las dos primeras.",
        ["Primer ajuste", "Mejor ajuste", "Menos asignado (Kubernetes)"],
        ["Llegada al azar (media de 200)", "CPU decreciente", "Memoria decreciente", "Dimensión dominante"],
        [[0.05, 34, 27, 0], [0.04, 34, 27, 0], [1.41, 0, 2, 4]],
        unit="pods sin ubicar", scale="coral", cell_fmt=fmt_exact, row_title="Política", col_title="Orden de llegada de los pods",
        highlight=[(0, 1), (0, 2), (1, 1), (1, 2)], label_w=230,
        note="Ordenar de mayor a menor mejora el empaquetado de una sola dimensión y lo empeora en dos: los pods grandes en CPU llenan los nodos y dejan memoria sin usar. Ninguna política gana siempre. El conjunto es sintético (69 250 m de CPU y 228 864 MiB pedidos) y el orden por dimensión dominante es una elección del autor; el peor caso con llegada al azar (4, 3 y 5 pods) está en la tabla.",
        note_kind="coral", foot=SINT)


def se351_reconciliacion() -> Fig:
    return line_chart(
        "Réplicas-segundo ausentes en 600 s con 10 réplicas deseadas, según cada cuánto revisa el controlador",
        "Línea con las réplicas-segundo ausentes en 600 segundos según el intervalo de revisión del controlador, media de 300 corridas: 102,6 con 1 segundo, 125,4 con 5, 193,9 con 15, 319,9 con 30 y 474,4 con 60; con 60 segundos faltan 4,6 veces más que con 1.",
        [("Réplicas-segundo ausentes", [(1, 102.6, "102,6", "t"), (5, 125.4, "125,4", "t"), (15, 193.9, "193,9", "t"), (30, 319.9, "319,9", "t"), (60, 474.4, "474,4", "l")], "coral")],
        x_label="Intervalo de revisión del controlador (s)", y_label="Réplicas-segundo ausentes en 600 s",
        x_ticks=[(1, "1"), (5, "5"), (15, "15"), (30, "30"), (60, "60")], y_ticks=[0, 100, 200, 300, 400, 500], point_labels="none",
        note="El bucle no evita el fallo: acota cuánto dura, y el arranque de 7 s deja un piso de 102,6 aun revisando cada segundo. La espera tras cada reinicio cuesta menos que reiniciar sin freno: con un retardo que se duplica desde 10 s hasta 300 s, una réplica que siempre falla se reinicia 15 veces por hora; con 10 s fijos serían 360. Dos fallos por réplica del 0,2 % por segundo y 3 pods perdidos en el segundo 100 son supuestos del autor.",
        note_kind="teal", foot=SINT)


def se351_sobreasignacion() -> Fig:
    return line_chart(
        "Sobreasignación: probabilidad de saturar un nodo y uso medio según cuánto se pide frente a la capacidad",
        "Líneas con dos curvas según la sobreasignación: la probabilidad de que el uso real supere la capacidad es 0 con 1,00 veces, 0,1 por ciento con 1,25, 4,3 con 1,5, 67,9 con 2 y 100 con 3; el uso medio del nodo sube de 51 a 65, 79, 97 y 100 por ciento. El riesgo despega después de 1,5 veces.",
        [("Probabilidad de saturar", [(1, 0, "0", "t"), (1.25, 0.1, "0,1", "t"), (1.5, 4.3, "4,3", "t"), (2, 67.9, "67,9", "b"), (3, 100, "100", "b")], "coral"),
         ("Uso medio del nodo", [(1, 51, "51", "t"), (1.25, 65, "65", "t"), (1.5, 79, "79", "t"), (2, 97, "97", "t"), (3, 100, "", "t")], "teal")],
        x_label="Pedido ÷ capacidad del nodo", y_label="Porcentaje (%)",
        x_ticks=[(1, "1,00"), (1.25, "1,25"), (1.5, "1,50"), (2, "2,00"), (3, "3,00")], y_ticks=[0, 25, 50, 75, 100], point_labels="none",
        note="La sobreasignación compra uso medio a cambio de riesgo de cola: pasar de 1,5 a 2,0 veces no suma un 33 % de riesgo, lo multiplica por 16. La distribución del uso (normal de media 0,55 y desviación 0,25 de lo pedido, acotada) es un supuesto del autor; con uso correlacionado entre pods el riesgo sería mayor.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-352
def se352_frio() -> Fig:
    shown = {96.6: "96,6", 79.1: "79,1", 46.8: "46,8", 3.0: "3,0", 83.3: "83,3", 37.0: "37,0", 5.3: "5,3", 0.05: "0,05", 37.4: "37,4",
             1.15: "1,15", 0.39: "0,39", 0.32: "0,32", 2.35: "2,35", 1.14: "1,14", 0.53: "0,53", 0.03: "0,03", 1.02: "1,02",
             0.24: "0,24", 0.08: "0,08", 0.01: "0,01"}
    return heatmap(
        "Porcentaje de peticiones que caen en un arranque en frío según la tasa de llegada y la inactividad tolerada",
        "Mapa de calor con el porcentaje de peticiones que arrancan en frío: con 0,05 peticiones por minuto, 96,6 si la instancia se descarta tras 1 minuto de inactividad y 3,0 si tras 60; con 1 por minuto, 37,4 y 0,32; con 30 por minuto, 1,02 y 0,01. El color se concentra en la esquina de poco tráfico y descarte rápido.",
        ["0,05 por minuto", "0,2 por minuto", "1 por minuto", "5 por minuto", "30 por minuto"],
        ["Descarte tras 1 min", "Descarte tras 5 min", "Descarte tras 15 min", "Descarte tras 60 min"],
        [[96.6, 79.1, 46.8, 3.0], [83.3, 37.0, 5.3, 0.05], [37.4, 1.15, 0.39, 0.32], [2.35, 1.14, 0.53, 0.03], [1.02, 0.24, 0.08, 0.01]],
        unit="% de peticiones en frío", scale="coral", cell_fmt=lambda v: shown[v] + " %", row_title="Tasa de llegada",
        col_title="Inactividad tolerada antes de descartar la instancia", label_w=150,
        note="El arranque en frío no es un defecto del tráfico alto: a 30 peticiones por minuto es raro y a 0,05 es casi la regla. La tasa baja con ráfagas sufre más que la alta uniforme. Siete días de llegadas de Poisson, una petición por instancia a la vez y 0,2 s de servicio son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se352_dependencias() -> Fig:
    return grouped_bars(
        "Tiempo de arrancar un proceso Python que solo importa módulos de la biblioteca estándar",
        "Barras horizontales agrupadas con la mediana de 21 repeticiones: sin dependencias, 49 milisegundos en Windows y 30 en Ubuntu; con json y re, 104 y 38; añadiendo sqlite3, decimal, http.client y email, 220 y 90; añadiendo asyncio, ssl, unittest y xml.dom, 734 y 155. El tiempo crece con lo que se importa.",
        ["Sin dependencias", "json y re", "+ sqlite3, decimal, http.client, email", "+ asyncio, ssl, unittest, xml.dom"],
        [("Windows 11", [49, 104, 220, 734], "navy"), ("Ubuntu (WSL2)", [30, 38, 90, 155], "teal")],
        unit="ms (mediana de 21 repeticiones)", horizontal=True, label_w=300,
        note="El coste inicial de una función sin servidor crece con lo que carga, no con lo que ejecuta: quince veces más en Windows entre la primera y la última barra. Es el único tiempo de esta clase medido de verdad; el arranque de una plataforma gestionada incluye además descarga y aislamiento que no se midió.",
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
    return stacked_bars(
        "Una regla nueva entre las 127 posibles: ¿acerca internet a un destino sensible? (partiendo de 4 saltos)",
        "Barras apiladas horizontales con las 127 reglas que se pueden añadir a una red de 12 servicios: para la base de datos 1 regla la deja a un salto, 5 a dos, 9 a tres y 112 no cambian la distancia; para el almacén de secretos son 1, 3 y 7, y 116 no la cambian. Casi todo el ancho es de reglas sin efecto.",
        ["Base de datos (1, 5 y 9 reglas acercan; 112 no)", "Almacén de secretos (1, 3 y 7 reglas acercan; 116 no)"],
        [("Dejan a 1 salto", [1, 1], "coral"), ("A 2 saltos", [5, 3], "gold"), ("A 3 saltos", [9, 7], "navy"), ("Sin efecto", [112, 116], "grey")],
        unit="Reglas posibles (de 127)", horizontal=True, label_w=260, plot_h=200,
        note="Nueve de cada diez reglas nuevas no acercan nada, pero 15 de 127 sí acercan la base de datos, y una sola la deja directa. Menos saltos no significa más tráfico: significa menos barreras entre un atacante y el dato. Un salto es una regla permitida; no se modelaron puertos, protocolos ni reglas de salida.",
        note_kind="coral", foot=SINT)


def se353_permisos() -> Fig:
    return grouped_bars(
        "Pares acción-recurso concedidos y usados por rol, según el estilo de política (25 roles, 400 pares posibles)",
        "Barras horizontales agrupadas en escala logarítmica: un rol administrador concede 400 pares y usa 5,8; conceder el servicio completo da 80,8; las acciones usadas sobre todos los recursos, 32,4; solo los pares usados, 5,8. Lo usado es 5,8 en los cuatro estilos, por lo que lo concedido va de 69 veces lo usado a lo justo.",
        ["Administrador (* sobre *)", "Todo el servicio sobre *", "Acciones usadas sobre *", "Pares acción-recurso usados"],
        [("Pares concedidos", [400, 80.8, 32.4, 5.8], "coral"), ("Pares usados", [5.8, 5.8, 5.8, 5.8], "teal")],
        unit="Pares acción-recurso por rol (media)", horizontal=True, log=True, ticks=[1, 10, 100, 1000], label_w=240,
        note="Dos roles conservan una ruta de escalada incluso con el mínimo porque su uso real incluye la acción de adjuntar políticas: el menor privilegio mide lo concedido contra lo usado, no si lo usado es prudente. Los roles con ruta de escalada por estilo (25, 6, 2 y 2) están en la tabla. Los roles, el registro de uso y las 60 acciones son sintéticos; generar la política desde el registro supone que el registro fue completo.",
        note_kind="gold", foot=SINT)


def se353_detector() -> Fig:
    return grouped_bars(
        "Detector de secretos: precisión y exhaustividad de cinco reglas (80 secretos sintéticos y 180 señuelos)",
        "Barras horizontales agrupadas con la precisión y la exhaustividad de cinco reglas: entropía 3,5 da 25,8 y 75,0 por ciento, entropía 4,0 da 40,0 y 50,0, entropía 4,5 da 34,8 y 40,0, el nombre de la variable da 100 y 65,0, y nombre o entropía 4,5 da 50,8 y 77,5. Ninguna regla alcanza ambas por encima del 80.",
        ["Entropía ≥ 3,5", "Entropía ≥ 4,0", "Entropía ≥ 4,5", "Solo el nombre de la variable", "Nombre o entropía ≥ 4,5"],
        [("Precisión", [25.8, 40.0, 34.8, 100.0, 50.8], "gold"), ("Exhaustividad", [75.0, 50.0, 40.0, 65.0, 77.5], "teal")],
        unit="%", horizontal=True, label_w=230, decimals=1,
        note="Los secretos hexadecimales y las contraseñas con palabras tienen entropía menor que un resumen SHA-256 en base 64, así que ningún umbral separa bien. El contexto (el nombre de la variable) es más preciso y deja pasar a los que no lo tienen. Los hallados, falsos positivos y omitidos están en la tabla. Los 80 secretos y 180 señuelos los generé yo: las cifras describen estas reglas sobre estos datos, no un escáner real.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-354
def se354_deriva() -> Fig:
    return line_chart(
        "Deriva sobre 100 recursos con 10 ediciones en el código: lo que el plan muestra y lo que el siguiente apply revierte",
        "Líneas según cuántos recursos se alteran a mano (0, 5 y 20): un plan sin refrescar muestra 0, 0,49 y 2,01 de ellos; un plan refrescado muestra 0, 5 y 20; el siguiente apply revierte 0, 4,51 y 17,99 arreglos manuales. La brecha entre las dos primeras líneas es la deriva que el plan sin refrescar no ve.",
        [("Deriva que muestra el plan refrescado", [(0, 0, "", "t"), (5, 5.0, "5,0", "t"), (20, 20.0, "20,0", "l")], "navy"),
         ("Arreglos manuales que el siguiente apply revierte", [(0, 0, "", "t"), (5, 4.51, "4,51", "r"), (20, 17.99, "17,99", "b")], "coral"),
         ("Deriva que muestra el plan sin refrescar", [(0, 0, "0", "t"), (5, 0.49, "0,49", "b"), (20, 2.01, "2,01", "b")], "gold")],
        x_label="Recursos alterados fuera del código (k)", y_label="Recursos (media de 1 000 corridas)",
        x_ticks=[(0, "0"), (5, "5"), (20, "20")], y_ticks=[0, 5, 10, 15, 20], point_labels="none",
        note="Un plan sin refresco compara el código con un archivo de estado que supone cierto: ve la deriva por casualidad. Con refresco la ve toda, y entonces aplicar sin leerla revierte los arreglos de emergencia hechos a mano. Los cambios totales del plan (10, 14,5 y 28,0 refrescado) están en la tabla. El modelo es un diferenciador de diccionarios, no Terraform ni OpenTofu.",
        note_kind="coral", foot=SINT)


def se354_estado() -> Fig:
    return stacked_bars(
        "Escrituras simultáneas sobre un mismo archivo de estado: resultado de todas las intercalaciones de leer y escribir",
        "Barras apiladas horizontales al 100 por ciento con el resultado de todas las intercalaciones: con 2 aplicaciones sin bloqueo, 2 de 6 no pierden nada y 4 pierden el trabajo de una; con 3, 6 de 90 no pierden nada, 36 pierden el de una y 48 el de dos; con bloqueo solo quedan las ejecuciones en serie y ninguna pierde trabajo.",
        ["2 aplicaciones, sin bloqueo (6 intercalaciones)", "3 aplicaciones, sin bloqueo (90)", "2 aplicaciones, con bloqueo (2)", "3 aplicaciones, con bloqueo (6)"],
        [("Sin pérdida", [2, 6, 2, 6], "teal"), ("Pierde el trabajo de una", [4, 36, 0, 0], "gold"), ("Pierde el trabajo de dos", [0, 48, 0, 0], "coral")],
        unit="Intercalaciones posibles", horizontal=True, percent=True, label_w=270, plot_h=240,
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
