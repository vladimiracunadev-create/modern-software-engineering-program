"""Figuras de SE-451 a SE-456: datos sintéticos con semilla fija y ejecuciones de código propio sobre datos sintéticos (CPython 3.12.9 en Windows 11, repetido con 3.12.3 en Ubuntu bajo WSL2)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import tab

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."


# ---------------------------------------------------------------- SE-451
def se451_pesos_y_ganador() -> Fig:
    return tab('Cuánto depende el ganador de los pesos',
               'Tabla con cinco proveedores sintéticos evaluados en seis criterios: con los pesos base el puntaje es 6,60 para A, 6,95 para B, 6,55 para C, 6,70 para D y 6,45 para E; con 20 000 combinaciones de pesos sorteadas gana A el 7,6 por ciento, B el 19,4, C el 30,9, D el 21,1 y E el 20,9, y al exigir seguridad de 6 o más D queda fuera y ganan A 18,9, B 24,2, C 36 y E 20,9.',
               ['Proveedor', 'Puntaje con los pesos base', 'Gana con pesos sorteados', 'Gana con la puerta de seguridad'], [['A', '6,60', '7,6 %', '18,9 %'], ['B', '6,95', '19,4 %', '24,2 %'], ['C', '6,55', '30,9 %', '36,0 %'], ['D', '6,70', '21,1 %', 'no pasa la puerta'], ['E', '6,45', '20,9 %', '20,9 %']], [100, 232, 216, 271], row_h=44, size=13,
               note='El proveedor B gana con los pesos del equipo por 0,25 puntos, pero con pesos al azar gana solo una de cada cinco veces; C, que queda tercero con los pesos base, gana casi una de cada tres. La puerta de seguridad cambia el reparto, no el hecho de que ninguno domina.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-451
def se451_comprar_o_construir() -> Fig:
    return tab('Cuánto cuesta comprar o construir en cinco años',
               'Tabla con 10 000 casos sintéticos de costo a cinco años: comprar cuesta de media 870, mediana 796 y percentil 90 de 1 235, construir de media 867, mediana 842 y percentil 90 de 1 085, y comprar cuesta más que construir en el 45,8 por ciento de los casos.',
               ['Opción', 'Costo medio', 'Mediana', 'Percentil 90'], [['Comprar', '870', '796', '1 235'], ['Construir', '867', '842', '1 085']], [182, 217, 169, 232], row_h=44, size=13,
               note='Las medias son casi iguales y las medianas favorecen comprar, pero el percentil 90 de comprar es 150 unidades mayor: la cola de alzas y de migración forzada. La decisión depende de cuánta cola puede asumir el equipo.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-451
def se451_cadena_de_disponibilidad() -> Fig:
    return tab('Cuánto cae una cadena de proveedores',
               'Tabla con la disponibilidad de una cadena de proveedores cada uno al 99,9 por ciento: uno da 99,9 por ciento y 526 minutos de caída al año, tres dan 99,7 y 1 575, cinco dan 99,501 y 2 623, y cinco con el más débil duplicado 99,6 y 2 100, con simulaciones de 536, 1 572, 2 615 y 2 083 minutos.',
               ['Cadena', 'Disponibilidad', 'Minutos de caída al año (cálculo)', 'Minutos de caída (simulado)'], [['1 proveedor', '99,900 %', '526', '536'], ['3 proveedores', '99,700 %', '1 575', '1 572'], ['5 proveedores', '99,501 %', '2 623', '2 615'], ['5, con el más débil duplicado', '99,600 %', '2 100', '2 083']], [245, 139, 286, 240], row_h=44, size=13,
               note='Cada proveedor adicional agrega unos 525 minutos de caída esperada, y la cadena de cinco pasa de 8,8 a 43,7 horas al año. Duplicar solo el eslabón más débil recupera la quinta parte del daño.',
               note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-452
def se452_licencias_y_politica() -> Fig:
    return tab('Qué bloquea una política de distribución',
               'Tabla con 60 dependencias sintéticas clasificadas por un analizador de expresiones de licencia: 42 permitidas, 11 por revisar, 4 bloqueadas y 3 desconocidas, frente a una búsqueda ingenua de la cadena GPL que marca 15, de las cuales 11 no están bloqueadas, no deja de ver ninguna bloqueada y da por buenas 3 desconocidas.',
               ['Resultado', 'Dependencias'], [['Permitidas', '42'], ['Por revisar', '11'], ['Bloqueadas', '4'], ['Desconocidas (vacío, NOASSERTION, referencia propia)', '3'], ['Marcadas por la búsqueda ingenua', '15'], ['Marcadas por la ingenua y no bloqueadas', '11'], ['Bloqueadas que la ingenua no ve', '0'], ['Desconocidas que la ingenua da por buenas', '3']], [582, 218], row_h=44, size=13,
               note='La búsqueda ingenua marca casi cuatro veces más dependencias que las bloqueadas (porque encuentra `LGPL`, `MIT OR GPL-2.0-only` y excepciones) y, a la vez, no ve las tres desconocidas. Los dos errores son distintos: uno frena trabajo innecesariamente y el otro deja pasar lo que no se sabe.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-452
def se452_firma_de_origen() -> Fig:
    return tab('Qué detecta una verificación de firma',
               'Tabla con 2 000 mensajes de commit sintéticos: 1 709 con pie de firma correcto aceptados por la verificación estricta, y 83 sin firma, 54 con firma de otra persona, 44 con el pie mal escrito, 49 con el pie en medio del texto y 61 con correo roto, todos rechazados; la verificación ingenua acepta 1 873 y la estricta 1 709.',
               ['Tipo de commit', 'Cantidad', 'Aceptados por la estricta'], [['Pie correcto', '1 709', '1 709'], ['Sin firma', '83', '0'], ['Firma de otra persona', '54', '0'], ['Pie mal escrito', '44', '0'], ['Pie en medio del texto', '49', '0'], ['Correo roto', '61', '0'], ['Total aceptado', '2 000', 'ingenua: 1 873; estricta: 1 709']], [283, 135, 381], row_h=44, size=13,
               note='La búsqueda ingenua da por firmados 164 commits que la estricta rechaza: la firma de otra persona, el pie en medio y el correo roto. Cada uno es un tipo de defecto distinto, con causa y corrección distintas.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-452
def se452_costo_del_patron_oscuro() -> Fig:
    return tab('Qué cuesta un flujo de cancelación escondido',
               'Tabla con 12 meses simulados de dos flujos de suscripción: el honesto acumula un ingreso neto de 22 965 al mes 3, 76 403 al mes 6 y 256 658 al mes 12 con 104 reclamos y 3 620 personas suscritas, y el de cancelación escondida acumula 26 972, 89 830 y 294 799 con 956 reclamos y 4 279 suscritas.',
               ['Flujo', 'Ingreso neto acumulado (mes 3 · 6 · 12)', 'Reclamos acumulados (mes 12)', 'Personas suscritas (mes 12)'], [['Honesto', '22 965 · 76 403 · 256 658', '104', '3 620'], ['Cancelación escondida', '26 972 · 89 830 · 294 799', '956', '4 279']], [176, 314, 235, 228], row_h=44, size=13,
               note='En esta simulación el flujo escondido gana en ingresos todo el año: 38 141 más a los doce meses. La contrapartida es nueve veces más reclamos.',
               note_kind='teal', foot=EJEC)

# ---------------------------------------------------------------- SE-453
def se453_orden_y_costo_de_demora() -> Fig:
    return tab('Cuánto cuesta esperar según el orden',
               'Tabla con 3 000 carteras sintéticas de 12 iniciativas: el orden de llegada cuesta de media 1,8 veces el óptimo y 2,61 veces en el percentil 95, lo más corto primero 1,3 y 1,66, el mayor costo de demora primero 1,13 y 1,26, y el costo de demora dividido por la duración 1 y 1 por ser el óptimo.',
               ['Orden de ejecución', 'Costo medio frente al óptimo', 'Peor caso (p95)'], [['Orden de llegada', '1,80', '2,61'], ['Lo más corto primero', '1,30', '1,66'], ['Mayor costo de demora primero', '1,13', '1,26'], ['Costo de demora entre duración', '1,00', '1,00']], [312, 307, 181], row_h=44, size=13,
               note='Esperar sin criterio cuesta un 80 % más que el óptimo de media y más del doble en una de cada veinte carteras; ordenar solo por valor o solo por duración recupera buena parte, pero no todo. La última fila es 1,00 por construcción: es el orden que minimiza el costo.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-453
def se453_valor_presente_y_orden() -> Fig:
    return tab('Cuándo un proyecto deja de ser el mejor',
               'Tabla con tres proyectos sintéticos con inversión de 100: Automatizar el cierre suma 60, tiene valor presente de 43,2 a 5 por ciento, 29,2 a 10, 7,4 a 20 y menos 8,6 a 30, retorno de 24,3 por ciento y recuperación en el año 2; Rediseñar el módulo suma 110 con 74,3, 46,3, 6,5 y menos 19,7, retorno de 22,1 y recuperación en el año 4; Plataforma interna suma 140 con 88, 49, menos 3,5 y menos 35,4, retorno de 19,1 y recuperación en el año 5.',
               ['Proyecto', 'Suma sin descontar', 'VAN 5 %', 'VAN 10 %', 'VAN 20 %', 'VAN 30 %', 'TIR', 'Recuperación'], [['Automatizar el cierre', '60', '43,2', '29,2', '7,4', '−8,6', '24,3 %', 'año 2'], ['Rediseñar el módulo', '110', '74,3', '46,3', '6,5', '−19,7', '22,1 %', 'año 4'], ['Plataforma interna', '140', '88,0', '49,0', '−3,5', '−35,4', '19,1 %', 'año 5']], [185, 170, 90, 92, 92, 92, 90, 123], row_h=44, size=13,
               note='A tasas del 5 % y del 10 %, la plataforma interna es la mejor por VAN; a partir del 20 % pasa a ser la peor y el primero es «Automatizar el cierre». La suma sin descontar y el VAN a tasa baja favorecen lo tardío; la TIR y la recuperación favorecen lo temprano.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-453
def se453_propio_nube_y_equilibrio() -> Fig:
    return tab('Propio o nube, y cuántas personas hacen falta',
               'Tabla con el cruce entre servidores propios y nube en el mes 33 sin descuento y el mes 39 con una tasa mensual de 0,8 por ciento, un equilibrio de 6 250 personas usuarias con márgenes de menos 86,7, 0, 30 y 63,3 por ciento para 3 000, 6 250, 10 000 y 30 000, y una probabilidad de alcanzar el equilibrio en 12 meses de 0, 52,5 y 99,3 por ciento desde 2 000, 4 000 y 6 000 personas.',
               ['Pregunta', 'Resultado'], [['Mes en que lo propio acumula menos costo (sin descontar)', '33'], ['Mes con tasa mensual de 0,8 %', '39'], ['Personas usuarias de equilibrio (20 000 / (4 − 0,8))', '6 250'], ['Margen con 3 000 · 6 250 · 10 000 · 30 000 personas', '−86,7 % · 0 % · 30,0 % · 63,3 %'], ['Probabilidad de alcanzar el equilibrio en 12 meses desde 2 000 · 4 000 · 6 000', '0,0 % · 52,5 % · 99,3 %']], [448, 352], row_h=44, size=13,
               note='Descontar retrasa seis meses el cruce, porque la inversión inicial pesa más que las cuotas futuras. El equilibrio de 6 250 personas separa a un servicio que pierde de uno que gana, pero alcanzarlo en un año es casi imposible desde 2 000 personas y casi seguro desde 6 000.',
               note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-454
def se454_entrevistas_y_eleccion() -> Fig:
    return tab('Qué eligen las entrevistas',
               'Tabla con 8 000 procesos de selección sintéticos de 10 candidaturas: una conversación libre elige una persona con habilidad media de 0,95, el 61,6 por ciento de lo alcanzable, tres conversaciones libres 1,10 y 71,2, una entrevista estructurada 1,25 y 80,9, tres entrevistas estructuradas 1,41 y 91,1, y elegir al azar 0 por ciento.',
               ['Procedimiento', 'Habilidad media de la persona elegida', 'Fracción de lo alcanzable (la mejor de las 10)'], [['Una conversación libre', '0,95', '61,6 %'], ['Tres conversaciones libres', '1,10', '71,2 %'], ['Una entrevista estructurada', '1,25', '80,9 %'], ['Tres entrevistas estructuradas', '1,41', '91,1 %'], ['Al azar', '0,00', '0 %']], [252, 317, 330], row_h=44, size=13,
               note='Añadir entrevistadoras ayuda, pero menos que estructurar: una estructurada (80,9 %) supera a tres libres (71,2 %), porque el halo compartido no se promedia.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-454
def se454_verificador_de_portafolio() -> Fig:
    return tab('Qué comprueba un verificador de portafolio',
               'Tabla con cuatro entradas sintéticas de portafolio revisadas por un verificador de seis reglas: la entrada con evidencia cumple 6, la entrada a medias 2 y le faltan comando, límite, decisión con alternativa y versión, la entrada de adjetivos 0 y le falta todo, y la entrada con relleno cumple 6 sin tener sustancia.',
               ['Entrada', 'Reglas cumplidas (de 6)', 'Qué falta'], [['Con evidencia', '6', 'nada'], ['A medias', '2', 'comando, límite, decisión y alternativa, versión'], ['De adjetivos', '0', 'todo'], ['Con relleno', '6', 'nada, pero sin sustancia']], [152, 251, 397], row_h=44, size=13,
               note='El verificador separa con claridad las dos entradas extremas, y distingue la que tiene la estructura incompleta. La última fila es el límite: una entrada con cifras, un comando y un enlace inventados cumple las seis reglas.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-454
def se454_defensa_por_profundidad() -> Fig:
    return tab('Qué impresión deja cada estrategia de defensa',
               'Tabla con una persona que responde seis preguntas de profundidad creciente: con conocimiento de nivel 2 defender todo con seguridad deja una impresión de menos 4,8 y se descubre un error seguro en el 98,4 por ciento de los casos, mientras que declarar el límite deja 2,3 y 0 por ciento; con conocimiento de nivel 4 defender todo deja 0,56 y 87,1 por ciento y declarar el límite 4,3 y 0 por ciento.',
               ['Conocimiento', 'Estrategia', 'Impresión media', 'Detectada en un error seguro'], [['Nivel 2', 'Defiende todo con seguridad', '−4,8', '98,4 %'], ['Nivel 2', 'Declara su límite y propone cómo comprobar', '2,3', '0 %'], ['Nivel 4', 'Defiende todo con seguridad', '0,56', '87,1 %'], ['Nivel 4', 'Declara su límite y propone cómo comprobar', '4,3', '0 %']], [123, 330, 147, 248], row_h=44, size=13,
               note='Con conocimiento de nivel 4, defender todo deja una impresión cercana a cero; declarar el límite, de 4,3. Con nivel 2 la diferencia es mayor, porque hay más preguntas en que inventar.',
               note_kind='teal', foot=EJEC)

# ---------------------------------------------------------------- SE-455
def se455_resultado_o_proceso() -> Fig:
    return tab('Cuántas decisiones hacen falta para distinguir a quien decide mejor',
               'Tabla con dos personas que deciden con calidad buena en el 65 y el 50 por ciento de los casos: con 5 decisiones por persona, juzgar por resultados identifica a la mejor en el 56,3 por ciento y por proceso en el 63, con 10 en 57,6 y 67,9, con 20 en 62,4 y 75,1, con 50 en 67,9 y 85, y con 100 en 73,6 y 93,4.',
               ['Decisiones por persona', 'Identifica a la mejor decisora por resultados', 'Por calidad del proceso'], [['5', '56,3 %', '63,0 %'], ['10', '57,6 %', '67,9 %'], ['20', '62,4 %', '75,1 %'], ['50', '67,9 %', '85,0 %'], ['100', '73,6 %', '93,4 %']], [217, 357, 226], row_h=44, size=13,
               note='Con diez decisiones por persona, juzgar por resultados apenas supera el azar (57,6 %); incluso con cien decisiones, el 26 % de las veces se elige a la persona equivocada. Juzgar el proceso, aun con una auditoría imperfecta, acierta más con cualquier cantidad.',
               note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-455
def se455_cobertura_de_un_panel() -> Fig:
    return tab('Qué cobertura logra un panel',
               'Tabla con 5 000 revisiones sintéticas de 30 modos de fallo en tres dominios: cuatro revisoras del mismo dominio cubren el 58 por ciento de media y 31,5 el dominio peor cubierto, dos y dos de dos dominios 67,2 y 39,8, una generalista y tres de dominios distintos 71 y 58,8, y la misma composición con ejercicio previo al fallo 83,2 y 73,1.',
               ['Composición del panel', 'Cobertura media', 'Dominio peor cubierto'], [['4 revisoras del mismo dominio', '58,0 %', '31,5 %'], ['2 y 2 de dos dominios', '67,2 %', '39,8 %'], ['Una generalista y tres de dominios distintos', '71,0 %', '58,8 %'], ['La anterior, con ejercicio previo al fallo', '83,2 %', '73,1 %']], [394, 175, 231], row_h=44, size=13,
               note='La composición pesa más que el número de personas: cuatro del mismo dominio dejan un dominio con menos de un tercio cubierto, y una composición diversa lo sube a más de la mitad. El ejercicio previo al fallo suma otros doce puntos.',
               note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-455
def se455_calibracion_y_brier() -> Fig:
    return tab('Qué dice la confianza declarada',
               'Tabla con 500 pronósticos de cada una de tres personas: la calibrada obtiene una puntuación de Brier de 0,175 y acierta 94,4 por ciento cuando declara 95; la sobreconfiada obtiene 0,249 y acierta 74,4 por ciento cuando declara 95; la que declara siempre 95 por ciento obtiene 0,317 y acierta 65 por ciento.',
               ['Persona', 'Brier', 'Acierto cuando declara 55 · 65 · 75 · 85 · 95 %'], [['Calibrada', '0,175', '53,5 · 73,7 · 69,0 · 82,7 · 94,4 %'], ['Sobreconfiada', '0,249', '50,5 · 69,7 · 57,0 · 65,5 · 74,4 %'], ['Siempre 95 %', '0,317', 'solo 95 %: 65,0 %']], [185, 132, 483], row_h=44, size=13,
               note='La calibrada declara 95 % y acierta alrededor de 94 %; la sobreconfiada, con la misma declaración, acierta 74 %. La diferencia es invisible mientras nadie contrasta las probabilidades con los resultados.',
               note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-456
def se456_verificador_de_dossier() -> Fig:
    return tab('Qué detecta el verificador',
               'Tabla con seis variantes sintéticas de un dossier verificadas por un script: la completa no tiene defectos, la que no tiene límites se detecta por tener menos de tres, la que tiene una afirmación sin evidencia se detecta en C5, la de evidencia alterada en C2, la de evidencia borrada en C3 y la de cifra distinta se detecta por el conflicto en el costo a cinco años pero no por la guardia de cinco o seis personas.',
               ['Variante', 'Defecto introducido', 'Defectos detectados', 'Cifras en conflicto'], [['Completo', 'ninguno', 'ninguno', 'ninguna'], ['Sin límites', 'LIMITES.md sin límites', 'menos de 3 límites', 'ninguna'], ['Afirmación sin respaldo', 'C5 sin evidencia', 'C5 sin evidencia', 'ninguna'], ['Evidencia alterada', 'e2.txt cambiado tras la huella', 'C2 con evidencia alterada', 'ninguna'], ['Evidencia faltante', 'e3.txt borrado', 'C3 con evidencia ausente', 'ninguna'], ['Cifra distinta', 'costo 1 020 frente a 1 200 y guardia 5 frente a 6', 'ninguno', 'TCO_5A']], [200, 330, 215, 178], row_h=44, size=13,
               note='Cada variante tiene un defecto distinto y el verificador lo señala con la afirmación o el archivo exactos. La última fila muestra el límite: se introdujeron dos incoherencias y se detectó una; la otra (personas de guardia, 5 en riesgos y 6 en el `README`) no se vio porque la cifra del `README` no estaba etiquetada.',
               note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-456
def se456_probabilidad_de_ser_vista() -> Fig:
    return tab('Cuánto se encuentra al muestrear',
               'Tabla con la probabilidad exacta de que una revisora encuentre al menos una afirmación sin respaldo en un dossier de 30: con 1 sin respaldo y 3, 5, 8 o 12 inspeccionadas es 10, 16,7, 26,7 y 40 por ciento, con 3 sin respaldo 28, 43,3, 62,1 y 79,9, y con 6 sin respaldo 50,1, 70,2, 87,4 y 96,9.',
               ['Afirmaciones sin respaldo', 'Revisa 3', 'Revisa 5', 'Revisa 8', 'Revisa 12'], [['1 de 30', '10,0 %', '16,7 %', '26,7 %', '40,0 %'], ['3 de 30', '28,0 %', '43,3 %', '62,1 %', '79,9 %'], ['6 de 30', '50,1 %', '70,2 %', '87,4 %', '96,9 %']], [299, 123, 123, 123, 133], row_h=44, size=13,
               note='Una sola afirmación sin respaldo entre treinta supera el 25 % de probabilidad de ser vista solo si se inspeccionan ocho. Para encontrar con 80 % un problema de tres afirmaciones hay que inspeccionar doce.',
               note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-456
def se456_hora_de_revision() -> Fig:
    return tab('Cuántas afirmaciones se comprueban en una hora',
               'Tabla con 5 000 revisiones simuladas de 60 minutos sobre un dossier de 30 afirmaciones: sin trazabilidad se comprueban 5,7 afirmaciones de media, entre 4 y 7 en los percentiles 10 y 90, y con una tabla de afirmación, evidencia y huella 21,7, entre 19 y 24.',
               ['Dossier', 'Afirmaciones comprobadas en 60 minutos (media)', 'p10 – p90'], [['Sin trazabilidad', '5,7', '4 – 7'], ['Con tabla afirmación–evidencia–huella', '21,7', '19 – 24']], [331, 360, 109], row_h=44, size=13,
               note='La tabla multiplica por casi cuatro lo que se puede comprobar en una hora; incluso así, no se llega a las treinta, por lo que el verificador automático sigue siendo necesario.',
               note_kind='teal', foot=EJEC)


FIGURES = {
    "se-451-pesos-y-ganador.svg": se451_pesos_y_ganador,
    "se-451-comprar-o-construir.svg": se451_comprar_o_construir,
    "se-451-cadena-de-disponibilidad.svg": se451_cadena_de_disponibilidad,
    "se-452-licencias-y-politica.svg": se452_licencias_y_politica,
    "se-452-firma-de-origen.svg": se452_firma_de_origen,
    "se-452-costo-del-patron-oscuro.svg": se452_costo_del_patron_oscuro,
    "se-453-orden-y-costo-de-demora.svg": se453_orden_y_costo_de_demora,
    "se-453-valor-presente-y-orden.svg": se453_valor_presente_y_orden,
    "se-453-propio-nube-y-equilibrio.svg": se453_propio_nube_y_equilibrio,
    "se-454-entrevistas-y-eleccion.svg": se454_entrevistas_y_eleccion,
    "se-454-verificador-de-portafolio.svg": se454_verificador_de_portafolio,
    "se-454-defensa-por-profundidad.svg": se454_defensa_por_profundidad,
    "se-455-resultado-o-proceso.svg": se455_resultado_o_proceso,
    "se-455-cobertura-de-un-panel.svg": se455_cobertura_de_un_panel,
    "se-455-calibracion-y-brier.svg": se455_calibracion_y_brier,
    "se-456-verificador-de-dossier.svg": se456_verificador_de_dossier,
    "se-456-probabilidad-de-ser-vista.svg": se456_probabilidad_de_ser_vista,
    "se-456-hora-de-revision.svg": se456_hora_de_revision,
}
