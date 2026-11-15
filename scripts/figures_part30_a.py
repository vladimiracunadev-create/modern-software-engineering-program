"""Figures for SE-361 to SE-366 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab

SINT = "Datos sintéticos y modelos del autor con semilla fija; Windows (CPython 3.12.9) y Ubuntu (WSL2, 3.12.3) con cifras idénticas."


# ---------------------------------------------------------------- SE-361
def se361_presupuesto() -> Fig:
    items = [
        ("Sin pruebas", 100.0, "coral", "100 % (16,00)"),
        ("Reparto uniforme (4 h por componente)", 50.5, "gold", "50,5 % (8,08)"),
        ("Proporcional al tamaño del código", 57.8, "coral", "57,8 % (9,24)"),
        ("Proporcional a probabilidad × impacto", 43.6, "teal", "43,6 % (6,98)"),
        ("Marginal (óptimo del modelo)", 42.7, "teal", "42,7 % (6,83)"),
    ]
    return bars("Pérdida esperada residual con 40 horas de pruebas repartidas de cinco maneras",
                "Barras con la pérdida esperada que queda como porcentaje de la pérdida sin pruebas: 100 por ciento sin pruebas, 50,5 con reparto uniforme, 57,8 proporcional al tamaño, 43,6 proporcional a probabilidad por impacto y 42,7 con el reparto marginal.",
                items, 5.0, "Repartir por tamaño es peor que repartir por igual (57,8 % frente a 50,5 %) porque el código más grande no es el más arriesgado. El reparto marginal pone 9,2 h en plazos y zonas horarias y 0,7 h en autenticación, cuyo impacto es 10: el modelo minimiza la pérdida esperada, no garantiza que lo catastrófico quede cubierto.",
                label_w=360, width=980, note_kind="gold", foot=SINT)


def se361_sensibilidad() -> Fig:
    rows = [
        ["Uniforme", "1,271", "1,455", "1,955"],
        ["Proporcional al tamaño", "1,441", "1,735", "2,382"],
        ["Proporcional a probabilidad × impacto", "1,128", "1,212", "1,460"],
        ["Marginal con las estimaciones", "1,101", "1,178", "1,396"],
    ]
    return tab("Pérdida real dividida por la pérdida del plan óptimo cuando las estimaciones se equivocan hasta un factor 2",
               "Tabla: con 5 000 realidades en las que probabilidad e impacto de cada componente se multiplican por un factor entre 0,5 y 2, el reparto por riesgo pierde en mediana 1,128 veces el óptimo y el uniforme 1,271 veces; el tamaño llega a 1,441. El reparto por riesgo supera al uniforme en 97,2 por ciento de las realidades.",
               ["Estrategia (se planea con las estimaciones)", "Mediana", "Percentil 90", "Máximo"], rows, [430, 130, 150, 130], row_h=48, size=13,
               note="Equivocarse por un factor 2 en cada estimación no invalida el reparto por riesgo: gana al uniforme en el 97,2 % de las 5 000 realidades. Lo que sí cambia es el ranking: el trío de componentes más arriesgados difiere del estimado en el 74,2 % de ellas. El plan es una hipótesis que se revisa, no un resultado.",
               note_kind="teal", foot=SINT)


def se361_niveles() -> Fig:
    rows = [
        ["Unitaria", "0,1", "lógica pura, frontera de datos", "2 de 8"],
        ["Contrato", "1", "contrato entre servicios", "1 de 8"],
        ["Integración", "2", "frontera de datos, contrato, configuración", "3 de 8"],
        ["De extremo a extremo", "30", "configuración, recorrido de usuario, accesibilidad", "3 de 8"],
        ["Exploratoria", "45", "recorrido de usuario, accesibilidad, concurrencia", "3 de 8"],
        ["De carga", "60", "concurrencia, rendimiento", "2 de 8"],
    ]
    return tab("Qué clases de fallo puede ver cada nivel de prueba (matriz del autor, costo por ejecución en minutos)",
               "Tabla: seis niveles de prueba con su costo supuesto por ejecución y las clases de fallo que pueden ver; ninguno cubre las ocho clases, las unitarias cubren dos y el conjunto más barato que cubre las ocho (unitaria, contrato, extremo a extremo y carga) cuesta 91,1 minutos.",
               ["Nivel", "Minutos", "Clases de fallo que puede ver", "Cubre"], rows, [200, 100, 460, 110], row_h=48, size=13,
               note="El conjunto más barato que cubre las ocho clases combina unitaria, contrato, extremo a extremo y carga (91,1 minutos). Sumar unitaria, integración y contrato cubre solo cuatro clases: ninguna cantidad de pruebas rápidas ve concurrencia, rendimiento, accesibilidad ni el recorrido del usuario. La matriz es un supuesto del autor.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-362
def se362_costuras() -> Fig:
    rows = [
        ["cerrar_y_avisar (antes)", "DB, dt, smtplib", "DB.execute, dt.datetime.now, smtplib.SMTP().sendmail", "Base, reloj y correo reales"],
        ["calcular_nota", "ninguno", "ninguna", "Función pura: entrada y salida"],
        ["horas_tarde", "ninguno", "total_seconds sobre sus argumentos", "El reloj llega como parámetro"],
        ["cerrar (después)", "calcular_nota, horas_tarde", "ninguna externa", "Base y correo entran como funciones"],
    ]
    return tab("Dependencias ocultas de una función antes y después de hacerla testable (análisis con ast)",
               "Tabla: la función original lee tres nombres globales (base de datos, reloj y correo) y llama a servicios reales; tras separar el cálculo, la hora y los efectos, la función de nota no tiene dependencias y la de cierre recibe la hora, el guardado y el aviso como argumentos.",
               ["Función", "Nombres libres", "Llamadas a lo externo", "Qué hace falta para probarla"], rows, [210, 170, 290, 250], row_h=60, size=12,
               note="Cada nombre libre es una costura que una prueba debe reemplazar o soportar. La función original no se puede ejecutar sin una base, un reloj y un servidor de correo; la versión refactorizada se prueba con valores. La medida cuenta dependencias en el código, no la calidad del diseño.",
               note_kind="teal", foot=SINT)


def se362_mutantes() -> Fig:
    rows = [
        ["5 casos típicos", "5", "100 %", "9 de 16", "7 (1 equivalente)"],
        ["14 casos con fronteras", "14", "100 %", "13 de 16", "3 (1 equivalente)"],
    ]
    return tab("Dos baterías de pruebas sobre la misma función de nota: ambas ejecutan todas las líneas",
               "Tabla: la batería de cinco casos típicos y la de catorce casos con fronteras recorren el 100 por ciento de las líneas de la función; la primera mata 9 de 16 mutantes y la segunda 13 de 16, y entre los tres que sobreviven hay uno equivalente y dos que señalan casos sin probar.",
               ["Batería", "Casos", "Líneas ejecutadas", "Mutantes muertos", "Sobreviven"], rows, [250, 90, 170, 190, 200], row_h=48, size=13,
               note="Las dos baterías tienen la misma cobertura de líneas y detectan cantidades muy distintas de cambios. Con las fronteras sobreviven un mutante equivalente (el tope 7,0 nunca se alcanza porque el factor no supera 1) y dos reales: el borde 0 frente a 1 hora de atraso y los decimales del redondeo, que ningún caso distingue.",
               note_kind="coral", foot=SINT)


def se362_reloj() -> Fig:
    rows = [
        ["Reloj real, margen de 1 s entre construir el plazo y comprobar", "173 de 10 000 (1,73 %)", "Depende de pausas del equipo"],
        ["Reloj inyectado, 5 casos de frontera (−1 s, 0, +1 s, +24 h, +24 h 1 s)", "0 de 10 000", "Determinista por construcción"],
    ]
    return tab("Una prueba de plazos con el reloj real y con el reloj como parámetro",
               "Tabla: una prueba que construye el plazo con el reloj real y comprueba un segundo después falla en 173 de 10 000 ejecuciones simuladas por pausas ocasionales; la misma lógica con la hora inyectada prueba sin azar las cinco fronteras del plazo.",
               ["Variante de la prueba", "Fallos", "Origen"], rows, [480, 230, 210], row_h=64, size=12,
               note="El 1,73 % viene de un modelo del autor (3 de cada 100 ejecuciones sufren una pausa de 0,5 a 3 s), no de una medición del equipo. La lección es el mecanismo: una prueba que depende de cuánto tarda la máquina falla a veces sin que haya un defecto, y con la hora inyectada la hora deja de ser una variable.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-363
def se363_matriz() -> Fig:
    rows = [
        ["Renombrar nota por calificación", "Sí", "No", "Sí", "Sí", "Sí"],
        ["Nota de número a texto", "Sí", "No", "Sí", "Sí", "No"],
        ["Estado nulo", "Sí", "No", "Sí", "Sí", "No"],
        ["Valor nuevo en el enum de estado", "Sí", "No", "Sí", "Sí", "No"],
        ["Orden de la lista invertido", "Sí", "No", "No", "Sí", "No"],
        ["Primera página con 1 de 2 elementos", "Sí", "No", "Sí", "Sí", "No"],
        ["Campo extra «revisor»", "No", "No", "No", "No", "Sí (falsa alarma)"],
        ["Fecha con espacio en vez de «T»", "No", "No", "No", "No", "No"],
    ]
    return tab("Ocho cambios del proveedor frente a cuatro pruebas del consumidor",
               "Tabla: de ocho cambios, seis rompen al panel; el doble escrito a mano no detecta ninguno, el contrato del consumidor detecta cinco, la prueba contra la respuesta real detecta los seis y la comparación del esquema completo detecta uno y da una falsa alarma con el campo extra.",
               ["Cambio del proveedor", "¿Rompe el panel?", "Doble fijo", "Contrato", "Respuesta real", "Esquema completo"], rows, [300, 105, 100, 105, 125, 170], row_h=36, size=12,
               note="El contrato no detecta el orden invertido porque no lo declara, y la prueba contra la respuesta real lo ve porque el panel espera un orden. Un contrato solo protege lo que afirma. Los ocho cambios son construcciones del autor sobre una respuesta JSON y una base SQLite en memoria.",
               note_kind="teal", foot=SINT)


def se363_dirigidos() -> Fig:
    rows = [
        ["Quitar «creada»", "Alarma", "exportador"],
        ["Renombrar «nota»", "Alarma", "panel, exportador"],
        ["Cambiar el tipo de «id»", "Alarma", "exportador"],
        ["Quitar «estado»", "Alarma", "panel, avisos"],
        ["Cambiar «estudiante»", "Alarma", "panel, exportador, avisos"],
        ["Cambiar el tipo de «creada»", "Alarma", "exportador"],
        ["Quitar «pagina»", "Alarma", "nadie (falsa alarma)"],
        ["Renombrar «total»", "Alarma", "nadie (falsa alarma)"],
        ["Quitar «revisor», que no existe", "Sin alarma", "nadie"],
        ["Añadir un campo", "Sin alarma", "nadie (compatible)"],
    ]
    return tab("Comparar todo el esquema o solo lo que cada consumidor usa: tres consumidores y diez cambios",
               "Tabla: ocho alarmas del diff de esquema completo, de las cuales seis afectan al menos a un consumidor y dos no afectan a ninguno; los contratos por consumidor señalan quién se rompe en cada cambio.",
               ["Cambio del proveedor", "Diff de esquema completo", "Consumidores afectados"], rows, [300, 250, 340], row_h=36, size=12,
               note="El diff de esquema acierta siempre que hay un consumidor afectado y señala dos cambios que nadie usa. Los contratos por consumidor no los señalan, y además dicen a quién avisar. Para que funcione, cada consumidor debe declarar los campos que lee: el contrato incompleto produce un falso sentimiento de seguridad.",
               note_kind="gold", foot=SINT)


def se363_localizacion() -> Fig:
    items = [
        ("Recorridos de extremo a extremo (3)", 2.71, "coral", "2,71 interfaces sospechosas de media"),
        ("Una prueba por interfaz (7)", 1.0, "teal", "1 interfaz sospechosa"),
    ]
    return bars("Interfaces sospechosas tras el primer fallo: 1 000 defectos de interfaz sorteados en 7 interfaces",
                "Barras: con tres recorridos de extremo a extremo, un defecto de interfaz deja en promedio 2,71 interfaces sospechosas, y en 857 de 1 000 casos son tres; con una prueba por interfaz la sospechosa es una.",
                items, 120.0, "En el sistema modelado, 857 de 1 000 defectos dejan tres interfaces sospechosas (los recorridos solo ven el camino entero) y 143 dejan una (el tramo común del recorrido). Siete pruebas de interfaz localizan el defecto; tres recorridos no. El grafo de siete componentes y tres recorridos es un modelo del autor.",
                label_w=380, width=1000, note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-364
def se364_pasos() -> Fig:
    rows = [
        ["0,1 %", "99,7", "99,3", "98,4", "97,0"],
        ["0,5 %", "98,5", "96,1", "92,5", "85,7"],
        ["1 %", "96,7", "92,3", "86,1", "73,5"],
        ["2 %", "94,2", "85,3", "73,8", "55,3"],
    ]
    return tab("Porcentaje de ejecuciones limpias de un recorrido según su cantidad de pasos y la inestabilidad de cada paso",
               "Tabla: un recorrido de 30 pasos con una inestabilidad de 2 por ciento por paso pasa limpio solo 55,3 por ciento de las veces; con 0,1 por ciento por paso pasa 97,0 por ciento. Una suite de 20 recorridos de 15 pasos con 0,5 por ciento por paso pasa limpia 22,5 por ciento de las veces.",
               ["Fallo espurio por paso", "3 pasos", "8 pasos", "15 pasos", "30 pasos"], rows, [250, 140, 140, 140, 140], row_h=44, size=13,
               note="El resultado sigue (1 − q)^k: un paso inestable no se nota y treinta sí. Una suite de 20 recorridos de 15 pasos con 0,5 % por paso (simulación: 22,45 %; teoría: 22,2 %) pasa limpia una de cada cuatro veces. Los porcentajes son de una simulación con semilla fija, no de un sistema.",
               note_kind="coral", foot=SINT)


def se364_cobertura() -> Fig:
    rows = [
        ["1", "48,3 % / 45,1 %", "46,0 % / 55,5 %"],
        ["2", "64,9 % / 71,1 %", "59,0 % / 72,0 %"],
        ["3", "74,9 % / 77,8 %", "71,6 % / 82,6 %"],
        ["5", "87,6 % / 89,6 %", "86,7 % / 93,7 %"],
        ["8", "98,0 % / 98,5 %", "97,8 % / 99,5 %"],
    ]
    return tab("Tráfico y riesgo cubiertos por k recorridos de hasta tres rutas (20 000 sesiones sintéticas, 25 rutas)",
               "Tabla: con un recorrido se cubre 48,3 por ciento del tráfico y 45,1 por ciento del riesgo eligiendo por tráfico; con cinco recorridos se cubre 87,6 por ciento del tráfico, y elegir por tráfico por impacto sube el riesgo cubierto a 93,7 por ciento con cinco.",
               ["Recorridos", "Elegidos por tráfico (tráfico / riesgo)", "Elegidos por tráfico × impacto (tráfico / riesgo)"], rows, [150, 370, 400], row_h=44, size=13,
               note="Cinco recorridos cubren el 87 % del tráfico y el 90 % del riesgo; los ocho siguientes aportan menos. Elegir por tráfico multiplicado por impacto cede 1 punto de tráfico y gana 4 de riesgo con cinco recorridos. Las rutas, su frecuencia (Zipf 1,1) y sus impactos son supuestos del autor.",
               note_kind="teal", foot=SINT)


def se364_instantanea() -> Fig:
    rows = [
        ["Cambios benignos (7)", "Falla en 7", "Falla en 0"],
        ["Defectos de contenido y estructura (6)", "Detecta 6", "Detecta 6"],
        ["Defectos de estilo o de estado (3)", "Detecta 3", "Detecta 0"],
        ["Precisión de las alarmas", "9 de 16 (56 %)", "6 de 6 (100 %)"],
        ["Cobertura de los defectos", "9 de 9", "6 de 9"],
    ]
    return tab("Instantánea del HTML frente a aserciones semánticas, sobre 7 cambios benignos y 9 defectos",
               "Tabla: la instantánea exacta falla en los siete cambios benignos y detecta los nueve defectos, con una precisión de 56 por ciento; las aserciones semánticas no fallan en ninguno de los benignos y detectan seis de nueve, sin ver el botón deshabilitado, la lista oculta ni el texto con el color del fondo.",
               ["Resultado", "Instantánea exacta", "Aserciones semánticas"], rows, [400, 260, 260], row_h=44, size=13,
               note="Si el equipo aprueba cada diferencia de la instantánea sin leerla, acepta los nueve defectos con la misma facilidad que los siete cambios benignos. Las aserciones semánticas no ven lo que está en atributos de estilo. Hace falta una comprobación de lo visual aparte; esta figura no la mide.",
               note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-365
def se365_hasta_el_fallo() -> Fig:
    rows = [
        ["Correcto", "no detecta", "0 de 100", "0 de 100 (sin falsas alarmas)"],
        ["Olvida el resto", "detecta", "100 de 100 (mediana 1)", "100 de 100"],
        ["Resto al último corrector", "no detecta", "100 de 100 (mediana 1)", "100 de 100"],
        ["Falla solo si hay menos entregas que correctores", "no detecta", "87 de 100 (mediana 66)", "100 de 100"],
        ["Pierde una entrega si n ≥ 500", "no detecta", "100 de 100 (mediana 4)", "100 de 100"],
    ]
    return tab("Cinco versiones de «repartir n entregas entre k correctores» frente a cinco ejemplos y a cuatro propiedades",
               "Tabla: cinco ejemplos escritos a mano detectan solo una de las cuatro versiones defectuosas; las propiedades con generador uniforme detectan las cuatro, una de ellas solo en 87 de 100 semillas, y un generador con 30 por ciento de casos cerca de la frontera la detecta en las 100.",
               ["Versión", "5 ejemplos", "Propiedades, generador uniforme", "Con 30 % de casos cerca de la frontera"], rows, [330, 120, 250, 250], row_h=48, size=12,
               note="Las propiedades son longitud igual a k, suma igual a n, diferencia máxima de 1 y ninguna cantidad negativa. El defecto que solo ocurre con n < k aparece en el 1 % de los casos uniformes y por eso necesita más casos: la calidad del generador es parte de la prueba. Cada celda es el resultado de 100 semillas.",
               note_kind="teal", foot=SINT)


def se365_reduccion() -> Fig:
    items = [
        ("Contraejemplo sin reducir (caracteres)", 155.3, "coral", "155,3 de media"),
        ("Contraejemplo reducido (caracteres)", 20.9, "teal", "20,9 de media"),
        ("Secuencia de 40 operaciones sin reducir", 40.0, "coral", "40"),
        ("Secuencia reducida (operaciones)", 9.7, "teal", "9,7 de media (9 a 12)"),
    ]
    return bars("Reducción (shrinking) de contraejemplos: 100 listas de nombres y 106 secuencias de operaciones",
                "Barras: un contraejemplo de una lista de nombres pasa de 155,3 caracteres a 20,9 tras reducirlo; una secuencia fallida de 40 operaciones sobre una cola pasa a 9,7 operaciones de media, entre 9 y 12.",
                items, 3.0, "El tamaño mínimo de la lista (unos 21 caracteres) viene del defecto: truncar a 20 solo aparece si el nombre tiene más de 20. La secuencia mínima de 9 operaciones es el estado que la cola necesita para llegar a la compactación defectuosa. Sin reducir, el contraejemplo es un ruido que nadie diagnostica.",
                label_w=360, width=980, note_kind="gold", foot=SINT)


def se365_modelo() -> Fig:
    items = [
        ("Longitud 3, 5 u 8", 0.0, "coral", "0 %"),
        ("Longitud 12", 24.7, "gold", "24,7 %"),
        ("Longitud 20", 54.7, "teal", "54,7 %"),
        ("Longitud 40", 54.8, "teal", "54,8 %"),
        ("Cuatro secuencias manuales", 0.0, "coral", "0 de 4"),
    ]
    return bars("Fracción de secuencias aleatorias que descubren el defecto de la cola, según su longitud (5 000 por barra)",
                "Barras: ninguna secuencia de hasta 8 operaciones descubre el defecto de la cola frente al modelo; con longitud 12 lo descubre 24,7 por ciento, y con 20 o 40 cerca de 55 por ciento; cuatro secuencias manuales no lo detectan.",
                items, 6.5, "La cola real pierde un elemento al compactar tras sacar tres, solo si quedan más de cuatro. Hace falta una secuencia de al menos 9 operaciones, y el 55 % de techo viene de que muchas secuencias largas cambian el estado antes de alcanzar la condición. Las pruebas por ejemplo de 2 a 6 operaciones nunca llegan.",
                label_w=280, width=940, note_kind="teal", foot=SINT)


# ---------------------------------------------------------------- SE-366
def se366_puntuacion() -> Fig:
    rows = [
        ["A: 3 casos del camino feliz", "3", "72,2 %", "11 de 18", "61,1 %"],
        ["B: A + 4 rechazos de formato", "7", "94,4 %", "11 de 18", "61,1 %"],
        ["C: B + bordes y exclusiones", "14", "100 %", "17 de 18", "94,4 %"],
        ["D: una prueba sin aserciones", "1", "66,7 %", "6 de 18", "33,3 %"],
    ]
    return tab("Cobertura de líneas y puntuación de mutación de cuatro baterías sobre el mismo módulo (18 mutantes)",
               "Tabla: pasar de la batería A a la B sube la cobertura de líneas de 72,2 a 94,4 por ciento y no cambia los mutantes muertos, que son 11 de 18; la batería C llega al 100 por ciento de líneas y mata 17 de 18; una sola prueba sin aserciones cubre 66,7 por ciento de las líneas y mata 6 de 18, todos por excepción.",
               ["Batería", "Casos", "Líneas ejecutadas", "Mutantes muertos", "Puntuación"], rows, [310, 90, 170, 160, 160], row_h=44, size=13,
               note="La batería B añade 22 puntos de cobertura y 0 mutantes muertos. La D alcanza dos tercios de las líneas sin una sola aserción. El único superviviente de C cambia el redondeo de 1 a 2 decimales y ningún promedio de los casos lo distingue. Las baterías y los 18 mutantes son del autor; ninguno es equivalente.",
               note_kind="coral", foot=SINT)


def se366_fuzzing() -> Fig:
    rows = [
        ["Nombre de más de 30 caracteres", "0 de 20", "20 de 20 (31)", "20 de 20 (317)"],
        ["Nombre vacío con nota 7,0", "0 de 20", "20 de 20 (101)", "15 de 20 (4 346)"],
        ["Identificador > 99 999 y estado anulada", "0 de 20", "20 de 20 (78)", "16 de 20 (6 826)"],
        ["Nota «nan» o «inf»", "0 de 20", "20 de 20 (43)", "20 de 20 (210)"],
    ]
    return tab("Cuatro defectos escondidos en un analizador: semillas que los hallan y mediana de entradas (20 semillas, 20 000 entradas)",
               "Tabla: el fuzzing con cadenas aleatorias no halló ninguno de los cuatro defectos; el generador que respeta los cuatro campos y usa valores límite los halló en las 20 semillas con medianas de 31 a 101 entradas; el guiado por cobertura que muta entradas previas los halló en 15 a 20 semillas con medianas de 210 a 6 826 entradas.",
               ["Defecto", "Bytes aleatorios", "Estructurado con valores límite", "Guiado por cobertura"], rows, [330, 150, 230, 210], row_h=44, size=12,
               note="Las cadenas aleatorias casi nunca forman cuatro campos con un identificador numérico, así que nunca llegan al código que falla. El generador estructurado conoce los valores límite del formato, y ese conocimiento es del autor: el resultado muestra el mecanismo y no la tasa de hallazgo de una herramienta real.",
               note_kind="gold", foot=SINT)


def se366_supervivientes() -> Fig:
    rows = [
        ["«or» por «and» en el rango de la nota", "Ningún caso trae una nota fuera de rango hasta la comparación", "0,9 o 7,1 deben rechazarse"],
        ["Límite inferior de 1,0 a 2,0, o «<» por «<=»", "Ningún caso usa la nota 1,0 exacta", "1,0 debe aceptarse"],
        ["Límite superior de 7,0 a 8,0", "Ningún caso usa una nota apenas sobre 7,0", "7,1 debe rechazarse"],
        ["«>» por «>=» en el límite superior", "Ningún caso usa la nota 7,0 exacta", "7,0 debe aceptarse"],
        ["«and» por «or» al excluir anuladas", "Ninguna entrada mezcla una anulada con nota", "Anulada con nota 2,0 entre válidas"],
        ["Redondeo de 1 a 2 decimales", "Todos los promedios probados tienen un decimal", "Promedio de tres notas, como 5,33"],
    ]
    return tab("Mutantes que sobreviven a la batería B (7 de 18) y el caso que los mata",
               "Tabla: siete mutantes sobreviven a la batería B, agrupados en seis causas; la batería C los mata todos salvo el cambio del redondeo de uno a dos decimales.",
               ["Mutante que sobrevive", "Por qué sobrevive", "Caso que lo mata"], rows, [350, 330, 240], row_h=52, size=12,
               note="Un mutante superviviente es una pregunta, no un veredicto: o falta un caso o el mutante es equivalente y no hay nada que probar. Aquí ninguno es equivalente, de modo que cada uno señala una prueba concreta que falta; los dos del límite inferior cuentan como una misma causa.",
               note_kind="teal", foot=SINT)


FIGURES = {
    "se-361-presupuesto-de-pruebas-por-estrategia.svg": se361_presupuesto,
    "se-361-sensibilidad-a-las-estimaciones.svg": se361_sensibilidad,
    "se-361-niveles-de-prueba-y-clases-de-fallo.svg": se361_niveles,
    "se-362-dependencias-ocultas-de-una-funcion.svg": se362_costuras,
    "se-362-cobertura-y-mutantes-muertos.svg": se362_mutantes,
    "se-362-reloj-real-frente-a-reloj-inyectado.svg": se362_reloj,
    "se-363-cambios-del-proveedor-y-pruebas.svg": se363_matriz,
    "se-363-contratos-por-consumidor.svg": se363_dirigidos,
    "se-363-localizar-un-defecto-de-interfaz.svg": se363_localizacion,
    "se-364-inestabilidad-por-pasos.svg": se364_pasos,
    "se-364-recorridos-criticos-elegidos.svg": se364_cobertura,
    "se-364-instantanea-o-aserciones.svg": se364_instantanea,
    "se-365-casos-hasta-el-primer-fallo.svg": se365_hasta_el_fallo,
    "se-365-reduccion-de-contraejemplos.svg": se365_reduccion,
    "se-365-secuencias-contra-un-modelo.svg": se365_modelo,
    "se-366-cobertura-frente-a-mutacion.svg": se366_puntuacion,
    "se-366-fuzzing-de-un-analizador.svg": se366_fuzzing,
    "se-366-mutantes-que-sobreviven.svg": se366_supervivientes,
}
