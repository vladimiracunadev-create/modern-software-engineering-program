"""Figures for SE-523 to SE-528 (integration, resilience, antipatterns and workshop: seeded simulations, ast analysis and a local socket measurement; Windows CPython 3.12; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab
from figures_part40_a import bars, flow

EJEC = "Código ejecutado de verdad (CPython 3.12, Windows 11); los recuentos son deterministas y los tiempos varían de equipo en equipo."
SIM = "Simulación con semilla fija sobre código ejecutado de verdad (CPython 3.12); las magnitudes son de este modelo, no de un sistema real."


# ---------------------------------------------------------------- SE-523
def se523_receptor_idempotente() -> Fig:
    rows = [['Suma real de pagos', '15 682', '0', 'Referencia'],
            ['Sin receptor idempotente', '18 759', '+3 077', '208 duplicados contados dos veces'],
            ['Con receptor idempotente', '15 682', '0', 'Los duplicados se descartan por identificador']]
    return tab('Mil mensajes con entrega al menos una vez: 208 duplicados y la suma de pagos',
               'Tabla con la suma de los pagos de mil mensajes en un canal con entrega al menos una vez y 208 duplicados: la suma real es 15682, sin receptor idempotente da 18759 con un error de 3077, y con receptor idempotente da 15682 porque descarta los duplicados por identificador.',
               ['Variante', 'Suma', 'Error', 'Causa'], rows, [310, 150, 150, 350], row_h=56, size=13,
               note='La entrega al menos una vez es la garantía habitual y barata; la exactamente una vez se construye en el receptor. Sin identificadores estables, el receptor idempotente no se puede escribir.',
               note_kind='coral', foot=SIM)


def se523_cuatro_patrones() -> Fig:
    rows = [['Content-Based Router', 'Mil mensajes por tipo', '601 pagos, 206 avisos, 193 bajas'],
            ['Dead Letter Channel', '200 mensajes, 25 de la muestra son veneno, tope de 3 intentos', '198 procesados, 2 a la cola de cartas muertas, 204 intentos'],
            ['Resequencer', 'Entrega desordenada en ventanas de 6', '977 pares fuera de orden a la entrada, 0 a la salida'],
            ['Correlation Identifier', '20 respuestas desordenadas', '20 de 20 asociadas por identificador; 1 de 20 por posición']]
    return tab('Cuatro patrones de mensajería y lo que se midió con un canal simulado',
               'Tabla con cuatro patrones de mensajería y lo medido en una simulación con semilla fija: el enrutador por contenido reparte mil mensajes en 601 pagos, 206 avisos y 193 bajas; el canal de cartas muertas con tope de 3 intentos procesa 198 de 200 mensajes y aparta 2 con 204 intentos; el reordenador pasa de 977 pares fuera de orden a 0; y el identificador de correlación asocia 20 de 20 respuestas frente a 1 de 20 por posición.',
               ['Patrón', 'Escenario', 'Resultado'], rows, [240, 330, 390], row_h=64, size=13,
               note='El catálogo de Hohpe y Woolf da nombre a los mismos problemas que aparecen con colas, buses y sistemas de eventos de hoy; el nombre sirve para discutir, la medida para decidir.',
               note_kind='teal', foot=SIM)


def se523_garantias() -> Fig:
    return flow('Qué garantía de entrega exige qué patrón en el receptor',
                'Diagrama de cuatro cajas: al menos una vez puede duplicar y exige un receptor idempotente, como mucho una vez puede perder y exige reconciliación, sin orden garantizado exige un reordenador si el orden importa, y el mensaje que nunca se procesa exige un canal de cartas muertas con alarma.',
                [[('AL MENOS UNA VEZ\nPuede duplicar → Idempotent Receiver', 'coral'), ('COMO MUCHO UNA VEZ\nPuede perder → reconciliación', 'gold')],
                 [('SIN ORDEN\nSi importa → Resequencer', 'teal'), ('VENENO\nNunca se procesa → Dead Letter Channel y alarma', 'navy')]],
                note='Cada garantía débil traslada una obligación al receptor. Elegir una garantía es elegir qué patrón se escribe después.',
                note_kind='gold', box_h=86, foot=EJEC)


# ---------------------------------------------------------------- SE-524
def se524_reintentos() -> Fig:
    rows = [['Intervalo fijo de 100 ms', '11 940', '1000', '1100 ms', '880'],
            ['Exponencial sin jitter', '10 320', '1000', '38 300 ms', '520'],
            ['Exponencial con jitter completo', '6230', '537', '7179 ms', '0'],
            ['Exponencial con jitter equilibrado', '5949', '759', '5668 ms', '0']]
    return tab('Mil clientes reintentan tras una caída de un segundo: cuatro políticas de espera',
               'Tabla con cuatro políticas de espera entre reintentos de mil clientes tras una caída de un segundo en un servicio que luego acepta 60 peticiones cada 100 milisegundos: intervalo fijo, 11940 intentos, pico de 1000 peticiones por 100 milisegundos, último éxito a 1100 milisegundos y 880 clientes abandonados; exponencial sin jitter, 10320 intentos, pico de 1000, último éxito a 38300 milisegundos y 520 abandonados; jitter completo, 6230 intentos, pico de 537, último éxito a 7179 milisegundos y ningún abandonado; y jitter equilibrado, 5949 intentos, pico de 759, último éxito a 5668 milisegundos y ningún abandonado.',
               ['Política', 'Intentos', 'Pico por 100 ms', 'Último éxito', 'Abandonados'], rows, [330, 130, 190, 170, 140], row_h=48, size=13,
               note='Sin jitter, los clientes siguen sincronizados y repiten el pico cada ronda. El jitter reparte la carga y todos terminan; la variante fija no gana: abandona 880 clientes tras 12 intentos. Un tope de intentos igual para todas permite comparar.',
               note_kind='coral', foot=SIM)


def se524_circuit_breaker() -> Fig:
    rows = [['Sin circuit breaker', '2000', '0', '1300'],
            ['Con circuit breaker', '1307', '693', '1296']]
    return tab('Una dependencia caída 7 segundos con 100 peticiones por segundo, con y sin circuit breaker',
               'Tabla con una dependencia caída siete segundos dentro de una ventana de veinte con cien peticiones por segundo: sin circuit breaker se hacen 2000 llamadas al servicio, ninguna se rechaza al instante y hay 1300 éxitos; con circuit breaker se hacen 1307 llamadas, 693 se rechazan al instante y hay 1296 éxitos.',
               ['Variante', 'Llamadas al servicio', 'Rechazadas al instante', 'Éxitos'], rows, [320, 220, 250, 170], row_h=60, size=13,
               note='El interruptor ahorra 693 llamadas a una dependencia que no puede contestar, a cambio de 4 éxitos menos por los instantes de la recuperación. Protege al llamante y a la dependencia caída; no repara nada.',
               note_kind='teal', foot=SIM)


def se524_amplificacion() -> Fig:
    return bars('Intentos al servicio por cada petición del usuario en el peor caso',
                'Gráfico de barras con los intentos al servicio por petición del usuario en el peor caso: 27 con tres capas que reintentan tres veces cada una y 1,33 con un presupuesto de reintentos del diez por ciento por capa.',
                [('3 capas × 3 intentos', 27, 'coral', '27'), ('Presupuesto del 10 % por capa', 1.331, 'teal', '1,33')], 24,
                note='La amplificación es multiplicativa: tres capas con tres intentos convierten una petición en veintisiete. Un presupuesto de reintentos acota la suma de los reintentos, no cada llamada.',
                note_kind='coral', foot=EJEC, label_w=360)


# ---------------------------------------------------------------- SE-525
def se525_bulkhead() -> Fig:
    return bars('Una dependencia lenta de 3 segundos entre t=10 y t=30: éxito de las peticiones de la dependencia sana',
                'Gráfico de barras con el porcentaje de peticiones de una dependencia sana que terminan dentro de 0,5 segundos mientras otra dependencia está lenta: 30,6 por ciento con un grupo compartido de 10 hilos y 100 por ciento con un compartimento propio de 8 hilos.',
                [('Grupo compartido de 10 hilos', 30.6, 'coral', '30,6 %'), ('Compartimento propio de 8 hilos', 100, 'teal', '100 %')], 6.5,
                note='Con compartimentos, la dependencia lenta solo ahoga su propio grupo (su éxito baja a 23,4 % en ambos casos). El compartimento no repara la dependencia lenta; limita el daño a quien depende de ella.',
                note_kind='teal', foot=SIM, label_w=380)


def se525_degradacion() -> Fig:
    return bars('Respuestas útiles con una dependencia caída el 40 % del tiempo',
                'Gráfico de barras con el porcentaje de respuestas útiles cuando una dependencia está caída el 40 por ciento del tiempo: 60,0 por ciento sin degradación y 87,5 por ciento con una respuesta degradada desde una caché obsoleta que acierta el 70 por ciento de las veces.',
                [('Sin degradación', 60.0, 'coral', '60,0 %'), ('Con caché obsoleta como respaldo', 87.5, 'teal', '87,5 %')], 8,
                note='La degradación cambia la pregunta de «¿funciona?» a «¿qué parte del valor se conserva?». Devolver un dato viejo es una decisión de producto: hay que decir cuánto de viejo es aceptable y avisar a la persona usuaria.',
                note_kind='gold', foot=SIM, label_w=380)


def se525_salto_adicional() -> Fig:
    rows = [['Cliente → servidor (directo)', '≈61 µs', 'Línea base'],
            ['Cliente → ambassador → servidor', '≈122 µs', 'Un salto más, ≈2 veces']]
    return tab('Costo de un salto adicional (ambassador o sidecar) medido con sockets locales',
               'Tabla con la mediana de una petición y su respuesta por sockets locales: unos 61 microsegundos directo del cliente al servidor y unos 122 microsegundos a través de un intermediario, aproximadamente el doble, con 2000 repeticiones tras 100 de calentamiento.',
               ['Camino', 'Mediana por petición-respuesta', 'Lectura'], rows, [380, 300, 280], row_h=56, size=13,
               note='El sidecar o el ambassador sacan reintentos, TLS o métricas de la aplicación al precio de un salto. En una red real el salto se mide en milisegundos y en el mismo equipo en decenas de microsegundos; esta cifra es de un equipo y de un protocolo trivial.',
               note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-526
def se526_god_class() -> Fig:
    rows = [['Servicio (antes)', '10', '8', '37 de 45'], ['Registro', '2', '1', '0 de 1'], ['Notificador', '2', '3', '0 de 1'], ['Migración', '3', '1', '0 de 3']]
    return tab('Una clase con demasiadas razones para cambiar, medida antes y después de separarla',
               'Tabla con una clase de servicio de diez métodos y ocho dependencias en la que 37 de 45 pares de métodos no comparten estado, y las tres clases en que se separa, Registro, Notificador y Migración, con 2, 2 y 3 métodos y ningún par sin estado compartido; la complejidad ciclomática máxima por función es 4 antes y 4 después.',
               ['Clase', 'Métodos', 'Dependencias', 'Pares sin estado compartido'], rows, [310, 150, 190, 310], row_h=46, size=13,
               note='La complejidad ciclomática máxima no cambia (4 antes, 4 después): la clase grande no era difícil por sus ramas sino por sus razones de cambio. Elegir la métrica equivocada habría declarado sano un diseño enfermo.',
               note_kind='coral', foot=EJEC)


def se526_ciclos() -> Fig:
    return flow('Un ciclo de dependencias entre tres módulos y cómo se rompe',
                'Diagrama de dos filas: en la primera, los módulos avisos, cursos y usuarios se dependen entre sí en un ciclo de tres; en la segunda, los tres dependen de un módulo de dominio común y no se dependen entre sí, y el análisis de componentes fuertemente conexos devuelve un ciclo antes y ninguno después.',
                [[('avisos → cursos, usuarios\ncursos → usuarios, avisos\nusuarios → cursos', 'coral'), ('Tarjan: 1 componente de tamaño 3', 'gold')],
                 [('avisos → dominio\ncursos → dominio\nusuarios → dominio', 'teal'), ('Tarjan: 0 ciclos', 'navy')]],
                note='Un ciclo impide cambiar, probar o desplegar un módulo sin los demás. Se rompe extrayendo lo compartido a un módulo del que todos dependan, no moviendo la dependencia de lugar.',
                note_kind='teal', box_h=96, foot=EJEC)


def se526_interes_de_la_deuda() -> Fig:
    rows = [['Sin pagar', '4,0 · 4,0 · 5,2 · 5,4 · 6,9 · 7,4 · 9,3 · 9,0 · 8,9 · 10,3', '70,4 h'],
            ['Pagando 6 h en el cambio 5', '4,0 · 4,0 · 5,4 · 5,7 · 13,1 · 4,0 · 4,0 · 4,0 · 5,6 · 5,4', '55,2 h']]
    return tab('Modelo ilustrativo del interés de la deuda: horas por cambio en diez cambios sucesivos',
               'Tabla con un modelo ilustrativo y no medido de diez cambios sucesivos: sin pagar la deuda las horas por cambio crecen de 4,0 a 10,3 y suman 70,4 horas; pagándola con 6 horas en el cambio cinco el cambio cinco cuesta 13,1 y luego vuelve a 4,0, y el total es 55,2 horas.',
               ['Escenario', 'Horas por cambio (cambios 1 a 10)', 'Total'], rows, [260, 560, 140], row_h=64, size=13,
               note='Es un modelo con supuestos del autor (un atajo cada dos cambios, interés lineal): ilustra por qué el costo se acumula, no predice un proyecto. Medir el interés real exige tiempos de cambio de un equipo.',
               note_kind='gold', foot=SIM)


# ---------------------------------------------------------------- SE-527
def se527_antes_despues() -> Fig:
    rows = [['Complejidad ciclomática máxima', '15', '3'], ['Nodos de sintaxis', '149', '215'], ['Tiempo por llamada', '≈260 ns', '≈380 ns'], ['Entradas del maestro dorado en que difiere', '—', '0 de 5000'], ['Complejidad al añadir un canal', '16 (+1)', 'una clase nueva, 0 funciones tocadas']]
    return tab('Tarifa de avisos: función con cadena de condiciones frente a Strategy con registro',
               'Tabla con la comparación de una función de tarifas con una cadena de condiciones y su refactor a Strategy con registro: la complejidad máxima baja de 15 a 3, los nodos suben de 149 a 215, el tiempo por llamada sube de unos 260 a unos 380 nanosegundos, el refactor difiere en 0 de 5000 entradas del maestro dorado y añadir un canal sube la complejidad de la función antigua a 16 y en la nueva solo añade una clase.',
               ['Medida', 'Antes', 'Después'], rows, [470, 230, 260], row_h=52, size=13,
               note='El refactor compró complejidad por función a cambio de un 44 % más de nodos y una indirección. Si el número de canales no va a crecer, ese costo no se justifica: la condición de salida es volver a una función simple.',
               note_kind='gold', foot=EJEC)


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


# ---------------------------------------------------------------- SE-528
def se528_detectores() -> Fig:
    rows = [['Por nombre de clase', '2', '5', '6', '29 %', '25 %'], ['Por estructura (ast)', '6', '1', '2', '86 %', '75 %']]
    return tab('Dos detectores de patrones sobre un corpus etiquetado de 14 fragmentos',
               'Tabla con dos detectores de patrones sobre un corpus de 14 fragmentos de los que 8 contienen un patrón real: el detector por nombre de clase obtiene 2 verdaderos positivos, 5 falsos positivos y 6 falsos negativos con una precisión del 29 por ciento y una exhaustividad del 25 por ciento, y el detector por estructura obtiene 6, 1 y 2 con una precisión del 86 por ciento y una exhaustividad del 75 por ciento.',
               ['Detector', 'Verdaderos +', 'Falsos +', 'Falsos −', 'Precisión', 'Exhaustividad'], rows, [260, 150, 130, 130, 140, 150], row_h=52, size=13,
               note='El nombre de una clase es una señal débil: abunda en decoraciones sin estructura y falta en patrones reales. El detector estructural se escribió conociendo parte del corpus y es optimista; el corpus es del autor.',
               note_kind='coral', foot=EJEC)


def se528_entrada_de_catalogo() -> Fig:
    return flow('Una entrada de catálogo de patrones: campos obligatorios y regla de aceptación',
                'Diagrama de seis cajas en dos filas con los campos de una entrada de catálogo: nombre, fuerza que resuelve, dónde vive en el código, evidencia, costo medido y condición de salida; una entrada sin evidencia, costo o condición de salida no se acepta.',
                [[('NOMBRE\nEl patrón y dónde se aplica', 'navy'), ('FUERZA\nQué dolor resuelve hoy', 'coral'), ('DÓNDE VIVE\nArchivo y clases', 'teal')],
                 [('EVIDENCIA\nMedida o prueba que lo sostiene', 'gold'), ('COSTO\nNodos, indirección, aprendizaje', 'coral'), ('SALIDA\nCuándo y cómo se retira', 'navy')]],
                note='De tres entradas de ejemplo, una está completa, una carece de evidencia, costo y salida, y una carece de costo; solo la primera se acepta.',
                note_kind='teal', box_h=84, foot=EJEC)


def se528_del_codigo_al_catalogo() -> Fig:
    rows = [['1. Inventario', 'Buscar estructuras con una regla y registrar candidatos', 'La regla por nombre da 5 falsos positivos en 14'],
            ['2. Verificación', 'Una persona lee cada candidato contra la definición del patrón', 'El detector estructural deja 1 falso positivo y 2 falsos negativos'],
            ['3. Fuerza y costo', 'Para cada patrón confirmado, nombrar la fuerza y medir el costo', 'Strategy: +44 % de nodos, complejidad 15 → 3'],
            ['4. Decisión', 'Conservar, simplificar o retirar, con condición de salida', 'Una entrada sin evidencia no entra']]
    return tab('Del código al catálogo: cuatro pasos y el hecho medido que justifica cada uno',
               'Tabla con cuatro pasos para pasar del código a un catálogo de patrones: inventario con una regla que por nombre da cinco falsos positivos en catorce fragmentos, verificación por una persona que deja un falso positivo y dos falsos negativos con el detector estructural, fuerza y costo con el ejemplo de Strategy que sube un 44 por ciento los nodos y baja la complejidad de 15 a 3, y decisión de conservar, simplificar o retirar con condición de salida.',
               ['Paso', 'Qué se hace', 'Hecho medido que lo justifica'], rows, [190, 400, 370], row_h=64, size=13,
               note='El catálogo es un documento vivo que responde por cada patrón del sistema. Su valor no está en la lista sino en las razones y en las salidas que registra.',
               note_kind='gold', foot=EJEC)


FIGURES = {
    "se-523-receptor-idempotente.svg": se523_receptor_idempotente,
    "se-523-cuatro-patrones.svg": se523_cuatro_patrones,
    "se-523-garantias.svg": se523_garantias,
    "se-524-reintentos.svg": se524_reintentos,
    "se-524-circuit-breaker.svg": se524_circuit_breaker,
    "se-524-amplificacion.svg": se524_amplificacion,
    "se-525-bulkhead.svg": se525_bulkhead,
    "se-525-degradacion.svg": se525_degradacion,
    "se-525-salto-adicional.svg": se525_salto_adicional,
    "se-526-god-class.svg": se526_god_class,
    "se-526-ciclos.svg": se526_ciclos,
    "se-526-interes-de-la-deuda.svg": se526_interes_de_la_deuda,
    "se-527-antes-despues.svg": se527_antes_despues,
    "se-527-maestro-dorado.svg": se527_maestro_dorado,
    "se-527-pasos-del-taller.svg": se527_pasos_del_taller,
    "se-528-detectores.svg": se528_detectores,
    "se-528-entrada-de-catalogo.svg": se528_entrada_de_catalogo,
    "se-528-del-codigo-al-catalogo.svg": se528_del_codigo_al_catalogo,
}
