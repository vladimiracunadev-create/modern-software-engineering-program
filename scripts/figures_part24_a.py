"""Figures for SE-289 to SE-294 (code analysis and synthetic simulations, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Medición sobre código de ejemplo y simulación con semilla fija; salidas idénticas en Windows y Ubuntu (WSL2)."


# ---------------------------------------------------------------- SE-289
def se289_lcom() -> Fig:
    rows = [
        ["Envio (clase mezclada)", "7", "3", "precio, aviso y bitácora no comparten atributos"],
        ["Precio", "3", "1", "peso y zona"],
        ["Aviso", "2", "1", "correo y plantilla"],
        ["Bitacora", "2", "1", "líneas de registro"],
    ]
    return tab("Falta de cohesión (LCOM4) de una clase de envíos y de su separación",
               "Tabla: una clase de envíos con siete métodos tiene tres componentes de métodos que no comparten atributos, LCOM4 igual a 3; al separarla en precio, aviso y bitácora cada clase tiene LCOM4 igual a 1.",
               ["Clase", "Métodos", "LCOM4", "Qué agrupa"], rows, [250, 120, 110, 410], row_h=44, size=13,
               note="LCOM4 cuenta los grupos de métodos conectados por atributos compartidos o llamadas entre sí; 3 significa tres clases en una. Con clases aleatorias de seis métodos, si cada uno usa un solo atributo de seis, ninguna clase queda en 1; con dos atributos por método, el 88,7 %; con tres, el 100 %: la métrica mide densidad de uso, no calidad del diseño.",
               note_kind="gold", foot=SINT)


def se289_sitios() -> Fig:
    rows = [
        ["Los clientes leen el campo peso_kg", "30", "51"],
        ["Los clientes llaman a un getter peso()", "0", "51"],
        ["Los clientes piden comportamiento (costo_por_peso, excede_limite)", "0", "0"],
    ]
    return tab("Sitios que hay que editar en 30 clientes al cambiar la representación del peso",
               "Tabla: con treinta clientes sintéticos, renombrar el campo peso_kg obliga a editar 30 sitios si los clientes lo leen directamente y ninguno si usan un getter o piden comportamiento; cambiar la unidad de kilos a gramos obliga a editar 51 sitios con campo o getter y ninguno si el comportamiento está encapsulado.",
               ["Diseño de acceso", "Renombrar el campo", "Cambiar kg a g"], rows, [520, 190, 180], row_h=52, size=13,
               note="Un getter oculta el nombre pero no el significado: los clientes siguen multiplicando kilos. Solo encapsular la decisión (qué es el peso y cuánto cuesta) deja la unidad dentro. Los 30 clientes salen de cuatro plantillas elegidas con semilla fija; es una construcción del autor, no un proyecto real.",
               note_kind="teal", foot=SINT)


def se289_ciclos() -> Fig:
    rows = [
        ["20 aristas al azar entre 20 módulos", "65,0 %"],
        ["40 aristas al azar", "100 %"],
        ["60 aristas al azar", "100 %"],
        ["Aristas hasta el primer ciclo: mediana (p10 – p90)", "18  (9 – 27)"],
        ["Aristas hasta el primer ciclo: mínimo y máximo", "2 y 47"],
        ["Con orden de capas (solo hacia abajo): ciclos posibles", "0"],
    ]
    return tab("Probabilidad de ciclos entre 20 módulos cuando las dependencias se añaden sin regla",
               "Tabla: al añadir dependencias al azar entre veinte módulos hay ciclo en el 65 por ciento de los casos con veinte aristas y en el 100 por ciento con cuarenta; el primer ciclo aparece con una mediana de 18 aristas; con un orden de capas que solo permite dependencias hacia abajo no hay ciclos posibles.",
               ["Situación", "Resultado"], rows, [610, 260], row_h=40, size=13,
               note="Los ciclos no son un accidente raro: aparecen pronto cuando nadie decide el sentido de las dependencias. Un orden de capas permite 190 de las 380 aristas posibles y elimina los ciclos por construcción. Grafos sintéticos de 2000 repeticiones; un grafo real no es aleatorio.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-290
def se290_reglas() -> Fig:
    rows = [
        ["2.ª", "descuento", "+2 / −0", "3", "ninguna", "+4 / −0", "2"],
        ["3.ª", "descuento", "+2 / −0", "4", "ninguna", "+4 / −0", "2"],
        ["4.ª", "descuento", "+2 / −0", "5", "ninguna", "+4 / −0", "2"],
        ["5.ª", "descuento", "+2 / −0", "6", "ninguna", "+4 / −0", "2"],
    ]
    return tab("Añadir una regla de descuento: cadena if/elif frente a registro de reglas",
               "Tabla: al añadir de la segunda a la quinta regla de descuento, la cadena if elif modifica siempre la función existente, añade dos líneas y su complejidad sube de 3 a 6; el registro no modifica ninguna función existente, añade cuatro líneas y la complejidad de la función descuento se queda en 2.",
               ["Regla añadida", "Cadena: modifica", "Líneas", "Complejidad", "Registro: modifica", "Líneas", "Complejidad"], rows, [120, 170, 110, 140, 190, 110, 140], row_h=40, size=12,
               note="Abierto/cerrado se ve como funciones existentes que no cambian: en la cadena, cada regla nueva reabre la función que todas las pruebas atraviesan; en el registro, no. El registro escribe más líneas por regla. Cuesta además dos decisiones nuevas: el orden y cómo se combinan reglas simultáneas (aquí, el máximo).",
               note_kind="teal", foot=SINT)


def se290_liskov() -> Fig:
    rows = [
        ["Compatible", "0", "0 de 2000"],
        ["Rechaza pesos mayores de 20 (precondición más fuerte)", "0", "1236 (61,8 %)"],
        ["Pierde monotonía solo si peso > 45 y zona 1", "0", "3 (0,1 %)"],
        ["Pesos desde 30 con 20 % de descuento (no monótona)", "0", "18 (0,9 %)"],
        ["Lanza KeyError en la zona 5 (excepción nueva)", "0", "382 (19,1 %)"],
    ]
    return tab("Subclases que rompen el contrato de Tarifa: tres ejemplos frente a 2000 entradas al azar",
               "Tabla: de cuatro subclases que violan el contrato de una tarifa, tres ejemplos de camino feliz no detectan ninguna; 2000 entradas al azar con una comprobación de contrato detectan el 61,8 por ciento de la que rechaza pesos altos, el 19,1 de la que lanza una excepción nueva, el 0,9 de la no monótona y solo el 0,1 de la que falla en un rincón estrecho.",
               ["Subclase", "Fallos en 3 ejemplos", "Fallos en 2000 entradas al azar"], rows, [480, 170, 250], row_h=52, size=13,
               note="Probar con la superclase en la mano es la prueba de sustitución: todas las subclases deben pasar el mismo conjunto de comprobaciones. Una violación que ocurre en el 0,1 % del dominio se escapa incluso a 2000 entradas: el azar no sustituye a razonar sobre las condiciones del contrato. El contrato es del autor.",
               note_kind="coral", foot=SINT)


def se290_interfaces() -> Fig:
    rows = [
        ["Clientes afectados al cambiar un método (media de 12)", "usan el método: 1,75 · dependen de la interfaz: 8", "dependen del rol: 5"],
        ["Métodos que debe implementar un doble de prueba", "12", "7,5"],
        ["Redondear a dos decimales y aplicar un tope: clases y funciones", "0 clases · 1 función", "6 clases · 8 métodos"],
        ["Mismo cálculo: nodos del árbol sintáctico y líneas", "17 nodos · 2 líneas", "126 nodos · 17 líneas"],
    ]
    return tab("Interfaces anchas y estructura innecesaria sobre el mismo comportamiento",
               "Tabla: con ocho clientes que usan entre uno y tres de doce métodos, cambiar un método afecta de verdad a 1,75 clientes pero a ocho si todos dependen de la interfaz ancha y a cinco si dependen de roles; la misma regla de redondeo y tope ocupa 17 nodos en una función y 126 con estrategias y fábrica.",
               ["Medida", "Opción simple", "Opción estructurada"], rows, [400, 300, 190], row_h=64, size=12,
               note="Segregar interfaces reduce la dependencia nominal, no la real: aun con roles, cinco clientes revisan un cambio que afecta a 1,75. Y la abstracción tiene precio de lectura: 7 veces más nodos para la misma regla. Sin un segundo uso, esa estructura no compra nada. Ocho clientes sintéticos con semilla fija.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-291
def se291_base() -> Fig:
    rows = [
        ["Herencia", "1000 de 1000", "0 de 1000"],
        ["Composición y delegación", "0 de 1000", "0 de 1000"],
    ]
    return tab("Contador de elementos agregados: lotes con cuenta errónea según el diseño y la base",
               "Tabla: un contador implementado por herencia cuenta mal los mil lotes cuando la clase base implementa agregar todos llamando a agregar, y ninguno cuando la base la implementa de otra manera; el mismo contador por composición y delegación cuenta bien los mil lotes con ambas bases.",
               ["Diseño del contador", "Base V1 (agregar_todos llama a agregar)", "Base V2 (agregar_todos usa extend)"], rows, [260, 350, 300], row_h=52, size=13,
               note="La subclase funcionaba o fallaba según un detalle interno de la base que ni la interfaz ni la documentación prometían: eso es la clase base frágil. La composición solo depende de lo que la base promete. La prueba que pasó con V2 no vio que V1 existía. Lotes de 1 a 6 elementos con semilla fija.",
               note_kind="coral", foot=SINT)


def se291_decoradores() -> Fig:
    rows = [
        ["4", "15", "4", "24", "14 de 24"],
        ["6", "63", "6", "720", "—"],
        ["8", "255", "8", "40 320", "—"],
        ["10", "1023", "10", "3 628 800", "—"],
    ]
    return tab("Opciones de envío combinables: subclases por combinación frente a decoradores",
               "Tabla: con cuatro opciones combinables hacen falta 15 subclases por combinación frente a 4 decoradores; con diez opciones, 1023 frente a 10; pero los decoradores se pueden aplicar en 24 órdenes con cuatro opciones y en 3 628 800 con diez, y con cuatro opciones los 24 órdenes dan 14 totales distintos.",
               ["Opciones", "Subclases", "Decoradores", "Órdenes posibles", "Totales distintos"], rows, [130, 170, 190, 220, 200], row_h=44, size=13,
               note="Con base 50, frágil +4, seguro ×1,02, urgente ×1,30 y refrigerado +6, los 24 órdenes dan 14 totales entre 76,30 y 79,56: la composición cambia el crecimiento (lineal en vez de exponencial) pero el orden pasa a ser parte del diseño y debe fijarse o probarse.",
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


# ---------------------------------------------------------------- SE-292
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
    rows = [
        ["Bucle simple (la excepción sube y corta el reparto)", "4704 de 5000", "101", "899 a 980"],
        ["Cada observador aislado con try/except", "4894 de 5000", "106", "968 a 985"],
        ["Baja durante el reparto, sin copiar la lista", "visita a, c, d", "—", "se salta b"],
        ["Baja durante el reparto, con copia de la lista", "visita a, b, c, d", "—", "—"],
    ]
    return tab("Notificaciones entregadas con 1000 eventos y 5 observadores que fallan el 2 % de las veces",
               "Tabla: con mil eventos y cinco observadores que fallan el dos por ciento de las veces, un bucle simple entrega 4704 de 5000 notificaciones porque una excepción corta el reparto, y con cada observador aislado se entregan 4894; dar de baja un observador durante el reparto sin copiar la lista salta al siguiente.",
               ["Variante", "Entregas", "Excepciones", "Por observador"], rows, [430, 190, 130, 160], row_h=52, size=13,
               note="El primero en la lista casi nunca pierde nada y el último pierde más: el orden de suscripción se vuelve una prioridad implícita. Aislar a los observadores sube la entrega pero oculta los fallos si nadie cuenta las excepciones. Falla cada observador con probabilidad 0,02, un supuesto.",
               note_kind="gold", foot=SINT)


def se292_estructura() -> Fig:
    rows = [
        ["Adaptador", "1,000", "0,940", "0,987", "0,985", "0,988"],
        ["Proxy", "0,940", "1,000", "0,926", "0,937", "0,945"],
        ["Decorador", "0,987", "0,926", "1,000", "0,988", "0,980"],
        ["Estrategia", "0,985", "0,937", "0,988", "1,000", "0,992"],
        ["Estado", "0,988", "0,945", "0,980", "0,992", "1,000"],
    ]
    return tab("Similitud de la estructura sintáctica entre implementaciones de cinco patrones",
               "Tabla: la similitud coseno entre los tipos de nodo del árbol sintáctico de implementaciones mínimas de adaptador, proxy, decorador, estrategia y estado va de 0,926 a 0,992, de modo que el código por sí solo casi no distingue un patrón de otro.",
               ["", "Adaptador", "Proxy", "Decorador", "Estrategia", "Estado"], rows, [170, 150, 130, 150, 150, 130], row_h=40, size=13,
               note="Las cinco clases guardan un colaborador y le delegan: lo que cambia es la intención (traducir, controlar el acceso, añadir, intercambiar un algoritmo, cambiar de comportamiento con el estado). El patrón no se reconoce por la forma sino por el motivo del cambio. Cinco clases escritas por el autor.",
               note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-293
def se293_impureza() -> Fig:
    rows = [
        ["Muta su argumento (sort, append)", "no", "sí", "sí"],
        ["Imprime", "no", "sí", "sí"],
        ["Argumento por defecto mutable", "no", "sí", "sí"],
        ["Lee una configuración global", "no", "no", "sí"],
        ["Lee el reloj", "no", "no", "sí"],
        ["Escribe un total global", "no", "no", "sí"],
        ["Devuelve su estado interno", "no", "no", "no"],
        ["Total de 8 impurezas / falsas alarmas en 4 puras", "0 / 0", "4 / 0", "7 / 0"],
    ]
    return tab("Impurezas detectadas según el nivel de la prueba",
               "Tabla: de ocho funciones impuras, una prueba con un ejemplo no detecta ninguna, repetir la llamada y comprobar la entrada y la salida detecta cuatro, y además perturbar el estado global entre llamadas detecta siete; la que devuelve su estado interno no la detecta ningún nivel; ninguna de las cuatro funciones puras dio falsa alarma.",
               ["Impureza", "Un ejemplo", "Repetir y comprobar", "Y perturbar lo global"], rows, [380, 130, 200, 210], row_h=36, size=12,
               note="Una función con un solo ejemplo correcto no demuestra pureza. La que devuelve una referencia a su estado interno pasa los tres niveles: se descubre solo cuando alguien muta el valor devuelto. Doce funciones escritas por el autor; el detector es una construcción simple.",
               note_kind="gold", foot=SINT)


def se293_cola() -> Fig:
    rows = [
        ["Estable 70/s → 80/s", "Sin límite", "20 000 / 0", "48", "99,2", "422,4"],
        ["Estable 70/s → 80/s", "Bloquea al productor", "20 000 / 0", "20", "81,7", "308,7"],
        ["Saturada 100/s → 80/s", "Sin límite", "20 000 / 0", "3992", "24 713,8", "49 544,7"],
        ["Saturada 100/s → 80/s", "Bloquea al productor", "20 000 / 0", "20", "220,7", "386,1"],
        ["Saturada 100/s → 80/s", "Descarta lo nuevo", "16 009 / 3991", "20", "212,8", "376,2"],
        ["Saturada 100/s → 80/s", "Descarta lo viejo", "16 078 / 3922", "20", "167,4", "271,1"],
    ]
    return tab("Cola entre un productor y un consumidor: 20 000 eventos, capacidad 20 (latencias en ms)",
               "Tabla: cuando llegan 100 eventos por segundo y se atienden 80, una cola sin límite llega a 3992 elementos y una latencia media de 24 713,8 milisegundos; con capacidad 20, bloquear al productor, descartar lo nuevo o descartar lo viejo mantienen la latencia entre 167 y 221 milisegundos a costa de bloquear al productor 50 segundos o de perder entre 3922 y 3991 eventos.",
               ["Escenario", "Política", "Procesados / descartados", "Cola máx.", "Latencia media", "p99"], rows, [230, 230, 220, 100, 140, 110], row_h=40, size=12,
               note="La cola sin límite no pierde nada y deja todo inservible: en la saturación nadie recibe una respuesta a tiempo. Un límite obliga a decidir quién paga: el productor espera, se pierde lo nuevo o se pierde lo viejo. Llegadas y servicios exponenciales con semilla fija; los tiempos son del modelo, no de una máquina.",
               note_kind="coral", foot=SINT)


def se293_hilos() -> Fig:
    rows = [
        ["2 incrementos por hilo (esperado 4)", "sin protección", "70", "2: 32 · 3: 32 · 4: 6"],
        ["2 incrementos por hilo (esperado 4)", "operación atómica", "6", "4: 6"],
        ["Reservar el último cupo (esperado 1)", "sin protección", "6", "1: 2 · 2: 4"],
        ["Reservar el último cupo (esperado 1)", "operación atómica", "2", "1: 2"],
    ]
    return tab("Todas las intercalaciones de dos hilos sobre un dato compartido",
               "Tabla: al enumerar las 70 intercalaciones de dos hilos que incrementan un contador dos veces cada uno, solo 6 dan el resultado esperado, 4; con operación atómica las 6 dan 4; al reservar el último cupo sin protección, 4 de las 6 intercalaciones venden el cupo dos veces y con una operación atómica ninguna.",
               ["Programa", "Variante", "Intercalaciones", "Resultados (valor: cuántas)"], rows, [330, 180, 150, 240], row_h=44, size=13,
               note="Solo 6 de 70 intercalaciones salen bien, y una prueba corrida mil veces puede no ver nunca las malas: depende del planificador. Enumerar, o diseñar para que un solo hilo sea dueño del dato, convierte la sospecha en conteo. Modelo de pasos atómicos, sin hilos reales.",
               note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-294
def se294_umbrales() -> Fig:
    rows = [
        ["Largo mayor de 25 líneas", "5", "una es una plantilla de 217 líneas, 83 % datos"],
        ["Más de 5 parámetros", "7", "primitivas de dibujo con parámetros opcionales"],
        ["Anidamiento mayor de 3", "1", "el convertidor de Markdown a HTML"],
        ["Complejidad ciclomática mayor de 10", "3", "convertidor (39), página (14), diagrama (12)"],
        ["Señaladas por alguna regla", "12 de 65", "—"],
        ["Si el largo de datos no cuenta", "11 de 12", "la plantilla sale de la lista"],
    ]
    return tab("Umbrales de olores sobre 65 funciones del propio repositorio (commit 4dafaa63)",
               "Tabla: sobre 65 funciones de cuatro archivos de scripts del repositorio, la regla de largo señala 5, la de parámetros 7, la de anidamiento 1 y la de complejidad ciclomática 3; en total 12 funciones; una de las señaladas por largo es una plantilla de 217 líneas con 83 por ciento de datos, y al excluir el largo de datos quedan 11.",
               ["Regla", "Funciones señaladas", "Qué hay detrás"], rows, [330, 190, 380], row_h=44, size=12,
               note="Las tres funciones de mayor complejidad merecen leerse: tienen lógica. La de 217 líneas es mayoritariamente texto de una plantilla: señalarla por largo es una falsa alarma que enseña a ignorar la herramienta. Los umbrales son convenciones del autor y se midió en el estado del repositorio de ese commit.",
               note_kind="gold", foot=SINT)


def se294_duplicacion() -> Fig:
    rows = [
        ["0,9", "32,3", "12,0"],
        ["0,5", "18,0", "60,1"],
        ["0,1", "3,6", "108,0"],
    ]
    return tab("120 cambios sobre dos usos parecidos: divergencias por olvido frente a ramas añadidas",
               "Tabla: si el 90 por ciento de los cambios afecta a las dos copias, mantener dos copias produce 32,3 divergencias por olvido en 120 cambios y una función compartida añade 12,0 ramas; si solo el 10 por ciento afecta a ambas, las copias producen 3,6 divergencias y la función compartida añade 108,0 ramas.",
               ["Fracción de cambios que afecta a ambos usos", "Dos copias: divergencias por olvido", "Función compartida: ramas añadidas"], rows, [380, 270, 270], row_h=52, size=13,
               note="La duplicación es un problema cuando los usos cambian por la misma razón; unirlos cuando cambian por razones distintas compra ramas y parámetros. No decide el parecido del texto sino la razón de cambio. Supuestos: olvido del 30 % en cada cambio común y una rama por cada cambio de un solo uso.",
               note_kind="teal", foot=SINT)


def se294_envidia() -> Fig:
    rows = [
        ["Recibo.texto", "0", "6", "señala", "problema"],
        ["Política.aplica", "0", "3", "señala", "problema"],
        ["Etiqueta.línea", "0", "4", "señala", "problema"],
        ["Serializador.a_dict", "0", "4", "señala", "legítimo"],
        ["Visitante.visita_envio", "3", "2", "—", "legítimo"],
        ["Pedido.total", "3", "0", "—", "legítimo"],
        ["Calculadora.costo", "1", "1", "—", "legítimo"],
        ["Cuenta.saldo_neto", "2", "0", "—", "legítimo"],
    ]
    return tab("Envidia de características en 8 métodos: detector frente a criterio del autor",
               "Tabla: un detector que señala los métodos con tres o más accesos a otro objeto y más que a sí mismo acierta tres de los cuatro métodos a los que el autor les ve un problema y da una falsa alarma con un serializador, que es legítimo; no deja pasar ningún problema de los ocho.",
               ["Método", "Accesos propios", "Accesos ajenos", "Detector", "Autor"], rows, [260, 170, 170, 150, 150], row_h=36, size=12,
               note="Tres verdaderos positivos, una falsa alarma y cuatro verdaderos negativos: el serializador accede a los campos de otro objeto por oficio. Que el método sea problema depende de si moverlo mejoraría el diseño: lo decide una persona con el contexto. Ocho métodos y etiquetas del autor.",
               note_kind="gold", foot=SINT)


FIGURES = {
    "se-289-cohesion-lcom4.svg": se289_lcom,
    "se-289-sitios-de-edicion.svg": se289_sitios,
    "se-289-primer-ciclo-de-dependencias.svg": se289_ciclos,
    "se-290-anadir-reglas-sin-modificar.svg": se290_reglas,
    "se-290-violaciones-de-liskov.svg": se290_liskov,
    "se-290-interfaz-ancha-e-indireccion.svg": se290_interfaces,
    "se-291-clase-base-fragil.svg": se291_base,
    "se-291-orden-de-decoradores.svg": se291_decoradores,
    "se-291-herencia-multiple-al-azar.svg": se291_mro,
    "se-292-singleton-y-orden-de-pruebas.svg": se292_singleton,
    "se-292-aislamiento-de-observadores.svg": se292_observadores,
    "se-292-patrones-con-la-misma-estructura.svg": se292_estructura,
    "se-293-deteccion-de-impureza.svg": se293_impureza,
    "se-293-contrapresion.svg": se293_cola,
    "se-293-intercalaciones-de-dos-hilos.svg": se293_hilos,
    "se-294-umbrales-sobre-codigo-real.svg": se294_umbrales,
    "se-294-duplicacion-frente-a-parametros.svg": se294_duplicacion,
    "se-294-envidia-de-caracteristicas.svg": se294_envidia,
}
