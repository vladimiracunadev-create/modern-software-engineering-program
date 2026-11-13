"""Figures for SE-151 to SE-156 (synthetic data, fixed seeds; identical on Windows CPython 3.12.9 and Ubuntu/WSL2 CPython 3.12.3 unless a timing is shown)."""
from __future__ import annotations

from figure_kit import Fig
from figures_part07_a import bars, tab
from figures_part10_a import SINT, intervals


# ---------------------------------------------------------------- SE-151
def se151_densidad() -> Fig:
    rows = [["2 % / 4 %", "123", "11", "27", "2,8", "9"], ["4 % / 6 %", "193", "4", "14", "5,5", "15"], ["8 % / 10 %", "382", "0", "0", "17,1", "31"]]
    return tab("Matriz de trazabilidad sintética (40 requisitos, 60 pruebas, 30 módulos): densidad de enlaces e impacto",
               "Tabla con tres densidades de enlaces entre requisitos, pruebas y módulos: con 123 enlaces hay 11 requisitos sin prueba y 27 pruebas sin requisito y el impacto medio de un cambio es 2,8 elementos; con 382 enlaces no hay huérfanos pero el impacto medio es 17,1 y el máximo 31.",
               ["Probabilidad de enlace (req–prueba / prueba–módulo)", "Enlaces", "Requisitos sin prueba", "Pruebas sin requisito", "Impacto medio", "Impacto máximo"],
               rows, [300, 110, 150, 150, 120, 130], row_h=40, size=13,
               note="Más enlaces eliminan huérfanos pero también hacen que casi cualquier cambio toque casi todo: un enlace por si acaso vuelve inútil el análisis de impacto. La trazabilidad útil es la mínima que responde preguntas concretas.", note_kind="gold", foot=SINT)


def se151_deterioro() -> Fig:
    rows = [["1 % por sprint", "95,1 %", "90,4 %", "81,8 %", "66,9 %"], ["3 % por sprint", "85,9 %", "73,7 %", "54,4 %", "29,6 %"], ["5 % por sprint", "77,4 %", "59,9 %", "35,8 %", "12,9 %"]]
    return tab("Fracción de enlaces manuales todavía correctos tras 5, 10, 20 y 40 sprints",
               "Tabla de enlaces de trazabilidad mantenidos a mano que siguen siendo correctos si cada sprint se degrada una fracción: con 1 por ciento queda 66,9 por ciento tras 40 sprints, con 3 por ciento 29,6 y con 5 por ciento 12,9.",
               ["Degradación", "5 sprints", "10 sprints", "20 sprints", "40 sprints"], rows, [260, 160, 160, 160, 160], row_h=40, size=13,
               note="El cálculo es (1−p)^sprints. En un verificador sintético con 10 requisitos, una etiqueta REQ-nnn en las pruebas detectó 1 enlace colgante y 6 requisitos sin prueba, pero también dejó fuera dos pruebas bien intencionadas por escribir «req-005» y «REQ-0006».", note_kind="coral", foot="Los porcentajes de degradación son hipótesis del autor; el verificador se ejecutó sobre un proyecto temporal con defectos inyectados.")


def se151_derivada() -> Fig:
    rows = [["T1 tarifa(0)", "tarifa", "R1"], ["T2 tarifa(5)", "tarifa", "R2"], ["T3 total(5, docente)", "exento, total", "R3"],
            ["T4 comprobante(10, estudiante)", "comprobante, exento, formato, tarifa, total", "R4"], ["T5 exento(estudiante)", "exento", "R3"]]
    return tab("Trazabilidad derivada: qué funciones toca realmente cada prueba (sys.settrace)",
               "Tabla de cinco pruebas con las funciones que ejecutan según un trazador: T1 y T2 solo tarifa, T3 exento y total, T4 cinco funciones y T5 exento; la prueba declarada de R4 toca también cuatro funciones de otros requisitos.",
               ["Prueba", "Funciones ejecutadas", "Requisito declarado"], rows, [320, 460, 170], row_h=40, size=13,
               note="El enlace declarado y el observado coinciden en R1–R3. T4 verifica el comprobante, pero un fallo en tarifa también la rompe: la prueba está acoplada a cuatro requisitos más. Ejecutar una función no prueba que se haya verificado su comportamiento.", note_kind="gold", foot="Medido con sys.settrace en CPython 3.12.9 (Windows) y 3.12.3 (Ubuntu); solo cuenta llamadas a funciones del módulo bajo prueba.")


