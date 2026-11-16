"""Figures for SE-433 to SE-438 (modernization of a legacy grading module: synthetic data with fixed seeds, plus runs of real CPython/SQLite code on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."

# ---------------------------------------------------------------- SE-433
def se433_capacidad_devorada() -> Fig:
    rows = [['1', '19,7 · 30,0', '40,9', '19,7 · 30,0', '14,9'], ['12', '33,0 · 30,0', '184,0', '12,6 · 30,0', '0,0'], ['24', '59,7 · 25,3', '401,2', '14,0 · 30,0', '0,0']]
    return tab('Un equipo de 100 unidades al mes: lo correctivo se come lo demás si no hay reserva preventiva',
               'Tabla con la capacidad mensual de un equipo en los meses 1, 12 y 24 con y sin una reserva del 20 por ciento para trabajo preventivo: sin reserva el trabajo correctivo sube de 19,7 a 59,7 unidades y la deuda de 40,9 a 401,2; con reserva el correctivo baja a 14,0 y la deuda a cero.',
               ['Mes', 'Sin reserva: correctivo · perfectivo', 'Sin reserva: deuda', 'Reserva del 20 %: correctivo · perfectivo', 'Reserva del 20 %: deuda'], rows, [90, 250, 150, 280, 170], row_h=48, size=13,
               note='Sin reserva, la carga correctiva pasa de 19,7 a 59,7 unidades y desplaza al perfectivo; con el 20 % reservado, el correctivo baja a 14,0 y se entrega todo lo pedido. Los coeficientes de realimentación entre deuda e incidencias son del autor: demuestran un mecanismo, no una magnitud.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-433
def se433_clasificar_es_un_juicio() -> Fig:
    rows = [['Claras', '456', '456 (100 %)', '—'], ['Ambiguas', '144', '74 (51 %)', '34 %'], ['Todas', '600', '530 (88,3 %)', '76,8 % (kappa 0,69)']]
    return tab('600 solicitudes sintéticas: un clasificador por palabras clave y el acuerdo entre dos revisoras',
               'Tabla con 600 solicitudes sintéticas: un clasificador por palabras clave acierta las 456 claras y 74 de las 144 ambiguas, 88,3 por ciento en total, y dos revisoras simuladas coinciden en el 76,8 por ciento con kappa 0,69, pero solo en el 34 por ciento de las ambiguas.',
               ['Conjunto', 'Solicitudes', 'Aciertos del clasificador', 'Acuerdo entre dos revisoras'], rows, [160, 150, 300, 330], row_h=48, size=13,
               note='El acierto global del 88 % esconde que una cuarta parte de la cartera es ambigua y que ahí el acuerdo entre personas es del 34 %. Esas solicitudes necesitan una conversación con quien las pidió. La proporción de ambiguas y las tasas de las revisoras son supuestos del autor.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-433
def se433_fecha_impuesta() -> Fig:
    items = [('3 meses', 24.6, 'coral', '24,6 %'), ('4 meses (mediana)', 44.0, 'coral', '44,0 %'), ('6 meses', 71.6, 'gold', '71,6 %'), ('8 meses', 85.3, 'teal', '85,3 %'), ('12 meses', 95.6, 'teal', '95,6 %')]
    return bars('Probabilidad de terminar a tiempo una adaptación obligatoria de mediana cuatro meses, según el margen',
                'Barras con la probabilidad de terminar a tiempo una adaptación obligatoria cuya duración mediana es de cuatro meses según el margen disponible: 24,6 por ciento con tres meses, 44,0 con cuatro, 71,6 con seis, 85,3 con ocho y 95,6 con doce.',
                items, 6.0, 'Empezar con un margen igual a la mediana llega a tiempo menos de la mitad de las veces. La duración (mediana 4 meses, dispersión 0,5, 15 % de dependencias ocultas que la duplican) es un supuesto del autor.',
                label_w=190, width=940, note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-434
def se434_puntos_calientes() -> Fig:
    rows = [['Solo tamaño', '10,3 %', '23,5 %', '11 de 30'], ['Solo frecuencia de cambio', '55,9 %', '51,7 %', '19 de 30'], ['Frecuencia × tamaño', '53,3 %', '55,6 %', '22 de 30']]
    return tab('Tres criterios para elegir 30 de 300 archivos en un historial sintético de 4 000 commits',
               'Tabla con tres criterios para elegir los 30 archivos de 300 en un historial sintético de 4 000 commits: el tamaño captura 23,5 por ciento de las correcciones y coincide con 11 de los 30 más corregidos, la frecuencia de cambio 51,7 por ciento y 19, y el producto de ambas 55,6 por ciento y 22.',
               ['Criterio de ranking', 'Commits en los 30', 'Correcciones en los 30', 'Coincide con los 30 más corregidos'], rows, [270, 200, 220, 270], row_h=48, size=13,
               note='El 10 % de los archivos concentra más de la mitad de los commits y de las correcciones. Ordenar por tamaño apenas supera al azar; el producto captura el 55,6 % de las correcciones. La relación entre tamaño y correcciones es un supuesto del autor.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-434
def se434_conocimiento_que_se_va() -> Fig:
    rows = [['12 meses', '40', '90', '13 %'], ['36 meses', '132', '187', '44 %'], ['60 meses', '194', '249', '65 %']]
    return tab('Archivos huérfanos de 300 con 12 personas y una rotación del 2 % mensual (200 simulaciones)',
               'Tabla con la mediana y el percentil 90 de archivos huérfanos de 300 tras 12, 36 y 60 meses con una rotación del 2 por ciento mensual entre 12 personas: 40 y 90, 132 y 187, y 194 y 249.',
               ['Horizonte', 'Huérfanos (mediana)', 'Percentil 90', 'Fracción de los 300 (mediana)'], rows, [180, 250, 220, 310], row_h=48, size=13,
               note='Con una rotación del 2 % mensual se van 9 de las 12 personas en cinco años y dos tercios de los archivos quedan sin persona asociada. La rotación, el 35 % de archivos compartidos y la asignación al azar son supuestos del autor.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-434
def se434_codigo_muerto() -> Fig:
    rows = [['Análisis por nombre (ast)', '45', '20', '25: 15 por cadena y 10 registradas'], ['Traza de una ejecución', '25', '20', '5: rama poco frecuente'], ['Coinciden las dos', '20', '20', '0']]
    return tab('Dos técnicas para encontrar código muerto en un módulo de 60 funciones con 20 realmente muertas',
               'Tabla con dos técnicas de detección de código muerto sobre 60 funciones con 20 muertas: el análisis por nombre propone 45 candidatos con 25 falsas alarmas, la traza de una ejecución propone 25 con 5 falsas alarmas y la coincidencia de ambas propone exactamente las 20 muertas.',
               ['Técnica', 'Candidatos', 'Muertas halladas', 'Falsas alarmas'], rows, [300, 150, 200, 320], row_h=52, size=13,
               note='Cada técnica se equivoca por una razón distinta. La coincidencia deja cero falsas alarmas solo porque en este módulo ningún uso dinámico estaba en una rama poco frecuente; una llamada por cadena en esa rama habría engañado a las dos.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-435
def se435_cobertura_no_es_detector() -> Fig:
    rows = [['5 ejemplos de la documentación', '16 de 18 (89 %)', '4 de 12'], ['5 entradas aleatorias', '15 de 18 (83 %)', '6 de 12'], ['20 entradas aleatorias', '16 de 18 (89 %)', '9 de 12'], ['100 entradas aleatorias', '16 de 18 (89 %)', '9 de 12'], ['1 000 entradas aleatorias', '18 de 18 (100 %)', '12 de 12'], ['14 casos de borde elegidos a mano', '17 de 18 (94 %)', '9 de 12']]
    return tab('Entradas para caracterizar nota_final: líneas cubiertas (18) y mutantes detectados (12)',
               'Tabla con seis conjuntos de entradas para caracterizar una función de nota final con 18 líneas y 12 mutantes: los cinco ejemplos de la documentación cubren 16 líneas y detectan 4 mutantes, 100 entradas aleatorias cubren 16 y detectan 9, 1 000 cubren 18 y detectan 12, y 14 casos de borde cubren 17 y detectan 9.',
               ['Conjunto de entradas', 'Líneas cubiertas', 'Mutantes detectados'], rows, [400, 250, 250], row_h=40, size=13,
               note='La cobertura de líneas no sube entre 20 y 100 entradas y los mutantes tampoco; los casos de borde cubren el 94 % y dejan vivos tres mutantes que mil entradas aleatorias matan. La función y los doce mutantes son del autor y se escribieron sabiendo qué buscaban.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-435
def se435_orden_de_un_conjunto() -> Fig:
    rows = [['1', 'pedro,marta,sofia,tomas,luis,ana'], ['2', 'pedro,marta,tomas,ana,sofia,luis'], ['3', 'luis,pedro,tomas,sofia,ana,marta'], ['Las ocho', '8 salidas distintas'], ['Ordenando antes de escribir', '1 salida']]
    return tab('El mismo programa con seis alumnos en un conjunto, en ocho procesos con semilla de hash distinta',
               'Tabla con tres de las ocho salidas del mismo programa con seis alumnos ejecutado con semillas de hash 1, 2 y 3, todas distintas entre sí, y el resultado de ordenar antes de escribir: una sola salida para los ocho procesos.',
               ['Semilla de hash', 'Salida'], rows, [300, 600], row_h=40, size=13,
               note='Un maestro dorado que compare el texto completo falla entre procesos aunque el código sea idéntico. Ordenar elimina la variación solo si el contrato no exige otro orden. El orden de los conjuntos de cadenas depende del intérprete y de su versión.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-435
def se435_costura_y_tiempo() -> Fig:
    rows = [['Windows 11 (CPython 3.12.9)', '771 ms', '0,34 ms', 'unas 2 200 veces'], ['Ubuntu bajo WSL2 (3.12.3)', '701 ms', '0,40 ms', 'unas 1 800 veces']]
    return tab('300 pruebas de nota_final con una dependencia de 2 ms y con una costura que la sustituye',
               'Tabla con 300 pruebas de la función de nota final: con una dependencia de 2 milisegundos tarda 771 milisegundos en Windows y 701 en Ubuntu, y con una costura que sustituye la dependencia tarda 0,34 y 0,40 milisegundos, unas 2 200 y 1 800 veces menos.',
               ['Sistema', 'Con la dependencia', 'Con costura', 'Razón'], rows, [330, 220, 180, 190], row_h=48, size=13,
               note='La espera de 2 ms es un supuesto y los tiempos de reloj cambian de equipo en equipo; la razón de varios órdenes de magnitud es la parte estable. La costura no prueba la dependencia real: queda pendiente una prueba de integración.',
               note_kind='gold', foot=REAL)

# ---------------------------------------------------------------- SE-436
def se436_costo_de_esperar() -> Fig:
    rows = [['Cada versión', '12,6 h · 18,9 h', '2,1 h · 2,1 h'], ['Cada 4 versiones', '14,4 h · 23,0 h', '5,5 h · 5,5 h'], ['Cada 12 versiones', '21,1 h · 35,5 h', '12,5 h · 18,6 h'], ['Una vez a las 48', '71,4 h · 134,6 h', '71,4 h · 134,6 h']]
    return tab('Esfuerzo de actualizar una dependencia con 12 % de versiones incompatibles en 48 versiones (2 000 historias)',
               'Tabla con el esfuerzo de actualizar una dependencia con 12 por ciento de versiones con cambio incompatible en 48 versiones: cada versión cuesta 12,6 horas de mediana y 2,1 la mayor actualización, cada 4 versiones 14,4 y 5,5, cada 12 versiones 21,1 y 12,5, y una sola vez a las 48 versiones 71,4 y 71,4 horas.',
               ['Cadencia', 'Esfuerzo total (mediana · p90)', 'Mayor actualización (mediana · p90)'], rows, [230, 340, 360], row_h=44, size=13,
               note='El número de cambios incompatibles es el mismo en las cuatro cadencias; lo que cambia es cuántos se juntan en un salto. Actualizar una sola vez cuesta 5,7 veces más que en cada versión. El 12 %, el 15 % de interacción y el 5 % de mezcla de causas son supuestos del autor.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-436
def se436_ventana_de_exposicion() -> Fig:
    rows = [['Continua (7 días tras la corrección)', '22 días', '107 días'], ['Lote mensual', '29 días', '126 días'], ['Lote trimestral', '68 días', '156 días'], ['Lote anual', '224 días', '361 días']]
    return tab('Exposición a avisos de seguridad en 40 dependencias y 31 avisos durante un año, según la política',
               'Tabla con la exposición a avisos de seguridad en 40 dependencias y 31 avisos durante un año según la política de actualización: continua 22 días de mediana y 107 el percentil 95, lote mensual 29 y 126, trimestral 68 y 156, y anual 224 y 361 días.',
               ['Política', 'Exposición mediana', 'Percentil 95'], rows, [420, 250, 250], row_h=44, size=13,
               note='El lote anual deja un aviso expuesto diez veces más que la política continua. Aun la continua tiene un percentil 95 de 107 días por el retraso del proveedor, que no depende de ti. El ritmo de avisos y el retraso (mediana 14 días) son supuestos del autor.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-436
def se436_radio_de_impacto() -> Fig:
    rows = [['Hoja (0–1 dependientes)', '6 797', '0,0', '1', '20'], ['Intermedio (2–4)', '3 822', '3,0', '9', '39'], ['Concentrador (5 o más)', '1 381', '12,0', '27', '44']]
    return tab('Paquetes arrastrados al actualizar uno, en 200 grafos sintéticos de 60 paquetes',
               'Tabla con el radio de impacto de actualizar un paquete en 200 grafos sintéticos de 60 paquetes: una hoja arrastra 0 paquetes de mediana y hasta 20, un paquete intermedio 3 de mediana y hasta 39, y un concentrador con cinco o más dependientes 12 de mediana, 27 en el percentil 90 y hasta 44.',
               ['Tipo de paquete', 'Paquetes', 'Arrastrados (mediana)', 'Percentil 90', 'Máximo'], rows, [300, 150, 200, 150, 120], row_h=48, size=13,
               note='Actualizar un concentrador arrastra 12 paquetes de mediana y 27 en el percentil 90. Los grafos son aleatorios y el 60 % de dependientes que excluye la versión nueva es un supuesto; los grafos reales tienen pocos paquetes muy centrales.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-437
def se437_exposicion_por_estrategia() -> Fig:
    rows = [['Corte único', '20 000 · 35 000', '4,0', '4'], ['Escalonado al 5 %', '1 000 · 1 750', '4,0', '20'], ['Escalonado con sombra previa', '250 · 1 000', '4,0', '40']]
    return tab('Migrar 40 rutas con 100 000 peticiones diarias y 10 % de rutas con regresión (2 000 historias)',
               'Tabla con tres estrategias para migrar 40 rutas con 100 000 peticiones diarias y 10 por ciento de rutas con regresión: el corte único afecta 20 000 peticiones de mediana y 35 000 en el percentil 95 y tarda 4 semanas, el escalonado al 5 por ciento 1 000 y 1 750 en 20 semanas, y el escalonado con sombra previa 250 y 1 000 en 40 semanas.',
               ['Estrategia', 'Peticiones afectadas (mediana · p95)', 'Regresiones', 'Semanas'], rows, [300, 330, 150, 130], row_h=48, size=13,
               note='La regresión ocurre las mismas 4,0 veces; cambia cuántas peticiones alcanza. El escalonado reduce el daño 20 veces a cambio de 5 veces más duración. El 10 %, los dos días hasta decidir y el 60 % de eficacia de la sombra son supuestos del autor.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-437
def se437_sombra_y_clases_raras() -> Fig:
    rows = [['Detectar una diferencia del 1 % (95 %)', '299 peticiones; 96 % de 400 corridas la ven'], ['Detectar el 0,1 %', '2 995 peticiones; 94 %'], ['Detectar el 0,01 %', '29 956 peticiones; 94 %'], ['Ventana de 1 semana incluye un cierre', '7 % de los inicios posibles'], ['Ventana de 4 semanas', '21 %'], ['Ventana de 8 semanas', '31 %'], ['Ventana de 12 semanas', '43 %']]
    return tab('Comparación en sombra: tamaño de muestra por tasa y frecuencia con que una ventana incluye un cierre',
               'Tabla con el tamaño de muestra para detectar una diferencia en comparación en sombra, 299 peticiones para el uno por ciento, 2 995 para el 0,1 y 29 956 para el 0,01, y con la frecuencia con que una ventana de 1, 4, 8 o 12 semanas incluye una de las cuatro semanas de cierre del año: 7, 21, 31 y 43 por ciento.',
               ['Pregunta', 'Resultado'], rows, [470, 450], row_h=40, size=13,
               note='El tamaño de muestra crece como 3 dividido por la tasa; pero una clase de tráfico que solo aparece en 4 de 52 semanas exige elegir la ventana por calendario. El calendario de cierres es un supuesto del autor.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-437
def se437_traduccion_anticorrupcion() -> Fig:
    rows = [['Traducción ingenua: lanza excepción', '4 402 (88,0 %)'], ['Capa anticorrupción: sin errores', '2 175'], ['Capa: con error de nota', '642'], ['Capa: con error de fecha', '2 491'], ['Estado «desconocido» (vacío, nulo o X)', '2 429'], ['Estado espacio y nulo, antes distintos, ahora iguales', '1 606']]
    return tab('5 000 registros sintéticos del modelo antiguo: traducción ingenua frente a una capa anticorrupción',
               'Tabla con 5 000 registros sintéticos del modelo antiguo: una traducción ingenua lanza excepción con 4 402, una capa anticorrupción no lanza ninguna y deja 2 175 registros sin errores, 642 con error de nota y 2 491 con error de fecha, y 1 606 registros con estado espacio o nulo se vuelven indistinguibles.',
               ['Resultado', 'Registros'], rows, [640, 280], row_h=40, size=13,
               note='La capa no lanza excepciones: clasifica y envía a cuarentena lo que no puede traducir, pero colapsa dos estados que el modelo antiguo distinguía. Las anomalías y sus frecuencias son una construcción del autor.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-438
def se438_cuatro_cambios_silenciosos() -> Fig:
    rows = [['Redondear a un decimal: regla antigua frente a round', '1 000 centésimas', '50 (5,0 %)'], ['Ordenar: punto de código frente a plegado de acentos', '2 000 nombres', '1 828 posiciones (91,4 %)'], ['Truncar a 6 bytes en UTF-8', '1 000 nombres', '114 con un carácter partido'], ['7n/2 frente a 7n//2', 'n de 1 a 1 000', '500 (los impares)']]
    return tab('Cuatro operaciones que siguen ejecutándose con otro resultado, medidas en CPython',
               'Tabla con cuatro operaciones del módulo medidas en CPython: redondear a un decimal cambia el resultado en 50 de 1 000 centésimas, ordenar 2 000 nombres por punto de código frente a plegado de acentos difiere en 1 828 posiciones, truncar a 6 bytes en UTF-8 parte 114 de 1 000 nombres y dividir 7n entre 2 con una barra frente a dos difiere en 500 de 1 000 casos.',
               ['Operación', 'Datos', 'Resultados distintos'], rows, [450, 190, 280], row_h=48, size=13,
               note='Ninguna lanza una excepción. Los datos son sintéticos y las frecuencias reales serán otras; las sondas ilustran el tipo de cambio y no son una lista completa de las diferencias de ninguna versión.',
               note_kind='coral', foot=REAL)

# ---------------------------------------------------------------- SE-438
def se438_reescritura_por_estructura() -> Fig:
    rows = [['Sustitución de texto', '252', '0'], ['Expresión regular con límites de palabra', '166', '0'], ['Árbol sintáctico (ast)', '0', '0']]
    return tab('Reescribir la llamada leer_nota en 400 fragmentos (148 llamadas reales): texto, expresión regular y árbol',
               'Tabla con tres formas de reescribir la llamada leer_nota en 400 fragmentos de código de los cuales 148 son llamadas reales: la sustitución de texto hace 252 reescrituras indebidas, la expresión regular con límites de palabra 166 y el árbol sintáctico 0, sin omitir ninguna llamada en ninguno de los tres.',
               ['Método', 'Reescrituras indebidas', 'Llamadas sin reescribir o mal reescritas'], rows, [400, 220, 300], row_h=48, size=13,
               note='Los tres encuentran todas las llamadas; la diferencia está en lo que cambian de más: comentarios, textos, métodos de otros objetos y definiciones. Los nueve tipos de fragmento son del autor y el árbol no se probó con código mal formado ni con reflexión.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-438
def se438_tren_de_versiones() -> Fig:
    rows = [['Al ser forzado', '16,3 % · 24,9 %', '3,0', '21'], ['Con un año de margen', '0,0 % · 6,3 %', '4,0', '28'], ['Paso a paso (6 meses de retraso)', '0,0 % · 0,0 %', '9,0', '19']]
    return tab('Tres políticas de seguimiento de versiones: una versión al año, tres años de soporte, diez años (1 000 historias)',
               'Tabla con tres políticas de seguimiento de versiones con soporte de tres años y una versión nueva al año durante diez años: al ser forzado deja 16,3 por ciento del tiempo sin soporte con 3 migraciones y 21 meses de trabajo, con un año de margen 0,0 por ciento de mediana y 6,3 en el percentil 90 con 4 migraciones y 28 meses, y paso a paso 0,0 con 9 migraciones y 19 meses.',
               ['Política', 'Sin soporte (mediana · p90)', 'Migraciones', 'Meses de migración'], rows, [330, 250, 150, 190], row_h=48, size=13,
               note='Esperar a que termine el soporte deja al equipo sin soporte el 16 % del tiempo; seguir paso a paso hace más migraciones y menos meses de trabajo solo si cada migración pequeña cuesta el 30 %. El calendario y el 30 % son supuestos del autor.',
               note_kind='gold', foot=SINT)


FIGURES = {
    "se-433-capacidad-devorada.svg": se433_capacidad_devorada,
    "se-433-clasificar-es-un-juicio.svg": se433_clasificar_es_un_juicio,
    "se-433-fecha-impuesta.svg": se433_fecha_impuesta,
    "se-434-puntos-calientes.svg": se434_puntos_calientes,
    "se-434-conocimiento-que-se-va.svg": se434_conocimiento_que_se_va,
    "se-434-codigo-muerto.svg": se434_codigo_muerto,
    "se-435-cobertura-no-es-detector.svg": se435_cobertura_no_es_detector,
    "se-435-orden-de-un-conjunto.svg": se435_orden_de_un_conjunto,
    "se-435-costura-y-tiempo.svg": se435_costura_y_tiempo,
    "se-436-costo-de-esperar.svg": se436_costo_de_esperar,
    "se-436-ventana-de-exposicion.svg": se436_ventana_de_exposicion,
    "se-436-radio-de-impacto.svg": se436_radio_de_impacto,
    "se-437-exposicion-por-estrategia.svg": se437_exposicion_por_estrategia,
    "se-437-sombra-y-clases-raras.svg": se437_sombra_y_clases_raras,
    "se-437-traduccion-anticorrupcion.svg": se437_traduccion_anticorrupcion,
    "se-438-cuatro-cambios-silenciosos.svg": se438_cuatro_cambios_silenciosos,
    "se-438-reescritura-por-estructura.svg": se438_reescritura_por_estructura,
    "se-438-tren-de-versiones.svg": se438_tren_de_versiones,
}
