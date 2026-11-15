"""Figures for SE-337 to SE-342 (synthetic models with fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figures_part07_a import bars, tab

SINT = "Modelos sintéticos con semilla fija; resultados idénticos en Windows y Ubuntu (WSL2) salvo donde se indica."


# ---------------------------------------------------------------- SE-337
def se337_modelos() -> "Fig":
    rows = [
        ["Secuencial", "20 000", "20 000", "20 000"],
        ["Concurrente, un núcleo (la espera se solapa)", "2 090 (×9,57)", "18 010 (×1,11)", "20 000 (×1,00)"],
        ["Paralelo, 4 núcleos, cada tarea bloquea su núcleo", "5 000 (×4,00)", "5 000 (×4,00)", "5 000 (×4,00)"],
        ["Concurrente y 4 núcleos", "590 (×33,90)", "4 510 (×4,43)", "5 000 (×4,00)"],
    ]
    return tab("Tiempo total de 200 solicitudes según el modelo de ejecución (milisegundos virtuales)",
               "Tabla con el tiempo total de 200 solicitudes: con 10 ms de CPU y 90 de espera, el modelo concurrente de un núcleo baja de 20 000 a 2 090 ms y combinado con 4 núcleos a 590; con 100 ms de CPU y nada de espera solo ayuda el paralelismo, que da 5 000.",
               ["Modelo", "10 ms CPU + 90 ms espera", "90 ms CPU + 10 ms espera", "100 ms CPU + 0 espera"], rows, [380, 190, 190, 190], row_h=52, size=13,
               note="Concurrencia y paralelismo resuelven problemas distintos: solapar esperas ayuda cuando hay espera; repartir CPU ayuda cuando hay CPU. Un hilo que bloquea mientras espera gasta un núcleo entero. Es un planificador en tiempo virtual escrito por el autor, no una medición de Python ni de un sistema operativo.",
               note_kind="gold", foot=SINT)


def se337_bucle() -> "Fig":
    items = [("Sin ceder nunca", 1, "coral", "1 de 20 latidos"), ("Cede cada 50 000 vueltas", 5, "gold", "5 de 20"),
             ("Cede cada 10 000 vueltas", 20, "teal", "20 de 20"), ("Cede cada 1 000 vueltas", 20, "teal", "20 de 20")]
    return bars("Latidos de una tarea vecina emitidos antes de que termine un cálculo de 200 000 vueltas (asyncio)",
                "Barras con los latidos que una tarea vecina logra emitir mientras otra calcula en el mismo bucle de eventos: un latido de 20 si el cálculo nunca cede, 5 si cede cada 50 000 vueltas y 20 de 20 si cede cada 10 000 o cada 1 000.",
                items, 22, "Un bucle de eventos es un solo hilo: una tarea que no espera no deja pasar a ninguna otra. Se cuentan latidos en vez de milisegundos para que el resultado no dependa del equipo. Ceder más a menudo reparte mejor, a costa de más cambios de contexto que esta medida no cuenta.",
                label_w=300, width=980, note_kind="coral", foot=SINT)


def se337_amdahl() -> "Fig":
    rows = [
        ["5 %", "1,90", "3,48", "5,93", "9,14", "15,42", "20", "171"],
        ["10 %", "1,82", "3,08", "4,71", "6,40", "8,77", "10", "81"],
        ["25 %", "1,60", "2,29", "2,91", "3,37", "3,82", "4", "28"],
        ["50 %", "1,33", "1,60", "1,78", "1,88", "1,97", "2", "10"],
    ]
    return tab("Aceleración según la parte secuencial y el número de trabajadores (ley de Amdahl)",
               "Tabla de la aceleración teórica: con un 5 por ciento secuencial, 64 trabajadores dan 15,4 veces y el tope es 20; con un 25 por ciento, 64 trabajadores dan 3,8 y el tope es 4; con un 50 por ciento el tope es 2.",
               ["Parte secuencial", "2", "4", "8", "16", "64", "Tope", "Trabajadores para el 90 % del tope"], rows, [150, 90, 90, 90, 90, 90, 90, 220], row_h=48, size=13,
               note="Acercarse al tope exige muchos más trabajadores de los que parece: con un 5 % secuencial, 171 para llegar al 90 % de 20. La fórmula es 1 / (s + (1 − s) / n) y supone una carga fija sin costo de coordinación, que en la práctica añade un tramo secuencial más.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-338
def se338_contador() -> "Fig":
    rows = [
        ["Sin cerrojo: leer, sumar, escribir", "70", "6", "32", "32"],
        ["Con cerrojo alrededor de cada incremento", "6", "6", "0", "0"],
    ]
    return tab("Dos hilos suben un contador dos veces cada uno: todas las intercalaciones (valor correcto: 4)",
               "Tabla: de 70 intercalaciones de dos hilos que leen, suman y escriben dos veces, solo 6 terminan en 4; 32 terminan en 3 y 32 en 2 sin aviso. Con un cerrojo alrededor de cada incremento solo son posibles 6 intercalaciones y todas terminan en 4.",
               ["Variante", "Intercalaciones posibles", "Final = 4", "Final = 3", "Final = 2"], rows, [420, 190, 110, 110, 110], row_h=52, size=13,
               note="Cuatro hilos reales de CPython 3.12 con 100 000 incrementos sin cerrojo dieron 400 000 en tres ejecuciones: el defecto existe y no se vio. Que una prueba pase no demuestra que no haya carrera; enumerar o forzar el orden sí la expone.",
               note_kind="coral", foot=SINT)


def se338_interbloqueo() -> "Fig":
    rows = [
        ["Un hilo toma A y luego B; el otro B y luego A", "6", "4", "2 (33,3 %)", "Ambos agotan el tiempo (Windows) · uno completa (Ubuntu)"],
        ["Ambos toman A y luego B", "2", "2", "0", "—"],
    ]
    return tab("Dos hilos y dos cerrojos: ejecuciones del modelo de estados que terminan en interbloqueo",
               "Tabla: con orden opuesto de adquisición, de 6 ejecuciones del modelo 2 terminan en interbloqueo; con el mismo orden ninguna. Con tiempo límite y una barrera, en Windows ambos hilos fallan y en Ubuntu uno completa tras liberar el otro.",
               ["Orden de adquisición", "Ejecuciones", "Completan", "Interbloqueo", "Con barrera y tiempo límite de 0,3 s"], rows, [330, 100, 100, 140, 280], row_h=66, size=12,
               note="Un orden global de adquisición elimina el ciclo de espera. El tiempo límite no lo evita: lo convierte en un error, y quién falla primero depende de una carrera de temporización (distinta entre los dos sistemas). Recuperarse exige liberar lo ya tomado y poder repetir.",
               note_kind="teal", foot="Modelo exhaustivo determinista; la última columna es una ejecución real y no es reproducible entre sistemas.")


def se338_granularidad() -> "Fig":
    rows = [
        ["Un cerrojo global", "12,5 %", "12,5 %"],
        ["8 fragmentos (clave módulo 8)", "59,1 %", "65,6 %"],
        ["Un cerrojo por curso (40)", "73,8 %", "91,7 %"],
    ]
    return tab("Fracción del trabajo que avanza sin esperar con 8 trabajadores (20 000 rondas, 40 cursos)",
               "Tabla: con un cerrojo global avanza el 12,5 por ciento del trabajo; con 8 fragmentos, 59,1 si los cursos se piden con popularidad Zipf y 65,6 si son uniformes; con un cerrojo por curso, 73,8 y 91,7.",
               ["Cerrojo", "Cursos con popularidad Zipf 1,1", "Cursos uniformes"], rows, [380, 270, 220], row_h=48, size=13,
               note="Dividir el cerrojo ayuda hasta donde la distribución de las claves lo permite: con unos pocos cursos populares, los trabajadores siguen chocando en el mismo cerrojo. Cada ronda es una comparación de claves, no tiempo de ejecución; un cerrojo por curso tiene además un costo de memoria y de orden de adquisición.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-339
def se339_orden() -> "Fig":
    rows = [
        ["Órdenes globales posibles de 3 emisores con 2 mensajes cada uno", "90"],
        ["Órdenes globales distintos observados en 2 000 ejecuciones", "89"],
        ["Ejecuciones en que un emisor vio alterado su propio orden", "0"],
    ]
    return tab("Un buzón conserva el orden de cada emisor, no el orden entre emisores",
               "Tabla: tres emisores con dos mensajes cada uno pueden producir 90 órdenes globales; en 2 000 ejecuciones asyncio produjo 89 distintos, y ninguna alteró el orden de los mensajes de un mismo emisor.",
               ["Medida", "Resultado"], rows, [640, 200], row_h=48, size=13,
               note="El orden entre emisores no existe como propiedad del buzón: depende de quién llegó antes. Cualquier lógica que lo suponga funcionará hasta que cambie el reparto de los turnos. El retardo aleatorio de los emisores es una construcción del autor.",
               note_kind="teal", foot=SINT)


def se339_contrapresion() -> "Fig":
    rows = [
        ["Cola sin límite", "3 000", "0", "2 000", "2 000 turnos"],
        ["Cola de 100", "1 099", "1 901", "99", "99 turnos"],
        ["Cola de 10", "1 009", "1 991", "9", "9 turnos"],
    ]
    return tab("Un productor de 3 mensajes por turno y un consumidor de 1 por turno, durante 1 000 turnos",
               "Tabla: sin límite, la cola llega a 2 000 mensajes y el último espera 2 000 turnos; con una cola de 100 se aceptan 1 099 y se rechazan 1 901, con espera de 99 turnos; con una cola de 10 se aceptan 1 009 y la espera baja a 9.",
               ["Buzón", "Aceptados", "Rechazados", "En cola al final", "Espera del último"], rows, [250, 150, 150, 170, 190], row_h=48, size=13,
               note="La cola no crea capacidad: solo decide dónde espera el exceso. Sin límite, el exceso se convierte en latencia creciente y memoria; con límite se convierte en un rechazo que el emisor puede ver y manejar. Las tasas de 3 y 1 son supuestos del autor.",
               note_kind="coral", foot=SINT)


def se339_estructura() -> "Fig":
    rows = [
        ["TaskGroup: una hermana falla", "b y c se cancelan; el error llega a quien creó el grupo", "0 tareas vivas"],
        ["gather con tareas sueltas: una falla", "El error llega, pero b y c siguen y terminan «ok» sin dueño", "2 tareas vivas"],
        ["Cancelar una transferencia de 4 pasos, sin escudo", "3 de 6 instantes dejan estado a medias (por ejemplo, 25 + 30)", "3 de 6 incoherentes"],
        ["Cancelar la misma transferencia con escudo", "La transferencia termina siempre: 25 + 35 y «completado»", "0 de 6 incoherentes"],
    ]
    return tab("Quién es dueño de una tarea y qué ocurre al cancelarla (asyncio, CPython 3.12)",
               "Tabla: con TaskGroup el fallo de una tarea cancela a sus hermanas y el error se propaga; con gather las hermanas siguen vivas sin dueño; cancelar una transferencia de cuatro pasos sin protección deja tres de seis instantes con estado a medias y con un escudo ninguno.",
               ["Caso", "Qué ocurrió", "Resultado"], rows, [330, 400, 170], row_h=62, size=12,
               note="La concurrencia estructurada ata la vida de una tarea al bloque que la creó. No resuelve la atomicidad: una cancelación llega en un punto de espera y deja lo ya hecho; hay que decidir qué es indivisible. Pasos simulados con await de turno, no entrada y salida real.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-340
def se340_lamport() -> "Fig":
    rows = [
        ["Pares de eventos (300 eventos, 3 nodos)", "44 850", "—"],
        ["Pares con relación de causalidad (reloj vectorial)", "40 317", "89,9 %"],
        ["Pares concurrentes (reloj vectorial)", "4 533", "10,1 %"],
        ["Pares a los que Lamport da marcas distintas", "44 617", "99,5 %"],
        ["…de ellos, concurrentes de verdad", "4 300", "9,6 %"],
    ]
    return tab("Relojes de Lamport frente a relojes vectoriales: qué orden inventa cada uno",
               "Tabla: en 300 eventos de 3 nodos hay 44 850 pares; 4 533 son concurrentes según el reloj vectorial; el reloj de Lamport da marcas distintas a 44 617 pares y 4 300 de ellos son concurrentes, de modo que aparenta un orden que no existe.",
               ["Medida", "Cantidad", "Porcentaje"], rows, [560, 150, 150], row_h=44, size=13,
               note="Si a causó b, la marca de Lamport de a es menor; la inversa no vale: una marca menor no implica causa. Los relojes vectoriales distinguen causa de concurrencia a cambio de un vector por evento. Mensajes y turnos son una simulación del autor con semilla 340.",
               note_kind="gold", foot=SINT)


def se340_desfase() -> "Fig":
    items = [("Desfase ±50 ms", 0.0, "teal", "0 %"), ("Desfase ±75 ms", 5.08, "gold", "5,08 %"), ("Desfase ±100 ms", 11.94, "gold", "11,94 %"),
             ("Desfase ±250 ms", 31.47, "coral", "31,47 %"), ("Desfase ±1 000 ms", 44.41, "coral", "44,41 %")]
    return bars("Escrituras posteriores que pierden frente a una anterior cuando gana la marca de tiempo más alta",
                "Barras con el porcentaje de veces que una escritura causalmente posterior, hecha 100 ms después, pierde contra la anterior: 0 con desfase de 50 ms, 5,1 con 75, 11,9 con 100, 31,5 con 250 y 44,4 con 1 000 ms; con reloj híbrido, 0 en todos.",
                items, 11, "La pérdida empieza cuando el desfase entre relojes supera la mitad de la separación causal (50 ms de cada lado con 100 ms de separación). Un reloj híbrido que toma el máximo entre la hora local y la última marca vista dio 0 de 20 000 en todos los casos. Los desfases son supuestos del autor.",
                label_w=240, width=980, note_kind="coral", foot=SINT)


def se340_reloj() -> "Fig":
    rows = [
        ["Resolución de time.time()", "15,6 ms", "1 ns"],
        ["Resolución de time.monotonic()", "15,6 ms", "1 ns"],
        ["Retrocesos de monotonic en 2 000 000 de lecturas", "0", "0"],
        ["Duraciones negativas por un ajuste de −80 ms (1 de cada 500), reloj de pared", "205 de 100 000", "205 de 100 000"],
        ["Duraciones erróneas con reloj monotónico", "0", "0"],
    ]
    return tab("Reloj de pared y reloj monotónico en dos sistemas operativos",
               "Tabla: en Windows la resolución de los relojes de Python es de 15,6 ms y en Ubuntu de 1 ns; el reloj monotónico no retrocedió en 2 millones de lecturas; un ajuste simulado del reloj de pared produjo 205 duraciones erróneas en 100 000 mediciones y el monotónico ninguna.",
               ["Medida", "Windows 11", "Ubuntu (WSL2)"], rows, [500, 190, 190], row_h=60, size=12,
               note="Para medir cuánto duró algo se usa un reloj monotónico; para decir cuándo ocurrió, el de pared, sabiendo que se ajusta y que los nodos no coinciden. La resolución es una propiedad del sistema, no de Python: medir 5 ms con un reloj de 15,6 ms es inexacto. El ajuste de −80 ms es un supuesto.",
               note_kind="teal", foot="Resolución medida con time.get_clock_info; el ajuste de reloj es una simulación con semilla 3403.")


# ---------------------------------------------------------------- SE-341
def se341_agotado() -> "Fig":
    rows = [
        ["2 % · 2 % · 1 %", "4 986", "2 946 (59,1 %)", "2 040"],
        ["2 % · 2 % · 10 %", "13 649", "11 609 (85,1 %)", "2 040"],
        ["0,5 % · 5 % · 2 %", "7 389", "6 904 (93,4 %)", "485"],
    ]
    return tab("Cuando el cliente se rinde, ¿se ejecutó la operación? (100 000 solicitudes, tres perfiles de red)",
               "Tabla: con 2 por ciento de peticiones perdidas, 2 de respuestas perdidas y 1 de respuestas lentas, hay 4 986 tiempos agotados y en 59,1 por ciento de ellos la operación sí se ejecutó; con respuestas lentas del 10 por ciento sube al 85,1 y con pérdida de peticiones del 0,5 y de respuestas del 5, al 93,4.",
               ["Petición perdida · respuesta perdida · respuesta lenta", "Tiempos agotados", "La operación se ejecutó", "No se ejecutó"], rows, [360, 160, 220, 150], row_h=52, size=13,
               note="Desde fuera, un tiempo agotado cubre tres historias que el cliente no puede distinguir. Reintentar sin una clave de idempotencia duplica el efecto en la mayoría de los casos. Las tres probabilidades son supuestos del autor; la proporción cambia con ellas, el mecanismo no.",
               note_kind="coral", foot=SINT)


def se341_reintentos() -> "Fig":
    items = [("1 capa", 3, "teal", "3 intentos"), ("2 capas", 9, "gold", "9 intentos"), ("3 capas", 27, "coral", "27 intentos"), ("4 capas", 81, "coral", "81 intentos")]
    return bars("Intentos que recibe el servicio final por cada solicitud, si cada capa reintenta 2 veces y el servicio falla siempre",
                "Barras: con 2 reintentos por capa, el servicio del fondo recibe 3 intentos con una capa, 9 con dos, 27 con tres y 81 con cuatro por cada solicitud del usuario.",
                items, 6, "El factor es (1 + reintentos) elevado al número de capas. Con un presupuesto de reintentos del 10 % por capa, los intentos por solicitud con el servicio caído quedaron en 1,10 en vez de 3,00, y con un reintento con espera aleatoria el pico bajó de 1 000 a 159 reintentos por ventana de 10 ms.",
                label_w=190, width=980, note_kind="gold", foot=SINT)


def se341_detector() -> "Fig":
    rows = [
        ["150 ms", "32,34 %", "1 150 ms"],
        ["300 ms", "10,97 %", "1 300 ms"],
        ["600 ms", "2,25 %", "1 600 ms"],
        ["1 200 ms", "0,28 %", "2 200 ms"],
        ["2 400 ms", "0,02 %", "3 400 ms"],
    ]
    return tab("Detector de fallos por latidos cada 1 000 ms: tiempo límite, falsas sospechas y retraso en detectar",
               "Tabla: con un retardo de red lognormal de mediana 100 ms y un tiempo límite de 150 ms, el 32,3 por ciento de los latidos de un nodo sano parecen una falla; con 600 ms, el 2,25; con 2 400 ms, el 0,02, y el nodo caído se detecta 1 150, 1 600 y 3 400 ms después del último latido.",
               ["Tiempo límite", "Latidos de un nodo sano sospechosos", "Detección de un nodo caído"], rows, [200, 360, 300], row_h=44, size=13,
               note="No existe un tiempo límite que dé detección rápida y cero falsas sospechas: subirlo baja las falsas alarmas y retrasa la detección. La distribución del retardo (lognormal, mediana 100 ms, p99 de 795 ms) es un supuesto del autor, no una red medida.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-342
def se342_cp_ap() -> "Fig":
    rows = [
        ["Operaciones rechazadas", "97", "0"],
        ["Operaciones atendidas", "903", "1 000"],
        ["Lecturas obsoletas", "0", "89"],
        ["Escrituras aceptadas por el lado aislado", "0", "27"],
        ["Escrituras descartadas al reparar la partición", "0", "27"],
    ]
    return tab("Una réplica de tres aislada durante 300 de 1 000 operaciones: rechazar o aceptar",
               "Tabla: si la réplica aislada rechaza operaciones (CP), se rechazan 97 y no hay lecturas obsoletas ni escrituras perdidas; si acepta (AP), se atienden las 1 000, pero hay 89 lecturas obsoletas y 27 escrituras del lado aislado que se descartan al reparar.",
               ["Medida", "Rechazar (CP)", "Aceptar (AP)"], rows, [480, 190, 190], row_h=46, size=13,
               note="Durante la partición no se puede conservar a la vez la respuesta a todas las peticiones y la coherencia con lo último escrito. Rechazar cuesta disponibilidad visible; aceptar cuesta un trabajo de reparación que hay que definir antes. La carga y la duración de la partición son supuestos del autor.",
               note_kind="teal", foot=SINT)


def se342_cuorum() -> "Fig":
    rows = [
        ["1", "1", "No", "2 / 2", "99,9999 %"],
        ["2", "2", "Sí", "1 / 1", "99,97 %"],
        ["3", "1", "Sí", "0 / 2", "97,03 % al escribir"],
        ["1", "3", "Sí", "2 / 0", "99,9999 % al escribir"],
        ["2", "1", "No", "1 / 2", "99,97 % al escribir"],
    ]
    return tab("Tres réplicas: cuántas escrituras y lecturas confirma cada cuórum y si garantiza ver lo último",
               "Tabla de cuórums con tres réplicas: W=1 y R=1 tolera dos caídas pero no garantiza leer lo último; W=2 y R=2 sí lo garantiza y tolera una; W=3 y R=1 lo garantiza pero no tolera ninguna caída al escribir; W=2 y R=1 no lo garantiza.",
               ["W", "R", "Garantiza lectura reciente (W + R > N)", "Caídas toleradas al escribir / leer", "Disponibilidad con 1 % de caída por réplica"], rows, [60, 60, 340, 220, 260], row_h=52, size=12,
               note="La garantía sale de la intersección: toda lectura toca al menos una réplica que vio la última escritura cuando W + R > N. A cambio se pierde tolerancia a caídas en una de las dos operaciones. Sin reloj ni fallos parciales de red: es el modelo de conjuntos alcanzables, no un sistema real.",
               note_kind="gold", foot="Enumeración exacta de subconjuntos y cálculo binomial; sin simulación aleatoria.")


def se342_reparacion() -> "Fig":
    rows = [
        ["Contador de entregas (2 059 reales)", "1 048 (pierde 1 011)", "2 059 (contador por réplica)"],
        ["Conjunto de entregas (750 reales)", "500 (pierde 250)", "750 (unión)"],
        ["50 entregas borradas en un lado", "Se pierden o se conservan según la marca", "La unión simple las resucita (50)"],
    ]
    return tab("Reparar dos lados que divergieron: último escritor gana frente a tipos que se fusionan",
               "Tabla: tras una partición, el último escritor gana conserva 1 048 de 2 059 entregas contadas y 500 de 750 entregas distintas; un contador por réplica y una unión de conjuntos conservan 2 059 y 750, pero la unión simple resucita las 50 entregas que se habían borrado.",
               ["Dato", "Último escritor gana", "Tipo que se fusiona"], rows, [330, 270, 290], row_h=60, size=12,
               note="Fusionar sin perder nada es posible cuando la operación conmuta y se tolera su semántica: sumar sí, borrar no sin más información. Cada tipo fusionable fija qué conflictos resuelve. Las cantidades salen de semilla 3423; la latencia de 1 ms frente a 81 ms de replicar de forma síncrona entre regiones es un supuesto.",
               note_kind="coral", foot=SINT)


FIGURES = {
    "se-337-concurrente-o-paralelo.svg": se337_modelos,
    "se-337-bucle-que-no-cede.svg": se337_bucle,
    "se-337-ley-de-amdahl.svg": se337_amdahl,
    "se-338-intercalaciones-del-contador.svg": se338_contador,
    "se-338-interbloqueo-por-orden.svg": se338_interbloqueo,
    "se-338-granularidad-del-cerrojo.svg": se338_granularidad,
    "se-339-orden-por-emisor.svg": se339_orden,
    "se-339-contrapresion-del-buzon.svg": se339_contrapresion,
    "se-339-dueno-de-una-tarea.svg": se339_estructura,
    "se-340-lamport-y-vectores.svg": se340_lamport,
    "se-340-desfase-y-ultimo-escritor.svg": se340_desfase,
    "se-340-reloj-de-pared-y-monotonico.svg": se340_reloj,
    "se-341-que-significa-un-tiempo-agotado.svg": se341_agotado,
    "se-341-amplificacion-de-reintentos.svg": se341_reintentos,
    "se-341-detector-de-fallos.svg": se341_detector,
    "se-342-rechazar-o-aceptar.svg": se342_cp_ap,
    "se-342-cuorum-de-lectura-y-escritura.svg": se342_cuorum,
    "se-342-reparar-lo-divergente.svg": se342_reparacion,
}