# ---------------------------------------------------------------- SE-152
def se152_retencion() -> Fig:
    items = [("«>=» en vez de «>»", 10, "gold", "10 borrados de más"), ("Ignora la retención de 730 días", 1473, "coral", "1 473 de más"), ("Ignora la retención legal", 39, "coral", "39 de más"),
             ("«12 meses» como 360 días", 83, "gold", "83 de más"), ("Desfase de un día por zona horaria", 14, "gold", "14 retenidos de más")]
    return bars("Purga por retención en 10 000 registros sintéticos: cuántos se tratan mal según la variante",
                "Barras de errores sobre 3907 registros que debían purgarse y 104 con retención legal: usar mayor o igual borra 10 de más; ignorar la retención de 730 días borra 1473; ignorar la retención legal borra 39; contar 12 meses como 360 días borra 83; un desfase de un día retiene 14 de más.",
                items, 0.3, "Cada variante parece correcta en una lectura rápida. Ignorar el caso de 730 días borra 1 473 registros que aún debían conservarse; ignorar la retención legal borra 39 que estaban bajo retención. Con un desfase de un día el error es de signo contrario: retiene datos que debían borrarse.",
                label_w=340, width=1000, note_kind="coral", foot=SINT)


def se152_stride() -> Fig:
    rows = [["Entidad externa", "3", "S, R", "6"], ["Proceso", "4", "S, T, R, I, D, E", "24"], ["Almacén de datos", "3", "T, R, I, D", "12"], ["Flujo de datos", "8", "T, I, D", "24"], ["Total", "18", "—", "66 de 108"]]
    return tab("STRIDE por elemento en un diagrama de flujo de datos sintético con 18 elementos",
               "Tabla de amenazas aplicables por tipo de elemento: 3 entidades externas con 2 categorías, 4 procesos con 6, 3 almacenes con 4 y 8 flujos con 3 suman 66 celdas de amenaza de las 108 posibles.",
               ["Tipo de elemento", "Cantidad", "Categorías aplicables", "Celdas a revisar"], rows, [250, 140, 340, 200], row_h=38, size=13,
               note="El mapa por elemento reduce 108 preguntas a 66, pero 66 sigue siendo una lista larga: cada celda debe terminar en un requisito, una aceptación explícita del riesgo o una nota de «no aplica». Una celda sin decisión es un requisito de seguridad que nadie escribió.", note_kind="gold", foot="Conteo aritmético con la tabla STRIDE por elemento de Microsoft; los números de elementos son un ejemplo del autor.")


