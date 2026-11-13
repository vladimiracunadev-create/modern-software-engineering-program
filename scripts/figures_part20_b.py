"""Figures for SE-247 to SE-252 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3 unless a time or a thread count is shown)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

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
    rows = [["0,50", "0,99 s", "1,00 s", "4,56 s", "7,64 s"], ["0,80", "3,96 s", "4,00 s", "13,71 s", "21,11 s"],
            ["0,90", "8,49 s", "9,00 s", "27,04 s", "39,22 s"], ["0,95", "18,04 s", "19,00 s", "55,60 s", "78,05 s"],
            ["1,05", "4 582 s", "no existe", "8 674 s", "9 080 s"]]
    return tab("Espera en la cola de un trabajador según la utilización (200 000 trabajos, servicio medio de 1 s)",
               "Tabla: con un trabajador y servicio exponencial de 1 segundo medio, la espera media es 0,99 s con utilización 0,50, 3,96 con 0,80, 8,49 con 0,90, 18,04 con 0,95 y 4 582 con 1,05; la teoría M/M/1 da 1, 4, 9 y 19 s y no existe equilibrio por encima de 1.",
               ["Utilización", "Espera media simulada", "Espera media teórica (M/M/1)", "Percentil 95", "Percentil 99"], rows, [160, 230, 250, 170, 170], row_h=44, size=13,
               note="Pasar de 0,90 a 0,95 duplica la espera media y el p99 pasa de 39 s a 78 s; por encima de 1 la cola crece sin tope mientras haya llegadas. La simulación supone llegadas aleatorias y servicios exponenciales, que casi ningún sistema real cumple exactamente.", note_kind="gold", foot=SINT)


def se247_venenoso() -> Fig:
    rows = [["Reintentar sin límite, al frente de la cola", "99 de 990", "0", "20 000 (tope del experimento)", "50 s (nunca termina)"],
            ["3 intentos y cola de muertos", "990 de 990", "10", "1 020", "509 s"],
            ["3 intentos, reintento al final de la cola", "990 de 990", "10", "1 020", "500 s"]]
    return tab("1 000 trabajos de 1 s con 10 venenosos y 2 trabajadores: qué política los aísla",
               "Tabla: si el trabajo venenoso se reintenta sin límite al frente de la cola, solo 99 de los 990 buenos terminan antes de agotar 20 000 ejecuciones; con tres intentos y cola de muertos, los 990 terminan y 10 trabajos quedan aislados.",
               ["Política", "Trabajos buenos completados", "En cola de muertos", "Ejecuciones", "Fin del último bueno"], rows, [370, 190, 130, 180, 170], row_h=64, size=12,
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
    rows = [["12 nombres de archivo hostiles", "escapan 3 en Windows y 2 en Ubuntu", "escapan 0; 6 rechazados"],
            ["10 MB de ceros comprimidos", "9,7 kB (1 027:1)", "tope de salida a 50 MB"],
            ["10 MB de texto repetido", "14,6 kB (685:1)", "tope de salida a 50 MB"],
            ["10 MB aleatorios", "10 003 kB (1:1)", "no comprime: el tamaño es el de entrada"],
            ["200 MB de ceros comprimidos", "194 kB", "lectura por trozos se detiene a 48 MB descomprimidos"]]
    return tab("Nombres de archivo hostiles y bombas de descompresión",
               "Tabla: de 12 nombres hostiles, el tratamiento ingenuo deja escapar 3 del directorio en Windows y 2 en Ubuntu y el estricto 0; 10 MB de ceros se comprimen a 9,7 kB (razón 1 027:1) y una bomba de 200 MB comprimida a 194 kB se detiene al llegar a 48 MB si se descomprime por trozos con tope.",
               ["Entrada", "Ingenuo / resultado", "Con límites"], rows, [330, 330, 330], row_h=56, size=12,
               note="La diferencia entre sistemas sale de que Windows trata la barra invertida como separador. El tamaño comprimido no dice nada del descomprimido: el límite debe aplicarse a la salida. Los nombres y las razones son sintéticos; no se probó ningún formato real de archivo comprimido ni un antivirus.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-249
def se249_cache() -> Fig:
    rows = [["50", "10 s", "34,3 %", "0,11 %"], ["50", "600 s", "34,4 %", "1,52 %"], ["500", "10 s", "57,8 %", "0,40 %"], ["500", "60 s", "64,3 %", "2,25 %"],
            ["500", "600 s", "65,0 %", "17,91 %"], ["2 500", "10 s", "57,8 %", "0,40 %"], ["2 500", "60 s", "76,3 %", "3,34 %"], ["2 500", "600 s", "87,9 %", "33,11 %"]]
    return tab(
        "Aciertos de caché y lecturas obsoletas según capacidad y TTL (200 000 lecturas, Zipf s = 1,0, 5 000 entregas)",
        "Tabla: con una caché LRU de 2 500 entradas y TTL de 600 segundos se acierta 87,9 por ciento pero 33,11 por ciento de las lecturas son obsoletas; con TTL de 10 segundos se acierta 57,8 por ciento con 0,40 por ciento obsoletas; con 50 entradas el TTL casi no cambia los aciertos.",
        ["Capacidad (entradas)", "TTL", "Aciertos", "Lecturas obsoletas"], rows, [260, 200, 220, 280], row_h=34, size=13,
        note="Subir el TTL compra aciertos con obsolescencia: de 60 a 600 s con 2 500 entradas el acierto sube 11,6 puntos y las lecturas obsoletas se multiplican por 10. Con capacidad pequeña el TTL no importa: manda la capacidad. La popularidad Zipf y el cambio cada 300 a 900 s son supuestos del autor.",
        note_kind="gold", foot=SINT)


def se249_estampida() -> Fig:
    items = [("Sin protección · Windows (3 ejecuciones)", 189, "coral", "169 a 189 consultas"), ("Sin protección · Ubuntu (3 ejecuciones)", 129, "coral", "46 a 129"),
             ("Single-flight · ambos sistemas (6 ejecuciones)", 1, "teal", "1")]
    return bars("Consultas al origen cuando una clave caliente expira y 200 hilos la piden a la vez",
                "Barras: sin protección, 200 hilos que encuentran la caché vacía generan entre 169 y 189 consultas al origen en Windows y entre 46 y 129 en Ubuntu; con una única carga en vuelo (single-flight) el origen recibe 1 consulta en las seis ejecuciones.",
                items, 2.4, "El número sin protección depende del reparto de hilos del sistema operativo y cambia entre ejecuciones; el valor con single-flight no. Esperar al líder reduce la carga del origen a cambio de que todos esperen su latencia (50 ms aquí) y de que un líder lento o fallido bloquee a los demás.",
                label_w=400, width=1020, note_kind="gold", foot="Hilos reales con una carga simulada de 50 ms; los recuentos sin protección no son deterministas.")


def se249_limitadores() -> Fig:
    rows = [["Ventana fija 100 / 10 s", "200 aceptadas", "954 de 1 000"], ["Ventana deslizante 100 / 10 s", "100", "920"],
            ["Cubeta de fichas, 10/s, capacidad 20", "39", "966"], ["Cubeta de fichas, 10/s, capacidad 100", "119", "1 000"]]
    return tab("Cuatro limitadores ante 200 solicitudes junto al cambio de ventana y ante tráfico uniforme",
               "Tabla: ante 200 solicitudes agrupadas en dos segundos alrededor del cambio de ventana, la ventana fija de 100 por 10 segundos acepta 200, la deslizante 100, la cubeta de capacidad 20 acepta 39 y la de capacidad 100 acepta 119; con tráfico legítimo uniforme aceptan 954, 920, 966 y 1 000 de 1 000.",
               ["Limitador", "Ráfaga de 200 en el borde de la ventana", "Tráfico uniforme de 1 000 en 100 s"], rows, [380, 330, 300], row_h=48, size=13,
               note="La ventana fija permite el doble del límite nominal en dos segundos. La deslizante es exacta pero rechaza más tráfico legítimo agrupado (920 frente a 966). La cubeta permite una ráfaga acotada por su capacidad y mantiene la tasa media. Ningún limitador distingue a un atacante de un cliente legítimo sin una identidad fiable.", note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-250
def se250_liveness() -> Fig:
    rows = [["Liveness y readiness consultan la base de datos", "4", "80 s", "el proceso se reinicia aunque no tenga fallo propio"],
            ["Liveness local; readiness consulta la base de datos", "0", "0 s", "la instancia sale del reparto pero no se reinicia"]]
    return tab("La base de datos cae 120 s de 600: qué hace cada diseño de sondeos",
               "Tabla: si el sondeo de vida consulta la base de datos, una caída de 120 segundos provoca 4 reinicios y 80 segundos sin proceso; si el sondeo de vida es local y solo el de disponibilidad consulta la base, hay 0 reinicios.",
               ["Diseño de sondeos", "Reinicios", "Segundos sin proceso", "Consecuencia"], rows, [380, 130, 200, 300], row_h=64, size=12,
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
    rows = [["D1 sin comprobar dueño (BOLA)", "—", "—", "detecta"], ["D2 asignación masiva", "—", "—", "detecta"], ["D3 inyección SQL", "—", "—", "detecta"],
            ["D4 GET con efecto", "—", "—", "detecta"], ["D5 error con detalles internos", "—", "—", "—"], ["D6 cuerpo sin tope", "—", "—", "detecta"],
            ["D7 validación laxa", "—", "detecta", "—"], ["D8 sin idempotencia", "—", "—", "detecta"], ["D9 estados inconsistentes", "—", "detecta", "—"],
            ["D10 token sin verificar", "—", "—", "detecta"]]
    return tab("Qué suite detecta cada defecto reintroducido en la API reparada",
               "Tabla de 10 defectos y 3 suites: la suite de camino feliz no detecta ninguno; la de contrato detecta la validación laxa y los códigos de estado inconsistentes; la adversaria detecta siete; el error con detalles internos no lo detecta ninguna cuando se reintroduce solo.",
               ["Defecto reintroducido", "Camino feliz (5 pruebas)", "Contrato (8)", "Adversaria (9)"], rows, [380, 220, 190, 200], row_h=34, size=12,
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
    rows = [["Filas de entrega", "1 184", "1 000"], ["Entregas duplicadas", "184", "0"], ["Entregas sin trabajo encolado", "109", "0"], ["Notas duplicadas", "110", "0"], ["Entregas sin nota", "109", "0"]]
    return tab("1 000 entregas con caídas, respuestas perdidas y trabajos entregados dos veces",
               "Tabla: con 8 por ciento de caídas antes de encolar, 8 por ciento de respuestas perdidas y 10 por ciento de trabajos entregados dos veces, el diseño ingenuo termina con 184 entregas duplicadas, 109 sin trabajo, 110 notas duplicadas y 109 entregas sin nota; el contractual con clave, outbox y efecto idempotente termina con 0 en todo.",
               ["Resultado", "Diseño ingenuo", "Contractual (clave + outbox + efecto idempotente)"], rows, [380, 220, 400], row_h=44, size=13,
               note="El diseño contractual cumple los cuatro invariantes bajo este modelo de fallos, no ante cualquier fallo: no se simularon corrupción de disco, relojes desfasados ni dos réplicas escribiendo a la vez. Las probabilidades de fallo son supuestos del autor.", note_kind="teal", foot=SINT)


def se252_alertas() -> Fig:
    rows = [["Caída total de 10 min", "14,6 %", "a los 4 min", "nunca"], ["5 % de errores durante 6 h", "18,3 %", "nunca", "a los 215 min"],
            ["Degradación lenta del 0,8 % sin corregir 10 días", "63,3 %", "nunca", "nunca"]]
    return tab("SLO de 99,5 % a 30 días: presupuesto consumido y alertas por tasa de consumo",
               "Tabla: una caída total de 10 minutos consume 14,6 por ciento del presupuesto de error y la alerta rápida (quema mayor a 14,4) salta a los 4 minutos; 5 por ciento de errores durante 6 horas consume 18,3 y solo la alerta lenta salta, a los 215 minutos; una degradación del 0,8 por ciento durante 10 días consume 63,3 y ninguna de las dos alertas salta.",
               ["Incidente simulado", "Presupuesto consumido", "Alerta rápida (14,4× en 1 h y 5 min)", "Alerta lenta (6× en 6 h y 30 min)"], rows, [330, 200, 250, 250], row_h=64, size=12,
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
