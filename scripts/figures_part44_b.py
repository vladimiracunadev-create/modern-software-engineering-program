"""Figuras de SE-535 a SE-540: datos sintéticos con semilla fija y ejecuciones de código propio sobre datos sintéticos (CPython 3.12.9 en Windows 11, repetido con 3.12.3 en Ubuntu bajo WSL2)."""
from __future__ import annotations

from figure_cases import case_cards
from figure_kit import Fig, fmt_es, grouped_bars, line_chart, percentile_intervals, stacked_bars

SINT = "Datos sintéticos con semilla fija; Windows y Ubuntu (WSL2) dan cifras idénticas."
EJEC = "Código ejecutado de verdad en Windows 11 y Ubuntu (WSL2) con datos sintéticos; los recuentos son idénticos en ambos."


# ---------------------------------------------------------------- SE-535
def se451_pesos_y_ganador() -> Fig:
    return grouped_bars('Cuánto depende el ganador de los pesos',
                        'Barras agrupadas con cinco proveedores sintéticos evaluados en seis criterios: con 20 000 combinaciones de pesos sorteadas gana A el 7,6 por ciento, B el 19,4, C el 30,9, D el 21,1 y E el 20,9; al exigir seguridad de 6 o más D queda fuera y ganan A 18,9, B 24,2, C 36 y E 20,9, aunque con los pesos base el mejor puntaje es el de B, 6,95.',
                        ['A (6,60 con los pesos base)', 'B (6,95)', 'C (6,55)', 'D (6,70)', 'E (6,45)'],
                        [('Gana con pesos sorteados', [7.6, 19.4, 30.9, 21.1, 20.9], 'teal'), ('Gana con la puerta de seguridad', [18.9, 24.2, 36.0, 0.0, 20.9], 'gold')],
                        unit='% de las 20 000 combinaciones en que gana', decimals=1,
                        note='D no pasa la puerta de seguridad. El proveedor B gana con los pesos del equipo por 0,25 puntos, pero con pesos al azar gana solo una de cada cinco veces; C, que queda tercero con los pesos base, gana casi una de cada tres. La puerta de seguridad cambia el reparto, no el hecho de que ninguno domina.',
                        note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-535
def se451_comprar_o_construir() -> Fig:
    return grouped_bars('Cuánto cuesta comprar o construir en cinco años',
                        'Barras agrupadas con 10 000 casos sintéticos de costo a cinco años: comprar cuesta de media 870, mediana 796 y percentil 90 de 1235; construir de media 867, mediana 842 y percentil 90 de 1085; comprar cuesta más que construir en el 45,8 por ciento de los casos.',
                        ['Comprar', 'Construir'],
                        [('Costo medio', [870, 867], 'teal'), ('Mediana', [796, 842], 'gold'), ('Percentil 90', [1235, 1085], 'coral')],
                        unit='costo a cinco años',
                        note='Comprar cuesta más que construir en el 45,8 % de los casos. Las medias son casi iguales y las medianas favorecen comprar, pero el percentil 90 de comprar es 150 unidades mayor: la cola de alzas y de migración forzada. La decisión depende de cuánta cola puede asumir el equipo.',
                        note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-535
def se451_cadena_de_disponibilidad() -> Fig:
    return grouped_bars('Cuánto cae una cadena de proveedores',
                        'Barras agrupadas con los minutos de caída al año de una cadena de proveedores cada uno al 99,9 por ciento: uno da 526 calculados y 536 simulados, tres 1575 y 1572, cinco 2623 y 2615, y cinco con el más débil duplicado 2100 y 2083.',
                        ['1 proveedor (99,900 %)', '3 proveedores (99,700 %)', '5 proveedores (99,501 %)', '5, con el más débil duplicado (99,600 %)'],
                        [('Minutos de caída al año (cálculo)', [526, 1575, 2623, 2100], 'teal'), ('Minutos de caída (simulado)', [536, 1572, 2615, 2083], 'grey')],
                        unit='minutos de caída al año',
                        note='Cada proveedor adicional agrega unos 525 minutos de caída esperada, y la cadena de cinco pasa de 8,8 a 43,7 horas al año. Duplicar solo el eslabón más débil recupera la quinta parte del daño.',
                        note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-536
def se452_licencias_y_politica() -> Fig:
    return stacked_bars('Qué bloquea una política de distribución',
                        'Barras horizontales apiladas con 60 dependencias sintéticas: un analizador de expresiones de licencia clasifica 42 como permitidas, 11 por revisar, 4 bloqueadas y 3 desconocidas, mientras la búsqueda ingenua de la cadena GPL marca 15, de las cuales 11 no están bloqueadas, ve las 4 bloqueadas y da por buenas las 3 desconocidas.',
                        ['Analizador de licencias', 'Búsqueda ingenua de GPL'],
                        [('Permitidas', [42, 0], 'teal'), ('Por revisar', [11, 0], 'gold'), ('Bloqueadas', [4, 4], 'coral'), ('Desconocidas (vacío, NOASSERTION, referencia propia)', [3, 0], 'navy'),
                         ('Marcadas sin estar bloqueadas', [0, 11], 'grey')],
                        unit='dependencias clasificadas o marcadas', horizontal=True, label_w=200,
                        note='La búsqueda ingenua deja sin marcar las otras 45 dependencias (entre ellas las 3 desconocidas) y marca 15 dependencias, casi cuatro veces las 4 bloqueadas (porque encuentra LGPL, MIT OR GPL-2.0-only y excepciones), no deja de ver ninguna bloqueada y a la vez no ve las tres desconocidas. Los dos errores son distintos: uno frena trabajo innecesariamente y el otro deja pasar lo que no se sabe.',
                        note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-536
def se452_firma_de_origen() -> Fig:
    return grouped_bars('Qué detecta una verificación de firma',
                        'Barras horizontales con 2 000 mensajes de commit sintéticos: 1 709 con pie de firma correcto los aceptan las dos verificaciones; la ingenua acepta además 54 con firma de otra persona, 49 con el pie en medio del texto y 61 con correo roto, y la estricta rechaza todos esos y los 83 sin firma y los 44 con el pie mal escrito.',
                        ['Pie correcto', 'Sin firma', 'Firma de otra persona', 'Pie mal escrito', 'Pie en medio del texto', 'Correo roto'],
                        [('Cantidad', [1709, 83, 54, 44, 49, 61], 'grey'), ('Aceptados por la ingenua', [1709, 0, 54, 0, 49, 61], 'coral'), ('Aceptados por la estricta', [1709, 0, 0, 0, 0, 0], 'teal')],
                        unit='mensajes de commit', horizontal=True, label_w=190,
                        note='Total aceptado: 1 873 con la ingenua y 1 709 con la estricta. La búsqueda ingenua da por firmados 164 commits que la estricta rechaza: la firma de otra persona, el pie en medio y el correo roto. Cada uno es un tipo de defecto distinto, con causa y corrección distintas.',
                        note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-536
def se452_costo_del_patron_oscuro() -> Fig:
    ms = [3, 6, 12]
    return line_chart('Qué cuesta un flujo de cancelación escondido',
                      'Líneas con el ingreso neto acumulado de 12 meses simulados de dos flujos de suscripción: el honesto suma 22 965 al mes 3, 76 403 al mes 6 y 256 658 al mes 12, y el de cancelación escondida 26 972, 89 830 y 294 799, con 956 reclamos frente a 104.',
                      [('Cancelación escondida', [(m, v, fmt_es(v), 't') for m, v in zip(ms, [26972, 89830, 294799])], 'coral'), ('Honesto', [(m, v, fmt_es(v), 'r' if m == 3 else 'b') for m, v in zip(ms, [22965, 76403, 256658])], 'teal')],
                      x_label='Mes', y_label='Ingreso neto acumulado', x_ticks=[(m, str(m)) for m in ms], y_ticks=[0, 100000, 200000, 300000],
                      note='Reclamos acumulados al mes 12: 104 con el flujo honesto y 956 con el de cancelación escondida; personas suscritas: 3 620 y 4 279. En esta simulación el flujo escondido gana en ingresos todo el año: 38 141 más a los doce meses. La contrapartida es nueve veces más reclamos.',
                      note_kind='teal', foot=EJEC)

# ---------------------------------------------------------------- SE-537
def se453_orden_y_costo_de_demora() -> Fig:
    return grouped_bars('Cuánto cuesta esperar según el orden',
                        'Barras agrupadas con el costo de 3 000 carteras sintéticas de 12 iniciativas frente al óptimo: el orden de llegada cuesta 1,80 veces de media y 2,61 en el percentil 95, lo más corto primero 1,30 y 1,66, el mayor costo de demora primero 1,13 y 1,26, y el costo de demora entre duración 1,00 y 1,00.',
                        ['Orden de llegada', 'Lo más corto primero', 'Mayor costo de demora primero', 'Costo de demora entre duración'],
                        [('Costo medio frente al óptimo', [1.80, 1.30, 1.13, 1.00], 'teal'), ('Peor caso (p95)', [2.61, 1.66, 1.26, 1.00], 'coral')],
                        unit='veces el costo del orden óptimo', decimals=2,
                        note='Esperar sin criterio cuesta un 80 % más que el óptimo de media y más del doble en una de cada veinte carteras; ordenar solo por valor o solo por duración recupera buena parte, pero no todo. La última categoría es 1,00 por construcción: es el orden que minimiza el costo.',
                        note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-537
def se453_valor_presente_y_orden() -> Fig:
    ts = [5, 10, 20, 30]
    return line_chart('Cuándo un proyecto deja de ser el mejor',
                      'Líneas con el valor actual neto de tres proyectos con inversión de 100 según la tasa de descuento: la plataforma interna es la mejor con 5 y 10 por ciento (88,0 y 49,0) y la peor con 20 y 30 (−3,5 y −35,4); automatizar el cierre pasa de 43,2 a −8,6 y rediseñar el módulo de 74,3 a −19,7, con lo que el orden se invierte.',
                      [('Plataforma interna', [(5, 88.0, '88,0', 'r'), (10, 49.0, '', 't'), (20, -3.5, '', 'b'), (30, -35.4, '−35,4', 'l')], 'coral'),
                       ('Rediseñar el módulo', [(5, 74.3, '74,3', 'r'), (10, 46.3, '', 't'), (20, 6.5, '', 't'), (30, -19.7, '−19,7', 'l')], 'gold'),
                       ('Automatizar el cierre', [(5, 43.2, '43,2', 'b'), (10, 29.2, '29,2', 'b'), (20, 7.4, '', 't'), (30, -8.6, '−8,6', 't')], 'teal')],
                      point_labels='none', x_label='Tasa de descuento (%)', y_label='Valor actual neto', x_ticks=[(t, f'{t} %') for t in ts], y_ticks=[-40, 0, 40, 80, 120], y_zero=False,
                      note='Valores con 10 % y 20 %: plataforma interna 49,0 y −3,5; rediseñar el módulo 46,3 y 6,5; automatizar el cierre 29,2 y 7,4. Suma sin descontar: 60, 110 y 140. TIR: 24,3 %, 22,1 % y 19,1 %; recuperación: año 2, año 4 y año 5. A tasas del 5 % y del 10 %, la plataforma interna es la mejor por VAN; a partir del 20 % pasa a ser la peor y el primero es «Automatizar el cierre». La suma sin descontar y el VAN a tasa baja favorecen lo tardío; la TIR y la recuperación favorecen lo temprano.',
                      note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-537
def se453_propio_nube_y_equilibrio() -> Fig:
    return case_cards('Propio o nube, y cuántas personas hacen falta',
                      'Cinco preguntas sobre servidores propios frente a nube como tarjetas: el cruce llega en el mes 33 sin descuento y en el 39 con una tasa mensual de 0,8 por ciento, el equilibrio es de 6 250 personas usuarias con márgenes de −86,7, 0, 30 y 63,3 por ciento, y alcanzarlo en 12 meses tiene probabilidad 0, 52,5 y 99,3 por ciento desde 2 000, 4 000 y 6 000.',
                      [('Mes en que lo propio acumula menos costo (sin descontar)', 'Mes 33', 'Antes de ese mes la nube cuesta menos.', 'gold'),
                       ('Mes con tasa mensual de 0,8 %', 'Mes 39', 'Descontar retrasa seis meses el cruce: la inversión inicial pesa más.', 'coral'),
                       ('Personas usuarias de equilibrio (20 000 / (4 − 0,8))', '6 250 personas', 'Separa un servicio que pierde de uno que gana.', 'teal'),
                       ('Margen con 3 000 · 6 250 · 10 000 · 30 000 personas', '−86,7 % · 0 % · 30,0 % · 63,3 %', 'El margen crece con cada persona por encima del equilibrio.', 'gold'),
                       ('Probabilidad de alcanzar el equilibrio en 12 meses desde 2 000 · 4 000 · 6 000', '0,0 % · 52,5 % · 99,3 %', 'Casi imposible desde 2 000, casi seguro desde 6 000.', 'coral')],
                      note='Descontar retrasa seis meses el cruce, porque la inversión inicial pesa más que las cuotas futuras. El equilibrio de 6 250 personas separa a un servicio que pierde de uno que gana, pero alcanzarlo en un año es casi imposible desde 2 000 personas y casi seguro desde 6 000.',
                      note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-538
def se454_entrevistas_y_eleccion() -> Fig:
    return grouped_bars('Qué eligen las entrevistas',
                        'Barras horizontales con la fracción de lo alcanzable que logra cada procedimiento de selección entre 10 candidaturas: una conversación libre 61,6 por ciento, tres libres 71,2, una entrevista estructurada 80,9, tres estructuradas 91,1 y elegir al azar 0, con habilidad media de la persona elegida de 0,95, 1,10, 1,25, 1,41 y 0.',
                        ['Una conversación libre (habilidad 0,95)', 'Tres conversaciones libres (1,10)', 'Una entrevista estructurada (1,25)', 'Tres entrevistas estructuradas (1,41)', 'Al azar (0,00)'],
                        [('Fracción de lo alcanzable (la mejor de las 10)', [61.6, 71.2, 80.9, 91.1, 0.0], 'teal')],
                        unit='% de la habilidad de la mejor candidatura', horizontal=True, label_w=330, decimals=1, ticks=[0, 25, 50, 75, 100],
                        note='Entre paréntesis, la habilidad media de la persona elegida. Añadir entrevistadoras ayuda, pero menos que estructurar: una estructurada (80,9 %) supera a tres libres (71,2 %), porque el halo compartido no se promedia.',
                        note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-538
def se454_verificador_de_portafolio() -> Fig:
    return stacked_bars('Qué comprueba un verificador de portafolio',
                        'Barras horizontales apiladas con las reglas cumplidas de seis por cuatro entradas sintéticas de portafolio: con evidencia 6, a medias 2 (faltan comando, límite, decisión con alternativa y versión), de adjetivos 0 y con relleno 6 sin tener sustancia.',
                        ['Con evidencia', 'A medias', 'De adjetivos', 'Con relleno'],
                        [('Reglas cumplidas', [6, 2, 0, 6], 'teal'), ('Reglas que faltan', [0, 4, 6, 0], 'coral')],
                        unit='reglas del verificador (de 6)', horizontal=True, label_w=160,
                        note='A la entrada a medias le faltan comando, límite, decisión y alternativa, y versión; a la de adjetivos, todo. El verificador separa con claridad las dos entradas extremas y distingue la que tiene la estructura incompleta. La última barra es el límite: una entrada con cifras, un comando y un enlace inventados cumple las seis reglas.',
                        note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-538
def se454_defensa_por_profundidad() -> Fig:
    return grouped_bars('Qué impresión deja cada estrategia de defensa',
                        'Barras horizontales con el porcentaje de errores seguros detectados en una persona que responde seis preguntas de profundidad creciente: con conocimiento de nivel 2 defender todo con seguridad se descubre en 98,4 por ciento de los casos y declarar el límite en 0; con nivel 4, 87,1 y 0; las impresiones medias son −4,8, 2,3, 0,56 y 4,3.',
                        ['Nivel 2 · defiende todo con seguridad (impresión −4,8)', 'Nivel 2 · declara su límite y propone cómo comprobar (2,3)', 'Nivel 4 · defiende todo con seguridad (0,56)', 'Nivel 4 · declara su límite y propone cómo comprobar (4,3)'],
                        [('Detectada en un error seguro', [98.4, 0.0, 87.1, 0.0], 'coral')],
                        unit='% de los casos con un error seguro detectado', horizontal=True, label_w=350, decimals=1, ticks=[0, 25, 50, 75, 100],
                        note='Entre paréntesis, la impresión media. Con conocimiento de nivel 4, defender todo deja una impresión cercana a cero; declarar el límite, de 4,3. Con nivel 2 la diferencia es mayor (−4,8 frente a 2,3), porque hay más preguntas en que inventar.',
                        note_kind='teal', foot=EJEC)

# ---------------------------------------------------------------- SE-539
def se455_resultado_o_proceso() -> Fig:
    ns = [5, 10, 20, 50, 100]
    return line_chart('Cuántas decisiones hacen falta para distinguir a quien decide mejor',
                      'Líneas con el porcentaje de veces que se identifica a la mejor decisora entre dos personas con calidad buena en 65 y 50 por ciento de los casos: por resultados de 56,3 por ciento con 5 decisiones a 73,6 con 100, y por calidad del proceso de 63,0 a 93,4.',
                      [('Por calidad del proceso', [(n, v, fmt_es(v, 1), 't') for n, v in zip(ns, [63.0, 67.9, 75.1, 85.0, 93.4])], 'teal'), ('Por resultados', [(n, v, fmt_es(v, 1), 'b') for n, v in zip(ns, [56.3, 57.6, 62.4, 67.9, 73.6])], 'coral')],
                      x_label='Decisiones por persona', y_label='Identifica a la mejor decisora (%)', log_x=True, x_ticks=[(n, str(n)) for n in ns], y_ticks=[50, 60, 70, 80, 90, 100], y_zero=False,
                      note='Con diez decisiones por persona, juzgar por resultados apenas supera el azar (57,6 %); incluso con cien decisiones, el 26 % de las veces se elige a la persona equivocada. Juzgar el proceso, aun con una auditoría imperfecta, acierta más con cualquier cantidad.',
                      note_kind='gold', foot=SINT)

# ---------------------------------------------------------------- SE-539
def se455_cobertura_de_un_panel() -> Fig:
    return grouped_bars('Qué cobertura logra un panel',
                        'Barras agrupadas con 5 000 revisiones sintéticas de 30 modos de fallo en tres dominios: cuatro revisoras del mismo dominio cubren el 58 por ciento de media y 31,5 el dominio peor cubierto; dos y dos de dos dominios 67,2 y 39,8; una generalista y tres de dominios distintos 71,0 y 58,8; la misma composición con ejercicio previo al fallo 83,2 y 73,1.',
                        ['4 revisoras del mismo dominio', '2 y 2 de dos dominios', 'Una generalista y tres de dominios distintos', 'La anterior, con ejercicio previo al fallo'],
                        [('Cobertura media', [58.0, 67.2, 71.0, 83.2], 'teal'), ('Dominio peor cubierto', [31.5, 39.8, 58.8, 73.1], 'coral')],
                        unit='% de los modos de fallo cubiertos', decimals=1, ticks=[0, 20, 40, 60, 80, 100],
                        note='La composición pesa más que el número de personas: cuatro del mismo dominio dejan un dominio con menos de un tercio cubierto, y una composición diversa lo sube a más de la mitad. El ejercicio previo al fallo suma otros doce puntos.',
                        note_kind='coral', foot=SINT)

# ---------------------------------------------------------------- SE-539
def se455_calibracion_y_brier() -> Fig:
    cs = [55, 65, 75, 85, 95]
    return line_chart('Qué dice la confianza declarada',
                      'Líneas con el acierto observado según la confianza declarada de 500 pronósticos de cada una de tres personas: la calibrada (Brier 0,175) acierta 94,4 por ciento cuando declara 95, la sobreconfiada (Brier 0,249) 74,4, y la que declara siempre 95 por ciento (Brier 0,317) acierta 65 por ciento, lejos de la diagonal de calibración perfecta.',
                      [('Calibración perfecta', [(c, c, '', 't') for c in cs], 'grey'), ('Calibrada (Brier 0,175)', [(c, v, fmt_es(v, 1), 't') for c, v in zip(cs, [53.5, 73.7, 69.0, 82.7, 94.4])], 'teal'),
                       ('Sobreconfiada (Brier 0,249)', [(c, v, fmt_es(v, 1), 'b') for c, v in zip(cs, [50.5, 69.7, 57.0, 65.5, 74.4])], 'coral'), ('Siempre 95 % (Brier 0,317)', [(95, 65.0, '65,0', 'b')], 'gold')],
                      point_labels='none', x_label='Confianza declarada (%)', y_label='Acierto observado (%)', x_ticks=[(c, str(c)) for c in cs], y_ticks=[40, 50, 60, 70, 80, 90, 100], y_zero=False,
                      note='La línea gris es la calibración perfecta: acierta lo que declara. La calibrada declara 95 % y acierta alrededor de 94 %; la sobreconfiada, con la misma declaración, acierta 74 %. La diferencia es invisible mientras nadie contrasta las probabilidades con los resultados.',
                      note_kind='teal', foot=SINT)

# ---------------------------------------------------------------- SE-540
def se456_verificador_de_dossier() -> Fig:
    return case_cards('Qué detecta el verificador',
                      'Seis variantes sintéticas de un dossier verificadas por un script como tarjetas: la completa no tiene defectos, la sin límites se detecta por tener menos de tres, la afirmación sin evidencia en C5, la evidencia alterada en C2, la evidencia borrada en C3, y la cifra distinta se detecta por el conflicto en el costo a cinco años pero no por la guardia de cinco o seis personas.',
                      [('Completo', 'Sin defectos detectados', 'No se introdujo ningún defecto.', 'teal'),
                       ('Sin límites: LIMITES.md sin límites', 'Detectado: menos de 3 límites', 'Señala el archivo exacto.', 'teal'),
                       ('Afirmación sin respaldo: C5 sin evidencia', 'Detectado: C5 sin evidencia', 'Señala la afirmación exacta.', 'teal'),
                       ('Evidencia alterada: e2.txt cambiado tras la huella', 'Detectado: C2 con evidencia alterada', 'La huella ya no coincide.', 'teal'),
                       ('Evidencia faltante: e3.txt borrado', 'Detectado: C3 con evidencia ausente', 'Señala la afirmación sin archivo.', 'teal'),
                       ('Cifra distinta: costo 1 020 frente a 1 200 y guardia 5 frente a 6', 'Detectado solo el conflicto TCO_5A', 'La guardia (5 frente a 6) no se vio: la cifra del README no estaba etiquetada.', 'coral')],
                      note='Cada variante tiene un defecto distinto y el verificador lo señala con la afirmación o el archivo exactos. La última tarjeta muestra el límite: se introdujeron dos incoherencias y se detectó una; la otra (personas de guardia, 5 en riesgos y 6 en el README) no se vio porque la cifra del README no estaba etiquetada.',
                      note_kind='gold', foot=EJEC)

# ---------------------------------------------------------------- SE-540
def se456_probabilidad_de_ser_vista() -> Fig:
    ns = [3, 5, 8, 12]
    return line_chart('Cuánto se encuentra al muestrear',
                      'Líneas con la probabilidad exacta de que una revisora encuentre al menos una afirmación sin respaldo en un dossier de 30 según las inspeccionadas: con 1 sin respaldo es 10,0, 16,7, 26,7 y 40,0 por ciento con 3, 5, 8 y 12; con 3 sin respaldo 28,0, 43,3, 62,1 y 79,9; con 6 sin respaldo 50,1, 70,2, 87,4 y 96,9.',
                      [('6 de 30 sin respaldo', [(n, v, fmt_es(v, 1), 't') for n, v in zip(ns, [50.1, 70.2, 87.4, 96.9])], 'teal'), ('3 de 30 sin respaldo', [(n, v, fmt_es(v, 1), 'b') for n, v in zip(ns, [28.0, 43.3, 62.1, 79.9])], 'gold'),
                       ('1 de 30 sin respaldo', [(n, v, fmt_es(v, 1), 'b') for n, v in zip(ns, [10.0, 16.7, 26.7, 40.0])], 'coral')],
                      x_label='Afirmaciones inspeccionadas', y_label='Probabilidad de encontrar al menos una (%)', x_ticks=[(n, str(n)) for n in ns], y_ticks=[0, 20, 40, 60, 80, 100],
                      note='Una sola afirmación sin respaldo entre treinta supera el 25 % de probabilidad de ser vista solo si se inspeccionan ocho. Para encontrar con 80 % un problema de tres afirmaciones hay que inspeccionar doce.',
                      note_kind='coral', foot=EJEC)

# ---------------------------------------------------------------- SE-540
def se456_hora_de_revision() -> Fig:
    return percentile_intervals('Cuántas afirmaciones se comprueban en una hora',
                                'Rangos de las afirmaciones comprobadas en 5 000 revisiones simuladas de 60 minutos sobre un dossier de 30 afirmaciones: sin trazabilidad 5,7 de media, entre 4 y 7 en los percentiles 10 y 90; con una tabla de afirmación, evidencia y huella 21,7, entre 19 y 24.',
                                [('Sin trazabilidad', [4, 5.7, 7]), ('Con tabla afirmación–evidencia–huella', [19, 21.7, 24])],
                                unit='afirmaciones comprobadas en 60 minutos', marks=('p10', 'media', 'p90'), decimals=1, label_w=300,
                                note='La tabla multiplica por casi cuatro lo que se puede comprobar en una hora; incluso así, no se llega a las treinta, por lo que el verificador automático sigue siendo necesario.',
                                note_kind='teal', foot=EJEC)

FIGURES = {
    "se-535-pesos-y-ganador.svg": se451_pesos_y_ganador,
    "se-535-comprar-o-construir.svg": se451_comprar_o_construir,
    "se-535-cadena-de-disponibilidad.svg": se451_cadena_de_disponibilidad,
    "se-536-licencias-y-politica.svg": se452_licencias_y_politica,
    "se-536-firma-de-origen.svg": se452_firma_de_origen,
    "se-536-costo-del-patron-oscuro.svg": se452_costo_del_patron_oscuro,
    "se-537-orden-y-costo-de-demora.svg": se453_orden_y_costo_de_demora,
    "se-537-valor-presente-y-orden.svg": se453_valor_presente_y_orden,
    "se-537-propio-nube-y-equilibrio.svg": se453_propio_nube_y_equilibrio,
    "se-538-entrevistas-y-eleccion.svg": se454_entrevistas_y_eleccion,
    "se-538-verificador-de-portafolio.svg": se454_verificador_de_portafolio,
    "se-538-defensa-por-profundidad.svg": se454_defensa_por_profundidad,
    "se-539-resultado-o-proceso.svg": se455_resultado_o_proceso,
    "se-539-cobertura-de-un-panel.svg": se455_cobertura_de_un_panel,
    "se-539-calibracion-y-brier.svg": se455_calibracion_y_brier,
    "se-540-verificador-de-dossier.svg": se456_verificador_de_dossier,
    "se-540-probabilidad-de-ser-vista.svg": se456_probabilidad_de_ser_vista,
    "se-540-hora-de-revision.svg": se456_hora_de_revision,
}
