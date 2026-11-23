"""Figures for SE-421 to SE-426 (synthetic data, fixed seeds; Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3)."""
from __future__ import annotations

from figure_kit import Fig, _kit_finish, _kit_start, grouped_bars, heatmap, line_chart, percentile_intervals
from figures_part07_a import bars

SINT = "Datos sintéticos y modelos del autor con semilla fija; Windows (CPython 3.12.9) y Ubuntu (WSL2, 3.12.3) con cifras idénticas."


# ---------------------------------------------------------------- SE-421
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
    return percentile_intervals(
        "Pérdida real frente a la del plan óptimo cuando las estimaciones se equivocan hasta un factor 2 (5 000 realidades)",
        "Intervalos con la mediana, el percentil 90 y el máximo de la razón entre la pérdida del plan y la del óptimo para cuatro estrategias: el reparto por probabilidad por impacto y el marginal quedan entre 1,10 y 1,46 veces el óptimo, el uniforme llega a 1,955 y el proporcional al tamaño a 2,382.",
        [("Uniforme", [1.271, 1.455, 1.955]),
         ("Proporcional al tamaño", [1.441, 1.735, 2.382]),
         ("Proporcional a probabilidad × impacto", [1.128, 1.212, 1.460]),
         ("Marginal con las estimaciones", [1.101, 1.178, 1.396])],
        unit="veces la pérdida del plan óptimo (1 = el óptimo de esa realidad)", marks=("mediana", "p90", "máx"), decimals=3,
        label_w=260,
        note="Equivocarse por un factor 2 en cada estimación no invalida el reparto por riesgo: gana al uniforme en el 97,2 % de las 5 000 realidades. Lo que sí cambia es el ranking: el trío de componentes más arriesgados difiere del estimado en el 74,2 % de ellas. El plan es una hipótesis que se revisa, no un resultado.",
        note_kind="teal", foot=SINT)


