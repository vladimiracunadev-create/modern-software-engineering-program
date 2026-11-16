"""Figures for SE-439 to SE-444 (modernization of a legacy grading module: synthetic data with fixed seeds, plus runs of real CPython/SQLite code on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."
REAL = "Medido en Windows 11 (CPython 3.12.9) y Ubuntu bajo WSL2 (3.12.3); los tiempos de reloj cambian de equipo en equipo."

# ---------------------------------------------------------------- SE-439
def se439_tamano_de_lote() -> Fig:
    rows = [['200 000', '4 005 ms', '4,0 s', '1 981 ms', '3 969 ms'], ['20 000', '405 ms', '4,2 s', '193 ms', '400 ms'], ['2 000', '45 ms', '6,5 s', '15 ms', '44 ms'], ['200', '9 ms', '29,0 s', '1,3 ms', '8,7 ms'], ['20', '5,4 ms', '254,0 s', '0,6 ms', '5,1 ms']]
    return tab('Relleno de 200 000 filas con 50 escrituras por segundo concurrentes, según el tamaño de lote',
               'Tabla con el relleno de 200 000 filas en cinco tamaños de lote con 50 escrituras por segundo: un lote de 200 000 bloquea 4 005 milisegundos y la escritura espera 3 969 en el percentil 99, un lote de 2 000 bloquea 45 y espera 44 con duración de 6,5 segundos, y un lote de 20 espera 5,1 pero el relleno dura 254 segundos.',
               ['Lote', 'Bloqueo por lote', 'Duración', 'Espera media', 'Espera p99'], rows, [160, 210, 170, 190, 190], row_h=40, size=13,
               note='Un lote pequeño casi no hace esperar a las escrituras y alarga el relleno por el costo fijo de cada lote. Los costos de 0,02 ms por fila y 5 ms por lote, la pausa de 20 ms y las llegadas Poisson son supuestos del autor.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-439
def se439_relleno_que_pisa() -> Fig:
    rows = [['Relleno ingenuo', '389'], ['Condicional por versión (y pasada final)', '0'], ['Condicional con la aplicación escribiendo en ambas columnas', '0'], ['Ingenuo con la aplicación escribiendo en ambas columnas', '389']]
    return tab('Relleno de 20 000 filas en lotes de 1 000 con un 2 % de filas modificadas por la aplicación entre lectura y escritura',
               'Tabla con cuatro estrategias de relleno de 20 000 filas en lotes de 1 000 con 2 por ciento de filas modificadas por la aplicación entre la lectura y la escritura: el relleno ingenuo deja 389 filas con la columna nueva distinta del texto, el condicional por versión deja 0, el condicional con doble escritura 0 y el ingenuo con doble escritura también 389.',
               ['Estrategia', 'Filas con la columna nueva distinta del texto'], rows, [600, 320], row_h=48, size=13,
               note='Los recuentos coinciden en las cuatro; el contenido, no. Escribir en ambas columnas no corrige un relleno ingenuo, que sobrescribe lo que la aplicación acaba de poner. La intercalación es determinista y no hay concurrencia real.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-439
def se439_metadatos_y_reconstruccion() -> Fig:
    rows = [['Añadir una columna nula', '0,37 ms', '0,34 ms'], ['Reconstruir la tabla (copiar)', '74 ms (200 veces)', '92 ms (267 veces)'], ['Rellenar con una sola sentencia', '57 ms', '62 ms'], ['Rellenar por lotes de 2 000', '60 ms (1,05 veces)', '151 ms (2,44 veces)']]
    return tab('Costo de cambios de esquema sobre 200 000 filas en SQLite',
               'Tabla con el costo real de cambios de esquema sobre 200 000 filas en SQLite: añadir una columna nula cuesta 0,37 milisegundos en Windows y 0,34 en Ubuntu, reconstruir la tabla 74 y 92, rellenar con una sentencia 57 y 62, y rellenar por lotes de 2 000 60 y 151.',
               ['Operación', 'Windows 11 (SQLite 3.45.3)', 'Ubuntu bajo WSL2 (SQLite 3.45.1)'], rows, [340, 290, 290], row_h=44, size=13,
               note='Añadir una columna es un cambio de metadatos y reconstruir la tabla cuesta cientos de veces más. SQLite es una base embebida en memoria; otros motores tienen reglas distintas. Los tiempos de reloj cambian de equipo en equipo.',
               note_kind='gold', foot=REAL)

# ---------------------------------------------------------------- SE-440
def se440_tres_formas_de_escribir_dos_veces() -> Fig:
    rows = [['Mejor esfuerzo (sin reintento)', '110', '292', '1 069'], ['Hasta tres intentos', '88', '84', '76'], ['Bandeja de salida con secuencia', '0', '0', '0']]
    return tab('Claves distintas entre dos almacenes tras 100 000 escrituras sobre 20 000 claves, según la tasa de fallo del segundo',
               'Tabla con las claves distintas entre dos almacenes tras 100 000 escrituras sobre 20 000 claves: el mejor esfuerzo deja 110, 292 y 1 069 con fallos del 0,1, 1 y 5 por ciento, tres intentos dejan 88, 84 y 76 por el desorden de las escrituras y una bandeja de salida con número de secuencia deja 0 en los tres casos.',
               ['Estrategia', 'p = 0,1 %', 'p = 1 %', 'p = 5 %'], rows, [390, 170, 170, 190], row_h=48, size=13,
               note='Los reintentos arreglan los fallos pero no el desorden (0,5 % de escrituras cruzadas); la bandeja con número de secuencia arregla ambos. Las tasas y el desorden son supuestos del autor y la bandeja reintenta sin límite.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-440
def se440_costo_de_detectar() -> Fig:
    rows = [['1', '108,5 ciclos · 108 490', '10,5 ciclos · 105 400', '1,0 ciclo · 1 100'], ['10', '10,9 ciclos · 10 947', '1,5 ciclos · 14 867', '1,0 ciclo · 9 667'], ['100', '1,6 ciclos · 1 583', '1,0 ciclo · 10 000', '1,0 ciclo · 63 483']]
    return tab('Ciclos y filas leídas hasta detectar divergencias entre 100 000 filas (media de 300 corridas)',
               'Tabla con ciclos y filas leídas hasta detectar divergencias entre 100 000 filas: con una divergencia el muestreo del 1 por ciento tarda 108,5 ciclos y lee 108 490 filas, el del 10 por ciento 10,5 ciclos y 105 400 filas, y las sumas por rangos un ciclo y 1 100 filas; con cien divergencias el muestreo del 1 por ciento lee 1 583 filas y las sumas por rangos 63 483.',
               ['Divergentes', 'Muestra del 1 %', 'Muestra del 10 %', 'Sumas por rangos'], rows, [160, 260, 260, 250], row_h=48, size=13,
               note='Con una divergencia las sumas por rangos ganan; con cien, el muestreo del 1 % lee menos. Las divergencias se reparten al azar y de forma uniforme, cosa que rara vez ocurre: suelen agruparse.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-440
def se440_matriz_de_compatibilidad() -> Fig:
    rows = [['Añadir campo opcional', 'falla · pasa', 'falla · pasa'], ['Añadir campo obligatorio', 'falla · pasa', 'falla · falla'], ['Quitar campo', 'falla · pasa', 'falla · pasa'], ['Renombrar campo', 'falla · falla', 'falla · pasa'], ['Cambiar el tipo', 'falla · falla', 'falla · falla'], ['Ampliar valores permitidos', 'falla · pasa', 'pasa · pasa']]
    return tab('Seis cambios de esquema y cuatro lecturas: lector viejo o nuevo, estricto o tolerante',
               'Tabla con seis cambios de esquema y cuatro lecturas: un lector estricto falla en 11 de 12 celdas, uno tolerante en 4 de 12; cambiar el tipo falla en las cuatro y renombrar un campo pasa con un lector tolerante nuevo que lee un dato viejo pero deja la nota ausente.',
               ['Cambio', 'Viejo lee dato nuevo (estricto · tolerante)', 'Nuevo lee dato viejo (estricto · tolerante)'], rows, [270, 330, 330], row_h=38, size=13,
               note='El lector estricto falla en 11 de 12 celdas; el tolerante, en 4. «Pasa» solo dice que no hubo excepción: un lector tolerante que lee un dato viejo tras renombrar la nota la deja ausente sin avisar. El registro de tres campos es del autor.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-441
def se441_ventana_de_observacion() -> Fig:
    rows = [['7 días', '54,9', '28 %'], ['30 días', '26,2', '14 %'], ['91 días', '10,5', '5 %'], ['180 días', '7,1', '4 %'], ['365 días', '0,0', '0 %'], ['400 días', '0,0', '0 %']]
    return tab('200 consumidores (194 reales) observados con distintas ventanas: cuántos reales se declararían «sin uso»',
               'Tabla con 200 consumidores sintéticos, 194 reales, observados con ventanas de 7, 30, 91, 180, 365 y 400 días: una ventana de 7 días declara sin uso a 54,9 consumidores reales, una de 30 días a 26,2, una de 91 días a 10,5, una de 180 días a 7,1 y las de 365 y 400 días a ninguno.',
               ['Ventana', 'Reales declarados «sin uso» (media)', 'Fracción de los 194'], rows, [200, 440, 280], row_h=40, size=13,
               note='Solo una ventana que cubra el ciclo más largo conocido ve a todos; un consumidor bianual que no esté en el inventario no lo vería ni la de 400 días. La mezcla de periodicidades es un supuesto del autor.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-441
def se441_retencion_por_reglas() -> Fig:
    rows = [['Corte único a 5 años', '5 479', '7 368'], ['Reglas por tipo con retención legal', '0', '0']]
    return tab('50 000 registros sintéticos de cuatro tipos: un corte único a cinco años frente a reglas por tipo',
               'Tabla con 50 000 registros sintéticos de cuatro tipos: un corte único a cinco años borra 5 479 registros antes de tiempo o en litigio y conserva 7 368 más de lo permitido, mientras que reglas por tipo con retención legal dan 0 y 0 por construcción del experimento.',
               ['Política', 'Borrados antes de tiempo o en litigio', 'Conservados más de lo permitido'], rows, [330, 330, 260], row_h=52, size=13,
               note='Las reglas dan cero porque definen la verdad del experimento: no prueban que los plazos sean correctos. Los plazos son ilustrativos del autor y no son asesoría legal.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-441
def se441_formatos_de_archivo() -> Fig:
    rows = [['CSV (tipos inferidos al leer)', '2,68 MB', '100 000 (10 080 pierden ceros; 19 851 vacíos pasan a nulos)'], ['Líneas JSON', '3,42 MB', '0'], ['SQLite', '3,31 MB', '0']]
    return tab('100 000 filas archivadas en tres formatos y leídas de vuelta',
               'Tabla con tres formatos para archivar 100 000 filas: CSV pesa 2,68 megabytes y ninguna fila vuelve idéntica porque cambian los tipos, 10 080 códigos pierden ceros y 19 851 textos vacíos se vuelven nulos; líneas JSON pesa 3,42 y SQLite 3,31, y en ambos todas las filas vuelven idénticas.',
               ['Formato', 'Tamaño', 'Filas que no vuelven idénticas'], rows, [300, 150, 470], row_h=52, size=13,
               note='El CSV solo guarda texto: sin un esquema que declare los tipos, los pierde. Un bit cambiado en un dígito del JSON deja un archivo válido que el lector acepta; solo la suma SHA-256 lo delata. Los datos son sintéticos.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-442
def se442_tres_opciones() -> Fig:
    rows = [['No hacer nada', '15,2', '12,1', '19,1'], ['Evolucionar', '13,5', '12,1', '15,1'], ['Reescribir', '19,1', '13,7', '27,6']]
    return tab('Costo acumulado a diez años de tres opciones en 20 000 escenarios (múltiplos del costo anual actual)',
               'Tabla con el costo acumulado a diez años de tres opciones en 20 000 escenarios sintéticos, en múltiplos del costo anual actual: no hacer nada tiene mediana 15,2 y rango de 12,1 a 19,1, evolucionar 13,5 y de 12,1 a 15,1, y reescribir 19,1 y de 13,7 a 27,6; reescribir es la opción más barata en el 9,4 por ciento de los escenarios.',
               ['Opción', 'Mediana', 'Percentil 10', 'Percentil 90'], rows, [300, 200, 200, 220], row_h=48, size=13,
               note='Reescribir es la opción más barata en el 9,4 % de los escenarios frente a evolucionar y tiene el rango más ancho. Es una consecuencia de los supuestos del autor, no un hallazgo sobre reescrituras reales.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-442
def se442_sensibilidad() -> Fig:
    rows = [['Costo de construir (3,0 → 12,0)', '+0,9 (37 %)', '+13,4 (0 %)', '12,5'], ['Costo anual del sistema nuevo (0,4 → 0,9)', '+3,2 (26 %)', '+7,5 (0 %)', '4,3'], ['Duración en años (1,5 → 4,0)', '+3,8 (18 %)', '+8,0 (1 %)', '4,2'], ['Deriva del alcance por año (0,05 → 0,25)', '+4,0 (14 %)', '+7,2 (6 %)', '3,2'], ['Probabilidad de abandono (0 → 0,4)', '+4,4 (11 %)', '+6,9 (7 %)', '2,4'], ['Crecimiento tras evolucionar (0,1 → 0,6)', '+6,2 (6 %)', '+4,6 (16 %)', '1,6'], ['Crecimiento del costo del legado (3 % → 15 %)', '+5,9 (4 %)', '+4,9 (16 %)', '1,0']]
    return tab('Sensibilidad: diferencia de costo entre reescribir y evolucionar al mover un parámetro (positiva: reescribir cuesta más)',
               'Tabla con la sensibilidad de la diferencia de costo entre reescribir y evolucionar: el costo de construir tiene el mayor recorrido, 12,5, y va de +0,9 con reescritura ganadora en el 37 por ciento de los escenarios a +13,4 con 0 por ciento; el costo anual del sistema nuevo 4,3, la duración 4,2, la deriva del alcance 3,2, el abandono 2,4, el crecimiento tras evolucionar 1,6 y el crecimiento del legado 1,0.',
               ['Parámetro (bajo → alto)', 'Con el valor bajo (gana)', 'Con el valor alto (gana)', 'Recorrido'], rows, [400, 200, 200, 120], row_h=40, size=12,
               note='El costo de construir domina; el crecimiento del costo del legado, el argumento más citado, es el de menor efecto. El análisis mueve un parámetro cada vez y no capta interacciones.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-442
def se442_horizonte_de_equilibrio() -> Fig:
    rows = [['4 años', '+6,7', '0 %'], ['6 años', '+6,3', '1 %'], ['8 años', '+6,0', '4 %'], ['10 años', '+5,7', '10 %'], ['15 años', '+4,5', '25 %'], ['20 años', '+3,4', '36 %']]
    return tab('Reescribir frente a evolucionar según el horizonte (6 000 escenarios por fila)',
               'Tabla con el horizonte de equilibrio entre reescribir y evolucionar: a 4 años reescribir cuesta 6,7 unidades más que evolucionar de mediana y gana en 0 por ciento de los escenarios, a 10 años 5,7 y 10 por ciento, a 15 años 4,5 y 25 por ciento, y a 20 años 3,4 y 36 por ciento.',
               ['Horizonte', 'Reescribir − evolucionar (mediana)', 'Reescribir gana'], rows, [200, 440, 280], row_h=40, size=13,
               note='La ventaja de evolucionar se acorta con el plazo, pero no se invierte en este rango. El horizonte es una variable de negocio: un sistema con fecha de retiro conocida cambia la respuesta más que cualquier detalle técnico.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-443
def se443_ruido_y_reintentos() -> Fig:
    rows = [['20 · ninguno', '64,3 %', '24,7 %'], ['20 · dos reintentos', '26,5 %', '58,2 %'], ['5 · ninguno', '23,2 %', '53,8 %'], ['5 · dos reintentos', '1,4 %', '90,3 %'], ['0 · ninguno', '0,0 %', '70,7 %']]
    return tab('5 000 commits por configuración: falsos rojos y defectos intermitentes (30 %) que salen verdes',
               'Tabla con cinco configuraciones de pruebas inestables y reintentos sobre 5 000 commits: con 20 inestables y sin reintentos el 64,3 por ciento de los commits sanos sale rojo y el 24,7 de los que tienen un defecto intermitente sale verde; con 5 inestables y dos reintentos 1,4 y 90,3; sin inestables y sin reintentos 0,0 y 70,7.',
               ['Inestables · reintentos', 'Commits sanos que salen rojos', 'Commits con defecto que salen verdes'], rows, [300, 300, 320], row_h=40, size=13,
               note='Reintentar reduce los falsos rojos y esconde defectos reales: con cinco inestables y dos reintentos el 90,3 % de los commits con el defecto pasan. La salida es aislar y corregir las inestables. El 5 %, el 30 % y la independencia son supuestos del autor.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-443
def se443_construccion_reproducible() -> Fig:
    rows = [['Bytecode', 'Invalidación por marca de tiempo', 'Distintas'], ['Bytecode', 'Invalidación por hash comprobado', 'Idénticas'], ['Archivo comprimido', 'Fechas de los archivos, orden del sistema', 'Distintas'], ['Archivo comprimido', 'Fechas fijas, orden del sistema', 'Idénticas'], ['Archivo comprimido', 'Fechas fijas, nombres ordenados', 'Idénticas']]
    return tab('Dos construcciones del mismo código con fechas de modificación distintas: ¿mismo artefacto?',
               'Tabla con cinco configuraciones de construcción del mismo código fuente con fechas de modificación distintas: el bytecode por marca de tiempo da artefactos distintos, por hash comprobado idénticos; el archivo comprimido con fechas del archivo da distintos, con fechas fijas idénticos y con fechas fijas y nombres ordenados idénticos.',
               ['Artefacto', 'Configuración', 'Resultado'], rows, [230, 470, 220], row_h=44, size=13,
               note='Fijar las fechas y el modo de invalidación basta aquí. Que el orden del sistema fuera estable en estas dos máquinas no está garantizado en general. Son treinta módulos de dos líneas: el experimento muestra el mecanismo, no la reproducibilidad de una cadena real.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-443
def se443_linea_base_con_incertidumbre() -> Fig:
    rows = [['10', '±19,3 puntos', '95 %'], ['20', '±15,4 puntos', '98 %'], ['50', '±9,6 puntos', '96 %'], ['200', '±4,9 puntos', '95 %'], ['1 000', '±2,2 puntos', '95 %']]
    return tab('Intervalo del 95 % de una tasa de cambios fallidos del 15 % según los cambios observados (3 000 periodos por fila)',
               'Tabla con el semiancho del intervalo de confianza del 95 por ciento de una tasa de cambios fallidos del 15 por ciento según los cambios observados: 19,3 puntos con 10, 15,4 con 20, 9,6 con 50, 4,9 con 200 y 2,2 con 1 000; para distinguir 15 de 10 por ciento hacen falta unos 686 cambios.',
               ['Cambios observados', 'Semiancho mediano', 'Contiene la tasa real'], rows, [300, 330, 290], row_h=40, size=13,
               note='Con 20 cambios la tasa del 15 % queda entre el 0 % y el 30 %. Para distinguir 15 % de 10 % con potencia del 80 % hacen falta unos 686 cambios. Se supone independencia entre cambios, algo falso cuando hay rachas.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-444
def se444_fases_y_divergencia() -> Fig:
    rows = [['0. Expandir', '5 000', '5 000', 'El nuevo está vacío'], ['1. Rellenar', '220', '220', 'Escrituras durante el relleno'], ['2. Doble escritura', '1', '0', 'Una segunda escritura falló'], ['3. Lectura del nuevo', '5', '0', 'Cinco fallos acumulados'], ['4. Solo escritura nueva', '391', '387', 'Valores que el antiguo no tiene']]
    return tab('Filas que difieren entre el esquema antiguo y el nuevo en cada fase de una migración de 5 000 filas',
               'Tabla con las filas que difieren entre el esquema antiguo y el nuevo en cinco fases de la migración de 5 000 filas: 5 000 al expandir, 220 tras rellenar, 1 y 0 con doble escritura con y sin fallos del uno por ciento, 5 y 0 con lectura del nuevo, y 391 y 387 al escribir solo en el nuevo, donde las diferencias son escrituras que el esquema antiguo no tiene.',
               ['Fase', 'Con 1 % de fallos', 'Sin fallos', 'Qué significa'], rows, [270, 170, 130, 350], row_h=44, size=13,
               note='La misma cuenta significa cosas distintas según la fase. En la fase 4 las diferencias son escrituras que solo existen en el esquema nuevo y que se perderían al volver sin reconstruir. SQLite en memoria, escrituras intercaladas de forma determinista.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-444
def se444_costo_de_volver() -> Fig:
    rows = [['0', '0', '0 %'], ['1', '58', '1,2 %'], ['3', '177', '3,5 %'], ['7', '406', '8,1 %'], ['14', '779', '15,6 %']]
    return tab('Filas que solo existen en el esquema nuevo según los días desde que se dejó de escribir en el antiguo (60 escrituras al día)',
               'Tabla con las filas que solo existen en el esquema nuevo según los días transcurridos desde que se dejó de escribir en el antiguo, con 60 escrituras diarias sobre 5 000 filas: 0 con cero días, 58 con uno, 177 con tres, 406 con siete y 779 con catorce.',
               ['Días', 'Filas que solo existen en el nuevo', 'Fracción de las 5 000'], rows, [160, 470, 290], row_h=40, size=13,
               note='Volver atrás pasa de no costar nada a afectar casi una de cada seis filas en dos semanas. Las escrituras uniformes sobre claves al azar son un supuesto del autor; en un sistema real se concentran en pocas filas y en fechas de cierre.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-444
def se444_reposo_antes_de_contraer() -> Fig:
    items = [('3 días', 86.7, 'coral', '86,7 %'), ('7 días', 60.1, 'coral', '60,1 %'), ('14 días', 33.2, 'gold', '33,2 %'), ('30 días', 11.4, 'gold', '11,4 %'), ('60 días', 2.9, 'teal', '2,9 %'), ('90 días', 1.1, 'teal', '1,1 %')]
    return bars('Defectos latentes que aparecen después de contraer, según el reposo (descubrimiento lognormal de mediana 9 días)',
                'Barras con la fracción de defectos latentes que aparecen después de contraer según el reposo, con descubrimiento lognormal de mediana nueve días: 86,7 por ciento con 3 días, 60,1 con 7, 33,2 con 14, 11,4 con 30, 2,9 con 60 y 1,1 con 90.',
                items, 6.0, 'Un reposo de tres días deja casi nueve de cada diez defectos latentes para después del punto de no retorno. La mediana de 9 días y la dispersión de 1,0 son supuestos del autor y se estiman con el historial de defectos propio.',
                label_w=130, width=940, note_kind='gold', foot=SINT)


FIGURES = {
    "se-439-tamano-de-lote.svg": se439_tamano_de_lote,
    "se-439-relleno-que-pisa.svg": se439_relleno_que_pisa,
    "se-439-metadatos-y-reconstruccion.svg": se439_metadatos_y_reconstruccion,
    "se-440-tres-formas-de-escribir-dos-veces.svg": se440_tres_formas_de_escribir_dos_veces,
    "se-440-costo-de-detectar.svg": se440_costo_de_detectar,
    "se-440-matriz-de-compatibilidad.svg": se440_matriz_de_compatibilidad,
    "se-441-ventana-de-observacion.svg": se441_ventana_de_observacion,
    "se-441-retencion-por-reglas.svg": se441_retencion_por_reglas,
    "se-441-formatos-de-archivo.svg": se441_formatos_de_archivo,
    "se-442-tres-opciones.svg": se442_tres_opciones,
    "se-442-sensibilidad.svg": se442_sensibilidad,
    "se-442-horizonte-de-equilibrio.svg": se442_horizonte_de_equilibrio,
    "se-443-ruido-y-reintentos.svg": se443_ruido_y_reintentos,
    "se-443-construccion-reproducible.svg": se443_construccion_reproducible,
    "se-443-linea-base-con-incertidumbre.svg": se443_linea_base_con_incertidumbre,
    "se-444-fases-y-divergencia.svg": se444_fases_y_divergencia,
    "se-444-costo-de-volver.svg": se444_costo_de_volver,
    "se-444-reposo-antes-de-contraer.svg": se444_reposo_antes_de_contraer,
}
