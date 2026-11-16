"""Figures for SE-259 to SE-264 (synthetic models with fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time is shown)."""
from __future__ import annotations

from figure_flow_rows import chain_rows
from figure_kit import Fig, grouped_bars, line_chart, scatter, stacked_bars
from figures_part07_a import bars, tab


SINT = "Modelo sintético con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2), salvo los tiempos indicados."
TIEMPO = "Tiempos medidos en un equipo (Windows 11, CPython 3.12.9); en Ubuntu (WSL2) la forma se repite con otras cifras."


# ---------------------------------------------------------------- SE-259
def se259_adopcion() -> Fig:
    days = [1, 7, 14, 30]
    ticks = [(d, str(d)) for d in days]
    data = [("Automática (35 % por día)", [34.6, 95.0, 99.9, 100], "teal"), ("Mixta (10 % por día)", [10.2, 52.2, 77.1, 95.6], "gold"),
            ("Manual (3 % por día)", [3.1, 18.6, 34.3, 59.2], "coral"), ("Empresarial con ventana (1 % por día)", [1.0, 6.8, 13.5, 26.2], "navy")]
    return line_chart(
        "Parte de la base instalada que ya tiene la versión nueva según el canal de actualización",
        "Líneas con el porcentaje de instalaciones con la versión nueva a 1, 7, 14 y 30 días según el canal: con actualización automática 34,6, 95,0, 99,9 y 100 por ciento; mixta 10,2, 52,2, 77,1 y 95,6; manual 3,1, 18,6, 34,3 y 59,2; empresarial con ventana 1,0, 6,8, 13,5 y 26,2.",
        [(name, [(d, v) for d, v in zip(days, vals)], kind) for name, vals, kind in data],
        x_label="Días desde la publicación", y_label="Instalaciones con la versión nueva (%)", x_ticks=ticks, y_ticks=[0, 25, 50, 75, 100],
        point_labels="last", decimals=1,
        note="Las probabilidades diarias son supuestos del autor, no medidas de ninguna tienda ni empresa. Lo transferible es la forma: con un canal lento las versiones coexisten durante meses y el servidor debe aceptar a todas.",
        note_kind="gold", foot=SINT)


def se259_retirar_campo() -> Fig:
    days = [7, 30, 90, 180]
    ticks = [(d, str(d)) for d in days]
    data = [("Automática (35 %)", [4.5, 0, 0, 0], "teal"), ("Mixta (10 %)", [47.1, 4.1, 0, 0], "gold"),
            ("Manual (3 %)", [80.9, 39.8, 6.2, 0.3], "coral"), ("Empresarial (1 %)", [93.2, 73.7, 40.2, 16.7], "navy")]
    return line_chart(
        "Clientes que siguen en la versión vieja cuando el servidor retira un campo",
        "Líneas con el porcentaje de clientes que aún usa la versión vieja al retirar un campo del servidor a los 7, 30, 90 y 180 días: con canal automático 4,5, 0, 0 y 0 por ciento; mixto 47,1, 4,1, 0 y 0; manual 80,9, 39,8, 6,2 y 0,3; empresarial 93,2, 73,7, 40,2 y 16,7.",
        [(name, [(d, v) for d, v in zip(days, vals)], kind) for name, vals, kind in data],
        x_label="Días hasta retirar el campo", y_label="Clientes en la versión vieja (%)", x_ticks=ticks, y_ticks=[0, 25, 50, 75, 100],
        point_labels="all", decimals=1,
        note="La fecha para retirar algo no se decide por el calendario sino por la fracción de clientes que aún lo necesita. Con un canal empresarial lento, a los 180 días queda una de cada seis instalaciones, y retirarlo las rompe.",
        note_kind="coral", foot=SINT)


