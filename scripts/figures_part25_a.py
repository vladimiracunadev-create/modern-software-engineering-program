"""Figures for SE-301 to SE-306 (synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, fmt_es, grouped_bars, heatmap, line_chart, percentile_intervals, stacked_bars
from figures_part07_a import bars

SINT = "Simulación sintética con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."
REAL = "Medición real en bucle local: depende de la máquina; rangos de cinco ejecuciones en Windows y cuatro en Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-301
def se301_pico() -> Fig:
    return percentile_intervals(
        "Latencia de la entrega en el pico según el número de trabajadores (33 803 peticiones)",
        "Intervalos en escala logarítmica con la mediana, el percentil 95 y el percentil 99 de la latencia de la entrega: con cuatro trabajadores la mediana ya es 26,3 segundos y el percentil 99 llega a 81,2; con cinco el percentil 95 baja a 0,514 segundos, por debajo del límite de 2 segundos, y de seis a dieciséis trabajadores casi no cambia.",
        [("4 trabajadores", [26.3, 76.6, 81.2]), ("5 trabajadores", [0.155, 0.514, 0.707]), ("6 trabajadores", [0.113, 0.265, 0.367]),
         ("8 trabajadores", [0.102, 0.230, 0.325]), ("16 trabajadores", [0.100, 0.227, 0.322])],
        unit="Latencia de la entrega (s)", marks=("p50", "p95", "p99"), log=True, ref_lines=[(2, "límite p95 = 2 s")],
        note="El umbral no es gradual: con 4 trabajadores la capacidad (unas 35 peticiones por segundo) queda por debajo de la llegada del pico (40) y la cola crece hasta el final de la ráfaga; con 5 o más el sistema se comporta como si no hubiera pico. Un escenario de calidad que diga «p95 de 2 s a 40 rps» detecta el umbral; «debe ser rápido» no.",
        note_kind="coral", foot=SINT)


def se301_serie() -> Fig:
    return line_chart(
        "Minutos de caída al mes de una cadena de componentes con 99,9 % cada uno (escala logarítmica)",
        "Líneas en escala logarítmica con los minutos de caída al mes según el número de componentes en serie: sin réplica sube de 43,2 con uno a 344,4 con ocho; con dos réplicas independientes la cuenta teórica es de 0,04 a 0,35 minutos; con 30 por ciento de causa común la simulación da 36,5 minutos con tres componentes y 65,3 con cinco, una mejora de 3,5 veces sobre no replicar, no de las mil de la cuenta independiente.",
        [("Sin réplica", [(1, 43.2), (3, 129.5), (5, 215.6), (8, 344.4)], "coral"),
         ("2 réplicas, caídas independientes", [(1, 0.04), (3, 0.13), (5, 0.22), (8, 0.35)], "teal"),
         ("2 réplicas, 30 % de causa común (simulado con 3 y 5)", [(3, 36.5), (5, 65.3)], "gold")],
        x_label="Componentes necesarios en serie", y_label="Minutos de caída al mes", log_y=True,
        x_ticks=[(1, "1"), (3, "3"), (5, "5"), (8, "8")], y_ticks=[0.01, 0.1, 1, 10, 100, 1000],
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
    return line_chart(
        "Dependencias reales no declaradas que aparecen según cuántas trazas se miran",
        "Línea con el número de dependencias no declaradas en la vista lógica que se ven al analizar trazas, en escala logarítmica de peticiones: una de tres con 100 peticiones, dos de tres con 1000, las tres con 5000 y con 100000; la dependencia declarada y nunca usada se ve desde la primera muestra.",
        [("No declaradas vistas (de 3)", [(100, 1, "1 de 3", "b"), (1000, 2, "2 de 3", "t"), (5000, 3, "3 de 3", "b"), (100000, 3, "3 de 3", "b")], "teal")],
        x_label="Peticiones analizadas", y_label="Dependencias no declaradas vistas", log_x=True,
        x_ticks=[(100, "100"), (1000, "1 000"), (5000, "5 000"), (100000, "100 000")], y_ticks=[0, 1, 2, 3],
        hlines=[(3, "las 3 existen")],
        annotations=[(100, 1, "La declarada y sin uso ya se ve con 100 peticiones", 95, 40)],
        note="Las tres dependencias tienen probabilidad 4 %, 0,5 % y 0,1 % por petición; la probabilidad de ver la última en n peticiones es 1 − (1 − p)ⁿ, 63 % con 1000 y 99 % con 5000. Que una traza no muestre una arista no prueba que no exista: solo acota con qué probabilidad la habríamos visto.",
        note_kind="gold", foot=SINT)


def se302_explosion() -> Fig:
    return grouped_bars(
        "Recorridos de usuario rotos por la caída del peor nodo (4 recorridos, 9 componentes)",
        "Barras horizontales con los recorridos de usuario que rompe la caída del peor nodo: un solo servidor rompe 4 de 4, separar aplicación y base sigue en 4, replicar solo la base sigue en 4 porque la web vive en un único nodo, y replicar también web e identidad baja el peor caso a 3 de 4.",
        ["Un solo servidor", "Aplicación y base de datos separadas", "3 nodos, solo la base replicada", "3 nodos, web, identidad y base replicadas"],
        [("Recorridos rotos por el peor nodo", [4, 4, 4, 3], "coral")],
        unit="Recorridos de usuario rotos (de 4)", horizontal=True, ticks=[0, 1, 2, 3, 4], label_w=250,
        note="Replicar la base de datos no protege si la puerta de entrada (la web) vive en un único nodo: los cuatro recorridos pasan por ella. La vista de despliegue se lee contra los recorridos, no componente por componente. Los recorridos y los nodos son del autor; no se simuló ninguna caída real.",
        note_kind="coral", foot=SINT)


def se302_cadena() -> Fig:
    return line_chart(
        "Latencia (ms) de una petición que atraviesa N servicios con mediana de 20 ms cada uno",
        "Líneas con la mediana y el percentil 99 de la latencia según el número de servicios llamados: en serie crecen de 20,0 y 80,6 milisegundos con un servicio a 186,3 y 321,1 con ocho, porque las latencias se suman; en paralelo solo llegan a 45,8 y 122,2, porque manda el más lento.",
        [("Serie, p99", [(1, 80.6, "80,6", "t"), (2, 122.9), (4, 193.7), (8, 321.1, "321,1", "t")], "coral"),
         ("Serie, p50", [(1, 20.0, "20,0", "t"), (2, 43.4), (4, 90.8), (8, 186.3, "186,3", "t")], "gold"),
         ("Paralelo, p99", [(1, 80.6), (2, 94.1), (4, 108.0), (8, 122.2, "122,2", "t")], "teal"),
         ("Paralelo, p50", [(1, 20.0), (2, 27.7), (4, 36.4), (8, 45.8, "45,8", "b")], "navy")],
        x_label="Servicios llamados (N)", y_label="Latencia de la petición (ms)", point_labels="none",
        x_ticks=[(1, "1"), (2, "2"), (4, "4"), (8, "8")], y_ticks=[0, 100, 200, 300, 400], log_x=True,
        note="En serie las latencias se suman y la cola se acumula; en paralelo manda el más lento. La probabilidad de tocar una llamada lenta crece como 1 − 0,99ᴺ. La vista de runtime muestra esas rutas; la lógica no. Latencias lognormales sintéticas (σ = 0,6) y llamadas independientes, un supuesto que la contención real rompe.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-303
def se303_llamada() -> Fig:
    return percentile_intervals(
        "Coste de una llamada: en proceso, serializada y por TCP en bucle local",
        "Intervalos en escala logarítmica con el rango medido entre ejecuciones: una llamada de función tarda de 0,22 a 0,84 microsegundos, serializar con JSON de 10,7 a 36,9, una ida y vuelta TCP en bucle local de 117 a 201 en la mediana y de 227 a 686 en el percentil 99; cada nivel de frontera queda a unas dos o tres décadas del anterior.",
        [("Llamada de función en el mismo proceso", [0.22, 0.84]), ("Serializar y deserializar JSON ida y vuelta", [10.7, 36.9]),
         ("TCP en bucle local, mediana", [117, 201]), ("TCP en bucle local, percentil 99", [227, 686])],
        unit="Tiempo por operación (µs), rango entre ejecuciones", marks=("mínimo", "máximo"), log=True,
        note="Medición real, sin red: el bucle local no tiene latencia de enlace, balanceador ni TLS, así que subestima el coste de cruzar una máquina. Las cifras cambian con la máquina; el orden de magnitud (dos o tres décimas de millar de veces) es lo que se repite. Una operación con 20 llamadas internas pasa de unos 7 µs a unos 2,3 ms si cada una cruza la red.",
        note_kind="gold", foot=REAL)


def se303_consistencia() -> Fig:
    return grouped_bars(
        "Operación que cruza tres servicios: estados inconsistentes con y sin compensación",
        "Barras agrupadas con el porcentaje de operaciones que quedan inconsistentes según la tasa de fallo por llamada: sin compensación 0,22, 1,98 y 9,27 por ciento con fallos de 0,1, 1 y 5 por ciento; con una compensación que falla el 5 por ciento de las veces quedan 0,02, 0,14 y 0,69 por ciento.",
        ["Fallo de 0,1 % por llamada", "Fallo de 1 % por llamada", "Fallo de 5 % por llamada"],
        [("Sin compensación", [0.22, 1.98, 9.27], "coral"), ("Con compensación (5 % de fallo)", [0.02, 0.14, 0.69], "teal")],
        unit="Operaciones inconsistentes (%)", ticks=[0, 2, 4, 6, 8, 10],
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
    return grouped_bars(
        "Módulos que dependen de la base de datos (40 módulos: 15 de dominio, 10 de aplicación, 8 web, 7 de infraestructura)",
        "Barras agrupadas con lo que arrastra un cambio de base de datos en tres estructuras: en las dos por capas dependen de ella 17 de 40 módulos, 3 de ellos de dominio, y hay 30 dependencias del dominio hacia la infraestructura; en la estructura hexagonal dependen 2 módulos, ninguno de dominio, y esas dependencias son 0.",
        ["Capas clásicas", "Capas con fugas", "Hexagonal"],
        [("Módulos dependientes de la BD", [17, 17, 2], "coral"), ("De ellos, de dominio", [3, 3, 0], "gold"), ("Dependencias dominio → infraestructura", [30, 30, 0], "navy")],
        unit="Módulos o dependencias (cantidad)", ticks=[0, 10, 20, 30],
        note="La dirección de la dependencia, no el número de capas, decide cuánto arrastra un cambio: invertirla en el borde (infraestructura → puerto del dominio) reduce los dependientes de 17 a 2. Los grafos son sintéticos con semilla fija y miden estructura, no esfuerzo. Aun así «hexagonal» no garantiza nada si los adaptadores filtran tipos de la base al dominio.",
        note_kind="teal", foot=SINT)


def se304_pruebas() -> Fig:
    return percentile_intervals(
        "Una prueba de la regla de promedio con tres implementaciones del repositorio (mediana de 60 ejecuciones)",
        "Intervalos en escala logarítmica con el rango entre ejecuciones de la mediana de una prueba: un doble en memoria tarda de 0,008 a 0,044 milisegundos, SQLite en memoria de 0,26 a 0,83 y SQLite en un archivo temporal de 102 a 133, miles de veces más que el doble.",
        [("Doble en memoria", [0.008, 0.044]), ("SQLite en memoria", [0.26, 0.83]), ("SQLite en archivo temporal", [102, 133])],
        unit="Mediana por prueba (ms), rango entre ejecuciones", marks=("mínimo", "máximo"), log=True,
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
    return stacked_bars(
        "Intercalaciones en las que se acepta más de un reenvío cuando el agregado admitía uno",
        "Barras horizontales apiladas al 100 por ciento con las intercalaciones que violan el invariante sin control de versión: 4 de 6 con dos comandos concurrentes, 72 de 90 con tres y 2160 de 2520 con cuatro, una proporción que crece con los comandos; con comprobación de versión del agregado ninguna lo viola.",
        ["2 comandos: 4 de 6 violan", "3 comandos: 72 de 90 violan", "4 comandos: 2 160 de 2 520 violan"],
        [("Aceptan más de un reenvío", [4, 72, 2160], "coral"), ("Respetan el invariante", [2, 18, 360], "teal")],
        unit="Intercalaciones", horizontal=True, percent=True, label_w=250,
        note="Leer, validar y escribir sin condición permite que dos comandos validen contra el mismo estado. Comparar la versión leída con la actual al escribir convierte la carrera en un rechazo reintentable. Se enumeraron todas las intercalaciones de pasos leer/escribir; no se usó una base de datos real, así que no se midió el coste de los reintentos.",
        note_kind="coral", foot=SINT)


def se305_notas() -> Fig:
    return grouped_bars(
        "Promedio de dos notas (1,0 a 7,0): empates exactos que se redondean distinto de la regla «medio hacia arriba»",
        "Barras horizontales con los pares de notas, de 1860 cuyo promedio cae justo en medio, que se redondean distinto de la regla medio hacia arriba: el float con round y el decimal con redondeo por defecto se apartan en 930, la mitad; el decimal con half-up declarado y los enteros en décimas, en ninguno.",
        ["Float con round()", "Decimal con redondeo por defecto (half-even)", "Decimal con half-up declarado", "Enteros en décimas con half-up"],
        [("Pares que difieren de half-up", [930, 930, 0, 0], "coral")],
        unit="Pares de notas (de 1 860 empates exactos)", horizontal=True, ticks=[0, 500, 1000, 1500, 2000],
        ref_lines=[(1860, "1 860 pares")], value_fmt=lambda v: "0" if v == 0 else "930 · 50 %", label_w=260,
        note="Ejemplo: 1,0 y 1,3 promedian 1,15; con float el resultado es 1,1 en lugar de 1,2. Un objeto de valor Nota que encapsula la representación y la regla de redondeo hace que la regla viva en un sitio y se pruebe contra todos los pares. Comprobado con Fraction como referencia exacta.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-306
def se306_consumo() -> Fig:
    return heatmap(
        "Entregas (de 2000) con estado erróneo según cómo procesa el consumidor",
        "Mapa de calor con las entregas erróneas de 2000 según el flujo de eventos y la estrategia del consumidor: los duplicados rompen solo al contador ingenuo, con 1824 entregas; el desorden rompe solo a quien se queda con la última llegada, con 6 y 2 entregas; el contador idempotente y la mayor secuencia dan 0 en todos los flujos.",
        ["Sin duplicados ni desorden", "5 % de duplicados", "Desorden de hasta 30 posiciones", "Duplicados y desorden"],
        ["Contador ingenuo", "Contador idempotente", "Última llegada gana", "Mayor secuencia gana"],
        [[0, 0, 0, 0], [1824, 0, 0, 0], [0, 0, 6, 0], [1824, 0, 2, 0]],
        unit="entregas erróneas de 2 000", row_title="Flujo de eventos", col_title="Estrategia del consumidor",
        scale="coral", vmin=0, vmax=2000, cell_fmt=lambda v: fmt_es(v, 0), highlight=[(1, 0), (2, 2), (3, 0), (3, 2)], cell_h=44, label_w=250,
        note="Los duplicados rompen lo que acumula; el desorden rompe lo que sobrescribe. Un identificador de evento y un número de secuencia por entidad son el contrato mínimo para que un consumidor sea correcto con entrega al-menos-una-vez. 100 000 eventos sintéticos sobre 2000 entregas, semilla fija.",
        note_kind="coral", foot=SINT)


def se306_reconstruccion() -> Fig:
    return line_chart(
        "Eventos que hay que aplicar para reconstruir un agregado de 10 000 eventos (5000 consultas)",
        "Líneas en escala logarítmica con los eventos aplicados al reconstruir según las instantáneas guardadas: sin instantáneas 5021 de media y 9893 en el percentil 99; con 10 instantáneas, una cada 1000 eventos, 507 y 991; con 50, 99 y 198; con 200, 24 y 49. Los eventos aplicados bajan casi en proporción inversa a las instantáneas guardadas.",
        [("Percentil 99", [(0, 9893, "9 893", "t"), (1, 991, "991", "t"), (2, 198, "198", "t"), (3, 49, "49", "t")], "coral"),
         ("Media", [(0, 5021, "5 021", "r"), (1, 507, "507", "b"), (2, 99, "99", "b"), (3, 24, "24", "b")], "teal")],
        x_label="Política de instantáneas (entre paréntesis, cuántas quedan guardadas)", y_label="Eventos aplicados al reconstruir", log_y=True,
        x_ticks=[(0, "Nunca (0)"), (1, "Cada 1 000 eventos (10)"), (2, "Cada 200 (50)"), (3, "Cada 50 (200)")], y_ticks=[10, 100, 1000, 10000],
        note="El coste de reconstruir es proporcional a la distancia hasta la última instantánea; el de guardarlas, a su número. El agregado «curso» recibe un evento por entrega (4 800 por periodo con 400 estudiantes y 12 tareas): agregados que crecen sin límite piden otro diseño del límite. Se contaron eventos aplicados, no segundos.",
        note_kind="gold", foot=SINT)


def se306_lectura() -> Fig:
    return percentile_intervals(
        "Retraso del modelo de lectura en un pico de 40 eventos por segundo (5 minutos)",
        "Intervalos en escala logarítmica con el retraso mediano y del percentil 99 según la capacidad del proyector: con 60 eventos por segundo el percentil 99 es 0,2 segundos; con 45, 0,8; con 41 sube a 3,3 y supera la recarga a 1 segundo; con 38, por debajo de la llegada, llega a 13,4 y supera también los 5 segundos.",
        [("Proyector de 60 por segundo", [0.02, 0.2]), ("Proyector de 45 por segundo", [0.04, 0.8]), ("Proyector de 41 por segundo", [0.06, 3.3]),
         ("Proyector de 38 por segundo", [0.09, 13.4])],
        unit="Retraso del modelo de lectura (s)", marks=("p50", "p99"), log=True, ref_lines=[(1, "recarga a 1 s"), (5, "a 5 s")],
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
