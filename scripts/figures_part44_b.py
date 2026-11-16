"""Figures for SE-535 to SE-540 (architectural styles: runs of real CPython code and seeded models over the Avisos case; Windows CPython 3.12.9; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab
from figures_part40_a import bars, flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9; los recuentos se repiten y los tiempos varían de un equipo a otro."
MODELO = "Modelo con parámetros del autor y semilla fija 44; muestra un mecanismo, no mide un sistema real."


# ---------------------------------------------------------------- SE-535
def se535_cola_central() -> Fig:
    rows = [['5', '19 %', '0,00', '0,00', '0,00'], ['10', '38 %', '0,03', '0,03', '0,00'], ['15', '56 %', '0,14', '0,14', '0,50'],
            ['20', '75 %', '0,53', '0,51', '1,66'], ['24', '90 %', '2,17', '1,97', '5,65']]
    return tab('Un equipo de datos central de cuatro personas atendiendo a D dominios: espera por solicitud de un conjunto de datos nuevo',
               'Tabla con un equipo central de cuatro personas que atiende solicitudes de D dominios, cada uno con 0,15 solicitudes por semana: con 5 dominios la utilización es 19 por ciento y la espera media 0,00 semanas, con 10 es 38 por ciento y 0,03, con 15 es 56 por ciento y 0,14, con 20 es 75 por ciento y 0,53 y con 24 es 90 por ciento y 2,17 semanas; la espera analítica de Erlang C coincide dentro del ruido y el percentil 90 llega a 5,65 semanas con 24 dominios.',
               ['Dominios', 'Utilización', 'Espera media simulada (semanas)', 'Espera media analítica', 'Espera p90 simulada'], rows, [150, 170, 280, 200, 180], row_h=56, size=13,
               note='La espera no crece en línea recta: pasar de 20 a 24 dominios (un 20 % más de demanda) multiplica la espera media por cuatro. La simulación coincide con la fórmula de Erlang C hasta el 90 % de utilización, lo que valida la simulación, no el modelo de organización.',
               note_kind='coral', foot=MODELO)


def se535_personas_necesarias() -> Fig:
    rows = [['Equipo central, sin penalización de contexto', '5 personas', '0,12'], ['Equipo central, penalización 0,5', '6 personas', '0,44'],
            ['Equipo central, penalización 1,0', '8 personas', '0,38'], ['Un equipo por dominio, 0,5 persona cada uno', '10 personas', '0,87'],
            ['Un equipo por dominio, 0,65 persona cada uno', '13 personas', '0,47']]
    return tab('Con 20 dominios, personas necesarias para que la espera media no pase de 0,5 semanas según quién es dueño del dato',
               'Tabla con las personas necesarias con 20 dominios para que la espera media no pase de 0,5 semanas: un equipo central necesita 5 personas sin penalización de contexto, 6 con penalización 0,5 y 8 con penalización 1,0, y unos equipos por dominio necesitan 10 personas en total con 0,5 persona por dominio, con una espera de 0,87 que no cumple, y 13 con 0,65 persona por dominio.',
               ['Modelo de propiedad', 'Personas en total', 'Espera media (semanas)'], rows, [460, 240, 260], row_h=58, size=13,
               note='En este modelo la propiedad por dominio no ahorra personas: mueve el trabajo y necesita más. Lo que compra es que el conocimiento del dominio deje de ser una penalización del equipo central y que el producto de datos tenga un dueño. La penalización de contexto es un supuesto del autor.',
               note_kind='gold', foot=MODELO)


def se535_derivas() -> Fig:
    rows = [['D1 columna renombrada', 'esquema', 'sí'], ['D2 tipo cambiado a texto', 'esquema', 'sí'], ['D3 columna eliminada', 'esquema', 'sí'],
            ['D4 nulos en estudiante (12,5 %)', 'esquema y completitud', 'sí'], ['D5 identificadores duplicados', 'unicidad', 'sí'], ['D6 datos atrasados (30 h)', 'frescura', 'sí'],
            ['D7 unidad cambiada a minutos', 'distribución', 'sí'], ['D8 significado invertido', 'distribución', 'sí'], ['L1 cambio legítimo de temporada', 'distribución', 'falsa alarma']]
    return tab('Ocho derivas de un producto de datos y un cambio legítimo: qué comprobación del contrato las detecta',
               'Tabla con nueve cambios sobre un producto de datos de 1 000 filas: las derivas D1 a D3 las detecta la comprobación de esquema, D4 la completitud y el esquema, D5 la unicidad, D6 la frescura y D7 y D8 la comprobación de distribución; el cambio legítimo de temporada L1 también falla la distribución y es una falsa alarma; solo con el esquema se detectan 4 de las 8 derivas.',
               ['Cambio', 'Comprobaciones que fallan', 'Resultado'], rows, [430, 330, 200], row_h=44, size=13,
               note='Las ocho derivas se detectan con cinco comprobaciones; con solo el esquema se detectarían 4. La unidad cambiada y el significado invertido son válidos para el esquema y solo se ven por su efecto en la distribución, que no distingue un defecto de un cambio real del negocio.',
               note_kind='teal', foot=EJEC)


# ---------------------------------------------------------------- SE-536
def se536_reubicacion() -> Fig:
    rows = [['Módulo del hash (h mod n)', '88 985', '89,0 %'], ['Hash por encuentro (rendezvous)', '11 176', '11,2 %'], ['Mínimo teórico (1/9)', '11 111', '11,1 %']]
    return tab('Pasar de 8 a 9 celdas con 100 000 inquilinos: cuántos cambian de celda según la función de asignación',
               'Tabla con tres funciones de asignación al pasar de 8 a 9 celdas con 100 000 inquilinos: el módulo del hash reubica 88 985 inquilinos, un 89,0 por ciento, el hash por encuentro reubica 11 176, un 11,2 por ciento, y el mínimo teórico es un noveno, 11,1 por ciento.',
               ['Función de asignación', 'Inquilinos reubicados', 'Proporción'], rows, [430, 280, 250], row_h=58, size=13,
               note='Con el módulo, añadir una celda mueve casi todo; con el hash por encuentro solo se mueve lo que la celda nueva se queda. Mover un inquilino es una migración de datos, de modo que la función de asignación decide el costo de crecer. El reparto entre las 8 celdas fue de 12 339 a 12 713 inquilinos por celda.',
               note_kind='gold', foot=EJEC)


def se536_radio() -> Fig:
    return bars('Fracción de los 1 000 inquilinos que un solo inquilino venenoso deja sin servicio según cómo está repartida la flota',
                'Gráfico de barras con la fracción de inquilinos afectada por un inquilino venenoso: en una flota compartida el 100 por ciento según el supuesto de reintentos, con ocho celdas el 10,9 por ciento, con fragmentación aleatoria de dos trabajadores de ocho el 3,0 por ciento queda caído del todo y el 45,6 por ciento queda degradado.',
                [('Flota compartida (supuesto)', 100, 'coral', '100 %'), ('Ocho celdas', 10.9, 'gold', '10,9 %'), ('Fragmentación: caídos del todo', 3.0, 'teal', '3,0 %'),
                 ('Fragmentación: degradados', 45.6, 'gold', '45,6 %')],
                scale=4, label_w=330,
                note='Las celdas acotan el daño a una fracción fija y la fragmentación lo reduce aún más a quien comparte todos sus trabajadores con el venenoso, a costa de degradar a casi la mitad. El 100 % de la flota compartida es un supuesto (los reintentos del cliente recorren todos los trabajadores), no una medición.',
                note_kind='teal', foot=MODELO)


def se536_costo_de_celdas() -> Fig:
    rows = [['Capacidad para cubrir el p99 de la carga', '1 824 unidades', '2 184 unidades (19,8 % más)'], ['Disponibilidad de un inquilino', '99,9 % de la flota', '99,890 % (enrutador por celda)'],
            ['Punto de fallo compartido', 'La flota entera', 'El enrutador']]
    return tab('Costo de repartir 1 000 inquilinos en 8 celdas frente a una flota compartida: capacidad, disponibilidad y punto de fallo',
               'Tabla con tres comparaciones entre una flota compartida y ocho celdas: la capacidad para cubrir el percentil 99 de la carga es 1 824 unidades frente a 2 184, un 19,8 por ciento más, la disponibilidad de un inquilino es la de la flota frente a 99,890 por ciento con el enrutador al 99,99 y la celda al 99,9, y el punto de fallo compartido es la flota entera frente al enrutador.',
               ['Comparación', 'Flota compartida', 'Ocho celdas'], rows, [370, 280, 310], row_h=62, size=13,
               note='Repartir cuesta capacidad (cada celda se dimensiona a su propio p99, y los picos no se compensan entre celdas) y mueve el punto de fallo al enrutador. La carga de cada inquilino es lognormal con semilla 44; una carga real tiene otra forma.',
               note_kind='coral', foot=MODELO)


# ---------------------------------------------------------------- SE-537
def se537_linter() -> Fig:
    rows = [['URL fija en el código', '1', '0'], ['Estado en memoria del proceso', '2', '0'], ['Registro en archivo local', '1', '0'], ['Lecturas del entorno', '1', '2']]
    return tab('Un linter de cuatro señales de 12-factor sobre una aplicación con defectos y su versión corregida',
               'Tabla con cuatro señales contadas por un linter de árbol sintáctico sobre dos versiones de la misma aplicación: URL fija 1 y 0, estado en memoria del proceso 2 y 0, registro en archivo local 1 y 0, y lecturas del entorno 1 y 2 en la versión corregida.',
               ['Señal', 'Aplicación con defectos', 'Aplicación corregida'], rows, [400, 280, 280], row_h=56, size=13,
               note='El linter ve la forma del código, no su comportamiento: una URL construida por concatenación o un estado guardado en un atributo de clase pasarían. Detecta cuatro señales de dos aplicaciones de juguete; no certifica que una aplicación sea 12-factor.',
               note_kind='gold', foot=EJEC)


def se537_sesiones() -> Fig:
    return bars('Peticiones sin sesión de 1 000 con tres instancias, 100 usuarios y una instancia que cae en la petición 500',
                'Gráfico de barras con las peticiones que no encuentran su sesión de 1 000: con sesiones en memoria y balanceo sin afinidad 611, con afinidad por usuario 140 que corresponden a la instancia caída, y con un almacén externo compartido 0.',
                [('En memoria, sin afinidad', 611, 'coral', '611'), ('En memoria, con afinidad', 140, 'gold', '140'), ('Almacén externo', 0, 'teal', '0')],
                scale=0.6, label_w=300,
                note='Una aplicación con estado en el proceso no puede escalar horizontalmente ni sobrevivir a una caída: sin afinidad falla en 611 de 1 000 peticiones aun sin caída; con afinidad pierde las sesiones de la instancia que cae. El estado externo lo resuelve a costa de una dependencia más, que el modelo no cuenta.',
                note_kind='coral', foot=MODELO)


def se537_desechabilidad() -> Fig:
    rows = [['Corte inmediato con 100 trabajos', '40 completados, 60 perdidos'], ['Drenaje ordenado, devuelve lo pendiente', '41 completados, 60 devueltos a la cola, 0 perdidos'],
            ['Mismo artefacto, configuración de desarrollo', 'Código 0 y umbrales 12 y 48'], ['Mismo artefacto, configuración de producción', 'Código 0 y umbrales 1, 24 y 72'],
            ['Mismo artefacto, sin configurar', 'Código 1: «falta AVISOS_UMBRALES»'], ['Arranque de un proceso Python (mediana)', '116 ms vacío; 249 ms con cuatro módulos']]
    return tab('Desechabilidad y configuración: qué pasa al parar un proceso, y un mismo artefacto con tres entornos',
               'Tabla con seis comprobaciones: un corte inmediato con 100 trabajos en una cola en memoria completa 40 y pierde 60, un drenaje ordenado completa 41 y devuelve 60 a la cola sin perder ninguno, el mismo artefacto con configuración de desarrollo sale con código 0, con configuración de producción sale con código 0 y otros umbrales y sin configurar sale con código 1 y un mensaje, y el arranque de un proceso de Python tarda una mediana de 116 milisegundos vacío y 249 con cuatro módulos.',
               ['Comprobación', 'Resultado'], rows, [470, 490], row_h=58, size=13,
               note='La misma huella del archivo con configuración distinta es la paridad que pide el factor de configuración; fallar de inmediato cuando falta es mejor que arrancar con un valor por defecto invisible. Los trabajos y el corte son un modelo; el arranque y la ejecución del artefacto sí se midieron.',
               note_kind='teal', foot=EJEC)


# ---------------------------------------------------------------- SE-538
def se538_divergencias() -> Fig:
    rows = [['Redondeo en el borde (el módulo nuevo trunca minutos)', '145', '71,4 %'], ['Plazo de extensión (el módulo nuevo lo olvidó)', '57', '28,1 %'],
            ['Cambio de hora (solo 2 días al año)', '1', '0,5 %'], ['Total de divergencias en 20 000 peticiones', '203', '1,01 %']]
    return tab('Módulo heredado y módulo nuevo ejecutados sobre las mismas 20 000 peticiones: divergencias por causa',
               'Tabla con las divergencias entre un módulo de avisos heredado y su reemplazo sobre 20 000 peticiones sintéticas: 145 por redondeo en el borde, 57 por el plazo de extensión que el módulo nuevo olvidó y 1 por cambio de hora, 203 en total, un 1,01 por ciento.',
               ['Causa', 'Divergencias', 'Proporción'], rows, [560, 200, 200], row_h=58, size=13,
               note='Tres defectos sembrados por el autor, con frecuencias tan distintas como 145, 57 y 1. Ejecutar los dos módulos en paralelo y comparar las salidas es la forma más barata de encontrar lo que ninguna prueba imaginó, pero solo encuentra lo que el tráfico real contiene.',
               note_kind='gold', foot=MODELO)


def se538_modo_sombra() -> Fig:
    rows = [['1 %', '46 %', '1 %', '75 %'], ['5 %', '95 %', '6 %', '100 %'], ['25 %', '100 %', '27 %', '100 %'], ['100 %', '100 %', '100 %', '100 %']]
    return tab('Probabilidad de ver cada causa de divergencia según la fracción del tráfico que se compara (500 repeticiones por fila)',
               'Tabla con la probabilidad de observar cada divergencia según la fracción del tráfico comparada en modo sombra: con 1 por ciento se ve el plazo de extensión el 46 por ciento de las veces, el cambio de hora el 1 por ciento y el redondeo el 75 por ciento; con 5 por ciento 95, 6 y 100; con 25 por ciento 100, 27 y 100; con todo el tráfico se ven los tres siempre.',
               ['Fracción comparada', 'Plazo de extensión', 'Cambio de hora', 'Redondeo en el borde'], rows, [230, 250, 230, 250], row_h=56, size=13,
               note='Un defecto que ocurre una vez en 20 000 peticiones no se ve comparando el 1 % ni el 25 % del tráfico con fiabilidad: su probabilidad es la fracción comparada. Comparar todo es la única forma de ver lo raro, y aun así solo si ocurre durante la comparación.',
               note_kind='coral', foot=MODELO)


def se538_escalones() -> Fig:
    rows = [['1 %', '0,8', '4,7 %'], ['5 %', '4,0', '76,2 %'], ['25 %', '20,0', '100,0 %'], ['50 %', '40,0', '100,0 %'], ['100 %', '80,0', '100,0 %']]
    return tab('Un defecto visible en 0,4 % de las peticiones con 20 000 peticiones por escalón: usuarios afectados y probabilidad de detectarlo',
               'Tabla con cinco escalones de tráfico para un defecto que afecta al 0,4 por ciento de las peticiones: con 1 por ciento hay 0,8 afectados esperados y 4,7 por ciento de probabilidad de ver al menos 3 errores, con 5 por ciento hay 4,0 y 76,2 por ciento, con 25 por ciento hay 20,0 y 100 por ciento, con 50 por ciento 40,0 y con 100 por ciento 80,0.',
               ['Escalón de tráfico', 'Usuarios afectados esperados', 'Probabilidad de ver al menos 3 errores'], rows, [270, 330, 360], row_h=56, size=13,
               note='Un escalón demasiado pequeño no detecta y uno demasiado grande daña: con 1 % no se alcanza a ver el defecto (4,7 %) y con 5 % se ve tres de cada cuatro veces afectando a unos 4 usuarios. Si el 5 % lo detiene, el daño acumulado es de 4,8 usuarios frente a 80 si se cambia de golpe.',
               note_kind='teal', foot=MODELO)


# ---------------------------------------------------------------- SE-539
def se539_escenarios() -> Fig:
    rows = [['S1 latencia', 'p99 ≤ 200 ms', 'Alta', 'Alta'], ['S2 disponibilidad', '≥ 99,9 %', 'Alta', 'Alta'], ['S3 radio de impacto', '≤ 15 % de inquilinos', 'Alta', 'Baja'],
            ['S4 coordinación de despliegue', '≤ 2 equipos', 'Media', 'Media'], ['S5 costo', '≤ 12 unidades', 'Media', 'Media'], ['S6 extensión', 'canal nuevo sin tocar el núcleo', 'Media', 'Media']]
    return tab('Seis escenarios de calidad de Avisos con su medida y su importancia en dos contextos',
               'Tabla con seis escenarios de calidad con su medida y su importancia en dos contextos: latencia con p99 de hasta 200 milisegundos y disponibilidad de al menos 99,9 por ciento son de importancia alta en ambos, el radio de impacto de hasta 15 por ciento de los inquilinos es alta con un cliente dominante y baja sin él, y la coordinación de despliegue, el costo y la extensión son de importancia media en ambos.',
               ['Escenario', 'Medida de respuesta', 'Con cliente dominante', 'Sin cliente dominante'], rows, [320, 330, 160, 160], row_h=56, size=13,
               note='Cada escenario tiene una medida que se puede comprobar; la importancia es una decisión de negocio, no una medición. El único escenario que cambia de importancia entre los dos contextos es el radio de impacto, y eso es suficiente para cambiar el resultado.',
               note_kind='gold', foot=MODELO)


def se539_candidatos() -> Fig:
    rows = [['Monolito modular', '80', '99,950 %', '11', '3', '0,596', '0,685'], ['Microservicios (4)', '194', '99,601 %', '0', '16', '0,583', '0,670'],
            ['Celdas (8) con monolito modular', '125', '99,890 %', '11', '18', '0,710', '0,652']]
    return tab('Tres candidatos con 12 equipos: valores que produce el modelo y utilidad ponderada en cada contexto',
               'Tabla con tres candidatos evaluados con 12 equipos: el monolito modular tiene p99 de 80 milisegundos, disponibilidad de 99,950 por ciento, 11 equipos a coordinar, costo 3 y utilidad 0,596 con cliente dominante y 0,685 sin él; los microservicios 194, 99,601, 0, 16, 0,583 y 0,670; las celdas con monolito modular 125, 99,890, 11, 18, 0,710 y 0,652.',
               ['Candidato', 'p99 (ms)', 'Disponibilidad', 'Equipos', 'Costo', 'Con cliente', 'Sin cliente'], rows, [290, 100, 150, 100, 90, 120, 120], row_h=66, size=13,
               note='Ningún candidato cumple los seis escenarios y los tres dejan tres o cuatro sin cumplir; las utilidades difieren en menos de 0,13. Con cliente dominante ganan las celdas y sin él el monolito modular; la decisión depende del contexto antes que del estilo.',
               note_kind='teal', foot=MODELO)


def se539_sensibilidad() -> Fig:
    rows = [['Con cliente dominante', 'Celdas', 'Celdas', 'Celdas'], ['Sin cliente dominante', 'Monolito modular', 'Monolito modular', 'Microservicios (desde 26)'],
            ['Con cliente dominante y cadena al 99,95 %', 'Microservicios', 'Microservicios', 'Microservicios'], ['Sin cliente dominante y cadena al 99,95 %', 'Microservicios', 'Microservicios', 'Microservicios']]
    return tab('Qué candidato gana según el contexto, el número de equipos y la disponibilidad supuesta de la cadena de microservicios',
               'Tabla con el candidato de mayor utilidad según el contexto y el número de equipos: con cliente dominante ganan las celdas con 4, 12 y 30 equipos, sin cliente dominante gana el monolito modular con 4 y 12 equipos y los microservicios desde 26, y si la disponibilidad de la cadena de microservicios fuese 99,95 por ciento en lugar de 99,601 ganan los microservicios en ambos contextos con cualquier número de equipos.',
               ['Situación', '4 equipos', '12 equipos', '30 equipos'], rows, [380, 190, 190, 200], row_h=62, size=13,
               note='El punto de sensibilidad más fuerte no es el número de equipos sino un supuesto: que la cadena de cuatro servicios tenga 99,601 % de disponibilidad. Cambiarlo a 99,95 % (con degradación y reintentos) invierte la decisión en todos los casos, y por eso esa medida debe ir al ADR como supuesto a verificar.',
               note_kind='coral', foot=MODELO)


# ---------------------------------------------------------------- SE-540
def se540_lint_de_adr() -> Fig:
    names = ['Sección Contexto', 'Sección Decisión', 'Sección Alternativas', 'Sección Consecuencias', 'Sección Reversibilidad', 'Sección Disparador de revisión',
             'Sección Evidencia', 'Al menos 2 alternativas con motivo', 'Consecuencia negativa declarada', 'Criterio medible', 'Disparador numérico']
    a = ['sí'] * 11
    b = ['sí', 'sí', 'NO', 'sí', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']
    c = ['sí', 'sí', 'sí', 'sí', 'NO', 'NO', 'sí', 'sí', 'sí', 'sí', 'NO']
    rows = [[n, x, y, z] for n, x, y, z in zip(names, a, b, c)]
    rows.append(['Criterios cumplidos', '11 de 11', '3 de 11', '8 de 11'])
    return tab('Un linter de once criterios sobre tres ADR: el completo, el que justifica con una moda y el que olvida su reversibilidad',
               'Tabla con once criterios aplicados a tres registros de decisión: el ADR-A, monolito modular con disparador de revisión, cumple 11 de 11; el ADR-B, que dice usar microservicios porque son la mejor práctica, cumple 3 de 11 y le faltan alternativas, reversibilidad, disparador, evidencia, consecuencias negativas y criterio medible; el ADR-C, celdas para el cliente grande, cumple 8 de 11 y le faltan la reversibilidad, el disparador de revisión y su criterio numérico.',
               ['Criterio', 'ADR-A', 'ADR-B', 'ADR-C'], rows, [440, 170, 170, 170], row_h=44, size=13,
               note='El linter comprueba presencia y forma, no verdad: un ADR con once criterios cumplidos puede decidir mal. Sirve para rechazar lo evidentemente incompleto (el ADR-B) antes de gastar tiempo de revisión humana.',
               note_kind='gold', foot=EJEC)


def se540_funcion_de_aptitud() -> Fig:
    rows = [['Limpia', '0', '0', 'Pasa'], ['El dominio importa la infraestructura', '1', '1', 'Falla'], ['Dos módulos de aplicación se importan entre sí', '0', '1', 'Falla'],
            ['Importación dinámica de la infraestructura', '0', '0', 'Pasa (no la ve)']]
    return tab('Una función de aptitud de capas sobre un paquete de juguete: violaciones y ciclos que detecta en cuatro variantes',
               'Tabla con una prueba de arquitectura basada en el árbol sintáctico sobre cuatro variantes de un paquete: la limpia no tiene violaciones ni ciclos y pasa, cuando el dominio importa la infraestructura hay 1 violación de capa y 1 ciclo y falla, cuando dos módulos de aplicación se importan entre sí hay 0 violaciones y 1 ciclo y falla, y una importación dinámica de la infraestructura no se detecta y pasa.',
               ['Variante del paquete', 'Violaciones de capa', 'Ciclos', 'Resultado'], rows, [430, 180, 130, 220], row_h=62, size=13,
               note='La prueba corre en unos 10 a 40 ms y detecta lo que está escrito como importación; una importación por nombre en una cadena la elude. Una función de aptitud protege una decisión contra la deriva solo en la medida en que su mecanismo ve la forma en que se rompe.',
               note_kind='teal', foot=EJEC)


def se540_ciclo_de_decision() -> Fig:
    return flow('Ciclo de una decisión arquitectónica defendida: de los escenarios al disparador de revisión',
                'Diagrama de cinco cajas en dos filas: escenarios de calidad con medida, alternativas evaluadas con evidencia, ADR con consecuencias negativas, función de aptitud que protege la decisión y disparador de revisión numérico; una flecha de retorno lleva del disparador a los escenarios.',
                [[('Escenarios\nCon medida y contexto', 'teal'), ('Alternativas\nEvaluadas con evidencia y supuestos', 'gold'), ('ADR\nDecisión, costos y reversibilidad', 'teal')],
                 [('Función de aptitud\nProtege la decisión contra la deriva', 'coral'), ('Disparador de revisión\nUn número y un plazo', 'gold')]],
                note='Una decisión arquitectónica es una hipótesis con fecha de revisión: el disparador numérico (por ejemplo, p99 mayor que 200 ms durante 3 días seguidos) dice cuándo la evidencia obliga a volver a los escenarios.',
                note_kind='teal', box_h=96, foot=MODELO)


FIGURES = {
    "se-535-cola-central.svg": se535_cola_central,
    "se-535-personas-necesarias.svg": se535_personas_necesarias,
    "se-535-derivas.svg": se535_derivas,
    "se-536-reubicacion.svg": se536_reubicacion,
    "se-536-radio.svg": se536_radio,
    "se-536-costo-de-celdas.svg": se536_costo_de_celdas,
    "se-537-linter.svg": se537_linter,
    "se-537-sesiones.svg": se537_sesiones,
    "se-537-desechabilidad.svg": se537_desechabilidad,
    "se-538-divergencias.svg": se538_divergencias,
    "se-538-modo-sombra.svg": se538_modo_sombra,
    "se-538-escalones.svg": se538_escalones,
    "se-539-escenarios.svg": se539_escenarios,
    "se-539-candidatos.svg": se539_candidatos,
    "se-539-sensibilidad.svg": se539_sensibilidad,
    "se-540-lint-de-adr.svg": se540_lint_de_adr,
    "se-540-funcion-de-aptitud.svg": se540_funcion_de_aptitud,
    "se-540-ciclo-de-decision.svg": se540_ciclo_de_decision,
}
