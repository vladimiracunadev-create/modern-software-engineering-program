"""Figures for SE-469 to SE-474 (SPEC, agents and agentic life cycle: synthetic data with fixed seeds, plus runs of real CPython/SQLite code on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3; no language model was invoked)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."

# ---------------------------------------------------------------- SE-469
def se469_vocabulario_vago() -> Fig:
    rows = [['Lista de palabras vagas', '50', '40', '10', '20'], ['Falta de medida o estado', '61', '56', '5', '4'], ['Palabra vaga y sin medida', '40', '40', '0', '20'], ['Palabra vaga o sin medida', '71', '56', '15', '4']]
    return tab('Cuatro detectores de vaguedad sobre 125 frases de requisitos: 60 vagas y 65 comprobables',
               'Tabla con cuatro detectores de vaguedad aplicados a 125 frases de requisitos, 60 vagas y 65 comprobables: la lista de palabras marca 50 y halla 40 con 10 falsas alarmas, la falta de medida marca 61 y halla 56 con 5 falsas alarmas, la combinación de ambas señales con y marca 40 sin falsas alarmas y deja pasar 20 vagas, y con o marca 71 con 15 falsas alarmas y deja pasar 4.',
               ['Detector', 'Marca', 'Vagas halladas', 'Falsas alarmas', 'Vagas que pasan'], rows, [340, 110, 170, 150, 150], row_h=44, size=13,
               note='Ninguno gana en todo: exigir las dos señales elimina las falsas alarmas y deja pasar 20 frases vagas; exigir una u otra deja pasar 4 a cambio de 15 falsas alarmas. Las frases y los detectores fueron escritos por el autor sabiendo qué buscan.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-469
def se469_espacio_de_interpretaciones() -> Fig:
    rows = [['0', '864', '184', '0 de 200'], ['2', '144', '107', '1 de 200'], ['4', '36', '36', '5 de 200'], ['6', '6', '6', '53 de 200'], ['8', '1', '1', '200 de 200']]
    return tab('Ocho decisiones abiertas de dos o tres lecturas: comportamientos posibles y observados en 200 implementaciones',
               'Tabla con una especificación de ocho decisiones abiertas de dos o tres lecturas cada una: con 0 decisiones resueltas hay 864 comportamientos posibles, 184 distintos en 200 implementaciones y ninguna coincide con la intención; con 2 hay 144 y 107 y una coincide; con 4 hay 36 y 36 y cinco coinciden; con 6 hay 6 y 6 y 53 coinciden; con 8 hay 1 y las 200 coinciden.',
               ['Decisiones resueltas', 'Comportamientos posibles', 'Distintos en 200 implementaciones', 'Coinciden con la intención'], rows, [210, 230, 270, 210], row_h=44, size=13,
               note='Cada decisión resuelta divide el espacio por su número de lecturas. Con las ocho abiertas, ninguna de 200 implementaciones coincide con la intención. El modelo supone decisiones independientes y lecturas igual de probables.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-469
def se469_trazabilidad_y_vacias() -> Fig:
    rows = [['Requisito sin prueba', '3', 'sí', '—'], ['Prueba huérfana', '2', 'sí', '—'], ['Identificador repetido', '1', 'sí', '—'], ['Requisito sin criterio', '2', 'sí', '—'], ['Prueba sin aserción', '3', 'no', 'sí'], ['Prueba que afirma algo irrelevante', '1', 'no', 'no'], ['Total encontrado', '12', '8', '11']]
    return tab('Doce defectos inyectados entre 25 entradas de especificación y 24 pruebas: qué comprobación encuentra cada uno',
               'Tabla con la comprobación automática de una especificación de 25 entradas y 24 pruebas con 12 defectos inyectados: la comprobación de identificadores y criterios encuentra 8, el recorrido del árbol sintáctico añade las 3 pruebas sin aserción y llega a 11, y queda sin ver una prueba que cita el requisito RF-02 pero afirma que dos más dos son cuatro.',
               ['Defecto inyectado', 'Cuántos', 'Identificadores y criterios', 'Árbol sintáctico'], rows, [390, 110, 230, 190], row_h=40, size=13,
               note='La comprobación formal encuentra 8 de 12 y el árbol sintáctico llega a 11. Queda sin ver una prueba con forma correcta que comprueba otra cosa. Los defectos los inyectó el autor y la comprobación se escribió para encontrarlos.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-470
def se470_incoherencias_entre_artefactos() -> Fig:
    rows = [['Requisito sin tarea', '3'], ['Identificador de tarea duplicado', '1'], ['Tarea con requisito inexistente', '1'], ['Tarea sin requisito', '1'], ['Plan que viola la constitución', '2'], ['Plan que cita un requisito inexistente', '1'], ['Conflicto numérico entre decisiones (24 frente a 48 horas)', '1'], ['Dependencia de una tarea posterior', '3'], ['Ciclo de dependencias', '1'], ['Tareas en paralelo sobre el mismo archivo', '1'], ['Código planificado antes de su prueba', '3'], ['Total', '18']]
    return tab('Hallazgos de un analizador de texto sobre constitución, plan y tareas con incoherencias inyectadas',
               'Tabla con los 18 hallazgos de un analizador de texto sobre tres artefactos de un servicio de avisos: tres requisitos sin tarea, un identificador de tarea duplicado, una tarea con requisito inexistente, una tarea sin requisito, dos decisiones del plan que violan la constitución, una que cita un requisito inexistente, un conflicto numérico entre 24 y 48 horas, tres dependencias hacia tareas posteriores, un ciclo, una pareja de tareas paralelas sobre el mismo archivo y tres tareas de código antes de su prueba.',
               ['Tipo de hallazgo', 'Cuántos'], rows, [700, 160], row_h=36, size=13,
               note='El analizador emite 18 hallazgos; 17 son incoherencias reales y uno es discutible. No ve dos problemas inyectados que exigen entender el significado: un canal distinto entre requisito y plan y un requisito sin mecanismo.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-470
def se470_presupuesto_de_preguntas() -> Fig:
    rows = [['0', '100,0 %', '100,0 %', '100,0 %', '100,0 %'], ['3', '78,7 %', '78,5 %', '46,4 %', '45,8 %'], ['5', '64,3 %', '64,5 %', '29,8 %', '29,3 %'], ['8', '42,8 %', '43,1 %', '14,0 %', '13,6 %'], ['14', '0,0 %', '0,0 %', '0,0 %', '0,0 %']]
    return tab('Fracción del costo esperado de 14 ambigüedades que queda sin resolver según el número de preguntas (2 000 especificaciones)',
               'Tabla con la fracción del costo esperado de catorce ambigüedades que queda sin resolver según el número de preguntas de clarificación y la estrategia en 2000 especificaciones: con cinco preguntas el orden del documento deja 64,3 por ciento, el azar 64,5, el mayor impacto 29,8 y el mayor costo esperado 29,3.',
               ['Preguntas', 'Orden del documento', 'Al azar', 'Mayor impacto', 'Mayor costo esperado'], rows, [150, 230, 150, 190, 200], row_h=44, size=13,
               note='El orden del documento rinde igual que el azar: no contiene información sobre cuánto importa cada ambigüedad. Ordenar por impacto o por costo esperado reduce a menos de la mitad lo que queda con cinco preguntas. Los impactos son supuestos del autor.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-470
def se470_tareas_y_ruta_critica() -> Fig:
    rows = [['1 trabajador', '52,3', '100,0 %'], ['2 trabajadores', '27,6', '52,7 %'], ['4 trabajadores', '14,4', '27,5 %'], ['8 trabajadores', '10,8', '20,6 %'], ['Ruta crítica (mínimo con cualquier número)', '10,4', '19,9 %'], ['Dependencias violadas en el orden del archivo', '8 de 53', '—']]
    return tab('Cuarenta tareas con 53 dependencias: duración con distinto número de trabajadores y orden del archivo',
               'Tabla con la duración de 40 tareas con 53 dependencias según el número de trabajadores: 52,3 con uno, 27,6 con dos, 14,4 con cuatro y 10,8 con ocho, con una ruta crítica de 10,4 y siete olas de hasta 13 tareas; si se ejecutan en el orden del archivo desordenado dentro de cada fase, 8 de 53 dependencias se violan.',
               ['Medida', 'Valor', 'Fracción del trabajo total'], rows, [470, 190, 260], row_h=40, size=13,
               note='La ruta crítica es un suelo: ocho trabajadores ya están a un 4 % de ella. Si el agente ejecuta las tareas en un orden de archivo desordenado dentro de cada fase, 8 de 53 dependencias se violan. Duraciones y dependencias son sintéticas.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-471
def se471_bucle_y_regresion() -> Fig:
    rows = [['0 %', '3', '5', '0,0 %', '0,00'], ['2 %', '5', '10', '9,4 %', '0,17'], ['5 %', '10', '10', '62,4 %', '1,84'], ['10 %', '10', '10', '96,3 %', '4,88']]
    return tab('Bucle implementar y converger con 40 criterios y 20 abiertos: pasadas según la tasa de regresión (5 000 corridas por fila)',
               'Tabla con la simulación de un bucle de implementar y converger sobre 40 criterios con 20 abiertos y una probabilidad de corrección de 0,7 por pasada: sin regresión la mediana es de 3 pasadas y ninguna corrida topa el máximo de 10; con 2 por ciento de regresión la mediana es de 5 y topa el 9,4 por ciento; con 5 por ciento la mediana es 10 y topa el 62,4; con 10 por ciento topa el 96,3 con 4,88 criterios abiertos de media.',
               ['Regresión por pasada', 'Pasadas (mediana)', 'Percentil 90', 'Topan el máximo de 10', 'Abiertos al parar (media)'], rows, [210, 190, 150, 210, 160], row_h=48, size=13,
               note='Una regresión del 5 % por pasada deja sin converger al 62,4 % de las corridas: de 20 criterios cumplidos, uno se rompe en cada pasada. La tasa de corrección de 0,7 y la independencia entre criterios son supuestos del autor.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-471
def se471_verificador_parcial() -> Fig:
    rows = [['100 %', '90,7 %', '0,0 %', '0,0'], ['80 %', '94,5 %', '93,7 %', '4,4'], ['50 %', '98,9 %', '98,9 %', '10,7'], ['30 %', '99,9 %', '99,9 %', '14,8']]
    return tab('Declaración de convergencia de un agente según la cobertura de su verificador (40 criterios, 5 000 corridas)',
               'Tabla con la declaración de convergencia de un agente según la cobertura de su verificador sobre 40 criterios: con cobertura del 100 por ciento declara el 90,7 por ciento de las corridas y ninguna con criterios abiertos; con el 80 por ciento declara el 94,5 y el 93,7 lo hace con criterios abiertos, 4,4 de media; con el 50 por ciento declara el 98,9 con 10,7 abiertos; con el 30 declara el 99,9 con 14,8.',
               ['Cobertura del verificador', 'Declara convergido', 'Con criterios aún abiertos', 'Abiertos reales al declarar'], rows, [250, 230, 250, 190], row_h=44, size=13,
               note='Cuanto peor es el verificador, antes declara convergencia, porque tiene menos que corregir. Los criterios que no ve nunca se corrigen. La columna del medio es la fracción de todas las corridas que declaran con criterios abiertos.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-471
def se471_criterios_y_variantes() -> Fig:
    rows = [['Camino feliz', '3', '3 de 10', 'ignora entregada, ignora silencio, repite, envía todos, avisa tras vencer, elige el más lejano, solo bloquea el idéntico'], ['Camino feliz y bordes', '9', '6 de 10', 'ignora entregada, ignora silencio, envía todos, elige el más lejano'], ['Criterios completos', '17', '10 de 10', 'ninguna']]
    return tab('Tres conjuntos de criterios ejecutables frente a diez variantes defectuosas de la regla de avisos',
               'Tabla con tres conjuntos de criterios ejecutables aplicados a diez variantes defectuosas de la regla de avisos: tres casos del camino feliz detectan 3 de 10, nueve casos con bordes detectan 6 de 10 y quedan vivas las que ignoran entregada, ignoran el silencio, envían todos los umbrales y eligen el más lejano, y diecisiete casos completos detectan las 10.',
               ['Conjunto de criterios', 'Casos', 'Detectadas', 'Variantes vivas'], rows, [230, 90, 130, 470], row_h=64, size=12,
               note='Las variantes que sobreviven al segundo conjunto dependen de combinaciones de estado que un caso de borde de un solo valor no ejercita. Las diez variantes y los 17 casos son del autor: el 10 de 10 es consecuencia de haberlos escrito sabiéndolo.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-472
def se472_leer_un_repositorio_ajeno() -> Fig:
    rows = [['Leer todo', '300', '1 004,0', '5 de 5'], ['Buscar el nombre y leer los que lo contienen', '4', '11,8', '4 de 5'], ['Buscar el nombre y el módulo que lo define', '9', '27,2', '5 de 5'], ['Mapa de arquitectura vigente y sus módulos', '5', '15,3', '5 de 5'], ['Mapa de hace un trimestre (sin el módulo dinámico)', '4', '11,8', '4 de 5']]
    return tab('Cinco estrategias para encontrar los usos de una función en un repositorio sintético de 300 módulos y 1 004 KB',
               'Tabla con cinco estrategias para encontrar los usos de una función en un repositorio sintético de 300 módulos y 1004 kilobytes: leer todo lee 300 módulos y encuentra 5 de 5, buscar el nombre lee 4 módulos y 11,8 kilobytes y encuentra 4, buscar el nombre y el módulo que la define lee 9 módulos y 27,2 kilobytes y encuentra 5, un mapa vigente lee 5 módulos y encuentra 5 y un mapa desactualizado lee 4 y encuentra 4.',
               ['Estrategia', 'Módulos leídos', 'KB leídos', 'Cambios hallados'], rows, [470, 150, 130, 170], row_h=44, size=13,
               note='La búsqueda por nombre cuesta el 1,2 % de la lectura total y no ve el uso por cadena de texto. Un mapa vale lo que valga su mantenimiento. El repositorio es sintético, con módulos pequeños y un solo uso dinámico.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-472
def se472_verificar_una_correccion() -> Fig:
    rows = [['Solo la batería existente', '5 de 5', '5 de 5', '3 de 5', '5 de 5'], ['Solo la reproducción', '0 de 5', '5 de 5', '5 de 5', '5 de 5'], ['Batería y reproducción', '0 de 5', '5 de 5', '3 de 5', '5 de 5'], ['Batería, reproducción y casos vecinos', '0 de 5', '0 de 5', '1 de 5', '5 de 5']]
    return tab('Cinco errores y cuatro candidatos de arreglo: cuántos acepta cada política de verificación',
               'Tabla con cuatro políticas de verificación aplicadas a cuatro candidatos de arreglo de cinco errores: la batería existente acepta el código sin corregir en 5 de 5 casos; la reproducción lo rechaza pero acepta el arreglo del síntoma en 5; batería y reproducción rechazan dos arreglos que rompen otro caso y aceptan 5 del síntoma; con casos vecinos solo se aceptan los arreglos de la causa, más uno que rompe otro caso.',
               ['Política de verificación', 'Sin corregir', 'Arregla el síntoma', 'Arregla y rompe otro caso', 'Arregla la causa'], rows, [330, 130, 160, 190, 130], row_h=48, size=13,
               note='La batería existente acepta el código sin corregir en los cinco casos: por eso el error existía. Solo los casos vecinos rechazan el arreglo del síntoma. Los errores, las baterías y los arreglos son del autor.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-472
def se472_cuando_evaluar_una_idea() -> Fig:
    rows = [['5 %', '−8,12', '−2,18', '0,00', 'no construir'], ['10 %', '−6,21', '−0,84', '0,00', 'no construir'], ['25 %', '−0,19', '3,38', '0,00', 'evaluar'], ['50 %', '9,68', '10,33', '0,00', 'evaluar'], ['75 %', '19,74', '17,29', '0,00', 'construir todo']]
    return tab('Valor esperado de tres políticas según la proporción de ideas buenas (construir 10, valor 40, evaluar 1)',
               'Tabla con el valor esperado de tres políticas para ideas cuyo costo de construir es 10, su valor 40 si es buena y 0 si no, y cuyo costo de evaluar es 1: con 5 por ciento de ideas buenas construir todo da menos 8,12, evaluar y construir si procede menos 2,18 y no construir 0; con 25 por ciento evaluar da 3,38 frente a menos 0,19; con 50 por ciento 10,33 frente a 9,68; con 75 por ciento construir todo da 19,74 frente a 17,29.',
               ['Ideas buenas', 'Construir todo', 'Evaluar y construir si procede', 'No construir', 'Mejor opción'], rows, [160, 190, 270, 150, 190], row_h=44, size=13,
               note='Evaluar compensa en un rango intermedio: con pocas ideas buenas conviene no construir y con casi todas buenas, construir sin evaluar. Los valores y la señal de evaluación son supuestos del autor.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-473
def se473_reglas_de_permiso() -> Fig:
    rows = [['Permitirlo todo', '16 de 16', '0 de 16', '0 de 14'], ['Lista por prefijo', '13 de 16', '3 de 16', '1 de 14'], ['Lista con análisis de segmentos', '4 de 16', '12 de 16', '1 de 14'], ['Segmentos y confinamiento de rutas', '0 de 16', '16 de 16', '0 de 14']]
    return tab('Cuatro políticas de permisos frente a 30 órdenes de shell (16 peligrosas y 14 inocuas), sin ejecutar ninguna',
               'Tabla con cuatro políticas de permisos aplicadas a 30 órdenes de shell, 16 peligrosas y 14 inocuas: permitirlo todo deja pasar las 16 peligrosas; la lista por prefijo deja pasar 13 y frena una inocua; el análisis de segmentos deja pasar 4, todas lecturas fuera del espacio de trabajo, y frena una inocua; los segmentos con confinamiento de rutas frenan las 16 y ninguna inocua.',
               ['Política', 'Peligrosas permitidas', 'Peligrosas frenadas', 'Inocuas frenadas'], rows, [360, 190, 190, 170], row_h=44, size=13,
               note='El prefijo deja pasar las órdenes compuestas; el análisis de segmentos deja pasar cuatro lecturas fuera del espacio de trabajo. Las treinta órdenes se escribieron sabiendo qué reglas las evaluarían: el cero de la última fila es mérito de la construcción.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-473
def se473_radio_de_dano() -> Fig:
    rows = [['Todas las herramientas, alcance completo', '41,6 %', '0,53'], ['Solo las herramientas de la tarea (6)', '21,3 %', '0,24'], ['…y escritura confinada al espacio de trabajo', '3,2 %', '0,03'], ['…y lo destructivo exige aprobación humana', '0,0 %', '0,00']]
    return tab('Sesiones de 20 acciones con un 5 % de desvíos y 12 herramientas: sesiones con algún daño según la configuración (5 000 sesiones)',
               'Tabla con la fracción de sesiones con algún daño en 5000 sesiones de 20 acciones con un 5 por ciento de desvíos y doce herramientas: con todas las herramientas y alcance completo 41,6 por ciento y 0,53 acciones dañinas por sesión; con solo las seis de la tarea 21,3 y 0,24; con escritura confinada 3,2 y 0,03; con aprobación humana para lo destructivo 0,0 y 0,00.',
               ['Configuración', 'Sesiones con algún daño', 'Acciones dañinas por sesión'], rows, [500, 230, 190], row_h=44, size=13,
               note='Cada restricción reduce el daño por una razón distinta y se acumulan. El cero de la última fila supone una aprobación humana perfecta, la suposición más débil. El 5 % de desvíos y la elección uniforme de herramienta son del autor.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-473
def se473_reglas_que_se_acumulan() -> Fig:
    rows = [['Nunca se revisan', '57', '20', '100 %'], ['Se revisan cada 12 semanas', '38', '4', '98 %'], ['Se revisan cada 4 semanas', '13', '1', '75 %']]
    return tab('Reglas «permitir siempre» tras 24 semanas con 6 solicitudes semanales (500 equipos por fila)',
               'Tabla con la acumulación de reglas de permitir siempre durante 24 semanas en 500 equipos con 6 solicitudes por semana: sin revisión la mediana es de 57 reglas, 20 amplias, y todos los equipos tienen alguna amplia; con revisión cada 12 semanas 38 reglas y 4 amplias, 98 por ciento de equipos; con revisión cada 4 semanas 13 reglas y 1 amplia, 75 por ciento de equipos.',
               ['Política de revisión', 'Reglas (mediana)', 'Reglas amplias (mediana)', 'Equipos con alguna regla amplia'], rows, [330, 170, 220, 200], row_h=44, size=13,
               note='Sin revisión se acumulan 57 reglas y todos los equipos tienen alguna amplia; revisar cada cuatro semanas mantiene el conjunto acotado sin eliminar el problema. El 40 % de aprobaciones permanentes y el 35 % de reglas amplias son supuestos del autor.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-474
def se474_gancho_y_modo_de_fallo() -> Fig:
    rows = [['Éxito (código 0)', '40 eventos'], ['Bloqueo (código 2)', '12 eventos'], ['Error (otro código)', '4 eventos'], ['Tiempo agotado', '2 eventos'], ['Peligrosas ejecutadas si solo el código 2 bloquea', '6 de 18'], ['Peligrosas ejecutadas si todo lo que no sea éxito bloquea', '0 de 18']]
    return tab('Un gancho de política ejecutado como proceso sobre 58 eventos (18 peligrosos): salidas y modo de fallo',
               'Tabla con 58 eventos ejecutados como procesos reales contra un gancho de política: 40 salen con éxito, 12 con bloqueo, 4 con error y 2 con tiempo agotado; si solo el código 2 bloquea, 6 de las 18 acciones peligrosas se ejecutan; si todo lo que no sea éxito bloquea, ninguna de las 18 se ejecuta y ninguna acción inocua se bloquea.',
               ['Medida', 'Resultado'], rows, [640, 230], row_h=40, size=13,
               note='El diseño por defecto de estos controles falla abierto: una caída o un tiempo agotado no bloquean. El gancho imita un contrato documentado, no es la herramienta; el arranque de un proceso cuesta decenas de milisegundos y cambia de equipo en equipo.',
               note_kind='coral', foot=REAL)

# ---------------------------------------------------------------- SE-474
def se474_cargar_habilidades() -> Fig:
    rows = [['Frases de activación: correcta · incorrecta · sin activar', '45 · 15 · 0'], ['Descripción genérica: correcta · incorrecta · sin activar', '29 · 15 · 16'], ['Cargar los 40 cuerpos al arrancar', '30 496 tokens'], ['Cargar solo las 40 descripciones', '778 tokens'], ['Descripciones y un cuerpo cargado (media)', '1 541 tokens']]
    return tab('Cuarenta habilidades y cien peticiones: selección según el estilo de descripción y costo de contexto de tres formas de cargar',
               'Tabla con 40 habilidades y 100 peticiones: con descripciones con frases de activación la selección activa la correcta en 45 de 60 y una incorrecta en 15 sin dejar ninguna sin activar; con descripciones genéricas activa la correcta en 29, una incorrecta en 15 y no activa 16; cargar los 40 cuerpos cuesta unos 30496 tokens, las 40 descripciones 778 y las descripciones más un cuerpo 1541.',
               ['Qué se mide', 'Resultado'], rows, [640, 230], row_h=40, size=13,
               note='Una buena descripción previene la falta de activación; el solape entre habilidades, que da las 15 activaciones incorrectas, es un defecto del conjunto. El selector es una coincidencia de palabras clave y los textos son sintéticos.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-474
def se474_confinar_rutas() -> Fig:
    rows = [['Comparar el prefijo de texto', '3 de 12', '7 de 10'], ['Prefijo con separador, sin normalizar', '7 de 12', '1 de 10'], ['Normalizar y luego comparar', '1 de 12', '0 de 10'], ['Normalizar, rechazar el byte nulo y comparar', '0 de 12', '0 de 10']]
    return tab('Cuatro comprobaciones de confinamiento al directorio de trabajo sobre 22 intentos (10 legítimos y 12 de escape)',
               'Tabla con cuatro comprobaciones de confinamiento de rutas sobre 22 intentos, 10 legítimos y 12 de escape: comparar el prefijo de texto deja pasar 3 escapes y rechaza 7 legítimos; el prefijo con separador sin normalizar deja pasar 7 y rechaza 1; normalizar deja pasar 1, el byte nulo, y no rechaza ninguno; normalizar y rechazar el byte nulo deja pasar 0 y no rechaza ninguno.',
               ['Comprobación', 'Escapes que pasan', 'Legítimos rechazados'], rows, [480, 220, 220], row_h=44, size=13,
               note='La barra invertida cambia de significado entre sistemas: queda dentro con las reglas de POSIX y fuera con las de Windows. Los enlaces simbólicos no se probaron. Pasar esta batería no demuestra que la comprobación sea correcta.',
               note_kind='gold', foot=EJEC)


FIGURES = {
    "se-469-vocabulario-vago.svg": se469_vocabulario_vago,
    "se-469-espacio-de-interpretaciones.svg": se469_espacio_de_interpretaciones,
    "se-469-trazabilidad-y-vacias.svg": se469_trazabilidad_y_vacias,
    "se-470-incoherencias-entre-artefactos.svg": se470_incoherencias_entre_artefactos,
    "se-470-presupuesto-de-preguntas.svg": se470_presupuesto_de_preguntas,
    "se-470-tareas-y-ruta-critica.svg": se470_tareas_y_ruta_critica,
    "se-471-bucle-y-regresion.svg": se471_bucle_y_regresion,
    "se-471-verificador-parcial.svg": se471_verificador_parcial,
    "se-471-criterios-y-variantes.svg": se471_criterios_y_variantes,
    "se-472-leer-un-repositorio-ajeno.svg": se472_leer_un_repositorio_ajeno,
    "se-472-verificar-una-correccion.svg": se472_verificar_una_correccion,
    "se-472-cuando-evaluar-una-idea.svg": se472_cuando_evaluar_una_idea,
    "se-473-reglas-de-permiso.svg": se473_reglas_de_permiso,
    "se-473-radio-de-dano.svg": se473_radio_de_dano,
    "se-473-reglas-que-se-acumulan.svg": se473_reglas_que_se_acumulan,
    "se-474-gancho-y-modo-de-fallo.svg": se474_gancho_y_modo_de_fallo,
    "se-474-cargar-habilidades.svg": se474_cargar_habilidades,
    "se-474-confinar-rutas.svg": se474_confinar_rutas,
}
