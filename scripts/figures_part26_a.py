"""Figures for SE-313 to SE-318 (design and enterprise patterns: runs of real CPython code with ast analysis, a seeded simulation and an in-memory sqlite3 database; Windows CPython 3.12; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig, dumbbell, grouped_bars, line_chart, scatter, stacked_bars
from figure_diagrams import chain, fan

from figures_part45_a import bars, flow

EJEC = "Código ejecutado de verdad (CPython 3.12, Windows 11); los recuentos son deterministas y los tiempos varían de equipo en equipo."
SIM = "Simulación con semilla fija sobre código ejecutado de verdad (CPython 3.12); las magnitudes son de este modelo, no de un sistema real."


# ---------------------------------------------------------------- SE-313
def se517_costo_del_patron() -> Fig:
    v = [2, 4, 8, 12]
    return line_chart(
        'Strategy frente a if/elif: tamaño y complejidad crecen distinto con el número de variantes',
        "Líneas en escala logarítmica con el tamaño en nodos de sintaxis y la complejidad ciclomática máxima de una función de tarifas según el número de variantes: if y elif pasa de 41 a 191 nodos y de complejidad 3 a 13; Strategy con registro pasa de 85 a 285 nodos y mantiene la complejidad en 2; el patrón cuesta más código y mantiene plana la complejidad.",
        [("Nodos Strategy", list(zip(v, [85, 125, 205, 285])), "coral"), ("Nodos if/elif", list(zip(v, [41, 71, 131, 191])), "gold"),
         ("Complejidad máx. if/elif", list(zip(v, [3, 5, 9, 13])), "teal"), ("Complejidad máx. Strategy", list(zip(v, [2, 2, 2, 2])), "navy")],
        x_label="Variantes de tarifa", y_label="Nodos o complejidad ciclomática", log_y=True,
        x_ticks=[(2, "2"), (4, "4"), (8, "8"), (12, "12")], y_ticks=[1, 10, 100, 1000], point_labels="none",
        note='El patrón cuesta más código en todos los tamaños probados (de 1,6 a 2,1 veces los nodos) y mantiene plana la complejidad de cada función. Añadir la quinta variante cambia una función existente con if/elif y ninguna con Strategy.', note_kind='gold', foot=EJEC)


def se517_cuando_usar() -> Fig:
    return flow('Pregunta por la fuerza antes de elegir el patrón',
                'Diagrama de decisión en cuatro cajas: nombrar la fuerza que duele, comprobar que la variación existe hoy y no solo en la imaginación, medir el costo del patrón en tamaño y en indirección y escribir la condición de salida; una flecha de retorno lleva a la primera caja si la fuerza no se puede nombrar.',
                [[('FUERZA\nNombra qué duele hoy: una variante nueva, un acoplamiento o un fallo', 'coral'), ('EVIDENCIA\nLa variación ya existe en el código o en el backlog, no en la imaginación', 'teal'), ('COSTO\nMide nodos, indirección y quien tiene que aprenderlo', 'gold')],
                 [('SALIDA\nEscribe cuándo se retirará el patrón y cómo se sabrá', 'navy')]],
                note='Un patrón sin fuerza nombrada es decoración con costo; con fuerza nombrada, evidencia y salida es una decisión que otra persona puede revisar.',
                note_kind='teal', box_h=100, foot=EJEC)


def se517_vocabulario_y_riesgo() -> Fig:
    return fan(
        'Qué aporta un catálogo de patrones y cómo se estropea',
        "Diagrama de cuatro aportes de un catálogo de patrones, vocabulario común, solución probada, evaluación del diseño y enseñanza, y para cada uno el modo en que se estropea: se usa el nombre sin la estructura, el contexto cambió y la solución se copió igual, se convierte en lista de verificación sin fuerza o se ve patrón donde hay un nombre de clase.",
        ("Un catálogo de patrones", "qué aporta y cómo se estropea", "navy"),
        [("Vocabulario común", "funciona: decir «es un Decorator» condensa una estructura conocida · se estropea: se usa el nombre sin que la estructura exista", "gold"),
         ("Solución probada", "funciona: resuelve un problema recurrente en un contexto · se estropea: el contexto cambió y la solución se copió igual", "gold"),
         ("Evaluación del diseño", "funciona: da criterios para discutir alternativas · se estropea: se convierte en lista de verificación sin fuerza", "gold"),
         ("Enseñanza", "funciona: permite entrar a un código ajeno más rápido · se estropea: se ve patrón donde hay un nombre de clase", "gold")],
        note='La tabla resume el argumento de la clase; la evidencia medida está en la figura anterior y en las siguientes clases de la parte.', note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-314
def se518_singleton_y_orden() -> Fig:
    return bars('Cuatro pruebas en las 24 ordenaciones posibles: el Singleton con estado hace que el orden importe',
                'Gráfico de barras con las 24 ordenaciones posibles de cuatro pruebas: con un Singleton de configuración mutable fallan 18 ordenaciones y con la misma lógica y la configuración inyectada fallan 0.',
                [('Singleton con estado mutable', 18, 'coral', '18 de 24'), ('Configuración inyectada', 0, 'teal', '0 de 24')], 28,
                note='Un Singleton que guarda estado convierte cada prueba en dependiente de las anteriores. La falla no está en el patrón como idea, está en el estado global mutable.',
                note_kind='coral', foot=EJEC)


def se518_prototype_copia() -> Fig:
    return grouped_bars(
        'Prototype: añadir un destinatario a un clon contamina a los demás si la copia es superficial',
        "Barras horizontales con los clones afectados, de 1 000, al añadir un destinatario a uno de ellos: con copia superficial son 1 000 de 1 000 porque comparten la lista con la plantilla, con copia profunda 1 y construyendo desde cero 0; la copia profunda cuesta unos 11 microsegundos frente a 1 de la superficial y 0,6 de construir.",
        ["Copia superficial (copy.copy), ≈1 µs", "Copia profunda (copy.deepcopy), ≈11 µs", "Construir desde cero, ≈0,6 µs"],
        [("Clones afectados", [1000, 1, 0], "coral")],
        unit="Clones afectados, de 1 000", horizontal=True, label_w=280, ticks=[0, 250, 500, 750, 1000],
        note='La copia profunda corrige el defecto compartido y cuesta del orden de diez a veinte veces más que construir. Los tiempos son de un equipo y se dan como orden de magnitud.', note_kind='gold', foot=EJEC)


def se518_cuatro_creacionales() -> Fig:
    return fan(
        'Cuatro patrones creacionales: la fuerza que atacan y lo que se midió',
        "Diagrama de cuatro patrones creacionales con la fuerza que atacan y lo medido: Factory con registro rechaza al crear 2 de 5 pedidos erróneos; Builder con argumentos con nombre rechaza las 500 llamadas con tipos intercambiados que la forma posicional aceptaba; Singleton hace fallar 18 de 24 ordenaciones de pruebas con estado mutable; Prototype contamina 1 000 clones con copia superficial y 1 con profunda.",
        ("Cuatro patrones creacionales", "la fuerza que atacan y lo que se midió", "navy"),
        [("Factory con registro", "ataca el canal desconocido · rechaza al crear: 2 de 5 pedidos erróneos se detectan antes de enviar", "teal"),
         ("Builder / argumentos con nombre", "ataca argumentos del mismo tipo intercambiados · 500 de 500 llamadas posicionales aceptadas; con kw_only se rechazan las 500", "teal"),
         ("Singleton", "ofrece un único punto de acceso · 18 de 24 ordenaciones de pruebas fallan con estado mutable", "coral"),
         ("Prototype", "copiar un objeto configurado · superficial: 1 000 contaminados; profunda: 1", "gold")],
        note='En Python, argumentos con nombre y dataclasses sustituyen buena parte del Builder; el mecanismo del patrón sigue siendo útil en lenguajes sin ellos.', note_kind='teal', foot=EJEC)


# ---------------------------------------------------------------- SE-315
def se519_orden_de_decoradores() -> Fig:
    return scatter(
        'Dos órdenes de los mismos decoradores, 3000 peticiones con latencias lognormales',
        "Dispersión de la latencia p99 y el éxito de dos órdenes de los mismos decoradores sobre 3 000 peticiones: con el reintento por fuera y un plazo de 80 ms por intento el éxito es 97,5 por ciento, la latencia p99 240 ms y 1,37 llamadas por petición; con el plazo total de 80 ms por fuera de los reintentos el éxito es 71,2 por ciento, la latencia 80 ms y 1,00 llamadas.",
        [("Reintento por fuera, plazo por intento", [(240, 97.5, "97,5 % · 240 ms · 1,37 llamadas", "l")], "teal"), ("Plazo total por fuera de los reintentos", [(80, 71.2, "71,2 % · 80 ms · 1,00 llamadas", "r")], "coral")],
        x_label="Latencia p99 (ms)", y_label="Éxito (%)", x_ticks=[(0, "0"), (50, "50"), (100, "100"), (150, "150"), (200, "200"), (250, "250"), (300, "")], y_ticks=[60, 70, 80, 90, 100], y_zero=False,
        note='Los mismos dos decoradores, apilados en otro orden, producen sistemas con políticas distintas: uno compra éxito con latencia y carga; el otro acota la latencia y pierde peticiones. El orden es una decisión de diseño, no un detalle.', note_kind='coral', foot=SIM)


def se519_cinco_estructurales() -> Fig:
    return fan(
        'Cinco patrones estructurales y el hecho medido de cada uno',
        "Diagrama de cinco patrones estructurales con un hecho medido de cada uno: el Adapter unifica dos proveedores en la misma forma, la Facade reduce siete llamadas del cliente a una, el Proxy construye 37 objetos para 1 000 proxies con 37 usos, el Composite necesita una guarda ante un ciclo y el orden de apilado del Decorator cambia la política.",
        ("Cinco patrones estructurales", "la fuerza y el hecho medido", "navy"),
        [("Adapter", "dos proveedores con formas distintas · ambos devuelven (id, aceptado) tras la adaptación", "teal"),
         ("Facade", "cliente que coordina subsistemas · 7 llamadas del cliente pasan a 1", "teal"),
         ("Proxy", "objeto costoso que no siempre se usa · 1 000 proxies, 37 usos, 37 objetos construidos", "teal"),
         ("Composite", "grupos que contienen grupos · con ciclo: lista correcta con guarda; RecursionError sin ella", "gold"),
         ("Decorator", "añadir comportamiento sin tocar el objeto · el orden de apilado cambia la política", "gold")],
        note='Los cinco comparten una forma (un objeto que envuelve o contiene a otro con la misma interfaz) y se distinguen por la intención: adaptar, simplificar, controlar el acceso, componer o añadir.', note_kind='teal', foot=EJEC)


def se519_envoltura() -> Fig:
    return flow('Quién envuelve a quién: el orden de la pila de decoradores',
                'Diagrama de dos pilas de tres cajas: en la primera, el reintento envuelve al plazo y este al backend, de modo que cada intento tiene su propio plazo; en la segunda, el plazo envuelve al reintento y este al backend, de modo que un solo plazo cubre todos los intentos.',
                [[('Reintento\n(por fuera)', 'navy'), ('Plazo por intento\n(por dentro)', 'gold'), ('Backend', 'teal')],
                 [('Plazo total\n(por fuera)', 'navy'), ('Reintento\n(por dentro)', 'gold'), ('Backend', 'teal')]],
                note='Cada fila es una pila. Lo que está más afuera decide primero y ve el costo de todo lo que envuelve: el plazo por fuera limita el tiempo total; el reintento por fuera multiplica los intentos.',
                note_kind='gold', box_h=70, foot=EJEC)


# ---------------------------------------------------------------- SE-316
def se520_banderas_y_estados() -> Fig:
    return bars('Diez mil secuencias de seis eventos: estados imposibles con banderas y con máquina de estados',
                'Gráfico de barras con el porcentaje de secuencias de seis eventos aleatorios que terminan en una combinación imposible de banderas, 69,7 por ciento con cuatro banderas booleanas y 0 por ciento con una máquina de estados que rechaza las transiciones ilegales.',
                [('Cuatro banderas booleanas', 69.7, 'coral', '69,7 %'), ('Tabla de transiciones', 0, 'teal', '0 %')], 6,
                note='Cuatro banderas representan 16 combinaciones y 9 violan las reglas; la máquina tiene 5 estados y 6 transiciones legales de 25 pares posibles, y rechaza el resto por nombre. El porcentaje depende de la definición de «imposible» del autor.',
                note_kind='coral', foot=SIM)


def se520_observer_y_comando() -> Fig:
    return fan(
        'Observer y Command: fugas, aislamiento de fallos y deshacer, medidos',
        "Diagrama de cinco medidas de Observer y Command: con referencias fuertes quedan vivos 1 000 de 1 000 oyentes descartados y con referencias débiles 0; sin aislamiento un oyente que falla impide la entrega a los demás y con aislamiento se entrega a 3 y se registra 1 error; el deshacer recupera el estado inicial en 200 de 200 secuencias.",
        ("Observer y Command", "fugas, aislamiento de fallos y deshacer", "navy"),
        [("Observer con referencias fuertes", "1 000 oyentes descartados sin darse de baja: 1 000 siguen vivos", "coral"),
         ("Observer con referencias débiles", "los mismos 1 000 oyentes: 0 siguen vivos", "teal"),
         ("Notificación sin aislamiento", "4 oyentes, el segundo falla: entrega a 1 oyente", "coral"),
         ("Notificación con aislamiento", "4 oyentes, el segundo falla: entrega a 3 y registra 1 error", "teal"),
         ("Command con deshacer", "200 secuencias aleatorias: estado inicial recuperado en 200 de 200", "teal")],
        note='El Observer desacopla al emisor de los receptores, pero deja a su cargo el ciclo de vida de los oyentes y el aislamiento de sus fallos: sin ellos, el desacoplamiento es una trampa.', note_kind='gold', foot=EJEC)


def se520_cinco_conductuales() -> Fig:
    return flow('Cinco patrones conductuales: qué parte del comportamiento se hace intercambiable',
                'Diagrama de cinco cajas en dos filas: Strategy hace intercambiable el algoritmo, Observer hace intercambiables los receptores, Command convierte una acción en un objeto que se puede encolar y deshacer, State hace que el comportamiento dependa de un estado nombrado y Template Method fija el esqueleto y deja pasos variables.',
                [[('STRATEGY\nel algoritmo', 'navy'), ('OBSERVER\nlos receptores', 'teal'), ('COMMAND\nla acción como objeto', 'gold')],
                 [('STATE\nel comportamiento según el estado', 'coral'), ('TEMPLATE METHOD\nesqueleto fijo, pasos variables', 'navy')]],
                note='Todos mueven una decisión de un condicional a un objeto. La pregunta práctica es si el condicional que se elimina crecía de verdad.',
                note_kind='teal', box_h=76, foot=EJEC)


# ---------------------------------------------------------------- SE-317
def se521_un_cambio_dos_disenos() -> Fig:
    return grouped_bars(
        'El mismo cambio de regla, un descuento del 10 % hecho en un solo lugar, en dos diseños',
        "Barras agrupadas con dos diseños del cálculo de totales ante un descuento del 10 por ciento aplicado en un solo lugar: en el diseño A, 3 clases leen el precio ajeno y la fórmula está copiada 3 veces, y los totales quedan inconsistentes (33,5 y 35); en el diseño B, con el Experto en información, 0 clases leen el precio ajeno, hay 2 copias y los totales coinciden (33,5 y 33,5).",
        ["A: la lógica vive en quien la usa", "B: Experto en información (Linea.subtotal)"],
        [("Clases que leen el precio ajeno", [3, 0], "coral"), ("Copias de la fórmula", [3, 2], "gold")],
        unit="Clases o copias", ticks=[0, 1, 2, 3, 4],
        note='Asignar el cálculo a quien tiene los datos (Experto en información) hace que un cambio de regla se haga en un lugar. No es un teorema: es una consecuencia verificable de dónde viven los datos.', note_kind='teal', foot=EJEC)


def se521_nueve_grasp() -> Fig:
    return flow('Los nueve principios GRASP agrupados por la pregunta que responden',
                'Diagrama de cuatro cajas con los nueve principios GRASP agrupados por pregunta: quién hace el trabajo con Creador, Experto en información y Controlador; cómo se relacionan con Bajo acoplamiento y Alta cohesión; cómo se varía con Polimorfismo y Variaciones protegidas; y cómo se aísla con Indirección y Fabricación pura.',
                [[('¿QUIÉN HACE EL TRABAJO?\nCreador · Experto en información · Controlador', 'navy'), ('¿CÓMO SE RELACIONAN?\nBajo acoplamiento · Alta cohesión', 'teal')],
                 [('¿CÓMO SE VARÍA?\nPolimorfismo · Variaciones protegidas', 'gold'), ('¿CÓMO SE AÍSLA?\nIndirección · Fabricación pura', 'coral')]],
                note='GRASP son criterios para decidir dónde poner una responsabilidad, no una lista de clases. Dos principios pueden tirar en direcciones opuestas y la decisión es del diseñador.',
                note_kind='gold', box_h=90, foot=EJEC)


def se521_cohesion_y_acoplamiento() -> Fig:
    return grouped_bars(
        'Cohesión medida con ast: pares de métodos que no comparten ningún atributo',
        "Barras agrupadas con la cohesión medida con análisis de sintaxis: una clase de servicio con 10 métodos y 8 dependencias tiene 37 de 45 pares de métodos sin estado compartido; después de separarla, Registro (2 métodos, 1 dependencia), Notificador (2 y 3) y Migración (3 y 1) tienen 0 de 1, 0 de 1 y 0 de 3 pares sin estado compartido.",
        ["Servicio con 10 métodos y 8 dependencias", "Registro (después de separar)", "Notificador (después de separar)", "Migración (después de separar)"],
        [("Métodos", [10, 2, 2, 3], "grey"), ("Dependencias", [8, 1, 3, 1], "gold"), ("Pares sin estado compartido", [37, 0, 0, 0], "coral")],
        unit="Métodos, dependencias o pares", ticks=[0, 10, 20, 30, 40],
        note='Pares de métodos que no comparten atributos es una aproximación a la falta de cohesión (LCOM). Es una señal, no una sentencia: dos métodos pueden estar cohesionados por el dominio sin tocar el mismo atributo.', note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-318
def se522_consultas() -> Fig:
    return bars('Listar 200 entregas con el nombre de su curso: consultas ejecutadas',
                'Gráfico de barras con el número de consultas a la base de datos al listar 200 entregas con el nombre de su curso: 201 con una consulta por entrega, el problema de las N más una consultas, y 1 con una sola consulta de lectura que une las dos tablas.',
                [('Un repositorio que carga cada curso por separado', 201, 'coral', '201 consultas'), ('Una consulta de lectura con unión', 1, 'teal', '1 consulta')], 1.0,
                note='Un Repository que oculta la base oculta también el número de consultas. La medición sale de contar las sentencias con un gancho de sqlite3, no de suponerlas.',
                note_kind='coral', foot=EJEC, label_w=420)


def se522_unidad_de_trabajo() -> Fig:
    return fan(
        'Unit of Work: sentencias UPDATE y atomicidad, medidas con sqlite3 en memoria',
        "Diagrama de cuatro medidas sobre una base sqlite3 en memoria: guardar todo lo cargado ejecuta 100 UPDATE aunque solo cambiaron 3 de 100 entregas y seguir los cambios ejecuta 3; con dos pasos sin transacción un fallo a mitad deja 1 persistido y el estado entregada sin el segundo paso; con una transacción deja 0 y vuelve a pendiente.",
        ("Unit of Work", "sentencias UPDATE y atomicidad, con sqlite3 en memoria", "navy"),
        [("Guardar todo lo cargado: 100 UPDATE", "escribe 97 filas que no cambiaron", "coral"),
         ("Seguir los cambios (Unit of Work): 3 UPDATE", "solo escribe las filas modificadas", "teal"),
         ("Dos pasos sin transacción, falla a mitad: 1 persistido", "queda a medias: estado «entregada» sin el segundo paso", "coral"),
         ("Dos pasos en una transacción, falla a mitad: 0 persistidos", "vuelve atrás: estado «pendiente»", "teal")],
        note='La unidad de trabajo agrupa lo que debe cambiar junto y lo que debe volver atrás junto. En SQL, la transacción es el mecanismo; el patrón es la disciplina de abrirla en un único lugar.', note_kind='teal', foot=EJEC)


def se522_tres_formas() -> Fig:
    return fan(
        'Tres formas de poner el acceso a datos en el modelo y lo que se midió de cada una',
        "Diagrama de tres formas de poner el acceso a datos en el modelo y lo medido: un doble en memoria de un repositorio ejecuta un caso en unos 11 microsegundos frente a unos 600 con sqlite, cerca de 50 veces; una Unit of Work deja 0 filas persistidas en lugar de 1 si el fallo ocurre a mitad; con Active Record la regla pura corre sin base y la que llama a save falla sin conexión.",
        ("Tres formas de acceso a datos", "qué modelan y qué se midió", "navy"),
        [("Repository", "colección en memoria de agregados · doble de prueba ≈11 µs frente a sqlite ≈600 µs por caso (≈50×)", "teal"),
         ("Unit of Work", "una transacción por caso de uso · fallo a mitad: 0 filas persistidas en lugar de 1", "teal"),
         ("Active Record", "la entidad sabe guardarse · la regla pura corre sin base; la que llama a save falla sin conexión", "gold")],
        note='Ambas formas de prueba son rápidas: la diferencia de 50 veces importa con miles de pruebas, no con decenas. Active Record es una opción razonable cuando el modelo es casi las tablas; deja de serlo cuando la regla de negocio crece.', note_kind='gold', foot=EJEC)


FIGURES = {
    "se-313-costo-del-patron.svg": se517_costo_del_patron,
    "se-313-cuando-usar.svg": se517_cuando_usar,
    "se-313-vocabulario-y-riesgo.svg": se517_vocabulario_y_riesgo,
    "se-314-singleton-y-orden.svg": se518_singleton_y_orden,
    "se-314-prototype-copia.svg": se518_prototype_copia,
    "se-314-cuatro-creacionales.svg": se518_cuatro_creacionales,
    "se-315-orden-de-decoradores.svg": se519_orden_de_decoradores,
    "se-315-cinco-estructurales.svg": se519_cinco_estructurales,
    "se-315-envoltura.svg": se519_envoltura,
    "se-316-banderas-y-estados.svg": se520_banderas_y_estados,
    "se-316-observer-y-comando.svg": se520_observer_y_comando,
    "se-316-cinco-conductuales.svg": se520_cinco_conductuales,
    "se-317-un-cambio-dos-disenos.svg": se521_un_cambio_dos_disenos,
    "se-317-nueve-grasp.svg": se521_nueve_grasp,
    "se-317-cohesion-y-acoplamiento.svg": se521_cohesion_y_acoplamiento,
    "se-318-consultas.svg": se522_consultas,
    "se-318-unidad-de-trabajo.svg": se522_unidad_de_trabajo,
    "se-318-tres-formas.svg": se522_tres_formas,
}
