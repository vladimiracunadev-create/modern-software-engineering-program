"""Figures for SE-247 to SE-252 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time or a thread count is shown)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, scatter
from figures_part07_a import bars

SINT = "Datos sintéticos, semilla fija; idénticos en Windows y Ubuntu (WSL2), salvo los tiempos y los recuentos de hilos indicados."


# ---------------------------------------------------------------- SE-247
def se247_duplicados() -> Fig:
    items = [("Caída 5 % · handler ingenuo", 117, "coral", "117 efectos duplicados"),
             ("Caída 5 % · handler idempotente", 0, "teal", "0"),
             ("Caída 20 % · handler ingenuo", 478, "coral", "478"),
             ("Caída 20 % · handler idempotente", 0, "teal", "0")]
    return bars("Efectos duplicados de 2 000 trabajos cuando el trabajador cae tras ejecutar y antes de confirmar",
                "Barras: con una cola de visibilidad, si el trabajador cae después de ejecutar el efecto y antes de confirmar, un handler ingenuo duplica 117 efectos con 5 por ciento de caídas y 478 con 20 por ciento; un handler idempotente deja 0 duplicados con las mismas 2 117 y 2 478 ejecuciones.",
                items, 0.95, "La cola entrega al menos una vez: 2 117 y 2 478 ejecuciones para 2 000 trabajos. El efecto exactamente una vez no lo da la cola, lo da el handler al registrar el trabajo ya hecho. La probabilidad de caída es un parámetro del autor.",
                label_w=330, width=1000, note_kind="coral", foot=SINT)


def se247_espera() -> Fig:
    return line_chart(
        "Espera en la cola de un trabajador según la utilización (200 000 trabajos, servicio medio de 1 s)",
        "Líneas en escala logarítmica con la espera según la utilización: la media simulada es 0,99 s con 0,50, 3,96 con 0,80, 8,49 con 0,90, 18,04 con 0,95 y 4 582 con 1,05; la teoría M/M/1 da 1, 4, 9 y 19 s y no existe por encima de 1; el percentil 95 va de 4,56 a 55,60 s hasta 0,95 y es 8 674 s con 1,05.",
        [("Media simulada", [(0.50, 0.99, "", "b"), (0.80, 3.96, "", "b"), (0.90, 8.49, "", "b"), (0.95, 18.04, "", "b"), (1.05, 4582, "4 582", "b")], "teal"),
         ("Media teórica M/M/1", [(0.50, 1.00, "", "t"), (0.80, 4.00, "", "t"), (0.90, 9.00, "", "t"), (0.95, 19.00, "", "t")], "gold"),
         ("Percentil 95", [(0.50, 4.56), (0.80, 13.71), (0.90, 27.04), (0.95, 55.60), (1.05, 8674, "8 674", "t")], "coral")],
        x_label="Utilización del trabajador", y_label="Espera (s)", log_y=True,
        x_ticks=[(0.50, "0,50"), (0.80, "0,80"), (0.90, "0,90"), (0.95, "0,95"), (1.05, "1,05")], y_ticks=[0.1, 1, 10, 100, 1000, 10000], decimals=2,
        note="Pasar de 0,90 a 0,95 duplica la espera media y el p99 pasa de 39 s a 78 s; por encima de 1 la cola crece sin tope mientras haya llegadas. La simulación supone llegadas aleatorias y servicios exponenciales, que casi ningún sistema real cumple exactamente.", note_kind="gold", foot=SINT)


def se247_venenoso() -> Fig:
    return grouped_bars(
        "1 000 trabajos de 1 s con 10 venenosos y 2 trabajadores: buenos que terminan según la política",
        "Barras con los trabajos buenos completados de 990: reintentar sin límite al frente de la cola completa 99 antes de agotar 20 000 ejecuciones; con tres intentos y cola de muertos, o con tres intentos y reintento al final de la cola, completa los 990 y deja 10 trabajos venenosos aislados.",
        ["Reintentar sin límite, al frente de la cola", "3 intentos y cola de muertos", "3 intentos, reintento al final de la cola"],
        [("Trabajos buenos completados", [99, 990, 990], "teal")],
        unit="Trabajos buenos completados (de 990)", horizontal=True, label_w=290, ref_lines=[(990, "990")],
        note="Un solo mensaje que siempre falla puede acaparar a los trabajadores. Limitar intentos y apartarlo convierte un fallo del sistema en una cola que una persona revisa. El 1 % de venenosos y la duración de 1 s son supuestos del autor.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-248
def se248_memoria() -> Fig:
    items = [("Leer todo en memoria", 64.01, "coral", "64,01 MiB"), ("Trozos de 4 KiB", 0.02, "teal", "0,02 MiB"),
             ("Trozos de 64 KiB", 0.13, "teal", "0,13 MiB"), ("Trozos de 1 MiB", 2.01, "teal", "2,01 MiB")]
    return bars("Pico de memoria de Python al calcular el SHA-256 de un archivo sintético de 64 MiB",
                "Barras: leer el archivo de 64 MiB entero provoca un pico de 64,01 MiB; leerlo por trozos de 4 KiB, 64 KiB o 1 MiB produce picos de 0,02, 0,13 y 2,01 MiB con el mismo SHA-256, 4fca9c72bd87.",
                items, 6.5, "El hash es idéntico; lo que cambia es la memoria que cada solicitud retiene. Con 50 cargas simultáneas el diseño que lee todo retiene 3,2 GiB solo en búfer. Los tiempos (190 a 420 ms) fueron del orden del mismo valor para cualquier tamaño de trozo y varían por equipo.",
                label_w=300, width=1000, note_kind="gold", foot="Medido con tracemalloc en CPython 3.12.9 (Windows) y 3.12.3 (Ubuntu); los picos coinciden con diferencias de 0,01 MiB.")


def se248_reanudable() -> Fig:
    items = [("Reiniciar desde cero (866 caídas)", 12421.2, "coral", "12 421 MiB"), ("Reanudar, trozos de 1 MiB", 101.5, "teal", "101,5 MiB"),
             ("Reanudar, trozos de 5 MiB", 117.5, "teal", "117,5 MiB"), ("Reanudar, trozos de 25 MiB", 301.5, "gold", "301,5 MiB")]
    return bars("Datos enviados para subir 100 MiB con una caída cada 15 MiB en media",
                "Barras: reiniciar la subida tras cada caída envía 12 421 MiB para entregar 100 MiB; reanudar por trozos de 1 MiB envía 101,5 MiB, de 5 MiB 117,5 MiB y de 25 MiB 301,5 MiB.",
                items, 0.04, "El trozo fija cuánto se repite tras una caída: uno pequeño repite poco pero exige más confirmaciones; uno grande repite más. Un archivo truncado sin Content-Length ni huella no se detecta; con SHA-256 sí.",
                label_w=320, width=1000, note_kind="gold", foot="Simulación con semilla 248; la tasa de caída es un supuesto del autor, no una medición de redes reales.")


def se248_nombres() -> Fig:
    return grouped_bars(
        "Bombas de descompresión: razón de compresión de tres entradas de 10 MB",
        "Barras horizontales en escala logarítmica con la razón de compresión de 10 MB de entrada: 1 027 a 1 para ceros, 685 a 1 para texto repetido y 1 a 1 para datos aleatorios; el tope de salida a 50 MB y la lectura por trozos detienen la bomba de 200 MB comprimida a 194 kB al llegar a 48 MB.",
        ["10 MB de ceros (9,7 kB)", "10 MB de texto repetido (14,6 kB)", "10 MB aleatorios (10 003 kB)"],
        [("Razón de compresión", [1027, 685, 1], "coral")],
        unit="Razón de compresión (veces)", horizontal=True, log=True, label_w=270,
        note="Los 12 nombres de archivo hostiles y la bomba de 200 MB están en la tabla. La diferencia entre sistemas sale de que Windows trata la barra invertida como separador. El tamaño comprimido no dice nada del descomprimido: el límite debe aplicarse a la salida. Los nombres y las razones son sintéticos; no se probó ningún formato real de archivo comprimido ni un antivirus.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-249
def se249_cache() -> Fig:
    return scatter(
        "Aciertos de caché y lecturas obsoletas según capacidad y TTL (200 000 lecturas, Zipf s = 1,0, 5 000 entregas)",
        "Puntos con los aciertos y las lecturas obsoletas de una caché LRU: con 50 entradas, 34,3 por ciento de aciertos con 0,11 de obsoletas a 10 s y 34,4 con 1,52 a 600 s; con 500, de 57,8 y 0,40 a 65,0 y 17,91; con 2 500 y TTL de 600 s, 87,9 por ciento de aciertos pero 33,11 de lecturas obsoletas.",
        [("50 entradas", [(34.3, 0.11, "10 s", "b"), (34.4, 1.52, "600 s", "t")], "gold"),
         ("500 entradas", [(57.8, 0.40, "10 s", "t"), (64.3, 2.25, "60 s", "b"), (65.0, 17.91, "600 s", "t")], "teal"),
         ("2 500 entradas", [(57.8, 0.40, " ", "t"), (76.3, 3.34, "60 s", "b"), (87.9, 33.11, "600 s", "l")], "coral")],
        x_label="Aciertos de caché (%)", y_label="Lecturas obsoletas (%)", decimals=2, y_zero=True,
        note="Subir el TTL compra aciertos con obsolescencia: de 60 a 600 s con 2 500 entradas el acierto sube 11,6 puntos y las lecturas obsoletas se multiplican por 10. Con capacidad pequeña el TTL no importa: manda la capacidad. La popularidad Zipf y el cambio cada 300 a 900 s son supuestos del autor.", note_kind="gold", foot=SINT)


def se249_estampida() -> Fig:
    items = [("Sin protección · Windows (3 ejecuciones)", 189, "coral", "169 a 189 consultas"), ("Sin protección · Ubuntu (3 ejecuciones)", 129, "coral", "46 a 129"),
             ("Single-flight · ambos sistemas (6 ejecuciones)", 1, "teal", "1")]
    return bars("Consultas al origen cuando una clave caliente expira y 200 hilos la piden a la vez",
                "Barras: sin protección, 200 hilos que encuentran la caché vacía generan entre 169 y 189 consultas al origen en Windows y entre 46 y 129 en Ubuntu; con una única carga en vuelo (single-flight) el origen recibe 1 consulta en las seis ejecuciones.",
                items, 2.4, "El número sin protección depende del reparto de hilos del sistema operativo y cambia entre ejecuciones; el valor con single-flight no. Esperar al líder reduce la carga del origen a cambio de que todos esperen su latencia (50 ms aquí) y de que un líder lento o fallido bloquee a los demás.",
                label_w=400, width=1020, note_kind="gold", foot="Hilos reales con una carga simulada de 50 ms; los recuentos sin protección no son deterministas.")


def se249_limitadores() -> Fig:
    return grouped_bars(
        "Solicitudes aceptadas de una ráfaga de 200 junto al cambio de ventana",
        "Barras con las solicitudes aceptadas de una ráfaga de 200 agrupadas en dos segundos alrededor del cambio de ventana: la ventana fija de 100 por 10 segundos acepta 200, la deslizante 100, la cubeta de fichas de capacidad 20 acepta 39 y la de capacidad 100 acepta 119; el límite pretendido es 100.",
        ["Ventana fija 100 / 10 s", "Ventana deslizante 100 / 10 s", "Cubeta de fichas, 10 por s, capacidad 20", "Cubeta de fichas, 10 por s, capacidad 100"],
        [("Aceptadas de 200", [200, 100, 39, 119], "gold")],
        unit="Solicitudes aceptadas (de 200)", horizontal=True, label_w=290, ref_lines=[(100, "límite 100")],
        note="La ventana fija permite el doble del límite nominal en dos segundos. La deslizante es exacta pero rechaza más tráfico legítimo agrupado (920 frente a 966). La cubeta permite una ráfaga acotada por su capacidad y mantiene la tasa media. Ningún limitador distingue a un atacante de un cliente legítimo sin una identidad fiable.", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-250
def se250_liveness() -> Fig:
    return grouped_bars(
        "La base de datos cae 120 s de 600: segundos sin proceso según el diseño de sondeos",
        "Barras con los segundos sin proceso: si el sondeo de vida consulta la base de datos hay 4 reinicios y 80 segundos sin proceso; si el sondeo de vida es local y solo el de disponibilidad consulta la base hay 0 reinicios y 0 segundos.",
        ["Liveness y readiness consultan la base (4 reinicios)", "Liveness local; readiness consulta la base (0 reinicios)"],
        [("Segundos sin proceso", [80, 0], "coral")],
        unit="Segundos sin proceso (de 600)", horizontal=True, label_w=310,
        note="Un reinicio no arregla una dependencia externa: la pierde la caché y añade 20 s de arranque a la caída. Los sondeos cada 5 s, el umbral de 3 fallos y el arranque de 20 s son parámetros del autor, no valores por defecto de una plataforma.", note_kind="coral", foot=SINT)


def se250_apagado() -> Fig:
    items = [("Apagado abrupto (la conexión se corta)", 30, "coral", "30 fallidas, 0 completadas"), ("Apagado con drenaje", 0, "teal", "0 fallidas, 30 completadas")]
    return bars("30 solicitudes en curso de 200 ms cuando se detiene un servidor local real",
                "Barras: al detenerlo de forma abrupta, 30 de 30 solicitudes en curso fallan; al dejar de aceptar conexiones nuevas y esperar a las que están en curso, 0 fallan y 30 se completan.",
                items, 11, "El drenaje exige tres pasos en orden: salir del reparto de tráfico, dejar de aceptar y esperar con un plazo máximo. Si el orchestrator mata el proceso antes de que termine el plazo, el drenaje no basta; el tiempo de gracia debe superar la solicitud más larga esperable.",
                label_w=360, width=1000, note_kind="gold", foot="Servidor HTTP de la biblioteca estándar; el apagado abrupto se simula cortando las conexiones, no matando el proceso.")


def se250_calentamiento() -> Fig:
    items = [("Tráfico desde el arranque (1 800 servidas)", 35.6, "coral", "35,6 %"), ("Readiness tras 30 s de calentamiento (1 200)", 15.1, "gold", "15,1 %"),
             ("Readiness por umbral de aciertos del 60 % (1 080)", 12.7, "teal", "12,7 %")]
    return bars("Solicitudes más lentas que 250 ms en una instancia nueva con la caché fría",
                "Barras: una instancia que recibe tráfico desde el arranque sirve 35,6 por ciento de solicitudes por encima de 250 ms; con readiness tras 30 segundos de calentamiento 15,1; con readiness por umbral de 60 por ciento de aciertos 12,7.",
                items, 11, "Esperar no elimina las solicitudes lentas: las traslada a otras instancias y retrasa la capacidad. El umbral por aciertos se adapta a la velocidad real del calentamiento; el tiempo fijo no. La curva de calentamiento lineal en 60 s es un supuesto del autor.",
                label_w=440, width=1040, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-251
def se251_matriz() -> Fig:
    return heatmap(
        "Qué suite detecta cada defecto reintroducido en la API reparada",
        "Mapa de calor de diez defectos y tres suites: la suite de camino feliz no detecta ninguno; la de contrato detecta la validación laxa y los estados inconsistentes; la adversaria detecta siete; el error con detalles internos no lo detecta ninguna cuando se reintroduce solo.",
        ["D1 sin comprobar dueño (BOLA)", "D2 asignación masiva", "D3 inyección SQL", "D4 GET con efecto", "D5 error con detalles internos",
         "D6 cuerpo sin tope", "D7 validación laxa", "D8 sin idempotencia", "D9 estados inconsistentes", "D10 token sin verificar"],
        ["Camino feliz (5 pruebas)", "Contrato (8)", "Adversaria (9)"],
        [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0], [0, 0, 1]],
        unit="Defecto detectado = 1, no detectado = 0", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "detecta" if v else "no", cell_h=34, label_w=250,
        note="El defecto D5 queda dormido: solo se manifiesta si algo provoca un error interno, y con la inyección corregida nada lo provoca. Una suite no prueba el camino de error si no sabe cómo llegar a él. Contado sobre una API de laboratorio, no sobre un producto.", note_kind="coral", foot=SINT)


def se251_inyeccion() -> Fig:
    items = [("SQL concatenado · cargas que filtran filas ajenas", 3, "coral", "3 de 12"), ("SQL concatenado · cargas que provocan error", 2, "gold", "2 de 12"),
             ("SQL parametrizado · filtran o provocan error", 0, "teal", "0 de 12")]
    return bars("12 cargas de inyección contra una búsqueda con SQL concatenado y con parámetros",
                "Barras: contra la búsqueda con SQL construido por concatenación, 3 de 12 cargas devuelven filas de otros usuarios y 2 provocan errores del motor; con consulta parametrizada ninguna hace ninguna de las dos cosas.",
                items, 60, "Los parámetros separan datos de instrucciones: la carga se trata siempre como texto. Esto cubre la inyección en valores; no cubre nombres de columna ni de orden, que no se pueden parametrizar y se validan contra una lista cerrada.",
                label_w=430, width=1020, note_kind="gold", foot=SINT)


def se251_suites() -> Fig:
    items = [("Camino feliz · API con 10 defectos", 0, "coral", "0 de 5 fallan"), ("Contrato · API con 10 defectos", 7, "gold", "7 de 8"),
             ("Adversaria · API con 10 defectos", 7, "gold", "7 de 9"), ("Las tres suites · API reparada", 0, "teal", "0 de 22")]
    return bars("Pruebas que fallan contra la API con los 10 defectos a la vez",
                "Barras: sobre la API con los 10 defectos, la suite de camino feliz tiene 0 pruebas fallidas de 5, la de contrato 7 de 8 y la adversaria 7 de 9; sobre la API reparada ninguna de las 22 pruebas falla.",
                items, 40, "Un conjunto verde de camino feliz no dice nada sobre la seguridad ni la coherencia: la API vulnerable lo supera. Que la API reparada pase todas las pruebas solo significa que las pruebas conocidas no fallan; no hay prueba de que no existan defectos que nadie escribió.",
                label_w=370, width=1000, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-252
def se252_caidas() -> Fig:
    return grouped_bars(
        "1 000 entregas con caídas, respuestas perdidas y trabajos entregados dos veces",
        "Barras horizontales con los resultados tras 1 000 entregas con 8 por ciento de caídas antes de encolar, 8 por ciento de respuestas perdidas y 10 por ciento de trabajos entregados dos veces: el diseño ingenuo termina con 1 184 filas, 184 entregas duplicadas, 109 sin trabajo encolado, 110 notas duplicadas y 109 entregas sin nota; el contractual con clave, outbox y efecto idempotente termina con 1 000 filas y 0 en todo lo demás.",
        ["Filas de entrega (esperadas: 1 000)", "Entregas duplicadas", "Entregas sin trabajo encolado", "Notas duplicadas", "Entregas sin nota"],
        [("Diseño ingenuo", [1184, 184, 109, 110, 109], "coral"), ("Contractual (clave + outbox + efecto idempotente)", [1000, 0, 0, 0, 0], "teal")],
        unit="Entregas o notas", horizontal=True, label_w=250,
        note="El diseño contractual cumple los cuatro invariantes bajo este modelo de fallos, no ante cualquier fallo: no se simularon corrupción de disco, relojes desfasados ni dos réplicas escribiendo a la vez. Las probabilidades de fallo son supuestos del autor.", note_kind="teal", foot=SINT)


def se252_alertas() -> Fig:
    return grouped_bars(
        "SLO de 99,5 % a 30 días: presupuesto de error consumido por incidente",
        "Barras horizontales con el presupuesto de error consumido por tres incidentes: una caída total de 10 minutos consume 14,6 por ciento y la alerta rápida salta a los 4 minutos; 5 por ciento de errores durante 6 horas consume 18,3 y solo la alerta lenta salta, a los 215 minutos; una degradación del 0,8 por ciento durante 10 días consume 63,3 y ninguna alerta salta.",
        ["Caída total de 10 min (alerta rápida a los 4 min)", "5 % de errores durante 6 h (alerta lenta a los 215 min)", "Degradación de 0,8 % durante 10 días (ninguna alerta)"],
        [("Presupuesto consumido", [14.6, 18.3, 63.3], "coral")],
        unit="Presupuesto de error consumido (%)", horizontal=True, decimals=1, label_w=330, ref_lines=[(100, "100 %")],
        note="La degradación lenta quema 1,7 veces el presupuesto por unidad de tiempo: por debajo de ambos umbrales y, sin embargo, consume casi dos tercios del mes. Hace falta una tercera ventana (por ejemplo 3 días con quema mayor a 1). Escenarios y umbrales sintéticos.", note_kind="gold", foot=SINT)


def se252_deriva() -> Fig:
    items = [("Solo existencia de rutas", 64, "coral", "64 de 189"), ("+ códigos de estado", 99, "gold", "99"),
             ("+ campos obligatorios", 156, "gold", "156"), ("+ campos extra (esquema cerrado)", 189, "teal", "189")]
    return bars("Mutaciones de la implementación que detecta cada capa de la comprobación de conformidad (12 rutas)",
                "Barras: de 189 mutaciones reales de la implementación de 12 rutas, comprobar solo que existan las rutas detecta 64, añadir códigos de estado 99, añadir campos obligatorios 156 y añadir campos extra (esquema cerrado) las 189.",
                items, 2.6, "Cada capa atrapa cambios que la anterior no ve; el mutante equivalente (11 de 200) no cambia nada y no cuenta. Un contrato conforme con la implementación no prueba que el contrato describa lo que los consumidores necesitan.",
                label_w=320, width=1000, note_kind="teal", foot=SINT)


FIGURES = {
    "se-247-efectos-duplicados-en-la-cola.svg": se247_duplicados,
    "se-247-espera-segun-la-utilizacion.svg": se247_espera,
    "se-247-mensaje-venenoso.svg": se247_venenoso,
    "se-248-memoria-segun-como-se-lee.svg": se248_memoria,
    "se-248-subida-reanudable.svg": se248_reanudable,
    "se-248-nombres-hostiles-y-bombas.svg": se248_nombres,
    "se-249-aciertos-y-obsolescencia.svg": se249_cache,
    "se-249-estampida-de-cache.svg": se249_estampida,
    "se-249-limitadores-en-el-borde-de-la-ventana.svg": se249_limitadores,
    "se-250-sondeo-de-vida-que-consulta-la-base.svg": se250_liveness,
    "se-250-apagado-abrupto-o-con-drenaje.svg": se250_apagado,
    "se-250-calentamiento-y-readiness.svg": se250_calentamiento,
    "se-251-defecto-que-detecta-cada-suite.svg": se251_matriz,
    "se-251-inyeccion-sql.svg": se251_inyeccion,
    "se-251-api-vulnerable-frente-a-suites.svg": se251_suites,
    "se-252-caidas-inyectadas-en-el-flujo.svg": se252_caidas,
    "se-252-alertas-por-tasa-de-consumo.svg": se252_alertas,
    "se-252-deteccion-de-deriva-del-contrato.svg": se252_deriva,
}
