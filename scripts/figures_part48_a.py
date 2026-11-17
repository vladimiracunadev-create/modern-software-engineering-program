"""Figures for SE-577 to SE-582 (WebAssembly, eBPF, accelerators and isolation boundaries: real runs of wasmtime 50.0.1, of the Linux kernel verifier under WSL2 and of NumPy proxies; Windows 11, CPython 3.12.9; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, grouped_bars, heatmap, line_chart, scatter

from figures_part40_a import flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9; los recuentos se repiten y los tiempos varían de una ejecución y de un equipo a otro."
NUCLEO = "Programas cargados de verdad en el núcleo de Linux de WSL2 (6.18.58.1); los mensajes y los límites son los de esa versión."
PROXY = "Medida de CPU con NumPy como proxy: muestra la forma del efecto, no su magnitud en un acelerador. No se ejecutó ningún núcleo en una GPU."
MODELO = "Modelo con parámetros del autor y semilla fija 48; muestra un mecanismo, no mide un sistema real."


# ---------------------------------------------------------------- SE-577
def se577_velocidad_suma() -> Fig:
    return grouped_bars(
        "La misma suma de 5 000 000 de enteros en tres tecnologías: WebAssembly con combustible, Python puro y NumPy",
        "Barras horizontales en escala logarítmica con el tiempo en milisegundos de sumar los enteros de 0 a 4 999 999: WebAssembly con medición de combustible 9,98, Python puro 777,4 y NumPy 3,5 sobre un arreglo ya creado.",
        ["WebAssembly con combustible activado", "Python puro (bucle)", "NumPy (arreglo ya creado)"],
        [("Tiempo", [9.98, 777.4, 3.5], "teal")],
        unit="Milisegundos (escala logarítmica)", horizontal=True, log=True, decimals=1, label_w=270,
        note="Los tres resultados coinciden (12 499 997 500 000). Wasm es unas 78 veces más rápido que el bucle de Python y unas 3 veces más lento que NumPy en esta ejecución; entre ejecuciones Wasm tardó de unos 10 a unos 16 ms y Python de unos 780 a unos 930 ms. Un módulo escrito a mano de 236 bytes, con la medición de combustible activada, que tiene un costo.",
        note_kind="gold", foot=EJEC)


def se577_capacidades_wasi() -> Fig:
    return flow(
        "Qué cruza la frontera: de una operación del módulo al recurso, solo por una importación que el anfitrión definió",
        "Diagrama de cuatro cajas encadenadas: el módulo con sus importaciones declaradas, el anfitrión que decide qué función definir, la capacidad concedida como función o descriptor de directorio y el recurso real; una nota indica que la superficie del módulo es la lista de sus importaciones.",
        [[("Módulo\nImportaciones declaradas: una lista fija que se lee al enlazar", "teal"),
          ("Anfitrión\nDecide qué función definir y con qué validación de argumentos", "gold"),
          ("Capacidad concedida\nUna función o un descriptor de directorio, nunca una ruta global", "teal"),
          ("Recurso\nArchivo, reloj o salida: solo lo que se concedió", "coral")]],
        note="La superficie del módulo es la lista de sus importaciones. Con cero importaciones no puede observar ni modificar nada fuera de su memoria; con una función que ejecuta lo que el módulo le dice, el aislamiento se rompe en esa función.",
        note_kind="teal", box_h=118, foot=EJEC)


def se577_mecanismos() -> Fig:
    filas = ["Leer fuera de su memoria", "Bucle infinito", "Crecer la memoria sin tope", "Abrir una conexión de red", "Abrir un archivo ajeno"]
    cols = ["Memoria lineal", "Combustible", "Límite del anfitrión", "Importación no concedida", "Directorio concedido"]
    vals = [[1 if i == j else 0 for j in range(5)] for i in range(5)]
    return heatmap(
        "Cinco cosas que una regla ajena podría intentar y el mecanismo que contiene cada una",
        "Mapa de calor con cinco escenarios y cinco mecanismos: la lectura fuera de memoria la contiene la memoria lineal, el bucle infinito el combustible, el crecimiento de memoria el límite del anfitrión, la conexión de red la importación no concedida y el archivo ajeno el directorio concedido; cada escenario tiene un solo mecanismo marcado.",
        filas, cols, vals, unit="contiene", scale="teal", vmin=0, vmax=1, cell_fmt=lambda v: "contiene" if v else "—", cell_h=40, label_w=240,
        note="Cada escenario tiene un solo mecanismo marcado: si falta configurarlo, nadie más lo contiene. El combustible no limita la memoria ni el límite de memoria detiene un bucle; son mecanismos que se configuran y se prueban por separado. Resume lo que se ejercitó en el laboratorio, no una enumeración de ataques.",
        note_kind="gold", foot=EJEC)


# ---------------------------------------------------------------- SE-578
def se578_pasos_del_arranque() -> Fig:
    return grouped_bars(
        "Los pasos del arranque de un módulo de WebAssembly y, como referencia, el arranque de un proceso de Python",
        "Barras horizontales en escala logarítmica con el costo en milisegundos de cinco pasos: crear el motor 0,047, compilar el módulo 3,486, deserializar el módulo compilado 0,168, instanciar y llamar 0,468 y arrancar un intérprete de Python como proceso 158,7.",
        ["Crear el motor (una vez)", "Compilar el binario (una vez por versión)", "Deserializar el módulo compilado", "Instanciar y llamar (por petición)", "Proceso de Python (referencia)"],
        [("Mediana", [0.047, 3.486, 0.168, 0.468, 158.7], "navy")],
        unit="Milisegundos (escala logarítmica)", horizontal=True, log=True, decimals=3, label_w=300,
        note="Compilar es unas 7 veces más caro que instanciar y unas 20 veces más que deserializar; el módulo serializado (14 728 bytes) es unas 60 veces mayor que el binario (236 bytes). El proceso de Python tardó entre unos 100 y unos 160 ms en distintas ejecuciones: entre 210 y 340 veces el costo de instanciar. No son funciones equivalentes.",
        note_kind="teal", foot=EJEC)


def se578_estado_entre_peticiones() -> Fig:
    ks = [1, 2, 3, 4, 5]
    return line_chart(
        "Valor que devuelve el contador del módulo en cinco peticiones según la política de instancias",
        "Líneas con el valor del contador en cinco peticiones: con una instancia reutilizada sube de 1 a 5 y con una instancia nueva por petición vale siempre 1.",
        [("Instancia reutilizada", list(zip(ks, [1, 2, 3, 4, 5])), "coral"), ("Instancia nueva por petición", list(zip(ks, [1, 1, 1, 1, 1])), "teal")],
        x_label="Petición", y_label="Valor que devuelve el contador", x_ticks=[(k, str(k)) for k in ks], y_ticks=[0, 1, 2, 3, 4, 5], point_labels="all", decimals=0, plot_h=260,
        note="Con una instancia reutilizada, el estado de una petición se filtra a la siguiente: el resultado de un estudiante depende del anterior. La instancia por petición cuesta unos 0,5 ms y garantiza que cada una parte limpia. Si una importación guarda datos en el anfitrión, el estado se puede filtrar aunque la instancia sea nueva.",
        note_kind="coral", foot=EJEC)


def se578_componentes() -> Fig:
    return flow(
        "Del módulo al componente: cómo se componen módulos de lenguajes distintos con interfaces tipadas (no se ejecutó)",
        "Diagrama de cuatro cajas encadenadas: interfaces escritas en WIT, componentes compilados desde lenguajes distintos, composición que enlaza lo exportado con lo importado y un mundo final con las importaciones que el anfitrión debe conceder; una nota indica que esta parte no se ejecutó.",
        [[("Interfaz en WIT\nTipos ricos: cadenas, listas, registros, variantes", "teal"),
          ("Componentes\nCompilados desde lenguajes distintos contra esa interfaz", "gold"),
          ("Composición\nLo que uno exporta se enlaza con lo que otro importa", "teal"),
          ("Mundo final\nLas importaciones que el anfitrión debe conceder", "coral")]],
        note="Según la especificación, el modelo de componentes evita acordar a mano cómo se pasa una cadena entre módulos, pero no elimina el costo de convertir tipos ni los permisos: siguen siendo importaciones concedidas. El paquete de Python de wasmtime 50.0.1 no expone componentes y esta parte no se ejecutó.",
        note_kind="gold", box_h=118, foot="Diagrama conceptual basado en la documentación citada; no es una medición.")


# ---------------------------------------------------------------- SE-579
def se579_presupuesto_del_verificador() -> Fig:
    return grouped_bars(
        "Instrucciones que el verificador del núcleo procesó antes de decidir, en siete programas",
        "Barras horizontales en escala logarítmica con las instrucciones que el verificador procesó en siete programas: leer un registro sin inicializar 1, el programa trivial 2, desreferenciar sin comprobar nulo con clave variable 7, con clave constante 7, lectura fuera del valor del mapa 8, el contador con comprobación de nulo 10 y el bucle sin salida 1 000 001.",
        ["Leer un registro sin inicializar (rechazado)", "Programa trivial r0 = 42 (aceptado)", "Sin comprobar nulo, clave variable (rechazado)", "Sin comprobar nulo, clave constante (aceptado)", "Leer fuera del valor del mapa (rechazado)", "Contador con comprobación de nulo (aceptado)", "Bucle sin salida (rechazado)"],
        [("Instrucciones procesadas", [1, 2, 7, 7, 8, 10, 1000001], "navy")],
        unit="Instrucciones procesadas (escala logarítmica)", horizontal=True, log=True, decimals=0, label_w=330, ref_lines=[(1000000, "límite 1 000 000")],
        note="Los rechazos por reglas de seguridad ocurren en pocas instrucciones. El bucle sin salida no recibió un mensaje de bucle infinito: consumió todo el presupuesto (BPF program is too large. Processed 1000001 insn). Un caso que parece inseguro, desreferenciar sin comprobar nulo con una clave constante, fue aceptado porque el análisis sabe que la búsqueda no puede fallar.",
        note_kind="gold", foot=NUCLEO)


def se579_ciclo_de_carga() -> Fig:
    return flow(
        "El recorrido de un programa eBPF: del bytecode al contador leído desde el espacio de usuario",
        "Diagrama con tres filas de cajas: cargar con la llamada de sistema y recibir el registro del verificador; compilar y enganchar el programa aceptado; ejecutar en el núcleo y leer el mapa desde el espacio de usuario; una nota indica que el mapa es el único canal de datos.",
        [[("1. Cargar\nbpf(PROG_LOAD) con el tipo, las instrucciones y un búfer de registro", "teal"),
          ("2. Verificar\nTodos los caminos, registros, accesos y presupuesto de instrucciones", "gold"),
          ("3. Aceptar o rechazar\nRechazo con mensaje; aceptación con un descriptor", "coral")],
         [("4. Compilar\nCompilación a código nativo (JIT) y enganche a un punto", "teal"),
          ("5. Ejecutar\nEn el núcleo en cada evento; solo ayudantes conocidos", "gold"),
          ("6. Leer el mapa\nEl espacio de usuario consulta el contador con otra llamada", "teal")]],
        note="El mapa es el único canal de datos entre el núcleo y el espacio de usuario. Cada tipo de programa tiene sus propios puntos de enganche, ayudantes permitidos y reglas de retorno; el laboratorio ejercita uno solo (filtro de socket) con BPF_PROG_TEST_RUN.",
        note_kind="teal", box_h=108, foot=NUCLEO)


def se579_costo_por_evento() -> Fig:
    return grouped_bars(
        "Costo de contar un evento: un programa eBPF ejecutado cien mil veces y la misma cuenta como llamada a una función de Python",
        "Barras horizontales en escala logarítmica con el costo por evento en nanosegundos: el contador eBPF tardó unos 52 nanosegundos por ejecución y la misma cuenta como función de Python dentro del proceso unos 766.",
        ["Programa eBPF en el núcleo", "Función de Python en el proceso"],
        [("Nanosegundos por evento", [52, 766], "teal")],
        unit="Nanosegundos por evento (escala logarítmica)", horizontal=True, log=True, decimals=0, label_w=260,
        note="El tiempo del programa eBPF lo informa el núcleo sobre 100 000 ejecuciones de prueba (41, 52, 53 y 56 ns en cuatro ejecuciones). La función de Python mide una llamada y la actualización de un diccionario, no leer un evento: es una comparación de escala y no una medida de una carga real. El mapa leído al final valía 100 000.",
        note_kind="gold", foot=NUCLEO)


# ---------------------------------------------------------------- SE-580
def se580_patron_de_acceso() -> Fig:
    return grouped_bars(
        "Sumar 1 048 576 elementos de un arreglo de 64 MiB según cómo se leen: contiguos, con salto y en orden aleatorio",
        "Barras con el tiempo en milisegundos de sumar 1 048 576 elementos de un arreglo de 16 777 216 valores de 32 bits según el patrón de lectura: contiguos 4,67, con un salto de 16 posiciones 9,32 y en orden aleatorio 27,56.",
        ["Contiguos", "Con salto de 16 posiciones", "En orden aleatorio"],
        [("Tiempo", [4.67, 9.32, 27.56], "navy")],
        unit="Milisegundos", decimals=2, plot_h=250,
        note="El mismo trabajo cuesta casi 6 veces más en orden aleatorio que contiguo (27,56 frente a 4,67 ms). Cada línea de memoria que se trae se usa menos. En una GPU la magnitud es otra, pero el mecanismo es el mismo: los hilos de un grupo que leen posiciones vecinas se sirven con pocas transacciones.",
        note_kind="teal", foot=PROXY)


def se580_divergencia() -> Fig:
    return line_chart(
        "Costo medio de un grupo de 32 hilos según la probabilidad de que cada hilo tome el camino A de una rama",
        "Líneas con el costo medio relativo de un grupo de 32 hilos según la probabilidad de que cada hilo tome el camino A: 1,00 con probabilidad 0, 1,28 con 0,01, 1,80 con 0,05 y 2,00 con 0,5.",
        [("Costo relativo a un solo camino", [(0, 1.0), (0.01, 1.28), (0.05, 1.80), (0.5, 2.0)], "coral")],
        x_label="Probabilidad de que un hilo tome el camino A", y_label="Costo relativo del grupo", x_ticks=[(0, "0"), (0.01, "0,01"), (0.05, "0,05"), (0.5, "0,5")],
        y_ticks=[1.0, 1.25, 1.5, 1.75, 2.0], point_labels="all", decimals=2, plot_h=280, y_zero=False,
        note="Con una probabilidad de 0,01 por hilo, el grupo ejecuta ambos caminos en el 27,8 % de los casos; con 0,05, en el 80,4 %. Basta un hilo discrepante de 32 para pagar los dos caminos. El modelo supone hilos independientes y dos caminos del mismo costo; con datos correlacionados el resultado cambia.",
        note_kind="coral", foot=MODELO)


def se580_intensidad_aritmetica() -> Fig:
    return scatter(
        "Rendimiento medido frente a operaciones por byte movido en tres operaciones de CPU",
        "Dispersión en escala logarítmica con el rendimiento en GFLOP/s frente a las operaciones por byte movido: la suma vectorial con unas 0,17 operaciones por byte rinde 0,38, el producto de matrices de 256 con 43 rinde 16,5 y el de 1024 con 171 rinde 86,8.",
        [("Suma vectorial", [(0.17, 0.38)], "coral"), ("Producto de matrices 256 × 256", [(43, 16.5)], "gold"), ("Producto de matrices 1024 × 1024", [(171, 86.8)], "teal")],
        x_label="Operaciones por byte movido (escala logarítmica)", y_label="GFLOP/s medidos (escala logarítmica)", log_x=True, log_y=True,
        x_ticks=[(0.1, "0,1"), (1, "1"), (10, "10"), (100, "100"), (1000, "1000")], y_ticks=[0.1, 1, 10, 100], point_labels="all", decimals=2, plot_h=300,
        note="El rendimiento sube con la intensidad aritmética: la suma vectorial, limitada por memoria, rinde 0,38 GFLOP/s y el producto de 1024 × 1024, 86,8 (más de 200 veces). En otras ejecuciones del producto de 1024 se midieron 105 a 112 GFLOP/s. No se dibujaron los techos de la máquina porque no se midieron sus picos de cómputo ni de ancho de banda.",
        note_kind="gold", foot=PROXY)


# ---------------------------------------------------------------- SE-581
def se581_lote_y_rendimiento() -> Fig:
    ks = [1, 4, 16, 64, 256]
    return line_chart(
        "Peticiones por segundo de una capa densa de 1024 × 1024 en CPU según el tamaño del lote",
        "Líneas con el rendimiento en peticiones por segundo según el tamaño del lote: 3693 con lote 1, 170 con lote 4, 3317 con lote 16, 8140 con lote 64 y 17863 con lote 256.",
        [("Peticiones por segundo", list(zip(ks, [3693, 170, 3317, 8140, 17863])), "teal")],
        x_label="Tamaño del lote (escala logarítmica)", y_label="Peticiones por segundo", log_x=True, x_ticks=[(k, str(k)) for k in ks],
        y_ticks=[0, 5000, 10000, 15000, 20000], point_labels="all", decimals=0, plot_h=280,
        note="El rendimiento sube de unas 3 700 a unas 17 900 peticiones por segundo con lotes de 1 a 256, pero no de forma monótona: con lote 4 cayó a 170 (de 170 a 363 en tres ejecuciones), una ruta lenta de la biblioteca para esa forma que no se investigó. La latencia por lote sube de 0,27 a 14,3 ms: cada petición espera a que el lote se llene y termine.",
        note_kind="gold", foot="Mediciones de CPU con NumPy 2.5.5; no se ejecutó nada en un acelerador. El valor del lote 4 es una anomalía real de esa máquina.")


def se581_amdahl_con_transferencia() -> Fig:
    return heatmap(
        "Aceleración total con una mejora de 50 veces en la parte acelerable, según la parte serie y la transferencia",
        "Mapa de calor con la aceleración total para una mejora de 50 veces en la parte acelerable: con parte serie de 0,05 es 14,5 sin transferencia, 8,4 con transferencia de 0,05 y 3,7 con 0,20; con parte serie de 0,20 es 4,6, 3,8 y 2,4.",
        ["Parte serie 5 %", "Parte serie 20 %"], ["Sin transferencia", "Transferencia 5 %", "Transferencia 20 %"],
        [[14.5, 8.4, 3.7], [4.6, 3.8, 2.4]], unit="veces", scale="teal", vmin=0, vmax=15, decimals=1, suffix=" ×", cell_h=70, label_w=190,
        note="Una mejora de 50 veces en el núcleo de cálculo termina entre 2,4 y 14,5 veces en el sistema. La fórmula es 1 / (s + t + (1 − s)/k) con k = 50. Es aritmética, no una medición: la transferencia real depende del bus y de si los datos pueden quedarse en el acelerador, y la parte serie de lo que se acelera de verdad.",
        note_kind="gold", foot=MODELO)


def se581_costo_por_demanda() -> Fig:
    d = [20, 100, 400, 1000, 2000, 6000]
    return line_chart(
        "Costo por millón de peticiones según la demanda sostenida: un acelerador y una CPU con precios supuestos",
        "Líneas en escala logarítmica con el costo en dólares por millón de peticiones según la demanda: el acelerador pasa de 41,67 con 20 peticiones por segundo a 0,42 con 2000 y la CPU de 5,56 a 0,78; el acelerador es más caro hasta 1000 y más barato desde 2000.",
        [("Acelerador (3,00 USD/h, 2000 peticiones/s por unidad)", list(zip(d, [41.67, 8.33, 2.08, 0.83, 0.42, 0.42])), "coral"),
         ("CPU (0,40 USD/h, 150 peticiones/s por unidad)", list(zip(d, [5.56, 1.11, 0.83, 0.78, 0.78, 0.74])), "teal")],
        x_label="Demanda en peticiones por segundo (escala logarítmica)", y_label="USD por millón de peticiones (escala logarítmica)", log_x=True, log_y=True,
        x_ticks=[(k, str(k)) for k in d], y_ticks=[0.1, 1, 10, 100], point_labels="none", decimals=2, plot_h=300,
        note="Se compran unidades enteras: con poca demanda el acelerador paga una unidad casi ociosa (41,67 USD por millón a 20 peticiones por segundo) y gana la CPU; a partir de unas 2 000 peticiones por segundo gana el acelerador (0,42 frente a 0,78). Los precios y las capacidades son supuestos del autor, no tarifas ni mediciones: con otros valores el cruce se desplaza o no existe.",
        note_kind="coral", foot=MODELO)


# ---------------------------------------------------------------- SE-582
def se582_costo_de_frontera() -> Fig:
    return grouped_bars(
        "Costo de crear y destruir una frontera de aislamiento: instancia de WebAssembly, hilo y proceso de Python",
        "Barras horizontales en escala logarítmica con el costo en milisegundos de crear y destruir cada frontera: una instancia de WebAssembly 0,092, un hilo 0,38 y un proceso nuevo de Python 99,4.",
        ["Instancia de WebAssembly (módulo compilado)", "Hilo del mismo proceso", "Proceso nuevo de Python"],
        [("Mediana", [0.092, 0.38, 99.4], "navy")],
        unit="Milisegundos (escala logarítmica)", horizontal=True, log=True, decimals=3, label_w=290,
        note="La instancia es unas mil veces más barata que el proceso. Que el hilo cueste más que la instancia no se investigó. El proceso tardó entre unos 100 y unos 160 ms en distintas ejecuciones. No se midieron contenedores ni microVM: en esta máquina Docker corre sobre WSL2 y su arranque mediría esa capa y no la frontera.",
        note_kind="teal", foot=EJEC)


def se582_capas_y_causas_comunes() -> Fig:
    ks = [1, 2, 3]
    return line_chart(
        "Probabilidad de cruzar todas las capas de aislamiento según su número, con capas independientes y con un fallo común",
        "Líneas en escala logarítmica con la probabilidad de cruzar todas las capas según su número: con p igual a 0,10 baja de 0,1 a 0,001 con tres capas independientes, con p igual a 0,02 baja de 0,02 a 0,000008 y con p igual a 0,02 y un fallo común entre pares de capas baja de 0,02 a 0,0004.",
        [("p = 0,10, capas independientes", list(zip(ks, [0.1, 0.01, 0.001])), "coral"),
         ("p = 0,02, capas independientes", list(zip(ks, [0.02, 0.0004, 0.000008])), "teal"),
         ("p = 0,02, con un fallo común entre pares", list(zip(ks, [0.02, 0.02, 0.0004])), "gold")],
        x_label="Número de capas", y_label="Probabilidad de cruzarlas todas (escala logarítmica)", log_y=True, x_ticks=[(k, str(k)) for k in ks],
        y_ticks=[0.00001, 0.0001, 0.001, 0.01, 0.1], point_labels="none", decimals=6, plot_h=290,
        note="Con dos capas que comparten una causa de fallo la probabilidad sigue en 0,02, como si no hubiera segunda capa. Antes de apilar una capa hay que preguntar qué no comparte con las anteriores. Las probabilidades por capa son supuestos del autor, no medidas; la realidad está entre la independencia total y la correlación total.",
        note_kind="coral", foot=MODELO)


def se582_escala_de_fronteras() -> Fig:
    return flow(
        "La escala de fronteras de aislamiento según lo que comparten con el anfitrión",
        "Diagrama de cuatro cajas encadenadas: un hilo que comparte todo el proceso, un proceso o contenedor que comparten el núcleo, un núcleo de aplicación o un módulo de WebAssembly que reducen la superficie compartida y una microVM que comparte solo el hipervisor; una nota indica que la fuerza depende de qué se comparte y no del nombre.",
        [[("Hilo\nComparte todo el proceso y no se puede cortar desde fuera", "coral"),
          ("Proceso o contenedor\nComparten el núcleo del anfitrión", "gold"),
          ("Núcleo de aplicación o Wasm\nReducen la superficie compartida con el anfitrión", "teal"),
          ("microVM\nNúcleo propio; se comparte el hipervisor y sus dispositivos", "teal")]],
        note="No es un orden total de seguridad: la fuerza depende de qué superficie queda compartida y de cuánto código la implementa, no del nombre. Cada frontera tiene configuraciones que la acercan o la alejan de su caja. Resumen conceptual de la documentación citada; solo se midieron hilo, instancia de Wasm y proceso.",
        note_kind="gold", box_h=118, foot="Diagrama conceptual basado en NIST SP 800-190 y en la documentación de gVisor, Firecracker y Kata; no es una medición.")


FIGURES = {
    "se-577-velocidad-suma.svg": se577_velocidad_suma,
    "se-577-capacidades-wasi.svg": se577_capacidades_wasi,
    "se-577-mecanismos.svg": se577_mecanismos,
    "se-578-pasos-del-arranque.svg": se578_pasos_del_arranque,
    "se-578-estado-entre-peticiones.svg": se578_estado_entre_peticiones,
    "se-578-componentes.svg": se578_componentes,
    "se-579-presupuesto-del-verificador.svg": se579_presupuesto_del_verificador,
    "se-579-ciclo-de-carga.svg": se579_ciclo_de_carga,
    "se-579-costo-por-evento.svg": se579_costo_por_evento,
    "se-580-patron-de-acceso.svg": se580_patron_de_acceso,
    "se-580-divergencia.svg": se580_divergencia,
    "se-580-intensidad-aritmetica.svg": se580_intensidad_aritmetica,
    "se-581-lote-y-rendimiento.svg": se581_lote_y_rendimiento,
    "se-581-amdahl-con-transferencia.svg": se581_amdahl_con_transferencia,
    "se-581-costo-por-demanda.svg": se581_costo_por_demanda,
    "se-582-costo-de-frontera.svg": se582_costo_de_frontera,
    "se-582-capas-y-causas-comunes.svg": se582_capas_y_causas_comunes,
    "se-582-escala-de-fronteras.svg": se582_escala_de_fronteras,
}