def se259_bloques() -> Fig:
    items = [
        ("Cambia el 1 % del paquete (1 de 32 bloques)", 96.8, "teal", "ahorra 96,8 %"),
        ("Cambia el 10 % (4 de 32 bloques)", 87.3, "teal", "ahorra 87,3 %"),
        ("Cambia el 50 % (17 de 32 bloques)", 46.2, "gold", "ahorra 46,2 %"),
        ("Cambia el 100 % (32 de 32 bloques)", 0, "coral", "−1,3 % (más que el completo)"),
    ]
    return bars("Descargar solo los bloques de 64 KiB que cambiaron frente al paquete completo",
                "Barras: de un paquete sintético de 2 MiB que comprime a 1 194 660 bytes, descargar solo los bloques de 64 KiB cuya huella cambió ahorra 96,8 por ciento si cambia el 1 por ciento, 87,3 si cambia el 10, 46,2 si cambia el 50 y cuesta un 1,3 por ciento más si cambia todo.",
                items, 6.0, "El ahorro depende de cuántos bloques cambian, no de cuánto pesa el cambio. Compilar de nuevo suele desplazar contenido y mover muchos bloques a la vez: el experimento usa datos sintéticos con cambios contiguos, el caso más favorable.",
                label_w=440, width=1160, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-260
def se260_conjuntos() -> Fig:
    items = [
        ("Conjunto con marcas únicas (alta gana)", 0.78, "gold", "0,78 de 8"),
        ("Conjunto donde la baja es definitiva", 4.23, "coral", "4,23 de 8"),
        ("Último escritor gana, relojes alineados", 0, "teal", "0 de 8"),
        ("Último escritor gana, reloj 10 pasos adelantado", 0.88, "gold", "0,88 de 8"),
        ("Último escritor gana, reloj 40 pasos adelantado", 2.14, "coral", "2,14 de 8"),
    ]
    return bars("Elementos finales que difieren de lo que el usuario hizo en último lugar",
                "Barras: con ocho elementos, tres réplicas y 60 operaciones, un conjunto con marcas únicas difiere de la última intención en 0,78 elementos de media, un conjunto con baja definitiva en 4,23, y el último escritor gana en 0 con relojes alineados, 0,88 con diez pasos de desfase y 2,14 con cuarenta.",
                items, 80.0, "No hay una política de conflicto sin pérdida: el conjunto con marcas respeta lo que cada réplica vio y por eso una alta concurrente a una baja sobrevive; el último escritor acierta solo si los relojes dicen la verdad. Se elige la política por la intención que se está dispuesto a sacrificar.",
                label_w=470, width=1160, note_kind="gold", foot=SINT)


def se260_duplicados() -> Fig:
    ps = [0, 5, 15, 30]
    return line_chart(
        "Estado final errado tras aplicar 40 operaciones con duplicados y desorden",
        "Líneas con el porcentaje de 1000 repeticiones que terminan con el estado errado según la probabilidad de duplicar cada envío: sin identificador 0 por ciento sin duplicados, 87,1 con 5 por ciento de reenvíos y 100 con 15 y 30; con identificador de operación, 0 en todos los casos.",
        [("Aplicar sin identificador", [(p, v) for p, v in zip(ps, [0, 87.1, 100, 100])], "coral"),
         ("Aplicar con identificador de operación", [(p, 0) for p in ps], "teal")],
        x_label="Probabilidad de duplicar cada envío (%)", y_label="Estado final errado (%)", x_ticks=[(p, str(p)) for p in ps], y_ticks=[0, 25, 50, 75, 100],
        point_labels="all", decimals=1,
        note="Con un 5 % de duplicación casi toda sesión de 40 operaciones termina mal si la operación «sumar uno» se aplica dos veces. La idempotencia no es un detalle del servidor: es lo que permite reintentar sin miedo.",
        note_kind="coral", foot=SINT)


def se260_relojes() -> Fig:
    items = [
        ("Sin desfase", 0, "teal", "0,00 %"),
        ("Desfase de 1 unidad", 0, "teal", "0,00 %"),
        ("Desfase de 5 unidades", 0.78, "gold", "0,78 %"),
        ("Desfase de 30 unidades", 7.76, "coral", "7,76 %"),
    ]
    return bars("Pares de eventos de dos dispositivos ordenados al revés por un reloj de pared desfasado",
                "Barras: con eventos separados por 1 a 10 unidades de tiempo y un dispositivo adelantado, el porcentaje de pares de eventos mal ordenados es 0 con desfase 0 y 1, 0,78 por ciento con desfase 5 y 7,76 por ciento con desfase 30.",
                items, 40.0, "Ordenar por el reloj de pared funciona mientras el desfase sea menor que el intervalo entre eventos, y deja de funcionar sin avisar. Los relojes lógicos (contadores por réplica) no dependen de la hora: ordenan lo causal y dejan lo concurrente declarado como concurrente.",
                label_w=300, width=900, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-261
def se261_lista() -> Fig:
    return grouped_bars(
        "Construir las etiquetas de toda la lista o solo las 20 visibles",
        "Barras agrupadas en escala logarítmica con el tiempo en Windows de construir las etiquetas de toda la lista, 0,50, 14,57 y 103,2 milisegundos con 1000, 10 000 y 100 000 elementos, o solo una ventana de 20, 0,027, 0,030 y 0,031; la razón sube de 18 a 3370 veces.",
        ["1000 elementos", "10 000 elementos", "100 000 elementos"],
        [("Todos los elementos", [0.50, 14.57, 103.2], "coral"), ("Ventana de 20", [0.027, 0.030, 0.031], "teal")],
        unit="Tiempo (ms)", log=True, ticks=[0.01, 0.1, 1, 10, 100, 1000], plot_h=260,
        note="El tiempo de la ventana no depende del tamaño de la lista, y el tiempo completo crece con él (la razón es de 18, 485 y 3370 veces). Es un proxy de cadenas en Python: no mide dibujo en pantalla ni el coste de un marco real; en Ubuntu fueron 0,44, 3,14 y 42,9 ms completos y 0,006 a 0,012 ms para la ventana.",
        note_kind="gold", foot=TIEMPO)


def se261_sondeo() -> Fig:
    pts = [("Sondeo cada 30 s", 15.3, 1440000, "coral"), ("Sondeo cada 5 min", 157.1, 144000, "gold"), ("Sondeo cada 15 min", 407.1, 48000, "navy"),
           ("Lote cada hora", 1794.6, 12000, "grey"), ("Empuje (un despertar por evento)", 0, 24000, "teal")]
    return scatter(
        "Energía y retraso de enterarse de 48 eventos en un día según cómo despierta la radio",
        "Dispersión de la energía, en unidades arbitrarias y escala logarítmica, frente a la latencia media de cinco políticas para 48 eventos en 24 horas: el sondeo cada 30 segundos gasta 1 440 000 con 15,3 s; cada 5 minutos 144 000 con 157,1 s; cada 15 minutos 48 000 con 407,1 s; el lote cada hora 12 000 con 1794,6 s; el empuje 24 000 con latencia 0.",
        [(n, [(x, y)], k) for n, x, y, k in pts],
        x_label="Latencia media (s)", y_label="Energía (u. a.)", log_y=True, y_ticks=[10000, 100000, 1000000, 10000000],
        x_ticks=[(0, "0"), (500, "500"), (1000, "1000"), (1500, "1500"), (2000, "2000")], point_labels="none", plot_h=300,
        annotations=[(0, 24000, "Empuje: 24 000 u. a. y 48 despertares, sin retraso", 30, -52), (15.3, 1440000, "Sondeo cada 30 s: 2880 despertares", 40, 6)],
        note="Los costes (100 por despertar y hasta 400 de cola) son supuestos del autor, no mediciones de un radio ni de una batería. La comparación enseña la estructura: la energía depende del número de despertares (2880, 288, 96, 24 y 48), y el empuje solo despierta cuando hay algo.",
        note_kind="gold", foot="Modelo determinista; salidas idénticas en Windows y Ubuntu (WSL2).")


def se261_cache() -> Fig:
    items = [
        ("Caché de 1 % del catálogo (10 elementos)", 30.3, "coral", "30,3 %"),
        ("Caché de 5 % (50 elementos)", 56.8, "gold", "56,8 %"),
        ("Caché de 10 % (100 elementos)", 67.3, "gold", "67,3 %"),
        ("Caché de 25 % (250 elementos)", 80.4, "gold", "80,4 %"),
        ("Caché de 50 % (500 elementos)", 90.0, "teal", "90,0 %"),
        ("Caché de 100 % (1000 elementos)", 98.0, "teal", "98,0 %"),
    ]
    return bars("Tasa de aciertos de una caché LRU con accesos que siguen una distribución de Zipf",
                "Barras: con 1000 miniaturas y 50 000 accesos con exponente 1,1, una caché que guarda el 1 por ciento del catálogo acierta 30,3 por ciento, 5 por ciento acierta 56,8, 10 por ciento 67,3, 25 por ciento 80,4, 50 por ciento 90 y el catálogo completo 98 por ciento.",
                items, 6.5, "Con accesos concentrados, un 10 % de memoria da dos tercios de los aciertos; los últimos puntos cuestan mucho más. El 98 % del catálogo completo no llega a 100 % porque cada elemento falla la primera vez. La distribución es sintética: los accesos reales deben medirse.",
                label_w=420, width=1180, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-262
def se262_integridad() -> Fig:
    rows = [
        [("CRC-32", "plain"), ("32 768 de 32 768 volteos detectados", "teal"), ("Sí: lo recalcula cualquiera", "coral"), ("Detecta corrupción, no manipulación", "gold")],
        [("SHA-256 junto al paquete", "plain"), ("32 768 de 32 768 volteos detectados", "teal"), ("Sí: se publica junto al archivo", "coral"), ("Solo vale si llega por un canal distinto", "gold")],
        [("HMAC con clave compartida", "plain"), ("32 768 de 32 768 volteos detectados", "teal"), ("No, sin la clave", "teal"), ("La clave no puede ir dentro del cliente", "gold")],
    ]
    return chain_rows(
        "Qué detecta cada comprobación al voltear un bit y qué ocurre cuando alguien manipula el paquete",
        "Diagrama de flujo de tres comprobaciones sobre un paquete de 4096 bytes: las tres detectan los 32 768 volteos de un bit; un atacante puede recalcular el CRC y el SHA-256 publicado junto al paquete, pero no el HMAC sin la clave, que a su vez tiene el límite de que la clave no puede ir en el cliente.",
        ["Comprobación", "Corrupción accidental", "¿Puede recalcularla quien modifica?", "Límite"], rows, [170, 200, 230, 190], gap=26,
        note="Detectar corrupción accidental y detectar manipulación son problemas distintos. Una firma con clave privada que el cliente no posee añade lo que ni un CRC ni un hash resuelven: la procedencia. Aquí se usó HMAC con una clave de prueba por falta de criptografía asimétrica en la biblioteca estándar.",
        note_kind="gold", foot="Clave de prueba que no protege nada; salidas idénticas en Windows y Ubuntu (WSL2).")


def se262_rutas() -> Fig:
    items = [
        ("Comprobar solo el prefijo de la ruta", 6, "coral", "6 escapes, 0 bloqueos erróneos"),
        ("Rechazar rutas que contengan dos puntos", 2, "gold", "2 escapes, 1 bloqueo erróneo"),
        ("Normalizar y comparar con la raíz y un separador", 0, "teal", "0 escapes, 0 bloqueos erróneos"),
    ]
    return bars("Doce rutas de prueba (siete intentos de escape) contra tres comprobaciones de confinamiento",
                "Barras: de doce rutas con siete intentos de salir de la carpeta permitida, comprobar solo el prefijo deja pasar 6 escapes, rechazar los dos puntos deja pasar 2 y bloquea 1 ruta legítima, y normalizar la ruta y comparar con la raíz más un separador deja pasar 0.",
                items, 40.0, "La comprobación ingenua falla donde la mente no mira: la carpeta de nombre parecido, la barra invertida, la ruta absoluta. Normalizar y comparar es la regla correcta aquí, pero depende del sistema: en el disco real también hay enlaces simbólicos, que el experimento no cubre.",
                label_w=400, width=1180, note_kind="gold", foot="Doce rutas escritas por el autor; la lista no agota los trucos posibles. Resultados idénticos en Windows y Ubuntu.")


def se262_secretos() -> Fig:
    rows = [
        [("Texto plano", "plain"), ("Sí: búsqueda de «sk_test_»", "coral"), ("No hace falta nada más", "plain")],
        [("Base64", "plain"), ("Sí: decodificar candidatos", "coral"), ("Un patrón y una línea de código", "plain")],
        [("XOR con un byte fijo", "plain"), ("Sí: probar los 256 bytes", "coral"), ("256 intentos por candidato", "plain")],
        [("Partido en tres trozos", "plain"), ("No con una búsqueda ingenua", "gold"), ("Pero el programa lo reconstruye al ejecutarse", "plain")],
    ]
    return chain_rows(
        "Un secreto ficticio dentro del paquete de un cliente: qué lo encuentra",
        "Diagrama de flujo de cuatro formas de guardar un secreto ficticio en un paquete de cliente: texto plano, base64 y XOR con un byte se recuperan con una búsqueda simple; partido en tres trozos evita la búsqueda ingenua, pero el programa lo reconstruye al ejecutarse y por tanto también quien lo observe.",
        ["Cómo se guarda", "¿Lo recupera quien tiene el paquete?", "Esfuerzo"], rows, [240, 290, 290],
        note="Ofuscar sube el esfuerzo de una búsqueda, no impide que quien posee el paquete lo ejecute y observe. Todo secreto que el cliente necesita para funcionar es, en la práctica, público para quien tenga el cliente: la defensa es no ponerlo ahí.",
        note_kind="coral", foot="Secreto ficticio de ejemplo; sin valor real. Resultados idénticos en Windows y Ubuntu (WSL2).")


# ---------------------------------------------------------------- SE-263
def se263_sistemas() -> Fig:
    rows = [
        ["Separador de ruta", "\\", "/"],
        ["Salto de línea de os.linesep", "CR LF", "LF"],
        ["Abrir «notas.txt» si existe «Notas.txt»", "Sí", "No"],
        ["Nombres con :, ?, CON, punto final, etc. (de 7)", "4 aceptados", "7 aceptados"],
        ["Bytes de «é» con la codificación por defecto", "1 (cp1252)", "2 (UTF-8)"],
        ["Reemplazar o borrar un archivo abierto", "Rechazado", "Permitido"],
        ["Bit de ejecución visible en un .txt", "Sí", "No"],
    ]
    return tab("Siete diferencias medidas entre Windows 11 y Ubuntu bajo WSL2 con el mismo programa",
               "Tabla de siete comportamientos del mismo programa en Windows y en Ubuntu: separador de ruta, salto de línea, distinción de mayúsculas en nombres, nombres aceptados, codificación por defecto, borrar un archivo abierto y bit de ejecución.",
               ["Comportamiento", "Windows 11", "Ubuntu (WSL2)"], rows, [500, 250, 250], row_h=40, size=13,
               kinds=["plain", "gold", "teal"],
               note="La codificación de «é» depende del modo de Python en cada sistema: con -X utf8 Windows también da 2 bytes. El mapa de diferencias es parcial; solo contiene lo que se midió y nada de iOS, Android ni macOS.",
               note_kind="gold", foot="Python 3.12.9 (Windows) y 3.12.3 (Ubuntu); sin opciones de UTF-8 forzado.")


def se263_esfuerzo() -> Fig:
    items = [
        ("Coste con los pesos de partida (3 por adaptar, 8 por ausente)", 60, "grey", "60"),
        ("Percentil 5 con costes inciertos", 38.1, "teal", "38,1"),
        ("Mediana con costes inciertos", 71.3, "gold", "71,3"),
        ("Percentil 95 con costes inciertos", 104.6, "coral", "104,6"),
    ]
    return bars("Coste de adaptar 14 funciones a dos plataformas: una cifra frente a un intervalo",
                "Barras: con 14 funciones y 28 casillas, un coste de 3 por adaptar y 8 por ausente da 60 puntos; si adaptar vale entre 1 y 6 y ausente entre 4 y 16, 10 000 sorteos dan 38,1 en el percentil 5, 71,3 en la mediana y 104,6 en el percentil 95.",
                items, 5.5, "La cifra puntual de 60 queda por debajo de la mediana: elegir un solo coste hace parecer más barato lo que tiene cola larga. Solo 5 de las 14 funciones son iguales en ambas plataformas; el estado de cada casilla es una suposición del autor, no una auditoría de dos sistemas reales.",
                label_w=500, width=1180, note_kind="gold", foot=SINT)


def se263_adaptador() -> Fig:
    rows = [
        [("Sin mutación (adaptador falso correcto)", "plain"), ("Ninguna comprobación falla", "plain"), ("Pasa", "teal")],
        [("Guardar no sobrescribe un valor existente", "plain"), ("sobrescribir", "gold"), ("Detectada", "teal")],
        [("Borrar lo ausente lanza una excepción", "plain"), ("excepción KeyError", "gold"), ("Detectada", "teal")],
        [("Listar devuelve el orden inverso", "plain"), ("orden", "gold"), ("Detectada", "teal")],
        [("Leer lo ausente devuelve cadena vacía", "plain"), ("ausente y borrar", "gold"), ("Detectada", "teal")],
    ]
    return chain_rows(
        "Un contrato de cinco comprobaciones contra cuatro adaptadores de almacenamiento defectuosos",
        "Diagrama de flujo de un adaptador de almacenamiento falso y cuatro mutaciones: el contrato de cinco comprobaciones pasa el adaptador correcto y detecta las cuatro mutaciones, una de ellas con una excepción, otra con dos comprobaciones fallidas.",
        ["Adaptador", "Comprobaciones que fallan", "Resultado del contrato"], rows, [400, 230, 190],
        note="El mismo contrato se ejecuta contra el adaptador falso de las pruebas y contra el adaptador real de cada plataforma: si el falso no cumple el contrato, las pruebas del resto de la aplicación certifican un comportamiento que no existe. Cuatro mutaciones no agotan los defectos posibles.",
        note_kind="gold", foot="Mutaciones escritas por el autor; resultados idénticos en Windows y Ubuntu (WSL2).")


# ---------------------------------------------------------------- SE-264
def se264_canal() -> Fig:
    items = [
        ("Sin reintento ni identificador (40 envíos)", 0, "coral", "0 % correctos"),
        ("Reintento sin identificador (61,5 envíos)", 0, "coral", "0 % correctos"),
        ("Identificador sin reintento (40 envíos)", 0, "gold", "0 % correctos"),
        ("Reintento con identificador (59,1 envíos)", 100, "teal", "100 % correctos"),
    ]
    return bars("Sincronizar 40 operaciones por un canal que pierde el 20 %, duplica el 10 % y reordena",
                "Barras: en 1000 sincronizaciones sintéticas de 40 operaciones, ni el reintento solo, ni el identificador solo, ni nada dejan el estado correcto; combinar reintento e identificador lo deja correcto el 100 por ciento de las veces, con 59,1 envíos en media en lugar de 40.",
                items, 5.5, "Cada mecanismo por separado deja en cero la fracción de sesiones correctas: el reintento sin identificador suma las duplicaciones, y el identificador sin reintento pierde lo que no llega. El precio de la corrección es un 48 % más de envíos.",
                label_w=440, width=1160, note_kind="gold", foot=SINT)


def se264_servidor() -> Fig:
    items = [
        ("Sin clave de idempotencia", 44, "coral", "44 aplicadas de 30 pedidas"),
        ("Con clave de idempotencia", 30, "teal", "30 aplicadas de 30 pedidas"),
    ]
    return bars("Reintentos contra un servidor HTTP local que pierde cada tercera respuesta",
                "Barras: con 30 operaciones pedidas a un servidor local que aplica cada tercera petición y pierde su respuesta, reintentar sin clave de idempotencia aplica 44 operaciones y con la clave se aplican exactamente 30, con 44 peticiones en ambos casos.",
                items, 10.0, "El reintento ciego convierte 30 operaciones en 44: las 14 de más son respuestas perdidas que el cliente repitió. El servidor local no sufre latencia ni pérdida real de red; solo reproduce el patrón de la respuesta perdida tras aplicar.",
                label_w=300, width=1000, note_kind="coral", foot="Servidor en 127.0.0.1 con puerto efímero; 178 y 96 ms en Windows, 106 y 58 ms en Ubuntu (WSL2).")


def se264_paquete() -> Fig:
    return stacked_bars(
        "240 mutaciones de un paquete de proyecto: 136 detectadas y 104 que el validador no ve",
        "Barras apiladas horizontales con las 240 mutaciones de un paquete de once campos: el validador de presencia detecta 136, borrar o vaciar un campo comprobado, y no ve 104: 13 por borrar, 17 por vaciar y 18 por cambiar un campo ajeno al validador y 56 por cambiar el contenido de un campo comprobado a otro valor no vacío.",
        ["Borrar un campo ajeno al validador", "Vaciar un campo ajeno al validador", "Cambiar un campo ajeno al validador", "Cambiar un campo que sí comprueba", "Borrar o vaciar un campo comprobado"],
        [("No detectadas", [13, 17, 18, 56, 0], "coral"), ("Detectadas", [0, 0, 0, 0, 136], "teal")],
        unit="Mutaciones", horizontal=True, label_w=300,
        note="Un validador que solo comprueba presencia aprueba un paquete con evidencia absurda: no mira enlaces ni huella, y acepta cualquier valor no vacío en los campos que sí comprueba. Ese hueco no se cierra con más reglas de forma: la evidencia la revisa una persona que ejecuta lo que el paquete dice.",
        note_kind="gold", foot="Paquete y mutaciones sintéticos con semilla fija; resultados idénticos en Windows y Ubuntu (WSL2).")


FIGURES = {
    "se-259-adopcion-segun-el-canal.svg": se259_adopcion,
    "se-259-clientes-viejos-al-retirar-un-campo.svg": se259_retirar_campo,
    "se-259-descarga-completa-o-por-bloques.svg": se259_bloques,
    "se-260-conjuntos-replicados-frente-a-la-intencion.svg": se260_conjuntos,
    "se-260-duplicados-e-identificadores.svg": se260_duplicados,
    "se-260-relojes-de-pared-desfasados.svg": se260_relojes,
    "se-261-lista-completa-o-ventana.svg": se261_lista,
    "se-261-sondeo-empuje-y-lotes.svg": se261_sondeo,
    "se-261-tamano-de-cache-y-aciertos.svg": se261_cache,
    "se-262-quien-puede-recalcular-la-comprobacion.svg": se262_integridad,
    "se-262-confinamiento-de-rutas.svg": se262_rutas,
    "se-262-secretos-en-el-paquete-del-cliente.svg": se262_secretos,
    "se-263-diferencias-medidas-entre-windows-y-ubuntu.svg": se263_sistemas,
    "se-263-coste-de-adaptacion-con-incertidumbre.svg": se263_esfuerzo,
    "se-263-mutantes-de-un-adaptador.svg": se263_adaptador,
    "se-264-canal-con-fallos-y-estado-final.svg": se264_canal,
    "se-264-clave-de-idempotencia-con-servidor-real.svg": se264_servidor,
    "se-264-mutaciones-del-paquete.svg": se264_paquete,
}
