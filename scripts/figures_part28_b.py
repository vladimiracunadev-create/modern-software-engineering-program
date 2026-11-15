"""Figures for SE-343 to SE-348 (synthetic models with fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figures_part07_a import bars, tab

SINT = "Modelos sintéticos con semilla fija; resultados idénticos en Windows y Ubuntu (WSL2) salvo donde se indica."


# ---------------------------------------------------------------- SE-343
def se343_lideres() -> "Fig":
    rows = [
        ["Sin partición", "1", "1"],
        ["Partición en 2 y 3", "2", "1"],
        ["Partición en 1 y 4", "2", "1"],
        ["Partición en 1, 1 y 3", "3", "1"],
        ["Partición en 2, 2 y 1", "3", "0 (nadie tiene mayoría)"],
        ["Las 15 biparticiones posibles de 5 nodos", "2 en las 15", "nunca más de 1"],
    ]
    return tab("Cinco nodos y una partición: líderes que se creen legítimos según la regla de elección",
               "Tabla: con la regla «el identificador mayor que veo vivo», una partición de cinco nodos produce dos o tres líderes a la vez, y las 15 biparticiones posibles producen dos; con la regla de mayoría nunca hay más de uno y en un reparto 2, 2, 1 no hay ninguno.",
               ["Situación", "Regla «el mayor que veo»", "Regla de mayoría"], rows, [380, 250, 260], row_h=44, size=13,
               note="La mayoría resuelve el cerebro dividido a cambio de disponibilidad: el grupo sin mayoría no elige a nadie. Dos mayorías siempre se cruzan en algún nodo, y de ahí sale la seguridad. Es un modelo de conjuntos de nodos, sin mensajes ni tiempo.",
               note_kind="teal", foot="Enumeración exacta de particiones; sin simulación aleatoria.")


def se343_cerco() -> "Fig":
    rows = [
        ["1 s", "1 de 10 000"],
        ["2 s", "73 de 10 000"],
        ["4 s", "854 de 10 000"],
        ["8 s", "2 918 de 10 000"],
    ]
    return tab("Un titular del arrendamiento que se pausa más de 10 s y escribe después de que otro tomó su lugar",
               "Tabla: con pausas de media 1, 2, 4 y 8 segundos, un arrendamiento de 10 segundos caduca antes de que el titular escriba en 1, 73, 854 y 2 918 de 10 000 tareas; sin testigo de cerco el almacén acepta esas 849 escrituras tardías de la corrida de media 4 s y con testigo rechaza las 849.",
               ["Pausa media del titular", "Tareas cuyo arrendamiento caduca antes de escribir"], rows, [320, 500], row_h=44, size=13,
               note="En la corrida de media 4 s hay 849 escrituras de un titular caducado (otra semilla da 854 caducados): sin testigo el almacén las acepta todas, con un número de cerco creciente las rechaza todas. El arrendamiento solo no basta porque el titular no sabe que caducó. Las pausas exponenciales son un supuesto del autor.",
               note_kind="coral", foot=SINT)


def se343_plazos() -> "Fig":
    rows = [
        ["150 ms (sin aleatoriedad)", "51,0 (no converge)", "0,0 %", "7 650 ms"],
        ["150 a 175 ms", "51,0 (no converge)", "0,0 %", "7 863 ms"],
        ["150 a 200 ms", "25,5", "3,1 %", "4 057 ms"],
        ["150 a 250 ms", "4,20", "24,0 %", "725 ms"],
        ["150 a 300 ms", "2,49", "40,3 %", "461 ms"],
        ["150 a 450 ms", "1,54", "64,7 %", "333 ms"],
    ]
    return tab("Elección de líder entre cinco nodos con plazos aleatorios (retardo de mensajes hasta 25 ms)",
               "Tabla: con plazos de elección sin aleatoriedad o con menos de 25 ms de dispersión no se llega a un líder en 50 rondas; con plazos entre 150 y 300 ms se necesitan 2,49 rondas de media y 461 ms, y entre 150 y 450 ms, 1,54 rondas y 333 ms.",
               ["Plazo de elección", "Rondas medias (tope 50)", "Líder en la primera ronda", "Tiempo medio hasta líder"], rows, [250, 230, 230, 200], row_h=44, size=13,
               note="La dispersión de los plazos debe ser mayor que el retardo de los mensajes para que un candidato gane antes de que otro se presente. Con mayor dispersión se tarda más en empezar una elección y menos en terminarla. Es un modelo simplificado inspirado en Raft, no Raft.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-344
def se344_entrega() -> "Fig":
    rows = [
        ["Aplicar y luego confirmar (al menos una vez)", "1 053", "+53 duplicados"],
        ["Confirmar y luego aplicar (como mucho una vez)", "950", "−50 perdidos"],
        ["Aplicar y registrar la clave en una transacción", "1 000", "0"],
    ]
    return tab("Contar 1 000 entregas cuando el consumidor se cae el 5 % de las veces en el peor punto",
               "Tabla: aplicar y luego confirmar cuenta 1 053 de 1 000 por los mensajes reentregados; confirmar y luego aplicar cuenta 950 y pierde 50; aplicar y registrar la clave de mensaje visto en la misma transacción cuenta exactamente 1 000.",
               ["Orden de las operaciones", "Total contado", "Diferencia con 1 000"], rows, [480, 190, 220], row_h=48, size=13,
               note="El proceso exactamente una vez no existe entre dos sistemas: lo que se logra es efecto único sobre el estado porque aplicar y recordar viven en una sola transacción. El 5 % de caídas es un supuesto del autor; el estado es una base SQLite real en memoria.",
               note_kind="teal", foot=SINT)


def se344_retencion() -> "Fig":
    rows = [
        ["1 minuto", "9 639 de 20 000 (48,20 %)"],
        ["1 hora", "550 de 20 000 (2,75 %)"],
        ["24 horas", "6 de 20 000 (0,03 %)"],
        ["7 días", "0 de 20 000"],
    ]
    return tab("Duplicados que llegan cuando la clave de idempotencia ya se olvidó y se ejecutan otra vez",
               "Tabla: con retraso de duplicados de cola larga (mediana 55 s, p99 9 209 s), una retención de 1 minuto deja pasar el 48,2 por ciento de los duplicados, una de 1 hora el 2,75, una de 24 horas el 0,03 y una de 7 días ninguno.",
               ["Retención de la clave", "Duplicados reejecutados"], rows, [300, 520], row_h=44, size=13,
               note="La retención de claves es una decisión de negocio sobre cuánto tarda en llegar el último duplicado posible, no un detalle de almacenamiento. Además, 615 de 640 reutilizaciones de una clave con otro cuerpo habrían devuelto la respuesta ajena sin la huella del cuerpo. La distribución lognormal es un supuesto del autor.",
               note_kind="gold", foot=SINT)


def se344_salida() -> "Fig":
    rows = [
        ["Anexar al archivo de salida", "Determinista", "209", "9", "0"],
        ["Anexar al archivo de salida", "Con valor aleatorio", "214", "14", "13"],
        ["Escribir por clave de tarea", "Determinista", "200", "0", "0"],
        ["Escribir por clave de tarea", "Con valor aleatorio", "200", "0", "0"],
    ]
    return tab("200 tareas, el 5 % se reintenta tras escribir y antes de confirmar: qué queda en la salida",
               "Tabla: anexar al archivo deja 9 filas duplicadas si la tarea es determinista y 14 si devuelve un valor aleatorio, con 13 claves que quedan con valores distintos; escribir por clave de tarea deja siempre 200 filas y ningún duplicado.",
               ["Cómo se escribe", "Tarea", "Filas", "Duplicadas", "Claves con valores distintos"], rows, [280, 190, 100, 130, 220], row_h=48, size=13,
               note="Escribir por clave convierte el reintento en una sobrescritura del mismo resultado; anexar convierte cada reintento en una fila más y, si la tarea no es determinista, en dos verdades. La tasa del 5 % y los valores son sintéticos; no se usó ningún sistema de procesamiento distribuido.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-345
def se345_balanceo() -> "Fig":
    rows = [
        ["Turnos rotativos", "13,3", "316,8", "535,1"],
        ["Aleatorio", "19,9", "361,6", "632,4"],
        ["Dos opciones al azar, la menos cargada", "4,5", "95,4", "203,6"],
        ["Menos conexiones (estado global)", "2,7", "52,6", "188,5"],
    ]
    return tab("10 servidores, 200 000 solicitudes de tamaño Pareto y 85 % de carga: tiempo hasta terminar (unidades de tiempo; tamaño medio 3,0)",
               "Tabla: con turnos rotativos el percentil 99 es 316,8 unidades y con reparto aleatorio 361,6; con dos opciones al azar baja a 95,4 y con la de menos conexiones a 52,6, con una carga del 85 por ciento y tamaños de cola pesada.",
               ["Política", "Mediana", "Percentil 99", "Percentil 99,9"], rows, [420, 140, 160, 170], row_h=48, size=13,
               note="Repartir por turnos equilibra el número de solicitudes, no el trabajo: un tamaño de cola pesada deja un servidor atascado mientras otros esperan. Mirar solo dos servidores logra casi todo el beneficio sin estado global. Los tamaños Pareto (forma 1,5) y el 85 % son supuestos del autor.",
               note_kind="gold", foot=SINT)


def se345_conmutacion() -> "Fig":
    rows = [
        ["Asíncrona", "6,11", "1,0 ms", "1,0 ms"],
        ["Semisíncrona (una réplica confirma)", "0", "21,1 ms", "63,6 ms"],
        ["Síncrona (dos réplicas confirman)", "0", "27,5 ms", "75,3 ms"],
    ]
    return tab("Conmutar tras la caída del primario con 200 escrituras por segundo: pérdida y costo de confirmar",
               "Tabla: con replicación asíncrona se pierden en promedio 6,11 escrituras ya confirmadas al conmutar y la confirmación tarda 1 ms; con una réplica síncrona no se pierde ninguna y la confirmación tarda 21,1 ms de mediana y 63,6 ms en el percentil 99.",
               ["Replicación", "Escrituras confirmadas perdidas", "Confirmación (mediana)", "Confirmación (p99)"], rows, [350, 210, 170, 170], row_h=52, size=12,
               note="La pérdida es el trabajo que el cliente ya consideró guardado y que la réplica nunca vio. Pagarlo en latencia lo evita. El retraso de 30 ms y el tiempo de ida y vuelta lognormal son supuestos del autor, no una red medida.",
               note_kind="coral", foot=SINT)


def se345_reparto() -> "Fig":
    rows = [
        ["5 000 escrituras de las entregas más recientes", "674 a 578 por fragmento (8 fragmentos)", "5 000 en un fragmento"],
        ["Consulta de 100 claves consecutivas", "8 fragmentos", "1 fragmento"],
        ["Consulta de 10 000 claves consecutivas", "8 fragmentos", "1 fragmento"],
        ["Consulta de 50 000 claves consecutivas", "8 fragmentos", "5 fragmentos"],
    ]
    return tab("Repartir por hash o por rango de fecha: dónde caen las escrituras nuevas y cuántos fragmentos toca una consulta",
               "Tabla: con reparto por hash, las 5 000 escrituras más recientes se reparten entre 8 fragmentos, de 578 a 674 cada uno, pero toda consulta de un tramo de fechas toca los 8; con rangos fijos, las 5 000 caen en un solo fragmento y una consulta de 100 claves toca uno.",
               ["Operación", "Reparto por hash", "Reparto por rango fijo"], rows, [380, 280, 230], row_h=60, size=12,
               note="Cada reparto abarata una pregunta y encarece la otra: el hash esparce la escritura y dispersa la lectura por rango; el rango agrupa la lectura y acumula la escritura nueva en un fragmento. Ocho fragmentos y 100 000 claves son sintéticos; el hash es MD5 solo por su reparto, no por seguridad.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-346
def se346_reintentos() -> "Fig":
    rows = [
        ["0 %", "100,0 % · 1,00", "100,0 % · 1,00", "100,0 % · 1,00"],
        ["20 %", "80,5 % · 1,00", "99,9 % · 1,24", "99,9 % · 1,24"],
        ["50 %", "50,1 % · 1,00", "93,1 % · 1,90", "93,1 % · 1,90"],
        ["80 %", "20,1 % · 1,00", "54,1 % · 3,05", "9,9 % · 0,53"],
    ]
    return tab("Éxito y llamadas por solicitud según el fallo inyectado y la estrategia del cliente (80 solicitudes por turno)",
               "Tabla de éxito y llamadas por solicitud: con 20 por ciento de fallo inyectado, los reintentos suben el éxito de 80,5 a 99,9 por ciento con 1,24 llamadas; con 80 por ciento de fallo los reintentos llegan a 54,1 con 3,05 llamadas y el interruptor baja el éxito a 9,9 con 0,53 llamadas.",
               ["Fallo inyectado", "Sin reintentos", "Con reintentos (máx. 4)", "Con interruptor"], rows, [180, 220, 240, 220], row_h=44, size=13,
               note="Un experimento de caos busca el punto donde la estrategia deja de proteger: aquí, entre 50 % y 80 %, los reintentos triplican la carga sobre una dependencia ya enferma y el interruptor sacrifica éxito para dejarla respirar. El servicio, su capacidad de 100 y el exceso son un modelo del autor.",
               note_kind="gold", foot=SINT)


def se346_planificador() -> "Fig":
    rows = [
        ["1,0 (cualquier hilo, siempre)", "84,35 %", "1", "2"],
        ["0,3", "40,34 %", "2", "6"],
        ["0,1", "15,41 %", "5", "17"],
        ["0,03 (hilos casi siempre seguidos)", "4,84 %", "14", "57"],
    ]
    return tab("El mismo defecto en 1 620 de 1 680 intercalaciones: cuántas ejecuciones al azar hacen falta según el planificador",
               "Tabla: aunque 1 620 de las 1 680 intercalaciones de tres solicitudes violan el cupo, un planificador que cambia de hilo con probabilidad 0,03 solo lo expone en el 4,84 por ciento de las ejecuciones, con mediana de 14 ejecuciones hasta verlo y 57 en el percentil 95.",
               ["Probabilidad de cambiar de hilo en cada paso", "Ejecuciones que fallan", "Ejecuciones hasta el primer fallo (mediana)", "Percentil 95"], rows, [330, 190, 260, 140], row_h=56, size=12,
               note="No todas las intercalaciones son igual de probables: los planificadores reales mantienen un hilo en marcha un buen rato. Por eso una pasada limpia dice poco y una semilla guardada permite repetir exactamente el mismo orden (misma semilla, misma traza, comprobado).",
               note_kind="coral", foot=SINT)


def se346_plan() -> "Fig":
    rows = [
        ["Campo ausente o vacío", "50 de 50"],
        ["Alcance del 100 % del tráfico", "33 de 33"],
        ["Condición de aborto inalcanzable", "29 de 29"],
        ["Hipótesis sin umbral medible", "35 de 35"],
        ["Resultado copiado de otro entorno", "0 de 29"],
        ["Reversión nunca ensayada", "0 de 24"],
    ]
    return tab("Linter de planes de caos sobre 200 mutaciones: 147 detectadas",
               "Tabla: un linter de forma detecta 147 de 200 mutaciones de un plan de experimento de caos, todas las de campos ausentes, alcance total, aborto inalcanzable e hipótesis sin umbral, y ninguna de las 53 que dejan los campos plausibles: resultados copiados de otro entorno y reversiones nunca ensayadas.",
               ["Mutación", "Detectadas"], rows, [560, 200], row_h=44, size=13,
               note="Las dos que el linter no ve son las que convierten un experimento en teatro: un resultado que no se obtuvo y una reversión que nunca se probó. Las reglas se escribieron conociendo las mutaciones, así que cada tipo sale al 0 % o al 100 %; la exactitud sobre planes reales es desconocida.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-347
def se347_carrera() -> "Fig":
    rows = [
        ["Intercalaciones de 2 solicitudes (3 pasos cada una)", "20"],
        ["…con dos entregas aceptadas con cupo 1", "18 (90 %)"],
        ["Calendario fallido al azar, con 4 solicitudes y ruido", "40 pasos"],
        ["Calendario mínimo que sigue fallando (reducción por bloques)", "6 pasos"],
    ]
    return tab("Reproducir la carrera del cupo y reducir el calendario hasta lo esencial",
               "Tabla: de las 20 intercalaciones de dos solicitudes que leen, comprueban y escriben el cupo, 18 aceptan dos entregas con cupo 1; un calendario fallido de 40 pasos con ruido se redujo a 6 pasos que siguen fallando.",
               ["Medida", "Resultado"], rows, [600, 220], row_h=48, size=13,
               note="Un fallo reproducible se reduce eliminando pasos mientras siga fallando: lo que queda es la explicación (leer, comprobar, leer, escribir, comprobar, escribir). El ruido son pasos ajenos al cupo y el calendario sale de la semilla 347; con hilos del sistema operativo no se controla el orden.",
               note_kind="teal", foot=SINT)


def se347_parcial() -> "Fig":
    rows = [
        ["Corte antes de cada uno de los 5 pasos, sin reintento", "4 de 5", "Solo el corte antes del primero deja todo intacto"],
        ["Respuesta perdida tras cada paso, reintento del flujo completo", "5 de 5", "Cupo, entrega, penalización y aviso se repiten"],
        ["Respuesta perdida tras cada paso, pasos idempotentes", "0 de 5", "Cada paso aplicado una sola vez"],
    ]
    return tab("Flujo de 5 pasos con efectos: puntos de fallo que dejan el estado incoherente",
               "Tabla: en un flujo de cinco pasos con efectos, un corte antes de cada paso deja un estado incoherente en 4 de 5 puntos; perder la respuesta tras cada paso y reintentar el flujo entero lo deja incoherente en 5 de 5; con pasos idempotentes, en ninguno.",
               ["Fallo inyectado", "Puntos incoherentes", "Qué ocurre"], rows, [380, 150, 360], row_h=60, size=12,
               note="Los dos fallos parciales distintos, el corte y la respuesta perdida, necesitan defensas distintas: el corte pide atomicidad o compensación; la respuesta perdida pide idempotencia. Se enumeran todos los puntos del flujo; los efectos son contadores en memoria, sin red.",
               note_kind="coral", foot="Enumeración exacta de los puntos de fallo; sin aleatoriedad.")


def se347_repeticiones() -> "Fig":
    items = [("5 ejecuciones", 6.9, "coral", "6,9 %"), ("10 ejecuciones", 13.4, "coral", "13,4 %"), ("50 ejecuciones", 51.3, "gold", "51,3 %"),
             ("100 ejecuciones", 76.3, "gold", "76,3 %"), ("200 ejecuciones", 94.4, "teal", "94,4 %"), ("300 ejecuciones", 98.7, "teal", "98,7 %")]
    return bars("Probabilidad de ver al menos una vez un fallo que aparece en 1 de cada 70 ejecuciones",
                "Barras con la probabilidad de ver un fallo que ocurre en 1 de cada 70 ejecuciones al repetir la prueba: 6,9 por ciento con 5 repeticiones, 13,4 con 10, 51,3 con 50, 76,3 con 100, 94,4 con 200 y 98,7 con 300.",
                items, 5.4, "Para el 95 % hacen falta 209 repeticiones y para el 99,9 % 481; una simulación de 10 000 campañas de 10 repeticiones dio 14,0 % frente al 13,4 % teórico. Enumerar las 70 intercalaciones las cubre todas. Repetir una prueba inestable en CI sin controlar el orden no la arregla.",
                label_w=190, width=980, note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-348
def se348_escalera() -> "Fig":
    rows = [
        ["Fallo duro", "3 000 lecturas falladas", "600 rechazadas", "0"],
        ["Caché obsoleta para lecturas", "3 000 lecturas obsoletas, 0 falladas", "600 rechazadas", "0"],
        ["Caché + cola de escrituras", "3 000 obsoletas, 0 falladas", "600 encoladas y reenviadas", "0 si la cola cabe"],
    ]
    return tab("La base de entregas cae 60 s de 300 (50 lecturas y 10 escrituras por segundo)",
               "Tabla: con fallo duro se pierden 3 000 lecturas y 600 escrituras durante la caída; con caché obsoleta las lecturas se sirven pero las 600 escrituras se rechazan; con caché y cola, las 3 000 lecturas son obsoletas, ninguna falla y las 600 escrituras se encolan y se reenvían al volver.",
               ["Estrategia", "Lecturas", "Escrituras", "Datos perdidos"], rows, [250, 290, 220, 170], row_h=58, size=12,
               note="Cada peldaño cambia un fallo visible por un estado que hay que declarar: una lectura vieja hasta N minutos, una escritura confirmada que aún no está en la base. Pasar de uno a otro es una decisión de producto con su límite, no un interruptor técnico. Tasas y duración son supuestos del autor.",
               note_kind="teal", foot=SINT)


def se348_sobrecarga() -> "Fig":
    rows = [
        ["Sin límite", "6 000 en cola", "21,2 turnos", "20,9 turnos", "0"],
        ["Cola acotada a 200", "100 en cola", "2,0 turnos", "2,0 turnos", "1 761 entregas y 4 139 listados"],
        ["Cola acotada con prioridad", "100 en cola", "1,0 turnos", "2,8 turnos", "0 entregas y 5 900 listados"],
    ]
    return tab("Llegan 150 solicitudes por turno a un sistema que atiende 100, durante 120 turnos",
               "Tabla: sin límite quedan 6 000 solicitudes en cola y la espera media sube a unos 21 turnos; con una cola acotada la espera baja a 2 turnos pero se descartan 1 761 entregas y 4 139 listados; con prioridad se descartan 0 entregas y 5 900 listados.",
               ["Política", "Al final", "Espera media de una entrega", "Espera media de un listado", "Descartadas"], rows, [220, 140, 180, 180, 190], row_h=62, size=12,
               note="Si llegan más solicitudes de las que se atienden, algo espera o se descarta; elegir qué se descarta es la política. La prioridad protege lo que no se puede reintentar sin costo. Que la cola crezca 50 por turno hasta 6 000 explica una espera que sube hasta unos 41 turnos (ley de Little). Las proporciones 30/70 y la capacidad son supuestos del autor.",
               note_kind="coral", foot=SINT)


def se348_paquete() -> "Fig":
    rows = [
        ["Campo ausente o vacío", "59 de 59"],
        ["Degradación sin límite declarado", "21 de 21"],
        ["Reintento «hasta que funcione»", "21 de 21"],
        ["Presupuesto de tiempos incoherente (800 ms con 3 llamadas de 500 ms)", "0 de 23"],
        ["Evidencia copiada del servicio vecino", "0 de 23"],
        ["Prueba de fallos que nunca se ejecutó", "0 de 25"],
        ["Garantía imposible (exactamente una vez y disponible en cualquier partición)", "0 de 28"],
    ]
    return tab("Validador del paquete del servicio distribuido sobre 200 mutaciones: 101 detectadas",
               "Tabla: un verificador de forma detecta 101 de 200 mutaciones de un paquete de servicio distribuido, todas las de campos ausentes, degradación sin límite y reintentos ilimitados, y ninguna de las 99 que dejan el texto plausible: tiempos incoherentes, evidencia copiada, pruebas no ejecutadas y garantías imposibles.",
               ["Mutación", "Detectadas"], rows, [640, 160], row_h=44, size=12,
               note="Un paquete completo no es un paquete correcto. Lo que ningún validador de forma ve es lo que ocurre en las revisiones reales: una garantía que no puede cumplirse, una prueba que no se corrió. Reglas escritas conociendo las mutaciones: la exactitud sobre paquetes reales es desconocida.",
               note_kind="gold", foot=SINT)


FIGURES = {
    "se-343-lideres-que-se-creen-legitimos.svg": se343_lideres,
    "se-343-testigo-de-cerco.svg": se343_cerco,
    "se-343-plazos-de-eleccion.svg": se343_plazos,
    "se-344-orden-de-aplicar-y-confirmar.svg": se344_entrega,
    "se-344-retencion-de-claves.svg": se344_retencion,
    "se-344-salida-por-anexo-o-por-clave.svg": se344_salida,
    "se-345-balanceo-y-cola-pesada.svg": se345_balanceo,
    "se-345-conmutacion-y-perdida.svg": se345_conmutacion,
    "se-345-hash-o-rango.svg": se345_reparto,
    "se-346-reintentos-e-interruptor.svg": se346_reintentos,
    "se-346-planificador-y-fallo-raro.svg": se346_planificador,
    "se-346-linter-de-planes-de-caos.svg": se346_plan,
    "se-347-carrera-y-calendario-minimo.svg": se347_carrera,
    "se-347-fallo-parcial-del-flujo.svg": se347_parcial,
    "se-347-repeticiones-para-ver-un-fallo.svg": se347_repeticiones,
    "se-348-escalera-de-degradacion.svg": se348_escalera,
    "se-348-sobrecarga-y-prioridad.svg": se348_sobrecarga,
    "se-348-validador-del-paquete.svg": se348_paquete,
}
