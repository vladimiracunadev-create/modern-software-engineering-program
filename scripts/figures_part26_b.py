"""Figures for SE-319 to SE-324 (integration, resilience, antipatterns and workshop: seeded simulations, ast analysis and a local socket measurement; Windows CPython 3.12; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, line_chart, scatter, stacked_bars
from figure_diagrams import chain, fan

from figures_part45_a import bars, flow

EJEC = "Código ejecutado de verdad (CPython 3.12, Windows 11); los recuentos son deterministas y los tiempos varían de equipo en equipo."
SIM = "Simulación con semilla fija sobre código ejecutado de verdad (CPython 3.12); las magnitudes son de este modelo, no de un sistema real."


# ---------------------------------------------------------------- SE-319
def se523_receptor_idempotente() -> Fig:
    return dumbbell(
        'Mil mensajes con entrega al menos una vez: 208 duplicados y la suma de pagos',
        "Puntos unidos por una línea con la suma de los pagos de mil mensajes con entrega al menos una vez y 208 duplicados: la suma real es 15 682; sin receptor idempotente da 18 759, con un error de 3 077 por duplicados contados dos veces; con receptor idempotente da 15 682 y el error es 0.",
        [("Sin receptor idempotente", 15682, 18759), ("Con receptor idempotente", 15682, 15682)],
        unit="Suma de pagos", names=("Suma real", "Suma calculada"), decimals=0, label_w=240,
        delta=lambda a, b: f"+{b - a:,}".replace(",", " ") if b != a else "0",
        note='La entrega al menos una vez es la garantía habitual y barata; la exactamente una vez se construye en el receptor. Sin identificadores estables, el receptor idempotente no se puede escribir.', note_kind='coral', foot=SIM)


def se523_cuatro_patrones() -> Fig:
    return fan(
        'Cuatro patrones de mensajería y lo que se midió con un canal simulado',
        "Diagrama de cuatro patrones de mensajería con lo medido en un canal simulado: el enrutador por contenido reparte mil mensajes en 601 pagos, 206 avisos y 193 bajas; la cola de cartas muertas procesa 198 y aparta 2 con 204 intentos; el resecuenciador deja 977 pares fuera de orden a la entrada y 0 a la salida; el identificador de correlación asocia 20 de 20 respuestas frente a 1 de 20 por posición.",
        ("Cuatro patrones de mensajería", "escenario y resultado medido en un canal simulado", "navy"),
        [("Content-Based Router", "mil mensajes por tipo · 601 pagos, 206 avisos, 193 bajas", "teal"),
         ("Dead Letter Channel", "200 mensajes, 25 de la muestra son veneno, tope de 3 intentos · 198 procesados, 2 a la cola de cartas muertas, 204 intentos", "teal"),
         ("Resequencer", "entrega desordenada en ventanas de 6 · 977 pares fuera de orden a la entrada, 0 a la salida", "teal"),
         ("Correlation Identifier", "20 respuestas desordenadas · 20 de 20 asociadas por identificador; 1 de 20 por posición", "teal")],
        note='El catálogo de Hohpe y Woolf da nombre a los mismos problemas que aparecen con colas, buses y sistemas de eventos de hoy; el nombre sirve para discutir, la medida para decidir.', note_kind='teal', foot=SIM)


def se523_garantias() -> Fig:
    return flow('Qué garantía de entrega exige qué patrón en el receptor',
                'Diagrama de cuatro cajas: al menos una vez puede duplicar y exige un receptor idempotente, como mucho una vez puede perder y exige reconciliación, sin orden garantizado exige un reordenador si el orden importa, y el mensaje que nunca se procesa exige un canal de cartas muertas con alarma.',
                [[('AL MENOS UNA VEZ\nPuede duplicar → Idempotent Receiver', 'coral'), ('COMO MUCHO UNA VEZ\nPuede perder → reconciliación', 'gold')],
                 [('SIN ORDEN\nSi importa → Resequencer', 'teal'), ('VENENO\nNunca se procesa → Dead Letter Channel y alarma', 'navy')]],
                note='Cada garantía débil traslada una obligación al receptor. Elegir una garantía es elegir qué patrón se escribe después.',
                note_kind='gold', box_h=86, foot=EJEC)


# ---------------------------------------------------------------- SE-320
def se524_reintentos() -> Fig:
    return grouped_bars(
        'Mil clientes reintentan tras una caída de un segundo: cuatro políticas de espera',
        "Barras agrupadas con el pico de peticiones por 100 milisegundos y los clientes abandonados de mil que reintentan tras una caída de un segundo: el intervalo fijo llega a 1 000 y abandonan 880; el exponencial sin jitter llega a 1 000 y abandonan 520; con jitter completo el pico baja a 537 y con jitter equilibrado a 759, y nadie abandona.",
        ["Intervalo fijo de 100 ms", "Exponencial sin jitter", "Exponencial con jitter completo", "Exponencial con jitter equilibrado"],
        [("Pico de peticiones por 100 ms", [1000, 1000, 537, 759], "coral"), ("Clientes abandonados", [880, 520, 0, 0], "gold")],
        unit="Peticiones por 100 ms o clientes, de 1 000", ticks=[0, 250, 500, 750, 1000],
        note='Sin jitter, los clientes siguen sincronizados y repiten el pico cada ronda. El jitter reparte la carga y todos terminan; la variante fija no gana: abandona 880 clientes tras 12 intentos. Un tope de intentos igual para todas permite comparar.', note_kind='coral', foot=SIM)


def se524_circuit_breaker() -> Fig:
    return stacked_bars(
        'Una dependencia caída 7 segundos con 100 peticiones por segundo, con y sin circuit breaker',
        "Barras apiladas con las 2 000 peticiones de una ventana de veinte segundos con la dependencia caída siete: sin circuit breaker las 2 000 llegan al servicio y no se rechaza ninguna; con circuit breaker llegan 1 307 y se rechazan al instante 693; los éxitos son 1 300 y 1 296.",
        ["Sin circuit breaker", "Con circuit breaker"],
        [("Llamadas al servicio", [2000, 1307], "coral"), ("Rechazadas al instante", [0, 693], "teal")],
        unit="Peticiones", horizontal=True, label_w=170,
        note='El interruptor ahorra 693 llamadas a una dependencia que no puede contestar, a cambio de 4 éxitos menos por los instantes de la recuperación. Protege al llamante y a la dependencia caída; no repara nada.', note_kind='teal', foot=SIM)


def se524_amplificacion() -> Fig:
    return bars('Intentos al servicio por cada petición del usuario en el peor caso',
                'Gráfico de barras con los intentos al servicio por petición del usuario en el peor caso: 27 con tres capas que reintentan tres veces cada una y 1,33 con un presupuesto de reintentos del diez por ciento por capa.',
                [('3 capas × 3 intentos', 27, 'coral', '27'), ('Presupuesto del 10 % por capa', 1.331, 'teal', '1,33')], 12,
                note='La amplificación es multiplicativa: tres capas con tres intentos convierten una petición en veintisiete. Un presupuesto de reintentos acota la suma de los reintentos, no cada llamada.',
                note_kind='coral', foot=EJEC, label_w=360)


# ---------------------------------------------------------------- SE-321
def se525_bulkhead() -> Fig:
    return bars('Una dependencia lenta de 3 segundos entre t=10 y t=30: éxito de las peticiones de la dependencia sana',
                'Gráfico de barras con el porcentaje de peticiones de una dependencia sana que terminan dentro de 0,5 segundos mientras otra dependencia está lenta: 30,6 por ciento con un grupo compartido de 10 hilos y 100 por ciento con un compartimento propio de 8 hilos.',
                [('Grupo compartido de 10 hilos', 30.6, 'coral', '30,6 %'), ('Compartimento propio de 8 hilos', 100, 'teal', '100 %')], 4.0,
                note='Con compartimentos, la dependencia lenta solo ahoga su propio grupo (su éxito baja a 23,4 % en ambos casos). El compartimento no repara la dependencia lenta; limita el daño a quien depende de ella.',
                note_kind='teal', foot=SIM, label_w=380)


def se525_degradacion() -> Fig:
    return bars('Respuestas útiles con una dependencia caída el 40 % del tiempo',
                'Gráfico de barras con el porcentaje de respuestas útiles cuando una dependencia está caída el 40 por ciento del tiempo: 60,0 por ciento sin degradación y 87,5 por ciento con una respuesta degradada desde una caché obsoleta que acierta el 70 por ciento de las veces.',
                [('Sin degradación', 60.0, 'coral', '60,0 %'), ('Con caché obsoleta como respaldo', 87.5, 'teal', '87,5 %')], 4.5,
                note='La degradación cambia la pregunta de «¿funciona?» a «¿qué parte del valor se conserva?». Devolver un dato viejo es una decisión de producto: hay que decir cuánto de viejo es aceptable y avisar a la persona usuaria.',
                note_kind='gold', foot=SIM, label_w=380)


def se525_salto_adicional() -> Fig:
    return grouped_bars(
        'Costo de un salto adicional (ambassador o sidecar) medido con sockets locales',
        "Barras horizontales con la mediana de una petición y su respuesta por sockets locales: unos 61 microsegundos directo del cliente al servidor y unos 122 a través de un intermediario, un salto adicional que cuesta cerca de dos veces la línea base.",
        ["Cliente → servidor (directo)", "Cliente → ambassador → servidor"],
        [("Mediana por petición-respuesta", [61, 122], "teal")],
        unit="Mediana por petición-respuesta (µs)", horizontal=True, label_w=270, ticks=[0, 30, 60, 90, 120, 150],
        note='El sidecar o el ambassador sacan reintentos, TLS o métricas de la aplicación al precio de un salto. En una red real el salto se mide en milisegundos y en el mismo equipo en decenas de microsegundos; esta cifra es de un equipo y de un protocolo trivial.', note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-322
def se526_god_class() -> Fig:
    return grouped_bars(
        'Una clase con demasiadas razones para cambiar, medida antes y después de separarla',
        "Barras agrupadas con una clase de servicio de 10 métodos y 8 dependencias en la que 37 de 45 pares de métodos no comparten estado, y las tres clases en que se separa: Registro tiene 2 métodos, 1 dependencia y 0 de 1 pares sin estado compartido; Notificador 2, 3 y 0 de 1; Migración 3, 1 y 0 de 3.",
        ["Servicio (antes)", "Registro", "Notificador", "Migración"],
        [("Métodos", [10, 2, 2, 3], "grey"), ("Dependencias", [8, 1, 3, 1], "gold"), ("Pares sin estado compartido", [37, 0, 0, 0], "coral")],
        unit="Métodos, dependencias o pares", ticks=[0, 10, 20, 30, 40],
        note='La complejidad ciclomática máxima no cambia (4 antes, 4 después): la clase grande no era difícil por sus ramas sino por sus razones de cambio. Elegir la métrica equivocada habría declarado sano un diseño enfermo.', note_kind='coral', foot=EJEC)


def se526_ciclos() -> Fig:
    return flow('Un ciclo de dependencias entre tres módulos y cómo se rompe',
                'Diagrama de dos filas: en la primera, los módulos avisos, cursos y usuarios se dependen entre sí en un ciclo de tres; en la segunda, los tres dependen de un módulo de dominio común y no se dependen entre sí, y el análisis de componentes fuertemente conexos devuelve un ciclo antes y ninguno después.',
                [[('avisos → cursos, usuarios\ncursos → usuarios, avisos\nusuarios → cursos', 'coral'), ('Tarjan: 1 componente de tamaño 3', 'gold')],
                 [('avisos → dominio\ncursos → dominio\nusuarios → dominio', 'teal'), ('Tarjan: 0 ciclos', 'navy')]],
                note='Un ciclo impide cambiar, probar o desplegar un módulo sin los demás. Se rompe extrayendo lo compartido a un módulo del que todos dependan, no moviendo la dependencia de lugar.',
                note_kind='teal', box_h=96, foot=EJEC)


def se526_interes_de_la_deuda() -> Fig:
    x = list(range(1, 11))
    sin = [4.0, 4.0, 5.2, 5.4, 6.9, 7.4, 9.3, 9.0, 8.9, 10.3]
    con = [4.0, 4.0, 5.4, 5.7, 13.1, 4.0, 4.0, 4.0, 5.6, 5.4]
    return line_chart(
        'Modelo ilustrativo del interés de la deuda: horas por cambio en diez cambios sucesivos',
        "Líneas de un modelo ilustrativo y no medido con las horas por cambio en diez cambios sucesivos: sin pagar la deuda crecen de 4,0 a 10,3 y suman 70,4 horas; pagándola con 6 horas en el cambio 5 el cambio 5 sube a 13,1, después vuelven a 4,0 y el total es 55,2 horas.",
        [("Sin pagar", list(zip(x, sin)), "coral"), ("Pagando 6 h en el cambio 5", list(zip(x, con)), "teal")],
        x_label="Cambio sucesivo", y_label="Horas por cambio", x_ticks=[(i, str(i)) for i in x], y_ticks=[0, 4, 8, 12, 16], decimals=1, point_labels="none",
        annotations=[(5, 13.1, "Cambio 5: 13,1 h (6 h de pago de la deuda)", 30, -6)],
        note='Es un modelo con supuestos del autor (un atajo cada dos cambios, interés lineal): ilustra por qué el costo se acumula, no predice un proyecto. Medir el interés real exige tiempos de cambio de un equipo.', note_kind='gold', foot=SIM)


# ---------------------------------------------------------------- SE-323
def se527_antes_despues() -> Fig:
    return dumbbell(
        'Tarifa de avisos: función con cadena de condiciones frente a Strategy con registro',
        "Puntos unidos por una línea, en escala logarítmica, con tres medidas de una función de tarifas antes y después de refactorizarla a Strategy con registro: la complejidad ciclomática máxima baja de 15 a 3, los nodos de sintaxis suben de 149 a 215 y el tiempo por llamada de unos 260 a unos 380 nanosegundos; las medidas tienen unidades distintas.",
        [("Complejidad ciclomática máxima", 15, 3), ("Nodos de sintaxis", 149, 215), ("Tiempo por llamada (ns)", 260, 380)],
        unit="Valor de cada medida (unidades distintas por fila)", names=("Antes", "Después"), log=True, decimals=0, label_w=260,
        delta=lambda a, b: f"{(b - a) / a * 100:+.0f} %".replace(".", ","),
        note='El refactor compró complejidad por función a cambio de un 44 % más de nodos y una indirección. Si el número de canales no va a crecer, ese costo no se justifica: la condición de salida es volver a una función simple.', note_kind='gold', foot=EJEC)


def se527_maestro_dorado() -> Fig:
    return bars('Seis mutantes del refactor: cuántos detecta el maestro dorado según la distribución de entradas',
                'Gráfico de barras con los mutantes del refactor detectados por un maestro dorado de seis posibles: 2 con 30 entradas aleatorias, 3 con 5000 entradas aleatorias de semilla fija y 6 con 5000 más 384 entradas de frontera.',
                [('30 entradas al azar', 2, 'coral', '2 de 6'), ('5000 entradas al azar', 3, 'gold', '3 de 6'), ('5000 más 384 de frontera', 6, 'teal', '6 de 6')], 70,
                note='Más entradas al azar no atraparon los tres mutantes de frontera: las entradas no tocaban los valores 50, 100 ni 1000. Un maestro dorado es tan bueno como las entradas que elige; los límites hay que escribirlos.',
                note_kind='coral', foot=SIM, label_w=330)


def se527_pasos_del_taller() -> Fig:
    return flow('Los pasos del taller: de la función vieja al patrón, con red de seguridad',
                'Diagrama de cinco cajas en dos filas: registrar el comportamiento actual con un maestro dorado, añadir las entradas de frontera, medir complejidad y tamaño antes, refactorizar a Strategy con registro y volver a medir y comparar; una flecha lleva de la última caja a la decisión de conservar o retirar el patrón.',
                [[('1. REGISTRAR\nMaestro dorado con semilla fija', 'navy'), ('2. FRONTERAS\nAñade las entradas de los límites', 'gold'), ('3. MEDIR ANTES\nComplejidad, nodos, tiempo', 'teal')],
                 [('4. REFACTORIZAR\nStrategy con registro, un paso por vez', 'coral'), ('5. MEDIR Y DECIDIR\nConserva o retira con la condición de salida', 'navy')]],
                note='Sin el paso 2 el maestro deja pasar tres de seis cambios; sin los pasos de medir, el patrón se queda por costumbre.',
                note_kind='gold', box_h=90, foot=EJEC)


# ---------------------------------------------------------------- SE-324
def se528_detectores() -> Fig:
    return grouped_bars(
        'Dos detectores de patrones sobre un corpus etiquetado de 14 fragmentos',
        "Barras agrupadas con los aciertos y errores de dos detectores sobre 14 fragmentos de los que 8 contienen un patrón real: el detector por nombre de clase obtiene 2 verdaderos positivos, 5 falsos positivos y 6 falsos negativos; el detector por estructura obtiene 6, 1 y 2.",
        ["Por nombre de clase", "Por estructura (ast)"],
        [("Verdaderos positivos", [2, 6], "teal"), ("Falsos positivos", [5, 1], "coral"), ("Falsos negativos", [6, 2], "gold")],
        unit="Fragmentos", ticks=[0, 2, 4, 6, 8],
        note='El nombre de una clase es una señal débil: abunda en decoraciones sin estructura y falta en patrones reales. El detector estructural se escribió conociendo parte del corpus y es optimista; el corpus es del autor.', note_kind='coral', foot=EJEC)


def se528_entrada_de_catalogo() -> Fig:
    return flow('Una entrada de catálogo de patrones: campos obligatorios y regla de aceptación',
                'Diagrama de seis cajas en dos filas con los campos de una entrada de catálogo: nombre, fuerza que resuelve, dónde vive en el código, evidencia, costo medido y condición de salida; una entrada sin evidencia, costo o condición de salida no se acepta.',
                [[('NOMBRE\nEl patrón y dónde se aplica', 'navy'), ('FUERZA\nQué dolor resuelve hoy', 'coral'), ('DÓNDE VIVE\nArchivo y clases', 'teal')],
                 [('EVIDENCIA\nMedida o prueba que lo sostiene', 'gold'), ('COSTO\nNodos, indirección, aprendizaje', 'coral'), ('SALIDA\nCuándo y cómo se retira', 'navy')]],
                note='De tres entradas de ejemplo, una está completa, una carece de evidencia, costo y salida, y una carece de costo; solo la primera se acepta.',
                note_kind='teal', box_h=84, foot=EJEC)


def se528_del_codigo_al_catalogo() -> Fig:
    return chain(
        'Del código al catálogo: cuatro pasos y el hecho medido que justifica cada uno',
        "Cadena de cuatro pasos para pasar del código a un catálogo de patrones con el hecho medido de cada uno: el inventario con una regla por nombre da 5 falsos positivos en 14 fragmentos; la verificación con un detector estructural deja 1 falso positivo y 2 negativos; para Strategy hay 44 por ciento más de nodos y la complejidad baja de 15 a 3; en la decisión una entrada sin evidencia no entra.",
        [("1. Inventario", "buscar estructuras con una regla y registrar candidatos · la regla por nombre da 5 falsos positivos en 14", "navy"),
         ("2. Verificación", "una persona lee cada candidato contra la definición · el detector estructural deja 1 falso positivo y 2 falsos negativos", "navy"),
         ("3. Fuerza y costo", "nombrar la fuerza y medir el costo · Strategy: +44 % de nodos, complejidad 15 → 3", "navy"),
         ("4. Decisión", "conservar, simplificar o retirar, con condición de salida · una entrada sin evidencia no entra", "teal")],
        note='El catálogo es un documento vivo que responde por cada patrón del sistema. Su valor no está en la lista sino en las razones y en las salidas que registra.', note_kind='gold', foot=EJEC)


FIGURES = {
    "se-319-receptor-idempotente.svg": se523_receptor_idempotente,
    "se-319-cuatro-patrones.svg": se523_cuatro_patrones,
    "se-319-garantias.svg": se523_garantias,
    "se-320-reintentos.svg": se524_reintentos,
    "se-320-circuit-breaker.svg": se524_circuit_breaker,
    "se-320-amplificacion.svg": se524_amplificacion,
    "se-321-bulkhead.svg": se525_bulkhead,
    "se-321-degradacion.svg": se525_degradacion,
    "se-321-salto-adicional.svg": se525_salto_adicional,
    "se-322-god-class.svg": se526_god_class,
    "se-322-ciclos.svg": se526_ciclos,
    "se-322-interes-de-la-deuda.svg": se526_interes_de_la_deuda,
    "se-323-antes-despues.svg": se527_antes_despues,
    "se-323-maestro-dorado.svg": se527_maestro_dorado,
    "se-323-pasos-del-taller.svg": se527_pasos_del_taller,
    "se-324-detectores.svg": se528_detectores,
    "se-324-entrada-de-catalogo.svg": se528_entrada_de_catalogo,
    "se-324-del-codigo-al-catalogo.svg": se528_del_codigo_al_catalogo,
}
