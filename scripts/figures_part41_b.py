"""Figures for SE-499 to SE-504 (harness and agentic engineering: gates, real Git merges, seeded simulations, injected faults and a governed mini-harness; Windows 11, CPython 3.12.9, Git 2.55; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab
from figures_part40_a import bars, flow

EJEC = "Código ejecutado de verdad en Windows 11 con CPython 3.12.9; ninguna cifra viene de un modelo de lenguaje."
SIM = "Simulación con semilla fija (parámetros del autor) ejecutada en Windows 11 con CPython 3.12.9; no mide ningún modelo real."


# ---------------------------------------------------------------- SE-499
def se499_cambios() -> Fig:
    rows = [['Error de sintaxis', 'sintaxis, estilo y pruebas', 'sí'], ['Importación sin usar', 'estilo', 'no'], ['Secreto literal', 'secretos', 'no'],
            ['Error de lógica que una prueba ve', 'pruebas', 'sí'], ['Prueba debilitada para ocultar el error', 'no debilitar pruebas', 'no'],
            ['Prueba omitida con un decorador', 'no debilitar pruebas', 'no'], ['Error que ninguna prueba ve', 'ninguna', 'no'],
            ['Prueba que replica el error', 'ninguna', 'no']]
    return tab('Qué compuerta atrapa cada defecto de 11 y qué atrapan las pruebas por sí solas',
               'Tabla con ocho de once cambios defectuosos: el error de sintaxis lo atrapan tres compuertas incluidas las pruebas; la importación sin usar, el secreto literal, la prueba debilitada y la prueba omitida solo las compuertas especializadas; el error de lógica que una prueba ve lo atrapan las pruebas; el error que ninguna prueba ve y la prueba que replica el error no los atrapa ninguna compuerta.',
               ['Cambio defectuoso', 'Compuerta que lo atrapa', '¿Lo atrapan solo las pruebas?'], rows, [380, 330, 230], row_h=44, size=13,
               note='El menú completo atrapa 9 de 11 defectos; las pruebas solas, 2. Los 2 restantes (un error que ninguna prueba ejerce y una prueba que replica el error) no los atrapa ninguna compuerta: son el límite del gate.',
               note_kind='coral', foot=EJEC)


def se499_por_compuerta() -> Fig:
    return bars('Defectos atrapados por cada compuerta del menú único (de 11)',
                'Gráfico de barras con los defectos atrapados de once por compuerta: sintaxis 1, estilo 5, secretos 1, pruebas 2, no debilitar pruebas 2; el menú completo atrapa 9.',
                [('Sintaxis', 1, 'plain', '1'), ('Estilo', 5, 'teal', '5'), ('Secretos', 1, 'plain', '1'), ('Pruebas', 2, 'gold', '2'), ('No debilitar pruebas', 2, 'gold', '2'), ('Menú completo', 9, 'navy', '9')],
                scale=40, note='Las compuertas baratas atrapan más defectos que la costosa: las pruebas tardan cientos de milisegundos; la sintaxis, el estilo y los secretos, unos pocos. Orden: lo barato primero.',
                note_kind='gold', foot=EJEC, label_w=330)


def se499_menu() -> Fig:
    return flow('Un solo punto de entrada que ejecuta las compuertas de la más barata a la más cara',
                'Diagrama con dos filas: el agente y la persona invocan el mismo comando; el menú ejecuta sintaxis, estilo, secretos, pruebas y la comprobación de que no se debilitaron pruebas; al primer fallo se detiene e imprime el nombre de la compuerta y el motivo; el código de salida decide.',
                [[('Mismo comando para agente y persona', 'gold'), ('Sintaxis, estilo y secretos', 'teal'), ('Pruebas y no debilitar pruebas', 'teal')],
                 [('Primer fallo detiene y nombra la compuerta', 'coral'), ('Código de salida decide', 'navy'), ('Misma compuerta en integración continua', 'plain')]],
                note='Un menú único elimina que cada quien corra una parte. La compuerta que corre en la integración continua debe ser exactamente la que corre el agente antes de entregar.',
                note_kind='gold', foot=EJEC, box_h=76)


# ---------------------------------------------------------------- SE-500
def se500_fusiones() -> Fig:
    rows = [['Archivos distintos', 'limpia', 'pasan'], ['Mismo archivo, zonas lejanas', 'limpia', 'pasan'], ['Mismas líneas', 'conflicto', 'no aplica'],
            ['Renombrar una función y usarla por otro lado', 'limpia', 'FALLAN']]
    return tab('Dos agentes en ramas de Git reales: lo que dice la fusión y lo que dicen las pruebas',
               'Tabla con cuatro escenarios de dos ramas de Git creadas en directorios temporales: archivos distintos y zonas lejanas del mismo archivo se fusionan limpios y las pruebas pasan; editar las mismas líneas produce un conflicto; renombrar una función en una rama y usarla desde otra se fusiona limpio y las pruebas fallan.',
               ['Escenario', 'Fusión de Git', 'Pruebas tras fusionar'], rows, [460, 220, 260], row_h=52, size=13,
               note='Que Git fusione sin conflicto no significa que el resultado funcione. El conflicto semántico solo lo ve una verificación posterior a la fusión, y el conflicto textual es el caso fácil.',
               note_kind='coral', foot=EJEC)


def se500_solapamiento() -> Fig:
    return bars('Probabilidad de que dos agentes toquen algún archivo común, con 40 archivos y 3 por tarea',
                'Gráfico de barras con la probabilidad de algún archivo compartido: 2 agentes 21,3 por ciento, 3 agentes 53,0, 4 agentes 79,9, 6 agentes 98,4 y 8 agentes 100.',
                [('2 agentes', 21.3, 'teal', '21,3 %'), ('3 agentes', 53.0, 'gold', '53,0 %'), ('4 agentes', 79.9, 'coral', '79,9 %'), ('6 agentes', 98.4, 'coral', '98,4 %'), ('8 agentes', 100.0, 'coral', '100 %')],
                scale=7.5, note='Los canales entre pares crecen como n(n-1)/2: 1, 3, 6, 15 y 28. Con un coordinador crecen como n. Más agentes en el mismo árbol compran paralelismo y pagan colisión.',
                note_kind='gold', foot=SIM, label_w=250)


def se500_roles() -> Fig:
    return flow('Coordinación mínima: propiedad de archivos, aislamiento por rama y un único integrador',
                'Diagrama con dos filas: un coordinador divide la tarea por propiedad de archivos; cada agente trabaja en su propia rama con su árbol de trabajo; un integrador fusiona de una en una y ejecuta la verificación completa después de cada fusión.',
                [[('Coordinador divide por propiedad de archivos', 'gold'), ('Cada agente en su rama y su árbol', 'teal'), ('Entrega con rastro y pruebas', 'plain')],
                 [('Un integrador fusiona de una en una', 'navy'), ('Verificación completa tras cada fusión', 'teal'), ('Conflicto: vuelve al coordinador', 'coral')]],
                note='La separación por rama evita pisarse; la verificación posterior a la fusión detecta lo que Git no ve. Falta decidir quién resuelve un conflicto, y esa decisión es de una persona o de un solo agente designado.',
                note_kind='gold', foot=EJEC, box_h=76)


# ---------------------------------------------------------------- SE-501
def se501_trazas() -> Fig:
    rows = [['Completo', '30', '0', '6 de 6', '5,0'], ['Sin contexto', '72', '0', '0 de 6', '—'], ['Escritura denegada', '36', '12', '0 de 6', '—'], ['Sin criterio de parada', '72', '0', '6 de 6', '12,0']]
    return tab('Métricas calculadas desde las trazas de cuatro configuraciones del harness mínimo',
               'Tabla con las métricas de las trazas de cuatro configuraciones sobre seis tareas: el harness completo usa 30 pasos, ninguna denegación, resuelve 6 de 6 con 5,0 pasos por tarea resuelta; sin contexto usa 72 pasos y resuelve 0; con la escritura denegada usa 36 pasos con 12 denegaciones y resuelve 0; sin criterio de parada usa 72 pasos y resuelve 6 de 6 con 12,0 pasos por tarea.',
               ['Configuración', 'Pasos totales', 'Denegaciones', 'Resueltas', 'Pasos por tarea resuelta'], rows, [300, 160, 170, 150, 160], row_h=48, size=13,
               note='Las dos configuraciones que gastan 72 pasos fallan por razones opuestas: una no resuelve nada y la otra lo resuelve todo sin parar. Solo la combinación de pasos, denegaciones y resultado las distingue.',
               note_kind='gold', foot=EJEC)


def se501_potencia() -> Fig:
    return bars('Probabilidad de detectar una mejora real de 6 puntos según el número de tareas',
                'Gráfico de barras con la probabilidad de detectar con una prueba pareada una mejora real de 6 puntos del harness: con 50 tareas 9,7 por ciento, con 200 tareas 24,5 y con 800 tareas 75,9.',
                [('50 tareas', 9.7, 'coral', '9,7 %'), ('200 tareas', 24.5, 'gold', '24,5 %'), ('800 tareas', 75.9, 'teal', '75,9 %')],
                scale=11, note='Con 50 tareas una mejora real de 6 puntos se detecta una vez de diez. Una conclusión «sin diferencia» con pocas tareas no dice que no la haya.',
                note_kind='gold', foot=SIM, label_w=250)


def se501_falsos_positivos() -> Fig:
    rows = [['50', '45,7 %', '2,1 %'], ['200', '48,7 %', '3,0 %'], ['800', '47,1 %', '3,0 %']]
    return tab('Declarar mejor a un harness idéntico: la regla «tiene más aciertos» frente a una prueba pareada',
               'Tabla con la proporción de veces que se declara mejor a un harness idéntico a la línea base: con 50 tareas la regla de más aciertos lo declara mejor el 45,7 por ciento y la prueba pareada el 2,1; con 200 tareas 48,7 y 3,0; con 800 tareas 47,1 y 3,0.',
               ['Tareas', 'Regla «tiene más aciertos»', 'Prueba pareada'], rows, [200, 380, 360], row_h=52, size=13,
               note='Comparar contra un harness idéntico muestra el ruido: la regla ingenua da por mejor la mitad de las veces algo que no cambió. La prueba pareada mantiene el error cerca del 3 %, a costa de la potencia.',
               note_kind='coral', foot=SIM)


# ---------------------------------------------------------------- SE-502
def se502_clasificacion() -> Fig:
    rows = [['docs/guia.md', 'bajo'], ['src/a.py con su prueba (40 líneas)', 'bajo'], ['src/a.py sin prueba', 'medio'], ['src/a.py con prueba, 400 líneas', 'medio'],
            ['requirements.txt (dependencias)', 'medio'], ['.github/workflows/ci.yml', 'alto'], ['auth/login.py con su prueba', 'alto'], ['migrations/0004.sql', 'alto']]
    return tab('Clasificación de riesgo por reglas sobre rutas, tamaño y dependencias: ocho de doce cambios',
               'Tabla con ocho de doce cambios clasificados por reglas deterministas: la documentación y un cambio de código con su prueba y 40 líneas son de riesgo bajo; el código sin prueba, el cambio de 400 líneas y el archivo de dependencias son de riesgo medio; el workflow de integración continua, la autenticación y la migración son de riesgo alto.',
               ['Cambio', 'Nivel de riesgo'], rows, [650, 290], row_h=44, size=13,
               note='Una regla de rutas es barata, auditable y fácil de eludir: un cambio peligroso en una carpeta que no aparece en la lista es de riesgo bajo. Se complementa con revisión humana de las reglas.',
               note_kind='gold', foot=EJEC)


def se502_escapes() -> Fig:
    return bars('Defectos que escapan por cada 1000 cambios según el modo de trabajo (modelo del autor)',
                'Gráfico de barras con los defectos que escapan por cada mil cambios: sin controles 89, revisión humana de todo 38 con 271 horas, y compuertas más revisión por riesgo 22 con 201 horas.',
                [('Sin controles', 89, 'coral', '89 (0 h)'), ('Revisión humana de todo', 38, 'gold', '38 (271 h)'), ('Compuertas + revisión por riesgo', 22, 'teal', '22 (201 h)')],
                scale=4.2, note='Modelo paramétrico: tres niveles de riesgo con probabilidades de defecto del autor y compuertas que atrapan 60 % de los defectos. Sirve para razonar la forma del compromiso; ninguna cifra es una tasa real.',
                note_kind='coral', foot=SIM, label_w=330)


def se502_ciclo() -> Fig:
    return flow('Un ciclo de desarrollo asistido con compuertas humanas donde el riesgo lo pide',
                'Diagrama con dos filas: la intención y el alcance se acuerdan antes; el agente construye con compuertas automáticas; el cambio se clasifica por riesgo; el riesgo bajo pasa con las compuertas, el medio y el alto exigen revisión humana; todo queda con rastro y se mide el resultado en operación.',
                [[('Intención y alcance acordados', 'gold'), ('Construcción con compuertas automáticas', 'teal'), ('Clasificar por riesgo', 'navy')],
                 [('Bajo: pasa con las compuertas', 'plain'), ('Medio y alto: revisión humana', 'coral'), ('Rastro y medición en operación', 'teal')]],
                note='AI-DLC organiza el trabajo en Inception, Construction y Operations con puntos de aprobación humana. Aquí se muestra solo la idea común: la profundidad del control depende del riesgo.',
                note_kind='gold', foot=EJEC, box_h=76)


# ---------------------------------------------------------------- SE-503
def se503_fallos() -> Fig:
    rows = [['F1 sin contexto entre pasos', '6 de 6', '6 de 6'], ['F2 herramienta de escritura ausente', '0 de 6 (lo confunde con F1)', '6 de 6'],
            ['F3 la parada no se respeta', '6 de 6', '6 de 6'], ['F4 sin instrucción de verificar', '3 de 3', '3 de 3'],
            ['F5 escritura denegada por permiso', '6 de 6', '6 de 6'], ['F6 tope de pasos demasiado bajo', '3 de 3', '3 de 3']]
    return tab('Seis fallos inyectados en el harness y cuántas veces los acierta el diagnóstico desde la traza',
               'Tabla con seis fallos inyectados: con la traza mínima el diagnóstico acierta los fallos de contexto, parada, verificación, permiso y tope, y confunde siempre la herramienta ausente con la falta de contexto; con la traza enriquecida, que incluye las herramientas ofrecidas, el contexto visible y la observación, acierta los 30 casos.',
               ['Fallo inyectado', 'Traza mínima', 'Traza enriquecida'], rows, [400, 330, 210], row_h=48, size=13,
               note='Con la traza mínima el diagnóstico acierta 24 de 30; con la enriquecida, 30 de 30. La diferencia es un campo, las herramientas ofrecidas, que decide entre dos fallos con síntomas idénticos.',
               note_kind='gold', foot=EJEC)


def se503_aciertos() -> Fig:
    return bars('Diagnósticos correctos de 30 con cada versión de la traza',
                'Gráfico de barras con los diagnósticos correctos de treinta casos: la traza mínima acierta 24 y la traza enriquecida con herramientas ofrecidas, contexto visible y observación acierta 30.',
                [('Traza mínima', 24, 'gold', '24 de 30'), ('Traza enriquecida', 30, 'teal', '30 de 30')],
                scale=28, note='Los 6 casos que falla la traza mínima son un mismo fallo, no seis: se corrige con un solo campo. Un diagnóstico que acierta siempre en un conjunto inyectado no garantiza lo mismo ante fallos que no se inyectaron.',
                note_kind='coral', foot=EJEC, label_w=330)


def se503_procedimiento() -> Fig:
    return flow('Procedimiento de diagnóstico: de la traza al componente y de ahí a una prueba de regresión',
                'Diagrama con dos filas: reproducir la falla con la misma tarea y la misma configuración; leer la traza buscando repeticiones, denegaciones y herramientas ofrecidas; formular una hipótesis sobre un componente del harness; cambiar solo ese componente; volver a ejecutar y añadir el caso al conjunto de regresión.',
                [[('Reproducir con la misma configuración', 'plain'), ('Leer la traza: repeticiones y denegaciones', 'teal'), ('Hipótesis sobre un solo componente', 'gold')],
                 [('Cambiar solo ese componente', 'navy'), ('Ejecutar de nuevo y comparar', 'teal'), ('Añadir el caso a la regresión', 'plain')]],
                note='Cambiar dos componentes a la vez impide saber cuál arregló la falla. El diagnóstico es una hipótesis refutable, no una intuición.',
                note_kind='gold', foot=EJEC, box_h=76)


# ---------------------------------------------------------------- SE-504
def se504_escenarios() -> Fig:
    rows = [['Seis tareas normales', '6 de 6; 5,0 pasos', '6 de 6; 5,0 pasos'], ['A1 debilitar la prueba', 'prueba alterada; terminada en falso', 'bloqueado; para por falta de progreso'],
            ['A2 leer fuera de la raíz', 'lectura fuera de la raíz', 'bloqueado; para por falta de progreso'], ['A3 repetir el mismo intento', '12 pasos hasta el tope', 'para en 3 pasos'],
            ['A4 terminar sin verificar', 'terminada en falso', 'rechazada; para por falta de progreso']]
    return tab('Harness sin controles frente a harness gobernado: tareas normales y cuatro escenarios adversos',
               'Tabla con cinco escenarios: en las seis tareas normales ambos harness resuelven 6 de 6 con 5,0 pasos; sin controles, debilitar la prueba la altera y deja la tarea terminada en falso, leer fuera de la raíz tiene éxito, repetir el mismo intento gasta 12 pasos y terminar sin verificar queda terminada en falso; gobernado bloquea la prueba alterada y la lectura, para a los 3 pasos el intento repetido y rechaza la terminación sin verificar.',
               ['Escenario', 'Sin controles', 'Gobernado'], rows, [330, 310, 300], row_h=52, size=13,
               note='Los controles no cuestan nada en las tareas normales y cambian el resultado en las adversas. Los cuatro escenarios son del autor: demuestran que cada control hace su trabajo, no que cubran todos los casos.',
               note_kind='gold', foot=EJEC)


def se504_arquitectura() -> Fig:
    return flow('Arquitectura del harness mínimo gobernado: seis controles alrededor de un bucle',
                'Diagrama con dos filas: instrucciones y herramientas mínimas; permisos y confinamiento de rutas; protección de las pruebas; verificación obligatoria antes de aceptar la terminación; detección de falta de progreso y tope de pasos; traza y evaluación al final.',
                [[('Instrucciones y herramientas mínimas', 'gold'), ('Permisos y confinamiento de rutas', 'teal'), ('Pruebas protegidas contra escritura', 'teal')],
                 [('Verificación obligatoria antes de terminar', 'navy'), ('Falta de progreso y tope de pasos', 'coral'), ('Traza y evaluación al final', 'plain')]],
                note='Cada caja corresponde a una clase de la parte. El conjunto es pequeño y se puede leer entero; esa es su virtud.',
                note_kind='gold', foot=EJEC, box_h=76)


def se504_adversos() -> Fig:
    return bars('Escenarios adversos que el harness gobernado contiene, de cuatro',
                'Gráfico de barras con los escenarios adversos contenidos de cuatro: sin controles 1, que es el intento repetido que solo acota el tope, y harness gobernado 4.',
                [('Sin controles', 1, 'coral', '1 de 4'), ('Gobernado', 4, 'teal', '4 de 4')],
                scale=30, note='Sin controles, solo el tope de 12 pasos limitó un escenario. Contener los cuatro no prueba que el harness sea seguro: prueba que estos cuatro controles funcionan contra estos cuatro intentos.',
                note_kind='coral', foot=EJEC, label_w=250)


FIGURES = {
    "se-499-defectos-y-compuertas.svg": se499_cambios,
    "se-499-atrapados-por-compuerta.svg": se499_por_compuerta,
    "se-499-menu-unico.svg": se499_menu,
    "se-500-fusiones-de-git.svg": se500_fusiones,
    "se-500-solapamiento-de-agentes.svg": se500_solapamiento,
    "se-500-roles-de-coordinacion.svg": se500_roles,
    "se-501-metricas-de-trazas.svg": se501_trazas,
    "se-501-potencia-de-la-comparacion.svg": se501_potencia,
    "se-501-falsos-positivos.svg": se501_falsos_positivos,
    "se-502-clasificacion-de-riesgo.svg": se502_clasificacion,
    "se-502-defectos-que-escapan.svg": se502_escapes,
    "se-502-ciclo-con-compuertas.svg": se502_ciclo,
    "se-503-fallos-inyectados.svg": se503_fallos,
    "se-503-aciertos-del-diagnostico.svg": se503_aciertos,
    "se-503-procedimiento.svg": se503_procedimiento,
    "se-504-escenarios-adversos.svg": se504_escenarios,
    "se-504-arquitectura.svg": se504_arquitectura,
    "se-504-contencion.svg": se504_adversos,
}
