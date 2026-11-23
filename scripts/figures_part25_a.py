"""Figures for SE-301 to SE-306 (code analysis and synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, heatmap, line_chart, percentile_intervals, scatter, stacked_bars
from figures_part07_a import bars

SINT = "Medición sobre código de ejemplo y simulación con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-301
def se289_lcom() -> Fig:
    return grouped_bars(
        "Métodos y grupos desconectados (LCOM4) de una clase de envíos y de su separación",
        "Barras agrupadas con el número de métodos y el LCOM4 de cuatro clases: la clase mezclada de envíos tiene 7 métodos y LCOM4 igual a 3; al separarla, precio tiene 3 métodos, aviso 2 y bitácora 2, y cada una tiene LCOM4 igual a 1.",
        ["Envío (clase mezclada)", "Precio", "Aviso", "Bitácora"],
        [("Métodos", [7, 3, 2, 2], "grey"), ("LCOM4 (grupos de métodos que no se tocan)", [3, 1, 1, 1], "coral")],
        unit="Cantidad", decimals=0, plot_h=260,
        note="LCOM4 cuenta los grupos de métodos conectados por atributos compartidos o llamadas entre sí; 3 significa tres clases en una. Con clases aleatorias de seis métodos, si cada uno usa un solo atributo de seis, ninguna clase queda en 1; con dos atributos por método, el 88,7 %; con tres, el 100 %: la métrica mide densidad de uso, no calidad del diseño.",
        note_kind="gold", foot=SINT)


def se289_sitios() -> Fig:
    return grouped_bars(
        "Sitios que hay que editar en 30 clientes al cambiar la representación del peso",
        "Barras agrupadas con los sitios que hay que editar en treinta clientes: renombrar el campo obliga a editar 30 sitios si los clientes leen peso_kg y ninguno con getter o comportamiento; cambiar kilos a gramos obliga a editar 51 sitios con campo o getter y ninguno si los clientes piden comportamiento.",
        ["Los clientes leen el campo peso_kg", "Los clientes llaman a un getter peso()", "Los clientes piden comportamiento"],
        [("Renombrar el campo", [30, 0, 0], "gold"), ("Cambiar kg a g", [51, 51, 0], "coral")],
        unit="Sitios que editar", horizontal=True, decimals=0, label_w=260,
        note="Un getter oculta el nombre pero no el significado: los clientes siguen multiplicando kilos. Solo encapsular la decisión (qué es el peso y cuánto cuesta) deja la unidad dentro. Los 30 clientes salen de cuatro plantillas elegidas con semilla fija; es una construcción del autor, no un proyecto real.",
        note_kind="teal", foot=SINT)


def se289_ciclos() -> Fig:
    return line_chart(
        "Probabilidad de ciclos entre 20 módulos cuando las dependencias se añaden sin regla",
        "Líneas con el porcentaje de grafos con ciclo según las aristas añadidas entre veinte módulos: al azar sube de 65 por ciento con 20 aristas a 100 con 40 y con 60; con un orden de capas se queda en 0; el primer ciclo aparece con una mediana de 18 aristas.",
        [("Aristas al azar", [(20, 65.0), (40, 100.0), (60, 100.0)], "coral"),
         ("Con orden de capas (solo hacia abajo)", [(20, 0.0), (40, 0.0), (60, 0.0)], "teal")],
        x_label="Aristas añadidas entre 20 módulos", y_label="Grafos con al menos un ciclo (%)",
        x_ticks=[(10, "10"), (20, "20"), (30, "30"), (40, "40"), (50, "50"), (60, "60")], y_ticks=[0, 20, 40, 60, 80, 100],
        vlines=[(18, "mediana del primer ciclo: 18")], decimals=1, plot_h=280,
        note="Los ciclos no son un accidente raro: aparecen pronto cuando nadie decide el sentido de las dependencias. El primer ciclo llega con una mediana de 18 aristas (p10 a p90: 9 a 27; mínimo 2, máximo 47). Un orden de capas permite 190 de las 380 aristas posibles y elimina los ciclos por construcción. Grafos sintéticos de 2000 repeticiones; un grafo real no es aleatorio.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-302
def se290_reglas() -> Fig:
    return line_chart(
        "Complejidad de la función de descuento al añadir reglas: cadena if/elif frente a registro",
        "Líneas con la complejidad ciclomática según la regla de descuento añadida: en la cadena if elif sube de 3 con la segunda regla a 6 con la quinta porque cada regla modifica la función; en el registro de reglas se queda en 2 y ninguna función existente se modifica.",
        [("Cadena if/elif (modifica la función, +2 líneas)", [(2, 3), (3, 4), (4, 5), (5, 6)], "coral"),
         ("Registro de reglas (no modifica, +4 líneas)", [(2, 2), (3, 2), (4, 2), (5, 2)], "teal")],
        x_label="Regla de descuento añadida", y_label="Complejidad de la función de descuento",
        x_ticks=[(2, "2.ª"), (3, "3.ª"), (4, "4.ª"), (5, "5.ª")], y_ticks=[0, 2, 4, 6, 8], decimals=0, plot_h=260,
        note="Abierto/cerrado se ve como funciones existentes que no cambian: en la cadena, cada regla nueva reabre la función que todas las pruebas atraviesan; en el registro, no. El registro escribe más líneas por regla (cuatro frente a dos). Cuesta además dos decisiones nuevas: el orden y cómo se combinan reglas simultáneas (aquí, el máximo).",
        note_kind="teal", foot=SINT)


def se290_liskov() -> Fig:
    return grouped_bars(
        "Subclases que rompen el contrato de Tarifa: tres ejemplos frente a 2000 entradas al azar",
        "Barras horizontales con el porcentaje de violaciones que detecta cada método en cinco subclases de una tarifa: tres ejemplos de camino feliz no detectan ninguna; 2000 entradas al azar detectan el 61,8 por ciento de la que rechaza pesos altos, el 19,1 de la que lanza una excepción nueva, el 0,9 de la no monótona y solo el 0,1 de la que falla en un rincón estrecho.",
        ["Compatible", "Rechaza pesos mayores de 20", "Lanza KeyError en la zona 5", "Pesos desde 30 con 20 % de descuento", "Pierde monotonía si peso > 45 y zona 1"],
        [("3 ejemplos de camino feliz", [0, 0, 0, 0, 0], "gold"), ("2000 entradas al azar", [0, 61.8, 19.1, 0.9, 0.1], "teal")],
        unit="Entradas en que se detecta la violación (%)", horizontal=True, decimals=1, label_w=290, width=980,
        note="Probar con la superclase en la mano es la prueba de sustitución: todas las subclases deben pasar el mismo conjunto de comprobaciones. Una violación que ocurre en el 0,1 % del dominio se escapa incluso a 2000 entradas: el azar no sustituye a razonar sobre las condiciones del contrato. El contrato es del autor.",
        note_kind="coral", foot=SINT)


def se290_interfaces() -> Fig:
    return dumbbell(
        "Interfaces anchas y estructura innecesaria: qué baja y qué sube al segregar y abstraer",
        "Gráfico de mancuernas en escala logarítmica: segregar la interfaz baja los clientes que revisan un cambio de 8 a 5 y los métodos de un doble de prueba de 12 a 7,5; abstraer la misma regla de redondeo y tope sube los nodos del árbol sintáctico de 17 a 126 y las líneas de 2 a 17.",
        [("Clientes que revisan un cambio (de 8)", 8, 5), ("Métodos de un doble de prueba", 12, 7.5),
         ("Nodos del árbol sintáctico de la misma regla", 17, 126), ("Líneas de la misma regla", 2, 17)],
        unit="Cantidad", names=("Interfaz ancha / función simple", "Roles / estrategias y fábrica"), log=True,
        delta=lambda a, b: "×" + f"{b / a:.1f}".replace(".", ","), lower_is_better=True, label_w=300, width=980,
        note="Segregar interfaces reduce la dependencia nominal, no la real: de ocho clientes solo 1,75 usan de verdad el método que cambia, y aun con roles cinco revisan el cambio. Y la abstracción tiene precio de lectura: 7 veces más nodos para la misma regla. Sin un segundo uso, esa estructura no compra nada. Ocho clientes sintéticos con semilla fija.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-303
def se291_base() -> Fig:
    return grouped_bars(
        "Contador de elementos agregados: lotes con cuenta errónea según el diseño y la base",
        "Barras agrupadas con los lotes mal contados de mil: el contador por herencia cuenta mal los 1000 lotes cuando la base implementa agregar todos llamando a agregar y ninguno cuando usa extend; el contador por composición y delegación cuenta bien los mil lotes con ambas bases.",
        ["Herencia", "Composición y delegación"],
        [("Base V1 (agregar_todos llama a agregar)", [1000, 0], "coral"), ("Base V2 (agregar_todos usa extend)", [0, 0], "teal")],
        unit="Lotes con cuenta errónea (de 1000)", decimals=0, plot_h=240,
        note="La subclase funcionaba o fallaba según un detalle interno de la base que ni la interfaz ni la documentación prometían: eso es la clase base frágil. La composición solo depende de lo que la base promete. La prueba que pasó con V2 no vio que V1 existía. Lotes de 1 a 6 elementos con semilla fija.",
        note_kind="coral", foot=SINT)


def se291_decoradores() -> Fig:
    return line_chart(
        "Opciones de envío combinables: subclases, decoradores y órdenes posibles",
        "Líneas en escala logarítmica según el número de opciones combinables: las subclases por combinación crecen de 15 con 4 opciones a 1023 con 10, los decoradores solo de 4 a 10, y los órdenes en que se pueden aplicar los decoradores crecen de 24 a 3 628 800.",
        [("Subclases por combinación", [(4, 15, "15", "r"), (6, 63), (8, 255), (10, 1023)], "coral"),
         ("Decoradores", [(4, 4, "4", "b"), (6, 6), (8, 8), (10, 10)], "teal"),
         ("Órdenes posibles de los decoradores", [(4, 24), (6, 720), (8, 40320), (10, 3628800)], "gold")],
        x_label="Opciones combinables", y_label="Cantidad", log_y=True,
        x_ticks=[(4, "4"), (6, "6"), (8, "8"), (10, "10")], y_ticks=[1, 10, 100, 1000, 10000, 100000, 1000000, 10000000],
        decimals=0, plot_h=300,
        note="Con cuatro opciones, base 50, frágil +4, seguro ×1,02, urgente ×1,30 y refrigerado +6, los 24 órdenes dan 14 totales entre 76,30 y 79,56: la composición cambia el crecimiento (lineal en vez de exponencial) pero el orden pasa a ser parte del diseño y debe fijarse o probarse.",
        note_kind="gold", foot=SINT)


def se291_mro() -> Fig:
    items = [
        ("Jerarquías que no se pueden crear (MRO)", 65.2, "coral", "65,2 %"),
        ("Jerarquías que se crean", 34.8, "teal", "34,8 %"),
        ("De las que heredan el mismo método de 2 o más bases: el elegido cambia al invertir las bases", 91.6, "gold", "91,6 % (175 de 191)"),
    ]
    return bars("3000 jerarquías aleatorias de 8 clases con hasta 3 bases cada una",
                "Barras: de tres mil jerarquías aleatorias de ocho clases con hasta tres bases, el 65,2 por ciento no se puede crear por un orden de resolución de métodos inconsistente; del resto, en el 91,6 por ciento de los casos con un método heredado de dos o más bases, invertir el orden de las bases cambia el método que se ejecuta.",
                items, 5, "Python rechaza con TypeError los órdenes de bases imposibles y resuelve el resto por un orden lineal definido por el orden en que se escriben las bases. Escribir class C(A, B) o class C(B, A) cambia el programa. Jerarquías sintéticas sin semántica: miden la mecánica, no cuán común es en proyectos reales.",
                label_w=470, width=1010, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-304
def se292_singleton() -> Fig:
    items = [
        ("Singleton sin reinicio", 99.8, "coral", "99,8 % de los órdenes fallan"),
        ("Singleton con reinicio por prueba", 0.0, "teal", "0 %"),
        ("Configuración inyectada", 0.0, "teal", "0 %"),
    ]
    return bars("Órdenes aleatorios de 12 pruebas con al menos un fallo (5000 órdenes)",
                "Barras: de cinco mil órdenes aleatorios de doce pruebas, ocho que leen el valor por defecto y cuatro que lo cambian, el 99,8 por ciento tiene algún fallo si la configuración es un singleton sin reinicio, y ninguno si se reinicia en cada prueba o si la configuración se inyecta.",
                items, 3.4, "Con lectoras primero hay 0 fallos y con escritoras primero 8: la suite pasa o falla según el orden. El reinicio por prueba arregla el síntoma pero exige que cada prueba conozca el singleton; la inyección quita la causa. Pruebas de ejemplo de una sola clase de configuración.",
                label_w=330, width=1000, note_kind="gold", foot=SINT)


def se292_observadores() -> Fig:
    return percentile_intervals(
        "Notificaciones perdidas por observador de 1000 eventos (5 observadores que fallan el 2 % de las veces)",
        "Intervalos con las notificaciones perdidas por observador, de 1000: con un bucle simple el mejor observador pierde 20, la media es 59,2 y el peor pierde 101 porque una excepción corta el reparto (4704 de 5000 entregas); con cada observador aislado pierden 15, 21,2 y 32 (4894 de 5000).",
        [("Bucle simple (la excepción sube y corta el reparto)", [20, 59.2, 101]),
         ("Cada observador aislado con try/except", [15, 21.2, 32])],
        unit="Notificaciones perdidas por observador (de 1000)", marks=("mejor observador", "media", "peor observador"), decimals=1,
        label_w=330, width=980,
        note="Las pérdidas son 1000 menos las entregas por observador (899 a 980 con el bucle simple, 968 a 985 aislado). El primero en la lista casi nunca pierde nada y el último pierde más: el orden de suscripción se vuelve una prioridad implícita. Aislar a los observadores baja las pérdidas pero oculta los fallos si nadie cuenta las excepciones (101 frente a 106). Dar de baja un observador durante el reparto sin copiar la lista salta a b; con copia se visita a, b, c, d. Falla cada observador con probabilidad 0,02, un supuesto.",
        note_kind="gold", foot=SINT)


def se292_estructura() -> Fig:
    nombres = ["Adaptador", "Proxy", "Decorador", "Estrategia", "Estado"]
    return heatmap(
        "Similitud de la estructura sintáctica entre implementaciones de cinco patrones",
        "Mapa de calor con la similitud coseno entre los tipos de nodo del árbol sintáctico de cinco patrones: todos los pares están entre 0,926 y 0,992, proxy con decorador es el par más distinto, 0,926, y estrategia con estado el más parecido, 0,992; el código casi no distingue un patrón de otro.",
        nombres, nombres,
        [[1.000, 0.940, 0.987, 0.985, 0.988],
         [0.940, 1.000, 0.926, 0.937, 0.945],
         [0.987, 0.926, 1.000, 0.988, 0.980],
         [0.985, 0.937, 0.988, 1.000, 0.992],
         [0.988, 0.945, 0.980, 0.992, 1.000]],
        unit="similitud coseno (escala desde 0,90)", scale="navy", vmin=0.90, vmax=1.0, decimals=3,
        highlight=[(1, 2), (2, 1), (3, 4), (4, 3)], cell_h=46,
        note="Las cinco clases guardan un colaborador y le delegan: lo que cambia es la intención (traducir, controlar el acceso, añadir, intercambiar un algoritmo, cambiar de comportamiento con el estado). El patrón no se reconoce por la forma sino por el motivo del cambio. Cinco clases escritas por el autor.",
        note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-305
def se293_impureza() -> Fig:
    return grouped_bars(
        "Impurezas detectadas, de 8, según el nivel de la prueba",
        "Barras con las impurezas que detecta cada nivel de prueba sobre ocho funciones impuras: un ejemplo no detecta ninguna, repetir la llamada y comprobar la entrada y la salida detecta cuatro, y perturbar además el estado global detecta siete; ninguna de las cuatro funciones puras dio falsa alarma.",
        ["Un ejemplo", "Repetir y comprobar", "Y perturbar lo global"],
        [("Impurezas detectadas", [0, 4, 7], "teal")],
        unit="Impurezas detectadas (de 8)", decimals=0, ref_lines=[(8, "8 funciones impuras")], ticks=[0, 2, 4, 6, 8], plot_h=260, width=900,
        note="Una función con un solo ejemplo correcto no demuestra pureza. La que devuelve una referencia a su estado interno pasa los tres niveles: se descubre solo cuando alguien muta el valor devuelto. Las que no se ven sin perturbar lo global son la lectura de configuración, la del reloj y la escritura de un total global. Doce funciones escritas por el autor, cuatro puras sin falsas alarmas; el detector es una construcción simple.",
        note_kind="gold", foot=SINT)


def se293_cola() -> Fig:
    return percentile_intervals(
        "Latencia de una cola entre un productor y un consumidor (20 000 eventos, capacidad 20)",
        "Intervalos en escala logarítmica con la latencia media y el percentil 99 de seis configuraciones de una cola: con llegadas de 100 por segundo y servicio de 80, la cola sin límite llega a 24 713,8 milisegundos de media y 49 544,7 de p99; con capacidad 20 las tres políticas mantienen la media entre 167 y 221 milisegundos.",
        [("Estable 70/s → 80/s, sin límite", [99.2, 422.4]), ("Estable 70/s → 80/s, bloquea al productor", [81.7, 308.7]),
         ("Saturada 100/s → 80/s, sin límite", [24713.8, 49544.7]), ("Saturada, bloquea al productor", [220.7, 386.1]),
         ("Saturada, descarta lo nuevo", [212.8, 376.2]), ("Saturada, descarta lo viejo", [167.4, 271.1])],
        unit="Latencia (ms)", marks=("media", "p99"), log=True, decimals=1, label_w=330, width=1000,
        note="La cola sin límite no pierde nada (cola máxima de 3992 elementos) y deja todo inservible: en la saturación nadie recibe una respuesta a tiempo. Un límite obliga a decidir quién paga: el productor espera unos 50 s, se pierden 3991 eventos nuevos o se pierden 3922 viejos. Llegadas y servicios exponenciales con semilla fija; los tiempos son del modelo, no de una máquina.",
        note_kind="coral", foot=SINT)


def se293_hilos() -> Fig:
    return stacked_bars(
        "Intercalaciones de dos hilos sobre un dato compartido que dan el resultado esperado",
        "Barras apiladas al 100 por ciento con las intercalaciones que dan el resultado esperado: sin protección solo 6 de 70 dan 4 en el contador y 2 de 6 dan un solo cupo vendido; con una operación atómica todas las intercalaciones dan el resultado esperado.",
        ["Contador de 2 incrementos por hilo, sin protección (70)", "Contador, operación atómica (6)", "Último cupo, sin protección (6)", "Último cupo, operación atómica (2)"],
        [("Resultado esperado", [6, 6, 2, 2], "teal"), ("Resultado erróneo", [64, 0, 4, 0], "coral")],
        unit="Intercalaciones", horizontal=True, percent=True, decimals=0, label_w=330, width=1000,
        note="Solo 6 de 70 intercalaciones salen bien, y una prueba corrida mil veces puede no ver nunca las malas: depende del planificador. En el contador los errores son 3 (32 intercalaciones) o 2 (32); en el cupo, 4 de 6 lo venden dos veces. Enumerar, o diseñar para que un solo hilo sea dueño del dato, convierte la sospecha en conteo. Modelo de pasos atómicos, sin hilos reales.",
        note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-306
def se294_umbrales() -> Fig:
    return grouped_bars(
        "Funciones señaladas por cada regla de olores sobre 65 funciones del propio repositorio (commit 4dafaa63)",
        "Barras horizontales con las funciones señaladas por cada regla entre 65: largo mayor de 25 líneas, 5; más de 5 parámetros, 7; anidamiento mayor de 3, 1; complejidad ciclomática mayor de 10, 3; por alguna regla, 12; si el largo de datos no cuenta, 11 porque sale una plantilla de 217 líneas con 83 por ciento de datos.",
        ["Largo mayor de 25 líneas", "Más de 5 parámetros", "Anidamiento mayor de 3", "Complejidad ciclomática mayor de 10",
         "Señaladas por alguna regla", "Si el largo de datos no cuenta"],
        [("Funciones señaladas (de 65)", [5, 7, 1, 3, 12, 11], "gold")],
        unit="Funciones señaladas", horizontal=True, decimals=0, label_w=300, width=960,
        note="Las tres funciones de mayor complejidad (el convertidor con 39, la página con 14 y el diagrama con 12) merecen leerse: tienen lógica. La de 217 líneas es mayoritariamente texto de una plantilla: señalarla por largo es una falsa alarma que enseña a ignorar la herramienta. Los umbrales son convenciones del autor y se midió en el estado del repositorio de ese commit.",
        note_kind="gold", foot=SINT)


def se294_duplicacion() -> Fig:
    return line_chart(
        "120 cambios sobre dos usos parecidos: divergencias por olvido frente a ramas añadidas",
        "Líneas según la fracción de cambios que afecta a ambos usos: las divergencias por olvido de dos copias bajan de 32,3 con el 90 por ciento a 3,6 con el 10 por ciento, mientras que las ramas que añade la función compartida suben de 12,0 a 108,0; las curvas se cruzan entre las fracciones 0,5 y 0,9.",
        [("Dos copias: divergencias por olvido", [(0.1, 3.6), (0.5, 18.0), (0.9, 32.3)], "coral"),
         ("Función compartida: ramas añadidas", [(0.1, 108.0), (0.5, 60.1), (0.9, 12.0)], "teal")],
        x_label="Fracción de cambios que afecta a ambos usos", y_label="Divergencias o ramas en 120 cambios",
        x_ticks=[(0.1, "0,1"), (0.3, "0,3"), (0.5, "0,5"), (0.7, "0,7"), (0.9, "0,9")], y_ticks=[0, 20, 40, 60, 80, 100, 120],
        decimals=1, plot_h=280,
        note="La duplicación es un problema cuando los usos cambian por la misma razón; unirlos cuando cambian por razones distintas compra ramas y parámetros. No decide el parecido del texto sino la razón de cambio. Supuestos: olvido del 30 % en cada cambio común y una rama por cada cambio de un solo uso.",
        note_kind="teal", foot=SINT)


def se294_envidia() -> Fig:
    return scatter(
        "Envidia de características en 8 métodos: accesos propios y ajenos frente al criterio del autor",
        "Dispersión de ocho métodos según sus accesos propios y ajenos: los tres que el autor considera un problema tienen cero accesos propios y tres o más ajenos, y el detector los señala; el serializador también tiene cero propios y cuatro ajenos y es una falsa alarma; los otros cuatro métodos legítimos no se señalan.",
        [("Problema según el autor (señalado)", [(0, 6, "Recibo.texto", "r"), (0, 3, "Política.aplica", "r"), (-0.1, 4, "Etiqueta.línea", "l")], "coral"),
         ("Legítimo, señalado (falsa alarma)", [(0.1, 4, "Serializador.a_dict", "r")], "gold"),
         ("Legítimo, no señalado", [(3, 2, "Visitante.visita_envio", "r"), (3, 0, "Pedido.total", "t"), (1, 1, "Calculadora.costo", "r"), (2, 0, "Cuenta.saldo_neto", "t")], "teal")],
        x_label="Accesos propios", y_label="Accesos a otro objeto",
        x_ticks=[(-1, ""), (0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4")],
        y_ticks=[0, 1, 2, 3, 4, 5, 6, 7], hlines=[(3, "umbral del detector: 3")], decimals=0,
        y_zero=True, plot_h=300, width=980,
        note="Tres verdaderos positivos, una falsa alarma y cuatro verdaderos negativos: el serializador accede a los campos de otro objeto por oficio. Los dos métodos con 0 accesos propios y 4 ajenos se dibujan separados 0,1 a cada lado para que se vean. Que el método sea problema depende de si moverlo mejoraría el diseño: lo decide una persona con el contexto. Ocho métodos y etiquetas del autor.",
        note_kind="gold", foot=SINT)


FIGURES = {
    "se-301-cohesion-lcom4.svg": se289_lcom,
    "se-301-sitios-de-edicion.svg": se289_sitios,
    "se-301-primer-ciclo-de-dependencias.svg": se289_ciclos,
    "se-302-anadir-reglas-sin-modificar.svg": se290_reglas,
    "se-302-violaciones-de-liskov.svg": se290_liskov,
    "se-302-interfaz-ancha-e-indireccion.svg": se290_interfaces,
    "se-303-clase-base-fragil.svg": se291_base,
    "se-303-orden-de-decoradores.svg": se291_decoradores,
    "se-303-herencia-multiple-al-azar.svg": se291_mro,
    "se-304-singleton-y-orden-de-pruebas.svg": se292_singleton,
    "se-304-aislamiento-de-observadores.svg": se292_observadores,
    "se-304-patrones-con-la-misma-estructura.svg": se292_estructura,
    "se-305-deteccion-de-impureza.svg": se293_impureza,
    "se-305-contrapresion.svg": se293_cola,
    "se-305-intercalaciones-de-dos-hilos.svg": se293_hilos,
    "se-306-umbrales-sobre-codigo-real.svg": se294_umbrales,
    "se-306-duplicacion-frente-a-parametros.svg": se294_duplicacion,
    "se-306-envidia-de-caracteristicas.svg": se294_envidia,
}
