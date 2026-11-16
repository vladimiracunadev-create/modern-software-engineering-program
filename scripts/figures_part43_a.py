"""Figures for SE-517 to SE-522 (design and enterprise patterns: runs of real CPython code with ast analysis, a seeded simulation and an in-memory sqlite3 database; Windows CPython 3.12; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab
from figures_part40_a import bars, flow

EJEC = "Código ejecutado de verdad (CPython 3.12, Windows 11); los recuentos son deterministas y los tiempos varían de equipo en equipo."
SIM = "Simulación con semilla fija sobre código ejecutado de verdad (CPython 3.12); las magnitudes son de este modelo, no de un sistema real."


# ---------------------------------------------------------------- SE-517
def se517_costo_del_patron() -> Fig:
    rows = [['2', '41', '85', '3', '2'], ['4', '71', '125', '5', '2'], ['8', '131', '205', '9', '2'], ['12', '191', '285', '13', '2']]
    return tab('Strategy frente a if/elif: tamaño y complejidad crecen distinto con el número de variantes',
               'Tabla con el tamaño en nodos de sintaxis y la complejidad ciclomática máxima de una función de tarifas escrita como cadena if y elif y como Strategy con registro: con 2 variantes son 41 y 85 nodos, con 4 son 71 y 125, con 8 son 131 y 205 y con 12 son 191 y 285; la complejidad máxima por función crece de 3 a 13 con if y elif y se mantiene en 2 con Strategy.',
               ['Variantes', 'Nodos if/elif', 'Nodos Strategy', 'CC máx. if/elif', 'CC máx. Strategy'], rows, [150, 190, 210, 200, 210], row_h=44, size=13,
               note='El patrón cuesta más código en todos los tamaños probados (de 1,6 a 2,1 veces los nodos) y mantiene plana la complejidad de cada función. Añadir la quinta variante cambia una función existente con if/elif y ninguna con Strategy.',
               note_kind='gold', foot=EJEC)


def se517_cuando_usar() -> Fig:
    return flow('Pregunta por la fuerza antes de elegir el patrón',
                'Diagrama de decisión en cuatro cajas: nombrar la fuerza que duele, comprobar que la variación existe hoy y no solo en la imaginación, medir el costo del patrón en tamaño y en indirección y escribir la condición de salida; una flecha de retorno lleva a la primera caja si la fuerza no se puede nombrar.',
                [[('FUERZA\nNombra qué duele hoy: una variante nueva, un acoplamiento o un fallo', 'coral'), ('EVIDENCIA\nLa variación ya existe en el código o en el backlog, no en la imaginación', 'teal'), ('COSTO\nMide nodos, indirección y quien tiene que aprenderlo', 'gold')],
                 [('SALIDA\nEscribe cuándo se retirará el patrón y cómo se sabrá', 'navy')]],
                note='Un patrón sin fuerza nombrada es decoración con costo; con fuerza nombrada, evidencia y salida es una decisión que otra persona puede revisar.',
                note_kind='teal', box_h=100, foot=EJEC)


def se517_vocabulario_y_riesgo() -> Fig:
    rows = [['Vocabulario común', 'Decir «es un Decorator» condensa una estructura conocida', 'Se usa el nombre sin que la estructura exista'],
            ['Solución probada', 'Resuelve un problema recurrente en un contexto', 'El contexto cambió y la solución se copió igual'],
            ['Evaluación del diseño', 'Da criterios para discutir alternativas', 'Se convierte en lista de verificación sin fuerza'],
            ['Enseñanza', 'Permite entrar a un código ajeno más rápido', 'Se ve patrón donde hay un nombre de clase']]
    return tab('Qué aporta un catálogo de patrones y cómo se estropea',
               'Tabla con cuatro aportes de un catálogo de patrones, vocabulario común, solución probada, evaluación del diseño y enseñanza, y para cada uno el modo en que se estropea cuando se usa sin la fuerza que lo justifica.',
               ['Aporte', 'Cuando funciona', 'Cómo se estropea'], rows, [210, 380, 370], row_h=60, size=13,
               note='La tabla resume el argumento de la clase; la evidencia medida está en la figura anterior y en las siguientes clases de la parte.',
               note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-518
def se518_singleton_y_orden() -> Fig:
    return bars('Cuatro pruebas en las 24 ordenaciones posibles: el Singleton con estado hace que el orden importe',
                'Gráfico de barras con las 24 ordenaciones posibles de cuatro pruebas: con un Singleton de configuración mutable fallan 18 ordenaciones y con la misma lógica y la configuración inyectada fallan 0.',
                [('Singleton con estado mutable', 18, 'coral', '18 de 24'), ('Configuración inyectada', 0, 'teal', '0 de 24')], 28,
                note='Un Singleton que guarda estado convierte cada prueba en dependiente de las anteriores. La falla no está en el patrón como idea, está en el estado global mutable.',
                note_kind='coral', foot=EJEC)


def se518_prototype_copia() -> Fig:
    rows = [['Copia superficial (copy.copy)', '1000 de 1000', '≈1 µs', 'Cada clon comparte la lista de destinatarios con la plantilla'],
            ['Copia profunda (copy.deepcopy)', '1 de 1000', '≈11 µs', 'Cada clon tiene su propia lista; cuesta unas 17 veces más que construir'],
            ['Construir desde cero', '0 de 1000', '≈0,6 µs', 'No hay plantilla compartida; hay que repetir los valores por defecto']]
    return tab('Prototype: añadir un destinatario a un clon contamina a los demás si la copia es superficial',
               'Tabla con tres formas de obtener 1000 avisos desde una plantilla: la copia superficial deja 1000 de 1000 clones afectados al añadir un destinatario a uno, la copia profunda deja 1 de 1000 con un coste de unos 11 microsegundos por copia, y construir desde cero deja 0 con unos 0,6 microsegundos.',
               ['Forma', 'Clones afectados', 'Coste por copia', 'Qué ocurre'], rows, [260, 170, 150, 380], row_h=72, size=13,
               note='La copia profunda corrige el defecto compartido y cuesta del orden de diez a veinte veces más que construir. Los tiempos son de un equipo y se dan como orden de magnitud.',
               note_kind='gold', foot=EJEC)


def se518_cuatro_creacionales() -> Fig:
    rows = [['Factory con registro', 'Canal desconocido', 'Rechaza al crear: 2 de 5 pedidos erróneos se detectan antes de enviar'],
            ['Builder / argumentos con nombre', 'Argumentos del mismo tipo intercambiados', '500 de 500 llamadas posicionales aceptadas; con kw_only se rechazan las 500'],
            ['Singleton', 'Un único punto de acceso', '18 de 24 ordenaciones de pruebas fallan con estado mutable'],
            ['Prototype', 'Copiar un objeto configurado', 'Superficial: 1000 contaminados; profunda: 1']]
    return tab('Cuatro patrones creacionales: la fuerza que atacan y lo que se midió',
               'Tabla con cuatro patrones creacionales, Factory con registro, Builder o argumentos con nombre, Singleton y Prototype, la fuerza que atacan y el resultado medido en el experimento: dos de cinco canales erróneos rechazados al crear, 500 de 500 llamadas posicionales aceptadas frente a 500 rechazadas con argumentos solo con nombre, 18 de 24 ordenaciones de pruebas fallidas con estado mutable y 1000 contaminados con copia superficial frente a 1 con copia profunda.',
               ['Patrón', 'Fuerza', 'Resultado medido'], rows, [250, 280, 430], row_h=64, size=13,
               note='En Python, argumentos con nombre y dataclasses sustituyen buena parte del Builder; el mecanismo del patrón sigue siendo útil en lenguajes sin ellos.',
               note_kind='teal', foot=EJEC)


# ---------------------------------------------------------------- SE-519
def se519_orden_de_decoradores() -> Fig:
    rows = [['Reintento por fuera, plazo de 80 ms por intento', '97,5 %', '240 ms', '1,37'],
            ['Plazo total de 80 ms por fuera de los reintentos', '71,2 %', '80 ms', '1,00']]
    return tab('Dos órdenes de los mismos decoradores, 3000 peticiones con latencias lognormales',
               'Tabla con dos órdenes de los mismos decoradores de plazo y reintento sobre 3000 peticiones con latencias lognormales de semilla fija: con el reintento por fuera y un plazo de 80 milisegundos por intento el éxito es 97,5 por ciento, el percentil 99 de latencia es 240 milisegundos y hay 1,37 llamadas al backend por petición; con un plazo total de 80 milisegundos por fuera de los reintentos el éxito es 71,2 por ciento, el percentil 99 es 80 milisegundos y hay 1,00 llamadas.',
               ['Orden de los decoradores', 'Éxito', 'Latencia p99', 'Llamadas por petición'], rows, [440, 140, 170, 210], row_h=70, size=13,
               note='Los mismos dos decoradores, apilados en otro orden, producen sistemas con políticas distintas: uno compra éxito con latencia y carga; el otro acota la latencia y pierde peticiones. El orden es una decisión de diseño, no un detalle.',
               note_kind='coral', foot=SIM)


def se519_cinco_estructurales() -> Fig:
    rows = [['Adapter', 'Dos proveedores con formas distintas', 'Ambos devuelven (id, aceptado) tras la adaptación'],
            ['Facade', 'Cliente que coordina subsistemas', '7 llamadas del cliente pasan a 1'],
            ['Proxy', 'Objeto costoso que no siempre se usa', '1000 proxies, 37 usos, 37 objetos construidos'],
            ['Composite', 'Grupos que contienen grupos', 'Con ciclo: lista correcta con guarda; RecursionError sin ella'],
            ['Decorator', 'Añadir comportamiento sin tocar el objeto', 'El orden de apilado cambia la política']]
    return tab('Cinco patrones estructurales y el hecho medido de cada uno',
               'Tabla con cinco patrones estructurales y un hecho medido de cada uno: el Adapter unifica dos proveedores en la misma forma, la Facade reduce siete llamadas del cliente a una, el Proxy perezoso construye 37 objetos para 1000 proxies cuando solo se usan 37, el Composite con un ciclo produce la lista correcta con una guarda de visitados y un error de recursión sin ella, y el orden de apilado de los Decorator cambia la política.',
               ['Patrón', 'Fuerza', 'Hecho medido'], rows, [170, 340, 450], row_h=56, size=13,
               note='Los cinco comparten una forma (un objeto que envuelve o contiene a otro con la misma interfaz) y se distinguen por la intención: adaptar, simplificar, controlar el acceso, componer o añadir.',
               note_kind='teal', foot=EJEC)


def se519_envoltura() -> Fig:
    return flow('Quién envuelve a quién: el orden de la pila de decoradores',
                'Diagrama de dos pilas de tres cajas: en la primera, el reintento envuelve al plazo y este al backend, de modo que cada intento tiene su propio plazo; en la segunda, el plazo envuelve al reintento y este al backend, de modo que un solo plazo cubre todos los intentos.',
                [[('Reintento\n(por fuera)', 'navy'), ('Plazo por intento\n(por dentro)', 'gold'), ('Backend', 'teal')],
                 [('Plazo total\n(por fuera)', 'navy'), ('Reintento\n(por dentro)', 'gold'), ('Backend', 'teal')]],
                note='Cada fila es una pila. Lo que está más afuera decide primero y ve el costo de todo lo que envuelve: el plazo por fuera limita el tiempo total; el reintento por fuera multiplica los intentos.',
                note_kind='gold', box_h=70, foot=EJEC)


# ---------------------------------------------------------------- SE-520
def se520_banderas_y_estados() -> Fig:
    return bars('Diez mil secuencias de seis eventos: estados imposibles con banderas y con máquina de estados',
                'Gráfico de barras con el porcentaje de secuencias de seis eventos aleatorios que terminan en una combinación imposible de banderas, 69,7 por ciento con cuatro banderas booleanas y 0 por ciento con una máquina de estados que rechaza las transiciones ilegales.',
                [('Cuatro banderas booleanas', 69.7, 'coral', '69,7 %'), ('Tabla de transiciones', 0, 'teal', '0 %')], 9,
                note='Cuatro banderas representan 16 combinaciones y 9 violan las reglas; la máquina tiene 5 estados y 6 transiciones legales de 25 pares posibles, y rechaza el resto por nombre. El porcentaje depende de la definición de «imposible» del autor.',
                note_kind='coral', foot=SIM)


def se520_observer_y_comando() -> Fig:
    rows = [['Observer con referencias fuertes', '1000 oyentes descartados sin darse de baja', '1000 siguen vivos'],
            ['Observer con referencias débiles', 'Los mismos 1000 oyentes', '0 siguen vivos'],
            ['Notificación sin aislamiento', '4 oyentes, el segundo falla', 'Entrega a 1 oyente'],
            ['Notificación con aislamiento', '4 oyentes, el segundo falla', 'Entrega a 3 y registra 1 error'],
            ['Command con deshacer', '200 secuencias aleatorias', 'Estado inicial recuperado en 200 de 200']]
    return tab('Observer y Command: fugas, aislamiento de fallos y deshacer, medidos',
               'Tabla con cinco medidas de Observer y Command: con referencias fuertes quedan vivos 1000 de 1000 oyentes descartados y con referencias débiles 0; sin aislamiento un oyente que falla impide la entrega a los otros y se entrega a 1 de 4, con aislamiento se entrega a 3 y se registra 1 error; y un Command con deshacer recupera el estado inicial en 200 de 200 secuencias aleatorias.',
               ['Variante', 'Situación', 'Resultado'], rows, [330, 330, 300], row_h=52, size=13,
               note='El Observer desacopla al emisor de los receptores, pero deja a su cargo el ciclo de vida de los oyentes y el aislamiento de sus fallos: sin ellos, el desacoplamiento es una trampa.',
               note_kind='gold', foot=EJEC)


def se520_cinco_conductuales() -> Fig:
    return flow('Cinco patrones conductuales: qué parte del comportamiento se hace intercambiable',
                'Diagrama de cinco cajas en dos filas: Strategy hace intercambiable el algoritmo, Observer hace intercambiables los receptores, Command convierte una acción en un objeto que se puede encolar y deshacer, State hace que el comportamiento dependa de un estado nombrado y Template Method fija el esqueleto y deja pasos variables.',
                [[('STRATEGY\nel algoritmo', 'navy'), ('OBSERVER\nlos receptores', 'teal'), ('COMMAND\nla acción como objeto', 'gold')],
                 [('STATE\nel comportamiento según el estado', 'coral'), ('TEMPLATE METHOD\nesqueleto fijo, pasos variables', 'navy')]],
                note='Todos mueven una decisión de un condicional a un objeto. La pregunta práctica es si el condicional que se elimina crecía de verdad.',
                note_kind='teal', box_h=76, foot=EJEC)


# ---------------------------------------------------------------- SE-521
def se521_un_cambio_dos_disenos() -> Fig:
    rows = [['A: la lógica vive en quien la usa', '3', '3', '(33,5 ; 35)', 'Inconsistente'],
            ['B: Experto en información (Linea.subtotal)', '0', '2', '(33,5 ; 33,5)', 'Consistente']]
    return tab('El mismo cambio de regla, un descuento del 10 % hecho en un solo lugar, en dos diseños',
               'Tabla con dos diseños del cálculo de totales de un pedido y el efecto de aplicar un descuento del 10 por ciento a partir de tres unidades en un solo lugar: en el diseño A, donde tres clases leen el precio del producto de cada línea, el total de Checkout da 33,5 y el de Factura 35 y son inconsistentes; en el diseño B, donde la línea calcula su subtotal, ambos dan 33,5 y son consistentes.',
               ['Diseño', 'Clases que leen el precio ajeno', 'Copias de la fórmula', 'Totales', 'Resultado'], rows, [250, 230, 140, 180, 160], row_h=72, size=13,
               note='Asignar el cálculo a quien tiene los datos (Experto en información) hace que un cambio de regla se haga en un lugar. No es un teorema: es una consecuencia verificable de dónde viven los datos.',
               note_kind='teal', foot=EJEC)


def se521_nueve_grasp() -> Fig:
    return flow('Los nueve principios GRASP agrupados por la pregunta que responden',
                'Diagrama de cuatro cajas con los nueve principios GRASP agrupados por pregunta: quién hace el trabajo con Creador, Experto en información y Controlador; cómo se relacionan con Bajo acoplamiento y Alta cohesión; cómo se varía con Polimorfismo y Variaciones protegidas; y cómo se aísla con Indirección y Fabricación pura.',
                [[('¿QUIÉN HACE EL TRABAJO?\nCreador · Experto en información · Controlador', 'navy'), ('¿CÓMO SE RELACIONAN?\nBajo acoplamiento · Alta cohesión', 'teal')],
                 [('¿CÓMO SE VARÍA?\nPolimorfismo · Variaciones protegidas', 'gold'), ('¿CÓMO SE AÍSLA?\nIndirección · Fabricación pura', 'coral')]],
                note='GRASP son criterios para decidir dónde poner una responsabilidad, no una lista de clases. Dos principios pueden tirar en direcciones opuestas y la decisión es del diseñador.',
                note_kind='gold', box_h=90, foot=EJEC)


def se521_cohesion_y_acoplamiento() -> Fig:
    rows = [['Servicio con 10 métodos y 8 dependencias', '10', '8', '37 de 45'],
            ['Registro (después de separar)', '2', '1', '0 de 1'],
            ['Notificador (después de separar)', '2', '3', '0 de 1'],
            ['Migración (después de separar)', '3', '1', '0 de 3']]
    return tab('Cohesión medida con ast: pares de métodos que no comparten ningún atributo',
               'Tabla con la cohesión medida con análisis de sintaxis: una clase de servicio con diez métodos y ocho dependencias en el constructor tiene 37 de 45 pares de métodos que no comparten ningún atributo, y al separarla en tres clases, Registro, Notificador y Migración, ningún par queda sin compartir estado.',
               ['Clase', 'Métodos', 'Dependencias', 'Pares sin estado compartido'], rows, [380, 150, 180, 250], row_h=48, size=13,
               note='Pares de métodos que no comparten atributos es una aproximación a la falta de cohesión (LCOM). Es una señal, no una sentencia: dos métodos pueden estar cohesionados por el dominio sin tocar el mismo atributo.',
               note_kind='gold', foot=EJEC)


# ---------------------------------------------------------------- SE-522
def se522_consultas() -> Fig:
    return bars('Listar 200 entregas con el nombre de su curso: consultas ejecutadas',
                'Gráfico de barras con el número de consultas a la base de datos al listar 200 entregas con el nombre de su curso: 201 con una consulta por entrega, el problema de las N más una consultas, y 1 con una sola consulta de lectura que une las dos tablas.',
                [('Un repositorio que carga cada curso por separado', 201, 'coral', '201 consultas'), ('Una consulta de lectura con unión', 1, 'teal', '1 consulta')], 2.2,
                note='Un Repository que oculta la base oculta también el número de consultas. La medición sale de contar las sentencias con un gancho de sqlite3, no de suponerlas.',
                note_kind='coral', foot=EJEC, label_w=420)


def se522_unidad_de_trabajo() -> Fig:
    rows = [['Guardar todo lo cargado', '100', 'Escribe 97 filas que no cambiaron'],
            ['Seguir los cambios (Unit of Work)', '3', 'Solo escribe las filas modificadas'],
            ['Dos pasos sin transacción, falla a mitad', '1 persistido', 'Queda a medias: estado «entregada» sin el segundo paso'],
            ['Dos pasos en una transacción, falla a mitad', '0 persistidos', 'Vuelve atrás: estado «pendiente»']]
    return tab('Unit of Work: sentencias UPDATE y atomicidad, medidas con sqlite3 en memoria',
               'Tabla con cuatro medidas sobre una base sqlite3 en memoria: guardar todo lo cargado ejecuta 100 UPDATE aunque solo 3 de 100 entregas cambiaron, seguir los cambios ejecuta 3, una operación de dos pasos sin transacción que falla a mitad deja el primer paso persistido y la misma operación dentro de una transacción vuelve atrás y deja el estado pendiente.',
               ['Variante', 'UPDATE o pasos persistidos', 'Qué ocurre'], rows, [380, 220, 360], row_h=60, size=13,
               note='La unidad de trabajo agrupa lo que debe cambiar junto y lo que debe volver atrás junto. En SQL, la transacción es el mecanismo; el patrón es la disciplina de abrirla en un único lugar.',
               note_kind='teal', foot=EJEC)


def se522_tres_formas() -> Fig:
    rows = [['Repository', 'Colección en memoria de agregados', 'Doble de prueba ≈11 µs frente a sqlite ≈600 µs por caso (≈50×)'],
            ['Unit of Work', 'Una transacción por caso de uso', 'Fallo a mitad: 0 filas persistidas en lugar de 1'],
            ['Active Record', 'La entidad sabe guardarse', 'La regla pura corre sin base; la que llama a save falla sin conexión']]
    return tab('Tres formas de poner el acceso a datos en el modelo y lo que se midió de cada una',
               'Tabla con tres formas de acceso a datos, Repository, Unit of Work y Active Record, y lo medido: un doble en memoria de un repositorio ejecuta un caso en unos 11 microsegundos frente a unos 600 de sqlite en memoria, una unidad de trabajo deja 0 filas persistidas tras un fallo a mitad frente a 1 sin ella, y en Active Record la regla pura corre sin base pero la que llama a guardar falla sin conexión.',
               ['Patrón', 'Qué modela', 'Qué se midió'], rows, [200, 310, 450], row_h=64, size=13,
               note='Ambas formas de prueba son rápidas: la diferencia de 50 veces importa con miles de pruebas, no con decenas. Active Record es una opción razonable cuando el modelo es casi las tablas; deja de serlo cuando la regla de negocio crece.',
               note_kind='gold', foot=EJEC)


FIGURES = {
    "se-517-costo-del-patron.svg": se517_costo_del_patron,
    "se-517-cuando-usar.svg": se517_cuando_usar,
    "se-517-vocabulario-y-riesgo.svg": se517_vocabulario_y_riesgo,
    "se-518-singleton-y-orden.svg": se518_singleton_y_orden,
    "se-518-prototype-copia.svg": se518_prototype_copia,
    "se-518-cuatro-creacionales.svg": se518_cuatro_creacionales,
    "se-519-orden-de-decoradores.svg": se519_orden_de_decoradores,
    "se-519-cinco-estructurales.svg": se519_cinco_estructurales,
    "se-519-envoltura.svg": se519_envoltura,
    "se-520-banderas-y-estados.svg": se520_banderas_y_estados,
    "se-520-observer-y-comando.svg": se520_observer_y_comando,
    "se-520-cinco-conductuales.svg": se520_cinco_conductuales,
    "se-521-un-cambio-dos-disenos.svg": se521_un_cambio_dos_disenos,
    "se-521-nueve-grasp.svg": se521_nueve_grasp,
    "se-521-cohesion-y-acoplamiento.svg": se521_cohesion_y_acoplamiento,
    "se-522-consultas.svg": se522_consultas,
    "se-522-unidad-de-trabajo.svg": se522_unidad_de_trabajo,
    "se-522-tres-formas.svg": se522_tres_formas,
}
