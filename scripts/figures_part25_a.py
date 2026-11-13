"""Figures for SE-301 to SE-306 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."
REAL = "Medición real en bucle local: depende de la máquina; rangos de cinco ejecuciones en Windows y cuatro en Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-301
def se301_pico() -> Fig:
    rows = [
        ["4", "26,3 s", "76,6 s", "81,2 s", "70,6 %"],
        ["5", "0,155 s", "0,514 s", "0,707 s", "0 %"],
        ["6", "0,113 s", "0,265 s", "0,367 s", "0 %"],
        ["8", "0,102 s", "0,230 s", "0,325 s", "0 %"],
        ["16", "0,100 s", "0,227 s", "0,322 s", "0 %"],
    ]
    return tab("Latencia de la entrega en el pico según el número de trabajadores (33 803 peticiones)",
               "Tabla: con cuatro trabajadores, que no alcanzan para 40 peticiones por segundo, la mediana de latencia es 26,3 segundos y el 70,6 por ciento tarda más de 2 segundos; con cinco trabajadores el percentil 95 baja a 0,514 segundos y de seis a dieciséis casi no cambia.",
               ["Trabajadores", "Mediana", "Percentil 95", "Percentil 99", "Más de 2 s"], rows, [190, 190, 190, 190, 190], row_h=40, size=13,
               note="El umbral no es gradual: con 4 trabajadores la capacidad (unas 35 peticiones por segundo) queda por debajo de la llegada del pico (40) y la cola crece hasta el final de la ráfaga; con 5 o más el sistema se comporta como si no hubiera pico. Un escenario de calidad que diga «p95 de 2 s a 40 rps» detecta el umbral; «debe ser rápido» no.",
               note_kind="coral", foot=SINT)


def se301_serie() -> Fig:
    rows = [
        ["1", "99,900 %", "43,2", "0,04", "—"],
        ["3", "99,700 %", "129,5", "0,13", "36,5"],
        ["5", "99,501 %", "215,6", "0,22", "65,3"],
        ["8", "99,203 %", "344,4", "0,35", "—"],
    ]
    return tab("Minutos de caída al mes de una cadena de componentes con 99,9 % cada uno",
               "Tabla: una cadena en serie de tres componentes con disponibilidad de 99,9 por ciento cada uno da 99,7 por ciento y 129,5 minutos de caída al mes; con dos réplicas independientes la cuenta teórica baja a 0,13 minutos, pero si el 30 por ciento de las caídas es de causa común la simulación da 36,5 minutos.",
               ["Componentes en serie", "Disponibilidad", "Min/mes sin réplica", "Min/mes, 2 réplicas independientes", "Min/mes, 2 réplicas y 30 % de causa común"], rows, [150, 150, 190, 250, 260], row_h=58, size=12,
               note="Duplicar cada componente reduce la caída unas 1000 veces solo si las caídas son independientes. Con un 30 % de causa común (despliegue, configuración, dependencia compartida) la mejora real es 3,5 veces, no 1000. La causa común es un supuesto del autor; el mecanismo es el que importa.",
               note_kind="gold", foot=SINT)


def se301_pareto() -> Fig:
    items = [("2 atributos", 6, "teal", "6 de 300"), ("3 atributos", 24, "teal", "24 de 300"), ("5 atributos", 105, "gold", "105 de 300"),
             ("8 atributos", 215, "coral", "215 de 300")]
    return bars("Candidatos no dominados entre 300 al azar según cuántos atributos se comparan",
                "Barras: de 300 arquitecturas candidatas al azar, quedan 6 sin dominar al comparar dos atributos, 24 con tres, 105 con cinco y 215 con ocho; con tres atributos del caso, latencia, costo y complejidad, solo 13 de 300 son no dominadas y 4 cumplen además las restricciones.",
                items, 2.0, "Cuantos más atributos se comparan, menos candidatos se pueden descartar por ser peores en todo y más decisiones dependen de pesos. Con latencia, costo y complejidad hay 13 candidatos no dominados; solo 4 cumplen además latencia ≤ 200 ms, costo ≤ 8 y complejidad ≤ 5. Las restricciones, no los pesos, hicieron la mayor parte del filtro. Candidatos y valores son sintéticos.",
                label_w=160, width=960, note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-302
def se302_trazas() -> Fig:
    rows = [
        ["100", "1 de 3", "1 de 1"],
        ["1 000", "2 de 3", "1 de 1"],
        ["5 000", "3 de 3", "1 de 1"],
        ["100 000", "3 de 3", "1 de 1"],
    ]
    return tab("Dependencias reales no declaradas en la vista lógica según cuántas trazas se miran",
               "Tabla: al comparar la vista lógica con trazas de ejecución, 100 peticiones revelan una de tres dependencias no declaradas, 1000 revelan dos y hacen falta unas 5000 para ver las tres; la dependencia declarada y nunca usada aparece desde la primera muestra.",
               ["Peticiones analizadas", "No declaradas vistas", "Declarada sin uso vista"], rows, [300, 300, 300], row_h=40, size=13,
               note="Las tres dependencias tienen probabilidad 4 %, 0,5 % y 0,1 % por petición; la probabilidad de ver la última en n peticiones es 1 − (1 − p)ⁿ, 63 % con 1000 y 99 % con 5000. Que una traza no muestre una arista no prueba que no exista: solo acota con qué probabilidad la habríamos visto.",
               note_kind="gold", foot=SINT)


def se302_explosion() -> Fig:
    rows = [
        ["Un solo servidor", "4 de 4", "—"],
        ["Aplicación y base de datos separadas", "4 de 4", "ninguno"],
        ["3 nodos, solo la base replicada", "4 de 4", "n2: 1 · n3: 3"],
        ["3 nodos, web, identidad y base replicadas", "3 de 4", "n1: 0 · n2: 1"],
    ]
    return tab("Recorridos de usuario rotos por la caída del peor nodo (4 recorridos, 9 componentes)",
               "Tabla: en un solo servidor la caída del único nodo rompe los 4 recorridos de usuario; separar aplicación y base no cambia el peor nodo; replicar solo la base lo deja en 4 de 4 porque la web sigue sola en un nodo; replicar también web e identidad baja el peor caso a 3 de 4.",
               ["Topología", "Peor nodo", "Otros nodos"], rows, [480, 200, 220], row_h=44, size=13,
               note="Replicar la base de datos no protege si la puerta de entrada (la web) vive en un único nodo: los cuatro recorridos pasan por ella. La vista de despliegue se lee contra los recorridos, no componente por componente. Los recorridos y los nodos son del autor; no se simuló ninguna caída real.",
               note_kind="coral", foot=SINT)


def se302_cadena() -> Fig:
    rows = [
        ["1", "20,0", "80,6", "20,0", "80,6", "1,0 %"],
        ["2", "43,4", "122,9", "27,7", "94,1", "2,0 %"],
        ["4", "90,8", "193,7", "36,4", "108,0", "3,9 %"],
        ["8", "186,3", "321,1", "45,8", "122,2", "7,7 %"],
    ]
    return tab("Latencia (ms) de una petición que atraviesa N servicios con mediana de 20 ms cada uno",
               "Tabla: con ocho servicios llamados en serie la mediana es 186 milisegundos y el percentil 99 321; llamados en paralelo 46 y 122; y la probabilidad de que alguna de las ocho llamadas supere su propio percentil 99 es 7,7 por ciento.",
               ["N", "Serie p50", "Serie p99", "Paralelo p50", "Paralelo p99", "Alguna llamada sobre su p99"], rows, [90, 160, 160, 170, 170, 230], row_h=40, size=13,
               note="En serie las latencias se suman y la cola se acumula; en paralelo manda el más lento. La probabilidad de tocar una llamada lenta crece como 1 − 0,99ᴺ. La vista de runtime muestra esas rutas; la lógica no. Latencias lognormales sintéticas (σ = 0,6) y llamadas independientes, un supuesto que la contención real rompe.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-303
def se303_llamada() -> Fig:
    rows = [
        ["Llamada de función en el mismo proceso", "0,22 – 0,84 µs", "1×"],
        ["Serializar y deserializar JSON ida y vuelta", "10,7 – 36,9 µs", "34 – 59×"],
        ["Ida y vuelta TCP en bucle local, mediana", "117 – 201 µs", "203 – 765×"],
        ["Ida y vuelta TCP en bucle local, percentil 99", "227 – 686 µs", "—"],
    ]
    return tab("Coste de una llamada: en proceso, serializada y por TCP en bucle local",
               "Tabla: una llamada de función tarda entre 0,22 y 0,84 microsegundos; serializar la petición con JSON entre 10,7 y 36,9; una ida y vuelta TCP en bucle local entre 117 y 201 microsegundos en la mediana, entre 203 y 765 veces la llamada local.",
               ["Operación", "Tiempo", "Razón sobre la llamada local"], rows, [470, 190, 250], row_h=44, size=13,
               note="Medición real, sin red: el bucle local no tiene latencia de enlace, balanceador ni TLS, así que subestima el coste de cruzar una máquina. Las cifras cambian con la máquina; el orden de magnitud (dos o tres décimas de millar de veces) es lo que se repite. Una operación con 20 llamadas internas pasa de unos 7 µs a unos 2,3 ms si cada una cruza la red.",
               note_kind="gold", foot=REAL)


def se303_consistencia() -> Fig:
    rows = [
        ["0,1 %", "99,69 %", "0,22 %", "0,02 %"],
        ["1 %", "97,01 %", "1,98 %", "0,14 %"],
        ["5 %", "85,78 %", "9,27 %", "0,69 %"],
    ]
    return tab("Operación que cruza tres servicios: estados inconsistentes con y sin compensación",
               "Tabla: si cada una de tres llamadas remotas falla con probabilidad 1 por ciento, sin compensación el 1,98 por ciento de las operaciones queda inconsistente; con compensación que falla el 5 por ciento de las veces queda el 0,14 por ciento; con 5 por ciento de fallo por llamada quedan 9,27 y 0,69 por ciento.",
               ["Fallo por llamada", "Operaciones completas", "Inconsistentes sin compensación", "Inconsistentes con compensación (5 % de fallo)"], rows, [200, 230, 270, 310], row_h=52, size=13,
               note="Una transacción local en el monolito deja 0 filas tras un fallo (se comprobó con SQLite). Entre servicios, la consistencia se compra con compensaciones, que también pueden fallar: no desaparece el estado intermedio, se reduce y se vuelve observable. 200 000 operaciones por celda; fallos independientes por supuesto.",
               note_kind="coral", foot=SINT)


def se303_fronteras() -> Fig:
    items = [("Inyectadas", 30, "grey", "30 (4 permitidas)"), ("Violaciones reales", 26, "gold", "26"),
             ("Detectadas por el análisis estático", 16, "teal", "16 (0 falsos positivos)"), ("Importaciones dinámicas no vistas", 10, "coral", "10")]
    return bars("Un comprobador de fronteras de un monolito modular (análisis estático con ast)",
                "Barras: de 30 importaciones inyectadas en un proyecto sintético de seis módulos, 4 eran permitidas y 26 violaban la frontera; el análisis estático detecta 16 sin falsos positivos y no ve las 10 que usan importación dinámica.",
                items, 11, "El comprobador lee los nodos de importación y detecta 16 de las 26 violaciones sin marcar ninguna de las permitidas; las 10 con `__import__` o `importlib` quedan fuera. Una regla de frontera comprobable es necesaria pero no suficiente: hace falta una segunda regla (prohibir la importación dinámica entre módulos) o una prueba en tiempo de ejecución.",
                label_w=330, width=1000, note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-304
def se304_impacto() -> Fig:
    rows = [
        ["Capas clásicas", "94", "17", "3", "30"],
        ["Capas con fugas", "102", "17", "3", "30"],
        ["Hexagonal", "86", "2", "0", "0"],
    ]
    return tab("Módulos que dependen de la base de datos (40 módulos: 15 de dominio, 10 de aplicación, 8 web, 7 de infraestructura)",
               "Tabla: al cambiar la base de datos, en una estructura por capas 17 de 40 módulos dependen de ella, entre ellos 3 de dominio y 6 de aplicación, y hay 30 dependencias del dominio hacia la infraestructura; en la estructura hexagonal dependen 2 módulos, ninguno de dominio, y hay 0 dependencias del dominio hacia la infraestructura.",
               ["Estructura", "Aristas", "Dependientes de la BD", "De ellos de dominio", "Dependencias dominio → infra"], rows, [230, 120, 260, 220, 230], row_h=40, size=13,
               note="La dirección de la dependencia, no el número de capas, decide cuánto arrastra un cambio: invertirla en el borde (infraestructura → puerto del dominio) reduce los dependientes de 17 a 2. Los grafos son sintéticos con semilla fija y miden estructura, no esfuerzo. Aun así «hexagonal» no garantiza nada si los adaptadores filtran tipos de la base al dominio.",
               note_kind="teal", foot=SINT)


def se304_pruebas() -> Fig:
    rows = [
        ["Doble en memoria", "0,008 – 0,044 ms", "1×"],
        ["SQLite en memoria", "0,26 – 0,83 ms", "16 – 41×"],
        ["SQLite en archivo temporal", "102 – 133 ms", "2 587 – 16 136×"],
    ]
    return tab("Una prueba de la regla de promedio con tres implementaciones del repositorio (mediana de 60 ejecuciones)",
               "Tabla: la misma prueba de la regla de promedio tarda entre 0,008 y 0,044 milisegundos con un doble en memoria, entre 0,26 y 0,83 con SQLite en memoria y entre 102 y 133 con SQLite en un archivo, entre 2587 y 16136 veces más que el doble.",
               ["Implementación del puerto", "Mediana por prueba", "Razón sobre el doble"], rows, [330, 270, 290], row_h=40, size=13,
               note="El puerto hace que la regla se pueda probar a velocidad de función. Medición real con crear el repositorio y 20 inserciones por prueba; el coste del archivo se debe sobre todo a crear, sincronizar y borrar un archivo, no a la regla. Es la razón por la que un doble necesita pruebas de contrato: es rápido, pero no demuestra que el adaptador real se comporte igual.",
               note_kind="gold", foot=REAL)


def se304_contrato() -> Fig:
    items = [("3 ejemplos de camino feliz", 1, "coral", "1 de 7"), ("Pruebas de contrato del puerto", 7, "teal", "7 de 7")]
    return bars("Defectos sembrados en dobles del repositorio que detecta cada suite",
                "Barras: de siete defectos sembrados en dobles de un repositorio, entre ellos duplicar al guardar, no reemplazar, no ordenar y devolver referencias compartidas, tres ejemplos de camino feliz matan 1 y una suite de contrato escrita contra el comportamiento de referencia mata los 7.",
                items, 50, "El contrato fija lo que el puerto promete (orden, aislamiento por curso, reemplazo sin duplicar, ausencia como None, rechazo de notas fuera de 1 a 7, copia defensiva). Se ejecuta contra todos los dobles y contra el adaptador real. Los defectos son sembrados por el autor: miden la capacidad de detectar esas siete formas de desviación, no la tasa de defectos de un repositorio.",
                label_w=300, width=960, note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-305
def se305_contextos() -> Fig:
    items = [("Un único modelo de 14 atributos", 56.8, "coral", "56,8 %"), ("Tres contextos con 3 atributos de contrato", 20.2, "teal", "20,2 %")]
    return bars("Probabilidad de que un cambio de un atributo afecte a código de otro equipo",
                "Barras: con un único modelo compartido de 14 atributos, el 56,8 por ciento de los cambios de un atributo afecta a código de otro de los tres equipos; con tres contextos y tres atributos de contrato compartidos baja al 20,2 por ciento.",
                items, 8.0, "Fronteras explícitas no eliminan el acoplamiento: lo concentran en el contrato (3 atributos). Las lecturas de cada equipo (5 a 9 atributos en el modelo único; 3 a 5 propios más el contrato) son supuestos del autor sobre 20 000 modelos al azar. El resultado depende de que el contrato sea pequeño y estable.",
                label_w=380, width=1000, note_kind="teal", foot=SINT)


def se305_agregado() -> Fig:
    rows = [
        ["2", "6", "4", "0"],
        ["3", "90", "72", "0"],
        ["4", "2 520", "2 160", "0"],
    ]
    return tab("Intercalaciones en las que se acepta más de un reenvío cuando el agregado admitía uno",
               "Tabla: con dos comandos concurrentes de reenvío de una entrega, 4 de las 6 intercalaciones posibles aceptan dos reenvíos cuando solo cabía uno; con tres comandos son 72 de 90 y con cuatro 2160 de 2520; con comprobación de versión del agregado ninguna lo permite.",
               ["Comandos concurrentes", "Intercalaciones", "Violan el invariante sin control", "Violan con versión"], rows, [250, 220, 280, 190], row_h=44, size=13,
               note="Leer, validar y escribir sin condición permite que dos comandos validen contra el mismo estado. Comparar la versión leída con la actual al escribir convierte la carrera en un rechazo reintentable. Se enumeraron todas las intercalaciones de pasos leer/escribir; no se usó una base de datos real, así que no se midió el coste de los reintentos.",
               note_kind="coral", foot=SINT)


def se305_notas() -> Fig:
    rows = [
        ["Float con round()", "930 de 1 860", "50 %"],
        ["Decimal con redondeo por defecto (half-even)", "930 de 1 860", "50 %"],
        ["Decimal con half-up declarado", "0 de 1 860", "0 %"],
        ["Enteros en décimas con half-up", "0 de 1 860", "0 %"],
    ]
    return tab("Promedio de dos notas (1,0 a 7,0): empates exactos que se redondean distinto de la regla «medio hacia arriba»",
               "Tabla: de los 1860 pares de notas cuyo promedio cae exactamente en medio de dos décimas, el float con round y el decimal con redondeo por defecto se apartan de la regla de redondear medio hacia arriba en 930, la mitad; el decimal con half-up declarado y los enteros en décimas no se apartan en ninguno.",
               ["Representación de la nota", "Pares que difieren", "Proporción"], rows, [480, 230, 190], row_h=44, size=13,
               note="Ejemplo: 1,0 y 1,3 promedian 1,15; con float el resultado es 1,1 en lugar de 1,2. Un objeto de valor Nota que encapsula la representación y la regla de redondeo hace que la regla viva en un sitio y se pruebe contra todos los pares. Comprobado con Fraction como referencia exacta.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-306
def se306_consumo() -> Fig:
    rows = [
        ["Sin duplicados ni desorden", "0", "0", "0", "0"],
        ["5 % de duplicados", "1 824", "0", "0", "0"],
        ["Desorden de hasta 30 posiciones", "0", "0", "6", "0"],
        ["Duplicados y desorden", "1 824", "0", "2", "0"],
    ]
    return tab("Entregas (de 2000) con estado erróneo según cómo procesa el consumidor",
               "Tabla: con 5 por ciento de duplicados, un contador ingenuo da un valor erróneo en 1824 de 2000 entregas y un contador idempotente por identificador de evento en ninguna; con desorden, quedarse con la última llegada falla en 6 entregas y quedarse con la mayor secuencia en ninguna.",
               ["Flujo de eventos", "Contador ingenuo", "Contador idempotente", "Última llegada gana", "Mayor secuencia gana"], rows, [270, 160, 190, 190, 190], row_h=44, size=13,
               note="Los duplicados rompen lo que acumula; el desorden rompe lo que sobrescribe. Un identificador de evento y un número de secuencia por entidad son el contrato mínimo para que un consumidor sea correcto con entrega al-menos-una-vez. 100 000 eventos sintéticos sobre 2000 entregas, semilla fija.",
               note_kind="coral", foot=SINT)


def se306_reconstruccion() -> Fig:
    rows = [
        ["Nunca", "5 021", "9 893", "0"],
        ["Cada 1 000 eventos", "507", "991", "10"],
        ["Cada 200 eventos", "99", "198", "50"],
        ["Cada 50 eventos", "24", "49", "200"],
    ]
    return tab("Eventos que hay que aplicar para reconstruir un agregado de 10 000 eventos (5000 consultas)",
               "Tabla: reconstruir el estado de un agregado de 10000 eventos sin instantáneas aplica en media 5021 eventos y en el percentil 99 9893; con una instantánea cada 1000 baja a 507 y 991, cada 200 a 99 y 198 y cada 50 a 24 y 49, a costa de 10, 50 y 200 instantáneas almacenadas.",
               ["Instantánea", "Eventos aplicados, media", "Percentil 99", "Instantáneas guardadas"], rows, [280, 250, 190, 230], row_h=44, size=13,
               note="El coste de reconstruir es proporcional a la distancia hasta la última instantánea; el de guardarlas, a su número. El agregado «curso» recibe un evento por entrega (4 800 por periodo con 400 estudiantes y 12 tareas): agregados que crecen sin límite piden otro diseño del límite. Se contaron eventos aplicados, no segundos.",
               note_kind="gold", foot=SINT)


def se306_lectura() -> Fig:
    rows = [
        ["60 por segundo", "0,02 s", "0,2 s", "0,0 %", "0,0 %"],
        ["45 por segundo", "0,04 s", "0,8 s", "0,4 %", "0,0 %"],
        ["41 por segundo", "0,06 s", "3,3 s", "13,5 %", "0,0 %"],
        ["38 por segundo", "0,09 s", "13,4 s", "27,8 %", "15,3 %"],
    ]
    return tab("Retraso del modelo de lectura en un pico de 40 eventos por segundo (5 minutos)",
               "Tabla: con un proyector que procesa 60 eventos por segundo el modelo de lectura se retrasa 0,2 segundos en el percentil 99 y nadie deja de ver su entrega; con 41 por segundo el percentil 99 sube a 3,3 segundos y el 13,5 por ciento no la ve al recargar a 1 segundo; con 38, por debajo de la llegada, el retraso sube a 13,4 segundos.",
               ["Capacidad del proyector", "Retraso p50", "Retraso p99", "No ve su entrega a 1 s", "No la ve a 5 s"], rows, [250, 150, 150, 190, 150], row_h=44, size=13,
               note="La consistencia eventual es un número, no un adjetivo: depende de cuánto margen tiene el proyector sobre el pico. Cuando la capacidad cae por debajo de la llegada la cola crece mientras dure la ráfaga. Un token de lectura propia (esperar la versión escrita) arregla la percepción de quien escribió sin eliminar el retraso para los demás.",
               note_kind="coral", foot=SINT)


FIGURES = {
    "se-301-pico-de-entrega.svg": se301_pico,
    "se-301-disponibilidad-en-serie.svg": se301_serie,
    "se-301-frontera-de-pareto.svg": se301_pareto,
    "se-302-trazas-y-vista-logica.svg": se302_trazas,
    "se-302-radio-de-explosion.svg": se302_explosion,
    "se-302-latencia-de-una-cadena.svg": se302_cadena,
    "se-303-coste-de-una-llamada.svg": se303_llamada,
    "se-303-consistencia-entre-servicios.svg": se303_consistencia,
    "se-303-fronteras-de-un-monolito-modular.svg": se303_fronteras,
    "se-304-impacto-de-cambiar-la-base.svg": se304_impacto,
    "se-304-velocidad-de-las-pruebas.svg": se304_pruebas,
    "se-304-pruebas-de-contrato.svg": se304_contrato,
    "se-305-acoplamiento-entre-contextos.svg": se305_contextos,
    "se-305-invariante-de-un-agregado.svg": se305_agregado,
    "se-305-redondeo-de-notas.svg": se305_notas,
    "se-306-consumidores-de-eventos.svg": se306_consumo,
    "se-306-reconstruccion-con-instantaneas.svg": se306_reconstruccion,
    "se-306-retraso-del-modelo-de-lectura.svg": se306_lectura,
}