def se361_niveles() -> Fig:
    clases = ["Lógica pura", "Frontera de datos", "Contrato", "Configuración", "Recorrido de usuario", "Accesibilidad", "Concurrencia", "Rendimiento"]
    vistas = {
        "Unitaria · 0,1 min": {0, 1},
        "Contrato · 1 min": {2},
        "Integración · 2 min": {1, 2, 3},
        "Extremo a extremo · 30 min": {3, 4, 5},
        "Exploratoria · 45 min": {4, 5, 6},
        "De carga · 60 min": {6, 7},
    }
    values = [[1.0 if j in s else None for j in range(8)] for s in vistas.values()]
    return heatmap(
        "Qué clases de fallo puede ver cada nivel de prueba (matriz del autor y costo por ejecución)",
        "Mapa de calor de seis niveles de prueba frente a ocho clases de fallo: ningún nivel cubre las ocho, la lógica pura solo la ve la prueba unitaria y el rendimiento solo la carga; el conjunto más barato que cubre las ocho (unitaria, contrato, extremo a extremo y carga) cuesta 91,1 minutos.",
        list(vistas), clases, values, unit="ve = el nivel puede ver esa clase de fallo; no = no la ve", scale="teal", vmin=0, vmax=1,
        cell_fmt=lambda v: "ve" if v else "no", width=1000, cell_h=44, label_w=230,
        note="El conjunto más barato que cubre las ocho clases combina unitaria, contrato, extremo a extremo y carga (91,1 minutos). Sumar unitaria, integración y contrato cubre solo cuatro clases: ninguna cantidad de pruebas rápidas ve concurrencia, rendimiento, accesibilidad ni el recorrido del usuario. La matriz es un supuesto del autor.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-422
def se362_costuras() -> Fig:
    f, y = _kit_start("Las dependencias ocultas de cerrar_y_avisar antes y después de separar cálculo, hora y efectos",
                      "Diagrama de dos mitades: antes, la función cerrar_y_avisar llama directamente a la base, al reloj y al servidor de correo reales; después, calcular_nota y horas_tarde son funciones puras y cerrar recibe la hora, el guardado y el aviso como argumentos.",
                      940, None)
    top = y + 4
    f.group(10, top, 440, 262, "Antes: tres nombres libres", "coral")
    f.box(28, top + 100, 150, 70, "cerrar_y_avisar", "coral", 14, bold=True)
    for i, label in enumerate(["DB.execute: base real", "dt.datetime.now: reloj real", "smtplib.SMTP().sendmail: correo real"]):
        by = top + 44 + i * 70
        f.box(238, by, 198, 56, label, "coral", 13)
        f.arrow([(178, top + 135), (238, by + 28)])
    f.group(470, top, 460, 262, "Después: costuras en los argumentos", "teal")
    f.box(486, top + 50, 170, 52, "calcular_nota: función pura", "teal", 13)
    f.box(486, top + 114, 170, 52, "horas_tarde: recibe el reloj", "teal", 13)
    f.box(716, top + 70, 200, 60, "cerrar(ahora, guardar, avisar)", "navy", 13, bold=True)
    f.arrow([(656, top + 76), (716, top + 90)])
    f.arrow([(656, top + 140), (716, top + 112)])
    for i, label in enumerate(["ahora (argumento)", "guardar (argumento)", "avisar (argumento)"]):
        bx = 486 + i * 143
        f.box(bx, top + 196, 137, 46, label, "gold", 13)
        f.arrow([(bx + 68, top + 196), (816, top + 130)], dashed=True)
    return _kit_finish(f, top + 262,
                       "Cada nombre libre es una costura que una prueba debe reemplazar o soportar. La función original no se puede ejecutar sin una base, un reloj y un servidor de correo; la versión refactorizada se prueba con valores. La medida cuenta dependencias en el código, no la calidad del diseño.",
                       "teal", SINT)


def se362_mutantes() -> Fig:
    etiquetas = {100.0: "100 %", 56.25: "9 de 16", 81.25: "13 de 16"}
    return grouped_bars(
        "Dos baterías sobre la misma función de nota: ambas ejecutan todas las líneas",
        "Barras agrupadas: la batería de cinco casos típicos y la de catorce casos con fronteras ejecutan el 100 por ciento de las líneas, pero la primera mata 9 de 16 mutantes (56 por ciento) y la segunda 13 de 16 (81 por ciento); entre los tres que sobreviven hay uno equivalente y dos que señalan casos sin probar.",
        ["5 casos típicos", "14 casos con fronteras"],
        [("Líneas ejecutadas", [100.0, 100.0], "grey"), ("Mutantes muertos (de 16)", [56.25, 81.25], "teal")],
        unit="% de las líneas ejecutadas, % de los 16 mutantes muertos", value_fmt=lambda v: etiquetas[v], ticks=[0, 25, 50, 75, 100],
        note="Las dos baterías tienen la misma cobertura de líneas y detectan cantidades muy distintas de cambios. Con las fronteras sobreviven un mutante equivalente (el tope 7,0 nunca se alcanza porque el factor no supera 1) y dos reales: el borde 0 frente a 1 hora de atraso y los decimales del redondeo, que ningún caso distingue.",
        note_kind="coral", foot=SINT)


def se362_reloj() -> Fig:
    return grouped_bars(
        "Una prueba de plazos con el reloj real y con el reloj como parámetro (10 000 ejecuciones simuladas)",
        "Barras horizontales con los fallos de la misma prueba de plazos en 10 000 ejecuciones simuladas: con el reloj real y un margen de 1 s falla 173 veces por pausas ocasionales; con la hora inyectada y cinco casos de frontera no falla ninguna.",
        ["Reloj real, margen de 1 s entre construir el plazo y comprobar", "Reloj inyectado, 5 casos de frontera (−1 s, 0, +1 s, +24 h, +24 h 1 s)"],
        [("Fallos en 10 000 ejecuciones", [173.0, 0.0], "coral")],
        unit="fallos en 10 000 ejecuciones (1,73 % frente a 0 %)", horizontal=True, label_w=330, decimals=0,
        note="El 1,73 % viene de un modelo del autor (3 de cada 100 ejecuciones sufren una pausa de 0,5 a 3 s), no de una medición del equipo. La lección es el mecanismo: una prueba que depende de cuánto tarda la máquina falla a veces sin que haya un defecto, y con la hora inyectada la hora deja de ser una variable.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-423
def se363_matriz() -> Fig:
    return grouped_bars(
        "Cuántos de los seis cambios que rompen al panel detecta cada prueba (de ocho cambios del proveedor)",
        "Barras agrupadas: de ocho cambios del proveedor, seis rompen al panel; el doble escrito a mano no detecta ninguno, el contrato del consumidor cinco, la prueba contra la respuesta real los seis y la comparación del esquema completo uno, con una falsa alarma por el campo extra.",
        ["Doble escrito a mano", "Contrato del consumidor", "Prueba contra la respuesta real", "Esquema completo"],
        [("Cambios que rompen y la prueba detecta", [0, 5, 6, 1], "teal"), ("Falsa alarma", [0, 0, 0, 1], "coral")],
        unit="cambios del proveedor (de 8)", decimals=0, ticks=[0, 2, 4, 6, 8], ref_lines=[(6, "6 cambios rompen al panel")],
        note="El contrato no detecta el orden invertido porque no lo declara, y la prueba contra la respuesta real lo ve porque el panel espera un orden. Un contrato solo protege lo que afirma. Los ocho cambios son construcciones del autor sobre una respuesta JSON y una base SQLite en memoria.",
        note_kind="teal", foot=SINT)


def se363_dirigidos() -> Fig:
    cambios = ["Quitar «creada»", "Renombrar «nota»", "Cambiar el tipo de «id»", "Quitar «estado»", "Cambiar «estudiante»",
               "Cambiar el tipo de «creada»", "Quitar «pagina»", "Renombrar «total»", "Quitar «revisor», que no existe", "Añadir un campo"]
    return grouped_bars(
        "Diez cambios del proveedor: alarma del esquema completo frente a consumidores realmente afectados",
        "Barras horizontales para diez cambios: el diff de esquema completo da alarma en ocho, pero en «pagina» y «total» ningún consumidor se rompe; los cambios que sí rompen afectan a entre uno y tres de los tres consumidores, y los contratos por consumidor dicen cuáles.",
        cambios,
        [("Consumidores afectados (de 3)", [1, 2, 1, 2, 3, 1, 0, 0, 0, 0], "teal"), ("Alarma del diff completo (1 = sí)", [1, 1, 1, 1, 1, 1, 1, 1, 0, 0], "gold")],
        unit="consumidores afectados · alarmas del diff", horizontal=True, label_w=250, decimals=0, ticks=[0, 1, 2, 3],
        note="El diff de esquema acierta siempre que hay un consumidor afectado y señala dos cambios que nadie usa (la barra dorada sin barra verde). Los contratos por consumidor no los señalan, y además dicen a quién avisar. Para que funcione, cada consumidor debe declarar los campos que lee: el contrato incompleto produce un falso sentimiento de seguridad.",
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


# ---------------------------------------------------------------- SE-424
def se364_pasos() -> Fig:
    pasos = [3, 8, 15, 30]
    datos = [("0,1 % por paso", [99.7, 99.3, 98.4, 97.0], "teal"), ("0,5 % por paso", [98.5, 96.1, 92.5, 85.7], "navy"),
             ("1 % por paso", [96.7, 92.3, 86.1, 73.5], "gold"), ("2 % por paso", [94.2, 85.3, 73.8, 55.3], "coral")]
    return line_chart(
        "Porcentaje de ejecuciones limpias de un recorrido según su cantidad de pasos y la inestabilidad de cada paso",
        "Cuatro líneas descendentes, una por inestabilidad por paso: con 0,1 por ciento el recorrido de 30 pasos pasa limpio 97,0 por ciento de las veces; con 2 por ciento pasa solo 55,3 por ciento, y la caída se acelera con la longitud.",
        [(n, [(p, v) for p, v in zip(pasos, vals)], k) for n, vals, k in datos],
        x_label="Pasos del recorrido", y_label="Ejecuciones limpias (%)", x_ticks=[(p, str(p)) for p in pasos], decimals=1, point_labels="last", y_zero=False,
        note="El resultado sigue (1 − q)^k: un paso inestable no se nota y treinta sí. Una suite de 20 recorridos de 15 pasos con 0,5 % por paso (simulación: 22,45 %; teoría: 22,2 %) pasa limpia una de cada cuatro veces. Los porcentajes son de una simulación con semilla fija, no de un sistema.",
        note_kind="coral", foot=SINT)


def se364_cobertura() -> Fig:
    ks = [1, 2, 3, 5, 8]
    return line_chart(
        "Tráfico y riesgo cubiertos por k recorridos de hasta tres rutas (20 000 sesiones sintéticas, 25 rutas)",
        "Cuatro curvas crecientes con el número de recorridos: el tráfico cubierto sube de 48 a 98 por ciento con ocho recorridos; con cinco, elegir por tráfico por impacto cubre 93,7 por ciento del riesgo frente a 89,6 por ciento al elegir solo por tráfico.",
        [("Tráfico cubierto, elegido por tráfico", list(zip(ks, [48.3, 64.9, 74.9, 87.6, 98.0])), "grey"),
         ("Riesgo cubierto, elegido por tráfico", list(zip(ks, [45.1, 71.1, 77.8, 89.6, 98.5])), "navy"),
         ("Tráfico cubierto, elegido por tráfico × impacto", list(zip(ks, [46.0, 59.0, 71.6, 86.7, 97.8])), "gold"),
         ("Riesgo cubierto, elegido por tráfico × impacto", list(zip(ks, [55.5, 72.0, 82.6, 93.7, 99.5])), "teal")],
        x_label="Recorridos elegidos (k)", y_label="Cobertura (%)", x_ticks=[(k, str(k)) for k in ks], decimals=1, point_labels="none",
        annotations=[(5, 93.7, "93,7 % (× impacto)", -110, -30), (5, 89.6, "89,6 % (solo tráfico)", 40, 46)],
        note="Cinco recorridos cubren el 87 % del tráfico y el 90 % del riesgo; los ocho siguientes aportan menos. Elegir por tráfico multiplicado por impacto cede 1 punto de tráfico y gana 4 de riesgo con cinco recorridos. Las rutas, su frecuencia (Zipf 1,1) y sus impactos son supuestos del autor.",
        note_kind="teal", foot=SINT)


def se364_instantanea() -> Fig:
    return grouped_bars(
        "Instantánea del HTML frente a aserciones semánticas, sobre 7 cambios benignos y 9 defectos",
        "Barras agrupadas: la instantánea exacta da alarma en los siete cambios benignos y detecta los nueve defectos; las aserciones semánticas no dan alarma en ninguno de los benignos y detectan seis de nueve, sin ver el botón deshabilitado, la lista oculta ni el texto con el color del fondo.",
        ["Falsas alarmas (de 7 cambios benignos)", "Defectos detectados (de 9)"],
        [("Instantánea exacta", [7, 9], "gold"), ("Aserciones semánticas", [0, 6], "teal")],
        unit="cambios o defectos", decimals=0, ticks=[0, 3, 6, 9],
        note="Si el equipo aprueba cada diferencia de la instantánea sin leerla, acepta los nueve defectos con la misma facilidad que los siete cambios benignos. Las aserciones semánticas no ven lo que está en atributos de estilo. Hace falta una comprobación de lo visual aparte; esta figura no la mide.",
        note_kind="gold", foot=SINT)


# ---------------------------------------------------------------- SE-425
def se365_hasta_el_fallo() -> Fig:
    return grouped_bars(
        "Cuatro versiones defectuosas de «repartir n entregas entre k correctores»: cuántas semillas detectan el defecto",
        "Barras horizontales con el porcentaje de semillas (de 100) que detectan cada defecto: cinco ejemplos escritos a mano detectan solo uno de los cuatro; las propiedades con generador uniforme detectan los cuatro, uno de ellos solo en 87 de 100; un generador con 30 por ciento de casos cerca de la frontera los detecta en las 100.",
        ["Olvida el resto", "Resto al último corrector", "Falla solo si hay menos entregas que correctores", "Pierde una entrega si n ≥ 500"],
        [("5 ejemplos (determinista)", [100.0, 0.0, 0.0, 0.0], "coral"), ("Propiedades, generador uniforme", [100.0, 100.0, 87.0, 100.0], "gold"),
         ("Con 30 % de casos cerca de la frontera", [100.0, 100.0, 100.0, 100.0], "teal")],
        unit="% de las 100 semillas que detectan el defecto", horizontal=True, label_w=300, decimals=0, ticks=[0, 25, 50, 75, 100],
        note="Las propiedades son longitud igual a k, suma igual a n, diferencia máxima de 1 y ninguna cantidad negativa. El defecto que solo ocurre con n < k aparece en el 1 % de los casos uniformes y por eso necesita más casos: la calidad del generador es parte de la prueba. Los ejemplos son deterministas: detectan o no.",
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


# ---------------------------------------------------------------- SE-426
def se366_puntuacion() -> Fig:
    return grouped_bars(
        "Cobertura de líneas y puntuación de mutación de cuatro baterías sobre el mismo módulo (18 mutantes)",
        "Barras agrupadas: de la batería A a la B la cobertura de líneas sube de 72,2 a 94,4 por ciento y los mutantes muertos se quedan en 61,1 por ciento (11 de 18); la C llega a 100 por ciento de líneas y 94,4 por ciento de mutantes muertos; la D cubre 66,7 por ciento de líneas con una sola prueba sin aserciones y mata 33,3 por ciento.",
        ["A: 3 casos del camino feliz", "B: A + 4 rechazos de formato", "C: B + bordes y exclusiones", "D: una prueba sin aserciones"],
        [("Líneas ejecutadas", [72.2, 94.4, 100.0, 66.7], "grey"), ("Mutantes muertos (de 18)", [61.1, 61.1, 94.4, 33.3], "teal")],
        unit="% de las líneas · % de los 18 mutantes", decimals=1, ticks=[0, 25, 50, 75, 100],
        note="La batería B añade 22 puntos de cobertura y 0 mutantes muertos. La D alcanza dos tercios de las líneas sin una sola aserción. El único superviviente de C cambia el redondeo de 1 a 2 decimales y ningún promedio de los casos lo distingue. Las baterías y los 18 mutantes son del autor; ninguno es equivalente.",
        note_kind="coral", foot=SINT)


def se366_fuzzing() -> Fig:
    return grouped_bars(
        "Cuatro defectos escondidos en un analizador: semillas (de 20) que los hallan con 20 000 entradas",
        "Barras horizontales: los bytes aleatorios no hallan ninguno de los cuatro defectos; el generador estructurado con valores límite los halla en las 20 semillas con medianas de 31 a 101 entradas; el guiado por cobertura los halla en 15 a 20 semillas con medianas de 210 a 6 826 entradas.",
        ["Nombre de más de 30 caracteres", "Nombre vacío con nota 7,0", "Identificador > 99 999 y estado anulada", "Nota «nan» o «inf»"],
        [("Bytes aleatorios", [0, 0, 0, 0], "coral"), ("Estructurado con valores límite", [20, 20, 20, 20], "teal"), ("Guiado por cobertura", [20, 15, 16, 20], "gold")],
        unit="semillas (de 20) que hallan el defecto", horizontal=True, label_w=270, decimals=0, ticks=[0, 5, 10, 15, 20],
        note="Las cadenas aleatorias casi nunca forman cuatro campos con un identificador numérico, así que nunca llegan al código que falla. El generador estructurado conoce los valores límite del formato, y ese conocimiento es del autor: el resultado muestra el mecanismo y no la tasa de hallazgo de una herramienta real. Las medianas de entradas están en la tabla.",
        note_kind="gold", foot=SINT)


def se366_supervivientes() -> Fig:
    f, y = _kit_start("Los casos que le faltan a la batería B: cuatro caen justo sobre un límite de la nota",
                      "Recta de la nota de 0,5 a 7,5 con la zona aceptada entre 1,0 y 7,0 y cuatro casos que matan mutantes de los límites y que la batería B no usa: 0,9 y 7,1 deben rechazarse; 1,0 y 7,0 deben aceptarse. Debajo, los otros dos casos que faltan: una anulada con nota entre válidas y un promedio de tres notas como 5,33.",
                      940, None)
    x0, x1 = 60.0, 880.0
    def px(v: float) -> float:
        return x0 + (v - 0.5) / 7.0 * (x1 - x0)
    base = y + 96
    f.box(px(1.0), base - 22, px(7.0) - px(1.0), 44, "Nota aceptada: de 1,0 a 7,0", "teal", 14, bold=True)
    for v in [0.5, 1, 2, 3, 4, 5, 6, 7]:
        f.line(px(v), base + 26, px(v), base + 34, "#5b7280")
        f.text(px(v), base + 52, str(v).replace(".", ",").replace(",0", ""), 13, "middle", 400, "#5b7280")
    f.line(x0, base + 26, x1, base + 26, "#5b7280")
    f.text((x0 + x1) / 2, base + 72, "Nota ingresada", 13, "middle", 400, "#5b7280")
    casos = [(0.9, "0,9 debe rechazarse", "coral", 10), (1.0, "1,0 debe aceptarse", "gold", 195),
             (7.0, "7,0 debe aceptarse", "gold", 560), (7.1, "7,1 debe rechazarse", "coral", 745)]
    for v, label, kind, bx in casos:
        by = base - 94
        f.box(bx, by, 175, 36, label, kind, 13, bold=True)
        f.arrow([(bx + 88, by + 36), (px(v), base - 22)], "")
    f.box(60, base + 96, 400, 56, "Anulada con nota 2,0 entre entradas válidas (mata «and» por «or» al excluir anuladas)", "navy", 13)
    f.box(480, base + 96, 400, 56, "Promedio de tres notas, como 5,33 (mata el cambio de redondeo de 1 a 2 decimales)", "navy", 13)
    return _kit_finish(f, base + 164,
                       "Un mutante superviviente es una pregunta, no un veredicto: o falta un caso o el mutante es equivalente y no hay nada que probar. Aquí ninguno es equivalente, de modo que cada uno señala una prueba concreta que falta; los dos del límite inferior cuentan como una misma causa. La tabla de la clase da la causa de cada superviviente.",
                       "teal", SINT)


FIGURES = {
    "se-421-presupuesto-de-pruebas-por-estrategia.svg": se361_presupuesto,
    "se-421-sensibilidad-a-las-estimaciones.svg": se361_sensibilidad,
    "se-421-niveles-de-prueba-y-clases-de-fallo.svg": se361_niveles,
    "se-422-dependencias-ocultas-de-una-funcion.svg": se362_costuras,
    "se-422-cobertura-y-mutantes-muertos.svg": se362_mutantes,
    "se-422-reloj-real-frente-a-reloj-inyectado.svg": se362_reloj,
    "se-423-cambios-del-proveedor-y-pruebas.svg": se363_matriz,
    "se-423-contratos-por-consumidor.svg": se363_dirigidos,
    "se-423-localizar-un-defecto-de-interfaz.svg": se363_localizacion,
    "se-424-inestabilidad-por-pasos.svg": se364_pasos,
    "se-424-recorridos-criticos-elegidos.svg": se364_cobertura,
    "se-424-instantanea-o-aserciones.svg": se364_instantanea,
    "se-425-casos-hasta-el-primer-fallo.svg": se365_hasta_el_fallo,
    "se-425-reduccion-de-contraejemplos.svg": se365_reduccion,
    "se-425-secuencias-contra-un-modelo.svg": se365_modelo,
    "se-426-cobertura-frente-a-mutacion.svg": se366_puntuacion,
    "se-426-fuzzing-de-un-analizador.svg": se366_fuzzing,
    "se-426-mutantes-que-sobreviven.svg": se366_supervivientes,
}