def se152_cadena() -> Fig:
    rows = [["Modificar la entrada 40", "Sí, en la 40"], ["Borrar la entrada 40", "Sí, en la 40"], ["Truncar el final (quedan 70 de 100)", "No"],
            ["Reconstruir toda la cadena sin la entrada 40", "No"], ["Reconstruir y comparar con el último hash guardado fuera", "Sí: el hash final no coincide"]]
    return tab("Registro encadenado con SHA-256: qué manipulaciones detecta la verificación",
               "Tabla de cinco manipulaciones de un registro de auditoría de 100 entradas encadenadas por hash: modificar y borrar una entrada se detectan; truncar el final y reconstruir toda la cadena no; con un hash final guardado fuera de la cadena la reconstrucción se detecta.",
               ["Manipulación", "¿La verificación la detecta?"], rows, [520, 400], row_h=40, size=13,
               kinds=["plain", ("teal", "teal", "coral", "coral", "teal")],
               note="La cadena prueba continuidad, no autoría ni totalidad. «Registro inalterable» como requisito debe decir qué ancla externa (almacén de solo anexar, sello de tiempo, copia en otro dominio) hace detectables el truncado y la reconstrucción.", note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-153
def se153_alcance() -> Fig:
    rows = [["4 %", "18", "0,7", "4", "17 de 30"], ["8 %", "38", "3,2", "13", "8 de 30"], ["15 %", "76", "4,9", "17", "6 de 30"]]
    return tab("Alcance transitivo de un cambio en 30 requisitos sintéticos según la densidad de dependencias",
               "Tabla de tres densidades de dependencias entre 30 requisitos: con 18 aristas un cambio afecta en media a 0,7 requisitos dependientes y como máximo a 4; con 76 aristas, a 4,9 y como máximo a 17; los cambios sin dependientes bajan de 17 a 6.",
               ["Probabilidad de dependencia", "Aristas", "Dependientes medios", "Máximo", "Cambios sin dependientes"], rows, [250, 120, 200, 130, 220], row_h=40, size=13,
               note="El coste de un cambio depende más de su posición en el grafo que de su tamaño textual: un requisito raíz con 17 dependientes transitivos es una decisión de línea base; uno sin dependientes es un ajuste local.", note_kind="gold", foot=SINT)


def se153_hash() -> Fig:
    rows = [["Espacio al final de cada fila", "Cambia", "No cambia"], ["Saltos de línea CRLF", "Cambia", "No cambia"], ["Columnas realineadas", "Cambia", "No cambia"],
            ["Tabulador en lugar de espacio", "Cambia", "No cambia"], ["30 s → 60 s", "Cambia", "Cambia"], ["Estado aprobado → borrador", "Cambia", "Cambia"]]
    return tab("Hash de una línea base: texto crudo frente a texto normalizado (6 ediciones)",
               "Tabla con seis ediciones de una tabla de requisitos: cuatro de formato cambian el hash del texto crudo pero no el normalizado; cambiar 30 s por 60 s y cambiar el estado cambian ambos.",
               ["Edición", "Hash del texto crudo", "Hash normalizado"], rows, [380, 270, 260], row_h=38, size=13,
               kinds=["plain", ("coral", "coral", "coral", "coral", "teal", "teal"), ("teal", "teal", "teal", "teal", "teal", "teal")],
               note="Un hash crudo da falsas alarmas de cambio; uno normalizado detecta cambios de contenido, pero también puede ocultar uno que importe (un espacio dentro de un identificador). La normalización es parte del contrato de la línea base y debe escribirse.", note_kind="gold", foot=SINT)


def se153_comite() -> Fig:
    rows = [["Cada 0,2 semanas", "0,10", "0,19", "1,2"], ["Cada semana", "0,50", "0,95", "6,0"], ["Cada 2 semanas", "0,99", "1,90", "12,0"], ["Cada 4 semanas", "1,97", "3,79", "23,9"]]
    return tab("Comité de cambios: espera de una solicitud según la cadencia (6 solicitudes por semana)",
               "Tabla de la espera de solicitudes de cambio con llegadas de 6 por semana: reunirse cada 0,2 semanas da espera media 0,10 y p95 0,19; cada semana 0,50 y 0,95; cada 2 semanas 0,99 y 1,90; cada 4 semanas 1,97 y 3,79, con 23,9 solicitudes por reunión.",
               ["Cadencia", "Espera media (semanas)", "Espera p95 (semanas)", "Solicitudes por reunión"], rows, [250, 250, 230, 200], row_h=40, size=13,
               note="La espera media es la mitad del periodo, y la carga por reunión crece con él: a las cuatro semanas el comité revisa 24 solicitudes de una vez. La cadencia es una decisión de costo y estabilidad, no una convención de calendario.", note_kind="gold", foot="Llegadas de Poisson sintéticas con semilla 1530; la tasa de 6 por semana es un supuesto del autor.")


# ---------------------------------------------------------------- SE-154
def se154_lecturas() -> Fig:
    items = [("3 operandos (A y B o C)", 2, "teal", "2 lecturas"), ("4 operandos", 5, "teal", "5"), ("5 operandos", 14, "gold", "14"), ("6 operandos", 42, "coral", "42"), ("7 operandos", 132, "coral", "132")]
    return bars("Lecturas posibles de una frase con y/o sin paréntesis (números de Catalan)",
                "Barras con el número de formas de agrupar una frase con conectores y y o: 2 con tres operandos, 5 con cuatro, 14 con cinco, 42 con seis y 132 con siete; la frase A y B o C se lee de dos maneras que difieren en 2 de 8 estados.",
                items, 4, "«A y B o C» tiene dos lecturas que dan resultados distintos en 2 de los 8 estados. Con cinco operandos mezclados (A y B o C y D o E) hay 14 lecturas y 10 funciones lógicas distintas: la ambigüedad estructural no se resuelve «leyendo con cuidado».",
                label_w=300, width=940, note_kind="coral", foot="Cálculo exacto; idéntico en Windows y Ubuntu.")


def se154_conflictos() -> Fig:
    rows = [["Q4, Q8, Q9", "3", "Sin conexión no sincroniza; sincroniza siempre; opera sin conexión"], ["Q5, Q6, Q7", "3", "Retiene 30 días; borra al salir; borrar al salir impide retener"],
            ["Q1, Q6, Q7, Q12", "4", "Guarda automático; borra al salir; borrar impide retener; guardar implica retener"],
            ["Q2, Q4, Q9, Q10", "4", "Cifrado; sin conexión no sincroniza; opera sin conexión; cifrado implica sincronizar"],
            ["Q3, Q6, Q7, Q9, Q12", "5", "Opera sin conexión; sin conexión guarda; guardar implica retener; borra al salir; borrar impide retener"], ["Q4, Q5, Q9, Q10, Q11", "5", "Opera sin conexión y no sincroniza; retiene; retener implica cifrar; cifrar implica sincronizar"]]
    return tab("Doce requisitos y seis conflictos mínimos: ninguno es un par de contradicciones evidentes",
               "Tabla de los seis subconjuntos mínimos insatisfacibles de doce requisitos sobre seis variables: dos de tres requisitos, dos de cuatro y dos de cinco; el máximo subconjunto compatible tiene diez.",
               ["Subconjunto mínimo", "Tamaño", "Por qué no pueden cumplirse a la vez"], rows, [200, 100, 620], row_h=48, size=13,
               note="Quitar los requisitos Q9 y Q7 resuelve los seis conflictos, y el máximo compatible es 10 de 12. Pero ningún par de ellos se contradice por sí solo: una revisión que compare requisitos de dos en dos no los verá. Es lógica proposicional exhaustiva, no una herramienta de producción.", note_kind="gold", foot=SINT)


def se154_celdas() -> Fig:
    items = [("Definidas en la especificación", 10, "teal", "10"), ("Imposibles por una regla escrita", 11, "gold", "11"), ("Preguntas abiertas", 21, "coral", "21")]
    return bars("Tabla estado–evento de una entrega: 6 estados × 7 eventos = 42 celdas",
                "Barras del estado de 42 celdas de una máquina de estados de una entrega: 10 definidas, 11 imposibles por una regla explícita y 21 preguntas abiertas, como qué ocurre al enviar una entrega ya enviada.",
                items, 20, "El borrador de especificación define 10 de 42 celdas. Las 21 preguntas abiertas incluyen casos reales: calificar una entrega solo «Enviada», retirar una entrega «En revisión», expirar sesión en cualquier estado posterior. Cada una es un requisito que alguien tendrá que inventar en código.",
                label_w=330, width=960, note_kind="coral", foot=SINT)


# ---------------------------------------------------------------- SE-155
def se155_puntaje() -> Fig:
    rows = [["10 requisitos no verificables", "10 de 10 bajo el umbral", "El puntaje promedio es 0,1 de 4 señales"], ["10 reparados por el autor", "8 de 10 sobre el umbral", "Dos fallan: «completará» y «redondeará» no están en la lista de verbos (puntajes 2 y 0)"],
            ["6 enunciados nuevos", "6 de 6 acertados", "Con casos escritos después de fijar la regla; muestra muy pequeña"]]
    return tab("Regla léxica de verificabilidad (4 señales, umbral 3) frente a 26 enunciados",
               "Tabla de una regla que puntúa cantidad con unidad, condición, estadístico o cota y respuesta observable: clasifica bien 10 de 10 enunciados vagos, 8 de 10 enunciados reparados y 6 de 6 enunciados nuevos.",
               ["Conjunto", "Resultado", "Lectura"], rows, [310, 230, 380], row_h=60, size=13,
               note="La regla no entiende nada: cuenta señales. Marcó como no verificable una reparación correcta («redondeará a un decimal con mitad hacia arriba… 25 casos») porque su vocabulario no incluye «redondeará». Sirve para mirar primero lo más vago, no para aprobar.", note_kind="gold", foot="Reglas y etiquetas escritas por el autor; seis casos nuevos no bastan para estimar una exactitud real.")


def se155_latencia() -> Fig:
    rows = [["1 cliente secuencial", "1,88–2,02 ms", "1,47–1,71 ms"], ["8 clientes concurrentes", "5,56–6,04 ms", "9,69–10,89 ms"]]
    return tab("Percentil 95 de 400 peticiones a un servidor local: tres corridas por escenario",
               "Tabla de tiempos de respuesta de un servidor HTTP en el mismo equipo: con un cliente el percentil 95 fue de 1,88 a 2,02 ms en Windows y de 1,47 a 1,71 ms en Ubuntu; con ocho clientes, de 5,56 a 6,04 y de 9,69 a 10,89.",
               ["Escenario (3 corridas de 400 peticiones)", "p95 en Windows 11", "p95 en Ubuntu (WSL2)"], rows, [420, 240, 260], row_h=44, size=13,
               note="Un requisito reparado («p95 ≤ 800 ms con 8 clientes») se verifica con un procedimiento, no con un adjetivo. Estas cifras son del bucle local de un solo equipo con un servidor trivial: ilustran el procedimiento, no el rendimiento de ningún sistema, y la variación entre corridas es parte del resultado.", note_kind="teal", foot="Medido con http.server y http.client en CPython 3.12.9 (Windows 11) y 3.12.3 (Ubuntu/WSL2); un solo equipo, red de bucle local.")


def se155_ceros() -> Fig:
    rows = [["1 por 100 (1e-2)", "299", "300"], ["1 por 1 000 (1e-3)", "2 995", "3 000"], ["1 por 10 000 (1e-4)", "29 956", "30 000"], ["1 por millón (1e-6)", "2 995 731", "3 000 000"]]
    return tab("Pruebas sin fallo necesarias para afirmar con 95 % de confianza que la tasa de fallo es menor que p",
               "Tabla de pruebas sin ningún fallo necesarias para acotar la tasa de fallo con 95 por ciento de confianza: 299 para 1 por ciento, 2995 para 1 por mil, 29956 para 1 por diez mil y 2995731 para 1 por millón; la regla de tres da 300, 3000, 30000 y 3000000.",
               ["Tasa máxima aceptada", "Pruebas sin fallo (exacto)", "Regla de tres (3/p)"], rows, [330, 300, 280], row_h=40, size=13,
               note="«El sistema nunca perderá datos» no se puede verificar con pruebas finitas. Con 100 pruebas sin fallos solo se puede afirmar que la tasa es menor que 3 %, y un sistema que falla 2 % de las veces pasa esas 100 pruebas en 12,8 % de las ocasiones.", note_kind="coral", foot="Cálculo exacto y simulación con semilla 155; idéntico en Windows y Ubuntu.")


# ---------------------------------------------------------------- SE-156
def se156_mutaciones() -> Fig:
    rows = [["Estructurales: id duplicado, criterio inexistente o ajeno, origen inexistente, sin dueño, prioridad inválida, dependencia inexistente, ciclo", "Detectadas (8 de 8)"],
            ["De completitud: sin supuestos, sin fuera de alcance, texto «por definir»", "Detectadas (3 de 3)"],
            ["Vocabulario: «adecuada» (la lista tiene «adecuado»)", "No detectada"],
            ["Semánticas: umbral 30 → 3 000 días; dos requisitos con plazos contradictorios; criterio que no prueba el requisito; ambigüedad sin palabras vagas", "No detectadas (0 de 4)"]]
    return tab("Validador de una especificación sintética con 16 defectos inyectados: 11 de 16 detectados",
               "Tabla de 16 mutaciones aplicadas a una especificación válida: el validador detecta las estructurales y de completitud (ocho y tres), pero no una palabra vaga flexionada ni las cuatro semánticas (umbral absurdo, contradicción entre dos requisitos, criterio ajeno y ambigüedad).",
               ["Tipo de defecto", "Resultado"], rows, [680, 240], row_h=60, size=13,
               kinds=["plain", ("teal", "teal", "gold", "coral")],
               note="La especificación base no produce errores. El validador comprueba forma y referencias; no compara 30 con 3 000 días, no sabe que dos plazos se excluyen y no distingue un criterio ajeno. Esa parte la cubre la revisión humana. Detectar 11 de 16 no es una probabilidad de que una especificación real esté bien.", note_kind="coral", foot=SINT)


def se156_camino() -> Fig:
    items = [("REQ-001 (5 días)", 5, "teal", "5"), ("REQ-003 (2 días, sin dependencias)", 2, "teal", "2"), ("REQ-002 (necesita REQ-001)", 8, "gold", "8"),
             ("REQ-005 (necesita REQ-001)", 8, "gold", "8"), ("REQ-004 (necesita REQ-001)", 9, "coral", "9, camino crítico")]
    return bars("Duración acumulada mínima de cinco requisitos con dependencias (costos supuestos en días)",
                "Barras del tiempo acumulado de cada requisito: REQ-001 5 días, REQ-003 2, REQ-002 8, REQ-005 8 y REQ-004 9; la suma secuencial es 17 días y el camino crítico 9, por REQ-001 seguido de REQ-004.",
                items, 40, "Con costos de 5, 3, 2, 4 y 3 días la suma secuencial es 17 y el camino crítico solo 9, porque tres requisitos pueden avanzar a la vez una vez terminado REQ-001. Una especificación que declara dependencias permite ese cálculo; una que no las declara no.",
                label_w=360, width=980, note_kind="teal", foot="Costos y dependencias de un ejemplo del autor; cálculo exacto.")


def se156_captura() -> Fig:
    items = [("Revisores independientes y defectos iguales", 30.0, 41.9, 60.0, "teal", "media 41,9"),
             ("Defectos de dificultad desigual", 23.1, 30.5, 39.6, "coral", "media 30,5")]
    return intervals("Estimar cuántos defectos quedan por captura-recaptura: dos revisores, 40 defectos reales",
                     "Gráfico de intervalos del estimador de Lincoln-Petersen sobre 40 defectos sembrados: con revisores independientes e igual dificultad la media es 41,9 con rango p5 a p95 de 30 a 60; con dificultad desigual, 30,5 con rango de 23,1 a 39,6, siempre por debajo de 40.",
                     items, 65, "defectos estimados",
                     note="Juntos, los dos revisores hallaron en media 28,0 y 25,4 defectos distintos de 40. Con dificultad igual el estimador es correcto en media pero impreciso (30 a 60). Con defectos difíciles para ambos, subestima: 30,5 frente a 40. Un número bajo de defectos restantes no es una garantía.", label_w=330, note_kind="gold", foot="3 000 simulaciones por escenario, semilla 156; probabilidades de detección 0,5 y 0,4 (supuestos del autor).")


FIGURES = {
    "se-151-densidad-de-enlaces-e-impacto.svg": se151_densidad,
    "se-151-deterioro-de-enlaces-manuales.svg": se151_deterioro,
    "se-151-trazabilidad-derivada-por-ejecucion.svg": se151_derivada,
    "se-152-errores-de-purga-por-retencion.svg": se152_retencion,
    "se-152-stride-por-elemento.svg": se152_stride,
    "se-152-cadena-de-hash-y-ancla-externa.svg": se152_cadena,
    "se-153-alcance-de-un-cambio.svg": se153_alcance,
    "se-153-hash-crudo-o-normalizado.svg": se153_hash,
    "se-153-cadencia-del-comite-de-cambios.svg": se153_comite,
    "se-154-lecturas-de-una-frase.svg": se154_lecturas,
    "se-154-conflictos-minimos.svg": se154_conflictos,
    "se-154-celdas-sin-definir.svg": se154_celdas,
    "se-155-regla-de-verificabilidad.svg": se155_puntaje,
    "se-155-latencia-en-bucle-local.svg": se155_latencia,
    "se-155-pruebas-sin-fallos.svg": se155_ceros,
    "se-156-validador-de-especificacion.svg": se156_mutaciones,
    "se-156-camino-critico.svg": se156_camino,
    "se-156-captura-recaptura.svg": se156_captura,
}
