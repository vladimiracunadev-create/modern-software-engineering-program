"""Figures for SE-307 to SE-312 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-307
def se307_frio() -> Fig:
    rows = [
        ["Estable (2 por segundo)", "0", "7 de 7 194 (0,10 %)", "—"],
        ["Picos de entrega", "0", "36 de 9 033 (0,40 %)", "11,1 % de 296"],
        ["Picos de entrega", "5", "15 de 9 033 (0,17 %)", "5,1 % de 296"],
        ["Picos de entrega", "10", "5 de 9 033 (0,06 %)", "0,7 % de 296"],
        ["Esporádico (4 por hora)", "0", "3 de 4", "—"],
        ["Esporádico (4 por hora)", "5", "0 de 4", "—"],
    ]
    return tab("Arranques en frío en una hora de tráfico según el patrón y las instancias mantenidas",
               "Tabla: con tráfico estable solo 0,10 por ciento de las peticiones arranca en frío; con picos de entrega, el 0,40 por ciento en la hora y el 11,1 por ciento de las peticiones de los primeros diez segundos del pico; mantener cinco instancias baja ese 11,1 a 5,1 y diez instancias a 0,7; con tráfico esporádico tres de cuatro peticiones arrancan en frío.",
               ["Patrón de tráfico", "Instancias mantenidas", "Peticiones con arranque en frío", "En los primeros 10 s del pico"], rows, [260, 190, 270, 230], row_h=44, size=13,
               note="El promedio engaña: 0,40 % parece despreciable, pero se concentra en los primeros segundos de la ráfaga, justo cuando hay gente entregando contra un plazo. El arranque en frío (0,8 s) y el tibio (30 ms) son supuestos del autor; el mecanismo es la espera mientras se crea una instancia por cada petición simultánea sin instancia libre.",
               note_kind="coral", foot=SINT)


def se307_costo() -> Fig:
    rows = [
        ["128 MB", "0,15 s", "22,2", "56 %"],
        ["128 MB", "1,0 s", "5,0", "12 %"],
        ["512 MB", "0,15 s", "7,8", "20 %"],
        ["512 MB", "1,0 s", "1,3", "3 %"],
        ["1 024 MB", "0,15 s", "4,2", "10 %"],
        ["1 024 MB", "1,0 s", "0,7", "2 %"],
    ]
    return tab("Tráfico a partir del cual un servidor fijo cuesta menos que pagar por uso (unidades ficticias)",
               "Tabla: con una función de 128 megabytes y 0,15 segundos por petición, un servidor fijo de 40 peticiones por segundo cuesta menos a partir de 22,2 peticiones por segundo, el 56 por ciento de su capacidad; con 1024 megabytes y un segundo por petición el punto de equilibrio baja a 0,7 peticiones por segundo, el 2 por ciento.",
               ["Memoria", "Duración por petición", "Equilibrio (peticiones por segundo)", "Del servidor de 40 rps"], rows, [190, 220, 300, 220], row_h=40, size=13,
               note="El equilibrio no es una propiedad del modelo serverless sino del producto memoria × duración y de la utilización: una función ligera y esporádica favorece el pago por uso; una pesada y sostenida favorece el servidor. Los precios (0,20 por millón, 0,0000167 por GB-s, 30 por servidor) son unidades ficticias de orden de magnitud, no una tarifa de proveedor; con dos servidores el equilibrio sube a 44,5 rps.",
               note_kind="gold", foot=SINT)


def se307_rumor() -> Fig:
    rows = [
        ["Fanout 1 · 20 % desconectados", "17,8", "21", "5 003"],
        ["Fanout 2 · 20 % desconectados", "10,5", "12", "5 402"],
        ["Fanout 3 · 20 % desconectados", "8,1", "9", "5 769"],
        ["Fanout 5 · 20 % desconectados", "6,0", "7", "6 563"],
        ["Fanout 2 · 0 % desconectados", "9,0", "10", "—"],
        ["Fanout 2 · 50 % desconectados", "14,3", "19", "—"],
        ["Fanout 2 · 80 % desconectados", "28,8", "40", "—"],
    ]
    return tab("Rondas para que un rumor llegue al 99 % de los pares conectados (1000 pares, 200 repeticiones)",
               "Tabla: en una red de mil pares con 20 por ciento desconectados, un rumor con fanout 2 llega al 99 por ciento de los conectados en 10,5 rondas de media y 12 como máximo, enviando 5402 mensajes; con fanout 5 tarda 6,0 rondas y envía 6563; con 80 por ciento de pares desconectados el fanout 2 tarda 28,8 rondas.",
               ["Configuración", "Rondas, media", "Rondas, máximo", "Mensajes, media"], rows, [400, 190, 200, 210], row_h=36, size=13,
               note="Las rondas crecen con el logaritmo del tamaño (8,2 con 100 pares, 10,5 con 1000, 13,1 con 10 000) y se disparan cuando casi todos los pares están desconectados. Más fanout acorta la difusión y encarece el tráfico: cinco veces el fanout envía solo un 31 % más de mensajes. Modelo sin latencias, sin fallos de enlace y con elección uniforme de pares.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-308
def se308_deteccion() -> Fig:
    items = [("Se revisa en cada commit", 1.00, "teal", "1,00 (p95: 1)"), ("Cada 20 commits", 1.30, "teal", "1,30 (p95: 2)"),
             ("Cada 100 commits", 2.50, "gold", "2,50 (p95: 5)"), ("Solo al final (400 commits)", 7.05, "coral", "7,05 (p95: 14)")]
    return bars("Puntos de uso de una dependencia indebida que hay que corregir según cuándo se detecta",
                "Barras: una dependencia indebida que entra en el commit t y atrae un uso nuevo con probabilidad 3 por ciento por commit deja 1,00 punto de uso por corregir si se detecta en el mismo commit, 1,30 si se revisa cada 20, 2,50 cada 100 y 7,05 si solo se revisa al final.",
                items, 60, "Cada commit sin detección es una oportunidad de que alguien se apoye en la violación: el coste de corregir crece con el tiempo hasta detectar. La tasa del 3 % es un supuesto; con otra tasa cambian las cifras, no la forma. Una función de aptitud que falla en el commit que introduce el problema hace la corrección tan barata como puede ser.",
                label_w=290, width=980, note_kind="teal", foot=SINT)


def se308_ruido() -> Fig:
    rows = [
        ["30", "× 1,10", "24,7 %", "21,6 %"],
        ["30", "× 1,25", "6,5 %", "61,0 %"],
        ["30", "× 1,50", "0,4 %", "94,5 %"],
        ["100", "× 1,10", "11,1 %", "10,1 %"],
        ["100", "× 1,25", "0,2 %", "69,3 %"],
        ["500", "× 1,10", "0,3 %", "0,5 %"],
        ["500", "× 1,25", "0,0 %", "87,5 %"],
    ]
    return tab("Prueba de rendimiento con umbral sobre el percentil 95: falsas alarmas y regresiones de +20 % no detectadas",
               "Tabla: con 30 muestras por ejecución y un umbral de 1,10 veces el percentil 95 esperado hay 24,7 por ciento de falsas alarmas y se pierde el 21,6 por ciento de las regresiones de 20 por ciento; con 500 muestras y 1,10 las dos cifras caen a 0,3 y 0,5 por ciento; con margen 1,25 casi nunca hay falsa alarma pero se pierde el 87,5 por ciento de las regresiones.",
               ["Muestras por ejecución", "Margen del umbral", "Falsas alarmas", "Regresión de +20 % perdida"], rows, [240, 220, 220, 260], row_h=40, size=13,
               note="El umbral y el número de muestras son una decisión estadística: con pocas muestras no existe un umbral que dé a la vez pocas falsas alarmas y pocas regresiones perdidas; con muchas sí, a costa de tiempo de ejecución. Una prueba que falla al azar se ignora, y una función de aptitud ignorada ha dejado de existir. 2000 ejecuciones por celda, latencias lognormales sintéticas.",
               note_kind="gold", foot=SINT)


def se308_tendencia() -> Fig:
    rows = [
        ["Umbral absoluto de 30", "0 %", "14 semanas tarde", "18 %", "0 %"],
        ["Trinquete: +2 sobre el mejor valor", "99 %", "18 semanas antes", "0 %", "24,4 %"],
        ["Pendiente > 0,1 por semana en 8 semanas", "95 %", "21 semanas antes", "0 %", "95,4 %"],
    ]
    return tab("Tres alarmas sobre una deriva de acoplamiento (926 series de 80 semanas con daño real sobre 26)",
               "Tabla: de 926 series con una deriva real que supera 26, el umbral absoluto de 30 nunca avisa antes del daño y no avisa nunca en el 18 por ciento; el trinquete avisa antes en el 99 por ciento con una mediana de 18 semanas de adelanto y 24,4 por ciento de falsas alarmas en series planas; la alarma por pendiente avisa antes en el 95 por ciento y da falsa alarma en el 95,4 por ciento de las series planas.",
               ["Alarma", "Avisa antes del daño", "Mediana", "Nunca avisa", "Falsas alarmas en series planas"], rows, [330, 170, 170, 130, 190], row_h=58, size=12,
               note="Una alarma que llega pronto es una alarma que se equivoca más: el umbral absoluto no da falsas alarmas porque llega tarde; la pendiente de ocho semanas ve tendencias en el ruido. La combinación habitual, un trinquete con tolerancia más una revisión humana de las alarmas, es una decisión sobre qué error cuesta más. Series sintéticas con deriva de 0,05 por semana y ruido de 0,4.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-309
def se309_pesos() -> Fig:
    rows = [
        ["Pesos base de la matriz", "3,95 puntos", "3,30 puntos", "3,45 puntos"],
        ["20 000 conjuntos de pesos al azar", "64,5 %", "35,0 %", "0,5 %"],
        ["Pesos base, puntajes con ±1 en la mitad de los casos", "80,4 %", "3,7 %", "15,9 %"],
    ]
    return tab("Quién gana la matriz de decisión cuando cambian los pesos o los puntajes",
               "Tabla: con los pesos base la matriz da 3,95 puntos al monolito modular, 3,30 a servicios y 3,45 a serverless; con 20000 conjuntos de pesos al azar el monolito gana el 64,5 por ciento de las veces, servicios el 35,0 y serverless el 0,5; con los pesos base y puntajes que varían en uno gana el monolito el 80,4 por ciento.",
               ["Condición", "Monolito modular", "Servicios", "Serverless"], rows, [440, 170, 150, 150], row_h=52, size=12,
               note="El ganador de los pesos base lleva 0,5 puntos de ventaja sobre 3,95, pero con pesos al azar pierde una de cada tres veces frente a servicios. Una matriz no decide: muestra qué supuestos hay que defender. Los puntajes son juicios del autor, no mediciones; sirven para ver sensibilidad, no para elegir una arquitectura real.",
               note_kind="gold", foot=SINT)


def se309_adr() -> Fig:
    rows = [
        ["Sin sección de alternativas", "12 de 12", "forma"],
        ["Estado inventado («en discusión»)", "12 de 12", "forma"],
        ["Fecha en formato 13/11/2026", "12 de 12", "forma"],
        ["Una sola alternativa", "12 de 12", "forma"],
        ["Alternativas «Ninguna» repetidas", "0 de 12", "sentido"],
        ["Consecuencias solo positivas", "0 de 12", "sentido"],
        ["Decisión que no responde al contexto", "0 de 12", "sentido"],
        ["Reversibilidad «Sí.» sin plazo ni condición", "0 de 12", "sentido"],
    ]
    return tab("Un comprobador de ADR frente a 12 ADR válidos con un defecto cada uno",
               "Tabla: el comprobador detecta las 12 de 12 variantes con un defecto de forma, falta de sección, estado inventado, fecha mal escrita o una sola alternativa, y 0 de 12 de las cuatro con un defecto de sentido, alternativas vacías, consecuencias solo positivas, decisión que no responde al contexto o reversibilidad sin condición; los doce ADR válidos pasan sin falsos positivos.",
               ["Defecto introducido", "Detectado", "Tipo"], rows, [500, 170, 150], row_h=38, size=13,
               note="El comprobador exige secciones, estado válido, fecha ISO y al menos dos alternativas: eso evita ADR incompletos, no malos. Las cuatro variantes que pasan cumplen la forma y vacían el contenido; eso lo ve una persona leyendo. Un ADR aceptado por el comprobador sigue necesitando revisión humana del sentido.",
               note_kind="coral", foot=SINT)


def se309_espera() -> Fig:
    rows = [
        ["5", "2,0", "5,7", "9,4", "13,0", "20,3", "30,3", "0 semanas"],
        ["30", "12,0", "14,3", "16,2", "17,9", "21,5", "31,5", "0 semanas"],
        ["100", "40,2", "38,2", "35,2", "31,8", "25,0", "35,0", "20 semanas"],
    ]
    return tab("Coste esperado (semanas-equipo) de decidir tras esperar, según lo caro que sea revertir",
               "Tabla: si revertir una decisión equivocada cuesta 5 o 30 semanas-equipo conviene decidir de inmediato, con costes esperados de 2,0 y 12,0; si cuesta 100 conviene esperar 20 semanas hasta que la evidencia sea fiable, con un coste esperado de 25,0 frente a 40,2 de decidir ya.",
               ["Coste de revertir", "Esperar 0", "4", "8", "12", "20", "30", "Mejor espera"], rows, [200, 110, 100, 100, 100, 100, 100, 160], row_h=44, size=13,
               note="La espera tiene un coste lineal de 1 por semana y la evidencia pasa de acertar el 60 % a acertar el 95 % tras un tiempo desconocido (2 a 20 semanas). Esperar solo compensa cuando equivocarse es caro y la evidencia mejora de verdad. Es un modelo de juguete con supuestos del autor: sirve para pensar la reversibilidad, no para fijar cifras.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-310
def se310_reparto() -> Fig:
    rows = [
        ["Por comunidad (afinidad real)", "4 (12 %)", "16,3 %", "1,16"],
        ["Un equipo grande y tres pequeños", "12 (38 %)", "40,0 %", "1,45"],
        ["Al azar", "26 (81 %)", "66,8 %", "1,89"],
        ["Por capa técnica", "29 (91 %)", "72,5 %", "2,11"],
    ]
    return tab("Reparto de 24 módulos entre 4 equipos: dependencias y cambios que cruzan equipos (32 dependencias)",
               "Tabla: al repartir 24 módulos por comunidades de afinidad, 4 de 32 dependencias cruzan equipos y el 16,3 por ciento de los cambios obliga a coordinar; al repartir por capa técnica cruzan 29 dependencias y el 72,5 por ciento de los cambios involucra a más de un equipo, con 2,11 equipos por cambio.",
               ["Reparto", "Dependencias entre equipos", "Cambios que cruzan equipos", "Equipos por cambio"], rows, [330, 230, 240, 200], row_h=40, size=13,
               note="Los equipos por capa técnica son cómodos para especialistas y obligan a que casi todo cambio de negocio cruce equipos. El reparto por comunidad ahorra coordinación solo si las comunidades existen en el grafo de dependencias; el grafo y las probabilidades de arista son sintéticos. Los canales de comunicación crecen como n(n−1)/2: 28 con 8 personas, 190 con 20.",
               note_kind="teal", foot=SINT)


def se310_huerfanos() -> Fig:
    rows = [
        ["1 persona", "5,04 %", "14,94 %", "29,99 %"],
        ["2 personas", "0,24 %", "2,13 %", "8,83 %"],
        ["3 personas", "0,01 %", "0,32 %", "2,69 %"],
    ]
    return tab("Módulos sin nadie que los conozca según cuántas personas los conocen y cuántas se van",
               "Tabla: si cada módulo lo conoce una sola persona y se va el 15 por ciento del equipo, queda sin conocimiento el 14,94 por ciento de los módulos; con dos personas por módulo el 2,13 y con tres el 0,32; con una salida del 30 por ciento, 29,99, 8,83 y 2,69 por ciento.",
               ["Quién conoce cada módulo", "Se va el 5 %", "Se va el 15 %", "Se va el 30 %"], rows, [330, 190, 190, 190], row_h=44, size=13,
               note="Pasar de una a dos personas por módulo reduce el riesgo unas siete veces (14,94 % → 2,13 %); pasar de dos a tres, algo más de seis. El resultado es q^k con salidas independientes; las salidas reales se correlacionan (reorganizaciones, un mismo proyecto). Además, con un propietario principal por módulo, 5 de 15 personas concentran la mitad de los 60 módulos.",
               note_kind="gold", foot=SINT)


def se310_colas() -> Fig:
    rows = [
        ["50 %", "1,4 / 4,5", "3,4 / 7,6", "5,3 / 10,4", "9,3 / 15,9"],
        ["70 %", "2,3 / 7,5", "5,6 / 12,5", "8,9 / 17,2", "15,4 / 25,8"],
        ["90 %", "6,5 / 18,9", "15,8 / 34,1", "24,9 / 47,3", "42,8 / 71,4"],
    ]
    return tab("Días de entrega de un cambio (mediana / percentil 90) según equipos por los que pasa y su ocupación",
               "Tabla: con equipos ocupados al 50 por ciento, un cambio que pasa por cinco equipos tarda 9,3 días de mediana y 15,9 en el percentil 90; con ocupación del 90 por ciento tarda 42,8 y 71,4 días; pasando por un solo equipo ocupado al 90 por ciento tarda 6,5 y 18,9.",
               ["Ocupación de cada equipo", "1 equipo", "2 equipos", "3 equipos", "5 equipos"], rows, [250, 170, 170, 170, 170], row_h=44, size=13,
               note="Cada traspaso añade una cola y la espera crece más que linealmente con la ocupación. El trabajo (servicio medio de un día) es el mismo en todas las celdas: lo que cambia es cuánto espera. Colas M/M/1 en serie con llegadas de Poisson, un modelo ideal; los equipos reales tienen trabajo en paralelo, prioridades y vacaciones.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-311
def se311_revision() -> Fig:
    rows = [
        ["E01", "Entrega en día normal, p95 ≤ 800 ms", "cumple · 445 ms"],
        ["E02", "Entrega en el pico (60 rps), p95 ≤ 2 s", "falla · satura al 120 %"],
        ["E03", "Consulta de nota, p95 ≤ 400 ms", "cumple · 155 ms"],
        ["E04", "Disponibilidad de la entrega ≥ 99,95 %", "falla · 99,905 %"],
        ["E05", "Disponibilidad de la consulta ≥ 99,9 %", "cumple · 99,930 %"],
        ["E06 – E08", "Si cae notificaciones, antivirus o notas, se sigue entregando", "cumple (3 de 3)"],
        ["E09", "El pico cabe con uso ≤ 80 %", "falla · uso 120 % de 50 rps"],
        ["E10", "El antivirus procesa 20 archivos por segundo", "falla · uso 125 % de 16 rps"],
        ["E11", "Cambiar la regla de nota toca ≤ 1 unidad", "falla · 2 unidades"],
        ["E12", "Cambiar el formato de archivo toca ≤ 1 unidad", "falla · 2 unidades"],
    ]
    return tab("Revisión ejecutable de la arquitectura en servicios contra 12 escenarios (supuestos del autor)",
               "Tabla: al ejecutar el modelo de la arquitectura en servicios contra doce escenarios, seis fallan: el pico de entrega satura el almacenamiento de archivos al 120 por ciento, la disponibilidad de la entrega da 99,905 por ciento, el antivirus llega al 125 por ciento de su capacidad y los dos cambios tocan dos unidades de despliegue.",
               ["Escenario", "Exigencia", "Resultado del modelo"], rows, [140, 480, 300], row_h=40, size=12,
               note="Seis de doce escenarios fallan y cuatro de ellos por la misma pieza: el almacenamiento de archivos y su revisión limitan el pico. Los números salen de un modelo con latencias p95 sumadas, disponibilidades por componente y capacidades supuestas; sirve para encontrar dónde mirar, no para predecir el comportamiento de un sistema real.",
               note_kind="coral", foot=SINT)


def se311_revisores() -> Fig:
    rows = [
        ["1 persona", "2,0 %", "9,4 %"],
        ["2 personas", "13,9 %", "40,3 %"],
        ["3 personas", "30,5 %", "65,3 %"],
        ["5 personas", "61,5 %", "89,4 %"],
    ]
    return tab("Probabilidad de que la revisión cubra las tres categorías débiles según quién revisa (5 escenarios por persona, 30 candidatos)",
               "Tabla: una persona que prefiere escenarios de latencia cubre las tres categorías débiles, capacidad, disponibilidad y cambio, el 2,0 por ciento de las veces; dos personas con la misma especialidad el 13,9 y cinco el 61,5; con especialidades distintas una persona cubre el 9,4, dos el 40,3 y cinco el 89,4 por ciento.",
               ["Personas que revisan", "Todas con la misma especialidad", "Con especialidades distintas"], rows, [260, 340, 300], row_h=44, size=13,
               note="Elegir escenarios sin sesgo (5 de 30 al azar) cubre las tres categorías el 12,2 % de las veces, más que una persona sesgada. El valor de varias miradas está en que sus sesgos no coinciden. Pesos de preferencia (×4 por la especialidad), categorías y debilidades son supuestos del autor.",
               note_kind="gold", foot=SINT)


def se311_sensibilidad() -> Fig:
    rows = [
        ["Capacidad de archivos", "× 0,5", "E02 y E09"],
        ["Capacidad de web, identidad, entregas o notas (cada una)", "× 0,5", "E09"],
        ["Instancias del antivirus", "× 1,3 o × 2", "E10"],
        ["Capacidad del antivirus", "× 2", "E10"],
        ["Latencia de cualquier componente", "× 0,5 a × 2", "ninguno"],
        ["Tasa de fallo de cualquier componente", "× 0,5 a × 2", "ninguno"],
    ]
    return tab("Perturbaciones de un parámetro que invierten algún veredicto (8 de 144 combinaciones)",
               "Tabla: al variar uno a uno nueve componentes por 0,5, 0,7, 1,3 y 2 en cuatro parámetros, solo ocho de 144 perturbaciones cambian algún veredicto: reducir a la mitad la capacidad de archivos rompe dos escenarios, reducir a la mitad la de otro componente rompe el de capacidad y subir las instancias del antivirus arregla el de su capacidad; ninguna variación de latencia ni de tasa de fallo cambia un veredicto.",
               ["Parámetro", "Variación", "Veredictos que se invierten"], rows, [450, 190, 270], row_h=44, size=13,
               note="Los veredictos son robustos a la latencia y a la tasa de fallo y frágiles a la capacidad. El escenario E04 falla por solo 0,015 puntos de disponibilidad, pero ninguna mejora individual de un componente lo arregla: su causa es la suma de componentes y la causa común. Un margen pequeño no implica sensibilidad a un parámetro concreto.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-312
def se312_validador() -> Fig:
    rows = [
        ["Escenario sin driver", "25 de 25", "estructura"],
        ["Umbral borrado", "25 de 25", "estructura"],
        ["ADR que apunta a un escenario inexistente", "25 de 25", "estructura"],
        ["Vista sin un componente", "25 de 25", "estructura"],
        ["Función de aptitud sobre un escenario inexistente", "25 de 25", "estructura"],
        ["ADR con una sola alternativa", "25 de 25", "estructura"],
        ["Umbral absurdo (999 999 ms)", "0 de 25", "sentido"],
        ["Función de aptitud que siempre pasa", "0 de 25", "sentido"],
    ]
    return tab("Validador del dossier de arquitectura frente a 200 mutaciones (150 detectadas)",
               "Tabla: de 200 mutaciones de un dossier de arquitectura el validador detecta 150, las seis de estructura (referencias rotas, umbral borrado, vista incompleta, una sola alternativa) en 25 de 25 casos cada una, y ninguna de las dos de sentido, un umbral de 999999 milisegundos y una función de aptitud que siempre pasa.",
               ["Mutación", "Detectadas", "Tipo"], rows, [520, 170, 170], row_h=38, size=13,
               note="El dossier base (4 drivers, 12 escenarios, 4 ADR, 6 funciones de aptitud, 4 vistas) pasa el validador y, aun así, el modelo ejecutable da cuatro fallas (E04, E08, E10, E12): validar la forma no es evaluar la arquitectura. Las mutaciones son del autor; la tasa de 150/200 depende de cuántas sean de sentido.",
               note_kind="coral", foot=SINT)


def se312_mes() -> Fig:
    rows = [
        ["Servicios", "50 rps", "99,748 %", "99,919 %", "60 %", "40,0"],
        ["Monolito modular", "50 rps", "99,794 %", "99,951 %", "74 %", "40,0"],
        ["Monolito + archivos asíncronos", "120 rps", "99,794 %", "99,951 %", "74 %", "0,0"],
        ["Propuesta final (más instancias)", "135 rps", "99,794 %", "99,951 %", "74 %", "0,0"],
    ]
    return tab("Mil meses simulados de cuatro arquitecturas (4 picos de 60 a 90 rps de 10 minutos por mes)",
               "Tabla: en mil meses simulados, las arquitecturas con capacidad de entrega de 50 peticiones por segundo pasan 40 minutos saturadas en promedio durante los picos y las de 120 y 135 no se saturan; la disponibilidad mensual mediana va de 99,919 a 99,951 por ciento y solo entre el 60 y el 74 por ciento de los meses alcanza 99,9 por ciento.",
               ["Arquitectura", "Capacidad de la ruta de entrega", "Disponibilidad p5", "Disponibilidad mediana", "Meses ≥ 99,9 %", "Min. saturados"], rows, [280, 150, 140, 150, 120, 150], row_h=58, size=12,
               note="Añadir instancias elimina la saturación pero no mejora la disponibilidad: lo domina la causa común. Eso obliga a una decisión de negocio escrita en un ADR: aceptar 99,9 % o invertir en aislar la causa común. Caídas con duración exponencial de 20 minutos y 30 % de causa común: supuestos del autor, no datos de un sistema.",
               note_kind="gold", foot=SINT)


def se312_impacto() -> Fig:
    rows = [
        ["ADR-1 · subir archivos por URL firmada", "8", "3", "5", "F1, F2, F5, F6"],
        ["ADR-2 · monolito modular", "10", "2", "9", "F1, F2, F3, F5, F6"],
        ["ADR-3 · revisión asíncrona", "7", "3", "4", "F1, F2, F4, F6"],
        ["ADR-4 · tres instancias", "10", "4", "6", "F1, F2, F3, F5, F6"],
    ]
    return tab("Escenarios que dependen de los componentes de cada decisión y los que su ADR no declara",
               "Tabla: al revertir la decisión del monolito modular dependen de sus componentes 10 de 12 escenarios, pero el ADR solo declara 2, es decir 9 sin declarar; la decisión de subir archivos por URL firmada afecta a 8 escenarios con 3 declarados; hay que re-ejecutar entre 4 y 5 funciones de aptitud según la decisión.",
               ["Decisión", "Escenarios afectados", "Declarados en el ADR", "Sin declarar", "Funciones de aptitud a re-ejecutar"], rows, [350, 150, 150, 120, 200], row_h=46, size=12,
               note="El grafo decisión → componente → escenario muestra que los ADR declaran menos dependencias de las reales: una decisión estructural como el monolito modular toca casi todo. Por eso un ADR lista los escenarios que podría romper, y esa lista se regenera desde el modelo en lugar de escribirse de memoria.",
               note_kind="teal", foot=SINT)


FIGURES = {
    "se-307-arranques-en-frio.svg": se307_frio,
    "se-307-equilibrio-de-costo.svg": se307_costo,
    "se-307-difusion-por-rumor.svg": se307_rumor,
    "se-308-cuando-se-detecta-una-violacion.svg": se308_deteccion,
    "se-308-falsas-alarmas-y-regresiones.svg": se308_ruido,
    "se-308-umbral-trinquete-y-tendencia.svg": se308_tendencia,
    "se-309-ganador-segun-pesos.svg": se309_pesos,
    "se-309-comprobador-de-adr.svg": se309_adr,
    "se-309-cuanto-esperar.svg": se309_espera,
    "se-310-reparto-de-modulos.svg": se310_reparto,
    "se-310-modulos-huerfanos.svg": se310_huerfanos,
    "se-310-entrega-con-colas.svg": se310_colas,
    "se-311-revision-ejecutable.svg": se311_revision,
    "se-311-cobertura-de-revisores.svg": se311_revisores,
    "se-311-sensibilidad-de-parametros.svg": se311_sensibilidad,
    "se-312-validador-del-dossier.svg": se312_validador,
    "se-312-un-mes-de-cuatro-arquitecturas.svg": se312_mes,
    "se-312-impacto-de-revertir-una-decision.svg": se312_impacto,
}
